#!/usr/bin/env python3
"""
llm_client.py — Async OpenRouter client with on-disk caching and exact cost tracking.

All LLM access in this experiment goes through OpenRouter. The client:
  * caches every (model, messages, params, sample_idx) response to disk so re-runs /
    resumes are free and partial progress survives interruptions;
  * tracks cumulative USD using OpenRouter's own `usage.cost` field (exact, per-call),
    appends a cost record after EVERY live call, and HARD-STOPS at $10;
  * exposes a single async `call()` coroutine guarded by a concurrency semaphore with
    tenacity retries + backoff for transient failures.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import math
import os
import time
from pathlib import Path

import aiohttp
from loguru import logger
from tenacity import (retry, retry_if_exception_type, stop_after_attempt,
                      wait_exponential)

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HARD_STOP_USD = 10.0


class BudgetExceeded(RuntimeError):
    pass


class TransientLLMError(RuntimeError):
    pass


class OpenRouterClient:
    def __init__(self, cache_dir: Path, cost_log: Path, concurrency: int = 28,
                 soft_cap_usd: float = 1.5, hard_stop_usd: float = HARD_STOP_USD,
                 timeout_s: int = 90, fallback_cache_dirs: list | None = None):
        self.api_key = os.environ.get("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise RuntimeError("OPENROUTER_API_KEY not set in environment")
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        # Read-only warm-start caches (e.g. a prior experiment's cache/). On a primary
        # miss we look here BEFORE spending money; a hit is promoted into cache_dir so
        # later runs find it locally. Identical sha256(payload+sample_idx) key scheme.
        self.fallback_cache_dirs = [Path(p) for p in (fallback_cache_dirs or [])]
        self.n_calls_fallback = 0
        self.cost_log = Path(cost_log)
        self.cost_log.parent.mkdir(parents=True, exist_ok=True)
        self.sem = asyncio.Semaphore(concurrency)
        self.soft_cap = soft_cap_usd
        self.hard_stop = hard_stop_usd
        self.timeout = aiohttp.ClientTimeout(total=timeout_s)
        self.cost_usd = 0.0
        self.n_calls_live = 0
        self.n_calls_cached = 0
        self.cached_tokens_observed = 0
        self._cost_lock = asyncio.Lock()
        self._soft_warned = False
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(timeout=self.timeout)
        return self

    async def __aexit__(self, *exc):
        if self._session:
            await self._session.close()

    # -- cache key / path -----------------------------------------------------
    def _key(self, payload: dict, sample_idx: int) -> str:
        blob = json.dumps(payload, sort_keys=True) + f"|s{sample_idx}"
        return hashlib.sha256(blob.encode()).hexdigest()

    def _path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    # -- cost bookkeeping -----------------------------------------------------
    async def _record_cost(self, cost: float, model: str, usage: dict):
        async with self._cost_lock:
            self.cost_usd += float(cost or 0.0)
            self.n_calls_live += 1
            ctd = (usage or {}).get("prompt_tokens_details") or {}
            self.cached_tokens_observed += int(ctd.get("cached_tokens", 0) or 0)
            rec = {"t": time.time(), "model": model, "cost": float(cost or 0.0),
                   "cum_usd": self.cost_usd, "usage": usage}
            with self.cost_log.open("a") as f:
                f.write(json.dumps(rec) + "\n")
            if self.cost_usd >= self.hard_stop:
                raise BudgetExceeded(
                    f"HARD STOP: cumulative spend ${self.cost_usd:.4f} >= ${self.hard_stop}")
            if self.cost_usd >= self.soft_cap and not self._soft_warned:
                self._soft_warned = True
                logger.warning(f"SOFT CAP reached: ${self.cost_usd:.4f} >= ${self.soft_cap}")

    # -- low-level POST with retry -------------------------------------------
    @retry(retry=retry_if_exception_type(TransientLLMError),
           stop=stop_after_attempt(5),
           wait=wait_exponential(multiplier=1.5, min=2, max=30), reraise=True)
    async def _post(self, payload: dict) -> dict:
        assert self._session is not None
        async with self.sem:
            try:
                async with self._session.post(
                    API_URL,
                    headers={"Authorization": f"Bearer {self.api_key}",
                             "Content-Type": "application/json"},
                    json=payload,
                ) as resp:
                    text = await resp.text()
                    if resp.status == 429 or resp.status >= 500:
                        raise TransientLLMError(f"status {resp.status}: {text[:200]}")
                    data = json.loads(text)
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                raise TransientLLMError(str(e))
            except json.JSONDecodeError as e:
                raise TransientLLMError(f"bad json: {e}")
        err = data.get("error")
        if err:
            msg = json.dumps(err)[:300]
            # provider-side rate/5xx wrapped inside 200 envelope -> retry
            code = err.get("code")
            if code in (429, 500, 502, 503, 520, 524) or "rate" in msg.lower():
                raise TransientLLMError(msg)
            raise RuntimeError(f"OpenRouter error: {msg}")
        return data

    # -- public call ----------------------------------------------------------
    async def call(self, model: str, messages: list[dict], *, max_tokens: int = 16,
                   temperature: float = 0.0, logprobs: bool = False,
                   top_logprobs: int = 0, seed: int | None = None,
                   sample_idx: int = 0) -> dict:
        """Return a normalised dict:
            {content, top_logprobs(list|None), cost, cached, cached_tokens, raw_usage}
        Uses disk cache; only cache-misses cost money / count toward the budget.
        """
        payload: dict = {"model": model, "messages": messages,
                         "max_tokens": max_tokens, "temperature": temperature}
        if logprobs:
            payload["logprobs"] = True
            payload["top_logprobs"] = top_logprobs
        if seed is not None:
            payload["seed"] = seed
        key = self._key(payload, sample_idx)
        cpath = self._path(key)
        if cpath.exists():
            try:
                cached = json.loads(cpath.read_text())
                self.n_calls_cached += 1
                cached["cached"] = True
                return cached
            except (json.JSONDecodeError, OSError):
                pass  # corrupt cache entry -> recompute
        # primary miss -> consult read-only warm-start caches; promote hits locally
        for fb in self.fallback_cache_dirs:
            fpath = fb / f"{key}.json"
            if fpath.exists():
                try:
                    cached = json.loads(fpath.read_text())
                except (json.JSONDecodeError, OSError):
                    continue
                self.n_calls_cached += 1
                self.n_calls_fallback += 1
                try:
                    cpath.write_text(json.dumps(cached))
                except OSError:
                    pass
                cached["cached"] = True
                return cached

        data = await self._post(payload)
        choice = (data.get("choices") or [{}])[0]
        msg = choice.get("message") or {}
        content = msg.get("content")
        usage = data.get("usage") or {}
        cost = usage.get("cost", 0.0)
        tlp = None
        lp = choice.get("logprobs")
        if lp and lp.get("content"):
            tlp = [{"token": tok.get("token"),
                    "top": [{"token": a.get("token"), "logprob": a.get("logprob")}
                            for a in (tok.get("top_logprobs") or [])]}
                   for tok in lp["content"][:4]]
        ctd = usage.get("prompt_tokens_details") or {}
        out = {"content": content, "top_logprobs": tlp, "cost": float(cost or 0.0),
               "cached": False, "cached_tokens": int(ctd.get("cached_tokens", 0) or 0),
               "raw_usage": {"prompt_tokens": usage.get("prompt_tokens"),
                             "completion_tokens": usage.get("completion_tokens")}}
        await self._record_cost(cost, model, usage)
        try:
            cpath.write_text(json.dumps(out))
        except OSError:
            pass
        return out


# ---------------------------------------------------------------------------
# Elicitation parsers (logprob softmax + portable self-consistency)
# ---------------------------------------------------------------------------
def yes_prob_from_logprobs(top_logprobs: list | None, content: str | None) -> float | None:
    """P(Yes) = softmax over the {Yes,No} logits at the first answer-bearing token.
    Scans up to the first 3 generated tokens for a position exposing yes/no."""
    if not top_logprobs:
        if content is None:
            return None
        c = content.strip().lower()
        if c.startswith("yes"):
            return 0.95
        if c.startswith("no"):
            return 0.05
        return None
    for tok in top_logprobs[:3]:
        ly = ln = None
        for a in tok.get("top", []):
            t = (a.get("token") or "").strip().lower()
            lp = a.get("logprob")
            if lp is None:
                continue
            if t == "yes" and (ly is None or lp > ly):
                ly = lp
            elif t == "no" and (ln is None or lp > ln):
                ln = lp
        if ly is not None or ln is not None:
            ly = ly if ly is not None else -25.0
            ln = ln if ln is not None else -25.0
            m = max(ly, ln)
            ey, en = math.exp(ly - m), math.exp(ln - m)
            return ey / (ey + en)
    # no yes/no among top tokens -> fall back to generated content
    return yes_prob_from_logprobs(None, content)


def parse_yes_conf(content: str | None) -> float | None:
    """Portable self-consistency parse: 'Answer: Yes/No, Confidence: 0-100' -> p(true).
    Returns p = conf/100 if Yes, 1-conf/100 if No. None if unparseable."""
    if not content:
        return None
    import re
    low = content.lower()
    is_yes = bool(re.search(r"\b(answer\s*[:\-]?\s*)?yes\b", low))
    is_no = bool(re.search(r"\b(answer\s*[:\-]?\s*)?no\b", low))
    if is_yes == is_no:  # both or neither -> ambiguous; use leading token
        m = re.match(r"\s*(yes|no)", low)
        if not m:
            return None
        is_yes = m.group(1) == "yes"
        is_no = not is_yes
    mconf = re.search(r"conf(?:idence)?\s*[:\-]?\s*(\d{1,3})", low)
    conf = None
    if mconf:
        conf = min(100, max(0, int(mconf.group(1))))
    if conf is None:
        conf = 75  # default moderate confidence when the model omits a number
    frac = conf / 100.0
    return frac if is_yes else (1.0 - frac)
