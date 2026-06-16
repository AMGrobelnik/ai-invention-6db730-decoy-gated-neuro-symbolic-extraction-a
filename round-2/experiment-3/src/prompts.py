#!/usr/bin/env python3
"""Verbatim-style prompt builders. Document text is placed FIRST (prefix) so that
provider prompt-caching can amortize it across the many isolated calls per document."""
from __future__ import annotations

ENTITY_TYPES = "PER (person), ORG (organization), LOC (location), TIME (date/period), NUM (number), MISC (other named entity)"

# ------------------------------- EXTRACTION (over-generate) ----------------------------
def extract_prompt(document: str) -> list[dict]:
    sys = (
        "You are a precise relation-extraction engine. From the DOCUMENT you list every "
        "plausible atomic factual relation between two named entities. Include relations that "
        "are explicitly stated AND ones that are only lightly/locally inferable. Over-generate: "
        "it is better to propose a borderline relation than to miss one. "
        f"Entity types: {ENTITY_TYPES}. "
        "Output ONLY JSON Lines, one compact JSON object per line, no prose, of the form: "
        '{"head":"<entity surface>","head_type":"PER","relation":"<short relation phrase>",'
        '"tail":"<entity surface>","tail_type":"LOC"}'
    )
    return [
        {"role": "system", "content": sys},
        {"role": "user", "content": f"DOCUMENT:\n{document}\n\nList the atomic relations as JSON Lines:"},
    ]


# ------------------------------- ISOLATED CONFIDENCE SCORING ---------------------------
def score_prompt(document: str, head: str, relation: str, tail: str) -> list[dict]:
    """Isolated, provenance-blinded verbalized [0,1] confidence (used identically for
    real candidates AND their decoys -> the only thing that differs is the statement)."""
    sys = (
        "You judge whether a single candidate statement is supported by a document. "
        "Read the DOCUMENT, then for the STATEMENT give the probability in [0,1] that the "
        "statement is explicitly stated or directly entailed by the document. Be calibrated: "
        "use values near 1.0 only when the document clearly supports it, near 0.0 when it does "
        'not. Output ONLY a JSON object: {"p": <number between 0 and 1>}.'
    )
    statement = f'"{head}" — {relation} — "{tail}"'
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": f"DOCUMENT:\n{document}\n\nSTATEMENT: {statement}\n\nJSON probability:"},
    ]


# ------------------------------- LOGPROB YES/NO SCORING (graded, de-saturated) ---------
def yesno_prompt(document: str, head: str, relation: str, tail: str) -> list[dict]:
    """One-token yes/no entailment prompt; the yes-token probability (from logprobs) is a
    graded, upper-tail-discriminative confidence used identically for reals and decoys."""
    sys = ("Answer whether the STATEMENT is explicitly stated or directly entailed by the "
           "DOCUMENT. Reply with exactly one word: yes or no.")
    statement = f'"{head}" — {relation} — "{tail}"'
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": f"DOCUMENT:\n{document}\n\nSTATEMENT: {statement}\n\nAnswer (yes or no):"},
    ]


# ------------------------------- COUNTERFACTUAL DECOY GENERATION -----------------------
def decoy_prompt(document: str, relation: str, head_type: str, tail_type: str,
                 entity_names: list[str] | None = None) -> list[dict]:
    """Property-matched (DeepCoy) counterfactual decoy: recombine the DOCUMENT'S OWN entities
    into a FALSE pairing, so the decoy is as document-grounded as the real candidate (same
    surface form / specificity) and the scorer is genuinely uncertain -> a fair knockoff
    competition. Out-of-document entities would make the decoy trivially rejectable (Zt~0)
    and collapse W to Z."""
    ents = ", ".join((entity_names or [])[:24])
    # NOTE: build via f-string/concatenation only — never %-format, because `relation` can
    # contain a literal '%' (e.g. "garnered 28.2% ratings") which would corrupt a format string.
    sys = (
        "You generate a counterfactual DECOY fact for a false-discovery-rate control test. "
        "Build a BELIEVABLE but FALSE fact by RECOMBINING entities that appear in THIS document, "
        "so the decoy is exactly as well-grounded as the real facts yet is NOT actually supported "
        "by the text. Keep the relation EXACTLY as given; pick a head and a tail from the "
        f"document's entities (prefer head type {head_type}, tail type {tail_type}) that the "
        "document does NOT link by this relation — the kind of plausible mistake a hurried reader "
        "might make. Do NOT reproduce any fact that is actually stated or entailed by the document. "
        'Output ONLY a JSON object with string keys "head", "relation", "tail" '
        "(keep \"relation\" equal to the given relation)."
    )
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": (f"DOCUMENT:\n{document}\n\nDOCUMENT ENTITIES: {ents}\n\n"
                     f"Produce one plausible but FALSE {relation} fact that recombines this "
                     f"document's entities, as JSON:")},
    ]


def entail_check_prompt(document: str, head: str, relation: str, tail: str) -> list[dict]:
    sys = (
        "You check entailment. Given the DOCUMENT and a STATEMENT, answer whether the statement "
        'is stated or directly entailed by the document. Output ONLY: {"entailed": true} or '
        '{"entailed": false}.'
    )
    statement = f'"{head}" — {relation} — "{tail}"'
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": f"DOCUMENT:\n{document}\n\nSTATEMENT: {statement}\n\nJSON:"},
    ]


# ------------------------------- BASELINE: CoT ----------------------------------------
def cot_prompt(document: str) -> list[dict]:
    sys = (
        "You extract relational facts from a document using careful step-by-step reasoning. "
        "First think briefly, then emit the final facts. "
        f"Entity types: {ENTITY_TYPES}. "
        "End your answer with a line 'TRIPLES:' followed by JSON Lines, one per line: "
        '{"head":"...","head_type":"PER","relation":"<phrase>","tail":"...","tail_type":"LOC","confidence":<0..1>}.'
    )
    return [
        {"role": "system", "content": sys},
        {"role": "user", "content": f"DOCUMENT:\n{document}\n\nReason, then give TRIPLES:"},
    ]


# ------------------------------- BASELINE: RAG (retrieved context) ---------------------
def rag_prompt(retrieved_sentences: list[str], title: str) -> list[dict]:
    ctx = "\n".join(f"- {s}" for s in retrieved_sentences)
    sys = (
        "You extract relational facts ONLY from the retrieved passages provided (do not use "
        f"outside knowledge). Entity types: {ENTITY_TYPES}. "
        "Output ONLY JSON Lines: "
        '{"head":"...","head_type":"PER","relation":"<phrase>","tail":"...","tail_type":"LOC","confidence":<0..1>}.'
    )
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": f"TOPIC: {title}\nRETRIEVED PASSAGES:\n{ctx}\n\nExtract the relational facts as JSON Lines:"},
    ]


# ------------------------------- RELATION ALIGNMENT (LLM pick) -------------------------
def relation_pick_prompt(relation_phrase: str, shortlist: list[tuple[str, str, str]]) -> list[dict]:
    """shortlist: list of (pcode, name, description). Returns one P-code or NO_RELATION."""
    opts = "\n".join(f"{pc} = {name}: {desc[:90]}" for pc, name, desc in shortlist)
    sys = (
        "You map a free-text relation phrase to the single best-matching Wikidata property code "
        "from the candidate list, or to NO_RELATION if none fits. "
        'Output ONLY a JSON object: {"pcode": "P131"} or {"pcode": "NO_RELATION"}.'
    )
    return [
        {"role": "system", "content": sys},
        {"role": "user",
         "content": f"RELATION PHRASE: '{relation_phrase}'\n\nCANDIDATES:\n{opts}\nNO_RELATION = none of the above\n\nJSON:"},
    ]
