#!/usr/bin/env python3
"""NEWS genre (SILVER) from Wikinews (CC BY 2.5).

Wikinews articles are genuinely short professional news prose. We curate
(head, relation, tail) gold facts DETERMINISTICALLY with offline spaCy
(dependency parse + NER) -- NO LLM. To keep gold high-precision we only emit
facts whose head & tail are recognized entities (or strong noun chunks) and
whose surfaces lie inside the provenance sentence:

  * entity-anchored SVO : (subjectNE, <verb_lemma>, objectNE)   "who did what"
  * occurred_on         : (subjectNE, occurred_on, DATE)        when
  * located_in          : (subjectNE, located_in, GPE/LOC)      where
  * affiliated_with     : (PER, affiliated_with, ORG)           appositive

gold_quality = silver (rule-based curation; limitation recorded).
"""
from __future__ import annotations
import json, glob, re
from pathlib import Path
from loguru import logger
import common as C

ROOT = Path(__file__).resolve().parent.parent
WN = ROOT / "raw" / "wikinews"
LICENSE = "CC BY 2.5 (Wikinews / Wikimedia Foundation)"
LO, HI = 1200, 3500
N_TARGET = 8
MIN_FACTS = 3

BOILER = ["Sources", "Related news", "Related articles", "External links",
          "External link", "Sister links", "References", "See also",
          "Have your say"]
SKIP_VERBS = {"be", "have", "do", "say", "tell", "report", "according", "include",
              "become", "seem", "appear", "want", "need", "use", "make", "get"}
SUBJ_DEPS = {"nsubj", "nsubjpass"}
OBJ_DEPS = {"dobj", "obj", "dative", "attr", "oprd", "pobj"}
# NE labels allowed as SVO endpoints (exclude DATE/TIME/number/money types)
SVO_NE = {"PERSON", "ORG", "GPE", "LOC", "FAC", "PRODUCT", "EVENT",
          "WORK_OF_ART", "NORP"}
# a DATE surface must carry a real date anchor (month/weekday/year/relative),
# not a vague time-of-day ("night") or a score/quantity.
DATE_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October|"
    r"November|December|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|"
    r"\b\d{4}\b|today|yesterday|tomorrow|\bago\b|"
    r"(last|next|this|past)\s+(week|month|year|night|decade))", re.IGNORECASE)


def _is_verb(lemma: str) -> bool:
    try:
        from nltk.corpus import wordnet as wn
        return bool(wn.synsets(lemma, pos="v"))
    except Exception:
        return True


def trim_article(extract: str) -> str:
    """Drop trailing boilerplate sections; keep dateline + news prose."""
    lines = extract.split("\n")
    cut = len(lines)
    for i, ln in enumerate(lines):
        if ln.strip() in BOILER:
            cut = i
            break
    body = "\n".join(lines[:cut]).strip()
    return body


def _mention(token, ent_by_tok):
    """Map a token to a NAMED-ENTITY mention (surface, [s,e], label) or None.
    For high-precision silver gold we anchor SVO endpoints on named entities."""
    if token.i in ent_by_tok:
        e = ent_by_tok[token.i]
        if e.label_ in SVO_NE and len(e.text.strip()) >= 2:
            return e.text, [e.start_char, e.end_char], e.label_
    return None


def extract_facts(text: str):
    nlp = C.get_nlp()
    doc = nlp(text)
    ent_by_tok = {}
    for e in doc.ents:
        for t in range(e.start, e.end):
            ent_by_tok[t] = e

    # map a token index -> the DATE/TIME entity that contains it (sane dates only)
    date_ent_at = {}
    for e in doc.ents:
        if e.label_ in ("DATE", "TIME") and DATE_RE.search(e.text):
            for t in range(e.start, e.end):
                date_ent_at[t] = e

    REL_PREPS = {"against", "with", "over", "into"}      # relational, not locative
    TMP_PREPS = {"on", "in", "during", "after", "before", "since", "at"}

    org_by_root = {e.root.i: e for e in doc.ents if e.label_ == "ORG"}
    facts = []
    for sent in doc.sents:
        sspan = [sent.start_char, sent.end_char]
        pers = [e for e in doc.ents if e.label_ == "PERSON" and sent.start <= e.start < sent.end]
        orgs = [e for e in doc.ents if e.label_ == "ORG" and sent.start <= e.start < sent.end]

        for tok in sent:
            if tok.pos_ != "VERB":
                continue
            lemma = tok.lemma_.lower()
            if lemma in SKIP_VERBS or not lemma.isalpha() or not _is_verb(lemma):
                continue
            subs = [c for c in tok.children if c.dep_ in SUBJ_DEPS]
            # objects: direct objects + objects of RELATIONAL prepositions only
            objs = [c for c in tok.children if c.dep_ in ("dobj", "obj", "dative", "attr", "oprd")]
            for prep in [c for c in tok.children if c.dep_ == "prep"]:
                if prep.lemma_.lower() in REL_PREPS:
                    objs += [c for c in prep.children if c.dep_ == "pobj"]
            # dates that modify THIS verb (temporal dependents) -> occurred_on
            verb_dates = []
            for c in tok.children:
                if c.i in date_ent_at and c.dep_ in ("npadvmod", "tmod", "advmod"):
                    verb_dates.append(date_ent_at[c.i])
                if c.dep_ == "prep" and c.lemma_.lower() in TMP_PREPS:
                    for pc in c.children:
                        if pc.dep_ == "pobj" and pc.i in date_ent_at:
                            verb_dates.append(date_ent_at[pc.i])
            for s in subs:
                sm = _mention(s, ent_by_tok)
                if not sm:
                    continue
                for o in objs:                      # NE-NE SVO -> high precision
                    om = _mention(o, ent_by_tok)
                    if not om or sm[0].strip().lower() == om[0].strip().lower():
                        continue
                    facts.append({"head": sm[0], "relation": lemma, "tail": om[0],
                                  "provenance_char_span": sspan})
                for d in verb_dates[:1]:            # when (tied to the action)
                    facts.append({"head": sm[0], "relation": "occurred_on",
                                  "tail": d.text, "provenance_char_span": sspan})

        # affiliated_with: STRICT dependency patterns only ("PER of ORG" /
        # "ORG's PER") -- adjacency co-occurrence is too noisy for gold.
        for p in pers:
            pr = p.root
            done = False
            # "PER of/from/at ORG"
            for c in pr.children:
                if c.dep_ == "prep" and c.lemma_.lower() in ("of", "from", "at"):
                    for pc in c.children:
                        if pc.dep_ == "pobj" and pc.i in org_by_root:
                            o = org_by_root[pc.i]
                            if o.start >= sent.start and o.end <= sent.end:
                                facts.append({"head": p.text, "relation": "affiliated_with",
                                              "tail": o.text, "provenance_char_span": sspan})
                                done = True
                if done:
                    break
            # "ORG's PER" (possessive)
            if not done:
                for o in orgs:
                    if o.root.dep_ == "poss" and o.root.head.i == pr.i:
                        facts.append({"head": p.text, "relation": "affiliated_with",
                                      "tail": o.text, "provenance_char_span": sspan})
                        break

    # doc-level dedup by (head,relation,tail) keeping earliest provenance; cap
    seen, ded = {}, []
    for f in sorted(facts, key=lambda x: x["provenance_char_span"][0]):
        k = (f["head"].lower(), f["relation"], f["tail"].lower())
        if k in seen:
            continue
        seen[k] = 1
        ded.append(f)
    return ded[:14]


def _topic_key(title: str) -> str:
    words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if len(w) > 2]
    return " ".join(words[:2]).lower()


def build():
    arts = []
    for f in sorted(glob.glob(str(WN / "article_*.json"))):
        j = json.loads(Path(f).read_text())
        for pid, p in j["query"]["pages"].items():
            ex = p.get("extract", "") or ""
            if not ex:
                continue
            body = trim_article(ex)
            if LO <= len(body) <= HI:
                arts.append((p["title"], int(p["pageid"]), body,
                             p.get("fullurl", ""),
                             (p.get("revisions") or [{}])[0].get("revid")))
    logger.info(f"Wikinews in-band trimmed articles: {len(arts)}")

    rows, used_topics = [], set()
    for title, pid, body, url, revid in arts:
        tk = _topic_key(title)
        if tk in used_topics:
            continue
        facts = extract_facts(body)
        if len(facts) < MIN_FACTS:
            continue
        ents = C.spacy_entities(body)
        if len(ents) < 4:
            continue
        used_topics.add(tk)
        doc_id = f"news_wikinews_{len(rows):02d}"
        vocab = sorted({f["relation"] for f in facts})
        try:
            row = C.make_row(
                doc_id=doc_id, document_text=body, genre="news",
                source=f"Wikinews:pageid_{pid}",
                entities=ents, facts=facts, license=LICENSE, gold_quality="silver",
                relation_vocab=vocab,
                extra_meta={"article_title": title, "source_url": url,
                            "revid": revid,
                            "source_dataset": "Wikinews (en.wikinews.org)",
                            "annotation": "deterministic spaCy SVO+5W rule-based (silver)"},
            )
            rows.append(row)
            logger.info(f"{doc_id}: len={len(body)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {title[:48]}")
        except ValueError as e:
            logger.warning(f"skip {doc_id} ({title[:40]}): {e}")
        if len(rows) >= N_TARGET:
            break
    return rows


if __name__ == "__main__":
    import sys
    logger.remove(); logger.add(sys.stdout, level="INFO",
                                format="{time:HH:mm:ss}|{level:<7}|{message}")
    rows = build()
    out = ROOT / "build" / "news_rows.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    logger.info(f"wrote {len(rows)} news rows -> {out}")
