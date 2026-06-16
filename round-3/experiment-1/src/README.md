# Iter-3 P1 — Powered self-consistency CLUTRR FDR calibration diagonal

The **single primary artifact**: a per-family (atomic / multi_hop) realized-FDR-vs-target-α
**calibration diagonal** for the label-free decoy-competition (knockoff+) FDR gate that admits
LLM-extracted kinship facts into a symbolic layer, scored under the diagnostic-VALIDATED
**K=5 self-consistency** elicitation on a **scaled** (≈593-doc, k≥6 oversampled) CLUTRR
crisp-gold corpus.

## What runs

`method.py` implements method + baselines + controls side-by-side in one pipeline:

| arm | what |
|-----|------|
| **METHOD** | counterfactual-decoy knockoff+ gate, self-consistency elicitation (headline) |
| **BASELINE 1** | PLAIN raw-confidence threshold gate (decoy-free; purely-neural foil) |
| **BASELINE 2** | random in-doc SWAP-decoy knockoff gate (anti-conservative negative control) |
| **CONTRAST** | the SAME diagonal under VERBALIZED confidence (discreteness/loose-target artifact) |
| **CORROBORATE** | deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025), r=1 |

### Iteration-3 additions (reviewer-driven)
- **(A)** self-consistency is the headline elicitation for the per-family diagonal.
- **(B)** every diagonal row surfaces the **(target α, decoy_fdr_hat, realized FDR) triple**
  with a pre-registered **self-report disconfirmation** (the gate's own `decoy_fdr_hat` is
  disconfirmed where it is anti-conservative vs realized beyond τ, *even when realized < α*).
- **(C)** verbalized contrast on the SAME data (quantified discreteness/loose-target artifact).
- **(D)** an **S1b difficulty ladder** L0→L4 (foreign-swap → in-doc swap → random-vocab →
  cf_2nd → primary-cf) scored under the SAME self-consistency elicitation to repair-or-bound
  the win-rate diagnostic blind spot.
- **(E)** independent foreign-entity entrapment corroboration restricted to α*.
- **(F)** full crux match (tail fail-to-reject + full-distribution result + tail-only
  decision-relevance justification).
- **(G)** Benjamini–Hochberg across ALL validation tests.
- **(H)** Generator≠Scorer carried forward as SETTLED (no new budget).
- **(I)** the single primary-disconfirmation verdict under self-consistency on `multi_hop`.

## Reuse (tested code from iter-2)
- `fdr_core.py` (iter-2 EXP1): entrapment FDP estimators, plain gate, α-certifiable.
- `fdr_stats.py` (iter-2 EXP2): knockoff+, signed-max W, doc-block bootstrap, BH, KS/MW/AD/perm,
  per-doc rank-normalization, decoy/baseline realized-FDR.
- `llm_client.py` (iter-2 EXP2): `OpenRouterClient` (disk cache, exact `usage.cost`, $10 hard
  stop) + `parse_yes_conf`. Extended with a **read-only `fallback_cache_dirs`** warm-start so the
  190-doc prefix's self-consistency scores hit the iter-2 cache (only NEW docs cost money).
- Extraction / decoy-gen / scoring prompts and per-doc seeds are byte-identical to iter-2 so the
  scaled corpus's original-190 prefix warm-starts deterministically.

## Run
```bash
uv run method.py --selftest      # offline stat unit tests (no API)
uv run method.py --mini          # 3-doc smoke
uv run method.py --n-docs 40     # scaling checkpoint
uv run method.py                 # full scaled corpus  -> method_out.json + figures/
```
CPU-only, async OpenRouter I/O (`openai/gpt-4.1-nano`), soft cap $3 / HARD STOP $10, cost
logged after every call to `logs/cost.jsonl`. `--light` restricts entrapment+verbalized to the
pilot slice (budget fallback).

## Output
`method_out.json` (schema `exp_gen_sol_out`): rich `metadata` (all analyses above) +
per-real `examples` carrying the self-consistency / verbalized Z-scores, W-statistics, and
per-α admission predictions. Figures in `figures/`. `data.py` regenerates the scaled corpus.
