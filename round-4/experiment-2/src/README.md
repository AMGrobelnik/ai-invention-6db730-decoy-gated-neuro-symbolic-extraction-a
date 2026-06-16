# Iter-4 dir-2 — P1-DECONFOUND

A **2-axis (extractor-strength × false-positive-density) persistence matrix** that de-confounds
the iteration-3 disconfirmation (multi_hop realized FDR 1.0 at α\*=0.5, paired sign-flip failure)
from a *pathological weak extractor* (gpt-4.1-nano forced multi-hop relation accuracy ≈0.17).

The label-free decoy-competition **knockoff+** gate admits LLM-extracted kinship facts into a
symbolic layer; each real competes against a property-matched **counterfactual decoy**
(W = signed-max), and the gate thresholds W (Barber–Candès eq. 1.9, the +1 kept) to certify
realized FDR ≤ α.

## The controlled factorial (`method.py`)

The extractor is also the **scorer** and the **decoy generator** (faithful self-detecting gate —
"can a competent model score its OWN errors").

| axis | levels |
|------|--------|
| **A — extractor strength** | `gpt-4.1-nano` (mh_acc≈0.17, weak) vs a Phase-0-verified **`gpt-4.1-mini`** (mh_acc≈0.45, competent) |
| **B — false-positive density** | post-hoc stratified subsample of the scored real pool to ~20% / 50% / 85% genuine-FALSE (**free** — reuses cached scores) + native |
| family | `multi_hop` (registered populable family) · `atomic` (contrast) |

Per (extractor × density × family) **cell**:
- realized-FDR-vs-α **diagonal** with document-block bootstrap (B≥2000) CIs + the gate's
  `decoy_fdr_hat` + the (α, decoy_fdr_hat, realized) **triple**;
- the **paired win-rate over FALSE pairs** at the operative cutoff (the KEY readout — < 0.5 means
  false reals beat their *own* decoys → paired non-exchangeability → anti-conservative);
- the **marginal crux** (decoy ~ spontaneous-error in distribution, and ≠ true-positive);
- a 10-seed subsample robustness spread (UNSTABLE flag if the win-rate straddles 0.5).

**Baseline** (purely-neural foil, side-by-side): the PLAIN raw-confidence threshold gate
(decoy-free), reported in every diagonal row.

## KEY OUTPUT — persist/vanish matrix + EARNED-vs-SCOPED decision rule

- **EARNED** — ≥2 powered competent-extractor cells across ≥2 densities with `marginal_holds`
  AND (`paired_fails` OR `anti_conservative`) ⇒ "marginal ≠ paired at the LLM scoring boundary,
  not an artifact of the weak nano extractor" (paper headline).
- **SCOPED** — competent cells show `gate_controls` AND `paired_ok` ⇒ the paired failure vanishes
  with a competent extractor; report the POSITIVE result and scope iter-3 to the weak-scorer regime.
- **DENSITY_DRIVEN** — failure tracks density for BOTH extractors.
- **UNDERPOWERED_INCONCLUSIVE** — too few powered/stable cells.

## Reuse / warm-start

`fdr_stats.py`, `fdr_core.py`, `llm_client.py` copied verbatim from iter-3 P1. Prompts,
per-doc seeds, extraction, decoy-gen and K=5 self-consistency scoring are byte-identical to
iter-3, so the nano arm **warm-starts from the copied iter-3 cache (≈ free)** and reproduces the
iter-3 sanity anchor (nano × multi_hop × 0.85: realized FDR ≈1.0 at α=0.5, paired win-rate <0.5).
Normalization is per-document rank-normalization over {reals ∪ cf} — identical recipe for both arms.

## Run

```bash
uv run method.py --selftest                  # offline unit tests (no API)
uv run method.py --mini                      # 3-doc smoke, both extractors
uv run method.py --phase0 --phase0-docs 40   # extractor probe (pick the competent extractor)
uv run method.py --strong --n-docs 40        # strong-extractor checkpoint
uv run method.py --n-docs 200                # full matched run (nano + strong)
uv run method.py --analyze-only              # rebuild matrix + figures from checkpoints (free)
```

CPU-only, async OpenRouter I/O, soft cap $4 / HARD STOP $10, cost logged to `logs/cost.jsonl`.

## Result (200 docs matched, gpt-4.1-mini strong arm, $2.94 total)

**VERDICT = EARNED** (robust under both normalization recipes). The iter-3 paired/anti-conservative
knockoff failure **persists — and strengthens — with a competent extractor**, so it is a property
of the LLM self-consistency *scoring* boundary, not an artifact of the weak gpt-4.1-nano extractor.

- **Phase-0**: gpt-4.1-mini clears the competence bar (multi-hop relation accuracy **0.455** ≥ 0.45,
  2.2× nano's 0.205); gpt-4o-mini 0.402 (just misses).
- **Sanity anchor reproduces iter-3 byte-for-byte** at the matched 40-doc scale (nano multi_hop:
  realized FDR **1.0** at α=0.5, **12** admissions all-false, paired win-rate 0.294; W array differs
  in 0/186 reals). At full scale the same weak-nano gate **admits nothing** → iter-3's realized=1.0
  was a 12-admission small-sample tail artifact.
- **Strong (competent) multi_hop**: paired win-rate **CI entirely <0.5 at all three densities**
  (0.27 / 0.37 / 0.35), and a **gold-based anti-conservative breach at density 0.85** (realized FDR
  **0.818**, CI [0.758, 0.860], 306/374 false admitted). The density-0.20 cell is *decoy-controlled*:
  the cf decoy is adequate (marginal VALID, gap −0.018) yet the false reals still beat it (0.268).
- **Mechanism**: the marginal "cf decoys too easy" (tail gap_md < 0) and the paired win-rate < 0.5 are
  two views of the **same self-favoring bias** — the LLM scores its OWN (possibly-wrong) extraction
  above a counterfactual decoy, violating the knockoff null and making the gate anti-conservative
  where the false-positive base rate is high. The bias also appears on the easier **atomic** family.

## Output

`method_out.json` (schema `exp_gen_sol_out`): rich `metadata`
(`phase0_extractor_probe`, `persistence_matrix`, `cells_full`, `earned_vs_scoped_verdict`,
`sanity_anchor_iter3_reproduction`, `extraction_quality`, `bh_correction`, `full_figure_captions`)
+ one `example` per scored real (z_real/z_decoy norm, W, density membership, per-α admit predictions).
Figures `F1`–`F4` in `figures/`.
