# review_hypo — create_idea

> Phase: `hypo_loop` · round 5 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 04:06:43 UTC

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
  Plausibility-Matched Decoy Competition for Label-Free FDR Control at the Text-to-Logic Admission Boundary: A Pilot-Gated,
  Tail-Validated Test of When LLM Counterfactual Decoys Achieve Exchangeability
hypothesis: |-
  PLAIN STATEMENT. When an LLM turns a short (~3000-char) document into Prolog FACTS and fuzzy-unification BRIDGE rules (Horn clauses that align a document predicate to an ontology/rule predicate when strict unification fails), force every proposed fact and bridge to out-score a PLAUSIBILITY-MATCHED synthetic decoy before it is admitted to the knowledge base, and pick the admission cutoff by target-decoy / knockoff+ competition. The decoy is a document-conditioned counterfactual: content the model finds plausible but the document does not entail. We hypothesize this controls the corpus-aggregate false-admission rate (FDR) of the resulting knowledge base to a user-specified target alpha WITH NO ground-truth labels, IN THE DEMONSTRABLE-ALPHA REGIME defined below, and ONLY where decoys are exchangeable with realized hallucinations in the high-score TAIL where admissions occur.

  STATUS OF THE CLAIM. Unlike Model-X knockoffs (exchangeable by construction) or shuffled-sequence proteomics decoys (with an equal-chance argument), LLM counterfactual decoys carry NO theoretical exchangeability guarantee - they come from the same model whose hallucinations they mimic. We therefore frame the result as an EMPIRICALLY-VALIDATED CALIBRATION, not a proven guarantee, and make 'when does the calibration hold' the central scientific question.

  PILOT PRECONDITION (Phase 0, gates the headline budget). Before spending the headline allocation we run a cheap labeled pilot (a few dozen items) to confirm two preconditions and, if they fail, we stop and report a methods-level negative: (P1) the chosen LLM score separates entailed from non-entailed content better than chance SPECIFICALLY IN THE UPPER TAIL; (P2) a TAIL-SPECIFIC power analysis shows the planned corpus yields enough above-cutoff matched pairs to power the tail tests at the target alpha, per genre. The pilot also selects the scoring elicitation (verbalized confidence vs. logprob-derived vs. self-consistency agreement) with the best tail separation.

  DEMONSTRABLE-ALPHA REGIME (stated up front). The knockoff+ '+1' offset gives a minimum estimable FDR on the order of 1/k at k admitted items, so demonstrating control at alpha needs on the order of 1/alpha admitted targets in the pooled set; mixing entrapment at ratio r inflates the variance of the estimator and modestly raises the effective floor. We REPORT this floor as a joint function of pooled candidate count and r, and we BOUND the 'user-specified alpha' claim to the range the corpus can actually demonstrate rather than implying arbitrarily small alpha.

  SECONDARY CLAIMS (each independently testable).
    S1 - DECOY-FAMILY SIGNATURE (the mechanism). Document-conditioned counterfactual decoys approach tail-exchangeability, whereas random type-matched entity/relation swaps are 'too easy' and anti-conservative (realized FDR exceeds target). Diagnosed by a TAIL-CONDITIONED win-rate (decoy-over-known-false-real win-rate among pairs scoring above the operative cutoff, target ~0.5) plus a two-sample test of the upper-tail score CDFs.
    S2 - INDEPENDENT ENTRAPMENT CORROBORATION (necessary, not sufficient). Entrapment items built by a mechanism INDEPENDENT of the decoy generator (foreign-document injection and explicit document-contradiction) yield a valid combined-estimator upper bound FDP_hat = N_E*(1+1/r)/(N_T+N_E) (Wen et al., Nat. Methods 2025; tighter paired form at r=1) that agrees with the decoy-FDR and with gold on tail-exchangeable families. Agreement is screening evidence; a small gold probe is the arbiter, and any co-failure is itself a reported result.
    S3 - WEDGE OVER CONFORMAL. At matched recall (full PR curves with bootstrap CIs), label-free decoy-gating matches or beats (i) a plain confidence threshold and (ii) the label-using Mohri-Hashimoto conformal-factuality baseline at a small matched label budget, on atomic-fact precision and hallucinated-conclusion rate. We report the two methods' GUARANTEE STATUS side by side (conformal: a finite-sample guarantee bought with calibration labels; decoy gate: an empirically-validated calibration bought with zero operation labels) so the comparison is not read as a guarantee versus an estimate.
    S4 - PREDICTIVE ACCOUNT OF EXCHANGEABILITY (promoted from fallback; the de-risked headline if full control is only partial). Pre-registered document/score features (entity density, document specificity, tail score-separation, genre) predict WHICH decoy-family x genre combinations achieve tail-exchangeability; the model is validated OUT-OF-SAMPLE on a held-out genre. This converts the likely-partial outcome from a pass/fail table into a mechanism-level insight.
    S5 - PREDICTABLE PROPAGATION (reduced-scale). Tightening alpha reduces the multi-hop hallucinated-conclusion rate in the direction and rough magnitude predicted by a fitted fan-out/conjunction proof-structure model.

  CLAIM-CHAIN DEPENDENCY. [pilot preconditions met] -> [tail-exchangeable decoy family] -> [valid label-free corpus-aggregate FDR estimate via TDC/knockoff+ within the demonstrable-alpha regime] -> [realized FDR tracks target alpha, gold-arbitrated] -> [independent entrapment agreement = necessary corroboration] -> [controlled fact+bridge FDR propagates to reduced multi-hop hallucination]. A break at any arrow is localized and reported; downstream claims are not asserted if an upstream arrow fails. S4 (the predictive account) is reported whether or not the diagonal-tracking arrow holds.

  SCOPE (pre-registered, $10 / CPU-only). PRIMARY claims (S1-S3 plus the demonstrable-alpha report) are evaluated on FACTS and fuzzy-unification BRIDGES on CLUTRR (paraphrased multi-hop kinship, gold graph) plus a hand-annotated realistic short-document set, split by genre (legal vs. narrative). If the tail-specific power analysis shows the budget cannot adequately power BOTH genres, we pre-register narrowing the headline diagonal-tracking claim to a single genre and treating the second as exploratory. Implicit common-sense RULE gating is a separately-reported EXPLORATORY arm on a small purpose-built gold rule set; fact-, bridge-, and rule-level calibration are never averaged together. S4 (predictive account), S5 (propagation), the ProbLog/isotonic ablation, and the full bake-off (CoT, RAG, LINC, Logic-LM, conformal selection, coherent factuality) are secondary or future work.
motivation: |-
  Operational text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob at this interface: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and only catches encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, coherent factuality) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem - selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth - via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make the FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound (the combined/paired form of Wen et al., 2025), with the entrapment constructed differently from the decoys or its agreement proves nothing. Importing matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary turns 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity - directly serving the ACL Knowledge Extraction goal of trustworthy, traceable extraction.

  Crucially, the design is built to yield insight even when exchangeability holds only partially. Because LLM counterfactual decoys carry no theoretical guarantee, the most probable outcome is per-genre/per-family partial control. We therefore pre-commit to a PREDICTIVE account (S4): a model of which document and score features make tail-exchangeability achievable, validated out-of-sample. That converts the likely-partial result into a mechanism-level contribution - a strong-accept-grade insight rather than a results table - and a cheap pilot ensures we never spend the headline budget confirming a precondition (tail score-separation, adequate tail sample size) that a few dozen labeled items could have surfaced first.
assumptions:
- >-
  TAIL EXCHANGEABILITY IS ENGINEERED AND TESTED, NOT GUARANTEED. Target-decoy / knockoff validity requires a genuinely-false
  real proposal and its matched decoy to be equally likely to receive any given score in the high-score region near the admission
  cutoff. Unlike Model-X knockoffs or shuffled-sequence decoys, LLM counterfactual decoys have no construction-level proof
  of this. We therefore (a) report the result as an empirically-validated calibration, not a theorem; (b) test the condition
  in the TAIL via a tail-conditioned win-rate (~0.5 among above-cutoff pairs) and an upper-tail two-sample CDF test, not on
  marginal average; (c) corroborate label-free via independent entrapment; (d) arbitrate with a small gold probe; and (e)
  report per family and per genre where it holds or fails anti-conservatively. A family with marginal win-rate ~0.5 but anti-conservative
  tail behavior is reported as FAILING.
- >-
  A SCORE-SEPARATION PRECONDITION MUST BE MET, AND IS DE-RISKED BY A PILOT. The LLM must emit a roughly monotone score that
  separates document-entailed from non-entailed content better than chance SPECIFICALLY in the upper tail; LLM verbalized
  confidence is known to be unreliable, so we do not assume this. A Phase-0 pilot (a few dozen labeled items) verifies tail
  separation and selects the best elicitation (verbalized confidence vs. logprob-derived vs. self-consistency agreement).
  The headline budget is GATED on the pilot; if no elicitation separates in the tail, no thresholding procedure can help,
  and we report that as a methods-level precondition failure.
- >-
  ENTRAPMENT VALIDITY REQUIRES THE VALID ESTIMATOR AND CONSTRUCTION INDEPENDENCE. Realized false-admission is estimated by
  the combined upper bound FDP_hat = N_E*(1+1/r)/(N_T+N_E) (paired form at r=1), with the entrapment-to-target ratio r chosen,
  reported, and propagated into the variance and the achievable-alpha floor; the inherently-flawed naive 'sample' ratio is
  not used. Entrapment is generated by a mechanism distinct from the counterfactual decoys (foreign-document injection, explicit
  contradiction) so agreement is evidential, not tautological. Agreement is necessary, never sufficient; gold is the arbiter
  and co-failures are reported.
- >-
  THE DEMONSTRABLE-ALPHA REGIME IS BOUNDED AND REPORTED. Corpus-aggregate pooling is the unit of control, because a single
  document yields only ~10-40 candidates. The knockoff+ '+1' offset gives a minimum estimable FDR on the order of 1/k at k
  admitted items, and entrapment at ratio r inflates the estimator variance, so the smallest demonstrable alpha is a joint
  function of pooled candidate count and r. We bound the 'user-specified alpha' claim to that demonstrable range, widen it
  primarily by adding documents per genre (the cheapest lever, since extraction dominates LLM cost), choose r to balance variance
  against the floor, and report whether a less-conservative competition bound (TDC-SB/UB, arXiv 2302.11837; the '+1'-removal
  analysis, arXiv 2204.13248) lowers the floor without breaking validity. Scores are rank-normalized per document before pooling,
  with a sensitivity analysis of the diagonal to the normalization choice.
- >-
  DECOY NON-ENTAILMENT IS IMPERFECT, ITS BIAS IS CHARACTERIZED, AND 'ZERO-LABEL' IS STATED PRECISELY. The more tail-matched
  a counterfactual decoy, the higher the risk it is actually entailed or world-true-and-inferable - a target masquerading
  as a decoy. Such contamination inflates the admitted-decoy count and biases the decoy-FDR estimate CONSERVATIVE (costing
  recall), the safe direction. We report the contamination rate per family and per genre, state the direction of its effect
  on the diagonal, and quantify the diagonal's sensitivity to plausible contamination rates. The contamination audit and the
  gold probe are small LABEL costs charged symmetrically against the conformal baseline's calibration-label budget: the wedge
  is ZERO labels for OPERATION (the gate runs label-free), with a small audit/probe budget only for VALIDATION.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then make TAIL exchangeability, the demonstrable-alpha regime, and a predictive account of exchangeability the central experimental objects.

  PRE-REGISTERED BUDGET SPLIT (of $10 / CPU-only): ~10% Phase-0 PILOT (gates everything below); ~55% HEADLINE (decoy-family showdown + entrapment validity + calibration diagonal on facts+bridges over CLUTRR and the realistic set, sized by the tail-specific power analysis); ~20% load-bearing baselines (plain confidence threshold + Mohri-Hashimoto conformal factuality); ~15% secondary (S4 predictive-account modeling, exploratory rule gating, ProbLog/isotonic ablation, S5 propagation, ungated translate-then-prove ablation).

  PHASE 0 - PILOT (precondition, runs before the headline allocation). On a few dozen labeled items: (i) measure whether each candidate elicitation (verbalized confidence, logprob-derived, self-consistency agreement) separates entailed from non-entailed content better than chance IN THE UPPER TAIL; pick the best. (ii) Estimate tail density and run a TAIL-SPECIFIC power analysis: how many above-cutoff matched pairs (and admitted N_T, N_E) are needed to detect a target departure of the tail win-rate from 0.5 and to power the upper-tail two-sample test at the operative alpha, PER GENRE. Size the corpus to that target. If the budget cannot power both genres, pre-register narrowing the headline to one genre. Gate the full run on the pilot and report it as a methods precondition.

  PIPELINE.
    (1) EXTRACTION: a cheap OpenRouter LLM reads the document and proposes typed first-order facts; argument types are grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing (to constrain decoys and license bridges), not for trusted constraints - the FDR claim assumes no constraint ontology.
    (2) DECOY GENERATION: the PRIMARY family is document-conditioned counterfactual decoys (prompt the LLM to fabricate maximally-plausible facts/bridges the document does NOT entail, conditioned on the document and types). The deliberately-easy random type-matched swap family is retained as the baseline predicted to be anti-conservative. Every decoy passes an explicit non-entailment check (symbolic non-derivability against the admitted KB + an LLM/human entailment audit on a sample); we report the contamination rate, its conservative direction, and a sensitivity analysis.
    (3) ENTRAPMENT (independent construction): a held-out set of foreign-document-injection and explicit-contradiction entrapment items, false by construction and generated unlike the counterfactual decoys, is mixed in at a chosen, reported ratio r (paired with the document-conditioned-counterfactual decoy family so the two are not near-redundant).
    (4) SCORING: the LLM scores reals, decoys, and entrapment jointly in batched prompts (cost control), using the pilot-selected elicitation; scores are rank-normalized per document.
    (5) FDR GATE: target-decoy / knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges; admitted items enter the KB with a logged certificate. We also evaluate whether TDC-SB/UB or the '+1'-removal rule lowers the achievable floor without breaking validity.
    (6) ENTRAPMENT VALIDATION (label-free, necessary): the combined estimator FDP_hat = N_E*(1+1/r)/(N_T+N_E) (paired form at r=1) upper-bounds realized false-admission; compare against decoy-FDR and gold; explicitly hunt for and report co-failures.
    (7) TAIL-AWARE DIAGNOSTIC (small labeled probe, measurement only, never used by the gate): on a labeled slice, report the decoy-over-known-false-real win-rate AND the decoy vs. false-real score CDFs as a function of score, with acceptance defined on the cutoff region (win-rate within tolerance of 0.5 among above-cutoff pairs + upper-tail two-sample test).
    (8) REASONING: admitted facts/bridges populate SWI-Prolog for crisp multi-hop deduction (primary mode); backward-chaining proofs export as trace-graphs whose leaves carry provenance (document span / ontology / admitted bridge) plus the decoy-competition + entrapment certificate. A ProbLog arm with an explicit isotonic score->probability map (fit on the probe) is a secondary ablation.

  DATASETS: CLUTRR (paraphrased) + a hand-annotated set of short legal/news/kids'-story documents carry the headline facts+bridges claims, split legal vs. narrative to expose per-genre exchangeability differences; ProofWriter/RuleTaker only for S5 propagation. Gold labels are used ONLY for evaluation, the optional probe, and the contamination audit; the operational gate is label-free.

  EXPERIMENTS: (a) validity-of-control - sweep alpha within the demonstrable range, measure realized corpus-aggregate FDR via the entrapment combined estimator and gold, test diagonal tracking above the floor, report sensitivity to per-document normalization; (b) decoy-family showdown - tail win-rate + entrapment agreement per family/genre; (c) extraction PR curves vs. the load-bearing baselines on facts+bridges, with guarantee-status reported side by side; (d) [secondary] S4 predictive account - fit the exchangeability model on pre-registered features and validate out-of-sample on a held-out genre; (e) [secondary] S5 propagation and exploratory rule gating; (f) cost check (< $10, CPU-only) + qualitative auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). The Phase-0 pilot must show the selected LLM score separates entailed from non-entailed content better than chance in the upper tail AND that the corpus can power the tail tests per genre (or the headline is pre-registered down to a single genre). If the pilot fails, the reported contribution is the precondition-failure analysis plus S4.

  PRIMARY (headline, facts+bridges over CLUTRR + realistic set, within the reported demonstrable-alpha range). CONFIRMED if: (1) for at least one decoy family, realized corpus-aggregate FDR tracks target alpha within a small tolerance above the achievable-alpha floor (calibration diagonal), stable under the per-document normalization sensitivity check, AND the independent entrapment combined-estimator upper bound agrees with both the decoy estimate and gold - self-corroborated, label-free control; (2) the decoy-family showdown shows the tail signature: counterfactual decoys reach tail-conditioned win-rate ~0.5 (and pass the upper-tail two-sample test) with entrapment+gold agreement, while random swaps are measurably anti-conservative; (3) at matched recall (PR curves with CIs), decoy-gating matches or beats a plain confidence threshold AND the Mohri-Hashimoto conformal baseline at a small matched label budget on fact precision and hallucinated-conclusion rate, with zero-label operation as the wedge and guarantee status reported side by side.

  CONTRIBUTION-SURVIVES-PARTIAL (de-risk, now PREDICTIVE not descriptive). Even if no family achieves full diagonal tracking, S4 is the reportable headline: a model of which document/score features (entity density, document specificity, tail score-separation, genre) govern tail-exchangeability, fit on the studied families and VALIDATED OUT-OF-SAMPLE on a held-out genre, plus the documented co-failure cases. The bar is a predictive account that generalizes, not a pass/fail table.

  SECONDARY. (4) S5 - tightening alpha reduces multi-hop hallucination in the direction predicted by the fitted proof-structure model; (5) ablating the decoy gate measurably worsens hallucination; (6) exploratory rule-gating separates correct from plausible-but-wrong implicit rules above chance on the small gold set; (7) the pipeline runs on commodity CPU within $10 and produces auditable trace-graphs with per-leaf certificates.

  DISCONFIRMED if: the pilot preconditions hold (so the test is fair) but NO decoy family achieves tail-exchangeable, gold-arbitrated diagonal tracking on either genre within the demonstrable-alpha range (random AND counterfactual decoys both anti-conservative in the tail) AND the entrapment estimator systematically co-fails against gold AND the S4 feature model fails to predict exchangeability out-of-sample; OR decoy-gating shows no precision/hallucination advantage over a plain confidence threshold at matched recall and is dominated by conformal even accounting for its zero-label disadvantage. A characterized failure boundary plus a validated S4 model remains a contribution; an uninterpretable null (control neither clearly holds nor clearly fails, with an underpowered tail test) is the true failure - which the Phase-0 power analysis is designed to prevent.
related_works:
- >-
  Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis
  using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench): gives the theory of entrapment FDP estimation, shows the
  naive 'sample' estimator is inherently flawed, and provides the valid combined upper bound FDP_hat = N_E*(1+1/r)/(N_T+N_E)
  with a tighter paired form at r=1. We adopt this estimator wholesale, choose and report r, and propagate r into variance
  and the alpha-floor. Difference: their domain is mass-spectrometry peptide identification; we transplant the estimator AND
  the construction-independence principle to validate LLM fact/bridge admission.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023): proposes
  TDC-SB and TDC-UB, giving tighter upper prediction bounds on the false discovery PROPORTION than the Katsevich-Ramdas approach.
  We test whether these bounds lower our achievable-alpha floor without breaking validity. Difference: developed for generic
  competition-based selection / mass spectrometry; we apply it to the LLM neural-to-symbolic boundary and to widening the
  demonstrable-alpha regime.
- >-
  He, Ebadi, Keich et al., 'Controlling the false discovery rate via competition: is the +1 needed?' (arXiv 2204.13248 / Statistics
  & Probability Letters 2023): analyses the '+1' correction that creates the minimum-estimable-FDR floor in TDC/knockoff+.
  Directly relevant to whether our small-discovery alpha-floor can be relaxed. Difference: a generic competition-control result;
  we use it to characterize and potentially widen the demonstrable-alpha range at the text-to-logic interface.
- >-
  Luo, Ebadi, Crook, Noble & Keich, 'Competition-based control of the false discovery proportion' (Biometrics 79(4):3472,
  2023; FDP-SD): rigorously controls the FDP (not just average FDR) in the knockoff/TDC setup with more power than Katsevich-Ramdas.
  Considered as an alternative threshold rule. Difference: numeric/peptide selection; we adapt the FDP-control idea to per-leaf
  certificates over admitted symbolic assertions.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm that removes
  claims until a user-specified factuality alpha is met via conformal prediction with a few labeled samples. Our primary load-bearing
  baseline. Difference: it requires labeled calibration, certifies the final filtered OUTPUT rather than the neural-to-symbolic
  admission boundary, and offers no synthetic-decoy mechanism, independent entrapment, or symbolic propagation with certificates.
  We report its finite-sample guarantee vs. our empirical calibration side by side; our wedge is label-free OPERATION at the
  fuzzy-unification interface.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no labels by competing each proposal against engineered decoys and
  corroborate via independent entrapment.
- >-
  Knockoff filter (Barber & Candes, Annals of Statistics 2015; Model-X knockoffs, Candes et al. 2018) and target-decoy competition
  (proteomics): select true signals among many candidates with guaranteed FDR by competing each real variable/peptide against
  a synthetic negative control that is exchangeable BY CONSTRUCTION. Difference: this machinery lives in numeric feature selection
  and mass spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM boundary where decoys
  carry NO such guarantee, and we therefore test exchangeability empirically in the high-score tail.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, 'Generating property-matched decoy molecules using
  deep learning', Bioinformatics 2021; protein-language-model decoys): generate decoys that reproduce the score properties
  of true positives so target-decoy FDR is well-calibrated. Difference: lives entirely in molecular screening / mass spectrometry;
  we import the PRINCIPLE - decoys must reproduce the false-positive score distribution, not be 'too easy' - to design LLM
  fact/bridge decoys as document-conditioned counterfactuals, never done for LLM-proposed symbolic assertions.
- >-
  Conformal factuality for reasoning chains, 'Conformal Language Model Reasoning with Coherent Factuality' (ICLR 2025 / arXiv
  2505.17126): extends conformal factuality to dependency graphs of claims so guarantees hold coherently across reasoning
  chains, with a labeled calibration set. Difference: labeled, certifies coverage over claim graphs rather than gating which
  extracted facts/bridges enter a symbolic KB; no decoys, no independent entrapment, no label-free knob.
- >-
  LINC (Olausson et al., EMNLP 2023) and Logic-LM (Pan et al., Findings of EMNLP 2023): LLM semantic-parse premises into FOL/symbolic
  form executed by a solver, with majority voting (LINC) or solver-error self-refinement (Logic-LM). Difference: no principled
  control over WHICH extracted content is admitted - hallucinated translations enter freely; voting smooths variance and refinement
  fixes solver/syntax errors, but a syntactically valid fabricated premise is never challenged. No FDR knob, no decoys, no
  label-free precision guarantee. (Context, descoped from primary baselines.)
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING (not constraints) and controls overall false-admission rate including
  where the ontology is silent - complementary.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, sharpened across review rounds. Genomics/proteomics solved the hardest
  label-poor problem - deciding which of thousands of candidate signals are real with no ground truth - with a guaranteed
  FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry), and discovered the two ways the
  trick breaks: decoys 'too unrealistic to fool' the scorer make the FDR optimistic (cured by property-matched decoys: DeepCoy,
  protein-LM decoys), and entrapment FDP must be estimated with a valid upper bound (the combined/paired estimator of Wen
  et al., Nature Methods 2025) using entrapment built unlike the decoys. I map all three onto the exact pressure point of
  a text-to-logic pipeline - the fuzzy-unification boundary where the LLM aligns predicates and supplies background knowledge.
  Because the dangerous hallucinations are PLAUSIBLE high-confidence false facts, the decoys must be plausible counterfactuals
  from the LLM's own prior, exchangeability must be checked IN THE TAIL, and the FDR must be corroborated by independently-constructed
  entrapment and arbitrated by a small gold probe. The latest refinement borrows the competition-based FDP-bounding literature
  (TDC-SB/UB, the '+1'-removal analysis) to characterize and potentially widen the demonstrable-alpha regime. Crucially, the
  transfer is honest about its weakest joint: LLM decoys carry no construction-level exchangeability guarantee, so the contribution
  is reframed as an empirically-validated calibration plus a predictive account of WHEN that calibration holds - a mechanism-level
  insight rather than a bare control claim.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content - a document-conditioned counterfactual the model finds plausible - so its confidence-score distribution reproduces
    that of genuine plausible hallucinations. It replaces random type-matched swaps, which are 'too easy' and make the estimated
    FDR optimistic.
- term: Tail-conditioned win-rate (tail-aware diagnostic)
  definition: >-
    The decoy-over-known-false-real win-rate computed ONLY among matched pairs whose scores fall above the operative admission
    cutoff, reported with the decoy and false-real score CDFs as a function of score and an upper-tail two-sample test. Target
    ~0.5 in the tail. It supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative
    exactly where admissions occur. Measurement only, never used by the operational gate.
- term: Phase-0 pilot and tail-specific power analysis
  definition: >-
    A cheap labeled run (a few dozen items) executed BEFORE the headline budget that (a) confirms the LLM score separates
    entailed from non-entailed content better than chance in the upper tail, (b) selects the scoring elicitation with the
    best tail separation, and (c) estimates how many above-cutoff matched pairs and admitted items (N_T, N_E) are needed to
    power the tail tests per genre, sizing the corpus to that target. The headline is gated on this pilot.
- term: Demonstrable-alpha range and achievable-alpha floor
  definition: >-
    Control is asserted over candidates pooled across documents within a dataset family. The knockoff+ '+1' offset gives a
    minimum estimable FDR on the order of 1/k at k admitted items, and entrapment at ratio r inflates the estimator variance,
    so the smallest demonstrable target alpha is a joint function of pooled candidate count and r. This range is reported
    up front and bounds the 'user-specified alpha' claim; it is widened mainly by adding documents and optionally by less-conservative
    bounds (TDC-SB/UB).
- term: Combined / paired entrapment estimator and the ratio r
  definition: >-
    The valid entrapment upper bound on realized false-admission: FDP_hat = N_E*(1+1/r)/(N_T+N_E), where N_T = admitted real
    items, N_E = admitted entrapment items, and r = entrapment-to-target ratio (reported; r=1 gives the tighter paired form).
    It replaces the inherently-flawed naive 'sample' ratio. r is propagated into the variance and the achievable-alpha floor.
- term: Independent entrapment and co-failure detection
  definition: >-
    Entrapment items are built by a mechanism distinct from the decoy generator - foreign-document injection and explicit
    document-contradiction - so their agreement with the LLM-counterfactual decoy FDR is evidential, not tautological. Because
    both are LLM-handled, agreement is necessary not sufficient; the small gold probe is the arbiter, and any co-failure (entrapment+decoy
    agree but gold disagrees) is explicitly reported.
- term: Predictive exchangeability account (S4)
  definition: >-
    A pre-registered model that predicts which decoy-family x genre combinations achieve tail-exchangeability from document/score
    features (entity density, document specificity, tail score-separation, genre), validated out-of-sample on a held-out genre.
    It elevates the likely-partial outcome from a descriptive pass/fail table to a mechanism-level, generalizable insight.
- term: Empirically-validated calibration (vs. proven guarantee)
  definition: >-
    The status of the FDR-control claim. Unlike Model-X knockoffs (exchangeable by construction) or shuffled-sequence proteomics
    decoys (with an equal-chance argument), LLM counterfactual decoys carry no theoretical exchangeability guarantee. The
    control is therefore an empirically-validated calibration whose validity is tested in the tail and corroborated by entrapment
    - not a theorem - and is reported as such alongside the conformal baseline's finite-sample guarantee.
- term: Per-document score normalization and corpus-aggregate control
  definition: >-
    Raw LLM confidence scores need not be comparable across documents, so scores are rank-normalized per document (or a per-document
    transform is fit) before pooling for corpus-aggregate target-decoy control, with a sensitivity analysis of the calibration
    diagonal to the normalization choice. A single ~3000-char document yields too few candidates for stable per-document control.
- term: Fuzzy unification and bridge rule
  definition: >-
    Fuzzy unification matches a document predicate to a rule/ontology predicate when strict symbolic unification fails (e.g.,
    'wrote(x,y)' must satisfy a rule needing 'author_of(x,y)'). It is the chief site where hallucination enters a text-to-logic
    reasoner. Each fuzzy match is materialized as an explicit, auditable Horn-clause BRIDGE (author_of(X,Y) :- wrote(X,Y))
    admitted only if it clears the decoy gate. Facts and bridges - not implicit common-sense rules - carry the headline FDR-control
    claim.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  We gate the fuzzy-unification boundary of a text-to-logic pipeline so every LLM-proposed fact and bridge rule must out-score
  a plausibility-matched counterfactual decoy (target-decoy / knockoff+ thresholding) before entering a Prolog knowledge base,
  controlling the corpus-aggregate hallucination rate to a target alpha with NO operation labels, within an explicitly reported
  demonstrable-alpha range. A Phase-0 pilot first verifies tail score-separation and powers the tail tests; validity is tested
  in the high-score TAIL and corroborated by an independently-constructed entrapment set via the valid combined estimator
  FDP=N_E(1+1/r)/(N_T+N_E) with a small gold probe as arbiter; and because LLM decoys carry no theoretical exchangeability
  guarantee, we pre-commit to a predictive account of WHICH decoy-family x genre combinations achieve tail-exchangeability
  (validated out-of-sample) as the de-risked, mechanism-level contribution.
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (rigor) S4 (the predictive account of exchangeability) is now the de-risked headline — the deliverable that survives if full diagonal control fails — but its validation, 'fit the feature model and validate OUT-OF-SAMPLE on a held-out genre', has only two genres (legal, narrative). Leave-one-genre-out therefore means training on one genre and testing on exactly one held-out genre: n=1 generalization unit, with 'genre' itself as one of the predictive features. A feature model (entity density, document specificity, tail score-separation, genre) fit on a handful of family x genre cells and 'validated' on a single held-out genre is an anecdote, not a generalizable mechanism-level account. The safety net for the whole program is, as designed, unvalidatable — which is the most consequential issue because the hypothesis leans on S4 precisely for the most probable (partial) outcome.
  Action: Make the unit of out-of-sample validation the document, not the genre. Fit the exchangeability model on document-level and score-level features across many documents and predict per-document (and per-item) tail-exchangeability, validating with leave-one-document-cluster-out (or leave-one-source-out) cross-validation so there are many held-out units. Keep the leave-one-genre-out result as one illustrative external test, explicitly labeled as a single-unit generalization probe, not the validation. If genre-level generalization is to be a real claim, pre-register >=3-4 genres/sources and report the budget cost; otherwise drop the genre-holdout framing from the success criterion.
- [MAJOR] (methodology) The entrapment corroboration (S2) inherits the same 'too-easy -> anti-conservative' failure mode the decoy side is carefully designed to detect, but with no analogous diagnostic. Foreign-document-injection and explicit-contradiction entrapment are plausibly EASIER to reject than subtle plausible counterfactual hallucinations (off-topic entities and overt contradictions are more detectable), so admitted-entrapment N_E under-represents realized false admissions and the combined estimator FDP_hat = N_E*(1+1/r)/(N_T+N_E) under-estimates true FDP. Construction-independence guards against tautological agreement but NOT against decoys and entrapment being anti-conservative simultaneously — which makes the co-failure scenario (entrapment + decoy agree, gold disagrees) not a remote caveat but a likely outcome. As written, the only guard is the gold probe, which makes entrapment partly redundant with the very gold arbiter it is meant to reduce reliance on.
  Action: Apply the tail-difficulty diagnostic to entrapment as well as decoys: report the admitted-entrapment score distribution against gold false-reals in the high-score region and test whether entrapment is calibrated to tail difficulty (not merely construction-independent). Pre-register that entrapment whose tail score distribution is materially easier than realized false-reals is reported as an invalid (anti-conservative) corroborator. Consider designing the entrapment to be plausibility/tail-matched (still by an independent mechanism) so its evidential value survives, and state explicitly the direction of bias if it is not.
- [MAJOR] (scope) The experimental program has expanded across iterations to a point that strains the fixed $10/CPU-only budget and the (unbudgeted) human annotation labor. The must-run set already includes: a Phase-0 pilot over three elicitations (self-consistency itself multiplies LLM calls); extraction over CLUTRR plus a hand-annotated legal+narrative set sized by a tail-specific power analysis (the cheapest lever is MORE documents, each requiring the full extract -> decoy -> entrapment -> joint-score stack); two decoy families; entrapment generation; a facts-and-bridges FDR gate; and two baselines (confidence + Mohri-Hashimoto conformal at a matched label budget). Layered on top are S4, S5 propagation, exploratory rule gating, a ProbLog/isotonic ablation, TDC-SB/UB and +1-removal evaluation, and a per-document normalization sensitivity sweep — all in a 15% secondary slice. The risk is that the tail-power requirement and the breadth jointly under-power everything, producing the uninterpretable null the design explicitly fears. The hand-annotated set's size and protocol are also a reproducibility-critical detail (the original brief demands 'highly reproducible') and are unspecified.
  Action: Publish a concrete feasibility budget BEFORE committing: expected document count per genre and total LLM call count implied by the power analysis (reals + decoys + entrapment x any self-consistency multiplier x facts/bridges), priced against $10. Designate only the pilot + a single-genre headline (decoy showdown + entrapment + calibration diagonal) + the two baselines as confirmatory must-runs; explicitly demote S5, rule gating, ProbLog, and TDC-SB/UB to 'if-budget-permits, reported as preliminary'. Specify the hand-annotated set's size, source, annotation guideline, and inter-annotator agreement so the headline is reproducible.
- [MAJOR] (methodology) The truth and non-entailment semantics of bridge rules are under-defined, yet bridges carry half the headline claim. A bridge (e.g., author_of(X,Y) :- wrote(X,Y)) is a universally-quantified, often defeasible Horn clause, not an atomic fact: 'false admission' of a bridge is not the same kind of event as a false atomic fact, 'non-entailment' of a universally-quantified rule by a ~3000-char document is subtle, and gold-labeling a bridge as correct/incorrect (especially defeasible bridges on the realistic legal/narrative set) is fuzzier than for facts. Without a crisp operational definition, the gold arbiter — on which the entire validation chain depends — is ill-specified for the bridge half, and the bridge-decoy / bridge-contamination notions are undefined. This can render the bridge-FDR results uninterpretable and waste the compute spent on them.
  Action: Define precisely, before running: (a) what makes a bridge 'true' (universally valid vs. document-licensed vs. usually-true-with-exceptions) and how gold annotators decide it; (b) what 'non-entailment' means for a bridge decoy and how contamination (a decoy bridge that is actually a valid mapping) is audited; (c) whether defeasible bridges are in or out of the headline scope. If bridge truth is only cleanly definable on CLUTRR's deterministic kinship canonicalization, scope the headline bridge claim there and treat realistic-genre bridges as exploratory.
- [MINOR] (rigor) The confirmatory success criterion is disjunctive ('for at least one decoy family, realized FDR tracks alpha ...') across family x genre x alpha cells, while the underlying tail tests (tail win-rate departure from 0.5, upper-tail two-sample CDF test, diagonal-tracking) are individually low-powered. Selecting the best-performing cell as the headline without a multiplicity correction or a pre-registered confirmatory cell inflates the chance of a spurious 'pass' — a particularly visible irony for a paper whose entire thesis is rigorous FDR control of selection among many candidates.
  Action: Pre-register the single (decoy family, genre, alpha-grid) combination that constitutes the confirmatory test, and treat all other cells as exploratory; or apply an explicit multiplicity correction to the family of validation tests and report it. State this in the success criteria so 'at least one family' cannot be read as post-hoc cherry-picking.
- [MINOR] (evidence) The related-work coverage, though strong on the proteomics/knockoff side and the labeled-conformal side, omits the most recent directly-comparable work that combines FDR control with LLM hallucination: 'Principled Detection of Hallucinations in LLMs via Multiple Testing' (arXiv 2508.18473, 2025), which uses conformal p-values + Benjamini-Hochberg with a labeled calibration set to control the false-alarm rate of hallucination detection. It is not a novelty threat (it needs labels, certifies output detection, uses BH on conformal p-values rather than target-decoy competition, and has no decoys/entrapment/symbolic propagation), but a top-venue reviewer will expect it cited and differentiated. The adjacent DINCO (self-generated distractors for verbalized-confidence calibration, OpenReview pZs4hhemXc) is worth a one-line mention as a candidate pilot elicitation.
  Action: Add arXiv 2508.18473 to related work and differentiate it along the same axes used for Mohri-Hashimoto/Jin-Candes (labeled vs. label-free operation; output-level detection vs. neuro-symbolic admission gating; BH-on-conformal-p-values vs. target-decoy/knockoff competition; no decoys/entrapment/per-leaf certificates). Its label requirement strengthens, not weakens, the label-free wedge. Optionally note DINCO's distractor-normalized confidence as a candidate elicitation for the Phase-0 pilot.
- [MINOR] (clarity) The density critique from the previous review was not addressed and is arguably worse. Nearly every field is a long defensive run-on that interleaves the claim, its caveats, and point-by-point rebuttals to earlier reviews. This is comprehensive but taxing; it obscures the genuine novelty, makes the hypothesis harder to evaluate now, and will cost the presentation score at ACL.
  Action: Tighten as previously suggested: keep hypothesis/summary to the mechanism and claim, move defensive asides into assumptions/method, cap sentence length, and lead the summary with one plain-language sentence of the mechanism before any qualification. Add a compact claim-chain table (S1-S5: test, pass criterion, what-is-reported-on-failure). Surface the demonstrable-alpha range, expected document/call counts, and the operation-vs-validation label budget once, early.
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

### [2] HUMAN-USER prompt · 2026-06-16 04:06:43 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-16 04:12:15 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same frame (label-free decoy-competition FDR gate at the text-to-logic boundary); refines S4 to doc-level, adds entrapment tail diagnostic, crisp CLUTRR bridges, feasibility budget.' is too long (at most 120 characters, got 181)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
