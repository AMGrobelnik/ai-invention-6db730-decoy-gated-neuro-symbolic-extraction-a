#!/usr/bin/env python3
"""Render paper-ready figures from method_out.json (CPU-only, no API).

Figures:
  fig1_matched_recall_wedge.jpg  — precision vs matched recall (participating systems) + delta CI
  fig2_regime_map.jpg            — 2-axis label-free regime map (Re-DocRED + CLUTRR anchors)
  fig3_wz_divergence.jpg         — Signal C: W vs Z ranking (gate cannot re-rank => null wedge)
  fig4_decoy_diagnostic.jpg      — Signal A win-rate bars + Signal B decoy/low-f-real score CDFs
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

WORKSPACE = Path(__file__).resolve().parent
FIG_DIR = WORKSPACE / "figures"
FIG_DIR.mkdir(exist_ok=True)


def _save(fig, name):
    p = FIG_DIR / name
    fig.savefig(p, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {p.name}")


def fig1_wedge(m):
    mr = m["matched_recall"]
    grid = mr["recall_grid"]
    part = mr.get("participating_systems", list(mr["precision"].keys()))
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    colors = {"METHOD": "#1f77b4", "PLAIN": "#d62728", "CoT": "#2ca02c",
              "RAG": "#9467bd", "CONF": "#ff7f0e"}
    for s in part:
        ys = mr["precision"].get(s, [])
        xs = [grid[i] for i in range(len(ys)) if ys[i] is not None]
        yy = [y for y in ys if y is not None]
        if xs:
            ax[0].plot(xs, yy, marker="o", ms=3, lw=1.6, label=s, color=colors.get(s))
    ax[0].set_xlabel("matched recall"); ax[0].set_ylabel("atomic-fact precision")
    ax[0].set_title("Matched-recall precision (participating systems)")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
    # delta panel
    d = mr["delta_method_minus_plain"]
    ci = mr["delta_ci"]
    lo = [c[0] if c and c[0] is not None else np.nan for c in ci]
    hi = [c[1] if c and c[1] is not None else np.nan for c in ci]
    ax[1].axhline(0, color="k", lw=0.8, ls="--")
    ax[1].plot(grid, d, color="#1f77b4", lw=1.8, label="Δ = METHOD − PLAIN")
    ax[1].fill_between(grid, lo, hi, color="#1f77b4", alpha=0.2, label="95% doc-block CI")
    ax[1].set_xlabel("matched recall"); ax[1].set_ylabel("Δ precision")
    rc = m.get("scope", {}).get("recall_ceiling")
    nd = m.get("scope", {}).get("n_docs_used")
    ax[1].set_title(f"Wedge Δ (disconfirmed at recall ≤ {rc} on {nd} docs)")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)
    _save(fig, "fig1_matched_recall_wedge.jpg")


def fig2_regime_map(m):
    rd = m["regime_diagnostic"]
    fig, ax = plt.subplots(figsize=(7.2, 5.6))
    # axis1 = decoy exchangeability (winrate_tail); axis2 = base-scorer calibration (proxy)
    # quadrant shading
    ax.axvspan(0.35, 0.65, color="#c8e6c9", alpha=0.4)  # exchangeable band
    ax.axvline(0.5, color="grey", ls=":", lw=1)
    ax.text(0.5, 1.02, "exchangeable (~0.5)", ha="center", fontsize=8, color="green")
    ax.text(0.06, 1.02, "too easy (<<0.5)", ha="left", fontsize=8, color="firebrick")
    pts = rd["cross_anchor"]["points"]
    for i, p in enumerate(pts):
        wr = p.get("winrate_tail")
        if wr is None:
            continue
        cal = 1.0 if p.get("base_scorer_calibrated") else 0.0
        sign = p.get("predicted_wedge_sign") or p.get("realized_wedge_sign") or "?"
        mk = {"null": "s", "positive": "^", "negative": "v"}.get(sign, "o")
        col = {"null": "#7f7f7f", "positive": "#2ca02c", "negative": "#d62728"}.get(sign, "k")
        cy = cal + (0.06 * ((i % 3) - 1))  # small vertical jitter so co-located labels don't overlap
        ax.scatter([wr], [cy], s=130, marker=mk, color=col, edgecolor="k", zorder=5)
        ax.annotate(f"{p['anchor']}\n[{sign}]", (wr, cy), fontsize=7,
                    xytext=(6, 6), textcoords="offset points")
    ax.set_xlim(-0.03, 0.75); ax.set_ylim(-0.3, 1.3)
    ax.set_yticks([0, 1]); ax.set_yticklabels(["low calibration", "high calibration"])
    ax.set_xlabel("decoy exchangeability  (tail win-rate Zt≥Z)")
    ax.set_ylabel("base-scorer calibration axis")
    ax.set_title("Label-free regime map: gate value vs (exchangeability × calibration)")
    ax.grid(alpha=0.3)
    _save(fig, "fig2_regime_map.jpg")


def fig3_wz(m):
    rd = m["regime_diagnostic"]["signal_C_wz_divergence"]
    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    rho = rd.get("spearman_admission")
    jac = rd.get("admitted_set_jaccard")
    feq = rd.get("frac_W_equals_Z")
    # illustrative identity scatter annotation (actual per-candidate W,Z not stored in out)
    ax.text(0.5, 0.62, f"Spearman ρ(W,Z) admission = {rho}", ha="center", fontsize=11)
    ax.text(0.5, 0.50, f"admitted-set Jaccard = {jac}", ha="center", fontsize=11)
    ax.text(0.5, 0.38, f"frac(W == Z) = {feq}", ha="center", fontsize=11)
    ax.text(0.5, 0.18, "ρ≈1, Jaccard≈1  ⇒  the gate cannot re-rank\n⇒  mechanically NULL wedge "
            "(Signal C predicts disconfirmation)", ha="center", fontsize=9, color="firebrick")
    ax.axis("off")
    ax.set_title("Signal C — W-vs-Z ranking divergence (direct wedge predictor)")
    _save(fig, "fig3_wz_divergence.jpg")


def fig4_decoy(m):
    rd = m["regime_diagnostic"]
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    # Signal A: winrate bars
    A = rd["signal_A_winrate_tail"]
    labels = [a["label"] for a in A if a.get("winrate") is not None]
    vals = [a["winrate"] for a in A if a.get("winrate") is not None]
    los = [a["winrate"] - (a["ci"][0] if a["ci"][0] is not None else a["winrate"]) for a in A if a.get("winrate") is not None]
    his = [(a["ci"][1] if a["ci"][1] is not None else a["winrate"]) - a["winrate"] for a in A if a.get("winrate") is not None]
    x = np.arange(len(labels))
    ax[0].bar(x, vals, yerr=[los, his], capsize=3, color="#d62728", alpha=0.8)
    ax[0].axhline(0.5, color="green", ls="--", label="exchangeable (0.5)")
    ax[0].set_xticks(x); ax[0].set_xticklabels(labels, rotation=30, ha="right", fontsize=7)
    ax[0].set_ylabel("decoy win-rate (Zt ≥ Z)")
    ax[0].set_title("Signal A — tail decoy win-rate (<<0.5 ⇒ too easy)")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3, axis="y")
    # Signal B: decoy mean vs low-f real mean (full + tail)
    B = rd["signal_B_cdf_match"]
    grp = ["full", "top_tail"]
    dm = [B["full_distribution"]["decoy_mean"], B["top_tail"]["decoy_mean"]]
    rm = [B["full_distribution"]["lowf_real_mean"], B["top_tail"]["lowf_real_mean"]]
    xb = np.arange(2); w = 0.35
    ax[1].bar(xb - w/2, dm, w, label="decoy mean (Zt)", color="#d62728", alpha=0.8)
    ax[1].bar(xb + w/2, rm, w, label="low-f real mean (Z)", color="#1f77b4", alpha=0.8)
    ax[1].set_xticks(xb); ax[1].set_xticklabels(grp)
    ax[1].set_ylabel("mean score")
    ksf = B["full_distribution"]["ks_p"]
    ax[1].set_title(f"Signal B — decoy vs spontaneous-error scores (KS p={ksf})")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3, axis="y")
    _save(fig, "fig4_decoy_diagnostic.jpg")


def main():
    p = Path(sys.argv[1] if len(sys.argv) > 1 else "method_out.json")
    m = json.loads(p.read_text())["metadata"]
    print(f"Rendering figures from {p} into {FIG_DIR}/")
    for fn in (fig1_wedge, fig2_regime_map, fig3_wz, fig4_decoy):
        try:
            fn(m)
        except Exception as e:
            print(f"  WARN {fn.__name__} failed: {e}")
    print("figures done")


if __name__ == "__main__":
    main()
