#!/usr/bin/env python3
"""make_figures.py — publication figures from method_out.json.

Generates:
  fig1_decoy_signature.png  — tail decoy win-rate vs alpha (the S1 signature), comparing
                              logprob vs portable elicitation and counterfactual vs random-swap.
  fig2_crux_cdf.png         — overlaid empirical CDFs of true-positive / spontaneous-error /
                              counterfactual-decoy score pools (the spontaneous-error tail match).
  fig3_fdr_calibration.png  — realized FDR vs nominal alpha for the decoy gate vs the raw-
                              confidence baseline (hallucination-control comparison).
  fig4_ablation.png         — Generator!=Scorer de-circularization: tail win-rate per (G,S) config.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)


def load():
    return json.loads((HERE / "method_out.json").read_text())["metadata"]


def pick_views(d, prefer):
    """Return up to two available view names, preferring `prefer` order."""
    avail = list(d)
    out = [v for v in prefer if v in avail]
    if not out:
        out = avail[:2]
    return out


def _rows_xy(rows, key):
    xs, ys, los, his = [], [], [], []
    for r in rows:
        if r.get(key) is None:
            continue
        xs.append(r["alpha"]); ys.append(r[key])
        ci = r.get("win_rate_ci") or [None, None]
        los.append(ci[0] if ci[0] is not None else r[key])
        his.append(ci[1] if ci[1] is not None else r[key])
    return xs, ys, los, his


def fig_decoy_signature(m):
    s1 = m["s1_decoy_signature_by_elicitation"]
    views = pick_views(s1, ("logprob_full", "portable_full", "logprob_pilot", "portable_pilot"))[:2]
    fig, axes = plt.subplots(1, len(views), figsize=(5.2 * len(views), 4.2), sharey=True)
    if len(views) == 1:
        axes = [axes]
    for ax, view in zip(axes, views):
        for fam, color, mk in (("counterfactual", "tab:blue", "o"),
                               ("random_swap", "tab:red", "s")):
            rows = s1[view][fam]["rows"]
            xs, ys, los, his = _rows_xy(rows, "tail_win_rate")
            if not xs:
                continue
            yerr = [[y - lo for y, lo in zip(ys, los)], [hi - y for y, hi in zip(ys, his)]]
            ax.errorbar(xs, ys, yerr=yerr, marker=mk, color=color, capsize=3,
                        label=fam.replace("_", " "), lw=1.8)
        # enrich with the certification-free robustness sweep (tail win-rate at top q%)
        for fam, color in (("counterfactual", "tab:blue"), ("random_swap", "tab:red")):
            sw = s1[view][fam].get("robustness_sweep", [])
            sx = [1.0 - r["quantile"] for r in sw if r.get("tail_win_rate") is not None]
            sy = [r["tail_win_rate"] for r in sw if r.get("tail_win_rate") is not None]
            if sx:
                ax.scatter(sx, sy, facecolors="none", edgecolors=color, s=45, alpha=0.6,
                           zorder=2)
        ax.axhline(0.5, ls="--", color="k", lw=1, alpha=0.7, label="exchangeable (0.5)")
        ax.set_title(view.replace("_", " "))
        ax.set_xlabel(r"nominal FDR $\alpha$ (filled, +CI) / tail depth $1-q$ (hollow)")
        ax.set_xlim(0.0, 0.55)
        ax.set_ylim(0, 0.75)
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("tail decoy win-rate")
    axes[-1].legend(fontsize=8, loc="upper left")
    fig.suptitle("S1 decoy signature: counterfactual ~0.5 (calibrated) vs anti-conservative swap",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_decoy_signature.png", dpi=150)
    plt.close(fig)


def fig_crux_cdf(m):
    crux = m["spontaneous_error_match_by_elicitation"]
    views = pick_views(crux, ("portable_full", "logprob_full", "portable_pilot"))[:2]
    fig, axes = plt.subplots(1, len(views), figsize=(5.2 * len(views), 4.2), sharey=True)
    if len(views) == 1:
        axes = [axes]
    for ax, view in zip(axes, views):
        cdfs = crux[view]["figure_cdfs"]
        x = cdfs["x"]
        ax.plot(x, cdfs["cdf_truepos"], color="tab:green", lw=2, label="true positives")
        ax.plot(x, cdfs["cdf_spont"], color="tab:orange", lw=2, label="spontaneous errors")
        ax.plot(x, cdfs["cdf_decoy"], color="tab:blue", lw=2, ls="--", label="counterfactual decoys")
        ax.set_title(view.replace("_", " "))
        ax.set_xlabel("rank-normalized entailment score")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("empirical CDF")
    axes[-1].legend(fontsize=8, loc="upper left")
    fig.suptitle("Spontaneous-error tail match: decoy CDF tracks genuine errors, not true positives",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(FIG / "fig2_crux_cdf.png", dpi=150)
    plt.close(fig)


def fig_fdr_calibration(m):
    base = m["baseline_vs_method_fdr_by_elicitation"]
    views = pick_views(base, ("portable_full", "logprob_full", "portable_pilot"))[:2]
    fig, axes = plt.subplots(1, len(views), figsize=(5.2 * len(views), 4.2), sharey=True)
    if len(views) == 1:
        axes = [axes]
    for ax, view in zip(axes, views):
        rows = base[view]["rows"]
        al = [r["alpha"] for r in rows]
        mf = [r["method_realized_fdr"] for r in rows]
        bf = [r["baseline_realized_fdr"] for r in rows]
        ax.plot([0, 0.5], [0, 0.5], ls=":", color="k", alpha=0.6, label="perfect calibration")
        ax.plot(al, mf, marker="o", color="tab:blue", lw=1.8, label="decoy-FDR gate (method)")
        ax.plot(al, bf, marker="s", color="tab:red", lw=1.8, label="raw-confidence baseline")
        ax.set_title(view.replace("_", " "))
        ax.set_xlabel(r"nominal FDR $\alpha$")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("realized FDR (crisp gold)")
    axes[-1].legend(fontsize=8, loc="upper left")
    fig.suptitle("Realized vs nominal FDR: gate control vs uncontrolled baseline hallucinations",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(FIG / "fig3_fdr_calibration.png", dpi=150)
    plt.close(fig)


def fig_ablation(m):
    ab = m.get("generator_ne_scorer", {})
    if not ab.get("ran"):
        return
    cfgs = ab["configs"]
    labels = [f"G={c['G']}\nS={c['S']}" for c in cfgs]
    wr = [c["tail_win_rate"] for c in cfgs]
    los = [c["win_rate_ci"][0] for c in cfgs]
    his = [c["win_rate_ci"][1] for c in cfgs]
    colors = ["tab:blue" if c["G"] == c["S"] else "tab:purple" for c in cfgs]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    xs = range(len(cfgs))
    yerr = [[(w - lo) if (w is not None and lo is not None) else 0 for w, lo in zip(wr, los)],
            [(hi - w) if (w is not None and hi is not None) else 0 for w, hi in zip(wr, his)]]
    ax.bar(xs, wr, color=colors, alpha=0.8, yerr=yerr, capsize=4)
    ax.axhline(0.5, ls="--", color="k", lw=1, label="exchangeable (0.5)")
    ax.set_xticks(list(xs)); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("tail decoy win-rate (portable)")
    ax.set_ylim(0, 0.75)
    ax.set_title(f"Generator!=Scorer de-circularization — verdict: {ab.get('verdict')}")
    ax.grid(alpha=0.3, axis="y")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig4_ablation.png", dpi=150)
    plt.close(fig)


def main():
    m = load()
    fig_decoy_signature(m)
    fig_crux_cdf(m)
    fig_fdr_calibration(m)
    fig_ablation(m)
    print("Figures written to", FIG)
    for p in sorted(FIG.glob("*.png")):
        print("  ", p.name, f"{p.stat().st_size//1024} KB")


if __name__ == "__main__":
    sys.exit(main())
