#!/usr/bin/env python3
"""
prob_reasoner.py — the LLM-as-probabilistic-reasoner layer (P4 deliverable).

This module turns the deterministic backward-chaining KB (kb_engine.KB) of admitted,
provenance- and certificate-bearing facts + hand-authored genre bridge rules into a
PROBABILISTIC program whose every leaf carries an LLM-supplied, FDR-certificate-consistent
unification weight, and computes the MARGINAL probability of every derived multi-hop
conclusion via weighted model counting.

Two interchangeable, *equivalent* engines (validated against each other in selftest):
  * ProbLog (primary): get_evaluatable().create_from(PrologString(prog)).evaluate()  -> {Term:prob}
    exactly per the verified research spec (Part C.5 deterministic->probabilistic swap).
  * Pure-Python EXACT weighted-model-count fallback (if ProbLog cannot install/run on a
    minimal CPU image): enumerate truth assignments of the distinct grounded leaves that
    feed the rules, run the existing deterministic kb.derive_all on each present-subset, and
    accumulate the assignment probability whenever the queried conclusion is derivable.
    For independent Bernoulli leaves + deterministic monotone rules this is IDENTICAL to
    ProbLog's WMC. A noisy-OR proof-level approximation is used only if the relevant-leaf
    count exceeds an enumeration cap (flagged explicitly in the output).

The deterministic engine REMAINS the baseline: NO headline number depends on this module.
Here we only ADD a probabilistic marginal + a probabilistic trace-graph on top of the
already-derived (and already-gated) proofs.

Certificate -> weight mapping (research spec Part C.2):
  p_i = calibrate(Z_i)                          # Z_i = per-doc rank-normalized real score
  (i)  gate-consistent shrinkage  w_i = (1 - alpha_hat) * p_i        [DEFAULT, headline]
  (ii) per-pair margin            w_i = clip(0.5 + 0.5 * W_i, eps, 1-eps)
  (iii) identity / no-shrinkage   w_i = p_i  (alpha_hat = 0)         [sensitivity baseline]
  entrapment FDP_hat is carried at the leaf as a consistency prior (annotation only).
"""
from __future__ import annotations

import re
from collections import defaultdict

import kb_engine as kbe
from kb_engine import V  # noqa: F401  (re-exported for selftest convenience)

EPS = 1e-3
ENUM_CAP = 18  # max distinct rule-feeding leaves for exact enumeration (2^18 = 262144)

# ---------------------------------------------------------------------------
# ProbLog availability (detected once at import; never fatal)
# ---------------------------------------------------------------------------
try:  # pragma: no cover - environment dependent
    from problog.program import PrologString
    from problog import get_evaluatable
    _PROBLOG_OK = True
except Exception:  # pragma: no cover
    PrologString = None
    get_evaluatable = None
    _PROBLOG_OK = False


def problog_available() -> bool:
    return _PROBLOG_OK


# ---------------------------------------------------------------------------
# Calibration + certificate -> weight maps
# ---------------------------------------------------------------------------
def calibrate(z, eps: float = EPS) -> float:
    """Z_i (per-doc rank-normalized real score in [0,1]) -> p_i in (0,1).

    DEFAULT = identity clamp: monotone, label-free (consistent with the label-free gate).
    Missing score -> 0.5 (no information)."""
    if z is None:
        return 0.5
    return min(1.0 - eps, max(eps, float(z)))


def weight_gate_consistent(z, alpha_hat: float, eps: float = EPS) -> float:
    """(i) DEFAULT: gate-consistent shrinkage w_i = (1 - alpha_hat) * calibrate(Z_i)."""
    p = calibrate(z, eps)
    ah = 0.0 if alpha_hat is None else float(alpha_hat)
    ah = min(1.0, max(0.0, ah))
    return min(1.0 - eps, max(eps, (1.0 - ah) * p))


def weight_margin(w_i, eps: float = EPS) -> float:
    """(ii) per-pair knockoff-margin weight w_i = clip(0.5 + 0.5*W_i, eps, 1-eps).

    W_i is the signed-max knockoff statistic built from rank-normalized real/decoy scores,
    so it already lives in [-1, 1]; the affine map sends the antisymmetric margin to a
    probability in (0,1) (0.5 at an exchangeable tie, ->1 as the real dominates its decoy)."""
    if w_i is None:
        return 0.5
    return min(1.0 - eps, max(eps, 0.5 + 0.5 * float(w_i)))


def weight_identity(z, eps: float = EPS) -> float:
    """(iii) identity / no-shrinkage baseline w_i = calibrate(Z_i) (alpha_hat = 0)."""
    return calibrate(z, eps)


# ---------------------------------------------------------------------------
# Prolog-atom sanitisation (functor slug + single-quoted constants) + back-map
# ---------------------------------------------------------------------------
def slug_functor(name: str) -> str:
    """Predicate functor -> valid lowercase Prolog atom: [^a-z0-9_]->'_', 'p_' prefix if
    it does not begin with a lowercase letter."""
    s = re.sub(r"[^a-z0-9_]", "_", str(name).lower())
    if not s or not s[0].isalpha():
        s = "p_" + s
    return s


def quote_const(name) -> str:
    """Entity constant -> single-quoted Prolog atom, inner quotes/backslashes escaped."""
    s = str(name).replace("\\", "\\\\").replace("'", "\\'")
    return "'" + s + "'"


def var_name(name: str) -> str:
    """kb_engine Var name -> valid Prolog variable (must start uppercase / underscore)."""
    s = re.sub(r"[^A-Za-z0-9_]", "_", str(name))
    if not s or not (s[0].isupper() or s[0] == "_"):
        s = "V_" + s
    return s


def _canon(atom_str: str) -> str:
    """Whitespace/quote-insensitive canonical key for matching ProbLog Term strings back
    to the (pred, args) we emitted. ProbLog drops unnecessary quotes in str(Term), so we
    strip quotes + whitespace on both sides before comparing."""
    return atom_str.replace("'", "").replace(" ", "")


def _render_atom(pred: str, args, is_rule: bool) -> str:
    """Render one atom. In a rule body/head, kb_engine Var objects become Prolog variables;
    everywhere else ground constants become single-quoted atoms."""
    parts = []
    for a in args:
        if kbe.is_var(a):
            parts.append(var_name(a.name))
        else:
            parts.append(quote_const(a))
    return f"{slug_functor(pred)}({','.join(parts)})"


def build_program(kb: kbe.KB, leaf_weights: dict, conclusions: list):
    """Assemble a ProbLog program string + a back-map for the queried conclusions.

    leaf_weights : {(pred, args_tuple) -> w_i in (0,1)} for the admitted facts.
    conclusions  : list of (pred, args) atoms to query (derived multi-hop heads).
    Returns (program_str, query_map) where query_map: canonical_atom_str -> (pred, args_tuple).
    """
    lines: list[str] = []
    # weighted facts
    for (pred, args), _cert in kb.facts.items():
        w = leaf_weights.get((pred, tuple(args)), 0.5)
        w = min(1.0 - EPS, max(EPS, float(w)))
        lines.append(f"{w:.6f}::{_render_atom(pred, args, is_rule=False)}.")
    # deterministic bridge rules (weight 1)
    for rule in kb.rules:
        head = _render_atom(rule["head_pred"], rule["head_args"], is_rule=True)
        body = ", ".join(_render_atom(p, a, is_rule=True) for (p, a) in rule["body"])
        lines.append(f"{head} :- {body}.")
    # queries
    query_map: dict[str, tuple] = {}
    seen = set()
    for (pred, args) in conclusions:
        atomstr = _render_atom(pred, args, is_rule=False)
        if atomstr in seen:
            continue
        seen.add(atomstr)
        lines.append(f"query({atomstr}).")
        query_map[_canon(atomstr)] = (pred, tuple(args))
    return "\n".join(lines), query_map


# ---------------------------------------------------------------------------
# Engine 1: ProbLog
# ---------------------------------------------------------------------------
def run_problog(program: str, query_map: dict) -> dict:
    """Evaluate a ProbLog program; map Term marginals back to (pred,args) -> prob.
    Raises on any ProbLog failure so the caller can fall back."""
    if not _PROBLOG_OK:
        raise RuntimeError("problog not importable")
    res = get_evaluatable().create_from(PrologString(program)).evaluate()
    out = {}
    for term, prob in res.items():
        key = query_map.get(_canon(str(term)))
        if key is not None:
            out[key] = float(prob)
    return out


# ---------------------------------------------------------------------------
# Engine 2: pure-Python EXACT weighted model counting (ProbLog-equivalent)
# ---------------------------------------------------------------------------
def _sub_kb(present_leaves, rules) -> kbe.KB:
    kb = kbe.KB()
    for (pred, args) in present_leaves:
        kb.add_fact(pred, args, {})
    for rule in rules:
        kb.add_rule(rule["name"], rule["head_pred"], rule["head_args"], rule["body"])
    return kb


def all_proofs_by_conclusion(kb: kbe.KB, max_depth: int = 4) -> dict:
    """Collect EVERY ground proof per conclusion (not deduped) — needed for noisy-OR."""
    out: dict[tuple, list] = defaultdict(list)
    for rule in kb.rules:
        for proof in kb.run_rule(rule, max_depth=max_depth):
            key = (proof["atom"][0], tuple(proof["atom"][1]))
            out[key].append(proof)
    return out


def run_wmc(kb: kbe.KB, leaf_weights: dict, conclusions: list,
            enum_cap: int = ENUM_CAP) -> tuple[dict, str]:
    """Exact WMC over the distinct rule-feeding leaves (ProbLog-equivalent for independent
    Bernoulli facts + deterministic monotone rules). Falls back to a flagged noisy-OR
    proof approximation only if that leaf count exceeds enum_cap.
    Returns ({(pred,args_tuple) -> marginal}, engine_tag)."""
    concl_keys = [(c[0], tuple(c[1])) for c in conclusions]
    if not concl_keys:
        return {}, ("fallback_exact_wmc" if not _PROBLOG_OK else "fallback_exact_wmc")
    relevant_preds = {p for rule in kb.rules for (p, _a) in rule["body"]}
    rl = [(pred, tuple(args)) for (pred, args) in kb.facts.keys() if pred in relevant_preds]
    n = len(rl)
    if n <= enum_cap:
        ws = [min(1.0 - EPS, max(EPS, float(leaf_weights.get(rl[i], 0.5)))) for i in range(n)]
        marg = {ck: 0.0 for ck in concl_keys}
        for mask in range(1 << n):
            p = 1.0
            for i in range(n):
                p *= ws[i] if (mask & (1 << i)) else (1.0 - ws[i])
            if p == 0.0:
                continue
            present = [rl[i] for i in range(n) if (mask & (1 << i))]
            sub = _sub_kb(present, kb.rules)
            derived = {(pp["atom"][0], tuple(pp["atom"][1]))
                       for pp in sub.derive_all(max_depth=4)}
            for ck in concl_keys:
                if ck in derived:
                    marg[ck] += p
        return {ck: min(1.0, max(0.0, v)) for ck, v in marg.items()}, "fallback_exact_wmc"
    # noisy-OR proof-level approximation (exact only when proofs share no leaves)
    proofs_by = all_proofs_by_conclusion(kb)
    marg = {}
    for ck in concl_keys:
        prod_not = 1.0
        for proof in proofs_by.get(ck, []):
            pl = 1.0
            for lf in kbe.iter_leaves(proof):
                key = (lf["atom"][0], tuple(lf["atom"][1]))
                pl *= min(1.0 - EPS, max(EPS, float(leaf_weights.get(key, 0.5))))
            prod_not *= (1.0 - pl)
        marg[ck] = min(1.0, max(0.0, 1.0 - prod_not))
    return marg, "fallback_noisy_or_approx"


# ---------------------------------------------------------------------------
# Unified marginal computation (try ProbLog, else WMC) — never raises
# ---------------------------------------------------------------------------
def conclusion_marginals(kb: kbe.KB, leaf_weights: dict, conclusions: list,
                         prefer_problog: bool = True) -> tuple[dict, str]:
    """Return ({(pred,args_tuple) -> marginal}, engine in {'problog','fallback_exact_wmc',
    'fallback_noisy_or_approx'}). On any ProbLog error, fall back to exact WMC."""
    if prefer_problog and _PROBLOG_OK:
        try:
            program, qmap = build_program(kb, leaf_weights, conclusions)
            marg = run_problog(program, qmap)
            # ProbLog can silently omit unreachable queries -> backfill via WMC
            missing = [c for c in conclusions if (c[0], tuple(c[1])) not in marg]
            if missing:
                wm, _ = run_wmc(kb, leaf_weights, missing)
                marg.update(wm)
            return marg, "problog"
        except Exception:  # pragma: no cover - parse/compile failure -> WMC
            pass
    return run_wmc(kb, leaf_weights, conclusions)


# ---------------------------------------------------------------------------
# Probabilistic trace-graph (reuse proof shape; add a 'prob' attribute per node)
# ---------------------------------------------------------------------------
def proof_to_prob_graph(proof: dict, leaf_weights: dict, marginals: dict) -> dict:
    """Flatten a proof into {nodes,edges} like kb_engine.proof_to_graph, but with a 'prob'
    field on every node: leaf prob = its calibrated weight w_i; derived/root prob = the
    (ProbLog/WMC) marginal of that sub-conclusion. Leaf certificates are preserved."""
    nodes, edges = [], []
    counter = [0]

    def atom_str(atom):
        return f"{atom[0]}({', '.join(map(str, atom[1]))})"

    def walk(node) -> int:
        nid = counter[0]
        counter[0] += 1
        key = (node["atom"][0], tuple(node["atom"][1]))
        if node["type"] == "leaf":
            w = leaf_weights.get(key)
            w = float(w) if w is not None else None
            nodes.append({"id": nid, "label": atom_str(node["atom"]), "kind": "leaf",
                          "prob": (round(w, 6) if w is not None else None),
                          "cert": node.get("cert")})
        else:
            m = marginals.get(key)
            nodes.append({"id": nid, "label": atom_str(node["atom"]), "kind": "derived",
                          "rule": node.get("rule"),
                          "prob": (round(float(m), 6) if m is not None else None)})
            for c in node.get("children", []):
                cid = walk(c)
                edges.append({"src": nid, "dst": cid, "rule": node.get("rule")})
        return nid

    walk(proof)
    return {"nodes": nodes, "edges": edges}


def prob_graph_to_dot(graph: dict, title: str = "") -> str:
    """DOT rendering with marginal/weight annotated on every node label."""
    import html
    lines = ["digraph prob_proof {", "  rankdir=TB;",
             '  node [style=filled, fontname="Helvetica", fontsize=10];']
    if title:
        lines.append(f'  labelloc="t"; label="{html.escape(title)}";')
    for n in graph["nodes"]:
        label = html.escape(n["label"])
        pr = n.get("prob")
        pr_s = f"\\np={pr:.3f}" if isinstance(pr, (int, float)) else ""
        if n["kind"] == "derived":
            color = "lightblue"
            extra = f'\\nrule: {html.escape(str(n.get("rule")))}{pr_s}'
            tooltip = "derived conclusion (marginal)"
        else:
            cert = n.get("cert") or {}
            hv = cert.get("hallucination_verdict", "?")
            color = "lightsalmon" if hv == "HALLUCINATED" else "palegreen"
            dc = cert.get("decoy_certificate") or {}
            ec = cert.get("entrapment_certificate") or {}
            extra = (f'{pr_s}\\nW={dc.get("W_i")} T={dc.get("T")} a={dc.get("alpha")}'
                     f'\\nFDP_hat={ec.get("FDP_hat")} r={ec.get("r")}')
            tooltip = html.escape(str(cert.get("provenance", ""))[:200] or "leaf fact")
        lines.append(f'  n{n["id"]} [label="{label}{extra}", fillcolor="{color}", '
                     f'tooltip="{tooltip}"];')
    for e in graph["edges"]:
        lines.append(f'  n{e["src"]} -> n{e["dst"]} [label="{html.escape(str(e.get("rule") or ""))}", '
                     f'fontsize=8];')
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Self-tests (Stage 0 for the probabilistic layer)
# ---------------------------------------------------------------------------
def _toy_two_hop_kb():
    kb = kbe.KB()
    kb.add_fact("cross_references", ("Art13", "Art6"),
                {"provenance": "Art.13 refers to Art.6", "hallucination_verdict": "ENTAILED",
                 "decoy_certificate": {"W_i": 0.9, "T": 0.4, "alpha": 0.2},
                 "entrapment_certificate": {"FDP_hat": 0.05, "r": 1}})
    kb.add_fact("grants_right", ("Art6", "lawful processing"),
                {"provenance": "Art.6 grants the right to lawful processing",
                 "hallucination_verdict": "ENTAILED",
                 "decoy_certificate": {"W_i": 0.7, "T": 0.4, "alpha": 0.2},
                 "entrapment_certificate": {"FDP_hat": 0.05, "r": 1}})
    kb.add_rule("relevant_right", "relevant_right", (V("A"), V("R")),
                [("cross_references", (V("A"), V("B"))), ("grants_right", (V("B"), V("R")))])
    lw = {("cross_references", ("Art13", "Art6")): 0.9,
          ("grants_right", ("Art6", "lawful processing")): 0.7}
    concl = [("relevant_right", ("Art13", "lawful processing"))]
    return kb, lw, concl


def selftest() -> None:
    # (1) calibration + weight maps
    assert abs(calibrate(0.5) - 0.5) < 1e-12
    assert calibrate(0.0) == EPS and calibrate(1.0) == 1.0 - EPS and calibrate(None) == 0.5
    assert abs(weight_gate_consistent(0.8, 0.2) - 0.8 * 0.8) < 1e-9
    assert abs(weight_identity(0.8) - 0.8) < 1e-9
    assert abs(weight_margin(0.0) - 0.5) < 1e-9 and abs(weight_margin(1.0) - (1.0 - EPS)) < 1e-9
    assert weight_gate_consistent(0.8, 0.2) <= weight_identity(0.8) + 1e-12  # shrinkage <= identity

    # (2) toy 2-hop: marginal == 0.9*0.7 == 0.63 (atom sanitisation incl. space in 'lawful processing')
    kb, lw, concl = _toy_two_hop_kb()
    program, qmap = build_program(kb, lw, concl)
    assert "relevant_right(A,R)" in program and "::cross_references('Art13','Art6')." in program
    wm, eng_w = run_wmc(kb, lw, concl)
    assert eng_w == "fallback_exact_wmc"
    assert abs(wm[("relevant_right", ("Art13", "lawful processing"))] - 0.63) < 1e-9, wm
    if _PROBLOG_OK:
        pm = run_problog(program, qmap)
        assert abs(pm[("relevant_right", ("Art13", "lawful processing"))] - 0.63) < 1e-9, pm
        # (3) fallback-equivalence: WMC == ProbLog within 1e-9
        assert abs(pm[("relevant_right", ("Art13", "lawful processing"))]
                   - wm[("relevant_right", ("Art13", "lawful processing"))]) < 1e-9

    # (4) two-proof noisy-OR sanity: two independent bridges -> 1-(1-0.5)*(1-0.4) = 0.7
    kb2 = kbe.KB()
    # proof 1: a -B1- c ; proof 2: a -B2- c  (two distinct intermediaries, shared conclusion)
    kb2.add_fact("cross_references", ("A", "B1"), {})
    kb2.add_fact("grants_right", ("B1", "C"), {})
    kb2.add_fact("cross_references", ("A", "B2"), {})
    kb2.add_fact("grants_right", ("B2", "C"), {})
    kb2.add_rule("relevant_right", "relevant_right", (V("X"), V("R")),
                 [("cross_references", (V("X"), V("Y"))), ("grants_right", (V("Y"), V("R")))])
    # weights chosen so proof1 prob = 0.5 (sqrt-ish) ... use explicit leaf weights:
    lw2 = {("cross_references", ("A", "B1")): 1.0 - EPS, ("grants_right", ("B1", "C")): 0.5,
           ("cross_references", ("A", "B2")): 1.0 - EPS, ("grants_right", ("B2", "C")): 0.4}
    concl2 = [("relevant_right", ("A", "C"))]
    wm2, _ = run_wmc(kb2, lw2, concl2)
    # proof1 ~ (1-eps)*0.5, proof2 ~ (1-eps)*0.4 ; exact WMC over 4 indep leaves
    # noisy-OR (shared leaf? none shared here) -> 1-(1-0.5')*(1-0.4') with 0.5'=(1-eps)*0.5
    exp = 1.0 - (1.0 - (1.0 - EPS) * 0.5) * (1.0 - (1.0 - EPS) * 0.4)
    assert abs(wm2[("relevant_right", ("A", "C"))] - exp) < 1e-6, (wm2, exp)
    if _PROBLOG_OK:
        program2, qmap2 = build_program(kb2, lw2, concl2)
        pm2 = run_problog(program2, qmap2)
        assert abs(pm2[("relevant_right", ("A", "C"))] - wm2[("relevant_right", ("A", "C"))]) < 1e-9

    # (5) prob trace-graph: leaf prob = weight, root prob = marginal, certs preserved
    proofs = kb.derive_all()
    marg, eng = conclusion_marginals(kb, lw, [(p["atom"][0], p["atom"][1]) for p in proofs])
    g = proof_to_prob_graph(proofs[0], lw, marg)
    root = next(n for n in g["nodes"] if n["kind"] == "derived")
    assert abs(root["prob"] - 0.63) < 1e-9
    leaves = [n for n in g["nodes"] if n["kind"] == "leaf"]
    assert len(leaves) == 2 and all(lf["cert"] and lf["prob"] is not None for lf in leaves)
    dot = prob_graph_to_dot(g, "toy")
    assert dot.startswith("digraph prob_proof {") and "p=0.630" in dot

    print(f"prob_reasoner selftest PASSED (problog_available={_PROBLOG_OK}, engine={eng})")


if __name__ == "__main__":
    selftest()
