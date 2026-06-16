"""
llm_client.py
=============
Async OpenRouter client (chat/completions) with:
  * exact cost tracking via OpenRouter's `usage.cost` (fallback: token x price), logged
    to logs/cost_log.jsonl AFTER EVERY CALL; SOFT_CAP ~$3 warning, HARD_CAP $10 -> HardStop.
  * bounded-concurrency (asyncio.Semaphore) for the many isolated scoring calls.
  * exponential-backoff retry on 429/5xx/timeouts/transient provider errors.
  * logprobs / top_logprobs support (probed available on openai/gpt-4.1-nano).
  * a persistent on-disk response cache (jsonl) keyed by the full request -> idempotent,
    resumable, and never double-charges across mini->pilot->full scaling.

All calls go through OpenRouter's endpoint (never a provider directly), per constraints.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
PRICES = {  # $/token (gpt-4.1-nano); used only as a fallback if usage.cost is absent
    "openai/gpt-4.1-nano": {"in": 0.10e-6, "out": 0.40e-6},
    "openai/gpt-4o-mini": {"in": 0.15e-6, "out": 0.60e-6},
}


class HardStop(Exception):
    """Raised when cumulative LLM cost crosses the hard cap -> STOP IMMEDIATELY."""


class CostTracker:
    def __init__(self, log_path: str, soft_cap: float = 3.0, hard_cap: float = 10.0):
        self.cumulative = 0.0
        self.n_calls = 0
        self.n_cache_hits = 0
        self.cached_tokens_total = 0
        self.soft_cap = soft_cap
        self.hard_cap = hard_cap
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self._soft_warned = False
        self._lock = asyncio.Lock()

    async def record(self, kind: str, usage: dict, model: str, cache_hit: bool):
        async with self._lock:
            cost = usage.get("cost")
            pin = usage.get("prompt_tokens", 0) or 0
            pout = usage.get("completion_tokens", 0) or 0
            cached = (usage.get("prompt_tokens_details") or {}).get("cached_tokens", 0) or 0
            if cost is None:
                pr = PRICES.get(model, PRICES["openai/gpt-4.1-nano"])
                cost = pin * pr["in"] + pout * pr["out"]
            if not cache_hit:  # cached responses cost nothing (already paid once)
                self.cumulative += float(cost)
                self.n_calls += 1
                self.cached_tokens_total += int(cached)
            else:
                self.n_cache_hits += 1
            rec = {"ts": round(time.time(), 3), "kind": kind, "in": pin, "out": pout,
                   "cached": int(cached), "call_cost": float(cost) if not cache_hit else 0.0,
                   "cum_cost": round(self.cumulative, 6), "cache_hit": cache_hit,
                   "n_calls": self.n_calls}
            with open(self.log_path, "a") as f:
                f.write(json.dumps(rec) + "\n")
            if self.cumulative > self.soft_cap and not self._soft_warned:
                self._soft_warned = True
                print(f"[COST] SOFT CAP ${self.soft_cap} crossed: cumulative ${self.cumulative:.4f}")
            if self.cumulative > self.hard_cap:
                raise HardStop(f"HARD CAP ${self.hard_cap} exceeded: ${self.cumulative:.4f}")


class LLMCache:
    """Persistent jsonl request->response cache. Key = md5 of the full request payload."""

    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.mem: dict[str, dict] = {}
        if self.path.exists():
            with open(self.path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        self.mem[rec["key"]] = rec["resp"]
                    except Exception:
                        continue
        self._lock = asyncio.Lock()

    @staticmethod
    def make_key(payload: dict, extra: str = "") -> str:
        blob = json.dumps(payload, sort_keys=True) + "||" + extra
        return hashlib.md5(blob.encode()).hexdigest()

    def get(self, key: str):
        return self.mem.get(key)

    async def put(self, key: str, resp: dict):
        async with self._lock:
            self.mem[key] = resp
            with open(self.path, "a") as f:
                f.write(json.dumps({"key": key, "resp": resp}) + "\n")


class LLM:
    def __init__(self, model: str, cost: CostTracker, cache: LLMCache,
                 concurrency: int = 12, max_retries: int = 6, timeout: float = 90.0):
        self.model = model
        self.cost = cost
        self.cache = cache
        self.sem = asyncio.Semaphore(concurrency)
        self.max_retries = max_retries
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.api_key = os.environ["OPENROUTER_API_KEY"]
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(timeout=self.timeout)
        return self

    async def __aexit__(self, *exc):
        if self._session:
            await self._session.close()

    async def chat(self, messages: list, kind: str, temperature: float = 0.0,
                   max_tokens: int = 16, logprobs: bool = False, top_logprobs: int = 0,
                   sample_idx: int = 0) -> dict:
        """One isolated chat call. Returns {content, first_token_top_logprobs(list of
        {token,logprob}), usage, cache_hit}. Cached by full request (sample_idx varies
        temperature>0 samples). max_tokens floored at 16 (OpenRouter provider minimum)."""
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max(16, max_tokens),
        }
        if logprobs:
            payload["logprobs"] = True
            payload["top_logprobs"] = top_logprobs
        key = self.cache.make_key(payload, extra=f"s{sample_idx}")
        cached = self.cache.get(key)
        if cached is not None:
            await self.cost.record(kind, cached.get("usage", {}), self.model, cache_hit=True)
            return {**cached, "cache_hit": True}

        async with self.sem:
            last_err = None
            for attempt in range(self.max_retries):
                try:
                    async with self._session.post(
                        OPENROUTER_URL,
                        headers={"Authorization": f"Bearer {self.api_key}",
                                 "Content-Type": "application/json"},
                        json=payload,
                    ) as r:
                        status = r.status
                        data = await r.json()
                        if status == 200 and "error" not in data:
                            parsed = self._parse(data)
                            await self.cache.put(key, parsed)
                            await self.cost.record(kind, parsed.get("usage", {}), self.model,
                                                   cache_hit=False)
                            return {**parsed, "cache_hit": False}
                        # provider/transient error -> maybe retry
                        last_err = data.get("error", data)
                        code = (last_err or {}).get("code", status) if isinstance(last_err, dict) else status
                        if status in (429, 500, 502, 503, 504) or status == 200:
                            await asyncio.sleep(min(2 ** attempt, 30) + 0.1 * attempt)
                            continue
                        raise RuntimeError(f"OpenRouter {status}: {last_err}")
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    last_err = repr(e)
                    await asyncio.sleep(min(2 ** attempt, 30) + 0.1 * attempt)
            raise RuntimeError(f"OpenRouter failed after {self.max_retries} retries: {last_err}")

    @staticmethod
    def _parse(data: dict) -> dict:
        ch = data["choices"][0]
        content = (ch.get("message") or {}).get("content") or ""
        top = []
        lp = ch.get("logprobs")
        if lp and lp.get("content"):
            first = lp["content"][0]
            top = [{"token": x["token"], "logprob": x["logprob"]}
                   for x in first.get("top_logprobs", [])]
        return {"content": content, "first_token_top_logprobs": top,
                "usage": data.get("usage", {}), "provider": data.get("provider")}
