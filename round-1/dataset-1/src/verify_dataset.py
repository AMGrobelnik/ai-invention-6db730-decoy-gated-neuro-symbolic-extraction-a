#!/usr/bin/env python3
"""Independent integrity verification of the built CLUTRR anchor dataset.

Re-checks every crisp-gold invariant on the FINAL output (not the builder's
internal state), so any silent corruption surfaces here.
"""
from __future__ import annotations

import ast
import json
import sys
from collections import Counter
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{message}")

HERE = Path(__file__).resolve().parent
F = HERE / "full_data_out.json"


def fail(cond, msg):
    if not cond:
        logger.error(f"FAIL: {msg}")
        raise AssertionError(msg)


def main():
    data = json.loads(F.read_text())
    md = data["metadata"]
    ds = data["datasets"][0]
    examples = ds["examples"]
    logger.info(f"Loaded {len(examples)} examples from {ds['dataset']}")

    n_pilot = 0
    n_conf = 0
    k_counter = Counter()
    conf_k = Counter()
    pilot_k = Counter()
    all_relations = set()
    seen_ids = set()
    checks = Counter()

    for ex in examples:
        # schema-shape: only input/output/metadata_*
        for key in ex:
            fail(key in ("input", "output") or key.startswith("metadata_"), f"bad key {key}")
        fail(isinstance(ex["input"], str) and isinstance(ex["output"], str), "input/output must be str")

        inp = json.loads(ex["input"])
        out = json.loads(ex["output"])
        k = ex["metadata_chain_length_k"]
        cid = ex["metadata_clutrr_id"]
        is_pilot = ex["metadata_is_pilot"]

        fail(cid not in seen_ids, f"duplicate clutrr_id {cid}")
        seen_ids.add(cid)
        k_counter[k] += 1
        if is_pilot:
            n_pilot += 1
            pilot_k[k] += 1
        else:
            n_conf += 1
            conf_k[k] += 1

        # fold + difficulty
        fail(ex["metadata_fold"] == f"k{k}", f"fold mismatch {cid}")
        fail(ex["metadata_difficulty_split"] == ("short" if k <= 3 else "long"), f"difficulty {cid}")
        fail(2 <= k <= 10, f"k out of range {cid}")

        entities = inp["entities"]
        ent_names = {e["name"] for e in entities}
        fail(len(entities) == k + 1, f"entities != k+1 for {cid}")
        for e in entities:
            fail(e["type"] == "person", f"entity type {cid}")
            fail(e["gender"] in ("male", "female"), f"gender {cid}")

        atomic = out["atomic_facts"]
        mh = out["multi_hop_facts"]
        mhqt = out["multi_hop_query_target"]
        graph = out["kinship_edge_graph"]

        # counts
        fail(len(atomic) == k, f"|atomic|={len(atomic)} != k={k} for {cid}")
        fail(len(mh) == k - 1, f"|multi_hop|={len(mh)} != k-1 for {cid}")
        fail(ex["metadata_n_atomic_facts"] == len(atomic), f"n_atomic md {cid}")
        fail(ex["metadata_n_multi_hop_facts"] == len(mh), f"n_mh md {cid}")

        # all fact names are known entities
        for f in atomic + mh + [mhqt]:
            fail(f["head"] in ent_names and f["tail"] in ent_names, f"unknown name in fact {cid}")
            all_relations.add(f["relation"])

        # query target present in multi_hop and equals the marked is_query_target fact
        qts = [m for m in mh if m.get("is_query_target")]
        fail(len(qts) == 1, f"exactly one query target expected {cid}")
        qt = qts[0]
        fail(
            (qt["head"], qt["relation"], qt["tail"]) == (mhqt["head"], mhqt["relation"], mhqt["tail"]),
            f"query target mismatch {cid}",
        )
        fail(qt["path_len"] == k, f"query target path_len != k for {cid}")
        # query target matches the document query pair
        fail(mhqt["head"] == inp["query"]["head"] and mhqt["tail"] == inp["query"]["tail"], f"query pair {cid}")

        # every derived_from child is a real atomic or derived triple
        triple_set = {(f["head"], f["relation"], f["tail"]) for f in atomic + mh}
        for m in mh:
            fail(len(m["derived_from"]) == 2, f"derived_from not binary {cid}")
            for child in m["derived_from"]:
                fail(tuple(child) in triple_set, f"derived_from child not found {cid}: {child}")

        # cross-check vs raw proof_state: derived keys == multi_hop triples
        ps = ast.literal_eval(ex["metadata_proof_state_raw"])
        ps_keys = set()
        for d in ps:
            ps_keys.update(d.keys())
        fail(ps_keys == {(m["head"], m["relation"], m["tail"]) for m in mh}, f"proof_state keys != multi_hop {cid}")

        # graph consistency: edges == atomic facts (by name), nodes == entities
        fail(len(graph["nodes"]) == k + 1, f"graph nodes {cid}")
        idx2name = {n["index"]: n["name"] for n in graph["nodes"]}
        graph_edges = {(idx2name[e["src"]], e["relation"], idx2name[e["dst"]]) for e in graph["edges"]}
        atomic_set = {(a["head"], a["relation"], a["tail"]) for a in atomic}
        fail(graph_edges == atomic_set, f"graph edges != atomic facts {cid}")

        # document is non-empty and not padded (length matches actual text)
        fail(len(inp["document_text"]) > 0, f"empty document {cid}")
        fail(ex["metadata_document_char_length"] == len(inp["document_text"]), f"doc len md {cid}")
        fail("[" not in inp["document_text"] and "]" not in inp["document_text"], f"brackets leaked {cid}")
        fail("[" in inp["document_text_bracketed"], f"bracketed copy missing markers {cid}")
        fail(ex["metadata_atomic_crosscheck"] == "match", f"atomic crosscheck not match {cid}")

        checks["ok"] += 1

    # aggregate checks
    fail(n_conf == sum(v for v in conf_k.values()), "conf count")
    fail(len(seen_ids) == len(examples), "dup ids")
    logger.info(f"Confirmatory={n_conf}  Pilot={n_pilot}  Total={len(examples)}")
    logger.info(f"k-distribution (all): {dict(sorted(k_counter.items()))}")
    logger.info(f"Confirmatory k-dist: {dict(sorted(conf_k.items()))}")
    logger.info(f"Pilot k-dist: {dict(sorted(pilot_k.items()))}")
    logger.info(f"Relations observed in facts ({len(all_relations)}): {sorted(all_relations)}")

    # metadata sanity
    fail(set(md["selected_confirmatory_ids"]).isdisjoint(md["selected_pilot_ids"]), "conf/pilot overlap in metadata")
    fail(len(md["selected_confirmatory_ids"]) == n_conf, "metadata conf ids count")
    fail(len(md["selected_pilot_ids"]) == n_pilot, "metadata pilot ids count")
    fail(set(md["relation_vocabulary"]) >= all_relations, "relation vocab incomplete")
    fail(md["seed"] == 20240617, "seed")

    # first 3 (mini/preview) span short and long chains
    first3_k = [examples[i]["metadata_chain_length_k"] for i in range(3)]
    logger.info(f"First-3 k (mini/preview span): {first3_k}")
    fail(any(x <= 3 for x in first3_k) and any(x >= 4 for x in first3_k), "mini does not span short+long")

    logger.info(f"\nALL {checks['ok']} EXAMPLES PASSED EVERY INTEGRITY CHECK ✓")


if __name__ == "__main__":
    main()
