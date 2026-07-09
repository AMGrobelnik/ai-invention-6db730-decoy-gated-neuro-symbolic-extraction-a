# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 04:44:09 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_research_1
```

### [2] SYSTEM-USER prompt · 2026-06-16 04:44:15 UTC

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
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

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
  A Label-Free FDR Knob at the Text-to-Logic Admission Boundary via Plausibility-Matched Decoy Competition: Calibration Validated
  on CLUTRR, Operational Hallucination-Reduction on Re-DocRED, Robustified Against Score-Dependence
hypothesis: |-
  MECHANISM (one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  THE GATE. For each candidate i, form the competition statistic W_i = score(real_i) - score(decoy_i). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. Validity rests on the null sign-flip property; we test it in the tail (not as a marginal average) and protect it against two LLM-specific dependence channels (threat table below).

  TWO ANCHORS (clean division of labor). (A) CLUTRR (free, deterministic, CRISP gold) hosts the CALIBRATION-VALIDITY claim and the single primary disconfirmation: does realized FDR track target alpha (the diagonal)? (B) Re-DocRED (human-annotated, open-vocabulary, 96 relation types, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS claim (atomic-fact precision/recall and hallucinated-conclusion rate vs baselines at matched recall), the genuine schema-alignment bridge test, and the document-level predictive model S5. CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful; the two are never conflated.

  THREE NUMBERS (stated once). (1) Demonstrable-alpha range: alpha in [0.05, 0.5]; the knockoff+ '+1' offset gives a minimum estimable FDR ~1/k at k admissions. (2) Confirmatory corpus: 120 CLUTRR docs + 120 Re-DocRED docs (>=4 clusters) + ~15 illustrative legal/news/story docs (non-confirmatory trace demo). (3) Labels: ZERO labels for operation; gold used only for validation, charged symmetrically against any labeled baseline's calibration labels.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent; populability-gated). Pre-registered on the CLUTRR candidate family Phase-0 shows is POPULABLE -- yielding >= N_false_min (pre-registered, default 40) genuine false admissions pooled at alpha*. Default family: MULTI-HOP inferred kinship relations, where extraction errors are dense; atomic facts over the closed kinship vocabulary are typically too clean to populate the diagonal. Under isolated provenance-blinded scoring at alpha*, the central control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. If NO CLUTRR family reaches N_false_min even after false-real enrichment (extractor over-generation + harder long-chain splits), the diagonal is declared UNTESTABLE at this difficulty and reported as a precondition outcome -- never as 'confirmed by conservatism'.

  CLAIM CHAIN (each row independently testable; a break is localized and reported).
  | # | CLAIM | TEST | PASS CRITERION |
  |---|-------|------|----------------|
  | S0 | Score separation (precondition) | Pilot: selected elicitation separates entailed vs non-entailed in the UPPER TAIL; isolated~batched agree on a labeled slice | tail-AUC>0.5 with CI; isolated~batched |
  | S1 | Decoy signature (mechanism) | Tail-conditioned win-rate among above-cutoff matched pairs + upper-tail two-sample CDF test | counterfactual decoys ~0.5; random swaps anti-conservative |
  | S2 | Calibration validity (CLUTRR) | Sweep alpha; realized FDR vs crisp gold; document-block-bootstrap CI on the diagonal, on the populable family | diagonal tracked within tau above the 1/k floor |
  | S3 | Entrapment corroboration | Independent tail-matched entrapment; combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E); entrapment passes its own tail-difficulty diagnostic | bound agrees with decoy-FDR and gold |
  | S4 | Operational wedge (Re-DocRED) | Matched-recall PR + hallucinated-conclusion rate vs PLAIN CONFIDENCE-THRESHOLD gate (primary zero-label comparator), CoT, RAG, and labeled Mohri-Hashimoto conformal | decoy-gating beats plain thresholding at equal zero labels; competitive with labeled conformal |
  | S5 | Document-level predictive account (Re-DocRED) | Predict per-document tail-exchangeability gap from doc/score features; leave-one-cluster-out + leave-one-document-out CV; pre-registered GAP-regression power analysis | out-of-sample predictive IFF >= N_min held-out units; else DESCRIPTIVE |
  | S6 | Predictable propagation (preliminary) | Tightening alpha lowers multi-hop hallucinated-conclusion rate | direction + rough magnitude |

  SCORE-DEPENDENCE ROBUSTNESS (threat table).
  | THREAT | HOW IT BREAKS THE NULL SIGN-FLIP PROPERTY | MITIGATION | PRE-REGISTERED TEST |
  |--------|-------------------------------------------|------------|---------------------|
  | Within-document score-noise correlation | pooled null signs become dependent; variance/floor understated (anti-conservative) | treat DOCUMENT as a block; document-block bootstrap for all FDP CIs; never i.i.d.-pool signs | block-bootstrap CI is the CI used by the primary disconfirmation |
  | Batched-scoring contrast effects | model implicitly detects the fabricated item and depresses decoy scores (FDP optimistic) | ISOLATED, provenance-blinded, order-randomized scoring as default | isolated-vs-batched check = discriminator: isolation restores diagonal => artifact; persists => genuine non-exchangeability |
  | Upper-tail overconfidence | verbalized confidence fails to separate entailed vs non-entailed exactly where admissions occur | Phase-0 selects elicitation by tail-AUC (verbalized / logprob / self-consistency / DINCO-style) | tail-AUC>0.5 with CI; budget gated on pilot |
  | Decoy too easy / contamination | non-tail-matched decoys make FDR optimistic; an actually-entailed decoy biases FDR conservative (safe side) | document-conditioned counterfactual decoys; non-entailment check; report contamination | tail-conditioned win-rate ~0.5; contamination sensitivity analysis |

  BUDGET ARITHMETIC (isolated default, shown explicitly). Confirmatory scoring items = 240 docs x ~20 candidates x 3 item-types (real + decoy + entrapment at r=1) ~= 14.4K isolated scoring calls; + ~0.7K extraction/decoy/entrapment-generation calls; + Phase-0 pilot. At ~450 input + ~30 output tokens/call this is ~7-15M tokens (candidate-count-dependent). At a sub-$0.30/M model this is ~$2-6 RAW; DOCUMENT-PREFIX PROMPT CACHING -- the ~60 item-scoring calls sharing one document context re-use a cached prefix (cache read ~0.1x) -- cuts input ~3-5x, projecting ~$1-3. Cumulative cost logged after every call; HARD STOP at $10. Isolated scoring is the DEFAULT for 100% of the confirmatory set (caching, not batching, buys the headroom); batching is used only in the labeled isolated-vs-batched sensitivity slice.

  BUDGET WATERFALL (ordering visible). Spend in strict priority order: (i) Phase-0 pilot (gates everything); (ii) fully power the CLUTRR calibration diagonal; (iii) fully power the Re-DocRED operational wedge; (iv) ONLY with leftover budget and ONLY if (ii) and (iii) clear their pre-registered power thresholds: S5 predictive model, S6 propagation, TDC-SB/UB and '+1'-floor relaxation, exploratory rule gating. The headline cannot be starved by secondary exploration.

  SHARED OPERATIONAL CONSTRUCT (Re-DocRED, the fair-mapping fix). All systems target the SAME object: (head-entity, Re-DocRED-relation, tail-entity) triples over the document's annotated entities, scored against human gold triples. A single fixed claim-decomposition + relation-alignment step maps EVERY system's raw output into this triple space identically -- neuro-symbolic admitted facts/bridges, the plain confidence-threshold gate, CoT free-text answers, RAG answers, and labeled-conformal filtered claims. Matched recall is enforced by sweeping each system's own score to a common recall operating point; precision and hallucinated-conclusion rate are compared there with document-block-bootstrap CIs. The wedge is isolated as decoy-gating vs PLAIN THRESHOLDING under identical zero labels; labeled conformal is the labeled reference point.

  SCOPE. Facts AND bridges carry the headline. CLUTRR bridges are crisp (deterministic kinship) and host the diagonal; Re-DocRED bridges are open-vocabulary relation-to-schema alignments and host the operational and predictive claims. Defeasible bridges, implicit common-sense rule gating, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S6 are preliminary / if-budget-permits.
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
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: research_iter1_dir3
type: research
objective: >-
  Deliver an implementation-ready specification of the FDR gate and its scalar inputs: exact knockoff+/TDC thresholding and
  the '+1' floor, the valid entrapment combined estimator, the document-block bootstrap, plausibility-matched decoy design,
  and the best label-free UPPER-TAIL score elicitation callable via OpenRouter -- so the Phase-0 pilot and CLUTRR calibration
  experiment can be coded directly without further design choices.
approach: >-
  Web-research and synthesize into concrete formulas + pseudo-procedures: (a) knockoff+ thresholding -- the most-permissive-cutoff
  rule with estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) and the 1/k minimum-estimable-FDR floor (Barber & Candes
  2015; He/Ebadi/Keich on whether the '+1' is needed, arXiv 2204.13248), and the tighter TDC-SB/UB bounds (Ebadi et al., arXiv
  2302.11837); (b) the valid entrapment combined UPPER bound FDP_hat = N_E(1+1/r)/(N_T+N_E) and why the naive 'sample' estimator
  is flawed (Wen et al., Nature Methods 2025, FDRBench), including how the ratio r propagates into variance and the achievable-alpha
  floor; (c) the document-block bootstrap procedure for all FDP/FDR CIs under within-document score dependence (resample whole
  documents, not candidates); (d) the null sign-flip property statement and its two LLM-specific anti-conservative failure
  modes (within-document score correlation; batched-scoring contrast effects) with the isolated-vs-batched discriminator logic;
  (e) plausibility/property-matched decoy generation -- the DeepCoy principle that decoys must reproduce the false-positive
  score distribution (not be 'too easy'), document-conditioned counterfactual construction, and non-entailment verification;
  (f) candidate UPPER-TAIL label-free elicitations -- verbalized confidence, token-logprob-derived scores, self-consistency,
  DINCO distractor-normalized confidence (arXiv 2509.25532), FactSelfCheck (arXiv 2503.17229) -- with reported tail-calibration
  behavior; (g) which sub-$0.30/M OpenRouter models expose token logprobs AND support prompt caching (for the document-prefix
  caching that makes default isolated scoring affordable), with current pricing. Output concrete formulas, a recommended elicitation
  shortlist for the pilot to test, and a short novelty-positioning note confirming no prior work applies knockoff/target-decoy
  FDR control at an LLM neuro-symbolic admission boundary.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

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
  "description": "Plan for a RESEARCH artifact.",
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
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 04:44:15 UTC

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

### [4] ASSISTANT · 2026-06-16 04:44:35 UTC

```
I'll research the key technical references to make this plan concrete and actionable. Let me start by loading the web tools and checking the user uploads folder.
```

### [5] TOOL CALL — ToolSearch · 2026-06-16 04:44:35 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-06-16 04:44:35 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [7] TOOL CALL — Glob · 2026-06-16 04:44:35 UTC

```
Pattern: "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads/**"
```

### [8] TOOL RESULT — Glob · 2026-06-16 04:44:35 UTC

```
{"filenames": [], "durationMs": 24, "numFiles": 0, "truncated": false}
```

### [9] ASSISTANT · 2026-06-16 04:44:41 UTC

```
No user uploads. Let me research the key technical references in parallel to ground the plan.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 04:44:41 UTC

```
Barber Candes 2015 knockoff filter FDR knockoff+ threshold formula 1 + #{Wj <= -t}
```

### [11] TOOL CALL — WebSearch · 2026-06-16 04:44:41 UTC

```
Wen Freestone Keich Noble 2025 Nature Methods entrapment FDR tandem mass spectrometry combined estimator
```

### [12] TOOL CALL — WebSearch · 2026-06-16 04:44:41 UTC

```
He Ebadi Keich "Controlling the FDR via competition is the +1 needed" arXiv 2204.13248
```

### [13] TOOL CALL — WebSearch · 2026-06-16 04:44:41 UTC

```
DINCO distractor-normalized confidence LLM hallucination arXiv 2509.25532
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 04:44:47 UTC

```
{"query": "He Ebadi Keich \"Controlling the FDR via competition is the +1 needed\" arXiv 2204.13248", "results": [{"tool_use_id": "srvtoolu_01HQJyH4FgNAbNKhGf9Hwsz8", "content": [{"title": "Competition-based control of the false discovery proportion", "url": "https://arxiv.org/pdf/2011.11939"}, {"title": "Grouped Competition Test with Unified False Discovery Rate Control", "url": "https://arxiv.org/html/2512.00901"}, {"title": "[2204.13248] Controlling the False Discovery Rate via Competition: is the +1 needed?", "url": "https://arxiv.org/abs/2204.13248"}, {"title": "[2302.11837] Bounding the FDP in competition-based control of the FDR", "url": "https://arxiv.org/abs/2302.11837"}, {"title": "Controlling the False Discovery Rate via Competition: is the +1 needed? - ADS", "url": "https://ui.adsabs.harvard.edu/abs/2022arXiv220413248R/abstract"}, {"title": "Controlling the False Discovery Rate via Competition: is the +1 needed?", "url": "https://arxiv.org/pdf/2204.13248"}, {"title": "[2011.11939] Competition-based control of the false discovery proportion", "url": "https://arxiv.org/abs/2011.11939"}, {"title": "Competition-Based Control of the False Discovery Proportion | Biometrics | Oxford Academic", "url": "https://doi.org/10.1111/biom.13830"}, {"title": "Multiple Competition-Based FDR Control and Its Application to Peptide Detection | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-030-45257-5_4"}]}, "I found the paper you're looking for! Here's the information about it:\n\n**Title:** Controlling the False Discovery Rate via Competition: is the +1 needed?\n\n**Authors:** Andrew Rajchert and Uri Keich from the School of Mathematics and Statistics, The University of Sydney\n\n**arXiv ID:** 2204.13248\n\n**Abstract:** Barber and Candès (2015) control of the FDR in feature selection relies on estimating the FDR by the number of knockoff wins +1 divided by the number of original wins. The authors study the necessity of the +1 in general settings.\n\nThe paper examines a fundamental question about the \"+1\" correction term used in competition-based false discovery rate (FDR) control methods, investigating whether this adjustment is truly necessary across different scenarios."], "durationSeconds": 5.248928021000004, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 04:44:47 UTC

```
{"query": "Barber Candes 2015 knockoff filter FDR knockoff+ threshold formula 1 + #{Wj <= -t}", "results": [{"tool_use_id": "srvtoolu_01GbMexMqxH7Xyr3618fSwjV", "content": [{"title": "The Knockoff Filter for Controlled Variable Selection", "url": "https://cran.r-project.org/web/packages/knockoff/knockoff.pdf"}, {"title": "Spatial Knockoff Bayesian Variable Selection in Genome-Wide Association   Studies", "url": "https://arxiv.org/pdf/2408.10401"}, {"title": "Bayesian Knockoff Filter", "url": "https://arxiv.org/pdf/2102.05223"}, {"title": "Panning for Gold: Model-X Knockoffs for High-dimensional Controlled   Variable Selection", "url": "https://arxiv.org/pdf/1610.02351"}, {"title": "Stability of a Generalized Debiased Lasso with Applications to   Resampling-Based Variable Selection", "url": "https://arxiv.org/pdf/2405.03063"}, {"title": "Adjusting the Benjamini-Hochberg method for controlling the false   discovery rate in knockoff assisted variable selection", "url": "https://arxiv.org/pdf/2102.09080"}, {"title": "A knockoff filter for high-dimensional selective inference", "url": "https://candes.su.domains/publications/downloads/HD_Knockoffs.pdf"}, {"title": "Sparse minimum Redundancy Maximum Relevance for feature selection", "url": "https://arxiv.org/pdf/2508.18901"}, {"title": "Knockoffs (statistics)", "url": "https://en.wikipedia.org/wiki/Knockoffs_(statistics)"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full"}]}, "I found relevant information about the Barber and Candès 2015 knockoff filter and the threshold formula. Here are the key results:\n\n## Knockoff+ Threshold Formula\n\nBarber and Candès (2015) proved the optimal threshold $t^*$ is given by: $$t^* = \\min \\left\\{ t \\in (0,1) : \\frac{1 + \\#\\{j : W_j \\leqslant -t\\}}{\\#\\{j : W_j \\geqslant t\\} \\lor 1} \\leqslant q \\right\\}$$\n\nThis is the **knockoff+** version of the threshold formula. The numerator includes the \"+1\" term, which increments the count of negative statistics. This threshold controls the expected number of false discoveries while maintaining FDR control.\n\n## Related Knockoff Formula\n\nThere is also a slightly different formulation without the \"+1\" term: $$T^* = \\min \\left\\{ t \\in \\mathcal{W} : \\frac{\\#\\{j : W_j \\le -t\\}}{\\#\\{j : W_j \\ge t\\} \\lor 1} \\le \\alpha \\right\\}$$ This version controls a slightly different measure called \"modified FDR\".\n\n## Key Results\n\nThe knockoff+ controls the FDR, and the knockoff controls a slight modification of the FDR, at the level q. The FDR control is exact even in finite sample settings regardless of the design or covariates, the number of variables in the model, or the noise to signal ratio."], "durationSeconds": 7.347613401000002, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-06-16 04:44:49 UTC

```
{"query": "Wen Freestone Keich Noble 2025 Nature Methods entrapment FDR tandem mass spectrometry combined estimator", "results": [{"tool_use_id": "srvtoolu_012qyev2mzRamGW9XaPNFE6S", "content": [{"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}, {"title": "GitHub - Noble-Lab/FDRBench: Estimation of false discovery proportion for mass spectrometry proteomics data using entrapment · GitHub", "url": "https://github.com/Noble-Lab/FDRBench"}, {"title": "(PDF) Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.researchgate.net/publication/392730664_Assessment_of_false_discovery_rate_control_in_tandem_mass_spectrometry_analysis_using_entrapment"}, {"title": "Reinvestigating the Correctness of Decoy-Based False Discovery Rate Control in Proteomics Tandem Mass Spectrometry - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/38687997/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2024.06.01.596967v2"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | Nature Methods", "url": "https://www.nature.com/articles/s41592-025-02719-x"}, {"title": "Analysis of Tandem Mass Spectrometry Data with CONGA: Combining Open and Narrow Searches with Group-Wise Analysis | Journal of Proteome Research", "url": "https://pubs.acs.org/doi/10.1021/acs.jproteome.3c00399"}, {"title": "How to Train a Postprocessor for Tandem Mass Spectrometry Proteomics Database Search While Maintaining Control of the False Discovery Rate | Journal of Proteome Research", "url": "https://pubs.acs.org/doi/10.1021/acs.jproteome.4c00742"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12240826/"}]}, "Based on the search results, I found the paper you're looking for:\n\nWen, B., Freestone, J., Riffle, M. et al. published \"Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment\" in Nature Methods 22, 1454–1463 (2025).\n\nThe paper presents a theoretical foundation for entrapment methods, along with a method that enables more accurate evaluation of false discovery rate (FDR) control in proteomics mass spectrometry analysis pipelines. \n\nThe FDRBench tool provides two main functions: (1) build entrapment databases using randomly shuffled target sequences or using sequences from foreign species, and (2) estimate the false discovery proportion (FDP) using the lower bound, combined, and paired methods.\n\nThe evaluation of popular data-dependent acquisition tools indicates that these generally seem to control the FDR, but data-independent acquisition tools exhibit inconsistent control of the FDR at both the peptide and protein levels."], "durationSeconds": 8.215692974999998, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-06-16 04:44:49 UTC

```
{"query": "DINCO distractor-normalized confidence LLM hallucination arXiv 2509.25532", "results": [{"tool_use_id": "srvtoolu_01XKQ2AYBXzNhoUP9KbaTgPG", "content": [{"title": "[2509.25532] Calibrating Verbalized Confidence with Self-Generated Distractors", "url": "https://arxiv.org/abs/2509.25532"}, {"title": "Calibrating Verbalized Confidence with Self-Generated Distractors", "url": "https://arxiv.org/html/2509.25532"}, {"title": "Calibrating Verbalized Confidence with Self-Generated Distractors", "url": "https://arxiv.org/pdf/2509.25532"}, {"title": "Beyond the Black Box: A Statistical Model for LLM Reasoning and   Inference", "url": "https://arxiv.org/pdf/2402.03175"}, {"title": "Quantifying the uncertainty of LLM hallucination spreading in complex adaptive social networks", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11252443/"}, {"title": "Eliminating Hallucination-Induced Errors in LLM Code Generation with Functional Clustering", "url": "https://arxiv.org/html/2506.11021v1"}]}, "Based on the search results, I found the paper you're looking for. Here's what the research is about:\n\nCalibrated confidence estimates are necessary for large language model outputs to be trusted by human users. While LLMs can express their confidence in human-interpretable ways, verbalized LLM-generated confidence scores have been found to be miscalibrated, reporting high confidence on instances with low accuracy.\n\nThe researchers hypothesize that this overconfidence stems from an LLM's heightened suggestibility when faced with claims it encodes little information about. They introduce Distractor-Normalized Coherence (DINCO), which estimates and accounts for an LLM's suggestibility bias by having the model verbalize its confidence independently across several self-generated distractors (alternative claims), and normalizes by the total verbalized confidence.\n\nThe paper (arXiv:2509.25532) was published on February 27, 2026, and is authored by Victor Wang and Elias Stengel-Eskin from The University of Texas at Austin. The full paper is available on arXiv in multiple formats (abstract, HTML, and PDF)."], "durationSeconds": 7.938934732999998, "searchCount": 1}
```

### [18] ASSISTANT · 2026-06-16 04:45:03 UTC

```
Key references confirmed. Now let me verify the entrapment estimator details, decoy generation, and OpenRouter model capabilities.
```

### [19] TOOL CALL — WebSearch · 2026-06-16 04:45:03 UTC

```
Ebadi Keich "Bounding the FDP in competition-based control" TDC-SB TDC-UB arXiv 2302.11837
```

### [20] TOOL CALL — WebSearch · 2026-06-16 04:45:03 UTC

```
DeepCoy property-matched decoy generation Bioinformatics 2021 reproduce score distribution
```

### [21] TOOL CALL — WebSearch · 2026-06-16 04:45:03 UTC

```
FactSelfCheck zero-resource per-fact hallucination score sampling consistency arXiv 2503.17229
```

### [22] TOOL CALL — WebSearch · 2026-06-16 04:45:03 UTC

```
OpenRouter models that expose token logprobs and support prompt caching pricing 2026
```

### [23] TOOL RESULT — WebSearch · 2026-06-16 04:45:07 UTC

```
{"query": "Ebadi Keich \"Bounding the FDP in competition-based control\" TDC-SB TDC-UB arXiv 2302.11837", "results": [{"tool_use_id": "srvtoolu_01MNrXV57ymoydX16wVovtsp", "content": [{"title": "[2302.11837] Bounding the FDP in competition-based control of the FDR", "url": "https://arxiv.org/abs/2302.11837"}, {"title": "Bounding the FDP in competition-based control of the FDR", "url": "https://arxiv.org/pdf/2302.11837"}, {"title": "bandsfdp: Compute Upper Prediction Bounds on the FDP in Competition-Based Setups", "url": "https://cran.r-project.org/web/packages/bandsfdp/index.html"}, {"title": "Bounding the FDP in competition-based control of the FDR", "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2302.11837"}, {"title": "R: Uniform Band", "url": "https://search.r-project.org/CRAN/refmans/bandsfdp/html/tdc_ub.html"}, {"title": "Competition-Based Control of the False Discovery Proportion | Biometrics | Oxford Academic", "url": "https://doi.org/10.1111/biom.13830"}, {"title": "[2011.11939] Competition-based control of the false discovery proportion", "url": "https://arxiv.org/abs/2011.11939"}, {"title": "Competition‐based control of the false discovery proportion - Luo - 2023 - Biometrics - Wiley Online Library", "url": "https://onlinelibrary.wiley.com/doi/full/10.1111/biom.13830"}, {"title": "Multiple Competition-Based FDR Control and Its Application to Peptide Detection | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-030-45257-5_4"}]}, "I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** \"Bounding the FDP in competition-based control of the FDR\"\n\n**Authors:** Arya Ebadi, Dong Luo, Jack Freestone, William Stafford Noble, and Uri Keich\n\n**ArXiv ID:** 2302.11837\n\n**Publication Date:** February 23, 2023\n\n**Summary:** The paper presents TDC-SB and TDC-UB that provide upper prediction bounds on the FDP in the list of discoveries generated when controlling the FDR using competition. Using simulated and real data, the new procedures offer significantly tighter upper bounds than ones obtained using the recently published approach of Katsevich and Ramdas, even when the latter is further improved using the interpolation concept of Goeman et al.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2302.11837, and there is also an R package called `bandsfdp` that implements the methods described in the paper."], "durationSeconds": 6.484792277, "searchCount": 1}
```

### [24] TOOL RESULT — WebSearch · 2026-06-16 04:45:11 UTC

```
{"query": "FactSelfCheck zero-resource per-fact hallucination score sampling consistency arXiv 2503.17229", "results": [{"tool_use_id": "srvtoolu_015VFfqXvAmdphUcsqt2Bdqf", "content": [{"title": "[2503.17229] FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs", "url": "https://arxiv.org/abs/2503.17229"}, {"title": "FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs", "url": "https://arxiv.org/html/2503.17229"}, {"title": "(PDF) FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs", "url": "https://www.researchgate.net/publication/390114432_FactSelfCheck_Fact-Level_Black-Box_Hallucination_Detection_for_LLMs"}, {"title": "Fact-Level Black-Box Hallucination Detection for LLMs", "url": "https://aclanthology.org/2026.findings-eacl.296.pdf"}, {"title": "Do LLM hallucination detectors suffer from low-resource effect?", "url": "https://arxiv.org/pdf/2601.16766"}, {"title": "SelfCheck-Eval: A Multi-Module Framework for Zero-Resource Hallucination Detection in Large Language Models", "url": "https://arxiv.org/pdf/2502.01812"}, {"title": "Computer Science Mar 2025", "url": "https://arxiv.org/list/cs/2025-03?skip=8525&show=25"}]}, "I found the paper! Here's what the search revealed:\n\nFactSelfCheck is a novel zero-resource black-box sampling-based method that enables fine-grained fact-level detection for hallucinations in Large Language Models. \n\nThe approach represents long-form text as interpretable knowledge graphs consisting of facts in the form of triples, and computes fine-grained hallucination scores without requiring external resources or training data by analyzing factual consistency across multiple LLM responses.\n\nThe fact-level approach significantly improves hallucination correction, achieving a 35.5% increase in factual content compared to the baseline, while sentence-level SelfCheckGPT yields only a 10.6% improvement.\n\nThe paper (arXiv 2503.17229) was authored by Albert Sawczyn and colleagues from Wrocław University of Science and Technology and University of Technology Sydney. The authors also contribute FavaMultiSamples, a novel dataset that addresses a gap in the field by providing the research community with a second dataset for evaluating sampling-based methods."], "durationSeconds": 8.962347493000001, "searchCount": 1}
```

### [25] TOOL RESULT — WebSearch · 2026-06-16 04:45:11 UTC

```
{"query": "OpenRouter models that expose token logprobs and support prompt caching pricing 2026", "results": [{"tool_use_id": "srvtoolu_01NLdiE5KGFqLAkuuHGNhQnv", "content": [{"title": "OpenRouter Pricing Guide 2026: Complete Cost Analysis | PromptCost.org", "url": "https://promptcost.org/en/blog/openrouter-pricing-guide-2026/"}, {"title": "Prompt Caching | Reduce AI Model Costs with OpenRouter | OpenRouter | Documentation", "url": "https://openrouter.ai/docs/guides/best-practices/prompt-caching"}, {"title": "OpenRouter Pricing Calculator & Cost Guide (Jun 2026)", "url": "https://costgoat.com/pricing/openrouter"}, {"title": "OpenRouter API Pricing 2026: Full Breakdown of Rates, Tiers, and Usage Costs - ZenMux", "url": "https://zenmux.ai/blog/openrouter-api-pricing-2026-full-breakdown-of-rates-tiers-and-usage-costs"}, {"title": "OpenRouter Models Pricing Calculator | Compare Model Costs Instantly", "url": "https://invertedstone.com/calculators/openrouter-pricing"}, {"title": "Usage Accounting - Track AI Model Token Usage", "url": "https://openrouter.ai/docs/cookbook/administration/usage-accounting"}, {"title": "www.educative.io", "url": "https://www.educative.io/courses/openrouter-fundamentals/gkmz0j7GQNk"}]}, "Based on the search results, I found information about OpenRouter's prompt caching support and pricing in 2026, but the results don't specifically detail which models expose token logprobs. Here's what I found:\n\n## Prompt Caching Support\n\nCache reads are charged at 0.25x or 0.50x the price of the original input pricing depending on the model. The usage object in API responses includes detailed cache metrics in the prompt_tokens_details field, including cached_tokens (tokens read from cache) and cache_write_tokens (tokens written to cache).\n\n## Models Supporting Prompt Caching\n\nThe search results mention that prompt caching with OpenAI is automated and does not require any additional configuration, and prompt caching with Grok is automated with cached tokens charged at 0.25x the original input token cost. Additionally, only certain Gemini models support caching, with details in Google's Gemini API Pricing Documentation.\n\n## Pricing Overview\n\nThe cheapest models are DeepSeek V3 at $0.01/M tokens, followed by Gemini 1.5 Flash at $0.075/M, and GPT-4o-mini at $0.15/M.\n\nHowever, the search results don't specifically identify which OpenRouter models expose token logprobs. You may need to check the OpenRouter API documentation directly for a complete list of models with logprobs support."], "durationSeconds": 8.619936938999999, "searchCount": 1}
```

### [26] TOOL RESULT — WebSearch · 2026-06-16 04:45:11 UTC

```
{"query": "DeepCoy property-matched decoy generation Bioinformatics 2021 reproduce score distribution", "results": [{"tool_use_id": "srvtoolu_012KkfC7qtxarzYFNQoghFt7", "content": [{"title": "Generating property-matched decoy molecules using deep learning - ORA - Oxford University Research Archive", "url": "https://ora.ox.ac.uk/objects/uuid:bc03af13-709f-445a-952e-ba6a08537baf"}, {"title": "Generating property-matched decoy molecules using deep learning | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/37/15/2134/6126797"}, {"title": "GitHub - fimrie/DeepCoy", "url": "https://github.com/fimrie/DeepCoy/tree/master"}, {"title": "GitHub - fimrie/DeepCoy · GitHub", "url": "https://github.com/fimrie/DeepCoy"}, {"title": "Generating property-matched decoy molecules using deep learning - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/33532838/"}, {"title": "GitHub - oxpig/DeepCoy · GitHub", "url": "https://github.com/oxpig/DeepCoy"}, {"title": "Generating property-matched decoy molecules using deep learning - ADS", "url": "https://ui.adsabs.harvard.edu/abs/2021Bioin..37.2134I/abstract"}, {"title": "Generating property-matched decoy molecules using deep learning", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8352508/"}, {"title": "(PDF) Generating Property-Matched Decoy Molecules Using Deep Learning", "url": "https://www.researchgate.net/publication/349040218_Generating_Property-Matched_Decoy_Molecules_Using_Deep_Learning"}]}, "I found comprehensive information about the DeepCoy paper. Here are the search results:\n\n## Overview\n\nDeepCoy is a deep learning method using graph neural networks that generates decoys to a user's preferred specification. The paper was authored by Fergus Imrie, Anthony R Bradley, and Charlotte M Deane, published in Bioinformatics, Volume 37, Issue 15, August 2021, Pages 2134–2141.\n\n## Motivation\n\nThe paper addresses the problem that decoy molecules in commonly used sets are biased, meaning methods often exploit these biases to separate actives and decoys rather than learn to perform molecular recognition.\n\n## Key Results\n\nFor all 102 DUD-E targets and 80 of the 81 DEKOIS 2.0 targets, the generated decoy molecules more closely matched the active molecules' physicochemical properties while introducing no discernible additional risk of false negatives.\n\nThe DeepCoy decoys improved the Deviation from Optimal Embedding (DOE) score by an average of 81% and 66%, respectively, decreasing from 0.166 to 0.032 for DUD-E and from 0.109 to 0.038 for DEKOIS 2.0.\n\n## Availability\n\nThe code is available at https://github.com/oxpig/DeepCoy, and generated molecules can be downloaded from http://opig.stats.ox.ac.uk/resources."], "durationSeconds": 10.013050632999999, "searchCount": 1}
```

### [27] ASSISTANT · 2026-06-16 04:45:31 UTC

```
I have all key references confirmed. Let me extract the exact entrapment estimator formulas and OpenRouter caching specifics — the two most load-bearing technical details for the spec.
```

### [28] TOOL CALL — WebFetch · 2026-06-16 04:45:31 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/
Prompt: Extract the exact mathematical formulas for FDP estimation using entrapment: (1) the lower bound estimator, (2) the combined estimator, (3) the paired estimator. Define every symbol (N_T, N_E, r, entrapment-to-target ratio). Explain precisely why the naive "sample" entrapment estimator is flawed/biased, and how the entrapment-to-target ratio r enters the formula. Quote the equations verbatim if possible.
```

### [29] TOOL CALL — WebFetch · 2026-06-16 04:45:31 UTC

```
URL: https://openrouter.ai/docs/guides/best-practices/prompt-caching
Prompt: Which model providers/models support prompt caching on OpenRouter, what is the cache read cost multiplier (e.g. 0.1x, 0.25x, 0.5x) for each, and is caching automatic or does it require explicit cache_control markers? Also note anything about which models support logprobs in the API.
```

### [30] TOOL RESULT — WebFetch · 2026-06-16 04:45:31 UTC

```
{"bytes": 276539, "code": 200, "codeText": "OK", "result": "# FDP Estimation Formulas in Entrapment Analysis\n\n## The Three Main Estimators\n\n### 1. Lower Bound Estimator\n**Formula:** FDP̂ = N_ℰ / (N_𝒯 + N_ℰ)\n\nThis method estimates FDP among target+entrapment discoveries by counting entrapment hits directly.\n\n### 2. Combined Estimator\n**Formula:** FDP̂ = N_ℰ(1 + 1/r) / (N_𝒯 + N_ℰ)\n\nThis incorporates the entrapment-to-target ratio r, providing a theoretically sound upper bound.\n\n### 3. Paired Estimator\n**Formula:** FDP̂* = [N_ℰ + N_ℰ≥s>𝒯 + 2·N_ℰ>𝒯≥s] / (N_𝒯 + N_ℰ)\n\nThis leverages target-entrapment pairing for tighter bounds.\n\n## Symbol Definitions\n\n- **N_𝒯**: Count of original target discoveries\n- **N_ℰ**: Count of entrapment discoveries  \n- **r**: Entrapment-to-target database size ratio (r = |ℰ|/|𝒯|)\n- **s**: Discovery score cutoff threshold\n\n## Why the \"Sample\" Method Fails\n\nThe sample method estimates: FDP̂ = N_ℰ · (1/r) / N_𝒯\n\nThe paper explains that this approach is \"inherently flawed because, while typically underestimating the FDP, it can also overestimate it in some unusual cases.\" It targets the wrong discovery list and ignores the full search space constraints.\n\nThe ratio **r** fundamentally matters: without it, the lower bound formula becomes biased. The combined formula's \"+1/r\" term corrects this distortion, making it theoretically valid for FDR control validation.", "durationMs": 6128, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}
```

### [31] TOOL RESULT — WebFetch · 2026-06-16 04:45:31 UTC

```
{"bytes": 19045, "code": 200, "codeText": "OK", "result": "# Prompt Caching Support on OpenRouter\n\n## Provider Summary\n\n| Provider | Cache Read Multiplier | Automatic? | Notes |\n|----------|----------------------|-----------|-------|\n| **OpenAI** | 0.25x–0.5x | Yes | \"Automated and does not require any additional configuration\" |\n| **Grok** | Variable* | Yes | Automated; specific multiplier not disclosed |\n| **Moonshot AI** | Variable* | Yes | Automated; specific multiplier not disclosed |\n| **Groq** | Variable* | Yes | \"Currently available on Kimi K2 models\" |\n| **Alibaba Qwen** | Variable* | No | \"Requires explicit cache breakpoints\" with `cache_control` |\n| **Anthropic Claude** | 0.9x | No | Offers automatic (top-level) or explicit per-block `cache_control` |\n| **DeepSeek** | Variable* | Yes | Automated; specific multiplier not disclosed |\n| **Google Gemini 2.5** | Variable* | Yes | \"Implicit caching\" works automatically; explicit `cache_control` available |\n\n*Multipliers listed as placeholder variables in the documentation and not specified with exact values.\n\n## Key Distinctions\n\nMost providers enable caching automatically, while **Alibaba and Anthropic** require explicit `cache_control` markers. Anthropic uniquely offers both automatic and explicit modes depending on use case and routing.\n\n**Note:** The documentation provided contains no information about logprobs support across these providers.", "durationMs": 4975, "url": "https://openrouter.ai/docs/guides/best-practices/prompt-caching"}
```

### [32] ASSISTANT · 2026-06-16 04:48:25 UTC

```
I now have all key references and formulas verified. Let me write the detailed research plan.
```

### [33] TOOL CALL — Write · 2026-06-16 04:48:25 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "Implementation-Ready Spec for the Label-Free FDR Gate at the Text-to-Logic Admission Boundary",
  "summary": "A focused web-research plan that produces a single, copy-pasteable specification sheet for every scalar input and procedure of the decoy-competition FDR gate: exact knockoff+/TDC thresholding and the 1/k '+1' floor (Barber & Candes 2015; Rajchert & Keich 2204.13248; Ebadi et al. 2302.11837), the valid entrapment combined/paired estimator and why the naive 'sample' estimator is biased (Wen et al., FDRBench, Nature Methods 2025), the document-block (cluster) bootstrap, the null sign-flip property with its two LLM-specific anti-conservative failure modes and the isolated-vs-batched discriminator, plausibility/property-matched decoy design (DeepCoy principle + document-conditioned counterfactuals + non-entailment check), an upper-tail-calibration-ranked shortlist of label-free elicitations (verbalized confidence, token-logprob, self-consistency/SelfCheckGPT, DINCO 2509.25532, FactSelfCheck 2503.17229), and a recommended sub-$0.30/M OpenRouter model (with two fallbacks) that exposes the capabilities actually required (logprobs and/or prompt caching) with current pricing — plus a short novelty-positioning note. Output enables Phase-0 and the CLUTRR calibration experiment to be coded with no further design decisions.",
  "runpod_compute_profile": "cpu_light",
  "question": "What are the exact, implementation-ready formulas, default scalar values, and OpenRouter configuration needed to build the label-free FDR gate at the LLM text-to-logic admission boundary — (a) knockoff+/TDC thresholding with the '+1' / 1/k minimum-estimable-FDR floor, (b) the valid entrapment combined/paired estimator (and why the naive 'sample' estimator is flawed) with how the ratio r enters variance and the achievable-alpha floor, (c) the document-block bootstrap for FDP/FDR CIs under within-document score dependence, (d) the null sign-flip property statement plus its two LLM-specific anti-conservative failure modes and the isolated-vs-batched discriminator logic, (e) plausibility/property-matched decoy generation (DeepCoy principle, document-conditioned counterfactual construction, non-entailment verification), (f) a ranked shortlist of label-free UPPER-TAIL score elicitations with reported tail-calibration behavior, and (g) a sub-$0.30/M OpenRouter model exposing token logprobs and/or prompt caching with current pricing — so the Phase-0 pilot and the CLUTRR calibration diagonal can be coded without further design choices?",
  "research_plan": "## 0. Framing, deliverable contract, and constraints\n\nThis is a PURE WEB-RESEARCH artifact (no code execution, no dataset downloads). The deliverable is a single consolidated **specification sheet** that a later method-executor can code from directly. Produce BOTH:\n- `research_out.json` with `{answer, sources, follow_up_questions}` where `answer` is the full spec (formulas, defaults, pseudocode blocks, the elicitation shortlist, the model recommendation, and the novelty note) rendered as structured markdown text;\n- `research_report.md` — the same spec laid out as a readable report with one section per sub-task (A–G) plus the novelty note and a final 'Parameter Defaults' table.\n\nDo NOT re-derive the statistics from scratch; EXTRACT the exact published formulas verbatim, define every symbol, and translate each into a short language-agnostic pseudo-procedure. Every numeric formula MUST be traceable to a cited primary source. Where a value is a free design parameter (alpha grid, tolerance tau, N_false_min, bootstrap replicate count B, entrapment ratio r), state a recommended default AND its justification.\n\nPrimary sources are already located (use these exact URLs first; the executor may discover more):\n- Barber & Candes 2015, 'Controlling the false discovery rate via knockoffs', Annals of Statistics 43(5): https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full ; CRAN vignette https://cran.r-project.org/web/packages/knockoff/knockoff.pdf ; Wikipedia overview https://en.wikipedia.org/wiki/Knockoffs_(statistics)\n- Rajchert & Keich 2022, 'Controlling the FDR via competition: is the +1 needed?', arXiv 2204.13248: https://arxiv.org/abs/2204.13248 and PDF https://arxiv.org/pdf/2204.13248\n- Ebadi, Luo, Freestone, Noble & Keich 2023, 'Bounding the FDP in competition-based control of the FDR' (TDC-SB / TDC-UB), arXiv 2302.11837: https://arxiv.org/abs/2302.11837 ; R package `bandsfdp`: https://cran.r-project.org/web/packages/bandsfdp/index.html and https://search.r-project.org/CRAN/refmans/bandsfdp/html/tdc_ub.html\n- Wen, Freestone, Riffle, Noble & Keich 2025, FDRBench / entrapment, Nature Methods 22:1454-1463: open PMC copy https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/ ; Nature https://www.nature.com/articles/s41592-025-02719-x ; code https://github.com/Noble-Lab/FDRBench\n- DeepCoy: Imrie, Bradley & Deane 2021, Bioinformatics 37(15):2134: https://academic.oup.com/bioinformatics/article/37/15/2134/6126797 ; code https://github.com/oxpig/DeepCoy\n- DINCO (Distractor-Normalized Coherence): arXiv 2509.25532: https://arxiv.org/abs/2509.25532 and HTML https://arxiv.org/html/2509.25532\n- FactSelfCheck: arXiv 2503.17229: https://arxiv.org/abs/2503.17229 ; EACL-Findings 2026 PDF https://aclanthology.org/2026.findings-eacl.296.pdf\n- OpenRouter prompt caching: https://openrouter.ai/docs/guides/best-practices/prompt-caching ; OpenRouter parameters / supported-parameters docs (for the `logprobs`/`top_logprobs` parameter and per-model support) — search openrouter.ai/docs for 'parameters', 'logprobs', and 'supported parameters'.\n\nWorkflow per source: web search to confirm the canonical URL -> web fetch to understand structure -> **fetch_grep** for exact equations, symbol definitions, and numbers (especially in PDFs). The garbled outputs typical of lossy fetch (e.g. a '+1/r' vs '(1+1/r)' ambiguity) MUST be resolved by fetch_grep against the PDF/PMC full text — do not trust a paraphrase for any equation that ends up in the spec.\n\n---\n\n## A. knockoff+/TDC thresholding and the '+1' / 1/k floor\n\n1. From Barber & Candes 2015 (fetch_grep the PDF/Annals page for 'knockoff+', 'data-dependent threshold', 'W_j'), extract VERBATIM:\n   - the data statistic definition W_j and its antisymmetry/flip-sign requirement;\n   - the **knockoff+** threshold: t = min{ t in W : (1 + #{j : W_j <= -t}) / max(1, #{j : W_j >= t}) <= q }, selected set S = {j : W_j >= t}; and the plain **knockoff** threshold (drop the +1, controls modified FDR). State which controls FDR vs mFDR.\n   Map the hypothesis's notation exactly: estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}); admit {i : W_i >= t} at the most permissive (smallest) t with estimate <= alpha.\n2. Derive and state the **minimum-estimable-FDR floor**: with k admissions and zero negatives the estimate equals (1+0)/k = 1/k, so target alpha is only attainable when k >= 1/alpha (alpha=0.05 -> >=20 admissions; alpha=0.1 -> >=10; alpha=0.5 -> >=2). This sets the demonstrable-alpha grid and the per-(facts/bridges)-per-anchor admission-count requirement. Recommend the alpha grid {0.05, 0.1, 0.2, 0.3, 0.5} from the hypothesis and tie each grid point to its k-floor.\n3. From Rajchert & Keich 2204.13248 extract: WHEN the '+1' can be dropped/relaxed without losing validity and the magnitude of the conservativeness the '+1' induces at small k (this is what the 'leftover-budget +1-floor relaxation' experiment would exploit). State the precise conditions/claims, not a vibe.\n4. From Ebadi et al. 2302.11837 extract the TDC-SB and TDC-UB upper-prediction-bound procedures (and that `bandsfdp` implements them); summarize their inputs (the same W signs/competition counts) and what tighter bound they give vs Katsevich-Ramdas. Mark these as the 'leftover-budget' tightening, not the headline. Note the R package as a reference implementation the method-executor can port to Python.\n5. PSEUDO-PROCEDURE to emit: `knockoff_plus_threshold(W[], alpha) -> (t, admitted_set, fdr_estimate)` scanning candidate cutoffs over sorted |W| values.\n\n## B. Valid entrapment combined/paired estimator and the ratio r\n\n1. From Wen et al. FDRBench (fetch_grep PMC11185562 and the Nature Methods text for 'combined', 'paired', 'lower bound', 'sample', 'entrapment-to-target ratio', 'N_E', 'N_T'), extract VERBATIM all three FDP estimators and define every symbol. Confirmed forms to verify exactly against the PDF:\n   - Lower bound: FDP_hat = N_E / (N_T + N_E)\n   - **Combined (the one the hypothesis uses): FDP_hat = N_E (1 + 1/r) / (N_T + N_E)** — confirm the grouping is (1 + 1/r), NOT 1 + 1/r outside, and confirm r = |entrapment set| / |target set| (database-size ratio), distinct from the admitted counts.\n   - Paired: FDP_hat* = [N_E + N_{E>=s>T} + 2 N_{E>T>=s}] / (N_T + N_E) (or the paper's exact paired form) — extract precisely; note it requires target-entrapment pairing and is tighter; r=1 paired is the tightest case.\n2. Extract the paper's EXACT argument for why the naive 'sample' estimator (FDP_hat = N_E (1/r) / N_T) is flawed/biased (it targets the wrong discovery list / ignores search-space constraints; typically underestimates but can overestimate). Quote it.\n3. Explain how r PROPAGATES: (i) into the point estimate via (1+1/r); (ii) into variance (smaller r -> fewer entrapment items -> higher variance of N_E -> wider CI); (iii) into the achievable-alpha floor (entrapment-based certificate cannot certify below ~ its own granularity). Recommend r=1 as default (tightest paired form, matches the hypothesis's r=1 entrapment-at-one item) and state the variance/cost trade-off of r>1.\n4. PSEUDO-PROCEDURE: `entrapment_fdp(N_T, N_E, r, estimator in {lower, combined, paired}) -> FDP_hat`. State that the gate uses decoy-competition for ADMISSION and entrapment as an INDEPENDENT corroborating upper bound (construction-independence — entrapment built by a mechanism distinct from decoys), comparing the two against gold.\n\n## C. Document-block (cluster) bootstrap for all FDP/FDR CIs\n\n1. State the threat being addressed: within-document LLM scoring-noise correlation makes i.i.d.-pooled W signs dependent, understating variance/floor (anti-conservative). Therefore resample WHOLE DOCUMENTS (blocks/clusters), not individual candidates.\n2. Specify the procedure concretely: for b in 1..B, sample documents WITH replacement to form a resampled corpus; recompute W-sign counts and re-run the knockoff+ threshold + entrapment estimate on the resampled corpus; collect the realized-FDP statistic; report the percentile CI (e.g. 2.5/97.5) and whether it lies entirely on the anti-conservative (above-alpha) side — THIS is the CI used by the primary disconfirmation. Recommend B>=2000 (justify: percentile-CI stability) and note the cluster/block bootstrap lineage (cluster bootstrap, Cameron-Gelbach-Miller; moving/block bootstrap) so the executor cites a methods anchor. Search terms: 'cluster bootstrap confidence interval', 'block bootstrap dependent data', 'pairs cluster bootstrap'.\n3. Note the two granularities needed: leave-one-cluster-out and leave-one-document-out CV for S5 are SEPARATE from the FDP bootstrap; clarify the distinction so the executor does not conflate them.\n4. PSEUDO-PROCEDURE: `doc_block_bootstrap(per_doc_records, statistic_fn, B) -> (point, ci_low, ci_high)`.\n\n## D. Null sign-flip property + two LLM failure modes + isolated-vs-batched discriminator\n\n1. State the null sign-flip property precisely (from Barber & Candes / TDC framing): among genuinely-false candidates, sign(W_i) is an independent fair coin (P=0.5) conditional on |W_i|; equivalently each false real and its matched decoy are exchangeable in the high-score tail. This is the SOLE validity condition; the gate is an empirically-validated calibration, not a theorem, because LLM decoys carry no construction-level proof.\n2. Catalog the TWO anti-conservative failure channels and their mitigations as a table the executor reproduces:\n   - Within-document score correlation -> dependent null signs, understated floor -> mitigation: document-block bootstrap (Sub-task C).\n   - Batched-scoring contrast effects -> model implicitly detects the fabricated item among co-presented candidates and depresses decoy scores -> FDP optimistic -> mitigation: ISOLATED, provenance-blinded, order-randomized scoring as default.\n3. Specify the **isolated-vs-batched discriminator** logic: run a labeled slice under both isolated and batched scoring; if isolation RESTORES the diagonal it was a scoring artifact; if anti-conservatism PERSISTS under isolation it is genuine decoy non-exchangeability. State this is the pre-registered test, and that isolated scoring is the default for 100% of the confirmatory set (caching, not batching, buys the headroom).\n4. State the two tail diagnostics (measurement only, never used by the gate): tail-conditioned win-rate ~0.5 among matched pairs ABOVE the admission cutoff, and an upper-tail two-sample CDF test (e.g. one-sided Kolmogorov-Smirnov or a tail-restricted Mann-Whitney) on real-false vs decoy scores in the admission region. Recommend the exact test and how 'tail' is delimited (scores >= operative cutoff t).\n\n## E. Plausibility / property-matched decoy generation\n\n1. From DeepCoy (Imrie et al. 2021) extract the load-bearing PRINCIPLE (fetch the Bioinformatics article + GitHub README): decoys must REPRODUCE the property/score distribution of the true positives (be property-matched), NOT be 'too easy'; biased/too-easy decoys let the scorer separate on artifacts and make estimated FDR optimistic; quantify with their DOE (Deviation from Optimal Embedding) improvement (0.166->0.032 DUD-E; 0.109->0.038 DEKOIS) as the cautionary evidence. Translate to text: an LLM decoy must reproduce the score distribution of genuine plausible hallucinations.\n2. Specify the PRIMARY decoy family for the gate: **document-conditioned counterfactual decoys** — maximally-plausible, document-NON-entailed facts/bridges drawn from the model's own prior conditioned on the document. Give a concrete generation recipe (LLM prompt template sketch): given a document + a target relation/entity-type schema, produce a fact that is plausible given the genre/entities but NOT entailed by the text. Contrast with the predicted-anti-conservative baseline: **random type-matched swaps** (kept deliberately as the negative control that should read anti-conservative).\n3. Specify the **non-entailment verification** gate every decoy must pass (so an accidentally-entailed decoy does not bias FDR conservatively): an independent entailment check against the document (e.g. NLI-style or a separate isolated LLM call asking 'is this entailed by the text? yes/no'); report contamination rate and run a contamination sensitivity analysis. State the diagnostic target: tail-conditioned win-rate ~0.5 for counterfactual decoys; measurably anti-conservative for random swaps.\n4. PSEUDO-PROCEDURE: `generate_decoy(document, candidate_real) -> decoy` and `verify_non_entailment(document, decoy) -> bool`. Define 'plausibility-matched' as: decoy and real share entity types / surface form / specificity so the only difference is entailment.\n\n## F. Upper-tail label-free score elicitation — ranked shortlist\n\n1. For EACH candidate elicitation, extract from its source the reported calibration behavior SPECIFICALLY in the high-confidence / upper tail (ECE, AUROC, selective-accuracy, overconfidence in the top bin):\n   - **Verbalized confidence** (model states 0-100 / 0-1): document the well-known overconfidence in the upper tail. Anchor sources: Xiong et al. 'Can LLMs Express Their Uncertainty?' (ICLR 2024) and Tian et al. 'Just Ask for Calibration' (EMNLP 2023). Search these.\n   - **Token-logprob-derived score** (sequence/average token logprob, or yes/no token probability for an entailment-framed prompt): note better calibration than verbalized for base models but degradation under RLHF; REQUIRES a model exposing logprobs (ties to Sub-task G).\n   - **Self-consistency / SelfCheckGPT** (Manakul et al. 2023): sample N completions, score by agreement; label-free, no logprobs needed but N x cost.\n   - **DINCO** (2509.25532): verbalize confidence independently across self-generated DISTRACTORS and normalize by total verbalized confidence — directly targets upper-tail overconfidence/suggestibility. Extract its reported calibration gains and the exact normalization formula (fetch_grep the HTML).\n   - **FactSelfCheck** (2503.17229): fact/triple-level black-box consistency scores across sampled responses; extract how the per-fact score is computed. Note its native fact-level granularity matches the gate's per-candidate unit.\n2. RANK the shortlist by (i) reported upper-tail discrimination, (ii) zero-label / black-box feasibility, (iii) per-call cost & whether logprobs are needed, (iv) compatibility with isolated provenance-blinded scoring. Deliver a recommended Phase-0 SHORTLIST (recommend 3-4 to pilot: verbalized as floor baseline, DINCO as the overconfidence-corrected primary candidate, a logprob/yes-no-token variant IF the chosen model exposes logprobs, and self-consistency/FactSelfCheck-style as the sampling option), with the metric Phase-0 should select on: **tail-AUC > 0.5 with CI** on a labeled slice, plus isolated~batched agreement.\n3. Make explicit the COUPLING to Sub-task G: if no affordable model exposes logprobs, the logprob elicitation drops out and DINCO/verbalized/self-consistency carry Phase-0 — state this contingency so the pilot is codeable regardless.\n\n## G. OpenRouter model: logprobs + prompt caching + sub-$0.30/M pricing\n\n1. Resolve the central tension and report it explicitly: cheap auto-caching models (e.g. DeepSeek, Gemini Flash tier) are great for document-prefix caching but token `logprobs` exposure through OpenRouter is uneven; the OpenAI-family (e.g. gpt-4o-mini / gpt-4.1-mini class) reliably exposes `logprobs`/`top_logprobs` and auto-caches at 0.25x-0.5x but verify the per-M price is <$0.30 input. Determine, from OpenRouter docs + per-model pages, a CONCRETE table: model id | input $/M | output $/M | cache-read multiplier | caching auto vs cache_control | logprobs/top_logprobs supported? | notes. Use the supported-parameters listing (search 'openrouter docs supported parameters logprobs') and individual model pages; flag any value that could not be confirmed from docs as 'to verify programmatically by the method-executor'.\n2. From the caching doc (https://openrouter.ai/docs/guides/best-practices/prompt-caching) confirm cache-read multipliers and the auto-vs-explicit behavior per provider (OpenAI/Grok/DeepSeek/Gemini auto; Anthropic & Qwen need explicit `cache_control` breakpoints; Anthropic cache-read ~0.1x but cache-WRITE ~1.25x — verify exact numbers, the lossy fetch gave a suspect 0.9x). Confirm the usage object returns `prompt_tokens_details.cached_tokens` so the method-executor can verify cache hits and log cost.\n3. Validate the budget arithmetic from the hypothesis against the chosen model: ~14.4K isolated scoring calls + ~0.7K generation calls + pilot, ~450 input + ~30 output tokens/call, ~7-15M tokens; with document-prefix caching at the model's cache-read multiplier, project the $ range and confirm it sits in the ~$1-3 zone and well under the $10 HARD CAP. Show the arithmetic.\n4. Deliver a RECOMMENDATION: one primary model + two fallbacks, each tagged with which elicitations (Sub-task F) it enables (logprob-dependent vs logprob-free). If the cheapest-with-caching model lacks logprobs, recommend a logprob-free elicitation as primary so the pipeline is not blocked. State that the method-executor must programmatically confirm logprobs return non-null on a 1-call probe before committing the budget (this is a follow_up_question, not something this research artifact can run).\n\n## H. Novelty-positioning note (short)\n\nWrite a 1-2 paragraph confirmation, grounded in targeted searches, that NO prior work applies knockoff / target-decoy / entrapment FDR control at an LLM neuro-symbolic (text-to-logic) admission boundary. Differentiate against: conformal factuality / coherent factuality / DCF (Mohri-Hashimoto ICML 2024; arXiv 2505.17126; 2604.20098), conformal selection + BH (Jin & Candes JMLR 2023), multiple-testing hallucination detection (Li-Magesh-Veeravalli 2508.18473), online conformal selection (GAIF 2509.03297), LINC / Logic-LM, and ontology-constraint filtering (ODKE+/SHACL) — all are LABELED and/or certify the OUTPUT, none gate the admission boundary label-free via decoy competition. Run 2-3 confirmatory searches ('knockoff filter LLM hallucination', 'target-decoy competition language model fact extraction', 'FDR control neuro-symbolic admission') to ensure no 2025-2026 preprint pre-empts the claim; report anything close.\n\n---\n\n## Output requirements & contingencies\n\n- `answer` (in research_out.json): the full spec — for EACH of A-G a (i) verbatim formula/statement with source, (ii) symbol glossary, (iii) pseudo-procedure, (iv) recommended default(s) — plus the elicitation shortlist, the OpenRouter model table + recommendation, and the novelty note.\n- `sources`: every URL actually used, grouped by sub-task.\n- `follow_up_questions`: surface the items only the method-executor can resolve at runtime (e.g. 'does the chosen model return non-null logprobs on a probe call?', 'does cache_control yield measured cached_tokens > 0?').\n- A final **Parameter Defaults table** with recommended values + justification: alpha grid {0.05,0.1,0.2,0.3,0.5}; tolerance tau (recommend a small absolute slack, e.g. 0.05, justify); N_false_min=40 (from hypothesis); entrapment ratio r=1 (paired, tightest); bootstrap B>=2000; self-consistency N (if used); tail cutoff = operative knockoff+ t.\n- CONTINGENCY 1 (paywall/lossy fetch on an equation): use fetch_grep on the open PMC / arXiv PDF; if still blocked, fall back to the CRAN `knockoff` / `bandsfdp` vignettes and the FDRBench GitHub README, which restate the formulas. Never ship a paraphrased equation.\n- CONTINGENCY 2 (no sub-$0.30/M model exposes logprobs + caching): explicitly recommend the logprob-FREE path (DINCO/verbalized/self-consistency on a cheap auto-caching model) as primary and document that logprob elicitation is optional/secondary.\n- CONTINGENCY 3 (a near-miss novelty hit found): report it in the novelty note with the precise difference rather than suppressing it.\n- Keep the report self-contained and code-ready: a method-executor reading only research_report.md should be able to implement Phase-0 + the CLUTRR calibration diagonal with zero additional literature lookup.",
  "explanation": "The hypothesis's entire headline — a label-free FDR knob at the text-to-logic admission boundary — stands or falls on getting the statistical machinery EXACTLY right: the knockoff+ threshold and its 1/k floor set which alpha values are even demonstrable and how many admissions each requires; the entrapment combined/paired estimator (and the documented flaw in the naive 'sample' estimator) is the independent corroboration of the decoy-FDR; the document-block bootstrap is literally the CI used by the single primary disconfirmation; the null sign-flip property and the isolated-vs-batched discriminator define what 'validity' means here; property-matched (counterfactual) decoys are the difference between a calibrated knob and an optimistic one; and the upper-tail elicitation + the OpenRouter model choice (logprobs vs caching vs <$0.30/M) jointly gate the Phase-0 budget release and the whole confirmatory run. This artifact has no dependencies and is on the critical path: the Phase-0 pilot and the CLUTRR calibration experiment cannot be coded until these formulas, defaults, the elicitation shortlist, and a concrete model are pinned down. Producing one consolidated, source-traceable spec sheet (with every equation verbatim and a pseudo-procedure per component) converts a pile of cross-domain papers into something a method-executor can implement directly, and the novelty note protects the contribution claim before any compute is spent."
}
```

### [34] TOOL RESULT — Write · 2026-06-16 04:48:25 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Implementation-Ready Spec for the Label-Free FDR Gate at the Text-to-Logic Admission Boundary\",\n  \"summary\": \"A focused web-research plan that produces a single, copy-pasteable specification sheet for every scalar input and procedure of the decoy-competition FDR gate: exact knockoff+/TDC thresholding and the 1/k '+1' floor (Barber & Candes 2015; Rajchert & Keich 2204.13248; Ebadi et al. 2302.11837), the valid entrapment combined/paired estimator and why the naive 'sample' estimator is biased (Wen et al., FDRBench, Nature Methods 2025), the document-block (cluster) bootstrap, the null sign-flip property with its two LLM-specific anti-conservative failure modes and the isolated-vs-batched discriminator, plausibility/property-matched decoy design (DeepCoy principle + document-conditioned counterfactuals + non-entailment check), an upper-tail-calibration-ranked shortlist of label-free elicitations (verbalized confidence, token-logprob, self-consistency/SelfCheckGPT, DINCO 2509.25532, FactSelfCheck 2503.17229), and a recommended sub-$0.30/M OpenRouter model (with two fallbacks) that exposes the capabilities actually required (logprobs and/or prompt caching) with current pricing — plus a short novelty-positioning note. Output enables Phase-0 and the CLUTRR calibration experiment to be coded with no further design decisions.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"What are the exact, implementation-ready formulas, default scalar values, and OpenRouter configuration needed to build the label-free FDR gate at the LLM text-to-logic admission boundary — (a) knockoff+/TDC thresholding with the '+1' / 1/k minimum-estimable-FDR floor, (b) the valid entrapment combined/paired estimator (and why the naive 'sample' estimator is flawed) with how the ratio r enters variance and the achievable-alpha floor, (c) the document-block bootstrap for FDP/FDR CIs under within-document score dependence, (d) the null sign-flip property statement plus its two LLM-specific anti-conservative failure modes and the isolated-vs-batched discriminator logic, (e) plausibility/property-matched decoy generation (DeepCoy principle, document-conditioned counterfactual construction, non-entailment verification), (f) a ranked shortlist of label-free UPPER-TAIL score elicitations with reported tail-calibration behavior, and (g) a sub-$0.30/M OpenRouter model exposing token logprobs and/or prompt caching with current pricing — so the Phase-0 pilot and the CLUTRR calibration diagonal can be coded without further design choices?\",\n  \"research_plan\": \"## 0. Framing, deliverable contract, and constraints\\n\\nThis is a PURE WEB-RESEARCH artifact (no code execution, no dataset downloads). The deliverable is a single consolidated **specification sheet** that a later method-executor can code from directly. Produce BOTH:\\n- `research_out.json` with `{answer, sources, follow_up_questions}` where `answer` is the full spec (formulas, defaults, pseudocode blocks, the elicitation shortlist, the model recommendation, and the novelty note) rendered as structured markdown text;\\n- `research_report.md` — the same spec laid out as a readable report with one section per sub-task (A–G) plus the novelty note and a final 'Parameter Defaults' table.\\n\\nDo NOT re-derive the statistics from scratch; EXTRACT the exact published formulas verbatim, define every symbol, and translate each into a short language-agnostic pseudo-procedure. Every numeric formula MUST be traceable to a cited primary source. Where a value is a free design parameter (alpha grid, tolerance tau, N_false_min, bootstrap replicate count B, entrapment ratio r), state a recommended default AND its justification.\\n\\nPrimary sources are already located (use these exact URLs first; the executor may discover more):\\n- Barber & Candes 2015, 'Controlling the false discovery rate via knockoffs', Annals of Statistics 43(5): https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full ; CRAN vignette https://cran.r-project.org/web/packages/knockoff/knockoff.pdf ; Wikipedia overview https://en.wikipedia.org/wiki/Knockoffs_(statistics)\\n- Rajchert & Keich 2022, 'Controlling the FDR via competition: is the +1 needed?', arXiv 2204.13248: https://arxiv.org/abs/2204.13248 and PDF https://arxiv.org/pdf/2204.13248\\n- Ebadi, Luo, Freestone, Noble & Keich 2023, 'Bounding the FDP in competition-based control of the FDR' (TDC-SB / TDC-UB), arXiv 2302.11837: https://arxiv.org/abs/2302.11837 ; R package `bandsfdp`: https://cran.r-project.org/web/packages/bandsfdp/index.html and https://search.r-project.org/CRAN/refmans/bandsfdp/html/tdc_ub.html\\n- Wen, Freestone, Riffle, Noble & Keich 2025, FDRBench / entrapment, Nature Methods 22:1454-1463: open PMC copy https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/ ; Nature https://www.nature.com/articles/s41592-025-02719-x ; code https://github.com/Noble-Lab/FDRBench\\n- DeepCoy: Imrie, Bradley & Deane 2021, Bioinformatics 37(15):2134: https://academic.oup.com/bioinformatics/article/37/15/2134/6126797 ; code https://github.com/oxpig/DeepCoy\\n- DINCO (Distractor-Normalized Coherence): arXiv 2509.25532: https://arxiv.org/abs/2509.25532 and HTML https://arxiv.org/html/2509.25532\\n- FactSelfCheck: arXiv 2503.17229: https://arxiv.org/abs/2503.17229 ; EACL-Findings 2026 PDF https://aclanthology.org/2026.findings-eacl.296.pdf\\n- OpenRouter prompt caching: https://openrouter.ai/docs/guides/best-practices/prompt-caching ; OpenRouter parameters / supported-parameters docs (for the `logprobs`/`top_logprobs` parameter and per-model support) — search openrouter.ai/docs for 'parameters', 'logprobs', and 'supported parameters'.\\n\\nWorkflow per source: web search to confirm the canonical URL -> web fetch to understand structure -> **fetch_grep** for exact equations, symbol definitions, and numbers (especially in PDFs). The garbled outputs typical of lossy fetch (e.g. a '+1/r' vs '(1+1/r)' ambiguity) MUST be resolved by fetch_grep against the PDF/PMC full text — do not trust a paraphrase for any equation that ends up in the spec.\\n\\n---\\n\\n## A. knockoff+/TDC thresholding and the '+1' / 1/k floor\\n\\n1. From Barber & Candes 2015 (fetch_grep the PDF/Annals page for 'knockoff+', 'data-dependent threshold', 'W_j'), extract VERBATIM:\\n   - the data statistic definition W_j and its antisymmetry/flip-sign requirement;\\n   - the **knockoff+** threshold: t = min{ t in W : (1 + #{j : W_j <= -t}) / max(1, #{j : W_j >= t}) <= q }, selected set S = {j : W_j >= t}; and the plain **knockoff** threshold (drop the +1, controls modified FDR). State which controls FDR vs mFDR.\\n   Map the hypothesis's notation exactly: estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}); admit {i : W_i >= t} at the most permissive (smallest) t with estimate <= alpha.\\n2. Derive and state the **minimum-estimable-FDR floor**: with k admissions and zero negatives the estimate equals (1+0)/k = 1/k, so target alpha is only attainable when k >= 1/alpha (alpha=0.05 -> >=20 admissions; alpha=0.1 -> >=10; alpha=0.5 -> >=2). This sets the demonstrable-alpha grid and the per-(facts/bridges)-per-anchor admission-count requirement. Recommend the alpha grid {0.05, 0.1, 0.2, 0.3, 0.5} from the hypothesis and tie each grid point to its k-floor.\\n3. From Rajchert & Keich 2204.13248 extract: WHEN the '+1' can be dropped/relaxed without losing validity and the magnitude of the conservativeness the '+1' induces at small k (this is what the 'leftover-budget +1-floor relaxation' experiment would exploit). State the precise conditions/claims, not a vibe.\\n4. From Ebadi et al. 2302.11837 extract the TDC-SB and TDC-UB upper-prediction-bound procedures (and that `bandsfdp` implements them); summarize their inputs (the same W signs/competition counts) and what tighter bound they give vs Katsevich-Ramdas. Mark these as the 'leftover-budget' tightening, not the headline. Note the R package as a reference implementation the method-executor can port to Python.\\n5. PSEUDO-PROCEDURE to emit: `knockoff_plus_threshold(W[], alpha) -> (t, admitted_set, fdr_estimate)` scanning candidate cutoffs over sorted |W| values.\\n\\n## B. Valid entrapment combined/paired estimator and the ratio r\\n\\n1. From Wen et al. FDRBench (fetch_grep PMC11185562 and the Nature Methods text for 'combined', 'paired', 'lower bound', 'sample', 'entrapment-to-target ratio', 'N_E', 'N_T'), extract VERBATIM all three FDP estimators and define every symbol. Confirmed forms to verify exactly against the PDF:\\n   - Lower bound: FDP_hat = N_E / (N_T + N_E)\\n   - **Combined (the one the hypothesis uses): FDP_hat = N_E (1 + 1/r) / (N_T + N_E)** — confirm the grouping is (1 + 1/r), NOT 1 + 1/r outside, and confirm r = |entrapment set| / |target set| (database-size ratio), distinct from the admitted counts.\\n   - Paired: FDP_hat* = [N_E + N_{E>=s>T} + 2 N_{E>T>=s}] / (N_T + N_E) (or the paper's exact paired form) — extract precisely; note it requires target-entrapment pairing and is tighter; r=1 paired is the tightest case.\\n2. Extract the paper's EXACT argument for why the naive 'sample' estimator (FDP_hat = N_E (1/r) / N_T) is flawed/biased (it targets the wrong discovery list / ignores search-space constraints; typically underestimates but can overestimate). Quote it.\\n3. Explain how r PROPAGATES: (i) into the point estimate via (1+1/r); (ii) into variance (smaller r -> fewer entrapment items -> higher variance of N_E -> wider CI); (iii) into the achievable-alpha floor (entrapment-based certificate cannot certify below ~ its own granularity). Recommend r=1 as default (tightest paired form, matches the hypothesis's r=1 entrapment-at-one item) and state the variance/cost trade-off of r>1.\\n4. PSEUDO-PROCEDURE: `entrapment_fdp(N_T, N_E, r, estimator in {lower, combined, paired}) -> FDP_hat`. State that the gate uses decoy-competition for ADMISSION and entrapment as an INDEPENDENT corroborating upper bound (construction-independence — entrapment built by a mechanism distinct from decoys), comparing the two against gold.\\n\\n## C. Document-block (cluster) bootstrap for all FDP/FDR CIs\\n\\n1. State the threat being addressed: within-document LLM scoring-noise correlation makes i.i.d.-pooled W signs dependent, understating variance/floor (anti-conservative). Therefore resample WHOLE DOCUMENTS (blocks/clusters), not individual candidates.\\n2. Specify the procedure concretely: for b in 1..B, sample documents WITH replacement to form a resampled corpus; recompute W-sign counts and re-run the knockoff+ threshold + entrapment estimate on the resampled corpus; collect the realized-FDP statistic; report the percentile CI (e.g. 2.5/97.5) and whether it lies entirely on the anti-conservative (above-alpha) side — THIS is the CI used by the primary disconfirmation. Recommend B>=2000 (justify: percentile-CI stability) and note the cluster/block bootstrap lineage (cluster bootstrap, Cameron-Gelbach-Miller; moving/block bootstrap) so the executor cites a methods anchor. Search terms: 'cluster bootstrap confidence interval', 'block bootstrap dependent data', 'pairs cluster bootstrap'.\\n3. Note the two granularities needed: leave-one-cluster-out and leave-one-document-out CV for S5 are SEPARATE from the FDP bootstrap; clarify the distinction so the executor does not conflate them.\\n4. PSEUDO-PROCEDURE: `doc_block_bootstrap(per_doc_records, statistic_fn, B) -> (point, ci_low, ci_high)`.\\n\\n## D. Null sign-flip property + two LLM failure modes + isolated-vs-batched discriminator\\n\\n1. State the null sign-flip property precisely (from Barber & Candes / TDC framing): among genuinely-false candidates, sign(W_i) is an independent fair coin (P=0.5) conditional on |W_i|; equivalently each false real and its matched decoy are exchangeable in the high-score tail. This is the SOLE validity condition; the gate is an empirically-validated calibration, not a theorem, because LLM decoys carry no construction-level proof.\\n2. Catalog the TWO anti-conservative failure channels and their mitigations as a table the executor reproduces:\\n   - Within-document score correlation -> dependent null signs, understated floor -> mitigation: document-block bootstrap (Sub-task C).\\n   - Batched-scoring contrast effects -> model implicitly detects the fabricated item among co-presented candidates and depresses decoy scores -> FDP optimistic -> mitigation: ISOLATED, provenance-blinded, order-randomized scoring as default.\\n3. Specify the **isolated-vs-batched discriminator** logic: run a labeled slice under both isolated and batched scoring; if isolation RESTORES the diagonal it was a scoring artifact; if anti-conservatism PERSISTS under isolation it is genuine decoy non-exchangeability. State this is the pre-registered test, and that isolated scoring is the default for 100% of the confirmatory set (caching, not batching, buys the headroom).\\n4. State the two tail diagnostics (measurement only, never used by the gate): tail-conditioned win-rate ~0.5 among matched pairs ABOVE the admission cutoff, and an upper-tail two-sample CDF test (e.g. one-sided Kolmogorov-Smirnov or a tail-restricted Mann-Whitney) on real-false vs decoy scores in the admission region. Recommend the exact test and how 'tail' is delimited (scores >= operative cutoff t).\\n\\n## E. Plausibility / property-matched decoy generation\\n\\n1. From DeepCoy (Imrie et al. 2021) extract the load-bearing PRINCIPLE (fetch the Bioinformatics article + GitHub README): decoys must REPRODUCE the property/score distribution of the true positives (be property-matched), NOT be 'too easy'; biased/too-easy decoys let the scorer separate on artifacts and make estimated FDR optimistic; quantify with their DOE (Deviation from Optimal Embedding) improvement (0.166->0.032 DUD-E; 0.109->0.038 DEKOIS) as the cautionary evidence. Translate to text: an LLM decoy must reproduce the score distribution of genuine plausible hallucinations.\\n2. Specify the PRIMARY decoy family for the gate: **document-conditioned counterfactual decoys** — maximally-plausible, document-NON-entailed facts/bridges drawn from the model's own prior conditioned on the document. Give a concrete generation recipe (LLM prompt template sketch): given a document + a target relation/entity-type schema, produce a fact that is plausible given the genre/entities but NOT entailed by the text. Contrast with the predicted-anti-conservative baseline: **random type-matched swaps** (kept deliberately as the negative control that should read anti-conservative).\\n3. Specify the **non-entailment verification** gate every decoy must pass (so an accidentally-entailed decoy does not bias FDR conservatively): an independent entailment check against the document (e.g. NLI-style or a separate isolated LLM call asking 'is this entailed by the text? yes/no'); report contamination rate and run a contamination sensitivity analysis. State the diagnostic target: tail-conditioned win-rate ~0.5 for counterfactual decoys; measurably anti-conservative for random swaps.\\n4. PSEUDO-PROCEDURE: `generate_decoy(document, candidate_real) -> decoy` and `verify_non_entailment(document, decoy) -> bool`. Define 'plausibility-matched' as: decoy and real share entity types / surface form / specificity so the only difference is entailment.\\n\\n## F. Upper-tail label-free score elicitation — ranked shortlist\\n\\n1. For EACH candidate elicitation, extract from its source the reported calibration behavior SPECIFICALLY in the high-confidence / upper tail (ECE, AUROC, selective-accuracy, overconfidence in the top bin):\\n   - **Verbalized confidence** (model states 0-100 / 0-1): document the well-known overconfidence in the upper tail. Anchor sources: Xiong et al. 'Can LLMs Express Their Uncertainty?' (ICLR 2024) and Tian et al. 'Just Ask for Calibration' (EMNLP 2023). Search these.\\n   - **Token-logprob-derived score** (sequence/average token logprob, or yes/no token probability for an entailment-framed prompt): note better calibration than verbalized for base models but degradation under RLHF; REQUIRES a model exposing logprobs (ties to Sub-task G).\\n   - **Self-consistency / SelfCheckGPT** (Manakul et al. 2023): sample N completions, score by agreement; label-free, no logprobs needed but N x cost.\\n   - **DINCO** (2509.25532): verbalize confidence independently across self-generated DISTRACTORS and normalize by total verbalized confidence — directly targets upper-tail overconfidence/suggestibility. Extract its reported calibration gains and the exact normalization formula (fetch_grep the HTML).\\n   - **FactSelfCheck** (2503.17229): fact/triple-level black-box consistency scores across sampled responses; extract how the per-fact score is computed. Note its native fact-level granularity matches the gate's per-candidate unit.\\n2. RANK the shortlist by (i) reported upper-tail discrimination, (ii) zero-label / black-box feasibility, (iii) per-call cost & whether logprobs are needed, (iv) compatibility with isolated provenance-blinded scoring. Deliver a recommended Phase-0 SHORTLIST (recommend 3-4 to pilot: verbalized as floor baseline, DINCO as the overconfidence-corrected primary candidate, a logprob/yes-no-token variant IF the chosen model exposes logprobs, and self-consistency/FactSelfCheck-style as the sampling option), with the metric Phase-0 should select on: **tail-AUC > 0.5 with CI** on a labeled slice, plus isolated~batched agreement.\\n3. Make explicit the COUPLING to Sub-task G: if no affordable model exposes logprobs, the logprob elicitation drops out and DINCO/verbalized/self-consistency carry Phase-0 — state this contingency so the pilot is codeable regardless.\\n\\n## G. OpenRouter model: logprobs + prompt caching + sub-$0.30/M pricing\\n\\n1. Resolve the central tension and report it explicitly: cheap auto-caching models (e.g. DeepSeek, Gemini Flash tier) are great for document-prefix caching but token `logprobs` exposure through OpenRouter is uneven; the OpenAI-family (e.g. gpt-4o-mini / gpt-4.1-mini class) reliably exposes `logprobs`/`top_logprobs` and auto-caches at 0.25x-0.5x but verify the per-M price is <$0.30 input. Determine, from OpenRouter docs + per-model pages, a CONCRETE table: model id | input $/M | output $/M | cache-read multiplier | caching auto vs cache_control | logprobs/top_logprobs supported? | notes. Use the supported-parameters listing (search 'openrouter docs supported parameters logprobs') and individual model pages; flag any value that could not be confirmed from docs as 'to verify programmatically by the method-executor'.\\n2. From the caching doc (https://openrouter.ai/docs/guides/best-practices/prompt-caching) confirm cache-read multipliers and the auto-vs-explicit behavior per provider (OpenAI/Grok/DeepSeek/Gemini auto; Anthropic & Qwen need explicit `cache_control` breakpoints; Anthropic cache-read ~0.1x but cache-WRITE ~1.25x — verify exact numbers, the lossy fetch gave a suspect 0.9x). Confirm the usage object returns `prompt_tokens_details.cached_tokens` so the method-executor can verify cache hits and log cost.\\n3. Validate the budget arithmetic from the hypothesis against the chosen model: ~14.4K isolated scoring calls + ~0.7K generation calls + pilot, ~450 input + ~30 output tokens/call, ~7-15M tokens; with document-prefix caching at the model's cache-read multiplier, project the $ range and confirm it sits in the ~$1-3 zone and well under the $10 HARD CAP. Show the arithmetic.\\n4. Deliver a RECOMMENDATION: one primary model + two fallbacks, each tagged with which elicitations (Sub-task F) it enables (logprob-dependent vs logprob-free). If the cheapest-with-caching model lacks logprobs, recommend a logprob-free elicitation as primary so the pipeline is not blocked. State that the method-executor must programmatically confirm logprobs return non-null on a 1-call probe before committing the budget (this is a follow_up_question, not something this research artifact can run).\\n\\n## H. Novelty-positioning note (short)\\n\\nWrite a 1-2 paragraph confirmation, grounded in targeted searches, that NO prior work applies knockoff / target-decoy / entrapment FDR control at an LLM neuro-symbolic (text-to-logic) admission boundary. Differentiate against: conformal factuality / coherent factuality / DCF (Mohri-Hashimoto ICML 2024; arXiv 2505.17126; 2604.20098), conformal selection + BH (Jin & Candes JMLR 2023), multiple-testing hallucination detection (Li-Magesh-Veeravalli 2508.18473), online conformal selection (GAIF 2509.03297), LINC / Logic-LM, and ontology-constraint filtering (ODKE+/SHACL) — all are LABELED and/or certify the OUTPUT, none gate the admission boundary label-free via decoy competition. Run 2-3 confirmatory searches ('knockoff filter LLM hallucination', 'target-decoy competition language model fact extraction', 'FDR control neuro-symbolic admission') to ensure no 2025-2026 preprint pre-empts the claim; report anything close.\\n\\n---\\n\\n## Output requirements & contingencies\\n\\n- `answer` (in research_out.json): the full spec — for EACH of A-G a (i) verbatim formula/statement with source, (ii) symbol glossary, (iii) pseudo-procedure, (iv) recommended default(s) — plus the elicitation shortlist, the OpenRouter model table + recommendation, and the novelty note.\\n- `sources`: every URL actually used, grouped by sub-task.\\n- `follow_up_questions`: surface the items only the method-executor can resolve at runtime (e.g. 'does the chosen model return non-null logprobs on a probe call?', 'does cache_control yield measured cached_tokens > 0?').\\n- A final **Parameter Defaults table** with recommended values + justification: alpha grid {0.05,0.1,0.2,0.3,0.5}; tolerance tau (recommend a small absolute slack, e.g. 0.05, justify); N_false_min=40 (from hypothesis); entrapment ratio r=1 (paired, tightest); bootstrap B>=2000; self-consistency N (if used); tail cutoff = operative knockoff+ t.\\n- CONTINGENCY 1 (paywall/lossy fetch on an equation): use fetch_grep on the open PMC / arXiv PDF; if still blocked, fall back to the CRAN `knockoff` / `bandsfdp` vignettes and the FDRBench GitHub README, which restate the formulas. Never ship a paraphrased equation.\\n- CONTINGENCY 2 (no sub-$0.30/M model exposes logprobs + caching): explicitly recommend the logprob-FREE path (DINCO/verbalized/self-consistency on a cheap auto-caching model) as primary and document that logprob elicitation is optional/secondary.\\n- CONTINGENCY 3 (a near-miss novelty hit found): report it in the novelty note with the precise difference rather than suppressing it.\\n- Keep the report self-contained and code-ready: a method-executor reading only research_report.md should be able to implement Phase-0 + the CLUTRR calibration diagonal with zero additional literature lookup.\",\n  \"explanation\": \"The hypothesis's entire headline — a label-free FDR knob at the text-to-logic admission boundary — stands or falls on getting the statistical machinery EXACTLY right: the knockoff+ threshold and its 1/k floor set which alpha values are even demonstrable and how many admissions each requires; the entrapment combined/paired estimator (and the documented flaw in the naive 'sample' estimator) is the independent corroboration of the decoy-FDR; the document-block bootstrap is literally the CI used by the single primary disconfirmation; the null sign-flip property and the isolated-vs-batched discriminator define what 'validity' means here; property-matched (counterfactual) decoys are the difference between a calibrated knob and an optimistic one; and the upper-tail elicitation + the OpenRouter model choice (logprobs vs caching vs <$0.30/M) jointly gate the Phase-0 budget release and the whole confirmatory run. This artifact has no dependencies and is on the critical path: the Phase-0 pilot and the CLUTRR calibration experiment cannot be coded until these formulas, defaults, the elicitation shortlist, and a concrete model are pinned down. Producing one consolidated, source-traceable spec sheet (with every equation verbatim and a pseudo-procedure per component) converts a pile of cross-domain papers into something a method-executor can implement directly, and the novelty note protects the contribution claim before any compute is spent.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [35] ASSISTANT · 2026-06-16 04:48:41 UTC

```
The research plan is written to `./.terminal_claude_agent_struct_out.json`.

## What I produced

A detailed plan for a **RESEARCH artifact** that delivers an implementation-ready spec sheet for the FDR gate — so the Phase-0 pilot and CLUTRR calibration experiment can be coded with no further design decisions.

**Grounding done first** (verified all primary sources exist and confirmed the key formulas, rather than hand-waving):
- **knockoff+ threshold** `(1 + #{Wⱼ≤−t}) / max(1,#{Wⱼ≥t}) ≤ q` — confirmed verbatim from Barber & Candès 2015; plus the `+1`-relaxation paper (Rajchert & Keich, 2204.13248) and TDC-SB/UB bounds (Ebadi et al., 2302.11837 + `bandsfdp` R package).
- **Entrapment estimators** — confirmed the combined form `FDP̂ = N_E(1+1/r)/(N_T+N_E)`, the lower-bound and paired forms, and the documented flaw in the naive "sample" estimator (Wen et al. FDRBench, Nature Methods 2025).
- **DeepCoy** property-matched-decoy principle (DOE 0.166→0.032), **DINCO** (2509.25532) and **FactSelfCheck** (2503.17229) elicitations, and the **OpenRouter caching/logprobs tension** (cheap auto-caching models vs reliable logprobs exposure).

**Plan structure** — sections A–G mapping 1:1 to the artifact direction's sub-questions, each requiring a verbatim formula + symbol glossary + pseudo-procedure + recommended default, plus a novelty-positioning note (H) and a Parameter Defaults table.

**Key design calls baked into the plan:**
- Resolve every equation via `fetch_grep` on open PDFs (never ship a paraphrased formula — flagged a suspect "0.9x" cache value from lossy fetch).
- Surfaced the **logprobs-vs-caching contingency**: if no sub-$0.30/M model exposes logprobs, recommend the logprob-free path (DINCO/verbalized/self-consistency on a cheap auto-caching model) so the pipeline is never blocked.
- Distinguished what only the *method*-executor can resolve at runtime (logprobs probe, cache-hit verification) → routed to `follow_up_questions`.

Compute profile: `cpu_light` (pure web research, no execution).
```
