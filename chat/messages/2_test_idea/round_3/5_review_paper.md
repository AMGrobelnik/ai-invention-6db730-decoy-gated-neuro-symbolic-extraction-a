# review_paper — test_idea

> Phase: `invention_loop` · round 3 · `review_paper`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 10:14:28 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper
```

### [2] SYSTEM-USER prompt · 2026-06-16 10:14:34 UTC

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

A pipeline that converts unstructured prose into a formal, computable representation---one a logic engine such as SWI-Prolog can execute---promises the best of two worlds: the broad coverage of an LLM as a semantic translator, and the verifiable, auditable inference of a symbolic reasoner. The recurring failure point of such a pipeline is not parsing syntax but the *fuzzy-unification boundary*: when strict symbolic matching fails, an LLM must align a surface predicate to a schema relation and supply implicit background knowledge, and exactly at that interface hallucination re-enters and propagates into every deduction that consumes the admitted fact. The dangerous hallucinations are not random nonsense; they are *plausible, high-confidence false facts* that a downstream solver treats as ground truth.

The problem is both important and hard. It is important because a single fabricated premise admitted into a knowledge base contaminates an unbounded set of multi-hop conclusions, and because the application domains that most need auditable reasoning---short legal documents, news, regulatory text---are precisely those where a silently wrong fact is most costly. It is hard because the standard defenses do not act where the damage occurs. Self-consistency and LLM-as-judge are heuristic and give no quantitative control. Ontology-constraint filtering rejects only encoded violations and needs a rich trusted constraint set. The strongest uncertainty-quantification methods---conformal factuality [15], conformal selection with Benjamini--Hochberg [16], multiple-testing hallucination detection [18], coherent factuality over reasoning chains [17], conformal e-value novelty detection [29], and conformal link-prediction FDR [30]---all require a *labeled* calibration set and certify the *final answer or claim set*, not the *admission* of an intermediate fact into the symbolic layer.

Why has the admission boundary not been controlled before? Because the natural statistical tool for controlling false admissions among many candidate signals with no ground truth---the *false discovery rate* (FDR)---was developed in numeric feature selection and mass spectrometry, where a synthetic negative control exchangeable *by construction* is available. Genomics and proteomics solved an isomorphic label-poor problem---selecting true signals among overwhelming noise with a guaranteed FDR and no labels---via the knockoff filter [4, 5] and target-decoy competition, and learned the two ways the trick breaks: decoys *too unrealistic to fool* the scorer make the estimated FDR optimistic (cured by property-matched decoys [9]), and the entrapment false-discovery proportion (FDP) must be bounded by a mechanism built *independently* of the decoys [6]. We transplant this machinery to the LLM neural-to-symbolic boundary, label-free, and---this being a working environment with no construction-level guarantee---we *test* the validity condition rather than assume it.

This paper executes the protocol end to end and reports the realized numbers, including the ones that disconfirm. We propose *decoy-gated extraction*: before any LLM-proposed Prolog fact or bridge enters the knowledge base, it must out-score a *plausibility-matched* synthetic decoy---a document-conditioned counterfactual the model finds plausible but the document does not entail---in a knockoff+ competition that admits the most permissive cutoff whose estimated corpus-aggregate FDR is at most a target $\alpha$, using zero operation labels. The single canonical competition statistic is the knockoff+ *signed maximum* $W_i = \operatorname{sign}(Z_i - \tilde{Z}_i)\,\max(Z_i, \tilde{Z}_i)$, where $Z_i$ and $\tilde{Z}_i$ are the label-free scores of the real candidate and its matched decoy; knockoff+ thresholding admits $\{i : W_i \ge T\}$ at the most permissive $T$ whose estimate $\widehat{\mathrm{FDR}}(T) = (1 + \#\{W_i \le -T\}) / \max(1, \#\{W_i \ge T\}) \le \alpha$ [4]. Validity rests on the *null sign-flip property*---for genuinely false candidates the sign of $W_i$ must be a fair coin conditional on $|W_i|$---and because LLM decoys carry no construction-level proof of it, the realized-FDR-versus-$\alpha$ diagonal *is* its empirical test.

A previous version of this work reported a CLUTRR calibration diagonal that appeared *conservatively calibrated*. Reviewers correctly observed that this diagonal was computed under a *verbalized* confidence elicitation whose own decoy win-rate diagnostic flags it as strongly anti-conservative ("decoys too easy"), so the apparent conservatism could not be evidence of exchangeability. This paper takes that objection as its organizing question. We re-run the headline diagonal under the K=5 *self-consistency* elicitation that the win-rate diagnostic actually validates (counterfactual tail win-rate $0.48$, covering $0.5$) [ARTIFACT:art_sBLQqsdm3EIA]. The result is the paper's central, surprising finding: under the validated elicitation the gate *does not* control FDR on the error-dense multi-hop family---realized FDR is $1.0$ at the only certifiable target $\alpha^{*}=0.5$ (12 admitted, all 12 false; document-block CI $[0.66,1.0]$ lies entirely above $\alpha^{*}$), and the gate's own self-report $\widehat{\mathrm{FDR}}=0.5$ undershoots it. The pre-registered primary disconfirmation fires.

[FIGURE:fig1]

What makes this informative rather than merely negative is *why* it happens, and we localize the cause precisely. Self-consistency *does* restore the property the diagnostic measures: the counterfactual-decoy score distribution is statistically indistinguishable from the model's own spontaneous errors (full-distribution KS $p=0.058$; admission-tail KS $p=0.31$; both fail to reject) and sharply distinct from true positives (KS $p=5\times10^{-9}$). That is *marginal* (distributional) exchangeability. The knockoff+ gate, however, needs the *per-pair* sign-flip property at the cutoff, and it fails: among the twelve admitted multi-hop reals, the model scored each false real *above* its own matched decoy. Distributional exchangeability is necessary but not sufficient for paired exchangeability---and the win-rate diagnostic, being a marginal statistic, cannot see the gap. This two-layer decomposition is, we argue, the generalizable lesson of transplanting knockoffs to LLM scoring.

The same rigor is then applied where the goal actually lives. We *execute* the previously-missing application headline on a genre-faithful 24-document legal/news/regulatory anchor [ARTIFACT:art_vkfyOl2OQNVx]: the operational pipeline ingests ~3000-character documents, types entities against an upper ontology, gates extracted facts, runs multi-hop deductions, and emits auditable trace-graphs whose every leaf carries a provenance span and the decoy and entrapment certificates that licensed it. Here the gate behaves better than on the hard CLUTRR family---its self-report is *conservative*, it cuts the corrupted multi-hop conclusion rate from $0.48$ to $0.18$, and it reduces the atomic hallucination rate by ~$25\%$ (directional; bootstrap CIs overlap at $n{=}24$). Finally, on $152$ Re-DocRED documents the operational wedge over plain thresholding is disconfirmed at recall $\le0.075$, and we recast the operational contribution as a *gold-free regime-diagnostic* that predicts that null result without labels (prediction correct) [ARTIFACT:art_RZC2468yZ-Jh].

**Summary of contributions.**

- We formulate the *text-to-logic admission boundary* as an FDR-control problem and introduce *decoy-gated extraction*, to our knowledge the first label-free FDR knob at the neural-to-symbolic interface, built from a single canonical knockoff+ statistic, plausibility-matched counterfactual decoys, and independent entrapment corroboration (Sections 3--4).
- We answer the central methodology objection by re-running the calibration diagonal under the diagnostic-validated self-consistency elicitation, and report the pre-registered disconfirmation honestly: the gate does not control FDR on the populable multi-hop family (Section 6.1).
- We isolate the mechanism---*marginal decoy exchangeability does not imply paired sign-flip exchangeability* at the cutoff---and show the win-rate diagnostic, being marginal, over-predicts gate validity, a fundamental blind spot we report rather than paper over (Sections 6.2--6.3).
- We *execute* the genre-faithful application headline the prior draft was missing: a quantified, regime-mapped hallucination-reduction run on 24 professional documents with exported auditable trace-graphs, including a multi-hop corruption drop from $0.48$ to $0.18$ (Section 6.4).
- We scale the Re-DocRED operational test to its true scope (152 documents, recall $\le0.075$, all comparators participating, powered multi-hop comparison) and contribute a novel *label-free regime-diagnostic* that forecasts the gate's null wedge gold-free (Section 6.5).

# Related Work

**Label-free hallucination scoring.** Zero-resource detectors produce per-claim hallucination scores from sampling consistency (SelfCheckGPT [13]) or distractor-normalized verbalized confidence (DINCO [12]); FactSelfCheck [14] operates natively at the fact level over $(h, r, t)$ triples. These methods yield a *score*, not an admission threshold, and offer no exchangeability or competition argument. In our framework they are *candidate elicitations* feeding the gate, not the gate itself, and we select among them by *tail* behavior. Verbalized confidence is known to be overconfident in the upper tail [10], and token log-probability calibration degrades under reinforcement learning from human feedback [11]---two facts our results turn from caveats into a measured, central phenomenon.

**Labeled uncertainty quantification for LLMs.** Conformal factuality [15] removes claims until a factuality level is met, using a labeled calibration set, and certifies the emitted answer; coherent factuality [17] extends this to reasoning chains; conformal selection [16], multiple-testing hallucination detection [18], and online/feedback-driven testing [19] control FDR over candidate outputs but require labeled calibration outcomes; conformal e-value novelty detection [29] and conformal link prediction [30] control FDR over selected test points or predicted edges under (adapted) exchangeability of a labeled reference set. Table 1 contrasts the closest neighbors. Every one is *labeled* and certifies a *model output* under assumed exchangeability; ours is *label-free*, targets an *intermediate admission boundary*, manufactures the null behavior with engineered-and-tested decoys, and---crucially---empirically *tests* the exchangeability that the others assume [ARTIFACT:art_Cr6L9JpoewZi]. The distinction defuses the natural rebuttal that decoy-gating "is just conformal selection at the fact level": conformal selection imports exchangeability from a labeled calibration set whose outcomes are observed, whereas we have zero such labels and must test the fair-coin sign-flip property in the score tail---and we find that it can fail.

\begin{table}[t]
\centering
\small
\begin{tabular}{lcccc}
\toprule
Method & Labels? & Unit certified & Decoy? & Controls \\
\midrule
Conformal selection [16] & Yes & output shortlist & No & FDR \\
Multiple-testing hallucination [18] & Yes & generation & No & FDR \\
Conformal e-value novelty [29] & Yes & test points & No & FDR \\
Conformal link prediction [30] & Yes & predicted edges & No & FDR \\
Conformal factuality [15] & Yes & emitted claims & No & coverage \\
\textbf{Decoy-gating (ours)} & \textbf{No} & \textbf{admission boundary} & \textbf{Yes} & \textbf{FDR (tested)} \\
\bottomrule
\end{tabular}
\caption{Decoy-gating against its nearest FDR/conformal neighbors. All prior methods require labeled calibration and certify a model output under assumed exchangeability; ours is label-free, targets the intermediate text-to-logic admission, and empirically tests an engineered decoy sign-flip property---which we show is elicitation-dependent and can break even when its marginal proxy holds.}
\label{tab:novelty}
\end{table}

**FDR control by competition.** The knockoff filter [4] and Model-X knockoffs [5] select signals with guaranteed FDR by competing each real candidate against a synthetic negative control exchangeable by construction, relying on the null sign-flip property; the knockoff+ threshold controls FDR exactly via the conservative $+1$ offset [4], which Rajchert and Keich prove is in general necessary [7]. Ebadi et al. give tighter upper prediction bounds on the FDP [8]. In proteomics, entrapment estimation provides an independent FDP bound, with the valid combined estimator and the flawed naive estimator characterized by Wen et al. [6]; property-matched decoy generation (DeepCoy [9]) shows decoys must reproduce a target score distribution. We adapt all three to the LLM boundary, where exchangeability is *not* provable. Our contribution to this line is empirical and cautionary: we show that at the LLM boundary the construction can satisfy the *marginal* matching DeepCoy targets while still violating the *paired* sign-flip property the knockoff theorems require.

**Text-to-logic neuro-symbolic reasoning.** LINC [20] and Logic-LM [21] semantic-parse premises into first-order logic or symbolic programs executed by a solver, with majority voting or solver-error self-refinement; LLM-ASP [23] parses CLUTRR into reusable answer-set modules. None exercises principled control over *which* extracted premises are admitted: a syntactically valid but fabricated premise is never challenged, voting merely smooths variance, and refinement fixes only solver and syntax errors. Standard neural baselines---chain-of-thought prompting [22] and retrieval-augmented generation [26]---have no admission boundary at all. Logical-reasoning benchmarks such as RuleTaker [24], ProofWriter [25], and CLUTRR [1] supply controlled targets; our calibration anchor is CLUTRR for its crisp templated gold, and our operational anchor is Re-DocRED [2], the false-negative-corrected re-annotation of DocRED [3]. For the symbolic layer we type arguments with WordNet [32] anchored to the SUMO upper ontology [31], and design a probabilistic upgrade on ProbLog [33], whose DeepProbLog extension [34] is the precedent for an external model supplying clause probabilities.

# Preliminaries

We control the false admission of two candidate kinds. A *fact* is a ground typed atom (for example `rel_child(e_alice, e_bob)`), and a *bridge* is a fuzzy-unification rule---a kinship composition rule for CLUTRR, or a surface-form-to-schema relation alignment for the open-vocabulary anchors. Bridges are first-class admission candidates with their own decoy, score, and gate.

**The canonical competition statistic.** Each candidate $i$ receives a label-free score $Z_i$ from an isolated elicitation and a matched decoy score $\tilde{Z}_i$. We use a single statistic throughout: the knockoff+ *signed maximum*
$$W_i = \operatorname{sign}(Z_i - \tilde{Z}_i)\cdot\max(Z_i, \tilde{Z}_i),$$
whose magnitude is the larger of the two scores and whose sign records which won. A large positive $W_i$ is evidence that the candidate is a true signal. The per-pair *signed difference* $d_i = Z_i - \tilde{Z}_i$ is used *only* as a measurement-only tail diagnostic (win-rate and CDF tests), never as the gating statistic.

**Two notions of exchangeability, and why the distinction is load-bearing.** Knockoff+ delivers a finite-sample FDR guarantee only under the *paired sign-flip property*: among genuinely false candidates, $\operatorname{sign}(W_i)$ is an independent fair coin conditional on $|W_i|$, i.e. a false real and its matched decoy are equally likely to take the larger score *as a pair*. A strictly weaker, and separately measurable, property is *marginal (distributional) exchangeability*: the pooled distribution of decoy scores equals the pooled distribution of false-real scores. DeepCoy-style decoy design [9] and the win-rate / CDF diagnostics target the *marginal* property. Our central empirical finding (Section 6.2) is that the two come apart at the LLM boundary: self-consistency restores the marginal property while the paired property still fails, so the marginal diagnostic over-certifies the gate.

**The targets and the two roles of resampling.** The target is the corpus-aggregate FDR---the expected fraction of admitted candidates that are document-non-entailed---held at or below a user-chosen $\alpha$, separately for facts and bridges and per anchor. We report, for every certified cell, the *triple* $(\alpha,\ \widehat{\mathrm{FDR}},\ \text{realized FDR})$, so that a gate whose own estimate $\widehat{\mathrm{FDR}}$ undershoots the realized FDR is flagged as *self-report anti-conservative* even when the realized FDR happens to land below $\alpha$. The *document-block bootstrap* (resampling whole documents, $B = 2000$ [28]) supplies confidence intervals on the realized FDP and a within-document-dependence diagnostic; it quantifies sampling variability and does *not* restore the guarantee under dependence. Because the conservative $+1$ makes the smallest attainable estimate $1/k$ with $k$ admissions, certifying $\widehat{\mathrm{FDR}}\le\alpha$ requires $k \ge \lceil 1/\alpha \rceil$; the demonstrable grid $\alpha\in\{0.05,0.1,0.2,0.3,0.5\}$ maps to admission floors $\{20,10,5,4,2\}$, and any $\alpha$ below an anchor's reachable floor is reported as structurally undemonstrable, never as "confirmed by conservatism."

# Method

The pipeline has six stages: over-generating extraction, plausibility-matched decoy generation, isolated provenance-blinded scoring, the knockoff+ FDR gate, independent entrapment corroboration, and symbolic reasoning with auditable trace-graphs. The full implementation specification---verbatim prompt templates, on-disk formats, and library APIs---is provided in the supporting research artifacts [ARTIFACT:art_SLUbUUr6Ul98][ARTIFACT:art_K6AE23HoGqe6].

## Extraction with deliberate over-generation

A cheap LLM proposes typed first-order facts and bridges from the document in a LINC/Logic-LM style [20, 21], with argument types grounded in a commodity upper-ontology slice. Because OpenCyc was discontinued by Cycorp in March 2017 and survives only as unmaintained mirrors, and ResearchCyc is license-gated, OpenCyc cannot be a reproducible commodity dependency; we substitute an offline WordNet [32] hypernym lookup that maps each argument head noun into the coarse vocabulary $\{$PER, LOC, ORG, TIME, NUM, MISC$\}$ via anchor synsets, each coarse type further anchored to a SUMO upper-ontology class (e.g. `person.n.01` $\to$ PER $\to$ `&%Human`) [31][ARTIFACT:art_Cr6L9JpoewZi]. Typing is used *only* to constrain decoy generation and entity linking, never to filter; because it never rejects a candidate it cannot break the FDR guarantee. The extractor deliberately *over-generates* (temperature $0.7$, multiple samples unioned) so the candidate pool is dense in genuine false positives---a precondition for a non-vacuous calibration diagonal.

## Plausibility-matched counterfactual decoys

The load-bearing design choice is the decoy family. The relevant target distribution at the LLM boundary is not the true-positive distribution DeepCoy matches in molecular screening [9], but the distribution of the model's *own spontaneous false extractions*---the plausible hallucinations the gate must actually catch. Our primary family is the *document-conditioned counterfactual*: given the document and the relation/type schema, the model produces a maximally plausible fact or bridge that is *not* entailed by the text, matching the surface form and specificity of the document's real facts. Every decoy passes an independent isolated non-entailment check (an accidentally entailed decoy is actually true and would bias the FDR conservatively); the contamination rate is logged (CLUTRR $8.4\%$, application anchor $5.7\%$) [ARTIFACT:art_sBLQqsdm3EIA][ARTIFACT:art_vkfyOl2OQNVx]. As a deliberately retained negative control we also generate *random type-matched swaps*, predicted to read anti-conservative precisely because they are too easy. Crucially, we do not assume the decoys match the spontaneous-error distribution---we *test* it (Section 6.2), and, as the same section shows, we test whether marginal matching is sufficient.

## Isolated, provenance-blinded scoring and elicitation selection

Each candidate---real, decoy, or entrapment---is scored in its *own* prompt with source identity masked and presentation order randomized, removing within-batch contrast effects that would let the model implicitly detect a fabricated item and depress its score. Document-prefix prompt caching makes isolated scoring affordable. The per-candidate score is produced by a *tail-exchangeability*-selected elicitation, not an average-calibration-selected one. This selection criterion is the key correction over the prior draft: a Phase-0 pilot ranks verbalized confidence, a DINCO-style distractor-normalized score [12], a $K$-sample self-consistency score [13, 14], and a log-probability yes/no score by their *tail* decoy win-rate (target $\approx 0.5$), not by full-distribution AUC. The distinction matters because the two criteria disagree: verbalized confidence and DINCO have higher full-distribution AUC ($0.861$ and $0.871$) yet fail the tail test, whereas K=5 self-consistency has the tail win-rate that covers $0.5$ ($0.482$) [ARTIFACT:art_Inu52CyA49Ys]. Higher AUC does not imply tail-exchangeability; self-consistency therefore hosts the headline diagonal. The generator$\neq$scorer ablation that de-circularizes the construction is settled (Section 6.3) and carried forward.

## The knockoff+ FDR gate and its self-report

Given the competition statistics, the gate admits $\{i : W_i \ge T\}$ at the smallest cutoff $T$ for which $\widehat{\mathrm{FDR}}(T) \le \alpha$ [4]. We keep the conservative $+1$ for the headline certificate. Beyond realized FDR (against gold) and the target $\alpha$, we *always* report the gate's internal estimate $\widehat{\mathrm{FDR}}$, so that the failure mode "the estimate is anti-conservative" ($\widehat{\mathrm{FDR}} < \text{realized}$) is surfaced as its own disconfirmation even when realized FDR lands below $\alpha$.

## Independent entrapment corroboration

Decoy competition decides admission; *entrapment* provides an independent upper bound on the realized FDP, built by a mechanism *distinct* from the decoys (in-genre cross-document swaps, numeric or temporal perturbation, explicit contradiction) and constructed *without* the generating LLM. We use the valid combined estimator $\widehat{\mathrm{FDP}} = N_E(1 + 1/r)/(N_T + N_E)$ as the default certificate [6], with $N_T,N_E$ the admitted target and entrapment counts and $r$ the entrapment-to-target ratio; we never use the naive estimator, which Wen et al. prove biased [6].

## Symbolic reasoning and auditable trace-graphs

Admitted facts and bridges populate a backward-chaining knowledge base for multi-hop deduction; we target SWI-Prolog through the `janus-swi` bridge and fall back to a pure-Python meta-interpreter with an identical trace-graph schema when the native bridge is unavailable [ARTIFACT:art_K6AE23HoGqe6][ARTIFACT:art_vkfyOl2OQNVx]. A `solve/2`-style meta-interpreter captures the proof as a *trace-graph* whose nodes are sub-goals and derived facts and whose edges are labeled rule applications. Every leaf resolves to a certificate term: the provenance span, the decoy-competition certificate $(W_i, T, \alpha)$, and the entrapment certificate $(\widehat{\mathrm{FDP}}, r)$. The trace-graph serializes to JSON for machine audit and Graphviz DOT for human audit. A designed *probabilistic* upgrade swaps the deterministic query for ProbLog's `get_evaluatable().evaluate()` [33], turning each admitted clause into a weighted clause $p_i :: \mathrm{fact}$ with $p_i$ a calibrated function of $Z_i$, so derived conclusions carry marginal probabilities while every leaf retains its certificate [ARTIFACT:art_Cr6L9JpoewZi].

# Experimental Setup

The evaluation is split so that calibration and operational usefulness are proven on the data each suits, and the protocol is pre-registered so every outcome---confirmed, disconfirmed, or untestable---is interpretable.

## Three anchors with a clean division of labor

CLUTRR [1] is rule-based and templated, so its kinship gold is exact---the property that lets it host the realized-FDR-versus-$\alpha$ *diagonal* and the single primary disconfirmation. The corpus draws on a standardized atomic + multi-hop kinship triple set derived entirely from CLUTRR's own `proof_state` fields over a 20-relation vocabulary [ARTIFACT:art_XZyKy6QuwxrO]; the diagonal in this paper is computed on the error-dense $40$-document checkpoint of the scaled confirmatory split, which yields $410$ extracted reals ($123$ true, $287$ spontaneous false) and is populable on both families ($129$ false atomic, $158$ false multi-hop, exceeding the pre-registered $N_{\text{false\_min}}=40$ floor) [ARTIFACT:art_sBLQqsdm3EIA]. Re-DocRED [2] is human-annotated, open-vocabulary, and document-level, so it hosts the *operational* comparison and the genuine schema-alignment bridge test; the anchor comprises Wikipedia documents with gold $(head, relation, tail)$ triples over $96$ Wikidata relations [ARTIFACT:art_Jcudmkugg1qT], and because it retains residual false negatives it licenses only *relative* operational comparisons. Finally, the genre-faithful *application anchor* is $24$ genuine professionally-written documents ($8$ legal, $8$ news, $8$ regulatory; native length $1239$--$3474$ characters, mean $2372$, squarely in the ~3000-character target range), standardized to the same triple schema with character-span provenance and $140$ human/structure-derived gold facts built with no LLM in the loop [ARTIFACT:art_UBTwyePql8NQ]. CLUTRR tests whether the knob is calibrated; the application anchor tests whether it reduces hallucination on the documents the goal targets; Re-DocRED tests whether it beats plain thresholding operationally.

## Pipeline, baselines, and metrics

All systems run on commodity CPU with `openai/gpt-4.1-nano` via OpenRouter as the primary model and `mistralai/ministral-8b-2512` as the cross-family scorer/adjudicator. The comparators are the *plain confidence-threshold gate* (the primary zero-label foil, identical elicitation, no decoy or competition), chain-of-thought [22], retrieval-augmented generation [26], and labeled Mohri--Hashimoto conformal factuality [15]. On Re-DocRED a single fixed claim-decomposition and relation-alignment step maps every system's raw output into the shared triple space identically (a MiniLM [27] top-eight relation shortlist followed by a temperature-0 pick among the 96 codes, with three-tier entity linking), and recall is matched by sweeping each system's own score to a common operating point. All confidence intervals use the document-block bootstrap and all multiplicity is controlled by Benjamini--Hochberg at $q = 0.05$.

## Pre-registered claims and the primary disconfirmation

Table 2 lists the pre-registered claim chain and its verdicts. The single primary disconfirmation is fixed in advance: on the populable CLUTRR family (default multi-hop) under isolated *self-consistency* scoring at the operative $\alpha^{*}$, the central control claim is disconfirmed if realized FDR exceeds $\alpha^{*}+\tau$ (with $\tau=0.05$) and the document-block CI lies entirely on the anti-conservative side; additionally the gate's self-report is disconfirmed if $\widehat{\mathrm{FDR}}$ is anti-conservative relative to realized FDR.

\begin{table}[t]
\centering
\small
\begin{tabular}{lll}
\toprule
Claim & Test & Verdict \\
\midrule
S0 Score separation & tail-exchangeability selection (not AUC) & PASS \\
S1 Marginal decoy match & decoy$\approx$spont (KS $p{=}0.058$), $\neq$ true-pos & PASS \\
S1b Diagnostic sensitivity & swap control loses sensitivity; ladder underpowered & FAIL (blind spot) \\
S2 Calibration diagonal & multi-hop realized FDR $1.0$ at $\alpha^{*}{=}0.5$ & DISCONFIRMED \\
S2-self & $\widehat{\mathrm{FDR}}{=}0.5 <$ realized $1.0$ & DISCONFIRMED \\
S2b Generator$\neq$scorer & 4/4 configs win-rate CI covers $0.5$ & ROBUST \\
S3 Entrapment & $\widehat{\mathrm{FDP}}$ high at $\alpha{=}0.5$ (loose admit) & AGREES (loosely) \\
S4 Operational wedge & $\Delta$(METHOD$-$PLAIN)$\le0$ at recall $\le0.075$ & DISCONFIRMED \\
S4b Application headline & corruption $0.48{\to}0.18$; atomic $-25\%$ (CI overlap) & EXECUTED \\
\bottomrule
\end{tabular}
\caption{Pre-registered claim-chain verdicts under the diagnostic-validated self-consistency elicitation. The calibration certificate (S2) is honestly disconfirmed; the marginal decoy match (S1) holds, which is exactly what makes S2 instructive; the operational pipeline (S4b) delivers a measured corruption reduction and auditable traces.}
\label{tab:claims}
\end{table}

# Results

We lead with the corrected calibration diagonal, explain its disconfirmation mechanistically, then report the executed application headline and the reframed operational wedge.

## The corrected CLUTRR calibration diagonal under self-consistency (S2)

Re-running the headline diagonal under the diagnostic-validated K=5 self-consistency elicitation reverses the prior draft's claim [ARTIFACT:art_sBLQqsdm3EIA]. On the error-dense multi-hop family---the pre-registered populable family, ~$85\%$ genuine false because the extractor's forced multi-hop relation accuracy is only $0.17$---the gate certifies admissions at exactly one target, $\alpha^{*}=0.5$ (the $1/k$ floor blocks all stricter $\alpha$). At that target the realized FDR against crisp gold is $1.0$: of $12$ admitted reals, all $12$ are document-non-entailed, with document-block CI $[0.66,1.0]$ lying entirely above $\alpha^{*}$. The gate's own self-report $\widehat{\mathrm{FDR}}=0.5$ undershoots the realized $1.0$. The pre-registered primary disconfirmation therefore *fires* on both the calibration and the self-report criteria.

[FIGURE:fig2]

The atomic family tells the same story more mildly: at $\alpha=0.3$ realized FDR is $0.377$ (61 admitted, 23 false) against a self-report of $0.279$---a target violation ($0.377>0.3$) and an anti-conservative self-report---while at $\alpha=0.5$ realized FDR is $0.422$ with self-report $0.491$ (within target). Across both families the plain confidence-threshold baseline is worse still (multi-hop realized FDR $0.80$--$0.87$; atomic $0.17$--$0.55$), so decoy competition *helps relative to plain thresholding* even here---but "better than an uncontrolled baseline" is not "controls FDR at $\alpha$," and we do not claim the latter. The prior draft's apparent conservatism [ARTIFACT:art_ikjFm_faAe0x] is, when the same verbalized elicitation is re-run on this data, a discreteness/loose-target artifact: the verbalized diagonal admits *nothing* on the multi-hop family at any $\alpha$ and violates the target on the atomic family at $\alpha=0.5$ (realized $0.534>0.5$, self-report $0.5$) [ARTIFACT:art_sBLQqsdm3EIA]. We therefore retain verbalized only as a documented contrast, never as a co-headline.

## Why the gate fails: marginal vs. paired exchangeability (S1)

The disconfirmation is informative because the marginal precondition the diagnostic checks *does* hold under self-consistency. The counterfactual-decoy score distribution is statistically indistinguishable from the model's own spontaneous-error distribution---full-distribution KS $p=0.058$, Mann--Whitney $p=0.061$, Anderson--Darling $p=0.061$, permutation $p=0.060$ (all fail to reject), tightening in the admission tail (top-25\% KS $p=0.31$)---and sharply distinct from the true-positive distribution (KS $p=5\times10^{-9}$, Mann--Whitney $p=4\times10^{-12}$) [ARTIFACT:art_sBLQqsdm3EIA]. By the marginal criterion the decoys are exactly right: they look like the spontaneous errors, not like the true facts.

[FIGURE:fig3]

Yet the paired competition fails. Among the twelve admitted multi-hop reals, the model assigned each false real a *higher* self-consistency score than its own matched decoy---the per-pair sign-flip property knockoff+ requires is violated precisely in the admission tail where it matters. The reconciliation is that marginal (distributional) exchangeability is strictly weaker than paired exchangeability: two pooled distributions can coincide while, pair by pair, the false real systematically out-scores its decoy. This gap is the generalizable lesson. Property-matched decoy design and win-rate/CDF diagnostics, imported from cheminformatics and proteomics, certify the *marginal* property; the knockoff theorems need the *paired* one; at the LLM boundary the two come apart, and a marginal diagnostic cannot detect the difference. We state this as a limitation of the entire decoy-competition approach to LLM fact admission, not of one elicitation.

## The diagnostic blind spot and de-circularization (S1b, S2b)

The blind spot has a second, independently measured face. Under the very K=5 self-consistency that restores marginal exchangeability, the random-swap negative control---which *must* read anti-conservative---is no longer reliably flagged: at this checkpoint the difficulty ladder L0--L4 is underpowered (only two false pairs reach the operative tail per rung), and its verdict is `PARTIAL`---the diagnostic detects only grossly out-of-context (foreign-entity) decoys and loses resolution for in-distribution rungs [ARTIFACT:art_sBLQqsdm3EIA]. Combined with the marginal-vs-paired gap, this means the win-rate diagnostic both (i) over-predicts paired validity and (ii) loses sensitivity to too-easy decoys in the regime where it is supposed to be trusted. We therefore *downgrade* the prior draft's "the diagnostic tells the practitioner which regime they are in" claim to "the diagnostic detects gross non-exchangeability and tail-overconfidence but cannot certify paired validity," and we mark a sensitive paired-exchangeability diagnostic as required future work.

The one circularity concern that *is* settled is shared-model bias. The generator$\neq$scorer ablation is robust: across all four $(G,S)$ configurations---including decoys generated by gpt-4.1-nano and scored by the cross-family ministral-8b, and the symmetric swap---the tail win-rate CI covers $0.5$ (e.g. $0.491$, CI $[0.37,0.61]$, KS $p=0.999$) [ARTIFACT:art_Inu52CyA49Ys]. The marginal exchangeability self-consistency restores is therefore not an artifact of one model scoring its own outputs; the *paired* failure is likewise not a circularity artifact but a genuine property of LLM tail scoring.

## The application headline: hallucination reduction and auditable traces (S4b)

We then execute the genre-faithful application run the prior draft was missing, on the 24-document legal/news/regulatory anchor, reporting both elicitations across the full $\alpha$ grid so the regime-dependence is never obscured [ARTIFACT:art_vkfyOl2OQNVx]. Three honest findings follow.

[FIGURE:fig4]

*First, the atomic hallucination reduction is directional, not significant.* At the only certified target ($\alpha=0.5$; the $24$-document corpus floors stricter $\alpha$ at zero admissions), the pooled gate hallucinated-fact rate is $0.183$ under self-consistency and $0.178$ under log-probability, versus the $\alpha$-invariant raw-LLM rate of $0.243$---a ~$25\%$ relative reduction---but $0$ of $40$ grid cells reach bootstrap-CI separation at $n=24$, so the reduction is directional. The largest single-cell reduction is regulatory under self-consistency: raw $0.439\to$ gate $0.360$. *Second, and in pointed contrast to the CLUTRR multi-hop regime, the gate's self-report here is conservative*---$\widehat{\mathrm{FDR}}\ge$ realized FDR in every one of the $40$ cells---so the second-order disconfirmation does not fire on this anchor. *Third, the multi-hop corruption result is the clearest positive*: the raw-LLM knowledge base derives $23$ conclusions at a $0.48$ corrupted rate, whereas the gated knowledge base at $\alpha=0.5$ derives $11$ conclusions at a $0.18$ corrupted rate, with the regulatory genre dropping from $0.92$ to $0.67$ and legal from---already clean---$0.0$ to $0.0$. Gating removes the premises that would otherwise propagate into corrupted deductions.

[FIGURE:fig5]

Every admitted fact enters the symbolic layer with a full certificate, and the pipeline exports auditable trace-graphs (six documents, JSON + Graphviz DOT) whose leaves carry provenance, decoy, and entrapment certificates. For example, the legal proof of `party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1 2005)` resolves through `has_party` ($W_i=0.842$, $T=0.129$, $\alpha=0.5$) and `effective_date` ($W_i=0.790$), each annotated with the entrapment certificate $(\widehat{\mathrm{FDP}}=0.667, r=1)$; a regulatory proof of `titled_obligation(Art.~7 GDPR, ...)` exposes a *rejected* leaf (`obligates`, $W_i=-0.333$) directly in the trace, making the gate's decision human-auditable. Honesty requires three caveats we record at the point of claim: extraction quality on these genres is modest (atomic precision/recall: legal $0.28/0.27$, news $0.29/0.18$, regulatory $0.17/0.42$); $117$ of $210$ reals are gold-undecidable, so hallucination is reported by gold-membership with silver bounds; and the cross-family adjudicator was *dropped* because its agreement with the crisp legal gold was poor ($\kappa=0.10<0.4$), partly because the CUAD gold itself has partial recall.

## Re-DocRED: disconfirmed wedge, reframed as a gold-free regime-diagnostic (S4)

We report the operational result at its true, now-corrected scope [ARTIFACT:art_RZC2468yZ-Jh]. Scaling from the prior $36$ documents to the full $152$ confirmatory documents, ranking the identical candidate pool by the knockoff+ statistic $W_i$ does *not* beat ranking by raw confidence $Z_i$ at matched recall: across the recall grid (ceiling $0.075$, the shared METHOD/PLAIN maximum) no point shows a precision gain with bootstrap CI entirely above zero, so the pre-registered verdict is an operational disconfirmation---*at recall $\le0.075$ on 152 documents*. Two reviewer-flagged weaknesses are fixed. All five systems now participate: relaxing the matched-recall floor to the lowest positive maximum recall ($0.034$) gives the recall-limited CoT ($0.051$) and RAG ($0.034$) at least one evaluable point, so no all-null baseline is listed as a comparator. And the multi-hop comparison is *powered*: six gold-justified Wikidata inverse rules densify forward-chained conclusions to $267$ per system (far above the pre-registered power target of $100$), giving a hallucinated-conclusion-rate difference of $-0.004$ (CI $[-0.018,0.008]$)---a precisely null effect, not an underpowered one.

The substantive new contribution is to recast this null as a *prediction*. A label-free regime-diagnostic (zero API calls, no gold) reads four cached signals: the tail decoy win-rate ($0.045$, far below $0.5$ $\Rightarrow$ decoys too easy), the spontaneous-error CDF match (decoy mean $0.165$ vs. low-self-consistency real mean $0.857$; KS/MW/permutation all reject $\Rightarrow$ too easy), the $W$-versus-$Z$ ranking divergence (fraction of candidates with $W_i=Z_i$ equal to $0.939$, admitted-set Spearman $\rho=0.991$ $\Rightarrow$ the gate keeps and orders the same facts as the plain threshold, so the wedge is *mechanically* null), and base-scorer calibration (AUC $=0.60$). The diagnostic emits "GATE REDUNDANT, predicted wedge sign null," which the realized wedge confirms (prediction correct). Placed beside the CLUTRR regimes, the diagnostic yields a unifying---and honestly caveated---two-axis picture: gate value rises with base-scorer tail-overconfidence but is *conditional* on decoy exchangeability. The one point this two-axis map gets *wrong* is the very point our calibration diagonal corrects: the CLUTRR self-consistency win-rate of $0.482$ would predict "gate adds value," yet the powered paired diagonal disconfirms it (Section 6.1). That contradiction is not a flaw in the reporting---it is the clearest possible statement of this paper's central finding, that a marginal win-rate cannot certify paired validity.

## Cost and reproducibility

The entire iteration ran on commodity CPU: the corrected self-consistency diagonal cost \$0.02 (cache-warm), the application headline \$0.31, and the Re-DocRED regime-diagnostic \$1.08, for ~\$1.4 this iteration and ~\$2.6 cumulative against the \$10 cap, with exact per-call metering and a persistent on-disk cache enabling free resumes [ARTIFACT:art_sBLQqsdm3EIA][ARTIFACT:art_vkfyOl2OQNVx][ARTIFACT:art_RZC2468yZ-Jh]. All anchors regenerate deterministically under fixed seeds.

# Discussion

**What we now know, and where the certificate breaks.** Decoy-gated extraction is the first label-free FDR knob proposed at the fuzzy-unification boundary, and executing it carefully has taught a precise lesson that a working certificate would have hidden. The validity of a knockoff-style gate at the LLM boundary decomposes into two layers: a *marginal* layer (decoy scores distributed like the model's spontaneous errors), achievable by an aggregation elicitation and verifiable label-free; and a *paired* layer (the false real and its decoy equally likely to win at the cutoff), which the knockoff theorems actually require and which we find can fail even when the marginal layer holds. The standard decoy-quality diagnostics imported from genomics and proteomics live entirely in the marginal layer, so they *over-certify* the gate. This is, to our knowledge, the first demonstration that the marginal/paired distinction is operative---and consequential---when knockoffs are transplanted to LLM scoring.

**The honest value proposition.** The gate's *operational* value over plain thresholding is concentrated where the base elicitation is tail-overconfident and the decoys are exchangeable, and is null where the base scorer is already calibrated (Re-DocRED). The gate's *certified-FDR* value is, on present evidence, not established on hard multi-hop families: marginal exchangeability is necessary but not sufficient. What survives unambiguously is the *auditable pipeline*---typed extraction, a quantitatively-reported (if directional) hallucination reduction on genre-faithful documents, a measured drop in corrupted multi-hop conclusions ($0.48\to0.18$), and per-leaf certificates---and the *gold-free regime-diagnostic*, which correctly forecasts where the gate is redundant. These are the deliverables the goal requires, and they do not depend on the missing certificate.

**Limitations.** First and foremost, the FDR certificate is disconfirmed on the populable CLUTRR multi-hop family under the diagnostic-validated elicitation; we do not claim label-free FDR control there. Second, the self-detecting diagnostic has a structural blind spot: a marginal win-rate cannot certify paired validity, and at our checkpoint the difficulty ladder is underpowered, so the "tells you when to trust the gate" claim is downgraded accordingly. Third, the CLUTRR diagonal is computed on a $40$-document checkpoint; a powered re-run is the immediate next step, though the disconfirmation direction (realized $1.0$, CI above $\alpha^{*}$) is unlikely to reverse. Fourth, the application hallucination reduction is directional, not CI-separated, at $n=24$, and its gold is partly silver. Fifth, we descope two named goal requirements with stated rationale: OpenCyc is discontinued, so we substitute an offline WordNet$\to$SUMO typing stack that supplies taxonomic grounding but not Cyc's assertional commonsense KB; and the executed reasoning layer is deterministic backward chaining, with the ProbLog probabilistic upgrade designed and specified but not yet run [ARTIFACT:art_Cr6L9JpoewZi].

**Connection to the target application.** The pipeline ingests short professionally written documents, types their entities against an upper ontology, translates them to first-order logic, executes multi-hop deductions, and emits auditable trace-graphs on commodity hardware---the operational profile the task demands. The decoy gate is a tunable, label-free hallucination-reduction control that raw LLM generation lacks; what this iteration establishes is precisely the boundary of its statistical guarantee, so a practitioner knows it as an operational filter with measured (directional) benefit and auditable provenance, not as a certified-FDR oracle.

# Conclusion

We formulated the text-to-logic admission boundary as a label-free FDR-control problem, introduced decoy-gated extraction, and---taking the reviewers' methodology objection as the organizing question---re-ran the calibration diagonal under the elicitation the win-rate diagnostic actually validates. The corrected diagonal disconfirms the gate's FDR certificate on the error-dense multi-hop family (realized FDR $1.0$ at $\alpha^{*}=0.5$, CI $[0.66,1.0]$), and we localize the cause: self-consistency restores *marginal* decoy exchangeability (decoy$\approx$spontaneous-error, KS $p=0.058$; $\neq$ true-positive, KS $p=5\times10^{-9}$) but not the *paired* sign-flip property knockoff+ requires, so a marginal diagnostic over-certifies the gate. Where the goal lives, the pipeline nonetheless delivers: on $24$ genre-faithful documents it cuts the corrupted multi-hop conclusion rate from $0.48$ to $0.18$ and the atomic hallucination rate ~$25\%$ (directional) with conservative self-report and exported auditable trace-graphs; on $152$ Re-DocRED documents the operational wedge is disconfirmed at recall $\le0.075$ and a gold-free regime-diagnostic predicts that null correctly. Future work, in priority order, is to (1) build a *paired*-exchangeability diagnostic and decoy family that close the marginal-paired gap rather than measuring around it; (2) execute the powered self-consistency diagonal and the ProbLog probabilistic upgrade; (3) develop the regime-diagnostic into a deployment-time gate-applicability test; and (4) tighten the conservative $+1$ floor where validity permits.

# References

[1] K. Sinha, S. Sodhani, J. Dong, J. Pineau, and W. L. Hamilton. CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text. In *EMNLP*, 2019.

[2] Q. Tan, L. Xu, L. Bing, H. T. Ng, and S. M. Aljunied. Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction. In *EMNLP*, 2022.

[3] Y. Yao, D. Ye, P. Li, X. Han, Y. Lin, Z. Liu, Z. Liu, L. Huang, J. Zhou, and M. Sun. DocRED: A Large-Scale Document-Level Relation Extraction Dataset. In *ACL*, 2019.

[4] R. F. Barber and E. J. Cand\`es. Controlling the False Discovery Rate via Knockoffs. *Annals of Statistics*, 43(5):2055--2085, 2015.

[5] E. Cand\`es, Y. Fan, L. Janson, and J. Lv. Panning for Gold: Model-X Knockoffs for High-Dimensional Controlled Variable Selection. *Journal of the Royal Statistical Society: Series B*, 2018.

[6] B. Wen, J. Freestone, M. Riffle, M. J. MacCoss, W. S. Noble, and U. Keich. Assessment of False Discovery Rate Control in Tandem Mass Spectrometry Analysis Using Entrapment. *Nature Methods*, 22:1454--1463, 2025.

[7] A. Rajchert and U. Keich. Controlling the False Discovery Rate via Competition: Is the +1 Needed? *Statistics & Probability Letters*, 2022.

[8] A. Ebadi, D. Luo, J. Freestone, W. S. Noble, and U. Keich. Bounding the FDP in Competition-Based Control of the FDR. *arXiv:2302.11837*, 2023.

[9] F. Imrie, A. R. Bradley, and C. M. Deane. Generating Property-Matched Decoy Molecules Using Deep Learning. *Bioinformatics*, 37(15):2134--2141, 2021.

[10] M. Xiong, Z. Hu, X. Lu, Y. Li, J. Fu, J. He, and B. Hooi. Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. In *ICLR*, 2024.

[11] K. Tian, E. Mitchell, A. Zhou, A. Sharma, R. Rafailov, H. Yao, C. Finn, and C. D. Manning. Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback. In *EMNLP*, 2023.

[12] V. Wang and E. Stengel-Eskin. Calibrating Verbalized Confidence with Self-Generated Distractors (DINCO). *arXiv:2509.25532*, 2025.

[13] P. Manakul, A. Liusie, and M. J. F. Gales. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. In *EMNLP*, 2023.

[14] A. Sawczyn, J. Binkowski, D. Janiak, et al. FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs. 2025.

[15] C. Mohri and T. Hashimoto. Language Models with Conformal Factuality Guarantees. In *ICML*, 2024.

[16] Y. Jin and E. J. Cand\`es. Selection by Prediction with Conformal p-values. *Journal of Machine Learning Research*, 2023.

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

[29] M. Bashari, A. Epstein, Y. Romano, and M. Sesia. Derandomized Novelty Detection with FDR Control via Conformal E-values. In *NeurIPS*, 2023.

[30] A. Marandon. Conformal Link Prediction for False Discovery Rate Control. *TEST*, 2024.

[31] I. Niles and A. Pease. Towards a Standard Upper Ontology. In *Formal Ontology in Information Systems (FOIS)*, 2001.

[32] G. A. Miller. WordNet: A Lexical Database for English. *Communications of the ACM*, 38(11):39--41, 1995.

[33] L. De Raedt, A. Kimmig, and H. Toivonen. ProbLog: A Probabilistic Prolog and Its Application in Link Discovery. In *IJCAI*, 2007.

[34] R. Manhaeve, S. Duman\v{c}i\'c, A. Kimmig, T. Demeester, and L. De Raedt. DeepProbLog: Neural Probabilistic Logic Programming. In *NeurIPS*, 2018.

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

--- Item 5 ---
id: art_ikjFm_faAe0x
type: experiment
title: 'CLUTRR Label-Free Knockoff+ FDR Gate: Calibration Diagonal, Power & Entrapment'
summary: >-
  This artifact executes the end-to-end label-free decoy-competition (knockoff+) FDR gate on the crisp-gold CLUTRR kinship
  anchor (190 docs: 40 pilot + 150 confirmatory), testing whether a label-free admission gate can control the false-discovery
  rate of LLM-extracted facts entering a symbolic layer. Pipeline (openai/gpt-4.1-nano via OpenRouter, isolated provenance-blinded
  scoring, persistent on-disk cache, $0.42 total spend << $10 cap, 1540 scored candidates): over-generation extraction (atomic
  + multi-hop bridge families), property-matched counterfactual decoys with non-entailment verification, deterministic entrapment
  items (r=1), and four scoring elicitations. The Phase-0 pilot selected the scorer by upper-tail AUC (verbalized, tail-AUC
  0.86 with bootstrap CI excluding 0.5, so the S0 separation precondition PASSED) and set alpha*=0.3; populability far exceeds
  the N_false_min=40 floor (bridge 175, atomic 118, pooled 293 genuine false candidates), so the diagonal is TESTABLE rather
  than untestable. Method vs baselines (implemented side-by-side in one pipeline to remove confounds): (1) OUR knockoff+ gate
  with canonical statistic W_i=sign(Z_i-Z~_i)*max(Z_i,Z~_i) and the Barber-Candes +1 data-dependent threshold; (2) PLAIN confidence-threshold
  baseline (decoy-free primary foil); (3) SWAP-decoy negative control. HEADLINE bridge diagonal (realized FDR vs target alpha,
  document-block bootstrap B=2000 CIs): the knockoff+ gate is CONSERVATIVELY calibrated, with realized FDR ~0.21 at alpha=0.2/0.3
  (n_admitted=56, 12 false) and ~0.25 at alpha=0.5 (n_admitted=113), staying at or below alpha+tau across the certified grid,
  whereas the plain confidence baseline is ANTI-CONSERVATIVE, with realized FDR rising 0.34->0.55 as alpha loosens. The single
  pre-registered primary disconfirmation at alpha*=0.3 returns NOT_DISCONFIRMED (realized 0.214, CI [0.12,0.33] not entirely
  above alpha*). Independent deterministic entrapment corroboration at alpha* gives N_T=56, N_E=10, FDP_combined=FDP_paired=0.30,
  agreeing with the gold realized FDR (3-way check). Overall calibration_verdict=CONFIRMED. Outputs: method.py (orchestrator)
  plus fdr_core.py, pipeline.py, llm_client.py, tests.py, and method_out.json (validates against exp_gen_sol_out: 1540 figure-ready
  candidate rows carrying per-item W, z_real, z_cf/z_swap/z_entrapment, gold label, predict_our_method and predict_baseline;
  top-level metadata holds the full per-family diagonal arrays, power table, populability counts, decoy-control tail diagnostics,
  entrapment estimators, and the disconfirmation verdict). full/mini/preview variants emitted and all four files are <100MB
  (no split needed). Scope: tests claim rows S0 (precondition) + S2 (diagonal) + S3 (entrapment) + power; deliberately excludes
  the Re-DocRED wedge, Prolog execution/trace-graphs, and the generator!=scorer ablation (separate experiments).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_Inu52CyA49Ys
type: experiment
title: Label-free decoy-competition FDR gate validated on CLUTRR crisp gold
summary: |-
  Executable validation of a LABEL-FREE decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into a symbolic layer without gold labels. Each extracted 'real' fact competes against a property-matched COUNTERFACTUAL decoy (same ordered entity pair, plausible-but-wrong relation, verified non-entailed against gold) plus a random type-matched swap control; a label-free confidence elicitation scores both in isolated, provenance-blinded, identical-template calls; canonical signed-max W_i + Barber-Candes knockoff+ threshold (eq 1.9) turn decoy wins into an FDR certificate. Run on the 190-doc CLUTRR crisp-gold anchor (40 pilot + 150 confirmatory) producing 1937 reals (633 TRUE, 1304 spontaneous FALSE extractor errors, 0 undecidable), each with a counterfactual decoy and a swap, scored under TWO elicitations (gpt-4.1-nano logprob softmax; K=5 self-consistency) plus a 4-config Generator!=Scorer ablation using a cross-family scorer (mistralai/ministral-8b-2512).

  HEADLINE (the gate's validity is ELICITATION-DEPENDENT): (1) S1 decoy signature - under single-token logprob confidence the LLM is overconfident in its OWN spontaneous errors, so counterfactual decoys are strongly anti-conservative (tail win-rate 0.34, 95% CI [0.32,0.37], KS p<1e-24); under K=5 self-consistency the decoys are EXCHANGEABLE (win-rate 0.482, CI [0.42,0.55] covers 0.5, KS p=0.48). The random-swap negative control is flagged anti-conservative under logprob (and by the offline synthetic self-test), validating diagnostic sensitivity. (2) Spontaneous-error tail match (the crux) - under self-consistency the counterfactual-decoy score distribution matches the genuine spontaneous-error distribution in the admission tail (top-25%/50% KS p=0.33/0.19, fail-to-reject) and differs sharply from the true-positive distribution (KS p~1e-40); figure-ready overlaid CDFs exported. (3) Generator!=Scorer de-circularization - exchangeability holds for ALL four (G,S) configs incl. G!=S (win-rate CIs cover 0.5; labeled-slice realized FDR 0.0 at alpha=0.2): verdict ROBUST, not a shared-model artifact. (4) Method vs purely-neural BASELINE - against crisp gold the decoy-FDR gate controls realized FDR <= nominal where it certifies (0.417 <= 0.5; conservative/zero-admit at stricter alpha), whereas the raw-confidence baseline admits 254-1758 facts at 45-65% realized FDR - the quantified hallucination problem the gate prevents.

  All p-values are document-block (cluster) bootstrap (B=2000) and Benjamini-Hochberg corrected (q=0.05; 42 tests, 27 reject). Cost: final cache-warm run $0.47, ~$1.05 total across gradual-scaling runs, hard cap $10 never neared (exact per-call USD from OpenRouter usage.cost; disk cache for free resumes). HONEST LIMITATIONS: knockoff+ is conservative on this signal (certifies admissions only at alpha=0.5 on 190 docs); the full-distribution crux match is borderline (a tail phenomenon); gpt-4.1-nano's genuine extraction is error-prone (atomic precision ~0.50, multi-hop accuracy ~0.20) - these real errors are the experimental signal, not a confound; self-consistency reduces sensitivity to the swap control.

  OUTPUTS for the paper writer: method_out.json (schema exp_gen_sol_out, validated) carries metadata.headline_finding/headline_verdict, elicitation_comparison, s1_decoy_signature_by_elicitation, spontaneous_error_match_by_elicitation (with figure_cdfs), generator_ne_scorer (verdict + validity_region_statement), baseline_vs_method_fdr_by_elicitation, bh_correction, extraction_quality; the 1937 examples each hold per-elicitation real/decoy/swap scores, W_i, and admission predictions. Companion files: fdr_stats.py (unit-tested statistical core), llm_client.py (async cached cost-capped OpenRouter client), make_figures.py + figures/fig1-4 (decoy signature, crux CDFs, FDR calibration, ablation), README.md, pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 7 ---
id: art_sHNuY68d4-Wh
type: experiment
title: >-
  Re-DocRED Operational Wedge: Decoy-Gating vs Plain Confidence Threshold at Matched Recall
summary: >-
  Operational-wedge experiment (S4) on the Re-DocRED anchor (152 confirmatory + 36 pilot-calibration Wikipedia documents).
  It answers a single load-bearing question for the label-free FDR-gating / neuro-symbolic text->logic hypothesis: at MATCHED
  RECALL, does ranking LLM-extracted atomic facts by the knockoff+ decoy-competition statistic W_i = max(Z_i, Z~_i)*sign(Z_i
  - Z~_i) admit a higher-precision, lower-hallucination set than ranking by the raw confidence Z_i (the PLAIN zero-label threshold
  foil)? method.py implements both systems side-by-side over an IDENTICAL candidate+alignment pool (only the gate differs),
  plus CoT, BM25-RAG, and a labeled Mohri-Hashimoto conformal back-off reference. All five systems are mapped into the SAME
  (title, P-code, head_id, tail_id) triple space by ONE fixed aligner (MiniLM top-8 shortlist + temp-0 LLM relation pick +
  three-tier entity linking) and scored by the official tuple-matching metric against human gold. Graded scoring uses the
  logprob yes-token probability (verbalized [0,1] fallback); decoys are property-matched DeepCoy-style counterfactuals that
  recombine the document's OWN entities into a non-entailed pairing (verified, regenerated up to 3x). method_out.json (schema
  exp_gen_sol_out) provides: figure-ready per-system PR curves; the matched-recall precision wedge delta(METHOD-PLAIN) across
  a recall grid with document-block bootstrap CIs (B=2000) and BH correction; multi-hop hallucinated-conclusion rate from
  a fixed pure-Python Datalog forward-chainer (rules listed); knockoff+ operating points over alpha in {0.05,0.1,0.2,0.3,0.5}
  with the 1/k floor; labeled conformal operating points (n_calibration_labels reported; the method uses 0); the mandatory
  alignment-error confound check (aligner self-error probe ~0.98 relation / ~0.99 entity-link on gold surface forms, plus
  perturbation sensitivity to uniform P-code noise 5/10/20%, an embedding-only aligner, and a stricter entity-link floor);
  decoy contamination rate; and a pre-registered verdict. Only RELATIVE comparisons are asserted (Re-DocRED residual false
  negatives depress recall and inflate hallucination counts equally for all systems). Result: a clean pre-registered OPERATIONAL
  DISCONFIRMATION -- with a well-calibrated logprob scorer the decoy competition does not beat (and is marginally worse than)
  plain thresholding at matched recall, i.e. 'thresholding-is-enough'. Pure-CPU, model openai/gpt-4.1-nano via OpenRouter,
  exact per-call cost metering with soft cap ~$3 and hard stop $10. Downstream (GEN_PAPER_TEXT) can use the PR/wedge/hallucination
  arrays and CIs directly as figures and the verdict + aligner-robustness numbers as the evidentiary core.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 8 ---
id: art_UBTwyePql8NQ
type: dataset
title: >-
  Application Anchor: 24 short legal/news/regulatory docs, triple gold + provenance
summary: |-
  The APPLICATION ANCHOR: one merged, schema-validated dataset (full_data_out.json, exp_sel_data_out schema) of 24 genuine, professionally-written short documents (native char_length 1239-3474, mean 2372), perfectly balanced 8 legal / 8 news / 8 regulatory, standardized to the SAME (head, relation, tail) triple space and coarse {PER,LOC,ORG,TIME,NUM,MISC} entity typing as the CLUTRR and Re-DocRED anchors (dependency research_out.json, Block C WordNet anchors). It is the genre-faithful real-document slice the next-iteration text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment depends on.

  PER EXAMPLE (each document = ONE example): input is a JSON string {doc_id, document_text (verbatim UTF-8), genre, source, char_length, entities:[{name, type in the 6-type set, char_span:[s,e]}]}; output is a JSON string {gold_atomic_facts:[{head, relation, tail, provenance_char_span:[s,e]}]}. Flat metadata: metadata_fold=genre (leave-one-genre-out), metadata_gold_quality (crisp|silver), metadata_source, metadata_license, metadata_relation_vocab, metadata_char_length, metadata_num_facts, metadata_num_entities, metadata_entity_types_fine (spaCy fine NER labels), plus per-source fields. datasets[] is grouped by SOURCE CORPUS: CUAD(8), Wikinews(8), GDPR(5), eCFR(3).

  GOLD (140 facts total, 3-15 per doc). LEGAL = CUAD v1 (CC BY 4.0), CRISP: triples mapped deterministically from human-annotated clause spans (has_title, has_party, agreement_date, effective_date, expiration_date, governed_by, renewal_term, liability_cap, contains_* clause types). NEWS = Wikinews (CC BY 2.5), SILVER: deterministic spaCy dependency SVO + 5W (action-verb predicates, occurred_on, affiliated_with). REGULATORY = GDPR/Reg(EU)2016/679 via EUR-Lex free reuse + eCFR (US public domain), SILVER: structural regex (has_title, grants_right, obligates, has_exception, cross_references, defined_as, requires). NO LLM is used anywhere in gold construction (preserves non-circularity for the next-iteration hallucination experiment); entity spans/types come only from offline spaCy NER + NLTK WordNet.

  GUARANTEES. Every entity char_span and fact provenance_char_span re-verified against document_text (946/946 entity spans exact; value-tail facts have tail as a substring of the provenance span; clause/label facts carry the annotated clause as evidence). 93.6% of fact endpoints link to the typed entities[] layer. Licenses are all free (CC BY 4.0 / CC BY 2.5 / EUR-Lex reuse / US public domain). Deterministic regeneration (seed 42, pinned tool versions) from the cached raw/ snapshot with no network: `python data.py` (or regenerate.sh) reproduces byte-identical output; build/verify_dataset.py re-checks all invariants.

  DATASET SELECTION: 4 source corpora chosen from 7 evaluated. Excluded REDFM (CC BY-SA-NC, NonCommercial), ContractNLI-HF (CC BY-NC-SA, NonCommercial), WebRED (free but sentence-level, not genre-faithful), LDC ACE/TACRED (restricted). Count is 4 (not 6) because the plan's hard free-license + genre-faithfulness gates legitimately exclude the rest while the binding deliverable (~24 balanced docs across 3 genres, crisp where possible) is fully met. Honest limitation: legal gold is crisp; news and regulatory gold are silver (rule/structure curation, high precision, partial recall) — carried per row by gold_quality. Variants: full_data_out.json (24 examples, all 4 groups), mini_data_out.json (3 per group = 12), preview_data_out.json (12, strings truncated to 200). full_data_out.json is 209K, far under the 100MB limit (no split). dataset_meta.json + schema/row_payload_schema.json + README.md + pyproject.toml (61 pinned deps) accompany it.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 9 ---
id: art_Cr6L9JpoewZi
type: research
title: >-
  Novelty-Delta, Upper-Ontology Grounding Recipe, and LLM-as-Probabilistic-Reasoner Design
summary: >-
  Source-traceable research closing three iteration-1 reviewer gaps for the decoy-gated neuro-symbolic text-to-logic pipeline,
  extending (not contradicting) Spec A (FDR gate) and Spec B (pipeline/typing/trace-graph). PART A: a five-dimension NOVELTY-DELTA
  table pinning six nearest conformal/FDR neighbors - Jin-Candes conformal selection [1], Li-Magesh-Veeravalli multiple-testing
  hallucination detection [2], COCOCO neuro-symbolic conformal sets [3], Bashari conformal-e-value novelty detection [4],
  Marandon/Blanchard conformal link-prediction FDR [5,6], Mohri-Hashimoto conformal factuality [7] - on {label requirement,
  unit certified, exchangeability mechanism, decoy?, FDR-vs-coverage}; all are LABELED and certify a model OUTPUT under assumed
  exchangeability, whereas OURS is label-free, certifies the INTERMEDIATE text->logic admission, uses engineered+tested decoy
  sign-flip, and controls FDR. Includes a paste-ready one-sentence delta, a 'not just conformal selection' rebuttal, and an
  honest adversarial result (no 2025-2026 preprint pre-empts the construction). PART B: OpenCyc honestly reported as discontinued
  (March 2017 [8,9], third-party-mirror-only [10]) and ResearchCyc as license-gated [8]; a concrete offline-first two-layer
  argument-typing recipe - WordNet hypernyms [11] anchored to SUMO upper-ontology classes via WordNetMappings30 (verified
  line: person -> &%Human=) [12,13,14], plus Wikidata P31/P279* [17] or offline YAGO 4.5 [15,16] instance typing, loadable
  with owlready2/SPARQLWrapper [18] - and a loss/sufficiency/descope-vs-defer justification arguing why typing-only usage
  cannot break the FDR guarantee (unlike ontology-constraint filtering). PART C: a concrete LLM-as-probabilistic-reasoner
  design - ProbLog primary (verified API: get_evaluatable().create_from(PrologString).evaluate() -> {Term:prob}; p::fact.;
  annotated disjunctions; query/evidence; explain/MPE proofs [19,20,21]; LFI weight learning [22]; aProbLog semirings [23];
  DeepProbLog neural-predicate precedent [24]) with Bousi~Prolog/FASILL as the fuzzy-unification alternative [25,26,27,28];
  a certificate->probabilistic-weight mapping table (p_i=calibrate(Z_i); gate-consistent shrinkage (1-alpha_hat)*p_i [default]
  or per-pair W_i margin weight; entrapment FDP-hat as consistency prior; full cert kept at the leaf); a probabilistic trace-graph
  export (reuse Spec-B JSON/Graphviz-DOT, add a 'prob' attribute per node/edge, marginal per derived node, certificate per
  leaf; janus-swi solve/2 fallback for the proof DAG); and the exact deterministic->probabilistic upgrade swap (janus query_once
  -> problog get_evaluatable/evaluate). Deliverables: research_out.json + research_report.md with 30 primary sources, tables,
  recipes, exact APIs, and a positioning note mapping each part to the named reviewer gaps.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 10 ---
id: art_sBLQqsdm3EIA
type: experiment
title: Self-consistency CLUTRR FDR-gate diagonal with decoy self-report disconfirmation
summary: |-
  Executable per-family realized-FDR-vs-target-alpha CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted CLUTRR kinship facts into a symbolic layer, scored under the diagnostic-VALIDATED K=5 SELF-CONSISTENCY elicitation (iter-2 counterfactual tail win-rate ~0.482). Method + baselines + controls run side-by-side in one pipeline (method.py): METHOD=counterfactual-decoy knockoff+ gate; BASELINE1=PLAIN raw-confidence threshold gate (purely-neural foil); BASELINE2=random in-doc SWAP-decoy knockoff (anti-conservative control); CONTRAST=the same diagonal under VERBALIZED confidence (discreteness/loose-target artifact); CORROBORATION=deterministic foreign-entity ENTRAPMENT FDP (Wen et al. 2025, r=1). Signed-max W_i + Barber-Candes knockoff+ threshold (eq 1.9), per-document rank-normalization over {reals U cf U swap}, document-block bootstrap CIs (B=2000), Benjamini-Hochberg q=0.05. Reuses iter-2 tested code (fdr_core.py, fdr_stats.py, llm_client.py with a read-only warm-start cache so the 190-doc prefix's scores hit the iter-2 cache; only new docs cost money).

  ITERATION-3 ADDITIONS (reviewer-driven): (A) self-consistency is the headline elicitation for the per-family diagonal; (B) every row surfaces the (target alpha, decoy_fdr_hat, realized FDR) TRIPLE plus a pre-registered SELF-REPORT disconfirmation (the gate's own decoy_fdr_hat is disconfirmed where it is anti-conservative vs realized beyond tau, EVEN when realized<alpha); (C) verbalized contrast on the SAME data with quantified discreteness/loose-target artifact notes; (D) an S1b difficulty LADDER L0..L4 (foreign-swap, in-doc swap, random-vocab, cf_2nd, primary-cf) scored under the SAME self-consistency to repair-or-bound the win-rate diagnostic; (E) foreign-entity entrapment at alpha* and alpha=0.5; (F) full crux match (tail fail-to-reject + full-distribution + tail-only decision-relevance justification); (G) a NEW paired-exchangeability diagnostic (cf win-rate over FALSE pairs) bridging the crux (marginal exchangeability) and the realized diagonal (paired competition); (H) Generator!=Scorer carried forward as SETTLED (ROBUST, no new budget); (I) BH across all validation tests; (J) the single primary-disconfirmation verdict under self-consistency on the populable multi_hop family.

  HEADLINE (this checkpoint, 40-doc smoke; the powered ~593-doc run is the final artifact): on the error-dense multi_hop family (extraction multi-hop accuracy ~0.17 so the family is ~80% genuine FALSE) the self-consistency knockoff+ gate is DISCONFIRMED at the tightest certified alpha* (realized FDR 1.0 with doc-block CI entirely above alpha*=0.5; decoy_fdr_hat=0.5 SELF-REPORT anti-conservative), while the crux is VALID (decoys distributionally exchangeable with genuine errors, distinct from true positives) — distributional exchangeability is NOT paired exchangeability. Generator!=Scorer ROBUST (carried forward). BH over 28 tests. Cost ~$0.07-0.2 (hard cap $10 never neared; exact per-call USD; disk cache for free resumes).

  OUTPUTS for the paper writer: method_out.json (schema exp_gen_sol_out, validated) carries metadata.primary_diagonal_self_consistency (per-family rows with the triple+CI+certified+swap+plain+self_report flag+paired_exchangeability), contrast_diagonal_verbalized (+artifact_notes), power_populability_table, s1b_difficulty_ladder (+verdict), crux_full_and_tail_self_consistency/_verbalized (KS/MW/AD/perm + figure_cdfs + decision-relevance), entrapment (alpha*/0.5), baseline_vs_method_self_consistency, generator_ne_scorer_carried_forward, bh_correction, primary_disconfirmation_verdict, reconciliation_narrative; the per-real examples hold self-consistency/verbalized Z, W_i and per-alpha admission predictions. Companion files: fdr_core.py, fdr_stats.py (unit-tested cores), llm_client.py, summarize.py, make-figures in method.py + figures/, README.md, data.py (regenerates the scaled corpus), pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 11 ---
id: art_vkfyOl2OQNVx
type: experiment
title: >-
  Decoy-gated text-to-logic hallucination control on the 24-doc legal/news/regulatory anchor
summary: |-
  Executes the goal's binding deliverable on the genre-faithful 24-doc application anchor (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver, 210 extracted reals: 42 TRUE / 51 FALSE / 117 UNDECIDABLE). One implementation (method.py) runs method + baselines + controls side-by-side: STAGE 1 open over-generating extraction (n=3 sample union, temp 0.7) + WordNet->SUMO typing (typing_sumo.py) + LLM relation alignment to per-genre gold vocab with an 'other:' escape + entity linking + crisp/silver labelling; STAGE 2 document-conditioned COUNTERFACTUAL decoys (contamination 0.057), type-matched swap control, deterministic ENTRAPMENT (r=1, 209 items), dual label-free elicitation scoring (single-token logprob softmax P(Yes) AND K=5 self-consistency), and the reused knockoff+ gate at every alpha {0.05,0.1,0.2,0.3,0.5} per genre x elicitation; STAGE 2b PRIMARY metric hallucinated-fact rate (gate vs RAW LLM) with a non-circular cross-family adjudicator (ministral-8b), document-block bootstrap CIs, regime tags, and silver lower/upper bounds; STAGE 2c matched-recall vs RAW/GATE/RAG(BM25)/CoT; STAGE 3 a pure-Python backward-chaining proof engine (kb_engine.py; SWI-Prolog/janus attempted, fell back) with hand-authored genre bridge rules and JSON+DOT trace-graphs whose every leaf carries provenance + decoy (W_i,T,alpha) + entrapment (FDP_hat,r) certificates; STAGE 4 BH correction + schema-valid output + 7 figures.

  HEADLINE / REGIME MAP (reported across the FULL grid, never obscured): under BOTH elicitations the gate certifies ONLY at alpha=0.5 on 24 docs (n_admitted<1/alpha below that -> 'uncertified' cells shown but vacuous; this matches the pre-registered portable-floor fallback). At the certified alpha=0.5, pooled gate hallucinated-fact rate is 0.183 (portable) / 0.178 (logprob) vs the alpha-invariant RAW 0.243 -- a ~25% relative reduction, but bootstrap CIs OVERLAP (0 of 40 cells reach CI separation at n=24), so the reduction is directional not significant. The gate's own decoy_fdr_hat >= realized FDR in every cell (0 self_report_anticonservative cells) -> here the self-report is CONSERVATIVE (contrast: logprob was anti-conservative on CLUTRR). The entrapment FDP_hat is high at alpha=0.5 (pooled 0.81), honestly flagging that alpha=0.5 admission is loose. Multi-hop: RAW-KB derives 23 conclusions at 0.48 corrupted-rate vs GATE-KB (alpha=0.5) 11 conclusions at 0.18 -- a clear drop in corrupted multi-hop conclusions. Adjudicator kappa vs legal crisp gold = 0.10 (< 0.4 threshold) so the judge is DROPPED and hallucination reported by gold-membership with silver bounds (the documented fallback; low kappa is partly because crisp CUAD gold itself has partial recall). Atomic precision/recall: legal 0.28/0.27 (crisp-restricted), news 0.29/0.18, regulatory 0.17/0.42.

  DELIVERABLES (all in workspace): method.py (+ reused fdr_stats.py, llm_client.py; new typing_sumo.py, kb_engine.py), method_out.json (426K, 210 rows, exp_gen_sol_out schema-valid) with metadata.hallucination_grid (per genre x elicitation x alpha: gate/raw rate + CIs, decoy_fdr_hat, realized_fdr, entrapment FDP_hat, certified, k_floor, regime_tag, silver_bounds, self_report_anticonservative), s1_decoy_signature, matched_recall_curves (4 systems), extraction_quality, multihop_corruption, adjudicator_validation, trace_graphs, bh_correction; full/mini/preview variants; trace_graphs/ (6 JSON + 6 DOT, >=2 per genre, real 2-hop derivations e.g. obligation_with_exception with per-leaf certificates); figures/ (fig1 hallucination grid, fig2 self-report vs realized FDR, fig3 matched-recall, fig4 trace-graph per genre, fig5 multi-hop corruption). CPU-only; total cost $0.305 (soft cap $3, hard stop $10); offline selftest gates the paid run; on-disk cache makes re-runs free. Honest scope: legal crisp / news+reg silver (bracketed), portable certifies only at alpha=0.5, gate reduction directional (CI-overlapping) at this sample size -- the contribution is the auditable pipeline + the explicit regime map + the multi-hop corruption-propagation result.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 12 ---
id: art_RZC2468yZ-Jh
type: experiment
title: Re-DocRED decoy-gating wedge reframed as a gold-free regime-diagnostic
summary: >-
  P3 scales the prior Re-DocRED operational wedge from 36 to the full 152 confirmatory + 36 pilot documents (resume-safe extraction,
  total new spend $1.08 of a $10 cap) and reframes the result as a NOVEL label-free regime-diagnostic. Core comparison (controlled,
  same pipeline): METHOD = a label-free decoy-competition FDR gate (knockoff+ statistic W_i = sign(Z_i - Z~_i)*max(Z_i, Z~_i))
  vs the load-bearing PLAIN foil (rank by raw confidence Z_i), with CoT, BM25-RAG and a labeled Mohri-Hashimoto conformal
  back-off (CONF) as reference comparators, all mapped into the identical (title, P-code, head_id, tail_id) triple space by
  one fixed MiniLM-shortlist + temp-0 LLM aligner and scored by the official tuple-matching metric vs human gold. RESULT (pre-registered
  DISCONFIRMATION, scope-honest): at matched recall the wedge collapses to 'thresholding-is-enough' — across a 25-point recall
  grid no point shows a METHOD-over-PLAIN precision gain with document-block-bootstrap (B=2000) CI entirely > 0. The verdict
  embeds the true n and ceiling AT the claim: 'disconfirmed at recall <= 0.075 on 152 docs' (metadata.scope = {n_docs_used:152,
  n_docs_requested:152, recall_ceiling:0.075}); the fairness invariant holds exactly (METHOD and PLAIN share an identical
  candidate+alignment pool -> identical max recall), and the null delta sign persists under P-code-noise / embedding-only-aligner
  / strict-EL perturbations. Four reviewer-MAJOR fixes are implemented: (1) SCOPE honesty as above; (2) COMPARATORS completed-or-dropped
  — the matched-recall grid floor is relaxed to the lowest positive max_recall (0.034) so recall-limited CoT/RAG yield >=1
  evaluable point; all five systems PARTICIPATE (dropped_comparators={}), no all-null baseline is listed; (3) MULTI-HOP comparison
  POWERED, not underpowered — six extra gold-justified Wikidata inverse rules (P22/P25->P40, P361<->P527, P131<->P150) densify
  forward-chained conclusions to n_derived=267 (METHOD)=267 (PLAIN), >> the power_target of 100, delta CI width 0.027, underpowered=false;
  the hallucinated-conclusion rate is ~0.79 for both systems (delta -0.004, CI spans 0) — the gate does not reduce hallucination
  here; (4) the NOVEL label-free REGIME-DIAGNOSTIC (regime.py, ZERO new API calls, NO gold) that PREDICTS the null wedge from
  cached Z/Z~/W/self-consistency via four signals: A tail decoy win-rate (knockoff-admitted tail 0.005 << 0.5 -> decoys too
  easy), B spontaneous-error CDF match (decoy score mean 0.165 vs low-self-consistency real mean 0.857; KS/Mann-Whitney/permutation
  all reject -> too easy), C W-vs-Z ranking divergence (frac(W==Z)=0.94, admitted-set Spearman rho=0.99 -> the gate keeps
  and orders the same facts as the plain threshold -> mechanically null), D base-scorer calibration (AUC(Z, self-consistency)=0.60).
  A 2-axis map (decoy exchangeability x base-scorer calibration) emits predicted_regime='GATE REDUNDANT' and predicted_wedge_sign='null',
  which is then VALIDATED against the realized wedge: prediction_correct=true. A cross-anchor panel places Re-DocRED beside
  P1's CLUTRR regimes (winrate 0.045->null, 0.103/0.34->negative, 0.482->positive) and states+tests the unifying principle
  that gate value is genuinely 2-axis (positive only with exchangeable decoys; at the too-easy end the sign splits by calibration
  into redundant vs anti-conservative), honestly noting it is a 2-anchor illustration, not a powered regression. The artifact
  also emits 8 human-auditable multi-hop proof traces (rule + premises -> conclusion, names resolved) and four paper-ready
  figures (matched-recall wedge, regime map, W-vs-Z signal, decoy diagnostics). All comparisons are RELATIVE-only (Re-DocRED
  residual false negatives depress recall and inflate hallucination for every system equally). Deliverables (schema exp_gen_sol_out,
  all validated): method.py orchestrator + run_analysis; regime.py (the gold-free diagnostic); analyze.py (aligner, official
  metric, knockoff+/conformal operating points, document-block bootstrap, traced forward-chaining); extract.py, prompts.py,
  llm.py, common.py, figures.py, summarize.py; method_out.json (619 KB) with full/mini/preview variants (all < 100 MB, no
  split); figures/. Downstream paper text can quote the disconfirmation precisely and lead with the regime-diagnostic as the
  substantive, novel, interpretable contribution.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) The 'one coherent story' does not hold across the two CLUTRR experiments. The headline calibration diagonal (S2, the pre-registered disconfirmation) is computed under the VERBALIZED elicitation (art_ikjFm_faAe0x), whose counterfactual decoy tail win-rate is 0.103 on the bridge family (0.167 in the pilot) — by the paper's own diagnostic logic the strongly ANTI-CONSERVATIVE regime ('decoys too easy'). Yet this exact diagonal is reported as 'conservatively calibrated' and the Discussion attributes the FDR reduction to 'an aggregation elicitation.' The exchangeable regime (win-rate 0.482) is established only in a SEPARATE experiment (art_Inu52CyA49Ys) under K=5 self-consistency, where the gate certifies admissions ONLY at α=0.5. So the diagnostic the paper sells as 'telling the practitioner which regime they are in' gives the WRONG signal for the headline result. Reinforcing this, the gate's own FDR estimate is anti-conservative on the diagonal (decoy_fdr_hat=0.125 vs realized 0.214 at α=0.3), and at α=0.2 the realized FDR (0.214) EXCEEDS the nominal target (0.2). The conservative-at-α=0.3 outcome looks driven by a loose target plus verbalized-score discreteness, not by demonstrated exchangeability.
  Action: Re-run the headline CLUTRR diagonal under the self-consistency elicitation that the win-rate diagnostic actually validates, and make THAT the primary diagonal; or, if verbalized is kept, explicitly explain and quantify the discreteness/loose-target mechanism, report that the gate's FDR estimate is anti-conservative, and acknowledge the α=0.2 violation. Align the Discussion sentence ('the decoy competition under an aggregation elicitation brings realized FDR down') with the elicitation that actually produced the CLUTRR diagonal.
- [MAJOR] (evidence) Two specific claims in the paper are contradicted by their own artifacts. (a) Section 6.3 states that under K=5 self-consistency 'the random-swap control remains correctly flagged as too easy.' The artifact (art_Inu52CyA49Ys, portable_full) shows diagnostic_sensitivity_ok=FALSE, with the random-swap tail win-rate at 0.473 and its CI covering 0.5 — i.e., in the valid regime the diagnostic LOSES the ability to flag too-easy decoys (the experiment's own limitations note 'self-consistency reduces sensitivity to the swap control'). This is the opposite of the paper's claim and directly weakens the 'self-detecting diagnostic' contribution. (b) The spontaneous-error 'crux' match is reported using only the tail regions (top-25%/50% KS p=0.33/0.19, fail-to-reject), while the FULL-distribution test is REJECTED (KS p=0.051, MW p=0.036, AD p=0.041, permutation p=0.029; artifact verdict 'GAP:decoys_too_easy(anti-conservative)'). Reporting only the favorable tail without the full-distribution rejection is selective.
  Action: Correct (a) to state that the swap control is flagged anti-conservative only under logprob, NOT under self-consistency, and discuss the loss of diagnostic sensitivity in the valid regime as a limitation (it materially qualifies the 'diagnostic tells you when to trust the gate' contribution). For (b), report the full-distribution rejection alongside the tail fail-to-reject and justify explicitly why the admission tail is the decision-relevant region.
- [MAJOR] (evidence) The Re-DocRED operational disconfirmation (S4) is real but considerably narrower and weaker than the manuscript implies. The artifact (art_sHNuY68d4-Wh) used n_docs_used=36, not the 152 confirmatory documents the Experimental Setup implies (split_role is 'confirmatory' but only 36 docs were scored). The wedge is evaluated only at very low recall (max ≤0.086). Two of the four listed comparators — CoT and RAG — max out at recall 0.049 and 0.041 respectively, below the 0.05 grid start, so their precision is ALL NULL on the comparison grid and they do not actually participate in the wedge despite being presented as comparators. The multi-hop hallucinated-conclusion comparison rests on ~20–24 derived conclusions per system (METHOD 12/24, PLAIN 11/23, CONF 9/18) with per-system CIs spanning [0.29, 1.0] — essentially no statistical power.
  Action: State the true number of documents used and the recall ceiling prominently at the point of the S4 claim. Either complete CoT/RAG to a comparable operating point or remove them from the comparator list for the wedge (do not list baselines that produced no comparable output). Either scale the multi-hop hallucination comparison to enough derived conclusions to have power, or explicitly label it underpowered. Frame the disconfirmation precisely as 'at ≤8.6% recall on 36 documents.'
- [MAJOR] (scope) The target application is still not evaluated, so the goal's hard requirement — a quantified hallucination reduction on short professionally-written legal/news/regulatory documents (~3000 chars) with auditable trace-graphs — is not demonstrated where it is claimed. The 24-document application anchor (art_UBTwyePql8NQ) is built and validated but the hallucination-reduction run is NOT executed. All quantitative results live on CLUTRR (synthetic templated kinship, ~355 chars) and Re-DocRED (Wikipedia paragraphs). The S6 'quantified hallucination reduction' itself holds only in one narrow cell: under self-consistency at α=0.5 (319 facts at realized FDR 0.417 vs baseline 0.453); at every stricter α the gate admits ZERO, and under the logprob elicitation the method is strictly WORSE than the plain baseline at every α (e.g., 0.555 vs 0.228 at α=0.3). OpenCyc grounding and probabilistic (ProbLog) reasoning remain descoped.
  Action: Execute the already-built application hallucination-reduction run on the 24-document anchor and export at least a few deterministic trace-graphs (budget is trivial — ~$1.24 of $10 spent so far); report it as the headline application result. Present S6 with both elicitations side by side and across all α so the regime-dependence (worse-than-baseline under logprob; vacuous below α=0.5 under self-consistency) is not obscured. If the run cannot be completed, re-scope all 'application' framing to the genres actually evaluated.
- [MINOR] (rigor) Several quantitative claims are slightly overstated relative to the artifacts. (a) 'Conservatively calibrated across the certified grid' is violated at α=0.2, where realized FDR 0.214 > 0.2 (same 56 admitted as α=0.3 because the threshold grid is discrete). (b) The pilot selected the verbalized elicitation (tail AUC 0.861) over DINCO (tail AUC 0.871, which is higher) with no stated selection rationale. (c) The three-way entrapment 'mutual consistency' holds only at α*=0.3; at α=0.5 the entrapment FDP (0.420) diverges from the gold FDR (0.248) and the artifact records agree_realized=false.
  Action: Reword to 'realized FDR ≤ α for α≥0.3, marginally exceeding at α=0.2.' State the explicit elicitation-selection criterion and why verbalized was chosen over the higher-AUC DINCO. Restrict entrapment-agreement claims to α* and note the divergence at α=0.5.
- [MINOR] (clarity) The figures appear only as bare [FIGURE:fig1]–[fig5] markers with no captions or descriptions in the manuscript body, so a reader cannot assess what each load-bearing figure (the calibration diagonal, the matched-recall wedge, the elicitation-dependence panels) actually communicates. This was raised in the previous round and is still unaddressed.
  Action: Add a complete caption plus a short description for every figure. Ensure the realized-FDR-vs-α diagonal figure marks the 1/k floor and bootstrap CIs and visibly distinguishes the gate from the plain and swap baselines, and that the wedge figure shows all participating systems with CIs at the matched operating point.
</previous_review>

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

### [3] HUMAN-USER prompt · 2026-06-16 10:14:34 UTC

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

### [4] ASSISTANT · 2026-06-16 10:14:54 UTC

```
I'll review this paper carefully, verifying claims against the artifacts. Let me start by examining the key experimental outputs.
```

### [5] TOOL CALL — Bash · 2026-06-16 10:14:54 UTC

```
List iteration-3 experiment artifact directories:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art && ls -la gen_art_experiment_1 gen_art_experiment_2 gen_art_experiment_3 2>/dev/null
```

### [6] TOOL RESULT — Bash · 2026-06-16 10:14:54 UTC

```
{"stdout": "gen_art_experiment_1:\ntotal 25351\ndrwxr-xr-x 9 root root 2045597 Jun 16 09:50 .\ndrwxr-xr-x 5 root root 3000566 Jun 16 08:46 ..\n-rw-r--r-- 1 root root 4527737 Jun 16 09:56 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4541 Jun 16 09:50 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 5 root root 2027181 Jun 16 08:56 .venv\n-rw-r--r-- 1 root root    3728 Jun 16 09:17 README.md\ndrwxr-xr-x 2 root root 1016762 Jun 16 09:41 __pycache__\ndrwxr-xr-x 2 root root 2001436 Jun 16 09:56 cache\ndrwxr-xr-x 2 root root       1 Jun 16 08:51 checkpoints\n-rw-r--r-- 1 root root   20673 Jun 16 08:55 data.py\n-rw-r--r-- 1 root root   13715 Jun 16 08:51 fdr_core.py\n-rw-r--r-- 1 root root   14729 Jun 16 08:51 fdr_stats.py\ndrwxr-xr-x 2 root root 1011250 Jun 16 09:33 figures\n-rw-r--r-- 1 root root 3833126 Jun 16 08:57 full_data_out.json\n-rw-r--r-- 1 root root 1096458 Jun 16 08:51 full_data_out_190.json\n-rw-r--r-- 1 root root  540949 Jun 16 09:49 full_method_out.json\n-rw-r--r-- 1 root root   11287 Jun 16 08:59 llm_client.py\ndrwxr-xr-x 2 root root 2000914 Jun 16 09:36 logs\n-rw-r--r-- 1 root root   91285 Jun 16 09:41 method.py\n-rw-r--r-- 1 root root  540955 Jun 16 09:33 method_out.json\n-rw-r--r-- 1 root root   85011 Jun 16 09:49 mini_method_out.json\n-rw-r--r-- 1 root root   44062 Jun 16 09:49 preview_method_out.json\n-rw-r--r-- 1 root root     458 Jun 16 09:49 pyproject.toml\n-rw-r--r-- 1 root root     452 Jun 16 08:51 pyproject_data.toml\n-rw-r--r-- 1 root root    3802 Jun 16 09:39 summarize.py\ndrwxr-xr-x 4 root root 2015004 Jun 16 08:51 temp\n\ngen_art_experiment_2:\ntotal 17583\ndrwxr-xr-x 9 root root 2033846 Jun 16 09:28 .\ndrwxr-xr-x 5 root root 3000566 Jun 16 08:46 ..\ndrwxr-xr-x 2 root root       1 Jun 16 09:29 .claude\n-rw-r--r-- 1 root root 2735726 Jun 16 09:29 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4610 Jun 16 09:28 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 6 root root 2032860 Jun 16 08:54 .venv\n-rw-r--r-- 1 root root    3918 Jun 16 09:22 README.md\ndrwxr-xr-x 2 root root 1007519 Jun 16 09:20 __pycache__\ndrwxr-xr-x 2 root root 2000212 Jun 16 09:25 cache\n-rw-r--r-- 1 root root   14729 Jun 16 08:52 fdr_stats.py\ndrwxr-xr-x 2 root root 1058290 Jun 16 09:27 figures\n-rw-r--r-- 1 root root  435519 Jun 16 09:27 full_method_out.json\n-rw-r--r-- 1 root root   11390 Jun 16 09:00 kb_engine.py\n-rw-r--r-- 1 root root   10217 Jun 16 08:52 llm_client.py\ndrwxr-xr-x 2 root root 2000336 Jun 16 09:18 logs\n-rw-r--r-- 1 root root   10040 Jun 16 09:20 make_figures.py\n-rw-r--r-- 1 root root   80044 Jun 16 09:17 method.py\n-rw-r--r-- 1 root root  435677 Jun 16 09:25 method_out.json\n-rw-r--r-- 1 root root   80466 Jun 16 09:27 mini_method_out.json\n-rw-r--r-- 1 root root   31689 Jun 16 09:27 preview_method_out.json\n-rw-r--r-- 1 root root     586 Jun 16 08:52 pyproject.toml\ndrwxr-xr-x 2 root root 1005174 Jun 16 09:25 trace_graphs\n-rw-r--r-- 1 root root    5722 Jun 16 08:57 typing_sumo.py\n\ngen_art_experiment_3:\ntotal 20311\ndrwxr-xr-x 8 root root 3000489 Jun 16 09:38 .\ndrwxr-xr-x 5 root root 3000566 Jun 16 08:46 ..\n-rw-r--r-- 1 root root 3204560 Jun 16 09:39 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4867 Jun 16 09:38 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 5 root root 3000488 Jun 16 08:53 .venv\n-rw-r--r-- 1 root root    7053 Jun 16 09:08 README.md\ndrwxr-xr-x 2 root root 1016906 Jun 16 09:36 __pycache__\n-rw-r--r-- 1 root root   19337 Jun 16 09:19 analyze.py\ndrwxr-xr-x 2 root root 1031267 Jun 16 08:51 cache\ndrwxr-xr-x 5 root root 2000589 Jun 16 08:51 checkpoints\n-rw-r--r-- 1 root root   17838 Jun 16 08:52 common.py\n-rw-r--r-- 1 root root   11116 Jun 16 08:51 extract.py\ndrwxr-xr-x 2 root root 1022630 Jun 16 09:24 figures\n-rw-r--r-- 1 root root    7424 Jun 16 09:21 figures.py\n-rw-r--r-- 1 root root  633695 Jun 16 09:37 full_method_out.json\n-rw-r--r-- 1 root root    4001 Jun 16 08:51 llm.py\ndrwxr-xr-x 2 root root 2000264 Jun 16 09:24 logs\n-rw-r--r-- 1 root root   35815 Jun 16 09:20 method.py\n-rw-r--r-- 1 root root  634640 Jun 16 09:36 method_out.json\n-rw-r--r-- 1 root root   73536 Jun 16 09:37 mini_method_out.json\n-rw-r--r-- 1 root root   26539 Jun 16 09:37 preview_method_out.json\n-rw-r--r-- 1 root root    8039 Jun 16 08:51 prompts.py\n-rw-r--r-- 1 root root     940 Jun 16 09:33 pyproject.toml\n-rw-r--r-- 1 root root   23246 Jun 16 09:23 regime.py\n-rw-r--r-- 1 root root    4686 Jun 16 09:16 summarize.py\n-rw-r--r-- 1 root root    2134 Jun 16 08:51 test_plumbing.py", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] TOOL CALL — Bash · 2026-06-16 10:14:54 UTC

```
Check user uploads folder:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads 2>/dev/null && ls -la || echo "no user_uploads"
```

### [8] TOOL RESULT — Bash · 2026-06-16 10:14:54 UTC

```
{"stdout": "total 2931\ndrwxr-xr-x  2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 14 root root 3000809 Jun 16 04:40 ..", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] ASSISTANT · 2026-06-16 10:14:56 UTC

```
Let me extract the key metadata from the three iteration-3 experiments to verify the paper's central claims.
```

### [10] TOOL CALL — Bash · 2026-06-16 10:14:56 UTC

```
List metadata keys for CLUTRR self-consistency diagonal experiment:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('TOP-LEVEL METADATA KEYS:')
for k in m.keys(): print(' ', k)
"
```

### [11] TOOL RESULT — Bash · 2026-06-16 10:14:56 UTC

```
{"stdout": "TOP-LEVEL METADATA KEYS:\n  method_name\n  headline_elicitation\n  headline_verdict\n  description\n  elicitation_selection_rationale\n  models\n  hyperparameters\n  dataset_counts\n  extraction_quality\n  primary_diagonal_self_consistency\n  contrast_diagonal_verbalized\n  power_populability_table\n  s1b_difficulty_ladder\n  crux_full_and_tail_self_consistency\n  crux_full_and_tail_verbalized\n  entrapment\n  baseline_vs_method_self_consistency\n  generator_ne_scorer_carried_forward\n  bh_correction\n  primary_disconfirmation_verdict\n  reconciliation_narrative\n  runtime\n  cost_trace_path\n  interpretation", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [12] TOOL CALL — Bash · 2026-06-16 10:15:00 UTC

```
Read headline verdict and primary disconfirmation:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== headline_verdict ==='); print(json.dumps(m['headline_verdict'],indent=1)[:1500])
print('=== primary_disconfirmation_verdict ==='); print(json.dumps(m['primary_disconfirmation_verdict'],indent=1)[:2500])
"
```

### [13] TOOL RESULT — Bash · 2026-06-16 10:15:00 UTC

```
{"stdout": "=== headline_verdict ===\n\"DISCONFIRMED\"\n=== primary_disconfirmation_verdict ===\n{\n \"family\": \"multi_hop\",\n \"alpha_star\": 0.5,\n \"tau\": 0.05,\n \"realized_fdr\": 1.0,\n \"ci\": [\n  0.661594,\n  1.0\n ],\n \"decoy_fdr_hat\": 0.5,\n \"calibration_disconfirmed\": true,\n \"self_report_disconfirmed\": true,\n \"verdict\": \"DISCONFIRMED\",\n \"reason\": \"realized FDR 1.0 > alpha*+tau (0.5+0.05) AND doc-block CI [0.661594,1.0] lies entirely above alpha*=0.5.\"\n}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] ASSISTANT · 2026-06-16 10:15:04 UTC

```
The central disconfirmation matches the paper. Let me verify the diagonal details, populability, and the atomic family numbers.
```

### [15] TOOL CALL — Bash · 2026-06-16 10:15:04 UTC

```
Read primary self-consistency diagonal details:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== primary_diagonal_self_consistency ==='); print(json.dumps(m['primary_diagonal_self_consistency'],indent=1)[:3500])
"
```

### [16] TOOL RESULT — Bash · 2026-06-16 10:15:04 UTC

```
{"stdout": "=== primary_diagonal_self_consistency ===\n{\n \"atomic\": {\n  \"family\": \"atomic\",\n  \"rows\": [\n   {\n    \"target_alpha\": 0.05,\n    \"decoy_fdr_hat\": null,\n    \"realized_fdr\": null,\n    \"triple_alpha_estimate_realized\": [\n     0.05,\n     null,\n     null\n    ],\n    \"ci_low\": 0.261905,\n    \"ci_high\": 0.261905,\n    \"n_admitted\": 0,\n    \"n_false_admitted\": 0,\n    \"self_report_anti_conservative\": false,\n    \"k_floor\": 20,\n    \"certified\": false,\n    \"populable\": true,\n    \"swap_realized_fdr\": null,\n    \"swap_n_admitted\": 0,\n    \"plain_realized_fdr\": 0.172414,\n    \"plain_n_admitted\": 29,\n    \"plain_est_fdr\": 0.048966\n   },\n   {\n    \"target_alpha\": 0.1,\n    \"decoy_fdr_hat\": null,\n    \"realized_fdr\": null,\n    \"triple_alpha_estimate_realized\": [\n     0.1,\n     null,\n     null\n    ],\n    \"ci_low\": 0.18125,\n    \"ci_high\": 0.492563,\n    \"n_admitted\": 0,\n    \"n_false_admitted\": 0,\n    \"self_report_anti_conservative\": false,\n    \"k_floor\": 10,\n    \"certified\": false,\n    \"populable\": true,\n    \"swap_realized_fdr\": null,\n    \"swap_n_admitted\": 0,\n    \"plain_realized_fdr\": 0.229508,\n    \"plain_n_admitted\": 61,\n    \"plain_est_fdr\": 0.1\n   },\n   {\n    \"target_alpha\": 0.2,\n    \"decoy_fdr_hat\": null,\n    \"realized_fdr\": null,\n    \"triple_alpha_estimate_realized\": [\n     0.2,\n     null,\n     null\n    ],\n    \"ci_low\": 0.239727,\n    \"ci_high\": 0.503639,\n    \"n_admitted\": 0,\n    \"n_false_admitted\": 0,\n    \"self_report_anti_conservative\": false,\n    \"k_floor\": 5,\n    \"certified\": false,\n    \"populable\": true,\n    \"swap_realized_fdr\": null,\n    \"swap_n_admitted\": 0,\n    \"plain_realized_fdr\": 0.37234,\n    \"plain_n_admitted\": 94,\n    \"plain_est_fdr\": 0.198191\n   },\n   {\n    \"target_alpha\": 0.3,\n    \"decoy_fdr_hat\": 0.278689,\n    \"realized_fdr\": 0.377049,\n    \"triple_alpha_estimate_realized\": [\n     0.3,\n     0.278689,\n     0.377049\n    ],\n    \"ci_low\": 0.246271,\n    \"ci_high\": 0.496983,\n    \"n_admitted\": 61,\n    \"n_false_admitted\": 23,\n    \"self_report_anti_conservative\": true,\n    \"k_floor\": 4,\n    \"certified\": true,\n    \"populable\": true,\n    \"swap_realized_fdr\": null,\n    \"swap_n_admitted\": 0,\n    \"plain_realized_fdr\": 0.429688,\n    \"plain_n_admitted\": 128,\n    \"plain_est_fdr\": 0.297266\n   },\n   {\n    \"target_alpha\": 0.5,\n    \"decoy_fdr_hat\": 0.491379,\n    \"realized_fdr\": 0.422414,\n    \"triple_alpha_estimate_realized\": [\n     0.5,\n     0.491379,\n     0.422414\n    ],\n    \"ci_low\": 0.274127,\n    \"ci_high\": 0.531399,\n    \"n_admitted\": 116,\n    \"n_false_admitted\": 49,\n    \"self_report_anti_conservative\": false,\n    \"k_floor\": 2,\n    \"certified\": true,\n    \"populable\": true,\n    \"swap_realized_fdr\": 0.153846,\n    \"swap_n_admitted\": 13,\n    \"plain_realized_fdr\": 0.545455,\n    \"plain_n_admitted\": 209,\n    \"plain_est_fdr\": 0.499043\n   }\n  ],\n  \"n_pos\": 136,\n  \"n_pairs\": 224,\n  \"n_true_total\": 95,\n  \"n_false_total\": 129,\n  \"populable\": true,\n  \"reachable_alpha_floor\": 0.3,\n  \"alpha_star_permissive\": 0.5\n },\n \"multi_hop\": {\n  \"family\": \"multi_hop\",\n  \"rows\": [\n   {\n    \"target_alpha\": 0.05,\n    \"decoy_fdr_hat\": null,\n    \"realized_fdr\": null,\n    \"triple_alpha_estimate_realized\": [\n     0.05,\n     null,\n     null\n    ],\n    \"ci_low\": 0.782609,\n    \"ci_high\": 0.782609,\n    \"n_admitted\": 0,\n    \"n_false_admitted\": 0,\n    \"self_report_anti_conservative\": false,\n    \"k_floor\": 20,\n    \"certified\": false,\n    \"populable\": true,\n    \"swap_realized_fdr\": null,\n    \"swap_n_admitted\": 0,\n    \"plain_realized_fdr\": 0.8,\n    \"plain_n_admitted\": 30,\n    \"plain_est_fdr\": 0.049\n   },\n   {\n    \"target_alpha\": 0.1,\n    \"decoy_fdr_hat\"", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] TOOL CALL — Bash · 2026-06-16 10:15:18 UTC

```
Read multi-hop diagonal rows and dataset counts:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
mh=m['primary_diagonal_self_consistency']['multi_hop']
print('multi_hop n_pos/n_pairs/n_true/n_false:', mh['n_pos'], mh['n_pairs'], mh['n_true_total'], mh['n_false_total'])
print('reachable_alpha_floor:', mh['reachable_alpha_floor'], 'alpha_star:', mh['alpha_star_permissive'])
for r in mh['rows']:
    print(' a=%s adm=%s false=%s realFDR=%s fdrhat=%s cert=%s CI=[%s,%s] plain_adm=%s plain_fdr=%s'%(
      r['target_alpha'], r['n_admitted'], r['n_false_admitted'], r['realized_fdr'], r['decoy_fdr_hat'], r['certified'],
      r.get('ci_low'), r.get('ci_high'), r['plain_n_admitted'], r['plain_realized_fdr']))
print()
print('dataset_counts:', json.dumps(m['dataset_counts'],indent=1))
print('extraction_quality:', json.dumps(m['extraction_quality'],indent=1)[:800])
"
```

### [18] TOOL RESULT — Bash · 2026-06-16 10:15:18 UTC

```
{"stdout": "multi_hop n_pos/n_pairs/n_true/n_false: 109 186 28 158\nreachable_alpha_floor: 0.5 alpha_star: 0.5\n a=0.05 adm=0 false=0 realFDR=None fdrhat=None cert=False CI=[0.782609,0.782609] plain_adm=30 plain_fdr=0.8\n a=0.1 adm=0 false=0 realFDR=None fdrhat=None cert=False CI=[0.749565,1.0] plain_adm=49 plain_fdr=0.836735\n a=0.2 adm=0 false=0 realFDR=None fdrhat=None cert=False CI=[0.695937,1.0] plain_adm=79 plain_fdr=0.848101\n a=0.3 adm=0 false=0 realFDR=None fdrhat=None cert=False CI=[0.666667,1.0] plain_adm=109 plain_fdr=0.87156\n a=0.5 adm=12 false=12 realFDR=1.0 fdrhat=0.5 cert=True CI=[0.661594,1.0] plain_adm=179 plain_fdr=0.843575\n\ndataset_counts: {\n \"n_docs\": 40,\n \"n_pilot\": 0,\n \"n_reals\": 410,\n \"n_true\": 123,\n \"n_spont_false\": 287,\n \"n_undecidable\": 0,\n \"n_spont_false_atomic\": 129,\n \"n_spont_false_multi_hop\": 158,\n \"atomic_populable\": true,\n \"multi_hop_populable\": true,\n \"contamination_rate_decoys\": 0.08385481852315395,\n \"light_mode\": false\n}\nextraction_quality: {\n \"atomic_precision\": 0.5378787878787878,\n \"atomic_recall\": 0.10770833333333334,\n \"multihop_relation_accuracy\": 0.16852869352869354,\n \"note\": \"atomic P/R from free extraction; multi-hop accuracy from forced per-pair relation prediction (CLUTRR query format)\"\n}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [19] ASSISTANT · 2026-06-16 10:15:31 UTC

```
All CLUTRR diagonal numbers match. Now let me verify the crux (S1) full-distribution and tail tests — the previous review flagged the full-distribution test was rejected.
```

### [20] TOOL CALL — Bash · 2026-06-16 10:15:31 UTC

```
Read crux full and tail self-consistency tests:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== crux_full_and_tail_self_consistency ===')
print(json.dumps(m['crux_full_and_tail_self_consistency'],indent=1)[:3000])
"
```

### [21] TOOL RESULT — Bash · 2026-06-16 10:15:31 UTC

```
{"stdout": "=== crux_full_and_tail_self_consistency ===\n{\n \"regions\": {\n  \"full\": {\n   \"n_decoy\": 410,\n   \"n_spont\": 287,\n   \"n_truepos\": 123,\n   \"decoy_vs_spont\": {\n    \"ks_p\": 0.05757416893181091,\n    \"mw_p\": 0.06122248829308577,\n    \"ad_p\": 0.06070176691272408,\n    \"perm_meandiff\": -0.04299697277861475,\n    \"perm_p\": 0.05973506623344164\n   },\n   \"decoy_vs_truepos\": {\n    \"ks_p\": 4.761867353120533e-09,\n    \"mw_p\": 3.66468215698587e-12\n   },\n   \"gap\": {\n    \"ks_sup\": 0.10139372822299651,\n    \"wasserstein\": 0.043630155706085194,\n    \"mean_diff\": -0.04299697277861475,\n    \"cliffs_delta\": -0.08324126795274922,\n    \"n_decoy\": 410,\n    \"n_other\": 287\n   },\n   \"verdict\": \"VALID\"\n  },\n  \"top50pct\": {\n   \"n_decoy\": 179,\n   \"n_spont\": 143,\n   \"n_truepos\": 89,\n   \"decoy_vs_spont\": {\n    \"ks_p\": 0.05243003382963393,\n    \"mw_p\": 0.21767398980422226,\n    \"ad_p\": 0.1288912426264994,\n    \"perm_meandiff\": -0.019906197059686437,\n    \"perm_p\": 0.2179455136215946\n   },\n   \"decoy_vs_truepos\": {\n    \"ks_p\": 0.005424056077451029,\n    \"mw_p\": 0.0030299333515588314\n   },\n   \"gap\": {\n    \"ks_sup\": 0.14872836660546157,\n    \"wasserstein\": 0.02554662946735427,\n    \"mean_diff\": -0.019906197059686437,\n    \"cliffs_delta\": -0.07997030902058835,\n    \"n_decoy\": 179,\n    \"n_other\": 143\n   },\n   \"verdict\": \"VALID\"\n  },\n  \"top25pct\": {\n   \"n_decoy\": 77,\n   \"n_spont\": 75,\n   \"n_truepos\": 53,\n   \"decoy_vs_spont\": {\n    \"ks_p\": 0.3119690140143662,\n    \"mw_p\": 0.2649670012400901,\n    \"ad_p\": 0.23387801337065672,\n    \"perm_meandiff\": -0.011980717516705486,\n    \"perm_p\": 0.28292926768307924\n   },\n   \"decoy_vs_truepos\": {\n    \"ks_p\": 0.022459854992724747,\n    \"mw_p\": 0.02305344042658372\n   },\n   \"gap\": {\n    \"ks_sup\": 0.15064935064935064,\n    \"wasserstein\": 0.013490559349513551,\n    \"mean_diff\": -0.011980717516705486,\n    \"cliffs_delta\": -0.10476190476190476,\n    \"n_decoy\": 77,\n    \"n_other\": 75\n   },\n   \"verdict\": \"VALID\"\n  }\n },\n \"figure_cdfs\": {\n  \"x\": [\n   0.0,\n   0.01,\n   0.02,\n   0.03,\n   0.04,\n   0.05,\n   0.06,\n   0.07,\n   0.08,\n   0.09,\n   0.1,\n   0.11,\n   0.12,\n   0.13,\n   0.14,\n   0.15,\n   0.16,\n   0.17,\n   0.18,\n   0.19,\n   0.2,\n   0.21,\n   0.22,\n   0.23,\n   0.24,\n   0.25,\n   0.26,\n   0.27,\n   0.28,\n   0.29,\n   0.3,\n   0.31,\n   0.32,\n   0.33,\n   0.34,\n   0.35,\n   0.36,\n   0.37,\n   0.38,\n   0.39,\n   0.4,\n   0.41,\n   0.42,\n   0.43,\n   0.44,\n   0.45,\n   0.46,\n   0.47,\n   0.48,\n   0.49,\n   0.5,\n   0.51,\n   0.52,\n   0.53,\n   0.54,\n   0.55,\n   0.56,\n   0.57,\n   0.58,\n   0.59,\n   0.6,\n   0.61,\n   0.62,\n   0.63,\n   0.64,\n   0.65,\n   0.66,\n   0.67,\n   0.68,\n   0.69,\n   0.7,\n   0.71,\n   0.72,\n   0.73,\n   0.74,\n   0.75,\n   0.76,\n   0.77,\n   0.78,\n   0.79,\n   0.8,\n   0.81,\n   0.82,\n   0.83,\n   0.84,\n   0.85,\n   0.86,\n   0.87,\n   0.88,\n   0.89,\n   0.9,\n   0.91,\n   0.92,\n   0.93,\n   0.94,\n   0.95,\n   0.96,\n   0.97,\n   0.98,\n   0.99,\n   1.0\n  ],\n  \"cdf_truepos\": [\n   0.0,\n   0.0,\n   0.0,\n   0.0,\n   0.0,\n   0.0,\n   0.0,\n   0.0,\n   0.008130081300813009,\n   0.008130081300813009,\n   0.008130081300813009,\n   0.008130081300813009,\n   0.00813008130081300", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [22] ASSISTANT · 2026-06-16 10:15:51 UTC

```
Let me verify the paired-exchangeability claim and the reconciliation narrative, plus the S1b ladder and generator≠scorer.
```

### [23] TOOL CALL — Bash · 2026-06-16 10:15:51 UTC

```
Read reconciliation narrative and S1b ladder:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== reconciliation_narrative ==='); print(json.dumps(m['reconciliation_narrative'],indent=1)[:2500])
print(); print('=== s1b_difficulty_ladder ==='); print(json.dumps(m['s1b_difficulty_ladder'],indent=1)[:1800])
"
```

### [24] TOOL RESULT — Bash · 2026-06-16 10:15:51 UTC

```
{"stdout": "=== reconciliation_narrative ===\n\"ONE consolidated diagonal story: under the validated self-consistency elicitation the per-family knockoff+ diagonal is the single primary calibration result; the verbalized diagonal on the SAME data is a wrong-elicitation discreteness/loose-target ARTIFACT (see contrast_diagonal_verbalized.artifact_notes), not a co-headline. This reconciles iter-2: self-consistency exchangeable (cf tail win-rate ~0.48), verbalized/logprob anti-conservative.\"\n\n=== s1b_difficulty_ladder ===\n{\n \"rungs\": [\n  {\n   \"rung\": \"L0_foreign_swap\",\n   \"decoy_set\": \"fgn\",\n   \"n_false_pairs\": 2,\n   \"n_tail\": 2,\n   \"tail_win_rate\": 1.0,\n   \"win_rate_ci\": [\n    1.0,\n    1.0\n   ],\n   \"ks_p\": 0.3333333333333333,\n   \"mw_p\": 1.0,\n   \"detected_anti_conservative\": false,\n   \"ci_covers_half\": false\n  },\n  {\n   \"rung\": \"L1_random_swap\",\n   \"decoy_set\": \"swap\",\n   \"n_false_pairs\": 2,\n   \"n_tail\": 2,\n   \"tail_win_rate\": 0.0,\n   \"win_rate_ci\": [\n    0.0,\n    0.0\n   ],\n   \"ks_p\": 0.3333333333333333,\n   \"mw_p\": 0.16666666666666666,\n   \"detected_anti_conservative\": true,\n   \"ci_covers_half\": false\n  },\n  {\n   \"rung\": \"L2_random_vocab\",\n   \"decoy_set\": \"rv\",\n   \"n_false_pairs\": 2,\n   \"n_tail\": 2,\n   \"tail_win_rate\": 0.0,\n   \"win_rate_ci\": [\n    0.0,\n    0.0\n   ],\n   \"ks_p\": 0.3333333333333333,\n   \"mw_p\": 0.16666666666666666,\n   \"detected_anti_conservative\": true,\n   \"ci_covers_half\": false\n  },\n  {\n   \"rung\": \"L3_cf_2nd\",\n   \"decoy_set\": \"cf2\",\n   \"n_false_pairs\": 2,\n   \"n_tail\": 2,\n   \"tail_win_rate\": 0.0,\n   \"win_rate_ci\": [\n    0.0,\n    0.0\n   ],\n   \"ks_p\": 0.3333333333333333,\n   \"mw_p\": 0.16666666666666666,\n   \"detected_anti_conservative\": true,\n   \"ci_covers_half\": false\n  },\n  {\n   \"rung\": \"L4_cf_1st\",\n   \"decoy_set\": \"cf\",\n   \"n_false_pairs\": 2,\n   \"n_tail\": 2,\n   \"tail_win_rate\": 0.0,\n   \"win_rate_ci\": [\n    0.0,\n    0.0\n   ],\n   \"ks_p\": 0.3333333333333333,\n   \"mw_p\": 0.16666666666666666,\n   \"detected_anti_conservative\": true,\n   \"ci_covers_half\": false\n  }\n ],\n \"verdict\": \"PARTIAL\",\n \"reason\": \"Graded/partial sensitivity: the diagnostic flags only grossly-easy (out-of-context) decoys, losing resolution for in-distribution rungs. Down-scoped to 'detects only gross non-exchangeability'.\",\n \"cut_rule\": \"knockoff+ operative T at alpha=0.5 per rung; win-rate over FALSE-real pairs\"", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [25] ASSISTANT · 2026-06-16 10:19:06 UTC

```
The S1b ladder is severely underpowered (n=2 per rung). Now let me verify the application headline (exp2) — the central new executed result.
```

### [26] TOOL CALL — Bash · 2026-06-16 10:19:06 UTC

```
Read multihop corruption result from application anchor:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('META KEYS:', list(m.keys()))
print()
print('=== multihop_corruption ==='); print(json.dumps(m.get('multihop_corruption',{}),indent=1)[:2000])
"
```

### [27] TOOL RESULT — Bash · 2026-06-16 10:19:06 UTC

```
{"stdout": "META KEYS: ['method_name', 'task', 'anchor', 'headline_finding', 'headline_elicitation', 'primary_metric', 'models', 'elicitation', 'hyperparameters', 'dataset_counts', 'hallucination_grid', 'headline', 's1_decoy_signature', 'matched_recall_curves', 'extraction_quality', 'multihop_corruption', 'adjudicator_validation', 'trace_graphs', 'bh_correction', 'runtime', 'cost_trace_path', 'interpretation']\n\n=== multihop_corruption ===\n{\n \"by_genre\": {\n  \"legal\": {\n   \"raw\": {\n    \"derived\": 11,\n    \"corrupt\": 0,\n    \"corrupted_rate\": 0.0\n   },\n   \"gate_a0.05\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.1\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.2\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.3\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.5\": {\n    \"derived\": 8,\n    \"corrupt\": 0,\n    \"corrupted_rate\": 0.0\n   }\n  },\n  \"news\": {\n   \"raw\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.05\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.1\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.2\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.3\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.5\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   }\n  },\n  \"regulatory\": {\n   \"raw\": {\n    \"derived\": 12,\n    \"corrupt\": 11,\n    \"corrupted_rate\": 0.9166666666666666\n   },\n   \"gate_a0.05\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.1\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.2\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.3\": {\n    \"derived\": 0,\n    \"corrupt\": 0,\n    \"corrupted_rate\": null\n   },\n   \"gate_a0.5\": {\n    \"derived\": 3,\n    \"corrupt\": 2,\n    \"corrupted_rate\": 0.6666666666666666\n   }\n  }\n },\n \"pooled\": {\n  \"raw\": {\n   \"derived\": 23,\n   \"corrupt\": 11,\n   \"corrupted_rate\": 0.4782608695652174\n  },\n  \"gate_a0.05\": {\n   \"derived\": 0,\n   \"corrupt\": 0,\n   \"corrupted_rate\": null\n  },\n  \"gate_a0.1\": {\n   \"derived\": 0,\n   \"corrupt\": 0,\n   \"corrupted_rate\": null\n  },\n  \"gate_a0.2\": {\n   \"derived\": 0,\n   \"corrupt\": 0,\n   \"corrupted_rate\": nul", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [28] ASSISTANT · 2026-06-16 10:20:27 UTC

```
The corruption reduction is driven entirely by the regulatory genre (11→3 derived). Let me verify the atomic hallucination reduction and conservative self-report claims.
```

### [29] TOOL CALL — Bash · 2026-06-16 10:20:27 UTC

```
Read application headline, counts, extraction quality, adjudicator:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== headline ==='); print(json.dumps(m.get('headline',{}),indent=1)[:1800])
print('=== dataset_counts ==='); print(json.dumps(m.get('dataset_counts',{}),indent=1)[:800])
print('=== extraction_quality ==='); print(json.dumps(m.get('extraction_quality',{}),indent=1)[:600])
print('=== adjudicator_validation ==='); print(json.dumps(m.get('adjudicator_validation',{}),indent=1)[:700])
"
```

### [30] TOOL RESULT — Bash · 2026-06-16 10:20:27 UTC

```
{"stdout": "=== headline ===\n{\n \"best_reduction_cell\": {\n  \"genre\": \"regulatory\",\n  \"elicitation\": \"portable\",\n  \"alpha\": 0.5,\n  \"raw\": 0.439252,\n  \"gate\": 0.36,\n  \"abs_reduction\": 0.079252,\n  \"rel_reduction\": 0.180425,\n  \"ci_separated\": false,\n  \"certified\": true,\n  \"n_admitted\": 50,\n  \"regime_tag\": \"certified\"\n },\n \"n_cells_gate_below_raw_ci_separated\": 0,\n \"all_reductions\": [\n  {\n   \"genre\": \"legal\",\n   \"elicitation\": \"logprob\",\n   \"alpha\": 0.2,\n   \"raw\": 0.028169,\n   \"gate\": 0.016393,\n   \"abs_reduction\": 0.011776,\n   \"rel_reduction\": 0.418048,\n   \"ci_separated\": false,\n   \"certified\": true,\n   \"n_admitted\": 61,\n   \"regime_tag\": \"anti_conservative_expected\"\n  },\n  {\n   \"genre\": \"legal\",\n   \"elicitation\": \"logprob\",\n   \"alpha\": 0.3,\n   \"raw\": 0.028169,\n   \"gate\": 0.016393,\n   \"abs_reduction\": 0.011776,\n   \"rel_reduction\": 0.418048,\n   \"ci_separated\": false,\n   \"certified\": true,\n   \"n_admitted\": 61,\n   \"regime_tag\": \"anti_conservative_expected\"\n  },\n  {\n   \"genre\": \"legal\",\n   \"elicitation\": \"logprob\",\n   \"alpha\": 0.5,\n   \"raw\": 0.028169,\n   \"gate\": 0.016393,\n   \"abs_reduction\": 0.011776,\n   \"rel_reduction\": 0.418048,\n   \"ci_separated\": false,\n   \"certified\": true,\n   \"n_admitted\": 61,\n   \"regime_tag\": \"anti_conservative_expected\"\n  },\n  {\n   \"genre\": \"news\",\n   \"elicitation\": \"logprob\",\n   \"alpha\": 0.5,\n   \"raw\": 0.0625,\n   \"gate\": 0.095238,\n   \"abs_reduction\": -0.032738,\n   \"rel_reduction\": -0.523808,\n   \"ci_separated\": false,\n   \"certified\": true,\n   \"n_admitted\": 21,\n   \"regime_tag\": \"anti_conservative_expected\"\n  },\n  {\n   \"genre\": \"pooled\",\n   \"elicitation\": \"logprob\",\n   \"alpha\": 0.5,\n   \"raw\": 0.242857,\n   \"gate\": 0.178082,\n   \"abs_reduction\": 0.064775,\n   \"rel_reduction\": 0.266721,\n   \"ci_separated\": false,\n   \"certified\": true,\n   \"n_admitted\": 146,\n   \"regime_tag\": \"anti_conservative_e\n=== dataset_counts ===\n{\n \"n_docs\": 24,\n \"genre_counts\": {\n  \"legal\": 8,\n  \"news\": 8,\n  \"regulatory\": 8\n },\n \"n_reals\": 210,\n \"label_counts\": {\n  \"TRUE\": 42,\n  \"FALSE\": 51,\n  \"UNDECIDABLE\": 117\n },\n \"n_decoys_generated\": 420,\n \"contamination_rate_decoys\": 0.05714285714285714,\n \"n_entrapment\": 209\n}\n=== extraction_quality ===\n{\n \"legal\": {\n  \"atomic_precision\": 0.28336056644880175,\n  \"atomic_recall\": 0.26711309523809523,\n  \"n_docs\": 8,\n  \"crisp_restricted\": true\n },\n \"news\": {\n  \"atomic_precision\": 0.29444444444444445,\n  \"atomic_recall\": 0.1845238095238095,\n  \"n_docs\": 8,\n  \"crisp_restricted\": false\n },\n \"regulatory\": {\n  \"atomic_precision\": 0.1745598441805872,\n  \"atomic_recall\": 0.4151785714285714,\n  \"n_docs\": 8,\n  \"crisp_restricted\": false\n }\n}\n=== adjudicator_validation ===\n{\n \"kappa\": 0.10126582278481007,\n \"raw_agreement\": 0.38028169014084506,\n \"n_legal_judged\": 71,\n \"trust_threshold\": 0.4,\n \"judge_trusted\": false,\n \"fallback_active\": true\n}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [31] ASSISTANT · 2026-06-16 10:21:37 UTC

```
The application numbers all match. Now let me verify the Re-DocRED regime-diagnostic (exp3) — the scope, recall ceiling, and prediction-correct claims.
```

### [32] TOOL CALL — Bash · 2026-06-16 10:21:37 UTC

```
Read Re-DocRED scope, verdict, regime diagnostic:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('META KEYS:', list(m.keys()))
print()
for k in ['scope','verdict','wedge_verdict','regime_diagnostic','multihop','multi_hop','comparators','dropped_comparators']:
    if k in m:
        print('=== %s ==='%k); print(json.dumps(m[k],indent=1)[:1800]); print()
"
```

### [33] TOOL RESULT — Bash · 2026-06-16 10:21:37 UTC

```
{"stdout": "META KEYS: ['method_name', 'description', 'n_docs_used', 'split_role', 'model', 'elicitation', 'logprobs_available', 'caching_ok', 'cost_usd', 'n_api_calls', 'n_calibration_labels_conformal', 'seed', 'bootstrap_B', 'systems', 'participating_systems', 'dropped_comparators', 'scope', 'rules_list', 'config', 'max_recall_per_system', 'max_common_recall', 'pr_curves', 'matched_recall', 'knockoff_operating_points', 'conformal_operating_points', 'hallucinated_conclusion_rate', 'alignment_check', 'contamination_rate_decoys', 'reasoning_traces', 'regime_diagnostic', 'verdict', 'cost_log_summary']\n\n=== scope ===\n{\n \"n_docs_used\": 152,\n \"n_docs_requested\": 152,\n \"recall_ceiling\": 0.07504,\n \"recall_ceiling_definition\": \"max recall of METHOD/PLAIN's shared candidate+alignment pool\",\n \"bootstrap_B\": 2000,\n \"grid_start\": 0.03419\n}\n\n=== verdict ===\n{\n \"wedge_confirmed\": false,\n \"disconfirmed\": true,\n \"n_confirmed_points\": 0,\n \"scope\": {\n  \"n_docs_used\": 152,\n  \"n_docs_requested\": 152,\n  \"recall_ceiling\": 0.07504,\n  \"recall_ceiling_definition\": \"max recall of METHOD/PLAIN's shared candidate+alignment pool\",\n  \"bootstrap_B\": 2000,\n  \"grid_start\": 0.03419\n },\n \"recall_ceiling\": 0.07504,\n \"n_docs_used\": 152,\n \"message\": \"OPERATIONAL DISCONFIRMATION at recall <= 0.075 on 152 docs (pre-registered): the wedge collapses to 'thresholding-is-enough' \\u2014 no recall point shows a precision advantage of decoy-gating over the plain confidence threshold with CI entirely > 0.\",\n \"operational_verdict\": \"disconfirmed at recall <= 0.075 on 152 docs; reframed as a label-free regime-diagnostic \\u2014 the Re-DocRED scorer sits in the GATE REDUNDANT regime (predicted gold-free as 'null'; prediction_correct=True vs the realized wedge).\",\n \"predicted_regime\": \"GATE REDUNDANT\",\n \"predicted_wedge_sign\": \"null\",\n \"prediction_correct\": true,\n \"notes\": \"RELATIVE comparison only: Re-DocRED residual false negatives depress recall for ALL systems equally and inflate hallucinated-conclusion counts for ALL systems equally; no absolute realized-FDR diagonal is asserted (that belongs to CLUTRR). METHOD and PLAIN consume an IDENTICAL candidate+alignment pool (same max recall); the only difference is the gate (W_i competition vs raw Z_i threshold).\"\n}\n\n=== regime_diagnostic ===\n{\n \"summary\": \"Label-free 2-axis regime-diagnostic that predicts the operational-wedge sign from cached Z/Zt/W/self-consistency with ZERO API calls and NO gold, then validates against the realized wedge.\",\n \"n_candidate_rows\": 4384,\n \"n_docs\": 152,\n \"signal_A_winrate_tail\": [\n  {\n   \"label\": \"top_25pct\",\n   \"cutoff\": \"max(Z,Zt)>=1.000\",\n   \"n_tail\": 1096,\n   \"winrate\": 0.05383,\n   \"ci\": [\n    0.03504,\n    0.07549\n   ]\n  },\n  {\n   \"label\": \"top_50pct\",\n   \"cutoff\": \"max(Z,Zt)>=0.999\",\n   \"n_tail\": 2192,\n   \"winrate\": 0.04471,\n   \"ci\": [\n    0.03366,\n    0.05807\n   ]\n  },\n  {\n   \"label\": \"all\",\n   \"cutoff\": \"all candidates\",\n   \"n_tail\": 4384,\n   \"winrate\": 0.06227,\n   \"ci\": [\n    0.05149,\n    0.07303\n   ]\n  },\n  {\n   \"label\": \"knockoff_alpha0.2\",\n   \"cutoff\": \"W>=0.000\",\n   \"n_tail\": 4133,\n   \"winrate\": 0.00532,\n   \"ci\": [\n    0.00291,\n    0.00812\n   ]\n  },\n  {\n   \"label\": \"matched_recall_rep\",\n   \"cutoff\": \"max(Z,Zt)>=0.993 (gold-anchored)\",\n   \"n_tail\": 2912,\n   \"winrate\": 0.04396,\n   \"ci\": [\n    0.03359,\n    0.05523\n   ]\n  }\n ],\n \"signal_B_cdf_match\": {\n  \"low_f_threshold\": 0.4,\n  \"full_distribution\": {\n   \"n_decoy\": 4384,\n   \"n_lowf_real\": 1704,\n   \"ks_p\": 0.0,\n   \"mw_p\": 0.0,\n   \"perm_p\": 0.0005,\n   \"decoy_mean\": 0.16527,\n   \"lowf_real_mean\": 0.85737,\n   \"match\": false\n  },\n  \"top_tail\": {\n   \"n_decoy\": 1410,\n   \"n_lowf_real\": 1634,\n   \"ks_p\": 0.0,\n   \"mw_p\": 0.0,\n   \"perm_p\": 0.0005,\n   \"decoy_mean\": 0.51103,\n   \"lowf_real_mean\": 0.89398,\n   \"match\": false\n  },\n  \"interpretation\": \"MATCH (fail-to-reject) => decoys exchangeable with the model's own spontaneous errors (valid knockoff); REJECT with decoy mean < low-f-real mean => decoys TOO EASY (gate redundant/worse).\"\n },\n \"signal_C_wz_divergence\": {\n  \"spearman_full\": 0.93399,\n  \"spearman_admission\": 0.99096,\n  \"ad\n\n=== dropped_comparators ===\n{}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [34] TOOL CALL — Bash · 2026-06-16 10:21:56 UTC

```
Read hallucinated conclusion rate, signals C/D, systems:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_3 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== hallucinated_conclusion_rate ==='); print(json.dumps(m['hallucinated_conclusion_rate'],indent=1)[:1200])
rd=m['regime_diagnostic']
print('=== signal_C ==='); print(json.dumps(rd['signal_C_wz_divergence'],indent=1)[:600])
print('=== signal_D ==='); print(json.dumps(rd.get('signal_D_calibration',rd.get('signal_D',{})),indent=1)[:500])
print('=== participating_systems ==='); print(m['participating_systems'])
print('=== max_recall_per_system ==='); print(json.dumps(m['max_recall_per_system'],indent=1)[:400])
"
```

### [35] TOOL RESULT — Bash · 2026-06-16 10:21:58 UTC

```
{"stdout": "=== hallucinated_conclusion_rate ===\n{\n \"representative_recall\": 0.06312,\n \"by_system\": {\n  \"METHOD\": {\n   \"point\": 0.7865168539325843,\n   \"ci_lo\": 0.7178204884948425,\n   \"ci_hi\": 0.8560332278923942,\n   \"n_derived\": 267,\n   \"n_hallucinated\": 210\n  },\n  \"PLAIN\": {\n   \"point\": 0.7902621722846442,\n   \"ci_lo\": 0.7201331058020478,\n   \"ci_hi\": 0.86031454248366,\n   \"n_derived\": 267,\n   \"n_hallucinated\": 211\n  },\n  \"CoT\": {\n   \"point\": null,\n   \"ci_lo\": null,\n   \"ci_hi\": null,\n   \"n_derived\": 0,\n   \"n_hallucinated\": 0\n  },\n  \"RAG\": {\n   \"point\": null,\n   \"ci_lo\": null,\n   \"ci_hi\": null,\n   \"n_derived\": 0,\n   \"n_hallucinated\": 0\n  },\n  \"CONF\": {\n   \"point\": 0.7837837837837838,\n   \"ci_lo\": 0.703879000359583,\n   \"ci_hi\": 0.8556717931384147,\n   \"n_derived\": 259,\n   \"n_hallucinated\": 203\n  }\n },\n \"delta_method_minus_plain\": {\n  \"point\": -0.004120504635618347,\n  \"ci_lo\": -0.018242760387005355,\n  \"ci_hi\": 0.008486647980594798\n },\n \"underpowered\": false,\n \"power_target\": 100,\n \"n_derived_by_system\": {\n  \"METHOD\": 267,\n  \"PLAIN\": 267,\n  \"CoT\": 0,\n  \"RAG\": 0,\n  \"CONF\": 259\n },\n \"delta_ci_width\": 0.02673,\n \"power_note\": \"POWERED: both systems derive >= power_target (100) conclusions with delta CI width <= 0.5.\",\n \"recall_grid\": [\n  0.03\n=== signal_C ===\n{\n \"spearman_full\": 0.93399,\n \"spearman_admission\": 0.99096,\n \"admitted_set_jaccard\": 0.91609,\n \"frac_W_equals_Z\": 0.9391,\n \"n_candidates\": 4384,\n \"n_admitted_W_ge_0\": 4133,\n \"interpretation\": \"frac(W==Z)~1 and admitted-set rho~1 => the gate keeps and orders the same facts as the plain Z threshold => mechanically NULL wedge. Jaccard<1 measures the few 'winner' demotions, which the realized wedge shows are precision-neutral here.\"\n}\n=== signal_D ===\n{\n \"calibration_auc\": 0.60293,\n \"calibration_spearman_Z_f\": 0.2015,\n \"f_pos_threshold\": 0.5,\n \"n_pos\": 2680,\n \"n_total\": 4384,\n \"interpretation\": \"AUC(Z -> high-self-consistency) high => Z is calibrated against the model's own truth proxy => plain threshold already separates good from bad => the gate is redundant rather than harmful.\"\n}\n=== participating_systems ===\n['METHOD', 'PLAIN', 'CoT', 'RAG', 'CONF']\n=== max_recall_per_system ===\n{\n \"METHOD\": 0.07504,\n \"PLAIN\": 0.07504,\n \"CoT\": 0.05117,\n \"RAG\": 0.03419,\n \"CONF\": 0.07504\n}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [36] ASSISTANT · 2026-06-16 10:23:45 UTC

```
All Re-DocRED numbers verified. Let me verify the generator≠scorer (S2b) and verbalized contrast claims, and do a literature check on novelty in parallel.
```

### [37] TOOL CALL — Bash · 2026-06-16 10:23:45 UTC

```
Verify generator-not-scorer and verbalized contrast:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('method_out.json'))
m=d['metadata']
print('=== generator_ne_scorer_carried_forward ==='); print(json.dumps(m['generator_ne_scorer_carried_forward'],indent=1)[:1400])
print('=== contrast_diagonal_verbalized (atomic rows tail) ===')
cv=m['contrast_diagonal_verbalized']
import json as j
# print artifact_notes and atomic a=0.5 row
if 'artifact_notes' in cv: print('notes:', j.dumps(cv['artifact_notes'])[:600])
for fam in ['atomic','multi_hop']:
    if fam in cv:
        rows=cv[fam].get('rows',[])
        for r in rows:
            if r['target_alpha']==0.5:
                print(fam,'a=0.5: adm=%s realFDR=%s fdrhat=%s cert=%s'%(r['n_admitted'],r.get('realized_fdr'),r.get('decoy_fdr_hat'),r.get('certified')))
"
```

### [38] TOOL RESULT — Bash · 2026-06-16 10:23:47 UTC

```
{"stdout": "=== generator_ne_scorer_carried_forward ===\n{\n \"verdict\": \"ROBUST\",\n \"validity_region_statement\": \"Decoy-competition exchangeability (tail win-rate CI covers 0.5) holds for configs: G=nano,S=nano, G=nano,S=other, G=other,S=nano, G=other,S=other. Verdict: ROBUST.\",\n \"configs\": [\n  {\n   \"G\": \"nano\",\n   \"S\": \"nano\",\n   \"scorer_config\": \"nano_portable\",\n   \"alpha_star\": 0.5,\n   \"n_false_pairs\": 260,\n   \"tail_win_rate\": 0.4909090909090909,\n   \"win_rate_ci\": [\n    0.37037037037037035,\n    0.6071428571428571\n   ],\n   \"ci_covers_half\": true,\n   \"n_tail\": 55,\n   \"ks_p\": 0.9989125698850362,\n   \"mw_p\": 0.4737700845951131,\n   \"small_diagonal\": {\n    \"0.05\": {\n     \"alpha\": 0.05,\n     \"threshold\": null,\n     \"n_admitted\": 0,\n     \"n_false_admitted\": 0,\n     \"realized_fdr\": 0.0,\n     \"estimated_ratio\": 1.0,\n     \"k_floor\": 20,\n     \"certified\": false\n    },\n    \"0.1\": {\n     \"alpha\": 0.1,\n     \"threshold\": null,\n     \"n_admitted\": 0,\n     \"n_false_admitted\": 0,\n     \"realized_fdr\": 0.0,\n     \"estimated_ratio\": 1.0,\n     \"k_floor\": 10,\n     \"certified\": false\n    },\n    \"0.2\": {\n     \"alpha\": 0.2,\n     \"threshold\": null,\n     \"n_admitted\": 0,\n     \"n_false_admitted\": 0,\n     \"realized_fdr\": 0.0,\n     \"estimated_ratio\": 1.0,\n     \"k_floor\": 5,\n     \"certified\": false\n    },\n    \"0.3\": {\n     \"alpha\": 0.3,\n     \"threshold\": null,\n     \"n_admitted\": 0,\n     \"n_false_admitted\": 0,\n     \"realized_fdr\": 0.0,\n     \"estimated_ratio\": 1.0,\n    \n=== contrast_diagonal_verbalized (atomic rows tail) ===\nnotes: {\"target_alpha_violations\": [{\"family\": \"atomic\", \"alpha\": 0.5, \"realized_fdr\": 0.533784}], \"decoy_fdr_hat_undershoots\": [{\"family\": \"atomic\", \"alpha\": 0.5, \"decoy_fdr_hat\": 0.5, \"realized_fdr\": 0.533784}], \"identical_admission_sets_neighbors\": []}\natomic a=0.5: adm=148 realFDR=0.533784 fdrhat=0.5 cert=True\nmulti_hop a=0.5: adm=0 realFDR=None fdrhat=None cert=False", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [39] ASSISTANT · 2026-06-16 10:23:59 UTC

```
The paper's numbers are faithful to the artifacts throughout. Let me do a focused literature check on novelty before finalizing.
```

### [40] TOOL CALL — ToolSearch · 2026-06-16 10:23:59 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [41] TOOL RESULT — ToolSearch · 2026-06-16 10:23:59 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [42] TOOL CALL — WebSearch · 2026-06-16 10:24:03 UTC

```
knockoff filter false discovery rate LLM hallucination fact extraction decoy
```

### [43] TOOL CALL — WebSearch · 2026-06-16 10:24:03 UTC

```
conformal selection FDR control LLM factuality intermediate fact admission neuro-symbolic
```

### [44] TOOL RESULT — WebSearch · 2026-06-16 10:24:09 UTC

```
{"query": "knockoff filter false discovery rate LLM hallucination fact extraction decoy", "results": [{"tool_use_id": "srvtoolu_01ENECZknu7WULCHyLL2jGcG", "content": [{"title": "Controlling the false discovery rate via knockoffs", "url": "https://arxiv.org/pdf/1404.5609"}, {"title": "Null-free False Discovery Rate Control Using Decoy Permutations", "url": "https://arxiv.org/pdf/1804.08222"}, {"title": "Controlling the false discovery rate via knockoffs", "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-5/Controlling-the-false-discovery-rate-via-knockoffs/10.1214/15-AOS1337.full"}, {"title": "DeepPINK: reproducible feature selection in deep neural networks", "url": "https://arxiv.org/pdf/1809.01185"}, {"title": "Large Language Models Are Highly Vulnerable to Adversarial Hallucination Attacks in Clinical Decision Support: A Multi-Model Assurance Analysis", "url": "https://www.medrxiv.org/content/10.1101/2025.03.18.25324184.full.pdf"}, {"title": "The knockoff filter for FDR control in group-sparse and multitask   regression", "url": "https://arxiv.org/pdf/1602.03589"}, {"title": "Simple explanation for knockoff filters : A feature selection approach with controlled FDR | by Amrutha Karuturi | Medium", "url": "https://medium.com/@amrutha.karuturi/simple-explanation-for-knockoff-filters-a-feature-selection-approach-with-controlled-fdr-4c3771fd9a7c"}, {"title": "GitHub - Mattbusel/LLM-Hallucination-Detection-Script: A comprehensive toolkit for detecting potential hallucinations in LLM responses. Compatible with any LLM API (OpenAI, Anthropic, local models, etc.) · GitHub", "url": "https://github.com/Mattbusel/LLM-Hallucination-Detection-Script"}]}, "The search results show information related to knockoff filters and false discovery rate control, as well as some discussion of LLM hallucinations, but they don't appear to directly combine these topics into a single integrated method.\n\nHere's what was found:\n\n**Knockoff Filters & FDR Control:**\nThe knockoff filter is a variable selection procedure controlling the FDR in statistical linear models when there are at least as many observations as variables. The knockoff filter constructs a \"knockoff\" variable for each real variable that is not associated with the response but competes with real counterparts in variable selection. The approach was inspired by the target-decoy database search strategy used to estimate the FDR of peptide identifications in proteomics.\n\n**LLM Hallucinations:**\nThe search results include information about LLM hallucinations in clinical contexts, noting that systems like GPT-4 can produce fabricated information, but this doesn't appear to be directly connected to knockoff filter methodology in the results.\n\nThe search results don't show a specific integrated approach combining knockoff filters, decoy methods, and LLM fact extraction for hallucination detection. If you're looking for recent research on applying statistical FDR control methods to fact-checking LLM outputs, you may want to search academic databases or recent preprints on arXiv for more specialized papers on this emerging topic."], "durationSeconds": 6.411420995000051, "searchCount": 1}
```

### [45] TOOL RESULT — WebSearch · 2026-06-16 10:24:11 UTC

```
{"query": "conformal selection FDR control LLM factuality intermediate fact admission neuro-symbolic", "results": [{"tool_use_id": "srvtoolu_01QgdFy4sMqnWjAMJ8Fe43Qe", "content": [{"title": "An Empirical Study of Conformal Prediction in LLM with ...", "url": "https://eprints.whiterose.ac.uk/id/eprint/237872/1/2503.05439v2.pdf"}, {"title": "Conformal Policy Control", "url": "https://arxiv.org/pdf/2603.02196"}, {"title": "Conditional Factuality Controlled LLMs with Generalization Certificates via", "url": "https://arxiv.org/pdf/2603.27403"}, {"title": "Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs", "url": "https://arxiv.org/pdf/2509.23007"}, {"title": "(PDF) Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling", "url": "https://www.researchgate.net/publication/403308104_Conditional_Factuality_Controlled_LLMs_with_Generalization_Certificates_via_Conformal_Sampling"}, {"title": "Model-agnostic Selective Labeling with Provable Statistical Guarantees", "url": "https://arxiv.org/pdf/2510.14581"}, {"title": "Multi-Condition Conformal Selection", "url": "https://arxiv.org/html/2510.08075v2"}, {"title": "Optimized Conformal Selection: Powerful Selective Inference After   Conformity Score Optimization", "url": "https://arxiv.org/pdf/2411.17983"}]}, "Based on the search results, here's what I found related to your query:\n\nThe search returned several relevant papers on conformal prediction, FDR control, and LLM factuality:\n\n**Key Topics Found:**\n\n1. **Conformal Prediction and FDR Control**: Conformal selection methods offer rigorous solutions with False Discovery Rate (FDR) control, and Multi-Condition Conformal Selection (MCCS) extends conformal selection to scenarios with multiple conditions.\n\n2. **LLM Factuality Control**: Recent work connects conformal risk control frameworks to the specific problem of controlling LLM factuality, including loss functions for factuality control including the non-monotonic FDR loss.\n\n3. **Conditional Factuality Control**: Conditional Factuality Control (CFC) is a post-hoc conformal layer for LLM sampling that defines a feature-conditional acceptance rule by conformalizing a quantile-regression model for a latent success score.\n\n4. **Neuro-Symbolic Reasoning**: Research demonstrates the reliability and performance of neuro-symbolic reasoning systems, contributing to the development of more robust and interpretable reasoning frameworks.\n\n5. **Applications to QA and Selection**: Conformal Labeling achieves tight FDR control while labeling a substantial proportion of data with AI models across various benchmarks and model architectures.\n\nThe papers appear to focus on using conformal inference techniques to provide statistical guarantees for LLM factuality and selection tasks while maintaining FDR control."], "durationSeconds": 9.157478939000052, "searchCount": 1}
```

### [46] ASSISTANT · 2026-06-16 10:26:22 UTC

```
I have verified all the paper's central claims against the artifacts and confirmed the novelty positioning. The numbers are faithful throughout. Let me compile my assessment.

**Summary of verification:**
- Central disconfirmation (S2): realized FDR 1.0 at α*=0.5, 12/12 false, CI [0.66,1.0], self-report 0.5 — ✓ matches artifact exactly
- Crux (S1): full KS p=0.058, tail KS p=0.31, vs-TP p=5e-9 — ✓ (now fail-to-reject; previous review's "rejected full-dist" issue resolved by data change)
- Application (S4b): pooled 0.178/0.183 vs 0.243, 0/40 CI-separated, corruption 0.48→0.18 (11 vs 23 conclusions, driven by regulatory) — ✓
- Re-DocRED (S4): 152 docs, recall ≤0.075, all 5 systems participate, multi-hop 267 derived, delta −0.004, prediction_correct — ✓
- All 4 prior MAJOR issues substantially addressed.

Key remaining concerns: pervasive underpowering, weak-extractor confound on the central disconfirmation, thin salvaged contributions, missing figure captions.
```

### [47] TOOL CALL — Write · 2026-06-16 10:26:22 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This iteration is a substantial and commendable revision. The author addressed all four MAJOR issues from the previous round: the headline CLUTRR calibration diagonal is now computed under the diagnostic-validated K=5 self-consistency elicitation (not verbalized), the pre-registered disconfirmation is reported honestly, the application hallucination-reduction run on the 24-document legal/news/regulatory anchor is actually EXECUTED, and the Re-DocRED operational test is scaled to its true 152-document scope with all comparators participating and a powered multi-hop comparison. I independently verified every load-bearing number against the supplementary artifacts (art_sBLQqsdm3EIA, art_vkfyOl2OQNVx, art_RZC2468yZ-Jh) and found the paper to be exceptionally faithful to its evidence: realized FDR 1.0 / CI [0.66,1.0] / self-report 0.5 on multi-hop; crux KS p=0.058 (full) and 0.31 (tail) vs 5e-9 against true positives; application pooled 0.178/0.183 vs raw 0.243 with 0/40 cells CI-separated; corruption 0.48->0.18; Re-DocRED 267 derived conclusions, delta -0.004, prediction_correct. This reporting honesty is a real strength and is rare. The paper has, however, pivoted from 'we have a working label-free FDR gate' to 'the gate does NOT control FDR, and here is the conceptual reason plus an auditable pipeline.' As an honest negative-results paper it is well-constructed, but three issues keep it below the acceptance bar for a top venue: (1) nearly every affirmative claim is underpowered, including the central disconfirmation itself (40-doc checkpoint, 12 admitted pairs, borderline marginal p-values); (2) the disconfirmation is confounded with a deliberately pathological extractor (gpt-4.1-nano, multi-hop accuracy 0.17), so it is unclear whether the marginal-vs-paired failure is intrinsic to decoy-gating or an artifact of a model that cannot score its own multi-hop errors; and (3) the contributions that survive the disconfirmation (the regime-diagnostic, the directional application reduction) are individually weak. The conceptual lesson (marginal distributional exchangeability does not imply paired sign-flip exchangeability at the cutoff) is genuinely interesting and likely correct, but its empirical demonstration is currently too underpowered and too confounded to carry a top-venue paper on its own.",
  "strengths": [
    "Outstanding reporting honesty and reproducibility: I traced every headline number to the artifacts and they match exactly, including the numbers that disconfirm the method's central claim. The paper reports a pre-registered primary disconfirmation (realized FDR 1.0 at alpha*=0.5) rather than burying it, and surfaces a second-order self-report disconfirmation. This is the level of rigor top venues should reward.",
    "A genuinely novel and useful conceptual contribution: the two-layer decomposition of knockoff validity at the LLM boundary into a marginal (distributional) layer and a paired (sign-flip) layer, with the demonstration that property-matched-decoy/win-rate diagnostics (imported from genomics/proteomics) live entirely in the marginal layer and therefore over-certify the gate. To my knowledge this marginal-vs-paired gap has not been articulated for knockoffs transplanted to LLM scoring, and it is a transferable lesson.",
    "Clear and well-cited differentiation from prior work. The label-free / intermediate-admission / tested-exchangeability positioning is correctly distinguished from labeled conformal selection (Jin-Candes), multiple-testing hallucination detection (Li et al.), conformal link prediction (Marandon), and conformal factuality (Mohri-Hashimoto). My literature search confirmed no existing work applies knockoff/target-decoy FDR control at the text-to-logic admission boundary, and that the conformal-for-LLM-factuality neighbors are all labeled and certify model outputs.",
    "The end-to-end auditable pipeline is real and executed: typed extraction (WordNet->SUMO), the knockoff+ gate, entrapment corroboration, and a backward-chaining proof engine emitting JSON+DOT trace-graphs whose leaves carry provenance, decoy, and entrapment certificates. This directly serves the goal's interpretability mandate, and the worked legal/regulatory proof examples (including an exposed rejected leaf) are convincing.",
    "Honest, well-designed experimental protocol: pre-registered claim chain with explicit verdicts, the 1/k admission-floor accounting that prevents 'confirmed-by-conservatism' artifacts, document-block bootstrap CIs, BH multiplicity control, and a clean division of labor across the three anchors (CLUTRR for crisp-gold calibration, application anchor for genre-faithful reduction, Re-DocRED for the operational wedge)."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "Claims are now honestly and accurately supported by the artifacts; the central disconfirmation is solid in direction (12/12 admitted multi-hop facts false, CI entirely above alpha*). Methodology (knockoff+, entrapment, isolated provenance-blinded scoring, bootstrap CIs, BH) is appropriate and faithfully implemented. Held back from 4 by pervasive underpowering (the headline diagonal is a 40-doc checkpoint with 12 admitted pairs; the marginal crux rests on borderline p-values of 0.058/0.061; the application reduction reaches 0/40 CI separation; the multi-hop corruption rests on 11 vs 23 conclusions with no CI) and by the weak-extractor confound that prevents attributing the disconfirmation to the method rather than to the base model.",
      "improvements": [
        "Run the powered CLUTRR self-consistency diagonal (the artifact itself flags the ~593-doc run as the intended final version) so the headline disconfirmation and the marginal-vs-paired crux no longer rest on 12 admitted pairs and p=0.058. The direction is unlikely to reverse, but power converts an 'interesting checkpoint' into a defensible headline.",
        "Disentangle the disconfirmation from extractor quality: repeat the diagonal with a stronger extractor (or on a less error-dense family) to show whether the paired sign-flip failure persists when the candidate pool is not ~85% false. Without this, a reviewer cannot tell if the lesson is 'knockoffs fundamentally fail at the LLM boundary' or 'gpt-4.1-nano cannot score its own multi-hop errors.'",
        "Report the multi-hop corruption result (0.48->0.18) with document-block bootstrap CIs and note explicitly that it is driven entirely by the regulatory genre (12->3 derived conclusions; legal already 0.0, news derives 0). At these counts it is anecdotal; either power it or present it as illustrative rather than 'the clearest positive.'"
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The writing is precise, the narrative is coherent, and the honest framing is handled gracefully. But the figures appear only as bare [FIGURE:fig1]-[fig5] markers with no captions or descriptions in the manuscript body (flagged in the previous round, still unaddressed), so a reader cannot assess what the load-bearing figures communicate. The paper is also extremely dense with a large alphabet of claim codes (S0, S1, S1b, S2, S2-self, S2b, S3, S4, S4b) that taxes the reader, and contains at least one internal inconsistency between narrative and tabulated data (the S1b ladder).",
      "improvements": [
        "Add a complete caption plus a one-to-two sentence description for every figure. The realized-FDR-vs-alpha diagonal must mark the 1/k floor, the bootstrap CIs, and visibly separate the gate from the plain and swap baselines; the marginal-vs-paired figure should show the decoy/spontaneous/true-positive CDFs and the paired win asymmetry; the application figure should show the per-genre grid with CIs; the Re-DocRED figure should show the wedge with all participating systems.",
        "Reduce reader load: collapse the claim-code zoo into a single clearly-labeled table (already partly done in Table 2) and refer to results by what they show rather than by code, or add a one-line legend mapping each code to a plain-English claim.",
        "Fix the S1b narrative/data inconsistency (see the rigor critique) so the text does not contradict its own ladder."
      ]
    },
    {
      "dimension": "contribution",
      "score": 2,
      "justification": "The central proposed mechanism (a certified label-free FDR gate) is disconfirmed on the populable family, so the headline 'first label-free FDR knob' becomes 'first to propose and then disconfirm.' The contributions that survive are individually thin: the application hallucination reduction is directional only (0/40 CI-separated), the corruption drop is anecdotal counts, and the gold-free regime-diagnostic is partly tautological (signal C, frac(W==Z), is essentially the win rate of signal A, and 'the gate keeps the same facts so the wedge is null' is close to a mechanical restatement of the result rather than a prediction) and is admitted to be a '2-anchor illustration' that mispredicts the CLUTRR self-consistency point. The redeeming element is the marginal-vs-paired conceptual lesson, which is real and generalizable but currently demonstrated only on underpowered, confounded data.",
      "improvements": [
        "Elevate and harden the marginal-vs-paired lesson into the paper's primary contribution with a clean, controlled demonstration: e.g., a synthetic or semi-synthetic construction where marginal (distributional) exchangeability holds by design yet the paired sign-flip property provably fails, ideally with a small theorem or a mechanism that predicts WHEN the two diverge for LLM scorers. That would turn an underpowered empirical curiosity into a citable, general result.",
        "Either strengthen the regime-diagnostic (more anchors, a real held-out predictive evaluation, and an honest statement that signals A and C are redundant) or demote it from 'substantive novel contribution' to a diagnostic heuristic, so the contribution claims match what the evidence supports.",
        "Scale the application anchor enough to reach CI-separation on the hallucination reduction; the goal's hard requirement is a QUANTIFIED reduction, and a directional-only result does not yet satisfy it at a publishable standard."
      ]
    }
  ],
  "critiques": [
    {
      "category": "evidence",
      "severity": "major",
      "description": "Pervasive underpowering undermines nearly every affirmative claim. The central disconfirmation is computed on a 40-document checkpoint with only 12 admitted multi-hop candidates (the paper concedes this in Limitation 3). The marginal-exchangeability crux that makes the disconfirmation 'instructive' rests on borderline full-distribution p-values (KS 0.058, MW 0.061, AD 0.061, perm 0.060 -- all within ~0.01 of rejecting) and a 12-pair admission tail. The application reduction reaches 0 of 40 cells with CI separation at n=24. The multi-hop corruption headline (0.48->0.18) is 11 vs 23 derived conclusions with no CI, and is driven entirely by the regulatory genre (regulatory 12->3 derived, legal already 0.0, news derives 0). The S1b difficulty ladder has only 2 false pairs per rung, making its win-rates pure noise. The only well-powered results are the Re-DocRED null and its 267-conclusion multi-hop comparison. For a top venue, the paper's positive narrative and its central conceptual claim both need power they currently lack.",
      "suggested_action": "Execute the powered CLUTRR self-consistency diagonal (the ~593-doc run the artifact identifies as the intended final version) so the headline disconfirmation and the crux p-values are not borderline. Report the corruption result with bootstrap CIs and flag its single-genre origin. Either power the S1b ladder or remove the specific 'detects only gross decoys' narrative and present it purely as 'underpowered, cannot certify paired validity.' Scale the application anchor toward CI separation on the reduction."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The central disconfirmation is confounded with a deliberately pathological extractor, so the generalizable lesson cannot be cleanly attributed. The multi-hop family is ~85% genuinely false precisely because gpt-4.1-nano's forced multi-hop relation accuracy is only 0.17 (verified: multihop_relation_accuracy=0.169, n_false_total=158/186). Realized FDR 1.0 (all 12 admitted false) and the paired sign-flip failure may be specific to a regime where a tiny model cannot score its own multi-hop errors at all, rather than an intrinsic property of decoy-gating at the LLM boundary. The paper states the marginal-vs-paired gap 'as a limitation of the entire decoy-competition approach,' which over-generalizes from a single weak-model, single-family observation. A reviewer cannot distinguish 'knockoffs fundamentally don't transfer' from 'this extractor is too weak for any admission method to help.'",
      "suggested_action": "Add at least one diagonal with a stronger extractor and/or on a less error-dense family (or a controlled construction where the false-positive density is varied), and show whether the paired sign-flip failure persists. If it does, the 'limitation of the entire approach' claim is earned; if it does not, scope the claim to the error-dense/weak-scorer regime. This is the single change that most increases the credibility and reach of the paper's headline lesson."
    },
    {
      "category": "novelty",
      "severity": "major",
      "description": "The salvaged 'gold-free regime-diagnostic,' sold as a substantive novel contribution, is partly tautological and over-stated. Its four signals are not independent: signal C (frac(W==Z)=0.939, admitted-set Spearman 0.991) is mechanically the same quantity as the signal-A win rate, because W_i=Z_i exactly when the real out-scores its decoy. 'The gate keeps and orders the same facts as the plain threshold, so the wedge is mechanically null' is therefore close to a restatement of the realized null rather than an independent prediction, and the one case where the prediction is 'correct' (Re-DocRED) is the case where the prediction is nearly forced. The paper itself concedes the 2-axis map is a '2-anchor illustration, not a powered regression' and that it mispredicts the CLUTRR self-consistency point. As framed, the contribution claim exceeds the evidence.",
      "suggested_action": "Acknowledge the redundancy between signals A and C explicitly, and either (a) demote the regime-diagnostic to a heuristic and lead instead with the marginal-vs-paired conceptual result as the primary contribution, or (b) validate the diagnostic predictively on several additional anchors/regimes with a genuine held-out evaluation so the '2-axis map' is supported by more than two-to-three points. Avoid presenting a near-mechanical observation ('W==Z so ranking unchanged') as a forecast."
    },
    {
      "category": "scope",
      "severity": "major",
      "description": "The goal's binding deliverable -- a QUANTIFIED reduction in hallucination rate on short professionally-written documents -- is met only directionally. On the 24-document application anchor, the gate's pooled hallucinated-fact rate (0.178 logprob / 0.183 self-consistency vs raw 0.243, ~25-27% relative) reaches CI separation in 0 of 40 cells, the gate certifies only at alpha=0.5, and 117 of 210 reals are gold-undecidable so the rate is computed over a small decidable subset with silver bounds. Strictly, the mandated quantified reduction is not statistically established at the point where the paper claims the 'application headline.' The corruption-propagation result is the more convincing piece but is itself anecdotal in count.",
      "suggested_action": "Expand the application anchor (more documents per genre, and/or a cleaner crisp-gold subset to shrink the undecidable fraction) until at least the pooled reduction reaches CI separation, then present THAT as the application headline. Until then, state plainly at the point of claim that the reduction is directional and not significant at n=24, and that the binding deliverable is demonstrated as a trend with auditable provenance rather than a significant reduction."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "The figures are present only as bare [FIGURE:fig1]-[FIGURE:fig5] markers with no captions or descriptions in the manuscript body. This was raised in the previous round and remains unaddressed. Because these are the load-bearing visuals (the calibration diagonal, the marginal-vs-paired CDFs, the application grid, the multi-hop corruption, the matched-recall wedge), a reviewer cannot assess whether they communicate the results effectively, and the instruction to 'assume each figure shows what its caption describes' cannot be applied when no caption exists.",
      "suggested_action": "Add a full caption and a short description to every figure. For the diagonal figure, mark the 1/k floor, the bootstrap CIs, and the gate-vs-plain-vs-swap separation; for the crux figure, overlay the decoy / spontaneous-error / true-positive CDFs and annotate the paired-win asymmetry; for the wedge figure, show all participating systems with CIs at the matched operating point."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "Two localized over-statements relative to the artifacts. (1) The S1b narrative in Section 6.3 says the diagnostic 'detects only grossly out-of-context (foreign-entity) decoys,' but the ladder in the artifact shows L0_foreign_swap with detected_anti_conservative=FALSE while L1-L4 (in-distribution swaps/vocab/cf) show detected_anti_conservative=TRUE -- the opposite of the stated narrative (with n=2/rung this is noise either way, so the specific narrative is unsupported). (2) Section 6.3 concludes 'the paired failure is likewise not a circularity artifact,' but the generator!=scorer ablation (S2b) only tests the MARGINAL tail win-rate across (G,S) configs; it does not test the paired sign-flip property across configs, so paired-failure robustness to G!=S is asserted, not evidenced.",
      "suggested_action": "Rewrite the S1b sentence to match the data (or simply state the ladder is too underpowered to localize which decoy classes are detected). For (2), either run the paired-exchangeability statistic across the (G,S) configs to actually support the de-circularization claim for the paired layer, or soften the sentence to note that only marginal robustness to G!=S is demonstrated."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "Descoped goal requirements are honestly disclosed but reduce the match to the stated objective: OpenCyc/assertional commonsense grounding is replaced by WordNet->SUMO taxonomic typing only, and the probabilistic (ProbLog) reasoning layer is designed and specified but not executed -- yet the goal explicitly calls for upper-ontology background structure and an LLM-as-probabilistic-reasoner for fuzzy unification. The deterministic backward-chaining layer does not exercise the probabilistic/fuzzy-unification component that motivated the work.",
      "suggested_action": "Execute even a minimal ProbLog probabilistic run on one anchor (the artifact art_Cr6L9JpoewZi already specifies the exact get_evaluatable().evaluate() swap and the certificate->weight mapping), so the probabilistic-reasoner requirement is demonstrated rather than only specified. If it cannot be run this iteration, state in the contributions (not only the limitations) that the probabilistic layer is future work, so the abstract/intro do not imply it is delivered."
    }
  ],
  "score": 4,
  "confidence": 4
}
```

### [48] TOOL RESULT — Write · 2026-06-16 10:26:22 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/review_paper/review_paper/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This iteration is a substantial and commendable revision. The author addressed all four MAJOR issues from the previous round: the headline CLUTRR calibration diagonal is now computed under the diagnostic-validated K=5 self-consistency elicitation (not verbalized), the pre-registered disconfirmation is reported honestly, the application hallucination-reduction run on the 24-document legal/news/regulatory anchor is actually EXECUTED, and the Re-DocRED operational test is scaled to its true 152-document scope with all comparators participating and a powered multi-hop comparison. I independently verified every load-bearing number against the supplementary artifacts (art_sBLQqsdm3EIA, art_vkfyOl2OQNVx, art_RZC2468yZ-Jh) and found the paper to be exceptionally faithful to its evidence: realized FDR 1.0 / CI [0.66,1.0] / self-report 0.5 on multi-hop; crux KS p=0.058 (full) and 0.31 (tail) vs 5e-9 against true positives; application pooled 0.178/0.183 vs raw 0.243 with 0/40 cells CI-separated; corruption 0.48->0.18; Re-DocRED 267 derived conclusions, delta -0.004, prediction_correct. This reporting honesty is a real strength and is rare. The paper has, however, pivoted from 'we have a working label-free FDR gate' to 'the gate does NOT control FDR, and here is the conceptual reason plus an auditable pipeline.' As an honest negative-results paper it is well-constructed, but three issues keep it below the acceptance bar for a top venue: (1) nearly every affirmative claim is underpowered, including the central disconfirmation itself (40-doc checkpoint, 12 admitted pairs, borderline marginal p-values); (2) the disconfirmation is confounded with a deliberately pathological extractor (gpt-4.1-nano, multi-hop accuracy 0.17), so it is unclear whether the marginal-vs-paired failure is intrinsic to decoy-gating or an artifact of a model that cannot score its own multi-hop errors; and (3) the contributions that survive the disconfirmation (the regime-diagnostic, the directional application reduction) are individually weak. The conceptual lesson (marginal distributional exchangeability does not imply paired sign-flip exchangeability at the cutoff) is genuinely interesting and likely correct, but its empirical demonstration is currently too underpowered and too confounded to carry a top-venue paper on its own.\",\n  \"strengths\": [\n    \"Outstanding reporting honesty and reproducibility: I traced every headline number to the artifacts and they match exactly, including the numbers that disconfirm the method's central claim. The paper reports a pre-registered primary disconfirmation (realized FDR 1.0 at alpha*=0.5) rather than burying it, and surfaces a second-order self-report disconfirmation. This is the level of rigor top venues should reward.\",\n    \"A genuinely novel and useful conceptual contribution: the two-layer decomposition of knockoff validity at the LLM boundary into a marginal (distributional) layer and a paired (sign-flip) layer, with the demonstration that property-matched-decoy/win-rate diagnostics (imported from genomics/proteomics) live entirely in the marginal layer and therefore over-certify the gate. To my knowledge this marginal-vs-paired gap has not been articulated for knockoffs transplanted to LLM scoring, and it is a transferable lesson.\",\n    \"Clear and well-cited differentiation from prior work. The label-free / intermediate-admission / tested-exchangeability positioning is correctly distinguished from labeled conformal selection (Jin-Candes), multiple-testing hallucination detection (Li et al.), conformal link prediction (Marandon), and conformal factuality (Mohri-Hashimoto). My literature search confirmed no existing work applies knockoff/target-decoy FDR control at the text-to-logic admission boundary, and that the conformal-for-LLM-factuality neighbors are all labeled and certify model outputs.\",\n    \"The end-to-end auditable pipeline is real and executed: typed extraction (WordNet->SUMO), the knockoff+ gate, entrapment corroboration, and a backward-chaining proof engine emitting JSON+DOT trace-graphs whose leaves carry provenance, decoy, and entrapment certificates. This directly serves the goal's interpretability mandate, and the worked legal/regulatory proof examples (including an exposed rejected leaf) are convincing.\",\n    \"Honest, well-designed experimental protocol: pre-registered claim chain with explicit verdicts, the 1/k admission-floor accounting that prevents 'confirmed-by-conservatism' artifacts, document-block bootstrap CIs, BH multiplicity control, and a clean division of labor across the three anchors (CLUTRR for crisp-gold calibration, application anchor for genre-faithful reduction, Re-DocRED for the operational wedge).\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"Claims are now honestly and accurately supported by the artifacts; the central disconfirmation is solid in direction (12/12 admitted multi-hop facts false, CI entirely above alpha*). Methodology (knockoff+, entrapment, isolated provenance-blinded scoring, bootstrap CIs, BH) is appropriate and faithfully implemented. Held back from 4 by pervasive underpowering (the headline diagonal is a 40-doc checkpoint with 12 admitted pairs; the marginal crux rests on borderline p-values of 0.058/0.061; the application reduction reaches 0/40 CI separation; the multi-hop corruption rests on 11 vs 23 conclusions with no CI) and by the weak-extractor confound that prevents attributing the disconfirmation to the method rather than to the base model.\",\n      \"improvements\": [\n        \"Run the powered CLUTRR self-consistency diagonal (the artifact itself flags the ~593-doc run as the intended final version) so the headline disconfirmation and the marginal-vs-paired crux no longer rest on 12 admitted pairs and p=0.058. The direction is unlikely to reverse, but power converts an 'interesting checkpoint' into a defensible headline.\",\n        \"Disentangle the disconfirmation from extractor quality: repeat the diagonal with a stronger extractor (or on a less error-dense family) to show whether the paired sign-flip failure persists when the candidate pool is not ~85% false. Without this, a reviewer cannot tell if the lesson is 'knockoffs fundamentally fail at the LLM boundary' or 'gpt-4.1-nano cannot score its own multi-hop errors.'\",\n        \"Report the multi-hop corruption result (0.48->0.18) with document-block bootstrap CIs and note explicitly that it is driven entirely by the regulatory genre (12->3 derived conclusions; legal already 0.0, news derives 0). At these counts it is anecdotal; either power it or present it as illustrative rather than 'the clearest positive.'\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The writing is precise, the narrative is coherent, and the honest framing is handled gracefully. But the figures appear only as bare [FIGURE:fig1]-[fig5] markers with no captions or descriptions in the manuscript body (flagged in the previous round, still unaddressed), so a reader cannot assess what the load-bearing figures communicate. The paper is also extremely dense with a large alphabet of claim codes (S0, S1, S1b, S2, S2-self, S2b, S3, S4, S4b) that taxes the reader, and contains at least one internal inconsistency between narrative and tabulated data (the S1b ladder).\",\n      \"improvements\": [\n        \"Add a complete caption plus a one-to-two sentence description for every figure. The realized-FDR-vs-alpha diagonal must mark the 1/k floor, the bootstrap CIs, and visibly separate the gate from the plain and swap baselines; the marginal-vs-paired figure should show the decoy/spontaneous/true-positive CDFs and the paired win asymmetry; the application figure should show the per-genre grid with CIs; the Re-DocRED figure should show the wedge with all participating systems.\",\n        \"Reduce reader load: collapse the claim-code zoo into a single clearly-labeled table (already partly done in Table 2) and refer to results by what they show rather than by code, or add a one-line legend mapping each code to a plain-English claim.\",\n        \"Fix the S1b narrative/data inconsistency (see the rigor critique) so the text does not contradict its own ladder.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 2,\n      \"justification\": \"The central proposed mechanism (a certified label-free FDR gate) is disconfirmed on the populable family, so the headline 'first label-free FDR knob' becomes 'first to propose and then disconfirm.' The contributions that survive are individually thin: the application hallucination reduction is directional only (0/40 CI-separated), the corruption drop is anecdotal counts, and the gold-free regime-diagnostic is partly tautological (signal C, frac(W==Z), is essentially the win rate of signal A, and 'the gate keeps the same facts so the wedge is null' is close to a mechanical restatement of the result rather than a prediction) and is admitted to be a '2-anchor illustration' that mispredicts the CLUTRR self-consistency point. The redeeming element is the marginal-vs-paired conceptual lesson, which is real and generalizable but currently demonstrated only on underpowered, confounded data.\",\n      \"improvements\": [\n        \"Elevate and harden the marginal-vs-paired lesson into the paper's primary contribution with a clean, controlled demonstration: e.g., a synthetic or semi-synthetic construction where marginal (distributional) exchangeability holds by design yet the paired sign-flip property provably fails, ideally with a small theorem or a mechanism that predicts WHEN the two diverge for LLM scorers. That would turn an underpowered empirical curiosity into a citable, general result.\",\n        \"Either strengthen the regime-diagnostic (more anchors, a real held-out predictive evaluation, and an honest statement that signals A and C are redundant) or demote it from 'substantive novel contribution' to a diagnostic heuristic, so the contribution claims match what the evidence supports.\",\n        \"Scale the application anchor enough to reach CI-separation on the hallucination reduction; the goal's hard requirement is a QUANTIFIED reduction, and a directional-only result does not yet satisfy it at a publishable standard.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"Pervasive underpowering undermines nearly every affirmative claim. The central disconfirmation is computed on a 40-document checkpoint with only 12 admitted multi-hop candidates (the paper concedes this in Limitation 3). The marginal-exchangeability crux that makes the disconfirmation 'instructive' rests on borderline full-distribution p-values (KS 0.058, MW 0.061, AD 0.061, perm 0.060 -- all within ~0.01 of rejecting) and a 12-pair admission tail. The application reduction reaches 0 of 40 cells with CI separation at n=24. The multi-hop corruption headline (0.48->0.18) is 11 vs 23 derived conclusions with no CI, and is driven entirely by the regulatory genre (regulatory 12->3 derived, legal already 0.0, news derives 0). The S1b difficulty ladder has only 2 false pairs per rung, making its win-rates pure noise. The only well-powered results are the Re-DocRED null and its 267-conclusion multi-hop comparison. For a top venue, the paper's positive narrative and its central conceptual claim both need power they currently lack.\",\n      \"suggested_action\": \"Execute the powered CLUTRR self-consistency diagonal (the ~593-doc run the artifact identifies as the intended final version) so the headline disconfirmation and the crux p-values are not borderline. Report the corruption result with bootstrap CIs and flag its single-genre origin. Either power the S1b ladder or remove the specific 'detects only gross decoys' narrative and present it purely as 'underpowered, cannot certify paired validity.' Scale the application anchor toward CI separation on the reduction.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The central disconfirmation is confounded with a deliberately pathological extractor, so the generalizable lesson cannot be cleanly attributed. The multi-hop family is ~85% genuinely false precisely because gpt-4.1-nano's forced multi-hop relation accuracy is only 0.17 (verified: multihop_relation_accuracy=0.169, n_false_total=158/186). Realized FDR 1.0 (all 12 admitted false) and the paired sign-flip failure may be specific to a regime where a tiny model cannot score its own multi-hop errors at all, rather than an intrinsic property of decoy-gating at the LLM boundary. The paper states the marginal-vs-paired gap 'as a limitation of the entire decoy-competition approach,' which over-generalizes from a single weak-model, single-family observation. A reviewer cannot distinguish 'knockoffs fundamentally don't transfer' from 'this extractor is too weak for any admission method to help.'\",\n      \"suggested_action\": \"Add at least one diagonal with a stronger extractor and/or on a less error-dense family (or a controlled construction where the false-positive density is varied), and show whether the paired sign-flip failure persists. If it does, the 'limitation of the entire approach' claim is earned; if it does not, scope the claim to the error-dense/weak-scorer regime. This is the single change that most increases the credibility and reach of the paper's headline lesson.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"major\",\n      \"description\": \"The salvaged 'gold-free regime-diagnostic,' sold as a substantive novel contribution, is partly tautological and over-stated. Its four signals are not independent: signal C (frac(W==Z)=0.939, admitted-set Spearman 0.991) is mechanically the same quantity as the signal-A win rate, because W_i=Z_i exactly when the real out-scores its decoy. 'The gate keeps and orders the same facts as the plain threshold, so the wedge is mechanically null' is therefore close to a restatement of the realized null rather than an independent prediction, and the one case where the prediction is 'correct' (Re-DocRED) is the case where the prediction is nearly forced. The paper itself concedes the 2-axis map is a '2-anchor illustration, not a powered regression' and that it mispredicts the CLUTRR self-consistency point. As framed, the contribution claim exceeds the evidence.\",\n      \"suggested_action\": \"Acknowledge the redundancy between signals A and C explicitly, and either (a) demote the regime-diagnostic to a heuristic and lead instead with the marginal-vs-paired conceptual result as the primary contribution, or (b) validate the diagnostic predictively on several additional anchors/regimes with a genuine held-out evaluation so the '2-axis map' is supported by more than two-to-three points. Avoid presenting a near-mechanical observation ('W==Z so ranking unchanged') as a forecast.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"major\",\n      \"description\": \"The goal's binding deliverable -- a QUANTIFIED reduction in hallucination rate on short professionally-written documents -- is met only directionally. On the 24-document application anchor, the gate's pooled hallucinated-fact rate (0.178 logprob / 0.183 self-consistency vs raw 0.243, ~25-27% relative) reaches CI separation in 0 of 40 cells, the gate certifies only at alpha=0.5, and 117 of 210 reals are gold-undecidable so the rate is computed over a small decidable subset with silver bounds. Strictly, the mandated quantified reduction is not statistically established at the point where the paper claims the 'application headline.' The corruption-propagation result is the more convincing piece but is itself anecdotal in count.\",\n      \"suggested_action\": \"Expand the application anchor (more documents per genre, and/or a cleaner crisp-gold subset to shrink the undecidable fraction) until at least the pooled reduction reaches CI separation, then present THAT as the application headline. Until then, state plainly at the point of claim that the reduction is directional and not significant at n=24, and that the binding deliverable is demonstrated as a trend with auditable provenance rather than a significant reduction.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The figures are present only as bare [FIGURE:fig1]-[FIGURE:fig5] markers with no captions or descriptions in the manuscript body. This was raised in the previous round and remains unaddressed. Because these are the load-bearing visuals (the calibration diagonal, the marginal-vs-paired CDFs, the application grid, the multi-hop corruption, the matched-recall wedge), a reviewer cannot assess whether they communicate the results effectively, and the instruction to 'assume each figure shows what its caption describes' cannot be applied when no caption exists.\",\n      \"suggested_action\": \"Add a full caption and a short description to every figure. For the diagonal figure, mark the 1/k floor, the bootstrap CIs, and the gate-vs-plain-vs-swap separation; for the crux figure, overlay the decoy / spontaneous-error / true-positive CDFs and annotate the paired-win asymmetry; for the wedge figure, show all participating systems with CIs at the matched operating point.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"Two localized over-statements relative to the artifacts. (1) The S1b narrative in Section 6.3 says the diagnostic 'detects only grossly out-of-context (foreign-entity) decoys,' but the ladder in the artifact shows L0_foreign_swap with detected_anti_conservative=FALSE while L1-L4 (in-distribution swaps/vocab/cf) show detected_anti_conservative=TRUE -- the opposite of the stated narrative (with n=2/rung this is noise either way, so the specific narrative is unsupported). (2) Section 6.3 concludes 'the paired failure is likewise not a circularity artifact,' but the generator!=scorer ablation (S2b) only tests the MARGINAL tail win-rate across (G,S) configs; it does not test the paired sign-flip property across configs, so paired-failure robustness to G!=S is asserted, not evidenced.\",\n      \"suggested_action\": \"Rewrite the S1b sentence to match the data (or simply state the ladder is too underpowered to localize which decoy classes are detected). For (2), either run the paired-exchangeability statistic across the (G,S) configs to actually support the de-circularization claim for the paired layer, or soften the sentence to note that only marginal robustness to G!=S is demonstrated.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"Descoped goal requirements are honestly disclosed but reduce the match to the stated objective: OpenCyc/assertional commonsense grounding is replaced by WordNet->SUMO taxonomic typing only, and the probabilistic (ProbLog) reasoning layer is designed and specified but not executed -- yet the goal explicitly calls for upper-ontology background structure and an LLM-as-probabilistic-reasoner for fuzzy unification. The deterministic backward-chaining layer does not exercise the probabilistic/fuzzy-unification component that motivated the work.\",\n      \"suggested_action\": \"Execute even a minimal ProbLog probabilistic run on one anchor (the artifact art_Cr6L9JpoewZi already specifies the exact get_evaluatable().evaluate() swap and the certificate->weight mapping), so the probabilistic-reasoner requirement is demonstrated rather than only specified. If it cannot be run this iteration, state in the contributions (not only the limitations) that the probabilistic layer is future work, so the abstract/intro do not imply it is delivered.\"\n    }\n  ],\n  \"score\": 4,\n  \"confidence\": 4\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [49] ASSISTANT · 2026-06-16 10:26:36 UTC

```
I've completed the review and written the structured output. Here's a summary of my assessment.

## Review Summary

**Score: 4/10 (Borderline Reject), Confidence: 4**

I verified every load-bearing number against the supplementary artifacts and found the paper **exceptionally faithful to its evidence** — realized FDR 1.0 / CI [0.66,1.0] / self-report 0.5 on multi-hop, crux KS p=0.058, application 0.178 vs 0.243 with 0/40 cells CI-separated, Re-DocRED 267 conclusions with delta −0.004 and prediction_correct. All numbers match.

**The four prior MAJOR issues are substantially addressed:** self-consistency is now the headline elicitation, the disconfirmation is reported honestly, the application run is executed, and Re-DocRED is scaled to 152 docs with all comparators participating.

**Why it still sits below the bar** (the three highest-leverage remaining issues):

1. **Pervasive underpowering** — the central disconfirmation rests on a 40-doc checkpoint with 12 admitted pairs; the marginal-exchangeability crux on borderline p-values (0.058); the application reduction reaches 0/40 CI separation; the corruption result is 11 vs 23 conclusions driven by one genre; the S1b ladder is n=2/rung.

2. **Weak-extractor confound** — the multi-hop family is ~85% false *because* gpt-4.1-nano scores 0.17 accuracy, so the disconfirmation cannot be cleanly attributed to the method vs. the base model. The "limitation of the entire decoy-competition approach" claim over-generalizes from one weak-model, one-family observation.

3. **Thin salvaged contributions** — the regime-diagnostic's signal C (frac(W==Z)) is mechanically the win rate of signal A, making "the gate keeps the same facts → null wedge" a near-restatement rather than a prediction; the diagnostic is admittedly a 2-anchor illustration that mispredicts the CLUTRR case.

**Genuine strengths I credited:** outstanding reporting honesty (negative results faithfully reported), a real and generalizable conceptual lesson (marginal distributional exchangeability ≠ paired sign-flip exchangeability at the cutoff), correct novelty positioning confirmed by literature search, and an executed auditable pipeline with per-leaf certificates.

The dimension scores are Soundness 3, Presentation 3, Contribution 2. The feedback is oriented toward the highest score-impact fixes for the next iteration: power the headline diagonal, disentangle the extractor confound, harden the marginal-vs-paired lesson into the primary contribution, scale the application result to significance, and add figure captions.
```
