# gen_art_experiment_3 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_3` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 10:53:27 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx4
type: experiment
title: >-
  P4+P2-framing: Minimal ProbLog probabilistic reasoner on the 24-doc anchor + honest finalized application reporting (corruption
  CIs, directional atomic reduction, conservative self-report)
summary: >-
  Reanalysis-plus-ProbLog experiment that REUSES the already-executed iter-3 P2 pipeline (method.py + kb_engine.py + typing_sumo.py
  + fdr_stats.py + llm_client.py + cached scores, all in iter_3/gen_art/gen_art_experiment_2) on the EXISTING 24-doc legal/news/regulatory
  anchor (art_UBTwyePql8NQ). Two deliverables: (P4) execute the goal-hard-required LLM-as-probabilistic-reasoner by swapping
  the deterministic backward-chaining query for a minimal ProbLog get_evaluatable().create_from(PrologString).evaluate() run
  with the certificate->weight mapping (gate-consistent shrinkage (1-alpha_hat)*calibrate(Z_i) default; per-pair W_i-margin
  alternative), emitting probabilistic trace-graphs (marginals per node + per-leaf provenance/decoy/entrapment certificates)
  on >=1 doc/genre, with a pure-Python exact weighted-model-counting fallback that reproduces ProbLog marginals if ProbLog
  cannot install; (P2-framing) recompute the multi-hop corruption result WITH document-block bootstrap CIs + an explicit single-genre
  (regulatory) origin flag and per-system derived-conclusion counts, report the pooled atomic hallucinated-fact reduction
  across BOTH elicitations x ALL alpha with CIs and state PLAINLY it is DIRECTIONAL/not CI-separated at n=24, and carry the
  CONSERVATIVE self-report finding (decoy_fdr_hat>=realized everywhere, contrasting CLUTRR). Deterministic backward-chaining
  stays the required baseline so no headline number depends on ProbLog. Emit figure-ready arrays + full captions; method_out.json
  schema-valid; log cumulative LLM cost after every call (this is ~$0 cache-hit reanalysis); soft cap ~$1, HARD STOP $10.
  CPU-only.
runpod_compute_profile: gpu
implementation_pseudocode: |
  ########################################################################
  # CONTEXT (read first). This artifact is LARGELY A REANALYSIS + a small
  # ProbLog run on ALREADY-CACHED LLM scores. Do NOT re-extract / re-score from
  # scratch. Reuse the iter-3 P2 execution verbatim and add the probabilistic
  # layer + honest finalized reporting on top.
  #
  # SOURCE OF TRUTH (read these files, copy them into THIS workspace):
  #   SRC = /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2
  #   Reuse:  method.py, kb_engine.py, typing_sumo.py, fdr_stats.py, llm_client.py,
  #           pyproject.toml, and the WHOLE cache/ directory (sha256-keyed LLM cache).
  #   Dataset (UNCHANGED 24-doc anchor, art_UBTwyePql8NQ):
  #     DEP_DATA = .../iter_2/gen_art/gen_art_dataset_1/full_data_out.json (+ mini_data_out.json)
  #   ProbLog spec: .../iter_2/gen_art/gen_art_research_1/research_out.json + research_report.md
  #                 (Part C: API, C.2 certificate->weight table, C.3 trace-graph, C.5 upgrade swap)
  #   The expanded anchor from Artifact-3 is NOT consumed here (it runs in parallel,
  #   consumed next iteration). Use ONLY the existing 24 docs.
  #
  # KEY FACTS ABOUT THE REUSED CODE (already verified):
  #  - kb_engine.KB: pure-Python backward-chaining. Fact=(pred,(args...))->cert dict.
  #    Rule=(name, head_pred, head_args tuple of V('X'), body list of (pred,args)).
  #    Uses explicit Var class (V('A')) -- NOT capitalization. derive_all(max_depth=4)
  #    returns proof dicts {type:derived/leaf, atom:[pred,[args]], rule, children/cert}.
  #    proof_to_graph -> {nodes,edges}; graph_to_dot -> DOT string. iter_leaves walks leaves.
  #    Each leaf cert = {provenance, provenance_char_span, hallucination_verdict,
  #       decoy_certificate:{W_i,T,alpha}, entrapment_certificate:{FDP_hat,r}}.
  #  - method.py constants: SEED=20240617, ALPHA_GRID=[0.05,0.10,0.20,0.30,0.50],
  #    B_BOOT=2000, K_SC=5, R_ENTRAP=1, GENRES=[legal,news,regulatory],
  #    PRIMARY_MODEL=openai/gpt-4.1-nano (logprob+portable/self-consistency),
  #    CROSS_MODEL=mistralai/ministral-8b-2512. Two elicitations: 'portable'(=K=5
  #    self-consistency, the 0.183 headline) and 'logprob'(0.178). raw baseline=0.243.
  #  - method.py already has: gate_and_hall_grid (per genre x elic x alpha: gate vs raw
  #    rate + raw_ci/gate_ci doc-block bootstrap + decoy_fdr_hat + entrapment FDP_hat),
  #    build_kb, derive_doc, multihop_corruption (RAW-KB vs GATE-KB derived/corrupt counts,
  #    NO CIs yet), export_trace_graphs (deterministic), W_cf_of (knockoff W_i for a real),
  #    rank_normalize_elic / headline_norm (per-doc rank-normalized real score Z_i),
  #    build_output (assembles method_out.json), selftest().
  #  - fdr_stats (st): doc_block_bootstrap(units, stat_fn, B, seed), knockoff_plus_threshold
  #    (returns threshold T + estimated_ratio == decoy_fdr_hat), BH, etc.
  #  - llm_client.OpenRouterClient: disk cache keyed sha256(payload+sample_idx), exact
  #    usage.cost, $10 hard-stop. Re-running same 24 docs @ same SEED = 100% cache hits = $0.
  ########################################################################

  # ----------------------------------------------------------------------
  # PHASE 0 -- WORKSPACE BOOTSTRAP (no LLM calls, ~minutes)
  # ----------------------------------------------------------------------
  0.1  Copy SRC/{method.py,kb_engine.py,typing_sumo.py,fdr_stats.py,llm_client.py,
       pyproject.toml} and SRC/cache/ into THIS workspace. Keep DEP_DATA absolute path.
  0.2  `uv sync`; then add the probabilistic-reasoning dep:
          `uv add problog`   (pure-Python; default compiler tries PySDD/d-DNNF backends)
       Also ensure networkx + matplotlib present (already in pyproject for rendering).
  0.3  Set env: PYTHONHASHSEED=0. Run the inherited `uv run method.py --selftest` FIRST
       to confirm the ported pipeline + kb_engine + fdr_stats selftests still PASS in this
       workspace (this re-validates the reused code before extending it).
  0.4  Quick cache-warmth check: run a MINI pass (mini_data_out.json, 12 docs) end-to-end
       reading from the copied cache/; confirm cumulative cost stays ~$0 (cache hits). If
       any miss appears, it is only for docs/prompts not previously scored -- log the cost,
       it must stay << $1. This proves we are reanalyzing, not re-scoring.

  # ----------------------------------------------------------------------
  # PHASE 1 -- PROBABILISTIC REASONER (P4): new module prob_reasoner.py
  # ----------------------------------------------------------------------
  # Goal: a minimal but REAL ProbLog run that turns admitted facts/bridges into a
  # weighted program, computes multi-hop conclusion MARGINALS, and exports probabilistic
  # trace-graphs. Deterministic kb_engine REMAINS the baseline (no headline depends on this).

  1.1  calibrate(Z_i) -> p_i in (0,1):
         Z_i = the per-doc RANK-NORMALIZED real score from headline_norm (already in [0,1];
           reuse the exact access path that W_cf_of uses to fetch the real's normalized score).
         DEFAULT calibrate = identity clamp: p_i = clip(Z_i, eps, 1-eps), eps=1e-3 (monotone,
           no labels needed -> keeps the method label-free, consistent with the gate).
         OPTIONAL sensitivity (report, do NOT headline): Platt/isotonic fit Z_i->P(entailed)
           on the gold hall_adj labels of the anchor reals; FLAG explicit overfit risk at n=24.

  1.2  Per-pair / FDR weights (the C.2 mapping table):
         alpha_hat = decoy_fdr_hat of the OPERATIVE gate cell for that (genre,elic) at the
           headline alpha (alpha*=0.5, the only certified one on 24 docs).
         (i) DEFAULT gate-consistent shrinkage:  w_i = (1 - alpha_hat) * p_i
         (ii) ALTERNATIVE per-pair margin:       w_i = clip(0.5 + 0.5*W_i_rank, eps, 1-eps)
              where W_i_rank = rank-normalized knockoff margin (W_cf_of). Report BOTH on the
              SAME proofs as a sensitivity row; headline marginals use (i).
         entrapment FDP_hat carried at the leaf as a consistency prior (annotation only, not
           folded into w_i for the headline -- keep it auditable and separable).

  1.3  KB -> ProbLog program string (handle the Prolog-atom gotcha CAREFULLY):
         sanitize(name): make a valid Prolog atom. Relations/predicate functors -> slug:
           lowercase, [^a-z0-9_]->'_', prefix 'p_' if starts non-alpha. Entity CONSTANTS ->
           single-quoted atoms: "Art13"->'Art13', "ACME Corp"->'ACME Corp' (escape inner quotes).
           Keep a bidirectional map {prolog_term <-> original} to map results back.
         For each admitted fact f with weight w_i:  emit  `<w_i>::<rel>(<h_atom>,<t_atom>).`
         For each genre BRIDGE_RULE (deterministic, weight 1): emit a Prolog rule
           `<head>(A,R) :- <b1>(A,B), <b2>(B,R).`  (V('A')->A etc.; vars are uppercase -> valid).
         For each DERIVED conclusion produced by kb.derive_all (the deterministic baseline
           already gives us exactly which conclusions exist), emit `query(<conclusion>).`
         NOTE: ProbLog computes ALL queries in one evaluate() call.

  1.4  Run ProbLog (the exact swap per spec C.5):
         from problog.program import PrologString
         from problog import get_evaluatable
         marginals = get_evaluatable().create_from(PrologString(prog)).evaluate() # {Term:prob}
         Map each Term back to (pred,args) via the bidirectional map -> conclusion_marginal.
         For a 2-hop single-proof bridge this yields p_leaf1*p_leaf2; multiple proofs -> the
         correct noisy-OR / WMC (ProbLog handles shared leaves exactly).

  1.5  Probabilistic trace-graph export (extend kb_engine, do NOT mutate the baseline):
         Reuse proof_to_graph -> add a 'prob' attribute to every node:
           leaf node prob = its calibrated weight w_i; derived/root node prob = the ProbLog
           marginal of that sub-conclusion (query each intermediate derived head too; for the
           non-recursive 2-hop bridges the only derived node is the root). Keep every leaf's
           full certificate (provenance + decoy{W_i,T,alpha} + entrapment{FDP_hat,r} + w_i).
         Extend graph_to_dot -> annotate each node label with its marginal/weight; add a
           second JSON dump prob_trace_<doc_id>.json carrying {graph_with_prob, program, marginals,
           mapping, engine:'problog'|'fallback'}. DOT path too.
         Export >=1 doc PER GENRE:
           regulatory -> a real multi-hop bridge proof (cross_references+grants_right) with a
             genuine multi-hop MARGINAL (this is the showcase; regulatory is the only genre that
             derives multi-hop conclusions).
           legal & news -> bridges rarely/never fire (news derives 0 multi-hop). Use the existing
             depth-1 _admission_trace: a single admitted fact with marginal = its w_i. This STILL
             demonstrates the probabilistic layer (LLM-supplied calibrated unification weight at a
             leaf). State this honestly in the output: the multi-hop probabilistic marginal is
             demonstrated on regulatory; legal/news show single-fact probabilistic admissions.

  1.6  Sensitivity table: for the regulatory multi-hop conclusions, report marginal under
       (i) gate-consistent shrinkage vs (ii) per-pair margin weight vs (default identity p_i
       with alpha_hat=0, i.e. no shrinkage) -- a 3-row table showing how the FDR certificate
       shifts the truth mass. This directly answers the spec's open 'how sensitive are multi-hop
       marginals to shrinkage vs margin weighting' question.

  # ----------------------------------------------------------------------
  # PHASE 2 -- FINALIZE HONEST APPLICATION REPORTING (P2-framing; NO new LLM calls)
  # ----------------------------------------------------------------------
  2.1  MULTI-HOP CORRUPTION WITH CIs + single-genre flag. Extend multihop_corruption:
         Bootstrap unit = the DOCUMENT. For RAW-KB and for GATE-KB(alpha=0.5):
           build per-doc lists of corrupt-flags over that doc's derived conclusions; resample
           DOCS with st.doc_block_bootstrap(B=B_BOOT, seed=SEED) and recompute corrupted_rate
           for raw, gate, and the DELTA (raw-gate). Report point + 95% CI for each.
         Add fields: per-genre {derived, corrupt, corrupted_rate} for raw & gate (this surfaces
           legal corrupted_rate already 0.0, news derived==0, regulatory 12->3); a top-level
           flag single_genre_origin='regulatory' with a one-line note that the pooled
           0.48->0.18 drop is ENTIRELY regulatory-driven (legal clean, news derives nothing);
           report per-system derived-conclusion COUNTS (e.g. raw ~23 vs gate ~11). State that
           with one contributing genre and ~11-23 conclusions the CI is WIDE and the drop is a
           DIRECTIONAL trend, not a significant reduction.
  2.2  POOLED ATOMIC HALLUCINATED-FACT REDUCTION across genres, BOTH elicitations x ALL alpha:
         For each (elic in {portable, logprob}, alpha in ALPHA_GRID): pool reals across all 3
           genres; compute pooled raw rate and pooled gate rate (admitted reals at that cell's T);
           doc-block bootstrap the DIFFERENCE (raw_rate - gate_rate) resampling docs across genres
           -> 95% CI on the reduction. cells_ci_separated = count of cells whose diff-CI excludes 0
           (EXPECT 0/40 -- confirm and REPORT the count). Headline numbers: portable gate 0.183 /
           logprob 0.178 vs raw 0.243 (~25% rel). STATE PLAINLY at the point of claim:
           'DIRECTIONAL, not CI-separated at n=24 (0/40 cells); demonstrated as a trend with
           auditable provenance.'  Keep the existing per-cell raw_ci/gate_ci too.
  2.3  CONSERVATIVE SELF-REPORT finding. For every (genre,elic,alpha) cell compute realized FDR
         (vs gold hall_adj) and compare to the gate's decoy_fdr_hat. anti_conservative_cells =
         count where decoy_fdr_hat < realized - tau (tau=0.05); EXPECT 0/40. Emit
         self_report_regime='conservative' with the explicit contrast: 'decoy_fdr_hat >= realized
         in all 40 cells here (gate UNDER-admits / over-estimates falsity), the OPPOSITE of the
         CLUTRR multi_hop anti-conservative regime (decoy_fdr_hat=0.5 < realized 1.0)'. Provide the
         (alpha, decoy_fdr_hat, realized) triples per cell for the figure.

  # ----------------------------------------------------------------------
  # PHASE 3 -- FIGURES (arrays + captions) + OUTPUT (NO new LLM calls)
  # ----------------------------------------------------------------------
  3.1  Emit figure-ready arrays under method_out.json['figures'] AND render PNGs via a small
       build_figures.py (matplotlib for bars/scatter; networkx+matplotlib for the graph, since
       there is NO system `dot` binary in this env -- do NOT shell out to graphviz). Figures:
         F1 pooled atomic hallucination raw vs gate across alpha, both elicitations, CI bars.
            CAPTION must state: doc-block bootstrap (B=2000), n=24 docs, 0/40 CI-separated cells,
            DIRECTIONAL trend; 1/k admission floor {20,10,5,4,2} for alpha {.05,.10,.20,.30,.50}.
         F2 multi-hop corruption RAW-KB vs GATE-KB(a=0.5) with CIs + per-genre stacked bars
            annotating that regulatory is the SOLE contributor (legal=0, news derives 0).
            CAPTION: derived-conclusion counts, single-genre origin, wide CI.
         F3 decoy_fdr_hat vs realized FDR scatter with y=x line, all 40 cells above the line
            (conservative regime), contrasted against the CLUTRR anti-conservative point.
            CAPTION: conservative self-report, contrast with CLUTRR.
         F4 a probabilistic trace-graph (regulatory multi-hop) rendered with node marginals +
            per-leaf certificate annotations. CAPTION: ProbLog (or fallback) marginal, gate-
            consistent shrinkage weights, per-leaf provenance+decoy+entrapment certificates.
       EVERY caption carries: bootstrap method+B, n, regime tag, and (where relevant) the 1/k floor.
  3.2  Assemble method_out.json by EXTENDING build_output. ADD top-level keys:
         'probabilistic_reasoning': {engine:'problog'|'fallback', mapping_default:'gate_consistent_shrinkage',
             per_doc_marginals:[...], sensitivity_shrinkage_vs_margin:[...], genres_with_multihop:['regulatory'],
             note:'deterministic backward-chaining remains the baseline; no headline number depends on ProbLog'},
         'prob_trace_graphs': {n_exported, examples:[{doc_id,genre,engine,conclusion,marginal,json_path,dot_path}]},
         updated 'multihop_corruption' (with CIs + per-genre counts + single_genre_origin),
         'atomic_reduction_pooled' (per elic x alpha: raw,gate,diff,diff_ci,cells_ci_separated,directional:true),
         'self_report_regime':'conservative' (+ per-cell triples + anti_conservative_cells:0),
         'figures' (arrays + captions), and a 'contributions' note that the probabilistic reasoner
         is DELIVERED (not only specified) so the abstract/intro never overclaim or underclaim.
       Keep ALL prior keys. Re-run the schema validation the prior run used (aii-json) against the
       SAME method_out schema; generate mini_/preview_ variants. Confirm schema-valid.
  3.3  Cost: append cumulative LLM cost to logs/cost.jsonl after EVERY call (there should be ~0
       new calls). Print final cumulative cost. Assert < SOFT_CAP (~$1); HARD STOP at $10.

  # ----------------------------------------------------------------------
  # RUN DISCIPLINE
  # ----------------------------------------------------------------------
  # Launch the full run as a DIRECTLY-tracked background python (NO trailing `&` inside a
  # background Bash -> avoids the orphan-double-write gotcha). Use timeout + PID:
  #   `uv run method.py --full & PID=$!` then poll `kill -0 $PID`. Stop strays by PID only
  #   (other runs share method.py -- NEVER pkill/grep-by-name). Total wall time ~minutes
  #   (reanalysis on cached scores + tiny ProbLog grounding).
fallback_plan: |-
  PROBLOG INSTALL/RUN FAILURE (the most likely risk -- ProbLog's knowledge-compilation backend PySDD/d-DNNF can fail to build on a minimal CPU image): fall back to a PURE-PYTHON EXACT weighted-model-counting (WMC) evaluator in prob_reasoner.py that REPRODUCES ProbLog marginals on these tiny proof DAGs. Algorithm: collect the DISTINCT grounded leaf facts in the doc's KB (each an independent Bernoulli with prob = its calibrated weight w_i). If #distinct_leaves <= 18: enumerate all 2^n truth assignments; for each, build a sub-KB containing only the 'present' facts, run the existing deterministic kb.derive_all, test whether the queried conclusion is derivable, and accumulate the assignment's probability (product of w_i for present, (1-w_i) for absent) into the marginal when derivable. This is EXACT WMC for independent facts + deterministic rules -> identical to ProbLog. If #distinct_leaves > 18: fall back to noisy-OR over the enumerated proofs (marginal = 1 - prod_over_proofs(1 - prod_over_leaves(w_i))) and FLAG it as an approximation in the output. Report engine='fallback' and state explicitly it is a 'faithful ProbLog-equivalent exact WMC' -- so the probabilistic layer is DEMONSTRATED either way and the CONTRIBUTIONS (not only limitations) can claim the reasoner is delivered. VALIDATION: add a selftest asserting fallback marginal == ProbLog marginal within 1e-9 on the toy 2-hop KB whenever ProbLog IS available; if ProbLog absent, assert the fallback's toy 2-hop marginal == p1*p2 analytically.

  NO MULTI-HOP CONCLUSIONS DERIVE ON ANY GENRE (bridges never fire because admitted facts don't chain): then the multi-hop probabilistic marginal cannot be shown on a real bridge. Fallback: (a) still demonstrate the probabilistic layer via depth-1 admission traces (single fact -> marginal = w_i) on all 3 genres -- the calibrated-weight-at-the-leaf is the minimal probabilistic-reasoner demonstration; (b) ADDITIONALLY construct ONE synthetic-but-faithful 2-hop query by chaining two genuinely-admitted regulatory facts that share an entity (cross_references(A,B) + grants_right(B,R)) even if the deterministic engine's _degenerate filter dropped it, clearly labeled as an illustrative multi-hop marginal over admitted (certified) leaves. Document honestly. (We already know from iter-3 that regulatory DOES derive ~12 multi-hop conclusions, so this is a safety net only.)

  PROLOG-ATOM ERRORS (entity strings with spaces/quotes/leading digits crash PrologString parsing): the sanitize() layer single-quotes all constants and slugifies functors with a bidirectional map; if a residual parse error occurs, log the offending program, skip that one document's ProbLog query (keep its deterministic trace), and proceed -- never let one doc abort the run. The fallback WMC evaluator does NOT need Prolog syntax, so switching engine='fallback' globally also sidesteps all atom-syntax issues.

  SCHEMA VALIDATION FAILS after adding new keys: the new keys are additive; if the method_out schema is strict (additionalProperties:false), nest all new content under an existing permissive container (e.g. the results/analysis object) rather than at top level, mirroring how the prior run nested multihop_corruption/trace_graphs. Re-validate with aii-json and iterate until valid; NEVER ship an invalid method_out.json.

  UNEXPECTED LLM COST (a cache miss because a doc/prompt hash changed): STOP if cumulative > $1 soft cap and investigate (most likely a SEED or prompt-template drift from the copied code). The intended cost is ~$0; if scores must be regenerated, regenerate ONLY the missing items, keep SEED=20240617 and PYTHONHASHSEED=0 so cached items stay hits, and log every call. Absolute HARD STOP at $10.

  BUDGET/TIME OVERRUN: the run is minutes-scale. If ProbLog grounding is somehow slow on a doc, cap per-doc ProbLog wall-time (e.g. 20s) and fall back to the WMC evaluator for that doc. The honest-reporting reanalysis (Phase 2) is pure numpy and must always complete even if the probabilistic layer is fully delegated to the fallback.
testing_plan: |-
  TIERED VALIDATION -- prove each layer on a tiny scale before the full 24-doc run; look for explicit confirmation signals at each step.

  1. INHERITED SELFTESTS (must pass before any new code): in THIS workspace run `uv run method.py --selftest`; confirm the ported kb_engine selftest ('kb_engine selftest PASSED'), fdr_stats/knockoff/bootstrap/BH selftests, and the toy 2-hop derivation all pass. This proves the reused code survived the copy. ALSO run `uv run kb_engine.py` (its __main__ selftest).

  2. PROBLOG MICRO-TEST (5-line script before touching real data): build the toy 2-hop KB from kb_engine.selftest (cross_references('Art13','Art6') @0.9, grants_right('Art6','lawful_processing') @0.7, rule relevant_right). Emit the ProbLog program via the new sanitize()/program-builder, run get_evaluatable().create_from(PrologString).evaluate(), and ASSERT marginal(relevant_right('Art13','lawful_processing')) == 0.9*0.7 == 0.63 (within 1e-9). This single assertion validates: atom sanitization, program emission, the evaluate() API, and the result-mapping back to (pred,args). If ProbLog import fails here, immediately switch to the fallback WMC evaluator and re-run the SAME assertion (must also give 0.63).

  3. FALLBACK-EQUIVALENCE TEST: on the same toy KB plus a 2-PROOF case (two independent bridges concluding the same atom with proof probs 0.5 and 0.4), assert ProbLog marginal == fallback WMC marginal within 1e-9, and == 1-(1-0.5)*(1-0.4)=0.7 for the noisy-OR sanity check. This guarantees the fallback is a faithful ProbLog-equivalent.

  4. MINI DATA SMOKE RUN (12 docs, mini_data_out.json): run the WHOLE pipeline (load cache -> grid -> corruption-with-CIs -> ProbLog/fallback marginals -> trace-graph export -> build_output) and CHECK confirmation signals: (a) cumulative cost ~0 (cache hits) -- if not, STOP and inspect; (b) regulatory yields >=1 multi-hop derived conclusion with a marginal in (0,1) and strictly < min(leaf weights) is false / equals product for single-proof -- sanity check the marginal magnitude; (c) every exported prob trace-graph leaf carries provenance + decoy_certificate + entrapment_certificate + w_i; (d) doc-block bootstrap returns finite CIs; (e) method_out.json passes aii-json schema validation on the mini variant.

  5. FULL RUN (24 docs) -- confirmation signals to verify before declaring done: (a) atomic_reduction_pooled reproduces the known points (portable gate ~0.183, logprob ~0.178, raw ~0.243) and cells_ci_separated == 0/40 (the directional-not-significant finding must reproduce); (b) multihop_corruption pooled raw ~0.48 -> gate(a=0.5) ~0.18 with single_genre_origin='regulatory' and per-genre counts showing legal corrupt=0, news derived=0; CIs present and WIDE; (c) self_report_regime='conservative' with anti_conservative_cells==0 (contrast vs CLUTRR reproduced); (d) prob_trace_graphs has >=1 example per genre (>=1 genuine multi-hop on regulatory) and reports engine in {'problog','fallback'}; (e) sensitivity table shows shrinkage vs margin marginals differ in the expected direction (shrinkage <= identity marginal since 1-alpha_hat<=1); (f) final method_out.json + mini/preview all schema-valid; (g) cumulative cost < $1.

  6. NEGATIVE / GUARD CHECKS: assert the DETERMINISTIC baseline numbers are UNCHANGED from the inherited run (the probabilistic layer must not perturb any headline metric -- diff the deterministic multihop_corruption point estimates against SRC/method_out.json); assert no new key removed an old key (superset check vs the prior method_out.json); confirm figures render to PNG without a system `dot` binary (networkx/matplotlib path). Run as a PID-tracked background process; verify completion by a fresh terminal signal (e.g. a final 'ALL DONE cost=$X' log line and the count of exported trace-graphs), NOT by grepping for generic strings that could match other runs.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_K6AE23HoGqe6
type: research
title: >-
  Spec: Text-to-FOL-to-Prolog Pipeline and the Fair Re-DocRED Operational Comparison
summary: >-
  Implementation-ready specification (verbatim prompt templates, on-disk data formats, exact library APIs, mapping rules,
  ASCII pipeline diagram, library table, and data-format cheat-sheets) for the extraction-to-Prolog neuro-symbolic pipeline
  and the fair matched-recall operational comparison of the decoy-gating hypothesis. Block A: LLM text->typed-FOL FACT/BRIDGE
  extraction with deliberate over-generation in LINC (NLTK/Prover9 FOL, <PREMISES>/<EVALUATE> tags) and Logic-LM (Predicates:::/Facts/Rules>>>/Query)
  style; controlled-functor fact()/bridge() on-disk forms; over-generation prompts (T=0.7, n=3, cap 20/doc) and the candidate-record
  JSON schema with worked CLUTRR and Re-DocRED examples. Block B: SWI-Prolog-from-Python execution (janus-swi RECOMMENDED
  with exact query_once/query/consult/apply_once API; pyswip fallback; swipl subprocess safety net) plus a vanilla solve/2
  proof-tree meta-interpreter extended so each leaf carries provenance + decoy_certificate (W_i,T,q) + entrapment_certificate
  (FDP-hat,r), exported to JSON and Graphviz DOT with a 2-hop example. Block C: offline WordNet hypernym argument typing into
  {PER,LOC,ORG,TIME,NUM,MISC} with exact synset anchors, reusing Re-DocRED gold NER, ConceptNet/DBpedia optional. Block D
  (load-bearing): the Re-DocRED JSON schema and official (title,r,h_idx,t_idx) triple-matching metric, plus ONE fixed claim-decomposition
  + relation-alignment (MiniLM top-8 shortlist -> fixed temp-0 LLM pick among 96 P-codes or NO_RELATION) + three-tier entity-linking
  procedure that maps neuro-symbolic/plain-threshold/CoT/RAG/conformal outputs identically into the (head, P-code, tail) space,
  with a per-system matched-recall score sweep, a hallucinated-conclusion-rate definition for multi-hop deductions, and document-block-bootstrap
  CIs. Block E: RAG (BM25) and CoT extraction prompts, the plain zero-label confidence-threshold gate (primary foil), and
  the verbatim Mohri-Hashimoto conformal back-off Algorithm 1 plus its reusable sayless.py implementation (BREAKDOWN_PROMPT,
  frequency+gpt scoring, ceil-quantile calibration), explicitly positioned as the LABELED reference the label-free decoy wedge
  improves on. The decoy-gating core states the knockoff statistic and the knockoff+ data-dependent FDR threshold. Ten design
  decisions are resolved with fallbacks; a shared sub-$0.30/M OpenRouter model with prompt caching is recommended. 26 primary
  sources (papers + GitHub repos) cited; high confidence except the full 96-row rel_info.json and model-logprob availability.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_UBTwyePql8NQ
type: dataset
title: >-
  Application Anchor: 24 short legal/news/regulatory docs, triple gold + provenance
summary: |-
  The APPLICATION ANCHOR: one merged, schema-validated dataset (full_data_out.json, exp_sel_data_out schema) of 24 genuine, professionally-written short documents (native char_length 1239-3474, mean 2372), perfectly balanced 8 legal / 8 news / 8 regulatory, standardized to the SAME (head, relation, tail) triple space and coarse {PER,LOC,ORG,TIME,NUM,MISC} entity typing as the CLUTRR and Re-DocRED anchors (dependency research_out.json, Block C WordNet anchors). It is the genre-faithful real-document slice the next-iteration text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment depends on.

  PER EXAMPLE (each document = ONE example): input is a JSON string {doc_id, document_text (verbatim UTF-8), genre, source, char_length, entities:[{name, type in the 6-type set, char_span:[s,e]}]}; output is a JSON string {gold_atomic_facts:[{head, relation, tail, provenance_char_span:[s,e]}]}. Flat metadata: metadata_fold=genre (leave-one-genre-out), metadata_gold_quality (crisp|silver), metadata_source, metadata_license, metadata_relation_vocab, metadata_char_length, metadata_num_facts, metadata_num_entities, metadata_entity_types_fine (spaCy fine NER labels), plus per-source fields. datasets[] is grouped by SOURCE CORPUS: CUAD(8), Wikinews(8), GDPR(5), eCFR(3).

  GOLD (140 facts total, 3-15 per doc). LEGAL = CUAD v1 (CC BY 4.0), CRISP: triples mapped deterministically from human-annotated clause spans (has_title, has_party, agreement_date, effective_date, expiration_date, governed_by, renewal_term, liability_cap, contains_* clause types). NEWS = Wikinews (CC BY 2.5), SILVER: deterministic spaCy dependency SVO + 5W (action-verb predicates, occurred_on, affiliated_with). REGULATORY = GDPR/Reg(EU)2016/679 via EUR-Lex free reuse + eCFR (US public domain), SILVER: structural regex (has_title, grants_right, obligates, has_exception, cross_references, defined_as, requires). NO LLM is used anywhere in gold construction (preserves non-circularity for the next-iteration hallucination experiment); entity spans/types come only from offline spaCy NER + NLTK WordNet.

  GUARANTEES. Every entity char_span and fact provenance_char_span re-verified against document_text (946/946 entity spans exact; value-tail facts have tail as a substring of the provenance span; clause/label facts carry the annotated clause as evidence). 93.6% of fact endpoints link to the typed entities[] layer. Licenses are all free (CC BY 4.0 / CC BY 2.5 / EUR-Lex reuse / US public domain). Deterministic regeneration (seed 42, pinned tool versions) from the cached raw/ snapshot with no network: `python data.py` (or regenerate.sh) reproduces byte-identical output; build/verify_dataset.py re-checks all invariants.

  DATASET SELECTION: 4 source corpora chosen from 7 evaluated. Excluded REDFM (CC BY-SA-NC, NonCommercial), ContractNLI-HF (CC BY-NC-SA, NonCommercial), WebRED (free but sentence-level, not genre-faithful), LDC ACE/TACRED (restricted). Count is 4 (not 6) because the plan's hard free-license + genre-faithfulness gates legitimately exclude the rest while the binding deliverable (~24 balanced docs across 3 genres, crisp where possible) is fully met. Honest limitation: legal gold is crisp; news and regulatory gold are silver (rule/structure curation, high precision, partial recall) — carried per row by gold_quality. Variants: full_data_out.json (24 examples, all 4 groups), mini_data_out.json (3 per group = 12), preview_data_out.json (12, strings truncated to 200). full_data_out.json is 209K, far under the 100MB limit (no split). dataset_meta.json + schema/row_payload_schema.json + README.md + pyproject.toml (61 pinned deps) accompany it.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

--- Dependency 3 ---
id: art_Cr6L9JpoewZi
type: research
title: >-
  Novelty-Delta, Upper-Ontology Grounding Recipe, and LLM-as-Probabilistic-Reasoner Design
summary: >-
  Source-traceable research closing three iteration-1 reviewer gaps for the decoy-gated neuro-symbolic text-to-logic pipeline,
  extending (not contradicting) Spec A (FDR gate) and Spec B (pipeline/typing/trace-graph). PART A: a five-dimension NOVELTY-DELTA
  table pinning six nearest conformal/FDR neighbors - Jin-Candes conformal selection [1], Li-Magesh-Veeravalli multiple-testing
  hallucination detection [2], COCOCO neuro-symbolic conformal sets [3], Bashari conformal-e-value novelty detection [4],
  Marandon/Blanchard conformal link-prediction FDR [5,6], Mohri-Hashimoto conformal factuality [7] - on {label requirement,
  unit certified, exchangeability mechanism, decoy?, FDR-vs-coverage}; all are LABELED and certify a model OUTPUT under assumed
  exchangeability, whereas OURS is label-free, certifies the INTERMEDIATE text->logic admission, uses engineered+tested decoy
  sign-flip, and controls FDR. Includes a paste-ready one-sentence delta, a 'not just conformal selection' rebuttal, and an
  honest adversarial result (no 2025-2026 preprint pre-empts the construction). PART B: OpenCyc honestly reported as discontinued
  (March 2017 [8,9], third-party-mirror-only [10]) and ResearchCyc as license-gated [8]; a concrete offline-first two-layer
  argument-typing recipe - WordNet hypernyms [11] anchored to SUMO upper-ontology classes via WordNetMappings30 (verified
  line: person -> &%Human=) [12,13,14], plus Wikidata P31/P279* [17] or offline YAGO 4.5 [15,16] instance typing, loadable
  with owlready2/SPARQLWrapper [18] - and a loss/sufficiency/descope-vs-defer justification arguing why typing-only usage
  cannot break the FDR guarantee (unlike ontology-constraint filtering). PART C: a concrete LLM-as-probabilistic-reasoner
  design - ProbLog primary (verified API: get_evaluatable().create_from(PrologString).evaluate() -> {Term:prob}; p::fact.;
  annotated disjunctions; query/evidence; explain/MPE proofs [19,20,21]; LFI weight learning [22]; aProbLog semirings [23];
  DeepProbLog neural-predicate precedent [24]) with Bousi~Prolog/FASILL as the fuzzy-unification alternative [25,26,27,28];
  a certificate->probabilistic-weight mapping table (p_i=calibrate(Z_i); gate-consistent shrinkage (1-alpha_hat)*p_i [default]
  or per-pair W_i margin weight; entrapment FDP-hat as consistency prior; full cert kept at the leaf); a probabilistic trace-graph
  export (reuse Spec-B JSON/Graphviz-DOT, add a 'prob' attribute per node/edge, marginal per derived node, certificate per
  leaf; janus-swi solve/2 fallback for the proof DAG); and the exact deterministic->probabilistic upgrade swap (janus query_once
  -> problog get_evaluatable/evaluate). Deliverables: research_out.json + research_report.md with 30 primary sources, tables,
  recipes, exact APIs, and a positioning note mapping each part to the named reviewer gaps.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

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

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-16 10:53:27 UTC

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

### [3] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 10:53:39 UTC

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

### [4] SKILL-INPUT — aii-python · 2026-06-16 10:53:43 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-16 10:54:05 UTC

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

### [6] SYSTEM-USER prompt · 2026-06-16 11:29:32 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx4
type: experiment
title: >-
  P4+P2-framing: Minimal ProbLog probabilistic reasoner on the 24-doc anchor + honest finalized application reporting (corruption
  CIs, directional atomic reduction, conservative self-report)
summary: >-
  Reanalysis-plus-ProbLog experiment that REUSES the already-executed iter-3 P2 pipeline (method.py + kb_engine.py + typing_sumo.py
  + fdr_stats.py + llm_client.py + cached scores, all in iter_3/gen_art/gen_art_experiment_2) on the EXISTING 24-doc legal/news/regulatory
  anchor (art_UBTwyePql8NQ). Two deliverables: (P4) execute the goal-hard-required LLM-as-probabilistic-reasoner by swapping
  the deterministic backward-chaining query for a minimal ProbLog get_evaluatable().create_from(PrologString).evaluate() run
  with the certificate->weight mapping (gate-consistent shrinkage (1-alpha_hat)*calibrate(Z_i) default; per-pair W_i-margin
  alternative), emitting probabilistic trace-graphs (marginals per node + per-leaf provenance/decoy/entrapment certificates)
  on >=1 doc/genre, with a pure-Python exact weighted-model-counting fallback that reproduces ProbLog marginals if ProbLog
  cannot install; (P2-framing) recompute the multi-hop corruption result WITH document-block bootstrap CIs + an explicit single-genre
  (regulatory) origin flag and per-system derived-conclusion counts, report the pooled atomic hallucinated-fact reduction
  across BOTH elicitations x ALL alpha with CIs and state PLAINLY it is DIRECTIONAL/not CI-separated at n=24, and carry the
  CONSERVATIVE self-report finding (decoy_fdr_hat>=realized everywhere, contrasting CLUTRR). Deterministic backward-chaining
  stays the required baseline so no headline number depends on ProbLog. Emit figure-ready arrays + full captions; method_out.json
  schema-valid; log cumulative LLM cost after every call (this is ~$0 cache-hit reanalysis); soft cap ~$1, HARD STOP $10.
  CPU-only.
runpod_compute_profile: gpu
implementation_pseudocode: |
  ########################################################################
  # CONTEXT (read first). This artifact is LARGELY A REANALYSIS + a small
  # ProbLog run on ALREADY-CACHED LLM scores. Do NOT re-extract / re-score from
  # scratch. Reuse the iter-3 P2 execution verbatim and add the probabilistic
  # layer + honest finalized reporting on top.
  #
  # SOURCE OF TRUTH (read these files, copy them into THIS workspace):
  #   SRC = /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2
  #   Reuse:  method.py, kb_engine.py, typing_sumo.py, fdr_stats.py, llm_client.py,
  #           pyproject.toml, and the WHOLE cache/ directory (sha256-keyed LLM cache).
  #   Dataset (UNCHANGED 24-doc anchor, art_UBTwyePql8NQ):
  #     DEP_DATA = .../iter_2/gen_art/gen_art_dataset_1/full_data_out.json (+ mini_data_out.json)
  #   ProbLog spec: .../iter_2/gen_art/gen_art_research_1/research_out.json + research_report.md
  #                 (Part C: API, C.2 certificate->weight table, C.3 trace-graph, C.5 upgrade swap)
  #   The expanded anchor from Artifact-3 is NOT consumed here (it runs in parallel,
  #   consumed next iteration). Use ONLY the existing 24 docs.
  #
  # KEY FACTS ABOUT THE REUSED CODE (already verified):
  #  - kb_engine.KB: pure-Python backward-chaining. Fact=(pred,(args...))->cert dict.
  #    Rule=(name, head_pred, head_args tuple of V('X'), body list of (pred,args)).
  #    Uses explicit Var class (V('A')) -- NOT capitalization. derive_all(max_depth=4)
  #    returns proof dicts {type:derived/leaf, atom:[pred,[args]], rule, children/cert}.
  #    proof_to_graph -> {nodes,edges}; graph_to_dot -> DOT string. iter_leaves walks leaves.
  #    Each leaf cert = {provenance, provenance_char_span, hallucination_verdict,
  #       decoy_certificate:{W_i,T,alpha}, entrapment_certificate:{FDP_hat,r}}.
  #  - method.py constants: SEED=20240617, ALPHA_GRID=[0.05,0.10,0.20,0.30,0.50],
  #    B_BOOT=2000, K_SC=5, R_ENTRAP=1, GENRES=[legal,news,regulatory],
  #    PRIMARY_MODEL=openai/gpt-4.1-nano (logprob+portable/self-consistency),
  #    CROSS_MODEL=mistralai/ministral-8b-2512. Two elicitations: 'portable'(=K=5
  #    self-consistency, the 0.183 headline) and 'logprob'(0.178). raw baseline=0.243.
  #  - method.py already has: gate_and_hall_grid (per genre x elic x alpha: gate vs raw
  #    rate + raw_ci/gate_ci doc-block bootstrap + decoy_fdr_hat + entrapment FDP_hat),
  #    build_kb, derive_doc, multihop_corruption (RAW-KB vs GATE-KB derived/corrupt counts,
  #    NO CIs yet), export_trace_graphs (deterministic), W_cf_of (knockoff W_i for a real),
  #    rank_normalize_elic / headline_norm (per-doc rank-normalized real score Z_i),
  #    build_output (assembles method_out.json), selftest().
  #  - fdr_stats (st): doc_block_bootstrap(units, stat_fn, B, seed), knockoff_plus_threshold
  #    (returns threshold T + estimated_ratio == decoy_fdr_hat), BH, etc.
  #  - llm_client.OpenRouterClient: disk cache keyed sha256(payload+sample_idx), exact
  #    usage.cost, $10 hard-stop. Re-running same 24 docs @ same SEED = 100% cache hits = $0.
  ########################################################################

  # ----------------------------------------------------------------------
  # PHASE 0 -- WORKSPACE BOOTSTRAP (no LLM calls, ~minutes)
  # ----------------------------------------------------------------------
  0.1  Copy SRC/{method.py,kb_engine.py,typing_sumo.py,fdr_stats.py,llm_client.py,
       pyproject.toml} and SRC/cache/ into THIS workspace. Keep DEP_DATA absolute path.
  0.2  `uv sync`; then add the probabilistic-reasoning dep:
          `uv add problog`   (pure-Python; default compiler tries PySDD/d-DNNF backends)
       Also ensure networkx + matplotlib present (already in pyproject for rendering).
  0.3  Set env: PYTHONHASHSEED=0. Run the inherited `uv run method.py --selftest` FIRST
       to confirm the ported pipeline + kb_engine + fdr_stats selftests still PASS in this
       workspace (this re-validates the reused code before extending it).
  0.4  Quick cache-warmth check: run a MINI pass (mini_data_out.json, 12 docs) end-to-end
       reading from the copied cache/; confirm cumulative cost stays ~$0 (cache hits). If
       any miss appears, it is only for docs/prompts not previously scored -- log the cost,
       it must stay << $1. This proves we are reanalyzing, not re-scoring.

  # ----------------------------------------------------------------------
  # PHASE 1 -- PROBABILISTIC REASONER (P4): new module prob_reasoner.py
  # ----------------------------------------------------------------------
  # Goal: a minimal but REAL ProbLog run that turns admitted facts/bridges into a
  # weighted program, computes multi-hop conclusion MARGINALS, and exports probabilistic
  # trace-graphs. Deterministic kb_engine REMAINS the baseline (no headline depends on this).

  1.1  calibrate(Z_i) -> p_i in (0,1):
         Z_i = the per-doc RANK-NORMALIZED real score from headline_norm (already in [0,1];
           reuse the exact access path that W_cf_of uses to fetch the real's normalized score).
         DEFAULT calibrate = identity clamp: p_i = clip(Z_i, eps, 1-eps), eps=1e-3 (monotone,
           no labels needed -> keeps the method label-free, consistent with the gate).
         OPTIONAL sensitivity (report, do NOT headline): Platt/isotonic fit Z_i->P(entailed)
           on the gold hall_adj labels of the anchor reals; FLAG explicit overfit risk at n=24.

  1.2  Per-pair / FDR weights (the C.2 mapping table):
         alpha_hat = decoy_fdr_hat of the OPERATIVE gate cell for that (genre,elic) at the
           headline alpha (alpha*=0.5, the only certified one on 24 docs).
         (i) DEFAULT gate-consistent shrinkage:  w_i = (1 - alpha_hat) * p_i
         (ii) ALTERNATIVE per-pair margin:       w_i = clip(0.5 + 0.5*W_i_rank, eps, 1-eps)
              where W_i_rank = rank-normalized knockoff margin (W_cf_of). Report BOTH on the
              SAME proofs as a sensitivity row; headline marginals use (i).
         entrapment FDP_hat carried at the leaf as a consistency prior (annotation only, not
           folded into w_i for the headline -- keep it auditable and separable).

  1.3  KB -> ProbLog program string (handle the Prolog-atom gotcha CAREFULLY):
         sanitize(name): make a valid Prolog atom. Relations/predicate functors -> slug:
           lowercase, [^a-z0-9_]->'_', prefix 'p_' if starts non-alpha. Entity CONSTANTS ->
           single-quoted atoms: "Art13"->'Art13', "ACME Corp"->'ACME Corp' (escape inner quotes).
           Keep a bidirectional map {prolog_term <-> original} to map results back.
         For each admitted fact f with weight w_i:  emit  `<w_i>::<rel>(<h_atom>,<t_atom>).`
         For each genre BRIDGE_RULE (deterministic, weight 1): emit a Prolog rule
           `<head>(A,R) :- <b1>(A,B), <b2>(B,R).`  (V('A')->A etc.; vars are uppercase -> valid).
         For each DERIVED conclusion produced by kb.derive_all (the deterministic baseline
           already gives us exactly which conclusions exist), emit `query(<conclusion>).`
         NOTE: ProbLog computes ALL queries in one evaluate() call.

  1.4  Run ProbLog (the exact swap per spec C.5):
         from problog.program import PrologString
         from problog import get_evaluatable
         marginals = get_evaluatable().create_from(PrologString(prog)).evaluate() # {Term:prob}
         Map each Term back to (pred,args) via the bidirectional map -> conclusion_marginal.
         For a 2-hop single-proof bridge this yields p_leaf1*p_leaf2; multiple proofs -> the
         correct noisy-OR / WMC (ProbLog handles shared leaves exactly).

  1.5  Probabilistic trace-graph export (extend kb_engine, do NOT mutate the baseline):
         Reuse proof_to_graph -> add a 'prob' attribute to every node:
           leaf node prob = its calibrated weight w_i; derived/root node prob = the ProbLog
           marginal of that sub-conclusion (query each intermediate derived head too; for the
           non-recursive 2-hop bridges the only derived node is the root). Keep every leaf's
           full certificate (provenance + decoy{W_i,T,alpha} + entrapment{FDP_hat,r} + w_i).
         Extend graph_to_dot -> annotate each node label with its marginal/weight; add a
           second JSON dump prob_trace_<doc_id>.json carrying {graph_with_prob, program, marginals,
           mapping, engine:'problog'|'fallback'}. DOT path too.
         Export >=1 doc PER GENRE:
           regulatory -> a real multi-hop bridge proof (cross_references+grants_right) with a
             genuine multi-hop MARGINAL (this is the showcase; regulatory is the only genre that
             derives multi-hop conclusions).
           legal & news -> bridges rarely/never fire (news derives 0 multi-hop). Use the existing
             depth-1 _admission_trace: a single admitted fact with marginal = its w_i. This STILL
             demonstrates the probabilistic layer (LLM-supplied calibrated unification weight at a
             leaf). State this honestly in the output: the multi-hop probabilistic marginal is
             demonstrated on regulatory; legal/news show single-fact probabilistic admissions.

  1.6  Sensitivity table: for the regulatory multi-hop conclusions, report marginal under
       (i) gate-consistent shrinkage vs (ii) per-pair margin weight vs (default identity p_i
       with alpha_hat=0, i.e. no shrinkage) -- a 3-row table showing how the FDR certificate
       shifts the truth mass. This directly answers the spec's open 'how sensitive are multi-hop
       marginals to shrinkage vs margin weighting' question.

  # ----------------------------------------------------------------------
  # PHASE 2 -- FINALIZE HONEST APPLICATION REPORTING (P2-framing; NO new LLM calls)
  # ----------------------------------------------------------------------
  2.1  MULTI-HOP CORRUPTION WITH CIs + single-genre flag. Extend multihop_corruption:
         Bootstrap unit = the DOCUMENT. For RAW-KB and for GATE-KB(alpha=0.5):
           build per-doc lists of corrupt-flags over that doc's derived conclusions; resample
           DOCS with st.doc_block_bootstrap(B=B_BOOT, seed=SEED) and recompute corrupted_rate
           for raw, gate, and the DELTA (raw-gate). Report point + 95% CI for each.
         Add fields: per-genre {derived, corrupt, corrupted_rate} for raw & gate (this surfaces
           legal corrupted_rate already 0.0, news derived==0, regulatory 12->3); a top-level
           flag single_genre_origin='regulatory' with a one-line note that the pooled
           0.48->0.18 drop is ENTIRELY regulatory-driven (legal clean, news derives nothing);
           report per-system derived-conclusion COUNTS (e.g. raw ~23 vs gate ~11). State that
           with one contributing genre and ~11-23 conclusions the CI is WIDE and the drop is a
           DIRECTIONAL trend, not a significant reduction.
  2.2  POOLED ATOMIC HALLUCINATED-FACT REDUCTION across genres, BOTH elicitations x ALL alpha:
         For each (elic in {portable, logprob}, alpha in ALPHA_GRID): pool reals across all 3
           genres; compute pooled raw rate and pooled gate rate (admitted reals at that cell's T);
           doc-block bootstrap the DIFFERENCE (raw_rate - gate_rate) resampling docs across genres
           -> 95% CI on the reduction. cells_ci_separated = count of cells whose diff-CI excludes 0
           (EXPECT 0/40 -- confirm and REPORT the count). Headline numbers: portable gate 0.183 /
           logprob 0.178 vs raw 0.243 (~25% rel). STATE PLAINLY at the point of claim:
           'DIRECTIONAL, not CI-separated at n=24 (0/40 cells); demonstrated as a trend with
           auditable provenance.'  Keep the existing per-cell raw_ci/gate_ci too.
  2.3  CONSERVATIVE SELF-REPORT finding. For every (genre,elic,alpha) cell compute realized FDR
         (vs gold hall_adj) and compare to the gate's decoy_fdr_hat. anti_conservative_cells =
         count where decoy_fdr_hat < realized - tau (tau=0.05); EXPECT 0/40. Emit
         self_report_regime='conservative' with the explicit contrast: 'decoy_fdr_hat >= realized
         in all 40 cells here (gate UNDER-admits / over-estimates falsity), the OPPOSITE of the
         CLUTRR multi_hop anti-conservative regime (decoy_fdr_hat=0.5 < realized 1.0)'. Provide the
         (alpha, decoy_fdr_hat, realized) triples per cell for the figure.

  # ----------------------------------------------------------------------
  # PHASE 3 -- FIGURES (arrays + captions) + OUTPUT (NO new LLM calls)
  # ----------------------------------------------------------------------
  3.1  Emit figure-ready arrays under method_out.json['figures'] AND render PNGs via a small
       build_figures.py (matplotlib for bars/scatter; networkx+matplotlib for the graph, since
       there is NO system `dot` binary in this env -- do NOT shell out to graphviz). Figures:
         F1 pooled atomic hallucination raw vs gate across alpha, both elicitations, CI bars.
            CAPTION must state: doc-block bootstrap (B=2000), n=24 docs, 0/40 CI-separated cells,
            DIRECTIONAL trend; 1/k admission floor {20,10,5,4,2} for alpha {.05,.10,.20,.30,.50}.
         F2 multi-hop corruption RAW-KB vs GATE-KB(a=0.5) with CIs + per-genre stacked bars
            annotating that regulatory is the SOLE contributor (legal=0, news derives 0).
            CAPTION: derived-conclusion counts, single-genre origin, wide CI.
         F3 decoy_fdr_hat vs realized FDR scatter with y=x line, all 40 cells above the line
            (conservative regime), contrasted against the CLUTRR anti-conservative point.
            CAPTION: conservative self-report, contrast with CLUTRR.
         F4 a probabilistic trace-graph (regulatory multi-hop) rendered with node marginals +
            per-leaf certificate annotations. CAPTION: ProbLog (or fallback) marginal, gate-
            consistent shrinkage weights, per-leaf provenance+decoy+entrapment certificates.
       EVERY caption carries: bootstrap method+B, n, regime tag, and (where relevant) the 1/k floor.
  3.2  Assemble method_out.json by EXTENDING build_output. ADD top-level keys:
         'probabilistic_reasoning': {engine:'problog'|'fallback', mapping_default:'gate_consistent_shrinkage',
             per_doc_marginals:[...], sensitivity_shrinkage_vs_margin:[...], genres_with_multihop:['regulatory'],
             note:'deterministic backward-chaining remains the baseline; no headline number depends on ProbLog'},
         'prob_trace_graphs': {n_exported, examples:[{doc_id,genre,engine,conclusion,marginal,json_path,dot_path}]},
         updated 'multihop_corruption' (with CIs + per-genre counts + single_genre_origin),
         'atomic_reduction_pooled' (per elic x alpha: raw,gate,diff,diff_ci,cells_ci_separated,directional:true),
         'self_report_regime':'conservative' (+ per-cell triples + anti_conservative_cells:0),
         'figures' (arrays + captions), and a 'contributions' note that the probabilistic reasoner
         is DELIVERED (not only specified) so the abstract/intro never overclaim or underclaim.
       Keep ALL prior keys. Re-run the schema validation the prior run used (aii-json) against the
       SAME method_out schema; generate mini_/preview_ variants. Confirm schema-valid.
  3.3  Cost: append cumulative LLM cost to logs/cost.jsonl after EVERY call (there should be ~0
       new calls). Print final cumulative cost. Assert < SOFT_CAP (~$1); HARD STOP at $10.

  # ----------------------------------------------------------------------
  # RUN DISCIPLINE
  # ----------------------------------------------------------------------
  # Launch the full run as a DIRECTLY-tracked background python (NO trailing `&` inside a
  # background Bash -> avoids the orphan-double-write gotcha). Use timeout + PID:
  #   `uv run method.py --full & PID=$!` then poll `kill -0 $PID`. Stop strays by PID only
  #   (other runs share method.py -- NEVER pkill/grep-by-name). Total wall time ~minutes
  #   (reanalysis on cached scores + tiny ProbLog grounding).
fallback_plan: |-
  PROBLOG INSTALL/RUN FAILURE (the most likely risk -- ProbLog's knowledge-compilation backend PySDD/d-DNNF can fail to build on a minimal CPU image): fall back to a PURE-PYTHON EXACT weighted-model-counting (WMC) evaluator in prob_reasoner.py that REPRODUCES ProbLog marginals on these tiny proof DAGs. Algorithm: collect the DISTINCT grounded leaf facts in the doc's KB (each an independent Bernoulli with prob = its calibrated weight w_i). If #distinct_leaves <= 18: enumerate all 2^n truth assignments; for each, build a sub-KB containing only the 'present' facts, run the existing deterministic kb.derive_all, test whether the queried conclusion is derivable, and accumulate the assignment's probability (product of w_i for present, (1-w_i) for absent) into the marginal when derivable. This is EXACT WMC for independent facts + deterministic rules -> identical to ProbLog. If #distinct_leaves > 18: fall back to noisy-OR over the enumerated proofs (marginal = 1 - prod_over_proofs(1 - prod_over_leaves(w_i))) and FLAG it as an approximation in the output. Report engine='fallback' and state explicitly it is a 'faithful ProbLog-equivalent exact WMC' -- so the probabilistic layer is DEMONSTRATED either way and the CONTRIBUTIONS (not only limitations) can claim the reasoner is delivered. VALIDATION: add a selftest asserting fallback marginal == ProbLog marginal within 1e-9 on the toy 2-hop KB whenever ProbLog IS available; if ProbLog absent, assert the fallback's toy 2-hop marginal == p1*p2 analytically.

  NO MULTI-HOP CONCLUSIONS DERIVE ON ANY GENRE (bridges never fire because admitted facts don't chain): then the multi-hop probabilistic marginal cannot be shown on a real bridge. Fallback: (a) still demonstrate the probabilistic layer via depth-1 admission traces (single fact -> marginal = w_i) on all 3 genres -- the calibrated-weight-at-the-leaf is the minimal probabilistic-reasoner demonstration; (b) ADDITIONALLY construct ONE synthetic-but-faithful 2-hop query by chaining two genuinely-admitted regulatory facts that share an entity (cross_references(A,B) + grants_right(B,R)) even if the deterministic engine's _degenerate filter dropped it, clearly labeled as an illustrative multi-hop marginal over admitted (certified) leaves. Document honestly. (We already know from iter-3 that regulatory DOES derive ~12 multi-hop conclusions, so this is a safety net only.)

  PROLOG-ATOM ERRORS (entity strings with spaces/quotes/leading digits crash PrologString parsing): the sanitize() layer single-quotes all constants and slugifies functors with a bidirectional map; if a residual parse error occurs, log the offending program, skip that one document's ProbLog query (keep its deterministic trace), and proceed -- never let one doc abort the run. The fallback WMC evaluator does NOT need Prolog syntax, so switching engine='fallback' globally also sidesteps all atom-syntax issues.

  SCHEMA VALIDATION FAILS after adding new keys: the new keys are additive; if the method_out schema is strict (additionalProperties:false), nest all new content under an existing permissive container (e.g. the results/analysis object) rather than at top level, mirroring how the prior run nested multihop_corruption/trace_graphs. Re-validate with aii-json and iterate until valid; NEVER ship an invalid method_out.json.

  UNEXPECTED LLM COST (a cache miss because a doc/prompt hash changed): STOP if cumulative > $1 soft cap and investigate (most likely a SEED or prompt-template drift from the copied code). The intended cost is ~$0; if scores must be regenerated, regenerate ONLY the missing items, keep SEED=20240617 and PYTHONHASHSEED=0 so cached items stay hits, and log every call. Absolute HARD STOP at $10.

  BUDGET/TIME OVERRUN: the run is minutes-scale. If ProbLog grounding is somehow slow on a doc, cap per-doc ProbLog wall-time (e.g. 20s) and fall back to the WMC evaluator for that doc. The honest-reporting reanalysis (Phase 2) is pure numpy and must always complete even if the probabilistic layer is fully delegated to the fallback.
testing_plan: |-
  TIERED VALIDATION -- prove each layer on a tiny scale before the full 24-doc run; look for explicit confirmation signals at each step.

  1. INHERITED SELFTESTS (must pass before any new code): in THIS workspace run `uv run method.py --selftest`; confirm the ported kb_engine selftest ('kb_engine selftest PASSED'), fdr_stats/knockoff/bootstrap/BH selftests, and the toy 2-hop derivation all pass. This proves the reused code survived the copy. ALSO run `uv run kb_engine.py` (its __main__ selftest).

  2. PROBLOG MICRO-TEST (5-line script before touching real data): build the toy 2-hop KB from kb_engine.selftest (cross_references('Art13','Art6') @0.9, grants_right('Art6','lawful_processing') @0.7, rule relevant_right). Emit the ProbLog program via the new sanitize()/program-builder, run get_evaluatable().create_from(PrologString).evaluate(), and ASSERT marginal(relevant_right('Art13','lawful_processing')) == 0.9*0.7 == 0.63 (within 1e-9). This single assertion validates: atom sanitization, program emission, the evaluate() API, and the result-mapping back to (pred,args). If ProbLog import fails here, immediately switch to the fallback WMC evaluator and re-run the SAME assertion (must also give 0.63).

  3. FALLBACK-EQUIVALENCE TEST: on the same toy KB plus a 2-PROOF case (two independent bridges concluding the same atom with proof probs 0.5 and 0.4), assert ProbLog marginal == fallback WMC marginal within 1e-9, and == 1-(1-0.5)*(1-0.4)=0.7 for the noisy-OR sanity check. This guarantees the fallback is a faithful ProbLog-equivalent.

  4. MINI DATA SMOKE RUN (12 docs, mini_data_out.json): run the WHOLE pipeline (load cache -> grid -> corruption-with-CIs -> ProbLog/fallback marginals -> trace-graph export -> build_output) and CHECK confirmation signals: (a) cumulative cost ~0 (cache hits) -- if not, STOP and inspect; (b) regulatory yields >=1 multi-hop derived conclusion with a marginal in (0,1) and strictly < min(leaf weights) is false / equals product for single-proof -- sanity check the marginal magnitude; (c) every exported prob trace-graph leaf carries provenance + decoy_certificate + entrapment_certificate + w_i; (d) doc-block bootstrap returns finite CIs; (e) method_out.json passes aii-json schema validation on the mini variant.

  5. FULL RUN (24 docs) -- confirmation signals to verify before declaring done: (a) atomic_reduction_pooled reproduces the known points (portable gate ~0.183, logprob ~0.178, raw ~0.243) and cells_ci_separated == 0/40 (the directional-not-significant finding must reproduce); (b) multihop_corruption pooled raw ~0.48 -> gate(a=0.5) ~0.18 with single_genre_origin='regulatory' and per-genre counts showing legal corrupt=0, news derived=0; CIs present and WIDE; (c) self_report_regime='conservative' with anti_conservative_cells==0 (contrast vs CLUTRR reproduced); (d) prob_trace_graphs has >=1 example per genre (>=1 genuine multi-hop on regulatory) and reports engine in {'problog','fallback'}; (e) sensitivity table shows shrinkage vs margin marginals differ in the expected direction (shrinkage <= identity marginal since 1-alpha_hat<=1); (f) final method_out.json + mini/preview all schema-valid; (g) cumulative cost < $1.

  6. NEGATIVE / GUARD CHECKS: assert the DETERMINISTIC baseline numbers are UNCHANGED from the inherited run (the probabilistic layer must not perturb any headline metric -- diff the deterministic multihop_corruption point estimates against SRC/method_out.json); assert no new key removed an old key (superset check vs the prior method_out.json); confirm figures render to PNG without a system `dot` binary (networkx/matplotlib path). Run as a PID-tracked background process; verify completion by a fresh terminal signal (e.g. a final 'ALL DONE cost=$X' log line and the count of exported trace-graphs), NOT by grepping for generic strings that could match other runs.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_K6AE23HoGqe6
type: research
title: >-
  Spec: Text-to-FOL-to-Prolog Pipeline and the Fair Re-DocRED Operational Comparison
summary: >-
  Implementation-ready specification (verbatim prompt templates, on-disk data formats, exact library APIs, mapping rules,
  ASCII pipeline diagram, library table, and data-format cheat-sheets) for the extraction-to-Prolog neuro-symbolic pipeline
  and the fair matched-recall operational comparison of the decoy-gating hypothesis. Block A: LLM text->typed-FOL FACT/BRIDGE
  extraction with deliberate over-generation in LINC (NLTK/Prover9 FOL, <PREMISES>/<EVALUATE> tags) and Logic-LM (Predicates:::/Facts/Rules>>>/Query)
  style; controlled-functor fact()/bridge() on-disk forms; over-generation prompts (T=0.7, n=3, cap 20/doc) and the candidate-record
  JSON schema with worked CLUTRR and Re-DocRED examples. Block B: SWI-Prolog-from-Python execution (janus-swi RECOMMENDED
  with exact query_once/query/consult/apply_once API; pyswip fallback; swipl subprocess safety net) plus a vanilla solve/2
  proof-tree meta-interpreter extended so each leaf carries provenance + decoy_certificate (W_i,T,q) + entrapment_certificate
  (FDP-hat,r), exported to JSON and Graphviz DOT with a 2-hop example. Block C: offline WordNet hypernym argument typing into
  {PER,LOC,ORG,TIME,NUM,MISC} with exact synset anchors, reusing Re-DocRED gold NER, ConceptNet/DBpedia optional. Block D
  (load-bearing): the Re-DocRED JSON schema and official (title,r,h_idx,t_idx) triple-matching metric, plus ONE fixed claim-decomposition
  + relation-alignment (MiniLM top-8 shortlist -> fixed temp-0 LLM pick among 96 P-codes or NO_RELATION) + three-tier entity-linking
  procedure that maps neuro-symbolic/plain-threshold/CoT/RAG/conformal outputs identically into the (head, P-code, tail) space,
  with a per-system matched-recall score sweep, a hallucinated-conclusion-rate definition for multi-hop deductions, and document-block-bootstrap
  CIs. Block E: RAG (BM25) and CoT extraction prompts, the plain zero-label confidence-threshold gate (primary foil), and
  the verbatim Mohri-Hashimoto conformal back-off Algorithm 1 plus its reusable sayless.py implementation (BREAKDOWN_PROMPT,
  frequency+gpt scoring, ceil-quantile calibration), explicitly positioned as the LABELED reference the label-free decoy wedge
  improves on. The decoy-gating core states the knockoff statistic and the knockoff+ data-dependent FDR threshold. Ten design
  decisions are resolved with fallbacks; a shared sub-$0.30/M OpenRouter model with prompt caching is recommended. 26 primary
  sources (papers + GitHub repos) cited; high confidence except the full 96-row rel_info.json and model-logprob availability.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_UBTwyePql8NQ
type: dataset
title: >-
  Application Anchor: 24 short legal/news/regulatory docs, triple gold + provenance
summary: |-
  The APPLICATION ANCHOR: one merged, schema-validated dataset (full_data_out.json, exp_sel_data_out schema) of 24 genuine, professionally-written short documents (native char_length 1239-3474, mean 2372), perfectly balanced 8 legal / 8 news / 8 regulatory, standardized to the SAME (head, relation, tail) triple space and coarse {PER,LOC,ORG,TIME,NUM,MISC} entity typing as the CLUTRR and Re-DocRED anchors (dependency research_out.json, Block C WordNet anchors). It is the genre-faithful real-document slice the next-iteration text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment depends on.

  PER EXAMPLE (each document = ONE example): input is a JSON string {doc_id, document_text (verbatim UTF-8), genre, source, char_length, entities:[{name, type in the 6-type set, char_span:[s,e]}]}; output is a JSON string {gold_atomic_facts:[{head, relation, tail, provenance_char_span:[s,e]}]}. Flat metadata: metadata_fold=genre (leave-one-genre-out), metadata_gold_quality (crisp|silver), metadata_source, metadata_license, metadata_relation_vocab, metadata_char_length, metadata_num_facts, metadata_num_entities, metadata_entity_types_fine (spaCy fine NER labels), plus per-source fields. datasets[] is grouped by SOURCE CORPUS: CUAD(8), Wikinews(8), GDPR(5), eCFR(3).

  GOLD (140 facts total, 3-15 per doc). LEGAL = CUAD v1 (CC BY 4.0), CRISP: triples mapped deterministically from human-annotated clause spans (has_title, has_party, agreement_date, effective_date, expiration_date, governed_by, renewal_term, liability_cap, contains_* clause types). NEWS = Wikinews (CC BY 2.5), SILVER: deterministic spaCy dependency SVO + 5W (action-verb predicates, occurred_on, affiliated_with). REGULATORY = GDPR/Reg(EU)2016/679 via EUR-Lex free reuse + eCFR (US public domain), SILVER: structural regex (has_title, grants_right, obligates, has_exception, cross_references, defined_as, requires). NO LLM is used anywhere in gold construction (preserves non-circularity for the next-iteration hallucination experiment); entity spans/types come only from offline spaCy NER + NLTK WordNet.

  GUARANTEES. Every entity char_span and fact provenance_char_span re-verified against document_text (946/946 entity spans exact; value-tail facts have tail as a substring of the provenance span; clause/label facts carry the annotated clause as evidence). 93.6% of fact endpoints link to the typed entities[] layer. Licenses are all free (CC BY 4.0 / CC BY 2.5 / EUR-Lex reuse / US public domain). Deterministic regeneration (seed 42, pinned tool versions) from the cached raw/ snapshot with no network: `python data.py` (or regenerate.sh) reproduces byte-identical output; build/verify_dataset.py re-checks all invariants.

  DATASET SELECTION: 4 source corpora chosen from 7 evaluated. Excluded REDFM (CC BY-SA-NC, NonCommercial), ContractNLI-HF (CC BY-NC-SA, NonCommercial), WebRED (free but sentence-level, not genre-faithful), LDC ACE/TACRED (restricted). Count is 4 (not 6) because the plan's hard free-license + genre-faithfulness gates legitimately exclude the rest while the binding deliverable (~24 balanced docs across 3 genres, crisp where possible) is fully met. Honest limitation: legal gold is crisp; news and regulatory gold are silver (rule/structure curation, high precision, partial recall) — carried per row by gold_quality. Variants: full_data_out.json (24 examples, all 4 groups), mini_data_out.json (3 per group = 12), preview_data_out.json (12, strings truncated to 200). full_data_out.json is 209K, far under the 100MB limit (no split). dataset_meta.json + schema/row_payload_schema.json + README.md + pyproject.toml (61 pinned deps) accompany it.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

--- Dependency 3 ---
id: art_Cr6L9JpoewZi
type: research
title: >-
  Novelty-Delta, Upper-Ontology Grounding Recipe, and LLM-as-Probabilistic-Reasoner Design
summary: >-
  Source-traceable research closing three iteration-1 reviewer gaps for the decoy-gated neuro-symbolic text-to-logic pipeline,
  extending (not contradicting) Spec A (FDR gate) and Spec B (pipeline/typing/trace-graph). PART A: a five-dimension NOVELTY-DELTA
  table pinning six nearest conformal/FDR neighbors - Jin-Candes conformal selection [1], Li-Magesh-Veeravalli multiple-testing
  hallucination detection [2], COCOCO neuro-symbolic conformal sets [3], Bashari conformal-e-value novelty detection [4],
  Marandon/Blanchard conformal link-prediction FDR [5,6], Mohri-Hashimoto conformal factuality [7] - on {label requirement,
  unit certified, exchangeability mechanism, decoy?, FDR-vs-coverage}; all are LABELED and certify a model OUTPUT under assumed
  exchangeability, whereas OURS is label-free, certifies the INTERMEDIATE text->logic admission, uses engineered+tested decoy
  sign-flip, and controls FDR. Includes a paste-ready one-sentence delta, a 'not just conformal selection' rebuttal, and an
  honest adversarial result (no 2025-2026 preprint pre-empts the construction). PART B: OpenCyc honestly reported as discontinued
  (March 2017 [8,9], third-party-mirror-only [10]) and ResearchCyc as license-gated [8]; a concrete offline-first two-layer
  argument-typing recipe - WordNet hypernyms [11] anchored to SUMO upper-ontology classes via WordNetMappings30 (verified
  line: person -> &%Human=) [12,13,14], plus Wikidata P31/P279* [17] or offline YAGO 4.5 [15,16] instance typing, loadable
  with owlready2/SPARQLWrapper [18] - and a loss/sufficiency/descope-vs-defer justification arguing why typing-only usage
  cannot break the FDR guarantee (unlike ontology-constraint filtering). PART C: a concrete LLM-as-probabilistic-reasoner
  design - ProbLog primary (verified API: get_evaluatable().create_from(PrologString).evaluate() -> {Term:prob}; p::fact.;
  annotated disjunctions; query/evidence; explain/MPE proofs [19,20,21]; LFI weight learning [22]; aProbLog semirings [23];
  DeepProbLog neural-predicate precedent [24]) with Bousi~Prolog/FASILL as the fuzzy-unification alternative [25,26,27,28];
  a certificate->probabilistic-weight mapping table (p_i=calibrate(Z_i); gate-consistent shrinkage (1-alpha_hat)*p_i [default]
  or per-pair W_i margin weight; entrapment FDP-hat as consistency prior; full cert kept at the leaf); a probabilistic trace-graph
  export (reuse Spec-B JSON/Graphviz-DOT, add a 'prob' attribute per node/edge, marginal per derived node, certificate per
  leaf; janus-swi solve/2 fallback for the proof DAG); and the exact deterministic->probabilistic upgrade swap (janus query_once
  -> problog get_evaluatable/evaluate). Deliverables: research_out.json + research_report.md with 30 primary sources, tables,
  recipes, exact APIs, and a positioning note mapping each part to the named reviewer gaps.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

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

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
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
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
