# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 04:44:09 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1
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
You are expanding an artifact direction of type: DATASET

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect
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

The dataset executor has 6h total (including writing code, debugging, testing, and fixing errors).

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

id: dataset_iter1_dir1
type: dataset
objective: >-
  Build the crisp-gold CLUTRR calibration anchor that hosts the calibration-validity diagonal (S2) and the single primary
  disconfirmation, with BOTH atomic-fact and multi-hop inferred-kinship gold plus difficulty splits, so a later experiment
  can measure populability (genuine false-admission counts at alpha*) and enrich false-reals via harder long chains.
approach: >-
  Acquire CLUTRR (Sinha et al., EMNLP 2019; facebookresearch/clutrr generator, or a HuggingFace mirror if available -- the
  generator is rule-based/templated and needs NO LLM). For each story produce a standardized row: document text (the narrative;
  for the multi-hop family prefer longer chains and, where a single story is very short, keep the native length and record
  it -- do not pad artificially), gold ATOMIC kinship facts (relations directly stated in the text, as (head, relation, tail)
  triples), gold MULTI-HOP inferred kinship relations (the query target plus all relations derivable by composition over the
  kinship graph, the error-dense 'populable' family), the full kinship edge-graph for provenance, per-entity gender/type metadata,
  and chain length k as metadata_fold. Include harder long-chain splits (k>=4) explicitly to densify potential false admissions,
  and flag a small labeled pilot slice (a few dozen rows) for Phase-0. Target ~150 confirmatory documents spread across k
  plus the pilot slice. Map everything to the SHARED (head, relation, tail) triple schema used by both anchors, validate with
  aii-json, and split full/mini/preview. Keep total size well under 300MB.
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

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for dataset artifacts:
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
  "description": "Plan for a DATASET artifact.",
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
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
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

### [4] ASSISTANT · 2026-06-16 04:44:43 UTC

```
I'll research CLUTRR to make this plan concrete. Let me start by checking the user uploads folder and loading web tools in parallel.
```

### [5] TOOL CALL — Glob · 2026-06-16 04:44:43 UTC

```
Pattern: "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads/**"
```

### [6] TOOL RESULT — Glob · 2026-06-16 04:44:43 UTC

```
{"filenames": [], "durationMs": 17, "numFiles": 0, "truncated": false}
```

### [7] TOOL CALL — ToolSearch · 2026-06-16 04:44:43 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [8] TOOL RESULT — ToolSearch · 2026-06-16 04:44:43 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [9] ASSISTANT · 2026-06-16 04:44:53 UTC

```
No user uploads. Let me research CLUTRR's structure, HuggingFace availability, and data format in parallel.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 04:44:53 UTC

```
CLUTRR dataset HuggingFace kinship reasoning Sinha 2019
```

### [11] TOOL CALL — WebSearch · 2026-06-16 04:44:53 UTC

```
CLUTRR facebookresearch generator data format columns story query relation
```

### [12] TOOL CALL — WebSearch · 2026-06-16 04:44:53 UTC

```
CLUTRR kinship relations list vocabulary mother father grandmother edge graph
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 04:44:59 UTC

```
{"query": "CLUTRR dataset HuggingFace kinship reasoning Sinha 2019", "results": [{"tool_use_id": "srvtoolu_01L353yGiNEN4bgrmsRy9RbS", "content": [{"title": "GitHub - kliang5/CLUTRR_huggingface_dataset", "url": "https://github.com/kliang5/CLUTRR_huggingface_dataset"}, {"title": "CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Request PDF", "url": "https://www.researchgate.net/publication/336997708_CLUTRR_A_Diagnostic_Benchmark_for_Inductive_Reasoning_from_Text"}, {"title": "Extracting and Following Paths for Robust Relational Reasoning with Large Language Models", "url": "https://arxiv.org/pdf/2412.17963"}, {"title": "Compositional Language Understanding with Text-based Relational   Reasoning", "url": "https://arxiv.org/pdf/1811.02959"}, {"title": "README.md · CLUTRR/v1 at main", "url": "https://huggingface.co/datasets/CLUTRR/v1/blob/main/README.md"}, {"title": "Improved Logical Reasoning of Language Models via Differentiable   Symbolic Programming", "url": "https://arxiv.org/pdf/2305.03742"}, {"title": "PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics", "url": "https://arxiv.org/pdf/2505.23126"}, {"title": "Learning Reasoning Strategies in End-to-End Differentiable Proving", "url": "https://arxiv.org/pdf/2007.06477"}, {"title": "Neural Compositional Rule Learning for Knowledge Graph Reasoning", "url": "https://arxiv.org/pdf/2303.03581"}, {"title": "CLUTRR (CLUTRR)", "url": "https://huggingface.co/CLUTRR"}]}, "Based on the web search results, here's what I found about the CLUTRR dataset:\n\n## Overview\n\nCLUTRR (Compositional Language Understanding and Text-based Relational Reasoning) is a diagnostic benchmark suite introduced by Sinha et al. in 2019 to test the systematic generalization and inductive reasoning capabilities of NLU systems.\n\n## Task Description\n\nCLUTRR contains a large set of semi-synthetic stories involving hypothetical families, and the task is to infer the relationship between two family members, whose relationship is not explicitly mentioned in the given story. The core idea is that, given a text-based story describing a subset of a kinship graph, the goal is to predict the relationship between two entities, whose relationship is not stated in the story.\n\n## Key Features\n\nThe CLUTRR benchmark allows testing a model's ability for systematic generalization by testing on stories that contain unseen combinations of logical rules, and tests for various forms of model robustness by adding different kinds of superfluous noise facts to the stories. To solve this task, a learning agent should be able to induce the logical rules governing the kinship relationships, such as the parent of a parent is a grandparent, and use these rules to infer the relationship between a given pair of entities.\n\n## Availability\n\nThe dataset is available on HuggingFace with citation information for the original 2019 EMNLP paper."], "durationSeconds": 7.704422374000002, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 04:44:59 UTC

```
{"query": "CLUTRR facebookresearch generator data format columns story query relation", "results": [{"tool_use_id": "srvtoolu_01VTecaDU3DmtgKkaReWdn8V", "content": [{"title": "CLUTRR (CLUTRR)", "url": "https://huggingface.co/CLUTRR"}, {"title": "clutrr/clutrr/main.py at main · facebookresearch/clutrr", "url": "https://github.com/facebookresearch/clutrr/blob/main/clutrr/main.py"}, {"title": "clutrr/README.md at main · facebookresearch/clutrr", "url": "https://github.com/facebookresearch/clutrr/blob/main/README.md"}, {"title": "Coupling Large Language Models with Logic Programming for Robust and   General Reasoning from Text", "url": "https://arxiv.org/pdf/2307.07696"}, {"title": "Compositional Language Understanding with Text-based Relational   Reasoning", "url": "https://arxiv.org/pdf/1811.02959"}, {"title": "SGinPG/README.md at master · NicolasAG/SGinPG", "url": "https://github.com/NicolasAG/SGinPG/blob/master/README.md"}, {"title": "GitHub - koustuvsinha/clutrr-workshop · GitHub", "url": "https://github.com/koustuvsinha/clutrr-workshop"}, {"title": "Evaluating Step-by-Step Reasoning through Symbolic Verification", "url": "https://arxiv.org/pdf/2212.08686"}, {"title": "Issues in the AMT templates and how to mitigate them · Issue #15 · facebookresearch/clutrr", "url": "https://github.com/facebookresearch/clutrr/issues/15"}, {"title": "Differentiable Reasoning over Long Stories -- Assessing Systematic   Generalisation in Neural Models", "url": "https://arxiv.org/pdf/2203.10620"}]}, "Based on the search results, here's information about the CLUTRR dataset format and generator:\n\n## CLUTRR Overview\n\nCLUTRR is a benchmark dataset generator to test relational reasoning on text. Given a text-based story describing a subset of a kinship graph, the goal is to predict the relationship between two entities, whose relationship is not stated in the story.\n\n## Data Format and Columns\n\nData samples in CLUTRR consist of a story and a target, where the target contains two entities and the relation that is needed to be inferred, and the story contains available triplets.\n\nBased on the example provided in the search results, the data format includes an id, story, query (with text_query), and target (with text_target) columns. The story contains narrative text about family members, and the query/target contains the relation to be predicted.\n\n## Data Generation Process\n\nEach example story is constructed in steps starting with generating a random kinship graph with nodes representing family members and edges representing relationships between them.\n\n## Task Configuration\n\nTo run a task, you specify train_task and test_tasks in the form of <task_id>.<relation_length>, such as: python main.py --train_tasks 1.3 --test_tasks 1.3,1.4\n\nThe official repository is available at https://github.com/facebookresearch/clutrr."], "durationSeconds": 7.463864409000002, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 04:45:03 UTC

```
{"query": "CLUTRR kinship relations list vocabulary mother father grandmother edge graph", "results": [{"tool_use_id": "srvtoolu_019kKkJXwKs5uPYJ4VXAR8DY", "content": [{"title": "CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text", "url": "https://arxiv.org/pdf/1908.06177"}, {"title": "PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics", "url": "https://arxiv.org/pdf/2505.23126"}, {"title": "Differentiable Reasoning over Long Stories -- Assessing Systematic   Generalisation in Neural Models", "url": "https://arxiv.org/pdf/2203.10620"}, {"title": "Extracting and Following Paths for Robust Relational Reasoning with Large Language Models", "url": "https://arxiv.org/pdf/2412.17963"}, {"title": "Coupling Large Language Models with Logic Programming for Robust and   General Reasoning from Text", "url": "https://arxiv.org/pdf/2307.07696"}, {"title": "From Grandmas to Uncles: Kinship Terms Around the World – Living for Languages", "url": "https://livingforlanguages.wordpress.com/2017/05/16/from-grandmas-to-uncles-kinship-terms-around-the-world/"}, {"title": "Le sens de la famille : analyse du vocabulaire de la parent{\\'e} par les   plongements de mots", "url": "https://arxiv.org/pdf/2406.19729"}, {"title": "Kinship terminology | Anthropology | Research Starters | EBSCO Research", "url": "https://www.ebsco.com/research-starters/anthropology/kinship-terminology"}]}, "Based on the search results, here's comprehensive information about CLUTRR kinship relations:\n\n## CLUTRR Kinship Relations Vocabulary\n\nCLUTRR uses the following kinship relations: son, father, husband, brother, grandson, grandfather, son-in-law, father-in-law, brother-in-law, uncle, nephew, daughter, mother, wife, sister, granddaughter, grandmother, daughter-in-law, mother-in-law, sister-in-law, aunt, and niece.\n\n## Knowledge Base Structure\n\nCLUTRR has two types of predicates: vertical predicates (parent-child relations) and horizontal predicates (sibling or significant other). All vertical predicates are denoted by their child-to-parent relation, with the prefix \"inv-\" appended for the corresponding parent-to-child relation.\n\nFor example, the notation \"[inv-grand,X,Y]\" represents \"X is the grandfather of Y\", while \"[grand,X,Y]\" means \"X's grandfather is Y\".\n\n## Edge Graph and Rules\n\nCLUTRR uses a small, tractable, and logically sound knowledge base of rules selected carefully to avoid ambiguity in resolution. The rules define how different kinship relations can be composed together (such as combining \"child\" and \"sibling\" relations) to derive other kinship relations like \"uncle\" or \"grandmother.\""], "durationSeconds": 9.981053031000004, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 04:45:49 UTC

```
Found the key resource: `CLUTRR/v1` on HuggingFace. Let me fetch its README and the GitHub README for exact format details.
```

### [17] TOOL CALL — WebFetch · 2026-06-16 04:45:49 UTC

```
URL: https://huggingface.co/datasets/CLUTRR/v1/blob/main/README.md
Prompt: Extract the full data format: what columns/fields each example has (story, query, target, clean_story, proof_state, genders, etc.), the available configurations/splits and their names (e.g. relation lengths k=2,3,4...), the kinship relations vocabulary, number of examples, and any details about how the gold supporting facts and the inferred target relation are represented. Quote field names exactly.
```

### [18] TOOL CALL — WebFetch · 2026-06-16 04:45:49 UTC

```
URL: https://github.com/facebookresearch/clutrr/blob/main/README.md
Prompt: Extract details about the CLUTRR data generation: the CSV output columns/fields (story, clean_story, proof_state, query, genders, target, f_comb, etc.), what each field contains, the relation length / chain length k parameter, the kinship relation vocabulary, and how supporting facts and inferred relations are stored. Also note any pre-generated datasets available for download and their file sizes.
```

### [19] TOOL RESULT — WebFetch · 2026-06-16 04:45:49 UTC

```
{"bytes": 138173, "code": 200, "codeText": "OK", "result": "# CLUTRR Dataset Format\n\n## Fields per Example\nEach instance contains: \"id\", \"story\", \"query\", \"target\", \"target_text\", \"clean_story\", \"proof_state\", \"f_comb\", \"task_name\", \"story_edges\", \"edge_types\", \"query_edge\", \"genders\", and \"task_split\".\n\n## Kinship Relations Vocabulary\n21 relations mapped to indices 0-20: aunt, son-in-law, grandfather, brother, sister, father, mother, grandmother, uncle, daughter-in-law, grandson, granddaughter, father-in-law, mother-in-law, nephew, son, daughter, niece, husband, wife, sister-in-law.\n\n## Configuration/Split Names\nSix task configurations exist: gen_train23_test2to10, gen_train234_test2to10, rob_train_clean_23_test_all_23, rob_train_sup_23_test_all_23, rob_train_irr_23_test_all_23, and rob_train_disc_23_test_all_23.\n\n## Task Naming Scheme\n\"task_[num1].[num2]\" where num1 (1-4) indicates noise type and num2 indicates clause length. Example: \"task_1.2 -- task requiring clauses of length 2 without adding noise facts.\"\n\n## Example Counts\nTotal instances range from 9,074-12,064 training examples depending on configuration, with 2,020-3,019 validation and 444-1,146 test instances.\n\n## Gold Facts Representation\nThe \"proof_state\" field contains the logical kinship derivation, while \"f_comb\" shows the combined relation path as hyphen-separated terms (e.g., \"mother-mother\").", "durationMs": 5399, "url": "https://huggingface.co/datasets/CLUTRR/v1/blob/main/README.md"}
```

### [20] TOOL RESULT — WebFetch · 2026-06-16 04:45:53 UTC

```
{"bytes": 301661, "code": 200, "codeText": "OK", "result": "# CLUTRR Dataset Generation Details\n\nBased on the README, I can provide the following information about CLUTRR:\n\n## Dataset Overview\n\nCLUTRR is a \"benchmark dataset generator to test relational reasoning on text\" focused on compositional language understanding with text-based relational reasoning.\n\n## Output Fields\n\nThe README does not explicitly detail the specific CSV column names (story, clean_story, proof_state, query, etc.). The document mentions that \"Generated data is stored in `data/` folder\" but does not enumerate individual field names or their contents.\n\n## Key Parameters\n\n**Relation Length (k):** The system supports variable relation chain lengths. Users can specify different k values for training and testing—for example, training on k=3 while testing on k=4, 5, or 6 to measure generalizability.\n\n**Task Types:** Seven task variations exist, ranging from \"Basic family relations, free of noise\" to mixed memory and reasoning tasks, with support for adding supporting facts, irrelevant facts, and disconnected facts.\n\n## Kinship Relations\n\nThe README references \"rules\\_store.yaml\" as the location for defining the relational vocabulary but does not list specific kinship terms in the provided text.\n\n## Pre-generated Datasets\n\nThe document notes that \"Pre-generated datasets used in our paper can be found here\" (with a Google Drive link), but file sizes are not specified in this README.", "durationMs": 6704, "url": "https://github.com/facebookresearch/clutrr/blob/main/README.md"}
```

### [21] ASSISTANT · 2026-06-16 04:46:13 UTC

```
Rich fields confirmed. Let me nail down the exact representation of the edge fields (`story_edges`, `edge_types`, `query_edge`, `genders`) and confirm which config gives long chains (k≥4), by fetching the HF loading script and an example row.
```

### [22] TOOL CALL — WebFetch · 2026-06-16 04:46:13 UTC

```
URL: https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py
Prompt: Show the datasets.Features definition: the exact field names and their types (Value/Sequence/etc.) for story_edges, edge_types, query_edge, genders, story, clean_story, proof_state, f_comb, target, target_text, query, task_name, task_split. Also list the config names (BUILDER_CONFIGS) and which data files / relation lengths each maps to.
```

### [23] TOOL CALL — WebFetch · 2026-06-16 04:46:13 UTC

```
URL: https://huggingface.co/datasets/CLUTRR/v1
Prompt: Show an example data row from the dataset viewer: the actual values of story, clean_story, query, target, target_text, story_edges, edge_types, query_edge, genders, f_comb, proof_state, task_name. I need to see how edges are represented (e.g. list of [node,node] pairs, integer relation codes) and how genders are formatted (e.g. "Anna:female,Bob:male"). Also note the number of rows in each split and config.
```

### [24] TOOL RESULT — WebFetch · 2026-06-16 04:46:13 UTC

```
{"bytes": 5774, "code": 200, "codeText": "OK", "result": "# CLUTRR Dataset Features and Configurations\n\n## Dataset Features Definition\n\nAll fields use `datasets.Value()` type:\n\n| Field | Type |\n|-------|------|\n| story | string |\n| clean_story | string |\n| proof_state | string |\n| f_comb | string |\n| target | int32 |\n| target_text | string |\n| query | string |\n| task_name | string |\n| task_split | string |\n| story_edges | string |\n| edge_types | string |\n| query_edge | string |\n| genders | string |\n\n## Builder Configurations\n\nThe script defines six configuration options in `BUILDER_CONFIGS`:\n\n1. `gen_train23_test2to10`\n2. `gen_train234_test2to10`\n3. `rob_train_clean_23_test_all_23`\n4. `rob_train_disc_23_test_all_23`\n5. `rob_train_irr_23_test_all_23`\n6. `rob_train_sup_23_test_all_23`\n\nEach configuration dynamically downloads corresponding train/validation/test CSV files from the remote repository. The numeric suffixes (e.g., \"23\", \"2to10\") indicate training and test relation lengths, with \"2to10\" suggesting generalization testing across 2-10 hop reasoning chains.", "durationMs": 3674, "url": "https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py"}
```

### [25] TOOL RESULT — WebFetch · 2026-06-16 04:46:17 UTC

```
{"bytes": 1097411, "code": 200, "codeText": "OK", "result": "# CLUTRR Dataset Structure\n\n## Example Data Row\n\nFrom the dataset documentation, here's a concrete example:\n\n**Story**: \"[Ashley]'s daughter, [Lillian], asked her mom to read her a story. [Nicholas]'s sister [Lillian] asked him for some help planting her garden.\"\n\n**Query**: ('Ashley', 'Nicholas')\n\n**Target**: 15 (corresponding to \"son\")\n\n**Target_text**: \"son\"\n\n**Story_edges**: [(0, 1), (1, 2)] — node indices as integer pairs\n\n**Edge_types**: ['daughter', 'brother'] — relationship labels as strings\n\n**Query_edge**: (0, 2) — tuple of node indices\n\n**Genders**: \"Ashley:female,Lillian:female,Nicholas:male\" — name:gender pairs separated by commas\n\n**F_comb**: \"daughter-brother\" — concatenated relationship chain\n\n**Proof_state**: \"[{('Ashley', 'son', 'Nicholas'): [('Ashley', 'daughter', 'Lillian'), ('Lillian', 'brother', 'Nicholas')]}]\"\n\n## Data Split Sizes\n\n| Configuration | Train | Validation | Test |\n|---|---|---|---|\n| gen_train234_test2to10 | 12,064 | 3,019 | 1,048 |\n| gen_train23_test2to10 | 9,074 | 2,020 | 1,146 |\n| rob_train_clean_23_test_all_23 | 8,098 | 2,026 | 447 |\n| rob_train_disc_23_test_all_23 | 8,080 | 2,020 | 445 |\n| rob_train_irr_23_test_all_23 | 8,079 | 2,020 | 444 |\n| rob_train_sup_23_test_all_23 | 8,123 | 2,031 | 447 |", "durationMs": 5645, "url": "https://huggingface.co/datasets/CLUTRR/v1"}
```

### [26] ASSISTANT · 2026-06-16 04:48:35 UTC

```
Excellent — I now have the precise field structure. Let me verify two final things for a concrete plan: CLUTRR's composition rules (for computing the multi-hop closure gold) and the exact data download path in the HF loading script.
```

### [27] TOOL CALL — WebFetch · 2026-06-16 04:48:35 UTC

```
URL: https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store/rules_store.yaml
Prompt: Show the full content of this kinship composition rules file. I need the compositional rules that map a pair of consecutive relations (e.g. daughter + brother) to the resulting relation (son), and any gender lists. Show the structure/format (keys like 'compositional', 'relations', 'gender') and several example entries verbatim.
```

### [28] TOOL CALL — WebFetch · 2026-06-16 04:48:35 UTC

```
URL: https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py
Prompt: Show the _URL or download URLs used by _split_generators / dl_manager.download — the exact remote location (URL) the CSV files for each config are downloaded from. Also show how task_name, relation length, and the CSV file names are constructed. Quote the relevant Python lines verbatim.
```

### [29] TOOL RESULT — WebFetch · 2026-06-16 04:48:35 UTC

```
{"bytes": 1594, "code": 200, "codeText": "OK", "result": "# Kinship Composition Rules File Structure\n\nThis file is licensed under Facebook's license (see LICENSE in root directory).\n\n## Format Overview\n\nThe file uses YAML structure with these main sections:\n\n**\"symmetric\"** - relations that work both directions (e.g., sibling↔sibling)\n\n**\"equivalence\"** - relations treated as equivalent within a domain\n\n**\"inverse-equivalence\"** - pairs defining opposing relationships (parent↔child, manager↔subordinate)\n\n**\"compositional\"** - the core mapping of consecutive relation pairs to results\n\n**\"relation_types\"** - domain categories: family and work\n\n## Compositional Rules Example\n\nThe compositional rules follow the pattern `(relation1, relation2): result_relation`.\n\nFor the family domain, examples include:\n- `(child, child): grand` - your child's child = grandchild\n- `(child, SO): in-law` - your child's spouse = in-law\n- `(sibling, sibling): sibling` - your sibling's sibling = sibling\n- `(SO, grand): grand` - spouse's grandparent = grandparent\n\nFor work domain:\n- `(works_at, works_at): coworker`\n- `(coworker, manager): coworker`\n\n**Note:** The file contains no gender lists. The rules use gender-neutral kinship terms like \"child,\" \"grand,\" and \"sibling.\"", "durationMs": 4172, "url": "https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store/rules_store.yaml"}
```

### [30] TOOL RESULT — WebFetch · 2026-06-16 04:48:37 UTC

````
{"bytes": 5774, "code": 200, "codeText": "OK", "result": "# CLUTRR Dataset Download URLs\n\n## Base URL and Construction\n\nThe base URL is defined as:\n```python\n_URL = \"https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/\"\n```\n\n## CSV File Download Locations\n\nIn `_split_generators`, the complete download URLs are constructed by appending task name and filename:\n\n```python\nurls_to_download = {\n    \"test\": _URL + task + \"/test.csv\",\n    \"train\": _URL + task + \"/train.csv\",\n    \"validation\": _URL + task + \"/validation.csv\",\n}\n```\n\n## Task Names\n\nThe available task configurations are:\n```python\n_TASK = [\"gen_train23_test2to10\", \"gen_train234_test2to10\", \n         \"rob_train_clean_23_test_all_23\", \"rob_train_disc_23_test_all_23\", \n         \"rob_train_irr_23_test_all_23\",\"rob_train_sup_23_test_all_23\"]\n```\n\n## Example URLs\n\nFor the `gen_train23_test2to10` task, the downloaded files would be:\n- `https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/gen_train23_test2to10/train.csv`\n- `https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/gen_train23_test2to10/validation.csv`\n- `https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/gen_train23_test2to10/test.csv`\n\nThe numeric suffixes in task names (e.g., \"23\", \"2to10\") appear to indicate relation length or generalization scope.", "durationMs": 4440, "url": "https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py"}
````

### [31] ASSISTANT · 2026-06-16 04:52:02 UTC

```
I now have everything needed for a concrete, actionable plan. Key findings:

- **Direct robust download**: HF `CLUTRR/v1` pulls CSVs from `https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/<task>/{train,validation,test}.csv` — the executor can fetch these directly, no `datasets` library or `trust_remote_code` needed.
- **Rich crisp-gold fields**: each row has `clean_story`, `story_edges`, `edge_types`, `genders`, `query_edge`, `target_text`, and especially `proof_state` (e.g. `[{('Ashley','son','Nicholas'): [('Ashley','daughter','Lillian'),('Lillian','brother','Nicholas')]}]`) which yields both atomic leaf facts and intermediate multi-hop derived relations **with names**, no rule-engine reimplementation.
- **k-range**: the `gen_*_test2to10` TEST splits span chain length k=2..10 (≈1048+1146 rows), perfect for difficulty splits with k≥4 emphasis.

Let me write the plan.
```

### [32] TOOL CALL — Write · 2026-06-16 04:52:02 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json

{
  "title": "CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples with k-Difficulty Splits",
  "summary": "Build the CLUTRR calibration anchor (S2 diagonal + primary disconfirmation) from the pre-generated CLUTRR/v1 CSVs. Each story becomes one standardized row carrying the narrative document, crisp gold ATOMIC kinship facts (directly-stated edges), crisp gold MULTI-HOP inferred relations (query target + all intermediate derived relations parsed from proof_state), the full kinship edge-graph, per-entity gender/type, and chain length k as metadata_fold. Stratify ~150 confirmatory docs across k=2..10 (oversampling the error-dense long-chain k>=4 family) plus a disjoint ~40-doc pilot slice. No LLM needed (CLUTRR is rule-based/templated); no decoys, no FDR computation (those are the experiment's job). Map everything to the shared {head, relation, tail} triple schema, validate with aii-json, emit full/mini/preview. Output is tiny (<1MB).",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "The ideal artifact is a single, crisp-gold, deterministic CLUTRR-derived dataset that can host BOTH the S2 calibration-validity diagonal and the single primary disconfirmation. Concretely it must have:\n\n(1) DETERMINISTIC CRISP GOLD. CLUTRR (Sinha et al., EMNLP 2019) is rule-based/templated, so the gold kinship relations are exact (no annotation noise) — this is exactly why it hosts CALIBRATION (the realized-FDR-vs-alpha diagonal) rather than operational usefulness. Every gold triple must be 100% derivable from CLUTRR's own structured fields (no homegrown rule reimplementation that could corrupt crispness).\n\n(2) TWO GOLD FAMILIES per document, both mapped to the shared {head, relation, tail} triple schema:\n   - ATOMIC kinship facts: the relations DIRECTLY STATED in the narrative (the k chain edges), e.g. (Ashley, daughter, Lillian). These populate the 'too clean' atomic family.\n   - MULTI-HOP inferred kinship relations: the query target (a relation NOT stated, must be inferred by composition) PLUS every intermediate derived relation along the proof path. This is the error-dense 'populable' family the primary disconfirmation is pre-registered on.\n\n(3) DIFFICULTY SPLITS over chain length k. k is the number of atomic edges in the chain (CLUTRR clause length). The dataset must span k=2..10 and OVERSAMPLE long chains (k>=4), where multi-hop extraction errors densify and the FDR diagonal becomes populable. k is recorded as metadata_fold and a coarse difficulty_split ('short' for k=2,3 vs 'long' for k>=4).\n\n(4) PROVENANCE & METADATA sufficient for the downstream experiment to (a) measure populability (genuine false-admission counts at alpha*), (b) enrich false-reals via harder long chains, and (c) run document-block bootstrap. Required per row: the full kinship edge-graph (nodes + typed edges), per-entity gender and type (type='person'), the canonical query pair, f_comb composition path, raw proof_state, original CLUTRR id, source config/split, document character length (NEVER artificially padded — record native length), and is_pilot flag.\n\n(5) SCALE & SHAPE. ~150 confirmatory documents stratified across k=2..10 plus a DISJOINT ~40-doc labeled pilot slice (flagged is_pilot=true) for Phase-0 (elicitation selection + populability + S5 feature-variance measurement). Total ~190 documents. Output rows follow {input, output, metadata_fold, metadata}. Total size is tiny (well under 1MB, far under the 300MB cap). Must validate against a JSON Schema via aii-json and ship full/mini/preview variants.\n\n(6) OUT OF SCOPE (do NOT do here — these belong to the EXPERIMENT artifact): generating decoys/entrapment, scoring candidates with an LLM, computing FDR/precision/recall, or running the Prolog reasoner. This artifact delivers ONLY the raw crisp-gold data + standardized labels + folds.",
  "dataset_search_plan": "STEP 1 — PRIMARY ACQUISITION (no LLM, no generator install needed). CLUTRR/v1 on HuggingFace stores pre-generated CSVs that its loader pulls from a public GitHub raw mirror. Download these CSVs DIRECTLY with requests/urllib (most robust path, avoids datasets-script deprecation and trust_remote_code issues):\n  base = https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/\n  Configs of interest (use the TEST splits — they span chain length k=2..10):\n    - {base}gen_train234_test2to10/test.csv   (~1048 rows, k=2..10)\n    - {base}gen_train23_test2to10/test.csv    (~1146 rows, k=2..10)\n  Also grab train.csv + validation.csv of these two configs ONLY if more low-k rows are needed to fill k=2,3 strata.\n  Each CSV row has columns: id, story, clean_story, proof_state, f_comb, target, target_text, query, task_name, task_split, story_edges, edge_types, query_edge, genders. (target is an int relation code; all the structured columns are PYTHON-REPR STRINGS — parse with ast.literal_eval, NOT json.loads, because they use single quotes and tuple keys.)\n\nSTEP 2 — FALLBACKS (try in order if Step 1 URLs 404 or the repo moved):\n  (a) HuggingFace hub resolve URLs: https://huggingface.co/datasets/CLUTRR/v1/resolve/main/<task>/test.csv , or load via `from datasets import load_dataset; load_dataset('CLUTRR/v1','gen_train234_test2to10', trust_remote_code=True)`.\n  (b) The HF dataset viewer parquet export for CLUTRR/v1.\n  (c) Original generator facebookresearch/clutrr (pip install -e .; rule-based, NO LLM): regenerate long chains via `python -m clutrr.main --train_tasks 1.2 --test_tasks 1.2,1.3,...,1.10` and read the data/ CSVs. Use ONLY as last resort (gives same fields). The authors' pre-generated tar (Google Drive link in facebookresearch/clutrr README) is another mirror.\n  Verify with aii-web-tools if any URL is uncertain. Confirm the downloaded file size is small (each CSV is a few MB) and well under 300MB.\n\nSTEP 3 — PARSE STRUCTURED FIELDS per row (ast.literal_eval each):\n  - clean_story (str): the noise-free narrative. This is the canonical document. Entity mentions may be wrapped in [Brackets] — produce document_text = brackets stripped (clean prose), and keep document_text_bracketed = raw clean_story for entity-span provenance. If clean_story is empty/missing, fall back to story.\n  - story_edges -> list of (i,j) integer node-index pairs, e.g. [(0,1),(1,2)].\n  - edge_types -> list of relation strings aligned 1:1 with story_edges, e.g. ['daughter','brother'].\n  - genders -> 'Name:gender,Name:gender,...' (e.g. 'Ashley:female,Lillian:female,Nicholas:male'); split into a name->gender map. Default assumption: names are listed in node-index order (validate in Step 7).\n  - query -> ('HeadName','TailName') string tuple; the canonical query pair.\n  - query_edge -> (i,j) node-index pair for the query.\n  - target_text -> the gold inferred relation string (e.g. 'son'); target -> its int code (don't rely on the int; use target_text).\n  - f_comb -> hyphen-joined composition chain (e.g. 'daughter-brother'); split('-') length = k.\n  - proof_state -> a list of dicts each mapping a DERIVED relation triple (tuple key) to its two child sub-facts (list value), e.g. [{('Ashley','son','Nicholas'): [('Ashley','daughter','Lillian'),('Lillian','brother','Nicholas')]}]. ast.literal_eval parses tuple-keyed dicts fine.\n  - task_name -> 'task_<noise>.<k>'; the part after '.' is k. CROSS-CHECK k three ways: len(edge_types) == len(f_comb.split('-')) == int(task_name.split('.')[-1]); if they disagree, prefer len(edge_types) and log the row.\n\nSTEP 4 — ATOMIC GOLD (directly-stated facts, crisp). The k chain edges are the atomic facts. Build named triples two independent ways and CROSS-VALIDATE:\n  (A) From proof_state: the LEAF triples (named triples that appear in a value list but are never themselves a dict key / never further decomposed) are the atomic facts.\n  (B) From (story_edges, edge_types, genders-order): for each story_edge (i,j) with type r, emit (name[i], r, name[j]) using the node-index->name map.\n  atomic_facts = the agreed set {head, relation, tail}. If (A) and (B) disagree on a row, prefer (A) [proof_state names are authoritative], set metadata.atomic_crosscheck='mismatch', and log the count. Expect |atomic_facts| == k.\n\nSTEP 5 — MULTI-HOP GOLD (inferred relations, crisp, from proof_state — NO rule reimplementation). Collect EVERY dict KEY across all proof_state entries: each key is a derived (head, relation, tail) triple. These are exactly the query target PLUS all intermediate derived relations along the resolution path (k-1 of them for a length-k chain). Store as multi_hop_facts, each as {head, relation, tail, derived_from: [the two child triples], path_len}. ALWAYS include the canonical query target separately as multi_hop_query_target = {head: query[0], relation: target_text, tail: query[1]} and assert it equals the top-level proof_state key (the un-decomposed root); flag mismatches. This gives crisp multi-hop gold for the exact entity pairs on the derivation path — the set the experiment should restrict over-generation scoring to (over-generation = proposing multiple candidate relations PER such pair; only the gold one is true). Expect |multi_hop_facts| == k-1.\n\nSTEP 6 — OPTIONAL all-pairs CLOSURE (enrichment only; only if time permits AND it can be validated; otherwise SKIP — do not risk corrupting crisp gold). If richer multi-hop gold is wanted, compute the transitive closure of derivable kinship relations over the (tree-structured, unique-path) kinship graph by REUSING CLUTRR's own resolution engine / rules_store.yaml (gender-neutral relations: child, grand, sibling, SO, in-law, composed then re-genderized via the entity's gender), NOT a homegrown rule set. HARD GATE: the engine must reproduce CLUTRR's provided target_text for the query pair on 100% of rows; if ANY row mismatches, DISCARD the closure entirely and keep only the Step-5 proof-derived gold, logging the reason. If kept, store as multi_hop_closure with per-fact path provenance and mark metadata.closure_validated=true.\n\nSTEP 7 — ENTITY METADATA + EDGE GRAPH. Build the node-index->name map robustly: pin query_edge endpoints to the query names, then align (story_edges, edge_types) to the named atomic leaf facts from proof_state to recover the remaining indices; cross-check against genders-order. entities = [{name, gender (from genders map), type:'person', node_index}]. kinship_edge_graph = {nodes:[{index,name,gender}], edges:[{src,dst,relation}]} (edges = story_edges + edge_types). Record metadata.namemap_method ('genders_order' | 'proofstate_align') and a boolean genders_order_valid.\n\nSTEP 8 — ROW CONSTRUCTION (shared {head,relation,tail} schema). Emit one row per document:\n  input: {doc_id, document_text, document_text_bracketed, entities:[...], query:{head,tail}}\n  output: {atomic_facts:[{head,relation,tail}...], multi_hop_facts:[{head,relation,tail,derived_from,path_len}...], multi_hop_query_target:{head,relation,tail}, kinship_edge_graph:{nodes,edges}, multi_hop_closure (optional)}\n  metadata_fold: 'k<k>'  (the chain length stratum, e.g. 'k2'..'k10')\n  metadata: {chain_length_k, difficulty_split:('short' if k<=3 else 'long'), f_comb, task_name, source_config, source_split, clutrr_id, is_pilot, n_atomic_facts, n_multi_hop_facts, document_char_length, proof_state_raw, noisy_story (the 'story' field), atomic_crosscheck, namemap_method, relation_vocab_version:'clutrr_kinship'}\n  Note the shared schema is the triple STRUCTURE {head,relation,tail}; CLUTRR relations are kinship terms (the Re-DocRED anchor will reuse the same structure with Wikidata relation strings). Emit a top-level/sidecar relation_vocabulary = sorted unique set of all relations observed across atomic+multi-hop (reference set: aunt, uncle, nephew, niece, son, daughter, father, mother, brother, sister, grandfather, grandmother, grandson, granddaughter, husband, wife, son-in-law, daughter-in-law, father-in-law, mother-in-law, sister-in-law — do NOT hardcode; emit observed).\n\nSTEP 9 — SAMPLING & STRATIFICATION (seeded, deterministic; record selected clutrr_ids). Pool the two gen TEST splits, dedup by clean_story. Compute k=len(edge_types) per row.\n  - CONFIRMATORY set (~150 docs), stratified across k and OVERSAMPLING long chains (k>=4) since they densify multi-hop false admissions. Suggested per-k counts (adjust to availability, keep total ~150 and k>=4 the majority): k2:12, k3:15, k4:20, k5:20, k6:20, k7:18, k8:18, k9:15, k10:12. If a high-k stratum is short on rows, pull more from the other gen config or shift counts to neighbouring k (log the realized distribution).\n  - PILOT slice (~40 docs), DISJOINT from confirmatory (separate seeded draw, is_pilot=true), stratified to include BOTH the atomic-clean family (k=2,3) and the multi-hop family (k>=4) so Phase-0 can measure per-family populability and S5 feature variance.\n  - Use a fixed RNG seed (e.g. 20240617) and write the seed + the exact selected id lists into metadata/sidecar for full reproducibility.\n\nSTEP 10 — VALIDATION (aii-json). Define a JSON Schema for the row (required input/output/metadata_fold keys, triple sub-schema {head,relation,tail all strings}, k in 2..10, difficulty_split enum). Validate ALL rows with the aii-json skill. Additional integrity checks to assert and log: every atomic/multi-hop head & tail name is in entities; |atomic_facts|==k; |multi_hop_facts|==k-1; multi_hop_query_target present in multi_hop_facts; document_text non-empty; no artificial padding. Report counts of any rows dropped (e.g. proof_state unparseable on BOTH methods) and the final realized k-distribution and pilot/confirmatory counts.\n\nSTEP 11 — OUTPUT VARIANTS. Write data_out.json (full, ~190 rows). Using aii-json, also emit mini (~20 rows, stratified across k incl. pilot examples) and preview (~3-5 rows spanning a short and a long chain). Run the aii-file-size-limit check (output will be tiny, no split expected). Keep everything well under 300MB.\n\nSTEP 12 — FAILURE HANDLING SUMMARY. (i) If the kliang5 raw URLs 404 -> use the Step-2 fallbacks. (ii) If the datasets script load fails on newer datasets versions -> use direct CSV download (Step 1) which sidesteps it. (iii) If proof_state fails to parse on a row -> reconstruct atomic facts from story_edges/edge_types (Step 4B); if multi-hop can't be recovered, drop the row and log. (iv) If k>=4 strata are under-populated after pooling both gen configs -> regenerate longer chains with the facebookresearch/clutrr generator (rule-based, no LLM) as a last resort. (v) If the optional closure (Step 6) fails its 100%-reproduction gate -> drop closure, keep proof-derived gold. (vi) NEVER pad short documents; record native document_char_length. (vii) Stay strictly in DATASET scope: no decoy generation, no LLM scoring, no FDR/precision computation — those are downstream experiment artifacts.",
  "target_num_datasets": 1
}
```

### [33] TOOL RESULT — Write · 2026-06-16 04:52:02 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples with k-Difficulty Splits\",\n  \"summary\": \"Build the CLUTRR calibration anchor (S2 diagonal + primary disconfirmation) from the pre-generated CLUTRR/v1 CSVs. Each story becomes one standardized row carrying the narrative document, crisp gold ATOMIC kinship facts (directly-stated edges), crisp gold MULTI-HOP inferred relations (query target + all intermediate derived relations parsed from proof_state), the full kinship edge-graph, per-entity gender/type, and chain length k as metadata_fold. Stratify ~150 confirmatory docs across k=2..10 (oversampling the error-dense long-chain k>=4 family) plus a disjoint ~40-doc pilot slice. No LLM needed (CLUTRR is rule-based/templated); no decoys, no FDR computation (those are the experiment's job). Map everything to the shared {head, relation, tail} triple schema, validate with aii-json, emit full/mini/preview. Output is tiny (<1MB).\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"The ideal artifact is a single, crisp-gold, deterministic CLUTRR-derived dataset that can host BOTH the S2 calibration-validity diagonal and the single primary disconfirmation. Concretely it must have:\\n\\n(1) DETERMINISTIC CRISP GOLD. CLUTRR (Sinha et al., EMNLP 2019) is rule-based/templated, so the gold kinship relations are exact (no annotation noise) — this is exactly why it hosts CALIBRATION (the realized-FDR-vs-alpha diagonal) rather than operational usefulness. Every gold triple must be 100% derivable from CLUTRR's own structured fields (no homegrown rule reimplementation that could corrupt crispness).\\n\\n(2) TWO GOLD FAMILIES per document, both mapped to the shared {head, relation, tail} triple schema:\\n   - ATOMIC kinship facts: the relations DIRECTLY STATED in the narrative (the k chain edges), e.g. (Ashley, daughter, Lillian). These populate the 'too clean' atomic family.\\n   - MULTI-HOP inferred kinship relations: the query target (a relation NOT stated, must be inferred by composition) PLUS every intermediate derived relation along the proof path. This is the error-dense 'populable' family the primary disconfirmation is pre-registered on.\\n\\n(3) DIFFICULTY SPLITS over chain length k. k is the number of atomic edges in the chain (CLUTRR clause length). The dataset must span k=2..10 and OVERSAMPLE long chains (k>=4), where multi-hop extraction errors densify and the FDR diagonal becomes populable. k is recorded as metadata_fold and a coarse difficulty_split ('short' for k=2,3 vs 'long' for k>=4).\\n\\n(4) PROVENANCE & METADATA sufficient for the downstream experiment to (a) measure populability (genuine false-admission counts at alpha*), (b) enrich false-reals via harder long chains, and (c) run document-block bootstrap. Required per row: the full kinship edge-graph (nodes + typed edges), per-entity gender and type (type='person'), the canonical query pair, f_comb composition path, raw proof_state, original CLUTRR id, source config/split, document character length (NEVER artificially padded — record native length), and is_pilot flag.\\n\\n(5) SCALE & SHAPE. ~150 confirmatory documents stratified across k=2..10 plus a DISJOINT ~40-doc labeled pilot slice (flagged is_pilot=true) for Phase-0 (elicitation selection + populability + S5 feature-variance measurement). Total ~190 documents. Output rows follow {input, output, metadata_fold, metadata}. Total size is tiny (well under 1MB, far under the 300MB cap). Must validate against a JSON Schema via aii-json and ship full/mini/preview variants.\\n\\n(6) OUT OF SCOPE (do NOT do here — these belong to the EXPERIMENT artifact): generating decoys/entrapment, scoring candidates with an LLM, computing FDR/precision/recall, or running the Prolog reasoner. This artifact delivers ONLY the raw crisp-gold data + standardized labels + folds.\",\n  \"dataset_search_plan\": \"STEP 1 — PRIMARY ACQUISITION (no LLM, no generator install needed). CLUTRR/v1 on HuggingFace stores pre-generated CSVs that its loader pulls from a public GitHub raw mirror. Download these CSVs DIRECTLY with requests/urllib (most robust path, avoids datasets-script deprecation and trust_remote_code issues):\\n  base = https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/\\n  Configs of interest (use the TEST splits — they span chain length k=2..10):\\n    - {base}gen_train234_test2to10/test.csv   (~1048 rows, k=2..10)\\n    - {base}gen_train23_test2to10/test.csv    (~1146 rows, k=2..10)\\n  Also grab train.csv + validation.csv of these two configs ONLY if more low-k rows are needed to fill k=2,3 strata.\\n  Each CSV row has columns: id, story, clean_story, proof_state, f_comb, target, target_text, query, task_name, task_split, story_edges, edge_types, query_edge, genders. (target is an int relation code; all the structured columns are PYTHON-REPR STRINGS — parse with ast.literal_eval, NOT json.loads, because they use single quotes and tuple keys.)\\n\\nSTEP 2 — FALLBACKS (try in order if Step 1 URLs 404 or the repo moved):\\n  (a) HuggingFace hub resolve URLs: https://huggingface.co/datasets/CLUTRR/v1/resolve/main/<task>/test.csv , or load via `from datasets import load_dataset; load_dataset('CLUTRR/v1','gen_train234_test2to10', trust_remote_code=True)`.\\n  (b) The HF dataset viewer parquet export for CLUTRR/v1.\\n  (c) Original generator facebookresearch/clutrr (pip install -e .; rule-based, NO LLM): regenerate long chains via `python -m clutrr.main --train_tasks 1.2 --test_tasks 1.2,1.3,...,1.10` and read the data/ CSVs. Use ONLY as last resort (gives same fields). The authors' pre-generated tar (Google Drive link in facebookresearch/clutrr README) is another mirror.\\n  Verify with aii-web-tools if any URL is uncertain. Confirm the downloaded file size is small (each CSV is a few MB) and well under 300MB.\\n\\nSTEP 3 — PARSE STRUCTURED FIELDS per row (ast.literal_eval each):\\n  - clean_story (str): the noise-free narrative. This is the canonical document. Entity mentions may be wrapped in [Brackets] — produce document_text = brackets stripped (clean prose), and keep document_text_bracketed = raw clean_story for entity-span provenance. If clean_story is empty/missing, fall back to story.\\n  - story_edges -> list of (i,j) integer node-index pairs, e.g. [(0,1),(1,2)].\\n  - edge_types -> list of relation strings aligned 1:1 with story_edges, e.g. ['daughter','brother'].\\n  - genders -> 'Name:gender,Name:gender,...' (e.g. 'Ashley:female,Lillian:female,Nicholas:male'); split into a name->gender map. Default assumption: names are listed in node-index order (validate in Step 7).\\n  - query -> ('HeadName','TailName') string tuple; the canonical query pair.\\n  - query_edge -> (i,j) node-index pair for the query.\\n  - target_text -> the gold inferred relation string (e.g. 'son'); target -> its int code (don't rely on the int; use target_text).\\n  - f_comb -> hyphen-joined composition chain (e.g. 'daughter-brother'); split('-') length = k.\\n  - proof_state -> a list of dicts each mapping a DERIVED relation triple (tuple key) to its two child sub-facts (list value), e.g. [{('Ashley','son','Nicholas'): [('Ashley','daughter','Lillian'),('Lillian','brother','Nicholas')]}]. ast.literal_eval parses tuple-keyed dicts fine.\\n  - task_name -> 'task_<noise>.<k>'; the part after '.' is k. CROSS-CHECK k three ways: len(edge_types) == len(f_comb.split('-')) == int(task_name.split('.')[-1]); if they disagree, prefer len(edge_types) and log the row.\\n\\nSTEP 4 — ATOMIC GOLD (directly-stated facts, crisp). The k chain edges are the atomic facts. Build named triples two independent ways and CROSS-VALIDATE:\\n  (A) From proof_state: the LEAF triples (named triples that appear in a value list but are never themselves a dict key / never further decomposed) are the atomic facts.\\n  (B) From (story_edges, edge_types, genders-order): for each story_edge (i,j) with type r, emit (name[i], r, name[j]) using the node-index->name map.\\n  atomic_facts = the agreed set {head, relation, tail}. If (A) and (B) disagree on a row, prefer (A) [proof_state names are authoritative], set metadata.atomic_crosscheck='mismatch', and log the count. Expect |atomic_facts| == k.\\n\\nSTEP 5 — MULTI-HOP GOLD (inferred relations, crisp, from proof_state — NO rule reimplementation). Collect EVERY dict KEY across all proof_state entries: each key is a derived (head, relation, tail) triple. These are exactly the query target PLUS all intermediate derived relations along the resolution path (k-1 of them for a length-k chain). Store as multi_hop_facts, each as {head, relation, tail, derived_from: [the two child triples], path_len}. ALWAYS include the canonical query target separately as multi_hop_query_target = {head: query[0], relation: target_text, tail: query[1]} and assert it equals the top-level proof_state key (the un-decomposed root); flag mismatches. This gives crisp multi-hop gold for the exact entity pairs on the derivation path — the set the experiment should restrict over-generation scoring to (over-generation = proposing multiple candidate relations PER such pair; only the gold one is true). Expect |multi_hop_facts| == k-1.\\n\\nSTEP 6 — OPTIONAL all-pairs CLOSURE (enrichment only; only if time permits AND it can be validated; otherwise SKIP — do not risk corrupting crisp gold). If richer multi-hop gold is wanted, compute the transitive closure of derivable kinship relations over the (tree-structured, unique-path) kinship graph by REUSING CLUTRR's own resolution engine / rules_store.yaml (gender-neutral relations: child, grand, sibling, SO, in-law, composed then re-genderized via the entity's gender), NOT a homegrown rule set. HARD GATE: the engine must reproduce CLUTRR's provided target_text for the query pair on 100% of rows; if ANY row mismatches, DISCARD the closure entirely and keep only the Step-5 proof-derived gold, logging the reason. If kept, store as multi_hop_closure with per-fact path provenance and mark metadata.closure_validated=true.\\n\\nSTEP 7 — ENTITY METADATA + EDGE GRAPH. Build the node-index->name map robustly: pin query_edge endpoints to the query names, then align (story_edges, edge_types) to the named atomic leaf facts from proof_state to recover the remaining indices; cross-check against genders-order. entities = [{name, gender (from genders map), type:'person', node_index}]. kinship_edge_graph = {nodes:[{index,name,gender}], edges:[{src,dst,relation}]} (edges = story_edges + edge_types). Record metadata.namemap_method ('genders_order' | 'proofstate_align') and a boolean genders_order_valid.\\n\\nSTEP 8 — ROW CONSTRUCTION (shared {head,relation,tail} schema). Emit one row per document:\\n  input: {doc_id, document_text, document_text_bracketed, entities:[...], query:{head,tail}}\\n  output: {atomic_facts:[{head,relation,tail}...], multi_hop_facts:[{head,relation,tail,derived_from,path_len}...], multi_hop_query_target:{head,relation,tail}, kinship_edge_graph:{nodes,edges}, multi_hop_closure (optional)}\\n  metadata_fold: 'k<k>'  (the chain length stratum, e.g. 'k2'..'k10')\\n  metadata: {chain_length_k, difficulty_split:('short' if k<=3 else 'long'), f_comb, task_name, source_config, source_split, clutrr_id, is_pilot, n_atomic_facts, n_multi_hop_facts, document_char_length, proof_state_raw, noisy_story (the 'story' field), atomic_crosscheck, namemap_method, relation_vocab_version:'clutrr_kinship'}\\n  Note the shared schema is the triple STRUCTURE {head,relation,tail}; CLUTRR relations are kinship terms (the Re-DocRED anchor will reuse the same structure with Wikidata relation strings). Emit a top-level/sidecar relation_vocabulary = sorted unique set of all relations observed across atomic+multi-hop (reference set: aunt, uncle, nephew, niece, son, daughter, father, mother, brother, sister, grandfather, grandmother, grandson, granddaughter, husband, wife, son-in-law, daughter-in-law, father-in-law, mother-in-law, sister-in-law — do NOT hardcode; emit observed).\\n\\nSTEP 9 — SAMPLING & STRATIFICATION (seeded, deterministic; record selected clutrr_ids). Pool the two gen TEST splits, dedup by clean_story. Compute k=len(edge_types) per row.\\n  - CONFIRMATORY set (~150 docs), stratified across k and OVERSAMPLING long chains (k>=4) since they densify multi-hop false admissions. Suggested per-k counts (adjust to availability, keep total ~150 and k>=4 the majority): k2:12, k3:15, k4:20, k5:20, k6:20, k7:18, k8:18, k9:15, k10:12. If a high-k stratum is short on rows, pull more from the other gen config or shift counts to neighbouring k (log the realized distribution).\\n  - PILOT slice (~40 docs), DISJOINT from confirmatory (separate seeded draw, is_pilot=true), stratified to include BOTH the atomic-clean family (k=2,3) and the multi-hop family (k>=4) so Phase-0 can measure per-family populability and S5 feature variance.\\n  - Use a fixed RNG seed (e.g. 20240617) and write the seed + the exact selected id lists into metadata/sidecar for full reproducibility.\\n\\nSTEP 10 — VALIDATION (aii-json). Define a JSON Schema for the row (required input/output/metadata_fold keys, triple sub-schema {head,relation,tail all strings}, k in 2..10, difficulty_split enum). Validate ALL rows with the aii-json skill. Additional integrity checks to assert and log: every atomic/multi-hop head & tail name is in entities; |atomic_facts|==k; |multi_hop_facts|==k-1; multi_hop_query_target present in multi_hop_facts; document_text non-empty; no artificial padding. Report counts of any rows dropped (e.g. proof_state unparseable on BOTH methods) and the final realized k-distribution and pilot/confirmatory counts.\\n\\nSTEP 11 — OUTPUT VARIANTS. Write data_out.json (full, ~190 rows). Using aii-json, also emit mini (~20 rows, stratified across k incl. pilot examples) and preview (~3-5 rows spanning a short and a long chain). Run the aii-file-size-limit check (output will be tiny, no split expected). Keep everything well under 300MB.\\n\\nSTEP 12 — FAILURE HANDLING SUMMARY. (i) If the kliang5 raw URLs 404 -> use the Step-2 fallbacks. (ii) If the datasets script load fails on newer datasets versions -> use direct CSV download (Step 1) which sidesteps it. (iii) If proof_state fails to parse on a row -> reconstruct atomic facts from story_edges/edge_types (Step 4B); if multi-hop can't be recovered, drop the row and log. (iv) If k>=4 strata are under-populated after pooling both gen configs -> regenerate longer chains with the facebookresearch/clutrr generator (rule-based, no LLM) as a last resort. (v) If the optional closure (Step 6) fails its 100%-reproduction gate -> drop closure, keep proof-derived gold. (vi) NEVER pad short documents; record native document_char_length. (vii) Stay strictly in DATASET scope: no decoy generation, no LLM scoring, no FDR/precision computation — those are downstream experiment artifacts.\",\n  \"target_num_datasets\": 1\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [34] ASSISTANT · 2026-06-16 04:52:16 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json`.

## Summary

I planned the **CLUTRR crisp-gold calibration anchor** — the dataset that hosts the S2 calibration-validity diagonal and the single primary disconfirmation. Key research-grounded decisions:

**Acquisition (no LLM, no generator install).** CLUTRR is rule-based/templated, so gold is exact. The `CLUTRR/v1` HF loader pulls pre-generated CSVs from a public GitHub raw mirror (`raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/...`) — the executor downloads those CSVs **directly**, sidestepping `datasets`-script deprecation/`trust_remote_code`. Three fallback sources listed.

**Crisp gold without rule reimplementation (the critical insight).** Each CSV row carries `proof_state`, e.g. `[{('Ashley','son','Nicholas'): [('Ashley','daughter','Lillian'),('Lillian','brother','Nicholas')]}]`. Parsing it yields:
- **Atomic facts** = the leaf triples (directly-stated edges) — the "too clean" family.
- **Multi-hop gold** = every dict *key* = query target + all intermediate derived relations along the path — the error-dense **populable** family. All with real names, no homegrown composition engine that could corrupt crispness. A dual-source cross-check (proof_state vs `story_edges`/`edge_types`/`genders`) guards integrity. Full all-pairs closure is offered only as **optional enrichment gated by 100% reproduction** of CLUTRR's own targets.

**Difficulty splits.** The `gen_*_test2to10` TEST splits span chain length k=2..10. Plan stratifies ~150 confirmatory docs across k, **oversampling k≥4** (where multi-hop errors densify to populate the diagonal), plus a disjoint ~40-doc seeded pilot slice covering both families for Phase-0.

**Schema & scope.** Maps to the shared `{head, relation, tail}` triple structure, full row schema (`input`/`output`/`metadata_fold`/`metadata`), aii-json validation, full/mini/preview variants, native document lengths (no padding), tiny output (<1MB). Explicitly **out of scope**: decoy/entrapment generation, LLM scoring, FDR computation — those are downstream experiment artifacts.

**Compute:** `cpu_heavy` (trivial CPU task; only download + parse + write). **target_num_datasets:** 1 (CLUTRR is the single calibration anchor; multiple fallback *sources* for it are listed).
```
