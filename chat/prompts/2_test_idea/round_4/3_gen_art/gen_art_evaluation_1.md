# gen_art_evaluation_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_evaluation_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 10:53:21 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Evaluate experimental results using domain-appropriate methods, metrics, and analysis techniques.
When in doubt, prefer more metrics over fewer — but only ones that make sense for the domain.
</task>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx5
type: evaluation
title: >-
  Demote the gold-free regime-diagnostic to a heuristic: prove signal C ≡ signal A (frac(W==Z)=1−winrate), quantify signal
  redundancy, and audit the regime map's mispredictions on an honest 4-point panel
summary: >-
  Pure-CPU, ZERO-API evaluation. Reads ONLY the cached gold-free signals already persisted by art_RZC2468yZ-Jh (Re-DocRED
  regime-diagnostic: metadata.regime_diagnostic + checkpoints/confirmatory/*.json per-candidate Z/Zt/W/conf_samples) and art_sBLQqsdm3EIA
  (CLUTRR self-consistency diagonal: metadata.primary_diagonal_self_consistency, metadata.primary_disconfirmation_verdict,
  metadata.reconciliation_narrative). It (1) FORMALLY derives and EMPIRICALLY verifies that signal C (frac(W==Z), admitted-set
  Spearman) is algebraically the SAME quantity as signal A (marginal tail decoy win-rate), so C carries zero new information;
  (2) quantifies how many of the '4 signals' are genuinely independent axes; (3) re-derives the 2-axis regime map AS A HEURISTIC,
  showing it MISPREDICTS the CLUTRR self-consistency anchor (marginal 0.482 → predicted 'gate adds value'; realized paired
  diagonal DISCONFIRMED, realized FDR 1.0) and that its one 'correct' Re-DocRED prediction is near-mechanical; (4) emits eval_out.json
  with the identity verification, the signal-dependence quantification, the demotion verdict, and figure-ready honest regime-panel
  arrays + full captions, plus a one-paragraph reframing recommendation. No LLM calls; spend = $0.00; deterministic.
runpod_compute_profile: cpu_heavy
metrics_descriptions: |-
  OVERVIEW. This EVALUATION resolves reviewer novelty-MAJOR for claim S4c by quantitatively DEMOTING the 'gold-free regime-diagnostic' from a substantive novel contribution to a deployment-time HEURISTIC. It performs NO new measurements: every number is either an algebraic identity or a re-reading/recomputation over cached arrays from the two dependency experiments. CPU-only, zero OpenRouter calls, $0.00 spend (log a cost line = 0.0 to be explicit). All steps are deterministic except optional bootstrap CIs (fixed seed=0, B=2000, reusing the document-block bootstrap from the dependency code).

  === INPUTS (exact paths & keys) ===
  A) Re-DocRED regime-diagnostic = art_RZC2468yZ-Jh at /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3/ . Canonical per-candidate source: checkpoints/confirmatory/redocred_*.json (each record has fields: title, candidates[], conf_samples[]; each candidate has Z (real score, float in [0,1]), Zt (matched-decoy score), W (knockoff statistic), decoy{head,relation,tail}, decoy_contaminated (bool)). Pre-computed summary: full_method_out.json -> metadata.regime_diagnostic with signal_A_winrate_tail[], signal_B_cdf_match{}, signal_C_wz_divergence{spearman_full=0.93399, spearman_admission=0.99096, admitted_set_jaccard=0.91609, frac_W_equals_Z=0.9391, n_candidates=4384, n_admitted_W_ge_0=4133}, signal_D_calibration{calibration_auc=0.60293}, winrate_tail_headline=0.04471, predicted_regime='GATE REDUNDANT', predicted_wedge_sign='null', regime_axes{rerank_blocked:true}, prediction_vs_realized{prediction_correct:true, realized_any_positive_recall_point:false}, cross_anchor{points[4], winrate_sorted, principle, direction}, thresholds{regime_rho_null=0.97, regime_jaccard_null=0.95, regime_exch_band=0.15, regime_calib_auc_hi=0.65, regime_low_f=0.4, regime_tail_quantiles=[0.25,0.5]}. Helper code to import or re-implement: regime.py (signal_A/B/C/D, classify), analyze.py (knockoff_plus_threshold, make_boot_counts, ratio_ci, conf_frequency), common.py (CONFIG).
  B) CLUTRR self-consistency diagonal = art_sBLQqsdm3EIA at /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/ . Scalars needed (no per-candidate arrays required for this eval): full_method_out.json -> metadata.primary_diagonal_self_consistency.multi_hop.rows[alpha=0.5] (decoy_fdr_hat=0.5, realized_fdr=1.0, n_admitted=12, n_false_admitted=12, ci=[0.661594,1.0], certified=true, self_report_anti_conservative=true); metadata.primary_disconfirmation_verdict{family:'multi_hop', alpha_star:0.5, realized_fdr:1.0, ci:[0.661594,1.0], decoy_fdr_hat:0.5, calibration_disconfirmed:true, self_report_disconfirmed:true, verdict:'DISCONFIRMED'}; metadata.reconciliation_narrative (states cf tail win-rate ~0.48 under self-consistency); and the cross_anchor CLUTRR coordinates already mirrored in (A) (verbalized 0.103/negative, logprob 0.34/negative, self_consistency 0.482/positive). ROBUSTNESS: try full_method_out.json first, then method_out.json, then mini_method_out.json; if a summary key was renamed, recompute from checkpoints rather than failing. Read-only: never mutate dependency files.

  === METRIC GROUP 1 — THE A≡C IDENTITY (the central deliverable) ===
  FORMAL DERIVATION (write into eval_out as a string + machine-checkable case table). W_i = sign(Z_i−Zt_i)·max(Z_i,Zt_i). Cases: (a) Z_i>Zt_i ⇒ sign=+1, max=Z_i ⇒ W_i=Z_i; (b) Z_i<Zt_i ⇒ sign=−1, max=Zt_i ⇒ W_i=−Zt_i ≠ Z_i (scores ≥0); (c) Z_i=Zt_i ⇒ sign=0 ⇒ W_i=0 (≠ Z_i unless Z_i=0). Therefore the per-candidate equality indicator 1[W_i=Z_i] = 1[Z_i>Zt_i] (modulo the measure-zero Z=Zt=0 edge). Signal-A win indicator is 1[Zt_i ≥ Z_i] = 1−1[Z_i>Zt_i] (ties counted as wins). Hence for ANY candidate set S: frac(W==Z | S) + winrate(S) = 1 − frac(Z==Zt | S, Z>0)  i.e. frac(W==Z) = 1 − winrate EXACTLY up to the tie fraction. This proves signal C is an algebraic restatement of signal A, not an independent forecast.
  EMPIRICAL VERIFICATION (compute deterministically from Re-DocRED checkpoints, the canonical source; do NOT trust the summary for this). Load all candidate rows with non-null Z,Zt,W (expect ~4384 over ~152 docs). For each set S in {all, top_25pct, top_50pct (the headline tail), knockoff_alpha0.2-admitted} — using the SAME max(Z,Zt) quantile cutoffs as regime.signal_A and the SAME A.knockoff_plus_threshold at alpha=0.2 — compute and tabulate: (i) winrate(S)=mean(Zt≥Z); (ii) frac_eq(S)=mean(isclose(W,Z,atol=1e-9)); (iii) tie_frac(S)=mean(Z==Zt); (iv) identity_residual(S)=|frac_eq(S) − (1 − winrate(S))|, EXPECT residual ≤ tie_frac(S)+1e-9; (v) indicator_corr(S)=Pearson corr between vectors 1[W==Z] and 1[Zt<Z], EXPECT ≈ +1.0. Headline cross-checks: full-set winrate must equal 1−frac_W_equals_Z = 1−0.9391 = 0.0609 to ~1e-6; top_50pct frac_eq must equal 1−winrate_tail_headline = 1−0.04471 = 0.95529 to ~1e-6. ADMITTED-SET FORCEDNESS: on the gate-admitted set {i: W_i≥0}, show W_i=Z_i for every member with Z_i>Zt_i and W_i=0 for the ties; recompute Spearman(W,Z)|admitted WITH ties (expect = reported 0.99096) and WITHOUT the W=0 tie rows (expect = 1.0 exactly), and recompute admitted_set_jaccard; report n_admitted, n_W_eq_Z, n_ties to EXPLAIN why the reported rho is 0.99096<1 (purely the handful of W=0 contaminated-decoy ties) and conclude admitted-set rho→1 and Jaccard→1 are MECHANICALLY FORCED. Emit a_equals_c_identity{formal_statement, case_table, per_set_table[], max_residual, indicator_corr, admitted_spearman_with_ties, admitted_spearman_without_ties, n_admitted, n_ties, verdict:'CONFIRMED' if max_residual≤max tie_frac+1e-6 and indicator_corr≥0.999}.

  === METRIC GROUP 2 — SIGNAL-DEPENDENCE QUANTIFICATION (effective axis count) ===
  Build the per-candidate signal-input provenance table over Re-DocRED rows: signal A consumes (Z,Zt); signal C consumes W=f(Z,Zt) — i.e. NO new raw data beyond A; signal B compares the decoy distribution {Zt_i} vs low-self-consistency real distribution {Z_i : f_i≤0.4}; signal D consumes (Z_i, f_i) via AUC(Z, 1[f≥0.5]). Compute: (i) corr(a_i,c_i) where a_i=1[Zt≥Z], c_i=1[W==Z] → the headline collinearity, EXPECT ≈1.0 in magnitude (−1 between c and a, +1 between c and 1[Z>Zt]); (ii) a raw-array overlap matrix marking which of {Z, Zt, W, f} each of A/B/C/D reads, making explicit that {A,C} share (Z,Zt) and C adds nothing, while D introduces f as the only genuinely new array; (iii) effective_independent_axes = count of distinct constructs after collapsing A≡C, namely TWO macro-axes (decoy-exchangeability {A=C, with B a distributional refinement of the SAME axis} × base-scorer-calibration {D}), with the explicit note that the diagnostic NOMINALLY advertises 4 signals but the decoy-exchangeability axis is double-counted (A and C) and B lives on that same axis. Emit signal_dependence{corr_a_c, raw_array_overlap_table, axes_after_collapse:2, c_redundant_with_a:true, b_same_axis_as_a:true, note}.

  === METRIC GROUP 3 — REGIME MAP AS HEURISTIC + MISPREDICTION AUDIT ===
  Assemble the 4 anchor points from cached cross_anchor and attach the REALIZED outcome from the source experiments: (P1) Re-DocRED logprob: winrate_tail=0.04471, calibration_auc=0.60293, predicted='GATE REDUNDANT'/'null'; realized='null' (no recall point with delta-CI>0) — but prediction is triggered by rerank_blocked (frac(W==Z)=0.9391≥0.90), i.e. SIGNAL C, which Group 1 proves equals signal A and which (gate keeps+orders the same facts ⇒ null wedge) is a near-RESTATEMENT of the realized null → set near_mechanical:true, independent_correct:false. (P2) CLUTRR self_consistency: winrate_tail=0.482, predicted='GATE ADDS VALUE'/'positive'; realized = DISCONFIRMED from experiment_1 primary_disconfirmation_verdict (realized_fdr=1.0 at alpha*=0.5, CI [0.661594,1.0], decoy_fdr_hat=0.5) → predicted positive but realized anti-conservative/disconfirmed → set mispredict:true (this is the anchor where the MARGINAL win-rate ≈0.5 cannot see the PAIRED sign-flip failure — exactly the headline marginal≠paired lesson, here surfaced as the heuristic's failure). (P3,P4) CLUTRR verbalized 0.103 → 'negative' and CLUTRR logprob 0.34 → 'negative' (hypothesis/iter-2-reported anti-conservative; flag source='hypothesis_reported', realized='anti-conservative (iter-2)', validated_at_paired_standard:false). Heuristic scorecard: count anchors that are BOTH (a) an independent (non-mechanical) prediction AND (b) correct against a realized PAIRED-standard outcome → result = 0 (Re-DocRED correct-but-mechanical; CLUTRR-SC independent-but-WRONG; verb/logprob not validated at the same paired standard). Emit regime_panel{points[4 with winrate_tail, calibration_auc_or_null, predicted_regime, predicted_wedge_sign, realized_outcome, mispredict, near_mechanical, source], mispredict_count:1, near_mechanical_count:1, independent_and_correct_count:0}. demotion_verdict{status:'HEURISTIC (demoted from novel contribution)', reasons:['signal C is algebraically identical to signal A: frac(W==Z)=1−winrate, corr(a,c)≈−1, identity_residual≤tie_frac', 'the one validated anchor (Re-DocRED) prediction is near-mechanical: rerank_blocked via frac(W==Z) restates the realized null', 'the map MISPREDICTS CLUTRR self-consistency (predicted positive from marginal 0.482; realized paired diagonal DISCONFIRMED, realized FDR 1.0)', 'a 4-point 2-anchor illustration, NOT a powered regression; <3 genuinely held-out anchors'], recommend:'present as deployment-time heuristic with stated redundancy; do NOT present W==Z so ranking unchanged as a forecast'}.

  === METRIC GROUP 4 — HONEST REGIME PANEL (figure-ready arrays + FULL caption) ===
  Emit figure_panel with parallel arrays for a single 2-axis scatter: x=[0.04471,0.482,0.103,0.34] (winrate_tail, x-axis label 'marginal decoy win-rate = 1−frac(W==Z) — a MARGINAL statistic; structurally blind to the paired sign-flip'), y=[0.60293, null, null, null] (calibration_auc; for the 3 CLUTRR hypothesis-reported points whose numeric AUC is NOT cached, set y=null and add a per-point note 'AUC not cached — placed on low-calibration band by base_scorer_calibrated=false'; do NOT fabricate a value), labels=['Re-DocRED (logprob)','CLUTRR (self-consistency)','CLUTRR (verbalized)','CLUTRR (logprob)'], predicted_sign=['null','positive','negative','negative'], realized_outcome=['null','DISCONFIRMED (FDR 1.0)','anti-conservative (iter-2)','anti-conservative (iter-2)'], flag=['near_mechanical','MISPREDICT','reported','reported'], exch_band=[0.35,0.65] and calib_hi=0.65 drawn as reference lines. FULL caption (string, paper-ready): state gold-free + zero-API; that x is the marginal win-rate equal to 1−frac(W==Z) so signals A and C are the SAME axis; that the map is a 4-POINT 2-ANCHOR ILLUSTRATION, not a regression; that it MISPREDICTS CLUTRR self-consistency (marginal 0.482 ⇒ predicted 'gate adds value'; the powered paired diagonal DISCONFIRMS, realized FDR 1.0, CI [0.66,1.0]); that its single 'correct' Re-DocRED prediction is near-mechanical because rerank_blocked (frac(W==Z)=0.94) restates the realized null; conclude: HEURISTIC ONLY. Optionally render the panel to figures/regime_panel.jpg via matplotlib (the dependency .venv has matplotlib); if rendering fails, still emit the arrays+caption (figure is optional, arrays are mandatory). reframing_recommendation (one-paragraph string): the paper should LEAD with the marginal-vs-paired conceptual contribution (powered by P1/Artifacts 1–2), present the regime-diagnostic as a deployment-time heuristic with explicitly stated A≡C redundancy, and never present 'W==Z so ranking unchanged' as a forecast.

  === OUTPUT & VALIDATION ===
  Write eval_out.json with top-level keys: metadata{anchor_ids:[art_RZC2468yZ-Jh, art_sBLQqsdm3EIA], input_paths, n_candidates_redocred, n_docs, seed:0, bootstrap_B:2000, llm_cost_usd:0.0, cpu_only:true}, a_equals_c_identity{...}, signal_dependence{...}, regime_panel{...}, demotion_verdict{...}, figure_panel{...}, reframing_recommendation, reproducibility{input_file_sha256[], code_entrypoint:'eval.py'}. Use the aii-json skill to validate against schema exp_gen_sol_out and generate full/mini/preview variants; run the aii-file-size-limit check and split if >100MB (it will be tiny, ~tens of KB). Save the analysis script as eval.py and a one-screen README.md noting zero-API, $0 spend, and that all numbers are derivable from the two cached method_out.json + Re-DocRED checkpoints.

  === FAILURE / ROBUSTNESS HANDLING ===
  (1) Source-of-truth: recompute the identity from checkpoints/confirmatory/*.json candidates[] (raw Z,Zt,W) rather than the summary, so the A≡C verification is INDEPENDENT of the prior regime.py code. (2) Contaminated decoys (decoy_contaminated=true ⇒ Zt≈Z, the 'winners'/W<0 cases): report n_contaminated; recompute the identity and winrate WITH and WITHOUT them; note that contamination INFLATES the apparent win-rate (decoys accidentally entailed score high), so the TRUE marginal exchangeability is even lower — this STRENGTHENS the demotion, never weakens it; surface as a caveat. (3) Exact ties (Z==Zt): count and report tie_frac; carry the tie-correction term in the identity statement; isclose atol=1e-9. (4) Missing/renamed summary keys: fall back full->method->mini, then recompute from checkpoints; the mispredict audit needs only the CLUTRR SCALARS (win-rate ≈0.482 from reconciliation_narrative; realized_fdr=1.0 from primary_disconfirmation_verdict) — NOT per-candidate CLUTRR arrays. (5) If matplotlib/regime.py import fails, re-implement the ~15-line identity + winrate inline (they are trivial) and skip the optional figure. (6) Determinism: no randomness in the primary numbers; any bootstrap uses seed=0. (7) Do not exceed budget: ZERO LLM calls; assert cost==0 before writing output.
metrics_justification: |-
  These metrics are exactly the evidence reviewer novelty-MAJOR and hypothesis claim S4c demand. S4c flags the regime-diagnostic as 'NOVEL but PARTLY TAUTOLOGICAL (signal C == signal A; Re-DocRED prediction near-forced)' and mandates EITHER demote-to-heuristic OR validate predictively on >=3 held-out anchors. Since this artifact runs no new anchors (zero API, $0), the in-scope, correct deliverable is a rigorous, auditable DEMOTION — and these specific metrics earn it.

  (1) The A≡C identity (frac(W==Z)=1−winrate, corr(a,c)≈−1, residual≤tie_frac, admitted-Spearman forced to 1 minus ties) is the load-bearing metric: it converts a hand-wavy 'these signals look correlated' into a PROOF that signal C is an algebraic restatement of signal A, with the residual measured to numerical precision against the canonical checkpoint data. A '4-signal diagnostic' that secretly double-counts the decoy-exchangeability axis overstates its novelty; quantifying the collinearity is precisely what makes the redundancy reviewable rather than asserted. Verifying frac_W_equals_Z=0.9391 against full-set winrate 0.0609 (and the top-50pct tail 0.95529 vs 0.04471) anchors the proof to the actual persisted numbers, not just algebra.

  (2) The signal-dependence / effective-axis count quantifies HOW MUCH of the advertised '4 signals' is real: collapsing A≡C (and noting B lives on the same exchangeability axis) shows the map is really a 2-axis construct (exchangeability × calibration) with one axis duplicated. This is the honest accounting a reviewer needs to judge novelty.

  (3) The mispredict audit is the right metric for a diagnostic that CLAIMS to 'tell you which regime you are in': such a claim must be judged on INDEPENDENT, non-mechanical predictions against realized outcomes. Showing (a) the one validated anchor (Re-DocRED) is predicted by signal C, which equals signal A and mechanically restates the realized null (near_mechanical), and (b) the map MISPREDICTS CLUTRR self-consistency — the single anchor where the marginal/paired distinction bites (marginal win-rate 0.482 ⇒ 'gate adds value', yet the powered paired diagonal is DISCONFIRMED with realized FDR 1.0) — yields independent_and_correct_count = 0. That number is the quantitative justification for demotion, and it directly reinforces the paper's headline: a MARGINAL statistic (win-rate = 1−frac(W==Z)) structurally cannot certify the PAIRED sign-flip property, which is why the heuristic fails exactly where it matters.

  (4) The honest regime panel (arrays + full caption + reframing recommendation) is the deliverable that re-points the paper to LEAD with the marginal-vs-paired conceptual result and present the regime-diagnostic as a heuristic with stated redundancy — satisfying the artifact objective and the goal's reproducibility/commodity-hardware constraint (pure CPU, $0, fully derivable from cached files). Together these metrics turn an over-claimed 'novel predictor' into a correctly-scoped heuristic with auditable, numerical backing, which is the precise scientific correction this iteration requires.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_sBLQqsdm3EIA
type: experiment
title: Self-consistency CLUTRR FDR-gate diagonal with decoy self-report disconfirmation
summary: |-
  Executable per-family realized-FDR-vs-target-alpha CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted CLUTRR kinship facts into a symbolic layer, scored under the diagnostic-VALIDATED K=5 SELF-CONSISTENCY elicitation (iter-2 counterfactual tail win-rate ~0.482). Method + baselines + controls run side-by-side in one pipeline (method.py): METHOD=counterfactual-decoy knockoff+ gate; BASELINE1=PLAIN raw-confidence threshold gate (purely-neural foil); BASELINE2=random in-doc SWAP-decoy knockoff (anti-conservative control); CONTRAST=the same diagonal under VERBALIZED confidence (discreteness/loose-target artifact); CORROBORATION=deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025, r=1). Signed-max W_i + Barber-Candes knockoff+ threshold (eq 1.9), per-document rank-normalization over {reals U cf U swap}, document-block bootstrap CIs (B=2000), Benjamini-Hochberg q=0.05. Reuses iter-2 tested code (fdr_core.py, fdr_stats.py, llm_client.py with a read-only warm-start cache so the 190-doc prefix's scores hit the iter-2 cache; only new docs cost money).

  ITERATION-3 ADDITIONS (reviewer-driven): (A) self-consistency is the headline elicitation for the per-family diagonal; (B) every row surfaces the (target alpha, decoy_fdr_hat, realized FDR) TRIPLE plus a pre-registered SELF-REPORT disconfirmation (the gate's own decoy_fdr_hat is disconfirmed where it is anti-conservative vs realized beyond tau, EVEN when realized<alpha); (C) verbalized contrast on the SAME data with quantified discreteness/loose-target artifact notes; (D) an S1b difficulty LADDER L0..L4 (foreign-swap, in-doc swap, random-vocab, cf_2nd, primary-cf) scored under the SAME self-consistency to repair-or-bound the win-rate diagnostic; (E) foreign-entity entrapment at alpha* and alpha=0.5; (F) full crux match (tail fail-to-reject + full-distribution + tail-only decision-relevance justification); (G) a NEW paired-exchangeability diagnostic (cf win-rate over FALSE pairs) bridging the crux (marginal exchangeability) and the realized diagonal (paired competition); (H) Generator!=Scorer carried forward as SETTLED (ROBUST, no new budget); (I) BH across all validation tests; (J) the single primary-disconfirmation verdict under self-consistency on the populable multi_hop family.

  HEADLINE (this checkpoint, 40-doc smoke; the powered ~593-doc run is the final artifact): on the error-dense multi_hop family (extraction multi-hop accuracy ~0.17 so the family is ~80% genuine FALSE) the self-consistency knockoff+ gate is DISCONFIRMED at the tightest certified alpha* (realized FDR 1.0 with doc-block CI entirely above alpha*=0.5; decoy_fdr_hat=0.5 SELF-REPORT anti-conservative), while the crux is VALID (decoys distributionally exchangeable with genuine errors, distinct from true positives) — distributional exchangeability is NOT paired exchangeability. Generator!=Scorer ROBUST (carried forward). BH over 28 tests. Cost ~$0.07-0.2 (hard cap $10 never neared; exact per-call USD; disk cache for free resumes).

  OUTPUTS for the paper writer: method_out.json (schema exp_gen_sol_out, validated) carries metadata.primary_diagonal_self_consistency (per-family rows with the triple+CI+certified+swap+plain+self_report flag+paired_exchangeability), contrast_diagonal_verbalized (+artifact_notes), power_populability_table, s1b_difficulty_ladder (+verdict), crux_full_and_tail_self_consistency/_verbalized (KS/MW/AD/perm + figure_cdfs + decision-relevance), entrapment (alpha*/0.5), baseline_vs_method_self_consistency, generator_ne_scorer_carried_forward, bh_correction, primary_disconfirmation_verdict, reconciliation_narrative; the per-real examples hold self-consistency/verbalized Z, W_i and per-alpha admission predictions. Companion files: fdr_core.py, fdr_stats.py (unit-tested cores), llm_client.py, summarize.py, make-figures in method.py + figures/, README.md, data.py (regenerates the scaled corpus), pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 2 ---
id: art_RZC2468yZ-Jh
type: experiment
title: Re-DocRED decoy-gating wedge reframed as a gold-free regime-diagnostic
summary: >-
  P3 scales the prior Re-DocRED operational wedge from 36 to the full 152 confirmatory + 36 pilot documents (resume-safe extraction,
  total new spend $1.08 of a $10 cap) and reframes the result as a NOVEL label-free regime-diagnostic. Core comparison (controlled,
  same pipeline): METHOD = a label-free decoy-competition FDR gate (knockoff+ statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i))
  vs the load-bearing PLAIN foil (rank by raw confidence Z_i), with CoT, BM25-RAG and a labeled Mohri-Hashimoto conformal
  back-off (CONF) as reference comparators, all mapped into the identical (title, P-code, head_id, tail_id) triple space by
  one fixed MiniLM-shortlist + temp-0 LLM aligner and scored by the official tuple-matching metric vs human gold. RESULT (pre-registered
  DISCONFIRMATION, scope-honest): at matched recall the wedge collapses to 'thresholding-is-enough' — across a 25-point recall
  grid no point shows a METHOD-over-PLAIN precision gain with document-block-bootstrap (B=2000) CI entirely > 0. The verdict
  embeds the true n and ceiling AT the claim: 'disconfirmed at recall <= 0.075 on 152 docs' (metadata.scope = {n_docs_used:152,
  n_docs_requested:152, recall_ceiling:0.075}); the fairness invariant holds exactly (METHOD and PLAIN share an identical
  candidate+alignment pool -> identical max recall), and the null delta sign persists under P-code-noise / embedding-only-aligner
  / strict-EL perturbations. Four reviewer-MAJOR fixes are implemented: (1) SCOPE honesty as above; (2) COMPARATORS completed-or-dropped
  — the matched-recall grid floor is relaxed to the lowest positive max_recall (0.034) so recall-limited CoT/RAG yield >=1
  evaluable point; all five systems PARTICIPATE (dropped_comparators={}), no all-null baseline is listed; (3) MULTI-HOP comparison
  POWERED, not underpowered — six extra gold-justified Wikidata inverse rules (P22/P25->P40, P361<->P527, P131<->P150) densify
  forward-chained conclusions to n_derived=267 (METHOD)=267 (PLAIN), >> the power_target of 100, delta CI width 0.027, underpowered=false;
  the hallucinated-conclusion rate is ~0.79 for both systems (delta -0.004, CI spans 0) — the gate does not reduce hallucination
  here; (4) the NOVEL label-free REGIME-DIAGNOSTIC (regime.py, ZERO new API calls, NO gold) that PREDICTS the null wedge from
  cached Z/Z~/W/self-consistency via four signals: A tail decoy win-rate (knockoff-admitted tail 0.005 << 0.5 -> decoys too
  easy), B spontaneous-error CDF match (decoy score mean 0.165 vs low-self-consistency real mean 0.857; KS/Mann-Whitney/permutation
  all reject -> too easy), C W-vs-Z ranking divergence (frac(W==Z)=0.94, admitted-set Spearman rho=0.99 -> the gate keeps
  and orders the same facts as the plain threshold -> mechanically null), D base-scorer calibration (AUC(Z, self-consistency)=0.60).
  A 2-axis map (decoy exchangeability x base-scorer calibration) emits predicted_regime='GATE REDUNDANT' and predicted_wedge_sign='null',
  which is then VALIDATED against the realized wedge: prediction_correct=true. A cross-anchor panel places Re-DocRED beside
  P1's CLUTRR regimes (winrate 0.045->null, 0.103/0.34->negative, 0.482->positive) and states+tests the unifying principle
  that gate value is genuinely 2-axis (positive only with exchangeable decoys; at the too-easy end the sign splits by calibration
  into redundant vs anti-conservative), honestly noting it is a 2-anchor illustration, not a powered regression. The artifact
  also emits 8 human-auditable multi-hop proof traces (rule + premises -> conclusion, names resolved) and four paper-ready
  figures (matched-recall wedge, regime map, W-vs-Z signal, decoy diagnostics). All comparisons are RELATIVE-only (Re-DocRED
  residual false negatives depress recall and inflate hallucination for every system equally). Deliverables (schema exp_gen_sol_out,
  all validated): method.py orchestrator + run_analysis; regime.py (the gold-free diagnostic); analyze.py (aligner, official
  metric, knockoff+/conformal operating points, document-block bootstrap, traced forward-chaining); extract.py, prompts.py,
  llm.py, common.py, figures.py, summarize.py; method_out.json (619 KB) with full/mini/preview variants (all < 100 MB, no
  split); figures/. Downstream paper text can quote the disconfirmation precisely and lead with the regime-diagnostic as the
  substantive, novel, interpretable contribution.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — evaluation metrics, agent orchestration patterns, benchmark design
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-16 10:53:21 UTC

```
### Goal

Develop an operational translation pipeline that converts unstructured textual content (e.g., short legal documents, news articles, kids' stories) into a formal first-order logic representation. The output must be capable of (probabilistic) reasoning using a logic reasoner (like Prolog), leveraging LLMs to dynamically resolve terminology, concepts, and relations that are not well defined in the explicit text.

### Reviewer Scope

Limit the technical core to areas the reviewer can deeply evaluate. Other fields are welcome for inspiration but should not host the substantive contribution.

Reviewer-evaluable areas: semantic technologies, logic programming, inductive logic programming, information retrieval, machine learning, LLMs, deep learning, knowledge extraction, knowledge graphs, reasoning, and text data analytics.

The pipeline should ingest a short document (approx. 3000 characters) and parse it into a structured, computable format. Methods may combine an LLM acting as a semantic translation engine (mapping natural text to first-order logic or Prolog predicates), a running logic interpreter (like SWI-Prolog) for symbolic execution, and the integration of upper ontologies like OpenCyc to supply necessary background structure and taxonomic grounding. Furthermore, an LLM should be deployed as a probabilistic reasoning engine to handle fuzzy unifications, semantic similarities, and logical gaps where strict symbolic matching fails due to language ambiguity.

Evaluation must be rigorous and compare the neuro-symbolic pipeline against purely neural baselines (e.g., standard RAG, chain-of-thought prompting) on standard logical reasoning benchmarks (e.g., RuleTaker, CLUTRR) or custom annotated datasets. It must specifically measure:
(i) the precision and recall of atomic fact extraction directly from the original document, and
(ii) the accuracy of multi-hop fact extraction and logical deductions that require synthesizing explicit document facts with implicit common-sense knowledge.

Outputs must provide human-auditable trace-graphs of the reasoning steps to clearly demonstrate the logical path taken.

Constraints: The pipeline must be highly reproducible on any short, professionally written documents. Inference must be executable on commodity hardware, and the system must report a quantified reduction in hallucination rates compared to raw LLM generation.

### Publication

Target ACL Knowledge Extraction track as the primary venue, with EMNLP or specialized neuro-symbolic AI conference tracks (e.g., NeSy) as fallback targets.

### Things to Avoid

Avoid simplistic propositional logic translations of the text. Avoid purely neural black-box systems that lack interpretable reasoning traces. The substantive contribution must be an operational, hybrid method for reasoning with textual content that explicitly minimizes hallucinations.
```

### [3] SKILL-INPUT — aii-python · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-json · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-16 10:53:31 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-06-16 11:11:02 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx5
type: evaluation
title: >-
  Demote the gold-free regime-diagnostic to a heuristic: prove signal C ≡ signal A (frac(W==Z)=1−winrate), quantify signal
  redundancy, and audit the regime map's mispredictions on an honest 4-point panel
summary: >-
  Pure-CPU, ZERO-API evaluation. Reads ONLY the cached gold-free signals already persisted by art_RZC2468yZ-Jh (Re-DocRED
  regime-diagnostic: metadata.regime_diagnostic + checkpoints/confirmatory/*.json per-candidate Z/Zt/W/conf_samples) and art_sBLQqsdm3EIA
  (CLUTRR self-consistency diagonal: metadata.primary_diagonal_self_consistency, metadata.primary_disconfirmation_verdict,
  metadata.reconciliation_narrative). It (1) FORMALLY derives and EMPIRICALLY verifies that signal C (frac(W==Z), admitted-set
  Spearman) is algebraically the SAME quantity as signal A (marginal tail decoy win-rate), so C carries zero new information;
  (2) quantifies how many of the '4 signals' are genuinely independent axes; (3) re-derives the 2-axis regime map AS A HEURISTIC,
  showing it MISPREDICTS the CLUTRR self-consistency anchor (marginal 0.482 → predicted 'gate adds value'; realized paired
  diagonal DISCONFIRMED, realized FDR 1.0) and that its one 'correct' Re-DocRED prediction is near-mechanical; (4) emits eval_out.json
  with the identity verification, the signal-dependence quantification, the demotion verdict, and figure-ready honest regime-panel
  arrays + full captions, plus a one-paragraph reframing recommendation. No LLM calls; spend = $0.00; deterministic.
runpod_compute_profile: cpu_heavy
metrics_descriptions: |-
  OVERVIEW. This EVALUATION resolves reviewer novelty-MAJOR for claim S4c by quantitatively DEMOTING the 'gold-free regime-diagnostic' from a substantive novel contribution to a deployment-time HEURISTIC. It performs NO new measurements: every number is either an algebraic identity or a re-reading/recomputation over cached arrays from the two dependency experiments. CPU-only, zero OpenRouter calls, $0.00 spend (log a cost line = 0.0 to be explicit). All steps are deterministic except optional bootstrap CIs (fixed seed=0, B=2000, reusing the document-block bootstrap from the dependency code).

  === INPUTS (exact paths & keys) ===
  A) Re-DocRED regime-diagnostic = art_RZC2468yZ-Jh at /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3/ . Canonical per-candidate source: checkpoints/confirmatory/redocred_*.json (each record has fields: title, candidates[], conf_samples[]; each candidate has Z (real score, float in [0,1]), Zt (matched-decoy score), W (knockoff statistic), decoy{head,relation,tail}, decoy_contaminated (bool)). Pre-computed summary: full_method_out.json -> metadata.regime_diagnostic with signal_A_winrate_tail[], signal_B_cdf_match{}, signal_C_wz_divergence{spearman_full=0.93399, spearman_admission=0.99096, admitted_set_jaccard=0.91609, frac_W_equals_Z=0.9391, n_candidates=4384, n_admitted_W_ge_0=4133}, signal_D_calibration{calibration_auc=0.60293}, winrate_tail_headline=0.04471, predicted_regime='GATE REDUNDANT', predicted_wedge_sign='null', regime_axes{rerank_blocked:true}, prediction_vs_realized{prediction_correct:true, realized_any_positive_recall_point:false}, cross_anchor{points[4], winrate_sorted, principle, direction}, thresholds{regime_rho_null=0.97, regime_jaccard_null=0.95, regime_exch_band=0.15, regime_calib_auc_hi=0.65, regime_low_f=0.4, regime_tail_quantiles=[0.25,0.5]}. Helper code to import or re-implement: regime.py (signal_A/B/C/D, classify), analyze.py (knockoff_plus_threshold, make_boot_counts, ratio_ci, conf_frequency), common.py (CONFIG).
  B) CLUTRR self-consistency diagonal = art_sBLQqsdm3EIA at /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/ . Scalars needed (no per-candidate arrays required for this eval): full_method_out.json -> metadata.primary_diagonal_self_consistency.multi_hop.rows[alpha=0.5] (decoy_fdr_hat=0.5, realized_fdr=1.0, n_admitted=12, n_false_admitted=12, ci=[0.661594,1.0], certified=true, self_report_anti_conservative=true); metadata.primary_disconfirmation_verdict{family:'multi_hop', alpha_star:0.5, realized_fdr:1.0, ci:[0.661594,1.0], decoy_fdr_hat:0.5, calibration_disconfirmed:true, self_report_disconfirmed:true, verdict:'DISCONFIRMED'}; metadata.reconciliation_narrative (states cf tail win-rate ~0.48 under self-consistency); and the cross_anchor CLUTRR coordinates already mirrored in (A) (verbalized 0.103/negative, logprob 0.34/negative, self_consistency 0.482/positive). ROBUSTNESS: try full_method_out.json first, then method_out.json, then mini_method_out.json; if a summary key was renamed, recompute from checkpoints rather than failing. Read-only: never mutate dependency files.

  === METRIC GROUP 1 — THE A≡C IDENTITY (the central deliverable) ===
  FORMAL DERIVATION (write into eval_out as a string + machine-checkable case table). W_i = sign(Z_i−Zt_i)·max(Z_i,Zt_i). Cases: (a) Z_i>Zt_i ⇒ sign=+1, max=Z_i ⇒ W_i=Z_i; (b) Z_i<Zt_i ⇒ sign=−1, max=Zt_i ⇒ W_i=−Zt_i ≠ Z_i (scores ≥0); (c) Z_i=Zt_i ⇒ sign=0 ⇒ W_i=0 (≠ Z_i unless Z_i=0). Therefore the per-candidate equality indicator 1[W_i=Z_i] = 1[Z_i>Zt_i] (modulo the measure-zero Z=Zt=0 edge). Signal-A win indicator is 1[Zt_i ≥ Z_i] = 1−1[Z_i>Zt_i] (ties counted as wins). Hence for ANY candidate set S: frac(W==Z | S) + winrate(S) = 1 − frac(Z==Zt | S, Z>0)  i.e. frac(W==Z) = 1 − winrate EXACTLY up to the tie fraction. This proves signal C is an algebraic restatement of signal A, not an independent forecast.
  EMPIRICAL VERIFICATION (compute deterministically from Re-DocRED checkpoints, the canonical source; do NOT trust the summary for this). Load all candidate rows with non-null Z,Zt,W (expect ~4384 over ~152 docs). For each set S in {all, top_25pct, top_50pct (the headline tail), knockoff_alpha0.2-admitted} — using the SAME max(Z,Zt) quantile cutoffs as regime.signal_A and the SAME A.knockoff_plus_threshold at alpha=0.2 — compute and tabulate: (i) winrate(S)=mean(Zt≥Z); (ii) frac_eq(S)=mean(isclose(W,Z,atol=1e-9)); (iii) tie_frac(S)=mean(Z==Zt); (iv) identity_residual(S)=|frac_eq(S) − (1 − winrate(S))|, EXPECT residual ≤ tie_frac(S)+1e-9; (v) indicator_corr(S)=Pearson corr between vectors 1[W==Z] and 1[Zt<Z], EXPECT ≈ +1.0. Headline cross-checks: full-set winrate must equal 1−frac_W_equals_Z = 1−0.9391 = 0.0609 to ~1e-6; top_50pct frac_eq must equal 1−winrate_tail_headline = 1−0.04471 = 0.95529 to ~1e-6. ADMITTED-SET FORCEDNESS: on the gate-admitted set {i: W_i≥0}, show W_i=Z_i for every member with Z_i>Zt_i and W_i=0 for the ties; recompute Spearman(W,Z)|admitted WITH ties (expect = reported 0.99096) and WITHOUT the W=0 tie rows (expect = 1.0 exactly), and recompute admitted_set_jaccard; report n_admitted, n_W_eq_Z, n_ties to EXPLAIN why the reported rho is 0.99096<1 (purely the handful of W=0 contaminated-decoy ties) and conclude admitted-set rho→1 and Jaccard→1 are MECHANICALLY FORCED. Emit a_equals_c_identity{formal_statement, case_table, per_set_table[], max_residual, indicator_corr, admitted_spearman_with_ties, admitted_spearman_without_ties, n_admitted, n_ties, verdict:'CONFIRMED' if max_residual≤max tie_frac+1e-6 and indicator_corr≥0.999}.

  === METRIC GROUP 2 — SIGNAL-DEPENDENCE QUANTIFICATION (effective axis count) ===
  Build the per-candidate signal-input provenance table over Re-DocRED rows: signal A consumes (Z,Zt); signal C consumes W=f(Z,Zt) — i.e. NO new raw data beyond A; signal B compares the decoy distribution {Zt_i} vs low-self-consistency real distribution {Z_i : f_i≤0.4}; signal D consumes (Z_i, f_i) via AUC(Z, 1[f≥0.5]). Compute: (i) corr(a_i,c_i) where a_i=1[Zt≥Z], c_i=1[W==Z] → the headline collinearity, EXPECT ≈1.0 in magnitude (−1 between c and a, +1 between c and 1[Z>Zt]); (ii) a raw-array overlap matrix marking which of {Z, Zt, W, f} each of A/B/C/D reads, making explicit that {A,C} share (Z,Zt) and C adds nothing, while D introduces f as the only genuinely new array; (iii) effective_independent_axes = count of distinct constructs after collapsing A≡C, namely TWO macro-axes (decoy-exchangeability {A=C, with B a distributional refinement of the SAME axis} × base-scorer-calibration {D}), with the explicit note that the diagnostic NOMINALLY advertises 4 signals but the decoy-exchangeability axis is double-counted (A and C) and B lives on that same axis. Emit signal_dependence{corr_a_c, raw_array_overlap_table, axes_after_collapse:2, c_redundant_with_a:true, b_same_axis_as_a:true, note}.

  === METRIC GROUP 3 — REGIME MAP AS HEURISTIC + MISPREDICTION AUDIT ===
  Assemble the 4 anchor points from cached cross_anchor and attach the REALIZED outcome from the source experiments: (P1) Re-DocRED logprob: winrate_tail=0.04471, calibration_auc=0.60293, predicted='GATE REDUNDANT'/'null'; realized='null' (no recall point with delta-CI>0) — but prediction is triggered by rerank_blocked (frac(W==Z)=0.9391≥0.90), i.e. SIGNAL C, which Group 1 proves equals signal A and which (gate keeps+orders the same facts ⇒ null wedge) is a near-RESTATEMENT of the realized null → set near_mechanical:true, independent_correct:false. (P2) CLUTRR self_consistency: winrate_tail=0.482, predicted='GATE ADDS VALUE'/'positive'; realized = DISCONFIRMED from experiment_1 primary_disconfirmation_verdict (realized_fdr=1.0 at alpha*=0.5, CI [0.661594,1.0], decoy_fdr_hat=0.5) → predicted positive but realized anti-conservative/disconfirmed → set mispredict:true (this is the anchor where the MARGINAL win-rate ≈0.5 cannot see the PAIRED sign-flip failure — exactly the headline marginal≠paired lesson, here surfaced as the heuristic's failure). (P3,P4) CLUTRR verbalized 0.103 → 'negative' and CLUTRR logprob 0.34 → 'negative' (hypothesis/iter-2-reported anti-conservative; flag source='hypothesis_reported', realized='anti-conservative (iter-2)', validated_at_paired_standard:false). Heuristic scorecard: count anchors that are BOTH (a) an independent (non-mechanical) prediction AND (b) correct against a realized PAIRED-standard outcome → result = 0 (Re-DocRED correct-but-mechanical; CLUTRR-SC independent-but-WRONG; verb/logprob not validated at the same paired standard). Emit regime_panel{points[4 with winrate_tail, calibration_auc_or_null, predicted_regime, predicted_wedge_sign, realized_outcome, mispredict, near_mechanical, source], mispredict_count:1, near_mechanical_count:1, independent_and_correct_count:0}. demotion_verdict{status:'HEURISTIC (demoted from novel contribution)', reasons:['signal C is algebraically identical to signal A: frac(W==Z)=1−winrate, corr(a,c)≈−1, identity_residual≤tie_frac', 'the one validated anchor (Re-DocRED) prediction is near-mechanical: rerank_blocked via frac(W==Z) restates the realized null', 'the map MISPREDICTS CLUTRR self-consistency (predicted positive from marginal 0.482; realized paired diagonal DISCONFIRMED, realized FDR 1.0)', 'a 4-point 2-anchor illustration, NOT a powered regression; <3 genuinely held-out anchors'], recommend:'present as deployment-time heuristic with stated redundancy; do NOT present W==Z so ranking unchanged as a forecast'}.

  === METRIC GROUP 4 — HONEST REGIME PANEL (figure-ready arrays + FULL caption) ===
  Emit figure_panel with parallel arrays for a single 2-axis scatter: x=[0.04471,0.482,0.103,0.34] (winrate_tail, x-axis label 'marginal decoy win-rate = 1−frac(W==Z) — a MARGINAL statistic; structurally blind to the paired sign-flip'), y=[0.60293, null, null, null] (calibration_auc; for the 3 CLUTRR hypothesis-reported points whose numeric AUC is NOT cached, set y=null and add a per-point note 'AUC not cached — placed on low-calibration band by base_scorer_calibrated=false'; do NOT fabricate a value), labels=['Re-DocRED (logprob)','CLUTRR (self-consistency)','CLUTRR (verbalized)','CLUTRR (logprob)'], predicted_sign=['null','positive','negative','negative'], realized_outcome=['null','DISCONFIRMED (FDR 1.0)','anti-conservative (iter-2)','anti-conservative (iter-2)'], flag=['near_mechanical','MISPREDICT','reported','reported'], exch_band=[0.35,0.65] and calib_hi=0.65 drawn as reference lines. FULL caption (string, paper-ready): state gold-free + zero-API; that x is the marginal win-rate equal to 1−frac(W==Z) so signals A and C are the SAME axis; that the map is a 4-POINT 2-ANCHOR ILLUSTRATION, not a regression; that it MISPREDICTS CLUTRR self-consistency (marginal 0.482 ⇒ predicted 'gate adds value'; the powered paired diagonal DISCONFIRMS, realized FDR 1.0, CI [0.66,1.0]); that its single 'correct' Re-DocRED prediction is near-mechanical because rerank_blocked (frac(W==Z)=0.94) restates the realized null; conclude: HEURISTIC ONLY. Optionally render the panel to figures/regime_panel.jpg via matplotlib (the dependency .venv has matplotlib); if rendering fails, still emit the arrays+caption (figure is optional, arrays are mandatory). reframing_recommendation (one-paragraph string): the paper should LEAD with the marginal-vs-paired conceptual contribution (powered by P1/Artifacts 1–2), present the regime-diagnostic as a deployment-time heuristic with explicitly stated A≡C redundancy, and never present 'W==Z so ranking unchanged' as a forecast.

  === OUTPUT & VALIDATION ===
  Write eval_out.json with top-level keys: metadata{anchor_ids:[art_RZC2468yZ-Jh, art_sBLQqsdm3EIA], input_paths, n_candidates_redocred, n_docs, seed:0, bootstrap_B:2000, llm_cost_usd:0.0, cpu_only:true}, a_equals_c_identity{...}, signal_dependence{...}, regime_panel{...}, demotion_verdict{...}, figure_panel{...}, reframing_recommendation, reproducibility{input_file_sha256[], code_entrypoint:'eval.py'}. Use the aii-json skill to validate against schema exp_gen_sol_out and generate full/mini/preview variants; run the aii-file-size-limit check and split if >100MB (it will be tiny, ~tens of KB). Save the analysis script as eval.py and a one-screen README.md noting zero-API, $0 spend, and that all numbers are derivable from the two cached method_out.json + Re-DocRED checkpoints.

  === FAILURE / ROBUSTNESS HANDLING ===
  (1) Source-of-truth: recompute the identity from checkpoints/confirmatory/*.json candidates[] (raw Z,Zt,W) rather than the summary, so the A≡C verification is INDEPENDENT of the prior regime.py code. (2) Contaminated decoys (decoy_contaminated=true ⇒ Zt≈Z, the 'winners'/W<0 cases): report n_contaminated; recompute the identity and winrate WITH and WITHOUT them; note that contamination INFLATES the apparent win-rate (decoys accidentally entailed score high), so the TRUE marginal exchangeability is even lower — this STRENGTHENS the demotion, never weakens it; surface as a caveat. (3) Exact ties (Z==Zt): count and report tie_frac; carry the tie-correction term in the identity statement; isclose atol=1e-9. (4) Missing/renamed summary keys: fall back full->method->mini, then recompute from checkpoints; the mispredict audit needs only the CLUTRR SCALARS (win-rate ≈0.482 from reconciliation_narrative; realized_fdr=1.0 from primary_disconfirmation_verdict) — NOT per-candidate CLUTRR arrays. (5) If matplotlib/regime.py import fails, re-implement the ~15-line identity + winrate inline (they are trivial) and skip the optional figure. (6) Determinism: no randomness in the primary numbers; any bootstrap uses seed=0. (7) Do not exceed budget: ZERO LLM calls; assert cost==0 before writing output.
metrics_justification: |-
  These metrics are exactly the evidence reviewer novelty-MAJOR and hypothesis claim S4c demand. S4c flags the regime-diagnostic as 'NOVEL but PARTLY TAUTOLOGICAL (signal C == signal A; Re-DocRED prediction near-forced)' and mandates EITHER demote-to-heuristic OR validate predictively on >=3 held-out anchors. Since this artifact runs no new anchors (zero API, $0), the in-scope, correct deliverable is a rigorous, auditable DEMOTION — and these specific metrics earn it.

  (1) The A≡C identity (frac(W==Z)=1−winrate, corr(a,c)≈−1, residual≤tie_frac, admitted-Spearman forced to 1 minus ties) is the load-bearing metric: it converts a hand-wavy 'these signals look correlated' into a PROOF that signal C is an algebraic restatement of signal A, with the residual measured to numerical precision against the canonical checkpoint data. A '4-signal diagnostic' that secretly double-counts the decoy-exchangeability axis overstates its novelty; quantifying the collinearity is precisely what makes the redundancy reviewable rather than asserted. Verifying frac_W_equals_Z=0.9391 against full-set winrate 0.0609 (and the top-50pct tail 0.95529 vs 0.04471) anchors the proof to the actual persisted numbers, not just algebra.

  (2) The signal-dependence / effective-axis count quantifies HOW MUCH of the advertised '4 signals' is real: collapsing A≡C (and noting B lives on the same exchangeability axis) shows the map is really a 2-axis construct (exchangeability × calibration) with one axis duplicated. This is the honest accounting a reviewer needs to judge novelty.

  (3) The mispredict audit is the right metric for a diagnostic that CLAIMS to 'tell you which regime you are in': such a claim must be judged on INDEPENDENT, non-mechanical predictions against realized outcomes. Showing (a) the one validated anchor (Re-DocRED) is predicted by signal C, which equals signal A and mechanically restates the realized null (near_mechanical), and (b) the map MISPREDICTS CLUTRR self-consistency — the single anchor where the marginal/paired distinction bites (marginal win-rate 0.482 ⇒ 'gate adds value', yet the powered paired diagonal is DISCONFIRMED with realized FDR 1.0) — yields independent_and_correct_count = 0. That number is the quantitative justification for demotion, and it directly reinforces the paper's headline: a MARGINAL statistic (win-rate = 1−frac(W==Z)) structurally cannot certify the PAIRED sign-flip property, which is why the heuristic fails exactly where it matters.

  (4) The honest regime panel (arrays + full caption + reframing recommendation) is the deliverable that re-points the paper to LEAD with the marginal-vs-paired conceptual result and present the regime-diagnostic as a heuristic with stated redundancy — satisfying the artifact objective and the goal's reproducibility/commodity-hardware constraint (pure CPU, $0, fully derivable from cached files). Together these metrics turn an over-claimed 'novel predictor' into a correctly-scoped heuristic with auditable, numerical backing, which is the precise scientific correction this iteration requires.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_sBLQqsdm3EIA
type: experiment
title: Self-consistency CLUTRR FDR-gate diagonal with decoy self-report disconfirmation
summary: |-
  Executable per-family realized-FDR-vs-target-alpha CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted CLUTRR kinship facts into a symbolic layer, scored under the diagnostic-VALIDATED K=5 SELF-CONSISTENCY elicitation (iter-2 counterfactual tail win-rate ~0.482). Method + baselines + controls run side-by-side in one pipeline (method.py): METHOD=counterfactual-decoy knockoff+ gate; BASELINE1=PLAIN raw-confidence threshold gate (purely-neural foil); BASELINE2=random in-doc SWAP-decoy knockoff (anti-conservative control); CONTRAST=the same diagonal under VERBALIZED confidence (discreteness/loose-target artifact); CORROBORATION=deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025, r=1). Signed-max W_i + Barber-Candes knockoff+ threshold (eq 1.9), per-document rank-normalization over {reals U cf U swap}, document-block bootstrap CIs (B=2000), Benjamini-Hochberg q=0.05. Reuses iter-2 tested code (fdr_core.py, fdr_stats.py, llm_client.py with a read-only warm-start cache so the 190-doc prefix's scores hit the iter-2 cache; only new docs cost money).

  ITERATION-3 ADDITIONS (reviewer-driven): (A) self-consistency is the headline elicitation for the per-family diagonal; (B) every row surfaces the (target alpha, decoy_fdr_hat, realized FDR) TRIPLE plus a pre-registered SELF-REPORT disconfirmation (the gate's own decoy_fdr_hat is disconfirmed where it is anti-conservative vs realized beyond tau, EVEN when realized<alpha); (C) verbalized contrast on the SAME data with quantified discreteness/loose-target artifact notes; (D) an S1b difficulty LADDER L0..L4 (foreign-swap, in-doc swap, random-vocab, cf_2nd, primary-cf) scored under the SAME self-consistency to repair-or-bound the win-rate diagnostic; (E) foreign-entity entrapment at alpha* and alpha=0.5; (F) full crux match (tail fail-to-reject + full-distribution + tail-only decision-relevance justification); (G) a NEW paired-exchangeability diagnostic (cf win-rate over FALSE pairs) bridging the crux (marginal exchangeability) and the realized diagonal (paired competition); (H) Generator!=Scorer carried forward as SETTLED (ROBUST, no new budget); (I) BH across all validation tests; (J) the single primary-disconfirmation verdict under self-consistency on the populable multi_hop family.

  HEADLINE (this checkpoint, 40-doc smoke; the powered ~593-doc run is the final artifact): on the error-dense multi_hop family (extraction multi-hop accuracy ~0.17 so the family is ~80% genuine FALSE) the self-consistency knockoff+ gate is DISCONFIRMED at the tightest certified alpha* (realized FDR 1.0 with doc-block CI entirely above alpha*=0.5; decoy_fdr_hat=0.5 SELF-REPORT anti-conservative), while the crux is VALID (decoys distributionally exchangeable with genuine errors, distinct from true positives) — distributional exchangeability is NOT paired exchangeability. Generator!=Scorer ROBUST (carried forward). BH over 28 tests. Cost ~$0.07-0.2 (hard cap $10 never neared; exact per-call USD; disk cache for free resumes).

  OUTPUTS for the paper writer: method_out.json (schema exp_gen_sol_out, validated) carries metadata.primary_diagonal_self_consistency (per-family rows with the triple+CI+certified+swap+plain+self_report flag+paired_exchangeability), contrast_diagonal_verbalized (+artifact_notes), power_populability_table, s1b_difficulty_ladder (+verdict), crux_full_and_tail_self_consistency/_verbalized (KS/MW/AD/perm + figure_cdfs + decision-relevance), entrapment (alpha*/0.5), baseline_vs_method_self_consistency, generator_ne_scorer_carried_forward, bh_correction, primary_disconfirmation_verdict, reconciliation_narrative; the per-real examples hold self-consistency/verbalized Z, W_i and per-alpha admission predictions. Companion files: fdr_core.py, fdr_stats.py (unit-tested cores), llm_client.py, summarize.py, make-figures in method.py + figures/, README.md, data.py (regenerates the scaled corpus), pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 2 ---
id: art_RZC2468yZ-Jh
type: experiment
title: Re-DocRED decoy-gating wedge reframed as a gold-free regime-diagnostic
summary: >-
  P3 scales the prior Re-DocRED operational wedge from 36 to the full 152 confirmatory + 36 pilot documents (resume-safe extraction,
  total new spend $1.08 of a $10 cap) and reframes the result as a NOVEL label-free regime-diagnostic. Core comparison (controlled,
  same pipeline): METHOD = a label-free decoy-competition FDR gate (knockoff+ statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i))
  vs the load-bearing PLAIN foil (rank by raw confidence Z_i), with CoT, BM25-RAG and a labeled Mohri-Hashimoto conformal
  back-off (CONF) as reference comparators, all mapped into the identical (title, P-code, head_id, tail_id) triple space by
  one fixed MiniLM-shortlist + temp-0 LLM aligner and scored by the official tuple-matching metric vs human gold. RESULT (pre-registered
  DISCONFIRMATION, scope-honest): at matched recall the wedge collapses to 'thresholding-is-enough' — across a 25-point recall
  grid no point shows a METHOD-over-PLAIN precision gain with document-block-bootstrap (B=2000) CI entirely > 0. The verdict
  embeds the true n and ceiling AT the claim: 'disconfirmed at recall <= 0.075 on 152 docs' (metadata.scope = {n_docs_used:152,
  n_docs_requested:152, recall_ceiling:0.075}); the fairness invariant holds exactly (METHOD and PLAIN share an identical
  candidate+alignment pool -> identical max recall), and the null delta sign persists under P-code-noise / embedding-only-aligner
  / strict-EL perturbations. Four reviewer-MAJOR fixes are implemented: (1) SCOPE honesty as above; (2) COMPARATORS completed-or-dropped
  — the matched-recall grid floor is relaxed to the lowest positive max_recall (0.034) so recall-limited CoT/RAG yield >=1
  evaluable point; all five systems PARTICIPATE (dropped_comparators={}), no all-null baseline is listed; (3) MULTI-HOP comparison
  POWERED, not underpowered — six extra gold-justified Wikidata inverse rules (P22/P25->P40, P361<->P527, P131<->P150) densify
  forward-chained conclusions to n_derived=267 (METHOD)=267 (PLAIN), >> the power_target of 100, delta CI width 0.027, underpowered=false;
  the hallucinated-conclusion rate is ~0.79 for both systems (delta -0.004, CI spans 0) — the gate does not reduce hallucination
  here; (4) the NOVEL label-free REGIME-DIAGNOSTIC (regime.py, ZERO new API calls, NO gold) that PREDICTS the null wedge from
  cached Z/Z~/W/self-consistency via four signals: A tail decoy win-rate (knockoff-admitted tail 0.005 << 0.5 -> decoys too
  easy), B spontaneous-error CDF match (decoy score mean 0.165 vs low-self-consistency real mean 0.857; KS/Mann-Whitney/permutation
  all reject -> too easy), C W-vs-Z ranking divergence (frac(W==Z)=0.94, admitted-set Spearman rho=0.99 -> the gate keeps
  and orders the same facts as the plain threshold -> mechanically null), D base-scorer calibration (AUC(Z, self-consistency)=0.60).
  A 2-axis map (decoy exchangeability x base-scorer calibration) emits predicted_regime='GATE REDUNDANT' and predicted_wedge_sign='null',
  which is then VALIDATED against the realized wedge: prediction_correct=true. A cross-anchor panel places Re-DocRED beside
  P1's CLUTRR regimes (winrate 0.045->null, 0.103/0.34->negative, 0.482->positive) and states+tests the unifying principle
  that gate value is genuinely 2-axis (positive only with exchangeable decoys; at the too-easy end the sign splits by calibration
  into redundant vs anti-conservative), honestly noting it is a 2-anchor illustration, not a powered regression. The artifact
  also emits 8 human-auditable multi-hop proof traces (rule + premises -> conclusion, names resolved) and four paper-ready
  figures (matched-recall wedge, regime map, W-vs-Z signal, decoy diagnostics). All comparisons are RELATIVE-only (Re-DocRED
  residual false negatives depress recall and inflate hallucination for every system equally). Deliverables (schema exp_gen_sol_out,
  all validated): method.py orchestrator + run_analysis; regime.py (the gold-free diagnostic); analyze.py (aligner, official
  metric, knockoff+/conformal operating points, document-block bootstrap, traced forward-chaining); extract.py, prompts.py,
  llm.py, common.py, figures.py, summarize.py; method_out.json (619 KB) with full/mini/preview variants (all < 100 MB, no
  split); figures/. Downstream paper text can quote the disconfirmation precisely and lead with the regime-diagnostic as the
  substantive, novel, interpretable contribution.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — evaluation metrics, agent orchestration patterns, benchmark design
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input eval_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to eval_out.json and full_eval_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "EvaluationExpectedFiles": {
      "description": "All expected output files from evaluation artifact.",
      "properties": {
        "script": {
          "description": "Path to eval.py script. Example: 'eval.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full evaluation JSON file. Example: 'full_eval_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini evaluation JSON file. Example: 'mini_eval_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview evaluation JSON file. Example: 'preview_eval_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "EvaluationExpectedFiles",
      "type": "object"
    }
  },
  "description": "Evaluation artifact \u2014 structured output + file metadata.\n\nEvaluates both proposed and baseline methods with appropriate metrics.\nProduces eval.py and eval_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/EvaluationExpectedFiles",
      "description": "All output files you created. Must include eval.py script plus full/mini/preview evaluation JSON files."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "EvaluationArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
