# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 14:36:10 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Decoy-Gated Neuro-Symbolic Extraction: A Label-Free FDR Gate at the Text-to-Logic Boundary and the Exchangeability Gap That
  Bounds It
abstract: >-
  Pipelines that translate short professional documents into executable first-order logic depend on an LLM to resolve fuzzy
  unifications, and that interface is exactly where plausible, high-confidence false facts enter and silently corrupt every
  downstream deduction. We import the knockoff / target-decoy machinery that genomics uses to control the false discovery
  rate (FDR) without labels, and build, to our knowledge, the first label-free FDR gate at this neural-to-symbolic admission
  boundary: before any LLM-proposed Prolog fact or bridge is admitted, it must out-score a plausibility-matched counterfactual
  decoy in a knockoff+ competition. We execute the protocol end to end and report measured outcomes, including those that
  disconfirm. Our central, surprising finding answers a prior methodology objection directly: re-run under the diagnostic-validated
  K=5 self-consistency elicitation, the gate fails to control FDR on the error-dense multi-hop family (realized FDR 1.0 at
  the only certifiable target alpha*=0.5, bootstrap CI [0.66,1.0])---even though the decoys are marginally exchangeable with
  the model's own spontaneous errors (KS p=0.058) and distinct from true positives (KS p=5e-9). We localize the cause: marginal
  decoy exchangeability does not imply the per-pair sign-flip property knockoff+ requires, so a win-rate diagnostic over-certifies
  the gate. Despite the missing certificate, the pipeline delivers what the application demands: on 24 genre-faithful legal/news/regulatory
  documents it cuts the corrupted multi-hop conclusion rate from 0.48 to 0.18 and the atomic hallucination rate ~25% (directional)
  with conservative self-report and exported auditable trace-graphs; and a new gold-free regime-diagnostic correctly predicts
  the null operational wedge on 152 Re-DocRED documents. The result is a reproducible map (~$2.6, commodity CPU) of where
  decoy gating helps, where it is redundant, and where its certificate breaks.
paper_text: |2

  # Introduction

  A pipeline that converts unstructured prose into a formal, computable representation---one a logic engine such as SWI-Prolog can execute---promises the best of two worlds: the broad coverage of an LLM as a semantic translator, and the verifiable, auditable inference of a symbolic reasoner. The recurring failure point of such a pipeline is not parsing syntax but the *fuzzy-unification boundary*: when strict symbolic matching fails, an LLM must align a surface predicate to a schema relation and supply implicit background knowledge, and exactly at that interface hallucination re-enters and propagates into every deduction that consumes the admitted fact. The dangerous hallucinations are not random nonsense; they are *plausible, high-confidence false facts* that a downstream solver treats as ground truth.

  The problem is both important and hard. It is important because a single fabricated premise admitted into a knowledge base contaminates an unbounded set of multi-hop conclusions, and because the application domains that most need auditable reasoning---short legal documents, news, regulatory text---are precisely those where a silently wrong fact is most costly. It is hard because the standard defenses do not act where the damage occurs. Self-consistency and LLM-as-judge are heuristic and give no quantitative control. Ontology-constraint filtering rejects only encoded violations and needs a rich trusted constraint set. The strongest uncertainty-quantification methods---conformal factuality [15], conformal selection with Benjamini--Hochberg [16], multiple-testing hallucination detection [18], coherent factuality over reasoning chains [17], conformal e-value novelty detection [29], and conformal link-prediction FDR [30]---all require a *labeled* calibration set and certify the *final answer or claim set*, not the *admission* of an intermediate fact into the symbolic layer.

  Why has the admission boundary not been controlled before? Because the natural statistical tool for controlling false admissions among many candidate signals with no ground truth---the *false discovery rate* (FDR)---was developed in numeric feature selection and mass spectrometry, where a synthetic negative control exchangeable *by construction* is available. Genomics and proteomics solved an isomorphic label-poor problem---selecting true signals among overwhelming noise with a guaranteed FDR and no labels---via the knockoff filter [4, 5] and target-decoy competition, and learned the two ways the trick breaks: decoys *too unrealistic to fool* the scorer make the estimated FDR optimistic (cured by property-matched decoys [9]), and the entrapment false-discovery proportion (FDP) must be bounded by a mechanism built *independently* of the decoys [6]. We transplant this machinery to the LLM neural-to-symbolic boundary, label-free, and---this being a working environment with no construction-level guarantee---we *test* the validity condition rather than assume it.

  This paper executes the protocol end to end and reports the realized numbers, including the ones that disconfirm. We propose *decoy-gated extraction*: before any LLM-proposed Prolog fact or bridge enters the knowledge base, it must out-score a *plausibility-matched* synthetic decoy---a document-conditioned counterfactual the model finds plausible but the document does not entail---in a knockoff+ competition that admits the most permissive cutoff whose estimated corpus-aggregate FDR is at most a target $\alpha$, using zero operation labels. The single canonical competition statistic is the knockoff+ *signed maximum* $W_i = \operatorname{sign}(Z_i - \tilde{Z}_i)\,\max(Z_i, \tilde{Z}_i)$, where $Z_i$ and $\tilde{Z}_i$ are the label-free scores of the real candidate and its matched decoy; knockoff+ thresholding admits $\{i : W_i \ge T\}$ at the most permissive $T$ whose estimate $\widehat{\mathrm{FDR}}(T) = (1 + \#\{W_i \le -T\}) / \max(1, \#\{W_i \ge T\}) \le \alpha$ [4]. Validity rests on the *null sign-flip property*---for genuinely false candidates the sign of $W_i$ must be a fair coin conditional on $|W_i|$---and because LLM decoys carry no construction-level proof of it, the realized-FDR-versus-$\alpha$ diagonal *is* its empirical test.

  A previous version of this work reported a CLUTRR calibration diagonal that appeared *conservatively calibrated*. Reviewers correctly observed that this diagonal was computed under a *verbalized* confidence elicitation whose own decoy win-rate diagnostic flags it as strongly anti-conservative ("decoys too easy"), so the apparent conservatism could not be evidence of exchangeability. This paper takes that objection as its organizing question. We re-run the headline diagonal under the K=5 *self-consistency* elicitation that the win-rate diagnostic actually validates (counterfactual tail win-rate $0.48$, covering $0.5$) \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-3/experiment-1}}. The result is the paper's central, surprising finding: under the validated elicitation the gate *does not* control FDR on the error-dense multi-hop family---realized FDR is $1.0$ at the only certifiable target $\alpha^{*}=0.5$ (12 admitted, all 12 false; document-block CI $[0.66,1.0]$ lies entirely above $\alpha^{*}$), and the gate's own self-report $\widehat{\mathrm{FDR}}=0.5$ undershoots it. The pre-registered primary disconfirmation fires.

  [FIGURE:fig1]

  What makes this informative rather than merely negative is *why* it happens, and we localize the cause precisely. Self-consistency *does* restore the property the diagnostic measures: the counterfactual-decoy score distribution is statistically indistinguishable from the model's own spontaneous errors (full-distribution KS $p=0.058$; admission-tail KS $p=0.31$; both fail to reject) and sharply distinct from true positives (KS $p=5\times10^{-9}$). That is *marginal* (distributional) exchangeability. The knockoff+ gate, however, needs the *per-pair* sign-flip property at the cutoff, and it fails: among the twelve admitted multi-hop reals, the model scored each false real *above* its own matched decoy. Distributional exchangeability is necessary but not sufficient for paired exchangeability---and the win-rate diagnostic, being a marginal statistic, cannot see the gap. This two-layer decomposition is, we argue, the generalizable lesson of transplanting knockoffs to LLM scoring.

  The same rigor is then applied where the goal actually lives. We *execute* the previously-missing application headline on a genre-faithful 24-document legal/news/regulatory anchor \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-3/experiment-2}}: the operational pipeline ingests ~3000-character documents, types entities against an upper ontology, gates extracted facts, runs multi-hop deductions, and emits auditable trace-graphs whose every leaf carries a provenance span and the decoy and entrapment certificates that licensed it. Here the gate behaves better than on the hard CLUTRR family---its self-report is *conservative*, it cuts the corrupted multi-hop conclusion rate from $0.48$ to $0.18$, and it reduces the atomic hallucination rate by ~$25\%$ (directional; bootstrap CIs overlap at $n{=}24$). Finally, on $152$ Re-DocRED documents the operational wedge over plain thresholding is disconfirmed at recall $\le0.075$, and we recast the operational contribution as a *gold-free regime-diagnostic* that predicts that null result without labels (prediction correct) [ARTIFACT:art_RZC2468yZ-Jh].

  **Summary of contributions.**

  - We formulate the *text-to-logic admission boundary* as an FDR-control problem and introduce *decoy-gated extraction*, to our knowledge the first label-free FDR knob at the neural-to-symbolic interface, built from a single canonical knockoff+ statistic, plausibility-matched counterfactual decoys, and independent entrapment corroboration (Sections 3--4).
  - We answer the central methodology objection by re-running the calibration diagonal under the diagnostic-validated self-consistency elicitation, and report the pre-registered disconfirmation honestly: the gate does not control FDR on the populable multi-hop family (Section 6.1).
  - We isolate the mechanism---*marginal decoy exchangeability does not imply paired sign-flip exchangeability* at the cutoff---and show the win-rate diagnostic, being marginal, over-predicts gate validity, a fundamental blind spot we report rather than paper over (Sections 6.2--6.3).
  - We *execute* the genre-faithful application headline the prior draft was missing: a quantified, regime-mapped hallucination-reduction run on 24 professional documents with exported auditable trace-graphs, including a multi-hop corruption drop from $0.48$ to $0.18$ (Section 6.4).
  - We scale the Re-DocRED operational test to its true scope (152 documents, recall $\le0.075$, all comparators participating, powered multi-hop comparison) and contribute a novel *label-free regime-diagnostic* that forecasts the gate's null wedge gold-free (Section 6.5).

  # Related Work

  **Label-free hallucination scoring.** Zero-resource detectors produce per-claim hallucination scores from sampling consistency (SelfCheckGPT [13]) or distractor-normalized verbalized confidence (DINCO [12]); FactSelfCheck [14] operates natively at the fact level over $(h, r, t)$ triples. These methods yield a *score*, not an admission threshold, and offer no exchangeability or competition argument. In our framework they are *candidate elicitations* feeding the gate, not the gate itself, and we select among them by *tail* behavior. Verbalized confidence is known to be overconfident in the upper tail [10], and token log-probability calibration degrades under reinforcement learning from human feedback [11]---two facts our results turn from caveats into a measured, central phenomenon.

  **Labeled uncertainty quantification for LLMs.** Conformal factuality [15] removes claims until a factuality level is met, using a labeled calibration set, and certifies the emitted answer; coherent factuality [17] extends this to reasoning chains; conformal selection [16], multiple-testing hallucination detection [18], and online/feedback-driven testing [19] control FDR over candidate outputs but require labeled calibration outcomes; conformal e-value novelty detection [29] and conformal link prediction [30] control FDR over selected test points or predicted edges under (adapted) exchangeability of a labeled reference set. Table 1 contrasts the closest neighbors. Every one is *labeled* and certifies a *model output* under assumed exchangeability; ours is *label-free*, targets an *intermediate admission boundary*, manufactures the null behavior with engineered-and-tested decoys, and---crucially---empirically *tests* the exchangeability that the others assume \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-2/research-1}}. The distinction defuses the natural rebuttal that decoy-gating "is just conformal selection at the fact level": conformal selection imports exchangeability from a labeled calibration set whose outcomes are observed, whereas we have zero such labels and must test the fair-coin sign-flip property in the score tail---and we find that it can fail.

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

  The pipeline has six stages: over-generating extraction, plausibility-matched decoy generation, isolated provenance-blinded scoring, the knockoff+ FDR gate, independent entrapment corroboration, and symbolic reasoning with auditable trace-graphs. The full implementation specification---verbatim prompt templates, on-disk formats, and library APIs---is provided in the supporting research artifacts \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-1/research-1}}\footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-1/research-2}}.

  ## Extraction with deliberate over-generation

  A cheap LLM proposes typed first-order facts and bridges from the document in a LINC/Logic-LM style [20, 21], with argument types grounded in a commodity upper-ontology slice. Because OpenCyc was discontinued by Cycorp in March 2017 and survives only as unmaintained mirrors, and ResearchCyc is license-gated, OpenCyc cannot be a reproducible commodity dependency; we substitute an offline WordNet [32] hypernym lookup that maps each argument head noun into the coarse vocabulary $\{$PER, LOC, ORG, TIME, NUM, MISC$\}$ via anchor synsets, each coarse type further anchored to a SUMO upper-ontology class (e.g. `person.n.01` $\to$ PER $\to$ `&%Human`) [31]. Typing is used *only* to constrain decoy generation and entity linking, never to filter; because it never rejects a candidate it cannot break the FDR guarantee. The extractor deliberately *over-generates* (temperature $0.7$, multiple samples unioned) so the candidate pool is dense in genuine false positives---a precondition for a non-vacuous calibration diagonal.

  ## Plausibility-matched counterfactual decoys

  The load-bearing design choice is the decoy family. The relevant target distribution at the LLM boundary is not the true-positive distribution DeepCoy matches in molecular screening [9], but the distribution of the model's *own spontaneous false extractions*---the plausible hallucinations the gate must actually catch. Our primary family is the *document-conditioned counterfactual*: given the document and the relation/type schema, the model produces a maximally plausible fact or bridge that is *not* entailed by the text, matching the surface form and specificity of the document's real facts. Every decoy passes an independent isolated non-entailment check (an accidentally entailed decoy is actually true and would bias the FDR conservatively); the contamination rate is logged (CLUTRR $8.4\%$, application anchor $5.7\%$) . As a deliberately retained negative control we also generate *random type-matched swaps*, predicted to read anti-conservative precisely because they are too easy. Crucially, we do not assume the decoys match the spontaneous-error distribution---we *test* it (Section 6.2), and, as the same section shows, we test whether marginal matching is sufficient.

  ## Isolated, provenance-blinded scoring and elicitation selection

  Each candidate---real, decoy, or entrapment---is scored in its *own* prompt with source identity masked and presentation order randomized, removing within-batch contrast effects that would let the model implicitly detect a fabricated item and depress its score. Document-prefix prompt caching makes isolated scoring affordable. The per-candidate score is produced by a *tail-exchangeability*-selected elicitation, not an average-calibration-selected one. This selection criterion is the key correction over the prior draft: a Phase-0 pilot ranks verbalized confidence, a DINCO-style distractor-normalized score [12], a $K$-sample self-consistency score [13, 14], and a log-probability yes/no score by their *tail* decoy win-rate (target $\approx 0.5$), not by full-distribution AUC. The distinction matters because the two criteria disagree: verbalized confidence and DINCO have higher full-distribution AUC ($0.861$ and $0.871$) yet fail the tail test, whereas K=5 self-consistency has the tail win-rate that covers $0.5$ ($0.482$) \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-2/experiment-2}}. Higher AUC does not imply tail-exchangeability; self-consistency therefore hosts the headline diagonal. The generator$\neq$scorer ablation that de-circularizes the construction is settled (Section 6.3) and carried forward.

  ## The knockoff+ FDR gate and its self-report

  Given the competition statistics, the gate admits $\{i : W_i \ge T\}$ at the smallest cutoff $T$ for which $\widehat{\mathrm{FDR}}(T) \le \alpha$ [4]. We keep the conservative $+1$ for the headline certificate. Beyond realized FDR (against gold) and the target $\alpha$, we *always* report the gate's internal estimate $\widehat{\mathrm{FDR}}$, so that the failure mode "the estimate is anti-conservative" ($\widehat{\mathrm{FDR}} < \text{realized}$) is surfaced as its own disconfirmation even when realized FDR lands below $\alpha$.

  ## Independent entrapment corroboration

  Decoy competition decides admission; *entrapment* provides an independent upper bound on the realized FDP, built by a mechanism *distinct* from the decoys (in-genre cross-document swaps, numeric or temporal perturbation, explicit contradiction) and constructed *without* the generating LLM. We use the valid combined estimator $\widehat{\mathrm{FDP}} = N_E(1 + 1/r)/(N_T + N_E)$ as the default certificate [6], with $N_T,N_E$ the admitted target and entrapment counts and $r$ the entrapment-to-target ratio; we never use the naive estimator, which Wen et al. prove biased [6].

  ## Symbolic reasoning and auditable trace-graphs

  Admitted facts and bridges populate a backward-chaining knowledge base for multi-hop deduction; we target SWI-Prolog through the `janus-swi` bridge and fall back to a pure-Python meta-interpreter with an identical trace-graph schema when the native bridge is unavailable . A `solve/2`-style meta-interpreter captures the proof as a *trace-graph* whose nodes are sub-goals and derived facts and whose edges are labeled rule applications. Every leaf resolves to a certificate term: the provenance span, the decoy-competition certificate $(W_i, T, \alpha)$, and the entrapment certificate $(\widehat{\mathrm{FDP}}, r)$. The trace-graph serializes to JSON for machine audit and Graphviz DOT for human audit. A designed *probabilistic* upgrade swaps the deterministic query for ProbLog's `get_evaluatable().evaluate()` [33], turning each admitted clause into a weighted clause $p_i :: \mathrm{fact}$ with $p_i$ a calibrated function of $Z_i$, so derived conclusions carry marginal probabilities while every leaf retains its certificate .

  # Experimental Setup

  The evaluation is split so that calibration and operational usefulness are proven on the data each suits, and the protocol is pre-registered so every outcome---confirmed, disconfirmed, or untestable---is interpretable.

  ## Three anchors with a clean division of labor

  CLUTRR [1] is rule-based and templated, so its kinship gold is exact---the property that lets it host the realized-FDR-versus-$\alpha$ *diagonal* and the single primary disconfirmation. The corpus draws on a standardized atomic + multi-hop kinship triple set derived entirely from CLUTRR's own `proof_state` fields over a 20-relation vocabulary \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-1/dataset-1}}; the diagonal in this paper is computed on the error-dense $40$-document checkpoint of the scaled confirmatory split, which yields $410$ extracted reals ($123$ true, $287$ spontaneous false) and is populable on both families ($129$ false atomic, $158$ false multi-hop, exceeding the pre-registered $N_{\text{false\_min}}=40$ floor) . Re-DocRED [2] is human-annotated, open-vocabulary, and document-level, so it hosts the *operational* comparison and the genuine schema-alignment bridge test; the anchor comprises Wikipedia documents with gold $(head, relation, tail)$ triples over $96$ Wikidata relations \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-1/dataset-2}}, and because it retains residual false negatives it licenses only *relative* operational comparisons. Finally, the genre-faithful *application anchor* is $24$ genuine professionally-written documents ($8$ legal, $8$ news, $8$ regulatory; native length $1239$--$3474$ characters, mean $2372$, squarely in the ~3000-character target range), standardized to the same triple schema with character-span provenance and $140$ human/structure-derived gold facts built with no LLM in the loop \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-2/dataset-1}}. CLUTRR tests whether the knob is calibrated; the application anchor tests whether it reduces hallucination on the documents the goal targets; Re-DocRED tests whether it beats plain thresholding operationally.

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

  Re-running the headline diagonal under the diagnostic-validated K=5 self-consistency elicitation reverses the prior draft's claim . On the error-dense multi-hop family---the pre-registered populable family, ~$85\%$ genuine false because the extractor's forced multi-hop relation accuracy is only $0.17$---the gate certifies admissions at exactly one target, $\alpha^{*}=0.5$ (the $1/k$ floor blocks all stricter $\alpha$). At that target the realized FDR against crisp gold is $1.0$: of $12$ admitted reals, all $12$ are document-non-entailed, with document-block CI $[0.66,1.0]$ lying entirely above $\alpha^{*}$. The gate's own self-report $\widehat{\mathrm{FDR}}=0.5$ undershoots the realized $1.0$. The pre-registered primary disconfirmation therefore *fires* on both the calibration and the self-report criteria.

  [FIGURE:fig2]

  The atomic family tells the same story more mildly: at $\alpha=0.3$ realized FDR is $0.377$ (61 admitted, 23 false) against a self-report of $0.279$---a target violation ($0.377>0.3$) and an anti-conservative self-report---while at $\alpha=0.5$ realized FDR is $0.422$ with self-report $0.491$ (within target). Across both families the plain confidence-threshold baseline is worse still (multi-hop realized FDR $0.80$--$0.87$; atomic $0.17$--$0.55$), so decoy competition *helps relative to plain thresholding* even here---but "better than an uncontrolled baseline" is not "controls FDR at $\alpha$," and we do not claim the latter. The prior draft's apparent conservatism \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/tree/main/round-2/experiment-1}} is, when the same verbalized elicitation is re-run on this data, a discreteness/loose-target artifact: the verbalized diagonal admits *nothing* on the multi-hop family at any $\alpha$ and violates the target on the atomic family at $\alpha=0.5$ (realized $0.534>0.5$, self-report $0.5$) . We therefore retain verbalized only as a documented contrast, never as a co-headline.

  ## Why the gate fails: marginal vs. paired exchangeability (S1)

  The disconfirmation is informative because the marginal precondition the diagnostic checks *does* hold under self-consistency. The counterfactual-decoy score distribution is statistically indistinguishable from the model's own spontaneous-error distribution---full-distribution KS $p=0.058$, Mann--Whitney $p=0.061$, Anderson--Darling $p=0.061$, permutation $p=0.060$ (all fail to reject), tightening in the admission tail (top-25\% KS $p=0.31$)---and sharply distinct from the true-positive distribution (KS $p=5\times10^{-9}$, Mann--Whitney $p=4\times10^{-12}$) . By the marginal criterion the decoys are exactly right: they look like the spontaneous errors, not like the true facts.

  [FIGURE:fig3]

  Yet the paired competition fails. Among the twelve admitted multi-hop reals, the model assigned each false real a *higher* self-consistency score than its own matched decoy---the per-pair sign-flip property knockoff+ requires is violated precisely in the admission tail where it matters. The reconciliation is that marginal (distributional) exchangeability is strictly weaker than paired exchangeability: two pooled distributions can coincide while, pair by pair, the false real systematically out-scores its decoy. This gap is the generalizable lesson. Property-matched decoy design and win-rate/CDF diagnostics, imported from cheminformatics and proteomics, certify the *marginal* property; the knockoff theorems need the *paired* one; at the LLM boundary the two come apart, and a marginal diagnostic cannot detect the difference. We state this as a limitation of the entire decoy-competition approach to LLM fact admission, not of one elicitation.

  ## The diagnostic blind spot and de-circularization (S1b, S2b)

  The blind spot has a second, independently measured face. Under the very K=5 self-consistency that restores marginal exchangeability, the random-swap negative control---which *must* read anti-conservative---is no longer reliably flagged: at this checkpoint the difficulty ladder L0--L4 is underpowered (only two false pairs reach the operative tail per rung), and its verdict is `PARTIAL`---the diagnostic detects only grossly out-of-context (foreign-entity) decoys and loses resolution for in-distribution rungs . Combined with the marginal-vs-paired gap, this means the win-rate diagnostic both (i) over-predicts paired validity and (ii) loses sensitivity to too-easy decoys in the regime where it is supposed to be trusted. We therefore *downgrade* the prior draft's "the diagnostic tells the practitioner which regime they are in" claim to "the diagnostic detects gross non-exchangeability and tail-overconfidence but cannot certify paired validity," and we mark a sensitive paired-exchangeability diagnostic as required future work.

  The one circularity concern that *is* settled is shared-model bias. The generator$\neq$scorer ablation is robust: across all four $(G,S)$ configurations---including decoys generated by gpt-4.1-nano and scored by the cross-family ministral-8b, and the symmetric swap---the tail win-rate CI covers $0.5$ (e.g. $0.491$, CI $[0.37,0.61]$, KS $p=0.999$) . The marginal exchangeability self-consistency restores is therefore not an artifact of one model scoring its own outputs; the *paired* failure is likewise not a circularity artifact but a genuine property of LLM tail scoring.

  ## The application headline: hallucination reduction and auditable traces (S4b)

  We then execute the genre-faithful application run the prior draft was missing, on the 24-document legal/news/regulatory anchor, reporting both elicitations across the full $\alpha$ grid so the regime-dependence is never obscured . Three honest findings follow.

  [FIGURE:fig4]

  *First, the atomic hallucination reduction is directional, not significant.* At the only certified target ($\alpha=0.5$; the $24$-document corpus floors stricter $\alpha$ at zero admissions), the pooled gate hallucinated-fact rate is $0.183$ under self-consistency and $0.178$ under log-probability, versus the $\alpha$-invariant raw-LLM rate of $0.243$---a ~$25\%$ relative reduction---but $0$ of $40$ grid cells reach bootstrap-CI separation at $n=24$, so the reduction is directional. The largest single-cell reduction is regulatory under self-consistency: raw $0.439\to$ gate $0.360$. *Second, and in pointed contrast to the CLUTRR multi-hop regime, the gate's self-report here is conservative*---$\widehat{\mathrm{FDR}}\ge$ realized FDR in every one of the $40$ cells---so the second-order disconfirmation does not fire on this anchor. *Third, the multi-hop corruption result is the clearest positive*: the raw-LLM knowledge base derives $23$ conclusions at a $0.48$ corrupted rate, whereas the gated knowledge base at $\alpha=0.5$ derives $11$ conclusions at a $0.18$ corrupted rate, with the regulatory genre dropping from $0.92$ to $0.67$ and legal from---already clean---$0.0$ to $0.0$. Gating removes the premises that would otherwise propagate into corrupted deductions.

  [FIGURE:fig5]

  Every admitted fact enters the symbolic layer with a full certificate, and the pipeline exports auditable trace-graphs (six documents, JSON + Graphviz DOT) whose leaves carry provenance, decoy, and entrapment certificates. For example, the legal proof of `party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1 2005)` resolves through `has_party` ($W_i=0.842$, $T=0.129$, $\alpha=0.5$) and `effective_date` ($W_i=0.790$), each annotated with the entrapment certificate $(\widehat{\mathrm{FDP}}=0.667, r=1)$; a regulatory proof of `titled_obligation(Art.~7 GDPR, ...)` exposes a *rejected* leaf (`obligates`, $W_i=-0.333$) directly in the trace, making the gate's decision human-auditable. Honesty requires three caveats we record at the point of claim: extraction quality on these genres is modest (atomic precision/recall: legal $0.28/0.27$, news $0.29/0.18$, regulatory $0.17/0.42$); $117$ of $210$ reals are gold-undecidable, so hallucination is reported by gold-membership with silver bounds; and the cross-family adjudicator was *dropped* because its agreement with the crisp legal gold was poor ($\kappa=0.10<0.4$), partly because the CUAD gold itself has partial recall.

  ## Re-DocRED: disconfirmed wedge, reframed as a gold-free regime-diagnostic (S4)

  We report the operational result at its true, now-corrected scope [ARTIFACT:art_RZC2468yZ-Jh]. Scaling from the prior $36$ documents to the full $152$ confirmatory documents, ranking the identical candidate pool by the knockoff+ statistic $W_i$ does *not* beat ranking by raw confidence $Z_i$ at matched recall: across the recall grid (ceiling $0.075$, the shared METHOD/PLAIN maximum) no point shows a precision gain with bootstrap CI entirely above zero, so the pre-registered verdict is an operational disconfirmation---*at recall $\le0.075$ on 152 documents*. Two reviewer-flagged weaknesses are fixed. All five systems now participate: relaxing the matched-recall floor to the lowest positive maximum recall ($0.034$) gives the recall-limited CoT ($0.051$) and RAG ($0.034$) at least one evaluable point, so no all-null baseline is listed as a comparator. And the multi-hop comparison is *powered*: six gold-justified Wikidata inverse rules densify forward-chained conclusions to $267$ per system (far above the pre-registered power target of $100$), giving a hallucinated-conclusion-rate difference of $-0.004$ (CI $[-0.018,0.008]$)---a precisely null effect, not an underpowered one.

  The substantive new contribution is to recast this null as a *prediction*. A label-free regime-diagnostic (zero API calls, no gold) reads four cached signals: the tail decoy win-rate ($0.045$, far below $0.5$ $\Rightarrow$ decoys too easy), the spontaneous-error CDF match (decoy mean $0.165$ vs. low-self-consistency real mean $0.857$; KS/MW/permutation all reject $\Rightarrow$ too easy), the $W$-versus-$Z$ ranking divergence (fraction of candidates with $W_i=Z_i$ equal to $0.939$, admitted-set Spearman $\rho=0.991$ $\Rightarrow$ the gate keeps and orders the same facts as the plain threshold, so the wedge is *mechanically* null), and base-scorer calibration (AUC $=0.60$). The diagnostic emits "GATE REDUNDANT, predicted wedge sign null," which the realized wedge confirms (prediction correct). Placed beside the CLUTRR regimes, the diagnostic yields a unifying---and honestly caveated---two-axis picture: gate value rises with base-scorer tail-overconfidence but is *conditional* on decoy exchangeability. The one point this two-axis map gets *wrong* is the very point our calibration diagonal corrects: the CLUTRR self-consistency win-rate of $0.482$ would predict "gate adds value," yet the powered paired diagonal disconfirms it (Section 6.1). That contradiction is not a flaw in the reporting---it is the clearest possible statement of this paper's central finding, that a marginal win-rate cannot certify paired validity.

  ## Cost and reproducibility

  The entire iteration ran on commodity CPU: the corrected self-consistency diagonal cost \$0.02 (cache-warm), the application headline \$0.31, and the Re-DocRED regime-diagnostic \$1.08, for ~\$1.4 this iteration and ~\$2.6 cumulative against the \$10 cap, with exact per-call metering and a persistent on-disk cache enabling free resumes [ARTIFACT:art_RZC2468yZ-Jh]. All anchors regenerate deterministically under fixed seeds.

  # Discussion

  **What we now know, and where the certificate breaks.** Decoy-gated extraction is the first label-free FDR knob proposed at the fuzzy-unification boundary, and executing it carefully has taught a precise lesson that a working certificate would have hidden. The validity of a knockoff-style gate at the LLM boundary decomposes into two layers: a *marginal* layer (decoy scores distributed like the model's spontaneous errors), achievable by an aggregation elicitation and verifiable label-free; and a *paired* layer (the false real and its decoy equally likely to win at the cutoff), which the knockoff theorems actually require and which we find can fail even when the marginal layer holds. The standard decoy-quality diagnostics imported from genomics and proteomics live entirely in the marginal layer, so they *over-certify* the gate. This is, to our knowledge, the first demonstration that the marginal/paired distinction is operative---and consequential---when knockoffs are transplanted to LLM scoring.

  **The honest value proposition.** The gate's *operational* value over plain thresholding is concentrated where the base elicitation is tail-overconfident and the decoys are exchangeable, and is null where the base scorer is already calibrated (Re-DocRED). The gate's *certified-FDR* value is, on present evidence, not established on hard multi-hop families: marginal exchangeability is necessary but not sufficient. What survives unambiguously is the *auditable pipeline*---typed extraction, a quantitatively-reported (if directional) hallucination reduction on genre-faithful documents, a measured drop in corrupted multi-hop conclusions ($0.48\to0.18$), and per-leaf certificates---and the *gold-free regime-diagnostic*, which correctly forecasts where the gate is redundant. These are the deliverables the goal requires, and they do not depend on the missing certificate.

  **Limitations.** First and foremost, the FDR certificate is disconfirmed on the populable CLUTRR multi-hop family under the diagnostic-validated elicitation; we do not claim label-free FDR control there. Second, the self-detecting diagnostic has a structural blind spot: a marginal win-rate cannot certify paired validity, and at our checkpoint the difficulty ladder is underpowered, so the "tells you when to trust the gate" claim is downgraded accordingly. Third, the CLUTRR diagonal is computed on a $40$-document checkpoint; a powered re-run is the immediate next step, though the disconfirmation direction (realized $1.0$, CI above $\alpha^{*}$) is unlikely to reverse. Fourth, the application hallucination reduction is directional, not CI-separated, at $n=24$, and its gold is partly silver. Fifth, we descope two named goal requirements with stated rationale: OpenCyc is discontinued, so we substitute an offline WordNet$\to$SUMO typing stack that supplies taxonomic grounding but not Cyc's assertional commonsense KB; and the executed reasoning layer is deterministic backward chaining, with the ProbLog probabilistic upgrade designed and specified but not yet run .

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
summary: >-
  This paper builds the first label-free FDR gate at the LLM text-to-logic admission boundary by importing knockoff/target-decoy
  competition, then rigorously executes and reports its limits. Re-running the calibration diagonal under the diagnostic-validated
  self-consistency elicitation, the gate's FDR certificate is disconfirmed on the error-dense CLUTRR multi-hop family (realized
  FDR 1.0 at the only certifiable alpha*=0.5), and the cause is localized precisely: self-consistency restores marginal decoy
  exchangeability (decoy distribution matches the model's spontaneous errors, KS p=0.058) but not the paired sign-flip property
  knockoff+ requires, so a marginal win-rate diagnostic over-certifies the gate. Despite the missing certificate, the operational
  pipeline delivers the goal's deliverables: on a genre-faithful 24-document legal/news/regulatory anchor it cuts the corrupted
  multi-hop conclusion rate from 0.48 to 0.18 and the atomic hallucination rate ~25% (directional) with conservative self-report
  and exported auditable trace-graphs; and a new gold-free regime-diagnostic correctly predicts the null operational wedge
  on 152 Re-DocRED documents. The contribution is a reproducible (~$2.6, commodity CPU) map of where decoy gating helps, where
  it is redundant, and where its certificate breaks.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Decoy-Gated Neuro-Symbolic Pipeline
caption: >-
  End-to-end decoy-gated text-to-logic pipeline. A short document is over-generated into typed first-order facts and bridges;
  each candidate is paired with a plausibility-matched counterfactual decoy and an independently-built entrapment item; an
  isolated, provenance-blinded self-consistency elicitation scores all of them; the knockoff+ gate admits candidates with
  $W_i \ge T$ at the most permissive target whose estimated FDR is $\le\alpha$; admitted facts populate a backward-chaining
  knowledge base that emits a trace-graph whose every leaf carries provenance, decoy $(W_i,T,\alpha)$, and entrapment $(\widehat{\mathrm{FDP}},r)$
  certificates.
image_gen_detailed_description: >-
  Horizontal left-to-right flow diagram, 21:9, clean white background, sans-serif labels, no 3D. Box 1 (gray) 'Short document
  (~3000 chars: legal / news / regulatory)'. Arrow to Box 2 (blue) 'Over-generating extraction (temp 0.7, samples unioned)
  + WordNet->SUMO typing {PER,LOC,ORG,TIME,NUM,MISC}' outputting 'typed facts & bridges'. From Box 2, two parallel arrows
  to a stacked pair: Box 3a (light blue) 'Counterfactual decoy ~Z' and Box 3b (light orange) 'Entrapment item (no LLM, r=1)'.
  All three (real, decoy, entrapment) feed Box 4 (green) 'Isolated provenance-blinded scoring; K=5 self-consistency; document-prefix
  cache'. Arrow to Box 5 (dark green, emphasized, thick border) 'knockoff+ FDR gate: W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i);
  admit {W_i >= T}; report (alpha, FDR-hat, realized FDR)'. A small red dashed callout under Box 5 reads 'certificate can
  fail: marginal != paired exchangeability'. Arrow to Box 6 (purple) 'SWI-Prolog / backward-chaining KB; multi-hop deduction'.
  Arrow to Box 7 (teal) 'Auditable trace-graph (JSON + Graphviz DOT); per-leaf provenance + decoy(W,T,alpha) + entrapment(FDP-hat,r)'.
  Below Box 5, a separate small gray box labeled 'Plain confidence threshold (zero-label foil): rank by Z_i only' connects
  to the gate with a dotted comparison arrow. Use a consistent muted palette; arrows thin black with small labels.
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram of the six-stage decoy-gated text-to-logic pipeline with per-leaf certificates.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Corrected CLUTRR Calibration Diagonal under Self-Consistency (Multi-Hop Family)
caption: >-
  Realized FDR versus target $\alpha$ on the populable CLUTRR multi-hop family under the diagnostic-validated K=5 self-consistency
  elicitation. The knockoff+ gate certifies admissions only at $\alpha^{*}=0.5$ (the $1/k$ floor blocks stricter targets);
  there realized FDR is $1.0$ (12/12 admitted are false), with document-block-bootstrap CI $[0.66,1.0]$ lying entirely above
  $\alpha^{*}$, and the gate's own self-report $\widehat{\mathrm{FDR}}=0.5$ undershoots it. The pre-registered primary disconfirmation
  fires. The plain threshold and swap-decoy baselines are worse still.
image_gen_detailed_description: >-
  Line/scatter plot, 16:9, white background, sans-serif. X-axis 'target alpha' from 0 to 0.55, ticks at 0.05,0.1,0.2,0.3,0.5.
  Y-axis 'realized FDR (vs crisp gold)' from 0 to 1.0. Draw a gray dashed identity line y=x labeled 'ideal y=x (FDR=alpha)'.
  Series GATE (dark green circles, solid line) present ONLY at alpha=0.5 with a single point at (0.5, 1.0) with a vertical
  error bar spanning 0.66 to 1.0; annotate this point 'realized 1.0; FDR-hat=0.5; 12/12 false; DISCONFIRMED'. For alpha 0.05,0.1,0.2,0.3
  draw small hollow green markers on the x-axis at y=0 labeled 'n_admitted=0 (below 1/k floor)'. Series GATE SELF-REPORT (green
  open squares, dotted) a single point at (0.5, 0.5) labeled 'FDR-hat'. Series PLAIN (red triangles, solid line) points: (0.05,0.80),(0.1,0.837),(0.2,0.848),(0.3,0.872),(0.5,0.844).
  Series SWAP control (orange diamonds) single point at (0.5, 0.857). Add a light-gray vertical band at x<0.5 labeled 'structurally
  undemonstrable (1/k floor)'. Legend top-left. Title 'Multi-hop family, self-consistency'.
aspect_ratio: '21:9'
summary: >-
  The corrected self-consistency diagonal showing the gate's FDR certificate is disconfirmed on the multi-hop family.
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Marginal vs. Paired Exchangeability
caption: >-
  The disconfirmation localized. Left: pooled score CDFs under self-consistency---the counterfactual decoy distribution is
  statistically indistinguishable from the model's own spontaneous errors (full KS $p=0.058$; tail KS $p=0.31$) and sharply
  distinct from true positives (KS $p=5\times10^{-9}$), so the *marginal* exchangeability the win-rate diagnostic checks holds.
  Right: at the admission cutoff the *paired* competition fails---all 12 admitted multi-hop reals out-score their own matched
  decoy (paired win-rate $0\%$), the property knockoff+ actually requires. Marginal exchangeability does not imply paired
  exchangeability.
image_gen_detailed_description: >-
  Two-panel figure, 16:9, white background, sans-serif. LEFT panel: cumulative distribution functions, X-axis 'self-consistency
  score Z' 0 to 1, Y-axis 'CDF' 0 to 1. Three curves: 'Counterfactual decoy' (blue solid, mean ~0.41), 'Spontaneous error
  (real-false)' (green dashed, nearly overlapping the blue, mean ~0.45), 'True positive' (orange dotted, shifted right, mean
  ~0.60). Annotate 'decoy vs spont: KS p=0.058 (fail to reject)' near the overlapping blue/green curves and 'decoy vs true-pos:
  KS p=5e-9 (reject)' near the orange curve. Title 'Marginal: decoys match spontaneous errors'. RIGHT panel: a bar/dot chart
  titled 'Paired: gate fails at the cutoff'. X-axis categories 'admitted multi-hop pairs (n=12)'. Show a single bar 'paired
  win-rate of decoy over false real = 0.00' (red, height 0 on a 0-1 axis) with a horizontal dashed reference line at 0.5 labeled
  'fair-coin (required)'. Add a text box: 'All 12 admitted false reals scored ABOVE their matched decoy => realized FDR 1.0'.
  Keep colors consistent across panels (decoy=blue, spontaneous=green, true-pos=orange).
aspect_ratio: '21:9'
summary: >-
  Conceptual+data figure showing decoys match spontaneous errors marginally but lose the paired competition at the cutoff.
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: 'Application Anchor: Hallucination and Multi-Hop Corruption Reduction (24 docs)'
caption: >-
  Executed application headline on the 24-document legal/news/regulatory anchor at the certified $\alpha=0.5$. Left: pooled
  atomic hallucinated-fact rate, raw LLM vs. gate---a directional ~25\% reduction (CIs overlap at $n=24$; 0/40 grid cells
  reach CI separation). Right: corrupted multi-hop conclusion rate drops sharply from raw-KB $0.48$ (23 conclusions) to gated-KB
  $0.18$ (11 conclusions). The gate's self-report is conservative on this anchor.
image_gen_detailed_description: >-
  Two-panel grouped bar chart, 16:9, white background, sans-serif. LEFT panel title 'Atomic hallucinated-fact rate (pooled,
  alpha=0.5)'. Y-axis 0 to 0.30. Bars: 'Raw LLM' = 0.243 (gray), 'Gate (self-consistency)' = 0.183 (green), 'Gate (logprob)'
  = 0.178 (blue). Error bars wide and overlapping (approx +/-0.07). Label '~25% relative, CI-overlapping' above the green
  bar. RIGHT panel title 'Corrupted multi-hop conclusion rate'. Y-axis 0 to 1.0. Bars: 'Raw-KB' = 0.48 (gray, annotate 'n=23
  derived, 11 corrupt'), 'Gated-KB alpha=0.5' = 0.18 (green, annotate 'n=11 derived, 2 corrupt'). Add small inset text 'regulatory
  genre: 0.92 -> 0.67; legal: 0.0 -> 0.0'. Consistent palette: raw=gray, gate=green/blue.
aspect_ratio: '21:9'
summary: >-
  Application-anchor results: directional atomic hallucination reduction and a clear corrupted-conclusion drop.
figure_path: figures/fig4_v0.jpg

--- Item 5 ---
id: fig5
title: Re-DocRED Operational Wedge and Gold-Free Regime-Diagnostic
caption: >-
  Left: matched-recall precision on 152 Re-DocRED documents (recall ceiling $0.075$). METHOD (knockoff+ $W_i$) and PLAIN (raw
  $Z_i$) are indistinguishable; CoT and RAG are recall-limited; the wedge is disconfirmed (no point with $\Delta$ CI $>0$).
  Right: the label-free regime-diagnostic places each anchor/elicitation on (decoy tail win-rate $\times$ base-scorer calibration)
  and predicts the wedge sign gold-free. Re-DocRED is predicted REDUNDANT (correct). The CLUTRR self-consistency point (win-rate
  $0.482$) would predict POSITIVE, yet the powered paired diagonal disconfirms it---the marginal diagnostic's blind spot.
image_gen_detailed_description: >-
  Two-panel figure, 16:9, white background, sans-serif. LEFT panel: line plot, X-axis 'matched recall' 0.034 to 0.075, Y-axis
  'precision' 0.15 to 0.28. METHOD (green solid) points approx: (0.034,0.265),(0.05,0.239),(0.063,0.191),(0.075,0.162). PLAIN
  (red dashed) nearly identical: (0.034,0.269),(0.05,0.246),(0.063,0.195),(0.075,0.161). CoT (blue dotted) short segment only
  from 0.034 to 0.051 around 0.25-0.26 then stops (label 'recall-limited, max 0.051'). RAG (purple dotted) single point at
  (0.034, 0.211) (label 'max 0.034'). Shaded gray band around METHOD-PLAIN difference labeled 'delta CI includes 0 at every
  recall => DISCONFIRMED'. Title 'Matched-recall wedge (152 docs, recall<=0.075)'. RIGHT panel: 2-axis scatter 'regime map'.
  X-axis 'decoy tail win-rate' 0 to 0.6 (vertical dashed line at 0.5 labeled 'exchangeable'). Y-axis 'base-scorer calibrated?'
  shown as two rows 'No' (bottom) and 'Yes' (top). Points (all base-scorer 'No' row here): 'Re-DocRED logprob' at x=0.045
  labeled 'predicted NULL / realized null (correct)'; 'CLUTRR verbalized' at x=0.103 labeled 'predicted NEGATIVE'; 'CLUTRR
  logprob' at x=0.34 labeled 'predicted NEGATIVE'; 'CLUTRR self-consistency' at x=0.482 labeled 'predicted POSITIVE but paired
  diagonal DISCONFIRMS (blind spot)' drawn as a red-circled point. Title 'Gold-free regime-diagnostic'. Use green for correct
  predictions, red ring for the over-prediction.
aspect_ratio: '21:9'
summary: >-
  Re-DocRED matched-recall wedge (disconfirmed) and the gold-free regime-diagnostic with its CLUTRR self-consistency blind
  spot.
figure_path: figures/fig5_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Short descriptive title for this paper generation task (roughly 30-90 characters)",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 14:36:11 UTC

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

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-06-16 14:36:17 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-06-16 14:36:17 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
