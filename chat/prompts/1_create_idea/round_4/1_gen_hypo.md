# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 4 · `gen_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 03:47:58 UTC

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
  Tail-Exchangeable Decoy Competition with Independent Entrapment Validation: Label-Free False-Discovery-Rate Control of Fact
  and Bridge Admission at the Fuzzy-Unification Boundary of Text-to-Logic Pipelines
hypothesis: |-
  PRIMARY CLAIM. At the neural-to-symbolic admission boundary of a text-to-logic pipeline - where an LLM proposes (a) atomic facts extracted from a ~3000-char document and (b) fuzzy-unification BRIDGE rules that align a document predicate to an ontology/rule predicate when strict unification fails - competing every proposal against PLAUSIBILITY-MATCHED synthetic decoys drawn from the LLM's own prior over document-plausible-but-non-entailed content, then selecting the admission cutoff by target-decoy / knockoff+ competition, controls the corpus-aggregate false-admission rate (FDR) of the resulting SWI-Prolog knowledge base to a user-specified target alpha WITH NO ground-truth labels - PROVIDED the decoys are exchangeable with realized hallucinations IN THE HIGH-SCORE TAIL where admissions actually occur (not merely on marginal average).

  SECONDARY CLAIMS (each independently testable; the contribution survives even if the primary control claim only holds per-family).
    S1 - DECOY-FAMILY SIGNATURE (the mechanism, falsifiable): random type-matched entity/relation swaps are 'too easy' and therefore anti-conservative (realized FDR exceeds target), whereas document-conditioned counterfactual decoys approach tail-exchangeability. This is diagnosed by a TAIL-CONDITIONED win-rate - the decoy-over-known-false-real win-rate computed among pairs scoring ABOVE the operative cutoff, target ~0.5 - plus a two-sample test of the upper-tail score CDFs, NOT a marginal average that can read 0.5 while failing in the tail.
    S2 - INDEPENDENT LABEL-FREE CORROBORATION (necessary, not sufficient): entrapment items built by a mechanism MECHANISTICALLY INDEPENDENT of the decoy generator - foreign-document injection (facts about entities lifted from an unrelated document) and explicit document-contradiction - when scored through the same gate, yield a VALID combined-estimator upper bound on realized false-admission, FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (Wen et al., Nat. Methods 2025; tighter paired form when r=1), that AGREES with the decoy-FDR and with gold on tail-exchangeable families. We claim this agreement is a NECESSARY screening test, never sufficient: because both decoys and entrapment are LLM-fabricated they can co-fail, so the small gold probe is the arbiter and any co-failure (entrapment+decoy agree, gold disagrees) is itself a reported result. We DROP the naive 'sample' ratio (admitted-entrapment / admitted-total) the proteomics literature shows is inherently flawed.
    S3 - WEDGE OVER CONFORMAL (the headline comparison): at matched recall (full PR curves with bootstrap CIs), decoy-gating with ZERO labels achieves atomic-fact precision and hallucinated-conclusion rate that match or beat (i) a plain confidence threshold and (ii) the label-using Mohri-Hashimoto conformal-factuality baseline at a small matched label budget - the differentiator being fully label-free OPERATION that gates the fuzzy-unification interface rather than the output.
    S4 - PREDICTABLE PROPAGATION (secondary, reduced-scale): tightening alpha reduces the multi-hop hallucinated-conclusion rate in the direction and rough magnitude predicted by a fitted fan-out/conjunction proof-structure model.

  CLAIM-CHAIN DEPENDENCY DIAGRAM (which result is contingent on which): [tail-exchangeable decoy family] -> [valid label-free corpus-aggregate FDR estimate via TDC/knockoff+] -> [realized FDR tracks target alpha above the achievable-alpha floor, GOLD-ARBITRATED] -> [independent entrapment combined-estimator agreement = necessary corroboration] -> [controlled fact+bridge FDR propagates to reduced multi-hop hallucination]. A break at any arrow is localized and reported; downstream claims are not asserted if an upstream arrow fails.

  SCOPE (pre-registered to fit $10 / CPU-only). PRIMARY claims (S1-S3 control + signature + wedge) are evaluated on FACTS and fuzzy-unification BRIDGES only, on CLUTRR (paraphrased multi-hop kinship, gold graph) plus a hand-annotated realistic short-document set. Implicit common-sense RULE gating is a SEPARATELY-REPORTED EXPLORATORY arm on a small purpose-built gold rule set (annotated missing rules with plausible-but-wrong distractors); fact-, bridge-, and rule-level calibration are NEVER averaged together. The full baseline bake-off (CoT, RAG, LINC, Logic-LM, conformal selection, coherent factuality, hybrid), the ProbLog/isotonic arm, and the propagation model (S4) are reduced-scale SECONDARY experiments.
motivation: >-
  Operational text-to-logic pipelines stall at the same crux: when strict symbolic unification fails, an LLM must perform
  fuzzy matching and supply background knowledge - and that interface is exactly where hallucination re-enters and silently
  corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence
  false facts (a reasonable-sounding inference the document never states). Practitioners have no quantitative, label-free
  knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted
  constraints and only catches encoded violations; and the strongest uncertainty-quantification methods - conformal factuality
  (Mohri-Hashimoto, ICML 2024), conformal selection + BH (Jin-Candes), coherent factuality - all require a LABELED calibration
  set and certify the final answer or claim set, not the neural-to-symbolic admission boundary. Genomics/proteomics solved
  an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth
  - via the knockoff filter and target-decoy competition, AND learned the two failure modes we must respect: (1) decoys 'too
  unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED decoys, and (2) entrapment FDP must be
  estimated with a VALID upper-bound estimator (the combined/paired form of Wen et al., Nat. Methods 2025), not the naive
  sample ratio, and entrapment must be constructed INDEPENDENTLY of the decoys or their agreement is uninformative. Importing
  all three - matched decoys, the valid combined entrapment estimator, and construction independence - to the fuzzy-unification
  boundary converts 'reduce hallucination' from a best-effort aspiration into a controlled, label-free, self-corroborated
  quantity. The wedge over conformal methods is precise: fully label-free operation, gating at the interface rather than the
  output, and propagation through exact symbolic deduction with per-leaf certificates - directly serving the ACL Knowledge
  Extraction goal of trustworthy, auditable fact extraction. Crucially the design is built to YIELD INSIGHT EVEN IF EXCHANGEABILITY
  ONLY HOLDS PARTIALLY: a per-family, per-genre characterization ('counterfactual decoys pass on narrative but fail on legal
  text') is the publishable core regardless of whether any family achieves full diagonal tracking.
assumptions:
- >-
  TAIL exchangeability is the crux, and it is TESTED, not assumed. The validity of target-decoy / knockoff control requires
  that a genuinely-false real proposal and its matched decoy are equally likely to receive any given score IN THE HIGH-SCORE
  REGION near the operative admission cutoff - not merely on marginal average. We measure a tail-conditioned win-rate (~0.5
  among pairs above the cutoff) and a two-sample test of upper-tail CDFs, validate label-free via independent entrapment,
  arbitrate with a small gold probe, and report per decoy family and per genre where it holds or fails anti-conservatively.
  A family with marginal win-rate ~0.5 but anti-conservative tail behavior is reported as FAILING.
- >-
  ENTRAPMENT validity requires the VALID estimator AND construction independence. (a) Realized false-admission is estimated
  by the combined upper-bound FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (or the tighter paired form at r=1), with the entrapment-to-target
  ratio r chosen and reported explicitly and propagated into the variance and the achievable-alpha floor; the naive 'sample'
  ratio is not used. (b) Entrapment is generated by a mechanism INDEPENDENT of the decoy generator - foreign-document injection
  and explicit document-contradiction, NOT the LLM-counterfactual prior that produces the primary decoys - so their agreement
  is evidential rather than tautological; we explicitly flag that foreign-entity entrapment vs a cross-document decoy family
  would be near-redundant and therefore pair foreign-document entrapment against the document-CONDITIONED-COUNTERFACTUAL decoy
  family. Entrapment agreement is necessary, never sufficient; gold is the arbiter.
- >-
  The LLM emits a usable, roughly monotone confidence/score for each proposed item (real, decoy, or entrapment) that separates
  document-entailed from non-entailed content better than chance; without such separation in the tail, no thresholding procedure
  (decoy-gated, conformal, or otherwise) can help.
- >-
  Corpus-aggregate pooling WITH per-document score normalization is the unit of control. A ~3000-char document yields only
  ~10-40 candidates, where target-decoy estimates are high-variance and the knockoff+ '+1' offset makes small alpha unachievable
  (min non-trivial FDR ~1/(k+1) at k admissions); control is therefore asserted over candidates POOLED across documents within
  a dataset family. Because raw LLM scores need not be comparable across documents, scores are RANK-NORMALIZED per document
  (or a per-document transform is fit) before pooling, OR a group-wise target-decoy procedure is used; we verify cross-document
  score-scale homogeneity and report a sensitivity analysis of the calibration diagonal to the normalization choice. The achievable-alpha
  floor is reported as a function of candidate count AND r.
- >-
  Multi-hop deduction error (the SECONDARY S4 claim) is dominated by erroneous admitted facts/bridges rather than the exact
  symbolic reasoner, and the transfer from fact/bridge-FDR to conclusion-level error - including fan-out (one false fact licensing
  many false conclusions) and conjunction depth - is captured by an explicit fitted proof-structure model, not assumed to
  be a smooth monotone map. This claim is not load-bearing for the primary contribution.
investigation_approach: |-
  Build the pipeline end to end and make TAIL exchangeability and INDEPENDENT entrapment validity the central experimental objects, under a pre-registered compute split. PRE-REGISTERED BUDGET ALLOCATION (of the $10 / CPU-only): ~60% to the HEADLINE - decoy-family showdown + entrapment validity + calibration diagonal on facts+bridges over CLUTRR and the realistic set, adequately powered via a prospective power analysis; ~25% to the load-bearing baseline comparison (plain confidence threshold + Mohri-Hashimoto conformal factuality only); ~15% to clearly-labeled SECONDARY arms (exploratory rule gating, ProbLog/isotonic ablation, S4 propagation, and a single ungated translate-then-prove ablation). DESCOPED EXPLICITLY: full CoT/RAG/LINC/Logic-LM/coherent-factuality/conformal-selection bake-off and the decoy+conformal hybrid are dropped from the primary program (mentioned as future work); ProofWriter/RuleTaker are used ONLY for the secondary S4 propagation experiment (gold proof DAGs are the asset), not for headline extraction.
    (1) EXTRACTION: a cheap OpenRouter LLM reads the document and proposes typed first-order facts; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing (to constrain decoy generation and license bridges), NOT for trusted disjointness/cardinality constraints - the FDR claim assumes no constraint ontology.
    (2) DECOY GENERATION (the matched-null redesign): the PRIMARY family is document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts/bridges the document does NOT entail, conditioned on the document and types), so their score distribution matches the realized hallucination null. The deliberately-easy random type-matched swap family is retained as the baseline PREDICTED to be anti-conservative. (Cross-document decoys are noted but de-emphasized because they are near-redundant with foreign-entity entrapment.) Every decoy passes an explicit NON-ENTAILMENT check (symbolic non-derivability against the admitted KB + an LLM/human entailment audit on a sample); we report the decoy contamination rate and exclude/down-weight contaminated items.
    (3) ENTRAPMENT (independent construction): a held-out set of foreign-document-injection and explicit-contradiction entrapment facts - false BY CONSTRUCTION and generated by a mechanism distinct from the counterfactual decoys - is mixed into the pool at a chosen, reported ratio r.
    (4) SCORING: the LLM scores reals, decoys, and entrapment jointly in batched prompts (cost control), returning one confidence per item; scores are rank-normalized per document.
    (5) FDR GATE: target-decoy competition / the knockoff+ threshold picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, SEPARATELY for facts and bridges; admitted items enter the KB with a logged certificate.
    (6) ENTRAPMENT VALIDATION (label-free, necessary): after gating, the COMBINED estimator FDP_hat = N_E*(1 + 1/r)/(N_T + N_E) (paired form reported at r=1) upper-bounds realized false-admission; we compare it against the decoy-FDR and, where available, gold. Agreement corroborates; a CO-FAILURE result (entrapment+decoy agree but gold disagrees) is explicitly hunted for and reported as the key validity caveat.
    (7) TAIL-AWARE ECA DIAGNOSTIC (small labeled probe, MEASUREMENT only, never used by the operational gate): on a labeled slice, report the decoy-over-known-false-real win-rate AND the decoy vs false-real score CDFs AS A FUNCTION OF SCORE, with the acceptance criterion defined on the cutoff region (win-rate within tolerance of 0.5 among pairs above the operative threshold + two-sample test of upper tails). This diagnostic is predicted to agree with the realized-vs-target diagonal in experiment (a).
    (8) REASONING: admitted facts/bridges populate SWI-Prolog for crisp multi-hop deduction (PRIMARY mode, keeping the headline FDR contribution independent of any calibration); backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted bridge) plus the decoy-competition + entrapment certificate. A ProbLog arm with an EXPLICIT isotonic score->probability map (fit on the small probe) is a SECONDARY ablation, ablated against crisp gating.
    (9) EXPLORATORY RULE GATING (separately reported): a small gold set of proofs requiring an unstated implicit common-sense bridging rule, each paired with correct and plausible-but-wrong distractor rules, evaluates rule-level FDR directly; results are reported apart from facts/bridges.
    (10) PROPAGATION (SECONDARY, S4): a Monte-Carlo simulator injects false facts at controlled FDR into actual ProofWriter/CLUTRR proof DAGs and predicts conclusion-level error from fan-out and conjunction depth; we test whether it predicts measured amplification.
    DATASETS: CLUTRR (paraphrased) + an enlarged hand-annotated set of short legal/news/kids'-story documents carry the headline facts+bridges claims (sized by power analysis, with the legal-vs-narrative split designed to expose per-genre exchangeability differences); ProofWriter/RuleTaker only for S4. Gold labels are used ONLY for evaluation and the optional probe; the operational gate is label-free.
    BASELINES (load-bearing only): plain confidence/self-consistency threshold and Mohri-Hashimoto conformal factuality at a small matched label budget, plus the ungated translate-then-prove ablation. Matched-recall is operationalized as full PR CURVES with bootstrap CIs (gated method sweeps its threshold; free-form baselines decomposed into atomic claims and matched to gold by entailment).
    EXPERIMENTS: (a) validity-of-control - sweep alpha, measure realized corpus-aggregate FDR via entrapment-combined-estimator and gold, test diagonal tracking above the achievable-alpha floor, report sensitivity to per-document normalization; (b) decoy-family showdown - TAIL win-rate + entrapment agreement per family/genre, testing that counterfactual decoys move onto the diagonal while random swaps are anti-conservative; (c) extraction PR curves vs the load-bearing baselines on facts+bridges; (d) [secondary] multi-hop accuracy and S4 propagation; (e) [secondary/exploratory] rule-gating gold; (f) cost check (LLM spend < $10, CPU-only) + qualitative auditable trace-graphs.
success_criteria: |-
  PRIMARY (headline, adequately powered on facts+bridges over CLUTRR + realistic set). CONFIRMED if: (1) for at least one decoy family, realized corpus-aggregate FDR tracks target alpha within a small tolerance ABOVE the achievable-alpha floor (calibration diagonal), stable under the per-document normalization sensitivity check, AND the INDEPENDENT entrapment combined-estimator upper bound agrees with both the decoy estimate and gold - demonstrating self-corroborated, label-free control; (2) the decoy-family showdown shows the mechanism's signature in the TAIL: counterfactual decoys achieve tail-conditioned win-rate ~0.5 (and pass the upper-tail two-sample test) with entrapment+gold agreement, while random type-matched swaps are measurably anti-conservative - establishing that the redesign, not luck, drives validity; (3) at matched recall (PR curves with CIs), decoy-gating yields atomic-fact precision and hallucinated-conclusion rate that match or beat a plain confidence threshold AND the label-using Mohri-Hashimoto conformal baseline at a small matched label budget - with the zero-label operation as the wedge.
    CONTRIBUTION-SURVIVES-PARTIAL clause (de-risking the most likely outcome): even if NO family achieves full diagonal tracking, a clean per-family, per-genre CHARACTERIZATION of when tail-exchangeability and independent-entrapment agreement can or cannot be engineered for LLM proposals (e.g., 'counterfactual decoys pass on narrative but fail on legal text'), together with the documented co-failure cases, is itself the reportable headline contribution.
    SECONDARY. (4) tightening alpha reduces multi-hop hallucination in the direction predicted by the fitted proof-structure model (S4); (5) ablating the decoy gate (trusting LLM fuzzy unification) measurably worsens hallucination; (6) exploratory rule-gating shows decoy competition separates correct from plausible-but-wrong implicit rules above chance on the small gold set; (7) the pipeline runs on commodity CPU within $10 and produces auditable trace-graphs with per-leaf decoy+entrapment certificates.
    DISCONFIRMED if: NO decoy family achieves tail-exchangeable, gold-arbitrated diagonal tracking above the alpha-floor on EITHER genre (with random AND counterfactual decoys both anti-conservative in the tail), AND the entrapment combined-estimator systematically co-fails with the decoys against gold; OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall AND is dominated by Mohri-Hashimoto conformal even accounting for its zero-label advantage. A negative that characterizes the failure boundary remains a contribution; an UNINTERPRETABLE null (control neither clearly holds nor clearly fails anywhere) is the true failure.
related_works:
- >-
  Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis
  using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench tool, Noble-Lab/FDRBench): provides the theory of entrapment
  FDP estimation, shows the naive 'sample' estimator (N_E/r / N_T) is inherently flawed (can over- AND under-estimate), and
  gives the VALID combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E) and a tighter PAIRED form at r=1. WE ADOPT this estimator
  wholesale to fix the previously-naive ratio, choose and report r, and propagate r into variance and the alpha-floor. Difference:
  their domain is mass spectrometry peptide identification; we transplant the estimator AND the construction-independence
  principle (entrapment must be built unlike the decoys) to validate LLM fact/bridge admission.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes
  claims until a user-specified factuality alpha is met via conformal prediction with a few labeled samples. NOW THE PRIMARY
  load-bearing baseline. Difference: it requires a labeled calibration set, certifies the final filtered OUTPUT rather than
  the neural-to-symbolic admission boundary, and provides no synthetic-decoy mechanism, no independent entrapment validation,
  and no symbolic propagation with per-leaf certificates. Our wedge is fully label-free operation at the fuzzy-unification
  interface.
- >-
  Jin & Candes, conformal selection / 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values +
  Benjamini-Hochberg to select candidates with FDR control under exchangeability of labeled calibration and test data. Demoted
  to secondary/future comparison. Difference: needs labeled calibration outcomes; we estimate and control FDR with NO labels
  by competing each proposal against engineered decoys and corroborate via independent entrapment.
- >-
  Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition
  (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against
  a synthetic negative control. Difference: this machinery lives in numeric feature selection and mass spectrometry; we adapt
  knockoff+ thresholding to the LLM neural-to-symbolic boundary and confront the Equal-Chance-Assumption failure mode in the
  high-score TAIL (not just marginally) with plausibility-matched decoys.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using
  deep learning', Bioinformatics 2021; protein-language-model decoys for target-decoy competition): generate decoys that reproduce
  the score properties of true positives so target-decoy FDR is well-calibrated. Difference: lives entirely in molecular screening
  / mass spectrometry; we import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too
  easy' - to design LLM fact/bridge decoys as document-conditioned counterfactuals, never done for LLM-proposed symbolic assertions.
- >-
  LINC (Olausson et al., EMNLP 2023): an LLM semantic-parses premises into FOL executed by a theorem prover with majority
  voting over translations. Difference: no principled control over WHICH extracted content is admitted - hallucinated translations
  enter freely and voting only smooths variance; no FDR knob, no decoys, no label-free precision guarantee. (Descoped from
  our primary baseline set for feasibility; noted as comparison context.)
- >-
  Logic-LM (Pan et al., Findings of EMNLP 2023): an LLM formulates a symbolic problem run by a solver with self-refinement
  on solver error messages. Difference: refinement repairs syntactic/solver errors, not factual hallucination - a syntactically
  valid but fabricated premise is never challenged; no statistical control of false extractions.
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including
  where the ontology is silent - complementary.
- >-
  Conformal factuality for reasoning chains, 'Conformal Language Model Reasoning with Coherent Factuality' (arXiv 2505.17126,
  2025): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning chains,
  with a labeled calibration set. Difference: labeled, certifies coverage over claim graphs rather than gating which extracted
  facts/bridges enter a symbolic KB; no decoys, no independent entrapment, no label-free knob. (Descoped to future comparison.)
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, now sharpened twice by review. Genomics/proteomics solved the hardest
  label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed
  FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry). That field ALSO discovered the
  two ways the trick breaks: (1) decoys 'too unrealistic to fool' the scorer make the FDR optimistic, cured by PROPERTY-MATCHED
  decoys (DeepCoy, protein-LM decoys); and (2) entrapment FDP must be estimated with a VALID upper bound - the combined/paired
  estimator of Wen et al. (Nature Methods 2025), NOT the naive sample ratio - and the entrapment set must be CONSTRUCTED DIFFERENTLY
  from the decoys, or their agreement proves nothing. I map all three onto the exact pressure point of a text-to-logic pipeline
  - the fuzzy-unification boundary where the LLM aligns predicates and supplies background knowledge - and import the matched-decoy
  cure, the valid combined entrapment estimator (with an explicit entrapment-to-target ratio r), and the construction-independence
  requirement specifically to defeat the anti-conservative failure: the dangerous hallucinations are PLAUSIBLE high-confidence
  false facts, so the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN
  THE TAIL (not on average), and the FDR must be corroborated by entrapment built unlike the decoys and arbitrated by a small
  gold probe. This turns the prompt's vague 'LLM as probabilistic reasoning engine for fuzzy unification' into a statistically
  disciplined, self-corroborated, label-free gate whose hallucination rate is a tunable, certified, auditable quantity.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's OWN prior over document-plausible-but-non-entailed
    content - a document-conditioned counterfactual the model finds plausible - so its confidence-score distribution reproduces
    that of genuine plausible hallucinations. This is the redesign that replaces random type-matched swaps, which are 'too
    easy' and make the estimated FDR optimistic (anti-conservative).
- term: Tail-conditioned win-rate (tail-aware ECA diagnostic)
  definition: >-
    The decoy-over-known-false-real win-rate computed ONLY among matched pairs whose scores fall ABOVE the operative admission
    cutoff, reported together with the decoy and false-real score CDFs as a function of score and an upper-tail two-sample
    test. Target ~0.5 in the tail. It supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative
    exactly where admissions occur. Used for measurement only, never by the operational gate.
- term: Combined / paired entrapment estimator and the ratio r
  definition: >-
    The VALID entrapment upper bound on realized false-admission: FDP_hat = N_E(1 + 1/r)/(N_T + N_E), where N_T = admitted
    real items, N_E = admitted entrapment items, and r = entrapment-to-target ratio (chosen and reported; e.g., r=1 for the
    tighter PAIRED form). It replaces the inherently-flawed naive 'sample' ratio (admitted-entrapment / admitted-total). r
    is propagated into the variance and the achievable-alpha floor.
- term: Independent entrapment and co-failure detection
  definition: >-
    Entrapment items are built by a mechanism DISTINCT from the decoy generator - foreign-document injection (foreign entities)
    and explicit document-contradiction - so their agreement with the LLM-counterfactual decoy FDR is evidential, not tautological.
    Because both are nonetheless LLM-handled, agreement is treated as NECESSARY not sufficient; the small gold probe is the
    arbiter, and any CO-FAILURE (entrapment+decoy agree but gold disagrees) is explicitly reported as the validity caveat.
- term: Equal Chance Assumption (tail exchangeability)
  definition: >-
    The validity condition inherited from target-decoy / knockoff theory: a genuinely-false real proposal and its matched
    decoy are equally likely to receive any given score, IN THE HIGH-SCORE TAIL where admissions occur. If decoys under-score
    the rare very-high-confidence plausible hallucinations, admitted decoys under-count admitted false reals and realized
    FDR exceeds target. We test it in the tail and validate it via independent entrapment rather than assume it.
- term: Per-document score normalization and group-wise control
  definition: >-
    Because raw LLM confidence scores need not be comparable across documents, scores are rank-normalized per document (or
    a per-document transform is fit) before pooling for corpus-aggregate target-decoy control - or a group-wise procedure
    respecting document structure is used - so a false real from an 'easy' document cannot spuriously out-rank decoys from
    a 'hard' one. Cross-document homogeneity is verified and a sensitivity analysis of the calibration diagonal to the normalization
    choice is reported.
- term: Corpus-aggregate FDR and the achievable-alpha floor
  definition: >-
    Control is asserted over candidates POOLED across documents within a dataset family (a single ~3000-char document yields
    too few candidates for stable control, with min non-trivial FDR ~1/(k+1) at k admissions and the knockoff+ '+1' offset).
    The achievable-alpha floor - the smallest target alpha reachable given candidate count AND the entrapment ratio r - is
    reported explicitly; per-document control is a secondary, high-variance quantity.
- term: Target-decoy competition / knockoff+ threshold
  definition: >-
    A label-free selection rule: rank reals and decoys by (per-document-normalized) score and choose the most permissive cutoff
    at which the decoy-estimated FDR ((admitted decoys + 1) / admitted reals) stays below alpha, applied separately to facts
    and bridges. Admitted items enter the KB with a certificate; the rest are rejected with their losing competition logged.
- term: Fuzzy unification and bridge rule
  definition: >-
    Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g.,
    'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic
    reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y))
    admitted only if it clears the decoy gate. Facts and bridges - NOT implicit common-sense rules - carry the headline FDR-control
    claim.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  We gate the fuzzy-unification boundary of a text-to-logic pipeline so every LLM-proposed fact and bridge rule must out-compete
  plausibility-matched counterfactual decoys (target-decoy / knockoff+ thresholding) before entering a Prolog knowledge base,
  controlling the corpus-aggregate hallucination rate to a user-specified target with NO labels; validity is tested in the
  high-score TAIL (not on average) and corroborated by an independently-constructed entrapment set scored through the VALID
  combined estimator FDP=N_E(1+1/r)/(N_T+N_E), with a small gold probe as arbiter. We predict this label-free gate matches
  or beats a plain confidence threshold and the label-using Mohri-Hashimoto conformal baseline on fact precision and hallucination
  at matched recall, and that a per-family/per-genre characterization of where tail-exchangeability holds is the publishable
  core even if full diagonal control is only partial.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_c769cf1156f4
overall_assessment: >-
  This is a strong, methodologically disciplined revision that addresses every critique from the previous round, in most cases
  thoroughly. The core idea — importing target-decoy/knockoff false-discovery-rate control with PLAUSIBILITY-MATCHED counterfactual
  decoys to gate the fuzzy-unification (fact + bridge) boundary of a text-to-logic pipeline, with no ground-truth labels —
  is a genuine, well-motivated Level-3 cross-domain transfer. My literature checks confirm the novelty is real: no indexed
  work applies competition-based FDR control with LLM-generated decoys to symbolic fact admission, and the closest adjacent
  methods (Mohri-Hashimoto conformal factuality, coherent factuality at ICLR 2025, Jin-Candes conformal selection, SelectLLM
  selective prediction) are correctly cited and differentiated. The revision fixes the four substantive issues from the prior
  review with precision: (i) it adopts the VALID combined entrapment estimator FDP_hat = N_E(1+1/r)/(N_T+N_E) from Wen et
  al. (Nature Methods 2025), drops the inherently-flawed naive sample ratio, introduces and propagates the entrapment-to-target
  ratio r, and reframes entrapment agreement as NECESSARY-not-sufficient with a gold arbiter and explicit co-failure detection;
  (ii) it makes the exchangeability diagnostic TAIL-aware (tail-conditioned win-rate among above-cutoff pairs + two-sample
  test of upper-tail CDFs) rather than marginal; (iii) it pre-registers a compute split (60% headline / 25% load-bearing baselines
  / 15% secondary), descopes the full bake-off and ProbLog/propagation arms, and cuts baselines to the two load-bearing comparisons
  (plain confidence threshold + Mohri-Hashimoto); (iv) it scopes the primary claim to facts + bridges, demotes implicit-rule
  gating to a separately-reported exploratory arm with a purpose-built gold set, and rank-normalizes scores per document before
  pooling with a sensitivity analysis. The honest 'contribution-survives-partial' clause is good scientific hygiene. The remaining
  concerns are execution-risk concerns, not design flaws: the tail focus (correctly adopted) is statistically data-hungry
  exactly where data is scarcest under a fixed sub-$10 budget; the achievable-alpha floor interacting with r may push the
  DEMONSTRABLE control regime above the practically interesting low-alpha range; and because LLM-counterfactual decoys carry
  no theoretical exchangeability guarantee (unlike Model-X knockoffs or shuffled-sequence decoys), the most likely outcome
  is a partial/per-genre characterization whose strength depends on whether it yields a predictive account rather than a pass/fail
  table. These are worth front-loading, but the design is sound and on track.
strengths:
- >-
  Genuine, verifiable novelty: target-decoy/knockoff+ FDR control with LLM-generated plausibility-matched counterfactual decoys,
  gating the neural-to-symbolic fact/bridge admission boundary, has not been done; the wedge over conformal methods (fully
  label-free operation, gating the interface rather than the output, symbolic propagation with per-leaf certificates) is precise
  and defensible.
- >-
  Exemplary responsiveness to prior review: the entrapment estimator is replaced with the correct Wen-et-al. combined/paired
  upper bound with explicit ratio r; the ECA diagnostic is made tail-conditioned; scope is pre-registered with an explicit
  budget split and descoping list; rule-gating is demoted to a clearly-labeled exploratory arm; per-document rank-normalization
  with a sensitivity analysis is added.
- >-
  Intellectual honesty about the crux: tail-exchangeability is treated as TESTED not assumed, entrapment agreement is framed
  as necessary-not-sufficient with gold as arbiter, co-failure is explicitly hunted for and reported, and the claim-chain
  dependency diagram localizes which result is contingent on which so downstream claims are not asserted when an upstream
  arrow breaks.
- >-
  Well-chosen, correctly-cited related work spanning the two relevant communities (knockoffs/target-decoy/property-matched
  decoys/entrapment in statistics+proteomics, and conformal factuality/selection in ML), with crisp differentiation from each.
- >-
  A de-risked fallback: a per-family, per-genre characterization of when tail-exchangeability and independent-entrapment agreement
  can be engineered is a publishable core even if no family achieves full diagonal tracking, so the iteration is unlikely
  to produce a wholly null outcome.
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The methodology is now technically sound: the correct entrapment estimator is adopted, the diagnostic is tail-aware, assumptions
    are stated and mostly tested rather than assumed, and the claim chain is explicitly localized. Two residual soundness
    risks keep this from a 4: (a) LLM-counterfactual decoys have no theoretical exchangeability guarantee, so validity rests
    entirely on empirical engineering of tail-exchangeability; and (b) the tail-conditioned diagnostics are statistically
    data-hungry under the fixed budget, risking an underpowered/uninterpretable headline.
  improvements:
  - >-
    WHAT: front-load a tail-specific power analysis. HOW: compute, before spending headline budget, how many above-cutoff
    matched pairs are needed for the upper-tail two-sample test and the tail-conditioned win-rate at the target alpha, and
    size the corpus to that (not to the marginal pool). WHY: the prior-review fix (tail-conditioning) is correct but multiplies
    sample requirements exactly where candidates are scarce; an underpowered tail test produces the 'uninterpretable null'
    the hypothesis itself names as the true-failure mode.
  - >-
    WHAT: state the no-theoretical-guarantee status explicitly and bound the claim. HOW: in the assumptions, contrast with
    Model-X knockoffs (exchangeability by construction) and shuffled-sequence proteomics decoys, and frame the FDR 'control'
    as an EMPIRICALLY-VALIDATED calibration rather than a proven guarantee. WHY: prevents over-claiming and pre-empts the
    strongest reviewer objection at a stats-aware venue.
- dimension: presentation
  score: 3
  justification: >-
    Much improved over the previous iteration: a crisp PRIMARY CLAIM, four enumerated independently-testable secondary claims
    (S1-S4), an explicit claim-chain dependency diagram, a clear scope/budget block, and a defined glossary. It reads far
    better than the previous single 250-word sentence. It is still very dense — most fields are long run-on sentences that
    interleave claim, caveat, and defensive response to prior review — which costs an ACL clarity reviewer real effort.
  improvements:
  - >-
    WHAT: tighten the prose further now that the structure is right. HOW: cap sentences, move the defensive 'we DROP the naive
    ratio / we DON'T assume X' asides into the assumptions block, and keep the hypothesis/summary fields to the claim itself.
    WHY: the genuine novelty is currently partly obscured by elaboration; a leaner statement raises the presentation/clarity
    score with near-zero risk.
  - >-
    WHAT: surface the achievable-alpha floor and the demonstrable-alpha range in the abstract/summary. HOW: one sentence stating
    the smallest alpha reachable given candidate count and r, so readers calibrate the 'control to user-specified alpha' claim
    immediately. WHY: avoids the impression of finer control than the design can demonstrate.
- dimension: contribution
  score: 3
  justification: >-
    A novel, well-motivated cross-domain transfer addressing a real and timely problem (label-free, auditable hallucination
    control at the text-to-logic interface), squarely on-target for the ACL Knowledge Extraction goal. The magnitude of the
    contribution is contingent: a clean positive result (diagonal tracking + matching/beating conformal with zero labels)
    would be a strong contribution, but the most probable outcome is partial, and the strength of the fallback depends on
    whether the characterization is predictive rather than descriptive.
  improvements:
  - >-
    WHAT: pre-commit to what elevates the fallback from a pass/fail table to a contribution. HOW: specify the predictive account
    you will deliver if full control fails — e.g., a model of which decoy-family x genre combinations achieve tail-exchangeability
    and WHY (document specificity, entity density, score-separation in the tail), validated out-of-sample on a held-out genre.
    WHY: turns the likely-partial outcome into a strong-accept-grade insight rather than a negative result.
  - >-
    WHAT: make the comparison to Mohri-Hashimoto a fair, interpretable contest. HOW: hold recall fixed via PR curves with
    bootstrap CIs (already planned) AND report the conformal baseline's guarantee status vs the decoy gate's empirical calibration
    side by side, so 'match or beat with zero labels' is not read as comparing a guarantee against an estimate. WHY: strengthens
    the headline S3 claim's credibility.
critiques:
- id: ''
  category: rigor
  severity: major
  description: >-
    The (correct) move to TAIL-conditioned exchangeability diagnostics introduces a statistical-power tension with the fixed
    sub-$10, CPU-only budget that is now the single biggest execution risk. The tail-conditioned win-rate is computed only
    among matched pairs scoring ABOVE the operative cutoff, and the two-sample test is on the UPPER tails of the score CDFs
    — both are, by construction, estimated from the sparse high-score region. With ~10-40 candidates per ~3000-char document
    and corpus-aggregate pooling, the number of above-cutoff matched pairs available for these tests can be small, so the
    headline decoy-family showdown (S1) and the calibration diagonal (primary criterion 1) risk being underpowered. The hypothesis
    itself names 'an uninterpretable null (control neither clearly holds nor clearly fails anywhere)' as the true failure
    mode, and an underpowered tail test is the most likely way to land there.
  suggested_action: >-
    Make the prospective power analysis TAIL-SPECIFIC, not marginal: estimate the number of above-cutoff matched pairs (and
    admitted items N_T, N_E) required to (a) detect a target departure of the tail win-rate from 0.5 and (b) power the upper-tail
    two-sample test at the operative alpha, then size the corpus to that target — including the per-genre split, since legal
    vs narrative must each be powered. Report the achievable-alpha floor jointly as a function of candidate count AND r so
    the demonstrable tail-region is explicit. If the budget cannot power both genres, pre-register narrowing to a single genre
    for the headline and treat the second as exploratory. Run a cheap pilot first (see the score-separation critique) to estimate
    tail density before committing the 60% headline allocation.
- id: ''
  category: methodology
  severity: major
  description: >-
    The achievable-alpha floor, now compounded by the entrapment ratio r, may exclude the practically meaningful low-alpha
    regime, weakening the 'trustworthy/auditable extraction' pitch even if control is demonstrated. With corpus pooling, the
    knockoff+ '+1' offset gives a minimum non-trivial FDR ~1/(k+1) at k admissions, and mixing in entrapment at ratio r further
    consumes admission slots and inflates the variance of FDP_hat. The combination can push the smallest demonstrable alpha
    well above the ~0.05-0.10 range a reader associates with 'trustworthy fact extraction.' If the design can only show diagonal
    tracking at, say, alpha ~ 0.2-0.3, the headline 'control to a user-specified target alpha' is technically true but operates
    in a coarse regime that materially undercuts the significance claim.
  suggested_action: >-
    Quantify and report the demonstrable alpha range up front (in the summary and success criteria), and bound the 'user-specified
    alpha' claim to that range rather than implying arbitrarily small alpha. To widen the usable range: (i) increase the pooled
    candidate count via more documents per genre (the cheapest lever given extraction is the dominant LLM cost); (ii) choose
    r to balance the entrapment-variance vs floor trade-off explicitly and report the chosen operating point; (iii) consider
    a less conservative competition-based bound (e.g., the FDP-bounding results in 'Bounding the FDP in competition-based
    control of the FDR', arXiv 2302.11837) as an alternative threshold rule and report whether it lowers the floor without
    breaking validity. Frame any success at coarse alpha honestly as a first demonstration.
- id: ''
  category: rigor
  severity: minor
  description: >-
    Validity rests entirely on empirically engineering tail-exchangeability, with no theoretical guarantee — unlike Model-X
    knockoffs (exchangeable by construction) or shuffled/reversed proteomics decoys (with a theoretical equal-chance argument).
    LLM-counterfactual decoys are generated from the same model whose hallucinations they are meant to mimic, so there is
    a real chance NO family achieves tail-exchangeable diagonal tracking on either genre. The hypothesis is honest about this
    and provides a survives-partial fallback, but the fallback as written ('counterfactual decoys pass on narrative but fail
    on legal text') is a descriptive pass/fail characterization, which is a weaker contribution than a top venue expects.
  suggested_action: >-
    Pre-commit to converting the likely-partial outcome into a PREDICTIVE account: specify in advance the document/score features
    hypothesized to govern tail-exchangeability (entity density, document specificity, tail score-separation, genre), fit
    a model that predicts which decoy-family x genre combinations achieve it, and validate it out-of-sample on a held-out
    genre. State this as an explicit secondary deliverable so the fallback is a mechanism-level insight rather than a results
    table.
- id: ''
  category: methodology
  severity: minor
  description: >-
    Verifying that plausibility-matched counterfactual decoys are genuinely NON-ENTAILED is close to the hard labeling problem
    the method aims to avoid, and contamination perturbs calibration. The more tail-matched (plausible) a counterfactual decoy
    is, the more likely it is actually entailed or world-true-and-inferable, in which case it is really a target masquerading
    as a decoy. Such contamination inflates the admitted-decoy count, biasing the decoy-FDR estimate conservative and costing
    recall, while the contamination check itself ('symbolic non-derivability + an LLM/human entailment audit') requires exactly
    the entailment judgments the label-free claim seeks to avoid.
  suggested_action: >-
    Report the contamination rate per decoy family and per genre, state the DIRECTION of its effect on the calibration diagonal
    (conservative vs anti-conservative), and quantify sensitivity of the diagonal to plausible contamination-rate values.
    Acknowledge that the non-entailment audit is a small label cost analogous to (and to be charged against) the conformal
    baseline's calibration-label budget, so the 'zero-label' wedge is stated precisely (zero labels for OPERATION; a small
    audit/probe budget for VALIDATION) rather than absolutely.
- id: ''
  category: evidence
  severity: minor
  description: >-
    The load-bearing assumption that the LLM emits a roughly monotone confidence/score separating document-entailed from non-entailed
    content IN THE TAIL is stated but not yet de-risked, despite well-documented unreliability of LLM verbalized confidence.
    If this separation fails in the high-score region, no thresholding procedure (decoy-gated, conformal, or otherwise) can
    succeed, and the entire headline budget would be spent confirming a negative that a cheap pilot could have surfaced first.
  suggested_action: >-
    Run a small, cheap pilot (a few dozen labeled items) BEFORE committing the headline budget: confirm the score separates
    entailed from non-entailed better than chance specifically in the upper tail, and pick the scoring elicitation (verbalized
    confidence vs logprob-derived vs self-consistency agreement) that best separates. Gate the full run on this pilot, and
    report the pilot as a methods precondition.
- id: ''
  category: clarity
  severity: minor
  description: >-
    Despite the strong structural refactor (primary claim + S1-S4 + dependency diagram + glossary), the proposal remains extremely
    dense: most fields are long run-on sentences that interleave the claim, its caveats, and point-by-point defensive responses
    to the previous review. This is comprehensive but taxing, and for an ACL submission the contribution risks being obscured
    by elaboration, costing the presentation/clarity score.
  suggested_action: >-
    Keep the hypothesis/summary fields to the claim itself; relocate the defensive asides ('we DROP the naive ratio', 'we
    do NOT assume X', 'NOT a marginal average') into the assumptions/method sections where they belong. Cap sentence length,
    and lead the summary with one plain-language sentence of the mechanism before the qualifications. Surface the achievable-alpha
    floor and the precise label-budget accounting early. This is polish, but it materially improves how the genuine novelty
    reads.
score: 6
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same decoy-gating/FDR frame; refines claims: tail-conditioning, valid estimator, scope cut to facts+bridges.
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

### [2] HUMAN-USER prompt · 2026-06-16 03:47:58 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-16 03:48:34 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
