#!/usr/bin/env python3
"""Print the headline results from method_out.json (no API). uv run summarize.py [path]."""
import json
import sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else "method_out.json")
m = json.loads(p.read_text())["metadata"]
dc = m["dataset_counts"]
print(f"== {p.name} ==")
print(f"docs={dc['n_docs']} reals={dc['n_reals']} TRUE={dc['n_true']} FALSE={dc['n_spont_false']} "
      f"(mh_false={dc['n_spont_false_multi_hop']}) n_extract={dc.get('n_extract_samples')}")
print(f"cost=${m['runtime']['cost_usd']:.4f} live={m['runtime']['n_calls_live']} "
      f"warm={m['runtime'].get('n_calls_warm_fallback')} elapsed={m['runtime']['elapsed_s']}s")
print(f"extraction: atomic P={m['extraction_quality']['atomic_precision']:.3f} "
      f"R={m['extraction_quality']['atomic_recall']:.3f} "
      f"mh_acc={m['extraction_quality']['multihop_relation_accuracy']:.3f}")

print("\n-- per-family realized-FDR diagonal (self-consistency) --")
for fam in ("atomic", "multi_hop", "pooled"):
    d = m["primary_diagonal_self_consistency"][fam]
    print(f"  [{fam}] n_false_total={d['n_false_total']} populable={d['populable']} "
          f"alpha*={d['reachable_alpha_floor']} n_pairs={d['n_pairs']}")
    for r in d["rows"]:
        cert = "CERT" if r["certified"] else "    "
        print(f"    a={r['target_alpha']:.2f} {cert} dfh={r['decoy_fdr_hat']} "
              f"realized={r['realized_fdr']} CI=[{r['ci_low']},{r['ci_high']}] "
              f"n_adm={r['n_admitted']} self_report_anti={r['self_report_anti_conservative']}")
    pe = d.get("paired_exchangeability") or {}
    print(f"    PAIRED: win_rate={pe.get('tail_win_rate_false_pairs')} "
          f"ci={pe.get('win_rate_ci')} covers_half={pe.get('ci_covers_half')} "
          f"n_tail={pe.get('n_tail_false_pairs')}")

pd = m["primary_disconfirmation_verdict"]
print(f"\nPRIMARY DISCONFIRMATION: {pd['verdict']} alpha*={pd.get('alpha_star')} "
      f"realized={pd.get('realized_fdr')} CI={pd.get('ci')} "
      f"self_report_disconfirmed={pd.get('self_report_disconfirmed')}")

cr = m["crux_full_and_tail_self_consistency"]["regions"]
print("\n-- marginal CRUX (decoy vs spontaneous-error), powered n --")
for rn in ("full", "top50pct", "top25pct"):
    rd = cr[rn]["decoy_vs_spont"]
    print(f"  {rn}: n_decoy={cr[rn]['n_decoy']} n_spont={cr[rn]['n_spont']} "
          f"ks_p={rd['ks_p']:.4g} mw_p={rd['mw_p']:.4g} ad_p={rd['ad_p']:.4g} "
          f"perm_p={rd['perm_p']:.4g} verdict={cr[rn]['verdict']}")

pg = m["paired_across_GS"]
print(f"\n-- PAIRED across (G,S): {pg['verdict']} (n_warm_docs={pg['n_warm_docs']}) --")
for c in pg["configs"]:
    print(f"  G={c['G']:>9} S={c['S']:>9} [{c['score_config']}/{c['decoy_set']}] "
          f"win_rate={c['paired_win_rate_false']} ci={c['win_rate_ci']} "
          f"n_false={c['n_false_pairs']} powered={c['powered']} "
          f"covers_half={c['ci_covers_half']} realized={c['realized_fdr']}")

ds = m["density_strata"]
print(f"\n-- DENSITY strata de-confound: {ds['verdict']} --")
for s in ds["strata"]:
    print(f"  {s['stratum']:>10} k={s['k_range']} n_false={s['n_false_pairs']} "
          f"density={s['false_density']} win_rate={s['paired_win_rate_false']} "
          f"realized={s['realized_fdr']} powered={s['powered']}")

sa = m["strong_extractor_arm"]
if sa.get("ran"):
    print(f"\n-- STRONG-extractor arm ({sa['extractor']}): {sa['verdict']} --")
    print(f"  n_docs={sa['n_docs']} n_mh_reals={sa['n_mh_reals']} n_false={sa['n_false']} "
          f"strong_mh_acc={sa['strong_mh_accuracy']} nano_mh_acc={sa['nano_mh_accuracy_same_docs']} "
          f"lift={sa['mh_acc_lift']}")
    print(f"  paired win_rate={sa['paired']['paired_win_rate_false']} "
          f"realized={sa['paired']['realized_fdr']} nonexch={sa['paired']['paired_nonexchangeable']}")
else:
    print(f"\n-- STRONG-extractor arm: NOT RUN ({sa.get('reason','')[:80]})")

lad = m["s1b_difficulty_ladder"]
print(f"\n-- S1b ladder: {lad['verdict']} (powered_rungs={lad['n_powered_rungs']}/"
      f"{len(lad['rungs'])}, n_ladder_docs={lad.get('n_ladder_docs')}) --")
for r in lad["rungs"]:
    print(f"  {r['rung']:>16} n_false={r['n_false_pairs']:>4} powered={r['powered']} "
          f"win_rate={r['tail_win_rate']} ci={r['win_rate_ci']} "
          f"detected_anti={r['detected_anti_conservative']}")

bh = m["bh_correction"]
print(f"\nBH q=0.05: {sum(1 for b in bh if b['reject'])}/{len(bh)} tests reject")
