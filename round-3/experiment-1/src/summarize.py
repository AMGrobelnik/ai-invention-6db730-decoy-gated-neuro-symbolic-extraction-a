#!/usr/bin/env python3
"""Print the headline results of method_out.json (or a given path) compactly."""
import json
import sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else "method_out.json")
m = json.loads(p.read_text())["metadata"]


def f(x):
    return "  -  " if x is None else f"{x:.3f}" if isinstance(x, float) else str(x)


dc = m["dataset_counts"]
print(f"=== {m['method_name'][:70]} ===")
print(f"headline elicitation={m['headline_elicitation']}  verdict={m['headline_verdict']}")
print(f"docs={dc['n_docs']} pilot={dc['n_pilot']} reals={dc['n_reals']} "
      f"TRUE={dc['n_true']} FALSE={dc['n_spont_false']} (mh_false={dc['n_spont_false_multi_hop']}, "
      f"atomic_false={dc['n_spont_false_atomic']}) contamination={f(dc['contamination_rate_decoys'])}")
eq = m["extraction_quality"]
print(f"extraction: atomic P={f(eq['atomic_precision'])} R={f(eq['atomic_recall'])} "
      f"multihop_acc={f(eq['multihop_relation_accuracy'])}")

for elic, key in (("SELF-CONSISTENCY (headline)", "primary_diagonal_self_consistency"),
                  ("VERBALIZED (contrast)", "contrast_diagonal_verbalized")):
    print(f"\n--- {elic} diagonal ---")
    for fam in ("multi_hop", "atomic"):
        d = m[key][fam]
        pe = d.get("paired_exchangeability") or {}
        print(f"  [{fam}] populable={d['populable']} n_false={d['n_false_total']} "
              f"reach_floor={d['reachable_alpha_floor']} "
              f"paired_exch_wr={f(pe.get('tail_win_rate_false_pairs'))} ci={pe.get('win_rate_ci')}")
        print("     alpha | dfh   | realized [CI]            | n_adm | cert | selfrep_anti | swap | plain")
        for r in d["rows"]:
            print(f"     {r['target_alpha']:<5} | {f(r['decoy_fdr_hat']):<5} | "
                  f"{f(r['realized_fdr'])} [{f(r['ci_low'])},{f(r['ci_high'])}] | "
                  f"{r['n_admitted']:<5} | {str(r['certified']):<5}| "
                  f"{str(r['self_report_anti_conservative']):<5} | {f(r['swap_realized_fdr'])} | {f(r['plain_realized_fdr'])}")

print("\n--- S1b LADDER:", m["s1b_difficulty_ladder"]["verdict"], "---")
for r in m["s1b_difficulty_ladder"]["rungs"]:
    print(f"  {r['rung']:<16} wr={f(r['tail_win_rate'])} ci={r['win_rate_ci']} "
          f"n_false={r['n_false_pairs']} detected={r['detected_anti_conservative']} covers0.5={r['ci_covers_half']}")

for tag, key in (("SC", "crux_full_and_tail_self_consistency"),
                 ("VB", "crux_full_and_tail_verbalized")):
    print(f"\n--- CRUX [{tag}] ---")
    for rn, rd in m[key]["regions"].items():
        print(f"  {rn:<9} decoy~spont ks={f(rd['decoy_vs_spont']['ks_p'])} mw={f(rd['decoy_vs_spont']['mw_p'])} "
              f"ad={f(rd['decoy_vs_spont']['ad_p'])} | vs_truepos ks={f(rd['decoy_vs_truepos']['ks_p'])} | {rd['verdict']}")

print("\n--- ENTRAPMENT ---")
for k, e in m["entrapment"].items():
    print(f"  {k}: alpha={e.get('alpha')} N_T={e['N_T']} N_E={e['N_E']} combined={f(e['fdp_combined'])} "
          f"paired={f(e['fdp_paired'])} realized={f(e['realized_fdr_gold'])} agree_realized={e['agree_realized']}")

print("\n--- GENERATOR != SCORER (carried forward):", m["generator_ne_scorer_carried_forward"]["verdict"])
pd = m["primary_disconfirmation_verdict"]
print("\n=== PRIMARY DISCONFIRMATION:", pd["verdict"], "===")
print(f"  alpha*={pd.get('alpha_star')} realized={f(pd.get('realized_fdr'))} CI={pd.get('ci')} "
      f"calib_disconf={pd.get('calibration_disconfirmed')} self_report_disconf={pd.get('self_report_disconfirmed')}")
print("  reason:", pd.get("reason"))
bh = m["bh_correction"]
print(f"\nBH: {len(bh)} tests, {sum(1 for b in bh if b['reject'])} reject at q=0.05")
rt = m["runtime"]
print(f"runtime: {rt['elapsed_s']}s cost=${rt['cost_usd']} live={rt['n_calls_live']} cached={rt['n_calls_cached']}")
