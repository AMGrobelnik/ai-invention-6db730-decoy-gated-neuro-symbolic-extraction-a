# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 05:34:02 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
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
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

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

<paper>
# Introduction

Operational pipelines that convert unstructured prose into a formal, computable representation---one a logic engine such as SWI-Prolog can execute---promise the best of two worlds: the broad coverage of an LLM as a semantic translator, and the verifiable, auditable inference of a symbolic reasoner. The recurring failure point of such pipelines is not parsing syntax but the *fuzzy-unification boundary*: when strict symbolic matching fails, an LLM must align a surface predicate to a schema relation and supply implicit background knowledge, and exactly at that interface hallucination re-enters and propagates into every deduction that consumes the admitted fact. The dangerous hallucinations are not random nonsense; they are *plausible, high-confidence false facts* that a downstream solver will treat as ground truth.

The problem is both practically important and technically hard. It is important because a single fabricated premise admitted into a knowledge base contaminates an unbounded set of multi-hop conclusions, and because the application domains that most need auditable reasoning---short legal documents, news, regulatory text---are precisely those where a silently wrong fact is most costly. It is hard because the standard defenses do not act where the damage occurs. Self-consistency and LLM-as-judge are heuristic and provide no quantitative control. Ontology-constraint filtering rejects only encoded violations and needs a rich trusted constraint set. The strongest uncertainty-quantification methods---conformal factuality [15], conformal selection with Benjamini-Hochberg [16], multiple-testing hallucination detection [18], coherent factuality over reasoning chains [17], and the newest online and feedback-driven variants [19]---all require a *labeled* calibration set and certify the *final answer or claim set*, not the *admission* of an intermediate fact or bridge into the symbolic layer.

Why has the admission boundary not been controlled before? Because the natural statistical tool for controlling false admissions among many candidate signals with no ground truth---the *false discovery rate* (FDR)---was developed in numeric feature selection and mass spectrometry, where a synthetic negative control exchangeable *by construction* is available. Genomics and proteomics solved an isomorphic label-poor problem---selecting true signals among overwhelming noise with a guaranteed FDR and no labels---via the knockoff filter [4, 5] and target-decoy competition, and learned the two ways the trick breaks: decoys that are *too unrealistic to fool* the scorer make the estimated FDR optimistic (cured by property-matched decoys [9]), and entrapment false-discovery-proportion (FDP) must be estimated with a valid upper bound built *independently* of the decoys [6]. No prior work imports this machinery to the LLM neural-to-symbolic boundary, label-free.

This paper does so. We propose *decoy-gated extraction*: before any LLM-proposed Prolog fact or bridge enters the knowledge base, it must out-score a *plausibility-matched* synthetic decoy---a document-conditioned counterfactual that the model finds plausible but the document does not entail---in a knockoff+ competition that admits the most permissive cutoff whose estimated corpus-aggregate FDR is at most a target $\alpha$, using zero operation labels. The competition statistic for candidate $i$ is $W_i = \mathrm{score}(\mathrm{real}_i) - \mathrm{score}(\mathrm{decoy}_i)$; knockoff+ thresholding scans cutoffs and admits $\{i : W_i \ge T\}$ at the most permissive $T$ whose estimated $\widehat{\mathrm{FDR}} = (1 + \#\{W_i \le -T\}) / \max(1, \#\{W_i \ge T\}) \le \alpha$ [4]. Validity rests on the *null sign-flip property* (for genuinely-false candidates the sign of $W_i$ is a fair coin conditional on $|W_i|$); because LLM decoys carry no construction-level proof of this property, we treat the gate as an *empirically validated calibration* rather than a theorem, test the property *in the tail* where admissions occur, and protect it against the two LLM-specific dependence channels that break it.

[FIGURE:fig1]

A label-free FDR knob is worth building only if it is *both calibrated and useful*, and the two claims are best proven on different data. We therefore adopt a two-anchor design with a clean division of labor. CLUTRR [1]---free, deterministic, with crisp templated gold over a closed kinship vocabulary---hosts the *calibration-validity* claim (does realized FDR track target $\alpha$?) and a single pre-registered primary disconfirmation. Re-DocRED [2]---human-annotated Wikipedia prose with 96 open relation types and document-level multi-hop structure---hosts the *operational-usefulness* claim (atomic-fact precision and hallucinated-conclusion rate versus baselines at matched recall) and a document-level predictive account of *when* the calibration holds. CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful; the two are never conflated.

**Scope and honesty.** The contribution of this iteration is the method, the prepared and validated evaluation infrastructure, and a falsifiable pre-registered protocol---not yet the realized empirical diagonal. We are explicit about this throughout: the datasets are built, the structural floors and budget are analyzed and shown feasible, and the protocol is registered with a single disconfirmation that can falsify the headline. We do not report fabricated FDR or precision numbers; the empirical run is the registered next step that the prepared anchors are sized to power.

**Summary of contributions.**

- We formulate the *text-to-logic admission boundary* as an FDR-control problem and introduce *decoy-gated extraction*, to our knowledge the first label-free FDR knob at the neural-to-symbolic interface, built from knockoff+ thresholding, plausibility-matched counterfactual decoys, and independent entrapment corroboration (Sections 3--4).
- We identify the two channels by which LLM scoring breaks the knockoff null sign-flip property---within-document score correlation and batched-scoring contrast effects---and neutralize them with a document-block bootstrap and isolated, provenance-blinded scoring, with an *isolated-versus-batched* check that doubles as a discriminator between a scoring artifact and genuine decoy non-exchangeability (Section 4.4).
- We design an auditable neuro-symbolic pipeline whose Prolog proof trace-graphs carry, at every leaf, a decoy-competition certificate and an entrapment certificate alongside the provenance span (Section 4.6).
- We deliver two prepared, schema-validated evaluation anchors---a 190-document crisp-gold CLUTRR calibration set and a 236-document Re-DocRED operational set---with a shared triple schema enabling an apples-to-apples matched-recall comparison against a plain confidence threshold, chain-of-thought, retrieval-augmented generation, and labeled conformal factuality (Sections 5--6).
- We give a structural feasibility analysis: the demonstrable-$\alpha$ grid tied to the $1/k$ minimum-estimable-FDR floor, and a budget arithmetic projecting under three US dollars of LLM cost on commodity CPU, against a hard ten-dollar cap (Sections 4.3, 6.5).
- We pre-register a falsifiable protocol---a single primary disconfirmation gated on populability, a six-row claim chain, and a threat table---so that the eventual empirical outcome is interpretable whether it confirms, disconfirms, or is declared untestable (Section 6).

# Related Work

**Label-free hallucination scoring.** Zero-resource detectors produce per-claim hallucination scores from sampling consistency (SelfCheckGPT [13]) or distractor-normalized verbalized confidence (DINCO [12]); FactSelfCheck [14] operates natively at the fact level over $(h, r, t)$ triples. These methods yield a *score*, not an admission threshold, and offer no exchangeability or competition argument. In our framework they are *candidate elicitations* feeding the gate, not the gate itself; our Phase-0 pilot selects among them by tail discrimination. Verbalized confidence is known to be overconfident in the upper tail [10], and token log-probability calibration degrades under reinforcement learning from human feedback [11]---which is exactly why we test elicitations on tail discrimination rather than average calibration.

**Labeled uncertainty quantification for LLMs.** Conformal factuality [15] removes claims until a factuality level is met, using a labeled calibration set, and certifies the emitted answer; coherent factuality [17] extends this to reasoning chains; conformal selection [16] and online/feedback-driven multiple testing [18, 19] control FDR over candidate outputs but require labeled calibration outcomes. All certify *outputs* and all are *labeled*. Our contribution is orthogonal and complementary: a *label-free* control at the *admission* boundary. Mohri-Hashimoto conformal factuality [15] is our load-bearing *labeled reference baseline*; we report its finite-sample guarantee side by side with our empirical calibration, and charge any baseline's calibration labels symmetrically against our zero labels.

**FDR control by competition.** The knockoff filter [4] and Model-X knockoffs [5] select signals with guaranteed FDR by competing each real candidate against a synthetic negative control exchangeable by construction, relying on the null sign-flip property; the knockoff+ threshold controls FDR exactly via the conservative $+1$ offset [4], which Rajchert and Keich prove is in general necessary [7]. Ebadi et al. give tighter upper prediction bounds on the FDP [8]. In proteomics, entrapment estimation provides an independent FDP bound, with the valid combined estimator and the flawed naive estimator characterized by Wen et al. [6]; property-matched decoy generation (DeepCoy [9]) shows decoys must reproduce the true-positive score distribution. We adapt all three to the LLM boundary, where exchangeability is *not* provable, and therefore add tail-conditioned diagnostics, a document-block bootstrap for within-document dependence [28], and a model of where the property holds.

**Text-to-logic neuro-symbolic reasoning.** LINC [20] and Logic-LM [21] semantic-parse premises into first-order logic or symbolic programs executed by a solver, with majority voting or solver-error self-refinement; LLM-ASP [23] parses CLUTRR into reusable answer-set modules. None exercises principled control over *which* extracted premises are admitted: a syntactically valid but fabricated premise is never challenged, voting merely smooths variance, and refinement fixes only solver and syntax errors. Standard neural baselines---chain-of-thought prompting [22] and retrieval-augmented generation [26]---have no admission boundary at all. Logical-reasoning benchmarks such as RuleTaker [24], ProofWriter [25], and CLUTRR [1] supply controlled reasoning targets; our calibration anchor is CLUTRR for its crisp templated gold, and our operational anchor is Re-DocRED [2], the false-negative-corrected re-annotation of DocRED [3].

# Preliminaries

We control the false admission of two candidate kinds. A *fact* is a ground typed atom (for example `rel_child(e_alice, e_bob)` with a side type table), and a *bridge* is a fuzzy-unification rule---a kinship composition rule for CLUTRR, or a surface-form-to-schema relation alignment for Re-DocRED. Bridges are first-class admission candidates with their own decoy, score, and gate. Each candidate $i$ receives a label-free score $Z_i$ from an isolated elicitation and a matched decoy score $\tilde{Z}_i$; the *competition statistic* is $W_i = (Z_i \vee \tilde{Z}_i)\,[2 \cdot \mathbf{1}(Z_i > \tilde{Z}_i) - 1]$, which reduces to the sign-antisymmetric difference of real and decoy scores [4, 5]. A large positive $W_i$ is evidence that the candidate is a true signal; the sign of $W_i$ is the win/lose of real versus decoy. The target is the corpus-aggregate FDR---the expected fraction of admitted candidates that are document-non-entailed---held at or below a user-chosen $\alpha$, separately for facts and bridges and per anchor, with all confidence intervals computed by resampling whole documents [28]. We use $a \vee b = \max(a, b)$ throughout.

# Method

The pipeline has six stages: over-generating extraction, plausibility-matched decoy generation, isolated provenance-blinded scoring, the knockoff+ FDR gate, independent entrapment corroboration, and symbolic reasoning with auditable trace-graphs. We describe each as the story of the admitted artifact, not of how we arrived at the design. The full implementation specification---verbatim prompt templates, on-disk formats, and library APIs---is provided in the supporting research artifacts [ARTIFACT:art_SLUbUUr6Ul98][ARTIFACT:art_K6AE23HoGqe6].

## Extraction with deliberate over-generation

A cheap LLM proposes typed first-order facts and bridges from the document in a LINC/Logic-LM style, with argument types grounded in a commodity upper-ontology slice. Following the user requirement of an OpenCyc-style taxonomic grounding, we use an offline WordNet hypernym lookup that maps each argument head noun into the coarse vocabulary $\{$PER, LOC, ORG, TIME, NUM, MISC$\}$ via anchor synsets (`person.n.01` to PER, `location.n.01` to LOC, `organization.n.01` to ORG, and so on), reusing Re-DocRED's gold mention types when present and typing all CLUTRR arguments to PER [ARTIFACT:art_K6AE23HoGqe6]. Typing is used *only* to constrain decoy generation and entity linking, never to filter. The extractor deliberately *over-generates*---temperature 0.7, three samples unioned, capped at twenty candidates per document---so that the candidate pool is dense in genuine false positives, which is a precondition for a non-vacuous calibration diagonal: a diagonal can only track $\alpha$ if a meaningful fraction of admitted reals are genuinely false.

## Plausibility-matched counterfactual decoys

The load-bearing design choice is the decoy family. The proteomics lesson is that decoys that are *too easy* let the scorer separate on artifacts and make the estimated FDR optimistic; DeepCoy quantifies the cost of unmatched decoys and the gain from property-matched ones, improving deviation-from-optimal-embedding by 81% (0.166 to 0.032 on DUD-E) and 66% (0.109 to 0.038 on DEKOIS 2.0) with no added false-negative risk [9]. Translated to text, a decoy must reproduce the score distribution of genuine *plausible* hallucinations---same entity types, surface form, and specificity---so that the only feature distinguishing it from a real-but-false fact is document non-entailment. Our primary family is the *document-conditioned counterfactual*: given the document and the relation/type schema, the model produces a maximally plausible fact or bridge that is *not* stated or entailed by the text, matching the surface form and specificity of the document's real facts. Every decoy passes an independent, isolated non-entailment check (an accidentally entailed decoy is actually true and would bias the FDR conservatively); the contamination rate is logged and a sensitivity analysis sweeps the rejection threshold [ARTIFACT:art_SLUbUUr6Ul98]. As a deliberately retained negative control we also generate *random type-matched swaps*, which are predicted to read anti-conservative precisely because they are too easy---validating the diagnostic.

## Isolated, provenance-blinded scoring

Each candidate, whether real, decoy, or entrapment, is scored in its *own* prompt with source identity masked and presentation order randomized, rather than scoring many candidates jointly. Isolation removes the within-batch contrast and ranking effects that would let the model implicitly detect the fabricated item and depress decoy scores---an anti-conservative failure of the second kind below. Isolated scoring is the default for 100% of the confirmatory set; the headroom is bought not by batching but by *document-prefix prompt caching*: the roughly sixty scoring calls that share one document context re-use a cached prefix at a fraction of the input cost. The per-candidate score is produced by a pilot-selected elicitation. Because verbalized confidence is overconfident in the upper tail [10] and log-probability calibration degrades under alignment [11], the elicitation is chosen on *tail* discrimination, not average calibration: a Phase-0 pilot ranks verbalized confidence (a floor baseline), a distractor-normalized DINCO-style score [12], a sampling-consistency score (SelfCheckGPT / FactSelfCheck [13, 14]), and---if the model exposes log-probabilities---a yes/no-token score, selecting the one whose area under the curve restricted to the admission tail exceeds 0.5 with a confidence interval [ARTIFACT:art_SLUbUUr6Ul98].

## The knockoff+ FDR gate and the structural $1/k$ floor

Given the competition statistics, the gate admits $\{i : W_i \ge T\}$ at the smallest (most permissive) cutoff $T$ for which $\widehat{\mathrm{FDR}}(T) = (1 + \#\{W_i \le -T\}) / (\#\{W_i \ge T\} \vee 1) \le \alpha$, which is the knockoff+ threshold controlling the FDR exactly [4]. The $+1$ in the numerator is conservative and, by the analysis of Rajchert and Keich, generally necessary [7]; we keep it for the headline certificate. Its conservativeness has a precise structural consequence we exploit for honesty: with $k$ admissions the smallest attainable FDR estimate is $1/k$, so certifying $\widehat{\mathrm{FDR}} \le \alpha$ requires $k \ge \lceil 1/\alpha \rceil$ admissions. The demonstrable-$\alpha$ grid is therefore tied to a known admission floor: $\alpha \in \{0.05, 0.10, 0.20, 0.30, 0.50\}$ maps to admission floors $\{20, 10, 5, 4, 2\}$ [ARTIFACT:art_SLUbUUr6Ul98]. An $\alpha$ below the floor reachable by a given anchor is structurally undemonstrable regardless of model quality---a fact we report rather than paper over.

[FIGURE:fig4]

## Robustifying the null sign-flip property

[FIGURE:fig2]

Knockoff+ validity rests on a single condition: among genuinely-false candidates, the sign of $W_i$ behaves like an independent fair coin conditional on $|W_i|$ [4]. For Gaussian knockoffs the condition is provable; for LLM decoys it is not, so the gate is an empirically validated calibration and we test the condition *in the tail*. Two LLM-specific channels can break it anti-conservatively.

The first is *within-document score correlation*: candidates from one document share context, entities, and genre, so their null $W$ signs are dependent, and pooling them as independent understates variance and the floor. The remedy is the *document-block bootstrap*: all FDP/FDR confidence intervals are computed by resampling whole documents (blocks) with replacement and re-running the entire gate on each resample, with at least 2000 resamples, following the cluster-bootstrap remedy for within-cluster dependence [28]. The resulting percentile interval is the confidence interval used by the primary disconfirmation.

The second is the *batched-scoring contrast effect*: if candidates are co-presented, the model can implicitly detect the odd fabricated item and depress its score, making the FDP optimistically low. The remedy is isolated, provenance-blinded, order-randomized scoring as the default. Crucially, a pre-registered *isolated-versus-batched* check on a labeled slice doubles as a discriminator: if isolation restores the calibration diagonal while batching is anti-conservative, the anti-conservatism was a scoring artifact; if it persists under isolation, the decoys are genuinely too easy and the decoy family must be fixed. Two measurement-only tail diagnostics complete the picture and are never consumed by the gate: the tail-conditioned win-rate of matched (false-real, decoy) pairs above the operative cutoff should be approximately 0.5, and a one-sided two-sample test (Kolmogorov-Smirnov or tail-restricted Mann-Whitney) on real-false versus decoy scores restricted to the admission region should not find decoy scores stochastically smaller.

## Independent entrapment corroboration

Decoy competition decides admission; *entrapment* provides an independent upper bound on the realized FDP, built by a mechanism *distinct* from the decoys (in-genre cross-document swaps, numeric or temporal perturbation, explicit contradiction) so the two FDR signals are independent corroborations against gold. We use the valid combined estimator $\widehat{\mathrm{FDP}} = N_E(1 + 1/r)/(N_T + N_E)$ as the default certificate and the tighter paired estimator at $r = 1$ when one-to-one pairing is available, where $N_T$ and $N_E$ are admitted target and entrapment counts and $r$ is the entrapment-to-target ratio; we never use the naive sample estimator, which Wen et al. prove biased [6]. The ratio $r$ propagates into the point estimate, the variance, and the achievable-$\alpha$ floor, and is reported. Entrapment carries its own tail-difficulty diagnostic so that an entrapment set that is too easy cannot silently inflate confidence.

## Symbolic reasoning and auditable trace-graphs

Admitted facts and bridges populate an SWI-Prolog knowledge base (via the bundled `janus-swi` bridge, with `pyswip` and a `swipl` subprocess as fallbacks) for multi-hop deduction [ARTIFACT:art_K6AE23HoGqe6]. A vanilla `solve/2` meta-interpreter captures the backward-chaining proof as a *trace-graph* whose nodes are sub-goals and derived facts and whose edges are labeled rule applications. Every leaf resolves against a side table that returns a certificate term: the provenance span, the decoy-competition certificate $(W_i, T, \alpha)$, and the entrapment certificate $(\widehat{\mathrm{FDP}}, r)$. The trace-graph is serialized to JSON for machine audit and to Graphviz DOT for human audit, satisfying the requirement that every conclusion expose the logical path taken and the statistical license of each premise it rests on. Beyond the two quantitative anchors, a small illustrative corpus of roughly fifteen short legal, news, and story documents exercises the trace-graph end to end on the genres the application targets; the corpus is explicitly non-confirmatory and used only to demonstrate the auditable output, never to assert calibration.

# Evaluation Design and Pre-Registered Protocol

The evaluation is split so that calibration and usefulness are proven on the data each suits, and it is pre-registered so that the eventual outcome is interpretable.

[FIGURE:fig3]

## Two anchors with a clean division of labor

CLUTRR [1] is rule-based and templated, so its kinship gold is exact---the property that lets it host the realized-FDR-versus-$\alpha$ *diagonal* and the single primary disconfirmation. Re-DocRED [2] is human-annotated, open-vocabulary, and document-level, so it hosts the *operational* claim, the genuine schema-alignment bridge test, and the document-level predictive account; because Re-DocRED retains residual false negatives, it licenses only *relative* operational comparisons under shared gold, never an absolute diagonal. CLUTRR proves the knob is calibrated; Re-DocRED proves it is useful.

## Prepared datasets

[FIGURE:fig5]

The CLUTRR calibration anchor comprises 190 stories (one story per example) drawn from the pooled test splits of two CLUTRR configurations, of which 1345 of 2191 pooled rows qualified as canonical simple-path chains, stratified over chain length $k = 2$ to $10$ and oversampling long chains: 150 confirmatory and 40 disjoint pilot examples, with the confirmatory $k$-distribution $\{k2{:}12, k3{:}15, k4{:}20, k5{:}20, k6{:}20, k7{:}18, k8{:}18, k9{:}15, k10{:}12\}$ [ARTIFACT:art_XZyKy6QuwxrO]. All gold is derived 100% from CLUTRR's own structured `proof_state` fields---leaf triples give the $k$ directly-stated *atomic* facts and dictionary keys give the $k-1$ *multi-hop* inferred relations---with no homegrown rule reimplementation, over a 20-relation kinship vocabulary. The atomic family is typically too clean to populate the diagonal; the multi-hop inferred-kinship family, where extraction errors are dense, is the *populable* family on which the primary disconfirmation is pre-registered.

The Re-DocRED operational anchor comprises 236 Wikipedia documents (one per example) drawn from 4053 pooled documents under the eligibility filter $80 \le \text{words} \le 400$, at least four entities, and at least five triples: 152 confirmatory, 36 pilot, and 48 reserve, exactly balanced across four dominant-entity-type folds (PER, ORG, LOC, MISC) at 38/9/12 each for leave-one-cluster-out cross-validation [ARTIFACT:art_Jcudmkugg1qT]. Each document carries the full annotated entity inventory with character spans, gold $(head, relation, tail)$ triples over 96 Wikidata relation types and 6 entity types with evidence sentences, and 17 per-document features (triple density ranges from 0.38 to 14.75 across the corpus) that supply the cross-document variance the document-level predictive model needs. Both datasets are schema-validated and regenerable deterministically on pure CPU from cached raw data under a fixed seed.

## Shared operational construct and matched-recall comparison

On Re-DocRED, every system targets the *same* object: $(head\text{-}entity, relation, tail\text{-}entity)$ triples over the document's annotated entities, scored against human gold by the official $(\text{title}, r, h_{\text{idx}}, t_{\text{idx}})$ matching metric [2, 3]. A single fixed claim-decomposition and relation-alignment step maps every system's raw output into this triple space identically: a sentence-embedding shortlist of the top-eight relation codes followed by a temperature-0 LLM pick among the 96 codes or `NO_RELATION`, with a three-tier entity-linking procedure (exact, alias/substring, embedding floor) [ARTIFACT:art_K6AE23HoGqe6]. Recall is matched by sweeping each system's own score to a common operating point; precision and the hallucinated-conclusion rate (the fraction of multi-hop derived conclusions whose triple is not entailed by gold) are compared there with document-block-bootstrap intervals. The comparators are the *plain confidence-threshold gate* (the primary zero-label foil, identical elicitation, no decoy or competition), chain-of-thought [22], retrieval-augmented generation [26], and labeled Mohri-Hashimoto conformal factuality [15] as the labeled reference. The wedge is isolated as decoy-gating versus plain thresholding under identical zero labels: if decoy-gating does not beat plain thresholding at matched recall, the operational claim collapses to "thresholding is enough" and is disconfirmed.

## Pre-registered claim chain and primary disconfirmation

[FIGURE:fig6]

The protocol is a six-row claim chain, each row independently testable so that a break is localized and reported rather than hidden. S0 (score separation) requires the selected elicitation to separate entailed from non-entailed content in the upper tail with isolated-batched agreement. S1 (decoy signature) requires counterfactual decoys to reach tail-conditioned win-rate near 0.5 and pass the upper-tail two-sample test while random swaps read anti-conservative. S2 (calibration validity, CLUTRR) requires realized FDR to track $\alpha$ within tolerance $\tau = 0.05$ above the $1/k$ floor on the populable family, with a document-block-bootstrap interval. S3 (entrapment corroboration) requires the combined-estimator bound to agree with the decoy FDR and gold. S4 (operational wedge, Re-DocRED) requires decoy-gating to beat plain thresholding at matched recall and stay competitive with labeled conformal. S5 (document-level predictive account) predicts the per-document tail-exchangeability gap from document and score features under leave-one-cluster-out and leave-one-document-out cross-validation, reported as *predictive* only if validated out-of-sample on at least a pre-registered minimum of held-out units and as *descriptive* otherwise. S6 (predictable propagation) checks that tightening $\alpha$ lowers the multi-hop hallucinated-conclusion rate in direction and rough magnitude.

The single primary disconfirmation is S4/S5-independent and populability-gated. On the populable CLUTRR family under isolated provenance-blinded scoring at the operative $\alpha^{*}$, the central control claim is *disconfirmed* if realized corpus-aggregate FDR against crisp gold exceeds $\alpha^{*}$ by more than $\tau$ *and* the document-block-bootstrap interval lies entirely on the anti-conservative side. The disconfirmation fires only if Phase-0 first shows the family is populable---yielding at least $N_{\text{false\_min}} = 40$ genuine false admissions pooled at $\alpha^{*}$, enriched if needed by extractor over-generation and harder long-chain splits. If no family reaches the threshold even after enrichment, the diagonal is declared *untestable at this difficulty* and reported as a precondition outcome---never as "confirmed by conservatism." This pre-registration is what converts a likely-partial result into an interpretable one: an uninterpretable null, in which control neither clearly holds nor clearly fails because the tail or the diagonal is underpowered, is the specific failure the Phase-0 power analysis is designed to prevent.

## Budget waterfall and feasibility

Spending follows a strict priority order so the headline cannot be starved by secondary exploration: (i) the Phase-0 pilot, which gates everything; (ii) fully powering the CLUTRR calibration diagonal; (iii) fully powering the Re-DocRED operational wedge; and (iv), only with leftover budget and only after (ii) and (iii) clear their power thresholds, the S5 predictive model, S6 propagation, FDP-bound tightening, and exploratory rule gating. The confirmatory scoring workload is roughly 240 documents times about 20 candidates times 3 item-types (real, decoy, entrapment at $r = 1$), about 14.4K isolated scoring calls, plus about 0.7K generation calls and the pilot, at roughly 450 input and 30 output tokens per call, about 7 to 15 million tokens depending on candidate count. At a model priced under 0.30 US dollars per million tokens with document-prefix caching, the projected cost is approximately one to three US dollars, with cumulative cost logged after every call and a hard stop at ten dollars [ARTIFACT:art_SLUbUUr6Ul98]. The entire pipeline runs on commodity CPU.

# Deliverables and Feasibility Analysis

We report the concrete, verifiable outputs this iteration produces; we do not report empirical FDR or precision results, which are the registered next step.

**Two validated evaluation anchors.** The CLUTRR anchor delivers 190 schema-validated examples with a 190-of-190 independent integrity pass, exact crisp gold derived solely from CLUTRR structured fields, and a stratified $k$-distribution that guarantees per-stratum supply above the admission floors of the demonstrable-$\alpha$ grid [ARTIFACT:art_XZyKy6QuwxrO]. The Re-DocRED anchor delivers 236 schema-validated documents with full entity inventories, gold triples over 96 relations with evidence spans, four balanced cross-validation folds, and 17 per-document features whose spread (triple density 0.38 to 14.75) confirms the cross-document variance that the predictive model S5 requires and that CLUTRR's near-homogeneous documents lack [ARTIFACT:art_Jcudmkugg1qT]. Both regenerate deterministically on CPU under seed 20240617.

**A structural guarantee of falsifiability.** The $1/k$ floor analysis ties each demonstrable $\alpha$ to a known admission count, so the protocol cannot mistake structural unreachability for control: the grid $\{0.05, 0.10, 0.20, 0.30, 0.50\}$ is admissible only where admissions reach $\{20, 10, 5, 4, 2\}$ respectively, and the populability gate ($N_{\text{false\_min}} = 40$) ensures the diagonal is asserted only where genuine false admissions exist [ARTIFACT:art_SLUbUUr6Ul98]. The primary disconfirmation, the threat table, and the claim chain together make every possible outcome---confirmed, disconfirmed, or untestable---reportable as a definite result.

**A feasibility envelope.** The budget arithmetic places the confirmatory run at approximately one to three US dollars against a ten-dollar hard cap, with isolated scoring affordable for 100% of the confirmatory set because document-prefix caching, not batching, buys the headroom---preserving the isolated-versus-batched discriminator that batching would destroy [ARTIFACT:art_SLUbUUr6Ul98]. Two runtime preconditions are flagged for the empirical step: confirming the chosen model returns non-null log-probabilities (else the logprob elicitation is dropped and DINCO, verbalized, and sampling-consistency carry the pilot), and confirming cached tokens are non-zero so the projection holds.

# Discussion

**What the design buys, and what it cannot promise.** Decoy-gated extraction converts an uncontrolled hallucination channel---the fuzzy-unification boundary---into a tunable one, with a per-leaf certificate and no operation labels. Because LLM decoys carry no theoretical guarantee of the null sign-flip property, the most probable empirical outcome is *partial* control rather than an exact diagonal, and we have designed for that honestly: the document-level predictive account S5 is intended to convert a likely-partial result into a generalizable mechanism-level insight about *when* the calibration holds, and the isolated-versus-batched discriminator localizes any anti-conservatism to either a scoring artifact or a decoy-family defect. Even coarse control---at $\alpha$ near 0.1---would be the first label-free FDR knob at this interface.

**Limitations.** First, and most important, this paper presents a validated design and prepared infrastructure, not a realized empirical diagonal; the calibration and operational claims are pre-registered, not demonstrated. Second, the validity condition is engineered and tested, not proven, so a persistent anti-conservatism under isolated scoring would falsify the headline and is a real possibility we have made falsifiable rather than hidden. Third, the calibration diagonal is contingent on populability: if neither CLUTRR family reaches the false-admission threshold even after enrichment, the diagonal is untestable at this difficulty, an honest precondition outcome rather than a success. Fourth, Re-DocRED's residual false negatives confine it to relative comparisons, which is why crisp-gold CLUTRR carries the absolute calibration claim. Fifth, the demonstrable-$\alpha$ grid is floored by the conservative $+1$; tighter FDP bounds [8] are exploratory and carry no finite-sample guarantee here.

**Connection to the target application.** The pipeline ingests short professionally written documents, translates them to first-order logic, executes multi-hop deductions in Prolog, and emits auditable trace-graphs on commodity hardware---the operational profile the task demands. The fuzzy-unification bridges are precisely the LLM-supplied predicate alignments and background-knowledge steps the application needs, and the FDR knob is the quantified hallucination-reduction control that raw LLM generation lacks.

# Conclusion

We have formulated the text-to-logic admission boundary as a label-free FDR-control problem and introduced decoy-gated extraction, which forces every LLM-proposed fact and fuzzy-unification bridge to out-score a plausibility-matched counterfactual decoy in a knockoff+ competition before entering a Prolog knowledge base, with independent entrapment corroboration and per-leaf audit certificates. We transplanted three ideas from genomics and proteomics---knockoff+ thresholding, property-matched decoys, and valid entrapment estimation---and robustified the null sign-flip property against the two channels by which LLM scoring breaks it, using a document-block bootstrap and isolated provenance-blinded scoring. We delivered two prepared and validated evaluation anchors, a structural analysis tying the demonstrable-$\alpha$ grid to a known admission floor, a feasibility envelope under three US dollars on commodity CPU, and a pre-registered protocol whose single primary disconfirmation makes the headline falsifiable. Future work, in registered priority order, is to (1) run the Phase-0 pilot and select the tail-discriminating elicitation; (2) measure the CLUTRR calibration diagonal on the populable multi-hop family with document-block-bootstrap intervals; (3) measure the Re-DocRED operational wedge against the plain-threshold foil at matched recall; and (4), budget permitting, fit the document-level predictive model of when the calibration holds.

# References

[1] K. Sinha, S. Sodhani, J. Dong, J. Pineau, and W. L. Hamilton. CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text. In *EMNLP*, 2019.

[2] Q. Tan, L. Xu, L. Bing, H. T. Ng, and S. M. Aljunied. Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction. In *EMNLP*, 2022.

[3] Y. Yao, D. Ye, P. Li, X. Han, Y. Lin, Z. Liu, Z. Liu, L. Huang, J. Zhou, and M. Sun. DocRED: A Large-Scale Document-Level Relation Extraction Dataset. In *ACL*, 2019.

[4] R. F. Barber and E. J. Candès. Controlling the False Discovery Rate via Knockoffs. *Annals of Statistics*, 43(5):2055--2085, 2015.

[5] E. Candès, Y. Fan, L. Janson, and J. Lv. Panning for Gold: Model-X Knockoffs for High-Dimensional Controlled Variable Selection. *Journal of the Royal Statistical Society: Series B*, 2018.

[6] B. Wen, J. Freestone, M. Riffle, M. J. MacCoss, W. S. Noble, and U. Keich. Assessment of False Discovery Rate Control in Tandem Mass Spectrometry Analysis Using Entrapment. *Nature Methods*, 22:1454--1463, 2025.

[7] A. Rajchert and U. Keich. Controlling the False Discovery Rate via Competition: Is the +1 Needed? *Statistics & Probability Letters*, 2022.

[8] A. Ebadi, D. Luo, J. Freestone, W. S. Noble, and U. Keich. Bounding the FDP in Competition-Based Control of the FDR. *arXiv:2302.11837*, 2023.

[9] F. Imrie, A. R. Bradley, and C. M. Deane. Generating Property-Matched Decoy Molecules Using Deep Learning. *Bioinformatics*, 37(15):2134--2141, 2021.

[10] M. Xiong, Z. Hu, X. Lu, Y. Li, J. Fu, J. He, and B. Hooi. Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. In *ICLR*, 2024.

[11] K. Tian, E. Mitchell, A. Zhou, A. Sharma, R. Rafailov, H. Yao, C. Finn, and C. D. Manning. Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback. In *EMNLP*, 2023.

[12] V. Wang and E. Stengel-Eskin. Calibrating Verbalized Confidence with Self-Generated Distractors (DINCO). *arXiv:2509.25532*, 2025.

[13] P. Manakul, A. Liusie, and M. J. F. Gales. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. In *EMNLP*, 2023.

[14] A. Sawczyn, J. Binkowski, D. Janiak, et al. FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs. In *Findings of EACL*, 2025.

[15] C. Mohri and T. Hashimoto. Language Models with Conformal Factuality Guarantees. In *ICML*, 2024.

[16] Y. Jin and E. J. Candès. Selection by Prediction with Conformal p-values. *Journal of Machine Learning Research*, 2023.

[17] M. Rubin-Toles, M. Gambhir, K. Ramji, et al. Conformal Language Model Reasoning with Coherent Factuality. In *ICLR*, 2025.

[18] J. Li, A. Magesh, and V. V. Veeravalli. Principled Detection of Hallucinations in Large Language Models via Multiple Testing. *arXiv:2508.18473*, 2025.

[19] L. Lu, Y. Huo, H. Ren, Z. Wang, and J. Zou. Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection. *arXiv:2509.03297*, 2025.

[20] T. X. Olausson, A. Gu, B. Lipkin, C. E. Zhang, A. Solar-Lezama, J. B. Tenenbaum, and R. Levy. LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. In *EMNLP*, 2023.

[21] L. Pan, A. Albalak, X. Wang, and W. Y. Wang. Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. In *Findings of EMNLP*, 2023.

[22] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In *NeurIPS*, 2022.

[23] Z. Yang, A. Ishay, and J. Lee. Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text. In *Findings of ACL*, 2023.

[24] P. Clark, O. Tafjord, and K. Richardson. Transformers as Soft Reasoners over Language. In *IJCAI*, 2020.

[25] O. Tafjord, B. Dalvi, and P. Clark. ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language. In *Findings of ACL*, 2021.

[26] P. Lewis, E. Perez, A. Piktus, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In *NeurIPS*, 2020.

[27] N. Reimers and I. Gurevych. Sentence-BERT: Sentence Embeddings Using Siamese BERT-Networks. In *EMNLP*, 2019.

[28] A. C. Cameron, J. B. Gelbach, and D. L. Miller. Bootstrap-Based Improvements for Inference with Clustered Errors. *Review of Economics and Statistics*, 90(3):414--427, 2008.
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_XZyKy6QuwxrO
type: dataset
title: 'CLUTRR Crisp-Gold Calibration Anchor: Atomic + Multi-Hop Kinship Triples'
summary: |-
  Standardized, deterministic CLUTRR-derived dataset that serves as the CRISP-GOLD calibration anchor for the neuro-symbolic text-to-logic hallucination-control experiment. Source: CLUTRR v1 (Sinha et al., EMNLP 2019, arXiv:1908.06177), pooled TEST splits of configs gen_train234_test2to10 (1048 rows) and gen_train23_test2to10 (1146 rows), fetched as raw CSVs from the kliang5/CLUTRR_huggingface_dataset GitHub mirror and staged in temp/datasets/. CLUTRR is rule-based/templated, so its kinship gold is exact (no annotation noise) — exactly the property needed to host the realized-FDR-vs-alpha calibration diagonal.

  SCALE & SHAPE: ONE dataset group 'CLUTRR-v1-CrispGold-CalibrationAnchor' with 190 examples (row == one CLUTRR story). 150 confirmatory + 40 disjoint pilot (metadata_is_pilot). Stratified over chain length k=2..10 oversampling long chains (k>=4): confirmatory k-dist {k2:12,k3:15,k4:20,k5:20,k6:20,k7:18,k8:18,k9:15,k10:12}; pilot {k2:5,k3:5,k4:5,k5:5,k6:5,k7:5,k8:5,k9:3,k10:2}. Seed 20240617; selected ids recorded in top-level metadata for reproducibility.

  SCHEMA (aii-json exp_sel_data_out; validated, plus an independent 190/190 integrity pass): each example has STRING input and output (JSON-serialized; parse with json.loads) plus flat metadata_* fields. input keys: doc_id, document_text (clean prose, [Name] brackets stripped, native length never padded), document_text_bracketed (raw for entity-span provenance), entities[{name,gender,type='person',node_index}], query{head,tail}. output keys: atomic_facts[{head,relation,tail}] = the k directly-stated chain edges (the 'too clean' atomic family); multi_hop_facts[{head,relation,tail,derived_from,path_len,is_query_target}] = the k-1 proof_state-derived inferred relations incl. the query target (the error-dense 'populable' family the primary disconfirmation is pre-registered on); multi_hop_query_target{head,relation,tail}; kinship_edge_graph{nodes[{index,name,gender}],edges[{src,dst,relation}]}. All facts use the shared {head,relation,tail} triple structure with kinship relation strings (a Re-DocRED anchor could reuse the same structure with Wikidata relations).

  PER-EXAMPLE METADATA: metadata_fold ('k2'..'k10'), metadata_chain_length_k, metadata_difficulty_split ('short' k<=3 / 'long' k>=4), metadata_f_comb, metadata_task_name, metadata_source_config, metadata_source_split, metadata_clutrr_id, metadata_is_pilot, metadata_n_atomic_facts, metadata_n_multi_hop_facts, metadata_document_char_length, metadata_proof_state_raw, metadata_noisy_story, metadata_atomic_crosscheck ('match'), metadata_namemap_method ('genders_order'), metadata_genders_order_valid, metadata_relation_vocab_version ('clutrr_kinship'). Top-level metadata also carries relation_vocabulary (20 observed kinship relations), full k-distributions, and selected confirmatory/pilot id lists.

  CRISPNESS GUARANTEE: all gold is derived 100% from CLUTRR's own structured fields (proof_state leaf triples = atomic; proof_state dict keys = multi-hop) with NO homegrown rule reimplementation. Restricted to canonical simple-path chains (distinct entities==k+1, distinct edges, |atomic|==k, |multi_hop|==k-1, exactly one proof root equal to the query target, genders-order node->name map reproduces the proof_state atomic leaves); 1345 of 2191 pooled rows qualified, giving ample per-stratum supply.

  SELECTION: CLUTRR is THE chosen dataset (target_num_datasets=1). Secondary candidate ProofWriter (tasksource/proofwriter, kept in temp/datasets/ as backup) was excluded — it provides T/F/Unknown answers over rule/fact theories, not the kinship atomic+multi-hop triple gold this experiment is registered on. OUT OF SCOPE here (left to the experiment artifact): decoy/entrapment generation, LLM scoring, FDR/precision/recall, Prolog execution, transitive-closure enrichment. Files: data.py (uv run data.py), full_data_out.json (1.1MB, <100MB so no split), mini_data_out.json (3 ex), preview_data_out.json (3 ex, truncated). Reproducible via pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_Jcudmkugg1qT
type: dataset
title: >-
  Re-DocRED Anchor: 236-doc triple-schema corpus with entities, evidence & 4 CV folds
summary: |-
  Operational-anchor dataset standardized from Re-DocRED (Tan et al., 'Revisiting DocRED — Addressing the False Negative Problem in Relation Extraction', EMNLP 2022; HuggingFace tonytan48/Re-DocRED, MIT, 606 downloads, arXiv 2205.12696). THE single chosen dataset for the label-free FDR-gating / neuro-symbolic text→logic hypothesis.

  FORMAT: full_data_out.json follows the exp_sel_data_out contract: {metadata, datasets:[{dataset:'Re-DocRED', examples:[...]}]}. 236 examples = one Wikipedia document each, drawn from 4053 pooled train/dev/test docs. Each example is raw data only (NO candidates, decoys, scores, or FDR — those are the experiment's job).

  PER-EXAMPLE FIELDS: input = the reconstructed ~200-word document prose (deterministic detokenization, exact char offsets); output = JSON string of the gold (head,relation,tail) triples. metadata_* carries the rich structure: metadata_entities (full annotated inventory, 6 types, mention token spans + exact char_spans, canonical_name, n_mentions), metadata_gold_triples (shared canonical schema: head/tail id+name+type, relation_pid+relation_name, evidence_sent_ids, resolved evidence_text), metadata_sents (verbatim tokens, authoritative grounding), metadata_sent_char_offsets, and 17 metadata_features S5 GAP-regression inputs (num_words/chars/sents/entities/triples, relation & entity-type profiles, entity/mention/triple densities, frac_singleton_entities, frac_multi_evidence_triples, max_evidence_sentence_gap). Flags: metadata_fold (cluster_PER/ORG/LOC/MISC — primary dominant-entity-type folds for leave-one-cluster-out CV), metadata_kmeans_cluster (secondary k-means scheme), metadata_split_role + metadata_is_confirmatory/is_pilot/is_reserve, metadata_seed (20240617).

  BALANCE: 152 confirmatory / 36 pilot / 48 reserve, exactly balanced across the 4 folds (38/9/12 each), examples interleaved round-robin by fold; documents span the feature range so cross-document variance (the S5 precondition) is preserved (e.g. triple_density 0.38–14.75 across folds). Eligibility: 80≤num_words≤400, ≥4 entities, ≥5 triples. Confirmatory/pilot/reserve are mutually exclusive; every triple indexes a valid entity (verified).

  COMPANIONS: relation_schema.json (all 96 Wikidata P-ids with human-readable names AND descriptions, fetched live from the Wikidata API — the shared triple space every downstream system aligns to), entity_type_schema.json (6 types + glosses), dataset_meta.json (citation, URLs, counts, seed, cluster schemes, per-fold counts), row_schema.json (the custom JSON-Schema every row was validated against).

  GOLD CAVEAT (recorded in metadata): Re-DocRED has residual false negatives, so this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) — never an absolute realized-FDR diagonal (that role belongs to the separate CLUTRR anchor).

  REPRODUCIBILITY: pure-CPU data prep; `uv run data.py` regenerates everything deterministically from cached raw JSON (re-downloads from HF/GitHub if absent; relation names from Wikidata or cache). pyproject.toml pins all 13 dependency versions. full=11.7MB (<100MB, no split); all of full/mini/preview validate against exp_sel_data_out.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_SLUbUUr6Ul98
type: research
title: 'Spec Sheet: Label-Free FDR Gate at the LLM Text-to-Logic Admission Boundary'
summary: >-
  Consolidated, source-traceable implementation spec for the label-free decoy-competition FDR gate that admits LLM-extracted
  facts/bridges into a Prolog/symbolic layer. Provides, for each component, a verbatim formula (with equation number and source),
  a symbol glossary, a language-agnostic pseudo-procedure, and a recommended default. KEY RESULTS: (A) knockoff+ admission
  threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha} (Barber-Candes eq 1.9, exact FDR via Thm 2; plain knockoff eq
  1.8 controls only modified FDR Thm 1); the minimum-estimable-FDR floor is 1/k, so certifying FDR<=alpha needs k>=ceil(1/alpha)
  admissions -> demonstrable alpha grid {0.05,0.1,0.2,0.3,0.5} maps to k-floors {20,10,5,4,2}. Rajchert-Keich prove the '+1'
  is generally necessary (t=1 optimal), so keep it; TDC-SB/TDC-UB (bandsfdp) are an optional tighter FDX bound. (B) Entrapment
  estimators verbatim from Wen et al. 2025: combined FDP=N_E(1+1/r)/(N_T+N_E) (upper bound, DEFAULT), paired (eq4, requires
  r=1, tighter), lower bound N_E/(N_T+N_E) (failure-only), and 'sample' N_E(1/r)/N_T which is INVALID (biased). r=#entrapment/#target;
  default r=1 paired. (C) Document-block (cluster) bootstrap B>=2000 for all FDP/FDR CIs (resample whole documents; Cameron-Gelbach-Miller
  anchor) — the CI used by the primary disconfirmation. (D) Sole validity condition = Barber-Candes Lemma 1 (null W signs
  are i.i.d. fair coins) = TDC equal-chance; two anti-conservative failure modes (within-doc correlation -> bootstrap; batched
  contrast effect -> isolated provenance-blinded order-randomized scoring) and the isolated-vs-batched discriminator. (E)
  Property-matched document-conditioned COUNTERFACTUAL decoys + non-entailment verification (DeepCoy principle; DOE 0.166->0.032/0.109->0.038);
  random type-matched swaps kept as the anti-conservative negative control. (F) Ranked label-free upper-tail elicitation shortlist:
  DINCO (primary, overconfidence-corrected), FactSelfCheck (fact-level), self-consistency/SelfCheckGPT, logprob/yes-no-token
  (if exposed), verbalized (overconfident floor); Phase-0 selects on tail-AUC>0.5 with CI + isolated~batched agreement. (G)
  Recommended model openai/gpt-4.1-nano ($0.10/$0.40 per M, logprobs+auto-caching, <$0.30 input); fallbacks gpt-4o-mini then
  a logprob-free cheap caching model; projected cost ~$1-3 << $10 cap. (H) Novelty confirmed: no prior work applies knockoff/target-decoy/entrapment
  FDR at a label-free LLM text->logic admission boundary (conformal factuality/selection are labeled and certify outputs).
  Includes a final Parameter Defaults table and runtime follow-ups (probe logprobs non-null; confirm cached_tokens>0).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 4 ---
id: art_K6AE23HoGqe6
type: research
title: >-
  Spec: Text-to-FOL-to-Prolog Pipeline and the Fair Re-DocRED Operational Comparison
summary: >-
  Implementation-ready specification (verbatim prompt templates, on-disk data formats, exact library APIs, mapping rules,
  ASCII pipeline diagram, library table, and data-format cheat-sheets) for the extraction-to-Prolog neuro-symbolic pipeline
  and the fair matched-recall operational comparison of the decoy-gating hypothesis. Block A: LLM text->typed-FOL FACT/BRIDGE
  extraction with deliberate over-generation in LINC (NLTK/Prover9 FOL, <PREMISES>/<EVALUATE> tags) and Logic-LM (Predicates:::/Facts/Rules>>>/Query)
  style; controlled-functor fact()/bridge() on-disk forms; over-generation prompts (T=0.7, n=3, cap 20/doc) and the candidate-record
  JSON schema with worked CLUTRR and Re-DocRED examples. Block B: SWI-Prolog-from-Python execution (janus-swi RECOMMENDED
  with exact query_once/query/consult/apply_once API; pyswip fallback; swipl subprocess safety net) plus a vanilla solve/2
  proof-tree meta-interpreter extended so each leaf carries provenance + decoy_certificate (W_i,T,q) + entrapment_certificate
  (FDP-hat,r), exported to JSON and Graphviz DOT with a 2-hop example. Block C: offline WordNet hypernym argument typing into
  {PER,LOC,ORG,TIME,NUM,MISC} with exact synset anchors, reusing Re-DocRED gold NER, ConceptNet/DBpedia optional. Block D
  (load-bearing): the Re-DocRED JSON schema and official (title,r,h_idx,t_idx) triple-matching metric, plus ONE fixed claim-decomposition
  + relation-alignment (MiniLM top-8 shortlist -> fixed temp-0 LLM pick among 96 P-codes or NO_RELATION) + three-tier entity-linking
  procedure that maps neuro-symbolic/plain-threshold/CoT/RAG/conformal outputs identically into the (head, P-code, tail) space,
  with a per-system matched-recall score sweep, a hallucinated-conclusion-rate definition for multi-hop deductions, and document-block-bootstrap
  CIs. Block E: RAG (BM25) and CoT extraction prompts, the plain zero-label confidence-threshold gate (primary foil), and
  the verbatim Mohri-Hashimoto conformal back-off Algorithm 1 plus its reusable sayless.py implementation (BREAKDOWN_PROMPT,
  frequency+gpt scoring, ceil-quantile calibration), explicitly positioned as the LABELED reference the label-free decoy wedge
  improves on. The decoy-gating core states the knockoff statistic and the knockoff+ data-dependent FDR threshold. Ten design
  decisions are resolved with fallbacks; a shared sub-$0.30/M OpenRouter model with prompt caching is recommended. 26 primary
  sources (papers + GitHub repos) cited; high confidence except the full 96-row rel_info.json and model-logprob availability.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_expected_files:
- research_out.json
</supplementary_materials>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
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
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 05:34:02 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-16 05:35:45 UTC

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
