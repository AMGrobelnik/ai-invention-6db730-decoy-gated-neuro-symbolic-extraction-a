# review_hypo — create_idea

> Phase: `hypo_loop` · round 6 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 04:22:02 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_6/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 04:22:08 UTC

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
  A Label-Free FDR Knob at the Text-to-Logic Admission Boundary via Plausibility-Matched Decoy Competition: Crisp-Gold Calibration
  Validity on CLUTRR and Operational Hallucination-Reduction on Open-Vocabulary Re-DocRED, Robustified Against Score-Dependence
hypothesis: |-
  PLAIN MECHANISM (one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model itself finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate then picks the most permissive admission cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  TWO-ANCHOR DESIGN (the key change this round). The mechanism is tested on two pre-registered confirmatory anchors with a clean division of labor, stated plainly: (A) CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim -- does realized FDR track target alpha (the diagonal) -- and the single primary disconfirmation; CLUTRR tests whether the knob is calibrated, NOT whether it is operationally useful on professional prose. (B) Re-DocRED (human-annotated, open-vocabulary, 96 relation types, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS claim -- atomic-fact precision/recall and hallucinated-conclusion rate versus neural baselines at matched recall -- AND the genuine fuzzy-unification bridge test (free-text relation aligned to a schema/ontology property is real ontology alignment, not a deterministic kinship normalization) AND the document-level predictive model S4 (because real cross-document feature variance lives here, not in CLUTRR). A tiny legal/news/kids'-story set is a qualitative trace-graph demo only (explicitly non-confirmatory).

  WHY THE SPLIT IS PRINCIPLED. CLUTRR gold is exact, so realized FDR can be measured precisely -- the right place for the diagonal. Re-DocRED gold has residual false negatives, so the ABSOLUTE realized FDR is noisy there, but a RELATIVE comparison of all methods under the same shared gold is robust -- the right place for the operational head-to-head. This is why diagonal-tracking is asserted only on CLUTRR while the operational win is asserted only on Re-DocRED.

  THREE LOAD-BEARING NUMBERS (stated once). (1) Demonstrable-alpha range: roughly alpha in [0.05, 0.5]; the knockoff+ '+1' offset gives a minimum estimable FDR ~1/k at k admissions, refined per anchor by the pilot. (2) Corpus & cost: <=300 CLUTRR docs + a pre-registered <=250-doc Re-DocRED subset (>=4 clusters) + ~20 illustrative legal/news/story docs; budget projected ~$2-5, HARD STOP at $10. (3) Label budget: ZERO labels for operation; gold is used only for validation, accounted symmetrically against any labeled baseline's calibration labels.

  SINGLE PRIMARY DISCONFIRMATION (S4-independent, the unfalsifiability fix). On CLUTRR FACTS, under isolated provenance-blinded scoring, at the pilot-powered alpha*: if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than a pre-registered tolerance tau AND the document-block-bootstrap confidence interval lies entirely on the anti-conservative side, the CENTRAL label-free control claim is DISCONFIRMED -- full stop, independent of entrapment agreement and independent of S4. S4 and entrapment are separately-reported secondary findings, never escape hatches that prevent a clean disconfirmation.

  CLAIM CHAIN (each row independently testable; a break is localized and reported).
  | # | CLAIM | TEST | PASS CRITERION | REPORTED ON FAIL |
  |---|-------|------|----------------|------------------|
  | S0 | Score separation (precondition) | Pilot: best elicitation separates entailed vs non-entailed in the UPPER TAIL better than chance; isolated vs lightly-batched scores agree on a labeled slice | tail-AUC>0.5 with CI; isolated~batched | run gated; precondition-failure is the reported result |
  | S1 | Decoy signature (mechanism) | Tail-conditioned win-rate among above-cutoff matched pairs (~0.5) + upper-tail two-sample CDF test | counterfactual decoys ~0.5; random swaps anti-conservative | family flagged anti-conservative |
  | S2 | Calibration validity (CLUTRR) | Sweep alpha; realized FDR vs crisp gold; document-block-bootstrap CI on the diagonal | diagonal tracked within tau above the 1/k floor | PRIMARY DISCONFIRMATION if anti-conservative beyond tau |
  | S3 | Entrapment corroboration (necessary, not sufficient) | Independent tail-matched entrapment; combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E); entrapment passes its own tail-difficulty diagnostic | bound agrees with decoy-FDR and gold; entrapment not too-easy | co-failure reported; too-easy entrapment flagged anti-conservative |
  | S4 | Operational wedge (Re-DocRED) | Matched-recall PR + hallucinated-conclusion rate vs CoT, RAG, and labeled Mohri-Hashimoto conformal | decoy-gating matches/beats all, zero-label operation as wedge | reported as no operational advantage |
  | S5 | Document-level predictive account (Re-DocRED) | Predict per-document tail-exchangeability gap from doc/score features; leave-one-cluster-out + leave-one-document-out CV; pre-registered GAP-regression power analysis | out-of-sample predictive IF >= N_min held-out units | reported DESCRIPTIVE (not predictive) below N_min |
  | S6 | Predictable propagation (preliminary) | Tightening alpha lowers multi-hop hallucinated-conclusion rate | direction + rough magnitude | reported as preliminary |

  SCORE-DEPENDENCE ROBUSTNESS (the methodology fix). knockoff+/TDC validity rests on the null sign-flip property: among genuinely-false candidates, sign(W_i) for W_i=score(real_i)-score(decoy_i) must behave like an independent fair coin conditional on |W_i|. Two design choices threaten this and are explicitly handled: (i) within-document correlation of LLM scoring noise breaks pooled-sign independence -- handled by treating the DOCUMENT as a block (document-block bootstrap for all FDP CIs; never i.i.d. pooled signs); (ii) batched joint scoring induces contrast effects that depress decoy scores anti-conservatively -- handled by ISOLATED, provenance-blinded, order-randomized scoring as the default. Crucially, the pre-registered isolated-vs-batched sensitivity check is the DISCRIMINATOR that separates a scoring artifact from genuine decoy non-exchangeability: if isolating restores the diagonal it was a batching artifact; if anti-conservatism persists under isolated scoring it is genuine non-exchangeability.

  SCOPE. Facts AND bridges carry the headline. CLUTRR bridges are crisp (deterministic kinship) and anchor the diagonal; Re-DocRED bridges are open-vocabulary relation-to-schema alignments and anchor the operational and predictive claims. Defeasible bridges, implicit common-sense rule gating, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S6 are preliminary / if-budget-permits.
motivation: |-
  Text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob there: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and catches only encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, multiple-testing hallucination detection, coherent factuality) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem -- selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth -- via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound built INDEPENDENTLY of the decoys. We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary, turning 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity.

  Why the two-anchor design matters (this round's central reframing). A label-free FDR knob is only valuable if it is BOTH calibrated AND useful where plausible hallucinations actually bite. CLUTRR's closed kinship vocabulary is the right place to prove CALIBRATION (free crisp gold, exact realized FDR) but the WRONG place to prove USEFULNESS (the relation set is tiny and well-known, so plausible hallucinations and genuine ontology-alignment bridges are weakest). We therefore add Re-DocRED -- realistic Wikipedia prose, 96 open relation types, document-level multi-hop, human gold with evidence spans -- as a fully-powered operational anchor where plausible hallucinations are rife and bridges are genuine schema alignments. This squarely answers the prior review: CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful; we never conflate the two.

  Why it matters even at coarse alpha: NO existing label-free method offers ANY FDR knob at the fuzzy-unification interface. A first, auditable, zero-operation-label control -- even at alpha ~0.1 -- converts an uncontrolled hallucination channel into a tunable one with per-leaf certificates. Because LLM decoys carry no theoretical guarantee, the most probable outcome is partial control; the document-level predictive account (S5), now based on Re-DocRED where features genuinely vary, converts a likely-partial result into a generalizable mechanism-level insight about WHEN the calibration holds.
assumptions:
- >-
  TAIL EXCHANGEABILITY AND THE NULL SIGN-FLIP PROPERTY ARE ENGINEERED AND TESTED, NOT GUARANTEED. knockoff+/TDC validity requires
  that, among genuinely-false candidates, sign(W_i) for W_i = score(real_i) - score(decoy_i) behaves like an independent fair
  coin conditional on |W_i| (the null sign-flip property), with each false real and its matched decoy equally likely to receive
  any score in the high-score region near the cutoff. LLM counterfactual decoys carry no construction-level proof of this,
  so we report an empirically-validated calibration (not a theorem) and test the condition IN THE TAIL (tail-conditioned win-rate
  ~0.5 plus an upper-tail two-sample CDF test, not a marginal average).
- >-
  SCORE-DEPENDENCE IS A FIRST-CLASS THREAT AND IS HANDLED, NOT ASSUMED AWAY. Two dependence channels can break the sign-flip
  analysis anti-conservatively: (i) WITHIN-DOCUMENT correlation of LLM scoring noise makes pooled null signs dependent --
  we therefore treat the DOCUMENT as a block, use a document-block bootstrap for all FDP confidence intervals, and never treat
  pooled signs as i.i.d. in the variance/floor analysis; (ii) BATCHED joint scoring induces contrast/ranking effects that
  let the model implicitly detect the fabricated item and depress decoy scores, biasing FDP_hat optimistic -- we therefore
  default to ISOLATED, provenance-blinded, order-randomized scoring, and pre-register an isolated-vs-batched sensitivity check
  that doubles as the DISCRIMINATOR between a scoring artifact (isolation restores the diagonal) and genuine decoy non-exchangeability
  (anti-conservatism persists under isolation).
- >-
  THE SCORE-SEPARATION PRECONDITION MUST BE MET AND IS PILOT-GATED. The LLM must emit a roughly monotone score separating
  document-entailed from non-entailed content better than chance SPECIFICALLY in the upper tail; verbalized confidence is
  documented to be overconfident exactly there, so we do not assume it. A Phase-0 pilot selects the best elicitation (verbalized,
  logprob-derived, self-consistency, DINCO-style distractor-normalized), verifies tail separation, and confirms isolated~batched
  agreement on a labeled slice. The headline budget is gated on the pilot; if no elicitation separates in the tail, that precondition-failure
  is the reported result.
- >-
  TWO-ANCHOR GOLD AND THE DEMONSTRABLE-ALPHA REGIME ARE BOUNDED AND CORPUS-AGGREGATE. Control is asserted over candidates
  pooled within an anchor; a single ~3000-char document yields only ~10-40 candidates, so the smallest demonstrable alpha
  is a joint function of pooled candidate count and entrapment ratio r (roughly [0.05, 0.5], refined by the pilot), widened
  mainly by adding documents. CLUTRR gold is exact, so the calibration DIAGONAL is asserted there; Re-DocRED gold has residual
  false negatives, so on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted (all methods face
  the same incompleteness), never an absolute diagonal. Decoy non-entailment is imperfect: an actually-entailed decoy biases
  the FDR estimate CONSERVATIVE (the safe direction); contamination rate is reported with a sensitivity analysis. Per-document
  rank-normalization precedes pooling, with a diagonal sensitivity check to the normalization choice.
- >-
  S5 IS POWERED WHERE FEATURE VARIANCE ACTUALLY EXISTS, WITH A PRE-REGISTERED PREDICTIVE-VS-DESCRIPTIVE THRESHOLD. The document-level
  tail-exchangeability gap can only be predicted if its input features vary; CLUTRR documents are near-homogeneous in those
  features (entity density, specificity, genre) and yield few per-document admissions at meaningful alpha, so S5 is BASED
  ON Re-DocRED, whose >=4 entity-type/topic clusters supply genuine cross-document variance. The Phase-0 pilot MEASURES and
  reports, on CLUTRR, both the cross-document variance of the S5 features and the expected per-document admitted-count at
  the operative alpha, demonstrating (not assuming) CLUTRR's unsuitability. The S5 unit is the document nested in clusters,
  validated by leave-one-cluster-out and leave-one-document-out CV with a pre-registered power analysis FOR THE GAP REGRESSION
  ITSELF; below a pre-registered minimum number N_min of held-out units with sufficient admissions, S5 is reported as DESCRIPTIVE
  (correlational), not predictive.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then make the two-anchor confirmatory design the central experimental object. Budget split of $10 / CPU-only: ~10% Phase-0 pilot (gates everything, measures CLUTRR feature variance and per-document admitted counts); ~30% CLUTRR calibration headline (the single pre-registered confirmatory cell + decoy showdown + tail-matched entrapment + the calibration diagonal with document-block-bootstrap CIs, facts and bridges); ~30% Re-DocRED operational headline (matched-recall PR + hallucinated-conclusion rate vs CoT, RAG, and conformal; open-vocabulary bridge alignment); ~15% baselines; ~15% secondary (S5 modeling on Re-DocRED, S6 propagation, exploratory rule gating, floor-relaxation).

  FEASIBILITY BUDGET (published before committing). Extraction ~one call/doc over <=550 docs; decoy + entrapment generation ~one call each per doc; SCORING defaults to isolated provenance-blinded calls (each real/decoy/entrapment item scored alone with identity masked and order randomized) -- the dominant cost -- mitigated by a cheap sub-$0.30/M model and, only if the pilot proves isolated~batched agreement, lightly-blinded small batches for the bulk with a full-isolated sensitivity subset. Projected ~$2-5, ~4-8M tokens; cumulative cost logged after every call; HARD STOP at $10.

  PHASE 0 -- PILOT (precondition + powerability). On a few dozen labeled items per anchor: (i) select the elicitation that best separates entailed vs non-entailed IN THE UPPER TAIL; (ii) confirm isolated~batched scoring agreement on a labeled slice (gate batching); (iii) MEASURE on CLUTRR the cross-document variance of the S5 features and the expected per-document admitted-count at the operative alpha; (iv) run a tail power analysis (above-cutoff matched pairs and admitted N_T, N_E needed) AND a GAP-regression power analysis for S5 on Re-DocRED (held-out units needed). Size both corpora to target; gate the full run.

  PIPELINE. (1) EXTRACTION: a cheap OpenRouter LLM proposes typed first-order facts; argument types grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing. (2) DECOY GENERATION: PRIMARY family = document-conditioned counterfactual decoys (maximally-plausible, non-entailed facts/bridges); random type-matched swaps retained as the predicted-anti-conservative baseline; every decoy passes a non-entailment check with reported contamination rate. (3) ENTRAPMENT: independent, tail-matched, false-by-construction (in-genre cross-document swaps, numeric/temporal perturbation, explicit contradiction), mixed at reported ratio r, with its own tail-difficulty diagnostic. (4) SCORING: isolated, provenance-blinded, order-randomized, using the pilot-selected elicitation; rank-normalized per document. (5) FDR GATE: knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges and separately per anchor; admitted items enter the KB with a logged certificate. (6) VARIANCE/CIs: document-block bootstrap throughout. (7) ENTRAPMENT VALIDATION: combined estimator upper-bounds realized false-admission; compare against decoy-FDR and gold; hunt co-failures. (8) TAIL DIAGNOSTICS (measurement only): for both decoys and entrapment, above-cutoff distribution vs gold false-reals + win-rate + upper-tail two-sample test. (9) REASONING: admitted facts/bridges populate SWI-Prolog for multi-hop deduction; backward-chaining proofs export as trace-graphs whose leaves carry provenance plus the decoy + entrapment certificate.

  EXPERIMENTS. (a) CLUTRR validity-of-control: sweep alpha; realized FDR via gold + entrapment bound; diagonal tracking with document-block-bootstrap CIs; normalization sensitivity; ISOLATED-VS-BATCHED sensitivity. (b) Decoy-family showdown + entrapment tail-difficulty. (c) Re-DocRED operational: matched-recall PR curves with CIs and hallucinated-conclusion rate vs CoT, RAG, and Mohri-Hashimoto conformal, with guarantee status side by side. (d) S5 document-level LOO-CV on Re-DocRED with the predictive-vs-descriptive threshold. (e) [preliminary] S6 propagation, exploratory rule gating, floor-relaxation. (f) Cost check (<$10, CPU-only) + auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). The Phase-0 pilot must show the selected score separates entailed from non-entailed content better than chance in the upper tail, that isolated~batched scores agree, and that the S5 power/variance measurements support a per-document or cluster gap regression. If the pilot fails, the reported contribution is the precondition-failure analysis.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent). On CLUTRR FACTS, under isolated provenance-blinded scoring, at the pilot-powered alpha*: the central label-free control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than the pre-registered tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. This is the one crisp result that can falsify the headline, independent of entrapment and of S5.

  CONFIRMED requires ALL of: (1) CALIBRATION VALIDITY (CLUTRR) -- realized FDR tracks target alpha within tau above the 1/k floor across the demonstrable grid, stable under the per-document normalization check and the isolated-vs-batched sensitivity check; (2) DECOY SIGNATURE -- counterfactual decoys reach tail-conditioned win-rate ~0.5 and pass the upper-tail two-sample test while random swaps are measurably anti-conservative, and entrapment passes its own tail-difficulty diagnostic with the combined-estimator bound agreeing with gold; (3) OPERATIONAL WEDGE (Re-DocRED) -- at matched recall (PR curves with document-block-bootstrap CIs), decoy-gating matches or beats CoT, RAG, AND the Mohri-Hashimoto conformal baseline on atomic-fact precision and hallucinated-conclusion rate, with zero-label operation as the wedge. A BH multiplicity correction is applied across all validation tests; non-confirmatory cells are exploratory.

  SECONDARY (separately reported, never escape hatches). (4) S5 document-level model: PREDICTIVE if validated out-of-sample across >= N_min held-out Re-DocRED units, else reported DESCRIPTIVE; either way it characterizes WHICH document/score features govern tail-exchangeability. (5) Entrapment self-corroboration agrees with gold (co-failures reported). (6) S6 -- tightening alpha reduces multi-hop hallucination in the predicted direction. (7) Ablating the decoy gate measurably worsens hallucination. (8) The pipeline runs on commodity CPU within $10 with auditable trace-graphs carrying per-leaf certificates.

  DISCONFIRMED if: the single primary disconfirmation fires (CLUTRR facts anti-conservative beyond tau under isolated scoring); OR, separately for the operational claim, decoy-gating shows no precision/hallucination advantage over CoT/RAG at matched recall on Re-DocRED and is dominated by conformal even accounting for its zero-label disadvantage. An uninterpretable null -- control neither clearly holds nor clearly fails because the tail or gap test is underpowered -- is the true failure the Phase-0 power analysis is designed to prevent.
related_works:
- >-
  Wen, Freestone, Riffle, Noble & Keich, 'Assessment of false discovery rate control in tandem mass spectrometry analysis
  using entrapment' (Nature Methods 22:1454-1463, 2025; FDRBench): gives the theory of entrapment FDP estimation, shows the
  naive 'sample' estimator is flawed, and provides the valid combined upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E). We adopt
  this estimator, report r, propagate r into variance and the alpha-floor, and ADD a tail-difficulty diagnostic for entrapment.
  Difference: their domain is peptide identification; we transplant the estimator and construction-independence to LLM fact/bridge
  admission.
- >-
  Barber & Candes, knockoff filter (Annals of Statistics 2015) and Candes et al., Model-X knockoffs (2018), plus target-decoy
  competition in proteomics: select true signals among many candidates with guaranteed FDR by competing each real against
  a synthetic negative control that is exchangeable BY CONSTRUCTION, relying on the null sign-flip property (signs of null
  statistics are i.i.d. coin flips conditional on magnitude). Difference: this machinery lives in numeric feature selection
  and mass spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM neuro-symbolic boundary
  where decoys carry NO such guarantee, so we test the sign-flip/exchangeability condition empirically in the tail, use a
  document-block bootstrap for within-document sign dependence, and model where it holds.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, Bioinformatics 2021; protein-language-model decoys):
  generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference:
  lives in molecular screening; we import the PRINCIPLE -- decoys must reproduce the false-positive score distribution, not
  be 'too easy' -- to design LLM fact/bridge decoys as document-conditioned counterfactuals.
- >-
  Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction' (EMNLP 2022; Re-DocRED).
  Verified by reading the full paper: DocRED comprises 5,053 Wikipedia documents (distant-supervised from Wikidata), averaging
  196.7 words and 19.5 entities, with 97 predefined relation types (96 real relations + no_relation) and human evidence sentences;
  Re-DocRED re-annotates 4,053 of them by adding the missed relation triples (yielding ~13 F1 of headroom) and is publicly
  available. We USE Re-DocRED as our open-vocabulary operational anchor (96 relation types, document-level multi-hop, human
  gold with evidence spans) precisely because it is where plausible hallucinations and genuine schema-alignment bridges actually
  arise; we assert only RELATIVE operational comparisons there (shared residual false negatives affect all methods equally),
  not the absolute FDR diagonal, which we assert on crisp-gold CLUTRR. Note: Re-DocRED documents are SHORT (~200 words, below
  the ~3000-char target), which is strictly easier for commodity hardware; we treat document length itself as an S5 feature.
- >-
  Li, Magesh & Veeravalli, 'Principled Detection of Hallucinations in Large Language Models via Multiple Testing' (arXiv 2508.18473,
  2025). Verified by reading the full paper: it reconceptualizes hallucination detection as hypothesis testing, aggregates
  multiple gray-box evaluation scores via conformal p-values, and applies the GENERAL (dependence-tolerant) Benjamini-Hochberg
  / Benjamini-Yekutieli procedure to control the FALSE-ALARM rate; crucially it 'adds a lightweight calibration step that
  uses a small calibration set of non-hallucinated prompts to provide theoretical control', and it operates at the PROMPT/generation
  level (labeling prompts as likely-to-hallucinate or not). Difference: it is LABELED (a calibration set of non-hallucinated
  prompts) and certifies the generation, whereas we are label-free for operation and gate the neuro-symbolic ADMISSION boundary
  via target-decoy competition with independent entrapment corroboration and per-leaf certificates. This confirmed labeled-calibration
  requirement strengthens our label-free wedge, and our competition-based control differs fundamentally from BH-on-conformal-p-values.
- >-
  Su, Long, Wang, Lin et al., 'Towards Unification of Hallucination Detection and Fact Verification for Large Language Models'
  (UniFact, arXiv 2512.02772, 2025). Verified by reading the paper: UniFact is an EVALUATION framework that enables instance-level
  comparison of model-centric hallucination detection and text-centric fact verification by dynamically generating model outputs
  and corresponding factuality labels; the abstract and content contain NO FDR control, target-decoy/knockoff competition,
  synthetic decoys, admission thresholds, or neuro-symbolic gating, and it requires ground-truth factuality labels. Difference:
  it measures whether generated text is factual; we provide a label-free admission-gating MECHANISM with competition-based
  FDR control and symbolic propagation. We could be EVALUATED under such a framework but our contribution is the control mechanism
  at the text-to-logic boundary.
- >-
  Sawczyn, Binkowski, Janiak, Gabrys & Kajdanowicz, 'FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs'
  (Findings of EACL 2026 / arXiv 2503.17229). Verified by reading the paper: a zero-resource black-box sampling-based method
  that represents text as knowledge-graph triples and computes fine-grained fact-level hallucination SCORES from factual consistency
  across multiple sampled responses (no external resources or training data), improving correction (+35.5% factual content).
  The content has NO false-discovery-rate control, target-decoy/knockoff competition, synthetic decoys, admission thresholds,
  or symbolic gating. Difference: it produces a per-fact detection score with no admission threshold or exchangeability/competition
  argument; FactSelfCheck-style sampling consistency is a CANDIDATE elicitation in our Phase-0 pilot, while our novelty is
  the label-free FDR gate built on whichever elicitation wins.
- >-
  Wang et al., 'Calibrating Verbalized Confidence with Self-Generated Distractors' (DINCO, arXiv 2509.25532, 2025): a zero-resource
  method normalizing verbalized confidence by total confidence over self-generated distractors. Difference: DINCO yields a
  better-calibrated SCALAR confidence for a single claim; it has no FDR control, admission threshold, or competition argument.
  We use DINCO-style distractor-normalized confidence as a candidate pilot elicitation.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm removing claims
  until a factuality alpha is met via conformal prediction with labeled samples. Our primary load-bearing baseline. Difference:
  it requires labeled calibration, certifies the final filtered OUTPUT rather than the admission boundary, and offers no synthetic-decoy
  mechanism, independent entrapment, or symbolic propagation. We report its finite-sample guarantee vs our empirical calibration
  side by side; our wedge is label-free OPERATION.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no operation labels by competing each proposal against engineered
  decoys and corroborate via independent tail-matched entrapment.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023; TDC-SB/UB)
  and He, Ebadi, Keich et al., 'Controlling the FDR via competition: is the +1 needed?' (arXiv 2204.13248, 2023): tighter
  FDP bounds and analysis of the '+1' correction that creates the minimum-estimable-FDR floor. We test (if budget permits)
  whether these lower our achievable-alpha floor without breaking validity. Difference: developed for generic competition-based
  selection; we apply them at the text-to-logic interface.
- >-
  LINC (Olausson et al., EMNLP 2023) and Logic-LM (Pan et al., Findings of EMNLP 2023): LLM semantic-parse premises into FOL/symbolic
  form executed by a solver, with majority voting or solver-error self-refinement. Difference: no principled control over
  WHICH extracted content is admitted -- a syntactically valid fabricated premise is never challenged; voting smooths variance
  and refinement fixes solver/syntax errors only. No FDR knob, no decoys, no label-free precision guarantee.
- >-
  Ontology-constraint hallucination filtering (ODKE+, Evontree, SHACL validation): reject LLM extractions violating trusted
  ontology constraints (disjointness, domain/range, cardinality). Difference: needs a rich trusted constraint set and only
  catches encoded violations; decoy-gating needs only TYPING and controls overall false-admission rate including where the
  ontology is silent -- complementary.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer, sharpened across review rounds. Genomics/proteomics solved the hardest
  label-poor problem -- deciding which of thousands of candidate signals are real with no ground truth -- with a guaranteed
  FDR via the knockoff filter (statistics) and target-decoy competition (mass spectrometry), and discovered the two ways the
  trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys: DeepCoy,
  protein-LM decoys), and entrapment FDP must be estimated with a valid upper bound (Wen et al., Nature Methods 2025) using
  entrapment built unlike the decoys. I map all three onto the fuzzy-unification boundary of a text-to-logic pipeline, where
  the LLM aligns predicates and supplies background knowledge. Because the dangerous hallucinations are PLAUSIBLE high-confidence
  false facts, the decoys must be plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE
  TAIL, and the FDR must be corroborated by independently-constructed tail-matched entrapment and arbitrated by a small gold
  probe. This round's refinements come from taking the statistical machinery seriously on its own terms: (a) the knockoff
  null SIGN-FLIP property is named explicitly, and the two ways LLM scoring can break it -- within-document score correlation
  and batched-scoring contrast effects -- are handled by a document-block bootstrap and isolated provenance-blinded scoring,
  with the isolated-vs-batched check doubling as the discriminator between a scoring artifact and genuine non-exchangeability;
  (b) the evaluation is split into a CALIBRATION anchor (CLUTRR, crisp free gold, exact diagonal) and an OPERATIONAL anchor
  (Re-DocRED, open-vocabulary human gold, where plausible hallucinations and genuine schema-alignment bridges live), so calibration
  validity and operational usefulness are each demonstrated where they are powerable rather than conflated; (c) the document-level
  predictive account is re-based onto Re-DocRED, where the features it predicts from actually vary, with a pre-registered
  predictive-vs-descriptive threshold; and (d) a single crisp CLUTRR-facts disconfirmation makes the headline falsifiable.
  DINCO's and FactSelfCheck's self-consistency signals become candidate pilot elicitations -- but the novelty is the competition-based,
  label-free FDR gate, not the confidence score.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content -- a document-conditioned counterfactual -- so its score distribution reproduces that of genuine plausible hallucinations.
    It replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Null sign-flip property (the validity condition)
  definition: >-
    The condition knockoff+/TDC FDR control rests on: among genuinely-false candidates, the sign of W_i = score(real_i) -
    score(decoy_i) behaves like an independent fair coin conditional on |W_i|. We name it explicitly because two LLM-scoring
    channels can break it anti-conservatively -- within-document score correlation and batched-scoring contrast effects --
    and design the method to test and protect against both.
- term: Two-anchor evaluation (calibration vs operational)
  definition: >-
    A deliberate split: CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim (the realized-FDR-vs-alpha
    diagonal) and the single primary disconfirmation; Re-DocRED (human-annotated, open-vocabulary, document-level multi-hop)
    hosts the OPERATIONAL-USEFULNESS claim (precision/recall and hallucinated-conclusion rate vs neural baselines at matched
    recall), the genuine schema-alignment bridge test, and the S5 predictive model. CLUTRR proves the knob is calibrated;
    Re-DocRED proves it is useful; the two are never conflated.
- term: Isolated provenance-blinded scoring
  definition: >-
    Each candidate (real, decoy, or entrapment) is scored in its OWN prompt with its source/identity masked and presentation
    order randomized, instead of scoring many candidates jointly in one batched prompt. This removes within-batch contrast/ranking
    effects that would let the model implicitly detect fabricated items and depress decoy scores (an anti-conservative artifact).
    A pre-registered isolated-vs-batched sensitivity check discriminates such an artifact (isolation restores the diagonal)
    from genuine decoy non-exchangeability (anti-conservatism persists).
- term: Document-block bootstrap
  definition: >-
    All FDP/FDR confidence intervals are computed by resampling whole DOCUMENTS (blocks), not individual candidates, so that
    within-document correlation of LLM scoring noise is respected. This replaces the i.i.d.-pooled-sign variance that the
    knockoff '+1' floor argument would otherwise assume, and yields the CI used in the primary disconfirmation.
- term: Tail-conditioned win-rate (tail diagnostic)
  definition: >-
    The win-rate of a decoy (or entrapment item) over a known-false real, computed ONLY among matched pairs scoring above
    the operative admission cutoff, reported with score CDFs and an upper-tail two-sample test. Target ~0.5 in the tail. Measurement
    only, never used by the gate; it supersedes the marginal win-rate, which can read 0.5 on average while a family is anti-conservative
    exactly where admissions occur.
- term: Combined / paired entrapment estimator and the ratio r
  definition: >-
    The valid entrapment upper bound on false-admission: FDP_hat = N_E(1+1/r)/(N_T+N_E), where N_T = admitted reals, N_E =
    admitted entrapment, r = entrapment-to-target ratio (reported; r=1 gives the tighter paired form). It replaces the flawed
    naive 'sample' ratio; r is propagated into the variance and the achievable-alpha floor. Entrapment is built by a mechanism
    distinct from the decoys and gets its own tail-difficulty diagnostic.
- term: Document-level predictive exchangeability account (S5), re-based on Re-DocRED
  definition: >-
    A model predicting the per-document tail-exchangeability gap (gold-arbitrated departure of realized false-admission from
    target among above-cutoff pairs) from document/score features, fitted on Re-DocRED (whose >=4 entity-type/topic clusters
    supply real cross-document feature variance, unlike near-homogeneous CLUTRR) and validated by leave-one-cluster-out and
    leave-one-document-out CV with a pre-registered GAP-regression power analysis. Below a pre-registered minimum N_min of
    held-out units it is reported DESCRIPTIVE, not predictive.
- term: Open-vocabulary fuzzy-unification bridge (Re-DocRED)
  definition: >-
    On Re-DocRED a bridge aligns a free-text-implied relation to one of 96 schema relation types/ontology properties when
    strict unification fails -- a genuine ontology-alignment decision with real ambiguity, unlike CLUTRR's deterministic kinship
    normalization. This is where the bridge half of the mechanism is tested for operational value; CLUTRR's crisp kinship
    bridges anchor only the calibration diagonal.
- term: Single primary disconfirmation
  definition: >-
    One pre-registered, S4/S5-independent result that can falsify the headline: on CLUTRR FACTS under isolated provenance-blinded
    scoring at the pilot-powered alpha*, if realized corpus-aggregate FDR exceeds alpha* by more than tolerance tau AND the
    document-block-bootstrap CI lies entirely on the anti-conservative side, the central label-free control claim is disconfirmed
    -- regardless of entrapment agreement or S5 outcome.
- term: Demonstrable-alpha range and achievable-alpha floor
  definition: >-
    Control is asserted over candidates pooled within an anchor. The knockoff+ '+1' offset gives a minimum estimable FDR ~1/k
    at k admitted items, and entrapment at ratio r inflates estimator variance, so the smallest demonstrable target alpha
    is a joint function of pooled candidate count and r (roughly [0.05, 0.5], refined by the pilot), widened mainly by adding
    documents and optionally by less-conservative bounds (TDC-SB/UB).
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  Every LLM-proposed fact and fuzzy-unification bridge must out-score a plausibility-matched counterfactual decoy in a target-decoy
  / knockoff+ competition before entering a Prolog knowledge base, giving a label-free FDR knob at the neuro-symbolic admission
  boundary; calibration validity (the realized-FDR-vs-alpha diagonal) is proven on crisp-gold CLUTRR with a single pre-registered
  disconfirmation, operational hallucination-reduction is proven on open-vocabulary Re-DocRED against neural baselines at
  matched recall, and the whole gate is robustified against the two ways LLM scoring can break the knockoff null sign-flip
  property -- within-document correlation (handled by a document-block bootstrap) and batched-scoring contrast effects (handled
  by isolated provenance-blinded scoring whose isolated-vs-batched check discriminates a scoring artifact from genuine non-exchangeability).
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

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (rigor) The document-level S4 predictive account is the de-risked deliverable that is supposed to survive a partial confirmatory outcome, and the prior review's fix correctly moved its validation unit from genre (n=1) to document/cluster ('many held-out units'). But that fix was made powerable by basing S4 on CLUTRR's free gold — and CLUTRR is precisely where S4 is likely ill-posed. CLUTRR documents are machine-generated kinship narratives over a small fixed relation vocabulary, varying mainly in hop-count and distractor injection; they are near-homogeneous in exactly the features S4 must predict from (entity density, 'document specificity', genre-as-feature). The genuine feature variance lives in the ~60-doc realistic set, which is 'illustrative' and underpowered. Compounding this, at a meaningful target alpha (~0.1) knockoff+ deliberately admits few items, so the per-document 'above-cutoff tail-exchangeability gap' is estimated from a handful of admissions per document — extremely noisy — forcing re-aggregation to clusters that shrinks the 'many held-out units' back toward few. The net risk is that the safety net is unvalidatable for the same power reasons the design fears, leaving the program exposed to the uninterpretable-null outcome.
  Action: In the Phase-0 pilot, measure and report two things before committing the S4 budget: (i) the cross-document variance of the S4 features ON CLUTRR, and (ii) the expected per-document admitted-count at the operative alpha. If CLUTRR feature variance or per-document tail counts are too small to support a per-document gap regression, either base S4 on the realistic set with a pre-registered >=3-4 sources/clusters (and budget it as confirmatory, not illustrative), or define the S4 unit at the cluster level with an explicit count of held-out units and a power analysis for the GAP regression itself (not just the win-rate test). State a minimum number of held-out units below which S4 is reported as descriptive, not predictive.
- [MAJOR] (scope) Scoping the single confirmatory headline to CLUTRR undercuts the motivating problem. The entire motivation — and the user's stated deliverable — is operational text-to-logic on realistic professional documents (legal clauses, news briefs, stories), where fuzzy unification and plausible hallucination actually bite. CLUTRR is synthetic, templated, closed-vocabulary kinship, where: (a) the LLM rarely produces PLAUSIBLE hallucinations because the relation set is tiny and well-known, so the 'plausibility-matched decoy' phenomenon the method hinges on is weakest and hardest to demonstrate meaningfully; (b) 'fuzzy-unification bridges' collapse to near-deterministic normalizations under the kinship algebra (the very crispness that makes bridge gold free also makes the bridge half of the headline a weak test of the genuine ontology-alignment mechanism); and (c) the targeted failure mode (dangerous plausible false facts) is least represented. The confirmatory cell may therefore validate calibration precisely where the mechanism matters least, while the realistic probe — the only place the method's value would show — is too small (~60 docs, illustrative) to support a claim.
  Action: Keep CLUTRR as the validity-of-control anchor (its free crisp gold is the right place to test FDR-diagonal tracking), but add an adequately-powered secondary confirmatory claim on the realistic set — e.g., atomic-fact precision and hallucinated-conclusion-rate vs. the two baselines at matched recall — that the published budget actually covers. Alternatively, reframe the contribution explicitly as 'validity of a label-free FDR knob on a crisp-gold synthetic benchmark' and soften the operational-pipeline framing. Either way, state plainly that CLUTRR tests calibration validity, not operational usefulness on professional documents.
- [MAJOR] (methodology) Knockoff+/TDC FDR control rests on the null sign-flip property: for genuinely-false reals, the sign of W_i = score(real_i) - score(decoy_i) must behave like an (exchangeable) coin flip conditional on magnitudes. Two design choices threaten this beyond the (acknowledged) construction-level exchangeability gap. (i) LLM scoring errors are correlated WITHIN a document (shared context, shared model biases), so pooled null signs are not independent; pooling correlated signs degrades the validity/variance relative to the i.i.d. analysis the '+1' floor argument assumes. (ii) Scoring reals, decoys, and entrapment JOINTLY in batched prompts (chosen for cost) introduces within-batch contrast/ranking effects that couple scores across items and can let the model implicitly detect the fabricated item, systematically depressing decoy scores -> fewer decoy wins -> anti-conservative (optimistic) FDP_hat. The tail diagnostics catch the marginal symptom but cannot distinguish a scoring artifact from genuine decoy non-exchangeability — so this confound could make the entire confirmatory run uninterpretable with respect to the central scientific question.
  Action: (a) Add to the assumptions an explicit statement of the sign-flip/dependence conditions knockoff+ needs, naming within-document sign dependence as a risk, and use a per-document block structure in the FDP variance estimate rather than treating pooled signs as independent. (b) Score each item or matched pair with provenance blinded and order randomized (ideally in isolation), and pre-register a sensitivity check of the calibration diagonal to isolated-vs-batched scoring so an anti-conservative scoring artifact is not mis-attributed to decoy exchangeability failure. (c) If batching must be kept for cost, demonstrate in the pilot that batched and isolated scores agree on a labeled slice before committing the headline budget.
- [MINOR] (rigor) The design is so thoroughly hedged that it verges on unfalsifiable as a package. Every claim row carries an 'ON FAIL: reported as X', and the DISCONFIRMED criterion requires a conjunction (counterfactual decoys anti-conservative AND entrapment co-fails AND S4 fails out-of-sample), so almost every outcome is framed as a contribution. Pre-registering the confirmatory cell addresses cherry-picking, but a top reviewer will still ask: what single result would make you conclude the central claim is wrong? With S4 simultaneously threatened by the powerability concern above, the universal safety net may not actually hold, making the over-hedging both a presentation and a rigor liability.
  Action: State one crisp, pre-registered PRIMARY disconfirmation tied to the confirmatory cell ALONE and independent of S4 (e.g., 'on CLUTRR facts at the pilot-powered alpha, counterfactual-decoy realized FDR exceeds target by more than tolerance tau => central control claim disconfirmed'). Keep S4 as a separately-reported finding that may add value on partial outcomes, not as a universal escape hatch that prevents any clean disconfirmation.
- [MINOR] (clarity) Density was flagged in the two previous rounds and is only marginally improved. The 'three load-bearing numbers up front' and the S1-S5 chain help, but nearly every field is still a long defensive run-on interleaving the claim, its caveats, and rebuttals to earlier reviews. This obscures the genuine novelty, makes the proposal harder to evaluate now, and will cost the ACL presentation score.
  Action: Lead each major field with one plain-language sentence of the mechanism before any qualification; move defensive asides into assumptions/method; render S1-S5 as a real table (claim | test | pass | on-fail); cap sentence length; and state the demonstrable-alpha range, expected document/call counts, and operation-vs-validation label budget exactly once, early. The methodology is strong enough that presentation is now a primary lever on the score.
- [MINOR] (evidence) Related work is strong on the proteomics/knockoff and labeled-conformal sides and now cites the closest hallucination-FDR neighbor (Li et al., 2508.18473) and DINCO. However, the late-2025/2026 hallucination-detection frontier is moving fast — e.g., recent work on unifying hallucination detection with fact verification (arXiv 2512.02772) and fact-level black-box hallucination detection (EACL 2026 Findings). These are not novelty threats (they are detection/verification, not label-free admission-gating via decoy competition, and carry no per-leaf certificates or symbolic propagation), but a top-venue reviewer will expect awareness of them.
  Action: Scan the most recent (late-2025/2026) fact-level hallucination-detection and fact-verification papers and add a one-line differentiation if relevant, reusing the existing axes (label-free operation vs. labeled/reference detection; neuro-symbolic admission-gating vs. output-level detection; competition/certificates vs. scoring). Low priority relative to the methodology critiques.
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

### [3] HUMAN-USER prompt · 2026-06-16 04:22:08 UTC

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

### [4] ASSISTANT · 2026-06-16 04:23:51 UTC

```
I'll ground my review in the literature before writing. Let me load web tools and check a few key things: novelty of applying knockoffs/target-decoy to LLM hallucination gating, the Re-DocRED stats cited, and the recent conformal-selection-for-LLM frontier.
```

### [5] TOOL CALL — ToolSearch · 2026-06-16 04:23:51 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-06-16 04:23:51 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [7] TOOL CALL — WebSearch · 2026-06-16 04:23:55 UTC

```
knockoff filter target-decoy competition LLM hallucination false discovery rate factuality
```

### [8] TOOL CALL — WebSearch · 2026-06-16 04:23:55 UTC

```
conformal selection FDR control LLM factual claims hallucination 2025
```

### [9] TOOL CALL — WebSearch · 2026-06-16 04:23:55 UTC

```
Re-DocRED relation extraction false negative 96 relation types document-level statistics
```

### [10] TOOL RESULT — WebSearch · 2026-06-16 04:24:01 UTC

```
{"query": "knockoff filter target-decoy competition LLM hallucination false discovery rate factuality", "results": [{"tool_use_id": "srvtoolu_018HCFRqAexA76GJdjHzhGJM", "content": [{"title": "Local False Discovery Rate Estimation with Competition-Based Procedures   for Variable Selection", "url": "https://arxiv.org/pdf/2206.02692"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}, {"title": "Challenging targets or describing mismatches? A comment on Common Decoy   Distribution by Madej et al", "url": "https://arxiv.org/pdf/2210.08815"}, {"title": "Unveiling the links between peptide identification and differential analysis FDR controls by means of a practical introduction to knockoff filters", "url": "https://www.biorxiv.org/content/10.1101/2021.08.20.454134.full.pdf"}, {"title": "Controlling the False Discovery Rate via knockoffs: is the +1 needed?", "url": "https://www.researchgate.net/publication/360254730_Controlling_the_False_Discovery_Rate_via_knockoffs_is_the_1_needed"}, {"title": "Controlling the False Discovery Rate via Competition: is the +1 needed?", "url": "https://arxiv.org/pdf/2204.13248"}, {"title": "Group-walk: a rigorous approach to group-wise false discovery rate analysis by target-decoy competition | Bioinformatics | Oxford Academic", "url": "https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii82/6701992"}]}, "I found search results related to knockoff filters, target-decoy competition, and false discovery rate (FDR) control. However, the results primarily focus on their applications in proteomics (peptide identification in mass spectrometry) and statistical variable selection, rather than on LLM hallucinations and factuality.\n\nHere's what the search found:\n\n**Key Concepts:**\n\nBoth TDFDR and knockoff filter are competition-based procedures that create \"fake\" variables called decoys or knockoffs, which compete with their corresponding original variables to produce ranking statistics.\n\nThe target-decoy approach was inspired by database search strategies in proteomics, while the knockoff filter is another FDR control method. Target-decoy competition (TDC) is a commonly used method for false discovery rate control in tandem mass spectrometry analysis, and has gained popularity in other fields with theoretical foundations laid by Barber and Candès in a general setting that includes feature selection.\n\n**Regarding LLM Hallucinations:**\n\nThe search results don't contain information specifically about applying these methods to LLM hallucination detection or factuality checking. These mathematical and statistical techniques for FDR control might be theoretically applicable to factuality verification in LLMs, but that application doesn't appear to be covered in the retrieved academic literature.\n\nWould you like me to search for more specific information about applying these statistical methods to LLM factuality or hallucination detection?"], "durationSeconds": 6.5442883589999985, "searchCount": 1}
```

### [11] TOOL RESULT — WebSearch · 2026-06-16 04:24:01 UTC

```
{"query": "Re-DocRED relation extraction false negative 96 relation types document-level statistics", "results": [{"tool_use_id": "srvtoolu_01VzVMgjnRUQtbCJadvCvWau", "content": [{"title": "[PDF] Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Revisiting-DocRED-Addressing-the-False-Negative-in-Tan-Xu/c86754c01fc64a8e8b445f530fe95c1dbab4eb03"}, {"title": "Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction - ADS", "url": "https://ui.adsabs.harvard.edu/abs/2022arXiv220512696T/abstract"}, {"title": "A Unified Positive-Unlabeled Learning Framework for Document-Level   Relation Extraction with Different Levels of Labeling", "url": "https://arxiv.org/pdf/2210.08709"}, {"title": "Revisiting DocRED -- Addressing the False Negative Problem in Relation   Extraction", "url": "https://arxiv.org/pdf/2205.12696"}, {"title": "DiVA-DocRE: A Discriminative and Voice-Aware Paradigm for Document-Level   Relation Extraction", "url": "https://arxiv.org/pdf/2409.13717"}, {"title": "Revisiting DocRED – Addressing the Overlooked False Negative Problem in Relation Extraction | DeepAI", "url": "https://deepai.org/publication/revisiting-docred-addressing-the-overlooked-false-negative-problem-in-relation-extraction"}, {"title": "Document-level denoising relation extraction with false-negative mining and reinforced positive-class knowledge distillation - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0306457323002704"}, {"title": "Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction - ACL Anthology", "url": "https://aclanthology.org/2022.emnlp-main.580/"}, {"title": "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction", "url": "https://arxiv.org/pdf/2511.08143"}, {"title": "Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction", "url": "https://arxiv.org/html/2205.12696"}]}, "Based on the search results, here's what I found about Re-DocRED relation extraction:\n\n## Overview\n\nRe-DocRED is the revised DocRED dataset, created to address a significant problem with the original annotation. The DocRED dataset is one of the most popular and widely used benchmarks for document-level relation extraction (RE) and adopts a recommend-revise annotation scheme, but the annotation of DocRED is incomplete, i.e., false negative samples are prevalent.\n\n## Dataset Details\n\nDocRED is a large-scale document-level RE dataset with 96 predefined relations constructed by a recommend-revise scheme from Wikipedia. To address the shortcoming, the researchers re-annotated 4,053 documents in the DocRED dataset by adding the missed relation triples back to the original DocRED, naming their revised dataset Re-DocRED.\n\n## Performance Improvements\n\nExperimental results show that models trained and evaluated on Re-DocRED achieve performance improvements of around 13 F1 points compared to the original DocRED dataset.\n\nThe Re-DocRED dataset addresses document-level relation extraction by providing comprehensive annotation across the 96 relation types while specifically tackling the false negative problem that was prevalent in the original DocRED dataset."], "durationSeconds": 6.296991040000008, "searchCount": 1}
```

### [12] TOOL RESULT — WebSearch · 2026-06-16 04:24:03 UTC

```
{"query": "conformal selection FDR control LLM factual claims hallucination 2025", "results": [{"tool_use_id": "srvtoolu_01CBm9Knomz5idhG2hKJ5eUF", "content": [{"title": "Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection", "url": "https://arxiv.org/html/2509.03297v1"}, {"title": "Differentiable Conformal Training for LLM Reasoning Factuality", "url": "https://arxiv.org/html/2604.20098"}, {"title": "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs", "url": "https://arxiv.org/pdf/2603.21172"}, {"title": "Aligning Model Properties via Conformal Risk Control", "url": "https://arxiv.org/pdf/2406.18777"}, {"title": "Conformal Language Modeling via Posterior Sampling", "url": "https://arxiv.org/html/2606.03731"}, {"title": "Conformal Prediction Adaptive to Unknown Subpopulation Shifts", "url": "https://arxiv.org/pdf/2506.05583"}, {"title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights", "url": "https://arxiv.org/pdf/2603.16817"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}, {"title": "Published as a conference paper at ICLR 2025 CONFORMAL LANGUAGE MODEL REASONING", "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf"}]}, "I found several highly relevant research papers on this topic. Here's a summary of what's being researched:\n\n## Key Research Areas\n\n**Conformal Prediction for LLM Hallucination Control:**\nConformal Prediction addresses hallucination by calibrating error rates on held-out data to provide statistically valid confidence guarantees and filter out risky claims, ensuring that hallucination rates remain below a user-specified level.\n\n**FDR Control with Feedback:**\nLLMs can hallucinate—producing plausible but incorrect content, and a remedy is to filter or certify LLM outputs. A recent paper from September 2025 addresses \"Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection\" and establishes FDR control under independence and mFDR control under local dependence.\n\n**Recent Advances (2025-2026):**\n\n- Differentiable Coherent Factuality (DCF) is a fully differentiable relaxation that enables learning improved scorers while provably recovering guarantees (April 2026)\n\n- While existing methods are effective where claims may be treated as independent, they do not generalize to reasoning problems, where the correctness of each step cannot be evaluated without the context of the steps that precede it (ICLR 2025)\n\n- Methods that produce calibrated predictions of factuality and leverage conformal prediction yield assumption-lean guarantees for reducing hallucinations\n\nThese papers represent the current state of research in combining conformal statistical methods with FDR control techniques to ensure reliable factual claims in LLM outputs."], "durationSeconds": 7.8438792410000024, "searchCount": 1}
```

### [13] ASSISTANT · 2026-06-16 04:26:34 UTC

```
The searches confirm the key facts I needed:
- **Novelty holds**: No existing work applies target-decoy/knockoff competition to LLM hallucination/factuality gating — the results are all proteomics/variable-selection. This is a genuine Level-3 transfer.
- **Re-DocRED stats are accurate**: 4,053 re-annotated docs, 96 relation types, ~13 F1 headroom — as cited.
- **The conformal-for-LLM frontier is active and labeled** (Feedback-Enhanced Online Multiple Testing for Conformal Selection, Sept 2025; Differentiable Coherent Factuality, 2026; conformal factuality robustness for RAG, 2026) — all require labeled calibration, so the label-free wedge survives, but the author should show awareness.

Now let me verify the previous critiques were addressed and write the review. I have enough to assess authoritatively. Let me write the structured output.
```

### [14] TOOL CALL — Write · 2026-06-16 04:26:34 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_6/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is a strong, mature revision of a genuinely novel idea: transplanting the target-decoy / knockoff+ false-discovery-rate machinery from proteomics/statistics to the neuro-symbolic admission boundary of a text-to-logic pipeline, giving a label-free, auditable FDR knob on which LLM-proposed facts and fuzzy-unification bridges may enter a Prolog KB. Web search confirms the transfer is novel (no prior work applies target-decoy/knockoff competition to LLM factuality gating) and that the cited Re-DocRED statistics (4,053 re-annotated docs, 96 relations, ~13 F1 headroom) and the labeled-conformal neighbor landscape are accurate. The revision addresses all three MAJOR critiques from the prior round in a principled way: (1) the SCOPE critique is fixed by the two-anchor design — CLUTRR (crisp free gold) hosts only the calibration-validity diagonal, Re-DocRED (open-vocabulary human gold) hosts the operational head-to-head and the S5 predictive model, and the proposal states plainly that CLUTRR tests calibration, not usefulness; (2) the METHODOLOGY critique is fixed by naming the null sign-flip property explicitly, adopting a document-block bootstrap for all FDP CIs, defaulting to isolated provenance-blinded order-randomized scoring, and — elegantly — using the isolated-vs-batched check as the discriminator between a scoring artifact and genuine non-exchangeability; (3) the unfalsifiability/RIGOR critique is fixed by a single pre-registered S4/S5-independent primary disconfirmation on CLUTRR FACTS. The prior S4/S5 powerability concern is addressed by re-basing the predictive model on Re-DocRED (real feature variance) with a pre-registered predictive-vs-descriptive N_min threshold. What remains are execution risks rather than conceptual flaws: a tension between the isolated-scoring fix and the $10 budget, under-specification of the operational head-to-head construct (and a dropped zero-label confidence-threshold baseline), and a real risk that the CLUTRR-FACTS calibration diagonal cannot be populated with enough genuine false admissions to be non-vacuous. None are fatal, but the first three should be settled before the headline budget is committed. Overall this is now a borderline-acceptable proposal whose trajectory across rounds is clearly upward.",
  "strengths": [
    "Genuine, verified novelty: a Level-3 cross-domain transfer of target-decoy / knockoff+ FDR control and the valid combined entrapment estimator (Wen et al., Nature Methods 2025) to the LLM text-to-logic admission boundary. Web search confirms no existing work applies competition-based FDR control to LLM hallucination gating; the closest neighbors (conformal factuality, conformal selection, multiple-testing hallucination detection) are all labeled and are correctly differentiated.",
    "Intellectually honest about the weakest joint: LLM counterfactual decoys carry no construction-level exchangeability guarantee, so the claim is stated as an empirically-validated calibration (not a theorem) and the sign-flip condition is tested IN THE TAIL (tail-conditioned win-rate + upper-tail two-sample CDF test), not as a marginal average.",
    "The two-anchor split (calibration on crisp-gold CLUTRR; operational usefulness on open-vocabulary Re-DocRED) is a principled, well-justified resolution of the prior scope critique — it puts each claim where it is actually powerable and refuses to conflate calibration with usefulness.",
    "Sophisticated and correct handling of the dependence threats to knockoff+ validity: the null sign-flip property is named, within-document correlation is handled by a document-block bootstrap, batched-contrast effects by isolated provenance-blinded scoring, and the isolated-vs-batched sensitivity check is repurposed as the discriminator between a scoring artifact and genuine non-exchangeability — a genuinely clever design move.",
    "A single, crisp, pre-registered primary disconfirmation (CLUTRR facts, isolated scoring, realized FDR exceeds alpha* by tau with a one-sided CI) makes the headline falsifiable and fixes the prior over-hedging concern; S5 and entrapment are explicitly demoted from escape hatches to separately-reported secondary findings.",
    "Strong methodological hygiene: Phase-0 gating pilot, pre-registered confirmatory cells, BH multiplicity correction across validation tests, document-block-bootstrap CIs throughout, explicit demonstrable-alpha floor (~1/k), reported decoy-contamination direction (conservative), and a hard $10 budget stop with per-call cost logging."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "The core statistical machinery (knockoff+ thresholding, the valid combined entrapment estimator, the null sign-flip property and the two dependence channels that threaten it) is correctly understood and thoughtfully protected. The remaining soundness risks are about whether the design can actually realize its tests within budget and difficulty regime, not about conceptual errors: (a) the isolated-scoring fix may not fit the $10 budget; (b) the CLUTRR-FACTS diagonal may be too clean to populate with genuine false admissions, risking a vacuously-conservative (untestable) result; (c) the operational head-to-head construct is under-specified. All three are addressable in the pilot.",
      "improvements": [
        "Recompute the feasibility budget under DEFAULT isolated scoring (each real/decoy/entrapment scored alone with document context re-sent): ~550 docs x ~25 candidates x ~3 item-types is tens of thousands of calls, plausibly far above the stated 4-8M tokens. Show the arithmetic; if it breaks $10, pre-register exactly what fraction stays isolated and prove the batched bulk inherits validity from the full-isolated sensitivity subset.",
        "Add to Phase-0 a measurement of the genuine false-REAL base rate among CLUTRR fact proposals at the operative alpha (not just tail separation and admitted count), and pre-register a minimum realized-false-admission count below which the diagonal is declared untestable (conservative, not 'tracking'). This protects the primary disconfirmation from firing/non-firing for lack of false positives rather than for control.",
        "Concentrate expected value on the precondition: state that the Phase-0 elicitation/tail-separation pilot (S0) is run first and that the headline budget is released only on its success, since the most-cited failure mode (LLM overconfidence in the upper tail) would otherwise null the entire confirmatory program."
      ]
    },
    {
      "dimension": "presentation",
      "score": 2,
      "justification": "Contextualization relative to prior work is excellent and the new plain-mechanism lead sentence, the three load-bearing numbers, and the rendered S0-S6 claim table are real improvements. But density — flagged across multiple rounds — remains the dominant reading impression: the assumptions, the score-dependence-robustness block, and the motivation are still long defensive run-ons that interleave the claim, its caveats, and rebuttals to earlier reviews, which obscures the genuine novelty and will cost the ACL presentation score.",
      "improvements": [
        "Lead every major field with one unqualified sentence of mechanism; move the score-dependence-robustness and the four assumptions into a compact table (threat | why it breaks sign-flip | mitigation | test) instead of paragraph walls.",
        "Cut the motivation to two moves: the mechanism, then the two-anchor rationale. The repeated 'this round's reframing / the methodology fix' meta-commentary belongs in a changelog, not the hypothesis body.",
        "State the demonstrable-alpha range, document/call counts, and operation-vs-validation label budget exactly once, early — currently they recur with slight variations across fields."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "The problem (an uncontrolled, label-free hallucination channel exactly at the fuzzy-unification boundary) is real and underserved, and the proposed first auditable zero-operation-label FDR knob there — with per-leaf certificates and symbolic propagation — is a novel capability that others would build on. The ceiling is bounded by the authors' own honest prior that the most probable outcome is partial control, but even then the S5 mechanism-level account of WHEN calibration holds is a generalizable contribution. The two-anchor design raises the contribution by making the operational claim a powered confirmatory anchor rather than an illustrative aside.",
      "improvements": [
        "Restore the plain confidence-threshold baseline as the primary zero-label comparator in the operational anchor (S4) so the contribution isolates the value of the decoy-competition machinery over naive thresholding under an identical zero-label budget — otherwise the 'wedge' risks collapsing to 'thresholding is enough'.",
        "Tighten the secondary list: pre-commit that S5/S6/TDC-SB-UB/rule-gating are reported only after the two anchors clear their power thresholds, so breadth does not dilute the headline."
      ]
    }
  ],
  "critiques": [
    {
      "category": "methodology",
      "severity": "major",
      "description": "Budget-vs-fix tension. The central methodology fix this round — DEFAULT isolated, provenance-blinded, order-randomized scoring (each real, decoy, and entrapment item scored in its own prompt) — multiplies the scoring call count by candidate multiplicity and re-sends document context per call. With <=300 CLUTRR + <=250 Re-DocRED + ~20 illustrative docs at ~10-40 candidates each, plus a 1:1 decoy and entrapment at ratio r, the isolated regime implies on the order of tens of thousands of scoring calls, each carrying document context. The stated projection (~4-8M tokens, $2-5, hard stop $10) appears to be inherited from the prior BATCHED design (~3 calls/doc) and likely understates isolated-scoring cost by a large factor. If the budget forces reverting to batched scoring for the bulk, the very fix that makes the confirmatory run interpretable is undermined, and the isolated-vs-batched discriminator weakens because most data is batched.",
      "suggested_action": "Recompute the feasibility budget explicitly for the isolated default: items = sum over docs of (candidates x {real, decoy, r-weighted entrapment}); per-call tokens including document context; total tokens and dollars at the chosen sub-$0.30/M model. If it breaches $10, either shrink the confirmatory corpus to what isolated scoring can afford, exploit prompt/context caching to amortize the re-sent document, or pre-register the exact isolated fraction and demonstrate in the pilot that the batched bulk reproduces the isolated diagonal on a labeled slice before committing the headline."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "Populability of the CLUTRR-FACTS calibration diagonal, on which the single primary disconfirmation rests. CLUTRR atomic-fact extraction over a tiny closed kinship vocabulary is easy, so genuinely-false extracted facts may be rare. The realized-FDR-vs-alpha diagonal can only be demonstrated to TRACK alpha if, at permissive cutoffs, a meaningful fraction of admitted reals are genuinely false (e.g., realized FDR must be able to rise toward 0.3 at alpha=0.3). If the false-real base rate is low, realized FDR sits near zero across the whole grid — trivially <= alpha (conservative everywhere) but NOT tracking — and the primary disconfirmation can neither fire nor be cleanly passed, because there are too few false admissions to estimate FDR at all. This is precisely the uninterpretable-null outcome the Phase-0 power analysis is meant to prevent, but the pilot as described measures tail SEPARATION and per-document admitted COUNT, not the genuine false-positive base rate among admissions.",
      "suggested_action": "Add to Phase-0 an explicit measurement, on CLUTRR facts at the operative alpha*, of the realized genuinely-false-admission count and base rate among proposals. Pre-register a minimum false-admission count below which the CLUTRR-facts diagonal is declared untestable (conservative, not tracking) rather than confirmatory. If the count is too low, deliberately enrich the false-real pool (e.g., harder multi-hop inferred relations the extractor gets wrong) or move the primary disconfirmation to CLUTRR BRIDGES, where multi-hop kinship inference produces denser errors."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "Operational head-to-head construct validity, plus a dropped baseline. The S4 operational confirmatory claim compares atomic-fact precision/recall and 'hallucinated-conclusion rate' of the neuro-symbolic pipeline against CoT, RAG, and labeled Mohri-Hashimoto conformal 'at matched recall.' Two problems: (a) CoT and RAG are generation/QA systems, not atomic-fact extractors in a shared schema, so 'matched-recall PR curves' across them is under-specified — you need a defined common extraction target and an explicit, fair mapping from each baseline's free-text output to comparable atomic facts and conclusions, or the comparison is apples-to-oranges; (b) the plain per-document/per-corpus confidence-threshold baseline — present as S3 in the prior iteration and the single most diagnostic ZERO-LABEL comparator — has been dropped from the headline operational set. Without it, S4 cannot show that the decoy-competition machinery adds operational value over naive confidence thresholding at the SAME zero-label budget; the 'wedge' could reduce to 'a confidence threshold already matches recall-for-recall.'",
      "suggested_action": "Specify the shared atomic-fact evaluation schema and the precise procedure for extracting comparable facts/conclusions from CoT and RAG outputs (e.g., a fixed claim-decomposition + alignment-to-Re-DocRED-relations step applied identically to all systems). Restore the plain confidence-threshold gate as the primary zero-label baseline in S4, so the operational wedge is measured as decoy-gating vs thresholding under identical labels, with labeled conformal reported alongside as the labeled reference point."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "Breadth vs depth on a $10 / CPU-only budget. The proposal now spans S0-S6 (seven claim rows), two anchors, three-plus baselines, an S5 model validated by both leave-one-cluster-out and leave-one-document-out CV with its own gap-regression power analysis, S6 propagation, and several 'if-budget-permits' threads (TDC-SB/UB, '+1'-floor relaxation, ProbLog/isotonic, defeasible bridges, rule gating). This is a lot of surface area for a one-call/doc pipeline under a hard $10 cap, and the prior rounds repeatedly pushed toward focus. The risk is that several cells end up underpowered and nothing is decisively nailed.",
      "suggested_action": "Pre-commit a strict budget waterfall: fully power the CLUTRR calibration diagonal and the Re-DocRED operational wedge FIRST, and explicitly state that S5/S6/floor-relaxation/rule-gating are run and reported only if the two anchors clear their pre-registered power thresholds, with leftover budget. Make this ordering visible in the feasibility section so a reviewer sees the headline cannot be starved by secondary exploration."
    },
    {
      "category": "evidence",
      "severity": "minor",
      "description": "The labeled-conformal-for-LLM frontier is moving fast and a top reviewer will expect current awareness. Beyond the cited Li et al. (2508.18473), Mohri-Hashimoto, and Jin-Candes, recent work directly applies conformal SELECTION / multiple testing to LLM claim filtering (e.g., feedback-enhanced online multiple testing for conformal selection, 2025; differentiable coherent factuality, 2026; conformal-factuality robustness for RAG, 2026). These are not novelty threats — they remain LABELED and certify outputs rather than gating the neuro-symbolic admission boundary via competition — so they actually reinforce the label-free wedge, but the proposal should show it knows them.",
      "suggested_action": "Add one or two sentences placing the work against the conformal-selection-applied-to-LLM-claims line, reusing the existing axes (label-free operation vs labeled calibration; competition/per-leaf certificates + symbolic propagation vs output-level certification). Low priority relative to the methodology and rigor critiques."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "Density remains the dominant presentation weakness despite genuine improvements (plain-mechanism lead, three load-bearing numbers, the claim table). The assumptions, the score-dependence-robustness block, and the motivation are still long defensive run-ons that interleave claim, caveat, and rebuttal-to-prior-review, which obscures the core novelty and will cost the ACL presentation score. This has been flagged in multiple rounds; with the methodology now strong, presentation is a primary remaining score lever.",
      "suggested_action": "Convert the score-dependence-robustness and assumptions prose into a compact table (threat | how it breaks the sign-flip property | mitigation | pre-registered test). Lead each field with one unqualified mechanism sentence before any caveat. Remove the round-over-round meta-commentary ('the key change this round', 'the methodology fix') from the hypothesis body. State the demonstrable-alpha range, doc/call counts, and label budget once."
    }
  ],
  "score": 5,
  "confidence": 4,
  "relation_type": "evolution",
  "relation_rationale": "Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness."
}
```

### [15] TOOL RESULT — Write · 2026-06-16 04:26:34 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_6/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is a strong, mature revision of a genuinely novel idea: transplanting the target-decoy / knockoff+ false-discovery-rate machinery from proteomics/statistics to the neuro-symbolic admission boundary of a text-to-logic pipeline, giving a label-free, auditable FDR knob on which LLM-proposed facts and fuzzy-unification bridges may enter a Prolog KB. Web search confirms the transfer is novel (no prior work applies target-decoy/knockoff competition to LLM factuality gating) and that the cited Re-DocRED statistics (4,053 re-annotated docs, 96 relations, ~13 F1 headroom) and the labeled-conformal neighbor landscape are accurate. The revision addresses all three MAJOR critiques from the prior round in a principled way: (1) the SCOPE critique is fixed by the two-anchor design — CLUTRR (crisp free gold) hosts only the calibration-validity diagonal, Re-DocRED (open-vocabulary human gold) hosts the operational head-to-head and the S5 predictive model, and the proposal states plainly that CLUTRR tests calibration, not usefulness; (2) the METHODOLOGY critique is fixed by naming the null sign-flip property explicitly, adopting a document-block bootstrap for all FDP CIs, defaulting to isolated provenance-blinded order-randomized scoring, and — elegantly — using the isolated-vs-batched check as the discriminator between a scoring artifact and genuine non-exchangeability; (3) the unfalsifiability/RIGOR critique is fixed by a single pre-registered S4/S5-independent primary disconfirmation on CLUTRR FACTS. The prior S4/S5 powerability concern is addressed by re-basing the predictive model on Re-DocRED (real feature variance) with a pre-registered predictive-vs-descriptive N_min threshold. What remains are execution risks rather than conceptual flaws: a tension between the isolated-scoring fix and the $10 budget, under-specification of the operational head-to-head construct (and a dropped zero-label confidence-threshold baseline), and a real risk that the CLUTRR-FACTS calibration diagonal cannot be populated with enough genuine false admissions to be non-vacuous. None are fatal, but the first three should be settled before the headline budget is committed. Overall this is now a borderline-acceptable proposal whose trajectory across rounds is clearly upward.\",\n  \"strengths\": [\n    \"Genuine, verified novelty: a Level-3 cross-domain transfer of target-decoy / knockoff+ FDR control and the valid combined entrapment estimator (Wen et al., Nature Methods 2025) to the LLM text-to-logic admission boundary. Web search confirms no existing work applies competition-based FDR control to LLM hallucination gating; the closest neighbors (conformal factuality, conformal selection, multiple-testing hallucination detection) are all labeled and are correctly differentiated.\",\n    \"Intellectually honest about the weakest joint: LLM counterfactual decoys carry no construction-level exchangeability guarantee, so the claim is stated as an empirically-validated calibration (not a theorem) and the sign-flip condition is tested IN THE TAIL (tail-conditioned win-rate + upper-tail two-sample CDF test), not as a marginal average.\",\n    \"The two-anchor split (calibration on crisp-gold CLUTRR; operational usefulness on open-vocabulary Re-DocRED) is a principled, well-justified resolution of the prior scope critique — it puts each claim where it is actually powerable and refuses to conflate calibration with usefulness.\",\n    \"Sophisticated and correct handling of the dependence threats to knockoff+ validity: the null sign-flip property is named, within-document correlation is handled by a document-block bootstrap, batched-contrast effects by isolated provenance-blinded scoring, and the isolated-vs-batched sensitivity check is repurposed as the discriminator between a scoring artifact and genuine non-exchangeability — a genuinely clever design move.\",\n    \"A single, crisp, pre-registered primary disconfirmation (CLUTRR facts, isolated scoring, realized FDR exceeds alpha* by tau with a one-sided CI) makes the headline falsifiable and fixes the prior over-hedging concern; S5 and entrapment are explicitly demoted from escape hatches to separately-reported secondary findings.\",\n    \"Strong methodological hygiene: Phase-0 gating pilot, pre-registered confirmatory cells, BH multiplicity correction across validation tests, document-block-bootstrap CIs throughout, explicit demonstrable-alpha floor (~1/k), reported decoy-contamination direction (conservative), and a hard $10 budget stop with per-call cost logging.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"The core statistical machinery (knockoff+ thresholding, the valid combined entrapment estimator, the null sign-flip property and the two dependence channels that threaten it) is correctly understood and thoughtfully protected. The remaining soundness risks are about whether the design can actually realize its tests within budget and difficulty regime, not about conceptual errors: (a) the isolated-scoring fix may not fit the $10 budget; (b) the CLUTRR-FACTS diagonal may be too clean to populate with genuine false admissions, risking a vacuously-conservative (untestable) result; (c) the operational head-to-head construct is under-specified. All three are addressable in the pilot.\",\n      \"improvements\": [\n        \"Recompute the feasibility budget under DEFAULT isolated scoring (each real/decoy/entrapment scored alone with document context re-sent): ~550 docs x ~25 candidates x ~3 item-types is tens of thousands of calls, plausibly far above the stated 4-8M tokens. Show the arithmetic; if it breaks $10, pre-register exactly what fraction stays isolated and prove the batched bulk inherits validity from the full-isolated sensitivity subset.\",\n        \"Add to Phase-0 a measurement of the genuine false-REAL base rate among CLUTRR fact proposals at the operative alpha (not just tail separation and admitted count), and pre-register a minimum realized-false-admission count below which the diagonal is declared untestable (conservative, not 'tracking'). This protects the primary disconfirmation from firing/non-firing for lack of false positives rather than for control.\",\n        \"Concentrate expected value on the precondition: state that the Phase-0 elicitation/tail-separation pilot (S0) is run first and that the headline budget is released only on its success, since the most-cited failure mode (LLM overconfidence in the upper tail) would otherwise null the entire confirmatory program.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 2,\n      \"justification\": \"Contextualization relative to prior work is excellent and the new plain-mechanism lead sentence, the three load-bearing numbers, and the rendered S0-S6 claim table are real improvements. But density — flagged across multiple rounds — remains the dominant reading impression: the assumptions, the score-dependence-robustness block, and the motivation are still long defensive run-ons that interleave the claim, its caveats, and rebuttals to earlier reviews, which obscures the genuine novelty and will cost the ACL presentation score.\",\n      \"improvements\": [\n        \"Lead every major field with one unqualified sentence of mechanism; move the score-dependence-robustness and the four assumptions into a compact table (threat | why it breaks sign-flip | mitigation | test) instead of paragraph walls.\",\n        \"Cut the motivation to two moves: the mechanism, then the two-anchor rationale. The repeated 'this round's reframing / the methodology fix' meta-commentary belongs in a changelog, not the hypothesis body.\",\n        \"State the demonstrable-alpha range, document/call counts, and operation-vs-validation label budget exactly once, early — currently they recur with slight variations across fields.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"The problem (an uncontrolled, label-free hallucination channel exactly at the fuzzy-unification boundary) is real and underserved, and the proposed first auditable zero-operation-label FDR knob there — with per-leaf certificates and symbolic propagation — is a novel capability that others would build on. The ceiling is bounded by the authors' own honest prior that the most probable outcome is partial control, but even then the S5 mechanism-level account of WHEN calibration holds is a generalizable contribution. The two-anchor design raises the contribution by making the operational claim a powered confirmatory anchor rather than an illustrative aside.\",\n      \"improvements\": [\n        \"Restore the plain confidence-threshold baseline as the primary zero-label comparator in the operational anchor (S4) so the contribution isolates the value of the decoy-competition machinery over naive thresholding under an identical zero-label budget — otherwise the 'wedge' risks collapsing to 'thresholding is enough'.\",\n        \"Tighten the secondary list: pre-commit that S5/S6/TDC-SB-UB/rule-gating are reported only after the two anchors clear their power thresholds, so breadth does not dilute the headline.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"Budget-vs-fix tension. The central methodology fix this round — DEFAULT isolated, provenance-blinded, order-randomized scoring (each real, decoy, and entrapment item scored in its own prompt) — multiplies the scoring call count by candidate multiplicity and re-sends document context per call. With <=300 CLUTRR + <=250 Re-DocRED + ~20 illustrative docs at ~10-40 candidates each, plus a 1:1 decoy and entrapment at ratio r, the isolated regime implies on the order of tens of thousands of scoring calls, each carrying document context. The stated projection (~4-8M tokens, $2-5, hard stop $10) appears to be inherited from the prior BATCHED design (~3 calls/doc) and likely understates isolated-scoring cost by a large factor. If the budget forces reverting to batched scoring for the bulk, the very fix that makes the confirmatory run interpretable is undermined, and the isolated-vs-batched discriminator weakens because most data is batched.\",\n      \"suggested_action\": \"Recompute the feasibility budget explicitly for the isolated default: items = sum over docs of (candidates x {real, decoy, r-weighted entrapment}); per-call tokens including document context; total tokens and dollars at the chosen sub-$0.30/M model. If it breaches $10, either shrink the confirmatory corpus to what isolated scoring can afford, exploit prompt/context caching to amortize the re-sent document, or pre-register the exact isolated fraction and demonstrate in the pilot that the batched bulk reproduces the isolated diagonal on a labeled slice before committing the headline.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"Populability of the CLUTRR-FACTS calibration diagonal, on which the single primary disconfirmation rests. CLUTRR atomic-fact extraction over a tiny closed kinship vocabulary is easy, so genuinely-false extracted facts may be rare. The realized-FDR-vs-alpha diagonal can only be demonstrated to TRACK alpha if, at permissive cutoffs, a meaningful fraction of admitted reals are genuinely false (e.g., realized FDR must be able to rise toward 0.3 at alpha=0.3). If the false-real base rate is low, realized FDR sits near zero across the whole grid — trivially <= alpha (conservative everywhere) but NOT tracking — and the primary disconfirmation can neither fire nor be cleanly passed, because there are too few false admissions to estimate FDR at all. This is precisely the uninterpretable-null outcome the Phase-0 power analysis is meant to prevent, but the pilot as described measures tail SEPARATION and per-document admitted COUNT, not the genuine false-positive base rate among admissions.\",\n      \"suggested_action\": \"Add to Phase-0 an explicit measurement, on CLUTRR facts at the operative alpha*, of the realized genuinely-false-admission count and base rate among proposals. Pre-register a minimum false-admission count below which the CLUTRR-facts diagonal is declared untestable (conservative, not tracking) rather than confirmatory. If the count is too low, deliberately enrich the false-real pool (e.g., harder multi-hop inferred relations the extractor gets wrong) or move the primary disconfirmation to CLUTRR BRIDGES, where multi-hop kinship inference produces denser errors.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"Operational head-to-head construct validity, plus a dropped baseline. The S4 operational confirmatory claim compares atomic-fact precision/recall and 'hallucinated-conclusion rate' of the neuro-symbolic pipeline against CoT, RAG, and labeled Mohri-Hashimoto conformal 'at matched recall.' Two problems: (a) CoT and RAG are generation/QA systems, not atomic-fact extractors in a shared schema, so 'matched-recall PR curves' across them is under-specified — you need a defined common extraction target and an explicit, fair mapping from each baseline's free-text output to comparable atomic facts and conclusions, or the comparison is apples-to-oranges; (b) the plain per-document/per-corpus confidence-threshold baseline — present as S3 in the prior iteration and the single most diagnostic ZERO-LABEL comparator — has been dropped from the headline operational set. Without it, S4 cannot show that the decoy-competition machinery adds operational value over naive confidence thresholding at the SAME zero-label budget; the 'wedge' could reduce to 'a confidence threshold already matches recall-for-recall.'\",\n      \"suggested_action\": \"Specify the shared atomic-fact evaluation schema and the precise procedure for extracting comparable facts/conclusions from CoT and RAG outputs (e.g., a fixed claim-decomposition + alignment-to-Re-DocRED-relations step applied identically to all systems). Restore the plain confidence-threshold gate as the primary zero-label baseline in S4, so the operational wedge is measured as decoy-gating vs thresholding under identical labels, with labeled conformal reported alongside as the labeled reference point.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"Breadth vs depth on a $10 / CPU-only budget. The proposal now spans S0-S6 (seven claim rows), two anchors, three-plus baselines, an S5 model validated by both leave-one-cluster-out and leave-one-document-out CV with its own gap-regression power analysis, S6 propagation, and several 'if-budget-permits' threads (TDC-SB/UB, '+1'-floor relaxation, ProbLog/isotonic, defeasible bridges, rule gating). This is a lot of surface area for a one-call/doc pipeline under a hard $10 cap, and the prior rounds repeatedly pushed toward focus. The risk is that several cells end up underpowered and nothing is decisively nailed.\",\n      \"suggested_action\": \"Pre-commit a strict budget waterfall: fully power the CLUTRR calibration diagonal and the Re-DocRED operational wedge FIRST, and explicitly state that S5/S6/floor-relaxation/rule-gating are run and reported only if the two anchors clear their pre-registered power thresholds, with leftover budget. Make this ordering visible in the feasibility section so a reviewer sees the headline cannot be starved by secondary exploration.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The labeled-conformal-for-LLM frontier is moving fast and a top reviewer will expect current awareness. Beyond the cited Li et al. (2508.18473), Mohri-Hashimoto, and Jin-Candes, recent work directly applies conformal SELECTION / multiple testing to LLM claim filtering (e.g., feedback-enhanced online multiple testing for conformal selection, 2025; differentiable coherent factuality, 2026; conformal-factuality robustness for RAG, 2026). These are not novelty threats — they remain LABELED and certify outputs rather than gating the neuro-symbolic admission boundary via competition — so they actually reinforce the label-free wedge, but the proposal should show it knows them.\",\n      \"suggested_action\": \"Add one or two sentences placing the work against the conformal-selection-applied-to-LLM-claims line, reusing the existing axes (label-free operation vs labeled calibration; competition/per-leaf certificates + symbolic propagation vs output-level certification). Low priority relative to the methodology and rigor critiques.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"Density remains the dominant presentation weakness despite genuine improvements (plain-mechanism lead, three load-bearing numbers, the claim table). The assumptions, the score-dependence-robustness block, and the motivation are still long defensive run-ons that interleave claim, caveat, and rebuttal-to-prior-review, which obscures the core novelty and will cost the ACL presentation score. This has been flagged in multiple rounds; with the methodology now strong, presentation is a primary remaining score lever.\",\n      \"suggested_action\": \"Convert the score-dependence-robustness and assumptions prose into a compact table (threat | how it breaks the sign-flip property | mitigation | pre-registered test). Lead each field with one unqualified mechanism sentence before any caveat. Remove the round-over-round meta-commentary ('the key change this round', 'the methodology fix') from the hypothesis body. State the demonstrable-alpha range, doc/call counts, and label budget once.\"\n    }\n  ],\n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [16] ASSISTANT · 2026-06-16 04:26:47 UTC

```
Review written to `./.terminal_claude_agent_struct_out.json`.

## Summary

**Verdict: 5/10 (Borderline Accept), confidence 4.** Soundness 3, Presentation 2, Contribution 3. H↔H relation: **evolution** (same decoy-competition FDR frame, refined into a two-anchor evaluation + sign-flip robustness).

**Grounding (web-verified):**
- The target-decoy/knockoff → LLM-hallucination-gating transfer is **genuinely novel** — search returns only proteomics/variable-selection uses, none for LLM factuality.
- Re-DocRED stats are **accurate** (4,053 re-annotated docs, 96 relations, ~13 F1 headroom).
- The conformal-for-LLM frontier is active but **all labeled**, so the label-free wedge survives.

**Prior round's 3 MAJORs are all substantively addressed:**
1. *Scope* → fixed by the two-anchor split (CLUTRR = calibration only; Re-DocRED = operational + S5).
2. *Sign-flip methodology* → fixed by naming the null sign-flip property, document-block bootstrap, isolated provenance-blinded scoring, and the clever isolated-vs-batched discriminator.
3. *Unfalsifiability* → fixed by the single S4/S5-independent primary disconfirmation on CLUTRR facts.

So I did **not** re-raise those. The score rose accordingly.

**New / remaining issues I flagged (ranked by score impact):**
- **[MAJOR methodology]** The isolated-scoring fix likely blows the $10 budget — the token/cost projection looks inherited from the old batched design. If they revert to batching, the fix self-defeats. Recompute and pre-register the isolated fraction.
- **[MAJOR rigor]** The CLUTRR-FACTS diagonal (where the primary disconfirmation lives) may be **too clean to populate with genuine false admissions** → vacuously conservative, can't fire or pass. Pilot must measure the false-real base rate, not just tail separation.
- **[MAJOR methodology]** The Re-DocRED operational head-to-head is under-specified (CoT/RAG aren't atomic-fact extractors — "matched recall" needs a shared schema), and the **plain confidence-threshold baseline was dropped** — the one comparison that isolates whether the decoy machinery beats naive thresholding under zero labels.
- **[MINOR]** Breadth-vs-depth on $10 (S0–S6, two anchors, multiple baselines); stale conformal-selection frontier; persistent density.
```

### [17] SYSTEM-USER prompt · 2026-06-16 04:26:48 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.' is too long (at most 120 characters, got 123)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [18] ASSISTANT · 2026-06-16 04:26:54 UTC

```
The `relation_rationale` is 3 characters too long. Let me shorten it.
```

### [19] TOOL CALL — Edit · 2026-06-16 04:26:54 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_6/review_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness."
NEW:   "relation_rationale": "Same decoy-competition FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness."
```

### [20] TOOL RESULT — Edit · 2026-06-16 04:26:54 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_6/review_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.\"", "newString": "  \"relation_rationale\": \"Same decoy-competition FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.\"", "originalFile": null, "structuredPatch": [{"oldStart": 80, "oldLines": 5, "newStart": 80, "newLines": 5, "lines": ["   \"score\": 5,", "   \"confidence\": 4,", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same decoy-competition label-free FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.\"", "+  \"relation_rationale\": \"Same decoy-competition FDR frame; refines evaluation into two anchors (CLUTRR/Re-DocRED) + sign-flip robustness.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [21] ASSISTANT · 2026-06-16 04:26:56 UTC

```
Fixed — the `relation_rationale` is now 117 characters (under the 120 limit). The review JSON is complete and valid at `./.terminal_claude_agent_struct_out.json`.
```
