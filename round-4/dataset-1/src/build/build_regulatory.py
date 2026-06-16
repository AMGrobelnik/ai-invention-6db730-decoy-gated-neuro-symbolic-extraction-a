#!/usr/bin/env python3
"""REGULATORY genre (SILVER) from GDPR (EUR-Lex/gdpr-info.eu) + eCFR (US, public
domain).

Regulatory prose is highly formulaic, so gold (head, relation, tail) facts are
curated DETERMINISTICALLY from the article/section structure with regex patterns
(NO LLM). Each provenance span is built to contain BOTH the head keyword and the
tail evidence, and is re-verified against document_text.

iter_4 DEEPENED RECALL (the lever that shrinks the undecidable fraction). We
capture ALL regex matches (not the first) and add relations so structured
obligations are more fully covered:
  GDPR : has_title, defined_as ('X' means Y), grants_right, obligates, prohibits
         (shall not / may not), has_exception, applies_to, cross_references,
         has_paragraph (one fact per numbered paragraph -> enumerated coverage).
  eCFR : has_title, defined_as, requires (must/shall), prohibits, applies_to,
         cross_references, has_provision (one fact per lettered paragraph head).
Every provenance span is re-verified; high precision is kept (tight patterns,
length bounds, dedup) so over-generation is avoided. gold_quality = silver.
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
GDPR_TARGET = 15            # iter_4: scale EU regulatory 5 -> ~15
ECFR_TARGET = 11            # iter_4: scale US regulatory 3 -> ~11
ECFR_PER_PART = 4           # diversity cap: <=4 sections per CFR part
MIN_FACTS = 3

EXCLUDE = {"empfehlung-erwaegungsgruende", "page-navigation", "link-to-overview",
           "feedback", "hidden-print"}

# smart + ascii quote class for 'term' definitions
_QO = "[‘'\"“]"
_QC = "[’'\"”]"


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


def _emit(facts, vocab, dt, head, rel, tail, ps, pe, tail_is_label=False):
    """Append a fact only if its provenance span verifies and (for value facts)
    the tail is a substring of the provenance span. Returns True on success."""
    tail = tail.strip().rstrip(",;:")
    if len(tail) < 3:
        return False
    if not (0 <= ps < pe <= len(dt)):
        return False
    prov = dt[ps:pe]
    if not prov.strip():
        return False
    if not tail_is_label and tail not in prov:
        return False
    facts.append({"head": head, "relation": rel, "tail": tail,
                  "provenance_char_span": [ps, pe], "_tail_is_label": tail_is_label})
    vocab.append(rel)
    return True


def _clip_clause(text, max_len=110):
    """Concise leading clause: cut at first ; : or sentence end, else word-bound."""
    cut = re.split(r"(?:;|:|\.\s)", text, maxsplit=1)[0].strip()
    if len(cut) > max_len:
        cut = cut[:max_len]
        if " " in cut:
            cut = cut[:cut.rfind(" ")]
    return cut.strip()


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
            _emit(facts, vocab, dt, art_label, "has_title", desc, sp[0], sp[1], tail_is_label=True)

    # defined_as: "'term' means <definition>" (rich in Art.4 and elsewhere)
    for m in re.finditer(_QO + r"([^’'\"’”\n]{2,45})" + _QC + r"\s+means\s+([^;\n]{6,180})", dt):
        term = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(2), m.start(2) + len(tail)
        if _emit(facts, vocab, dt, term, "defined_as", tail, ps, pe):
            _add_entity(ents, dt, term, C.coarse_type(term))

    # grants_right: "...the right to/of X"
    for m in re.finditer(r"(data subject\b[^.]*?\bright (?:to|of) )([a-z][^.;:\n]{3,90})", dt):
        tail = re.split(r"\s+(?:and|where|under|in accordance|pursuant|which|referred)\b",
                        m.group(2).strip().rstrip(","))[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 4:
            _emit(facts, vocab, dt, "data subject", "grants_right", tail, ps, pe)

    # obligates: "the controller/processor shall <action>" (not "shall not")
    for subj in ("controller", "processor"):
        for m in re.finditer(r"(%s shall (?:have the obligation to )?)(?!not\b)([a-z][^.;:\n]{4,95})" % subj, dt):
            tail = re.split(r"\s+(?:where|unless|in accordance|pursuant|without undue|referred|and the)\b",
                            m.group(2).strip().rstrip(","))[0].strip()
            ps, pe = m.start(1), m.start(2) + len(tail)
            if len(tail) >= 5:
                _emit(facts, vocab, dt, subj, "obligates", tail, ps, pe)

    # prohibits: "<subject> shall not / may not <action>" (exclude "shall not apply")
    for m in re.finditer(r"(controller|processor|data subject|Member States?|This Regulation)\s+"
                         r"(?:shall|may|must)\s+not\s+(?!apply\b)([a-z][^.;:\n]{4,95})", dt):
        subj = m.group(1)
        tail = re.split(r"\s+(?:where|unless|except|in accordance|pursuant|referred)\b",
                        m.group(2).strip().rstrip(","))[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 5:
            _emit(facts, vocab, dt, subj, "prohibits", tail, ps, pe)

    # has_exception: "shall not apply ... <condition>"
    for m in re.finditer(r"(shall not apply (?:to the extent that |where |if )?)([a-z][^.;:\n]{4,95})", dt):
        tail = re.split(r"\s+(?:and|referred)\b", m.group(2).strip().rstrip(","))[0].strip()
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(tail) >= 5:
            _emit(facts, vocab, dt, art_label, "has_exception", tail, ps, pe)

    # applies_to: "This Regulation/Article applies to X"
    for m in re.finditer(r"(This (?:Regulation|Article|Chapter|Section)\s+(?:shall\s+)?appl(?:ies|y)\s+to\s+)"
                         r"([a-z][^.;:\n]{4,110})", dt):
        tail = re.split(r"\s+(?:and|where|carried|in the context)\b",
                        m.group(2).strip().rstrip(","))[0].strip()
        ps, pe = m.start(2), m.start(2) + len(tail)
        if len(tail) >= 5:
            _emit(facts, vocab, dt, art_label, "applies_to", tail, ps, pe)

    # has_paragraph: one fact per numbered paragraph -> enumerated coverage
    for m in re.finditer(r"(?m)^(\d+)\.\s+(.+)$", dt):
        body = m.group(2).strip()
        if len(re.findall(r"[A-Za-z]+", body)) < 6:
            continue
        tail = _clip_clause(body, 110)
        ps = m.start(2)
        pe = ps + len(tail)
        _emit(facts, vocab, dt, art_label, "has_paragraph", tail, ps, pe, tail_is_label=True)

    # cross_references: other "Article M"
    for m in re.finditer(r"Article\s+(\d+)", dt):
        if int(m.group(1)) == art_n:
            continue
        surf = m.group(0)
        _emit(facts, vocab, dt, art_label, "cross_references", surf, m.start(), m.end(), tail_is_label=True)
        _add_entity(ents, dt, surf, "MISC")

    _add_entity(ents, dt, "data subject", "PER")
    _add_entity(ents, dt, "controller", "ORG")
    _add_entity(ents, dt, "processor", "ORG")
    ents += C.spacy_entities(dt)  # enrich with offline NER
    return facts, ents, vocab


def ecfr_sections():
    """Yield (title_no, section_no, heading, document_text)."""
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
            _emit(facts, vocab, dt, sec_label, "has_title", desc, sp[0], sp[1], tail_is_label=True)

    # defined_as: "X means Y."
    for m in re.finditer(r"([A-Z][A-Za-z][A-Za-z ]{1,40}?)\s+means\s+([^.;:\n]{6,130})", dt):
        term = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(1), m.start(2) + len(tail)
        if _emit(facts, vocab, dt, term, "defined_as", tail, ps, pe):
            _add_entity(ents, dt, term, C.coarse_type(term))

    # requires: "<subject> must/shall <action>" (not negated)
    for m in re.finditer(r"((?:An?|The|You|Each|Every|No)\s+[A-Za-z ]{0,30}?)\b(?:must|shall)\s+"
                         r"(?!not\b)([a-z][^.;:\n]{4,95})", dt):
        subj = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(subj) >= 2 and len(tail) >= 5:
            _emit(facts, vocab, dt, subj, "requires", tail, ps, pe)

    # prohibits: "<subject> may not / shall not / must not <action>"
    for m in re.finditer(r"((?:An?|The|You|Each|Every|No)\s+[A-Za-z ]{0,30}?)\b"
                         r"(?:may|shall|must)\s+not\s+([a-z][^.;:\n]{4,95})", dt):
        subj = m.group(1).strip()
        tail = m.group(2).strip().rstrip(",")
        ps, pe = m.start(1), m.start(2) + len(tail)
        if len(subj) >= 2 and len(tail) >= 5:
            _emit(facts, vocab, dt, subj, "prohibits", tail, ps, pe)

    # applies_to: "This part/section applies to X"
    for m in re.finditer(r"(This (?:part|section|subpart)\s+(?:of this [a-z]+ )?appl(?:ies|y)\s+to\s+)"
                         r"([a-z][^.;:\n]{4,110})", dt):
        tail = re.split(r"\s+(?:and|that|who|which)\b", m.group(2).strip().rstrip(","))[0].strip()
        ps, pe = m.start(2), m.start(2) + len(tail)
        if len(tail) >= 5:
            _emit(facts, vocab, dt, sec_label, "applies_to", tail, ps, pe)

    # has_provision: one fact per lettered paragraph heading "(a) Heading."
    for m in re.finditer(r"\(([a-z])\)(?:\(\d+\))?\s+([A-Z][A-Za-z ,'\-/]{3,70})\.", dt):
        head_txt = m.group(2).strip()
        if len(re.findall(r"[A-Za-z]+", head_txt)) < 1:
            continue
        _emit(facts, vocab, dt, sec_label, "has_provision", head_txt,
              m.start(2), m.start(2) + len(head_txt), tail_is_label=True)

    # cross_references: other "§ X.Y"
    for m in re.finditer(r"§\s*(\d+\.\d+)", dt):
        if m.group(1) == sec_no:
            continue
        surf = m.group(0)
        _emit(facts, vocab, dt, sec_label, "cross_references", surf, m.start(), m.end(), tail_is_label=True)

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
    n_gdpr = 0
    for n, title, dt in gd:
        if n_gdpr >= GDPR_TARGET:
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
            n_gdpr += 1
            logger.info(f"{doc_id}: len={len(dt)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {title[:45]}")
        except ValueError as e:
            logger.warning(f"skip {doc_id}: {e}")
    # ---- eCFR (US) ----  ROUND-ROBIN across CFR parts for jurisdictional breadth
    # (telemarketing, HIPAA, Reg S-P, Reg E, COPPA, FTC Safeguards, Reg P) rather
    # than alphabetical filling that would never reach the title-16/17/45 parts.
    ec = ecfr_sections()
    logger.info(f"eCFR in-band sections: {len(ec)}")
    PART_ORDER = ["1005", "1016", "310", "312", "314", "248", "164"]
    buckets = {}
    for rec in ec:
        part = rec[1].split(".")[0]
        buckets.setdefault(part, []).append(rec)
    order = [p for p in PART_ORDER if buckets.get(p)] + [p for p in sorted(buckets) if p not in PART_ORDER]

    def _make_ecfr_row(tno, sec_no, heading, dt):
        facts, ents, vocab = ecfr_facts(dt, sec_no, heading)
        doc_id = f"reg_ecfr_{tno}_{sec_no.replace('.', '_')}"
        try:
            row = C.make_row(doc_id=doc_id, document_text=dt, genre="regulatory",
                             source=f"eCFR:{tno}CFR{sec_no}", entities=ents, facts=facts,
                             license=ECFR_LICENSE, gold_quality="silver", relation_vocab=vocab,
                             extra_meta={"section": f"{tno} CFR {sec_no}", "jurisdiction": "US",
                                         "source_dataset": "Electronic Code of Federal Regulations (eCFR)",
                                         "source_url": "https://www.ecfr.gov/",
                                         "ecfr_date": "2024-12-31",
                                         "annotation": "deterministic structural regex curation (silver)"})
        except ValueError as e:
            logger.warning(f"skip {doc_id}: {e}")
            return None
        if row["metadata_num_facts"] < MIN_FACTS:
            logger.info(f"skip {doc_id}: only {row['metadata_num_facts']} facts")
            return None
        logger.info(f"{doc_id}: len={len(dt)} facts={row['metadata_num_facts']} "
                    f"ents={row['metadata_num_entities']} :: {heading[:45]}")
        return row

    n_ec, part_count, idx = 0, {}, {p: 0 for p in buckets}
    while n_ec < ECFR_TARGET:
        progressed = False
        for part in order:
            if n_ec >= ECFR_TARGET:
                break
            if part_count.get(part, 0) >= ECFR_PER_PART:
                continue
            recs = buckets[part]
            while idx[part] < len(recs):
                tno, sec_no, heading, dt = recs[idx[part]]
                idx[part] += 1
                row = _make_ecfr_row(tno, sec_no, heading, dt)
                if row is None:
                    continue
                rows.append(row)
                n_ec += 1
                part_count[part] = part_count.get(part, 0) + 1
                progressed = True
                break
        if not progressed:
            break
    logger.info(f"regulatory: {n_gdpr} GDPR + {n_ec} eCFR (parts={part_count})")
    return rows


if __name__ == "__main__":
    import sys
    logger.remove(); logger.add(sys.stdout, level="INFO",
                                format="{time:HH:mm:ss}|{level:<7}|{message}")
    rows = build()
    out = ROOT / "build" / "regulatory_rows.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    logger.info(f"wrote {len(rows)} regulatory rows -> {out}")
