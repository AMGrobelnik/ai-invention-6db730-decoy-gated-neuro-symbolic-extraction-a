# P2 — Hallucination-reduction of a decoy-gated neuro-symbolic text→logic pipeline

Executes the goal's binding deliverable on the **24-doc legal/news/regulatory application
anchor** (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver):
a **label-free decoy-competition (knockoff+) FDR gate** that admits LLM-extracted
`(head, relation, tail)` facts into a running logic engine, measured against **raw LLM**,
**RAG (BM25)**, and **chain-of-thought** baselines, with **human-auditable trace-graphs**.

## What runs

`method.py` (one implementation; method + baselines + controls side-by-side):

| Stage | What |
|-------|------|
| 1 | Over-generating extraction (n=3 sample union) → WordNet→SUMO typing → open→gold relation alignment (`+ "other:"` escape) → entity linking → crisp/silver labelling vs gold. |
| 2 | Document-conditioned **counterfactual decoys** + type-matched **swap** control + deterministic **entrapment** (r=1) + **dual elicitation** scoring (single-token logprob softmax P(Yes) **and** K=5 self-consistency) + **knockoff+** gate at every α, per genre × elicitation, with the gate's own `decoy_fdr_hat`, realized FDR vs gold, and the entrapment `FDP_hat` bound + the second-order `self_report_anticonservative` flag. |
| 2b | **PRIMARY METRIC**: hallucinated-fact rate (decoy-gate vs RAW LLM) per genre × elicitation × α, with a **non-circular cross-family adjudicator** (`mistralai/ministral-8b`, validated on legal crisp gold by Cohen's κ), document-block bootstrap CIs, regime tags, and silver lower/upper bounds. |
| 2c | **SECONDARY**: matched-recall precision / hallucination-rate vs RAW / GATE / RAG / CoT. |
| 3 | Reasoning + **auditable trace-graphs**: pure-Python backward-chaining meta-interpreter over admitted facts + hand-authored genre bridge rules; every leaf carries provenance + decoy (`W_i,T,α`) + entrapment (`FDP_hat,r`) certificates; multi-hop corrupted-conclusion rate RAW-KB vs GATE-KB across α. |
| 4 | Benjamini–Hochberg correction, schema-valid `method_out.json`, figures. |

CPU-only. Soft cap $3 (warn), hard stop $10 (`BudgetExceeded`). On-disk cache → free resumes.

## Files
- `method.py` — full pipeline (`fdr_stats.py`, `llm_client.py` reused verbatim from iter-2; `typing_sumo.py` WordNet→SUMO typing; `kb_engine.py` proof engine + DOT/JSON export).
- `method_out.json` (+ `mini_`/`preview_`) — `exp_gen_sol_out` schema: one row per admitted/extracted real fact; metadata holds `hallucination_grid`, `s1_decoy_signature`, `matched_recall_curves`, `extraction_quality`, `multihop_corruption`, `adjudicator_validation`, `trace_graphs`, `bh_correction`.
- `trace_graphs/` — per-doc proof JSON + Graphviz DOT (≥2 per genre).
- `figures/` — `fig1_hallucination_grid`, `fig2_fdr_selfreport`, `fig3_matched_recall`, `fig4_tracegraph_<genre>`, `fig5_multihop_corruption`.

## Reproduce
```bash
uv run method.py --selftest                          # offline unit tests (no API)
uv run method.py --mini --elic logprob --k-sc 2      # 12-doc smoke
PYTHONHASHSEED=0 uv run method.py                    # full 24 docs, both elicitations
uv run make_figures.py
```
`OPENROUTER_API_KEY` must be set. Models: `openai/gpt-4.1-nano` (primary scorer/generator,
logprobs + prompt caching) and `mistralai/ministral-8b` (cross-family adjudicator).

## Honest scope
- Legal gold is **crisp** (CUAD); news/regulatory gold is **silver** (partial recall) — carried per row by `gold_quality` and bracketed by silver lower/upper hallucination bounds.
- SWI-Prolog/janus-swi attempted, **fell back** to the pure-Python engine (identical JSON+DOT trace-graph schema with per-leaf certificates).
- Relation extraction uses open over-generation + LLM alignment to the per-genre gold vocab with an `"other:"` escape; the regime map (where the gate helps / is null / is worse) is reported across the **full** grid, never obscured.

## Iter-4 additions — LLM-as-probabilistic-reasoner (P4) + honest finalized reporting (P2)

This run is a **$0 cache-hit reanalysis** of the same 24-doc anchor (identical deterministic
numbers — verified unchanged against the prior run) that ADDS two deliverables on top:

**(P4) Probabilistic reasoner — `prob_reasoner.py`.** Each document's admitted-fact KB +
genre bridge rules is compiled to a **weighted ProbLog program** and multi-hop conclusion
**marginals** are computed via `get_evaluatable().create_from(PrologString).evaluate()`
(ProbLog primary, **exact weighted-model-counting fallback** that is validated equal to ProbLog
to 1e-9, including the shared-leaf case where naïve noisy-OR fails). Certificate→weight map:
`w_i = (1 − alpha_hat)·calibrate(Z_i)` (gate-consistent shrinkage, DEFAULT) with
`alpha_hat = decoy_fdr_hat` of the operative (genre, portable, α=0.5) gate cell; per-pair
margin `0.5+0.5·W_i` and identity (no-shrinkage) reported as a sensitivity table. **Probabilistic
trace-graphs** (`prob_trace_graphs/`, JSON + DOT) annotate every node with its marginal/weight and
keep every leaf's provenance + decoy + entrapment certificate. Multi-hop marginals are demonstrated
on **regulatory** (real `cross_references+grants_right` / `obligates+has_exception` bridges);
legal/news show single-fact probabilistic admissions. **The deterministic backward-chaining engine
remains the baseline — NO headline number depends on ProbLog.**

**(P2) Honest finalized reporting** (in `method_out.json['metadata']`):
- `atomic_reduction_pooled` — pooled atomic hallucinated-fact reduction per (elicitation, α) with
  document-block bootstrap CIs on the raw−gate **difference**; stated PLAINLY as a **DIRECTIONAL
  ~25% trend, NOT CI-separated at n=24** (`0/40` grid cells, `0/10` pooled cells).
- `multihop_corruption` (+ `ci`) — RAW-KB→GATE-KB(α=0.5) corruption drop **0.52→0.25** with bootstrap
  CIs, `single_genre_origin='regulatory'`, per-system conclusion counts (21→8) and an explicit
  WIDE-CI / single-genre caveat (legal corrupt=0, news derives 0).
- `self_report_regime='conservative'` (`self_report_analysis`) — `decoy_fdr_hat ≥ realized` in
  **all 40** cells (`anti_conservative_cells=0`), the OPPOSITE of the CLUTRR multi-hop
  anti-conservative regime (0.5 < 1.0).
- `figures` — figure-ready arrays + full captions; rendered to PNG by `build_figures.py`
  (`F1` pooled atomic CI bars, `F2` multi-hop corruption + per-genre counts, `F3` decoy_fdr_hat-vs-
  realized scatter with the CLUTRR contrast, `F4` a regulatory probabilistic trace-graph).
  Rendering uses **networkx/matplotlib** (no system `dot` binary).

```bash
uv run prob_reasoner.py                 # probabilistic-reasoner selftest (toy 2-hop=0.63, fallback==ProbLog)
PYTHONHASHSEED=0 uv run method.py        # full run: produces the extended method_out.json ($0, cached)
uv run build_figures.py method_out.json  # render F1–F4 PNGs
```
