#!/usr/bin/env python3
"""Standardize the CLUTRR Crisp-Gold Calibration Anchor dataset.

Run with:  uv run data.py   (deps declared in pyproject.toml)

Loads the pre-generated CLUTRR/v1 TEST CSVs staged in temp/datasets/ and converts
them into ONE standardized dataset of ~190 documents grouped under a single dataset,
conforming to the aii-json `exp_sel_data_out` schema:

    {"metadata": {...}, "datasets": [{"dataset": <name>, "examples": [ <row>, ... ]}]}

Each CLUTRR story = ONE example row (row == example). Per row:
  - input  (JSON string): doc_id, document_text (brackets stripped), document_text_bracketed,
            entities[{name,gender,type,node_index}], query{head,tail}
  - output (JSON string): atomic_facts[{head,relation,tail}] (directly-stated chain edges),
            multi_hop_facts[{head,relation,tail,derived_from,path_len,is_query_target}]
            (proof_state-derived inferred relations incl. the query target),
            multi_hop_query_target{head,relation,tail}, kinship_edge_graph{nodes,edges}
  - metadata_* flat fields: fold, chain_length_k, difficulty_split, f_comb, task_name,
            source_config, source_split, clutrr_id, is_pilot, n_atomic_facts,
            n_multi_hop_facts, document_char_length, proof_state_raw, noisy_story,
            atomic_crosscheck, namemap_method, genders_order_valid, relation_vocab_version

Everything is derived deterministically from CLUTRR's own structured fields
(proof_state, story_edges, edge_types, genders) — NO rule reimplementation, NO LLM,
NO decoys, NO FDR (those belong to the downstream experiment artifact).

Why CLUTRR is THE selected dataset: it is rule-based/templated, so its kinship gold is
exact (no annotation noise), which is precisely what lets it host the FDR calibration
diagonal; and proof_state gives crisp ATOMIC (directly-stated) + MULTI-HOP (inferred)
gold for the pre-registered disconfirmation. The secondary candidate (ProofWriter,
in temp/datasets/) is rule/fact theories with T/F/Unknown answers — it lacks the
kinship atomic+multi-hop triple gold this artifact's experiment is registered on, so
it is NOT included here (target_num_datasets=1).
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import resource
import sys
from collections import Counter, defaultdict
from pathlib import Path

import psutil
from loguru import logger

# --------------------------------------------------------------------------- #
# Setup
# --------------------------------------------------------------------------- #
HERE = Path(__file__).resolve().parent
DATASETS_DIR = HERE / "temp" / "datasets"
OUT_FILE = HERE / "full_data_out.json"
LOG_DIR = HERE / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOG_DIR / "data.log", rotation="30 MB", level="DEBUG")

# Memory guard: tiny CPU task (~2200 short CSV rows). Cap at 4GB.
_avail = psutil.virtual_memory().available
RAM_BUDGET = min(4 * 1024**3, int(_avail * 0.5))
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

DATASET_NAME = "CLUTRR-v1-CrispGold-CalibrationAnchor"
SEED = 20240617

# CLUTRR gen TEST configs (both span chain length k=2..10), staged in temp/datasets/.
CONFIGS = {
    "gen_train234_test2to10": "CLUTRR_v1_gen_train234_test2to10_test.csv",
    "gen_train23_test2to10": "CLUTRR_v1_gen_train23_test2to10_test.csv",
}

# Confirmatory stratification: SCALED to ~535 docs (iter-3), oversampling long chains (k>=6).
# NOTE: the per-k shuffled bucket order is invariant to these counts (the shared rng advances
# only by bucket sizes), so confirm=bucket[:n_conf] is a deterministic PREFIX-SUPERSET of the
# original 190-doc selection -> every original doc keeps its doc_id/text and HITS the warm cache.
CONFIRM_COUNTS = {2: 20, 3: 25, 4: 40, 5: 55, 6: 80, 7: 90, 8: 90, 9: 75, 10: 60}
# Pilot slice: ~52 docs, DISJOINT from confirmatory, both families represented (k>=6 oversampled).
PILOT_COUNTS = {2: 5, 3: 5, 4: 6, 5: 7, 6: 8, 7: 8, 8: 8, 9: 6, 10: 5}
# Round-robin k order that alternates short/long so mini/preview span both families.
K_ORDER = [2, 10, 6, 3, 9, 7, 4, 8, 5]


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #
def parse_proof_state(ps_str: str):
    """Parse CLUTRR proof_state (python-repr string of list-of-tuple-keyed-dicts).

    Returns (derived_order, leaf_facts, root, derived_children):
      - derived_order: list of derived (head, rel, tail) triples = dict keys (order preserved)
      - leaf_facts:    child triples never used as a key  (the atomic facts)
      - root:          the single derived triple never used as a child (== query target), else None
      - derived_children: {derived_triple: [child triple, child triple]}
    """
    ps = ast.literal_eval(ps_str)
    derived_order: list[tuple] = []
    children_all: list[tuple] = []
    derived_children: dict[tuple, list[tuple]] = {}
    for d in ps:
        for key, val in d.items():
            derived_order.append(key)
            derived_children[key] = list(val)
            children_all.extend(val)
    keyset = set(derived_order)
    childset = set(children_all)
    leaf = [c for c in dict.fromkeys(children_all) if c not in keyset]
    roots = [k for k in derived_order if k not in childset]
    root = roots[0] if len(roots) == 1 else None
    return derived_order, leaf, root, derived_children


def parse_genders(genders_raw: str):
    """'Name:gender,Name:gender,...' -> (ordered_names, name->gender map)."""
    order: list[str] = []
    gmap: dict[str, str] = {}
    for pair in genders_raw.split(","):
        name, gender = pair.rsplit(":", 1)
        order.append(name)
        gmap[name] = gender
    return order, gmap


def path_len(triple, derived_children, memo):
    """Number of atomic (leaf) edges spanned by a derived triple's proof subtree."""
    if triple not in derived_children:
        return 1  # leaf atomic fact
    if triple in memo:
        return memo[triple]
    total = sum(path_len(c, derived_children, memo) for c in derived_children[triple])
    memo[triple] = total
    return total


def strip_brackets(text: str) -> str:
    """Remove CLUTRR's [Name] entity-span markers, leaving clean prose."""
    return re.sub(r"[\[\]]", "", text)


# --------------------------------------------------------------------------- #
# Row construction
# --------------------------------------------------------------------------- #
def build_record(row: dict, config: str):
    """Parse one CLUTRR CSV row into a parsed record dict, or None if it fails the
    crisp simple-path invariants. Logs (does not raise) on rejection."""
    clutrr_id = row["id"]
    try:
        edge_types = ast.literal_eval(row["edge_types"])
        story_edges = [tuple(e) for e in ast.literal_eval(row["story_edges"])]
        query = tuple(ast.literal_eval(row["query"]))
        target_text = row["target_text"]
        f_comb = row["f_comb"]
        task_name = row["task_name"]
        clean_story = row.get("clean_story") or row.get("story") or ""
        noisy_story = row.get("story") or clean_story
        gorder, gmap = parse_genders(row["genders"])
        derived_order, leaf, root, derived_children = parse_proof_state(row["proof_state"])
    except (ValueError, SyntaxError, KeyError) as exc:
        logger.debug(f"[{clutrr_id}] parse failure: {exc}")
        return None

    k = len(edge_types)
    if not clean_story:
        return None

    # --- Crisp simple-path invariants (canonical clean CLUTRR chain) --------- #
    nodes_used = sorted({i for e in story_edges for i in e})
    simple_path = (
        len(nodes_used) == k + 1
        and nodes_used == list(range(k + 1))
        and len(set(story_edges)) == k
    )
    if not simple_path:
        return None
    # k cross-check three ways (Step 3): len(edge_types)==len(f_comb)==task_name k
    if not (len(edge_types) == len(f_comb.split("-")) == int(task_name.split(".")[-1])):
        return None
    if max(nodes_used) >= len(gorder):
        return None
    # genders-order namemap must reproduce the proof_state atomic (leaf) set
    leafset = set(leaf)
    namemap_ok = all(
        (gorder[i], rel, gorder[j]) in leafset for (i, j), rel in zip(story_edges, edge_types)
    )
    if not namemap_ok:
        return None
    if len(leaf) != k or len(derived_order) != k - 1 or root is None:
        return None
    if root != (query[0], target_text, query[1]):
        return None

    # --- Entities ----------------------------------------------------------- #
    entities = [
        {"name": name, "gender": gmap[name], "type": "person", "node_index": idx}
        for idx, name in enumerate(gorder)
    ]
    all_names = set(gorder)

    # --- Atomic gold (directly-stated, narrative order via story_edges) ------- #
    # (B) from (story_edges, edge_types, namemap); cross-validated against (A) proof_state leaves.
    atomic_facts = [
        {"head": gorder[i], "relation": rel, "tail": gorder[j]}
        for (i, j), rel in zip(story_edges, edge_types)
    ]
    atomic_crosscheck = (
        "match"
        if {(a["head"], a["relation"], a["tail"]) for a in atomic_facts} == leafset
        else "mismatch"
    )

    # --- Multi-hop gold (inferred, from proof_state derived keys; NO rule reimpl) #
    memo: dict[tuple, int] = {}
    multi_hop_facts = []
    for d in derived_order:
        multi_hop_facts.append(
            {
                "head": d[0],
                "relation": d[1],
                "tail": d[2],
                "derived_from": [list(c) for c in derived_children[d]],
                "path_len": path_len(d, derived_children, memo),
                "is_query_target": d == root,
            }
        )
    # build-up order: smallest compositions first, query target (path_len==k) last
    multi_hop_facts.sort(key=lambda m: (m["path_len"], not m["is_query_target"]))

    mh_query_target = {"head": query[0], "relation": target_text, "tail": query[1]}

    # --- Kinship edge graph ------------------------------------------------- #
    kinship_edge_graph = {
        "nodes": [
            {"index": i, "name": gorder[i], "gender": gmap[gorder[i]]}
            for i in range(len(gorder))
        ],
        "edges": [
            {"src": i, "dst": j, "relation": rel}
            for (i, j), rel in zip(story_edges, edge_types)
        ],
    }

    # --- Integrity: every fact name must be a known entity ------------------ #
    fact_names = set()
    for f in atomic_facts + multi_hop_facts + [mh_query_target]:
        fact_names.add(f["head"])
        fact_names.add(f["tail"])
    if not fact_names <= all_names:
        logger.debug(f"[{clutrr_id}] fact name not in entities")
        return None

    document_text = strip_brackets(clean_story)
    relations = sorted({f["relation"] for f in atomic_facts + multi_hop_facts})

    input_obj = {
        "doc_id": clutrr_id,
        "document_text": document_text,
        "document_text_bracketed": clean_story,
        "entities": entities,
        "query": {"head": query[0], "tail": query[1]},
    }
    output_obj = {
        "atomic_facts": atomic_facts,
        "multi_hop_facts": multi_hop_facts,
        "multi_hop_query_target": mh_query_target,
        "kinship_edge_graph": kinship_edge_graph,
    }

    return {
        "k": k,
        "clutrr_id": clutrr_id,
        "config": config,
        "input_obj": input_obj,
        "output_obj": output_obj,
        "f_comb": f_comb,
        "task_name": task_name,
        "n_atomic": len(atomic_facts),
        "n_multi_hop": len(multi_hop_facts),
        "doc_char_len": len(document_text),
        "proof_state_raw": row["proof_state"],
        "noisy_story": noisy_story,
        "atomic_crosscheck": atomic_crosscheck,
        "relations": relations,
    }


def to_example(rec: dict, is_pilot: bool) -> dict:
    """Render a parsed record into a schema-compliant example row (row == example)."""
    k = rec["k"]
    return {
        "input": json.dumps(rec["input_obj"], ensure_ascii=False),
        "output": json.dumps(rec["output_obj"], ensure_ascii=False),
        "metadata_fold": f"k{k}",
        "metadata_chain_length_k": k,
        "metadata_difficulty_split": "short" if k <= 3 else "long",
        "metadata_f_comb": rec["f_comb"],
        "metadata_task_name": rec["task_name"],
        "metadata_source_config": rec["config"],
        "metadata_source_split": "test",
        "metadata_clutrr_id": rec["clutrr_id"],
        "metadata_is_pilot": is_pilot,
        "metadata_n_atomic_facts": rec["n_atomic"],
        "metadata_n_multi_hop_facts": rec["n_multi_hop"],
        "metadata_document_char_length": rec["doc_char_len"],
        "metadata_proof_state_raw": rec["proof_state_raw"],
        "metadata_noisy_story": rec["noisy_story"],
        "metadata_atomic_crosscheck": rec["atomic_crosscheck"],
        "metadata_namemap_method": "genders_order",
        "metadata_genders_order_valid": True,
        "metadata_relation_vocab_version": "clutrr_kinship",
    }


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
@logger.catch(reraise=True)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="cap clean records for testing (0=all)")
    args = ap.parse_args()

    import random

    rng = random.Random(SEED)

    # 1) Load + pool both TEST configs, dedup by clean_story.
    pool: dict[str, tuple] = {}
    raw_counts = Counter()
    for config, fn in CONFIGS.items():
        path = DATASETS_DIR / fn
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        raw_counts[config] = len(rows)
        logger.info(f"Loaded {len(rows)} rows from {config} ({fn})")
        for r in rows:
            cs = r.get("clean_story") or r.get("story") or ""
            if cs and cs not in pool:
                pool[cs] = (r, config)
    logger.info(f"Pooled deduped rows: {len(pool)}")

    # 2) Parse + filter to crisp simple-path records.
    clean: list[dict] = []
    n_rejected = 0
    for cs, (r, config) in pool.items():
        rec = build_record(r, config)
        if rec is None:
            n_rejected += 1
            continue
        clean.append(rec)
        if args.limit and len(clean) >= args.limit:
            break
    logger.info(f"Clean simple-path records: {len(clean)} (rejected {n_rejected})")

    clean_by_k: dict[int, list[dict]] = defaultdict(list)
    for rec in clean:
        clean_by_k[rec["k"]].append(rec)
    logger.info("Clean k-distribution: " + ", ".join(f"k{k}={len(clean_by_k[k])}" for k in sorted(clean_by_k)))

    # 3) Seeded stratified sampling: confirmatory + DISJOINT pilot.
    confirm_by_k: dict[int, list[dict]] = {}
    pilot_by_k: dict[int, list[dict]] = {}
    for k in sorted(clean_by_k):
        bucket = sorted(clean_by_k[k], key=lambda x: x["clutrr_id"])  # deterministic pre-shuffle order
        rng.shuffle(bucket)
        n_conf = CONFIRM_COUNTS.get(k, 0)
        n_pilot = PILOT_COUNTS.get(k, 0)
        if len(bucket) < n_conf + n_pilot:
            logger.warning(f"k={k}: only {len(bucket)} available for {n_conf}+{n_pilot} requested")
        confirm_by_k[k] = bucket[:n_conf]
        pilot_by_k[k] = bucket[n_conf : n_conf + n_pilot]

    confirm_ids = {rec["clutrr_id"] for recs in confirm_by_k.values() for rec in recs}
    pilot_ids = {rec["clutrr_id"] for recs in pilot_by_k.values() for rec in recs}
    assert confirm_ids.isdisjoint(pilot_ids), "confirmatory and pilot overlap!"

    # 4) Round-robin interleave by K_ORDER so mini/preview span short+long chains.
    queues = {k: list(confirm_by_k.get(k, [])) + list(pilot_by_k.get(k, [])) for k in clean_by_k}
    examples: list[dict] = []
    remaining = True
    while remaining:
        remaining = False
        for k in K_ORDER:
            q = queues.get(k)
            if q:
                rec = q.pop(0)
                examples.append(to_example(rec, is_pilot=rec["clutrr_id"] in pilot_ids))
                remaining = True

    # 5) Aggregate metadata.
    conf_k_dist = {f"k{k}": len(confirm_by_k.get(k, [])) for k in sorted(clean_by_k)}
    pilot_k_dist = {f"k{k}": len(pilot_by_k.get(k, [])) for k in sorted(clean_by_k)}
    relation_vocab = sorted({rel for rec in clean for rel in rec["relations"]})
    logger.info(f"Confirmatory={len(confirm_ids)} Pilot={len(pilot_ids)} Total examples={len(examples)}")
    logger.info(f"Confirmatory k-dist: {conf_k_dist}")
    logger.info(f"Pilot k-dist: {pilot_k_dist}")
    logger.info(f"Relation vocabulary ({len(relation_vocab)}): {relation_vocab}")

    out = {
        "metadata": {
            "source": (
                "CLUTRR v1 (Sinha et al., EMNLP 2019, arXiv:1908.06177). Pre-generated TEST splits "
                "of configs gen_train234_test2to10 and gen_train23_test2to10, staged in temp/datasets/ "
                "from the kliang5/CLUTRR_huggingface_dataset GitHub raw CSV mirror."
            ),
            "title": "CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples with k-Difficulty Splits",
            "selected_best_dataset": DATASET_NAME,
            "selection_rationale": (
                "CLUTRR is rule-based/templated so its kinship gold is exact (no annotation noise) — "
                "the property that lets it host the FDR calibration diagonal; proof_state yields crisp "
                "ATOMIC (directly-stated) + MULTI-HOP (inferred) triple gold for the pre-registered "
                "disconfirmation. Secondary candidate ProofWriter (kept in temp/datasets/) has only "
                "T/F/Unknown answers over rule/fact theories, not kinship atomic+multi-hop triples, so "
                "it is excluded (target_num_datasets=1)."
            ),
            "row_is_example": "Each CLUTRR story is one example; 190 stories -> 190 examples.",
            "schema_note": (
                "input/output are JSON-serialized strings (parse with json.loads). "
                "input keys: doc_id, document_text (brackets stripped), document_text_bracketed, "
                "entities[{name,gender,type,node_index}], query{head,tail}. output keys: "
                "atomic_facts[{head,relation,tail}], multi_hop_facts[{head,relation,tail,derived_from,"
                "path_len,is_query_target}], multi_hop_query_target{head,relation,tail}, "
                "kinship_edge_graph{nodes,edges}."
            ),
            "seed": SEED,
            "raw_rows_per_config": dict(raw_counts),
            "pooled_deduped_rows": len(pool),
            "clean_simple_path_records": len(clean),
            "rejected_non_simple_path": n_rejected,
            "clean_k_distribution": {f"k{k}": len(clean_by_k[k]) for k in sorted(clean_by_k)},
            "confirmatory_count": len(confirm_ids),
            "pilot_count": len(pilot_ids),
            "total_documents": len(examples),
            "confirmatory_k_distribution": conf_k_dist,
            "pilot_k_distribution": pilot_k_dist,
            "relation_vocabulary": relation_vocab,
            "relation_vocab_version": "clutrr_kinship",
            "selected_confirmatory_ids": sorted(confirm_ids),
            "selected_pilot_ids": sorted(pilot_ids),
            "example_ordering": "round-robin across k (order " + str(K_ORDER) + ") so mini/preview span short and long chains",
            "filtering": (
                "Restricted to canonical CLUTRR simple-path chains: distinct entities==k+1, distinct "
                "story edges==k, |atomic|==k, |multi_hop|==k-1, exactly one proof root equal to the "
                "query target, and a genders-order node->name map that reproduces the proof_state "
                "atomic leaves. Guarantees deterministic crisp gold."
            ),
            "out_of_scope": (
                "No decoy/entrapment generation, no LLM scoring, no FDR/precision/recall, no Prolog "
                "execution, no transitive-closure enrichment — those belong to the experiment artifact."
            ),
        },
        "datasets": [
            {
                "dataset": DATASET_NAME,
                "examples": examples,
            }
        ],
    }

    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {OUT_FILE} ({OUT_FILE.stat().st_size/1024:.1f} KB, {len(examples)} examples)")


if __name__ == "__main__":
    main()
