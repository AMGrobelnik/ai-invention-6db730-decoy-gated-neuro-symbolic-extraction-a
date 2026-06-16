#!/usr/bin/env python3
"""Stage 2 (pure-Python + small memoized relation-pick API): map every system into the
shared (title, P-code, head_id, tail_id) space via ONE fixed aligner, score by the official
tuple-matching metric, and produce the matched-recall wedge, multi-hop hallucination rate,
knockoff+ operating points, document-block bootstrap CIs, and the alignment confound check."""
from __future__ import annotations

import asyncio
import json
import math
import random
from pathlib import Path

import numpy as np
from loguru import logger

import prompts
from common import (ALIGN_CACHE_FILE, CONFIG, RULES, Embedder, build_pcode_embeddings,
                    load_relation_schema, norm)
from llm import LLM

SYSTEMS = ["METHOD", "PLAIN", "CoT", "RAG", "CONF"]


# ======================================================================================
# RELATION ALIGNMENT (hybrid: MiniLM shortlist + temp-0 LLM pick; embedding fallback)
# ======================================================================================
class Aligner:
    def __init__(self, embedder: Embedder, rel_schema: list[dict]):
        self.emb = embedder
        self.np = np
        self.pcodes, self.pcode_emb, self.pmap = build_pcode_embeddings(embedder, rel_schema)
        self.rel_cache: dict[str, str] = {}
        if ALIGN_CACHE_FILE.exists():
            try:
                self.rel_cache = json.loads(ALIGN_CACHE_FILE.read_text())
            except Exception:
                self.rel_cache = {}

    def _shortlist(self, phrase: str):
        e = self.emb.encode_cached([phrase])[0]
        sims = self.pcode_emb @ e
        idx = np.argsort(-sims)[: CONFIG["align_shortlist_k"]]
        return [(self.pcodes[i], self.pmap[self.pcodes[i]]["relation_name"],
                 self.pmap[self.pcodes[i]]["relation_description"], float(sims[i])) for i in idx]

    def embed_only_pcode(self, phrase: str) -> str | None:
        e = self.emb.encode_cached([phrase])[0]
        sims = self.pcode_emb @ e
        i = int(np.argmax(sims))
        return self.pcodes[i] if sims[i] >= CONFIG["align_embed_floor"] else None

    async def resolve_phrases(self, phrases: list[str], cost_meter):
        """Resolve unique relation phrases to P-codes via the LLM picker (memoized+cached)."""
        uniq = sorted({norm(p) for p in phrases if p and p.strip()})
        todo = [p for p in uniq if p not in self.rel_cache]
        logger.info(f"Relation alignment: {len(uniq)} unique phrases, {len(todo)} need LLM pick")
        if not todo:
            return
        async with LLM(cost_meter) as llm:
            sem = asyncio.Semaphore(CONFIG["global_concurrency"])

            async def pick(phrase):
                async with sem:
                    shortlist = self._shortlist(phrase)
                    from common import parse_json_obj
                    content, _ = await llm.chat(
                        prompts.relation_pick_prompt(phrase, [(p, n, d) for p, n, d, _ in shortlist]),
                        max_tokens=20, temperature=CONFIG["temperature_align"], tag="rel_pick")
                    obj = parse_json_obj(content) if content else None
                    pc = obj.get("pcode") if isinstance(obj, dict) else None
                    valid = {p for p, _, _, _ in shortlist}
                    if pc == "NO_RELATION":
                        result = None
                    elif pc in valid:
                        result = pc
                    else:  # embedding fallback
                        top_pc, _, _, top_sim = shortlist[0]
                        result = top_pc if top_sim >= CONFIG["align_embed_floor"] else None
                    self.rel_cache[phrase] = result if result else "NO_RELATION"

            await asyncio.gather(*(pick(p) for p in todo))
        ALIGN_CACHE_FILE.write_text(json.dumps(self.rel_cache))

    def relation_pcode(self, phrase: str, mode: str = "hybrid") -> str | None:
        if mode == "embed_only":
            return self.embed_only_pcode(phrase)
        pc = self.rel_cache.get(norm(phrase))
        if pc is None:  # not resolved -> embedding fallback
            return self.embed_only_pcode(phrase)
        return None if pc == "NO_RELATION" else pc


# ======================================================================================
# ENTITY LINKING (three tiers: exact -> alias/substring -> embedding floor)
# ======================================================================================
def build_doc_entity_index(embedder: Embedder, entities: list[dict]):
    exact = {}
    alias = []  # (norm_name, entity_id, length)
    canon_names, canon_ids = [], []
    for e in entities:
        eid = e["entity_id"]
        names = set(e.get("aliases") or []) | {e.get("canonical_name", "")}
        for nm in names:
            nn = norm(nm)
            if not nn:
                continue
            exact.setdefault(nn, eid)
            alias.append((nn, eid, len(nn)))
        canon_names.append(e.get("canonical_name", "") or (e.get("aliases") or [""])[0])
        canon_ids.append(eid)
    canon_emb = embedder.encode_cached(canon_names) if canon_names else np.zeros((0, 384))
    return {"exact": exact, "alias": alias, "canon_emb": canon_emb, "canon_ids": canon_ids}


def link_entity(surface: str, idx: dict, embedder: Embedder, floor: float) -> int | None:
    s = norm(surface)
    if not s:
        return None
    if s in idx["exact"]:
        return idx["exact"][s]
    # tier 2: substring (longest matching alias)
    best = None
    for nn, eid, ln in idx["alias"]:
        if ln < 3 or len(s) < 3:
            continue
        if s in nn or nn in s:
            score = min(len(s), ln)
            if best is None or score > best[0]:
                best = (score, eid)
    if best is not None:
        return best[1]
    # tier 3: embedding
    if len(idx["canon_ids"]) == 0:
        return None
    e = embedder.encode_cached([surface])[0]
    sims = idx["canon_emb"] @ e
    i = int(np.argmax(sims))
    return idx["canon_ids"][i] if sims[i] >= floor else None


# ======================================================================================
# BUILD PER-SYSTEM ALIGNED ITEMS  (title, pcode, h_id, t_id, score)
# ======================================================================================
def conf_frequency(cand: dict, samples: list[list[dict]]) -> float:
    """Fraction of stochastic samples containing a triple matching the candidate
    (token-Jaccard >= 0.5 on both head and tail)."""
    if not samples:
        return 0.0
    ch, ct = set(norm(cand["head"]).split()), set(norm(cand["tail"]).split())
    if not ch or not ct:
        return 0.0
    def jac(a, b):
        return len(a & b) / max(1, len(a | b))
    hits = 0
    for samp in samples:
        found = False
        for tr in samp:
            sh, st = set(norm(tr.get("head", "")).split()), set(norm(tr.get("tail", "")).split())
            if jac(ch, sh) >= 0.5 and jac(ct, st) >= 0.5:
                found = True
                break
        if found:
            hits += 1
    return hits / len(samples)


def align_records(records: list[dict], aligner: Aligner, embedder: Embedder,
                  mode: str = "hybrid", el_floor: float | None = None):
    """Returns dict: system -> list of items {title,pcode,h_id,t_id,score,doc}. Items keep
    pcode separate so alignment-noise sensitivity can be applied downstream."""
    el_floor = el_floor if el_floor is not None else CONFIG["el_embed_floor"]
    out = {s: [] for s in SYSTEMS}
    for rec in records:
        title = rec["title"]
        eidx = build_doc_entity_index(embedder, rec["entities"])

        def align(h, r, t):
            pc = aligner.relation_pcode(r, mode=mode)
            if pc is None:
                return None
            hid = link_entity(h, eidx, embedder, el_floor)
            tid = link_entity(t, eidx, embedder, el_floor)
            if hid is None or tid is None:
                return None
            return (pc, hid, tid)

        # METHOD + PLAIN share the SAME candidate pool (W computable) -> identical recall ceiling
        for c in rec["candidates"]:
            if c.get("W") is None:
                continue
            a = align(c["head"], c["relation"], c["tail"])
            if a is None:
                continue
            pc, hid, tid = a
            base = {"title": title, "pcode": pc, "h_id": hid, "t_id": tid, "doc": title}
            out["METHOD"].append({**base, "score": c["W"]})
            out["PLAIN"].append({**base, "score": c["Z"]})
            # CONF: combined frequency + gpt(Z)
            freq = conf_frequency(c, rec.get("conf_samples", []))
            combined = 0.5 * freq + 0.5 * (c["Z"] if c["Z"] is not None else 0.0)
            out["CONF"].append({**base, "score": combined})
        for sysname, key in (("CoT", "cot"), ("RAG", "rag")):
            for tr in rec.get(key, []):
                a = align(tr["head"], tr["relation"], tr["tail"])
                if a is None:
                    continue
                pc, hid, tid = a
                out[sysname].append({"title": title, "pcode": pc, "h_id": hid, "t_id": tid,
                                     "doc": title, "score": float(tr.get("confidence", 0.5))})
    return out


def build_gold(records: list[dict]):
    gold = set()
    gold_by_doc = {}
    for rec in records:
        title = rec["title"]
        gset = gold_by_doc.setdefault(title, set())
        for g in rec["gold_triples"]:
            tup = (title, g["relation_pid"], g["head_id"], g["tail_id"])
            gold.add(tup)
            gset.add(tup)
    return gold, gold_by_doc


# ======================================================================================
# METRIC: PR CURVE + matched-recall machinery
# ======================================================================================
def materialize(items, gold, noise_p=0.0, seed=0, pcodes=None):
    """Collapse aligned items to unique tuples with max score; mark correctness. Optional
    uniform P-code corruption (alignment-noise sensitivity)."""
    rng = random.Random(seed)
    tuples = {}
    for it in items:
        pc = it["pcode"]
        if noise_p > 0 and pcodes and rng.random() < noise_p:
            pc = rng.choice([p for p in pcodes if p != pc])
        tup = (it["title"], pc, it["h_id"], it["t_id"])
        sc = it["score"]
        if sc is None:
            continue
        if tup not in tuples or sc > tuples[tup][0]:
            tuples[tup] = (sc, it["doc"])
    recs = [{"tuple": k, "score": v[0], "doc": v[1], "correct": k in gold}
            for k, v in tuples.items()]
    recs.sort(key=lambda r: r["score"], reverse=True)
    return recs


def pr_curve(recs, total_gold):
    pts = []
    correct = sub = 0
    for r in recs:
        sub += 1
        if r["correct"]:
            correct += 1
        pts.append((correct / max(1, total_gold), correct / sub, r["score"]))
    return pts


def threshold_for_recall(recs, total_gold, r_star):
    """Smallest score-threshold (most permissive) whose admitted set reaches recall>=r_star."""
    correct = sub = 0
    for r in recs:
        sub += 1
        if r["correct"]:
            correct += 1
        if correct / max(1, total_gold) >= r_star:
            return r["score"], correct / sub  # (threshold, precision at that point)
    return (recs[-1]["score"] if recs else 0.0), (correct / max(1, sub))


def per_doc_stats(recs, thr, doc_list):
    """For a fixed threshold, per-doc (submitted, correct) counts over admitted tuples."""
    sub = {d: 0 for d in doc_list}
    cor = {d: 0 for d in doc_list}
    for r in recs:
        if r["score"] >= thr:
            sub[r["doc"]] += 1
            if r["correct"]:
                cor[r["doc"]] += 1
    return (np.array([sub[d] for d in doc_list], float),
            np.array([cor[d] for d in doc_list], float))


def admitted_by_doc(recs, thr):
    by = {}
    for r in recs:
        if r["score"] >= thr:
            by.setdefault(r["doc"], []).append(r["tuple"])
    return by


# ======================================================================================
# MULTI-HOP FORWARD CHAINING (hallucinated-conclusion rate)
# ======================================================================================
def forward_chain(facts: set, max_iter: int = 6) -> set:
    facts = set(facts)
    by_rel = {}
    for (r, h, t) in facts:
        by_rel.setdefault(r, set()).add((h, t))
    derived = set()
    changed = True
    it = 0
    while changed and it < max_iter:
        changed = False
        it += 1
        for rule in RULES:
            subs = [{}]
            for (r, a, b) in rule["body"]:
                nxt = []
                for s in subs:
                    for (h, t) in by_rel.get(r, ()):
                        s2 = dict(s)
                        ok = True
                        for var, val in ((a, h), (b, t)):
                            if var in s2 and s2[var] != val:
                                ok = False
                                break
                            s2[var] = val
                        if ok:
                            nxt.append(s2)
                subs = nxt
                if not subs:
                    break
            r, a, b = rule["head"]
            for s in subs:
                if a in s and b in s and s[a] != s[b]:
                    f = (r, s[a], s[b])
                    if f not in facts:
                        facts.add(f)
                        by_rel.setdefault(r, set()).add((s[a], s[b]))
                        derived.add(f)
                        changed = True
    return derived


def forward_chain_traced(facts: set, max_iter: int = 6) -> list[dict]:
    """Like forward_chain but records, for the FIRST derivation of each new fact, the rule and
    the body premises that fired -> human-auditable proof-trace records."""
    facts = set(facts)
    by_rel = {}
    for (r, h, t) in facts:
        by_rel.setdefault(r, set()).add((h, t))
    traces = []
    changed = True
    it = 0
    while changed and it < max_iter:
        changed = False
        it += 1
        for rule in RULES:
            subs = [({}, [])]  # (binding, premise-list)
            for (r, a, b) in rule["body"]:
                nxt = []
                for s, prem in subs:
                    for (h, t) in by_rel.get(r, ()):
                        s2 = dict(s)
                        ok = True
                        for var, val in ((a, h), (b, t)):
                            if var in s2 and s2[var] != val:
                                ok = False
                                break
                            s2[var] = val
                        if ok:
                            nxt.append((s2, prem + [(r, h, t)]))
                subs = nxt
                if not subs:
                    break
            r, a, b = rule["head"]
            for s, prem in subs:
                if a in s and b in s and s[a] != s[b]:
                    f = (r, s[a], s[b])
                    if f not in facts:
                        facts.add(f)
                        by_rel.setdefault(r, set()).add((s[a], s[b]))
                        traces.append({"conclusion": list(f), "rule": rule["name"],
                                       "premises": [list(p) for p in prem]})
                        changed = True
    return traces


def hallu_per_doc(admitted, gold_by_doc, doc_list):
    """Per-doc (n_derived, n_hallucinated) from forward chaining admitted atomic facts."""
    nd = {d: 0 for d in doc_list}
    nh = {d: 0 for d in doc_list}
    for d, tuples in admitted.items():
        facts = {(pc, h, t) for (_, pc, h, t) in tuples}
        derived = forward_chain(facts)
        gset = gold_by_doc.get(d, set())
        nd[d] = len(derived)
        nh[d] = sum(1 for (pc, h, t) in derived if (d, pc, h, t) not in gset)
    return (np.array([nd[x] for x in doc_list], float),
            np.array([nh[x] for x in doc_list], float))


# ======================================================================================
# KNOCKOFF+ THRESHOLD (research_1 A.6, eq. 1.9)
# ======================================================================================
def knockoff_plus_threshold(W: list[float], alpha: float):
    if not W:
        return None
    mags = sorted({abs(w) for w in W})
    for t in mags:
        pos = sum(1 for w in W if w >= t)
        neg = sum(1 for w in W if w <= -t)
        fdr_hat = (1 + neg) / max(1, pos)
        if fdr_hat <= alpha:
            return t
    return None


# ======================================================================================
# CONFORMAL (Mohri-Hashimoto) calibrated operating points for the LABELED reference (CONF)
# ======================================================================================
def conformal_operating_points(calib_items_by_doc, test_items, gold_total, alphas):
    """q-hat = ceil((n+1)(1-alpha))/n quantile of per-doc back-off scores; retain sub-claims
    with combined score > q-hat. calib_items_by_doc: {doc: [(score, correct)...]}.
    test_items: [(score, correct)...] (materialized unique CONF tuples on the test split)."""
    r_list = []
    for doc, items in calib_items_by_doc.items():
        inc = [s for s, c in items if not c]
        # r_doc = smallest cutoff that excludes every incorrect retained claim
        r_list.append(max(inc) if inc else -1.0)
    n = max(1, len(r_list))
    r_sorted = sorted(r_list)
    out = {}
    for alpha in alphas:
        k = math.ceil((n + 1) * (1 - alpha))
        k = min(max(k, 1), n)
        qhat = r_sorted[k - 1]
        retained = [(s, c) for (s, c) in test_items if s > qhat]
        n_ret = len(retained)
        cor = sum(1 for s, c in retained if c)
        out[str(alpha)] = {"q_hat": round(float(qhat), 5),
                           "recall": cor / max(1, gold_total),
                           "precision": cor / max(1, n_ret), "n_retained": n_ret}
    return out


# ======================================================================================
# DOCUMENT-BLOCK BOOTSTRAP (B>=2000), vectorized via shared multinomial count matrix
# ======================================================================================
def make_boot_counts(n_docs, B, seed):
    rng = np.random.default_rng(seed)
    return rng.multinomial(n_docs, [1.0 / n_docs] * n_docs, size=B).astype(float)  # (B, D)


def ratio_ci(counts, num_vec, den_vec):
    num = counts @ num_vec
    den = counts @ den_vec
    with np.errstate(divide="ignore", invalid="ignore"):
        vals = np.where(den > 0, num / den, np.nan)
    vals = vals[~np.isnan(vals)]
    if len(vals) == 0:
        return (float("nan"), float("nan"))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def diff_ci(counts, numA, denA, numB, denB):
    a = counts @ numA
    da = counts @ denA
    b = counts @ numB
    db = counts @ denB
    with np.errstate(divide="ignore", invalid="ignore"):
        va = np.where(da > 0, a / da, np.nan)
        vb = np.where(db > 0, b / db, np.nan)
    d = va - vb
    d = d[~np.isnan(d)]
    if len(d) == 0:
        return (float("nan"), float("nan"), float("nan"))
    return (float(np.mean(d)), float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5)))
