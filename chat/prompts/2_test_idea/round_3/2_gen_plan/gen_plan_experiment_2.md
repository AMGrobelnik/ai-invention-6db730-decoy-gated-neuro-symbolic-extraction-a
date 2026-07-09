# gen_plan_experiment_2 — test_idea

> Phase: `invention_loop` · round 3 · `gen_plan`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 08:37:02 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

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

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter3_dir2
type: experiment
objective: >-
  P2 (THE HEADLINE) -- Execute the goal's binding, still-undone requirement: a quantified, auditable hallucination reduction
  of decoy-gated neuro-symbolic extraction versus raw LLM generation (and the goal-required neural baselines RAG and chain-of-thought)
  on the genre-faithful 24-doc professional anchor (~3000-char legal/news/regulatory documents), under BOTH elicitations x
  ALL alpha, with WordNet->SUMO upper-ontology typing, atomic-fact precision/recall and multi-hop deduction accuracy, and
  human-auditable trace-graphs carrying per-leaf provenance + decoy + entrapment certificates. This resolves reviewer MAJOR
  #4 and delivers the goal's core deliverable on the genre it actually targets.
approach: >-
  On the 24-doc anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 140 gold facts, mean
  2372 chars), run the full pipeline per the pipeline spec and the FDR-gate spec dependencies, re-using the tested OpenRouter
  client, gate code, and K=5 self-consistency elicitation from the iteration-2 experiment workspaces (art_Inu52CyA49Ys, art_sHNuY68d4-Wh)
  read from the persisted run tree. STAGE 1 EXTRACTION + TYPING: LLM over-generates typed first-order FACT/BRIDGE candidates
  (LINC/Logic-LM style); argument types grounded via the offline WordNet->SUMO recipe (Block C of the grounding/design dependency:
  WordNet hypernyms -> {PER,LOC,ORG,TIME,NUM,MISC} -> SUMO upper-ontology classes via WordNetMappings30), used ONLY for typing/decoy-constraint,
  never to filter. STAGE 2 DECOYS + SCORING + GATE: property-matched document-conditioned counterfactual decoys with non-entailment
  check -> ISOLATED provenance-blinded scoring under BOTH the VERBALIZED and the K=5 SELF-CONSISTENCY elicitations -> knockoff+
  gate across ALL alpha {0.05,0.1,0.2,0.3,0.5} with deterministic entrapment corroboration (r=1). PRIMARY METRIC (goal hard
  requirement): hallucinated-fact rate -- the fraction of admitted atomic facts NOT entailed by the document (judged against
  gold facts + provenance char-spans, with a documented adjudication procedure for the silver genres) -- for decoy-gated extraction
  vs RAW LLM generation (no gate, all extracted facts admitted), reported PER GENRE, under BOTH elicitations x ALL alpha,
  with document-block bootstrap CIs. The regime-dependence MUST be explicit and never obscured: report that under logprob/verbalized
  the method can be worse-than-baseline at some alpha, and under self-consistency it is vacuous below the certified alpha
  -- present the full grid so a reader sees exactly the cell where the reduction is real. SECONDARY METRICS (goal requirements
  i and ii): atomic-fact extraction precision and recall vs gold; multi-hop deduction accuracy from admitted facts via the
  symbolic reasoner; and a matched-recall comparison of decoy-gated vs RAW LLM vs RAG (BM25) vs chain-of-thought (the goal-required
  purely-neural baselines) on the shared (head, relation, tail) triple schema. STAGE 3 REASONING + TRACE-GRAPHS (goal hard
  requirement): admitted facts/bridges populate SWI-Prolog (janus-swi) for multi-hop backward-chaining deduction; export human-auditable
  trace-graphs (JSON + Graphviz DOT) on AT LEAST a handful of documents spanning all three genres, where every leaf carries
  its provenance span, the decoy-competition certificate (W_i, T, alpha), and the entrapment certificate (FDP_hat, r). OPTIONAL
  ProbLog upgrade (per Part C of the grounding/design dependency, if time/budget permit): weighted clauses p_i::fact with
  p_i a calibrated, gate-consistent-shrinkage function of Z_i, producing probabilistic trace-graphs with per-node marginal
  probabilities -- deterministic backward-chaining is the REQUIRED baseline, ProbLog is the upgrade, so the headline numbers
  do not depend on it. Assert crisp comparisons on the legal (crisp-gold) slice and clearly-labeled relative comparisons on
  the silver slices. OUTPUT method_out.json (schema-valid) with: figure-ready per-genre hallucination-rate bars (gate vs raw
  vs RAG vs CoT) with CIs across alpha x both elicitations; atomic precision/recall and multi-hop accuracy tables; the certified-alpha
  grid with 1/k floors; entrapment numbers; and serialized example trace-graphs (with at least one rendered DOT per genre).
  Gradual scaling; log cumulative LLM cost after EVERY call; soft cap ~$3, HARD STOP at $10.
depends_on:
- id: art_UBTwyePql8NQ
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
- id: art_Cr6L9JpoewZi
  label: grounding
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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

--- Dependency 2 ---
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

--- Dependency 3 ---
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

--- Dependency 4 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Short title for the plan",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 08:37:02 UTC

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
