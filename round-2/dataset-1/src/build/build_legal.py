#!/usr/bin/env python3
"""LEGAL genre (CRISP) from CUAD (CC BY 4.0).

CUAD ships human-annotated clause spans (answer text + char offset) per the 41
CUAD clause categories, in SQuAD format (raw/cuad_data/CUADv1.json). We map each
POPULATED clause category to a (head, relation, tail) triple deterministically:

  * value-bearing categories  -> tail = verbatim concise annotated span
                                 (the surface evidence; provenance = its span)
  * clause-presence categories -> tail = normalized clause-type token,
                                 provenance = the annotated clause span (evidence)

head = the agreement document entity (the Document Name span). NO LLM is used.
"""
from __future__ import annotations
import re, json
from pathlib import Path
from loguru import logger
import common as C

ROOT = Path(__file__).resolve().parent.parent
CUAD = ROOT / "raw" / "cuad_data" / "CUADv1.json"
LICENSE = "CC BY 4.0 (Atticus Project / CUAD v1; Zenodo 4595826)"
LO, HI = 1300, 3550          # length band (tolerance) for legal docs
MIN_FACTS = 3
N_TARGET = 8

# category -> (relation, kind)  kind: "value" = verbatim tail, "label" = clause token
CAT_MAP = {
    "Document Name":        ("has_title", "value"),
    "Parties":              ("has_party", "value"),
    "Agreement Date":       ("agreement_date", "value"),
    "Effective Date":       ("effective_date", "value"),
    "Expiration Date":      ("expiration_date", "value"),
    "Renewal Term":         ("renewal_term", "value"),
    "Notice Period To Terminate Renewal": ("notice_to_terminate_renewal", "value"),
    "Governing Law":        ("governed_by", "value"),
    "Cap On Liability":     ("liability_cap", "value"),
    "Warranty Duration":    ("warranty_duration", "value"),
    "Minimum Commitment":   ("minimum_commitment", "value"),
    "Revenue/Profit Sharing": ("revenue_profit_sharing", "value"),
    # clause-presence (salient legal clause types) -> label tails
    "Non-Compete":          ("contains_non_compete", "label"),
    "Exclusivity":          ("contains_exclusivity", "label"),
    "No-Solicit Of Customers": ("contains_no_solicit_customers", "label"),
    "No-Solicit Of Employees": ("contains_no_solicit_employees", "label"),
    "Non-Disparagement":    ("contains_non_disparagement", "label"),
    "Termination For Convenience": ("contains_termination_for_convenience", "label"),
    "Change Of Control":    ("contains_change_of_control", "label"),
    "Anti-Assignment":      ("contains_anti_assignment", "label"),
    "Ip Ownership Assignment": ("contains_ip_ownership_assignment", "label"),
    "License Grant":        ("contains_license_grant", "label"),
    "Source Code Escrow":   ("contains_source_code_escrow", "label"),
    "Post-Termination Services": ("contains_post_termination_services", "label"),
    "Audit Rights":         ("contains_audit_rights", "label"),
    "Insurance":            ("contains_insurance", "label"),
    "Covenant Not To Sue":  ("contains_covenant_not_to_sue", "label"),
    "Third Party Beneficiary": ("contains_third_party_beneficiary", "label"),
}
VALUE_CATS = {k for k, (_, kind) in CAT_MAP.items() if kind == "value"}

TYPE_KEYWORDS = ["hosting", "license", "licens", "maintenance", "co-branding", "cobranding",
                 "manufactur", "outsourcing", "content", "service", "supply", "reseller",
                 "joint filing", "promotion", "development", "consulting", "distribution"]


def _cat_of(question: str) -> str:
    m = re.search(r'related to "([^"]+)"', question)
    return m.group(1) if m else question[:40]


def _trim_value(text: str, start: int, max_len: int = 120):
    """Trim a verbatim answer to a concise tail ending on a word boundary."""
    t = text.strip()
    # tail = leading portion of the (stripped) answer; keep span aligned to text
    lead_ws = len(text) - len(text.lstrip())
    s = start + lead_ws
    body = t
    if len(body) > max_len:
        cut = body[:max_len]
        if " " in cut:
            cut = cut[:cut.rfind(" ")]
        body = cut
    return body, [s, s + len(body)]


def _clean_party(text: str, start: int, ctx: str):
    """Clean a CUAD party answer (strip wrapping parens/quotes/punct, drop
    generic defined-term fragments). Return (surface, [s,e]) or None."""
    cleaned = text.strip().strip(' ().,"\'“”')
    if "collectively" in cleaned.lower() or "hereinafter" in cleaned.lower():
        return None
    if len(cleaned) < 2 or sum(c.isalpha() for c in cleaned) < 2:
        return None
    idx = text.find(cleaned)
    if idx < 0:
        return None
    s = start + idx
    if ctx[s:s + len(cleaned)] != cleaned:
        return None
    return cleaned, [s, s + len(cleaned)]


def _infer_type(title: str) -> str:
    t = title.lower()
    for kw in TYPE_KEYWORDS:
        if kw in t:
            return kw
    return "other"


def build():
    data = json.loads(CUAD.read_text())["data"]
    candidates = []
    for art in data:
        ctx = art["paragraphs"][0]["context"]
        if not (LO <= len(ctx) <= HI):
            continue
        qas = art["paragraphs"][0]["qas"]
        # collect first answer per category; ALL distinct answers for Parties
        cat_ans = {}
        party_ans = []
        for q in qas:
            if not q["answers"]:
                continue
            cat = _cat_of(q["question"])
            if cat not in CAT_MAP:
                continue
            if cat == "Parties":
                seen_p = {p["text"] for p in party_ans}
                for a in q["answers"]:
                    if a["text"] in seen_p:
                        continue
                    if ctx[a["answer_start"]:a["answer_start"] + len(a["text"])] == a["text"]:
                        party_ans.append(a); seen_p.add(a["text"])
                if party_ans and "Parties" not in cat_ans:
                    cat_ans["Parties"] = party_ans[0]
            elif cat not in cat_ans:
                a = q["answers"][0]
                if ctx[a["answer_start"]:a["answer_start"] + len(a["text"])] == a["text"]:
                    cat_ans[cat] = a
        cat_ans["_parties"] = party_ans
        real_cats = [c for c in cat_ans if c != "_parties"]
        n_val = sum(1 for c in real_cats if c in VALUE_CATS)
        n_facts = len(real_cats) + max(0, len(cat_ans.get("_parties", [])) - 1)
        if n_facts >= MIN_FACTS and "Document Name" in cat_ans and n_val >= 2:
            candidates.append((art["title"], ctx, cat_ans, qas))
    logger.info(f"CUAD in-band candidates with >=3 facts: {len(candidates)}")

    # diversity selection: <=2 per inferred type, prefer more facts then title
    candidates.sort(key=lambda x: (-len(x[2]), x[0]))
    chosen, type_count = [], {}
    for title, ctx, cat_ans, qas in candidates:
        ty = _infer_type(title)
        if type_count.get(ty, 0) >= 2:
            continue
        type_count[ty] = type_count.get(ty, 0) + 1
        chosen.append((title, ctx, cat_ans, qas))
        if len(chosen) >= N_TARGET:
            break
    logger.info(f"CUAD chosen: {len(chosen)} (types={type_count})")

    rows = []
    for ci, (title, ctx, cat_ans, qas) in enumerate(chosen):
        doc_id = f"legal_cuad_{ci:02d}"
        # agreement head entity = Document Name span
        dn = cat_ans["Document Name"]
        agr_name, agr_span = _trim_value(dn["text"], dn["answer_start"], 90)
        if ctx[agr_span[0]:agr_span[1]] != agr_name:
            agr_span = [dn["answer_start"], dn["answer_start"] + len(dn["text"])]
            agr_name = dn["text"]
        entities = [{"name": agr_name, "type": "MISC", "char_span": agr_span, "_fine": "AGREEMENT"}]
        # spaCy NER over the contract for parties/dates/jurisdictions/amounts
        for e in C.spacy_entities(ctx, allowed_labels={"ORG", "PERSON", "GPE", "LOC",
                                                       "DATE", "MONEY", "PERCENT", "LAW"}):
            entities.append(e)

        facts, vocab, fine = [], [], {}
        parties = cat_ans.get("_parties", [])
        # all populated categories -> facts (value + label)
        for cat, a in cat_ans.items():
            if cat == "_parties":
                continue
            rel, kind = CAT_MAP[cat]
            vocab.append(rel)
            if cat == "Parties":
                for pa in parties:
                    cleaned = _clean_party(pa["text"], pa["answer_start"], ctx)
                    if not cleaned:
                        continue
                    ptail, pspan = cleaned
                    facts.append({"head": agr_name, "relation": "has_party",
                                  "tail": ptail, "provenance_char_span": pspan})
                    fine[ptail] = "has_party"
                    entities.append({"name": ptail, "type": "ORG",
                                     "char_span": pspan, "_fine": "has_party"})
                continue
            if kind == "value":
                tail, span = _trim_value(a["text"], a["answer_start"], 120)
                if ctx[span[0]:span[1]] != tail or len(tail.strip()) < 2:
                    continue
                facts.append({"head": agr_name, "relation": rel, "tail": tail,
                              "provenance_char_span": span})
                # register value tails that look like entities
                ftype = C.coarse_type(tail)
                if rel == "has_party":
                    ftype = "ORG"
                elif rel in ("agreement_date", "effective_date", "expiration_date",
                             "warranty_duration", "renewal_term"):
                    ftype = "TIME"
                elif rel == "governed_by":
                    ftype = "LOC"
                fine[tail] = rel
                entities.append({"name": tail, "type": ftype, "char_span": span, "_fine": rel})
            else:  # label / clause-presence
                tok = rel.replace("contains_", "")
                span = [a["answer_start"], a["answer_start"] + len(a["text"])]
                facts.append({"head": agr_name, "relation": rel, "tail": tok,
                              "provenance_char_span": span, "_tail_is_label": True})
        try:
            row = C.make_row(
                doc_id=doc_id, document_text=ctx, genre="legal", source=f"CUAD:{title}",
                entities=entities, facts=facts, license=LICENSE, gold_quality="crisp",
                relation_vocab=vocab,
                extra_meta={"contract_title": title,
                            "source_dataset": "CUAD v1 (theatticusproject)",
                            "source_url": "https://zenodo.org/records/4595826",
                            "annotation": "human-annotated CUAD clause spans"},
            )
            rows.append(row)
            logger.info(f"{doc_id}: len={len(ctx)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {title[:50]}")
        except ValueError as e:
            logger.warning(f"skip {doc_id}: {e}")
    return rows


if __name__ == "__main__":
    import sys
    from loguru import logger as lg
    lg.remove(); lg.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    rows = build()
    out = ROOT / "build" / "legal_rows.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    logger.info(f"wrote {len(rows)} legal rows -> {out}")
