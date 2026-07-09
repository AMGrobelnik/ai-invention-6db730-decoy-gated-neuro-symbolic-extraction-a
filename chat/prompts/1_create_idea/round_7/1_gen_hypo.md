# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 7 · `gen_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 04:27:07 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<previous_hypothesis>
Your hypothesis from the previous iteration. The reviewer evaluated it below.

hypothesis_id: gen_hypo_1
model: claude-opus-4-8
is_seeded: false
seeds: []
kind: hypothesis
title: >-
  A Label-Free FDR Knob at the Text-to-Logic Admission Boundary via Plausibility-Matched Decoy Competition: Crisp-Gold Calibration
  Validity on CLUTRR and Operational Hallucination-Reduction on Open-Vocabulary Re-DocRED, Robustified Against Score-Dependence
hypothesis: |-
  PLAIN MECHANISM (one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model itself finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate then picks the most permissive admission cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  TWO-ANCHOR DESIGN (the key change this round). The mechanism is tested on two pre-registered confirmatory anchors with a clean division of labor, stated plainly: (A) CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim -- does realized FDR track target alpha (the diagonal) -- and the single primary disconfirmation; CLUTRR tests whether the knob is calibrated, NOT whether it is operationally useful on professional prose. (B) Re-DocRED (human-annotated, open-vocabulary, 96 relation types, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS claim -- atomic-fact precision/recall and hallucinated-conclusion rate versus neural baselines at matched recall -- AND the genuine fuzzy-unification bridge test (free-text relation aligned to a schema/ontology property is real ontology alignment, not a deterministic kinship normalization) AND the document-level predictive model S4 (because real cross-document feature variance lives here, not in CLUTRR). A tiny legal/news/kids'-story set is a qualitative trace-graph demo only (explicitly non-confirmatory).

  WHY THE SPLIT IS PRINCIPLED. CLUTRR gold is exact, so realized FDR can be measured precisely -- the right place for the diagonal. Re-DocRED gold has residual false negatives, so the ABSOLUTE realized FDR is noisy there, but a RELATIVE comparison of all methods under the same shared gold is robust -- the right place for the operational head-to-head. This is why diagonal-tracking is asserted only on CLUTRR while the operational win is asserted only on Re-DocRED.

  THREE LOAD-BEARING NUMBERS (stated once). (1) Demonstrable-alpha range: roughly alpha in [0.05, 0.5]; the knockoff+ '+1' offset gives a minimum estimable FDR ~1/k at k admissions, refined per anchor by the pilot. (2) Corpus & cost: <=300 CLUTRR docs + a pre-registered <=250-doc Re-DocRED subset (>=4 clusters) + ~20 illustrative legal/news/story docs; budget projected ~$2-5, HARD STOP at $10. (3) Label budget: ZERO labels for operation; gold is used only for validation, accounted symmetrically against any labeled baseline's calibration labels.

  SINGLE PRIMARY DISCONFIRMATION (S4-independent, the unfalsifiability fix). On CLUTRR FACTS, under isolated provenance-blinded scoring, at the pilot-powered alpha*: if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than a pre-registered tolerance tau AND the document-block-bootstrap confidence interval lies entirely on the anti-conservative side, the CENTRAL label-free control claim is DISCONFIRMED -- full stop, independent of entrapment agreement and independent of S4. S4 and entrapment are separately-reported secondary findings, never escape hatches that prevent a clean disconfirmation.

  CLAIM CHAIN (each row independently testable; a break is localized and reported).
  | # | CLAIM | TEST | PASS CRITERION | REPORTED ON FAIL |
  |---|-------|------|----------------|------------------|
  | S0 | Score separation (precondition) | Pilot: best elicitation separates entailed vs non-entailed in the UPPER TAIL better than chance; isolated vs lightly-batched scores agree on a labeled slice | tail-AUC>0.5 with CI; isolated~batched | run gated; precondition-failure is the reported result |
  | S1 | Decoy signature (mechanism) | Tail-conditioned win-rate among above-cutoff matched pairs (~0.5) + upper-tail two-sample CDF test | counterfactual decoys ~0.5; random swaps anti-conservative | family flagged anti-conservative |
  | S2 | Calibration validity (CLUTRR) | Sweep alpha; realized FDR vs crisp gold; document-block-bootstrap CI on the diagonal | diagonal tracked within tau above the 1/k floor | PRIMARY DISCONFIRMATION if anti-conservative beyond tau |
  | S3 | Entrapment corroboration (necessary, not sufficient) | Independent tail-matched entrapment; combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E); entrapment passes its own tail-difficulty diagnostic | bound agrees with decoy-FDR and gold; entrapment not too-easy | co-failure reported; too-easy entrapment flagged anti-conservative |
  | S4 | Operational wedge (Re-DocRED) | Matched-recall PR + hallucinated-conclusion rate vs CoT, RAG, and labeled Mohri-Hashimoto conformal | decoy-gating matches/beats all, zero-label operation as wedge | reported as no operational advantage |
  | S5 | Document-level predictive account (Re-DocRED) | Predict per-document tail-exchangeability gap from doc/score features; leave-one-cluster-out + leave-one-document-out CV; pre-registered GAP-regression power analysis | out-of-sample predictive IF >= N_min held-out units | reported DESCRIPTIVE (not predictive) below N_min |
  | S6 | Predictable propagation (preliminary) | Tightening alpha lowers multi-hop hallucinated-conclusion rate | direction + rough magnitude | reported as preliminary |

  SCORE-DEPENDENCE ROBUSTNESS (the methodology fix). knockoff+/TDC validity rests on the null sign-flip property: among genuinely-false candidates, sign(W_i) for W_i=score(real_i)-score(decoy_i) must behave like an independent fair coin conditional on |W_i|. Two design choices threaten this and are explicitly handled: (i) within-document correlation of LLM scoring noise breaks pooled-sign independence -- handled by treating the DOCUMENT as a block (document-block bootstrap for all FDP CIs; never i.i.d. pooled signs); (ii) batched joint scoring induces contrast effects that depress decoy scores anti-conservatively -- handled by ISOLATED, provenance-blinded, order-randomized scoring as the default. Crucially, the pre-registered isolated-vs-batched sensitivity check is the DISCRIMINATOR that separates a scoring artifact from genuine decoy non-exchangeability: if isolating restores the diagonal it was a batching artifact; if anti-conservatism persists under isolated scoring it is genuine non-exchangeability.

  SCOPE. Facts AND bridges carry the headline. CLUTRR bridges are crisp (deterministic kinship) and anchor the diagonal; Re-DocRED bridges are open-vocabulary relation-to-schema alignments and anchor the operational and predictive claims. Defeasible bridges, implicit common-sense rule gating, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S6 are preliminary / if-budget-permits.
motivation: |-
  Text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob there: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and catches only encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, multiple-testing hallucination detection, coherent factuality) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem -- selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth -- via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound built INDEPENDENTLY of the decoys. We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary, turning 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity.

  Why the two-anchor design matters (this round's central reframing). A label-free FDR knob is only valuable if it is BOTH calibrated AND useful where plausible hallucinations actually bite. CLUTRR's closed kinship vocabulary is the right place to prove CALIBRATION (free crisp gold, exact realized FDR) but the WRONG place to prove USEFULNESS (the relation set is tiny and well-known, so plausible hallucinations and genuine ontology-alignment bridges are weakest). We therefore add Re-DocRED -- realistic Wikipedia prose, 96 open relation types, document-level multi-hop, human gold with evidence spans -- as a fully-powered operational anchor where plausible hallucinations are rife and bridges are genuine schema alignments. This squarely answers the prior review: CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful; we never conflate the two.

  Why it matters even at coarse alpha: NO existing label-free method offers ANY FDR knob at the fuzzy-unification interface. A first, auditable, zero-operation-label control -- even at alpha ~0.1 -- converts an uncontrolled hallucination channel into a tunable one with per-leaf certificates. Because LLM decoys carry no theoretical guarantee, the most probable outcome is partial control; the document-level predictive account (S5), now based on Re-DocRED where features genuinely vary, converts a likely-partial result into a generalizable mechanism-level insight about WHEN the calibration holds.
assumptions:
- >-
  TAIL EXCHANGEABILITY AND THE NULL SIGN-FLIP PROPERTY ARE ENGINEERED AND TESTED, NOT GUARANTEED. knockoff+/TDC validity requires
  that, among genuinely-false candidates, sign(W_i) for W_i = score(real_i) - score(decoy_i) behaves like an independent fair
  coin conditional on |W_i| (the null sign-flip property), with each false real and its matched decoy equally likely to receive
  any score in the high-score region near the cutoff. LLM counterfactual decoys carry no construction-level proof of this,
  so we report an empirically-validated calibration (not a theorem) and test the condition IN THE TAIL (tail-conditioned win-rate
  ~0.5 plus an upper-tail two-sample CDF test, not a marginal average).
- >-
  SCORE-DEPENDENCE IS A FIRST-CLASS THREAT AND IS HANDLED, NOT ASSUMED AWAY. Two dependence channels can break the sign-flip
  analysis anti-conservatively: (i) WITHIN-DOCUMENT correlation of LLM scoring noise makes pooled null signs dependent --
  we therefore treat the DOCUMENT as a block, use a document-block bootstrap for all FDP confidence intervals, and never treat
  pooled signs as i.i.d. in the variance/floor analysis; (ii) BATCHED joint scoring induces contrast/ranking effects that
  let the model implicitly detect the fabricated item and depress decoy scores, biasing FDP_hat optimistic -- we therefore
  default to ISOLATED, provenance-blinded, order-randomized scoring, and pre-register an isolated-vs-batched sensitivity check
  that doubles as the DISCRIMINATOR between a scoring artifact (isolation restores the diagonal) and genuine decoy non-exchangeability
  (anti-conservatism persists under isolation).
- >-
  THE SCORE-SEPARATION PRECONDITION MUST BE MET AND IS PILOT-GATED. The LLM must emit a roughly monotone score separating
  document-entailed from non-entailed content better than chance SPECIFICALLY in the upper tail; verbalized confidence is
  documented to be overconfident exactly there, so we do not assume it. A Phase-0 pilot selects the best elicitation (verbalized,
  logprob-derived, self-consistency, DINCO-style distractor-normalized), verifies tail separation, and confirms isolated~batched
  agreement on a labeled slice. The headline budget is gated on the pilot; if no elicitation separates in the tail, that precondition-failure
  is the reported result.
- >-
  TWO-ANCHOR GOLD AND THE DEMONSTRABLE-ALPHA REGIME ARE BOUNDED AND CORPUS-AGGREGATE. Control is asserted over candidates
  pooled within an anchor; a single ~3000-char document yields only ~10-40 candidates, so the smallest demonstrable alpha
  is a joint function of pooled candidate count and entrapment ratio r (roughly [0.05, 0.5], refined by the pilot), widened
  mainly by adding documents. CLUTRR gold is exact, so the calibration DIAGONAL is asserted there; Re-DocRED gold has residual
  false negatives, so on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted (all methods face
  the same incompleteness), never an absolute diagonal. Decoy non-entailment is imperfect: an actually-entailed decoy biases
  the FDR estimate CONSERVATIVE (the safe direction); contamination rate is reported with a sensitivity analysis. Per-document
  rank-normalization precedes pooling, with a diagonal sensitivity check to the normalization choice.
- >-
  S5 IS POWERED WHERE FEATURE VARIANCE ACTUALLY EXISTS, WITH A PRE-REGISTERED PREDICTIVE-VS-DESCRIPTIVE THRESHOLD. The document-level
  tail-exchangeability gap can only be predicted if its input features vary; CLUTRR documents are near-homogeneous in those
  features (entity density, specificity, genre) and yield few per-document admissions at meaningful alpha, so S5 is BASED
  ON Re-DocRED, whose >=4 entity-type/topic clusters supply genuine cross-document variance. The Phase-0 pilot MEASURES and
  reports, on CLUTRR, both the cross-document variance of the S5 features and the expected per-document admitted-count at
  the operative alpha, demonstrating (not assuming) CLUTRR's unsuitability. The S5 unit is the document nested in clusters,
  validated by leave-one-cluster-out and leave-one-document-out CV with a pre-registered power analysis FOR THE GAP REGRESSION
  ITSELF; below a pre-registered minimum number N_min of held-out units with sufficient admissions, S5 is reported as DESCRIPTIVE
  (correlational), not predictive.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then make the two-anchor confirmatory design the central experimental object. Budget split of $10 / CPU-only: ~10% Phase-0 pilot (gates everything, measures CLUTRR feature variance and per-document admitted counts); ~30% CLUTRR calibration headline (the single pre-registered confirmatory cell + decoy showdown + tail-matched entrapment + the calibration diagonal with document-block-bootstrap CIs, facts and bridges); ~30% Re-DocRED operational headline (matched-recall PR + hallucinated-conclusion rate vs CoT, RAG, and conformal; open-vocabulary bridge alignment); ~15% baselines; ~15% secondary (S5 modeling on Re-DocRED, S6 propagation, exploratory rule gating, floor-relaxation).

  FEASIBILITY BUDGET (published before committing). Extraction ~one call/doc over <=550 docs; decoy + entrapment generation ~one call each per doc; SCORING defaults to isolated provenance-blinded calls (each real/decoy/entrapment item scored alone with identity masked and order randomized) -- the dominant cost -- mitigated by a cheap sub-$0.30/M model and, only if the pilot proves isolated~batched agreement, lightly-blinded small batches for the bulk with a full-isolated sensitivity subset. Projected ~$2-5, ~4-8M tokens; cumulative cost logged after every call; HARD STOP at $10.

  PHASE 0 -- PILOT (precondition + powerability). On a few dozen labeled items per anchor: (i) select the elicitation that best separates entailed vs non-entailed IN THE UPPER TAIL; (ii) confirm isolated~batched scoring agreement on a labeled slice (gate batching); (iii) MEASURE on CLUTRR the cross-document variance of the S5 features and the expected per-document admitted-count at the operative alpha; (iv) run a tail power analysis (above-cutoff matched pairs and admitted N_T, N_E needed) AND a GAP-regression power analysis for S5 on Re-DocRED (held-out units needed). Size both corpora to target; gate the full run.

  PIPELINE. (1) EXTRACTION: a cheap OpenRouter LLM proposes typed first-order facts; argument types grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing. (2) DECOY GENERATION: PRIMARY family = document-conditioned counterfactual decoys (maximally-plausible, non-entailed facts/bridges); random type-matched swaps retained as the predicted-anti-conservative baseline; every decoy passes a non-entailment check with reported contamination rate. (3) ENTRAPMENT: independent, tail-matched, false-by-construction (in-genre cross-document swaps, numeric/temporal perturbation, explicit contradiction), mixed at reported ratio r, with its own tail-difficulty diagnostic. (4) SCORING: isolated, provenance-blinded, order-randomized, using the pilot-selected elicitation; rank-normalized per document. (5) FDR GATE: knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges and separately per anchor; admitted items enter the KB with a logged certificate. (6) VARIANCE/CIs: document-block bootstrap throughout. (7) ENTRAPMENT VALIDATION: combined estimator upper-bounds realized false-admission; compare against decoy-FDR and gold; hunt co-failures. (8) TAIL DIAGNOSTICS (measurement only): for both decoys and entrapment, above-cutoff distribution vs gold false-reals + win-rate + upper-tail two-sample test. (9) REASONING: admitted facts/bridges populate SWI-Prolog for multi-hop deduction; backward-chaining proofs export as trace-graphs whose leaves carry provenance plus the decoy + entrapment certificate.

  EXPERIMENTS. (a) CLUTRR validity-of-control: sweep alpha; realized FDR via gold + entrapment bound; diagonal tracking with document-block-bootstrap CIs; normalization sensitivity; ISOLATED-VS-BATCHED sensitivity. (b) Decoy-family showdown + entrapment tail-difficulty. (c) Re-DocRED operational: matched-recall PR curves with CIs and hallucinated-conclusion rate vs CoT, RAG, and Mohri-Hashimoto conformal, with guarantee status side by side. (d) S5 document-level LOO-CV on Re-DocRED with the predictive-vs-descriptive threshold. (e) [preliminary] S6 propagation, exploratory rule gating, floor-relaxation. (f) Cost check (<$10, CPU-only) + auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). The Phase-0 pilot must show the selected score separates entailed from non-entailed content better than chance in the upper tail, that isolated~batched scores agree, and that the S5 power/variance measurements support a per-document or cluster gap regression. If the pilot fails, the reported contribution is the precondition-failure analysis.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent). On CLUTRR FACTS, under isolated provenance-blinded scoring, at the pilot-powered alpha*: the central label-free control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than the pre-registered tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. This is the one crisp result that can falsify the headline, independent of entrapment and of S5.

  CONFIRMED requires ALL of: (1) CALIBRATION VALIDITY (CLUTRR) -- realized FDR tracks target alpha within tau above the 1/k floor across the demonstrable grid, stable under the per-document normalization check and the isolated-vs-batched sensitivity check; (2) DECOY SIGNATURE -- counterfactual decoys reach tail-conditioned win-rate ~0.5 and pass the upper-tail two-sample test while random swaps are measurably anti-conservative, and entrapment passes its own tail-difficulty diagnostic with the combined-estimator bound agreeing with gold; (3) OPERATIONAL WEDGE (Re-DocRED) -- at matched recall (PR curves with document-block-bootstrap CIs), decoy-gating matches or beats CoT, RAG, AND the Mohri-Hashimoto conformal baseline on atomic-fact precision and hallucinated-conclusion rate, with zero-label operation as the wedge. A BH multiplicity correction is applied across all validation tests; non-confirmatory cells are exploratory.

  SECONDARY (separately reported, never escape hatches). (4) S5 document-level model: PREDICTIVE if validated out-of-sample across >= N_min held-out Re-DocRED units, else reported DESCRIPTIVE; either way it characterizes WHICH document/score features govern tail-exchangeability. (5) Entrapment self-corroboration agrees with gold (co-failures reported). (6) S6 -- tightening alpha reduces multi-hop hallucination in the predicted direction. (7) Ablating the decoy gate measurably worsens hallucination. (8) The pipeline runs on commodity CPU within $10 with auditable trace-graphs carrying per-leaf certificates.

  DISCONFIRMED if: the single primary disconfirmation fires (CLUTRR facts anti-conservative beyond tau under isolated scoring); OR, separately for the operational claim, decoy-gating shows no precision/hallucination advantage over CoT/RAG at matched recall on Re-DocRED and is dominated by conformal even accounting for its zero-label disadvantage. An uninterpretable null -- control neither clearly holds nor clearly fails because the tail or gap test is underpowered -- is the true failure the Phase-0 power analysis is designed to prevent.
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
  a synthetic negative control that is exchangeable BY CONSTRUCTION, relying on the null sign-flip property (signs of null
  statistics are i.i.d. coin flips conditional on magnitude). Difference: this machinery lives in numeric feature selection
  and mass spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM neuro-symbolic boundary
  where decoys carry NO such guarantee, so we test the sign-flip/exchangeability condition empirically in the tail, use a
  document-block bootstrap for within-document sign dependence, and model where it holds.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, Bioinformatics 2021; protein-language-model decoys):
  generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference:
  lives in molecular screening; we import the PRINCIPLE -- decoys must reproduce the false-positive score distribution, not
  be 'too easy' -- to design LLM fact/bridge decoys as document-conditioned counterfactuals.
- >-
  Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction' (EMNLP 2022; Re-DocRED).
  Verified by reading the full paper: DocRED comprises 5,053 Wikipedia documents (distant-supervised from Wikidata), averaging
  196.7 words and 19.5 entities, with 97 predefined relation types (96 real relations + no_relation) and human evidence sentences;
  Re-DocRED re-annotates 4,053 of them by adding the missed relation triples (yielding ~13 F1 of headroom) and is publicly
  available. We USE Re-DocRED as our open-vocabulary operational anchor (96 relation types, document-level multi-hop, human
  gold with evidence spans) precisely because it is where plausible hallucinations and genuine schema-alignment bridges actually
  arise; we assert only RELATIVE operational comparisons there (shared residual false negatives affect all methods equally),
  not the absolute FDR diagonal, which we assert on crisp-gold CLUTRR. Note: Re-DocRED documents are SHORT (~200 words, below
  the ~3000-char target), which is strictly easier for commodity hardware; we treat document length itself as an S5 feature.
- >-
  Li, Magesh & Veeravalli, 'Principled Detection of Hallucinations in Large Language Models via Multiple Testing' (arXiv 2508.18473,
  2025). Verified by reading the full paper: it reconceptualizes hallucination detection as hypothesis testing, aggregates
  multiple gray-box evaluation scores via conformal p-values, and applies the GENERAL (dependence-tolerant) Benjamini-Hochberg
  / Benjamini-Yekutieli procedure to control the FALSE-ALARM rate; crucially it 'adds a lightweight calibration step that
  uses a small calibration set of non-hallucinated prompts to provide theoretical control', and it operates at the PROMPT/generation
  level (labeling prompts as likely-to-hallucinate or not). Difference: it is LABELED (a calibration set of non-hallucinated
  prompts) and certifies the generation, whereas we are label-free for operation and gate the neuro-symbolic ADMISSION boundary
  via target-decoy competition with independent entrapment corroboration and per-leaf certificates. This confirmed labeled-calibration
  requirement strengthens our label-free wedge, and our competition-based control differs fundamentally from BH-on-conformal-p-values.
- >-
  Su, Long, Wang, Lin et al., 'Towards Unification of Hallucination Detection and Fact Verification for Large Language Models'
  (UniFact, arXiv 2512.02772, 2025). Verified by reading the paper: UniFact is an EVALUATION framework that enables instance-level
  comparison of model-centric hallucination detection and text-centric fact verification by dynamically generating model outputs
  and corresponding factuality labels; the abstract and content contain NO FDR control, target-decoy/knockoff competition,
  synthetic decoys, admission thresholds, or neuro-symbolic gating, and it requires ground-truth factuality labels. Difference:
  it measures whether generated text is factual; we provide a label-free admission-gating MECHANISM with competition-based
  FDR control and symbolic propagation. We could be EVALUATED under such a framework but our contribution is the control mechanism
  at the text-to-logic boundary.
- >-
  Sawczyn, Binkowski, Janiak, Gabrys & Kajdanowicz, 'FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs'
  (Findings of EACL 2026 / arXiv 2503.17229). Verified by reading the paper: a zero-resource black-box sampling-based method
  that represents text as knowledge-graph triples and computes fine-grained fact-level hallucination SCORES from factual consistency
  across multiple sampled responses (no external resources or training data), improving correction (+35.5% factual content).
  The content has NO false-discovery-rate control, target-decoy/knockoff competition, synthetic decoys, admission thresholds,
  or symbolic gating. Difference: it produces a per-fact detection score with no admission threshold or exchangeability/competition
  argument; FactSelfCheck-style sampling consistency is a CANDIDATE elicitation in our Phase-0 pilot, while our novelty is
  the label-free FDR gate built on whichever elicitation wins.
- >-
  Wang et al., 'Calibrating Verbalized Confidence with Self-Generated Distractors' (DINCO, arXiv 2509.25532, 2025): a zero-resource
  method normalizing verbalized confidence by total confidence over self-generated distractors. Difference: DINCO yields a
  better-calibrated SCALAR confidence for a single claim; it has no FDR control, admission threshold, or competition argument.
  We use DINCO-style distractor-normalized confidence as a candidate pilot elicitation.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm removing claims
  until a factuality alpha is met via conformal prediction with labeled samples. Our primary load-bearing baseline. Difference:
  it requires labeled calibration, certifies the final filtered OUTPUT rather than the admission boundary, and offers no synthetic-decoy
  mechanism, independent entrapment, or symbolic propagation. We report its finite-sample guarantee vs our empirical calibration
  side by side; our wedge is label-free OPERATION.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no operation labels by competing each proposal against engineered
  decoys and corroborate via independent tail-matched entrapment.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023; TDC-SB/UB)
  and He, Ebadi, Keich et al., 'Controlling the FDR via competition: is the +1 needed?' (arXiv 2204.13248, 2023): tighter
  FDP bounds and analysis of the '+1' correction that creates the minimum-estimable-FDR floor. We test (if budget permits)
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
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, sharpened across review rounds. Genomics/proteomics solved the hardest
  label-poor problem -- deciding which of thousands of candidate signals are real with no ground truth -- with a guaranteed
  FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry), and discovered the two ways the
  trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys: DeepCoy,
  protein-LM decoys), and entrapment FDP must be estimated with a valid upper bound (Wen et al., Nature Methods 2025) using
  entrapment built unlike the decoys. I map all three onto the fuzzy-unification boundary of a text-to-logic pipeline, where
  the LLM aligns predicates and supplies background knowledge. Because the dangerous hallucinations are PLAUSIBLE high-confidence
  false facts, the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE
  TAIL, and the FDR must be corroborated by independently-constructed tail-matched entrapment and arbitrated by a small gold
  probe. This round's refinements come from taking the statistical machinery seriously on its own terms: (a) the knockoff
  null SIGN-FLIP property is named explicitly, and the two ways LLM scoring can break it -- within-document score correlation
  and batched-scoring contrast effects -- are handled by a document-block bootstrap and isolated provenance-blinded scoring,
  with the isolated-vs-batched check doubling as the discriminator between a scoring artifact and genuine non-exchangeability;
  (b) the evaluation is split into a CALIBRATION anchor (CLUTRR, crisp free gold, exact diagonal) and an OPERATIONAL anchor
  (Re-DocRED, open-vocabulary human gold, where plausible hallucinations and genuine schema-alignment bridges live), so calibration
  validity and operational usefulness are each demonstrated where they are powerable rather than conflated; (c) the document-level
  predictive account is re-based onto Re-DocRED, where the features it predicts from actually vary, with a pre-registered
  predictive-vs-descriptive threshold; and (d) a single crisp CLUTRR-facts disconfirmation makes the headline falsifiable.
  DINCO's and FactSelfCheck's self-consistency signals become candidate pilot elicitations -- but the novelty is the competition-based,
  label-free FDR gate, not the confidence score.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content -- a document-conditioned counterfactual -- so its score distribution reproduces that of genuine plausible hallucinations.
    It replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Null sign-flip property (the validity condition)
  definition: >-
    The condition knockoff+/TDC FDR control rests on: among genuinely-false candidates, the sign of W_i = score(real_i) -
    score(decoy_i) behaves like an independent fair coin conditional on |W_i|. We name it explicitly because two LLM-scoring
    channels can break it anti-conservatively -- within-document score correlation and batched-scoring contrast effects --
    and design the method to test and protect against both.
- term: Two-anchor evaluation (calibration vs operational)
  definition: >-
    A deliberate split: CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim (the realized-FDR-vs-alpha
    diagonal) and the single primary disconfirmation; Re-DocRED (human-annotated, open-vocabulary, document-level multi-hop)
    hosts the OPERATIONAL-USEFULNESS claim (precision/recall and hallucinated-conclusion rate vs neural baselines at matched
    recall), the genuine schema-alignment bridge test, and the S5 predictive model. CLUTRR proves the knob is calibrated;
    Re-DocRED proves it is useful; the two are never conflated.
- term: Isolated provenance-blinded scoring
  definition: >-
    Each candidate (real, decoy, or entrapment) is scored in its OWN prompt with its source/identity masked and presentation
    order randomized, instead of scoring many candidates jointly in one batched prompt. This removes within-batch contrast/ranking
    effects that would let the model implicitly detect fabricated items and depress decoy scores (an anti-conservative artifact).
    A pre-registered isolated-vs-batched sensitivity check discriminates such an artifact (isolation restores the diagonal)
    from genuine decoy non-exchangeability (anti-conservatism persists).
- term: Document-block bootstrap
  definition: >-
    All FDP/FDR confidence intervals are computed by resampling whole DOCUMENTS (blocks), not individual candidates, so that
    within-document correlation of LLM scoring noise is respected. This replaces the i.i.d.-pooled-sign variance that the
    knockoff '+1' floor argument would otherwise assume, and yields the CI used in the primary disconfirmation.
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
    naive 'sample' ratio; r is propagated into the variance and the achievable-alpha floor. Entrapment is built by a mechanism
    distinct from the decoys and gets its own tail-difficulty diagnostic.
- term: Document-level predictive exchangeability account (S5), re-based on Re-DocRED
  definition: >-
    A model predicting the per-document tail-exchangeability gap (gold-arbitrated departure of realized false-admission from
    target among above-cutoff pairs) from document/score features, fitted on Re-DocRED (whose >=4 entity-type/topic clusters
    supply real cross-document feature variance, unlike near-homogeneous CLUTRR) and validated by leave-one-cluster-out and
    leave-one-document-out CV with a pre-registered GAP-regression power analysis. Below a pre-registered minimum N_min of
    held-out units it is reported DESCRIPTIVE, not predictive.
- term: Open-vocabulary fuzzy-unification bridge (Re-DocRED)
  definition: >-
    On Re-DocRED a bridge aligns a free-text-implied relation to one of 96 schema relation types/ontology properties when
    strict unification fails -- a genuine ontology-alignment decision with real ambiguity, unlike CLUTRR's deterministic kinship
    normalization. This is where the bridge half of the mechanism is tested for operational value; CLUTRR's crisp kinship
    bridges anchor only the calibration diagonal.
- term: Single primary disconfirmation
  definition: >-
    One pre-registered, S4/S5-independent result that can falsify the headline: on CLUTRR FACTS under isolated provenance-blinded
    scoring at the pilot-powered alpha*, if realized corpus-aggregate FDR exceeds alpha* by more than tolerance tau AND the
    document-block-bootstrap CI lies entirely on the anti-conservative side, the central label-free control claim is disconfirmed
    -- regardless of entrapment agreement or S5 outcome.
- term: Demonstrable-alpha range and achievable-alpha floor
  definition: >-
    Control is asserted over candidates pooled within an anchor. The knockoff+ '+1' offset gives a minimum estimable FDR ~1/k
    at k admitted items, and entrapment at ratio r inflates estimator variance, so the smallest demonstrable target alpha
    is a joint function of pooled candidate count and r (roughly [0.05, 0.5], refined by the pilot), widened mainly by adding
    documents and optionally by less-conservative bounds (TDC-SB/UB).
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  Every LLM-proposed fact and fuzzy-unification bridge must out-score a plausibility-matched counterfactual decoy in a target-decoy
  / knockoff+ competition before entering a Prolog knowledge base, giving a label-free FDR knob at the neuro-symbolic admission
  boundary; calibration validity (the realized-FDR-vs-alpha diagonal) is proven on crisp-gold CLUTRR with a single pre-registered
  disconfirmation, operational hallucination-reduction is proven on open-vocabulary Re-DocRED against neural baselines at
  matched recall, and the whole gate is robustified against the two ways LLM scoring can break the knockoff null sign-flip
  property -- within-document correlation (handled by a document-block bootstrap) and batched-scoring contrast effects (handled
  by isolated provenance-blinded scoring whose isolated-vs-batched check discriminates a scoring artifact from genuine non-exchangeability).
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_268b984b2827
overall_assessment: >-
  This is a strong, mature revision of a genuinely novel idea: transplanting the target-decoy / knockoff+ false-discovery-rate
  machinery from proteomics/statistics to the neuro-symbolic admission boundary of a text-to-logic pipeline, giving a label-free,
  auditable FDR knob on which LLM-proposed facts and fuzzy-unification bridges may enter a Prolog KB. Web search confirms
  the transfer is novel (no prior work applies target-decoy/knockoff competition to LLM factuality gating) and that the cited
  Re-DocRED statistics (4,053 re-annotated docs, 96 relations, ~13 F1 headroom) and the labeled-conformal neighbor landscape
  are accurate. The revision addresses all three MAJOR critiques from the prior round in a principled way: (1) the SCOPE critique
  is fixed by the two-anchor design — CLUTRR (crisp free gold) hosts only the calibration-validity diagonal, Re-DocRED (open-vocabulary
  human gold) hosts the operational head-to-head and the S5 predictive model, and the proposal states plainly that CLUTRR
  tests calibration, not usefulness; (2) the METHODOLOGY critique is fixed by naming the null sign-flip property explicitly,
  adopting a document-block bootstrap for all FDP CIs, defaulting to isolated provenance-blinded order-randomized scoring,
  and — elegantly — using the isolated-vs-batched check as the discriminator between a scoring artifact and genuine non-exchangeability;
  (3) the unfalsifiability/RIGOR critique is fixed by a single pre-registered S4/S5-independent primary disconfirmation on
  CLUTRR FACTS. The prior S4/S5 powerability concern is addressed by re-basing the predictive model on Re-DocRED (real feature
  variance) with a pre-registered predictive-vs-descriptive N_min threshold. What remains are execution risks rather than
  conceptual flaws: a tension between the isolated-scoring fix and the $10 budget, under-specification of the operational
  head-to-head construct (and a dropped zero-label confidence-threshold baseline), and a real risk that the CLUTRR-FACTS calibration
  diagonal cannot be populated with enough genuine false admissions to be non-vacuous. None are fatal, but the first three
  should be settled before the headline budget is committed. Overall this is now a borderline-acceptable proposal whose trajectory
  across rounds is clearly upward.
strengths:
- >-
  Genuine, verified novelty: a Level-3 cross-domain transfer of target-decoy / knockoff+ FDR control and the valid combined
  entrapment estimator (Wen et al., Nature Methods 2025) to the LLM text-to-logic admission boundary. Web search confirms
  no existing work applies competition-based FDR control to LLM hallucination gating; the closest neighbors (conformal factuality,
  conformal selection, multiple-testing hallucination detection) are all labeled and are correctly differentiated.
- >-
  Intellectually honest about the weakest joint: LLM counterfactual decoys carry no construction-level exchangeability guarantee,
  so the claim is stated as an empirically-validated calibration (not a theorem) and the sign-flip condition is tested IN
  THE TAIL (tail-conditioned win-rate + upper-tail two-sample CDF test), not as a marginal average.
- >-
  The two-anchor split (calibration on crisp-gold CLUTRR; operational usefulness on open-vocabulary Re-DocRED) is a principled,
  well-justified resolution of the prior scope critique — it puts each claim where it is actually powerable and refuses to
  conflate calibration with usefulness.
- >-
  Sophisticated and correct handling of the dependence threats to knockoff+ validity: the null sign-flip property is named,
  within-document correlation is handled by a document-block bootstrap, batched-contrast effects by isolated provenance-blinded
  scoring, and the isolated-vs-batched sensitivity check is repurposed as the discriminator between a scoring artifact and
  genuine non-exchangeability — a genuinely clever design move.
- >-
  A single, crisp, pre-registered primary disconfirmation (CLUTRR facts, isolated scoring, realized FDR exceeds alpha* by
  tau with a one-sided CI) makes the headline falsifiable and fixes the prior over-hedging concern; S5 and entrapment are
  explicitly demoted from escape hatches to separately-reported secondary findings.
- >-
  Strong methodological hygiene: Phase-0 gating pilot, pre-registered confirmatory cells, BH multiplicity correction across
  validation tests, document-block-bootstrap CIs throughout, explicit demonstrable-alpha floor (~1/k), reported decoy-contamination
  direction (conservative), and a hard $10 budget stop with per-call cost logging.
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The core statistical machinery (knockoff+ thresholding, the valid combined entrapment estimator, the null sign-flip property
    and the two dependence channels that threaten it) is correctly understood and thoughtfully protected. The remaining soundness
    risks are about whether the design can actually realize its tests within budget and difficulty regime, not about conceptual
    errors: (a) the isolated-scoring fix may not fit the $10 budget; (b) the CLUTRR-FACTS diagonal may be too clean to populate
    with genuine false admissions, risking a vacuously-conservative (untestable) result; (c) the operational head-to-head
    construct is under-specified. All three are addressable in the pilot.
  improvements:
  - >-
    Recompute the feasibility budget under DEFAULT isolated scoring (each real/decoy/entrapment scored alone with document
    context re-sent): ~550 docs x ~25 candidates x ~3 item-types is tens of thousands of calls, plausibly far above the stated
    4-8M tokens. Show the arithmetic; if it breaks $10, pre-register exactly what fraction stays isolated and prove the batched
    bulk inherits validity from the full-isolated sensitivity subset.
  - >-
    Add to Phase-0 a measurement of the genuine false-REAL base rate among CLUTRR fact proposals at the operative alpha (not
    just tail separation and admitted count), and pre-register a minimum realized-false-admission count below which the diagonal
    is declared untestable (conservative, not 'tracking'). This protects the primary disconfirmation from firing/non-firing
    for lack of false positives rather than for control.
  - >-
    Concentrate expected value on the precondition: state that the Phase-0 elicitation/tail-separation pilot (S0) is run first
    and that the headline budget is released only on its success, since the most-cited failure mode (LLM overconfidence in
    the upper tail) would otherwise null the entire confirmatory program.
- dimension: presentation
  score: 2
  justification: >-
    Contextualization relative to prior work is excellent and the new plain-mechanism lead sentence, the three load-bearing
    numbers, and the rendered S0-S6 claim table are real improvements. But density — flagged across multiple rounds — remains
    the dominant reading impression: the assumptions, the score-dependence-robustness block, and the motivation are still
    long defensive run-ons that interleave the claim, its caveats, and rebuttals to earlier reviews, which obscures the genuine
    novelty and will cost the ACL presentation score.
  improvements:
  - >-
    Lead every major field with one unqualified sentence of mechanism; move the score-dependence-robustness and the four assumptions
    into a compact table (threat | why it breaks sign-flip | mitigation | test) instead of paragraph walls.
  - >-
    Cut the motivation to two moves: the mechanism, then the two-anchor rationale. The repeated 'this round's reframing /
    the methodology fix' meta-commentary belongs in a changelog, not the hypothesis body.
  - >-
    State the demonstrable-alpha range, document/call counts, and operation-vs-validation label budget exactly once, early
    — currently they recur with slight variations across fields.
- dimension: contribution
  score: 3
  justification: >-
    The problem (an uncontrolled, label-free hallucination channel exactly at the fuzzy-unification boundary) is real and
    underserved, and the proposed first auditable zero-operation-label FDR knob there — with per-leaf certificates and symbolic
    propagation — is a novel capability that others would build on. The ceiling is bounded by the authors' own honest prior
    that the most probable outcome is partial control, but even then the S5 mechanism-level account of WHEN calibration holds
    is a generalizable contribution. The two-anchor design raises the contribution by making the operational claim a powered
    confirmatory anchor rather than an illustrative aside.
  improvements:
  - >-
    Restore the plain confidence-threshold baseline as the primary zero-label comparator in the operational anchor (S4) so
    the contribution isolates the value of the decoy-competition machinery over naive thresholding under an identical zero-label
    budget — otherwise the 'wedge' risks collapsing to 'thresholding is enough'.
  - >-
    Tighten the secondary list: pre-commit that S5/S6/TDC-SB-UB/rule-gating are reported only after the two anchors clear
    their power thresholds, so breadth does not dilute the headline.
critiques:
- id: ''
  category: methodology
  severity: major
  description: >-
    Budget-vs-fix tension. The central methodology fix this round — DEFAULT isolated, provenance-blinded, order-randomized
    scoring (each real, decoy, and entrapment item scored in its own prompt) — multiplies the scoring call count by candidate
    multiplicity and re-sends document context per call. With <=300 CLUTRR + <=250 Re-DocRED + ~20 illustrative docs at ~10-40
    candidates each, plus a 1:1 decoy and entrapment at ratio r, the isolated regime implies on the order of tens of thousands
    of scoring calls, each carrying document context. The stated projection (~4-8M tokens, $2-5, hard stop $10) appears to
    be inherited from the prior BATCHED design (~3 calls/doc) and likely understates isolated-scoring cost by a large factor.
    If the budget forces reverting to batched scoring for the bulk, the very fix that makes the confirmatory run interpretable
    is undermined, and the isolated-vs-batched discriminator weakens because most data is batched.
  suggested_action: >-
    Recompute the feasibility budget explicitly for the isolated default: items = sum over docs of (candidates x {real, decoy,
    r-weighted entrapment}); per-call tokens including document context; total tokens and dollars at the chosen sub-$0.30/M
    model. If it breaches $10, either shrink the confirmatory corpus to what isolated scoring can afford, exploit prompt/context
    caching to amortize the re-sent document, or pre-register the exact isolated fraction and demonstrate in the pilot that
    the batched bulk reproduces the isolated diagonal on a labeled slice before committing the headline.
- id: ''
  category: rigor
  severity: major
  description: >-
    Populability of the CLUTRR-FACTS calibration diagonal, on which the single primary disconfirmation rests. CLUTRR atomic-fact
    extraction over a tiny closed kinship vocabulary is easy, so genuinely-false extracted facts may be rare. The realized-FDR-vs-alpha
    diagonal can only be demonstrated to TRACK alpha if, at permissive cutoffs, a meaningful fraction of admitted reals are
    genuinely false (e.g., realized FDR must be able to rise toward 0.3 at alpha=0.3). If the false-real base rate is low,
    realized FDR sits near zero across the whole grid — trivially <= alpha (conservative everywhere) but NOT tracking — and
    the primary disconfirmation can neither fire nor be cleanly passed, because there are too few false admissions to estimate
    FDR at all. This is precisely the uninterpretable-null outcome the Phase-0 power analysis is meant to prevent, but the
    pilot as described measures tail SEPARATION and per-document admitted COUNT, not the genuine false-positive base rate
    among admissions.
  suggested_action: >-
    Add to Phase-0 an explicit measurement, on CLUTRR facts at the operative alpha*, of the realized genuinely-false-admission
    count and base rate among proposals. Pre-register a minimum false-admission count below which the CLUTRR-facts diagonal
    is declared untestable (conservative, not tracking) rather than confirmatory. If the count is too low, deliberately enrich
    the false-real pool (e.g., harder multi-hop inferred relations the extractor gets wrong) or move the primary disconfirmation
    to CLUTRR BRIDGES, where multi-hop kinship inference produces denser errors.
- id: ''
  category: methodology
  severity: major
  description: >-
    Operational head-to-head construct validity, plus a dropped baseline. The S4 operational confirmatory claim compares atomic-fact
    precision/recall and 'hallucinated-conclusion rate' of the neuro-symbolic pipeline against CoT, RAG, and labeled Mohri-Hashimoto
    conformal 'at matched recall.' Two problems: (a) CoT and RAG are generation/QA systems, not atomic-fact extractors in
    a shared schema, so 'matched-recall PR curves' across them is under-specified — you need a defined common extraction target
    and an explicit, fair mapping from each baseline's free-text output to comparable atomic facts and conclusions, or the
    comparison is apples-to-oranges; (b) the plain per-document/per-corpus confidence-threshold baseline — present as S3 in
    the prior iteration and the single most diagnostic ZERO-LABEL comparator — has been dropped from the headline operational
    set. Without it, S4 cannot show that the decoy-competition machinery adds operational value over naive confidence thresholding
    at the SAME zero-label budget; the 'wedge' could reduce to 'a confidence threshold already matches recall-for-recall.'
  suggested_action: >-
    Specify the shared atomic-fact evaluation schema and the precise procedure for extracting comparable facts/conclusions
    from CoT and RAG outputs (e.g., a fixed claim-decomposition + alignment-to-Re-DocRED-relations step applied identically
    to all systems). Restore the plain confidence-threshold gate as the primary zero-label baseline in S4, so the operational
    wedge is measured as decoy-gating vs thresholding under identical labels, with labeled conformal reported alongside as
    the labeled reference point.
- id: ''
  category: scope
  severity: minor
  description: >-
    Breadth vs depth on a $10 / CPU-only budget. The proposal now spans S0-S6 (seven claim rows), two anchors, three-plus
    baselines, an S5 model validated by both leave-one-cluster-out and leave-one-document-out CV with its own gap-regression
    power analysis, S6 propagation, and several 'if-budget-permits' threads (TDC-SB/UB, '+1'-floor relaxation, ProbLog/isotonic,
    defeasible bridges, rule gating). This is a lot of surface area for a one-call/doc pipeline under a hard $10 cap, and
    the prior rounds repeatedly pushed toward focus. The risk is that several cells end up underpowered and nothing is decisively
    nailed.
  suggested_action: >-
    Pre-commit a strict budget waterfall: fully power the CLUTRR calibration diagonal and the Re-DocRED operational wedge
    FIRST, and explicitly state that S5/S6/floor-relaxation/rule-gating are run and reported only if the two anchors clear
    their pre-registered power thresholds, with leftover budget. Make this ordering visible in the feasibility section so
    a reviewer sees the headline cannot be starved by secondary exploration.
- id: ''
  category: evidence
  severity: minor
  description: >-
    The labeled-conformal-for-LLM frontier is moving fast and a top reviewer will expect current awareness. Beyond the cited
    Li et al. (2508.18473), Mohri-Hashimoto, and Jin-Candes, recent work directly applies conformal SELECTION / multiple testing
    to LLM claim filtering (e.g., feedback-enhanced online multiple testing for conformal selection, 2025; differentiable
    coherent factuality, 2026; conformal-factuality robustness for RAG, 2026). These are not novelty threats — they remain
    LABELED and certify outputs rather than gating the neuro-symbolic admission boundary via competition — so they actually
    reinforce the label-free wedge, but the proposal should show it knows them.
  suggested_action: >-
    Add one or two sentences placing the work against the conformal-selection-applied-to-LLM-claims line, reusing the existing
    axes (label-free operation vs labeled calibration; competition/per-leaf certificates + symbolic propagation vs output-level
    certification). Low priority relative to the methodology and rigor critiques.
- id: ''
  category: clarity
  severity: minor
  description: >-
    Density remains the dominant presentation weakness despite genuine improvements (plain-mechanism lead, three load-bearing
    numbers, the claim table). The assumptions, the score-dependence-robustness block, and the motivation are still long defensive
    run-ons that interleave claim, caveat, and rebuttal-to-prior-review, which obscures the core novelty and will cost the
    ACL presentation score. This has been flagged in multiple rounds; with the methodology now strong, presentation is a primary
    remaining score lever.
  suggested_action: >-
    Convert the score-dependence-robustness and assumptions prose into a compact table (threat | how it breaks the sign-flip
    property | mitigation | pre-registered test). Lead each field with one unqualified mechanism sentence before any caveat.
    Remove the round-over-round meta-commentary ('the key change this round', 'the methodology fix') from the hypothesis body.
    State the demonstrable-alpha range, doc/call counts, and label budget once.
score: 5
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same decoy-competition FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.
</previous_review_feedback><user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Concise, self-explanatory title",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 04:27:07 UTC

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
