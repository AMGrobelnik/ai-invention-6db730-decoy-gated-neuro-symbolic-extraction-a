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

iter_4 SCALE-UP (crisp is the priority lever). CUAD's 510 contracts are mostly
LONG (median ~33k chars); only ~22 fall naturally in the short-document band. To
build a DEEP crisp legal pool we add a DETERMINISTIC EXCERPT-WINDOW strategy:
for a long contract we pick the ~1.3-3.5k-char window covering the densest
cluster of >=3 fully-contained human clause spans (preferring windows that
contain the Document Name / Parties preamble), snap the window to clean
sentence / paragraph boundaries (NO mid-sentence truncation), RE-BASE every
contained clause's char offset into the excerpt (s' = s - w_start), keep only
clauses fully inside the window, and re-verify every re-based span. One excerpt
per source contract (distinct contracts) preserves document diversity. Gold
stays 100% human-annotated -> gold_quality='crisp'.
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
N_TARGET = 30                # iter_4: scale 8 -> ~30 crisp legal docs
DIV_CAP = 6                  # iter_4: relaxed diversity cap (was 2) per inferred type
WSPAN = 3200                 # max char extent of a clustered excerpt window

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

# clean-boundary regex for excerpt snapping (paragraph / sentence / clause ends)
_BOUNDARY = re.compile(r"\n\n|\n|\.\s|;\s|:\s")


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


def _norm_title(title: str) -> str:
    """Human-readable contract-type token from a CUAD filename-style title.
    e.g. 'LIMEENERGYCO_..-EX-10-DISTRIBUTOR AGREEMENT' -> 'DISTRIBUTOR AGREEMENT'."""
    tail = re.split(r"[-_]", title)[-1].strip()
    return tail if len(tail) >= 3 else title.strip()


# --------------------------------------------------------------------------- #
# Excerpt-window helpers (deterministic, clean-boundary, re-based + re-verified)
# --------------------------------------------------------------------------- #
def _snap_left(ctx: str, pos: int, lookback: int = 600) -> int:
    if pos <= 0:
        return 0
    lo = max(0, pos - lookback)
    cands = [m.end() for m in _BOUNDARY.finditer(ctx[lo:pos])]
    return lo + cands[-1] if cands else pos


def _snap_right(ctx: str, pos: int, lookahead: int = 600) -> int:
    L = len(ctx)
    if pos >= L:
        return L
    hi = min(L, pos + lookahead)
    m = _BOUNDARY.search(ctx[pos:hi])
    return pos + m.end() if m else hi


def _snap_right_within(ctx: str, ws: int, max_len: int) -> int:
    """Largest clean boundary at or before ws+max_len (never mid-sentence)."""
    L = len(ctx)
    hi = min(L, ws + max_len)
    if hi >= L:
        return L
    cands = [m.end() for m in _BOUNDARY.finditer(ctx[ws:hi])]
    return ws + cands[-1] if cands else hi


def _snap_window(ctx: str, rs: int, re_: int):
    """Snap a raw [rs,re_) cluster to a clean, in-band [ws,we) window."""
    L = len(ctx)
    cluster_len = re_ - rs
    want = min(max(cluster_len + 600, 1800), HI - 150)
    pad = max(0, want - cluster_len)
    ws = _snap_left(ctx, max(0, rs - pad // 2))
    we = _snap_right(ctx, min(L, re_ + (pad - pad // 2)))
    if we - ws > HI:                         # too long -> pull right edge to a boundary
        we = _snap_right_within(ctx, ws, HI)
    if we - ws < LO:                         # too short -> extend right to a boundary
        we = max(we, _snap_right(ctx, ws + LO + 150))
        we = min(we, _snap_right_within(ctx, ws, HI), L)
    return ws, we


def _best_window(ctx: str, spans, docname_span):
    """Pick the in-band window maximizing contained clause spans (>=3), with a
    bonus for containing the Document Name / a Parties span. spans: (s,e,cat)."""
    if len(spans) < MIN_FACTS:
        return None
    ss = sorted(spans)
    n = len(ss)
    best = None  # (key, ws, we); key=(score, -ws) maximized
    for i in range(n):
        j = i
        while j < n and ss[j][1] - ss[i][0] <= WSPAN:
            j += 1
        cluster = ss[i:j]
        if len(cluster) < MIN_FACTS:
            continue
        rs = cluster[0][0]
        re_ = max(e for _, e, _ in cluster)
        ws, we = _snap_window(ctx, rs, re_)
        if not (LO <= we - ws <= HI):
            continue
        contained = [sp for sp in ss if ws <= sp[0] and sp[1] <= we]
        if len(contained) < MIN_FACTS:
            continue
        cats_in = {c for _, _, c in contained}
        has_dn = docname_span is not None and ws <= docname_span[0] and docname_span[1] <= we
        score = len(contained) + (3 if has_dn else 0) + (2 if "Parties" in cats_in else 0)
        key = (score, -ws)
        if best is None or key > best[0]:
            best = (key, ws, we)
    return (best[1], best[2]) if best else None


def _local_catans(all_spans, ws: int, we: int):
    """Local (re-based) cat_ans + parties from spans fully inside [ws,we)."""
    cat_ans, parties = {}, []
    for s, e, cat, txt in sorted(all_spans):
        if not (ws <= s and e <= we):
            continue
        if cat == "Parties":
            parties.append({"text": txt, "answer_start": s - ws})
        elif cat not in cat_ans:
            cat_ans[cat] = {"text": txt, "answer_start": s - ws}
    return cat_ans, parties


# --------------------------------------------------------------------------- #
# CUAD answer collection
# --------------------------------------------------------------------------- #
def _collect_whole(ctx: str, qas):
    """First answer per category (excl Parties) + all distinct Parties; verified."""
    cat_ans, parties, seen_p = {}, [], set()
    for q in qas:
        if not q["answers"]:
            continue
        cat = _cat_of(q["question"])
        if cat not in CAT_MAP:
            continue
        if cat == "Parties":
            for a in q["answers"]:
                if a["text"] in seen_p:
                    continue
                s = a["answer_start"]
                if ctx[s:s + len(a["text"])] == a["text"]:
                    parties.append({"text": a["text"], "answer_start": s})
                    seen_p.add(a["text"])
        elif cat not in cat_ans:
            a = q["answers"][0]
            s = a["answer_start"]
            if ctx[s:s + len(a["text"])] == a["text"]:
                cat_ans[cat] = {"text": a["text"], "answer_start": s}
    return cat_ans, parties


def _all_spans(ctx: str, qas):
    out = []
    for q in qas:
        if not q["answers"]:
            continue
        cat = _cat_of(q["question"])
        if cat not in CAT_MAP:
            continue
        for a in q["answers"]:
            s = a["answer_start"]
            e = s + len(a["text"])
            if 0 <= s < e <= len(ctx) and ctx[s:e] == a["text"]:
                out.append((s, e, cat, a["text"]))
    return out


def _docname(ctx: str, qas):
    for q in qas:
        if _cat_of(q["question"]) == "Document Name" and q["answers"]:
            a = q["answers"][0]
            s = a["answer_start"]
            if ctx[s:s + len(a["text"])] == a["text"]:
                return a["text"], s
    return None, None


# --------------------------------------------------------------------------- #
# Shared (head, relation, tail) builder -- identical for whole + excerpt docs
# --------------------------------------------------------------------------- #
def _facts_from_catans(local_ctx: str, agr_name: str, agr_span, cat_ans, parties):
    """Build entities + facts from a LOCAL context (whole contract or excerpt).
    cat_ans answer_start values are LOCAL to local_ctx; agr_span (Document Name
    entity) is LOCAL or None. Mirrors the iter_2 logic exactly."""
    entities, facts, vocab, fine = [], [], [], {}
    if agr_span is not None and local_ctx[agr_span[0]:agr_span[1]] == agr_name:
        entities.append({"name": agr_name, "type": "MISC",
                         "char_span": [agr_span[0], agr_span[1]], "_fine": "AGREEMENT"})
    # spaCy NER over the contract/excerpt for parties/dates/jurisdictions/amounts
    for e in C.spacy_entities(local_ctx, allowed_labels={"ORG", "PERSON", "GPE", "LOC",
                                                         "DATE", "MONEY", "PERCENT", "LAW"}):
        entities.append(e)

    for cat, a in cat_ans.items():
        rel, kind = CAT_MAP[cat]
        vocab.append(rel)
        if kind == "value":
            tail, span = _trim_value(a["text"], a["answer_start"], 120)
            if local_ctx[span[0]:span[1]] != tail or len(tail.strip()) < 2:
                continue
            facts.append({"head": agr_name, "relation": rel, "tail": tail,
                          "provenance_char_span": span})
            ftype = C.coarse_type(tail)
            if rel in ("agreement_date", "effective_date", "expiration_date",
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

    for pa in parties:
        cleaned = _clean_party(pa["text"], pa["answer_start"], local_ctx)
        if not cleaned:
            continue
        ptail, pspan = cleaned
        facts.append({"head": agr_name, "relation": "has_party",
                      "tail": ptail, "provenance_char_span": pspan})
        vocab.append("has_party")
        fine[ptail] = "has_party"
        entities.append({"name": ptail, "type": "ORG", "char_span": pspan, "_fine": "has_party"})
    return entities, facts, vocab, fine


def build():
    data = json.loads(CUAD.read_text())["data"]
    arts = sorted(data, key=lambda a: a["title"])   # deterministic order

    whole_cands, long_arts = [], []
    for art in arts:
        ctx = art["paragraphs"][0]["context"]
        qas = art["paragraphs"][0]["qas"]
        title = art["title"]
        if LO <= len(ctx) <= HI:
            cat_ans, parties = _collect_whole(ctx, qas)
            nval = sum(1 for c in cat_ans if c in VALUE_CATS)
            if "Document Name" in cat_ans and nval >= 2 and (len(cat_ans) + len(parties)) >= MIN_FACTS:
                whole_cands.append((title, ctx, cat_ans, parties, len(cat_ans) + len(parties)))
        elif len(ctx) > HI:
            long_arts.append((title, ctx, qas))
    logger.info(f"CUAD whole-contract in-band candidates (>=3 facts): {len(whole_cands)}; "
                f"long contracts (windowable pool): {len(long_arts)}")

    chosen = []   # ("whole"|"excerpt", title, local_ctx, cat_ans, parties, extra)
    type_count = {}
    seen_text = set()   # dedup distinct-title contracts with byte-identical context

    # 1) whole-contract docs first (richest first, relaxed diversity cap)
    whole_cands.sort(key=lambda x: (-x[4], x[0]))
    for title, ctx, cat_ans, parties, _nf in whole_cands:
        ty = _infer_type(title)
        if type_count.get(ty, 0) >= DIV_CAP:
            continue
        if ctx in seen_text:
            continue
        seen_text.add(ctx)
        chosen.append(("whole", title, ctx, cat_ans, parties, None))
        type_count[ty] = type_count.get(ty, 0) + 1
        if len(chosen) >= N_TARGET:
            break
    n_whole = len(chosen)
    logger.info(f"CUAD whole-contract chosen: {n_whole} (types={type_count})")

    # 2) excerpt windows from long contracts (one per distinct contract) to top up
    for title, ctx, qas in long_arts:
        if len(chosen) >= N_TARGET:
            break
        ty = _infer_type(title)
        if type_count.get(ty, 0) >= DIV_CAP:
            continue
        spans = _all_spans(ctx, qas)
        if len(spans) < MIN_FACTS:
            continue
        dn_text, dn_start = _docname(ctx, qas)
        dn_span = None
        if dn_text is not None:
            dn_span = _trim_value(dn_text, dn_start, 90)[1]
        win = _best_window(ctx, [(s, e, cat) for (s, e, cat, _) in spans], dn_span)
        if not win:
            continue
        ws, we = win
        excerpt = ctx[ws:we]
        if excerpt in seen_text:
            continue
        cat_ans_l, parties_l = _local_catans(spans, ws, we)
        if len(cat_ans_l) + len(parties_l) < MIN_FACTS:
            continue
        seen_text.add(excerpt)
        agr_name = _trim_value(dn_text, dn_start, 90)[0] if dn_text is not None else _norm_title(title)
        agr_span = None
        if dn_span is not None and ws <= dn_span[0] and dn_span[1] <= we:
            cand = [dn_span[0] - ws, dn_span[1] - ws]
            if excerpt[cand[0]:cand[1]] == agr_name:
                agr_span = cand
        chosen.append(("excerpt", title, excerpt, cat_ans_l, parties_l, (ws, we, agr_name, agr_span)))
        type_count[ty] = type_count.get(ty, 0) + 1
    logger.info(f"CUAD total chosen: {len(chosen)} ({n_whole} whole + "
                f"{len(chosen) - n_whole} excerpt); types={type_count}")

    rows = []
    for ci, (kind, title, local_ctx, cat_ans, parties, extra) in enumerate(chosen):
        doc_id = f"legal_cuad_{ci:02d}"
        if kind == "whole":
            dn = cat_ans["Document Name"]
            agr_name, agr_span = _trim_value(dn["text"], dn["answer_start"], 90)
            if local_ctx[agr_span[0]:agr_span[1]] != agr_name:
                agr_span = [dn["answer_start"], dn["answer_start"] + len(dn["text"])]
                agr_name = dn["text"]
            cat_ans_use = {c: a for c, a in cat_ans.items() if c != "Parties"}
            window_meta = {"excerpt": False}
        else:
            ws, we, agr_name, agr_span = extra
            cat_ans_use = cat_ans
            window_meta = {"excerpt": True, "excerpt_char_window": [ws, we]}

        ents, facts, vocab, fine = _facts_from_catans(local_ctx, agr_name, agr_span, cat_ans_use, parties)
        try:
            extra_meta = {"contract_title": title,
                          "source_dataset": "CUAD v1 (theatticusproject)",
                          "source_url": "https://zenodo.org/records/4595826",
                          "annotation": "human-annotated CUAD clause spans"}
            extra_meta.update(window_meta)
            row = C.make_row(
                doc_id=doc_id, document_text=local_ctx, genre="legal", source=f"CUAD:{title}",
                entities=ents, facts=facts, license=LICENSE, gold_quality="crisp",
                relation_vocab=vocab, extra_meta=extra_meta,
            )
            rows.append(row)
            logger.info(f"{doc_id}[{kind[:3]}]: len={len(local_ctx)} facts={row['metadata_num_facts']} "
                        f"ents={row['metadata_num_entities']} :: {title[:46]}")
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
