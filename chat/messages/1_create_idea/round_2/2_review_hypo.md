# review_hypo — create_idea

> Phase: `hypo_loop` · round 2 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 03:31:42 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 03:31:48 UTC

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
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<previous_hypothesis>
The hypothesis from the PREVIOUS iteration (before the revision under review).
Use this to classify how the current hypothesis relates to it (see the H↔H
edge instructions in the task).

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

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (rigor) Exchangeability (the proteomics Equal Chance Assumption) is the single load-bearing assumption, and as specified the decoy construction is likely to violate it in the ANTI-CONSERVATIVE direction. The TDC literature is explicit: if decoys are 'too unrealistic to fool the search engine,' FDP is UNDER-estimated. The LLM-calibration literature shows models assign HIGH confidence to plausible hallucinations. The dangerous false reals are precisely the plausible ones (e.g., a reasonable-sounding inference the document never states); random same-type entity/relation-swap decoys are easy negatives that the LLM will score low. So admitted decoys will under-count admitted false reals, the estimated FDR will be optimistic, and realized FDR will exceed target — the opposite of the claimed control. The decoys are exchangeable with the WRONG (easy) null.
  Action: Generate decoys that match the realized hallucination distribution: have the LLM fabricate maximally-plausible, document-conditioned counterfactual facts/bridges/rules (and emphasize cross-document decoys), rather than random type-matched swaps. Then validate ECA directly on a labeled probe set by checking that a known-false real and its matched decoy each win the score competition ~50% of the time; only proceed to the calibration sweep for decoy families that pass this test. Report the win-rate per decoy family as a first-class result.
- [MAJOR] (evidence) Strong, recent, label-efficient baselines are under-credited and not used as baselines. Mohri & Hashimoto (ICML 2024, 'Language Models with Conformal Factuality Guarantees') already filters claims to a user-specified factuality alpha with 'very few human-annotated samples'; conformal selection (Jin & Candes) applies BH to conformal p-values for FDR-controlled selection; 'Conformal LM Reasoning with Coherent Factuality' (2505.17126) handles multi-step dependency graphs. The hypothesis characterizes conformal methods as needing a labeled calibration set and certifying only single answers, which is no longer accurate for claim-level/set-level conformal factuality. This weakens both the novelty framing and the empirical comparison.
  Action: Add conformal factuality (Mohri-Hashimoto) and conformal-selection+BH as explicit baselines at a matched (small) label budget, plus a multi-step coherent-factuality variant for the deduction experiment. Re-sharpen the novelty claim to the genuine wedge: fully label-free control that gates the neural->symbolic interface and propagates through symbolic deduction with auditable per-leaf certificates. Cite these works in related work and explain precisely what each cannot do that decoy-gating can.
- [MAJOR] (rigor) Small candidate count per document undermines per-document FDR control. A ~3000-character document yields perhaps 10-40 candidate facts; target-decoy/knockoff estimates are high-variance at this scale (the proteomics literature flags decoy-induced variability as 'particularly problematic for smaller FDR thresholds, data sets, or databases'), and the knockoff+ '+1' offset makes small alpha unachievable (with k discoveries the minimum non-trivial FDR is ~1/(k+1), so e.g. alpha=0.05 requires ~20+ admissions). The success criterion 'realized FDR tracks target along the diagonal per dataset family' is therefore ill-posed at the per-document level the abstract claims.
  Action: State explicitly that control is corpus-aggregate (pooled over documents), and report the achievable-alpha floor as a function of candidate count. Show the calibration diagonal on pooled discoveries, and report per-document variance separately. Consider grouping facts across documents within a dataset to increase the effective number of hypotheses where the application allows.
- [MAJOR] (scope) Benchmark mismatch for the extraction-precision claim. RuleTaker/ProofWriter present facts and rules already in near-symbolic, templated form, so 'atomic-fact extraction precision/recall' is near-trivial there and does not stress the hallucination gate; the gate's value only appears under paraphrase and genuine textual ambiguity. CLUTRR (paraphrased relations) is the meaningful synthetic test, and the realistic legal/news/story setting is where the contribution actually matters — but that set is described as 'small hand-annotated,' which is likely underpowered for the strong significance claims in success criterion (2).
  Action: Use RuleTaker/ProofWriter primarily for the reasoner-propagation experiment (where gold proofs are the asset), not for the headline extraction-PR claim. Enlarge the realistic annotated set (or add a paraphrased/back-translated RuleTaker variant) to obtain adequate power, run a power analysis for the precision/hallucination-rate comparisons, and restrict the strong extraction-PR significance claims to CLUTRR and the realistic set.
- [MINOR] (methodology) The ProbLog probabilities are to be 'set from calibrated scores,' but in a fully label-free regime there is no mechanism that calibrates raw LLM scores to probabilities — decoy competition yields a SET-level FDR, not a per-fact probability. Mapping decoy-competition rank to a ProbLog fact probability is currently unjustified and could silently inject miscalibration into every probabilistic conclusion.
  Action: Either drop the probabilistic-reasoning arm and use crisp admit/reject (cleanest), or specify an explicit, documented monotone score->probability map (e.g., isotonic on a small labeled probe, or a fixed heuristic), and ablate its effect on conclusion accuracy so the contribution of the probability mapping is separated from the gate itself.
- [MINOR] (methodology) 'Matched recall' comparisons across CoT, RAG, LINC/Logic-LM are not operationalized. These baselines do not naturally produce an atomic-fact precision-recall curve (CoT/RAG emit free-form text; LINC emits a single translation), so equalizing recall to compare precision is underspecified and could be gamed.
  Action: Specify the recall-matching protocol: for the gated method sweep the admission threshold to trace a full PR curve; for free-form baselines define a claim-extraction-and-matching protocol (e.g., decompose outputs into atomic claims, match to gold by entailment) and report full PR curves with confidence intervals rather than single matched-recall points.
- [MINOR] (methodology) Decoys are required to be 'guaranteed NOT entailed by the document,' but verifying non-entailment is itself an error-prone extraction/reasoning step. A same-type entity 'absent from the document' may be entailed via admitted common-sense, and a 'not-stated' relation may follow by deduction — contaminating the negative controls and biasing the FDR estimate.
  Action: Define and validate the non-entailment check explicitly (e.g., symbolic non-derivability against the admitted KB plus a human/LLM entailment audit on a sample), and report the contamination rate of decoys that turn out to be entailed. Exclude or down-weight contaminated decoys and quantify the effect on the calibration curve.
- [MINOR] (rigor) The propagation claim ('tightening alpha monotonically and predictably reduces multi-hop hallucination') is optimistic: a single false admitted fact can fan out to many false conclusions (amplification), conclusions are conjunctions of admitted facts/rules, and the symbolic reasoner is exact, so conclusion-level error is a nonlinear function of fact-level FDR, not a smooth monotone transfer. Assumption (d) (deduction error dominated by admitted facts/rules) is plausible but should be argued, not asserted.
  Action: Add a small analytical or Monte-Carlo model linking fact-level FDR to conclusion-level error under the actual proof structures (fan-out, conjunction depth) to set quantitative expectations for experiment (d), and measure amplification empirically (false conclusions per false admitted fact). This makes 'predictable propagation' a tested quantity rather than a hope.
</previous_review>

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

STEP 3 — H↔H EDGE (only if a <previous_hypothesis> block is present):
Classify how the current hypothesis relates to the previous iteration's hypothesis
using Moulines's structuralist typology. Set ``relation_type`` to one of:
    - "evolution": refining specialised claims while keeping the same conceptual frame
    - "embedding": the previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian, incommensurable shift)
Set ``relation_rationale`` to a brief justification (≤120 chars).

If no <previous_hypothesis> is present (this is iteration 1), leave both fields
null/empty.

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

### [3] HUMAN-USER prompt · 2026-06-16 03:31:48 UTC

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

### [4] ASSISTANT · 2026-06-16 03:33:10 UTC

```
I'll review this revised hypothesis carefully. Let me first ground my review in evidence by checking novelty and key technical claims, then assess how well the revision addresses prior critiques.

Let me load the web research tools and check the user uploads.
```

### [5] TOOL CALL — ToolSearch · 2026-06-16 03:33:10 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-06-16 03:33:10 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [7] TOOL CALL — Bash · 2026-06-16 03:33:10 UTC

```
List user uploads and run directory contents:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---ITER---" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/ 2>/dev/null && echo "---RUN---" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/ 2>/dev/null
```

### [8] TOOL RESULT — Bash · 2026-06-16 03:33:10 UTC

```
{"stdout": "total 1954\ndrwxr-xr-x 2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 8 root root 2000375 Jun 16 03:25 ..\n---ITER---\ntotal 4985\ndrwxr-xr-x 4 root root 1051649 Jun 16 03:31 .\ndrwxr-xr-x 8 root root 2000375 Jun 16 03:25 ..\ndrwxr-xr-x 3 root root 1044892 Jun 16 03:25 gen_hypo\ndrwxr-xr-x 2 root root 1006756 Jun 16 03:31 review_hypo\n---RUN---\ntotal 9965\ndrwxr-xr-x   8 root root 2000375 Jun 16 03:25 .\ndrwxr-xr-x 159 root root 3011777 Jun 16 03:05 ..\ndrwxr-xr-x   2 root root       1 Jun 16 03:05 .hf_cache\n-rw-r--r--   1 root root   33758 Jun 16 03:05 .workflow_input.json\ndrwxr-xr-x   4 root root 1002340 Jun 16 03:05 config\ndrwxr-xr-x   4 root root 1101594 Jun 16 03:19 iter_1\ndrwxr-xr-x   4 root root 1051649 Jun 16 03:31 iter_2\ndrwxr-xr-x   4 root root 2000220 Jun 16 03:05 sinks\ndrwxr-xr-x   2 root root       1 Jun 16 03:05 user_uploads", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] ASSISTANT · 2026-06-16 03:33:19 UTC

```
User uploads is empty. Let me run targeted searches to verify novelty and key technical concerns.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 03:33:19 UTC

```
knockoff filter target-decoy competition false discovery rate control LLM hallucination extracted facts
```

### [11] TOOL CALL — WebSearch · 2026-06-16 03:33:19 UTC

```
entrapment experiments false discovery rate validation proteomics bias overestimate paired separate 2024 2025
```

### [12] TOOL CALL — WebSearch · 2026-06-16 03:33:19 UTC

```
conformal factuality language models guarantees labeled calibration Mohri Hashimoto claim level FDR selection
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 03:33:25 UTC

```
{"query": "knockoff filter target-decoy competition false discovery rate control LLM hallucination extracted facts", "results": [{"tool_use_id": "srvtoolu_01LigZUkx9AcRjmEKq8nphPy", "content": [{"title": "Controlling the False Discovery Rate via knockoffs: is the +1 needed?", "url": "https://www.researchgate.net/publication/360254730_Controlling_the_False_Discovery_Rate_via_knockoffs_is_the_1_needed"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}, {"title": "Local False Discovery Rate Estimation with Competition-Based Procedures   for Variable Selection", "url": "https://arxiv.org/pdf/2206.02692"}, {"title": "Controlling the False Discovery Rate via Knockoffs", "url": "https://www.researchgate.net/publication/262982872_Controlling_the_False_Discovery_Rate_via_Knockoffs"}, {"title": "Controlling the False Discovery Rate via Competition: is the +1 needed?", "url": "https://arxiv.org/pdf/2204.13248"}, {"title": "Competition-based control of the false discovery proportion", "url": "https://arxiv.org/pdf/2011.11939"}, {"title": "Group-walk: a rigorous approach to group-wise false discovery rate analysis by target-decoy competition | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii82/6701992"}, {"title": "(PDF) A theoretical foundation of the target-decoy search strategy for false discovery rate control in proteomics", "url": "https://www.researchgate.net/publication/270515531_A_theoretical_foundation_of_the_target-decoy_search_strategy_for_false_discovery_rate_control_in_proteomics"}]}, "I've performed the web search for your query. The results show substantial research on knockoff filters, target-decoy competition, and false discovery rate (FDR) control in statistical hypothesis testing and proteomics, though the results don't appear to directly address the specific combination with LLM hallucination and extracted facts.\n\nHere's a summary of what the search found:\n\n**Key Concepts from the Results:**\n\n1. **Target-Decoy Competition (TDC)**: Target-decoy competition is a commonly used method for false discovery rate control in the analysis of tandem mass spectrometry data.\n\n2. **Knockoff Filter**: The knockoff filter is a method for variable selection in regression that constructs a \"knockoff\" variable for each real variable. The knockoff variables are not (conditionally on the original variables) associated with the response, but they compete with their real counterparts in variable selection.\n\n3. **Competition-Based FDR Control**: Both TDFDR and knockoff filter divide variables into two groups through a competition procedure. Then they use the number of the \"fake\" variables to estimate that of the falsely rejected true nulls, and further, achieve the control of FDR.\n\nThe search results primarily focus on statistical applications in proteomics and variable selection rather than applications to LLM-generated content or fact extraction. If you're interested in applying these FDR control techniques to validate LLM-extracted facts, you may need more specialized literature at the intersection of these fields."], "durationSeconds": 7.494338103999995, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 03:33:25 UTC

```
{"query": "entrapment experiments false discovery rate validation proteomics bias overestimate paired separate 2024 2025", "results": [{"tool_use_id": "srvtoolu_011e7q51xwH7w3qwkCoy7Zor", "content": [{"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}, {"title": "(PDF) Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.researchgate.net/publication/381145194_Assessment_of_false_discovery_rate_control_in_tandem_mass_spectrometry_analysis_using_entrapment"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment | Nature Methods", "url": "https://www.nature.com/articles/s41592-025-02719-x"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/38895431/"}, {"title": "On the use of tandem mass spectra acquired from samples of evolutionarily distant organisms to validate methods for false discovery rate estimation - Madej - 2024 - PROTEOMICS - Wiley Online Library", "url": "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/pmic.202300398"}, {"title": "GitHub - Noble-Lab/FDRBench: Estimation of false discovery proportion for mass spectrometry proteomics data using entrapment · GitHub", "url": "https://github.com/Noble-Lab/FDRBench"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12240826/"}, {"title": "Assessment of false discovery rate control in tandem mass spectrometry analysis using entrapment", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11185562/"}]}, "I found relevant research on this topic. Here's what the search results show:\n\n## Overview\n\nA critical challenge in mass spectrometry proteomics is accurately assessing error control, especially given that software tools employ distinct methods for reporting errors, and many tools are closed-source and poorly documented.\n\n## Entrapment Methods and Overestimation Issue\n\nThree prevalent methods for validating false discovery rate (FDR) control have been identified: one invalid, one providing only a lower bound, and one valid but under-powered.\n\nRegarding the overestimation bias you asked about, the combined estimation method can often substantially overestimate the FDP (false discovery proportion), which motivated researchers to propose a complementary 'paired estimation' approach that takes advantage of sample-entrapment pairing information to reduce the conservative bias while still retaining its upper bound nature.\n\n## Entrapment Database Construction\n\nIn the 'shuffled entrapment' approach, the entrapment sequences are derived analogously to decoy sequences by shuffling the corresponding target sequences, whereas in the 'foreign entrapment' approach they are taken from the proteome of some other species.\n\n## Publication\n\nThis work was published in Nature Methods in 2025, with authors including Bo Wen, Jack Freestone, Michael Riffle, Michael J. MacCoss, William S. Noble, and Uri Keich from the University of Washington and University of Sydney."], "durationSeconds": 7.180110925000001, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 03:33:27 UTC

```
{"query": "conformal factuality language models guarantees labeled calibration Mohri Hashimoto claim level FDR selection", "results": [{"tool_use_id": "srvtoolu_016ZzUJoKVqhK3tWc49i5iWw", "content": [{"title": "GitHub - tatsu-lab/conformal-factual-lm · GitHub", "url": "https://github.com/tatsu-lab/conformal-factual-lm"}, {"title": "[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"}, {"title": "Conformal Language Model Reasoning with Coherent Factuality", "url": "https://arxiv.org/html/2505.17126"}, {"title": "(PDF) Conformal Linguistic Calibration: Trading-off between Factuality and Specificity", "url": "https://www.researchgate.net/publication/389391889_Conformal_Linguistic_Calibration_Trading-off_between_Factuality_and_Specificity"}, {"title": "Large language model validity via enhanced conformal prediction methods", "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf"}, {"title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights", "url": "https://arxiv.org/pdf/2603.16817"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}, {"title": "Language models with conformal factuality guarantees | Proceedings of the 41st International Conference on Machine Learning", "url": "https://dl.acm.org/doi/10.5555/3692070.3693538"}]}, "Based on the search results, I found relevant information about your query on conformal factuality for language models:\n\n## Key Research\n\nThe official repository for the paper \"Language Models with Conformal Factuality Guarantees\" is by Christopher Mohri and Tatsunori Hashimoto. This work proposes conformal factuality, a framework that can ensure high probability correctness guarantees for language models by connecting language modeling and conformal prediction.\n\n## Main Approach\n\nMohri & Hashimoto improve the factuality of language model generations by splitting them into subclaims and filtering low-confidence subclaims via conformal prediction. They achieve conformal factuality guarantees by filtering subclaims based on a threshold τ determined by split conformal prediction, where a subclaim is included in the filtered response if its confidence score exceeds the threshold.\n\n## Guarantees and Calibration\n\nThe method applies split conformal prediction to filter generations by removing weak claims according to some threshold calibrated to a desired error rate α. The approach provides formal guarantees while maintaining a significant portion of the original output.\n\n## Applications and Related Work\n\nThe framework has been applied to various datasets and has inspired subsequent work exploring adaptations and robustness properties across different settings."], "durationSeconds": 9.629872487, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 03:33:43 UTC

```
The searches confirm the key points. Let me do one more novelty check on recent LLM/knockoff and neuro-symbolic text-to-logic work, plus grab the entrapment estimator detail.
```

### [17] TOOL CALL — WebSearch · 2026-06-16 03:33:43 UTC

```
knockoffs conformal p-values large language model factuality FDR control selection 2025 generated claims
```

### [18] TOOL CALL — WebFetch · 2026-06-16 03:33:43 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/
Prompt: What are the three entrapment methods for FDR validation described, which is invalid / lower-bound / valid-but-underpowered, and what is the difference between combined and paired entrapment estimation? Does the paper warn that entrapment estimates can themselves be biased or share assumptions with the method being validated?
```

### [19] TOOL RESULT — WebSearch · 2026-06-16 03:33:47 UTC

```
{"query": "knockoffs conformal p-values large language model factuality FDR control selection 2025 generated claims", "results": [{"tool_use_id": "srvtoolu_01Sc39ezjZ7T1iCR3MRpTknv", "content": [{"title": "Conformal Language Model Reasoning with Coherent Factuality for ICLR 2025 - IBM Research", "url": "https://research.ibm.com/publications/conformal-language-model-reasoning-with-coherent-factuality"}, {"title": "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models", "url": "https://arxiv.org/html/2604.13991"}, {"title": "ACS: An interactive framework for conformal selection", "url": "https://arxiv.org/pdf/2507.15825"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}, {"title": "Published as a conference paper at ICLR 2025 CONFORMAL LANGUAGE MODEL REASONING", "url": "https://openreview.net/pdf?id=AJpUZd8Clb"}, {"title": "Conformal Selective Prediction with General Risk Control", "url": "https://arxiv.org/pdf/2603.24704"}, {"title": "Optimized Conformal Selection: Powerful Selective Inference After   Conformity Score Optimization", "url": "https://arxiv.org/pdf/2411.17983"}, {"title": "(PDF) Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models", "url": "https://www.researchgate.net/publication/403868268_Adaptive_Conformal_Prediction_for_Improving_Factuality_of_Generations_by_Large_Language_Models"}, {"title": "A Unified Framework for Large-Scale Inference of Classification: Error Rate Control and Optimality", "url": "https://arxiv.org/pdf/2504.07321"}]}, "Based on the search results, I found several relevant papers addressing the intersection of conformal prediction, language model factuality, and FDR control:\n\n## Key Research Areas\n\n**Conformal Prediction for LLM Factuality:**\n\nRecent work has proposed evaluating the \"factuality\" of claims decomposed from a language model generation and applying conformal prediction techniques to filter out those claims that are not factual.\n\nAn adaptive conformal prediction approach extends conformal score transformation methods to LLMs, enabling prompt-dependent calibration while retaining marginal coverage guarantees and improving conditional coverage, while naturally supporting selective prediction to filter out unreliable claims.\n\n**Coherent Factuality in Reasoning:**\n\nA conformal-prediction-based method has been developed to guarantee coherent factuality of language model outputs by applying split conformal prediction to subgraphs within a \"deducibility\" graph representing reasoning problem steps.\n\n**FDR Control and Selection:**\n\nConformal selection addresses FDR control by extending conformal inference ideas to multiple test samples, offering an automatic pipeline to construct p-values using calibration data and determine the selection set by multiple testing.\n\nThe search results include papers from 2025-2026 covering these topics, with applications ranging from long-form generation to medical question-answering and drug discovery."], "durationSeconds": 7.3778450630000005, "searchCount": 1}
```

### [20] TOOL RESULT — WebFetch · 2026-06-16 03:33:49 UTC

```
{"bytes": 276539, "code": 200, "codeText": "OK", "result": "# Three Entrapment Methods for FDR Validation\n\nThe paper identifies three main approaches:\n\n1. **Combined method** (valid upper bound): \"FDP^𝒯∪ℰ𝒯=Nℰ(1+1/r)/(N𝒯+Nℰ)\" - provides an estimated upper bound on the false discovery proportion.\n\n2. **Lower bound method** (invalid for proving control): Uses the formula without the 1/r term. The authors prove this \"represents a lower bound on the FDP\" and can only show that tools *fail* to control FDR, not that they succeed.\n\n3. **Sample method** (fundamentally flawed): \"FDP^𝒯=Nℰ⋅1/r/N𝒯\" - the authors argue this is \"inherently flawed\" because it can both over- and underestimate the true FDP unpredictably.\n\n## Combined vs. Paired Estimation\n\nThe paired method improves upon combined estimation by leveraging sample-entrapment pairing information. The authors explain that the paired method \"allow[s] us to reduce the conservative bias of the combined method while still retaining its upper bound nature.\" Paired estimation yields tighter upper bounds, particularly useful for smaller entrapment-to-target ratios.\n\n## Assumptions and Bias Concerns\n\nYes, the paper directly addresses this. Regarding circular reasoning with shuffled sequences, the authors acknowledge that \"tools often use the decoy sequences differently than they are used by the entrapment estimation methods,\" validating their approach despite potential concerns about shared assumptions between validation and analysis methods.", "durationMs": 7131, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11185562/"}
```

### [21] ASSISTANT · 2026-06-16 03:36:42 UTC

```
I now have strong evidence grounding. Key findings:

1. **Novelty confirmed**: No prior application of knockoffs/target-decoy competition to LLM-extracted facts/hallucination. The transplant to the neural-symbolic boundary is genuinely novel; the closest relatives (conformal factuality/selection) are correctly cited as baselines.
2. **Entrapment estimator subtlety (Nature Methods 2025)**: There are three entrapment estimators with different formulas — the naive "sample" form (`N_E·(1/r)/N_T`) is "inherently flawed" (can over/under-estimate), the "combined" form (`N_E(1+1/r)/(N_T+N_E)`) is a valid upper bound, and "paired" tightens it. The entrapment-to-target ratio `r` is central. The hypothesis's described estimator (admitted-entrapment / admitted-total) matches the *flawed* form.
3. **Conformal baseline framing accurate.**

All eight prior critiques were substantively addressed. My critiques are new/deeper escalations, not re-raises. Let me write the review.
```

### [22] TOOL CALL — Write · 2026-06-16 03:36:42 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is a strong, highly responsive revision that addresses essentially every major and minor critique from the previous round in substance, not just in framing. The single load-bearing weakness flagged last time — that random type-matched decoys would be 'too easy' and make the FDR anti-conservative — is now the central experimental object: decoys are redesigned as plausibility-matched (document-conditioned counterfactual and cross-document) drawn from the LLM's own prior, exchangeability is TESTED via a win-rate~0.5 probe rather than assumed, and a new label-free entrapment self-validation layer (imported from the proteomics Nature Methods 2025 line) is added. The conformal-factuality literature (Mohri-Hashimoto, Jin-Candes conformal selection, coherent factuality) is now correctly cited and used as baselines, and the novelty wedge is re-sharpened to the genuine differentiator: fully label-free OPERATION that gates the neural→symbolic interface and propagates through exact symbolic deduction with per-leaf certificates. Corpus-aggregate control with an explicit achievable-alpha floor, PR curves with CIs for matched-recall, a decoy contamination-rate audit, a fitted Monte-Carlo proof-structure propagation model, and a crisp-primary/ProbLog-ablation split all directly answer prior actions. A targeted novelty search confirms no prior application of knockoffs/target-decoy competition to LLM-proposed symbolic assertions, so the core contribution is genuinely original. The remaining concerns are now (1) feasibility: the design has ballooned into a ~6-experiment, ~10-baseline, 4-dataset program that is not credibly executable under the stated $10 / CPU-only budget without everything being underpowered; (2) a precise, evidence-grounded problem with the entrapment validation — the described estimator is the form the proteomics literature calls 'inherently flawed,' and entrapment can co-fail with decoys because both are LLM-fabricated, so 'self-validation' is necessary-but-not-sufficient; and (3) a subtlety in the win-rate diagnostic (marginal vs. tail exchangeability). None are fatal; all are addressable by triage and sharpening. The trajectory is clearly positive and the core idea is publishable-quality if the validity story is tightened and scope is triaged before burning compute.",
  "strengths": [
    "Genuinely novel cross-domain transfer: a targeted search confirms target-decoy competition / knockoffs have never been applied to LLM-proposed symbolic assertions or the neural-to-symbolic admission boundary. The plausibility-matched-decoy + entrapment combination at the fuzzy-unification interface is original and well-motivated.",
    "Exemplary responsiveness to prior review: the exchangeability crux is now tested (win-rate~0.5 probe), the decoy redesign (plausibility-matched / cross-document, with random swaps retained as a deliberately-failing baseline) is a falsifiable mechanism claim, and a decoy-family showdown is a first-class experiment rather than an afterthought.",
    "Intellectual honesty about the central risk: the hypothesis explicitly does NOT assume exchangeability, reports per-family where it holds/fails in the anti-conservative direction, and pre-commits that a clean negative characterization ('cross-document decoys pass on narrative but fail on legal text') is itself a reportable contribution — a well-designed hypothesis that yields insight regardless of outcome.",
    "Correct, current contextualization of the strongest baselines (Mohri-Hashimoto conformal factuality, Jin-Candes conformal selection+BH, coherent factuality) with a defensible, sharply stated wedge (label-free operation, interface-level gating, symbolic propagation with per-leaf certificates), plus a hybrid decoy+conformal ablation.",
    "Rigorous statistical hygiene relative to the prior version: corpus-aggregate control with an explicit achievable-alpha floor as a function of candidate count; PR curves with bootstrap CIs and a claim-decomposition protocol for free-form baselines; an explicit non-entailment check with reported decoy contamination rate; crisp deduction as primary with the ProbLog/isotonic map quarantined as an ablation so calibration cannot be confused with the gate.",
    "Treats propagation as a tested, not hoped-for, quantity: a Monte-Carlo proof-structure model (fan-out, conjunction depth) is fit and tested against measured amplification on actual ProofWriter/CLUTRR proof DAGs."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "The methodology is now careful, self-aware, and tests its own crux rather than assuming it; validity is operationalized through three cross-checks (win-rate probe, entrapment, gold). Residual soundness gaps keep it from excellent: the entrapment estimator as described is the form the proteomics literature shows is unreliable; entrapment and decoys share an LLM-fabrication failure mode so their agreement is not independent confirmation; and the marginal win-rate~0.5 criterion does not guarantee tail exchangeability where admissions actually occur.",
      "improvements": [
        "Adopt the VALID entrapment estimator. The described 'admitted-entrapment / admitted-total' is the 'sample' estimator that Wen et al., Nat. Methods 2025 prove can both over- and under-estimate the FDP. Switch to the combined upper-bound form FDP_hat = N_E(1 + 1/r)/(N_T + N_E) (or the tighter paired form), explicitly choose and report the entrapment-to-target ratio r, and account for r in the variance. WHY: without this, the headline 'self-validation' is built on a known-flawed estimator and could silently endorse an anti-conservative gate. (+1)",
        "Make entrapment and decoy generation MECHANISTICALLY INDEPENDENT so their agreement is evidential. In proteomics, entrapment (foreign proteome) is constructed differently from decoys (shuffled), which is what makes the cross-check meaningful; here both are LLM-fabricated plausible facts and can co-fail. Use foreign-document-injection / explicit-contradiction entrapment against document-conditioned-counterfactual decoys, and flag that foreign-entity entrapment is nearly redundant with the cross-document decoy family (their agreement is partly tautological). Treat entrapment as necessary-not-sufficient and report cases where entrapment agrees but gold disagrees. (+1)",
        "Condition the win-rate diagnostic on the score region near the operative admission cutoff (report decoy/false-real score CDFs and win-rate as a function of score), not just the marginal average. WHY: a family can show aggregate win-rate 0.5 yet be anti-conservative in the high-score tail where admissions happen. (+0.5)"
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "Contextualization relative to prior work is excellent and differentiation is crisp. Clarity, however, is hurt by extreme density — the core 'hypothesis' is a single ~250-word sentence and most fields are long run-ons that absorbed every prior critique inline. An expert can follow it, but the primary claim is buried under defensive elaboration.",
      "improvements": [
        "Restructure into a crisp primary claim (label-free corpus-aggregate FDR control at the neural→symbolic boundary via plausibility-matched decoys, self-validated by entrapment) plus 3-4 enumerated secondary claims (decoy-family signature, beats/matches conformal at zero labels, predictable propagation, auditable certificates). Move defensive caveats into assumptions/method. WHY: improves reviewer parse-ability and foregrounds the actual contribution. (+0.5)",
        "Add a one-line dependency diagram of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement -> propagation), so the reader sees which results are contingent on which. (+0.25)"
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "A confirmed-novel, well-motivated transfer that converts 'reduce hallucination' into a controlled, self-validated, reported quantity at exactly the right pressure point (fuzzy unification), with a defensible wedge over the strongest conformal baselines. It addresses a meaningful problem and others would build on it. Held below excellent by the contingency on exchangeability actually being achievable for LLM proposals (the most likely real-world outcome is partial/per-family) and by feasibility risk that could prevent the contribution from being convincingly demonstrated.",
      "improvements": [
        "Ensure the contribution survives a partial-exchangeability outcome by designing the decoy-family showdown and the legal-vs-narrative characterization to be the publishable core even if no family achieves full diagonal tracking. WHY: de-risks the contribution against the most probable result. (+0.5)",
        "Give the under-evaluated component (c) implicit common-sense rule gating a real gold evaluation or scope it down (see scope critique); right now the most novel/hardest gating target lacks a clean benchmark, weakening the breadth of the contribution. (+0.25)"
      ]
    }
  ],
  "critiques": [
    {
      "category": "scope",
      "severity": "major",
      "description": "Scope has ballooned far beyond what the stated resources can support. The design now spans 3 decoy families x 3 candidate types (facts/bridges/rules), ~10 baselines (several of which are themselves LLM-multi-sample-heavy: LINC majority voting, self-consistency, three conformal methods, a hybrid), 4 dataset families (ProofWriter, RuleTaker, CLUTRR, an enlarged hand-annotated legal/news/story set), full PR-curve threshold sweeps with bootstrap CIs, entrapment, an ECA labeled probe, a fitted Monte-Carlo propagation model, crisp + ProbLog arms, isotonic calibration, and a prospective power analysis — all under a <$10 LLM budget on commodity CPU. This is not credible. The likely failure mode is that everything is run too thinly, so the strong significance claims in success criterion (3) fail for statistical-power reasons rather than scientific ones, wasting the compute. This is the single biggest practical risk to the iteration.",
      "suggested_action": "Triage and pre-register the compute allocation. Designate the genuinely novel core — the decoy-family showdown + entrapment validity + calibration diagonal above the alpha-floor on CLUTRR and the realistic set — as the adequately-powered headline. Demote the full baseline bake-off (especially the multi-sample CoT/RAG/LINC and the three conformal variants) and the ProbLog/propagation arms to clearly-labeled secondary experiments run at reduced scale. Either raise the budget to a realistic figure for the headline experiments or cut the baseline set to the 2-3 most informative (a plain confidence threshold and Mohri-Hashimoto conformal factuality are the load-bearing comparisons). State explicitly what was descoped."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "The entrapment self-validation — now a headline claim ('continuously self-validated without labels') — has two concrete problems grounded in the very proteomics literature it imports. (a) Wrong estimator: the hypothesis computes 'admitted-entrapment / admitted-total' as the realized false-admission proportion. Wen et al. (Nature Methods 2025, 'Assessment of FDR control ... using entrapment') show this 'sample' form is 'inherently flawed' — it can both over- and under-estimate the FDP unpredictably. The valid upper-bound form is the combined estimator FDP_hat = N_E(1 + 1/r)/(N_T + N_E), with a tighter 'paired' variant; both depend on the entrapment-to-target ratio r, which the hypothesis never mentions. (b) Non-independence / co-failure: in proteomics, entrapment (foreign proteome) is constructed and used differently from decoys (shuffled sequences), which is what makes their agreement informative. Here BOTH decoys and entrapment are LLM-fabricated plausible-but-false facts, so they can share the same anti-conservative failure mode — two biased estimators agreeing does not validate either, and the cross-document decoy family vs foreign-entity entrapment are nearly the same construction (their agreement is partly tautological). Consequently 'self-validated, label-free control' is overstated: entrapment agreement is necessary, not sufficient.",
      "suggested_action": "Replace the naive ratio with the valid combined (or paired) entrapment estimator, explicitly select and report the entrapment-to-target ratio r, and propagate r into the achievable-alpha-floor and variance analysis. Construct entrapment by a mechanism INDEPENDENT of the decoy generator (foreign-document injection / explicit contradiction) and pair it against the document-conditioned-counterfactual decoy family specifically; note that foreign-entity entrapment vs the cross-document decoy family is a weak (near-redundant) cross-check. Frame entrapment agreement as a necessary screening test and reserve the gold-labeled probe as the true arbiter of exchangeability; add a 'co-failure detection' result reporting any case where entrapment+decoys agree but gold disagrees. Cite Wen et al. 2025 and the FDRBench framework."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "The exchangeability acceptance criterion (decoy-over-false-real win-rate ~0.5 on the labeled probe) is a MARGINAL statistic, but target-decoy / knockoff validity depends on exchangeability in the high-score TAIL near the operative admission cutoff, not on average over all matched pairs. A decoy family can exhibit aggregate win-rate ≈ 0.5 while being systematically anti-conservative exactly in the region where admissions occur (e.g., decoys match easy false reals but under-score the rare very-high-confidence plausible hallucinations that drive realized FDR). Using the marginal win-rate as the gate for which families 'pass' could therefore admit a family that fails where it matters.",
      "suggested_action": "Make the ECA diagnostic tail-aware: report the win-rate and the decoy vs known-false-real score CDFs as a function of score, and define the acceptance criterion on the cutoff region (e.g., win-rate within tolerance of 0.5 among pairs scoring above the operative threshold, plus a two-sample test of the upper-tail distributions). Connect this explicitly to the realized-vs-target diagonal in experiment (a) so the diagnostic and the calibration outcome are predicted to agree."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "Component (c), gating of IMPLICIT common-sense rules that close proof gaps, is featured prominently (it is arguably the most novel and hardest part of the contribution) but lacks a clean gold evaluation. CLUTRR's 'rules' are fixed universal kinship-composition axioms (not document-specific, effectively always-admitted, so decoy-gating them is near-trivial); ProofWriter/RuleTaker rules are explicitly stated in the text (not implicit common-sense). Neither benchmark provides gold for 'which implicit common-sense rule was needed and was it correctly admitted vs. hallucinated.' The headline FDR-control results will therefore largely reflect fact and bridge gating, while the rule-gating claim rides along unevaluated.",
      "suggested_action": "Either (i) construct a small gold set with annotated missing/implicit common-sense rules (e.g., proofs that require an unstated bridging rule, with both correct and plausible-but-wrong rule distractors) to evaluate rule-level FDR directly, or (ii) scope the primary claim to facts + fuzzy-unification bridges and explicitly label rule-gating as exploratory/qualitative until a gold benchmark exists. Report fact-, bridge-, and rule-level calibration separately so the rule claim is not silently averaged into the fact result."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "Corpus-aggregate control pools candidates across documents and applies a single target-decoy threshold over the pooled real/decoy ranking. This assumes LLM confidence scores are comparable across documents. If score scales vary by document (easy vs. hard / short vs. dense), the pooled cutoff will be dominated by high-scoring documents and a false real from an 'easy' document can out-rank decoys drawn from a 'hard' one, breaking the pooled FDR estimate even when per-document exchangeability holds.",
      "suggested_action": "Standardize or rank-normalize scores per document before pooling (or fit a per-document score transform), verify cross-document score-scale homogeneity empirically, and report a sensitivity analysis of the calibration diagonal to the normalization choice. Alternatively use a grouped/conditional procedure (e.g., group-wise target-decoy) that respects document structure."
    },
    {
      "category": "presentation",
      "severity": "minor",
      "description": "The proposal is extremely dense: the central 'hypothesis' field is a single ~250-word sentence and most fields are long run-ons in which the primary claim, the assumptions, the method, and the defensive responses to prior review are interleaved. It is comprehensive but hard to parse, and the contribution risks being obscured by elaboration — a real liability for an ACL submission's clarity score.",
      "suggested_action": "Refactor into a crisp one-sentence primary claim plus 3-4 enumerated secondary claims, with a short dependency diagram of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement -> predictable propagation). Push caveats into the assumptions/method sections. This is polish, but it materially improves how the genuine novelty reads."
    }
  ],
  "score": 6,
  "confidence": 4,
  "relation_type": "evolution",
  "relation_rationale": "Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines."
}
```

### [23] TOOL RESULT — Write · 2026-06-16 03:36:42 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is a strong, highly responsive revision that addresses essentially every major and minor critique from the previous round in substance, not just in framing. The single load-bearing weakness flagged last time — that random type-matched decoys would be 'too easy' and make the FDR anti-conservative — is now the central experimental object: decoys are redesigned as plausibility-matched (document-conditioned counterfactual and cross-document) drawn from the LLM's own prior, exchangeability is TESTED via a win-rate~0.5 probe rather than assumed, and a new label-free entrapment self-validation layer (imported from the proteomics Nature Methods 2025 line) is added. The conformal-factuality literature (Mohri-Hashimoto, Jin-Candes conformal selection, coherent factuality) is now correctly cited and used as baselines, and the novelty wedge is re-sharpened to the genuine differentiator: fully label-free OPERATION that gates the neural→symbolic interface and propagates through exact symbolic deduction with per-leaf certificates. Corpus-aggregate control with an explicit achievable-alpha floor, PR curves with CIs for matched-recall, a decoy contamination-rate audit, a fitted Monte-Carlo proof-structure propagation model, and a crisp-primary/ProbLog-ablation split all directly answer prior actions. A targeted novelty search confirms no prior application of knockoffs/target-decoy competition to LLM-proposed symbolic assertions, so the core contribution is genuinely original. The remaining concerns are now (1) feasibility: the design has ballooned into a ~6-experiment, ~10-baseline, 4-dataset program that is not credibly executable under the stated $10 / CPU-only budget without everything being underpowered; (2) a precise, evidence-grounded problem with the entrapment validation — the described estimator is the form the proteomics literature calls 'inherently flawed,' and entrapment can co-fail with decoys because both are LLM-fabricated, so 'self-validation' is necessary-but-not-sufficient; and (3) a subtlety in the win-rate diagnostic (marginal vs. tail exchangeability). None are fatal; all are addressable by triage and sharpening. The trajectory is clearly positive and the core idea is publishable-quality if the validity story is tightened and scope is triaged before burning compute.\",\n  \"strengths\": [\n    \"Genuinely novel cross-domain transfer: a targeted search confirms target-decoy competition / knockoffs have never been applied to LLM-proposed symbolic assertions or the neural-to-symbolic admission boundary. The plausibility-matched-decoy + entrapment combination at the fuzzy-unification interface is original and well-motivated.\",\n    \"Exemplary responsiveness to prior review: the exchangeability crux is now tested (win-rate~0.5 probe), the decoy redesign (plausibility-matched / cross-document, with random swaps retained as a deliberately-failing baseline) is a falsifiable mechanism claim, and a decoy-family showdown is a first-class experiment rather than an afterthought.\",\n    \"Intellectual honesty about the central risk: the hypothesis explicitly does NOT assume exchangeability, reports per-family where it holds/fails in the anti-conservative direction, and pre-commits that a clean negative characterization ('cross-document decoys pass on narrative but fail on legal text') is itself a reportable contribution — a well-designed hypothesis that yields insight regardless of outcome.\",\n    \"Correct, current contextualization of the strongest baselines (Mohri-Hashimoto conformal factuality, Jin-Candes conformal selection+BH, coherent factuality) with a defensible, sharply stated wedge (label-free operation, interface-level gating, symbolic propagation with per-leaf certificates), plus a hybrid decoy+conformal ablation.\",\n    \"Rigorous statistical hygiene relative to the prior version: corpus-aggregate control with an explicit achievable-alpha floor as a function of candidate count; PR curves with bootstrap CIs and a claim-decomposition protocol for free-form baselines; an explicit non-entailment check with reported decoy contamination rate; crisp deduction as primary with the ProbLog/isotonic map quarantined as an ablation so calibration cannot be confused with the gate.\",\n    \"Treats propagation as a tested, not hoped-for, quantity: a Monte-Carlo proof-structure model (fan-out, conjunction depth) is fit and tested against measured amplification on actual ProofWriter/CLUTRR proof DAGs.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"The methodology is now careful, self-aware, and tests its own crux rather than assuming it; validity is operationalized through three cross-checks (win-rate probe, entrapment, gold). Residual soundness gaps keep it from excellent: the entrapment estimator as described is the form the proteomics literature shows is unreliable; entrapment and decoys share an LLM-fabrication failure mode so their agreement is not independent confirmation; and the marginal win-rate~0.5 criterion does not guarantee tail exchangeability where admissions actually occur.\",\n      \"improvements\": [\n        \"Adopt the VALID entrapment estimator. The described 'admitted-entrapment / admitted-total' is the 'sample' estimator that Wen et al., Nat. Methods 2025 prove can both over- and under-estimate the FDP. Switch to the combined upper-bound form FDP_hat = N_E(1 + 1/r)/(N_T + N_E) (or the tighter paired form), explicitly choose and report the entrapment-to-target ratio r, and account for r in the variance. WHY: without this, the headline 'self-validation' is built on a known-flawed estimator and could silently endorse an anti-conservative gate. (+1)\",\n        \"Make entrapment and decoy generation MECHANISTICALLY INDEPENDENT so their agreement is evidential. In proteomics, entrapment (foreign proteome) is constructed differently from decoys (shuffled), which is what makes the cross-check meaningful; here both are LLM-fabricated plausible facts and can co-fail. Use foreign-document-injection / explicit-contradiction entrapment against document-conditioned-counterfactual decoys, and flag that foreign-entity entrapment is nearly redundant with the cross-document decoy family (their agreement is partly tautological). Treat entrapment as necessary-not-sufficient and report cases where entrapment agrees but gold disagrees. (+1)\",\n        \"Condition the win-rate diagnostic on the score region near the operative admission cutoff (report decoy/false-real score CDFs and win-rate as a function of score), not just the marginal average. WHY: a family can show aggregate win-rate 0.5 yet be anti-conservative in the high-score tail where admissions happen. (+0.5)\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"Contextualization relative to prior work is excellent and differentiation is crisp. Clarity, however, is hurt by extreme density — the core 'hypothesis' is a single ~250-word sentence and most fields are long run-ons that absorbed every prior critique inline. An expert can follow it, but the primary claim is buried under defensive elaboration.\",\n      \"improvements\": [\n        \"Restructure into a crisp primary claim (label-free corpus-aggregate FDR control at the neural→symbolic boundary via plausibility-matched decoys, self-validated by entrapment) plus 3-4 enumerated secondary claims (decoy-family signature, beats/matches conformal at zero labels, predictable propagation, auditable certificates). Move defensive caveats into assumptions/method. WHY: improves reviewer parse-ability and foregrounds the actual contribution. (+0.5)\",\n        \"Add a one-line dependency diagram of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement -> propagation), so the reader sees which results are contingent on which. (+0.25)\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"A confirmed-novel, well-motivated transfer that converts 'reduce hallucination' into a controlled, self-validated, reported quantity at exactly the right pressure point (fuzzy unification), with a defensible wedge over the strongest conformal baselines. It addresses a meaningful problem and others would build on it. Held below excellent by the contingency on exchangeability actually being achievable for LLM proposals (the most likely real-world outcome is partial/per-family) and by feasibility risk that could prevent the contribution from being convincingly demonstrated.\",\n      \"improvements\": [\n        \"Ensure the contribution survives a partial-exchangeability outcome by designing the decoy-family showdown and the legal-vs-narrative characterization to be the publishable core even if no family achieves full diagonal tracking. WHY: de-risks the contribution against the most probable result. (+0.5)\",\n        \"Give the under-evaluated component (c) implicit common-sense rule gating a real gold evaluation or scope it down (see scope critique); right now the most novel/hardest gating target lacks a clean benchmark, weakening the breadth of the contribution. (+0.25)\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"scope\",\n      \"severity\": \"major\",\n      \"description\": \"Scope has ballooned far beyond what the stated resources can support. The design now spans 3 decoy families x 3 candidate types (facts/bridges/rules), ~10 baselines (several of which are themselves LLM-multi-sample-heavy: LINC majority voting, self-consistency, three conformal methods, a hybrid), 4 dataset families (ProofWriter, RuleTaker, CLUTRR, an enlarged hand-annotated legal/news/story set), full PR-curve threshold sweeps with bootstrap CIs, entrapment, an ECA labeled probe, a fitted Monte-Carlo propagation model, crisp + ProbLog arms, isotonic calibration, and a prospective power analysis — all under a <$10 LLM budget on commodity CPU. This is not credible. The likely failure mode is that everything is run too thinly, so the strong significance claims in success criterion (3) fail for statistical-power reasons rather than scientific ones, wasting the compute. This is the single biggest practical risk to the iteration.\",\n      \"suggested_action\": \"Triage and pre-register the compute allocation. Designate the genuinely novel core — the decoy-family showdown + entrapment validity + calibration diagonal above the alpha-floor on CLUTRR and the realistic set — as the adequately-powered headline. Demote the full baseline bake-off (especially the multi-sample CoT/RAG/LINC and the three conformal variants) and the ProbLog/propagation arms to clearly-labeled secondary experiments run at reduced scale. Either raise the budget to a realistic figure for the headline experiments or cut the baseline set to the 2-3 most informative (a plain confidence threshold and Mohri-Hashimoto conformal factuality are the load-bearing comparisons). State explicitly what was descoped.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The entrapment self-validation — now a headline claim ('continuously self-validated without labels') — has two concrete problems grounded in the very proteomics literature it imports. (a) Wrong estimator: the hypothesis computes 'admitted-entrapment / admitted-total' as the realized false-admission proportion. Wen et al. (Nature Methods 2025, 'Assessment of FDR control ... using entrapment') show this 'sample' form is 'inherently flawed' — it can both over- and under-estimate the FDP unpredictably. The valid upper-bound form is the combined estimator FDP_hat = N_E(1 + 1/r)/(N_T + N_E), with a tighter 'paired' variant; both depend on the entrapment-to-target ratio r, which the hypothesis never mentions. (b) Non-independence / co-failure: in proteomics, entrapment (foreign proteome) is constructed and used differently from decoys (shuffled sequences), which is what makes their agreement informative. Here BOTH decoys and entrapment are LLM-fabricated plausible-but-false facts, so they can share the same anti-conservative failure mode — two biased estimators agreeing does not validate either, and the cross-document decoy family vs foreign-entity entrapment are nearly the same construction (their agreement is partly tautological). Consequently 'self-validated, label-free control' is overstated: entrapment agreement is necessary, not sufficient.\",\n      \"suggested_action\": \"Replace the naive ratio with the valid combined (or paired) entrapment estimator, explicitly select and report the entrapment-to-target ratio r, and propagate r into the achievable-alpha-floor and variance analysis. Construct entrapment by a mechanism INDEPENDENT of the decoy generator (foreign-document injection / explicit contradiction) and pair it against the document-conditioned-counterfactual decoy family specifically; note that foreign-entity entrapment vs the cross-document decoy family is a weak (near-redundant) cross-check. Frame entrapment agreement as a necessary screening test and reserve the gold-labeled probe as the true arbiter of exchangeability; add a 'co-failure detection' result reporting any case where entrapment+decoys agree but gold disagrees. Cite Wen et al. 2025 and the FDRBench framework.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The exchangeability acceptance criterion (decoy-over-false-real win-rate ~0.5 on the labeled probe) is a MARGINAL statistic, but target-decoy / knockoff validity depends on exchangeability in the high-score TAIL near the operative admission cutoff, not on average over all matched pairs. A decoy family can exhibit aggregate win-rate ≈ 0.5 while being systematically anti-conservative exactly in the region where admissions occur (e.g., decoys match easy false reals but under-score the rare very-high-confidence plausible hallucinations that drive realized FDR). Using the marginal win-rate as the gate for which families 'pass' could therefore admit a family that fails where it matters.\",\n      \"suggested_action\": \"Make the ECA diagnostic tail-aware: report the win-rate and the decoy vs known-false-real score CDFs as a function of score, and define the acceptance criterion on the cutoff region (e.g., win-rate within tolerance of 0.5 among pairs scoring above the operative threshold, plus a two-sample test of the upper-tail distributions). Connect this explicitly to the realized-vs-target diagonal in experiment (a) so the diagnostic and the calibration outcome are predicted to agree.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"Component (c), gating of IMPLICIT common-sense rules that close proof gaps, is featured prominently (it is arguably the most novel and hardest part of the contribution) but lacks a clean gold evaluation. CLUTRR's 'rules' are fixed universal kinship-composition axioms (not document-specific, effectively always-admitted, so decoy-gating them is near-trivial); ProofWriter/RuleTaker rules are explicitly stated in the text (not implicit common-sense). Neither benchmark provides gold for 'which implicit common-sense rule was needed and was it correctly admitted vs. hallucinated.' The headline FDR-control results will therefore largely reflect fact and bridge gating, while the rule-gating claim rides along unevaluated.\",\n      \"suggested_action\": \"Either (i) construct a small gold set with annotated missing/implicit common-sense rules (e.g., proofs that require an unstated bridging rule, with both correct and plausible-but-wrong rule distractors) to evaluate rule-level FDR directly, or (ii) scope the primary claim to facts + fuzzy-unification bridges and explicitly label rule-gating as exploratory/qualitative until a gold benchmark exists. Report fact-, bridge-, and rule-level calibration separately so the rule claim is not silently averaged into the fact result.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"Corpus-aggregate control pools candidates across documents and applies a single target-decoy threshold over the pooled real/decoy ranking. This assumes LLM confidence scores are comparable across documents. If score scales vary by document (easy vs. hard / short vs. dense), the pooled cutoff will be dominated by high-scoring documents and a false real from an 'easy' document can out-rank decoys drawn from a 'hard' one, breaking the pooled FDR estimate even when per-document exchangeability holds.\",\n      \"suggested_action\": \"Standardize or rank-normalize scores per document before pooling (or fit a per-document score transform), verify cross-document score-scale homogeneity empirically, and report a sensitivity analysis of the calibration diagonal to the normalization choice. Alternatively use a grouped/conditional procedure (e.g., group-wise target-decoy) that respects document structure.\"\n    },\n    {\n      \"category\": \"presentation\",\n      \"severity\": \"minor\",\n      \"description\": \"The proposal is extremely dense: the central 'hypothesis' field is a single ~250-word sentence and most fields are long run-ons in which the primary claim, the assumptions, the method, and the defensive responses to prior review are interleaved. It is comprehensive but hard to parse, and the contribution risks being obscured by elaboration — a real liability for an ACL submission's clarity score.\",\n      \"suggested_action\": \"Refactor into a crisp one-sentence primary claim plus 3-4 enumerated secondary claims, with a short dependency diagram of the claim chain (exchangeability -> valid FDR estimate -> entrapment agreement -> predictable propagation). Push caveats into the assumptions/method sections. This is polish, but it materially improves how the genuine novelty reads.\"\n    }\n  ],\n  \"score\": 6,\n  \"confidence\": 4,\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [24] ASSISTANT · 2026-06-16 03:36:52 UTC

```
Let me validate the JSON output is well-formed.
```

### [25] TOOL CALL — Bash · 2026-06-16 03:36:52 UTC

```
Validate output JSON structure and key fields:
python3 -c "import json; d=json.load(open('.terminal_claude_agent_struct_out.json')); print('valid JSON'); print('keys:', list(d.keys())); print('score:', d['score'], '| confidence:', d['confidence']); print('relation:', d['relation_type']); print('n_critiques:', len(d['critiques']), '| severities:', [c['severity'] for c in d['critiques']]); print('n_strengths:', len(d['strengths']), '| n_dims:', len(d['dimension_scores']))"
```

### [26] TOOL RESULT — Bash · 2026-06-16 03:36:52 UTC

```
{"stdout": "valid JSON\nkeys: ['overall_assessment', 'strengths', 'dimension_scores', 'critiques', 'score', 'confidence', 'relation_type', 'relation_rationale']\nscore: 6 | confidence: 4\nrelation: evolution\nn_critiques: 6 | severities: ['major', 'major', 'major', 'minor', 'minor', 'minor']\nn_strengths: 6 | n_dims: 3", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] ASSISTANT · 2026-06-16 03:37:09 UTC

```
Review complete and written to `.terminal_claude_agent_struct_out.json` (valid, schema-conformant).

## Summary

This is a **strong, highly responsive revision** — I scored it **6/10 (Weak Accept), confidence 4**, up meaningfully from the prior round. The author addressed all eight previous critiques in substance:

- **Exchangeability** is now the central tested object (plausibility-matched/cross-document decoys, win-rate~0.5 probe, random swaps demoted to a deliberately-failing baseline).
- **Conformal baselines** (Mohri-Hashimoto, Jin-Candes, coherent factuality) are correctly cited and added, with a sharpened label-free wedge.
- **Corpus-aggregate control + alpha-floor, PR curves with CIs, contamination-rate audit, Monte-Carlo propagation model, crisp-primary/ProbLog-ablation** all directly answer prior actions.

A novelty search **confirmed** no prior application of knockoffs/target-decoy to LLM-proposed symbolic assertions — the core transfer is genuinely original.

My new critiques (not re-raises) are:

1. **[MAJOR scope]** Scope ballooned to ~6 experiments × ~10 baselines × 4 datasets — not credibly executable under $10/CPU-only without everything being underpowered. Triage and pre-register compute.
2. **[MAJOR rigor]** Evidence-grounded entrapment problem: the described estimator (`admitted-entrapment/admitted-total`) is the form Nature Methods 2025 calls "inherently flawed" — must use the valid combined/paired estimator with the entrapment-to-target ratio `r`; and entrapment can *co-fail* with decoys since both are LLM-fabricated, so agreement is necessary-not-sufficient.
3. **[MAJOR rigor]** Win-rate~0.5 is marginal, but TDC validity depends on *tail* exchangeability near the admission cutoff.
4. **[MINOR]** Implicit common-sense rule gating (component c) lacks a clean gold benchmark; cross-document pooling needs score normalization; the prose is extremely dense.

Classified the H↔H edge as **evolution** — same TDC/knockoff frame, sharpened decoy design plus added entrapment/conformal layers.
```

### [28] SYSTEM-USER prompt · 2026-06-16 03:37:12 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines.' is too long (at most 120 characters, got 131)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [29] ASSISTANT · 2026-06-16 03:37:22 UTC

```
The `relation_rationale` exceeds 120 characters. Let me shorten it.
```

### [30] TOOL CALL — Edit · 2026-06-16 03:37:22 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines."
NEW:   "relation_rationale": "Same TDC/knockoff gating frame; sharpened decoys to plausibility-matched, added entrapment validation."
```

### [31] TOOL RESULT — Edit · 2026-06-16 03:37:22 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines.\"", "newString": "  \"relation_rationale\": \"Same TDC/knockoff gating frame; sharpened decoys to plausibility-matched, added entrapment validation.\"", "originalFile": null, "structuredPatch": [{"oldStart": 79, "oldLines": 5, "newStart": 79, "newLines": 5, "lines": ["   \"score\": 6,", "   \"confidence\": 4,", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines.\"", "+  \"relation_rationale\": \"Same TDC/knockoff gating frame; sharpened decoys to plausibility-matched, added entrapment validation.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [32] TOOL CALL — Bash · 2026-06-16 03:37:26 UTC

```
Verify JSON valid and rationale length under 120:
python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_2/review_hypo/.terminal_claude_agent_struct_out.json')); r=d['relation_rationale']; print('valid JSON'); print('relation_rationale len:', len(r)); print(r)"
```

### [33] TOOL RESULT — Bash · 2026-06-16 03:37:26 UTC

```
{"stdout": "valid JSON\nrelation_rationale len: 102\nSame TDC/knockoff gating frame; sharpened decoys to plausibility-matched, added entrapment validation.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [34] ASSISTANT · 2026-06-16 03:37:29 UTC

```
Fixed. The `relation_rationale` is now 102 characters (under the 120 limit), and the JSON remains valid and schema-conformant. The review is complete.
```
