"""
summarize.py -- human-readable summary + sanity checks of method_out.json, and emit
figures_data.json (clean arrays for the calibration-diagonal figure).
Run: uv run summarize.py
"""
import json
import math
from pathlib import Path

WS = Path(__file__).resolve().parent


def fmt(x, nd=3):
    return "  NA " if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


def main():
    d = json.load(open(WS / "method_out.json"))
    m = d["metadata"]
    meta = m["meta"]
    print("=" * 78)
    print("CLUTRR LABEL-FREE KNOCKOFF+ FDR CALIBRATION DIAGONAL -- RESULTS SUMMARY")
    print("=" * 78)
    print(f"model={meta['model']} scale={meta['scale']} seed={meta['seed']}")
    print(f"docs: pilot={meta['n_docs_pilot']} confirmatory={meta['n_docs_confirmatory']}")
    print(f"selected_elicitation={meta['selected_elicitation']} "
          f"logprobs={meta['probes']['logprobs_available']} cache_tok={meta['probes']['cache_hit_tokens']}")
    print(f"cost=${meta['cumulative_cost_usd']} calls={meta['n_llm_calls']} "
          f"cache_hits={meta['n_cache_hits']} wall={meta['wall_time_sec']}s")
    print(f"alpha*={m['alpha_star']}  CALIBRATION VERDICT = {m['calibration_verdict']}")

    print("\n--- Pilot: elicitation tail-AUC (selection metric) ---")
    for e, v in m["pilot"]["elicitation_tail_auc"].items():
        print(f"  {e:18s} tail_auc={fmt(v['tail_auc'])} CI={v['tail_auc_ci']} "
              f"full_auc={fmt(v['full_auc'])} (nT={v['n_true']},nF={v['n_false']})")
    print(f"  contamination_rate={m['pilot']['contamination_rate']} "
          f"discard_rate={m['pilot']['discard_rate']}")
    cb = m["pilot"]["control_behavior"]
    print(f"  control: cf_tail_win_rate={fmt(cb['counterfactual_tail_win_rate'])} "
          f"swap_tail_win_rate={fmt(cb['swap_tail_win_rate'])} "
          f"KS_p={cb['ks_pvalue_cf_vs_realfalse']} MW_p={cb['mannwhitney_pvalue']}")

    print("\n--- Power analysis (projected to confirmatory) ---")
    print(f"  {'alpha':>6} {'kfloor':>6} {'pilot_adm':>9} {'proj_adm':>8} {'proj_false':>10} "
          f"{'clears':>6} {'ci_halfwidth':>12}")
    for r in m["power_analysis"]:
        print(f"  {r['alpha']:>6} {r['k_floor']:>6} {r['pilot_admissions']:>9} "
              f"{r['projected_admissions']:>8} {r['projected_false']:>10} "
              f"{str(r['clears_floor']):>6} {fmt(r['ci_half_width']):>12}")

    figures = {}
    for fam in ("bridge", "atomic", "pooled"):
        diag = m["diagonal"][fam]
        print(f"\n--- Diagonal: {fam.upper()} family  "
              f"(n_total={diag['n_total']} n_true={diag['n_true']} n_false={diag['n_false_total']} "
              f"n_pos={diag['n_pos']}) ---")
        print(f"  {'alpha':>6} {'realized':>9} {'ci_lo':>7} {'ci_hi':>7} {'decoy_hat':>9} "
              f"{'n_adm':>6} {'n_false':>7} {'cert':>5} | {'swap':>6} {'plain':>6} {'plain_est':>9}")
        xs, ys, los, his, decoy, swap, plain = [], [], [], [], [], [], []
        for r in diag["rows"]:
            print(f"  {r['target_alpha']:>6} {fmt(r['realized_fdr']):>9} {fmt(r['ci_low']):>7} "
                  f"{fmt(r['ci_high']):>7} {fmt(r['decoy_fdr_hat']):>9} {r['n_admitted']:>6} "
                  f"{r['n_false']:>7} {str(r['certified']):>5} | {fmt(r['swap_realized_fdr']):>6} "
                  f"{fmt(r['plain_realized_fdr']):>6} {fmt(r['plain_est_fdr']):>9}")
            xs.append(r["target_alpha"]); ys.append(r["realized_fdr"])
            los.append(r["ci_low"]); his.append(r["ci_high"]); decoy.append(r["decoy_fdr_hat"])
            swap.append(r["swap_realized_fdr"]); plain.append(r["plain_realized_fdr"])
        figures[fam] = {"target_alpha": xs, "realized_fdr": ys, "ci_low": los, "ci_high": his,
                        "decoy_fdr_hat": decoy, "swap_realized_fdr": swap, "plain_realized_fdr": plain,
                        "k_floor": [r["k_floor"] for r in diag["rows"]],
                        "certified": [r["certified"] for r in diag["rows"]]}

    print("\n--- Entrapment corroboration (r=1) ---")
    for a, e in m["entrapment"].items():
        print(f"  alpha={a}: N_T={e['N_T']} N_E={e['N_E']} combined={fmt(e['fdp_combined'])} "
              f"CI={e.get('fdp_combined_ci')} paired={fmt(e['fdp_paired'])} "
              f"realized_gold={fmt(e['realized_fdr_gold'])} decoy_hat={fmt(e['decoy_fdr_hat'])} "
              f"agree_realized={e['agree_realized']} agree_decoy={e['agree_decoy']}")

    print("\n--- PRE-REGISTERED DISCONFIRMATION ---")
    dc = m["disconfirmation"]
    print(f"  family={dc['family']} alpha*={dc['alpha_star']} realized_fdr={fmt(dc['realized_fdr'])} "
          f"CI={dc['ci']} tau={dc['tau']}")
    print(f"  n_false_total_in_family={dc['n_false_total_in_family']} (N_false_min={meta['N_false_min']})")
    print(f"  VERDICT = {dc['verdict']}")
    print(f"  reason: {dc['reason']}")

    # sanity checks
    print("\n--- SANITY CHECKS ---")
    bridge = figures["bridge"]
    cf = [y for y in bridge["realized_fdr"] if y is not None]
    sw = [y for y in bridge["swap_realized_fdr"] if y is not None]
    if cf and sw:
        print(f"  swap mean realized ({sum(sw)/len(sw):.3f}) vs counterfactual mean "
              f"({sum(cf)/len(cf):.3f}) -- swap should be >= (more anti-conservative): "
              f"{'OK' if sum(sw)/len(sw) >= sum(cf)/len(cf) - 1e-9 else 'NOTE: not observed'}")
    figures["meta"] = {"alpha_star": m["alpha_star"], "tau": meta["tau"],
                       "calibration_verdict": m["calibration_verdict"],
                       "disconfirmation_verdict": dc["verdict"]}
    (WS / "figures_data.json").write_text(json.dumps(figures, indent=2))
    print("\n[wrote figures_data.json]")


if __name__ == "__main__":
    main()
