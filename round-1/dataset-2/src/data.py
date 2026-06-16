#!/usr/bin/env python3
"""data.py — single entrypoint that standardizes Re-DocRED into the operational anchor dataset.

Run:  uv run data.py   (deps declared in pyproject.toml: numpy, scikit-learn, jsonschema, loguru)

Pipeline (pure CPU, raw data only — NO experiment outputs/scores/decoys/FDR):
  1. Acquire Re-DocRED (cached under temp/datasets/redocred_raw, else download from HF resolve URLs).
  2. Build the shared 96-relation inventory (cached Wikidata names+descriptions, else query Wikidata API).
  3. Standardize each of the 4053 documents -> reconstructed text, full entity inventory (exact char
     spans), gold (h,r,t) triples in a shared canonical schema with evidence, per-document S5 features.
  4. Cluster (primary: dominant-entity-type collapsed to 4 folds; secondary: k-means), select a
     balanced confirmatory/pilot/reserve split, assemble exp_sel_data_out rows.
  5. Validate every row against a custom row JSON-Schema; emit full/mini/preview + companion files.

THE single chosen dataset is Re-DocRED (Tan et al., EMNLP 2022) — the plan's mandated single source.
"""
from __future__ import annotations

import json
import resource
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

import jsonschema
import numpy as np
from loguru import logger
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ----------------------------------------------------------------------------- paths / limits
WS = Path(__file__).resolve().parent
RAW = WS / "temp/datasets/redocred_raw"
LOGS = WS / "logs"
RAW.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOGS / "data.log"), rotation="30 MB", level="DEBUG")

resource.setrlimit(resource.RLIMIT_AS, (8 * 1024**3, 8 * 1024**3))  # 8GB cap; data ~25MB, never OOM

SEED = 20240617
KMEANS_K = 5
KMEANS_RS = 42
TOP_REL_K = 20
ENTITY_TYPES = ["PER", "ORG", "LOC", "TIME", "NUM", "MISC"]
TYPE_PRIORITY = {"PER": 0, "ORG": 1, "LOC": 2, "MISC": 3, "TIME": 4, "NUM": 5}
N_CONF, N_PILOT, N_RESERVE = 38, 9, 12  # per cluster -> 152 / 36 / 48

HF_BASE = "https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main"
GH_BASE = "https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data"
FILES = [("train_revised.json", "train"), ("dev_revised.json", "dev"), ("test_revised.json", "test")]
EXPECT_COUNTS = {"train": 3053, "dev": 500, "test": 500}

ENTITY_TYPE_GLOSS = {
    "PER": "Person — individuals, real or fictional (e.g. Wilfried Schneider).",
    "ORG": "Organization — companies, institutions, bands, teams, agencies (e.g. Zest Airways).",
    "LOC": "Location — geopolitical entities, places, geographic features (e.g. Philippines).",
    "TIME": "Time — dates, years, periods (e.g. 2013, 13 March).",
    "NUM": "Number — numeric quantities not otherwise typed (e.g. 24, 1.2 million).",
    "MISC": "Miscellaneous — named entities not covered above: creative works, events, products, nationalities, etc.",
}

NO_SPACE_BEFORE = {
    ",", ".", "!", "?", ";", ":", ")", "]", "}", "%", "''", "”", "’", "…",
    "'s", "'S", "'re", "'ve", "'ll", "'d", "'m", "n't", "N'T", "'t", "'",
}
NO_SPACE_AFTER = {"(", "[", "{", "``", "“", "`", "$", "#"}

REL_NAME: dict[str, str] = {}  # filled in main


# ----------------------------------------------------------------------------- STEP 1: acquire
def _fetch(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "aii-redocred-prep/1.0"})
        data = urllib.request.urlopen(req, timeout=120).read()
        dest.write_bytes(data)
        return True
    except Exception as e:  # noqa: BLE001
        logger.warning(f"fetch failed {url}: {e}")
        return False


def acquire():
    for fname, _ in FILES:
        dest = RAW / fname
        if dest.exists() and dest.stat().st_size > 1_000_000:
            logger.info(f"cached {fname} ({dest.stat().st_size} bytes)")
            continue
        if not _fetch(f"{HF_BASE}/{fname}", dest):  # primary: HF
            logger.info(f"HF failed, GitHub fallback for {fname}")
            if not _fetch(f"{GH_BASE}/{fname}", dest):  # fallback A: GitHub raw
                raise SystemExit(f"Could not download {fname} from HF or GitHub")
        logger.info(f"downloaded {fname} ({dest.stat().st_size} bytes)")


# ----------------------------------------------------------------------------- STEP 3: relation inventory
def build_relation_schema(pids: list[str]) -> dict:
    cache = RAW / "relation_schema_wikidata.json"
    if cache.exists():
        schema = json.loads(cache.read_text())
        if all(p in schema and schema[p].get("relation_name") for p in pids):
            logger.info(f"cached relation schema ({len(schema)})")
            return schema
    logger.info(f"querying Wikidata for {len(pids)} P-ids")
    schema: dict = {}
    for i in range(0, len(pids), 50):
        grp = pids[i:i + 50]
        url = ("https://www.wikidata.org/w/api.php?action=wbgetentities&ids="
               + urllib.parse.quote("|".join(grp)) + "&props=labels|descriptions&languages=en&format=json")
        data = {"entities": {}}
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "aii-redocred-prep/1.0 (research)"})
                data = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
                break
            except Exception as e:  # noqa: BLE001
                logger.warning(f"wikidata retry {attempt}: {e}")
                time.sleep(2 * (attempt + 1))
        for pid, ent in data.get("entities", {}).items():
            schema[pid] = {
                "relation_pid": pid,
                "relation_name": ent.get("labels", {}).get("en", {}).get("value"),
                "relation_description": ent.get("descriptions", {}).get("en", {}).get("value"),
            }
        time.sleep(0.3)
    cache.write_text(json.dumps(schema, indent=2, ensure_ascii=False))
    return schema


# ----------------------------------------------------------------------------- STEP 4: standardize
def detokenize(tokens: list[str]):
    """Deterministic detok -> (sentence_string, per-token half-open [start,end) char spans)."""
    s, spans, suppress_next, dq_open = "", [], False, True
    for tok in tokens:
        if s == "":
            sep = ""
        elif suppress_next:
            sep = ""
        elif tok in NO_SPACE_BEFORE:
            sep = ""
        elif tok == '"':
            sep = "" if not dq_open else " "
        else:
            sep = " "
        s += sep
        start = len(s)
        s += tok
        spans.append((start, len(s)))
        if tok in NO_SPACE_AFTER:
            suppress_next = True
        elif tok == '"':
            suppress_next = dq_open
            dq_open = not dq_open
        else:
            suppress_next = False
    return s, spans


def reconstruct(sents):
    sent_strings, per_sent_spans = [], []
    for toks in sents:
        st, sp = detokenize(toks)
        sent_strings.append(st)
        per_sent_spans.append(sp)
    offsets, cur = [], 0
    for st in sent_strings:
        offsets.append(cur)
        cur += len(st) + 1
    return " ".join(sent_strings), offsets, per_sent_spans, sent_strings


def entity_type_of(mentions):
    c = Counter(m["type"] for m in mentions)
    return max(c.items(), key=lambda kv: (kv[1], -TYPE_PRIORITY.get(kv[0], 99)))[0]


def canonical_name(mentions):
    c = Counter(m["name"] for m in mentions)
    return max(c.items(), key=lambda kv: (kv[1], len(kv[0])))[0]


def char_span_for(pos, sent_id, offsets, per_sent_spans):
    try:
        spans = per_sent_spans[sent_id]
        s_tok, e_tok = pos[0], pos[1] - 1
        if not (0 <= s_tok < len(spans)) or not (0 <= e_tok < len(spans)):
            return None
        return [offsets[sent_id] + spans[s_tok][0], offsets[sent_id] + spans[e_tok][1]]
    except Exception:  # noqa: BLE001 — char span is convenience; token pos is authoritative
        return None


def process_document(doc, split_origin, orig_index):
    sents = doc["sents"]
    text, offsets, per_sent_spans, sent_strings = reconstruct(sents)
    entities, total_mentions, etype_counts = [], 0, Counter()
    for i, mentions in enumerate(doc["vertexSet"]):
        etype = entity_type_of(mentions)
        etype_counts[etype] += 1
        ms = [{"name": m["name"], "sent_id": m["sent_id"], "pos": list(m["pos"]),
               "char_span": char_span_for(list(m["pos"]), m["sent_id"], offsets, per_sent_spans)}
              for m in mentions]
        total_mentions += len(ms)
        entities.append({"entity_id": i, "type": etype, "canonical_name": canonical_name(mentions),
                         "n_mentions": len(ms), "mentions": ms})

    seen, gold = set(), []
    for lab in doc["labels"]:
        h, t, r = lab["h"], lab["t"], lab["r"]
        if (h, r, t) in seen:
            continue
        seen.add((h, r, t))
        ev = list(lab.get("evidence", []) or [])
        gold.append({
            "head_id": h, "head_name": entities[h]["canonical_name"] if h < len(entities) else None,
            "head_type": entities[h]["type"] if h < len(entities) else None,
            "relation_pid": r, "relation_name": REL_NAME.get(r, r),
            "tail_id": t, "tail_name": entities[t]["canonical_name"] if t < len(entities) else None,
            "tail_type": entities[t]["type"] if t < len(entities) else None,
            "evidence_sent_ids": ev,
            "evidence_text": [sent_strings[s] for s in ev if 0 <= s < len(sent_strings)],
        })

    num_words = sum(len(s) for s in sents)
    num_sents, num_entities, num_triples = len(sents), len(entities), len(gold)
    rel_counts = Counter(g["relation_pid"] for g in gold)
    etc = {tp: int(etype_counts.get(tp, 0)) for tp in ENTITY_TYPES}
    dominant = max(ENTITY_TYPES, key=lambda tp: (etc[tp], -TYPE_PRIORITY[tp])) if num_entities else "MISC"
    multi_ev = sum(1 for g in gold if len(g["evidence_sent_ids"]) > 1)
    gaps = [max(g["evidence_sent_ids"]) - min(g["evidence_sent_ids"]) for g in gold if g["evidence_sent_ids"]]
    singletons = sum(1 for e in entities if e["n_mentions"] == 1)
    features = {
        "num_words": num_words, "num_chars": len(text), "num_sents": num_sents,
        "num_entities": num_entities, "num_triples": num_triples,
        "num_relation_types_present": len(rel_counts),
        "num_entity_types_present": sum(1 for tp in ENTITY_TYPES if etc[tp] > 0),
        "entity_type_counts": etc, "dominant_entity_type": dominant,
        "relation_pid_counts": dict(rel_counts),
        "avg_mentions_per_entity": (total_mentions / num_entities) if num_entities else 0.0,
        "entity_density": (num_entities / num_words) if num_words else 0.0,
        "mention_density": (total_mentions / num_words) if num_words else 0.0,
        "triple_density": (num_triples / num_sents) if num_sents else 0.0,
        "frac_singleton_entities": (singletons / num_entities) if num_entities else 0.0,
        "frac_multi_evidence_triples": (multi_ev / num_triples) if num_triples else 0.0,
        "max_evidence_sentence_gap": int(max(gaps)) if gaps else 0,
    }
    return {"id": f"redocred_{split_origin}_{orig_index}", "title": doc["title"], "text": text,
            "sents": sents, "sent_char_offsets": offsets, "entities": entities, "gold_triples": gold,
            "split_origin": split_origin, "orig_index": orig_index, "features": features}


# ----------------------------------------------------------------------------- STEP 6/7 helpers
def primary_cluster(dominant):
    return {"PER": "cluster_PER", "ORG": "cluster_ORG", "LOC": "cluster_LOC"}.get(dominant, "cluster_MISC")


def even_pick(items, n):
    if n <= 0 or not items:
        return []
    if n >= len(items):
        return list(items)
    idx = sorted(set(int(round(x)) for x in np.linspace(0, len(items) - 1, n)))
    i = 0
    while len(idx) < n and i < len(items):
        if i not in idx:
            idx.append(i)
        i += 1
    return [items[i] for i in sorted(idx)[:n]]


# ----------------------------------------------------------------------------- STEP 9: custom row schema
def build_row_schema():
    mention = {"type": "object", "required": ["name", "sent_id", "pos", "char_span"], "additionalProperties": False,
               "properties": {"name": {"type": "string"}, "sent_id": {"type": "integer", "minimum": 0},
                              "pos": {"type": "array", "items": {"type": "integer"}, "minItems": 2, "maxItems": 2},
                              "char_span": {"oneOf": [{"type": "null"},
                                                      {"type": "array", "items": {"type": "integer"},
                                                       "minItems": 2, "maxItems": 2}]}}}
    entity = {"type": "object", "required": ["entity_id", "type", "canonical_name", "n_mentions", "mentions"],
              "additionalProperties": False,
              "properties": {"entity_id": {"type": "integer", "minimum": 0},
                             "type": {"enum": ENTITY_TYPES}, "canonical_name": {"type": "string"},
                             "n_mentions": {"type": "integer", "minimum": 1},
                             "mentions": {"type": "array", "minItems": 1, "items": mention}}}
    triple = {"type": "object", "additionalProperties": False,
              "required": ["head_id", "head_name", "head_type", "relation_pid", "relation_name",
                           "tail_id", "tail_name", "tail_type", "evidence_sent_ids", "evidence_text"],
              "properties": {"head_id": {"type": "integer", "minimum": 0},
                             "head_name": {"type": ["string", "null"]}, "head_type": {"type": ["string", "null"]},
                             "relation_pid": {"type": "string", "pattern": "^P[0-9]+$"},
                             "relation_name": {"type": "string"}, "tail_id": {"type": "integer", "minimum": 0},
                             "tail_name": {"type": ["string", "null"]}, "tail_type": {"type": ["string", "null"]},
                             "evidence_sent_ids": {"type": "array", "items": {"type": "integer"}},
                             "evidence_text": {"type": "array", "items": {"type": "string"}}}}
    return {
        "$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "additionalProperties": False,
        "required": ["input", "output", "metadata_fold", "metadata_id", "metadata_split_origin",
                     "metadata_orig_index", "metadata_split_role", "metadata_is_confirmatory",
                     "metadata_is_pilot", "metadata_is_reserve", "metadata_kmeans_cluster",
                     "metadata_cluster_scheme", "metadata_seed", "metadata_sents", "metadata_sent_char_offsets",
                     "metadata_entities", "metadata_gold_triples", "metadata_features", "metadata_gold_caveat",
                     "metadata_title"],
        "properties": {
            "input": {"type": "string", "minLength": 1}, "output": {"type": "string", "minLength": 1},
            "metadata_fold": {"enum": ["cluster_PER", "cluster_ORG", "cluster_LOC", "cluster_MISC"]},
            "metadata_id": {"type": "string", "pattern": "^redocred_(train|dev|test)_[0-9]+$"},
            "metadata_title": {"type": "string"}, "metadata_split_origin": {"enum": ["train", "dev", "test"]},
            "metadata_orig_index": {"type": "integer", "minimum": 0},
            "metadata_split_role": {"enum": ["confirmatory", "pilot", "reserve"]},
            "metadata_is_confirmatory": {"type": "boolean"}, "metadata_is_pilot": {"type": "boolean"},
            "metadata_is_reserve": {"type": "boolean"}, "metadata_kmeans_cluster": {"type": "integer", "minimum": 0},
            "metadata_cluster_scheme": {"type": "string"}, "metadata_seed": {"type": "integer"},
            "metadata_sents": {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
            "metadata_sent_char_offsets": {"type": "array", "items": {"type": "integer"}},
            "metadata_entities": {"type": "array", "minItems": 1, "items": entity},
            "metadata_gold_triples": {"type": "array", "items": triple},
            "metadata_features": {"type": "object", "additionalProperties": True,
                                  "required": ["num_words", "num_chars", "num_sents", "num_entities", "num_triples",
                                               "num_relation_types_present", "num_entity_types_present",
                                               "entity_type_counts", "dominant_entity_type", "relation_pid_counts",
                                               "avg_mentions_per_entity", "entity_density", "mention_density",
                                               "triple_density", "frac_singleton_entities",
                                               "frac_multi_evidence_triples", "max_evidence_sentence_gap"]},
            "metadata_gold_caveat": {"type": "string"},
        },
    }


# ----------------------------------------------------------------------------- main
@logger.catch(reraise=True)
def main():
    global REL_NAME
    acquire()

    # load + parse (STEP 1/2)
    rows, pid_set = [], set()
    for fname, origin in FILES:
        docs = json.loads((RAW / fname).read_text())
        assert isinstance(docs, list) and len(docs) == EXPECT_COUNTS[origin], f"{fname} count drift"
        d0 = docs[0]
        assert {"title", "sents", "vertexSet", "labels"} <= set(d0), f"{fname} schema drift"
        logger.info(f"{fname}: {len(docs)} docs (schema OK)")
        for idx, doc in enumerate(docs):
            for lab in doc["labels"]:
                pid_set.add(lab["r"])
    pids = sorted(pid_set)

    rel_schema_wd = build_relation_schema(pids)
    REL_NAME = {p: (rel_schema_wd.get(p, {}).get("relation_name") or p) for p in pids}
    logger.info(f"relation inventory: {len(REL_NAME)} P-ids (e.g. P26={REL_NAME.get('P26')})")

    for fname, origin in FILES:
        for idx, doc in enumerate(json.loads((RAW / fname).read_text())):
            rows.append(process_document(doc, origin, idx))
    logger.info(f"standardized {len(rows)} documents")

    # secondary k-means (STEP 6)
    corpus_rel = Counter()
    for r in rows:
        corpus_rel.update(r["features"]["relation_pid_counts"])
    top_rels = [p for p, _ in corpus_rel.most_common(TOP_REL_K)]
    rel_index = {p: i for i, p in enumerate(top_rels)}
    feats = []
    for r in rows:
        f = r["features"]
        et = np.array([f["entity_type_counts"][tp] for tp in ENTITY_TYPES], dtype=float)
        et = et / et.sum() if et.sum() else et
        rv = np.zeros(len(top_rels)); tot = 0
        for p, c in f["relation_pid_counts"].items():
            if p in rel_index:
                rv[rel_index[p]] += c; tot += c
        if tot:
            rv = rv / tot
        feats.append(np.concatenate([et, rv, [f["num_words"]]]))
    Xs = StandardScaler().fit_transform(np.array(feats))
    km = KMeans(n_clusters=KMEANS_K, random_state=KMEANS_RS, n_init=10).fit(Xs)
    for r, lab in zip(rows, km.labels_):
        r["kmeans_cluster"] = int(lab)
        r["metadata_fold"] = primary_cluster(r["features"]["dominant_entity_type"])

    # eligibility + balanced selection (STEP 7)
    def eligible(r):
        f = r["features"]
        return 80 <= f["num_words"] <= 400 and f["num_entities"] >= 4 and f["num_triples"] >= 5

    elig = [r for r in rows if eligible(r)]
    clusters = ["cluster_PER", "cluster_ORG", "cluster_LOC", "cluster_MISC"]
    by_cluster = {c: [r for r in elig if r["metadata_fold"] == c] for c in clusters}
    logger.info(f"eligible {len(elig)}/{len(rows)} | " + " ".join(f"{c}={len(by_cluster[c])}" for c in clusters))

    role_counts, per_cluster_rows = Counter(), {}
    for c in clusters:
        pool = sorted(by_cluster[c], key=lambda r: (r["features"]["num_words"], r["id"]))
        conf = even_pick(pool, N_CONF)
        rem = [r for r in pool if r["id"] not in {x["id"] for x in conf}]
        pilot = even_pick(rem, N_PILOT)
        rem2 = [r for r in rem if r["id"] not in {x["id"] for x in pilot}]
        reserve = even_pick(rem2, N_RESERVE)
        for r in conf: r["_role"] = "confirmatory"
        for r in pilot: r["_role"] = "pilot"
        for r in reserve: r["_role"] = "reserve"
        per_cluster_rows[c] = conf + pilot + reserve
        role_counts[(c, "confirmatory")] += len(conf)
        role_counts[(c, "pilot")] += len(pilot)
        role_counts[(c, "reserve")] += len(reserve)
        logger.info(f"  {c}: conf={len(conf)} pilot={len(pilot)} reserve={len(reserve)}")
    # round-robin interleave by cluster so the dataset leads with cluster-diverse rows
    # (keeps auto-generated first-N mini/preview representative across all 4 folds)
    selected = []
    for rank in range(max(len(v) for v in per_cluster_rows.values())):
        for c in clusters:
            if rank < len(per_cluster_rows[c]):
                selected.append(per_cluster_rows[c][rank])

    # assemble exp_sel_data_out rows (STEP 8)
    caveat = ("Re-DocRED has residual false negatives; supports RELATIVE operational comparisons at "
              "matched recall only (precision, hallucinated-conclusion rate), not an absolute realized-FDR diagonal.")
    examples = []
    for r in selected:
        role = r["_role"]
        examples.append({
            "input": r["text"], "output": json.dumps(r["gold_triples"], ensure_ascii=False),
            "metadata_fold": r["metadata_fold"], "metadata_id": r["id"], "metadata_title": r["title"],
            "metadata_split_origin": r["split_origin"], "metadata_orig_index": r["orig_index"],
            "metadata_split_role": role, "metadata_is_confirmatory": role == "confirmatory",
            "metadata_is_pilot": role == "pilot", "metadata_is_reserve": role == "reserve",
            "metadata_kmeans_cluster": r["kmeans_cluster"],
            "metadata_cluster_scheme": "dominant_entity_type_collapsed_4", "metadata_seed": SEED,
            "metadata_sents": r["sents"], "metadata_sent_char_offsets": r["sent_char_offsets"],
            "metadata_entities": r["entities"], "metadata_gold_triples": r["gold_triples"],
            "metadata_features": r["features"], "metadata_gold_caveat": caveat,
        })

    # validate every row against the custom schema (STEP 9; fail loudly)
    validator = jsonschema.Draft7Validator(build_row_schema())
    nerr = 0
    for ex in examples:
        for e in sorted(validator.iter_errors(ex), key=lambda e: list(e.path))[:3]:
            logger.error(f"{ex.get('metadata_id')}: {list(e.path)} -> {e.message}"); nerr += 1
    if nerr:
        raise SystemExit(f"ROW SCHEMA VALIDATION FAILED ({nerr} errors)")
    logger.info(f"all {len(examples)} rows PASS custom row schema")

    # cross-consistency (STEP 10 invariants)
    ids = [e["metadata_id"] for e in examples]
    assert len(ids) == len(set(ids)), "duplicate ids across roles"
    for ex in examples:
        assert json.loads(ex["output"]) == ex["metadata_gold_triples"]
        assert sum([ex["metadata_is_confirmatory"], ex["metadata_is_pilot"], ex["metadata_is_reserve"]]) == 1
        nent = len(ex["metadata_entities"])
        for k, en in enumerate(ex["metadata_entities"]):
            assert en["entity_id"] == k
        for g in ex["metadata_gold_triples"]:
            assert 0 <= g["head_id"] < nent and 0 <= g["tail_id"] < nent

    # dataset-level metadata
    per_cluster = {c: {role: role_counts[(c, role)] for role in ("confirmatory", "pilot", "reserve")}
                   for c in clusters}
    dataset_meta = {
        "name": "Re-DocRED Operational Anchor (label-free FDR-gating)",
        "source": "Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED — Addressing the False Negative "
                  "Problem in Relation Extraction', EMNLP 2022)",
        "paper_url": "https://arxiv.org/abs/2205.12696",
        "data_urls": {fn.split("_")[0]: f"{HF_BASE}/{fn}" for fn, _ in FILES},
        "license": "MIT", "raw_doc_counts": {**EXPECT_COUNTS, "total": sum(EXPECT_COUNTS.values())},
        "n_emitted_rows": len(examples),
        "n_confirmatory": sum(e["metadata_is_confirmatory"] for e in examples),
        "n_pilot": sum(e["metadata_is_pilot"] for e in examples),
        "n_reserve": sum(e["metadata_is_reserve"] for e in examples),
        "clusters": clusters, "per_cluster_counts": per_cluster,
        "cluster_scheme": "dominant_entity_type_collapsed_4 (PER/ORG/LOC/MISC; TIME&NUM->MISC)",
        "secondary_cluster_scheme": f"kmeans (k={KMEANS_K}, random_state={KMEANS_RS}) on entity-type "
                                    f"histogram + top-{TOP_REL_K} relation profile + standardized length",
        "seed": SEED, "eligibility_filter": "80<=num_words<=400 AND num_entities>=4 AND num_triples>=5",
        "n_relation_types": len(REL_NAME), "n_entity_types": len(ENTITY_TYPES),
        "gold_caveat": "Re-DocRED has residual false negatives; this dataset licenses ONLY relative "
                       "operational comparisons at matched recall (precision, hallucinated-conclusion rate) "
                       "— never an absolute realized-FDR diagonal.",
        "shared_triple_space": "All downstream systems (neuro-symbolic, plain confidence threshold, CoT, RAG, "
                               "labeled conformal) map their raw output into THIS identical entity set and "
                               "96-relation triple space at matched recall; only RELATIVE operational "
                               "comparisons are asserted (residual false negatives affect all systems equally).",
        "companion_files": ["relation_schema.json", "entity_type_schema.json", "dataset_meta.json", "row_schema.json"],
    }

    out_obj = {"metadata": dataset_meta, "datasets": [{"dataset": "Re-DocRED", "examples": examples}]}
    (WS / "full_data_out.json").write_text(json.dumps(out_obj, indent=2, ensure_ascii=False))

    # companion files
    rel_list = [{"relation_pid": p, "relation_name": rel_schema_wd.get(p, {}).get("relation_name") or p,
                 "relation_description": rel_schema_wd.get(p, {}).get("relation_description")} for p in pids]
    (WS / "relation_schema.json").write_text(json.dumps(rel_list, indent=2, ensure_ascii=False))
    (WS / "entity_type_schema.json").write_text(json.dumps(
        [{"entity_type": tp, "gloss": ENTITY_TYPE_GLOSS[tp]} for tp in ENTITY_TYPES], indent=2, ensure_ascii=False))
    (WS / "dataset_meta.json").write_text(json.dumps(dataset_meta, indent=2, ensure_ascii=False))
    (WS / "row_schema.json").write_text(json.dumps(build_row_schema(), indent=2))
    # mini_data_out.json / preview_data_out.json are produced from full_data_out.json by the
    # aii-json skill's format script (aii_json_format_mini_preview.py --format exp_sel_data_out).

    # STEP 10 sanity report
    covered_rels = {g["relation_pid"] for e in examples for g in e["metadata_gold_triples"]}
    covered_types = {en["type"] for e in examples for en in e["metadata_entities"]}
    logger.info("=== SANITY REPORT ===")
    logger.info(f"rows={len(examples)} conf={dataset_meta['n_confirmatory']} "
                f"pilot={dataset_meta['n_pilot']} reserve={dataset_meta['n_reserve']}")
    logger.info(f"per-cluster={per_cluster}")
    logger.info(f"relations covered={len(covered_rels)}/96 entity-types={len(covered_types)}/6")
    for c in clusters:
        sub = [e for e in examples if e["metadata_fold"] == c]
        nw = [e["metadata_features"]["num_words"] for e in sub]
        td = [e["metadata_features"]["triple_density"] for e in sub]
        me = [e["metadata_features"]["frac_multi_evidence_triples"] for e in sub]
        logger.info(f"  {c} n={len(sub)} num_words[{min(nw)},{max(nw)}] "
                    f"triple_density[{min(td):.2f},{max(td):.2f}] frac_multi_ev[{min(me):.2f},{max(me):.2f}]")
    ex0 = examples[0]
    logger.info(f"EXAMPLE {ex0['metadata_id']} [{ex0['metadata_fold']}/{ex0['metadata_split_role']}] "
                f"ents={len(ex0['metadata_entities'])} triples={len(ex0['metadata_gold_triples'])}")
    logger.info(f"  text: {ex0['input'][:200]}")
    for g in ex0["metadata_gold_triples"][:3]:
        logger.info(f"  ({g['head_name']}) -[{g['relation_name']}]-> ({g['tail_name']}) ev={g['evidence_sent_ids']}")
    logger.info("=== DONE: single chosen dataset = Re-DocRED ===")


if __name__ == "__main__":
    main()
