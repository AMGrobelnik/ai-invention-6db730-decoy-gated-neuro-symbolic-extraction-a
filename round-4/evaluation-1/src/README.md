# Evaluation — Demote the gold-free regime-diagnostic to a heuristic

**Zero-API. Pure-CPU. `$0.00` spend. Deterministic** (only the winrate CIs use a seeded
document-block bootstrap, `seed=0`, `B=2000`).

This evaluation performs **no new measurements** and makes **no LLM calls**. Every number is
either an algebraic identity or a re-reading / recomputation over arrays already cached by the
two dependency experiments. It resolves reviewer novelty-MAJOR / hypothesis claim **S4c** by
quantitatively demoting the "gold-free regime-diagnostic" from a substantive novel contribution
to a deployment-time **heuristic**.

## Inputs (read-only)

| Anchor | Path | What is read |
|---|---|---|
| `art_RZC2468yZ-Jh` (Re-DocRED regime-diagnostic) | `.../iter_3/gen_art/gen_art_experiment_3` | **canonical** per-candidate `Z, Zt, W` in `checkpoints/confirmatory/redocred_*.json` (152 docs, 4384 candidates); `metadata.regime_diagnostic` summary for cross-checks |
| `art_sBLQqsdm3EIA` (CLUTRR self-consistency diagonal) | `.../iter_3/gen_art/gen_art_experiment_1` | `metadata.primary_disconfirmation_verdict` and `primary_diagonal_self_consistency.multi_hop` **scalars** only |

The A≡C identity is recomputed from the **checkpoints** (raw `Z, Zt, W`), not the summary, so the
verification is independent of the prior `regime.py` code.

## What it computes (metric groups)

1. **The A≡C identity (central deliverable).** `W_i = sign(Z_i−Zt_i)·max(Z_i,Zt_i)`, so
   `1[W==Z] = 1[Z>Zt]` (modulo the measure-zero `Z=Zt=0` edge) and the signal-A win indicator is
   `1[Zt>=Z] = 1−1[Z>Zt]`. Therefore for **any** candidate set S:
   `frac(W==Z | S) = 1 − winrate(S)` exactly, up to the `Z=Zt=0` tie fraction. Empirically the
   per-set residual **equals** the `Z=Zt=0` fraction to ~1e-16 in every set, `corr(a,c) ≈ −0.99`,
   and the admitted-set Spearman is `0.990959` with ties / `1.0` without the `W=0` ties
   (mechanically forced). Verdict: **CONFIRMED** — signal C is an algebraic restatement of signal
   A and carries zero new information.
2. **Signal-dependence quantification.** Of the nominally "4 signals", the decoy-exchangeability
   axis is double-counted (A≡C, with B a distributional refinement of the same axis); only D adds
   a genuinely new array (self-consistency `f`). **Effective independent axes = 2.**
3. **Regime-map-as-heuristic + mispredict audit.** The map's one validated anchor (Re-DocRED null)
   is **near-mechanical** (triggered by `frac(W==Z)=0.94` = signal C, which restates the realized
   null); it **mispredicts** CLUTRR self-consistency (marginal win-rate `0.482` ⇒ predicted "gate
   adds value", yet the powered paired diagonal is **DISCONFIRMED**, realized FDR `1.0`, CI
   `[0.66,1.0]`). **independent_and_correct_count = 0.**
4. **Honest figure-ready regime panel** (`figures/regime_panel.jpg` + arrays + full caption) and a
   one-paragraph **reframing recommendation**: lead with the marginal-vs-paired conceptual result;
   present the diagnostic as a heuristic with stated A≡C redundancy; never present "W==Z so ranking
   unchanged" as a forecast.

## Run

```bash
uv venv .venv --python=3.12 && source .venv/bin/activate
uv pip install numpy "scipy>=1.11" matplotlib loguru
python eval.py            # full (all 152 checkpoints); ~17s, <1 GB RAM, $0
python eval.py --limit 3  # smoke test on 3 checkpoints
```

## Outputs

- `eval_out.json` — schema `exp_eval_sol_out` (validated); rich blocks
  (`a_equals_c_identity`, `signal_dependence`, `regime_panel`, `demotion_verdict`, `figure_panel`,
  `reframing_recommendation`, `reproducibility`) live under `metadata` because the schema permits
  only `{metadata, metrics_agg, datasets}` at the top level. `mini_/preview_/full_` variants also
  validate.
- `figures/regime_panel.jpg` — the honest 2-axis panel (optional; arrays are mandatory and always
  emitted).

All headline numbers reproduce the cached summary to 5 dp: `frac(W==Z)=0.9391`, top-50% tail
`winrate=0.04471` ⇒ `frac_eq=0.95529`, admitted Spearman `0.99096`, admitted Jaccard `0.91609`.
Everything here is derivable from the two cached `full_method_out.json` files + the Re-DocRED
confirmatory checkpoints.
