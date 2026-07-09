# gen_plan_experiment_3 — test_idea

> Phase: `invention_loop` · round 4 · `gen_plan`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_3` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 10:41:15 UTC

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
  Decoy-Gated Neuro-Symbolic Extraction: A Label-Free FDR Gate Whose Validity Hinges on PAIRED (Not Just Marginal) Decoy Exchangeability
  -- Power and De-Confound the CLUTRR Disconfirmation Against Extractor Strength, Establish the Professional-Document Hallucination-Reduction
  Headline at CI Separation, and Execute the Probabilistic Reasoner
hypothesis: |-
  MECHANISM (unchanged, one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  WHAT IS NOW EXECUTED (iteration-3, MEASURED). Three experiments ran for ~$1.4 this iteration (~$2.6 cumulative of the $10 cap): (P1) the self-consistency CLUTRR calibration diagonal [art_sBLQqsdm3EIA] -- BUT on a 40-doc CHECKPOINT (410 reals: 123 true / 287 spontaneous false), NOT the powered ~593-doc run the artifact itself names as the intended final version; (P2) the 24-doc legal/news/regulatory APPLICATION headline [art_vkfyOl2OQNVx], executed end-to-end with auditable trace-graphs (210 reals: 42 true / 51 false / 117 gold-undecidable); (P3) the Re-DocRED operational wedge scaled to 152 confirmatory docs and reframed as a gold-free regime-diagnostic [art_RZC2468yZ-Jh]. Iteration-4's job is NOT to re-build but to POWER and DE-CONFOUND the central finding, SCALE the application to statistical significance, and execute the still-missing probabilistic reasoner the goal hard-requires.

  THE DECISIVE FINDING (what the evidence now says, honestly). The central scientific contribution has SHIFTED from 'elicitation-dependence' to a sharper, deeper distinction -- but that finding is currently CONFOUNDED and UNDERPOWERED, which dictates the entire iteration-4 mandate.
    (1) THE HEADLINE CONCEPTUAL LESSON IS MARGINAL != PAIRED EXCHANGEABILITY. Under the diagnostic-validated K=5 self-consistency elicitation, the counterfactual-decoy score distribution is statistically indistinguishable from the model's OWN spontaneous-error distribution (full-dist KS p=0.058, MW p=0.061, AD p=0.061, perm p=0.060 -- all FAIL to reject; admission-tail top-25% KS p=0.31) and sharply distinct from true positives (KS p=5e-9, MW p=4e-12). That is MARGINAL (distributional) exchangeability -- exactly the property DeepCoy-style decoy design and the win-rate/CDF diagnostics target, and it HOLDS. Yet knockoff+ requires the strictly stronger PER-PAIR sign-flip property at the cutoff, and it FAILS: among the 12 admitted multi_hop reals the model scored EACH false real above its own matched decoy, so realized FDR is 1.0 at the only certifiable alpha*=0.5 (doc-block CI [0.66,1.0] entirely above alpha*) and the gate's self-report decoy_fdr_hat=0.5 undershoots realized 1.0. The pre-registered primary disconfirmation FIRES on both calibration and self-report criteria. The win-rate diagnostic, being a MARGINAL statistic, structurally cannot see this gap.
    (2) THE DISCONFIRMATION IS CONFOUNDED WITH A PATHOLOGICAL EXTRACTOR AND IS UNDERPOWERED -- so the 'limitation of the entire decoy-competition approach' claim is NOT YET EARNED. The multi_hop family is ~85% genuinely false ONLY because gpt-4.1-nano's forced multi-hop relation accuracy is 0.169 (n_false 158/186) -- a regime where a tiny model essentially cannot score its own multi-hop errors at all. Realized FDR 1.0 (all 12 admitted false) and the paired sign-flip failure may therefore reflect 'this extractor is too weak for ANY admission method to help' rather than an intrinsic property of decoy-gating at the LLM boundary. Compounding this, EVERY affirmative number rests on thin power: 40 docs / 12 admitted pairs, crux p-values all within ~0.01 of rejecting (0.058-0.061), the S1b ladder has only 2 false pairs/rung. A reviewer cannot distinguish 'knockoffs fundamentally do not transfer' from 'this single weak-model, single-family checkpoint is too noisy to conclude anything.' DE-CONFOUNDING + POWERING this is the single change that most increases the credibility and reach of the headline lesson.
    (3) THE ONLY WELL-POWERED RESULT IS NEGATIVE-OPERATIONAL, AND THE APPLICATION HEADLINE IS DIRECTIONAL-ONLY. On 152 Re-DocRED docs the operational wedge over plain thresholding is cleanly DISCONFIRMED at recall<=0.075 ('thresholding-is-enough when the base scorer is calibrated'), and its 267-conclusion multi-hop comparison is genuinely powered (halluc rate ~0.79 both systems, delta -0.004, CI [-0.018,0.008]). On the 24-doc application anchor the ~25% relative atomic hallucination reduction (gate 0.183 self-consistency / 0.178 logprob vs raw 0.243) reaches CI separation in 0 of 40 cells, and the multi-hop corruption drop (0.48->0.18) is 11 vs 23 derived conclusions with NO CI and is driven entirely by the regulatory genre (regulatory 12->3; legal already 0.0; news derives 0). The honest unifying principle survives: the gate adds value only where the base elicitation is tail-overconfident AND decoys are paired-exchangeable, and is redundant where the base scorer is already calibrated -- but every quantitative leg of that principle needs power it currently lacks.

  THE ONE THING THAT MATTERS NOW (iteration-4 mandate, in priority order).
    P1 -- POWER AND DE-CONFOUND THE CALIBRATION DIAGONAL (this is the headline experiment). (a) POWER: execute the full ~593-doc self-consistency CLUTRR diagonal the artifact already specifies, so the disconfirmation and the marginal-exchangeability crux p-values are NOT borderline (target: crux full-dist tests clearly fail-to-reject or clearly reject with n well above the current 12-pair tail; report the realized-FDR-vs-alpha diagonal with decoy_fdr_hat vs realized vs alpha across the certified grid). (b) DE-CONFOUND -- the decisive addition: run at least one diagonal with a STRONGER extractor (or a less error-dense family, or a controlled construction that VARIES false-positive density across, e.g., 20% / 50% / 85% genuine-false) and measure whether the PER-PAIR sign-flip failure PERSISTS. If the paired failure survives across extractor strength and false-positive density, the 'marginal != paired is a property of the LLM boundary' lesson is EARNED and becomes the paper's headline; if it vanishes with a competent extractor (i.e. the gate then controls realized FDR at alpha), SCOPE the claim to the error-dense/weak-scorer regime and report the positive 'gate works when the extractor can score its own errors' result instead. Either outcome is publishable; the current single-point observation is not. (c) Add a PAIRED-exchangeability statistic (per-pair win-rate over FALSE pairs at the cutoff) reported DISTINCTLY from the marginal win-rate, and compute it ACROSS the (G,S) configs (see de-circularization below).
    P2 -- ESTABLISH THE APPLICATION HEADLINE AT CI SEPARATION (the goal's binding deliverable). Scale the 24-doc legal/news/regulatory anchor toward statistical significance: more documents per genre AND a cleaner crisp-gold subset to shrink the 117/210 gold-undecidable fraction, until at least the POOLED hallucinated-fact reduction (gate vs raw LLM) reaches document-block-bootstrap CI separation; report the multi-hop corruption result WITH CIs and an explicit single-genre-origin flag. Until CI separation is reached, state PLAINLY at the point of claim that the reduction is DIRECTIONAL and not significant at the current n, and that the binding deliverable is demonstrated as a trend with auditable provenance, not a significant reduction. Continue exporting per-leaf-certified trace-graphs across all genres and elicitations and the full alpha grid.
    P3 -- LEAD WITH THE CONCEPTUAL RESULT; DEMOTE THE REGIME-DIAGNOSTIC. Make MARGINAL-vs-PAIRED exchangeability (P1) the paper's primary novel contribution. Acknowledge EXPLICITLY that the regime-diagnostic's signals are not independent -- signal C (frac(W==Z)=0.939, admitted-set Spearman rho=0.991) is mechanically the SAME quantity as signal-A tail win-rate, because W_i=Z_i exactly when the real out-scores its decoy, so 'the gate keeps and orders the same facts as the plain threshold, so the wedge is mechanically null' is close to a restatement of the realized null, not an independent forecast -- and either (a) DEMOTE the regime-diagnostic to a heuristic (default) or (b) validate it predictively on several additional anchors/regimes with a genuine held-out evaluation so the 2-axis map rests on more than 2-3 points. Do NOT present a near-mechanical observation as a forecast.
    P4 -- EXECUTE THE PROBABILISTIC REASONER (goal hard-requirement, currently only specified). Run even a MINIMAL ProbLog probabilistic-reasoning step on one anchor using the exact get_evaluatable().create_from(...).evaluate() swap and certificate->weight mapping already specified [art_Cr6L9JpoewZi], so the LLM-as-probabilistic-reasoner / fuzzy-unification requirement is DEMONSTRATED rather than only designed. If it cannot run, state in the CONTRIBUTIONS (not only limitations) that the probabilistic layer is future work, so the abstract/intro never imply it is delivered.

  THE GATE (one canonical statistic; unchanged). For each candidate i with real score Z_i and matched-decoy score Z~_i, the competition statistic is the knockoff+ signed maximum W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. NEW reporting requirements: (i) ALWAYS report the gate's internal estimate decoy_fdr_hat alongside realized FDR and alpha, so 'the estimate is anti-conservative' (decoy_fdr_hat < realized) is surfaced as its own failure mode; (ii) report the MARGINAL diagnostic (pooled decoy-vs-spontaneous-error win-rate / CDF tests) and the PAIRED diagnostic (per-pair win-rate over false pairs at the cutoff) SEPARATELY, because the central finding is precisely that the marginal can hold while the paired fails.

  VALIDITY HONESTY (now empirically grounded). knockoff+ delivers a finite-sample FDR GUARANTEE only under the joint-null PAIRED sign-flip property; for LLM decoys that property is UNPROVABLE. The iteration-3 evidence localizes the failure to a two-layer structure: a MARGINAL layer (decoy scores distributed like the model's spontaneous errors), which is label-free testable and which self-consistency RESTORES; and a PAIRED layer (false real and its decoy equally likely to take the larger score AS A PAIR), which the knockoff theorems actually require and which FAILS at the cutoff on the current evidence. The realized-FDR-vs-alpha diagonal IS the empirical test of the paired layer. The standard decoy-quality diagnostics imported from genomics/proteomics live entirely in the marginal layer and therefore OVER-CERTIFY the gate. CRITICAL CAVEAT carried into iteration-4: this two-layer story is, on present evidence, observed in ONE weak-extractor, error-dense, 12-pair regime; it is asserted as the paper's headline ONLY if P1's de-confounding shows the paired failure persists across extractor strength / false-positive density. If it does not persist, the validity story is re-scoped to the weak-scorer regime and the positive 'controls FDR with a competent extractor' result leads instead. The document-block bootstrap supplies realized-FDP CIs and a dependence diagnostic; it does NOT restore the guarantee.

  THE DIAGNOSTIC BLIND SPOT (materially qualifies the 'self-detecting gate' contribution). The headline was once 'tail diagnostics tell the practitioner which regime they are in.' Two faces of a blind spot remain: (1) STRUCTURAL -- a MARGINAL win-rate cannot certify PAIRED validity, period (this is the conceptual core, not a power issue). (2) UNDERPOWERED -- the S1b difficulty ladder L0..L4 has only 2 false pairs/rung, so its verdict (PARTIAL) is noise; the prior narrative that 'the diagnostic detects only grossly out-of-context (foreign-entity) decoys' is in fact CONTRADICTED by the artifact (L0 foreign-swap detected_anti_conservative=FALSE while L1-L4 in-distribution rungs=TRUE) and must be either powered or restated purely as 'underpowered, cannot localize which decoy classes are detected, cannot certify paired validity.' CLAIM S1b stands: a usable self-detecting gate REQUIRES a diagnostic that retains discriminating power in the valid regime AND that probes the PAIRED layer; iteration-4 supplies a powered paired-exchangeability diagnostic or reports the blind spot as a fundamental limitation and downgrades the 'tells you when to trust the gate' claim accordingly.

  DE-CIRCULARIZATION (MARGINAL settled; PAIRED not yet evidenced). The Generator!=Scorer ablation is ROBUST for the MARGINAL tail win-rate across all four (G,S) configs incl. decoys from gpt-4.1-nano scored by cross-family ministral-8b (CIs cover 0.5, e.g. 0.491 [0.37,0.61], KS p=0.999), so restored marginal exchangeability is NOT a shared-model artifact. HOWEVER -- a rigor gap surfaced this iteration -- the ablation tests ONLY the marginal statistic; the PAIRED sign-flip property has NOT been tested across (G,S) configs, so paired-failure robustness to G!=S is currently ASSERTED, not evidenced. Iteration-4 must either compute the paired-exchangeability statistic across the (G,S) configs to actually support de-circularization for the paired layer, or explicitly soften the claim to 'only marginal robustness to G!=S is demonstrated.'

  POWER (the binding gate for every affirmative claim). Phase-0 must demonstrate, UNDER SELF-CONSISTENCY, that the certified grid extends below the loose alpha*=0.5 (>= 1/alpha admissions AND >= N_false_min=40 genuine false admissions among reals) on the SCALED corpus before the diagonal is asserted at tighter alpha; the ~593-doc run is the vehicle. Crux full-distribution tests must move off the borderline; the application reduction must reach CI separation on the pooled metric; the corruption result must carry CIs. Any alpha / cell whose power floor is not reached is reported as a precondition, NEVER as 'confirmed by conservatism.'

  SCOPE / GOAL ALIGNMENT (the application is the binding deliverable). The goal targets ~3000-character professionally written legal/news/regulatory documents, upper-ontology grounding, an LLM probabilistic-reasoning engine at fuzzy unifications, auditable trace-graphs, and a QUANTIFIED hallucination reduction vs raw LLM. CLUTRR (synthetic kinship, crisp gold) hosts the powered+de-confounded calibration diagonal and the marginal-vs-paired lesson; Re-DocRED (Wikipedia prose, human gold) hosts the well-powered operational comparison; the 24-doc professional slice [art_UBTwyePql8NQ] hosts the application headline (WordNet->SUMO typing standing in for the discontinued OpenCyc, used ONLY for typing; minimal ProbLog probabilistic step; hallucination-reduction vs raw across both elicitations and all alpha; per-leaf-certified trace-graphs). If the application reduction cannot reach CI separation after scaling, report it as a directional trend with auditable provenance, never as a significant reduction.

  CLAIM CHAIN (each row independently testable; verdicts reflect iteration-3 evidence and the iteration-4 mandate).
    | # | CLAIM | STATUS | ITERATION-4 ACTION / PASS CRITERION |
    |---|-------|--------|-------------------------------------|
    | S0 | Score separation via tail-exchangeability SELECTION (not AUC) | PASS | confirm under the elicitation hosting the powered diagonal; verbalized/DINCO higher AUC (0.861/0.871) but fail the tail test; self-consistency tail win-rate 0.482 |
    | S1 | MARGINAL decoy match (decoy ~ spontaneous error, != true positive) | HOLDS but BORDERLINE/UNDERPOWERED (KS p=0.058 etc., 12-pair tail) | power to clearly fail-to-reject (or reject) on the ~593-doc run |
    | S1c (NEW, HEADLINE) | MARGINAL != PAIRED: marginal holds while per-pair sign-flip fails at the cutoff | OBSERVED but CONFOUNDED (weak extractor acc 0.17, error-dense, 12 pairs) | DE-CONFOUND across extractor strength / false-positive density; if paired failure persists -> earned headline; else scope to weak-scorer regime |
    | S1b | Diagnostic sensitivity / paired-layer detectability | FAIL/UNDERPOWERED (2 false pairs/rung; prior narrative contradicted by data) | power the ladder or report as purely underpowered; supply a paired-exchangeability diagnostic or report fundamental limitation |
    | S2 | Calibration diagonal (CLUTRR, self-consistency) | DISCONFIRMED on 40-doc checkpoint (realized 1.0 at alpha*=0.5, CI [0.66,1.0]) but UNDERPOWERED+CONFOUNDED | power to ~593 docs + de-confound; report decoy_fdr_hat vs realized vs alpha across certified grid |
    | S2-self | Gate self-report tracks realized | DISCONFIRMED on CLUTRR multi_hop (decoy_fdr_hat=0.5 < realized 1.0); CONSERVATIVE on application (>=realized in all 40 cells) | report both regimes; surface anti-conservative self-report as its own failure mode |
    | S2b | Generator!=Scorer de-circularization | MARGINAL ROBUST (4/4 cover 0.5); PAIRED NOT YET TESTED | compute the PAIRED statistic across (G,S) configs OR soften to 'marginal-only' |
    | S3 | Entrapment corroboration | AGREES loosely (FDP_hat high, e.g. application pooled 0.81 at alpha=0.5, honestly flagging loose admission) | report at alpha* and 0.5; restrict agreement claims to where they hold |
    | S4 | Operational wedge (Re-DocRED) | DISCONFIRMED, WELL-POWERED (152 docs, recall<=0.075; 267-conclusion multi-hop delta -0.004, CI [-0.018,0.008]) | stands; 'thresholding-is-enough when base scorer calibrated' |
    | S4b | Application hallucination reduction (professional docs) -- BINDING DELIVERABLE | EXECUTED but DIRECTIONAL (gate 0.183/0.178 vs raw 0.243 ~25%; 0/40 cells CI-separated); corruption 0.48->0.18 (11 vs 23, single-genre, no CI) | scale to POOLED CI separation; cleaner crisp gold to shrink 117/210 undecidable; corruption with CIs + single-genre flag |
    | S4c | Gold-free regime-diagnostic | NOVEL but PARTLY TAUTOLOGICAL (signal C == signal A; Re-DocRED prediction near-forced) | acknowledge A/C redundancy; demote to heuristic OR validate predictively on >=3 held-out anchors |
    | S7 (NEW) | LLM-as-probabilistic-reasoner (ProbLog) at fuzzy unifications | SPECIFIED, NOT RUN | execute a minimal ProbLog run on one anchor (get_evaluatable().evaluate(), certificate->weight) OR state as future work in contributions |
    | S5 / S6 | Document-level predictive account / predictable propagation | leftover-only | predictive IFF >= N_min held-out units; else descriptive |

  VALIDITY OF THE TWO-LAYER NOVELTY (positioning). To our knowledge this is the first demonstration that, when knockoffs/target-decoy competition are transplanted to LLM scoring, the MARGINAL property the cheminformatics/proteomics decoy-quality diagnostics target (DeepCoy, win-rate/CDF) can be satisfied while the PAIRED sign-flip property the knockoff theorems require is violated -- so a marginal diagnostic over-certifies the gate. All nearest neighbors (conformal factuality/selection/coherent-factuality, multiple-testing hallucination detection, conformal e-value novelty, conformal link prediction) are LABELED, certify a model OUTPUT, and ASSUME exchangeability; ours is label-free, certifies the INTERMEDIATE admission boundary, and empirically TESTS exchangeability -- and finds the marginal-vs-paired gap. This conceptual contribution is asserted as the headline ONLY after P1's powering+de-confounding; otherwise it is reported as a scoped observation in the weak-extractor regime.

  BUDGET (unchanged ceiling, far underspent). ~$2.6 of the $10 cap spent cumulatively. Isolated provenance-blinded scoring with document-prefix prompt caching remains default; cumulative LLM cost logged after every call; HARD STOP at $10. Waterfall ORDER: (P1) powered+de-confounded self-consistency diagonal with the paired statistic across (G,S); (P2) scaled application reduction to CI separation + minimal ProbLog (P4); (P3) demote/validate the regime-diagnostic; then S5/S6/floor-relaxation leftover-only.

  SCOPE OF CLAIMS. The honest central claim is now: a label-free FDR gate at the text-to-logic admission boundary is EXECUTABLE; its certified-FDR validity decomposes into a MARGINAL layer (label-free testable, restored by self-consistency) and a PAIRED layer (required by knockoff+, observed to fail at the cutoff in a weak-extractor error-dense regime), so a marginal diagnostic over-certifies it; whether the paired failure is intrinsic to the LLM boundary or specific to weak extractors / error-dense families is THE open question iteration-4 resolves by de-confounding; the gate's operational value over plain thresholding is NULL where the base scorer is calibrated (well-powered on Re-DocRED) and its application hallucination-reduction is currently a directional trend with auditable provenance pending scaling to CI separation. Facts AND bridges carry the claim.

  MOTIVATION (unchanged core). Text-to-logic pipelines stall where strict symbolic unification fails and an LLM must fuzzy-match predicates and supply background knowledge; that interface is where PLAUSIBLE, high-confidence false facts re-enter and silently corrupt every downstream deduction, and no existing label-free method offers an FDR knob there (self-consistency/LLM-judge are heuristic; ontology filters catch only encoded violations; conformal factuality/selection/multiple-testing all need LABELED calibration and certify the OUTPUT, not the admission boundary). Genomics/proteomics solved the isomorphic label-poor problem with the knockoff filter + target-decoy competition and learned the two failure modes (too-easy decoys -> optimistic FDR, cured by property-matched decoys; entrapment FDP needs a valid independent upper bound). We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary. The iteration-3 evidence refines this into a cautionary, generalizable lesson -- marginal matching is necessary but not sufficient for the paired property the theorems require -- and the deliverable that matters is the regime-aware, application-faithful, auditable hallucination-reduction the goal hard-requires, established at adequate power.

  KEY ASSUMPTIONS (carried, updated by evidence). (1) The null sign-flip property is ENGINEERED AND TESTED, not guaranteed -- and the evidence shows it must be tested at the PAIRED layer, not just the marginal layer; a marginal win-rate ~0.5 does NOT imply paired validity. (2) The disconfirmation must be DE-CONFOUNDED from extractor weakness/error-density before any 'intrinsic limitation' claim is made -- false-positive density and extractor strength are now treated as experimental axes, not fixed at the pathological gpt-4.1-nano multi-hop regime (acc 0.17). (3) Score-dependence handled by document-block bootstrap + isolated provenance-blinded scoring. (4) The diagonal needs genuine false admissions AND adequate power (the ~593-doc run is the binding vehicle). (5) A usable self-detecting diagnostic must probe the PAIRED layer and retain sensitivity in the valid regime -- currently UNMET, pre-registered for repair or honest down-scoping. (6) The application headline must reach CI separation on the pooled reduction to be claimed as significant; otherwise it is a directional trend. (7) The probabilistic reasoner must be EXECUTED (minimal ProbLog) or explicitly declared future work in the contributions.

  INVESTIGATION APPROACH. Strict budget waterfall: Phase-0 (confirm separation + populability + power floor + marginal AND paired diagnostics under self-consistency on the scaled corpus) -> P1 powered+de-confounded self-consistency CLUTRR diagonal varying extractor strength / false-positive density, with the paired statistic across (G,S) -> P2 application hallucination-reduction scaled to CI separation + minimal ProbLog run -> P3 demote/validate the regime-diagnostic -> leftover S5/S6. CPU-only; cost logged after every call; HARD STOP at $10. Pipeline unchanged in structure (over-generating extraction -> property-matched counterfactual decoys with non-entailment verification -> isolated provenance-blinded self-consistency scoring -> knockoff+ gate reporting realized FDR AND decoy_fdr_hat AND marginal+paired diagnostics -> independent entrapment corroboration -> document-block bootstrap CIs -> SWI-Prolog/ProbLog reasoning with auditable per-leaf-certified trace-graphs). FIGURES must carry full captions (1/k floor, bootstrap CIs, gate-vs-plain-vs-swap separation on the diagonal; overlaid decoy/spontaneous/true-positive CDFs with the paired-win asymmetry annotated on the crux; all participating systems with CIs at the matched operating point on the wedge).

  SUCCESS CRITERIA. PRECONDITION (gate): the SCALED self-consistency run must confirm score separation, populability >= N_false_min, a non-empty certified grid below alpha=0.5, AND non-borderline crux p-values BEFORE the diagonal is asserted. PRIMARY DISCONFIRMATION (single): on the populable CLUTRR family under isolated self-consistency at the operative alpha, the central control claim is DISCONFIRMED if realized corpus-aggregate FDR exceeds alpha by more than tau (tau=0.05) AND the document-block-bootstrap CI lies entirely on the anti-conservative side; the gate's self-report is additionally disconfirmed if decoy_fdr_hat is anti-conservative relative to realized. CONFIRMED of the HEADLINE CONCEPTUAL LESSON requires: the paired sign-flip failure PERSISTS across at least two extractor-strength / false-positive-density settings while marginal exchangeability holds (earning 'marginal != paired at the LLM boundary'); if the paired failure VANISHES with a competent extractor, the positive result 'the gate controls realized FDR at alpha when the extractor can score its own errors' is reported and the limitation is scoped to the weak-scorer regime. APPLICATION: the binding deliverable is CONFIRMED only when the pooled hallucinated-fact reduction vs raw LLM reaches document-block-bootstrap CI separation; otherwise reported as a directional trend with auditable provenance. The Re-DocRED operational claim stands as DISCONFIRMED-at-scope (thresholding-is-enough when the base scorer is calibrated), framed precisely (n=152, recall ceiling 0.075). A BH multiplicity correction is applied across all validation tests. DISCONFIRMED if the primary disconfirmation fires under the validated elicitation at adequate power; an uninterpretable null (underpowered tail/diagonal/gap) is the failure the Phase-0 power analysis is designed to prevent.
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
  Same gate frame; headline re-pointed to marginal-vs-paired exchangeability with a powering + de-confounding mandate.
_confidence_delta: decreased
_key_changes:
- >-
  REFRAMED THE HEADLINE CONTRIBUTION to MARGINAL != PAIRED exchangeability (new claim S1c): under self-consistency the counterfactual-decoy
  distribution matches the model's spontaneous errors (marginal, KS p=0.058) yet the per-pair sign-flip property fails at
  the cutoff (12/12 admitted multi_hop reals out-score their decoys; realized FDR 1.0 at alpha*=0.5) -- a marginal diagnostic
  over-certifies the gate [art_sBLQqsdm3EIA].
- >-
  ADDED A DE-CONFOUNDING MANDATE (reviewer methodology-MAJOR): the disconfirmation is confounded with a pathological extractor
  (gpt-4.1-nano multi-hop accuracy 0.169, family ~85% false) and only 12 admitted pairs; iteration-4 MUST vary extractor strength
  / false-positive density to test whether the paired failure is intrinsic to the LLM boundary or specific to the weak-scorer/error-dense
  regime, and scope the 'limitation of the entire approach' claim accordingly.
- >-
  MADE POWERING THE BINDING GATE (reviewer evidence-MAJOR): mandated the full ~593-doc self-consistency diagonal (vs the current
  40-doc checkpoint) so the disconfirmation and crux p-values (all within ~0.01 of rejecting) are not borderline; corruption
  result reported with CIs and a single-genre-origin flag; S1b ladder (2 false pairs/rung) powered or restated as purely underpowered.
- >-
  DEMOTED THE REGIME-DIAGNOSTIC (reviewer novelty-MAJOR): acknowledged that signal C (frac(W==Z)=0.939) is mechanically identical
  to signal-A win-rate, so the 'mechanically null' prediction restates the realized null; recast as a heuristic and led with
  the marginal-vs-paired conceptual result, unless validated predictively on >=3 held-out anchors [art_RZC2468yZ-Jh].
- >-
  SET A CI-SEPARATION BAR FOR THE BINDING APPLICATION DELIVERABLE (reviewer scope-MAJOR): the ~25% reduction reaches 0/40
  cells of CI separation at n=24; mandated scaling the anchor (more docs/genre, cleaner crisp gold to shrink the 117/210 undecidable
  fraction) until the pooled reduction is CI-separated, and stating it as directional until then [art_vkfyOl2OQNVx].
- >-
  SPLIT DE-CIRCULARIZATION INTO MARGINAL (settled ROBUST across 4 (G,S) configs) vs PAIRED (NOT YET TESTED across configs);
  mandated computing the paired-exchangeability statistic across (G,S) or softening the de-circularization claim to marginal-only
  (reviewer rigor-MINOR).
- >-
  PROMOTED THE PROBABILISTIC REASONER to an explicit claim S7 (reviewer rigor-MINOR + goal alignment): execute a minimal ProbLog
  run (get_evaluatable().evaluate(), certificate->weight) on one anchor or declare it future work in the CONTRIBUTIONS, since
  the goal hard-requires an LLM-as-probabilistic-reasoner at fuzzy unifications.
- >-
  FIXED THE S1b OVER-STATEMENT (reviewer rigor-MINOR): the artifact ladder shows L0 foreign-swap NOT detected while L1-L4
  ARE -- the opposite of the prior 'detects only gross decoys' narrative; rewritten as underpowered, and figure-caption requirements
  (1/k floor, CIs, gate-vs-plain-vs-swap, paired-win asymmetry) made explicit.
- >-
  CONFIDENCE DECREASED: the headline disconfirmation is both confounded (weak extractor) and underpowered (12 pairs, borderline
  p-values), the only well-powered result is the Re-DocRED operational null, and the binding application reduction is directional-only
  -- the core idea and a sharper conceptual lesson survive, but every affirmative claim now needs power and de-confounding
  it currently lacks.
relation_type: evolution
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter4_dir4
type: experiment
objective: >-
  P4 + P2-FRAMING -- Execute the still-missing probabilistic reasoner (a minimal ProbLog run) so the goal's LLM-as-probabilistic-reasoner
  / fuzzy-unification HARD requirement is DEMONSTRATED rather than only specified, and finalize the application pipeline's
  HONEST reporting on the existing anchor: the multi-hop corruption-propagation result WITH bootstrap CIs and an explicit
  single-genre-origin flag, the directional-not-significant atomic-reduction framing stated at the point of claim, and probabilistic
  trace-graphs carrying per-leaf certificates. Resolves reviewer rigor-MINOR (ProbLog) and strengthens scope-MAJOR's honest
  framing.
approach: >-
  On the EXISTING 24-doc application anchor (art_UBTwyePql8NQ; the expanded anchor from Artifact 3 runs in parallel and is
  consumed next iteration), reuse the full pipeline + knockoff+ gate + kb_engine + trace-graph code from art_vkfyOl2OQNVx
  (read from the run tree). EXECUTE THE PROBABILISTIC UPGRADE per art_Cr6L9JpoewZi Part C: swap the deterministic backward-chaining
  query for ProbLog get_evaluatable().create_from(PrologString).evaluate() -> {Term:prob}; map each admitted clause to a weighted
  clause p_i::fact with p_i = calibrate(Z_i) under the gate-consistent-shrinkage mapping (1-alpha_hat)*p_i (default; per-pair
  W_i-margin weight as the alternative), and use entrapment FDP_hat as a consistency prior; emit PROBABILISTIC trace-graphs
  (JSON + Graphviz DOT) with per-node MARGINAL probabilities AND every leaf carrying provenance span + decoy certificate (W_i,
  T, alpha) + entrapment certificate (FDP_hat, r), on >= 1 document per genre. Deterministic backward-chaining REMAINS the
  required baseline so no headline number depends on ProbLog; if ProbLog cannot install/run in the environment, fall back
  to a pure-Python weighted AND/OR semiring evaluator that REPRODUCES ProbLog marginals on these small proof DAGs and report
  it as a faithful ProbLog-equivalent, so the probabilistic layer is DEMONSTRATED either way (and the contribution -- not
  only the limitation -- can state the probabilistic reasoner is delivered). FINALIZE HONEST APPLICATION REPORTING: recompute
  the multi-hop corruption result (RAW-KB vs GATE-KB at alpha=0.5) WITH document-block bootstrap CIs and an EXPLICIT flag
  that the drop (0.48->0.18) is regulatory-genre-driven (legal already 0.0, news derives 0), reporting per-system derived-conclusion
  counts; report the pooled atomic hallucinated-fact reduction (gate 0.183 self-consistency / 0.178 logprob vs raw 0.243)
  across BOTH elicitations x ALL alpha with CIs and STATE PLAINLY at the point of claim that it is DIRECTIONAL and not CI-separated
  at n=24 (0/40 cells), demonstrated as a trend with auditable provenance; carry the CONSERVATIVE self-report finding (decoy_fdr_hat
  >= realized in all cells, contrasting the CLUTRR anti-conservative regime). Emit figure-ready arrays + FULL FIGURE CAPTIONS.
  method_out.json schema-valid. Log cumulative LLM cost after EVERY call (this is largely a reanalysis + ProbLog run on cached
  scores); soft cap ~$1, HARD STOP at $10.
depends_on:
- id: art_UBTwyePql8NQ
  label: dataset
  relation_type:
  relation_rationale:
- id: art_Cr6L9JpoewZi
  label: problog-spec
  relation_type:
  relation_rationale:
- id: art_K6AE23HoGqe6
  label: pipeline
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

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
out_expected_files:
- research_out.json
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

### [2] HUMAN-USER prompt · 2026-06-16 10:41:15 UTC

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
