# gen_art_experiment_2 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_2` (terminal_claude_agent)

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/results/out.json`
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
id: gen_plan_experiment_2_idx2
type: experiment
title: >-
  P1-DECONFOUND: A 2-Axis (Extractor-Strength x False-Positive-Density) Persistence Matrix for the Marginal-vs-Paired Knockoff+
  Failure on CLUTRR
summary: >-
  De-confound the iteration-3 disconfirmation (realized FDR 1.0 at alpha*=0.5, paired sign-flip failure on 12 multi_hop pairs)
  from a pathological extractor (gpt-4.1-nano forced multi-hop relation accuracy 0.169, ~85% genuine-false). Reuse the EXACT
  iter-3 P1 code (art_sBLQqsdm3EIA = .../iter_3/gen_art/gen_art_experiment_1: method.py + fdr_stats.py + fdr_core.py + llm_client.py
  + data.py + warm caches) and run a controlled factorial: AXIS A = extractor strength (gpt-4.1-nano baseline vs >=1 Phase-0-verified
  stronger extractor with multi-hop accuracy >> 0.17, ideally >= 0.45, used as extractor==scorer==decoy-generator so the model
  scores its OWN errors); AXIS B = false-positive density (stratified post-hoc subsampling of the scored real pool to ~20%/~50%/~85%
  genuine-false, FREE because it reuses already-computed scores). Per (extractor x density) cell: realized-FDR-vs-alpha diagonal
  with doc-block bootstrap (B>=2000) CIs, the gate's decoy_fdr_hat, the PAIRED win-rate over FALSE pairs at the cutoff (the
  key readout), and the MARGINAL crux (decoy~spontaneous-error vs !=true-positive). KEY OUTPUT: a persist/vanish matrix +
  an explicit EARNED-vs-SCOPED decision rule. If the paired failure PERSISTS for a competent extractor at matched/varied density
  while the marginal holds -> 'marginal != paired at the LLM boundary' is EARNED (paper headline); if it VANISHES (gate controls
  realized FDR at alpha) -> report the POSITIVE result and SCOPE the limitation to the weak-scorer/error-dense regime. CPU-only,
  soft cap ~$4, HARD STOP $10.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ############################################################################
  # STAGE -1 -- WORKSPACE BOOTSTRAP (reuse, do NOT rewrite the gate/scoring/stats)
  ############################################################################
  # The single most important efficiency + correctness move: copy the iter-3 P1
  # experiment (art_sBLQqsdm3EIA) into this workspace and EXTEND it. Do NOT
  # reimplement knockoff+, the bootstrap, or the OpenRouter client.
  SRC = /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
  cp SRC/{method.py,fdr_stats.py,fdr_core.py,llm_client.py,data.py,pyproject.toml} ./
  # Copy SRC/cache/ -> ./cache/ (warm-start the nano cell: the 190-doc prefix
  # self-consistency scores already exist => the nano arm is ~FREE).
  # Keep WARM_CACHES (iter-2 exp2 cache) as a read-only fallback_cache_dirs list
  # exactly as in SRC/method.py (the client promotes hits into ./cache).
  # Fresh ./logs/cost.jsonl so the $4 soft cap governs NEW spend only.
  # Set PYTHONHASHSEED=0; SEED=20240617 (per-doc seeds use hashlib, not hash()).
  #
  # DATASET (dep art_XZyKy6QuwxrO): regenerate a corpus large enough to supply
  # BOTH cells. Edit data.py CONFIRM_COUNTS/PILOT_COUNTS to ~250-320 confirmatory
  # docs (oversample k>=6 long chains => more multi_hop reals => denser false pool
  # for the strong extractor). The original 190 are a deterministic PREFIX so the
  # nano warm-cache still hits. `uv run data.py` -> full_data_out.json. Crisp gold
  # (Doc.label) is preserved by build_record. ~1345 clean rows available.
  #
  # Reused primitives (signatures verified in SRC):
  #   st.knockoff_plus_threshold(W, alpha)->(T,n_adm_pos,ratio)  [ratio == decoy_fdr_hat]
  #   st.W_signed_max(zr,zd);  st._knockoff_fast / _realized_fast (vectorized, bootstrap hot loop)
  #   st.tail_win_rate(list[(zr,zd)], cut)->(winrate,n_tail)  [decoy wins iff zd>zr]
  #   st.doc_block_bootstrap(doc_arrays, stat_fn, B, seed)->{ci_low,ci_high}
  #   st.rank_normalize(pool_dict, seed);  st.k_floor(alpha) -> {0.05:20,0.1:10,0.2:5,0.3:4,0.5:2}
  #   st.ks_two_sample / mannwhitney / anderson_darling_2samp / permutation_two_sample
  #   st.benjamini_hochberg(pvals,q);  fc.plain_threshold_gate(Z,alpha)
  #   llm_client.OpenRouterClient.call(model, messages, max_tokens, temperature, seed, sample_idx)
  #   method.extract_doc / gen_counterfactual_decoys / gen_swaps / score_portable / analyze_crux
  #   method.diagonal_for_family / _pairs_for / _decoy_map / norm_pool  (the diagonal + paired block)

  CONSTANTS:
    ALPHA_GRID = [0.05,0.10,0.20,0.30,0.50]; TAU=0.05; N_FALSE_MIN=40; K_SC=5; B_BOOT=2000
    DENSITIES   = [0.20, 0.50, 0.85]            # target genuine-FALSE fraction of scored real pool
    ACC_THRESHOLD = 0.45                         # Phase-0 competent-extractor bar (>> 0.17)
    SOFT_CAP_USD = 4.0; HARD_STOP_USD = 10.0
    EXTRACTOR_CANDIDATES = ['openai/gpt-4.1-mini','openai/gpt-4o-mini','openai/gpt-4.1']  # probe order cheap->dear
    FAMILIES = ['multi_hop','atomic']            # multi_hop is the registered populable family; atomic for contrast

  ############################################################################
  # STAGE 0 -- OFFLINE SELFTEST (no API). Extend SRC/method.selftest().
  ############################################################################
  # Keep ALL existing asserts. ADD:
  #  (1) subsample_to_density(): on a synthetic pool of labelled reals it returns a
  #      subset whose realized FALSE fraction == target within +/-1/pool_size, and
  #      every returned cand keeps its doc_id (doc blocks intact).
  #  (2) persistence-cell logic on two synthetic fixtures: (a) PAIRED-FAILS fixture
  #      (false reals' zr deterministically > their decoy zd) => paired win-rate CI_high<0.5
  #      AND realized FDR > alpha with CI_low>alpha; (b) PAIRED-OK fixture (fair coin)
  #      => win-rate CI covers 0.5 AND realized FDR <= alpha. Assert the EARNED/SCOPED
  #      classifier returns the right label on each.
  # Run: uv run method.py --selftest  (must pass before any API call).

  ############################################################################
  # STAGE 1 -- PHASE-0 EXTRACTOR PROBE (pick the competent extractor)  [~$0.1-0.3]
  ############################################################################
  def phase0_probe(candidates, pilot_docs ~ 40 docs):
    for model in candidates:
       run method.extract_doc(client, doc, model) for each pilot doc   # extract_doc must accept a model arg
       # extract_doc already computes mh_acc (forced per-pair fill-in-blank vs crisp gold)
       record mean mh_acc, atomic_precision/recall, mean #false_reals/doc, $ spent
    # PARAMETERIZE extract_doc: replace its hardcoded PRIMARY_MODEL with an
    # `extractor_model` argument (default 'openai/gpt-4.1-nano' to preserve cache identity).
    pick STRONG = cheapest candidate with mh_acc >= ACC_THRESHOLD;
         if none clears 0.45 -> pick the highest-accuracy candidate, record achieved acc,
         and flag matrix scope = 'extractor strength varied 0.17 -> {achieved}' (see FALLBACK).
    EMIT phase0 block: {nano_mh_acc, per-candidate mh_acc + cost, chosen STRONG, threshold_cleared}.

  ############################################################################
  # STAGE 2 -- PER-EXTRACTOR PIPELINE (the only NEW spend; nano is warm-cached)
  ############################################################################
  # Generalize SRC/method.run() into run_for_extractor(M): extractor==scorer==decoy-generator=M
  #   (the faithful self-detecting-gate setup; directly tests 'can a competent model
  #    score its OWN errors'). The DENSITY axis holds the scorer fixed within an extractor.
  def run_for_extractor(M, docs, K=K_SC):
    EXTRACTION:  reals_by_doc[d] = extract_doc(client, d, rng, extractor_model=M)   # 1 call/doc
                 # crisp 3-way label per real via Doc.label (TRUE/FALSE/UND); record mh_acc
    DECOYS:      cf_by_doc[d] = gen_counterfactual_decoys(client, d, reals, model=M, rng)  # 1 call/doc
                 # (swap decoys optional negative control; SKIP to save budget unless cheap)
    SCORING:     for cand in reals + cf_decoys:  zmap[(M,cand_id)] = score_portable(client, M, doc_text, claim)
                 # K=5 isolated provenance-blinded self-consistency; doc-prefix prompt caching ON
                 # (re-uses one cached doc context across the ~K*(#reals+#decoys) calls/doc)
    RETURN pipe_M = {docs,reals_by_doc,cf_by_doc,all_reals,zmap,ext_meta,...}   # same shape SRC expects
    # NOTE the only structural change vs SRC: thread `extractor_model`/`scorer_model`=M through
    #      extract_doc, gen_counterfactual_decoys, score_portable. Everything downstream (norm_pool,
    #      _pairs_for, diagonal_for_family, analyze_crux) is reused VERBATIM, called with pipe_M.
  pipe_nano = run_for_extractor('openai/gpt-4.1-nano', docs)   # ~free via warm cache for 190-prefix
  pipe_strong = run_for_extractor(STRONG, docs_strong)         # NEW spend; cost-gate doc count (see STAGE 5)
  save pipe checkpoints (SRC save_pipe_ckpt pattern) so analysis re-runs need NO API.

  ############################################################################
  # STAGE 3 -- DENSITY-CONTROLLED SUBSAMPLING (AXIS B; zero API cost)
  ############################################################################
  def subsample_to_density(family_reals, target_false_frac, seed):
    # family_reals: reals of one family (multi_hop) with crisp label TRUE/FALSE (drop UND).
    T = [c for c in family_reals if label==TRUE];  F = [c for c in family_reals if label==FALSE]
    # keep the SMALLER side whole, downsample the larger to hit target fraction; maximize pool size.
    if target_false_frac high (0.85): keep all F, sample |T| s.t. |F|/(|F|+|T|)==0.85
    else (0.20/0.50): keep all T, sample |F| s.t. ratio==target
    rng=Random(seed); shuffle then truncate the downsampled side; PRESERVE doc_id on every kept cand.
    RETURN set(kept cand_ids)   # the (real, its cf decoy) pairs that ENTER the gate for this cell
    # Robustness: repeat over SUBSAMPLE_SEEDS=range(10); report median + min/max of realized FDR
    #             and paired win-rate across seeds so the cell is not a single lucky draw.

  ############################################################################
  # STAGE 4 -- PER-CELL METRICS  (reuse the iter-3 diagonal + paired block)
  ############################################################################
  def cell_metrics(pipe_M, family, density, seed):
    norm = norm_pool(pipe_M, SC)                       # per-doc rank-normalized self-consistency Z
    keep = subsample_to_density(_family_reals(pipe_M,family), density, seed)
    # Build per_doc pairs restricted to `keep`, exactly like _pairs_for but filtered:
    per_doc = {doc_id: [ {zr,zd,label,doc_id,w=W_signed_max(zr,zd)} for real in keep with cf decoy scored ]}
    flat = concat(per_doc.values())
    rows = []   # the realized-FDR-vs-alpha DIAGONAL
    for alpha in ALPHA_GRID:
       T,n_adm_pos,ratio = knockoff_plus_threshold([p.w for p in flat], alpha)  # ratio = decoy_fdr_hat
       adm = [p for p in flat if p.w>=T];  n_adm=len(adm); n_false=#(adm.label==FALSE)
       realized = n_false/n_adm
       ci = doc_block_bootstrap(_doc_arrays(per_doc), stat=_realized_fast(.,alpha), B=B_BOOT, seed=SEED)
       certified = (n_adm>=k_floor(alpha))
       populable_at_alpha = (n_false>=... )   # see floor rule below
       self_report_anti = (realized - ratio) > TAU
       plain = fc.plain_threshold_gate(raw_self_consistency_Z_of_kept, alpha)  # zero-label foil
       rows.append({alpha, decoy_fdr_hat=ratio, realized_fdr=realized, ci_low,ci_high,
                    n_admitted=n_adm, n_false_admitted=n_false, k_floor, certified,
                    self_report_anti_conservative, plain_realized_fdr})
    # PAIRED-EXCHANGEABILITY (the KEY readout) -- reuse SRC diagonal_for_family's paired block:
    Tcut = knockoff_plus_threshold([p.w for p in flat], 0.50)[0];  cut = Tcut if finite else 0.0
    false_pairs = [p for p in flat if p.label==FALSE]
    wr_pe,n_tail = tail_win_rate([(p.zr,p.zd) for p in false_pairs], cut)      # decoy wins iff zd>zr
    ci_pe = doc_block_bootstrap(false_pairs grouped by doc, mean(zd>zr), B=1000, seed=SEED)
    paired_fails = (ci_pe.ci_high < 0.5)        # false reals systematically beat their OWN decoys
    paired_ok    = (ci_pe.ci_low <= 0.5 <= ci_pe.ci_high)
    # MARGINAL crux (decoy ~ spontaneous-error, != true-positive) RESTRICTED to this cell's reals:
    crux = analyze_crux(pipe_M restricted to family+keep, norm)  # gives decoy_vs_spont ks/mw + decoy_vs_truepos
    marginal_holds = (crux.tail.decoy_vs_spont.ks_p>0.05 and mw_p>0.05) and (decoy_vs_truepos rejects)
    RETURN {extractor:M, density, family, mh_acc, n_reals, n_false_total, n_true_total,
            diagonal_rows:rows, paired:{win_rate:wr_pe, ci:ci_pe, n_tail, paired_fails, paired_ok},
            marginal:{ks_p,mw_p,verdict,marginal_holds}, seed_spread:{realized,winrate over 10 seeds}}
  CELLS = [ cell_metrics(pipe, fam, rho, seed=SEED) for pipe in {nano,strong} for fam in FAMILIES for rho in DENSITIES ]

  # FLOOR / POWER RULE (binding):
  #   A cell is ASSERTED at alpha only if n_admitted>=k_floor(alpha). The DISCONFIRMATION
  #   (anti-conservative) at a given alpha additionally requires n_false_admitted>=N_FALSE_MIN(=40)
  #   OR, if fewer, is reported as 'directional, below false-admission floor'. A clean LOW realized
  #   FDR with CI entirely <= alpha is the POSITIVE 'gate controls' result and does NOT need 40
  #   false admissions (few false admitted IS the good outcome). Cells with NO certified alpha
  #   below 0.5 => 'NO_CERTIFIED_ALPHA' precondition, never 'confirmed by conservatism'.

  ############################################################################
  # STAGE 5 -- PERSISTENCE MATRIX + EARNED-vs-SCOPED VERDICT (explicit decision rule)
  ############################################################################
  # Per cell define (at operative alpha* = most-permissive CERTIFIED alpha, AND also at fixed alpha=0.5):
  #   anti_conservative(c) := realized_fdr > alpha + TAU AND ci_low > alpha          # the primary disconfirmation
  #   gate_controls(c)     := realized_fdr <= alpha + TAU AND NOT(ci_low > alpha)     # ideally ci_high<=alpha at alpha*
  #   paired_fails(c)      := paired.ci_high < 0.5
  #   paired_ok(c)         := paired.ci covers 0.5
  #   marginal_holds(c)    := marginal.marginal_holds
  #   competent(c)         := mh_acc(c.extractor) >= ACC_THRESHOLD
  #   powered(c)           := n_admitted>=k_floor(alpha) (and n_false>=N_FALSE_MIN for a disconfirmation assertion)
  #
  # DECISION RULE (emit verbatim as earned_vs_scoped_verdict.decision_rule):
  #   IF there exist >=2 POWERED competent-extractor cells spanning >=2 densities with
  #      marginal_holds AND (paired_fails OR anti_conservative):
  #         verdict = 'EARNED'  -> 'marginal != paired is a property of the LLM scoring boundary,
  #                                 not an artifact of the weak gpt-4.1-nano extractor; it persists
  #                                 with a competent extractor (mh_acc>=ACC_THRESHOLD) and across
  #                                 false-positive density while the MARGINAL decoy-quality diagnostic
  #                                 is satisfied' => becomes the paper HEADLINE (claim S1c earned).
  #   ELIF the POWERED competent-extractor cells show gate_controls AND paired_ok:
  #         verdict = 'SCOPED'  -> 'the paired failure VANISHES with a competent extractor: the gate
  #                                 controls realized FDR at alpha when the model can score its own
  #                                 errors. Report the POSITIVE result; scope the iter-3 disconfirmation
  #                                 to the weak-scorer / error-dense regime (S1c re-scoped).'
  #   ELIF failure tracks DENSITY (persists at 0.85 for BOTH extractors, vanishes at 0.20 for BOTH):
  #         verdict = 'DENSITY_DRIVEN' -> governing variable is false-positive density, not extractor
  #                                 competence; report the density crossover explicitly.
  #   ELSE: verdict = 'UNDERPOWERED_INCONCLUSIVE' -> not enough powered cells to separate hypotheses
  #                                 (the failure the floor/power rule is designed to prevent); list
  #                                 which cells fell below k_floor / N_FALSE_MIN.
  # matrix = 2 (extractor) x 3 (density) x 2 (family) table of {realized_fdr(+CI), decoy_fdr_hat,
  #          paired win-rate(+CI), marginal verdict, anti_conservative/gate_controls flags, powered}.
  # BH (st.benjamini_hochberg, q=0.05) across ALL cell p-values (marginal ks/mw + paired ks per cell).
  # SANITY ANCHOR: the nano x 0.85 x multi_hop cell MUST reproduce the iter-3 headline
  #   (realized FDR ~1.0 at alpha*=0.5, paired win-rate <0.5) -- assert + log; if not, STOP and debug
  #   (warm-cache mismatch) before spending on the strong extractor.

  ############################################################################
  # STAGE 6 -- FIGURES (full captions) + OUTPUT (exp_gen_sol_out schema)
  ############################################################################
  # Figures (Agg backend, .jpg into figures/), each caption carrying the 1/k floor, doc-block
  # bootstrap CIs, and the persist/vanish reading:
  #  F1 persistence heatmap: anti_conservative flag / realized FDR across (extractor x density) at alpha*,
  #     cells annotated with n_admitted, n_false, decoy_fdr_hat, 'below floor' hatching.
  #  F2 realized-FDR-vs-alpha diagonals: nano vs strong overlaid at matched density (0.85 and 0.50),
  #     ideal y=x dashed, 1/k floor shaded, doc-block CIs as error bars, plain-baseline + (optional) swap dotted.
  #  F3 paired win-rate over FALSE pairs (+CI) per cell with the 0.5 exchangeable line -- THE persist/vanish chart;
  #     annotate the paired-win asymmetry (mean(zd>zr)).
  #  F4 marginal crux CDF overlay (true-positive / spontaneous-error / counterfactual-decoy) per extractor,
  #     to show MARGINAL holds while PAIRED differs across extractors.
  # OUTPUT method_out.json via SRC build_output pattern, schema 'exp_gen_sol_out':
  #   {metadata:{...}, datasets:[{dataset:'CLUTRR-v1-CrispGold-CalibrationAnchor', examples:[...]}]}
  #   metadata MUST include: phase0_extractor_probe, persistence_matrix (full 2x3x2),
  #     per-cell {diagonal_rows incl (alpha,decoy_fdr_hat,realized,ci) TRIPLE, paired, marginal},
  #     earned_vs_scoped_verdict{verdict, decision_rule(verbatim), supporting_cells},
  #     extraction_quality per extractor (mh_acc, atomic P/R), dataset_counts, hyperparameters,
  #     bh_correction, figure-ready arrays, full_figure_captions{F1..F4}, runtime+cost_trace_path.
  #   examples[]: one per scored real carrying input(JSON: doc_id,head,relation,tail,claim,extractor),
  #     output=crisp label, metadata_* (z_real, z_decoy, w, fact_type, density_membership flags,
  #     per-alpha admit predictions). VALIDATE with the aii-json skill against exp_gen_sol_out.
  #   If method_out.json > file-size limit, use aii-file-size-limit skill to split + emit mini/preview.
  # Run order (gradual scaling, cost-gated): --selftest -> --mini(3 docs both extractors) ->
  #   phase0 probe -> nano full (warm) -> strong --n-docs 40 checkpoint (CHECK cost+populability) ->
  #   strong full (cap doc count so projected $ <= soft cap $4). Log cost after EVERY call (cost.jsonl).
  #   Background+PID launch (uv run method.py & PID=$!), never block-poll a long foreground run.
fallback_plan: |-
  EXTRACTOR (Axis A) cannot clear 0.45: (a) lower the bar to the best achievable and report the matrix as 'extractor strength varied 0.17 -> {achieved_mh_acc}'; even a jump to ~0.30-0.40 meaningfully de-confounds. (b) If NO candidate beats ~0.20 on multi_hop (CLUTRR long-chain kinship is genuinely hard), pivot the de-confound onto a LESS error-dense FAMILY: run the diagonal on ATOMIC facts (directly stated, low intrinsic error) with gpt-4.1-nano -- atomic is the natural 'competent' regime for the same model, giving a within-model strength contrast at zero extra-model cost. (c) Try one strong open model via OpenRouter (e.g. a Qwen/Llama-70B-class instruct) if OpenAI minis underperform; pick on Phase-0 mh_acc/$.
  BUDGET overrun on the strong extractor: cut strong-extractor docs first (120 -> 80 -> 40), then drop the swap negative control and entrapment/ladder/verbalized entirely (NOT needed for dir2's core), then reduce K self-consistency 5->3 for the strong arm only (record K per cell in metadata; note the small reduction in score resolution), then restrict to multi_hop only. The nano arm is warm-cached and ~free regardless. Hard stop at $10 is enforced by llm_client BudgetExceeded; on hard stop, emit whatever cells completed with the matrix flagged partial.
  FLOOR not reached (strong extractor yields too few FALSE reals for 0.85 density or <40 false admissions): (a) lean on Axis B subsampling -- 0.50/0.20 cells still populate; (b) scale strong-extractor docs up (more k>=6 long chains => more multi_hop errors) within budget; (c) report the under-floor cell as a PRECONDITION ('directional, below false-admission floor'), never as a conclusion. A clean low realized FDR with CI<=alpha is still the valid POSITIVE 'gate controls' result and needs only n_admitted>=k_floor, not 40 false.
  NO certified alpha below 0.5 in a cell: report 'NO_CERTIFIED_ALPHA' (a precondition outcome) for that cell; the matrix verdict then rests on the cells that ARE certified.
  HIGH subsample variance: the 10-seed robustness loop already reports spread; if a cell's realized FDR / win-rate flips sign across seeds, mark it UNSTABLE and exclude from the EARNED/SCOPED count (treat as underpowered).
  WARM-CACHE / sanity-anchor mismatch: if the nano x 0.85 x multi_hop cell does NOT reproduce the iter-3 headline (realized ~1.0 at alpha*=0.5, paired win-rate <0.5), STOP before spending on the strong extractor -- the bug is in corpus regeneration (doc-prefix ordering) or model/prompt drift, not the science; diff the regenerated 190-prefix doc_ids against iter-3 and fix before proceeding.
  WORST CASE (API/quota dies early): the nano warm-cached cells + Phase-0 probe alone still deliver a partial matrix and an honest 'INCONCLUSIVE/underpowered, only the weak-extractor point reproduced' verdict -- which is a faithful, publishable scoping statement, not a vacuous null.
  OPTIONAL EXTENSION if budget remains under $4: add ONE cross-scorer cell (strong extractor's facts scored by gpt-4.1-nano, G!=S) and compute the PAIRED win-rate there too, partially satisfying the hypothesis's 'compute the paired statistic across (G,S) configs' (S2b); if not run, state plainly in metadata that paired de-circularization remains marginal-only.
testing_plan: |-
  1) OFFLINE FIRST (no API, no cost): `uv run method.py --selftest`. Keep every existing iter-3 assert (knockoff+ vs vectorized _knockoff_fast equality over 200 random arrays, W signed-max antisymmetry, fair-coin win-rate in (0.45,0.55), too-easy decoy win-rate<0.45 + KS sig, doc-block CI > iid CI, Doc.label crisp 3-way, BH monotonic, entrapment estimators, rank_normalize). ADD asserts for the two NEW functions: (a) subsample_to_density hits the target FALSE fraction within +/-1/pool and preserves doc_ids; (b) on a PAIRED-FAILS synthetic fixture (false reals' zr deterministically above their decoy zd) the cell yields paired win-rate CI_high<0.5 AND realized FDR>alpha with CI_low>alpha, and the EARNED/SCOPED classifier labels it a persistence; on a PAIRED-OK fair-coin fixture it yields win-rate CI covering 0.5 + realized FDR<=alpha and classifies as gate_controls. Must be green before any network call.
  2) MINI SMOKE (~cents): `uv run method.py --mini` (3 docs) for BOTH extractors -- confirm extraction JSON parses, gen_counterfactual_decoys returns non-empty, score_portable returns floats in [0,1], cost logs to cost.jsonl, cache files written. No crashes through cell_metrics on the tiny pool.
  3) PHASE-0 PROBE (~$0.1-0.3): run the extractor probe on ~40 pilot docs; PRINT mh_acc + atomic P/R + $/doc per candidate. CONFIRMATION SIGNAL: at least one candidate's multi-hop accuracy is clearly > 0.17 (ideally >= 0.45) and gpt-4.1-nano reproduces ~0.169. Pick the cheapest clearing the bar; abort-to-fallback if none.
  4) NANO SANITY ANCHOR (~free, warm cache): run the nano arm + cell_metrics on multi_hop x 0.85 (native density). CONFIRMATION SIGNAL: realized FDR ~1.0 at alpha*=0.5 with CI [~0.66,1.0], paired win-rate <0.5 -- i.e. the iter-3 headline reproduces. If it does not, STOP and debug warm-cache/corpus ordering (see fallback) -- do NOT spend on the strong extractor until this matches.
  5) STRONG-EXTRACTOR CHECKPOINT (`--n-docs 40`): run the strong arm on 40 docs; inspect populability (n_false reals per family per density) and the cost trajectory. CONFIRMATION SIGNAL: projected full-run cost (linear extrapolation) <= soft cap $4 AND at least the 0.50/0.85 multi_hop cells reach n_admitted>=k_floor(0.5)=2 (and ideally toward N_FALSE_MIN at full scale). Only then launch the full strong arm.
  6) FULL RUN (background + PID, never block-poll): `uv run method.py & PID=$!`; tail logs/run.log; verify cost.jsonl cum_usd stays < $4 (soft) and never hits $10 (hard). On completion: re-run analysis offline (`--analyze-only` from the saved pipe checkpoints, no API) while iterating on figures/matrix so re-analysis is free.
  7) OUTPUT VALIDATION: validate method_out.json against exp_gen_sol_out with the aii-json skill; confirm the persistence_matrix has all attempted (extractor x density x family) cells with the (alpha, decoy_fdr_hat, realized) triple + CIs + paired win-rate + marginal verdict, and that earned_vs_scoped_verdict.decision_rule is present verbatim. Check file size (aii-file-size-limit) and emit mini/preview variants. Final smell test: the verdict (EARNED / SCOPED / DENSITY_DRIVEN / UNDERPOWERED) must be entailed by the matrix cells it cites -- spot-check 2 cited cells by hand against the diagonal rows.
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

### [3] SKILL-INPUT — aii-python · 2026-06-16 10:53:35 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 10:53:35 UTC

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

### [5] SKILL-INPUT — aii-use-hardware · 2026-06-16 10:53:35 UTC

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

### [6] SKILL-INPUT — aii-json · 2026-06-16 10:53:47 UTC

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

### [7] SKILL-INPUT — aii-parallel-computing · 2026-06-16 10:53:47 UTC

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

### [8] SKILL-INPUT — aii-file-size-limit · 2026-06-16 10:53:47 UTC

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

### [9] SYSTEM-USER prompt · 2026-06-16 12:44:30 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2/results/out.json`
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
id: gen_plan_experiment_2_idx2
type: experiment
title: >-
  P1-DECONFOUND: A 2-Axis (Extractor-Strength x False-Positive-Density) Persistence Matrix for the Marginal-vs-Paired Knockoff+
  Failure on CLUTRR
summary: >-
  De-confound the iteration-3 disconfirmation (realized FDR 1.0 at alpha*=0.5, paired sign-flip failure on 12 multi_hop pairs)
  from a pathological extractor (gpt-4.1-nano forced multi-hop relation accuracy 0.169, ~85% genuine-false). Reuse the EXACT
  iter-3 P1 code (art_sBLQqsdm3EIA = .../iter_3/gen_art/gen_art_experiment_1: method.py + fdr_stats.py + fdr_core.py + llm_client.py
  + data.py + warm caches) and run a controlled factorial: AXIS A = extractor strength (gpt-4.1-nano baseline vs >=1 Phase-0-verified
  stronger extractor with multi-hop accuracy >> 0.17, ideally >= 0.45, used as extractor==scorer==decoy-generator so the model
  scores its OWN errors); AXIS B = false-positive density (stratified post-hoc subsampling of the scored real pool to ~20%/~50%/~85%
  genuine-false, FREE because it reuses already-computed scores). Per (extractor x density) cell: realized-FDR-vs-alpha diagonal
  with doc-block bootstrap (B>=2000) CIs, the gate's decoy_fdr_hat, the PAIRED win-rate over FALSE pairs at the cutoff (the
  key readout), and the MARGINAL crux (decoy~spontaneous-error vs !=true-positive). KEY OUTPUT: a persist/vanish matrix +
  an explicit EARNED-vs-SCOPED decision rule. If the paired failure PERSISTS for a competent extractor at matched/varied density
  while the marginal holds -> 'marginal != paired at the LLM boundary' is EARNED (paper headline); if it VANISHES (gate controls
  realized FDR at alpha) -> report the POSITIVE result and SCOPE the limitation to the weak-scorer/error-dense regime. CPU-only,
  soft cap ~$4, HARD STOP $10.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ############################################################################
  # STAGE -1 -- WORKSPACE BOOTSTRAP (reuse, do NOT rewrite the gate/scoring/stats)
  ############################################################################
  # The single most important efficiency + correctness move: copy the iter-3 P1
  # experiment (art_sBLQqsdm3EIA) into this workspace and EXTEND it. Do NOT
  # reimplement knockoff+, the bootstrap, or the OpenRouter client.
  SRC = /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
  cp SRC/{method.py,fdr_stats.py,fdr_core.py,llm_client.py,data.py,pyproject.toml} ./
  # Copy SRC/cache/ -> ./cache/ (warm-start the nano cell: the 190-doc prefix
  # self-consistency scores already exist => the nano arm is ~FREE).
  # Keep WARM_CACHES (iter-2 exp2 cache) as a read-only fallback_cache_dirs list
  # exactly as in SRC/method.py (the client promotes hits into ./cache).
  # Fresh ./logs/cost.jsonl so the $4 soft cap governs NEW spend only.
  # Set PYTHONHASHSEED=0; SEED=20240617 (per-doc seeds use hashlib, not hash()).
  #
  # DATASET (dep art_XZyKy6QuwxrO): regenerate a corpus large enough to supply
  # BOTH cells. Edit data.py CONFIRM_COUNTS/PILOT_COUNTS to ~250-320 confirmatory
  # docs (oversample k>=6 long chains => more multi_hop reals => denser false pool
  # for the strong extractor). The original 190 are a deterministic PREFIX so the
  # nano warm-cache still hits. `uv run data.py` -> full_data_out.json. Crisp gold
  # (Doc.label) is preserved by build_record. ~1345 clean rows available.
  #
  # Reused primitives (signatures verified in SRC):
  #   st.knockoff_plus_threshold(W, alpha)->(T,n_adm_pos,ratio)  [ratio == decoy_fdr_hat]
  #   st.W_signed_max(zr,zd);  st._knockoff_fast / _realized_fast (vectorized, bootstrap hot loop)
  #   st.tail_win_rate(list[(zr,zd)], cut)->(winrate,n_tail)  [decoy wins iff zd>zr]
  #   st.doc_block_bootstrap(doc_arrays, stat_fn, B, seed)->{ci_low,ci_high}
  #   st.rank_normalize(pool_dict, seed);  st.k_floor(alpha) -> {0.05:20,0.1:10,0.2:5,0.3:4,0.5:2}
  #   st.ks_two_sample / mannwhitney / anderson_darling_2samp / permutation_two_sample
  #   st.benjamini_hochberg(pvals,q);  fc.plain_threshold_gate(Z,alpha)
  #   llm_client.OpenRouterClient.call(model, messages, max_tokens, temperature, seed, sample_idx)
  #   method.extract_doc / gen_counterfactual_decoys / gen_swaps / score_portable / analyze_crux
  #   method.diagonal_for_family / _pairs_for / _decoy_map / norm_pool  (the diagonal + paired block)

  CONSTANTS:
    ALPHA_GRID = [0.05,0.10,0.20,0.30,0.50]; TAU=0.05; N_FALSE_MIN=40; K_SC=5; B_BOOT=2000
    DENSITIES   = [0.20, 0.50, 0.85]            # target genuine-FALSE fraction of scored real pool
    ACC_THRESHOLD = 0.45                         # Phase-0 competent-extractor bar (>> 0.17)
    SOFT_CAP_USD = 4.0; HARD_STOP_USD = 10.0
    EXTRACTOR_CANDIDATES = ['openai/gpt-4.1-mini','openai/gpt-4o-mini','openai/gpt-4.1']  # probe order cheap->dear
    FAMILIES = ['multi_hop','atomic']            # multi_hop is the registered populable family; atomic for contrast

  ############################################################################
  # STAGE 0 -- OFFLINE SELFTEST (no API). Extend SRC/method.selftest().
  ############################################################################
  # Keep ALL existing asserts. ADD:
  #  (1) subsample_to_density(): on a synthetic pool of labelled reals it returns a
  #      subset whose realized FALSE fraction == target within +/-1/pool_size, and
  #      every returned cand keeps its doc_id (doc blocks intact).
  #  (2) persistence-cell logic on two synthetic fixtures: (a) PAIRED-FAILS fixture
  #      (false reals' zr deterministically > their decoy zd) => paired win-rate CI_high<0.5
  #      AND realized FDR > alpha with CI_low>alpha; (b) PAIRED-OK fixture (fair coin)
  #      => win-rate CI covers 0.5 AND realized FDR <= alpha. Assert the EARNED/SCOPED
  #      classifier returns the right label on each.
  # Run: uv run method.py --selftest  (must pass before any API call).

  ############################################################################
  # STAGE 1 -- PHASE-0 EXTRACTOR PROBE (pick the competent extractor)  [~$0.1-0.3]
  ############################################################################
  def phase0_probe(candidates, pilot_docs ~ 40 docs):
    for model in candidates:
       run method.extract_doc(client, doc, model) for each pilot doc   # extract_doc must accept a model arg
       # extract_doc already computes mh_acc (forced per-pair fill-in-blank vs crisp gold)
       record mean mh_acc, atomic_precision/recall, mean #false_reals/doc, $ spent
    # PARAMETERIZE extract_doc: replace its hardcoded PRIMARY_MODEL with an
    # `extractor_model` argument (default 'openai/gpt-4.1-nano' to preserve cache identity).
    pick STRONG = cheapest candidate with mh_acc >= ACC_THRESHOLD;
         if none clears 0.45 -> pick the highest-accuracy candidate, record achieved acc,
         and flag matrix scope = 'extractor strength varied 0.17 -> {achieved}' (see FALLBACK).
    EMIT phase0 block: {nano_mh_acc, per-candidate mh_acc + cost, chosen STRONG, threshold_cleared}.

  ############################################################################
  # STAGE 2 -- PER-EXTRACTOR PIPELINE (the only NEW spend; nano is warm-cached)
  ############################################################################
  # Generalize SRC/method.run() into run_for_extractor(M): extractor==scorer==decoy-generator=M
  #   (the faithful self-detecting-gate setup; directly tests 'can a competent model
  #    score its OWN errors'). The DENSITY axis holds the scorer fixed within an extractor.
  def run_for_extractor(M, docs, K=K_SC):
    EXTRACTION:  reals_by_doc[d] = extract_doc(client, d, rng, extractor_model=M)   # 1 call/doc
                 # crisp 3-way label per real via Doc.label (TRUE/FALSE/UND); record mh_acc
    DECOYS:      cf_by_doc[d] = gen_counterfactual_decoys(client, d, reals, model=M, rng)  # 1 call/doc
                 # (swap decoys optional negative control; SKIP to save budget unless cheap)
    SCORING:     for cand in reals + cf_decoys:  zmap[(M,cand_id)] = score_portable(client, M, doc_text, claim)
                 # K=5 isolated provenance-blinded self-consistency; doc-prefix prompt caching ON
                 # (re-uses one cached doc context across the ~K*(#reals+#decoys) calls/doc)
    RETURN pipe_M = {docs,reals_by_doc,cf_by_doc,all_reals,zmap,ext_meta,...}   # same shape SRC expects
    # NOTE the only structural change vs SRC: thread `extractor_model`/`scorer_model`=M through
    #      extract_doc, gen_counterfactual_decoys, score_portable. Everything downstream (norm_pool,
    #      _pairs_for, diagonal_for_family, analyze_crux) is reused VERBATIM, called with pipe_M.
  pipe_nano = run_for_extractor('openai/gpt-4.1-nano', docs)   # ~free via warm cache for 190-prefix
  pipe_strong = run_for_extractor(STRONG, docs_strong)         # NEW spend; cost-gate doc count (see STAGE 5)
  save pipe checkpoints (SRC save_pipe_ckpt pattern) so analysis re-runs need NO API.

  ############################################################################
  # STAGE 3 -- DENSITY-CONTROLLED SUBSAMPLING (AXIS B; zero API cost)
  ############################################################################
  def subsample_to_density(family_reals, target_false_frac, seed):
    # family_reals: reals of one family (multi_hop) with crisp label TRUE/FALSE (drop UND).
    T = [c for c in family_reals if label==TRUE];  F = [c for c in family_reals if label==FALSE]
    # keep the SMALLER side whole, downsample the larger to hit target fraction; maximize pool size.
    if target_false_frac high (0.85): keep all F, sample |T| s.t. |F|/(|F|+|T|)==0.85
    else (0.20/0.50): keep all T, sample |F| s.t. ratio==target
    rng=Random(seed); shuffle then truncate the downsampled side; PRESERVE doc_id on every kept cand.
    RETURN set(kept cand_ids)   # the (real, its cf decoy) pairs that ENTER the gate for this cell
    # Robustness: repeat over SUBSAMPLE_SEEDS=range(10); report median + min/max of realized FDR
    #             and paired win-rate across seeds so the cell is not a single lucky draw.

  ############################################################################
  # STAGE 4 -- PER-CELL METRICS  (reuse the iter-3 diagonal + paired block)
  ############################################################################
  def cell_metrics(pipe_M, family, density, seed):
    norm = norm_pool(pipe_M, SC)                       # per-doc rank-normalized self-consistency Z
    keep = subsample_to_density(_family_reals(pipe_M,family), density, seed)
    # Build per_doc pairs restricted to `keep`, exactly like _pairs_for but filtered:
    per_doc = {doc_id: [ {zr,zd,label,doc_id,w=W_signed_max(zr,zd)} for real in keep with cf decoy scored ]}
    flat = concat(per_doc.values())
    rows = []   # the realized-FDR-vs-alpha DIAGONAL
    for alpha in ALPHA_GRID:
       T,n_adm_pos,ratio = knockoff_plus_threshold([p.w for p in flat], alpha)  # ratio = decoy_fdr_hat
       adm = [p for p in flat if p.w>=T];  n_adm=len(adm); n_false=#(adm.label==FALSE)
       realized = n_false/n_adm
       ci = doc_block_bootstrap(_doc_arrays(per_doc), stat=_realized_fast(.,alpha), B=B_BOOT, seed=SEED)
       certified = (n_adm>=k_floor(alpha))
       populable_at_alpha = (n_false>=... )   # see floor rule below
       self_report_anti = (realized - ratio) > TAU
       plain = fc.plain_threshold_gate(raw_self_consistency_Z_of_kept, alpha)  # zero-label foil
       rows.append({alpha, decoy_fdr_hat=ratio, realized_fdr=realized, ci_low,ci_high,
                    n_admitted=n_adm, n_false_admitted=n_false, k_floor, certified,
                    self_report_anti_conservative, plain_realized_fdr})
    # PAIRED-EXCHANGEABILITY (the KEY readout) -- reuse SRC diagonal_for_family's paired block:
    Tcut = knockoff_plus_threshold([p.w for p in flat], 0.50)[0];  cut = Tcut if finite else 0.0
    false_pairs = [p for p in flat if p.label==FALSE]
    wr_pe,n_tail = tail_win_rate([(p.zr,p.zd) for p in false_pairs], cut)      # decoy wins iff zd>zr
    ci_pe = doc_block_bootstrap(false_pairs grouped by doc, mean(zd>zr), B=1000, seed=SEED)
    paired_fails = (ci_pe.ci_high < 0.5)        # false reals systematically beat their OWN decoys
    paired_ok    = (ci_pe.ci_low <= 0.5 <= ci_pe.ci_high)
    # MARGINAL crux (decoy ~ spontaneous-error, != true-positive) RESTRICTED to this cell's reals:
    crux = analyze_crux(pipe_M restricted to family+keep, norm)  # gives decoy_vs_spont ks/mw + decoy_vs_truepos
    marginal_holds = (crux.tail.decoy_vs_spont.ks_p>0.05 and mw_p>0.05) and (decoy_vs_truepos rejects)
    RETURN {extractor:M, density, family, mh_acc, n_reals, n_false_total, n_true_total,
            diagonal_rows:rows, paired:{win_rate:wr_pe, ci:ci_pe, n_tail, paired_fails, paired_ok},
            marginal:{ks_p,mw_p,verdict,marginal_holds}, seed_spread:{realized,winrate over 10 seeds}}
  CELLS = [ cell_metrics(pipe, fam, rho, seed=SEED) for pipe in {nano,strong} for fam in FAMILIES for rho in DENSITIES ]

  # FLOOR / POWER RULE (binding):
  #   A cell is ASSERTED at alpha only if n_admitted>=k_floor(alpha). The DISCONFIRMATION
  #   (anti-conservative) at a given alpha additionally requires n_false_admitted>=N_FALSE_MIN(=40)
  #   OR, if fewer, is reported as 'directional, below false-admission floor'. A clean LOW realized
  #   FDR with CI entirely <= alpha is the POSITIVE 'gate controls' result and does NOT need 40
  #   false admissions (few false admitted IS the good outcome). Cells with NO certified alpha
  #   below 0.5 => 'NO_CERTIFIED_ALPHA' precondition, never 'confirmed by conservatism'.

  ############################################################################
  # STAGE 5 -- PERSISTENCE MATRIX + EARNED-vs-SCOPED VERDICT (explicit decision rule)
  ############################################################################
  # Per cell define (at operative alpha* = most-permissive CERTIFIED alpha, AND also at fixed alpha=0.5):
  #   anti_conservative(c) := realized_fdr > alpha + TAU AND ci_low > alpha          # the primary disconfirmation
  #   gate_controls(c)     := realized_fdr <= alpha + TAU AND NOT(ci_low > alpha)     # ideally ci_high<=alpha at alpha*
  #   paired_fails(c)      := paired.ci_high < 0.5
  #   paired_ok(c)         := paired.ci covers 0.5
  #   marginal_holds(c)    := marginal.marginal_holds
  #   competent(c)         := mh_acc(c.extractor) >= ACC_THRESHOLD
  #   powered(c)           := n_admitted>=k_floor(alpha) (and n_false>=N_FALSE_MIN for a disconfirmation assertion)
  #
  # DECISION RULE (emit verbatim as earned_vs_scoped_verdict.decision_rule):
  #   IF there exist >=2 POWERED competent-extractor cells spanning >=2 densities with
  #      marginal_holds AND (paired_fails OR anti_conservative):
  #         verdict = 'EARNED'  -> 'marginal != paired is a property of the LLM scoring boundary,
  #                                 not an artifact of the weak gpt-4.1-nano extractor; it persists
  #                                 with a competent extractor (mh_acc>=ACC_THRESHOLD) and across
  #                                 false-positive density while the MARGINAL decoy-quality diagnostic
  #                                 is satisfied' => becomes the paper HEADLINE (claim S1c earned).
  #   ELIF the POWERED competent-extractor cells show gate_controls AND paired_ok:
  #         verdict = 'SCOPED'  -> 'the paired failure VANISHES with a competent extractor: the gate
  #                                 controls realized FDR at alpha when the model can score its own
  #                                 errors. Report the POSITIVE result; scope the iter-3 disconfirmation
  #                                 to the weak-scorer / error-dense regime (S1c re-scoped).'
  #   ELIF failure tracks DENSITY (persists at 0.85 for BOTH extractors, vanishes at 0.20 for BOTH):
  #         verdict = 'DENSITY_DRIVEN' -> governing variable is false-positive density, not extractor
  #                                 competence; report the density crossover explicitly.
  #   ELSE: verdict = 'UNDERPOWERED_INCONCLUSIVE' -> not enough powered cells to separate hypotheses
  #                                 (the failure the floor/power rule is designed to prevent); list
  #                                 which cells fell below k_floor / N_FALSE_MIN.
  # matrix = 2 (extractor) x 3 (density) x 2 (family) table of {realized_fdr(+CI), decoy_fdr_hat,
  #          paired win-rate(+CI), marginal verdict, anti_conservative/gate_controls flags, powered}.
  # BH (st.benjamini_hochberg, q=0.05) across ALL cell p-values (marginal ks/mw + paired ks per cell).
  # SANITY ANCHOR: the nano x 0.85 x multi_hop cell MUST reproduce the iter-3 headline
  #   (realized FDR ~1.0 at alpha*=0.5, paired win-rate <0.5) -- assert + log; if not, STOP and debug
  #   (warm-cache mismatch) before spending on the strong extractor.

  ############################################################################
  # STAGE 6 -- FIGURES (full captions) + OUTPUT (exp_gen_sol_out schema)
  ############################################################################
  # Figures (Agg backend, .jpg into figures/), each caption carrying the 1/k floor, doc-block
  # bootstrap CIs, and the persist/vanish reading:
  #  F1 persistence heatmap: anti_conservative flag / realized FDR across (extractor x density) at alpha*,
  #     cells annotated with n_admitted, n_false, decoy_fdr_hat, 'below floor' hatching.
  #  F2 realized-FDR-vs-alpha diagonals: nano vs strong overlaid at matched density (0.85 and 0.50),
  #     ideal y=x dashed, 1/k floor shaded, doc-block CIs as error bars, plain-baseline + (optional) swap dotted.
  #  F3 paired win-rate over FALSE pairs (+CI) per cell with the 0.5 exchangeable line -- THE persist/vanish chart;
  #     annotate the paired-win asymmetry (mean(zd>zr)).
  #  F4 marginal crux CDF overlay (true-positive / spontaneous-error / counterfactual-decoy) per extractor,
  #     to show MARGINAL holds while PAIRED differs across extractors.
  # OUTPUT method_out.json via SRC build_output pattern, schema 'exp_gen_sol_out':
  #   {metadata:{...}, datasets:[{dataset:'CLUTRR-v1-CrispGold-CalibrationAnchor', examples:[...]}]}
  #   metadata MUST include: phase0_extractor_probe, persistence_matrix (full 2x3x2),
  #     per-cell {diagonal_rows incl (alpha,decoy_fdr_hat,realized,ci) TRIPLE, paired, marginal},
  #     earned_vs_scoped_verdict{verdict, decision_rule(verbatim), supporting_cells},
  #     extraction_quality per extractor (mh_acc, atomic P/R), dataset_counts, hyperparameters,
  #     bh_correction, figure-ready arrays, full_figure_captions{F1..F4}, runtime+cost_trace_path.
  #   examples[]: one per scored real carrying input(JSON: doc_id,head,relation,tail,claim,extractor),
  #     output=crisp label, metadata_* (z_real, z_decoy, w, fact_type, density_membership flags,
  #     per-alpha admit predictions). VALIDATE with the aii-json skill against exp_gen_sol_out.
  #   If method_out.json > file-size limit, use aii-file-size-limit skill to split + emit mini/preview.
  # Run order (gradual scaling, cost-gated): --selftest -> --mini(3 docs both extractors) ->
  #   phase0 probe -> nano full (warm) -> strong --n-docs 40 checkpoint (CHECK cost+populability) ->
  #   strong full (cap doc count so projected $ <= soft cap $4). Log cost after EVERY call (cost.jsonl).
  #   Background+PID launch (uv run method.py & PID=$!), never block-poll a long foreground run.
fallback_plan: |-
  EXTRACTOR (Axis A) cannot clear 0.45: (a) lower the bar to the best achievable and report the matrix as 'extractor strength varied 0.17 -> {achieved_mh_acc}'; even a jump to ~0.30-0.40 meaningfully de-confounds. (b) If NO candidate beats ~0.20 on multi_hop (CLUTRR long-chain kinship is genuinely hard), pivot the de-confound onto a LESS error-dense FAMILY: run the diagonal on ATOMIC facts (directly stated, low intrinsic error) with gpt-4.1-nano -- atomic is the natural 'competent' regime for the same model, giving a within-model strength contrast at zero extra-model cost. (c) Try one strong open model via OpenRouter (e.g. a Qwen/Llama-70B-class instruct) if OpenAI minis underperform; pick on Phase-0 mh_acc/$.
  BUDGET overrun on the strong extractor: cut strong-extractor docs first (120 -> 80 -> 40), then drop the swap negative control and entrapment/ladder/verbalized entirely (NOT needed for dir2's core), then reduce K self-consistency 5->3 for the strong arm only (record K per cell in metadata; note the small reduction in score resolution), then restrict to multi_hop only. The nano arm is warm-cached and ~free regardless. Hard stop at $10 is enforced by llm_client BudgetExceeded; on hard stop, emit whatever cells completed with the matrix flagged partial.
  FLOOR not reached (strong extractor yields too few FALSE reals for 0.85 density or <40 false admissions): (a) lean on Axis B subsampling -- 0.50/0.20 cells still populate; (b) scale strong-extractor docs up (more k>=6 long chains => more multi_hop errors) within budget; (c) report the under-floor cell as a PRECONDITION ('directional, below false-admission floor'), never as a conclusion. A clean low realized FDR with CI<=alpha is still the valid POSITIVE 'gate controls' result and needs only n_admitted>=k_floor, not 40 false.
  NO certified alpha below 0.5 in a cell: report 'NO_CERTIFIED_ALPHA' (a precondition outcome) for that cell; the matrix verdict then rests on the cells that ARE certified.
  HIGH subsample variance: the 10-seed robustness loop already reports spread; if a cell's realized FDR / win-rate flips sign across seeds, mark it UNSTABLE and exclude from the EARNED/SCOPED count (treat as underpowered).
  WARM-CACHE / sanity-anchor mismatch: if the nano x 0.85 x multi_hop cell does NOT reproduce the iter-3 headline (realized ~1.0 at alpha*=0.5, paired win-rate <0.5), STOP before spending on the strong extractor -- the bug is in corpus regeneration (doc-prefix ordering) or model/prompt drift, not the science; diff the regenerated 190-prefix doc_ids against iter-3 and fix before proceeding.
  WORST CASE (API/quota dies early): the nano warm-cached cells + Phase-0 probe alone still deliver a partial matrix and an honest 'INCONCLUSIVE/underpowered, only the weak-extractor point reproduced' verdict -- which is a faithful, publishable scoping statement, not a vacuous null.
  OPTIONAL EXTENSION if budget remains under $4: add ONE cross-scorer cell (strong extractor's facts scored by gpt-4.1-nano, G!=S) and compute the PAIRED win-rate there too, partially satisfying the hypothesis's 'compute the paired statistic across (G,S) configs' (S2b); if not run, state plainly in metadata that paired de-circularization remains marginal-only.
testing_plan: |-
  1) OFFLINE FIRST (no API, no cost): `uv run method.py --selftest`. Keep every existing iter-3 assert (knockoff+ vs vectorized _knockoff_fast equality over 200 random arrays, W signed-max antisymmetry, fair-coin win-rate in (0.45,0.55), too-easy decoy win-rate<0.45 + KS sig, doc-block CI > iid CI, Doc.label crisp 3-way, BH monotonic, entrapment estimators, rank_normalize). ADD asserts for the two NEW functions: (a) subsample_to_density hits the target FALSE fraction within +/-1/pool and preserves doc_ids; (b) on a PAIRED-FAILS synthetic fixture (false reals' zr deterministically above their decoy zd) the cell yields paired win-rate CI_high<0.5 AND realized FDR>alpha with CI_low>alpha, and the EARNED/SCOPED classifier labels it a persistence; on a PAIRED-OK fair-coin fixture it yields win-rate CI covering 0.5 + realized FDR<=alpha and classifies as gate_controls. Must be green before any network call.
  2) MINI SMOKE (~cents): `uv run method.py --mini` (3 docs) for BOTH extractors -- confirm extraction JSON parses, gen_counterfactual_decoys returns non-empty, score_portable returns floats in [0,1], cost logs to cost.jsonl, cache files written. No crashes through cell_metrics on the tiny pool.
  3) PHASE-0 PROBE (~$0.1-0.3): run the extractor probe on ~40 pilot docs; PRINT mh_acc + atomic P/R + $/doc per candidate. CONFIRMATION SIGNAL: at least one candidate's multi-hop accuracy is clearly > 0.17 (ideally >= 0.45) and gpt-4.1-nano reproduces ~0.169. Pick the cheapest clearing the bar; abort-to-fallback if none.
  4) NANO SANITY ANCHOR (~free, warm cache): run the nano arm + cell_metrics on multi_hop x 0.85 (native density). CONFIRMATION SIGNAL: realized FDR ~1.0 at alpha*=0.5 with CI [~0.66,1.0], paired win-rate <0.5 -- i.e. the iter-3 headline reproduces. If it does not, STOP and debug warm-cache/corpus ordering (see fallback) -- do NOT spend on the strong extractor until this matches.
  5) STRONG-EXTRACTOR CHECKPOINT (`--n-docs 40`): run the strong arm on 40 docs; inspect populability (n_false reals per family per density) and the cost trajectory. CONFIRMATION SIGNAL: projected full-run cost (linear extrapolation) <= soft cap $4 AND at least the 0.50/0.85 multi_hop cells reach n_admitted>=k_floor(0.5)=2 (and ideally toward N_FALSE_MIN at full scale). Only then launch the full strong arm.
  6) FULL RUN (background + PID, never block-poll): `uv run method.py & PID=$!`; tail logs/run.log; verify cost.jsonl cum_usd stays < $4 (soft) and never hits $10 (hard). On completion: re-run analysis offline (`--analyze-only` from the saved pipe checkpoints, no API) while iterating on figures/matrix so re-analysis is free.
  7) OUTPUT VALIDATION: validate method_out.json against exp_gen_sol_out with the aii-json skill; confirm the persistence_matrix has all attempted (extractor x density x family) cells with the (alpha, decoy_fdr_hat, realized) triple + CIs + paired win-rate + marginal verdict, and that earned_vs_scoped_verdict.decision_rule is present verbatim. Check file size (aii-file-size-limit) and emit mini/preview variants. Final smell test: the verdict (EARNED / SCOPED / DENSITY_DRIVEN / UNDERPOWERED) must be entailed by the matrix cells it cites -- spot-check 2 cited cells by hand against the diagonal rows.
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
