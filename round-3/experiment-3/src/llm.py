#!/usr/bin/env python3
"""Async OpenRouter client with bounded concurrency, retries, and exact cost metering."""
from __future__ import annotations

import asyncio
import os

import aiohttp
from loguru import logger
from tenacity import (retry, retry_if_exception_type, stop_after_attempt,
                      wait_exponential)

from common import CONFIG, BudgetExceeded, CostMeter

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class RetryableHTTP(Exception):
    pass


class LLM:
    def __init__(self, cost_meter: CostMeter, model: str | None = None,
                 concurrency: int | None = None):
        self.cost_meter = cost_meter
        self.model = model or CONFIG["model_primary"]
        self.fallbacks = CONFIG["model_fallbacks"]
        self.sem = asyncio.Semaphore(concurrency or CONFIG["global_concurrency"])
        self.session: aiohttp.ClientSession | None = None
        self.key = os.environ["OPENROUTER_API_KEY"]

    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=120, connect=20)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self

    async def __aexit__(self, *exc):
        if self.session:
            await self.session.close()

    @retry(retry=retry_if_exception_type(RetryableHTTP),
           wait=wait_exponential(multiplier=1.2, min=1, max=20),
           stop=stop_after_attempt(5), reraise=True)
    async def _post(self, body: dict) -> dict:
        async with self.sem:
            async with self.session.post(
                OPENROUTER_URL,
                json=body,
                headers={"Authorization": f"Bearer {self.key}",
                         "Content-Type": "application/json"},
            ) as resp:
                if resp.status in (429, 500, 502, 503, 504):
                    txt = await resp.text()
                    raise RetryableHTTP(f"{resp.status}: {txt[:200]}")
                data = await resp.json()
                if "error" in data and "choices" not in data:
                    msg = str(data["error"])[:200]
                    # transient provider errors -> retry
                    if any(k in msg.lower() for k in ("rate", "timeout", "overloaded", "502", "503")):
                        raise RetryableHTTP(msg)
                    raise RuntimeError(f"API error: {msg}")
                return data

    async def chat(self, messages: list[dict], *, max_tokens: int = 64,
                   temperature: float = 0.0, want_logprobs: bool = False,
                   tag: str = "") -> tuple[str | None, dict | None]:
        """Returns (content, logprobs). Records cost. Returns (None, None) on failure."""
        models = [self.model] + [m for m in self.fallbacks if m != self.model]
        last_err = None
        for model in models:
            body = {
                "model": model,
                "messages": messages,
                "max_tokens": max(16, max_tokens),
                "temperature": temperature,
            }
            if want_logprobs:
                body["logprobs"] = True
                body["top_logprobs"] = 5
            try:
                data = await self._post(body)
            except BudgetExceeded:
                raise
            except Exception as e:
                last_err = e
                logger.debug(f"[{tag}] model {model} failed: {str(e)[:160]}")
                continue
            try:
                ch = data["choices"][0]
                content = ch["message"]["content"]
                usage = data.get("usage", {})
                self.cost_meter.add(usage, model, tag=tag)
                return content, ch.get("logprobs")
            except BudgetExceeded:
                raise
            except Exception as e:
                last_err = e
                logger.debug(f"[{tag}] parse failed for {model}: {str(e)[:160]}")
                continue
        logger.warning(f"[{tag}] all models failed: {str(last_err)[:160]}")
        return None, None
