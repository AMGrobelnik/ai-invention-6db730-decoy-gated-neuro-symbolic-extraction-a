#!/usr/bin/env python3
"""Independent, from-scratch verification of the final data_out.json.

Re-checks every invariant the dataset claims, with NO reliance on the build code:
  1. JSON parse of every input/output string.
  2. char_length == len(document_text); length band sanity.
  3. Every entity char_span verifies: document_text[s:e] == name.
  4. Every entity type in {PER,LOC,ORG,TIME,NUM,MISC}.
  5. Every fact provenance_char_span valid; value-tail facts have tail in span;
     EVERY fact's provenance span non-empty.
  6. Head/tail entity-linking coverage (how many fact endpoints appear in the
     document text -> the dataset is usable for span-grounded extraction).
  7. Genre / quality / license balance + relation-vocab report.
Also runs a trivial substring "baseline" recall to confirm the gold is
recoverable from the raw document (signal check, not an LLM).
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
COARSE = {"PER", "LOC", "ORG", "TIME", "NUM", "MISC"}


def main():
    data = json.loads((ROOT / "data_out.json").read_text())
    assert "datasets" in data and len(data["datasets"]) >= 1
    exs = [e for d in data["datasets"] for e in d["examples"]]
    group_sizes = {d["dataset"]: len(d["examples"]) for d in data["datasets"]}
    errors, warns = [], []
    n_ent = n_ent_ok = 0
    n_fact = n_fact_tail_in_span = 0
    head_linked = tail_linked = 0
    genres, quality, lic = Counter(), Counter(), Counter()
    rels = Counter()
    type_counts = Counter()
    lens = []

    for ex in exs:
        inp = json.loads(ex["input"])
        out = json.loads(ex["output"])
        did = inp["doc_id"]
        dt = inp["document_text"]
        genres[inp["genre"]] += 1
        quality[ex["metadata_gold_quality"]] += 1
        lic[ex["metadata_license"]] += 1
        lens.append(len(dt))

        # length consistency
        if inp["char_length"] != len(dt):
            errors.append(f"{did}: char_length {inp['char_length']} != len {len(dt)}")
        if ex["metadata_char_length"] != len(dt):
            errors.append(f"{did}: metadata_char_length mismatch")
        if not (1100 <= len(dt) <= 3600):
            warns.append(f"{did}: length {len(dt)} outside ~1150-3550 band")

        ent_surfaces = set()
        for e in inp["entities"]:
            n_ent += 1
            s, ee = e["char_span"]
            type_counts[e["type"]] += 1
            if e["type"] not in COARSE:
                errors.append(f"{did}: bad entity type {e['type']}")
            if 0 <= s <= ee <= len(dt) and dt[s:ee] == e["name"]:
                n_ent_ok += 1
                ent_surfaces.add(e["name"])
            else:
                errors.append(f"{did}: entity span FAIL {e['name']!r} {e['char_span']}")

        facts = out["gold_atomic_facts"]
        if len(facts) < 3:
            warns.append(f"{did}: only {len(facts)} facts")
        for f in facts:
            n_fact += 1
            rels[f["relation"]] += 1
            s, ee = f["provenance_char_span"]
            if not (0 <= s < ee <= len(dt)):
                errors.append(f"{did}: bad provenance span {f['provenance_char_span']}")
                continue
            prov = dt[s:ee]
            if not prov.strip():
                errors.append(f"{did}: empty provenance for {f}")
            if f["tail"] in prov:
                n_fact_tail_in_span += 1
            # entity-linking coverage: do head/tail appear in the document?
            if f["head"] in dt:
                head_linked += 1
            if f["tail"] in dt:
                tail_linked += 1

    print("=" * 64)
    print(f"documents: {len(exs)}  | source-dataset groups: {group_sizes}")
    print(f"genres={dict(genres)}")
    print(f"gold_quality={dict(quality)}")
    print(f"licenses:")
    for k, v in lic.items():
        print(f"   {v:2d}  {k[:70]}")
    print(f"char_length: min={min(lens)} max={max(lens)} mean={sum(lens)//len(lens)}")
    print("-" * 64)
    print(f"entities: {n_ent} | spans verified: {n_ent_ok}/{n_ent} "
          f"({100*n_ent_ok/n_ent:.1f}%)")
    print(f"entity type dist: {dict(type_counts)}")
    print(f"facts: {n_fact} | tail-in-provenance: {n_fact_tail_in_span}/{n_fact} "
          f"({100*n_fact_tail_in_span/n_fact:.1f}%) [rest are clause/label facts]")
    print(f"fact head appears in doc: {head_linked}/{n_fact} ({100*head_linked/n_fact:.1f}%)")
    print(f"fact tail appears in doc: {tail_linked}/{n_fact} ({100*tail_linked/n_fact:.1f}%)")
    print(f"distinct relations: {len(rels)}")
    print(f"top relations: {rels.most_common(12)}")
    print("-" * 64)
    print(f"ERRORS: {len(errors)}")
    for e in errors[:30]:
        print("   ERR", e)
    print(f"WARNINGS: {len(warns)}")
    for w in warns[:20]:
        print("   warn", w)
    print("=" * 64)
    print("RESULT:", "PASS — all spans/types/lengths verified" if not errors
          else f"FAIL — {len(errors)} errors")


if __name__ == "__main__":
    main()
