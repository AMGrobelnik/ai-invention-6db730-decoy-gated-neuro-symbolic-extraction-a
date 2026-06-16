"""
pipeline.py
===========
The LLM-facing stages of the FDR gate (all calls isolated + provenance-blinded):

  MODULE 2  extraction with over-generation (atomic + bridge, T=0.7, n=3, union, cap 20/family)
  MODULE 3  counterfactual decoys + non-entailment gate + swap-decoy negative control
  MODULE 6  deterministic entrapment items (cross-doc swap + explicit contradiction), r=1
  MODULE 4  isolated scoring elicitations: verbalized / logprob_yesno / self_consistency / DINCO

A candidate is a triple (head, relation, tail) read as "tail is head's relation".
Scoring is provenance-blinded: every item (real / counterfactual-decoy / swap-decoy /
entrapment) is scored by the SAME isolated prompt, so the scorer cannot tell the source.
"""
from __future__ import annotations

import json
import math
import re
from typing import Sequence

import numpy as np

VOCAB = ["aunt", "brother", "daughter", "daughter-in-law", "father", "father-in-law",
         "granddaughter", "grandfather", "grandmother", "grandson", "husband", "mother",
         "mother-in-law", "nephew", "niece", "sister", "son", "son-in-law", "uncle", "wife"]
VOCAB_SET = set(VOCAB)

# gender / generation-opposite map used to manufacture explicit-contradiction entrapment
CONTRADICTION = {
    "father": "mother", "mother": "father", "son": "daughter", "daughter": "son",
    "brother": "sister", "sister": "brother", "husband": "wife", "wife": "husband",
    "uncle": "aunt", "aunt": "uncle", "nephew": "niece", "niece": "nephew",
    "grandfather": "grandmother", "grandmother": "grandfather",
    "grandson": "granddaughter", "granddaughter": "grandson",
    "father-in-law": "mother-in-law", "mother-in-law": "father-in-law",
    "son-in-law": "daughter-in-law", "daughter-in-law": "son-in-law",
}


def fact_nl(h: str, r: str, t: str) -> str:
    """Natural-language verbalization of (h,r,t): 'tail is head's relation'."""
    return f"{t} is {h}'s {r}"


def _extract_json_array(text: str):
    """Robustly pull the first JSON array of objects out of an LLM response."""
    if not text:
        return []
    # try fenced or raw array
    m = re.search(r"\[.*\]", text, flags=re.DOTALL)
    if m:
        try:
            arr = json.loads(m.group(0))
            if isinstance(arr, list):
                return arr
        except Exception:
            pass
    # line-by-line fallback: each line a json object
    out = []
    for line in text.splitlines():
        line = line.strip().rstrip(",")
        if line.startswith("{") and line.endswith("}"):
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    return out


def _clean_triples(raw_list, entities: set, cap: int):
    """Keep only well-formed {head,relation,tail} triples with in-vocab relation and
    known entities; dedup; head!=tail; cap. Returns (triples, n_seen, n_discarded)."""
    seen = set()
    out = []
    n_seen = 0
    for obj in raw_list:
        if not isinstance(obj, dict):
            continue
        n_seen += 1
        h = str(obj.get("head", "")).strip()
        r = str(obj.get("relation", "")).strip().lower()
        t = str(obj.get("tail", "")).strip()
        if h in entities and t in entities and h != t and r in VOCAB_SET:
            key = (h, r, t)
            if key not in seen:
                seen.add(key)
                out.append({"head": h, "relation": r, "tail": t})
        if len(out) >= cap:
            break
    n_disc = n_seen - len(out)
    return out, n_seen, n_disc


# ============================================================================
# MODULE 2 -- extraction with over-generation
# ============================================================================
ATOMIC_INSTR = (
    "You extract kinship relations from a short story.\n"
    "From the STORY, list every kinship relation that is DIRECTLY STATED between two people.\n"
    "Use ONLY these people: {entities}.\n"
    "Use ONLY these relation words: {vocab}.\n"
    "A triple {{\"head\":H,\"relation\":R,\"tail\":T}} means: 'T is H's R' (e.g. "
    "{{\"head\":\"Gabrielle\",\"relation\":\"grandson\",\"tail\":\"Dan\"}} means 'Dan is Gabrielle's grandson').\n"
    "Output ONLY a JSON array of such triples, nothing else."
)
BRIDGE_INSTR = (
    "You infer kinship relations from a short story.\n"
    "List ADDITIONAL kinship relations between people that are IMPLIED but NOT directly stated "
    "(multi-hop, derived by chaining the stated relations).\n"
    "Use ONLY these people: {entities}.\n"
    "Use ONLY these relation words: {vocab}.\n"
    "A triple {{\"head\":H,\"relation\":R,\"tail\":T}} means: 'T is H's R'.\n"
    "Give your BEST GUESS for the relationship of as many connected pairs as you can, even if "
    "you are not fully certain. Output ONLY a JSON array of such triples, nothing else."
)


async def extract_candidates(llm, doc, n_samples=3, cap_per_family=20):
    """Two-pass over-generation extraction. Returns dict with 'atomic'/'bridge' candidate
    triple lists (family-tagged) plus discard stats."""
    story = doc["document_text"]
    entities = [e["name"] for e in doc["entities"]]
    ent_set = set(entities)
    ent_str = ", ".join(entities)
    vocab_str = ", ".join(VOCAB)

    async def one_pass(instr, kind):
        union = []
        for s in range(n_samples):
            sys = instr.format(entities=ent_str, vocab=vocab_str)
            msgs = [{"role": "system", "content": sys},
                    {"role": "user", "content": f"STORY:\n{story}\n\nJSON array:"}]
            resp = await llm.chat(msgs, kind=kind, temperature=0.7, max_tokens=900, sample_idx=s)
            union.extend(_extract_json_array(resp["content"]))
        return union

    atomic_raw = await one_pass(ATOMIC_INSTR, "extract_atomic")
    bridge_raw = await one_pass(BRIDGE_INSTR, "extract_bridge")
    atomic, a_seen, a_disc = _clean_triples(atomic_raw, ent_set, cap_per_family)
    bridge, b_seen, b_disc = _clean_triples(bridge_raw, ent_set, cap_per_family)
    return {"atomic": atomic, "bridge": bridge,
            "discard": {"atomic_seen": a_seen, "atomic_disc": a_disc,
                        "bridge_seen": b_seen, "bridge_disc": b_disc}}


# ============================================================================
# MODULE 3 -- decoys
# ============================================================================
DECOY_INSTR = (
    "You write a single PLAUSIBLE but FALSE kinship statement about a story's characters.\n"
    "People available: {entities}. Relation words allowed: {vocab}.\n"
    "Produce ONE kinship triple {{\"head\":H,\"relation\":R,\"tail\":T}} (meaning 'T is H's R') that:\n"
    "  - is plausible for this family genre and matches the style of the real relations, AND\n"
    "  - is NOT stated or entailed by the story (it must be FALSE given the story).\n"
    "Reuse the head '{head}' if you can, so the statement matches in type/structure.\n"
    "Output ONLY the JSON triple."
)
ENTAIL_INSTR = (
    "You judge entailment against a short story. Answer with exactly one word: Yes or No.\n"
    "Is the statement ENTAILED (logically implied or directly stated) by the story?"
)


async def make_counterfactual_decoy(llm, doc, real, max_tries=3):
    """Generate a property-matched counterfactual decoy for `real`, verified non-entailed.
    Returns (decoy_triple, contamination_flag) where contamination_flag counts an entailed
    (rejected) generation. Falls back to a deterministic swap if generation keeps failing."""
    story = doc["document_text"]
    entities = [e["name"] for e in doc["entities"]]
    ent_str = ", ".join(entities)
    vocab_str = ", ".join(VOCAB)
    contaminated = 0
    for attempt in range(max_tries):
        sys = DECOY_INSTR.format(entities=ent_str, vocab=vocab_str, head=real["head"])
        msgs = [{"role": "system", "content": sys},
                {"role": "user", "content": f"STORY:\n{story}\n\nReal relation to mirror in style: "
                                             f"'{fact_nl(**_hrt(real))}'. JSON triple:"}]
        resp = await llm.chat(msgs, kind="decoy_gen", temperature=0.7, max_tokens=80, sample_idx=attempt)
        arr = _extract_json_array(resp["content"])
        cand = None
        if arr and isinstance(arr[0], dict):
            cand = arr[0]
        else:
            obj = re.search(r"\{[^{}]*\}", resp["content"] or "", flags=re.DOTALL)
            if obj:
                try:
                    cand = json.loads(obj.group(0))
                except Exception:
                    cand = None
        if not cand:
            continue
        h = str(cand.get("head", "")).strip()
        r = str(cand.get("relation", "")).strip().lower()
        t = str(cand.get("tail", "")).strip()
        if h not in entities or t not in entities or h == t or r not in VOCAB_SET:
            continue
        decoy = {"head": h, "relation": r, "tail": t}
        if (h, r, t) == _hrt_tuple(real):
            continue
        # non-entailment verification (isolated, T=0.0)
        entailed = await _is_entailed(llm, story, decoy)
        if entailed:
            contaminated = 1
            continue
        return decoy, contaminated
    # fallback: deterministic non-entailed swap (guaranteed by construction below)
    return make_swap_decoy(doc, real, seed_offset=997), contaminated


async def _is_entailed(llm, story, triple) -> bool:
    msgs = [{"role": "system", "content": ENTAIL_INSTR},
            {"role": "user", "content": f"STORY:\n{story}\n\nSTATEMENT: {fact_nl(**_hrt(triple))}\nAnswer Yes or No:"}]
    resp = await llm.chat(msgs, kind="nonentail_check", temperature=0.0, max_tokens=16)
    return resp["content"].strip().lower().startswith("y")


def make_swap_decoy(doc, real, seed_offset=0):
    """Negative-control decoy (NO LLM): random type-matched swap of the tail to a different
    person in the same doc (predicted anti-conservative -- 'too easy')."""
    entities = [e["name"] for e in doc["entities"]]
    rng = np.random.default_rng(abs(hash((doc["doc_id"], _hrt_tuple(real), seed_offset))) % (2**32))
    others = [e for e in entities if e != real["head"] and e != real["tail"]]
    if not others:  # tiny doc: swap relation instead
        alt = [r for r in VOCAB if r != real["relation"]]
        return {"head": real["head"], "relation": str(rng.choice(alt)), "tail": real["tail"]}
    new_tail = str(rng.choice(others))
    return {"head": real["head"], "relation": real["relation"], "tail": new_tail}


# ============================================================================
# MODULE 6 -- deterministic entrapment (false-by-construction, r=1)
# ============================================================================
def make_entrapment(doc, real, all_docs_pool, gold_true, covered_pairs, idx):
    """One entrapment item per real (r=1), built WITHOUT the generating LLM, by a mechanism
    DISTINCT from the counterfactual decoys. Alternates two constructions:
      (a) explicit contradiction: a true covered pair (h,t) assigned the gender/generation-
          opposite relation (guaranteed false & non-entailed);
      (b) cross-document swap: a real triple from another doc remapped onto this doc's names.
    Both are deterministic. Returns (entrapment_triple, mechanism)."""
    rng = np.random.default_rng(abs(hash((doc["doc_id"], _hrt_tuple(real), "ent", idx))) % (2**32))
    use_contradiction = (idx % 2 == 0)
    if use_contradiction and real["relation"] in CONTRADICTION:
        contra = CONTRADICTION[real["relation"]]
        cand = {"head": real["head"], "relation": contra, "tail": real["tail"]}
        # ensure it is genuinely false (not accidentally a true gold triple)
        if (cand["head"], cand["relation"], cand["tail"]) not in gold_true:
            return cand, "contradiction"
    # cross-document swap: borrow a relation from another doc, remap onto this doc's people
    entities = [e["name"] for e in doc["entities"]]
    if len(entities) >= 2:
        other = all_docs_pool[int(rng.integers(0, len(all_docs_pool)))]
        rel = str(rng.choice(VOCAB))
        a, b = rng.choice(len(entities), size=2, replace=False)
        cand = {"head": entities[int(a)], "relation": rel, "tail": entities[int(b)]}
        if (cand["head"], cand["relation"], cand["tail"]) not in gold_true:
            return cand, "cross_doc"
    # last resort: contradiction of relation with a random tail
    alt = [r for r in VOCAB if r != real["relation"]]
    return {"head": real["head"], "relation": str(rng.choice(alt)), "tail": real["tail"]}, "fallback"


# ============================================================================
# MODULE 4 -- isolated scoring elicitations (return Z in [0,1])
# ============================================================================
SCORE_VERBALIZED = (
    "You assess whether a kinship statement is true given a short story.\n"
    "Respond with ONLY a single number between 0 and 1 = the probability the statement is "
    "true (entailed) given the story. No words, just the number."
)
SCORE_YESNO = (
    "You assess whether a kinship statement is entailed by a short story.\n"
    "Answer with exactly one word: Yes (entailed/true) or No (not entailed/false)."
)


def _hrt(tr):
    return {"h": tr["head"], "r": tr["relation"], "t": tr["tail"]}


def _hrt_tuple(tr):
    return (tr["head"], tr["relation"], tr["tail"])


async def score_verbalized(llm, story, triple, sample_idx=0) -> float:
    msgs = [{"role": "system", "content": SCORE_VERBALIZED},
            {"role": "user", "content": f"STORY:\n{story}\n\nSTATEMENT: {fact_nl(**_hrt(triple))}\nProbability:"}]
    resp = await llm.chat(msgs, kind="score_verbalized", temperature=0.0, max_tokens=16, sample_idx=sample_idx)
    return _parse_prob(resp["content"])


async def score_logprob_yesno(llm, story, triple) -> float:
    msgs = [{"role": "system", "content": SCORE_YESNO},
            {"role": "user", "content": f"STORY:\n{story}\n\nSTATEMENT: {fact_nl(**_hrt(triple))}\nAnswer Yes or No:"}]
    resp = await llm.chat(msgs, kind="score_logprob", temperature=0.0, max_tokens=16,
                          logprobs=True, top_logprobs=8)
    p_yes, p_no = 0.0, 0.0
    for tok in resp["first_token_top_logprobs"]:
        w = tok["token"].strip().lower()
        p = math.exp(tok["logprob"])
        if w.startswith("yes"):
            p_yes += p
        elif w.startswith("no"):
            p_no += p
    if p_yes + p_no > 0:
        return p_yes / (p_yes + p_no)
    # fallback to the generated word
    return 0.85 if resp["content"].strip().lower().startswith("y") else 0.15


async def score_self_consistency(llm, story, triple, n=5) -> float:
    yes = 0
    for s in range(n):
        msgs = [{"role": "system", "content": SCORE_YESNO},
                {"role": "user", "content": f"STORY:\n{story}\n\nSTATEMENT: {fact_nl(**_hrt(triple))}\nAnswer Yes or No:"}]
        resp = await llm.chat(msgs, kind="score_selfcons", temperature=0.7, max_tokens=16, sample_idx=s)
        if resp["content"].strip().lower().startswith("y"):
            yes += 1
    return yes / n


async def score_dinco(llm, story, triple, covered_for_pair=None, n_distractors=3) -> float:
    """DINCO (SPEC1 F.4): verbalize confidence on the main claim + self-generated distractors
    (other vocab relations for the SAME (h,t) pair), normalize: f_NVC(main)=f_VC(main)/max(1,sum).
    """
    h, t = triple["head"], triple["tail"]
    rng = np.random.default_rng(abs(hash((h, t, triple["relation"]))) % (2**32))
    alts = [r for r in VOCAB if r != triple["relation"]]
    rng.shuffle(alts)
    distractors = alts[:n_distractors]
    claims = [triple] + [{"head": h, "relation": r, "tail": t} for r in distractors]
    confs = []
    for i, c in enumerate(claims):
        confs.append(await score_verbalized(llm, story, c, sample_idx=100 + i))
    beta = max(1.0, sum(confs))
    return confs[0] / beta


def _parse_prob(text: str) -> float:
    if not text:
        return 0.5
    m = re.search(r"[-+]?\d*\.?\d+", text)
    if not m:
        return 0.5
    try:
        v = float(m.group(0))
    except Exception:
        return 0.5
    if v > 1.0:  # model answered on a 0-100 scale
        v = v / 100.0
    return float(min(1.0, max(0.0, v)))


ELICITATIONS = {
    "verbalized": lambda llm, story, tr: score_verbalized(llm, story, tr),
    "logprob_yesno": lambda llm, story, tr: score_logprob_yesno(llm, story, tr),
    "self_consistency": lambda llm, story, tr: score_self_consistency(llm, story, tr, n=5),
    "dinco": lambda llm, story, tr: score_dinco(llm, story, tr),
}
