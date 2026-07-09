# review_hypo — create_idea

> Phase: `hypo_loop` · round 1 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 03:19:57 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_1/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 03:20:03 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<hypothesis>
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
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>





<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE:
This is the first iteration — there is no previous hypothesis. Leave
``relation_type`` null and ``relation_rationale`` empty.

Provide your review via structured output.
</task><user_data>
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 03:20:03 UTC

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

### [4] ASSISTANT · 2026-06-16 03:20:50 UTC

```
I'll start by reviewing my relevant memory, checking user uploads, and grounding the review in evidence through web research.
```

### [5] TOOL CALL — Read · 2026-06-16 03:20:50 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
```

### [6] TOOL CALL — Bash · 2026-06-16 03:20:50 UTC

```
List user uploads and current dir:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_1/review_hypo 2>/dev/null
```

### [7] TOOL CALL — ToolSearch · 2026-06-16 03:20:50 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [8] TOOL RESULT — Read · 2026-06-16 03:20:50 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "content": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n", "numLines": 19, "startLine": 1, "totalLines": 19}}
```

### [9] TOOL RESULT — ToolSearch · 2026-06-16 03:20:50 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [10] TOOL RESULT — Bash · 2026-06-16 03:20:50 UTC

```
{"stdout": "total 1954\ndrwxr-xr-x 2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 7 root root 2000164 Jun 16 03:05 ..\n---\ntotal 2075\ndrwxr-xr-x 2 root root 1004478 Jun 16 03:19 .\ndrwxr-xr-x 4 root root 1073428 Jun 16 03:19 ..\n-rw-r--r-- 1 root root   45863 Jun 16 03:20 .repl_agent.ptylog", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] ASSISTANT · 2026-06-16 03:20:56 UTC

```
User uploads is empty. Now let me ground the review in evidence with targeted searches on novelty and known failure modes.
```

### [12] TOOL CALL — WebSearch · 2026-06-16 03:20:56 UTC

```
knockoff filter target-decoy competition false discovery rate LLM hallucination selection
```

### [13] TOOL CALL — WebSearch · 2026-06-16 03:20:56 UTC

```
conformal prediction false discovery rate control LLM generated claims factuality
```

### [14] TOOL CALL — WebSearch · 2026-06-16 03:20:56 UTC

```
LLM confidence scores calibration hallucination plausible false facts overconfident
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 03:21:02 UTC

```
{"query": "knockoff filter target-decoy competition false discovery rate LLM hallucination selection", "results": [{"tool_use_id": "srvtoolu_011E5c3Fkcn72AEnxHdUbFq2", "content": [{"title": "Local False Discovery Rate Estimation with Competition-Based Procedures   for Variable Selection", "url": "https://arxiv.org/pdf/2206.02692"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}, {"title": "DeepPINK: reproducible feature selection in deep neural networks", "url": "https://arxiv.org/pdf/1809.01185"}, {"title": "Controlling the false discovery rate via competition: Is the +1 needed? - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167715223000433"}, {"title": "Controlling the False Discovery Rate via knockoffs: is the +1 needed?", "url": "https://www.researchgate.net/publication/360254730_Controlling_the_False_Discovery_Rate_via_knockoffs_is_the_1_needed"}, {"title": "Controlling the FDR in variable selection via multiple knockoffs", "url": "https://arxiv.org/pdf/1911.09442"}, {"title": "Group-walk: a rigorous approach to group-wise false discovery rate analysis by target-decoy competition | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii82/6701992"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://arxiv.org/pdf/1404.5609"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full"}]}, "I've completed the web search for your query about knockoff filters, target-decoy competition, false discovery rate, and LLM hallucination selection. Here are the key findings:\n\n## Main Concepts\n\nThe knockoff filter is a competition-based method that uses fake variables, called knockoffs, to control FDR. The idea of using competition for FDR control originates from the target-decoy (TD) search strategy used in mass spectrometry-based proteomics, which takes advantage of competitive decoy peptide sequences to estimate and control the FDR of peptide identifications.\n\n## How Target-Decoy Competition Works\n\nTarget-decoy competition (TDC) relies on associating with each hypothesis a \"target\" score and a \"decoy\" score. These scores are presumably generated so that for true null hypotheses the target and decoy are equally likely to win independently of all other hypotheses.\n\n## Applications\n\nOriginally aiming at variable selection in linear regression, the knockoff filter achieves FDR control for correlated variables in specific settings by constructing the knockoffs in an elaborated manner. Competition-based FDR control has recently gained significant popularity in other fields after Barber and Candès laid its theoretical foundation in a more general setting that included the feature selection problem.\n\nThe search results primarily focus on statistical methods for variable selection and proteomics applications. There doesn't appear to be specific information about applications to LLM hallucination selection in these results."], "durationSeconds": 7.033206212000005, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-06-16 03:21:04 UTC

```
{"query": "LLM confidence scores calibration hallucination plausible false facts overconfident", "results": [{"tool_use_id": "srvtoolu_01RWvtUUsWCBKeCSiaL5u9mt", "content": [{"title": "Confidence Calibration in LLMs", "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"}, {"title": "Avoiding LLM hallucinations and building LLM confidence scores", "url": "https://nanonets.com/blog/how-to-tell-if-your-llm-is-hallucinating/"}, {"title": "Atomic Calibration of LLMs in Long-Form Generations - ACL Anthology", "url": "https://aclanthology.org/2025.findings-ijcnlp.9/"}, {"title": "Cost-Effective Hallucination Detection for LLMs", "url": "https://arxiv.org/pdf/2407.21424"}, {"title": "Large Legal Fictions: Profiling Legal Hallucinations in Large Language   Models", "url": "https://arxiv.org/pdf/2401.01301"}, {"title": "Hallucination Detection and Mitigation in Large Language Models", "url": "https://arxiv.org/pdf/2601.09929"}, {"title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability", "url": "https://arxiv.org/pdf/2505.21772"}, {"title": "Multicalibration for Confidence Scoring in LLMs", "url": "https://arxiv.org/pdf/2404.04689"}]}, "I've performed the web search for you. Here are the key findings on LLM confidence scores calibration and hallucination:\n\n## Key Concepts\n\nConfidence calibration in LLMs is the process of aligning model confidence scores with the true probability of correctness across various tasks. Confidence calibration is essential to enhance the trustworthiness of LLMs as an effective indicator of hallucination.\n\n## The Problem: Overconfident Hallucinations\n\nA critical issue is that LLMs can produce high-confidence hallucinations where the model consistently generates the same incorrect output with high certainty, with entropy remaining low because the model's probability distribution is sharply peaked around wrong answers. Neural models tend to be miscalibrated, particularly in the form of models being overconfident.\n\n## Measurement Metrics\n\nExpected Calibration Error (ECE) quantifies the alignment between a model's predicted confidence scores and its actual empirical accuracy—a perfectly calibrated model would have matching confidence and accuracy.\n\n## Approaches to Improvement\n\nRecent techniques include natural language critique prompts and supervised critique calibration that teach LLMs patterns of over-/under-confidence. Atomic calibration evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims."], "durationSeconds": 7.415611677000001, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-06-16 03:21:08 UTC

```
{"query": "conformal prediction false discovery rate control LLM generated claims factuality", "results": [{"tool_use_id": "srvtoolu_014bDZyxa4F36oJ8y6es3wUn", "content": [{"title": "Differentiable Conformal Training for LLM Reasoning Factuality", "url": "https://arxiv.org/html/2604.20098"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}, {"title": "Filtering with Confidence: When Data Augmentation Meets Conformal Prediction", "url": "https://arxiv.org/pdf/2509.21479"}, {"title": "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs", "url": "https://arxiv.org/pdf/2603.21172"}, {"title": "[2604.20098] Differentiable Conformal Training for LLM Reasoning Factuality", "url": "https://arxiv.org/abs/2604.20098"}, {"title": "Prune 'n Predict: Optimizing LLM Decision-making with Conformal Prediction", "url": "https://arxiv.org/pdf/2501.00555"}, {"title": "Conformal Language Modeling via Posterior Sampling", "url": "https://arxiv.org/html/2606.03731"}, {"title": "ICLR Poster CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift", "url": "https://iclr.cc/virtual/2026/poster/10008295"}]}, "Based on the search results, here's what I found about conformal prediction, false discovery rate control, and LLM-generated claims factuality:\n\n## Key Applications\n\nConformal Prediction addresses LLM hallucination by calibrating error rates on held-out data to provide statistically valid confidence guarantees, filtering out risky claims to ensure hallucination rates remain below a user-specified level.\n\n## False Discovery Rate Control\n\nRecent work extends conformal prediction to multiple test units with a focus on ensuring valid false discovery rate (FDR) control for factuality verification tasks.\n\n## Approaches to Claim Validation\n\nResearch in this area includes several methods:\n- Approaches segment LLM outputs into individual claims and apply conformal prediction to select factual ones\n- Coherent Factuality extends to multi-step reasoning by representing outputs as dependency graphs and jointly validating claims with their logical ancestors\n- The goal is to calibrate a pruning procedure that removes a minimal number of claims from an LLM-generated response, such that the remaining claims are all factual with high probability\n\n## Recent Advances\n\nRecent work introduces Differentiable Coherent Factuality (DCF), a fully differentiable relaxation that enables learning improved scorers while provably recovering the original algorithm's guarantees.\n\n## Limitations\n\nDespite their strong theoretical guarantees, conformal prediction techniques rely heavily on the exchangeability assumption between calibration and test data, which is frequently violated in real-world scenarios with dynamic covariate shifts."], "durationSeconds": 11.669083298000006, "searchCount": 1}
```

### [18] TOOL CALL — WebSearch · 2026-06-16 03:21:26 UTC

```
target-decoy competition limitations decoys not representative false targets proteomics FDR validity
```

### [19] TOOL CALL — WebSearch · 2026-06-16 03:21:26 UTC

```
Mohri Hashimoto language models conformal factuality guarantees claim filtering
```

### [20] TOOL CALL — WebSearch · 2026-06-16 03:21:26 UTC

```
conformal selection FDR control Jin Candes selecting candidates label-free p-values
```

### [21] TOOL RESULT — WebSearch · 2026-06-16 03:21:32 UTC

```
{"query": "Mohri Hashimoto language models conformal factuality guarantees claim filtering", "results": [{"tool_use_id": "srvtoolu_01TCDrbAdnZUVrXFgC6j63Gb", "content": [{"title": "Language Models with Conformal Factuality Guarantees", "url": "https://arxiv.org/pdf/2402.10978"}, {"title": "Language Models with Conformal Factuality Guarantees", "url": "https://proceedings.mlr.press/v235/mohri24a.html"}, {"title": "Statistical methods for assessing the factual accuracy of large language models | Department of Statistics", "url": "https://statistics.stanford.edu/events/statistical-methods-assessing-factual-accuracy-large-language-models"}, {"title": "Large language model validity via enhanced conformal prediction methods", "url": "https://arxiv.org/pdf/2406.09714"}, {"title": "[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"}, {"title": "Conformal Language Model Reasoning with Coherent Factuality", "url": "https://arxiv.org/pdf/2505.17126"}, {"title": "Large language model validity via enhanced conformal prediction methods", "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf"}, {"title": "GitHub - tatsu-lab/conformal-factual-lm · GitHub", "url": "https://github.com/tatsu-lab/conformal-factual-lm"}, {"title": "Large language model validity via enhanced conformal prediction methods", "url": "https://arxiv.org/html/2406.09714v1"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}]}, "Based on the search results, here's what I found about Mohri and Hashimoto's work on language models with conformal factuality guarantees and claim filtering:\n\n## Overview\n\nChristopher Mohri and Tatsunori Hashimoto propose \"conformal factuality,\" a framework that can ensure high probability correctness guarantees for language models by connecting language modeling and conformal prediction.\n\n## Core Approach\n\nThe correctness of an LM output is equivalent to an uncertainty quantification problem, where the uncertainty sets are defined as the entailment set of an LM's output. Conformal prediction in language models corresponds to a back-off algorithm that provides high probability correctness guarantees by progressively making LM outputs less specific (and expanding the associated uncertainty sets).\n\n## Claim Filtering Mechanism\n\nThe methods work by filtering a claim from the LLM's original response if a scoring function evaluated on the claim fails to exceed some estimated threshold. More specifically, they improve the factuality of LM generations by splitting them into subclaims and filtering low-confidence subclaims via conformal prediction.\n\n## Key Benefits\n\nThis approach applies to any black-box LM and requires very few human-annotated samples. The method obtains factuality calibrated to a user-specified parameter α while maintaining a significant proportion of the original output."], "durationSeconds": 7.139874761999992, "searchCount": 1}
```

### [22] TOOL RESULT — WebSearch · 2026-06-16 03:21:34 UTC

```
{"query": "target-decoy competition limitations decoys not representative false targets proteomics FDR validity", "results": [{"tool_use_id": "srvtoolu_01Lrgzo3L9oSZJA5dHisRmUT", "content": [{"title": "Protein Language Model Decoys for Target–Decoy Competition in Proteomics: Quality Assessment and Benchmarks | bioRxiv", "url": "https://www.biorxiv.org/content/10.64898/2026.03.27.714819v1.full"}, {"title": "Beyond target-decoy competition: stable validation of peptide and protein identifications in mass spectrometry-based discovery proteomics | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/765057v2.full"}, {"title": "An averaging strategy to reduce variability in target-decoy estimates of false discovery rate", "url": "https://www.biorxiv.org/content/10.1101/440594.full.pdf"}, {"title": "Challenging targets or describing mismatches? A comment on Common Decoy   Distribution by Madej et al", "url": "https://arxiv.org/pdf/2210.08815"}, {"title": "How to train a post-processor for tandem mass spectrometry proteomics database search while maintaining control of the false discovery rate", "url": "https://www.biorxiv.org/content/10.1101/2023.10.26.564068.full.pdf"}, {"title": "Beyond target-decoy competition: stable validation of peptide and protein identifications in mass spectrometry-based discovery proteomics", "url": "https://www.biorxiv.org/content/10.1101/765057.full.pdf"}, {"title": "Target-decoy search strategy for mass spectrometry-based proteomics - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/20013364/"}, {"title": "Averaging Strategy To Reduce Variability in Target-Decoy Estimates of False Discovery Rate | Journal of Proteome Research", "url": "https://pubs.acs.org/doi/10.1021/acs.jproteome.8b00802"}, {"title": "When Target–Decoy False Discovery Rate Estimations Are Inaccurate and How to Spot Instances | Journal of Proteome Research", "url": "https://pubs.acs.org/doi/abs/10.1021/pr301063v"}]}, "I've performed the web search for information about target-decoy competition limitations in proteomics. Here are the key findings:\n\n## Key Limitations and Concerns:\n\n**Equal Chance Assumption (ECA) Validity:**\nThe quality of target-decoy competition FDR estimates is strictly linked to the validity of the Equal Chance Assumption (i.e., the decoy's capacity to adequately fool the database search engine). If it fools it too much, the TDC-FDR will overestimate the FDP; whereas if it is too unrealistic to fool the search engine, the FDP will be underestimated.\n\n**Stability Issues:**\nTarget-decoy competition has become less reliable as the accuracy of modern mass spectrometers improved. Additionally, the procedure can yield different results for a fixed data set analyzed with different decoy databases, and this decoy-induced variability is particularly problematic for smaller FDR thresholds, data sets, or databases.\n\n**Decoy Design Challenges:**\nLarge-scale proteomics relies heavily on target-decoy competition for false discovery rate estimation in peptide identification, and the performance of this strategy depends strongly on the design of the decoy database. The research shows that decoys can become so close to real targets that target protection begins to fail.\n\n**Practical Issues with Common Decoy Construction:**\nThe most common decoy construction is the reversal of the entire target protein before it is digested into decoy peptides. These decoy peptides are different from ones created by reversing the target peptides directly and, in particular, their mass often differs slightly from that of the corresponding reversed peptide making for a somewhat unnatural pairing.\n\nThe search results indicate that while target-decoy competition remains the most widely used FDR control method in proteomics, its effectiveness depends critically on whether decoys are sufficiently representative of false matches without being artificially easy or difficult to distinguish."], "durationSeconds": 10.092079347999999, "searchCount": 1}
```

### [23] TOOL RESULT — WebSearch · 2026-06-16 03:21:38 UTC

```
{"query": "conformal selection FDR control Jin Candes selecting candidates label-free p-values", "results": [{"tool_use_id": "srvtoolu_01GzLeVH7vTRis39ThPNJ1ew", "content": [{"title": "Selective labeling with false discovery rate control", "url": "https://arxiv.org/html/2510.14581v1"}, {"title": "Optimized Conformal Selection: Powerful Selective Inference After   Conformity Score Optimization", "url": "https://arxiv.org/pdf/2411.17983"}, {"title": "Selection from Hierarchical Data with Conformal e-values", "url": "https://arxiv.org/html/2501.02514"}, {"title": "Selective conformal inference with false coverage-statement rate control", "url": "https://arxiv.org/pdf/2301.00584"}, {"title": "conformal-selection-for-efficient-and-accurate-compound- ...", "url": "https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/672102dcf9980725cf45d9c3/original/conformal-selection-for-efficient-and-accurate-compound-screening-in-drug-discovery.pdf"}, {"title": "Distribution-Free Selection of Low-Risk Oncology Patients for Survival Beyond a Time Horizon", "url": "https://arxiv.org/pdf/2512.18118"}, {"title": "ACS: An interactive framework for conformal selection", "url": "https://arxiv.org/pdf/2507.15825"}, {"title": "Selection by Prediction with Conformal p-values", "url": "https://www.jmlr.org/papers/volume24/22-1176/22-1176.pdf"}, {"title": "SAFER: A Calibrated Risk-Aware Multimodal Recommendation Model for Dynamic Treatment Regimes", "url": "https://arxiv.org/pdf/2506.06649"}, {"title": "[2307.09291] Model-free selective inference under covariate shift via weighted conformal p-values", "url": "https://arxiv.org/abs/2307.09291"}]}, "Based on the search results, here's what I found about conformal selection with FDR control by Jin and Candès:\n\n## Overview\n\nConformal selection aims to identify unlabeled samples with large unobserved labels while controlling selection errors. Given labeled data and unlabeled test samples, the goal is to select a subset of test samples such that most of them obey specified thresholds, formalized by false discovery rate (FDR) control.\n\n## Methodology\n\nThe conformal selection pipeline constructs p-values using a set of labeled calibration data and determines the selection set by multiple testing. More specifically, conformal selection formulates the selection task as a multiple hypotheses testing problem where each unit in the test set is associated with a hypothesis, constructs a p-value for each hypothesis, and obtains the selection set by applying the Benjamini Hochberg procedure to the p-values.\n\n## FDR Control Guarantee\n\nConformal selection achieves FDR control as long as the training and the test data are jointly exchangeable. The conformal p-values satisfy a property that ensures smaller values provide evidence of positive selection outcomes and is sufficient to guarantee FDR control when the BH procedure is applied.\n\n## Extensions and Applications\n\nRecent extensions include applications to covariate shift, online settings, constrained settings, and applications to drug discovery and large language models."], "durationSeconds": 12.849139175999998, "searchCount": 1}
```

### [24] ASSISTANT · 2026-06-16 03:24:17 UTC

```
I have strong evidence to ground the review. Key findings:

1. **The Equal Chance Assumption (ECA) is the documented Achilles' heel of target-decoy competition** — proteomics literature states FDR estimates are valid only if decoys are "just right": too-unrealistic decoys → FDP *underestimated* (anti-conservative); decoy-induced variability is "particularly problematic for smaller FDR thresholds, data sets, or databases."
2. **LLMs produce high-confidence *plausible* hallucinations** — so the dangerous false reals get high scores while type-matched random decoys get low scores → distribution mismatch → ECA violated in the anti-conservative direction.
3. **Strong recent baselines are under-credited/missing**: Mohri & Hashimoto (ICML 2024) conformal factuality already filters claims to user-specified α with very few labels; conformal selection (Jin & Candès) + BH gives FDR-controlled selection; Coherent Factuality (2505.17126) handles multi-step.

Let me write the structured review.
```

### [25] TOOL CALL — Write · 2026-06-16 03:24:17 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_1/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is a genuinely creative Level-3 cross-domain transfer: importing the knockoff filter / target-decoy competition (TDC) FDR machinery from statistics and proteomics to gate the neural-to-symbolic admission boundary of a text-to-logic pipeline, so the hallucination rate of an extracted Prolog/ProbLog knowledge base becomes a tunable, label-free, certified quantity. The problem is important and well-aligned with the ACL Knowledge Extraction trustworthiness goal, the writing is clear, the related-work coverage is strong, and the proposal is unusually honest about its crux (exchangeability) with explicit, well-designed confirm/disconfirm criteria and decoy-family ablations. The auditable trace-graphs with per-leaf decoy certificates are a real strength. However, the entire headline claim ('control hallucination to a user-specified alpha without labels') is load-bearing on a single assumption — that synthetic decoys are statistically exchangeable with genuinely-false LLM proposals (the proteomics 'Equal Chance Assumption') — and both the target-decoy literature and the LLM-calibration literature predict this will fail in the anti-conservative direction for the proposed decoy construction: the consequential hallucinations are PLAUSIBLE false facts that the LLM scores highly, whereas random type-matched decoys are 'too unrealistic to fool' the scorer, which the proteomics literature explicitly notes leads to UNDER-estimated FDP (realized FDR exceeds target). Three further issues compound this: (1) the per-document candidate set is tiny (~10-40 items), where TDC is known to be high-variance and the knockoff+ offset makes small alpha unachievable; (2) two of three benchmark families (RuleTaker/ProofWriter) present facts in near-symbolic form, making the extraction-precision claim near-trivial there, while the realistic setting (legal/news/story) is a small hand-annotated set that is likely underpowered for the significance claims; and (3) strong, recent, label-efficient baselines (Mohri-Hashimoto conformal factuality; conformal selection + BH; Coherent Factuality) are under-credited and not used as baselines, weakening both the novelty framing and the evaluation. None of these is necessarily fatal — the crux is directly tested and even a characterization of when ECA holds for LLM proposals would be publishable — but the decoy construction must be redesigned to target the realized hallucination distribution, the FDR claim must be re-scoped to corpus-aggregate, and the conformal baselines must be added before experiments will produce a defensible top-venue result.",
  "strengths": [
    "Genuinely novel cross-domain transfer: target-decoy/knockoff FDR control has lived entirely in feature selection and mass-spectrometry proteomics and (per literature search) has not been applied to LLM-proposed symbolic assertions, fuzzy unification, or neuro-symbolic reasoning. The 'fully label-free' angle is a real differentiator from conformal methods.",
    "Tackles a precise, important, and well-scoped problem — quantitative hallucination control at the exact pressure point (the neural-to-symbolic admission boundary where fuzzy unification and common-sense gap-filling occur) — directly serving the ACL Knowledge Extraction trustworthiness/auditability goal.",
    "Unusually honest and well-structured science: the exchangeability assumption is named as the crux, experiment (a) directly tests it (realized vs target alpha along the diagonal), decoy-family ablations (e) isolate which constructions preserve exchangeability, and the DISCONFIRMED criteria are concrete and falsifiable. A negative result would still be informative.",
    "The auditable trace-graphs with provenance tags (document span vs ontology vs admitted common-sense) and a per-leaf decoy-competition certificate are a strong interpretability contribution and differentiate the work from black-box neural baselines.",
    "Realistic, reproducible scope: commodity CPU, $10 LLM budget, batched joint scoring of reals+decoys, and a sensible benchmark spread (ProofWriter/RuleTaker for gold proofs, CLUTRR for paraphrased multi-hop, plus a hand-annotated realistic set)."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 2,
      "justification": "The core validity claim rests on decoy exchangeability (the proteomics Equal Chance Assumption), which both the TDC literature and LLM-calibration findings predict will fail in the anti-conservative direction for the proposed random/type-matched decoys: plausible hallucinations get high LLM confidence, random decoys get low confidence, so admitted-decoy counts under-estimate admitted-false-real counts and realized FDR exceeds target. Compounded by small per-document candidate counts (high-variance TDC, unachievable small alpha with the +1 offset) and an unjustified label-free score->ProbLog-probability calibration step. The design is honest and tests the crux, but as specified the central guarantee is likely to break.",
      "improvements": [
        "Redesign decoy construction to match the REALIZED hallucination distribution, not a random null. WHAT: generate decoys via the LLM's own plausible-but-document-contradicted counterfactual process (and lean on cross-document decoys, which are the closest to the dangerous null), rather than random same-type entity/relation swaps. HOW: prompt the LLM to fabricate maximally-plausible facts the document does NOT entail, conditioned on document context, so the decoy score distribution matches that of genuine plausible hallucinations. WHY: this is the difference between estimating the FDR of the easy null and the consequential null; it directly attacks the anti-conservative failure mode and could move the calibration curve onto the diagonal (large soundness impact).",
        "Add a direct ECA diagnostic on a labeled probe set BEFORE trusting any calibration curve. WHAT/HOW: on a held-out labeled slice, compare the score distributions of KNOWN-false reals vs their decoys (e.g., two-sample test, win-rate of decoy over false real should be ~0.5). WHY: turns the central assumption from hoped-for into measured, and tells you which decoy family (if any) achieves exchangeability.",
        "Re-scope the FDR claim from per-document to corpus-aggregate and report the achievable-alpha floor. WHY: per-document TDC with ~10-40 items and the knockoff+ offset cannot deliver small alpha; aggregate control is statistically meaningful and honestly reportable."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "Clear, well-organized, with precise terminology, a strong related-work section, and explicit confirm/disconfirm criteria. Main deductions: the framing oversells a 'guarantee' that is actually conditional on an empirically fragile assumption, and it lumps all conformal methods as 'needs labels / certifies single answers,' which under-credits recent label-efficient claim-level conformal FDR work.",
      "improvements": [
        "Soften 'controls hallucination to a user-specified alpha WITHOUT labels' to a conditional claim ('controls... PROVIDED engineered decoys satisfy exchangeability, which we test'). WHY: a top reviewer will otherwise read the unconditional guarantee as overclaiming.",
        "Sharpen the true novelty wedge: not 'no one does tunable claim-level alpha' (Mohri-Hashimoto already does, with very few labels) but 'fully label-free + gates the neural->symbolic interface + propagates through symbolic deduction with per-leaf certificates.' WHY: a precise wedge is more credible and harder to attack.",
        "State explicitly the dependency on the commodity upper-ontology slice for typed decoys and bridge licensing, since the abstract claims 'without a trusted ontology of constraints' — clarify it needs typing, not constraints."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "Original idea attacking a meaningful problem with potential community value (a tunable, auditable hallucination knob for text-to-logic). The contribution is somewhat de-risked by the validity question, but even a careful characterization of when/if ECA can be engineered for LLM proposals, plus the auditable-trace contribution, would be valuable. Held back from 4 by the missing strong baselines and the benchmark mismatch that limits how convincingly the headline claims can be demonstrated.",
      "improvements": [
        "Add Mohri-Hashimoto conformal factuality, conformal selection + BH, and a Coherent-Factuality-style multi-step variant as BASELINES (not just related work), at matched label budget. WHY: directly demonstrates the value of label-free-ness and situates the contribution against the actual state of the art (large contribution+rigor impact).",
        "Position the work as complementary to ontology-constraint filtering and conformal calibration (it already argues this) and show a hybrid (decoy-gate + conformal) ablation. WHY: turns a potential 'why not just use conformal' rejection into a contribution.",
        "Commit to releasing the decoy-generation prompts, the calibration harness, and the hand-annotated realistic dataset. WHY: reproducible artifacts raise contribution at KE/NeSy venues."
      ]
    }
  ],
  "critiques": [
    {
      "category": "rigor",
      "severity": "major",
      "description": "Exchangeability (the proteomics Equal Chance Assumption) is the single load-bearing assumption, and as specified the decoy construction is likely to violate it in the ANTI-CONSERVATIVE direction. The TDC literature is explicit: if decoys are 'too unrealistic to fool the search engine,' FDP is UNDER-estimated. The LLM-calibration literature shows models assign HIGH confidence to plausible hallucinations. The dangerous false reals are precisely the plausible ones (e.g., a reasonable-sounding inference the document never states); random same-type entity/relation-swap decoys are easy negatives that the LLM will score low. So admitted decoys will under-count admitted false reals, the estimated FDR will be optimistic, and realized FDR will exceed target — the opposite of the claimed control. The decoys are exchangeable with the WRONG (easy) null.",
      "suggested_action": "Generate decoys that match the realized hallucination distribution: have the LLM fabricate maximally-plausible, document-conditioned counterfactual facts/bridges/rules (and emphasize cross-document decoys), rather than random type-matched swaps. Then validate ECA directly on a labeled probe set by checking that a known-false real and its matched decoy each win the score competition ~50% of the time; only proceed to the calibration sweep for decoy families that pass this test. Report the win-rate per decoy family as a first-class result."
    },
    {
      "category": "evidence",
      "severity": "major",
      "description": "Strong, recent, label-efficient baselines are under-credited and not used as baselines. Mohri & Hashimoto (ICML 2024, 'Language Models with Conformal Factuality Guarantees') already filters claims to a user-specified factuality alpha with 'very few human-annotated samples'; conformal selection (Jin & Candes) applies BH to conformal p-values for FDR-controlled selection; 'Conformal LM Reasoning with Coherent Factuality' (2505.17126) handles multi-step dependency graphs. The hypothesis characterizes conformal methods as needing a labeled calibration set and certifying only single answers, which is no longer accurate for claim-level/set-level conformal factuality. This weakens both the novelty framing and the empirical comparison.",
      "suggested_action": "Add conformal factuality (Mohri-Hashimoto) and conformal-selection+BH as explicit baselines at a matched (small) label budget, plus a multi-step coherent-factuality variant for the deduction experiment. Re-sharpen the novelty claim to the genuine wedge: fully label-free control that gates the neural->symbolic interface and propagates through symbolic deduction with auditable per-leaf certificates. Cite these works in related work and explain precisely what each cannot do that decoy-gating can."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "Small candidate count per document undermines per-document FDR control. A ~3000-character document yields perhaps 10-40 candidate facts; target-decoy/knockoff estimates are high-variance at this scale (the proteomics literature flags decoy-induced variability as 'particularly problematic for smaller FDR thresholds, data sets, or databases'), and the knockoff+ '+1' offset makes small alpha unachievable (with k discoveries the minimum non-trivial FDR is ~1/(k+1), so e.g. alpha=0.05 requires ~20+ admissions). The success criterion 'realized FDR tracks target along the diagonal per dataset family' is therefore ill-posed at the per-document level the abstract claims.",
      "suggested_action": "State explicitly that control is corpus-aggregate (pooled over documents), and report the achievable-alpha floor as a function of candidate count. Show the calibration diagonal on pooled discoveries, and report per-document variance separately. Consider grouping facts across documents within a dataset to increase the effective number of hypotheses where the application allows."
    },
    {
      "category": "scope",
      "severity": "major",
      "description": "Benchmark mismatch for the extraction-precision claim. RuleTaker/ProofWriter present facts and rules already in near-symbolic, templated form, so 'atomic-fact extraction precision/recall' is near-trivial there and does not stress the hallucination gate; the gate's value only appears under paraphrase and genuine textual ambiguity. CLUTRR (paraphrased relations) is the meaningful synthetic test, and the realistic legal/news/story setting is where the contribution actually matters — but that set is described as 'small hand-annotated,' which is likely underpowered for the strong significance claims in success criterion (2).",
      "suggested_action": "Use RuleTaker/ProofWriter primarily for the reasoner-propagation experiment (where gold proofs are the asset), not for the headline extraction-PR claim. Enlarge the realistic annotated set (or add a paraphrased/back-translated RuleTaker variant) to obtain adequate power, run a power analysis for the precision/hallucination-rate comparisons, and restrict the strong extraction-PR significance claims to CLUTRR and the realistic set."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "The ProbLog probabilities are to be 'set from calibrated scores,' but in a fully label-free regime there is no mechanism that calibrates raw LLM scores to probabilities — decoy competition yields a SET-level FDR, not a per-fact probability. Mapping decoy-competition rank to a ProbLog fact probability is currently unjustified and could silently inject miscalibration into every probabilistic conclusion.",
      "suggested_action": "Either drop the probabilistic-reasoning arm and use crisp admit/reject (cleanest), or specify an explicit, documented monotone score->probability map (e.g., isotonic on a small labeled probe, or a fixed heuristic), and ablate its effect on conclusion accuracy so the contribution of the probability mapping is separated from the gate itself."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "'Matched recall' comparisons across CoT, RAG, LINC/Logic-LM are not operationalized. These baselines do not naturally produce an atomic-fact precision-recall curve (CoT/RAG emit free-form text; LINC emits a single translation), so equalizing recall to compare precision is underspecified and could be gamed.",
      "suggested_action": "Specify the recall-matching protocol: for the gated method sweep the admission threshold to trace a full PR curve; for free-form baselines define a claim-extraction-and-matching protocol (e.g., decompose outputs into atomic claims, match to gold by entailment) and report full PR curves with confidence intervals rather than single matched-recall points."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "Decoys are required to be 'guaranteed NOT entailed by the document,' but verifying non-entailment is itself an error-prone extraction/reasoning step. A same-type entity 'absent from the document' may be entailed via admitted common-sense, and a 'not-stated' relation may follow by deduction — contaminating the negative controls and biasing the FDR estimate.",
      "suggested_action": "Define and validate the non-entailment check explicitly (e.g., symbolic non-derivability against the admitted KB plus a human/LLM entailment audit on a sample), and report the contamination rate of decoys that turn out to be entailed. Exclude or down-weight contaminated decoys and quantify the effect on the calibration curve."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The propagation claim ('tightening alpha monotonically and predictably reduces multi-hop hallucination') is optimistic: a single false admitted fact can fan out to many false conclusions (amplification), conclusions are conjunctions of admitted facts/rules, and the symbolic reasoner is exact, so conclusion-level error is a nonlinear function of fact-level FDR, not a smooth monotone transfer. Assumption (d) (deduction error dominated by admitted facts/rules) is plausible but should be argued, not asserted.",
      "suggested_action": "Add a small analytical or Monte-Carlo model linking fact-level FDR to conclusion-level error under the actual proof structures (fan-out, conjunction depth) to set quantitative expectations for experiment (d), and measure amplification empirically (false conclusions per false admitted fact). This makes 'predictable propagation' a tested quantity rather than a hope."
    }
  ],
  "score": 5,
  "confidence": 4,
  "relation_type": null,
  "relation_rationale": ""
}
```

### [26] TOOL RESULT — Write · 2026-06-16 03:24:17 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_1/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is a genuinely creative Level-3 cross-domain transfer: importing the knockoff filter / target-decoy competition (TDC) FDR machinery from statistics and proteomics to gate the neural-to-symbolic admission boundary of a text-to-logic pipeline, so the hallucination rate of an extracted Prolog/ProbLog knowledge base becomes a tunable, label-free, certified quantity. The problem is important and well-aligned with the ACL Knowledge Extraction trustworthiness goal, the writing is clear, the related-work coverage is strong, and the proposal is unusually honest about its crux (exchangeability) with explicit, well-designed confirm/disconfirm criteria and decoy-family ablations. The auditable trace-graphs with per-leaf decoy certificates are a real strength. However, the entire headline claim ('control hallucination to a user-specified alpha without labels') is load-bearing on a single assumption — that synthetic decoys are statistically exchangeable with genuinely-false LLM proposals (the proteomics 'Equal Chance Assumption') — and both the target-decoy literature and the LLM-calibration literature predict this will fail in the anti-conservative direction for the proposed decoy construction: the consequential hallucinations are PLAUSIBLE false facts that the LLM scores highly, whereas random type-matched decoys are 'too unrealistic to fool' the scorer, which the proteomics literature explicitly notes leads to UNDER-estimated FDP (realized FDR exceeds target). Three further issues compound this: (1) the per-document candidate set is tiny (~10-40 items), where TDC is known to be high-variance and the knockoff+ offset makes small alpha unachievable; (2) two of three benchmark families (RuleTaker/ProofWriter) present facts in near-symbolic form, making the extraction-precision claim near-trivial there, while the realistic setting (legal/news/story) is a small hand-annotated set that is likely underpowered for the significance claims; and (3) strong, recent, label-efficient baselines (Mohri-Hashimoto conformal factuality; conformal selection + BH; Coherent Factuality) are under-credited and not used as baselines, weakening both the novelty framing and the evaluation. None of these is necessarily fatal — the crux is directly tested and even a characterization of when ECA holds for LLM proposals would be publishable — but the decoy construction must be redesigned to target the realized hallucination distribution, the FDR claim must be re-scoped to corpus-aggregate, and the conformal baselines must be added before experiments will produce a defensible top-venue result.\",\n  \"strengths\": [\n    \"Genuinely novel cross-domain transfer: target-decoy/knockoff FDR control has lived entirely in feature selection and mass-spectrometry proteomics and (per literature search) has not been applied to LLM-proposed symbolic assertions, fuzzy unification, or neuro-symbolic reasoning. The 'fully label-free' angle is a real differentiator from conformal methods.\",\n    \"Tackles a precise, important, and well-scoped problem — quantitative hallucination control at the exact pressure point (the neural-to-symbolic admission boundary where fuzzy unification and common-sense gap-filling occur) — directly serving the ACL Knowledge Extraction trustworthiness/auditability goal.\",\n    \"Unusually honest and well-structured science: the exchangeability assumption is named as the crux, experiment (a) directly tests it (realized vs target alpha along the diagonal), decoy-family ablations (e) isolate which constructions preserve exchangeability, and the DISCONFIRMED criteria are concrete and falsifiable. A negative result would still be informative.\",\n    \"The auditable trace-graphs with provenance tags (document span vs ontology vs admitted common-sense) and a per-leaf decoy-competition certificate are a strong interpretability contribution and differentiate the work from black-box neural baselines.\",\n    \"Realistic, reproducible scope: commodity CPU, $10 LLM budget, batched joint scoring of reals+decoys, and a sensible benchmark spread (ProofWriter/RuleTaker for gold proofs, CLUTRR for paraphrased multi-hop, plus a hand-annotated realistic set).\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The core validity claim rests on decoy exchangeability (the proteomics Equal Chance Assumption), which both the TDC literature and LLM-calibration findings predict will fail in the anti-conservative direction for the proposed random/type-matched decoys: plausible hallucinations get high LLM confidence, random decoys get low confidence, so admitted-decoy counts under-estimate admitted-false-real counts and realized FDR exceeds target. Compounded by small per-document candidate counts (high-variance TDC, unachievable small alpha with the +1 offset) and an unjustified label-free score->ProbLog-probability calibration step. The design is honest and tests the crux, but as specified the central guarantee is likely to break.\",\n      \"improvements\": [\n        \"Redesign decoy construction to match the REALIZED hallucination distribution, not a random null. WHAT: generate decoys via the LLM's own plausible-but-document-contradicted counterfactual process (and lean on cross-document decoys, which are the closest to the dangerous null), rather than random same-type entity/relation swaps. HOW: prompt the LLM to fabricate maximally-plausible facts the document does NOT entail, conditioned on document context, so the decoy score distribution matches that of genuine plausible hallucinations. WHY: this is the difference between estimating the FDR of the easy null and the consequential null; it directly attacks the anti-conservative failure mode and could move the calibration curve onto the diagonal (large soundness impact).\",\n        \"Add a direct ECA diagnostic on a labeled probe set BEFORE trusting any calibration curve. WHAT/HOW: on a held-out labeled slice, compare the score distributions of KNOWN-false reals vs their decoys (e.g., two-sample test, win-rate of decoy over false real should be ~0.5). WHY: turns the central assumption from hoped-for into measured, and tells you which decoy family (if any) achieves exchangeability.\",\n        \"Re-scope the FDR claim from per-document to corpus-aggregate and report the achievable-alpha floor. WHY: per-document TDC with ~10-40 items and the knockoff+ offset cannot deliver small alpha; aggregate control is statistically meaningful and honestly reportable.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"Clear, well-organized, with precise terminology, a strong related-work section, and explicit confirm/disconfirm criteria. Main deductions: the framing oversells a 'guarantee' that is actually conditional on an empirically fragile assumption, and it lumps all conformal methods as 'needs labels / certifies single answers,' which under-credits recent label-efficient claim-level conformal FDR work.\",\n      \"improvements\": [\n        \"Soften 'controls hallucination to a user-specified alpha WITHOUT labels' to a conditional claim ('controls... PROVIDED engineered decoys satisfy exchangeability, which we test'). WHY: a top reviewer will otherwise read the unconditional guarantee as overclaiming.\",\n        \"Sharpen the true novelty wedge: not 'no one does tunable claim-level alpha' (Mohri-Hashimoto already does, with very few labels) but 'fully label-free + gates the neural->symbolic interface + propagates through symbolic deduction with per-leaf certificates.' WHY: a precise wedge is more credible and harder to attack.\",\n        \"State explicitly the dependency on the commodity upper-ontology slice for typed decoys and bridge licensing, since the abstract claims 'without a trusted ontology of constraints' — clarify it needs typing, not constraints.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"Original idea attacking a meaningful problem with potential community value (a tunable, auditable hallucination knob for text-to-logic). The contribution is somewhat de-risked by the validity question, but even a careful characterization of when/if ECA can be engineered for LLM proposals, plus the auditable-trace contribution, would be valuable. Held back from 4 by the missing strong baselines and the benchmark mismatch that limits how convincingly the headline claims can be demonstrated.\",\n      \"improvements\": [\n        \"Add Mohri-Hashimoto conformal factuality, conformal selection + BH, and a Coherent-Factuality-style multi-step variant as BASELINES (not just related work), at matched label budget. WHY: directly demonstrates the value of label-free-ness and situates the contribution against the actual state of the art (large contribution+rigor impact).\",\n        \"Position the work as complementary to ontology-constraint filtering and conformal calibration (it already argues this) and show a hybrid (decoy-gate + conformal) ablation. WHY: turns a potential 'why not just use conformal' rejection into a contribution.\",\n        \"Commit to releasing the decoy-generation prompts, the calibration harness, and the hand-annotated realistic dataset. WHY: reproducible artifacts raise contribution at KE/NeSy venues.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"Exchangeability (the proteomics Equal Chance Assumption) is the single load-bearing assumption, and as specified the decoy construction is likely to violate it in the ANTI-CONSERVATIVE direction. The TDC literature is explicit: if decoys are 'too unrealistic to fool the search engine,' FDP is UNDER-estimated. The LLM-calibration literature shows models assign HIGH confidence to plausible hallucinations. The dangerous false reals are precisely the plausible ones (e.g., a reasonable-sounding inference the document never states); random same-type entity/relation-swap decoys are easy negatives that the LLM will score low. So admitted decoys will under-count admitted false reals, the estimated FDR will be optimistic, and realized FDR will exceed target — the opposite of the claimed control. The decoys are exchangeable with the WRONG (easy) null.\",\n      \"suggested_action\": \"Generate decoys that match the realized hallucination distribution: have the LLM fabricate maximally-plausible, document-conditioned counterfactual facts/bridges/rules (and emphasize cross-document decoys), rather than random type-matched swaps. Then validate ECA directly on a labeled probe set by checking that a known-false real and its matched decoy each win the score competition ~50% of the time; only proceed to the calibration sweep for decoy families that pass this test. Report the win-rate per decoy family as a first-class result.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"Strong, recent, label-efficient baselines are under-credited and not used as baselines. Mohri & Hashimoto (ICML 2024, 'Language Models with Conformal Factuality Guarantees') already filters claims to a user-specified factuality alpha with 'very few human-annotated samples'; conformal selection (Jin & Candes) applies BH to conformal p-values for FDR-controlled selection; 'Conformal LM Reasoning with Coherent Factuality' (2505.17126) handles multi-step dependency graphs. The hypothesis characterizes conformal methods as needing a labeled calibration set and certifying only single answers, which is no longer accurate for claim-level/set-level conformal factuality. This weakens both the novelty framing and the empirical comparison.\",\n      \"suggested_action\": \"Add conformal factuality (Mohri-Hashimoto) and conformal-selection+BH as explicit baselines at a matched (small) label budget, plus a multi-step coherent-factuality variant for the deduction experiment. Re-sharpen the novelty claim to the genuine wedge: fully label-free control that gates the neural->symbolic interface and propagates through symbolic deduction with auditable per-leaf certificates. Cite these works in related work and explain precisely what each cannot do that decoy-gating can.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"Small candidate count per document undermines per-document FDR control. A ~3000-character document yields perhaps 10-40 candidate facts; target-decoy/knockoff estimates are high-variance at this scale (the proteomics literature flags decoy-induced variability as 'particularly problematic for smaller FDR thresholds, data sets, or databases'), and the knockoff+ '+1' offset makes small alpha unachievable (with k discoveries the minimum non-trivial FDR is ~1/(k+1), so e.g. alpha=0.05 requires ~20+ admissions). The success criterion 'realized FDR tracks target along the diagonal per dataset family' is therefore ill-posed at the per-document level the abstract claims.\",\n      \"suggested_action\": \"State explicitly that control is corpus-aggregate (pooled over documents), and report the achievable-alpha floor as a function of candidate count. Show the calibration diagonal on pooled discoveries, and report per-document variance separately. Consider grouping facts across documents within a dataset to increase the effective number of hypotheses where the application allows.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"major\",\n      \"description\": \"Benchmark mismatch for the extraction-precision claim. RuleTaker/ProofWriter present facts and rules already in near-symbolic, templated form, so 'atomic-fact extraction precision/recall' is near-trivial there and does not stress the hallucination gate; the gate's value only appears under paraphrase and genuine textual ambiguity. CLUTRR (paraphrased relations) is the meaningful synthetic test, and the realistic legal/news/story setting is where the contribution actually matters — but that set is described as 'small hand-annotated,' which is likely underpowered for the strong significance claims in success criterion (2).\",\n      \"suggested_action\": \"Use RuleTaker/ProofWriter primarily for the reasoner-propagation experiment (where gold proofs are the asset), not for the headline extraction-PR claim. Enlarge the realistic annotated set (or add a paraphrased/back-translated RuleTaker variant) to obtain adequate power, run a power analysis for the precision/hallucination-rate comparisons, and restrict the strong extraction-PR significance claims to CLUTRR and the realistic set.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"The ProbLog probabilities are to be 'set from calibrated scores,' but in a fully label-free regime there is no mechanism that calibrates raw LLM scores to probabilities — decoy competition yields a SET-level FDR, not a per-fact probability. Mapping decoy-competition rank to a ProbLog fact probability is currently unjustified and could silently inject miscalibration into every probabilistic conclusion.\",\n      \"suggested_action\": \"Either drop the probabilistic-reasoning arm and use crisp admit/reject (cleanest), or specify an explicit, documented monotone score->probability map (e.g., isotonic on a small labeled probe, or a fixed heuristic), and ablate its effect on conclusion accuracy so the contribution of the probability mapping is separated from the gate itself.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"'Matched recall' comparisons across CoT, RAG, LINC/Logic-LM are not operationalized. These baselines do not naturally produce an atomic-fact precision-recall curve (CoT/RAG emit free-form text; LINC emits a single translation), so equalizing recall to compare precision is underspecified and could be gamed.\",\n      \"suggested_action\": \"Specify the recall-matching protocol: for the gated method sweep the admission threshold to trace a full PR curve; for free-form baselines define a claim-extraction-and-matching protocol (e.g., decompose outputs into atomic claims, match to gold by entailment) and report full PR curves with confidence intervals rather than single matched-recall points.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"Decoys are required to be 'guaranteed NOT entailed by the document,' but verifying non-entailment is itself an error-prone extraction/reasoning step. A same-type entity 'absent from the document' may be entailed via admitted common-sense, and a 'not-stated' relation may follow by deduction — contaminating the negative controls and biasing the FDR estimate.\",\n      \"suggested_action\": \"Define and validate the non-entailment check explicitly (e.g., symbolic non-derivability against the admitted KB plus a human/LLM entailment audit on a sample), and report the contamination rate of decoys that turn out to be entailed. Exclude or down-weight contaminated decoys and quantify the effect on the calibration curve.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The propagation claim ('tightening alpha monotonically and predictably reduces multi-hop hallucination') is optimistic: a single false admitted fact can fan out to many false conclusions (amplification), conclusions are conjunctions of admitted facts/rules, and the symbolic reasoner is exact, so conclusion-level error is a nonlinear function of fact-level FDR, not a smooth monotone transfer. Assumption (d) (deduction error dominated by admitted facts/rules) is plausible but should be argued, not asserted.\",\n      \"suggested_action\": \"Add a small analytical or Monte-Carlo model linking fact-level FDR to conclusion-level error under the actual proof structures (fan-out, conjunction depth) to set quantitative expectations for experiment (d), and measure amplification empirically (false conclusions per false admitted fact). This makes 'predictable propagation' a tested quantity rather than a hope.\"\n    }\n  ],\n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": null,\n  \"relation_rationale\": \"\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [27] TOOL CALL — Bash · 2026-06-16 03:24:23 UTC

```
Validate output JSON structure:
python3 -c "import json; d=json.load(open('.terminal_claude_agent_struct_out.json')); print('valid JSON'); print('score',d['score'],'conf',d['confidence']); print('critiques',len(d['critiques']),'majors',sum(1 for c in d['critiques'] if c['severity']=='major')); print('dims',[(x['dimension'],x['score']) for x in d['dimension_scores']]); print('relation_type',d['relation_type'])"
```

### [28] TOOL RESULT — Bash · 2026-06-16 03:24:23 UTC

```
{"stdout": "valid JSON\nscore 5 conf 4\ncritiques 8 majors 4\ndims [('soundness', 2), ('presentation', 3), ('contribution', 3)]\nrelation_type None", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [29] ASSISTANT · 2026-06-16 03:24:43 UTC

```
Output is valid (score 5, confidence 4, 8 critiques with 4 majors, relation_type null for iteration 1). Let me record the review outcome to memory for downstream iterations.
```

### [30] TOOL CALL — Edit · 2026-06-16 03:24:43 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
OLD: Output written to run dir `.terminal_claude_agent_struct_out.json`.
NEW: Output written to run dir `.terminal_claude_agent_struct_out.json`.

**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:
1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: "too unrealistic to fool" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.
2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to "fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates."
3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.
4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.
Minors: label-free score→ProbLog-prob mapping unjustified; "matched recall" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).
```

### [31] TOOL RESULT — Edit · 2026-06-16 03:24:43 UTC

```
{"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "oldString": "Output written to run dir `.terminal_claude_agent_struct_out.json`.", "newString": "Output written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).", "originalFile": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n", "structuredPatch": [{"oldStart": 16, "oldLines": 3, "newStart": 16, "newLines": 10, "lines": [" **Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.", " ", " Output written to run dir `.terminal_claude_agent_struct_out.json`.", "+", "+**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:", "+1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.", "+2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"", "+3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.", "+4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.", "+Minors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1)."]}], "userModified": false, "replaceAll": false}
```

### [32] ASSISTANT · 2026-06-16 03:24:55 UTC

```
Review complete and written to `.terminal_claude_agent_struct_out.json`.

## Summary

**Overall: 5/10 (Borderline Accept), confidence 4.** Soundness 2 · Presentation 3 · Contribution 3. First iteration → `relation_type` null.

This is a genuinely original Level-3 cross-domain transfer (knockoff/target-decoy FDR control → the neural-to-symbolic admission boundary) attacking an important, well-scoped problem, and it's unusually honest about testing its own crux. But the headline guarantee is fragile in a way the literature actually predicts.

**The four major, score-blocking issues:**

1. **Exchangeability will likely fail anti-conservatively (the #1 risk).** The proteomics Equal Chance Assumption says decoys "too unrealistic to fool the scorer" → FDP *under*-estimated. The dangerous hallucinations are *plausible* facts that LLMs score with high confidence; the proposed random type-matched decoys are easy negatives scored low → admitted decoys undercount false reals → realized FDR *exceeds* target (the opposite of the claim). **Fix:** decoys must be LLM-fabricated plausible-but-contradicted counterfactuals matched to the realized hallucination distribution, plus a direct ECA diagnostic (false-real vs decoy win-rate ≈ 0.5) on a labeled probe *before* trusting any calibration curve.

2. **Missing label-efficient baselines undercut both novelty and evaluation.** Mohri & Hashimoto (ICML 2024) already filters claims to a user-specified α with few labels; conformal selection + BH gives FDR-controlled selection; Coherent Factuality handles multi-step. These must become baselines, and the novelty wedge re-sharpened to "fully label-free + gates the neural→symbolic interface + symbolic propagation + per-leaf certificates."

3. **Tiny per-document candidate counts (~10–40)** make per-document TDC high-variance and small α unachievable (knockoff+ offset). Re-scope control to **corpus-aggregate** and report the achievable-α floor.

4. **Benchmark mismatch:** RuleTaker/ProofWriter facts are already near-symbolic, so the extraction-precision claim is near-trivial there — use them for proof-propagation only; the realistic legal/news set carrying the real claim is small and likely underpowered (enlarge + power-analyze).

Plus four minors (unjustified score→ProbLog-probability mapping; under-operationalized "matched recall"; error-prone decoy non-entailment verification; nonlinear fan-out propagation). I grounded all of this in the target-decoy and conformal-factuality literature, and updated the project memory with the verdict so downstream iterations can act on the fixes without re-deriving them.
```
