#!/usr/bin/env python3
"""Canonical standardization entrypoint for the APPLICATION ANCHOR dataset.

Builds the genre row-sets deterministically from the cached raw/ snapshot
(no network) and standardizes them into the exp_sel_data_out schema, GROUPED BY
SOURCE DATASET (each document is ONE example):

  datasets = [ {dataset: "CUAD",     examples:[...8 legal docs...]},
               {dataset: "Wikinews", examples:[...8 news docs...]},
               {dataset: "GDPR",     examples:[...5 regulatory EU docs...]},
               {dataset: "eCFR",     examples:[...3 regulatory US docs...]} ]

Every example carries metadata_fold = genre (enables leave-one-genre-out), a
crisp/silver gold_quality flag, per-row license, and the relation vocabulary.
NO LLM is used in gold construction. Outputs:
  data_out.json, full_data_out.json, mini_data_out.json, preview_data_out.json,
  dataset_meta.json.

Run:  python data.py   (or: bash regenerate.sh)
"""
from __future__ import annotations
import os, sys, json, glob, statistics, hashlib
from pathlib import Path
from collections import Counter, defaultdict
from loguru import logger

ROOT = Path(__file__).resolve().parent
os.environ.setdefault("NLTK_DATA", str(ROOT / "raw" / "nltk_data"))
sys.path.insert(0, str(ROOT / "build"))

import build_legal, build_news, build_regulatory  # noqa: E402

SEED = 42
# stable source-corpus -> dataset-group order
CORPUS_ORDER = ["CUAD", "Wikinews", "GDPR", "eCFR"]
TOOL_VERSIONS = {
    "python": "3.12", "spacy": "3.7.5", "spacy_model": "en_core_web_sm==3.7.1",
    "nltk": "3.9.1 (wordnet, omw-1.4)", "numpy": "1.26.4",
    "beautifulsoup4": "4.12.3 (lxml 5.3.0 parser)",
    "reserved_next_iteration": "sentence-transformers all-MiniLM-L6-v2, rank_bm25 "
                               "(NOT used for gold here; reserved for next-iteration "
                               "relation-alignment / retrieval)",
}


def corpus_of(source: str) -> str:
    return source.split(":")[0]


def raw_manifest():
    man = {}
    cu = ROOT / "raw" / "cuad_data" / "CUADv1.json"
    if cu.exists():
        man["CUADv1.json"] = {"bytes": cu.stat().st_size,
                              "sha256_16": hashlib.sha256(cu.read_bytes()).hexdigest()[:16]}
    man["gdpr_html_files"] = len(glob.glob(str(ROOT / "raw" / "gdpr" / "art-*.html")))
    man["wikinews_article_files"] = len(glob.glob(str(ROOT / "raw" / "wikinews" / "article_*.json")))
    man["ecfr_xml_files"] = len(glob.glob(str(ROOT / "raw" / "ecfr" / "*.xml")))
    return man


def build_meta(rows):
    genres = Counter(r["metadata_genre"] for r in rows)
    quality = Counter(r["metadata_gold_quality"] for r in rows)
    qbyg = defaultdict(Counter); cbyg = Counter(); lic = Counter()
    relvocab = defaultdict(set); lens = []; nfacts = []; nents = []
    dec_all = []; dec_by_g = defaultdict(list); sub_all = []
    crisp_subset = 0
    for r in rows:
        gg = r["metadata_genre"]
        qbyg[gg][r["metadata_gold_quality"]] += 1
        cbyg[corpus_of(r["metadata_source"])] += 1
        lic[r["metadata_license"]] += 1
        for rel in r["metadata_relation_vocab"]:
            relvocab[gg].add(rel)
        lens.append(r["metadata_char_length"]); nfacts.append(r["metadata_num_facts"])
        nents.append(r["metadata_num_entities"])
        df = r["metadata_decidable_fraction"]
        dec_all.append(df); dec_by_g[gg].append(df)
        sub_all.append(r["metadata_decidable_subscores"])
        if r.get("metadata_crisp_subset"):
            crisp_subset += 1

    def _stat(xs):
        return {"min": round(min(xs), 4), "max": round(max(xs), 4),
                "mean": round(statistics.mean(xs), 4),
                "median": round(statistics.median(xs), 4)}
    decidable_summary = {
        "note": ("Deterministic coverage proxy (NO model). composite = mean(sentence_coverage, "
                 "entity_participation, char_coverage). Descriptive per-row feature (like "
                 "num_facts) so the experiment can rank/select the most-decidable documents; "
                 "NOT an experiment metric."),
        "overall": _stat(dec_all),
        "by_genre": {g: _stat(v) for g, v in dec_by_g.items()},
        "subscore_means_overall": {
            k: round(statistics.mean([s[k] for s in sub_all]), 4)
            for k in ("sentence_coverage", "entity_participation", "char_coverage")},
    }
    return {
        "name": "application_anchor",
        "description": (
            "Genre-faithful APPLICATION anchor: short, professionally-written legal / "
            "news / regulatory documents standardized to a shared (head, relation, tail) "
            "triple schema with char-span provenance, coarse {PER,LOC,ORG,TIME,NUM,MISC} "
            "entity typing, a crisp-vs-silver gold_quality flag, per-row license, and a "
            "genre fold (metadata_fold) for leave-one-genre-out. ONE merged file assembled "
            "from multiple source corpora; the datasets[] array is grouped by source "
            "corpus. Built for a text->FOL->Prolog neuro-symbolic atomic-fact-extraction & "
            "hallucination-control experiment. NO LLM in gold construction (non-circularity). "
            "iter_4: scaled to ~84 docs (~24-32/genre; crisp-prioritized legal via CUAD "
            "excerpt windows + deepened silver recall) and adds a crisp-only fold "
            "(metadata_crisp_subset) and a deterministic coverage proxy "
            "(metadata_decidable_fraction) for selecting the cleanest documents."),
        "schema_per_example": {
            "grouping": "datasets[] is grouped by SOURCE CORPUS; each document is ONE example.",
            "input": "JSON string: {doc_id, document_text, genre, source, char_length, "
                     "entities:[{name,type in {PER,LOC,ORG,TIME,NUM,MISC},char_span:[s,e]}]}",
            "output": "JSON string: {gold_atomic_facts:[{head,relation,tail,"
                      "provenance_char_span:[s,e]}]}",
            "metadata": "metadata_fold(genre), metadata_genre, metadata_gold_quality(crisp|silver), "
                        "metadata_crisp_subset(bool; crisp-only fold), metadata_decidable_fraction"
                        "(float [0,1] composite coverage proxy), metadata_decidable_subscores"
                        "({sentence_coverage,entity_participation,char_coverage}), metadata_source, "
                        "metadata_license, metadata_relation_vocab, metadata_char_length, "
                        "metadata_num_facts, metadata_num_entities, metadata_doc_id, "
                        "metadata_entity_types_fine(optional), metadata_excerpt(legal whole vs excerpt)",
        },
        "n_documents": len(rows),
        "n_source_datasets": len(set(corpus_of(r["metadata_source"]) for r in rows)),
        "dataset_selection_rationale": (
            "4 source corpora CHOSEN from 9+ evaluated. Kept (free commercial+research "
            "license + genre-faithful short documents + supports deterministic no-LLM gold): "
            "CUAD (legal, CRISP), Wikinews (news, silver), GDPR + eCFR (regulatory, silver). "
            "iter_4 SCALE: legal CRISP is the priority lever -- CUAD's 510 contracts are mostly "
            "long (median ~33k chars), so beyond the ~22 naturally short whole contracts we add "
            "DETERMINISTIC excerpt windows (densest clause-span cluster, clean-boundary, re-based "
            "+ re-verified) for ~30 crisp legal docs; regulatory deepens silver recall (more GDPR "
            "articles + 6 CFR parts incl. HIPAA/Reg S-P) and news broadens predicates. Excluded "
            "for the HARD free-license / genre / format gates: MAUD (source merger texts CC-BY-NC-SA "
            "3.0, NonCommercial; multiple-choice on very long docs), LEDGAR (provision classification, "
            "no relational span facts), ContractNLI (CC-BY-NC-SA, NonCommercial), REDFM (CC BY-SA-NC), "
            "WebRED (sentence-level TFRecord), LDC ACE/TACRED (research-restricted). No free-license "
            "span-annotated 5th legal corpus exists, so CUAD excerpt windows supply crisp depth."),
        "genre_counts": dict(genres),
        "source_dataset_counts": dict(cbyg),
        "gold_quality_counts": dict(quality),
        "gold_quality_by_genre": {k: dict(v) for k, v in qbyg.items()},
        "license_counts": dict(lic),
        "relation_vocab_by_genre": {k: sorted(v) for k, v in relvocab.items()},
        "crisp_subset_count": crisp_subset,
        "decidable_fraction": decidable_summary,
        "total_facts": sum(nfacts), "total_entities": sum(nents),
        "facts_per_doc": {"min": min(nfacts), "max": max(nfacts),
                          "mean": round(statistics.mean(nfacts), 2)},
        "char_length": {"min": min(lens), "max": max(lens),
                        "mean": round(statistics.mean(lens), 1),
                        "median": int(statistics.median(lens))},
        "sources": {
            "CUAD (legal)": "CUAD v1 (theatticusproject) — CC BY 4.0 — human-annotated "
                            "clause spans (CRISP). https://zenodo.org/records/4595826",
            "Wikinews (news)": "en.wikinews.org — CC BY 2.5 — deterministic spaCy SVO+5W "
                               "rule-based curation (SILVER).",
            "GDPR (regulatory, EU)": "Regulation (EU) 2016/679 (EUR-Lex CELEX:32016R0679; "
                                     "text via gdpr-info.eu) — EUR-Lex free reuse — "
                                     "deterministic structural regex curation (SILVER).",
            "eCFR (regulatory, US)": "Electronic Code of Federal Regulations (ecfr.gov, versioner "
                                     "API @ 2024-12-31) — US Government public domain — deterministic "
                                     "structural regex curation (SILVER). Parts: 12 CFR 1005 (Reg E), "
                                     "12 CFR 1016 (Reg P), 16 CFR 312 (COPPA), 16 CFR 314 (FTC "
                                     "Safeguards), 17 CFR 248 (Reg S-P), 45 CFR 164 (HIPAA).",
        },
        "evaluated_but_excluded": {
            "MAUD (TheAtticusProject/maud)": "annotations CC-BY 4.0 BUT the source merger-agreement "
                                             "texts are CC-BY-NC-SA 3.0 (NonCommercial); multiple-choice "
                                             "expert labels on very long (>50k char) docs, not (h,r,t) "
                                             "char-span facts on ~3k-char documents.",
            "LEDGAR (LexGLUE coastalcph)": "single-label provision CLASSIFICATION only; no relational "
                                           "span facts -> not a crisp (head,relation,tail) source.",
            "REDFM (Babelscape)": "CC BY-SA-NC 4.0 (NonCommercial) — fails free-license rule; "
                                  "Wikipedia-genre overlap with the Re-DocRED anchor.",
            "ContractNLI (HF kiddothe2b)": "CC-BY-NC-SA 3.0 underlying docs (NonCommercial) — fails "
                                           "free-license rule; document-level NLI labels, not span facts.",
            "WebRED (google-research)": "CC BY-SA 3.0 (usable) but sentence-level TFRecord, not "
                                        "genre-faithful short documents; Wikinews preferred.",
            "LDC ACE / TACRED": "research-restricted / non-free — excluded per plan.",
        },
        "determinism": {
            "seed": SEED, "tool_versions": TOOL_VERSIONS,
            "regeneration": "Deterministic from cached raw/ with no network: python data.py "
                            "(build_legal+build_news+build_regulatory). Stable sort within "
                            "each source group by doc_id; source groups in fixed order "
                            f"{CORPUS_ORDER}.",
            "raw_cache_manifest": raw_manifest(),
        },
        "verification": "Every entity char_span and fact provenance_char_span is re-verified "
                        "against document_text (build/verify_dataset.py). Value-tail facts: "
                        "tail is a substring of the provenance span; clause/label facts: the "
                        "provenance span is the annotated supporting evidence.",
        "limitations": "Legal gold is CRISP (CUAD human clause-span annotation), including the "
                       "excerpt-window legal docs whose every clause span is re-based and re-verified. "
                       "News and regulatory gold are SILVER (deterministic rule/structure curation, no "
                       "LLM): facts are span-supported and high-precision but rule-based recall is "
                       "partial -- metadata_decidable_fraction reports this per-document coverage so the "
                       "experiment can select the most-decidable docs. gold_quality + crisp_subset carry "
                       "the crisp/silver split per row. decidable_fraction is a DESCRIPTIVE proxy (no "
                       "model), NOT an experiment metric.",
    }


def main():
    logger.remove(); logger.add(sys.stdout, level="INFO",
                                format="{time:HH:mm:ss}|{level:<7}|{message}")
    logger.info("building genre row-sets from cached raw/ ...")
    rows = build_legal.build() + build_news.build() + build_regulatory.build()
    logger.info(f"built {len(rows)} document rows")

    # group by source corpus (stable order), sort within group by doc_id
    groups = defaultdict(list)
    for r in rows:
        groups[corpus_of(r["metadata_source"])].append(r)
    datasets = []
    for c in CORPUS_ORDER:
        if groups.get(c):
            ex = sorted(groups[c], key=lambda r: r["metadata_doc_id"])
            datasets.append({"dataset": c, "examples": ex})
    # any unexpected corpus -> append deterministically
    for c in sorted(groups):
        if c not in CORPUS_ORDER:
            datasets.append({"dataset": c,
                             "examples": sorted(groups[c], key=lambda r: r["metadata_doc_id"])})

    meta = build_meta(rows)
    out = {"metadata": meta, "datasets": datasets}
    # data_out.json (canonical) and full_data_out.json (identical full copy).
    # mini/preview variants are produced by the aii-json format script downstream.
    (ROOT / "data_out.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    (ROOT / "full_data_out.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    (ROOT / "dataset_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))

    logger.info(f"datasets(by corpus)={[(d['dataset'], len(d['examples'])) for d in datasets]}")
    logger.info(f"genres={meta['genre_counts']} quality={meta['gold_quality_counts']} "
                f"facts={meta['total_facts']} ents={meta['total_entities']}")
    logger.info("wrote data_out.json + full_data_out.json + dataset_meta.json")


if __name__ == "__main__":
    main()
