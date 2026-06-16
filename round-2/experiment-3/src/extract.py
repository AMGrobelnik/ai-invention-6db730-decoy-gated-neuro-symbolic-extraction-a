#!/usr/bin/env python3
"""Stage 1 (API-heavy): per-document extraction, isolated real scoring, counterfactual
decoy generation+verification+scoring -> W_i, and the CoT/RAG/conformal baseline raw
outputs. Each document is checkpointed to disk (resume-safe). NO alignment/metrics here
(those are pure-Python Stage 2) so that this expensive stage runs exactly once."""
from __future__ import annotations

import asyncio
import json
import math
from pathlib import Path

from loguru import logger
from rank_bm25 import BM25Okapi

import prompts
from common import CONFIG, CKPT_DIR, BudgetExceeded, norm
from llm import LLM


# --------------------------------------------------------------------------------------
def split_sentences(doc: dict) -> list[str]:
    text = doc["input"]
    offs = doc.get("sent_char_offsets") or []
    sents = []
    if offs:
        for i, start in enumerate(offs):
            end = offs[i + 1] if i + 1 < len(offs) else len(text)
            s = text[start:end].strip()
            if s:
                sents.append(s)
    if not sents:
        sents = [s.strip() for s in text.replace("\n", " ").split(". ") if s.strip()]
    return sents or [text]


def dedup_candidates(triples: list[dict], cap: int) -> list[dict]:
    seen = set()
    out = []
    for t in triples:
        key = (norm(t["head"]), norm(t["relation"]), norm(t["tail"]))
        if key in seen or not key[0] or not key[2]:
            continue
        seen.add(key)
        out.append(t)
        if len(out) >= cap:
            break
    return out


# --------------------------------------------------------------------------------------
async def extract_candidates(llm: LLM, doc: dict) -> list[dict]:
    msgs = prompts.extract_prompt(doc["input"])
    tasks = [llm.chat(msgs, max_tokens=900, temperature=CONFIG["temperature_extract"],
                      tag="extract") for _ in range(CONFIG["n_overgen"])]
    results = await asyncio.gather(*tasks)
    from common import parse_triples_jsonl
    union = []
    for content, _ in results:
        if content:
            union.extend(parse_triples_jsonl(content))
    return dedup_candidates(union, CONFIG["cand_cap"])


async def elicit_confidence(llm: LLM, doc: dict, head: str, relation: str, tail: str,
                            tag: str) -> float | None:
    """Graded label-free confidence in [0,1]: primary = logprob yes-token; fallback =
    verbalized [0,1]. Used IDENTICALLY for real candidates and their decoys (isolated)."""
    from common import parse_yes_logprob, parse_prob
    content, lp = await llm.chat(
        prompts.yesno_prompt(doc["input"], head, relation, tail),
        max_tokens=2, temperature=0.0, want_logprobs=True, tag=tag)
    s = parse_yes_logprob(lp)
    if s is not None:
        return s
    content, _ = await llm.chat(
        prompts.score_prompt(doc["input"], head, relation, tail),
        max_tokens=20, temperature=0.0, tag=tag + "_vb")
    return parse_prob(content) if content else None


async def score_real(llm: LLM, doc: dict, cand: dict) -> float | None:
    return await elicit_confidence(llm, doc, cand["head"], cand["relation"], cand["tail"],
                                   tag="score_real")


async def make_decoy(llm: LLM, doc: dict, cand: dict) -> tuple[dict | None, bool]:
    """Generate a counterfactual decoy, verify non-entailment (regenerate while entailed).
    Returns (decoy, final_is_entailed). final_is_entailed=True only when NO non-entailed decoy
    could be produced within the regen budget -> the contamination that actually biases W_i."""
    from common import parse_json_obj
    ht = cand.get("head_type", "MISC")
    tt = cand.get("tail_type", "MISC")
    ent_names = [e.get("canonical_name", "") for e in doc.get("entities", []) if e.get("canonical_name")]
    decoy = None
    for attempt in range(CONFIG["decoy_max_regen"] + 1):
        content, _ = await llm.chat(
            prompts.decoy_prompt(doc["input"], cand["relation"], ht, tt, ent_names),
            max_tokens=90, temperature=CONFIG["temperature_decoy"], tag="decoy_gen")
        obj = parse_json_obj(content) if content else None
        if not obj or not obj.get("head") or not obj.get("tail"):
            continue
        cand_decoy = {"head": str(obj["head"]).strip(),
                      "relation": cand["relation"],
                      "tail": str(obj["tail"]).strip()}
        ec, _ = await llm.chat(
            prompts.entail_check_prompt(doc["input"], cand_decoy["head"],
                                        cand_decoy["relation"], cand_decoy["tail"]),
            max_tokens=16, temperature=0.0, tag="decoy_verify")
        eobj = parse_json_obj(ec) if ec else None
        entailed = bool(eobj.get("entailed")) if isinstance(eobj, dict) else False
        decoy = cand_decoy
        if not entailed:
            return decoy, False  # clean non-entailed decoy found
    return decoy, True  # exhausted regen budget without a non-entailed decoy


async def process_candidate(llm: LLM, doc: dict, cand: dict) -> dict:
    z_task = asyncio.create_task(score_real(llm, doc, cand))
    decoy, contaminated = await make_decoy(llm, doc, cand)
    zt = None
    if decoy:
        zt = await elicit_confidence(llm, doc, decoy["head"], decoy["relation"], decoy["tail"],
                                     tag="score_decoy")
    z = await z_task
    out = dict(cand)
    out["Z"] = z
    out["Zt"] = zt
    out["decoy"] = decoy
    out["decoy_contaminated"] = contaminated
    if z is not None and zt is not None:
        out["W"] = max(z, zt) * (1.0 if z > zt else (-1.0 if z < zt else 0.0))
    else:
        out["W"] = None
    return out


async def baseline_cot(llm: LLM, doc: dict) -> list[dict]:
    from common import parse_triples_jsonl
    content, _ = await llm.chat(prompts.cot_prompt(doc["input"]),
                                max_tokens=900, temperature=0.0, tag="cot")
    if not content:
        return []
    tail = content.split("TRIPLES:")[-1] if "TRIPLES:" in content else content
    return parse_triples_jsonl(tail)


async def baseline_rag(llm: LLM, doc: dict) -> list[dict]:
    from common import parse_triples_jsonl
    sents = split_sentences(doc)
    tokenized = [norm(s).split() for s in sents]
    if not any(tokenized):
        return []
    bm25 = BM25Okapi([t or ["x"] for t in tokenized])
    query = norm(doc["title"]).split() or ["x"]
    scores = bm25.get_scores(query)
    order = sorted(range(len(sents)), key=lambda i: scores[i], reverse=True)
    top = [sents[i] for i in order[:5]]
    content, _ = await llm.chat(prompts.rag_prompt(top, doc["title"]),
                                max_tokens=700, temperature=0.0, tag="rag")
    return parse_triples_jsonl(content) if content else []


async def baseline_conf_samples(llm: LLM, doc: dict) -> list[list[dict]]:
    """Mohri-Hashimoto back-off frequency signal: N extra stochastic extraction samples.
    The per-candidate frequency score is computed in Stage 2 by matching candidates against
    these samples; the gpt-score reuses the isolated real score Z (no extra calls)."""
    from common import parse_triples_jsonl
    msgs = prompts.extract_prompt(doc["input"])
    tasks = [llm.chat(msgs, max_tokens=900, temperature=CONFIG["temperature_extract"],
                      tag="conf_sample") for _ in range(CONFIG["n_conf_samples"])]
    res = await asyncio.gather(*tasks)
    return [parse_triples_jsonl(c) if c else [] for c, _ in res]


# --------------------------------------------------------------------------------------
async def process_doc(llm: LLM, doc: dict, ckpt_path: Path) -> dict:
    cands = await extract_candidates(llm, doc)
    cand_tasks = [process_candidate(llm, doc, c) for c in cands]
    cot_task = asyncio.create_task(baseline_cot(llm, doc))
    rag_task = asyncio.create_task(baseline_rag(llm, doc))
    conf_task = asyncio.create_task(baseline_conf_samples(llm, doc))
    # return_exceptions so one malformed candidate/baseline can never drop the whole document
    results = await asyncio.gather(*cand_tasks, cot_task, rag_task, conf_task,
                                   return_exceptions=True)
    n_cand = len(cand_tasks)
    scored = []
    for s in results[:n_cand]:
        if isinstance(s, Exception):
            logger.warning(f"candidate failed in {doc['doc_id']}: {s!r}")
        else:
            scored.append(s)
    cot, rag, conf_samples = results[n_cand], results[n_cand + 1], results[n_cand + 2]
    cot = [] if isinstance(cot, Exception) else cot
    rag = [] if isinstance(rag, Exception) else rag
    conf_samples = [] if isinstance(conf_samples, Exception) else conf_samples

    n_gen = sum(1 for c in scored if c.get("decoy"))
    n_cont = sum(1 for c in scored if c.get("decoy_contaminated"))
    record = {
        "doc_id": doc["doc_id"], "title": doc["title"], "fold": doc["fold"],
        "split_role": doc["split_role"],
        "entities": doc["entities"], "gold_triples": doc["gold_triples"],
        "candidates": scored,
        "cot": cot, "rag": rag, "conf_samples": conf_samples,
        "contamination": {"n_generated": n_gen, "n_entailed": n_cont},
    }
    ckpt_path.write_text(json.dumps(record))
    n_valid_w = sum(1 for c in scored if c.get("W") is not None)
    logger.info(f"  doc {doc['doc_id']}: {len(scored)} cands ({n_valid_w} W), "
                f"cot={len(cot)} rag={len(rag)} contam={n_cont}/{n_gen}")
    return record


async def run_extraction(docs: list[dict], cost_meter, split_tag: str) -> int:
    out_dir = CKPT_DIR / split_tag
    out_dir.mkdir(parents=True, exist_ok=True)
    doc_sem = asyncio.Semaphore(CONFIG["doc_concurrency"])
    stop = {"flag": False}
    done = 0
    todo = []
    for doc in docs:
        ckpt = out_dir / f"{doc['doc_id']}.json"
        if ckpt.exists():
            try:
                json.loads(ckpt.read_text())
                done += 1
                continue
            except Exception:
                pass
        todo.append((doc, ckpt))
    logger.info(f"[{split_tag}] {done} cached, {len(todo)} to process")

    async with LLM(cost_meter) as llm:
        async def worker(doc, ckpt):
            nonlocal done
            if stop["flag"]:
                return
            async with doc_sem:
                if stop["flag"]:
                    return
                if cost_meter.over_soft():
                    logger.warning(f"SOFT CAP ${cost_meter.soft_cap} reached "
                                   f"(${cost_meter.total:.3f}); stopping new docs")
                    stop["flag"] = True
                    return
                try:
                    await process_doc(llm, doc, ckpt)
                    done += 1
                except BudgetExceeded as e:
                    logger.error(str(e))
                    stop["flag"] = True
                except Exception as e:
                    logger.exception(f"doc {doc['doc_id']} failed: {e}")

        await asyncio.gather(*(worker(d, c) for d, c in todo))
    logger.info(f"[{split_tag}] extraction complete: {done} docs, cost ${cost_meter.total:.4f}")
    return done
