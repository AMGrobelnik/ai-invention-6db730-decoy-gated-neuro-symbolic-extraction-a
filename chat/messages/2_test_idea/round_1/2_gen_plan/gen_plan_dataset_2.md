# gen_plan_dataset_2 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_2` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 04:44:09 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_2
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

id: dataset_iter1_dir2
type: dataset
objective: >-
  Build the open-vocabulary, human-gold Re-DocRED operational anchor that hosts the operational-usefulness wedge (S4) and
  the document-level predictive account (S5), standardized to the SAME triple schema and partitioned into >=4 entity/topic
  clusters so cross-document feature variance exists for the S5 GAP regression.
approach: >-
  Acquire Re-DocRED (Tan et al., EMNLP 2022, 'Revisiting DocRED'; tonytan48/Re-DocRED on GitHub or a HuggingFace mirror; the
  original DocRED is also on HF datasets). For each document produce a standardized row: full reconstructed document text
  (from the tokenized sentences, ~200 words), the annotated entity set with entity types (PER/ORG/LOC/TIME/NUM/MISC) and mention
  spans, gold (head-entity, relation, tail-entity) triples over the annotated entities across the 96 Wikidata relation types,
  evidence sentence spans per triple, relation-type and entity-type metadata, document length (word count) as an explicit
  S5 feature, and a cluster label assigned by dominant entity type / topic giving >=4 clusters as metadata_fold (this enables
  leave-one-cluster-out CV). Flag a small labeled pilot slice for Phase-0 and the S5 power analysis. Target ~150 confirmatory
  documents balanced across clusters plus the pilot slice. Assert only that gold supports RELATIVE operational comparisons
  (residual false negatives affect all systems equally). Map to the SHARED (head, relation, tail) triple schema, validate
  with aii-json, split full/mini/preview, keep under 300MB.
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

### [4] ASSISTANT · 2026-06-16 04:44:33 UTC

```
I'll research the Re-DocRED dataset to make this plan concrete and actionable. Let me start with parallel searches on its format, availability, and schema.
```

### [5] TOOL CALL — ToolSearch · 2026-06-16 04:44:33 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-06-16 04:44:33 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [7] TOOL CALL — Read · 2026-06-16 04:44:33 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
```

### [8] TOOL RESULT — Read · 2026-06-16 04:44:33 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "content": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\n\n**REVIEW_HYPO iter_7 verdict (2026-06-16):** score 6/10 (weak accept, up from 5), conf 4. Soundness 3, Presentation 3 (bumped from 2 — threat table + claim-chain table delivered as prior review asked), Contribution 3. relation_type=evolution. All 4 prior-iter_4 majors substantively ADDRESSED: (a) isolated-scoring budget recomputed explicitly (240 docs×~20 cand×3 item-types≈14.4K calls, 7-15M tok) + document-prefix prompt caching → fits $10 hard stop; (b) primary disconfirmation now POPULABILITY-GATED, moved to error-dense MULTI-HOP kinship family w/ N_false_min=40, explicit UNTESTABLE outcome; (c) SHARED operational construct (fixed claim-decomp+relation-align maps all systems to identical (h,r,t) triples) + RESTORED plain zero-label confidence-threshold comparator; (d) explicit BUDGET WATERFALL. Novelty re-confirmed: closest new work arXiv 2606.00402 (Jun 2026, knockoff filtering) = human-vs-machine TEXT DETECTION, different task, NOT a threat — but add 1 sentence of awareness. 2 residual majors (second-order, not blocking): (1) rigor — diagonal positive-CONFIRMATION power: N_false_min sized for populability not grid-wise tracking CIs under document-block bootstrap (~120 docs); ~40 false admissions across 5+ alpha points → underpowered positive claim (single-point disconfirmation OK). Fix: pre-register grid-tracking power separately. (2) methodology/significance — absolute calibration asserted ONLY on toy CLUTRR; Re-DocRED only RELATIVE; S5 transfer-bridge is leftover-budget → headline 'calibrated knob useful on realistic text' never directly connected. Fix: pull a conservatively-biased (upper-bound, gold-FN-inflated) realized-FDR curve on Re-DocRED into committed budget. 4 minors: graded (not binary) decoy/false-real tail-exchangeability test w/ conservative correction; symbolic-reasoning/trace-graph/OpenCyc + vs-RAW-LLM deliverables now thin vs statistical core (goal/venue alignment) — commit them non-leftover; cite 2606.00402 line; density still the main presentation lever. Output written to run dir.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n\n**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.\n", "numLines": 36, "startLine": 1, "totalLines": 36}}
```

### [9] ASSISTANT · 2026-06-16 04:44:39 UTC

```
I have the context. Now let me research the Re-DocRED dataset format, availability, and schema in parallel.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 04:44:39 UTC

```
Re-DocRED tonytan48 GitHub dataset train_revised.json format Revisiting DocRED
```

### [11] TOOL CALL — WebSearch · 2026-06-16 04:44:39 UTC

```
Re-DocRED HuggingFace datasets mirror tonytan48 relation extraction
```

### [12] TOOL CALL — WebSearch · 2026-06-16 04:44:39 UTC

```
DocRED data format vertexSet sents labels h t r evidence JSON structure entity types PER ORG LOC TIME NUM MISC
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 04:44:43 UTC

```
{"query": "Re-DocRED tonytan48 GitHub dataset train_revised.json format Revisiting DocRED", "results": [{"tool_use_id": "srvtoolu_0192MZ47CkBrntoa4FHRtDTt", "content": [{"title": "GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub", "url": "https://github.com/tonytan48/KD-DocRE"}, {"title": "Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction", "url": "https://arxiv.org/html/2205.12696"}, {"title": "Re-DocRED/README.md at main · tonytan48/Re-DocRED", "url": "https://github.com/tonytan48/Re-DocRED/blob/main/README.md"}, {"title": "tonytan48/Re-DocRED · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED"}, {"title": "(PDF) Revisiting DocRED -- Addressing the Overlooked False Negative Problem in Relation Extraction", "url": "https://www.researchgate.net/publication/360859401_Revisiting_DocRED_--_Addressing_the_Overlooked_False_Negative_Problem_in_Relation_Extraction"}, {"title": "GitHub - wisper12933/LMRC", "url": "https://github.com/wisper12933/LMRC"}, {"title": "README.md · tonytan48/Re-DocRED at main", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED/blob/main/README.md"}, {"title": "tonytan48/Re-DocRED · Discussions", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED/discussions"}, {"title": "tonytan48 - Overview", "url": "https://github.com/tonytan48"}, {"title": "Revisiting DocRED -- Addressing the False Negative Problem in Relation   Extraction", "url": "https://arxiv.org/pdf/2205.12696"}]}, "Based on the search results, here's what I found about the Re-DocRED dataset by tonytan48:\n\n## Overview\n\nRe-DocRED is the dataset from the EMNLP 2022 research paper \"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction\". The original DocRED dataset contained a significant percentage of false negative examples due to incomplete annotation, so 4,053 documents were revised.\n\n## Dataset Files and Format\n\nThe Re-DocRED dataset contains files named train_revised.json, dev_revised.json, and test_revised.json in the data directory.\n\n## Key Improvements\n\nThe Re-DocRED dataset resolved the incompleteness problem by supplementing large amounts of relation triples, addressed logical inconsistencies in DocRED, and corrected coreferential errors.\n\n## Performance Impact\n\nModels trained and evaluated on Re-DocRED achieve performance improvements of around 13 F1 points compared to the original DocRED.\n\n## Access\n\nThe dataset is publicly available at https://github.com/tonytan48/Re-DocRED."], "durationSeconds": 5.233742584000003, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 04:44:45 UTC

````
{"query": "DocRED data format vertexSet sents labels h t r evidence JSON structure entity types PER ORG LOC TIME NUM MISC", "results": [{"tool_use_id": "srvtoolu_01MwV1rTD3Cyf1EJJMtTvYDm", "content": [{"title": "DocRED/data at master · thunlp/DocRED", "url": "https://github.com/thunlp/DocRED/tree/master/data"}, {"title": "DocRED/data/README.md at master · thunlp/DocRED", "url": "https://github.com/thunlp/DocRED/blob/master/data/README.md"}, {"title": "DocRed/gen_data.py at master · hongwang600/DocRed", "url": "https://github.com/hongwang600/DocRed/blob/master/gen_data.py"}, {"title": "DocRED/code/gen_data.py at master · thunlp/DocRED", "url": "https://github.com/thunlp/DocRED/blob/master/code/gen_data.py"}, {"title": "thunlp/docred · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/thunlp/docred"}, {"title": "amodaresi/Re-DocRED-CF · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/amodaresi/Re-DocRED-CF"}, {"title": "DocRED dataset and its baseline", "url": "https://programming.vip/docs/docred-dataset-and-its-baseline.html"}, {"title": "huggingface.co", "url": "https://huggingface.co/datasets/thunlp/docred/blob/30755ecba81fbc2676f071e8a29fd5a3c474e565/docred.py"}]}, "Based on the search results, here's the DocRED data format structure:\n\n## JSON Structure\n\nThe DocRED format contains:\n- **title**: Document title\n- **sents**: Array of sentences, each containing words\n- **vertexSet**: Array of entities, where each entity contains multiple mentions with properties:\n  - **name**: mention name\n  - **sent_id**: sentence index containing the mention\n  - **pos**: position of mention in the sentence\n  - **type**: NER type\n- **labels**: Array of relation annotations with:\n  - **h**: index of head entity in vertexSet\n  - **t**: index of tail entity in vertexSet\n  - **r**: relation type\n  - **evidence**: evidence sentence IDs\n\n## Example Structure\n\nA concrete example shows:\n```json\n{\n  \"title\": \"Title of the document\",\n  \"sents\": [[\"This\", \"is\", \"a\", \"sentence\"], [\"This\", \"is\", \"another\", \"sentence\"]],\n  \"vertexSet\": [\n    [{\"name\": \"sentence\", \"pos\": [3], \"sent_id\": 0, \"type\": \"NN\"}, \n     {\"name\": \"sentence\", \"pos\": [3], \"sent_id\": 1, \"type\": \"NN\"}],\n    [{\"name\": \"This\", \"pos\": [0], \"sent_id\": 0, \"type\": \"NN\"}]\n  ],\n  \"labels\": {\"evidence\": [[0]], \"head\": [0], \"relation_id\": [\"P1\"], \"relation_text\": [\"is_a\"], \"tail\": [0]}\n}\n```\n\nThe dataset is designed for document-level relation extraction, requiring systems to synthesize information across multiple sentences to extract and infer entity relations."], "durationSeconds": 5.745801123999998, "searchCount": 1}
````

### [15] TOOL RESULT — WebSearch · 2026-06-16 04:44:47 UTC

```
{"query": "Re-DocRED HuggingFace datasets mirror tonytan48 relation extraction", "results": [{"tool_use_id": "srvtoolu_01Tn99gjMj1EKCzNqc5k8LFT", "content": [{"title": "tonytan48/Re-DocRED · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED"}, {"title": "GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss", "url": "https://github.com/tonytan48/kd-docre"}, {"title": "README.md · tonytan48/Re-DocRED at main", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED/blob/main/README.md"}, {"title": "Daily Papers - Hugging Face", "url": "https://huggingface.co/papers?q=relation+triples"}, {"title": "Low-Level Laser Therapy for Plantar Fasciitis", "url": "https://cdn.clinicaltrials.gov/large-docs/81/NCT05763381/Prot_SAP_002.pdf"}, {"title": "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction", "url": "https://arxiv.org/pdf/2511.08143"}, {"title": "thunlp/docred · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/thunlp/docred"}, {"title": "tonytan48/Re-DocRED · Discussions", "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED/discussions"}, {"title": "docred.py · thunlp/docred at main", "url": "https://huggingface.co/datasets/thunlp/docred/blob/main/docred.py"}, {"title": "Models – Hugging Face", "url": "https://huggingface.co/models?other=relation-extraction"}]}, "Based on the search results, here's what I found about Re-DocRED:\n\n## Overview\n\nRe-DocRED is a dataset from an EMNLP 2022 research paper titled \"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction\". DocRED is a widely used benchmark for document-level relation extraction, but contains a significant percentage of false negative examples (incomplete annotation).\n\n## Key Improvements\n\nThe researchers revised 4,053 documents in the DocRED dataset and resolved its problems. The Re-DocRED Dataset resolved the following problems of DocRED: resolved the incompleteness problem by supplementing large amounts of relation triples, addressed the logical inconsistencies in DocRED, and corrected the coreferential errors within DocRED.\n\n## Performance Impact\n\nModels trained and evaluated on Re-DocRED gains around 13 F1 compared to DocRED.\n\n## Availability\n\nThe dataset is available on HuggingFace at the tonytan48/Re-DocRED repository, and the leaderboard of Re-DocRED is hosted on Paperswithcode."], "durationSeconds": 8.197413953999996, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 04:45:01 UTC

```
Let me fetch the exact dataset structure and relation mapping details in parallel.
```

### [17] TOOL CALL — WebFetch · 2026-06-16 04:45:01 UTC

```
URL: https://huggingface.co/datasets/tonytan48/Re-DocRED
Prompt: What files are in this dataset repository (exact filenames and paths), what is the data format/schema of each document (fields like title, sents, vertexSet, labels), how many documents in train/dev/test, and how to download it (HF datasets load_dataset usage or direct file URLs)? List all data files and config names.
```

### [18] TOOL CALL — WebFetch · 2026-06-16 04:45:01 UTC

```
URL: https://github.com/tonytan48/Re-DocRED/blob/main/README.md
Prompt: What is the directory structure and file list of this repo? What are the exact data file names (train/dev/test), the statistics (number of documents, triples, entities per document, average length), and where is the relation info / rel_info.json file mapping relation P-ids to names? How many relation types are there? Provide download instructions.
```

### [19] TOOL RESULT — WebFetch · 2026-06-16 04:45:01 UTC

```
{"bytes": 1487410, "code": 200, "codeText": "OK", "result": "Based on the webpage content provided, I cannot give you the specific details you're requesting. The page shows metadata about the \"Re-DocRED\" dataset by tonytan48 on Hugging Face, including that it uses JSON format and is sized between 1K-10K, but the actual file listings, schema details, document counts, and download instructions are not included in the excerpt.\n\nTo find this information, you would need to:\n\n1. Visit the full dataset page at `huggingface.co/datasets/tonytan48/Re-DocRED`\n2. Check the \"Files and versions\" section (referenced but not shown)\n3. Review the dataset card for schema documentation\n4. Look for train/dev/test split information\n\nThe webpage content provided is \"truncated due to length,\" so the detailed file structure and loading instructions aren't available in your source material.", "durationMs": 3969, "url": "https://huggingface.co/datasets/tonytan48/Re-DocRED"}
```

### [20] TOOL CALL — WebFetch · 2026-06-16 04:45:01 UTC

```
URL: https://github.com/thunlp/DocRED/blob/master/data/README.md
Prompt: Describe the exact JSON data format for DocRED: the structure of each document including title, sents (tokenized sentences), vertexSet (entities with mentions: name, sent_id, pos, type), and labels (h, t, r, evidence). What are the entity type values? What is rel_info.json and what does it contain? How are positions (pos) defined - token offsets within a sentence?
```

### [21] TOOL RESULT — WebFetch · 2026-06-16 04:45:01 UTC

```
{"bytes": 243059, "code": 200, "codeText": "OK", "result": "# Re-DocRED Dataset Information\n\nBased on the README content provided, here's what I can tell you:\n\n## Dataset Statistics\nThe Re-DocRED dataset contains three splits with these metrics:\n\n| Split | Documents | Avg. Triples | Avg. Entities | Avg. Sentences |\n|-------|-----------|--------------|---------------|----------------|\n| Train | 3,053 | 28.1 | 19.4 | 7.9 |\n| Dev | 500 | 34.6 | 19.4 | 8.2 |\n| Test | 500 | 34.9 | 19.6 | 7.9 |\n\n## Location\n\"The Re-DocRED dataset is located as ./data directory\"\n\n## Missing Information\nThe README does not provide:\n- Specific file names (train/dev/test formats)\n- Number of relation types\n- Location or structure of rel_info.json mapping files\n- Download instructions or links\n- Complete directory structure\n\n## To Access Complete Details\nYou would need to:\n1. Visit the full repository at https://github.com/tonytan48/Re-DocRED\n2. Browse the `./data` directory in the repository\n3. Check for additional documentation files beyond this README\n\nThe repository references the EMNLP 2022 paper for technical details about the dataset improvements addressing false negatives in the original DocRED.", "durationMs": 4183, "url": "https://github.com/tonytan48/Re-DocRED/blob/main/README.md"}
```

### [22] TOOL RESULT — WebFetch · 2026-06-16 04:45:03 UTC

```
{"bytes": 234237, "code": 200, "codeText": "OK", "result": "# DocRED Data Format Overview\n\nBased on the GitHub README, here's the documented structure:\n\n## Core JSON Schema\n\nEach document contains:\n\n- **title**: Document name\n- **sents**: Array of tokenized sentences, where each sentence is `[word1, word2, ...]`\n- **vertexSet**: Entity array with mentions containing:\n  - `name`: Mention text\n  - `sent_id`: Sentence index containing the mention\n  - `pos`: \"postion of mention in a sentence\"\n  - `type`: NER type classification\n- **labels**: Relation triples with:\n  - `h`: Head entity index in vertexSet\n  - `t`: Tail entity index in vertexSet\n  - `r`: Relation type\n  - `evidence`: Array of supporting sentence IDs\n\n## Unanswered Questions\n\nThe README doesn't specify:\n- **Entity type values**: No list of NER types is provided\n- **rel_info.json**: The file is mentioned as \"uploaded\" but not documented in this README\n- **Position definition**: The README uses vague phrasing (\"postion of mention in a sentence\") without clarifying if positions are token indices, character offsets, or another format\n\nYou'd need to examine actual data files or supplementary documentation to resolve these ambiguities.", "durationMs": 4164, "url": "https://github.com/thunlp/DocRED/blob/master/data/README.md"}
```

### [23] ASSISTANT · 2026-06-16 04:45:13 UTC

```
Let me get the exact file listing and relation mapping. I'll query the HF API tree and the raw rel_info.json.
```

### [24] TOOL CALL — WebFetch · 2026-06-16 04:45:13 UTC

```
URL: https://huggingface.co/api/datasets/tonytan48/Re-DocRED/tree/main/data
Prompt: List every file path and filename shown in this JSON response, including their sizes.
```

### [25] TOOL RESULT — WebFetch · 2026-06-16 04:45:13 UTC

```
{"bytes": 0, "code": 404, "codeText": "Not Found", "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 188, "url": "https://huggingface.co/api/datasets/tonytan48/Re-DocRED/tree/main/data"}
```

### [26] TOOL CALL — WebFetch · 2026-06-16 04:45:13 UTC

```
URL: https://huggingface.co/api/datasets/tonytan48/Re-DocRED/tree/main
Prompt: List every file path, directory, and filename shown in this JSON response, including their sizes.
```

### [27] TOOL CALL — WebFetch · 2026-06-16 04:45:13 UTC

```
URL: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/rel_info.json
Prompt: Show the contents. How many key-value pairs (relation P-id to relation name) are there? List a representative sample of about 20 entries including the P-id keys and relation name values.
```

### [28] TOOL RESULT — WebFetch · 2026-06-16 04:45:13 UTC

```
{"bytes": 712, "code": 200, "codeText": "OK", "result": "# Files in Repository\n\n**File Listing:**\n\n1. **.gitattributes** — 2,320 bytes\n2. **README.md** — 1,557 bytes\n3. **dev_revised.json** — 3,245,588 bytes (~3.1 MB)\n4. **test_revised.json** — 3,207,228 bytes (~3.1 MB)\n5. **train_revised.json** — 18,602,933 bytes (~18.6 MB)\n\nAll files are located in the root directory. No subdirectories are present in this repository structure.", "durationMs": 1628, "url": "https://huggingface.co/api/datasets/tonytan48/Re-DocRED/tree/main"}
```

### [29] TOOL RESULT — WebFetch · 2026-06-16 04:45:13 UTC

```
{"bytes": 0, "code": 404, "codeText": "Not Found", "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 373, "url": "https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/rel_info.json"}
```

### [30] ASSISTANT · 2026-06-16 04:45:23 UTC

```
Let me locate the relation info file and confirm entity types.
```

### [31] TOOL CALL — WebFetch · 2026-06-16 04:45:23 UTC

```
URL: https://raw.githubusercontent.com/thunlp/DocRED/master/code/rel_info.json
Prompt: Show the contents. How many key-value pairs (relation P-id to relation name) are there? List about 15 sample entries with P-id keys and relation name values.
```

### [32] TOOL RESULT — WebFetch · 2026-06-16 04:45:23 UTC

```
{"bytes": 0, "code": 404, "codeText": "Not Found", "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 163, "url": "https://raw.githubusercontent.com/thunlp/DocRED/master/code/rel_info.json"}
```

### [33] TOOL CALL — WebFetch · 2026-06-16 04:45:23 UTC

```
URL: https://github.com/tonytan48/Re-DocRED/tree/main/data
Prompt: List all files in this data directory, including rel_info.json if present, and their names.
```

### [34] TOOL CALL — WebSearch · 2026-06-16 04:45:23 UTC

```
DocRED rel_info.json 96 relations P6 P17 P19 Wikidata "head of government" raw github
```

### [35] TOOL RESULT — WebFetch · 2026-06-16 04:45:23 UTC

```
{"bytes": 231943, "code": 200, "codeText": "OK", "result": "Based on the GitHub page content provided, the data directory contains the following files:\n\n1. **README.md** - Documentation file\n2. **dev_revised.json** - Development dataset in JSON format\n3. **test_revised.json** - Test dataset in JSON format\n4. **train_revised.json** - Training dataset in JSON format\n\nThe page does not indicate the presence of a \"rel_info.json\" file in this directory listing. Only these four items are shown in the files and folders table on the main branch of the Re-DocRED repository's data folder.", "durationMs": 2659, "url": "https://github.com/tonytan48/Re-DocRED/tree/main/data"}
```

### [36] TOOL RESULT — WebSearch · 2026-06-16 04:45:35 UTC

```
{"query": "DocRED rel_info.json 96 relations P6 P17 P19 Wikidata \"head of government\" raw github", "results": [{"tool_use_id": "srvtoolu_01YTsGaovfK2fwQ1pD7XxhJN", "content": [{"title": "A Large-Scale Document-Level Relation Extraction Dataset", "url": "https://aclanthology.org/P19-1074.pdf"}, {"title": "DocRED: A Large-Scale Document-Level Relation Extraction Dataset", "url": "https://arxiv.org/pdf/1906.06127"}, {"title": "DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF", "url": "https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"}, {"title": "DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology", "url": "https://aclanthology.org/P19-1074/"}, {"title": "DocRED: A Large-Scale Document-Level Relation Extraction Dataset", "url": "https://www.groundai.com/project/docred-a-large-scale-document-level-relation-extraction-dataset/1"}, {"title": "Semi-automatic Data Enhancement for Document-Level Relation Extraction   with Distant Supervision from Large Language Models", "url": "https://arxiv.org/pdf/2311.07314"}, {"title": "Relation Extraction — DeepPavlov 1.7.0 documentation", "url": "https://docs.deeppavlov.ai/en/master/features/models/relation_extraction.html"}]}, "Based on the search results, I found information about DocRED's relation set:\n\nDocRED contains 96 predefined relations and 6 entity types, with an average of 19.5 entities per document. \n\nThe dataset includes 96 frequent relation types from Wikidata. Some of the relations you mentioned include:\n\n- P6: \"head of government\" - head of the executive power of this town, city, municipality, state, country, or other governmental body\n- P17: \"country\" - sovereign state of this item; don't use on humans\n- P19: \"place of birth\" - most specific known birth location of person, animal or fictional character\n\nThe search results include the academic papers from ACL 2019, which contain detailed lists of the relations used in DocRED. However, I didn't find the specific GitHub repository with the raw `rel_info.json` file in these results. If you're looking for the raw file, you might want to check the official DocRED GitHub repository directly."], "durationSeconds": 12.915806331999994, "searchCount": 1}
```

### [37] ASSISTANT · 2026-06-16 04:46:01 UTC

```
The HF Re-DocRED mirror has only the 3 JSON files (no rel_info.json). Let me pin down where the relation-name mapping lives and confirm licensing/length stats.
```

### [38] TOOL CALL — WebFetch · 2026-06-16 04:46:01 UTC

```
URL: https://huggingface.co/datasets/thunlp/docred/resolve/main/rel_info.json
Prompt: Show the contents. How many relation P-id to name pairs? List ~15 sample entries (P-id and name).
```

### [39] TOOL RESULT — WebFetch · 2026-06-16 04:46:01 UTC

```
{"bytes": 0, "code": 404, "codeText": "Not Found", "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 187, "url": "https://huggingface.co/datasets/thunlp/docred/resolve/main/rel_info.json"}
```

### [40] TOOL CALL — WebFetch · 2026-06-16 04:46:01 UTC

```
URL: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/rel_info.json
Prompt: Show the contents and count of relation P-id to name pairs.
```

### [41] TOOL RESULT — WebFetch · 2026-06-16 04:46:01 UTC

```
{"bytes": 0, "code": 404, "codeText": "Not Found", "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 153, "url": "https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/rel_info.json"}
```

### [42] TOOL CALL — WebFetch · 2026-06-16 04:46:01 UTC

```
URL: https://arxiv.org/html/2205.12696
Prompt: What is the license of Re-DocRED? What is the average number of words/tokens per document, average entities, average relation triples, and number of relation types (96?) and entity types (6: PER/ORG/LOC/TIME/NUM/MISC)? Any details on how documents are tokenized into sentences.
```

### [43] TOOL RESULT — WebFetch · 2026-06-16 04:46:01 UTC

```
{"bytes": 250225, "code": 200, "codeText": "OK", "result": "# Re-DocRED Dataset Specifications\n\n## License\nThe document does not specify a license for Re-DocRED. It only states: \"Our dataset is publicly available at https://github.com/tonytan48/Re-DocRED.\"\n\n## Dataset Statistics\n\n**Document-level metrics:**\n- Average words per document: 198.4\n- Average entities: 19.4 (training), 19.6 (test)\n- Average relation triples: 28.1 (training), 34.6-34.9 (dev/test)\n\n**Relation and entity types:**\n- Relation types: 96 (including no_relation)\n- Entity types: The document does not specify entity type counts or categories\n\n## Sentence Tokenization\nThe paper provides no details on tokenization methodology or sentence segmentation approaches used in Re-DocRED.\n\n**Note:** Table 5 shows \"Avg. # Sentences\" (7.9-8.2), indicating documents contain multiple sentences, but the tokenization process itself remains undocumented in the provided text.", "durationMs": 4262, "url": "https://arxiv.org/html/2205.12696"}
```

### [44] ASSISTANT · 2026-06-16 04:49:55 UTC

```
I have everything I need. Confirmed facts:

- **Source**: `tonytan48/Re-DocRED` on HF — root files `train_revised.json` (18.6MB), `dev_revised.json` (3.1MB), `test_revised.json` (3.1MB); ~25MB total, far under 300MB. GitHub fallback under `/data/`.
- **Format**: DocRED schema — `title`, `sents` (token lists), `vertexSet` (entities → mentions `{name, sent_id, pos:[start,end] token offsets, type}`), `labels` (`{h, t, r=P-id, evidence:[sent_ids]}`).
- **Stats**: 4,053 docs (3,053/500/500), avg 198.4 words, ~19.4 entities, ~28–35 triples/doc, ~8 sentences; 96 Wikidata relations; 6 entity types (PER/ORG/LOC/TIME/NUM/MISC).
- **rel_info.json** not on the HF mirror → resolve relation names/descriptions via original DocRED repo or Wikidata API.

Now let me write the plan.
```

### [45] TOOL CALL — Write · 2026-06-16 04:49:55 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_2/.terminal_claude_agent_struct_out.json

{
  "title": "Re-DocRED Operational Anchor: Standardized Triple-Schema Corpus with Entity Inventory, Evidence, Per-Document S5 Features, and >=4 Cross-Document Clusters",
  "summary": "Acquire Re-DocRED (Tan et al., EMNLP 2022) and standardize it into one operational anchor dataset for the label-free FDR-gating hypothesis. Each row is one Wikipedia document carrying: (1) the reconstructed ~200-word text, (2) the full annotated entity inventory (6 types, mention spans), (3) the human-gold (head, relation, tail) triples mapped into a SHARED canonical triple schema with relation names + evidence sentences, (4) per-document descriptive features that vary across documents (length, entity/triple density, relation/entity-type profiles, multi-hop/evidence-span proxies) for the S5 GAP regression, and (5) a cluster label (metadata_fold) giving >=4 entity-type/topic clusters for leave-one-cluster-out CV, plus a flag splitting a ~30-40-doc Phase-0 pilot slice from ~150 balanced confirmatory documents. The dataset supplies the SAME triple space and entity set into which every system (neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal) is later mapped at matched recall; it asserts only RELATIVE operational comparisons (residual false negatives affect all systems equally). Raw data is ~25MB; standardized output is well under 300MB. Pure CPU data-prep: download, parse, compute per-document descriptive features, cluster, flag, validate, split full/mini/preview.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "SINGLE SOURCE, deeply standardized (this is a one-dataset standardization task, not a broad search). The dataset is Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022). It is the operational anchor: it hosts the S4 operational-usefulness wedge and the S5 document-level predictive account. It is NOT used for the absolute calibration diagonal (that is CLUTRR, a separate artifact); on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted, because Re-DocRED still has residual false negatives that affect all systems equally.\n\nWHY RE-DocRED IS IDEAL: (a) realistic open-vocabulary Wikipedia prose (not a toy closed vocabulary), so the relation-to-schema alignment that the neuro-symbolic 'bridge' must perform is genuine; (b) 96 Wikidata relation types + 6 entity types -> a large open relation space where plausible hallucinations actually bite; (c) human-revised gold triples WITH evidence sentences (~13 F1 of recovered false negatives over original DocRED), giving the cleanest available document-level gold for relative precision/recall; (d) SHORT documents (avg 198.4 words, ~8 sentences, ~19.4 entities, ~28-35 triples) -> roughly the ~3000-character target in the goal, CPU-friendly, and cheap to score under the $10 LLM budget; (e) document-level multi-hop structure (triples whose evidence spans multiple sentences) supports the hallucinated-conclusion-rate measurement; (f) heterogeneous topics (biographies, organizations, places, creative works/events) yield the >=4 entity-type/topic clusters needed so S5 input features genuinely VARY across documents (CLUTRR cannot supply this variance -- that is precisely why this anchor exists).\n\nSIZE / SHAPE OF THE DELIVERED DATASET: ~150 CONFIRMATORY documents balanced across >=4 clusters (target ~35-40 per cluster for 4 clusters) PLUS a ~30-40-document PILOT slice (disjoint from confirmatory, also spread across clusters) flagged for Phase-0 elicitation selection / tail-AUC power analysis and the S5 GAP-regression power analysis. Total ~180-200 standardized rows. Optionally retain a small reserve pool (another ~30-60 docs, flagged is_reserve) so the experiment can top up any under-powered cluster without re-running this artifact. Raw Re-DocRED is ~25MB across three JSON files; the standardized data_out.json (full) will be on the order of tens of MB -- comfortably under the 300MB hard limit (still run the aii-file-size-limit check and split if needed).\n\nEACH ROW MUST CARRY (raw data only -- NO experiment outputs, NO scores, NO FDR, NO decoys): the reconstructed document text; the complete annotated entity inventory with entity types and mention spans; the gold (head, relation, tail) triples in a single SHARED canonical schema with human-readable relation names + per-triple evidence sentence ids and resolved evidence text; per-document descriptive features (these are simple properties of the data -- length, counts, densities, profiles -- NOT derived experimental statistics); a cluster label as metadata_fold; and pilot/confirmatory/reserve flags. The relation inventory (the 96 P-ids with names and descriptions) and entity-type inventory are emitted as a companion reference so all downstream systems align to the identical triple space.\n\nGOLD CAVEAT (must be recorded in dataset-level metadata): Re-DocRED gold has residual false negatives; therefore this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) -- never an absolute realized-FDR diagonal. State this explicitly so the experiment does not misuse it.",
  "dataset_search_plan": "STEP 1 -- ACQUIRE Re-DocRED (single source; verify first, then download).\n  Primary source (CONFIRMED to exist, public, no auth): HuggingFace dataset 'tonytan48/Re-DocRED'. The three data files sit at the repo ROOT (not under data/). Download directly via the resolve URLs:\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/train_revised.json  (~18.6 MB, 3,053 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/dev_revised.json    (~3.1 MB, 500 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/test_revised.json   (~3.1 MB, 500 docs)\n  Use either the aii-hf-datasets skill (huggingface_hub.hf_hub_download with repo_type='dataset') or plain requests.get on the resolve URLs. Total ~25 MB -> trivially within 300MB and within memory.\n  Fallback A (if HF is down): GitHub raw from tonytan48/Re-DocRED, files under the data/ folder: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/train_revised.json (and dev_revised.json, test_revised.json).\n  Fallback B: the GitHub release / repo zip of github.com/tonytan48/Re-DocRED. Do NOT substitute the original noisy thunlp/DocRED gold for the confirmatory set (it has the false-negative problem Re-DocRED fixes); the original DocRED may only be used, optionally, for a residual-FN sensitivity note.\n  After download, assert each file parses as JSON and is a list of document objects; log counts (expect 3053 / 500 / 500). Pool all 4,053 documents into one working list tagged by split_origin.\n\nSTEP 2 -- CONFIRM the source schema on a few documents before mass processing.\n  Each document object has: 'title' (str); 'sents' (list of sentences, each a list of word tokens); 'vertexSet' (list of ENTITIES; each entity is a list of MENTIONS; each mention = {'name': str, 'sent_id': int, 'pos': [start_token, end_token] HALF-OPEN token offsets within that sentence, 'type': one of PER/ORG/LOC/TIME/NUM/MISC}); 'labels' (list of TRIPLES; each = {'h': head entity index into vertexSet, 't': tail entity index into vertexSet, 'r': relation Wikidata P-id string e.g. 'P26', 'evidence': list of sentence ids}). Print one full example and assert these keys/types exist; abort with a clear message if the schema differs (so a silently-changed mirror is caught early).\n\nSTEP 3 -- BUILD the relation inventory (the shared canonical relation space; 96 Wikidata relations).\n  The HF mirror does NOT ship rel_info.json, so resolve relation P-id -> human-readable name (+ description) by, in priority order:\n    (i) Try to download a DocRED rel_info.json (P-id->name map) from the original repo, e.g. github.com/thunlp/DocRED (search the repo tree for 'rel_info.json'; it is part of the original DocRED meta). If found, use its names.\n    (ii) ROBUST DEFAULT -- collect the set of unique P-ids actually appearing across all documents' labels, then batch-query the Wikidata API for English label + description: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P26|P17|...&props=labels|descriptions&languages=en&format=json (chunk ids to <=50 per call; this is free, public, no LLM budget). Cache the result to a local relation_schema.json.\n    (iii) Fallback: hardcode the well-known DocRED 96-relation name map (e.g. P6=head of government, P17=country, P19=place of birth, P26=spouse, P27=country of citizenship, P569=date of birth, P570=date of death, ...). \n  Emit a companion file relation_schema.json: a list of {relation_pid, relation_name, relation_description} for every P-id present (expect ~96). The DESCRIPTION is valuable downstream for the relation-alignment step that maps every system's raw output into this triple space -- include it. Also emit entity_type_schema = the 6 types with short glosses.\n\nSTEP 4 -- STANDARDIZE each document into one row. For every document compute and store:\n  4a. TEXT RECONSTRUCTION: build 'text' deterministically. Per sentence, join its tokens; apply light, deterministic detokenization (no space before ,.!?;:)]} or before a closing quote/possessive; no space after ([{ or opening quote) so the prose reads naturally for the LLM extractor; then join sentences with a single space. Record 'sent_char_offsets' = the character offset in 'text' where each sentence begins. ALSO keep the original tokenized 'sents' verbatim (token offsets are the authoritative grounding; char spans are convenience).\n  4b. ENTITY INVENTORY ('entities'): for each vertexSet entity i emit {entity_id: i, type: <entity type>, canonical_name: <pick the longest or most frequent mention surface>, mentions: [{name, sent_id, pos:[start_tok,end_tok], char_span:[start_char,end_char] computed from sent_char_offsets + the detokenized token positions}]}. If char-span computation is fragile for any mention, fall back to leaving char_span null but ALWAYS keep the token pos. Record n_mentions per entity.\n  4c. GOLD TRIPLES ('gold_triples', the SHARED schema): for each label emit {head_id, head_name(=canonical_name of head), head_type, relation_pid, relation_name(from STEP 3), tail_id, tail_name, tail_type, evidence_sent_ids: [...], evidence_text: [the reconstructed text of each evidence sentence]}. If a triple has empty evidence (can happen for re-annotated triples), keep evidence_sent_ids=[] and evidence_text=[] (do not drop the triple). De-duplicate identical (head_id, relation_pid, tail_id) triples if any.\n  Keep this row as raw data only: NO candidate generation, NO decoys, NO scoring, NO derived FDR. Those belong to the experiment.\n\nSTEP 5 -- COMPUTE per-document descriptive features (raw properties of the data, stored under metadata; these are the S5 GAP-regression inputs, NOT experiment results). For each document record: num_words (token count of text), num_chars, num_sents, num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts (dict over the 6 types), dominant_entity_type (argmax of entity_type_counts; break ties by a fixed type priority PER>ORG>LOC>MISC>TIME>NUM), relation_pid_counts (dict), avg_mentions_per_entity, entity_density (num_entities/num_words), mention_density (total_mentions/num_words), triple_density (num_triples/num_sents), frac_singleton_entities (entities with exactly 1 mention), and TWO multi-hop / cross-sentence proxies: frac_multi_evidence_triples (fraction of triples with >1 evidence sentence) and max_evidence_sentence_gap (max over triples of (max evidence sent_id - min evidence sent_id); 0 if all single-sentence). These features deliberately VARY across documents/clusters -- that variance is the reason Re-DocRED (not CLUTRR) hosts S5.\n\nSTEP 6 -- CLUSTER documents into >=4 clusters (metadata_fold for leave-one-cluster-out CV).\n  PRIMARY scheme (interpretable, recommended as metadata_fold): cluster_by = dominant_entity_type, collapsed to FOUR genre-like clusters -> {PER-dominant (biographies), ORG-dominant (organizations/bands/companies), LOC-dominant (places/geography), MISC-dominant (creative works/events/other)}. Map the rare TIME/NUM-dominant documents into MISC (or their nearest non-rare dominant type) so exactly >=4 well-populated clusters result. Set metadata_fold = 'cluster_PER' | 'cluster_ORG' | 'cluster_LOC' | 'cluster_MISC'.\n  SECONDARY scheme (store ALSO, for robustness, under metadata.kmeans_cluster): run k-means (k=5 or 6, fixed random_state for reproducibility) on a per-document feature vector = normalized 6-dim entity-type histogram concatenated with the normalized top-relation profile (and standardized length). This gives a topical clustering independent of the entity-type rule; the experiment can switch to it if the entity-type folds prove too correlated.\n  VALIDATE the primary scheme: confirm >=4 clusters each have enough source documents to fill the balanced confirmatory quota (target ~35-40/cluster for ~150 confirmatory + pilot). If any primary cluster is too small, top it up from the secondary k-means clusters or relax the collapse (e.g. split MISC), but ALWAYS keep >=4 clusters and record which scheme produced metadata_fold.\n\nSTEP 7 -- SELECT and FLAG the confirmatory set, pilot slice, and reserve.\n  Eligibility filter (keep documents that are useful and on-spec): num_words roughly in [80, 400] (most Re-DocRED docs are ~200; this trims outliers while keeping the ~3000-char target), num_entities >= 4, num_triples >= 5 (so each document can actually host enough candidates to matter). Do not over-filter -- record num_words as a feature rather than discarding moderately long docs.\n  CONFIRMATORY: sample ~150 documents BALANCED across the >=4 primary clusters (e.g. 4 clusters x ~38 = 152). Within each cluster prefer documents spanning the feature range (do not pick only the densest) so cross-document feature variance is preserved for S5. Set metadata.is_confirmatory=true.\n  PILOT: sample a DISJOINT ~30-40 documents, also spread across clusters, for Phase-0 (elicitation/tail-AUC selection) and the S5 power analysis. Set metadata.is_pilot=true, is_confirmatory=false. Pilot docs are 'labeled' simply in that gold is available (all Re-DocRED docs have gold) -- do NOT fabricate negative/decoy triples here; candidate and decoy generation is the experiment's job.\n  RESERVE (optional): flag another ~30-60 disjoint docs is_reserve=true so the experiment can top up an under-powered cluster without re-running this artifact.\n  Use a FIXED random seed for all sampling and record it in dataset-level metadata for reproducibility. Ensure confirmatory / pilot / reserve are mutually exclusive (no document appears twice).\n\nSTEP 8 -- ASSEMBLE the output row schema. Each row in data_out.json:\n  {\n    'id': 'redocred_<split_origin>_<orig_index>',\n    'input': { 'title', 'text', 'sents', 'sent_char_offsets', 'entities': [ {entity_id, type, canonical_name, n_mentions, mentions:[{name, sent_id, pos, char_span}]} ] },\n    'output': { 'gold_triples': [ {head_id, head_name, head_type, relation_pid, relation_name, tail_id, tail_name, tail_type, evidence_sent_ids, evidence_text} ] },\n    'metadata_fold': '<cluster label from STEP 6 primary scheme>',\n    'metadata': { 'split_origin', 'orig_index', 'is_confirmatory', 'is_pilot', 'is_reserve', 'kmeans_cluster', 'cluster_scheme', 'seed', plus ALL per-document features from STEP 5 (num_words, num_chars, num_sents, num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts, dominant_entity_type, relation_pid_counts, avg_mentions_per_entity, entity_density, mention_density, triple_density, frac_singleton_entities, frac_multi_evidence_triples, max_evidence_sentence_gap), 'gold_caveat': 'Re-DocRED has residual false negatives; supports RELATIVE operational comparisons only, not an absolute FDR diagonal.' }\n  }\n  Keep field names exactly aligned with the standard DATASET output contract {input, output, metadata_fold, ...}. Also write companion files: relation_schema.json (96 P-ids), entity_type_schema.json (6 types), and a top-level dataset_meta object (source citation + URLs, split counts, seed, cluster scheme, per-cluster doc counts, the gold_caveat, and a one-line statement that this is the shared triple space all systems map into at matched recall).\n\nSTEP 9 -- VALIDATE and SPLIT. Author a JSON Schema for the row and run the aii-json skill to validate every row in data_out.json against it (fail loudly on any missing/extra field or type mismatch). Then use aii-json to generate the full / mini / preview variants (mini = a few rows per cluster incl. at least one pilot row; preview = 1-2 illustrative rows with all fields populated). Run the aii-file-size-limit skill on data_out.json (expected tens of MB, under 300MB) and split only if it exceeds the limit.\n\nSTEP 10 -- SANITY REPORT (log, do not put in data_out as derived stats): print final counts (total rows, confirmatory/pilot/reserve, per-cluster), the realized feature ranges per cluster (to confirm cross-document variance exists -- the S5 precondition), the number of unique relation P-ids covered vs 96 and unique entity types covered vs 6, and a handful of fully-rendered example rows (text + entities + a few gold triples with evidence) for eyeball QA. Confirm no document appears in more than one of confirmatory/pilot/reserve, and that every gold triple's head_id/tail_id index a valid entity.\n\nFAILURE SCENARIOS & MITIGATIONS:\n  - HF mirror missing/changed -> GitHub raw fallback (Step 1 fallback A/B); assert schema in Step 2 to catch silent format drift.\n  - rel_info.json unavailable -> Wikidata wbgetentities API (free, no LLM budget) then hardcoded map (Step 3).\n  - Cluster imbalance (PER-dominant dominates) -> collapse rare TIME/NUM into MISC, top up from k-means secondary scheme, or split MISC; always keep >=4 balanced, populated clusters (Step 6).\n  - Documents too short/long or too few triples -> eligibility filter in Step 7 (keep ~80-400 words, >=5 triples) but record length as a feature rather than aggressively discarding.\n  - Empty evidence on re-annotated triples -> keep the triple with empty evidence arrays (Step 4c); do not drop.\n  - char_span computation fragile for odd tokenization -> leave char_span null but always retain authoritative token pos (Step 4b).\n  - Temptation to manufacture negatives/decoys for the pilot -> DO NOT; this is a raw-data artifact. Candidate/decoy/scoring generation is the downstream experiment's responsibility (keeps this strictly within DATASET executor scope).",
  "target_num_datasets": 1
}
```

### [46] TOOL RESULT — Write · 2026-06-16 04:49:55 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_2/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Re-DocRED Operational Anchor: Standardized Triple-Schema Corpus with Entity Inventory, Evidence, Per-Document S5 Features, and >=4 Cross-Document Clusters\",\n  \"summary\": \"Acquire Re-DocRED (Tan et al., EMNLP 2022) and standardize it into one operational anchor dataset for the label-free FDR-gating hypothesis. Each row is one Wikipedia document carrying: (1) the reconstructed ~200-word text, (2) the full annotated entity inventory (6 types, mention spans), (3) the human-gold (head, relation, tail) triples mapped into a SHARED canonical triple schema with relation names + evidence sentences, (4) per-document descriptive features that vary across documents (length, entity/triple density, relation/entity-type profiles, multi-hop/evidence-span proxies) for the S5 GAP regression, and (5) a cluster label (metadata_fold) giving >=4 entity-type/topic clusters for leave-one-cluster-out CV, plus a flag splitting a ~30-40-doc Phase-0 pilot slice from ~150 balanced confirmatory documents. The dataset supplies the SAME triple space and entity set into which every system (neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal) is later mapped at matched recall; it asserts only RELATIVE operational comparisons (residual false negatives affect all systems equally). Raw data is ~25MB; standardized output is well under 300MB. Pure CPU data-prep: download, parse, compute per-document descriptive features, cluster, flag, validate, split full/mini/preview.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"SINGLE SOURCE, deeply standardized (this is a one-dataset standardization task, not a broad search). The dataset is Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022). It is the operational anchor: it hosts the S4 operational-usefulness wedge and the S5 document-level predictive account. It is NOT used for the absolute calibration diagonal (that is CLUTRR, a separate artifact); on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted, because Re-DocRED still has residual false negatives that affect all systems equally.\\n\\nWHY RE-DocRED IS IDEAL: (a) realistic open-vocabulary Wikipedia prose (not a toy closed vocabulary), so the relation-to-schema alignment that the neuro-symbolic 'bridge' must perform is genuine; (b) 96 Wikidata relation types + 6 entity types -> a large open relation space where plausible hallucinations actually bite; (c) human-revised gold triples WITH evidence sentences (~13 F1 of recovered false negatives over original DocRED), giving the cleanest available document-level gold for relative precision/recall; (d) SHORT documents (avg 198.4 words, ~8 sentences, ~19.4 entities, ~28-35 triples) -> roughly the ~3000-character target in the goal, CPU-friendly, and cheap to score under the $10 LLM budget; (e) document-level multi-hop structure (triples whose evidence spans multiple sentences) supports the hallucinated-conclusion-rate measurement; (f) heterogeneous topics (biographies, organizations, places, creative works/events) yield the >=4 entity-type/topic clusters needed so S5 input features genuinely VARY across documents (CLUTRR cannot supply this variance -- that is precisely why this anchor exists).\\n\\nSIZE / SHAPE OF THE DELIVERED DATASET: ~150 CONFIRMATORY documents balanced across >=4 clusters (target ~35-40 per cluster for 4 clusters) PLUS a ~30-40-document PILOT slice (disjoint from confirmatory, also spread across clusters) flagged for Phase-0 elicitation selection / tail-AUC power analysis and the S5 GAP-regression power analysis. Total ~180-200 standardized rows. Optionally retain a small reserve pool (another ~30-60 docs, flagged is_reserve) so the experiment can top up any under-powered cluster without re-running this artifact. Raw Re-DocRED is ~25MB across three JSON files; the standardized data_out.json (full) will be on the order of tens of MB -- comfortably under the 300MB hard limit (still run the aii-file-size-limit check and split if needed).\\n\\nEACH ROW MUST CARRY (raw data only -- NO experiment outputs, NO scores, NO FDR, NO decoys): the reconstructed document text; the complete annotated entity inventory with entity types and mention spans; the gold (head, relation, tail) triples in a single SHARED canonical schema with human-readable relation names + per-triple evidence sentence ids and resolved evidence text; per-document descriptive features (these are simple properties of the data -- length, counts, densities, profiles -- NOT derived experimental statistics); a cluster label as metadata_fold; and pilot/confirmatory/reserve flags. The relation inventory (the 96 P-ids with names and descriptions) and entity-type inventory are emitted as a companion reference so all downstream systems align to the identical triple space.\\n\\nGOLD CAVEAT (must be recorded in dataset-level metadata): Re-DocRED gold has residual false negatives; therefore this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) -- never an absolute realized-FDR diagonal. State this explicitly so the experiment does not misuse it.\",\n  \"dataset_search_plan\": \"STEP 1 -- ACQUIRE Re-DocRED (single source; verify first, then download).\\n  Primary source (CONFIRMED to exist, public, no auth): HuggingFace dataset 'tonytan48/Re-DocRED'. The three data files sit at the repo ROOT (not under data/). Download directly via the resolve URLs:\\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/train_revised.json  (~18.6 MB, 3,053 docs)\\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/dev_revised.json    (~3.1 MB, 500 docs)\\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/test_revised.json   (~3.1 MB, 500 docs)\\n  Use either the aii-hf-datasets skill (huggingface_hub.hf_hub_download with repo_type='dataset') or plain requests.get on the resolve URLs. Total ~25 MB -> trivially within 300MB and within memory.\\n  Fallback A (if HF is down): GitHub raw from tonytan48/Re-DocRED, files under the data/ folder: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/train_revised.json (and dev_revised.json, test_revised.json).\\n  Fallback B: the GitHub release / repo zip of github.com/tonytan48/Re-DocRED. Do NOT substitute the original noisy thunlp/DocRED gold for the confirmatory set (it has the false-negative problem Re-DocRED fixes); the original DocRED may only be used, optionally, for a residual-FN sensitivity note.\\n  After download, assert each file parses as JSON and is a list of document objects; log counts (expect 3053 / 500 / 500). Pool all 4,053 documents into one working list tagged by split_origin.\\n\\nSTEP 2 -- CONFIRM the source schema on a few documents before mass processing.\\n  Each document object has: 'title' (str); 'sents' (list of sentences, each a list of word tokens); 'vertexSet' (list of ENTITIES; each entity is a list of MENTIONS; each mention = {'name': str, 'sent_id': int, 'pos': [start_token, end_token] HALF-OPEN token offsets within that sentence, 'type': one of PER/ORG/LOC/TIME/NUM/MISC}); 'labels' (list of TRIPLES; each = {'h': head entity index into vertexSet, 't': tail entity index into vertexSet, 'r': relation Wikidata P-id string e.g. 'P26', 'evidence': list of sentence ids}). Print one full example and assert these keys/types exist; abort with a clear message if the schema differs (so a silently-changed mirror is caught early).\\n\\nSTEP 3 -- BUILD the relation inventory (the shared canonical relation space; 96 Wikidata relations).\\n  The HF mirror does NOT ship rel_info.json, so resolve relation P-id -> human-readable name (+ description) by, in priority order:\\n    (i) Try to download a DocRED rel_info.json (P-id->name map) from the original repo, e.g. github.com/thunlp/DocRED (search the repo tree for 'rel_info.json'; it is part of the original DocRED meta). If found, use its names.\\n    (ii) ROBUST DEFAULT -- collect the set of unique P-ids actually appearing across all documents' labels, then batch-query the Wikidata API for English label + description: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P26|P17|...&props=labels|descriptions&languages=en&format=json (chunk ids to <=50 per call; this is free, public, no LLM budget). Cache the result to a local relation_schema.json.\\n    (iii) Fallback: hardcode the well-known DocRED 96-relation name map (e.g. P6=head of government, P17=country, P19=place of birth, P26=spouse, P27=country of citizenship, P569=date of birth, P570=date of death, ...). \\n  Emit a companion file relation_schema.json: a list of {relation_pid, relation_name, relation_description} for every P-id present (expect ~96). The DESCRIPTION is valuable downstream for the relation-alignment step that maps every system's raw output into this triple space -- include it. Also emit entity_type_schema = the 6 types with short glosses.\\n\\nSTEP 4 -- STANDARDIZE each document into one row. For every document compute and store:\\n  4a. TEXT RECONSTRUCTION: build 'text' deterministically. Per sentence, join its tokens; apply light, deterministic detokenization (no space before ,.!?;:)]} or before a closing quote/possessive; no space after ([{ or opening quote) so the prose reads naturally for the LLM extractor; then join sentences with a single space. Record 'sent_char_offsets' = the character offset in 'text' where each sentence begins. ALSO keep the original tokenized 'sents' verbatim (token offsets are the authoritative grounding; char spans are convenience).\\n  4b. ENTITY INVENTORY ('entities'): for each vertexSet entity i emit {entity_id: i, type: <entity type>, canonical_name: <pick the longest or most frequent mention surface>, mentions: [{name, sent_id, pos:[start_tok,end_tok], char_span:[start_char,end_char] computed from sent_char_offsets + the detokenized token positions}]}. If char-span computation is fragile for any mention, fall back to leaving char_span null but ALWAYS keep the token pos. Record n_mentions per entity.\\n  4c. GOLD TRIPLES ('gold_triples', the SHARED schema): for each label emit {head_id, head_name(=canonical_name of head), head_type, relation_pid, relation_name(from STEP 3), tail_id, tail_name, tail_type, evidence_sent_ids: [...], evidence_text: [the reconstructed text of each evidence sentence]}. If a triple has empty evidence (can happen for re-annotated triples), keep evidence_sent_ids=[] and evidence_text=[] (do not drop the triple). De-duplicate identical (head_id, relation_pid, tail_id) triples if any.\\n  Keep this row as raw data only: NO candidate generation, NO decoys, NO scoring, NO derived FDR. Those belong to the experiment.\\n\\nSTEP 5 -- COMPUTE per-document descriptive features (raw properties of the data, stored under metadata; these are the S5 GAP-regression inputs, NOT experiment results). For each document record: num_words (token count of text), num_chars, num_sents, num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts (dict over the 6 types), dominant_entity_type (argmax of entity_type_counts; break ties by a fixed type priority PER>ORG>LOC>MISC>TIME>NUM), relation_pid_counts (dict), avg_mentions_per_entity, entity_density (num_entities/num_words), mention_density (total_mentions/num_words), triple_density (num_triples/num_sents), frac_singleton_entities (entities with exactly 1 mention), and TWO multi-hop / cross-sentence proxies: frac_multi_evidence_triples (fraction of triples with >1 evidence sentence) and max_evidence_sentence_gap (max over triples of (max evidence sent_id - min evidence sent_id); 0 if all single-sentence). These features deliberately VARY across documents/clusters -- that variance is the reason Re-DocRED (not CLUTRR) hosts S5.\\n\\nSTEP 6 -- CLUSTER documents into >=4 clusters (metadata_fold for leave-one-cluster-out CV).\\n  PRIMARY scheme (interpretable, recommended as metadata_fold): cluster_by = dominant_entity_type, collapsed to FOUR genre-like clusters -> {PER-dominant (biographies), ORG-dominant (organizations/bands/companies), LOC-dominant (places/geography), MISC-dominant (creative works/events/other)}. Map the rare TIME/NUM-dominant documents into MISC (or their nearest non-rare dominant type) so exactly >=4 well-populated clusters result. Set metadata_fold = 'cluster_PER' | 'cluster_ORG' | 'cluster_LOC' | 'cluster_MISC'.\\n  SECONDARY scheme (store ALSO, for robustness, under metadata.kmeans_cluster): run k-means (k=5 or 6, fixed random_state for reproducibility) on a per-document feature vector = normalized 6-dim entity-type histogram concatenated with the normalized top-relation profile (and standardized length). This gives a topical clustering independent of the entity-type rule; the experiment can switch to it if the entity-type folds prove too correlated.\\n  VALIDATE the primary scheme: confirm >=4 clusters each have enough source documents to fill the balanced confirmatory quota (target ~35-40/cluster for ~150 confirmatory + pilot). If any primary cluster is too small, top it up from the secondary k-means clusters or relax the collapse (e.g. split MISC), but ALWAYS keep >=4 clusters and record which scheme produced metadata_fold.\\n\\nSTEP 7 -- SELECT and FLAG the confirmatory set, pilot slice, and reserve.\\n  Eligibility filter (keep documents that are useful and on-spec): num_words roughly in [80, 400] (most Re-DocRED docs are ~200; this trims outliers while keeping the ~3000-char target), num_entities >= 4, num_triples >= 5 (so each document can actually host enough candidates to matter). Do not over-filter -- record num_words as a feature rather than discarding moderately long docs.\\n  CONFIRMATORY: sample ~150 documents BALANCED across the >=4 primary clusters (e.g. 4 clusters x ~38 = 152). Within each cluster prefer documents spanning the feature range (do not pick only the densest) so cross-document feature variance is preserved for S5. Set metadata.is_confirmatory=true.\\n  PILOT: sample a DISJOINT ~30-40 documents, also spread across clusters, for Phase-0 (elicitation/tail-AUC selection) and the S5 power analysis. Set metadata.is_pilot=true, is_confirmatory=false. Pilot docs are 'labeled' simply in that gold is available (all Re-DocRED docs have gold) -- do NOT fabricate negative/decoy triples here; candidate and decoy generation is the experiment's job.\\n  RESERVE (optional): flag another ~30-60 disjoint docs is_reserve=true so the experiment can top up an under-powered cluster without re-running this artifact.\\n  Use a FIXED random seed for all sampling and record it in dataset-level metadata for reproducibility. Ensure confirmatory / pilot / reserve are mutually exclusive (no document appears twice).\\n\\nSTEP 8 -- ASSEMBLE the output row schema. Each row in data_out.json:\\n  {\\n    'id': 'redocred_<split_origin>_<orig_index>',\\n    'input': { 'title', 'text', 'sents', 'sent_char_offsets', 'entities': [ {entity_id, type, canonical_name, n_mentions, mentions:[{name, sent_id, pos, char_span}]} ] },\\n    'output': { 'gold_triples': [ {head_id, head_name, head_type, relation_pid, relation_name, tail_id, tail_name, tail_type, evidence_sent_ids, evidence_text} ] },\\n    'metadata_fold': '<cluster label from STEP 6 primary scheme>',\\n    'metadata': { 'split_origin', 'orig_index', 'is_confirmatory', 'is_pilot', 'is_reserve', 'kmeans_cluster', 'cluster_scheme', 'seed', plus ALL per-document features from STEP 5 (num_words, num_chars, num_sents, num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts, dominant_entity_type, relation_pid_counts, avg_mentions_per_entity, entity_density, mention_density, triple_density, frac_singleton_entities, frac_multi_evidence_triples, max_evidence_sentence_gap), 'gold_caveat': 'Re-DocRED has residual false negatives; supports RELATIVE operational comparisons only, not an absolute FDR diagonal.' }\\n  }\\n  Keep field names exactly aligned with the standard DATASET output contract {input, output, metadata_fold, ...}. Also write companion files: relation_schema.json (96 P-ids), entity_type_schema.json (6 types), and a top-level dataset_meta object (source citation + URLs, split counts, seed, cluster scheme, per-cluster doc counts, the gold_caveat, and a one-line statement that this is the shared triple space all systems map into at matched recall).\\n\\nSTEP 9 -- VALIDATE and SPLIT. Author a JSON Schema for the row and run the aii-json skill to validate every row in data_out.json against it (fail loudly on any missing/extra field or type mismatch). Then use aii-json to generate the full / mini / preview variants (mini = a few rows per cluster incl. at least one pilot row; preview = 1-2 illustrative rows with all fields populated). Run the aii-file-size-limit skill on data_out.json (expected tens of MB, under 300MB) and split only if it exceeds the limit.\\n\\nSTEP 10 -- SANITY REPORT (log, do not put in data_out as derived stats): print final counts (total rows, confirmatory/pilot/reserve, per-cluster), the realized feature ranges per cluster (to confirm cross-document variance exists -- the S5 precondition), the number of unique relation P-ids covered vs 96 and unique entity types covered vs 6, and a handful of fully-rendered example rows (text + entities + a few gold triples with evidence) for eyeball QA. Confirm no document appears in more than one of confirmatory/pilot/reserve, and that every gold triple's head_id/tail_id index a valid entity.\\n\\nFAILURE SCENARIOS & MITIGATIONS:\\n  - HF mirror missing/changed -> GitHub raw fallback (Step 1 fallback A/B); assert schema in Step 2 to catch silent format drift.\\n  - rel_info.json unavailable -> Wikidata wbgetentities API (free, no LLM budget) then hardcoded map (Step 3).\\n  - Cluster imbalance (PER-dominant dominates) -> collapse rare TIME/NUM into MISC, top up from k-means secondary scheme, or split MISC; always keep >=4 balanced, populated clusters (Step 6).\\n  - Documents too short/long or too few triples -> eligibility filter in Step 7 (keep ~80-400 words, >=5 triples) but record length as a feature rather than aggressively discarding.\\n  - Empty evidence on re-annotated triples -> keep the triple with empty evidence arrays (Step 4c); do not drop.\\n  - char_span computation fragile for odd tokenization -> leave char_span null but always retain authoritative token pos (Step 4b).\\n  - Temptation to manufacture negatives/decoys for the pilot -> DO NOT; this is a raw-data artifact. Candidate/decoy/scoring generation is the downstream experiment's responsibility (keeps this strictly within DATASET executor scope).\",\n  \"target_num_datasets\": 1\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [47] ASSISTANT · 2026-06-16 04:50:07 UTC

```
The plan is written. Summary of what I produced:

## Plan: Re-DocRED Operational Anchor

**Compute**: `cpu_heavy` (pure CPU data-prep — download ~25MB, parse, compute per-doc features, cluster, validate).

**Source verified**: `tonytan48/Re-DocRED` on HuggingFace — 3 root JSON files (`train_revised.json` 18.6MB, `dev_revised.json`/`test_revised.json` 3.1MB each), 4,053 docs total. DocRED schema confirmed: `title` / `sents` (token lists) / `vertexSet` (entities→mentions with token-offset `pos` and 6 types PER/ORG/LOC/TIME/NUM/MISC) / `labels` (`h,t,r=P-id,evidence`). Stats: ~198 words, ~19.4 entities, ~28–35 triples, ~8 sentences, 96 Wikidata relations.

**Key planning decisions** the executor needs:
1. **Relation names** — HF mirror ships no `rel_info.json`, so the plan gives a 3-tier resolution: DocRED repo → Wikidata `wbgetentities` API (free, no LLM budget, also yields descriptions for the alignment step) → hardcoded map.
2. **Shared triple schema** — every gold triple emitted as canonical `(head, relation, tail)` with names + evidence sentences + a companion `relation_schema.json`, so all downstream systems map into the identical space.
3. **>=4 clusters** — primary = dominant-entity-type (PER/ORG/LOC/MISC genres) as `metadata_fold` for leave-one-cluster-out CV; secondary k-means on entity+relation profiles stored alongside for robustness.
4. **S5 feature variance** — per-document descriptive features (length, densities, profiles, multi-evidence/evidence-gap multi-hop proxies) stored as raw metadata, with explicit balanced sampling to preserve cross-doc variance.
5. **~150 confirmatory + ~30-40 pilot + reserve**, mutually exclusive, fixed seed.
6. **Scope guardrails** — raw data only; no decoys/scoring/FDR (experiment's job), and the `gold_caveat` (residual false negatives → relative comparisons only) is baked into metadata.

`target_num_datasets: 1` (single-source deep standardization, not a broad search). Failure modes (mirror drift, rel_info absence, cluster imbalance, empty evidence, char-span fragility) each have an explicit mitigation, and aii-json validation + full/mini/preview split + aii-file-size-limit check close it out.

Output written to `./.terminal_claude_agent_struct_out.json`.
```
