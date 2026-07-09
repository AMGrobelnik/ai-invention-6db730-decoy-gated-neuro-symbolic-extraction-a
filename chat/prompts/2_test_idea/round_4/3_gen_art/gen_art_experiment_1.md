# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: >-
  Power & De-Confound the Self-Consistency CLUTRR FDR Calibration Diagonal (iter-4 P1, headline)
summary: >-
  Execute the FULL ~593-doc self-consistency CLUTRR realized-FDR-vs-alpha calibration diagonal that iter-3 designed but only
  ran on a 40-doc checkpoint, so the primary disconfirmation and the marginal-exchangeability crux p-values move off the borderline
  (n >> the current 12-pair tail). For BOTH families (atomic, multi_hop) report the (target alpha, decoy_fdr_hat, realized
  FDR) triple across the full certified grid with doc-block-bootstrap CIs and the pre-registered self-report disconfirmation.
  Add a per-pair PAIRED-exchangeability statistic reported DISTINCTLY from the marginal win-rate AND computed across the four
  (Generator,Scorer) configs (incl. cross-family ministral-8b) so paired-layer de-circularization is evidenced not asserted.
  DE-CONFOUND the disconfirmation from extractor weakness/error-density by (a) a zero-API false-positive-density stratification
  of the paired statistic, and (b) a budget-gated STRONGER-EXTRACTOR arm that tests whether the per-pair sign-flip failure
  PERSISTS or VANISHES with a competent extractor. Power the S1b L0..L4 ladder to a stated false-pairs-per-rung floor or restate
  it as purely underpowered (deleting the contradicted 'detects only gross decoys' narrative). Reuse the tested OpenRouterClient
  + knockoff+ gate + fdr_stats/fdr_core from iter-3 P1 (art_sBLQqsdm3EIA) and iter-2 EXP2 (art_Inu52CyA49Ys); warm-start from
  their caches so only NEW docs cost money. CPU-only, async I/O, soft cap $4, HARD STOP $10, full figure captions, schema-valid
  method_out.json.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ## CONTEXT: 95% of this code already exists & is tested. This artifact SCALES + ADDS three things.
  ## Reuse workspace = iter_3/gen_art/gen_art_experiment_1 (art_sBLQqsdm3EIA, the P1 diagonal).
  ##   It already implements: extract_doc, gen_counterfactual_decoys, gen_swaps, gen_random_vocab,
  ##   gen_foreign_swap, score_portable(K=5 SC), score_verbalized, norm_pool, diagonal_for_family
  ##   (emits the (alpha,decoy_fdr_hat,realized) TRIPLE + self_report_anti_conservative + doc-block
  ##   bootstrap CI + swap_realized_fdr + plain_realized_fdr + a paired_exchangeability block),
  ##   analyze_crux (full+top50+top25 KS/MW/AD/perm + CDF overlays), analyze_s1b_ladder (L0..L4),
  ##   entrapment_analysis (Wen 2025 combined/paired r=1), primary_disconfirmation, collect_bh (BH q=0.05),
  ##   build_examples/build_output (schema exp_gen_sol_out), make_figures, power_table, selftest,
  ##   save_pipe_ckpt/load_pipe_ckpt, --selftest/--mini/--n-docs/--light/--full CLI.
  ##   fdr_stats.py: knockoff_plus_threshold(W,alpha)->(T,n_adm_pos,ratio); W_signed_max; rank_normalize;
  ##   doc_block_bootstrap(units,stat_fn,B,seed); ks_two_sample; mannwhitney; anderson_darling_2samp;
  ##   permutation_two_sample; tail_win_rate(pairs,thr)->(wr,n_tail); k_floor; benjamini_hochberg; empirical_cdf.
  ##   fdr_core.py: entrapment_fdp(N_T,N_E,r,estimator); plain_threshold_gate(Z,alpha)->(thr,adm_idx,est).
  ##   llm_client.py: OpenRouterClient(cache_dir,cost_log,concurrency,soft_cap,hard_stop,fallback_cache_dirs)
  ##   with exact usage.cost, disk cache keyed sha256(payload+sample_idx), $10 hard stop, parse_yes_conf.
  ## decoy_fdr_hat == knockoff+ `ratio` = (1+#{W<=-T})/max(1,#{W>=T}) -> already in each diagonal row.

  # ========================= PHASE 0  SETUP + WARM-START (no/low API) =========================
  COPY the full iter_3 P1 workspace tree into THIS workspace EXCEPT logs/ and method_out.json:
      method.py, fdr_stats.py, fdr_core.py, llm_client.py, pyproject.toml, figures helper.
  COPY prior caches to warm-start (only NEW docs then cost money):
      cp -r iter_3/.../gen_art_experiment_1/cache/*  ./cache/        # writable primary (190-prefix + 40-doc ckpt)
      set WARM_CACHES (read-only fallback) = [ iter_2/.../gen_art_experiment_2/cache,
                                                iter_3/.../gen_art_experiment_1/cache ]   # ministral (G,S) + SC prefix
  FRESH logs/cost.jsonl so the soft cap governs NEW spend only. export PYTHONHASHSEED=0.
  Set constants: SEED=20240617; ALPHA_GRID=[0.05,0.10,0.20,0.30,0.50] (k-floors {20,10,5,4,2});
      B_BOOT=2000; K_SC=5; N_FALSE_MIN=40; TAU=0.05; SOFT_CAP_USD=4.0; HARD_STOP_USD=10.0;
      PRIMARY_MODEL='openai/gpt-4.1-nano'; CROSS_SCORER='mistralai/ministral-8b-2512';
      STRONG_EXTRACTOR='openai/gpt-4.1-mini'  # de-confound arm (fallback 'openai/gpt-4.1' if budget allows).
  run `uv run method.py --selftest`  -> MUST pass all offline stat unit tests (knockoff+, _knockoff_fast==slow,
      bootstrap, BH, KS/MW/AD/perm) BEFORE any API call.

  # ========================= PHASE 1  SCALE THE CORPUS (regenerate data.py) =========================
  EDIT the dependency generator iter_1/.../gen_art_dataset_1/data.py counts (copy data.py + temp/datasets CSVs here):
      CONFIRM_COUNTS -> target ~593 confirmatory, k>=6 OVERSAMPLED, e.g.
          {2:30, 3:45, 4:60, 5:70, 6:88, 7:88, 8:82, 9:68, 10:62}  (sum=593)
      PILOT_COUNTS  -> enlarge so the S1b ladder is powerable, e.g.
          {2:8, 3:10, 4:14, 5:16, 6:18, 7:18, 8:16, 9:12, 10:10}  (sum=122)
      Keep seed 20240617 and the k-bucket sort(clutrr_id)+rng.shuffle so the ORIGINAL 190 ids remain a
      deterministic PREFIX-superset (this is what makes the warm cache hit). Crisp gold is enforced inside
      build_record (canonical simple-path: distinct entities==k+1, |atomic|==k, |multi_hop|==k-1, one proof
      root==query target) so integrity is auto-preserved.
  run `uv run data.py` -> ./full_data_out.json (the SCALED corpus). Pooled clean supply ~1345 rows, so 593+122
      is feasible; data.py logs a warning + takes min() if any k-bucket is short. READ BACK metadata: realized
      per-k counts, n_confirmatory, n_pilot. If realized total < ~500, that is fine for power (the 40-doc ckpt
      already had 287 spontaneous-false reals); record actual n. DO NOT fabricate docs to hit 593.

  # ========================= PHASE 2  PIPELINE RUN (gradual scaling, background, PID-managed) =========================
  MODIFY run()/extract_doc for OVER-GENERATION (densifies false positives, raises admission counts):
      add N_EXTRACT_SAMPLES=2 (config, default 2; 1 == legacy cache-identical fallback).
      For each doc: call extract_doc N_EXTRACT_SAMPLES times at temperature=0.7 (seed=SEED+s, sample_idx=s),
      UNION the per-pair predicted relations into a set of distinct (h,r,t) reals; label each via doc.label
      (TRUE / FALSE-spontaneous / UNDECIDABLE). Keep T=0.0 single-sample available as budget fallback.
      NOTE: T=0.7 over-gen breaks extraction cache-identity (cheap, 1-2 calls/doc) but SCORING cache still
      hits for any recurring claim; new wrong-relation claims score live.
  Pipeline order (unchanged structure, all in ONE async run() under the OpenRouterClient):
      1. EXTRACTION over all docs (over-gen union) -> reals_by_doc with labels; per-doc atomic P/R + multi_hop acc.
         LOG n_true / n_spontaneous_false / n_undecidable and the multi_hop extractor accuracy (the confound metric).
      2. DECOYS: gen_counterfactual_decoys (cf=L4 primary + cf2=L3, ONE batched call/doc, log contamination_rate=
         n_contam/n_gen) + gen_swaps (L1 random in-doc swap = anti-conservative control) for ALL docs;
         gen_random_vocab (L2) + gen_foreign_swap (L0 'fgn' + entrapment 'ent', deterministic foreign-name draw).
         Run cf/cf2/swap/entrapment on ALL docs; rv/fgn (ladder-only rungs) on the (enlarged) pilot+ladder subset.
      3. SCORING (isolated, provenance-blinded, order-randomized, document-prefix cached):
         SELF-CONSISTENCY (headline): score_portable (K=5, temp0.7, seed=SEED+i) over reals U cf U swap U ent
         (+ cf2/rv/fgn on ladder subset). VERBALIZED contrast: score_verbalized over reals U cf U swap (the
         documented discreteness/loose-target artifact, NOT a co-headline).
      Per-document rank-normalize via norm_pool (pool = reals U cf U swap, exactly the iter-2 pool) so the
      headline diagonal reconciles with prior iterations; one coherent Z-scale per (config).
  GRADUAL SCALING + cost discipline (avoid the iter-2 block-polling crash):
      `uv run method.py --mini`         # 3-doc smoke: pipeline + analysis end-to-end, asserts schema-valid out
      `uv run method.py --n-docs 40`    # reproduce the iter-3 checkpoint numbers from cache (~$0, sanity)
      `uv run method.py --n-docs 150`   # mid checkpoint; confirm power gate + cost trajectory
      `uv run method.py` (FULL) in BACKGROUND with PID: `uv run method.py & PID=$!`; poll `kill -0 $PID`;
         `tail -f logs/run.log & TAIL_PID=$!`. Log cumulative cost after EVERY call to logs/cost.jsonl.
         If cost crosses SOFT_CAP_USD=4 -> trigger budget fallback (see fallback_plan), never exceed $10.

  # ========================= PHASE 3  PER-FAMILY POWERED DIAGONAL + POWER GATE =========================
  for family in ['atomic','multi_hop','pooled']:
      diag[family] = diagonal_for_family(pipe, norm_sc, family, raw_conf=raw_sc)   # existing fn
      # each row already carries: target_alpha, decoy_fdr_hat, realized_fdr,
      #   triple_alpha_estimate_realized=[alpha,decoy_fdr_hat,realized], ci_low/ci_high (doc-block bootstrap B=2000),
      #   n_admitted, n_false_admitted, self_report_anti_conservative ((realized-decoy_fdr_hat)>TAU),
      #   k_floor, certified, populable, swap_realized_fdr, plain_realized_fdr, plain_est_fdr.
  POWER GATE (binding; pre-registered): a row's alpha is CERTIFIED only if n_admitted >= k_floor(alpha) AND the
      family is populable (n_false_total >= N_FALSE_MIN=40 genuine false reals). Any sub-floor alpha is reported
      as a PRECONDITION-not-met, NEVER 'confirmed by conservatism'. Record reachable_alpha_floor and
      alpha_star_permissive per family. EXPECTATION: multi_hop is the populable disconfirmation family.
  SELF-REPORT disconfirmation: surface every row where decoy_fdr_hat is anti-conservative vs realized beyond TAU
      (even when realized<alpha) as its own failure mode.

  # ========================= PHASE 4  POWERED CRUX (marginal exchangeability) =========================
  crux_sc = analyze_crux(pipe, norm_sc)   # full-distribution KS/MW/AD/permutation + admission-tail (top25/top50)
      two-sample tests on the SCALED multi_hop FALSE reals vs counterfactual decoys vs TRUE positives.
  Report, for the powered n (>> 12): whether the counterfactual-decoy distribution clearly FAILS-TO-REJECT vs the
      spontaneous-error distribution (marginal exchangeability HOLDS) or clearly REJECTS, with the p-values no
      longer borderline (~0.058-0.061 at n=12). Produce figure-ready overlaid empirical CDFs
      (decoy / spontaneous-error / true-positive) via empirical_cdf on a shared grid.
  Also run crux_vb under verbalized for the contrast.

  # ========================= PHASE 5 (NEW #1)  PAIRED STATISTIC, DISTINCT + ACROSS (G,S) =========================
  # (a) Already-present paired block in diagonal_for_family: paired_exchangeability = tail_win_rate over FALSE
  #     pairs at the most-permissive operative cutoff (alpha=0.50), with doc-block-bootstrap CI + ci_covers_half
  #     + ks_p_decoy_vs_real. Surface it under metadata.paired_vs_marginal with an EXPLICIT label that this is the
  #     PER-PAIR sign-flip statistic the knockoff+ theorems require, reported SEPARATELY from the MARGINAL
  #     win-rate/CDF tests in Phase 4 (the central finding: marginal can hold while paired fails).
  # (b) NEW function paired_exchangeability_across_GS(pipe):
       CONFIGS = [('nano','nano'), ('nano','ministral'), ('ministral','nano'), ('ministral','ministral')]
       # generator G picks WHICH decoy set (cf generated by nano vs by ministral); scorer S picks WHICH cached
       # Z-scores (SC by nano vs SC by ministral). Use the iter-2/iter-3 CACHED scores for the 190-doc PREFIX
       # where all four configs already exist (warm cache => ~$0). Extend to more docs ONLY if budget < soft cap.
       for (G,S) in CONFIGS:
          decoys = cf_by_doc generated with generator==G (regenerate decoys with model=G; nano cached, ministral
              cached from iter-2 de-circularization run); Z = SC scores under scorer==S (cached).
          rank-normalize per doc over reals U decoys(G) U swap on the S-scale; build false-real pairs;
          T = knockoff_plus_threshold(W_all, 0.50); wr_false = tail_win_rate over FALSE pairs at T;
          CI via doc_block_bootstrap(B=2000); record n_false_pairs.
          If n_false_pairs < PAIRED_FLOOR (=20) -> mark config UNDERPOWERED (report n, do not interpret).
       metadata.paired_across_GS = list of {G,S, paired_win_rate_false, ci, n_false_pairs, ci_covers_half, powered}.
       INTERPRET: if the PAIRED failure (win-rate clearly <0.5, CI excludes 0.5 OR realized FDR=1 at cutoff)
          persists across all 4 configs incl. cross-family ministral-8b -> paired-layer de-circularization is
          EVIDENCED (not a shared-model artifact). Else SOFTEN the claim to 'only marginal robustness to G!=S
          is demonstrated' (per S2b mandate). Carry the MARGINAL G!=S result forward as SETTLED (no new budget).

  # ========================= PHASE 6 (NEW #2)  DE-CONFOUND extractor strength / false-positive density =========================
  # Goal: distinguish 'knockoffs fundamentally do not transfer at the LLM boundary' (intrinsic) from
  # 'this single weak-extractor, error-dense regime is too noisy' (confound = nano multi_hop acc ~0.17, ~85% false).
  # (a) FREE density stratification (zero extra API): bin multi_hop FALSE pairs by chain length k into
  #     LOW (k in 2-3), MED (k in 4-6), HIGH (k in 7-10) -> a natural genuine-false-density gradient
  #     (~20% / ~50% / ~85% false among admitted reals, verified empirically per bin). For each bin compute the
  #     PAIRED per-pair sign-flip win-rate + realized FDR at the cutoff + doc-block CI. metadata.density_strata.
  #     If the paired failure PERSISTS across bins (esp. holds at LOW density) -> the failure is NOT merely
  #     error-density-driven. If it VANISHES at LOW density -> scope the limitation to the error-dense regime.
  # NOTE: the FULL extractor-strength x false-positive-density de-confound MATRIX is owned by the sibling iter-4
  #   artifact dir2 (reusing this same art_sBLQqsdm3EIA code). P1's job is the POWERED diagonal + paired-(G,S) + S1b;
  #   the FREE k-density stratification (6a) is P1's self-contained de-confound. The stronger-extractor arm (6b)
  #   below is an OPTIONAL preview only — run it solely if budget is ample AND dir2 has not already covered it;
  #   otherwise SKIP 6b (no duplicate spend) and cite dir2 for the full matrix.
  # (b) BUDGET-GATED STRONGER-EXTRACTOR arm (the decisive de-confound; run only if cost < $3 after Phase 5):
  #     Re-run EXTRACTION with STRONG_EXTRACTOR (gpt-4.1-mini) over the multi_hop family on the full corpus if
  #     affordable, else a powered subset (>=150 docs). KEEP the SCORER fixed at nano-SC (isolates the EXTRACTOR
  #     effect). Generate cf decoys for the new reals; score reals+decoys (nano-SC). Recompute, for this stronger
  #     extractor: multi_hop accuracy (expect lift from ~0.17), realized FDR vs alpha diagonal, decoy_fdr_hat,
  #     and the PAIRED win-rate at the cutoff. metadata.strong_extractor_arm = {extractor, n_docs, mh_acc,
  #     diagonal_rows, paired_win_rate, realized_fdr_at_alpha_star, verdict}.
  #     VERDICT logic (pre-registered): if paired sign-flip failure PERSISTS with the competent extractor ->
  #     'marginal != paired is a property of the LLM boundary' is EARNED (headline). If it VANISHES (gate now
  #     controls realized FDR <= alpha) -> report the POSITIVE result 'the gate controls FDR when the extractor
  #     can score its own errors' and SCOPE the limitation to the weak-scorer/error-dense regime. Either outcome
  #     is publishable; record which fired.

  # ========================= PHASE 7 (NEW #3)  S1b LADDER: power-or-bound =========================
  ladder = analyze_s1b_ladder(pipe) over LADDER=[L0_foreign_swap(fgn), L1_random_swap(swap), L2_random_vocab(rv),
      L3_cf_2nd(cf2), L4_cf_1st(cf)] scored under the SAME K=5 self-consistency.
  POWER it: score the rungs on the (enlarged ~122-doc) pilot UNION the first ~100 confirmatory docs until EACH
      rung has >= N_LADDER_FALSE_MIN=30 FALSE pairs (record realized n per rung). For each rung report tail
      win-rate over false pairs + KS/MW + doc-block CI + detected_anti_conservative flag.
  If a rung cannot reach the floor within budget -> report it PURELY as 'underpowered; cannot localize which decoy
      classes are detected; cannot certify paired validity' and DELETE the contradicted 'detects only gross decoys'
      narrative (iter-3 data showed L0 foreign-swap detected=FALSE while L1-L4 in-distribution=TRUE, the opposite).

  # ========================= PHASE 8  ENTRAPMENT + DISCONFIRMATION + BH + FIGURES + OUTPUT =========================
  for family,alpha in [(disconf_family, alpha_star), (disconf_family, 0.50)]:
      entrap[family,alpha] = entrapment_analysis(pipe, family, alpha)   # Wen 2025 combined bound
          FDP_hat = N_E*(1+1/r)/(N_T+N_E), r=1 (paired) at alpha* AND 0.50; report agreement with realized + decoy.
  verdict = primary_disconfirmation(pipe, norm_sc, diag['multi_hop'])  # DISCONFIRMED iff realized FDR exceeds
      operative alpha by > TAU AND the doc-block-bootstrap CI lies entirely on the anti-conservative side, under
      isolated self-consistency at adequate power; self-report additionally disconfirmed if decoy_fdr_hat anti-conservative.
  bh = collect_bh(diag_sc, ladder, crux_sc, crux_vb, entrap)            # BH q=0.05 across ALL validation tests.
  FIGURES (make_figures, extend captions to be FULL & self-contained):
      F1 per-family realized-FDR-vs-alpha DIAGONAL: method(cf) vs PLAIN-threshold vs SWAP, with doc-block CI bands,
         the 1/k minimum-estimable-FDR floor drawn, decoy_fdr_hat overlaid per alpha, certified cells marked.
      F2 CRUX overlaid CDFs (decoy / spontaneous-error / true-positive) with the PAIRED-win asymmetry annotated and
         the four-test (KS/MW/AD/perm) p-values in the caption (marginal-holds-while-paired-fails annotated).
      F3 PAIRED win-rate across the 4 (G,S) configs with CIs and the 0.5 line.
      F4 DE-CONFOUND: paired win-rate / realized FDR vs false-positive-density bins (+ stronger-extractor point).
      F5 S1b ladder L0..L4 win-rate + CIs with the per-rung false-pair n in the caption.
      Every caption states: 1/k floor, B=2000 doc-block bootstrap, the n it rests on, and the verdict it supports.
  build_output(pipe, analysis, out_path='method_out.json')  # schema exp_gen_sol_out: metadata{ all diagonals,
      power/populability table, triple per cell, self-report flags, marginal crux, PAIRED block + paired_across_GS,
      density_strata, strong_extractor_arm, S1b verdict, entrapment, BH table, primary-disconfirmation verdict,
      runtime+cost, full figure captions } + per-real examples (SC/VB Z, W, per-alpha admission predictions).
  VALIDATE with aii-json skill against exp_gen_sol_out; if >100MB use aii-file-size-limit to split. Write README.
  FINAL cost report from logs/cost.jsonl; assert < $10; figures/ populated; selftest still green.
fallback_plan: |-
  BUDGET (primary risk). The full over-generation SC scoring of ~593 docs minus the warm-cached 190-prefix is the main cost. Mitigations in priority order, each triggered when logs/cost.jsonl crosses SOFT_CAP_USD=$4: (1) drop N_EXTRACT_SAMPLES from 2 to 1 (legacy T=0.0 cache-identical extraction) — removes the live over-gen scoring; (2) cap the corpus at the largest n already scored (e.g. --n-docs 300) and report the realized n honestly as the power achieved — even ~300 docs gives >>40 genuine false reals, far above the 12-pair tail; (3) restrict the STRONGER-EXTRACTOR de-confound arm to a 150-doc powered subset, then to pilot-only, then SKIP it (the FREE k-density stratification still de-confounds error-density vs intrinsic-failure with zero API); (4) restrict the (G,S) paired analysis to the cached 190-prefix only (warm, ~$0) and mark wider configs underpowered; (5) restrict ladder/verbalized/entrapment to the pilot slice via the existing --light flag. HARD STOP at $10 is enforced inside OpenRouterClient (raises BudgetExceeded, caught, partial results still written schema-valid).

  DATA SUPPLY. If a k-bucket is short of the scaled CONFIRM_COUNTS (data.py logs the warning and takes min), accept the realized per-k counts; if total clean supply (~1345) cannot reach ~593 with k>=6 oversample, reduce the low-k counts first (keep the hard long-chain k>=6 emphasis) and record actual n. Do NOT relax the canonical simple-path crisp-gold constraint (that would poison the realized-FDR ground truth).

  DE-CONFOUND VANISHES vs PERSISTS — both are planned outcomes, not failures: if the paired sign-flip failure VANISHES with the stronger extractor or at LOW false-positive density, report the POSITIVE 'gate controls realized FDR at alpha when the extractor can score its own errors' and SCOPE the limitation to the weak-scorer/error-dense regime; if it PERSISTS across extractor strength and density, the 'marginal != paired at the LLM boundary' headline is earned. Pre-register both branches so the write-up is honest either way.

  UNDERPOWERED CRUX/LADDER. If even the full scaled run leaves a crux test or a ladder rung below its floor, report it as a PRECONDITION not met (underpowered, uninterpretable null) rather than as confirmation — this is exactly the Phase-0 power gate's job. The S1b rung that cannot reach 30 false pairs is reported purely as 'underpowered; cannot certify paired validity' with the contradicted 'gross-decoy' narrative deleted.

  CROSS-FAMILY MINISTRAL SCORES MISSING. If the warm cache does not contain ministral-8b scores for some prefix candidates (e.g. over-gen introduced new claims), compute the paired-(G,S) statistic ONLY on candidates present in all four configs and report n; do not score new ministral items unless budget allows. ministral has no logprobs, so it uses K=5 self-consistency (5 calls/item) — keep it cache-bound.

  STRONGER-EXTRACTOR MODEL CHOICE. Prefer openai/gpt-4.1-mini (cheap, strong multi-hop). If its multi-hop accuracy lift over nano is marginal (<0.15 absolute), escalate to openai/gpt-4.1 on a smaller subset; if neither lifts accuracy meaningfully, report that even a stronger extractor stays error-dense on long CLUTRR chains and treat the density stratification as the operative de-confound.

  RUNTIME/CRASH. Run the full job in BACKGROUND with PID management (never block-poll a long foreground run — that caused the iter-2 crash). save_pipe_ckpt/load_pipe_ckpt already checkpoint the scored pipe; on restart the disk cache + checkpoint make resumes free. Set RLIMIT_AS ~12GB; the bootstrap is vectorized (_knockoff_fast) so B=2000 over thousands of reals finishes in seconds.
testing_plan: |-
  Confirmation signals, smallest-first, before committing budget to the full run:

  1. OFFLINE UNIT TESTS (no API, must pass first): `uv run method.py --selftest`. Asserts knockoff_plus_threshold matches the Barber-Candes +1 definition, _knockoff_fast == the slow reference on random W, doc_block_bootstrap CI coverage, BH monotonicity, and KS/MW/AD/permutation sanity. Add one NEW assertion for paired_exchangeability_across_GS on synthetic pairs (win-rate 0.5 for exchangeable input, ->0 for real-always-wins input) and one for the k-density binning (correct k->bin map, monotone false-density). Green selftest is the gate to any API call.

  2. SCHEMA + PLUMBING: `uv run method.py --mini` (3 docs). Confirms the whole pipeline (extract -> decoys -> SC+VB scoring -> per-family diagonal -> crux -> paired -> ladder -> entrapment -> figures -> build_output) runs end-to-end and that method_out.json validates against exp_gen_sol_out via the aii-json skill. Inspect that each diagonal row carries the (alpha, decoy_fdr_hat, realized) triple and the self_report flag, and that metadata.paired_across_GS / density_strata / strong_extractor_arm keys exist (even if marked underpowered at n=3).

  3. WARM-CACHE / DETERMINISM CHECK: `uv run method.py --n-docs 40`. With the copied iter-3 cache this should reproduce the iter-3 checkpoint numbers (realized multi_hop FDR ~1.0 at alpha*=0.5, CI ~[0.66,1.0]; marginal crux p ~0.058-0.061; cf tail win-rate ~0.482) at NEAR-ZERO new cost (n_calls_live should be ~0, n_calls_cached/warm high). This is the load-bearing confirmation that the warm-start works and that scaling only pays for NEW docs. If live calls are high here, STOP and fix cache identity (PYTHONHASHSEED=0, prefix-superset id order, byte-identical prompts) before scaling.

  4. MID CHECKPOINT: `uv run method.py --n-docs 150` in background+PID. Watch logs/cost.jsonl: cost should rise only for docs 41..150 (the 190-prefix beyond 40 is also warm). Confirm the POWER GATE: does multi_hop reach N_FALSE_MIN=40 genuine false reals and >= k_floor admissions at one or more alphas? Confirm crux n is already well above 12 and p-values are moving off the borderline. Confirm the de-confound density bins each have a usable false-pair count. Project full-run cost from the 41..150 slope; if it would exceed $4, pre-apply a budget fallback before the full run.

  5. FULL RUN: `uv run method.py` (background, PID, tail the log). Success signals to verify in method_out.json: (i) both families have a certified-alpha grid with the triple + doc-block CIs; (ii) the primary-disconfirmation verdict fires (or not) at adequate power with non-borderline support; (iii) the marginal crux clearly fails-to-reject OR rejects (not p~0.06); (iv) paired_across_GS reports the per-pair win-rate for >=2 powered configs; (v) the de-confound shows whether the paired failure persists across density bins and (if run) the stronger extractor; (vi) the S1b ladder either meets the 30-false-pair floor per rung or is honestly labeled underpowered; (vii) BH table present; (viii) 5 figures with full captions; (ix) final cost < $10. Treat an underpowered tail/diagonal/ladder as a precondition-not-met outcome, never as confirmation-by-conservatism.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_XZyKy6QuwxrO
type: dataset
title: 'CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples'
summary: |-
  Standardized, deterministic CLUTRR-derived dataset that serves as the CRISP-GOLD calibration anchor for the neuro-symbolic text-to-logic hallucination-control experiment. Source: CLUTRR v1 (Sinha et al., EMNLP 2019, arXiv:1908.06177), pooled TEST splits of configs gen_train234_test2to10 (1048 rows) and gen_train23_test2to10 (1146 rows), fetched as raw CSVs from the kliang5/CLUTRR_huggingface_dataset GitHub mirror and staged in temp/datasets/. CLUTRR is rule-based/templated, so its kinship gold is exact (no annotation noise) — exactly the property needed to host the realized-FDR-vs-alpha calibration diagonal.

  SCALE & SHAPE: ONE dataset group 'CLUTRR-v1-CrispGold-CalibrationAnchor' with 190 examples (row == one CLUTRR story). 150 confirmatory + 40 disjoint pilot (metadata_is_pilot). Stratified over chain length k=2..10 oversampling long chains (k>=4): confirmatory k-dist {k2:12,k3:15,k4:20,k5:20,k6:20,k7:18,k8:18,k9:15,k10:12}; pilot {k2:5,k3:5,k4:5,k5:5,k6:5,k7:5,k8:5,k9:3,k10:2}. Seed 20240617; selected ids recorded in top-level metadata for reproducibility.

  SCHEMA (aii-json exp_sel_data_out; validated, plus an independent 190/190 integrity pass): each example has STRING input and output (JSON-serialized; parse with json.loads) plus flat metadata_* fields. input keys: doc_id, document_text (clean prose, [Name] brackets stripped, native length never padded), document_text_bracketed (raw for entity-span provenance), entities[{name,gender,type='person',node_index}], query{head,tail}. output keys: atomic_facts[{head,relation,tail}] = the k directly-stated chain edges (the 'too clean' atomic family); multi_hop_facts[{head,relation,tail,derived_from,path_len,is_query_target}] = the k-1 proof_state-derived inferred relations incl. the query target (the error-dense 'populable' family the primary disconfirmation is pre-registered on); multi_hop_query_target{head,relation,tail}; kinship_edge_graph{nodes[{index,name,gender}],edges[{src,dst,relation}]}. All facts use the shared {head,relation,tail} triple structure with kinship relation strings (a Re-DocRED anchor could reuse the same structure with Wikidata relations).

  PER-EXAMPLE METADATA: metadata_fold ('k2'..'k10'), metadata_chain_length_k, metadata_difficulty_split ('short' k<=3 / 'long' k>=4), metadata_f_comb, metadata_task_name, metadata_source_config, metadata_source_split, metadata_clutrr_id, metadata_is_pilot, metadata_n_atomic_facts, metadata_n_multi_hop_facts, metadata_document_char_length, metadata_proof_state_raw, metadata_noisy_story, metadata_atomic_crosscheck ('match'), metadata_namemap_method ('genders_order'), metadata_genders_order_valid, metadata_relation_vocab_version ('clutrr_kinship'). Top-level metadata also carries relation_vocabulary (20 observed kinship relations), full k-distributions, and selected confirmatory/pilot id lists.

  CRISPNESS GUARANTEE: all gold is derived 100% from CLUTRR's own structured fields (proof_state leaf triples = atomic; proof_state dict keys = multi-hop) with NO homegrown rule reimplementation. Restricted to canonical simple-path chains (distinct entities==k+1, distinct edges, |atomic|==k, |multi_hop|==k-1, exactly one proof root equal to the query target, genders-order node->name map reproduces the proof_state atomic leaves); 1345 of 2191 pooled rows qualified, giving ample per-stratum supply.

  SELECTION: CLUTRR is THE chosen dataset (target_num_datasets=1). Secondary candidate ProofWriter (tasksource/proofwriter, kept in temp/datasets/ as backup) was excluded — it provides T/F/Unknown answers over rule/fact theories, not the kinship atomic+multi-hop triple gold this experiment is registered on. OUT OF SCOPE here (left to the experiment artifact): decoy/entrapment generation, LLM scoring, FDR/precision/recall, Prolog execution, transitive-closure enrichment. Files: data.py (uv run data.py), full_data_out.json (1.1MB, <100MB so no split), mini_data_out.json (3 ex), preview_data_out.json (3 ex, truncated). Reproducible via pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_SLUbUUr6Ul98
type: research
title: 'Spec Sheet: Label-Free FDR Gate at the LLM Text-to-Logic Admission Boundary'
summary: >-
  Consolidated, source-traceable implementation spec for the label-free decoy-competition FDR gate that admits LLM-extracted
  facts/bridges into a Prolog/symbolic layer. Provides, for each component, a verbatim formula (with equation number and source),
  a symbol glossary, a language-agnostic pseudo-procedure, and a recommended default. KEY RESULTS: (A) knockoff+ admission
  threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha} (Barber-Candes eq 1.9, exact FDR via Thm 2; plain knockoff eq
  1.8 controls only modified FDR Thm 1); the minimum-estimable-FDR floor is 1/k, so certifying FDR<=alpha needs k>=ceil(1/alpha)
  admissions -> demonstrable alpha grid {0.05,0.1,0.2,0.3,0.5} maps to k-floors {20,10,5,4,2}. Rajchert-Keich prove the '+1'
  is generally necessary (t=1 optimal), so keep it; TDC-SB/TDC-UB (bandsfdp) are an optional tighter FDX bound. (B) Entrapment
  estimators verbatim from Wen et al. 2025: combined FDP=N_E(1+1/r)/(N_T+N_E) (upper bound, DEFAULT), paired (eq4, requires
  r=1, tighter), lower bound N_E/(N_T+N_E) (failure-only), and 'sample' N_E(1/r)/N_T which is INVALID (biased). r=#entrapment/#target;
  default r=1 paired. (C) Document-block (cluster) bootstrap B>=2000 for all FDP/FDR CIs (resample whole documents; Cameron-Gelbach-Miller
  anchor) — the CI used by the primary disconfirmation. (D) Sole validity condition = Barber-Candes Lemma 1 (null W signs
  are i.i.d. fair coins) = TDC equal-chance; two anti-conservative failure modes (within-doc correlation -> bootstrap; batched
  contrast effect -> isolated provenance-blinded order-randomized scoring) and the isolated-vs-batched discriminator. (E)
  Property-matched document-conditioned COUNTERFACTUAL decoys + non-entailment verification (DeepCoy principle; DOE 0.166->0.032/0.109->0.038);
  random type-matched swaps kept as the anti-conservative negative control. (F) Ranked label-free upper-tail elicitation shortlist:
  DINCO (primary, overconfidence-corrected), FactSelfCheck (fact-level), self-consistency/SelfCheckGPT, logprob/yes-no-token
  (if exposed), verbalized (overconfident floor); Phase-0 selects on tail-AUC>0.5 with CI + isolated~batched agreement. (G)
  Recommended model openai/gpt-4.1-nano ($0.10/$0.40 per M, logprobs+auto-caching, <$0.30 input); fallbacks gpt-4o-mini then
  a logprob-free cheap caching model; projected cost ~$1-3 << $10 cap. (H) Novelty confirmed: no prior work applies knockoff/target-decoy/entrapment
  FDR at a label-free LLM text->logic admission boundary (conformal factuality/selection are labeled and certify outputs).
  Includes a final Parameter Defaults table and runtime follow-ups (probe logprobs non-null; confirm cached_tokens>0).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_1
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

### [3] SYSTEM-USER prompt · 2026-06-16 12:03:07 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: >-
  Power & De-Confound the Self-Consistency CLUTRR FDR Calibration Diagonal (iter-4 P1, headline)
summary: >-
  Execute the FULL ~593-doc self-consistency CLUTRR realized-FDR-vs-alpha calibration diagonal that iter-3 designed but only
  ran on a 40-doc checkpoint, so the primary disconfirmation and the marginal-exchangeability crux p-values move off the borderline
  (n >> the current 12-pair tail). For BOTH families (atomic, multi_hop) report the (target alpha, decoy_fdr_hat, realized
  FDR) triple across the full certified grid with doc-block-bootstrap CIs and the pre-registered self-report disconfirmation.
  Add a per-pair PAIRED-exchangeability statistic reported DISTINCTLY from the marginal win-rate AND computed across the four
  (Generator,Scorer) configs (incl. cross-family ministral-8b) so paired-layer de-circularization is evidenced not asserted.
  DE-CONFOUND the disconfirmation from extractor weakness/error-density by (a) a zero-API false-positive-density stratification
  of the paired statistic, and (b) a budget-gated STRONGER-EXTRACTOR arm that tests whether the per-pair sign-flip failure
  PERSISTS or VANISHES with a competent extractor. Power the S1b L0..L4 ladder to a stated false-pairs-per-rung floor or restate
  it as purely underpowered (deleting the contradicted 'detects only gross decoys' narrative). Reuse the tested OpenRouterClient
  + knockoff+ gate + fdr_stats/fdr_core from iter-3 P1 (art_sBLQqsdm3EIA) and iter-2 EXP2 (art_Inu52CyA49Ys); warm-start from
  their caches so only NEW docs cost money. CPU-only, async I/O, soft cap $4, HARD STOP $10, full figure captions, schema-valid
  method_out.json.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ## CONTEXT: 95% of this code already exists & is tested. This artifact SCALES + ADDS three things.
  ## Reuse workspace = iter_3/gen_art/gen_art_experiment_1 (art_sBLQqsdm3EIA, the P1 diagonal).
  ##   It already implements: extract_doc, gen_counterfactual_decoys, gen_swaps, gen_random_vocab,
  ##   gen_foreign_swap, score_portable(K=5 SC), score_verbalized, norm_pool, diagonal_for_family
  ##   (emits the (alpha,decoy_fdr_hat,realized) TRIPLE + self_report_anti_conservative + doc-block
  ##   bootstrap CI + swap_realized_fdr + plain_realized_fdr + a paired_exchangeability block),
  ##   analyze_crux (full+top50+top25 KS/MW/AD/perm + CDF overlays), analyze_s1b_ladder (L0..L4),
  ##   entrapment_analysis (Wen 2025 combined/paired r=1), primary_disconfirmation, collect_bh (BH q=0.05),
  ##   build_examples/build_output (schema exp_gen_sol_out), make_figures, power_table, selftest,
  ##   save_pipe_ckpt/load_pipe_ckpt, --selftest/--mini/--n-docs/--light/--full CLI.
  ##   fdr_stats.py: knockoff_plus_threshold(W,alpha)->(T,n_adm_pos,ratio); W_signed_max; rank_normalize;
  ##   doc_block_bootstrap(units,stat_fn,B,seed); ks_two_sample; mannwhitney; anderson_darling_2samp;
  ##   permutation_two_sample; tail_win_rate(pairs,thr)->(wr,n_tail); k_floor; benjamini_hochberg; empirical_cdf.
  ##   fdr_core.py: entrapment_fdp(N_T,N_E,r,estimator); plain_threshold_gate(Z,alpha)->(thr,adm_idx,est).
  ##   llm_client.py: OpenRouterClient(cache_dir,cost_log,concurrency,soft_cap,hard_stop,fallback_cache_dirs)
  ##   with exact usage.cost, disk cache keyed sha256(payload+sample_idx), $10 hard stop, parse_yes_conf.
  ## decoy_fdr_hat == knockoff+ `ratio` = (1+#{W<=-T})/max(1,#{W>=T}) -> already in each diagonal row.

  # ========================= PHASE 0  SETUP + WARM-START (no/low API) =========================
  COPY the full iter_3 P1 workspace tree into THIS workspace EXCEPT logs/ and method_out.json:
      method.py, fdr_stats.py, fdr_core.py, llm_client.py, pyproject.toml, figures helper.
  COPY prior caches to warm-start (only NEW docs then cost money):
      cp -r iter_3/.../gen_art_experiment_1/cache/*  ./cache/        # writable primary (190-prefix + 40-doc ckpt)
      set WARM_CACHES (read-only fallback) = [ iter_2/.../gen_art_experiment_2/cache,
                                                iter_3/.../gen_art_experiment_1/cache ]   # ministral (G,S) + SC prefix
  FRESH logs/cost.jsonl so the soft cap governs NEW spend only. export PYTHONHASHSEED=0.
  Set constants: SEED=20240617; ALPHA_GRID=[0.05,0.10,0.20,0.30,0.50] (k-floors {20,10,5,4,2});
      B_BOOT=2000; K_SC=5; N_FALSE_MIN=40; TAU=0.05; SOFT_CAP_USD=4.0; HARD_STOP_USD=10.0;
      PRIMARY_MODEL='openai/gpt-4.1-nano'; CROSS_SCORER='mistralai/ministral-8b-2512';
      STRONG_EXTRACTOR='openai/gpt-4.1-mini'  # de-confound arm (fallback 'openai/gpt-4.1' if budget allows).
  run `uv run method.py --selftest`  -> MUST pass all offline stat unit tests (knockoff+, _knockoff_fast==slow,
      bootstrap, BH, KS/MW/AD/perm) BEFORE any API call.

  # ========================= PHASE 1  SCALE THE CORPUS (regenerate data.py) =========================
  EDIT the dependency generator iter_1/.../gen_art_dataset_1/data.py counts (copy data.py + temp/datasets CSVs here):
      CONFIRM_COUNTS -> target ~593 confirmatory, k>=6 OVERSAMPLED, e.g.
          {2:30, 3:45, 4:60, 5:70, 6:88, 7:88, 8:82, 9:68, 10:62}  (sum=593)
      PILOT_COUNTS  -> enlarge so the S1b ladder is powerable, e.g.
          {2:8, 3:10, 4:14, 5:16, 6:18, 7:18, 8:16, 9:12, 10:10}  (sum=122)
      Keep seed 20240617 and the k-bucket sort(clutrr_id)+rng.shuffle so the ORIGINAL 190 ids remain a
      deterministic PREFIX-superset (this is what makes the warm cache hit). Crisp gold is enforced inside
      build_record (canonical simple-path: distinct entities==k+1, |atomic|==k, |multi_hop|==k-1, one proof
      root==query target) so integrity is auto-preserved.
  run `uv run data.py` -> ./full_data_out.json (the SCALED corpus). Pooled clean supply ~1345 rows, so 593+122
      is feasible; data.py logs a warning + takes min() if any k-bucket is short. READ BACK metadata: realized
      per-k counts, n_confirmatory, n_pilot. If realized total < ~500, that is fine for power (the 40-doc ckpt
      already had 287 spontaneous-false reals); record actual n. DO NOT fabricate docs to hit 593.

  # ========================= PHASE 2  PIPELINE RUN (gradual scaling, background, PID-managed) =========================
  MODIFY run()/extract_doc for OVER-GENERATION (densifies false positives, raises admission counts):
      add N_EXTRACT_SAMPLES=2 (config, default 2; 1 == legacy cache-identical fallback).
      For each doc: call extract_doc N_EXTRACT_SAMPLES times at temperature=0.7 (seed=SEED+s, sample_idx=s),
      UNION the per-pair predicted relations into a set of distinct (h,r,t) reals; label each via doc.label
      (TRUE / FALSE-spontaneous / UNDECIDABLE). Keep T=0.0 single-sample available as budget fallback.
      NOTE: T=0.7 over-gen breaks extraction cache-identity (cheap, 1-2 calls/doc) but SCORING cache still
      hits for any recurring claim; new wrong-relation claims score live.
  Pipeline order (unchanged structure, all in ONE async run() under the OpenRouterClient):
      1. EXTRACTION over all docs (over-gen union) -> reals_by_doc with labels; per-doc atomic P/R + multi_hop acc.
         LOG n_true / n_spontaneous_false / n_undecidable and the multi_hop extractor accuracy (the confound metric).
      2. DECOYS: gen_counterfactual_decoys (cf=L4 primary + cf2=L3, ONE batched call/doc, log contamination_rate=
         n_contam/n_gen) + gen_swaps (L1 random in-doc swap = anti-conservative control) for ALL docs;
         gen_random_vocab (L2) + gen_foreign_swap (L0 'fgn' + entrapment 'ent', deterministic foreign-name draw).
         Run cf/cf2/swap/entrapment on ALL docs; rv/fgn (ladder-only rungs) on the (enlarged) pilot+ladder subset.
      3. SCORING (isolated, provenance-blinded, order-randomized, document-prefix cached):
         SELF-CONSISTENCY (headline): score_portable (K=5, temp0.7, seed=SEED+i) over reals U cf U swap U ent
         (+ cf2/rv/fgn on ladder subset). VERBALIZED contrast: score_verbalized over reals U cf U swap (the
         documented discreteness/loose-target artifact, NOT a co-headline).
      Per-document rank-normalize via norm_pool (pool = reals U cf U swap, exactly the iter-2 pool) so the
      headline diagonal reconciles with prior iterations; one coherent Z-scale per (config).
  GRADUAL SCALING + cost discipline (avoid the iter-2 block-polling crash):
      `uv run method.py --mini`         # 3-doc smoke: pipeline + analysis end-to-end, asserts schema-valid out
      `uv run method.py --n-docs 40`    # reproduce the iter-3 checkpoint numbers from cache (~$0, sanity)
      `uv run method.py --n-docs 150`   # mid checkpoint; confirm power gate + cost trajectory
      `uv run method.py` (FULL) in BACKGROUND with PID: `uv run method.py & PID=$!`; poll `kill -0 $PID`;
         `tail -f logs/run.log & TAIL_PID=$!`. Log cumulative cost after EVERY call to logs/cost.jsonl.
         If cost crosses SOFT_CAP_USD=4 -> trigger budget fallback (see fallback_plan), never exceed $10.

  # ========================= PHASE 3  PER-FAMILY POWERED DIAGONAL + POWER GATE =========================
  for family in ['atomic','multi_hop','pooled']:
      diag[family] = diagonal_for_family(pipe, norm_sc, family, raw_conf=raw_sc)   # existing fn
      # each row already carries: target_alpha, decoy_fdr_hat, realized_fdr,
      #   triple_alpha_estimate_realized=[alpha,decoy_fdr_hat,realized], ci_low/ci_high (doc-block bootstrap B=2000),
      #   n_admitted, n_false_admitted, self_report_anti_conservative ((realized-decoy_fdr_hat)>TAU),
      #   k_floor, certified, populable, swap_realized_fdr, plain_realized_fdr, plain_est_fdr.
  POWER GATE (binding; pre-registered): a row's alpha is CERTIFIED only if n_admitted >= k_floor(alpha) AND the
      family is populable (n_false_total >= N_FALSE_MIN=40 genuine false reals). Any sub-floor alpha is reported
      as a PRECONDITION-not-met, NEVER 'confirmed by conservatism'. Record reachable_alpha_floor and
      alpha_star_permissive per family. EXPECTATION: multi_hop is the populable disconfirmation family.
  SELF-REPORT disconfirmation: surface every row where decoy_fdr_hat is anti-conservative vs realized beyond TAU
      (even when realized<alpha) as its own failure mode.

  # ========================= PHASE 4  POWERED CRUX (marginal exchangeability) =========================
  crux_sc = analyze_crux(pipe, norm_sc)   # full-distribution KS/MW/AD/permutation + admission-tail (top25/top50)
      two-sample tests on the SCALED multi_hop FALSE reals vs counterfactual decoys vs TRUE positives.
  Report, for the powered n (>> 12): whether the counterfactual-decoy distribution clearly FAILS-TO-REJECT vs the
      spontaneous-error distribution (marginal exchangeability HOLDS) or clearly REJECTS, with the p-values no
      longer borderline (~0.058-0.061 at n=12). Produce figure-ready overlaid empirical CDFs
      (decoy / spontaneous-error / true-positive) via empirical_cdf on a shared grid.
  Also run crux_vb under verbalized for the contrast.

  # ========================= PHASE 5 (NEW #1)  PAIRED STATISTIC, DISTINCT + ACROSS (G,S) =========================
  # (a) Already-present paired block in diagonal_for_family: paired_exchangeability = tail_win_rate over FALSE
  #     pairs at the most-permissive operative cutoff (alpha=0.50), with doc-block-bootstrap CI + ci_covers_half
  #     + ks_p_decoy_vs_real. Surface it under metadata.paired_vs_marginal with an EXPLICIT label that this is the
  #     PER-PAIR sign-flip statistic the knockoff+ theorems require, reported SEPARATELY from the MARGINAL
  #     win-rate/CDF tests in Phase 4 (the central finding: marginal can hold while paired fails).
  # (b) NEW function paired_exchangeability_across_GS(pipe):
       CONFIGS = [('nano','nano'), ('nano','ministral'), ('ministral','nano'), ('ministral','ministral')]
       # generator G picks WHICH decoy set (cf generated by nano vs by ministral); scorer S picks WHICH cached
       # Z-scores (SC by nano vs SC by ministral). Use the iter-2/iter-3 CACHED scores for the 190-doc PREFIX
       # where all four configs already exist (warm cache => ~$0). Extend to more docs ONLY if budget < soft cap.
       for (G,S) in CONFIGS:
          decoys = cf_by_doc generated with generator==G (regenerate decoys with model=G; nano cached, ministral
              cached from iter-2 de-circularization run); Z = SC scores under scorer==S (cached).
          rank-normalize per doc over reals U decoys(G) U swap on the S-scale; build false-real pairs;
          T = knockoff_plus_threshold(W_all, 0.50); wr_false = tail_win_rate over FALSE pairs at T;
          CI via doc_block_bootstrap(B=2000); record n_false_pairs.
          If n_false_pairs < PAIRED_FLOOR (=20) -> mark config UNDERPOWERED (report n, do not interpret).
       metadata.paired_across_GS = list of {G,S, paired_win_rate_false, ci, n_false_pairs, ci_covers_half, powered}.
       INTERPRET: if the PAIRED failure (win-rate clearly <0.5, CI excludes 0.5 OR realized FDR=1 at cutoff)
          persists across all 4 configs incl. cross-family ministral-8b -> paired-layer de-circularization is
          EVIDENCED (not a shared-model artifact). Else SOFTEN the claim to 'only marginal robustness to G!=S
          is demonstrated' (per S2b mandate). Carry the MARGINAL G!=S result forward as SETTLED (no new budget).

  # ========================= PHASE 6 (NEW #2)  DE-CONFOUND extractor strength / false-positive density =========================
  # Goal: distinguish 'knockoffs fundamentally do not transfer at the LLM boundary' (intrinsic) from
  # 'this single weak-extractor, error-dense regime is too noisy' (confound = nano multi_hop acc ~0.17, ~85% false).
  # (a) FREE density stratification (zero extra API): bin multi_hop FALSE pairs by chain length k into
  #     LOW (k in 2-3), MED (k in 4-6), HIGH (k in 7-10) -> a natural genuine-false-density gradient
  #     (~20% / ~50% / ~85% false among admitted reals, verified empirically per bin). For each bin compute the
  #     PAIRED per-pair sign-flip win-rate + realized FDR at the cutoff + doc-block CI. metadata.density_strata.
  #     If the paired failure PERSISTS across bins (esp. holds at LOW density) -> the failure is NOT merely
  #     error-density-driven. If it VANISHES at LOW density -> scope the limitation to the error-dense regime.
  # NOTE: the FULL extractor-strength x false-positive-density de-confound MATRIX is owned by the sibling iter-4
  #   artifact dir2 (reusing this same art_sBLQqsdm3EIA code). P1's job is the POWERED diagonal + paired-(G,S) + S1b;
  #   the FREE k-density stratification (6a) is P1's self-contained de-confound. The stronger-extractor arm (6b)
  #   below is an OPTIONAL preview only — run it solely if budget is ample AND dir2 has not already covered it;
  #   otherwise SKIP 6b (no duplicate spend) and cite dir2 for the full matrix.
  # (b) BUDGET-GATED STRONGER-EXTRACTOR arm (the decisive de-confound; run only if cost < $3 after Phase 5):
  #     Re-run EXTRACTION with STRONG_EXTRACTOR (gpt-4.1-mini) over the multi_hop family on the full corpus if
  #     affordable, else a powered subset (>=150 docs). KEEP the SCORER fixed at nano-SC (isolates the EXTRACTOR
  #     effect). Generate cf decoys for the new reals; score reals+decoys (nano-SC). Recompute, for this stronger
  #     extractor: multi_hop accuracy (expect lift from ~0.17), realized FDR vs alpha diagonal, decoy_fdr_hat,
  #     and the PAIRED win-rate at the cutoff. metadata.strong_extractor_arm = {extractor, n_docs, mh_acc,
  #     diagonal_rows, paired_win_rate, realized_fdr_at_alpha_star, verdict}.
  #     VERDICT logic (pre-registered): if paired sign-flip failure PERSISTS with the competent extractor ->
  #     'marginal != paired is a property of the LLM boundary' is EARNED (headline). If it VANISHES (gate now
  #     controls realized FDR <= alpha) -> report the POSITIVE result 'the gate controls FDR when the extractor
  #     can score its own errors' and SCOPE the limitation to the weak-scorer/error-dense regime. Either outcome
  #     is publishable; record which fired.

  # ========================= PHASE 7 (NEW #3)  S1b LADDER: power-or-bound =========================
  ladder = analyze_s1b_ladder(pipe) over LADDER=[L0_foreign_swap(fgn), L1_random_swap(swap), L2_random_vocab(rv),
      L3_cf_2nd(cf2), L4_cf_1st(cf)] scored under the SAME K=5 self-consistency.
  POWER it: score the rungs on the (enlarged ~122-doc) pilot UNION the first ~100 confirmatory docs until EACH
      rung has >= N_LADDER_FALSE_MIN=30 FALSE pairs (record realized n per rung). For each rung report tail
      win-rate over false pairs + KS/MW + doc-block CI + detected_anti_conservative flag.
  If a rung cannot reach the floor within budget -> report it PURELY as 'underpowered; cannot localize which decoy
      classes are detected; cannot certify paired validity' and DELETE the contradicted 'detects only gross decoys'
      narrative (iter-3 data showed L0 foreign-swap detected=FALSE while L1-L4 in-distribution=TRUE, the opposite).

  # ========================= PHASE 8  ENTRAPMENT + DISCONFIRMATION + BH + FIGURES + OUTPUT =========================
  for family,alpha in [(disconf_family, alpha_star), (disconf_family, 0.50)]:
      entrap[family,alpha] = entrapment_analysis(pipe, family, alpha)   # Wen 2025 combined bound
          FDP_hat = N_E*(1+1/r)/(N_T+N_E), r=1 (paired) at alpha* AND 0.50; report agreement with realized + decoy.
  verdict = primary_disconfirmation(pipe, norm_sc, diag['multi_hop'])  # DISCONFIRMED iff realized FDR exceeds
      operative alpha by > TAU AND the doc-block-bootstrap CI lies entirely on the anti-conservative side, under
      isolated self-consistency at adequate power; self-report additionally disconfirmed if decoy_fdr_hat anti-conservative.
  bh = collect_bh(diag_sc, ladder, crux_sc, crux_vb, entrap)            # BH q=0.05 across ALL validation tests.
  FIGURES (make_figures, extend captions to be FULL & self-contained):
      F1 per-family realized-FDR-vs-alpha DIAGONAL: method(cf) vs PLAIN-threshold vs SWAP, with doc-block CI bands,
         the 1/k minimum-estimable-FDR floor drawn, decoy_fdr_hat overlaid per alpha, certified cells marked.
      F2 CRUX overlaid CDFs (decoy / spontaneous-error / true-positive) with the PAIRED-win asymmetry annotated and
         the four-test (KS/MW/AD/perm) p-values in the caption (marginal-holds-while-paired-fails annotated).
      F3 PAIRED win-rate across the 4 (G,S) configs with CIs and the 0.5 line.
      F4 DE-CONFOUND: paired win-rate / realized FDR vs false-positive-density bins (+ stronger-extractor point).
      F5 S1b ladder L0..L4 win-rate + CIs with the per-rung false-pair n in the caption.
      Every caption states: 1/k floor, B=2000 doc-block bootstrap, the n it rests on, and the verdict it supports.
  build_output(pipe, analysis, out_path='method_out.json')  # schema exp_gen_sol_out: metadata{ all diagonals,
      power/populability table, triple per cell, self-report flags, marginal crux, PAIRED block + paired_across_GS,
      density_strata, strong_extractor_arm, S1b verdict, entrapment, BH table, primary-disconfirmation verdict,
      runtime+cost, full figure captions } + per-real examples (SC/VB Z, W, per-alpha admission predictions).
  VALIDATE with aii-json skill against exp_gen_sol_out; if >100MB use aii-file-size-limit to split. Write README.
  FINAL cost report from logs/cost.jsonl; assert < $10; figures/ populated; selftest still green.
fallback_plan: |-
  BUDGET (primary risk). The full over-generation SC scoring of ~593 docs minus the warm-cached 190-prefix is the main cost. Mitigations in priority order, each triggered when logs/cost.jsonl crosses SOFT_CAP_USD=$4: (1) drop N_EXTRACT_SAMPLES from 2 to 1 (legacy T=0.0 cache-identical extraction) — removes the live over-gen scoring; (2) cap the corpus at the largest n already scored (e.g. --n-docs 300) and report the realized n honestly as the power achieved — even ~300 docs gives >>40 genuine false reals, far above the 12-pair tail; (3) restrict the STRONGER-EXTRACTOR de-confound arm to a 150-doc powered subset, then to pilot-only, then SKIP it (the FREE k-density stratification still de-confounds error-density vs intrinsic-failure with zero API); (4) restrict the (G,S) paired analysis to the cached 190-prefix only (warm, ~$0) and mark wider configs underpowered; (5) restrict ladder/verbalized/entrapment to the pilot slice via the existing --light flag. HARD STOP at $10 is enforced inside OpenRouterClient (raises BudgetExceeded, caught, partial results still written schema-valid).

  DATA SUPPLY. If a k-bucket is short of the scaled CONFIRM_COUNTS (data.py logs the warning and takes min), accept the realized per-k counts; if total clean supply (~1345) cannot reach ~593 with k>=6 oversample, reduce the low-k counts first (keep the hard long-chain k>=6 emphasis) and record actual n. Do NOT relax the canonical simple-path crisp-gold constraint (that would poison the realized-FDR ground truth).

  DE-CONFOUND VANISHES vs PERSISTS — both are planned outcomes, not failures: if the paired sign-flip failure VANISHES with the stronger extractor or at LOW false-positive density, report the POSITIVE 'gate controls realized FDR at alpha when the extractor can score its own errors' and SCOPE the limitation to the weak-scorer/error-dense regime; if it PERSISTS across extractor strength and density, the 'marginal != paired at the LLM boundary' headline is earned. Pre-register both branches so the write-up is honest either way.

  UNDERPOWERED CRUX/LADDER. If even the full scaled run leaves a crux test or a ladder rung below its floor, report it as a PRECONDITION not met (underpowered, uninterpretable null) rather than as confirmation — this is exactly the Phase-0 power gate's job. The S1b rung that cannot reach 30 false pairs is reported purely as 'underpowered; cannot certify paired validity' with the contradicted 'gross-decoy' narrative deleted.

  CROSS-FAMILY MINISTRAL SCORES MISSING. If the warm cache does not contain ministral-8b scores for some prefix candidates (e.g. over-gen introduced new claims), compute the paired-(G,S) statistic ONLY on candidates present in all four configs and report n; do not score new ministral items unless budget allows. ministral has no logprobs, so it uses K=5 self-consistency (5 calls/item) — keep it cache-bound.

  STRONGER-EXTRACTOR MODEL CHOICE. Prefer openai/gpt-4.1-mini (cheap, strong multi-hop). If its multi-hop accuracy lift over nano is marginal (<0.15 absolute), escalate to openai/gpt-4.1 on a smaller subset; if neither lifts accuracy meaningfully, report that even a stronger extractor stays error-dense on long CLUTRR chains and treat the density stratification as the operative de-confound.

  RUNTIME/CRASH. Run the full job in BACKGROUND with PID management (never block-poll a long foreground run — that caused the iter-2 crash). save_pipe_ckpt/load_pipe_ckpt already checkpoint the scored pipe; on restart the disk cache + checkpoint make resumes free. Set RLIMIT_AS ~12GB; the bootstrap is vectorized (_knockoff_fast) so B=2000 over thousands of reals finishes in seconds.
testing_plan: |-
  Confirmation signals, smallest-first, before committing budget to the full run:

  1. OFFLINE UNIT TESTS (no API, must pass first): `uv run method.py --selftest`. Asserts knockoff_plus_threshold matches the Barber-Candes +1 definition, _knockoff_fast == the slow reference on random W, doc_block_bootstrap CI coverage, BH monotonicity, and KS/MW/AD/permutation sanity. Add one NEW assertion for paired_exchangeability_across_GS on synthetic pairs (win-rate 0.5 for exchangeable input, ->0 for real-always-wins input) and one for the k-density binning (correct k->bin map, monotone false-density). Green selftest is the gate to any API call.

  2. SCHEMA + PLUMBING: `uv run method.py --mini` (3 docs). Confirms the whole pipeline (extract -> decoys -> SC+VB scoring -> per-family diagonal -> crux -> paired -> ladder -> entrapment -> figures -> build_output) runs end-to-end and that method_out.json validates against exp_gen_sol_out via the aii-json skill. Inspect that each diagonal row carries the (alpha, decoy_fdr_hat, realized) triple and the self_report flag, and that metadata.paired_across_GS / density_strata / strong_extractor_arm keys exist (even if marked underpowered at n=3).

  3. WARM-CACHE / DETERMINISM CHECK: `uv run method.py --n-docs 40`. With the copied iter-3 cache this should reproduce the iter-3 checkpoint numbers (realized multi_hop FDR ~1.0 at alpha*=0.5, CI ~[0.66,1.0]; marginal crux p ~0.058-0.061; cf tail win-rate ~0.482) at NEAR-ZERO new cost (n_calls_live should be ~0, n_calls_cached/warm high). This is the load-bearing confirmation that the warm-start works and that scaling only pays for NEW docs. If live calls are high here, STOP and fix cache identity (PYTHONHASHSEED=0, prefix-superset id order, byte-identical prompts) before scaling.

  4. MID CHECKPOINT: `uv run method.py --n-docs 150` in background+PID. Watch logs/cost.jsonl: cost should rise only for docs 41..150 (the 190-prefix beyond 40 is also warm). Confirm the POWER GATE: does multi_hop reach N_FALSE_MIN=40 genuine false reals and >= k_floor admissions at one or more alphas? Confirm crux n is already well above 12 and p-values are moving off the borderline. Confirm the de-confound density bins each have a usable false-pair count. Project full-run cost from the 41..150 slope; if it would exceed $4, pre-apply a budget fallback before the full run.

  5. FULL RUN: `uv run method.py` (background, PID, tail the log). Success signals to verify in method_out.json: (i) both families have a certified-alpha grid with the triple + doc-block CIs; (ii) the primary-disconfirmation verdict fires (or not) at adequate power with non-borderline support; (iii) the marginal crux clearly fails-to-reject OR rejects (not p~0.06); (iv) paired_across_GS reports the per-pair win-rate for >=2 powered configs; (v) the de-confound shows whether the paired failure persists across density bins and (if run) the stronger extractor; (vi) the S1b ladder either meets the 30-false-pair floor per rung or is honestly labeled underpowered; (vii) BH table present; (viii) 5 figures with full captions; (ix) final cost < $10. Treat an underpowered tail/diagonal/ladder as a precondition-not-met outcome, never as confirmation-by-conservatism.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_XZyKy6QuwxrO
type: dataset
title: 'CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples'
summary: |-
  Standardized, deterministic CLUTRR-derived dataset that serves as the CRISP-GOLD calibration anchor for the neuro-symbolic text-to-logic hallucination-control experiment. Source: CLUTRR v1 (Sinha et al., EMNLP 2019, arXiv:1908.06177), pooled TEST splits of configs gen_train234_test2to10 (1048 rows) and gen_train23_test2to10 (1146 rows), fetched as raw CSVs from the kliang5/CLUTRR_huggingface_dataset GitHub mirror and staged in temp/datasets/. CLUTRR is rule-based/templated, so its kinship gold is exact (no annotation noise) — exactly the property needed to host the realized-FDR-vs-alpha calibration diagonal.

  SCALE & SHAPE: ONE dataset group 'CLUTRR-v1-CrispGold-CalibrationAnchor' with 190 examples (row == one CLUTRR story). 150 confirmatory + 40 disjoint pilot (metadata_is_pilot). Stratified over chain length k=2..10 oversampling long chains (k>=4): confirmatory k-dist {k2:12,k3:15,k4:20,k5:20,k6:20,k7:18,k8:18,k9:15,k10:12}; pilot {k2:5,k3:5,k4:5,k5:5,k6:5,k7:5,k8:5,k9:3,k10:2}. Seed 20240617; selected ids recorded in top-level metadata for reproducibility.

  SCHEMA (aii-json exp_sel_data_out; validated, plus an independent 190/190 integrity pass): each example has STRING input and output (JSON-serialized; parse with json.loads) plus flat metadata_* fields. input keys: doc_id, document_text (clean prose, [Name] brackets stripped, native length never padded), document_text_bracketed (raw for entity-span provenance), entities[{name,gender,type='person',node_index}], query{head,tail}. output keys: atomic_facts[{head,relation,tail}] = the k directly-stated chain edges (the 'too clean' atomic family); multi_hop_facts[{head,relation,tail,derived_from,path_len,is_query_target}] = the k-1 proof_state-derived inferred relations incl. the query target (the error-dense 'populable' family the primary disconfirmation is pre-registered on); multi_hop_query_target{head,relation,tail}; kinship_edge_graph{nodes[{index,name,gender}],edges[{src,dst,relation}]}. All facts use the shared {head,relation,tail} triple structure with kinship relation strings (a Re-DocRED anchor could reuse the same structure with Wikidata relations).

  PER-EXAMPLE METADATA: metadata_fold ('k2'..'k10'), metadata_chain_length_k, metadata_difficulty_split ('short' k<=3 / 'long' k>=4), metadata_f_comb, metadata_task_name, metadata_source_config, metadata_source_split, metadata_clutrr_id, metadata_is_pilot, metadata_n_atomic_facts, metadata_n_multi_hop_facts, metadata_document_char_length, metadata_proof_state_raw, metadata_noisy_story, metadata_atomic_crosscheck ('match'), metadata_namemap_method ('genders_order'), metadata_genders_order_valid, metadata_relation_vocab_version ('clutrr_kinship'). Top-level metadata also carries relation_vocabulary (20 observed kinship relations), full k-distributions, and selected confirmatory/pilot id lists.

  CRISPNESS GUARANTEE: all gold is derived 100% from CLUTRR's own structured fields (proof_state leaf triples = atomic; proof_state dict keys = multi-hop) with NO homegrown rule reimplementation. Restricted to canonical simple-path chains (distinct entities==k+1, distinct edges, |atomic|==k, |multi_hop|==k-1, exactly one proof root equal to the query target, genders-order node->name map reproduces the proof_state atomic leaves); 1345 of 2191 pooled rows qualified, giving ample per-stratum supply.

  SELECTION: CLUTRR is THE chosen dataset (target_num_datasets=1). Secondary candidate ProofWriter (tasksource/proofwriter, kept in temp/datasets/ as backup) was excluded — it provides T/F/Unknown answers over rule/fact theories, not the kinship atomic+multi-hop triple gold this experiment is registered on. OUT OF SCOPE here (left to the experiment artifact): decoy/entrapment generation, LLM scoring, FDR/precision/recall, Prolog execution, transitive-closure enrichment. Files: data.py (uv run data.py), full_data_out.json (1.1MB, <100MB so no split), mini_data_out.json (3 ex), preview_data_out.json (3 ex, truncated). Reproducible via pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_SLUbUUr6Ul98
type: research
title: 'Spec Sheet: Label-Free FDR Gate at the LLM Text-to-Logic Admission Boundary'
summary: >-
  Consolidated, source-traceable implementation spec for the label-free decoy-competition FDR gate that admits LLM-extracted
  facts/bridges into a Prolog/symbolic layer. Provides, for each component, a verbatim formula (with equation number and source),
  a symbol glossary, a language-agnostic pseudo-procedure, and a recommended default. KEY RESULTS: (A) knockoff+ admission
  threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha} (Barber-Candes eq 1.9, exact FDR via Thm 2; plain knockoff eq
  1.8 controls only modified FDR Thm 1); the minimum-estimable-FDR floor is 1/k, so certifying FDR<=alpha needs k>=ceil(1/alpha)
  admissions -> demonstrable alpha grid {0.05,0.1,0.2,0.3,0.5} maps to k-floors {20,10,5,4,2}. Rajchert-Keich prove the '+1'
  is generally necessary (t=1 optimal), so keep it; TDC-SB/TDC-UB (bandsfdp) are an optional tighter FDX bound. (B) Entrapment
  estimators verbatim from Wen et al. 2025: combined FDP=N_E(1+1/r)/(N_T+N_E) (upper bound, DEFAULT), paired (eq4, requires
  r=1, tighter), lower bound N_E/(N_T+N_E) (failure-only), and 'sample' N_E(1/r)/N_T which is INVALID (biased). r=#entrapment/#target;
  default r=1 paired. (C) Document-block (cluster) bootstrap B>=2000 for all FDP/FDR CIs (resample whole documents; Cameron-Gelbach-Miller
  anchor) — the CI used by the primary disconfirmation. (D) Sole validity condition = Barber-Candes Lemma 1 (null W signs
  are i.i.d. fair coins) = TDC equal-chance; two anti-conservative failure modes (within-doc correlation -> bootstrap; batched
  contrast effect -> isolated provenance-blinded order-randomized scoring) and the isolated-vs-batched discriminator. (E)
  Property-matched document-conditioned COUNTERFACTUAL decoys + non-entailment verification (DeepCoy principle; DOE 0.166->0.032/0.109->0.038);
  random type-matched swaps kept as the anti-conservative negative control. (F) Ranked label-free upper-tail elicitation shortlist:
  DINCO (primary, overconfidence-corrected), FactSelfCheck (fact-level), self-consistency/SelfCheckGPT, logprob/yes-no-token
  (if exposed), verbalized (overconfident floor); Phase-0 selects on tail-AUC>0.5 with CI + isolated~batched agreement. (G)
  Recommended model openai/gpt-4.1-nano ($0.10/$0.40 per M, logprobs+auto-caching, <$0.30 input); fallbacks gpt-4o-mini then
  a logprob-free cheap caching model; projected cost ~$1-3 << $10 cap. (H) Novelty confirmed: no prior work applies knockoff/target-decoy/entrapment
  FDR at a label-free LLM text->logic admission boundary (conformal factuality/selection are labeled and certify outputs).
  Includes a final Parameter Defaults table and runtime follow-ups (probe logprobs non-null; confirm cached_tokens>0).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_1
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

### [4] SYSTEM-USER prompt · 2026-06-16 12:06:16 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
