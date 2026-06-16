#!/usr/bin/env python3
"""
kb_engine.py — pure-Python backward-chaining meta-interpreter over admitted facts +
hand-authored genre bridge rules, with auditable trace-graph export (JSON + Graphviz DOT).

This is the DEFAULT reasoning engine (the plan's deliverable): it satisfies the goal's
"running logic interpreter + human-auditable trace-graphs" requirement without a system
SWI-Prolog. It mirrors the classic vanilla meta-interpreter

    solve(true, true).
    solve((A,B), (PA,PB)) :- solve(A,PA), solve(B,PB).
    solve(A, node(A, Rule, Proof)) :- (A :- Body), solve(Body, Proof).
    solve(A, leaf(A, Cert)) :- admitted_fact(A, Cert).

Each leaf resolves against the admitted-fact table and carries a certificate
    cert = {provenance_char_span, decoy_certificate:{W_i,T,alpha}, entrapment_certificate:{FDP_hat,r}}
so every derived conclusion is traceable to gated, provenance-bearing base facts.

A Fact is a ground atom: (pred, (arg1, arg2, ...)).
A Rule is (head_pred, head_args, body) where head_args/body atoms use string VARIABLES
(identifiers starting with an uppercase letter) and constants (anything else).
Rules here are non-recursive and range-restricted, so SLD resolution terminates.
"""
from __future__ import annotations

import html
import itertools
from pathlib import Path

# ---------------------------------------------------------------------------
# Term helpers — explicit logic variables (entity constants are arbitrary strings,
# so a capitalization convention cannot distinguish vars from constants).
# ---------------------------------------------------------------------------
class Var:
    __slots__ = ("name",)

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Var) and other.name == self.name

    def __hash__(self):
        return hash(("Var", self.name))

    def __repr__(self):
        return f"?{self.name}"


def V(name: str) -> Var:
    return Var(name)


def is_var(x) -> bool:
    return isinstance(x, Var)


def unify(pat, val, subst: dict) -> dict | None:
    """Unify a (possibly variable-bearing) arg tuple `pat` with ground tuple `val`."""
    s = dict(subst)
    for p, v in zip(pat, val):
        if is_var(p):
            if p in s:
                if s[p] != v:
                    return None
            else:
                s[p] = v
        elif p != v:
            return None
    return s


def subst_args(args, subst: dict) -> tuple:
    return tuple(subst.get(a, a) if is_var(a) else a for a in args)


class KB:
    """Admitted facts + bridge rules + a backward-chaining solver with proof capture."""

    def __init__(self) -> None:
        # (pred, args_tuple) -> certificate dict
        self.facts: dict[tuple, dict] = {}
        self.by_pred: dict[str, list[tuple]] = {}
        self.rules: list[dict] = []

    def add_fact(self, pred: str, args: tuple, cert: dict) -> None:
        key = (pred, tuple(args))
        if key not in self.facts:
            self.facts[key] = cert
            self.by_pred.setdefault(pred, []).append(tuple(args))

    def add_rule(self, name: str, head_pred: str, head_args: tuple, body: list) -> None:
        """body: list of (pred, args) atoms; vars are shared across head+body."""
        self.rules.append({"name": name, "head_pred": head_pred,
                           "head_args": tuple(head_args), "body": list(body)})

    # -- backward chaining ---------------------------------------------------
    @staticmethod
    def _rename(atom_args, tag: str):
        """Rename variables in an arg tuple with a unique tag to avoid clashes."""
        return tuple(Var(f"{a.name}_{tag}") if is_var(a) else a for a in atom_args)

    def _solve_atom(self, pred: str, args: tuple, subst: dict, depth: int):
        """Yield (new_subst, proof_node) for goal pred(args) under subst.

        Goal args are first grounded through subst; remaining unbound vars are matched
        against facts (binding them) or expanded via rules with fresh-renamed variables.
        """
        g_args = subst_args(args, subst)
        # 1) base facts
        for fact_args in self.by_pred.get(pred, []):
            s2 = unify(g_args, fact_args, subst)
            if s2 is not None:
                cert = self.facts[(pred, fact_args)]
                yield s2, {"type": "leaf", "atom": [pred, list(fact_args)], "cert": cert}
        # 2) rule expansion (non-recursive bridges; depth cap is a safety net)
        if depth <= 0:
            return
        for ri, rule in enumerate(self.rules):
            if rule["head_pred"] != pred:
                continue
            tag = f"{depth}_{ri}"
            head = self._rename(rule["head_args"], tag)
            s_head = unify(head, g_args, subst)  # bind renamed head vars to the (ground) goal
            if s_head is None:
                continue
            body = [(p, self._rename(a, tag)) for (p, a) in rule["body"]]
            for sb, child_proofs in self._solve_body(body, s_head, depth - 1):
                head_ground = subst_args(head, sb)
                if any(is_var(a) for a in head_ground):
                    continue
                yield sb, {"type": "derived", "atom": [pred, list(head_ground)],
                           "rule": rule["name"], "children": child_proofs}

    def _solve_body(self, body: list, subst: dict, depth: int):
        if not body:
            yield subst, []
            return
        first, rest = body[0], body[1:]
        for s2, proof in self._solve_atom(first[0], first[1], subst, depth):
            for s3, proofs in self._solve_body(rest, s2, depth):
                yield s3, [proof] + proofs

    def run_rule(self, rule: dict, max_depth: int = 4):
        """Solve a rule's body over the KB and yield fully-ground derived proofs."""
        body = list(rule["body"])
        for sb, child_proofs in self._solve_body(body, {}, max_depth):
            head_ground = subst_args(rule["head_args"], sb)
            if any(is_var(a) for a in head_ground):
                continue
            yield {"type": "derived", "atom": [rule["head_pred"], list(head_ground)],
                   "rule": rule["name"], "children": child_proofs}

    def derive_all(self, max_depth: int = 4) -> list[dict]:
        """Run every rule and collect distinct derived conclusions with one proof each."""
        seen, out = set(), []
        for rule in self.rules:
            for proof in self.run_rule(rule, max_depth):
                key = (proof["atom"][0], tuple(proof["atom"][1]))
                if key in seen:
                    continue
                seen.add(key)
                out.append(proof)
        return out


# ---------------------------------------------------------------------------
# Proof-graph flattening + leaf walk
# ---------------------------------------------------------------------------
def iter_leaves(proof: dict):
    if proof["type"] == "leaf":
        yield proof
    else:
        for c in proof.get("children", []):
            yield from iter_leaves(c)


def proof_to_graph(proof: dict) -> dict:
    """Flatten a proof tree into {nodes:[{id,label,kind,cert?}], edges:[{src,dst,rule}]}."""
    nodes, edges = [], []
    counter = itertools.count()

    def atom_str(atom):
        pred, args = atom[0], atom[1]
        return f"{pred}({', '.join(map(str, args))})"

    def walk(node) -> int:
        nid = next(counter)
        if node["type"] == "leaf":
            nodes.append({"id": nid, "label": atom_str(node["atom"]),
                          "kind": "leaf", "cert": node.get("cert")})
        else:
            nodes.append({"id": nid, "label": atom_str(node["atom"]),
                          "kind": "derived", "rule": node.get("rule")})
            for c in node.get("children", []):
                cid = walk(c)
                edges.append({"src": nid, "dst": cid, "rule": node.get("rule")})
        return nid

    walk(proof)
    return {"nodes": nodes, "edges": edges}


def graph_to_dot(graph: dict, title: str = "") -> str:
    """Render a flattened proof graph to Graphviz DOT.

    Node colour encodes gate status: derived=lightblue, admitted-entailed leaf=palegreen,
    hallucinated leaf=lightsalmon. Leaf tooltip carries provenance + W_i + FDP_hat.
    """
    lines = ["digraph proof {", '  rankdir=TB;', '  node [style=filled, fontname="Helvetica", fontsize=10];']
    if title:
        lines.append(f'  labelloc="t"; label="{html.escape(title)}";')
    for n in graph["nodes"]:
        label = html.escape(n["label"])
        if n["kind"] == "derived":
            color, extra = "lightblue", f'\\nrule: {html.escape(str(n.get("rule")))}'
            tooltip = "derived conclusion"
        else:
            cert = n.get("cert") or {}
            hv = cert.get("hallucination_verdict", "?")
            color = "lightsalmon" if hv == "HALLUCINATED" else "palegreen"
            dc = cert.get("decoy_certificate") or {}
            ec = cert.get("entrapment_certificate") or {}
            extra = (f'\\nW={dc.get("W_i")} T={dc.get("T")} a={dc.get("alpha")}'
                     f'\\nFDP_hat={ec.get("FDP_hat")} r={ec.get("r")}')
            tooltip = html.escape(str(cert.get("provenance", ""))[:200] or "leaf fact")
        lines.append(f'  n{n["id"]} [label="{label}{extra}", fillcolor="{color}", '
                     f'tooltip="{tooltip}"];')
    for e in graph["edges"]:
        lines.append(f'  n{e["src"]} -> n{e["dst"]} [label="{html.escape(str(e.get("rule") or ""))}", '
                     f'fontsize=8];')
    lines.append("}")
    return "\n".join(lines)


def selftest() -> None:
    kb = KB()
    # toy 2-hop derivation: cross_references(a,b), grants_right(b,r) => relevant_right(a,r)
    kb.add_fact("cross_references", ("Art13", "Art6"),
                {"provenance": "Art.13 refers to Art.6", "hallucination_verdict": "ENTAILED",
                 "decoy_certificate": {"W_i": 0.9, "T": 0.4, "alpha": 0.2},
                 "entrapment_certificate": {"FDP_hat": 0.05, "r": 1}})
    kb.add_fact("grants_right", ("Art6", "lawful_processing"),
                {"provenance": "Art.6 grants the right to lawful processing",
                 "hallucination_verdict": "ENTAILED",
                 "decoy_certificate": {"W_i": 0.7, "T": 0.4, "alpha": 0.2},
                 "entrapment_certificate": {"FDP_hat": 0.05, "r": 1}})
    kb.add_rule("relevant_right", "relevant_right", (V("A"), V("R")),
                [("cross_references", (V("A"), V("B"))), ("grants_right", (V("B"), V("R")))])
    derived = kb.derive_all()
    assert len(derived) == 1, f"expected 1 derived, got {len(derived)}"
    d = derived[0]
    assert d["atom"][0] == "relevant_right" and d["atom"][1] == ["Art13", "lawful_processing"], d["atom"]
    leaves = list(iter_leaves(d))
    assert len(leaves) == 2 and all("cert" in lf and lf["cert"].get("decoy_certificate")
                                    and lf["cert"].get("entrapment_certificate")
                                    and "provenance" in lf["cert"] for lf in leaves), \
        "every leaf must carry all three certificate fields"
    g = proof_to_graph(d)
    dot = graph_to_dot(g, title="toy")
    assert dot.startswith("digraph proof {") and "relevant_right" in dot
    assert "->" in dot and "fillcolor" in dot
    print("kb_engine selftest PASSED")


if __name__ == "__main__":
    selftest()
