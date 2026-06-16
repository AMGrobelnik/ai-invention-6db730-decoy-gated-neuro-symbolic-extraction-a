#!/usr/bin/env python3
"""Shared config, cost meter, parsing helpers, embedding + alignment core for the
Re-DocRED operational-wedge experiment (decoy-gating vs plain confidence threshold).

This module is imported by both the extraction stage (method.py --stage extract)
and the analysis stage (method.py --stage analyze).
"""
from __future__ import annotations

import json
import math
import re
import sys
import threading
from pathlib import Path

from loguru import logger

# --------------------------------------------------------------------------------------
# PATHS
# --------------------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent
DEP_DATA_DIR = Path(
    "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2"
)
FULL_DATA = DEP_DATA_DIR / "full_data_out.json"
MINI_DATA = DEP_DATA_DIR / "mini_data_out.json"
RELATION_SCHEMA = DEP_DATA_DIR / "relation_schema.json"
ENTITY_TYPE_SCHEMA = DEP_DATA_DIR / "entity_type_schema.json"

CKPT_DIR = WORKSPACE / "checkpoints"
LOGS_DIR = WORKSPACE / "logs"
CACHE_DIR = WORKSPACE / "cache"
for _d in (CKPT_DIR, LOGS_DIR, CACHE_DIR):
    _d.mkdir(parents=True, exist_ok=True)

COST_LOG = LOGS_DIR / "cost.jsonl"
ALIGN_CACHE_FILE = CACHE_DIR / "align_relation_cache.json"
PCODE_EMB_FILE = CACHE_DIR / "pcode_embeddings.npz"

# --------------------------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------------------------
CONFIG = dict(
    model_primary="openai/gpt-4.1-nano",
    model_fallbacks=["openai/gpt-4o-mini"],
    # extraction / scoring
    temperature_extract=0.7,
    n_overgen=3,
    cand_cap=30,
    temperature_score=0.0,
    temperature_decoy=0.9,
    temperature_align=0.0,
    elicitation="logprob_yes_token (verbalized_[0,1] fallback)",
    n_conf_samples=5,
    decoy_max_regen=3,
    # FDR gate
    alpha_grid=[0.05, 0.10, 0.20, 0.30, 0.50],
    W_floor_k={0.05: 20, 0.10: 10, 0.20: 5, 0.30: 4, 0.50: 2},
    # alignment / entity linking
    align_shortlist_k=8,
    align_embed_floor=0.45,
    el_embed_floor=0.6,
    el_strict_floor=0.7,
    conf_match_floor=0.7,
    # evaluation
    bootstrap_B=2000,
    recall_grid_n=25,
    noise_levels=[0.05, 0.10, 0.20],
    # multi-hop power (P3): target #derived conclusions per compared system; below this the
    # hallucinated-conclusion comparison is flagged UNDERPOWERED with exact counts.
    power_target=100,
    # regime-diagnostic (P3, label-free)
    regime_low_f=0.40,          # self-consistency freq <= this => label-free spontaneous-error proxy
    regime_tail_quantiles=[0.25, 0.50],  # gold-free operative-tail cutoffs (top-q by max(Z,Zt))
    regime_exch_band=0.15,      # |winrate_tail-0.5|<=band => decoys EXCHANGEABLE
    regime_calib_auc_hi=0.65,   # base-scorer calibration AUC >= this => "calibrated" axis
    regime_rho_null=0.97,       # admission-region Spearman(W,Z) >= this => gate cannot re-rank
    regime_jaccard_null=0.95,   # admitted-set Jaccard >= this => null wedge predicted
    # budget / concurrency
    soft_cap_usd=2.0,
    hard_stop_usd=10.0,
    global_concurrency=32,
    doc_concurrency=10,
    seed=20240617,
    embed_model="sentence-transformers/all-MiniLM-L6-v2",
)

# gpt-4.1-nano fallback pricing (USD per token) if usage.cost ever missing
PRICE = {
    "openai/gpt-4.1-nano": (0.10e-6, 0.40e-6),
    "openai/gpt-4o-mini": (0.15e-6, 0.60e-6),
}

# Multi-hop Datalog rules over Re-DocRED relations (gold-justified, well-known).
# Each: name, body list of (pcode, var_head, var_tail), head (pcode, var_head, var_tail).
RULES = [
    {"name": "transitive_located_in_admin (P131;P131->P131)",
     "body": [("P131", "X", "Y"), ("P131", "Y", "Z")], "head": ("P131", "X", "Z")},
    {"name": "located_in_admin_then_country (P131;P17->P17)",
     "body": [("P131", "X", "Y"), ("P17", "Y", "Z")], "head": ("P17", "X", "Z")},
    {"name": "transitive_contains_admin (P150;P150->P150)",
     "body": [("P150", "X", "Y"), ("P150", "Y", "Z")], "head": ("P150", "X", "Z")},
    {"name": "transitive_part_of (P361;P361->P361)",
     "body": [("P361", "X", "Y"), ("P361", "Y", "Z")], "head": ("P361", "X", "Z")},
    {"name": "transitive_has_part (P527;P527->P527)",
     "body": [("P527", "X", "Y"), ("P527", "Y", "Z")], "head": ("P527", "X", "Z")},
    {"name": "sibling_shares_father (P3373;P22->P22)",
     "body": [("P3373", "X", "Y"), ("P22", "Y", "Z")], "head": ("P22", "X", "Z")},
    {"name": "sibling_shares_mother (P3373;P25->P25)",
     "body": [("P3373", "X", "Y"), ("P25", "Y", "Z")], "head": ("P25", "X", "Z")},
    {"name": "capital_of_implies_located_in (P36->P131)",
     "body": [("P36", "X", "Y")], "head": ("P131", "X", "Y")},
    {"name": "sibling_symmetric (P3373->P3373)",
     "body": [("P3373", "X", "Y")], "head": ("P3373", "Y", "X")},
    {"name": "spouse_symmetric (P26->P26)",
     "body": [("P26", "X", "Y")], "head": ("P26", "Y", "X")},
    # --- P3: extra well-known gold-justified Wikidata inverse properties (densify the
    #     derived-conclusion count toward power_target; both METHOD & PLAIN use them). ---
    {"name": "father_implies_child (P22->P40 inverse)",
     "body": [("P22", "X", "Y")], "head": ("P40", "Y", "X")},
    {"name": "mother_implies_child (P25->P40 inverse)",
     "body": [("P25", "X", "Y")], "head": ("P40", "Y", "X")},
    {"name": "part_of_implies_has_part (P361->P527 inverse)",
     "body": [("P361", "X", "Y")], "head": ("P527", "Y", "X")},
    {"name": "has_part_implies_part_of (P527->P361 inverse)",
     "body": [("P527", "X", "Y")], "head": ("P361", "Y", "X")},
    {"name": "located_in_admin_inverse_contains (P131->P150 inverse)",
     "body": [("P131", "X", "Y")], "head": ("P150", "Y", "X")},
    {"name": "contains_admin_inverse_located_in (P150->P131 inverse)",
     "body": [("P150", "X", "Y")], "head": ("P131", "Y", "X")},
]


# --------------------------------------------------------------------------------------
# LOGGING
# --------------------------------------------------------------------------------------
def setup_logging(tag: str = "run") -> None:
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    logger.add(LOGS_DIR / f"{tag}.log", rotation="30 MB", level="DEBUG", enqueue=True)


# --------------------------------------------------------------------------------------
# COST METER  (thread/async safe; OpenRouter returns exact usage.cost in USD)
# --------------------------------------------------------------------------------------
class BudgetExceeded(Exception):
    pass


class CostMeter:
    def __init__(self, hard_stop: float, soft_cap: float, persist: bool = True):
        self.hard_stop = hard_stop
        self.soft_cap = soft_cap
        self.total = 0.0
        self.n_calls = 0
        self._lock = threading.Lock()
        self._persist = persist
        # resume cumulative total across stages/runs from cost.jsonl
        if persist and COST_LOG.exists():
            try:
                for line in COST_LOG.read_text().splitlines():
                    rec = json.loads(line)
                    self.total = rec.get("cumulative", self.total)
                    self.n_calls += 1
                logger.info(f"Resumed cost meter: ${self.total:.4f} over {self.n_calls} prior calls")
            except Exception:
                logger.warning("Could not parse existing cost.jsonl; starting fresh counter")

    def add(self, usage: dict, model: str, tag: str = "") -> float:
        cost = usage.get("cost")
        if cost is None:
            pin, pout = PRICE.get(model, (0.10e-6, 0.40e-6))
            cost = usage.get("prompt_tokens", 0) * pin + usage.get("completion_tokens", 0) * pout
        with self._lock:
            self.total += cost
            self.n_calls += 1
            cum = self.total
            n = self.n_calls
        if self._persist:
            with self._lock:
                with COST_LOG.open("a") as f:
                    f.write(json.dumps({"tag": tag, "cost": cost, "cumulative": cum,
                                        "model": model, "n": n}) + "\n")
        if cum >= self.hard_stop:
            raise BudgetExceeded(f"HARD STOP: cumulative ${cum:.4f} >= ${self.hard_stop}")
        return cost

    def over_soft(self) -> bool:
        return self.total >= self.soft_cap


# --------------------------------------------------------------------------------------
# PARSING HELPERS (robust to LLM formatting noise)
# --------------------------------------------------------------------------------------
_FENCE = re.compile(r"^```[a-zA-Z]*\n?|```$", re.MULTILINE)


def strip_fences(s: str) -> str:
    return _FENCE.sub("", s).strip()


def parse_json_obj(text: str):
    """Extract the first JSON object from a possibly noisy LLM response."""
    if not text:
        return None
    t = strip_fences(text)
    try:
        return json.loads(t)
    except Exception:
        pass
    # find first {...} balanced
    start = t.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(t)):
            if t[i] == "{":
                depth += 1
            elif t[i] == "}":
                depth -= 1
                if depth == 0:
                    frag = t[start:i + 1]
                    try:
                        return json.loads(frag)
                    except Exception:
                        break
        start = t.find("{", start + 1)
    return None


def parse_prob(text: str) -> float | None:
    """Parse a probability in [0,1] from an LLM response (json {'p':..} or bare number)."""
    obj = parse_json_obj(text)
    if isinstance(obj, dict):
        for k in ("p", "probability", "prob", "confidence", "score"):
            if k in obj:
                try:
                    v = float(obj[k])
                    if v > 1.0:  # model may give 0..100
                        v = v / 100.0
                    return min(1.0, max(0.0, v))
                except Exception:
                    pass
    if text:
        m = re.search(r"(\d+\.\d+|\d+)", strip_fences(text))
        if m:
            try:
                v = float(m.group(1))
                if v > 1.0:
                    v = v / 100.0
                return min(1.0, max(0.0, v))
            except Exception:
                return None
    return None


_YES = {"yes", "y", "true", "yeah", "yep", "supported", "entailed", "correct"}
_NO = {"no", "n", "false", "nope", "not", "unsupported", "incorrect"}


def parse_yes_logprob(lp) -> float | None:
    """Graded P(yes) from the first-token top_logprobs of a yes/no entailment prompt."""
    if not isinstance(lp, dict):
        return None
    content = lp.get("content")
    if not content:
        return None
    tok = content[0]
    tops = tok.get("top_logprobs") or []
    yes = no = 0.0
    for o in tops:
        t = (o.get("token") or "").strip().lower()
        try:
            p = math.exp(o.get("logprob", -50.0))
        except Exception:
            continue
        if t in _YES:
            yes += p
        elif t in _NO:
            no += p
    if yes + no > 0:
        return yes / (yes + no)
    t0 = (tok.get("token") or "").strip().lower()
    if t0[:1] == "y":
        return 0.85
    if t0[:1] == "n":
        return 0.15
    return None


def parse_triples_jsonl(text: str) -> list[dict]:
    """Parse a list of {head,relation,tail,(confidence)} triples from JSONL or a JSON array."""
    if not text:
        return []
    t = strip_fences(text)
    out = []
    # try whole-text JSON array first
    try:
        arr = json.loads(t)
        if isinstance(arr, list):
            for o in arr:
                if isinstance(o, dict):
                    out.append(o)
            if out:
                return _clean_triples(out)
    except Exception:
        pass
    for line in t.splitlines():
        line = line.strip().rstrip(",")
        if not line or not line.startswith("{"):
            continue
        try:
            o = json.loads(line)
            if isinstance(o, dict):
                out.append(o)
        except Exception:
            continue
    return _clean_triples(out)


def _clean_triples(raw: list[dict]) -> list[dict]:
    out = []
    for o in raw:
        h = o.get("head") or o.get("subject") or o.get("h")
        r = o.get("relation") or o.get("rel") or o.get("r") or o.get("relation_phrase")
        ta = o.get("tail") or o.get("object") or o.get("t")
        if not (h and r and ta):
            continue
        rec = {"head": str(h).strip(), "relation": str(r).strip(), "tail": str(ta).strip()}
        if "confidence" in o or "conf" in o or "p" in o:
            try:
                c = float(o.get("confidence", o.get("conf", o.get("p"))))
                if c > 1.0:
                    c = c / 100.0
                rec["confidence"] = min(1.0, max(0.0, c))
            except Exception:
                rec["confidence"] = 0.5
        for tk in ("head_type", "tail_type"):
            if tk in o:
                rec[tk] = str(o[tk]).strip().upper()
        out.append(rec)
    return out


# --------------------------------------------------------------------------------------
# NORMALIZATION
# --------------------------------------------------------------------------------------
_PUNCT = re.compile(r"[^\w\s]")
_WS = re.compile(r"\s+")
_STOP_PREFIX = re.compile(r"^(the|a|an|los|las|el|la)\s+", re.IGNORECASE)


def norm(s: str) -> str:
    if not s:
        return ""
    s = s.lower().strip()
    s = _PUNCT.sub(" ", s)
    s = _STOP_PREFIX.sub("", s)
    s = _WS.sub(" ", s).strip()
    return s


# --------------------------------------------------------------------------------------
# DATA LOADING (slim projection of only required fields)
# --------------------------------------------------------------------------------------
def load_docs(data_path: Path, split_role: str | None, limit: int | None) -> list[dict]:
    """Load Re-DocRED examples, projecting only the fields we need."""
    logger.info(f"Loading data from {data_path} (split_role={split_role}, limit={limit})")
    blob = json.loads(data_path.read_text())
    examples = blob["datasets"][0]["examples"]
    docs = []
    for ex in examples:
        role = ex.get("metadata_split_role")
        if split_role and role != split_role:
            continue
        gold = ex.get("metadata_gold_triples", [])
        ents = ex.get("metadata_entities", [])
        docs.append({
            "doc_id": ex.get("metadata_id"),
            "title": ex.get("metadata_title"),
            "fold": ex.get("metadata_fold"),
            "split_role": role,
            "input": ex.get("input", ""),
            "sent_char_offsets": ex.get("metadata_sent_char_offsets", []),
            "entities": [{
                "entity_id": e["entity_id"],
                "type": e.get("type", "MISC"),
                "canonical_name": e.get("canonical_name", ""),
                "aliases": list({m.get("name", "") for m in e.get("mentions", [])}
                                | {e.get("canonical_name", "")}),
            } for e in ents],
            "gold_triples": [{
                "head_id": g["head_id"], "tail_id": g["tail_id"],
                "relation_pid": g["relation_pid"], "relation_name": g.get("relation_name", ""),
                "head_name": g.get("head_name", ""), "tail_name": g.get("tail_name", ""),
                "head_type": g.get("head_type", "MISC"), "tail_type": g.get("tail_type", "MISC"),
            } for g in gold],
        })
        if limit and len(docs) >= limit:
            break
    del blob
    logger.info(f"Loaded {len(docs)} docs")
    return docs


def load_relation_schema() -> list[dict]:
    return json.loads(RELATION_SCHEMA.read_text())


# --------------------------------------------------------------------------------------
# EMBEDDING MODEL + alignment primitives  (CPU, sentence-transformers MiniLM)
# --------------------------------------------------------------------------------------
class Embedder:
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        import numpy as np
        self.np = np
        logger.info(f"Loading embedding model {CONFIG['embed_model']} (CPU)")
        self.model = SentenceTransformer(CONFIG["embed_model"], device="cpu")
        self._cache: dict[str, "np.ndarray"] = {}

    def encode(self, texts: list[str]):
        return self.model.encode(texts, normalize_embeddings=True, convert_to_numpy=True,
                                 show_progress_bar=False, batch_size=64)

    def encode_cached(self, texts: list[str]):
        np = self.np
        missing = [t for t in texts if t not in self._cache]
        if missing:
            embs = self.encode(missing)
            for t, e in zip(missing, embs):
                self._cache[t] = e
        return np.vstack([self._cache[t] for t in texts])


def build_pcode_embeddings(embedder: Embedder, rel_schema: list[dict]):
    """Precompute (and cache to disk) the 96 P-code embeddings from name + description."""
    np = embedder.np
    pcodes = [r["relation_pid"] for r in rel_schema]
    if PCODE_EMB_FILE.exists():
        z = np.load(PCODE_EMB_FILE, allow_pickle=True)
        if list(z["pcodes"]) == pcodes:
            logger.info("Loaded cached P-code embeddings")
            return pcodes, z["emb"], {r["relation_pid"]: r for r in rel_schema}
    texts = [f"{r['relation_name']}: {r['relation_description']}" for r in rel_schema]
    emb = embedder.encode(texts)
    np.savez(PCODE_EMB_FILE, pcodes=np.array(pcodes), emb=emb)
    logger.info(f"Computed {len(pcodes)} P-code embeddings")
    return pcodes, emb, {r["relation_pid"]: r for r in rel_schema}
