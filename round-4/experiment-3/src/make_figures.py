#!/usr/bin/env python3
"""make_figures.py — publication figures from method_out.json.

  fig1_hallucination_grid.png  — gate-vs-raw hallucinated-fact rate across alpha,
                                  per genre x elicitation, with bootstrap CIs (PRIMARY).
  fig2_fdr_selfreport.png       — realized FDR vs the gate's own decoy_fdr_hat vs alpha.
  fig3_matched_recall.png       — precision & hallucination-rate vs matched recall,
                                  RAW / GATE / RAG / CoT.
  fig4_tracegraph_<genre>.png   — rendered proof / admission trace-graph per genre.
  fig5_multihop_corruption.png  — corrupted multi-hop conclusion rate vs alpha (RAW vs GATE).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)
GENRES = ["legal", "news", "regulatory", "pooled"]


def load():
    return json.loads((HERE / "method_out.json").read_text())["metadata"]


def _cells(grid, genre, elic):
    rows = [c for c in grid if c["genre"] == genre and c["elicitation"] == elic]
    return sorted(rows, key=lambda c: c["alpha"])


def fig_hallucination_grid(m):
    grid = m["hallucination_grid"]
    elics = sorted({c["elicitation"] for c in grid})
    fig, axes = plt.subplots(len(elics), len(GENRES),
                             figsize=(3.5 * len(GENRES), 3.4 * len(elics)), squeeze=False)
    for r, elic in enumerate(elics):
        for cc, genre in enumerate(GENRES):
            ax = axes[r][cc]
            rows = _cells(grid, genre, elic)
            al = [c["alpha"] for c in rows]
            gate = [c["gate_hall_rate"] for c in rows]
            glo = [(c["gate_hall_ci"][0] if c["gate_hall_rate"] is not None else None) for c in rows]
            ghi = [(c["gate_hall_ci"][1] if c["gate_hall_rate"] is not None else None) for c in rows]
            raw = [c["raw_hall_rate"] for c in rows]
            xs = [a for a, g in zip(al, gate) if g is not None]
            ys = [g for g in gate if g is not None]
            lo = [l for l, g in zip(glo, gate) if g is not None]
            hi = [h for h, g in zip(ghi, gate) if g is not None]
            if xs:
                yerr = [[y - (l if l is not None else y) for y, l in zip(ys, lo)],
                        [(h if h is not None else y) - y for y, h in zip(ys, hi)]]
                ax.errorbar(xs, ys, yerr=yerr, marker="o", color="tab:blue", capsize=3,
                            lw=1.8, label="decoy-gate")
            rr = [v for v in raw if v is not None]
            if rr:
                ax.axhline(rr[0], ls="--", color="tab:red", lw=1.6, label="raw LLM")
                rci = next((c["raw_hall_ci"] for c in rows if c["raw_hall_rate"] is not None), None)
                if rci and rci[0] is not None:
                    ax.axhspan(rci[0], rci[1], color="tab:red", alpha=0.10)
            if r == 0:
                ax.set_title(genre, fontsize=11)
            if cc == 0:
                ax.set_ylabel(f"{elic}\nhallucinated-fact rate", fontsize=9)
            ax.set_xlabel(r"$\alpha$")
            ax.set_ylim(0, 1.0)
            ax.grid(alpha=0.3)
            if r == 0 and cc == len(GENRES) - 1:
                ax.legend(fontsize=8, loc="upper right")
    fig.suptitle("Hallucinated-fact rate: decoy-gate vs raw LLM (per genre x elicitation x α)",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_hallucination_grid.png", dpi=150)
    plt.close(fig)


def fig_fdr_selfreport(m):
    grid = m["hallucination_grid"]
    elics = sorted({c["elicitation"] for c in grid})
    fig, axes = plt.subplots(1, len(elics), figsize=(5.2 * len(elics), 4.2), squeeze=False)
    for i, elic in enumerate(elics):
        ax = axes[0][i]
        rows = _cells(grid, "pooled", elic)
        al = [c["alpha"] for c in rows]
        dfh = [c["decoy_fdr_hat"] for c in rows]
        rf = [c["realized_fdr"] for c in rows]
        ax.plot([0, 0.5], [0, 0.5], ls=":", color="k", alpha=0.6, label="nominal α")
        ax.plot(al, dfh, marker="o", color="tab:blue", lw=1.8, label="decoy_fdr_hat (self-report)")
        ax.plot(al, rf, marker="s", color="tab:green", lw=1.8, label="realized FDR (gold)")
        anti = [c["alpha"] for c in rows if c["self_report_anticonservative"]]
        for a in anti:
            ax.axvline(a, color="tab:red", ls="-", alpha=0.25)
        ax.set_title(f"pooled — {elic}")
        ax.set_xlabel(r"nominal $\alpha$")
        ax.set_ylabel("FDR")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig.suptitle("Gate self-report (decoy_fdr_hat) vs realized FDR; red = self-report anti-conservative",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(FIG / "fig2_fdr_selfreport.png", dpi=150)
    plt.close(fig)


def fig_matched_recall(m):
    mr = m.get("matched_recall_curves", {})
    systems = [s for s in ("raw", "gate", "rag", "cot") if s in mr]
    if not systems:
        return
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    colors = {"raw": "tab:red", "gate": "tab:blue", "rag": "tab:orange", "cot": "tab:green"}
    for s in systems:
        pts = [p for p in mr[s]["points"] if p.get("reached")]
        if not pts:
            continue
        rec = [p["recall_target"] for p in pts]
        prec = [p["precision"] for p in pts]
        hall = [p["halluc_rate"] for p in pts]
        axes[0].plot(rec, prec, marker="o", color=colors[s], label=f"{s} (max R={mr[s]['max_recall']})")
        axes[1].plot(rec, hall, marker="o", color=colors[s], label=s)
    axes[0].set_xlabel("matched recall"); axes[0].set_ylabel("precision"); axes[0].grid(alpha=0.3)
    axes[0].legend(fontsize=8); axes[0].set_title("Precision @ matched recall")
    axes[1].set_xlabel("matched recall"); axes[1].set_ylabel("hallucinated-fact rate")
    axes[1].grid(alpha=0.3); axes[1].legend(fontsize=8); axes[1].set_title("Hallucination @ matched recall")
    fig.suptitle("Matched-recall comparison: RAW / GATE / RAG / CoT", fontsize=12)
    fig.tight_layout()
    fig.savefig(FIG / "fig3_matched_recall.png", dpi=150)
    plt.close(fig)


def fig_multihop(m):
    mh = m.get("multihop_corruption", {})
    pooled = mh.get("pooled", {})
    if not pooled:
        return
    alphas = []
    gate = []
    for k, v in pooled.items():
        if k.startswith("gate_a"):
            alphas.append(float(k.replace("gate_a", "")))
            gate.append(v.get("corrupted_rate"))
    order = sorted(range(len(alphas)), key=lambda i: alphas[i])
    alphas = [alphas[i] for i in order]
    gate = [gate[i] for i in order]
    raw_rate = pooled.get("raw", {}).get("corrupted_rate")
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    xs = [a for a, g in zip(alphas, gate) if g is not None]
    ys = [g for g in gate if g is not None]
    if xs:
        ax.plot(xs, ys, marker="o", color="tab:blue", lw=1.8, label="GATE-KB")
    if raw_rate is not None:
        ax.axhline(raw_rate, ls="--", color="tab:red", lw=1.6, label="RAW-KB")
    ax.set_xlabel(r"nominal $\alpha$")
    ax.set_ylabel("corrupted multi-hop conclusion rate")
    ax.set_ylim(0, 1.05)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_title("Multi-hop corruption: a conclusion is corrupt if any leaf is hallucinated")
    fig.tight_layout()
    fig.savefig(FIG / "fig5_multihop_corruption.png", dpi=150)
    plt.close(fig)


def _render_graph(graph, title, path):
    G = nx.DiGraph()
    labels, colors = {}, []
    for n in graph["nodes"]:
        G.add_node(n["id"])
        lab = n["label"]
        if n["kind"] == "leaf":
            cert = n.get("cert") or {}
            hv = cert.get("hallucination_verdict", "?")
            dc = cert.get("decoy_certificate") or {}
            lab += f"\nW={dc.get('W_i')} T={dc.get('T')}"
            color = "lightsalmon" if hv == "HALLUCINATED" else "palegreen"
        else:
            color = "lightblue"
        labels[n["id"]] = lab
        colors.append(color)
    for e in graph["edges"]:
        G.add_edge(e["src"], e["dst"], label=e.get("rule") or "")
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    except Exception:
        # no graphviz binary -> layered layout by BFS depth
        roots = [n for n in G.nodes if G.in_degree(n) == 0]
        depth = {}
        for r in roots:
            for node, d in nx.single_source_shortest_path_length(G, r).items():
                depth[node] = max(depth.get(node, 0), d)
        bylvl = {}
        for node, d in depth.items():
            bylvl.setdefault(d, []).append(node)
        pos = {}
        for d, nodes in bylvl.items():
            for i, node in enumerate(sorted(nodes)):
                pos[node] = (i - (len(nodes) - 1) / 2.0, -d)
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    nx.draw(G, pos, ax=ax, node_color=colors, node_size=2600, with_labels=False,
            edgecolors="black", arrows=True, arrowsize=14)
    nx.draw_networkx_labels(G, pos, labels, font_size=7, ax=ax)
    elabels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, elabels, font_size=7, ax=ax)
    ax.set_title(title, fontsize=10)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def fig_tracegraphs(m):
    seen = set()
    for ex in m.get("trace_graphs", {}).get("examples", []):
        genre = ex["genre"]
        if genre in seen:
            continue
        seen.add(genre)
        title = f"{ex['doc_id']} [{genre}] — {ex.get('kind', 'trace')}: {ex.get('rule')}"
        _render_graph(ex["graph"], title, FIG / f"fig4_tracegraph_{genre}.png")


def main():
    m = load()
    fig_hallucination_grid(m)
    fig_fdr_selfreport(m)
    fig_matched_recall(m)
    fig_multihop(m)
    fig_tracegraphs(m)
    print("Figures written to", FIG)
    for p in sorted(FIG.glob("*.png")):
        print("  ", p.name, f"{p.stat().st_size // 1024} KB")


if __name__ == "__main__":
    sys.exit(main())
