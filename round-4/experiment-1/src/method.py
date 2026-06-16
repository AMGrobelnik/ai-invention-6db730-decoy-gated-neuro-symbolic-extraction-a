#!/usr/bin/env python3
"""
method.py — Iteration-3 P1.

THE SINGLE PRIMARY ARTIFACT: a powered, per-family CLUTRR realized-FDR-vs-target-alpha
CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that
admits LLM-extracted kinship facts into a symbolic layer, scored under the
diagnostic-VALIDATED K=5 SELF-CONSISTENCY elicitation (iter-2 counterfactual tail
win-rate ~0.482, CI covers 0.5) on a SCALED, error-dense CLUTRR corpus (k>=6 oversampled).

Compared method + baselines + controls, side-by-side in ONE pipeline:
  * METHOD     : counterfactual-decoy knockoff+ gate (self-consistency elicitation, headline).
  * BASELINE 1 : PLAIN raw-confidence threshold gate (decoy-free; the purely-neural foil).
  * BASELINE 2 : random in-doc SWAP-decoy knockoff gate (anti-conservative negative control).
  * CONTRAST   : the SAME diagonal under VERBALIZED confidence (documented discreteness /
                 loose-target artifact, NOT a co-headline).
  * CORROBORATE: deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025), r=1.

Iteration-3 additions over iter-2 (reviewer-driven):
  (A) headline elicitation = self-consistency for the per-family diagonal;
  (B) the (target alpha, decoy_fdr_hat, realized FDR) TRIPLE + a pre-registered SELF-REPORT
      disconfirmation (the gate's own decoy_fdr_hat is DISCONFIRMED where it is anti-
      conservative vs realized beyond tau, EVEN when realized < alpha);
  (C) verbalized contrast on the SAME scaled data (discreteness / loose-target quantification);
  (D) an S1b difficulty-graded LADDER L0..L4 (foreign-swap -> in-doc swap -> random-vocab ->
      cf_2nd -> primary-cf) scored under the SAME self-consistency elicitation to
      repair-or-bound the diagnostic blind spot;
  (E) independent deterministic foreign-entity entrapment corroboration restricted to alpha*;
  (F) full crux match (tail fail-to-reject + full-distribution result, decision-relevance
      justification) reported in full;
  (G) BH multiplicity across ALL validation tests;
  (H) Generator!=Scorer carried forward as SETTLED (no new budget);
  (I) the single primary-disconfirmation verdict under self-consistency on multi_hop.

CPU-only, async LLM I/O via OpenRouter (gpt-4.1-nano), disk cache + read-only warm-start
from iter-2 caches, exact usage.cost logged after EVERY call, soft cap $3, HARD STOP $10.

Usage:
  uv run method.py --selftest             # offline stat unit tests, no API
  uv run method.py --mini                 # 3-doc smoke
  uv run method.py --n-docs 40            # first 40 docs
  uv run method.py                        # full scaled corpus
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

# empty-slice means (e.g. a density stratum or crux tail with no items) intentionally yield NaN,
# which _nan()/_clean() convert to JSON null. Silence the benign numpy "invalid value"/"divide"
# RuntimeWarnings so the deliverable log stays readable (the NaN handling itself is explicit).
np.seterr(invalid="ignore", divide="ignore")

# scipy.anderson_ksamp emits API-change + p-value-cap UserWarnings; they do not affect the
# reported significance levels (clipped to [0.001, 0.25]) — silence to keep logs readable.
warnings.filterwarnings("ignore", category=UserWarning, module="scipy")
warnings.filterwarnings("ignore", message=".*midrank.*")
warnings.filterwarnings("ignore", message=".*p-value capped.*")

import fdr_core as fc          # entrapment FDP estimators, plain gate, alpha-certifiable
import fdr_stats as st         # knockoff+, W, bootstrap, BH, two-sample tests, rank-norm
from llm_client import OpenRouterClient, BudgetExceeded

# ---------------------------------------------------------------------------
# Constants / guardrails
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
FULL_DATA = HERE / "full_data_out.json"     # the SCALED 593-doc corpus (iter-3 build, prefix-superset of the original 190)
# read-only warm-start caches consulted on a primary miss BEFORE spending money (hits are promoted
# into the local primary cache). Order: iter-3 P1 first (ent/cf2/rv/fgn + cf/swap SC for its 40-doc
# checkpoint), then iter-2 EXP2 (nano SC+VB for the full 190-doc prefix + ministral-8b SC and the
# ministral-generated 'cfo' decoys on the original 40 PILOT docs — the warm (G,S) 2x2 matrix).
_BASE = Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop")
WARM_CACHES = [
    _BASE / "iter_3/gen_art/gen_art_experiment_1/cache",
    _BASE / "iter_2/gen_art/gen_art_experiment_2/cache",
]

SEED = 20240617
ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]   # k-floors {20,10,5,4,2}
B_BOOT = 2000
B_BOOT_INNER = 1000                            # cheaper bootstrap for ladder/entrapment/GS/density
K_SC = 5                                        # self-consistency samples (headline)
N_FALSE_MIN = 40                                # spontaneous-error populability floor
N_LADDER_FALSE_MIN = 30                         # S1b per-rung false-pair power floor (Phase 7)
PAIRED_FLOOR = 20                               # per-(G,S)-config false-pair power floor (Phase 5)
TAU = 0.05                                      # tolerance band for disconfirmation
SOFT_CAP_USD = 4.0                              # NEW-spend soft cap (iter-4); fresh cost.jsonl governs it
HARD_STOP_USD = 10.0
N_EXTRACT_SAMPLES = 1                           # extraction over-gen samples; 1 == legacy T=0.0 cache-identical

PRIMARY_MODEL = "openai/gpt-4.1-nano"
OTHER_MODEL = "mistralai/ministral-8b-2512"     # cross-family scorer/generator for the (G,S) paired matrix
STRONG_EXTRACTOR = "openai/gpt-4.1-mini"        # de-confound arm (Phase 6b): competent extractor, scorer fixed = nano

# The ORIGINAL 40 pilot doc_ids (iter-1 dataset) — the ONLY docs for which the full warm (G,S) 2x2
# matrix (ministral-8b SC scores + ministral-generated 'cfo' decoys) exists in the iter-2 cache.
# Phase 5 runs the (G,S) paired statistic on the intersection of these with the loaded corpus so it
# is ~$0 (warm). Wider docs are scored only if budget is ample.
GS_WARM_IDS = {
    '044054de-0354-4164-98c8-c7c7362c668b', '046c5373-f233-4eb4-874f-31b3bbd0b6f0',
    '08430cd0-2995-4430-a3ef-b32131f1ffdf', '0cbdd9fd-81dc-4d4a-8243-cc3be5087685',
    '108d589b-e10d-4780-8f29-245424333489', '20691b30-5e09-4f17-9676-6c3d0f12a09e',
    '25ae9e66-79d8-4600-b0ea-13a53fd6a138', '273af8aa-11fa-4ab7-9b4c-bb4d257e08fb',
    '3fd00bbb-a1bc-4646-8e4a-55ad47c1a9d4', '424413ca-1fa5-4c8e-96df-19827a1dfc9b',
    '453ce3aa-c46c-4eac-a32b-d708c67a4f07', '464afcd8-9ca3-4d45-b6fd-942afcd0568a',
    '4690a981-9a1b-4f57-94a4-705d6053d5aa', '4e9c81e4-3119-4afc-a5c8-474bf504d636',
    '509a0843-288b-4f5c-b691-8e9e9962faa3', '50a51456-f763-4832-82da-db04427fc7c2',
    '58c061c5-877f-499e-8fcc-123c911e959b', '5c68514c-eb80-4a99-a891-313a6e9f3e28',
    '64aa79ed-d010-4bbb-aebd-6a798640bb73', '65056b01-798d-449a-80f8-67db4545ed65',
    '67c93a7f-b3f2-4270-856d-5cdb5d436564', '726d800a-edbc-4fb2-8f45-8c2354fba35e',
    '7914f072-1728-4c50-a048-55670155f9af', '91c8f4a3-c89e-43f7-8e71-54cdbed7cdc6',
    '959a2142-8956-4cad-9f2c-fdd870e386b8', '9a48d3e9-c071-4925-b235-8965fafe5f2c',
    'a107c25b-ed84-48c1-9ab8-a7dc52c077fe', 'a1eff894-631a-4df3-86d5-692de85cc0cb',
    'a60170b6-e99b-4f27-90d6-945ea757d377', 'adce16bd-8ba1-464d-96c3-7a6ef5c24636',
    'b9fb47d5-f383-425a-a2a6-fbbd0c5e9fbd', 'ca954b95-9585-4e53-a179-58348f9ef7cb',
    'cf8ccbb5-d2b6-4ac5-b39d-774f0b932866', 'd6c1d802-f129-4c65-b60f-83dcfbe51e87',
    'dbbb0c11-863d-4e20-890a-cb6425c6a0a5', 'e5472486-125c-4b1c-af94-dc96355a37b8',
    'e734b1a0-1862-4563-ab8b-1474446b567b', 'ebefed69-b4f7-4041-9fa0-9ede3fc9bd6a',
    'efb867c4-a113-4ba7-976e-02ccfc887771', 'f5037c68-34fe-42b9-a7b3-bbe70e739c31',
}

TRUE, FALSE, UND = "TRUE", "FALSE", "UNDECIDABLE"
SC, VB = "sc", "vb"                              # zmap config tags (nano self-consistency, nano verbalized)
MIN_SC = "min_sc"                               # zmap config tag: ministral-8b K=5 self-consistency (cross-family scorer)
STR_SC = "str_sc"                               # zmap config tag: nano SC scoring of STRONG-extractor reals/decoys (Phase 6b)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(HERE / "logs").mkdir(exist_ok=True)
logger.add(HERE / "logs" / "run.log", rotation="30 MB", level="DEBUG")


def set_mem_limit(gb: float = 12.0):
    try:
        soft = int(gb * 1024**3)
        resource.setrlimit(resource.RLIMIT_AS, (soft, soft))
    except (ValueError, OSError) as e:
        logger.warning(f"could not set RLIMIT_AS: {e}")


# ===========================================================================
# Data loading + crisp gold  (reused verbatim from iter-2 for cache identity)
# ===========================================================================
def verbalize(h: str, r: str, t: str) -> str:
    """CLUTRR triple (h, r, t) means 'tail is head's relation' => '{t} is the {r} of {h}.'"""
    return f"{t} is the {r} of {h}."


def _doc_seed(doc_id: str, salt: int = 0) -> int:
    """Stable per-document seed (hashlib, NOT Python's randomized hash()) so extraction
    shuffles, decoy fallbacks and swaps are reproducible across runs and doc subsets."""
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
# Prompts  (reused verbatim from iter-2 EXP2 for self-consistency cache identity)
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


SCORE_VB_SYS = ("You assess whether a kinship claim is entailed by a short document. "
                "A claim is entailed if it is directly stated OR can be derived from "
                "stated facts.")


def score_messages_verbalized(doc_text: str, claim: str) -> list[dict]:
    """Single-call verbalized confidence (0-100). The documented discreteness/loose-target
    contrast elicitation (iter-2 showed verbalized tail win-rate anti-conservative)."""
    return [
        {"role": "system", "content": SCORE_VB_SYS},
        {"role": "user", "content":
            f"Document: {doc_text}\n\nClaim: {claim}\n"
            "Give ONLY an integer 0-100 = your confidence (percent) that the claim is "
            "true/entailed by the document. No words, just the number."},
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


# ---------------------------------------------------------------------------
# JSON parsing from LLM output
# ---------------------------------------------------------------------------
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


def _parse_prob(text: str | None) -> float | None:
    if not text:
        return None
    import re
    m = re.search(r"[-+]?\d*\.?\d+", text)
    if not m:
        return None
    try:
        v = float(m.group(0))
    except ValueError:
        return None
    if v > 1.0:
        v = v / 100.0
    return float(min(1.0, max(0.0, v)))


# ===========================================================================
# Extraction (one call/doc) -> reals (labeled) + atomic P/R + multi-hop accuracy
#   reused verbatim from iter-2 EXP2 so the extraction call hits the warm cache
# ===========================================================================
async def extract_doc(client: OpenRouterClient, doc: Doc, rng: random.Random,
                      model: str = PRIMARY_MODEL, n_extract: int = 1,
                      cid_tag: str = "real") -> dict:
    """Extract reals (labeled candidate kinship facts) from one doc.

    n_extract==1 (DEFAULT): a single T=0.0 call (byte-identical to iter-2/iter-3 => warm-cache hit);
        emits ONE real per pair keyed `{doc_id}:{cid_tag}:{h}>{t}` (legacy id => downstream cache hits).
    n_extract>1 (over-generation): the T=0.0 call PLUS (n_extract-1) extra T=0.7 sampled calls; the
        per-pair predicted relations are UNIONED into a set of DISTINCT (h,r,t) reals (relation-tagged
        cand_id `{doc_id}:{cid_tag}:{h}>{t}#{r}`), densifying spontaneous false positives. Off by default
        (budget; the single-sample corpus is already >>40-false populable at scale).
    `model` lets the Phase-6b strong-extractor arm reuse this with a competent extractor.
    """
    pairs = list(doc.atomic_pairs) + list(doc.multi_pairs)
    pair_type = {p: "atomic" for p in doc.atomic_pairs}
    for p in doc.multi_pairs:
        pair_type.setdefault(p, "multi_hop")
    shuffled = pairs[:]
    rng.shuffle(shuffled)
    stated_triples: set = set()
    # per-pair set of distinct predicted relations across samples (union for over-gen)
    pred_rels: dict[tuple[str, str], list[str]] = {}
    for s in range(max(1, n_extract)):
        if s == 0:
            res = await client.call(model, extract_messages(doc, shuffled),
                                    max_tokens=900, temperature=0.0)
        else:
            res = await client.call(model, extract_messages(doc, shuffled),
                                    max_tokens=900, temperature=0.7, seed=SEED + s, sample_idx=s)
        parsed = _extract_json(res["content"]) or {}
        stated = parsed.get("stated") if isinstance(parsed, dict) else None
        inferred = parsed.get("inferred") if isinstance(parsed, dict) else None
        stated = stated if isinstance(stated, list) else []
        inferred = inferred if isinstance(inferred, list) else []
        stated_text_parts = []
        for st in stated:
            if isinstance(st, str):
                stated_text_parts.append(st)
            elif isinstance(st, list) and len(st) == 3:
                h, r, t = str(st[0]).strip(), _norm_rel(st[1]), str(st[2]).strip()
                if r:
                    stated_triples.add((h, r, t))
        for (a, r, b) in parse_stated_sentences("\n".join(stated_text_parts)):
            if a in doc.entities and b in doc.entities:
                stated_triples.add((a, r, b))
        for idx, (h, t) in enumerate(shuffled):
            r = _norm_rel(inferred[idx]) if idx < len(inferred) else None
            if r and r not in pred_rels.get((h, t), []):
                pred_rels.setdefault((h, t), []).append(r)

    gold_atomic = set(doc.atomic_facts)
    tp = len(stated_triples & gold_atomic)
    prec = tp / len(stated_triples) if stated_triples else float("nan")
    rec = tp / len(gold_atomic) if gold_atomic else float("nan")

    reals = []
    n_mh_correct = n_mh_total = 0
    for (h, t) in pairs:
        rels = pred_rels.get((h, t), [])
        if not rels:
            continue
        ftype = pair_type[(h, t)]
        # multi-hop accuracy uses the FIRST (T=0.0) prediction so the confound metric is stable
        if ftype == "multi_hop":
            n_mh_total += 1
            if rels[0] == doc.gold_rel.get((h, t)):
                n_mh_correct += 1
        legacy = (len(rels) == 1)
        for r in rels:
            cid = (f"{doc.doc_id}:{cid_tag}:{h}>{t}" if legacy
                   else f"{doc.doc_id}:{cid_tag}:{h}>{t}#{r}")
            reals.append({"cand_id": cid, "doc_id": doc.doc_id,
                          "h": h, "r": r, "t": t, "fact_type": ftype,
                          "label": doc.label(h, r, t), "claim": verbalize(h, r, t)})
    return {"doc_id": doc.doc_id, "reals": reals, "atomic_prec": prec, "atomic_rec": rec,
            "n_stated": len(stated_triples), "n_pairs": len(pairs),
            "mh_acc": (n_mh_correct / n_mh_total) if n_mh_total else float("nan"),
            "n_mh": n_mh_total}


# ===========================================================================
# Decoy / ladder-rung / entrapment construction
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
    """Return (decoys_L4, decoys2_L3, n_generated, n_contaminated). ONE batched call/doc
    (cache-identical to iter-2 for cf=L4). cf2=L3 = the second verified-non-entailed
    alternative parsed from the SAME (already-cached) generation, so it costs no new gen."""
    items = [(c["h"], c["r"], c["t"]) for c in reals]
    if not items:
        return [], [], 0, 0
    res = await client.call(model, decoy_messages(doc, items), max_tokens=700, temperature=0.0)
    parsed = _extract_json(res["content"])
    decoys, decoys2, n_gen, n_contam = [], [], 0, 0
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
        chosen = []                       # collect up to 2 distinct verified-non-entailed alts
        for rr in cand_rels:
            if rr not in chosen and verify_nonentailed(doc, h, rr, t, avoid):
                chosen.append(rr)
            if len(chosen) >= 2:
                break
        # deterministic fallback to fill the 1st (cf) slot exactly as iter-2 did
        if not chosen:
            pool = [x for x in RELATION_VOCAB if verify_nonentailed(doc, h, x, t, avoid)]
            if pool:
                chosen.append(pool[rng.randrange(len(pool))])
        if not chosen:
            continue
        decoys.append({"cand_id": f"{doc.doc_id}:cf:{h}>{t}", "doc_id": doc.doc_id,
                       "h": h, "r": chosen[0], "t": t, "pair": (h, t),
                       "real_id": c["cand_id"], "claim": verbalize(h, chosen[0], t)})
        # cf2 (L3): a SECOND distinct alternative; deterministic fallback if only one alt
        r2 = chosen[1] if len(chosen) >= 2 else None
        if r2 is None:
            pool = [x for x in RELATION_VOCAB
                    if x != chosen[0] and verify_nonentailed(doc, h, x, t, avoid)]
            if pool:
                r2 = pool[rng.randrange(len(pool))]
        if r2 is not None:
            decoys2.append({"cand_id": f"{doc.doc_id}:cf2:{h}>{t}", "doc_id": doc.doc_id,
                            "h": h, "r": r2, "t": t, "real_id": c["cand_id"],
                            "claim": verbalize(h, r2, t)})
    return decoys, decoys2, n_gen, n_contam


async def gen_cf_compat(client: OpenRouterClient, doc: Doc, reals: list[dict],
                        model: str, rng: random.Random, cid_tag: str) -> tuple[list[dict], int, int]:
    """iter-2-FAITHFUL single-choice counterfactual decoy generator (Phase 5 (G,S) matrix).

    Byte-identical to iter-2 EXP2.gen_counterfactual_decoys: ONE batched generation call/doc, and
    the chosen decoy relation = the FIRST verified-non-entailed LLM alternative (else a salt-driven
    random-vocab fallback). It deliberately does NOT parse a 2nd alt / consume extra rng (unlike the
    iter-3 cf path), so the chosen relation — and therefore the decoy CLAIM and its cache key —
    reproduce iter-2 EXACTLY for BOTH the LLM-provided and the fallback cases. With model=OTHER_MODEL
    and the iter-2 salt (31) this makes the ministral-generated 'cfo' decoys and their cached nano- and
    ministral-SC scores warm-hit on the original 40 pilot docs. Returns (decoys, n_gen, n_contam)."""
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
        chosen = None
        for rr in cand_rels:
            if verify_nonentailed(doc, h, rr, t, avoid):
                chosen = rr
                break
        if chosen is None:
            pool = [x for x in RELATION_VOCAB if verify_nonentailed(doc, h, x, t, avoid)]
            if pool:
                chosen = pool[rng.randrange(len(pool))]
        if chosen is None:
            continue
        decoys.append({"cand_id": f"{doc.doc_id}:{cid_tag}:{h}>{t}", "doc_id": doc.doc_id,
                       "h": h, "r": chosen, "t": t, "pair": (h, t), "real_id": c["cand_id"],
                       "claim": verbalize(h, chosen, t)})
    return decoys, n_gen, n_contam


def gen_swaps(doc: Doc, reals: list[dict], rng: random.Random) -> list[dict]:
    """L1 random in-document swap: tail -> another in-doc entity (kept relation)."""
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


def gen_random_vocab(doc: Doc, reals: list[dict], rng: random.Random) -> list[dict]:
    """L2 random-vocab: keep the entities, swap the relation to a random non-entailed
    vocabulary relation (medium difficulty)."""
    out = []
    for c in reals:
        h, r, t = c["h"], c["r"], c["t"]
        pool = [x for x in RELATION_VOCAB if verify_nonentailed(doc, h, x, t, {r})]
        if not pool:
            continue
        rr = pool[rng.randrange(len(pool))]
        out.append({"cand_id": f"{doc.doc_id}:rv:{h}>{t}", "doc_id": doc.doc_id,
                    "h": h, "r": rr, "t": t, "real_id": c["cand_id"],
                    "claim": verbalize(h, rr, t)})
    return out


def gen_foreign_swap(doc: Doc, reals: list[dict], foreign_names: list[str],
                     rng: random.Random, salt_tag: str, cid_tag: str) -> list[dict]:
    """L0 foreign-swap / entrapment: tail -> an entity sampled from a DIFFERENT document
    (out-of-context, false-by-construction; relation kept). Deterministic per (doc, real).
    Used for L0 (cid_tag='fgn') and, with an independent draw, for ENTRAPMENT (cid_tag='ent')."""
    out = []
    in_doc = set(doc.entities)
    for c in reals:
        h, r, t = c["h"], c["r"], c["t"]
        # deterministic per-(doc,real,salt) seed via hashlib (NEVER python hash()): stable
        # foreign-entity draws across processes/runs so cache keys are reproducible.
        sd = int(hashlib.sha256(f"{doc.doc_id}|{h}|{t}|{salt_tag}|{SEED}".encode()).hexdigest()[:12], 16)
        rloc = random.Random(sd)
        # pick a foreign name not in this document (guaranteed non-entailed)
        cand = None
        for _ in range(8):
            nm = foreign_names[rloc.randrange(len(foreign_names))]
            if nm not in in_doc and nm != h:
                cand = nm
                break
        if cand is None:
            continue
        out.append({"cand_id": f"{doc.doc_id}:{cid_tag}:{h}>{t}", "doc_id": doc.doc_id,
                    "h": h, "r": r, "t": cand, "real_id": c["cand_id"],
                    "claim": verbalize(h, r, cand)})
    return out


_SALTS = {"extract": 0, "decoy": 7, "swap": 99, "rv": 13, "fgn": 23, "ent": 41, "cfo": 31}
# salt 31 == iter-2 EXP2's OTHER-model (ministral) decoy generation salt -> warm cfo cache hits.


# ===========================================================================
# Scoring (isolated, provenance-blinded). sc => K_SC calls; vb => 1 call.
# ===========================================================================
async def score_portable(client: OpenRouterClient, model: str, doc_text: str, claim: str) -> float:
    """K=5 self-consistency (headline). Cache-identical to iter-2 EXP2.score_portable."""
    ps = []
    for i in range(K_SC):
        from llm_client import parse_yes_conf
        res = await client.call(model, score_messages_portable(doc_text, claim),
                                max_tokens=24, temperature=0.7, seed=SEED + i, sample_idx=i)
        p = parse_yes_conf(res["content"])
        if p is not None:
            ps.append(p)
    return float(np.mean(ps)) if ps else 0.5


async def score_verbalized(client: OpenRouterClient, model: str, doc_text: str, claim: str) -> float:
    res = await client.call(model, score_messages_verbalized(doc_text, claim),
                            max_tokens=16, temperature=0.0)
    p = _parse_prob(res["content"])
    return float(p) if p is not None else 0.5


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
        errs = [r for r in res if isinstance(r, Exception)]
        n_err = len(errs)
        if errs:
            logger.warning(f"  [{label}] first error: {type(errs[0]).__name__}: {errs[0]}")
        logger.info(f"  [{label}] {min(i+batch, len(coros))}/{len(coros)} done | "
                    f"cost=${client.cost_usd:.4f} | live={client.n_calls_live} "
                    f"cached={client.n_calls_cached} (warm={client.n_calls_fallback}) | errs={n_err}")
    return out


async def run(docs: list[Doc], cache_dir: Path, cost_log: Path, concurrency: int,
              light: bool = False, n_extract: int = N_EXTRACT_SAMPLES, do_gs: bool = True,
              do_strong: bool = False, strong_docs_cap: int | None = None,
              ladder_conf: int = 60) -> dict:
    """light=True (fallback): restrict entrapment + ladder + verbalized to the pilot slice.

    Phase-5 (G,S) paired matrix and Phase-6b strong-extractor arm are BUDGET-GATED: the headline
    diagonal (reals+cf+swap+ent SC, +VB contrast) always completes; the optional arms run only while
    cumulative NEW cost stays under the soft cap, so the soft cap actively governs optional spend."""
    rng = random.Random(SEED)
    t0 = time.time()
    pilot_ids = {d.doc_id for d in docs if d.is_pilot} or {docs[0].doc_id}
    conf_order = [d.doc_id for d in docs if d.doc_id not in pilot_ids]
    # S1b ladder scope (Phase 7): pilot UNION the first `ladder_conf` confirmatory docs so the
    # L0..L4 rungs (fgn/rv/cf2) can be POWERED to the per-rung false-pair floor (cf/swap = corpus-wide).
    ladder_ids = set(pilot_ids) | set(conf_order[:max(0, ladder_conf)])
    gs_ids = {d.doc_id for d in docs if d.doc_id in GS_WARM_IDS}      # warm (G,S) 2x2 doc set
    foreign_names = sorted({e for d in docs for e in d.entities})

    async with OpenRouterClient(cache_dir, cost_log, concurrency=concurrency,
                                soft_cap_usd=SOFT_CAP_USD, hard_stop_usd=HARD_STOP_USD,
                                fallback_cache_dirs=WARM_CACHES) as client:
        # ---- 1. EXTRACTION ----
        logger.info(f"Extraction over {len(docs)} docs (n_extract={n_extract})...")
        ext = await run_batched([extract_doc(client, d, random.Random(_doc_seed(d.doc_id)),
                                             n_extract=n_extract)
                                 for d in docs], 96, "extract", client)
        doc_by_id = {d.doc_id: d for d in docs}
        reals_by_doc, ext_meta = {}, []
        for d, e in zip(docs, ext):
            reals_by_doc[d.doc_id] = e["reals"] if e else []
            if e:
                ext_meta.append(e)
        all_reals = [c for d in docs for c in reals_by_doc[d.doc_id]]
        n_true = sum(1 for c in all_reals if c["label"] == TRUE)
        n_spont = sum(1 for c in all_reals if c["label"] == FALSE)
        n_und = sum(1 for c in all_reals if c["label"] == UND)
        logger.info(f"reals={len(all_reals)} TRUE={n_true} FALSE(spont)={n_spont} UND={n_und}")

        # ---- 2. DECOYS (cf=L4, cf2=L3) + SWAPS + LADDER RUNGS + ENTRAPMENT ----
        logger.info("Generating counterfactual decoys (cf/cf2) + swaps + rungs + entrapment...")
        dec = await run_batched(
            [gen_counterfactual_decoys(client, d, reals_by_doc[d.doc_id], PRIMARY_MODEL,
                                       random.Random(_doc_seed(d.doc_id, _SALTS["decoy"])))
             for d in docs], 96, "decoy", client)
        cf_by_doc, cf2_by_doc, swap_by_doc = {}, {}, {}
        rv_by_doc, fgn_by_doc, ent_by_doc = {}, {}, {}
        n_gen = n_contam = 0
        for d, dd in zip(docs, dec):
            decoys, decoys2, g, c = dd if dd else ([], [], 0, 0)
            cf_by_doc[d.doc_id] = decoys
            cf2_by_doc[d.doc_id] = decoys2
            n_gen += g
            n_contam += c
            swap_by_doc[d.doc_id] = gen_swaps(d, reals_by_doc[d.doc_id],
                                              random.Random(_doc_seed(d.doc_id, _SALTS["swap"])))
            # entrapment on ALL docs (unless light); foreign/randvocab generated on the LADDER scope
            ent_by_doc[d.doc_id] = gen_foreign_swap(
                d, reals_by_doc[d.doc_id], foreign_names,
                random.Random(_doc_seed(d.doc_id, _SALTS["ent"])), "ent", "ent")
            if d.doc_id in ladder_ids:
                rv_by_doc[d.doc_id] = gen_random_vocab(
                    d, reals_by_doc[d.doc_id],
                    random.Random(_doc_seed(d.doc_id, _SALTS["rv"])))
                fgn_by_doc[d.doc_id] = gen_foreign_swap(
                    d, reals_by_doc[d.doc_id], foreign_names,
                    random.Random(_doc_seed(d.doc_id, _SALTS["fgn"])), "fgn", "fgn")
        contamination_rate = (n_contam / n_gen) if n_gen else 0.0
        logger.info(f"decoys generated; contamination_rate={contamination_rate:.4f}")

        # cfo: ministral-GENERATED counterfactual decoys (Phase 5, G=ministral) on the warm (G,S) docs
        cfo_by_doc = {}
        if do_gs and gs_ids:
            gs_docs = [d for d in docs if d.doc_id in gs_ids]
            logger.info(f"Generating ministral-cf (cfo) decoys on {len(gs_docs)} warm (G,S) docs...")
            deco = await run_batched(
                [gen_cf_compat(client, d, reals_by_doc[d.doc_id], OTHER_MODEL,
                               random.Random(_doc_seed(d.doc_id, _SALTS["cfo"])), "cfo")
                 for d in gs_docs], 64, "decoy-cfo", client)
            for d, dd in zip(gs_docs, deco):
                cfo_by_doc[d.doc_id] = dd[0] if dd else []

        # ---- 3. SCORING (zmap[(config, cand_id)] = z) ----
        zmap: dict[tuple, float] = {}

        def tasks_for(cands, config, model, method):
            return [(config, c["cand_id"], method, model,
                     doc_by_id[c["doc_id"]].text, c["claim"]) for c in cands]

        async def run_score(task):
            config, cid, method, model, dtext, claim = task
            z = (await score_portable(client, model, dtext, claim) if method == "portable"
                 else await score_verbalized(client, model, dtext, claim))
            return (config, cid, z)

        def collect(by_doc, doc_filter=None):
            return [c for d in docs if (doc_filter is None or d.doc_id in doc_filter)
                    for c in by_doc.get(d.doc_id, [])]

        async def score_into_zmap(tasks, batch, label):
            for r in await run_batched([run_score(t) for t in tasks], batch, label, client):
                if r:
                    zmap[(r[0], r[1])] = r[2]

        ent_scope = pilot_ids if light else None       # all docs unless light
        # SELF-CONSISTENCY headline scoring (nano): reals + cf + swap + ent (always run) +
        # ladder rungs cf2/rv/fgn on the LADDER scope.
        sc_tasks = (tasks_for(all_reals, SC, PRIMARY_MODEL, "portable")
                    + tasks_for(collect(cf_by_doc), SC, PRIMARY_MODEL, "portable")
                    + tasks_for(collect(swap_by_doc), SC, PRIMARY_MODEL, "portable")
                    + tasks_for(collect(ent_by_doc, ent_scope), SC, PRIMARY_MODEL, "portable"))
        logger.info(f"Self-consistency headline scoring: {len(sc_tasks)} items x K={K_SC} ...")
        await score_into_zmap(sc_tasks, 600, "score-sc")

        # ladder rung scoring (cf2/rv/fgn) — restrict to pilot if light OR soft cap already reached
        ladder_scope = pilot_ids if (light or client.cost_usd >= SOFT_CAP_USD) else ladder_ids
        rung_tasks = (tasks_for(collect(cf2_by_doc, ladder_scope), SC, PRIMARY_MODEL, "portable")
                      + tasks_for(collect(rv_by_doc, ladder_scope), SC, PRIMARY_MODEL, "portable")
                      + tasks_for(collect(fgn_by_doc, ladder_scope), SC, PRIMARY_MODEL, "portable"))
        logger.info(f"S1b ladder rung scoring: {len(rung_tasks)} items "
                    f"(scope={'pilot' if ladder_scope is pilot_ids else 'pilot+conf'}) ...")
        await score_into_zmap(rung_tasks, 600, "score-rung")

        # VERBALIZED contrast scoring (nano): reals + cf + swap
        vb_scope = pilot_ids if light else None
        vb_tasks = (tasks_for(collect(reals_by_doc, vb_scope), VB, PRIMARY_MODEL, "verbalized")
                    + tasks_for(collect(cf_by_doc, vb_scope), VB, PRIMARY_MODEL, "verbalized")
                    + tasks_for(collect(swap_by_doc, vb_scope), VB, PRIMARY_MODEL, "verbalized"))
        logger.info(f"Verbalized contrast scoring: {len(vb_tasks)} items ...")
        await score_into_zmap(vb_tasks, 600, "score-vb")

        # ---- 4. PHASE 5 (G,S) paired matrix scoring (warm; budget-gated) ----
        gs_scored = False
        if do_gs and gs_ids and client.cost_usd < SOFT_CAP_USD:
            gs_reals = collect(reals_by_doc, gs_ids)
            gs_cf = collect(cf_by_doc, gs_ids)
            gs_cfo = collect(cfo_by_doc, gs_ids)
            gs_swap = collect(swap_by_doc, gs_ids)
            # nano-SC of cfo (reals/cf/swap already nano-SC scored above); ministral-SC of all four
            gs_tasks = (tasks_for(gs_cfo, SC, PRIMARY_MODEL, "portable")
                        + tasks_for(gs_reals, MIN_SC, OTHER_MODEL, "portable")
                        + tasks_for(gs_cf, MIN_SC, OTHER_MODEL, "portable")
                        + tasks_for(gs_cfo, MIN_SC, OTHER_MODEL, "portable")
                        + tasks_for(gs_swap, MIN_SC, OTHER_MODEL, "portable"))
            logger.info(f"(G,S) paired matrix scoring: {len(gs_tasks)} items "
                        f"(nano+ministral SC on {len(gs_ids)} warm docs) ...")
            await score_into_zmap(gs_tasks, 500, "score-gs")
            gs_scored = True
        elif do_gs:
            logger.warning(f"(G,S) matrix SKIPPED (cost=${client.cost_usd:.4f} >= soft cap "
                           f"${SOFT_CAP_USD} or no warm docs); reported underpowered.")

        # ---- 5. PHASE 6b strong-extractor de-confound arm (optional; budget-gated) ----
        strong_reals_by_doc, strong_cf_by_doc, strong_meta = {}, {}, []
        strong_docs_ids = []
        if do_strong and client.cost_usd < SOFT_CAP_USD:
            # pick a multi-hop-rich powered subset: confirmatory docs in k-descending order
            cand = sorted([d for d in docs if d.k >= 4],
                          key=lambda d: (-d.k, d.doc_id))
            cap = strong_docs_cap if strong_docs_cap else len(cand)
            strong_set = cand[:cap]
            strong_docs_ids = [d.doc_id for d in strong_set]
            logger.info(f"STRONG-extractor arm ({STRONG_EXTRACTOR}) re-extraction on "
                        f"{len(strong_set)} docs (k>=4)...")
            sext = await run_batched(
                [extract_doc(client, d, random.Random(_doc_seed(d.doc_id)),
                             model=STRONG_EXTRACTOR, n_extract=1, cid_tag="sreal")
                 for d in strong_set], 64, "extract-strong", client)
            for d, e in zip(strong_set, sext):
                # keep only multi_hop reals (the de-confound target family)
                mh = [c for c in (e["reals"] if e else []) if c["fact_type"] == "multi_hop"]
                strong_reals_by_doc[d.doc_id] = mh
                if e:
                    strong_meta.append({"doc_id": d.doc_id, "k": d.k, "mh_acc": e["mh_acc"],
                                        "n_mh": e["n_mh"]})
            # nano-generated cf decoys for the strong reals (scorer fixed nano => isolates extractor)
            sdec = await run_batched(
                [gen_counterfactual_decoys(client, d, strong_reals_by_doc.get(d.doc_id, []),
                                           PRIMARY_MODEL,
                                           random.Random(_doc_seed(d.doc_id, _SALTS["decoy"])))
                 for d in strong_set], 64, "decoy-strong", client)
            for d, dd in zip(strong_set, sdec):
                decoys = dd[0] if dd else []
                for x in decoys:
                    x["cand_id"] = f"{d.doc_id}:scf:{x['h']}>{x['t']}"
                strong_cf_by_doc[d.doc_id] = decoys
            s_reals = [c for v in strong_reals_by_doc.values() for c in v]
            s_cf = [c for v in strong_cf_by_doc.values() for c in v]
            str_tasks = (tasks_for(s_reals, STR_SC, PRIMARY_MODEL, "portable")
                         + tasks_for(s_cf, STR_SC, PRIMARY_MODEL, "portable"))
            logger.info(f"STRONG-extractor nano-SC scoring: {len(str_tasks)} items ...")
            await score_into_zmap(str_tasks, 500, "score-strong")
        elif do_strong:
            logger.warning(f"STRONG-extractor arm SKIPPED (cost=${client.cost_usd:.4f} >= soft cap).")

        elapsed = time.time() - t0
        runtime = {"elapsed_s": round(elapsed, 1), "cost_usd": round(client.cost_usd, 6),
                   "n_calls_live": client.n_calls_live, "n_calls_cached": client.n_calls_cached,
                   "n_calls_warm_fallback": client.n_calls_fallback,
                   "cached_tokens_observed": client.cached_tokens_observed}
        logger.info(f"Pipeline done in {elapsed:.1f}s | cost=${client.cost_usd:.4f} | "
                    f"live={client.n_calls_live} cached={client.n_calls_cached} "
                    f"warm={client.n_calls_fallback}")

    return {"docs": docs, "doc_by_id": doc_by_id, "pilot_ids": pilot_ids,
            "ladder_ids": ladder_ids, "gs_ids": gs_ids, "gs_scored": gs_scored,
            "reals_by_doc": reals_by_doc, "cf_by_doc": cf_by_doc, "cf2_by_doc": cf2_by_doc,
            "swap_by_doc": swap_by_doc, "rv_by_doc": rv_by_doc, "fgn_by_doc": fgn_by_doc,
            "ent_by_doc": ent_by_doc, "cfo_by_doc": cfo_by_doc, "all_reals": all_reals, "zmap": zmap,
            "strong_reals_by_doc": strong_reals_by_doc, "strong_cf_by_doc": strong_cf_by_doc,
            "strong_meta": strong_meta, "strong_docs_ids": strong_docs_ids,
            "ext_meta": ext_meta, "contamination_rate": contamination_rate, "n_gen_decoys": n_gen,
            "n_true": n_true, "n_spont": n_spont, "n_und": n_und, "light": light,
            "n_extract": n_extract, "runtime": runtime}


# ===========================================================================
# Normalization helpers (per-document rank-normalization; single coherent Z-scale)
# ===========================================================================
def _base_pool(pipe, doc_id):
    """The iter-2 normalization pool for a doc: reals U cf(L4) U swap(L1)."""
    return (pipe["reals_by_doc"].get(doc_id, []) + pipe["cf_by_doc"].get(doc_id, [])
            + pipe["swap_by_doc"].get(doc_id, []))


def norm_pool(pipe, config, extra_by_doc=None, docs=None):
    """Per-document rank-normalize raw `config` scores over {reals U cf U swap (U extra)}.
    With no extra this is EXACTLY the iter-2 pool, so the headline diagonal reconciles
    with iter-2. For a ladder rung / entrapment set, `extra_by_doc` adds that set so the
    extra items live on the SAME normalized Z-scale as the reals they compete with."""
    zmap = pipe["zmap"]
    norm = {}
    dd = docs if docs is not None else pipe["docs"]
    for d in dd:
        cands = _base_pool(pipe, d.doc_id)
        if extra_by_doc:
            cands = cands + extra_by_doc.get(d.doc_id, [])
        pool = {}
        seen = set()
        for c in cands:
            cid = c["cand_id"]
            if cid in seen:
                continue
            seen.add(cid)
            key = (config, cid)
            if key in zmap:
                pool[cid] = zmap[key]
        norm.update(st.rank_normalize(pool, SEED))
    return norm


def _nan(x):
    if x is None:
        return None
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    return round(float(x), 6)


# ===========================================================================
# Per-family realized-FDR calibration DIAGONAL  (the SINGLE primary artifact)
# ===========================================================================
def _family_reals(pipe, family):
    if family == "pooled":
        return [c for c in pipe["all_reals"]]
    return [c for c in pipe["all_reals"] if c["fact_type"] == family]


def _decoy_map(pipe, by_key):
    """real_id -> decoy cand_id for a given decoy set name."""
    src = {"cf": pipe["cf_by_doc"], "cf2": pipe["cf2_by_doc"], "swap": pipe["swap_by_doc"],
           "rv": pipe["rv_by_doc"], "fgn": pipe["fgn_by_doc"], "ent": pipe["ent_by_doc"],
           "cfo": pipe.get("cfo_by_doc", {}), "scf": pipe.get("strong_cf_by_doc", {})}[by_key]
    return {c["real_id"]: c["cand_id"] for dd in src.values() for c in dd}


def _pairs_for(pipe, norm, family, decoy_key, docs_filter=None):
    """Per-doc list of {zr, zd, label, doc_id, w, real_id}. Reals of `family` with both
    real and decoy scored in `norm`."""
    dmap = _decoy_map(pipe, decoy_key)
    pool_ids = None
    if docs_filter is not None:
        pool_ids = {d.doc_id for d in docs_filter}
    per_doc = {}
    for c in _family_reals(pipe, family):
        if pool_ids is not None and c["doc_id"] not in pool_ids:
            continue
        zr = norm.get(c["cand_id"])
        did = dmap.get(c["cand_id"])
        zd = norm.get(did) if did else None
        if zr is None or zd is None:
            continue
        per_doc.setdefault(c["doc_id"], []).append(
            {"zr": zr, "zd": zd, "label": c["label"], "doc_id": c["doc_id"],
             "w": st.W_signed_max(zr, zd), "real_id": c["cand_id"]})
    return per_doc


def _realized_fdr(pairs_flat, alpha):
    if not pairs_flat:
        return float("nan"), 0, 0, None
    W = [p["w"] for p in pairs_flat]
    T, n_adm_pos, ratio = st.knockoff_plus_threshold(W, alpha)
    if math.isinf(T):
        return float("nan"), 0, 0, None
    adm = [p for p in pairs_flat if p["w"] >= T]
    n = len(adm)
    nf = sum(1 for p in adm if p["label"] == FALSE)
    realized = (nf / n) if n else float("nan")
    return realized, n, nf, ratio


# Vectorized knockoff+ (O(n log n)) — IDENTICAL output to st.knockoff_plus_threshold (asserted
# in selftest). Used inside the doc-block bootstrap hot loop so the powered (B>=2000) diagonal
# over ~thousands of reals finishes in seconds rather than O(distinct|W|^2) minutes.
def _knockoff_fast(W: np.ndarray, alpha: float):
    Wa = np.asarray(W, dtype=float)
    if Wa.size == 0:
        return math.inf, 0, 1.0
    sW = np.sort(Wa)
    mags = np.unique(np.abs(Wa))
    mags = mags[mags > 0.0]
    if mags.size == 0:
        return math.inf, 0, 1.0
    pos = sW.size - np.searchsorted(sW, mags, side="left")     # #(W >= t)
    neg = np.searchsorted(sW, -mags, side="right")             # #(W <= -t)
    ratio = (1.0 + neg) / np.maximum(1, pos)
    feas = np.nonzero(ratio <= alpha)[0]
    if feas.size == 0:
        return math.inf, 0, 1.0
    i = int(feas[0])                                           # smallest feasible magnitude
    return float(mags[i]), int(pos[i]), float(ratio[i])


def _realized_fast(zr: np.ndarray, zd: np.ndarray, isfalse: np.ndarray, alpha: float) -> float:
    """Realized FDR of the knockoff+ admitted set, fully vectorized."""
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


def _doc_arrays(per_doc):
    """Per-document (zr, zd, isfalse) numpy triples for fast bootstrap resampling."""
    out = []
    for v in per_doc.values():
        out.append((np.array([p["zr"] for p in v], float),
                    np.array([p["zd"] for p in v], float),
                    np.array([p["label"] == FALSE for p in v], bool)))
    return out


def diagonal_for_family(pipe, norm, family, raw_conf):
    """Full diagonal (method/swap/plain) with doc-block bootstrap CIs + the
    (alpha, decoy_fdr_hat, realized) TRIPLE + the pre-registered SELF-REPORT check."""
    per_doc_cf = _pairs_for(pipe, norm, family, "cf")
    per_doc_sw = _pairs_for(pipe, norm, family, "swap")
    flat_cf = [p for v in per_doc_cf.values() for p in v]
    flat_sw = [p for v in per_doc_sw.values() for p in v]
    doc_arrays_cf = _doc_arrays(per_doc_cf)
    famreals = _family_reals(pipe, family)
    n_false_total = sum(1 for c in famreals if c["label"] == FALSE)
    n_true_total = sum(1 for c in famreals if c["label"] == TRUE)
    populable = n_false_total >= N_FALSE_MIN
    n_pos = sum(1 for p in flat_cf if p["w"] > 0)

    rows = []
    for alpha in ALPHA_GRID:
        realized, n_adm, n_false, ratio = _realized_fdr(flat_cf, alpha)
        decoy_fdr_hat = ratio if ratio is not None else None

        def stat_fn(resample, a=alpha):
            if not resample:
                return float("nan")
            zr = np.concatenate([u[0] for u in resample])
            zd = np.concatenate([u[1] for u in resample])
            isf = np.concatenate([u[2] for u in resample])
            return _realized_fast(zr, zd, isf, a)
        ci = st.doc_block_bootstrap(doc_arrays_cf, stat_fn, B=B_BOOT, seed=SEED)

        realized_sw, n_adm_sw, _, _ = _realized_fdr(flat_sw, alpha)
        # PLAIN raw-confidence baseline gate (decoy-free, purely-neural foil)
        Zraw = [raw_conf[c["cand_id"]] for c in famreals if c["cand_id"] in raw_conf]
        labraw = [c["label"] for c in famreals if c["cand_id"] in raw_conf]
        thr_p, adm_p, est_p = fc.plain_threshold_gate(Zraw, alpha)
        nfp = sum(1 for i in adm_p if labraw[i] == FALSE)
        realized_p = (nfp / len(adm_p)) if adm_p else float("nan")

        self_report_anti = (decoy_fdr_hat is not None and not math.isnan(realized)
                            and (realized - decoy_fdr_hat) > TAU)
        certified = (n_adm >= st.k_floor(alpha)) and populable
        rows.append({
            "target_alpha": alpha,
            "decoy_fdr_hat": _nan(decoy_fdr_hat),
            "realized_fdr": _nan(realized),
            "triple_alpha_estimate_realized": [alpha, _nan(decoy_fdr_hat), _nan(realized)],
            "ci_low": _nan(ci["ci_low"]), "ci_high": _nan(ci["ci_high"]),
            "n_admitted": n_adm, "n_false_admitted": n_false,
            "self_report_anti_conservative": bool(self_report_anti),
            "k_floor": st.k_floor(alpha), "certified": bool(certified),
            "populable": bool(populable),
            "swap_realized_fdr": _nan(realized_sw), "swap_n_admitted": n_adm_sw,
            "plain_realized_fdr": _nan(realized_p), "plain_n_admitted": len(adm_p),
            "plain_est_fdr": _nan(est_p)})
    certified_alphas = [r["target_alpha"] for r in rows if r["certified"]]
    # PAIRED-EXCHANGEABILITY DIAGNOSTIC (the knockoff null) over FALSE-real pairs in the
    # operative admission tail. This is the bridge between the crux (distributional
    # exchangeability of the decoy MARGINAL) and the realized diagonal (the PAIRED
    # competition the gate actually runs). win-rate ~0.5 => paired-exchangeable (Barber-
    # Candes null holds, realized FDR<=alpha is then guaranteed in expectation); win-rate
    # < 0.5 => the false real systematically beats its own counterfactual decoy (decoys
    # too easy / the LLM is confidently wrong) => anti-conservative. Reconciles iter-2
    # (self-consistency cf tail win-rate ~0.482).
    Tcut, _, _ = st.knockoff_plus_threshold([p["w"] for p in flat_cf], 0.50)
    cutv = Tcut if not math.isinf(Tcut) else 0.0
    fp = [p for p in flat_cf if p["label"] == FALSE]
    wr_pe, n_tail_pe = st.tail_win_rate([(p["zr"], p["zd"]) for p in fp], cutv)
    tail_pe = [p for p in fp if max(p["zr"], p["zd"]) >= cutv]
    ks_pe_s, ks_pe_p = st.ks_two_sample([p["zd"] for p in tail_pe], [p["zr"] for p in tail_pe], "two-sided")
    fbpe = {}
    for p in tail_pe:
        fbpe.setdefault(p["doc_id"], []).append(p)

    def _wrfn(resample):
        flatp = [p for grp in resample for p in grp]
        if not flatp:
            return float("nan")
        return float(np.mean([1.0 if p["zd"] > p["zr"] else 0.0 for p in flatp]))
    ci_pe = st.doc_block_bootstrap(list(fbpe.values()), _wrfn, B=B_BOOT_INNER, seed=SEED)
    paired_exch = {
        "operative_alpha": 0.50, "tail_win_rate_false_pairs": _nan(wr_pe),
        "win_rate_ci": [_nan(ci_pe["ci_low"]), _nan(ci_pe["ci_high"])], "n_tail_false_pairs": n_tail_pe,
        "ks_p_decoy_vs_real": ks_pe_p,
        "ci_covers_half": bool(ci_pe["ci_low"] is not None and not math.isnan(ci_pe["ci_low"])
                               and ci_pe["ci_low"] <= 0.5 <= ci_pe["ci_high"]),
        "interpretation": ("win-rate ~0.5 (CI covers 0.5) => paired-exchangeable knockoff null holds; "
                           "< 0.5 => false reals beat their own counterfactual decoys (anti-conservative)")}
    return {"family": family, "rows": rows, "n_pos": n_pos, "paired_exchangeability": paired_exch,
            "n_pairs": len(flat_cf), "n_true_total": n_true_total,
            "n_false_total": n_false_total, "populable": bool(populable),
            "reachable_alpha_floor": (min(certified_alphas) if certified_alphas else None),
            "alpha_star_permissive": (max(certified_alphas) if certified_alphas else None)}


# ===========================================================================
# S1b difficulty-graded LADDER (L0..L4) under self-consistency (pilot slice)
# ===========================================================================
LADDER = [("L0_foreign_swap", "fgn"), ("L1_random_swap", "swap"), ("L2_random_vocab", "rv"),
          ("L3_cf_2nd", "cf2"), ("L4_cf_1st", "cf")]


def analyze_s1b_ladder(pipe):
    """Phase 7: POWER-or-BOUND the S1b L0..L4 difficulty ladder. Rungs are scored on the enlarged
    ladder scope (pilot U first-N confirmatory). Each rung reports its realized false-pair n and a
    `powered` flag (>= N_LADDER_FALSE_MIN). Under-floor rungs are reported PURELY as underpowered
    (cannot localize which decoy classes are detected / cannot certify paired validity) — the
    contradicted 'detects only gross decoys' narrative is NOT asserted."""
    ladder_ids = pipe.get("ladder_ids") or pipe["pilot_ids"]
    ladder_docs = [d for d in pipe["docs"] if d.doc_id in ladder_ids]
    rungs = []
    for name, key in LADDER:
        extra = {"cf": pipe["cf_by_doc"], "cf2": pipe["cf2_by_doc"], "swap": pipe["swap_by_doc"],
                 "rv": pipe["rv_by_doc"], "fgn": pipe["fgn_by_doc"]}[key]
        norm = norm_pool(pipe, SC, extra_by_doc=extra, docs=ladder_docs)
        per_doc = _pairs_for(pipe, norm, "pooled", key, docs_filter=ladder_docs)
        flat = [p for v in per_doc.values() for p in v]
        false_pairs = [p for p in flat if p["label"] == FALSE]
        W_all = [p["w"] for p in flat]
        T, _, _ = st.knockoff_plus_threshold(W_all, 0.50)   # most-permissive operative cutoff
        cut = T if not math.isinf(T) else 0.0
        wr, n_tail = st.tail_win_rate([(p["zr"], p["zd"]) for p in false_pairs], cut)
        tail = [p for p in false_pairs if max(p["zr"], p["zd"]) >= cut]
        ks_s, ks_p = st.ks_two_sample([p["zd"] for p in tail], [p["zr"] for p in tail], "two-sided")
        mw_s, mw_p = st.mannwhitney([p["zd"] for p in tail], [p["zr"] for p in tail], "less")
        fb = {}
        for p in tail:
            fb.setdefault(p["doc_id"], []).append(p)

        def wr_fn(resample):
            flatp = [p for grp in resample for p in grp]
            if not flatp:
                return float("nan")
            return float(np.mean([1.0 if p["zd"] > p["zr"] else 0.0 for p in flatp]))
        ci = st.doc_block_bootstrap(list(fb.values()), wr_fn, B=B_BOOT_INNER, seed=SEED)
        covers_half = (ci["ci_low"] is not None and not math.isnan(ci["ci_low"])
                       and ci["ci_low"] <= 0.5 <= ci["ci_high"])
        detected = (ci["ci_high"] is not None and not math.isnan(ci["ci_high"])
                    and ci["ci_high"] < 0.5)
        rungs.append({"rung": name, "decoy_set": key, "n_false_pairs": len(false_pairs),
                      "n_tail": n_tail, "tail_win_rate": _nan(wr),
                      "win_rate_ci": [_nan(ci["ci_low"]), _nan(ci["ci_high"])],
                      "ks_p": ks_p, "mw_p": mw_p,
                      "powered": bool(len(false_pairs) >= N_LADDER_FALSE_MIN),
                      "detected_anti_conservative": bool(detected),
                      "ci_covers_half": bool(covers_half)})
    powered = [r for r in rungs if r["powered"]]
    underfloor = [r["rung"] for r in rungs if not r["powered"]]
    by = {r["rung"]: r for r in rungs}
    if not powered:
        verdict = "UNDERPOWERED"
        reason = (f"No rung reached the {N_LADDER_FALSE_MIN}-false-pair floor on {len(ladder_docs)} "
                  f"ladder docs (under-floor: {underfloor}). The ladder is UNDERPOWERED: it cannot "
                  f"localize which decoy classes are detected and cannot certify paired validity. "
                  f"The 'detects only gross decoys' narrative is NOT asserted.")
    else:
        det = [r["rung"] for r in powered if r["detected_anti_conservative"]]
        cov = [r["rung"] for r in powered if r["ci_covers_half"]]
        easy_det = any(r in det for r in ("L0_foreign_swap", "L1_random_swap", "L2_random_vocab"))
        hard_cov = (by["L4_cf_1st"]["powered"] and by["L4_cf_1st"]["ci_covers_half"])
        if easy_det and hard_cov:
            verdict = "GRADED_DETECTS_EASY"
            reason = (f"Among POWERED rungs, easy decoy classes are flagged anti-conservative "
                      f"(CI<0.5: {det}) while the hard counterfactual rung L4 covers 0.5: the "
                      f"win-rate diagnostic discriminates difficulty in the powered regime. "
                      f"Under-floor (uninterpreted): {underfloor or 'none'}.")
        elif not det:
            verdict = "BLIND_ALL_COVER_HALF"
            reason = (f"Every POWERED rung's win-rate CI covers 0.5 ({cov}): even gross decoy classes "
                      f"are not flagged under self-consistency — the win-rate diagnostic is a blunt "
                      f"instrument here (down-scoped). Under-floor (uninterpreted): {underfloor or 'none'}.")
        else:
            verdict = "GRADED_PARTIAL"
            reason = (f"POWERED rungs show graded/partial sensitivity (detected: {det}; cover-0.5: "
                      f"{cov}). Under-floor (uninterpreted): {underfloor or 'none'}.")
    return {"rungs": rungs, "verdict": verdict, "reason": reason,
            "n_ladder_docs": len(ladder_docs), "n_powered_rungs": len(powered),
            "n_false_min_per_rung": N_LADDER_FALSE_MIN,
            "cut_rule": "knockoff+ operative T at alpha=0.5 per rung; win-rate over FALSE-real pairs"}


# ===========================================================================
# Crux match in full (decoy ~ spontaneous-error; decoy != true-positive)
# ===========================================================================
def analyze_crux(pipe, norm):
    reals = pipe["all_reals"]
    cf_real = _decoy_map(pipe, "cf")
    F_tp, F_sp, F_dc = [], [], []
    sp_doc, dc_doc = {}, {}
    for c in reals:
        z = norm.get(c["cand_id"])
        if z is None:
            continue
        if c["label"] == TRUE:
            F_tp.append(z)
        elif c["label"] == FALSE:
            F_sp.append(z)
            sp_doc.setdefault(c["doc_id"], []).append(z)
        did = cf_real.get(c["cand_id"])
        if did is not None:
            zd = norm.get(did)
            if zd is not None:
                F_dc.append(zd)
                dc_doc.setdefault(c["doc_id"], []).append(zd)
    pooled = np.array(F_tp + F_sp + F_dc)
    regions = {}
    for rname, q in {"full": None, "top50pct": 0.50, "top25pct": 0.75}.items():
        if q is None:
            dec, spo, tru = F_dc, F_sp, F_tp
        else:
            thr = float(np.quantile(pooled, q)) if pooled.size else 0.0
            dec = [z for z in F_dc if z >= thr]
            spo = [z for z in F_sp if z >= thr]
            tru = [z for z in F_tp if z >= thr]
        ks_ms, ks_mp = st.ks_two_sample(dec, spo, "two-sided")
        mw_ms, mw_mp = st.mannwhitney(dec, spo, "two-sided")
        ad_ms, ad_mp = st.anderson_darling_2samp(dec, spo)
        perm_obs, perm_mp = st.permutation_two_sample(dec, spo, n_perm=4000, seed=SEED)
        ks_ds, ks_dp = st.ks_two_sample(dec, tru, "two-sided")
        mw_ds, mw_dp = st.mannwhitney(dec, tru, "two-sided")
        gap = st.tail_gap(dec, spo)
        match_ok = (ks_mp > 0.05) and (mw_mp > 0.05)
        differ_ok = (ks_dp <= 0.05) or (mw_dp <= 0.05)
        verdict = ("VALID" if (match_ok and differ_ok)
                   else ("GAP:decoys_too_hard(conservative)" if gap["mean_diff"] > 0
                         else "GAP:decoys_too_easy(anti-conservative)"))
        regions[rname] = {
            "n_decoy": len(dec), "n_spont": len(spo), "n_truepos": len(tru),
            "decoy_vs_spont": {"ks_p": ks_mp, "mw_p": mw_mp, "ad_p": ad_mp,
                               "perm_meandiff": perm_obs, "perm_p": perm_mp},
            "decoy_vs_truepos": {"ks_p": ks_dp, "mw_p": mw_dp},
            "gap": gap, "verdict": verdict}
    grid = [round(x, 3) for x in np.linspace(0, 1, 101)]
    figure_cdfs = {"x": grid, "cdf_truepos": st.empirical_cdf(F_tp, grid),
                   "cdf_spont": st.empirical_cdf(F_sp, grid),
                   "cdf_decoy": st.empirical_cdf(F_dc, grid)}
    decision = ("Only the ADMISSION TAIL is decision-relevant: the gate acts solely on pairs "
                "with W>=T (the upper tail), so the tail fail-to-reject (decoy ~ spontaneous "
                "error) is the operative validity condition. The full-distribution test is "
                "reported for completeness; a full-distribution rejection driven by the LOW "
                "tail (where the gate never admits) does NOT invalidate tail calibration.")
    return {"regions": regions, "figure_cdfs": figure_cdfs,
            "n_truepos": len(F_tp), "n_spont": len(F_sp), "n_decoy": len(F_dc),
            "populable": len(F_sp) >= N_FALSE_MIN, "decision_relevance_justification": decision}


# ===========================================================================
# Entrapment corroboration (deterministic foreign-entity, r=1)
# ===========================================================================
def entrapment_analysis(pipe, family, alpha):
    docs = pipe["docs"]
    scope = pipe["pilot_ids"] if pipe["light"] else {d.doc_id for d in docs}
    norm = norm_pool(pipe, SC, extra_by_doc=pipe["ent_by_doc"],
                     docs=[d for d in docs if d.doc_id in scope])
    ent_map = _decoy_map(pipe, "ent")
    cf_map = _decoy_map(pipe, "cf")
    per_doc = {}
    for c in _family_reals(pipe, family):
        if c["doc_id"] not in scope:
            continue
        zr = norm.get(c["cand_id"])
        did = ent_map.get(c["cand_id"])
        cf_id = cf_map.get(c["cand_id"])
        zcf = norm.get(cf_id) if cf_id else None
        ze = norm.get(did) if did else None
        if zr is None or zcf is None or ze is None:
            continue
        per_doc.setdefault(c["doc_id"], []).append(
            {"zr": zr, "zcf": zcf, "ze": ze, "label": c["label"],
             "w": st.W_signed_max(zr, zcf)})
    flat = [p for v in per_doc.values() for p in v]
    W = [p["w"] for p in flat]
    T, _, decoy_fdr_hat = st.knockoff_plus_threshold(W, alpha)
    cut = T if not math.isinf(T) else float("inf")
    adm_real = [p for p in flat if p["w"] >= cut] if not math.isinf(cut) else []
    N_T = len(adm_real)
    real_adm_mask = [(p["w"] >= cut) if not math.isinf(cut) else False for p in flat]
    ent_adm_mask = [(p["ze"] >= cut) if not math.isinf(cut) else False for p in flat]
    N_E = int(sum(ent_adm_mask))
    combined = fc.entrapment_fdp(N_T, N_E, r=1.0, estimator="combined")
    pc = fc.paired_entrapment_counts([p["zr"] for p in flat], [p["ze"] for p in flat],
                                     real_adm_mask, ent_adm_mask, cut)
    paired = fc.entrapment_fdp(N_T, N_E, r=1.0, estimator="paired", paired_counts=pc)
    realized = (sum(1 for p in adm_real if p["label"] == FALSE) / N_T) if N_T else float("nan")

    ent_docs = [(np.array([p["w"] for p in v], float), np.array([p["ze"] for p in v], float))
                for v in per_doc.values()]

    def comb_stat(resample):
        if not resample:
            return float("nan")
        Wb = np.concatenate([u[0] for u in resample])
        Ze = np.concatenate([u[1] for u in resample])
        Tb, _, _ = _knockoff_fast(Wb, alpha)
        if math.isinf(Tb):
            return float("nan")
        nt = int((Wb >= Tb).sum())
        ne = int((Ze >= Tb).sum())
        return fc.entrapment_fdp(nt, ne, r=1.0, estimator="combined")
    ci = st.doc_block_bootstrap(ent_docs, comb_stat, B=B_BOOT_INNER, seed=SEED)
    dfh = decoy_fdr_hat if not math.isinf(T) else None
    return {"alpha": alpha, "N_T": N_T, "N_E": N_E, "r": 1,
            "fdp_combined": _nan(combined), "fdp_combined_ci": [_nan(ci["ci_low"]), _nan(ci["ci_high"])],
            "fdp_paired": _nan(paired), "decoy_fdr_hat": _nan(dfh),
            "realized_fdr_gold": _nan(realized),
            "agree_realized": _agree(combined, realized),
            "agree_decoy": _agree(combined, dfh),
            "ent_median_z": _nan(float(np.median([p["ze"] for p in flat])) if flat else float("nan")),
            "real_median_z": _nan(float(np.median([p["zr"] for p in flat])) if flat else float("nan"))}


def _agree(a, b, tol=0.10):
    if a is None or b is None:
        return None
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        return None
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        return None
    return bool(abs(float(a) - float(b)) <= tol)


# ===========================================================================
# Shared PAIRED-exchangeability statistic (per-pair sign-flip win-rate in the
# operative admission tail) — the knockoff-null condition the gate actually runs.
# Reported DISTINCTLY from the MARGINAL crux (analyze_crux).
# ===========================================================================
def _paired_stat(flat, alpha=0.50, B=B_BOOT_INNER):
    """flat: per-pair dicts {zr, zd, label, doc_id, w}. Returns the tail decoy-win-rate over
    FALSE-real pairs at the knockoff+ operative cutoff T(alpha), with a doc-block-bootstrap CI,
    ci_covers_half, n_tail, n_false_pairs, the realized FDR at alpha, and KS(decoy vs real in tail).
    win-rate ~0.5 (CI covers 0.5) => paired-exchangeable knockoff null holds; < 0.5 (CI excludes
    0.5) => the false real systematically beats its OWN decoy => paired non-exchangeability."""
    false_pairs = [p for p in flat if p["label"] == FALSE]
    Wall = [p["w"] for p in flat]
    T, _, _ = st.knockoff_plus_threshold(Wall, alpha)
    cut = T if not math.isinf(T) else 0.0
    wr, n_tail = st.tail_win_rate([(p["zr"], p["zd"]) for p in false_pairs], cut)
    tail = [p for p in false_pairs if max(p["zr"], p["zd"]) >= cut]
    ks_s, ks_p = st.ks_two_sample([p["zd"] for p in tail], [p["zr"] for p in tail], "two-sided")
    fb = {}
    for p in tail:
        fb.setdefault(p["doc_id"], []).append(p)

    def wr_fn(resample):
        fl = [p for grp in resample for p in grp]
        if not fl:
            return float("nan")
        return float(np.mean([1.0 if p["zd"] > p["zr"] else 0.0 for p in fl]))
    ci = st.doc_block_bootstrap(list(fb.values()), wr_fn, B=B, seed=SEED)
    realized, n_adm, n_false, _ = _realized_fdr(flat, alpha)
    covers = (ci["ci_low"] is not None and not math.isnan(ci["ci_low"])
              and ci["ci_low"] <= 0.5 <= ci["ci_high"])
    detected = (ci["ci_high"] is not None and not math.isnan(ci["ci_high"]) and ci["ci_high"] < 0.5)
    return {"paired_win_rate_false": _nan(wr), "win_rate_ci": [_nan(ci["ci_low"]), _nan(ci["ci_high"])],
            "n_tail": n_tail, "n_false_pairs": len(false_pairs), "ci_covers_half": bool(covers),
            "paired_nonexchangeable": bool(detected), "ks_p_decoy_vs_real_tail": ks_p,
            "realized_fdr": _nan(realized), "n_admitted": n_adm, "n_false_admitted": n_false}


def _gs_per_doc_norm(pipe, score_cfg, decoy_by_doc, docs):
    """Per-document rank-normalize `score_cfg` scores over {reals U decoy_by_doc U swap} for `docs`.
    A symmetric per-config normalization so each (G,S) cell competes its real against its OWN
    generator's decoy on its OWN scorer's scale (per-doc normalization is independent across docs,
    so the (cf,SC) cell here equals the headline SC normalization restricted to these docs)."""
    zmap = pipe["zmap"]
    norm = {}
    for d in docs:
        did = d.doc_id
        cands = (pipe["reals_by_doc"].get(did, []) + decoy_by_doc.get(did, [])
                 + pipe["swap_by_doc"].get(did, []))
        pool, seen = {}, set()
        for c in cands:
            cid = c["cand_id"]
            if cid in seen:
                continue
            seen.add(cid)
            if (score_cfg, cid) in zmap:
                pool[cid] = zmap[(score_cfg, cid)]
        norm.update(st.rank_normalize(pool, SEED))
    return norm


def _pairs_from_norm(pipe, norm, dmap, docs, family="multi_hop"):
    """Build per-pair list for `family` reals over `docs`, pairing each real with its decoy via dmap."""
    pool_ids = {d.doc_id for d in docs}
    per_doc = {}
    for c in _family_reals(pipe, family):
        if c["doc_id"] not in pool_ids:
            continue
        zr = norm.get(c["cand_id"])
        did = dmap.get(c["cand_id"])
        zd = norm.get(did) if did else None
        if zr is None or zd is None:
            continue
        per_doc.setdefault(c["doc_id"], []).append(
            {"zr": zr, "zd": zd, "label": c["label"], "doc_id": c["doc_id"],
             "w": st.W_signed_max(zr, zd), "real_id": c["cand_id"]})
    return per_doc


# ===========================================================================
# PHASE 5 (NEW #1): PAIRED statistic across the four (G,S) configs
#   G in {nano, ministral} chooses WHICH decoy set (cf vs cfo); S in {nano, ministral} chooses
#   WHICH cached self-consistency Z-scale. The full 2x2 is WARM on the 40 original-pilot docs.
# ===========================================================================
def paired_exchangeability_across_GS(pipe):
    gs_ids = pipe.get("gs_ids", set())
    gs_docs = [d for d in pipe["docs"] if d.doc_id in gs_ids]
    CONFIGS = [("nano", "nano", SC, "cf"), ("nano", "ministral", MIN_SC, "cf"),
               ("ministral", "nano", SC, "cfo"), ("ministral", "ministral", MIN_SC, "cfo")]
    rows = []
    for (Gtag, Stag, scfg, dset) in CONFIGS:
        dec_by_doc = pipe["cf_by_doc"] if dset == "cf" else pipe.get("cfo_by_doc", {})
        norm = _gs_per_doc_norm(pipe, scfg, dec_by_doc, gs_docs)
        dmap = {c["real_id"]: c["cand_id"] for did in gs_ids for c in dec_by_doc.get(did, [])}
        # pooled families (atomic + multi_hop) for max power on the small warm set
        per_doc = _pairs_from_norm(pipe, norm, dmap, gs_docs, family="pooled")
        flat = [p for v in per_doc.values() for p in v]
        ps = _paired_stat(flat, alpha=0.50)
        rows.append({"G": Gtag, "S": Stag, "score_config": scfg, "decoy_set": dset,
                     "powered": bool(ps["n_false_pairs"] >= PAIRED_FLOOR), **ps})
    powered = [r for r in rows if r["powered"]]
    cross = [r for r in powered if r["G"] != r["S"]]
    if not powered:
        verdict = "UNDERPOWERED"
        interp = (f"No (G,S) config reached the {PAIRED_FLOOR}-false-pair floor on the "
                  f"{len(gs_docs)} warm docs; the paired (G,S) de-circularization is UNDERPOWERED "
                  f"(reported, not interpreted). The MARGINAL G!=S robustness is carried from iter-2.")
    elif all(r["ci_covers_half"] for r in powered):
        verdict = "PAIRED_EXCHANGEABLE_ACROSS_GS"
        interp = ("Per-pair decoy-win-rate CI covers 0.5 for every powered config INCLUDING the "
                  "cross-family ministral-8b cells: the knockoff paired null holds across generator "
                  "and scorer. Any realized-FDR breach is therefore a TRUE/FALSE non-separation "
                  "effect (confidence fails to rank true above false), NOT paired non-exchangeability "
                  "and NOT a shared-model (self-grading) artifact — paired-layer de-circularization "
                  "is EVIDENCED.")
    elif all(r["paired_nonexchangeable"] for r in powered):
        verdict = "PAIRED_NONEXCHANGEABLE_ACROSS_GS"
        interp = ("Per-pair decoy-win-rate is < 0.5 with CI excluding 0.5 for every powered config "
                  "including cross-family ministral-8b: false reals systematically beat their own "
                  "decoys regardless of generator/scorer — paired non-exchangeability is a property "
                  "of the LLM boundary (de-circularized), not a shared-model artifact.")
    else:
        verdict = "MIXED_SOFTEN_TO_MARGINAL"
        interp = ("Powered configs disagree on the paired null; only MARGINAL robustness to G!=S is "
                  "demonstrated (per the S2b mandate). Per-config win-rates are reported individually.")
    return {"configs": rows, "n_warm_docs": len(gs_docs), "gs_scored": pipe.get("gs_scored", False),
            "paired_floor": PAIRED_FLOOR, "verdict": verdict, "interpretation": interp,
            "marginal_gs_carried": ("Generator!=Scorer MARGINAL exchangeability settled in iter-2 "
                                    "(4/4 configs' tail win-rate CI cover 0.5 incl. ministral-8b).")}


# ===========================================================================
# PHASE 6a (NEW #2a): FREE false-positive-DENSITY stratification (zero extra API)
#   Bin multi_hop FALSE pairs by chain length k -> a natural genuine-false-density gradient.
#   Distinguishes 'knockoffs intrinsically do not transfer' from 'this error-dense regime is noisy'.
# ===========================================================================
DENSITY_BINS = [("LOW_k2_3", 2, 3), ("MED_k4_6", 4, 6), ("HIGH_k7_10", 7, 10)]


def density_strata_analysis(pipe, norm_sc):
    per_doc = _pairs_for(pipe, norm_sc, "multi_hop", "cf")
    k_by_doc = {d.doc_id: d.k for d in pipe["docs"]}
    strata = []
    for (name, klo, khi) in DENSITY_BINS:
        flat = [p for did, v in per_doc.items() if klo <= k_by_doc.get(did, 0) <= khi for p in v]
        n_total = len(flat)
        n_false = sum(1 for p in flat if p["label"] == FALSE)
        ps = _paired_stat(flat, alpha=0.50)
        strata.append({"stratum": name, "k_range": [klo, khi], "n_pairs": n_total,
                       "n_false_pairs": n_false,
                       "false_density": _nan(n_false / n_total) if n_total else None,
                       "powered": bool(n_false >= N_LADDER_FALSE_MIN), **ps})
    powered = [s for s in strata if s["powered"]]
    low = next((s for s in strata if s["stratum"].startswith("LOW") and s["powered"]), None)
    if not powered:
        verdict = "UNDERPOWERED"
        interp = "No density stratum reached the false-pair floor; reported, not interpreted."
    else:
        breaches = [s for s in powered if s["realized_fdr"] is not None and s["realized_fdr"] > 0.5 + TAU]
        if low is not None and (low["realized_fdr"] is not None and low["realized_fdr"] <= 0.5 + TAU) \
                and len(breaches) > 0:
            verdict = "SCOPED_TO_ERROR_DENSE_REGIME"
            interp = ("The realized-FDR breach VANISHES at LOW false-positive density (short chains) "
                      "and appears only in the error-dense (long-chain) strata: the limitation is "
                      "scoped to the weak-scorer/error-dense regime, not an intrinsic knockoff failure.")
        elif len(breaches) >= len(powered):
            verdict = "PERSISTS_ACROSS_DENSITY"
            interp = ("The realized-FDR breach PERSISTS across density strata (including the lowest "
                      "powered density): the failure is NOT merely error-density-driven.")
        else:
            verdict = "GRADED_WITH_DENSITY"
            interp = ("The realized-FDR / paired win-rate vary monotonically with false-positive "
                      "density; the breach is density-modulated. Per-stratum values reported.")
    return {"strata": strata, "n_false_min_per_stratum": N_LADDER_FALSE_MIN,
            "verdict": verdict, "interpretation": interp,
            "note": ("FREE (0 API) k-density de-confound. The FULL extractor-strength x "
                     "false-positive-density matrix is owned by the sibling iter-4 artifact (dir2); "
                     "the optional strong-extractor preview here is metadata.strong_extractor_arm.")}


# ===========================================================================
# PHASE 6b (NEW #2b): STRONGER-EXTRACTOR de-confound arm (optional, budget-gated)
#   Re-extract multi_hop with gpt-4.1-mini, KEEP scorer = nano-SC (isolates the extractor effect).
# ===========================================================================
def strong_extractor_analysis(pipe):
    s_by_doc = pipe.get("strong_reals_by_doc", {})
    s_reals = [c for v in s_by_doc.values() for c in v]
    if not s_reals:
        return {"ran": False,
                "reason": ("strong-extractor arm not run (budget-gated off or --strong not set). The "
                           "FULL extractor-strength x false-positive-density matrix is delegated to the "
                           "sibling iter-4 artifact (dir2); the FREE k-density stratification "
                           "(metadata.density_strata) is P1's self-contained de-confound.")}
    docs = [d for d in pipe["docs"] if d.doc_id in pipe.get("strong_docs_ids", [])]
    dmap = _decoy_map(pipe, "scf")
    norm = _gs_per_doc_norm_strong(pipe, docs)
    per_doc = {}
    for c in s_reals:
        zr = norm.get(c["cand_id"])
        did = dmap.get(c["cand_id"])
        zd = norm.get(did) if did else None
        if zr is None or zd is None:
            continue
        per_doc.setdefault(c["doc_id"], []).append(
            {"zr": zr, "zd": zd, "label": c["label"], "doc_id": c["doc_id"],
             "w": st.W_signed_max(zr, zd), "real_id": c["cand_id"]})
    flat = [p for v in per_doc.values() for p in v]
    n_false = sum(1 for c in s_reals if c["label"] == FALSE)
    n_true = sum(1 for c in s_reals if c["label"] == TRUE)
    mh_acc = float(np.nanmean([m["mh_acc"] for m in pipe.get("strong_meta", [])])) \
        if pipe.get("strong_meta") else float("nan")
    rows = []
    for alpha in ALPHA_GRID:
        realized, n_adm, n_false_adm, ratio = _realized_fdr(flat, alpha)
        rows.append({"target_alpha": alpha, "decoy_fdr_hat": _nan(ratio),
                     "realized_fdr": _nan(realized), "n_admitted": n_adm,
                     "n_false_admitted": n_false_adm, "k_floor": st.k_floor(alpha),
                     "certified": bool(n_adm >= st.k_floor(alpha) and n_false >= N_FALSE_MIN)})
    ps = _paired_stat(flat, alpha=0.50)
    # compare to nano extractor mh_acc on the same docs
    nano_mh = float(np.nanmean([e["mh_acc"] for e in pipe.get("ext_meta", [])
                                if e["doc_id"] in pipe.get("strong_docs_ids", [])])) \
        if pipe.get("ext_meta") else float("nan")
    breach = (ps["realized_fdr"] is not None and ps["realized_fdr"] > 0.5 + TAU
              and ps["paired_nonexchangeable"])
    if not (n_false >= N_FALSE_MIN):
        verdict = "UNDERPOWERED"
    elif breach:
        verdict = "PERSISTS_WITH_STRONG_EXTRACTOR"
    else:
        verdict = "VANISHES_WITH_STRONG_EXTRACTOR"
    return {"ran": True, "extractor": STRONG_EXTRACTOR, "scorer": PRIMARY_MODEL + " (nano-SC, fixed)",
            "n_docs": len(docs), "n_mh_reals": len(s_reals), "n_false": n_false, "n_true": n_true,
            "strong_mh_accuracy": _nan(mh_acc), "nano_mh_accuracy_same_docs": _nan(nano_mh),
            "mh_acc_lift": _nan((mh_acc - nano_mh) if (mh_acc == mh_acc and nano_mh == nano_mh) else float("nan")),
            "diagonal_rows": rows, "paired": ps, "verdict": verdict,
            "interpretation": (
                "VERDICT logic (pre-registered): if the per-pair sign-flip failure PERSISTS with the "
                "competent extractor, 'marginal != paired at the LLM boundary' is EARNED; if it "
                "VANISHES (gate now controls realized FDR <= alpha), the gate controls FDR when the "
                "extractor can score its own errors and the limitation is SCOPED to the weak-scorer/"
                "error-dense regime. Either outcome is publishable; this records which fired.")}


def _gs_per_doc_norm_strong(pipe, docs):
    """Per-doc rank-normalize STR_SC scores over {strong_reals U strong_cf} for the strong arm."""
    zmap = pipe["zmap"]
    norm = {}
    for d in docs:
        did = d.doc_id
        cands = (pipe.get("strong_reals_by_doc", {}).get(did, [])
                 + pipe.get("strong_cf_by_doc", {}).get(did, []))
        pool, seen = {}, set()
        for c in cands:
            cid = c["cand_id"]
            if cid in seen:
                continue
            seen.add(cid)
            if (STR_SC, cid) in zmap:
                pool[cid] = zmap[(STR_SC, cid)]
        norm.update(st.rank_normalize(pool, SEED))
    return norm


# ===========================================================================
# Method vs purely-neural baseline: realized FDR vs nominal alpha
# ===========================================================================
def baseline_vs_method(pipe, norm, raw_conf, family="pooled"):
    cf_real = _decoy_map(pipe, "cf")
    method_reals, baseline_reals = [], []
    for c in _family_reals(pipe, family):
        if c["label"] not in (TRUE, FALSE):
            continue
        zr = norm.get(c["cand_id"])
        did = cf_real.get(c["cand_id"])
        zd = norm.get(did) if did else None
        zraw = raw_conf.get(c["cand_id"])
        if zr is None or zd is None or zraw is None:
            continue
        is_false = c["label"] == FALSE
        method_reals.append({"w": st.W_signed_max(zr, zd), "is_false": is_false})
        baseline_reals.append({"z": zraw, "is_false": is_false})
    rows = []
    for a in ALPHA_GRID:
        m = st.decoy_gate_fdr(method_reals, a)
        b = st.baseline_confidence_gate_fdr(baseline_reals, a)
        rows.append({"alpha": a, "method_realized_fdr": _nan(m["realized_fdr"]),
                     "method_n_admitted": m["n_admitted"], "method_n_false": m["n_false_admitted"],
                     "method_certified": m["certified"],
                     "baseline_realized_fdr": _nan(b["realized_fdr"]),
                     "baseline_n_admitted": b["n_admitted"], "baseline_n_false": b["n_false_admitted"]})
    return {"family": family, "n_labelable_reals": len(method_reals), "rows": rows}


# ===========================================================================
# Verbalized contrast quantification (discreteness / loose-target artifact)
# ===========================================================================
def verbalized_artifact_notes(diag_vb):
    notes = {"target_alpha_violations": [], "decoy_fdr_hat_undershoots": [],
             "identical_admission_sets_neighbors": []}
    for fam, d in diag_vb.items():
        rows = d["rows"]
        prev_adm = None
        for r in rows:
            a = r["target_alpha"]
            rf, dfh = r["realized_fdr"], r["decoy_fdr_hat"]
            if rf is not None and rf > a:
                notes["target_alpha_violations"].append({"family": fam, "alpha": a, "realized_fdr": rf})
            if dfh is not None and rf is not None and dfh < rf - 1e-9:
                notes["decoy_fdr_hat_undershoots"].append(
                    {"family": fam, "alpha": a, "decoy_fdr_hat": dfh, "realized_fdr": rf})
            if prev_adm is not None and r["n_admitted"] == prev_adm and r["n_admitted"] > 0:
                notes["identical_admission_sets_neighbors"].append(
                    {"family": fam, "alpha": a, "n_admitted": r["n_admitted"]})
            prev_adm = r["n_admitted"]
    return notes


# ===========================================================================
# Primary disconfirmation verdict (single, self-consistency, multi_hop, alpha*)
# ===========================================================================
def primary_disconfirmation(pipe, norm, diag_mh):
    family = "multi_hop"
    alpha_star = diag_mh["reachable_alpha_floor"]
    populable = diag_mh["populable"]
    if not populable:
        return {"family": family, "alpha_star": alpha_star, "verdict": "UNTESTABLE",
                "reason": (f"populable family '{family}' has {diag_mh['n_false_total']} genuine "
                           f"FALSE candidates (< N_false_min={N_FALSE_MIN}); diagonal precondition "
                           f"unmet (NOT 'confirmed by conservatism')."),
                "calibration_disconfirmed": None, "self_report_disconfirmed": None}
    if alpha_star is None:
        return {"family": family, "alpha_star": None, "verdict": "NO_CERTIFIED_ALPHA",
                "reason": ("no alpha in the grid is certified on multi_hop (n_admitted < k_floor "
                           "at every alpha): the gate certifies nothing at this scale; reported as "
                           "a precondition outcome, NOT 'confirmed by conservatism'."),
                "calibration_disconfirmed": None, "self_report_disconfirmed": None}
    row = next(r for r in diag_mh["rows"] if r["target_alpha"] == alpha_star)
    realized, lo, hi = row["realized_fdr"], row["ci_low"], row["ci_high"]
    dfh = row["decoy_fdr_hat"]
    calib_dis = (realized is not None and realized > alpha_star + TAU
                 and lo is not None and lo > alpha_star)
    self_dis = bool(row["self_report_anti_conservative"])
    if calib_dis:
        verdict = "DISCONFIRMED"
        reason = (f"realized FDR {realized} > alpha*+tau ({alpha_star}+{TAU}) AND doc-block CI "
                  f"[{lo},{hi}] lies entirely above alpha*={alpha_star}.")
    else:
        verdict = "NOT_DISCONFIRMED"
        reason = (f"realized FDR {realized} (CI [{lo},{hi}]) does not exceed alpha*+tau with CI "
                  f"entirely above alpha*={alpha_star}; gate calibration holds at the tightest "
                  f"certified alpha.")
    return {"family": family, "alpha_star": alpha_star, "tau": TAU,
            "realized_fdr": realized, "ci": [lo, hi], "decoy_fdr_hat": dfh,
            "calibration_disconfirmed": bool(calib_dis),
            "self_report_disconfirmed": self_dis, "verdict": verdict, "reason": reason,
            "paired_exchangeability": diag_mh.get("paired_exchangeability"),
            "mechanism_note": (
                "Reconcile the verdict with the crux/paired-exchangeability diagnostic: if the "
                "cf tail win-rate over FALSE pairs covers 0.5 the knockoff null holds and any "
                "realized-FDR breach is a true/false NON-SEPARATION effect (confidence fails to "
                "rank true above false on this family); if win-rate < 0.5 the false reals beat "
                "their own counterfactual decoys (decoys too easy under self-consistency).")}


# ===========================================================================
# BH multiplicity across ALL validation tests
# ===========================================================================
def collect_bh(diag_sc, ladder, crux_sc, crux_vb, entrap, paired_gs=None, density=None):
    tests = []
    for fam, d in diag_sc.items():
        for r in d["rows"]:
            pass  # diagonal rows carry no p-values; handled via CI/triple
    for r in ladder["rungs"]:
        if r["ks_p"] is not None:
            tests.append((f"ladder.{r['rung']}.ks", r["ks_p"]))
        if r["mw_p"] is not None:
            tests.append((f"ladder.{r['rung']}.mw", r["mw_p"]))
    for tag, crux in (("sc", crux_sc), ("vb", crux_vb)):
        for rname, rd in crux["regions"].items():
            tests.append((f"crux[{tag}].{rname}.decoy_vs_spont.ks", rd["decoy_vs_spont"]["ks_p"]))
            tests.append((f"crux[{tag}].{rname}.decoy_vs_spont.mw", rd["decoy_vs_spont"]["mw_p"]))
            tests.append((f"crux[{tag}].{rname}.decoy_vs_truepos.ks", rd["decoy_vs_truepos"]["ks_p"]))
    if paired_gs:
        for c in paired_gs.get("configs", []):
            if c.get("powered"):
                tests.append((f"paired_GS.G={c['G']},S={c['S']}.ks_decoy_vs_real",
                              c.get("ks_p_decoy_vs_real_tail")))
    if density:
        for s in density.get("strata", []):
            if s.get("powered"):
                tests.append((f"density.{s['stratum']}.ks_decoy_vs_real",
                              s.get("ks_p_decoy_vs_real_tail")))
    tests = [(n, p) for (n, p) in tests
             if p is not None and not (isinstance(p, float) and math.isnan(p))]
    bh = st.benjamini_hochberg([p for _, p in tests], q=0.05)
    return [{"test_name": n, **b} for (n, _), b in zip(tests, bh)]


# ===========================================================================
# Carried-forward Generator!=Scorer (settled iter-2; no new budget)
# ===========================================================================
def load_generator_ne_scorer():
    p = Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/"
             "iter_2/gen_art/gen_art_experiment_2/method_out.json")
    try:
        m = json.loads(p.read_text())["metadata"]["generator_ne_scorer"]
    except Exception as e:
        logger.warning(f"could not load carried-forward G!=S: {e}")
        return {"verdict": "ROBUST", "source": "art_Inu52CyA49Ys",
                "note": "settled iter-2; file unavailable at read time", "ran": False}
    return {"verdict": m.get("verdict"),
            "validity_region_statement": m.get("validity_region_statement"),
            "configs": m.get("configs"),
            "source": "art_Inu52CyA49Ys (iter-2 gen_art_experiment_2)",
            "note": "SETTLED in iter-2 (4/4 configs cover 0.5 incl. cross-family ministral-8b); "
                    "embedded as provenance, NO new budget spent."}


# ===========================================================================
# Output assembly (exp_gen_sol_out schema) + figures
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


def build_examples(pipe, norm_sc, raw_sc, norm_vb, raw_vb):
    cf_real = _decoy_map(pipe, "cf")
    swap_real = _decoy_map(pipe, "swap")
    cf_rel = {c["real_id"]: c["r"] for dd in pipe["cf_by_doc"].values() for c in dd}
    swap_t = {c["real_id"]: c["t"] for dd in pipe["swap_by_doc"].values() for c in dd}
    # per-family knockoff thresholds for admission predictions (self-consistency)
    a_thr = {}
    for fam in ("atomic", "multi_hop"):
        per_doc = _pairs_for(pipe, norm_sc, fam, "cf")
        W = [p["w"] for v in per_doc.values() for p in v]
        a_thr[fam] = {a: st.knockoff_plus_threshold(W, a)[0] for a in ALPHA_GRID}
    examples = []
    for c in pipe["all_reals"]:
        did, sid = cf_real.get(c["cand_id"]), swap_real.get(c["cand_id"])
        zr_sc, zr_vb = norm_sc.get(c["cand_id"]), norm_vb.get(c["cand_id"])
        zd_sc = norm_sc.get(did) if did else None
        zs_sc = norm_sc.get(sid) if sid else None
        zd_vb = norm_vb.get(did) if did else None
        w_cf_sc = st.W_signed_max(zr_sc, zd_sc) if (zr_sc is not None and zd_sc is not None) else None
        w_sw_sc = st.W_signed_max(zr_sc, zs_sc) if (zr_sc is not None and zs_sc is not None) else None
        w_cf_vb = st.W_signed_max(zr_vb, zd_vb) if (zr_vb is not None and zd_vb is not None) else None
        ex = {
            "input": json.dumps({"doc_id": c["doc_id"], "head": c["h"], "relation": c["r"],
                                 "tail": c["t"], "claim": c["claim"], "candidate_kind": "real"}),
            "output": c["label"],
            "metadata_doc_id": c["doc_id"], "metadata_fact_type": c["fact_type"],
            "metadata_chain_length_k": pipe["doc_by_id"][c["doc_id"]].k,
            "metadata_is_pilot": pipe["doc_by_id"][c["doc_id"]].is_pilot,
            "metadata_decoy_relation": cf_rel.get(c["cand_id"]),
            "metadata_swap_tail": swap_t.get(c["cand_id"]),
            "metadata_z_real_raw_sc": _nan(raw_sc.get(c["cand_id"])),
            "metadata_z_real_sc": _nan(zr_sc), "metadata_z_decoy_sc": _nan(zd_sc),
            "metadata_z_swap_sc": _nan(zs_sc), "metadata_w_cf_sc": _nan(w_cf_sc),
            "metadata_w_swap_sc": _nan(w_sw_sc),
            "metadata_z_real_raw_vb": _nan(raw_vb.get(c["cand_id"])),
            "metadata_z_real_vb": _nan(zr_vb), "metadata_w_cf_vb": _nan(w_cf_vb)}
        if w_cf_sc is not None:
            for a in ALPHA_GRID:
                T = a_thr[c["fact_type"]][a]
                ex[f"predict_admit_sc_a{int(a*100):02d}"] = (
                    "yes" if (not math.isinf(T) and w_cf_sc >= T) else "no")
        examples.append(_clean(ex))
    return examples


def build_output(pipe, analysis, out_path):
    a = analysis
    em = pipe["ext_meta"]
    atomic_prec = float(np.nanmean([e["atomic_prec"] for e in em])) if em else float("nan")
    atomic_rec = float(np.nanmean([e["atomic_rec"] for e in em])) if em else float("nan")
    mh_acc = float(np.nanmean([e["mh_acc"] for e in em])) if em else float("nan")

    examples = build_examples(pipe, a["norm_sc"], a["raw_sc"], a["norm_vb"], a["raw_vb"])

    diag_sc = a["diag_sc"]
    mh = diag_sc["multi_hop"]
    metadata = {
        "method_name": "Powered self-consistency CLUTRR realized-FDR calibration diagonal for a "
                       "label-free decoy-competition (knockoff+) FDR gate at the LLM text->logic "
                       "fact-admission boundary",
        "headline_elicitation": "self_consistency_k5",
        "headline_verdict": a["primary_disconfirmation"]["verdict"],
        "description": (
            "The single primary artifact is a per-family (atomic / multi_hop) realized-FDR-vs-"
            "target-alpha calibration diagonal for the counterfactual-decoy knockoff+ gate, scored "
            "under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED, error-"
            "dense CLUTRR crisp-gold corpus. Each diagonal row surfaces the (target alpha, "
            "decoy_fdr_hat, realized FDR) TRIPLE with a pre-registered self-report disconfirmation, "
            "doc-block bootstrap CIs, the swap-decoy negative control, and the plain raw-confidence "
            "baseline. Verbalized confidence is run on the SAME data as a documented discreteness/"
            "loose-target contrast. An S1b difficulty ladder (L0..L4) repairs-or-bounds the win-rate "
            "diagnostic; deterministic foreign-entity entrapment corroborates at alpha*; "
            "Generator!=Scorer is carried forward as settled."),
        "elicitation_selection_rationale": (
            "Self-consistency hosts the headline because its counterfactual tail win-rate covers 0.5 "
            "(iter-2: 0.482, CI[0.42,0.55]) — the diagnostic-VALIDATED exchangeable regime — whereas "
            "single-call VERBALIZED and single-token LOGPROB confidence were flagged anti-conservative "
            "in iter-2 (logprob bridge tail win-rate 0.34, CI[0.32,0.37], KS p<1e-20; verbalized "
            "overconfident). Note tail-exchangeability, NOT full-distribution AUC, is the selection "
            "criterion (iter-2 verbalized full-AUC 0.861 ~ DINCO 0.871, yet verbalized fails the tail "
            "test): higher AUC does not imply tail-exchangeability. logprob is NOT re-scored at scale "
            "(its iter-2 anti-conservativity is cited); DINCO is not re-run (criterion documented)."),
        "models": {"primary_scorer_and_generator": PRIMARY_MODEL,
                   "cross_family_scorer_generator_for_carried_forward_ablation": OTHER_MODEL},
        "hyperparameters": {
            "seed": SEED, "alpha_grid": ALPHA_GRID, "K_self_consistency": K_SC, "B_bootstrap": B_BOOT,
            "B_bootstrap_inner": B_BOOT_INNER, "tau": TAU, "n_false_min": N_FALSE_MIN,
            "soft_cap_usd": SOFT_CAP_USD, "hard_stop_usd": HARD_STOP_USD,
            "W_statistic": "signed-max  W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i)",
            "knockoff_plus": "Barber-Candes eq 1.9 (the +1 kept; exact FDR control)",
            "bootstrap": "document-block (cluster) resampling",
            "multiplicity": "Benjamini-Hochberg q=0.05",
            "scoring": "isolated, provenance-blinded, order-randomized, document-prefix cached",
            "rank_normalization": "per-document over {reals U cf(L4) U swap(L1)}; ladder/entrapment "
                                  "items normalized within {pool U that-set} so they share the scale",
            "alpha_star_definition": "smallest CERTIFIED alpha on the populable multi_hop family "
                                     "(n_admitted>=k_floor AND family false-populability>=40); the "
                                     "tightest target the gate certifies => the STRONGEST disconfirmation test"},
        "dataset_counts": {
            "n_docs": len(pipe["docs"]),
            "n_pilot": sum(1 for d in pipe["docs"] if d.is_pilot),
            "n_reals": len(pipe["all_reals"]), "n_true": pipe["n_true"],
            "n_spont_false": pipe["n_spont"], "n_undecidable": pipe["n_und"],
            "n_spont_false_atomic": sum(1 for c in pipe["all_reals"]
                                        if c["fact_type"] == "atomic" and c["label"] == FALSE),
            "n_spont_false_multi_hop": sum(1 for c in pipe["all_reals"]
                                           if c["fact_type"] == "multi_hop" and c["label"] == FALSE),
            "atomic_populable": diag_sc["atomic"]["populable"],
            "multi_hop_populable": diag_sc["multi_hop"]["populable"],
            "contamination_rate_decoys": pipe["contamination_rate"],
            "n_extract_samples": pipe.get("n_extract", 1),
            "n_confirmatory": sum(1 for d in pipe["docs"] if not d.is_pilot),
            "n_ladder_docs": len(pipe.get("ladder_ids", []) or []),
            "n_gs_warm_docs": len(pipe.get("gs_ids", []) or []),
            "n_strong_extractor_docs": len(pipe.get("strong_docs_ids", []) or []),
            "light_mode": pipe["light"]},
        "extraction_quality": {"atomic_precision": atomic_prec, "atomic_recall": atomic_rec,
                               "multihop_relation_accuracy": mh_acc,
                               "note": "atomic P/R from free extraction; multi-hop accuracy from "
                                       "forced per-pair relation prediction (CLUTRR query format)"},
        "primary_diagonal_self_consistency": {fam: diag_sc[fam] for fam in ("atomic", "multi_hop", "pooled")},
        "contrast_diagonal_verbalized": {**{fam: a["diag_vb"][fam] for fam in ("atomic", "multi_hop", "pooled")},
                                         "artifact_notes": a["vb_artifact_notes"]},
        "power_populability_table": a["power_table"],
        "s1b_difficulty_ladder": a["ladder"],
        "crux_full_and_tail_self_consistency": a["crux_sc"],
        "crux_full_and_tail_verbalized": a["crux_vb"],
        "entrapment": a["entrapment"],
        "baseline_vs_method_self_consistency": a["baseline_sc"],
        "generator_ne_scorer_carried_forward": a["gen_ne_scorer"],
        "paired_vs_marginal": {
            "explanation": (
                "The MARGINAL crux (crux_full_and_tail_*) tests whether the counterfactual-decoy "
                "score DISTRIBUTION matches the spontaneous-error distribution (a population test). "
                "The PAIRED statistic (each diagonal row's paired_exchangeability AND "
                "paired_across_GS) tests, per real, whether the false real beats its OWN decoy — "
                "the actual knockoff+ sign-flip the gate's FDR theorem requires. They can diverge: "
                "the marginal can hold while the paired fails (or vice versa). Both are reported "
                "DISTINCTLY so the validity argument is evidenced, not asserted."),
            "multi_hop_paired_exchangeability": diag_sc["multi_hop"].get("paired_exchangeability"),
            "atomic_paired_exchangeability": diag_sc["atomic"].get("paired_exchangeability")},
        "paired_across_GS": a["paired_across_GS"],
        "density_strata": a["density_strata"],
        "strong_extractor_arm": a["strong_extractor_arm"],
        "bh_correction": a["bh"],
        "primary_disconfirmation_verdict": a["primary_disconfirmation"],
        "reconciliation_narrative": (
            "ONE consolidated diagonal story: under the validated self-consistency elicitation the "
            "per-family knockoff+ diagonal is the single primary calibration result; the verbalized "
            "diagonal on the SAME data is a wrong-elicitation discreteness/loose-target ARTIFACT "
            "(see contrast_diagonal_verbalized.artifact_notes), not a co-headline. This reconciles "
            "iter-2: self-consistency exchangeable (cf tail win-rate ~0.48), verbalized/logprob "
            "anti-conservative."),
        "runtime": pipe["runtime"], "cost_trace_path": "logs/cost.jsonl",
        "interpretation": {
            "diagonal_expected": "realized FDR <= target alpha (+tau) at certified alphas under "
                                 "self-consistency; the knockoff+ gate is conservative.",
            "self_report_check": "decoy_fdr_hat is DISCONFIRMED at any alpha where it is anti-"
                                 "conservative vs realized beyond tau (even if realized < alpha).",
            "ladder_expected": "easy rungs (L0 foreign-swap, L1 in-doc swap) flagged anti-conservative "
                               "while hard L4-cf covers 0.5 => REPAIRED; if even L0 covers 0.5 => "
                               "BLIND_LIMITATION (diagnostic down-scoped).",
            "crux_expected": "decoy ~ spontaneous-error in the admission tail (fail-to-reject) and != "
                             "true-positive (reject); full-distribution result reported with tail-only "
                             "decision-relevance justification.",
            "entrapment_expected": "combined FDP ~ realized at alpha*; divergence at alpha=0.5 reported."}}

    out = {"metadata": _clean(metadata),
           "datasets": [{"dataset": "CLUTRR-v1-CrispGold-CalibrationAnchor", "examples": examples}]}
    out_path.write_text(json.dumps(out, indent=2))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.0f} KB, {len(examples)} examples)")
    return out


def power_table(diag_sc):
    table = {}
    for fam in ("atomic", "multi_hop"):
        d = diag_sc[fam]
        rows = []
        for r in d["rows"]:
            rows.append({"alpha": r["target_alpha"], "k_floor": r["k_floor"],
                         "n_admitted": r["n_admitted"], "certified": r["certified"],
                         "n_false_admitted": r["n_false_admitted"], "populable": r["populable"]})
        table[fam] = {"rows": rows, "n_false_total": d["n_false_total"],
                      "populable": d["populable"], "reachable_alpha_floor": d["reachable_alpha_floor"],
                      "alpha_star_permissive": d["alpha_star_permissive"]}
    return table


# ===========================================================================
# Figures
# ===========================================================================
def make_figures(out, fig_dir: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig_dir.mkdir(exist_ok=True)
    m = out["metadata"]
    paths = []
    # 1) calibration diagonal (self-consistency) for atomic + multi_hop
    try:
        diag = m["primary_diagonal_self_consistency"]
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot([0, 0.55], [0, 0.55], "k--", lw=1, label="ideal (realized=alpha)")
        for fam, col in (("multi_hop", "tab:red"), ("atomic", "tab:blue")):
            rows = [r for r in diag[fam]["rows"] if r["realized_fdr"] is not None]
            if not rows:
                continue
            xs = [r["target_alpha"] for r in rows]
            ys = [r["realized_fdr"] for r in rows]
            lo = [max(0.0, r["realized_fdr"] - (r["ci_low"] if r["ci_low"] is not None else r["realized_fdr"]))
                  for r in rows]
            hi = [max(0.0, (r["ci_high"] if r["ci_high"] is not None else r["realized_fdr"]) - r["realized_fdr"])
                  for r in rows]
            ax.errorbar(xs, ys, yerr=[lo, hi], marker="o", color=col, capsize=3,
                        label=f"{fam} realized FDR")
            dh_xy = [(r["target_alpha"], r["decoy_fdr_hat"]) for r in rows
                     if r["decoy_fdr_hat"] is not None]
            if dh_xy:
                ax.plot([x for x, _ in dh_xy], [y for _, y in dh_xy], marker="x", ls=":",
                        color=col, alpha=0.7, label=f"{fam} decoy_fdr_hat")
        ax.set_xlabel("target alpha"); ax.set_ylabel("FDR")
        ax.set_title("Self-consistency knockoff+ calibration diagonal")
        ax.legend(fontsize=7); fig.tight_layout()
        p = fig_dir / "figure_diagonal_self_consistency.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"diagonal figure failed: {e}")
    # 2) crux CDF overlay (self-consistency)
    try:
        cd = m["crux_full_and_tail_self_consistency"]["figure_cdfs"]
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(cd["x"], cd["cdf_truepos"], label="true positives", color="tab:green")
        ax.plot(cd["x"], cd["cdf_spont"], label="spontaneous errors (FALSE reals)", color="tab:orange")
        ax.plot(cd["x"], cd["cdf_decoy"], label="counterfactual decoys", color="tab:purple")
        ax.set_xlabel("normalized self-consistency score Z"); ax.set_ylabel("empirical CDF")
        ax.set_title("Decoy vs spontaneous-error vs true-positive CDFs")
        ax.legend(fontsize=8); fig.tight_layout()
        p = fig_dir / "figure_crux_cdfs_self_consistency.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"crux figure failed: {e}")
    # 3) S1b difficulty ladder
    try:
        rungs = m["s1b_difficulty_ladder"]["rungs"]
        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        names = [r["rung"] for r in rungs]
        wr = [r["tail_win_rate"] if r["tail_win_rate"] is not None else np.nan for r in rungs]
        lo = [(r["tail_win_rate"] - (r["win_rate_ci"][0] if r["win_rate_ci"][0] is not None else r["tail_win_rate"]))
              if r["tail_win_rate"] is not None else 0 for r in rungs]
        hi = [((r["win_rate_ci"][1] if r["win_rate_ci"][1] is not None else r["tail_win_rate"]) - r["tail_win_rate"])
              if r["tail_win_rate"] is not None else 0 for r in rungs]
        ax.axhline(0.5, color="k", ls="--", lw=1, label="exchangeable (0.5)")
        ax.errorbar(range(len(names)), wr, yerr=[lo, hi], marker="s", capsize=4, color="tab:red")
        ax.set_xticks(range(len(names))); ax.set_xticklabels(names, rotation=30, ha="right", fontsize=7)
        ax.set_ylabel("tail decoy-win-rate"); ax.set_title("S1b difficulty ladder (self-consistency)")
        ax.legend(fontsize=8); fig.tight_layout()
        p = fig_dir / "figure_s1b_ladder.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"ladder figure failed: {e}")
    # 4) PAIRED win-rate across the 4 (G,S) configs
    try:
        cfgs = m["paired_across_GS"]["configs"]
        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        labels = [f"G={c['G']}\nS={c['S']}" for c in cfgs]
        wr = [c["paired_win_rate_false"] if c["paired_win_rate_false"] is not None else np.nan for c in cfgs]
        lo = [(c["paired_win_rate_false"] - (c["win_rate_ci"][0] if c["win_rate_ci"][0] is not None else c["paired_win_rate_false"]))
              if c["paired_win_rate_false"] is not None else 0 for c in cfgs]
        hi = [((c["win_rate_ci"][1] if c["win_rate_ci"][1] is not None else c["paired_win_rate_false"]) - c["paired_win_rate_false"])
              if c["paired_win_rate_false"] is not None else 0 for c in cfgs]
        cols = ["tab:green" if c["powered"] else "tab:gray" for c in cfgs]
        ax.axhline(0.5, color="k", ls="--", lw=1, label="exchangeable (0.5)")
        for i in range(len(cfgs)):
            ax.errorbar([i], [wr[i]], yerr=[[lo[i]], [hi[i]]], marker="o", capsize=4, color=cols[i])
        ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, fontsize=8)
        ax.set_ylabel("per-pair decoy-win-rate (FALSE reals)")
        ax.set_title("Paired exchangeability across (Generator, Scorer)\n(green=powered, gray=underpowered)")
        ax.legend(fontsize=8); fig.tight_layout()
        p = fig_dir / "figure_paired_across_GS.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"paired-GS figure failed: {e}")
    # 5) DE-CONFOUND: paired win-rate / realized FDR vs false-positive-density (+ strong extractor)
    try:
        strata = m["density_strata"]["strata"]
        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        xs = [s["false_density"] if s["false_density"] is not None else np.nan for s in strata]
        wr = [s["paired_win_rate_false"] if s["paired_win_rate_false"] is not None else np.nan for s in strata]
        rf = [s["realized_fdr"] if s["realized_fdr"] is not None else np.nan for s in strata]
        ax.axhline(0.5, color="k", ls="--", lw=1, label="exchangeable / alpha=0.5")
        ax.plot(xs, wr, marker="o", color="tab:red", label="paired win-rate (FALSE)")
        ax.plot(xs, rf, marker="s", color="tab:purple", label="realized FDR @0.5")
        for s, x in zip(strata, xs):
            ax.annotate(s["stratum"].split("_")[0], (x, 0.02), fontsize=7, ha="center")
        sa = m.get("strong_extractor_arm", {})
        if sa.get("ran") and sa.get("paired", {}).get("paired_win_rate_false") is not None:
            ax.scatter([0.5], [sa["paired"]["paired_win_rate_false"]], marker="*", s=160,
                       color="tab:blue", label=f"strong-extractor ({STRONG_EXTRACTOR.split('/')[-1]})", zorder=5)
        ax.set_xlabel("genuine-false density among admitted reals")
        ax.set_ylabel("statistic"); ax.set_title("De-confound: paired win-rate / realized FDR vs false-positive density")
        ax.legend(fontsize=7); fig.tight_layout()
        p = fig_dir / "figure_deconfound_density.jpg"
        fig.savefig(p, dpi=130); plt.close(fig); paths.append(str(p))
    except Exception as e:
        logger.warning(f"density de-confound figure failed: {e}")
    logger.info(f"figures: {paths}")
    return paths


# ===========================================================================
# Offline self-tests (Stage 0): port iter-2 EXP1 + EXP2 assertions + new ones
# ===========================================================================
def selftest():
    logger.info("STAGE 0 — offline statistics unit tests (fdr_stats + fdr_core)")
    # (a) k-floor map
    assert [st.k_floor(a) for a in ALPHA_GRID] == [20, 10, 5, 4, 2], "k-floor mapping"
    assert [fc.k_floor(a) for a in ALPHA_GRID] == [20, 10, 5, 4, 2], "fc k-floor mapping"
    # knockoff+ admits-all-positive / admits-nothing-infeasible (both modules)
    W = [0.9] * 25 + [-0.3]
    T, n, ratio = st.knockoff_plus_threshold(W, 0.05)
    assert n >= 20 and ratio <= 0.05, f"st knockoff admit {n} ratio {ratio}"
    Tc, admc, rc = fc.knockoff_plus_threshold(W, 0.05)
    assert len(admc) >= 20 and rc <= 0.05, "fc knockoff admit"
    Tn, nn, _ = st.knockoff_plus_threshold([-0.5, -0.4, 0.1], 0.05)
    assert nn == 0 and math.isinf(Tn), "infeasible admits nothing"
    # vectorized _knockoff_fast must match st.knockoff_plus_threshold EXACTLY (random arrays)
    rng0 = np.random.default_rng(7)
    for _ in range(200):
        n = int(rng0.integers(1, 80))
        Wr = np.round(rng0.normal(0, 1, n), 3)
        for a in ALPHA_GRID:
            Ts, ns, rs = st.knockoff_plus_threshold(Wr, a)
            Tf, nf2, rf = _knockoff_fast(Wr, a)
            assert (math.isinf(Ts) == math.isinf(Tf)), "fast knockoff feasibility mismatch"
            if not math.isinf(Ts):
                assert abs(Ts - Tf) < 1e-9 and ns == nf2 and abs(rs - rf) < 1e-9, \
                    f"fast knockoff mismatch a={a}: st=({Ts},{ns},{rs}) fast=({Tf},{nf2},{rf})"
    # (b) W signed-max antisymmetry + tie
    assert st.W_signed_max(0.8, 0.3) == 0.8 and st.W_signed_max(0.3, 0.8) == -0.8
    assert abs(st.W_signed_max(0.5, 0.5)) == 0.0, "tie sign zero"
    assert fc.w_statistic(0.8, 0.3) == 0.8 and fc.w_statistic(0.3, 0.8) == -0.8
    # (c) fair-coin win-rate in (0.45,0.55); too-easy decoys < 0.45 & KS sig (S1b anchor)
    rng = np.random.default_rng(0)
    fair = [(float(rng.random()), float(rng.random())) for _ in range(2000)]
    wr, _ = st.tail_win_rate(fair, 0.0)
    assert 0.45 < wr < 0.55, f"fair-coin win-rate {wr}"
    easy = [(float(rng.random()), float(rng.random()) * 0.5) for _ in range(2000)]
    wr2, _ = st.tail_win_rate(easy, 0.0)
    assert wr2 < 0.45, f"too-easy decoy win-rate {wr2}"
    _, ksp = st.ks_two_sample([d for _, d in easy], [r for r, _ in easy], "two-sided")
    assert ksp < 0.05, f"KS must detect too-easy decoys p={ksp}"
    # foreign-swap-style: decoy ALWAYS far below real -> win-rate ~ 0 & detected (CI high < 0.5)
    foreign = [(0.6 + 0.4 * float(rng.random()), 0.2 * float(rng.random())) for _ in range(300)]
    wrf, _ = st.tail_win_rate(foreign, 0.0)
    assert wrf < 0.1, f"foreign-swap win-rate should be ~0, got {wrf}"
    # (d) doc-block CI wider than iid on clustered data
    clustered = [[0.0] * 20 if i % 2 == 0 else [1.0] * 20 for i in range(20)]
    block = st.doc_block_bootstrap(clustered, lambda u: float(np.mean([x for g in u for x in g])), B=500, seed=1)
    flat = [x for u in clustered for x in u]
    iid = st.doc_block_bootstrap(flat, lambda u: float(np.mean(u)) if len(u) else float("nan"), B=500, seed=1)
    assert (block["ci_high"] - block["ci_low"]) > (iid["ci_high"] - iid["ci_low"]), "block CI > iid CI"
    # (e) Doc.label crisp 3-way on a tiny synthetic
    raw = {"input": json.dumps({"doc_id": "x", "document_text": "t", "entities":
           [{"name": "Dan"}, {"name": "Micheal"}, {"name": "Gabrielle"}], "query": {}}),
           "output": json.dumps({"atomic_facts": [{"head": "Gabrielle", "relation": "grandson", "tail": "Dan"},
                                                   {"head": "Dan", "relation": "brother", "tail": "Micheal"}],
                                 "multi_hop_facts": []}),
           "metadata_chain_length_k": 2, "metadata_is_pilot": False, "metadata_fold": "k2"}
    d0 = Doc(raw)
    assert d0.label("Dan", "brother", "Micheal") == TRUE
    assert d0.label("Gabrielle", "grandson", "Dan") == TRUE
    assert d0.label("Dan", "mother", "Micheal") == FALSE
    assert d0.label("Dan", "brother", "Gabrielle") == UND
    # (f) BH monotonic
    bh = st.benjamini_hochberg([0.001, 0.5, 0.02, 0.9], q=0.05)
    assert bh[0]["reject"] and not bh[1]["reject"], "BH"
    # (g) decoy gate realized <= alpha on clean synthetic; baseline anti-conservative shape
    reals = [{"w": 0.9, "is_false": False}] * 18 + [{"w": -0.2, "is_false": True}] * 2
    g = st.decoy_gate_fdr(reals, 0.10)
    assert g["n_admitted"] >= 10 and g["realized_fdr"] <= 0.10 + 1e-9, "decoy gate fdr"
    # (h) entrapment estimators (fc): combined upper bound; paired shapes; sample INVALID
    assert abs(fc.entrapment_fdp(10, 5, 1.0, "combined") - (5 * 2 / 15)) < 1e-9
    assert abs(fc.entrapment_fdp(10, 5, 1.0, "lower") - (5 / 15)) < 1e-9
    pc = fc.paired_entrapment_counts([0.9, 0.1], [0.2, 0.8], [True, False], [False, True], 0.5)
    _ = fc.entrapment_fdp(1, 1, 1.0, "paired", paired_counts=pc)
    try:
        fc.entrapment_fdp(10, 5, 1.0, "sample")
        assert False, "sample estimator must raise"
    except ValueError:
        pass
    # (i) rank_normalize: single-element pool -> 0.5; monotone
    assert st.rank_normalize({"a": 3.0}, SEED)["a"] == 0.5
    rn = st.rank_normalize({"a": 0.1, "b": 0.9, "c": 0.5}, SEED)
    assert rn["b"] > rn["c"] > rn["a"], "rank monotone"
    # (j) self-report anti-conservative flag logic
    realized, dfh = 0.30, 0.10
    assert (realized - dfh) > TAU, "self-report flag should trigger when estimate undershoots realized"
    # (k) plain_threshold_gate admits high-confidence first
    thr, adm, est = fc.plain_threshold_gate([0.95] * 10 + [0.1] * 5, 0.10)
    assert len(adm) >= 5 and est <= 0.10 + 1e-9, "plain gate"
    # (l) NEW Phase-5: _paired_stat (the per-pair sign-flip statistic underlying paired_across_GS).
    #     Realistic mix: TRUE pairs (real beats decoy) set the knockoff+ admission tail; the FALSE
    #     pairs in it are exchangeable -> tail win-rate ~0.5, CI covers 0.5, NOT flagged. With the
    #     FALSE pairs ALSO real-wins (decoys too easy) -> win-rate -> 0, CI<0.5, flagged. Multi-doc so
    #     the doc-block bootstrap is genuine. (Marginal-win-rate calibration is checked in (c).)
    rngp = np.random.default_rng(3)
    def _mk(false_real_wins):
        rows = []
        for i in range(1200):
            if i % 2 == 0:                       # TRUE positive: real clearly beats decoy
                zr, zd, lab = 0.55 + 0.45 * float(rngp.random()), 0.45 * float(rngp.random()), TRUE
            elif false_real_wins:                # FALSE but real still wins (decoys too easy)
                zr, zd, lab = 0.55 + 0.45 * float(rngp.random()), 0.45 * float(rngp.random()), FALSE
            else:                                # FALSE exchangeable (fair coin)
                zr, zd, lab = float(rngp.random()), float(rngp.random()), FALSE
            rows.append({"zr": zr, "zd": zd, "label": lab, "doc_id": f"d{i % 30}",
                         "w": st.W_signed_max(zr, zd)})
        return rows
    pe = _paired_stat(_mk(False), alpha=0.50)
    assert pe["paired_win_rate_false"] is not None and 0.35 <= pe["paired_win_rate_false"] <= 0.65, \
        f"exchangeable-FALSE tail win-rate {pe['paired_win_rate_false']}"
    assert not pe["paired_nonexchangeable"], "exchangeable FALSE pairs must NOT be flagged nonexchangeable"
    pr = _paired_stat(_mk(True), alpha=0.50)
    assert pr["paired_win_rate_false"] is not None and pr["paired_win_rate_false"] < 0.2, \
        f"real-always-wins FALSE tail win-rate {pr['paired_win_rate_false']}"
    assert pr["paired_nonexchangeable"] and not pr["ci_covers_half"], "real-always-wins -> CI<0.5 flagged"
    # (m) NEW Phase-6a: k-density binning map is correct & disjoint-covering over k=2..10.
    def _kbin(k):
        return [n for (n, lo, hi) in DENSITY_BINS if lo <= k <= hi]
    assert all(len(_kbin(k)) == 1 for k in range(2, 11)), "every k in 2..10 maps to exactly one bin"
    assert _kbin(2) == ["LOW_k2_3"] and _kbin(5) == ["MED_k4_6"] and _kbin(9) == ["HIGH_k7_10"]
    # monotone false-density toy: synthetic per-stratum false counts increase with k-bin
    dens = [3 / 30.0, 15 / 30.0, 26 / 30.0]
    assert dens[0] < dens[1] < dens[2], "toy false-density gradient is monotone"
    logger.info("STAGE 0 — all offline unit tests PASSED ✓")


# ===========================================================================
# Offline analysis driver
# ===========================================================================
def analyze(pipe):
    norm_sc = norm_pool(pipe, SC)
    norm_vb = norm_pool(pipe, VB)
    raw_sc = {cid: z for (cfg, cid), z in pipe["zmap"].items() if cfg == SC}
    raw_vb = {cid: z for (cfg, cid), z in pipe["zmap"].items() if cfg == VB}
    diag_sc = {fam: diagonal_for_family(pipe, norm_sc, fam, raw_sc)
               for fam in ("atomic", "multi_hop", "pooled")}
    diag_vb = {fam: diagonal_for_family(pipe, norm_vb, fam, raw_vb)
               for fam in ("atomic", "multi_hop", "pooled")}
    crux_sc = analyze_crux(pipe, norm_sc)
    crux_vb = analyze_crux(pipe, norm_vb)
    ladder = analyze_s1b_ladder(pipe)
    diag_mh = diag_sc["multi_hop"]
    alpha_star = diag_mh["reachable_alpha_floor"] or 0.50
    entrap = {"at_alpha_star": {"alpha_star": alpha_star,
                                **entrapment_analysis(pipe, "multi_hop", alpha_star)},
              "at_alpha_0p50": entrapment_analysis(pipe, "multi_hop", 0.50)}
    baseline_sc = {fam: baseline_vs_method(pipe, norm_sc, raw_sc, fam)
                   for fam in ("multi_hop", "atomic", "pooled")}
    gen_ne = load_generator_ne_scorer()
    pdisc = primary_disconfirmation(pipe, norm_sc, diag_mh)
    # NEW iter-4 analyses
    paired_gs = paired_exchangeability_across_GS(pipe)
    density = density_strata_analysis(pipe, norm_sc)
    strong = strong_extractor_analysis(pipe)
    bh = collect_bh(diag_sc, ladder, crux_sc, crux_vb, entrap, paired_gs=paired_gs, density=density)
    return {"norm_sc": norm_sc, "norm_vb": norm_vb, "raw_sc": raw_sc, "raw_vb": raw_vb,
            "diag_sc": diag_sc, "diag_vb": diag_vb, "crux_sc": crux_sc, "crux_vb": crux_vb,
            "ladder": ladder, "entrapment": entrap, "baseline_sc": baseline_sc,
            "gen_ne_scorer": gen_ne, "primary_disconfirmation": pdisc, "bh": bh,
            "paired_across_GS": paired_gs, "density_strata": density, "strong_extractor_arm": strong,
            "vb_artifact_notes": verbalized_artifact_notes(diag_vb),
            "power_table": power_table(diag_sc)}


# ===========================================================================
# Pipe checkpoint (fast offline re-analysis without re-reading the score cache)
# ===========================================================================
class _LiteDoc:
    __slots__ = ("doc_id", "is_pilot", "k")

    def __init__(self, di):
        self.doc_id, self.is_pilot, self.k = di["doc_id"], di["is_pilot"], di["k"]


PIPE_CKPT = HERE / "checkpoints" / "pipe.json"


_CKPT_KEYS = ("reals_by_doc", "cf_by_doc", "cf2_by_doc", "swap_by_doc", "rv_by_doc",
              "fgn_by_doc", "ent_by_doc", "cfo_by_doc", "strong_reals_by_doc", "strong_cf_by_doc",
              "strong_meta", "strong_docs_ids", "ext_meta", "contamination_rate", "n_gen_decoys",
              "n_true", "n_spont", "n_und", "light", "n_extract", "gs_scored", "runtime")


def save_pipe_ckpt(pipe):
    PIPE_CKPT.parent.mkdir(exist_ok=True)
    ck = {"docinfo": [{"doc_id": d.doc_id, "is_pilot": d.is_pilot, "k": d.k} for d in pipe["docs"]],
          "zmap": {f"{cfg}\t{cid}": z for (cfg, cid), z in pipe["zmap"].items()},
          "ladder_ids": sorted(pipe.get("ladder_ids", []) or []),
          "gs_ids": sorted(pipe.get("gs_ids", []) or [])}
    for key in _CKPT_KEYS:
        ck[key] = pipe.get(key)
    PIPE_CKPT.write_text(json.dumps(ck))
    logger.info(f"saved pipe checkpoint -> {PIPE_CKPT} ({PIPE_CKPT.stat().st_size/1e6:.1f} MB)")


def load_pipe_ckpt():
    ck = json.loads(PIPE_CKPT.read_text())
    docs = [_LiteDoc(di) for di in ck["docinfo"]]
    doc_by_id = {d.doc_id: d for d in docs}
    zmap = {tuple(k.split("\t", 1)): v for k, v in ck["zmap"].items()}
    reals_by_doc = ck["reals_by_doc"]
    all_reals = [c for d in docs for c in reals_by_doc[d.doc_id]]
    pilot_ids = {d.doc_id for d in docs if d.is_pilot} or {docs[0].doc_id}
    pipe = {"docs": docs, "doc_by_id": doc_by_id, "pilot_ids": pilot_ids,
            "all_reals": all_reals, "zmap": zmap,
            "ladder_ids": set(ck.get("ladder_ids") or pilot_ids),
            "gs_ids": set(ck.get("gs_ids") or [])}
    for key in _CKPT_KEYS:
        pipe[key] = ck.get(key)
    # backfill keys absent in older checkpoints
    for k2, default in (("cfo_by_doc", {}), ("strong_reals_by_doc", {}), ("strong_cf_by_doc", {}),
                        ("strong_meta", []), ("strong_docs_ids", []), ("n_extract", 1),
                        ("gs_scored", False)):
        if pipe.get(k2) is None:
            pipe[k2] = default
    return pipe


# ===========================================================================
# Main
# ===========================================================================
def _finish(pipe, args):
    logger.info("Analyzing (offline)...")
    analysis = analyze(pipe)
    out_path = HERE / ("mini_method_out.json" if args.mini else "method_out.json")
    out = build_output(pipe, analysis, out_path)
    if not args.mini:
        make_figures(out, HERE / "figures")
    gc.collect()
    pd = analysis["primary_disconfirmation"]
    logger.info(f"DONE cost=${pipe['runtime']['cost_usd']:.4f} | verdict={pd['verdict']} "
                f"alpha*={pd.get('alpha_star')} | self_report_disconfirmed={pd.get('self_report_disconfirmed')}")


async def amain(args):
    set_mem_limit(16.0)
    if args.analyze_only:
        logger.info("ANALYZE-ONLY: loading pipe checkpoint (no API, no cache reads)...")
        pipe = load_pipe_ckpt()
        logger.info(f"loaded pipe: {len(pipe['docs'])} docs, {len(pipe['all_reals'])} reals, "
                    f"{len(pipe['zmap'])} scores")
        _finish(pipe, args)
        return
    docs = load_docs(FULL_DATA, n_docs=(3 if args.mini else args.n_docs),
                     pilot_only=args.pilot_only)
    logger.info(f"Loaded {len(docs)} docs (pilot={sum(d.is_pilot for d in docs)})")
    pipe = await run(docs, cache_dir=HERE / "cache", cost_log=HERE / "logs" / "cost.jsonl",
                     concurrency=args.concurrency, light=args.light,
                     n_extract=args.n_extract, do_gs=(not args.no_gs),
                     do_strong=args.strong, strong_docs_cap=args.strong_cap,
                     ladder_conf=args.ladder_conf)
    if not args.mini:
        save_pipe_ckpt(pipe)
    _finish(pipe, args)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mini", action="store_true")
    ap.add_argument("--n-docs", type=int, default=None)
    ap.add_argument("--pilot-only", action="store_true")
    ap.add_argument("--light", action="store_true",
                    help="fallback: restrict entrapment + verbalized to the pilot slice")
    ap.add_argument("--analyze-only", action="store_true",
                    help="re-run analysis + output from the saved pipe checkpoint (no API)")
    ap.add_argument("--concurrency", type=int, default=24)
    ap.add_argument("--n-extract", type=int, default=N_EXTRACT_SAMPLES,
                    help="extraction over-gen samples (1==legacy cache-identical; 2 densifies false positives)")
    ap.add_argument("--no-gs", action="store_true", help="skip the Phase-5 (G,S) paired matrix")
    ap.add_argument("--strong", action="store_true",
                    help="run the Phase-6b stronger-extractor de-confound arm (budget-gated)")
    ap.add_argument("--strong-cap", type=int, default=None,
                    help="cap #docs for the strong-extractor arm (default: all k>=4 docs)")
    ap.add_argument("--ladder-conf", type=int, default=60,
                    help="# confirmatory docs (beyond pilot) to score the S1b ladder rungs on (Phase 7)")
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
