# Decoy-Competition FDR Gate for LLM Text→Logic Fact Admission — Experiment Artifact

A **label-free False-Discovery-Rate (FDR) gate** that admits LLM-extracted kinship facts
into a symbolic layer **without gold labels**, validated on CLUTRR's *crisp* gold. Each
extracted "real" fact competes against a property-matched **counterfactual decoy** (same
ordered entity pair, a plausible-but-wrong relation, verified non-entailed against gold). A
label-free confidence elicitation scores both; the **knockoff+** rule (Barber–Candès 2015,
eq. 1.9) turns decoy "wins" into an FDR certificate. The experiment stress-tests the gate's
core statistical assumptions and compares it to a purely-neural raw-confidence baseline.

## Headline finding (one sentence)

The gate's validity is **elicitation-dependent**: with single-token **logprob** confidence the
LLM is overconfident in its *own spontaneous errors* so counterfactual decoys are
**anti-conservative** (tail win-rate ≈ 0.34 ≪ 0.5, KS p < 1e-24); with **K=5 self-consistency**
confidence the decoys become **exchangeable** (win-rate ≈ 0.48, 95% CI [0.42, 0.55] covers 0.5,
KS p = 0.48), their score distribution **matches the genuine spontaneous-error tail** (and
differs from true positives), the gate **controls realized FDR ≤ nominal** while the
raw-confidence baseline admits **45–65 %** false facts, and exchangeability is **robust to
Generator ≠ Scorer** across model families (de-circularized).

## The four results (all on the same pipeline, method + baseline + controls side-by-side)

1. **S1 decoy signature.** On the *known-false* reals (genuine extractor errors), real-vs-decoy
   tail win-rate should be ≈ 0.5 (exchangeable). Counterfactual decoys reach 0.482 (CI covers
   0.5) under self-consistency but only 0.34 (CI [0.32,0.37]) under logprob. The **random
   type-matched swap** negative control is flagged anti-conservative under logprob (win 0.32,
   p≈1e-9), validating diagnostic *sensitivity*; the offline synthetic self-test independently
   confirms the win-rate/KS diagnostic detects a deliberately "too-easy" decoy family.

2. **Spontaneous-error tail match (the crux).** The counterfactual-decoy score distribution
   `F_decoy` tracks the genuine spontaneous-error distribution `F_spont` (FALSE reals) — *fail
   to reject* in the admission tail (top-25 %/50 %: KS p = 0.33/0.19) — and differs sharply from
   the true-positive distribution `F_truepos` (KS p ≈ 1e-40). See `figures/fig2_crux_cdf.png`.

3. **Generator ≠ Scorer de-circularization.** Re-running the win-rate test with decoys from
   model G scored by a *different-family* model S (and the symmetric swap) keeps the win-rate's
   CI over 0.5 for **all four (G,S) configs** incl. G≠S, with realized labeled-slice FDR = 0.0
   at α=0.2. Verdict: **ROBUST** — exchangeability is *not* a shared-model artifact.

4. **Method vs purely-neural baseline (hallucination control).** Against crisp gold, the
   decoy-FDR gate's realized FDR ≤ nominal where it certifies (0.417 ≤ 0.5; conservative /
   zero-admit at stricter α on this data), whereas the raw-confidence baseline admits
   254–1758 facts at **45–65 % realized FDR** — exactly the hallucination problem the gate
   prevents. See `figures/fig3_fdr_calibration.png`.

## Dataset & models

* **Data** (READ-ONLY dependency): `…/iter_1/gen_art/gen_art_dataset_1/full_data_out.json` —
  190 CLUTRR-v1 stories (40 pilot + 150 confirmatory), crisp atomic + multi-hop kinship gold,
  chain length k=2..10. CLUTRR is rule-based so gold is exact (no annotation noise) — the
  property that lets it host a realized-FDR-vs-α calibration diagonal.
* **Primary model** `openai/gpt-4.1-nano` (generator + scorer; exposes logprobs; $0.10/$0.40 /M).
* **Cross-family model** `mistralai/ministral-8b-2512` (de-circularization; no logprobs; $0.15/M).
* **Crisp 3-way label** vs gold per (head, relation, tail): TRUE (entailed), FALSE (contradicts
  the gold relation on an enumerated pair = a genuine extractor error), UNDECIDABLE (unlisted
  pair, excluded). Reals are forced relation-predictions over every gold-enumerated pair, so the
  multi-hop pairs form the error-dense family the diagnostics need.

## Scale & cost

190 docs → **1937 reals** (633 TRUE, 1304 spontaneous FALSE, 0 undecidable), 1937 counterfactual
decoys + 1937 swaps, scored under two elicitations on all docs plus a 4-config cross-family
ablation on the 40 pilot docs. Final (cache-warm) run **$0.468**; total project spend across all
gradual-scaling runs ≈ $1.05; hard cap $10 never approached. B=2000 document-block bootstrap;
Benjamini–Hochberg at q=0.05 across 42 validation tests (27 reject).

## Files

| File | What |
|---|---|
| `method.py` | Full pipeline: extraction → counterfactual+swap decoys → isolated provenance-blinded scoring (logprob & self-consistency) → S1 / crux / ablation / baseline analyses → `method_out.json`. CLI: `--selftest`, `--mini`, `--n-docs N`, `--pilot-only`, `--ablation`, `--portable-headline`. |
| `fdr_stats.py` | Pure statistical core (knockoff+ threshold, signed-max W, win-rate, one-sided KS/MW/AD/permutation, tail effect sizes, document-block bootstrap, BH, realized-FDR gates). Unit-tested by `--selftest`. |
| `llm_client.py` | Async OpenRouter client: disk cache (free resumes), exact per-call cost from `usage.cost`, hard-stop at $10, logprob/self-consistency elicitation parsers. |
| `make_figures.py` | Generates `figures/fig1..4*.png`. |
| `method_out.json` | **Primary output** (schema `exp_gen_sol_out`, validated). 1937 examples (one per real, with per-elicitation scores/W and admission predictions) + rich `metadata`. |
| `logs/cost.jsonl` | Per-call cumulative cost trace. |
| `cache/` | Response cache (re-runs reproduce for $0). |

## Reproduce

```bash
uv run method.py --selftest                              # offline stat unit tests (no API)
uv run method.py --ablation --portable-headline          # full 190-doc run (cache → free)
uv run make_figures.py                                   # figures
```

## `method_out.json` → `metadata` map (for the paper writer)

* `headline_finding`, `headline_elicitation`, `headline_verdict` — the one-paragraph result.
* `elicitation_comparison` — per-view (logprob_full / portable_full) verdict + win-rate + CI.
* `s1_decoy_signature_by_elicitation[view][counterfactual|random_swap].rows` — per-α tail
  win-rate, bootstrap CI, KS/MW p, plus a `robustness_sweep` over tail quantiles.
* `spontaneous_error_match_by_elicitation[view]` — `regions{full,top50pct,top25pct}` with
  decoy~spont and decoy~truepos tests, gap effect sizes, and `figure_cdfs` (x grid + 3 CDFs).
* `generator_ne_scorer` — 4 (G,S) configs, win-rate CIs, labeled-slice diagonal, `verdict`,
  `validity_region_statement`.
* `baseline_vs_method_fdr_by_elicitation[view].rows` — realized FDR vs nominal α for the gate
  and the raw-confidence baseline.
* `bh_correction` — every p-value with BH-adjusted p and reject flag.
* `extraction_quality` — free-extraction atomic precision/recall + multi-hop relation accuracy
  (the LLM's genuine, error-prone extraction behaviour the gate operates on).

## Honest limitations

* The knockoff+ gate is **conservative** on this signal: under the calibrated (self-consistency)
  elicitation it certifies admissions only at α=0.5 on 190 docs (0 admits at stricter α). It
  trades power for control — but is never *anti-conservative* like the baseline.
* The full-distribution crux is borderline (KS p≈0.05; MW rejects) — the decoy≈spont match is a
  *tail* phenomenon (top-25 %/50 % clearly VALID), which is the region admission actually uses.
* `gpt-4.1-nano` is a small model; its atomic precision ≈ 0.50 and multi-hop accuracy ≈ 0.20 on
  terse pronoun-heavy CLUTRR stories. These genuine errors are the experimental signal, not a
  confound — the methodology validation does not depend on extractor accuracy.
* Self-consistency reduces the diagnostic's sensitivity to the swap control (both null families
  become exchangeable under it); sensitivity is demonstrated via logprob + the synthetic test.
