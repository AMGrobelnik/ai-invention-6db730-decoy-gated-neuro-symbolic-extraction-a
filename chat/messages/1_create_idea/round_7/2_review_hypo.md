# review_hypo — create_idea

> Phase: `hypo_loop` · round 7 · `review_hypo`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 04:33:35 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 04:33:41 UTC

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
  A Label-Free FDR Knob at the Text-to-Logic Admission Boundary via Plausibility-Matched Decoy Competition: Calibration Validated
  on CLUTRR, Operational Hallucination-Reduction on Re-DocRED, Robustified Against Score-Dependence
hypothesis: |-
  MECHANISM (one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  THE GATE. For each candidate i, form the competition statistic W_i = score(real_i) - score(decoy_i). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. Validity rests on the null sign-flip property; we test it in the tail (not as a marginal average) and protect it against two LLM-specific dependence channels (threat table below).

  TWO ANCHORS (clean division of labor). (A) CLUTRR (free, deterministic, CRISP gold) hosts the CALIBRATION-VALIDITY claim and the single primary disconfirmation: does realized FDR track target alpha (the diagonal)? (B) Re-DocRED (human-annotated, open-vocabulary, 96 relation types, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS claim (atomic-fact precision/recall and hallucinated-conclusion rate vs baselines at matched recall), the genuine schema-alignment bridge test, and the document-level predictive model S5. CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful; the two are never conflated.

  THREE NUMBERS (stated once). (1) Demonstrable-alpha range: alpha in [0.05, 0.5]; the knockoff+ '+1' offset gives a minimum estimable FDR ~1/k at k admissions. (2) Confirmatory corpus: 120 CLUTRR docs + 120 Re-DocRED docs (>=4 clusters) + ~15 illustrative legal/news/story docs (non-confirmatory trace demo). (3) Labels: ZERO labels for operation; gold used only for validation, charged symmetrically against any labeled baseline's calibration labels.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent; populability-gated). Pre-registered on the CLUTRR candidate family Phase-0 shows is POPULABLE -- yielding >= N_false_min (pre-registered, default 40) genuine false admissions pooled at alpha*. Default family: MULTI-HOP inferred kinship relations, where extraction errors are dense; atomic facts over the closed kinship vocabulary are typically too clean to populate the diagonal. Under isolated provenance-blinded scoring at alpha*, the central control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. If NO CLUTRR family reaches N_false_min even after false-real enrichment (extractor over-generation + harder long-chain splits), the diagonal is declared UNTESTABLE at this difficulty and reported as a precondition outcome -- never as 'confirmed by conservatism'.

  CLAIM CHAIN (each row independently testable; a break is localized and reported).
  | # | CLAIM | TEST | PASS CRITERION |
  |---|-------|------|----------------|
  | S0 | Score separation (precondition) | Pilot: selected elicitation separates entailed vs non-entailed in the UPPER TAIL; isolated~batched agree on a labeled slice | tail-AUC>0.5 with CI; isolated~batched |
  | S1 | Decoy signature (mechanism) | Tail-conditioned win-rate among above-cutoff matched pairs + upper-tail two-sample CDF test | counterfactual decoys ~0.5; random swaps anti-conservative |
  | S2 | Calibration validity (CLUTRR) | Sweep alpha; realized FDR vs crisp gold; document-block-bootstrap CI on the diagonal, on the populable family | diagonal tracked within tau above the 1/k floor |
  | S3 | Entrapment corroboration | Independent tail-matched entrapment; combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E); entrapment passes its own tail-difficulty diagnostic | bound agrees with decoy-FDR and gold |
  | S4 | Operational wedge (Re-DocRED) | Matched-recall PR + hallucinated-conclusion rate vs PLAIN CONFIDENCE-THRESHOLD gate (primary zero-label comparator), CoT, RAG, and labeled Mohri-Hashimoto conformal | decoy-gating beats plain thresholding at equal zero labels; competitive with labeled conformal |
  | S5 | Document-level predictive account (Re-DocRED) | Predict per-document tail-exchangeability gap from doc/score features; leave-one-cluster-out + leave-one-document-out CV; pre-registered GAP-regression power analysis | out-of-sample predictive IFF >= N_min held-out units; else DESCRIPTIVE |
  | S6 | Predictable propagation (preliminary) | Tightening alpha lowers multi-hop hallucinated-conclusion rate | direction + rough magnitude |

  SCORE-DEPENDENCE ROBUSTNESS (threat table).
  | THREAT | HOW IT BREAKS THE NULL SIGN-FLIP PROPERTY | MITIGATION | PRE-REGISTERED TEST |
  |--------|-------------------------------------------|------------|---------------------|
  | Within-document score-noise correlation | pooled null signs become dependent; variance/floor understated (anti-conservative) | treat DOCUMENT as a block; document-block bootstrap for all FDP CIs; never i.i.d.-pool signs | block-bootstrap CI is the CI used by the primary disconfirmation |
  | Batched-scoring contrast effects | model implicitly detects the fabricated item and depresses decoy scores (FDP optimistic) | ISOLATED, provenance-blinded, order-randomized scoring as default | isolated-vs-batched check = discriminator: isolation restores diagonal => artifact; persists => genuine non-exchangeability |
  | Upper-tail overconfidence | verbalized confidence fails to separate entailed vs non-entailed exactly where admissions occur | Phase-0 selects elicitation by tail-AUC (verbalized / logprob / self-consistency / DINCO-style) | tail-AUC>0.5 with CI; budget gated on pilot |
  | Decoy too easy / contamination | non-tail-matched decoys make FDR optimistic; an actually-entailed decoy biases FDR conservative (safe side) | document-conditioned counterfactual decoys; non-entailment check; report contamination | tail-conditioned win-rate ~0.5; contamination sensitivity analysis |

  BUDGET ARITHMETIC (isolated default, shown explicitly). Confirmatory scoring items = 240 docs x ~20 candidates x 3 item-types (real + decoy + entrapment at r=1) ~= 14.4K isolated scoring calls; + ~0.7K extraction/decoy/entrapment-generation calls; + Phase-0 pilot. At ~450 input + ~30 output tokens/call this is ~7-15M tokens (candidate-count-dependent). At a sub-$0.30/M model this is ~$2-6 RAW; DOCUMENT-PREFIX PROMPT CACHING -- the ~60 item-scoring calls sharing one document context re-use a cached prefix (cache read ~0.1x) -- cuts input ~3-5x, projecting ~$1-3. Cumulative cost logged after every call; HARD STOP at $10. Isolated scoring is the DEFAULT for 100% of the confirmatory set (caching, not batching, buys the headroom); batching is used only in the labeled isolated-vs-batched sensitivity slice.

  BUDGET WATERFALL (ordering visible). Spend in strict priority order: (i) Phase-0 pilot (gates everything); (ii) fully power the CLUTRR calibration diagonal; (iii) fully power the Re-DocRED operational wedge; (iv) ONLY with leftover budget and ONLY if (ii) and (iii) clear their pre-registered power thresholds: S5 predictive model, S6 propagation, TDC-SB/UB and '+1'-floor relaxation, exploratory rule gating. The headline cannot be starved by secondary exploration.

  SHARED OPERATIONAL CONSTRUCT (Re-DocRED, the fair-mapping fix). All systems target the SAME object: (head-entity, Re-DocRED-relation, tail-entity) triples over the document's annotated entities, scored against human gold triples. A single fixed claim-decomposition + relation-alignment step maps EVERY system's raw output into this triple space identically -- neuro-symbolic admitted facts/bridges, the plain confidence-threshold gate, CoT free-text answers, RAG answers, and labeled-conformal filtered claims. Matched recall is enforced by sweeping each system's own score to a common recall operating point; precision and hallucinated-conclusion rate are compared there with document-block-bootstrap CIs. The wedge is isolated as decoy-gating vs PLAIN THRESHOLDING under identical zero labels; labeled conformal is the labeled reference point.

  SCOPE. Facts AND bridges carry the headline. CLUTRR bridges are crisp (deterministic kinship) and host the diagonal; Re-DocRED bridges are open-vocabulary relation-to-schema alignments and host the operational and predictive claims. Defeasible bridges, implicit common-sense rule gating, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S6 are preliminary / if-budget-permits.
motivation: |-
  Text-to-logic pipelines stall at one crux: when strict symbolic unification fails, an LLM must fuzzy-match predicates and supply background knowledge, and that interface is exactly where hallucination re-enters and silently corrupts every downstream deduction. The dangerous hallucinations are not random nonsense but PLAUSIBLE, high-confidence false facts. Practitioners have no quantitative, label-free knob there: self-consistency and LLM-as-judge are heuristic; ontology-constraint filtering needs rich trusted constraints and catches only encoded violations; and the strongest uncertainty-quantification methods (conformal factuality, conformal selection + BH, multiple-testing hallucination detection, coherent factuality, and the newest online and differentiable variants) all need a LABELED calibration set and certify the final answer or claim set, not the neural-to-symbolic admission boundary.

  Genomics and proteomics solved an isomorphic label-poor problem -- selecting true signals among overwhelming noise with a guaranteed FDR and no ground truth -- via the knockoff filter and target-decoy competition, and learned the two ways the trick breaks: decoys 'too unrealistic to fool' the scorer make FDR optimistic (cured by property-matched decoys), and entrapment FDP must be estimated with a valid upper bound built INDEPENDENTLY of the decoys. We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary, turning 'reduce hallucination' from a best-effort aspiration into a self-corroborated, label-free, auditable quantity with per-leaf certificates.

  The two-anchor design makes the value claim honest. A label-free FDR knob is worth building only if it is BOTH calibrated AND useful where plausible hallucinations actually bite. CLUTRR's closed kinship vocabulary is the right place to prove CALIBRATION (free crisp gold, exact realized FDR) but the wrong place to prove USEFULNESS (the relation set is tiny and well-known). Re-DocRED -- realistic Wikipedia prose, 96 open relation types, document-level multi-hop, human gold with evidence spans -- is the right place to prove operational usefulness, with a fixed shared extraction schema so the neuro-symbolic pipeline, a plain zero-label confidence threshold, CoT, RAG, and labeled conformal are all measured on the same triples at matched recall. The plain confidence threshold is the load-bearing comparator: it shows whether the decoy-competition machinery adds value over naive thresholding at the SAME zero-label budget, so the wedge cannot collapse to 'a threshold was enough.'

  Why it matters even at coarse alpha: NO existing label-free method offers ANY FDR knob at the fuzzy-unification interface. A first, auditable, zero-operation-label control -- even at alpha ~0.1 -- converts an uncontrolled hallucination channel into a tunable one. Because LLM decoys carry no theoretical guarantee, the most probable outcome is partial control; the Re-DocRED document-level predictive account (S5) converts a likely-partial result into a generalizable mechanism-level insight about WHEN the calibration holds.
assumptions:
- >-
  NULL SIGN-FLIP PROPERTY IS ENGINEERED AND TESTED, NOT GUARANTEED. knockoff+/TDC validity requires that, among genuinely-false
  candidates, sign(W_i) for W_i = score(real_i) - score(decoy_i) behaves like an independent fair coin conditional on |W_i|,
  with each false real and its matched decoy equally likely to receive any score in the high-score region near the cutoff.
  LLM counterfactual decoys carry no construction-level proof of this, so the claim is an empirically-validated calibration
  (not a theorem), tested IN THE TAIL via tail-conditioned win-rate ~0.5 plus an upper-tail two-sample CDF test.
- >-
  SCORE-DEPENDENCE IS HANDLED, NOT ASSUMED AWAY. Within-document correlation of LLM scoring noise is respected by treating
  the DOCUMENT as a block (document-block bootstrap for all FDP CIs; never i.i.d.-pooled signs). Batched-scoring contrast
  effects are removed by ISOLATED, provenance-blinded, order-randomized scoring as the default, with a pre-registered isolated-vs-batched
  check that doubles as the DISCRIMINATOR between a scoring artifact (isolation restores the diagonal) and genuine decoy non-exchangeability
  (anti-conservatism persists under isolation).
- >-
  THE SCORE-SEPARATION PRECONDITION IS PILOT-GATED. The LLM must emit a roughly monotone score separating document-entailed
  from non-entailed content better than chance SPECIFICALLY in the upper tail; verbalized confidence is documented to be overconfident
  there, so it is not assumed. A Phase-0 pilot selects the best elicitation (verbalized, logprob-derived, self-consistency,
  DINCO-style distractor-normalized), verifies tail separation, and confirms isolated~batched agreement on a labeled slice.
  The headline budget is released only on pilot success; otherwise the precondition-failure analysis is the reported result.
- >-
  THE CALIBRATION DIAGONAL NEEDS GENUINE FALSE ADMISSIONS, AND POPULABILITY IS MEASURED BEFORE IT IS ASSERTED. A realized-FDR-vs-alpha
  diagonal can only TRACK alpha if a meaningful fraction of admitted reals are genuinely false; on CLUTRR's easy closed vocabulary
  atomic facts may be too clean. Phase-0 measures, at the operative alpha*, the genuine false-admission count among CLUTRR
  proposals separately for atomic facts and multi-hop inferred kinship; the primary disconfirmation is pre-registered on whichever
  family reaches N_false_min (default 40 pooled; default expectation: multi-hop). The false-real pool is enriched by extractor
  over-generation and harder long-chain CLUTRR splits. Below N_false_min on all families, the diagonal is declared UNTESTABLE
  (not 'conservative, therefore confirmed'). CLUTRR gold is exact so the diagonal is asserted there; Re-DocRED gold has residual
  false negatives so only RELATIVE operational comparisons under shared gold are asserted there.
- >-
  S5 IS POWERED WHERE FEATURE VARIANCE EXISTS, WITH A PRE-REGISTERED PREDICTIVE-VS-DESCRIPTIVE THRESHOLD. The per-document
  tail-exchangeability gap can only be predicted if its input features vary; CLUTRR documents are near-homogeneous in entity
  density, specificity, and genre, so S5 is based on Re-DocRED (>=4 entity-type/topic clusters supply real cross-document
  variance). The S5 unit is the document nested in clusters, validated by leave-one-cluster-out and leave-one-document-out
  CV with a pre-registered GAP-regression power analysis; below a pre-registered minimum N_min of held-out units with sufficient
  admissions, S5 is reported DESCRIPTIVE, not predictive.
investigation_approach: |-
  Build the pipeline end to end, run a gating pilot first, then execute a strict BUDGET WATERFALL: Phase-0 pilot -> CLUTRR calibration diagonal -> Re-DocRED operational wedge -> (leftover only, gated on the two anchors clearing power thresholds) S5 / S6 / floor-relaxation / rule-gating. CPU-only; cumulative LLM cost logged after every call; HARD STOP at $10.

  FEASIBILITY (published before committing; see the budget arithmetic in the hypothesis). Isolated, provenance-blinded scoring is the default for 100% of the ~14.4K confirmatory scoring items; the ~7-15M projected tokens are kept to ~$1-3 by document-prefix prompt caching (the ~60 scoring calls per document re-use one cached document context at ~0.1x read cost). A sub-$0.30/M model is used; batching appears only in the labeled isolated-vs-batched sensitivity slice.

  PHASE 0 -- PILOT (precondition + powerability). On a few dozen labeled items per anchor: (i) select the elicitation that best separates entailed vs non-entailed IN THE UPPER TAIL; (ii) confirm isolated~batched agreement on a labeled slice (gate batching); (iii) MEASURE the genuine false-admission count among CLUTRR atomic-fact and multi-hop-bridge proposals at alpha* and choose the populable family for the primary disconfirmation (enrich via over-generation + long-chain splits if sparse); (iv) MEASURE on CLUTRR the cross-document variance of the S5 features (demonstrating CLUTRR's unsuitability for S5); (v) run a tail power analysis AND a GAP-regression power analysis for S5 on Re-DocRED. Size both corpora to target; gate the full run.

  PIPELINE. (1) EXTRACTION: a cheap OpenRouter LLM proposes typed first-order facts; argument types grounded in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology, standing in for OpenCyc) used ONLY for typing; the extractor OVER-GENERATES on CLUTRR to densify false positives. (2) DECOY GENERATION: PRIMARY family = document-conditioned counterfactual decoys (maximally-plausible, non-entailed facts/bridges); random type-matched swaps retained as the predicted-anti-conservative baseline; every decoy passes a non-entailment check with reported contamination. (3) ENTRAPMENT: independent, tail-matched, false-by-construction (in-genre cross-document swaps, numeric/temporal perturbation, explicit contradiction), mixed at reported ratio r, with its own tail-difficulty diagnostic. (4) SCORING: isolated, provenance-blinded, order-randomized, pilot-selected elicitation; rank-normalized per document. (5) FDR GATE: knockoff+ thresholding picks the most permissive cutoff with estimated corpus-aggregate FDR <= alpha, separately for facts and bridges and per anchor; admitted items enter the KB with a logged certificate. (6) VARIANCE/CIs: document-block bootstrap throughout. (7) ENTRAPMENT VALIDATION: combined estimator upper-bounds realized false-admission; compare against decoy-FDR and gold. (8) TAIL DIAGNOSTICS (measurement only): above-cutoff distribution vs gold false-reals + win-rate + upper-tail two-sample test. (9) REASONING: admitted facts/bridges populate SWI-Prolog for multi-hop deduction; backward-chaining proofs export as trace-graphs whose leaves carry provenance plus the decoy + entrapment certificate.

  SHARED OPERATIONAL EVALUATION (Re-DocRED). A single fixed claim-decomposition + relation-alignment step maps every system's output to (head, Re-DocRED-relation, tail) triples identically -- neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal. Recall is matched by sweeping each system's own score to a common operating point; precision and hallucinated-conclusion rate are compared there with document-block-bootstrap CIs.

  EXPERIMENTS. (a) CLUTRR validity-of-control: sweep alpha; realized FDR via gold + entrapment bound on the populable family; diagonal tracking with block-bootstrap CIs; normalization and isolated-vs-batched sensitivity. (b) Decoy-family showdown + entrapment tail-difficulty. (c) Re-DocRED operational: matched-recall PR + hallucinated-conclusion rate vs PLAIN THRESHOLD (primary zero-label comparator), CoT, RAG, and labeled conformal, with guarantee status side by side. (d) [leftover only] S5 LOO-CV on Re-DocRED with the predictive-vs-descriptive threshold; S6 propagation; floor-relaxation; rule gating. (e) Cost check (<$10, CPU-only) + auditable trace-graphs.
success_criteria: |-
  PRECONDITION (gate). Phase-0 must show the selected score separates entailed from non-entailed content better than chance in the upper tail, isolated~batched agree, a CLUTRR family reaches N_false_min genuine false admissions, and the S5 power/variance measurements support a gap regression on Re-DocRED. If the pilot fails any gate, the reported contribution is the precondition-failure analysis.

  PRIMARY DISCONFIRMATION (single, S4/S5-independent). On the populable CLUTRR family (default: multi-hop inferred kinship) under isolated provenance-blinded scoring at alpha*: the central label-free control claim is DISCONFIRMED if realized corpus-aggregate FDR (vs crisp gold) exceeds alpha* by more than tolerance tau AND the document-block-bootstrap CI lies entirely on the anti-conservative side. If no family reaches N_false_min even after enrichment, the diagonal is reported UNTESTABLE (a precondition outcome), never as confirmed-by-conservatism.

  CONFIRMED requires ALL of: (1) CALIBRATION VALIDITY (CLUTRR) -- realized FDR tracks target alpha within tau above the 1/k floor across the demonstrable grid on the populable family, stable under the normalization and isolated-vs-batched checks; (2) DECOY SIGNATURE -- counterfactual decoys reach tail-conditioned win-rate ~0.5 and pass the upper-tail two-sample test while random swaps are measurably anti-conservative, and entrapment passes its tail-difficulty diagnostic with the combined-estimator bound agreeing with gold; (3) OPERATIONAL WEDGE (Re-DocRED) -- at matched recall (PR curves with block-bootstrap CIs), decoy-gating BEATS the plain confidence-threshold gate on atomic-fact precision and hallucinated-conclusion rate under identical zero labels, and stays competitive with the labeled Mohri-Hashimoto conformal reference. A BH multiplicity correction is applied across all validation tests.

  SECONDARY (reported only after the two anchors clear power thresholds; never escape hatches). (4) S5 document-level model: PREDICTIVE if validated out-of-sample across >= N_min held-out Re-DocRED units, else DESCRIPTIVE; either way it characterizes WHICH features govern tail-exchangeability. (5) Entrapment self-corroboration agrees with gold (co-failures reported). (6) S6 -- tightening alpha reduces multi-hop hallucination in the predicted direction. (7) Ablating the decoy gate measurably worsens hallucination. (8) The pipeline runs on commodity CPU within $10 with auditable trace-graphs carrying per-leaf certificates.

  DISCONFIRMED if: the primary disconfirmation fires (populable CLUTRR family anti-conservative beyond tau under isolated scoring); OR, separately for the operational claim, decoy-gating shows no precision/hallucination advantage over the PLAIN CONFIDENCE-THRESHOLD gate at matched recall on Re-DocRED (the wedge collapses to 'thresholding is enough'). An uninterpretable null -- control neither clearly holds nor clearly fails because the tail, the diagonal, or the gap test is underpowered -- is the true failure the Phase-0 power analysis (now including the false-admission base-rate measurement) is designed to prevent.
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
  a synthetic negative control exchangeable BY CONSTRUCTION, relying on the null sign-flip property (signs of null statistics
  are i.i.d. coin flips conditional on magnitude). Difference: this machinery lives in numeric feature selection and mass
  spectrometry where exchangeability is provable; we adapt knockoff+ thresholding to the LLM neuro-symbolic boundary where
  decoys carry NO such guarantee, so we test the sign-flip condition empirically in the tail, use a document-block bootstrap
  for within-document sign dependence, and model where it holds.
- >-
  Property-matched decoy generation in cheminformatics/proteomics (DeepCoy, Bioinformatics 2021; protein-language-model decoys):
  generate decoys that reproduce the score properties of true positives so target-decoy FDR is well-calibrated. Difference:
  lives in molecular screening; we import the PRINCIPLE -- decoys must reproduce the false-positive score distribution, not
  be 'too easy' -- to design LLM fact/bridge decoys as document-conditioned counterfactuals.
- >-
  Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction' (EMNLP 2022; Re-DocRED).
  DocRED comprises 5,053 Wikipedia documents (distant-supervised from Wikidata), averaging 196.7 words and 19.5 entities,
  with 97 predefined relation types (96 real + no_relation) and human evidence sentences; Re-DocRED re-annotates 4,053 by
  adding missed triples (~13 F1 of headroom) and is public. We USE Re-DocRED as the open-vocabulary operational anchor (a
  fixed shared (head, relation, tail) extraction schema for ALL systems), asserting only RELATIVE operational comparisons
  (shared residual false negatives affect all methods equally), not the absolute FDR diagonal, which we assert on crisp-gold
  CLUTRR. Re-DocRED documents are SHORT (~200 words), which is strictly easier for commodity hardware; we treat document length
  itself as an S5 feature.
- >-
  Li, Magesh & Veeravalli, 'Principled Detection of Hallucinations in Large Language Models via Multiple Testing' (arXiv 2508.18473,
  2025): reconceptualizes hallucination detection as hypothesis testing, aggregates gray-box scores via conformal p-values,
  and applies general (dependence-tolerant) Benjamini-Hochberg/Yekutieli to control the false-alarm rate; it 'adds a lightweight
  calibration step that uses a small calibration set of non-hallucinated prompts to provide theoretical control', operating
  at the PROMPT/generation level. Difference: it is LABELED and certifies the generation; we are label-free for operation
  and gate the neuro-symbolic ADMISSION boundary via target-decoy competition with independent entrapment corroboration and
  per-leaf certificates. Its confirmed labeled-calibration requirement strengthens our label-free wedge.
- >-
  Lu, Huo, Ren, Wang & Zou, 'Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection' (arXiv 2509.03297,
  2025): GAIF, a feedback-enhanced generalized alpha-investing framework that dynamically adjusts thresholds using revealed
  outcomes for finite-sample (m)FDR control, extended to online conformal selection via independent conformal p-values and
  feedback-driven model selection. Difference: it REQUIRES revealed labeled outcomes (feedback) and selects/certifies candidate
  outputs online; we control FDR with ZERO operation labels via decoy competition at the text-to-logic admission boundary,
  with symbolic propagation. The conformal-selection line reinforces -- not threatens -- the label-free wedge.
- >-
  Hittesdorf, Salzetta & Cheng, 'Differentiable Conformal Training for LLM Reasoning Factuality' (Differentiable Coherent
  Factuality / DCF, arXiv 2604.20098, 2026), building on 'Conformal Language Model Reasoning with Coherent Factuality' (arXiv
  2505.17126, ICLR 2025): represent reasoning outputs as dependency graphs and jointly validate claims with their logical
  ancestors; DCF makes the scorer differentiable to learn better scorers while recovering conformal guarantees. Difference:
  both require LABELED held-out calibration and certify OUTPUT claim graphs; we gate the neuro-symbolic ADMISSION boundary
  label-free via decoy competition, and our trace-graph is a Prolog proof with per-leaf decoy+entrapment certificates, not
  a conformally-validated claim DAG.
- >-
  Mohri & Hashimoto, 'Language Models with Conformal Factuality Guarantees' (ICML 2024): a back-off algorithm removing claims
  until a factuality alpha is met via conformal prediction with labeled samples. Our load-bearing LABELED reference baseline
  in S4. Difference: it requires labeled calibration, certifies the final filtered OUTPUT rather than the admission boundary,
  and offers no synthetic-decoy mechanism, independent entrapment, or symbolic propagation. We report its finite-sample guarantee
  vs our empirical calibration side by side; our wedge is label-free OPERATION measured against a plain zero-label threshold.
- >-
  Jin & Candes, 'Selection by Prediction with Conformal p-values' (JMLR 2023): conformal p-values + Benjamini-Hochberg to
  select candidates with FDR control under exchangeability of labeled calibration and test data. Difference: needs labeled
  calibration outcomes; we estimate and control FDR with no operation labels by competing each proposal against engineered
  decoys and corroborate via independent tail-matched entrapment.
- >-
  Ebadi, Crook, Keich et al., 'Bounding the FDP in competition-based control of the FDR' (arXiv 2302.11837, 2023; TDC-SB/UB)
  and He, Ebadi, Keich et al., 'Controlling the FDR via competition: is the +1 needed?' (arXiv 2204.13248, 2023): tighter
  FDP bounds and analysis of the '+1' correction that sets the minimum-estimable-FDR floor. We test (leftover budget only)
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
- >-
  FactSelfCheck (Sawczyn et al., Findings of EACL 2026 / arXiv 2503.17229) and DINCO (Wang et al., arXiv 2509.25532, 2025):
  zero-resource black-box methods producing per-fact hallucination scores from sampling consistency / distractor-normalized
  verbalized confidence. Difference: both yield a per-claim detection SCORE with no admission threshold, exchangeability,
  or competition argument; FactSelfCheck-style and DINCO-style signals are CANDIDATE elicitations in our Phase-0 pilot, while
  our novelty is the label-free FDR gate built on whichever elicitation wins.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer. Genomics/proteomics solved the hardest label-poor problem -- deciding
  which of thousands of candidate signals are real with no ground truth -- with a guaranteed FDR via the knockoff filter (statistics)
  and target-decoy competition (mass spectrometry), and discovered the two ways the trick breaks: decoys 'too unrealistic
  to fool' the scorer make FDR optimistic (cured by property-matched decoys: DeepCoy, protein-LM decoys), and entrapment FDP
  must be estimated with a valid upper bound (Wen et al., Nature Methods 2025) using entrapment built unlike the decoys. We
  map all three onto the fuzzy-unification boundary of a text-to-logic pipeline, where the LLM aligns predicates and supplies
  background knowledge. Because the dangerous hallucinations are PLAUSIBLE high-confidence false facts, the decoys must be
  plausible counterfactuals from the LLM's own prior, exchangeability must be checked IN THE TAIL, and the FDR must be corroborated
  by independently-constructed tail-matched entrapment and arbitrated by a small gold probe. Three further moves come from
  taking the statistical machinery seriously on its own terms: (a) the knockoff null SIGN-FLIP property is named explicitly,
  and the two ways LLM scoring can break it -- within-document score correlation and batched-scoring contrast effects -- are
  handled by a document-block bootstrap and isolated provenance-blinded scoring, with the isolated-vs-batched check doubling
  as the discriminator between a scoring artifact and genuine non-exchangeability; (b) evaluation is split into a CALIBRATION
  anchor (CLUTRR, crisp free gold, exact diagonal -- with the disconfirmation pre-registered on the candidate family dense
  enough in genuine errors to be non-vacuous) and an OPERATIONAL anchor (Re-DocRED, open-vocabulary human gold, a fixed shared
  extraction schema for all systems, with a plain zero-label confidence threshold as the primary comparator so the wedge isolates
  the decoy machinery's value); (c) the document-level predictive account is based on Re-DocRED where the predicted features
  actually vary, with a pre-registered predictive-vs-descriptive threshold.
terms:
- term: Plausibility-matched (counterfactual) decoy
  definition: >-
    A synthetic candidate (fact or fuzzy-unification bridge) generated from the LLM's own prior over document-plausible-but-non-entailed
    content -- a document-conditioned counterfactual -- so its score distribution reproduces that of genuine plausible hallucinations.
    It replaces random type-matched swaps, which are 'too easy' and make the estimated FDR optimistic.
- term: Null sign-flip property (the validity condition)
  definition: >-
    The condition knockoff+/TDC FDR control rests on: among genuinely-false candidates, the sign of W_i = score(real_i) -
    score(decoy_i) behaves like an independent fair coin conditional on |W_i|. Two LLM-scoring channels can break it anti-conservatively
    -- within-document score correlation and batched-scoring contrast effects -- so the method tests and protects against
    both.
- term: Two-anchor evaluation (calibration vs operational)
  definition: >-
    CLUTRR (free, deterministic, crisp gold) hosts the CALIBRATION-VALIDITY claim (the realized-FDR-vs-alpha diagonal) and
    the single primary disconfirmation; Re-DocRED (human-annotated, open-vocabulary, document-level multi-hop) hosts the OPERATIONAL-USEFULNESS
    claim, the genuine schema-alignment bridge test, and the S5 predictive model. CLUTRR proves the knob is calibrated; Re-DocRED
    proves it is useful; the two are never conflated.
- term: Populability gate and false-real enrichment
  definition: >-
    A realized-FDR diagonal can only TRACK alpha if enough admitted reals are genuinely false. Phase-0 measures, at alpha*,
    the genuine false-admission count among CLUTRR atomic-fact and multi-hop-bridge proposals; the primary disconfirmation
    is pre-registered on whichever family reaches N_false_min (default 40 pooled). The false-real pool is enriched by extractor
    over-generation and harder long-chain splits. Below N_false_min on all families, the diagonal is declared UNTESTABLE,
    not confirmed-by-conservatism.
- term: Plain confidence-threshold baseline (the operational comparator)
  definition: >-
    A zero-label gate that admits candidates whose raw elicited confidence exceeds a swept threshold, with no decoy, no competition,
    no entrapment. It is the PRIMARY zero-label comparator in S4: if decoy-gating does not beat it at matched recall on precision
    and hallucinated-conclusion rate under identical labels, the operational wedge is disconfirmed (it reduces to 'thresholding
    is enough').
- term: Shared operational construct (Re-DocRED)
  definition: >-
    All systems target the SAME (head-entity, Re-DocRED-relation, tail-entity) triples over annotated entities, scored against
    human gold. A single fixed claim-decomposition + relation-alignment step maps every system's raw output -- neuro-symbolic,
    plain threshold, CoT, RAG, labeled conformal -- into this triple space identically, and recall is matched by sweeping
    each system's own score to a common operating point, so the comparison is apples-to-apples.
- term: Isolated provenance-blinded scoring
  definition: >-
    Each candidate (real, decoy, or entrapment) is scored in its OWN prompt with source/identity masked and presentation order
    randomized, instead of scoring many candidates jointly. This removes within-batch contrast/ranking effects that would
    let the model implicitly detect fabricated items and depress decoy scores. It is the default for 100% of the confirmatory
    set; document-prefix prompt caching keeps it affordable. The pre-registered isolated-vs-batched check discriminates a
    scoring artifact (isolation restores the diagonal) from genuine non-exchangeability (anti-conservatism persists).
- term: Document-prefix prompt caching
  definition: >-
    Because all ~60 isolated scoring calls for one document re-send the same document context, that prefix is cached once
    and re-read at ~0.1x cost per call. This is the mechanism that makes default isolated scoring fit the $10 budget (~$1-3
    projected) without reverting to batching, preserving the isolated-vs-batched discriminator.
- term: Document-block bootstrap
  definition: >-
    All FDP/FDR confidence intervals are computed by resampling whole DOCUMENTS (blocks), not individual candidates, so within-document
    correlation of LLM scoring noise is respected. This replaces the i.i.d.-pooled-sign variance the knockoff '+1' floor argument
    would otherwise assume, and yields the CI used in the primary disconfirmation.
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
    naive 'sample' ratio; r is propagated into variance and the achievable-alpha floor. Entrapment is built by a mechanism
    distinct from the decoys and gets its own tail-difficulty diagnostic.
- term: Single primary disconfirmation
  definition: >-
    One pre-registered, S4/S5-independent result that can falsify the headline: on the populable CLUTRR family under isolated
    provenance-blinded scoring at alpha*, if realized corpus-aggregate FDR exceeds alpha* by more than tolerance tau AND the
    document-block-bootstrap CI lies entirely on the anti-conservative side, the central label-free control claim is disconfirmed
    -- regardless of entrapment agreement or S5 outcome.
- term: Trace-graph
  definition: >-
    A human-auditable graph of the backward-chaining proof: nodes are sub-goals/derived facts, edges are rule applications,
    and each leaf carries its provenance (document span, ontology axiom, or admitted bridge) plus the decoy-competition and
    entrapment certificate that licensed it.
summary: >-
  Every LLM-proposed fact and fuzzy-unification bridge must out-score a plausibility-matched counterfactual decoy in a target-decoy
  / knockoff+ competition before entering a Prolog knowledge base, giving a label-free FDR knob at the neuro-symbolic admission
  boundary; calibration validity is proven on crisp-gold CLUTRR (with the single disconfirmation pre-registered on the error-dense,
  populable candidate family), operational hallucination-reduction is proven on open-vocabulary Re-DocRED against a plain
  zero-label confidence threshold and neural baselines on a shared extraction schema at matched recall, the gate is robustified
  against the two ways LLM scoring breaks the null sign-flip property (document-block bootstrap and isolated provenance-blinded
  scoring kept affordable by document-prefix caching), and a strict budget waterfall powers the two anchors before any secondary
  analysis.
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
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) Budget-vs-fix tension. The central methodology fix this round — DEFAULT isolated, provenance-blinded, order-randomized scoring (each real, decoy, and entrapment item scored in its own prompt) — multiplies the scoring call count by candidate multiplicity and re-sends document context per call. With <=300 CLUTRR + <=250 Re-DocRED + ~20 illustrative docs at ~10-40 candidates each, plus a 1:1 decoy and entrapment at ratio r, the isolated regime implies on the order of tens of thousands of scoring calls, each carrying document context. The stated projection (~4-8M tokens, $2-5, hard stop $10) appears to be inherited from the prior BATCHED design (~3 calls/doc) and likely understates isolated-scoring cost by a large factor. If the budget forces reverting to batched scoring for the bulk, the very fix that makes the confirmatory run interpretable is undermined, and the isolated-vs-batched discriminator weakens because most data is batched.
  Action: Recompute the feasibility budget explicitly for the isolated default: items = sum over docs of (candidates x {real, decoy, r-weighted entrapment}); per-call tokens including document context; total tokens and dollars at the chosen sub-$0.30/M model. If it breaches $10, either shrink the confirmatory corpus to what isolated scoring can afford, exploit prompt/context caching to amortize the re-sent document, or pre-register the exact isolated fraction and demonstrate in the pilot that the batched bulk reproduces the isolated diagonal on a labeled slice before committing the headline.
- [MAJOR] (rigor) Populability of the CLUTRR-FACTS calibration diagonal, on which the single primary disconfirmation rests. CLUTRR atomic-fact extraction over a tiny closed kinship vocabulary is easy, so genuinely-false extracted facts may be rare. The realized-FDR-vs-alpha diagonal can only be demonstrated to TRACK alpha if, at permissive cutoffs, a meaningful fraction of admitted reals are genuinely false (e.g., realized FDR must be able to rise toward 0.3 at alpha=0.3). If the false-real base rate is low, realized FDR sits near zero across the whole grid — trivially <= alpha (conservative everywhere) but NOT tracking — and the primary disconfirmation can neither fire nor be cleanly passed, because there are too few false admissions to estimate FDR at all. This is precisely the uninterpretable-null outcome the Phase-0 power analysis is meant to prevent, but the pilot as described measures tail SEPARATION and per-document admitted COUNT, not the genuine false-positive base rate among admissions.
  Action: Add to Phase-0 an explicit measurement, on CLUTRR facts at the operative alpha*, of the realized genuinely-false-admission count and base rate among proposals. Pre-register a minimum false-admission count below which the CLUTRR-facts diagonal is declared untestable (conservative, not tracking) rather than confirmatory. If the count is too low, deliberately enrich the false-real pool (e.g., harder multi-hop inferred relations the extractor gets wrong) or move the primary disconfirmation to CLUTRR BRIDGES, where multi-hop kinship inference produces denser errors.
- [MAJOR] (methodology) Operational head-to-head construct validity, plus a dropped baseline. The S4 operational confirmatory claim compares atomic-fact precision/recall and 'hallucinated-conclusion rate' of the neuro-symbolic pipeline against CoT, RAG, and labeled Mohri-Hashimoto conformal 'at matched recall.' Two problems: (a) CoT and RAG are generation/QA systems, not atomic-fact extractors in a shared schema, so 'matched-recall PR curves' across them is under-specified — you need a defined common extraction target and an explicit, fair mapping from each baseline's free-text output to comparable atomic facts and conclusions, or the comparison is apples-to-oranges; (b) the plain per-document/per-corpus confidence-threshold baseline — present as S3 in the prior iteration and the single most diagnostic ZERO-LABEL comparator — has been dropped from the headline operational set. Without it, S4 cannot show that the decoy-competition machinery adds operational value over naive confidence thresholding at the SAME zero-label budget; the 'wedge' could reduce to 'a confidence threshold already matches recall-for-recall.'
  Action: Specify the shared atomic-fact evaluation schema and the precise procedure for extracting comparable facts/conclusions from CoT and RAG outputs (e.g., a fixed claim-decomposition + alignment-to-Re-DocRED-relations step applied identically to all systems). Restore the plain confidence-threshold gate as the primary zero-label baseline in S4, so the operational wedge is measured as decoy-gating vs thresholding under identical labels, with labeled conformal reported alongside as the labeled reference point.
- [MINOR] (scope) Breadth vs depth on a $10 / CPU-only budget. The proposal now spans S0-S6 (seven claim rows), two anchors, three-plus baselines, an S5 model validated by both leave-one-cluster-out and leave-one-document-out CV with its own gap-regression power analysis, S6 propagation, and several 'if-budget-permits' threads (TDC-SB/UB, '+1'-floor relaxation, ProbLog/isotonic, defeasible bridges, rule gating). This is a lot of surface area for a one-call/doc pipeline under a hard $10 cap, and the prior rounds repeatedly pushed toward focus. The risk is that several cells end up underpowered and nothing is decisively nailed.
  Action: Pre-commit a strict budget waterfall: fully power the CLUTRR calibration diagonal and the Re-DocRED operational wedge FIRST, and explicitly state that S5/S6/floor-relaxation/rule-gating are run and reported only if the two anchors clear their pre-registered power thresholds, with leftover budget. Make this ordering visible in the feasibility section so a reviewer sees the headline cannot be starved by secondary exploration.
- [MINOR] (evidence) The labeled-conformal-for-LLM frontier is moving fast and a top reviewer will expect current awareness. Beyond the cited Li et al. (2508.18473), Mohri-Hashimoto, and Jin-Candes, recent work directly applies conformal SELECTION / multiple testing to LLM claim filtering (e.g., feedback-enhanced online multiple testing for conformal selection, 2025; differentiable coherent factuality, 2026; conformal-factuality robustness for RAG, 2026). These are not novelty threats — they remain LABELED and certify outputs rather than gating the neuro-symbolic admission boundary via competition — so they actually reinforce the label-free wedge, but the proposal should show it knows them.
  Action: Add one or two sentences placing the work against the conformal-selection-applied-to-LLM-claims line, reusing the existing axes (label-free operation vs labeled calibration; competition/per-leaf certificates + symbolic propagation vs output-level certification). Low priority relative to the methodology and rigor critiques.
- [MINOR] (clarity) Density remains the dominant presentation weakness despite genuine improvements (plain-mechanism lead, three load-bearing numbers, the claim table). The assumptions, the score-dependence-robustness block, and the motivation are still long defensive run-ons that interleave claim, caveat, and rebuttal-to-prior-review, which obscures the core novelty and will cost the ACL presentation score. This has been flagged in multiple rounds; with the methodology now strong, presentation is a primary remaining score lever.
  Action: Convert the score-dependence-robustness and assumptions prose into a compact table (threat | how it breaks the sign-flip property | mitigation | pre-registered test). Lead each field with one unqualified mechanism sentence before any caveat. Remove the round-over-round meta-commentary ('the key change this round', 'the methodology fix') from the hypothesis body. State the demonstrable-alpha range, doc/call counts, and label budget once.
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

### [3] HUMAN-USER prompt · 2026-06-16 04:33:41 UTC

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

### [4] ASSISTANT · 2026-06-16 04:36:20 UTC

```
I'll review this hypothesis carefully. Let me start by checking the user uploads folder and grounding my review with targeted searches on the novelty of the core idea.
```

### [5] TOOL CALL — Bash · 2026-06-16 04:36:20 UTC

```
List user uploads and memory directory:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && echo "---MEMORY---" && ls -la /root/.claude/projects/-ai-inventor/memory/ 2>/dev/null
```

### [6] TOOL CALL — ToolSearch · 2026-06-16 04:36:20 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [7] TOOL RESULT — ToolSearch · 2026-06-16 04:36:20 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [8] TOOL RESULT — Bash · 2026-06-16 04:36:20 UTC

```
{"stdout": "total 1956\ndrwxr-xr-x  2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 13 root root 2001473 Jun 16 04:27 ..\n---MEMORY---\ntotal 1969\ndrwxr-xr-x 2 root   root   1001134 Jun 16 03:59 .\ndrwxr-xr-x 3 root   root   1001134 Jun  9 03:14 ..\n-rw-r--r-- 1 root   root       517 Jun 16 03:27 MEMORY.md\n-rw-r--r-- 1 231072 231072    1460 Jun 12 03:34 project_drim_results.md\n-rw-r--r-- 1 root   root      7060 Jun 16 03:59 project_knockoff_gated_neurosymbolic.md\n-rw-r--r-- 1 root   root      2583 Jun 16 03:27 project_sae_substitution_classes.md", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] ASSISTANT · 2026-06-16 04:36:24 UTC

```
Let me check my existing memory on this project and run targeted novelty searches in parallel.
```

### [10] TOOL CALL — Read · 2026-06-16 04:36:24 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
```

### [11] TOOL RESULT — Read · 2026-06-16 04:36:24 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "content": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n\n**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.\n", "numLines": 34, "startLine": 1, "totalLines": 34}}
```

### [12] TOOL CALL — WebSearch · 2026-06-16 04:36:24 UTC

```
knockoff filter target-decoy competition FDR control LLM hallucination detection
```

### [13] TOOL CALL — WebSearch · 2026-06-16 04:36:24 UTC

```
label-free false discovery rate control LLM knowledge extraction admission neuro-symbolic
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 04:36:34 UTC

```
{"query": "label-free false discovery rate control LLM knowledge extraction admission neuro-symbolic", "results": [{"tool_use_id": "srvtoolu_015o43KuRKkCHNYKnXe4BB3T", "content": [{"title": "Neurosymbolic Information Extraction from Transactional Documents∗", "url": "https://www.arxiv.org/pdf/2512.09666"}, {"title": "LLM-Driven Knowledge Extraction in Temporal and Description Logics | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-031-77792-9_12"}, {"title": "Adjudicator: Correcting Noisy Labels with a KG-Informed Council of LLM Agents", "url": "https://arxiv.org/pdf/2512.13704"}, {"title": "Saliency Map-Guided Knowledge Discovery for Subclass Identification with LLM-Based Symbolic Approximations", "url": "https://arxiv.org/html/2511.07126"}, {"title": "(PDF) Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control", "url": "https://www.researchgate.net/publication/399853538_Neuro-Symbolic_Verification_for_Preventing_LLM_Hallucinations_in_Process_Control"}, {"title": "LLMs & Symbolic Solvers: A Neuro-Symbolic Approach", "url": "https://www.emergentmind.com/topics/llms-with-symbolic-solvers"}, {"title": "Selective Labeling with False Discovery Rate Control | OpenReview", "url": "https://openreview.net/forum?id=7ExZkCQU5Z"}, {"title": "Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control", "url": "https://doi.org/10.3390/pr14020322"}]}, "I've completed the web search for your query. Here are the results:\n\nThe search returned several relevant papers and resources on neuro-symbolic approaches, LLM knowledge extraction, and false discovery rate control:\n\n1. **Neurosymbolic Information Extraction from Transactional Documents** - This work applies multiple layers of symbolic validation to filter out erroneous outputs, ensuring only high-quality, accurate predictions are retained.\n\n2. **LLM-Driven Knowledge Extraction in Temporal and Description Logics** - This approach combines Large Language Model functionalities with symbolic verification modules as a foundational framework of neuro-symbolic knowledge acquisition systems from semi-structured data.\n\n3. **Selective Labeling with False Discovery Rate Control** - This introduces Conformal Labeling, a novel method to identify instances where AI predictions can be provably trusted by controlling the false discovery rate (FDR), the proportion of incorrect labels within the selected subset.\n\n4. **Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control** - This develops a neuro-symbolic framework in which Abductive Logic Programming evaluates the coherence of model-generated explanations, with counter-abduction generating rival hypotheses and Discourse-weighted ALP incorporating structure from operator notes.\n\n5. **Adjudicator: Correcting Noisy Labels with a KG-Informed Council of LLM Agents** - This system aims to achieve near-perfect detection of errors in a controlled environment to prove the neuro-symbolic logic is robust enough to be trusted.\n\n6. **Saliency Map-Guided Knowledge Discovery for Subclass Identification** - This proposes a neuro-symbolic approach for sensor signal-based knowledge discovery, leveraging gradient-based saliency maps derived from trained neural networks to guide the discovery process."], "durationSeconds": 10.762586393999984, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 04:36:36 UTC

```
{"query": "knockoff filter target-decoy competition FDR control LLM hallucination detection", "results": [{"tool_use_id": "srvtoolu_01HE4otNaZMrr3MH1Pd4YKab", "content": [{"title": "A Distribution-Free Framework for Rewrite-Based Human-text Detection via Knockoff Filtering", "url": "https://arxiv.org/html/2606.00402"}, {"title": "Grouped Competition Test with Unified False Discovery Rate Control", "url": "https://arxiv.org/html/2512.00901"}, {"title": "Bounding the FDP in competition-based control of the FDR", "url": "https://arxiv.org/pdf/2302.11837"}, {"title": "Unveiling the links between peptide identification and differential analysis FDR controls by means of a practical introduction to knockoff filters", "url": "https://www.biorxiv.org/content/10.1101/2021.08.20.454134.full.pdf"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}, {"title": "Local False Discovery Rate Estimation with Competition-Based Procedures   for Variable Selection", "url": "https://arxiv.org/pdf/2206.02692"}, {"title": "Competition-Based Control of the False Discovery Proportion | Biometrics | Oxford Academic", "url": "https://doi.org/10.1111/biom.13830"}, {"title": "Competition-based control of the false discovery proportion", "url": "https://arxiv.org/pdf/2011.11939"}]}, "Based on the search results, I found relevant information about these statistical methods and their application to LLM detection:\n\n## Key Findings\n\nCompetition tests generate two (or more) statistics for each hypothesis and let them compete, then incorporate the outcomes of these competitions into threshold setting. The earliest competition tests include Fixed-X Knockoff and Target-Decoy Competition.\n\n### Application to LLM Detection\n\nMost importantly, a recent framework applies statistical calibration for controlling false discoveries in rewrite-based detectors, showing that rewrite-based detection implicitly constructs knockoff samples, allowing arbitrary rewrite detectors to be converted into finite-sample calibrated detectors with FDR guarantees without retraining. Rewrite-based detection enables LLM-generated text detection to be formulated as a multiple hypothesis testing problem with knockoff structure.\n\n### General FDR Control Methods\n\nThese competition-based approaches only require a single competing decoy/knockoff null score for each observed score, where decoys are constructed so that for a true null hypothesis, the decoy and observed scores are exchangeable.\n\nThe idea of using competition for FDR control originates from the target-decoy search strategy used in mass spectrometry-based proteomics.\n\nThis intersection of statistical methods and LLM detection represents a novel application of established false discovery rate control techniques to address hallucination detection in language models."], "durationSeconds": 12.020066076999996, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 04:38:05 UTC

```
I have what I need. Key finding: the closest emerging work is a **June-2026** paper applying knockoff filtering to LLM-text *detection* (arXiv 2606.00402) — a different task, so the core idea (FDR gate at the text-to-logic admission boundary) remains novel, but it confirms "knockoffs-for-LLM" is now an active line the author should acknowledge. My memory confirms this is iteration 7 of a well-tracked evolution, and the prior review's four majors map cleanly onto what this revision changed.

Let me verify the closest competitor's scope before finalizing.
```

### [17] TOOL CALL — WebFetch · 2026-06-16 04:38:05 UTC

```
URL: https://arxiv.org/abs/2606.00402
Prompt: What task does this paper address (human-vs-machine text detection? fact extraction? hallucination?), and how does it use knockoff filtering / FDR control? Does it gate LLM-extracted symbolic facts or a neuro-symbolic admission boundary, or something else?
```

### [18] TOOL RESULT — WebFetch · 2026-06-16 04:38:05 UTC

```
{"bytes": 44582, "code": 200, "codeText": "OK", "result": "Based on the arXiv abstract provided:\n\n**Task Addressed:**\nThis paper tackles human-versus-machine text detection, specifically identifying LLM-generated content versus human-written text.\n\n**Knockoff Filtering & FDR Control Approach:**\nThe authors observe that \"rewrite-based detection implicitly constructs knockoff samples, enabling LLM-generated text detection to be formulated as a multiple hypothesis testing problem with knockoff structure.\" Rather than requiring neuro-symbolic boundaries or fact extraction, their method converts existing rewrite detectors into ones with finite-sample false discovery rate (FDR) guarantees through \"a simple calibration procedure\" without retraining.\n\n**Key Innovation:**\nThe framework separates detection statistic design from false discovery control—allowing any current rewrite-based detector to inherit statistical guarantees by applying knockoff-based calibration, demonstrated across three detection models, 19 domains, and four LLMs.\n\nThe approach doesn't gate symbolic facts or employ neuro-symbolic admission boundaries; instead, it wraps detection statistics with distribution-free statistical guarantees using knockoff filtering methodology.", "durationMs": 5017, "url": "https://arxiv.org/abs/2606.00402"}
```

### [19] ASSISTANT · 2026-06-16 04:39:18 UTC

```
Confirmed — that paper is human-vs-machine text detection, not symbolic-fact gating, so the core idea remains novel. I now have everything needed. Writing the review.
```

### [20] TOOL CALL — Write · 2026-06-16 04:39:18 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is iteration-7 of a well-tracked evolution of a genuinely novel idea: importing knockoff+/target-decoy competition (genomics/proteomics FDR control) to the neuro-symbolic text-to-logic admission boundary, giving a label-free, tunable FDR knob over which LLM-proposed Prolog facts and fuzzy-unification bridges enter a knowledge base. The revision substantively and convincingly addresses ALL four major critiques from the prior round: (1) the isolated-scoring budget is now recomputed explicitly (240 docs x ~20 candidates x 3 item-types ~= 14.4K isolated calls, ~7-15M tokens) with document-prefix prompt caching as the concrete mechanism that keeps it within the $10 hard stop; (2) the single primary disconfirmation is now populability-gated and moved to the error-dense MULTI-HOP inferred-kinship family with a pre-registered N_false_min and an explicit UNTESTABLE (not 'confirmed-by-conservatism') outcome; (3) the operational head-to-head now defines a SHARED operational construct (a single fixed claim-decomposition + relation-alignment step mapping every system to identical (head, relation, tail) triples) and RESTORES the plain zero-label confidence-threshold gate as the primary comparator; (4) a strict budget waterfall protects the two anchors before any secondary analysis. The design is exemplary in its intellectual honesty (validity condition framed as engineered-and-tested rather than a theorem; pre-registered falsifiable disconfirmation; explicit handling of the uninterpretable-null failure mode) and the related work is thorough and current. Novelty re-confirmed against the literature, including the very recent (June 2026) emergence of knockoff-filtering-for-LLM work, which targets a different task (human-vs-machine text detection) and does not threaten this contribution. Residual concerns are now second-order: (a) the calibration DIAGONAL's positive-confirmation power under document-block bootstrap may exceed what N_false_min (sized for populability) guarantees across the full alpha grid; (b) the absolute calibration claim is asserted only on toy-vocabulary CLUTRR and never directly measured on realistic Re-DocRED, with the transfer-bridge (S5) sitting in the leftover tier; (c) the symbolic-reasoning / trace-graph deliverables that the stated ACL Knowledge-Extraction goal centers are now thin relative to the statistical core; and (d) density remains the main presentation lever. These are refinements on a sound, falsifiable, feasible design rather than blocking flaws. The most probable real-world outcome (the authors honestly concede) is partial control plus a mechanism-level account of when it holds — which, given the pre-registration and the precondition-failure reporting plan, is itself a publishable result. Recommend weak accept; the proposal is on track and the highest-value remaining moves are tightening the diagonal power analysis and pulling a minimal calibration-transfer check out of the leftover tier.",
  "strengths": [
    "Genuinely novel Level-3 cross-domain methodological transfer: knockoff+/target-decoy FDR control has never been applied to gate LLM-extracted symbolic facts/bridges at a neuro-symbolic admission boundary. Novelty re-confirmed against current literature; the closest 2026 work (arXiv 2606.00402, knockoff filtering for human-vs-machine text detection) addresses a different task and is not a threat.",
    "Exemplary intellectual honesty: the knockoff null sign-flip / decoy-exchangeability condition is explicitly named as engineered-and-empirically-tested (not a theorem), the single primary disconfirmation is pre-registered and S4/S5-independent, and the design pre-registers UNTESTABLE / precondition-failure / DESCRIPTIVE outcomes rather than spinning conservatism or underpowered nulls as confirmation. The title itself honestly scopes 'calibration on CLUTRR, operational on Re-DocRED.'",
    "All four prior-round major critiques are substantively addressed with concrete, checkable mechanisms (explicit isolated-scoring budget arithmetic + document-prefix prompt caching; populability-gated disconfirmation on the error-dense multi-hop family with N_false_min; shared operational construct + restored plain-threshold zero-label comparator; explicit budget waterfall). This is a responsive, well-engineered revision.",
    "Strong, specific threat modeling of the two LLM-specific dependence channels that break the sign-flip property (within-document score correlation -> document-block bootstrap for all FDP CIs; batched-scoring contrast effects -> isolated provenance-blinded scoring), with the isolated-vs-batched check cleverly doubling as the discriminator between a scoring artifact and genuine non-exchangeability.",
    "Clean, principled division of labor across two anchors (CLUTRR crisp gold for the calibration diagonal; Re-DocRED open-vocabulary human gold for relative operational usefulness and cross-document feature variance), with the load-bearing plain confidence-threshold comparator ensuring the wedge cannot collapse to 'a threshold was enough.'",
    "Feasible, reproducible, and falsifiable: CPU-only, $10 hard stop with cost logged after every call, pre-registered power analyses, a gating Phase-0 pilot, and auditable trace-graphs with per-leaf decoy+entrapment certificates. Related work is thorough, current (2025-2026 conformal/multiple-testing line), and well-differentiated along consistent axes."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "Technically careful and honest. The core validity condition is correctly identified, the two anti-conservative dependence channels are explicitly mitigated and tested, the FDR estimator and entrapment upper bound are the correct ones from the cited proteomics literature, and the disconfirmation is pre-registered. Held back from 4 by two residual issues: the positive diagonal-tracking claim may be underpowered under document-block bootstrap relative to N_false_min (which is sized for populability, not grid-wise CI tracking), and the absolute calibration is validated only on toy CLUTRR with the CLUTRR->Re-DocRED transfer left untested in the committed budget.",
      "improvements": [
        "Run the Phase-0 power analysis explicitly against the document-block-bootstrap effective sample size and the grid-wise tracking CI width, and pre-register the false-admission/document counts needed for the positive CONFIRMED claim separately from N_false_min for populability.",
        "Pull a minimal calibration-transfer check into the committed budget: report a conservatively-biased (upper-bound) realized-FDR-vs-alpha curve on Re-DocRED against human gold, explicitly labeled as an upper bound because residual gold false negatives inflate measured FDR.",
        "Treat the decoy/false-real tail-exchangeability test as graded (with CI) rather than binary, and pre-register a conservative FDR correction for a small measured anti-conservative tail bias instead of an all-or-nothing precondition fail."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "Materially improved over prior rounds: the score-dependence robustness is now a compact threat table (exactly as the prior review requested), the claim chain is a clean per-row table, and the three load-bearing numbers are stated once. This earns credit. But density remains the dominant weakness: the assumptions block, the motivation, and several mechanism paragraphs are still long, heavily-parenthesized run-ons interleaving claim, caveat, and lingering round-over-round meta-commentary, which obscures the core novelty and will cost the ACL presentation score.",
      "improvements": [
        "Lead each assumption and each mechanism paragraph with one unqualified sentence before any caveat; lift the remaining caveats into the existing tables or footnotes.",
        "Cut residual meta-commentary ('the fair-mapping fix', 'clean division of labor', 'stated once') from the hypothesis body.",
        "Add a single 30-second plain-language mechanism paragraph a non-specialist reviewer can absorb without parsing the statistical machinery."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "A novel, auditable, label-free FDR knob at an interface where no existing label-free method offers any FDR control is a meaningful contribution that others would build on, and the cross-domain transfer is principled. The realized significance is bounded by two things the authors honestly flag: the most likely outcome is partial (not theorem-backed) control, and the absolute calibration is demonstrated on a closed toy vocabulary while the realistic-domain claim is only relative. Elevating the transfer story and the symbolic-reasoning deliverables would push this toward 4.",
      "improvements": [
        "Elevate at least the descriptive S5 transfer correlation (when does CLUTRR-calibrated control hold on Re-DocRED?) from leftover-only to a committed deliverable, so the calibration->operational link is characterized rather than skipped.",
        "Concretely scope the brief's neuro-symbolic deliverables (multi-hop hallucinated-conclusion-rate vs RAW LLM generation; exported trace-graphs with per-leaf certificates) within the committed budget, not contingent on leftover budget.",
        "State the expected practical payoff at coarse alpha (~0.1) more concretely so a reader sees why even partial control is a useful, tunable knob."
      ]
    }
  ],
  "critiques": [
    {
      "category": "rigor",
      "severity": "major",
      "description": "The positive CONFIRMED criterion requires the realized-FDR-vs-alpha diagonal to TRACK alpha 'within tau above the 1/k floor across the demonstrable grid' (alpha in [0.05, 0.5]) on the populable CLUTRR family, with document-block-bootstrap CIs. The pre-registered N_false_min (default 40 pooled false admissions) is sized to establish POPULABILITY (that the diagonal is non-vacuous), but it is not obviously sized to demonstrate grid-wise TRACKING. The document-block bootstrap resamples whole documents (~120), sharply reducing effective sample size relative to i.i.d. candidate counts; spreading ~40 false admissions across 5+ alpha grid points leaves only a handful per point, which is likely underpowered for a CI-based 'tracks within tau' claim. The single-point primary disconfirmation at alpha* may remain estimable, but the positive confirmation risks exactly the uninterpretable-null outcome the design is built to avoid.",
      "suggested_action": "In Phase-0, run the diagonal power analysis explicitly against (i) the document-block-bootstrap effective sample size and (ii) the per-grid-point CI width needed to assert 'within tau.' Pre-register the false-admission and document counts required for the positive tracking claim SEPARATELY from N_false_min for populability. If the budget cannot reach it, concentrate the grid on fewer alpha points with adequate per-point counts, widen tau with justification, or down-scope the positive claim to 'diagonal estimable and not anti-conservative at alpha*' while reporting the full grid descriptively."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "By design the absolute FDR diagonal — the actual test of whether the knob is calibrated — is asserted ONLY on CLUTRR's closed, deterministic kinship vocabulary, which the motivation itself concedes is the wrong place to demonstrate usefulness. On Re-DocRED only RELATIVE claims (decoy-gating beats the plain threshold at matched recall) are asserted; the knob's calibration is never measured there because of residual gold false negatives. The intended bridge — S5, the predictive account of WHEN calibration transfers — is explicitly a leftover-budget item that may be reported merely DESCRIPTIVE. The net risk: after the full budget is spent, the headline 'calibrated label-free FDR knob useful on realistic text' is established only as {calibrated on a toy domain} + {relatively-better-than-threshold on realistic text}, with no direct evidence the calibration transfers — a significance ceiling even if every confirmatory cell passes.",
      "suggested_action": "Pull a minimal calibration-transfer check out of the leftover tier into the committed Re-DocRED anchor. Residual gold false negatives bias realized FDR measured against human gold UPWARD (uncounted-true triples scored as false admissions), so a realized-FDR-vs-alpha curve on Re-DocRED is a conservative UPPER BOUND: if even this upper-bound curve stays near alpha it is strong suggestive evidence of transfer, and if it blows up it localizes the failure. Report it explicitly as an upper bound. Alternatively, pre-register the descriptive S5 transfer correlation as a non-optional deliverable so the calibration->operational link is at least characterized rather than skipped."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The entire headline reduces to one empirical precondition: that engineered 'document-conditioned counterfactual' decoys are score-exchangeable in the upper tail with NATURALLY-occurring false reals (extractor hallucinations). These arise from two different generative processes — deliberate plausible-but-non-entailed construction vs. spontaneous extraction error — so their tail score distributions need not match, and the method treats the tail-conditioned win-rate ~0.5 test as a binary pass/fail gate. A moderate, consistent deviation (e.g., win-rate 0.4) would fail the headline outright with no graceful fallback, even though such a deviation is informative and partially correctable.",
      "suggested_action": "Report the tail win-rate / upper-tail two-sample statistic as a graded quantity with CI, and pre-register a graded response: a small measured anti-conservative tail bias triggers a documented conservative FDR correction (inflate the estimate by the measured bias) rather than a binary fail. Additionally report the direct match of the decoy score distribution to the GOLD false-real score distribution in the tail on the labeled slice — that distributional match, not the win-rate alone, is the actual validity condition."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "The stated GOAL and venue (ACL Knowledge Extraction) center an operational text->FOL->Prolog pipeline with ontology grounding, multi-hop symbolic deduction, human-auditable trace-graphs, and a quantified hallucination reduction vs RAW LLM generation. In this iteration the substantive contribution has (defensibly) concentrated on the statistical FDR gate, while the symbolic-reasoning deliverables are thin: the ontology is 'used ONLY for typing,' SWI-Prolog multi-hop deduction and trace-graphs appear mainly as pipeline step (9), and S6 (alpha -> multi-hop hallucination propagation) plus rule-gating are preliminary/leftover. A reviewer expecting the neuro-symbolic deliverables of the brief may find the audit-trail and vs-raw-LLM contributions underdeveloped relative to the calibration study.",
      "suggested_action": "Within the committed (non-leftover) budget, concretely scope the minimum symbolic-reasoning deliverables the brief requires: at least one quantified multi-hop hallucinated-conclusion-rate comparison of the gated pipeline vs RAW LLM generation (make the 'vs raw generation' delta explicit beyond CoT/RAG), and a small concrete set of exported trace-graphs with per-leaf certificates. Keep S6's magnitude claim preliminary, but ensure the audit-trail and vs-raw-LLM deliverables are not entirely contingent on leftover budget."
    },
    {
      "category": "evidence",
      "severity": "minor",
      "description": "The knockoffs-for-LLM space is now moving quickly. A June-2026 paper ('A Distribution-Free Framework for Rewrite-Based Human-text Detection via Knockoff Filtering,' arXiv 2606.00402) applies knockoff filtering with finite-sample FDR guarantees to LLM-generated-text detection by observing that rewrite-based detection implicitly constructs knockoffs — a different task (machine-vs-human text detection), but the same core import of knockoff competition into an LLM pipeline. It is not a novelty threat to gating the text-to-logic admission boundary, but a top reviewer will expect awareness that 'knockoffs/decoy competition for LLM tasks' is now an active, independently-emerging line.",
      "suggested_action": "Add one sentence positioning this work against the emerging knockoff/decoy-competition-for-LLM line (e.g., rewrite-based knockoff detection), reusing the existing axes: those methods construct knockoffs for output/text-level detection with finite-sample guarantees under their own exchangeability constructions, whereas this work places engineered, empirically-tested decoys at the neuro-symbolic ADMISSION boundary (no construction-level guarantee), with independent entrapment corroboration and symbolic propagation."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "Density remains the dominant presentation weakness. The threat table, the claim-chain table, and the 'three numbers stated once' discipline are genuine, creditable improvements over prior rounds, but the assumptions block, the motivation, and several mechanism paragraphs are still long, heavily-parenthesized run-ons that interleave claim, caveat, and lingering round-over-round meta-commentary. For an ACL submission this will cost the presentation score and partly obscure the core novelty.",
      "suggested_action": "Lead each assumption and each mechanism paragraph with one unqualified sentence before any caveat; lift remaining caveats into the existing tables or footnotes. Cut residual meta-commentary ('the fair-mapping fix', 'clean division of labor'). Add a one-paragraph plain-language mechanism statement absorbable in 30 seconds by a non-specialist."
    }
  ],
  "score": 6,
  "confidence": 4,
  "relation_type": "evolution",
  "relation_rationale": "Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline."
}
```

### [21] TOOL RESULT — Write · 2026-06-16 04:39:18 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is iteration-7 of a well-tracked evolution of a genuinely novel idea: importing knockoff+/target-decoy competition (genomics/proteomics FDR control) to the neuro-symbolic text-to-logic admission boundary, giving a label-free, tunable FDR knob over which LLM-proposed Prolog facts and fuzzy-unification bridges enter a knowledge base. The revision substantively and convincingly addresses ALL four major critiques from the prior round: (1) the isolated-scoring budget is now recomputed explicitly (240 docs x ~20 candidates x 3 item-types ~= 14.4K isolated calls, ~7-15M tokens) with document-prefix prompt caching as the concrete mechanism that keeps it within the $10 hard stop; (2) the single primary disconfirmation is now populability-gated and moved to the error-dense MULTI-HOP inferred-kinship family with a pre-registered N_false_min and an explicit UNTESTABLE (not 'confirmed-by-conservatism') outcome; (3) the operational head-to-head now defines a SHARED operational construct (a single fixed claim-decomposition + relation-alignment step mapping every system to identical (head, relation, tail) triples) and RESTORES the plain zero-label confidence-threshold gate as the primary comparator; (4) a strict budget waterfall protects the two anchors before any secondary analysis. The design is exemplary in its intellectual honesty (validity condition framed as engineered-and-tested rather than a theorem; pre-registered falsifiable disconfirmation; explicit handling of the uninterpretable-null failure mode) and the related work is thorough and current. Novelty re-confirmed against the literature, including the very recent (June 2026) emergence of knockoff-filtering-for-LLM work, which targets a different task (human-vs-machine text detection) and does not threaten this contribution. Residual concerns are now second-order: (a) the calibration DIAGONAL's positive-confirmation power under document-block bootstrap may exceed what N_false_min (sized for populability) guarantees across the full alpha grid; (b) the absolute calibration claim is asserted only on toy-vocabulary CLUTRR and never directly measured on realistic Re-DocRED, with the transfer-bridge (S5) sitting in the leftover tier; (c) the symbolic-reasoning / trace-graph deliverables that the stated ACL Knowledge-Extraction goal centers are now thin relative to the statistical core; and (d) density remains the main presentation lever. These are refinements on a sound, falsifiable, feasible design rather than blocking flaws. The most probable real-world outcome (the authors honestly concede) is partial control plus a mechanism-level account of when it holds — which, given the pre-registration and the precondition-failure reporting plan, is itself a publishable result. Recommend weak accept; the proposal is on track and the highest-value remaining moves are tightening the diagonal power analysis and pulling a minimal calibration-transfer check out of the leftover tier.\",\n  \"strengths\": [\n    \"Genuinely novel Level-3 cross-domain methodological transfer: knockoff+/target-decoy FDR control has never been applied to gate LLM-extracted symbolic facts/bridges at a neuro-symbolic admission boundary. Novelty re-confirmed against current literature; the closest 2026 work (arXiv 2606.00402, knockoff filtering for human-vs-machine text detection) addresses a different task and is not a threat.\",\n    \"Exemplary intellectual honesty: the knockoff null sign-flip / decoy-exchangeability condition is explicitly named as engineered-and-empirically-tested (not a theorem), the single primary disconfirmation is pre-registered and S4/S5-independent, and the design pre-registers UNTESTABLE / precondition-failure / DESCRIPTIVE outcomes rather than spinning conservatism or underpowered nulls as confirmation. The title itself honestly scopes 'calibration on CLUTRR, operational on Re-DocRED.'\",\n    \"All four prior-round major critiques are substantively addressed with concrete, checkable mechanisms (explicit isolated-scoring budget arithmetic + document-prefix prompt caching; populability-gated disconfirmation on the error-dense multi-hop family with N_false_min; shared operational construct + restored plain-threshold zero-label comparator; explicit budget waterfall). This is a responsive, well-engineered revision.\",\n    \"Strong, specific threat modeling of the two LLM-specific dependence channels that break the sign-flip property (within-document score correlation -> document-block bootstrap for all FDP CIs; batched-scoring contrast effects -> isolated provenance-blinded scoring), with the isolated-vs-batched check cleverly doubling as the discriminator between a scoring artifact and genuine non-exchangeability.\",\n    \"Clean, principled division of labor across two anchors (CLUTRR crisp gold for the calibration diagonal; Re-DocRED open-vocabulary human gold for relative operational usefulness and cross-document feature variance), with the load-bearing plain confidence-threshold comparator ensuring the wedge cannot collapse to 'a threshold was enough.'\",\n    \"Feasible, reproducible, and falsifiable: CPU-only, $10 hard stop with cost logged after every call, pre-registered power analyses, a gating Phase-0 pilot, and auditable trace-graphs with per-leaf decoy+entrapment certificates. Related work is thorough, current (2025-2026 conformal/multiple-testing line), and well-differentiated along consistent axes.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"Technically careful and honest. The core validity condition is correctly identified, the two anti-conservative dependence channels are explicitly mitigated and tested, the FDR estimator and entrapment upper bound are the correct ones from the cited proteomics literature, and the disconfirmation is pre-registered. Held back from 4 by two residual issues: the positive diagonal-tracking claim may be underpowered under document-block bootstrap relative to N_false_min (which is sized for populability, not grid-wise CI tracking), and the absolute calibration is validated only on toy CLUTRR with the CLUTRR->Re-DocRED transfer left untested in the committed budget.\",\n      \"improvements\": [\n        \"Run the Phase-0 power analysis explicitly against the document-block-bootstrap effective sample size and the grid-wise tracking CI width, and pre-register the false-admission/document counts needed for the positive CONFIRMED claim separately from N_false_min for populability.\",\n        \"Pull a minimal calibration-transfer check into the committed budget: report a conservatively-biased (upper-bound) realized-FDR-vs-alpha curve on Re-DocRED against human gold, explicitly labeled as an upper bound because residual gold false negatives inflate measured FDR.\",\n        \"Treat the decoy/false-real tail-exchangeability test as graded (with CI) rather than binary, and pre-register a conservative FDR correction for a small measured anti-conservative tail bias instead of an all-or-nothing precondition fail.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"Materially improved over prior rounds: the score-dependence robustness is now a compact threat table (exactly as the prior review requested), the claim chain is a clean per-row table, and the three load-bearing numbers are stated once. This earns credit. But density remains the dominant weakness: the assumptions block, the motivation, and several mechanism paragraphs are still long, heavily-parenthesized run-ons interleaving claim, caveat, and lingering round-over-round meta-commentary, which obscures the core novelty and will cost the ACL presentation score.\",\n      \"improvements\": [\n        \"Lead each assumption and each mechanism paragraph with one unqualified sentence before any caveat; lift the remaining caveats into the existing tables or footnotes.\",\n        \"Cut residual meta-commentary ('the fair-mapping fix', 'clean division of labor', 'stated once') from the hypothesis body.\",\n        \"Add a single 30-second plain-language mechanism paragraph a non-specialist reviewer can absorb without parsing the statistical machinery.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"A novel, auditable, label-free FDR knob at an interface where no existing label-free method offers any FDR control is a meaningful contribution that others would build on, and the cross-domain transfer is principled. The realized significance is bounded by two things the authors honestly flag: the most likely outcome is partial (not theorem-backed) control, and the absolute calibration is demonstrated on a closed toy vocabulary while the realistic-domain claim is only relative. Elevating the transfer story and the symbolic-reasoning deliverables would push this toward 4.\",\n      \"improvements\": [\n        \"Elevate at least the descriptive S5 transfer correlation (when does CLUTRR-calibrated control hold on Re-DocRED?) from leftover-only to a committed deliverable, so the calibration->operational link is characterized rather than skipped.\",\n        \"Concretely scope the brief's neuro-symbolic deliverables (multi-hop hallucinated-conclusion-rate vs RAW LLM generation; exported trace-graphs with per-leaf certificates) within the committed budget, not contingent on leftover budget.\",\n        \"State the expected practical payoff at coarse alpha (~0.1) more concretely so a reader sees why even partial control is a useful, tunable knob.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The positive CONFIRMED criterion requires the realized-FDR-vs-alpha diagonal to TRACK alpha 'within tau above the 1/k floor across the demonstrable grid' (alpha in [0.05, 0.5]) on the populable CLUTRR family, with document-block-bootstrap CIs. The pre-registered N_false_min (default 40 pooled false admissions) is sized to establish POPULABILITY (that the diagonal is non-vacuous), but it is not obviously sized to demonstrate grid-wise TRACKING. The document-block bootstrap resamples whole documents (~120), sharply reducing effective sample size relative to i.i.d. candidate counts; spreading ~40 false admissions across 5+ alpha grid points leaves only a handful per point, which is likely underpowered for a CI-based 'tracks within tau' claim. The single-point primary disconfirmation at alpha* may remain estimable, but the positive confirmation risks exactly the uninterpretable-null outcome the design is built to avoid.\",\n      \"suggested_action\": \"In Phase-0, run the diagonal power analysis explicitly against (i) the document-block-bootstrap effective sample size and (ii) the per-grid-point CI width needed to assert 'within tau.' Pre-register the false-admission and document counts required for the positive tracking claim SEPARATELY from N_false_min for populability. If the budget cannot reach it, concentrate the grid on fewer alpha points with adequate per-point counts, widen tau with justification, or down-scope the positive claim to 'diagonal estimable and not anti-conservative at alpha*' while reporting the full grid descriptively.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"By design the absolute FDR diagonal — the actual test of whether the knob is calibrated — is asserted ONLY on CLUTRR's closed, deterministic kinship vocabulary, which the motivation itself concedes is the wrong place to demonstrate usefulness. On Re-DocRED only RELATIVE claims (decoy-gating beats the plain threshold at matched recall) are asserted; the knob's calibration is never measured there because of residual gold false negatives. The intended bridge — S5, the predictive account of WHEN calibration transfers — is explicitly a leftover-budget item that may be reported merely DESCRIPTIVE. The net risk: after the full budget is spent, the headline 'calibrated label-free FDR knob useful on realistic text' is established only as {calibrated on a toy domain} + {relatively-better-than-threshold on realistic text}, with no direct evidence the calibration transfers — a significance ceiling even if every confirmatory cell passes.\",\n      \"suggested_action\": \"Pull a minimal calibration-transfer check out of the leftover tier into the committed Re-DocRED anchor. Residual gold false negatives bias realized FDR measured against human gold UPWARD (uncounted-true triples scored as false admissions), so a realized-FDR-vs-alpha curve on Re-DocRED is a conservative UPPER BOUND: if even this upper-bound curve stays near alpha it is strong suggestive evidence of transfer, and if it blows up it localizes the failure. Report it explicitly as an upper bound. Alternatively, pre-register the descriptive S5 transfer correlation as a non-optional deliverable so the calibration->operational link is at least characterized rather than skipped.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The entire headline reduces to one empirical precondition: that engineered 'document-conditioned counterfactual' decoys are score-exchangeable in the upper tail with NATURALLY-occurring false reals (extractor hallucinations). These arise from two different generative processes — deliberate plausible-but-non-entailed construction vs. spontaneous extraction error — so their tail score distributions need not match, and the method treats the tail-conditioned win-rate ~0.5 test as a binary pass/fail gate. A moderate, consistent deviation (e.g., win-rate 0.4) would fail the headline outright with no graceful fallback, even though such a deviation is informative and partially correctable.\",\n      \"suggested_action\": \"Report the tail win-rate / upper-tail two-sample statistic as a graded quantity with CI, and pre-register a graded response: a small measured anti-conservative tail bias triggers a documented conservative FDR correction (inflate the estimate by the measured bias) rather than a binary fail. Additionally report the direct match of the decoy score distribution to the GOLD false-real score distribution in the tail on the labeled slice — that distributional match, not the win-rate alone, is the actual validity condition.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The stated GOAL and venue (ACL Knowledge Extraction) center an operational text->FOL->Prolog pipeline with ontology grounding, multi-hop symbolic deduction, human-auditable trace-graphs, and a quantified hallucination reduction vs RAW LLM generation. In this iteration the substantive contribution has (defensibly) concentrated on the statistical FDR gate, while the symbolic-reasoning deliverables are thin: the ontology is 'used ONLY for typing,' SWI-Prolog multi-hop deduction and trace-graphs appear mainly as pipeline step (9), and S6 (alpha -> multi-hop hallucination propagation) plus rule-gating are preliminary/leftover. A reviewer expecting the neuro-symbolic deliverables of the brief may find the audit-trail and vs-raw-LLM contributions underdeveloped relative to the calibration study.\",\n      \"suggested_action\": \"Within the committed (non-leftover) budget, concretely scope the minimum symbolic-reasoning deliverables the brief requires: at least one quantified multi-hop hallucinated-conclusion-rate comparison of the gated pipeline vs RAW LLM generation (make the 'vs raw generation' delta explicit beyond CoT/RAG), and a small concrete set of exported trace-graphs with per-leaf certificates. Keep S6's magnitude claim preliminary, but ensure the audit-trail and vs-raw-LLM deliverables are not entirely contingent on leftover budget.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The knockoffs-for-LLM space is now moving quickly. A June-2026 paper ('A Distribution-Free Framework for Rewrite-Based Human-text Detection via Knockoff Filtering,' arXiv 2606.00402) applies knockoff filtering with finite-sample FDR guarantees to LLM-generated-text detection by observing that rewrite-based detection implicitly constructs knockoffs — a different task (machine-vs-human text detection), but the same core import of knockoff competition into an LLM pipeline. It is not a novelty threat to gating the text-to-logic admission boundary, but a top reviewer will expect awareness that 'knockoffs/decoy competition for LLM tasks' is now an active, independently-emerging line.\",\n      \"suggested_action\": \"Add one sentence positioning this work against the emerging knockoff/decoy-competition-for-LLM line (e.g., rewrite-based knockoff detection), reusing the existing axes: those methods construct knockoffs for output/text-level detection with finite-sample guarantees under their own exchangeability constructions, whereas this work places engineered, empirically-tested decoys at the neuro-symbolic ADMISSION boundary (no construction-level guarantee), with independent entrapment corroboration and symbolic propagation.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"Density remains the dominant presentation weakness. The threat table, the claim-chain table, and the 'three numbers stated once' discipline are genuine, creditable improvements over prior rounds, but the assumptions block, the motivation, and several mechanism paragraphs are still long, heavily-parenthesized run-ons that interleave claim, caveat, and lingering round-over-round meta-commentary. For an ACL submission this will cost the presentation score and partly obscure the core novelty.\",\n      \"suggested_action\": \"Lead each assumption and each mechanism paragraph with one unqualified sentence before any caveat; lift remaining caveats into the existing tables or footnotes. Cut residual meta-commentary ('the fair-mapping fix', 'clean division of labor'). Add a one-paragraph plain-language mechanism statement absorbable in 30 seconds by a non-specialist.\"\n    }\n  ],\n  \"score\": 6,\n  \"confidence\": 4,\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [22] ASSISTANT · 2026-06-16 04:39:26 UTC

```
Let me validate the JSON and update my project memory with this iteration's verdict for pipeline continuity.
```

### [23] TOOL CALL — Bash · 2026-06-16 04:39:26 UTC

```
Validate review JSON structure and key fields:
python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json')); print('VALID JSON'); print('score',d['score'],'conf',d['confidence'],'rel',d['relation_type']); print('critiques',len(d['critiques']),'majors',sum(1 for c in d['critiques'] if c['severity']=='major')); print('dims',[(s['dimension'],s['score']) for s in d['dimension_scores']])"
```

### [24] TOOL RESULT — Bash · 2026-06-16 04:39:26 UTC

```
{"stdout": "VALID JSON\nscore 6 conf 4 rel evolution\ncritiques 6 majors 2\ndims [('soundness', 3), ('presentation', 3), ('contribution', 3)]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [25] ASSISTANT · 2026-06-16 04:39:44 UTC

```
Now updating my project memory with the iter_7 verdict for continuity across pipeline rounds.
```

### [26] TOOL CALL — Edit · 2026-06-16 04:39:44 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md
OLD: 4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.
NEW: 4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.

**REVIEW_HYPO iter_7 verdict (2026-06-16):** score 6/10 (weak accept, up from 5), conf 4. Soundness 3, Presentation 3 (bumped from 2 — threat table + claim-chain table delivered as prior review asked), Contribution 3. relation_type=evolution. All 4 prior-iter_4 majors substantively ADDRESSED: (a) isolated-scoring budget recomputed explicitly (240 docs×~20 cand×3 item-types≈14.4K calls, 7-15M tok) + document-prefix prompt caching → fits $10 hard stop; (b) primary disconfirmation now POPULABILITY-GATED, moved to error-dense MULTI-HOP kinship family w/ N_false_min=40, explicit UNTESTABLE outcome; (c) SHARED operational construct (fixed claim-decomp+relation-align maps all systems to identical (h,r,t) triples) + RESTORED plain zero-label confidence-threshold comparator; (d) explicit BUDGET WATERFALL. Novelty re-confirmed: closest new work arXiv 2606.00402 (Jun 2026, knockoff filtering) = human-vs-machine TEXT DETECTION, different task, NOT a threat — but add 1 sentence of awareness. 2 residual majors (second-order, not blocking): (1) rigor — diagonal positive-CONFIRMATION power: N_false_min sized for populability not grid-wise tracking CIs under document-block bootstrap (~120 docs); ~40 false admissions across 5+ alpha points → underpowered positive claim (single-point disconfirmation OK). Fix: pre-register grid-tracking power separately. (2) methodology/significance — absolute calibration asserted ONLY on toy CLUTRR; Re-DocRED only RELATIVE; S5 transfer-bridge is leftover-budget → headline 'calibrated knob useful on realistic text' never directly connected. Fix: pull a conservatively-biased (upper-bound, gold-FN-inflated) realized-FDR curve on Re-DocRED into committed budget. 4 minors: graded (not binary) decoy/false-real tail-exchangeability test w/ conservative correction; symbolic-reasoning/trace-graph/OpenCyc + vs-RAW-LLM deliverables now thin vs statistical core (goal/venue alignment) — commit them non-leftover; cite 2606.00402 line; density still the main presentation lever. Output written to run dir.
```

### [27] TOOL RESULT — Edit · 2026-06-16 04:39:44 UTC

```
{"filePath": "/root/.claude/projects/-ai-inventor/memory/project_knockoff_gated_neurosymbolic.md", "oldString": "4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.", "newString": "4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\n\n**REVIEW_HYPO iter_7 verdict (2026-06-16):** score 6/10 (weak accept, up from 5), conf 4. Soundness 3, Presentation 3 (bumped from 2 — threat table + claim-chain table delivered as prior review asked), Contribution 3. relation_type=evolution. All 4 prior-iter_4 majors substantively ADDRESSED: (a) isolated-scoring budget recomputed explicitly (240 docs×~20 cand×3 item-types≈14.4K calls, 7-15M tok) + document-prefix prompt caching → fits $10 hard stop; (b) primary disconfirmation now POPULABILITY-GATED, moved to error-dense MULTI-HOP kinship family w/ N_false_min=40, explicit UNTESTABLE outcome; (c) SHARED operational construct (fixed claim-decomp+relation-align maps all systems to identical (h,r,t) triples) + RESTORED plain zero-label confidence-threshold comparator; (d) explicit BUDGET WATERFALL. Novelty re-confirmed: closest new work arXiv 2606.00402 (Jun 2026, knockoff filtering) = human-vs-machine TEXT DETECTION, different task, NOT a threat — but add 1 sentence of awareness. 2 residual majors (second-order, not blocking): (1) rigor — diagonal positive-CONFIRMATION power: N_false_min sized for populability not grid-wise tracking CIs under document-block bootstrap (~120 docs); ~40 false admissions across 5+ alpha points → underpowered positive claim (single-point disconfirmation OK). Fix: pre-register grid-tracking power separately. (2) methodology/significance — absolute calibration asserted ONLY on toy CLUTRR; Re-DocRED only RELATIVE; S5 transfer-bridge is leftover-budget → headline 'calibrated knob useful on realistic text' never directly connected. Fix: pull a conservatively-biased (upper-bound, gold-FN-inflated) realized-FDR curve on Re-DocRED into committed budget. 4 minors: graded (not binary) decoy/false-real tail-exchangeability test w/ conservative correction; symbolic-reasoning/trace-graph/OpenCyc + vs-RAW-LLM deliverables now thin vs statistical core (goal/venue alignment) — commit them non-leftover; cite 2606.00402 line; density still the main presentation lever. Output written to run dir.", "originalFile": "---\nname: project_knockoff_gated_neurosymbolic\ndescription: GEN_HYPO output for run_MQN7mBg4AhvH — knockoff/decoy FDR-control gate for neuro-symbolic text-to-logic\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 184753b0-79a6-4fe0-b1f3-565fe0def156\n---\n\nHypothesis generated 2026-06-16 for run_MQN7mBg4AhvH (UNSEEDED GEN_HYPO), AII prompt = text→FOL→Prolog neuro-symbolic pipeline, ACL Knowledge Extraction venue.\n\n**Core idea:** Import the knockoff filter (Barber & Candès) / target-decoy competition (proteomics) FDR-control principle to gate the neural→symbolic boundary. Every LLM-proposed symbolic assertion (atomic fact, fuzzy-unification bridge, common-sense rule) is competed against matched synthetic decoys (exchangeable-but-false); admissions are thresholded on decoy-estimated false-discovery rate → label-free, per-document, tunable hallucination control propagated through Prolog/ProbLog multi-hop reasoning.\n\n**Why novel:** knockoff/target-decoy confined to genomics/proteomics/stats; never applied to LLM extraction or neuro-symbolic reasoning. Abandoned (too crowded): ontology-constraint filtering, MaxSAT/consistency consensus, LLM→ProbLog probs, soft/fuzzy unification (NTP, Bousi~Prolog), conformal prediction (CP+ASP, predicate-conditional conformal KG, PASC), abductive missing-premise (2511.04020).\n\n**Crux assumption to test:** decoy exchangeability (realized FDR tracks target α). Validate on ProofWriter/RuleTaker, CLUTRR, + small hand-annotated legal/news/story docs.\n\nOutput written to run dir `.terminal_claude_agent_struct_out.json`.\n\n**REVIEW_HYPO iter_1 verdict (2026-06-16):** score 5/10 (borderline), conf 4. Soundness 2, Presentation 3, Contribution 3. 4 major critiques the author should fix before/early in experiments:\n1. (rigor, #1 risk) Decoy exchangeability / proteomics Equal Chance Assumption likely fails ANTI-CONSERVATIVELY: dangerous hallucinations are PLAUSIBLE (high LLM confidence), but random type-matched entity/relation-swap decoys are easy negatives (low score) → admitted-decoy count under-estimates false reals → realized FDR EXCEEDS target. TDC lit: \"too unrealistic to fool\" → FDP under-estimated. Fix: generate decoys as LLM-fabricated plausible-but-contradicted counterfactuals (+ cross-doc decoys); add direct ECA diagnostic (false-real vs decoy win-rate ≈0.5 on labeled probe) BEFORE trusting calibration curve.\n2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"\n3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.\n4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.\nMinors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).\n\n**REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:\n1. Decoy REDESIGN → **plausibility-matched decoys**: drawn from LLM's own generative prior over document-plausible-but-non-entailed facts + cross-document decoys (true elsewhere, false here); random type-swaps kept only as deliberately-easy failing baseline. Imported principle from cheminformatics/proteomics property-matched decoys (DeepCoy, protein-LM decoys): \"decoy hits must reproduce false-target-hit behavior.\"\n2. NEW central methodological import — **entrapment validation** (Nature Methods 2025, proteomics): spike plausibility-matched, false-BY-CONSTRUCTION facts (foreign injected entities) into pool; admitted-entrapment/admitted-total = label-free estimate of realized false-admission, validates decoy-FDR with NO labels. Plus win-rate ECA diagnostic (~0.5) on small labeled probe (measurement only).\n3. Conformal baselines added as actual BASELINES at matched label budget: Mohri-Hashimoto (2402.10978), Jin-Candès conformal selection+BH (2210.01408), Coherent Factuality (2505.17126) — all confirmed to NEED labeled calibration → sharpens label-free wedge. + hybrid decoy+conformal ablation.\n4. FDR re-scoped to **corpus-aggregate** + report achievable-α floor (~1/(k+1)). RuleTaker/ProofWriter → propagation only; headline extraction-PR on CLUTRR + enlarged realistic set (power analysis). Crisp SWI-Prolog primary; ProbLog arm now explicit isotonic map on probe, ablated. Matched-recall = full PR curves (claim-decompose + entailment-match for free-form baselines). Non-entailment contamination-rate audit. Propagation = fitted Monte-Carlo fan-out/conjunction model + measured amplification. Novelty re-verified clean (no decoy/knockoff FDR for LLM-extracted symbolic facts exists). Output re-written to run dir.\n\n**REVIEW_HYPO iter_4 verdict (2026-06-16):** score 5/10 (borderline, improving), conf 4. Soundness 3, Presentation 2, Contribution 3. relation_type=evolution. Prior review's 6 critiques all substantively ADDRESSED (Phase-0 pilot gates headline; tail-specific per-genre power analysis; demonstrable-alpha regime bounded as f(k,r) w/ TDC-SB/UB + +1-removal cited; S4 promoted to predictive out-of-sample account; contamination char. w/ symmetric label-budget accounting). Novelty re-confirmed via web (target-decoy/knockoff still never applied to LLM extraction; closest = arXiv 2508.18473 'Principled Detection of Hallucinations via Multiple Testing' = conformal p-values+BH, NEEDS labeled calib → reinforces label-free wedge, NOT a threat; WebFetch fast-model falsely claimed it used decoys — verified via PDF grep it does not). 4 NEW majors (next layer exposed): (1) S4 'out-of-sample on held-out genre' = n=1 genre → de-risk unvalidatable; fix = document-level leave-cluster-out CV. (2) Entrapment inherits 'too-easy→anti-conservative' failure like decoys but has NO tail-difficulty diagnostic → co-failure likely; add tail diagnostic for entrapment. (3) Scope ballooned vs $10/CPU + unbudgeted hand-annotation → publish feasibility call/doc counts, demote S5/rule-gating/ProbLog/TDC-SB-UB to if-budget. (4) Bridge-rule truth/non-entailment semantics under-defined (universally-quantified/defeasible) → gold arbiter ill-specified for half the headline. 3 minors: multiple-comparisons hygiene ('at least one family' disjunction, pre-register confirmatory cell); cite arXiv 2508.18473 + DINCO; density still unfixed (worse). Output written to run dir.\n", "structuredPatch": [{"oldStart": 22, "oldLines": 6, "newStart": 22, "newLines": 8, "lines": [" 2. (evidence/novelty) Add missing label-efficient baselines, not just related work: Mohri & Hashimoto ICML2024 conformal factuality (claim filtering to user α, few labels); conformal selection (Jin & Candès)+BH; Coherent Factuality 2505.17126 (multi-step). Re-sharpen wedge to \"fully label-free + gates neural→symbolic interface + symbolic propagation + per-leaf certificates.\"", " 3. (rigor) Per-doc candidate count ~10-40 → TDC high-variance; knockoff+ offset makes small α unachievable (min FDR ≈1/(k+1)). Re-scope control to corpus-AGGREGATE, report achievable-α floor.", " 4. (scope) RuleTaker/ProofWriter extraction is near-trivial (facts already symbolic) → use for proof-propagation only; headline precision claims belong to CLUTRR + (underpowered) realistic legal/news set — enlarge it, run power analysis.", "+", "+**REVIEW_HYPO iter_7 verdict (2026-06-16):** score 6/10 (weak accept, up from 5), conf 4. Soundness 3, Presentation 3 (bumped from 2 — threat table + claim-chain table delivered as prior review asked), Contribution 3. relation_type=evolution. All 4 prior-iter_4 majors substantively ADDRESSED: (a) isolated-scoring budget recomputed explicitly (240 docs×~20 cand×3 item-types≈14.4K calls, 7-15M tok) + document-prefix prompt caching → fits $10 hard stop; (b) primary disconfirmation now POPULABILITY-GATED, moved to error-dense MULTI-HOP kinship family w/ N_false_min=40, explicit UNTESTABLE outcome; (c) SHARED operational construct (fixed claim-decomp+relation-align maps all systems to identical (h,r,t) triples) + RESTORED plain zero-label confidence-threshold comparator; (d) explicit BUDGET WATERFALL. Novelty re-confirmed: closest new work arXiv 2606.00402 (Jun 2026, knockoff filtering) = human-vs-machine TEXT DETECTION, different task, NOT a threat — but add 1 sentence of awareness. 2 residual majors (second-order, not blocking): (1) rigor — diagonal positive-CONFIRMATION power: N_false_min sized for populability not grid-wise tracking CIs under document-block bootstrap (~120 docs); ~40 false admissions across 5+ alpha points → underpowered positive claim (single-point disconfirmation OK). Fix: pre-register grid-tracking power separately. (2) methodology/significance — absolute calibration asserted ONLY on toy CLUTRR; Re-DocRED only RELATIVE; S5 transfer-bridge is leftover-budget → headline 'calibrated knob useful on realistic text' never directly connected. Fix: pull a conservatively-biased (upper-bound, gold-FN-inflated) realized-FDR curve on Re-DocRED into committed budget. 4 minors: graded (not binary) decoy/false-real tail-exchangeability test w/ conservative correction; symbolic-reasoning/trace-graph/OpenCyc + vs-RAW-LLM deliverables now thin vs statistical core (goal/venue alignment) — commit them non-leftover; cite 2606.00402 line; density still the main presentation lever. Output written to run dir.", " Minors: label-free score→ProbLog-prob mapping unjustified; \"matched recall\" across CoT/RAG/LINC not operationalized; decoy non-entailment verification is itself error-prone; propagation is nonlinear (fan-out amplification), not smoothly monotone. relation_type=null (iter 1).", " ", " **REVISION iter_2 (2026-06-16):** Revised same hypothesis (per instructions — not a new one), addressing all 8 critiques. Key moves:"]}], "userModified": false, "replaceAll": false}
```

### [28] ASSISTANT · 2026-06-16 04:39:55 UTC

```
Review complete and written to `./.terminal_claude_agent_struct_out.json` (validated as well-formed).

## Summary

**Verdict: 6/10 (Weak Accept), confidence 4.** Soundness 3, Presentation 3, Contribution 3. Relation to prior iteration: **evolution**.

This iteration-7 revision is a strong, responsive one. I verified that **all four major critiques from the prior round are substantively addressed**:
- **Budget** — recomputed explicitly for isolated scoring (~14.4K calls, 7–15M tokens) with document-prefix prompt caching as the concrete mechanism keeping it under the $10 hard stop.
- **Populability** — the primary disconfirmation is now populability-gated, moved to the error-dense multi-hop kinship family, with `N_false_min` and an explicit `UNTESTABLE` (not "confirmed-by-conservatism") outcome.
- **Operational construct** — a shared (head, relation, tail) triple space mapping every system identically, and the **plain zero-label confidence-threshold comparator restored** as the load-bearing baseline.
- **Scope** — an explicit budget waterfall protecting the two anchors.

I grounded novelty in a live search: the closest 2026 work (arXiv 2606.00402, knockoff filtering) targets human-vs-machine **text detection** — a different task — so the core idea (FDR gate at the text-to-logic admission boundary) remains genuinely novel.

**Two residual majors** (now second-order, not blocking):
1. **rigor** — the *positive* diagonal-tracking confirmation may be underpowered under document-block bootstrap; `N_false_min` is sized for populability, not grid-wise CI tracking.
2. **methodology/significance** — absolute calibration is asserted only on toy-vocabulary CLUTRR and never directly measured on realistic Re-DocRED, with the transfer-bridge (S5) stranded in the leftover tier. Suggested a cheap fix: a conservatively-biased (gold-false-negative-inflated) upper-bound FDR curve on Re-DocRED.

Plus four minors (graded vs. binary exchangeability test, thin symbolic-reasoning/trace-graph deliverables vs. the stated ACL goal, awareness of the emerging knockoffs-for-LLM line, and lingering density). I credited the genuine presentation improvement (the requested threat table + claim-chain table landed), bumping presentation from 2→3. Project memory updated for pipeline continuity.
```

### [29] SYSTEM-USER prompt · 2026-06-16 04:39:58 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline.' is too long (at most 120 characters, got 130)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [30] ASSISTANT · 2026-06-16 04:40:06 UTC

```
The `relation_rationale` exceeds 120 characters. Let me shorten it.
```

### [31] TOOL CALL — Edit · 2026-06-16 04:40:06 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline."
NEW:   "relation_rationale": "Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic."
```

### [32] TOOL RESULT — Edit · 2026-06-16 04:40:06 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline.\"", "newString": "  \"relation_rationale\": \"Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic.\"", "originalFile": null, "structuredPatch": [{"oldStart": 81, "oldLines": 5, "newStart": 81, "newLines": 5, "lines": ["   \"score\": 6,", "   \"confidence\": 4,", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic, restored threshold baseline.\"", "+  \"relation_rationale\": \"Same two-anchor decoy-FDR frame; refines populability gate, shared eval construct, budget arithmetic.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [33] TOOL CALL — Bash · 2026-06-16 04:40:12 UTC

```
Validate JSON and relation_rationale length:
python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/iter_7/review_hypo/.terminal_claude_agent_struct_out.json')); r=d['relation_rationale']; print('VALID JSON; relation_rationale len =', len(r)); assert len(r)<=120, 'TOO LONG'; print('OK <=120')"
```

### [34] TOOL RESULT — Bash · 2026-06-16 04:40:12 UTC

```
{"stdout": "VALID JSON; relation_rationale len = 101\nOK <=120", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [35] ASSISTANT · 2026-06-16 04:40:15 UTC

```
Fixed. The `relation_rationale` is now 101 characters (under the 120 limit), and the JSON validates. The review is complete and written to `./.terminal_claude_agent_struct_out.json`.
```
