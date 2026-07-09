# review_hypo — create_idea

> Phase: `hypo_loop` · round 4 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 03:52:46 UTC

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

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (rigor) The (correct) move to TAIL-conditioned exchangeability diagnostics introduces a statistical-power tension with the fixed sub-$10, CPU-only budget that is now the single biggest execution risk. The tail-conditioned win-rate is computed only among matched pairs scoring ABOVE the operative cutoff, and the two-sample test is on the UPPER tails of the score CDFs — both are, by construction, estimated from the sparse high-score region. With ~10-40 candidates per ~3000-char document and corpus-aggregate pooling, the number of above-cutoff matched pairs available for these tests can be small, so the headline decoy-family showdown (S1) and the calibration diagonal (primary criterion 1) risk being underpowered. The hypothesis itself names 'an uninterpretable null (control neither clearly holds nor clearly fails anywhere)' as the true failure mode, and an underpowered tail test is the most likely way to land there.
  Action: Make the prospective power analysis TAIL-SPECIFIC, not marginal: estimate the number of above-cutoff matched pairs (and admitted items N_T, N_E) required to (a) detect a target departure of the tail win-rate from 0.5 and (b) power the upper-tail two-sample test at the operative alpha, then size the corpus to that target — including the per-genre split, since legal vs narrative must each be powered. Report the achievable-alpha floor jointly as a function of candidate count AND r so the demonstrable tail-region is explicit. If the budget cannot power both genres, pre-register narrowing to a single genre for the headline and treat the second as exploratory. Run a cheap pilot first (see the score-separation critique) to estimate tail density before committing the 60% headline allocation.
- [MAJOR] (methodology) The achievable-alpha floor, now compounded by the entrapment ratio r, may exclude the practically meaningful low-alpha regime, weakening the 'trustworthy/auditable extraction' pitch even if control is demonstrated. With corpus pooling, the knockoff+ '+1' offset gives a minimum non-trivial FDR ~1/(k+1) at k admissions, and mixing in entrapment at ratio r further consumes admission slots and inflates the variance of FDP_hat. The combination can push the smallest demonstrable alpha well above the ~0.05-0.10 range a reader associates with 'trustworthy fact extraction.' If the design can only show diagonal tracking at, say, alpha ~ 0.2-0.3, the headline 'control to a user-specified target alpha' is technically true but operates in a coarse regime that materially undercuts the significance claim.
  Action: Quantify and report the demonstrable alpha range up front (in the summary and success criteria), and bound the 'user-specified alpha' claim to that range rather than implying arbitrarily small alpha. To widen the usable range: (i) increase the pooled candidate count via more documents per genre (the cheapest lever given extraction is the dominant LLM cost); (ii) choose r to balance the entrapment-variance vs floor trade-off explicitly and report the chosen operating point; (iii) consider a less conservative competition-based bound (e.g., the FDP-bounding results in 'Bounding the FDP in competition-based control of the FDR', arXiv 2302.11837) as an alternative threshold rule and report whether it lowers the floor without breaking validity. Frame any success at coarse alpha honestly as a first demonstration.
- [MINOR] (rigor) Validity rests entirely on empirically engineering tail-exchangeability, with no theoretical guarantee — unlike Model-X knockoffs (exchangeable by construction) or shuffled/reversed proteomics decoys (with a theoretical equal-chance argument). LLM-counterfactual decoys are generated from the same model whose hallucinations they are meant to mimic, so there is a real chance NO family achieves tail-exchangeable diagonal tracking on either genre. The hypothesis is honest about this and provides a survives-partial fallback, but the fallback as written ('counterfactual decoys pass on narrative but fail on legal text') is a descriptive pass/fail characterization, which is a weaker contribution than a top venue expects.
  Action: Pre-commit to converting the likely-partial outcome into a PREDICTIVE account: specify in advance the document/score features hypothesized to govern tail-exchangeability (entity density, document specificity, tail score-separation, genre), fit a model that predicts which decoy-family x genre combinations achieve it, and validate it out-of-sample on a held-out genre. State this as an explicit secondary deliverable so the fallback is a mechanism-level insight rather than a results table.
- [MINOR] (methodology) Verifying that plausibility-matched counterfactual decoys are genuinely NON-ENTAILED is close to the hard labeling problem the method aims to avoid, and contamination perturbs calibration. The more tail-matched (plausible) a counterfactual decoy is, the more likely it is actually entailed or world-true-and-inferable, in which case it is really a target masquerading as a decoy. Such contamination inflates the admitted-decoy count, biasing the decoy-FDR estimate conservative and costing recall, while the contamination check itself ('symbolic non-derivability + an LLM/human entailment audit') requires exactly the entailment judgments the label-free claim seeks to avoid.
  Action: Report the contamination rate per decoy family and per genre, state the DIRECTION of its effect on the calibration diagonal (conservative vs anti-conservative), and quantify sensitivity of the diagonal to plausible contamination-rate values. Acknowledge that the non-entailment audit is a small label cost analogous to (and to be charged against) the conformal baseline's calibration-label budget, so the 'zero-label' wedge is stated precisely (zero labels for OPERATION; a small audit/probe budget for VALIDATION) rather than absolutely.
- [MINOR] (evidence) The load-bearing assumption that the LLM emits a roughly monotone confidence/score separating document-entailed from non-entailed content IN THE TAIL is stated but not yet de-risked, despite well-documented unreliability of LLM verbalized confidence. If this separation fails in the high-score region, no thresholding procedure (decoy-gated, conformal, or otherwise) can succeed, and the entire headline budget would be spent confirming a negative that a cheap pilot could have surfaced first.
  Action: Run a small, cheap pilot (a few dozen labeled items) BEFORE committing the headline budget: confirm the score separates entailed from non-entailed better than chance specifically in the upper tail, and pick the scoring elicitation (verbalized confidence vs logprob-derived vs self-consistency agreement) that best separates. Gate the full run on this pilot, and report the pilot as a methods precondition.
- [MINOR] (clarity) Despite the strong structural refactor (primary claim + S1-S4 + dependency diagram + glossary), the proposal remains extremely dense: most fields are long run-on sentences that interleave the claim, its caveats, and point-by-point defensive responses to the previous review. This is comprehensive but taxing, and for an ACL submission the contribution risks being obscured by elaboration, costing the presentation/clarity score.
  Action: Keep the hypothesis/summary fields to the claim itself; relocate the defensive asides ('we DROP the naive ratio', 'we do NOT assume X', 'NOT a marginal average') into the assumptions/method sections where they belong. Cap sentence length, and lead the summary with one plain-language sentence of the mechanism before the qualifications. Surface the achievable-alpha floor and the precise label-budget accounting early. This is polish, but it materially improves how the genuine novelty reads.
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

### [2] HUMAN-USER prompt · 2026-06-16 03:52:46 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-16 04:00:13 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.' is too long (at most 120 characters, got 143)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
