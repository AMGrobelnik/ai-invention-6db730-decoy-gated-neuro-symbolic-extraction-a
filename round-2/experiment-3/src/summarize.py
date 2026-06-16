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

print("\nVERDICT:")
print(f"  wedge_confirmed={m['verdict']['wedge_confirmed']} "
      f"disconfirmed={m['verdict']['disconfirmed']} "
      f"n_confirmed_points={m['verdict']['n_confirmed_points']}")
print(f"  {m['verdict']['message']}")
