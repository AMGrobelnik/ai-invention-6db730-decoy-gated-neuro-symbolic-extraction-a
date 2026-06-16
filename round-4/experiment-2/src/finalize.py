#!/usr/bin/env python3
"""Post-run finalize: inject the TRUE grand-total LLM spend (summed across every process
that wrote to logs/cost.jsonl) into method_out.json metadata, and print a verdict summary."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
grand = sum(json.loads(l)["cost"] for l in (HERE / "logs" / "cost.jsonl").open())
out_path = HERE / "method_out.json"
out = json.loads(out_path.read_text())
m = out["metadata"]
m["grand_total_llm_spend_usd_all_processes"] = round(grand, 4)
m.setdefault("cost_note", (
    "total_cost_usd is the final reproducible run's process spend; "
    "grand_total_llm_spend_usd_all_processes sums every probe/checkpoint/run in this workspace."))
out_path.write_text(json.dumps(out, indent=2))

v = m["earned_vs_scoped_verdict"]
print(f"GRAND TOTAL LLM spend (all processes): ${grand:.4f}")
print(f"VERDICT: {v['verdict']}")
print(f"strong_extractor={v['strong_extractor']} competent={v['strong_competent']} "
      f"earned_cells={v['n_earned_cells']} scoped_cells={v['n_scoped_cells']}")
print(f"robustness({m['robustness_alt_normalization']['normalization_pool']}): "
      f"{m['robustness_alt_normalization']['verdict']}")
sa = m["sanity_anchor_iter3_reproduction"]
print(f"sanity_anchor reproduces_iter3={sa.get('reproduces_iter3_direction')} "
      f"(nano realized@0.5={sa.get('realized_fdr_at_0.5')} paired_wr={sa.get('paired_win_rate')})")
print("\n-- strong multi_hop persistence cells --")
for r in m["persistence_matrix"]:
    if r["extractor"].endswith("mini") and r["family"] == "multi_hop":
        print(f"  dens={r['density']} nF={r['n_false']} realized@a*={r['realized_fdr_at_alpha_star']} "
              f"ci={r['ci_at_alpha_star']} paired_wr={r['paired_win_rate']} ci={r['paired_win_rate_ci']} "
              f"pf={r['paired_fails']} anti={r['anti_conservative']} gc={r['gate_controls']} "
              f"marg={r['marginal_holds']} pow={r['powered']} unstable={r['unstable']}")
print("-- nano multi_hop (weak-extractor reference) --")
for r in m["persistence_matrix"]:
    if r["extractor"].endswith("nano") and r["family"] == "multi_hop":
        print(f"  dens={r['density']} nF={r['n_false']} realized@a*={r['realized_fdr_at_alpha_star']} "
              f"paired_wr={r['paired_win_rate']} ci={r['paired_win_rate_ci']} pf={r['paired_fails']} "
              f"marg={r['marginal_holds']} comp={r['competent']}")
print("-- strong atomic (competent-regime contrast) --")
for r in m["persistence_matrix"]:
    if r["extractor"].endswith("mini") and r["family"] == "atomic":
        print(f"  dens={r['density']} nF={r['n_false']} realized@a*={r['realized_fdr_at_alpha_star']} "
              f"paired_wr={r['paired_win_rate']} pf={r['paired_fails']} gc={r['gate_controls']} "
              f"paired_ok={r['paired_ok']} marg={r['marginal_holds']}")
