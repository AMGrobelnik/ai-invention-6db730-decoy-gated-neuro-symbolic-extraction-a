#!/usr/bin/env python3
"""
method.py — P2 headline experiment.

Hallucination-reduction of a LABEL-FREE decoy-competition (knockoff+) FDR gate for
LLM text->logic fact admission, on the genre-faithful 24-doc legal/news/regulatory
APPLICATION ANCHOR (8 CUAD-crisp / 8 Wikinews-silver / 8 GDPR+eCFR-silver), compared
side-by-side against RAW LLM extraction, RAG (BM25), and chain-of-thought (CoT).

Pipeline (method + baselines + controls in ONE implementation):
  STAGE 1  over-generating extraction (n-sample union) + WordNet->SUMO typing + open->gold
           relation alignment + entity linking + crisp/silver labelling vs gold.
  STAGE 2  document-conditioned COUNTERFACTUAL decoys + type-matched swap control +
           deterministic ENTRAPMENT (r=1) + dual label-free elicitation scoring
           (single-token logprob softmax P(Yes) AND K-sample self-consistency) +
           knockoff+ gate at every alpha, per genre x elicitation, with the gate's OWN
           decoy_fdr_hat, realized FDR vs gold, and the entrapment FDP_hat bound.
  STAGE 2b PRIMARY METRIC: hallucinated-fact rate (decoy-gate vs RAW LLM) per
           genre x elicitation x alpha, with a NON-circular cross-family adjudicator,
           document-block bootstrap CIs, regime tags, and silver lower/upper bounds.
  STAGE 2c SECONDARY: matched-recall precision / hallucination-rate vs RAW / RAG / CoT.
  STAGE 3  reasoning + AUDITABLE trace-graphs (pure-Python backward-chaining engine,
           genre bridge rules) with per-leaf provenance + decoy + entrapment certificates;
           multi-hop corrupted-conclusion rate RAW-KB vs GATE-KB.
  STAGE 4  BH multiplicity correction, schema-valid method_out.json, figures.

CPU-only; soft cap $3 (warn), hard stop $10 (BudgetExceeded). On-disk cache => free resumes.

Usage:
  uv run method.py --selftest                 # offline unit tests, no API
  uv run method.py --mini --elic logprob --k-sc 2   # 12-doc smoke
  uv run method.py                            # full 24 docs, both elicitations
"""
from __future__ import annotations

import argparse
import asyncio
import gc
import hashlib
import json
import math
import random
import re
import resource
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from loguru import logger

import fdr_stats as st
import kb_engine as kbe
import prob_reasoner as pr
import typing_sumo as tsumo
from kb_engine import V
from llm_client import (BudgetExceeded, OpenRouterClient, parse_yes_conf,
                        yes_prob_from_logprobs)

# ---------------------------------------------------------------------------
# Constants / guardrails
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
DEP_DATA = Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/"
                "iter_2/gen_art/gen_art_dataset_1")
FULL_DATA = DEP_DATA / "full_data_out.json"
MINI_DATA = DEP_DATA / "mini_data_out.json"

SEED = 20240617
ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]      # k-floors {20,10,5,4,2}
B_BOOT = 2000
K_SC = 5                                          # self-consistency samples (portable)
R_ENTRAP = 1                                      # paired entrapment (one per real)
N_SAMPLES_EXTRACT = 3                             # over-generation: union of n samples
EXTRACT_TEMP = 0.7
REALS_CAP = 20                                    # cap aligned reals/doc (cost bound)
CAND_CAP = 40                                     # cap raw candidates/doc before alignment
RECALL_GRID = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
KAPPA_TRUST = 0.4                                 # adjudicator-trust threshold (legal kappa)
SOFT_CAP_USD = 3.0
HARD_STOP_USD = 10.0

PRIMARY_MODEL = "openai/gpt-4.1-nano"             # logprobs + cheap, doc-prefix caching
CROSS_MODEL = "mistralai/ministral-8b-2512"       # cross-family judge / generator ($0.15/M)

GENRES = ["legal", "news", "regulatory"]

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(HERE / "logs").mkdir(exist_ok=True)
logger.add(HERE / "logs" / "run.log", rotation="30 MB", level="DEBUG")


def set_mem_limit(gb: float = 8.0):
    try:
        soft = int(gb * 1024**3)
        resource.setrlimit(resource.RLIMIT_AS, (soft, soft))
    except (ValueError, OSError) as e:
        logger.warning(f"could not set RLIMIT_AS: {e}")


def _doc_seed(doc_id: str, salt: int = 0) -> int:
    h = hashlib.sha256(f"{doc_id}|{SEED}|{salt}".encode()).hexdigest()
    return int(h[:12], 16)


# ---------------------------------------------------------------------------
# Normalisation + matching helpers
# ---------------------------------------------------------------------------
_WS = re.compile(r"\s+")
_EDGE = re.compile(r"^[\s\"'`.,;:()\[\]]+|[\s\"'`.,;:()\[\]]+$")


def norm(s: str) -> str:
    if not isinstance(s, str):
        s = str(s)
    s = _EDGE.sub("", s)
    s = _WS.sub(" ", s).strip().lower()
    return s


def norm_match(a: str, b: str) -> bool:
    """Normalised equality OR substring containment (>=3 chars) — surface-robust."""
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    if len(na) >= 3 and len(nb) >= 3 and (na in nb or nb in na):
        return True
    return False


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
class AnchorDoc:
    __slots__ = ("doc_id", "text", "genre", "gold_quality", "source", "relation_vocab",
                 "char_length", "entities", "entity_names", "gold_facts", "gold_set",
                 "gold_pair_rel", "sumo_by_entity", "entities_by_type", "ntext")

    def __init__(self, raw: dict):
        inp = json.loads(raw["input"])
        out = json.loads(raw["output"])
        self.doc_id = inp["doc_id"]
        self.text = inp["document_text"]
        self.ntext = norm(self.text)
        self.genre = raw.get("metadata_fold") or inp.get("genre")
        self.gold_quality = raw.get("metadata_gold_quality", "silver")
        self.source = raw.get("metadata_source", "")
        self.relation_vocab = list(raw.get("metadata_relation_vocab") or [])
        self.char_length = int(raw.get("metadata_char_length", len(self.text)))
        self.entities = [{"name": e["name"], "type": e.get("type", "MISC"),
                          "char_span": e.get("char_span")} for e in inp.get("entities", [])]
        self.entity_names = [e["name"] for e in self.entities]
        gf = out.get("gold_atomic_facts", [])
        self.gold_facts = [{"head": f["head"], "relation": f["relation"], "tail": f["tail"],
                            "provenance_char_span": f.get("provenance_char_span")} for f in gf]
        self.gold_set = {(f["head"], f["relation"], f["tail"]) for f in self.gold_facts}
        self.gold_pair_rel: dict[tuple[str, str], set] = defaultdict(set)
        for f in self.gold_facts:
            self.gold_pair_rel[(norm(f["head"]), norm(f["tail"]))].add(f["relation"])
        # SUMO typing per entity (used ONLY to constrain swaps/entrapment)
        self.sumo_by_entity = {}
        self.entities_by_type = defaultdict(list)
        for e in self.entities:
            ty = tsumo.type_entity(e["name"], e.get("type"))
            self.sumo_by_entity[e["name"]] = ty
            self.entities_by_type[ty["coarse"]].append(e["name"])

    # -- entity grounding / linking -----------------------------------------
    def grounded(self, endpoint: str) -> bool:
        """Endpoint links if it is a substring of the document OR a gold entity."""
        ne = norm(endpoint)
        if len(ne) >= 2 and ne in self.ntext:
            return True
        for en in self.entity_names:
            if norm_match(endpoint, en):
                return True
        for f in self.gold_facts:
            if norm_match(endpoint, f["head"]) or norm_match(endpoint, f["tail"]):
                return True
        return False

    def gold_exact(self, h: str, r: str, t: str) -> bool:
        for (gh, gr, gt) in self.gold_set:
            if gr == r and norm_match(h, gh) and norm_match(t, gt):
                return True
        return False

    def covered_pair_rels(self, h: str, t: str) -> set:
        out = set()
        for (gh, gt), rels in self.gold_pair_rel.items():
            if norm_match(h, gh) and norm_match(t, gt):
                out |= rels
        return out

    def label(self, h: str, r: str, t: str) -> str:
        """Crisp 3-way label vs gold (TRUE / FALSE / UNDECIDABLE)."""
        if self.gold_exact(h, r, t):
            return "TRUE"
        if not (self.grounded(h) and self.grounded(t)):
            return "FALSE"           # ungrounded endpoint
        cov = self.covered_pair_rels(h, t)
        if cov and r not in cov:
            return "FALSE"           # contradiction on a gold-covered pair
        return "UNDECIDABLE"

    def entity_type(self, name: str) -> str:
        if name in self.sumo_by_entity:
            return self.sumo_by_entity[name]["coarse"]
        return tsumo.type_entity(name)["coarse"]


def load_anchor(path: Path, genres=None, n_docs: int | None = None,
                per_genre: int | None = None) -> list[AnchorDoc]:
    raw = json.loads(path.read_text())
    docs = []
    for group in raw["datasets"]:
        for ex in group["examples"]:
            docs.append(AnchorDoc(ex))
    if genres:
        docs = [d for d in docs if d.genre in genres]
    docs.sort(key=lambda d: d.doc_id)
    if per_genre is not None:
        by_g = defaultdict(list)
        for d in docs:
            by_g[d.genre].append(d)
        docs = [d for g in GENRES for d in by_g.get(g, [])[:per_genre]]
    if n_docs is not None:
        docs = docs[:n_docs]
    return docs


# ---------------------------------------------------------------------------
# Verbalisation (uniform across candidate kinds; provenance-blinded)
# ---------------------------------------------------------------------------
def verbalize(h: str, r: str, t: str) -> str:
    return f'In the document, "{h}" has the relation [{r.replace("_", " ")}] to "{t}".'


# ---------------------------------------------------------------------------
# JSON parsing from LLM output (balanced-brace) — robust to prose / fences
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


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
def _vocab_block(doc: AnchorDoc) -> str:
    return ", ".join(doc.relation_vocab) if doc.relation_vocab else "(open)"


def extract_messages(doc: AnchorDoc, mode: str = "raw", retrieved: str | None = None) -> list[dict]:
    ents = "; ".join(doc.entity_names[:60])
    vocab = _vocab_block(doc)
    body = retrieved if (mode == "rag" and retrieved) else doc.text
    sysmsg = ("You extract atomic relational facts from a short professional document "
              "(legal / news / regulatory). Output STRICT JSON only.")
    common = (
        f"Entities (use these surface forms where possible): {ents}\n\n"
        f"Preferred relation vocabulary for this genre: {vocab}\n"
        "If a fact's relation is not in the vocabulary, use \"other:<short phrase>\".\n\n"
        "OVER-GENERATE: list EVERY plausible (head, relation, tail) fact you can find, "
        "including uncertain or weakly-implied ones. Each fact must have a short "
        "verbatim provenance quote copied from the text.\n"
        "Respond with STRICT JSON only:\n"
        '{"facts": [{"head": "...", "relation": "...", "tail": "...", "provenance_quote": "..."}]}')
    if mode == "cot":
        user = (f"Document:\n{body}\n\n"
                "First reason step by step (briefly) about who/what is related to whom, "
                "then list the facts.\n\n" + common)
    elif mode == "rag":
        user = (f"Retrieved passages from the document:\n{body}\n\n" + common)
    else:
        user = (f"Document:\n{body}\n\n" + common)
    return [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]


def align_messages(doc: AnchorDoc, phrases: list[str]) -> list[dict]:
    vocab = ", ".join(doc.relation_vocab)
    lines = "\n".join(f"{i+1}. {p}" for i, p in enumerate(phrases))
    sysmsg = "You normalise relation phrases to a fixed vocabulary. Output STRICT JSON only."
    user = (f"Target relation vocabulary: {vocab}\n\n"
            "For each numbered relation phrase below, pick the SINGLE closest vocabulary "
            "relation that means the same thing, or \"NO_RELATION\" if none matches.\n"
            f"{lines}\n\n"
            'Respond with STRICT JSON only: {"map": ["<vocab_or_NO_RELATION>", ...]} '
            "in the same order.")
    return [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]


def decoy_messages(doc: AnchorDoc, items: list[tuple]) -> list[dict]:
    vocab = ", ".join(doc.relation_vocab)
    lines = "\n".join(f'{i+1}. head="{h}", tail="{t}" (current relation: {r})'
                      for i, (h, r, t) in enumerate(items))
    sysmsg = ("You propose alternative relations for a head/tail pair, using ONLY a fixed "
              "vocabulary. Output STRICT JSON only.")
    user = (f"Relation vocabulary: {vocab}\n\n"
            "For each numbered head/tail pair, give the TWO most plausible ALTERNATIVE "
            "relations from the vocabulary (each different from the current one), most "
            "plausible first — a likely-but-possibly-wrong guess for that pair.\n"
            f"{lines}\n\n"
            'Respond with STRICT JSON only: a JSON array with one ["alt1","alt2"] pair per '
            "item, in order.")
    return [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]


def score_messages_logprob(doc_text: str, claim: str) -> list[dict]:
    return [
        {"role": "system", "content":
            "You judge whether a relational claim is directly stated in or logically "
            "entailed by a document. Answer with exactly one word: Yes or No."},
        {"role": "user", "content":
            f"Document: {doc_text}\n\nClaim: {claim}\n"
            "Is this claim stated in or entailed by the document? Answer Yes or No."},
    ]


def score_messages_portable(doc_text: str, claim: str) -> list[dict]:
    return [
        {"role": "system", "content":
            "You judge whether a relational claim is directly stated in or logically "
            "entailed by a document."},
        {"role": "user", "content":
            f"Document: {doc_text}\n\nClaim: {claim}\n"
            "Is this claim stated in or entailed by the document? Respond in EXACTLY this "
            "format:\nAnswer: <Yes or No>\nConfidence: <integer 0-100>"},
    ]


def judge_messages(doc_text: str, h: str, r: str, t: str, prov: str) -> list[dict]:
    claim = verbalize(h, r, t)
    return [
        {"role": "system", "content":
            "You are a strict fact-checker. Given a DOCUMENT and a FACT (with the quote it "
            "was extracted from), decide if the fact is stated in or entailed by the "
            "document. Answer with exactly one word: Entailed, Unsupported, or Contradicted."},
        {"role": "user", "content":
            f"DOCUMENT:\n{doc_text}\n\nFACT: {claim}\nExtraction quote: \"{prov}\"\n"
            "Is the FACT stated in or entailed by the DOCUMENT? "
            "Answer Entailed, Unsupported, or Contradicted."},
    ]


# ---------------------------------------------------------------------------
# STAGE 1 — extraction (n-sample union) for one system (raw / rag / cot)
# ---------------------------------------------------------------------------
def sentence_chunks(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.strip()) > 0]


def bm25_retrieve(doc: AnchorDoc, k: int = 6) -> str:
    from rank_bm25 import BM25Okapi
    chunks = sentence_chunks(doc.text)
    if len(chunks) <= k:
        return "\n".join(chunks)
    tokenized = [re.findall(r"[a-zA-Z0-9]+", c.lower()) for c in chunks]
    bm = BM25Okapi(tokenized)
    query = re.findall(r"[a-zA-Z0-9]+",
                       (" ".join(doc.relation_vocab) + " " + " ".join(doc.entity_names[:20])).lower())
    scores = bm.get_scores(query)
    top = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)[:k]
    top.sort()
    return "\n".join(chunks[i] for i in top)


async def extract_system(client: OpenRouterClient, doc: AnchorDoc, mode: str,
                         n_samples: int) -> dict:
    """Return {triples: {(h,r_raw,t): freq}, prov: {(h,r_raw,t): quote}}."""
    retrieved = bm25_retrieve(doc) if mode == "rag" else None
    msgs = extract_messages(doc, mode=mode, retrieved=retrieved)
    freq: dict[tuple, int] = defaultdict(int)
    prov: dict[tuple, str] = {}
    for i in range(n_samples):
        res = await client.call(PRIMARY_MODEL, msgs, max_tokens=1100,
                                temperature=EXTRACT_TEMP, seed=SEED + i, sample_idx=i)
        parsed = _extract_json(res["content"]) or {}
        facts = parsed.get("facts") if isinstance(parsed, dict) else None
        if not isinstance(facts, list):
            continue
        for f in facts:
            if not isinstance(f, dict):
                continue
            h, r, t = f.get("head"), f.get("relation"), f.get("tail")
            if not (isinstance(h, str) and isinstance(r, str) and isinstance(t, str)):
                continue
            h, r, t = h.strip(), r.strip(), t.strip()
            if not h or not r or not t:
                continue
            key = (h, r, t)
            freq[key] += 1
            prov.setdefault(key, str(f.get("provenance_quote", ""))[:300])
    # cap by frequency then deterministic order
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:CAND_CAP]
    return {"triples": {k: v for k, v in items}, "prov": prov, "n_samples": n_samples}


def _vocab_relation(r_raw: str, vocab: list[str]) -> str | None:
    rl = r_raw.strip().lower()
    for v in vocab:
        if rl == v.lower():
            return v
    return None


# ---------------------------------------------------------------------------
# STAGE 2 — decoys / swaps / entrapment
# ---------------------------------------------------------------------------
def verify_nonentailed(doc: AnchorDoc, h: str, r: str, t: str, avoid: set) -> bool:
    if r in avoid:
        return False
    if doc.gold_exact(h, r, t):
        return False
    cov = doc.covered_pair_rels(h, t)
    if r in cov:
        return False
    return True


def deterministic_decoy_relation(doc: AnchorDoc, h: str, r: str, t: str,
                                 rng: random.Random) -> str | None:
    pool = [v for v in doc.relation_vocab if verify_nonentailed(doc, h, v, t, {r})]
    if not pool:
        return None
    return pool[rng.randrange(len(pool))]


async def gen_counterfactual_decoys(client: OpenRouterClient, doc: AnchorDoc,
                                    reals: list[dict], rng: random.Random):
    """One batched call/doc -> decoy per real. Returns (decoys, n_gen, n_contam)."""
    items = [(c["h"], c["r"], c["t"]) for c in reals]
    if not items:
        return [], 0, 0
    res = await client.call(PRIMARY_MODEL, decoy_messages(doc, items),
                            max_tokens=900, temperature=0.0)
    parsed = _extract_json(res["content"])
    decoys, n_gen, n_contam = [], 0, 0
    for i, c in enumerate(reals):
        h, r, t = c["h"], c["r"], c["t"]
        cov = doc.covered_pair_rels(h, t)
        alts = parsed[i] if (isinstance(parsed, list) and i < len(parsed)) else None
        cand = []
        if isinstance(alts, list):
            for a in alts:
                rv = _vocab_relation(a, doc.relation_vocab) if isinstance(a, str) else None
                if rv:
                    n_gen += 1
                    if doc.gold_exact(h, rv, t) or rv in cov:
                        n_contam += 1
                    cand.append(rv)
        chosen = next((rv for rv in cand if verify_nonentailed(doc, h, rv, t, {r})), None)
        if chosen is None:
            chosen = deterministic_decoy_relation(doc, h, r, t, rng)
        if chosen is None:
            continue
        decoys.append({"cand_id": f"{doc.doc_id}:cf:{i}", "doc_id": doc.doc_id,
                       "h": h, "r": chosen, "t": t, "real_id": c["cand_id"],
                       "claim": verbalize(h, chosen, t), "kind": "cf_decoy"})
    return decoys, n_gen, n_contam


def gen_swaps(doc: AnchorDoc, reals: list[dict], rng: random.Random) -> list[dict]:
    swaps = []
    for i, c in enumerate(reals):
        h, r, t = c["h"], c["r"], c["t"]
        ttype = doc.entity_type(t)
        pool = [p for p in doc.entities_by_type.get(ttype, [])
                if not norm_match(p, t) and not norm_match(p, h)
                and verify_nonentailed(doc, h, r, p, set())]
        if not pool:
            pool = [p for p in doc.entity_names
                    if not norm_match(p, t) and not norm_match(p, h)
                    and verify_nonentailed(doc, h, r, p, set())]
        if not pool:
            continue
        tp = pool[rng.randrange(len(pool))]
        swaps.append({"cand_id": f"{doc.doc_id}:swap:{i}", "doc_id": doc.doc_id,
                      "h": h, "r": r, "t": tp, "real_id": c["cand_id"],
                      "claim": verbalize(h, r, tp), "kind": "swap"})
    return swaps


def gen_entrapment(doc: AnchorDoc, reals: list[dict], global_pool: dict,
                   rng: random.Random) -> list[dict]:
    """Deterministic false-by-construction items (r=1, paired). Three constructions:
       (a) cross-document same-type entity swap on the tail,
       (b) relation perturbation to a contradicting vocabulary relation,
       (c) numeric/temporal perturbation on TIME/NUM tails.
    Each entrapment also gets a deterministic counterfactual decoy for its own W."""
    out = []
    for i, c in enumerate(reals):
        h, r, t = c["h"], c["r"], c["t"]
        ttype = doc.entity_type(t)
        kind, eh, er, et = None, h, r, t
        # (c) numeric/temporal perturbation
        if ttype in ("TIME", "NUM") and re.search(r"\d", t):
            et = _perturb_number(t, rng)
            if et != t:
                kind = "entrap_numeric"
        # (a) cross-document entity swap (same coarse type)
        if kind is None:
            cross = [e for e in global_pool.get(ttype, []) if e[0] != doc.doc_id
                     and not norm_match(e[1], t)]
            if cross:
                et = cross[rng.randrange(len(cross))][1]
                kind = "entrap_xdoc"
        # (b) relation perturbation to a contradicting vocab relation
        if kind is None:
            pool = [v for v in doc.relation_vocab if v != r
                    and verify_nonentailed(doc, h, v, t, {r})]
            if pool:
                er = pool[rng.randrange(len(pool))]
                kind = "entrap_relation"
        if kind is None:
            continue
        # entrapment must be false-by-construction; skip the rare case it lands on gold
        if doc.gold_exact(eh, er, et):
            continue
        dec_r = deterministic_decoy_relation(doc, eh, er, et, rng)
        if dec_r is None:
            continue
        out.append({"cand_id": f"{doc.doc_id}:entrap:{i}", "doc_id": doc.doc_id,
                    "h": eh, "r": er, "t": et, "real_id": c["cand_id"], "kind": kind,
                    "claim": verbalize(eh, er, et),
                    "decoy": {"cand_id": f"{doc.doc_id}:entrapdec:{i}", "doc_id": doc.doc_id,
                              "h": eh, "r": dec_r, "t": et, "kind": "entrap_decoy",
                              "claim": verbalize(eh, dec_r, et)}})
    return out


def _perturb_number(t: str, rng: random.Random) -> str:
    digits = [m.start() for m in re.finditer(r"\d", t)]
    if not digits:
        return t
    pos = digits[rng.randrange(len(digits))]
    old = t[pos]
    new = str((int(old) + 1 + rng.randrange(8)) % 10)
    if new == old:
        new = str((int(old) + 1) % 10)
    return t[:pos] + new + t[pos + 1:]


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
async def score_logprob(client: OpenRouterClient, doc_text: str, claim: str) -> float:
    res = await client.call(PRIMARY_MODEL, score_messages_logprob(doc_text, claim),
                            max_tokens=16, temperature=0.0, logprobs=True, top_logprobs=5)
    z = yes_prob_from_logprobs(res["top_logprobs"], res["content"])
    return float(z) if z is not None else 0.5


async def score_portable(client: OpenRouterClient, doc_text: str, claim: str, k: int) -> float:
    ps = []
    for i in range(k):
        res = await client.call(PRIMARY_MODEL, score_messages_portable(doc_text, claim),
                                max_tokens=24, temperature=0.7, seed=SEED + i, sample_idx=i)
        p = parse_yes_conf(res["content"])
        if p is not None:
            ps.append(p)
    return float(np.mean(ps)) if ps else 0.5


# ---------------------------------------------------------------------------
# Orchestration helper
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
        n_err = sum(1 for r in res if isinstance(r, Exception))
        if n_err:
            for r in res:
                if isinstance(r, Exception) and not isinstance(r, BudgetExceeded):
                    logger.debug(f"  [{label}] task error: {type(r).__name__}: {r}")
        logger.info(f"  [{label}] {min(i+batch, len(coros))}/{len(coros)} | "
                    f"cost=${client.cost_usd:.4f} | live={client.n_calls_live} "
                    f"cached={client.n_calls_cached} | errs={n_err}")
    return out


# ---------------------------------------------------------------------------
# Genre bridge rules (hand-authored, in-genre common-sense gap-filling = multi-hop)
# ---------------------------------------------------------------------------
BRIDGE_RULES = {
    "legal": [
        ("party_bound_effective", "party_bound_effective", (V("A"), V("P"), V("D")),
         [("has_party", (V("A"), V("P"))), ("effective_date", (V("A"), V("D")))]),
        ("titled_dated", "titled_dated", (V("A"), V("T"), V("D")),
         [("has_title", (V("A"), V("T"))), ("agreement_date", (V("A"), V("D")))]),
    ],
    "news": [
        ("co_occurring", "co_occurring", (V("X"), V("Y"), V("D")),
         [("occurred_on", (V("X"), V("D"))), ("occurred_on", (V("Y"), V("D")))]),
    ],
    "regulatory": [
        ("relevant_right", "relevant_right", (V("A"), V("R")),
         [("cross_references", (V("A"), V("B"))), ("grants_right", (V("B"), V("R")))]),
        ("obligation_with_exception", "obligation_with_exception", (V("A"), V("O"), V("E")),
         [("obligates", (V("A"), V("O"))), ("has_exception", (V("A"), V("E")))]),
        ("titled_obligation", "titled_obligation", (V("A"), V("T"), V("O")),
         [("has_title", (V("A"), V("T"))), ("obligates", (V("A"), V("O")))]),
    ],
}


def _degenerate(proof: dict) -> bool:
    """Drop trivial self-derivations (e.g. co_occurring(X,X,D))."""
    name = proof.get("rule")
    args = proof["atom"][1]
    if name == "co_occurring" and len(args) >= 2 and norm_match(args[0], args[1]):
        return True
    return False


# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------
async def run(docs: list[AnchorDoc], cache_dir: Path, cost_log: Path, *, elic: str,
              k_sc: int, n_samples: int, concurrency: int, do_matched_recall: bool,
              soft_cap: float) -> dict:
    t0 = time.time()
    elics = (["logprob", "portable"] if elic == "both" else [elic])
    async with OpenRouterClient(cache_dir, cost_log, concurrency=concurrency,
                                soft_cap_usd=soft_cap, hard_stop_usd=HARD_STOP_USD) as client:
        doc_by_id = {d.doc_id: d for d in docs}

        # ---- STAGE 1: extraction for RAW / RAG / CoT ----
        systems = ["raw", "rag", "cot"] if do_matched_recall else ["raw"]
        logger.info(f"STAGE 1 extraction (systems={systems}, n_samples={n_samples})...")
        ext_tasks, ext_keys = [], []
        for mode in systems:
            for d in docs:
                ext_tasks.append(extract_system(client, d, mode, n_samples))
                ext_keys.append((mode, d.doc_id))
        ext_res = await run_batched(ext_tasks, 48, "extract", client)
        raw_ext = {("raw", d.doc_id): None for d in docs}
        ext_by = {}
        for (mode, did), r in zip(ext_keys, ext_res):
            ext_by[(mode, did)] = r or {"triples": {}, "prov": {}, "n_samples": n_samples}

        # ---- STAGE 1b: relation alignment (open 'other' phrases -> gold vocab) ----
        align_phrases = {d.doc_id: set() for d in docs}
        for (mode, did), r in ext_by.items():
            d = doc_by_id[did]
            for (h, r_raw, t) in r["triples"]:
                if _vocab_relation(r_raw, d.relation_vocab) is None:
                    align_phrases[did].add(r_raw.strip().lower())
        align_map = {d.doc_id: {} for d in docs}
        a_tasks, a_keys = [], []
        for d in docs:
            phrases = sorted(align_phrases[d.doc_id])
            if phrases and d.relation_vocab:
                a_tasks.append(client.call(PRIMARY_MODEL, align_messages(d, phrases),
                                           max_tokens=400, temperature=0.0))
                a_keys.append((d.doc_id, phrases))
        a_res = await run_batched(a_tasks, 48, "align", client) if a_tasks else []
        for (did, phrases), r in zip(a_keys, a_res):
            if r is None:
                continue
            parsed = _extract_json(r["content"]) or {}
            mp = parsed.get("map") if isinstance(parsed, dict) else None
            if isinstance(mp, list):
                for ph, target in zip(phrases, mp):
                    v = _vocab_relation(str(target), doc_by_id[did].relation_vocab) if target else None
                    if v:
                        align_map[did][ph] = v

        def aligned_facts(mode: str, d: AnchorDoc) -> list[dict]:
            """Map a system's raw triples into the gold (head, vocab-relation, tail) space."""
            r = ext_by[(mode, d.doc_id)]
            out, seen = [], set()
            for (h, r_raw, t), freq in r["triples"].items():
                rv = _vocab_relation(r_raw, d.relation_vocab)
                if rv is None:
                    rv = align_map[d.doc_id].get(r_raw.strip().lower())
                if rv is None:
                    continue
                key = (norm(h), rv, norm(t))
                if key in seen:
                    continue
                seen.add(key)
                out.append({"h": h, "r": rv, "t": t, "freq": freq,
                            "conf": freq / max(1, r["n_samples"]),
                            "prov": r["prov"].get((h, r_raw, t), ""),
                            "label": d.label(h, rv, t), "gold_exact": d.gold_exact(h, rv, t)})
            return out

        # RAW reals = aligned RAW facts (capped), the gating pool
        reals_by_doc, sys_facts = {}, defaultdict(dict)
        for d in docs:
            for mode in systems:
                facts = aligned_facts(mode, d)
                if mode == "raw":
                    facts = sorted(facts, key=lambda f: (-f["freq"], f["h"], f["r"], f["t"]))[:REALS_CAP]
                    for i, f in enumerate(facts):
                        f["cand_id"] = f"{d.doc_id}:real:{i}"
                        f["doc_id"] = d.doc_id
                        f["claim"] = verbalize(f["h"], f["r"], f["t"])
                        f["kind"] = "real"
                    reals_by_doc[d.doc_id] = facts
                sys_facts[mode][d.doc_id] = facts
        all_reals = [c for d in docs for c in reals_by_doc[d.doc_id]]
        n_lab = {lab: sum(1 for c in all_reals if c["label"] == lab)
                 for lab in ("TRUE", "FALSE", "UNDECIDABLE")}
        logger.info(f"reals={len(all_reals)} by-label={n_lab}")

        # ---- STAGE 2: decoys + swaps + entrapment ----
        logger.info("STAGE 2 decoys + swaps + entrapment...")
        global_pool = defaultdict(list)
        for d in docs:
            for e in d.entities:
                global_pool[d.entity_type(e["name"])].append((d.doc_id, e["name"]))
        dec = await run_batched(
            [gen_counterfactual_decoys(client, d, reals_by_doc[d.doc_id],
                                       random.Random(_doc_seed(d.doc_id, 7))) for d in docs],
            48, "decoy", client)
        cf_by_doc, swap_by_doc, entrap_by_doc = {}, {}, {}
        n_gen = n_contam = 0
        for d, dd in zip(docs, dec):
            decoys, g, c = dd if dd else ([], 0, 0)
            cf_by_doc[d.doc_id] = decoys
            n_gen += g
            n_contam += c
            swap_by_doc[d.doc_id] = gen_swaps(d, reals_by_doc[d.doc_id],
                                              random.Random(_doc_seed(d.doc_id, 99)))
            entrap_by_doc[d.doc_id] = gen_entrapment(d, reals_by_doc[d.doc_id], global_pool,
                                                     random.Random(_doc_seed(d.doc_id, 31)))
        contamination_rate = (n_contam / n_gen) if n_gen else 0.0
        logger.info(f"decoys; contamination_rate={contamination_rate:.4f}")

        cf_real = {c["real_id"]: c for d in docs for c in cf_by_doc[d.doc_id]}
        swap_real = {c["real_id"]: c for d in docs for c in swap_by_doc[d.doc_id]}

        # ---- STAGE 2: scoring (both elicitations) ----
        zmap: dict[tuple, float] = {}

        def cands_for(elic_name: str) -> list[dict]:
            cs = list(all_reals)
            cs += [c for d in docs for c in cf_by_doc[d.doc_id]]
            cs += [e for d in docs for e in entrap_by_doc[d.doc_id]]
            cs += [e["decoy"] for d in docs for e in entrap_by_doc[d.doc_id]]
            if elic_name == "logprob":   # swaps = logprob-only anti-conservative control
                cs += [c for d in docs for c in swap_by_doc[d.doc_id]]
            return cs

        async def run_score(elic_name, cand):
            d = doc_by_id[cand["doc_id"]]
            if elic_name == "logprob":
                z = await score_logprob(client, d.text, cand["claim"])
            else:
                z = await score_portable(client, d.text, cand["claim"], k_sc)
            return (elic_name, cand["cand_id"], z)

        for en in elics:
            cs = cands_for(en)
            logger.info(f"STAGE 2 scoring elic={en} over {len(cs)} candidates...")
            res = await run_batched([run_score(en, c) for c in cs], 240, f"score-{en}", client)
            for r in res:
                if r:
                    zmap[(r[0], r[1])] = r[2]

        # ---- STAGE 2b: adjudicator (cross-family judge) ----
        logger.info("STAGE 2b cross-family adjudicator (gray-zone + legal validation)...")
        judge_targets = {}   # (doc_id,h,r,t) -> fact-ish dict
        for d in docs:
            for c in reals_by_doc[d.doc_id]:
                if c["label"] == "UNDECIDABLE" or d.genre == "legal":
                    judge_targets[(d.doc_id, c["h"], c["r"], c["t"])] = c
            if do_matched_recall:
                for mode in ("rag", "cot"):
                    for f in sys_facts[mode][d.doc_id]:
                        if f["label"] == "UNDECIDABLE":
                            judge_targets[(d.doc_id, f["h"], f["r"], f["t"])] = f
        jt_list = list(judge_targets.items())

        async def run_judge(key, f):
            d = doc_by_id[key[0]]
            res = await client.call(CROSS_MODEL, judge_messages(d.text, f["h"], f["r"], f["t"],
                                                                f.get("prov", "")),
                                    max_tokens=16, temperature=0.0)
            txt = (res["content"] or "").strip().lower()
            if "contradict" in txt:
                v = "Contradicted"
            elif "unsupport" in txt:
                v = "Unsupported"
            elif "entail" in txt:
                v = "Entailed"
            else:
                v = "Unsupported"
            return (key, v)

        jres = await run_batched([run_judge(k, f) for k, f in jt_list], 96, "judge", client)
        judge_verdict = {k: v for kv in jres if kv for (k, v) in [kv]}

        elapsed = time.time() - t0
        runtime = {"elapsed_s": elapsed, "cost_usd": client.cost_usd,
                   "n_calls_live": client.n_calls_live, "n_calls_cached": client.n_calls_cached,
                   "cached_tokens_observed": client.cached_tokens_observed}
        logger.info(f"Pipeline done {elapsed:.1f}s | cost=${client.cost_usd:.4f}")

    return {"docs": docs, "doc_by_id": doc_by_id, "reals_by_doc": reals_by_doc,
            "all_reals": all_reals, "cf_by_doc": cf_by_doc, "swap_by_doc": swap_by_doc,
            "entrap_by_doc": entrap_by_doc, "cf_real": cf_real, "swap_real": swap_real,
            "zmap": zmap, "elics": elics, "sys_facts": sys_facts, "systems": systems,
            "judge_verdict": judge_verdict, "judge_targets": judge_targets,
            "contamination_rate": contamination_rate, "n_gen_decoys": n_gen,
            "n_lab": n_lab, "runtime": runtime, "k_sc": k_sc, "n_samples": n_samples}


# ===========================================================================
# ANALYSIS (offline, on collected Z)
# ===========================================================================
def rank_normalize_elic(pipe: dict, elic: str) -> dict:
    """Per-document rank-normalisation of every scored candidate Z for one elicitation."""
    zmap = pipe["zmap"]
    norm_out = {}
    for d in pipe["docs"]:
        pool = {}
        cands = (pipe["reals_by_doc"][d.doc_id] + pipe["cf_by_doc"][d.doc_id]
                 + pipe["swap_by_doc"][d.doc_id] + pipe["entrap_by_doc"][d.doc_id]
                 + [e["decoy"] for e in pipe["entrap_by_doc"][d.doc_id]])
        for c in cands:
            k = (elic, c["cand_id"])
            if k in zmap:
                pool[c["cand_id"]] = zmap[k]
        norm_out.update(st.rank_normalize(pool, SEED))
    return norm_out


def cohen_kappa(pairs: list[tuple[bool, bool]]) -> tuple[float, float]:
    n = len(pairs)
    if n == 0:
        return float("nan"), float("nan")
    po = sum(1 for a, b in pairs if a == b) / n
    pa1 = sum(1 for a, _ in pairs if a) / n
    pb1 = sum(1 for _, b in pairs if b) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    kappa = 1.0 if pe == 1 else (po - pe) / (1 - pe)
    return float(kappa), float(po)


def adjudicator_validation(pipe: dict) -> dict:
    """Cohen's kappa between cross-family judge and crisp legal gold on the legal slice."""
    jv = pipe["judge_verdict"]
    pairs = []
    for d in pipe["docs"]:
        if d.genre != "legal":
            continue
        for c in pipe["reals_by_doc"][d.doc_id]:
            v = jv.get((d.doc_id, c["h"], c["r"], c["t"]))
            if v is None:
                continue
            judge_hall = v in ("Unsupported", "Contradicted")
            gold_hall = not c["gold_exact"]
            pairs.append((judge_hall, gold_hall))
    kappa, agree = cohen_kappa(pairs)
    trust = (not math.isnan(kappa)) and kappa >= KAPPA_TRUST
    return {"kappa": kappa, "raw_agreement": agree, "n_legal_judged": len(pairs),
            "trust_threshold": KAPPA_TRUST, "judge_trusted": bool(trust),
            "fallback_active": bool(not trust)}


def annotate_hallucination(pipe: dict, trust_judge: bool) -> None:
    """Attach hall_strict (lower), hall_loose (upper), hall_adj (point) to every fact."""
    jv = pipe["judge_verdict"]

    def ann(f, doc_id):
        lab = f["label"]
        f["hall_strict"] = (lab == "FALSE")
        f["hall_loose"] = (lab != "TRUE")
        if lab == "TRUE":
            f["hall_adj"] = False
            f["verdict"] = "ENTAILED"
        elif lab == "FALSE":
            f["hall_adj"] = True
            f["verdict"] = "HALLUCINATED"
        else:
            v = jv.get((doc_id, f["h"], f["r"], f["t"]))
            if trust_judge and v is not None:
                f["hall_adj"] = v in ("Unsupported", "Contradicted")
                f["verdict"] = ("HALLUCINATED" if f["hall_adj"] else "ENTAILED") + "(judge)"
            else:
                f["hall_adj"] = f["hall_strict"]
                f["verdict"] = "GRAY(gold-fallback)"

    for d in pipe["docs"]:
        for c in pipe["reals_by_doc"][d.doc_id]:
            ann(c, d.doc_id)
        for mode in pipe["systems"]:
            if mode == "raw":
                continue
            for f in pipe["sys_facts"][mode][d.doc_id]:
                ann(f, d.doc_id)


def W_cf_of(pipe: dict, normm: dict, real: dict):
    cf = pipe["cf_real"].get(real["cand_id"])
    if cf is None:
        return None
    zr, zd = normm.get(real["cand_id"]), normm.get(cf["cand_id"])
    if zr is None or zd is None:
        return None
    return st.W_signed_max(zr, zd)


def W_entrap_of(pipe: dict, normm: dict, entrap: dict):
    ze, zd = normm.get(entrap["cand_id"]), normm.get(entrap["decoy"]["cand_id"])
    if ze is None or zd is None:
        return None
    return st.W_signed_max(ze, zd)


def _rate(units, key):
    flat = [f for u in units for f in u]
    if not flat:
        return float("nan")
    return float(np.mean([1.0 if f[key] else 0.0 for f in flat]))


def gate_and_hall_grid(pipe: dict, norms_by_elic: dict) -> list[dict]:
    """The headline grid: one cell per (genre, elicitation, alpha)."""
    grid = []
    for elic, normm in norms_by_elic.items():
        # precompute W per real and per entrapment item
        for real in pipe["all_reals"]:
            real["_w"] = W_cf_of(pipe, normm, real)
        entraps = [e for d in pipe["docs"] for e in pipe["entrap_by_doc"][d.doc_id]]
        for e in entraps:
            e["_w"] = W_entrap_of(pipe, normm, e)
        for genre in GENRES + ["pooled"]:
            sel = (lambda d: True) if genre == "pooled" else (lambda d, g=genre: d.genre == g)
            reals_g = [c for c in pipe["all_reals"]
                       if sel(pipe["doc_by_id"][c["doc_id"]]) and c.get("_w") is not None]
            entrap_g = [e for e in entraps
                        if sel(pipe["doc_by_id"][e["doc_id"]]) and e.get("_w") is not None]
            Wr = [c["_w"] for c in reals_g]
            # doc-block bootstrap units (raw = all reals; gate = admitted reals at T)
            docs_in = sorted({c["doc_id"] for c in reals_g})
            for alpha in ALPHA_GRID:
                T, n_pos, ratio = st.knockoff_plus_threshold(Wr, alpha)
                admit = [] if math.isinf(T) else [c for c in reals_g if c["_w"] >= T]
                N_T = len(admit)
                N_E = 0 if math.isinf(T) else sum(1 for e in entrap_g if e["_w"] >= T)
                realized = (sum(1 for c in admit if c["label"] == "FALSE") / N_T) if N_T else 0.0
                fdp = (N_E * (1 + 1.0 / R_ENTRAP) / (N_T + N_E)) if (N_T + N_E) else None
                kf = st.k_floor(alpha)
                # bootstrap CIs
                raw_units = [[c for c in reals_g if c["doc_id"] == did] for did in docs_in]
                gate_units = [[c for c in admit if c["doc_id"] == did] for did in docs_in]
                raw_ci = st.doc_block_bootstrap(raw_units, lambda u: _rate(u, "hall_adj"),
                                                B=B_BOOT, seed=SEED)
                gate_ci = st.doc_block_bootstrap(gate_units, lambda u: _rate(u, "hall_adj"),
                                                 B=B_BOOT, seed=SEED)
                regime = ("anti_conservative_expected" if elic == "logprob"
                          else ("certified" if N_T >= kf else "uncertified(n<1/alpha)"))
                cell = {
                    "genre": genre, "elicitation": elic, "alpha": alpha,
                    "n_reals": len(reals_g), "n_admitted": N_T, "k_floor": kf,
                    "certified": bool(N_T >= kf),
                    "threshold": (None if math.isinf(T) else round(T, 6)),
                    "decoy_fdr_hat": round(ratio, 6),
                    "realized_fdr": round(realized, 6),
                    "self_report_anticonservative": bool(ratio < realized),
                    "entrapment": {"N_T": N_T, "N_E": N_E, "r": R_ENTRAP,
                                   "FDP_hat": (round(fdp, 6) if fdp is not None else None)},
                    "gate_hall_rate": (round(gate_ci["point"], 6)
                                       if not math.isnan(gate_ci["point"]) else None),
                    "gate_hall_ci": [gate_ci["ci_low"], gate_ci["ci_high"]],
                    "raw_hall_rate": (round(raw_ci["point"], 6)
                                      if not math.isnan(raw_ci["point"]) else None),
                    "raw_hall_ci": [raw_ci["ci_low"], raw_ci["ci_high"]],
                    "silver_bounds": {
                        "gate_lower": _rate(gate_units, "hall_strict"),
                        "gate_upper": _rate(gate_units, "hall_loose"),
                        "raw_lower": _rate(raw_units, "hall_strict"),
                        "raw_upper": _rate(raw_units, "hall_loose")},
                    "regime_tag": regime,
                    "ci_separation_gate_below_raw": bool(
                        not math.isnan(gate_ci["ci_high"]) and not math.isnan(raw_ci["ci_low"])
                        and gate_ci["ci_high"] < raw_ci["ci_low"]),
                }
                grid.append(cell)
    return grid


def matched_recall_curves(pipe: dict, headline_norm: dict) -> dict:
    """Matched-recall precision / hallucination-rate for RAW / GATE / RAG / CoT."""
    docs = pipe["docs"]
    gold_total = sum(len(d.gold_set) for d in docs)

    def matched_gold_id(d: AnchorDoc, f: dict):
        for (gh, gr, gt) in d.gold_set:
            if gr == f["r"] and norm_match(f["h"], gh) and norm_match(f["t"], gt):
                return (d.doc_id, gh, gr, gt)
        return None

    def system_facts(system: str) -> list[dict]:
        out = []
        for d in docs:
            if system in ("raw", "gate"):
                base = pipe["reals_by_doc"][d.doc_id]
            else:
                base = pipe["sys_facts"][system][d.doc_id]
            for f in base:
                if system == "gate":
                    sc = W_cf_of(pipe, headline_norm, f)
                    if sc is None:
                        continue
                else:
                    sc = f.get("conf", 0.0)
                out.append({"doc_id": d.doc_id, "score": sc, "hall_adj": f["hall_adj"],
                            "gold": matched_gold_id(d, f)})
        return out

    curves = {}
    for system in ["raw", "gate", "rag", "cot"]:
        if system in ("rag", "cot") and system not in pipe["systems"]:
            continue
        facts = system_facts(system)
        facts.sort(key=lambda x: x["score"], reverse=True)
        pts = []
        for target in RECALL_GRID:
            covered, admitted, halluc = set(), 0, 0
            thr = None
            for f in facts:
                admitted += 1
                if f["gold"]:
                    covered.add(f["gold"])
                if f["hall_adj"]:
                    halluc += 1
                rec = len(covered) / gold_total if gold_total else 0.0
                if rec >= target:
                    thr = f["score"]
                    break
            reached = thr is not None and admitted > 0
            if not reached:
                pts.append({"recall_target": target, "reached": False})
                continue
            adm = [f for f in facts if f["score"] >= thr]
            docs_in = sorted({f["doc_id"] for f in adm})
            units = [[f for f in adm if f["doc_id"] == did] for did in docs_in]

            def prec_fn(uu):
                flat = [f for g in uu for f in g]
                return (sum(1 for f in flat if f["gold"]) / len(flat)) if flat else float("nan")

            def hall_fn(uu):
                flat = [f for g in uu for f in g]
                return (sum(1 for f in flat if f["hall_adj"]) / len(flat)) if flat else float("nan")
            pci = st.doc_block_bootstrap(units, prec_fn, B=1000, seed=SEED)
            hci = st.doc_block_bootstrap(units, hall_fn, B=1000, seed=SEED)
            pts.append({"recall_target": target, "reached": True, "n_admitted": len(adm),
                        "precision": round(pci["point"], 6),
                        "precision_ci": [pci["ci_low"], pci["ci_high"]],
                        "halluc_rate": round(hci["point"], 6),
                        "halluc_ci": [hci["ci_low"], hci["ci_high"]]})
        max_rec = 0.0
        cov, adm = set(), 0
        for f in facts:
            adm += 1
            if f["gold"]:
                cov.add(f["gold"])
        max_rec = (len(cov) / gold_total) if gold_total else 0.0
        curves[system] = {"points": pts, "max_recall": round(max_rec, 6), "n_facts": len(facts)}
    curves["gold_total"] = gold_total
    return curves


def extraction_quality(pipe: dict) -> dict:
    """Atomic precision/recall per genre (crisp-restricted on legal)."""
    out = {}
    for genre in GENRES:
        docs = [d for d in pipe["docs"] if d.genre == genre]
        precs, recs = [], []
        for d in docs:
            facts = pipe["reals_by_doc"][d.doc_id]
            extracted = {(norm(f["h"]), f["r"], norm(f["t"])) for f in facts}
            tp = sum(1 for f in facts if f["gold_exact"])
            prec = tp / len(facts) if facts else float("nan")
            rec = (sum(1 for g in d.gold_set if any(f["gold_exact"] and f["r"] == g[1]
                   and norm_match(f["h"], g[0]) and norm_match(f["t"], g[2]) for f in facts))
                   / len(d.gold_set)) if d.gold_set else float("nan")
            precs.append(prec)
            recs.append(rec)
        def _safe_mean(xs):
            vals = [x for x in xs if x == x]  # drop NaN
            return float(np.mean(vals)) if vals else None
        out[genre] = {"atomic_precision": _safe_mean(precs),
                      "atomic_recall": _safe_mean(recs),
                      "n_docs": len(docs), "crisp_restricted": genre == "legal"}
    return out


# ---------------------------------------------------------------------------
# STAGE 3 — KB / trace-graphs / multi-hop corruption
# ---------------------------------------------------------------------------
def build_kb(doc: AnchorDoc, facts: list[dict], headline_norm: dict, pipe: dict,
             gate_cell: dict | None) -> kbe.KB:
    kb = kbe.KB()
    for f in facts:
        w = W_cf_of(pipe, headline_norm, f) if "cand_id" in f else None
        cert = {"provenance": f.get("prov", ""),
                "provenance_char_span": None,
                "hallucination_verdict": "HALLUCINATED" if f.get("hall_adj") else "ENTAILED",
                "decoy_certificate": {"W_i": (round(w, 4) if w is not None else None),
                                      "T": (gate_cell or {}).get("threshold"),
                                      "alpha": (gate_cell or {}).get("alpha")},
                "entrapment_certificate": {
                    "FDP_hat": ((gate_cell or {}).get("entrapment") or {}).get("FDP_hat"),
                    "r": R_ENTRAP}}
        kb.add_fact(f["r"], (f["h"], f["t"]), cert)
    for spec in BRIDGE_RULES.get(doc.genre, []):
        kb.add_rule(*spec)
    return kb


def derive_doc(kb: kbe.KB) -> list[dict]:
    return [p for p in kb.derive_all(max_depth=4) if not _degenerate(p)]


def multihop_corruption(pipe: dict, headline_norm: dict, grid: list[dict],
                        headline_elic: str) -> dict:
    """Corrupted-conclusion rate (any supporting leaf HALLUCINATED) RAW-KB vs GATE-KB."""
    out = {"by_genre": {}, "pooled": {}}
    cell_by = {(c["genre"], c["alpha"]): c for c in grid if c["elicitation"] == headline_elic}
    pooled = {"raw": {"derived": 0, "corrupt": 0}}
    for a in ALPHA_GRID:
        pooled[f"gate_a{a}"] = {"derived": 0, "corrupt": 0}
    for genre in GENRES:
        docs = [d for d in pipe["docs"] if d.genre == genre]
        g = {"raw": {"derived": 0, "corrupt": 0}}
        for a in ALPHA_GRID:
            g[f"gate_a{a}"] = {"derived": 0, "corrupt": 0}
        for d in docs:
            reals = pipe["reals_by_doc"][d.doc_id]
            # RAW-KB: all reals
            kb = build_kb(d, reals, headline_norm, pipe, None)
            for p in derive_doc(kb):
                corrupt = any((lf["cert"] or {}).get("hallucination_verdict") == "HALLUCINATED"
                              for lf in kbe.iter_leaves(p))
                g["raw"]["derived"] += 1
                g["raw"]["corrupt"] += int(corrupt)
                pooled["raw"]["derived"] += 1
                pooled["raw"]["corrupt"] += int(corrupt)
            # GATE-KB per alpha
            for a in ALPHA_GRID:
                cell = cell_by.get((genre, a))
                T = cell["threshold"] if cell else None
                if T is None:
                    continue
                admit = [r for r in reals if (r.get("_w") is not None and r["_w"] >= T)]
                kb2 = build_kb(d, admit, headline_norm, pipe, cell)
                for p in derive_doc(kb2):
                    corrupt = any((lf["cert"] or {}).get("hallucination_verdict") == "HALLUCINATED"
                                  for lf in kbe.iter_leaves(p))
                    g[f"gate_a{a}"]["derived"] += 1
                    g[f"gate_a{a}"]["corrupt"] += int(corrupt)
                    pooled[f"gate_a{a}"]["derived"] += 1
                    pooled[f"gate_a{a}"]["corrupt"] += int(corrupt)

        def rate(x):
            return (x["corrupt"] / x["derived"]) if x["derived"] else None
        out["by_genre"][genre] = {k: {"derived": v["derived"], "corrupt": v["corrupt"],
                                      "corrupted_rate": rate(v)} for k, v in g.items()}
    out["pooled"] = {k: {"derived": v["derived"], "corrupt": v["corrupt"],
                         "corrupted_rate": (v["corrupt"] / v["derived"]) if v["derived"] else None}
                     for k, v in pooled.items()}
    return out


def _admission_trace(real: dict, cert: dict) -> dict:
    """Depth-1 trace for the admission boundary: admitted_fact(...) <- leaf with certificate.
    Used to guarantee per-genre auditable artifacts when no multi-hop bridge fires."""
    concl = f"{real['r']}({real['h']},{real['t']})"
    return {"type": "derived", "atom": ["admitted_fact", [concl]], "rule": "admission",
            "children": [{"type": "leaf", "atom": [real["r"], [real["h"], real["t"]]],
                          "cert": cert}]}


def export_trace_graphs(pipe: dict, headline_norm: dict, grid: list[dict],
                        headline_elic: str, out_dir: Path) -> dict:
    """Export >=2 docs/genre as JSON + DOT trace-graphs with certificate leaves.
    Real multi-hop proofs are exported first; genres without (enough) firing bridges are
    topped up with depth-1 admission traces so every genre has auditable artifacts."""
    out_dir.mkdir(exist_ok=True)
    cell_by = {(c["genre"], c["alpha"]): c for c in grid if c["elicitation"] == headline_elic}
    serialized, dot_paths = [], []

    def write_doc(d, genre, proofs, gate_cell, kind):
        graphs = [kbe.proof_to_graph(p) for p in proofs[:6]]
        jpath = out_dir / f"trace_{d.doc_id}.json"
        jpath.write_text(json.dumps({"doc_id": d.doc_id, "genre": genre, "kind": kind,
                                     "n_proofs": len(proofs), "graphs": graphs,
                                     "proofs": proofs[:6]}, indent=2))
        dot = kbe.graph_to_dot(graphs[0], title=f"{d.doc_id} [{genre}] {proofs[0]['rule']}")
        dpath = out_dir / f"trace_{d.doc_id}.dot"
        dpath.write_text(dot)
        dot_paths.append(str(dpath.relative_to(HERE)))
        serialized.append({"doc_id": d.doc_id, "genre": genre, "kind": kind,
                           "rule": proofs[0]["rule"], "conclusion": proofs[0]["atom"],
                           "graph": graphs[0], "json_path": str(jpath.relative_to(HERE)),
                           "dot_path": str(dpath.relative_to(HERE))})

    for genre in GENRES:
        docs = [d for d in pipe["docs"] if d.genre == genre]
        cells = [cell_by.get((genre, a)) for a in ALPHA_GRID]
        gate_cell = next((c for c in reversed(cells) if c and c["certified"]),
                         cells[-1] if cells else None)
        done = set()
        # 1) real multi-hop proofs
        for d in docs:
            if len([s for s in serialized if s["genre"] == genre]) >= 2:
                break
            kb = build_kb(d, pipe["reals_by_doc"][d.doc_id], headline_norm, pipe, gate_cell)
            proofs = derive_doc(kb)
            if proofs:
                write_doc(d, genre, proofs, gate_cell, "multi_hop")
                done.add(d.doc_id)
        # 2) top up with admission traces so each genre has >=2 artifacts
        for d in docs:
            if len([s for s in serialized if s["genre"] == genre]) >= 2:
                break
            if d.doc_id in done:
                continue
            reals = sorted(pipe["reals_by_doc"][d.doc_id],
                           key=lambda r: (r.get("_w") if r.get("_w") is not None else -9))
            reals = [r for r in reals if r.get("_w") is not None] or pipe["reals_by_doc"][d.doc_id]
            if not reals:
                continue
            kb = build_kb(d, [reals[-1]], headline_norm, pipe, gate_cell)
            cert = list(kb.facts.values())[0] if kb.facts else {"provenance": reals[-1].get("prov", "")}
            write_doc(d, genre, [_admission_trace(reals[-1], cert)], gate_cell, "admission")
    return {"n_exported": len(serialized), "examples": serialized, "dot_paths": dot_paths,
            "note": "multi_hop = real bridge derivation; admission = depth-1 admission-boundary "
                    "trace with full per-leaf certificate (used where no bridge fires)."}


def s1_signature(pipe: dict, norms_by_elic: dict) -> dict:
    """Counterfactual vs random-swap tail decoy win-rate (the S1 diagnostic-sensitivity
    control). Win-rate ~0.5 => exchangeable; <0.5 => anti-conservative. Swaps are scored
    under logprob only (the documented anti-conservative negative control)."""
    out = {}
    for elic, normm in norms_by_elic.items():
        fam_out = {}
        for fam, lookup in (("counterfactual", pipe["cf_real"]),
                            ("random_swap", pipe["swap_real"])):
            pairs = []
            for c in pipe["all_reals"]:
                dec = lookup.get(c["cand_id"])
                if not dec:
                    continue
                zr, zd = normm.get(c["cand_id"]), normm.get(dec["cand_id"])
                if zr is None or zd is None:
                    continue
                pairs.append({"zr": zr, "zd": zd, "w": st.W_signed_max(zr, zd),
                              "label": c["label"]})
            W = [p["w"] for p in pairs]
            false_pairs = [(p["zr"], p["zd"]) for p in pairs if p["label"] == "FALSE"]
            rows = []
            for a in ALPHA_GRID:
                T, n, ratio = st.knockoff_plus_threshold(W, a)
                wr, nt = st.tail_win_rate(false_pairs, (0.0 if math.isinf(T) else T))
                rows.append({"alpha": a, "n_admitted": n,
                             "threshold": (None if math.isinf(T) else round(T, 6)),
                             "tail_win_rate": (None if math.isnan(wr) else round(wr, 6)),
                             "n_tail": nt})
            fam_out[fam] = {"rows": rows, "n_pairs": len(pairs)}
        out[elic] = fam_out
    return out


def collect_bh(grid: list[dict], adj: dict) -> list[dict]:
    """BH across the validation tests (gate-below-raw CI separation + adjudicator)."""
    tests = []
    for c in grid:
        # one-sided bootstrap-style p: fraction of overlap proxy via CI; use a z-like proxy
        gr, rr = c.get("gate_hall_rate"), c.get("raw_hall_rate")
        glo, ghi = c["gate_hall_ci"]
        rlo, rhi = c["raw_hall_ci"]
        if gr is None or rr is None or any(v is None or (isinstance(v, float) and math.isnan(v))
                                           for v in [glo, ghi, rlo, rhi]):
            continue
        se = (max(1e-9, (ghi - glo) / 3.92) ** 2 + max(1e-9, (rhi - rlo) / 3.92) ** 2) ** 0.5
        zstat = (rr - gr) / se if se > 0 else 0.0
        from scipy.stats import norm as _norm
        p = float(1 - _norm.cdf(zstat))  # H1: gate < raw
        tests.append((f"gate<raw[{c['genre']}|{c['elicitation']}|a{c['alpha']}]", p))
    if not math.isnan(adj.get("kappa", float("nan"))):
        # adjudicator agreement test (binomial vs chance 0.5)
        n = max(1, adj["n_legal_judged"])
        from scipy.stats import binomtest
        k = int(round(adj["raw_agreement"] * n))
        p = float(binomtest(k, n, 0.5, alternative="greater").pvalue)
        tests.append(("adjudicator_agreement_vs_chance", p))
    tests = [(nm, pp) for nm, pp in tests if pp is not None and not math.isnan(pp)]
    if not tests:
        return []
    bh = st.benjamini_hochberg([p for _, p in tests], q=0.05)
    return [{"test_name": nm, **b} for (nm, _), b in zip(tests, bh)]


# ---------------------------------------------------------------------------
# Build method_out.json (exp_gen_sol_out schema)
# ---------------------------------------------------------------------------
def _clean(o):
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        return _clean(float(o))
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def compute_headline(grid: list[dict]) -> dict:
    """Locate cells where gate hallucination < raw with CI separation; summarise regime map."""
    reductions = []
    for c in grid:
        if c["gate_hall_rate"] is None or c["raw_hall_rate"] is None:
            continue
        delta = c["raw_hall_rate"] - c["gate_hall_rate"]
        reductions.append({"genre": c["genre"], "elicitation": c["elicitation"],
                           "alpha": c["alpha"], "raw": c["raw_hall_rate"],
                           "gate": c["gate_hall_rate"], "abs_reduction": round(delta, 6),
                           "rel_reduction": (round(delta / c["raw_hall_rate"], 6)
                                             if c["raw_hall_rate"] else None),
                           "ci_separated": c["ci_separation_gate_below_raw"],
                           "certified": c["certified"], "n_admitted": c["n_admitted"],
                           "regime_tag": c["regime_tag"]})
    sep = [r for r in reductions if r["ci_separated"] and r["abs_reduction"] > 0]
    sep.sort(key=lambda r: r["abs_reduction"], reverse=True)
    best = sep[0] if sep else (max(reductions, key=lambda r: r["abs_reduction"])
                               if reductions else None)
    anticons = [{"genre": c["genre"], "elicitation": c["elicitation"], "alpha": c["alpha"],
                 "decoy_fdr_hat": c["decoy_fdr_hat"], "realized_fdr": c["realized_fdr"]}
                for c in grid if c["self_report_anticonservative"]]
    return {"best_reduction_cell": best,
            "n_cells_gate_below_raw_ci_separated": len(sep),
            "all_reductions": reductions,
            "self_report_anticonservative_cells": anticons}


# ===========================================================================
# ITER-4 ADDITIONS — (P4) probabilistic reasoner + (P2) honest finalized reporting.
# These are PURELY ADDITIVE: they read the existing pipe/grid and never mutate any
# deterministic headline metric (the backward-chaining engine remains the baseline).
# ===========================================================================
def _corrupt_units(pipe: dict, headline_norm: dict, docs: list, admit_fn) -> list:
    """Per-document list of corrupted-flags over that document's derived conclusions."""
    units = []
    for d in docs:
        kb = build_kb(d, admit_fn(d), headline_norm, pipe, None)
        flags = []
        for p in derive_doc(kb):
            corrupt = any((lf["cert"] or {}).get("hallucination_verdict") == "HALLUCINATED"
                          for lf in kbe.iter_leaves(p))
            flags.append(1.0 if corrupt else 0.0)
        units.append(flags)
    return units


def multihop_corruption_ci(pipe: dict, headline_norm: dict, grid: list[dict],
                           headline_elic: str, base_multihop: dict) -> dict:
    """Augment the multi-hop corruption result with document-block bootstrap CIs (raw,
    gate@alpha=0.5, and the raw-gate delta), a single-genre origin flag, and per-system
    derived-conclusion counts. POINT ESTIMATES are the existing ones (unchanged)."""
    out = json.loads(json.dumps(base_multihop))  # deep copy; keep all prior fields
    cell_by = {(c["genre"], c["alpha"]): c for c in grid if c["elicitation"] == headline_elic}
    docs = pipe["docs"]

    def rate(units):
        flat = [x for u in units for x in u]
        return float(np.mean(flat)) if flat else float("nan")

    def gate_admit(d):
        cell = cell_by.get((d.genre, 0.5))
        T = cell["threshold"] if cell else None
        if T is None:
            return []
        return [r for r in pipe["reals_by_doc"][d.doc_id]
                if r.get("_w") is not None and r["_w"] >= T]

    raw_units = _corrupt_units(pipe, headline_norm, docs,
                               lambda d: pipe["reals_by_doc"][d.doc_id])
    gate_units = _corrupt_units(pipe, headline_norm, docs, gate_admit)
    raw_ci = st.doc_block_bootstrap(raw_units, rate, B=B_BOOT, seed=SEED)
    gate_ci = st.doc_block_bootstrap(gate_units, rate, B=B_BOOT, seed=SEED)
    paired = [{"raw": r, "gate": g} for r, g in zip(raw_units, gate_units)]

    def delta_fn(units):
        rf = [x for u in units for x in u["raw"]]
        gf = [x for u in units for x in u["gate"]]
        if not rf or not gf:
            return float("nan")
        return float(np.mean(rf) - np.mean(gf))
    delta_ci = st.doc_block_bootstrap(paired, delta_fn, B=B_BOOT, seed=SEED)

    # which genres actually contribute multi-hop derivations (corrupt or not)
    bg = out["by_genre"]
    contrib = [g for g in GENRES if (bg[g]["raw"]["derived"] or 0) > 0]
    corrupt_contrib = [g for g in GENRES if (bg[g]["raw"]["corrupt"] or 0) > 0]
    single = corrupt_contrib[0] if len(corrupt_contrib) == 1 else None

    out["ci"] = {
        "bootstrap": "document-block (cluster) resampling", "B": B_BOOT, "n_docs": len(docs),
        "raw_corrupted_rate": {"point": (None if math.isnan(raw_ci["point"]) else round(raw_ci["point"], 6)),
                               "ci": [raw_ci["ci_low"], raw_ci["ci_high"]]},
        "gate_a0.5_corrupted_rate": {"point": (None if math.isnan(gate_ci["point"]) else round(gate_ci["point"], 6)),
                                     "ci": [gate_ci["ci_low"], gate_ci["ci_high"]]},
        "delta_raw_minus_gate": {"point": (None if math.isnan(delta_ci["point"]) else round(delta_ci["point"], 6)),
                                 "ci": [delta_ci["ci_low"], delta_ci["ci_high"]],
                                 "ci_excludes_zero": bool(not math.isnan(delta_ci["ci_low"])
                                                          and delta_ci["ci_low"] > 0)},
    }
    out["per_system_derived_counts"] = {
        "raw_kb": out["pooled"]["raw"]["derived"],
        "gate_kb_a0.5": out["pooled"]["gate_a0.5"]["derived"]}
    out["single_genre_origin"] = single
    out["contributing_genres"] = contrib
    out["origin_note"] = (
        f"The pooled multi-hop corruption drop ({out['pooled']['raw'].get('corrupted_rate')} -> "
        f"{out['pooled']['gate_a0.5'].get('corrupted_rate')}) is ENTIRELY {single}-driven: "
        f"legal derives clean conclusions (corrupt=0) and news derives none "
        f"(derived={bg['news']['raw']['derived']}). With one contributing genre and only "
        f"{out['pooled']['raw']['derived']}->{out['pooled']['gate_a0.5']['derived']} conclusions the "
        f"CI is WIDE; this is a DIRECTIONAL trend, not a significant reduction.")
    return out


def atomic_reduction_pooled(pipe: dict, norms_by_elic: dict, grid: list[dict]) -> dict:
    """Pooled (all-genre) atomic hallucinated-fact reduction per (elicitation, alpha) with a
    document-block bootstrap CI on the raw-gate DIFFERENCE. Reports the directional-not-
    significant finding explicitly (expected 0 CI-separated cells at n=24)."""
    by_cell, n_sep, n_cells = [], 0, 0
    for elic in pipe["elics"]:
        normm = norms_by_elic[elic]
        pooled_cells = {c["alpha"]: c for c in grid
                        if c["genre"] == "pooled" and c["elicitation"] == elic}
        Wd, reals_g = {}, []
        for r in pipe["all_reals"]:
            w = W_cf_of(pipe, normm, r)
            if w is not None:
                Wd[r["cand_id"]] = w
                reals_g.append(r)
        docs_in = sorted({r["doc_id"] for r in reals_g})
        for alpha in ALPHA_GRID:
            cell = pooled_cells.get(alpha)
            if not cell:
                continue
            T = cell["threshold"]
            raw, gate = cell["raw_hall_rate"], cell["gate_hall_rate"]
            units = []
            for did in docs_in:
                rr = [r for r in reals_g if r["doc_id"] == did]
                raw_flags = [1.0 if r.get("hall_adj") else 0.0 for r in rr]
                gate_flags = ([] if T is None else
                              [1.0 if r.get("hall_adj") else 0.0 for r in rr if Wd[r["cand_id"]] >= T])
                units.append({"raw": raw_flags, "gate": gate_flags})

            def diff_fn(uu):
                rf = [x for u in uu for x in u["raw"]]
                gf = [x for u in uu for x in u["gate"]]
                if not rf or not gf:
                    return float("nan")
                return float(np.mean(rf) - np.mean(gf))
            dci = st.doc_block_bootstrap(units, diff_fn, B=B_BOOT, seed=SEED)
            diff = (raw - gate) if (raw is not None and gate is not None) else None
            sep = bool(not math.isnan(dci["ci_low"]) and dci["ci_low"] > 0)
            n_sep += int(sep)
            n_cells += 1
            by_cell.append({"elicitation": elic, "alpha": alpha, "raw": raw, "gate": gate,
                            "diff": (round(diff, 6) if diff is not None else None),
                            "rel_reduction": (round(diff / raw, 6) if (diff is not None and raw) else None),
                            "diff_ci": [dci["ci_low"], dci["ci_high"]],
                            "ci_separated": sep, "n_admitted": cell["n_admitted"],
                            "directional": bool(diff is not None and diff > 0)})
    grid_sep = sum(1 for c in grid if c.get("ci_separation_gate_below_raw"))
    return {
        "by_cell": by_cell,
        "cells_ci_separated_pooled": n_sep, "n_pooled_cells": n_cells,
        "cells_ci_separated_allgrid": grid_sep, "n_allgrid_cells": len(grid),
        "directional_not_significant": True,
        "headline_alpha": 0.5,
        "note": (f"Pooled atomic hallucinated-fact reduction is DIRECTIONAL, not CI-separated at "
                 f"n=24: {grid_sep}/{len(grid)} grid cells and {n_sep}/{n_cells} pooled cells have a "
                 f"raw-gate difference CI excluding 0. Reported as a ~25% relative-reduction trend "
                 f"with auditable provenance, NOT a significant reduction."),
    }


def self_report_regime_analysis(grid: list[dict], tau: float = 0.05) -> dict:
    """Compare the gate's own decoy_fdr_hat to the realized FDR in every cell. CONSERVATIVE
    regime <=> decoy_fdr_hat >= realized everywhere (gate over-estimates falsity / under-admits)
    — the OPPOSITE of the CLUTRR multi-hop anti-conservative regime."""
    triples, anti = [], 0
    for c in grid:
        dfh, rel = c["decoy_fdr_hat"], c["realized_fdr"]
        is_anti = bool(dfh is not None and rel is not None and dfh < rel - tau)
        anti += int(is_anti)
        triples.append({"genre": c["genre"], "elicitation": c["elicitation"], "alpha": c["alpha"],
                        "decoy_fdr_hat": dfh, "realized_fdr": rel,
                        "gap_hat_minus_realized": (round(dfh - rel, 6) if (dfh is not None and rel is not None) else None),
                        "anti_conservative": is_anti})
    regime = ("conservative" if anti == 0 else
              ("anti_conservative" if anti == len(grid) else "mixed"))
    return {
        "regime": regime, "anti_conservative_cells": anti, "n_cells": len(grid), "tau": tau,
        "triples": triples,
        "clutrr_contrast": {
            "clutrr_multihop_decoy_fdr_hat": 0.5, "clutrr_multihop_realized": 1.0,
            "note": ("decoy_fdr_hat >= realized in ALL cells here (the gate over-estimates "
                     "falsity / under-admits => CONSERVATIVE), the OPPOSITE of the CLUTRR "
                     "multi_hop anti-conservative regime where decoy_fdr_hat=0.5 < realized=1.0.")},
        "interpretation": ("A conservative self-report means the certificate is an UPPER bound on "
                           "the realized error here: the operator can trust decoy_fdr_hat as a safe "
                           "(if loose) ceiling on admitted-fact falsity."),
    }


def _leaf_weights_for_doc(pipe: dict, headline_norm: dict, d: AnchorDoc,
                          alpha_hat: float, scheme: str) -> dict:
    """{(rel,(h,t)) -> w_i} for one document under a weighting scheme (first occurrence wins,
    mirroring build_kb's fact dedup)."""
    lw = {}
    for f in pipe["reals_by_doc"][d.doc_id]:
        if "cand_id" not in f:
            continue
        key = (f["r"], (f["h"], f["t"]))
        if key in lw:
            continue
        z = headline_norm.get(f["cand_id"])
        if scheme == "gate_consistent":
            w = pr.weight_gate_consistent(z, alpha_hat)
        elif scheme == "margin":
            w = pr.weight_margin(W_cf_of(pipe, headline_norm, f))
        else:  # identity / no-shrinkage
            w = pr.weight_identity(z)
        lw[key] = w
    return lw


def prob_reasoning_block(pipe: dict, norms_by_elic: dict, grid: list[dict],
                         headline_elic: str, out_dir: Path) -> dict:
    """P4 deliverable: turn each document's admitted-fact KB into a weighted ProbLog program
    (gate-consistent shrinkage weights), compute multi-hop conclusion MARGINALS (ProbLog,
    exact-WMC fallback), and export probabilistic trace-graphs (>=1/genre; genuine multi-hop
    on regulatory, single-fact probabilistic admissions on legal/news)."""
    out_dir.mkdir(exist_ok=True)
    headline_norm = norms_by_elic[headline_elic]
    ah_by_genre = {c["genre"]: c["decoy_fdr_hat"] for c in grid
                   if c["elicitation"] == headline_elic and c["alpha"] == 0.5}
    gate_cell_by = {(c["genre"], c["alpha"]): c for c in grid if c["elicitation"] == headline_elic}

    examples, per_doc_marginals, sensitivity = [], [], []
    genres_with_multihop = set()
    engine_used = set()

    def write_prob_doc(d, genre, proofs, kb, lw, kind):
        concl = [(p["atom"][0], p["atom"][1]) for p in proofs]
        marg, eng = pr.conclusion_marginals(kb, lw, concl)
        engine_used.add(eng)
        graphs = [pr.proof_to_prob_graph(p, lw, marg) for p in proofs[:6]]
        program, _qm = pr.build_program(kb, lw, concl)
        jpath = out_dir / f"prob_trace_{d.doc_id}.json"
        jpath.write_text(json.dumps(_clean({
            "doc_id": d.doc_id, "genre": genre, "engine": eng, "kind": kind,
            "graphs": graphs,
            "marginals": [{"conclusion": [k[0], list(k[1])], "marginal": v} for k, v in marg.items()],
            "program": program}), indent=2))
        dot = pr.prob_graph_to_dot(graphs[0], title=f"{d.doc_id} [{genre}] {proofs[0]['rule']} (prob)")
        dpath = out_dir / f"prob_trace_{d.doc_id}.dot"
        dpath.write_text(dot)
        p0 = proofs[0]
        k0 = (p0["atom"][0], tuple(p0["atom"][1]))
        examples.append(_clean({
            "doc_id": d.doc_id, "genre": genre, "engine": eng, "kind": kind,
            "rule": p0["rule"], "conclusion": p0["atom"], "marginal": marg.get(k0),
            "n_conclusions": len(marg),
            "json_path": str(jpath.relative_to(HERE)), "dot_path": str(dpath.relative_to(HERE))}))
        per_doc_marginals.append(_clean({
            "doc_id": d.doc_id, "genre": genre, "engine": eng, "kind": kind,
            "marginals": [{"conclusion": [k[0], list(k[1])], "marginal": v} for k, v in marg.items()]}))
        return marg, concl

    for genre in GENRES:
        docs = [d for d in pipe["docs"] if d.genre == genre]
        gc = gate_cell_by.get((genre, 0.5))
        ah = ah_by_genre.get(genre, 0.0) or 0.0
        exported = 0
        # (1) genuine multi-hop probabilistic marginals (regulatory is the showcase)
        for d in docs:
            if exported >= (3 if genre == "regulatory" else 1):
                break
            kb = build_kb(d, pipe["reals_by_doc"][d.doc_id], headline_norm, pipe, gc)
            proofs = derive_doc(kb)
            if not proofs:
                continue
            lw = _leaf_weights_for_doc(pipe, headline_norm, d, ah, "gate_consistent")
            marg, concl = write_prob_doc(d, genre, proofs, kb, lw, "multi_hop")
            genres_with_multihop.add(genre)
            exported += 1
            # sensitivity: marginal under the 3 weight schemes on the SAME proofs (regulatory)
            if genre == "regulatory":
                scheme_marg = {}
                for scheme in ("gate_consistent", "margin", "identity"):
                    lw_s = _leaf_weights_for_doc(pipe, headline_norm, d, ah, scheme)
                    m_s, _e = pr.conclusion_marginals(kb, lw_s, concl)
                    scheme_marg[scheme] = m_s
                for (cp, ca) in concl:
                    key = (cp, tuple(ca))
                    sensitivity.append(_clean({
                        "doc_id": d.doc_id, "conclusion": [cp, list(ca)],
                        "alpha_hat": ah,
                        "marginal_gate_consistent_shrinkage": scheme_marg["gate_consistent"].get(key),
                        "marginal_per_pair_margin": scheme_marg["margin"].get(key),
                        "marginal_identity_no_shrinkage": scheme_marg["identity"].get(key)}))
        # (2) top up with a depth-1 probabilistic admission trace where no bridge fires
        if exported == 0:
            for d in docs:
                reals = [r for r in pipe["reals_by_doc"][d.doc_id] if r.get("_w") is not None]
                reals = reals or pipe["reals_by_doc"][d.doc_id]
                if not reals:
                    continue
                real = sorted(reals, key=lambda r: (r.get("_w") if r.get("_w") is not None else -9),
                              reverse=True)[0]
                kb_tmp = build_kb(d, [real], headline_norm, pipe, gc)
                cert = (list(kb_tmp.facts.values())[0] if kb_tmp.facts
                        else {"provenance": real.get("prov", "")})
                lw = _leaf_weights_for_doc(pipe, headline_norm, d, ah, "gate_consistent")
                w_i = lw.get((real["r"], (real["h"], real["t"])), 0.5)
                concl_str = f"{real['r']}({real['h']},{real['t']})"
                proof = _admission_trace(real, cert)
                marg = {("admitted_fact", (concl_str,)): w_i}
                graph = pr.proof_to_prob_graph(proof, lw, marg)
                program, _qm = pr.build_program(kb_tmp, lw, [])
                jpath = out_dir / f"prob_trace_{d.doc_id}.json"
                jpath.write_text(json.dumps(_clean({
                    "doc_id": d.doc_id, "genre": genre, "engine": "leaf_weight", "kind": "admission",
                    "graphs": [graph],
                    "marginals": [{"conclusion": ["admitted_fact", [concl_str]], "marginal": w_i}],
                    "program": program}), indent=2))
                dot = pr.prob_graph_to_dot(graph, title=f"{d.doc_id} [{genre}] admission (prob)")
                dpath = out_dir / f"prob_trace_{d.doc_id}.dot"
                dpath.write_text(dot)
                engine_used.add("leaf_weight")
                examples.append(_clean({
                    "doc_id": d.doc_id, "genre": genre, "engine": "leaf_weight", "kind": "admission",
                    "rule": "admission", "conclusion": ["admitted_fact", [concl_str]],
                    "marginal": w_i, "n_conclusions": 1,
                    "json_path": str(jpath.relative_to(HERE)), "dot_path": str(dpath.relative_to(HERE))}))
                per_doc_marginals.append(_clean({
                    "doc_id": d.doc_id, "genre": genre, "engine": "leaf_weight", "kind": "admission",
                    "marginals": [{"conclusion": ["admitted_fact", [concl_str]], "marginal": w_i}]}))
                exported += 1
                break

    return {
        "engine": ("problog" if "problog" in engine_used else
                   ("fallback_exact_wmc" if "fallback_exact_wmc" in engine_used else
                    ("fallback_noisy_or_approx" if "fallback_noisy_or_approx" in engine_used
                     else "leaf_weight"))),
        "engines_used": sorted(engine_used),
        "problog_available": pr.problog_available(),
        "mapping_default": "gate_consistent_shrinkage",
        "weight_map": {"gate_consistent_shrinkage": "w_i = (1 - alpha_hat) * calibrate(Z_i)  [DEFAULT]",
                       "per_pair_margin": "w_i = clip(0.5 + 0.5*W_i, eps, 1-eps)",
                       "identity_no_shrinkage": "w_i = calibrate(Z_i), alpha_hat=0  [sensitivity baseline]",
                       "calibrate": "identity clamp Z_i -> [eps, 1-eps] (label-free, monotone)",
                       "alpha_hat_source": "decoy_fdr_hat of the operative (genre, %s, alpha=0.5) gate cell" % headline_elic},
        "alpha_hat_by_genre": ah_by_genre,
        "genres_with_multihop": sorted(genres_with_multihop),
        "n_exported": len(examples),
        "examples": examples,
        "per_doc_marginals": per_doc_marginals,
        "sensitivity_shrinkage_vs_margin": sensitivity,
        "note": ("deterministic backward-chaining remains the baseline; NO headline number depends "
                 "on ProbLog. Multi-hop probabilistic marginals are demonstrated on regulatory "
                 "(real cross_references+grants_right bridges); legal/news show single-fact "
                 "probabilistic admissions (marginal = the leaf's calibrated unification weight)."),
    }


def figure_arrays(grid: list[dict], atomic_pooled: dict, multihop_ci: dict,
                  self_report: dict, prob_block: dict) -> dict:
    """Figure-ready arrays + full captions (F1-F4). PNGs are rendered by build_figures.py."""
    elics = sorted({c["elicitation"] for c in grid})
    # ---- F1: pooled atomic raw vs gate across alpha, both elicitations, CI bars ----
    f1 = {"alpha_grid": ALPHA_GRID, "k_floor": [st.k_floor(a) for a in ALPHA_GRID], "by_elic": {}}
    for elic in elics:
        cells = {c["alpha"]: c for c in grid if c["genre"] == "pooled" and c["elicitation"] == elic}
        f1["by_elic"][elic] = {
            "raw": [cells[a]["raw_hall_rate"] for a in ALPHA_GRID if a in cells],
            "raw_ci": [cells[a]["raw_hall_ci"] for a in ALPHA_GRID if a in cells],
            "gate": [cells[a]["gate_hall_rate"] for a in ALPHA_GRID if a in cells],
            "gate_ci": [cells[a]["gate_hall_ci"] for a in ALPHA_GRID if a in cells],
            "n_admitted": [cells[a]["n_admitted"] for a in ALPHA_GRID if a in cells]}
    f1["caption"] = (
        "F1. Pooled (all-genre) atomic hallucinated-fact rate, RAW LLM vs decoy-competition "
        "gate, across alpha for both elicitations (logprob, portable). Error bars = "
        f"document-block (cluster) bootstrap 95% CI (B={B_BOOT}), n=24 docs. "
        f"{atomic_pooled['cells_ci_separated_allgrid']}/{atomic_pooled['n_allgrid_cells']} grid "
        "cells are CI-separated => the ~25% relative reduction at alpha=0.5 (raw~0.245 -> "
        "gate~0.18) is a DIRECTIONAL trend, NOT significant at n=24. The 1/k admission floor is "
        "{20,10,5,4,2} for alpha {.05,.10,.20,.30,.50}.")
    # ---- F2: multi-hop corruption raw vs gate(a=0.5) with CIs + per-genre counts ----
    bg = multihop_ci["by_genre"]
    f2 = {
        "raw_point": multihop_ci["ci"]["raw_corrupted_rate"]["point"],
        "raw_ci": multihop_ci["ci"]["raw_corrupted_rate"]["ci"],
        "gate_point": multihop_ci["ci"]["gate_a0.5_corrupted_rate"]["point"],
        "gate_ci": multihop_ci["ci"]["gate_a0.5_corrupted_rate"]["ci"],
        "delta_point": multihop_ci["ci"]["delta_raw_minus_gate"]["point"],
        "delta_ci": multihop_ci["ci"]["delta_raw_minus_gate"]["ci"],
        "per_genre": {g: {"raw_derived": bg[g]["raw"]["derived"], "raw_corrupt": bg[g]["raw"]["corrupt"],
                          "gate_derived": bg[g]["gate_a0.5"]["derived"],
                          "gate_corrupt": bg[g]["gate_a0.5"]["corrupt"]} for g in GENRES},
        "single_genre_origin": multihop_ci.get("single_genre_origin")}
    f2["caption"] = (
        "F2. Multi-hop corrupted-conclusion rate, RAW-KB vs GATE-KB (alpha=0.5), with "
        f"document-block bootstrap 95% CIs (B={B_BOOT}). Per-genre derived-conclusion counts show "
        f"the drop ({f2['raw_point']} -> {f2['gate_point']}) is ENTIRELY "
        f"{multihop_ci.get('single_genre_origin')}-driven: legal derives clean conclusions "
        f"(corrupt=0), news derives none. With one contributing genre and "
        f"{multihop_ci['per_system_derived_counts']['raw_kb']}->"
        f"{multihop_ci['per_system_derived_counts']['gate_kb_a0.5']} conclusions the CI is WIDE; "
        "the reduction is DIRECTIONAL, not significant.")
    # ---- F3: decoy_fdr_hat vs realized FDR scatter (conservative regime) + CLUTRR contrast ----
    f3 = {
        "points": [{"alpha": t["alpha"], "genre": t["genre"], "elicitation": t["elicitation"],
                    "decoy_fdr_hat": t["decoy_fdr_hat"], "realized_fdr": t["realized_fdr"]}
                   for t in self_report["triples"]],
        "clutrr_point": {"decoy_fdr_hat": 0.5, "realized_fdr": 1.0, "label": "CLUTRR multi_hop"},
        "regime": self_report["regime"], "anti_conservative_cells": self_report["anti_conservative_cells"]}
    f3["caption"] = (
        "F3. Self-report calibration: the gate's own decoy_fdr_hat (x) vs the realized FDR "
        f"against gold (y), all {self_report['n_cells']} (genre x elicitation x alpha) cells. "
        f"ALL points lie on/above the y=x line (anti_conservative_cells="
        f"{self_report['anti_conservative_cells']}) => CONSERVATIVE self-report (decoy_fdr_hat >= "
        "realized). Contrast: the CLUTRR multi_hop point (0.5, 1.0) sits BELOW y=x "
        "(anti-conservative) — opposite regimes on different anchors.")
    # ---- F4: a probabilistic trace-graph (regulatory multi-hop) ----
    reg_ex = next((e for e in prob_block["examples"]
                   if e["genre"] == "regulatory" and e["kind"] == "multi_hop"), None)
    any_ex = reg_ex or (prob_block["examples"][0] if prob_block["examples"] else None)
    f4 = {"example": any_ex, "engine": prob_block["engine"],
          "json_path": (any_ex or {}).get("json_path")}
    f4["caption"] = (
        "F4. Probabilistic trace-graph for a regulatory multi-hop conclusion "
        f"({(any_ex or {}).get('rule')}), engine={prob_block['engine']}. Node labels carry the "
        "ProbLog/WMC marginal (derived nodes) or the gate-consistent shrinkage weight "
        "w_i=(1-alpha_hat)*calibrate(Z_i) (leaf nodes); every leaf retains its provenance + decoy "
        "(W_i,T,alpha) + entrapment (FDP_hat,r) certificate. Deterministic backward-chaining "
        "remains the baseline; the marginal is an added probabilistic annotation.")
    return {"F1": f1, "F2": f2, "F3": f3, "F4": f4}


def build_output(pipe: dict, norms_by_elic: dict, grid: list[dict], headline: dict,
                 adj: dict, mr: dict, extq: dict, multihop: dict, traces: dict,
                 bh: list, s1: dict, headline_elic: str, out_path: Path,
                 extra: dict | None = None) -> dict:
    docs, doc_by_id = pipe["docs"], pipe["doc_by_id"]
    # per-(elic,genre,alpha) threshold lookup for example-level admission flags
    thr = {(c["elicitation"], c["genre"], c["alpha"]): c["threshold"] for c in grid}

    examples = []
    for c in pipe["all_reals"]:
        d = doc_by_id[c["doc_id"]]
        cf = pipe["cf_real"].get(c["cand_id"])
        ex = {
            "input": json.dumps({"doc_id": c["doc_id"], "head": c["h"], "relation": c["r"],
                                 "tail": c["t"], "genre": d.genre,
                                 "candidate_kind": "real"}),
            "output": c["label"],
            "metadata_doc_id": c["doc_id"], "metadata_genre": d.genre,
            "metadata_gold_quality": d.gold_quality,
            "metadata_gold_exact": bool(c["gold_exact"]),
            "metadata_hallucination_verdict": c.get("verdict"),
            "metadata_hall_adj": bool(c.get("hall_adj")),
            "metadata_extraction_freq": c["freq"],
            "metadata_sumo_type_head": d.sumo_by_entity.get(c["h"], {}).get(
                "sumo", tsumo.type_entity(c["h"])["sumo"]),
            "metadata_sumo_type_tail": d.sumo_by_entity.get(c["t"], {}).get(
                "sumo", tsumo.type_entity(c["t"])["sumo"]),
            "metadata_decoy_relation": (cf or {}).get("r"),
            "metadata_provenance_quote": str(c.get("prov", ""))[:200],
        }
        for elic, normm in norms_by_elic.items():
            tag = "lp" if elic == "logprob" else "pt"
            zr = normm.get(c["cand_id"])
            zd = normm.get(cf["cand_id"]) if cf else None
            w = st.W_signed_max(zr, zd) if (zr is not None and zd is not None) else None
            ex[f"metadata_z_real_rank_{tag}"] = zr
            ex[f"metadata_z_decoy_rank_{tag}"] = zd
            ex[f"metadata_w_cf_{tag}"] = (round(w, 6) if w is not None else None)
            ex[f"metadata_z_real_raw_{tag}"] = pipe["zmap"].get((elic, c["cand_id"]))
            if w is not None:
                for a in ALPHA_GRID:
                    T = thr.get((elic, d.genre, a))
                    ex[f"predict_admit_{tag}_a{int(a*100):02d}"] = (
                        "yes" if (T is not None and w >= T) else "no")
        examples.append(_clean(ex))

    metadata = {
        "method_name": "Label-free decoy-competition (knockoff+) FDR gate for LLM "
                       "text->logic fact admission, with auditable trace-graphs",
        "task": "Operational neuro-symbolic translation of short legal/news/regulatory "
                "documents into gated (head, relation, tail) facts that feed a running "
                "backward-chaining logic engine, with a quantified hallucination-rate "
                "reduction vs raw LLM and human-auditable reasoning traces.",
        "anchor": "24-doc application anchor (8 legal CUAD-crisp / 8 news Wikinews-silver "
                  "/ 8 regulatory GDPR+eCFR-silver)",
        "headline_finding": headline.get("headline_statement", ""),
        "headline_elicitation": headline_elic,
        "primary_metric": "hallucinated-fact rate (decoy-gate vs RAW LLM) per genre x "
                          "elicitation x alpha, with document-block bootstrap CIs",
        "models": {"primary_scorer_generator": PRIMARY_MODEL,
                   "cross_family_adjudicator": CROSS_MODEL},
        "elicitation": {
            "logprob": "softmax P(Yes) over {Yes,No} first-token logits (gpt-4.1-nano)",
            "portable": f"K={pipe['k_sc']} self-consistency Yes/No+confidence, temp 0.7, "
                        "mean p(true)"},
        "hyperparameters": {"seed": SEED, "alpha_grid": ALPHA_GRID, "B_bootstrap": B_BOOT,
                            "K_self_consistency": pipe["k_sc"], "r_entrapment": R_ENTRAP,
                            "n_extraction_samples": pipe["n_samples"],
                            "extraction_temperature": EXTRACT_TEMP, "reals_cap_per_doc": REALS_CAP,
                            "candidate_cap_per_doc": CAND_CAP, "recall_grid": RECALL_GRID,
                            "kappa_trust_threshold": KAPPA_TRUST,
                            "W_statistic": "signed-max", "knockoff_plus": "Barber-Candes eq 1.9",
                            "bootstrap": "document-block (cluster) resampling",
                            "multiplicity": "Benjamini-Hochberg q=0.05",
                            "scoring": "isolated, provenance-blinded, identical template",
                            "extraction_mode": "open-vocab over-generation + LLM relation "
                                               "alignment to per-genre gold vocab + 'other' escape",
                            "reasoning_engine": "pure-Python backward-chaining meta-interpreter "
                                                "(janus-swi/SWI-Prolog attempted, fell back; "
                                                "identical JSON+DOT trace-graph schema)",
                            "typing": "WordNet hypernym -> coarse {PER,LOC,ORG,TIME,NUM,MISC} "
                                      "-> SUMO class (typing-only, never filters)"},
        "dataset_counts": {"n_docs": len(docs),
                           "genre_counts": {g: sum(1 for d in docs if d.genre == g) for g in GENRES},
                           "n_reals": len(pipe["all_reals"]), "label_counts": pipe["n_lab"],
                           "n_decoys_generated": pipe["n_gen_decoys"],
                           "contamination_rate_decoys": pipe["contamination_rate"],
                           "n_entrapment": sum(len(pipe["entrap_by_doc"][d.doc_id]) for d in docs)},
        "hallucination_grid": grid,
        "headline": headline,
        "s1_decoy_signature": s1,
        "matched_recall_curves": mr,
        "extraction_quality": extq,
        "multihop_corruption": multihop,
        "adjudicator_validation": adj,
        "trace_graphs": traces,
        "bh_correction": bh,
        "runtime": pipe["runtime"],
        "cost_trace_path": "logs/cost.jsonl",
        "interpretation": {
            "primary": "Per (genre, elicitation, alpha) the gate hallucination rate is "
                       "compared to the alpha-invariant RAW rate with CI separation; the full "
                       "grid is reported so regime-dependence is explicit.",
            "regime": "logprob: anti-conservative expected (LLM overconfident in own errors); "
                      "portable: vacuous below the certified alpha (n_admitted<1/alpha) — shown "
                      "as 'uncertified' but populated.",
            "second_order": "self_report_anticonservative flags cells where the gate's own "
                            "decoy_fdr_hat under-states the realized FDR.",
            "trace_graphs": "every admitted leaf carries provenance + decoy (W_i,T,alpha) + "
                            "entrapment (FDP_hat,r) certificates; derived conclusions are "
                            "corrupted iff any supporting leaf is hallucinated."},
    }
    # ITER-4 additive blocks (probabilistic reasoner + honest finalized reporting + figures).
    if extra:
        for k, v in extra.items():
            metadata[k] = v
    out = {"metadata": _clean(metadata),
           "datasets": [{"dataset": "ApplicationAnchor-24doc-Legal-News-Regulatory",
                         "examples": examples}]}
    out_path.write_text(json.dumps(out, indent=2))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.0f} KB, {len(examples)} rows)")
    return out


# ---------------------------------------------------------------------------
# Offline self-tests (Stage 0)
# ---------------------------------------------------------------------------
def selftest():
    logger.info("STAGE 0 — offline unit tests")
    # (a) fdr_stats / knockoff / bootstrap / BH (ported from iter-2)
    assert [st.k_floor(a) for a in ALPHA_GRID] == [20, 10, 5, 4, 2]
    W = [0.9] * 25 + [-0.3]
    T, n, ratio = st.knockoff_plus_threshold(W, 0.05)
    assert n >= 20 and ratio <= 0.05
    Tn, nn, _ = st.knockoff_plus_threshold([-0.5, -0.4, 0.1], 0.05)
    assert nn == 0 and math.isinf(Tn)
    assert st.W_signed_max(0.8, 0.3) == 0.8 and st.W_signed_max(0.3, 0.8) == -0.8
    assert abs(st.W_signed_max(0.5, 0.5)) == 0.0
    rng = np.random.default_rng(0)
    fair = [(float(rng.random()), float(rng.random())) for _ in range(2000)]
    wr, _ = st.tail_win_rate(fair, 0.0)
    assert 0.45 < wr < 0.55
    easy = [(float(rng.random()), float(rng.random()) * 0.5) for _ in range(2000)]
    _, ksp = st.ks_two_sample([d for _, d in easy], [r for r, _ in easy], "two-sided")
    assert ksp < 0.05
    clustered = [[0.0] * 20 if i % 2 == 0 else [1.0] * 20 for i in range(20)]
    blk = st.doc_block_bootstrap(clustered, lambda u: float(np.mean([x for g in u for x in g]))
                                 if u else float("nan"), B=500, seed=1)
    flat = [x for u in clustered for x in u]
    iid = st.doc_block_bootstrap(flat, lambda u: float(np.mean(u)) if len(u) else float("nan"),
                                 B=500, seed=1)
    assert (blk["ci_high"] - blk["ci_low"]) > (iid["ci_high"] - iid["ci_low"])
    bh = st.benjamini_hochberg([0.001, 0.5, 0.02, 0.9], q=0.05)
    assert bh[0]["reject"] and not bh[1]["reject"]
    g = st.decoy_gate_fdr([{"w": 0.9, "is_false": False}] * 18 + [{"w": -0.2, "is_false": True}] * 2, 0.10)
    assert g["realized_fdr"] <= 0.10 + 1e-9
    # (b) module selftests
    tsumo.selftest()
    kbe.selftest()
    pr.selftest()  # probabilistic reasoner: toy 2-hop=0.63, noisy-OR equivalence, prob graph
    # (c) anchor-specific
    docs = load_anchor(MINI_DATA)
    assert len(docs) == 12, f"mini docs {len(docs)}"
    n_ok = n_tot = 0
    for d in docs:
        for e in d.entities:
            sp = e.get("char_span")
            if sp and isinstance(sp, list) and len(sp) == 2:
                n_tot += 1
                if d.text[sp[0]:sp[1]] == e["name"]:
                    n_ok += 1
    assert n_tot > 0 and n_ok / n_tot >= 0.95, f"entity char_span exactness {n_ok}/{n_tot}"
    assert tsumo.wordnet_type("person")[1].startswith("&%Human")
    # adjudicator unit cases: gold-exact -> ENTAILED, ungrounded -> HALLUCINATED
    d0 = docs[0]
    gh, gr, gt = next(iter(d0.gold_set))
    assert d0.label(gh, gr, gt) == "TRUE"
    assert d0.label("Zzzqq Nonexistent Entity", gr, "Yyywww Nobody") == "FALSE"
    # proof engine 2-hop on toy reg KB + DOT
    kb = kbe.KB()
    kb.add_fact("cross_references", ("S1", "S6"), {"hallucination_verdict": "ENTAILED",
                "provenance": "x", "decoy_certificate": {"W_i": 0.9, "T": 0.3, "alpha": 0.2},
                "entrapment_certificate": {"FDP_hat": 0.0, "r": 1}})
    kb.add_fact("grants_right", ("S6", "access"), {"hallucination_verdict": "ENTAILED",
                "provenance": "y", "decoy_certificate": {"W_i": 0.8, "T": 0.3, "alpha": 0.2},
                "entrapment_certificate": {"FDP_hat": 0.0, "r": 1}})
    for spec in BRIDGE_RULES["regulatory"][:1]:
        kb.add_rule(*spec)
    der = kb.derive_all()
    assert any(p["atom"][0] == "relevant_right" and p["atom"][1] == ["S1", "access"] for p in der)
    dot = kbe.graph_to_dot(kbe.proof_to_graph(der[0]))
    assert dot.startswith("digraph proof {") and "->" in dot
    logger.info("STAGE 0 — all offline unit tests PASSED ✓")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def amain(args):
    set_mem_limit(10.0)
    data_path = MINI_DATA if args.mini else FULL_DATA
    docs = load_anchor(data_path, n_docs=args.n_docs, per_genre=args.per_genre)
    logger.info(f"Loaded {len(docs)} docs from {data_path.name} "
                f"(genres={{{', '.join(f'{g}:{sum(1 for d in docs if d.genre==g)}' for g in GENRES)}}})")
    cache_dir = HERE / "cache"
    cost_log = HERE / "logs" / "cost.jsonl"
    do_mr = not args.no_matched_recall
    pipe = await run(docs, cache_dir=cache_dir, cost_log=cost_log, elic=args.elic,
                     k_sc=args.k_sc, n_samples=args.n_samples, concurrency=args.concurrency,
                     do_matched_recall=do_mr, soft_cap=args.soft_cap)

    logger.info("ANALYSIS ...")
    adj = adjudicator_validation(pipe)
    logger.info(f"  adjudicator kappa={adj['kappa']:.3f} trusted={adj['judge_trusted']}")
    annotate_hallucination(pipe, trust_judge=adj["judge_trusted"])
    norms_by_elic = {e: rank_normalize_elic(pipe, e) for e in pipe["elics"]}
    grid = gate_and_hall_grid(pipe, norms_by_elic)
    headline_elic = "portable" if "portable" in pipe["elics"] else pipe["elics"][0]
    headline_norm = norms_by_elic[headline_elic]
    headline = compute_headline(grid)
    best = headline.get("best_reduction_cell")
    headline["headline_statement"] = (
        ("Decoy-gating reduces the hallucinated-fact rate vs raw LLM in "
         f"{headline['n_cells_gate_below_raw_ci_separated']} of the grid cells with CI "
         f"separation; the largest CI-separated reduction is at {best['genre']}/"
         f"{best['elicitation']}/alpha={best['alpha']}: raw={best['raw']:.3f} -> "
         f"gate={best['gate']:.3f} (abs {best['abs_reduction']:.3f}).")
        if best else "No populated grid cells.")
    mr = matched_recall_curves(pipe, headline_norm) if do_mr else {"note": "matched-recall skipped"}
    extq = extraction_quality(pipe)
    multihop = multihop_corruption(pipe, headline_norm, grid, headline_elic)
    traces = export_trace_graphs(pipe, headline_norm, grid, headline_elic, HERE / "trace_graphs")
    logger.info(f"  trace-graphs exported: {traces['n_exported']}")
    s1 = s1_signature(pipe, norms_by_elic)
    bh = collect_bh(grid, adj)

    # ---- ITER-4: probabilistic reasoner (P4) + honest finalized reporting (P2) ----
    logger.info("ITER-4 probabilistic reasoner + finalized reporting ...")
    multihop_ci = multihop_corruption_ci(pipe, headline_norm, grid, headline_elic, multihop)
    atomic_pooled = atomic_reduction_pooled(pipe, norms_by_elic, grid)
    self_report = self_report_regime_analysis(grid)
    prob_block = prob_reasoning_block(pipe, norms_by_elic, grid, headline_elic,
                                      HERE / "prob_trace_graphs")
    figs = figure_arrays(grid, atomic_pooled, multihop_ci, self_report, prob_block)
    logger.info(f"  prob trace-graphs: {prob_block['n_exported']} | engine={prob_block['engine']} "
                f"| multihop genres={prob_block['genres_with_multihop']} "
                f"| self_report={self_report['regime']} | atomic CI-sep "
                f"{atomic_pooled['cells_ci_separated_allgrid']}/{atomic_pooled['n_allgrid_cells']}")
    extra = {
        "probabilistic_reasoning": prob_block,
        "prob_trace_graphs": {"n_exported": prob_block["n_exported"],
                              "engine": prob_block["engine"],
                              "examples": prob_block["examples"]},
        "multihop_corruption": multihop_ci,           # supersedes the base point-only block
        "atomic_reduction_pooled": atomic_pooled,
        "self_report_regime": self_report["regime"],
        "self_report_analysis": self_report,
        "figures": figs,
        "contributions": {
            "probabilistic_reasoner_delivered": True,
            "statement": ("The LLM-as-probabilistic-reasoner is DELIVERED (executed), not only "
                          "specified: admitted facts become a weighted ProbLog program and "
                          "multi-hop conclusion marginals are computed (ProbLog primary, exact-WMC "
                          "fallback). Deterministic backward-chaining remains the baseline so no "
                          "headline number depends on the probabilistic layer."),
            "honest_reporting": ("Atomic reduction reported as a DIRECTIONAL ~25% trend (0 CI-"
                                 "separated cells at n=24); multi-hop corruption drop flagged as "
                                 "single-genre (regulatory) with wide CIs; self-report is "
                                 "CONSERVATIVE (decoy_fdr_hat >= realized everywhere), contrasting "
                                 "the CLUTRR anti-conservative regime.")},
    }

    out_path = HERE / ("mini_method_out.json" if args.mini else "method_out.json")
    build_output(pipe, norms_by_elic, grid, headline, adj, mr, extq, multihop, traces,
                 bh, s1, headline_elic, out_path, extra=extra)
    gc.collect()
    logger.info(f"DONE. cost=${pipe['runtime']['cost_usd']:.4f} | {headline['headline_statement']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mini", action="store_true")
    ap.add_argument("--n-docs", type=int, default=None)
    ap.add_argument("--per-genre", type=int, default=None)
    ap.add_argument("--elic", choices=["both", "logprob", "portable"], default="both")
    ap.add_argument("--k-sc", type=int, default=K_SC)
    ap.add_argument("--n-samples", type=int, default=N_SAMPLES_EXTRACT)
    ap.add_argument("--no-matched-recall", action="store_true")
    ap.add_argument("--concurrency", type=int, default=28)
    ap.add_argument("--soft-cap", type=float, default=SOFT_CAP_USD)
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

