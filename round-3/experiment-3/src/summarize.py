#!/usr/bin/env python3
"""Pretty-print the headline results from method_out.json for quick human inspection."""
import json
import sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else "method_out.json")
m = json.loads(p.read_text())["metadata"]

print("=" * 78)
print(f"METHOD: {m['method_name']}")
print(f"docs={m['n_docs_used']} model={m['model']} cost=${m['cost_usd']} "
      f"calls={m['n_api_calls']} B={m['bootstrap_B']}")
print(f"elicitation={m['elicitation']} logprobs={m['logprobs_available']} "
      f"contamination={m['contamination_rate_decoys']}")
print(f"max_recall: " + ", ".join(f"{s}={v}" for s, v in m["max_recall_per_system"].items()))
print("=" * 78)

mr = m["matched_recall"]
print("\nMATCHED-RECALL PRECISION WEDGE (METHOD - PLAIN):")
print(f"{'recall':>8} {'precM':>7} {'precP':>7} {'delta':>8} {'ci_lo':>8} {'ci_hi':>8} {'p':>6} {'BH':>3}")
for i, r in enumerate(mr["recall_grid"]):
    pm = mr["precision"]["METHOD"][i]
    pp = mr["precision"]["PLAIN"][i]
    d = mr["delta_method_minus_plain"][i]
    lo, hi = mr["delta_ci"][i]
    pv = mr["delta_bootstrap_p_value"][i]
    bh = "*" if mr["bh_significant"][i] else ""
    def f(x):
        return f"{x:.3f}" if isinstance(x, (int, float)) else " - "
    print(f"{r:>8.3f} {f(pm):>7} {f(pp):>7} {f(d):>8} {f(lo):>8} {f(hi):>8} {f(pv):>6} {bh:>3}")

print("\nKNOCKOFF+ OPERATING POINTS (METHOD's own gate):")
for a, v in m["knockoff_operating_points"].items():
    print(f"  alpha={a}: recall={v['recall']} precision={v['precision']} "
          f"n_admit={v['n_admit']} T={v['T']} k_floor_met={v['k_floor_met']}")

h = m["hallucinated_conclusion_rate"]
print(f"\nMULTI-HOP HALLUCINATION RATE @ recall={h['representative_recall']}:")
for s, v in h["by_system"].items():
    print(f"  {s:>7}: rate={v['point']} ci=[{v['ci_lo']},{v['ci_hi']}] "
          f"(derived={v['n_derived']} hallu={v['n_hallucinated']})")
dd = h["delta_method_minus_plain"]
print(f"  DELTA(METHOD-PLAIN): {dd['point']} ci=[{dd['ci_lo']},{dd['ci_hi']}] (lower=better)")

ac = m["alignment_check"]
print(f"\nALIGNER SELF-ERROR PROBE: relation_acc={ac['aligner_relation_accuracy']} "
      f"entitylink_acc={ac['aligner_entitylink_accuracy']}")
print("ALIGNMENT SENSITIVITY (delta sign must persist):")
for k, v in ac["sensitivity"].items():
    print(f"  {k:>22}: delta={v['delta']} ci={v.get('ci')}")

sc = m.get("scope", {})
print(f"\nSCOPE (honesty): n_docs_used={sc.get('n_docs_used')} / requested={sc.get('n_docs_requested')} "
      f"| recall_ceiling={sc.get('recall_ceiling')} | B={sc.get('bootstrap_B')} grid0={sc.get('grid_start')}")
print(f"participating_systems={m.get('participating_systems')}  dropped={list((m.get('dropped_comparators') or {}).keys())}")

hp = m["hallucinated_conclusion_rate"]
print(f"\nMULTI-HOP POWER: underpowered={hp.get('underpowered')} target={hp.get('power_target')} "
      f"n_derived_by_system={hp.get('n_derived_by_system')} delta_ci_width={hp.get('delta_ci_width')}")

rd = m.get("regime_diagnostic", {})
if rd:
    print("\n=== LABEL-FREE REGIME-DIAGNOSTIC (gold-free; zero API) ===")
    sA = rd["signal_A_winrate_tail"]
    print("  Signal A — tail decoy win-rate (Zt>=Z; ~0.5 exchangeable, <<0.5 too-easy):")
    for a in sA:
        print(f"    {a['label']:>18}: winrate={a['winrate']} ci={a['ci']} (n_tail={a['n_tail']})")
    sB = rd["signal_B_cdf_match"]["full_distribution"]
    print(f"  Signal B — CDF match (full): decoy_mean={sB['decoy_mean']} lowf_real_mean={sB['lowf_real_mean']} "
          f"ks_p={sB['ks_p']} mw_p={sB['mw_p']} perm_p={sB['perm_p']} match={sB['match']}")
    sC = rd["signal_C_wz_divergence"]
    print(f"  Signal C — W-vs-Z: rho_admission={sC['spearman_admission']} jaccard={sC['admitted_set_jaccard']} "
          f"frac(W==Z)={sC['frac_W_equals_Z']}")
    sD = rd["signal_D_calibration"]
    print(f"  Signal D — calibration: auc={sD['calibration_auc']} spearman(Z,f)={sD['calibration_spearman_Z_f']}")
    print(f"  => PREDICTED regime={rd['predicted_regime']} wedge_sign={rd['predicted_wedge_sign']} "
          f"(basis: {rd['prediction_basis']})")
    pvr = rd["prediction_vs_realized"]
    print(f"  => VALIDATION: realized={pvr['realized_wedge_sign']} prediction_correct={pvr['prediction_correct']}")
    print(f"  CROSS-ANCHOR ({rd['cross_anchor']['clutrr_source']}): {rd['cross_anchor']['winrate_sorted']}")

print("\nVERDICT:")
print(f"  wedge_confirmed={m['verdict']['wedge_confirmed']} "
      f"disconfirmed={m['verdict']['disconfirmed']} "
      f"n_confirmed_points={m['verdict']['n_confirmed_points']}")
print(f"  {m['verdict']['message']}")
print(f"  OPERATIONAL: {m['verdict'].get('operational_verdict')}")
