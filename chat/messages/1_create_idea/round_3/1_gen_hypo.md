# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 3 · `gen_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 03:37:34 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_3/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-06-16 03:37:40 UTC

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
  Plausibility-Matched Decoy Competition with Entrapment Validation: Label-Free False-Discovery-Rate Control at the Neural-to-Symbolic
  Boundary of Text-to-Logic Reasoning
hypothesis: >-
  At every point where an LLM proposes symbolic content to add to a logic knowledge base built from a document - (a) atomic
  facts extracted from the text, (b) fuzzy-unification bridges that map a document predicate to an ontology/rule predicate
  when strict unification fails, and (c) implicit common-sense rules that close gaps in a proof - the proposal can be competed
  against matched synthetic 'decoy' items engineered to reproduce the score behavior of genuinely-false proposals while being
  verifiably not entailed by the document. We hypothesize that decoy competition controls the false-admission rate of the
  resulting SWI-Prolog/ProbLog knowledge base to a user-specified corpus-aggregate target alpha WITHOUT ground-truth labels,
  PROVIDED the decoys are exchangeable with the realized hallucination distribution - and that the necessary exchangeability
  is NOT achieved by random type-matched swaps (which the target-decoy literature predicts under-estimate FDR because they
  are 'too easy' for the scorer) but IS approached by plausibility-matched decoys drawn from the LLM's own generative prior
  over document-plausible-but-non-entailed facts, with cross-document decoys (true elsewhere, false here) as the closest natural
  null. We further hypothesize that this exchangeability can be CONTINUOUSLY SELF-VALIDATED without labels by an entrapment
  check imported from proteomics - spiking known-false-by-construction facts into the candidate pool and verifying that the
  decoy-estimated FDR agrees with the entrapment-measured realized false-admission proportion - and that, where the entrapment
  check passes, the extraction-level FDR propagates through multi-hop deduction in a way captured by an explicit proof-structure
  (fan-out/conjunction) model, so that the decoy-gated pipeline attains higher atomic-fact precision and a lower hallucinated-conclusion
  rate at matched recall than chain-of-thought, RAG, ungated translate-then-prove systems (LINC/Logic-LM), AND label-using
  conformal-factuality baselines (Mohri-Hashimoto, conformal selection + BH, coherent-factuality), while emitting human-auditable
  proof trace-graphs in which every admitted fact and rule carries the decoy-competition and entrapment certificate that licensed
  it.
motivation: >-
  Operational text-to-logic pipelines stall on the same crux: when strict symbolic unification fails, an LLM must perform
  fuzzy matching and supply missing common-sense knowledge - and this is precisely where hallucination re-enters and silently
  corrupts every downstream deduction. The most consequential hallucinations are not random nonsense but PLAUSIBLE false facts
  the model is confident about (a reasonable-sounding inference the document never states). Existing defenses leave a practitioner
  without a quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint
  filtering needs rich trusted constraints and only catches encoded violations; and the strongest recent uncertainty-quantification
  methods - conformal factuality (Mohri-Hashimoto, ICML 2024), conformal selection with BH (Jin-Candes), and coherent factuality
  for reasoning chains - all require a labeled calibration set and certify the final answer or a claim set, not the neural-to-symbolic
  admission boundary. The genomics/proteomics community solved an isomorphic label-poor problem - selecting true signals among
  overwhelming noise with a guaranteed false-discovery rate and no ground truth - via the knockoff filter and target-decoy
  competition. Critically, that community ALSO learned why naive decoys fail (decoys 'too unrealistic to fool' the scorer
  make the FDR optimistic) and engineered two cures we import wholesale: PROPERTY-MATCHED decoys that reproduce the false-positive
  score distribution, and ENTRAPMENT experiments that validate the FDR estimate against a known-false spike-in without labeling
  the real candidates. Transplanting these to the neural-to-symbolic boundary converts 'reduce hallucination' from a best-effort
  aspiration into a controlled, self-validated, reported quantity. The wedge over conformal methods is precise and defensible:
  fully label-free operation, gating at the fuzzy-unification interface rather than the output, and propagation through exact
  symbolic deduction with a per-leaf certificate - directly serving the ACL Knowledge Extraction goal of trustworthy, auditable
  fact extraction and reasoning.
assumptions:
- >-
  Plausibility-matched exchangeability (the revised crux, TESTED not assumed): decoys sampled from the LLM's generative prior
  over document-plausible-but-non-entailed facts - plus cross-document decoys (true elsewhere, false here) - reproduce the
  LLM confidence-score distribution of genuinely-false reals, including the high-scoring plausible hallucinations that matter,
  so admitted decoys are an unbiased estimate of admitted false reals. We do NOT assume this holds; we measure it (decoy-vs-known-false-real
  win-rate near 0.5 on a small labeled probe), validate it label-free (entrapment agreement), and report per decoy family
  where it holds or fails in the anti-conservative direction.
- >-
  Entrapment validity: facts constructed to reference foreign entities injected from an unrelated document or to contradict
  explicit document content are false-BY-CONSTRUCTION for that document, so the rate at which they are admitted is a label-free
  estimate of the realized false-admission proportion - usable to validate the decoy-FDR estimate without annotating any real
  candidate. Entrapment facts must themselves be plausibility-matched, else they test only the easy null.
- >-
  The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates
  document-entailed from non-entailed content better than chance; without such separation no thresholding procedure (decoy-gated,
  conformal, or otherwise) can help.
- >-
  Corpus-aggregate pooling is the meaningful unit of control: a ~3000-char document yields only ~10-40 candidates, where target-decoy
  estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable (min non-trivial FDR is ~1/(k+1)
  with k admissions), so control is asserted over candidates pooled across documents within a dataset family; per-document
  control is reported as a secondary, high-variance quantity with an explicit achievable-alpha floor.
- >-
  Multi-hop deduction error is dominated by erroneous admitted facts/rules rather than the exact symbolic reasoner, and the
  transfer from fact-level FDR to conclusion-level error - including fan-out amplification (one false fact licensing many
  false conclusions) and conjunction depth (a conclusion needing several admitted leaves) - is captured by an explicit proof-structure
  model we fit and test, NOT assumed to be a smooth monotone map.
investigation_approach: >-
  Build the pipeline end to end and make the exchangeability crux the central experimental object. (1) Extraction: a cheap
  OpenRouter LLM reads the ~3000-char document and proposes candidate atomic facts as typed first-order predicates; argument
  types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc). NOTE
  we depend on this slice only for TYPING (to constrain decoy generation and license bridges), not for trusted disjointness/cardinality
  CONSTRAINTS - the FDR claim assumes no constraint ontology. (2) Decoy generation - the key redesign: instead of random same-type
  entity/relation swaps, decoys are drawn from the LLM's OWN generative prior over plausible-but-false content, conditioned
  on the document, so their score distribution matches the realized hallucination null. Families compared head-to-head: (i)
  document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts the document does NOT
  entail), (ii) cross-document decoys (facts true in a sibling document of the same genre, false here), (iii) the OLD random
  type-matched swaps as a deliberately-easy baseline expected to fail. Bridges and gap-filling rules get analogous plausible
  decoys (plausible-but-unsupported predicate alignments and rules attached to unsupported sub-goals). Every decoy passes
  an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on
  a sample); we report the decoy contamination rate (decoys that turn out entailed) and exclude/down-weight contaminated ones,
  quantifying the effect on calibration. (3) Scoring: the LLM scores reals, decoys, and entrapment items jointly in batched
  prompts (cost control) returning one confidence per item. (4) FDR gate: target-decoy competition / the knockoff+ threshold
  picks the most permissive admission cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts, bridges,
  and rules; admitted items enter the KB with a logged certificate, rejected items logged with their losing competition. (5)
  Entrapment self-validation (label-free): a held-out set of plausibility-matched, false-by-construction entrapment facts
  is mixed into the pool; after gating, admitted-entrapment / admitted-total estimates the REALIZED false-admission proportion,
  which we compare against the decoy-estimated FDR - agreement validates ECA, a gap exposes anti-conservatism per family.
  (6) ECA diagnostic (small labeled probe, used for MEASUREMENT only, not by the operational gate): on a labeled slice, two-sample-test
  the scores of KNOWN-false reals vs their matched decoys and report the decoy-over-false-real win-rate (target ~0.5) per
  family - this cross-checks entrapment. (7) Reasoning: admitted facts/rules populate SWI-Prolog for CRISP multi-hop deduction
  (the primary mode, which keeps the headline FDR contribution independent of any calibration). A ProbLog arm is run only
  as an ablation, with fact probabilities set by an EXPLICIT, documented monotone score->probability map (isotonic regression
  fit on the same small labeled probe) whose contribution is ablated against crisp gating so probability miscalibration cannot
  be confused with the gate's effect. Backward-chaining proofs export as trace-graphs whose leaves carry provenance (document
  span / ontology / admitted common-sense) and the decoy+entrapment certificate. (8) Propagation model: a Monte-Carlo simulator
  injects false facts at controlled FDR into the actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error
  from fan-out and conjunction depth; we fit it and test whether it predicts the empirically measured amplification (false
  conclusions per false admitted fact). Datasets: ProofWriter/RuleTaker used PRIMARILY for the reasoner-propagation experiment
  (gold proofs are the asset) and only secondarily, via a PARAPHRASED/back-translated variant, for extraction; CLUTRR (paraphrased
  multi-hop kinship, gold graph) and an ENLARGED hand-annotated set of short legal/news/kids'-story documents carry the headline
  extraction-precision claims, sized by a prospective power analysis. Gold labels are used ONLY for evaluation and the optional
  probe; the operational gate is label-free. Baselines: CoT, standard RAG, LINC/Logic-LM, an ungated translate-then-prove
  ablation (trust LLM fuzzy unification), a plain confidence-threshold / self-consistency gate, AND the label-using conformal
  baselines - Mohri-Hashimoto conformal factuality, conformal selection + BH (Jin-Candes), and a coherent-factuality multi-step
  variant - each given a matched small label budget; plus a HYBRID decoy-gate + conformal ablation. Matched-recall comparison
  is operationalized as full precision-recall CURVES: the gated method sweeps its admission threshold; free-form baselines
  (CoT/RAG) are decomposed into atomic claims and matched to gold by entailment to trace their own PR curve; we report curves
  with bootstrap confidence intervals, not single matched-recall points. Experiments: (a) validity-of-control - sweep alpha,
  measure realized corpus-aggregate FDR via entrapment and (where available) gold, test diagonal tracking and report the achievable-alpha
  floor vs candidate count; (b) decoy-family showdown - win-rate and entrapment agreement per family, testing the prediction
  that plausibility-matched/cross-document decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction
  PR curves vs all baselines on CLUTRR + realistic set; (d) multi-hop accuracy / hallucinated-conclusion rate vs all baselines;
  (e) propagation - does tightening alpha reduce multi-hop hallucination as the fitted proof-structure model predicts, and
  what is the measured amplification; (f) cost/commodity check (LLM spend under $10, CPU-only) plus qualitative auditable
  trace-graphs.
success_criteria: >-
  CONFIRMED if: (1) for at least one engineered decoy family, the realized corpus-aggregate atomic-fact FDR tracks the target
  alpha within a small tolerance on CLUTRR and the realistic set (calibration curve near the diagonal ABOVE the achievable-alpha
  floor), AND the label-free entrapment estimate of realized false-admission agrees with both the decoy estimate and gold
  - demonstrating self-validated, label-free control; (2) the decoy-family showdown confirms the mechanism's signature: plausibility-matched
  and/or cross-document decoys achieve win-rate near 0.5 and entrapment agreement, while random type-matched swaps are measurably
  anti-conservative (realized FDR exceeds target) - i.e., the redesign, not luck, drives validity; (3) at matched recall (full
  PR curves with CIs), decoy-gating yields significantly higher atomic-fact precision and lower hallucinated-conclusion rate
  than CoT, RAG, LINC/Logic-LM, a plain confidence/self-consistency gate, AND the conformal baselines at matched label budget
  - or, if conformal wins on precision, decoy-gating matches it with ZERO labels (the label-free wedge), and the hybrid improves
  on both; (4) tightening alpha reduces multi-hop hallucination in the direction and magnitude predicted by the fitted proof-structure
  model, with measured amplification consistent with the simulator (propagation is a tested quantity); (5) ablating the decoy
  gate (trusting LLM fuzzy unification) measurably worsens hallucination, isolating the gate as the causal mechanism; and
  (6) the pipeline runs on commodity CPU within the $10 budget and produces human-auditable trace-graphs with per-leaf decoy+entrapment
  certificates. DISCONFIRMED if: NO decoy family achieves entrapment-validated diagonal tracking above the alpha-floor (exchangeability
  is unfixable for LLM proposals, with random AND plausibility-matched decoys both anti-conservative); OR decoy-gating shows
  no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by label-using
  conformal baselines even accounting for its zero-label advantage; OR controlling extraction FDR does not translate into
  reduced multi-hop error in any way the proof-structure model can capture (amplification dominates unpredictably or the symbolic
  reasoner is not the bottleneck). NOTE: a clean negative that CHARACTERIZES when/whether ECA can be engineered for LLM proposals
  (e.g., 'cross-document decoys pass entrapment on narrative text but fail on legal text') is itself a reportable contribution.
related_works:
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes
  claims until a user-specified factuality alpha is met, using conformal prediction and very few human-annotated samples.
  NOW USED AS A BASELINE. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT (claim set)
  rather than the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no entrapment self-validation,
  and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification
  interface.
- >-
  Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): builds conformal p-values
  and applies Benjamini-Hochberg to select candidates with FDR control, proven valid under exchangeability of labeled calibration
  and test data. NOW USED AS A BASELINE. Difference: it needs labeled calibration outcomes; our method estimates and controls
  FDR with NO labels by competing each proposal against engineered decoys and self-validates via entrapment. We import the
  FDR-via-multiple-testing framing but replace the labeled calibration set with decoy competition.
- >-
  'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126, 2025): extends conformal factuality to
  dependency graphs of claims so guarantees hold coherently across reasoning chains, again with a labeled calibration set.
  NOW USED AS A BASELINE for the deduction experiment. Difference: labeled, and it guarantees coverage over claim graphs rather
  than gating which extracted facts/rules enter a symbolic KB; it has no decoy competition, no entrapment validation, and
  no label-free knob.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using
  deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition, bioRxiv 2026): generate
  decoys that reproduce the physicochemical/score properties of true positives so target-decoy FDR is well-calibrated. Difference:
  this lives entirely in molecular screening and mass spectrometry. We import the PRINCIPLE - decoys must reproduce the false-positive
  score distribution, not be 'too easy' - to redesign LLM fact/rule decoys as plausibility-matched counterfactuals, an application
  that has never existed for LLM-proposed symbolic assertions.
- >-
  Entrapment experiments for FDR validation in tandem mass spectrometry ('Assessment of false discovery rate control... using
  entrapment', Nature Methods 2025; entrapment-sequence standards): spike a known-false database into the search and measure
  the realized false discovery proportion to validate target-decoy estimates without exhaustive ground truth. Difference:
  a proteomics validation methodology; we transplant it as a label-free internal validity check on LLM fact admission - plausibility-matched,
  document-false-by-construction entrapment facts whose admission rate validates (or refutes) the decoy-FDR estimate per decoy
  family.
- >-
  Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition
  (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against
  a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt
  it to the LLM neural-to-symbolic boundary, confront the Equal-Chance-Assumption failure mode head-on with plausibility-matched
  decoys, and add entrapment self-validation.
- >-
  LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into first-order logic executed by a theorem prover,
  with majority voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated
  translations enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee.
- >-
  Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver, with self-refinement
  on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically
  valid but fabricated premise is never challenged; no statistical control of false extractions, no decoy competition.
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including
  where the ontology is silent - complementary, and we test a hybrid.
- >-
  Abductive missing-premise generation/validation in RAG (arXiv 2511.04020) and LLM-to-ProbLog pipelines (e.g., LLM-AR): an
  LLM generates candidate premises/probabilistic rules validated neurally or executed. Difference: candidate validity is judged
  neurally so hallucinated premises pass, with no statistical false-admission control; we compete every proposal against plausibility-matched
  decoys and self-validate the rate via entrapment.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, sharpened by the reviewer's exchangeability critique. Genomics/proteomics
  solved the hardest label-poor problem - deciding which of thousands of candidate signals are real with no ground truth -
  with a guaranteed false-discovery rate via the knockoff filter (statistics) and target-decoy competition (mass-spectrometry).
  But that field ALSO discovered why naive negative controls fail: decoys that are 'too unrealistic to fool' the scorer make
  the FDR optimistic, so they engineered PROPERTY-MATCHED decoys (e.g., DeepCoy, protein-LM decoys) that reproduce the false-positive
  score distribution, and ENTRAPMENT experiments that validate an FDR estimate against a known-false spike-in WITHOUT labeling
  the real candidates. I map all three onto the exact pressure point of a text-to-logic pipeline - the neural-to-symbolic
  admission boundary where the LLM does fuzzy unification and supplies common-sense - and import the matched-decoy and entrapment
  cures specifically to defeat the anti-conservative failure the reviewer predicted: the dangerous hallucinations are PLAUSIBLE
  high-confidence false facts, so the decoys must themselves be plausible (drawn from the LLM's generative prior, or true-elsewhere
  cross-document facts), and the resulting FDR must be continuously self-validated by entrapment. This turns the prompt's
  vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically disciplined, self-checking, label-free
  gate whose hallucination rate is a tunable, certified, auditable quantity.
terms:
- term: Plausibility-matched decoy
  definition: >-
    A synthetic candidate (fact, bridge, or rule) generated from the LLM's OWN prior over document-plausible-but-non-entailed
    content - either a document-conditioned counterfactual the model finds plausible, or a fact true in a sibling document
    but false here - so its confidence-score distribution reproduces that of genuine plausible hallucinations. This is the
    redesign that replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Entrapment validation
  definition: >-
    A label-free internal validity check imported from proteomics: spike plausibility-matched, false-BY-CONSTRUCTION facts
    (e.g., referencing entities injected from an unrelated document) into the candidate pool; after gating, the fraction of
    admitted items that are entrapment facts estimates the REALIZED false-admission proportion, validating (or exposing a
    gap in) the decoy-estimated FDR without annotating any real candidate.
- term: Equal Chance Assumption (exchangeability)
  definition: >-
    The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched
    decoy are equally likely to receive any given score, so admitted decoys are an unbiased estimate of admitted false reals.
    If decoys are too unrealistic, admitted decoys UNDER-count admitted false reals and realized FDR exceeds target (anti-conservative).
    We test it (win-rate ~0.5) and validate it (entrapment) rather than assume it.
- term: Decoy-over-false-real win-rate
  definition: >-
    An ECA diagnostic computed on a small labeled probe: among matched (known-false real, decoy) pairs, the fraction in which
    the decoy scores at least as high as the false real. A value near 0.5 indicates exchangeability for that decoy family;
    values well below 0.5 reveal the anti-conservative failure the reviewer flagged. Used for measurement only, never by the
    operational gate.
- term: Corpus-aggregate FDR and the achievable-alpha floor
  definition: >-
    Because a single ~3000-char document yields only ~10-40 candidates - too few for stable target-decoy control, with a minimum
    non-trivial FDR of ~1/(k+1) at k admissions - control is asserted over candidates POOLED across documents within a dataset
    family. The achievable-alpha floor (the smallest target alpha reachable given the candidate count and the knockoff+ '+1'
    offset) is reported explicitly; per-document control is a secondary, high-variance quantity.
- term: Target-decoy competition / knockoff+ threshold
  definition: >-
    A label-free selection rule: rank reals and decoys by score and choose the most permissive admission cutoff at which the
    decoy-estimated FDR (admitted decoys + 1, divided by admitted reals) stays below alpha. Items above the cutoff are admitted
    with a certificate; the rest are rejected with their losing competition logged.
- term: Fuzzy unification and bridge rule
  definition: >-
    Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g.,
    'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic
    reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y))
    admitted only if it clears the decoy gate, so the alignment is visible in the trace instead of an opaque per-pair guess.
- term: Amplification (fact-FDR to conclusion-error transfer)
  definition: >-
    The number of false multi-hop conclusions licensed per false admitted fact. Because conclusions are conjunctions of admitted
    leaves and a single false fact can fan out across a proof DAG, conclusion-level error is a NONLINEAR function of fact-level
    FDR; we fit a Monte-Carlo proof-structure model (fan-out, conjunction depth) to predict it and test the prediction empirically.
- term: Non-entailment check and contamination rate
  definition: >-
    Every decoy and entrapment item must be verifiably NOT entailed by the document. Verifying this is itself error-prone,
    so we define an explicit check (symbolic non-derivability against the admitted KB plus an LLM/human entailment audit on
    a sample) and report the contamination rate - decoys that turn out entailed - excluding or down-weighting them and quantifying
    the effect on the calibration curve.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf is annotated with its provenance (document span, ontology axiom, or admitted common-sense rule) plus the
    decoy-competition and entrapment certificate that licensed it.
- term: Crisp vs probabilistic reasoning arm
  definition: >-
    SWI-Prolog crisp admit/reject deduction is the PRIMARY mode, keeping the FDR contribution independent of any calibration.
    A ProbLog arm is an ablation in which fact probabilities come from an EXPLICIT isotonic score->probability map fit on
    a small labeled probe, ablated against crisp gating so probability miscalibration cannot be mistaken for the gate's effect.
summary: >-
  Importing the knockoff filter, property-matched decoys, and entrapment FDR-validation from statistics and proteomics, we
  gate the neural-to-symbolic boundary of a text-to-logic pipeline so that every LLM-proposed fact, fuzzy-unification bridge,
  and common-sense rule must out-compete PLAUSIBILITY-MATCHED synthetic decoys - drawn from the LLM's own prior so they mimic
  real hallucinations - before entering a Prolog/ProbLog knowledge base, controlling the corpus-aggregate hallucination rate
  to a user-specified target with no labels and continuously self-validating that control via entrapment spike-ins. We predict
  this label-free, self-checking gate propagates predictably through symbolic deduction (via a fitted fan-out/conjunction
  model) and beats CoT, RAG, ungated neuro-symbolic, and even label-using conformal-factuality baselines on precision and
  hallucination at matched recall, while emitting auditable proof trace-graphs with per-leaf decoy+entrapment certificates.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_638a4cb91c08
overall_assessment: >-
  This is a strong, highly responsive revision that addresses essentially every major and minor critique from the previous
  round in substance, not just in framing. The single load-bearing weakness flagged last time — that random type-matched decoys
  would be 'too easy' and make the FDR anti-conservative — is now the central experimental object: decoys are redesigned as
  plausibility-matched (document-conditioned counterfactual and cross-document) drawn from the LLM's own prior, exchangeability
  is TESTED via a win-rate~0.5 probe rather than assumed, and a new label-free entrapment self-validation layer (imported
  from the proteomics Nature Methods 2025 line) is added. The conformal-factuality literature (Mohri-Hashimoto, Jin-Candes
  conformal selection, coherent factuality) is now correctly cited and used as baselines, and the novelty wedge is re-sharpened
  to the genuine differentiator: fully label-free OPERATION that gates the neural→symbolic interface and propagates through
  exact symbolic deduction with per-leaf certificates. Corpus-aggregate control with an explicit achievable-alpha floor, PR
  curves with CIs for matched-recall, a decoy contamination-rate audit, a fitted Monte-Carlo proof-structure propagation model,
  and a crisp-primary/ProbLog-ablation split all directly answer prior actions. A targeted novelty search confirms no prior
  application of knockoffs/target-decoy competition to LLM-proposed symbolic assertions, so the core contribution is genuinely
  original. The remaining concerns are now (1) feasibility: the design has ballooned into a ~6-experiment, ~10-baseline, 4-dataset
  program that is not credibly executable under the stated $10 / CPU-only budget without everything being underpowered; (2)
  a precise, evidence-grounded problem with the entrapment validation — the described estimator is the form the proteomics
  literature calls 'inherently flawed,' and entrapment can co-fail with decoys because both are LLM-fabricated, so 'self-validation'
  is necessary-but-not-sufficient; and (3) a subtlety in the win-rate diagnostic (marginal vs. tail exchangeability). None
  are fatal; all are addressable by triage and sharpening. The trajectory is clearly positive and the core idea is publishable-quality
  if the validity story is tightened and scope is triaged before burning compute.
strengths:
- >-
  Genuinely novel cross-domain transfer: a targeted search confirms target-decoy competition / knockoffs have never been applied
  to LLM-proposed symbolic assertions or the neural-to-symbolic admission boundary. The plausibility-matched-decoy + entrapment
  combination at the fuzzy-unification interface is original and well-motivated.
- >-
  Exemplary responsiveness to prior review: the exchangeability crux is now tested (win-rate~0.5 probe), the decoy redesign
  (plausibility-matched / cross-document, with random swaps retained as a deliberately-failing baseline) is a falsifiable
  mechanism claim, and a decoy-family showdown is a first-class experiment rather than an afterthought.
- >-
  Intellectual honesty about the central risk: the hypothesis explicitly does NOT assume exchangeability, reports per-family
  where it holds/fails in the anti-conservative direction, and pre-commits that a clean negative characterization ('cross-document
  decoys pass on narrative but fail on legal text') is itself a reportable contribution — a well-designed hypothesis that
  yields insight regardless of outcome.
- >-
  Correct, current contextualization of the strongest baselines (Mohri-Hashimoto conformal factuality, Jin-Candes conformal
  selection+BH, coherent factuality) with a defensible, sharply stated wedge (label-free operation, interface-level gating,
  symbolic propagation with per-leaf certificates), plus a hybrid decoy+conformal ablation.
- >-
  Rigorous statistical hygiene relative to the prior version: corpus-aggregate control with an explicit achievable-alpha floor
  as a function of candidate count; PR curves with bootstrap CIs and a claim-decomposition protocol for free-form baselines;
  an explicit non-entailment check with reported decoy contamination rate; crisp deduction as primary with the ProbLog/isotonic
  map quarantined as an ablation so calibration cannot be confused with the gate.
- >-
  Treats propagation as a tested, not hoped-for, quantity: a Monte-Carlo proof-structure model (fan-out, conjunction depth)
  is fit and tested against measured amplification on actual ProofWriter/CLUTRR proof DAGs.
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The methodology is now careful, self-aware, and tests its own crux rather than assuming it; validity is operationalized
    through three cross-checks (win-rate probe, entrapment, gold). Residual soundness gaps keep it from excellent: the entrapment
    estimator as described is the form the proteomics literature shows is unreliable; entrapment and decoys share an LLM-fabrication
    failure mode so their agreement is not independent confirmation; and the marginal win-rate~0.5 criterion does not guarantee
    tail exchangeability where admissions actually occur.
  improvements:
  - >-
    Adopt the VALID entrapment estimator. The described 'admitted-entrapment / admitted-total' is the 'sample' estimator that
    Wen et al., Nat. Methods 2025 prove can both over- and under-estimate the FDP. Switch to the combined upper-bound form
    FDP_hat = N_E(1 + 1/r)/(N_T + N_E) (or the tighter paired form), explicitly choose and report the entrapment-to-target
    ratio r, and account for r in the variance. WHY: without this, the headline 'self-validation' is built on a known-flawed
    estimator and could silently endorse an anti-conservative gate. (+1)
  - >-
    Make entrapment and decoy generation MECHANISTICALLY INDEPENDENT so their agreement is evidential. In proteomics, entrapment
    (foreign proteome) is constructed differently from decoys (shuffled), which is what makes the cross-check meaningful;
    here both are LLM-fabricated plausible facts and can co-fail. Use foreign-document-injection / explicit-contradiction
    entrapment against document-conditioned-counterfactual decoys, and flag that foreign-entity entrapment is nearly redundant
    with the cross-document decoy family (their agreement is partly tautological). Treat entrapment as necessary-not-sufficient
    and report cases where entrapment agrees but gold disagrees. (+1)
  - >-
    Condition the win-rate diagnostic on the score region near the operative admission cutoff (report decoy/false-real score
    CDFs and win-rate as a function of score), not just the marginal average. WHY: a family can show aggregate win-rate 0.5
    yet be anti-conservative in the high-score tail where admissions happen. (+0.5)
- dimension: presentation
  score: 3
  justification: >-
    Contextualization relative to prior work is excellent and differentiation is crisp. Clarity, however, is hurt by extreme
    density — the core 'hypothesis' is a single ~250-word sentence and most fields are long run-ons that absorbed every prior
    critique inline. An expert can follow it, but the primary claim is buried under defensive elaboration.
  improvements:
  - >-
    Restructure into a crisp primary claim (label-free corpus-aggregate FDR control at the neural→symbolic boundary via plausibility-matched
    decoys, self-validated by entrapment) plus 3-4 enumerated secondary claims (decoy-family signature, beats/matches conformal
    at zero labels, predictable propagation, auditable certificates). Move defensive caveats into assumptions/method. WHY:
    improves reviewer parse-ability and foregrounds the actual contribution. (+0.5)
  - >-
    Add a one-line dependency diagram of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement ->
    propagation), so the reader sees which results are contingent on which. (+0.25)
- dimension: contribution
  score: 3
  justification: >-
    A confirmed-novel, well-motivated transfer that converts 'reduce hallucination' into a controlled, self-validated, reported
    quantity at exactly the right pressure point (fuzzy unification), with a defensible wedge over the strongest conformal
    baselines. It addresses a meaningful problem and others would build on it. Held below excellent by the contingency on
    exchangeability actually being achievable for LLM proposals (the most likely real-world outcome is partial/per-family)
    and by feasibility risk that could prevent the contribution from being convincingly demonstrated.
  improvements:
  - >-
    Ensure the contribution survives a partial-exchangeability outcome by designing the decoy-family showdown and the legal-vs-narrative
    characterization to be the publishable core even if no family achieves full diagonal tracking. WHY: de-risks the contribution
    against the most probable result. (+0.5)
  - >-
    Give the under-evaluated component (c) implicit common-sense rule gating a real gold evaluation or scope it down (see
    scope critique); right now the most novel/hardest gating target lacks a clean benchmark, weakening the breadth of the
    contribution. (+0.25)
critiques:
- id: ''
  category: scope
  severity: major
  description: >-
    Scope has ballooned far beyond what the stated resources can support. The design now spans 3 decoy families x 3 candidate
    types (facts/bridges/rules), ~10 baselines (several of which are themselves LLM-multi-sample-heavy: LINC majority voting,
    self-consistency, three conformal methods, a hybrid), 4 dataset families (ProofWriter, RuleTaker, CLUTRR, an enlarged
    hand-annotated legal/news/story set), full PR-curve threshold sweeps with bootstrap CIs, entrapment, an ECA labeled probe,
    a fitted Monte-Carlo propagation model, crisp + ProbLog arms, isotonic calibration, and a prospective power analysis —
    all under a <$10 LLM budget on commodity CPU. This is not credible. The likely failure mode is that everything is run
    too thinly, so the strong significance claims in success criterion (3) fail for statistical-power reasons rather than
    scientific ones, wasting the compute. This is the single biggest practical risk to the iteration.
  suggested_action: >-
    Triage and pre-register the compute allocation. Designate the genuinely novel core — the decoy-family showdown + entrapment
    validity + calibration diagonal above the alpha-floor on CLUTRR and the realistic set — as the adequately-powered headline.
    Demote the full baseline bake-off (especially the multi-sample CoT/RAG/LINC and the three conformal variants) and the
    ProbLog/propagation arms to clearly-labeled secondary experiments run at reduced scale. Either raise the budget to a realistic
    figure for the headline experiments or cut the baseline set to the 2-3 most informative (a plain confidence threshold
    and Mohri-Hashimoto conformal factuality are the load-bearing comparisons). State explicitly what was descoped.
- id: ''
  category: rigor
  severity: major
  description: >-
    The entrapment self-validation — now a headline claim ('continuously self-validated without labels') — has two concrete
    problems grounded in the very proteomics literature it imports. (a) Wrong estimator: the hypothesis computes 'admitted-entrapment
    / admitted-total' as the realized false-admission proportion. Wen et al. (Nature Methods 2025, 'Assessment of FDR control
    ... using entrapment') show this 'sample' form is 'inherently flawed' — it can both over- and under-estimate the FDP unpredictably.
    The valid upper-bound form is the combined estimator FDP_hat = N_E(1 + 1/r)/(N_T + N_E), with a tighter 'paired' variant;
    both depend on the entrapment-to-target ratio r, which the hypothesis never mentions. (b) Non-independence / co-failure:
    in proteomics, entrapment (foreign proteome) is constructed and used differently from decoys (shuffled sequences), which
    is what makes their agreement informative. Here BOTH decoys and entrapment are LLM-fabricated plausible-but-false facts,
    so they can share the same anti-conservative failure mode — two biased estimators agreeing does not validate either, and
    the cross-document decoy family vs foreign-entity entrapment are nearly the same construction (their agreement is partly
    tautological). Consequently 'self-validated, label-free control' is overstated: entrapment agreement is necessary, not
    sufficient.
  suggested_action: >-
    Replace the naive ratio with the valid combined (or paired) entrapment estimator, explicitly select and report the entrapment-to-target
    ratio r, and propagate r into the achievable-alpha-floor and variance analysis. Construct entrapment by a mechanism INDEPENDENT
    of the decoy generator (foreign-document injection / explicit contradiction) and pair it against the document-conditioned-counterfactual
    decoy family specifically; note that foreign-entity entrapment vs the cross-document decoy family is a weak (near-redundant)
    cross-check. Frame entrapment agreement as a necessary screening test and reserve the gold-labeled probe as the true arbiter
    of exchangeability; add a 'co-failure detection' result reporting any case where entrapment+decoys agree but gold disagrees.
    Cite Wen et al. 2025 and the FDRBench framework.
- id: ''
  category: rigor
  severity: major
  description: >-
    The exchangeability acceptance criterion (decoy-over-false-real win-rate ~0.5 on the labeled probe) is a MARGINAL statistic,
    but target-decoy / knockoff validity depends on exchangeability in the high-score TAIL near the operative admission cutoff,
    not on average over all matched pairs. A decoy family can exhibit aggregate win-rate ≈ 0.5 while being systematically
    anti-conservative exactly in the region where admissions occur (e.g., decoys match easy false reals but under-score the
    rare very-high-confidence plausible hallucinations that drive realized FDR). Using the marginal win-rate as the gate for
    which families 'pass' could therefore admit a family that fails where it matters.
  suggested_action: >-
    Make the ECA diagnostic tail-aware: report the win-rate and the decoy vs known-false-real score CDFs as a function of
    score, and define the acceptance criterion on the cutoff region (e.g., win-rate within tolerance of 0.5 among pairs scoring
    above the operative threshold, plus a two-sample test of the upper-tail distributions). Connect this explicitly to the
    realized-vs-target diagonal in experiment (a) so the diagnostic and the calibration outcome are predicted to agree.
- id: ''
  category: scope
  severity: minor
  description: >-
    Component (c), gating of IMPLICIT common-sense rules that close proof gaps, is featured prominently (it is arguably the
    most novel and hardest part of the contribution) but lacks a clean gold evaluation. CLUTRR's 'rules' are fixed universal
    kinship-composition axioms (not document-specific, effectively always-admitted, so decoy-gating them is near-trivial);
    ProofWriter/RuleTaker rules are explicitly stated in the text (not implicit common-sense). Neither benchmark provides
    gold for 'which implicit common-sense rule was needed and was it correctly admitted vs. hallucinated.' The headline FDR-control
    results will therefore largely reflect fact and bridge gating, while the rule-gating claim rides along unevaluated.
  suggested_action: >-
    Either (i) construct a small gold set with annotated missing/implicit common-sense rules (e.g., proofs that require an
    unstated bridging rule, with both correct and plausible-but-wrong rule distractors) to evaluate rule-level FDR directly,
    or (ii) scope the primary claim to facts + fuzzy-unification bridges and explicitly label rule-gating as exploratory/qualitative
    until a gold benchmark exists. Report fact-, bridge-, and rule-level calibration separately so the rule claim is not silently
    averaged into the fact result.
- id: ''
  category: methodology
  severity: minor
  description: >-
    Corpus-aggregate control pools candidates across documents and applies a single target-decoy threshold over the pooled
    real/decoy ranking. This assumes LLM confidence scores are comparable across documents. If score scales vary by document
    (easy vs. hard / short vs. dense), the pooled cutoff will be dominated by high-scoring documents and a false real from
    an 'easy' document can out-rank decoys drawn from a 'hard' one, breaking the pooled FDR estimate even when per-document
    exchangeability holds.
  suggested_action: >-
    Standardize or rank-normalize scores per document before pooling (or fit a per-document score transform), verify cross-document
    score-scale homogeneity empirically, and report a sensitivity analysis of the calibration diagonal to the normalization
    choice. Alternatively use a grouped/conditional procedure (e.g., group-wise target-decoy) that respects document structure.
- id: ''
  category: presentation
  severity: minor
  description: >-
    The proposal is extremely dense: the central 'hypothesis' field is a single ~250-word sentence and most fields are long
    run-ons in which the primary claim, the assumptions, the method, and the defensive responses to prior review are interleaved.
    It is comprehensive but hard to parse, and the contribution risks being obscured by elaboration — a real liability for
    an ACL submission's clarity score.
  suggested_action: >-
    Refactor into a crisp one-sentence primary claim plus 3-4 enumerated secondary claims, with a short dependency diagram
    of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement -> predictable propagation). Push caveats
    into the assumptions/method sections. This is polish, but it materially improves how the genuine novelty reads.
score: 6
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same TDC/knockoff gating frame; sharpened decoys to plausibility-matched, added entrapment validation.
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

### [3] HUMAN-USER prompt · 2026-06-16 03:37:40 UTC

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

### [4] ASSISTANT · 2026-06-16 03:38:14 UTC

```
I'll start by reviewing the reviewer feedback carefully and doing targeted research to get the key technical corrections right — especially the entrapment estimator formula from Wen et al. 2025, which the reviewer flagged as a specific fix. Let me load the web tools and check the user uploads in parallel.
```

### [5] TOOL CALL — Skill · 2026-06-16 03:38:14 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 03:38:14 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Bash · 2026-06-16 03:38:14 UTC

```
List user uploads and run directory:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/ 2>/dev/null
```

### [8] TOOL RESULT — Bash · 2026-06-16 03:38:14 UTC

```
{"stdout": "total 1955\ndrwxr-xr-x 2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 9 root root 2000471 Jun 16 03:37 ..\n---\ntotal 10978\ndrwxr-xr-x   9 root root 2000471 Jun 16 03:37 .\ndrwxr-xr-x 159 root root 3011777 Jun 16 03:05 ..\ndrwxr-xr-x   2 root root       1 Jun 16 03:05 .hf_cache\n-rw-r--r--   1 root root   33758 Jun 16 03:05 .workflow_input.json\ndrwxr-xr-x   4 root root 1002340 Jun 16 03:05 config\ndrwxr-xr-x   4 root root 1101594 Jun 16 03:19 iter_1\ndrwxr-xr-x   4 root root 1083977 Jun 16 03:31 iter_2\ndrwxr-xr-x   3 root root 1004494 Jun 16 03:37 iter_3\ndrwxr-xr-x   4 root root 2000280 Jun 16 03:05 sinks\ndrwxr-xr-x   2 root root       1 Jun 16 03:05 user_uploads", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] ASSISTANT · 2026-06-16 03:38:20 UTC

```
I have built-in web tools as deferred. Let me load them and research the key technical correction — the Wen et al. 2025 entrapment estimator.
```

### [10] TOOL CALL — ToolSearch · 2026-06-16 03:38:20 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [11] TOOL RESULT — ToolSearch · 2026-06-16 03:38:20 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [12] TOOL CALL — WebSearch · 2026-06-16 03:38:24 UTC

```
Wen entrapment FDR control proteomics Nature Methods 2025 combined estimator paired
```

### [13] TOOL CALL — WebSearch · 2026-06-16 03:38:24 UTC

```
FDRBench entrapment false discovery rate estimator N_E (1 + 1/r) combined paired peptide
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 03:38:32 UTC

```
{"query": "Wen entrapment FDR control proteomics Nature Methods 2025 combined estimator paired", "results": [{"tool_use_id": "srvtoolu_018jURfiYjoCK96dd4Km4aU8", "content": [{"title": "Accurate de novo sequencing of the modified proteome with OmniNovo", "url": "https://arxiv.org/pdf/2512.12272"}, {"title": "GitHub - Noble-Lab/FDRBench: Estimation of false discovery proportion for mass spectrometry proteomics data using entrapment · GitHub", "url": "https://github.com/Noble-Lab/FDRBench"}, {"title": "(PDF) Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.researchgate.net/publication/392730664_Assessment_of_false_discovery_rate_control_in_tandem_mass_spectrometry_analysis_using_entrapment"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | Nature Methods", "url": "https://www.nature.com/articles/s41592-025-02719-x"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/38895431/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12240826/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.biorxiv.org/content/10.1101/2024.06.01.596967.full.pdf"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11185562/"}, {"title": "How to Train a Postprocessor for Tandem Mass Spectrometry Proteomics Database Search While Maintaining Control of the False Discovery Rate | Journal of Proteome Research", "url": "https://pubs.acs.org/doi/10.1021/acs.jproteome.4c00742"}]}, "The search has returned relevant results about the paper. Here's what I found:\n\nThe paper \"Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment\" was authored by Wen, B., Freestone, J., Riffle, M. et al. and published in Nature Methods 22, 1454–1463 (2025).\n\nA theoretical foundation for entrapment methods is presented, along with a method that enables more accurate evaluation of false discovery rate (FDR) control in proteomics mass spectrometry analysis pipelines.\n\nThe paired entrapment-based False Discovery Proportion (FDP) estimation framework establishes a one-to-one pairing (r=1) between each original target and a unique entrapment sequence. The paired estimation method provides a tighter upper bound on the FDP by evaluating the specific score relationship between each target and its paired mimic.\n\nThe paper identifies three prevalent methods for validating FDR control: one invalid, one providing only a lower bound, and one valid but under-powered. Evaluation of popular data-dependent acquisition tools indicates that these generally seem to control the FDR, but data-independent acquisition tools exhibit inconsistent control of the FDR at both the peptide and protein levels."], "durationSeconds": 7.411774021000005, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 03:38:34 UTC

```
{"query": "FDRBench entrapment false discovery rate estimator N_E (1 + 1/r) combined paired peptide", "results": [{"tool_use_id": "srvtoolu_01LEJWkYgwB5W5ejFMDLHPrZ", "content": [{"title": "GitHub - Noble-Lab/FDRBench: Estimation of false discovery proportion for mass spectrometry proteomics data using entrapment · GitHub", "url": "https://github.com/Noble-Lab/FDRBench"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12240826/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2024.06.01.596967v1.full"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | Nature Methods", "url": "https://www.nature.com/articles/s41592-025-02719-x"}, {"title": "Accurate de novo sequencing of the modified proteome with OmniNovo", "url": "https://arxiv.org/pdf/2512.12272"}, {"title": "(PDF) Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.researchgate.net/publication/392730664_Assessment_of_false_discovery_rate_control_in_tandem_mass_spectrometry_analysis_using_entrapment"}, {"title": "False discovery rate estimation using candidate peptides for each spectrum", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9623924/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/38895431/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.biorxiv.org/content/10.1101/2024.06.01.596967.full.pdf"}]}, "Based on the search results, I found information about FDRBench and its entrapment-based false discovery rate estimation methods.\n\nFDRBench is a Java tool that provides two main functions: (1) build entrapment databases using randomly shuffled target sequences or using sequences from foreign species, and (2) estimate FDP using the lower bound, combined, and paired methods.\n\nRegarding the specific formula you asked about with N_E and the (1 + 1/r) term, the \"combined\" method estimates the FDP among the target+entrapment discoveries while taking into account r, which is the effective ratio of the entrapment to original target database size.\n\nThe paired method works differently: By taking advantage of sample-entrapment pairing information, this method allows us to reduce the conservative bias of the combined method while still retaining its upper bound nature. As such, the paired estimation method is more likely to provide evidence of proper FDR control than the combined method is. For this method to work, say, in peptide-level analysis, each original target peptide must be paired with a unique entrapment peptide (so r = 1). In practice, this means that the paired estimation method requires a shuffling or reversal to generate the entrapment peptides."], "durationSeconds": 9.141817187000001, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 03:38:44 UTC

```
Let me extract the exact estimator formulas from the paper's full text.
```

### [17] TOOL CALL — Bash · 2026-06-16 03:38:44 UTC

```
Grep entrapment estimator formulas from bioRxiv PDF:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://www.biorxiv.org/content/10.1101/2024.06.01.596967.full.pdf" --pattern "combined|paired estimat|1 \+ 1|entrapment-to-target|lower bound" --max-matches 25 --context-chars 260 -i
```

### [18] TOOL RESULT — Bash [ERROR] · 2026-06-16 03:38:44 UTC

```
Error: Exit code 1
Error: HTTP 403
```

### [19] TOOL CALL — Bash · 2026-06-16 03:38:48 UTC

```
Grep entrapment estimator formulas from PMC article:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://pmc.ncbi.nlm.nih.gov/articles/PMC12240826/" --pattern "combined method|paired method|1 \+ 1|entrapment-to-target|lower bound|sample method|inherently flawed|N_\{?E" --max-matches 30 --context-chars 240 -i
```

### [20] TOOL RESULT — Bash · 2026-06-16 03:38:48 UTC

```
{"stdout": "URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12240826/\nType: HTML\nPattern: combined method|paired method|1 \\+ 1|entrapment-to-target|lower bound|sample method|inherently flawed|N_\\{?E (0 matches in 133 chars)\n\n--- Content ---\n\nNo matches found for pattern: combined method|paired method|1 \\+ 1|entrapment-to-target|lower bound|sample method|inherently flawed|N_\\{?E", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [21] TOOL CALL — WebFetch · 2026-06-16 03:39:00 UTC

```
URL: https://github.com/Noble-Lab/FDRBench
Prompt: Extract the exact formulas and definitions for the entrapment FDP estimators: the "lower bound", "combined", and "paired" methods. In particular, what is the combined estimator formula in terms of the number of entrapment matches and the entrapment-to-target ratio r? What does r mean and how is it set? How does the paired method differ and why is it a tighter upper bound? Why is the naive "sample" estimator considered flawed?
```

### [22] TOOL RESULT — WebFetch · 2026-06-16 03:39:00 UTC

```
{"bytes": 512405, "code": 200, "codeText": "OK", "result": "# FDRBench FDP Estimator Methods\n\nBased on the provided documentation, I can only partially address your request, as the page does not contain the explicit mathematical formulas for these estimators.\n\n## What the Documentation Shows\n\nThe page describes three FDP estimation methods but does not present their mathematical definitions:\n\n1. **Lower bound method** - mentioned as available but formula not provided\n2. **Combined method** - described as producing output columns like `combined_fdp` but formula not specified\n3. **Paired method** - noted as requiring \"the peptide pair `*.txt` file generated in Workflow 1\" but mathematical details absent\n\n## What's Missing\n\nThe documentation does not explain:\n- The exact formula for the combined estimator or how it uses the entrapment-to-target ratio *r*\n- The definition of *r* or how users set it (though `-fold` parameter appears relevant)\n- Why the paired method provides tighter bounds\n- Why a naive \"sample\" estimator is flawed\n\n## Available Information\n\nThe page indicates *r* relates to entrapment-to-target proportions (described as \"R Ratio\" for Foreign Species mode), and the `-fold` parameter controls \"number of entrapment copies per target.\" However, the specific mathematical relationships remain undefined in this source.\n\nFor complete formulas and theoretical justification, you would need to consult the referenced Nature Methods publication: Wen et al. (2025).", "durationMs": 7023, "url": "https://github.com/Noble-Lab/FDRBench"}
```

### [23] TOOL CALL — WebFetch · 2026-06-16 03:39:18 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/
Prompt: Give the exact mathematical formula for the "combined" entrapment FDP estimator and the "paired" estimator. What is r (entrapment-to-target database ratio)? Why is the naive 'sample' estimator (entrapment discoveries divided by total discoveries) considered invalid/flawed? Quote the formulas verbatim if present.
```

### [24] TOOL RESULT — WebFetch · 2026-06-16 03:39:18 UTC

```
{"bytes": 276539, "code": 200, "codeText": "OK", "result": "# Entrapment FDP Estimators\n\n## Combined Estimator Formula\n\nThe combined method estimates FDP among target+entrapment discoveries:\n\n**FDP^(T∪E) = N_E(1+1/r) / (N_T + N_E)**\n\nWhere N_T = original target discoveries, N_E = entrapment discoveries, and r = entrapment-to-target database ratio.\n\n## Paired Estimator Formula\n\nThe paired method provides a tighter upper bound:\n\n**FDP^(T∪E)* = [N_E + N_E≥s>T + 2·N_E>T≥s] / (N_T + N_E)**\n\nWhere s = discovery cutoff score; additional terms account for paired peptide scoring relationships.\n\n## What is r?\n\nThe parameter r represents \"the effective ratio of the entrapment to original target database size.\" For example, r=1 means equal-sized databases, while r=5 means five times more entrapment sequences than original targets.\n\n## Why the Sample Estimator Fails\n\nThe sample method (N_E·(1/r) / N_T) is \"inherently flawed because, while typically underestimating the FDP, it can also overestimate it in some unusual cases.\" This inconsistency means it cannot reliably establish either FDR control success or failure.", "durationMs": 5985, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}
```

### [25] ASSISTANT · 2026-06-16 03:42:39 UTC

```
I now have the exact formulas confirmed:
- **Combined estimator** (valid upper bound): FDP̂ = N_E(1+1/r)/(N_T+N_E)
- **Paired estimator** (tighter, requires r=1 pairing): FDP̂* = [N_E + N_{E≥s>T} + 2·N_{E>T≥s}]/(N_T+N_E)
- **Sample estimator** (flawed): N_E·(1/r)/N_T — the one the reviewer flagged
- r = entrapment-to-target database ratio

I have everything needed to revise. The novelty was confirmed by the reviewer, so I'll focus entirely on addressing the six critiques: (1) triage scope, (2) fix the entrapment estimator + make it mechanistically independent, (3) tail-aware win-rate, (4) rule-gating gold, (5) per-document score normalization, (6) crisp restructure with a dependency diagram. Let me write the revised hypothesis.
```

### [26] TOOL CALL — Write · 2026-06-16 03:42:39 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_3/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Tail-Exchangeable Decoy Competition with Independent Entrapment Validation: Label-Free False-Discovery-Rate Control of Fact and Bridge Admission at the Fuzzy-Unification Boundary of Text-to-Logic Pipelines",
  "hypothesis": "PRIMARY CLAIM. At the neural-to-symbolic admission boundary of a text-to-logic pipeline - where an LLM proposes (a) atomic facts extracted from a ~3000-char document and (b) fuzzy-unification BRIDGE rules that align a document predicate to an ontology/rule predicate when strict unification fails - competing every proposal against PLAUSIBILITY-MATCHED synthetic decoys drawn from the LLM's own prior over document-plausible-but-non-entailed content, then selecting the admission cutoff by target-decoy / knockoff+ competition, controls the corpus-aggregate false-admission rate (FDR) of the resulting SWI-Prolog knowledge base to a user-specified target alpha WITH NO ground-truth labels - PROVIDED the decoys are exchangeable with realized hallucinations IN THE HIGH-SCORE TAIL where admissions actually occur (not merely on marginal average).\n\nSECONDARY CLAIMS (each independently testable; the contribution survives even if the primary control claim only holds per-family).\n  S1 - DECOY-FAMILY SIGNATURE (the mechanism, falsifiable): random type-matched entity/relation swaps are 'too easy' and therefore anti-conservative (realized FDR exceeds target), whereas document-conditioned counterfactual decoys approach tail-exchangeability. This is diagnosed by a TAIL-CONDITIONED win-rate - the decoy-over-known-false-real win-rate computed among pairs scoring ABOVE the operative cutoff, target ~0.5 - plus a two-sample test of the upper-tail score CDFs, NOT a marginal average that can read 0.5 while failing in the tail.\n  S2 - INDEPENDENT LABEL-FREE CORROBORATION (necessary, not sufficient): entrapment items built by a mechanism MECHANISTICALLY INDEPENDENT of the decoy generator - foreign-document injection (facts about entities lifted from an unrelated document) and explicit document-contradiction - when scored through the same gate, yield a VALID combined-estimator upper bound on realized false-admission, FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (Wen et al., Nat. Methods 2025; tighter paired form when r=1), that AGREES with the decoy-FDR and with gold on tail-exchangeable families. We claim this agreement is a NECESSARY screening test, never sufficient: because both decoys and entrapment are LLM-fabricated they can co-fail, so the small gold probe is the arbiter and any co-failure (entrapment+decoy agree, gold disagrees) is itself a reported result. We DROP the naive 'sample' ratio (admitted-entrapment / admitted-total) the proteomics literature shows is inherently flawed.\n  S3 - WEDGE OVER CONFORMAL (the headline comparison): at matched recall (full PR curves with bootstrap CIs), decoy-gating with ZERO labels achieves atomic-fact precision and hallucinated-conclusion rate that match or beat (i) a plain confidence threshold and (ii) the label-using Mohri-Hashimoto conformal-factuality baseline at a small matched label budget - the differentiator being fully label-free OPERATION that gates the fuzzy-unification interface rather than the output.\n  S4 - PREDICTABLE PROPAGATION (secondary, reduced-scale): tightening alpha reduces the multi-hop hallucinated-conclusion rate in the direction and rough magnitude predicted by a fitted fan-out/conjunction proof-structure model.\n\nCLAIM-CHAIN DEPENDENCY DIAGRAM (which result is contingent on which): [tail-exchangeable decoy family] -> [valid label-free corpus-aggregate FDR estimate via TDC/knockoff+] -> [realized FDR tracks target alpha above the achievable-alpha floor, GOLD-ARBITRATED] -> [independent entrapment combined-estimator agreement = necessary corroboration] -> [controlled fact+bridge FDR propagates to reduced multi-hop hallucination]. A break at any arrow is localized and reported; downstream claims are not asserted if an upstream arrow fails.\n\nSCOPE (pre-registered to fit $10 / CPU-only). PRIMARY claims (S1-S3 control + signature + wedge) are evaluated on FACTS and fuzzy-unification BRIDGES only, on CLUTRR (paraphrased multi-hop kinship, gold graph) plus a hand-annotated realistic short-document set. Implicit common-sense RULE gating is a SEPARATELY-REPORTED EXPLORATORY arm on a small purpose-built gold rule set (annotated missing rules with plausible-but-wrong distractors); fact-, bridge-, and rule-level calibration are NEVER averaged together. The full baseline bake-off (CoT, RAG, LINC, Logic-LM, conformal selection, coherent factuality, hybrid), the ProbLog/isotonic arm, and the propagation model (S4) are reduced-scale SECONDARY experiments.",
  "motivation": "Operational text-to-logic pipelines stall at the same crux: when strict symbolic unification fails, an LLM must perform fuzzy matching and supply background knowledge - and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts (a reasonable-sounding inference the document never states). Practitioners have no quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and only catches encoded violations; and the strongest uncertainty-quantification methods - conformal factuality (Mohri-Hashimoto, ICML 2024), conformal selection + BH (Jin-Candes), coherent factuality - all require a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary. Genomics/proteomics solved an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth - via the knockoff filter and target-decoy competition, AND learned the two failure modes we must respect: (1) decoys 'too unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED decoys, and (2) entrapment FDP must be estimated with a VALID upper-bound estimator (the combined/paired form of Wen et al., Nat. Methods 2025), not the naive sample ratio, and entrapment must be constructed INDEPENDENTLY of the decoys or their agreement is uninformative. Importing all three - matched decoys, the valid combined entrapment estimator, and construction independence - to the fuzzy-unification boundary converts 'reduce hallucination' from a best-effort aspiration into a controlled, label-free, self-corroborated quantity. The wedge over conformal methods is precise: fully label-free operation, gating at the interface rather than the output, and propagation through exact symbolic deduction with per-leaf certificates - directly serving the ACL Knowledge Extraction goal of trustworthy, auditable fact extraction. Crucially the design is built to YIELD INSIGHT EVEN IF EXCHANGEABILITY ONLY HOLDS PARTIALLY: a per-family, per-genre characterization ('counterfactual decoys pass on narrative but fail on legal text') is the publishable core regardless of whether any family achieves full diagonal tracking.",
  "assumptions": [
    "TAIL exchangeability is the crux, and it is TESTED, not assumed. The validity of target-decoy / knockoff control requires that a genuinely-false real proposal and its matched decoy are equally likely to receive any given score IN THE HIGH-SCORE REGION near the operative admission cutoff - not merely on marginal average. We measure a tail-conditioned win-rate (~0.5 among pairs above the cutoff) and a two-sample test of upper-tail CDFs, validate label-free via independent entrapment, arbitrate with a small gold probe, and report per decoy family and per genre where it holds or fails anti-conservatively. A family with marginal win-rate ~0.5 but anti-conservative tail behavior is reported as FAILING.",
    "ENTRAPMENT validity requires the VALID estimator AND construction independence. (a) Realized false-admission is estimated by the combined upper-bound FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (or the tighter paired form at r=1), with the entrapment-to-target ratio r chosen and reported explicitly and propagated into the variance and the achievable-alpha floor; the naive 'sample' ratio is not used. (b) Entrapment is generated by a mechanism INDEPENDENT of the decoy generator - foreign-document injection and explicit document-contradiction, NOT the LLM-counterfactual prior that produces the primary decoys - so their agreement is evidential rather than tautological; we explicitly flag that foreign-entity entrapment vs a cross-document decoy family would be near-redundant and therefore pair foreign-document entrapment against the document-CONDITIONED-COUNTERFACTUAL decoy family. Entrapment agreement is necessary, never sufficient; gold is the arbiter.",
    "The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates document-entailed from non-entailed content better than chance; without such separation in the tail, no thresholding procedure (decoy-gated, conformal, or otherwise) can help.",
    "Corpus-aggregate pooling WITH per-document score normalization is the unit of control. A ~3000-char document yields only ~10-40 candidates, where target-decoy estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable (min non-trivial FDR ~1/(k+1) at k admissions); control is therefore asserted over candidates POOLED across documents within a dataset family. Because raw LLM scores need not be comparable across documents, scores are RANK-NORMALIZED per document (or a per-document transform is fit) before pooling, OR a group-wise target-decoy procedure is used; we verify cross-document score-scale homogeneity and report a sensitivity analysis of the calibration diagonal to the normalization choice. The achievable-alpha floor is reported as a function of candidate count AND r.",
    "Multi-hop deduction error (the SECONDARY S4 claim) is dominated by erroneous admitted facts/bridges rather than the exact symbolic reasoner, and the transfer from fact/bridge-FDR to conclusion-level error - including fan-out (one false fact licensing many false conclusions) and conjunction depth - is captured by an explicit fitted proof-structure model, not assumed to be a smooth monotone map. This claim is not load-bearing for the primary contribution."
  ],
  "investigation_approach": "Build the pipeline end to end and make TAIL exchangeability and INDEPENDENT entrapment validity the central experimental objects, under a pre-registered compute split. PRE-REGISTERED BUDGET ALLOCATION (of the $10 / CPU-only): ~60% to the HEADLINE - decoy-family showdown + entrapment validity + calibration diagonal on facts+bridges over CLUTRR and the realistic set, adequately powered via a prospective power analysis; ~25% to the load-bearing baseline comparison (plain confidence threshold + Mohri-Hashimoto conformal factuality only); ~15% to clearly-labeled SECONDARY arms (exploratory rule gating, ProbLog/isotonic ablation, S4 propagation, and a single ungated translate-then-prove ablation). DESCOPED EXPLICITLY: full CoT/RAG/LINC/Logic-LM/coherent-factuality/conformal-selection bake-off and the decoy+conformal hybrid are dropped from the primary program (mentioned as future work); ProofWriter/RuleTaker are used ONLY for the secondary S4 propagation experiment (gold proof DAGs are the asset), not for headline extraction.\n  (1) EXTRACTION: a cheap OpenRouter LLM reads the document and proposes typed first-order facts; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing (to constrain decoy generation and license bridges), NOT for trusted disjointness/cardinality constraints - the FDR claim assumes no constraint ontology.\n  (2) DECOY GENERATION (the matched-null redesign): the PRIMARY family is document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts/bridges the document does NOT entail, conditioned on the document and types), so their score distribution matches the realized hallucination null. The deliberately-easy random type-matched swap family is retained as the baseline PREDICTED to be anti-conservative. (Cross-document decoys are noted but de-emphasized because they are near-redundant with foreign-entity entrapment.) Every decoy passes an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB + an LLM/human entailment audit on a sample); we report the decoy contamination rate and exclude/down-weight contaminated items.\n  (3) ENTRAPMENT (independent construction): a held-out set of foreign-document-injection and explicit-contradiction entrapment facts - false BY CONSTRUCTION and generated by a mechanism distinct from the counterfactual decoys - is mixed into the pool at a chosen, reported ratio r.\n  (4) SCORING: the LLM scores reals, decoys, and entrapment jointly in batched prompts (cost control), returning one confidence per item; scores are rank-normalized per document.\n  (5) FDR GATE: target-decoy competition / the knockoff+ threshold picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, SEPARATELY for facts and bridges; admitted items enter the KB with a logged certificate.\n  (6) ENTRAPMENT VALIDATION (label-free, necessary): after gating, the COMBINED estimator FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (paired form reported at r=1) upper-bounds realized false-admission; we compare it against the decoy-FDR and, where available, gold. Agreement corroborates; a CO-FAILURE result (entrapment+decoy agree but gold disagrees) is explicitly hunted for and reported as the key validity caveat.\n  (7) TAIL-AWARE ECA DIAGNOSTIC (small labeled probe, MEASUREMENT only, never used by the operational gate): on a labeled slice, report the decoy-over-known-false-real win-rate AND the decoy vs false-real score CDFs AS A FUNCTION OF SCORE, with the acceptance criterion defined on the cutoff region (win-rate within tolerance of 0.5 among pairs above the operative threshold + two-sample test of upper tails). This diagnostic is predicted to agree with the realized-vs-target diagonal in experiment (a).\n  (8) REASONING: admitted facts/bridges populate SWI-Prolog for crisp multi-hop deduction (PRIMARY mode, keeping the headline FDR contribution independent of any calibration); backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted bridge) plus the decoy-competition + entrapment certificate. A ProbLog arm with an EXPLICIT isotonic score->probability map (fit on the small probe) is a SECONDARY ablation, ablated against crisp gating.\n  (9) EXPLORATORY RULE GATING (separately reported): a small gold set of proofs requiring an unstated implicit common-sense bridging rule, each paired with correct and plausible-but-wrong distractor rules, evaluates rule-level FDR directly; results are reported apart from facts/bridges.\n  (10) PROPAGATION (SECONDARY, S4): a Monte-Carlo simulator injects false facts at controlled FDR into actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error from fan-out and conjunction depth; we test whether it predicts measured amplification.\n  DATASETS: CLUTRR (paraphrased) + an enlarged hand-annotated set of short legal/news/kids'-story documents carry the headline facts+bridges claims (sized by power analysis, with the legal-vs-narrative split designed to expose per-genre exchangeability differences); ProofWriter/RuleTaker only for S4. Gold labels are used ONLY for evaluation and the optional probe; the operational gate is label-free.\n  BASELINES (load-bearing only): plain confidence/self-consistency threshold and Mohri-Hashimoto conformal factuality at a small matched label budget, plus the ungated translate-then-prove ablation. Matched-recall is operationalized as full PR CURVES with bootstrap CIs (gated method sweeps its threshold; free-form baselines decomposed into atomic claims and matched to gold by entailment).\n  EXPERIMENTS: (a) validity-of-control - sweep alpha, measure realized corpus-aggregate FDR via entrapment-combined-estimator and gold, test diagonal tracking above the achievable-alpha floor, report sensitivity to per-document normalization; (b) decoy-family showdown - TAIL win-rate + entrapment agreement per family/genre, testing that counterfactual decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction PR curves vs the load-bearing baselines on facts+bridges; (d) [secondary] multi-hop accuracy and S4 propagation; (e) [secondary/exploratory] rule-gating gold; (f) cost check (LLM spend < $10, CPU-only) + qualitative auditable trace-graphs.",
  "success_criteria": "PRIMARY (headline, adequately powered on facts+bridges over CLUTRR + realistic set). CONFIRMED if: (1) for at least one decoy family, realized corpus-aggregate FDR tracks target alpha within a small tolerance ABOVE the achievable-alpha floor (calibration diagonal), stable under the per-document normalization sensitivity check, AND the INDEPENDENT entrapment combined-estimator upper bound agrees with both the decoy estimate and gold - demonstrating self-corroborated, label-free control; (2) the decoy-family showdown shows the mechanism's signature in the TAIL: counterfactual decoys achieve tail-conditioned win-rate ~0.5 (and pass the upper-tail two-sample test) with entrapment+gold agreement, while random type-matched swaps are measurably anti-conservative - establishing that the redesign, not luck, drives validity; (3) at matched recall (PR curves with CIs), decoy-gating yields atomic-fact precision and hallucinated-conclusion rate that match or beat a plain confidence threshold AND the label-using Mohri-Hashimoto conformal baseline at a small matched label budget - with the zero-label operation as the wedge.\n  CONTRIBUTION-SURVIVES-PARTIAL clause (de-risking the most likely outcome): even if NO family achieves full diagonal tracking, a clean per-family, per-genre CHARACTERIZATION of when tail-exchangeability and independent-entrapment agreement can or cannot be engineered for LLM proposals (e.g., 'counterfactual decoys pass on narrative but fail on legal text'), together with the documented co-failure cases, is itself the reportable headline contribution.\n  SECONDARY. (4) tightening alpha reduces multi-hop hallucination in the direction predicted by the fitted proof-structure model (S4); (5) ablating the decoy gate (trusting LLM fuzzy unification) measurably worsens hallucination; (6) exploratory rule-gating shows decoy competition separates correct from plausible-but-wrong implicit rules above chance on the small gold set; (7) the pipeline runs on commodity CPU within $10 and produces auditable trace-graphs with per-leaf decoy+entrapment certificates.\n  DISCONFIRMED if: NO decoy family achieves tail-exchangeable, gold-arbitrated diagonal tracking above the alpha-floor on EITHER genre (with random AND counterfactual decoys both anti-conservative in the tail), AND the entrapment combined-estimator systematically co-fails with the decoys against gold; OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by Mohri-Hashimoto conformal even accounting for its zero-label advantage. A negative that characterizes the failure boundary remains a contribution; an UNINTERPRETABLE null (control neither clearly holds nor clearly fails anywhere) is the true failure.",
  "related_works": [
    "Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench tool, Noble-Lab/FDRBench): provides the theory of entrapment FDP estimation, shows the naive 'sample' estimator (N_E/r / N_T) is inherently flawed (can over- AND under-estimate), and gives the VALID combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E) and a tighter PAIRED form at r=1. WE ADOPT this estimator wholesale to fix the previously-naive ratio, choose and report r, and propagate r into variance and the alpha-floor. Difference: their domain is mass spectrometry peptide identification; we transplant the estimator AND the construction-independence principle (entrapment must be built unlike the decoys) to validate LLM fact/bridge admission.",
    "Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes claims until a user-specified factuality alpha is met via conformal prediction with a few labeled samples. NOW THE PRIMARY load-bearing baseline. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT rather than the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no independent entrapment validation, and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification interface.",
    "Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to select candidates with FDR control under exchangeability of labeled calibration and test data. Demoted to secondary/future comparison. Difference: needs labeled calibration outcomes; we estimate and control FDR with NO labels by competing each proposal against engineered decoys and corroborate via independent entrapment.",
    "Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt knockoff+ thresholding to the LLM neural-to-symbolic boundary and confront the Equal-Chance-Assumption failure mode in the high-score TAIL (not just marginally) with plausibility-matched decoys.",
    "Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition): generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference: lives entirely in molecular screening / mass spectrometry; we import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too easy' - to design LLM fact/bridge decoys as document-conditioned counterfactuals, never done for LLM-proposed symbolic assertions.",
    "LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into FOL executed by a theorem prover with majority voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated translations enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee. (Descoped from our primary baseline set for feasibility; noted as comparison context.)",
    "Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver with self-refinement on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically valid but fabricated premise is never challenged; no statistical control of false extractions.",
    "Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including where the ontology is silent - complementary.",
    "Conformal factuality for reasoning chains, 'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126, 2025): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning chains, with a labeled calibration set. Difference: labeled, certifies coverage over claim graphs rather than gating which extracted facts/bridges enter a symbolic KB; no decoys, no independent entrapment, no label-free knob. (Descoped to future comparison.)"
  ],
  "inspiration": "A Level-3 (methodological) cross-domain transfer, now sharpened twice by review. Genomics/proteomics solved the hardest label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry). That field ALSO discovered the two ways the trick breaks: (1) decoys 'too unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED decoys (DeepCoy, protein-LM decoys); and (2) entrapment FDP must be estimated with a VALID upper bound - the combined/paired estimator of Wen et al. (Nature Methods 2025), NOT the naive sample ratio - and the entrapment set must be CONSTRUCTED DIFFERENTLY from the decoys, or their agreement proves nothing. I map all three onto the exact pressure point of a text-to-logic pipeline - the fuzzy-unification boundary where the LLM aligns predicates and supplies background knowledge - and import the matched-decoy cure, the valid combined entrapment estimator (with an explicit entrapment-to-target ratio r), and the construction-independence requirement specifically to defeat the anti-conservative failure: the dangerous hallucinations are PLAUSIBLE high-confidence false facts, so the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE TAIL (not on average), and the FDR must be corroborated by entrapment built unlike the decoys and arbitrated by a small gold probe. This turns the prompt's vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically disciplined, self-corroborated, label-free gate whose hallucination rate is a tunable, certified, auditable quantity.",
  "terms": [
    {
      "term": "Plausibility-matched (counterfactual) decoy",
      "definition": "A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's OWN prior over document-plausible-but-non-entailed content - a document-conditioned counterfactual the model finds plausible - so its confidence-score distribution reproduces that of genuine plausible hallucinations. This is the redesign that replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic (anti-conservative)."
    },
    {
      "term": "Tail-conditioned win-rate (tail-aware ECA diagnostic)",
      "definition": "The decoy-over-known-false-real win-rate computed ONLY among matched pairs whose scores fall ABOVE the operative admission cutoff, reported together with the decoy and false-real score CDFs as a function of score and an upper-tail two-sample test. Target ~0.5 in the tail. It supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative exactly where admissions occur. Used for measurement only, never by the operational gate."
    },
    {
      "term": "Combined / paired entrapment estimator and the ratio r",
      "definition": "The VALID entrapment upper bound on realized false-admission: FDP_hat = N_E(1 + 1/r)/(N_T + N_E), where N_T = admitted real items, N_E = admitted entrapment items, and r = entrapment-to-target ratio (chosen and reported; e.g., r=1 for the tighter PAIRED form). It replaces the inherently-flawed naive 'sample' ratio (admitted-entrapment / admitted-total). r is propagated into the variance and the achievable-alpha floor."
    },
    {
      "term": "Independent entrapment and co-failure detection",
      "definition": "Entrapment items are built by a mechanism DISTINCT from the decoy generator - foreign-document injection (foreign entities) and explicit document-contradiction - so their agreement with the LLM-counterfactual decoy FDR is evidential, not tautological. Because both are nonetheless LLM-handled, agreement is treated as NECESSARY not sufficient; the small gold probe is the arbiter, and any CO-FAILURE (entrapment+decoy agree but gold disagrees) is explicitly reported as the validity caveat."
    },
    {
      "term": "Equal Chance Assumption (tail exchangeability)",
      "definition": "The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched decoy are equally likely to receive any given score, IN THE HIGH-SCORE TAIL where admissions occur. If decoys under-score the rare very-high-confidence plausible hallucinations, admitted decoys under-count admitted false reals and realized FDR exceeds target. We test it in the tail and validate it via independent entrapment rather than assume it."
    },
    {
      "term": "Per-document score normalization and group-wise control",
      "definition": "Because raw LLM confidence scores need not be comparable across documents, scores are rank-normalized per document (or a per-document transform is fit) before pooling for corpus-aggregate target-decoy control - or a group-wise procedure respecting document structure is used - so a false real from an 'easy' document cannot spuriously out-rank decoys from a 'hard' one. Cross-document homogeneity is verified and a sensitivity analysis of the calibration diagonal to the normalization choice is reported."
    },
    {
      "term": "Corpus-aggregate FDR and the achievable-alpha floor",
      "definition": "Control is asserted over candidates POOLED across documents within a dataset family (a single ~3000-char document yields too few candidates for stable control, with min non-trivial FDR ~1/(k+1) at k admissions and the knockoff+ '+1' offset). The achievable-alpha floor - the smallest target alpha reachable given candidate count AND the entrapment ratio r - is reported explicitly; per-document control is a secondary, high-variance quantity."
    },
    {
      "term": "Target-decoy competition / knockoff+ threshold",
      "definition": "A label-free selection rule: rank reals and decoys by (per-document-normalized) score and choose the most permissive cutoff at which the decoy-estimated FDR ((admitted decoys + 1) / admitted reals) stays below alpha, applied separately to facts and bridges. Admitted items enter the KB with a certificate; the rest are rejected with their losing competition logged."
    },
    {
      "term": "Fuzzy unification and bridge rule",
      "definition": "Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g., 'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y)) admitted only if it clears the decoy gate. Facts and bridges - NOT implicit common-sense rules - carry the headline FDR-control claim."
    },
    {
      "term": "Trace-graph",
      "definition": "A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications, and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and entrapment certificate that licensed it."
    }
  ],
  "summary": "We gate the fuzzy-unification boundary of a text-to-logic pipeline so every LLM-proposed fact and bridge rule must out-compete plausibility-matched counterfactual decoys (target-decoy / knockoff+ thresholding) before entering a Prolog knowledge base, controlling the corpus-aggregate hallucination rate to a user-specified target with NO labels; validity is tested in the high-score TAIL (not on average) and corroborated by an independently-constructed entrapment set scored through the VALID combined estimator FDP=N_E(1+1/r)/(N_T+N_E), with a small gold probe as arbiter. We predict this label-free gate matches or beats a plain confidence threshold and the label-using Mohri-Hashimoto conformal baseline on fact precision and hallucination at matched recall, and that a per-family/per-genre characterization of where tail-exchangeability holds is the publishable core even if full diagonal control is only partial."
}
```

### [27] TOOL RESULT — Write · 2026-06-16 03:42:39 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_3/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Tail-Exchangeable Decoy Competition with Independent Entrapment Validation: Label-Free False-Discovery-Rate Control of Fact and Bridge Admission at the Fuzzy-Unification Boundary of Text-to-Logic Pipelines\",\n  \"hypothesis\": \"PRIMARY CLAIM. At the neural-to-symbolic admission boundary of a text-to-logic pipeline - where an LLM proposes (a) atomic facts extracted from a ~3000-char document and (b) fuzzy-unification BRIDGE rules that align a document predicate to an ontology/rule predicate when strict unification fails - competing every proposal against PLAUSIBILITY-MATCHED synthetic decoys drawn from the LLM's own prior over document-plausible-but-non-entailed content, then selecting the admission cutoff by target-decoy / knockoff+ competition, controls the corpus-aggregate false-admission rate (FDR) of the resulting SWI-Prolog knowledge base to a user-specified target alpha WITH NO ground-truth labels - PROVIDED the decoys are exchangeable with realized hallucinations IN THE HIGH-SCORE TAIL where admissions actually occur (not merely on marginal average).\\n\\nSECONDARY CLAIMS (each independently testable; the contribution survives even if the primary control claim only holds per-family).\\n  S1 - DECOY-FAMILY SIGNATURE (the mechanism, falsifiable): random type-matched entity/relation swaps are 'too easy' and therefore anti-conservative (realized FDR exceeds target), whereas document-conditioned counterfactual decoys approach tail-exchangeability. This is diagnosed by a TAIL-CONDITIONED win-rate - the decoy-over-known-false-real win-rate computed among pairs scoring ABOVE the operative cutoff, target ~0.5 - plus a two-sample test of the upper-tail score CDFs, NOT a marginal average that can read 0.5 while failing in the tail.\\n  S2 - INDEPENDENT LABEL-FREE CORROBORATION (necessary, not sufficient): entrapment items built by a mechanism MECHANISTICALLY INDEPENDENT of the decoy generator - foreign-document injection (facts about entities lifted from an unrelated document) and explicit document-contradiction - when scored through the same gate, yield a VALID combined-estimator upper bound on realized false-admission, FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (Wen et al., Nat. Methods 2025; tighter paired form when r=1), that AGREES with the decoy-FDR and with gold on tail-exchangeable families. We claim this agreement is a NECESSARY screening test, never sufficient: because both decoys and entrapment are LLM-fabricated they can co-fail, so the small gold probe is the arbiter and any co-failure (entrapment+decoy agree, gold disagrees) is itself a reported result. We DROP the naive 'sample' ratio (admitted-entrapment / admitted-total) the proteomics literature shows is inherently flawed.\\n  S3 - WEDGE OVER CONFORMAL (the headline comparison): at matched recall (full PR curves with bootstrap CIs), decoy-gating with ZERO labels achieves atomic-fact precision and hallucinated-conclusion rate that match or beat (i) a plain confidence threshold and (ii) the label-using Mohri-Hashimoto conformal-factuality baseline at a small matched label budget - the differentiator being fully label-free OPERATION that gates the fuzzy-unification interface rather than the output.\\n  S4 - PREDICTABLE PROPAGATION (secondary, reduced-scale): tightening alpha reduces the multi-hop hallucinated-conclusion rate in the direction and rough magnitude predicted by a fitted fan-out/conjunction proof-structure model.\\n\\nCLAIM-CHAIN DEPENDENCY DIAGRAM (which result is contingent on which): [tail-exchangeable decoy family] -> [valid label-free corpus-aggregate FDR estimate via TDC/knockoff+] -> [realized FDR tracks target alpha above the achievable-alpha floor, GOLD-ARBITRATED] -> [independent entrapment combined-estimator agreement = necessary corroboration] -> [controlled fact+bridge FDR propagates to reduced multi-hop hallucination]. A break at any arrow is localized and reported; downstream claims are not asserted if an upstream arrow fails.\\n\\nSCOPE (pre-registered to fit $10 / CPU-only). PRIMARY claims (S1-S3 control + signature + wedge) are evaluated on FACTS and fuzzy-unification BRIDGES only, on CLUTRR (paraphrased multi-hop kinship, gold graph) plus a hand-annotated realistic short-document set. Implicit common-sense RULE gating is a SEPARATELY-REPORTED EXPLORATORY arm on a small purpose-built gold rule set (annotated missing rules with plausible-but-wrong distractors); fact-, bridge-, and rule-level calibration are NEVER averaged together. The full baseline bake-off (CoT, RAG, LINC, Logic-LM, conformal selection, coherent factuality, hybrid), the ProbLog/isotonic arm, and the propagation model (S4) are reduced-scale SECONDARY experiments.\",\n  \"motivation\": \"Operational text-to-logic pipelines stall at the same crux: when strict symbolic unification fails, an LLM must perform fuzzy matching and supply background knowledge - and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts (a reasonable-sounding inference the document never states). Practitioners have no quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and only catches encoded violations; and the strongest uncertainty-quantification methods - conformal factuality (Mohri-Hashimoto, ICML 2024), conformal selection + BH (Jin-Candes), coherent factuality - all require a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary. Genomics/proteomics solved an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth - via the knockoff filter and target-decoy competition, AND learned the two failure modes we must respect: (1) decoys 'too unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED decoys, and (2) entrapment FDP must be estimated with a VALID upper-bound estimator (the combined/paired form of Wen et al., Nat. Methods 2025), not the naive sample ratio, and entrapment must be constructed INDEPENDENTLY of the decoys or their agreement is uninformative. Importing all three - matched decoys, the valid combined entrapment estimator, and construction independence - to the fuzzy-unification boundary converts 'reduce hallucination' from a best-effort aspiration into a controlled, label-free, self-corroborated quantity. The wedge over conformal methods is precise: fully label-free operation, gating at the interface rather than the output, and propagation through exact symbolic deduction with per-leaf certificates - directly serving the ACL Knowledge Extraction goal of trustworthy, auditable fact extraction. Crucially the design is built to YIELD INSIGHT EVEN IF EXCHANGEABILITY ONLY HOLDS PARTIALLY: a per-family, per-genre characterization ('counterfactual decoys pass on narrative but fail on legal text') is the publishable core regardless of whether any family achieves full diagonal tracking.\",\n  \"assumptions\": [\n    \"TAIL exchangeability is the crux, and it is TESTED, not assumed. The validity of target-decoy / knockoff control requires that a genuinely-false real proposal and its matched decoy are equally likely to receive any given score IN THE HIGH-SCORE REGION near the operative admission cutoff - not merely on marginal average. We measure a tail-conditioned win-rate (~0.5 among pairs above the cutoff) and a two-sample test of upper-tail CDFs, validate label-free via independent entrapment, arbitrate with a small gold probe, and report per decoy family and per genre where it holds or fails anti-conservatively. A family with marginal win-rate ~0.5 but anti-conservative tail behavior is reported as FAILING.\",\n    \"ENTRAPMENT validity requires the VALID estimator AND construction independence. (a) Realized false-admission is estimated by the combined upper-bound FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (or the tighter paired form at r=1), with the entrapment-to-target ratio r chosen and reported explicitly and propagated into the variance and the achievable-alpha floor; the naive 'sample' ratio is not used. (b) Entrapment is generated by a mechanism INDEPENDENT of the decoy generator - foreign-document injection and explicit document-contradiction, NOT the LLM-counterfactual prior that produces the primary decoys - so their agreement is evidential rather than tautological; we explicitly flag that foreign-entity entrapment vs a cross-document decoy family would be near-redundant and therefore pair foreign-document entrapment against the document-CONDITIONED-COUNTERFACTUAL decoy family. Entrapment agreement is necessary, never sufficient; gold is the arbiter.\",\n    \"The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates document-entailed from non-entailed content better than chance; without such separation in the tail, no thresholding procedure (decoy-gated, conformal, or otherwise) can help.\",\n    \"Corpus-aggregate pooling WITH per-document score normalization is the unit of control. A ~3000-char document yields only ~10-40 candidates, where target-decoy estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable (min non-trivial FDR ~1/(k+1) at k admissions); control is therefore asserted over candidates POOLED across documents within a dataset family. Because raw LLM scores need not be comparable across documents, scores are RANK-NORMALIZED per document (or a per-document transform is fit) before pooling, OR a group-wise target-decoy procedure is used; we verify cross-document score-scale homogeneity and report a sensitivity analysis of the calibration diagonal to the normalization choice. The achievable-alpha floor is reported as a function of candidate count AND r.\",\n    \"Multi-hop deduction error (the SECONDARY S4 claim) is dominated by erroneous admitted facts/bridges rather than the exact symbolic reasoner, and the transfer from fact/bridge-FDR to conclusion-level error - including fan-out (one false fact licensing many false conclusions) and conjunction depth - is captured by an explicit fitted proof-structure model, not assumed to be a smooth monotone map. This claim is not load-bearing for the primary contribution.\"\n  ],\n  \"investigation_approach\": \"Build the pipeline end to end and make TAIL exchangeability and INDEPENDENT entrapment validity the central experimental objects, under a pre-registered compute split. PRE-REGISTERED BUDGET ALLOCATION (of the $10 / CPU-only): ~60% to the HEADLINE - decoy-family showdown + entrapment validity + calibration diagonal on facts+bridges over CLUTRR and the realistic set, adequately powered via a prospective power analysis; ~25% to the load-bearing baseline comparison (plain confidence threshold + Mohri-Hashimoto conformal factuality only); ~15% to clearly-labeled SECONDARY arms (exploratory rule gating, ProbLog/isotonic ablation, S4 propagation, and a single ungated translate-then-prove ablation). DESCOPED EXPLICITLY: full CoT/RAG/LINC/Logic-LM/coherent-factuality/conformal-selection bake-off and the decoy+conformal hybrid are dropped from the primary program (mentioned as future work); ProofWriter/RuleTaker are used ONLY for the secondary S4 propagation experiment (gold proof DAGs are the asset), not for headline extraction.\\n  (1) EXTRACTION: a cheap OpenRouter LLM reads the document and proposes typed first-order facts; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing (to constrain decoy generation and license bridges), NOT for trusted disjointness/cardinality constraints - the FDR claim assumes no constraint ontology.\\n  (2) DECOY GENERATION (the matched-null redesign): the PRIMARY family is document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts/bridges the document does NOT entail, conditioned on the document and types), so their score distribution matches the realized hallucination null. The deliberately-easy random type-matched swap family is retained as the baseline PREDICTED to be anti-conservative. (Cross-document decoys are noted but de-emphasized because they are near-redundant with foreign-entity entrapment.) Every decoy passes an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB + an LLM/human entailment audit on a sample); we report the decoy contamination rate and exclude/down-weight contaminated items.\\n  (3) ENTRAPMENT (independent construction): a held-out set of foreign-document-injection and explicit-contradiction entrapment facts - false BY CONSTRUCTION and generated by a mechanism distinct from the counterfactual decoys - is mixed into the pool at a chosen, reported ratio r.\\n  (4) SCORING: the LLM scores reals, decoys, and entrapment jointly in batched prompts (cost control), returning one confidence per item; scores are rank-normalized per document.\\n  (5) FDR GATE: target-decoy competition / the knockoff+ threshold picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, SEPARATELY for facts and bridges; admitted items enter the KB with a logged certificate.\\n  (6) ENTRAPMENT VALIDATION (label-free, necessary): after gating, the COMBINED estimator FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (paired form reported at r=1) upper-bounds realized false-admission; we compare it against the decoy-FDR and, where available, gold. Agreement corroborates; a CO-FAILURE result (entrapment+decoy agree but gold disagrees) is explicitly hunted for and reported as the key validity caveat.\\n  (7) TAIL-AWARE ECA DIAGNOSTIC (small labeled probe, MEASUREMENT only, never used by the operational gate): on a labeled slice, report the decoy-over-known-false-real win-rate AND the decoy vs false-real score CDFs AS A FUNCTION OF SCORE, with the acceptance criterion defined on the cutoff region (win-rate within tolerance of 0.5 among pairs above the operative threshold + two-sample test of upper tails). This diagnostic is predicted to agree with the realized-vs-target diagonal in experiment (a).\\n  (8) REASONING: admitted facts/bridges populate SWI-Prolog for crisp multi-hop deduction (PRIMARY mode, keeping the headline FDR contribution independent of any calibration); backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted bridge) plus the decoy-competition + entrapment certificate. A ProbLog arm with an EXPLICIT isotonic score->probability map (fit on the small probe) is a SECONDARY ablation, ablated against crisp gating.\\n  (9) EXPLORATORY RULE GATING (separately reported): a small gold set of proofs requiring an unstated implicit common-sense bridging rule, each paired with correct and plausible-but-wrong distractor rules, evaluates rule-level FDR directly; results are reported apart from facts/bridges.\\n  (10) PROPAGATION (SECONDARY, S4): a Monte-Carlo simulator injects false facts at controlled FDR into actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error from fan-out and conjunction depth; we test whether it predicts measured amplification.\\n  DATASETS: CLUTRR (paraphrased) + an enlarged hand-annotated set of short legal/news/kids'-story documents carry the headline facts+bridges claims (sized by power analysis, with the legal-vs-narrative split designed to expose per-genre exchangeability differences); ProofWriter/RuleTaker only for S4. Gold labels are used ONLY for evaluation and the optional probe; the operational gate is label-free.\\n  BASELINES (load-bearing only): plain confidence/self-consistency threshold and Mohri-Hashimoto conformal factuality at a small matched label budget, plus the ungated translate-then-prove ablation. Matched-recall is operationalized as full PR CURVES with bootstrap CIs (gated method sweeps its threshold; free-form baselines decomposed into atomic claims and matched to gold by entailment).\\n  EXPERIMENTS: (a) validity-of-control - sweep alpha, measure realized corpus-aggregate FDR via entrapment-combined-estimator and gold, test diagonal tracking above the achievable-alpha floor, report sensitivity to per-document normalization; (b) decoy-family showdown - TAIL win-rate + entrapment agreement per family/genre, testing that counterfactual decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction PR curves vs the load-bearing baselines on facts+bridges; (d) [secondary] multi-hop accuracy and S4 propagation; (e) [secondary/exploratory] rule-gating gold; (f) cost check (LLM spend < $10, CPU-only) + qualitative auditable trace-graphs.\",\n  \"success_criteria\": \"PRIMARY (headline, adequately powered on facts+bridges over CLUTRR + realistic set). CONFIRMED if: (1) for at least one decoy family, realized corpus-aggregate FDR tracks target alpha within a small tolerance ABOVE the achievable-alpha floor (calibration diagonal), stable under the per-document normalization sensitivity check, AND the INDEPENDENT entrapment combined-estimator upper bound agrees with both the decoy estimate and gold - demonstrating self-corroborated, label-free control; (2) the decoy-family showdown shows the mechanism's signature in the TAIL: counterfactual decoys achieve tail-conditioned win-rate ~0.5 (and pass the upper-tail two-sample test) with entrapment+gold agreement, while random type-matched swaps are measurably anti-conservative - establishing that the redesign, not luck, drives validity; (3) at matched recall (PR curves with CIs), decoy-gating yields atomic-fact precision and hallucinated-conclusion rate that match or beat a plain confidence threshold AND the label-using Mohri-Hashimoto conformal baseline at a small matched label budget - with the zero-label operation as the wedge.\\n  CONTRIBUTION-SURVIVES-PARTIAL clause (de-risking the most likely outcome): even if NO family achieves full diagonal tracking, a clean per-family, per-genre CHARACTERIZATION of when tail-exchangeability and independent-entrapment agreement can or cannot be engineered for LLM proposals (e.g., 'counterfactual decoys pass on narrative but fail on legal text'), together with the documented co-failure cases, is itself the reportable headline contribution.\\n  SECONDARY. (4) tightening alpha reduces multi-hop hallucination in the direction predicted by the fitted proof-structure model (S4); (5) ablating the decoy gate (trusting LLM fuzzy unification) measurably worsens hallucination; (6) exploratory rule-gating shows decoy competition separates correct from plausible-but-wrong implicit rules above chance on the small gold set; (7) the pipeline runs on commodity CPU within $10 and produces auditable trace-graphs with per-leaf decoy+entrapment certificates.\\n  DISCONFIRMED if: NO decoy family achieves tail-exchangeable, gold-arbitrated diagonal tracking above the alpha-floor on EITHER genre (with random AND counterfactual decoys both anti-conservative in the tail), AND the entrapment combined-estimator systematically co-fails with the decoys against gold; OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by Mohri-Hashimoto conformal even accounting for its zero-label advantage. A negative that characterizes the failure boundary remains a contribution; an UNINTERPRETABLE null (control neither clearly holds nor clearly fails anywhere) is the true failure.\",\n  \"related_works\": [\n    \"Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench tool, Noble-Lab/FDRBench): provides the theory of entrapment FDP estimation, shows the naive 'sample' estimator (N_E/r / N_T) is inherently flawed (can over- AND under-estimate), and gives the VALID combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E) and a tighter PAIRED form at r=1. WE ADOPT this estimator wholesale to fix the previously-naive ratio, choose and report r, and propagate r into variance and the alpha-floor. Difference: their domain is mass spectrometry peptide identification; we transplant the estimator AND the construction-independence principle (entrapment must be built unlike the decoys) to validate LLM fact/bridge admission.\",\n    \"Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes claims until a user-specified factuality alpha is met via conformal prediction with a few labeled samples. NOW THE PRIMARY load-bearing baseline. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT rather than the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no independent entrapment validation, and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification interface.\",\n    \"Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to select candidates with FDR control under exchangeability of labeled calibration and test data. Demoted to secondary/future comparison. Difference: needs labeled calibration outcomes; we estimate and control FDR with NO labels by competing each proposal against engineered decoys and corroborate via independent entrapment.\",\n    \"Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt knockoff+ thresholding to the LLM neural-to-symbolic boundary and confront the Equal-Chance-Assumption failure mode in the high-score TAIL (not just marginally) with plausibility-matched decoys.\",\n    \"Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition): generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference: lives entirely in molecular screening / mass spectrometry; we import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too easy' - to design LLM fact/bridge decoys as document-conditioned counterfactuals, never done for LLM-proposed symbolic assertions.\",\n    \"LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into FOL executed by a theorem prover with majority voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated translations enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee. (Descoped from our primary baseline set for feasibility; noted as comparison context.)\",\n    \"Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver with self-refinement on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically valid but fabricated premise is never challenged; no statistical control of false extractions.\",\n    \"Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including where the ontology is silent - complementary.\",\n    \"Conformal factuality for reasoning chains, 'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126, 2025): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning chains, with a labeled calibration set. Difference: labeled, certifies coverage over claim graphs rather than gating which extracted facts/bridges enter a symbolic KB; no decoys, no independent entrapment, no label-free knob. (Descoped to future comparison.)\"\n  ],\n  \"inspiration\": \"A Level-3 (methodological) cross-domain transfer, now sharpened twice by review. Genomics/proteomics solved the hardest label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry). That field ALSO discovered the two ways the trick breaks: (1) decoys 'too unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED decoys (DeepCoy, protein-LM decoys); and (2) entrapment FDP must be estimated with a VALID upper bound - the combined/paired estimator of Wen et al. (Nature Methods 2025), NOT the naive sample ratio - and the entrapment set must be CONSTRUCTED DIFFERENTLY from the decoys, or their agreement proves nothing. I map all three onto the exact pressure point of a text-to-logic pipeline - the fuzzy-unification boundary where the LLM aligns predicates and supplies background knowledge - and import the matched-decoy cure, the valid combined entrapment estimator (with an explicit entrapment-to-target ratio r), and the construction-independence requirement specifically to defeat the anti-conservative failure: the dangerous hallucinations are PLAUSIBLE high-confidence false facts, so the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE TAIL (not on average), and the FDR must be corroborated by entrapment built unlike the decoys and arbitrated by a small gold probe. This turns the prompt's vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically disciplined, self-corroborated, label-free gate whose hallucination rate is a tunable, certified, auditable quantity.\",\n  \"terms\": [\n    {\n      \"term\": \"Plausibility-matched (counterfactual) decoy\",\n      \"definition\": \"A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's OWN prior over document-plausible-but-non-entailed content - a document-conditioned counterfactual the model finds plausible - so its confidence-score distribution reproduces that of genuine plausible hallucinations. This is the redesign that replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic (anti-conservative).\"\n    },\n    {\n      \"term\": \"Tail-conditioned win-rate (tail-aware ECA diagnostic)\",\n      \"definition\": \"The decoy-over-known-false-real win-rate computed ONLY among matched pairs whose scores fall ABOVE the operative admission cutoff, reported together with the decoy and false-real score CDFs as a function of score and an upper-tail two-sample test. Target ~0.5 in the tail. It supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative exactly where admissions occur. Used for measurement only, never by the operational gate.\"\n    },\n    {\n      \"term\": \"Combined / paired entrapment estimator and the ratio r\",\n      \"definition\": \"The VALID entrapment upper bound on realized false-admission: FDP_hat = N_E(1 + 1/r)/(N_T + N_E), where N_T = admitted real items, N_E = admitted entrapment items, and r = entrapment-to-target ratio (chosen and reported; e.g., r=1 for the tighter PAIRED form). It replaces the inherently-flawed naive 'sample' ratio (admitted-entrapment / admitted-total). r is propagated into the variance and the achievable-alpha floor.\"\n    },\n    {\n      \"term\": \"Independent entrapment and co-failure detection\",\n      \"definition\": \"Entrapment items are built by a mechanism DISTINCT from the decoy generator - foreign-document injection (foreign entities) and explicit document-contradiction - so their agreement with the LLM-counterfactual decoy FDR is evidential, not tautological. Because both are nonetheless LLM-handled, agreement is treated as NECESSARY not sufficient; the small gold probe is the arbiter, and any CO-FAILURE (entrapment+decoy agree but gold disagrees) is explicitly reported as the validity caveat.\"\n    },\n    {\n      \"term\": \"Equal Chance Assumption (tail exchangeability)\",\n      \"definition\": \"The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched decoy are equally likely to receive any given score, IN THE HIGH-SCORE TAIL where admissions occur. If decoys under-score the rare very-high-confidence plausible hallucinations, admitted decoys under-count admitted false reals and realized FDR exceeds target. We test it in the tail and validate it via independent entrapment rather than assume it.\"\n    },\n    {\n      \"term\": \"Per-document score normalization and group-wise control\",\n      \"definition\": \"Because raw LLM confidence scores need not be comparable across documents, scores are rank-normalized per document (or a per-document transform is fit) before pooling for corpus-aggregate target-decoy control - or a group-wise procedure respecting document structure is used - so a false real from an 'easy' document cannot spuriously out-rank decoys from a 'hard' one. Cross-document homogeneity is verified and a sensitivity analysis of the calibration diagonal to the normalization choice is reported.\"\n    },\n    {\n      \"term\": \"Corpus-aggregate FDR and the achievable-alpha floor\",\n      \"definition\": \"Control is asserted over candidates POOLED across documents within a dataset family (a single ~3000-char document yields too few candidates for stable control, with min non-trivial FDR ~1/(k+1) at k admissions and the knockoff+ '+1' offset). The achievable-alpha floor - the smallest target alpha reachable given candidate count AND the entrapment ratio r - is reported explicitly; per-document control is a secondary, high-variance quantity.\"\n    },\n    {\n      \"term\": \"Target-decoy competition / knockoff+ threshold\",\n      \"definition\": \"A label-free selection rule: rank reals and decoys by (per-document-normalized) score and choose the most permissive cutoff at which the decoy-estimated FDR ((admitted decoys + 1) / admitted reals) stays below alpha, applied separately to facts and bridges. Admitted items enter the KB with a certificate; the rest are rejected with their losing competition logged.\"\n    },\n    {\n      \"term\": \"Fuzzy unification and bridge rule\",\n      \"definition\": \"Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g., 'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y)) admitted only if it clears the decoy gate. Facts and bridges - NOT implicit common-sense rules - carry the headline FDR-control claim.\"\n    },\n    {\n      \"term\": \"Trace-graph\",\n      \"definition\": \"A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications, and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and entrapment certificate that licensed it.\"\n    }\n  ],\n  \"summary\": \"We gate the fuzzy-unification boundary of a text-to-logic pipeline so every LLM-proposed fact and bridge rule must out-compete plausibility-matched counterfactual decoys (target-decoy / knockoff+ thresholding) before entering a Prolog knowledge base, controlling the corpus-aggregate hallucination rate to a user-specified target with NO labels; validity is tested in the high-score TAIL (not on average) and corroborated by an independently-constructed entrapment set scored through the VALID combined estimator FDP=N_E(1+1/r)/(N_T+N_E), with a small gold probe as arbiter. We predict this label-free gate matches or beats a plain confidence threshold and the label-using Mohri-Hashimoto conformal baseline on fact precision and hallucination at matched recall, and that a per-family/per-genre characterization of where tail-exchangeability holds is the publishable core even if full diagonal control is only partial.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [28] ASSISTANT · 2026-06-16 03:42:57 UTC

```
Let me validate the JSON output against the schema.
```

### [29] TOOL CALL — Bash · 2026-06-16 03:42:57 UTC

```
Validate JSON structure and confirm key fixes present:
python3 -c "
import json
with open('.terminal_claude_agent_struct_out.json') as f:
    d = json.load(f)
req = ['title','hypothesis','motivation','assumptions','investigation_approach','success_criteria','related_works','inspiration','terms','summary']
missing = [k for k in req if k not in d]
print('Valid JSON. Missing required:', missing)
print('assumptions:', len(d['assumptions']), '| related_works:', len(d['related_works']), '| terms:', len(d['terms']))
for t in d['terms']:
    assert 'term' in t and 'definition' in t, t
print('All terms have term+definition.')
print('Title len:', len(d['title']))
# quick check the key fixes are present
h = d['hypothesis']
for k in ['N_E*(1 + 1/r)','tail','TAIL','PRIMARY','S1','S2','S3','S4','CLAIM-CHAIN','DESCOPED']:
    print(f'  contains {k!r}:', k in h or k in d['investigation_approach'])
"
```

### [30] TOOL RESULT — Bash · 2026-06-16 03:42:57 UTC

```
{"stdout": "Valid JSON. Missing required: []\nassumptions: 5 | related_works: 9 | terms: 10\nAll terms have term+definition.\nTitle len: 205\n  contains 'N_E*(1 + 1/r)': True\n  contains 'tail': True\n  contains 'TAIL': True\n  contains 'PRIMARY': True\n  contains 'S1': True\n  contains 'S2': True\n  contains 'S3': True\n  contains 'S4': True\n  contains 'CLAIM-CHAIN': True\n  contains 'DESCOPED': True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [31] ASSISTANT · 2026-06-16 03:43:10 UTC

```
The revised hypothesis is written and validated. Here's how it addresses each of the reviewer's six critiques:

**1. Scope ballooned (major)** → Pre-registered a compute split (~60% headline / ~25% load-bearing baselines / ~15% secondary) and an explicit **DESCOPED** list. The genuinely-novel core (decoy-family showdown + entrapment validity + calibration diagonal on **facts + bridges**) is the adequately-powered headline; the baseline set is cut to the two load-bearing comparisons (plain confidence threshold + Mohri-Hashimoto); ProbLog, propagation, and ProofWriter/RuleTaker are clearly-labeled secondary arms.

**2a. Wrong entrapment estimator (major)** → Replaced the flawed "sample" ratio with the **valid combined upper bound** `FDP̂ = N_E(1 + 1/r)/(N_T + N_E)` (paired form at r=1), with the entrapment-to-target ratio **r** chosen, reported, and propagated into variance and the achievable-alpha floor. Cited Wen et al. (Nature Methods 2025) and FDRBench — I fetched the paper to confirm the exact formula.

**2b. Co-failure / non-independence (major)** → Entrapment is now **mechanistically independent** of the decoy generator (foreign-document injection + explicit contradiction, vs. LLM-counterfactual decoys), with the near-redundant cross-document/foreign-entity pairing explicitly avoided. Entrapment agreement is framed as **necessary-not-sufficient**, gold is the arbiter, and **co-failure detection** (entrapment+decoy agree but gold disagrees) is a first-class reported result.

**3. Marginal vs. tail win-rate (major)** → The ECA diagnostic is now **tail-conditioned**: win-rate ~0.5 among pairs *above the operative cutoff* + score-CDF curves + an upper-tail two-sample test, explicitly predicted to agree with the realized-vs-target diagonal.

**4. Rule-gating lacks gold (minor)** → Primary claims scoped to **facts + bridges**; implicit-rule gating demoted to a separately-reported exploratory arm on a purpose-built gold rule set with plausible-but-wrong distractors. Fact/bridge/rule calibration are never averaged.

**5. Cross-document score comparability (minor)** → Added **per-document rank-normalization** (or group-wise TDC) before pooling, with homogeneity verification and a sensitivity analysis of the calibration diagonal.

**6. Density (minor)** → Restructured into a crisp **PRIMARY** claim + four enumerated **secondary claims (S1–S4)** + a one-line **claim-chain dependency diagram**, with caveats pushed into assumptions/method.

I also added the **contribution-survives-partial-exchangeability** clause the reviewer requested: a per-family/per-genre characterization ("counterfactual decoys pass on narrative but fail on legal") is the publishable core even if no family achieves full diagonal control.

Output written to `./.terminal_claude_agent_struct_out.json` (valid against the schema: all 10 required fields, 5 assumptions, 9 related works, 10 terms).

Sources: [Wen et al., Nature Methods 2025 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/), [Noble-Lab/FDRBench](https://github.com/Noble-Lab/FDRBench).
```
