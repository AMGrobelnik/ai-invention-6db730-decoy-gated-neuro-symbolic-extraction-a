#!/usr/bin/env python3
"""REGULATORY genre (SILVER) from GDPR (EUR-Lex/gdpr-info.eu) + eCFR (US, public
domain).

Regulatory prose is highly formulaic, so gold (head, relation, tail) facts are
curated DETERMINISTICALLY from the article/section structure with regex patterns
(NO LLM). Each provenance span is built to contain BOTH the head keyword and the
tail evidence, and is re-verified against document_text.

GDPR relation vocab : has_title, grants_right, obligates, prohibits,
                      has_exception, cross_references, defined_as
eCFR relation vocab : has_title, defined_as, requires, cross_references
gold_quality = silver (documented deterministic curation).
"""
from __future__ import annotations
import re, json, glob
from pathlib import Path
from loguru import logger
from bs4 import BeautifulSoup
import common as C

ROOT = Path(__file__).resolve().parent.parent
GDPR_DIR = ROOT / "raw" / "gdpr"
ECFR_DIR = ROOT / "raw" / "ecfr"
GDPR_LICENSE = ("EUR-Lex reuse (© European Union; Regulation (EU) 2016/679, "
                "CELEX:32016R0679; free reuse with attribution); text via gdpr-info.eu")
ECFR_LICENSE = "Public domain (US Government work; eCFR / GPO, ecfr.gov)"
LO, HI = 1150, 3550
GDPR_TARGET = 5
ECFR_TARGET = 3
MIN_FACTS = 3

EXCLUDE = {"empfehlung-erwaegungsgruende", "page-navigation", "link-to-overview",
           "feedback", "hidden-print"}


def clean_gdpr(html: str):
    s = BeautifulSoup(html, "lxml")
    h1 = s.select_one("h1.entry-title") or s.select_one("h1")
    title = h1.get_text(" ", strip=True) if h1 else ""
    ec = s.select_one("div.entry-content")
    blocks = []
    for c in ec.find_all(recursive=False):
        if set(c.get("class") or []) & EXCLUDE:
            continue
        if c.name in ("ol", "ul"):
            for i, li in enumerate(c.find_all("li", recursive=False), 1):
                t = re.sub(r"\s+", " ", li.get_text(" ", strip=True)).strip()
                if t:
                    blocks.append(f"{i}. {t}")
        elif c.name == "p":
            t = re.sub(r"\s+", " ", c.get_text(" ", strip=True)).strip()
            if t:
                blocks.append(t)
    body = "\n".join(blocks)
    return title, (title + "\n\n" + body if body else title)


def _span_ok(dt, s, e, surf):
    return 0 <= s < e <= len(dt) and dt[s:e] == surf


def _add_entity(ents, dt, name, typ):
    sp = C.find_span(dt, name)
    if sp:
        ents.append({"name": name, "type": typ, "char_span": sp, "_fine": typ})


def gdpr_facts(dt: str, art_n: int, title: str):
    facts, ents, vocab = [], [], []
    art_label = f"Art. {art_n} GDPR"
    if art_label not in dt:
        art_label = title
    _add_entity(ents, dt, art_label, "MISC")
    # has_title: descriptive title after the "Art. N GDPR" prefix
    m = re.search(r"Art\.\s*%d\s*GDPR\s+(.+)" % art_n, title)
    if m:
        desc = m.group(1).strip()
        sp = C.find_span(dt, desc)
        if sp:
            facts.append({"head": art_label, "relation": "has_title", "tail": desc,
                          "provenance_char_span": sp})
            vocab.append("has_title")

    # grants_right: "...the right to/of X"
    for m in re.finditer(r"(data subject\b[^.]*?\bright (?:to|of) )([a-z][^.;:\n]{3,90})", dt):
        tail = m.group(2).strip().rstrip(",")
        tail = re.split(r"\s+(?:and|where|under|in accordance|pursuant|which|referred)\b", tail)[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 4 and _span_ok(dt, ps, pe, dt[ps:pe]) and tail in dt[ps:pe]:
            facts.append({"head": "data subject", "relation": "grants_right", "tail": tail,
                          "provenance_char_span": [ps, pe]})
            vocab.append("grants_right")
    # obligates: "the controller shall <action>" / "shall have the obligation to <X>"
    for m in re.finditer(r"(controller shall (?:have the obligation to )?)([a-z][^.;:\n]{4,90})", dt):
        tail = m.group(2).strip().rstrip(",")
        tail = re.split(r"\s+(?:where|unless|in accordance|pursuant|without undue|referred|and the)\b", tail)[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 5 and tail in dt[ps:pe]:
            facts.append({"head": "controller", "relation": "obligates", "tail": tail,
                          "provenance_char_span": [ps, pe]})
            vocab.append("obligates")
    # has_exception: "shall not apply ... <condition>"
    for m in re.finditer(r"(shall not apply (?:to the extent that |where |if )?)([a-z][^.;:\n]{4,90})", dt):
        tail = m.group(2).strip().rstrip(",")
        tail = re.split(r"\s+(?:and|referred)\b", tail)[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 5 and tail in dt[ps:pe]:
            facts.append({"head": art_label, "relation": "has_exception", "tail": tail,
                          "provenance_char_span": [ps, pe], "_tail_is_label": False})
            vocab.append("has_exception")
    # cross_references: other "Article M"
    for m in re.finditer(r"Article\s+(\d+)", dt):
        if int(m.group(1)) == art_n:
            continue
        surf = m.group(0)
        sp = [m.start(), m.end()]
        facts.append({"head": art_label, "relation": "cross_references", "tail": surf,
                      "provenance_char_span": sp})
        vocab.append("cross_references")
        _add_entity(ents, dt, surf, "MISC")
    _add_entity(ents, dt, "data subject", "PER")
    _add_entity(ents, dt, "controller", "ORG")
    ents += C.spacy_entities(dt)  # enrich with offline NER
    return facts, ents, vocab


def ecfr_sections():
    """Yield (title_no, part, section_no, heading, document_text)."""
    out = []
    for f in sorted(glob.glob(str(ECFR_DIR / "*.xml"))):
        s = BeautifulSoup(Path(f).read_text(), "lxml-xml")
        tno = re.search(r"title-(\d+)", f).group(1)
        for sec in s.find_all("DIV8"):
            head = sec.find("HEAD")
            htxt = re.sub(r"\s+", " ", head.get_text(" ", strip=True)) if head else ""
            ps = [re.sub(r"\s+", " ", p.get_text(" ", strip=True)) for p in sec.find_all("P")]
            ps = [p for p in ps if p]
            body = htxt + "\n" + "\n".join(ps)
            if LO <= len(body) <= HI:
                out.append((tno, sec.get("N"), htxt, body))
    return out


def ecfr_facts(dt: str, sec_no: str, heading: str):
    facts, ents, vocab = [], [], []
    sec_label = f"§ {sec_no}"
    if sec_label not in dt:
        sec_label = heading.split(".")[0]
    _add_entity(ents, dt, sec_label, "MISC")
    # has_title: heading after "§ N "
    m = re.match(r"§\s*[\d.]+\s+(.+)", heading)
    if m:
        desc = m.group(1).strip().rstrip(".")
        sp = C.find_span(dt, desc)
        if sp:
            facts.append({"head": sec_label, "relation": "has_title", "tail": desc,
                          "provenance_char_span": sp})
            vocab.append("has_title")
    # defined_as: "X means Y."
    for m in re.finditer(r"([A-Z][A-Za-z][A-Za-z ]{1,40}?)\s+means\s+([^.;:\n]{6,110})", dt):
        term = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(1), m.start(2) + len(tail)
        if tail in dt[ps:pe]:
            facts.append({"head": term, "relation": "defined_as", "tail": tail,
                          "provenance_char_span": [ps, pe]})
            vocab.append("defined_as")
            _add_entity(ents, dt, term, C.coarse_type(term))
    # requires: "<subject> must <action>"
    for m in re.finditer(r"((?:An?|The|You|Each|Every)\s+[A-Za-z ]{0,30}?)\bmust\s+([a-z][^.;:\n]{4,90})", dt):
        subj = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(subj) >= 2 and tail in dt[ps:pe]:
            facts.append({"head": subj, "relation": "requires", "tail": tail,
                          "provenance_char_span": [ps, pe]})
            vocab.append("requires")
    # cross_references: other "§ X.Y"
    for m in re.finditer(r"§\s*(\d+\.\d+)", dt):
        if m.group(1) == sec_no:
            continue
        surf = m.group(0)
        facts.append({"head": sec_label, "relation": "cross_references", "tail": surf,
                      "provenance_char_span": [m.start(), m.end()]})
        vocab.append("cross_references")
    ents += C.spacy_entities(dt)  # enrich with offline NER
    return facts, ents, vocab


def build():
    rows = []
    # ---- GDPR (EU) ----
    gd = []
    for f in sorted(glob.glob(str(GDPR_DIR / "art-*.html")),
                    key=lambda x: int(re.search(r"art-(\d+)", x).group(1))):
        n = int(re.search(r"art-(\d+)", f).group(1))
        title, dt = clean_gdpr(Path(f).read_text())
        if LO <= len(dt) <= HI:
            gd.append((n, title, dt))
    logger.info(f"GDPR in-band: {len(gd)}")
    for n, title, dt in gd:
        if len([r for r in rows if r['metadata_genre'] == 'regulatory' and 'GDPR' in r['metadata_source']]) >= GDPR_TARGET:
            break
        facts, ents, vocab = gdpr_facts(dt, n, title)
        doc_id = f"reg_gdpr_{n:02d}"
        try:
            row = C.make_row(doc_id=doc_id, document_text=dt, genre="regulatory",
                             source=f"GDPR:Art{n}", entities=ents, facts=facts,
                             license=GDPR_LICENSE, gold_quality="silver",
                             relation_vocab=vocab,
                             extra_meta={"article": f"GDPR Article {n}", "jurisdiction": "EU",
                                         "source_dataset": "GDPR / Regulation (EU) 2016/679",
                                         "source_url": f"https://gdpr-info.eu/art-{n}-gdpr/",
                                         "legal_source": "EUR-Lex CELEX:32016R0679",
                                         "annotation": "deterministic structural regex curation (silver)"})
            if row["metadata_num_facts"] < MIN_FACTS:
                logger.info(f"skip {doc_id}: only {row['metadata_num_facts']} facts")
                continue
            rows.append(row)
            logger.info(f"{doc_id}: len={len(dt)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {title[:45]}")
        except ValueError as e:
            logger.warning(f"skip {doc_id}: {e}")
    # ---- eCFR (US) ----
    ec = ecfr_sections()
    logger.info(f"eCFR in-band sections: {len(ec)}")
    n_ec = 0
    for tno, sec_no, heading, dt in ec:
        if n_ec >= ECFR_TARGET:
            break
        facts, ents, vocab = ecfr_facts(dt, sec_no, heading)
        doc_id = f"reg_ecfr_{sec_no.replace('.', '_')}"
        try:
            row = C.make_row(doc_id=doc_id, document_text=dt, genre="regulatory",
                             source=f"eCFR:{tno}CFR{sec_no}", entities=ents, facts=facts,
                             license=ECFR_LICENSE, gold_quality="silver",
                             relation_vocab=vocab,
                             extra_meta={"section": f"{tno} CFR {sec_no}", "jurisdiction": "US",
                                         "source_dataset": "Electronic Code of Federal Regulations (eCFR)",
                                         "source_url": "https://www.ecfr.gov/",
                                         "annotation": "deterministic structural regex curation (silver)"})
            if row["metadata_num_facts"] < MIN_FACTS:
                logger.info(f"skip {doc_id}: only {row['metadata_num_facts']} facts")
                continue
            rows.append(row)
            n_ec += 1
            logger.info(f"{doc_id}: len={len(dt)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {heading[:45]}")
        except ValueError as e:
            logger.warning(f"skip {doc_id}: {e}")
    return rows


if __name__ == "__main__":
    import sys
    logger.remove(); logger.add(sys.stdout, level="INFO",
                                format="{time:HH:mm:ss}|{level:<7}|{message}")
    rows = build()
    out = ROOT / "build" / "regulatory_rows.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    logger.info(f"wrote {len(rows)} regulatory rows -> {out}")
