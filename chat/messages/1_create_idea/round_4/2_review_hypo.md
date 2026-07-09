# review_hypo — create_idea

> Phase: `hypo_loop` · round 4 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 03:52:40 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 03:52:46 UTC

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

### [3] HUMAN-USER prompt · 2026-06-16 03:52:46 UTC

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

### [4] ASSISTANT · 2026-06-16 03:54:06 UTC

```
I'll review this hypothesis carefully. Let me first ground my review in the current state of the field, then assess what's changed since the previous iteration.

Let me load the web research tools and check the user uploads.
```

### [5] TOOL CALL — ToolSearch · 2026-06-16 03:54:06 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-06-16 03:54:06 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [7] TOOL CALL — Bash · 2026-06-16 03:54:06 UTC

```
List user uploads and read relevant memory files:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---MEMORY---" && cat /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md 2>/dev/null && echo "---DRIM---" && cat /root/.claude/projects/-ai-inventor/memory/project_drim_results.md 2>/dev/null
```

### [8] TOOL RESULT — Bash · 2026-06-16 03:54:06 UTC

```
{"stdout": "total 1955\ndrwxr-xr-x  2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 10 root root 2000777 Jun 16 03:47 ..\n---MEMORY---\n---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n---DRIM---\n---\nname: project-drim-results\ndescription: Final results of the dRIM experiment pipeline for gen_art_experiment_1 (run_C25WCeQ-dDlK)\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: f0974d37-c07d-4b21-8902-40d30b14db05\n---\n\nExperiment completed: Directed Risk Interaction Matrix (dRIM) pipeline for S&P 500 10-K financial distress prediction.\n\n**Output:** `method_out.json` — 3639 examples, 1.8 MB, schema-validated (exp_gen_sol_out).\n\n**Verdict: disconfirmed**\n\n**Why:** Inter-model kappa = 0.155 (threshold ≥0.60 for confirmed; <0.50 = disconfirmed). PR-AUC delta (dRIM vs NPMI baseline) = 0.0 — no predictive improvement from directed risk interaction features.\n\n**Key stats:**\n- dRIM density: 1.7% (low overlap of risk pairs in passages)\n- Total LLM calls: 136,892 over 3639 filings\n- API cost: $2.57 (budget cap $9.50)\n- Runtime: ~4h (fixed sequential→gather async bug partway through)\n\n**Pipeline timing:**\n- Boilerplate rate: 54.7% (33,101 candidate passages)\n- EDGAR distress events: 31 firm-years out of 3,744\n- FinBERT: 8000 sampled paragraphs, ~10 min on CPU\n- dRIM scoring: ~12 min/batch × 18 batches = ~3.5h wall time after async fix\n\n**Regression results (PR-AUC):**\n- baseline_a_lm: 0.0038\n- baseline_b_pb_stress: 0.0046\n- baseline_c_finbert: 0.0043\n- baseline_d_npmi: 0.0073\n- ablation_no_direction: 0.0073\n- full_drim: 0.0073\n\n**How to apply:** This workspace/run is complete. Output files at gen_art_experiment_1/.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] ASSISTANT · 2026-06-16 03:54:14 UTC

```
The user_uploads folder is empty. My memory confirms this is the same hypothesis line at iteration 4. Let me ground the review with targeted searches on the novelty threat and known failure modes.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 03:54:14 UTC

```
target-decoy competition knockoff false discovery rate LLM hallucination fact extraction
```

### [11] TOOL CALL — WebSearch · 2026-06-16 03:54:14 UTC

```
decoy synthetic negative control FDR control large language model factuality 2025
```

### [12] TOOL CALL — WebSearch · 2026-06-16 03:54:14 UTC

```
LLM verbalized confidence calibration unreliable tail high-confidence hallucination
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 03:54:21 UTC

```
{"query": "target-decoy competition knockoff false discovery rate LLM hallucination fact extraction", "results": [{"tool_use_id": "srvtoolu_01Rr8NCPmYfTnzABSkiwKZkn", "content": [{"title": "Controlling the false discovery rate via competition: Is the +1 needed? - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167715223000433"}, {"title": "Group-walk, a rigorous approach to group-wise false discovery rate analysis by target-decoy competition", "url": "https://www.biorxiv.org/content/10.1101/2022.01.30.478144.full.pdf"}, {"title": "Group-walk: a rigorous approach to group-wise false discovery rate analysis by target-decoy competition | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii82/6701992"}, {"title": "Group-walk, a rigorous approach to group-wise false discovery rate analysis by target-decoy competition | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2022.01.30.478144v2.full"}, {"title": "Controlling the False Discovery Rate via Competition: is the +1 needed?", "url": "https://arxiv.org/pdf/2204.13248"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}]}, "Here are the search results for your query about target-decoy competition, knockoff, false discovery rate, LLM hallucination, and fact extraction:\n\n## Key Findings\n\n**Target-Decoy Competition (TDC) and Knockoffs:**\nTarget-decoy competition (TDC) relies on associating with each hypothesis a \"target\" score and a \"decoy\" score (analogous to the knockoff score). The knockoff approach involves pairing each original variable with an artificially introduced \"knockoff\" variable so they can compete against each other in terms of their contribution to the linear model.\n\n**False Discovery Rate Control:**\nTarget-decoy competition (TDC) is a commonly used method for false discovery rate (FDR) control in the analysis of tandem mass spectrometry data. Barber and Candés recently used the same principle in their knockoff+ procedure to control the FDR in feature selection in a classical linear regression model.\n\n**Applications and Recent Developments:**\nCompetition-based FDR control has gained a lot of interest in the statistical and machine learning communities. Group-walk is a procedure that controls the FDR in the target-decoy/knockoff setting while taking into account a given group structure.\n\n**Note:** The search results focus on the statistical and computational aspects of target-decoy competition and knockoff methods primarily in proteomics and machine learning contexts. The results do not contain information specifically addressing LLM hallucination or fact extraction applications of these techniques."], "durationSeconds": 7.811127380000006, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 03:54:25 UTC

```
{"query": "LLM verbalized confidence calibration unreliable tail high-confidence hallucination", "results": [{"tool_use_id": "srvtoolu_018WybS9de3UR6xnKzrr4X8d", "content": [{"title": "ConfTuner: Training Large Language Models to Express Their Confidence Verbally", "url": "https://arxiv.org/pdf/2508.18847"}, {"title": "Calibrating Verbalized Confidence with Self-Generated Distractors | OpenReview", "url": "https://openreview.net/forum?id=pZs4hhemXc"}, {"title": "Part I | Understanding the Engineering Roots of LLM Hallucinations | by Luka | Medium", "url": "https://dr-luka.medium.com/part-i-understanding-the-engineering-roots-of-llm-hallucinations-1822ec0612d3"}, {"title": "Confidence Calibration in LLMs", "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"}, {"title": "I-CALM: Incentivizing Confidence-Aware Abstention for LLM Hallucination Mitigation", "url": "https://arxiv.org/html/2604.03904v1"}, {"title": "Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning", "url": "https://arxiv.org/html/2512.19920v1"}, {"title": "Evaluating large language models for accuracy incentivizes hallucinations | Nature", "url": "https://www.nature.com/articles/s41586-026-10549-w"}, {"title": "LLM Hallucinations", "url": "https://www.emergentmind.com/topics/hallucination-in-large-language-models"}]}, "Based on the search results, here's what I found on LLM verbalized confidence calibration and its relationship to hallucinations:\n\n## Key Findings\n\n**The Core Problem:**\nLLMs often report very high confidence even when producing hallucinated or incorrect content. Verbalized LLM-generated confidence scores have empirically been found to be miscalibrated, reporting high confidence on instances with low accuracy.\n\n**Why This Happens:**\nThe overconfidence often stems from a given LLM's heightened suggestibility when faced with claims that it encodes little information about. Additionally, LLMs exhibit poor uncertainty calibration and often generate incorrect answers with high confidence.\n\n**Challenges with Self-Reported Confidence:**\nModels may not reliably convert stated confidence into an optimal answer/abstain policy, consistent with evidence that LLM decisions can be weakly coupled to verbal confidence.\n\n**Current Approaches:**\nResearchers are developing training-based methods to improve calibration. Recent efforts have focused on improving the elicitation of verbalized confidence from LLMs, though prompt-based methods have shown limited effects in improving calibration.\n\nThe search results reveal that this is an active area of research with multiple proposed solutions, including distractor-based approaches, reinforcement learning-based calibration, and critique-based methods."], "durationSeconds": 9.856711987000002, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 03:54:29 UTC

```
{"query": "decoy synthetic negative control FDR control large language model factuality 2025", "results": [{"tool_use_id": "srvtoolu_01MFfKPNpL2SMR3frtVCHvZz", "content": [{"title": "Principled Detection of Hallucinations in Large Language Models via Multiple Testing", "url": "https://arxiv.org/pdf/2508.18473"}, {"title": "DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models", "url": "https://arxiv.org/html/2601.01156v1"}, {"title": "Hallucination to Truth: A Review of Fact-Checking and Factuality Evaluation in Large Language Models", "url": "https://arxiv.org/html/2508.03860"}, {"title": "Survey on Factuality in Large Language Models", "url": "https://dl.acm.org/doi/pdf/10.1145/3742420"}, {"title": "Sparse Reward Subsystem in Large Language Models", "url": "https://arxiv.org/pdf/2602.00986"}, {"title": "Towards Unification of Hallucination Detection and Fact Verification for Large Language Models", "url": "https://arxiv.org/pdf/2512.02772"}, {"title": "The Curious Case of Factuality Finetuning: Models' Internal Beliefs Can Improve Factuality", "url": "https://arxiv.org/pdf/2507.08371"}]}, "Based on the search results, I found several relevant papers and research related to your query about factuality control and hallucination detection in large language models from 2025:\n\n## Key Findings:\n\n**Recent Papers on Factuality and Hallucination Detection (2025):**\n\n1. **Factool** addresses factuality detection in generative AI with a tool-augmented framework for multi-task and multi-domain scenarios.\n\n2. Recent work on factuality control uses parameter-efficient techniques like LoRA to induce hallucinations by fine-tuning models with hallucinated QA pairs from datasets like HaluEval.\n\n3. A comprehensive review examined studies published between January 2021 and September 2025 that employed LLMs to verify external claims or factual content, with research showing that fine-tuning on synthetic and ANLI data boosts robustness.\n\n4. Recent surveys on factuality in LLMs were published in September 2025, examining hallucination, factuality, outdated information, and domain-specificity.\n\n5. Recent work on unfamiliar fine-tuning examples explores how they control language model hallucination, published in April 2025.\n\nThe research landscape in 2025 focuses heavily on using synthetic negative controls and various fine-tuning approaches to improve factuality and detect hallucinations in large language models, though the specific methodology combining \"decoy synthetic negative control\" with formal FDR control may require more targeted research."], "durationSeconds": 14.54636206900001, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 03:54:47 UTC

```
Novelty confirmed: target-decoy/knockoff FDR is confined to proteomics/stats. But two 2025 papers are close conceptual neighbors I should check — one on multiple-testing for hallucination detection, one on self-generated distractors for confidence calibration.
```

### [17] TOOL CALL — WebFetch · 2026-06-16 03:54:47 UTC

```
URL: https://arxiv.org/pdf/2508.18473
Prompt: Summarize the method and main claim. Does it use FDR control, multiple hypothesis testing, decoys, or synthetic negative controls for LLM hallucination detection? Does it require labeled calibration data? Does it gate fact extraction or symbolic/neuro-symbolic admission, or does it certify output text?
```

### [18] TOOL CALL — WebFetch · 2026-06-16 03:54:47 UTC

```
URL: https://openreview.net/forum?id=pZs4hhemXc
Prompt: Summarize the method. How are "self-generated distractors" used to calibrate verbalized confidence? Is this related to target-decoy competition or FDR control? Does it require labels?
```

### [19] TOOL RESULT — WebFetch · 2026-06-16 03:54:47 UTC

```
{"bytes": 172850, "code": 200, "codeText": "OK", "result": "# Summary of DINCO Method\n\n## Core Approach\n\nThe paper introduces **Distractor-Normalized Coherence (DINCO)**, which addresses miscalibrated confidence in LLMs by accounting for model suggestibility. The method works by having the model \"verbalize its confidence independently across several self-generated distractors (i.e. alternative claims), and normalizes by the total verbalized confidence.\"\n\n## How Self-Generated Distractors Work\n\nRather than relying on a single confidence statement, DINCO generates alternative claims and asks the model to express confidence about each one. By normalizing the original answer's confidence by the total confidence across all alternatives, the method reduces overconfidence bias that stems from the model's tendency to be suggestible about unfamiliar claims.\n\nThe approach integrates two coherence dimensions: consistency across sampled generations (self-consistency) and consistency across validations on incompatible claims.\n\n## Relation to Target-Decoy or FDR Control\n\nThe document provided contains no mention of target-decoy competition or false discovery rate (FDR) control, so I cannot comment on those connections based on this content.\n\n## Label Requirements\n\nThe abstract does not explicitly address whether labeled data is required for the method, so I cannot definitively answer this question from the material provided.", "durationMs": 4202, "url": "https://openreview.net/forum?id=pZs4hhemXc"}
```

### [20] TOOL RESULT — WebFetch · 2026-06-16 03:54:51 UTC

```
{"bytes": 514502, "code": 200, "codeText": "OK", "result": "# Summary of the Method\n\nThis paper proposes a principled approach to detecting hallucinations in Large Language Models using **multiple hypothesis testing with False Discovery Rate (FDR) control**.\n\n## Key Method Components\n\n**Multiple Testing Framework**: The authors apply classical statistical multiple testing procedures to hallucination detection. They state the approach is \"principled\" through formal hypothesis testing methodology rather than heuristic scoring.\n\n**FDR Control**: The method explicitly uses FDR control mechanisms. The paper leverages Benjamini-Hochberg procedures and related multiple testing corrections to maintain statistical guarantees while testing multiple claims simultaneously.\n\n**Synthetic Negative Controls**: The approach employs synthetic or decoy-based verification. Rather than relying solely on external knowledge bases, the method generates counterfactual statements to test model consistency—if the model contradicts itself when presented variants, this indicates potential hallucination.\n\n**No Labeled Calibration Data Required**: The method is designed to work without requiring labeled hallucination datasets for calibration, making it more practically applicable.\n\n**Output Certification**: The approach certifies which statements in LLM outputs are reliable versus hallucinated through statistical testing, effectively gating the credibility of individual claims rather than binary accept/reject decisions.\n\nThe core innovation combines classical statistical rigor with LLM evaluation, providing formal guarantees about false positive rates in hallucination detection rather than relying on neural scoring functions.\n\n[Binary content (application/pdf, 502.4KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-iter-4-review-hypo/35b925b6-7ac6-4dfc-985d-ee82700d7377/tool-results/webfetch-1781582081953-9dkzwj.pdf]", "durationMs": 8196, "url": "https://arxiv.org/pdf/2508.18473"}
```

### [21] ASSISTANT · 2026-06-16 03:55:09 UTC

```
The first paper is a serious novelty neighbor. The WebFetch summary came from a fast model and may have embellished — let me verify the actual claims against the PDF text before weighting this as a major critique.
```

### [22] TOOL CALL — Bash · 2026-06-16 03:55:09 UTC

```
Extract key terms from the multiple-testing hallucination PDF:
PDF=$(ls -t /root/.claude/projects/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-iter-4-review-hypo/*/tool-results/webfetch-*.pdf 2>/dev/null | head -1); echo "PDF: $PDF"; if command -v pdftotext >/dev/null 2>&1; then pdftotext "$PDF" - 2>/dev/null | grep -iE "decoy|knockoff|counterfactual|false discovery|benjamini|hochberg|target-decoy|calibrat|label|exchange" | head -40; else echo "no pdftotext"; fi
```

### [23] TOOL RESULT — Bash · 2026-06-16 03:55:09 UTC

```
{"stdout": "PDF: /root/.claude/projects/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-iter-4-review-hypo/35b925b6-7ac6-4dfc-985d-ee82700d7377/tool-results/webfetch-1781582081953-9dkzwj.pdf\nmultiple evaluation scores via conformal pvalues, enabling calibrated detection with controlled false alarm rate. Extensive experiments\ncalibration step that uses a small calibration set\nproperties. This represents a significant shift toward principled inference, providing the first framework capable of offering calibrated false-alarm control in a generative context (Section 3).\nto generate hallucinations, labeled as correct, from\n\fprompts likely to generate hallucinations, labeled\ncalibration dataset C = {xci }ni=1\nmaking it difficult to explicitly label data as coming\nand reference answers to label the generations as\ncalibration dataset C and its scores\non the general version of the Benjamini-Hochberg\n(BH) procedure that allows the scores to be dependent (Benjamini and Yekutieli, 2001). If the\nH0 , but we have access to the calibration set C,\nin the calibration set as {sji = sj (xci ) : xci ∈\nconformal p-values and their random versions, conditioned on the calibration dataset C, are defined\nthe scores from the calibration dataset C and the\n2023)). Let α, δ ∈ (0, 1). Denote the calibration\nset as C. When the size of the calibration set |C| is\n(Magesh et al., 2023), the size of calibration dataset\nImportantly, the required calibration size depends only on the parameters (α, ϵ, δ, K) and is\ntested. When the calibration set is small, ϵ can be\nthe underlying baseline scores already use. A calibration set can be constructed from prompts in\ntask, it can aggregate them into a single calibrated\nmarginal guarantees over random calibration sets,\nlong as the size of the calibration dataset is sufficiently large. The calibration set’s diversity and\nThe final part is to construct the calibration\ndataset, which requires a method to label whether\nor not. Using the reference answer, each promptgeneration pair is labeled based on the Rouge-L\nprompt is deemed not likely to generate hallucinations, since its generations are approximately correct. Finally, the calibration dataset is constructed\nAlgorithm 2: Assign hallucination labels\nnot to generate hallucinations. We repeat the experiments 10 times using a randomized calibration\nthe size of the calibration dataset is 1, 000. We\nMathematically, given the calibration dataset C, the\nWe also study the effect of the calibration set\nsize. In principle, increasing the calibration size\nwe increase the calibration set from 1,000 to\nto 0.2%). Meanwhile, the standard deviation increases by more than 0.2%, likely because allocating more samples to calibration leaves fewer\nNext, we further enlarge the calibration set by\ncalibration prompts without hallucinated generations from the combined pool. This setting serves\nthis mixed calibration set, our performance changes\nobtain a calibration set large enough to fully meet", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [24] ASSISTANT · 2026-06-16 03:59:09 UTC

```
Verified — and this changes my read importantly. The Aug-2025 paper (arXiv 2508.18473, "Principled Detection of Hallucinations via Multiple Testing") uses conformal p-values + Benjamini-Hochberg and **requires a labeled calibration set (~1,000 items)** — the WebFetch summary's "decoy/counterfactual" claim was fabricated by the summarizer. So it's a labeled FDR-for-hallucination method that *reinforces* this hypothesis's label-free wedge rather than threatening its novelty, but it's a directly-comparable recent work the related-work section omits.

I now have what I need. The core idea remains genuinely novel (target-decoy/knockoff has never been transplanted to LLM extraction), the revision is highly responsive to the prior review, and LLM tail-overconfidence is well-documented (supporting the pilot's importance). Let me write the review.
```

### [25] TOOL CALL — Write · 2026-06-16 03:59:09 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is iteration 4 of a genuinely novel and unusually rigorous hypothesis: transplant target-decoy / knockoff+ FDR control, entrapment FDP estimation (Wen et al., Nat. Methods 2025), and property-matched decoy design (DeepCoy) from genomics/proteomics to the fuzzy-unification admission boundary of a text-to-logic pipeline, so every LLM-proposed fact and bridge must out-score a plausibility-matched counterfactual decoy before entering a Prolog KB, with label-free corpus-aggregate FDR control. I verified the novelty against the literature: target-decoy/knockoff control remains confined to proteomics/stats/feature-selection and has not been applied to LLM extraction or the neuro-symbolic boundary; the closest recent neighbor (arXiv 2508.18473, conformal p-values + Benjamini-Hochberg for hallucination detection) needs a labeled calibration set and certifies output, so it reinforces rather than threatens the label-free wedge. The revision is highly responsive to the prior review: the power analysis is now tail-specific and per-genre, the achievable-alpha floor is bounded up front as a joint function of (k, r), the score-separation precondition is de-risked by a Phase-0 pilot (well-justified given documented LLM tail-overconfidence), contamination is characterized with symmetric label-budget accounting, and the fallback is promoted from a descriptive pass/fail table to a predictive account (S4). The honest reframing from 'guarantee' to 'empirically-validated calibration' with 'when does it hold' as the central question is exactly right. What still keeps this at borderline are four residual, fixable issues that the previous fixes exposed underneath: (1) S4 — now the load-bearing de-risk — is validated 'out-of-sample on a held-out genre' with only two genres, i.e. n=1 generalization unit, so the safety net is itself unvalidatable as designed; (2) the entrapment corroboration inherits the same 'too-easy' anti-conservative failure mode as decoys but has no analogous tail-difficulty diagnostic, making the co-failure scenario more likely than the design admits; (3) the experimental program has steadily ballooned (pilot + 2-genre headline + 2 baselines + S4 + S5 + rule gating + ProbLog + TDC-SB/UB), straining a $10/CPU-only budget plus unbudgeted hand-annotation; (4) the truth/non-entailment semantics of bridge rules (universally-quantified, often defeasible Horn clauses) are under-defined, leaving the gold arbiter for half the headline ill-specified. Clarity/density, flagged last round, is unaddressed and arguably worse. Fixing these would plausibly move the score to 6-7.",
  "strengths": [
    "Genuinely novel, well-grounded Level-3 cross-domain transfer. I confirmed against the literature that target-decoy/knockoff FDR control has never been applied to LLM-proposed symbolic assertions or the neuro-symbolic admission boundary; the related-work mapping (Wen et al. entrapment, Barber-Candes knockoffs, DeepCoy property-matched decoys, Mohri-Hashimoto / Jin-Candes / coherent factuality conformal baselines, ontology-constraint filters) is accurate and well-differentiated.",
    "Exceptionally honest framing. The claim is explicitly downgraded from a theorem to an empirically-validated calibration, with 'when does the calibration hold' made the central scientific object — the correct stance given LLM decoys carry no construction-level exchangeability guarantee, and a stronger contribution than a bare control claim.",
    "The Phase-0 pilot gating the headline budget is excellent research hygiene and directly de-risks the single most likely silent killer (no tail score-separation). It is well-motivated: LLM verbalized confidence is documented to be miscalibrated and overconfident exactly in the high-confidence region where admissions occur.",
    "Tail-conditioned diagnostics (win-rate among above-cutoff pairs + an upper-tail two-sample CDF test) correctly target the region where target-decoy validity actually matters, rather than a marginal average that can read 0.5 while failing where admissions happen. This is a sharp, non-obvious methodological point.",
    "Strong graceful-failure architecture: explicit claim decomposition (S1-S5), a dependency chain that localizes and reports breaks, a demonstrable-alpha regime stated up front, and a glossary. Negatives (precondition failure, co-failure, anti-conservative families) are pre-registered as reportable results, reducing the risk of an uninterpretable null.",
    "Highly responsive to the prior review: tail-specific per-genre power analysis, alpha-floor bounded as f(k, r) with TDC-SB/UB and the +1-removal analysis cited as floor-relaxing options, contamination direction/sensitivity characterized, and the label budget stated precisely (zero labels for operation; small audit/probe for validation, charged symmetrically against the conformal baseline)."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "The statistical reasoning is careful and unusually self-aware for a pre-experiment hypothesis: tail-conditioned validity, the valid combined entrapment estimator (not the naive ratio), the +1/r-aware alpha floor, per-document normalization sensitivity, and a pilot gate. Up from 2 in iteration 1. It is held below 4 by three genuine residual gaps: the S4 out-of-sample validation is n=1 genre; the entrapment arm has no tail-difficulty diagnostic and can co-fail anti-conservatively with the decoys; and bridge-rule truth/non-entailment is not crisply defined.",
      "improvements": [
        "Re-base S4's out-of-sample validation on the document (many units) rather than the genre (two units): predict per-document/per-item tail-exchangeability from document-level features with leave-one-cluster-out CV, keeping the single genre-holdout as one illustrative test, not the validation. This makes the headline de-risk actually powerable.",
        "Add a tail-difficulty diagnostic for entrapment symmetric to the decoy one: report the admitted-entrapment score distribution vs. gold false-reals in the tail, so 'entrapment is too easy -> anti-conservative FDP_hat' is detected, not merely caveated as a possible co-failure.",
        "Give a precise operational definition of bridge truth and bridge non-entailment for universally-quantified (and defeasible) Horn clauses, and of bridge-decoy contamination, with the annotation guideline that defines the gold arbiter for the bridge half of the headline."
      ]
    },
    {
      "dimension": "presentation",
      "score": 2,
      "justification": "The macro-structure (plain statement + status-of-claim + S1-S5 + dependency chain + glossary) is good, but the previous review's density critique was not addressed and is arguably worse: most fields are long defensive run-ons interleaving claim, caveat, and point-by-point rebuttals to prior reviews. For an ACL submission this buries the contribution, and it already impedes evaluation of the hypothesis itself.",
      "improvements": [
        "Keep hypothesis/summary to the mechanism and the claim; relocate defensive asides ('we do NOT assume', 'we DROP the naive ratio', 'NOT a marginal average') into assumptions/method. Cap sentence length and lead the summary with one plain-language sentence of the mechanism before any qualification.",
        "Surface the three load-bearing numbers early and once: the demonstrable-alpha range, the expected pooled candidate/document count from the power analysis, and the label budget (operation vs. validation).",
        "Add a single compact table of the claim chain (S1-S5: what each tests, the pass criterion, and what is reported if it fails) so a reader can grasp the contribution and its failure modes without parsing the prose."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "A novel, well-differentiated method addressing a real and well-motivated problem (a label-free, auditable hallucination knob exactly at the fuzzy-unification interface, where existing conformal methods need labels and certify the output, not the admission boundary). The predictive-account reframe (S4) is a strong move toward a mechanism-level insight. Held below 4 because realization is genuinely uncertain (no exchangeability guarantee, likely-partial control), the de-risk S4 is under-powered as designed, and significance is bounded to a corpus-aggregate, coarse-alpha regime.",
      "improvements": [
        "Make S4 robustly validatable (see soundness) so the 'contribution survives partial' guarantee is real rather than aspirational — this is what protects the contribution if the headline control claim fails.",
        "State the demonstrable-alpha range concretely and argue why control even at a coarse alpha at the neuro-symbolic boundary is a useful first result, so significance is not read as contingent on small alpha.",
        "Position against arXiv 2508.18473 explicitly (labeled, output-level, BH on conformal p-values, no decoys/entrapment/symbolic propagation) to sharpen the label-free + interface-gating + per-leaf-certificate wedge against the very latest FDR-for-hallucination work."
      ]
    }
  ],
  "critiques": [
    {
      "category": "rigor",
      "severity": "major",
      "description": "S4 (the predictive account of exchangeability) is now the de-risked headline — the deliverable that survives if full diagonal control fails — but its validation, 'fit the feature model and validate OUT-OF-SAMPLE on a held-out genre', has only two genres (legal, narrative). Leave-one-genre-out therefore means training on one genre and testing on exactly one held-out genre: n=1 generalization unit, with 'genre' itself as one of the predictive features. A feature model (entity density, document specificity, tail score-separation, genre) fit on a handful of family x genre cells and 'validated' on a single held-out genre is an anecdote, not a generalizable mechanism-level account. The safety net for the whole program is, as designed, unvalidatable — which is the most consequential issue because the hypothesis leans on S4 precisely for the most probable (partial) outcome.",
      "suggested_action": "Make the unit of out-of-sample validation the document, not the genre. Fit the exchangeability model on document-level and score-level features across many documents and predict per-document (and per-item) tail-exchangeability, validating with leave-one-document-cluster-out (or leave-one-source-out) cross-validation so there are many held-out units. Keep the leave-one-genre-out result as one illustrative external test, explicitly labeled as a single-unit generalization probe, not the validation. If genre-level generalization is to be a real claim, pre-register >=3-4 genres/sources and report the budget cost; otherwise drop the genre-holdout framing from the success criterion."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The entrapment corroboration (S2) inherits the same 'too-easy -> anti-conservative' failure mode the decoy side is carefully designed to detect, but with no analogous diagnostic. Foreign-document-injection and explicit-contradiction entrapment are plausibly EASIER to reject than subtle plausible counterfactual hallucinations (off-topic entities and overt contradictions are more detectable), so admitted-entrapment N_E under-represents realized false admissions and the combined estimator FDP_hat = N_E*(1+1/r)/(N_T+N_E) under-estimates true FDP. Construction-independence guards against tautological agreement but NOT against decoys and entrapment being anti-conservative simultaneously — which makes the co-failure scenario (entrapment + decoy agree, gold disagrees) not a remote caveat but a likely outcome. As written, the only guard is the gold probe, which makes entrapment partly redundant with the very gold arbiter it is meant to reduce reliance on.",
      "suggested_action": "Apply the tail-difficulty diagnostic to entrapment as well as decoys: report the admitted-entrapment score distribution against gold false-reals in the high-score region and test whether entrapment is calibrated to tail difficulty (not merely construction-independent). Pre-register that entrapment whose tail score distribution is materially easier than realized false-reals is reported as an invalid (anti-conservative) corroborator. Consider designing the entrapment to be plausibility/tail-matched (still by an independent mechanism) so its evidential value survives, and state explicitly the direction of bias if it is not."
    },
    {
      "category": "scope",
      "severity": "major",
      "description": "The experimental program has expanded across iterations to a point that strains the fixed $10/CPU-only budget and the (unbudgeted) human annotation labor. The must-run set already includes: a Phase-0 pilot over three elicitations (self-consistency itself multiplies LLM calls); extraction over CLUTRR plus a hand-annotated legal+narrative set sized by a tail-specific power analysis (the cheapest lever is MORE documents, each requiring the full extract -> decoy -> entrapment -> joint-score stack); two decoy families; entrapment generation; a facts-and-bridges FDR gate; and two baselines (confidence + Mohri-Hashimoto conformal at a matched label budget). Layered on top are S4, S5 propagation, exploratory rule gating, a ProbLog/isotonic ablation, TDC-SB/UB and +1-removal evaluation, and a per-document normalization sensitivity sweep — all in a 15% secondary slice. The risk is that the tail-power requirement and the breadth jointly under-power everything, producing the uninterpretable null the design explicitly fears. The hand-annotated set's size and protocol are also a reproducibility-critical detail (the original brief demands 'highly reproducible') and are unspecified.",
      "suggested_action": "Publish a concrete feasibility budget BEFORE committing: expected document count per genre and total LLM call count implied by the power analysis (reals + decoys + entrapment x any self-consistency multiplier x facts/bridges), priced against $10. Designate only the pilot + a single-genre headline (decoy showdown + entrapment + calibration diagonal) + the two baselines as confirmatory must-runs; explicitly demote S5, rule gating, ProbLog, and TDC-SB/UB to 'if-budget-permits, reported as preliminary'. Specify the hand-annotated set's size, source, annotation guideline, and inter-annotator agreement so the headline is reproducible."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The truth and non-entailment semantics of bridge rules are under-defined, yet bridges carry half the headline claim. A bridge (e.g., author_of(X,Y) :- wrote(X,Y)) is a universally-quantified, often defeasible Horn clause, not an atomic fact: 'false admission' of a bridge is not the same kind of event as a false atomic fact, 'non-entailment' of a universally-quantified rule by a ~3000-char document is subtle, and gold-labeling a bridge as correct/incorrect (especially defeasible bridges on the realistic legal/narrative set) is fuzzier than for facts. Without a crisp operational definition, the gold arbiter — on which the entire validation chain depends — is ill-specified for the bridge half, and the bridge-decoy / bridge-contamination notions are undefined. This can render the bridge-FDR results uninterpretable and waste the compute spent on them.",
      "suggested_action": "Define precisely, before running: (a) what makes a bridge 'true' (universally valid vs. document-licensed vs. usually-true-with-exceptions) and how gold annotators decide it; (b) what 'non-entailment' means for a bridge decoy and how contamination (a decoy bridge that is actually a valid mapping) is audited; (c) whether defeasible bridges are in or out of the headline scope. If bridge truth is only cleanly definable on CLUTRR's deterministic kinship canonicalization, scope the headline bridge claim there and treat realistic-genre bridges as exploratory."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The confirmatory success criterion is disjunctive ('for at least one decoy family, realized FDR tracks alpha ...') across family x genre x alpha cells, while the underlying tail tests (tail win-rate departure from 0.5, upper-tail two-sample CDF test, diagonal-tracking) are individually low-powered. Selecting the best-performing cell as the headline without a multiplicity correction or a pre-registered confirmatory cell inflates the chance of a spurious 'pass' — a particularly visible irony for a paper whose entire thesis is rigorous FDR control of selection among many candidates.",
      "suggested_action": "Pre-register the single (decoy family, genre, alpha-grid) combination that constitutes the confirmatory test, and treat all other cells as exploratory; or apply an explicit multiplicity correction to the family of validation tests and report it. State this in the success criteria so 'at least one family' cannot be read as post-hoc cherry-picking."
    },
    {
      "category": "evidence",
      "severity": "minor",
      "description": "The related-work coverage, though strong on the proteomics/knockoff side and the labeled-conformal side, omits the most recent directly-comparable work that combines FDR control with LLM hallucination: 'Principled Detection of Hallucinations in LLMs via Multiple Testing' (arXiv 2508.18473, 2025), which uses conformal p-values + Benjamini-Hochberg with a labeled calibration set to control the false-alarm rate of hallucination detection. It is not a novelty threat (it needs labels, certifies output detection, uses BH on conformal p-values rather than target-decoy competition, and has no decoys/entrapment/symbolic propagation), but a top-venue reviewer will expect it cited and differentiated. The adjacent DINCO (self-generated distractors for verbalized-confidence calibration, OpenReview pZs4hhemXc) is worth a one-line mention as a candidate pilot elicitation.",
      "suggested_action": "Add arXiv 2508.18473 to related work and differentiate it along the same axes used for Mohri-Hashimoto/Jin-Candes (labeled vs. label-free operation; output-level detection vs. neuro-symbolic admission gating; BH-on-conformal-p-values vs. target-decoy/knockoff competition; no decoys/entrapment/per-leaf certificates). Its label requirement strengthens, not weakens, the label-free wedge. Optionally note DINCO's distractor-normalized confidence as a candidate elicitation for the Phase-0 pilot."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "The density critique from the previous review was not addressed and is arguably worse. Nearly every field is a long defensive run-on that interleaves the claim, its caveats, and point-by-point rebuttals to earlier reviews. This is comprehensive but taxing; it obscures the genuine novelty, makes the hypothesis harder to evaluate now, and will cost the presentation score at ACL.",
      "suggested_action": "Tighten as previously suggested: keep hypothesis/summary to the mechanism and claim, move defensive asides into assumptions/method, cap sentence length, and lead the summary with one plain-language sentence of the mechanism before any qualification. Add a compact claim-chain table (S1-S5: test, pass criterion, what-is-reported-on-failure). Surface the demonstrable-alpha range, expected document/call counts, and the operation-vs-validation label budget once, early."
    }
  ],
  "score": 5,
  "confidence": 4,
  "relation_type": "evolution",
  "relation_rationale": "Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4."
}
```

### [26] TOOL RESULT — Write · 2026-06-16 03:59:09 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is iteration 4 of a genuinely novel and unusually rigorous hypothesis: transplant target-decoy / knockoff+ FDR control, entrapment FDP estimation (Wen et al., Nat. Methods 2025), and property-matched decoy design (DeepCoy) from genomics/proteomics to the fuzzy-unification admission boundary of a text-to-logic pipeline, so every LLM-proposed fact and bridge must out-score a plausibility-matched counterfactual decoy before entering a Prolog KB, with label-free corpus-aggregate FDR control. I verified the novelty against the literature: target-decoy/knockoff control remains confined to proteomics/stats/feature-selection and has not been applied to LLM extraction or the neuro-symbolic boundary; the closest recent neighbor (arXiv 2508.18473, conformal p-values + Benjamini-Hochberg for hallucination detection) needs a labeled calibration set and certifies output, so it reinforces rather than threatens the label-free wedge. The revision is highly responsive to the prior review: the power analysis is now tail-specific and per-genre, the achievable-alpha floor is bounded up front as a joint function of (k, r), the score-separation precondition is de-risked by a Phase-0 pilot (well-justified given documented LLM tail-overconfidence), contamination is characterized with symmetric label-budget accounting, and the fallback is promoted from a descriptive pass/fail table to a predictive account (S4). The honest reframing from 'guarantee' to 'empirically-validated calibration' with 'when does it hold' as the central question is exactly right. What still keeps this at borderline are four residual, fixable issues that the previous fixes exposed underneath: (1) S4 — now the load-bearing de-risk — is validated 'out-of-sample on a held-out genre' with only two genres, i.e. n=1 generalization unit, so the safety net is itself unvalidatable as designed; (2) the entrapment corroboration inherits the same 'too-easy' anti-conservative failure mode as decoys but has no analogous tail-difficulty diagnostic, making the co-failure scenario more likely than the design admits; (3) the experimental program has steadily ballooned (pilot + 2-genre headline + 2 baselines + S4 + S5 + rule gating + ProbLog + TDC-SB/UB), straining a $10/CPU-only budget plus unbudgeted hand-annotation; (4) the truth/non-entailment semantics of bridge rules (universally-quantified, often defeasible Horn clauses) are under-defined, leaving the gold arbiter for half the headline ill-specified. Clarity/density, flagged last round, is unaddressed and arguably worse. Fixing these would plausibly move the score to 6-7.\",\n  \"strengths\": [\n    \"Genuinely novel, well-grounded Level-3 cross-domain transfer. I confirmed against the literature that target-decoy/knockoff FDR control has never been applied to LLM-proposed symbolic assertions or the neuro-symbolic admission boundary; the related-work mapping (Wen et al. entrapment, Barber-Candes knockoffs, DeepCoy property-matched decoys, Mohri-Hashimoto / Jin-Candes / coherent factuality conformal baselines, ontology-constraint filters) is accurate and well-differentiated.\",\n    \"Exceptionally honest framing. The claim is explicitly downgraded from a theorem to an empirically-validated calibration, with 'when does the calibration hold' made the central scientific object — the correct stance given LLM decoys carry no construction-level exchangeability guarantee, and a stronger contribution than a bare control claim.\",\n    \"The Phase-0 pilot gating the headline budget is excellent research hygiene and directly de-risks the single most likely silent killer (no tail score-separation). It is well-motivated: LLM verbalized confidence is documented to be miscalibrated and overconfident exactly in the high-confidence region where admissions occur.\",\n    \"Tail-conditioned diagnostics (win-rate among above-cutoff pairs + an upper-tail two-sample CDF test) correctly target the region where target-decoy validity actually matters, rather than a marginal average that can read 0.5 while failing where admissions happen. This is a sharp, non-obvious methodological point.\",\n    \"Strong graceful-failure architecture: explicit claim decomposition (S1-S5), a dependency chain that localizes and reports breaks, a demonstrable-alpha regime stated up front, and a glossary. Negatives (precondition failure, co-failure, anti-conservative families) are pre-registered as reportable results, reducing the risk of an uninterpretable null.\",\n    \"Highly responsive to the prior review: tail-specific per-genre power analysis, alpha-floor bounded as f(k, r) with TDC-SB/UB and the +1-removal analysis cited as floor-relaxing options, contamination direction/sensitivity characterized, and the label budget stated precisely (zero labels for operation; small audit/probe for validation, charged symmetrically against the conformal baseline).\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"The statistical reasoning is careful and unusually self-aware for a pre-experiment hypothesis: tail-conditioned validity, the valid combined entrapment estimator (not the naive ratio), the +1/r-aware alpha floor, per-document normalization sensitivity, and a pilot gate. Up from 2 in iteration 1. It is held below 4 by three genuine residual gaps: the S4 out-of-sample validation is n=1 genre; the entrapment arm has no tail-difficulty diagnostic and can co-fail anti-conservatively with the decoys; and bridge-rule truth/non-entailment is not crisply defined.\",\n      \"improvements\": [\n        \"Re-base S4's out-of-sample validation on the document (many units) rather than the genre (two units): predict per-document/per-item tail-exchangeability from document-level features with leave-one-cluster-out CV, keeping the single genre-holdout as one illustrative test, not the validation. This makes the headline de-risk actually powerable.\",\n        \"Add a tail-difficulty diagnostic for entrapment symmetric to the decoy one: report the admitted-entrapment score distribution vs. gold false-reals in the tail, so 'entrapment is too easy -> anti-conservative FDP_hat' is detected, not merely caveated as a possible co-failure.\",\n        \"Give a precise operational definition of bridge truth and bridge non-entailment for universally-quantified (and defeasible) Horn clauses, and of bridge-decoy contamination, with the annotation guideline that defines the gold arbiter for the bridge half of the headline.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 2,\n      \"justification\": \"The macro-structure (plain statement + status-of-claim + S1-S5 + dependency chain + glossary) is good, but the previous review's density critique was not addressed and is arguably worse: most fields are long defensive run-ons interleaving claim, caveat, and point-by-point rebuttals to prior reviews. For an ACL submission this buries the contribution, and it already impedes evaluation of the hypothesis itself.\",\n      \"improvements\": [\n        \"Keep hypothesis/summary to the mechanism and the claim; relocate defensive asides ('we do NOT assume', 'we DROP the naive ratio', 'NOT a marginal average') into assumptions/method. Cap sentence length and lead the summary with one plain-language sentence of the mechanism before any qualification.\",\n        \"Surface the three load-bearing numbers early and once: the demonstrable-alpha range, the expected pooled candidate/document count from the power analysis, and the label budget (operation vs. validation).\",\n        \"Add a single compact table of the claim chain (S1-S5: what each tests, the pass criterion, and what is reported if it fails) so a reader can grasp the contribution and its failure modes without parsing the prose.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"A novel, well-differentiated method addressing a real and well-motivated problem (a label-free, auditable hallucination knob exactly at the fuzzy-unification interface, where existing conformal methods need labels and certify the output, not the admission boundary). The predictive-account reframe (S4) is a strong move toward a mechanism-level insight. Held below 4 because realization is genuinely uncertain (no exchangeability guarantee, likely-partial control), the de-risk S4 is under-powered as designed, and significance is bounded to a corpus-aggregate, coarse-alpha regime.\",\n      \"improvements\": [\n        \"Make S4 robustly validatable (see soundness) so the 'contribution survives partial' guarantee is real rather than aspirational — this is what protects the contribution if the headline control claim fails.\",\n        \"State the demonstrable-alpha range concretely and argue why control even at a coarse alpha at the neuro-symbolic boundary is a useful first result, so significance is not read as contingent on small alpha.\",\n        \"Position against arXiv 2508.18473 explicitly (labeled, output-level, BH on conformal p-values, no decoys/entrapment/symbolic propagation) to sharpen the label-free + interface-gating + per-leaf-certificate wedge against the very latest FDR-for-hallucination work.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"S4 (the predictive account of exchangeability) is now the de-risked headline — the deliverable that survives if full diagonal control fails — but its validation, 'fit the feature model and validate OUT-OF-SAMPLE on a held-out genre', has only two genres (legal, narrative). Leave-one-genre-out therefore means training on one genre and testing on exactly one held-out genre: n=1 generalization unit, with 'genre' itself as one of the predictive features. A feature model (entity density, document specificity, tail score-separation, genre) fit on a handful of family x genre cells and 'validated' on a single held-out genre is an anecdote, not a generalizable mechanism-level account. The safety net for the whole program is, as designed, unvalidatable — which is the most consequential issue because the hypothesis leans on S4 precisely for the most probable (partial) outcome.\",\n      \"suggested_action\": \"Make the unit of out-of-sample validation the document, not the genre. Fit the exchangeability model on document-level and score-level features across many documents and predict per-document (and per-item) tail-exchangeability, validating with leave-one-document-cluster-out (or leave-one-source-out) cross-validation so there are many held-out units. Keep the leave-one-genre-out result as one illustrative external test, explicitly labeled as a single-unit generalization probe, not the validation. If genre-level generalization is to be a real claim, pre-register >=3-4 genres/sources and report the budget cost; otherwise drop the genre-holdout framing from the success criterion.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The entrapment corroboration (S2) inherits the same 'too-easy -> anti-conservative' failure mode the decoy side is carefully designed to detect, but with no analogous diagnostic. Foreign-document-injection and explicit-contradiction entrapment are plausibly EASIER to reject than subtle plausible counterfactual hallucinations (off-topic entities and overt contradictions are more detectable), so admitted-entrapment N_E under-represents realized false admissions and the combined estimator FDP_hat = N_E*(1+1/r)/(N_T+N_E) under-estimates true FDP. Construction-independence guards against tautological agreement but NOT against decoys and entrapment being anti-conservative simultaneously — which makes the co-failure scenario (entrapment + decoy agree, gold disagrees) not a remote caveat but a likely outcome. As written, the only guard is the gold probe, which makes entrapment partly redundant with the very gold arbiter it is meant to reduce reliance on.\",\n      \"suggested_action\": \"Apply the tail-difficulty diagnostic to entrapment as well as decoys: report the admitted-entrapment score distribution against gold false-reals in the high-score region and test whether entrapment is calibrated to tail difficulty (not merely construction-independent). Pre-register that entrapment whose tail score distribution is materially easier than realized false-reals is reported as an invalid (anti-conservative) corroborator. Consider designing the entrapment to be plausibility/tail-matched (still by an independent mechanism) so its evidential value survives, and state explicitly the direction of bias if it is not.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"major\",\n      \"description\": \"The experimental program has expanded across iterations to a point that strains the fixed $10/CPU-only budget and the (unbudgeted) human annotation labor. The must-run set already includes: a Phase-0 pilot over three elicitations (self-consistency itself multiplies LLM calls); extraction over CLUTRR plus a hand-annotated legal+narrative set sized by a tail-specific power analysis (the cheapest lever is MORE documents, each requiring the full extract -> decoy -> entrapment -> joint-score stack); two decoy families; entrapment generation; a facts-and-bridges FDR gate; and two baselines (confidence + Mohri-Hashimoto conformal at a matched label budget). Layered on top are S4, S5 propagation, exploratory rule gating, a ProbLog/isotonic ablation, TDC-SB/UB and +1-removal evaluation, and a per-document normalization sensitivity sweep — all in a 15% secondary slice. The risk is that the tail-power requirement and the breadth jointly under-power everything, producing the uninterpretable null the design explicitly fears. The hand-annotated set's size and protocol are also a reproducibility-critical detail (the original brief demands 'highly reproducible') and are unspecified.\",\n      \"suggested_action\": \"Publish a concrete feasibility budget BEFORE committing: expected document count per genre and total LLM call count implied by the power analysis (reals + decoys + entrapment x any self-consistency multiplier x facts/bridges), priced against $10. Designate only the pilot + a single-genre headline (decoy showdown + entrapment + calibration diagonal) + the two baselines as confirmatory must-runs; explicitly demote S5, rule gating, ProbLog, and TDC-SB/UB to 'if-budget-permits, reported as preliminary'. Specify the hand-annotated set's size, source, annotation guideline, and inter-annotator agreement so the headline is reproducible.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The truth and non-entailment semantics of bridge rules are under-defined, yet bridges carry half the headline claim. A bridge (e.g., author_of(X,Y) :- wrote(X,Y)) is a universally-quantified, often defeasible Horn clause, not an atomic fact: 'false admission' of a bridge is not the same kind of event as a false atomic fact, 'non-entailment' of a universally-quantified rule by a ~3000-char document is subtle, and gold-labeling a bridge as correct/incorrect (especially defeasible bridges on the realistic legal/narrative set) is fuzzier than for facts. Without a crisp operational definition, the gold arbiter — on which the entire validation chain depends — is ill-specified for the bridge half, and the bridge-decoy / bridge-contamination notions are undefined. This can render the bridge-FDR results uninterpretable and waste the compute spent on them.\",\n      \"suggested_action\": \"Define precisely, before running: (a) what makes a bridge 'true' (universally valid vs. document-licensed vs. usually-true-with-exceptions) and how gold annotators decide it; (b) what 'non-entailment' means for a bridge decoy and how contamination (a decoy bridge that is actually a valid mapping) is audited; (c) whether defeasible bridges are in or out of the headline scope. If bridge truth is only cleanly definable on CLUTRR's deterministic kinship canonicalization, scope the headline bridge claim there and treat realistic-genre bridges as exploratory.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The confirmatory success criterion is disjunctive ('for at least one decoy family, realized FDR tracks alpha ...') across family x genre x alpha cells, while the underlying tail tests (tail win-rate departure from 0.5, upper-tail two-sample CDF test, diagonal-tracking) are individually low-powered. Selecting the best-performing cell as the headline without a multiplicity correction or a pre-registered confirmatory cell inflates the chance of a spurious 'pass' — a particularly visible irony for a paper whose entire thesis is rigorous FDR control of selection among many candidates.\",\n      \"suggested_action\": \"Pre-register the single (decoy family, genre, alpha-grid) combination that constitutes the confirmatory test, and treat all other cells as exploratory; or apply an explicit multiplicity correction to the family of validation tests and report it. State this in the success criteria so 'at least one family' cannot be read as post-hoc cherry-picking.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The related-work coverage, though strong on the proteomics/knockoff side and the labeled-conformal side, omits the most recent directly-comparable work that combines FDR control with LLM hallucination: 'Principled Detection of Hallucinations in LLMs via Multiple Testing' (arXiv 2508.18473, 2025), which uses conformal p-values + Benjamini-Hochberg with a labeled calibration set to control the false-alarm rate of hallucination detection. It is not a novelty threat (it needs labels, certifies output detection, uses BH on conformal p-values rather than target-decoy competition, and has no decoys/entrapment/symbolic propagation), but a top-venue reviewer will expect it cited and differentiated. The adjacent DINCO (self-generated distractors for verbalized-confidence calibration, OpenReview pZs4hhemXc) is worth a one-line mention as a candidate pilot elicitation.\",\n      \"suggested_action\": \"Add arXiv 2508.18473 to related work and differentiate it along the same axes used for Mohri-Hashimoto/Jin-Candes (labeled vs. label-free operation; output-level detection vs. neuro-symbolic admission gating; BH-on-conformal-p-values vs. target-decoy/knockoff competition; no decoys/entrapment/per-leaf certificates). Its label requirement strengthens, not weakens, the label-free wedge. Optionally note DINCO's distractor-normalized confidence as a candidate elicitation for the Phase-0 pilot.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The density critique from the previous review was not addressed and is arguably worse. Nearly every field is a long defensive run-on that interleaves the claim, its caveats, and point-by-point rebuttals to earlier reviews. This is comprehensive but taxing; it obscures the genuine novelty, makes the hypothesis harder to evaluate now, and will cost the presentation score at ACL.\",\n      \"suggested_action\": \"Tighten as previously suggested: keep hypothesis/summary to the mechanism and claim, move defensive asides into assumptions/method, cap sentence length, and lead the summary with one plain-language sentence of the mechanism before any qualification. Add a compact claim-chain table (S1-S5: test, pass criterion, what-is-reported-on-failure). Surface the demonstrable-alpha range, expected document/call counts, and the operation-vs-validation label budget once, early.\"\n    }\n  ],\n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [27] ASSISTANT · 2026-06-16 03:59:15 UTC

```
Let me validate the JSON and update my memory with this iteration's verdict.
```

### [28] TOOL CALL — Bash · 2026-06-16 03:59:15 UTC

```
Validate output JSON and print summary:
python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json')); print('valid JSON'); print('score', d['score'], '| conf', d['confidence'], '| relation', d['relation_type']); print('critiques:', len(d['critiques']), '| majors:', sum(1 for c in d['critiques'] if c['severity']=='major')); print('dims:', {x['dimension']:x['score'] for x in d['dimension_scores']})"
```

### [29] TOOL RESULT — Bash · 2026-06-16 03:59:15 UTC

```
{"stdout": "valid JSON\nscore 5 | conf 4 | relation evolution\ncritiques: 7 | majors: 4\ndims: {'soundness': 3, 'presentation': 2, 'contribution': 3}", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [30] ASSISTANT · 2026-06-16 03:59:37 UTC

```
Valid. Let me update memory with this iteration's verdict for continuity across the pipeline.
```

### [31] TOOL CALL — Edit · 2026-06-16 03:59:37 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
OLD: 3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.
4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.
NEW: 3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.
4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.

**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.
```

### [32] TOOL RESULT — Edit [ERROR] · 2026-06-16 03:59:37 UTC

```
Error: File has not been read yet. Read it first before writing to it.
```

### [33] TOOL CALL — Read · 2026-06-16 03:59:39 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
```

### [34] TOOL RESULT — Read · 2026-06-16 03:59:39 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "content": "3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n", "numLines": 3, "startLine": 30, "totalLines": 32}}
```

### [35] TOOL CALL — Edit · 2026-06-16 03:59:59 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
OLD: Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.
NEW: Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.

**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.
```

### [36] TOOL RESULT — Edit · 2026-06-16 03:59:59 UTC

```
{"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "oldString": "Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.", "newString": "Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n\n**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.", "originalFile": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n", "structuredPatch": [{"oldStart": 29, "oldLines": 3, "newStart": 29, "newLines": 5, "lines": [" 2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).", " 3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.", " 4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.", "+", "+**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir."]}], "userModified": false, "replaceAll": false}
```

### [37] ASSISTANT · 2026-06-16 04:00:11 UTC

```
Review complete and written to `./.terminal_claude_agent_struct_out.json`.

## Summary

**Score: 5/10 (borderline accept, improving) · Confidence: 4 · Relation to prior iteration: evolution**

This is a strong, highly responsive iteration-4 revision of a genuinely novel hypothesis (transplanting target-decoy/knockoff FDR control + entrapment validation + property-matched decoys to the LLM fuzzy-unification admission boundary). I grounded the review in the literature and confirmed:
- **Novelty holds** — target-decoy/knockoff has never been applied to LLM extraction or the neuro-symbolic boundary.
- The closest 2025 neighbor (arXiv 2508.18473, FDR-via-multiple-testing for hallucination) **needs labeled calibration**, so it *reinforces* the label-free wedge rather than threatening novelty. (Notably, the WebFetch summarizer hallucinated that this paper "uses decoys/counterfactuals" — I verified against the PDF that it does not, avoiding a false "you missed prior work" critique.)

**All six prior-review critiques were substantively addressed** (Phase-0 pilot gate, tail-specific power analysis, bounded demonstrable-alpha regime, predictive S4, contamination accounting). So I did not re-raise them.

The four **new major** issues are the next layer exposed by those fixes:
1. **S4 is unvalidatable as designed** — "out-of-sample on a held-out genre" with only 2 genres = n=1; since S4 is the de-risk, fix it with document-level cross-validation.
2. **Entrapment has no tail-difficulty diagnostic** — it inherits the same "too-easy → anti-conservative" failure as decoys, making co-failure likely.
3. **Scope has ballooned** vs. $10/CPU + unbudgeted hand-annotation — publish feasibility numbers and demote secondary arms.
4. **Bridge-rule truth/non-entailment semantics are under-defined** — leaving the gold arbiter ill-specified for half the headline.

Plus three minors: multiple-comparisons hygiene, the missing recent citation, and the still-unaddressed density. Dimension scores: soundness 3, presentation 2, contribution 3.
```

### [38] SYSTEM-USER prompt · 2026-06-16 04:00:13 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.' is too long (at most 120 characters, got 143)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [39] TOOL CALL — Edit · 2026-06-16 04:00:27 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4."
NEW:   "relation_rationale": "Same decoy/knockoff-FDR frame; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4."
```

### [40] TOOL RESULT — Edit · 2026-06-16 04:00:27 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.\"", "newString": "  \"relation_rationale\": \"Same decoy/knockoff-FDR frame; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.\"", "originalFile": null, "structuredPatch": [{"oldStart": 87, "oldLines": 5, "newStart": 87, "newLines": 5, "lines": ["   \"score\": 5,", "   \"confidence\": 4,", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same decoy/knockoff-FDR frame at the fuzzy-unification boundary; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.\"", "+  \"relation_rationale\": \"Same decoy/knockoff-FDR frame; adds Phase-0 pilot gate, bounded demonstrable-alpha regime, and predictive S4.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [41] TOOL CALL — Bash · 2026-06-16 04:00:37 UTC

```
Validate JSON and check relation_rationale length:
python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_4/review_hypo/.terminal_claude_agent_struct_out.json')); r=d['relation_rationale']; print('valid JSON | relation_rationale len =', len(r), '(<=120 OK)' if len(r)<=120 else 'TOO LONG')"
```

### [42] TOOL RESULT — Bash · 2026-06-16 04:00:37 UTC

```
{"stdout": "valid JSON | relation_rationale len = 109 (<=120 OK)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [43] ASSISTANT · 2026-06-16 04:00:38 UTC

```
Fixed. The `relation_rationale` is now 109 characters (under the 120 limit), and the JSON validates. All other fields are unchanged.
```
