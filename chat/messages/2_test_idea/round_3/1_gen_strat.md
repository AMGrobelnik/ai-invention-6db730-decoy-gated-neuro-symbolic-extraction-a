# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 3 · `gen_strat`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 08:27:57 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-06-16 08:28:03 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

<available_resources>
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

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

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

<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: >-
  Decoy-Gated Neuro-Symbolic Extraction: A Label-Free FDR Gate Whose Validity Is Elicitation-Dependent -- Consolidate the
  CLUTRR Calibration Diagonal Under the Diagnostic-Validated Self-Consistency Elicitation, Power It to a Tight Certified Grid,
  and Execute the Still-Missing Professional-Document Hallucination-Reduction Headline with Trace-Graphs
hypothesis: |-
  MECHANISM (unchanged, one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  WHAT IS NOW EXECUTED (iteration-2, MEASURED -- the proposal is no longer a proposal). The full pipeline ran end to end on commodity CPU for ~$1.24 of the $10 cap, producing three executed experiments plus a built application anchor: (A) CLUTRR calibration diagonal under VERBALIZED scoring [art_ikjFm_faAe0x] -- realized FDR vs crisp gold, knockoff+ vs plain-threshold vs swap-control baselines, entrapment corroboration, populability far above the N_false_min=40 floor (bridge 710 / atomic 469 / pooled 1179 genuine false candidates), primary disconfirmation NOT_DISCONFIRMED at alpha*=0.3; (B) the elicitation/mechanism + Generator!=Scorer de-circularization study [art_Inu52CyA49Ys] -- 1937 reals (633 true, 1304 spontaneous false), two elicitations (single-token logprob, K=5 self-consistency), a 4-config cross-family ablation; (C) the Re-DocRED operational wedge [art_sHNuY68d4-Wh]; (D) the 24-doc legal/news/regulatory APPLICATION anchor, built and schema-validated but NOT yet run [art_UBTwyePql8NQ]. The job of iteration-3 is NOT to re-build; it is to CONSOLIDATE the calibration story under the elicitation the diagnostic actually validates, POWER it, and FINALLY EXECUTE the application headline.

  THE DECISIVE FINDING (what the evidence now says, honestly). The label-free FDR gate is EXECUTABLE and where it certifies it controls realized FDR, but THREE results sharply narrow the headline claim and reset the next iteration's mandate:
    (1) VALIDITY IS ELICITATION-DEPENDENT. Under single-token logprob the model is overconfident in its OWN spontaneous errors, so counterfactual decoys are too easy and the gate is strongly ANTI-CONSERVATIVE (tail win-rate 0.34, KS p<1e-24; on CLUTRR the method is strictly WORSE than the plain baseline at every alpha, e.g. 0.555 vs 0.228 at alpha=0.3). Under K=5 self-consistency the decoys become EXCHANGEABLE with genuine spontaneous errors in the admission tail (win-rate 0.482, CI [0.42,0.55] covers 0.5, KS p=0.48). This elicitation-dependence is the central mechanism-level contribution and survives a cross-family scorer (S2b ROBUST).
    (2) THE HEADLINE DIAGONAL WAS COMPUTED UNDER THE WRONG ELICITATION. The pre-registered primary diagonal (A) used VERBALIZED scoring, whose counterfactual-decoy tail win-rate is 0.103 on the bridge family (0.167 pilot) -- i.e. by the method's OWN diagnostic this is the anti-conservative 'decoys too easy' regime, NOT the validated exchangeable regime. The reported 'conservative calibration' (realized FDR 0.214 at alpha=0.2/0.3) is therefore not evidence of exchangeability: the gate's OWN FDR estimate is anti-conservative (decoy_fdr_hat=0.125 << realized 0.214 at alpha=0.3), alpha=0.2 is actually VIOLATED (realized 0.214 > 0.200, same 56 admissions as alpha=0.3 due to score discreteness), and the apparent conservatism at alpha>=0.3 is driven by a loose target plus verbalized-score discreteness. The self-consistency regime that the diagnostic DOES validate certifies admissions only at alpha=0.5 on the current 190-doc corpus. The two CLUTRR experiments must be reconciled into ONE internally consistent diagonal under the diagnostic-validated elicitation.
    (3) THE OPERATIONAL VALUE IS REGIME-BOUNDED AND, ON RE-DocRED, NULL. With an already-calibrated logprob scorer, decoy competition does NOT beat a plain confidence threshold at matched recall (Delta(METHOD-PLAIN) in [-0.017,+0.004], never significantly positive, significantly negative at the top of the recall grid) -- the wedge collapses to 'thresholding is enough'. The honest unifying principle: the gate adds value ONLY where the base elicitation is tail-overconfident, and is redundant where it is calibrated.

  THE ONE THING THAT MATTERS NOW (iteration-3 mandate, in priority order).
    P1 -- CONSOLIDATE + POWER THE CALIBRATION DIAGONAL UNDER THE VALIDATED ELICITATION. Re-run the headline CLUTRR realized-FDR-vs-alpha diagonal under the K=5 self-consistency elicitation that the win-rate diagnostic validates (win-rate 0.482), and make THAT the single primary diagonal; keep verbalized only as a documented contrast that quantifies the discreteness/loose-target artifact. Because self-consistency certifies only at alpha=0.5 on 190 docs, SCALE UP the (regenerable) CLUTRR confirmatory set -- more documents and harder long-chain (large-k) splits that densify genuine errors AND raise admission counts -- until the validated elicitation reaches a tighter CERTIFIED grid (alpha with >= 1/alpha admissions), else report the reachable floor honestly. ADD a second-order validity check: the gate's OWN FDR estimate (decoy_fdr_hat) must itself track the realized FDR -- an estimate that undershoots realized (as verbalized did) is a disconfirmation of the gate's self-report even when realized happens to land below alpha.
    P2 -- EXECUTE THE APPLICATION HEADLINE (the goal's hard requirement, still undone). Run the already-built 24-doc legal/news/regulatory hallucination-reduction experiment [art_UBTwyePql8NQ]: hallucinated-fact rate of decoy-gated extraction vs raw LLM generation, under BOTH elicitations and across ALL alpha (so the regime-dependence -- worse-than-baseline under logprob; vacuous below alpha=0.5 under self-consistency -- is explicit, never obscured), with auditable trace-graphs exported on at least a handful of documents (provenance + decoy + entrapment certificate at every leaf). This is the genre-faithful headline the CLUTRR/Re-DocRED proxies cannot carry; budget is trivial (~$1.24 spent of $10).
    P3 -- REFRAME (not re-litigate) THE OPERATIONAL WEDGE. The Re-DocRED disconfirmation stands but is narrow: report the TRUE scope at the point of claim -- n_docs_used=36 (not the 152 confirmatory implied), recall ceiling <=0.086 -- and either (i) scale to enough documents and a higher achievable recall with the multi-hop hallucination comparison powered to enough derived conclusions (it now rests on ~20-24, CIs spanning [0.29,1.0]), and comparators that actually reach the grid (CoT/RAG maxed at recall 0.049/0.041, below the 0.05 grid start, so they produced NO comparable output and must be completed or dropped -- never listed as participating baselines when they are all-null), or (ii) accept 'thresholding-is-enough when the base scorer is calibrated' as the finding and recast the operational contribution as the label-free REGIME-DIAGNOSTIC that tells a practitioner which regime they are in.

  THE GATE (one canonical statistic; unchanged). For each candidate i with real score Z_i and matched-decoy score Z~_i, the competition statistic is the knockoff+ signed maximum W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. The per-pair signed difference d_i = Z_i - Z~_i is used ONLY as a tail diagnostic (win-rate, CDF tests), never as the gating statistic. NEW reporting requirement: alongside realized FDR (vs gold) and target alpha, ALWAYS report the gate's internal estimate decoy_fdr_hat, so 'the estimate is anti-conservative' (decoy_fdr_hat < realized) is surfaced as its own failure mode.

  VALIDITY HONESTY (now empirically grounded, not aspirational). knockoff+ delivers a finite-sample FDR GUARANTEE only under the joint null SIGN-FLIP property; for LLM decoys that property is UNPROVABLE, and the evidence shows it HOLDS or FAILS by elicitation: logprob breaks it (overconfidence in own errors), self-consistency restores it IN THE TAIL. The realized-FDR-vs-alpha diagonal IS its empirical test, but only meaningful under the elicitation whose tail-win-rate diagnostic covers 0.5; a diagonal computed under an elicitation the diagnostic FLAGS (verbalized, win-rate 0.103) cannot be cited as 'conservatively calibrated by exchangeability'. The document-block bootstrap supplies realized-FDP CIs and a dependence DIAGNOSTIC; it does NOT restore the guarantee. The crux SPONTANEOUS-ERROR MATCH must be reported in FULL: under self-consistency the decoy distribution matches genuine spontaneous errors in the admission tail (top-25%/50% KS p=0.33/0.19, fail-to-reject) but the FULL-distribution test is REJECTED (KS p=0.051, MW p=0.036, AD p=0.041, permutation p=0.029; verdict 'decoys_too_easy / anti-conservative'). Iteration-3 reports BOTH, and either re-tunes the decoy family to match the full spontaneous-error distribution OR justifies, on stated decision-theoretic grounds, why the admission tail is the only decision-relevant region (only above-cutoff pairs affect the gate).

  THE DIAGNOSTIC BLIND SPOT (new rigor concern -- materially qualifies the 'self-detecting gate' contribution). The headline contribution was 'tail diagnostics tell the practitioner which regime they are in.' The evidence shows the diagnostic LOSES SENSITIVITY exactly in the valid regime: under K=5 self-consistency the random-swap negative control (which MUST read anti-conservative) instead has win-rate 0.473 with CI covering 0.5 (diagnostic_sensitivity_ok=FALSE) -- the same aggregation that makes the diagnostic trustworthy for the counterfactual decoys destroys its ability to flag a too-easy control. CLAIM S1b: a usable self-detecting gate REQUIRES a diagnostic that retains discriminating power in the valid regime. Iteration-3 must either supply one (e.g. a calibrated-difficulty ENTRAPMENT LADDER injected at known anti-conservative difficulty, or a difficulty-graded synthetic-decoy spike-in whose detectability is measured under the SAME elicitation as the headline) or report the blind spot as a fundamental limitation of the win-rate/swap diagnostic and downgrade the 'tells you when to trust the gate' claim accordingly.

  DE-CIRCULARIZATION (SETTLED this iteration). The Generator!=Scorer ablation is RESOLVED: exchangeability holds for all four (G,S) configs including decoys from gpt-4.1-nano scored by cross-family ministral-8b (and the swap); tail win-rate CIs cover 0.5 (G!=S: 0.496, CI [0.44,0.55], KS p=0.15) and labeled-slice realized FDR is 0.0 at alpha=0.2. Verdict ROBUST: the restored exchangeability is NOT a shared-model artifact. This is no longer an open question; iteration-3 carries it forward as established and does not re-spend budget on it.

  POWER (updated to the validated elicitation). The relevant power target is now under SELF-CONSISTENCY, where the 190-doc corpus certifies admissions only at alpha=0.5. Phase-0 must demonstrate, for the validated elicitation, that the certified grid extends to tighter alpha (>= 1/alpha admissions AND >= N_false_min=40 genuine false admissions among reals) BEFORE the diagonal is asserted there; if not, SCALE UP the regenerable CLUTRR confirmatory set (more documents, harder long-chain large-k splits) until the power target is met or declared unreachable. The CERTIFIED-alpha grid is reported honestly: any alpha whose 1/k admission floor is not reached under the validated elicitation is dropped and reported as a precondition, NEVER as 'confirmed by conservatism'.

  SCOPE / GOAL ALIGNMENT (the application is the headline now). The goal targets ~3000-character professionally written legal/news/regulatory documents, upper-ontology grounding, an LLM probabilistic-reasoning engine at fuzzy unifications, auditable trace-graphs, and a quantified hallucination reduction vs raw LLM. CLUTRR (synthetic ~355-char kinship) and Re-DocRED (Wikipedia prose) remain the CALIBRATION and STATISTICAL-OPERATIONAL anchors -- they buy crisp gold for the diagonal and human gold for the wedge -- but they are PROXIES, and the goal's hard-required application number does NOT yet exist on genre-faithful documents. Iteration-3's P2 closes this gap on the built 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean 2372 chars): (i) ground argument types in a commodity upper-ontology slice (offline WordNet->SUMO standing in for the discontinued OpenCyc, used ONLY for typing), (ii) optionally run the designed ProbLog probabilistic-reasoning step at fuzzy unifications [art_Cr6L9JpoewZi], (iii) report the hallucination-reduction of decoy-gated vs raw LLM extraction across BOTH elicitations and ALL alpha, (iv) export auditable trace-graphs with per-leaf provenance + decoy + entrapment certificates. If P2 cannot be completed, ALL 'application' framing is re-scoped to the genres actually evaluated.

  CLAIM CHAIN (each row independently testable; verdicts reflect iteration-2 evidence and the iteration-3 mandate).
    | # | CLAIM | STATUS | ITERATION-3 ACTION / PASS CRITERION |
    |---|-------|--------|-------------------------------------|
    | S0 | Score separation (precondition) | PASS (tail-AUC 0.86 [0.79,0.91]) | state the explicit elicitation-SELECTION criterion (verbalized was chosen over higher-AUC DINCO 0.871 with no rationale -- justify or switch); confirm separation under the elicitation that hosts the headline diagonal |
    | S1 | Decoy signature + spontaneous-error match | PARTIAL (tail match under self-consistency; FULL-dist REJECTED) | report full + tail; counterfactual decoys ~0.5 tail-win-rate under the validated elicitation; re-tune to match the full spontaneous-error distribution OR justify tail-only on decision-relevance |
    | S1b | Diagnostic sensitivity in the VALID regime (NEW) | FAIL (swap win-rate 0.473, sensitivity_ok=FALSE under self-consistency) | supply a diagnostic that flags too-easy decoys in the valid regime (difficulty-graded entrapment/spike-in) OR report as a fundamental limitation |
    | S2 | Calibration diagonal (CLUTRR) -- under the DIAGNOSTIC-VALIDATED elicitation, powered | CONFOUNDED as run (headline used verbalized=anti-conservative regime; alpha=0.2 violated; decoy_fdr_hat anti-conservative) | re-run the primary diagonal under self-consistency; report decoy_fdr_hat vs realized vs alpha; scale CLUTRR to a tight certified grid; diagonal tracked within tau across the certified grid |
    | S2b | Generator!=Scorer de-circularization | SETTLED ROBUST (4/4 configs cover 0.5) | carry forward as established; no new budget |
    | S3 | Entrapment corroboration (non-circular) | AGREES at alpha* (FDP 0.30 brackets gold 0.214); DIVERGES at alpha=0.5 (FDP 0.420 vs gold 0.248, agree=false) | restrict the agreement claim to alpha*; report the alpha=0.5 divergence honestly |
    | S4 | Operational wedge (Re-DocRED) | DISCONFIRMED but NARROW (n=36, recall<=0.086; CoT/RAG all-null; multi-hop underpowered) | state true n and recall ceiling at the claim; scale + power the multi-hop comparison + complete/drop CoT/RAG, OR accept 'thresholding-is-enough' and reframe as a regime-diagnostic |
    | S4b | Application hallucination reduction (professional docs) -- THE HEADLINE | NOT RUN (anchor built only) | EXECUTE on 24 docs, both elicitations x all alpha, vs raw LLM, with auditable trace-graphs; quantified reduction reported with CI (goal hard requirement) |
    | S5 | Document-level predictive account (Re-DocRED) | leftover-only | out-of-sample predictive IFF >= N_min held-out units; else DESCRIPTIVE |
    | S6 | Predictable propagation (preliminary) | leftover-only | tightening alpha lowers multi-hop hallucinated-conclusion rate (direction + rough magnitude) |

  BUDGET (unchanged ceiling, far underspent). ~$1.24 of the $10 cap spent across iteration-2. Isolated provenance-blinded scoring with document-prefix prompt caching remains the default. Cumulative LLM cost logged after every call; HARD STOP at $10. The budget waterfall ORDER is now: (P1) the powered self-consistency CLUTRR diagonal + decoy_fdr_hat calibration + S1b diagnostic-sensitivity fix; (P2) the application hallucination-reduction headline with trace-graphs; (P3) the reframed/scaled Re-DocRED wedge; then S5/S6/floor-relaxation/rule-gating leftover-only.

  SCOPE OF CLAIMS. The honest central claim is now: a label-free FDR gate at the text-to-logic admission boundary is EXECUTABLE and, in the diagnostic-validated self-consistency regime, controls realized FDR where it certifies; its value over plain thresholding is CONCENTRATED where the base elicitation is tail-overconfident and is NULL where the base scorer is already calibrated; the self-detecting diagnostic has a known blind spot in the valid regime; and the genre-faithful application hallucination-reduction headline remains to be executed. Facts AND bridges carry the claim. CLUTRR (crisp) hosts the powered diagonal + the settled G!=S de-circularization; Re-DocRED hosts the operational comparison; the 24-doc professional slice hosts the application headline. Defeasible bridges, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S5/S6 remain preliminary / if-budget-permits.

  MOTIVATION (unchanged core). Text-to-logic pipelines stall where strict symbolic unification fails and an LLM must fuzzy-match predicates and supply background knowledge; that interface is where PLAUSIBLE, high-confidence false facts re-enter and silently corrupt every downstream deduction, and no existing label-free method offers an FDR knob there (self-consistency/LLM-judge are heuristic; ontology filters catch only encoded violations; conformal factuality/selection/multiple-testing methods all need LABELED calibration and certify the OUTPUT, not the admission boundary). Genomics/proteomics solved the isomorphic label-poor problem with the knockoff filter + target-decoy competition and learned the two failure modes (too-easy decoys -> optimistic FDR, cured by property-matched decoys; entrapment FDP needs a valid independent upper bound). We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary. The iteration-2 evidence refines the value proposition: the knob is real but its operational benefit is regime-bounded, so the deliverable that matters is the regime-aware, application-faithful, auditable hallucination-reduction the goal hard-requires -- which is why iteration-3 leads with executing it.

  KEY ASSUMPTIONS (carried, updated by evidence). (1) The null sign-flip property is ENGINEERED AND TESTED, not guaranteed -- and the evidence shows it is ELICITATION-DEPENDENT (holds under self-consistency in the tail, fails under logprob), so the diagonal is only asserted under the diagnostic-validated elicitation. (2) Score-dependence handled by document-block bootstrap + isolated provenance-blinded scoring (default). (3) The score-separation precondition is pilot-gated (PASSED). (4) The diagonal needs genuine false admissions AND populability is measured first (populability confirmed: pooled 1179 false candidates >> 40). (5) NEW: a usable self-detecting diagnostic must retain sensitivity in the valid regime -- currently UNMET and pre-registered for repair or honest down-scoping. (6) The application headline is executable within budget and is the binding deliverable.

  INVESTIGATION APPROACH. Strict budget waterfall: Phase-0 (confirm separation + populability + decoy_fdr_hat calibration + diagnostic-sensitivity under the validated elicitation) -> P1 powered self-consistency CLUTRR diagonal -> P2 application hallucination-reduction headline with trace-graphs -> P3 reframed/scaled Re-DocRED wedge -> leftover S5/S6. CPU-only; cost logged after every call; HARD STOP at $10. Pipeline unchanged in structure (over-generating extraction -> property-matched counterfactual decoys with non-entailment verification -> isolated provenance-blinded self-consistency scoring -> knockoff+ gate reporting realized FDR AND decoy_fdr_hat -> independent entrapment corroboration -> document-block bootstrap CIs -> SWI-Prolog/ProbLog reasoning with auditable trace-graphs).

  SUCCESS CRITERIA. PRECONDITION (gate): Phase-0 must confirm, UNDER THE ELICITATION THAT HOSTS THE HEADLINE DIAGONAL, that score separation holds, populability >= N_false_min, the certified grid is non-empty, AND the swap-control diagnostic retains sensitivity (or the blind spot is reported). PRIMARY DISCONFIRMATION (single): on the populable CLUTRR family under isolated SELF-CONSISTENCY scoring at the operative alpha, the central control claim is DISCONFIRMED if realized corpus-aggregate FDR exceeds alpha by more than tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side; ADDITIONALLY the gate's self-report is disconfirmed if decoy_fdr_hat is anti-conservative relative to realized. CONFIRMED requires: (1) CALIBRATION VALIDITY -- realized FDR tracks alpha within tau across the certified grid under the validated elicitation, with decoy_fdr_hat itself tracking realized; (2) DECOY SIGNATURE -- counterfactual decoys exchangeable in the tail under the validated elicitation, with the full-distribution result reported and either matched or justified; (3) APPLICATION HEADLINE -- a quantified hallucination reduction vs raw LLM on the 24-doc professional anchor, reported across both elicitations and all alpha, with auditable trace-graphs. The Re-DocRED operational claim is reported as DISCONFIRMED-at-scope (thresholding-is-enough when the base scorer is calibrated) OR re-tested at adequate power; either way it is framed precisely (true n, recall ceiling). A BH multiplicity correction is applied across all validation tests. DISCONFIRMED if: the primary disconfirmation fires under the validated elicitation; an uninterpretable null (underpowered tail/diagonal/gap) is the failure the Phase-0 power analysis is designed to prevent.
motivation: |-
  Text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob there: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and catches only encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, multiple-testing hallucination detection, coherent factuality, and the newest online and differentiable variants) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem -- selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth -- via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound built INDEPENDENTLY of the decoys. We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary, turning 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity with per-leaf certificates.

  The two-anchor design makes the value claim honest. A label-free FDR knob is worth building only if it is BOTH calibrated AND useful where plausible hallucinations actually bite. CLUTRR's closed kinship vocabulary is the right place to prove CALIBRATION (free crisp gold, exact realized FDR) but the wrong place to prove USEFULNESS (the relation set is tiny and well-known). Re-DocRED -- realistic Wikipedia prose, 96 open relation types, document-level multi-hop, human gold with evidence spans -- is the right place to prove operational usefulness, with a fixed shared extraction schema so the neuro-symbolic pipeline, a plain zero-label confidence threshold, CoT, RAG, and labeled conformal are all measured on the same triples at matched recall. The plain confidence threshold is the load-bearing comparator: it shows whether the decoy-competition machinery adds value over naive thresholding at the SAME zero-label budget, so the wedge cannot collapse to 'a threshold was enough.'

  Why it matters even at coarse alpha: NO existing label-free method offers ANY FDR knob at the fuzzy-unification interface. A first, auditable, zero-operation-label control -- even at alpha ~0.1 -- converts an uncontrolled hallucination channel into a tunable one. Because LLM decoys carry no theoretical guarantee, the most probable outcome is partial control; the Re-DocRED document-level predictive account (S5) converts a likely-partial result into a generalizable mechanism-level insight about WHEN the calibration holds.
assumptions:
- >-
  NULL SIGN-FLIP PROPERTY IS ENGINEERED AND TESTED, NOT GUARANTEED. knockoff+/TDC validity requires that, among genuinely-false
  candidates, sign(W_i) for W_i = score(real_i) - score(decoy_i) behaves like an independent fair coin conditional on |W_i|,
  with each false real and its matched decoy equally likely to receive any score in the high-score region near the cutoff.
  LLM counterfactual decoys carry no construction-level proof of this, so the claim is an empirically-validated calibration
  (not a theorem), tested IN THE TAIL via tail-conditioned win-rate ~0.5 plus an upper-tail two-sample CDF test.
- >-
  SCORE-DEPENDENCE IS HANDLED, NOT ASSUMED AWAY. Within-document correlation of LLM scoring noise is respected by treating
  the DOCUMENT as a block (document-block bootstrap for all FDP CIs; never i.i.d.-pooled signs). Batched-scoring contrast
  effects are removed by ISOLATED, provenance-blinded, order-randomized scoring as the default, with a pre-registered isolated-vs-batched
  check that doubles as the DISCRIMINATOR between a scoring artifact (isolation restores the diagonal) and genuine decoy non-exchangeability
  (anti-conservatism persists under isolation).
- >-
  THE SCORE-SEPARATION PRECONDITION IS PILOT-GATED. The LLM must emit a roughly monotone score separating document-entailed
  from non-entailed content better than chance SPECIFICALLY in the upper tail; verbalized confidence is documented to be overconfident
  there, so it is not assumed. A Phase-0 pilot selects the best elicitation (verbalized, logprob-derived, self-consistency,
  DINCO-style distractor-normalized), verifies tail separation, and confirms isolated~batched agreement on a labeled slice.
  The headline budget is released only on pilot success; otherwise the precondition-failure analysis is the reported result.
- >-
  THE CALIBRATION DIAGONAL NEEDS GENUINE FALSE ADMISSIONS, AND POPULABILITY IS MEASURED BEFORE IT IS ASSERTED. A realized-FDR-vs-alpha
  diagonal can only TRACK alpha if a meaningful fraction of admitted reals are genuinely false; on CLUTRR's easy closed vocabulary
  atomic facts may be too clean. Phase-0 measures, at the operative alpha*, the genuine false-admission count among CLUTRR
  proposals separately for atomic facts and multi-hop inferred kinship; the primary disconfirmation is pre-registered on whichever
  family reaches N_false_min (default 40 pooled; default expectation: multi-hop). The false-real pool is enriched by extractor
  over-generation and harder long-chain CLUTRR splits. Below N_false_min on all families, the diagonal is declared UNTESTABLE
  (not 'conservative, therefore confirmed'). CLUTRR gold is exact so the diagonal is asserted there; Re-DocRED gold has residual
  false negatives so only RELATIVE operational comparisons under shared gold are asserted there.
- >-
  S5 IS POWERED WHERE FEATURE VARIANCE EXISTS, WITH A PRE-REGISTERED PREDICTIVE-VS-DESCRIPTIVE THRESHOLD. The per-document
  tail-exchangeability gap can only be predicted if its input features vary; CLUTRR documents are near-homogeneous in entity
  density, specificity, and genre, so S5 is based on Re-DocRED (>=4 entity-type/topic clusters supply real cross-document
  variance). The S5 unit is the document nested in clusters, validated by leave-one-cluster-out and leave-one-document-out
  CV with a pre-registered GAP-regression power analysis; below a pre-registered minimum N_min of held-out units with sufficient
  admissions, S5 is reported DESCRIPTIVE, not predictive.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then execute a strict BUDGET WATERFALL: Phase-0 pilot -> CLUTRR calibration diagonal -> Re-DocRED operational wedge -> (leftover only, gated on the two anchors clearing power thresholds) S5 / S6 / floor-relaxation / rule-gating. CPU-only; cumulative LLM cost logged after every call; HARD STOP at $10.

  FEASIBILITY (published before committing; see the budget arithmetic in the hypothesis). Isolated, provenance-blinded scoring is the default for 100% of the ~14.4K confirmatory scoring items; the ~7-15M projected tokens are kept to ~$1-3 by document-prefix prompt caching (the ~60 scoring calls per document re-use one cached document context at ~0.1x read cost). A sub-$0.30/M model is used; batching appears only in the labeled isolated-vs-batched sensitivity slice.

  PHASE 0 -- PILOT (precondition + powerability). On a few dozen labeled items per anchor: (i) select the elicitation that best separates entailed vs non-entailed IN THE UPPER TAIL; (ii) confirm isolated~batched agreement on a labeled slice (gate batching); (iii) MEASURE the genuine false-admission count among CLUTRR atomic-fact and multi-hop-bridge proposals at alpha* and choose the populable family for the primary disconfirmation (enrich via over-generation + long-chain splits if sparse); (iv) MEASURE on CLUTRR the cross-document variance of the S5 features (demonstrating CLUTRR's unsuitability for S5); (v) run a tail power analysis AND a GAP-regression power analysis for S5 on Re-DocRED. Size both corpora to target; gate the full run.

  PIPELINE. (1) EXTRACTION: a cheap OpenRouter LLM proposes typed first-order facts; argument types grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing; the extractor OVER-GENERATES on CLUTRR to densify false positives. (2) DECOY GENERATION: PRIMARY family = document-conditioned counterfactual decoys (maximally-plausible, non-entailed facts/bridges); random type-matched swaps retained as the predicted-anti-conservative baseline; every decoy passes a non-entailment check with reported contamination. (3) ENTRAPMENT: independent, tail-matched, false-by-construction (in-genre cross-document swaps, numeric/temporal perturbation, explicit contradiction), mixed at reported ratio r, with its own tail-difficulty diagnostic. (4) SCORING: isolated, provenance-blinded, order-randomized, pilot-selected elicitation; rank-normalized per document. (5) FDR GATE: knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges and per anchor; admitted items enter the KB with a logged certificate. (6) VARIANCE/CIs: document-block bootstrap throughout. (7) ENTRAPMENT VALIDATION: combined estimator upper-bounds realized false-admission; compare against decoy-FDR and gold. (8) TAIL DIAGNOSTICS (measurement only): above-cutoff distribution vs gold false-reals + win-rate + upper-tail two-sample test. (9) REASONING: admitted facts/bridges populate SWI-Prolog for multi-hop deduction; backward-chaining proofs export as trace-graphs whose leaves carry provenance plus the decoy + entrapment certificate.

  SHARED OPERATIONAL EVALUATION (Re-DocRED). A single fixed claim-decomposition + relation-alignment step maps every system's output to (head, Re-DocRED-relation, tail) triples identically -- neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal. Recall is matched by sweeping each system's own score to a common operating point; precision and hallucinated-conclusion rate are compared there with document-block-bootstrap CIs.

  EXPERIMENTS. (a) CLUTRR validity-of-control: sweep alpha; realized FDR via gold + entrapment bound on the populable family; diagonal tracking with block-bootstrap CIs; normalization and isolated-vs-batched sensitivity. (b) Decoy-family showdown + entrapment tail-difficulty. (c) Re-DocRED operational: matched-recall PR + hallucinated-conclusion rate vs PLAIN THRESHOLD (primary zero-label comparator), CoT, RAG, and labeled conformal, with guarantee status side by side. (d) [leftover only] S5 LOO-CV on Re-DocRED with the predictive-vs-descriptive threshold; S6 propagation; floor-relaxation; rule gating. (e) Cost check (<$10, CPU-only) + auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). Phase-0 must show the selected score separates entailed from non-entailed content better than chance in the upper tail, isolated~batched agree, a CLUTRR family reaches N_false_min genuine false admissions, and the S5 power/variance measurements support a gap regression on Re-DocRED. If the pilot fails any gate, the reported contribution is the precondition-failure analysis.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent). On the populable CLUTRR family (default: multi-hop inferred kinship) under isolated provenance-blinded scoring at alpha*: the central label-free control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. If no family reaches N_false_min even after enrichment, the diagonal is reported UNTESTABLE (a precondition outcome), never as confirmed-by-conservatism.

  CONFIRMED requires ALL of: (1) CALIBRATION VALIDITY (CLUTRR) -- realized FDR tracks target alpha within tau above the 1/k floor across the demonstrable grid on the populable family, stable under the normalization and isolated-vs-batched checks; (2) DECOY SIGNATURE -- counterfactual decoys reach tail-conditioned win-rate ~0.5 and pass the upper-tail two-sample test while random swaps are measurably anti-conservative, and entrapment passes its tail-difficulty diagnostic with the combined-estimator bound agreeing with gold; (3) OPERATIONAL WEDGE (Re-DocRED) -- at matched recall (PR curves with block-bootstrap CIs), decoy-gating BEATS the plain confidence-threshold gate on atomic-fact precision and hallucinated-conclusion rate under identical zero labels, and stays competitive with the labeled Mohri-Hashimoto conformal reference. A BH multiplicity correction is applied across all validation tests.

  SECONDARY (reported only after the two anchors clear power thresholds; never escape hatches). (4) S5 document-level model: PREDICTIVE if validated out-of-sample across >= N_min held-out Re-DocRED units, else DESCRIPTIVE; either way it characterizes WHICH features govern tail-exchangeability. (5) Entrapment self-corroboration agrees with gold (co-failures reported). (6) S6 -- tightening alpha reduces multi-hop hallucination in the predicted direction. (7) Ablating the decoy gate measurably worsens hallucination. (8) The pipeline runs on commodity CPU within $10 with auditable trace-graphs carrying per-leaf certificates.

  DISCONFIRMED if: the primary disconfirmation fires (populable CLUTRR family anti-conservative beyond tau under isolated scoring); OR, separately for the operational claim, decoy-gating shows no precision/hallucination advantage over the PLAIN CONFIDENCE-THRESHOLD gate at matched recall on Re-DocRED (the wedge collapses to 'thresholding is enough'). An uninterpretable null -- control neither clearly holds nor clearly fails because the tail, the diagonal, or the gap test is underpowered -- is the true failure the Phase-0 power analysis (now including the false-admission base-rate measurement) is designed to prevent.
related_works:
- >-
  Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis
  using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench): gives the theory of entrapment FDP estimation, shows the
  naive 'sample' estimator is flawed, and provides the valid combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E). We adopt
  this estimator, report r, propagate r into variance and the alpha-floor, and ADD a tail-difficulty diagnostic for entrapment.
  Difference: their domain is peptide identification; we transplant the estimator and construction-independence to LLM fact/bridge
  admission.
- >-
  Barber & Candes, knockoff filter (Annals of Statistics 2015) and Candes et al., Model-X knockoffs (2018), plus target-decoy
  competition in proteomics: select true signals among many candidates with guaranteed FDR by competing each real against
  a synthetic negative control exchangeable BY CONSTRUCTION, relying on the null sign-flip property (signs of null statistics
  are i.i.d. coin flips conditional on magnitude). Difference: this machinery lives in numeric feature selection and mass
  spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM neuro-symbolic boundary where
  decoys carry NO such guarantee, so we test the sign-flip condition empirically in the tail, use a document-block bootstrap
  for within-document sign dependence, and model where it holds.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, Bioinformatics 2021; protein-language-model decoys):
  generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference:
  lives in molecular screening; we import the PRINCIPLE -- decoys must reproduce the false-positive score distribution, not
  be 'too easy' -- to design LLM fact/bridge decoys as document-conditioned counterfactuals.
- >-
  Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction' (EMNLP 2022; Re-DocRED).
  DocRED comprises 5,053 Wikipedia documents (distant-supervised from Wikidata), averaging 196.7 words and 19.5 entities,
  with 97 predefined relation types (96 real + no_relation) and human evidence sentences; Re-DocRED re-annotates 4,053 by
  adding missed triples (~13 F1 of headroom) and is public. We USE Re-DocRED as the open-vocabulary operational anchor (a
  fixed shared (head, relation, tail) extraction schema for ALL systems), asserting only RELATIVE operational comparisons
  (shared residual false negatives affect all methods equally), not the absolute FDR diagonal, which we assert on crisp-gold
  CLUTRR. Re-DocRED documents are SHORT (~200 words), which is strictly easier for commodity hardware; we treat document length
  itself as an S5 feature.
- >-
  Li, Magesh & Veeravalli, 'Principled Detection of Hallucinations in Large Language Models via Multiple Testing' (arXiv 2508.18473,
  2025): reconceptualizes hallucination detection as hypothesis testing, aggregates gray-box scores via conformal p-values,
  and applies general (dependence-tolerant) Benjamini-Hochberg/Yekutieli to control the false-alarm rate; it 'adds a lightweight
  calibration step that uses a small calibration set of non-hallucinated prompts to provide theoretical control', operating
  at the PROMPT/generation level. Difference: it is LABELED and certifies the generation; we are label-free for operation
  and gate the neuro-symbolic ADMISSION boundary via target-decoy competition with independent entrapment corroboration and
  per-leaf certificates. Its confirmed labeled-calibration requirement strengthens our label-free wedge.
- >-
  Lu, Huo, Ren, Wang & Zou, 'Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection' (arXiv 2509.03297,
  2025): GAIF, a feedback-enhanced generalized alpha-investing framework that dynamically adjusts thresholds using revealed
  outcomes for finite-sample (m)FDR control, extended to online conformal selection via independent conformal p-values and
  feedback-driven model selection. Difference: it REQUIRES revealed labeled outcomes (feedback) and selects/certifies candidate
  outputs online; we control FDR with ZERO operation labels via decoy competition at the text-to-logic admission boundary,
  with symbolic propagation. The conformal-selection line reinforces -- not threatens -- the label-free wedge.
- >-
  Hittesdorf, Salzetta & Cheng, 'Differentiable Conformal Training for LLM Reasoning Factuality' (Differentiable Coherent
  Factuality / DCF, arXiv 2604.20098, 2026), building on 'Conformal Language Model Reasoning with Coherent Factuality' (arXiv
  2505.17126, ICLR 2025): represent reasoning outputs as dependency graphs and jointly validate claims with their logical
  ancestors; DCF makes the scorer differentiable to learn better scorers while recovering conformal guarantees. Difference:
  both require LABELED held-out calibration and certify OUTPUT claim graphs; we gate the neuro-symbolic ADMISSION boundary
  label-free via decoy competition, and our trace-graph is a Prolog proof with per-leaf decoy+entrapment certificates, not
  a conformally-validated claim DAG.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm removing claims
  until a factuality alpha is met via conformal prediction with labeled samples. Our load-bearing LABELED reference baseline
  in S4. Difference: it requires labeled calibration, certifies the final filtered OUTPUT rather than the admission boundary,
  and offers no synthetic-decoy mechanism, independent entrapment, or symbolic propagation. We report its finite-sample guarantee
  vs our empirical calibration side by side; our wedge is label-free OPERATION measured against a plain zero-label threshold.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no operation labels by competing each proposal against engineered
  decoys and corroborate via independent tail-matched entrapment.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023; TDC-SB/UB)
  and He, Ebadi, Keich et al., 'Controlling the FDR via competition: is the +1 needed?' (arXiv 2204.13248, 2023): tighter
  FDP bounds and analysis of the '+1' correction that sets the minimum-estimable-FDR floor. We test (leftover budget only)
  whether these lower our achievable-alpha floor without breaking validity. Difference: developed for generic competition-based
  selection; we apply them at the text-to-logic interface.
- >-
  LINC (Olausson et al., EMNLP 2023) and Logic-LM (Pan et al., Findings of EMNLP 2023): LLM semantic-parse premises into FOL/symbolic
  form executed by a solver, with majority voting or solver-error self-refinement. Difference: no principled control over
  WHICH extracted content is admitted -- a syntactically valid fabricated premise is never challenged; voting smooths variance
  and refinement fixes solver/syntax errors only. No FDR knob, no decoys, no label-free precision guarantee.
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING and controls overall false-admission rate including where the
  ontology is silent -- complementary.
- >-
  FactSelfCheck (Sawczyn et al., Findings of EACL 2026 / arXiv 2503.17229) and DINCO (Wang et al., arXiv 2509.25532, 2025):
  zero-resource black-box methods producing per-fact hallucination scores from sampling consistency / distractor-normalized
  verbalized confidence. Difference: both yield a per-claim detection SCORE with no admission threshold, exchangeability,
  or competition argument; FactSelfCheck-style and DINCO-style signals are CANDIDATE elicitations in our Phase-0 pilot, while
  our novelty is the label-free FDR gate built on whichever elicitation wins.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer. Genomics/proteomics solved the hardest label-poor problem -- deciding
  which of thousands of candidate signals are real with no ground truth -- with a guaranteed FDR via the knockoff filter (statistics)
  and target-decoy competition (mass spectrometry), and discovered the two ways the trick breaks: decoys 'too unrealistic
  to fool' the scorer make FDR optimistic (cured by property-matched decoys: DeepCoy, protein-LM decoys), and entrapment FDP
  must be estimated with a valid upper bound (Wen et al., Nature Methods 2025) using entrapment built unlike the decoys. We
  map all three onto the fuzzy-unification boundary of a text-to-logic pipeline, where the LLM aligns predicates and supplies
  background knowledge. Because the dangerous hallucinations are PLAUSIBLE high-confidence false facts, the decoys must be
  plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE TAIL, and the FDR must be corroborated
  by independently-constructed tail-matched entrapment and arbitrated by a small gold probe. Three further moves come from
  taking the statistical machinery seriously on its own terms: (a) the knockoff null SIGN-FLIP property is named explicitly,
  and the two ways LLM scoring can break it -- within-document score correlation and batched-scoring contrast effects -- are
  handled by a document-block bootstrap and isolated provenance-blinded scoring, with the isolated-vs-batched check doubling
  as the discriminator between a scoring artifact and genuine non-exchangeability; (b) evaluation is split into a CALIBRATION
  anchor (CLUTRR, crisp free gold, exact diagonal -- with the disconfirmation pre-registered on the candidate family dense
  enough in genuine errors to be non-vacuous) and an OPERATIONAL anchor (Re-DocRED, open-vocabulary human gold, a fixed shared
  extraction schema for all systems, with a plain zero-label confidence threshold as the primary comparator so the wedge isolates
  the decoy machinery's value); (c) the document-level predictive account is based on Re-DocRED where the predicted features
  actually vary, with a pre-registered predictive-vs-descriptive threshold.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content -- a document-conditioned counterfactual -- so its score distribution reproduces that of genuine plausible hallucinations.
    It replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Null sign-flip property (the validity condition)
  definition: >-
    The condition knockoff+/TDC FDR control rests on: among genuinely-false candidates, the sign of W_i = score(real_i) -
    score(decoy_i) behaves like an independent fair coin conditional on |W_i|. Two LLM-scoring channels can break it anti-conservatively
    -- within-document score correlation and batched-scoring contrast effects -- so the method tests and protects against
    both.
- term: Two-anchor evaluation (calibration vs operational)
  definition: >-
    CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim (the realized-FDR-vs-alpha diagonal) and
    the single primary disconfirmation; Re-DocRED (human-annotated, open-vocabulary, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS
    claim, the genuine schema-alignment bridge test, and the S5 predictive model. CLUTRR proves the knob is calibrated; Re-DocRED
    proves it is useful; the two are never conflated.
- term: Populability gate and false-real enrichment
  definition: >-
    A realized-FDR diagonal can only TRACK alpha if enough admitted reals are genuinely false. Phase-0 measures, at alpha*,
    the genuine false-admission count among CLUTRR atomic-fact and multi-hop-bridge proposals; the primary disconfirmation
    is pre-registered on whichever family reaches N_false_min (default 40 pooled). The false-real pool is enriched by extractor
    over-generation and harder long-chain splits. Below N_false_min on all families, the diagonal is declared UNTESTABLE,
    not confirmed-by-conservatism.
- term: Plain confidence-threshold baseline (the operational comparator)
  definition: >-
    A zero-label gate that admits candidates whose raw elicited confidence exceeds a swept threshold, with no decoy, no competition,
    no entrapment. It is the PRIMARY zero-label comparator in S4: if decoy-gating does not beat it at matched recall on precision
    and hallucinated-conclusion rate under identical labels, the operational wedge is disconfirmed (it reduces to 'thresholding
    is enough').
- term: Shared operational construct (Re-DocRED)
  definition: >-
    All systems target the SAME (head-entity, Re-DocRED-relation, tail-entity) triples over annotated entities, scored against
    human gold. A single fixed claim-decomposition + relation-alignment step maps every system's raw output -- neuro-symbolic,
    plain threshold, CoT, RAG, labeled conformal -- into this triple space identically, and recall is matched by sweeping
    each system's own score to a common operating point, so the comparison is apples-to-apples.
- term: Isolated provenance-blinded scoring
  definition: >-
    Each candidate (real, decoy, or entrapment) is scored in its OWN prompt with source/identity masked and presentation order
    randomized, instead of scoring many candidates jointly. This removes within-batch contrast/ranking effects that would
    let the model implicitly detect fabricated items and depress decoy scores. It is the default for 100% of the confirmatory
    set; document-prefix prompt caching keeps it affordable. The pre-registered isolated-vs-batched check discriminates a
    scoring artifact (isolation restores the diagonal) from genuine non-exchangeability (anti-conservatism persists).
- term: Document-prefix prompt caching
  definition: >-
    Because all ~60 isolated scoring calls for one document re-send the same document context, that prefix is cached once
    and re-read at ~0.1x cost per call. This is the mechanism that makes default isolated scoring fit the $10 budget (~$1-3
    projected) without reverting to batching, preserving the isolated-vs-batched discriminator.
- term: Document-block bootstrap
  definition: >-
    All FDP/FDR confidence intervals are computed by resampling whole DOCUMENTS (blocks), not individual candidates, so within-document
    correlation of LLM scoring noise is respected. This replaces the i.i.d.-pooled-sign variance the knockoff '+1' floor argument
    would otherwise assume, and yields the CI used in the primary disconfirmation.
- term: Tail-conditioned win-rate (tail diagnostic)
  definition: >-
    The win-rate of a decoy (or entrapment item) over a known-false real, computed ONLY among matched pairs scoring above
    the operative admission cutoff, reported with score CDFs and an upper-tail two-sample test. Target ~0.5 in the tail. Measurement
    only, never used by the gate; it supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative
    exactly where admissions occur.
- term: Combined / paired entrapment estimator and the ratio r
  definition: >-
    The valid entrapment upper bound on false-admission: FDP_hat = N_E(1+1/r)/(N_T+N_E), where N_T = admitted reals, N_E =
    admitted entrapment, r = entrapment-to-target ratio (reported; r=1 gives the tighter paired form). It replaces the flawed
    naive 'sample' ratio; r is propagated into variance and the achievable-alpha floor. Entrapment is built by a mechanism
    distinct from the decoys and gets its own tail-difficulty diagnostic.
- term: Single primary disconfirmation
  definition: >-
    One pre-registered, S4/S5-independent result that can falsify the headline: on the populable CLUTRR family under isolated
    provenance-blinded scoring at alpha*, if realized corpus-aggregate FDR exceeds alpha* by more than tolerance tau AND the
    document-block-bootstrap CI lies entirely on the anti-conservative side, the central label-free control claim is disconfirmed
    -- regardless of entrapment agreement or S5 outcome.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  Every LLM-proposed fact and fuzzy-unification bridge must out-score a plausibility-matched counterfactual decoy in a target-decoy
  / knockoff+ competition before entering a Prolog knowledge base, giving a label-free FDR knob at the neuro-symbolic admission
  boundary; calibration validity is proven on crisp-gold CLUTRR (with the single disconfirmation pre-registered on the error-dense,
  populable candidate family), operational hallucination-reduction is proven on open-vocabulary Re-DocRED against a plain
  zero-label confidence threshold and neural baselines on a shared extraction schema at matched recall, the gate is robustified
  against the two ways LLM scoring breaks the null sign-flip property (document-block bootstrap and isolated provenance-blinded
  scoring kept affordable by document-prefix caching), and a strict budget waterfall powers the two anchors before any secondary
  analysis.
_relation_rationale: >-
  Same gate/two-anchor frame; re-pointed to the validated self-consistency diagonal and the application headline.
_confidence_delta: decreased
_key_changes:
- >-
  RE-POINTED THE HEADLINE DIAGONAL (review methodology-major): the pre-registered CLUTRR primary diagonal was computed under
  VERBALIZED scoring, whose decoy tail win-rate (0.103 bridge) the method's OWN diagnostic flags as anti-conservative; mandated
  re-running it under the K=5 SELF-CONSISTENCY elicitation the diagnostic actually validates (win-rate 0.482) and reconciling
  the two CLUTRR experiments into one internally consistent diagonal, keeping verbalized only as a documented discreteness/loose-target
  contrast.
- >-
  ADDED A SELF-REPORT VALIDITY CHECK (review methodology/rigor): the gate must report its OWN estimate decoy_fdr_hat against
  realized FDR; on the verbalized diagonal decoy_fdr_hat=0.125 undershot realized 0.214 and alpha=0.2 was VIOLATED (0.214>0.200)
  -- the apparent conservatism was a discreteness artifact, not exchangeability, and is now flagged as its own failure mode.
- >-
  NEW CLAIM S1b -- DIAGNOSTIC BLIND SPOT (review evidence-major): under the valid self-consistency regime the swap control
  loses sensitivity (win-rate 0.473, CI covers 0.5, diagnostic_sensitivity_ok=FALSE), so the 'self-detecting gate' contribution
  is materially qualified; iteration-3 must supply a difficulty-graded diagnostic that works in the valid regime or report
  the limitation.
- >-
  CRUX MATCH REPORTED IN FULL (review evidence-major): mandated reporting the REJECTED full-distribution spontaneous-error
  test (KS p=0.051, MW 0.036, AD 0.041, perm 0.029, verdict decoys_too_easy) alongside the tail fail-to-reject, with explicit
  decision-relevance justification for the tail or a decoy re-tune.
- >-
  APPLICATION HEADLINE PROMOTED TO PRIORITY P2 (review scope-major): the built 24-doc legal/news/regulatory hallucination-reduction
  run is still UNEXECUTED; mandated executing it vs raw LLM across BOTH elicitations and ALL alpha with auditable trace-graphs,
  since all current numbers live on CLUTRR/Re-DocRED proxies.
- >-
  RE-DocRED WEDGE REFRAMED PRECISELY (review evidence-major): disconfirmation stands but is narrow -- true n_docs=36 (not
  152) and recall<=0.086; CoT/RAG never reached the grid (all-null) and must be completed or dropped; multi-hop comparison
  (~20-24 conclusions, CIs [0.29,1.0]) must be powered or labeled underpowered; operational value recast as a regime-diagnostic.
- >-
  DE-CIRCULARIZATION MARKED SETTLED: the Generator!=Scorer ablation is ROBUST across 4 configs incl. cross-family ministral-8b;
  carried forward as established, no new budget.
- >-
  ENTRAPMENT AGREEMENT RESTRICTED to alpha* (FDP 0.30 brackets gold 0.214); the alpha=0.5 divergence (FDP 0.420 vs gold 0.248,
  agree=false) now reported honestly.
- >-
  MINOR FIXES (review rigor/clarity): require an explicit elicitation-selection rationale (verbalized was chosen over higher-AUC
  DINCO 0.871) and full figure captions marking the 1/k floor, bootstrap CIs, and gate-vs-plain-vs-swap distinction.
- >-
  CONFIDENCE DECREASED: the headline calibration was confounded by score discreteness + a loose target, the self-detecting
  diagnostic has a blind spot in the valid regime, the operational wedge is disconfirmed, and the goal's application headline
  is still unrun -- the core idea survives but its demonstrated operational value is narrower than projected.
relation_type: evolution
</hypothesis>

<iteration_status>
Current iteration: 3 of 10
Remaining (including this one): 8
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: >-
  Execute the Realized Numbers: CLUTRR Diagonal, Re-DocRED Wedge, and the Generator!=Scorer De-Circularization for the Label-Free
  Decoy-Competition FDR Gate
objective: >-
  Convert iteration-1's prepared-and-validated infrastructure into the three realized empirical numbers the prior paper lacked
  (the single decisive 3/10 blocker): (1) the CLUTRR calibration diagonal -- does realized corpus-aggregate FDR track target
  alpha on the populable multi-hop family, with a demonstrated pre-run power analysis and document-block-bootstrap CIs; (2)
  the Re-DocRED operational wedge -- does decoy-gating beat a plain confidence threshold (and CoT/RAG/labeled-conformal) at
  matched recall on atomic-fact precision and hallucinated-conclusion rate; and (3) a prominently-reported decoy-mechanism
  validation with a generator!=scorer de-circularization ablation and a decoy-vs-spontaneous-error tail-CDF match that directly
  tests the reviewer's deepest methodological objection. In parallel we build the genre-faithful professional-document application
  anchor (legal/news/regulatory ~3000-char docs with gold) and a novelty/upper-ontology/probabilistic-reasoning specification,
  so the scope-mismatch MAJOR is closed structurally this iteration and quantitatively next. The novel contribution realized
  here is the FIRST empirical demonstration of label-free knockoff+/target-decoy FDR control at the LLM text-to-logic admission
  boundary, with its validity region honestly mapped.
rationale: >-
  The reviewer feedback is unambiguous: the dominant score blocker is that NO central claim was measured (S2 diagonal, S4
  wedge, S3 entrapment, S6 hallucination-reduction all unrun), and ACL/EMNLP/NeSy do not run a registered-report track. Iteration
  1 already delivered exactly what makes execution possible NOW: two schema-validated anchors (crisp-gold CLUTRR art_XZyKy6QuwxrO;
  human-gold Re-DocRED art_Jcudmkugg1qT) and two implementation-ready specs (the FDR-gate+elicitation spec art_SLUbUUr6Ul98
  with the recommended sub-$0.30/M model, knockoff+/entrapment/bootstrap formulas, and the canonical statistic; the pipeline+operational-comparison
  spec art_K6AE23HoGqe6 with prompt templates, the shared relation-alignment step, and baseline recipes). Because experiments
  require an existing DATASET dependency and the anchors exist, the highest-leverage move is three focused, parallel, self-contained
  EXPERIMENTS that each run their own pilot internally and report numbers -- directly killing the empirical-results MAJOR.
  The de-circularization experiment is split out and elevated to a first-class result because it answers the methodology MAJOR
  (same LLM generates and scores; the right matching target is the SPONTANEOUS false-real distribution, not the true-positive
  distribution; shared-model bias can break exchangeability either direction). The power MAJOR is answered by a concrete pre-run
  power calculation folded into the diagonal experiment (which alpha values clear the 1/k floor at what CI half-width, with
  mandatory enrichment/pooling if marginal). The scope MAJOR is answered by building the professional-doc anchor now (the
  application experiment runs next iteration on it) plus a research spec that justifies the OpenCyc and probabilistic-reasoning
  substitutions and supplies the novelty comparison table (novelty MINOR). All five artifacts run in parallel and share the
  $10 cap, so each experiment carries an explicit conservative soft cap and logs cumulative cost after every call; the spec's
  ~$1-3 projection for both confirmatory anchors leaves comfortable margin.
artifact_directions:
- id: experiment_iter2_dir1
  type: experiment
  objective: >-
    Produce the HEADLINE calibration diagonal (realized FDR vs target alpha) and execute the single pre-registered primary
    disconfirmation on crisp-gold CLUTRR, accompanied by an explicit pre-run statistical power analysis (answering the power
    MAJOR) and independent entrapment corroboration (S0 + S2 + S3 + power).
  approach: >-
    Implement the end-to-end gate exactly per the two specs [art_SLUbUUr6Ul98, art_K6AE23HoGqe6]. STAGE A (Phase-0 pilot,
    on the 40-example disjoint pilot slice): (i) select the label-free elicitation by tail-AUC with a bootstrap CI among the
    spec's shortlist -- verbalized confidence (floor), DINCO-style distractor-normalized, self-consistency/SelfCheckGPT, and
    a logprob yes/no-token score IF the model exposes non-null logprobs -- requiring tail-AUC>0.5 in the upper (admission)
    tail; confirm isolated~batched agreement on the labeled slice. (ii) Measure POPULABILITY: the count of GENUINE false admissions
    (vs crisp CLUTRR gold) among atomic-fact vs multi-hop-inferred-kinship proposals at the operative alpha*; pre-register
    the disconfirmation on whichever family reaches N_false_min=40 pooled (default expectation: multi-hop), enriching the
    false-real pool via extractor over-generation (T=0.7, n=3 samples unioned, cap 20 candidates/doc) and the dataset's harder
    long-chain k>=4 splits; if still marginal, POOL the atomic+multi-hop families to lift the admission count above the floor
    for tighter alpha (per the reviewer's suggestion), reporting the pooled-vs-separate sensitivity. (iii) Compute and REPORT
    the pre-run power calculation: given the measured false-admission rate, the within-document intra-class correlation, and
    B>=2000 document-block (cluster) bootstrap resamples, state which alpha in {0.05,0.10,0.20,0.30,0.50} clear the 1/k admission
    floor {20,10,5,4,2} and at what CI half-width; scale the regenerable CLUTRR confirmatory set (re-run data.py with more
    docs / harder splits) until the power target is met or declared unreachable. STAGE B (confirmatory diagonal): extraction
    over-generation -> document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination
    rate, sweep the rejection threshold) -> ISOLATED provenance-blinded order-randomized scoring with document-prefix prompt
    caching -> knockoff+ gate using the CANONICAL competition statistic W_i = (Z_i v Z~_i)*sign(Z_i - Z~_i) (signed magnitude-max;
    the per-pair difference d_i = Z_i - Z~_i is reserved as a TAIL DIAGNOSTIC ONLY, never the gating statistic -- fixing the
    iteration-1 inconsistency) with admission threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for facts
    and bridges; sweep alpha and compute realized corpus-aggregate FDR vs crisp gold with document-block-bootstrap percentile
    CIs -- this IS the diagonal. Keep random type-matched swaps as the predicted-anti-conservative negative control. STAGE
    C (entrapment): build deterministically-constructed tail-matched entrapment WITHOUT the generating LLM (in-genre cross-document
    kinship swaps, numeric/temporal perturbation, explicit contradiction) at ratio r=1, compute the valid combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E),
    and check agreement with the decoy-FDR and gold; attach a per-entrapment tail-difficulty diagnostic. Report the CERTIFIED-alpha
    grid honestly (drop any alpha whose 1/k floor is unreached, labeling it a precondition, NEVER 'confirmed by conservatism');
    evaluate the primary disconfirmation at alpha* with tolerance tau=0.05. Cleanly SEPARATE the two roles of the bootstrap
    (it quantifies FDP/FDR sampling variability) from validity-under-dependence (an empirical property established by the
    tail diagnostics + isolated-vs-batched discriminator), per the rigor MINOR. Use the spec's recommended openai/gpt-4.1-nano
    (logprobs+auto-caching, <$0.30/M); gradual scaling mini->full per aii-long-running-tasks; log cumulative LLM cost after
    EVERY call; soft cap ~$3 for this experiment, HARD STOP at $10. Output method_out.json with: the alpha-vs-realized-FDR
    diagonal arrays (figure-ready, with 1/k floor and CI bands marked), the power-analysis table, entrapment numbers, populability
    counts per family, and the disconfirmation verdict.
  depends_on:
  - id: art_XZyKy6QuwxrO
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_SLUbUUr6Ul98
    label: methodology
    relation_type:
    relation_rationale:
  - id: art_K6AE23HoGqe6
    label: pipeline
    relation_type:
    relation_rationale:
- id: experiment_iter2_dir2
  type: experiment
  objective: >-
    Elevate the S1 tail-exchangeability check and the generator!=scorer de-circularization to first-class, prominently-reported
    empirical results that directly test the reviewer's deepest methodological objection: whether the gate's calibration is
    an artifact of a SINGLE LLM both generating decoys and scoring, and whether the decoys reproduce the SPONTANEOUS false-real
    score distribution (the right matching target) rather than the true-positive distribution.
  approach: >-
    Operate on a labeled CLUTRR slice (the 40-example pilot plus a bounded confirmatory subset, to cap cost) using crisp gold
    to define known-false reals. (1) DECOY SIGNATURE (S1): construct matched (false-real, counterfactual-decoy) pairs; report
    the tail-conditioned win-rate among pairs scoring ABOVE the operative admission cutoff (target ~0.5), and a one-sided
    upper-tail two-sample CDF test (KS and tail-restricted Mann-Whitney) on real-false vs counterfactual-decoy scores restricted
    to the admission region; include random type-matched swaps as the predicted measurably-anti-conservative control to validate
    the diagnostic's sensitivity. (2) SPONTANEOUS-ERROR TAIL MATCH (the crux the reviewer named): collect the scores of GENUINE
    extractor errors -- spontaneous false reals identified vs crisp gold -- and run a tail CDF-match test between counterfactual-decoy
    scores and these spontaneous-error scores; explicitly report the matching GAP and discuss why matching the false-real
    (not true-positive) distribution is the load-bearing requirement; assert the decoy family as valid only if it passes this
    match, else report the gap and re-tune. (3) GENERATOR!=SCORER ABLATION (S2b, de-circularization): re-run the win-rate
    / CDF tests and a small labeled-slice diagonal with decoys generated by model G but scored by a DIFFERENT-FAMILY model
    S via OpenRouter (e.g., G=an OpenAI-family nano model, S=a cheap Llama/Qwen/Mistral-family model), plus the symmetric
    swap; if exchangeability and the diagonal hold ONLY when G=S, report this as a localized shared-model artifact (a reported
    negative result), not as confirmation. Use the canonical W_i; compute all CIs by document-block bootstrap (B>=2000); apply
    a Benjamini-Hochberg multiplicity correction across the family of validation tests. Keep all scoring isolated and provenance-blinded.
    Use cheap sub-$0.30/M models with caching; gradual scaling; log cumulative cost after EVERY call; soft cap ~$1.5 for this
    experiment, HARD STOP at $10. Output method_out.json with the tail-exchangeability tables, the decoy-vs-spontaneous-error
    match (figure-ready CDFs), and the G==S vs G!=S verdict with its validity-region statement.
  depends_on:
  - id: art_XZyKy6QuwxrO
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_SLUbUUr6Ul98
    label: methodology
    relation_type:
    relation_rationale:
- id: experiment_iter2_dir3
  type: experiment
  objective: >-
    Produce the OPERATIONAL WEDGE on Re-DocRED: at matched recall, does decoy-gating beat the plain confidence-threshold gate
    (primary zero-label foil) on atomic-fact precision and hallucinated-conclusion rate, and stay competitive with labeled
    conformal -- with all baselines on the shared triple schema and an explicit alignment-error sensitivity check (S4 + evidence
    MINOR).
  approach: >-
    Per the pipeline spec [art_K6AE23HoGqe6], implement the single fixed claim-decomposition + relation-alignment step (MiniLM
    top-8 relation shortlist -> temperature-0 LLM pick among the 96 Wikidata P-codes or NO_RELATION, with the three-tier entity-linking
    exact/alias/embedding procedure) that maps EVERY system's raw output identically into the (head-entity, P-code, tail-entity)
    triple space, scored by the official (title, r, h_idx, t_idx) matching metric against Re-DocRED human gold. SYSTEMS compared
    at a common operating point (recall matched by sweeping each system's own score): (a) decoy-gating (the method), (b) the
    PLAIN confidence-threshold gate -- identical elicitation, NO decoy/competition/entrapment (the load-bearing primary zero-label
    foil), (c) chain-of-thought extraction, (d) RAG (BM25 retrieval), (e) labeled Mohri-Hashimoto conformal back-off (the
    labeled reference, with its calibration-label cost charged symmetrically against our zero labels). At the matched-recall
    point report precision, the hallucinated-conclusion rate (fraction of multi-hop derived conclusions whose triple is not
    entailed by gold), and PR curves, all with document-block-bootstrap CIs (B>=2000). CRITICAL CONFOUND CHECK (evidence MINOR):
    measure the relation-alignment step's OWN error rate on a labeled slice and verify the wedge survives reasonable alignment-error
    perturbation (re-run the comparison under injected alignment noise / an alternative alignment threshold), so 'decoy-gating
    beats thresholding' is isolated from alignment noise that hits all systems uniformly. Assert ONLY relative comparisons
    (Re-DocRED residual false negatives affect all systems equally; no absolute FDR diagonal here -- that belongs to CLUTRR).
    Pre-register the operational disconfirmation: if decoy-gating shows no precision/hallucination advantage over the plain
    threshold at matched recall, the wedge collapses to 'thresholding is enough' and is reported as disconfirmed. Use the
    spec's cheap model + document-prefix caching; gradual scaling mini->full; log cumulative cost after EVERY call; soft cap
    ~$3 for this experiment, HARD STOP at $10. Output method_out.json with figure-ready matched-recall PR arrays and hallucination-rate
    bars per system with CIs, plus the alignment-error rate and its sensitivity result.
  depends_on:
  - id: art_Jcudmkugg1qT
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_K6AE23HoGqe6
    label: pipeline
    relation_type:
    relation_rationale:
  - id: art_SLUbUUr6Ul98
    label: methodology
    relation_type:
    relation_rationale:
- id: dataset_iter2_dir4
  type: dataset
  objective: >-
    Build the genre-faithful APPLICATION anchor the scope MAJOR demands: ~15-30 genuine short professionally-written legal/news/regulatory
    documents (~1500-3000 characters, the goal's target length) standardized to the shared (head, relation, tail) triple schema
    with trustworthy gold atomic facts, entity typing for upper-ontology grounding, and provenance spans -- so next iteration
    can run the application-faithful hallucination-reduction experiment (decoy-gated extraction vs raw LLM generation) and
    export auditable trace-graphs on the genres the goal actually targets.
  approach: >-
    Source REAL professional documents with reliable gold, strongly preferring freely-available human-annotated information-extraction
    corpora so the gold is crisp-enough for the RELATIVE hallucination comparison: legal (e.g., CUAD contract-clause annotations,
    EUR-Lex provisions, court-opinion syllabi/holdings, ContractNLI), news/newswire (e.g., a relation- or event-annotated
    newswire set such as a freely-licensed slice of relation-extraction or event corpora; avoid LDC-restricted ACE unless
    an open mirror exists), and regulatory (e.g., eCFR or GDPR article snippets paired with structured summaries). Select
    ~15-30 documents in the ~1500-3000 char range, balanced across the three genres, with native length preserved (never padded).
    For each document produce a standardized row mapping to the SAME shared triple schema used by the CLUTRR and Re-DocRED
    anchors: input = {doc_id, document_text, genre, source, char_length, entities[{name, type, char_span}]}; output = {gold_atomic_facts[{head,
    relation, tail, provenance_char_span}]}; metadata_* = coarse upper-ontology entity types (PER/ORG/LOC/TIME/NUM/MISC, with
    finer ontology classes where the source provides them), a gold_quality flag distinguishing CRISP human-annotated gold
    from documented SILVER curated gold, license, and the genre fold. Where a document has no pre-existing annotation, apply
    a documented high-rigor curation protocol (deterministic extraction from structured companion data, or careful manual-style
    curation with explicit cross-checks) and label the result silver, recording the limitation transparently. Do NOT run any
    LLM scoring, decoy generation, FDR, or Prolog here (those are the next-iteration application experiment's job, which will
    depend on THIS dataset). Validate every row with aii-json against a row schema; split full/mini/preview; keep total size
    well under 300MB; ensure deterministic regeneration from cached raw sources under a fixed seed. Record citations, URLs,
    licenses, and per-genre counts in a dataset_meta.json companion.
  depends_on:
  - id: art_K6AE23HoGqe6
    label: schema-guidance
    relation_type:
    relation_rationale:
- id: research_iter2_dir5
  type: research
  objective: >-
    Close three remaining reviewer gaps with one focused specification: (a) a crisp NOVELTY comparison table preempting the
    'this is just labeled conformal selection at the fact level' rebuttal (novelty MINOR), (b) a concrete REAL upper-ontology
    grounding recipe with explicit justification of any commodity substitute (scope MAJOR -- the OpenCyc substitution), and
    (c) a concrete LLM-as-PROBABILISTIC-reasoning-engine design at fuzzy unifications (scope MAJOR -- the deterministic-for-probabilistic
    substitution, and the goal's named 'probabilistic reasoning engine' requirement).
  approach: >-
    Web-research (aii-web-tools: search -> fetch -> fetch_grep) and synthesize into research_out.json + research_report.md.
    (a) NOVELTY TABLE: build a one-page table contrasting decoy-gated extraction against its nearest neighbors -- conformal
    selection (Jin-Candes), multiple-testing hallucination detection (Li/Magesh/Veeravalli), COCOCO (conformal sets for neuro-symbolic
    concept-based models), conformal e-value novelty detection with FDR control, conformal link-prediction FDR, and Mohri-Hashimoto
    conformal factuality -- across the dimensions {label requirement (labeled vs label-free), unit certified (final answer
    / claim set vs INTERMEDIATE admission/bridge), exchangeability mechanism, decoy/competition-based?, controls FDR vs coverage};
    state the precise delta in one sentence (label-free + decoy competition + neural-to-symbolic admission boundary). (b)
    UPPER-ONTOLOGY GROUNDING: survey the real options for OpenCyc-style taxonomic grounding -- OpenCyc/ResearchCyc current
    availability and access route, SUMO, DBpedia/YAGO ontology classes, Wikidata class hierarchy, WordNet hypernyms -- and
    specify ONE concrete argument-typing recipe with library/API; explicitly justify the commodity substitute by stating what
    taxonomic grounding is LOST relative to OpenCyc and why typing-only usage (constraining decoy generation and entity linking,
    never filtering) suffices, and which goal requirement is descoped vs deferred. (c) PROBABILISTIC REASONING ENGINE: specify
    a concrete LLM-as-probabilistic-reasoner design at the fuzzy-unification boundary -- e.g., ProbLog (the problog Python
    package) or a fuzzy-unification layer where the LLM supplies calibrated unification/bridge probabilities that feed probabilistic
    inference, with the exact API, how the decoy-competition certificate (W_i, T, alpha) and entrapment certificate map onto
    the probabilistic weights, and how probabilistic trace-graphs are produced -- justifying the iteration-1 deterministic
    backward-chaining substitution and giving the implementable upgrade path. Output concrete tables, recipes, library choices,
    and a short source-traceable positioning note.
  depends_on:
  - id: art_SLUbUUr6Ul98
    label: extends
    relation_type:
    relation_rationale:
  - id: art_K6AE23HoGqe6
    label: extends
    relation_type:
    relation_rationale:
expected_outcome: >-
  After this iteration the project will hold its FIRST empirical results on every central claim, directly dissolving the dominant
  3/10 'no results' blocker: (1) a realized CLUTRR calibration diagonal (alpha vs realized FDR) on the populable multi-hop
  family with document-block-bootstrap CIs, a reported certified-alpha grid, an explicit pre-run power calculation stating
  which alphas are demonstrable at what CI half-width, entrapment corroboration, and a definite primary-disconfirmation verdict
  (confirmed / disconfirmed / untestable-at-this-difficulty -- each interpretable); (2) a prominently-reported decoy-mechanism
  validation -- tail-conditioned win-rate, upper-tail CDF tests, the decoy-vs-spontaneous-error tail match, and the generator!=scorer
  ablation -- that establishes (or bounds) the gate's empirical validity region and answers the circularity MAJOR head-on;
  (3) a Re-DocRED operational wedge with matched-recall PR curves and hallucinated-conclusion rates for decoy-gating vs the
  plain-threshold foil, CoT, RAG, and labeled conformal, plus the alignment-step error rate isolating the wedge from alignment
  noise; (4) a schema-validated professional-document anchor (~15-30 genuine legal/news/regulatory ~3000-char docs with gold)
  that closes the scope gap structurally and unblocks next iteration's application-faithful hallucination-reduction experiment;
  and (5) a novelty comparison table plus justified specifications for real upper-ontology grounding and an LLM probabilistic-reasoning
  engine, answering the novelty and substitution objections. Together these turn the iteration-1 proposal into an empirically-grounded
  paper, with the canonical W_i statistic, the bootstrap-vs-validity separation, and figure-ready diagonal/wedge arrays all
  in hand for the rewrite. Total LLM spend held well under the $10 cap by conservative per-experiment soft caps and cumulative
  cost logging.
summary: >-
  Execute, don't re-plan. Three parallel, self-contained EXPERIMENTS on the existing validated anchors deliver the three realized
  numbers the prior paper lacked -- the CLUTRR calibration diagonal with a demonstrated power analysis (S0/S2/S3 + power),
  the Re-DocRED operational wedge vs the plain-threshold foil at matched recall with an alignment-error check (S4), and a
  first-class decoy-mechanism validation with a generator!=scorer de-circularization and a decoy-vs-spontaneous-error tail
  match (S1/S2b) -- directly answering the empirical-results, methodology-circularity, and power MAJORs. In parallel, a DATASET
  builds the genre-faithful professional-document application anchor and a RESEARCH spec supplies the novelty comparison table
  and the justified OpenCyc / probabilistic-reasoning substitutions, closing the scope and novelty objections. All five run
  concurrently, depend only on iteration-1 artifacts, use the canonical knockoff+ statistic and document-block-bootstrap CIs,
  and share the $10 cap under conservative per-experiment soft caps.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 2 ---
id: art_Jcudmkugg1qT
type: dataset
title: >-
  Re-DocRED Anchor: 236-doc triple-schema corpus with entities, evidence & 4 CV folds
summary: |-
  Operational-anchor dataset standardized from Re-DocRED (Tan et al., 'Revisiting DocRED — Addressing the False Negative Problem in Relation Extraction', EMNLP 2022; HuggingFace tonytan48/Re-DocRED, MIT, 606 downloads, arXiv 2205.12696). THE single chosen dataset for the label-free FDR-gating / neuro-symbolic text→logic hypothesis.

  FORMAT: full_data_out.json follows the exp_sel_data_out contract: {metadata, datasets:[{dataset:'Re-DocRED', examples:[...]}]}. 236 examples = one Wikipedia document each, drawn from 4053 pooled train/dev/test docs. Each example is raw data only (NO candidates, decoys, scores, or FDR — those are the experiment's job).

  PER-EXAMPLE FIELDS: input = the reconstructed ~200-word document prose (deterministic detokenization, exact char offsets); output = JSON string of the gold (head,relation,tail) triples. metadata_* carries the rich structure: metadata_entities (full annotated inventory, 6 types, mention token spans + exact char_spans, canonical_name, n_mentions), metadata_gold_triples (shared canonical schema: head/tail id+name+type, relation_pid+relation_name, evidence_sent_ids, resolved evidence_text), metadata_sents (verbatim tokens, authoritative grounding), metadata_sent_char_offsets, and 17 metadata_features S5 GAP-regression inputs (num_words/chars/sents/entities/triples, relation & entity-type profiles, entity/mention/triple densities, frac_singleton_entities, frac_multi_evidence_triples, max_evidence_sentence_gap). Flags: metadata_fold (cluster_PER/ORG/LOC/MISC — primary dominant-entity-type folds for leave-one-cluster-out CV), metadata_kmeans_cluster (secondary k-means scheme), metadata_split_role + metadata_is_confirmatory/is_pilot/is_reserve, metadata_seed (20240617).

  BALANCE: 152 confirmatory / 36 pilot / 48 reserve, exactly balanced across the 4 folds (38/9/12 each), examples interleaved round-robin by fold; documents span the feature range so cross-document variance (the S5 precondition) is preserved (e.g. triple_density 0.38–14.75 across folds). Eligibility: 80≤num_words≤400, ≥4 entities, ≥5 triples. Confirmatory/pilot/reserve are mutually exclusive; every triple indexes a valid entity (verified).

  COMPANIONS: relation_schema.json (all 96 Wikidata P-ids with human-readable names AND descriptions, fetched live from the Wikidata API — the shared triple space every downstream system aligns to), entity_type_schema.json (6 types + glosses), dataset_meta.json (citation, URLs, counts, seed, cluster schemes, per-fold counts), row_schema.json (the custom JSON-Schema every row was validated against).

  GOLD CAVEAT (recorded in metadata): Re-DocRED has residual false negatives, so this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) — never an absolute realized-FDR diagonal (that role belongs to the separate CLUTRR anchor).

  REPRODUCIBILITY: pure-CPU data prep; `uv run data.py` regenerates everything deterministically from cached raw JSON (re-downloads from HF/GitHub if absent; relation names from Wikidata or cache). pyproject.toml pins all 13 dependency versions. full=11.7MB (<100MB, no split); all of full/mini/preview validate against exp_sel_data_out.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 3 ---
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
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 4 ---
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
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 5 ---
id: art_ikjFm_faAe0x
type: experiment
title: 'CLUTRR Label-Free Knockoff+ FDR Gate: Calibration Diagonal, Power & Entrapment'
summary: >-
  This artifact executes the end-to-end label-free decoy-competition (knockoff+) FDR gate on the crisp-gold CLUTRR kinship
  anchor (190 docs: 40 pilot + 150 confirmatory), testing whether a label-free admission gate can control the false-discovery
  rate of LLM-extracted facts entering a symbolic layer. Pipeline (openai/gpt-4.1-nano via OpenRouter, isolated provenance-blinded
  scoring, persistent on-disk cache, $0.42 total spend << $10 cap, 1540 scored candidates): over-generation extraction (atomic
  + multi-hop bridge families), property-matched counterfactual decoys with non-entailment verification, deterministic entrapment
  items (r=1), and four scoring elicitations. The Phase-0 pilot selected the scorer by upper-tail AUC (verbalized, tail-AUC
  0.86 with bootstrap CI excluding 0.5, so the S0 separation precondition PASSED) and set alpha*=0.3; populability far exceeds
  the N_false_min=40 floor (bridge 175, atomic 118, pooled 293 genuine false candidates), so the diagonal is TESTABLE rather
  than untestable. Method vs baselines (implemented side-by-side in one pipeline to remove confounds): (1) OUR knockoff+ gate
  with canonical statistic W_i=sign(Z_i-Z~_i)*max(Z_i,Z~_i) and the Barber-Candes +1 data-dependent threshold; (2) PLAIN confidence-threshold
  baseline (decoy-free primary foil); (3) SWAP-decoy negative control. HEADLINE bridge diagonal (realized FDR vs target alpha,
  document-block bootstrap B=2000 CIs): the knockoff+ gate is CONSERVATIVELY calibrated, with realized FDR ~0.21 at alpha=0.2/0.3
  (n_admitted=56, 12 false) and ~0.25 at alpha=0.5 (n_admitted=113), staying at or below alpha+tau across the certified grid,
  whereas the plain confidence baseline is ANTI-CONSERVATIVE, with realized FDR rising 0.34->0.55 as alpha loosens. The single
  pre-registered primary disconfirmation at alpha*=0.3 returns NOT_DISCONFIRMED (realized 0.214, CI [0.12,0.33] not entirely
  above alpha*). Independent deterministic entrapment corroboration at alpha* gives N_T=56, N_E=10, FDP_combined=FDP_paired=0.30,
  agreeing with the gold realized FDR (3-way check). Overall calibration_verdict=CONFIRMED. Outputs: method.py (orchestrator)
  plus fdr_core.py, pipeline.py, llm_client.py, tests.py, and method_out.json (validates against exp_gen_sol_out: 1540 figure-ready
  candidate rows carrying per-item W, z_real, z_cf/z_swap/z_entrapment, gold label, predict_our_method and predict_baseline;
  top-level metadata holds the full per-family diagonal arrays, power table, populability counts, decoy-control tail diagnostics,
  entrapment estimators, and the disconfirmation verdict). full/mini/preview variants emitted and all four files are <100MB
  (no split needed). Scope: tests claim rows S0 (precondition) + S2 (diagonal) + S3 (entrapment) + power; deliberately excludes
  the Re-DocRED wedge, Prolog execution/trace-graphs, and the generator!=scorer ablation (separate experiments).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 6 ---
id: art_Inu52CyA49Ys
type: experiment
title: Label-free decoy-competition FDR gate validated on CLUTRR crisp gold
summary: |-
  Executable validation of a LABEL-FREE decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into a symbolic layer without gold labels. Each extracted 'real' fact competes against a property-matched COUNTERFACTUAL decoy (same ordered entity pair, plausible-but-wrong relation, verified non-entailed against gold) plus a random type-matched swap control; a label-free confidence elicitation scores both in isolated, provenance-blinded, identical-template calls; canonical signed-max W_i + Barber-Candes knockoff+ threshold (eq 1.9) turn decoy wins into an FDR certificate. Run on the 190-doc CLUTRR crisp-gold anchor (40 pilot + 150 confirmatory) producing 1937 reals (633 TRUE, 1304 spontaneous FALSE extractor errors, 0 undecidable), each with a counterfactual decoy and a swap, scored under TWO elicitations (gpt-4.1-nano logprob softmax; K=5 self-consistency) plus a 4-config Generator!=Scorer ablation using a cross-family scorer (mistralai/ministral-8b-2512).

  HEADLINE (the gate's validity is ELICITATION-DEPENDENT): (1) S1 decoy signature - under single-token logprob confidence the LLM is overconfident in its OWN spontaneous errors, so counterfactual decoys are strongly anti-conservative (tail win-rate 0.34, 95% CI [0.32,0.37], KS p<1e-24); under K=5 self-consistency the decoys are EXCHANGEABLE (win-rate 0.482, CI [0.42,0.55] covers 0.5, KS p=0.48). The random-swap negative control is flagged anti-conservative under logprob (and by the offline synthetic self-test), validating diagnostic sensitivity. (2) Spontaneous-error tail match (the crux) - under self-consistency the counterfactual-decoy score distribution matches the genuine spontaneous-error distribution in the admission tail (top-25%/50% KS p=0.33/0.19, fail-to-reject) and differs sharply from the true-positive distribution (KS p~1e-40); figure-ready overlaid CDFs exported. (3) Generator!=Scorer de-circularization - exchangeability holds for ALL four (G,S) configs incl. G!=S (win-rate CIs cover 0.5; labeled-slice realized FDR 0.0 at alpha=0.2): verdict ROBUST, not a shared-model artifact. (4) Method vs purely-neural BASELINE - against crisp gold the decoy-FDR gate controls realized FDR <= nominal where it certifies (0.417 <= 0.5; conservative/zero-admit at stricter alpha), whereas the raw-confidence baseline admits 254-1758 facts at 45-65% realized FDR - the quantified hallucination problem the gate prevents.

  All p-values are document-block (cluster) bootstrap (B=2000) and Benjamini-Hochberg corrected (q=0.05; 42 tests, 27 reject). Cost: final cache-warm run $0.47, ~$1.05 total across gradual-scaling runs, hard cap $10 never neared (exact per-call USD from OpenRouter usage.cost; disk cache for free resumes). HONEST LIMITATIONS: knockoff+ is conservative on this signal (certifies admissions only at alpha=0.5 on 190 docs); the full-distribution crux match is borderline (a tail phenomenon); gpt-4.1-nano's genuine extraction is error-prone (atomic precision ~0.50, multi-hop accuracy ~0.20) - these real errors are the experimental signal, not a confound; self-consistency reduces sensitivity to the swap control.

  OUTPUTS for the paper writer: method_out.json (schema exp_gen_sol_out, validated) carries metadata.headline_finding/headline_verdict, elicitation_comparison, s1_decoy_signature_by_elicitation, spontaneous_error_match_by_elicitation (with figure_cdfs), generator_ne_scorer (verdict + validity_region_statement), baseline_vs_method_fdr_by_elicitation, bh_correction, extraction_quality; the 1937 examples each hold per-elicitation real/decoy/swap scores, W_i, and admission predictions. Companion files: fdr_stats.py (unit-tested statistical core), llm_client.py (async cached cost-capped OpenRouter client), make_figures.py + figures/fig1-4 (decoy signature, crux CDFs, FDR calibration, ablation), README.md, pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 7 ---
id: art_sHNuY68d4-Wh
type: experiment
title: >-
  Re-DocRED Operational Wedge: Decoy-Gating vs Plain Confidence Threshold at Matched Recall
summary: >-
  Operational-wedge experiment (S4) on the Re-DocRED anchor (152 confirmatory + 36 pilot-calibration Wikipedia documents).
  It answers a single load-bearing question for the label-free FDR-gating / neuro-symbolic text->logic hypothesis: at MATCHED
  RECALL, does ranking LLM-extracted atomic facts by the knockoff+ decoy-competition statistic W_i = max(Z_i, Z~_i)*sign(Z_i
  - Z~_i) admit a higher-precision, lower-hallucination set than ranking by the raw confidence Z_i (the PLAIN zero-label threshold
  foil)? method.py implements both systems side-by-side over an IDENTICAL candidate+alignment pool (only the gate differs),
  plus CoT, BM25-RAG, and a labeled Mohri-Hashimoto conformal back-off reference. All five systems are mapped into the SAME
  (title, P-code, head_id, tail_id) triple space by ONE fixed aligner (MiniLM top-8 shortlist + temp-0 LLM relation pick +
  three-tier entity linking) and scored by the official tuple-matching metric against human gold. Graded scoring uses the
  logprob yes-token probability (verbalized [0,1] fallback); decoys are property-matched DeepCoy-style counterfactuals that
  recombine the document's OWN entities into a non-entailed pairing (verified, regenerated up to 3x). method_out.json (schema
  exp_gen_sol_out) provides: figure-ready per-system PR curves; the matched-recall precision wedge delta(METHOD-PLAIN) across
  a recall grid with document-block bootstrap CIs (B=2000) and BH correction; multi-hop hallucinated-conclusion rate from
  a fixed pure-Python Datalog forward-chainer (rules listed); knockoff+ operating points over alpha in {0.05,0.1,0.2,0.3,0.5}
  with the 1/k floor; labeled conformal operating points (n_calibration_labels reported; the method uses 0); the mandatory
  alignment-error confound check (aligner self-error probe ~0.98 relation / ~0.99 entity-link on gold surface forms, plus
  perturbation sensitivity to uniform P-code noise 5/10/20%, an embedding-only aligner, and a stricter entity-link floor);
  decoy contamination rate; and a pre-registered verdict. Only RELATIVE comparisons are asserted (Re-DocRED residual false
  negatives depress recall and inflate hallucination counts equally for all systems). Result: a clean pre-registered OPERATIONAL
  DISCONFIRMATION -- with a well-calibrated logprob scorer the decoy competition does not beat (and is marginally worse than)
  plain thresholding at matched recall, i.e. 'thresholding-is-enough'. Pure-CPU, model openai/gpt-4.1-nano via OpenRouter,
  exact per-call cost metering with soft cap ~$3 and hard stop $10. Downstream (GEN_PAPER_TEXT) can use the PR/wedge/hallucination
  arrays and CIs directly as figures and the verdict + aligner-robustness numbers as the evidentiary core.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 8 ---
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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 9 ---
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
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.


# Introduction

Operational pipelines that convert unstructured prose into a formal, computable representation---one a logic engine such as SWI-Prolog can execute---promise the best of two worlds: the broad coverage of an LLM as a semantic translator, and the verifiable, auditable inference of a symbolic reasoner. The recurring failure point of such pipelines is not parsing syntax but the *fuzzy-unification boundary*: when strict symbolic matching fails, an LLM must align a surface predicate to a schema relation and supply implicit background knowledge, and exactly at that interface hallucination re-enters and propagates into every deduction that consumes the admitted fact. The dangerous hallucinations are not random nonsense; they are *plausible, high-confidence false facts* that a downstream solver will treat as ground truth.

The problem is both practically important and technically hard. It is important because a single fabricated premise admitted into a knowledge base contaminates an unbounded set of multi-hop conclusions, and because the application domains that most need auditable reasoning---short legal documents, news, regulatory text---are precisely those where a silently wrong fact is most costly. It is hard because the standard defenses do not act where the damage occurs. Self-consistency and LLM-as-judge are heuristic and provide no quantitative control. Ontology-constraint filtering rejects only encoded violations and needs a rich trusted constraint set. The strongest uncertainty-quantification methods---conformal factuality [15], conformal selection with Benjamini--Hochberg [16], multiple-testing hallucination detection [18], coherent factuality over reasoning chains [17], conformal e-value novelty detection [29], and conformal link-prediction FDR [30]---all require a *labeled* calibration set and certify the *final answer or claim set*, not the *admission* of an intermediate fact or bridge into the symbolic layer.

Why has the admission boundary not been controlled before? Because the natural statistical tool for controlling false admissions among many candidate signals with no ground truth---the *false discovery rate* (FDR)---was developed in numeric feature selection and mass spectrometry, where a synthetic negative control exchangeable *by construction* is available. Genomics and proteomics solved an isomorphic label-poor problem---selecting true signals among overwhelming noise with a guaranteed FDR and no labels---via the knockoff filter [4, 5] and target-decoy competition, and learned the two ways the trick breaks: decoys *too unrealistic to fool* the scorer make the estimated FDR optimistic (cured by property-matched decoys [9]), and entrapment false-discovery-proportion (FDP) must be estimated with a valid upper bound built *independently* of the decoys [6]. No prior work imports this machinery to the LLM neural-to-symbolic boundary, label-free.

This paper does so, and---unlike its predecessor, which the reviewers correctly judged a proposal because it reported no measured outcome---it *executes* the protocol end to end and reports the realized numbers, including the ones that disconfirm. We propose *decoy-gated extraction*: before any LLM-proposed Prolog fact or bridge enters the knowledge base, it must out-score a *plausibility-matched* synthetic decoy---a document-conditioned counterfactual the model finds plausible but the document does not entail---in a knockoff+ competition that admits the most permissive cutoff whose estimated corpus-aggregate FDR is at most a target $\alpha$, using zero operation labels. The single canonical competition statistic is the knockoff+ *signed maximum* $W_i = \operatorname{sign}(Z_i - \tilde{Z}_i)\,\max(Z_i, \tilde{Z}_i)$, where $Z_i$ and $\tilde{Z}_i$ are the label-free scores of the real candidate and its matched decoy; the per-pair *difference* $d_i = Z_i - \tilde{Z}_i$ is reserved exclusively for tail diagnostics. Knockoff+ thresholding scans cutoffs and admits $\{i : W_i \ge T\}$ at the most permissive $T$ whose estimate $\widehat{\mathrm{FDR}}(T) = (1 + \#\{W_i \le -T\}) / \max(1, \#\{W_i \ge T\}) \le \alpha$ [4]. Validity rests on the *null sign-flip property* (for genuinely-false candidates the sign of $W_i$ is a fair coin conditional on $|W_i|$); because LLM decoys carry no construction-level proof of this property, the realized-FDR-versus-$\alpha$ diagonal *is* its empirical test, not a corollary of a theorem.

Our headline finding is that a label-free FDR knob at this interface is achievable, and that its validity is *elicitation-dependent in a way the method itself detects*. On crisp-gold CLUTRR the gate is conservatively calibrated on the error-dense multi-hop family where a plain confidence threshold is anti-conservative, the pre-registered primary disconfirmation does not fire, and independent deterministic entrapment corroborates the gold FDR [ARTIFACT:art_ikjFm_faAe0x]. A dedicated mechanism study isolates *why*: single-token log-probability confidence makes the model rate its own spontaneous hallucinations too highly, so counterfactual decoys are too easy and the gate becomes anti-conservative, whereas $K{=}5$ self-consistency restores exchangeability between decoys and genuine spontaneous errors in the admission tail---and the result is robust to scoring with a different model family, refuting the shared-model circularity objection [ARTIFACT:art_Inu52CyA49Ys]. We are equally explicit about the negative result: on open-vocabulary Re-DocRED, with an already-calibrated scorer, decoy competition does *not* beat a plain threshold at matched recall---the wedge collapses to "thresholding is enough" [ARTIFACT:art_sHNuY68d4-Wh]. The two outcomes are one coherent story: the gate's value is concentrated exactly where the base confidence signal is overconfident, and the tail diagnostics tell the practitioner which regime they are in.

[FIGURE:fig1]

**Summary of contributions.**

- We formulate the *text-to-logic admission boundary* as an FDR-control problem and introduce *decoy-gated extraction*, to our knowledge the first label-free FDR knob at the neural-to-symbolic interface, built from a single canonical knockoff+ statistic, plausibility-matched counterfactual decoys, and independent entrapment corroboration (Sections 3--4).
- We *execute* the pre-registered protocol and report measured outcomes with document-block-bootstrap confidence intervals: a conservatively calibrated CLUTRR diagonal with the disconfirmation not firing, a quantified hallucination reduction versus raw LLM generation, and a disconfirmed Re-DocRED operational wedge (Section 6).
- We establish that gate validity is *elicitation-dependent* and characterize the mechanism: overconfident point elicitations break decoy exchangeability while aggregation elicitations restore it, matching the decoy score distribution to that of genuine spontaneous errors---not true positives---in the admission tail (Section 6.3).
- We *de-circularize* the construction with a generator$\neq$scorer ablation across model families and show exchangeability is robust, directly answering the shared-model objection (Section 6.3).
- We deliver three validated anchors---crisp-gold CLUTRR, open-vocabulary Re-DocRED, and a new genre-faithful application set of 24 short legal/news/regulatory documents---together with an offline WordNet$\to$SUMO upper-ontology typing recipe and a ProbLog upgrade path for probabilistic reasoning (Sections 4--5).

# Related Work

**Label-free hallucination scoring.** Zero-resource detectors produce per-claim hallucination scores from sampling consistency (SelfCheckGPT [13]) or distractor-normalized verbalized confidence (DINCO [12]); FactSelfCheck [14] operates natively at the fact level over $(h, r, t)$ triples. These methods yield a *score*, not an admission threshold, and offer no exchangeability or competition argument. In our framework they are *candidate elicitations* feeding the gate, not the gate itself, and our Phase-0 pilot selects among them by tail discrimination. Verbalized confidence is known to be overconfident in the upper tail [10], and token log-probability calibration degrades under reinforcement learning from human feedback [11]---two facts our results turn from caveats into a measured, central phenomenon.

**Labeled uncertainty quantification for LLMs.** Conformal factuality [15] removes claims until a factuality level is met, using a labeled calibration set, and certifies the emitted answer; coherent factuality [17] extends this to reasoning chains; conformal selection [16], multiple-testing hallucination detection [18], and online/feedback-driven testing [19] control FDR over candidate outputs but require labeled calibration outcomes; conformal e-value novelty detection [29] and conformal link prediction [30] control FDR over selected test points or predicted edges under (adapted) exchangeability of a labeled reference set. Table 1 contrasts the closest neighbors on four axes. Every one is *labeled* and certifies a *model output* under assumed exchangeability; ours is *label-free*, certifies an *intermediate admission boundary*, manufactures the null behavior with engineered-and-tested decoys, and controls FDR [ARTIFACT:art_Cr6L9JpoewZi].

\begin{table}[t]
\centering
\small
\begin{tabular}{lcccc}
\toprule
Method & Labels? & Unit certified & Decoy? & Controls \\
\midrule
Conformal selection [16] & Yes & output shortlist & No & FDR \\
Multiple-testing hallucination [18] & Yes & generation & No & FDR \\
Conformal e-value novelty [29] & Yes & test points & No & FDR \\
Conformal link prediction [30] & Yes & predicted edges & No & FDR \\
Conformal factuality [15] & Yes & emitted claims & No & coverage \\
\textbf{Decoy-gating (ours)} & \textbf{No} & \textbf{admission boundary} & \textbf{Yes} & \textbf{FDR} \\
\bottomrule
\end{tabular}
\caption{Decoy-gating against its nearest FDR/conformal neighbors. All prior methods require labeled calibration and certify a model output under assumed exchangeability; ours is label-free, certifies the intermediate text-to-logic admission, and tests an engineered decoy sign-flip.}
\label{tab:novelty}
\end{table}

The distinction defuses the natural rebuttal that decoy-gating "is just conformal selection at the fact level": conformal selection imports exchangeability from a labeled calibration set whose outcomes are observed, whereas we have zero such labels and instead *test* the fair-coin sign-flip property in the score tail. Mohri--Hashimoto conformal factuality [15] remains our load-bearing *labeled reference baseline*, reported side by side with our zero-label gate.

**FDR control by competition.** The knockoff filter [4] and Model-X knockoffs [5] select signals with guaranteed FDR by competing each real candidate against a synthetic negative control exchangeable by construction, relying on the null sign-flip property; the knockoff+ threshold controls FDR exactly via the conservative $+1$ offset [4], which Rajchert and Keich prove is in general necessary [7]. Ebadi et al. give tighter upper prediction bounds on the FDP [8]. In proteomics, entrapment estimation provides an independent FDP bound, with the valid combined estimator and the flawed naive estimator characterized by Wen et al. [6]; property-matched decoy generation (DeepCoy [9]) shows decoys must reproduce the true-positive score distribution. We adapt all three to the LLM boundary, where exchangeability is *not* provable, and therefore add tail-conditioned diagnostics, a document-block bootstrap for within-document dependence [28], and a measured account of the elicitation regime in which the property holds.

**Text-to-logic neuro-symbolic reasoning.** LINC [20] and Logic-LM [21] semantic-parse premises into first-order logic or symbolic programs executed by a solver, with majority voting or solver-error self-refinement; LLM-ASP [23] parses CLUTRR into reusable answer-set modules. None exercises principled control over *which* extracted premises are admitted: a syntactically valid but fabricated premise is never challenged, voting merely smooths variance, and refinement fixes only solver and syntax errors. Standard neural baselines---chain-of-thought prompting [22] and retrieval-augmented generation [26]---have no admission boundary at all. Logical-reasoning benchmarks such as RuleTaker [24], ProofWriter [25], and CLUTRR [1] supply controlled reasoning targets; our calibration anchor is CLUTRR for its crisp templated gold, and our operational anchor is Re-DocRED [2], the false-negative-corrected re-annotation of DocRED [3]. For the symbolic layer we type arguments with WordNet [32] anchored to the SUMO upper ontology [31], and design a probabilistic upgrade on ProbLog [33], whose DeepProbLog extension [34] is the precedent for an external model supplying clause probabilities.

# Preliminaries

We control the false admission of two candidate kinds. A *fact* is a ground typed atom (for example `rel_child(e_alice, e_bob)` with a side type table), and a *bridge* is a fuzzy-unification rule---a kinship composition rule for CLUTRR, or a surface-form-to-schema relation alignment for Re-DocRED. Bridges are first-class admission candidates with their own decoy, score, and gate.

**The canonical competition statistic.** Each candidate $i$ receives a label-free score $Z_i$ from an isolated elicitation and a matched decoy score $\tilde{Z}_i$. We use a single statistic throughout: the knockoff+ *signed maximum*
$$W_i = \operatorname{sign}(Z_i - \tilde{Z}_i)\cdot\max(Z_i, \tilde{Z}_i),$$
whose magnitude is the larger of the two scores and whose sign records which won. A large positive $W_i$ is evidence that the candidate is a true signal. The per-pair *signed difference* $d_i = Z_i - \tilde{Z}_i$ is used *only* as a measurement-only tail diagnostic (win-rate and CDF tests), never as the gating statistic. (The prior draft used two inconsistent definitions of $W_i$; we fix the canonical one here and apply it in every experiment.)

**The target and the two roles of resampling.** The target is the corpus-aggregate FDR---the expected fraction of admitted candidates that are document-non-entailed---held at or below a user-chosen $\alpha$, separately for facts and bridges and per anchor. Two statistical objects must not be conflated. First, knockoff+ delivers a *finite-sample FDR guarantee* only under the joint null sign-flip property; for LLM decoys that property is unprovable, so the realized-FDR-versus-$\alpha$ diagonal *is* its empirical test. Second, the *document-block bootstrap* (resampling whole documents, $B \ge 2000$ [28]) supplies confidence intervals on the realized FDP and a within-document-dependence *diagnostic*; it does *not* restore the guarantee when dependence violates the fair-coin assumption. We keep the two roles separate everywhere: the bootstrap quantifies sampling variability, and validity under dependence is an empirical property established by the tail diagnostics and the isolated-versus-batched check, not a theorem.

# Method

The pipeline has six stages: over-generating extraction, plausibility-matched decoy generation, isolated provenance-blinded scoring, the knockoff+ FDR gate, independent entrapment corroboration, and symbolic reasoning with auditable trace-graphs. The full implementation specification---verbatim prompt templates, on-disk formats, and library APIs---is provided in the supporting research artifacts [ARTIFACT:art_SLUbUUr6Ul98][ARTIFACT:art_K6AE23HoGqe6].

## Extraction with deliberate over-generation

A cheap LLM proposes typed first-order facts and bridges from the document in a LINC/Logic-LM style [20, 21], with argument types grounded in a commodity upper-ontology slice. Because OpenCyc was discontinued by Cycorp in March 2017 and survives only as unmaintained third-party mirrors, and ResearchCyc is license-gated, OpenCyc cannot be a reproducible commodity dependency; we substitute an offline WordNet [32] hypernym lookup that maps each argument head noun into the coarse vocabulary $\{$PER, LOC, ORG, TIME, NUM, MISC$\}$ via anchor synsets, with each coarse type further anchored to a genuine SUMO upper-ontology class (e.g. `person.n.01` $\to$ PER $\to$ `&%Human`) through the `WordNetMappings30` files [31], reusing Re-DocRED's gold mention types when present and typing all CLUTRR arguments to PER [ARTIFACT:art_Cr6L9JpoewZi]. Typing is used *only* to constrain decoy generation and entity linking, never to filter; because it never rejects a candidate it cannot break the FDR guarantee, unlike ontology-constraint filtering. The extractor deliberately *over-generates* (temperature 0.7, multiple samples unioned) so the candidate pool is dense in genuine false positives---a precondition for a non-vacuous calibration diagonal.

## Plausibility-matched counterfactual decoys, and the matching target the reviewers identified

The load-bearing design choice is the decoy family, and the central subtlety---raised sharply in review---is *which* distribution the decoy must match. DeepCoy matches the *true-positive* distribution so that target-decoy competition is calibrated in molecular screening [9]. At the LLM boundary the relevant target is different: the decoy must reproduce the score distribution of the model's *own spontaneous false extractions*---the plausible hallucinations the gate must actually catch---because those, not the true positives, are the genuine false candidates competing for admission. Our primary family is the *document-conditioned counterfactual*: given the document and the relation/type schema, the model produces a maximally plausible fact or bridge that is *not* entailed by the text, matching the surface form and specificity of the document's real facts. Every decoy passes an independent isolated non-entailment check (an accidentally entailed decoy is actually true and would bias the FDR conservatively); the contamination rate is logged (CLUTRR $8.9\%$, Re-DocRED $12.9\%$) [ARTIFACT:art_Inu52CyA49Ys][ARTIFACT:art_sHNuY68d4-Wh]. As a deliberately retained negative control we also generate *random type-matched swaps*, predicted to read anti-conservative precisely because they are too easy. Crucially, we do not assume the decoys match the spontaneous-error distribution---we *test* it directly (Section 6.3), and report the admission-tail region in which the match holds.

## Isolated, provenance-blinded scoring and de-circularization

Each candidate---real, decoy, or entrapment---is scored in its *own* prompt with source identity masked and presentation order randomized, removing the within-batch contrast effects that would let the model implicitly detect the fabricated item and depress its score. Isolated scoring is the default for the full confirmatory set; document-prefix prompt caching makes it affordable. The per-candidate score is produced by a pilot-selected elicitation chosen on *tail* discrimination rather than average calibration: a Phase-0 pilot ranks verbalized confidence, a distractor-normalized DINCO-style score [12], a $K$-sample self-consistency score [13, 14], and a log-probability yes/no-token score, selecting the one whose area under the curve restricted to the admission tail exceeds $0.5$ with a confidence interval.

The reviewers' deepest objection is that the *same* model generates the decoys and scores both candidates, so the gate could merely measure a shared idiosyncrasy. We answer this with two pre-registered moves. First, a *generator$\neq$scorer* ablation: on a labeled slice, decoys generated by model $G$ are scored by a different-family model $S$ (and the symmetric swap), and exchangeability is asserted only if it survives $G \neq S$. Second, a *spontaneous-error match* test elevated to a first-class result: we compare the decoy score distribution to the distribution of genuine spontaneous extractor errors in the admission tail. If the diagonal held only when $G = S$, or if decoys matched true positives rather than spontaneous errors, the control would be reported as an artifact rather than a success.

## The knockoff+ FDR gate and the structural $1/k$ floor

Given the competition statistics, the gate admits $\{i : W_i \ge T\}$ at the smallest cutoff $T$ for which $\widehat{\mathrm{FDR}}(T) \le \alpha$ [4]. The $+1$ in the numerator is conservative and, by Rajchert and Keich, generally necessary [7]; we keep it for the headline certificate. Its conservativeness has a precise structural consequence: with $k$ admissions the smallest attainable FDR estimate is $1/k$, so certifying $\widehat{\mathrm{FDR}} \le \alpha$ requires $k \ge \lceil 1/\alpha \rceil$ admissions. The demonstrable-$\alpha$ grid is therefore tied to a known admission floor: $\alpha \in \{0.05, 0.10, 0.20, 0.30, 0.50\}$ maps to floors $\{20, 10, 5, 4, 2\}$. An $\alpha$ below the floor reachable by an anchor is structurally undemonstrable regardless of model quality---a fact we report rather than paper over.

## Independent entrapment corroboration

Decoy competition decides admission; *entrapment* provides an independent upper bound on the realized FDP, built by a mechanism *distinct* from the decoys (in-genre cross-document swaps, numeric or temporal perturbation, explicit contradiction) and constructed *without* the generating LLM, so the two FDR signals are independent corroborations. We use the valid combined estimator $\widehat{\mathrm{FDP}} = N_E(1 + 1/r)/(N_T + N_E)$ as the default certificate and the tighter paired estimator at $r = 1$ when one-to-one pairing is available, where $N_T$ and $N_E$ are admitted target and entrapment counts and $r$ is the entrapment-to-target ratio; we never use the naive estimator, which Wen et al. prove biased [6].

## Symbolic reasoning and auditable trace-graphs

Admitted facts and bridges populate an SWI-Prolog knowledge base (via the bundled `janus-swi` bridge) for multi-hop deduction [ARTIFACT:art_K6AE23HoGqe6]. A vanilla `solve/2` meta-interpreter captures the backward-chaining proof as a *trace-graph* whose nodes are sub-goals and derived facts and whose edges are labeled rule applications. Every leaf resolves against a side table returning a certificate term: the provenance span, the decoy-competition certificate $(W_i, T, \alpha)$, and the entrapment certificate $(\widehat{\mathrm{FDP}}, r)$. The trace-graph serializes to JSON for machine audit and Graphviz DOT for human audit. A designed *probabilistic* upgrade swaps the deterministic `query_once` for ProbLog's `get_evaluatable().evaluate()` [33], turning each admitted clause into a weighted clause $p_i :: \mathrm{fact}$ with $p_i$ a calibrated function of $Z_i$ (default gate-consistent shrinkage $(1-\widehat{\alpha})\,p_i$), so that derived conclusions carry marginal probabilities while every leaf retains its full certificate [ARTIFACT:art_Cr6L9JpoewZi].

# Experimental Setup

The evaluation is split so that calibration and operational usefulness are proven on the data each suits, and the protocol is pre-registered so that every outcome---confirmed, disconfirmed, or untestable---is interpretable.

## Three anchors with a clean division of labor

CLUTRR [1] is rule-based and templated, so its kinship gold is exact---the property that lets it host the realized-FDR-versus-$\alpha$ *diagonal* and the single primary disconfirmation. The anchor comprises 190 stories (150 confirmatory, 40 pilot) stratified over chain length $k = 2$ to $10$, with all gold derived from CLUTRR's own `proof_state` fields over a 20-relation kinship vocabulary [ARTIFACT:art_XZyKy6QuwxrO]. Re-DocRED [2] is human-annotated, open-vocabulary, and document-level, so it hosts the *operational* claim and the genuine schema-alignment bridge test; the anchor comprises 236 Wikipedia documents with gold $(head, relation, tail)$ triples over 96 Wikidata relations and four balanced entity-type folds [ARTIFACT:art_Jcudmkugg1qT]. Because Re-DocRED retains residual false negatives, it licenses only *relative* operational comparisons under shared gold, never an absolute diagonal. Finally, addressing the reviewers' scope concern, we add a genre-faithful *application anchor*: 24 genuine professionally-written documents (8 legal, 8 news, 8 regulatory; native length 1239--3474 characters, mean 2372, squarely in the $\sim$3000-character target range), standardized to the same triple schema with character-span provenance and 140 human/structure-derived gold facts built with no LLM in the loop [ARTIFACT:art_UBTwyePql8NQ]. CLUTRR proves the knob is calibrated, Re-DocRED probes whether it is operationally useful, and the application anchor is the genre-faithful slice on which the application-faithful hallucination-reduction run is the immediate next step.

## Pipeline, baselines, and metrics

All systems run on commodity CPU with `openai/gpt-4.1-nano` via OpenRouter as the primary model and `mistralai/ministral-8b-2512` as the cross-family scorer for de-circularization. On Re-DocRED a single fixed claim-decomposition and relation-alignment step maps every system's raw output into the shared triple space identically (a MiniLM [27] top-eight relation shortlist followed by a temperature-0 pick among the 96 codes, with three-tier entity linking), and recall is matched by sweeping each system's own score to a common operating point. The comparators are the *plain confidence-threshold gate* (the primary zero-label foil, identical elicitation, no decoy or competition), chain-of-thought [22], retrieval-augmented generation [26], and labeled Mohri--Hashimoto conformal factuality [15]. All confidence intervals use the document-block bootstrap and all multiplicity is controlled by Benjamini--Hochberg at $q = 0.05$.

## Pre-run power analysis

Power was computed before the confirmatory run from pilot admission counts, the $1/k$ floor, and the bootstrap CI half-width [ARTIFACT:art_ikjFm_faAe0x]. On the CLUTRR multi-hop bridge family, $\alpha = 0.05, 0.10, 0.20$ do not clear their floors at pilot scale (projected admissions $0$), whereas $\alpha = 0.30$ (floor $4$, projected $45$ admissions, $15$ false) and $\alpha = 0.50$ (floor $2$, projected $75$ admissions, $19$ false) clear, with projected CI half-widths $\approx 0.23$. Populability far exceeds the pre-registered $N_{\text{false\_min}} = 40$ floor: the confirmatory bridge family contains $710$ genuine false candidates, atomic $469$, pooled $1179$. The diagonal is therefore *testable*, and we report the certified grid honestly: $\alpha$ values whose floor is not reached are dropped rather than counted as "confirmed by conservatism."

# Results

We report results against the pre-registered six-row claim chain (S0--S6), leading with the positive findings and stating the disconfirmation plainly. Table 2 summarizes the claim-chain verdicts.

\begin{table}[t]
\centering
\small
\begin{tabular}{lll}
\toprule
Claim & Test & Verdict \\
\midrule
S0 Score separation & upper-tail AUC $0.86$ $[0.79,0.91]$ & PASS \\
S1 Decoy signature & self-consistency win-rate $0.482$, KS $p{=}0.48$ & PASS \\
S2 Calibration diagonal & realized FDR $\le \alpha{+}\tau$ on bridge family & PASS (certified grid) \\
S2b Generator$\neq$scorer & 4/4 configs win-rate CI covers $0.5$ & ROBUST \\
S3 Entrapment & $\widehat{\mathrm{FDP}}{=}0.30$ brackets gold $0.214$ & AGREES \\
S4 Operational wedge & $\Delta$(METHOD$-$PLAIN) $\le 0$, not sig. & DISCONFIRMED \\
S6 Hallucination reduction & gate $\le$ target vs raw $45$--$65\%$ & PASS (valid regime) \\
\bottomrule
\end{tabular}
\caption{Pre-registered claim-chain verdicts. The calibration claims (S0--S3, S6) pass within the certified regime; the operational wedge (S4) is honestly disconfirmed. S5 (document-level predictive account) was budget-deferred.}
\label{tab:claims}
\end{table}

## The CLUTRR calibration diagonal (S0, S2)

The Phase-0 pilot passed the score-separation precondition (S0): the selected verbalized elicitation reached upper-tail AUC $0.86$ with bootstrap CI $[0.79, 0.91]$ excluding $0.5$ (DINCO $0.87$, self-consistency $0.83$, log-probability $0.81$), and set the operative $\alpha^{*} = 0.3$ [ARTIFACT:art_ikjFm_faAe0x].

[FIGURE:fig2]

On the populable multi-hop bridge family, the decoy gate is *conservatively calibrated* across the certified grid (Figure 2). Realized FDR against crisp gold is $0.214$ at both $\alpha = 0.2$ and $\alpha = 0.3$ (56 admitted, 12 false, bootstrap CI $[0.12, 0.33]$) and $0.248$ at $\alpha = 0.5$ (113 admitted, 28 false, CI $[0.17, 0.33]$); at $\alpha = 0.05, 0.1$ the conservative $+1$ floor forces zero admissions, an honest consequence of the floor rather than a calibration claim. The plain confidence-threshold baseline, by contrast, is *anti-conservative*, with realized FDR rising $0.34 \to 0.41 \to 0.55$ across $\alpha = 0.2, 0.3, 0.5$---it admits at face value the very plausible hallucinations the gate rejects. The atomic family tells the same story more tightly (realized FDR $0.10$ at $\alpha = 0.1$--$0.2$, $0.12$ at $\alpha = 0.3$--$0.5$; plain baseline $0.16 \to 0.48$). The single pre-registered primary disconfirmation, evaluated at $\alpha^{*} = 0.3$ on the bridge family, returns **NOT\_DISCONFIRMED**: realized FDR $0.214$ with CI $[0.12, 0.33]$ does not exceed $\alpha^{*} + \tau$ with the interval entirely on the anti-conservative side (S2 holds within the certified grid).

## Entrapment corroboration (S3)

Independent deterministic entrapment, built without the generating LLM, corroborates the gold FDR at $\alpha^{*} = 0.3$: with $N_T = 56$ admitted reals and $N_E = 10$ admitted entrapment items at $r = 1$, the combined and paired estimators agree at $\widehat{\mathrm{FDP}} = 0.30$ (CI $[0.16, 0.52]$), bracketing the gold realized FDR of $0.214$ from above as a valid upper bound should [ARTIFACT:art_ikjFm_faAe0x]. The three independent FDR signals---decoy estimate, entrapment bound, and crisp gold---are mutually consistent at the operative cutoff.

## Validity is elicitation-dependent, and de-circularized (S1, S2b)

The most informative result is *why* the gate works when it works. A dedicated mechanism study over 1937 reals (633 true, 1304 spontaneous false) decomposes validity by elicitation [ARTIFACT:art_Inu52CyA49Ys].

[FIGURE:fig3]

Under *single-token log-probability* confidence the model is overconfident in its own spontaneous errors, so counterfactual decoys are *too easy* and the gate is strongly anti-conservative: the tail-conditioned win-rate of decoys over known-false reals is $0.18$--$0.34$ across $\alpha$ (well below the exchangeable $0.5$), with KS and Mann--Whitney $p < 10^{-20}$. Under $K{=}5$ *self-consistency* the picture inverts: decoys become *exchangeable* with spontaneous errors (tail win-rate $0.482$, CI $[0.42, 0.55]$ covering $0.5$, KS $p = 0.48$), the random-swap control remains correctly flagged as too easy, and---the crux the reviewers identified---the decoy score distribution *matches the genuine spontaneous-error distribution* in the admission tail (top-25\% KS $p = 0.33$, top-50\% KS $p = 0.19$, both fail-to-reject) while *differing sharply from the true-positive distribution* ($p$ from $10^{-6}$ to $10^{-14}$). Matching spontaneous errors rather than true positives is exactly the condition that makes the null sign-flip plausible at this boundary, and we establish it empirically rather than assume it.

The generator$\neq$scorer ablation refutes the shared-model objection directly. Across all four $(G, S)$ configurations---including decoys generated by gpt-4.1-nano and scored by the cross-family ministral-8b, and the symmetric swap---the tail win-rate CI covers $0.5$ (e.g. $G{\neq}S$: $0.496$, CI $[0.44, 0.55]$, KS $p = 0.15$), so exchangeability is **ROBUST** and not an artifact of a single model scoring its own outputs (S2b holds). Across 42 bootstrap-and-BH-corrected tests, 27 reject, with significance concentrated exactly where the theory predicts: the anti-conservative log-probability decoys and the too-easy random swaps.

## Quantified hallucination reduction versus raw LLM generation (S6/goal requirement)

[FIGURE:fig4]

The goal's hard requirement is a quantified hallucination reduction relative to raw LLM generation, and the gate delivers one in the regime where it is valid. Under self-consistency the decoy gate *controls* realized FDR where it certifies---admitting 319 facts at realized FDR $0.417 \le 0.5$ at $\alpha = 0.5$, and conservatively admitting nothing at stricter $\alpha$---whereas the raw confidence-threshold baseline admits hallucinated facts at *uncontrolled* rates of $45$--$65\%$ (254 facts at $0.45$ FDR rising to 1758 facts at $0.65$) [ARTIFACT:art_Inu52CyA49Ys]. On CLUTRR under the verbalized elicitation the same contrast holds at every certified $\alpha$ (gate $0.21$--$0.25$ versus plain $0.34$--$0.55$). The gate converts an uncontrolled hallucination channel into one whose realized false-admission rate sits at or below the nominal target.

## The operational wedge is disconfirmed on Re-DocRED (S4)

[FIGURE:fig5]

We report the negative result without spin. On Re-DocRED, ranking the identical candidate pool by the knockoff+ statistic $W_i$ does *not* beat ranking by the raw confidence $Z_i$ at matched recall: across the recall grid $0.05$--$0.086$ the precision gap $\Delta(\text{METHOD}-\text{PLAIN})$ ranges from $-0.017$ to $+0.004$ and is never significantly positive under BH (it is significantly *negative* at the highest-recall points), so the pre-registered verdict is an **operational disconfirmation**---the wedge collapses to "thresholding is enough" [ARTIFACT:art_sHNuY68d4-Wh]. The multi-hop hallucinated-conclusion rate is statistically indistinguishable (METHOD $0.50$ vs PLAIN $0.478$, $\Delta = +0.014$, CI $[0, 0.05]$), and the labeled conformal reference (259 calibration labels) is comparable to both. Critically, the result is not an alignment artifact: the shared aligner self-tests at $0.978$ relation accuracy and $0.994$ entity-linking accuracy on gold surface forms, and the (absent) wedge is stable under injected P-code noise of 5--20\%, an embedding-only aligner, and a stricter entity-linking floor. The disconfirmation is consistent with the mechanism: the Re-DocRED scorer is the *well-calibrated* log-probability yes-token signal, precisely the regime in which decoy competition adds nothing over a plain threshold.

## Cost and reproducibility (S-budget)

The entire study ran on commodity CPU. The CLUTRR diagonal cost \$0.42, the elicitation/de-circularization study \$0.47, and the Re-DocRED wedge \$0.35---about \$1.24 total against the \$10 hard cap, with exact per-call cost metering and a persistent on-disk cache enabling free resumes [ARTIFACT:art_ikjFm_faAe0x][ARTIFACT:art_Inu52CyA49Ys][ARTIFACT:art_sHNuY68d4-Wh]. All three anchors regenerate deterministically under fixed seeds.

# Discussion

**What the design buys, and exactly where.** Decoy-gated extraction is the first label-free FDR knob at the fuzzy-unification boundary, and we have now *measured* it rather than projected it. The unifying lesson from the calibration success and the operational disconfirmation is a single, actionable principle: *the gate's value is concentrated where the base confidence signal is overconfident.* When the raw elicitation is wildly miscalibrated in the tail---verbalized confidence and single-token log-probability on CLUTRR, where raw thresholding runs at $34$--$65\%$ FDR---the decoy competition (under an aggregation elicitation) brings realized FDR down to or below the target. When the raw elicitation is already well-calibrated---log-probability yes-token on Re-DocRED---a plain threshold is as good, and the competition is redundant. The decisive practical contribution is therefore not a universal win but a *diagnostic*: the tail win-rate and the spontaneous-error CDF match tell the practitioner, label-free, which regime they are in and whether to trust the gate.

**The elicitation-dependence answers the reviewers' methodology objection.** The reviewers predicted a specific failure mode---that a model may score its own document-anchored hallucinations differently from deliberately-constructed counterfactuals, biasing $W$ signs. Our results confirm that prediction is real (the log-probability regime) *and* show it is detectable and curable: the spontaneous-error match test catches it, an aggregation elicitation fixes it, and the generator$\neq$scorer ablation proves the cured exchangeability is not a shared-model artifact. We thus treat gate validity as an empirically established property reported with its failure region, never an assumed one.

**Limitations.** First, the operational wedge on Re-DocRED is disconfirmed: decoy competition is not a free lunch over plain thresholding when the base scorer is calibrated, and we say so. Second, the calibration success is contingent on the elicitation; a deployment that uses only single-token log-probabilities would see anti-conservative behavior, which is why we ship the diagnostics. Third, the genre-faithful application anchor is *built and validated* but the application-faithful hallucination-reduction run on it has not yet been executed---it is the immediate next step, not a claimed result, and we are explicit that the headline numbers above live on CLUTRR and Re-DocRED proxies. Fourth, we descope two named goal requirements with stated rationale: OpenCyc is discontinued, so we substitute an offline WordNet$\to$SUMO typing stack that supplies taxonomic grounding but not Cyc's assertional commonsense KB; and the executed reasoning layer is deterministic backward chaining, with the ProbLog probabilistic upgrade designed and specified but not yet run. Fifth, Re-DocRED's residual false negatives confine it to relative comparisons, and the demonstrable-$\alpha$ grid is floored by the conservative $+1$.

**Connection to the target application.** The pipeline ingests short professionally written documents, types their entities against an upper ontology, translates them to first-order logic, executes multi-hop deductions in Prolog, and emits auditable trace-graphs on commodity hardware---the operational profile the task demands. The FDR knob is the quantified, label-free hallucination-reduction control that raw LLM generation lacks, and the diagnostics make its applicability self-reporting.

# Conclusion

We formulated the text-to-logic admission boundary as a label-free FDR-control problem, introduced decoy-gated extraction, and---closing the gap that sank the prior draft---executed the protocol end to end. On crisp-gold CLUTRR the gate is conservatively calibrated where a plain confidence threshold is anti-conservative (realized FDR $0.21$--$0.25$ versus $0.34$--$0.55$), the pre-registered disconfirmation does not fire, and independent entrapment corroborates ($\widehat{\mathrm{FDP}} = 0.30$). The validity is elicitation-dependent in a way the method detects: aggregation elicitations restore decoy-to-spontaneous-error exchangeability in the admission tail, the result is robust to a different-family scorer, and against raw generation the gate cuts realized hallucination from $45$--$65\%$ to at or below the nominal target. On Re-DocRED, with an already-calibrated scorer, the operational wedge is honestly disconfirmed. Future work, in registered priority order, is to (1) execute the application-faithful hallucination-reduction run on the validated 24-document anchor with exported trace-graphs; (2) deploy the ProbLog probabilistic-reasoning upgrade at fuzzy unifications; (3) extend the elicitation-regime diagnostic into a deployment-time gate-applicability test; and (4) relax the conservative $+1$ floor via tighter FDP bounds where validity permits.

# References

[1] K. Sinha, S. Sodhani, J. Dong, J. Pineau, and W. L. Hamilton. CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text. In *EMNLP*, 2019.

[2] Q. Tan, L. Xu, L. Bing, H. T. Ng, and S. M. Aljunied. Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction. In *EMNLP*, 2022.

[3] Y. Yao, D. Ye, P. Li, X. Han, Y. Lin, Z. Liu, Z. Liu, L. Huang, J. Zhou, and M. Sun. DocRED: A Large-Scale Document-Level Relation Extraction Dataset. In *ACL*, 2019.

[4] R. F. Barber and E. J. Candès. Controlling the False Discovery Rate via Knockoffs. *Annals of Statistics*, 43(5):2055--2085, 2015.

[5] E. Candès, Y. Fan, L. Janson, and J. Lv. Panning for Gold: Model-X Knockoffs for High-Dimensional Controlled Variable Selection. *Journal of the Royal Statistical Society: Series B*, 2018.

[6] B. Wen, J. Freestone, M. Riffle, M. J. MacCoss, W. S. Noble, and U. Keich. Assessment of False Discovery Rate Control in Tandem Mass Spectrometry Analysis Using Entrapment. *Nature Methods*, 22:1454--1463, 2025.

[7] A. Rajchert and U. Keich. Controlling the False Discovery Rate via Competition: Is the +1 Needed? *Statistics & Probability Letters*, 2022.

[8] A. Ebadi, D. Luo, J. Freestone, W. S. Noble, and U. Keich. Bounding the FDP in Competition-Based Control of the FDR. *arXiv:2302.11837*, 2023.

[9] F. Imrie, A. R. Bradley, and C. M. Deane. Generating Property-Matched Decoy Molecules Using Deep Learning. *Bioinformatics*, 37(15):2134--2141, 2021.

[10] M. Xiong, Z. Hu, X. Lu, Y. Li, J. Fu, J. He, and B. Hooi. Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. In *ICLR*, 2024.

[11] K. Tian, E. Mitchell, A. Zhou, A. Sharma, R. Rafailov, H. Yao, C. Finn, and C. D. Manning. Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback. In *EMNLP*, 2023.

[12] V. Wang and E. Stengel-Eskin. Calibrating Verbalized Confidence with Self-Generated Distractors (DINCO). *arXiv:2509.25532*, 2025.

[13] P. Manakul, A. Liusie, and M. J. F. Gales. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. In *EMNLP*, 2023.

[14] A. Sawczyn, J. Binkowski, D. Janiak, et al. FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs. 2025.

[15] C. Mohri and T. Hashimoto. Language Models with Conformal Factuality Guarantees. In *ICML*, 2024.

[16] Y. Jin and E. J. Candès. Selection by Prediction with Conformal p-values. *Journal of Machine Learning Research*, 2023.

[17] M. Rubin-Toles, M. Gambhir, K. Ramji, et al. Conformal Language Model Reasoning with Coherent Factuality. In *ICLR*, 2025.

[18] J. Li, A. Magesh, and V. V. Veeravalli. Principled Detection of Hallucinations in Large Language Models via Multiple Testing. *arXiv:2508.18473*, 2025.

[19] L. Lu, Y. Huo, H. Ren, Z. Wang, and J. Zou. Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection. *arXiv:2509.03297*, 2025.

[20] T. X. Olausson, A. Gu, B. Lipkin, C. E. Zhang, A. Solar-Lezama, J. B. Tenenbaum, and R. Levy. LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. In *EMNLP*, 2023.

[21] L. Pan, A. Albalak, X. Wang, and W. Y. Wang. Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. In *Findings of EMNLP*, 2023.

[22] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In *NeurIPS*, 2022.

[23] Z. Yang, A. Ishay, and J. Lee. Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text. In *Findings of ACL*, 2023.

[24] P. Clark, O. Tafjord, and K. Richardson. Transformers as Soft Reasoners over Language. In *IJCAI*, 2020.

[25] O. Tafjord, B. Dalvi, and P. Clark. ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language. In *Findings of ACL*, 2021.

[26] P. Lewis, E. Perez, A. Piktus, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In *NeurIPS*, 2020.

[27] N. Reimers and I. Gurevych. Sentence-BERT: Sentence Embeddings Using Siamese BERT-Networks. In *EMNLP*, 2019.

[28] A. C. Cameron, J. B. Gelbach, and D. L. Miller. Bootstrap-Based Improvements for Inference with Clustered Errors. *Review of Economics and Statistics*, 90(3):414--427, 2008.

[29] M. Bashari, A. Epstein, Y. Romano, and M. Sesia. Derandomized Novelty Detection with FDR Control via Conformal E-values. In *NeurIPS*, 2023.

[30] A. Marandon. Conformal Link Prediction for False Discovery Rate Control. *TEST*, 2024.

[31] I. Niles and A. Pease. Towards a Standard Upper Ontology. In *Formal Ontology in Information Systems (FOIS)*, 2001.

[32] G. A. Miller. WordNet: A Lexical Database for English. *Communications of the ACM*, 38(11):39--41, 1995.

[33] L. De Raedt, A. Kimmig, and H. Toivonen. ProbLog: A Probabilistic Prolog and Its Application in Link Discovery. In *IJCAI*, 2007.

[34] R. Manhaeve, S. Dumančić, A. Kimmig, T. Demeester, and L. De Raedt. DeepProbLog: Neural Probabilistic Logic Programming. In *NeurIPS*, 2018.

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (methodology) The 'one coherent story' does not hold across the two CLUTRR experiments. The headline calibration diagonal (S2, the pre-registered disconfirmation) is computed under the VERBALIZED elicitation (art_ikjFm_faAe0x), whose counterfactual decoy tail win-rate is 0.103 on the bridge family (0.167 in the pilot) — by the paper's own diagnostic logic the strongly ANTI-CONSERVATIVE regime ('decoys too easy'). Yet this exact diagonal is reported as 'conservatively calibrated' and the Discussion attributes the FDR reduction to 'an aggregation elicitation.' The exchangeable regime (win-rate 0.482) is established only in a SEPARATE experiment (art_Inu52CyA49Ys) under K=5 self-consistency, where the gate certifies admissions ONLY at α=0.5. So the diagnostic the paper sells as 'telling the practitioner which regime they are in' gives the WRONG signal for the headline result. Reinforcing this, the gate's own FDR estimate is anti-conservative on the diagonal (decoy_fdr_hat=0.125 vs realized 0.214 at α=0.3), and at α=0.2 the realized FDR (0.214) EXCEEDS the nominal target (0.2). The conservative-at-α=0.3 outcome looks driven by a loose target plus verbalized-score discreteness, not by demonstrated exchangeability.
  Action: Re-run the headline CLUTRR diagonal under the self-consistency elicitation that the win-rate diagnostic actually validates, and make THAT the primary diagonal; or, if verbalized is kept, explicitly explain and quantify the discreteness/loose-target mechanism, report that the gate's FDR estimate is anti-conservative, and acknowledge the α=0.2 violation. Align the Discussion sentence ('the decoy competition under an aggregation elicitation brings realized FDR down') with the elicitation that actually produced the CLUTRR diagonal.
- [MAJOR] (evidence) Two specific claims in the paper are contradicted by their own artifacts. (a) Section 6.3 states that under K=5 self-consistency 'the random-swap control remains correctly flagged as too easy.' The artifact (art_Inu52CyA49Ys, portable_full) shows diagnostic_sensitivity_ok=FALSE, with the random-swap tail win-rate at 0.473 and its CI covering 0.5 — i.e., in the valid regime the diagnostic LOSES the ability to flag too-easy decoys (the experiment's own limitations note 'self-consistency reduces sensitivity to the swap control'). This is the opposite of the paper's claim and directly weakens the 'self-detecting diagnostic' contribution. (b) The spontaneous-error 'crux' match is reported using only the tail regions (top-25%/50% KS p=0.33/0.19, fail-to-reject), while the FULL-distribution test is REJECTED (KS p=0.051, MW p=0.036, AD p=0.041, permutation p=0.029; artifact verdict 'GAP:decoys_too_easy(anti-conservative)'). Reporting only the favorable tail without the full-distribution rejection is selective.
  Action: Correct (a) to state that the swap control is flagged anti-conservative only under logprob, NOT under self-consistency, and discuss the loss of diagnostic sensitivity in the valid regime as a limitation (it materially qualifies the 'diagnostic tells you when to trust the gate' contribution). For (b), report the full-distribution rejection alongside the tail fail-to-reject and justify explicitly why the admission tail is the decision-relevant region.
- [MAJOR] (evidence) The Re-DocRED operational disconfirmation (S4) is real but considerably narrower and weaker than the manuscript implies. The artifact (art_sHNuY68d4-Wh) used n_docs_used=36, not the 152 confirmatory documents the Experimental Setup implies (split_role is 'confirmatory' but only 36 docs were scored). The wedge is evaluated only at very low recall (max ≤0.086). Two of the four listed comparators — CoT and RAG — max out at recall 0.049 and 0.041 respectively, below the 0.05 grid start, so their precision is ALL NULL on the comparison grid and they do not actually participate in the wedge despite being presented as comparators. The multi-hop hallucinated-conclusion comparison rests on ~20–24 derived conclusions per system (METHOD 12/24, PLAIN 11/23, CONF 9/18) with per-system CIs spanning [0.29, 1.0] — essentially no statistical power.
  Action: State the true number of documents used and the recall ceiling prominently at the point of the S4 claim. Either complete CoT/RAG to a comparable operating point or remove them from the comparator list for the wedge (do not list baselines that produced no comparable output). Either scale the multi-hop hallucination comparison to enough derived conclusions to have power, or explicitly label it underpowered. Frame the disconfirmation precisely as 'at ≤8.6% recall on 36 documents.'
- [MAJOR] (scope) The target application is still not evaluated, so the goal's hard requirement — a quantified hallucination reduction on short professionally-written legal/news/regulatory documents (~3000 chars) with auditable trace-graphs — is not demonstrated where it is claimed. The 24-document application anchor (art_UBTwyePql8NQ) is built and validated but the hallucination-reduction run is NOT executed. All quantitative results live on CLUTRR (synthetic templated kinship, ~355 chars) and Re-DocRED (Wikipedia paragraphs). The S6 'quantified hallucination reduction' itself holds only in one narrow cell: under self-consistency at α=0.5 (319 facts at realized FDR 0.417 vs baseline 0.453); at every stricter α the gate admits ZERO, and under the logprob elicitation the method is strictly WORSE than the plain baseline at every α (e.g., 0.555 vs 0.228 at α=0.3). OpenCyc grounding and probabilistic (ProbLog) reasoning remain descoped.
  Action: Execute the already-built application hallucination-reduction run on the 24-document anchor and export at least a few deterministic trace-graphs (budget is trivial — ~$1.24 of $10 spent so far); report it as the headline application result. Present S6 with both elicitations side by side and across all α so the regime-dependence (worse-than-baseline under logprob; vacuous below α=0.5 under self-consistency) is not obscured. If the run cannot be completed, re-scope all 'application' framing to the genres actually evaluated.
- [MINOR] (rigor) Several quantitative claims are slightly overstated relative to the artifacts. (a) 'Conservatively calibrated across the certified grid' is violated at α=0.2, where realized FDR 0.214 > 0.2 (same 56 admitted as α=0.3 because the threshold grid is discrete). (b) The pilot selected the verbalized elicitation (tail AUC 0.861) over DINCO (tail AUC 0.871, which is higher) with no stated selection rationale. (c) The three-way entrapment 'mutual consistency' holds only at α*=0.3; at α=0.5 the entrapment FDP (0.420) diverges from the gold FDR (0.248) and the artifact records agree_realized=false.
  Action: Reword to 'realized FDR ≤ α for α≥0.3, marginally exceeding at α=0.2.' State the explicit elicitation-selection criterion and why verbalized was chosen over the higher-AUC DINCO. Restrict entrapment-agreement claims to α* and note the divergence at α=0.5.
- [MINOR] (clarity) The figures appear only as bare [FIGURE:fig1]–[fig5] markers with no captions or descriptions in the manuscript body, so a reader cannot assess what each load-bearing figure (the calibration diagonal, the matched-recall wedge, the elicitation-dependence panels) actually communicates. This was raised in the previous round and is still unaddressed.
  Action: Add a complete caption plus a short description for every figure. Ensure the realized-FDR-vs-α diagonal figure marks the 1/k floor and bootstrap CIs and visibly distinguishes the gate from the plain and swap baselines, and that the wedge figure shows all participating systems with CIs at the matched operating point.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 7 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Short name for this strategy",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 08:28:03 UTC

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

### [4] ASSISTANT · 2026-06-16 08:32:40 UTC

```
I'll start by checking the user uploads folder for any relevant materials, then craft the strategy.
```

### [5] TOOL CALL — Bash · 2026-06-16 08:32:40 UTC

```
List user uploads folder contents:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---" && find /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads -type f 2>/dev/null | head -50
```

### [6] TOOL RESULT — Bash · 2026-06-16 08:32:40 UTC

```
{"stdout": "total 2931\ndrwxr-xr-x  2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 14 root root 3000241 Jun 16 04:40 ..\n---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] ASSISTANT · 2026-06-16 08:34:39 UTC

```
The uploads folder is empty. I have everything I need from the hypothesis, reviewer feedback, existing artifacts, and current paper draft. 

My analysis: this is an **execution iteration**. The reviewers' four MAJOR issues map cleanly onto the hypothesis's P1/P2/P3 mandate. The cleanest, highest-impact strategy is three focused parallel experiments, each landing one MAJOR plus the goal's binding requirement, all depending only on existing artifacts:

- **P1**: re-run the headline CLUTRR diagonal under the *validated* self-consistency elicitation on a scaled corpus, add the `decoy_fdr_hat` self-report check, repair/bound the S1b diagnostic blind spot, and report the crux match in full → fixes MAJOR #1, #2, MINOR #5.
- **P2**: execute the still-missing application hallucination-reduction headline on the 24-doc professional anchor with trace-graphs → fixes MAJOR #4 (the goal's hard requirement).
- **P3**: reframe the Re-DocRED wedge with honest scope, completed/dropped comparators, powered multi-hop, and a novel label-free regime-diagnostic → fixes MAJOR #3.
```

### [8] TOOL CALL — Write · 2026-06-16 08:34:39 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Consolidate Under the Validated Elicitation, Execute the Application Headline, and Reframe the Wedge as a Label-Free Regime-Diagnostic",
      "objective": "Turn iteration-2's central finding -- that the gate's validity is ELICITATION-DEPENDENT -- into one internally consistent, genre-faithful, publishable story by executing three things the reviewers and the goal require but the current paper lacks. (1) Make the K=5 self-consistency CLUTRR realized-FDR-vs-alpha diagonal the SINGLE primary calibration diagonal (the one the win-rate diagnostic actually validates at 0.482), powered on a SCALED CLUTRR corpus to a tighter certified grid, with a new SECOND-ORDER self-report check (the gate's own decoy_fdr_hat must track realized FDR) and a difficulty-graded diagnostic that retains sensitivity in the valid regime (repairing or honestly bounding the S1b blind spot). (2) EXECUTE the still-missing application hallucination-reduction headline on the already-built 24-doc legal/news/regulatory anchor: hallucinated-fact rate of decoy-gated neuro-symbolic extraction vs raw LLM generation (plus RAG/CoT neural baselines) under BOTH elicitations x ALL alpha, with WordNet->SUMO upper-ontology typing, atomic precision/recall + multi-hop deduction accuracy, and auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. (3) Reframe the Re-DocRED operational wedge with its TRUE scope (n_docs and recall ceiling stated at the claim), completed-or-dropped CoT/RAG comparators, a powered multi-hop hallucinated-conclusion comparison, and a NOVEL label-free regime-diagnostic that predicts -- before any gold -- which regime a scorer is in (overconfident -> gate helps; calibrated -> thresholding-is-enough). The novel contribution realized this iteration is the first internally-consistent, genre-faithful, label-free FDR gate at the text-to-logic admission boundary with a measured, self-detecting validity region and a quantified, auditable hallucination reduction on professionally written documents.",
      "rationale": "The reviewer feedback is unambiguous and maps one-to-one onto the iteration-3 mandate, so this iteration is about EXECUTION and INTERNAL CONSISTENCY, not new infrastructure. MAJOR #1 (the 'one coherent story' breaks: the headline diagonal was computed under VERBALIZED scoring, which the method's own diagnostic flags as anti-conservative at win-rate 0.103, while exchangeability was only shown separately under self-consistency) is fixed by P1 re-running the primary diagonal under the validated self-consistency elicitation and reconciling the two CLUTRR experiments into one diagonal, reporting decoy_fdr_hat vs realized vs alpha and the alpha=0.2 violation/discreteness mechanism honestly. MAJOR #2 (two claims contradicted by their own artifacts: the swap control is NOT flagged too-easy under self-consistency, diagnostic_sensitivity_ok=FALSE; and the spontaneous-error crux match's FULL-distribution test is REJECTED while only the tail was reported) is fixed by P1's S1b difficulty-graded diagnostic repair and full+tail crux reporting. MAJOR #4 (the target application is still not evaluated -- the goal's HARD requirement of a quantified hallucination reduction on ~3000-char professional documents with auditable trace-graphs is undone) is fixed by P2 executing the built 24-doc anchor end to end; budget is trivial (~$1.24 of $10 spent). MAJOR #3 (the Re-DocRED disconfirmation is real but far narrower than implied: n_docs_used=36 not 152, recall<=0.086, CoT/RAG all-null, multi-hop underpowered) is fixed by P3 reporting true scope, completing-or-dropping comparators, powering the multi-hop comparison, and recasting the operational value as a label-free regime-diagnostic. MINOR rigor/clarity items (elicitation-selection rationale, entrapment-agreement restricted to alpha*, BH multiplicity across all tests, figure-ready arrays marking the 1/k floor + CIs + gate-vs-plain-vs-swap) are baked into each experiment's required outputs. All three artifacts depend only on EXISTING iteration-1/2 artifacts, run fully in parallel, reuse the tested OpenRouter clients and gate code, and share the $10 cap with conservative per-experiment soft caps -- so the iteration converts the prepared anchors and the elicitation-dependence diagnosis into the three realized numbers the paper still needs, with the de-circularization (Generator!=Scorer, ROBUST) carried forward as SETTLED and not re-spent.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "P1 -- Produce the SINGLE primary CLUTRR calibration diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED, error-dense corpus, powered to a tight certified grid; add the second-order self-report check (the gate's own decoy_fdr_hat must track realized FDR); repair or honestly bound the S1b diagnostic blind spot with a difficulty-graded ladder measured under the SAME elicitation; report the spontaneous-error crux match in FULL (tail + full-distribution); and reconcile the iteration-2 verbalized and self-consistency CLUTRR experiments into ONE internally consistent diagonal narrative. This is the artifact that resolves reviewer MAJOR #1, MAJOR #2, and the rigor MINORs on the calibration claim.",
          "approach": "SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.",
          "depends_on": [
            { "id": "art_XZyKy6QuwxrO", "label": "dataset" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" },
            { "id": "art_Inu52CyA49Ys", "label": "elicitation" },
            { "id": "art_ikjFm_faAe0x", "label": "contrast" }
          ]
        },
        {
          "type": "experiment",
          "objective": "P2 (THE HEADLINE) -- Execute the goal's binding, still-undone requirement: a quantified, auditable hallucination reduction of decoy-gated neuro-symbolic extraction versus raw LLM generation (and the goal-required neural baselines RAG and chain-of-thought) on the genre-faithful 24-doc professional anchor (~3000-char legal/news/regulatory documents), under BOTH elicitations x ALL alpha, with WordNet->SUMO upper-ontology typing, atomic-fact precision/recall and multi-hop deduction accuracy, and human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. This resolves reviewer MAJOR #4 and delivers the goal's core deliverable on the genre it actually targets.",
          "approach": "On the 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean 2372 chars), run the full pipeline per the pipeline spec and the FDR-gate spec, reusing the tested OpenRouter client, gate code, and self-consistency elicitation from the dependencies. STAGE 1 EXTRACTION + TYPING: LLM over-generates typed first-order FACT/BRIDGE candidates (LINC/Logic-LM style); argument types grounded via the offline WordNet->SUMO recipe (Block C of the grounding/design dependency: WordNet hypernyms -> {PER,LOC,ORG,TIME,NUM,MISC} -> SUMO upper-ontology classes via WordNetMappings30), used ONLY for typing/decoy-constraint, never to filter. STAGE 2 DECOYS + SCORING + GATE: property-matched document-conditioned counterfactual decoys with non-entailment check -> ISOLATED provenance-blinded scoring under BOTH the VERBALIZED and the K=5 SELF-CONSISTENCY elicitations -> knockoff+ gate across ALL alpha {0.05,0.1,0.2,0.3,0.5} with deterministic entrapment corroboration (r=1). PRIMARY METRIC (goal hard requirement): hallucinated-fact rate -- the fraction of admitted atomic facts NOT entailed by the document (judged against gold facts + provenance char-spans, with a documented adjudication procedure for the silver genres) -- for decoy-gated extraction vs RAW LLM generation (no gate, all extracted facts admitted), reported PER GENRE, under BOTH elicitations x ALL alpha, with document-block bootstrap CIs. The regime-dependence MUST be explicit and never obscured: report that under logprob/verbalized the method can be worse-than-baseline at some alpha, and under self-consistency it is vacuous below the certified alpha -- present the full grid so a reader sees exactly the cell where the reduction is real. SECONDARY METRICS (goal requirements i and ii): atomic-fact extraction precision and recall vs gold; multi-hop deduction accuracy from admitted facts via the symbolic reasoner; and a matched-recall comparison of decoy-gated vs RAW LLM vs RAG (BM25) vs chain-of-thought (the goal-required purely-neural baselines) on the shared (head, relation, tail) triple schema. STAGE 3 REASONING + TRACE-GRAPHS (goal hard requirement): admitted facts/bridges populate SWI-Prolog (janus-swi) for multi-hop backward-chaining deduction; export human-auditable trace-graphs (JSON + Graphviz DOT) on AT LEAST a handful of documents spanning all three genres, where every leaf carries its provenance span, the decoy-competition certificate (W_i, T, alpha), and the entrapment certificate (FDP_hat, r). OPTIONAL ProbLog upgrade (per Part C of the grounding/design dependency, if time/budget permit): weighted clauses p_i::fact with p_i a calibrated, gate-consistent-shrinkage function of Z_i, producing probabilistic trace-graphs with per-node marginal probabilities -- deterministic backward-chaining is the REQUIRED baseline, ProbLog is the upgrade, so the headline numbers do not depend on it. Assert crisp comparisons on the legal (crisp-gold) slice and clearly-labeled relative comparisons on the silver slices. OUTPUT method_out.json (schema-valid) with: figure-ready per-genre hallucination-rate bars (gate vs raw vs RAG vs CoT) with CIs across alpha x both elicitations; atomic precision/recall and multi-hop accuracy tables; the certified-alpha grid with 1/k floors; entrapment numbers; and serialized example trace-graphs (with at least one rendered DOT per genre). Gradual scaling; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.",
          "depends_on": [
            { "id": "art_UBTwyePql8NQ", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" },
            { "id": "art_Cr6L9JpoewZi", "label": "grounding" },
            { "id": "art_Inu52CyA49Ys", "label": "elicitation" }
          ]
        },
        {
          "type": "experiment",
          "objective": "P3 -- Reframe and re-power the Re-DocRED operational wedge so the disconfirmation is reported PRECISELY (true number of documents used and the recall ceiling stated AT the point of claim), comparators are completed-or-dropped (no all-null baselines listed as participating), the multi-hop hallucinated-conclusion comparison is powered or explicitly labeled underpowered, and the operational contribution is recast as a NOVEL label-free REGIME-DIAGNOSTIC that predicts where decoy-gating adds value. This resolves reviewer MAJOR #3 and converts a narrow negative result into the paper's unifying operational insight.",
          "approach": "Build on the prior wedge experiment (reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it. SCOPE HONESTY: run on substantially more than the prior 36 scored documents (target the full 152 confirmatory Re-DocRED docs from the dependency anchor) and report the ACHIEVABLE recall ceiling explicitly at the claim ('at <=X% recall on N documents'); never imply 152 confirmatory while scoring fewer. COMPARATORS: bring chain-of-thought and BM25-RAG to a comparable matched-recall operating point on the shared triple schema; if either cannot reach the grid start (the prior run had CoT/RAG max recall 0.049/0.041 below the 0.05 grid start, all-null), REMOVE it from the wedge comparator list and say so -- do NOT list all-null baselines as participating. Keep the plain confidence-threshold gate as the load-bearing zero-label foil and labeled Mohri-Hashimoto conformal as the labeled reference (report its calibration-label count vs the method's zero labels). At the matched-recall operating point report precision, the precision-wedge delta(METHOD-PLAIN), and PR curves with document-block bootstrap (B>=2000) CIs and BH correction. POWER THE MULTI-HOP COMPARISON: forward-chain over more documents / deeper rules to raise the number of derived conclusions per system above a stated power target for the hallucinated-conclusion-rate comparison; if it remains underpowered, label it UNDERPOWERED explicitly with the conclusion count and CI width (the prior run rested on ~20-24 conclusions, CIs spanning [0.29,1.0]). REGIME-DIAGNOSTIC (the novel reframing, connecting to P1): using ONLY the label-free signals (tail-conditioned win-rate and the spontaneous-error CDF match, computed without gold), PREDICT which regime Re-DocRED's scorer is in (an already-calibrated logprob yes-token scorer -> 'thresholding-is-enough', gate redundant), then VALIDATE that prediction against the realized null wedge; pair this with P1's CLUTRR regime (overconfident verbalized/logprob tail -> gate adds value) to state and test the unifying principle 'the gate adds value only where the base elicitation is tail-overconfident, and is redundant where it is calibrated', reporting the diagnostic's predictive direction across both anchors. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally). Keep the alignment-error confound check from the prior run. OUTPUT method_out.json (schema-valid) with: figure-ready matched-recall PR arrays and the precision-wedge delta with CIs for ONLY the participating systems; multi-hop hallucination bars with explicit per-system conclusion counts and CIs (or an underpowered flag); the regime-diagnostic prediction-vs-realized panel; and a precisely-scoped operational verdict ('disconfirmed at <=X% recall on N docs; reframed as regime-diagnostic'). Log cumulative LLM cost after EVERY call; soft cap ~$2, HARD STOP at $10.",
          "depends_on": [
            { "id": "art_Jcudmkugg1qT", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_sHNuY68d4-Wh", "label": "extends" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" }
          ]
        }
      ],
      "expected_outcome": "After this iteration the project will hold an internally CONSISTENT and genre-faithful evidentiary core that directly dissolves all four reviewer MAJORs and meets the goal's binding requirement. (1) From P1: a SINGLE primary CLUTRR calibration diagonal computed under the diagnostic-validated K=5 self-consistency elicitation on a scaled, error-dense corpus, with realized FDR vs alpha and document-block-bootstrap CIs across a tighter CERTIFIED grid; the new second-order self-report check (decoy_fdr_hat vs realized vs alpha) reported at every alpha; the S1b diagnostic either REPAIRED via a difficulty-graded ladder (with a detectability-vs-difficulty curve) or honestly bounded as a fundamental limitation; the spontaneous-error crux reported in FULL (tail fail-to-reject AND full-distribution rejection, with decision-relevance justification or a re-tuned decoy family); the verbalized diagonal retained only as a documented discreteness/loose-target contrast with the alpha=0.2 violation surfaced; entrapment agreement restricted to alpha*; and BH multiplicity applied across all tests -- the calibration story is now coherent and the diagnostic gives the RIGHT signal for the headline. (2) From P2: the goal's headline application result -- a quantified, per-genre hallucination reduction of decoy-gated extraction vs raw LLM generation (and RAG/CoT) on ~3000-char professional legal/news/regulatory documents, reported under BOTH elicitations x ALL alpha so the regime-dependence is explicit, with atomic precision/recall, multi-hop deduction accuracy, WordNet->SUMO typing, and exported human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates (and optionally a ProbLog probabilistic upgrade) -- moving the headline off the CLUTRR/Re-DocRED proxies and onto the genre the goal targets. (3) From P3: a precisely-scoped Re-DocRED operational result (true n_docs and recall ceiling stated at the claim, comparators completed-or-dropped, multi-hop comparison powered or explicitly flagged underpowered) recast as a NOVEL label-free regime-diagnostic validated across both anchors. Together these turn the disconfirmed/confounded iteration-2 paper into a coherent contribution -- a label-free FDR knob at the text-to-logic admission boundary that is calibrated under the validated elicitation, self-detecting about its own validity region, redundant where the base scorer is calibrated, and delivering an auditable hallucination reduction on professional documents -- with all figure-ready arrays (diagonals with 1/k floor + CIs + gate-vs-plain-vs-swap, hallucination bars, regime panels, trace-graphs) in hand for the rewrite, and total LLM spend held well under the $10 cap.",
      "summary": "An execution iteration with three parallel, self-contained experiments that each land one reviewer MAJOR and depend only on existing artifacts. P1 re-runs the headline CLUTRR realized-FDR-vs-alpha diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED corpus, adds the decoy_fdr_hat second-order self-report check, repairs or bounds the S1b diagnostic blind spot with a difficulty-graded ladder, and reports the crux match in full -- reconciling the two CLUTRR experiments into one coherent diagonal (fixes MAJOR #1, #2, rigor MINORs). P2 executes the still-missing application headline on the 24-doc professional anchor: hallucinated-fact rate of decoy-gated extraction vs raw LLM (plus RAG/CoT), both elicitations x all alpha, with WordNet->SUMO typing, atomic precision/recall + multi-hop accuracy, and auditable trace-graphs (fixes MAJOR #4, the goal's hard requirement). P3 reframes the Re-DocRED wedge with true scope, completed-or-dropped comparators, a powered multi-hop comparison, and a novel label-free regime-diagnostic (fixes MAJOR #3). De-circularization is carried forward as SETTLED; BH multiplicity and document-block-bootstrap CIs are applied throughout; budget stays far under the $10 cap."
    }
  ]
}
```

### [9] TOOL RESULT — Write · 2026-06-16 08:34:39 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Consolidate Under the Validated Elicitation, Execute the Application Headline, and Reframe the Wedge as a Label-Free Regime-Diagnostic\",\n      \"objective\": \"Turn iteration-2's central finding -- that the gate's validity is ELICITATION-DEPENDENT -- into one internally consistent, genre-faithful, publishable story by executing three things the reviewers and the goal require but the current paper lacks. (1) Make the K=5 self-consistency CLUTRR realized-FDR-vs-alpha diagonal the SINGLE primary calibration diagonal (the one the win-rate diagnostic actually validates at 0.482), powered on a SCALED CLUTRR corpus to a tighter certified grid, with a new SECOND-ORDER self-report check (the gate's own decoy_fdr_hat must track realized FDR) and a difficulty-graded diagnostic that retains sensitivity in the valid regime (repairing or honestly bounding the S1b blind spot). (2) EXECUTE the still-missing application hallucination-reduction headline on the already-built 24-doc legal/news/regulatory anchor: hallucinated-fact rate of decoy-gated neuro-symbolic extraction vs raw LLM generation (plus RAG/CoT neural baselines) under BOTH elicitations x ALL alpha, with WordNet->SUMO upper-ontology typing, atomic precision/recall + multi-hop deduction accuracy, and auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. (3) Reframe the Re-DocRED operational wedge with its TRUE scope (n_docs and recall ceiling stated at the claim), completed-or-dropped CoT/RAG comparators, a powered multi-hop hallucinated-conclusion comparison, and a NOVEL label-free regime-diagnostic that predicts -- before any gold -- which regime a scorer is in (overconfident -> gate helps; calibrated -> thresholding-is-enough). The novel contribution realized this iteration is the first internally-consistent, genre-faithful, label-free FDR gate at the text-to-logic admission boundary with a measured, self-detecting validity region and a quantified, auditable hallucination reduction on professionally written documents.\",\n      \"rationale\": \"The reviewer feedback is unambiguous and maps one-to-one onto the iteration-3 mandate, so this iteration is about EXECUTION and INTERNAL CONSISTENCY, not new infrastructure. MAJOR #1 (the 'one coherent story' breaks: the headline diagonal was computed under VERBALIZED scoring, which the method's own diagnostic flags as anti-conservative at win-rate 0.103, while exchangeability was only shown separately under self-consistency) is fixed by P1 re-running the primary diagonal under the validated self-consistency elicitation and reconciling the two CLUTRR experiments into one diagonal, reporting decoy_fdr_hat vs realized vs alpha and the alpha=0.2 violation/discreteness mechanism honestly. MAJOR #2 (two claims contradicted by their own artifacts: the swap control is NOT flagged too-easy under self-consistency, diagnostic_sensitivity_ok=FALSE; and the spontaneous-error crux match's FULL-distribution test is REJECTED while only the tail was reported) is fixed by P1's S1b difficulty-graded diagnostic repair and full+tail crux reporting. MAJOR #4 (the target application is still not evaluated -- the goal's HARD requirement of a quantified hallucination reduction on ~3000-char professional documents with auditable trace-graphs is undone) is fixed by P2 executing the built 24-doc anchor end to end; budget is trivial (~$1.24 of $10 spent). MAJOR #3 (the Re-DocRED disconfirmation is real but far narrower than implied: n_docs_used=36 not 152, recall<=0.086, CoT/RAG all-null, multi-hop underpowered) is fixed by P3 reporting true scope, completing-or-dropping comparators, powering the multi-hop comparison, and recasting the operational value as a label-free regime-diagnostic. MINOR rigor/clarity items (elicitation-selection rationale, entrapment-agreement restricted to alpha*, BH multiplicity across all tests, figure-ready arrays marking the 1/k floor + CIs + gate-vs-plain-vs-swap) are baked into each experiment's required outputs. All three artifacts depend only on EXISTING iteration-1/2 artifacts, run fully in parallel, reuse the tested OpenRouter clients and gate code, and share the $10 cap with conservative per-experiment soft caps -- so the iteration converts the prepared anchors and the elicitation-dependence diagnosis into the three realized numbers the paper still needs, with the de-circularization (Generator!=Scorer, ROBUST) carried forward as SETTLED and not re-spent.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"P1 -- Produce the SINGLE primary CLUTRR calibration diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED, error-dense corpus, powered to a tight certified grid; add the second-order self-report check (the gate's own decoy_fdr_hat must track realized FDR); repair or honestly bound the S1b diagnostic blind spot with a difficulty-graded ladder measured under the SAME elicitation; report the spontaneous-error crux match in FULL (tail + full-distribution); and reconcile the iteration-2 verbalized and self-consistency CLUTRR experiments into ONE internally consistent diagonal narrative. This is the artifact that resolves reviewer MAJOR #1, MAJOR #2, and the rigor MINORs on the calibration claim.\",\n          \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",\n          \"depends_on\": [\n            { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },\n            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" },\n            { \"id\": \"art_ikjFm_faAe0x\", \"label\": \"contrast\" }\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"P2 (THE HEADLINE) -- Execute the goal's binding, still-undone requirement: a quantified, auditable hallucination reduction of decoy-gated neuro-symbolic extraction versus raw LLM generation (and the goal-required neural baselines RAG and chain-of-thought) on the genre-faithful 24-doc professional anchor (~3000-char legal/news/regulatory documents), under BOTH elicitations x ALL alpha, with WordNet->SUMO upper-ontology typing, atomic-fact precision/recall and multi-hop deduction accuracy, and human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. This resolves reviewer MAJOR #4 and delivers the goal's core deliverable on the genre it actually targets.\",\n          \"approach\": \"On the 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean 2372 chars), run the full pipeline per the pipeline spec and the FDR-gate spec, reusing the tested OpenRouter client, gate code, and self-consistency elicitation from the dependencies. STAGE 1 EXTRACTION + TYPING: LLM over-generates typed first-order FACT/BRIDGE candidates (LINC/Logic-LM style); argument types grounded via the offline WordNet->SUMO recipe (Block C of the grounding/design dependency: WordNet hypernyms -> {PER,LOC,ORG,TIME,NUM,MISC} -> SUMO upper-ontology classes via WordNetMappings30), used ONLY for typing/decoy-constraint, never to filter. STAGE 2 DECOYS + SCORING + GATE: property-matched document-conditioned counterfactual decoys with non-entailment check -> ISOLATED provenance-blinded scoring under BOTH the VERBALIZED and the K=5 SELF-CONSISTENCY elicitations -> knockoff+ gate across ALL alpha {0.05,0.1,0.2,0.3,0.5} with deterministic entrapment corroboration (r=1). PRIMARY METRIC (goal hard requirement): hallucinated-fact rate -- the fraction of admitted atomic facts NOT entailed by the document (judged against gold facts + provenance char-spans, with a documented adjudication procedure for the silver genres) -- for decoy-gated extraction vs RAW LLM generation (no gate, all extracted facts admitted), reported PER GENRE, under BOTH elicitations x ALL alpha, with document-block bootstrap CIs. The regime-dependence MUST be explicit and never obscured: report that under logprob/verbalized the method can be worse-than-baseline at some alpha, and under self-consistency it is vacuous below the certified alpha -- present the full grid so a reader sees exactly the cell where the reduction is real. SECONDARY METRICS (goal requirements i and ii): atomic-fact extraction precision and recall vs gold; multi-hop deduction accuracy from admitted facts via the symbolic reasoner; and a matched-recall comparison of decoy-gated vs RAW LLM vs RAG (BM25) vs chain-of-thought (the goal-required purely-neural baselines) on the shared (head, relation, tail) triple schema. STAGE 3 REASONING + TRACE-GRAPHS (goal hard requirement): admitted facts/bridges populate SWI-Prolog (janus-swi) for multi-hop backward-chaining deduction; export human-auditable trace-graphs (JSON + Graphviz DOT) on AT LEAST a handful of documents spanning all three genres, where every leaf carries its provenance span, the decoy-competition certificate (W_i, T, alpha), and the entrapment certificate (FDP_hat, r). OPTIONAL ProbLog upgrade (per Part C of the grounding/design dependency, if time/budget permit): weighted clauses p_i::fact with p_i a calibrated, gate-consistent-shrinkage function of Z_i, producing probabilistic trace-graphs with per-node marginal probabilities -- deterministic backward-chaining is the REQUIRED baseline, ProbLog is the upgrade, so the headline numbers do not depend on it. Assert crisp comparisons on the legal (crisp-gold) slice and clearly-labeled relative comparisons on the silver slices. OUTPUT method_out.json (schema-valid) with: figure-ready per-genre hallucination-rate bars (gate vs raw vs RAG vs CoT) with CIs across alpha x both elicitations; atomic precision/recall and multi-hop accuracy tables; the certified-alpha grid with 1/k floors; entrapment numbers; and serialized example trace-graphs (with at least one rendered DOT per genre). Gradual scaling; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",\n          \"depends_on\": [\n            { \"id\": \"art_UBTwyePql8NQ\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },\n            { \"id\": \"art_Cr6L9JpoewZi\", \"label\": \"grounding\" },\n            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" }\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"P3 -- Reframe and re-power the Re-DocRED operational wedge so the disconfirmation is reported PRECISELY (true number of documents used and the recall ceiling stated AT the point of claim), comparators are completed-or-dropped (no all-null baselines listed as participating), the multi-hop hallucinated-conclusion comparison is powered or explicitly labeled underpowered, and the operational contribution is recast as a NOVEL label-free REGIME-DIAGNOSTIC that predicts where decoy-gating adds value. This resolves reviewer MAJOR #3 and converts a narrow negative result into the paper's unifying operational insight.\",\n          \"approach\": \"Build on the prior wedge experiment (reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it. SCOPE HONESTY: run on substantially more than the prior 36 scored documents (target the full 152 confirmatory Re-DocRED docs from the dependency anchor) and report the ACHIEVABLE recall ceiling explicitly at the claim ('at <=X% recall on N documents'); never imply 152 confirmatory while scoring fewer. COMPARATORS: bring chain-of-thought and BM25-RAG to a comparable matched-recall operating point on the shared triple schema; if either cannot reach the grid start (the prior run had CoT/RAG max recall 0.049/0.041 below the 0.05 grid start, all-null), REMOVE it from the wedge comparator list and say so -- do NOT list all-null baselines as participating. Keep the plain confidence-threshold gate as the load-bearing zero-label foil and labeled Mohri-Hashimoto conformal as the labeled reference (report its calibration-label count vs the method's zero labels). At the matched-recall operating point report precision, the precision-wedge delta(METHOD-PLAIN), and PR curves with document-block bootstrap (B>=2000) CIs and BH correction. POWER THE MULTI-HOP COMPARISON: forward-chain over more documents / deeper rules to raise the number of derived conclusions per system above a stated power target for the hallucinated-conclusion-rate comparison; if it remains underpowered, label it UNDERPOWERED explicitly with the conclusion count and CI width (the prior run rested on ~20-24 conclusions, CIs spanning [0.29,1.0]). REGIME-DIAGNOSTIC (the novel reframing, connecting to P1): using ONLY the label-free signals (tail-conditioned win-rate and the spontaneous-error CDF match, computed without gold), PREDICT which regime Re-DocRED's scorer is in (an already-calibrated logprob yes-token scorer -> 'thresholding-is-enough', gate redundant), then VALIDATE that prediction against the realized null wedge; pair this with P1's CLUTRR regime (overconfident verbalized/logprob tail -> gate adds value) to state and test the unifying principle 'the gate adds value only where the base elicitation is tail-overconfident, and is redundant where it is calibrated', reporting the diagnostic's predictive direction across both anchors. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally). Keep the alignment-error confound check from the prior run. OUTPUT method_out.json (schema-valid) with: figure-ready matched-recall PR arrays and the precision-wedge delta with CIs for ONLY the participating systems; multi-hop hallucination bars with explicit per-system conclusion counts and CIs (or an underpowered flag); the regime-diagnostic prediction-vs-realized panel; and a precisely-scoped operational verdict ('disconfirmed at <=X% recall on N docs; reframed as regime-diagnostic'). Log cumulative LLM cost after EVERY call; soft cap ~$2, HARD STOP at $10.\",\n          \"depends_on\": [\n            { \"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_sHNuY68d4-Wh\", \"label\": \"extends\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }\n          ]\n        }\n      ],\n      \"expected_outcome\": \"After this iteration the project will hold an internally CONSISTENT and genre-faithful evidentiary core that directly dissolves all four reviewer MAJORs and meets the goal's binding requirement. (1) From P1: a SINGLE primary CLUTRR calibration diagonal computed under the diagnostic-validated K=5 self-consistency elicitation on a scaled, error-dense corpus, with realized FDR vs alpha and document-block-bootstrap CIs across a tighter CERTIFIED grid; the new second-order self-report check (decoy_fdr_hat vs realized vs alpha) reported at every alpha; the S1b diagnostic either REPAIRED via a difficulty-graded ladder (with a detectability-vs-difficulty curve) or honestly bounded as a fundamental limitation; the spontaneous-error crux reported in FULL (tail fail-to-reject AND full-distribution rejection, with decision-relevance justification or a re-tuned decoy family); the verbalized diagonal retained only as a documented discreteness/loose-target contrast with the alpha=0.2 violation surfaced; entrapment agreement restricted to alpha*; and BH multiplicity applied across all tests -- the calibration story is now coherent and the diagnostic gives the RIGHT signal for the headline. (2) From P2: the goal's headline application result -- a quantified, per-genre hallucination reduction of decoy-gated extraction vs raw LLM generation (and RAG/CoT) on ~3000-char professional legal/news/regulatory documents, reported under BOTH elicitations x ALL alpha so the regime-dependence is explicit, with atomic precision/recall, multi-hop deduction accuracy, WordNet->SUMO typing, and exported human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates (and optionally a ProbLog probabilistic upgrade) -- moving the headline off the CLUTRR/Re-DocRED proxies and onto the genre the goal targets. (3) From P3: a precisely-scoped Re-DocRED operational result (true n_docs and recall ceiling stated at the claim, comparators completed-or-dropped, multi-hop comparison powered or explicitly flagged underpowered) recast as a NOVEL label-free regime-diagnostic validated across both anchors. Together these turn the disconfirmed/confounded iteration-2 paper into a coherent contribution -- a label-free FDR knob at the text-to-logic admission boundary that is calibrated under the validated elicitation, self-detecting about its own validity region, redundant where the base scorer is calibrated, and delivering an auditable hallucination reduction on professional documents -- with all figure-ready arrays (diagonals with 1/k floor + CIs + gate-vs-plain-vs-swap, hallucination bars, regime panels, trace-graphs) in hand for the rewrite, and total LLM spend held well under the $10 cap.\",\n      \"summary\": \"An execution iteration with three parallel, self-contained experiments that each land one reviewer MAJOR and depend only on existing artifacts. P1 re-runs the headline CLUTRR realized-FDR-vs-alpha diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED corpus, adds the decoy_fdr_hat second-order self-report check, repairs or bounds the S1b diagnostic blind spot with a difficulty-graded ladder, and reports the crux match in full -- reconciling the two CLUTRR experiments into one coherent diagonal (fixes MAJOR #1, #2, rigor MINORs). P2 executes the still-missing application headline on the 24-doc professional anchor: hallucinated-fact rate of decoy-gated extraction vs raw LLM (plus RAG/CoT), both elicitations x all alpha, with WordNet->SUMO typing, atomic precision/recall + multi-hop accuracy, and auditable trace-graphs (fixes MAJOR #4, the goal's hard requirement). P3 reframes the Re-DocRED wedge with true scope, completed-or-dropped comparators, a powered multi-hop comparison, and a novel label-free regime-diagnostic (fixes MAJOR #3). De-circularization is carried forward as SETTLED; BH multiplicity and document-block-bootstrap CIs are applied throughout; budget stays far under the $10 cap.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [10] ASSISTANT · 2026-06-16 08:34:45 UTC

```
Let me verify the output is valid JSON against the expected structure.
```

### [11] TOOL CALL — Bash · 2026-06-16 08:34:45 UTC

```
Validate JSON structure and constraints:
python3 -c "
import json
d=json.load(open('.terminal_claude_agent_struct_out.json'))
s=d['strategies']
print('n_strategies:',len(s))
st=s[0]
print('title ok:',bool(st['title']))
for k in ['objective','rationale','expected_outcome','summary']: assert st[k], k
ads=st['artifact_directions']
print('n_artifacts:',len(ads),'(limit 7)')
assert len(ads)<=7
for i,a in enumerate(ads):
    assert a['type'] in {'experiment','research','proof','evaluation','dataset'}, a['type']
    assert a['objective'] and a['approach']
    deps=a.get('depends_on',[])
    print(f'  art{i+1}: type={a[\"type\"]} ndeps={len(deps)} deps='+','.join(x['id']+':'+x['label'] for x in deps))
    for x in deps: assert x['id'] and x['label']
print('VALID')
"
```

### [12] TOOL RESULT — Bash · 2026-06-16 08:34:45 UTC

```
{"stdout": "n_strategies: 1\ntitle ok: True\nn_artifacts: 3 (limit 7)\n  art1: type=experiment ndeps=4 deps=art_XZyKy6QuwxrO:dataset,art_SLUbUUr6Ul98:methodology,art_Inu52CyA49Ys:elicitation,art_ikjFm_faAe0x:contrast\n  art2: type=experiment ndeps=5 deps=art_UBTwyePql8NQ:dataset,art_K6AE23HoGqe6:pipeline,art_SLUbUUr6Ul98:methodology,art_Cr6L9JpoewZi:grounding,art_Inu52CyA49Ys:elicitation\n  art3: type=experiment ndeps=4 deps=art_Jcudmkugg1qT:dataset,art_K6AE23HoGqe6:pipeline,art_sHNuY68d4-Wh:extends,art_SLUbUUr6Ul98:methodology\nVALID", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] ASSISTANT · 2026-06-16 08:35:01 UTC

```
The strategy is written and validated. 

## Summary

I generated **1 focused execution strategy** with **3 parallel experiments**, each landing a reviewer MAJOR and depending only on existing artifacts. This is iteration 3's clear mandate: not re-building, but consolidating under the validated elicitation, executing the missing application headline, and reframing the wedge.

**The strategy: "Consolidate Under the Validated Elicitation, Execute the Application Headline, and Reframe the Wedge as a Label-Free Regime-Diagnostic"**

| Artifact | Fixes | What it does |
|---|---|---|
| **P1 — CLUTRR self-consistency diagonal** (exp) | MAJOR #1, #2, rigor MINORs | Re-runs the headline realized-FDR-vs-α diagonal under the *diagnostic-validated* K=5 self-consistency elicitation on a **scaled** corpus; adds the `decoy_fdr_hat` second-order self-report check; repairs/bounds the S1b diagnostic blind spot with a difficulty-graded ladder; reports the crux match in **full** (tail + rejected full-distribution); keeps verbalized only as a documented discreteness contrast with the α=0.2 violation surfaced. |
| **P2 — Application headline** (exp) | MAJOR #4 (goal's hard requirement) | Executes the built 24-doc legal/news/regulatory anchor: hallucinated-fact rate of decoy-gated extraction vs raw LLM (+RAG/CoT), **both elicitations × all α**, WordNet→SUMO typing, atomic precision/recall + multi-hop accuracy, and **auditable trace-graphs** with per-leaf provenance+decoy+entrapment certificates. |
| **P3 — Re-DocRED wedge reframe** (exp) | MAJOR #3 | States true scope (n_docs, recall ceiling) at the claim; completes-or-drops CoT/RAG; powers (or flags) the multi-hop comparison; recasts the operational value as a **novel label-free regime-diagnostic** validated across both anchors. |

**Key design choices:**
- All three run in parallel, depend only on existing iteration-1/2 artifacts, and reuse tested clients/gate code — so the powered diagonal lands *this* iteration (P1 scales CLUTRR via the regenerable `data.py` itself).
- De-circularization (Generator≠Scorer, ROBUST) is carried forward as **settled** — no new budget.
- BH multiplicity and document-block-bootstrap CIs throughout; figure-ready arrays (1/k floor, CI bands, gate-vs-plain-vs-swap) baked into each output to address the figure MINOR downstream.
- Budget stays far under the $10 cap (~$1.24 spent so far; soft caps ~$3/$3/$2).

I kept it to 3 deep experiments rather than padding toward the 7-artifact limit — depth over breadth, with each experiment directly preempting a reviewer objection.
```

### [14] SYSTEM-USER prompt · 2026-06-16 08:35:03 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'experiment_iter3_dir1' (experiment): dependency 'art_Inu52CyA49Ys' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir1' (experiment): dependency 'art_ikjFm_faAe0x' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir2' (experiment): dependency 'art_Inu52CyA49Ys' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir3' (experiment): dependency 'art_sHNuY68d4-Wh' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})

INSUFFICIENT VALID ARTIFACTS:
  Required: at least 1 valid artifacts
  Found: 0 valid out of 3 total
  Artifacts with invalid types, duplicate IDs, or invalid dependencies don't count as valid.

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []
2. Ensure at least 1 artifacts are fully valid (correct types, no ID conflicts, valid dependencies)

Output the corrected JSON with the fixed strategies.
</task>
```

### [15] ASSISTANT · 2026-06-16 08:35:30 UTC

```
The fix is clear: experiments can only depend on `research` and `dataset` artifacts, not other experiments. I'll remove the experiment-type dependencies (`art_Inu52CyA49Ys`, `art_ikjFm_faAe0x`, `art_sHNuY68d4-Wh`) and keep only the valid dataset/research deps. The prior experiments' code/results remain accessible via the run tree, so I'll adjust the approach wording accordingly.
```

### [16] TOOL CALL — Edit · 2026-06-16 08:35:30 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            { "id": "art_XZyKy6QuwxrO", "label": "dataset" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" },
            { "id": "art_Inu52CyA49Ys", "label": "elicitation" },
            { "id": "art_ikjFm_faAe0x", "label": "contrast" }
          ]
NEW:           "depends_on": [
            { "id": "art_XZyKy6QuwxrO", "label": "dataset" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" }
          ]
```

### [17] TOOL RESULT — Edit · 2026-06-16 08:35:30 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },\n            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" },\n            { \"id\": \"art_ikjFm_faAe0x\", \"label\": \"contrast\" }\n          ]", "newString": "          \"depends_on\": [\n            { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }\n          ]", "originalFile": null, "structuredPatch": [{"oldStart": 11, "oldLines": 9, "newStart": 11, "newLines": 7, "lines": ["           \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "           \"depends_on\": [", "             { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },", "-            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },", "-            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" },", "-            { \"id\": \"art_ikjFm_faAe0x\", \"label\": \"contrast\" }", "+            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }", "           ]", "         },", "         {"]}], "userModified": false, "replaceAll": false}
```

### [18] TOOL CALL — Edit · 2026-06-16 08:35:38 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            { "id": "art_UBTwyePql8NQ", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" },
            { "id": "art_Cr6L9JpoewZi", "label": "grounding" },
            { "id": "art_Inu52CyA49Ys", "label": "elicitation" }
          ]
NEW:           "depends_on": [
            { "id": "art_UBTwyePql8NQ", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" },
            { "id": "art_Cr6L9JpoewZi", "label": "grounding" }
          ]
```

### [19] TOOL RESULT — Edit · 2026-06-16 08:35:38 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            { \"id\": \"art_UBTwyePql8NQ\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },\n            { \"id\": \"art_Cr6L9JpoewZi\", \"label\": \"grounding\" },\n            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" }\n          ]", "newString": "          \"depends_on\": [\n            { \"id\": \"art_UBTwyePql8NQ\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },\n            { \"id\": \"art_Cr6L9JpoewZi\", \"label\": \"grounding\" }\n          ]", "originalFile": null, "structuredPatch": [{"oldStart": 22, "oldLines": 8, "newStart": 22, "newLines": 7, "lines": ["             { \"id\": \"art_UBTwyePql8NQ\", \"label\": \"dataset\" },", "             { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },", "             { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" },", "-            { \"id\": \"art_Cr6L9JpoewZi\", \"label\": \"grounding\" },", "-            { \"id\": \"art_Inu52CyA49Ys\", \"label\": \"elicitation\" }", "+            { \"id\": \"art_Cr6L9JpoewZi\", \"label\": \"grounding\" }", "           ]", "         },", "         {"]}], "userModified": false, "replaceAll": false}
```

### [20] TOOL CALL — Edit · 2026-06-16 08:35:43 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            { "id": "art_Jcudmkugg1qT", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_sHNuY68d4-Wh", "label": "extends" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" }
          ]
NEW:           "depends_on": [
            { "id": "art_Jcudmkugg1qT", "label": "dataset" },
            { "id": "art_K6AE23HoGqe6", "label": "pipeline" },
            { "id": "art_SLUbUUr6Ul98", "label": "methodology" }
          ]
```

### [21] TOOL RESULT — Edit · 2026-06-16 08:35:43 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            { \"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_sHNuY68d4-Wh\", \"label\": \"extends\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }\n          ]", "newString": "          \"depends_on\": [\n            { \"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\" },\n            { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },\n            { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }\n          ]", "originalFile": null, "structuredPatch": [{"oldStart": 32, "oldLines": 7, "newStart": 32, "newLines": 6, "lines": ["           \"depends_on\": [", "             { \"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\" },", "             { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },", "-            { \"id\": \"art_sHNuY68d4-Wh\", \"label\": \"extends\" },", "             { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }", "           ]", "         }"]}], "userModified": false, "replaceAll": false}
```

### [22] ASSISTANT · 2026-06-16 08:36:03 UTC

```
Now I'll fix the approach wording that referenced reusing code "from the dependencies," since the prior experiments are no longer formal deps (they remain accessible via the run tree).
```

### [23] TOOL CALL — Edit · 2026-06-16 08:36:03 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD: re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction
NEW: re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (re-use the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the iteration-2 CLUTRR experiment workspaces art_ikjFm_faAe0x and art_Inu52CyA49Ys, read from the persisted run tree, and implement the gate per the methodology spec dependency): over-generation extraction
```

### [24] TOOL RESULT — Edit · 2026-06-16 08:36:03 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction", "newString": "re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (re-use the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the iteration-2 CLUTRR experiment workspaces art_ikjFm_faAe0x and art_Inu52CyA49Ys, read from the persisted run tree, and implement the gate per the methodology spec dependency): over-generation extraction", "originalFile": null, "structuredPatch": [{"oldStart": 8, "oldLines": 7, "newStart": 8, "newLines": 7, "lines": ["         {", "           \"type\": \"experiment\",", "           \"objective\": \"P1 -- Produce the SINGLE primary CLUTRR calibration diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED, error-dense corpus, powered to a tight certified grid; add the second-order self-report check (the gate's own decoy_fdr_hat must track realized FDR); repair or honestly bound the S1b diagnostic blind spot with a difficulty-graded ladder measured under the SAME elicitation; report the spontaneous-error crux match in FULL (tail + full-distribution); and reconcile the iteration-2 verbalized and self-consistency CLUTRR experiments into ONE internally consistent diagonal narrative. This is the artifact that resolves reviewer MAJOR #1, MAJOR #2, and the rigor MINORs on the calibration claim.\",", "-          \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (reuse the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the dependencies): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "+          \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (re-use the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the iteration-2 CLUTRR experiment workspaces art_ikjFm_faAe0x and art_Inu52CyA49Ys, read from the persisted run tree, and implement the gate per the methodology spec dependency): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "           \"depends_on\": [", "             { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },", "             { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }"]}], "userModified": false, "replaceAll": false}
```

### [25] TOOL CALL — Edit · 2026-06-16 08:36:09 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD: Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget).
NEW: Carry forward the Generator!=Scorer de-circularization from the iteration-2 mechanism-study experiment (art_Inu52CyA49Ys, read from the run tree) as SETTLED (no new budget).
```

### [26] TOOL RESULT — Edit · 2026-06-16 08:36:09 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget).", "newString": "Carry forward the Generator!=Scorer de-circularization from the iteration-2 mechanism-study experiment (art_Inu52CyA49Ys, read from the run tree) as SETTLED (no new budget).", "originalFile": null, "structuredPatch": [{"oldStart": 8, "oldLines": 7, "newStart": 8, "newLines": 7, "lines": ["         {", "           \"type\": \"experiment\",", "           \"objective\": \"P1 -- Produce the SINGLE primary CLUTRR calibration diagonal under the diagnostic-VALIDATED K=5 self-consistency elicitation on a SCALED, error-dense corpus, powered to a tight certified grid; add the second-order self-report check (the gate's own decoy_fdr_hat must track realized FDR); repair or honestly bound the S1b diagnostic blind spot with a difficulty-graded ladder measured under the SAME elicitation; report the spontaneous-error crux match in FULL (tail + full-distribution); and reconcile the iteration-2 verbalized and self-consistency CLUTRR experiments into ONE internally consistent diagonal narrative. This is the artifact that resolves reviewer MAJOR #1, MAJOR #2, and the rigor MINORs on the calibration claim.\",", "-          \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (re-use the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the iteration-2 CLUTRR experiment workspaces art_ikjFm_faAe0x and art_Inu52CyA49Ys, read from the persisted run tree, and implement the gate per the methodology spec dependency): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the dependency as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "+          \"approach\": \"SCALE THE CORPUS: regenerate CLUTRR via the dependency's regenerable data.py with substantially more documents (target ~500-800 stories) and oversampled HARD long-chain large-k splits (k>=6) to densify genuine multi-hop errors AND raise admission counts; re-verify crisp-gold integrity (proof_state-derived atomic + multi_hop facts, canonical simple-path constraints) exactly as the existing anchor does. PIPELINE (re-use the tested async cached cost-capped OpenRouter client and knockoff+ gate code from the iteration-2 CLUTRR experiment workspaces art_ikjFm_faAe0x and art_Inu52CyA49Ys, read from the persisted run tree, and implement the gate per the methodology spec dependency): over-generation extraction (T=0.7, multiple samples unioned) -> property-matched document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination) -> ISOLATED, provenance-blinded, order-randomized scoring under K=5 SELF-CONSISTENCY as the HEADLINE elicitation, with document-prefix prompt caching. Compute the diagonal with the canonical statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i) and the Barber-Candes +1 knockoff+ threshold T=min{t:(1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for the atomic and multi-hop bridge families; sweep alpha in {0.05,0.1,0.2,0.3,0.5}; report realized corpus-aggregate FDR vs crisp gold with document-block bootstrap (B>=2000) percentile CIs -- this IS the primary diagonal. ALSO compute the VERBALIZED diagonal on the SAME scaled data as a DOCUMENTED CONTRAST, and quantify the discreteness/loose-target artifact (state explicitly that under verbalized the alpha=0.2 target is VIOLATED, realized 0.214>0.2, and decoy_fdr_hat undershoots realized). SECOND-ORDER SELF-REPORT CHECK (new, per reviewer MAJOR #1): at every alpha report a triple (target alpha, gate internal estimate decoy_fdr_hat, realized FDR vs gold); pre-register that the gate's self-report is DISCONFIRMED at any alpha where decoy_fdr_hat is anti-conservative relative to realized beyond tolerance tau, even when realized happens to land below alpha. POWER: demonstrate, UNDER self-consistency, the certified grid -- each reported alpha must have >=1/alpha admissions AND >=N_false_min=40 genuine false admissions among reals; report the reachable alpha floor honestly and drop any alpha below it as a precondition (NEVER 'confirmed by conservatism'); if 190->scaled is still too coarse, scale further or declare the floor. S1b DIAGNOSTIC REPAIR (per reviewer MAJOR #2a): inject a difficulty-graded spike-in / entrapment LADDER at KNOWN anti-conservative difficulties (random type-matched swaps at the easy end, graded-plausibility counterfactuals toward the hard end) and measure, under the SAME self-consistency elicitation, whether the tail-conditioned win-rate / swap-control diagnostic recovers the ability to flag the known-too-easy items; if it does, S1b is REPAIRED (report the detectability-vs-difficulty curve); if it does not, report the win-rate/swap diagnostic's loss of sensitivity in the valid regime as a FUNDAMENTAL LIMITATION and explicitly down-scope the 'tells you when to trust the gate' claim. CRUX MATCH IN FULL (per reviewer MAJOR #2b): report BOTH the admission-tail two-sample tests (top-25%/50% KS, fail-to-reject) AND the FULL-distribution tests (KS/MW/AD/permutation, currently rejected, verdict decoys_too_easy), with figure-ready overlaid CDFs (counterfactual decoy vs genuine spontaneous error vs true positive); then EITHER re-tune the counterfactual-decoy family toward the full spontaneous-error distribution OR justify, on stated decision-theoretic grounds, why only the admission tail (above-cutoff pairs are the only pairs the gate acts on) is decision-relevant. Independent deterministic entrapment corroboration at alpha* (combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), r=1) with the agreement claim RESTRICTED to alpha* and the alpha=0.5 divergence reported honestly. State the explicit elicitation-SELECTION criterion (why self-consistency hosts the headline; note verbalized AUC 0.861 vs DINCO 0.871). Carry forward the Generator!=Scorer de-circularization from the iteration-2 mechanism-study experiment (art_Inu52CyA49Ys, read from the run tree) as SETTLED (no new budget). Apply a BH multiplicity correction across ALL validation tests. OUTPUT method_out.json (schema-valid) with: per-family alpha-vs-realized-FDR diagonal arrays (figure-ready, marking the 1/k floor, bootstrap CI bands, and the gate-vs-plain-vs-swap distinction), the decoy_fdr_hat overlay per alpha, the power/populability table, the S1b difficulty-ladder detectability curve, the crux CDFs (tail + full with all four test p-values), entrapment estimators, and the single primary-disconfirmation verdict under self-consistency. Gradual scaling mini->full; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "           \"depends_on\": [", "             { \"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\" },", "             { \"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\" }"]}], "userModified": false, "replaceAll": false}
```

### [27] TOOL CALL — Edit · 2026-06-16 08:36:15 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD: run the full pipeline per the pipeline spec and the FDR-gate spec, reusing the tested OpenRouter client, gate code, and self-consistency elicitation from the dependencies. STAGE 1 EXTRACTION + TYPING:
NEW: run the full pipeline per the pipeline spec and the FDR-gate spec dependencies, re-using the tested OpenRouter client, gate code, and K=5 self-consistency elicitation from the iteration-2 experiment workspaces (art_Inu52CyA49Ys, art_sHNuY68d4-Wh) read from the persisted run tree. STAGE 1 EXTRACTION + TYPING:
```

### [28] TOOL RESULT — Edit · 2026-06-16 08:36:15 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "run the full pipeline per the pipeline spec and the FDR-gate spec, reusing the tested OpenRouter client, gate code, and self-consistency elicitation from the dependencies. STAGE 1 EXTRACTION + TYPING:", "newString": "run the full pipeline per the pipeline spec and the FDR-gate spec dependencies, re-using the tested OpenRouter client, gate code, and K=5 self-consistency elicitation from the iteration-2 experiment workspaces (art_Inu52CyA49Ys, art_sHNuY68d4-Wh) read from the persisted run tree. STAGE 1 EXTRACTION + TYPING:", "originalFile": null, "structuredPatch": [{"oldStart": 17, "oldLines": 7, "newStart": 17, "newLines": 7, "lines": ["         {", "           \"type\": \"experiment\",", "           \"objective\": \"P2 (THE HEADLINE) -- Execute the goal's binding, still-undone requirement: a quantified, auditable hallucination reduction of decoy-gated neuro-symbolic extraction versus raw LLM generation (and the goal-required neural baselines RAG and chain-of-thought) on the genre-faithful 24-doc professional anchor (~3000-char legal/news/regulatory documents), under BOTH elicitations x ALL alpha, with WordNet->SUMO upper-ontology typing, atomic-fact precision/recall and multi-hop deduction accuracy, and human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. This resolves reviewer MAJOR #4 and delivers the goal's core deliverable on the genre it actually targets.\",", "-          \"approach\": \"On the 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean 2372 chars), run the full pipeline per the pipeline spec and the FDR-gate spec, reusing the tested OpenRouter client, gate code, and self-consistency elicitation from the dependencies. STAGE 1 EXTRACTION + TYPING: LLM over-generates typed first-order FACT/BRIDGE candidates (LINC/Logic-LM style); argument types grounded via the offline WordNet->SUMO recipe (Block C of the grounding/design dependency: WordNet hypernyms -> {PER,LOC,ORG,TIME,NUM,MISC} -> SUMO upper-ontology classes via WordNetMappings30), used ONLY for typing/decoy-constraint, never to filter. STAGE 2 DECOYS + SCORING + GATE: property-matched document-conditioned counterfactual decoys with non-entailment check -> ISOLATED provenance-blinded scoring under BOTH the VERBALIZED and the K=5 SELF-CONSISTENCY elicitations -> knockoff+ gate across ALL alpha {0.05,0.1,0.2,0.3,0.5} with deterministic entrapment corroboration (r=1). PRIMARY METRIC (goal hard requirement): hallucinated-fact rate -- the fraction of admitted atomic facts NOT entailed by the document (judged against gold facts + provenance char-spans, with a documented adjudication procedure for the silver genres) -- for decoy-gated extraction vs RAW LLM generation (no gate, all extracted facts admitted), reported PER GENRE, under BOTH elicitations x ALL alpha, with document-block bootstrap CIs. The regime-dependence MUST be explicit and never obscured: report that under logprob/verbalized the method can be worse-than-baseline at some alpha, and under self-consistency it is vacuous below the certified alpha -- present the full grid so a reader sees exactly the cell where the reduction is real. SECONDARY METRICS (goal requirements i and ii): atomic-fact extraction precision and recall vs gold; multi-hop deduction accuracy from admitted facts via the symbolic reasoner; and a matched-recall comparison of decoy-gated vs RAW LLM vs RAG (BM25) vs chain-of-thought (the goal-required purely-neural baselines) on the shared (head, relation, tail) triple schema. STAGE 3 REASONING + TRACE-GRAPHS (goal hard requirement): admitted facts/bridges populate SWI-Prolog (janus-swi) for multi-hop backward-chaining deduction; export human-auditable trace-graphs (JSON + Graphviz DOT) on AT LEAST a handful of documents spanning all three genres, where every leaf carries its provenance span, the decoy-competition certificate (W_i, T, alpha), and the entrapment certificate (FDP_hat, r). OPTIONAL ProbLog upgrade (per Part C of the grounding/design dependency, if time/budget permit): weighted clauses p_i::fact with p_i a calibrated, gate-consistent-shrinkage function of Z_i, producing probabilistic trace-graphs with per-node marginal probabilities -- deterministic backward-chaining is the REQUIRED baseline, ProbLog is the upgrade, so the headline numbers do not depend on it. Assert crisp comparisons on the legal (crisp-gold) slice and clearly-labeled relative comparisons on the silver slices. OUTPUT method_out.json (schema-valid) with: figure-ready per-genre hallucination-rate bars (gate vs raw vs RAG vs CoT) with CIs across alpha x both elicitations; atomic precision/recall and multi-hop accuracy tables; the certified-alpha grid with 1/k floors; entrapment numbers; and serialized example trace-graphs (with at least one rendered DOT per genre). Gradual scaling; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "+          \"approach\": \"On the 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean 2372 chars), run the full pipeline per the pipeline spec and the FDR-gate spec dependencies, re-using the tested OpenRouter client, gate code, and K=5 self-consistency elicitation from the iteration-2 experiment workspaces (art_Inu52CyA49Ys, art_sHNuY68d4-Wh) read from the persisted run tree. STAGE 1 EXTRACTION + TYPING: LLM over-generates typed first-order FACT/BRIDGE candidates (LINC/Logic-LM style); argument types grounded via the offline WordNet->SUMO recipe (Block C of the grounding/design dependency: WordNet hypernyms -> {PER,LOC,ORG,TIME,NUM,MISC} -> SUMO upper-ontology classes via WordNetMappings30), used ONLY for typing/decoy-constraint, never to filter. STAGE 2 DECOYS + SCORING + GATE: property-matched document-conditioned counterfactual decoys with non-entailment check -> ISOLATED provenance-blinded scoring under BOTH the VERBALIZED and the K=5 SELF-CONSISTENCY elicitations -> knockoff+ gate across ALL alpha {0.05,0.1,0.2,0.3,0.5} with deterministic entrapment corroboration (r=1). PRIMARY METRIC (goal hard requirement): hallucinated-fact rate -- the fraction of admitted atomic facts NOT entailed by the document (judged against gold facts + provenance char-spans, with a documented adjudication procedure for the silver genres) -- for decoy-gated extraction vs RAW LLM generation (no gate, all extracted facts admitted), reported PER GENRE, under BOTH elicitations x ALL alpha, with document-block bootstrap CIs. The regime-dependence MUST be explicit and never obscured: report that under logprob/verbalized the method can be worse-than-baseline at some alpha, and under self-consistency it is vacuous below the certified alpha -- present the full grid so a reader sees exactly the cell where the reduction is real. SECONDARY METRICS (goal requirements i and ii): atomic-fact extraction precision and recall vs gold; multi-hop deduction accuracy from admitted facts via the symbolic reasoner; and a matched-recall comparison of decoy-gated vs RAW LLM vs RAG (BM25) vs chain-of-thought (the goal-required purely-neural baselines) on the shared (head, relation, tail) triple schema. STAGE 3 REASONING + TRACE-GRAPHS (goal hard requirement): admitted facts/bridges populate SWI-Prolog (janus-swi) for multi-hop backward-chaining deduction; export human-auditable trace-graphs (JSON + Graphviz DOT) on AT LEAST a handful of documents spanning all three genres, where every leaf carries its provenance span, the decoy-competition certificate (W_i, T, alpha), and the entrapment certificate (FDP_hat, r). OPTIONAL ProbLog upgrade (per Part C of the grounding/design dependency, if time/budget permit): weighted clauses p_i::fact with p_i a calibrated, gate-consistent-shrinkage function of Z_i, producing probabilistic trace-graphs with per-node marginal probabilities -- deterministic backward-chaining is the REQUIRED baseline, ProbLog is the upgrade, so the headline numbers do not depend on it. Assert crisp comparisons on the legal (crisp-gold) slice and clearly-labeled relative comparisons on the silver slices. OUTPUT method_out.json (schema-valid) with: figure-ready per-genre hallucination-rate bars (gate vs raw vs RAG vs CoT) with CIs across alpha x both elicitations; atomic precision/recall and multi-hop accuracy tables; the certified-alpha grid with 1/k floors; entrapment numbers; and serialized example trace-graphs (with at least one rendered DOT per genre). Gradual scaling; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.\",", "           \"depends_on\": [", "             { \"id\": \"art_UBTwyePql8NQ\", \"label\": \"dataset\" },", "             { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },"]}], "userModified": false, "replaceAll": false}
```

### [29] TOOL CALL — Edit · 2026-06-16 08:36:21 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD: Build on the prior wedge experiment (reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it.
NEW: Build on the prior wedge experiment (art_sHNuY68d4-Wh, read from the persisted run tree -- reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it.
```

### [30] TOOL RESULT — Edit · 2026-06-16 08:36:21 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "Build on the prior wedge experiment (reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it.", "newString": "Build on the prior wedge experiment (art_sHNuY68d4-Wh, read from the persisted run tree -- reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it.", "originalFile": null, "structuredPatch": [{"oldStart": 28, "oldLines": 7, "newStart": 28, "newLines": 7, "lines": ["         {", "           \"type\": \"experiment\",", "           \"objective\": \"P3 -- Reframe and re-power the Re-DocRED operational wedge so the disconfirmation is reported PRECISELY (true number of documents used and the recall ceiling stated AT the point of claim), comparators are completed-or-dropped (no all-null baselines listed as participating), the multi-hop hallucinated-conclusion comparison is powered or explicitly labeled underpowered, and the operational contribution is recast as a NOVEL label-free REGIME-DIAGNOSTIC that predicts where decoy-gating adds value. This resolves reviewer MAJOR #3 and converts a narrow negative result into the paper's unifying operational insight.\",", "-          \"approach\": \"Build on the prior wedge experiment (reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it. SCOPE HONESTY: run on substantially more than the prior 36 scored documents (target the full 152 confirmatory Re-DocRED docs from the dependency anchor) and report the ACHIEVABLE recall ceiling explicitly at the claim ('at <=X% recall on N documents'); never imply 152 confirmatory while scoring fewer. COMPARATORS: bring chain-of-thought and BM25-RAG to a comparable matched-recall operating point on the shared triple schema; if either cannot reach the grid start (the prior run had CoT/RAG max recall 0.049/0.041 below the 0.05 grid start, all-null), REMOVE it from the wedge comparator list and say so -- do NOT list all-null baselines as participating. Keep the plain confidence-threshold gate as the load-bearing zero-label foil and labeled Mohri-Hashimoto conformal as the labeled reference (report its calibration-label count vs the method's zero labels). At the matched-recall operating point report precision, the precision-wedge delta(METHOD-PLAIN), and PR curves with document-block bootstrap (B>=2000) CIs and BH correction. POWER THE MULTI-HOP COMPARISON: forward-chain over more documents / deeper rules to raise the number of derived conclusions per system above a stated power target for the hallucinated-conclusion-rate comparison; if it remains underpowered, label it UNDERPOWERED explicitly with the conclusion count and CI width (the prior run rested on ~20-24 conclusions, CIs spanning [0.29,1.0]). REGIME-DIAGNOSTIC (the novel reframing, connecting to P1): using ONLY the label-free signals (tail-conditioned win-rate and the spontaneous-error CDF match, computed without gold), PREDICT which regime Re-DocRED's scorer is in (an already-calibrated logprob yes-token scorer -> 'thresholding-is-enough', gate redundant), then VALIDATE that prediction against the realized null wedge; pair this with P1's CLUTRR regime (overconfident verbalized/logprob tail -> gate adds value) to state and test the unifying principle 'the gate adds value only where the base elicitation is tail-overconfident, and is redundant where it is calibrated', reporting the diagnostic's predictive direction across both anchors. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally). Keep the alignment-error confound check from the prior run. OUTPUT method_out.json (schema-valid) with: figure-ready matched-recall PR arrays and the precision-wedge delta with CIs for ONLY the participating systems; multi-hop hallucination bars with explicit per-system conclusion counts and CIs (or an underpowered flag); the regime-diagnostic prediction-vs-realized panel; and a precisely-scoped operational verdict ('disconfirmed at <=X% recall on N docs; reframed as regime-diagnostic'). Log cumulative LLM cost after EVERY call; soft cap ~$2, HARD STOP at $10.\",", "+          \"approach\": \"Build on the prior wedge experiment (art_sHNuY68d4-Wh, read from the persisted run tree -- reuse its identical candidate+alignment pool, the fixed MiniLM top-8 + temp-0 relation aligner, the three-tier entity linking, and the official tuple-matching metric) and scale it. SCOPE HONESTY: run on substantially more than the prior 36 scored documents (target the full 152 confirmatory Re-DocRED docs from the dependency anchor) and report the ACHIEVABLE recall ceiling explicitly at the claim ('at <=X% recall on N documents'); never imply 152 confirmatory while scoring fewer. COMPARATORS: bring chain-of-thought and BM25-RAG to a comparable matched-recall operating point on the shared triple schema; if either cannot reach the grid start (the prior run had CoT/RAG max recall 0.049/0.041 below the 0.05 grid start, all-null), REMOVE it from the wedge comparator list and say so -- do NOT list all-null baselines as participating. Keep the plain confidence-threshold gate as the load-bearing zero-label foil and labeled Mohri-Hashimoto conformal as the labeled reference (report its calibration-label count vs the method's zero labels). At the matched-recall operating point report precision, the precision-wedge delta(METHOD-PLAIN), and PR curves with document-block bootstrap (B>=2000) CIs and BH correction. POWER THE MULTI-HOP COMPARISON: forward-chain over more documents / deeper rules to raise the number of derived conclusions per system above a stated power target for the hallucinated-conclusion-rate comparison; if it remains underpowered, label it UNDERPOWERED explicitly with the conclusion count and CI width (the prior run rested on ~20-24 conclusions, CIs spanning [0.29,1.0]). REGIME-DIAGNOSTIC (the novel reframing, connecting to P1): using ONLY the label-free signals (tail-conditioned win-rate and the spontaneous-error CDF match, computed without gold), PREDICT which regime Re-DocRED's scorer is in (an already-calibrated logprob yes-token scorer -> 'thresholding-is-enough', gate redundant), then VALIDATE that prediction against the realized null wedge; pair this with P1's CLUTRR regime (overconfident verbalized/logprob tail -> gate adds value) to state and test the unifying principle 'the gate adds value only where the base elicitation is tail-overconfident, and is redundant where it is calibrated', reporting the diagnostic's predictive direction across both anchors. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally). Keep the alignment-error confound check from the prior run. OUTPUT method_out.json (schema-valid) with: figure-ready matched-recall PR arrays and the precision-wedge delta with CIs for ONLY the participating systems; multi-hop hallucination bars with explicit per-system conclusion counts and CIs (or an underpowered flag); the regime-diagnostic prediction-vs-realized panel; and a precisely-scoped operational verdict ('disconfirmed at <=X% recall on N docs; reframed as regime-diagnostic'). Log cumulative LLM cost after EVERY call; soft cap ~$2, HARD STOP at $10.\",", "           \"depends_on\": [", "             { \"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\" },", "             { \"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\" },"]}], "userModified": false, "replaceAll": false}
```

### [31] ASSISTANT · 2026-06-16 08:36:38 UTC

```
Now let me re-validate the full structure and dependency-type rules against the existing artifact types.
```

### [32] TOOL CALL — Bash · 2026-06-16 08:36:38 UTC

```
Re-validate dependency types and structure:
python3 -c "
import json
d=json.load(open('.terminal_claude_agent_struct_out.json'))
# existing artifact types
TYPES={'art_XZyKy6QuwxrO':'dataset','art_Jcudmkugg1qT':'dataset','art_SLUbUUr6Ul98':'research','art_K6AE23HoGqe6':'research','art_ikjFm_faAe0x':'experiment','art_Inu52CyA49Ys':'experiment','art_sHNuY68d4-Wh':'experiment','art_UBTwyePql8NQ':'dataset','art_Cr6L9JpoewZi':'research'}
ALLOWED={'research','dataset'}  # for experiment deps
s=d['strategies']; assert len(s)==1
ads=s[0]['artifact_directions']
print('n_artifacts:',len(ads))
ok=0
for i,a in enumerate(ads):
    assert a['type'] in {'experiment','research','proof','evaluation','dataset'}
    assert a['objective'] and a['approach']
    deps=a.get('depends_on',[])
    hasdataset=False; valid=True
    for x in deps:
        assert x['id'] in TYPES, ('unknown dep',x['id'])
        assert x['label'].strip()
        t=TYPES[x['id']]
        if t=='dataset': hasdataset=True
        if a['type']=='experiment' and t not in ALLOWED:
            valid=False; print('  INVALID dep',x['id'],t)
    if a['type']=='experiment' and not hasdataset:
        valid=False; print('  MISSING dataset dep')
    if valid: ok+=1
    print(f'  art{i+1} type={a[\"type\"]} valid={valid} deps='+','.join(x[\"id\"]+\":\"+TYPES[x[\"id\"]] for x in deps))
print('VALID_ARTIFACTS:',ok)
assert ok>=1
print('ALL CHECKS PASS')
"
```

### [33] TOOL RESULT — Bash · 2026-06-16 08:36:38 UTC

```
{"stdout": "n_artifacts: 3\n  art1 type=experiment valid=True deps=art_XZyKy6QuwxrO:dataset,art_SLUbUUr6Ul98:research\n  art2 type=experiment valid=True deps=art_UBTwyePql8NQ:dataset,art_K6AE23HoGqe6:research,art_SLUbUUr6Ul98:research,art_Cr6L9JpoewZi:research\n  art3 type=experiment valid=True deps=art_Jcudmkugg1qT:dataset,art_K6AE23HoGqe6:research,art_SLUbUUr6Ul98:research\nVALID_ARTIFACTS: 3\nALL CHECKS PASS", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [34] ASSISTANT · 2026-06-16 08:36:50 UTC

```
All issues are fixed. The corrected strategy now validates cleanly:

**Dependency fixes applied** — removed the three experiment-type dependencies that violated the rule (experiments may only depend on `research` and `dataset` artifacts):
- **P1**: dropped `art_Inu52CyA49Ys` + `art_ikjFm_faAe0x` (experiments) → now depends on `art_XZyKy6QuwxrO` (dataset) + `art_SLUbUUr6Ul98` (research)
- **P2**: dropped `art_Inu52CyA49Ys` (experiment) → now depends on `art_UBTwyePql8NQ` (dataset) + `art_K6AE23HoGqe6`, `art_SLUbUUr6Ul98`, `art_Cr6L9JpoewZi` (research)
- **P3**: dropped `art_sHNuY68d4-Wh` (experiment) → now depends on `art_Jcudmkugg1qT` (dataset) + `art_K6AE23HoGqe6`, `art_SLUbUUr6Ul98` (research)

Each experiment retains its **required dataset dependency** plus the relevant research specs. I also adjusted the approach text so the prior iteration-2 experiment code/results are referenced via the **persisted run tree** (which state-persistence makes accessible) rather than as formal dependencies — preserving the intent of reusing tested clients/gate code and carrying forward the settled de-circularization, without an invalid dependency edge.

**Validation result: 3/3 artifacts valid** (correct types, valid dependency types, every experiment has a dataset dep, all labels non-empty, all IDs reference existing artifacts). The strategy's substance is unchanged — three parallel execution experiments addressing all four reviewer MAJORs and the goal's binding application requirement.
```
