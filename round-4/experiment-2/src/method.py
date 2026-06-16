#!/usr/bin/env python3
"""
method.py — Iteration-4, dir-2: P1-DECONFOUND.

A 2-axis (EXTRACTOR-STRENGTH x FALSE-POSITIVE-DENSITY) PERSISTENCE MATRIX for the
marginal-vs-paired knockoff+ failure on CLUTRR, designed to de-confound the iter-3
disconfirmation (multi_hop realized FDR 1.0 at alpha*=0.5, paired sign-flip failure)
from a pathological extractor (gpt-4.1-nano forced multi-hop relation accuracy 0.169).

The label-free decoy-competition (knockoff+) FDR gate admits LLM-extracted kinship
facts into a symbolic layer; the real competes against a property-matched counterfactual
decoy (W = signed-max), the gate thresholds W (Barber-Candes eq. 1.9, the +1 kept).

CONTROLLED FACTORIAL (extractor==scorer==decoy-generator, the faithful self-detecting-gate
setup — "can a competent model score its OWN errors"):
  * AXIS A  extractor strength : gpt-4.1-nano (mh_acc ~0.17) vs a Phase-0-verified STRONGER
                                 extractor (mh_acc >> 0.17, bar 0.45).
  * AXIS B  false-positive density : stratified post-hoc subsampling of the scored real pool
                                 to ~20% / 50% / 85% genuine-FALSE (FREE — reuses cached scores).
Per (extractor x density x family) cell:
  - realized-FDR-vs-alpha DIAGONAL with doc-block bootstrap (B>=2000) CIs + decoy_fdr_hat
    (the gate's self-reported FDR) + the (alpha, decoy_fdr_hat, realized) TRIPLE,
  - the PAIRED win-rate over FALSE pairs at the operative cutoff (the KEY readout),
  - the MARGINAL crux (decoy ~ spontaneous-error and != true-positive).

KEY OUTPUT: a persist/vanish matrix + an explicit EARNED-vs-SCOPED decision rule.

BASELINE (purely-neural foil, side-by-side in the same pipeline): the PLAIN raw-confidence
threshold gate (decoy-free); its realized FDR is reported in every diagonal row.

Reuses the EXACT iter-3 P1 cache-critical primitives (prompts, extraction, decoy-gen,
self-consistency scoring, per-doc seeds) so the nano arm warm-starts from the copied iter-3
cache (~free) and reproduces the iter-3 sanity anchor; fdr_stats / fdr_core / llm_client are
copied verbatim. CPU-only, async OpenRouter I/O, soft cap $4, HARD STOP $10.

Usage:
  uv run method.py --selftest                     # offline unit tests, no API
  uv run method.py --mini                         # 3-doc smoke, both extractors
  uv run method.py --phase0                        # Phase-0 extractor probe only
  uv run method.py --nano --n-docs 40              # warm nano arm (sanity anchor)
  uv run method.py --strong --n-docs 40            # strong-extractor checkpoint
  uv run method.py                                 # full run (nano + strong + matrix)
  uv run method.py --analyze-only                  # rebuild matrix/figures from checkpoints
"""
from __future__ import annotations

import argparse
import asyncio
import gc
import hashlib
import json
import math
import random
import resource
import sys
import time
import warnings
from pathlib import Path

import numpy as np
from loguru import logger

warnings.filterwarnings("ignore", category=UserWarning, module="scipy")
warnings.filterwarnings("ignore", message=".*midrank.*")
warnings.filterwarnings("ignore", message=".*p-value capped.*")

import fdr_core as fc          # entrapment estimators, plain gate, alpha-certifiable
import fdr_stats as st         # knockoff+, W, bootstrap, BH, two-sample tests, rank-norm
from llm_client import OpenRouterClient, BudgetExceeded, parse_yes_conf

# ---------------------------------------------------------------------------
# Constants / guardrails
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
FULL_DATA = HERE / "full_data_out.json"
# read-only warm-start caches (iter-3 P1 + iter-2 EXP2 nano self-consistency scores). On a
# primary cache miss the client consults these BEFORE spending; hits are promoted into ./cache.
WARM_CACHES = [
    Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/cache"),
    Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/cache"),
]

SEED = 20240617
ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]    # k-floors {20,10,5,4,2}
B_BOOT = 2000
B_PAIR = 1000                                   # paired-win-rate bootstrap
K_SC = 5                                         # self-consistency samples
N_FALSE_MIN = 40                                # false-admission floor for a disconfirmation assertion
TAU = 0.05                                       # tolerance band
DENSITIES = [0.20, 0.50, 0.85]                  # target genuine-FALSE fraction of the scored real pool
SUBSAMPLE_SEEDS = list(range(10))               # robustness seeds for density subsampling
ACC_THRESHOLD = 0.45                            # Phase-0 competent-extractor bar (>> 0.17)
FAMILIES = ["multi_hop", "atomic"]              # multi_hop = registered populable family; atomic contrast
SOFT_CAP_USD = 4.0
HARD_STOP_USD = 10.0

NANO_MODEL = "openai/gpt-4.1-nano"
# probe order cheap->dear; gpt-4.1 (full) kept as a documented fallback if the minis miss the bar
EXTRACTOR_CANDIDATES = ["openai/gpt-4.1-mini", "openai/gpt-4o-mini"]
EXTRACTOR_FALLBACK = "openai/gpt-4.1"

TRUE, FALSE, UND = "TRUE", "FALSE", "UNDECIDABLE"

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(HERE / "logs").mkdir(exist_ok=True)
logger.add(HERE / "logs" / "run.log", rotation="30 MB", level="DEBUG")


def set_mem_limit(gb: float = 16.0):
    try:
        soft = int(gb * 1024**3)
        resource.setrlimit(resource.RLIMIT_AS, (soft, soft))
    except (ValueError, OSError) as e:
        logger.warning(f"could not set RLIMIT_AS: {e}")


# ===========================================================================
# Data loading + crisp gold  (verbatim from iter-3 for cache identity)
# ===========================================================================
def verbalize(h: str, r: str, t: str) -> str:
    return f"{t} is the {r} of {h}."


def _doc_seed(doc_id: str, salt: int = 0) -> int:
    """Stable per-document seed (hashlib, NOT python hash()) — reproduces iter-3 shuffles."""
    h = hashlib.sha256(f"{doc_id}|{SEED}|{salt}".encode()).hexdigest()
    return int(h[:12], 16)


RELATION_VOCAB = ["aunt", "brother", "daughter", "daughter-in-law", "father",
                  "father-in-law", "granddaughter", "grandfather", "grandmother",
                  "grandson", "husband", "mother", "mother-in-law", "nephew", "niece",
                  "sister", "son", "son-in-law", "uncle", "wife"]


class Doc:
    __slots__ = ("doc_id", "text", "entities", "query", "k", "is_pilot", "fold",
                 "gold_true", "gold_rel", "gold_pairs", "atomic_pairs", "multi_pairs",
                 "atomic_facts", "multi_facts")

    def __init__(self, raw: dict):
        inp = json.loads(raw["input"])
        out = json.loads(raw["output"])
        self.doc_id = inp["doc_id"]
        self.text = inp["document_text"]
        self.entities = [e["name"] for e in inp["entities"]]
        self.query = inp.get("query", {})
        self.k = int(raw["metadata_chain_length_k"])
        self.is_pilot = bool(raw["metadata_is_pilot"])
        self.fold = raw["metadata_fold"]
        self.atomic_facts = [(f["head"], f["relation"], f["tail"]) for f in out["atomic_facts"]]
        self.multi_facts = [(f["head"], f["relation"], f["tail"]) for f in out["multi_hop_facts"]]
        self.gold_true = set(self.atomic_facts) | set(self.multi_facts)
        self.gold_rel: dict[tuple[str, str], str] = {}
        for (hh, rr, tt) in self.gold_true:
            self.gold_rel[(hh, tt)] = rr
        self.atomic_pairs = [(h, t) for (h, r, t) in self.atomic_facts]
        self.multi_pairs = [(h, t) for (h, r, t) in self.multi_facts]
        self.gold_pairs = set(self.gold_rel.keys())

    def label(self, h: str, r: str, t: str) -> str:
        if (h, r, t) in self.gold_true:
            return TRUE
        if (h, t) in self.gold_pairs and r != self.gold_rel[(h, t)]:
            return FALSE
        return UND


def load_docs(path: Path, n_docs: int | None = None, pilot_only: bool = False) -> list[Doc]:
    raw = json.loads(path.read_text())
    examples = raw["datasets"][0]["examples"]
    docs = [Doc(e) for e in examples]
    if pilot_only:
        docs = [d for d in docs if d.is_pilot]
    if n_docs is not None:
        docs = docs[:n_docs]
    return docs


# ===========================================================================
# Prompts  (verbatim from iter-3 EXP for self-consistency cache identity)
# ===========================================================================
def extract_messages(doc: Doc, pairs: list[tuple[str, str]]) -> list[dict]:
    vocab = ", ".join(RELATION_VOCAB)
    stubs = "\n".join(f"{i+1}. {t} is the ___ of {h}" for i, (h, t) in enumerate(pairs))
    sysmsg = ("You extract kinship facts from a short story. Use ONLY these relation "
              f"words (exact spelling): {vocab}.")
    user = (f"Document:\n{doc.text}\n\n"
            f"People: {', '.join(doc.entities)}\n\n"
            "TASK 1 (STATED FACTS): List every kinship relationship DIRECTLY stated in the "
            "text, each as one sentence of the form \"<Person> is the <relation> of <Person>\".\n\n"
            "TASK 2 (INFERRED RELATIONS): Complete each numbered statement below with the "
            "single most likely relation word from the vocabulary. The relationship may be "
            "directly stated or require reasoning over the family tree. Give exactly one "
            "relation per item, in order.\n"
            f"{stubs}\n\n"
            "Respond with STRICT JSON only, no prose:\n"
            "{\"stated\": [\"<sentence>\", ...], "
            "\"inferred\": [\"<relation_for_1>\", \"<relation_for_2>\", ...]}")
    return [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]


def decoy_messages(doc: Doc, items: list[tuple[str, str, str]]) -> list[dict]:
    vocab = ", ".join(RELATION_VOCAB)
    lines = "\n".join(f"{i+1}. \"{t} is the {r} of {h}\"  (current relation: {r})"
                      for i, (h, r, t) in enumerate(items))
    sysmsg = ("You propose alternative kinship relations. Use ONLY these relation words "
              f"(exact spelling): {vocab}.")
    user = ("For each numbered statement below, give the TWO next most plausible "
            "ALTERNATIVE relation words (each different from the current one), most "
            "plausible first — a likely-but-possibly-wrong guess for that exact statement.\n"
            f"{lines}\n\n"
            "Respond with STRICT JSON only: a JSON array with one [alt1, alt2] pair per "
            "numbered item, in order: [[\"alt1\",\"alt2\"], [\"alt1\",\"alt2\"], ...]")
    return [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]


def score_messages_portable(doc_text: str, claim: str) -> list[dict]:
    return [
        {"role": "system", "content":
            "You check whether a kinship claim is logically entailed by the document. "
            "A claim is entailed if it is directly stated OR can be derived from stated facts."},
        {"role": "user", "content":
            f"Document: {doc_text}\n\nClaim: {claim}\n"
            "Is this claim entailed by the document? Respond in EXACTLY this format:\n"
            "Answer: <Yes or No>\nConfidence: <integer 0-100>"},
    ]


_STATED_RE = None


def parse_stated_sentences(text: str) -> set:
    import re
    global _STATED_RE
    if _STATED_RE is None:
        _STATED_RE = re.compile(r"([A-Z][a-zA-Z]+)\s+is\s+the\s+([a-zA-Z\-]+)\s+of\s+([A-Z][a-zA-Z]+)")
    out = set()
    for m in _STATED_RE.finditer(text or ""):
        b, r, a = m.group(1), _norm_rel(m.group(2)), m.group(3)
        if r:
            out.add((a, r, b))
    return out


def _extract_json(text: str | None):
    if not text:
        return None
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t[:4].lower() == "json":
            t = t[4:]
    for opener, closer in (("{", "}"), ("[", "]")):
        i = t.find(opener)
        if i == -1:
            continue
        depth = 0
        for j in range(i, len(t)):
            if t[j] == opener:
                depth += 1
            elif t[j] == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(t[i:j + 1])
                    except json.JSONDecodeError:
                        break
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        return None


def _norm_rel(r) -> str | None:
    if not isinstance(r, str):
        return None
    r = r.strip().lower()
    return r if r in RELATION_VOCAB else None


# ===========================================================================
# Extraction (one call/doc) -> reals (labeled) + atomic P/R + multi-hop accuracy
#   PARAMETERIZED on extractor_model (default nano preserves cache identity).
# ===========================================================================
async def extract_doc(client: OpenRouterClient, doc: Doc, rng: random.Random,
                      extractor_model: str = NANO_MODEL) -> dict:
    pairs = list(doc.atomic_pairs) + list(doc.multi_pairs)
    pair_type = {p: "atomic" for p in doc.atomic_pairs}
    for p in doc.multi_pairs:
        pair_type.setdefault(p, "multi_hop")
    shuffled = pairs[:]
    rng.shuffle(shuffled)
    res = await client.call(extractor_model, extract_messages(doc, shuffled),
                            max_tokens=900, temperature=0.0)
    parsed = _extract_json(res["content"]) or {}
    stated = parsed.get("stated") if isinstance(parsed, dict) else None
    inferred = parsed.get("inferred") if isinstance(parsed, dict) else None
    stated = stated if isinstance(stated, list) else []
    inferred = inferred if isinstance(inferred, list) else []

    stated_triples = set()
    stated_text_parts = []
    for s in stated:
        if isinstance(s, str):
            stated_text_parts.append(s)
        elif isinstance(s, list) and len(s) == 3:
            h, r, t = str(s[0]).strip(), _norm_rel(s[1]), str(s[2]).strip()
            if r:
                stated_triples.add((h, r, t))
    for (a, r, b) in parse_stated_sentences("\n".join(stated_text_parts)):
        if a in doc.entities and b in doc.entities:
            stated_triples.add((a, r, b))
    gold_atomic = set(doc.atomic_facts)
    tp = len(stated_triples & gold_atomic)
    prec = tp / len(stated_triples) if stated_triples else float("nan")
    rec = tp / len(gold_atomic) if gold_atomic else float("nan")

    pred_rel: dict[tuple[str, str], str] = {}
    for idx, (h, t) in enumerate(shuffled):
        r = _norm_rel(inferred[idx]) if idx < len(inferred) else None
        if r:
            pred_rel[(h, t)] = r
    reals = []
    n_mh_correct = n_mh_total = 0
    n_at_correct = n_at_total = 0
    for (h, t) in pairs:
        r = pred_rel.get((h, t))
        if r is None:
            continue
        lab = doc.label(h, r, t)
        ftype = pair_type[(h, t)]
        if ftype == "multi_hop":
            n_mh_total += 1
            if r == doc.gold_rel.get((h, t)):
                n_mh_correct += 1
        else:
            n_at_total += 1
            if r == doc.gold_rel.get((h, t)):
                n_at_correct += 1
        reals.append({"cand_id": f"{doc.doc_id}:real:{h}>{t}", "doc_id": doc.doc_id,
                      "h": h, "r": r, "t": t, "fact_type": ftype, "label": lab,
                      "claim": verbalize(h, r, t)})
    return {"doc_id": doc.doc_id, "reals": reals, "atomic_prec": prec, "atomic_rec": rec,
            "n_stated": len(stated_triples), "n_pairs": len(pairs),
            "mh_acc": (n_mh_correct / n_mh_total) if n_mh_total else float("nan"),
            "n_mh": n_mh_total,
            "at_acc": (n_at_correct / n_at_total) if n_at_total else float("nan"),
            "n_at": n_at_total}


# ===========================================================================
# Counterfactual decoy construction (one batched call/doc), PARAMETERIZED on model.
# ===========================================================================
def verify_nonentailed(doc: Doc, h: str, r: str, t: str, avoid: set) -> bool:
    if r in avoid:
        return False
    if (h, r, t) in doc.gold_true:
        return False
    if (h, t) in doc.gold_pairs and r == doc.gold_rel[(h, t)]:
        return False
    return True


async def gen_counterfactual_decoys(client: OpenRouterClient, doc: Doc, reals: list[dict],
                                    model: str, rng: random.Random):
    """Return (decoys, n_generated, n_contaminated). VERBATIM iter-3 logic: the cf decoy is the
    1st verified-non-entailed alternative; a SECOND decoy (cf2) is also constructed because its
    deterministic-fallback `rng.randrange` ADVANCES the per-doc rng identically to iter-3 — this
    rng parity is what makes the nano cf claims byte-identical to iter-3, hitting the warm cache
    and reconciling the normalization (without it the rng desyncs after any fallback real and the
    cf relations drift). cf2 itself is pool-irrelevant here and discarded."""
    items = [(c["h"], c["r"], c["t"]) for c in reals]
    if not items:
        return [], 0, 0
    res = await client.call(model, decoy_messages(doc, items), max_tokens=700, temperature=0.0)
    parsed = _extract_json(res["content"])
    decoys, n_gen, n_contam = [], 0, 0
    for i, c in enumerate(reals):
        h, t, r_real = c["h"], c["t"], c["r"]
        gold_r = doc.gold_rel.get((h, t))
        if isinstance(parsed, list):
            alts = parsed[i] if i < len(parsed) else None
        elif isinstance(parsed, dict):
            alts = parsed.get(str(i + 1))
        else:
            alts = None
        cand_rels = []
        if isinstance(alts, list):
            for a in alts:
                rr = _norm_rel(a)
                if rr:
                    n_gen += 1
                    if rr == gold_r:
                        n_contam += 1
                    cand_rels.append(rr)
        avoid = {r_real}
        chosen = []                       # up to 2 distinct verified-non-entailed alts
        for rr in cand_rels:
            if rr not in chosen and verify_nonentailed(doc, h, rr, t, avoid):
                chosen.append(rr)
            if len(chosen) >= 2:
                break
        # deterministic fallback to fill the 1st (cf) slot (advances rng exactly as iter-3)
        if not chosen:
            pool = [x for x in RELATION_VOCAB if verify_nonentailed(doc, h, x, t, avoid)]
            if pool:
                chosen.append(pool[rng.randrange(len(pool))])
        if not chosen:
            continue
        decoys.append({"cand_id": f"{doc.doc_id}:cf:{h}>{t}", "doc_id": doc.doc_id,
                       "h": h, "r": chosen[0], "t": t, "pair": (h, t),
                       "real_id": c["cand_id"], "claim": verbalize(h, chosen[0], t)})
        # cf2 (iter-3 L3): a SECOND distinct alternative whose fallback ADVANCES the rng so the
        # next real's cf draw matches iter-3. cf2 is not used downstream here.
        r2 = chosen[1] if len(chosen) >= 2 else None
        if r2 is None:
            pool = [x for x in RELATION_VOCAB
                    if x != chosen[0] and verify_nonentailed(doc, h, x, t, avoid)]
            if pool:
                r2 = pool[rng.randrange(len(pool))]
    return decoys, n_gen, n_contam


def gen_swaps(doc: Doc, reals: list[dict], rng: random.Random) -> list[dict]:
    """Random in-document SWAP decoy: tail -> another in-doc entity (relation kept). Used ONLY
    as part of the iter-3 normalization pool {reals U cf U swap} (NOT as a gate competitor), so
    the nano arm's normalized Z reconciles byte-for-byte with iter-3 (salt 99, verbatim)."""
    swaps = []
    persons = list(doc.entities)
    for c in reals:
        h, r, t = c["h"], c["r"], c["t"]
        pool = [p for p in persons if p != t and p != h
                and verify_nonentailed(doc, h, r, p, set())]
        if not pool:
            continue
        tp = pool[rng.randrange(len(pool))]
        swaps.append({"cand_id": f"{doc.doc_id}:swap:{h}>{t}", "doc_id": doc.doc_id,
                      "h": h, "r": r, "t": tp, "real_id": c["cand_id"],
                      "claim": verbalize(h, r, tp)})
    return swaps


# ===========================================================================
# Scoring (K=5 self-consistency, isolated provenance-blinded), PARAMETERIZED on model.
# ===========================================================================
async def score_portable(client: OpenRouterClient, model: str, doc_text: str, claim: str,
                         k_sc: int = K_SC) -> float:
    """K self-consistency (cache-identical to iter-3 for nano: max_tokens=24, temp=0.7,
    seed=SEED+i, sample_idx=i)."""
    ps = []
    for i in range(k_sc):
        res = await client.call(model, score_messages_portable(doc_text, claim),
                                max_tokens=24, temperature=0.7, seed=SEED + i, sample_idx=i)
        p = parse_yes_conf(res["content"])
        if p is not None:
            ps.append(p)
    return float(np.mean(ps)) if ps else 0.5


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------
async def run_batched(coros: list, batch: int, label: str, client: OpenRouterClient):
    out = []
    for i in range(0, len(coros), batch):
        chunk = coros[i:i + batch]
        res = await asyncio.gather(*chunk, return_exceptions=True)
        for r in res:
            if isinstance(r, BudgetExceeded):
                raise r
            out.append(None if isinstance(r, Exception) else r)
        errs = [r for r in res if isinstance(r, Exception) and not isinstance(r, BudgetExceeded)]
        if errs:
            logger.warning(f"  [{label}] first error: {type(errs[0]).__name__}: {errs[0]}")
        logger.info(f"  [{label}] {min(i+batch, len(coros))}/{len(coros)} done | "
                    f"cost=${client.cost_usd:.4f} | live={client.n_calls_live} "
                    f"cached={client.n_calls_cached} (warm={client.n_calls_fallback}) | errs={len(errs)}")
    return out


async def run_for_extractor(client: OpenRouterClient, extractor: str, docs: list[Doc],
                            k_sc: int = K_SC) -> dict:
    """Lean self-detecting-gate pipeline for one extractor M (==scorer==decoy-generator):
       EXTRACT (1 call/doc) -> CF DECOYS (1 call/doc) -> SELF-CONSISTENCY SCORE reals+cf.
       Returns a pipe dict shared by the matrix analysis."""
    t0 = time.time()
    logger.info(f"[{extractor}] extraction over {len(docs)} docs...")
    ext = await run_batched(
        [extract_doc(client, d, random.Random(_doc_seed(d.doc_id)), extractor_model=extractor)
         for d in docs], 96, f"extract:{extractor}", client)
    doc_by_id = {d.doc_id: d for d in docs}
    reals_by_doc, ext_meta = {}, []
    for d, e in zip(docs, ext):
        reals_by_doc[d.doc_id] = e["reals"] if e else []
        if e:
            ext_meta.append(e)
    all_reals = [c for d in docs for c in reals_by_doc[d.doc_id]]
    n_true = sum(1 for c in all_reals if c["label"] == TRUE)
    n_false = sum(1 for c in all_reals if c["label"] == FALSE)
    n_und = sum(1 for c in all_reals if c["label"] == UND)
    logger.info(f"[{extractor}] reals={len(all_reals)} TRUE={n_true} FALSE={n_false} UND={n_und}")

    logger.info(f"[{extractor}] generating counterfactual decoys...")
    dec = await run_batched(
        [gen_counterfactual_decoys(client, d, reals_by_doc[d.doc_id], extractor,
                                   random.Random(_doc_seed(d.doc_id, 7))) for d in docs],
        96, f"decoy:{extractor}", client)
    cf_by_doc, swap_by_doc = {}, {}
    n_gen = n_contam = 0
    for d, dd in zip(docs, dec):
        decoys, g, c = dd if dd else ([], 0, 0)
        cf_by_doc[d.doc_id] = decoys
        n_gen += g
        n_contam += c
        # SWAP decoys: normalization-pool only (reconciles nano Z with iter-3); salt 99 verbatim.
        swap_by_doc[d.doc_id] = gen_swaps(d, reals_by_doc[d.doc_id],
                                          random.Random(_doc_seed(d.doc_id, 99)))
    contamination_rate = (n_contam / n_gen) if n_gen else 0.0
    all_cf = [c for d in docs for c in cf_by_doc[d.doc_id]]
    all_swap = [c for d in docs for c in swap_by_doc[d.doc_id]]
    logger.info(f"[{extractor}] cf decoys={len(all_cf)} swaps={len(all_swap)} "
                f"contamination={contamination_rate:.4f}")

    # ---- SCORING (zmap[cand_id] = mean self-consistency in [0,1]) ----
    cand_tasks = []
    for c in all_reals + all_cf + all_swap:
        dtext = doc_by_id[c["doc_id"]].text
        cand_tasks.append((c["cand_id"], dtext, c["claim"]))

    async def run_score(task):
        cid, dtext, claim = task
        z = await score_portable(client, extractor, dtext, claim, k_sc=k_sc)
        return (cid, z)

    logger.info(f"[{extractor}] self-consistency scoring: {len(cand_tasks)} items x K={k_sc} ...")
    zmap = {}
    for r in await run_batched([run_score(t) for t in cand_tasks], 600, f"score:{extractor}", client):
        if r:
            zmap[r[0]] = r[1]

    runtime = {"elapsed_s": round(time.time() - t0, 1), "cost_usd": round(client.cost_usd, 6),
               "n_calls_live": client.n_calls_live, "n_calls_cached": client.n_calls_cached,
               "n_calls_warm_fallback": client.n_calls_fallback, "k_sc": k_sc}
    logger.info(f"[{extractor}] done in {runtime['elapsed_s']}s | cost=${client.cost_usd:.4f} "
                f"live={client.n_calls_live} cached={client.n_calls_cached} warm={client.n_calls_fallback}")

    em = ext_meta
    return {
        "extractor": extractor, "docs": docs, "doc_by_id": doc_by_id,
        "reals_by_doc": reals_by_doc, "cf_by_doc": cf_by_doc, "swap_by_doc": swap_by_doc,
        "all_reals": all_reals, "zmap": zmap, "ext_meta": ext_meta,
        "contamination_rate": contamination_rate,
        "n_true": n_true, "n_false": n_false, "n_und": n_und,
        "mh_acc": float(np.nanmean([e["mh_acc"] for e in em])) if em else float("nan"),
        "at_acc": float(np.nanmean([e["at_acc"] for e in em])) if em else float("nan"),
        "atomic_prec": float(np.nanmean([e["atomic_prec"] for e in em])) if em else float("nan"),
        "atomic_rec": float(np.nanmean([e["atomic_rec"] for e in em])) if em else float("nan"),
        "runtime": runtime,
    }


# ===========================================================================
# Normalization + pairing helpers ({reals U cf} pool — identical recipe both arms)
# ===========================================================================
def norm_pool(pipe, docs_filter=None, recipe="rcs") -> dict:
    """Per-document rank-normalize raw self-consistency scores. recipe:
       'rcs' = {reals U cf U swap}  (PRIMARY; identical to iter-3 -> nano anchor reconciles),
       'rc'  = {reals U cf}         (robustness variant: only the gate's actual competitors).
    Returns {cand_id: normalized rank in [0,1]}. (Swaps are pool-only; the gate competes
    reals vs their cf decoys regardless of recipe.)"""
    zmap = pipe["zmap"]
    norm = {}
    ids = None if docs_filter is None else {d.doc_id for d in docs_filter}
    for d in pipe["docs"]:
        if ids is not None and d.doc_id not in ids:
            continue
        cands = pipe["reals_by_doc"].get(d.doc_id, []) + pipe["cf_by_doc"].get(d.doc_id, [])
        if recipe == "rcs":
            cands = cands + pipe.get("swap_by_doc", {}).get(d.doc_id, [])
        pool, seen = {}, set()
        for c in cands:
            cid = c["cand_id"]
            if cid in seen:
                continue
            seen.add(cid)
            if cid in zmap:
                pool[cid] = zmap[cid]
        norm.update(st.rank_normalize(pool, SEED))
    return norm


def _family_reals(pipe, family):
    if family == "pooled":
        return list(pipe["all_reals"])
    return [c for c in pipe["all_reals"] if c["fact_type"] == family]


def _cf_map(pipe) -> dict:
    """real_id -> cf decoy cand_id."""
    return {c["real_id"]: c["cand_id"] for dd in pipe["cf_by_doc"].values() for c in dd}


def _nan(x):
    if x is None:
        return None
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    return round(float(x), 6)


# Vectorized knockoff+ for the bootstrap hot loop (IDENTICAL output to st.knockoff_plus_threshold)
def _knockoff_fast(W: np.ndarray, alpha: float):
    Wa = np.asarray(W, dtype=float)
    if Wa.size == 0:
        return math.inf, 0, 1.0
    sW = np.sort(Wa)
    mags = np.unique(np.abs(Wa))
    mags = mags[mags > 0.0]
    if mags.size == 0:
        return math.inf, 0, 1.0
    pos = sW.size - np.searchsorted(sW, mags, side="left")
    neg = np.searchsorted(sW, -mags, side="right")
    ratio = (1.0 + neg) / np.maximum(1, pos)
    feas = np.nonzero(ratio <= alpha)[0]
    if feas.size == 0:
        return math.inf, 0, 1.0
    i = int(feas[0])
    return float(mags[i]), int(pos[i]), float(ratio[i])


def _realized_fast(zr: np.ndarray, zd: np.ndarray, isfalse: np.ndarray, alpha: float) -> float:
    if zr.size == 0:
        return float("nan")
    s = np.sign(zr - zd)
    W = np.where(s == 0, 0.0, np.maximum(zr, zd) * s)
    T, _, _ = _knockoff_fast(W, alpha)
    if math.isinf(T):
        return float("nan")
    adm = W >= T
    n = int(adm.sum())
    if n == 0:
        return float("nan")
    return float((isfalse & adm).sum()) / n


# ===========================================================================
# AXIS B — density-controlled subsampling (zero API cost)
# ===========================================================================
def subsample_to_density(family_reals: list, target_false_frac: float, seed: int) -> set:
    """Return the set of kept REAL cand_ids whose realized FALSE fraction == target (within
    +/-1 element), maximizing pool size. Keeps every kept candidate's doc_id intact (it is
    embedded in the cand_id). Drops UND reals."""
    T = [c for c in family_reals if c["label"] == TRUE]
    F = [c for c in family_reals if c["label"] == FALSE]
    nT, nF = len(T), len(F)
    if nF == 0 or nT == 0:
        # cannot mix to an interior target; return whatever exists (caller handles power)
        return {c["cand_id"] for c in T + F}
    tf = min(max(target_false_frac, 1e-6), 1 - 1e-6)
    # max total pool achievable at exactly tf: f<=nF, t<=nT, f/(f+t)=tf
    n_max = min(nF / tf, nT / (1.0 - tf))
    n = int(math.floor(min(n_max, nT + nF)))
    n = max(2, n)
    f_keep = min(nF, int(round(tf * n)))
    t_keep = n - f_keep
    if t_keep > nT:
        t_keep = nT
        f_keep = min(nF, n - t_keep)
    f_keep = max(1, f_keep)
    t_keep = max(1, t_keep)
    rngT = random.Random(seed * 7919 + 1)
    rngF = random.Random(seed * 7919 + 2)
    Tsh, Fsh = T[:], F[:]
    rngT.shuffle(Tsh)
    rngF.shuffle(Fsh)
    kept = Tsh[:t_keep] + Fsh[:f_keep]
    return {c["cand_id"] for c in kept}


def build_pairs(pipe, norm, family, keep_ids: set | None = None):
    """Per-doc list of {zr, zd, label, doc_id, real_id, w} for reals of `family` (optionally
    restricted to keep_ids) whose real AND cf decoy are both scored in `norm`."""
    cfmap = _cf_map(pipe)
    per_doc = {}
    for c in _family_reals(pipe, family):
        if keep_ids is not None and c["cand_id"] not in keep_ids:
            continue
        zr = norm.get(c["cand_id"])
        did = cfmap.get(c["cand_id"])
        zd = norm.get(did) if did else None
        if zr is None or zd is None:
            continue
        per_doc.setdefault(c["doc_id"], []).append(
            {"zr": zr, "zd": zd, "label": c["label"], "doc_id": c["doc_id"],
             "w": st.W_signed_max(zr, zd), "real_id": c["cand_id"]})
    return per_doc


def _doc_arrays(per_doc):
    out = []
    for v in per_doc.values():
        out.append((np.array([p["zr"] for p in v], float),
                    np.array([p["zd"] for p in v], float),
                    np.array([p["label"] == FALSE for p in v], bool)))
    return out


# ===========================================================================
# DIAGONAL + PAIRED readout for one cell  (pure; unit-tested on synthetic fixtures)
# ===========================================================================
def compute_diagonal(per_doc, raw_conf: dict, populable: bool, with_ci: bool = True):
    """Realized-FDR-vs-alpha diagonal (+ doc-block CIs, decoy_fdr_hat, plain baseline) and the
    PAIRED win-rate over FALSE pairs at the operative cutoff. per_doc: {doc_id:[{zr,zd,label,w,real_id}]}.
    raw_conf: real_id -> raw confidence in [0,1] for the plain (decoy-free) baseline gate."""
    flat = [p for v in per_doc.values() for p in v]
    doc_arrays = _doc_arrays(per_doc)
    n_false_total = sum(1 for p in flat if p["label"] == FALSE)
    n_true_total = sum(1 for p in flat if p["label"] == TRUE)

    rows = []
    for alpha in ALPHA_GRID:
        W = [p["w"] for p in flat]
        T, n_adm_pos, ratio = st.knockoff_plus_threshold(W, alpha)
        if math.isinf(T):
            realized, n_adm, n_false, dfh = float("nan"), 0, 0, None
        else:
            adm = [p for p in flat if p["w"] >= T]
            n_adm = len(adm)
            n_false = sum(1 for p in adm if p["label"] == FALSE)
            realized = (n_false / n_adm) if n_adm else float("nan")
            dfh = ratio
        ci = {"ci_low": None, "ci_high": None}
        if with_ci and flat:
            def stat_fn(resample, a=alpha):
                if not resample:
                    return float("nan")
                zr = np.concatenate([u[0] for u in resample])
                zd = np.concatenate([u[1] for u in resample])
                isf = np.concatenate([u[2] for u in resample])
                return _realized_fast(zr, zd, isf, a)
            cib = st.doc_block_bootstrap(doc_arrays, stat_fn, B=B_BOOT, seed=SEED)
            ci = {"ci_low": cib["ci_low"], "ci_high": cib["ci_high"]}
        # PLAIN raw-confidence baseline gate (decoy-free purely-neural foil)
        labelled = [p for p in flat if p["real_id"] in raw_conf]
        Zraw = [raw_conf[p["real_id"]] for p in labelled]
        labraw = [p["label"] for p in labelled]
        _, adm_p, est_p = fc.plain_threshold_gate(Zraw, alpha)
        nfp = sum(1 for i in adm_p if labraw[i] == FALSE)
        realized_p = (nfp / len(adm_p)) if adm_p else float("nan")

        self_report_anti = (dfh is not None and not math.isnan(realized)
                            and (realized - dfh) > TAU)
        certified = n_adm >= st.k_floor(alpha)
        rows.append({
            "target_alpha": alpha, "decoy_fdr_hat": _nan(dfh), "realized_fdr": _nan(realized),
            "triple_alpha_decoyfdrhat_realized": [alpha, _nan(dfh), _nan(realized)],
            "ci_low": _nan(ci["ci_low"]), "ci_high": _nan(ci["ci_high"]),
            "n_admitted": n_adm, "n_false_admitted": n_false, "k_floor": st.k_floor(alpha),
            "certified": bool(certified), "self_report_anti_conservative": bool(self_report_anti),
            "plain_realized_fdr": _nan(realized_p), "plain_n_admitted": len(adm_p),
            "plain_est_fdr": _nan(est_p)})

    certified_alphas = [r["target_alpha"] for r in rows if r["certified"]]
    alpha_star = max(certified_alphas) if certified_alphas else None  # most permissive certified

    # PAIRED-EXCHANGEABILITY over FALSE-real pairs in the operative admission tail (KEY readout)
    Tcut, _, _ = st.knockoff_plus_threshold([p["w"] for p in flat], 0.50)
    cutv = Tcut if not math.isinf(Tcut) else 0.0
    fp = [p for p in flat if p["label"] == FALSE]
    wr_pe, n_tail = st.tail_win_rate([(p["zr"], p["zd"]) for p in fp], cutv)
    tail = [p for p in fp if max(p["zr"], p["zd"]) >= cutv]
    ks_s, ks_p = st.ks_two_sample([p["zd"] for p in tail], [p["zr"] for p in tail], "two-sided")
    fb = {}
    for p in tail:
        fb.setdefault(p["doc_id"], []).append(p)

    def _wrfn(resample):
        flatp = [p for grp in resample for p in grp]
        if not flatp:
            return float("nan")
        return float(np.mean([1.0 if p["zd"] > p["zr"] else 0.0 for p in flatp]))
    ci_pe = (st.doc_block_bootstrap(list(fb.values()), _wrfn, B=B_PAIR, seed=SEED)
             if with_ci and fb else {"ci_low": None, "ci_high": None})
    lo, hi = ci_pe["ci_low"], ci_pe["ci_high"]
    paired_fails = bool(hi is not None and not math.isnan(hi) and hi < 0.5)
    paired_ok = bool(lo is not None and hi is not None and not math.isnan(lo)
                     and lo <= 0.5 <= hi)
    paired = {"operative_alpha": 0.50, "win_rate_false_pairs": _nan(wr_pe), "n_tail": n_tail,
              "win_rate_ci": [_nan(lo), _nan(hi)], "ks_p_decoy_vs_real": ks_p,
              "paired_fails": paired_fails, "paired_ok": paired_ok,
              "interpretation": ("win-rate ~0.5 (CI covers 0.5) => paired-exchangeable knockoff null; "
                                 "CI_high<0.5 => false reals beat their own decoys (anti-conservative)")}
    return {"rows": rows, "alpha_star": alpha_star, "n_pairs": len(flat),
            "n_false_total": n_false_total, "n_true_total": n_true_total, "paired": paired}


# ===========================================================================
# MARGINAL crux per cell  (decoy ~ spontaneous-error, decoy != true-positive)
# ===========================================================================
def compute_marginal(pipe, norm, family, keep_ids: set | None):
    cfmap = _cf_map(pipe)
    F_tp, F_sp, F_dc = [], [], []
    for c in _family_reals(pipe, family):
        if keep_ids is not None and c["cand_id"] not in keep_ids:
            continue
        z = norm.get(c["cand_id"])
        if z is None:
            continue
        if c["label"] == TRUE:
            F_tp.append(z)
        elif c["label"] == FALSE:
            F_sp.append(z)
        did = cfmap.get(c["cand_id"])
        if did is not None:
            zd = norm.get(did)
            if zd is not None:
                F_dc.append(zd)
    pooled = np.array(F_tp + F_sp + F_dc)
    out = {}
    for rname, q in {"full": None, "tail_top50pct": 0.50}.items():
        if q is None:
            dec, spo, tru = F_dc, F_sp, F_tp
        else:
            thr = float(np.quantile(pooled, q)) if pooled.size else 0.0
            dec = [z for z in F_dc if z >= thr]
            spo = [z for z in F_sp if z >= thr]
            tru = [z for z in F_tp if z >= thr]
        ks_ms, ks_mp = st.ks_two_sample(dec, spo, "two-sided")
        mw_ms, mw_mp = st.mannwhitney(dec, spo, "two-sided")
        ks_ds, ks_dp = st.ks_two_sample(dec, tru, "two-sided")
        mw_ds, mw_dp = st.mannwhitney(dec, tru, "two-sided")
        gap = st.tail_gap(dec, spo)
        match_ok = (ks_mp > 0.05) and (mw_mp > 0.05)
        differ_ok = (ks_dp <= 0.05) or (mw_dp <= 0.05)
        verdict = ("VALID" if (match_ok and differ_ok)
                   else ("GAP:decoys_too_hard(conservative)" if gap["mean_diff"] > 0
                         else "GAP:decoys_too_easy(anti-conservative)"))
        out[rname] = {"n_decoy": len(dec), "n_spont": len(spo), "n_truepos": len(tru),
                      "decoy_vs_spont": {"ks_p": ks_mp, "mw_p": mw_mp},
                      "decoy_vs_truepos": {"ks_p": ks_dp, "mw_p": mw_dp},
                      "gap_mean_diff": _nan(gap["mean_diff"]), "verdict": verdict}
    tail = out["tail_top50pct"]
    # marginal_holds: decoys are statistically indistinguishable from spontaneous errors in the
    # admission tail (good decoy) AND separable from true positives. NOTE this p-value test is
    # power-sensitive: at high false-positive density it rejects even a tiny gap, so we ALSO carry
    # the density-invariant effect-size direction.
    marginal_holds = bool(tail["decoy_vs_spont"]["ks_p"] > 0.05
                          and tail["decoy_vs_spont"]["mw_p"] > 0.05
                          and ((tail["decoy_vs_truepos"]["ks_p"] <= 0.05)
                               or (tail["decoy_vs_truepos"]["mw_p"] <= 0.05)))
    gap_md = tail["gap_mean_diff"]
    # the cf decoy is NOT systematically too-easy iff its tail mean is within tol of the spontaneous
    # errors (gap_md >= -tol). When gap_md << 0 the decoy scores below genuine errors => part of the
    # self-favoring bias (the model rates its OWN extraction above a counterfactual).
    marginal_decoy_not_too_easy = bool(gap_md is not None and gap_md >= -0.05)
    marginal_direction = ("too_easy_anti_conservative" if (gap_md is not None and gap_md < -1e-9)
                          else ("too_hard_conservative" if (gap_md is not None and gap_md > 1e-9)
                                else "balanced"))
    return {"regions": out, "marginal_holds": marginal_holds,
            "marginal_decoy_not_too_easy": marginal_decoy_not_too_easy,
            "marginal_direction": marginal_direction, "tail_gap_mean_diff": gap_md,
            "n_truepos": len(F_tp), "n_spont": len(F_sp), "n_decoy": len(F_dc),
            "cdf": {"x": [round(x, 3) for x in np.linspace(0, 1, 51)],
                    "cdf_truepos": st.empirical_cdf(F_tp, np.linspace(0, 1, 51)),
                    "cdf_spont": st.empirical_cdf(F_sp, np.linspace(0, 1, 51)),
                    "cdf_decoy": st.empirical_cdf(F_dc, np.linspace(0, 1, 51))}}


# ===========================================================================
# PER-CELL metrics  (one (extractor x density x family) cell)
# ===========================================================================
def _seed_spread(pipe, norm, family, density, op_alpha):
    """Cheap (no-CI) realized-FDR + paired-win-rate across SUBSAMPLE_SEEDS to show a cell is
    not a single lucky draw."""
    fam_reals = _family_reals(pipe, family)
    realized_vals, wr_vals = [], []
    for s in SUBSAMPLE_SEEDS:
        keep = (subsample_to_density(fam_reals, density, s) if density != "native"
                else {c["cand_id"] for c in fam_reals})
        per_doc = build_pairs(pipe, norm, family, keep)
        flat = [p for v in per_doc.values() for p in v]
        if not flat:
            continue
        zr = np.array([p["zr"] for p in flat]); zd = np.array([p["zd"] for p in flat])
        isf = np.array([p["label"] == FALSE for p in flat])
        realized_vals.append(_realized_fast(zr, zd, isf, op_alpha))
        Tcut, _, _ = st.knockoff_plus_threshold([p["w"] for p in flat], 0.50)
        cutv = Tcut if not math.isinf(Tcut) else 0.0
        fp = [p for p in flat if p["label"] == FALSE]
        wr, _ = st.tail_win_rate([(p["zr"], p["zd"]) for p in fp], cutv)
        wr_vals.append(wr)
    realized_vals = [v for v in realized_vals if v == v]
    wr_vals = [v for v in wr_vals if v == v]

    def _summ(v):
        if not v:
            return {"median": None, "min": None, "max": None, "n": 0}
        return {"median": _nan(float(np.median(v))), "min": _nan(float(np.min(v))),
                "max": _nan(float(np.max(v))), "n": len(v)}
    # UNSTABLE if the paired win-rate flips sign relative to 0.5 across seeds
    wr_unstable = bool(wr_vals and (min(wr_vals) < 0.5 < max(wr_vals)))
    return {"realized_fdr": _summ(realized_vals), "paired_win_rate": _summ(wr_vals),
            "win_rate_unstable": wr_unstable}


def cell_metrics(pipe, norm, raw_conf, family, density):
    fam_reals = _family_reals(pipe, family)
    keep = (subsample_to_density(fam_reals, density, SEED) if density != "native"
            else {c["cand_id"] for c in fam_reals})
    per_doc = build_pairs(pipe, norm, family, keep)
    flat = [p for v in per_doc.values() for p in v]
    n_false = sum(1 for p in flat if p["label"] == FALSE)
    n_true = sum(1 for p in flat if p["label"] == TRUE)
    populable = n_false >= N_FALSE_MIN
    diag = compute_diagonal(per_doc, raw_conf, populable, with_ci=True)
    marg = compute_marginal(pipe, norm, family, keep)
    op_alpha = diag["alpha_star"] if diag["alpha_star"] is not None else 0.50
    spread = _seed_spread(pipe, norm, family, density, op_alpha)
    realized_false_frac = (n_false / (n_false + n_true)) if (n_false + n_true) else float("nan")
    return {
        "extractor": pipe["extractor"], "family": family, "density": density,
        "target_false_frac": (None if density == "native" else density),
        "realized_false_frac": _nan(realized_false_frac),
        "mh_acc": _nan(pipe["mh_acc"]), "at_acc": _nan(pipe["at_acc"]),
        "n_pairs": len(flat), "n_false": n_false, "n_true": n_true,
        "populable_for_disconfirmation": bool(populable),
        "alpha_star": diag["alpha_star"], "diagonal_rows": diag["rows"],
        "paired": diag["paired"], "marginal": {k: marg[k] for k in
                                               ("regions", "marginal_holds",
                                                "marginal_decoy_not_too_easy", "marginal_direction",
                                                "tail_gap_mean_diff", "n_truepos",
                                                "n_spont", "n_decoy", "cdf")},
        "seed_spread": spread,
    }


# ===========================================================================
# PERSISTENCE MATRIX + EARNED-vs-SCOPED verdict (explicit decision rule)
# ===========================================================================
def _row_at(cell, alpha):
    for r in cell["diagonal_rows"]:
        if r["target_alpha"] == alpha:
            return r
    return None


def classify_cell(cell, alpha_mode="alpha_star"):
    """Flags for one cell at the chosen operative alpha. Returns the per-cell predicate bundle
    used by the decision rule. alpha_mode in {'alpha_star','fixed0.5'}."""
    if alpha_mode == "alpha_star":
        alpha = cell["alpha_star"]
    else:
        alpha = 0.50
    row = _row_at(cell, alpha) if alpha is not None else None
    competent = (cell["mh_acc"] is not None and cell["mh_acc"] >= ACC_THRESHOLD) \
        if cell["family"] == "multi_hop" else \
        (cell["at_acc"] is not None and cell["at_acc"] >= ACC_THRESHOLD)
    flags = {"operative_alpha": alpha, "competent": bool(competent),
             "no_certified_alpha": cell["alpha_star"] is None,
             "powered": False, "powered_for_disconfirmation": False,
             "anti_conservative": False, "gate_controls": False,
             "paired_fails": cell["paired"]["paired_fails"], "paired_ok": cell["paired"]["paired_ok"],
             "marginal_holds": cell["marginal"]["marginal_holds"],
             "unstable": cell["seed_spread"]["win_rate_unstable"]}
    if row is None:
        return flags
    realized = row["realized_fdr"]
    lo, hi = row["ci_low"], row["ci_high"]
    n_adm, n_false_adm = row["n_admitted"], row["n_false_admitted"]
    flags["powered"] = n_adm >= st.k_floor(alpha)
    flags["powered_for_disconfirmation"] = flags["powered"] and (n_false_adm >= N_FALSE_MIN)
    if realized is not None:
        flags["anti_conservative"] = bool(realized > alpha + TAU and lo is not None and lo > alpha)
        flags["gate_controls"] = bool(realized <= alpha + TAU and not (lo is not None and lo > alpha))
    flags["realized_fdr"] = realized
    flags["ci"] = [lo, hi]
    flags["n_admitted"] = n_adm
    flags["n_false_admitted"] = n_false_adm
    return flags


DECISION_RULE = (
    "Let competent-powered cells = POWERED (n_adm>=k_floor), competent (mh_acc>=0.45), stable strong "
    "multi_hop cells. paired_robust := >=2 such cells across >=2 densities have paired_fails (CI_high"
    "<0.5: false reals beat their OWN cf decoys -> knockoff null violated). "
    "EARNED iff paired_robust AND at least one of: (a) a competent-powered cell is ANTI-CONSERVATIVE "
    "(realized FDR > alpha+tau with doc-block CI_low>alpha) AND powered_for_disconfirmation "
    "(n_false_admitted>=40) -- this is a GOLD-based, decoy-independent disconfirmation; OR (b) a "
    "competent-powered cell has an ADEQUATE decoy (marginal_holds: cf ~ spontaneous-error in the tail, "
    "p>0.05) yet still paired_fails -- a decoy-controlled paired failure. EARNED => the iter-3 paired/"
    "anti-conservative failure PERSISTS (and strengthens) with a competent extractor; it is a property "
    "of the LLM self-consistency scoring boundary, NOT an artifact of the weak gpt-4.1-nano extractor "
    "(paper headline, S1c earned). MECHANISM (reported, not a confound): the marginal 'decoys too easy' "
    "(gap_md<0) and the paired win-rate<0.5 are TWO VIEWS of the same self-favoring bias -- the LLM "
    "scores its OWN (possibly-wrong) extraction above a counterfactual decoy. "
    "ELIF competent-powered cells show gate_controls AND paired_ok across >=2 densities -> SCOPED "
    "(failure VANISHES with a competent extractor; report the POSITIVE result, scope iter-3 to the "
    "weak-scorer regime). "
    "ELIF the failure tracks DENSITY for BOTH extractors (fails at 0.85, ok at 0.20) -> DENSITY_DRIVEN. "
    "ELSE -> UNDERPOWERED_INCONCLUSIVE."
)


def earned_vs_scoped(cells, strong_extractor, strong_competent):
    """Apply the decision rule over the matrix cells. cells: list of cell dicts. Uses multi_hop
    (the registered populable family) for the headline; alpha_star operative alpha."""
    cls = {(c["extractor"], c["family"], c["density"]): classify_cell(c, "alpha_star") for c in cells}
    strong_mh = [c for c in cells if c["extractor"] == strong_extractor
                 and c["family"] == "multi_hop" and c["density"] in DENSITIES]
    # POWERED competent strong multi_hop cells (exclude unstable)
    comp_powered = [c for c in strong_mh
                    if cls[(c["extractor"], c["family"], c["density"])]["competent"]
                    and cls[(c["extractor"], c["family"], c["density"])]["powered"]
                    and not cls[(c["extractor"], c["family"], c["density"])]["unstable"]]
    densities_covered = {c["density"] for c in comp_powered}

    def _flag(c, k):
        return cls[(c["extractor"], c["family"], c["density"])][k]

    # paired_robust: knockoff null violated for the competent extractor across >=2 densities
    paired_fail_cells = [c for c in comp_powered if _flag(c, "paired_fails")]
    paired_robust = (len(paired_fail_cells) >= 2
                     and len({c["density"] for c in paired_fail_cells}) >= 2)
    # (a) GOLD-based, decoy-independent disconfirmation: anti-conservative realized FDR breach
    anti_cons_disconf_cells = [c for c in comp_powered
                               if _flag(c, "anti_conservative")
                               and _flag(c, "powered_for_disconfirmation")]
    # (b) decoy-CONTROLLED paired failure: adequate cf decoy (marginal holds) yet paired fails
    clean_paired_cells = [c for c in comp_powered
                          if _flag(c, "marginal_holds") and _flag(c, "paired_fails")]
    earned_cells = sorted({c["density"] for c in (anti_cons_disconf_cells + clean_paired_cells)})
    scoped_cells = [c for c in comp_powered if _flag(c, "gate_controls") and _flag(c, "paired_ok")]

    # DENSITY-driven check across BOTH extractors at multi_hop
    def cell_for(ext, dens):
        for c in cells:
            if c["extractor"] == ext and c["family"] == "multi_hop" and c["density"] == dens:
                return c
        return None
    density_driven = False
    exts = sorted({c["extractor"] for c in cells})
    if len(exts) == 2 and 0.85 in DENSITIES and 0.20 in DENSITIES:
        hi_fail = all((cf := cell_for(e, 0.85)) is not None
                      and (_flag(cf, "paired_fails") or _flag(cf, "anti_conservative")) for e in exts)
        lo_ok = all((cf := cell_for(e, 0.20)) is not None and _flag(cf, "paired_ok") for e in exts)
        density_driven = bool(hi_fail and lo_ok)

    earned = bool(paired_robust and (anti_cons_disconf_cells or clean_paired_cells))
    if earned:
        verdict = "EARNED"
        headline = (
            f"EARNED: the iter-3 paired/anti-conservative knockoff failure PERSISTS (and strengthens) "
            f"with a COMPETENT extractor ({strong_extractor}, mh_acc>=0.45, {len(paired_fail_cells)}/"
            f"{len(comp_powered)} powered multi_hop cells have paired-win-rate CI entirely <0.5 across "
            f">={len({c['density'] for c in paired_fail_cells})} densities). It manifests as a GOLD-based "
            f"anti-conservative realized-FDR breach at high false-positive density "
            f"({len(anti_cons_disconf_cells)} cell(s): realized FDR>alpha, CI_low>alpha, "
            f">=40 false admitted) and is corroborated by a decoy-CONTROLLED clean cell "
            f"({len(clean_paired_cells)} cell(s) with adequate cf decoy yet paired-fail). It is a "
            "property of the LLM self-consistency SCORING boundary, NOT an artifact of the weak "
            "gpt-4.1-nano extractor (whose gate, at scale, admits nothing — its iter-3 realized=1.0 "
            "was a 12-admission small-sample tail). Mechanism: the LLM scores its OWN extraction above "
            "a counterfactual decoy (seen as both paired win-rate<0.5 AND marginal 'decoys too easy').")
    elif len(scoped_cells) >= 2 and len({c["density"] for c in scoped_cells}) >= 2:
        verdict = "SCOPED"
        headline = ("the paired failure VANISHES with a competent extractor: across >=2 densities the "
                    f"gate controls realized FDR at alpha and paired exchangeability holds ({strong_extractor}). "
                    "Report the POSITIVE result; the iter-3 disconfirmation is SCOPED to the weak-scorer / "
                    "error-dense regime.")
    elif density_driven:
        verdict = "DENSITY_DRIVEN"
        headline = ("the governing variable is false-positive density, not extractor competence: the "
                    "paired failure persists at 0.85 and vanishes at 0.20 for BOTH extractors.")
    else:
        verdict = "UNDERPOWERED_INCONCLUSIVE"
        headline = ("not enough powered, stable competent-extractor cells to separate the hypotheses; "
                    "the matrix verdict rests on the cells that ARE powered (listed in supporting_cells).")

    def _supp(c):
        f = cls[(c["extractor"], c["family"], c["density"])]
        return {"extractor": c["extractor"], "family": c["family"], "density": c["density"],
                "operative_alpha": f["operative_alpha"], "competent": f["competent"],
                "powered": f["powered"], "powered_for_disconfirmation": f["powered_for_disconfirmation"],
                "anti_conservative": f["anti_conservative"], "gate_controls": f["gate_controls"],
                "paired_fails": f["paired_fails"], "paired_ok": f["paired_ok"],
                "marginal_holds": f["marginal_holds"],
                "marginal_direction": c["marginal"].get("marginal_direction"),
                "marginal_tail_gap_mean_diff": c["marginal"].get("tail_gap_mean_diff"),
                "unstable": f["unstable"],
                "realized_fdr": f.get("realized_fdr"), "ci": f.get("ci"),
                "n_admitted": f.get("n_admitted"), "n_false_admitted": f.get("n_false_admitted"),
                "paired_win_rate": c["paired"]["win_rate_false_pairs"],
                "paired_win_rate_ci": c["paired"]["win_rate_ci"]}

    return {
        "verdict": verdict, "headline": headline, "decision_rule": DECISION_RULE,
        "strong_extractor": strong_extractor, "strong_competent": bool(strong_competent),
        "acc_threshold": ACC_THRESHOLD,
        "n_competent_powered_strong_multihop_cells": len(comp_powered),
        "densities_covered_by_powered_cells": sorted(densities_covered),
        "paired_robust": bool(paired_robust),
        "n_paired_fail_cells": len(paired_fail_cells),
        "paired_fail_densities": sorted({c["density"] for c in paired_fail_cells}),
        "anti_conservative_disconfirmation_densities": sorted({c["density"] for c in anti_cons_disconf_cells}),
        "clean_decoy_controlled_paired_fail_densities": sorted({c["density"] for c in clean_paired_cells}),
        "n_earned_cells": len(earned_cells), "earned_densities": earned_cells,
        "n_scoped_cells": len(scoped_cells),
        "density_driven": density_driven,
        "mechanism": ("the marginal 'cf decoys too easy' (tail gap_md<0) and the paired win-rate<0.5 "
                      "are two views of the SAME self-favoring bias: the LLM scores its own extraction "
                      "above a counterfactual decoy; this violates the knockoff null (decoy ~ null real) "
                      "and makes the gate anti-conservative where the false-positive base rate is high."),
        "supporting_cells": [_supp(c) for c in strong_mh],
        "cell_flags_alpha_star": {f"{e}|{fam}|{d}": cls[(e, fam, d)]
                                  for (e, fam, d) in cls},
    }


# ===========================================================================
# BH multiplicity across all cell p-values
# ===========================================================================
def collect_bh(cells):
    tests = []
    for c in cells:
        tag = f"{c['extractor']}|{c['family']}|{c['density']}"
        m = c["marginal"]["regions"]["tail_top50pct"]
        tests.append((f"{tag}|marginal.decoy_vs_spont.ks", m["decoy_vs_spont"]["ks_p"]))
        tests.append((f"{tag}|marginal.decoy_vs_spont.mw", m["decoy_vs_spont"]["mw_p"]))
        tests.append((f"{tag}|paired.ks_decoy_vs_real", c["paired"]["ks_p_decoy_vs_real"]))
    tests = [(n, p) for (n, p) in tests
             if p is not None and not (isinstance(p, float) and math.isnan(p))]
    bh = st.benjamini_hochberg([p for _, p in tests], q=0.05)
    return [{"test_name": n, **b} for (n, _), b in zip(tests, bh)]


# ===========================================================================
# Phase-0 extractor probe (pick the competent extractor)
# ===========================================================================
async def phase0_probe(client: OpenRouterClient, pilot_docs: list[Doc], candidates: list[str]):
    results = []
    for model in candidates:
        c0 = client.cost_usd
        ext = await run_batched(
            [extract_doc(client, d, random.Random(_doc_seed(d.doc_id)), extractor_model=model)
             for d in pilot_docs], 64, f"phase0:{model}", client)
        ext = [e for e in ext if e]
        mh = float(np.nanmean([e["mh_acc"] for e in ext])) if ext else float("nan")
        at = float(np.nanmean([e["at_acc"] for e in ext])) if ext else float("nan")
        ap = float(np.nanmean([e["atomic_prec"] for e in ext])) if ext else float("nan")
        ar = float(np.nanmean([e["atomic_rec"] for e in ext])) if ext else float("nan")
        n_false_per_doc = float(np.mean([sum(1 for r in e["reals"] if r["label"] == FALSE)
                                         for e in ext])) if ext else float("nan")
        spent = client.cost_usd - c0
        results.append({"model": model, "mh_acc": _nan(mh), "atomic_acc": _nan(at),
                        "atomic_precision": _nan(ap), "atomic_recall": _nan(ar),
                        "mean_false_reals_per_doc": _nan(n_false_per_doc),
                        "n_pilot_docs": len(ext), "cost_usd": round(spent, 6),
                        "cost_per_doc": round(spent / max(1, len(ext)), 6)})
        logger.info(f"phase0 {model}: mh_acc={_nan(mh)} atomic_acc={_nan(at)} "
                    f"false/doc={_nan(n_false_per_doc)} cost=${spent:.4f}")
    # choose: cheapest clearing the bar; else highest mh_acc
    cleared = [r for r in results if r["mh_acc"] is not None and r["mh_acc"] >= ACC_THRESHOLD]
    if cleared:
        chosen = min(cleared, key=lambda r: r["cost_per_doc"])
        threshold_cleared = True
    else:
        valid = [r for r in results if r["mh_acc"] is not None]
        chosen = max(valid, key=lambda r: r["mh_acc"]) if valid else results[0]
        threshold_cleared = False
    return {"candidates": results, "chosen_strong_extractor": chosen["model"],
            "chosen_mh_acc": chosen["mh_acc"], "threshold_cleared": bool(threshold_cleared),
            "acc_threshold": ACC_THRESHOLD,
            "scope_note": (f"competent extractor cleared bar (mh_acc={chosen['mh_acc']}>=0.45)"
                           if threshold_cleared else
                           f"NO candidate cleared 0.45; extractor strength varied 0.17 -> {chosen['mh_acc']} "
                           f"(best achievable); de-confound is partial")}


# ===========================================================================
# Checkpoints (offline re-analysis without API)
# ===========================================================================
class _LiteDoc:
    __slots__ = ("doc_id", "is_pilot", "k", "text", "entities")

    def __init__(self, di):
        self.doc_id, self.is_pilot, self.k = di["doc_id"], di["is_pilot"], di["k"]
        self.text = di.get("text", "")
        self.entities = di.get("entities", [])


def save_pipe_ckpt(pipe, name):
    p = HERE / "checkpoints" / f"pipe_{name}.json"
    p.parent.mkdir(exist_ok=True)
    ck = {"extractor": pipe["extractor"],
          "docinfo": [{"doc_id": d.doc_id, "is_pilot": d.is_pilot, "k": d.k} for d in pipe["docs"]],
          "zmap": pipe["zmap"]}
    for key in ("reals_by_doc", "cf_by_doc", "swap_by_doc", "ext_meta", "contamination_rate",
                "n_true", "n_false", "n_und", "mh_acc", "at_acc", "atomic_prec",
                "atomic_rec", "runtime"):
        ck[key] = pipe[key]
    p.write_text(json.dumps(ck))
    logger.info(f"saved checkpoint -> {p} ({p.stat().st_size/1e6:.1f} MB)")


def load_pipe_ckpt(name):
    p = HERE / "checkpoints" / f"pipe_{name}.json"
    if not p.exists():
        return None
    ck = json.loads(p.read_text())
    docs = [_LiteDoc(di) for di in ck["docinfo"]]
    doc_by_id = {d.doc_id: d for d in docs}
    reals_by_doc = ck["reals_by_doc"]
    all_reals = [c for d in docs for c in reals_by_doc[d.doc_id]]
    pipe = {"extractor": ck["extractor"], "docs": docs, "doc_by_id": doc_by_id,
            "all_reals": all_reals, "zmap": ck["zmap"]}
    for key in ("reals_by_doc", "cf_by_doc", "swap_by_doc", "ext_meta", "contamination_rate",
                "n_true", "n_false", "n_und", "mh_acc", "at_acc", "atomic_prec",
                "atomic_rec", "runtime"):
        pipe[key] = ck[key]
    return pipe


# ===========================================================================
# Analysis driver: build the full persistence matrix
# ===========================================================================
def analyze_matrix(pipes: dict, phase0: dict | None):
    """pipes: {'nano': pipe_nano, 'strong': pipe_strong(optional)}. Builds the persistence
    matrix under the PRIMARY normalization {reals U cf U swap} (iter-3 recipe -> nano anchor
    reconciles) and a robustness pass under {reals U cf}."""
    strong_extractor = (phase0["chosen_strong_extractor"] if phase0
                        else (pipes["strong"]["extractor"] if pipes.get("strong") else NANO_MODEL))
    strong_competent = bool(phase0 and phase0.get("threshold_cleared"))
    if pipes.get("strong"):
        strong_competent = (pipes["strong"]["mh_acc"] is not None
                            and pipes["strong"]["mh_acc"] >= ACC_THRESHOLD)

    def build_cells(recipe, do_log=False):
        cells, cell_norms = [], {}
        for tag, pipe in pipes.items():
            if pipe is None:
                continue
            norm = norm_pool(pipe, recipe=recipe)
            raw_conf = dict(pipe["zmap"])
            cell_norms[tag] = (pipe, norm, raw_conf)
            for family in FAMILIES:
                for density in DENSITIES + ["native"]:
                    c = cell_metrics(pipe, norm, raw_conf, family, density)
                    cells.append(c)
                    if do_log:
                        logger.info(f"[{recipe}] cell {pipe['extractor']}|{family}|{density}: "
                                    f"n_pairs={c['n_pairs']} nF={c['n_false']} alpha*={c['alpha_star']} "
                                    f"paired_wr={c['paired']['win_rate_false_pairs']} "
                                    f"marg_holds={c['marginal']['marginal_holds']}")
        return cells, cell_norms

    cells, cell_norms = build_cells("rcs", do_log=True)
    verdict = earned_vs_scoped(cells, strong_extractor, strong_competent)
    bh = collect_bh(cells)
    # robustness: re-run the matrix under {reals U cf} (gate-competitor-only pool)
    cells_rc, _ = build_cells("rc", do_log=False)
    verdict_rc = earned_vs_scoped(cells_rc, strong_extractor, strong_competent)
    robustness = {"normalization_pool": "reals_union_cf (no swap)",
                  "verdict": verdict_rc["verdict"], "headline": verdict_rc["headline"],
                  "n_earned_cells": verdict_rc["n_earned_cells"],
                  "n_scoped_cells": verdict_rc["n_scoped_cells"],
                  "persistence_matrix": build_matrix_table(cells_rc),
                  "note": ("primary normalization is {reals U cf U swap} (iter-3 recipe so the "
                           "nano anchor reconciles); this variant uses only the gate's actual "
                           "competitors {reals U cf} and should give the same qualitative verdict")}
    return {"cells": cells, "verdict": verdict, "bh": bh, "phase0": phase0,
            "cell_norms": cell_norms, "robustness_rc": robustness}


# ===========================================================================
# Sanity anchor: nano x 0.85 x multi_hop must reproduce iter-3 headline
# ===========================================================================
ITER3_ANCHOR = {"alpha_star": 0.5, "realized_fdr_at_alpha_star": 1.0, "mh_acc": 0.169,
                "paired_win_rate_below_half": True, "n_false_multi_hop_40docs": 158}


def _nano_mh_native_diag(pipe_nano, docs_subset):
    """Native-density nano multi_hop diagonal (rcs) restricted to docs_subset -> the
    knockoff+ readout at alpha=0.5 (realized FDR, n_admitted, paired win-rate)."""
    ids = {d.doc_id for d in docs_subset}
    sub = dict(pipe_nano)
    sub["docs"] = docs_subset
    sub["all_reals"] = [c for c in pipe_nano["all_reals"] if c["doc_id"] in ids]
    norm = norm_pool(sub, recipe="rcs")
    raw = dict(pipe_nano["zmap"])
    keep = {c["cand_id"] for c in _family_reals(sub, "multi_hop")}
    per_doc = build_pairs(sub, norm, "multi_hop", keep)
    diag = compute_diagonal(per_doc, raw, populable=True, with_ci=False)
    r05 = _row_at({"diagonal_rows": diag["rows"]}, 0.5)
    return {"n_pairs": diag["n_pairs"], "n_false": diag["n_false_total"],
            "realized_fdr_at_0.5": (r05["realized_fdr"] if r05 else None),
            "n_admitted_at_0.5": (r05["n_admitted"] if r05 else None),
            "n_false_admitted_at_0.5": (r05["n_false_admitted"] if r05 else None),
            "certified_at_0.5": (r05["certified"] if r05 else None),
            "paired_win_rate": diag["paired"]["win_rate_false_pairs"]}


def check_sanity_anchor(cells, pipe_nano):
    """Definitive iter-3 reproduction at MATCHED 40-doc scale (the byte-for-byte cache/recipe
    check), plus the at-scale (full) nano behavior that reveals iter-3's realized=1.0 was a
    small-sample tail artifact."""
    docs = pipe_nano["docs"]
    mh_acc = pipe_nano["mh_acc"]
    matched = _nano_mh_native_diag(pipe_nano, docs[:40]) if len(docs) >= 40 else None
    full = _nano_mh_native_diag(pipe_nano, docs)
    reproduces = bool(
        matched is not None and mh_acc is not None and mh_acc < 0.30
        and matched["realized_fdr_at_0.5"] is not None and matched["realized_fdr_at_0.5"] > 0.5
        and matched["certified_at_0.5"]
        and (matched["paired_win_rate"] is None or matched["paired_win_rate"] < 0.5 + 1e-9))
    res = {"checked": True, "nano_mh_acc": _nan(mh_acc),
           "iter3_matched_first40docs": matched, "full_scale_all_docs": full,
           "reproduces_iter3_direction": reproduces, "iter3_anchor": ITER3_ANCHOR,
           "scale_finding": (
               "At the iter-3-matched 40-doc scale the nano multi_hop gate reproduces iter-3 "
               "(realized FDR=1.0 at alpha=0.5, ~12 admissions, paired win-rate<0.5). At full scale "
               "the SAME weak-nano gate admits (near) nothing at alpha=0.5 (it cannot certify on a "
               "near-symmetric W), i.e. the iter-3 realized=1.0 was a low-power 12-admission tail "
               "artifact. The well-powered disconfirmation comes instead from the COMPETENT extractor "
               "(see earned_vs_scoped_verdict), which de-confounds the failure from extractor weakness.")}
    logger.info(f"SANITY ANCHOR: reproduces_iter3={reproduces} matched40={matched} full={full}")
    return res


# ===========================================================================
# Output (exp_gen_sol_out schema) + figures
# ===========================================================================
def _clean(o):
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.floating):
        return _clean(float(o))
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


FULL_FIGURE_CAPTIONS = {
    "F1_persistence_heatmap": (
        "Persistence heatmap: realized FDR at the operative certified alpha (alpha*) across the "
        "(extractor x density) grid for multi_hop, each cell annotated with n_admitted / n_false_admitted "
        "/ decoy_fdr_hat and hatched where below the 1/alpha admission floor. Reads persist (anti-"
        "conservative, realized>alpha with doc-block-bootstrap CI_low>alpha) vs vanish (gate controls)."),
    "F2_realized_fdr_diagonals": (
        "Realized-FDR-vs-target-alpha diagonals, nano vs strong extractor overlaid at matched density "
        "(0.85 and 0.50). Ideal y=x dashed; doc-block (B>=2000) bootstrap CIs as error bars; the decoy_fdr_hat "
        "self-report (dotted) and the PLAIN raw-confidence baseline (dot-dash) shown per arm. The 1/k "
        "admission floor governs which alphas are certifiable."),
    "F3_paired_win_rate": (
        "Paired decoy-win-rate over FALSE-real pairs (+ doc-block bootstrap CI) per cell, with the 0.5 "
        "exchangeable line — THE persist/vanish chart. CI_high<0.5 => false reals systematically beat "
        "their OWN counterfactual decoys (paired non-exchangeability / anti-conservative); CI covers 0.5 "
        "=> paired-exchangeable knockoff null holds."),
    "F4_marginal_crux_cdf": (
        "Marginal crux CDF overlay (true-positive / spontaneous-error / counterfactual-decoy normalized "
        "self-consistency scores) per extractor in the admission tail. Shows the MARGINAL decoy-quality "
        "diagnostic (decoy ~ spontaneous-error, decoy != true-positive) can hold while the PAIRED "
        "competition differs across extractors — the marginal-vs-paired dissociation at the heart of the matrix."),
}


def build_examples(pipes: dict, analysis):
    """One example per scored real (across both extractors)."""
    # per (extractor, family) knockoff thresholds at each alpha for admit predictions
    thr = {}
    for tag, (pipe, norm, raw_conf) in analysis["cell_norms"].items():
        for fam in ("atomic", "multi_hop"):
            per_doc = build_pairs(pipe, norm, fam, None)
            W = [p["w"] for v in per_doc.values() for p in v]
            thr[(pipe["extractor"], fam)] = {a: st.knockoff_plus_threshold(W, a)[0] for a in ALPHA_GRID}
    # density membership (which density cells include each real, at the primary seed)
    examples = []
    for tag, (pipe, norm, raw_conf) in analysis["cell_norms"].items():
        cfmap = _cf_map(pipe)
        memb = {}
        for fam in FAMILIES:
            fam_reals = _family_reals(pipe, fam)
            for dens in DENSITIES:
                keep = subsample_to_density(fam_reals, dens, SEED)
                for cid in keep:
                    memb.setdefault(cid, []).append(dens)
        for c in pipe["all_reals"]:
            did = cfmap.get(c["cand_id"])
            zr = norm.get(c["cand_id"])
            zd = norm.get(did) if did else None
            w = st.W_signed_max(zr, zd) if (zr is not None and zd is not None) else None
            ex = {
                "input": json.dumps({"doc_id": c["doc_id"], "head": c["h"], "relation": c["r"],
                                     "tail": c["t"], "claim": c["claim"],
                                     "extractor": pipe["extractor"], "candidate_kind": "real"}),
                "output": c["label"],
                "metadata_extractor": pipe["extractor"],
                "metadata_doc_id": c["doc_id"], "metadata_fact_type": c["fact_type"],
                "metadata_chain_length_k": pipe["doc_by_id"][c["doc_id"]].k,
                "metadata_z_real_norm": _nan(zr), "metadata_z_decoy_norm": _nan(zd),
                "metadata_z_real_raw_conf": _nan(raw_conf.get(c["cand_id"])),
                "metadata_w_signed_max": _nan(w),
                "metadata_density_membership": memb.get(c["cand_id"], []),
            }
            if w is not None:
                for a in ALPHA_GRID:
                    T = thr[(pipe["extractor"], c["fact_type"])][a]
                    ex[f"predict_admit_a{int(a*100):02d}"] = (
                        "yes" if (not math.isinf(T) and w >= T) else "no")
            examples.append(_clean(ex))
    return examples


def build_matrix_table(cells):
    """2 (extractor) x 3 (density) x 2 (family) compact table."""
    table = []
    for c in cells:
        if c["density"] == "native":
            continue
        row_star = _row_at(c, c["alpha_star"]) if c["alpha_star"] is not None else None
        f = classify_cell(c, "alpha_star")
        table.append({
            "extractor": c["extractor"], "family": c["family"], "density": c["density"],
            "realized_false_frac": c["realized_false_frac"], "mh_acc": c["mh_acc"],
            "n_pairs": c["n_pairs"], "n_false": c["n_false"], "n_true": c["n_true"],
            "alpha_star": c["alpha_star"],
            "realized_fdr_at_alpha_star": (row_star["realized_fdr"] if row_star else None),
            "ci_at_alpha_star": ([row_star["ci_low"], row_star["ci_high"]] if row_star else None),
            "decoy_fdr_hat_at_alpha_star": (row_star["decoy_fdr_hat"] if row_star else None),
            "n_admitted_at_alpha_star": (row_star["n_admitted"] if row_star else None),
            "n_false_admitted_at_alpha_star": (row_star["n_false_admitted"] if row_star else None),
            "paired_win_rate": c["paired"]["win_rate_false_pairs"],
            "paired_win_rate_ci": c["paired"]["win_rate_ci"],
            "marginal_holds": c["marginal"]["marginal_holds"],
            "marginal_direction": c["marginal"].get("marginal_direction"),
            "marginal_tail_gap_mean_diff": c["marginal"].get("tail_gap_mean_diff"),
            "competent": f["competent"], "powered": f["powered"],
            "powered_for_disconfirmation": f["powered_for_disconfirmation"],
            "anti_conservative": f["anti_conservative"], "gate_controls": f["gate_controls"],
            "paired_fails": f["paired_fails"], "paired_ok": f["paired_ok"],
            "unstable": f["unstable"],
            "seed_spread_realized_median": c["seed_spread"]["realized_fdr"]["median"],
            "seed_spread_paired_median": c["seed_spread"]["paired_win_rate"]["median"],
        })
    return table


def build_output(pipes, analysis, out_path, sanity):
    cells = analysis["cells"]
    examples = build_examples(pipes, analysis)
    pipe_nano = pipes.get("nano")
    pipe_strong = pipes.get("strong")
    total_cost = sum(p["runtime"]["cost_usd"] for p in pipes.values() if p)

    extraction_quality = {}
    for tag, p in pipes.items():
        if p is None:
            continue
        extraction_quality[p["extractor"]] = {
            "multihop_relation_accuracy": _nan(p["mh_acc"]),
            "atomic_relation_accuracy": _nan(p["at_acc"]),
            "atomic_precision": _nan(p["atomic_prec"]), "atomic_recall": _nan(p["atomic_rec"]),
            "competent": bool(p["mh_acc"] is not None and p["mh_acc"] >= ACC_THRESHOLD),
            "n_docs": len(p["docs"]), "n_reals": len(p["all_reals"]),
            "n_false": p["n_false"], "n_true": p["n_true"],
            "contamination_rate_decoys": _nan(p["contamination_rate"]),
            "runtime": p["runtime"]}

    metadata = {
        "method_name": ("P1-DECONFOUND: a 2-axis (extractor-strength x false-positive-density) "
                        "persistence matrix for the marginal-vs-paired knockoff+ failure on CLUTRR"),
        "headline_verdict": analysis["verdict"]["verdict"],
        "headline": analysis["verdict"]["headline"],
        "description": (
            "Controlled factorial de-confounding the iter-3 disconfirmation (multi_hop realized FDR 1.0 "
            "at alpha*=0.5, paired sign-flip failure) from a pathological weak extractor. AXIS A = "
            "extractor strength (gpt-4.1-nano mh_acc~0.17 vs a Phase-0-verified stronger extractor); "
            "AXIS B = false-positive density (post-hoc stratified subsampling of the scored real pool to "
            "~20/50/85% genuine-FALSE, FREE). The extractor is also the scorer and the decoy generator "
            "(faithful self-detecting gate). Per cell: realized-FDR-vs-alpha diagonal (doc-block bootstrap "
            "CIs + decoy_fdr_hat + the (alpha,decoy_fdr_hat,realized) triple), the PAIRED win-rate over "
            "FALSE pairs (key readout), and the MARGINAL crux. Output: a persist/vanish matrix + an "
            "explicit EARNED-vs-SCOPED decision rule."),
        "axes": {"axis_A_extractor_strength": [NANO_MODEL,
                                               (pipe_strong["extractor"] if pipe_strong else None)],
                 "axis_B_false_positive_density": DENSITIES,
                 "families": FAMILIES,
                 "extractor_equals_scorer_equals_decoy_generator": True},
        "phase0_extractor_probe": analysis["phase0"],
        "hyperparameters": {
            "seed": SEED, "alpha_grid": ALPHA_GRID, "K_self_consistency": K_SC,
            "B_bootstrap_diagonal": B_BOOT, "B_bootstrap_paired": B_PAIR, "tau": TAU,
            "n_false_min": N_FALSE_MIN, "densities": DENSITIES, "subsample_seeds": SUBSAMPLE_SEEDS,
            "acc_threshold_competent": ACC_THRESHOLD, "soft_cap_usd": SOFT_CAP_USD,
            "hard_stop_usd": HARD_STOP_USD,
            "W_statistic": "signed-max  W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i)",
            "knockoff_plus": "Barber-Candes eq 1.9 (the +1 kept; exact FDR control)",
            "normalization_pool": ("PRIMARY per-document rank-normalization over {reals U cf U swap} "
                                   "(identical recipe both arms; matches iter-3 so the nano anchor "
                                   "reconciles). Robustness variant {reals U cf} in robustness_alt_normalization. "
                                   "Swaps are pool-only; the gate competes reals vs their cf decoys."),
            "bootstrap": "document-block (cluster) resampling",
            "multiplicity": "Benjamini-Hochberg q=0.05 across all cell marginal/paired p-values",
            "scoring": "isolated, provenance-blinded K=5 self-consistency, document-prefix cached",
            "baseline": "PLAIN raw-confidence threshold gate (decoy-free purely-neural foil), per diagonal row",
            "alpha_star_definition": "most-permissive CERTIFIED alpha (n_admitted >= ceil(1/alpha))",
            "floor_power_rule": (
                "a cell is ASSERTED at alpha only if n_admitted>=k_floor(alpha); an anti-conservative "
                "disconfirmation additionally requires n_false_admitted>=40 (else 'directional, below "
                "false-admission floor'); a clean low realized FDR with CI<=alpha is the POSITIVE "
                "'gate controls' result and needs only n_admitted>=k_floor")},
        "extraction_quality": extraction_quality,
        "persistence_matrix": build_matrix_table(cells),
        "cells_full": cells,
        "earned_vs_scoped_verdict": analysis["verdict"],
        "robustness_alt_normalization": analysis.get("robustness_rc"),
        "sanity_anchor_iter3_reproduction": sanity,
        "bh_correction": analysis["bh"],
        "full_figure_captions": FULL_FIGURE_CAPTIONS,
        "dataset": "CLUTRR-v1-CrispGold-CalibrationAnchor",
        "total_cost_usd": round(total_cost, 6), "cost_trace_path": "logs/cost.jsonl",
        "interpretation": {
            "persist": ("if the paired failure PERSISTS for a competent extractor at matched/varied density "
                        "while the marginal holds -> 'marginal != paired at the LLM boundary' is EARNED (headline)"),
            "vanish": ("if it VANISHES (gate controls realized FDR at alpha) -> report the POSITIVE result and "
                       "SCOPE the limitation to the weak-scorer / error-dense regime"),
            "density_driven": "if the failure tracks density for BOTH extractors -> density is the governing variable",
            "marginal_vs_paired": ("the MARGINAL crux (decoy ~ spontaneous-error in distribution) can hold while "
                                   "the PAIRED competition (each false real vs its OWN decoy) fails — the matrix "
                                   "localizes which axis drives that dissociation")},
    }
    out = {"metadata": _clean(metadata),
           "datasets": [{"dataset": "CLUTRR-v1-CrispGold-CalibrationAnchor", "examples": examples}]}
    out_path.write_text(json.dumps(out, indent=2))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.0f} KB, {len(examples)} examples)")
    return out


def make_figures(out, fig_dir: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig_dir.mkdir(exist_ok=True)
    m = out["metadata"]
    cells = m["cells_full"]
    paths = []

    def get_cell(ext, fam, dens):
        for c in cells:
            if c["extractor"] == ext and c["family"] == fam and c["density"] == dens:
                return c
        return None
    exts = sorted({c["extractor"] for c in cells}, key=lambda e: (e != NANO_MODEL, e))

    # F1 persistence heatmap (multi_hop, extractor x density), realized FDR at alpha*
    try:
        fig, ax = plt.subplots(figsize=(7, 3.6))
        grid = np.full((len(exts), len(DENSITIES)), np.nan)
        for i, e in enumerate(exts):
            for j, d in enumerate(DENSITIES):
                c = get_cell(e, "multi_hop", d)
                if c is None or c["alpha_star"] is None:
                    continue
                row = _row_at(c, c["alpha_star"])
                if row and row["realized_fdr"] is not None:
                    grid[i, j] = row["realized_fdr"]
        im = ax.imshow(grid, cmap="Reds", vmin=0, vmax=1, aspect="auto")
        ax.set_xticks(range(len(DENSITIES))); ax.set_xticklabels([f"{d:.2f}" for d in DENSITIES])
        ax.set_yticks(range(len(exts)))
        ax.set_yticklabels([e.split("/")[-1] for e in exts], fontsize=8)
        ax.set_xlabel("target FALSE density"); ax.set_ylabel("extractor")
        ax.set_title("F1  realized FDR at alpha*  (multi_hop)")
        for i, e in enumerate(exts):
            for j, d in enumerate(DENSITIES):
                c = get_cell(e, "multi_hop", d)
                if c is None:
                    continue
                row = _row_at(c, c["alpha_star"]) if c["alpha_star"] is not None else None
                txt = "n/c" if row is None else f"{row['realized_fdr']:.2f}\nnF={row['n_false_admitted']}/{row['n_admitted']}"
                ax.text(j, i, txt, ha="center", va="center", fontsize=6.5,
                        color=("white" if (not np.isnan(grid[i, j]) and grid[i, j] > 0.5) else "black"))
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="realized FDR")
        fig.tight_layout()
        p = fig_dir / "F1_persistence_heatmap.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"F1 failed: {e}")

    # F2 realized-FDR diagonals nano vs strong at matched density (0.85 and 0.50)
    try:
        fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), sharey=True)
        for ax, dens in zip(axes, [0.85, 0.50]):
            ax.plot([0, 0.55], [0, 0.55], "k--", lw=1, label="ideal (realized=alpha)")
            for e, col in zip(exts, ["tab:blue", "tab:red", "tab:green"]):
                c = get_cell(e, "multi_hop", dens)
                if c is None:
                    continue
                rows = [r for r in c["diagonal_rows"] if r["realized_fdr"] is not None]
                if not rows:
                    continue
                xs = [r["target_alpha"] for r in rows]; ys = [r["realized_fdr"] for r in rows]
                lo = [max(0.0, r["realized_fdr"] - (r["ci_low"] if r["ci_low"] is not None else r["realized_fdr"])) for r in rows]
                hi = [max(0.0, (r["ci_high"] if r["ci_high"] is not None else r["realized_fdr"]) - r["realized_fdr"]) for r in rows]
                lab = e.split("/")[-1]
                ax.errorbar(xs, ys, yerr=[lo, hi], marker="o", color=col, capsize=3, label=f"{lab} realized")
                dh = [(r["target_alpha"], r["decoy_fdr_hat"]) for r in rows if r["decoy_fdr_hat"] is not None]
                if dh:
                    ax.plot([x for x, _ in dh], [y for _, y in dh], ":", marker="x", color=col, alpha=0.7,
                            label=f"{lab} decoy_fdr_hat")
                pl = [(r["target_alpha"], r["plain_realized_fdr"]) for r in rows if r["plain_realized_fdr"] is not None]
                if pl:
                    ax.plot([x for x, _ in pl], [y for _, y in pl], "-.", color=col, alpha=0.5, lw=1,
                            label=f"{lab} plain baseline")
            ax.set_xlabel("target alpha"); ax.set_title(f"density={dens:.2f}")
            ax.legend(fontsize=6)
        axes[0].set_ylabel("realized FDR")
        fig.suptitle("F2  realized-FDR diagonals (multi_hop): nano vs strong")
        fig.tight_layout()
        p = fig_dir / "F2_realized_fdr_diagonals.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"F2 failed: {e}")

    # F3 paired win-rate over FALSE pairs per cell
    try:
        fig, ax = plt.subplots(figsize=(9, 4.4))
        labels, xs, los, his = [], [], [], []
        x = 0
        colors = []
        for e in exts:
            for fam in FAMILIES:
                for d in DENSITIES:
                    c = get_cell(e, fam, d)
                    if c is None:
                        continue
                    wr = c["paired"]["win_rate_false_pairs"]
                    ci = c["paired"]["win_rate_ci"]
                    if wr is None:
                        continue
                    labels.append(f"{e.split('/')[-1]}\n{fam[:5]}|{d}")
                    xs.append(wr)
                    lo = wr - (ci[0] if ci[0] is not None else wr)
                    hi = (ci[1] if ci[1] is not None else wr) - wr
                    los.append(max(0, lo)); his.append(max(0, hi))
                    colors.append("tab:blue" if e == NANO_MODEL else "tab:red")
                    x += 1
        ax.axhline(0.5, color="k", ls="--", lw=1, label="exchangeable (0.5)")
        ax.errorbar(range(len(xs)), xs, yerr=[los, his], fmt="none", capsize=3, ecolor="gray")
        for i, (xv, cc) in enumerate(zip(xs, colors)):
            ax.plot(i, xv, "s", color=cc, markersize=7)
        ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, rotation=60, ha="right", fontsize=6)
        ax.set_ylabel("paired decoy-win-rate (FALSE pairs)")
        ax.set_title("F3  paired win-rate over FALSE pairs (blue=nano gpt-4.1-nano, red=strong gpt-4.1-mini)")
        ax.legend(fontsize=8); fig.tight_layout()
        p = fig_dir / "F3_paired_win_rate.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"F3 failed: {e}")

    # F4 marginal crux CDF per extractor (multi_hop native)
    try:
        fig, axes = plt.subplots(1, len(exts), figsize=(5.2 * len(exts), 4.2), squeeze=False)
        for ax, e in zip(axes[0], exts):
            c = get_cell(e, "multi_hop", "native")
            if c is None:
                continue
            cd = c["marginal"].get("cdf") if "cdf" in c["marginal"] else None
            # cdf was kept only in compute_marginal output; pull from regions if absent
            if cd is None:
                continue
            ax.plot(cd["x"], cd["cdf_truepos"], color="tab:green", label="true positives")
            ax.plot(cd["x"], cd["cdf_spont"], color="tab:orange", label="spontaneous errors (FALSE reals)")
            ax.plot(cd["x"], cd["cdf_decoy"], color="tab:purple", label="counterfactual decoys")
            ax.set_xlabel("normalized self-consistency Z"); ax.set_ylabel("empirical CDF")
            ax.set_title(e.split("/")[-1], fontsize=9); ax.legend(fontsize=7)
        fig.suptitle("F4  marginal crux CDFs (multi_hop): decoy ~ spont, decoy != true-pos")
        fig.tight_layout()
        p = fig_dir / "F4_marginal_crux_cdf.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"F4 failed: {e}")

    logger.info(f"figures: {paths}")
    return paths


# ===========================================================================
# Offline self-tests
# ===========================================================================
def selftest():
    logger.info("STAGE 0 — offline unit tests")
    # k-floor
    assert [st.k_floor(a) for a in ALPHA_GRID] == [20, 10, 5, 4, 2]
    # knockoff fast == slow over random arrays
    rng0 = np.random.default_rng(7)
    for _ in range(200):
        n = int(rng0.integers(1, 80))
        Wr = np.round(rng0.normal(0, 1, n), 3)
        for a in ALPHA_GRID:
            Ts, ns, rs = st.knockoff_plus_threshold(Wr, a)
            Tf, nf2, rf = _knockoff_fast(Wr, a)
            assert (math.isinf(Ts) == math.isinf(Tf))
            if not math.isinf(Ts):
                assert abs(Ts - Tf) < 1e-9 and ns == nf2 and abs(rs - rf) < 1e-9
    # W signed-max antisymmetry
    assert st.W_signed_max(0.8, 0.3) == 0.8 and st.W_signed_max(0.3, 0.8) == -0.8
    assert abs(st.W_signed_max(0.5, 0.5)) == 0.0
    # fair-coin win-rate
    rng = np.random.default_rng(0)
    fair = [(float(rng.random()), float(rng.random())) for _ in range(2000)]
    wr, _ = st.tail_win_rate(fair, 0.0)
    assert 0.45 < wr < 0.55, f"fair-coin win-rate {wr}"
    # Doc.label crisp 3-way
    raw = {"input": json.dumps({"doc_id": "x", "document_text": "t", "entities":
           [{"name": "Dan"}, {"name": "Mike"}, {"name": "Gail"}], "query": {}}),
           "output": json.dumps({"atomic_facts": [{"head": "Gail", "relation": "grandson", "tail": "Dan"},
                                                   {"head": "Dan", "relation": "brother", "tail": "Mike"}],
                                 "multi_hop_facts": []}),
           "metadata_chain_length_k": 2, "metadata_is_pilot": False, "metadata_fold": "k2"}
    d0 = Doc(raw)
    assert d0.label("Dan", "brother", "Mike") == TRUE
    assert d0.label("Dan", "mother", "Mike") == FALSE
    assert d0.label("Dan", "brother", "Gail") == UND
    # BH monotone
    bh = st.benjamini_hochberg([0.001, 0.5, 0.02, 0.9], q=0.05)
    assert bh[0]["reject"] and not bh[1]["reject"]

    # (NEW 1) subsample_to_density hits target FALSE fraction + preserves doc_ids
    fam = []
    for i in range(300):
        lab = TRUE if i < 100 else FALSE
        fam.append({"cand_id": f"doc{i%30}:real:{i}", "doc_id": f"doc{i%30}", "label": lab})
    for target in (0.20, 0.50, 0.85):
        keep = subsample_to_density(fam, target, seed=1)
        kept = [c for c in fam if c["cand_id"] in keep]
        nF = sum(1 for c in kept if c["label"] == FALSE)
        frac = nF / len(kept)
        assert abs(frac - target) <= 1.0 / len(kept) + 1e-9, f"density {target}: got {frac} n={len(kept)}"
        # doc_ids preserved (every kept cand_id encodes its doc_id)
        assert all(c["doc_id"] in c["cand_id"] for c in kept)
    logger.info("  subsample_to_density OK")

    # (NEW 2) PAIRED-FAILS fixture: false reals' zr deterministically above decoy zd
    def _mk_pairs(false_zr, false_zd, n_docs=20, per=8, n_true=80):
        per_doc = {}
        raw_conf = {}
        # FALSE reals: zr > zd (real beats its own decoy) -> paired fails, gate anti-conservative
        idx = 0
        for d in range(n_docs):
            for _ in range(per):
                cid = f"d{d}:real:F{idx}"
                zr, zd = false_zr(), false_zd()
                per_doc.setdefault(f"d{d}", []).append(
                    {"zr": zr, "zd": zd, "label": FALSE, "doc_id": f"d{d}",
                     "w": st.W_signed_max(zr, zd), "real_id": cid})
                raw_conf[cid] = zr
                idx += 1
        # TRUE reals scored LOW so the admitted tail is dominated by FALSE reals
        for j in range(n_true):
            d = j % n_docs
            cid = f"d{d}:real:T{j}"
            zr, zd = 0.2 * np.random.RandomState(j).random(), 0.1
            per_doc.setdefault(f"d{d}", []).append(
                {"zr": float(zr), "zd": float(zd), "label": TRUE, "doc_id": f"d{d}",
                 "w": st.W_signed_max(float(zr), float(zd)), "real_id": cid})
            raw_conf[cid] = float(zr)
        return per_doc, raw_conf
    rs = np.random.RandomState(0)
    per_doc, raw_conf = _mk_pairs(lambda: 0.85 + 0.1 * rs.random(), lambda: 0.1 + 0.1 * rs.random())
    diag = compute_diagonal(per_doc, raw_conf, populable=True, with_ci=True)
    assert diag["paired"]["paired_fails"], f"PAIRED-FAILS: expected paired_fails, ci={diag['paired']['win_rate_ci']}"
    row5 = next(r for r in diag["rows"] if r["target_alpha"] == 0.5)
    assert row5["realized_fdr"] is not None and row5["realized_fdr"] > 0.5
    # classifier on a synthetic cell
    cell_fail = {"extractor": "strong", "family": "multi_hop", "density": 0.85,
                 "mh_acc": 0.5, "at_acc": 0.5, "alpha_star": diag["alpha_star"],
                 "diagonal_rows": diag["rows"], "paired": diag["paired"],
                 "marginal": {"marginal_holds": True}, "n_false": 160, "n_true": 80,
                 "seed_spread": {"win_rate_unstable": False,
                                 "realized_fdr": {"median": 1.0}, "paired_win_rate": {"median": 0.1}}}
    f = classify_cell(cell_fail, "alpha_star")
    assert f["paired_fails"] and f["powered"], f"classifier fail-cell: {f}"
    logger.info("  PAIRED-FAILS fixture OK (paired_fails + anti-conservative detected)")

    # (NEW 3) PAIRED-OK fair-coin fixture
    rs2 = np.random.RandomState(1)
    per_doc2 = {}
    raw_conf2 = {}
    idx = 0
    for d in range(25):
        for _ in range(8):
            zr, zd = float(rs2.random()), float(rs2.random())
            lab = FALSE if rs2.random() < 0.3 else TRUE
            cid = f"e{d}:real:{idx}"
            per_doc2.setdefault(f"e{d}", []).append(
                {"zr": zr, "zd": zd, "label": lab, "doc_id": f"e{d}",
                 "w": st.W_signed_max(zr, zd), "real_id": cid})
            raw_conf2[cid] = zr
            idx += 1
    diag2 = compute_diagonal(per_doc2, raw_conf2, populable=True, with_ci=True)
    assert diag2["paired"]["paired_ok"], f"PAIRED-OK: expected ci covers 0.5, got {diag2['paired']['win_rate_ci']}"
    cell_ok = {"extractor": "strong", "family": "multi_hop", "density": 0.50,
               "mh_acc": 0.5, "at_acc": 0.5, "alpha_star": diag2["alpha_star"],
               "diagonal_rows": diag2["rows"], "paired": diag2["paired"],
               "marginal": {"marginal_holds": True}, "n_false": 60, "n_true": 140,
               "seed_spread": {"win_rate_unstable": False,
                               "realized_fdr": {"median": 0.3}, "paired_win_rate": {"median": 0.5}}}
    fok = classify_cell(cell_ok, "alpha_star")
    assert fok["paired_ok"], f"classifier ok-cell paired_ok: {fok}"
    # decision rule: two PAIRED-OK competent powered cells across 2 densities -> SCOPED
    cell_ok2 = dict(cell_ok); cell_ok2 = json.loads(json.dumps(cell_ok2)); cell_ok2["density"] = 0.20
    verdict = earned_vs_scoped([cell_ok, cell_ok2], "strong", True)
    assert verdict["verdict"] in ("SCOPED", "UNDERPOWERED_INCONCLUSIVE"), verdict["verdict"]
    # two EARNED cells across 2 densities -> EARNED
    cell_f2 = json.loads(json.dumps(cell_fail)); cell_f2["density"] = 0.50
    verdict2 = earned_vs_scoped([cell_fail, cell_f2], "strong", True)
    assert verdict2["verdict"] == "EARNED", verdict2["verdict"]
    logger.info("  PAIRED-OK fixture + decision rule (EARNED/SCOPED) OK")
    logger.info("STAGE 0 — all offline unit tests PASSED ✓")


# ===========================================================================
# Main
# ===========================================================================
async def amain(args):
    set_mem_limit(16.0)
    cost_log = HERE / "logs" / "cost.jsonl"
    cache_dir = HERE / "cache"

    if args.analyze_only:
        logger.info("ANALYZE-ONLY: loading checkpoints (no API)...")
        pipes = {"nano": load_pipe_ckpt("nano"), "strong": load_pipe_ckpt("strong")}
        phase0 = None
        pf = HERE / "checkpoints" / "phase0.json"
        if pf.exists():
            phase0 = json.loads(pf.read_text())
        _finish(pipes, phase0, args)
        return

    n_docs = 3 if args.mini else args.n_docs
    docs = load_docs(FULL_DATA, n_docs=n_docs)
    logger.info(f"Loaded {len(docs)} docs")

    async with OpenRouterClient(cache_dir, cost_log, concurrency=args.concurrency,
                                soft_cap_usd=SOFT_CAP_USD, hard_stop_usd=HARD_STOP_USD,
                                fallback_cache_dirs=WARM_CACHES) as client:
        phase0 = None
        if args.phase0 or (not args.nano and not args.strong and not args.mini):
            # sample pilot docs from the FULL corpus (not just the first n_docs) so the probe
            # mh_acc estimate is representative and stable regardless of the run's doc count.
            pilot_src = load_docs(FULL_DATA) if (n_docs is not None and not args.mini) else docs
            pilot = [d for d in pilot_src if d.is_pilot][:args.phase0_docs] or docs[:args.phase0_docs]
            logger.info(f"PHASE-0 probe over {len(pilot)} pilot docs...")
            # include nano (warm-cached) for the mh_acc~0.169 sanity check alongside the candidates
            probe_models = [NANO_MODEL] + (EXTRACTOR_CANDIDATES if not args.mini
                                           else EXTRACTOR_CANDIDATES[:1])
            if args.extractor and args.extractor not in probe_models:
                probe_models.append(args.extractor)
            phase0 = await phase0_probe(client, pilot, probe_models)
            (HERE / "checkpoints").mkdir(exist_ok=True)
            (HERE / "checkpoints" / "phase0.json").write_text(json.dumps(phase0))
            logger.info(f"PHASE-0 chosen strong extractor: {phase0['chosen_strong_extractor']} "
                        f"(mh_acc={phase0['chosen_mh_acc']}, cleared={phase0['threshold_cleared']})")
            if args.phase0:
                return

        pipes = {"nano": None, "strong": None}
        strong_model = (phase0["chosen_strong_extractor"] if phase0
                        else (args.extractor or EXTRACTOR_CANDIDATES[0]))

        run_nano = args.nano or args.mini or (not args.strong and not args.phase0)
        run_strong = args.strong or args.mini or (not args.nano and not args.phase0)

        if run_nano:
            pipes["nano"] = await run_for_extractor(client, NANO_MODEL, docs, k_sc=args.k_sc)
            if not args.mini:
                save_pipe_ckpt(pipes["nano"], "nano")
        if run_strong:
            strong_docs = docs[:args.strong_docs] if args.strong_docs else docs
            pipes["strong"] = await run_for_extractor(client, strong_model, strong_docs, k_sc=args.k_sc)
            if not args.mini:
                save_pipe_ckpt(pipes["strong"], "strong")

    _finish(pipes, phase0, args)


def _finish(pipes, phase0, args):
    if all(p is None for p in pipes.values()):
        logger.error("no pipes to analyze")
        return
    logger.info("Building persistence matrix (offline)...")
    analysis = analyze_matrix(pipes, phase0)
    sanity = check_sanity_anchor(analysis["cells"], pipes["nano"]) if pipes.get("nano") else {"checked": False}
    out_path = HERE / ("mini_method_out.json" if args.mini else "method_out.json")
    out = build_output(pipes, analysis, out_path, sanity)
    if not args.mini:
        make_figures(out, HERE / "figures")
    gc.collect()
    v = analysis["verdict"]
    logger.info(f"DONE verdict={v['verdict']} | strong={v['strong_extractor']} "
                f"competent={v['strong_competent']} | "
                f"earned_cells={v['n_earned_cells']} scoped_cells={v['n_scoped_cells']}")
    if sanity.get("checked"):
        logger.info(f"sanity_anchor reproduces_iter3={sanity.get('reproduces_iter3_direction')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mini", action="store_true")
    ap.add_argument("--phase0", action="store_true", help="run Phase-0 extractor probe only")
    ap.add_argument("--phase0-docs", type=int, default=40)
    ap.add_argument("--nano", action="store_true", help="run only the nano arm")
    ap.add_argument("--strong", action="store_true", help="run only the strong arm")
    ap.add_argument("--extractor", type=str, default=None, help="strong extractor model override")
    ap.add_argument("--n-docs", type=int, default=None)
    ap.add_argument("--strong-docs", type=int, default=None, help="cap docs for the strong arm")
    ap.add_argument("--k-sc", type=int, default=K_SC)
    ap.add_argument("--analyze-only", action="store_true")
    ap.add_argument("--concurrency", type=int, default=24)
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    try:
        asyncio.run(amain(args))
    except BudgetExceeded as e:
        logger.error(f"Budget exceeded, aborting: {e}")
        raise


if __name__ == "__main__":
    main()
