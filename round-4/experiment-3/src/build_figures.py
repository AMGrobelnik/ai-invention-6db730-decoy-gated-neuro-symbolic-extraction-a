#!/usr/bin/env python3
"""
build_figures.py — render F1-F4 PNGs from method_out.json['metadata']['figures'] +
the exported probabilistic trace-graphs. Pure matplotlib (+ networkx for the graph): there
is NO system `dot` binary in this environment, so the graph is laid out with networkx.

F1  pooled atomic hallucination raw vs gate across alpha, both elicitations, CI bars.
F2  multi-hop corruption RAW-KB vs GATE-KB(a=0.5) with CIs + per-genre stacked counts.
F3  decoy_fdr_hat vs realized FDR scatter (conservative regime) + CLUTRR contrast.
F4  a probabilistic trace-graph (regulatory multi-hop) with node marginals + leaf certs.
"""
from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from loguru import logger

HERE = Path(__file__).resolve().parent
FIG_DIR = HERE / "figures"


def _ci_err(points, cis):
    """Convert [point...] + [[lo,hi]...] to asymmetric yerr (2xN), NaN-safe."""
    lo, hi = [], []
    for p, c in zip(points, cis):
        if p is None or c is None or c[0] is None or c[1] is None:
            lo.append(0.0)
            hi.append(0.0)
        else:
            lo.append(max(0.0, p - c[0]))
            hi.append(max(0.0, c[1] - p))
    return np.array([lo, hi])


def _wrap(cap, width=110):
    return "\n".join(textwrap.wrap(cap, width))


def fig_f1(f1: dict, path: Path):
    alphas = f1["alpha_grid"]
    elics = list(f1["by_elic"].keys())
    fig, axes = plt.subplots(1, len(elics), figsize=(6.2 * len(elics), 4.6), sharey=True)
    if len(elics) == 1:
        axes = [axes]
    x = np.arange(len(alphas))
    w = 0.36
    for ax, elic in zip(axes, elics):
        d = f1["by_elic"][elic]
        raw = [v if v is not None else np.nan for v in d["raw"]]
        gate = [v if v is not None else np.nan for v in d["gate"]]
        ax.bar(x - w / 2, raw, w, yerr=_ci_err(d["raw"], d["raw_ci"]), capsize=3,
               color="#d9886a", label="RAW LLM")
        ax.bar(x + w / 2, gate, w, yerr=_ci_err(d["gate"], d["gate_ci"]), capsize=3,
               color="#5b8c5a", label="decoy gate")
        for i, n in enumerate(d.get("n_admitted", [])):
            ax.text(x[i] + w / 2, (gate[i] if gate[i] == gate[i] else 0) + 0.005,
                    f"n={n}", ha="center", va="bottom", fontsize=7)
        ax.set_title(f"elicitation = {elic}")
        ax.set_xticks(x)
        ax.set_xticklabels([f"α={a}\n(k≥{kf})" for a, kf in zip(alphas, f1["k_floor"])], fontsize=8)
        ax.set_xlabel("target FDR level α")
        ax.grid(axis="y", alpha=0.3)
    axes[0].set_ylabel("pooled atomic hallucinated-fact rate")
    axes[0].legend(loc="upper right", fontsize=9)
    fig.suptitle("F1 — Pooled atomic hallucination: RAW LLM vs decoy-competition FDR gate",
                 fontsize=12, y=0.99)
    fig.text(0.5, -0.02, _wrap(f1["caption"]), ha="center", va="top", fontsize=7.5)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def fig_f2(f2: dict, path: Path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8))
    # left: raw vs gate corrupted rate with CIs
    labels = ["RAW-KB", "GATE-KB (α=0.5)"]
    pts = [f2["raw_point"], f2["gate_point"]]
    cis = [f2["raw_ci"], f2["gate_ci"]]
    pts_p = [p if p is not None else np.nan for p in pts]
    ax1.bar([0, 1], pts_p, 0.5, yerr=_ci_err(pts, cis), capsize=4,
            color=["#d9886a", "#5b8c5a"])
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("multi-hop corrupted-conclusion rate")
    dp = f2.get("delta_point")
    dci = f2.get("delta_ci") or [None, None]
    dci_s = ("[%.3f, %.3f]" % (dci[0], dci[1])) if (dci[0] is not None and dci[1] is not None) else "n/a"
    ax1.set_title(f"corruption drop Δ={dp} (95% CI {dci_s})", fontsize=10)
    ax1.grid(axis="y", alpha=0.3)
    # right: per-genre derived/corrupt counts (raw)
    genres = list(f2["per_genre"].keys())
    xg = np.arange(len(genres))
    raw_d = [f2["per_genre"][g]["raw_derived"] for g in genres]
    raw_c = [f2["per_genre"][g]["raw_corrupt"] for g in genres]
    gate_d = [f2["per_genre"][g]["gate_derived"] for g in genres]
    gate_c = [f2["per_genre"][g]["gate_corrupt"] for g in genres]
    bw = 0.2
    ax2.bar(xg - 1.5 * bw, raw_d, bw, color="#d9886a", label="RAW derived")
    ax2.bar(xg - 0.5 * bw, raw_c, bw, color="#a83232", label="RAW corrupt")
    ax2.bar(xg + 0.5 * bw, gate_d, bw, color="#5b8c5a", label="GATE derived")
    ax2.bar(xg + 1.5 * bw, gate_c, bw, color="#2d572c", label="GATE corrupt")
    ax2.set_xticks(xg)
    ax2.set_xticklabels(genres)
    ax2.set_ylabel("# multi-hop conclusions")
    ax2.set_title(f"per-genre counts (sole contributor: {f2.get('single_genre_origin')})", fontsize=10)
    ax2.legend(fontsize=8)
    ax2.grid(axis="y", alpha=0.3)
    fig.suptitle("F2 — Multi-hop corrupted-conclusion rate: RAW-KB vs GATE-KB", fontsize=12)
    fig.text(0.5, -0.04, _wrap(f2["caption"]), ha="center", va="top", fontsize=7.5)
    fig.tight_layout(rect=[0, 0.02, 1, 0.95])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def fig_f3(f3: dict, path: Path):
    fig, ax = plt.subplots(figsize=(6.6, 6.2))
    ax.plot([0, 1], [0, 1], "k--", alpha=0.6, label="y = x (self-calibrated)")
    cmap = {"logprob": "#3b6fb0", "portable": "#b06f3b"}
    seen = set()
    for p in f3["points"]:
        x, y = p["decoy_fdr_hat"], p["realized_fdr"]
        if x is None or y is None:
            continue
        lab = p["elicitation"] if p["elicitation"] not in seen else None
        seen.add(p["elicitation"])
        ax.scatter(x, y, c=cmap.get(p["elicitation"], "gray"), s=42, alpha=0.75,
                   edgecolors="white", linewidths=0.5, label=lab)
    cp = f3["clutrr_point"]
    ax.scatter(cp["decoy_fdr_hat"], cp["realized_fdr"], marker="*", s=320, c="#c0392b",
               edgecolors="black", linewidths=0.7, label=cp["label"] + " (anti-conservative)", zorder=5)
    # region below y=x (decoy_fdr_hat >= realized) = CONSERVATIVE (green);
    # region above y=x (realized > decoy_fdr_hat) = anti-conservative (red)
    ax.fill_between([0, 1], [0, 0], [0, 1], color="#5b8c5a", alpha=0.08)
    ax.fill_between([0, 1], [0, 1], [1, 1], color="#c0392b", alpha=0.08)
    ax.text(0.55, 0.18, "CONSERVATIVE\n(decoy_fdr_hat ≥ realized)", fontsize=9, color="#2d572c")
    ax.text(0.04, 0.86, "anti-conservative\n(realized > decoy_fdr_hat)", fontsize=9, color="#a83232")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.05)
    ax.set_xlabel("gate self-report  decoy_fdr_hat")
    ax.set_ylabel("realized FDR vs gold")
    ax.set_title(f"F3 — Self-report regime: {f3['regime']} "
                 f"(anti-conservative cells = {f3['anti_conservative_cells']})", fontsize=11)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(alpha=0.3)
    fig.text(0.5, -0.02, _wrap(f3["caption"]), ha="center", va="top", fontsize=7.5)
    fig.tight_layout(rect=[0, 0.02, 1, 1])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def fig_f4(f4: dict, path: Path):
    ex = f4.get("example")
    if not ex or not ex.get("json_path"):
        logger.warning("F4: no probabilistic trace example available")
        return
    tj = json.loads((HERE / ex["json_path"]).read_text())
    graph = tj["graphs"][0]

    def wrap_lbl(s, width=22):
        return "\n".join(textwrap.wrap(str(s), width)) or str(s)

    G = nx.DiGraph()
    labels, colors, node_order = {}, [], []
    for n in graph["nodes"]:
        G.add_node(n["id"])
        node_order.append(n["id"])
        pr_s = f"\np={n['prob']:.3f}" if isinstance(n.get("prob"), (int, float)) else ""
        if n["kind"] == "derived":
            colors.append("#aed0e0")
            labels[n["id"]] = f"{wrap_lbl(n['label'])}{pr_s}\n[{n.get('rule')}]"
        else:
            cert = n.get("cert") or {}
            hv = cert.get("hallucination_verdict", "?")
            colors.append("#f0a58c" if hv == "HALLUCINATED" else "#a9d99b")
            dc = cert.get("decoy_certificate") or {}
            wv = dc.get("W_i")
            tv = dc.get("T")
            labels[n["id"]] = (f"{wrap_lbl(n['label'])}{pr_s}\n"
                               f"W={wv} T={(round(tv,3) if isinstance(tv,(int,float)) else tv)} "
                               f"α={dc.get('alpha')}\n{hv}")
    for e in graph["edges"]:
        G.add_edge(e["src"], e["dst"])
    # hierarchical layout: root (no incoming) at top
    try:
        roots = [n for n in G.nodes if G.in_degree(n) == 0]
        depth = {}
        for r in roots:
            for node, d in nx.shortest_path_length(G, r).items():
                depth[node] = max(depth.get(node, 0), d)
        bylevel = {}
        for node, d in depth.items():
            bylevel.setdefault(d, []).append(node)
        pos = {}
        for d, nodes in bylevel.items():
            for i, node in enumerate(sorted(nodes)):
                pos[node] = (i - (len(nodes) - 1) / 2.0, -d)
    except Exception:
        pos = nx.spring_layout(G, seed=7)
    fig, ax = plt.subplots(figsize=(12, 7))
    nx.draw_networkx_edges(G, pos, ax=ax, arrows=True, arrowsize=16,
                           edge_color="#555", min_target_margin=26, min_source_margin=26)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors, node_size=4200,
                           edgecolors="black", linewidths=0.8)
    nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=6.6)
    xs = [p[0] for p in pos.values()] or [0]
    ys = [p[1] for p in pos.values()] or [0]
    ax.set_xlim(min(xs) - 1.4, max(xs) + 1.4)
    ax.set_ylim(min(ys) - 0.7, max(ys) + 0.7)
    mg = ex.get("marginal")
    mg_s = f"{mg:.4f}" if isinstance(mg, (int, float)) else str(mg)
    ax.set_title(f"F4 — Probabilistic trace-graph  [{tj['genre']}, engine={tj['engine']}]  "
                 f"{ex.get('rule')}  marginal={mg_s}", fontsize=10.5)
    ax.axis("off")
    fig.text(0.5, 0.01, _wrap(f4["caption"]), ha="center", va="bottom", fontsize=7.5)
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    src = HERE / (sys.argv[1] if len(sys.argv) > 1 else "method_out.json")
    FIG_DIR.mkdir(exist_ok=True)
    figs = json.loads(src.read_text())["metadata"]["figures"]
    fig_f1(figs["F1"], FIG_DIR / "F1_atomic_hallucination.png")
    fig_f2(figs["F2"], FIG_DIR / "F2_multihop_corruption.png")
    fig_f3(figs["F3"], FIG_DIR / "F3_self_report_regime.png")
    fig_f4(figs["F4"], FIG_DIR / "F4_prob_trace_graph.png")
    rendered = sorted(p.name for p in FIG_DIR.glob("F*.png"))
    logger.info(f"Rendered figures -> {FIG_DIR}: {rendered}")


if __name__ == "__main__":
    main()
