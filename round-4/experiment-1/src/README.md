# Iter-4 P1 — Powered & de-confounded self-consistency CLUTRR FDR calibration diagonal

The headline artifact: a per-family (atomic / multi_hop) **realized-FDR-vs-target-α calibration
diagonal** for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted
kinship facts into a symbolic layer, scored under the diagnostic-VALIDATED **K=5 self-consistency**
elicitation on the **full ≈593-doc** (k≥6 oversampled) CLUTRR crisp-gold corpus — the scale iter-3
*designed* but only ran on a 40-doc checkpoint. Powering to the full corpus moves the primary
disconfirmation and the marginal-exchangeability crux p-values off the n=12-pair borderline.

## What runs (`method.py`) — method + baselines + controls, one pipeline

| arm | what |
|-----|------|
| **METHOD** | counterfactual-decoy knockoff+ gate, K=5 self-consistency elicitation (headline) |
| **BASELINE 1** | PLAIN raw-confidence threshold gate (decoy-free; purely-neural foil) |
| **BASELINE 2** | random in-doc SWAP-decoy knockoff gate (anti-conservative negative control) |
| **CONTRAST** | the SAME diagonal under VERBALIZED confidence (discreteness / loose-target artifact) |
| **CORROBORATE** | deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025), r=1 |

### Iteration-4 additions (the three NEW analyses)
1. **PAIRED statistic, distinct from the marginal & across (G,S)** — `paired_across_GS`. Each
   diagonal row already carries `paired_exchangeability` (the per-pair sign-flip win-rate the
   knockoff+ theorem actually requires, reported SEPARATELY from the marginal crux). The new
   `paired_exchangeability_across_GS` reruns it across the four (Generator, Scorer) configs —
   {nano,ministral-8b} × {nano,ministral-8b} — so paired-layer de-circularization is **evidenced**,
   not asserted. Warm on the 40 original-pilot docs (cfo = ministral-generated decoys + ministral-SC
   scores reused from the iter-2 cache ⇒ ≈$0).
2. **De-confound extractor-weakness / error-density** — `density_strata` (FREE, 0 API): bins
   multi_hop FALSE pairs by chain length k into LOW/MED/HIGH genuine-false-density strata and reports
   the paired win-rate + realized FDR per bin. Optional **`strong_extractor_arm`** (Phase 6b, budget-
   gated, `--strong`): re-extracts with gpt-4.1-mini, scorer fixed at nano-SC, to test whether the
   per-pair sign-flip failure PERSISTS or VANISHES with a competent extractor. (The FULL
   extractor-strength × density matrix is owned by the sibling iter-4 artifact; here it is a preview.)
3. **S1b ladder power-or-bound** — `analyze_s1b_ladder` scores L0..L4 on pilot ∪ first-N confirmatory
   so each rung reports its realized false-pair n and a `powered` flag; under-floor rungs are reported
   PURELY as underpowered (the contradicted "detects only gross decoys" narrative is not asserted).

## Reuse (tested code, warm-started)
- `fdr_core.py`, `fdr_stats.py`, `llm_client.py` reused verbatim from iter-2/iter-3.
- Extraction / decoy-gen / scoring prompts + per-doc seeds are byte-identical to iter-2/iter-3, so the
  593-corpus's original-190 prefix warm-starts deterministically from the read-only `WARM_CACHES`
  (iter-3 P1 + iter-2 EXP2). Only NEW docs cost money. `gen_cf_compat` reproduces iter-2's
  single-choice cfo generation exactly for cache identity.
- `data.py` regenerates the corpus; `full_data_out.json` (593 docs = 535 confirmatory + 58 pilot) is
  the iter-3 build reused directly (a deterministic prefix-superset of the original 190).

## Run
```bash
uv run method.py --selftest      # offline stat unit tests (no API) — gate to any API call
uv run method.py --mini          # 3-doc smoke
uv run method.py --n-docs 40     # warm-cache determinism check (reproduces iter-3, ~$0 new)
uv run method.py                 # full 593-doc corpus -> method_out.json + figures/
uv run method.py --strong --strong-cap 80    # + the Phase-6b stronger-extractor de-confound preview
uv run method.py --analyze-only  # re-run analysis + output from the saved pipe checkpoint (no API)
```
CPU-only, async OpenRouter I/O (`openai/gpt-4.1-nano`; `mistralai/ministral-8b-2512` for cross-family
(G,S); `openai/gpt-4.1-mini` strong-extractor arm). Soft cap $4, HARD STOP $10, cost logged after every
call to `logs/cost.jsonl`. Optional arms (G,S matrix, strong extractor, full ladder scope) are
budget-gated so the headline diagonal always completes. `--light` restricts entrapment+verbalized to
the pilot slice (fallback).

## Output
`method_out.json` (schema `exp_gen_sol_out`): rich `metadata` (per-family powered diagonal with the
(target α, decoy_fdr_hat, realized) triple + doc-block bootstrap CIs + self-report disconfirmation;
`paired_vs_marginal`; `paired_across_GS`; `density_strata`; `strong_extractor_arm`; powered S1b ladder;
marginal crux; entrapment; BH table; primary-disconfirmation verdict; runtime+cost) + per-real
`examples` carrying the self-consistency / verbalized Z-scores, W-statistics, and per-α admission
predictions. Five figures in `figures/`.
```
F1 figure_diagonal_self_consistency.jpg   per-family realized-FDR-vs-α diagonal (+CIs, decoy_fdr_hat)
F2 figure_crux_cdfs_self_consistency.jpg  decoy / spontaneous-error / true-positive CDF overlay
F3 figure_s1b_ladder.jpg                  S1b L0..L4 tail win-rate + CIs
F4 figure_paired_across_GS.jpg            paired win-rate across the 4 (G,S) configs
F5 figure_deconfound_density.jpg          paired win-rate / realized FDR vs false-positive density
```
