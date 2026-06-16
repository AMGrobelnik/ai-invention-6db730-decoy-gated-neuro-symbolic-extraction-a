# Re-DocRED Operational Wedge — Decoy-Gating vs Plain Confidence Threshold

**Question (S4).** At *matched recall*, does a label-free **decoy-competition FDR gate**
(knockoff+ statistic `W_i = max(Z_i, Z̃_i)·sign(Z_i − Z̃_i)`) admit a *cleaner* set of
LLM-extracted atomic facts into a symbolic layer than a **plain confidence threshold** (rank
by the raw score `Z_i`) — measured by atomic-fact precision and multi-hop hallucinated-conclusion
rate? The plain threshold is the load-bearing foil; CoT, BM25-RAG and a labeled Mohri–Hashimoto
conformal back-off are secondary context.

Only **relative** comparisons at matched recall are asserted: Re-DocRED has residual false
negatives that depress recall and inflate hallucination counts for **all** systems equally, so
no absolute realized-FDR diagonal is claimed (that role belongs to the separate CLUTRR anchor).

## Pipeline (one shared triple space)

All five systems are mapped into the **identical** `(title, P-code, head_id, tail_id)` Re-DocRED
triple space by ONE fixed aligner and scored by the official tuple-matching metric against human
gold.

- **Stage 1 — `extract.py` (API-heavy, checkpointed, resume-safe).** Per document:
  1. **Over-generating extraction** (LINC/Logic-LM style, `n=3` samples @ T=0.7, dedup, cap 30).
  2. **Isolated graded scoring** `Z_i` of each real candidate — logprob *yes*-token probability
     (verbalized `[0,1]` fallback), provenance-blinded.
  3. **Property-matched counterfactual decoys** (DeepCoy principle): recombine the document's OWN
     entities into a FALSE pairing so the decoy is *equally document-grounded* as the real
     candidate; verify **non-entailment** (regenerate up to 3×, log contamination); score `Z̃_i`
     with the identical isolated protocol → `W_i`.
  4. Baselines: **CoT** (think→emit triples), **RAG** (BM25 top-5 sentence retrieval→triples),
     and the **conformal** frequency signal (`N=5` extra stochastic samples).
- **Stage 2 — `analyze.py` + `method.py` (pure-Python + small memoized relation-pick API).**
  - **Aligner.** Relation = MiniLM top-8 P-code shortlist → fixed temp-0 LLM pick (or NO_RELATION),
    embedding-argmax fallback (floor 0.45). Entity linking = exact → alias/substring → MiniLM
    cosine ≥ 0.6. Applied identically to every system **and to gold surface forms** (self-error
    probe).
  - **Official metric + PR curves** per system; **METHOD ranks by `W_i`, PLAIN by `Z_i` over the
    IDENTICAL candidate+alignment pool** (fairness invariant: identical max recall — checked).
  - **Matched-recall wedge:** precision per system across a recall grid; headline
    `Δ(r) = prec_METHOD(r) − prec_PLAIN(r)` with document-block bootstrap CIs (B≥2000) and BH
    correction. **Pre-registered disconfirmation:** wedge "collapses to thresholding-is-enough" if
    no recall point has `Δ` CI entirely > 0.
  - **knockoff+ operating points** (`α ∈ {0.05,0.1,0.2,0.3,0.5}`, eq. 1.9, with the `1/k` floor).
  - **Multi-hop hallucinated-conclusion rate:** forward-chain a fixed Datalog rule set
    (`rules_list` in the output) over each system's admitted facts at partial admission; report
    relative METHOD−PLAIN delta (at max recall both admit the identical pool, so the delta is read
    at ~70% of max recall).
  - **Conformal operating points** (Mohri–Hashimoto): `q̂` calibrated on the labeled **pilot**
    split; `n_calibration_labels` reported (METHOD uses 0).
  - **Alignment-error confound check:** aligner self-error probe on gold + perturbation sensitivity
    (uniform P-code noise 5/10/20 %, embedding-only aligner, strict EL floor 0.7) — the wedge sign
    must persist.

## Model / cost

`openai/gpt-4.1-nano` via OpenRouter (logprobs + auto-caching). Exact cost is read from
`usage.cost` after every call and appended to `logs/cost.jsonl`. Soft cap ~$3, **HARD STOP $10**
(asserted after every call; partial checkpoints flushed on stop).

## Run

```bash
uv run method.py --stage all --data mini                       # 3-doc smoke test
uv run method.py --stage all --split confirmatory --limit 152 \
                 --calib-limit 36 --bootstrap-B 2000            # full experiment
```

Output: `method_out.json` (schema `exp_gen_sol_out`): figure-ready PR curves, matched-recall
precision wedge + CIs, hallucination bars, knockoff/conformal operating points, alignment-check,
verdict, and per-document `predict_*` triples.

## Files

`common.py` config/cost-meter/parsing/embedding · `llm.py` async OpenRouter client ·
`prompts.py` prompt builders · `extract.py` Stage 1 · `analyze.py` Stage 2 metrics ·
`method.py` orchestrator + output · `summarize.py` headline pretty-printer · `test_plumbing.py`
no-API mapping-core unit test.
