# review_hypo — create_idea

> Phase: `hypo_loop` · round 2 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 03:31:48 UTC

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

### [2] HUMAN-USER prompt · 2026-06-16 03:31:48 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-16 03:37:12 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same TDC/knockoff FDR-gating frame; sharpened decoys to plausibility-matched and added entrapment validation + conformal baselines.' is too long (at most 120 characters, got 131)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
