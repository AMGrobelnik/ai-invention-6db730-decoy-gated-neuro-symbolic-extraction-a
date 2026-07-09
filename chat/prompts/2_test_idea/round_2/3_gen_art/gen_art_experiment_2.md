# gen_art_experiment_2 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 06:13:25 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/results/out.json`
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
  S1 Tail-Exchangeability + Spontaneous-Error Match + Generator!=Scorer De-Circularization on CLUTRR Crisp Gold
summary: >-
  Elevate two methodology-defense results to first-class empirical numbers on a labeled CLUTRR slice (40 pilot + bounded confirmatory
  subset). (1) DECOY SIGNATURE (S1): tail-conditioned win-rate (~0.5) and upper-tail two-sample CDF tests (KS + tail Mann-Whitney)
  on known-false reals vs document-conditioned counterfactual decoys, with random type-matched swaps as the predicted anti-conservative
  control that validates diagnostic sensitivity. (2) SPONTANEOUS-ERROR TAIL MATCH (the reviewer's named crux): show counterfactual-decoy
  scores reproduce the GENUINE extractor-error (spontaneous false-real) tail distribution, NOT the true-positive distribution,
  with a reported matching gap. (3) GENERATOR!=SCORER ABLATION (S2b): re-run win-rate/CDF tests and a small labeled-slice
  diagonal with decoys from family G scored by a DIFFERENT-family S (and the symmetric swap); if exchangeability/diagonal
  hold only when G=S, report a localized shared-model artifact (a reported negative result). Canonical W_i; document-block
  bootstrap (B>=2000); BH multiplicity correction; isolated provenance-blinded scoring; cheap sub-$0.30/M models with caching;
  gradual scaling; cumulative cost logged after EVERY call; soft cap ~$1.5, HARD STOP $10. Output method_out.json with tables,
  figure-ready CDFs, and the G==S vs G!=S verdict + validity-region statement.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # ============================================================================
  # EXPERIMENT: S1 decoy-signature + spontaneous-error match + G!=S de-circularization
  # CPU-only; all LLM calls via OpenRouter (aii-openrouter-llms skill). Read skills:
  #   aii-openrouter-llms, aii-parallel-computing (async), aii-long-running-tasks
  #   (gradual scaling), aii-json (validate method_out.json), aii-use-hardware.
  # Dataset dependency files are READ-ONLY; do not re-derive gold rules by hand.
  # ============================================================================

  # ---------------------------------------------------------------------------
  # 0. SETUP, CONSTANTS, COST GUARDRAILS
  # ---------------------------------------------------------------------------
  SEED = 20240617
  ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]      # k-floors = ceil(1/a) = {20,10,5,4,2}
  TAU = 0.05                                       # FDR-vs-alpha tolerance (report sensitivity {0,0.05})
  B_BOOT = 2000                                    # document-block bootstrap replicates (>=2000)
  N_FALSE_MIN = 40                                 # spontaneous-error populability floor (pooled)
  K_SC = 5                                          # self-consistency samples (portable elicitation)
  SOFT_CAP_USD = 1.5; HARD_STOP_USD = 10.0
  PRIMARY_MODEL = 'openai/gpt-4.1-nano'            # $0.10/$0.40 per M, logprobs+auto-cache
  # Different-FAMILY scorer for the ablation: pick a current cheap (<$0.30/M input) NON-OpenAI
  # instruct model via the aii-openrouter-llms skill, preferring one that exposes logprobs.
  # Default candidates in order: qwen/* flash/instruct, meta-llama/llama-3.x-instruct,
  # mistralai/* small. Bind the resolved id to OTHER_MODEL.

  COST = 0.0    # cumulative USD; updated after EVERY call from response usage + price table
  def log_cost(resp):
      global COST
      COST += price(resp.model, resp.usage)        # cached_tokens billed at provider read-mult
      append_jsonl('logs/cost.jsonl', {'model':resp.model,'usage':resp.usage,'cum_usd':COST})
      assert COST < HARD_STOP_USD, f'HARD STOP: spend {COST} reached cap'   # crash-safe abort

  # OpenRouter call wrapper: async, retry w/ backoff, isolated (one candidate per call),
  # provenance-blinded prompt, order of any in-prompt options randomized by SEED.
  # Concurrency via asyncio.Semaphore (e.g. 24); see aii-parallel-computing.

  # ---------------------------------------------------------------------------
  # 1. LOAD DATA + BUILD CRISP GOLD AND THE KNOWN-FALSE LABELER
  # ---------------------------------------------------------------------------
  # Dep1 dataset: .../iter_1/gen_art/gen_art_dataset_1/full_data_out.json (190 ex).
  # Dep2 spec   : .../iter_1/gen_art/gen_art_research_1/research_out.json (formulas).
  rows = load_json(full_data_out.json).datasets[0].examples
  for r in rows:
      inp = json.loads(r.input); out = json.loads(r.output)        # STRING fields -> json.loads
      r.entities=inp.entities; r.doc=inp.document_text; r.query=inp.query; r.k=r.metadata_chain_length_k
      r.is_pilot=r.metadata_is_pilot
      # GOLD_TRUE: directed triples that are entailed/derivable = atomic_facts UNION multi_hop_facts.
      r.gold_true = set((f.head,f.relation,f.tail) for f in out.atomic_facts + out.multi_hop_facts)
      # Canonical relation per ORDERED pair (kinship pair has a unique directed relation):
      r.gold_rel = { (h,t): rel for (h,rel,t) in r.gold_true }      # used for crisp labeling
      r.gold_pairs = set(r.gold_rel.keys())
  RELATIONS = full_data.metadata.relation_vocabulary               # 20 kinship relations

  def label(doc_row, h, rel, t):
      # CRISP 3-way label vs CLUTRR gold (exact, no annotation noise):
      if (h,rel,t) in doc_row.gold_true:                 return 'TRUE'
      if (h,t) in doc_row.gold_pairs and rel!=doc_row.gold_rel[(h,t)]: return 'FALSE'  # contradiction
      return 'UNDECIDABLE'   # pair not enumerated in gold (distant/no-vocab) -> excluded from crisp sets
  # Rationale: restricting FALSE to enumerated-pair contradictions avoids mislabeling unlisted
  # inverse/distant relations; keeps the known-false set defensible and exact.

  # ---------------------------------------------------------------------------
  # 2. EXTRACTION (OVER-GENERATE TO DENSIFY SPONTANEOUS ERRORS -> the crux's data)
  # ---------------------------------------------------------------------------
  # One extraction call per document (generation, not scoring -> batching OK here).
  # Prompt G to extract BOTH (a) atomic stated kinship facts and (b) ALL multi-hop
  # inferred kinship relations among entity pairs it can derive (push long chains).
  # Multi-hop is the ERROR-DENSE family; long-k docs yield the most spontaneous errors.
  for d in DOCS:
      raw = LLM_generate(G, EXTRACT_PROMPT(d.doc, d.entities, RELATIONS)); log_cost(raw)
      d.reals = parse_triples(raw)                       # dedupe; keep only entity pairs in d
      for c in d.reals: c.lab = label(d, c.head, c.rel, c.tail)
      d.true_reals  = [c for c in d.reals if c.lab=='TRUE']
      d.spont_errs  = [c for c in d.reals if c.lab=='FALSE']   # GENUINE extractor errors (target dist)
      # drop UNDECIDABLE reals from crisp diagnostics (logged for transparency)
  N_spont = sum(len(d.spont_errs) for d in DOCS)
  if N_spont < N_FALSE_MIN:   # enrich: more long-k docs, higher temperature, stronger over-gen prompt
      enrich_until(N_spont>=N_FALSE_MIN OR exhausted); if still short -> mark crux 'UNDERPOWERED'

  # ---------------------------------------------------------------------------
  # 3. DECOY GENERATION (matched counterfactual) + RANDOM-SWAP NEGATIVE CONTROL
  # ---------------------------------------------------------------------------
  # For EACH real candidate c=(h,rel,t) build a 1:1 matched decoy and a swap control.
  # (A) COUNTERFACTUAL DECOY (PRIMARY, property-matched, DeepCoy principle): ask G for the
  #     MOST PLAUSIBLE ALTERNATIVE kinship relation for the SAME ordered pair (h,t), i.e.
  #     identical surface form/entities/specificity, differing only in relation. Take the
  #     model's top suggestion; if it equals the crisp gold relation (decoy would be TRUE),
  #     take the next suggestion. VERIFY NON-ENTAILMENT deterministically vs crisp gold:
  #     accept iff (h,rel_decoy,t) not in gold_true AND rel_decoy != gold_rel[(h,t)].
  #     For FALSE reals also require rel_decoy != c.rel (decoy must differ from the real).
  #     Log contamination_rate = #(generated decoys that were gold-entailed)/#generated.
  # (B) RANDOM TYPE-MATCHED SWAP (negative control, EXPECTED anti-conservative): keep (h,rel),
  #     replace t by a random same-type (person) entity t' in d, t'!=t; verify non-entailed.
  for d in DOCS:
    for c in d.reals:
       c.decoy = gen_counterfactual(G, d, c); log_cost(...); verify_nonentailment_via_gold(c.decoy)
       c.swap  = random_type_matched_swap(d, c, rng=SEED)            # deterministic, no LLM

  # ---------------------------------------------------------------------------
  # 4. SCORING: ISOLATED, PROVENANCE-BLINDED, ORDER-RANDOMIZED -> Z per candidate
  # ---------------------------------------------------------------------------
  # Every candidate (real, counterfactual-decoy, swap) scored in ITS OWN call with source/
  # identity masked; identical template; document prefix cached. Two elicitations:
  #  PRIMARY (main S1 + crux, scorer=PRIMARY_MODEL): logprob P(entailed). One call: ask
  #    'Is this claim entailed by the document? Answer Yes or No.' read top_logprobs of the
  #    first answer token; Z = softmax over {Yes,No} logits -> P(Yes) in (0,1) (fine-grained,
  #    avoids ties, best tail resolution). Probe logprobs non-null first (see TESTING).
  #  PORTABLE (used for the G!=S ablation on BOTH models so family is the only variable, and
  #    as the nano fallback if logprobs are null): K_SC isolated Yes/No+confidence(0-100) calls
  #    at temp~0.7; per call p = conf/100 if Yes else 1-conf/100; Z = mean(p over K_SC).
  def score(model, d, cand, elic):
      if elic=='logprob': r=LLM(model, ENTAIL_PROMPT_BLIND(d.doc,cand)); log_cost(r); return softmax_yes(r)
      else: ps=[yn_conf(LLM(model,ENTAIL_PROMPT_BLIND(d.doc,cand),temp=0.7)) for _ in range(K_SC)];
            [log_cost(x) for x in ...]; return mean(ps)
  # RANK-NORMALIZE within each document: pool all candidate Z of d, map to [0,1] ranks so
  # per-document scoring-scale differences cancel; tiny deterministic jitter (hash(cand_id,SEED))
  # breaks exact ties. Store Z_real, Z_decoy(cf), Z_swap (all rank-normalized).

  # ---------------------------------------------------------------------------
  # 5. CANONICAL W_i + KNOCKOFF+ OPERATIVE CUTOFF (research_out.json A.2/A.6)
  # ---------------------------------------------------------------------------
  # Pair each real i with its matched decoy (counterfactual for the headline; swap for control).
  def W(Zr, Zd):  return max(Zr,Zd) * sign(Zr - Zd)        # signed-max (magnitude max, sign by winner)
  def knockoff_plus_T(Ws, alpha):                          # eq 1.9; most-permissive feasible cutoff
      for t in sorted(unique(abs(Ws))):
          pos=sum(w>=t for w in Ws); neg=sum(w<=-t for w in Ws)
          if (1+neg)/max(1,pos) <= alpha: return t,pos,(1+neg)/max(1,pos)
      return inf,0,1.0
  # Operative cutoff: per alpha in ALPHA_GRID with achievable admissions >= ceil(1/alpha),
  # compute T(alpha). 'Tail/admission region' for a diagnostic = {pairs with |W_i| >= T(alpha*)}.
  # alpha* = the most permissive CERTIFIED alpha (admissions >= k-floor). Drop alphas whose
  # k-floor is unreached and REPORT them as preconditions (never 'confirmed by conservatism').

  # ---------------------------------------------------------------------------
  # 6. S1 DECOY SIGNATURE (per decoy family: counterfactual vs random-swap)
  # ---------------------------------------------------------------------------
  # Restrict to KNOWN-FALSE reals (label=='FALSE') -> the population whose exchangeability matters.
  for fam in ['counterfactual','random_swap']:
    pairs = [(d, Zr=c.Zreal, Zd=(c.Zdecoy if fam=='counterfactual' else c.Zswap))
             for d in DOCS for c in d.spont_errs]
    for alpha in CERTIFIED_ALPHAS:
       T = knockoff_plus_T([W(p.Zr,p.Zd) for p in ALLPAIRS], alpha)
       tail = [p for p in pairs if max(p.Zr,p.Zd) >= T]
       win_rate = mean(p.Zd > p.Zr for p in tail)                   # decoy-wins fraction; target ~0.5
       # one-sided upper-tail two-sample tests on scores restricted to admission region:
       ks  = ks_2samp_one_sided(decoy_scores_in_tail, falsereal_scores_in_tail)  # decoy < real?
       mw  = mannwhitney_one_sided(decoy_scores_in_tail, falsereal_scores_in_tail)
       ci  = doc_block_bootstrap(stat=win_rate_fn, units=DOCS, B=B_BOOT, seed=SEED)  # whole-doc resample
       record(fam, alpha, win_rate, ci, ks.p, mw.p, n_tail=len(tail))
  # EXPECTED: counterfactual win_rate CI covers 0.5 & KS/MW non-significant (exchangeable);
  #           random_swap win_rate measurably < 0.5 & KS/MW significant (anti-conservative) ->
  #           validates the diagnostic's SENSITIVITY (it can detect a bad decoy family).
  # Also report a tail-cutoff ROBUSTNESS sweep at quantiles {top50%,top25%,top10%, knockoff+T}.

  # ---------------------------------------------------------------------------
  # 7. SPONTANEOUS-ERROR TAIL MATCH  (THE LOAD-BEARING CRUX)
  # ---------------------------------------------------------------------------
  # Build THREE score pools (rank-normalized, pooled over docs):
  #   F_truepos  = Z of TRUE reals          (the WRONG matching target)
  #   F_spont    = Z of FALSE reals          (spontaneous extractor errors = the RIGHT target)
  #   F_decoy    = Z of counterfactual decoys (deliberately generated null population)
  for region in ['admission_tail(|.|>=T(alpha*))','top25pct','full']:
    test_match  = two_sample_tail(F_decoy, F_spont,   region)   # WANT: fail-to-reject (decoy ~ spont)
    test_differ = two_sample_tail(F_decoy, F_truepos, region)   # WANT: reject (decoy NOT ~ truepos)
    gap = {'ks_sup': ks_sup_in_region(F_decoy,F_spont),
           'wasserstein_tail': W1(F_decoy_tail,F_spont_tail),
           'mean_diff': mean(F_decoy_tail)-mean(F_spont_tail),
           'cliffs_delta': cliffs(F_decoy_tail,F_spont_tail)}      # signed: + => decoys too HARD
    ci_gap = doc_block_bootstrap(stat=ks_sup_fn, units=DOCS, B=B_BOOT)
    record_crux(region, test_match.p, test_differ.p, gap, ci_gap)
  # two_sample_tail := primary one-sided KS; SUPPLEMENT with Anderson-Darling + a permutation
  # two-sample test (robust when tail n is small). EXPORT figure-ready CDF arrays for all three
  # pools (x grid + empirical CDF) so the paper can draw the overlaid tail CDFs.
  # VERDICT: decoy family is VALID iff (decoy~spont fail-to-reject after BH) AND (decoy!=truepos
  # rejected). Else report the GAP + direction (too-easy=anti-conservative / too-hard=conservative)
  # and flag 're-tune decoy family' rather than asserting validity.

  # ---------------------------------------------------------------------------
  # 8. GENERATOR != SCORER ABLATION (S2b de-circularization)  [PORTABLE elicitation]
  # ---------------------------------------------------------------------------
  # Run on the 40-doc PILOT slice to cap cost. Four configs over (G=decoy generator, S=scorer):
  CONFIGS = [('nano','nano'), ('nano','OTHER'), ('OTHER','nano'), ('OTHER','OTHER')]
  #   G changes which model wrote the decoys (re-generate decoys with OTHER for G=OTHER configs).
  #   S changes which model scores (re-score reals+decoys with S, PORTABLE elicitation for ALL
  #   so model FAMILY is the only variable). nano also scored with PORTABLE here for apples-to-apples.
  for (g,s) in CONFIGS:
     decoys_g = decoys generated by model g (reuse sec.3 for g==G_main; else regenerate)
     Z = {cand: score(model=s, d, cand, elic='portable') for cand in reals+decoys_g+swaps}
     win_rate_cf = tail_conditioned_win_rate(false_reals, decoys_g, S=s)   # sec.6 machinery
     ks_p, mw_p  = upper_tail_two_sample(...)
     small_diag  = { alpha: realized_FDR_vs_crispgold(knockoff+ admit set at alpha) for alpha in
                     CERTIFIED_ALPHAS }                # labeled-slice diagonal (gold = exact)
     ci = doc_block_bootstrap(B=B_BOOT)
     record_ablation((g,s), win_rate_cf, ci, ks_p, mw_p, small_diag)
  # VERDICT logic:
  #   if win_rate ~0.5 AND diagonal tracked for ALL configs (incl. G!=S) -> 'ROBUST: not a
  #       shared-model artifact' (de-circularization PASSES; strongest outcome).
  #   if exchangeability/diagonal hold ONLY when g==s -> 'SHARED-MODEL ARTIFACT (localized
  #       negative result)': report explicitly, do NOT count as confirmation.
  #   Emit a VALIDITY-REGION STATEMENT naming the (G,S) pairs over which the control is calibrated.

  # ---------------------------------------------------------------------------
  # 9. MULTIPLICITY: BENJAMINI-HOCHBERG ACROSS ALL VALIDATION TESTS
  # ---------------------------------------------------------------------------
  # Collect every p (S1 KS/MW per fam x alpha; crux match/differ per region; ablation KS/MW per
  # config). Apply BH at q=0.05; report raw p, BH-adjusted p, reject flag in one table.

  # ---------------------------------------------------------------------------
  # 10. OUTPUT method_out.json  (validate with aii-json; split if >file-size-limit)
  # ---------------------------------------------------------------------------
  method_out = {
    'meta': {models:{primary,other}, ALPHA_GRID, certified_alphas, TAU, B_BOOT, K_SC, SEED,
             n_docs, n_reals, n_true, n_spont, contamination_rate, elicitation, cost_usd:COST,
             logprobs_available, cached_tokens_observed},
    's1_decoy_signature': [{family, alpha, T, n_tail, tail_win_rate, win_rate_ci,
                            ks_stat, ks_p, mw_stat, mw_p, robustness_sweep}],
    'spontaneous_error_match': {regions:[{region, decoy_vs_spont_p, decoy_vs_truepos_p, gap{...},
                            gap_ci, verdict}], figure_cdfs:{x, cdf_truepos, cdf_spont, cdf_decoy}},
    'generator_ne_scorer': {configs:[{G,S, tail_win_rate, win_rate_ci, ks_p, mw_p, small_diagonal}],
                            verdict:'ROBUST'|'SHARED_MODEL_ARTIFACT', validity_region_statement},
    'bh_correction': [{test_name, raw_p, bh_adj_p, reject}],
    'bootstrap': {method:'document-block', B:B_BOOT},
    'cost_trace_path':'logs/cost.jsonl'
  }
  write_json('method_out.json', method_out); aii_json_validate(method_out)
fallback_plan: >-
  LOGPROBS UNAVAILABLE on gpt-4.1-nano route (probe returns null): drop the logprob elicitation and use the PORTABLE self-consistency
  elicitation (K_SC isolated Yes/No+confidence, Z=mean per-call p) as PRIMARY everywhere; it is logprob-free and already the
  ablation default, so nothing else changes. CACHING NOT FIRING (cached_tokens==0): proceed anyway (docs are tiny, ~100 tokens)
  but lower the candidate over-generation / doc count to hold the soft cap. DIFFERENT-FAMILY MODEL PROBLEMS (degenerate/constant
  scores, no Yes/No separation, or >$0.30/M): try the next family in order qwen -> llama -> mistral via aii-openrouter-llms;
  if none gives usable separation, report the ablation on the best-available cross-family pair and state the limitation (do
  not fabricate a clean G!=S result). SPONTANEOUS ERRORS TOO SPARSE (N_spont<40 after enrichment): push harder over-generation
  (force multi-hop inference on every entity pair, raise temperature, draw more long-k confirmatory docs), then pool atomic+multi-hop;
  if still <40, report the crux + S1 as UNDERPOWERED/UNTESTABLE with the measured false-admission base-rate (a precondition
  outcome) instead of asserting a noisy ~0.5. TAIL TOO THIN at knockoff+ T (few |W|>=T pairs): report diagnostics at multiple
  tail quantiles (top50/25/10%) and at the most permissive CERTIFIED alpha; if every region is underpowered, present effect
  sizes (Wasserstein, Cliff's delta) descriptively with CIs and explicitly decline a significance verdict. KS UNDERPOWERED:
  supplement with Anderson-Darling + a permutation two-sample test and always report effect sizes regardless of p. COUNTERFACTUAL
  DECOY CONTAMINATION (accidentally gold-entailed): CLUTRR gold is crisp, so reject deterministically via gold membership
  and regenerate; report contamination_rate and a sensitivity sweep. COST projection > soft cap after the smoke test: reduce
  K_SC (5->3), cap candidates/doc, or shrink the confirmatory subset (keep admissions >= the smallest certified-alpha k-floor);
  the logprob path is cheapest, prefer it. WORST CASE (LLM access flaky): cache every raw response to disk keyed by (model,prompt_hash)
  so re-runs are free and partial results survive; the stats pipeline (sections 5-9) runs offline on cached scores. NEVER
  exceed $10 (assert in log_cost aborts the run).
testing_plan: >-
  STAGE 0 -- OFFLINE STATS UNIT TESTS (no API, no cost): (a) knockoff_plus_T on the spec's worked example must reproduce the
  eq-1.9 threshold and the k-floor mapping {0.05->20,...,0.5->2}; assert it admits nothing when no feasible cutoff exists.
  (b) W() signed-max: assert magnitude==max(Zr,Zd) and sign flips when real/decoy swapped (antisymmetry). (c) SYNTHETIC SCORER
  sanity: generate fake scores where decoy signs are fair coins -> tail win-rate CI must cover 0.5 and KS non-significant;
  where decoys are deliberately 'too easy' (shift decoy scores down) -> win-rate CI below 0.5 and KS significant (confirms
  the diagnostic detects anti-conservatism). (d) doc_block_bootstrap returns wider CIs than naive i.i.d. bootstrap on clustered
  synthetic data. (e) label() unit tests on the 3 mini_data_out.json examples: TRUE for listed atomic/multi-hop triples, FALSE
  for a contradicting relation on an enumerated pair, UNDECIDABLE for an unlisted pair. STAGE 1 -- 1-CALL API PROBES (<$0.01):
  confirm gpt-4.1-nano returns non-null logprobs/top_logprobs; confirm usage.prompt_tokens_details.cached_tokens>0 on a repeated
  document prefix; confirm the chosen OTHER_MODEL returns parseable Yes/No+confidence (and logprobs if claimed). Select elicitation
  per Stage-1 outcome. STAGE 2 -- 3-DOC SMOKE (pilot, mix k=2/k=6/k=10 from mini set; <$0.05): run extraction->decoy->scoring
  end-to-end; eyeball that (i) over-generation yields some spontaneous FALSE reals (especially on k=10), (ii) counterfactual
  decoys are gold-verified non-entailed and surface-matched, (iii) scores vary (not all 0/1), (iv) cost-per-doc extrapolates
  under the soft cap. STAGE 3 -- 40-DOC PILOT (confirmation gate, target <~$0.7): compute S1 + crux. CONFIRMATION SIGNALS
  to see before scaling: counterfactual tail win-rate CI includes 0.5 while random-swap CI sits clearly below 0.5; F_decoy
  tracks F_spont (fail-to-reject) and departs from F_truepos (reject) in the tail; N_spont>=40. If signals are absent, branch
  to the matching fallback (enrich errors / re-tune decoys / widen tail region) BEFORE spending more. STAGE 4 -- SCALE + ABLATION:
  add the bounded confirmatory subset for the headline S1/crux numbers, then run the four-config G!=S ablation on the 40 pilot
  docs with the portable elicitation. Run B>=2000 document-block bootstrap and BH only at the end on the full result set.
  Throughout: log cumulative cost after EVERY call, print a running total each batch, and hard-stop at $10; checkpoint cached
  responses so any interruption resumes for free. Final: aii-json validate method_out.json and aii-file-size-limit check/split.
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

### [2] HUMAN-USER prompt · 2026-06-16 06:13:25 UTC

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

### [3] SKILL-INPUT — aii-openrouter-llms · 2026-06-16 06:13:39 UTC

The agent loaded the **aii-openrouter-llms** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-openrouter-llms
description: Searches and calls LLMs from OpenRouter's extensive catalog (Claude, GPT, Gemini, Llama, Mistral, DeepSeek, etc.) with reasoning and temperature control. Use when user needs to access various LLMs, compare language models, call different model providers, find the best model for a task, or look up model pricing and costs per million tokens.
---

## Contents

- Workflow (2-phase model discovery and calling)
- Scripts (Search, Get Params, Call)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: Model Discovery and Calling

### Phase 1: Search for Models
Find models with pricing, context length, and descriptions
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

### Phase 2 (optional): Get Model Parameters
Check what parameters a specific model supports
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

### Phase 3: Call Model
Call a model using the API name from search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

---

## Scripts

### Search OpenRouter models (aii_or_search_llms.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_search_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 5' ::: 'claude' 'gpt' 'gemini'
```

**Example output:**
```
Found 5 models for query: claude

[1] Anthropic: Claude Opus 4.5
    API: anthropic/claude-opus-4.5
    Context: 200,000 tokens
    Price: $5.00/M in, $25.00/M out
    Claude Opus 4.5 is Anthropic's frontier reasoning model...

[2] Anthropic: Claude Haiku 4.5
    API: anthropic/claude-haiku-4.5
    Context: 200,000 tokens
    Price: $1.00/M in, $5.00/M out
    ...
```

**Parameters:**

`query` (optional, positional)
- Search query to filter models (e.g., 'claude', 'gpt', 'reasoning')

`--limit, -n` (optional)
- Maximum number of results (default: 10)

`--series, -s` (optional)
- Filter by model family
- Valid: GPT, Claude, Gemini, Grok, Cohere, Nova, Qwen, Yi, DeepSeek, Mistral, Llama2, Llama3, Llama4, RWKV, Qwen3, Router, Media, Other, PaLM

`--timeout` (optional)
- Request timeout in seconds (default: 60)

**Tips:**
- Use the `API` field from results for the `--model` parameter in calls
- Search is fast (queries OpenRouter's model list)

---

### Get model parameters (aii_or_get_llm_params.py)

Get detailed information and supported parameters for a specific model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

**Parallel execution (multiple models):**

IMPORTANT: When checking multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_get_llm_params.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: Anthropic: Claude Haiku 4.5
API: anthropic/claude-haiku-4.5

=== Capabilities ===
Context Length: 200,000 tokens
Max Output: 64,000 tokens
Modality: text+image->text
Input: image, text
Output: text
Moderated: Yes

=== Pricing ===
Input: $1.0000/M tokens
Output: $5.0000/M tokens

=== Supported Parameters ===
  - include_reasoning
  - max_tokens
  - reasoning
  - stop
  - temperature
  - tool_choice
  - tools
  - top_k
  - top_p
```

**Parameters:**

`model` (required, positional)
- Model API name (e.g., 'anthropic/claude-haiku-4.5', 'openai/o1')

`--timeout` (optional)
- Request timeout in seconds (default: 30)

**Tips:**
- Use after search to see which parameters a model supports
- Check supported_parameters before using --reasoning or other options

---

### Call OpenRouter model (aii_or_call_llms.py)

Make an API call to an OpenRouter LLM model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

**Parallel execution (multiple calls):**

IMPORTANT: When calling multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_call_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --model {} --input "What is 2+2?"' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: anthropic/claude-haiku-4.5

Response:
Four.

Tokens: 12 in, 5 out
```

**Parameters:**

`--model, -m` (required)
- API model name from search results (format: `provider/model-name`)
- Examples: `anthropic/claude-sonnet-4`, `openai/gpt-5`, `google/gemini-2.5-pro`

`--input, -i` (required, unless using --input-json)
- Simple string prompt

`--input-json` (optional)
- Full conversation JSON for multi-turn (mutually exclusive with --input)

`--max-tokens` (optional)
- Maximum output tokens (default: 9000)

`--reasoning` (optional)
- Reasoning effort for reasoning models: `minimal`, `low`, `medium`, `high`

`--temperature, -t` (optional)
- Randomness (0.0-2.0): 0.0=deterministic, 0.7=balanced, 1.5+=creative

`--top-p` (optional)
- Nucleus sampling (0.0-1.0)

`--instructions` (optional)
- System instructions/prompt

`--web-search` (optional)
- Enable web search with max results (e.g., 10)

`--params, -p` (optional)
- Extra model-specific parameters as JSON string
- Use `aii_or_get_llm_params.py` to see which params a model supports
- Example: `--params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'`

`--timeout` (optional)
- Request timeout in seconds (default: 120)

**Examples:**

Simple call:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "Write a haiku about coding" \
  --temperature 0.8
```

With system instructions:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-haiku-4.5" \
  --input "Explain recursion" \
  --instructions "You are a helpful programming tutor. Keep explanations concise."
```

With reasoning (for o1-style models):
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "openai/o1" \
  --input "Solve this complex math problem" \
  --reasoning high
```

With web search:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "What are the latest AI news?" \
  --web-search 10 \
  --max-tokens 15000
```

With extra model-specific params:
```bash
# Step 1: Check what params the model supports
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "meta-llama/llama-3.3-70b-instruct"
# Shows: frequency_penalty, top_k, seed, min_p, etc.

# Step 2: Call with those params
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "meta-llama/llama-3.3-70b-instruct" \
  --input "Write a short poem" \
  --params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'
```

---

## Tips

- Use `aii_or_search_llms.py` first to find models, then copy `API` field for `--model`
- Use `aii_or_get_llm_params.py` to check what params a model supports before using `--params`
- For web search, increase `--max-tokens` to handle larger responses (15000+)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 06:13:39 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-16 06:13:49 UTC

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

### [6] SKILL-INPUT — aii-parallel-computing · 2026-06-16 06:13:49 UTC

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

### [7] SKILL-INPUT — aii-python · 2026-06-16 06:13:57 UTC

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

### [8] SKILL-INPUT — aii-use-hardware · 2026-06-16 06:13:57 UTC

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

### [9] SKILL-INPUT — aii-file-size-limit · 2026-06-16 06:13:57 UTC

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

### [10] SYSTEM-USER prompt · 2026-06-16 07:50:24 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/results/out.json`
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
  S1 Tail-Exchangeability + Spontaneous-Error Match + Generator!=Scorer De-Circularization on CLUTRR Crisp Gold
summary: >-
  Elevate two methodology-defense results to first-class empirical numbers on a labeled CLUTRR slice (40 pilot + bounded confirmatory
  subset). (1) DECOY SIGNATURE (S1): tail-conditioned win-rate (~0.5) and upper-tail two-sample CDF tests (KS + tail Mann-Whitney)
  on known-false reals vs document-conditioned counterfactual decoys, with random type-matched swaps as the predicted anti-conservative
  control that validates diagnostic sensitivity. (2) SPONTANEOUS-ERROR TAIL MATCH (the reviewer's named crux): show counterfactual-decoy
  scores reproduce the GENUINE extractor-error (spontaneous false-real) tail distribution, NOT the true-positive distribution,
  with a reported matching gap. (3) GENERATOR!=SCORER ABLATION (S2b): re-run win-rate/CDF tests and a small labeled-slice
  diagonal with decoys from family G scored by a DIFFERENT-family S (and the symmetric swap); if exchangeability/diagonal
  hold only when G=S, report a localized shared-model artifact (a reported negative result). Canonical W_i; document-block
  bootstrap (B>=2000); BH multiplicity correction; isolated provenance-blinded scoring; cheap sub-$0.30/M models with caching;
  gradual scaling; cumulative cost logged after EVERY call; soft cap ~$1.5, HARD STOP $10. Output method_out.json with tables,
  figure-ready CDFs, and the G==S vs G!=S verdict + validity-region statement.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # ============================================================================
  # EXPERIMENT: S1 decoy-signature + spontaneous-error match + G!=S de-circularization
  # CPU-only; all LLM calls via OpenRouter (aii-openrouter-llms skill). Read skills:
  #   aii-openrouter-llms, aii-parallel-computing (async), aii-long-running-tasks
  #   (gradual scaling), aii-json (validate method_out.json), aii-use-hardware.
  # Dataset dependency files are READ-ONLY; do not re-derive gold rules by hand.
  # ============================================================================

  # ---------------------------------------------------------------------------
  # 0. SETUP, CONSTANTS, COST GUARDRAILS
  # ---------------------------------------------------------------------------
  SEED = 20240617
  ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]      # k-floors = ceil(1/a) = {20,10,5,4,2}
  TAU = 0.05                                       # FDR-vs-alpha tolerance (report sensitivity {0,0.05})
  B_BOOT = 2000                                    # document-block bootstrap replicates (>=2000)
  N_FALSE_MIN = 40                                 # spontaneous-error populability floor (pooled)
  K_SC = 5                                          # self-consistency samples (portable elicitation)
  SOFT_CAP_USD = 1.5; HARD_STOP_USD = 10.0
  PRIMARY_MODEL = 'openai/gpt-4.1-nano'            # $0.10/$0.40 per M, logprobs+auto-cache
  # Different-FAMILY scorer for the ablation: pick a current cheap (<$0.30/M input) NON-OpenAI
  # instruct model via the aii-openrouter-llms skill, preferring one that exposes logprobs.
  # Default candidates in order: qwen/* flash/instruct, meta-llama/llama-3.x-instruct,
  # mistralai/* small. Bind the resolved id to OTHER_MODEL.

  COST = 0.0    # cumulative USD; updated after EVERY call from response usage + price table
  def log_cost(resp):
      global COST
      COST += price(resp.model, resp.usage)        # cached_tokens billed at provider read-mult
      append_jsonl('logs/cost.jsonl', {'model':resp.model,'usage':resp.usage,'cum_usd':COST})
      assert COST < HARD_STOP_USD, f'HARD STOP: spend {COST} reached cap'   # crash-safe abort

  # OpenRouter call wrapper: async, retry w/ backoff, isolated (one candidate per call),
  # provenance-blinded prompt, order of any in-prompt options randomized by SEED.
  # Concurrency via asyncio.Semaphore (e.g. 24); see aii-parallel-computing.

  # ---------------------------------------------------------------------------
  # 1. LOAD DATA + BUILD CRISP GOLD AND THE KNOWN-FALSE LABELER
  # ---------------------------------------------------------------------------
  # Dep1 dataset: .../iter_1/gen_art/gen_art_dataset_1/full_data_out.json (190 ex).
  # Dep2 spec   : .../iter_1/gen_art/gen_art_research_1/research_out.json (formulas).
  rows = load_json(full_data_out.json).datasets[0].examples
  for r in rows:
      inp = json.loads(r.input); out = json.loads(r.output)        # STRING fields -> json.loads
      r.entities=inp.entities; r.doc=inp.document_text; r.query=inp.query; r.k=r.metadata_chain_length_k
      r.is_pilot=r.metadata_is_pilot
      # GOLD_TRUE: directed triples that are entailed/derivable = atomic_facts UNION multi_hop_facts.
      r.gold_true = set((f.head,f.relation,f.tail) for f in out.atomic_facts + out.multi_hop_facts)
      # Canonical relation per ORDERED pair (kinship pair has a unique directed relation):
      r.gold_rel = { (h,t): rel for (h,rel,t) in r.gold_true }      # used for crisp labeling
      r.gold_pairs = set(r.gold_rel.keys())
  RELATIONS = full_data.metadata.relation_vocabulary               # 20 kinship relations

  def label(doc_row, h, rel, t):
      # CRISP 3-way label vs CLUTRR gold (exact, no annotation noise):
      if (h,rel,t) in doc_row.gold_true:                 return 'TRUE'
      if (h,t) in doc_row.gold_pairs and rel!=doc_row.gold_rel[(h,t)]: return 'FALSE'  # contradiction
      return 'UNDECIDABLE'   # pair not enumerated in gold (distant/no-vocab) -> excluded from crisp sets
  # Rationale: restricting FALSE to enumerated-pair contradictions avoids mislabeling unlisted
  # inverse/distant relations; keeps the known-false set defensible and exact.

  # ---------------------------------------------------------------------------
  # 2. EXTRACTION (OVER-GENERATE TO DENSIFY SPONTANEOUS ERRORS -> the crux's data)
  # ---------------------------------------------------------------------------
  # One extraction call per document (generation, not scoring -> batching OK here).
  # Prompt G to extract BOTH (a) atomic stated kinship facts and (b) ALL multi-hop
  # inferred kinship relations among entity pairs it can derive (push long chains).
  # Multi-hop is the ERROR-DENSE family; long-k docs yield the most spontaneous errors.
  for d in DOCS:
      raw = LLM_generate(G, EXTRACT_PROMPT(d.doc, d.entities, RELATIONS)); log_cost(raw)
      d.reals = parse_triples(raw)                       # dedupe; keep only entity pairs in d
      for c in d.reals: c.lab = label(d, c.head, c.rel, c.tail)
      d.true_reals  = [c for c in d.reals if c.lab=='TRUE']
      d.spont_errs  = [c for c in d.reals if c.lab=='FALSE']   # GENUINE extractor errors (target dist)
      # drop UNDECIDABLE reals from crisp diagnostics (logged for transparency)
  N_spont = sum(len(d.spont_errs) for d in DOCS)
  if N_spont < N_FALSE_MIN:   # enrich: more long-k docs, higher temperature, stronger over-gen prompt
      enrich_until(N_spont>=N_FALSE_MIN OR exhausted); if still short -> mark crux 'UNDERPOWERED'

  # ---------------------------------------------------------------------------
  # 3. DECOY GENERATION (matched counterfactual) + RANDOM-SWAP NEGATIVE CONTROL
  # ---------------------------------------------------------------------------
  # For EACH real candidate c=(h,rel,t) build a 1:1 matched decoy and a swap control.
  # (A) COUNTERFACTUAL DECOY (PRIMARY, property-matched, DeepCoy principle): ask G for the
  #     MOST PLAUSIBLE ALTERNATIVE kinship relation for the SAME ordered pair (h,t), i.e.
  #     identical surface form/entities/specificity, differing only in relation. Take the
  #     model's top suggestion; if it equals the crisp gold relation (decoy would be TRUE),
  #     take the next suggestion. VERIFY NON-ENTAILMENT deterministically vs crisp gold:
  #     accept iff (h,rel_decoy,t) not in gold_true AND rel_decoy != gold_rel[(h,t)].
  #     For FALSE reals also require rel_decoy != c.rel (decoy must differ from the real).
  #     Log contamination_rate = #(generated decoys that were gold-entailed)/#generated.
  # (B) RANDOM TYPE-MATCHED SWAP (negative control, EXPECTED anti-conservative): keep (h,rel),
  #     replace t by a random same-type (person) entity t' in d, t'!=t; verify non-entailed.
  for d in DOCS:
    for c in d.reals:
       c.decoy = gen_counterfactual(G, d, c); log_cost(...); verify_nonentailment_via_gold(c.decoy)
       c.swap  = random_type_matched_swap(d, c, rng=SEED)            # deterministic, no LLM

  # ---------------------------------------------------------------------------
  # 4. SCORING: ISOLATED, PROVENANCE-BLINDED, ORDER-RANDOMIZED -> Z per candidate
  # ---------------------------------------------------------------------------
  # Every candidate (real, counterfactual-decoy, swap) scored in ITS OWN call with source/
  # identity masked; identical template; document prefix cached. Two elicitations:
  #  PRIMARY (main S1 + crux, scorer=PRIMARY_MODEL): logprob P(entailed). One call: ask
  #    'Is this claim entailed by the document? Answer Yes or No.' read top_logprobs of the
  #    first answer token; Z = softmax over {Yes,No} logits -> P(Yes) in (0,1) (fine-grained,
  #    avoids ties, best tail resolution). Probe logprobs non-null first (see TESTING).
  #  PORTABLE (used for the G!=S ablation on BOTH models so family is the only variable, and
  #    as the nano fallback if logprobs are null): K_SC isolated Yes/No+confidence(0-100) calls
  #    at temp~0.7; per call p = conf/100 if Yes else 1-conf/100; Z = mean(p over K_SC).
  def score(model, d, cand, elic):
      if elic=='logprob': r=LLM(model, ENTAIL_PROMPT_BLIND(d.doc,cand)); log_cost(r); return softmax_yes(r)
      else: ps=[yn_conf(LLM(model,ENTAIL_PROMPT_BLIND(d.doc,cand),temp=0.7)) for _ in range(K_SC)];
            [log_cost(x) for x in ...]; return mean(ps)
  # RANK-NORMALIZE within each document: pool all candidate Z of d, map to [0,1] ranks so
  # per-document scoring-scale differences cancel; tiny deterministic jitter (hash(cand_id,SEED))
  # breaks exact ties. Store Z_real, Z_decoy(cf), Z_swap (all rank-normalized).

  # ---------------------------------------------------------------------------
  # 5. CANONICAL W_i + KNOCKOFF+ OPERATIVE CUTOFF (research_out.json A.2/A.6)
  # ---------------------------------------------------------------------------
  # Pair each real i with its matched decoy (counterfactual for the headline; swap for control).
  def W(Zr, Zd):  return max(Zr,Zd) * sign(Zr - Zd)        # signed-max (magnitude max, sign by winner)
  def knockoff_plus_T(Ws, alpha):                          # eq 1.9; most-permissive feasible cutoff
      for t in sorted(unique(abs(Ws))):
          pos=sum(w>=t for w in Ws); neg=sum(w<=-t for w in Ws)
          if (1+neg)/max(1,pos) <= alpha: return t,pos,(1+neg)/max(1,pos)
      return inf,0,1.0
  # Operative cutoff: per alpha in ALPHA_GRID with achievable admissions >= ceil(1/alpha),
  # compute T(alpha). 'Tail/admission region' for a diagnostic = {pairs with |W_i| >= T(alpha*)}.
  # alpha* = the most permissive CERTIFIED alpha (admissions >= k-floor). Drop alphas whose
  # k-floor is unreached and REPORT them as preconditions (never 'confirmed by conservatism').

  # ---------------------------------------------------------------------------
  # 6. S1 DECOY SIGNATURE (per decoy family: counterfactual vs random-swap)
  # ---------------------------------------------------------------------------
  # Restrict to KNOWN-FALSE reals (label=='FALSE') -> the population whose exchangeability matters.
  for fam in ['counterfactual','random_swap']:
    pairs = [(d, Zr=c.Zreal, Zd=(c.Zdecoy if fam=='counterfactual' else c.Zswap))
             for d in DOCS for c in d.spont_errs]
    for alpha in CERTIFIED_ALPHAS:
       T = knockoff_plus_T([W(p.Zr,p.Zd) for p in ALLPAIRS], alpha)
       tail = [p for p in pairs if max(p.Zr,p.Zd) >= T]
       win_rate = mean(p.Zd > p.Zr for p in tail)                   # decoy-wins fraction; target ~0.5
       # one-sided upper-tail two-sample tests on scores restricted to admission region:
       ks  = ks_2samp_one_sided(decoy_scores_in_tail, falsereal_scores_in_tail)  # decoy < real?
       mw  = mannwhitney_one_sided(decoy_scores_in_tail, falsereal_scores_in_tail)
       ci  = doc_block_bootstrap(stat=win_rate_fn, units=DOCS, B=B_BOOT, seed=SEED)  # whole-doc resample
       record(fam, alpha, win_rate, ci, ks.p, mw.p, n_tail=len(tail))
  # EXPECTED: counterfactual win_rate CI covers 0.5 & KS/MW non-significant (exchangeable);
  #           random_swap win_rate measurably < 0.5 & KS/MW significant (anti-conservative) ->
  #           validates the diagnostic's SENSITIVITY (it can detect a bad decoy family).
  # Also report a tail-cutoff ROBUSTNESS sweep at quantiles {top50%,top25%,top10%, knockoff+T}.

  # ---------------------------------------------------------------------------
  # 7. SPONTANEOUS-ERROR TAIL MATCH  (THE LOAD-BEARING CRUX)
  # ---------------------------------------------------------------------------
  # Build THREE score pools (rank-normalized, pooled over docs):
  #   F_truepos  = Z of TRUE reals          (the WRONG matching target)
  #   F_spont    = Z of FALSE reals          (spontaneous extractor errors = the RIGHT target)
  #   F_decoy    = Z of counterfactual decoys (deliberately generated null population)
  for region in ['admission_tail(|.|>=T(alpha*))','top25pct','full']:
    test_match  = two_sample_tail(F_decoy, F_spont,   region)   # WANT: fail-to-reject (decoy ~ spont)
    test_differ = two_sample_tail(F_decoy, F_truepos, region)   # WANT: reject (decoy NOT ~ truepos)
    gap = {'ks_sup': ks_sup_in_region(F_decoy,F_spont),
           'wasserstein_tail': W1(F_decoy_tail,F_spont_tail),
           'mean_diff': mean(F_decoy_tail)-mean(F_spont_tail),
           'cliffs_delta': cliffs(F_decoy_tail,F_spont_tail)}      # signed: + => decoys too HARD
    ci_gap = doc_block_bootstrap(stat=ks_sup_fn, units=DOCS, B=B_BOOT)
    record_crux(region, test_match.p, test_differ.p, gap, ci_gap)
  # two_sample_tail := primary one-sided KS; SUPPLEMENT with Anderson-Darling + a permutation
  # two-sample test (robust when tail n is small). EXPORT figure-ready CDF arrays for all three
  # pools (x grid + empirical CDF) so the paper can draw the overlaid tail CDFs.
  # VERDICT: decoy family is VALID iff (decoy~spont fail-to-reject after BH) AND (decoy!=truepos
  # rejected). Else report the GAP + direction (too-easy=anti-conservative / too-hard=conservative)
  # and flag 're-tune decoy family' rather than asserting validity.

  # ---------------------------------------------------------------------------
  # 8. GENERATOR != SCORER ABLATION (S2b de-circularization)  [PORTABLE elicitation]
  # ---------------------------------------------------------------------------
  # Run on the 40-doc PILOT slice to cap cost. Four configs over (G=decoy generator, S=scorer):
  CONFIGS = [('nano','nano'), ('nano','OTHER'), ('OTHER','nano'), ('OTHER','OTHER')]
  #   G changes which model wrote the decoys (re-generate decoys with OTHER for G=OTHER configs).
  #   S changes which model scores (re-score reals+decoys with S, PORTABLE elicitation for ALL
  #   so model FAMILY is the only variable). nano also scored with PORTABLE here for apples-to-apples.
  for (g,s) in CONFIGS:
     decoys_g = decoys generated by model g (reuse sec.3 for g==G_main; else regenerate)
     Z = {cand: score(model=s, d, cand, elic='portable') for cand in reals+decoys_g+swaps}
     win_rate_cf = tail_conditioned_win_rate(false_reals, decoys_g, S=s)   # sec.6 machinery
     ks_p, mw_p  = upper_tail_two_sample(...)
     small_diag  = { alpha: realized_FDR_vs_crispgold(knockoff+ admit set at alpha) for alpha in
                     CERTIFIED_ALPHAS }                # labeled-slice diagonal (gold = exact)
     ci = doc_block_bootstrap(B=B_BOOT)
     record_ablation((g,s), win_rate_cf, ci, ks_p, mw_p, small_diag)
  # VERDICT logic:
  #   if win_rate ~0.5 AND diagonal tracked for ALL configs (incl. G!=S) -> 'ROBUST: not a
  #       shared-model artifact' (de-circularization PASSES; strongest outcome).
  #   if exchangeability/diagonal hold ONLY when g==s -> 'SHARED-MODEL ARTIFACT (localized
  #       negative result)': report explicitly, do NOT count as confirmation.
  #   Emit a VALIDITY-REGION STATEMENT naming the (G,S) pairs over which the control is calibrated.

  # ---------------------------------------------------------------------------
  # 9. MULTIPLICITY: BENJAMINI-HOCHBERG ACROSS ALL VALIDATION TESTS
  # ---------------------------------------------------------------------------
  # Collect every p (S1 KS/MW per fam x alpha; crux match/differ per region; ablation KS/MW per
  # config). Apply BH at q=0.05; report raw p, BH-adjusted p, reject flag in one table.

  # ---------------------------------------------------------------------------
  # 10. OUTPUT method_out.json  (validate with aii-json; split if >file-size-limit)
  # ---------------------------------------------------------------------------
  method_out = {
    'meta': {models:{primary,other}, ALPHA_GRID, certified_alphas, TAU, B_BOOT, K_SC, SEED,
             n_docs, n_reals, n_true, n_spont, contamination_rate, elicitation, cost_usd:COST,
             logprobs_available, cached_tokens_observed},
    's1_decoy_signature': [{family, alpha, T, n_tail, tail_win_rate, win_rate_ci,
                            ks_stat, ks_p, mw_stat, mw_p, robustness_sweep}],
    'spontaneous_error_match': {regions:[{region, decoy_vs_spont_p, decoy_vs_truepos_p, gap{...},
                            gap_ci, verdict}], figure_cdfs:{x, cdf_truepos, cdf_spont, cdf_decoy}},
    'generator_ne_scorer': {configs:[{G,S, tail_win_rate, win_rate_ci, ks_p, mw_p, small_diagonal}],
                            verdict:'ROBUST'|'SHARED_MODEL_ARTIFACT', validity_region_statement},
    'bh_correction': [{test_name, raw_p, bh_adj_p, reject}],
    'bootstrap': {method:'document-block', B:B_BOOT},
    'cost_trace_path':'logs/cost.jsonl'
  }
  write_json('method_out.json', method_out); aii_json_validate(method_out)
fallback_plan: >-
  LOGPROBS UNAVAILABLE on gpt-4.1-nano route (probe returns null): drop the logprob elicitation and use the PORTABLE self-consistency
  elicitation (K_SC isolated Yes/No+confidence, Z=mean per-call p) as PRIMARY everywhere; it is logprob-free and already the
  ablation default, so nothing else changes. CACHING NOT FIRING (cached_tokens==0): proceed anyway (docs are tiny, ~100 tokens)
  but lower the candidate over-generation / doc count to hold the soft cap. DIFFERENT-FAMILY MODEL PROBLEMS (degenerate/constant
  scores, no Yes/No separation, or >$0.30/M): try the next family in order qwen -> llama -> mistral via aii-openrouter-llms;
  if none gives usable separation, report the ablation on the best-available cross-family pair and state the limitation (do
  not fabricate a clean G!=S result). SPONTANEOUS ERRORS TOO SPARSE (N_spont<40 after enrichment): push harder over-generation
  (force multi-hop inference on every entity pair, raise temperature, draw more long-k confirmatory docs), then pool atomic+multi-hop;
  if still <40, report the crux + S1 as UNDERPOWERED/UNTESTABLE with the measured false-admission base-rate (a precondition
  outcome) instead of asserting a noisy ~0.5. TAIL TOO THIN at knockoff+ T (few |W|>=T pairs): report diagnostics at multiple
  tail quantiles (top50/25/10%) and at the most permissive CERTIFIED alpha; if every region is underpowered, present effect
  sizes (Wasserstein, Cliff's delta) descriptively with CIs and explicitly decline a significance verdict. KS UNDERPOWERED:
  supplement with Anderson-Darling + a permutation two-sample test and always report effect sizes regardless of p. COUNTERFACTUAL
  DECOY CONTAMINATION (accidentally gold-entailed): CLUTRR gold is crisp, so reject deterministically via gold membership
  and regenerate; report contamination_rate and a sensitivity sweep. COST projection > soft cap after the smoke test: reduce
  K_SC (5->3), cap candidates/doc, or shrink the confirmatory subset (keep admissions >= the smallest certified-alpha k-floor);
  the logprob path is cheapest, prefer it. WORST CASE (LLM access flaky): cache every raw response to disk keyed by (model,prompt_hash)
  so re-runs are free and partial results survive; the stats pipeline (sections 5-9) runs offline on cached scores. NEVER
  exceed $10 (assert in log_cost aborts the run).
testing_plan: >-
  STAGE 0 -- OFFLINE STATS UNIT TESTS (no API, no cost): (a) knockoff_plus_T on the spec's worked example must reproduce the
  eq-1.9 threshold and the k-floor mapping {0.05->20,...,0.5->2}; assert it admits nothing when no feasible cutoff exists.
  (b) W() signed-max: assert magnitude==max(Zr,Zd) and sign flips when real/decoy swapped (antisymmetry). (c) SYNTHETIC SCORER
  sanity: generate fake scores where decoy signs are fair coins -> tail win-rate CI must cover 0.5 and KS non-significant;
  where decoys are deliberately 'too easy' (shift decoy scores down) -> win-rate CI below 0.5 and KS significant (confirms
  the diagnostic detects anti-conservatism). (d) doc_block_bootstrap returns wider CIs than naive i.i.d. bootstrap on clustered
  synthetic data. (e) label() unit tests on the 3 mini_data_out.json examples: TRUE for listed atomic/multi-hop triples, FALSE
  for a contradicting relation on an enumerated pair, UNDECIDABLE for an unlisted pair. STAGE 1 -- 1-CALL API PROBES (<$0.01):
  confirm gpt-4.1-nano returns non-null logprobs/top_logprobs; confirm usage.prompt_tokens_details.cached_tokens>0 on a repeated
  document prefix; confirm the chosen OTHER_MODEL returns parseable Yes/No+confidence (and logprobs if claimed). Select elicitation
  per Stage-1 outcome. STAGE 2 -- 3-DOC SMOKE (pilot, mix k=2/k=6/k=10 from mini set; <$0.05): run extraction->decoy->scoring
  end-to-end; eyeball that (i) over-generation yields some spontaneous FALSE reals (especially on k=10), (ii) counterfactual
  decoys are gold-verified non-entailed and surface-matched, (iii) scores vary (not all 0/1), (iv) cost-per-doc extrapolates
  under the soft cap. STAGE 3 -- 40-DOC PILOT (confirmation gate, target <~$0.7): compute S1 + crux. CONFIRMATION SIGNALS
  to see before scaling: counterfactual tail win-rate CI includes 0.5 while random-swap CI sits clearly below 0.5; F_decoy
  tracks F_spont (fail-to-reject) and departs from F_truepos (reject) in the tail; N_spont>=40. If signals are absent, branch
  to the matching fallback (enrich errors / re-tune decoys / widen tail region) BEFORE spending more. STAGE 4 -- SCALE + ABLATION:
  add the bounded confirmatory subset for the headline S1/crux numbers, then run the four-config G!=S ablation on the 40 pilot
  docs with the portable elicitation. Run B>=2000 document-block bootstrap and BH only at the end on the full result set.
  Throughout: log cumulative cost after EVERY call, print a running total each batch, and hard-stop at $10; checkpoint cached
  responses so any interruption resumes for free. Final: aii-json validate method_out.json and aii-file-size-limit check/split.
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
