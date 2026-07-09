# gen_paper_text — test_idea

> Phase: `invention_loop` · round 4 · `gen_paper_text`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 12:51:33 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_paper_text/gen_paper_text
```

### [2] SYSTEM-USER prompt · 2026-06-16 12:51:39 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.


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

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (evidence) Pervasive underpowering undermines nearly every affirmative claim. The central disconfirmation is computed on a 40-document checkpoint with only 12 admitted multi-hop candidates (the paper concedes this in Limitation 3). The marginal-exchangeability crux that makes the disconfirmation 'instructive' rests on borderline full-distribution p-values (KS 0.058, MW 0.061, AD 0.061, perm 0.060 -- all within ~0.01 of rejecting) and a 12-pair admission tail. The application reduction reaches 0 of 40 cells with CI separation at n=24. The multi-hop corruption headline (0.48->0.18) is 11 vs 23 derived conclusions with no CI, and is driven entirely by the regulatory genre (regulatory 12->3 derived, legal already 0.0, news derives 0). The S1b difficulty ladder has only 2 false pairs per rung, making its win-rates pure noise. The only well-powered results are the Re-DocRED null and its 267-conclusion multi-hop comparison. For a top venue, the paper's positive narrative and its central conceptual claim both need power they currently lack.
  Action: Execute the powered CLUTRR self-consistency diagonal (the ~593-doc run the artifact identifies as the intended final version) so the headline disconfirmation and the crux p-values are not borderline. Report the corruption result with bootstrap CIs and flag its single-genre origin. Either power the S1b ladder or remove the specific 'detects only gross decoys' narrative and present it purely as 'underpowered, cannot certify paired validity.' Scale the application anchor toward CI separation on the reduction.
- [MAJOR] (methodology) The central disconfirmation is confounded with a deliberately pathological extractor, so the generalizable lesson cannot be cleanly attributed. The multi-hop family is ~85% genuinely false precisely because gpt-4.1-nano's forced multi-hop relation accuracy is only 0.17 (verified: multihop_relation_accuracy=0.169, n_false_total=158/186). Realized FDR 1.0 (all 12 admitted false) and the paired sign-flip failure may be specific to a regime where a tiny model cannot score its own multi-hop errors at all, rather than an intrinsic property of decoy-gating at the LLM boundary. The paper states the marginal-vs-paired gap 'as a limitation of the entire decoy-competition approach,' which over-generalizes from a single weak-model, single-family observation. A reviewer cannot distinguish 'knockoffs fundamentally don't transfer' from 'this extractor is too weak for any admission method to help.'
  Action: Add at least one diagonal with a stronger extractor and/or on a less error-dense family (or a controlled construction where the false-positive density is varied), and show whether the paired sign-flip failure persists. If it does, the 'limitation of the entire approach' claim is earned; if it does not, scope the claim to the error-dense/weak-scorer regime. This is the single change that most increases the credibility and reach of the paper's headline lesson.
- [MAJOR] (novelty) The salvaged 'gold-free regime-diagnostic,' sold as a substantive novel contribution, is partly tautological and over-stated. Its four signals are not independent: signal C (frac(W==Z)=0.939, admitted-set Spearman 0.991) is mechanically the same quantity as the signal-A win rate, because W_i=Z_i exactly when the real out-scores its decoy. 'The gate keeps and orders the same facts as the plain threshold, so the wedge is mechanically null' is therefore close to a restatement of the realized null rather than an independent prediction, and the one case where the prediction is 'correct' (Re-DocRED) is the case where the prediction is nearly forced. The paper itself concedes the 2-axis map is a '2-anchor illustration, not a powered regression' and that it mispredicts the CLUTRR self-consistency point. As framed, the contribution claim exceeds the evidence.
  Action: Acknowledge the redundancy between signals A and C explicitly, and either (a) demote the regime-diagnostic to a heuristic and lead instead with the marginal-vs-paired conceptual result as the primary contribution, or (b) validate the diagnostic predictively on several additional anchors/regimes with a genuine held-out evaluation so the '2-axis map' is supported by more than two-to-three points. Avoid presenting a near-mechanical observation ('W==Z so ranking unchanged') as a forecast.
- [MAJOR] (scope) The goal's binding deliverable -- a QUANTIFIED reduction in hallucination rate on short professionally-written documents -- is met only directionally. On the 24-document application anchor, the gate's pooled hallucinated-fact rate (0.178 logprob / 0.183 self-consistency vs raw 0.243, ~25-27% relative) reaches CI separation in 0 of 40 cells, the gate certifies only at alpha=0.5, and 117 of 210 reals are gold-undecidable so the rate is computed over a small decidable subset with silver bounds. Strictly, the mandated quantified reduction is not statistically established at the point where the paper claims the 'application headline.' The corruption-propagation result is the more convincing piece but is itself anecdotal in count.
  Action: Expand the application anchor (more documents per genre, and/or a cleaner crisp-gold subset to shrink the undecidable fraction) until at least the pooled reduction reaches CI separation, then present THAT as the application headline. Until then, state plainly at the point of claim that the reduction is directional and not significant at n=24, and that the binding deliverable is demonstrated as a trend with auditable provenance rather than a significant reduction.
- [MINOR] (clarity) The figures are present only as bare [FIGURE:fig1]-[FIGURE:fig5] markers with no captions or descriptions in the manuscript body. This was raised in the previous round and remains unaddressed. Because these are the load-bearing visuals (the calibration diagonal, the marginal-vs-paired CDFs, the application grid, the multi-hop corruption, the matched-recall wedge), a reviewer cannot assess whether they communicate the results effectively, and the instruction to 'assume each figure shows what its caption describes' cannot be applied when no caption exists.
  Action: Add a full caption and a short description to every figure. For the diagonal figure, mark the 1/k floor, the bootstrap CIs, and the gate-vs-plain-vs-swap separation; for the crux figure, overlay the decoy / spontaneous-error / true-positive CDFs and annotate the paired-win asymmetry; for the wedge figure, show all participating systems with CIs at the matched operating point.
- [MINOR] (rigor) Two localized over-statements relative to the artifacts. (1) The S1b narrative in Section 6.3 says the diagnostic 'detects only grossly out-of-context (foreign-entity) decoys,' but the ladder in the artifact shows L0_foreign_swap with detected_anti_conservative=FALSE while L1-L4 (in-distribution swaps/vocab/cf) show detected_anti_conservative=TRUE -- the opposite of the stated narrative (with n=2/rung this is noise either way, so the specific narrative is unsupported). (2) Section 6.3 concludes 'the paired failure is likewise not a circularity artifact,' but the generator!=scorer ablation (S2b) only tests the MARGINAL tail win-rate across (G,S) configs; it does not test the paired sign-flip property across configs, so paired-failure robustness to G!=S is asserted, not evidenced.
  Action: Rewrite the S1b sentence to match the data (or simply state the ladder is too underpowered to localize which decoy classes are detected). For (2), either run the paired-exchangeability statistic across the (G,S) configs to actually support the de-circularization claim for the paired layer, or soften the sentence to note that only marginal robustness to G!=S is demonstrated.
- [MINOR] (rigor) Descoped goal requirements are honestly disclosed but reduce the match to the stated objective: OpenCyc/assertional commonsense grounding is replaced by WordNet->SUMO taxonomic typing only, and the probabilistic (ProbLog) reasoning layer is designed and specified but not executed -- yet the goal explicitly calls for upper-ontology background structure and an LLM-as-probabilistic-reasoner for fuzzy unification. The deterministic backward-chaining layer does not exercise the probabilistic/fuzzy-unification component that motivated the work.
  Action: Execute even a minimal ProbLog probabilistic run on one anchor (the artifact art_Cr6L9JpoewZi already specifies the exact get_evaluatable().evaluate() swap and the certificate->weight mapping), so the probabilistic-reasoner requirement is demonstrated rather than only specified. If it cannot be run this iteration, state in the contributions (not only the limitations) that the probabilistic layer is future work, so the abstract/intro do not imply it is delivered.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: >-
  Decoy-Gated Neuro-Symbolic Extraction: A Label-Free FDR Gate Whose Validity Hinges on PAIRED (Not Just Marginal) Decoy Exchangeability
  -- Power and De-Confound the CLUTRR Disconfirmation Against Extractor Strength, Establish the Professional-Document Hallucination-Reduction
  Headline at CI Separation, and Execute the Probabilistic Reasoner
hypothesis: |-
  MECHANISM (unchanged, one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  WHAT IS NOW EXECUTED (iteration-3, MEASURED). Three experiments ran for ~$1.4 this iteration (~$2.6 cumulative of the $10 cap): (P1) the self-consistency CLUTRR calibration diagonal [art_sBLQqsdm3EIA] -- BUT on a 40-doc CHECKPOINT (410 reals: 123 true / 287 spontaneous false), NOT the powered ~593-doc run the artifact itself names as the intended final version; (P2) the 24-doc legal/news/regulatory APPLICATION headline [art_vkfyOl2OQNVx], executed end-to-end with auditable trace-graphs (210 reals: 42 true / 51 false / 117 gold-undecidable); (P3) the Re-DocRED operational wedge scaled to 152 confirmatory docs and reframed as a gold-free regime-diagnostic [art_RZC2468yZ-Jh]. Iteration-4's job is NOT to re-build but to POWER and DE-CONFOUND the central finding, SCALE the application to statistical significance, and execute the still-missing probabilistic reasoner the goal hard-requires.

  THE DECISIVE FINDING (what the evidence now says, honestly). The central scientific contribution has SHIFTED from 'elicitation-dependence' to a sharper, deeper distinction -- but that finding is currently CONFOUNDED and UNDERPOWERED, which dictates the entire iteration-4 mandate.
    (1) THE HEADLINE CONCEPTUAL LESSON IS MARGINAL != PAIRED EXCHANGEABILITY. Under the diagnostic-validated K=5 self-consistency elicitation, the counterfactual-decoy score distribution is statistically indistinguishable from the model's OWN spontaneous-error distribution (full-dist KS p=0.058, MW p=0.061, AD p=0.061, perm p=0.060 -- all FAIL to reject; admission-tail top-25% KS p=0.31) and sharply distinct from true positives (KS p=5e-9, MW p=4e-12). That is MARGINAL (distributional) exchangeability -- exactly the property DeepCoy-style decoy design and the win-rate/CDF diagnostics target, and it HOLDS. Yet knockoff+ requires the strictly stronger PER-PAIR sign-flip property at the cutoff, and it FAILS: among the 12 admitted multi_hop reals the model scored EACH false real above its own matched decoy, so realized FDR is 1.0 at the only certifiable alpha*=0.5 (doc-block CI [0.66,1.0] entirely above alpha*) and the gate's self-report decoy_fdr_hat=0.5 undershoots realized 1.0. The pre-registered primary disconfirmation FIRES on both calibration and self-report criteria. The win-rate diagnostic, being a MARGINAL statistic, structurally cannot see this gap.
    (2) THE DISCONFIRMATION IS CONFOUNDED WITH A PATHOLOGICAL EXTRACTOR AND IS UNDERPOWERED -- so the 'limitation of the entire decoy-competition approach' claim is NOT YET EARNED. The multi_hop family is ~85% genuinely false ONLY because gpt-4.1-nano's forced multi-hop relation accuracy is 0.169 (n_false 158/186) -- a regime where a tiny model essentially cannot score its own multi-hop errors at all. Realized FDR 1.0 (all 12 admitted false) and the paired sign-flip failure may therefore reflect 'this extractor is too weak for ANY admission method to help' rather than an intrinsic property of decoy-gating at the LLM boundary. Compounding this, EVERY affirmative number rests on thin power: 40 docs / 12 admitted pairs, crux p-values all within ~0.01 of rejecting (0.058-0.061), the S1b ladder has only 2 false pairs/rung. A reviewer cannot distinguish 'knockoffs fundamentally do not transfer' from 'this single weak-model, single-family checkpoint is too noisy to conclude anything.' DE-CONFOUNDING + POWERING this is the single change that most increases the credibility and reach of the headline lesson.
    (3) THE ONLY WELL-POWERED RESULT IS NEGATIVE-OPERATIONAL, AND THE APPLICATION HEADLINE IS DIRECTIONAL-ONLY. On 152 Re-DocRED docs the operational wedge over plain thresholding is cleanly DISCONFIRMED at recall<=0.075 ('thresholding-is-enough when the base scorer is calibrated'), and its 267-conclusion multi-hop comparison is genuinely powered (halluc rate ~0.79 both systems, delta -0.004, CI [-0.018,0.008]). On the 24-doc application anchor the ~25% relative atomic hallucination reduction (gate 0.183 self-consistency / 0.178 logprob vs raw 0.243) reaches CI separation in 0 of 40 cells, and the multi-hop corruption drop (0.48->0.18) is 11 vs 23 derived conclusions with NO CI and is driven entirely by the regulatory genre (regulatory 12->3; legal already 0.0; news derives 0). The honest unifying principle survives: the gate adds value only where the base elicitation is tail-overconfident AND decoys are paired-exchangeable, and is redundant where the base scorer is already calibrated -- but every quantitative leg of that principle needs power it currently lacks.

  THE ONE THING THAT MATTERS NOW (iteration-4 mandate, in priority order).
    P1 -- POWER AND DE-CONFOUND THE CALIBRATION DIAGONAL (this is the headline experiment). (a) POWER: execute the full ~593-doc self-consistency CLUTRR diagonal the artifact already specifies, so the disconfirmation and the marginal-exchangeability crux p-values are NOT borderline (target: crux full-dist tests clearly fail-to-reject or clearly reject with n well above the current 12-pair tail; report the realized-FDR-vs-alpha diagonal with decoy_fdr_hat vs realized vs alpha across the certified grid). (b) DE-CONFOUND -- the decisive addition: run at least one diagonal with a STRONGER extractor (or a less error-dense family, or a controlled construction that VARIES false-positive density across, e.g., 20% / 50% / 85% genuine-false) and measure whether the PER-PAIR sign-flip failure PERSISTS. If the paired failure survives across extractor strength and false-positive density, the 'marginal != paired is a property of the LLM boundary' lesson is EARNED and becomes the paper's headline; if it vanishes with a competent extractor (i.e. the gate then controls realized FDR at alpha), SCOPE the claim to the error-dense/weak-scorer regime and report the positive 'gate works when the extractor can score its own errors' result instead. Either outcome is publishable; the current single-point observation is not. (c) Add a PAIRED-exchangeability statistic (per-pair win-rate over FALSE pairs at the cutoff) reported DISTINCTLY from the marginal win-rate, and compute it ACROSS the (G,S) configs (see de-circularization below).
    P2 -- ESTABLISH THE APPLICATION HEADLINE AT CI SEPARATION (the goal's binding deliverable). Scale the 24-doc legal/news/regulatory anchor toward statistical significance: more documents per genre AND a cleaner crisp-gold subset to shrink the 117/210 gold-undecidable fraction, until at least the POOLED hallucinated-fact reduction (gate vs raw LLM) reaches document-block-bootstrap CI separation; report the multi-hop corruption result WITH CIs and an explicit single-genre-origin flag. Until CI separation is reached, state PLAINLY at the point of claim that the reduction is DIRECTIONAL and not significant at the current n, and that the binding deliverable is demonstrated as a trend with auditable provenance, not a significant reduction. Continue exporting per-leaf-certified trace-graphs across all genres and elicitations and the full alpha grid.
    P3 -- LEAD WITH THE CONCEPTUAL RESULT; DEMOTE THE REGIME-DIAGNOSTIC. Make MARGINAL-vs-PAIRED exchangeability (P1) the paper's primary novel contribution. Acknowledge EXPLICITLY that the regime-diagnostic's signals are not independent -- signal C (frac(W==Z)=0.939, admitted-set Spearman rho=0.991) is mechanically the SAME quantity as signal-A tail win-rate, because W_i=Z_i exactly when the real out-scores its decoy, so 'the gate keeps and orders the same facts as the plain threshold, so the wedge is mechanically null' is close to a restatement of the realized null, not an independent forecast -- and either (a) DEMOTE the regime-diagnostic to a heuristic (default) or (b) validate it predictively on several additional anchors/regimes with a genuine held-out evaluation so the 2-axis map rests on more than 2-3 points. Do NOT present a near-mechanical observation as a forecast.
    P4 -- EXECUTE THE PROBABILISTIC REASONER (goal hard-requirement, currently only specified). Run even a MINIMAL ProbLog probabilistic-reasoning step on one anchor using the exact get_evaluatable().create_from(...).evaluate() swap and certificate->weight mapping already specified [art_Cr6L9JpoewZi], so the LLM-as-probabilistic-reasoner / fuzzy-unification requirement is DEMONSTRATED rather than only designed. If it cannot run, state in the CONTRIBUTIONS (not only limitations) that the probabilistic layer is future work, so the abstract/intro never imply it is delivered.

  THE GATE (one canonical statistic; unchanged). For each candidate i with real score Z_i and matched-decoy score Z~_i, the competition statistic is the knockoff+ signed maximum W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. NEW reporting requirements: (i) ALWAYS report the gate's internal estimate decoy_fdr_hat alongside realized FDR and alpha, so 'the estimate is anti-conservative' (decoy_fdr_hat < realized) is surfaced as its own failure mode; (ii) report the MARGINAL diagnostic (pooled decoy-vs-spontaneous-error win-rate / CDF tests) and the PAIRED diagnostic (per-pair win-rate over false pairs at the cutoff) SEPARATELY, because the central finding is precisely that the marginal can hold while the paired fails.

  VALIDITY HONESTY (now empirically grounded). knockoff+ delivers a finite-sample FDR GUARANTEE only under the joint-null PAIRED sign-flip property; for LLM decoys that property is UNPROVABLE. The iteration-3 evidence localizes the failure to a two-layer structure: a MARGINAL layer (decoy scores distributed like the model's spontaneous errors), which is label-free testable and which self-consistency RESTORES; and a PAIRED layer (false real and its decoy equally likely to take the larger score AS A PAIR), which the knockoff theorems actually require and which FAILS at the cutoff on the current evidence. The realized-FDR-vs-alpha diagonal IS the empirical test of the paired layer. The standard decoy-quality diagnostics imported from genomics/proteomics live entirely in the marginal layer and therefore OVER-CERTIFY the gate. CRITICAL CAVEAT carried into iteration-4: this two-layer story is, on present evidence, observed in ONE weak-extractor, error-dense, 12-pair regime; it is asserted as the paper's headline ONLY if P1's de-confounding shows the paired failure persists across extractor strength / false-positive density. If it does not persist, the validity story is re-scoped to the weak-scorer regime and the positive 'controls FDR with a competent extractor' result leads instead. The document-block bootstrap supplies realized-FDP CIs and a dependence diagnostic; it does NOT restore the guarantee.

  THE DIAGNOSTIC BLIND SPOT (materially qualifies the 'self-detecting gate' contribution). The headline was once 'tail diagnostics tell the practitioner which regime they are in.' Two faces of a blind spot remain: (1) STRUCTURAL -- a MARGINAL win-rate cannot certify PAIRED validity, period (this is the conceptual core, not a power issue). (2) UNDERPOWERED -- the S1b difficulty ladder L0..L4 has only 2 false pairs/rung, so its verdict (PARTIAL) is noise; the prior narrative that 'the diagnostic detects only grossly out-of-context (foreign-entity) decoys' is in fact CONTRADICTED by the artifact (L0 foreign-swap detected_anti_conservative=FALSE while L1-L4 in-distribution rungs=TRUE) and must be either powered or restated purely as 'underpowered, cannot localize which decoy classes are detected, cannot certify paired validity.' CLAIM S1b stands: a usable self-detecting gate REQUIRES a diagnostic that retains discriminating power in the valid regime AND that probes the PAIRED layer; iteration-4 supplies a powered paired-exchangeability diagnostic or reports the blind spot as a fundamental limitation and downgrades the 'tells you when to trust the gate' claim accordingly.

  DE-CIRCULARIZATION (MARGINAL settled; PAIRED not yet evidenced). The Generator!=Scorer ablation is ROBUST for the MARGINAL tail win-rate across all four (G,S) configs incl. decoys from gpt-4.1-nano scored by cross-family ministral-8b (CIs cover 0.5, e.g. 0.491 [0.37,0.61], KS p=0.999), so restored marginal exchangeability is NOT a shared-model artifact. HOWEVER -- a rigor gap surfaced this iteration -- the ablation tests ONLY the marginal statistic; the PAIRED sign-flip property has NOT been tested across (G,S) configs, so paired-failure robustness to G!=S is currently ASSERTED, not evidenced. Iteration-4 must either compute the paired-exchangeability statistic across the (G,S) configs to actually support de-circularization for the paired layer, or explicitly soften the claim to 'only marginal robustness to G!=S is demonstrated.'

  POWER (the binding gate for every affirmative claim). Phase-0 must demonstrate, UNDER SELF-CONSISTENCY, that the certified grid extends below the loose alpha*=0.5 (>= 1/alpha admissions AND >= N_false_min=40 genuine false admissions among reals) on the SCALED corpus before the diagonal is asserted at tighter alpha; the ~593-doc run is the vehicle. Crux full-distribution tests must move off the borderline; the application reduction must reach CI separation on the pooled metric; the corruption result must carry CIs. Any alpha / cell whose power floor is not reached is reported as a precondition, NEVER as 'confirmed by conservatism.'

  SCOPE / GOAL ALIGNMENT (the application is the binding deliverable). The goal targets ~3000-character professionally written legal/news/regulatory documents, upper-ontology grounding, an LLM probabilistic-reasoning engine at fuzzy unifications, auditable trace-graphs, and a QUANTIFIED hallucination reduction vs raw LLM. CLUTRR (synthetic kinship, crisp gold) hosts the powered+de-confounded calibration diagonal and the marginal-vs-paired lesson; Re-DocRED (Wikipedia prose, human gold) hosts the well-powered operational comparison; the 24-doc professional slice [art_UBTwyePql8NQ] hosts the application headline (WordNet->SUMO typing standing in for the discontinued OpenCyc, used ONLY for typing; minimal ProbLog probabilistic step; hallucination-reduction vs raw across both elicitations and all alpha; per-leaf-certified trace-graphs). If the application reduction cannot reach CI separation after scaling, report it as a directional trend with auditable provenance, never as a significant reduction.

  CLAIM CHAIN (each row independently testable; verdicts reflect iteration-3 evidence and the iteration-4 mandate).
    | # | CLAIM | STATUS | ITERATION-4 ACTION / PASS CRITERION |
    |---|-------|--------|-------------------------------------|
    | S0 | Score separation via tail-exchangeability SELECTION (not AUC) | PASS | confirm under the elicitation hosting the powered diagonal; verbalized/DINCO higher AUC (0.861/0.871) but fail the tail test; self-consistency tail win-rate 0.482 |
    | S1 | MARGINAL decoy match (decoy ~ spontaneous error, != true positive) | HOLDS but BORDERLINE/UNDERPOWERED (KS p=0.058 etc., 12-pair tail) | power to clearly fail-to-reject (or reject) on the ~593-doc run |
    | S1c (NEW, HEADLINE) | MARGINAL != PAIRED: marginal holds while per-pair sign-flip fails at the cutoff | OBSERVED but CONFOUNDED (weak extractor acc 0.17, error-dense, 12 pairs) | DE-CONFOUND across extractor strength / false-positive density; if paired failure persists -> earned headline; else scope to weak-scorer regime |
    | S1b | Diagnostic sensitivity / paired-layer detectability | FAIL/UNDERPOWERED (2 false pairs/rung; prior narrative contradicted by data) | power the ladder or report as purely underpowered; supply a paired-exchangeability diagnostic or report fundamental limitation |
    | S2 | Calibration diagonal (CLUTRR, self-consistency) | DISCONFIRMED on 40-doc checkpoint (realized 1.0 at alpha*=0.5, CI [0.66,1.0]) but UNDERPOWERED+CONFOUNDED | power to ~593 docs + de-confound; report decoy_fdr_hat vs realized vs alpha across certified grid |
    | S2-self | Gate self-report tracks realized | DISCONFIRMED on CLUTRR multi_hop (decoy_fdr_hat=0.5 < realized 1.0); CONSERVATIVE on application (>=realized in all 40 cells) | report both regimes; surface anti-conservative self-report as its own failure mode |
    | S2b | Generator!=Scorer de-circularization | MARGINAL ROBUST (4/4 cover 0.5); PAIRED NOT YET TESTED | compute the PAIRED statistic across (G,S) configs OR soften to 'marginal-only' |
    | S3 | Entrapment corroboration | AGREES loosely (FDP_hat high, e.g. application pooled 0.81 at alpha=0.5, honestly flagging loose admission) | report at alpha* and 0.5; restrict agreement claims to where they hold |
    | S4 | Operational wedge (Re-DocRED) | DISCONFIRMED, WELL-POWERED (152 docs, recall<=0.075; 267-conclusion multi-hop delta -0.004, CI [-0.018,0.008]) | stands; 'thresholding-is-enough when base scorer calibrated' |
    | S4b | Application hallucination reduction (professional docs) -- BINDING DELIVERABLE | EXECUTED but DIRECTIONAL (gate 0.183/0.178 vs raw 0.243 ~25%; 0/40 cells CI-separated); corruption 0.48->0.18 (11 vs 23, single-genre, no CI) | scale to POOLED CI separation; cleaner crisp gold to shrink 117/210 undecidable; corruption with CIs + single-genre flag |
    | S4c | Gold-free regime-diagnostic | NOVEL but PARTLY TAUTOLOGICAL (signal C == signal A; Re-DocRED prediction near-forced) | acknowledge A/C redundancy; demote to heuristic OR validate predictively on >=3 held-out anchors |
    | S7 (NEW) | LLM-as-probabilistic-reasoner (ProbLog) at fuzzy unifications | SPECIFIED, NOT RUN | execute a minimal ProbLog run on one anchor (get_evaluatable().evaluate(), certificate->weight) OR state as future work in contributions |
    | S5 / S6 | Document-level predictive account / predictable propagation | leftover-only | predictive IFF >= N_min held-out units; else descriptive |

  VALIDITY OF THE TWO-LAYER NOVELTY (positioning). To our knowledge this is the first demonstration that, when knockoffs/target-decoy competition are transplanted to LLM scoring, the MARGINAL property the cheminformatics/proteomics decoy-quality diagnostics target (DeepCoy, win-rate/CDF) can be satisfied while the PAIRED sign-flip property the knockoff theorems require is violated -- so a marginal diagnostic over-certifies the gate. All nearest neighbors (conformal factuality/selection/coherent-factuality, multiple-testing hallucination detection, conformal e-value novelty, conformal link prediction) are LABELED, certify a model OUTPUT, and ASSUME exchangeability; ours is label-free, certifies the INTERMEDIATE admission boundary, and empirically TESTS exchangeability -- and finds the marginal-vs-paired gap. This conceptual contribution is asserted as the headline ONLY after P1's powering+de-confounding; otherwise it is reported as a scoped observation in the weak-extractor regime.

  BUDGET (unchanged ceiling, far underspent). ~$2.6 of the $10 cap spent cumulatively. Isolated provenance-blinded scoring with document-prefix prompt caching remains default; cumulative LLM cost logged after every call; HARD STOP at $10. Waterfall ORDER: (P1) powered+de-confounded self-consistency diagonal with the paired statistic across (G,S); (P2) scaled application reduction to CI separation + minimal ProbLog (P4); (P3) demote/validate the regime-diagnostic; then S5/S6/floor-relaxation leftover-only.

  SCOPE OF CLAIMS. The honest central claim is now: a label-free FDR gate at the text-to-logic admission boundary is EXECUTABLE; its certified-FDR validity decomposes into a MARGINAL layer (label-free testable, restored by self-consistency) and a PAIRED layer (required by knockoff+, observed to fail at the cutoff in a weak-extractor error-dense regime), so a marginal diagnostic over-certifies it; whether the paired failure is intrinsic to the LLM boundary or specific to weak extractors / error-dense families is THE open question iteration-4 resolves by de-confounding; the gate's operational value over plain thresholding is NULL where the base scorer is calibrated (well-powered on Re-DocRED) and its application hallucination-reduction is currently a directional trend with auditable provenance pending scaling to CI separation. Facts AND bridges carry the claim.

  MOTIVATION (unchanged core). Text-to-logic pipelines stall where strict symbolic unification fails and an LLM must fuzzy-match predicates and supply background knowledge; that interface is where PLAUSIBLE, high-confidence false facts re-enter and silently corrupt every downstream deduction, and no existing label-free method offers an FDR knob there (self-consistency/LLM-judge are heuristic; ontology filters catch only encoded violations; conformal factuality/selection/multiple-testing all need LABELED calibration and certify the OUTPUT, not the admission boundary). Genomics/proteomics solved the isomorphic label-poor problem with the knockoff filter + target-decoy competition and learned the two failure modes (too-easy decoys -> optimistic FDR, cured by property-matched decoys; entrapment FDP needs a valid independent upper bound). We import matched decoys, the valid combined estimator, and construction-independence to the fuzzy-unification boundary. The iteration-3 evidence refines this into a cautionary, generalizable lesson -- marginal matching is necessary but not sufficient for the paired property the theorems require -- and the deliverable that matters is the regime-aware, application-faithful, auditable hallucination-reduction the goal hard-requires, established at adequate power.

  KEY ASSUMPTIONS (carried, updated by evidence). (1) The null sign-flip property is ENGINEERED AND TESTED, not guaranteed -- and the evidence shows it must be tested at the PAIRED layer, not just the marginal layer; a marginal win-rate ~0.5 does NOT imply paired validity. (2) The disconfirmation must be DE-CONFOUNDED from extractor weakness/error-density before any 'intrinsic limitation' claim is made -- false-positive density and extractor strength are now treated as experimental axes, not fixed at the pathological gpt-4.1-nano multi-hop regime (acc 0.17). (3) Score-dependence handled by document-block bootstrap + isolated provenance-blinded scoring. (4) The diagonal needs genuine false admissions AND adequate power (the ~593-doc run is the binding vehicle). (5) A usable self-detecting diagnostic must probe the PAIRED layer and retain sensitivity in the valid regime -- currently UNMET, pre-registered for repair or honest down-scoping. (6) The application headline must reach CI separation on the pooled reduction to be claimed as significant; otherwise it is a directional trend. (7) The probabilistic reasoner must be EXECUTED (minimal ProbLog) or explicitly declared future work in the contributions.

  INVESTIGATION APPROACH. Strict budget waterfall: Phase-0 (confirm separation + populability + power floor + marginal AND paired diagnostics under self-consistency on the scaled corpus) -> P1 powered+de-confounded self-consistency CLUTRR diagonal varying extractor strength / false-positive density, with the paired statistic across (G,S) -> P2 application hallucination-reduction scaled to CI separation + minimal ProbLog run -> P3 demote/validate the regime-diagnostic -> leftover S5/S6. CPU-only; cost logged after every call; HARD STOP at $10. Pipeline unchanged in structure (over-generating extraction -> property-matched counterfactual decoys with non-entailment verification -> isolated provenance-blinded self-consistency scoring -> knockoff+ gate reporting realized FDR AND decoy_fdr_hat AND marginal+paired diagnostics -> independent entrapment corroboration -> document-block bootstrap CIs -> SWI-Prolog/ProbLog reasoning with auditable per-leaf-certified trace-graphs). FIGURES must carry full captions (1/k floor, bootstrap CIs, gate-vs-plain-vs-swap separation on the diagonal; overlaid decoy/spontaneous/true-positive CDFs with the paired-win asymmetry annotated on the crux; all participating systems with CIs at the matched operating point on the wedge).

  SUCCESS CRITERIA. PRECONDITION (gate): the SCALED self-consistency run must confirm score separation, populability >= N_false_min, a non-empty certified grid below alpha=0.5, AND non-borderline crux p-values BEFORE the diagonal is asserted. PRIMARY DISCONFIRMATION (single): on the populable CLUTRR family under isolated self-consistency at the operative alpha, the central control claim is DISCONFIRMED if realized corpus-aggregate FDR exceeds alpha by more than tau (tau=0.05) AND the document-block-bootstrap CI lies entirely on the anti-conservative side; the gate's self-report is additionally disconfirmed if decoy_fdr_hat is anti-conservative relative to realized. CONFIRMED of the HEADLINE CONCEPTUAL LESSON requires: the paired sign-flip failure PERSISTS across at least two extractor-strength / false-positive-density settings while marginal exchangeability holds (earning 'marginal != paired at the LLM boundary'); if the paired failure VANISHES with a competent extractor, the positive result 'the gate controls realized FDR at alpha when the extractor can score its own errors' is reported and the limitation is scoped to the weak-scorer regime. APPLICATION: the binding deliverable is CONFIRMED only when the pooled hallucinated-fact reduction vs raw LLM reaches document-block-bootstrap CI separation; otherwise reported as a directional trend with auditable provenance. The Re-DocRED operational claim stands as DISCONFIRMED-at-scope (thresholding-is-enough when the base scorer is calibrated), framed precisely (n=152, recall ceiling 0.075). A BH multiplicity correction is applied across all validation tests. DISCONFIRMED if the primary disconfirmation fires under the validated elicitation at adequate power; an uninterpretable null (underpowered tail/diagonal/gap) is the failure the Phase-0 power analysis is designed to prevent.
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
_relation_rationale: >-
  Same gate frame; headline re-pointed to marginal-vs-paired exchangeability with a powering + de-confounding mandate.
_confidence_delta: decreased
_key_changes:
- >-
  REFRAMED THE HEADLINE CONTRIBUTION to MARGINAL != PAIRED exchangeability (new claim S1c): under self-consistency the counterfactual-decoy
  distribution matches the model's spontaneous errors (marginal, KS p=0.058) yet the per-pair sign-flip property fails at
  the cutoff (12/12 admitted multi_hop reals out-score their decoys; realized FDR 1.0 at alpha*=0.5) -- a marginal diagnostic
  over-certifies the gate [art_sBLQqsdm3EIA].
- >-
  ADDED A DE-CONFOUNDING MANDATE (reviewer methodology-MAJOR): the disconfirmation is confounded with a pathological extractor
  (gpt-4.1-nano multi-hop accuracy 0.169, family ~85% false) and only 12 admitted pairs; iteration-4 MUST vary extractor strength
  / false-positive density to test whether the paired failure is intrinsic to the LLM boundary or specific to the weak-scorer/error-dense
  regime, and scope the 'limitation of the entire approach' claim accordingly.
- >-
  MADE POWERING THE BINDING GATE (reviewer evidence-MAJOR): mandated the full ~593-doc self-consistency diagonal (vs the current
  40-doc checkpoint) so the disconfirmation and crux p-values (all within ~0.01 of rejecting) are not borderline; corruption
  result reported with CIs and a single-genre-origin flag; S1b ladder (2 false pairs/rung) powered or restated as purely underpowered.
- >-
  DEMOTED THE REGIME-DIAGNOSTIC (reviewer novelty-MAJOR): acknowledged that signal C (frac(W==Z)=0.939) is mechanically identical
  to signal-A win-rate, so the 'mechanically null' prediction restates the realized null; recast as a heuristic and led with
  the marginal-vs-paired conceptual result, unless validated predictively on >=3 held-out anchors [art_RZC2468yZ-Jh].
- >-
  SET A CI-SEPARATION BAR FOR THE BINDING APPLICATION DELIVERABLE (reviewer scope-MAJOR): the ~25% reduction reaches 0/40
  cells of CI separation at n=24; mandated scaling the anchor (more docs/genre, cleaner crisp gold to shrink the 117/210 undecidable
  fraction) until the pooled reduction is CI-separated, and stating it as directional until then [art_vkfyOl2OQNVx].
- >-
  SPLIT DE-CIRCULARIZATION INTO MARGINAL (settled ROBUST across 4 (G,S) configs) vs PAIRED (NOT YET TESTED across configs);
  mandated computing the paired-exchangeability statistic across (G,S) or softening the de-circularization claim to marginal-only
  (reviewer rigor-MINOR).
- >-
  PROMOTED THE PROBABILISTIC REASONER to an explicit claim S7 (reviewer rigor-MINOR + goal alignment): execute a minimal ProbLog
  run (get_evaluatable().evaluate(), certificate->weight) on one anchor or declare it future work in the CONTRIBUTIONS, since
  the goal hard-requires an LLM-as-probabilistic-reasoner at fuzzy unifications.
- >-
  FIXED THE S1b OVER-STATEMENT (reviewer rigor-MINOR): the artifact ladder shows L0 foreign-swap NOT detected while L1-L4
  ARE -- the opposite of the prior 'detects only gross decoys' narrative; rewritten as underpowered, and figure-caption requirements
  (1/k floor, CIs, gate-vs-plain-vs-swap, paired-win asymmetry) made explicit.
- >-
  CONFIDENCE DECREASED: the headline disconfirmation is both confounded (weak extractor) and underpowered (12 pairs, borderline
  p-values), the only well-powered result is the Re-DocRED operational null, and the binding application reduction is directional-only
  -- the core idea and a sharper conceptual lesson survive, but every affirmative claim now needs power and de-confounding
  it currently lacks.
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 17 research artifacts across all iterations.

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

--- Item 13 ---
id: art_XsxfC0rkmmD1
type: experiment
title: >-
  Powered & De-Confounded Self-Consistency CLUTRR knockoff+ FDR Calibration Diagonal
summary: >-
  Iter-4 P1 executes the FULL ~593-doc (535 confirmatory + 58 pilot, k>=6 oversampled) self-consistency CLUTRR realized-FDR-vs-target-alpha
  CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into
  a symbolic layer, powering the diagonal that iter-3 designed but only ran on a 40-doc checkpoint. METHOD (counterfactual-decoy
  knockoff+ gate, K=5 self-consistency elicitation, openai/gpt-4.1-nano) is compared side-by-side in ONE pipeline against
  BASELINE-1 (PLAIN raw-confidence threshold gate, the purely-neural foil), BASELINE-2 (random in-doc SWAP-decoy knockoff
  control), a VERBALIZED-confidence contrast on the same data, and a deterministic foreign-entity ENTRAPMENT corroboration
  (Wen et al. 2025, r=1). Code/caches are warm-started from iter-3 P1 and iter-2 EXP2 so only NEW docs cost money (full run
  far under the $10 cap; soft cap $4 governs optional arms). PROVIDES, for atomic / multi_hop / pooled families: the (target
  alpha, decoy_fdr_hat, realized FDR) TRIPLE across the certified alpha grid {0.05,0.1,0.2,0.3,0.5} (k-floors {20,10,5,4,2})
  with B=2000 document-block bootstrap CIs, a binding POWER GATE (alpha certified only if n_admitted>=k_floor AND family has
  >=40 genuine false reals), and a pre-registered SELF-REPORT disconfirmation (decoy_fdr_hat flagged where anti-conservative
  vs realized beyond tau=0.05). THREE NEW analyses extend iter-3: (1) the per-pair PAIRED-exchangeability statistic (the sign-flip
  win-rate the knockoff+ theorem actually requires) reported DISTINCTLY from the marginal CDF/KS crux AND across the four
  (Generator, Scorer) configs {nano,ministral-8b}x{nano,ministral-8b} (the cfo=ministral-generated decoys and ministral-8b
  SC scores are warm on the 40 original-pilot docs), so paired-layer de-circularization is evidenced not asserted (the central
  reconciliation: the marginal can hold while the paired layer's behaviour drives the realized FDR); (2) a DE-CONFOUND of
  extractor-weakness/error-density via a zero-API false-positive-density stratification (multi_hop FALSE pairs binned by chain
  length k into LOW/MED/HIGH) plus an optional budget-gated STRONGER-EXTRACTOR arm (openai/gpt-4.1-mini, scorer fixed at nano-SC)
  that tests whether the per-pair failure PERSISTS or VANISHES with a competent extractor (the full extractor-strength x density
  matrix is delegated to the sibling iter-4 artifact dir2); (3) a POWER-or-BOUND S1b ladder (L0 foreign-swap -> L1 in-doc
  swap -> L2 random-vocab -> L3 cf_2nd -> L4 primary-cf) scored under the same K=5 self-consistency, with each rung's realized
  false-pair n and a per-rung power flag, under-floor rungs reported purely as underpowered (the contradicted 'detects only
  gross decoys' narrative deleted). The primary disconfirmation is pre-registered on the populable multi_hop family at the
  tightest certified alpha; the 40-doc warm-cache reproduction matched iter-3 exactly (realized FDR 1.0 at alpha*=0.5, CI
  [0.66,1.0], n_adm=12; marginal crux KS p~0.058). Outputs: method.py (full method+baselines+controls+selftest), schema-valid
  method_out.json (exp_gen_sol_out) with rich metadata (all diagonals, power/populability table, triple-per-cell, self-report
  flags, marginal crux with overlaid CDFs, paired_vs_marginal block, paired_across_GS, density_strata, strong_extractor_arm,
  S1b ladder verdict, entrapment, BH q=0.05 multiplicity table, primary-disconfirmation verdict, runtime+cost) plus per-real
  examples carrying SC/VB Z-scores, W-statistics and per-alpha admission predictions; five figures with self-contained captions
  (diagonal, crux CDFs, S1b ladder, paired-across-(G,S), density de-confound). Downstream GEN_PAPER_TEXT can cite the powered
  diagonal, the distinct marginal-vs-paired result, the (G,S) de-circularization, the density/extractor de-confound, and the
  BH-corrected validation tests.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 14 ---
id: art_SxBOgRTuPGdR
type: experiment
title: Extractor-strength x density persistence matrix for a CLUTRR knockoff+ FDR gate
summary: |-
  P1-DECONFOUND executes a controlled 2-axis (extractor-strength x false-positive-density) persistence matrix on the CLUTRR crisp-gold corpus to de-confound the iteration-3 disconfirmation of the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into a symbolic layer. method.py reuses iter-3 primitives verbatim (fdr_stats/fdr_core/llm_client; knockoff+ threshold Barber-Candes eq.1.9, signed-max W, document-block bootstrap B>=2000, BH) and adds: subsample_to_density (free Axis-B reuse of cached scores), compute_diagonal (realized-FDR-vs-alpha + decoy_fdr_hat + plain raw-confidence BASELINE per row + paired win-rate over FALSE pairs), compute_marginal (decoy~spont, decoy!=true-pos, with effect-size direction), per-cell metrics with a 10-seed robustness spread, and an explicit EARNED/SCOPED decision rule. The extractor is also the scorer and decoy-generator (self-detecting gate).

  VERDICT = EARNED (robust under both {reals u cf u swap} primary and {reals u cf} robustness normalizations; $2.94 total spend, hard cap $10). Phase-0 selected gpt-4.1-mini as the COMPETENT extractor (multi-hop relation accuracy 0.453 >= 0.45 bar, vs weak gpt-4.1-nano 0.205; gpt-4o-mini 0.402 missed). At 200 matched docs (K=5 self-consistency): the competent mini's multi_hop paired win-rate CI lies entirely below 0.5 at ALL three densities (0.27/0.37/0.35 -> false reals beat their OWN counterfactual decoys), and the gate is GOLD-based anti-conservative at density 0.85 (realized FDR 0.818, doc-block CI [0.758,0.860], 306/374 false admitted). The density-0.20 cell is decoy-controlled (marginal VALID, gap -0.018, yet paired-fails 0.268). The weak nano gate, at scale, admits nothing (realized=None) -> iter-3's realized=1.0 was a 12-admission small-sample tail artifact; the sanity anchor reproduces iter-3 byte-for-byte at the matched 40-doc scale (realized 1.0, 12 admits, W differs 0/186). Mechanism: the marginal 'cf decoys too easy' (gap<0) and paired win-rate<0.5 are two views of the SAME self-favoring bias -- the LLM scores its own (possibly-wrong) extraction above a counterfactual decoy; this also appears on the easier atomic family. So the failure is a property of the LLM self-consistency SCORING boundary, NOT a weak-extractor artifact (paper headline, S1c earned). BH: 24/48 cell tests reject at q=0.05.

  OUTPUTS (schema exp_gen_sol_out, validated): method_out.json (4.1MB, <100MB so no split) with metadata.phase0_extractor_probe, persistence_matrix (2x3x2), cells_full (per-cell diagonal triple+CIs, paired, marginal, seed_spread), earned_vs_scoped_verdict (verdict + verbatim decision_rule + supporting_cells), robustness_alt_normalization, sanity_anchor_iter3_reproduction, extraction_quality, bh_correction, full_figure_captions, grand_total_llm_spend; plus 4167 examples (2055 nano + 2112 mini, one per scored real with z_real/z_decoy/W, density membership, per-alpha admit predictions). Figures F1 persistence heatmap, F2 nano-vs-strong diagonals, F3 paired win-rate (blue=nano,red=mini), F4 marginal crux CDFs. Checkpoints (pipe_nano/pipe_strong/phase0) enable free --analyze-only re-runs. Key reuse caveat for downstream: iter-3 cf-decoy generation builds a discarded second decoy whose fallback advances the per-doc RNG; replicate it to keep cache/normalization parity.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 15 ---
id: art_fo9-7UYPvELK
type: dataset
title: 84-Doc Legal/News/Regulatory Application Anchor with Crisp + Silver Triple Gold
summary: |-
  iter_4 'application anchor': 84 short, professionally-written documents (legal 30 / news 28 / regulatory 26) standardized to the exp_sel_data_out schema for the text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment. datasets[] is GROUPED BY SOURCE CORPUS -- CUAD (30 legal, CRISP), Wikinews (28 news, silver), GDPR (15 regulatory-EU, silver), eCFR (11 regulatory-US, silver) -- and each DOCUMENT is ONE example (84 total). Per example: input is a JSON STRING {doc_id, document_text, genre, source, char_length, entities:[{name,type in {PER,LOC,ORG,TIME,NUM,MISC},char_span:[s,e]}]}; output is a JSON STRING {gold_atomic_facts:[{head,relation,tail,provenance_char_span:[s,e]}]}; flat metadata_* keys carry metadata_fold(=genre), metadata_genre, metadata_gold_quality(crisp|silver), metadata_crisp_subset(bool, NEW), metadata_decidable_fraction(float [0,1], NEW) + metadata_decidable_subscores{sentence_coverage,entity_participation,char_coverage}, metadata_source, metadata_license, metadata_relation_vocab, metadata_char_length, metadata_num_facts, metadata_num_entities, metadata_doc_id, metadata_excerpt(legal whole-vs-excerpt-window), metadata_entity_types_fine.

  NO LLM is used anywhere in gold construction (non-circularity). Legal gold is CRISP (CUAD human clause spans); to scale the crisp pool beyond the ~21 naturally short whole contracts, deterministic EXCERPT WINDOWS over CUAD's 510 long contracts pick the densest cluster of >=3 fully-contained human clause spans, snap to clean sentence/paragraph boundaries (no mid-sentence cut), re-base each clause offset into the excerpt (s'=s-w_start) and re-verify (21 whole + 9 excerpt). Regulatory + news gold are SILVER (deterministic spaCy/regex curation, no LLM) with DEEPENED recall: GDPR/eCFR add prohibits/applies_to/defined_as/per-paragraph facts across 38 GDPR articles + 6 eCFR parts round-robined (Reg E, Reg P, COPPA, FTC Safeguards, Reg S-P, HIPAA); news adds quote attribution (say/announce), dependency-gated located_in, and met_with on top of NE-NE SVO + occurred_on + affiliated_with.

  Verification (build/verify_dataset.py, independent re-parse of every string): 0 errors, 2774/2774 entity char_spans verify (document_text[s:e]==name), 547 facts, value-fact tails 100% substrings of their provenance span (the only 8 non-substring tails are legitimate clause-presence LABEL facts whose provenance is the human clause span), >=3 facts/doc (mean 6.51). crisp_subset=30. decidable_fraction composite min 0.114 / mean 0.304 / median 0.248 / max 0.769 (regulatory 0.466 > news 0.240 > legal 0.223). Validates against exp_sel_data_out (full + mini). full_data_out.json is 687KB (well under 100MB; no split needed). Byte-identical deterministic regeneration via regenerate.sh or `uv run --no-sync data.py` (PYTHONHASHSEED=42, SEED=42; pinned spaCy 3.7.5 + en_core_web_sm 3.7.1 + numpy 1.26.4 + nltk 3.9.1 + bs4 4.12.3 / lxml 5.3.0).

  All sources are FREE for commercial+research reuse: CUAD CC BY 4.0, Wikinews CC BY 2.5, GDPR EUR-Lex free reuse (CELEX:32016R0679), eCFR US public domain (17 USC 105). NonCommercial / format-incompatible candidates (MAUD CC-BY-NC-SA source texts, LEDGAR classification-only, ContractNLI CC-BY-NC-SA, REDFM CC-BY-SA-NC, WebRED sentence-level) were evaluated and excluded (documented in dataset_meta.json + temp/datasets/CANDIDATE_EVALUATION.md); no free-license span-annotated 5th legal corpus exists. Downstream use: build a crisp-only fold via metadata_crisp_subset ALONGSIDE the genre folds (metadata_fold), and rank/select the most-decidable documents via metadata_decidable_fraction to shrink the gold-undecidable fraction toward CI-separated pooled hallucination-reduction. Files: data.py (canonical builder), full_data_out.json (84 examples), mini_data_out.json (12), preview_data_out.json (truncated), dataset_meta.json, schema/, build/ scripts (common.py + fetch_sources.py + build_{legal,news,regulatory}.py + verify_dataset.py), cached raw/ snapshot, regenerate.sh, README.md, pyproject.toml (61 pinned deps).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 16 ---
id: art_Sd8BgJ00OeGZ
type: experiment
title: ProbLog probabilistic reasoner + honest finalized reporting on the 24-doc anchor
summary: |-
  Executes gen_plan_experiment_3_idx4 as a $0 cache-hit REANALYSIS of the iter-3 P2 pipeline on the SAME 24-doc legal/news/regulatory application anchor, adding two deliverables on top of the inherited method+baselines (which stay byte-for-byte identical: hallucination_grid, multihop point estimates, trace_graphs and extraction_quality were verified UNCHANGED, and the new metadata keys are a strict superset of the prior run's).

  (P4) LLM-as-PROBABILISTIC-REASONER (new module prob_reasoner.py). Each document's admitted-fact KB + hand-authored genre bridge rules is compiled to a WEIGHTED ProbLog program and multi-hop conclusion MARGINALS are computed via get_evaluatable().create_from(PrologString).evaluate() (engine='problog'; ProbLog 2.2.10 installed and working). A pure-Python EXACT weighted-model-counting fallback is included and VALIDATED equal to ProbLog to 1e-9, including the shared-leaf case where naive noisy-OR fails (toy 2-hop=0.63; shared-leaf conclusions 0.48/0.40 match exactly). Certificate->weight map: DEFAULT gate-consistent shrinkage w_i=(1-alpha_hat)*calibrate(Z_i) with alpha_hat=decoy_fdr_hat of the operative (genre,portable,alpha=0.5) cell and calibrate=identity-clamp; per-pair margin 0.5+0.5*W_i and identity/no-shrinkage reported as a 12-row sensitivity table (shrinkage<=identity confirmed everywhere). Probabilistic trace-graphs (prob_trace_graphs/, JSON+DOT) annotate every node with its marginal/weight and retain each leaf's provenance + decoy (W_i,T,alpha) + entrapment (FDP_hat,r) certificate; genuine multi-hop marginals are shown on regulatory bridges, single-fact probabilistic admissions on legal/news. Deterministic backward-chaining REMAINS the baseline; NO headline number depends on ProbLog.

  (P2) HONEST FINALIZED REPORTING (metadata, no new LLM calls). atomic_reduction_pooled: pooled atomic hallucinated-fact reduction per (elicitation,alpha) with document-block bootstrap CIs on the raw-gate DIFFERENCE; raw~0.245 -> gate~0.18 (~26% relative) but stated PLAINLY as DIRECTIONAL, not significant (0/40 grid + 0/10 pooled CI-separated cells at n=24). multihop_corruption (+ci): RAW-KB->GATE-KB(alpha=0.5) corruption 0.52->0.25 with bootstrap CIs, single_genre_origin='regulatory', per-system counts (21->8 conclusions), and an explicit WIDE-CI single-genre caveat (legal corrupt=0, news derives 0). self_report_regime='conservative': decoy_fdr_hat>=realized in ALL 40 cells (anti_conservative_cells=0), the OPPOSITE of the CLUTRR multi-hop anti-conservative regime (0.5<1.0).

  Figures: figure-ready arrays + full captions under metadata.figures, rendered to PNG by build_figures.py via networkx+matplotlib (NO system dot binary): F1 pooled atomic CI bars (both elicitations), F2 multi-hop corruption + per-genre counts, F3 decoy_fdr_hat-vs-realized scatter with the CLUTRR contrast, F4 a regulatory probabilistic trace-graph (showcase: a corrupted conclusion marginal=0.05 whose hallucinated leaf, W=-0.33<T, is correctly down-weighted).

  Outputs: method_out.json (+full/mini/preview, all schema-valid against exp_gen_sol_out; one row per extracted real fact, all rich analysis under permissive metadata), 4 figure PNGs, 4 probabilistic trace-graphs (legal/news/2x regulatory), 7 deterministic trace-graphs. CPU-only; total live LLM spend ~$0.06 (final full run $0.00, fully cached and deterministic at reals=208); soft cap $1, hard stop $10 honoured.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 17 ---
id: art_iCOHKeSAQZhn
type: evaluation
title: >-
  Demoting the gold-free regime-diagnostic to a heuristic: A=C identity + mispredict audit
summary: >-
  Zero-API, pure-CPU, $0.00 evaluation (eval.py) that quantitatively DEMOTES the iter-3 gold-free regime-diagnostic (art_RZC2468yZ-Jh)
  from a novel contribution to a deployment-time HEURISTIC, resolving reviewer novelty-MAJOR / claim S4c. It performs NO new
  measurements: every number is an algebraic identity or a recomputation over cached arrays (Re-DocRED confirmatory checkpoints'
  raw Z/Zt/W, 4384 candidates over 152 docs; CLUTRR self-consistency scalars from art_sBLQqsdm3EIA). KEY RESULTS, all reproducing
  the cached summary to 5 dp: (1) A=C IDENTITY CONFIRMED — since W=sign(Z-Zt)*max(Z,Zt), 1[W==Z]=1[Z>Zt], so frac(W==Z)=1-winrate
  exactly up to the measure-zero Z=Zt=0 edge; per-set identity_residual EQUALS the Z=Zt=0 fraction to ~1e-16 in every set
  {all, top_25pct, top_50pct, knockoff_alpha0.2-admitted}, corr(a,c)=-0.988, and the admitted-set Spearman is 0.990959 WITH
  the W=0 ties and 1.0 WITHOUT them (mechanically forced; jaccard 0.916087). Case table verified exactly: 4111 rows Z>Zt->W=Z,
  251 Z<Zt->W=-Zt, 22 Z==Zt->W=0. So signal C carries ZERO new information beyond signal A. (2) SIGNAL DEPENDENCE — of the
  nominal 4 signals, A and C are identical and B is a distributional refinement of the same decoy-exchangeability axis; only
  D adds a genuinely new array (self-consistency f); effective_independent_axes=2. (3) MISPREDICT AUDIT — the map's one validated
  anchor (Re-DocRED null) is near-mechanical (rerank_blocked via frac(W==Z)=0.94 restates the realized null); it MISPREDICTS
  CLUTRR self-consistency (marginal win-rate 0.482 => predicted 'gate adds value'/positive, yet the powered paired diagonal
  is DISCONFIRMED, realized FDR 1.0, CI [0.66,1.0]); independent_and_correct_count=0. (4) HONEST PANEL — figure_panel arrays
  (x=[0.04471,0.482,0.103,0.34], y=[0.60293,null,null,null]) + paper-ready caption + figures/regime_panel.jpg, plus a reframing_recommendation
  to LEAD with the marginal-vs-paired conceptual result and present the diagnostic as a heuristic with stated A=C redundancy.
  Contamination caveat: excluding 515 contaminated decoys LOWERS the win-rate (0.0623->0.0277), strengthening the demotion.
  Output eval_out.json validates against schema exp_eval_sol_out (rich blocks nested under metadata; metrics_agg has 31 numeric
  scalars; datasets carry the per-set identity table and the 4-point regime panel with predict_/eval_/metadata_ fields). Deterministic
  (seed=0; only winrate CIs use the B=2000 doc-block bootstrap). Companion: README.md, pinned pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 5 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

title: >-
  Powered & De-Confounded Self-Consistency CLUTRR knockoff+ FDR Calibration Diagonal
type: experiment
summary: >-
  Iter-4 P1 executes the FULL ~593-doc (535 confirmatory + 58 pilot, k>=6 oversampled) self-consistency CLUTRR realized-FDR-vs-target-alpha
  CALIBRATION DIAGONAL for the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into
  a symbolic layer, powering the diagonal that iter-3 designed but only ran on a 40-doc checkpoint. METHOD (counterfactual-decoy
  knockoff+ gate, K=5 self-consistency elicitation, openai/gpt-4.1-nano) is compared side-by-side in ONE pipeline against
  BASELINE-1 (PLAIN raw-confidence threshold gate, the purely-neural foil), BASELINE-2 (random in-doc SWAP-decoy knockoff
  control), a VERBALIZED-confidence contrast on the same data, and a deterministic foreign-entity ENTRAPMENT corroboration
  (Wen et al. 2025, r=1). Code/caches are warm-started from iter-3 P1 and iter-2 EXP2 so only NEW docs cost money (full run
  far under the $10 cap; soft cap $4 governs optional arms). PROVIDES, for atomic / multi_hop / pooled families: the (target
  alpha, decoy_fdr_hat, realized FDR) TRIPLE across the certified alpha grid {0.05,0.1,0.2,0.3,0.5} (k-floors {20,10,5,4,2})
  with B=2000 document-block bootstrap CIs, a binding POWER GATE (alpha certified only if n_admitted>=k_floor AND family has
  >=40 genuine false reals), and a pre-registered SELF-REPORT disconfirmation (decoy_fdr_hat flagged where anti-conservative
  vs realized beyond tau=0.05). THREE NEW analyses extend iter-3: (1) the per-pair PAIRED-exchangeability statistic (the sign-flip
  win-rate the knockoff+ theorem actually requires) reported DISTINCTLY from the marginal CDF/KS crux AND across the four
  (Generator, Scorer) configs {nano,ministral-8b}x{nano,ministral-8b} (the cfo=ministral-generated decoys and ministral-8b
  SC scores are warm on the 40 original-pilot docs), so paired-layer de-circularization is evidenced not asserted (the central
  reconciliation: the marginal can hold while the paired layer's behaviour drives the realized FDR); (2) a DE-CONFOUND of
  extractor-weakness/error-density via a zero-API false-positive-density stratification (multi_hop FALSE pairs binned by chain
  length k into LOW/MED/HIGH) plus an optional budget-gated STRONGER-EXTRACTOR arm (openai/gpt-4.1-mini, scorer fixed at nano-SC)
  that tests whether the per-pair failure PERSISTS or VANISHES with a competent extractor (the full extractor-strength x density
  matrix is delegated to the sibling iter-4 artifact dir2); (3) a POWER-or-BOUND S1b ladder (L0 foreign-swap -> L1 in-doc
  swap -> L2 random-vocab -> L3 cf_2nd -> L4 primary-cf) scored under the same K=5 self-consistency, with each rung's realized
  false-pair n and a per-rung power flag, under-floor rungs reported purely as underpowered (the contradicted 'detects only
  gross decoys' narrative deleted). The primary disconfirmation is pre-registered on the populable multi_hop family at the
  tightest certified alpha; the 40-doc warm-cache reproduction matched iter-3 exactly (realized FDR 1.0 at alpha*=0.5, CI
  [0.66,1.0], n_adm=12; marginal crux KS p~0.058). Outputs: method.py (full method+baselines+controls+selftest), schema-valid
  method_out.json (exp_gen_sol_out) with rich metadata (all diagonals, power/populability table, triple-per-cell, self-report
  flags, marginal crux with overlaid CDFs, paired_vs_marginal block, paired_across_GS, density_strata, strong_extractor_arm,
  S1b ladder verdict, entrapment, BH q=0.05 multiplicity table, primary-disconfirmation verdict, runtime+cost) plus per-real
  examples carrying SC/VB Z-scores, W-statistics and per-alpha admission predictions; five figures with self-contained captions
  (diagonal, crux CDFs, S1b ladder, paired-across-(G,S), density de-confound). Downstream GEN_PAPER_TEXT can cite the powered
  diagonal, the distinct marginal-vs-paired result, the (G,S) de-circularization, the density/extractor de-confound, and the
  BH-corrected validation tests.
id: art_XsxfC0rkmmD1

title: Extractor-strength x density persistence matrix for a CLUTRR knockoff+ FDR gate
type: experiment
summary: |-
  P1-DECONFOUND executes a controlled 2-axis (extractor-strength x false-positive-density) persistence matrix on the CLUTRR crisp-gold corpus to de-confound the iteration-3 disconfirmation of the label-free decoy-competition (knockoff+) FDR gate that admits LLM-extracted kinship facts into a symbolic layer. method.py reuses iter-3 primitives verbatim (fdr_stats/fdr_core/llm_client; knockoff+ threshold Barber-Candes eq.1.9, signed-max W, document-block bootstrap B>=2000, BH) and adds: subsample_to_density (free Axis-B reuse of cached scores), compute_diagonal (realized-FDR-vs-alpha + decoy_fdr_hat + plain raw-confidence BASELINE per row + paired win-rate over FALSE pairs), compute_marginal (decoy~spont, decoy!=true-pos, with effect-size direction), per-cell metrics with a 10-seed robustness spread, and an explicit EARNED/SCOPED decision rule. The extractor is also the scorer and decoy-generator (self-detecting gate).

  VERDICT = EARNED (robust under both {reals u cf u swap} primary and {reals u cf} robustness normalizations; $2.94 total spend, hard cap $10). Phase-0 selected gpt-4.1-mini as the COMPETENT extractor (multi-hop relation accuracy 0.453 >= 0.45 bar, vs weak gpt-4.1-nano 0.205; gpt-4o-mini 0.402 missed). At 200 matched docs (K=5 self-consistency): the competent mini's multi_hop paired win-rate CI lies entirely below 0.5 at ALL three densities (0.27/0.37/0.35 -> false reals beat their OWN counterfactual decoys), and the gate is GOLD-based anti-conservative at density 0.85 (realized FDR 0.818, doc-block CI [0.758,0.860], 306/374 false admitted). The density-0.20 cell is decoy-controlled (marginal VALID, gap -0.018, yet paired-fails 0.268). The weak nano gate, at scale, admits nothing (realized=None) -> iter-3's realized=1.0 was a 12-admission small-sample tail artifact; the sanity anchor reproduces iter-3 byte-for-byte at the matched 40-doc scale (realized 1.0, 12 admits, W differs 0/186). Mechanism: the marginal 'cf decoys too easy' (gap<0) and paired win-rate<0.5 are two views of the SAME self-favoring bias -- the LLM scores its own (possibly-wrong) extraction above a counterfactual decoy; this also appears on the easier atomic family. So the failure is a property of the LLM self-consistency SCORING boundary, NOT a weak-extractor artifact (paper headline, S1c earned). BH: 24/48 cell tests reject at q=0.05.

  OUTPUTS (schema exp_gen_sol_out, validated): method_out.json (4.1MB, <100MB so no split) with metadata.phase0_extractor_probe, persistence_matrix (2x3x2), cells_full (per-cell diagonal triple+CIs, paired, marginal, seed_spread), earned_vs_scoped_verdict (verdict + verbatim decision_rule + supporting_cells), robustness_alt_normalization, sanity_anchor_iter3_reproduction, extraction_quality, bh_correction, full_figure_captions, grand_total_llm_spend; plus 4167 examples (2055 nano + 2112 mini, one per scored real with z_real/z_decoy/W, density membership, per-alpha admit predictions). Figures F1 persistence heatmap, F2 nano-vs-strong diagonals, F3 paired win-rate (blue=nano,red=mini), F4 marginal crux CDFs. Checkpoints (pipe_nano/pipe_strong/phase0) enable free --analyze-only re-runs. Key reuse caveat for downstream: iter-3 cf-decoy generation builds a discarded second decoy whose fallback advances the per-doc RNG; replicate it to keep cache/normalization parity.
id: art_SxBOgRTuPGdR

title: 84-Doc Legal/News/Regulatory Application Anchor with Crisp + Silver Triple Gold
type: dataset
summary: |-
  iter_4 'application anchor': 84 short, professionally-written documents (legal 30 / news 28 / regulatory 26) standardized to the exp_sel_data_out schema for the text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment. datasets[] is GROUPED BY SOURCE CORPUS -- CUAD (30 legal, CRISP), Wikinews (28 news, silver), GDPR (15 regulatory-EU, silver), eCFR (11 regulatory-US, silver) -- and each DOCUMENT is ONE example (84 total). Per example: input is a JSON STRING {doc_id, document_text, genre, source, char_length, entities:[{name,type in {PER,LOC,ORG,TIME,NUM,MISC},char_span:[s,e]}]}; output is a JSON STRING {gold_atomic_facts:[{head,relation,tail,provenance_char_span:[s,e]}]}; flat metadata_* keys carry metadata_fold(=genre), metadata_genre, metadata_gold_quality(crisp|silver), metadata_crisp_subset(bool, NEW), metadata_decidable_fraction(float [0,1], NEW) + metadata_decidable_subscores{sentence_coverage,entity_participation,char_coverage}, metadata_source, metadata_license, metadata_relation_vocab, metadata_char_length, metadata_num_facts, metadata_num_entities, metadata_doc_id, metadata_excerpt(legal whole-vs-excerpt-window), metadata_entity_types_fine.

  NO LLM is used anywhere in gold construction (non-circularity). Legal gold is CRISP (CUAD human clause spans); to scale the crisp pool beyond the ~21 naturally short whole contracts, deterministic EXCERPT WINDOWS over CUAD's 510 long contracts pick the densest cluster of >=3 fully-contained human clause spans, snap to clean sentence/paragraph boundaries (no mid-sentence cut), re-base each clause offset into the excerpt (s'=s-w_start) and re-verify (21 whole + 9 excerpt). Regulatory + news gold are SILVER (deterministic spaCy/regex curation, no LLM) with DEEPENED recall: GDPR/eCFR add prohibits/applies_to/defined_as/per-paragraph facts across 38 GDPR articles + 6 eCFR parts round-robined (Reg E, Reg P, COPPA, FTC Safeguards, Reg S-P, HIPAA); news adds quote attribution (say/announce), dependency-gated located_in, and met_with on top of NE-NE SVO + occurred_on + affiliated_with.

  Verification (build/verify_dataset.py, independent re-parse of every string): 0 errors, 2774/2774 entity char_spans verify (document_text[s:e]==name), 547 facts, value-fact tails 100% substrings of their provenance span (the only 8 non-substring tails are legitimate clause-presence LABEL facts whose provenance is the human clause span), >=3 facts/doc (mean 6.51). crisp_subset=30. decidable_fraction composite min 0.114 / mean 0.304 / median 0.248 / max 0.769 (regulatory 0.466 > news 0.240 > legal 0.223). Validates against exp_sel_data_out (full + mini). full_data_out.json is 687KB (well under 100MB; no split needed). Byte-identical deterministic regeneration via regenerate.sh or `uv run --no-sync data.py` (PYTHONHASHSEED=42, SEED=42; pinned spaCy 3.7.5 + en_core_web_sm 3.7.1 + numpy 1.26.4 + nltk 3.9.1 + bs4 4.12.3 / lxml 5.3.0).

  All sources are FREE for commercial+research reuse: CUAD CC BY 4.0, Wikinews CC BY 2.5, GDPR EUR-Lex free reuse (CELEX:32016R0679), eCFR US public domain (17 USC 105). NonCommercial / format-incompatible candidates (MAUD CC-BY-NC-SA source texts, LEDGAR classification-only, ContractNLI CC-BY-NC-SA, REDFM CC-BY-SA-NC, WebRED sentence-level) were evaluated and excluded (documented in dataset_meta.json + temp/datasets/CANDIDATE_EVALUATION.md); no free-license span-annotated 5th legal corpus exists. Downstream use: build a crisp-only fold via metadata_crisp_subset ALONGSIDE the genre folds (metadata_fold), and rank/select the most-decidable documents via metadata_decidable_fraction to shrink the gold-undecidable fraction toward CI-separated pooled hallucination-reduction. Files: data.py (canonical builder), full_data_out.json (84 examples), mini_data_out.json (12), preview_data_out.json (truncated), dataset_meta.json, schema/, build/ scripts (common.py + fetch_sources.py + build_{legal,news,regulatory}.py + verify_dataset.py), cached raw/ snapshot, regenerate.sh, README.md, pyproject.toml (61 pinned deps).
id: art_fo9-7UYPvELK

title: ProbLog probabilistic reasoner + honest finalized reporting on the 24-doc anchor
type: experiment
summary: |-
  Executes gen_plan_experiment_3_idx4 as a $0 cache-hit REANALYSIS of the iter-3 P2 pipeline on the SAME 24-doc legal/news/regulatory application anchor, adding two deliverables on top of the inherited method+baselines (which stay byte-for-byte identical: hallucination_grid, multihop point estimates, trace_graphs and extraction_quality were verified UNCHANGED, and the new metadata keys are a strict superset of the prior run's).

  (P4) LLM-as-PROBABILISTIC-REASONER (new module prob_reasoner.py). Each document's admitted-fact KB + hand-authored genre bridge rules is compiled to a WEIGHTED ProbLog program and multi-hop conclusion MARGINALS are computed via get_evaluatable().create_from(PrologString).evaluate() (engine='problog'; ProbLog 2.2.10 installed and working). A pure-Python EXACT weighted-model-counting fallback is included and VALIDATED equal to ProbLog to 1e-9, including the shared-leaf case where naive noisy-OR fails (toy 2-hop=0.63; shared-leaf conclusions 0.48/0.40 match exactly). Certificate->weight map: DEFAULT gate-consistent shrinkage w_i=(1-alpha_hat)*calibrate(Z_i) with alpha_hat=decoy_fdr_hat of the operative (genre,portable,alpha=0.5) cell and calibrate=identity-clamp; per-pair margin 0.5+0.5*W_i and identity/no-shrinkage reported as a 12-row sensitivity table (shrinkage<=identity confirmed everywhere). Probabilistic trace-graphs (prob_trace_graphs/, JSON+DOT) annotate every node with its marginal/weight and retain each leaf's provenance + decoy (W_i,T,alpha) + entrapment (FDP_hat,r) certificate; genuine multi-hop marginals are shown on regulatory bridges, single-fact probabilistic admissions on legal/news. Deterministic backward-chaining REMAINS the baseline; NO headline number depends on ProbLog.

  (P2) HONEST FINALIZED REPORTING (metadata, no new LLM calls). atomic_reduction_pooled: pooled atomic hallucinated-fact reduction per (elicitation,alpha) with document-block bootstrap CIs on the raw-gate DIFFERENCE; raw~0.245 -> gate~0.18 (~26% relative) but stated PLAINLY as DIRECTIONAL, not significant (0/40 grid + 0/10 pooled CI-separated cells at n=24). multihop_corruption (+ci): RAW-KB->GATE-KB(alpha=0.5) corruption 0.52->0.25 with bootstrap CIs, single_genre_origin='regulatory', per-system counts (21->8 conclusions), and an explicit WIDE-CI single-genre caveat (legal corrupt=0, news derives 0). self_report_regime='conservative': decoy_fdr_hat>=realized in ALL 40 cells (anti_conservative_cells=0), the OPPOSITE of the CLUTRR multi-hop anti-conservative regime (0.5<1.0).

  Figures: figure-ready arrays + full captions under metadata.figures, rendered to PNG by build_figures.py via networkx+matplotlib (NO system dot binary): F1 pooled atomic CI bars (both elicitations), F2 multi-hop corruption + per-genre counts, F3 decoy_fdr_hat-vs-realized scatter with the CLUTRR contrast, F4 a regulatory probabilistic trace-graph (showcase: a corrupted conclusion marginal=0.05 whose hallucinated leaf, W=-0.33<T, is correctly down-weighted).

  Outputs: method_out.json (+full/mini/preview, all schema-valid against exp_gen_sol_out; one row per extracted real fact, all rich analysis under permissive metadata), 4 figure PNGs, 4 probabilistic trace-graphs (legal/news/2x regulatory), 7 deterministic trace-graphs. CPU-only; total live LLM spend ~$0.06 (final full run $0.00, fully cached and deterministic at reals=208); soft cap $1, hard stop $10 honoured.
id: art_Sd8BgJ00OeGZ

title: >-
  Demoting the gold-free regime-diagnostic to a heuristic: A=C identity + mispredict audit
type: evaluation
summary: >-
  Zero-API, pure-CPU, $0.00 evaluation (eval.py) that quantitatively DEMOTES the iter-3 gold-free regime-diagnostic (art_RZC2468yZ-Jh)
  from a novel contribution to a deployment-time HEURISTIC, resolving reviewer novelty-MAJOR / claim S4c. It performs NO new
  measurements: every number is an algebraic identity or a recomputation over cached arrays (Re-DocRED confirmatory checkpoints'
  raw Z/Zt/W, 4384 candidates over 152 docs; CLUTRR self-consistency scalars from art_sBLQqsdm3EIA). KEY RESULTS, all reproducing
  the cached summary to 5 dp: (1) A=C IDENTITY CONFIRMED — since W=sign(Z-Zt)*max(Z,Zt), 1[W==Z]=1[Z>Zt], so frac(W==Z)=1-winrate
  exactly up to the measure-zero Z=Zt=0 edge; per-set identity_residual EQUALS the Z=Zt=0 fraction to ~1e-16 in every set
  {all, top_25pct, top_50pct, knockoff_alpha0.2-admitted}, corr(a,c)=-0.988, and the admitted-set Spearman is 0.990959 WITH
  the W=0 ties and 1.0 WITHOUT them (mechanically forced; jaccard 0.916087). Case table verified exactly: 4111 rows Z>Zt->W=Z,
  251 Z<Zt->W=-Zt, 22 Z==Zt->W=0. So signal C carries ZERO new information beyond signal A. (2) SIGNAL DEPENDENCE — of the
  nominal 4 signals, A and C are identical and B is a distributional refinement of the same decoy-exchangeability axis; only
  D adds a genuinely new array (self-consistency f); effective_independent_axes=2. (3) MISPREDICT AUDIT — the map's one validated
  anchor (Re-DocRED null) is near-mechanical (rerank_blocked via frac(W==Z)=0.94 restates the realized null); it MISPREDICTS
  CLUTRR self-consistency (marginal win-rate 0.482 => predicted 'gate adds value'/positive, yet the powered paired diagonal
  is DISCONFIRMED, realized FDR 1.0, CI [0.66,1.0]); independent_and_correct_count=0. (4) HONEST PANEL — figure_panel arrays
  (x=[0.04471,0.482,0.103,0.34], y=[0.60293,null,null,null]) + paper-ready caption + figures/regime_panel.jpg, plus a reframing_recommendation
  to LEAD with the marginal-vs-paired conceptual result and present the diagnostic as a heuristic with stated A=C redundancy.
  Contamination caveat: excluding 515 contaminated decoys LOWERS the win-rate (0.0623->0.0277), strengthening the demotion.
  Output eval_out.json validates against schema exp_eval_sol_out (rich blocks nested under metadata; metrics_agg has 31 numeric
  scalars; datasets carry the per-set identity table and the 4-point regime panel with predict_/eval_/metadata_ fields). Deterministic
  (seed=0; only winrate CIs use the B=2000 doc-block bootstrap). Companion: README.md, pinned pyproject.toml.
id: art_iCOHKeSAQZhn
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Short descriptive figure title",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title - concise, descriptive, captures the main contribution",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 12:51:39 UTC

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

### [4] ASSISTANT · 2026-06-16 12:51:40 UTC

```
Please run /login · API Error: 401 Invalid authentication credentials
```

### [5] SYSTEM-USER prompt · 2026-06-16 12:51:41 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [6] ASSISTANT · 2026-06-16 12:51:44 UTC

```
Please run /login · API Error: 401 Invalid authentication credentials
```

### [7] SYSTEM-USER prompt · 2026-06-16 12:51:45 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [8] ASSISTANT · 2026-06-16 12:51:47 UTC

```
Please run /login · API Error: 401 Invalid authentication credentials
```
