# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 2 · `gen_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 03:25:01 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-06-16 03:25:07 UTC

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
  Knockoff-Gated Text-to-Logic: Label-Free False-Discovery-Rate Control of LLM-Extracted Facts and Rules for Hallucination-Bounded
  Neuro-Symbolic Reasoning
hypothesis: >-
  At every point where an LLM proposes symbolic content to add to a logic knowledge base built from a document - (a) atomic
  facts extracted from the text, (b) fuzzy-unification bridges that map a document predicate to an ontology/rule predicate
  when strict unification fails, and (c) implicit common-sense rules that close gaps in a proof - the proposal can be competed
  against matched synthetic 'knockoff' (decoy) items that are engineered to be statistically exchangeable with false proposals
  but are guaranteed not entailed by the document. We hypothesize that thresholding admissions on the decoy-estimated false-discovery
  rate (FDR) - i.e., admitting only proposals whose confidence score beats enough decoys - controls the hallucination rate
  of the resulting SWI-Prolog/ProbLog knowledge base to a user-specified target alpha WITHOUT any ground-truth labels and
  WITHOUT a trusted ontology of constraints. We further hypothesize that this extraction-level FDR control propagates predictably
  to multi-hop deduction, so that a decoy-gated pipeline attains substantially higher atomic-fact precision and a lower hallucinated-conclusion
  rate at matched recall than chain-of-thought, standard RAG, and ungated translate-then-prove neuro-symbolic systems (LINC
  / Logic-LM), while emitting human-auditable proof trace-graphs in which every admitted fact and rule carries the decoy-competition
  certificate that licensed it.
motivation: >-
  Operational text-to-logic pipelines stall on the same crux: when strict symbolic unification fails, the system must let
  an LLM perform fuzzy matching and supply missing common-sense knowledge - and this is precisely where hallucination re-enters
  and silently corrupts every downstream deduction. Today's defenses are unsatisfying for arbitrary professional documents:
  self-consistency and LLM-as-judge are heuristic with no quantitative guarantee; conformal calibration needs a labeled held-out
  set and only certifies single answers; ontology-constraint filtering needs rich trusted constraints and only catches violations
  the ontology happens to encode. None of them gives a practitioner a KNOB that sets the hallucination rate of the extracted
  knowledge base to a chosen target, with a statistical rationale, no labels, and an auditable certificate per admitted fact.
  The genomics and proteomics communities solved an isomorphic problem - selecting true signals among overwhelming noise with
  a guaranteed false-discovery rate and no ground truth - via the knockoff filter and target-decoy competition, by competing
  each real candidate against synthetic negative controls. Importing that principle to the neural-to-symbolic admission boundary
  would convert 'reduce hallucination' from a best-effort aspiration into a controlled, reported quantity. The payoff is a
  reproducible, commodity-hardware neuro-symbolic reader for short legal, news, and narrative documents whose outputs are
  both bounded in hallucination and fully explainable - directly serving the ACL Knowledge Extraction goal of trustworthy,
  auditable fact extraction and reasoning.
assumptions:
- >-
  Exchangeability (the validity condition inherited from target-decoy / knockoff theory): decoys can be constructed whose
  LLM confidence-score distribution matches that of genuinely-false real proposals, so that the count of admitted decoys is
  an unbiased estimate of the count of admitted false reals at any threshold.
- >-
  The LLM emits a usable, roughly monotone confidence/score for each proposed item (real or decoy) that separates document-entailed
  from non-entailed content better than chance; without such separation no thresholding procedure can help.
- >-
  Short, professionally written documents (~3000 characters) are self-contained enough that 'entailed by the document (possibly
  plus admitted common-sense)' is well-defined, so a planted decoy entity/relation/rule that the document does not support
  is genuinely a false proposal.
- >-
  Multi-hop deduction error is dominated by erroneous admitted facts and rules rather than by the symbolic reasoner itself,
  so bounding the admission FDR meaningfully bounds the rate of hallucinated conclusions.
investigation_approach: >-
  Build the pipeline end to end. (1) Extraction: a cheap OpenRouter LLM reads the ~3000-char document and proposes candidate
  atomic facts as typed first-order predicates; argument types are grounded in a commodity upper ontology (a WordNet/ConceptNet/DBpedia-ontology
  slice standing in for OpenCyc) to enable typed decoys and bridge licensing. (2) Decoy generation: for each real candidate,
  synthesize matched knockoffs - entity-swap decoys (same ontological type, absent from the document), relation-swap decoys
  (same arity, not stated), and cross-document decoys (true elsewhere, false here); for fuzzy-unification bridges and gap-filling
  rules, synthesize decoy bridges between unrelated predicate pairs and decoy rules attached to deliberately unsupported sub-goals.
  (3) Scoring: the LLM scores reals and decoys jointly in batched prompts (cost control) returning a confidence per item.
  (4) FDR gate: apply target-decoy competition / the knockoff+ threshold to pick the admission cutoff achieving estimated
  FDR <= alpha, separately for facts, bridges, and rules. (5) Reasoning: admitted facts/rules populate SWI-Prolog (crisp deduction)
  and ProbLog (probabilistic facts with probability set from calibrated scores) for multi-hop inference; backward-chaining
  proofs are exported as trace-graphs whose nodes are annotated with provenance (document span vs ontology vs admitted common-sense)
  and the decoy certificate that cleared each leaf. Evaluate on ProofWriter/RuleTaker (gold facts, rules, and proofs), CLUTRR
  (kinship with paraphrased surface relations, strong compositional constraints, multi-hop, gold graph), and a small hand-annotated
  set of short legal/news/kids'-story documents; gold labels are used ONLY for evaluation - the method is label-free. Experiments:
  (a) Validity-of-control - sweep target alpha and measure realized atomic-fact FDR, testing whether realized tracks target
  along the diagonal (this directly tests the exchangeability assumption); (b) atomic-fact precision/recall vs all baselines
  at matched recall; (c) multi-hop accuracy and hallucinated-conclusion rate vs CoT, RAG, LINC/Logic-LM, and an ablation that
  trusts the LLM's fuzzy unification (no decoy gate); (d) propagation - does tightening alpha monotonically and predictably
  reduce multi-hop hallucination; (e) decoy-construction ablations isolating which decoy families preserve exchangeability;
  (f) cost/commodity check (total LLM spend under the $10 cap, CPU-only runtime) plus qualitative auditable trace-graph examples.
success_criteria: >-
  CONFIRMED if: (1) realized atomic-fact FDR tracks the target alpha within a small tolerance across all three dataset families
  (calibration curve near the diagonal), demonstrating label-free control; (2) at matched recall, decoy-gating yields significantly
  higher atomic-fact precision and a significantly lower hallucinated-conclusion rate than CoT, RAG, and LINC/Logic-LM, and
  than a plain confidence-threshold / self-consistency gate; (3) tightening alpha monotonically and predictably reduces multi-hop
  hallucination, evidencing propagation from extraction-FDR to deduction error; (4) ablating the decoy gate (trusting LLM
  fuzzy unification) measurably worsens hallucination, isolating the gate as the causal mechanism; and (5) the pipeline runs
  on commodity CPU within the $10 LLM budget and produces human-auditable trace-graphs. DISCONFIRMED if: realized FDR systematically
  departs from target (exchangeability fails) and no decoy design repairs it; OR decoy-gating shows no precision/hallucination
  advantage over a simple confidence threshold at matched recall; OR controlling extraction FDR does not translate into controlled
  multi-hop error (error compounding or the symbolic reasoner dominates).
related_works:
- >-
  LINC (Olausson et al., EMNLP 2023): an LLM acts as a semantic parser translating premises into first-order logic that an
  external theorem prover then executes, with majority voting over several translations. Difference: LINC has no principled
  control over WHICH extracted content is admitted - incorrect or hallucinated translations enter the prover freely and voting
  only smooths variance; it offers no false-discovery-rate knob, no synthetic decoys, and no label-free precision guarantee
  on the extracted facts/rules.
- >-
  Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a problem into a symbolic representation that a solver
  runs, with a self-refinement loop driven by the solver's error messages. Difference: refinement repairs syntactic/solver-level
  errors, not factual hallucination - a syntactically valid but fabricated premise is never challenged; there is no statistical
  control of false extractions and no decoy competition.
- >-
  LAMBADA (Kazemi et al., ACL 2023): backward-chaining reasoning where few-shot-prompted LLM modules check whether facts and
  rules support a goal. Difference: every verification step is itself neural (and thus hallucination-prone), there is no symbolic
  knowledge-base admission gate, and there is no quantitative FDR control or synthetic negative control.
- >-
  Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition
  (proteomics mass-spectrometry FDR estimation): select true signals among many candidates with guaranteed FDR by competing
  each real variable/peptide against a synthetic negative control. Difference: this machinery lives entirely in numeric feature
  selection and mass spectrometry; it has never been applied to LLM-proposed symbolic assertions, fuzzy unification, or neuro-symbolic
  reasoning. Our contribution is to adapt it to the neural-to-symbolic boundary and to test whether the required exchangeability
  can be engineered for LLM proposals over text.
- >-
  Conformal-prediction neuro-symbolic methods (e.g., conformal abstention for LLM hallucination; CP with ASP scaffolds; predicate-conditional
  conformalized answer sets for KG embeddings; pipeline-aware split conformal): provide distribution-free coverage guarantees
  for neural/neuro-symbolic outputs. Difference: these require a labeled calibration set and certify the coverage of a single
  predicted answer or a per-query set; our method is label-free and per-document, controls the FDR of a SET of admitted facts/rules
  via decoy competition, and gates the neural-to-symbolic interface rather than the final answer.
- >-
  Ontology-constraint hallucination filtering (e.g., ODKE+, Evontree, SHACL-based validation): reject LLM extractions that
  violate trusted ontology constraints such as disjointness, domain/range, or cardinality. Difference: these need a rich trusted
  constraint set and only catch errors that happen to violate an encoded constraint; decoy-gating requires no trusted constraints
  and controls overall false-admission rate, including where the ontology is silent - it is complementary, not competing.
- >-
  Abductive missing-premise generation/validation in RAG (arXiv 2511.04020) and LLM-to-ProbLog pipelines (e.g., LLM-AR): an
  LLM generates candidate premises or probabilistic rules and an LLM/heuristic validates or executes them. Difference: candidate
  validity is judged neurally (so hallucinated premises can pass) with no statistical false-admission control; our method
  instead competes every neural proposal against synthetic decoys to hold the false-admission rate to a target.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer. The hardest, label-poor problem in genomics and proteomics - deciding
  which of thousands of candidate signals are real when there is no ground truth - is solved with a guaranteed false-discovery
  rate by the knockoff filter (statistics) and target-decoy competition (mass-spectrometry proteomics): manufacture synthetic
  'negative-control' copies engineered to be exchangeable with the noise, let the same selection procedure score reals and
  decoys together, and read off the false-discovery rate from how many decoys sneak through. The imported insight is that
  you can estimate AND control the rate of false discoveries with no labels by competing against engineered decoys. I map
  this onto the exact pressure point of a text-to-logic pipeline - the neural-to-symbolic admission boundary where the LLM
  does fuzzy unification and supplies common-sense knowledge - turning the prompt's vague 'LLM as probabilistic reasoning
  engine for fuzzy unification' into a statistically disciplined gate whose hallucination rate is a tunable, certified, auditable
  quantity.
terms:
- term: Knockoff / decoy fact
  definition: >-
    A synthetic candidate (fact, predicate bridge, or rule) deliberately constructed to be exchangeable with a genuinely-false
    LLM proposal but guaranteed NOT entailed by the source document - e.g., a same-type entity absent from the text, a same-arity
    relation the text never states, or a bridge between unrelated predicates. It serves as a negative control.
- term: False discovery rate (FDR)
  definition: >-
    The expected proportion of admitted items that are actually false (here, the fraction of facts/rules entering the symbolic
    knowledge base that are hallucinated rather than document-entailed). The pipeline targets a user-chosen FDR ceiling alpha.
- term: Target-decoy competition / knockoff+ threshold
  definition: >-
    A label-free selection rule: rank reals and decoys by score, and choose the most permissive admission cutoff at which
    the decoy-estimated FDR (roughly, admitted decoys divided by admitted reals, with a small-sample correction) stays below
    alpha. Items above the cutoff are admitted; the rest are rejected with a logged certificate.
- term: Exchangeability
  definition: >-
    The key validity condition: a false real proposal and its matched decoy are equally likely to receive any given score,
    so counting admitted decoys gives an unbiased estimate of admitted false reals. If this holds, the FDR estimate (and thus
    the control) is valid; testing it is central to the investigation.
- term: Fuzzy unification
  definition: >-
    Matching a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g., 'wrote(x,y)'
    must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic reasoner;
    here each fuzzy match is materialized as a decoy-gated bridge rule.
- term: Bridge rule
  definition: >-
    An explicit, auditable Horn clause (e.g., author_of(X,Y) :- wrote(X,Y)) that records a fuzzy unification as a reusable
    axiom in the logic program, so the alignment appears in the reasoning trace instead of being an opaque per-pair guess.
    Bridge rules are admitted only if they clear the decoy gate.
- term: Neuro-symbolic translation
  definition: >-
    Converting natural-language text into a formal logic representation (first-order predicates and rules) executable by a
    logic reasoner, using an LLM as the translation engine and a symbolic interpreter (SWI-Prolog / ProbLog) as the inference
    engine.
- term: Atomic fact extraction
  definition: >-
    Identifying the individual ground predicates directly asserted by the document (e.g., parent(anna, bob)); measured by
    precision and recall against gold annotations - the prompt's evaluation metric (i).
- term: Multi-hop deduction
  definition: >-
    Reasoning that chains several admitted facts and rules - including implicit common-sense rules - to derive a conclusion
    not stated explicitly (e.g., composing kinship relations across a CLUTRR story); the prompt's evaluation metric (ii).
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf is annotated with its provenance (document span, ontology axiom, or admitted common-sense rule) and the
    decoy-competition certificate that licensed it.
- term: ProbLog
  definition: >-
    A probabilistic extension of Prolog in which facts/rules carry independent probabilities and query probabilities are computed
    over the induced distribution of logic programs; used here to propagate decoy-calibrated confidences through the proof
    so every conclusion gets a probability.
summary: >-
  Borrowing the knockoff filter and target-decoy competition from statistics and proteomics, we gate the neural-to-symbolic
  boundary of a text-to-logic pipeline so that every LLM-proposed fact, fuzzy-unification bridge, and common-sense rule must
  out-compete matched synthetic decoys before entering a Prolog/ProbLog knowledge base - controlling the hallucination rate
  of extracted knowledge to a user-specified target with no ground-truth labels. We predict this label-free false-discovery-rate
  gate propagates to multi-hop reasoning, beating CoT, RAG, and ungated neuro-symbolic baselines on precision and hallucination
  at matched recall while producing auditable proof trace-graphs.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_516bba393d18
overall_assessment: >-
  This is a genuinely creative Level-3 cross-domain transfer: importing the knockoff filter / target-decoy competition (TDC)
  FDR machinery from statistics and proteomics to gate the neural-to-symbolic admission boundary of a text-to-logic pipeline,
  so the hallucination rate of an extracted Prolog/ProbLog knowledge base becomes a tunable, label-free, certified quantity.
  The problem is important and well-aligned with the ACL Knowledge Extraction trustworthiness goal, the writing is clear,
  the related-work coverage is strong, and the proposal is unusually honest about its crux (exchangeability) with explicit,
  well-designed confirm/disconfirm criteria and decoy-family ablations. The auditable trace-graphs with per-leaf decoy certificates
  are a real strength. However, the entire headline claim ('control hallucination to a user-specified alpha without labels')
  is load-bearing on a single assumption — that synthetic decoys are statistically exchangeable with genuinely-false LLM proposals
  (the proteomics 'Equal Chance Assumption') — and both the target-decoy literature and the LLM-calibration literature predict
  this will fail in the anti-conservative direction for the proposed decoy construction: the consequential hallucinations
  are PLAUSIBLE false facts that the LLM scores highly, whereas random type-matched decoys are 'too unrealistic to fool' the
  scorer, which the proteomics literature explicitly notes leads to UNDER-estimated FDP (realized FDR exceeds target). Three
  further issues compound this: (1) the per-document candidate set is tiny (~10-40 items), where TDC is known to be high-variance
  and the knockoff+ offset makes small alpha unachievable; (2) two of three benchmark families (RuleTaker/ProofWriter) present
  facts in near-symbolic form, making the extraction-precision claim near-trivial there, while the realistic setting (legal/news/story)
  is a small hand-annotated set that is likely underpowered for the significance claims; and (3) strong, recent, label-efficient
  baselines (Mohri-Hashimoto conformal factuality; conformal selection + BH; Coherent Factuality) are under-credited and not
  used as baselines, weakening both the novelty framing and the evaluation. None of these is necessarily fatal — the crux
  is directly tested and even a characterization of when ECA holds for LLM proposals would be publishable — but the decoy
  construction must be redesigned to target the realized hallucination distribution, the FDR claim must be re-scoped to corpus-aggregate,
  and the conformal baselines must be added before experiments will produce a defensible top-venue result.
strengths:
- >-
  Genuinely novel cross-domain transfer: target-decoy/knockoff FDR control has lived entirely in feature selection and mass-spectrometry
  proteomics and (per literature search) has not been applied to LLM-proposed symbolic assertions, fuzzy unification, or neuro-symbolic
  reasoning. The 'fully label-free' angle is a real differentiator from conformal methods.
- >-
  Tackles a precise, important, and well-scoped problem — quantitative hallucination control at the exact pressure point (the
  neural-to-symbolic admission boundary where fuzzy unification and common-sense gap-filling occur) — directly serving the
  ACL Knowledge Extraction trustworthiness/auditability goal.
- >-
  Unusually honest and well-structured science: the exchangeability assumption is named as the crux, experiment (a) directly
  tests it (realized vs target alpha along the diagonal), decoy-family ablations (e) isolate which constructions preserve
  exchangeability, and the DISCONFIRMED criteria are concrete and falsifiable. A negative result would still be informative.
- >-
  The auditable trace-graphs with provenance tags (document span vs ontology vs admitted common-sense) and a per-leaf decoy-competition
  certificate are a strong interpretability contribution and differentiate the work from black-box neural baselines.
- >-
  Realistic, reproducible scope: commodity CPU, $10 LLM budget, batched joint scoring of reals+decoys, and a sensible benchmark
  spread (ProofWriter/RuleTaker for gold proofs, CLUTRR for paraphrased multi-hop, plus a hand-annotated realistic set).
dimension_scores:
- dimension: soundness
  score: 2
  justification: >-
    The core validity claim rests on decoy exchangeability (the proteomics Equal Chance Assumption), which both the TDC literature
    and LLM-calibration findings predict will fail in the anti-conservative direction for the proposed random/type-matched
    decoys: plausible hallucinations get high LLM confidence, random decoys get low confidence, so admitted-decoy counts under-estimate
    admitted-false-real counts and realized FDR exceeds target. Compounded by small per-document candidate counts (high-variance
    TDC, unachievable small alpha with the +1 offset) and an unjustified label-free score->ProbLog-probability calibration
    step. The design is honest and tests the crux, but as specified the central guarantee is likely to break.
  improvements:
  - >-
    Redesign decoy construction to match the REALIZED hallucination distribution, not a random null. WHAT: generate decoys
    via the LLM's own plausible-but-document-contradicted counterfactual process (and lean on cross-document decoys, which
    are the closest to the dangerous null), rather than random same-type entity/relation swaps. HOW: prompt the LLM to fabricate
    maximally-plausible facts the document does NOT entail, conditioned on document context, so the decoy score distribution
    matches that of genuine plausible hallucinations. WHY: this is the difference between estimating the FDR of the easy null
    and the consequential null; it directly attacks the anti-conservative failure mode and could move the calibration curve
    onto the diagonal (large soundness impact).
  - >-
    Add a direct ECA diagnostic on a labeled probe set BEFORE trusting any calibration curve. WHAT/HOW: on a held-out labeled
    slice, compare the score distributions of KNOWN-false reals vs their decoys (e.g., two-sample test, win-rate of decoy
    over false real should be ~0.5). WHY: turns the central assumption from hoped-for into measured, and tells you which decoy
    family (if any) achieves exchangeability.
  - >-
    Re-scope the FDR claim from per-document to corpus-aggregate and report the achievable-alpha floor. WHY: per-document
    TDC with ~10-40 items and the knockoff+ offset cannot deliver small alpha; aggregate control is statistically meaningful
    and honestly reportable.
- dimension: presentation
  score: 3
  justification: >-
    Clear, well-organized, with precise terminology, a strong related-work section, and explicit confirm/disconfirm criteria.
    Main deductions: the framing oversells a 'guarantee' that is actually conditional on an empirically fragile assumption,
    and it lumps all conformal methods as 'needs labels / certifies single answers,' which under-credits recent label-efficient
    claim-level conformal FDR work.
  improvements:
  - >-
    Soften 'controls hallucination to a user-specified alpha WITHOUT labels' to a conditional claim ('controls... PROVIDED
    engineered decoys satisfy exchangeability, which we test'). WHY: a top reviewer will otherwise read the unconditional
    guarantee as overclaiming.
  - >-
    Sharpen the true novelty wedge: not 'no one does tunable claim-level alpha' (Mohri-Hashimoto already does, with very few
    labels) but 'fully label-free + gates the neural->symbolic interface + propagates through symbolic deduction with per-leaf
    certificates.' WHY: a precise wedge is more credible and harder to attack.
  - >-
    State explicitly the dependency on the commodity upper-ontology slice for typed decoys and bridge licensing, since the
    abstract claims 'without a trusted ontology of constraints' — clarify it needs typing, not constraints.
- dimension: contribution
  score: 3
  justification: >-
    Original idea attacking a meaningful problem with potential community value (a tunable, auditable hallucination knob for
    text-to-logic). The contribution is somewhat de-risked by the validity question, but even a careful characterization of
    when/if ECA can be engineered for LLM proposals, plus the auditable-trace contribution, would be valuable. Held back from
    4 by the missing strong baselines and the benchmark mismatch that limits how convincingly the headline claims can be demonstrated.
  improvements:
  - >-
    Add Mohri-Hashimoto conformal factuality, conformal selection + BH, and a Coherent-Factuality-style multi-step variant
    as BASELINES (not just related work), at matched label budget. WHY: directly demonstrates the value of label-free-ness
    and situates the contribution against the actual state of the art (large contribution+rigor impact).
  - >-
    Position the work as complementary to ontology-constraint filtering and conformal calibration (it already argues this)
    and show a hybrid (decoy-gate + conformal) ablation. WHY: turns a potential 'why not just use conformal' rejection into
    a contribution.
  - >-
    Commit to releasing the decoy-generation prompts, the calibration harness, and the hand-annotated realistic dataset. WHY:
    reproducible artifacts raise contribution at KE/NeSy venues.
critiques:
- id: ''
  category: rigor
  severity: major
  description: >-
    Exchangeability (the proteomics Equal Chance Assumption) is the single load-bearing assumption, and as specified the decoy
    construction is likely to violate it in the ANTI-CONSERVATIVE direction. The TDC literature is explicit: if decoys are
    'too unrealistic to fool the search engine,' FDP is UNDER-estimated. The LLM-calibration literature shows models assign
    HIGH confidence to plausible hallucinations. The dangerous false reals are precisely the plausible ones (e.g., a reasonable-sounding
    inference the document never states); random same-type entity/relation-swap decoys are easy negatives that the LLM will
    score low. So admitted decoys will under-count admitted false reals, the estimated FDR will be optimistic, and realized
    FDR will exceed target — the opposite of the claimed control. The decoys are exchangeable with the WRONG (easy) null.
  suggested_action: >-
    Generate decoys that match the realized hallucination distribution: have the LLM fabricate maximally-plausible, document-conditioned
    counterfactual facts/bridges/rules (and emphasize cross-document decoys), rather than random type-matched swaps. Then
    validate ECA directly on a labeled probe set by checking that a known-false real and its matched decoy each win the score
    competition ~50% of the time; only proceed to the calibration sweep for decoy families that pass this test. Report the
    win-rate per decoy family as a first-class result.
- id: ''
  category: evidence
  severity: major
  description: >-
    Strong, recent, label-efficient baselines are under-credited and not used as baselines. Mohri & Hashimoto (ICML 2024,
    'Language Models with Conformal Factuality Guarantees') already filters claims to a user-specified factuality alpha with
    'very few human-annotated samples'; conformal selection (Jin & Candes) applies BH to conformal p-values for FDR-controlled
    selection; 'Conformal LM Reasoning with Coherent Factuality' (2505.17126) handles multi-step dependency graphs. The hypothesis
    characterizes conformal methods as needing a labeled calibration set and certifying only single answers, which is no longer
    accurate for claim-level/set-level conformal factuality. This weakens both the novelty framing and the empirical comparison.
  suggested_action: >-
    Add conformal factuality (Mohri-Hashimoto) and conformal-selection+BH as explicit baselines at a matched (small) label
    budget, plus a multi-step coherent-factuality variant for the deduction experiment. Re-sharpen the novelty claim to the
    genuine wedge: fully label-free control that gates the neural->symbolic interface and propagates through symbolic deduction
    with auditable per-leaf certificates. Cite these works in related work and explain precisely what each cannot do that
    decoy-gating can.
- id: ''
  category: rigor
  severity: major
  description: >-
    Small candidate count per document undermines per-document FDR control. A ~3000-character document yields perhaps 10-40
    candidate facts; target-decoy/knockoff estimates are high-variance at this scale (the proteomics literature flags decoy-induced
    variability as 'particularly problematic for smaller FDR thresholds, data sets, or databases'), and the knockoff+ '+1'
    offset makes small alpha unachievable (with k discoveries the minimum non-trivial FDR is ~1/(k+1), so e.g. alpha=0.05
    requires ~20+ admissions). The success criterion 'realized FDR tracks target along the diagonal per dataset family' is
    therefore ill-posed at the per-document level the abstract claims.
  suggested_action: >-
    State explicitly that control is corpus-aggregate (pooled over documents), and report the achievable-alpha floor as a
    function of candidate count. Show the calibration diagonal on pooled discoveries, and report per-document variance separately.
    Consider grouping facts across documents within a dataset to increase the effective number of hypotheses where the application
    allows.
- id: ''
  category: scope
  severity: major
  description: >-
    Benchmark mismatch for the extraction-precision claim. RuleTaker/ProofWriter present facts and rules already in near-symbolic,
    templated form, so 'atomic-fact extraction precision/recall' is near-trivial there and does not stress the hallucination
    gate; the gate's value only appears under paraphrase and genuine textual ambiguity. CLUTRR (paraphrased relations) is
    the meaningful synthetic test, and the realistic legal/news/story setting is where the contribution actually matters —
    but that set is described as 'small hand-annotated,' which is likely underpowered for the strong significance claims in
    success criterion (2).
  suggested_action: >-
    Use RuleTaker/ProofWriter primarily for the reasoner-propagation experiment (where gold proofs are the asset), not for
    the headline extraction-PR claim. Enlarge the realistic annotated set (or add a paraphrased/back-translated RuleTaker
    variant) to obtain adequate power, run a power analysis for the precision/hallucination-rate comparisons, and restrict
    the strong extraction-PR significance claims to CLUTRR and the realistic set.
- id: ''
  category: methodology
  severity: minor
  description: >-
    The ProbLog probabilities are to be 'set from calibrated scores,' but in a fully label-free regime there is no mechanism
    that calibrates raw LLM scores to probabilities — decoy competition yields a SET-level FDR, not a per-fact probability.
    Mapping decoy-competition rank to a ProbLog fact probability is currently unjustified and could silently inject miscalibration
    into every probabilistic conclusion.
  suggested_action: >-
    Either drop the probabilistic-reasoning arm and use crisp admit/reject (cleanest), or specify an explicit, documented
    monotone score->probability map (e.g., isotonic on a small labeled probe, or a fixed heuristic), and ablate its effect
    on conclusion accuracy so the contribution of the probability mapping is separated from the gate itself.
- id: ''
  category: methodology
  severity: minor
  description: >-
    'Matched recall' comparisons across CoT, RAG, LINC/Logic-LM are not operationalized. These baselines do not naturally
    produce an atomic-fact precision-recall curve (CoT/RAG emit free-form text; LINC emits a single translation), so equalizing
    recall to compare precision is underspecified and could be gamed.
  suggested_action: >-
    Specify the recall-matching protocol: for the gated method sweep the admission threshold to trace a full PR curve; for
    free-form baselines define a claim-extraction-and-matching protocol (e.g., decompose outputs into atomic claims, match
    to gold by entailment) and report full PR curves with confidence intervals rather than single matched-recall points.
- id: ''
  category: methodology
  severity: minor
  description: >-
    Decoys are required to be 'guaranteed NOT entailed by the document,' but verifying non-entailment is itself an error-prone
    extraction/reasoning step. A same-type entity 'absent from the document' may be entailed via admitted common-sense, and
    a 'not-stated' relation may follow by deduction — contaminating the negative controls and biasing the FDR estimate.
  suggested_action: >-
    Define and validate the non-entailment check explicitly (e.g., symbolic non-derivability against the admitted KB plus
    a human/LLM entailment audit on a sample), and report the contamination rate of decoys that turn out to be entailed. Exclude
    or down-weight contaminated decoys and quantify the effect on the calibration curve.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The propagation claim ('tightening alpha monotonically and predictably reduces multi-hop hallucination') is optimistic:
    a single false admitted fact can fan out to many false conclusions (amplification), conclusions are conjunctions of admitted
    facts/rules, and the symbolic reasoner is exact, so conclusion-level error is a nonlinear function of fact-level FDR,
    not a smooth monotone transfer. Assumption (d) (deduction error dominated by admitted facts/rules) is plausible but should
    be argued, not asserted.
  suggested_action: >-
    Add a small analytical or Monte-Carlo model linking fact-level FDR to conclusion-level error under the actual proof structures
    (fan-out, conjunction depth) to set quantitative expectations for experiment (d), and measure amplification empirically
    (false conclusions per false admitted fact). This makes 'predictable propagation' a tested quantity rather than a hope.
score: 5
confidence: 4
relation_type:
relation_rationale: ''
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

### [3] HUMAN-USER prompt · 2026-06-16 03:25:07 UTC

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

### [4] ASSISTANT · 2026-06-16 03:26:27 UTC

```
I'll revise my previous hypothesis to address the reviewer's feedback. The instruction is clear: keep the core knockoff/target-decoy transfer, but fix the load-bearing problems. Let me first do targeted research to verify the key additions I'm planning (especially proteomics "entrapment" FDR validation and the conformal baselines the reviewer flagged), then write the revised hypothesis.

Let me load the web tools skill.
```

### [5] TOOL CALL — Skill · 2026-06-16 03:26:27 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 03:26:27 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] ASSISTANT · 2026-06-16 03:26:33 UTC

```
I'll use the built-in WebSearch/WebFetch tools plus the fetch_grep script. Let me load the deferred web tools and run parallel searches to verify my key additions.
```

### [8] TOOL CALL — ToolSearch · 2026-06-16 03:26:33 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [9] TOOL RESULT — ToolSearch · 2026-06-16 03:26:33 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [10] ASSISTANT · 2026-06-16 03:26:45 UTC

```
I'll run parallel searches to verify the conformal baselines, the proteomics entrapment-validation method, and to guard novelty against any prior "decoy FDR for LLM outputs" work.
```

### [11] TOOL CALL — WebSearch · 2026-06-16 03:26:45 UTC

```
Mohri Hashimoto language models conformal factuality guarantees ICML 2024
```

### [12] TOOL CALL — WebSearch · 2026-06-16 03:26:45 UTC

```
conformal selection FDR Jin Candes selecting candidates BH conformal p-values
```

### [13] TOOL CALL — WebSearch · 2026-06-16 03:26:45 UTC

```
entrapment experiments validate target-decoy FDR estimation proteomics equal chance assumption
```

### [14] TOOL CALL — WebSearch · 2026-06-16 03:26:45 UTC

```
knockoff filter false discovery rate LLM hallucination extracted facts text
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 03:26:49 UTC

```
{"query": "Mohri Hashimoto language models conformal factuality guarantees ICML 2024", "results": [{"tool_use_id": "srvtoolu_01M95Y7hbXBqotn9kfwVC2RY", "content": [{"title": "ICML Poster Language Models with Conformal Factuality Guarantees", "url": "https://icml.cc/virtual/2024/poster/32822"}, {"title": "Language Models with Conformal Factuality Guarantees", "url": "https://proceedings.mlr.press/v235/mohri24a.html"}, {"title": "Language Models with Conformal Factuality Guarantees", "url": "https://arxiv.org/pdf/2402.10978"}, {"title": "Language models with conformal factuality guarantees | Proceedings of the 41st International Conference on Machine Learning", "url": "https://dl.acm.org/doi/10.5555/3692070.3693538"}, {"title": "[2402.10978] Language Models with Conformal Factuality Guarantees", "url": "https://arxiv.org/abs/2402.10978"}, {"title": "[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"}, {"title": "Language Models with Conformal Factuality Guarantees", "url": "https://axi.lims.ac.uk/paper/2402.10978"}, {"title": "Language Models with Conformal Factuality Guarantees [Quick Review]", "url": "https://liner.com/review/language-models-with-conformal-factuality-guarantees"}, {"title": "Conformal Language Model Reasoning with Coherent Factuality", "url": "https://arxiv.org/pdf/2505.17126"}, {"title": "Set-Valued Prediction for Large Language Models with Feasibility-Aware Coverage Guarantees", "url": "https://arxiv.org/pdf/2603.22966"}]}, "Based on the search results, I found detailed information about the work by Mohri and Hashimoto on conformal factuality for language models at ICML 2024.\n\n## Overview\n\nChristopher Mohri and Tatsunori Hashimoto published \"Language Models with Conformal Factuality Guarantees\" in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024).\n\n## Main Contribution\n\nThe work proposes conformal factuality, a framework that can ensure high probability correctness guarantees for language models by connecting language modeling and conformal prediction.\n\n## Core Insight and Approach\n\nThe key observation is that the correctness of a language model output is equivalent to an uncertainty quantification problem, where the uncertainty sets are defined as the entailment set of the model's output. Using this connection, conformal prediction in language models corresponds to a back-off algorithm that provides high probability correctness guarantees by progressively making outputs less specific (and expanding the associated uncertainty sets).\n\n## Practical Advantages\n\nThis approach applies to any black-box language model and requires very few human-annotated samples.\n\nThe paper addresses a major challenge in language model deployment: guaranteeing the correctness and factuality of outputs, which is crucial for reliable applications."], "durationSeconds": 6.968898604000001, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-06-16 03:26:52 UTC

```
{"query": "conformal selection FDR Jin Candes selecting candidates BH conformal p-values", "results": [{"tool_use_id": "srvtoolu_0121DhkKJD3HwPBzMryjpTEN", "content": [{"title": "conformal-selection-for-efficient-and-accurate-compound- ...", "url": "https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/672102dcf9980725cf45d9c3/original/conformal-selection-for-efficient-and-accurate-compound-screening-in-drug-discovery.pdf"}, {"title": "(PDF) Selection by Prediction with Conformal p-values", "url": "https://www.researchgate.net/publication/364164553_Selection_by_Prediction_with_Conformal_p-values"}, {"title": "Selection from Hierarchical Data with Conformal e-values", "url": "https://arxiv.org/pdf/2501.02514"}, {"title": "Selection by Prediction with Conformal p-values", "url": "https://www.jmlr.org/papers/volume24/22-1176/22-1176.pdf"}, {"title": "Selective conformal inference with false coverage-statement rate control", "url": "https://arxiv.org/pdf/2301.00584"}, {"title": "Confidence on the Focal: Conformal Prediction with Selection-Conditional   Coverage", "url": "https://arxiv.org/pdf/2403.03868"}, {"title": "Distribution-Free Selection of Low-Risk Oncology Patients for Survival Beyond a Time Horizon", "url": "https://arxiv.org/pdf/2512.18118"}, {"title": "Selection by Prediction with Conformal p-values", "url": "https://arxiv.org/pdf/2210.01408"}]}, "Based on the search results, here's what I found about conformal selection with FDR control by Jin and Candès:\n\n## Overview\n\nJin and Candès proposed Conformal Selection, a prediction-assisted selection framework that controls the false discovery rate (FDR) of the selected set. This method addresses screening procedures in decision-making pipelines such as job hiring and drug discovery that involve selecting candidates whose unobserved outcomes exceed user-specified values.\n\n## Methodology\n\nConformal selection formulates the selection task as a multiple hypotheses testing problem, where each unit in the test set is associated with a hypothesis and rejecting a null hypothesis means selecting the corresponding unit. It then constructs a p-value for each hypothesis, and obtains the selection set by applying the Benjamini Hochberg (BH) procedure to the p-values.\n\n## Key Theoretical Result\n\nJin and Candès proved that the conformal p-values are PRDS (Positive Regression Dependence on a Subset), thereby ensuring the integration of the CP framework while preserving valid FDR control. Under the PRDS property, the Benjamini-Hochberg procedure remains valid.\n\n## FDR Control Guarantee\n\nIt is proved in Jin and Candès that conformal selection achieves FDR control as long as the training and the test data are jointly exchangeable."], "durationSeconds": 8.200728732999996, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-06-16 03:26:52 UTC

```
{"query": "entrapment experiments validate target-decoy FDR estimation proteomics equal chance assumption", "results": [{"tool_use_id": "srvtoolu_018GUSU33jT9NHUgAVCR1Kra", "content": [{"title": "False discovery rate estimation using candidate peptides for each spectrum", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9623924/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | Nature Methods", "url": "https://www.nature.com/articles/s41592-025-02719-x"}, {"title": "(PDF) A theoretical foundation of the target-decoy search strategy for false discovery rate control in proteomics", "url": "https://www.researchgate.net/publication/270515531_A_theoretical_foundation_of_the_target-decoy_search_strategy_for_false_discovery_rate_control_in_proteomics"}, {"title": "A semi-supervised framework for diverse multiple hypothesis testing scenarios", "url": "https://arxiv.org/pdf/2411.15771"}, {"title": "A theoretical foundation of the target-decoy search strategy for false   discovery rate control in proteomics", "url": "https://arxiv.org/pdf/1501.00537"}, {"title": "Fast and Accurate Protein False Discovery Rates on Large-Scale Proteomics Data Sets with Percolator 3.0 | Journal of The American Society for Mass Spectrometry | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s13361-016-1460-7"}, {"title": "An Improved Target-decoy Strategy for Evaluation of Database", "url": "https://www.atlantis-press.com/article/25860148.pdf"}, {"title": "(PDF) Using the entrapment sequence method as a standard to evaluate key steps of proteomics data analysis process", "url": "https://www.researchgate.net/publication/315064040_Using_the_entrapment_sequence_method_as_a_standard_to_evaluate_key_steps_of_proteomics_data_analysis_process"}]}, "I found several relevant sources about entrapment experiments and target-decoy FDR estimation in proteomics. Here are the key findings:\n\n## Entrapment Experiments and FDR Validation\n\nA theoretical framework for entrapment experiments has been proposed, allowing for rigorous characterization of different approaches to FDR control in proteomics. Entrapment experiments have been used empirically to validate assumptions, where a sample of known peptides is used so that the actual false discovery proportion can be gauged.\n\n## Equal Chance Assumption\n\nOne of the basic assumptions of the concatenated target-decoy search strategy is the Equal Chance Assumption. The target-decoy strategy estimates the FDR upon the assumption that when all spectra are identified incorrectly, the probabilities of the spectra matching the target or decoy peptides are identical. However, when the spectrum is identified incorrectly, the probabilities of the spectra matching the target or decoy peptides are not the same, and if these probabilities are not equal, the estimate of the FDR can be inaccurate.\n\n## Validation Through Entrapment Methodology\n\nThe accuracy of FDR estimates has been assessed using sample and entrapment databases to provide ground truth regarding the correctness of peptide identifications. Entrapment experiments have corroborated the assumptions used in target-decoy competition, with studies showing that the FDR is controlled using this approach."], "durationSeconds": 7.257703412000002, "searchCount": 1}
```

### [18] TOOL RESULT — WebSearch · 2026-06-16 03:26:52 UTC

```
{"query": "knockoff filter false discovery rate LLM hallucination extracted facts text", "results": [{"tool_use_id": "srvtoolu_01LhEkspmPfv4Yi1gKBNJRYZ", "content": [{"title": "KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge", "url": "https://arxiv.org/pdf/2602.19643"}, {"title": "The Dawn After the Dark: An Empirical Study on Factuality Hallucination   in Large Language Models", "url": "https://arxiv.org/pdf/2401.03205"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://arxiv.org/pdf/1404.5609"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full"}, {"title": "Controlling the False Discovery Rate via Knockoffs", "url": "https://www.researchgate.net/publication/262982872_Controlling_the_False_Discovery_Rate_via_Knockoffs"}, {"title": "A generalized knockoff procedure for FDR control in structural change detection - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0304407622001567"}]}, "I found search results covering different aspects of your query. Here's what the results show:\n\n## Knockoff Filter and False Discovery Rate (FDR)\n\nThe knockoff filter is a variable selection procedure controlling the FDR in the statistical linear model whenever there are at least as many observations as variables. The method operates by manufacturing knockoff variables that are cheap—their construction does not require any new data—and are designed to mimic the correlation structure found within the existing variables, in a way that allows for accurate FDR control.\n\n## LLM Hallucination and Extracted Facts\n\nRegarding detecting hallucinations in LLM responses, the approach decomposes the challenging hallucination detection task into two simpler subtasks: 1) extract multiple factual statements from a lengthy response; and 2) determine whether each statement contains hallucinations. Instead of training a specific model for fact extraction, researchers leverage the strong instruction-following capabilities of LLMs, and instruct GPT-4 to extract factual statements that could be proven to be true or false according to world knowledge.\n\nHowever, the search results show these are largely separate research areas—knockoff filters for statistical variable selection and methods for detecting LLM hallucinations through fact extraction and verification. There doesn't appear to be direct intersection between these topics in the results returned."], "durationSeconds": 7.237284953999988, "searchCount": 1}
```

### [19] ASSISTANT · 2026-06-16 03:27:22 UTC

```
Strong confirmations: conformal baselines exist as the reviewer described, the proteomics **entrapment** validation method is real and recent (Nature Methods 2025), and there's no prior "decoy/knockoff FDR for LLM-extracted facts" work. Let me fetch the entrapment paper and Coherent Factuality to nail the mechanisms, and run one more novelty guard on plausibility-matched decoy generation.
```

### [20] TOOL CALL — WebFetch · 2026-06-16 03:27:22 UTC

```
URL: https://www.nature.com/articles/s41592-025-02719-x
Prompt: How do entrapment experiments validate the accuracy of target-decoy FDR estimates? What is the entrapment database, how is the realized false discovery proportion measured from spike-in known-false entries, and how does this test the equal chance assumption? Summarize the method precisely.
```

### [21] TOOL RESULT — WebFetch · 2026-06-16 03:27:22 UTC

```
{"bytes": 886, "code": 303, "codeText": "See Other", "result": "REDIRECT DETECTED: The URL redirects to a different host.\n\nOriginal URL: https://www.nature.com/articles/s41592-025-02719-x\nRedirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41592-025-02719-x\nStatus: 303 See Other\n\nTo complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:\n- url: \"https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41592-025-02719-x\"\n- prompt: \"How do entrapment experiments validate the accuracy of target-decoy FDR estimates? What is the entrapment database, how is the realized false discovery proportion measured from spike-in known-false entries, and how does this test the equal chance assumption? Summarize the method precisely.\"", "durationMs": 325, "url": "https://www.nature.com/articles/s41592-025-02719-x"}
```

### [22] TOOL CALL — WebFetch · 2026-06-16 03:27:22 UTC

```
URL: https://arxiv.org/pdf/2505.17126
Prompt: What does Conformal Language Model Reasoning with Coherent Factuality do? How does it handle multi-step reasoning / dependency graphs of claims? Does it require a labeled calibration set? What guarantee does it provide?
```

### [23] TOOL CALL — WebSearch · 2026-06-16 03:27:22 UTC

```
plausibility-matched decoy generation calibrated decoys equal chance assumption competition FDR improved decoy realistic
```

### [24] TOOL RESULT — WebFetch · 2026-06-16 03:27:26 UTC

```
{"bytes": 1409649, "code": 200, "codeText": "OK", "result": "# Conformal Language Model Reasoning with Coherent Factuality\n\n## Overview\nThis work applies conformal prediction to language models to provide statistical guarantees about factuality. The approach enables models to quantify uncertainty about their claims while maintaining coherence across related statements.\n\n## Multi-Step Reasoning & Dependency Graphs\nThe paper addresses how to handle interconnected claims. Rather than treating each statement independently, the method considers relationships between claims. According to the document, it works with \"coherent factuality,\" meaning it maintains consistency across dependent claims in reasoning chains, though the exact mechanism requires examining the full paper's technical sections.\n\n## Calibration Requirements\nYes, the approach requires a labeled calibration set. The conformal prediction framework relies on held-out data to establish validity guarantees, which is standard for this methodology.\n\n## Guarantees Provided\nThe method provides \"conformal\" statistical guarantees—specifically, it ensures that prediction sets (sets of plausible answers) achieve a desired coverage level with high probability. As stated in the document, this approach aims to offer \"validity\" in uncertainty quantification, meaning the model's confidence estimates are calibrated to actual correctness rates across different subgroups and domains.\n\nThe paper builds on prior work by Mohri et al. on conformal factuality, extending these ideas to handle complex reasoning scenarios where multiple claims interact.\n\n[Binary content (application/pdf, 1.3MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-iter-2-gen-hypo-claude-agent/90719c83-04c6-4f47-8239-589640163a39/tool-results/webfetch-1781580438959-99rt3m.pdf]", "durationMs": 6184, "url": "https://arxiv.org/pdf/2505.17126"}
```

### [25] TOOL RESULT — WebSearch · 2026-06-16 03:27:30 UTC

```
{"query": "plausibility-matched decoy generation calibrated decoys equal chance assumption competition FDR improved decoy realistic", "results": [{"tool_use_id": "srvtoolu_01VS16te4ui9XeTRJBykdECm", "content": [{"title": "Protein Language Model Decoys for Target–Decoy Competition in Proteomics: Quality Assessment and Benchmarks | bioRxiv", "url": "https://www.biorxiv.org/content/10.64898/2026.03.27.714819v1.full"}, {"title": "Generating property-matched decoy molecules using deep learning | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/37/15/2134/6126797"}, {"title": "Generating property-matched decoy molecules using deep learning - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8352508/"}, {"title": "Beyond target-decoy competition: stable validation of peptide and protein identifications in mass spectrometry-based discovery proteomics | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/765057v2.full"}, {"title": "Generating property-matched decoy molecules using deep learning", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8352508/"}, {"title": "Generating Property-Matched Decoy Molecules Using Deep Learning", "url": "https://www.biorxiv.org/content/10.1101/2020.08.26.268193.full.pdf"}, {"title": "Generating Property-Matched Decoy Molecules Using Deep Learning | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2020.08.26.268193v1.full"}, {"title": "(PDF) Generating Property-Matched Decoy Molecules Using Deep Learning", "url": "https://www.researchgate.net/publication/349040218_Generating_Property-Matched_Decoy_Molecules_Using_Deep_Learning"}, {"title": "Generating property-matched decoy molecules using deep learning - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/33532838/"}]}, "Based on the web search results, I found relevant information about your query topic. Here are the key findings:\n\n## Equal Chance Assumption and FDR Control\n\nThe Equal Chance Assumption states that target mismatches and decoy matches are equally likely, making it possible to estimate the number of target mismatches for any given cut-off score. The quality of target-decoy competition (TDC) FDR estimates is strictly linked to the Equal Chance Assumption—the decoy's capacity to adequately fool the database search engine. If it fools it too much, the TDC-FDR will overestimate the false discovery proportion; whereas if it is too unrealistic, the FDP will be underestimated.\n\n## Calibrated Decoys\n\nFor spectra that do not correspond to any peptide in the target database, the chances of matching to target or decoy peptides should be equal (0.5/0.5 symmetry in the idealized balanced case), and TDC is well calibrated only if decoy hits reproduce the behavior of false target hits.\n\n## Property-Matched Decoys\n\nDecoys are typically selected to match the chemical properties of active molecules while simultaneously ensuring structure mismatching to minimize the chance of decoys being binders ('property-matched decoys'). Deep learning methods like DeepCoy generated decoy molecules that more closely matched active molecules' physicochemical properties, improving the Deviation from Optimal Embedding score by an average of 81% and 66% respectively."], "durationSeconds": 10.303564765999996, "searchCount": 1}
```

### [26] ASSISTANT · 2026-06-16 03:30:43 UTC

```
This is exactly what I needed. The searches confirm all the pieces of my revision:

1. **The ECA failure mode is documented precisely** — "if [the decoy] is too unrealistic, the FDP will be underestimated" — confirming the reviewer's anti-conservative critique, and pointing to the fix: **property/plausibility-matched decoys** (DeepCoy, protein-LM decoys) where "decoy hits reproduce the behavior of false target hits."
2. **Entrapment** (Nature Methods 2025) is a real, label-free method to *validate* FDR estimates by spiking known-false entries — a perfect import to turn "we hope ECA holds" into "we self-validate it."
3. The conformal baselines (Mohri-Hashimoto, Jin-Candès conformal selection, Coherent Factuality) all **require labeled calibration data** — sharpening my label-free novelty wedge.
4. No prior work applies decoy/knockoff FDR to LLM-extracted symbolic facts.

I have enough to write a strong revision that addresses all eight critiques. Let me write the output.
```

### [27] TOOL CALL — Write · 2026-06-16 03:30:43 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Plausibility-Matched Decoy Competition with Entrapment Validation: Label-Free False-Discovery-Rate Control at the Neural-to-Symbolic Boundary of Text-to-Logic Reasoning",
  "hypothesis": "At every point where an LLM proposes symbolic content to add to a logic knowledge base built from a document - (a) atomic facts extracted from the text, (b) fuzzy-unification bridges that map a document predicate to an ontology/rule predicate when strict unification fails, and (c) implicit common-sense rules that close gaps in a proof - the proposal can be competed against matched synthetic 'decoy' items engineered to reproduce the score behavior of genuinely-false proposals while being verifiably not entailed by the document. We hypothesize that decoy competition controls the false-admission rate of the resulting SWI-Prolog/ProbLog knowledge base to a user-specified corpus-aggregate target alpha WITHOUT ground-truth labels, PROVIDED the decoys are exchangeable with the realized hallucination distribution - and that the necessary exchangeability is NOT achieved by random type-matched swaps (which the target-decoy literature predicts under-estimate FDR because they are 'too easy' for the scorer) but IS approached by plausibility-matched decoys drawn from the LLM's own generative prior over document-plausible-but-non-entailed facts, with cross-document decoys (true elsewhere, false here) as the closest natural null. We further hypothesize that this exchangeability can be CONTINUOUSLY SELF-VALIDATED without labels by an entrapment check imported from proteomics - spiking known-false-by-construction facts into the candidate pool and verifying that the decoy-estimated FDR agrees with the entrapment-measured realized false-admission proportion - and that, where the entrapment check passes, the extraction-level FDR propagates through multi-hop deduction in a way captured by an explicit proof-structure (fan-out/conjunction) model, so that the decoy-gated pipeline attains higher atomic-fact precision and a lower hallucinated-conclusion rate at matched recall than chain-of-thought, RAG, ungated translate-then-prove systems (LINC/Logic-LM), AND label-using conformal-factuality baselines (Mohri-Hashimoto, conformal selection + BH, coherent-factuality), while emitting human-auditable proof trace-graphs in which every admitted fact and rule carries the decoy-competition and entrapment certificate that licensed it.",
  "motivation": "Operational text-to-logic pipelines stall on the same crux: when strict symbolic unification fails, an LLM must perform fuzzy matching and supply missing common-sense knowledge - and this is precisely where hallucination re-enters and silently corrupts every downstream deduction. The most consequential hallucinations are not random nonsense but PLAUSIBLE false facts the model is confident about (a reasonable-sounding inference the document never states). Existing defenses leave a practitioner without a quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and only catches encoded violations; and the strongest recent uncertainty-quantification methods - conformal factuality (Mohri-Hashimoto, ICML 2024), conformal selection with BH (Jin-Candes), and coherent factuality for reasoning chains - all require a labeled calibration set and certify the final answer or a claim set, not the neural-to-symbolic admission boundary. The genomics/proteomics community solved an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed false-discovery rate and no ground truth - via the knockoff filter and target-decoy competition. Critically, that community ALSO learned why naive decoys fail (decoys 'too unrealistic to fool' the scorer make the FDR optimistic) and engineered two cures we import wholesale: PROPERTY-MATCHED decoys that reproduce the false-positive score distribution, and ENTRAPMENT experiments that validate the FDR estimate against a known-false spike-in without labeling the real candidates. Transplanting these to the neural-to-symbolic boundary converts 'reduce hallucination' from a best-effort aspiration into a controlled, self-validated, reported quantity. The wedge over conformal methods is precise and defensible: fully label-free operation, gating at the fuzzy-unification interface rather than the output, and propagation through exact symbolic deduction with a per-leaf certificate - directly serving the ACL Knowledge Extraction goal of trustworthy, auditable fact extraction and reasoning.",
  "assumptions": [
    "Plausibility-matched exchangeability (the revised crux, TESTED not assumed): decoys sampled from the LLM's generative prior over document-plausible-but-non-entailed facts - plus cross-document decoys (true elsewhere, false here) - reproduce the LLM confidence-score distribution of genuinely-false reals, including the high-scoring plausible hallucinations that matter, so admitted decoys are an unbiased estimate of admitted false reals. We do NOT assume this holds; we measure it (decoy-vs-known-false-real win-rate near 0.5 on a small labeled probe), validate it label-free (entrapment agreement), and report per decoy family where it holds or fails in the anti-conservative direction.",
    "Entrapment validity: facts constructed to reference foreign entities injected from an unrelated document or to contradict explicit document content are false-BY-CONSTRUCTION for that document, so the rate at which they are admitted is a label-free estimate of the realized false-admission proportion - usable to validate the decoy-FDR estimate without annotating any real candidate. Entrapment facts must themselves be plausibility-matched, else they test only the easy null.",
    "The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates document-entailed from non-entailed content better than chance; without such separation no thresholding procedure (decoy-gated, conformal, or otherwise) can help.",
    "Corpus-aggregate pooling is the meaningful unit of control: a ~3000-char document yields only ~10-40 candidates, where target-decoy estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable (min non-trivial FDR is ~1/(k+1) with k admissions), so control is asserted over candidates pooled across documents within a dataset family; per-document control is reported as a secondary, high-variance quantity with an explicit achievable-alpha floor.",
    "Multi-hop deduction error is dominated by erroneous admitted facts/rules rather than the exact symbolic reasoner, and the transfer from fact-level FDR to conclusion-level error - including fan-out amplification (one false fact licensing many false conclusions) and conjunction depth (a conclusion needing several admitted leaves) - is captured by an explicit proof-structure model we fit and test, NOT assumed to be a smooth monotone map."
  ],
  "investigation_approach": "Build the pipeline end to end and make the exchangeability crux the central experimental object. (1) Extraction: a cheap OpenRouter LLM reads the ~3000-char document and proposes candidate atomic facts as typed first-order predicates; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc). NOTE we depend on this slice only for TYPING (to constrain decoy generation and license bridges), not for trusted disjointness/cardinality CONSTRAINTS - the FDR claim assumes no constraint ontology. (2) Decoy generation - the key redesign: instead of random same-type entity/relation swaps, decoys are drawn from the LLM's OWN generative prior over plausible-but-false content, conditioned on the document, so their score distribution matches the realized hallucination null. Families compared head-to-head: (i) document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts the document does NOT entail), (ii) cross-document decoys (facts true in a sibling document of the same genre, false here), (iii) the OLD random type-matched swaps as a deliberately-easy baseline expected to fail. Bridges and gap-filling rules get analogous plausible decoys (plausible-but-unsupported predicate alignments and rules attached to unsupported sub-goals). Every decoy passes an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on a sample); we report the decoy contamination rate (decoys that turn out entailed) and exclude/down-weight contaminated ones, quantifying the effect on calibration. (3) Scoring: the LLM scores reals, decoys, and entrapment items jointly in batched prompts (cost control) returning one confidence per item. (4) FDR gate: target-decoy competition / the knockoff+ threshold picks the most permissive admission cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts, bridges, and rules; admitted items enter the KB with a logged certificate, rejected items logged with their losing competition. (5) Entrapment self-validation (label-free): a held-out set of plausibility-matched, false-by-construction entrapment facts is mixed into the pool; after gating, admitted-entrapment / admitted-total estimates the REALIZED false-admission proportion, which we compare against the decoy-estimated FDR - agreement validates ECA, a gap exposes anti-conservatism per family. (6) ECA diagnostic (small labeled probe, used for MEASUREMENT only, not by the operational gate): on a labeled slice, two-sample-test the scores of KNOWN-false reals vs their matched decoys and report the decoy-over-false-real win-rate (target ~0.5) per family - this cross-checks entrapment. (7) Reasoning: admitted facts/rules populate SWI-Prolog for CRISP multi-hop deduction (the primary mode, which keeps the headline FDR contribution independent of any calibration). A ProbLog arm is run only as an ablation, with fact probabilities set by an EXPLICIT, documented monotone score->probability map (isotonic regression fit on the same small labeled probe) whose contribution is ablated against crisp gating so probability miscalibration cannot be confused with the gate's effect. Backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted common-sense) and the decoy+entrapment certificate. (8) Propagation model: a Monte-Carlo simulator injects false facts at controlled FDR into the actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error from fan-out and conjunction depth; we fit it and test whether it predicts the empirically measured amplification (false conclusions per false admitted fact). Datasets: ProofWriter/RuleTaker used PRIMARILY for the reasoner-propagation experiment (gold proofs are the asset) and only secondarily, via a PARAPHRASED/back-translated variant, for extraction; CLUTRR (paraphrased multi-hop kinship, gold graph) and an ENLARGED hand-annotated set of short legal/news/kids'-story documents carry the headline extraction-precision claims, sized by a prospective power analysis. Gold labels are used ONLY for evaluation and the optional probe; the operational gate is label-free. Baselines: CoT, standard RAG, LINC/Logic-LM, an ungated translate-then-prove ablation (trust LLM fuzzy unification), a plain confidence-threshold / self-consistency gate, AND the label-using conformal baselines - Mohri-Hashimoto conformal factuality, conformal selection + BH (Jin-Candes), and a coherent-factuality multi-step variant - each given a matched small label budget; plus a HYBRID decoy-gate + conformal ablation. Matched-recall comparison is operationalized as full precision-recall CURVES: the gated method sweeps its admission threshold; free-form baselines (CoT/RAG) are decomposed into atomic claims and matched to gold by entailment to trace their own PR curve; we report curves with bootstrap confidence intervals, not single matched-recall points. Experiments: (a) validity-of-control - sweep alpha, measure realized corpus-aggregate FDR via entrapment and (where available) gold, test diagonal tracking and report the achievable-alpha floor vs candidate count; (b) decoy-family showdown - win-rate and entrapment agreement per family, testing the prediction that plausibility-matched/cross-document decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction PR curves vs all baselines on CLUTRR + realistic set; (d) multi-hop accuracy / hallucinated-conclusion rate vs all baselines; (e) propagation - does tightening alpha reduce multi-hop hallucination as the fitted proof-structure model predicts, and what is the measured amplification; (f) cost/commodity check (LLM spend under $10, CPU-only) plus qualitative auditable trace-graphs.",
  "success_criteria": "CONFIRMED if: (1) for at least one engineered decoy family, the realized corpus-aggregate atomic-fact FDR tracks the target alpha within a small tolerance on CLUTRR and the realistic set (calibration curve near the diagonal ABOVE the achievable-alpha floor), AND the label-free entrapment estimate of realized false-admission agrees with both the decoy estimate and gold - demonstrating self-validated, label-free control; (2) the decoy-family showdown confirms the mechanism's signature: plausibility-matched and/or cross-document decoys achieve win-rate near 0.5 and entrapment agreement, while random type-matched swaps are measurably anti-conservative (realized FDR exceeds target) - i.e., the redesign, not luck, drives validity; (3) at matched recall (full PR curves with CIs), decoy-gating yields significantly higher atomic-fact precision and lower hallucinated-conclusion rate than CoT, RAG, LINC/Logic-LM, a plain confidence/self-consistency gate, AND the conformal baselines at matched label budget - or, if conformal wins on precision, decoy-gating matches it with ZERO labels (the label-free wedge), and the hybrid improves on both; (4) tightening alpha reduces multi-hop hallucination in the direction and magnitude predicted by the fitted proof-structure model, with measured amplification consistent with the simulator (propagation is a tested quantity); (5) ablating the decoy gate (trusting LLM fuzzy unification) measurably worsens hallucination, isolating the gate as the causal mechanism; and (6) the pipeline runs on commodity CPU within the $10 budget and produces human-auditable trace-graphs with per-leaf decoy+entrapment certificates. DISCONFIRMED if: NO decoy family achieves entrapment-validated diagonal tracking above the alpha-floor (exchangeability is unfixable for LLM proposals, with random AND plausibility-matched decoys both anti-conservative); OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by label-using conformal baselines even accounting for its zero-label advantage; OR controlling extraction FDR does not translate into reduced multi-hop error in any way the proof-structure model can capture (amplification dominates unpredictably or the symbolic reasoner is not the bottleneck). NOTE: a clean negative that CHARACTERIZES when/whether ECA can be engineered for LLM proposals (e.g., 'cross-document decoys pass entrapment on narrative text but fail on legal text') is itself a reportable contribution.",
  "related_works": [
    "Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes claims until a user-specified factuality alpha is met, using conformal prediction and very few human-annotated samples. NOW USED AS A BASELINE. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT (claim set) rather than the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no entrapment self-validation, and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification interface.",
    "Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): builds conformal p-values and applies Benjamini-Hochberg to select candidates with FDR control, proven valid under exchangeability of labeled calibration and test data. NOW USED AS A BASELINE. Difference: it needs labeled calibration outcomes; our method estimates and controls FDR with NO labels by competing each proposal against engineered decoys and self-validates via entrapment. We import the FDR-via-multiple-testing framing but replace the labeled calibration set with decoy competition.",
    "'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126, 2025): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning chains, again with a labeled calibration set. NOW USED AS A BASELINE for the deduction experiment. Difference: labeled, and it guarantees coverage over claim graphs rather than gating which extracted facts/rules enter a symbolic KB; it has no decoy competition, no entrapment validation, and no label-free knob.",
    "Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition, bioRxiv 2026): generate decoys that reproduce the physicochemical/score properties of true positives so target-decoy FDR is well-calibrated. Difference: this lives entirely in molecular screening and mass spectrometry. We import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too easy' - to redesign LLM fact/rule decoys as plausibility-matched counterfactuals, an application that has never existed for LLM-proposed symbolic assertions.",
    "Entrapment experiments for FDR validation in tandem mass spectrometry ('Assessment of false discovery rate control... using entrapment', Nature Methods 2025; entrapment-sequence standards): spike a known-false database into the search and measure the realized false discovery proportion to validate target-decoy estimates without exhaustive ground truth. Difference: a proteomics validation methodology; we transplant it as a label-free internal validity check on LLM fact admission - plausibility-matched, document-false-by-construction entrapment facts whose admission rate validates (or refutes) the decoy-FDR estimate per decoy family.",
    "Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt it to the LLM neural-to-symbolic boundary, confront the Equal-Chance-Assumption failure mode head-on with plausibility-matched decoys, and add entrapment self-validation.",
    "LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into first-order logic executed by a theorem prover, with majority voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated translations enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee.",
    "Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver, with self-refinement on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically valid but fabricated premise is never challenged; no statistical control of false extractions, no decoy competition.",
    "Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including where the ontology is silent - complementary, and we test a hybrid.",
    "Abductive missing-premise generation/validation in RAG (arXiv 2511.04020) and LLM-to-ProbLog pipelines (e.g., LLM-AR): an LLM generates candidate premises/probabilistic rules validated neurally or executed. Difference: candidate validity is judged neurally so hallucinated premises pass, with no statistical false-admission control; we compete every proposal against plausibility-matched decoys and self-validate the rate via entrapment."
  ],
  "inspiration": "A Level-3 (methodological) cross-domain transfer, sharpened by the reviewer's exchangeability critique. Genomics/proteomics solved the hardest label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed false-discovery rate via the knockoff filter (statistics) and target-decoy competition (mass-spectrometry). But that field ALSO discovered why naive negative controls fail: decoys that are 'too unrealistic to fool' the scorer make the FDR optimistic, so they engineered PROPERTY-MATCHED decoys (e.g., DeepCoy, protein-LM decoys) that reproduce the false-positive score distribution, and ENTRAPMENT experiments that validate an FDR estimate against a known-false spike-in WITHOUT labeling the real candidates. I map all three onto the exact pressure point of a text-to-logic pipeline - the neural-to-symbolic admission boundary where the LLM does fuzzy unification and supplies common-sense - and import the matched-decoy and entrapment cures specifically to defeat the anti-conservative failure the reviewer predicted: the dangerous hallucinations are PLAUSIBLE high-confidence false facts, so the decoys must themselves be plausible (drawn from the LLM's generative prior, or true-elsewhere cross-document facts), and the resulting FDR must be continuously self-validated by entrapment. This turns the prompt's vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically disciplined, self-checking, label-free gate whose hallucination rate is a tunable, certified, auditable quantity.",
  "terms": [
    {
      "term": "Plausibility-matched decoy",
      "definition": "A synthetic candidate (fact, bridge, or rule) generated from the LLM's OWN prior over document-plausible-but-non-entailed content - either a document-conditioned counterfactual the model finds plausible, or a fact true in a sibling document but false here - so its confidence-score distribution reproduces that of genuine plausible hallucinations. This is the redesign that replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic."
    },
    {
      "term": "Entrapment validation",
      "definition": "A label-free internal validity check imported from proteomics: spike plausibility-matched, false-BY-CONSTRUCTION facts (e.g., referencing entities injected from an unrelated document) into the candidate pool; after gating, the fraction of admitted items that are entrapment facts estimates the REALIZED false-admission proportion, validating (or exposing a gap in) the decoy-estimated FDR without annotating any real candidate."
    },
    {
      "term": "Equal Chance Assumption (exchangeability)",
      "definition": "The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched decoy are equally likely to receive any given score, so admitted decoys are an unbiased estimate of admitted false reals. If decoys are too unrealistic, admitted decoys UNDER-count admitted false reals and realized FDR exceeds target (anti-conservative). We test it (win-rate ~0.5) and validate it (entrapment) rather than assume it."
    },
    {
      "term": "Decoy-over-false-real win-rate",
      "definition": "An ECA diagnostic computed on a small labeled probe: among matched (known-false real, decoy) pairs, the fraction in which the decoy scores at least as high as the false real. A value near 0.5 indicates exchangeability for that decoy family; values well below 0.5 reveal the anti-conservative failure the reviewer flagged. Used for measurement only, never by the operational gate."
    },
    {
      "term": "Corpus-aggregate FDR and the achievable-alpha floor",
      "definition": "Because a single ~3000-char document yields only ~10-40 candidates - too few for stable target-decoy control, with a minimum non-trivial FDR of ~1/(k+1) at k admissions - control is asserted over candidates POOLED across documents within a dataset family. The achievable-alpha floor (the smallest target alpha reachable given the candidate count and the knockoff+ '+1' offset) is reported explicitly; per-document control is a secondary, high-variance quantity."
    },
    {
      "term": "Target-decoy competition / knockoff+ threshold",
      "definition": "A label-free selection rule: rank reals and decoys by score and choose the most permissive admission cutoff at which the decoy-estimated FDR (admitted decoys + 1, divided by admitted reals) stays below alpha. Items above the cutoff are admitted with a certificate; the rest are rejected with their losing competition logged."
    },
    {
      "term": "Fuzzy unification and bridge rule",
      "definition": "Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g., 'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y)) admitted only if it clears the decoy gate, so the alignment is visible in the trace instead of an opaque per-pair guess."
    },
    {
      "term": "Amplification (fact-FDR to conclusion-error transfer)",
      "definition": "The number of false multi-hop conclusions licensed per false admitted fact. Because conclusions are conjunctions of admitted leaves and a single false fact can fan out across a proof DAG, conclusion-level error is a NONLINEAR function of fact-level FDR; we fit a Monte-Carlo proof-structure model (fan-out, conjunction depth) to predict it and test the prediction empirically."
    },
    {
      "term": "Non-entailment check and contamination rate",
      "definition": "Every decoy and entrapment item must be verifiably NOT entailed by the document. Verifying this is itself error-prone, so we define an explicit check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on a sample) and report the contamination rate - decoys that turn out entailed - excluding or down-weighting them and quantifying the effect on the calibration curve."
    },
    {
      "term": "Trace-graph",
      "definition": "A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications, and each leaf is annotated with its provenance (document span, ontology axiom, or admitted common-sense rule) plus the decoy-competition and entrapment certificate that licensed it."
    },
    {
      "term": "Crisp vs probabilistic reasoning arm",
      "definition": "SWI-Prolog crisp admit/reject deduction is the PRIMARY mode, keeping the FDR contribution independent of any calibration. A ProbLog arm is an ablation in which fact probabilities come from an EXPLICIT isotonic score->probability map fit on a small labeled probe, ablated against crisp gating so probability miscalibration cannot be mistaken for the gate's effect."
    }
  ],
  "summary": "Importing the knockoff filter, property-matched decoys, and entrapment FDR-validation from statistics and proteomics, we gate the neural-to-symbolic boundary of a text-to-logic pipeline so that every LLM-proposed fact, fuzzy-unification bridge, and common-sense rule must out-compete PLAUSIBILITY-MATCHED synthetic decoys - drawn from the LLM's own prior so they mimic real hallucinations - before entering a Prolog/ProbLog knowledge base, controlling the corpus-aggregate hallucination rate to a user-specified target with no labels and continuously self-validating that control via entrapment spike-ins. We predict this label-free, self-checking gate propagates predictably through symbolic deduction (via a fitted fan-out/conjunction model) and beats CoT, RAG, ungated neuro-symbolic, and even label-using conformal-factuality baselines on precision and hallucination at matched recall, while emitting auditable proof trace-graphs with per-leaf decoy+entrapment certificates."
}
```

### [28] TOOL RESULT — Write · 2026-06-16 03:30:43 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Plausibility-Matched Decoy Competition with Entrapment Validation: Label-Free False-Discovery-Rate Control at the Neural-to-Symbolic Boundary of Text-to-Logic Reasoning\",\n  \"hypothesis\": \"At every point where an LLM proposes symbolic content to add to a logic knowledge base built from a document - (a) atomic facts extracted from the text, (b) fuzzy-unification bridges that map a document predicate to an ontology/rule predicate when strict unification fails, and (c) implicit common-sense rules that close gaps in a proof - the proposal can be competed against matched synthetic 'decoy' items engineered to reproduce the score behavior of genuinely-false proposals while being verifiably not entailed by the document. We hypothesize that decoy competition controls the false-admission rate of the resulting SWI-Prolog/ProbLog knowledge base to a user-specified corpus-aggregate target alpha WITHOUT ground-truth labels, PROVIDED the decoys are exchangeable with the realized hallucination distribution - and that the necessary exchangeability is NOT achieved by random type-matched swaps (which the target-decoy literature predicts under-estimate FDR because they are 'too easy' for the scorer) but IS approached by plausibility-matched decoys drawn from the LLM's own generative prior over document-plausible-but-non-entailed facts, with cross-document decoys (true elsewhere, false here) as the closest natural null. We further hypothesize that this exchangeability can be CONTINUOUSLY SELF-VALIDATED without labels by an entrapment check imported from proteomics - spiking known-false-by-construction facts into the candidate pool and verifying that the decoy-estimated FDR agrees with the entrapment-measured realized false-admission proportion - and that, where the entrapment check passes, the extraction-level FDR propagates through multi-hop deduction in a way captured by an explicit proof-structure (fan-out/conjunction) model, so that the decoy-gated pipeline attains higher atomic-fact precision and a lower hallucinated-conclusion rate at matched recall than chain-of-thought, RAG, ungated translate-then-prove systems (LINC/Logic-LM), AND label-using conformal-factuality baselines (Mohri-Hashimoto, conformal selection + BH, coherent-factuality), while emitting human-auditable proof trace-graphs in which every admitted fact and rule carries the decoy-competition and entrapment certificate that licensed it.\",\n  \"motivation\": \"Operational text-to-logic pipelines stall on the same crux: when strict symbolic unification fails, an LLM must perform fuzzy matching and supply missing common-sense knowledge - and this is precisely where hallucination re-enters and silently corrupts every downstream deduction. The most consequential hallucinations are not random nonsense but PLAUSIBLE false facts the model is confident about (a reasonable-sounding inference the document never states). Existing defenses leave a practitioner without a quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and only catches encoded violations; and the strongest recent uncertainty-quantification methods - conformal factuality (Mohri-Hashimoto, ICML 2024), conformal selection with BH (Jin-Candes), and coherent factuality for reasoning chains - all require a labeled calibration set and certify the final answer or a claim set, not the neural-to-symbolic admission boundary. The genomics/proteomics community solved an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed false-discovery rate and no ground truth - via the knockoff filter and target-decoy competition. Critically, that community ALSO learned why naive decoys fail (decoys 'too unrealistic to fool' the scorer make the FDR optimistic) and engineered two cures we import wholesale: PROPERTY-MATCHED decoys that reproduce the false-positive score distribution, and ENTRAPMENT experiments that validate the FDR estimate against a known-false spike-in without labeling the real candidates. Transplanting these to the neural-to-symbolic boundary converts 'reduce hallucination' from a best-effort aspiration into a controlled, self-validated, reported quantity. The wedge over conformal methods is precise and defensible: fully label-free operation, gating at the fuzzy-unification interface rather than the output, and propagation through exact symbolic deduction with a per-leaf certificate - directly serving the ACL Knowledge Extraction goal of trustworthy, auditable fact extraction and reasoning.\",\n  \"assumptions\": [\n    \"Plausibility-matched exchangeability (the revised crux, TESTED not assumed): decoys sampled from the LLM's generative prior over document-plausible-but-non-entailed facts - plus cross-document decoys (true elsewhere, false here) - reproduce the LLM confidence-score distribution of genuinely-false reals, including the high-scoring plausible hallucinations that matter, so admitted decoys are an unbiased estimate of admitted false reals. We do NOT assume this holds; we measure it (decoy-vs-known-false-real win-rate near 0.5 on a small labeled probe), validate it label-free (entrapment agreement), and report per decoy family where it holds or fails in the anti-conservative direction.\",\n    \"Entrapment validity: facts constructed to reference foreign entities injected from an unrelated document or to contradict explicit document content are false-BY-CONSTRUCTION for that document, so the rate at which they are admitted is a label-free estimate of the realized false-admission proportion - usable to validate the decoy-FDR estimate without annotating any real candidate. Entrapment facts must themselves be plausibility-matched, else they test only the easy null.\",\n    \"The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates document-entailed from non-entailed content better than chance; without such separation no thresholding procedure (decoy-gated, conformal, or otherwise) can help.\",\n    \"Corpus-aggregate pooling is the meaningful unit of control: a ~3000-char document yields only ~10-40 candidates, where target-decoy estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable (min non-trivial FDR is ~1/(k+1) with k admissions), so control is asserted over candidates pooled across documents within a dataset family; per-document control is reported as a secondary, high-variance quantity with an explicit achievable-alpha floor.\",\n    \"Multi-hop deduction error is dominated by erroneous admitted facts/rules rather than the exact symbolic reasoner, and the transfer from fact-level FDR to conclusion-level error - including fan-out amplification (one false fact licensing many false conclusions) and conjunction depth (a conclusion needing several admitted leaves) - is captured by an explicit proof-structure model we fit and test, NOT assumed to be a smooth monotone map.\"\n  ],\n  \"investigation_approach\": \"Build the pipeline end to end and make the exchangeability crux the central experimental object. (1) Extraction: a cheap OpenRouter LLM reads the ~3000-char document and proposes candidate atomic facts as typed first-order predicates; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc). NOTE we depend on this slice only for TYPING (to constrain decoy generation and license bridges), not for trusted disjointness/cardinality CONSTRAINTS - the FDR claim assumes no constraint ontology. (2) Decoy generation - the key redesign: instead of random same-type entity/relation swaps, decoys are drawn from the LLM's OWN generative prior over plausible-but-false content, conditioned on the document, so their score distribution matches the realized hallucination null. Families compared head-to-head: (i) document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts the document does NOT entail), (ii) cross-document decoys (facts true in a sibling document of the same genre, false here), (iii) the OLD random type-matched swaps as a deliberately-easy baseline expected to fail. Bridges and gap-filling rules get analogous plausible decoys (plausible-but-unsupported predicate alignments and rules attached to unsupported sub-goals). Every decoy passes an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on a sample); we report the decoy contamination rate (decoys that turn out entailed) and exclude/down-weight contaminated ones, quantifying the effect on calibration. (3) Scoring: the LLM scores reals, decoys, and entrapment items jointly in batched prompts (cost control) returning one confidence per item. (4) FDR gate: target-decoy competition / the knockoff+ threshold picks the most permissive admission cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts, bridges, and rules; admitted items enter the KB with a logged certificate, rejected items logged with their losing competition. (5) Entrapment self-validation (label-free): a held-out set of plausibility-matched, false-by-construction entrapment facts is mixed into the pool; after gating, admitted-entrapment / admitted-total estimates the REALIZED false-admission proportion, which we compare against the decoy-estimated FDR - agreement validates ECA, a gap exposes anti-conservatism per family. (6) ECA diagnostic (small labeled probe, used for MEASUREMENT only, not by the operational gate): on a labeled slice, two-sample-test the scores of KNOWN-false reals vs their matched decoys and report the decoy-over-false-real win-rate (target ~0.5) per family - this cross-checks entrapment. (7) Reasoning: admitted facts/rules populate SWI-Prolog for CRISP multi-hop deduction (the primary mode, which keeps the headline FDR contribution independent of any calibration). A ProbLog arm is run only as an ablation, with fact probabilities set by an EXPLICIT, documented monotone score->probability map (isotonic regression fit on the same small labeled probe) whose contribution is ablated against crisp gating so probability miscalibration cannot be confused with the gate's effect. Backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted common-sense) and the decoy+entrapment certificate. (8) Propagation model: a Monte-Carlo simulator injects false facts at controlled FDR into the actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error from fan-out and conjunction depth; we fit it and test whether it predicts the empirically measured amplification (false conclusions per false admitted fact). Datasets: ProofWriter/RuleTaker used PRIMARILY for the reasoner-propagation experiment (gold proofs are the asset) and only secondarily, via a PARAPHRASED/back-translated variant, for extraction; CLUTRR (paraphrased multi-hop kinship, gold graph) and an ENLARGED hand-annotated set of short legal/news/kids'-story documents carry the headline extraction-precision claims, sized by a prospective power analysis. Gold labels are used ONLY for evaluation and the optional probe; the operational gate is label-free. Baselines: CoT, standard RAG, LINC/Logic-LM, an ungated translate-then-prove ablation (trust LLM fuzzy unification), a plain confidence-threshold / self-consistency gate, AND the label-using conformal baselines - Mohri-Hashimoto conformal factuality, conformal selection + BH (Jin-Candes), and a coherent-factuality multi-step variant - each given a matched small label budget; plus a HYBRID decoy-gate + conformal ablation. Matched-recall comparison is operationalized as full precision-recall CURVES: the gated method sweeps its admission threshold; free-form baselines (CoT/RAG) are decomposed into atomic claims and matched to gold by entailment to trace their own PR curve; we report curves with bootstrap confidence intervals, not single matched-recall points. Experiments: (a) validity-of-control - sweep alpha, measure realized corpus-aggregate FDR via entrapment and (where available) gold, test diagonal tracking and report the achievable-alpha floor vs candidate count; (b) decoy-family showdown - win-rate and entrapment agreement per family, testing the prediction that plausibility-matched/cross-document decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction PR curves vs all baselines on CLUTRR + realistic set; (d) multi-hop accuracy / hallucinated-conclusion rate vs all baselines; (e) propagation - does tightening alpha reduce multi-hop hallucination as the fitted proof-structure model predicts, and what is the measured amplification; (f) cost/commodity check (LLM spend under $10, CPU-only) plus qualitative auditable trace-graphs.\",\n  \"success_criteria\": \"CONFIRMED if: (1) for at least one engineered decoy family, the realized corpus-aggregate atomic-fact FDR tracks the target alpha within a small tolerance on CLUTRR and the realistic set (calibration curve near the diagonal ABOVE the achievable-alpha floor), AND the label-free entrapment estimate of realized false-admission agrees with both the decoy estimate and gold - demonstrating self-validated, label-free control; (2) the decoy-family showdown confirms the mechanism's signature: plausibility-matched and/or cross-document decoys achieve win-rate near 0.5 and entrapment agreement, while random type-matched swaps are measurably anti-conservative (realized FDR exceeds target) - i.e., the redesign, not luck, drives validity; (3) at matched recall (full PR curves with CIs), decoy-gating yields significantly higher atomic-fact precision and lower hallucinated-conclusion rate than CoT, RAG, LINC/Logic-LM, a plain confidence/self-consistency gate, AND the conformal baselines at matched label budget - or, if conformal wins on precision, decoy-gating matches it with ZERO labels (the label-free wedge), and the hybrid improves on both; (4) tightening alpha reduces multi-hop hallucination in the direction and magnitude predicted by the fitted proof-structure model, with measured amplification consistent with the simulator (propagation is a tested quantity); (5) ablating the decoy gate (trusting LLM fuzzy unification) measurably worsens hallucination, isolating the gate as the causal mechanism; and (6) the pipeline runs on commodity CPU within the $10 budget and produces human-auditable trace-graphs with per-leaf decoy+entrapment certificates. DISCONFIRMED if: NO decoy family achieves entrapment-validated diagonal tracking above the alpha-floor (exchangeability is unfixable for LLM proposals, with random AND plausibility-matched decoys both anti-conservative); OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by label-using conformal baselines even accounting for its zero-label advantage; OR controlling extraction FDR does not translate into reduced multi-hop error in any way the proof-structure model can capture (amplification dominates unpredictably or the symbolic reasoner is not the bottleneck). NOTE: a clean negative that CHARACTERIZES when/whether ECA can be engineered for LLM proposals (e.g., 'cross-document decoys pass entrapment on narrative text but fail on legal text') is itself a reportable contribution.\",\n  \"related_works\": [\n    \"Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes claims until a user-specified factuality alpha is met, using conformal prediction and very few human-annotated samples. NOW USED AS A BASELINE. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT (claim set) rather than the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no entrapment self-validation, and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification interface.\",\n    \"Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): builds conformal p-values and applies Benjamini-Hochberg to select candidates with FDR control, proven valid under exchangeability of labeled calibration and test data. NOW USED AS A BASELINE. Difference: it needs labeled calibration outcomes; our method estimates and controls FDR with NO labels by competing each proposal against engineered decoys and self-validates via entrapment. We import the FDR-via-multiple-testing framing but replace the labeled calibration set with decoy competition.\",\n    \"'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126, 2025): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning chains, again with a labeled calibration set. NOW USED AS A BASELINE for the deduction experiment. Difference: labeled, and it guarantees coverage over claim graphs rather than gating which extracted facts/rules enter a symbolic KB; it has no decoy competition, no entrapment validation, and no label-free knob.\",\n    \"Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition, bioRxiv 2026): generate decoys that reproduce the physicochemical/score properties of true positives so target-decoy FDR is well-calibrated. Difference: this lives entirely in molecular screening and mass spectrometry. We import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too easy' - to redesign LLM fact/rule decoys as plausibility-matched counterfactuals, an application that has never existed for LLM-proposed symbolic assertions.\",\n    \"Entrapment experiments for FDR validation in tandem mass spectrometry ('Assessment of false discovery rate control... using entrapment', Nature Methods 2025; entrapment-sequence standards): spike a known-false database into the search and measure the realized false discovery proportion to validate target-decoy estimates without exhaustive ground truth. Difference: a proteomics validation methodology; we transplant it as a label-free internal validity check on LLM fact admission - plausibility-matched, document-false-by-construction entrapment facts whose admission rate validates (or refutes) the decoy-FDR estimate per decoy family.\",\n    \"Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt it to the LLM neural-to-symbolic boundary, confront the Equal-Chance-Assumption failure mode head-on with plausibility-matched decoys, and add entrapment self-validation.\",\n    \"LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into first-order logic executed by a theorem prover, with majority voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated translations enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee.\",\n    \"Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver, with self-refinement on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically valid but fabricated premise is never challenged; no statistical control of false extractions, no decoy competition.\",\n    \"Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including where the ontology is silent - complementary, and we test a hybrid.\",\n    \"Abductive missing-premise generation/validation in RAG (arXiv 2511.04020) and LLM-to-ProbLog pipelines (e.g., LLM-AR): an LLM generates candidate premises/probabilistic rules validated neurally or executed. Difference: candidate validity is judged neurally so hallucinated premises pass, with no statistical false-admission control; we compete every proposal against plausibility-matched decoys and self-validate the rate via entrapment.\"\n  ],\n  \"inspiration\": \"A Level-3 (methodological) cross-domain transfer, sharpened by the reviewer's exchangeability critique. Genomics/proteomics solved the hardest label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed false-discovery rate via the knockoff filter (statistics) and target-decoy competition (mass-spectrometry). But that field ALSO discovered why naive negative controls fail: decoys that are 'too unrealistic to fool' the scorer make the FDR optimistic, so they engineered PROPERTY-MATCHED decoys (e.g., DeepCoy, protein-LM decoys) that reproduce the false-positive score distribution, and ENTRAPMENT experiments that validate an FDR estimate against a known-false spike-in WITHOUT labeling the real candidates. I map all three onto the exact pressure point of a text-to-logic pipeline - the neural-to-symbolic admission boundary where the LLM does fuzzy unification and supplies common-sense - and import the matched-decoy and entrapment cures specifically to defeat the anti-conservative failure the reviewer predicted: the dangerous hallucinations are PLAUSIBLE high-confidence false facts, so the decoys must themselves be plausible (drawn from the LLM's generative prior, or true-elsewhere cross-document facts), and the resulting FDR must be continuously self-validated by entrapment. This turns the prompt's vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically disciplined, self-checking, label-free gate whose hallucination rate is a tunable, certified, auditable quantity.\",\n  \"terms\": [\n    {\n      \"term\": \"Plausibility-matched decoy\",\n      \"definition\": \"A synthetic candidate (fact, bridge, or rule) generated from the LLM's OWN prior over document-plausible-but-non-entailed content - either a document-conditioned counterfactual the model finds plausible, or a fact true in a sibling document but false here - so its confidence-score distribution reproduces that of genuine plausible hallucinations. This is the redesign that replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.\"\n    },\n    {\n      \"term\": \"Entrapment validation\",\n      \"definition\": \"A label-free internal validity check imported from proteomics: spike plausibility-matched, false-BY-CONSTRUCTION facts (e.g., referencing entities injected from an unrelated document) into the candidate pool; after gating, the fraction of admitted items that are entrapment facts estimates the REALIZED false-admission proportion, validating (or exposing a gap in) the decoy-estimated FDR without annotating any real candidate.\"\n    },\n    {\n      \"term\": \"Equal Chance Assumption (exchangeability)\",\n      \"definition\": \"The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched decoy are equally likely to receive any given score, so admitted decoys are an unbiased estimate of admitted false reals. If decoys are too unrealistic, admitted decoys UNDER-count admitted false reals and realized FDR exceeds target (anti-conservative). We test it (win-rate ~0.5) and validate it (entrapment) rather than assume it.\"\n    },\n    {\n      \"term\": \"Decoy-over-false-real win-rate\",\n      \"definition\": \"An ECA diagnostic computed on a small labeled probe: among matched (known-false real, decoy) pairs, the fraction in which the decoy scores at least as high as the false real. A value near 0.5 indicates exchangeability for that decoy family; values well below 0.5 reveal the anti-conservative failure the reviewer flagged. Used for measurement only, never by the operational gate.\"\n    },\n    {\n      \"term\": \"Corpus-aggregate FDR and the achievable-alpha floor\",\n      \"definition\": \"Because a single ~3000-char document yields only ~10-40 candidates - too few for stable target-decoy control, with a minimum non-trivial FDR of ~1/(k+1) at k admissions - control is asserted over candidates POOLED across documents within a dataset family. The achievable-alpha floor (the smallest target alpha reachable given the candidate count and the knockoff+ '+1' offset) is reported explicitly; per-document control is a secondary, high-variance quantity.\"\n    },\n    {\n      \"term\": \"Target-decoy competition / knockoff+ threshold\",\n      \"definition\": \"A label-free selection rule: rank reals and decoys by score and choose the most permissive admission cutoff at which the decoy-estimated FDR (admitted decoys + 1, divided by admitted reals) stays below alpha. Items above the cutoff are admitted with a certificate; the rest are rejected with their losing competition logged.\"\n    },\n    {\n      \"term\": \"Fuzzy unification and bridge rule\",\n      \"definition\": \"Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g., 'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y)) admitted only if it clears the decoy gate, so the alignment is visible in the trace instead of an opaque per-pair guess.\"\n    },\n    {\n      \"term\": \"Amplification (fact-FDR to conclusion-error transfer)\",\n      \"definition\": \"The number of false multi-hop conclusions licensed per false admitted fact. Because conclusions are conjunctions of admitted leaves and a single false fact can fan out across a proof DAG, conclusion-level error is a NONLINEAR function of fact-level FDR; we fit a Monte-Carlo proof-structure model (fan-out, conjunction depth) to predict it and test the prediction empirically.\"\n    },\n    {\n      \"term\": \"Non-entailment check and contamination rate\",\n      \"definition\": \"Every decoy and entrapment item must be verifiably NOT entailed by the document. Verifying this is itself error-prone, so we define an explicit check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on a sample) and report the contamination rate - decoys that turn out entailed - excluding or down-weighting them and quantifying the effect on the calibration curve.\"\n    },\n    {\n      \"term\": \"Trace-graph\",\n      \"definition\": \"A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications, and each leaf is annotated with its provenance (document span, ontology axiom, or admitted common-sense rule) plus the decoy-competition and entrapment certificate that licensed it.\"\n    },\n    {\n      \"term\": \"Crisp vs probabilistic reasoning arm\",\n      \"definition\": \"SWI-Prolog crisp admit/reject deduction is the PRIMARY mode, keeping the FDR contribution independent of any calibration. A ProbLog arm is an ablation in which fact probabilities come from an EXPLICIT isotonic score->probability map fit on a small labeled probe, ablated against crisp gating so probability miscalibration cannot be mistaken for the gate's effect.\"\n    }\n  ],\n  \"summary\": \"Importing the knockoff filter, property-matched decoys, and entrapment FDR-validation from statistics and proteomics, we gate the neural-to-symbolic boundary of a text-to-logic pipeline so that every LLM-proposed fact, fuzzy-unification bridge, and common-sense rule must out-compete PLAUSIBILITY-MATCHED synthetic decoys - drawn from the LLM's own prior so they mimic real hallucinations - before entering a Prolog/ProbLog knowledge base, controlling the corpus-aggregate hallucination rate to a user-specified target with no labels and continuously self-validating that control via entrapment spike-ins. We predict this label-free, self-checking gate propagates predictably through symbolic deduction (via a fitted fan-out/conjunction model) and beats CoT, RAG, ungated neuro-symbolic, and even label-using conformal-factuality baselines on precision and hallucination at matched recall, while emitting auditable proof trace-graphs with per-leaf decoy+entrapment certificates.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [29] ASSISTANT · 2026-06-16 03:30:57 UTC

```
Let me validate the output JSON against the schema.
```

### [30] TOOL CALL — Bash · 2026-06-16 03:30:57 UTC

```
Validate output JSON structure against schema:
python3 -c "
import json
d=json.load(open('.terminal_claude_agent_struct_out.json'))
req=['title','hypothesis','motivation','assumptions','investigation_approach','success_criteria','related_works','inspiration','terms','summary']
for k in req:
    assert k in d, 'MISSING '+k
assert isinstance(d['assumptions'],list) and 2<=len(d['assumptions'])<=5, 'assumptions len '+str(len(d['assumptions']))
assert isinstance(d['related_works'],list), 'related_works'
assert isinstance(d['terms'],list), 'terms'
for t in d['terms']:
    assert set(t.keys())=={'term','definition'}, t.keys()
print('VALID JSON, all required keys present')
print('assumptions:',len(d['assumptions']),'| related_works:',len(d['related_works']),'| terms:',len(d['terms']))
print('title chars:',len(d['title']))
"
```

### [31] TOOL RESULT — Bash · 2026-06-16 03:30:57 UTC

```
{"stdout": "VALID JSON, all required keys present\nassumptions: 5 | related_works: 10 | terms: 11\ntitle chars: 168", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [32] ASSISTANT · 2026-06-16 03:31:03 UTC

```
The output is valid. Let me update the memory file for this revised hypothesis since there's an existing entry for it.
```

### [33] TOOL CALL — Read · 2026-06-16 03:31:03 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
```

### [34] TOOL RESULT — Read · 2026-06-16 03:31:03 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "content": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n", "numLines": 26, "startLine": 1, "totalLines": 26}}
```

### [35] TOOL CALL — Edit · 2026-06-16 03:31:19 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
OLD: Minors: label-free score→ProbLog-prob mapping unjustified; "matched recall" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).
NEW: Minors: label-free score→ProbLog-prob mapping unjustified; "matched recall" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).

**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:
1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): "decoy hits must reproduce false-target-hit behavior."
2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).
3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.
4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.
```

### [36] TOOL RESULT — Edit · 2026-06-16 03:31:19 UTC

```
{"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "oldString": "Minors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).", "newString": "Minors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.", "originalFile": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n", "structuredPatch": [{"oldStart": 23, "oldLines": 3, "newStart": 23, "newLines": 9, "lines": [" 3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.", " 4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.", " Minors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).", "+", "+**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:", "+1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"", "+2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).", "+3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.", "+4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir."]}], "userModified": false, "replaceAll": false}
```

### [37] ASSISTANT · 2026-06-16 03:31:36 UTC

```
Done. The revised hypothesis is written to `.terminal_claude_agent_struct_out.json` (validated against the schema: all 10 required fields, 5 assumptions, 10 related works, 11 terms).

## What I did

Per the instructions, I **revised** the previous knockoff/target-decoy hypothesis rather than replacing it — keeping the genuinely novel cross-domain transfer (FDR control at the neural→symbolic boundary) while fixing every critique. I ran focused research first to ground the fixes, which confirmed:

- The **anti-conservative failure mode is documented** in the target-decoy literature ("too unrealistic to fool → FDP underestimated"), and the proteomics/cheminformatics cure already exists: **property-matched decoys** (DeepCoy, protein-LM decoys).
- **Entrapment** is a real, recent (Nature Methods 2025), *label-free* method to validate FDR estimates — a perfect import.
- All three conformal baselines the reviewer named **require labeled calibration**, which sharpens the label-free wedge.
- No prior work applies decoy/knockoff FDR to LLM-extracted symbolic facts — novelty holds.

## How each critique was addressed

| Critique | Fix |
|---|---|
| **#1 ECA fails anti-conservatively** (major) | Decoys redesigned as **plausibility-matched** — drawn from the LLM's own prior over document-plausible-but-non-entailed facts + cross-document decoys; random swaps kept only as a deliberately-failing baseline. Added win-rate diagnostic (~0.5) and a decoy-family showdown. |
| **#2 conformal baselines missing** (major) | Mohri-Hashimoto, Jin-Candès conformal selection+BH, and Coherent Factuality added as **actual baselines** at matched label budget + a hybrid ablation; novelty wedge re-sharpened to *label-free + interface-gating + symbolic propagation + per-leaf certificates*. |
| **#3 small candidate count** (major) | FDR **re-scoped to corpus-aggregate**, with explicit achievable-α floor (~1/(k+1)). |
| **#4 benchmark mismatch** (major) | RuleTaker/ProofWriter → propagation only; headline extraction-PR restricted to CLUTRR + enlarged realistic set with a power analysis. |
| **#5 ProbLog calibration** (minor) | Crisp SWI-Prolog is now primary; ProbLog is an ablation with an explicit isotonic map, ablated separately. |
| **#6 matched recall** (minor) | Operationalized as full PR curves; free-form baselines decomposed into claims + entailment-matched. |
| **#7 non-entailment errors** (minor) | Explicit non-entailment check + reported contamination rate. |
| **#8 propagation nonlinear** (minor) | Fitted Monte-Carlo fan-out/conjunction model + measured amplification. |

The standout new scientific element is **entrapment-based, label-free self-validation of the FDR gate** — it converts the reviewer's biggest worry ("we just hope exchangeability holds") into a continuously measured, reportable quantity, and makes even a clean negative result publishable.
```
