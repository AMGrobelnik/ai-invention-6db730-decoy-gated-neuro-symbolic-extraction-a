#!/usr/bin/env python3
"""Shared utilities for the application-anchor builder.

- Coarse upper-ontology entity typing into {PER,LOC,ORG,TIME,NUM,MISC},
  matching Block C of the dependency spec (research_out.json):
    * spaCy NER label -> coarse type (named entities)
    * NLTK WordNet hypernym-path anchors -> coarse type (common-noun heads/tails)
- Span verification helpers (every char_span MUST satisfy text[s:e]==surface).
- Row assembly into the exp_sel_data_out schema (input/output are JSON STRINGS).

NO LLM is used anywhere in gold construction (non-circularity for the
next-iteration hallucination experiment). Offline tools only.
"""
from __future__ import annotations
import os, json, functools
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ.setdefault("NLTK_DATA", str(ROOT / "raw" / "nltk_data"))

import spacy
import nltk
nltk.data.path.insert(0, str(ROOT / "raw" / "nltk_data"))
from nltk.corpus import wordnet as wn

SEED = 42
COARSE_TYPES = {"PER", "LOC", "ORG", "TIME", "NUM", "MISC"}

# ---- spaCy NER label -> coarse upper-ontology type --------------------------
SPACY_TO_COARSE = {
    "PERSON": "PER",
    "NORP": "MISC",          # nationalities/religions/political groups
    "FAC": "LOC",
    "ORG": "ORG",
    "GPE": "LOC",
    "LOC": "LOC",
    "PRODUCT": "MISC",
    "EVENT": "MISC",
    "WORK_OF_ART": "MISC",
    "LAW": "MISC",
    "LANGUAGE": "MISC",
    "DATE": "TIME",
    "TIME": "TIME",
    "PERCENT": "NUM",
    "MONEY": "NUM",
    "QUANTITY": "NUM",
    "ORDINAL": "NUM",
    "CARDINAL": "NUM",
}

# ---- WordNet hypernym anchor synsets -> coarse type (Block C) ----------------
# anchor synset name -> coarse type. We test presence anywhere on a hypernym path.
WN_ANCHORS = [
    ("person.n.01", "PER"),
    ("location.n.01", "LOC"),
    ("region.n.03", "LOC"),
    ("organization.n.01", "ORG"),
    ("social_group.n.01", "ORG"),
    ("time_period.n.01", "TIME"),
    ("number.n.02", "NUM"),
    ("measure.n.02", "NUM"),
]


@functools.lru_cache(maxsize=4096)
def wordnet_type(word: str) -> str:
    """Coarse type of a common noun via WordNet hypernym paths (Block C)."""
    w = (word or "").strip().lower().split()
    if not w:
        return "MISC"
    head = w[-1]  # head noun of the phrase
    try:
        syns = wn.synsets(head, pos=wn.NOUN)
    except Exception:
        return "MISC"
    if not syns:
        return "MISC"
    anchor_names = {a for a, _ in WN_ANCHORS}
    # use the most common (first) sense's hypernym closure
    for syn in syns[:3]:
        path_names = set()
        for path in syn.hypernym_paths():
            for s in path:
                path_names.add(s.name())
        hit = path_names & anchor_names
        if hit:
            # respect WN_ANCHORS priority order
            for a, t in WN_ANCHORS:
                if a in hit:
                    return t
    return "MISC"


def coarse_type(surface: str, spacy_label: str | None = None) -> str:
    """Coarse type: prefer spaCy NER label mapping; fall back to WordNet."""
    if spacy_label and spacy_label in SPACY_TO_COARSE:
        return SPACY_TO_COARSE[spacy_label]
    return wordnet_type(surface)


# ---- spaCy singleton --------------------------------------------------------
_NLP = None


def get_nlp():
    global _NLP
    if _NLP is None:
        _NLP = spacy.load("en_core_web_sm")
    return _NLP


# ---- span verification ------------------------------------------------------
def verify_span(text: str, span, surface: str) -> bool:
    s, e = span
    return 0 <= s <= e <= len(text) and text[s:e] == surface


def find_span(text: str, surface: str, start_hint: int = 0):
    """Return [s,e] for the first exact occurrence of surface at/after hint."""
    if not surface:
        return None
    i = text.find(surface, start_hint)
    if i < 0 and start_hint > 0:
        i = text.find(surface)
    if i < 0:
        return None
    return [i, i + len(surface)]


# ---- entity collection ------------------------------------------------------
def spacy_entities(text: str, allowed_labels=None):
    """Run spaCy NER; return verified coarse-typed entity dicts (deduped)."""
    nlp = get_nlp()
    doc = nlp(text)
    seen = set()
    ents = []
    for ent in doc.ents:
        if allowed_labels and ent.label_ not in allowed_labels:
            continue
        name = ent.text.strip()
        if len(name) < 2:
            continue
        span = [ent.start_char, ent.end_char]
        # spaCy span may include trailing whitespace differences; re-verify
        if text[span[0]:span[1]] != ent.text:
            continue
        name_span = [ent.start_char, ent.start_char + len(name)]
        if text[name_span[0]:name_span[1]] != name:
            name_span = span
            name = ent.text
        key = (name, name_span[0])
        if key in seen:
            continue
        seen.add(key)
        ctype = SPACY_TO_COARSE.get(ent.label_, "MISC")
        # spaCy frequently mislabels short ALL-CAPS acronyms (protocols, codes)
        # as ORG; downgrade these to MISC for cleaner typing.
        if ctype == "ORG" and name.isupper() and len(name) <= 5 and " " not in name:
            ctype = "MISC"
        ents.append({
            "name": name,
            "type": ctype,
            "char_span": name_span,
            "_fine": ent.label_,
        })
    return ents


# ---- row assembly (exp_sel_data_out schema) ---------------------------------
def make_row(*, doc_id: str, document_text: str, genre: str, source: str,
             entities: list, facts: list, license: str, gold_quality: str,
             relation_vocab: list, entity_types_fine: dict | None = None,
             extra_meta: dict | None = None) -> dict:
    """Assemble one schema row. input/output serialized to JSON strings.

    Drops any entity/fact whose char_span does not verify against document_text.
    Returns the row dict; raises ValueError if no valid facts remain.
    """
    L = len(document_text)
    clean_ents = []
    fine_map = dict(entity_types_fine or {})
    for e in entities:
        sp = e["char_span"]
        if verify_span(document_text, sp, e["name"]) and e["type"] in COARSE_TYPES:
            clean_ents.append({"name": e["name"], "type": e["type"], "char_span": [sp[0], sp[1]]})
            # fine type = the spaCy NER label (a finer class than the coarse 6-set)
            f = e.get("_fine")
            if f in SPACY_TO_COARSE:
                fine_map.setdefault(e["name"], f)
    # dedup entities by (name, span)
    seen = set(); ded = []
    for e in clean_ents:
        k = (e["name"], e["char_span"][0], e["char_span"][1])
        if k not in seen:
            seen.add(k); ded.append(e)
    clean_ents = ded

    clean_facts = []
    for f in facts:
        sp = f["provenance_char_span"]
        if not (0 <= sp[0] < sp[1] <= L):
            continue
        prov = document_text[sp[0]:sp[1]]
        if not prov.strip():
            continue
        tail_is_label = f.get("_tail_is_label", False)
        # Value-bearing facts: the tail IS the surface evidence -> must be in span.
        # Label facts (e.g. clause-type relations): the provenance span itself is
        # the human-annotated supporting evidence; tail is a normalized token.
        if not tail_is_label and f["tail"] not in prov:
            continue
        clean_facts.append({
            "head": f["head"], "relation": f["relation"], "tail": f["tail"],
            "provenance_char_span": [sp[0], sp[1]],
        })
    # dedup facts by (head,relation,tail) keeping earliest provenance
    clean_facts.sort(key=lambda f: f["provenance_char_span"][0])
    seen = set(); ded = []
    for f in clean_facts:
        k = (f["head"].lower(), f["relation"], f["tail"].lower())
        if k not in seen:
            seen.add(k); ded.append(f)
    clean_facts = ded
    if not clean_facts:
        raise ValueError(f"{doc_id}: no valid facts after verification")

    inp = {
        "doc_id": doc_id,
        "document_text": document_text,
        "genre": genre,
        "source": source,
        "char_length": L,
        "entities": clean_ents,
    }
    out = {"gold_atomic_facts": clean_facts}
    row = {
        "input": json.dumps(inp, ensure_ascii=False),
        "output": json.dumps(out, ensure_ascii=False),
        "metadata_doc_id": doc_id,
        "metadata_fold": genre,
        "metadata_genre": genre,
        "metadata_source": source,
        "metadata_license": license,
        "metadata_gold_quality": gold_quality,
        "metadata_char_length": L,
        "metadata_num_entities": len(clean_ents),
        "metadata_num_facts": len(clean_facts),
        "metadata_relation_vocab": sorted(set(relation_vocab)),
    }
    if fine_map:
        row["metadata_entity_types_fine"] = fine_map
    if extra_meta:
        for k, v in extra_meta.items():
            row[f"metadata_{k}"] = v
    return row
