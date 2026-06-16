#!/usr/bin/env python3
"""STEP 0/1 (no API): validate data loading + deterministic mapping core on GOLD surface forms."""
from common import (MINI_DATA, Embedder, build_pcode_embeddings, load_docs, load_relation_schema)
import analyze as A
from loguru import logger
import sys
logger.remove(); logger.add(sys.stdout, level="INFO", format="{message}")

docs = load_docs(MINI_DATA, None, None)
print(f"Loaded {len(docs)} docs")
d0 = docs[0]
print("doc0 title:", d0["title"], "| n_entities:", len(d0["entities"]),
      "| n_gold:", len(d0["gold_triples"]))
gold, gbd = A.build_gold([{**d0, "title": d0["title"]}])
print("GOLD sample:", list(gold)[:5])

rel_schema = load_relation_schema()
emb = Embedder()
aligner = A.Aligner(emb, rel_schema)
print("pcode emb shape:", aligner.pcode_emb.shape)

# relation shortlist: is the gold P-code in the top-8 for clear cases?
hits = 0; tot = 0
for d in docs:
    for g in d["gold_triples"][:6]:
        sl = aligner._shortlist(g["relation_name"])
        codes = [p for p, _, _, _ in sl]
        tot += 1
        if g["relation_pid"] in codes:
            hits += 1
        else:
            print(f"  MISS rel {g['relation_pid']} '{g['relation_name']}' -> shortlist {codes[:4]}")
print(f"Relation shortlist recall@8 on gold: {hits}/{tot}")

# entity linking: do exact/alias tiers resolve gold entity_ids?
el_ok = 0; el_tot = 0
for d in docs:
    eidx = A.build_doc_entity_index(emb, d["entities"])
    for g in d["gold_triples"]:
        hid = A.link_entity(g["head_name"], eidx, emb, 0.6)
        tid = A.link_entity(g["tail_name"], eidx, emb, 0.6)
        el_tot += 1
        if hid == g["head_id"] and tid == g["tail_id"]:
            el_ok += 1
print(f"Entity-linking accuracy on gold surfaces: {el_ok}/{el_tot} = {el_ok/max(1,el_tot):.3f}")

# embedding-only relation alignment (no API) sanity
ro = 0; rt = 0
for d in docs:
    for g in d["gold_triples"]:
        pc = aligner.embed_only_pcode(g["relation_name"])
        rt += 1
        if pc == g["relation_pid"]:
            ro += 1
print(f"Embedding-only relation accuracy on gold: {ro}/{rt} = {ro/max(1,rt):.3f}")
print("PLUMBING OK")
