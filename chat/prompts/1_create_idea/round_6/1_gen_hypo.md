# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 6 · `gen_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 04:12:40 UTC

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
  Label-Free FDR Control at the Text-to-Logic Admission Boundary via Plausibility-Matched Decoy Competition, with a Document-Level
  Predictive Model of When LLM Counterfactual Decoys Are Tail-Exchangeable
hypothesis: |-
  PLAIN MECHANISM. An LLM reads a short (~3000-char) document and proposes typed Prolog FACTS and fuzzy-unification BRIDGE rules (Horn clauses that align a document predicate to an ontology/target predicate when strict unification fails). Before any fact or bridge enters the knowledge base, it must out-score a plausibility-matched synthetic DECOY: a candidate the model itself finds plausible but the document does not entail. A target-decoy / knockoff+ rule then picks the most permissive admission cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha. The gate uses ZERO operation labels.

  CENTRAL CLAIM. Realized FDR tracks target alpha (a calibration diagonal) within a stated demonstrable-alpha regime, BUT ONLY where decoys are exchangeable with realized hallucinations in the high-score TAIL where admissions happen. Unlike Model-X knockoffs or shuffled-peptide decoys, LLM counterfactual decoys carry no construction-level exchangeability guarantee. We therefore (a) state the result as an empirically-validated calibration, not a theorem, and (b) make the de-risked deliverable a DOCUMENT-LEVEL predictive model of WHEN tail-exchangeability holds.

  THREE LOAD-BEARING NUMBERS (stated once, up front).
    - Demonstrable-alpha range: roughly alpha in [0.05, 0.5]. The knockoff+ '+1' offset gives a minimum estimable FDR ~1/k at k admissions; the Phase-0 pilot refines this per genre.
    - Corpus & cost: <=300 confirmatory documents (CLUTRR, free deterministic gold) + <=60 illustrative realistic documents; ~3,000-5,000 LLM calls, ~4-6M tokens; projected ~$2-5 on a sub-$0.50/M-token model; HARD STOP at $10.
    - Label budget: ZERO labels for operation (the gate is label-free); a small audit/probe charged ONLY to validation, accounted symmetrically against the conformal baseline's calibration labels.

  CLAIM CHAIN (each row independently testable; a break is localized and reported, it does not silently propagate downstream).
    S1 DECOY SIGNATURE (mechanism) | TEST: tail-conditioned win-rate among above-cutoff matched pairs (target ~0.5) + upper-tail two-sample CDF test | PASS: counterfactual decoys ~0.5, random type-matched swaps measurably anti-conservative | ON FAIL: family reported as anti-conservative.
    S2 ENTRAPMENT CORROBORATION (necessary, not sufficient) | TEST: independently-constructed, TAIL-MATCHED entrapment yields combined bound FDP_hat = N_E(1+1/r)/(N_T+N_E) that agrees with decoy-FDR and gold; entrapment must pass its OWN tail-difficulty diagnostic | PASS: agreement + entrapment not materially easier than gold false-reals in the tail | ON FAIL: entrapment flagged anti-conservative; co-failure (entrapment+decoy agree, gold disagrees) reported.
    S3 WEDGE OVER CONFORMAL | TEST: matched-recall PR curves with bootstrap CIs vs (i) plain confidence threshold and (ii) labeled Mohri-Hashimoto conformal factuality | PASS: decoy-gating matches/beats both on atomic-fact precision and hallucinated-conclusion rate, with zero-label operation as the wedge | ON FAIL: reported as no advantage.
    S4 DOCUMENT-LEVEL PREDICTIVE ACCOUNT (de-risked headline) | TEST: predict per-document/per-item tail-exchangeability gap from document+score features; leave-one-document-cluster-out CV (many held-out units) | PASS: out-of-sample predictive of where the calibration holds | ON FAIL: reported with the genre-holdout probe as a single-unit external check.
    S5 PREDICTABLE PROPAGATION (preliminary) | TEST: tightening alpha lowers multi-hop hallucinated-conclusion rate per a fitted proof-structure model | PASS: direction+rough magnitude match | ON FAIL: reported as preliminary.

  PRE-REGISTERED CONFIRMATORY CELL (anti-cherry-pick). The single confirmatory test is the ONE cell (counterfactual-decoy family, CLUTRR, demonstrable-alpha grid). All other family x genre x alpha cells are exploratory; a Benjamini-Hochberg multiplicity correction is applied across the family of validation tests and reported. 'At least one family passes' is NOT a confirmatory criterion.

  SCOPE. Facts AND bridges on CLUTRR (paraphrased multi-hop kinship) carry the confirmatory headline because gold is free and bridge truth is crisp under kinship canonicalization. The hand-annotated realistic set (legal clauses / news briefs / kids' stories) is an illustrative external probe with a published annotation guideline and reported inter-annotator agreement. Defeasible bridges are OUT of the headline (exploratory). Implicit common-sense RULE gating, ProbLog/isotonic, TDC-SB/UB and '+1'-removal floor-relaxation, and S5 are preliminary / if-budget-permits.
motivation: |-
  Text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob there: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and catches only encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, multiple-testing hallucination detection, coherent factuality) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem -- selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth -- via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound built INDEPENDENTLY of the decoys. We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary, turning 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity -- directly serving the ACL Knowledge Extraction goal of trustworthy, traceable extraction.

  Why it matters even at a coarse alpha: NO existing label-free method offers ANY FDR knob at the fuzzy-unification interface. A first, auditable, zero-operation-label control -- even at alpha ~0.1 -- is a useful and novel capability, because it converts an uncontrolled hallucination channel into a tunable one with per-leaf certificates. And because LLM decoys carry no theoretical guarantee, the most probable outcome is partial control; we therefore pre-commit to a DOCUMENT-LEVEL predictive model (S4) of where the calibration holds, validated across many held-out document clusters. That converts the likely-partial result from a pass/fail table into a generalizable mechanism-level insight that survives even if full diagonal control does not.
assumptions:
- >-
  TAIL EXCHANGEABILITY IS ENGINEERED AND TESTED, NOT GUARANTEED. Target-decoy / knockoff+ validity needs a genuinely-false
  real proposal and its matched decoy to be equally likely to receive any given score in the high-score region near the cutoff.
  LLM counterfactual decoys have no construction-level proof of this. We therefore report an empirically-validated calibration
  (not a theorem); test the condition in the TAIL (tail-conditioned win-rate ~0.5 among above-cutoff pairs plus an upper-tail
  two-sample CDF test, not a marginal average); corroborate label-free via independent tail-matched entrapment; arbitrate
  with a small gold probe; and report per family and per genre where it holds or fails anti-conservatively.
- >-
  A SCORE-SEPARATION PRECONDITION MUST BE MET, AND IS DE-RISKED BY A PILOT. The LLM must emit a roughly monotone score that
  separates document-entailed from non-entailed content better than chance SPECIFICALLY in the upper tail; verbalized confidence
  is documented to be overconfident exactly there, so we do not assume it. A Phase-0 pilot (a few dozen labeled items) verifies
  tail separation and selects the best elicitation among verbalized confidence, logprob-derived, self-consistency agreement,
  and DINCO-style distractor-normalized confidence. The headline budget is gated on the pilot; if no elicitation separates
  in the tail, that is the reported methods-level result.
- >-
  ENTRAPMENT MUST BE INDEPENDENT, VALID-ESTIMATOR-BASED, AND TAIL-MATCHED. Realized false-admission is bounded by FDP_hat
  = N_E(1+1/r)/(N_T+N_E) (paired form at r=1), never the flawed naive 'sample' ratio; r is reported and propagated into variance
  and the alpha-floor. Entrapment is generated by a mechanism distinct from the decoys (in-genre cross-document swaps, numeric/temporal
  perturbation, explicit contradiction) so agreement is evidential, not tautological. CRUCIALLY, entrapment inherits the same
  'too-easy -> anti-conservative' risk as decoys: if admitted-entrapment tail scores are materially easier than gold false-reals,
  N_E under-counts and FDP_hat under-estimates true FDP. We therefore run a tail-difficulty diagnostic on entrapment too and
  report any easier-in-the-tail entrapment as an invalid (anti-conservative) corroborator, stating the bias direction.
- >-
  THE DEMONSTRABLE-ALPHA REGIME IS BOUNDED AND CORPUS-AGGREGATE. A single ~3000-char document yields only ~10-40 candidates,
  so control is asserted over candidates pooled across documents within a dataset family. The '+1' offset gives a minimum
  estimable FDR ~1/k at k admissions; entrapment at ratio r inflates estimator variance; so the smallest demonstrable alpha
  is a joint function of pooled candidate count and r, reported up front (roughly [0.05, 0.5]). We widen it mainly by adding
  documents (the cheapest lever) and, if budget permits, by less-conservative bounds (TDC-SB/UB; the '+1'-removal analysis).
  Raw LLM scores need not be comparable across documents, so scores are rank-normalized per document before pooling, with
  a sensitivity check of the diagonal to the normalization choice.
- >-
  BRIDGE TRUTH IS DEFINED CRISPLY ON CLUTRR; DEFEASIBLE BRIDGES ARE OUT OF THE HEADLINE. A bridge maps a document predicate
  to a target predicate (author_of(X,Y) :- wrote(X,Y)). On CLUTRR a bridge is TRUE iff its predicate mapping is valid under
  the deterministic kinship algebra for all consistent instantiations (gold-checkable, free); FALSE otherwise; a bridge decoy
  is NON-ENTAILED iff its mapping is not licensed by the document plus ontology typing; bridge-decoy CONTAMINATION (a decoy
  that is actually a valid mapping) is audited symbolically against the kinship algebra. On the realistic set, many bridges
  are defeasible (usually-true-with-exceptions); these get a three-way gold label (universally-valid / document-licensed /
  invalid) and are EXPLORATORY only. The headline bridge claim lives on CLUTRR where truth is unambiguous. Decoy non-entailment
  is imperfect: a decoy that is actually entailed inflates the admitted-decoy count and biases the FDR estimate CONSERVATIVE
  (the safe direction); contamination rate is reported per family/genre with a diagonal sensitivity analysis.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then make TAIL exchangeability, the demonstrable-alpha regime, and the DOCUMENT-LEVEL predictive account the central experimental objects. Budget split of $10 / CPU-only: ~10% Phase-0 pilot (gates everything); ~55% confirmatory headline (one pre-registered cell + decoy showdown + tail-matched entrapment + calibration diagonal on facts+bridges over CLUTRR); ~20% load-bearing baselines (plain confidence threshold + Mohri-Hashimoto conformal factuality); ~15% secondary/preliminary (S4 modeling on the realistic set, S5 propagation, exploratory rule gating, ProbLog/isotonic, TDC-SB/UB floor-relaxation).

  FEASIBILITY BUDGET (published before committing). Extraction ~300 calls; decoy generation ~300 calls; joint scoring of reals+decoys+entrapment, batched ~3 calls/doc, ~900 calls; pilot ~550 calls (includes self-consistency and DINCO-style elicitations); conformal baseline back-off ~300 calls; realistic-set probe ~360 calls. Total ~2,700-3,400 confirmatory calls (+retries), ~4-6M tokens, projected ~$2-5 on a sub-$0.50/M model. Cumulative cost is logged after every call; the run hard-stops at $10. CLUTRR carries the confirmatory headline precisely because its gold is FREE, removing the unbudgeted-annotation bottleneck.

  HAND-ANNOTATED REALISTIC SET (reproducibility-critical, illustrative). ~60 short professionally-written public-domain/CC documents across legal clauses, news briefs, and kids' stories. A published guideline defines atomic-fact gold and the three-way bridge label. Two annotators label an overlapping subset; we report Cohen's kappa / inter-annotator agreement. This set is the external probe, not the confirmatory unit.

  PHASE 0 -- PILOT (precondition). On a few dozen labeled items: (i) measure which elicitation (verbalized, logprob-derived, self-consistency, DINCO-style distractor-normalized) separates entailed from non-entailed content better than chance IN THE UPPER TAIL; pick the best. (ii) Estimate tail density and run a tail-specific power analysis: how many above-cutoff matched pairs and admitted N_T, N_E are needed to detect a tail win-rate departure from 0.5 and power the upper-tail two-sample test at the operative alpha. Size the corpus to that target. Gate the full run; report the pilot as a methods precondition.

  PIPELINE. (1) EXTRACTION: a cheap OpenRouter LLM proposes typed first-order facts; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing, not as trusted constraints. (2) DECOY GENERATION: PRIMARY family = document-conditioned counterfactual decoys (fabricate maximally-plausible, non-entailed facts/bridges conditioned on document+types); the deliberately-easy random type-matched swap family is retained as the predicted-anti-conservative baseline. Every decoy passes a non-entailment check (symbolic non-derivability + sampled entailment audit); contamination rate and its conservative direction are reported. (3) ENTRAPMENT (independent + tail-matched): an in-genre cross-document-swap / numeric-temporal-perturbation / explicit-contradiction set, false by construction, mixed at a reported ratio r; entrapment is designed to be plausible/tail-matched and its tail-difficulty is diagnosed (see below). (4) SCORING: reals, decoys, entrapment scored jointly in batched prompts using the pilot-selected elicitation; scores rank-normalized per document. (5) FDR GATE: knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges; admitted items enter the KB with a logged certificate. (6) ENTRAPMENT VALIDATION: the combined estimator upper-bounds realized false-admission; we compare against decoy-FDR and gold and explicitly hunt co-failures. (7) TAIL DIAGNOSTICS (measurement only, never used by the gate): for BOTH decoys and entrapment, report the above-cutoff score distribution vs gold false-reals plus the win-rate and upper-tail two-sample test; entrapment materially easier in the tail is flagged anti-conservative. (8) REASONING: admitted facts/bridges populate SWI-Prolog for crisp multi-hop deduction; backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted bridge) plus the decoy + entrapment certificate.

  S4 DOCUMENT-LEVEL VALIDATION (the de-risk, made powerable). Define a per-document (or per-small-cluster) tail-exchangeability gap: among above-cutoff matched pairs in that document, the gold-arbitrated departure of realized false-admission from target. Fit a model predicting this gap from document features (entity density, document specificity, tail score-separation, genre-as-a-feature) and validate with leave-one-document-cluster-out cross-validation -- MANY held-out units, powered primarily on CLUTRR where gold is free. The leave-one-genre-out result is reported as ONE illustrative external probe, explicitly a single-unit generalization check, not the validation.

  EXPERIMENTS. (a) Validity-of-control: sweep alpha within the demonstrable range on the pre-registered confirmatory cell; measure realized FDR via gold and the entrapment combined estimator; test diagonal tracking above the floor; report normalization sensitivity. (b) Decoy-family showdown + entrapment tail-difficulty per family. (c) Matched-recall PR curves vs the two baselines with guarantee status side by side. (d) S4 document-level LOO-CV. (e) [preliminary] S5 propagation, exploratory rule gating, ProbLog/isotonic, floor-relaxation. (f) Cost check (<$10, CPU-only) + auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). The Phase-0 pilot must show the selected score separates entailed from non-entailed content better than chance in the upper tail AND that the corpus can power the tail tests. If the pilot fails, the reported contribution is the precondition-failure analysis plus the document-level S4 model.

  PRIMARY (the single pre-registered confirmatory cell: counterfactual-decoy family, CLUTRR, demonstrable-alpha grid; facts AND bridges). CONFIRMED if: (1) realized corpus-aggregate FDR tracks target alpha within a small tolerance above the achievable floor (calibration diagonal), stable under the per-document normalization check, AND the independent tail-matched entrapment combined-estimator bound agrees with both the decoy estimate and gold -- self-corroborated, label-free control; (2) the decoy showdown shows the tail signature -- counterfactual decoys reach tail-conditioned win-rate ~0.5 and pass the upper-tail two-sample test, while random swaps are measurably anti-conservative, AND entrapment passes its own tail-difficulty diagnostic; (3) at matched recall (PR curves with CIs), decoy-gating matches or beats a plain confidence threshold AND the Mohri-Hashimoto conformal baseline at a small matched label budget on fact precision and hallucinated-conclusion rate, with zero-label operation as the wedge. A BH multiplicity correction is applied across all validation tests and reported; non-confirmatory cells are exploratory.

  CONTRIBUTION-SURVIVES-PARTIAL (the de-risk, now powerable). Even if the diagonal does not fully track, the reportable headline is the DOCUMENT-LEVEL S4 model: which document/score features govern tail-exchangeability, fit and validated by leave-one-document-cluster-out CV across many held-out units (powered on CLUTRR's free gold), plus documented co-failure cases. The bar is out-of-sample document-level prediction, not a pass/fail table; the genre-holdout is one illustrative probe only.

  SECONDARY / PRELIMINARY. (4) S5 -- tightening alpha reduces multi-hop hallucination in the predicted direction; (5) ablating the decoy gate measurably worsens hallucination; (6) exploratory rule-gating separates correct from plausible-but-wrong implicit rules above chance; (7) the pipeline runs on commodity CPU within $10 and produces auditable trace-graphs with per-leaf certificates.

  DISCONFIRMED if: the pilot preconditions hold (so the test is fair) but on the pre-registered confirmatory cell the counterfactual-decoy family is anti-conservative in the tail AND the entrapment estimator co-fails against gold AND the document-level S4 model fails out-of-sample (no document feature predicts the exchangeability gap); OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall and is dominated by conformal even accounting for its zero-label disadvantage. A characterized failure boundary plus a validated S4 model remains a contribution; an uninterpretable null (control neither clearly holds nor clearly fails, underpowered tail test) is the true failure, which the Phase-0 power analysis is designed to prevent.
related_works:
- >-
  Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis
  using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench): gives the theory of entrapment FDP estimation, shows the
  naive 'sample' estimator is flawed, and provides the valid combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E) (tighter
  paired form at r=1). We adopt this estimator, choose and report r, and propagate r into variance and the alpha-floor. Difference:
  their domain is peptide identification; we transplant the estimator AND construction-independence to validate LLM fact/bridge
  admission, and we ADD a tail-difficulty diagnostic for entrapment (their entrapment validity rests on different domain assumptions).
- >-
  Barber & Candes, knockoff filter (Annals of Statistics 2015) and Candes et al., Model-X knockoffs (2018), plus target-decoy
  competition in proteomics: select true signals among many candidates with guaranteed FDR by competing each real variable/peptide
  against a synthetic negative control that is exchangeable BY CONSTRUCTION. Difference: this machinery lives in numeric feature
  selection and mass spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM neuro-symbolic
  boundary where decoys carry NO such guarantee, so we test exchangeability empirically in the high-score tail and model where
  it holds.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using
  deep learning', Bioinformatics 2021; protein-language-model decoys): generate decoys that reproduce the score properties
  of true positives so target-decoy FDR is well-calibrated. Difference: lives in molecular screening / mass spectrometry;
  we import the PRINCIPLE -- decoys must reproduce the false-positive score distribution, not be 'too easy' -- to design LLM
  fact/bridge decoys as document-conditioned counterfactuals, never done for LLM-proposed symbolic assertions.
- >-
  Li, Magesh & Veeravalli, 'Principled Detection of Hallucinations in Large Language Models via Multiple Testing' (arXiv 2508.18473,
  2025): formulates hallucination detection as hypothesis testing and aggregates multiple evaluation scores via conformal
  p-values to detect hallucinated OUTPUTS with a controlled false-alarm rate. The closest recent FDR-for-hallucination neighbor.
  Difference along four axes: (i) it needs a reference/calibration distribution and certifies the generated answer, we are
  label-free for operation and gate the neuro-symbolic ADMISSION boundary; (ii) BH-on-conformal-p-values vs target-decoy/knockoff
  competition; (iii) no decoys, no independent entrapment corroboration; (iv) no symbolic propagation or per-leaf certificates.
  Its label/reference requirement strengthens, not weakens, our label-free wedge.
- >-
  Wang et al., 'Calibrating Verbalized Confidence with Self-Generated Distractors' (DINCO, arXiv 2509.25532 / OpenReview pZs4hhemXc,
  2025): a zero-resource method that normalizes an LLM's verbalized confidence for a claim by the total confidence over self-generated
  distractor claims (weighted by uniqueness and counterfactuality), reducing overconfidence on short- and long-form generation.
  Difference: DINCO produces a better-calibrated SCALAR confidence for a single claim; it has no FDR control, no admission
  threshold, and no exchangeability/competition argument. We use DINCO-style distractor-normalized confidence as a CANDIDATE
  elicitation in the Phase-0 pilot (it may give better tail separation); our contribution is the target-decoy competition
  and label-free FDR gate built on whichever elicitation wins.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes
  claims until a user-specified factuality alpha is met via conformal prediction with a few labeled samples. Our primary load-bearing
  baseline. Difference: it requires labeled calibration, certifies the final filtered OUTPUT rather than the admission boundary,
  and offers no synthetic-decoy mechanism, independent entrapment, or symbolic propagation with certificates. We report its
  finite-sample guarantee vs our empirical calibration side by side; our wedge is label-free OPERATION at the fuzzy-unification
  interface.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no operation labels by competing each proposal against engineered
  decoys and corroborate via independent tail-matched entrapment.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023; TDC-SB/UB)
  and He, Ebadi, Keich et al., 'Controlling the FDR via competition: is the +1 needed?' (arXiv 2204.13248 / Stat. & Prob.
  Letters 2023): tighter FDP bounds and analysis of the '+1' correction that creates the minimum-estimable-FDR floor. We test
  (if budget permits) whether these lower our achievable-alpha floor without breaking validity. Difference: developed for
  generic competition-based selection / mass spectrometry; we apply them to widen the demonstrable-alpha regime at the text-to-logic
  interface.
- >-
  Conformal factuality for reasoning chains, 'Conformal Language Model Reasoning with Coherent Factuality' (ICLR 2025 / arXiv
  2505.17126): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning
  chains, with a labeled calibration set. Difference: labeled, certifies coverage over claim graphs rather than gating which
  extracted facts/bridges enter a symbolic KB; no decoys, no independent entrapment, no label-free knob.
- >-
  LINC (Olausson et al., EMNLP 2023) and Logic-LM (Pan et al., Findings of EMNLP 2023): LLM semantic-parse premises into FOL/symbolic
  form executed by a solver, with majority voting (LINC) or solver-error self-refinement (Logic-LM). Difference: no principled
  control over WHICH extracted content is admitted -- a syntactically valid fabricated premise is never challenged; voting
  smooths variance and refinement fixes solver/syntax errors only. No FDR knob, no decoys, no label-free precision guarantee.
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including
  where the ontology is silent -- complementary.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, sharpened across review rounds. Genomics/proteomics solved the hardest
  label-poor problem -- deciding which of thousands of candidate signals are real with no ground truth -- with a guaranteed
  FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry), and discovered the two ways the
  trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys: DeepCoy,
  protein-LM decoys), and entrapment FDP must be estimated with a valid upper bound (Wen et al., Nature Methods 2025) using
  entrapment built unlike the decoys. I map all three onto the exact pressure point of a text-to-logic pipeline -- the fuzzy-unification
  boundary where the LLM aligns predicates and supplies background knowledge. Because the dangerous hallucinations are PLAUSIBLE
  high-confidence false facts, the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must
  be checked IN THE TAIL, and the FDR must be corroborated by independently-constructed, TAIL-MATCHED entrapment and arbitrated
  by a small gold probe. The latest refinements: entrapment now gets its own tail-difficulty diagnostic (the same 'too-easy'
  failure mode the decoys are guarded against); the predictive account of WHEN the calibration holds is re-based on the DOCUMENT
  (many held-out units) rather than the genre (n=1); and bridge truth is defined crisply on CLUTRR's kinship canonicalization.
  A separate nod: DINCO's self-generated distractors (used elsewhere to normalize confidence) become a candidate pilot elicitation
  -- but our novelty is the competition-based, label-free FDR gate, not the confidence score itself. The transfer is honest
  about its weakest joint: LLM decoys carry no construction-level exchangeability guarantee, so the contribution is an empirically-validated
  calibration PLUS a document-level predictive account of when it holds -- a mechanism-level insight rather than a bare control
  claim.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content -- a document-conditioned counterfactual -- so its score distribution reproduces that of genuine plausible hallucinations.
    It replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Tail-conditioned win-rate (tail diagnostic)
  definition: >-
    The win-rate of a decoy (or entrapment item) over a known-false real, computed ONLY among matched pairs scoring above
    the operative admission cutoff, reported with the score CDFs and an upper-tail two-sample test. Target ~0.5 in the tail.
    It supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative exactly where admissions
    occur. Measurement only, never used by the gate.
- term: Entrapment tail-difficulty diagnostic
  definition: >-
    A symmetric check applied to the entrapment set: the admitted-entrapment score distribution is compared to gold false-reals
    in the high-score region. If entrapment is materially easier to reject in the tail, its admitted count N_E under-represents
    realized false admissions and the combined estimator UNDER-estimates true FDP (anti-conservative). Such entrapment is
    reported as an invalid corroborator, with the bias direction stated.
- term: Combined / paired entrapment estimator and the ratio r
  definition: >-
    The valid entrapment upper bound on false-admission: FDP_hat = N_E(1+1/r)/(N_T+N_E), where N_T = admitted reals, N_E =
    admitted entrapment, r = entrapment-to-target ratio (reported; r=1 gives the tighter paired form). It replaces the flawed
    naive 'sample' ratio; r is propagated into the variance and the achievable-alpha floor.
- term: Independent + tail-matched entrapment
  definition: >-
    Entrapment built by a mechanism distinct from the decoy generator (in-genre cross-document swaps, numeric/temporal perturbation,
    explicit contradiction) AND designed to be plausible/tail-matched, so its agreement with the decoy FDR is evidential rather
    than tautological and is not anti-conservative through being too easy. Agreement is necessary, never sufficient; the small
    gold probe is the arbiter, and any co-failure is reported.
- term: Document-level predictive exchangeability account (S4)
  definition: >-
    A model that predicts the per-document/per-item tail-exchangeability gap (gold-arbitrated departure of realized false-admission
    from target among above-cutoff pairs) from document/score features (entity density, specificity, tail score-separation,
    genre-as-feature), validated by leave-one-document-cluster-out cross-validation across MANY held-out units (powered on
    CLUTRR's free gold). The leave-one-genre-out result is one illustrative external probe, not the validation.
- term: Demonstrable-alpha range and achievable-alpha floor
  definition: >-
    Control is asserted over candidates pooled across documents within a dataset family. The knockoff+ '+1' offset gives a
    minimum estimable FDR ~1/k at k admitted items, and entrapment at ratio r inflates estimator variance, so the smallest
    demonstrable target alpha is a joint function of pooled candidate count and r (roughly [0.05, 0.5], refined by the pilot).
    It is widened mainly by adding documents and optionally by less-conservative bounds (TDC-SB/UB).
- term: Bridge truth on CLUTRR (and defeasible exclusion)
  definition: >-
    A bridge (author_of(X,Y) :- wrote(X,Y)) is a universally-quantified Horn clause. On CLUTRR it is TRUE iff its predicate
    mapping is valid under the deterministic kinship algebra for all consistent instantiations (gold-checkable); FALSE otherwise.
    A bridge decoy is NON-ENTAILED iff its mapping is not licensed by the document plus typing; contamination is audited symbolically.
    Defeasible bridges (usually-true-with-exceptions) get a three-way realistic-set label (universally-valid / document-licensed
    / invalid) and are EXPLORATORY only; the confirmatory bridge claim lives on CLUTRR.
- term: Pre-registered confirmatory cell and multiplicity correction
  definition: >-
    The single (decoy family, genre, alpha-grid) combination -- counterfactual decoys on CLUTRR over the demonstrable-alpha
    grid -- that constitutes the confirmatory test. All other family x genre x alpha cells are exploratory, and a Benjamini-Hochberg
    correction is applied across the family of validation tests so 'at least one family passes' cannot be read as post-hoc
    cherry-picking.
- term: Fuzzy unification and bridge rule
  definition: >-
    Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails. It
    is the chief site where hallucination enters a text-to-logic reasoner. Each fuzzy match is materialized as an explicit,
    auditable Horn-clause BRIDGE admitted only if it clears the decoy gate. Facts and bridges -- not implicit common-sense
    rules -- carry the headline FDR-control claim.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  Every LLM-proposed fact and fuzzy-unification bridge rule must out-score a plausibility-matched counterfactual decoy in
  a target-decoy / knockoff+ competition before entering a Prolog knowledge base, controlling the corpus-aggregate hallucination
  rate to a target alpha with zero operation labels, within an explicitly reported demonstrable-alpha range. A Phase-0 pilot
  first verifies tail score-separation; validity is tested in the high-score TAIL and corroborated by an independently-constructed,
  tail-matched entrapment set via the valid combined estimator FDP=N_E(1+1/r)/(N_T+N_E), with a small gold probe as arbiter;
  and because LLM decoys carry no theoretical exchangeability guarantee, the de-risked deliverable is a DOCUMENT-LEVEL predictive
  model (leave-one-cluster-out) of which documents achieve tail-exchangeability.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_62cb4972b7b9
overall_assessment: >-
  This is a mature, intellectually honest revision that addresses all four MAJOR critiques from the previous round well: the
  S4 validation unit is moved from genre (n=1) to document/cluster; a symmetric tail-difficulty diagnostic is added for entrapment;
  bridge truth is defined crisply on CLUTRR's kinship algebra with defeasible bridges descoped to exploratory; a concrete
  feasibility budget with a hard stop is published; the confirmatory cell is pre-registered with a BH multiplicity correction;
  and the missing related work (arXiv 2508.18473, DINCO) is cited and differentiated. The core idea — a label-free, target-decoy
  / knockoff+ FDR gate at the fuzzy-unification boundary of a text-to-logic pipeline, with plausibility-matched LLM counterfactual
  decoys, an independent valid entrapment estimator, and a document-level predictive account of when the calibration holds
  — is genuinely novel; my searches found no prior work combining competition-based FDR control with the LLM neuro-symbolic
  admission boundary, and the closest neighbors are cited and correctly differentiated. The honest reframing as an empirically-validated
  calibration (not a theorem) plus a predictive de-risk is a strength rather than a weakness. However, three of the revision's
  own fixes create or sharpen genuine, addressable concerns that now gate the score: (1) the document-level S4 de-risk — the
  deliverable meant to survive a partial confirmatory outcome — is itself likely underpowered/ill-posed precisely on CLUTRR,
  the dataset chosen to power it, because CLUTRR documents are near-homogeneous in the very features S4 must predict from
  and yield few per-document admissions at a meaningful alpha; (2) scoping the confirmatory headline to CLUTRR risks demonstrating
  the mechanism where it matters least, since CLUTRR's closed kinship vocabulary is exactly where 'plausible high-confidence
  false facts' and genuine fuzzy-unification bridges are weakest, while the realistic set that motivates the work is demoted
  to an underpowered probe; (3) knockoff+ validity rests on a null sign-flip property that within-document score correlation
  and the cost-driven joint/batched scoring can break in an anti-conservative direction that the design would mis-attribute
  to decoy non-exchangeability. None is fatal; each is addressable in one iteration. The trajectory is strongly positive —
  borderline accept, with a clear path to a 6-7 once the S4-powerability, external-validity, and scoring-dependence issues
  are resolved.
strengths:
- >-
  Exceptional intellectual honesty about the weakest joint: the proposal openly states that LLM counterfactual decoys carry
  NO construction-level exchangeability guarantee (unlike Model-X knockoffs or shuffled-peptide decoys), reframes the result
  as an empirically-validated calibration rather than a theorem, and makes 'when does it hold' the central scientific object.
  This candor is rare and is the right scientific posture for a cross-domain transfer.
- >-
  Genuinely novel cross-domain transfer. The combination — label-free target-decoy/knockoff+ competition with plausibility-matched
  LLM decoys, a valid combined entrapment estimator FDP_hat=N_E(1+1/r)/(N_T+N_E), and per-leaf certificates at the text-to-logic
  admission boundary — does not appear in prior work; the related-work section correctly differentiates Mohri-Hashimoto, Jin-Candes,
  Li et al. (2508.18473), DINCO, DeepCoy, and the FDRBench entrapment theory along the right axes (labeled-vs-label-free,
  output-certification-vs-admission-gating, BH-on-conformal-p-values-vs-competition).
- >-
  Strong methodological rigor for a pre-experiment proposal: a pre-registered single confirmatory cell, an explicit BH multiplicity
  correction across validation tests, a Phase-0 power-analysis gate, per-document rank-normalization with a sensitivity check,
  and a tail-conditioned (not marginal) win-rate diagnostic — directly defusing the cherry-picking risk that is especially
  ironic for an FDR paper.
- >-
  Symmetric tail-difficulty diagnostic for the entrapment corroborator (the prior round's gap), with the bias direction stated
  and 'too-easy' entrapment pre-registered as an invalid/anti-conservative corroborator.
- >-
  Crisp, gold-checkable bridge-truth semantics on CLUTRR via the deterministic kinship algebra, with contamination's conservative
  bias direction characterized — resolving the prior under-definition of the bridge half of the headline.
- >-
  A concrete, published feasibility budget (~2,700-3,400 calls, ~4-6M tokens, ~$2-5, hard stop at $10) and a clear operation-vs-validation
  label accounting, making the resource claim auditable up front.
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The statistical transplant is careful and honest: the valid combined estimator is used (not the flawed naive ratio), the
    demonstrable-alpha floor and its 1/k origin are stated, tail diagnostics are conditioned where admissions occur, and the
    result is correctly framed as calibration not theorem. Held from 4 by (a) the core exchangeability gap being acknowledged
    but unmodeled at the level of within-document sign dependence, which the cost-driven batched scoring can worsen anti-conservatively;
    and (b) the S4 de-risk being likely underpowered on the dataset chosen to power it.
  improvements:
  - >-
    State explicitly which dependence/exchangeability conditions the knockoff+ guarantee requires (null sign-flip property)
    and name within-document score correlation as a risk to pooled-sign independence; add a per-document block structure to
    the FDP variance rather than treating pooled signs as i.i.d.
  - >-
    Score each real/decoy/entrapment item (or matched pair) with provenance blinded and order randomized, avoiding within-batch
    contrast effects; report a sensitivity check of the calibration diagonal to isolated-vs-batched scoring so an anti-conservative
    artifact is not mis-read as decoy non-exchangeability.
  - >-
    Report, from the pilot, the actual per-document admitted-count at the operative alpha and the cross-document variance
    of the S4 features on CLUTRR, so the powerability of the de-risk is demonstrated rather than assumed.
- dimension: presentation
  score: 2
  justification: >-
    Improved by surfacing the three load-bearing numbers up front and by the S1-S5 claim-chain structure, but the prose is
    still long, defensive run-ons that interleave claim, caveat, and point-by-point rebuttal to prior reviews. This was flagged
    in two prior rounds; it still obscures the genuine novelty and would cost the ACL presentation score.
  improvements:
  - >-
    Lead each major field (hypothesis, summary, each assumption) with ONE plain sentence of the mechanism/claim before any
    qualifier; move rebuttals and caveats into assumptions/method.
  - >-
    Render the S1-S5 claim chain as an actual table with columns (claim | test | pass criterion | what-is-reported-on-failure)
    instead of inline pipe-delimited prose; cap sentence length.
  - >-
    Cut the repeated restatements of the demonstrable-alpha range, label budget, and decoy-too-easy caveat to a single early
    statement each; the document currently re-derives them in nearly every field.
- dimension: contribution
  score: 3
  justification: >-
    A first label-free FDR knob at the fuzzy-unification interface is a genuinely valuable and novel capability, and the design
    yields a mechanism-level insight (S4) even under the most probable partial outcome. Held from 4 by the external-validity
    gap: scoping the confirmatory headline to CLUTRR's closed kinship vocabulary risks demonstrating calibration validity
    where the targeted phenomenon (plausible high-confidence false facts, genuine ontology-alignment bridges) is weakest,
    so the contribution as scoped may not deliver the motivating operational capability.
  improvements:
  - >-
    Add a clearly-scoped, budget-powered secondary confirmatory claim on the realistic set (precision / hallucination-reduction
    vs. baselines at matched recall) so the motivating operational capability is demonstrated somewhere adequately powered,
    even if FDR-diagonal validity stays CLUTRR-only.
  - >-
    If the realistic set cannot be powered, reframe the headline honestly as 'validity of a label-free FDR knob, established
    on a crisp-gold synthetic benchmark' and soften the operational-pipeline framing, rather than implying the confirmatory
    cell delivers the legal/news/story use case.
critiques:
- id: ''
  category: rigor
  severity: major
  description: >-
    The document-level S4 predictive account is the de-risked deliverable that is supposed to survive a partial confirmatory
    outcome, and the prior review's fix correctly moved its validation unit from genre (n=1) to document/cluster ('many held-out
    units'). But that fix was made powerable by basing S4 on CLUTRR's free gold — and CLUTRR is precisely where S4 is likely
    ill-posed. CLUTRR documents are machine-generated kinship narratives over a small fixed relation vocabulary, varying mainly
    in hop-count and distractor injection; they are near-homogeneous in exactly the features S4 must predict from (entity
    density, 'document specificity', genre-as-feature). The genuine feature variance lives in the ~60-doc realistic set, which
    is 'illustrative' and underpowered. Compounding this, at a meaningful target alpha (~0.1) knockoff+ deliberately admits
    few items, so the per-document 'above-cutoff tail-exchangeability gap' is estimated from a handful of admissions per document
    — extremely noisy — forcing re-aggregation to clusters that shrinks the 'many held-out units' back toward few. The net
    risk is that the safety net is unvalidatable for the same power reasons the design fears, leaving the program exposed
    to the uninterpretable-null outcome.
  suggested_action: >-
    In the Phase-0 pilot, measure and report two things before committing the S4 budget: (i) the cross-document variance of
    the S4 features ON CLUTRR, and (ii) the expected per-document admitted-count at the operative alpha. If CLUTRR feature
    variance or per-document tail counts are too small to support a per-document gap regression, either base S4 on the realistic
    set with a pre-registered >=3-4 sources/clusters (and budget it as confirmatory, not illustrative), or define the S4 unit
    at the cluster level with an explicit count of held-out units and a power analysis for the GAP regression itself (not
    just the win-rate test). State a minimum number of held-out units below which S4 is reported as descriptive, not predictive.
- id: ''
  category: scope
  severity: major
  description: >-
    Scoping the single confirmatory headline to CLUTRR undercuts the motivating problem. The entire motivation — and the user's
    stated deliverable — is operational text-to-logic on realistic professional documents (legal clauses, news briefs, stories),
    where fuzzy unification and plausible hallucination actually bite. CLUTRR is synthetic, templated, closed-vocabulary kinship,
    where: (a) the LLM rarely produces PLAUSIBLE hallucinations because the relation set is tiny and well-known, so the 'plausibility-matched
    decoy' phenomenon the method hinges on is weakest and hardest to demonstrate meaningfully; (b) 'fuzzy-unification bridges'
    collapse to near-deterministic normalizations under the kinship algebra (the very crispness that makes bridge gold free
    also makes the bridge half of the headline a weak test of the genuine ontology-alignment mechanism); and (c) the targeted
    failure mode (dangerous plausible false facts) is least represented. The confirmatory cell may therefore validate calibration
    precisely where the mechanism matters least, while the realistic probe — the only place the method's value would show
    — is too small (~60 docs, illustrative) to support a claim.
  suggested_action: >-
    Keep CLUTRR as the validity-of-control anchor (its free crisp gold is the right place to test FDR-diagonal tracking),
    but add an adequately-powered secondary confirmatory claim on the realistic set — e.g., atomic-fact precision and hallucinated-conclusion-rate
    vs. the two baselines at matched recall — that the published budget actually covers. Alternatively, reframe the contribution
    explicitly as 'validity of a label-free FDR knob on a crisp-gold synthetic benchmark' and soften the operational-pipeline
    framing. Either way, state plainly that CLUTRR tests calibration validity, not operational usefulness on professional
    documents.
- id: ''
  category: methodology
  severity: major
  description: >-
    Knockoff+/TDC FDR control rests on the null sign-flip property: for genuinely-false reals, the sign of W_i = score(real_i)
    - score(decoy_i) must behave like an (exchangeable) coin flip conditional on magnitudes. Two design choices threaten this
    beyond the (acknowledged) construction-level exchangeability gap. (i) LLM scoring errors are correlated WITHIN a document
    (shared context, shared model biases), so pooled null signs are not independent; pooling correlated signs degrades the
    validity/variance relative to the i.i.d. analysis the '+1' floor argument assumes. (ii) Scoring reals, decoys, and entrapment
    JOINTLY in batched prompts (chosen for cost) introduces within-batch contrast/ranking effects that couple scores across
    items and can let the model implicitly detect the fabricated item, systematically depressing decoy scores -> fewer decoy
    wins -> anti-conservative (optimistic) FDP_hat. The tail diagnostics catch the marginal symptom but cannot distinguish
    a scoring artifact from genuine decoy non-exchangeability — so this confound could make the entire confirmatory run uninterpretable
    with respect to the central scientific question.
  suggested_action: >-
    (a) Add to the assumptions an explicit statement of the sign-flip/dependence conditions knockoff+ needs, naming within-document
    sign dependence as a risk, and use a per-document block structure in the FDP variance estimate rather than treating pooled
    signs as independent. (b) Score each item or matched pair with provenance blinded and order randomized (ideally in isolation),
    and pre-register a sensitivity check of the calibration diagonal to isolated-vs-batched scoring so an anti-conservative
    scoring artifact is not mis-attributed to decoy exchangeability failure. (c) If batching must be kept for cost, demonstrate
    in the pilot that batched and isolated scores agree on a labeled slice before committing the headline budget.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The design is so thoroughly hedged that it verges on unfalsifiable as a package. Every claim row carries an 'ON FAIL:
    reported as X', and the DISCONFIRMED criterion requires a conjunction (counterfactual decoys anti-conservative AND entrapment
    co-fails AND S4 fails out-of-sample), so almost every outcome is framed as a contribution. Pre-registering the confirmatory
    cell addresses cherry-picking, but a top reviewer will still ask: what single result would make you conclude the central
    claim is wrong? With S4 simultaneously threatened by the powerability concern above, the universal safety net may not
    actually hold, making the over-hedging both a presentation and a rigor liability.
  suggested_action: >-
    State one crisp, pre-registered PRIMARY disconfirmation tied to the confirmatory cell ALONE and independent of S4 (e.g.,
    'on CLUTRR facts at the pilot-powered alpha, counterfactual-decoy realized FDR exceeds target by more than tolerance tau
    => central control claim disconfirmed'). Keep S4 as a separately-reported finding that may add value on partial outcomes,
    not as a universal escape hatch that prevents any clean disconfirmation.
- id: ''
  category: clarity
  severity: minor
  description: >-
    Density was flagged in the two previous rounds and is only marginally improved. The 'three load-bearing numbers up front'
    and the S1-S5 chain help, but nearly every field is still a long defensive run-on interleaving the claim, its caveats,
    and rebuttals to earlier reviews. This obscures the genuine novelty, makes the proposal harder to evaluate now, and will
    cost the ACL presentation score.
  suggested_action: >-
    Lead each major field with one plain-language sentence of the mechanism before any qualification; move defensive asides
    into assumptions/method; render S1-S5 as a real table (claim | test | pass | on-fail); cap sentence length; and state
    the demonstrable-alpha range, expected document/call counts, and operation-vs-validation label budget exactly once, early.
    The methodology is strong enough that presentation is now a primary lever on the score.
- id: ''
  category: evidence
  severity: minor
  description: >-
    Related work is strong on the proteomics/knockoff and labeled-conformal sides and now cites the closest hallucination-FDR
    neighbor (Li et al., 2508.18473) and DINCO. However, the late-2025/2026 hallucination-detection frontier is moving fast
    — e.g., recent work on unifying hallucination detection with fact verification (arXiv 2512.02772) and fact-level black-box
    hallucination detection (EACL 2026 Findings). These are not novelty threats (they are detection/verification, not label-free
    admission-gating via decoy competition, and carry no per-leaf certificates or symbolic propagation), but a top-venue reviewer
    will expect awareness of them.
  suggested_action: >-
    Scan the most recent (late-2025/2026) fact-level hallucination-detection and fact-verification papers and add a one-line
    differentiation if relevant, reusing the existing axes (label-free operation vs. labeled/reference detection; neuro-symbolic
    admission-gating vs. output-level detection; competition/certificates vs. scoring). Low priority relative to the methodology
    critiques.
score: 5
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same decoy-competition FDR-gate frame; refines S4 to doc-level, adds entrapment tail diagnostic, crisp CLUTRR bridges.
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

### [2] HUMAN-USER prompt · 2026-06-16 04:12:40 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-16 04:15:21 UTC

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

### [4] SYSTEM-USER prompt · 2026-06-16 04:19:37 UTC

```
STOP — your tool log shows you only SEARCHED the web and never opened or read a single full page. Search result snippets (titles, URLs, one-line descriptions) are NOT sufficient evidence: they cannot confirm novelty, and they cannot give you the exact methods, numbers, or claims of prior work.

Before you finalise this hypothesis you MUST now actually fetch and read the most relevant sources in full. Use the built-in `WebFetch` tool (or, for exact quotes/numbers, the aii-web-tools `aii_fast_web_fetch.py fetch`/`grep` script). Open at least the few most relevant URLs, read their real content, and let that evidence revise your conclusions.

Then re-write your structured output file with the corrected, evidence-grounded result. Do not stop until you have fetched at least one full page.
```
