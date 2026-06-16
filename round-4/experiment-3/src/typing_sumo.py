#!/usr/bin/env python3
"""
typing_sumo.py — offline WordNet -> coarse-type -> SUMO-class argument typing.

Recipe (SPEC_PIPE Block C + SPEC_GND Block B): head noun -> wn.synsets(word, pos=NOUN)
-> hypernym_paths() -> presence of anchor synsets:
    person.n.01                       -> PER  / &%Human
    location.n.01, region.n.03        -> LOC  / &%GeographicArea
    organization.n.01, social_group.n.01 -> ORG / &%Organization (&%Group)
    time_period.n.01                  -> TIME / &%TimePosition
    number.n.02, measure.n.02         -> NUM  / &%Quantity (&%Number)
else MISC / &%Entity. The SUMO suffix convention (=,+,@) from WordNetMappings30 is honoured
where a direct anchor is hit (person -> &%Human=, the verified line in SPEC_GND).

Typing is used ONLY to constrain type-matched swaps / entrapment to the same SUMO class.
It is NEVER used to filter candidates, so it cannot affect the FDR guarantee.
The dataset's coarse {PER,LOC,ORG,TIME,NUM,MISC} type is used as a robust fallback.
"""
from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path

# point NLTK at the venv-local corpus downloaded at setup time
_HERE = Path(__file__).resolve().parent
for _p in (_HERE / ".venv" / "nltk_data", Path.home() / "nltk_data"):
    if _p.exists():
        os.environ.setdefault("NLTK_DATA", str(_p))
        import nltk  # noqa: E402
        if str(_p) not in nltk.data.path:
            nltk.data.path.insert(0, str(_p))

try:
    from nltk.corpus import wordnet as wn
    _WN_OK = True
    # force-load so the first lookup doesn't race
    wn.ensure_loaded()
except Exception:  # pragma: no cover - exercised only if corpus missing
    wn = None
    _WN_OK = False

# anchor synset name -> (coarse, sumo class with WordNetMappings30 suffix)
_ANCHORS = [
    ("person.n.01", "PER", "&%Human="),
    ("organization.n.01", "ORG", "&%Organization="),
    ("social_group.n.01", "ORG", "&%Group+"),
    ("location.n.01", "LOC", "&%GeographicArea+"),
    ("region.n.03", "LOC", "&%GeographicArea+"),
    ("time_period.n.01", "TIME", "&%TimePosition+"),
    ("measure.n.02", "NUM", "&%Quantity+"),
    ("number.n.02", "NUM", "&%Number="),
]

# coarse dataset type -> SUMO class (fallback when WordNet gives nothing)
COARSE_TO_SUMO = {
    "PER": "&%Human=",
    "ORG": "&%Organization=",
    "LOC": "&%GeographicArea+",
    "TIME": "&%TimePosition+",
    "NUM": "&%Quantity+",
    "MISC": "&%Entity+",
}

_DATE_RE = re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4}|\d{4}|january|february|march|april|may|june|"
                      r"july|august|september|october|november|december|monday|tuesday|"
                      r"wednesday|thursday|friday|saturday|sunday)\b", re.I)
_NUM_RE = re.compile(r"\d")


def _head_noun(name: str) -> str:
    """Last alphabetic token, lowercased — a cheap head-noun heuristic."""
    toks = re.findall(r"[A-Za-z]+", name or "")
    return toks[-1].lower() if toks else ""


@lru_cache(maxsize=4096)
def wordnet_type(word: str) -> tuple[str | None, str | None]:
    """Type a single noun via WordNet hypernym paths. Returns (coarse, sumo) or (None, None)."""
    if not _WN_OK or not word:
        return None, None
    try:
        syns = wn.synsets(word, pos=wn.NOUN)
    except Exception:
        return None, None
    if not syns:
        return None, None
    anchor_names = {a[0] for a in _ANCHORS}
    # scan the dominant senses; first anchor encountered (closest to root order) wins
    for syn in syns[:3]:
        try:
            paths = syn.hypernym_paths()
        except Exception:
            continue
        path_names = {s.name() for p in paths for s in p}
        for aname, coarse, sumo in _ANCHORS:
            if aname in path_names:
                return coarse, sumo
    return None, None


def type_entity(name: str, coarse_fallback: str | None = None) -> dict:
    """Return {'coarse', 'sumo', 'source'} for an entity surface form.

    Priority: WordNet head-noun anchor -> dataset coarse fallback -> surface regex
    (digits/dates) -> MISC. Numbers/dates are recognised by regex first because the
    dataset's PER/ORG spaCy labels are unreliable for value tails (legal dates, reg ids).
    """
    # surface shortcuts for value-like tails (dates, section numbers, money, percentages)
    if _DATE_RE.search(name or ""):
        return {"coarse": "TIME", "sumo": "&%TimePosition+", "source": "regex_date"}
    coarse, sumo = wordnet_type(_head_noun(name))
    if coarse is not None:
        return {"coarse": coarse, "sumo": sumo, "source": "wordnet"}
    if _NUM_RE.search(name or "") and not re.search(r"[A-Za-z]{3,}", name or ""):
        return {"coarse": "NUM", "sumo": "&%Quantity+", "source": "regex_num"}
    if coarse_fallback in COARSE_TO_SUMO:
        return {"coarse": coarse_fallback, "sumo": COARSE_TO_SUMO[coarse_fallback],
                "source": "dataset_coarse"}
    return {"coarse": "MISC", "sumo": "&%Entity+", "source": "default"}


def selftest() -> None:
    assert _WN_OK, "WordNet corpus not available"
    c, s = wordnet_type("person")
    assert c == "PER" and s.startswith("&%Human"), f"person -> {c},{s}"
    c, s = wordnet_type("organization")
    assert c == "ORG" and s.startswith("&%Organization"), f"organization -> {c},{s}"
    c, s = wordnet_type("company")
    assert c == "ORG", f"company -> {c}"  # company is-a organization
    # value tails
    assert type_entity("March 27, 2006")["coarse"] == "TIME"
    assert type_entity("55")["coarse"] == "NUM"            # bare numeric tail
    assert type_entity("Zorptech", "ORG")["coarse"] == "ORG"  # no WN sense -> coarse fallback
    print("typing_sumo selftest PASSED")


if __name__ == "__main__":
    selftest()
