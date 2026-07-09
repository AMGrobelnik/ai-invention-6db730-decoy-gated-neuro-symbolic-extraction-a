# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 05:57:00 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-06-16 05:57:06 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

<available_resources>
<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

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

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

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

<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: >-
  Decoy-Gated Neuro-Symbolic Extraction: Executing the Label-Free FDR Diagonal, the Operational Wedge, and a Quantified Hallucination-Reduction
  on Professional Documents -- with Generator!=Scorer De-Circularization and Demonstrated Power
hypothesis: |-
  MECHANISM (unchanged, one sentence). Before any LLM-proposed Prolog FACT or fuzzy-unification BRIDGE rule enters a knowledge base, it must out-score a plausibility-matched synthetic DECOY (a candidate the model finds plausible but the document does not entail) in a target-decoy / knockoff+ competition; the gate admits the most permissive cutoff whose estimated corpus-aggregate false-admission rate (FDR) is at most a target alpha, using ZERO operation labels.

  WHAT IS NOW SETTLED (iteration-1 deliverable, reviewer-verified). The two evaluation anchors and two implementation-ready methodology specs EXIST, are schema-validated, deterministically regenerable on commodity CPU under a fixed seed, and were independently confirmed by review to match the paper exactly: (A) CLUTRR calibration anchor -- 190 examples (150 confirmatory + 40 pilot), k=2..10 hop stratification, CRISP gold from proof_state fields; (B) Re-DocRED operational anchor -- 236 documents (152 confirmatory / 36 pilot / 48 reserve), 4 balanced entity-type clusters (PER/ORG/LOC/MISC), 96 relation types, human gold with evidence spans. The pipeline, decoy/entrapment construction, scoring, gate, and the shared-triple operational comparison are specified to formulas and prompt templates. Therefore the next iteration does NOT re-plan or re-build; it EXECUTES.

  THE ONE THING THAT MATTERS NOW (the realized diagonal). The iteration-1 paper was scored below bar (3/10) for a single decisive reason: it reported NO empirical result on any central claim. The contribution of this iteration is the REALIZED numbers: (1) the calibration diagonal -- does realized FDR track target alpha on the populable CLUTRR family? (2) the operational wedge -- does decoy-gating beat a plain confidence threshold at matched recall on Re-DocRED? (3) the goal's HARD REQUIREMENT -- a quantified reduction in hallucination rate versus raw LLM generation, measured on genuine short professionally-written documents with auditable trace-graphs. All three with document-block-bootstrap CIs. Nothing secondary is reported until these land.

  THE GATE (one canonical statistic; clarity fix). For each candidate i with real score Z_i and matched-decoy score Z~_i, the competition statistic is the knockoff+ signed maximum W_i = (Z_i OR Z~_i) * sign(Z_i - Z~_i) (i.e. magnitude max(Z_i, Z~_i), sign by which won). knockoff+ thresholding scans cutoffs t and admits {i : W_i >= t} at the most permissive t whose estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha. The per-pair signed DIFFERENCE d_i = Z_i - Z~_i is used ONLY as a tail diagnostic (win-rate, CDF tests), never as the gating statistic. (Iteration-1 paper used two inconsistent W_i definitions; this iteration fixes the canonical one above.)

  VALIDITY HONESTY (rigor fix). knockoff+ delivers a FINITE-SAMPLE FDR GUARANTEE only under the joint null SIGN-FLIP property; for LLM decoys that property is UNPROVABLE, so the realized-FDR-vs-alpha diagonal IS its empirical test, not a corollary of a theorem. The document-block bootstrap supplies realized-FDP confidence intervals and a within-document-dependence DIAGNOSTIC; it does NOT restore the guarantee. We never conflate the two.

  DE-CIRCULARIZATION (methodology fix -- the deepest review concern). The review's decisive methodological objection is that the SAME LLM both generates the counterfactual decoys and scores real-vs-decoy, and that the relevant matching target is the score distribution of SPONTANEOUS false extractions, not of deliberately generated decoys. Three pre-registered moves break this:
    (a) GENERATOR != SCORER ABLATION. On a labeled slice, decoys generated by model G are scored by a DIFFERENT-FAMILY model S (and the symmetric swap). If the diagonal holds only when G=S, the control is an artifact of shared idiosyncrasy and is REPORTED AS SUCH (a localized negative result), not as confirmation.
    (b) SPONTANEOUS-ERROR CDF MATCH. Phase-0 adds a tail CDF-match test between counterfactual-decoy scores and the scores of GENUINE extractor errors (the spontaneous false admissions the gate must actually catch). A decoy family that does not reproduce the spontaneous-error tail is re-tuned or its matching gap is reported; the diagonal is only asserted on a decoy family that passes this match.
    (c) INDEPENDENT ENTRAPMENT as the non-circular corroborator. Entrapment items are built by DETERMINISTIC perturbation (in-genre cross-document swaps, numeric/temporal perturbation, explicit contradiction) -- constructed WITHOUT the generating LLM -- and provide a valid upper bound FDP_hat = N_E(1+1/r)/(N_T+N_E) that must agree with the decoy-FDR and with gold.

  DEMONSTRATED POWER (rigor fix). The review flagged that diagonal power may be marginal: certifying alpha=0.05 needs >=20 admissions (1/k floor) and the populability gate needs N_false_min=40 genuine false admissions pooled. Phase-0 MUST demonstrate both are reachable on the CLUTRR multi-hop family at the operative alpha* BEFORE the diagonal is asserted; if not, the (regenerable) CLUTRR confirmatory set is SCALED UP -- more documents and harder long-chain (large-k) splits that densify genuine errors -- until the power target is met or declared unreachable. The CERTIFIED-alpha grid is reported honestly: any alpha whose 1/k admission floor is not reached is dropped from the certified diagonal and reported as a precondition (NEVER as 'confirmed by conservatism').

  SCOPE / GOAL ALIGNMENT (scope fix). The goal targets ~3000-character professionally written legal/news/regulatory documents, upper-ontology (OpenCyc-style) grounding, and an LLM probabilistic-reasoning engine at fuzzy unifications. CLUTRR (synthetic ~355-char kinship) and Re-DocRED (Wikipedia prose) remain the CALIBRATION and STATISTICAL-OPERATIONAL anchors -- they buy crisp gold for the exact diagonal and human gold for the wedge -- but they are proxies, not the application. This iteration ADDS a genre-faithful OPERATIONAL DEMONSTRATION slice: ~15-30 genuine short professionally-written documents (legal/news/regulatory), on which we (i) ground argument types in a commodity upper-ontology slice (WordNet/ConceptNet/DBpedia-ontology standing in for OpenCyc) used ONLY for typing, (ii) run an explicit LLM probabilistic-reasoning step at fuzzy unifications, (iii) report the goal's HARD-REQUIRED quantified hallucination-reduction of decoy-gated extraction vs raw LLM generation, and (iv) export auditable trace-graphs whose leaves carry provenance + decoy + entrapment certificates. The application-faithful headline number lives here; the anchors grant it statistical validity.

  CLAIM CHAIN (each row independently testable; a break is localized and reported).
  | # | CLAIM | TEST | PASS CRITERION |
  |---|-------|------|----------------|
  | S0 | Score separation (precondition) | Phase-0: selected elicitation separates entailed vs non-entailed in the UPPER TAIL; isolated~batched agree on a labeled slice | tail-AUC>0.5 with CI; isolated~batched |
  | S1 | Decoy signature + spontaneous-error match (mechanism) | Tail-conditioned win-rate among above-cutoff matched pairs + upper-tail two-sample CDF test + decoy-vs-spontaneous-error tail CDF match | counterfactual decoys ~0.5; decoy tail ~ spontaneous-error tail; random swaps anti-conservative |
  | S2 | Calibration validity / the DIAGONAL (CLUTRR) | Sweep alpha; realized FDR vs crisp gold; document-block-bootstrap CI on the diagonal, on the populable family at demonstrated power | diagonal tracked within tau above the 1/k floor across the CERTIFIED grid |
  | S2b | Generator!=Scorer de-circularization (CLUTRR) | Re-run the diagonal with decoys from G scored by different-family S (and swap) on a labeled slice | diagonal survives G!=S, else reported as shared-model artifact |
  | S3 | Entrapment corroboration (non-circular) | Independent deterministically-built tail-matched entrapment; combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E) | bound agrees with decoy-FDR and gold |
  | S4 | Operational wedge (Re-DocRED) | Matched-recall PR + hallucinated-conclusion rate vs PLAIN CONFIDENCE-THRESHOLD gate (primary zero-label comparator), CoT, RAG, labeled Mohri-Hashimoto conformal | decoy-gating beats plain thresholding at equal zero labels; competitive with labeled conformal |
  | S4b | Application-faithful hallucination reduction (professional docs) | On ~15-30 genuine short legal/news/regulatory docs: hallucinated-fact rate of decoy-gated extraction vs raw LLM generation; trace-graphs exported | quantified reduction reported with CI; trace-graphs auditable (goal hard requirement) |
  | S5 | Document-level predictive account (Re-DocRED) | Predict per-document tail-exchangeability gap; leave-one-cluster-out + leave-one-document-out CV; pre-registered GAP-regression power analysis | out-of-sample predictive IFF >= N_min held-out units; else DESCRIPTIVE |
  | S6 | Predictable propagation (preliminary) | Tightening alpha lowers multi-hop hallucinated-conclusion rate | direction + rough magnitude |

  BUDGET (unchanged ceiling). Isolated, provenance-blinded scoring is the default for the full confirmatory set; document-prefix prompt caching keeps the ~7-15M projected tokens to ~$1-3; the added professional-doc slice and the G!=S ablation slice add a small labeled increment. Cumulative LLM cost logged after every call; HARD STOP at $10. The budget waterfall is unchanged in ORDER but its first three priorities are now the three realized numbers above (diagonal, wedge, professional-doc hallucination reduction); S5/S6/floor-relaxation/rule-gating remain leftover-only.

  SCOPE OF CLAIMS. Facts AND bridges carry the headline. CLUTRR bridges are crisp and host the diagonal + the G!=S de-circularization; Re-DocRED bridges host the operational wedge and the predictive account; the professional-doc slice hosts the application-faithful hallucination-reduction headline. Defeasible bridges, ProbLog/isotonic, TDC-SB/UB and '+1'-floor relaxation, and S6 remain preliminary / if-budget-permits.
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
  Same gate mechanism and two-anchor frame; re-pointed from build to executing the diagonal and wedge.
_confidence_delta: decrease
_key_changes:
- >-
  STATUS UPDATE: marked the two anchors and two methodology specs as BUILT and reviewer-verified; the hypothesis now starts
  from a ready, validated pipeline and mandates EXECUTION rather than further building or planning.
- >-
  PRIMARY MANDATE: re-prioritized the contribution to the three realized numbers the iteration-1 paper lacked (diagonal, operational
  wedge, and the goal's hard-required quantified hallucination-reduction vs raw LLM) -- directly answering the decisive 'no
  empirical results' critique (score 3/10).
- >-
  CIRCULARITY (review methodology-major): added a pre-registered generator!=scorer ablation (different-family scorer) and
  a decoy-vs-spontaneous-extractor-error tail-CDF match; entrapment re-framed as the non-circular, deterministically-built
  corroborator. A diagonal that needs generator=scorer is reported as a shared-model artifact.
- >-
  SCOPE (review scope-major): added a genre-faithful operational slice of ~15-30 genuine short professional legal/news/regulatory
  documents with upper-ontology typing, an LLM probabilistic-reasoning step at fuzzy unifications, and auditable trace-graphs,
  to land the goal's application-faithful hallucination-reduction headline that CLUTRR/Re-DocRED proxies cannot carry.
- >-
  POWER (review rigor-major): converted the diagonal's power analysis into a hard Phase-0 precondition (>=20 admissions and
  >=40 false admissions) with mandatory scaling of the regenerable CLUTRR confirmatory set, and an honestly reported certified-alpha
  grid (drop alphas whose 1/k floor is unreached).
- >-
  CLARITY (review clarity-minor): fixed the two inconsistent W_i definitions to one canonical knockoff+ signed-max statistic;
  reserved the per-pair signed difference for tail diagnostics only; specified figure content (the diagonal and the matched-recall
  wedge with CIs).
- >-
  RIGOR (review rigor-minor): explicitly separated the finite-sample FDR GUARANTEE (under the unprovable sign-flip property,
  tested by the diagonal) from the document-block bootstrap (realized-FDP CIs + dependence diagnostic, NOT a restored guarantee).
- >-
  NOVELTY (review novelty-minor): sharpened the boundary against conformal selection (Jin-Candes), multiple-testing hallucination
  detection (Li et al.), Mohri-Hashimoto conformal factuality, and COCOCO -- the label-free + intermediate-admission-boundary
  distinction is the novelty wedge.
relation_type: evolution
</hypothesis>

<iteration_status>
Current iteration: 2 of 10
Remaining (including this one): 9
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: >-
  Foundations: Two-Anchor Corpora and Implementation-Ready Methodology for the Label-Free Decoy-Competition FDR Gate
objective: >-
  Establish the foundational building blocks that the entire budget-waterfall depends on: (1) the two evaluation anchors standardized
  to a single shared (head, relation, tail) triple schema -- crisp-gold CLUTRR for the calibration-validity claim (S2) and
  the primary disconfirmation, and human-gold Re-DocRED for the operational-usefulness wedge (S4) and the document-level predictive
  account (S5); and (2) two implementation-ready methodology specs that lock down every design decision needed to code the
  Phase-0 pilot and the FDR gate -- the statistical control machinery plus label-free score elicitation, and the neuro-symbolic
  extraction-to-Prolog pipeline plus the fair shared operational construct and baselines. The novel contribution being built
  toward is importing target-decoy / knockoff+ FDR control to the LLM text-to-logic admission boundary as a label-free, auditable
  hallucination-control knob; this iteration makes that contribution executable.
rationale: >-
  The hypothesis mandates a strict budget waterfall whose first stage is a Phase-0 pilot that GATES all confirmatory spend.
  A pilot cannot be coded until two things exist: the labeled data slices it measures (false-admission base rate on CLUTRR,
  tail-AUC separation, S5 feature variance) and a methodology that is pinned down to formulas, estimators, prompt templates,
  elicitation shortlists, and model choices. Structurally, an EXPERIMENT must depend on at least one existing DATASET, and
  in iteration 1 there are no existing artifacts -- so experiments are impossible NOW and would have nothing to depend on.
  The highest-leverage move is therefore to build the two anchor corpora and the two methodology specs IN PARALLEL this iteration,
  so that iteration 2's Phase-0 pilot experiment can depend on both datasets and launch immediately with zero design ambiguity.
  This also de-risks the most failure-prone parts up front: whether OpenRouter models expose logprobs and prompt caching (cost
  feasibility), whether CLUTRR families can be made populable, and whether the entrapment/knockoff estimators are implemented
  exactly right. Datasets prepare raw data + gold only (no LLM scoring); all scoring, decoy/entrapment generation, and gate
  computation are deferred to experiments in later iterations, matching executor scopes.
artifact_directions:
- id: dataset_iter1_dir1
  type: dataset
  objective: >-
    Build the crisp-gold CLUTRR calibration anchor that hosts the calibration-validity diagonal (S2) and the single primary
    disconfirmation, with BOTH atomic-fact and multi-hop inferred-kinship gold plus difficulty splits, so a later experiment
    can measure populability (genuine false-admission counts at alpha*) and enrich false-reals via harder long chains.
  approach: >-
    Acquire CLUTRR (Sinha et al., EMNLP 2019; facebookresearch/clutrr generator, or a HuggingFace mirror if available -- the
    generator is rule-based/templated and needs NO LLM). For each story produce a standardized row: document text (the narrative;
    for the multi-hop family prefer longer chains and, where a single story is very short, keep the native length and record
    it -- do not pad artificially), gold ATOMIC kinship facts (relations directly stated in the text, as (head, relation,
    tail) triples), gold MULTI-HOP inferred kinship relations (the query target plus all relations derivable by composition
    over the kinship graph, the error-dense 'populable' family), the full kinship edge-graph for provenance, per-entity gender/type
    metadata, and chain length k as metadata_fold. Include harder long-chain splits (k>=4) explicitly to densify potential
    false admissions, and flag a small labeled pilot slice (a few dozen rows) for Phase-0. Target ~150 confirmatory documents
    spread across k plus the pilot slice. Map everything to the SHARED (head, relation, tail) triple schema used by both anchors,
    validate with aii-json, and split full/mini/preview. Keep total size well under 300MB.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Build the open-vocabulary, human-gold Re-DocRED operational anchor that hosts the operational-usefulness wedge (S4) and
    the document-level predictive account (S5), standardized to the SAME triple schema and partitioned into >=4 entity/topic
    clusters so cross-document feature variance exists for the S5 GAP regression.
  approach: >-
    Acquire Re-DocRED (Tan et al., EMNLP 2022, 'Revisiting DocRED'; tonytan48/Re-DocRED on GitHub or a HuggingFace mirror;
    the original DocRED is also on HF datasets). For each document produce a standardized row: full reconstructed document
    text (from the tokenized sentences, ~200 words), the annotated entity set with entity types (PER/ORG/LOC/TIME/NUM/MISC)
    and mention spans, gold (head-entity, relation, tail-entity) triples over the annotated entities across the 96 Wikidata
    relation types, evidence sentence spans per triple, relation-type and entity-type metadata, document length (word count)
    as an explicit S5 feature, and a cluster label assigned by dominant entity type / topic giving >=4 clusters as metadata_fold
    (this enables leave-one-cluster-out CV). Flag a small labeled pilot slice for Phase-0 and the S5 power analysis. Target
    ~150 confirmatory documents balanced across clusters plus the pilot slice. Assert only that gold supports RELATIVE operational
    comparisons (residual false negatives affect all systems equally). Map to the SHARED (head, relation, tail) triple schema,
    validate with aii-json, split full/mini/preview, keep under 300MB.
  depends_on: []
- id: research_iter1_dir3
  type: research
  objective: >-
    Deliver an implementation-ready specification of the FDR gate and its scalar inputs: exact knockoff+/TDC thresholding
    and the '+1' floor, the valid entrapment combined estimator, the document-block bootstrap, plausibility-matched decoy
    design, and the best label-free UPPER-TAIL score elicitation callable via OpenRouter -- so the Phase-0 pilot and CLUTRR
    calibration experiment can be coded directly without further design choices.
  approach: >-
    Web-research and synthesize into concrete formulas + pseudo-procedures: (a) knockoff+ thresholding -- the most-permissive-cutoff
    rule with estimated FDR = (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) and the 1/k minimum-estimable-FDR floor (Barber & Candes
    2015; He/Ebadi/Keich on whether the '+1' is needed, arXiv 2204.13248), and the tighter TDC-SB/UB bounds (Ebadi et al.,
    arXiv 2302.11837); (b) the valid entrapment combined UPPER bound FDP_hat = N_E(1+1/r)/(N_T+N_E) and why the naive 'sample'
    estimator is flawed (Wen et al., Nature Methods 2025, FDRBench), including how the ratio r propagates into variance and
    the achievable-alpha floor; (c) the document-block bootstrap procedure for all FDP/FDR CIs under within-document score
    dependence (resample whole documents, not candidates); (d) the null sign-flip property statement and its two LLM-specific
    anti-conservative failure modes (within-document score correlation; batched-scoring contrast effects) with the isolated-vs-batched
    discriminator logic; (e) plausibility/property-matched decoy generation -- the DeepCoy principle that decoys must reproduce
    the false-positive score distribution (not be 'too easy'), document-conditioned counterfactual construction, and non-entailment
    verification; (f) candidate UPPER-TAIL label-free elicitations -- verbalized confidence, token-logprob-derived scores,
    self-consistency, DINCO distractor-normalized confidence (arXiv 2509.25532), FactSelfCheck (arXiv 2503.17229) -- with
    reported tail-calibration behavior; (g) which sub-$0.30/M OpenRouter models expose token logprobs AND support prompt caching
    (for the document-prefix caching that makes default isolated scoring affordable), with current pricing. Output concrete
    formulas, a recommended elicitation shortlist for the pilot to test, and a short novelty-positioning note confirming no
    prior work applies knockoff/target-decoy FDR control at an LLM neuro-symbolic admission boundary.
  depends_on: []
- id: research_iter1_dir4
  type: research
  objective: >-
    Deliver an implementation-ready specification of the extraction-to-Prolog pipeline and the FAIR operational comparison:
    LLM text-to-typed-FOL extraction with over-generation, SWI-Prolog execution and auditable trace-graphs, commodity upper-ontology
    typing, the single shared claim-decomposition + relation-alignment step that maps every system into Re-DocRED triple space
    at matched recall, and the baseline comparators -- so the operational-wedge experiment can be coded directly.
  approach: >-
    Web-research and synthesize into concrete designs, prompt templates, and library choices: (a) LLM text-to-FOL/Prolog semantic
    parsing patterns from LINC (Olausson et al., EMNLP 2023) and Logic-LM (Pan et al., Findings EMNLP 2023) -- typed first-order
    FACT and fuzzy-unification BRIDGE formats, and a deliberate over-generation prompt to densify candidate false positives
    on CLUTRR; (b) SWI-Prolog integration from Python (pyswip) -- asserting admitted facts/bridges, backward-chaining multi-hop
    deduction, and exporting backward-chaining proofs as human-auditable trace-graphs whose leaves carry provenance (document
    span / ontology axiom / admitted bridge) plus slots for the decoy + entrapment certificate; (c) commodity upper-ontology
    typing standing in for OpenCyc -- using WordNet / ConceptNet / DBpedia-ontology to ground predicate ARGUMENT TYPES only
    (not for entailment), with concrete lookup recipes; (d) the FIXED shared claim-decomposition + relation-alignment procedure
    that maps neuro-symbolic admitted facts/bridges, the plain confidence-threshold gate, CoT, RAG, and labeled Mohri-Hashimoto
    conformal output identically into the common (head, Re-DocRED-relation, tail) triple space, including the per-system score-sweep
    that enforces matched recall at a common operating point; (e) the baseline recipes themselves -- standard RAG and chain-of-thought
    triple-extraction prompts, and the Mohri-Hashimoto conformal-factuality back-off (ICML 2024) as the LABELED reference
    baseline, noting its labeled-calibration requirement so the label-free wedge is positioned correctly. Output a concrete
    pipeline diagram, prompt templates, the relation-alignment mapping rules, and recommended Python libraries.
  depends_on: []
expected_outcome: >-
  After this iteration completes, the project will have: (1) a schema-validated crisp-gold CLUTRR calibration corpus (~150
  docs + labeled pilot slice) carrying both atomic-fact and multi-hop inferred-kinship gold with chain-length difficulty folds
  and long-chain enrichment, ready to host the realized-FDR-vs-alpha diagonal and the populability/false-admission measurement;
  (2) a schema-validated human-gold Re-DocRED operational corpus (~150 docs + pilot slice) over annotated entities with 96-relation
  triples, evidence spans, document-length features, and >=4 entity/topic clusters, ready to host the operational wedge and
  the S5 GAP regression -- both corpora mapped to ONE shared (head, relation, tail) triple schema; (3) an implementation-ready
  statistical-control + elicitation spec (exact knockoff+/TDC/entrapment estimators, document-block bootstrap, decoy design,
  an elicitation shortlist, and a vetted list of cheap OpenRouter models with logprob + prompt-caching support and pricing);
  and (4) an implementation-ready neuro-symbolic-pipeline + operational-comparison spec (text-to-FOL extraction, pyswip/SWI-Prolog
  trace-graphs, ontology typing, the shared relation-alignment mapping, and baseline recipes including the labeled conformal
  reference). Iteration 2 can then launch the budget-waterfall Phase-0 pilot as an EXPERIMENT depending on both datasets,
  with every design decision already settled.
summary: >-
  Iteration 1 lays the foundation for a label-free target-decoy / knockoff+ FDR gate at the LLM text-to-logic admission boundary
  by building, in parallel, the two evaluation anchors (crisp-gold CLUTRR for calibration validity; human-gold Re-DocRED for
  operational usefulness) standardized to one shared triple schema, plus two implementation-ready methodology specs (the FDR-control
  machinery with label-free score elicitation, and the neuro-symbolic extraction-to-Prolog pipeline with the fair shared operational
  construct and baselines). These four parallel artifacts unblock the budget-waterfall Phase-0 pilot in iteration 2, since
  experiments require existing dataset dependencies that do not yet exist.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
out_dependency_files:
  file_list:
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
out_dependency_files:
  file_list:
  - research_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

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
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) No empirical results are reported for any central claim. The realized-FDR-vs-alpha calibration diagonal (S2), the operational wedge of decoy-gating vs. plain thresholding at matched recall (S4), the entrapment corroboration (S3), and the goal's explicit hard requirement of a 'quantified reduction in hallucination rates compared to raw LLM generation' (S6) are all unmeasured. The paper is candid about this, but candor does not change the contribution level: at ACL/EMNLP/NeSy a paper whose headline method is unvalidated is a proposal, and these venues do not run a registered-report track. This is the dominant score blocker.
  Action: Execute the pre-registered protocol in the registered priority order (Phase-0 pilot -> CLUTRR diagonal -> Re-DocRED wedge) and report actual numbers with document-block-bootstrap CIs in the camera-ready tables. The infrastructure and budget are already sized for it; at minimum report the CLUTRR diagonal on the populable multi-hop family and the Re-DocRED wedge vs. the plain-threshold foil. Even a partial, honest result (e.g., calibrated at alpha>=0.1, untestable below) would move the paper from reject toward weak-accept.
- [MAJOR] (methodology) The load-bearing validity condition (the knockoff null sign-flip property) is unprovable for LLM decoys, and the construction is circular: the same LLM generates the counterfactual decoys AND scores both real and decoy candidates. Worse, the relevant matching target is the score distribution of spontaneous false-REAL candidates (the model's own document-anchored hallucinations), which is unknown and uncontrollable a priori, not the true-positive distribution that DeepCoy matches. There is a concrete reason to expect non-exchangeability: a model may systematically score its own document-anchored hallucinations differently from deliberately-constructed counterfactuals, biasing W signs and breaking FDR control in either direction. The paper flags 'decoys too easy -> anti-conservative' but not this asymmetry between matching false-positive vs. true-positive score distributions, nor the shared-model bias channel.
  Action: Make the S1 tail-exchangeability check (win-rate ~0.5 and the upper-tail two-sample test on false-real vs. decoy scores) a first-class, prominently reported result, not just a gating diagnostic. Add an ablation that decouples the generator and scorer (decoys generated and/or scored by a different model) to test whether shared-model bias inflates the gate. Explicitly discuss why matching the false-real (not true-positive) distribution is the crux, and treat the gate's validity as an empirically established property reported with its failure region, not an assumed one.
- [MAJOR] (scope) Scope mismatch with the stated goal and target application. The goal targets ~3000-character professionally written legal/news/regulatory documents, OpenCyc-style upper-ontology grounding, and an LLM 'probabilistic reasoning engine.' The actual anchors are ~355-character synthetic templated kinship stories (CLUTRR; I measured mean 354.9 chars, max 917) and ~200-word Wikipedia paragraphs (Re-DocRED; mean ~199 words); OpenCyc is replaced by a coarse 6-type WordNet hypernym slice {PER,LOC,ORG,TIME,NUM,MISC}; and the Prolog layer is a deterministic backward-chaining meta-interpreter, not probabilistic reasoning. The 15-document legal/news/story corpus is explicitly non-confirmatory. So the headline application genres are never quantitatively evaluated, and two named requirements (OpenCyc, probabilistic reasoning) are substituted without quantitative justification.
  Action: Either (a) add a quantitative anchor in the target genre (a small annotated legal/news set with crisp-enough gold for at least relative comparisons), or (b) reframe the scope claims to match what is evaluated (short-document kinship reasoning + document-level relation extraction). Justify the WordNet-for-OpenCyc and deterministic-for-probabilistic substitutions explicitly, and state plainly which goal requirements are descoped this iteration vs. deferred.
- [MAJOR] (rigor) Statistical power for the diagonal is not demonstrated and may be marginal. To certify alpha=0.05 the 1/k floor requires >=20 admissions, and the populability gate requires N_false_min=40 genuine false admissions pooled. With 150 confirmatory CLUTRR documents each contributing ~5 multi-hop facts (I measured mean 4.9, min 1) and acknowledged within-document dependence, the effective independent sample is small, so the document-block-bootstrap CIs may be too wide to distinguish 'tracks alpha within tau=0.05' from 'anti-conservative.' The paper itself concedes the diagonal may be declared 'untestable' -- a likely outcome that would leave the headline unproven even after the run.
  Action: Report a concrete pre-run power calculation: given expected false-admission counts, the within-document intra-class correlation, and B>=2000 block-bootstrap resamples, which alpha values can actually be demonstrated and at what CI half-width? If power is marginal, enrich the false-positive pool further (harder long-chain CLUTRR splits, more aggressive over-generation) or, where gold permits, pool the CLUTRR atomic and multi-hop families to lift the admission count above the floor for tighter alpha.
- [MINOR] (rigor) The paper risks conflating bootstrap-based inference with dependence-robust validity. Knockoff+ controls FDR in finite samples under the joint sign-flip property; the document-block bootstrap provides percentile CIs for the realized FDP but does not restore the FDR control GUARANTEE when within-document dependence violates the i.i.d.-fair-coin assumption. As written, the bootstrap is sometimes presented as if it addresses the dependence threat to validity itself.
  Action: Separate the two roles cleanly in Section 4.4/Preliminaries: (1) the block bootstrap quantifies FDP/FDR sampling variability; (2) validity under dependence is an empirical property established by the tail diagnostics and the isolated-vs-batched discriminator, not a theorem. Cite the relevant dependent-knockoff literature if you wish to claim any theoretical robustness.
- [MINOR] (novelty) The novelty claim is defensible but under-defended against the closest recent work. Reviewers will probe the boundary with conformal selection (Jin-Candes [16]), multiple-testing hallucination detection [18], COCOCO (conformal sets for neuro-symbolic concept-based models), conformal e-value novelty detection with FDR, and conformal link-prediction FDR. The current prose asserts orthogonality but does not make the distinctions crisp enough to preempt a 'this is just labeled conformal selection at the fact level' rebuttal.
  Action: Add a one-page comparison table contrasting each nearest-neighbor method on (label requirement, unit certified [final answer/claim set vs. intermediate admission/bridge], exchangeability mechanism, whether decoy-based). Explicitly position COCOCO and conformal-selection-FDR as the most adjacent and articulate the precise delta (label-free + decoy competition + admission boundary).
- [MINOR] (clarity) Two inconsistent definitions of the competition statistic W_i appear: the introduction uses W_i = score(real_i) - score(decoy_i) (a signed difference), while Preliminaries uses W_i = (Z_i v Z~_i)[2*1(Z_i>Z~_i)-1] (a signed maximum). These are mathematically distinct statistics; using them interchangeably without comment will confuse expert readers and invites doubt about which guarantee actually applies.
  Action: Choose one canonical statistic, define it once in Preliminaries, and use it consistently. If you intend to support both, state that both are valid antisymmetric knockoff statistics and specify which is used in the experiments.
- [MINOR] (clarity) Figures are referenced only as [FIGURE:figN] markers with no captions or descriptions visible in the manuscript text, so it is impossible to assess whether the planned figures would effectively communicate the (eventual) results. Given that the central evidence will be a calibration diagonal and an operational wedge, the figures are load-bearing.
  Action: Include a complete caption and a short description for each figure in the manuscript. Ensure fig for the realized-FDR-vs-alpha diagonal (with the 1/k floor and bootstrap CIs marked) and fig for the matched-recall precision/hallucination-rate comparison against all baselines are present and self-explanatory.
- [MINOR] (evidence) The baseline suite is well chosen on paper (plain confidence-threshold gate, CoT, RAG, labeled Mohri-Hashimoto conformal factuality) but none has been run, and the 'matched-recall' comparison hinges on a single fixed claim-decomposition + relation-alignment step (MiniLM top-8 shortlist -> temp-0 LLM pick among 96 codes). That alignment step is itself an LLM component that could inject errors uniformly across systems and confound the wedge.
  Action: When running S4, report the alignment step's own error rate (e.g., on a labeled slice) and verify the wedge survives reasonable alignment-error sensitivity. Show the plain-threshold foil and conformal reference at the matched operating point with CIs so the 'decoy-gating beats thresholding' claim is isolated from alignment noise.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 7 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


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
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Short name for this strategy",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 05:57:06 UTC

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

### [4] ASSISTANT · 2026-06-16 06:01:20 UTC

```
I'll analyze the situation and design the strategy. The dominant reviewer blocker is crystal clear: **no empirical results**. Iteration 1 built all the infrastructure (2 datasets, 2 methodology specs, all reviewer-verified). This iteration must EXECUTE and report real numbers, while addressing the methodology-circularity, scope-mismatch, and power MAJORs.

Let me verify the existing artifacts are in place before finalizing dependency references.
```

### [5] TOOL CALL — Bash · 2026-06-16 06:01:20 UTC

```
Verify existing artifact outputs and check user uploads:
echo "=== CLUTRR dataset ===" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/ 2>/dev/null | head -20
echo "=== Re-DocRED dataset ===" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/ 2>/dev/null | head -20
echo "=== FDR spec ===" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_1/ 2>/dev/null | head -20
echo "=== pipeline spec ===" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_2/ 2>/dev/null | head -20
echo "=== user uploads ===" && ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads/ 2>/dev/null | head -20
```

### [6] TOOL RESULT — Bash · 2026-06-16 06:01:20 UTC

```
{"stdout": "=== CLUTRR dataset ===\ntotal 11779\ndrwxr-xr-x 6 root root 2015607 Jun 16 05:19 .\ndrwxr-xr-x 6 root root 2041260 Jun 16 04:52 ..\n-rw-r--r-- 1 root root 1777974 Jun 16 05:20 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4579 Jun 16 05:19 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 4 root root 2000317 Jun 16 05:09 .venv\n-rw-r--r-- 1 root root   20349 Jun 16 05:17 data.py\ndrwxr-xr-x 2 root root       1 Jun 16 04:57 data_out\n-rw-r--r-- 1 root root 1096458 Jun 16 05:18 full_data_out.json\ndrwxr-xr-x 2 root root 1000864 Jun 16 05:15 logs\n-rw-r--r-- 1 root root   28906 Jun 16 05:18 mini_data_out.json\n-rw-r--r-- 1 root root    8214 Jun 16 05:18 preview_data_out.json\n-rw-r--r-- 1 root root     452 Jun 16 05:18 pyproject.toml\ndrwxr-xr-x 4 root root 2015004 Jun 16 04:59 temp\n-rw-r--r-- 1 root root   41411 Jun 16 05:18 uv.lock\n-rw-r--r-- 1 root root    6884 Jun 16 05:17 verify_dataset.py\n=== Re-DocRED dataset ===\ntotal 21710\ndrwxr-xr-x 5 root root  2025457 Jun 16 05:14 .\ndrwxr-xr-x 6 root root  2041260 Jun 16 04:52 ..\n-rw-r--r-- 1 root root  1126142 Jun 16 05:14 .repl_agent.ptylog\n-rw-r--r-- 1 root root     3819 Jun 16 05:14 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 4 root root  2021811 Jun 16 05:00 .venv\n-rw-r--r-- 1 root root    28626 Jun 16 05:12 data.py\n-rw-r--r-- 1 root root     2350 Jun 16 05:12 dataset_meta.json\n-rw-r--r-- 1 root root      777 Jun 16 05:12 entity_type_schema.json\n-rw-r--r-- 1 root root 11748737 Jun 16 05:13 full_data_out.json\ndrwxr-xr-x 2 root root  1001145 Jun 16 05:08 logs\n-rw-r--r-- 1 root root   100691 Jun 16 05:13 mini_data_out.json\n-rw-r--r-- 1 root root    23020 Jun 16 05:13 preview_data_out.json\n-rw-r--r-- 1 root root      434 Jun 16 05:11 pyproject.toml\n-rw-r--r-- 1 root root    20970 Jun 16 05:12 relation_schema.json\n-rw-r--r-- 1 root root     6398 Jun 16 05:12 row_schema.json\ndrwxr-xr-x 3 root root  2002391 Jun 16 04:55 temp\n-rw-r--r-- 1 root root    73906 Jun 16 05:12 uv.lock\n=== FDR spec ===\ntotal 5140\ndrwxr-xr-x 2 root root 2000116 Jun 16 05:12 .\ndrwxr-xr-x 6 root root 2041260 Jun 16 04:52 ..\n-rw-r--r-- 1 root root 1067558 Jun 16 05:12 .repl_agent.ptylog\n-rw-r--r-- 1 root root   51824 Jun 16 05:11 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root   51505 Jun 16 05:11 research_out.json\n-rw-r--r-- 1 root root   49282 Jun 16 05:12 research_report.md\n=== pipeline spec ===\ntotal 3865\ndrwxr-xr-x 2 root root 1081394 Jun 16 05:08 .\ndrwxr-xr-x 6 root root 2041260 Jun 16 04:52 ..\n-rw-r--r-- 1 root root  772666 Jun 16 05:08 .repl_agent.ptylog\n-rw-r--r-- 1 root root   21160 Jun 16 05:08 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root   19923 Jun 16 05:06 research_out.json\n-rw-r--r-- 1 root root   19728 Jun 16 05:08 research_report.md\n=== user uploads ===\ntotal 1998\ndrwxr-xr-x  2 root root       1 Jun 16 03:05 .\ndrwxr-xr-x 14 root root 2044446 Jun 16 04:40 ..", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] ASSISTANT · 2026-06-16 06:03:17 UTC

```
All four iteration-1 artifacts are present and complete (CLUTRR dataset, Re-DocRED dataset, FDR-gate spec, pipeline spec). User uploads is empty. I have everything needed to finalize the strategy.

My analysis is clear: iteration 1 built and validated all infrastructure but scored 3/10 for **zero empirical results**. This iteration must EXECUTE. I'll design a focused 5-artifact strategy that produces the three realized numbers (diagonal, wedge, de-circularization) while addressing every reviewer MAJOR.
```

### [8] TOOL CALL — Write · 2026-06-16 06:03:17 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Execute the Realized Numbers: CLUTRR Diagonal, Re-DocRED Wedge, and the Generator!=Scorer De-Circularization for the Label-Free Decoy-Competition FDR Gate",
      "objective": "Convert iteration-1's prepared-and-validated infrastructure into the three realized empirical numbers the prior paper lacked (the single decisive 3/10 blocker): (1) the CLUTRR calibration diagonal -- does realized corpus-aggregate FDR track target alpha on the populable multi-hop family, with a demonstrated pre-run power analysis and document-block-bootstrap CIs; (2) the Re-DocRED operational wedge -- does decoy-gating beat a plain confidence threshold (and CoT/RAG/labeled-conformal) at matched recall on atomic-fact precision and hallucinated-conclusion rate; and (3) a prominently-reported decoy-mechanism validation with a generator!=scorer de-circularization ablation and a decoy-vs-spontaneous-error tail-CDF match that directly tests the reviewer's deepest methodological objection. In parallel we build the genre-faithful professional-document application anchor (legal/news/regulatory ~3000-char docs with gold) and a novelty/upper-ontology/probabilistic-reasoning specification, so the scope-mismatch MAJOR is closed structurally this iteration and quantitatively next. The novel contribution realized here is the FIRST empirical demonstration of label-free knockoff+/target-decoy FDR control at the LLM text-to-logic admission boundary, with its validity region honestly mapped.",
      "rationale": "The reviewer feedback is unambiguous: the dominant score blocker is that NO central claim was measured (S2 diagonal, S4 wedge, S3 entrapment, S6 hallucination-reduction all unrun), and ACL/EMNLP/NeSy do not run a registered-report track. Iteration 1 already delivered exactly what makes execution possible NOW: two schema-validated anchors (crisp-gold CLUTRR art_XZyKy6QuwxrO; human-gold Re-DocRED art_Jcudmkugg1qT) and two implementation-ready specs (the FDR-gate+elicitation spec art_SLUbUUr6Ul98 with the recommended sub-$0.30/M model, knockoff+/entrapment/bootstrap formulas, and the canonical statistic; the pipeline+operational-comparison spec art_K6AE23HoGqe6 with prompt templates, the shared relation-alignment step, and baseline recipes). Because experiments require an existing DATASET dependency and the anchors exist, the highest-leverage move is three focused, parallel, self-contained EXPERIMENTS that each run their own pilot internally and report numbers -- directly killing the empirical-results MAJOR. The de-circularization experiment is split out and elevated to a first-class result because it answers the methodology MAJOR (same LLM generates and scores; the right matching target is the SPONTANEOUS false-real distribution, not the true-positive distribution; shared-model bias can break exchangeability either direction). The power MAJOR is answered by a concrete pre-run power calculation folded into the diagonal experiment (which alpha values clear the 1/k floor at what CI half-width, with mandatory enrichment/pooling if marginal). The scope MAJOR is answered by building the professional-doc anchor now (the application experiment runs next iteration on it) plus a research spec that justifies the OpenCyc and probabilistic-reasoning substitutions and supplies the novelty comparison table (novelty MINOR). All five artifacts run in parallel and share the $10 cap, so each experiment carries an explicit conservative soft cap and logs cumulative cost after every call; the spec's ~$1-3 projection for both confirmatory anchors leaves comfortable margin.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Produce the HEADLINE calibration diagonal (realized FDR vs target alpha) and execute the single pre-registered primary disconfirmation on crisp-gold CLUTRR, accompanied by an explicit pre-run statistical power analysis (answering the power MAJOR) and independent entrapment corroboration (S0 + S2 + S3 + power).",
          "approach": "Implement the end-to-end gate exactly per the two specs [art_SLUbUUr6Ul98, art_K6AE23HoGqe6]. STAGE A (Phase-0 pilot, on the 40-example disjoint pilot slice): (i) select the label-free elicitation by tail-AUC with a bootstrap CI among the spec's shortlist -- verbalized confidence (floor), DINCO-style distractor-normalized, self-consistency/SelfCheckGPT, and a logprob yes/no-token score IF the model exposes non-null logprobs -- requiring tail-AUC>0.5 in the upper (admission) tail; confirm isolated~batched agreement on the labeled slice. (ii) Measure POPULABILITY: the count of GENUINE false admissions (vs crisp CLUTRR gold) among atomic-fact vs multi-hop-inferred-kinship proposals at the operative alpha*; pre-register the disconfirmation on whichever family reaches N_false_min=40 pooled (default expectation: multi-hop), enriching the false-real pool via extractor over-generation (T=0.7, n=3 samples unioned, cap 20 candidates/doc) and the dataset's harder long-chain k>=4 splits; if still marginal, POOL the atomic+multi-hop families to lift the admission count above the floor for tighter alpha (per the reviewer's suggestion), reporting the pooled-vs-separate sensitivity. (iii) Compute and REPORT the pre-run power calculation: given the measured false-admission rate, the within-document intra-class correlation, and B>=2000 document-block (cluster) bootstrap resamples, state which alpha in {0.05,0.10,0.20,0.30,0.50} clear the 1/k admission floor {20,10,5,4,2} and at what CI half-width; scale the regenerable CLUTRR confirmatory set (re-run data.py with more docs / harder splits) until the power target is met or declared unreachable. STAGE B (confirmatory diagonal): extraction over-generation -> document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination rate, sweep the rejection threshold) -> ISOLATED provenance-blinded order-randomized scoring with document-prefix prompt caching -> knockoff+ gate using the CANONICAL competition statistic W_i = (Z_i v Z~_i)*sign(Z_i - Z~_i) (signed magnitude-max; the per-pair difference d_i = Z_i - Z~_i is reserved as a TAIL DIAGNOSTIC ONLY, never the gating statistic -- fixing the iteration-1 inconsistency) with admission threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for facts and bridges; sweep alpha and compute realized corpus-aggregate FDR vs crisp gold with document-block-bootstrap percentile CIs -- this IS the diagonal. Keep random type-matched swaps as the predicted-anti-conservative negative control. STAGE C (entrapment): build deterministically-constructed tail-matched entrapment WITHOUT the generating LLM (in-genre cross-document kinship swaps, numeric/temporal perturbation, explicit contradiction) at ratio r=1, compute the valid combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), and check agreement with the decoy-FDR and gold; attach a per-entrapment tail-difficulty diagnostic. Report the CERTIFIED-alpha grid honestly (drop any alpha whose 1/k floor is unreached, labeling it a precondition, NEVER 'confirmed by conservatism'); evaluate the primary disconfirmation at alpha* with tolerance tau=0.05. Cleanly SEPARATE the two roles of the bootstrap (it quantifies FDP/FDR sampling variability) from validity-under-dependence (an empirical property established by the tail diagnostics + isolated-vs-batched discriminator), per the rigor MINOR. Use the spec's recommended openai/gpt-4.1-nano (logprobs+auto-caching, <$0.30/M); gradual scaling mini->full per aii-long-running-tasks; log cumulative LLM cost after EVERY call; soft cap ~$3 for this experiment, HARD STOP at $10. Output method_out.json with: the alpha-vs-realized-FDR diagonal arrays (figure-ready, with 1/k floor and CI bands marked), the power-analysis table, entrapment numbers, populability counts per family, and the disconfirmation verdict.",
          "depends_on": [
            {"id": "art_XZyKy6QuwxrO", "label": "dataset"},
            {"id": "art_SLUbUUr6Ul98", "label": "methodology"},
            {"id": "art_K6AE23HoGqe6", "label": "pipeline"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Elevate the S1 tail-exchangeability check and the generator!=scorer de-circularization to first-class, prominently-reported empirical results that directly test the reviewer's deepest methodological objection: whether the gate's calibration is an artifact of a SINGLE LLM both generating decoys and scoring, and whether the decoys reproduce the SPONTANEOUS false-real score distribution (the right matching target) rather than the true-positive distribution.",
          "approach": "Operate on a labeled CLUTRR slice (the 40-example pilot plus a bounded confirmatory subset, to cap cost) using crisp gold to define known-false reals. (1) DECOY SIGNATURE (S1): construct matched (false-real, counterfactual-decoy) pairs; report the tail-conditioned win-rate among pairs scoring ABOVE the operative admission cutoff (target ~0.5), and a one-sided upper-tail two-sample CDF test (KS and tail-restricted Mann-Whitney) on real-false vs counterfactual-decoy scores restricted to the admission region; include random type-matched swaps as the predicted measurably-anti-conservative control to validate the diagnostic's sensitivity. (2) SPONTANEOUS-ERROR TAIL MATCH (the crux the reviewer named): collect the scores of GENUINE extractor errors -- spontaneous false reals identified vs crisp gold -- and run a tail CDF-match test between counterfactual-decoy scores and these spontaneous-error scores; explicitly report the matching GAP and discuss why matching the false-real (not true-positive) distribution is the load-bearing requirement; assert the decoy family as valid only if it passes this match, else report the gap and re-tune. (3) GENERATOR!=SCORER ABLATION (S2b, de-circularization): re-run the win-rate / CDF tests and a small labeled-slice diagonal with decoys generated by model G but scored by a DIFFERENT-FAMILY model S via OpenRouter (e.g., G=an OpenAI-family nano model, S=a cheap Llama/Qwen/Mistral-family model), plus the symmetric swap; if exchangeability and the diagonal hold ONLY when G=S, report this as a localized shared-model artifact (a reported negative result), not as confirmation. Use the canonical W_i; compute all CIs by document-block bootstrap (B>=2000); apply a Benjamini-Hochberg multiplicity correction across the family of validation tests. Keep all scoring isolated and provenance-blinded. Use cheap sub-$0.30/M models with caching; gradual scaling; log cumulative cost after EVERY call; soft cap ~$1.5 for this experiment, HARD STOP at $10. Output method_out.json with the tail-exchangeability tables, the decoy-vs-spontaneous-error match (figure-ready CDFs), and the G==S vs G!=S verdict with its validity-region statement.",
          "depends_on": [
            {"id": "art_XZyKy6QuwxrO", "label": "dataset"},
            {"id": "art_SLUbUUr6Ul98", "label": "methodology"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Produce the OPERATIONAL WEDGE on Re-DocRED: at matched recall, does decoy-gating beat the plain confidence-threshold gate (primary zero-label foil) on atomic-fact precision and hallucinated-conclusion rate, and stay competitive with labeled conformal -- with all baselines on the shared triple schema and an explicit alignment-error sensitivity check (S4 + evidence MINOR).",
          "approach": "Per the pipeline spec [art_K6AE23HoGqe6], implement the single fixed claim-decomposition + relation-alignment step (MiniLM top-8 relation shortlist -> temperature-0 LLM pick among the 96 Wikidata P-codes or NO_RELATION, with the three-tier entity-linking exact/alias/embedding procedure) that maps EVERY system's raw output identically into the (head-entity, P-code, tail-entity) triple space, scored by the official (title, r, h_idx, t_idx) matching metric against Re-DocRED human gold. SYSTEMS compared at a common operating point (recall matched by sweeping each system's own score): (a) decoy-gating (the method), (b) the PLAIN confidence-threshold gate -- identical elicitation, NO decoy/competition/entrapment (the load-bearing primary zero-label foil), (c) chain-of-thought extraction, (d) RAG (BM25 retrieval), (e) labeled Mohri-Hashimoto conformal back-off (the labeled reference, with its calibration-label cost charged symmetrically against our zero labels). At the matched-recall point report precision, the hallucinated-conclusion rate (fraction of multi-hop derived conclusions whose triple is not entailed by gold), and PR curves, all with document-block-bootstrap CIs (B>=2000). CRITICAL CONFOUND CHECK (evidence MINOR): measure the relation-alignment step's OWN error rate on a labeled slice and verify the wedge survives reasonable alignment-error perturbation (re-run the comparison under injected alignment noise / an alternative alignment threshold), so 'decoy-gating beats thresholding' is isolated from alignment noise that hits all systems uniformly. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally; no absolute FDR diagonal here -- that belongs to CLUTRR). Pre-register the operational disconfirmation: if decoy-gating shows no precision/hallucination advantage over the plain threshold at matched recall, the wedge collapses to 'thresholding is enough' and is reported as disconfirmed. Use the spec's cheap model + document-prefix caching; gradual scaling mini->full; log cumulative cost after EVERY call; soft cap ~$3 for this experiment, HARD STOP at $10. Output method_out.json with figure-ready matched-recall PR arrays and hallucination-rate bars per system with CIs, plus the alignment-error rate and its sensitivity result.",
          "depends_on": [
            {"id": "art_Jcudmkugg1qT", "label": "dataset"},
            {"id": "art_K6AE23HoGqe6", "label": "pipeline"},
            {"id": "art_SLUbUUr6Ul98", "label": "methodology"}
          ]
        },
        {
          "type": "dataset",
          "objective": "Build the genre-faithful APPLICATION anchor the scope MAJOR demands: ~15-30 genuine short professionally-written legal/news/regulatory documents (~1500-3000 characters, the goal's target length) standardized to the shared (head, relation, tail) triple schema with trustworthy gold atomic facts, entity typing for upper-ontology grounding, and provenance spans -- so next iteration can run the application-faithful hallucination-reduction experiment (decoy-gated extraction vs raw LLM generation) and export auditable trace-graphs on the genres the goal actually targets.",
          "approach": "Source REAL professional documents with reliable gold, strongly preferring freely-available human-annotated information-extraction corpora so the gold is crisp-enough for the RELATIVE hallucination comparison: legal (e.g., CUAD contract-clause annotations, EUR-Lex provisions, court-opinion syllabi/holdings, ContractNLI), news/newswire (e.g., a relation- or event-annotated newswire set such as a freely-licensed slice of relation-extraction or event corpora; avoid LDC-restricted ACE unless an open mirror exists), and regulatory (e.g., eCFR or GDPR article snippets paired with structured summaries). Select ~15-30 documents in the ~1500-3000 char range, balanced across the three genres, with native length preserved (never padded). For each document produce a standardized row mapping to the SAME shared triple schema used by the CLUTRR and Re-DocRED anchors: input = {doc_id, document_text, genre, source, char_length, entities[{name, type, char_span}]}; output = {gold_atomic_facts[{head, relation, tail, provenance_char_span}]}; metadata_* = coarse upper-ontology entity types (PER/ORG/LOC/TIME/NUM/MISC, with finer ontology classes where the source provides them), a gold_quality flag distinguishing CRISP human-annotated gold from documented SILVER curated gold, license, and the genre fold. Where a document has no pre-existing annotation, apply a documented high-rigor curation protocol (deterministic extraction from structured companion data, or careful manual-style curation with explicit cross-checks) and label the result silver, recording the limitation transparently. Do NOT run any LLM scoring, decoy generation, FDR, or Prolog here (those are the next-iteration application experiment's job, which will depend on THIS dataset). Validate every row with aii-json against a row schema; split full/mini/preview; keep total size well under 300MB; ensure deterministic regeneration from cached raw sources under a fixed seed. Record citations, URLs, licenses, and per-genre counts in a dataset_meta.json companion.",
          "depends_on": [
            {"id": "art_K6AE23HoGqe6", "label": "schema-guidance"}
          ]
        },
        {
          "type": "research",
          "objective": "Close three remaining reviewer gaps with one focused specification: (a) a crisp NOVELTY comparison table preempting the 'this is just labeled conformal selection at the fact level' rebuttal (novelty MINOR), (b) a concrete REAL upper-ontology grounding recipe with explicit justification of any commodity substitute (scope MAJOR -- the OpenCyc substitution), and (c) a concrete LLM-as-PROBABILISTIC-reasoning-engine design at fuzzy unifications (scope MAJOR -- the deterministic-for-probabilistic substitution, and the goal's named 'probabilistic reasoning engine' requirement).",
          "approach": "Web-research (aii-web-tools: search -> fetch -> fetch_grep) and synthesize into research_out.json + research_report.md. (a) NOVELTY TABLE: build a one-page table contrasting decoy-gated extraction against its nearest neighbors -- conformal selection (Jin-Candes), multiple-testing hallucination detection (Li/Magesh/Veeravalli), COCOCO (conformal sets for neuro-symbolic concept-based models), conformal e-value novelty detection with FDR control, conformal link-prediction FDR, and Mohri-Hashimoto conformal factuality -- across the dimensions {label requirement (labeled vs label-free), unit certified (final answer / claim set vs INTERMEDIATE admission/bridge), exchangeability mechanism, decoy/competition-based?, controls FDR vs coverage}; state the precise delta in one sentence (label-free + decoy competition + neural-to-symbolic admission boundary). (b) UPPER-ONTOLOGY GROUNDING: survey the real options for OpenCyc-style taxonomic grounding -- OpenCyc/ResearchCyc current availability and access route, SUMO, DBpedia/YAGO ontology classes, Wikidata class hierarchy, WordNet hypernyms -- and specify ONE concrete argument-typing recipe with library/API; explicitly justify the commodity substitute by stating what taxonomic grounding is LOST relative to OpenCyc and why typing-only usage (constraining decoy generation and entity linking, never filtering) suffices, and which goal requirement is descoped vs deferred. (c) PROBABILISTIC REASONING ENGINE: specify a concrete LLM-as-probabilistic-reasoner design at the fuzzy-unification boundary -- e.g., ProbLog (the problog Python package) or a fuzzy-unification layer where the LLM supplies calibrated unification/bridge probabilities that feed probabilistic inference, with the exact API, how the decoy-competition certificate (W_i, T, alpha) and entrapment certificate map onto the probabilistic weights, and how probabilistic trace-graphs are produced -- justifying the iteration-1 deterministic backward-chaining substitution and giving the implementable upgrade path. Output concrete tables, recipes, library choices, and a short source-traceable positioning note.",
          "depends_on": [
            {"id": "art_SLUbUUr6Ul98", "label": "extends"},
            {"id": "art_K6AE23HoGqe6", "label": "extends"}
          ]
        }
      ],
      "expected_outcome": "After this iteration the project will hold its FIRST empirical results on every central claim, directly dissolving the dominant 3/10 'no results' blocker: (1) a realized CLUTRR calibration diagonal (alpha vs realized FDR) on the populable multi-hop family with document-block-bootstrap CIs, a reported certified-alpha grid, an explicit pre-run power calculation stating which alphas are demonstrable at what CI half-width, entrapment corroboration, and a definite primary-disconfirmation verdict (confirmed / disconfirmed / untestable-at-this-difficulty -- each interpretable); (2) a prominently-reported decoy-mechanism validation -- tail-conditioned win-rate, upper-tail CDF tests, the decoy-vs-spontaneous-error tail match, and the generator!=scorer ablation -- that establishes (or bounds) the gate's empirical validity region and answers the circularity MAJOR head-on; (3) a Re-DocRED operational wedge with matched-recall PR curves and hallucinated-conclusion rates for decoy-gating vs the plain-threshold foil, CoT, RAG, and labeled conformal, plus the alignment-step error rate isolating the wedge from alignment noise; (4) a schema-validated professional-document anchor (~15-30 genuine legal/news/regulatory ~3000-char docs with gold) that closes the scope gap structurally and unblocks next iteration's application-faithful hallucination-reduction experiment; and (5) a novelty comparison table plus justified specifications for real upper-ontology grounding and an LLM probabilistic-reasoning engine, answering the novelty and substitution objections. Together these turn the iteration-1 proposal into an empirically-grounded paper, with the canonical W_i statistic, the bootstrap-vs-validity separation, and figure-ready diagonal/wedge arrays all in hand for the rewrite. Total LLM spend held well under the $10 cap by conservative per-experiment soft caps and cumulative cost logging.",
      "summary": "Execute, don't re-plan. Three parallel, self-contained EXPERIMENTS on the existing validated anchors deliver the three realized numbers the prior paper lacked -- the CLUTRR calibration diagonal with a demonstrated power analysis (S0/S2/S3 + power), the Re-DocRED operational wedge vs the plain-threshold foil at matched recall with an alignment-error check (S4), and a first-class decoy-mechanism validation with a generator!=scorer de-circularization and a decoy-vs-spontaneous-error tail match (S1/S2b) -- directly answering the empirical-results, methodology-circularity, and power MAJORs. In parallel, a DATASET builds the genre-faithful professional-document application anchor and a RESEARCH spec supplies the novelty comparison table and the justified OpenCyc / probabilistic-reasoning substitutions, closing the scope and novelty objections. All five run concurrently, depend only on iteration-1 artifacts, use the canonical knockoff+ statistic and document-block-bootstrap CIs, and share the $10 cap under conservative per-experiment soft caps."
    }
  ]
}
```

### [9] TOOL RESULT — Write · 2026-06-16 06:03:17 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Execute the Realized Numbers: CLUTRR Diagonal, Re-DocRED Wedge, and the Generator!=Scorer De-Circularization for the Label-Free Decoy-Competition FDR Gate\",\n      \"objective\": \"Convert iteration-1's prepared-and-validated infrastructure into the three realized empirical numbers the prior paper lacked (the single decisive 3/10 blocker): (1) the CLUTRR calibration diagonal -- does realized corpus-aggregate FDR track target alpha on the populable multi-hop family, with a demonstrated pre-run power analysis and document-block-bootstrap CIs; (2) the Re-DocRED operational wedge -- does decoy-gating beat a plain confidence threshold (and CoT/RAG/labeled-conformal) at matched recall on atomic-fact precision and hallucinated-conclusion rate; and (3) a prominently-reported decoy-mechanism validation with a generator!=scorer de-circularization ablation and a decoy-vs-spontaneous-error tail-CDF match that directly tests the reviewer's deepest methodological objection. In parallel we build the genre-faithful professional-document application anchor (legal/news/regulatory ~3000-char docs with gold) and a novelty/upper-ontology/probabilistic-reasoning specification, so the scope-mismatch MAJOR is closed structurally this iteration and quantitatively next. The novel contribution realized here is the FIRST empirical demonstration of label-free knockoff+/target-decoy FDR control at the LLM text-to-logic admission boundary, with its validity region honestly mapped.\",\n      \"rationale\": \"The reviewer feedback is unambiguous: the dominant score blocker is that NO central claim was measured (S2 diagonal, S4 wedge, S3 entrapment, S6 hallucination-reduction all unrun), and ACL/EMNLP/NeSy do not run a registered-report track. Iteration 1 already delivered exactly what makes execution possible NOW: two schema-validated anchors (crisp-gold CLUTRR art_XZyKy6QuwxrO; human-gold Re-DocRED art_Jcudmkugg1qT) and two implementation-ready specs (the FDR-gate+elicitation spec art_SLUbUUr6Ul98 with the recommended sub-$0.30/M model, knockoff+/entrapment/bootstrap formulas, and the canonical statistic; the pipeline+operational-comparison spec art_K6AE23HoGqe6 with prompt templates, the shared relation-alignment step, and baseline recipes). Because experiments require an existing DATASET dependency and the anchors exist, the highest-leverage move is three focused, parallel, self-contained EXPERIMENTS that each run their own pilot internally and report numbers -- directly killing the empirical-results MAJOR. The de-circularization experiment is split out and elevated to a first-class result because it answers the methodology MAJOR (same LLM generates and scores; the right matching target is the SPONTANEOUS false-real distribution, not the true-positive distribution; shared-model bias can break exchangeability either direction). The power MAJOR is answered by a concrete pre-run power calculation folded into the diagonal experiment (which alpha values clear the 1/k floor at what CI half-width, with mandatory enrichment/pooling if marginal). The scope MAJOR is answered by building the professional-doc anchor now (the application experiment runs next iteration on it) plus a research spec that justifies the OpenCyc and probabilistic-reasoning substitutions and supplies the novelty comparison table (novelty MINOR). All five artifacts run in parallel and share the $10 cap, so each experiment carries an explicit conservative soft cap and logs cumulative cost after every call; the spec's ~$1-3 projection for both confirmatory anchors leaves comfortable margin.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Produce the HEADLINE calibration diagonal (realized FDR vs target alpha) and execute the single pre-registered primary disconfirmation on crisp-gold CLUTRR, accompanied by an explicit pre-run statistical power analysis (answering the power MAJOR) and independent entrapment corroboration (S0 + S2 + S3 + power).\",\n          \"approach\": \"Implement the end-to-end gate exactly per the two specs [art_SLUbUUr6Ul98, art_K6AE23HoGqe6]. STAGE A (Phase-0 pilot, on the 40-example disjoint pilot slice): (i) select the label-free elicitation by tail-AUC with a bootstrap CI among the spec's shortlist -- verbalized confidence (floor), DINCO-style distractor-normalized, self-consistency/SelfCheckGPT, and a logprob yes/no-token score IF the model exposes non-null logprobs -- requiring tail-AUC>0.5 in the upper (admission) tail; confirm isolated~batched agreement on the labeled slice. (ii) Measure POPULABILITY: the count of GENUINE false admissions (vs crisp CLUTRR gold) among atomic-fact vs multi-hop-inferred-kinship proposals at the operative alpha*; pre-register the disconfirmation on whichever family reaches N_false_min=40 pooled (default expectation: multi-hop), enriching the false-real pool via extractor over-generation (T=0.7, n=3 samples unioned, cap 20 candidates/doc) and the dataset's harder long-chain k>=4 splits; if still marginal, POOL the atomic+multi-hop families to lift the admission count above the floor for tighter alpha (per the reviewer's suggestion), reporting the pooled-vs-separate sensitivity. (iii) Compute and REPORT the pre-run power calculation: given the measured false-admission rate, the within-document intra-class correlation, and B>=2000 document-block (cluster) bootstrap resamples, state which alpha in {0.05,0.10,0.20,0.30,0.50} clear the 1/k admission floor {20,10,5,4,2} and at what CI half-width; scale the regenerable CLUTRR confirmatory set (re-run data.py with more docs / harder splits) until the power target is met or declared unreachable. STAGE B (confirmatory diagonal): extraction over-generation -> document-conditioned counterfactual decoys with an isolated non-entailment check (log contamination rate, sweep the rejection threshold) -> ISOLATED provenance-blinded order-randomized scoring with document-prefix prompt caching -> knockoff+ gate using the CANONICAL competition statistic W_i = (Z_i v Z~_i)*sign(Z_i - Z~_i) (signed magnitude-max; the per-pair difference d_i = Z_i - Z~_i is reserved as a TAIL DIAGNOSTIC ONLY, never the gating statistic -- fixing the iteration-1 inconsistency) with admission threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha}, separately for facts and bridges; sweep alpha and compute realized corpus-aggregate FDR vs crisp gold with document-block-bootstrap percentile CIs -- this IS the diagonal. Keep random type-matched swaps as the predicted-anti-conservative negative control. STAGE C (entrapment): build deterministically-constructed tail-matched entrapment WITHOUT the generating LLM (in-genre cross-document kinship swaps, numeric/temporal perturbation, explicit contradiction) at ratio r=1, compute the valid combined bound FDP_hat=N_E(1+1/r)/(N_T+N_E), and check agreement with the decoy-FDR and gold; attach a per-entrapment tail-difficulty diagnostic. Report the CERTIFIED-alpha grid honestly (drop any alpha whose 1/k floor is unreached, labeling it a precondition, NEVER 'confirmed by conservatism'); evaluate the primary disconfirmation at alpha* with tolerance tau=0.05. Cleanly SEPARATE the two roles of the bootstrap (it quantifies FDP/FDR sampling variability) from validity-under-dependence (an empirical property established by the tail diagnostics + isolated-vs-batched discriminator), per the rigor MINOR. Use the spec's recommended openai/gpt-4.1-nano (logprobs+auto-caching, <$0.30/M); gradual scaling mini->full per aii-long-running-tasks; log cumulative LLM cost after EVERY call; soft cap ~$3 for this experiment, HARD STOP at $10. Output method_out.json with: the alpha-vs-realized-FDR diagonal arrays (figure-ready, with 1/k floor and CI bands marked), the power-analysis table, entrapment numbers, populability counts per family, and the disconfirmation verdict.\",\n          \"depends_on\": [\n            {\"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\"},\n            {\"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\"},\n            {\"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Elevate the S1 tail-exchangeability check and the generator!=scorer de-circularization to first-class, prominently-reported empirical results that directly test the reviewer's deepest methodological objection: whether the gate's calibration is an artifact of a SINGLE LLM both generating decoys and scoring, and whether the decoys reproduce the SPONTANEOUS false-real score distribution (the right matching target) rather than the true-positive distribution.\",\n          \"approach\": \"Operate on a labeled CLUTRR slice (the 40-example pilot plus a bounded confirmatory subset, to cap cost) using crisp gold to define known-false reals. (1) DECOY SIGNATURE (S1): construct matched (false-real, counterfactual-decoy) pairs; report the tail-conditioned win-rate among pairs scoring ABOVE the operative admission cutoff (target ~0.5), and a one-sided upper-tail two-sample CDF test (KS and tail-restricted Mann-Whitney) on real-false vs counterfactual-decoy scores restricted to the admission region; include random type-matched swaps as the predicted measurably-anti-conservative control to validate the diagnostic's sensitivity. (2) SPONTANEOUS-ERROR TAIL MATCH (the crux the reviewer named): collect the scores of GENUINE extractor errors -- spontaneous false reals identified vs crisp gold -- and run a tail CDF-match test between counterfactual-decoy scores and these spontaneous-error scores; explicitly report the matching GAP and discuss why matching the false-real (not true-positive) distribution is the load-bearing requirement; assert the decoy family as valid only if it passes this match, else report the gap and re-tune. (3) GENERATOR!=SCORER ABLATION (S2b, de-circularization): re-run the win-rate / CDF tests and a small labeled-slice diagonal with decoys generated by model G but scored by a DIFFERENT-FAMILY model S via OpenRouter (e.g., G=an OpenAI-family nano model, S=a cheap Llama/Qwen/Mistral-family model), plus the symmetric swap; if exchangeability and the diagonal hold ONLY when G=S, report this as a localized shared-model artifact (a reported negative result), not as confirmation. Use the canonical W_i; compute all CIs by document-block bootstrap (B>=2000); apply a Benjamini-Hochberg multiplicity correction across the family of validation tests. Keep all scoring isolated and provenance-blinded. Use cheap sub-$0.30/M models with caching; gradual scaling; log cumulative cost after EVERY call; soft cap ~$1.5 for this experiment, HARD STOP at $10. Output method_out.json with the tail-exchangeability tables, the decoy-vs-spontaneous-error match (figure-ready CDFs), and the G==S vs G!=S verdict with its validity-region statement.\",\n          \"depends_on\": [\n            {\"id\": \"art_XZyKy6QuwxrO\", \"label\": \"dataset\"},\n            {\"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Produce the OPERATIONAL WEDGE on Re-DocRED: at matched recall, does decoy-gating beat the plain confidence-threshold gate (primary zero-label foil) on atomic-fact precision and hallucinated-conclusion rate, and stay competitive with labeled conformal -- with all baselines on the shared triple schema and an explicit alignment-error sensitivity check (S4 + evidence MINOR).\",\n          \"approach\": \"Per the pipeline spec [art_K6AE23HoGqe6], implement the single fixed claim-decomposition + relation-alignment step (MiniLM top-8 relation shortlist -> temperature-0 LLM pick among the 96 Wikidata P-codes or NO_RELATION, with the three-tier entity-linking exact/alias/embedding procedure) that maps EVERY system's raw output identically into the (head-entity, P-code, tail-entity) triple space, scored by the official (title, r, h_idx, t_idx) matching metric against Re-DocRED human gold. SYSTEMS compared at a common operating point (recall matched by sweeping each system's own score): (a) decoy-gating (the method), (b) the PLAIN confidence-threshold gate -- identical elicitation, NO decoy/competition/entrapment (the load-bearing primary zero-label foil), (c) chain-of-thought extraction, (d) RAG (BM25 retrieval), (e) labeled Mohri-Hashimoto conformal back-off (the labeled reference, with its calibration-label cost charged symmetrically against our zero labels). At the matched-recall point report precision, the hallucinated-conclusion rate (fraction of multi-hop derived conclusions whose triple is not entailed by gold), and PR curves, all with document-block-bootstrap CIs (B>=2000). CRITICAL CONFOUND CHECK (evidence MINOR): measure the relation-alignment step's OWN error rate on a labeled slice and verify the wedge survives reasonable alignment-error perturbation (re-run the comparison under injected alignment noise / an alternative alignment threshold), so 'decoy-gating beats thresholding' is isolated from alignment noise that hits all systems uniformly. Assert ONLY relative comparisons (Re-DocRED residual false negatives affect all systems equally; no absolute FDR diagonal here -- that belongs to CLUTRR). Pre-register the operational disconfirmation: if decoy-gating shows no precision/hallucination advantage over the plain threshold at matched recall, the wedge collapses to 'thresholding is enough' and is reported as disconfirmed. Use the spec's cheap model + document-prefix caching; gradual scaling mini->full; log cumulative cost after EVERY call; soft cap ~$3 for this experiment, HARD STOP at $10. Output method_out.json with figure-ready matched-recall PR arrays and hallucination-rate bars per system with CIs, plus the alignment-error rate and its sensitivity result.\",\n          \"depends_on\": [\n            {\"id\": \"art_Jcudmkugg1qT\", \"label\": \"dataset\"},\n            {\"id\": \"art_K6AE23HoGqe6\", \"label\": \"pipeline\"},\n            {\"id\": \"art_SLUbUUr6Ul98\", \"label\": \"methodology\"}\n          ]\n        },\n        {\n          \"type\": \"dataset\",\n          \"objective\": \"Build the genre-faithful APPLICATION anchor the scope MAJOR demands: ~15-30 genuine short professionally-written legal/news/regulatory documents (~1500-3000 characters, the goal's target length) standardized to the shared (head, relation, tail) triple schema with trustworthy gold atomic facts, entity typing for upper-ontology grounding, and provenance spans -- so next iteration can run the application-faithful hallucination-reduction experiment (decoy-gated extraction vs raw LLM generation) and export auditable trace-graphs on the genres the goal actually targets.\",\n          \"approach\": \"Source REAL professional documents with reliable gold, strongly preferring freely-available human-annotated information-extraction corpora so the gold is crisp-enough for the RELATIVE hallucination comparison: legal (e.g., CUAD contract-clause annotations, EUR-Lex provisions, court-opinion syllabi/holdings, ContractNLI), news/newswire (e.g., a relation- or event-annotated newswire set such as a freely-licensed slice of relation-extraction or event corpora; avoid LDC-restricted ACE unless an open mirror exists), and regulatory (e.g., eCFR or GDPR article snippets paired with structured summaries). Select ~15-30 documents in the ~1500-3000 char range, balanced across the three genres, with native length preserved (never padded). For each document produce a standardized row mapping to the SAME shared triple schema used by the CLUTRR and Re-DocRED anchors: input = {doc_id, document_text, genre, source, char_length, entities[{name, type, char_span}]}; output = {gold_atomic_facts[{head, relation, tail, provenance_char_span}]}; metadata_* = coarse upper-ontology entity types (PER/ORG/LOC/TIME/NUM/MISC, with finer ontology classes where the source provides them), a gold_quality flag distinguishing CRISP human-annotated gold from documented SILVER curated gold, license, and the genre fold. Where a document has no pre-existing annotation, apply a documented high-rigor curation protocol (deterministic extraction from structured companion data, or careful manual-style curation with explicit cross-checks) and label the result silver, recording the limitation transparently. Do NOT run any LLM scoring, decoy generation, FDR, or Prolog here (those are the next-iteration application experiment's job, which will depend on THIS dataset). Validate every row with aii-json against a row schema; split full/mini/preview; keep total size well under 300MB; ensure deterministic regeneration from cached raw sources under a fixed seed. Record citations, URLs, licenses, and per-genre counts in a dataset_meta.json companion.\",\n          \"depends_on\": [\n            {\"id\": \"art_K6AE23HoGqe6\", \"label\": \"schema-guidance\"}\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Close three remaining reviewer gaps with one focused specification: (a) a crisp NOVELTY comparison table preempting the 'this is just labeled conformal selection at the fact level' rebuttal (novelty MINOR), (b) a concrete REAL upper-ontology grounding recipe with explicit justification of any commodity substitute (scope MAJOR -- the OpenCyc substitution), and (c) a concrete LLM-as-PROBABILISTIC-reasoning-engine design at fuzzy unifications (scope MAJOR -- the deterministic-for-probabilistic substitution, and the goal's named 'probabilistic reasoning engine' requirement).\",\n          \"approach\": \"Web-research (aii-web-tools: search -> fetch -> fetch_grep) and synthesize into research_out.json + research_report.md. (a) NOVELTY TABLE: build a one-page table contrasting decoy-gated extraction against its nearest neighbors -- conformal selection (Jin-Candes), multiple-testing hallucination detection (Li/Magesh/Veeravalli), COCOCO (conformal sets for neuro-symbolic concept-based models), conformal e-value novelty detection with FDR control, conformal link-prediction FDR, and Mohri-Hashimoto conformal factuality -- across the dimensions {label requirement (labeled vs label-free), unit certified (final answer / claim set vs INTERMEDIATE admission/bridge), exchangeability mechanism, decoy/competition-based?, controls FDR vs coverage}; state the precise delta in one sentence (label-free + decoy competition + neural-to-symbolic admission boundary). (b) UPPER-ONTOLOGY GROUNDING: survey the real options for OpenCyc-style taxonomic grounding -- OpenCyc/ResearchCyc current availability and access route, SUMO, DBpedia/YAGO ontology classes, Wikidata class hierarchy, WordNet hypernyms -- and specify ONE concrete argument-typing recipe with library/API; explicitly justify the commodity substitute by stating what taxonomic grounding is LOST relative to OpenCyc and why typing-only usage (constraining decoy generation and entity linking, never filtering) suffices, and which goal requirement is descoped vs deferred. (c) PROBABILISTIC REASONING ENGINE: specify a concrete LLM-as-probabilistic-reasoner design at the fuzzy-unification boundary -- e.g., ProbLog (the problog Python package) or a fuzzy-unification layer where the LLM supplies calibrated unification/bridge probabilities that feed probabilistic inference, with the exact API, how the decoy-competition certificate (W_i, T, alpha) and entrapment certificate map onto the probabilistic weights, and how probabilistic trace-graphs are produced -- justifying the iteration-1 deterministic backward-chaining substitution and giving the implementable upgrade path. Output concrete tables, recipes, library choices, and a short source-traceable positioning note.\",\n          \"depends_on\": [\n            {\"id\": \"art_SLUbUUr6Ul98\", \"label\": \"extends\"},\n            {\"id\": \"art_K6AE23HoGqe6\", \"label\": \"extends\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"After this iteration the project will hold its FIRST empirical results on every central claim, directly dissolving the dominant 3/10 'no results' blocker: (1) a realized CLUTRR calibration diagonal (alpha vs realized FDR) on the populable multi-hop family with document-block-bootstrap CIs, a reported certified-alpha grid, an explicit pre-run power calculation stating which alphas are demonstrable at what CI half-width, entrapment corroboration, and a definite primary-disconfirmation verdict (confirmed / disconfirmed / untestable-at-this-difficulty -- each interpretable); (2) a prominently-reported decoy-mechanism validation -- tail-conditioned win-rate, upper-tail CDF tests, the decoy-vs-spontaneous-error tail match, and the generator!=scorer ablation -- that establishes (or bounds) the gate's empirical validity region and answers the circularity MAJOR head-on; (3) a Re-DocRED operational wedge with matched-recall PR curves and hallucinated-conclusion rates for decoy-gating vs the plain-threshold foil, CoT, RAG, and labeled conformal, plus the alignment-step error rate isolating the wedge from alignment noise; (4) a schema-validated professional-document anchor (~15-30 genuine legal/news/regulatory ~3000-char docs with gold) that closes the scope gap structurally and unblocks next iteration's application-faithful hallucination-reduction experiment; and (5) a novelty comparison table plus justified specifications for real upper-ontology grounding and an LLM probabilistic-reasoning engine, answering the novelty and substitution objections. Together these turn the iteration-1 proposal into an empirically-grounded paper, with the canonical W_i statistic, the bootstrap-vs-validity separation, and figure-ready diagonal/wedge arrays all in hand for the rewrite. Total LLM spend held well under the $10 cap by conservative per-experiment soft caps and cumulative cost logging.\",\n      \"summary\": \"Execute, don't re-plan. Three parallel, self-contained EXPERIMENTS on the existing validated anchors deliver the three realized numbers the prior paper lacked -- the CLUTRR calibration diagonal with a demonstrated power analysis (S0/S2/S3 + power), the Re-DocRED operational wedge vs the plain-threshold foil at matched recall with an alignment-error check (S4), and a first-class decoy-mechanism validation with a generator!=scorer de-circularization and a decoy-vs-spontaneous-error tail match (S1/S2b) -- directly answering the empirical-results, methodology-circularity, and power MAJORs. In parallel, a DATASET builds the genre-faithful professional-document application anchor and a RESEARCH spec supplies the novelty comparison table and the justified OpenCyc / probabilistic-reasoning substitutions, closing the scope and novelty objections. All five run concurrently, depend only on iteration-1 artifacts, use the canonical knockoff+ statistic and document-block-bootstrap CIs, and share the $10 cap under conservative per-experiment soft caps.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [10] ASSISTANT · 2026-06-16 06:03:23 UTC

```
Let me validate the JSON is well-formed.
```

### [11] TOOL CALL — Bash · 2026-06-16 06:03:23 UTC

```
Validate strategy JSON structure and dependencies:
python3 -c "
import json
p='/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json'
d=json.load(open(p))
s=d['strategies']
print('strategies:', len(s))
st=s[0]
print('keys:', sorted(st.keys()))
ads=st['artifact_directions']
print('artifact_directions:', len(ads))
for i,a in enumerate(ads):
    deps=[(x['id'],x['label']) for x in a.get('depends_on',[])]
    print(f'  [{i}] {a[\"type\"]:11s} deps={deps}')
print('VALID JSON, all checks pass')
"
```

### [12] TOOL RESULT — Bash · 2026-06-16 06:03:23 UTC

```
{"stdout": "strategies: 1\nkeys: ['artifact_directions', 'expected_outcome', 'objective', 'rationale', 'summary', 'title']\nartifact_directions: 5\n  [0] experiment  deps=[('art_XZyKy6QuwxrO', 'dataset'), ('art_SLUbUUr6Ul98', 'methodology'), ('art_K6AE23HoGqe6', 'pipeline')]\n  [1] experiment  deps=[('art_XZyKy6QuwxrO', 'dataset'), ('art_SLUbUUr6Ul98', 'methodology')]\n  [2] experiment  deps=[('art_Jcudmkugg1qT', 'dataset'), ('art_K6AE23HoGqe6', 'pipeline'), ('art_SLUbUUr6Ul98', 'methodology')]\n  [3] dataset     deps=[('art_K6AE23HoGqe6', 'schema-guidance')]\n  [4] research    deps=[('art_SLUbUUr6Ul98', 'extends'), ('art_K6AE23HoGqe6', 'extends')]\nVALID JSON, all checks pass", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] ASSISTANT · 2026-06-16 06:03:27 UTC

```
The strategy is written and validated. Let me record a brief continuity note in memory, since the iteration progression is genuine project state not derivable from code or git.
```

### [14] TOOL CALL — Read · 2026-06-16 06:03:27 UTC

```
/root/.claude/projects/-ai-inventor/memory/project_drim_invloop_iter1.md
```

### [15] TOOL RESULT — Read · 2026-06-16 06:03:27 UTC

```
{"type": "text", "file": {"filePath": "/root/.claude/projects/-ai-inventor/memory/project_drim_invloop_iter1.md", "content": "---\nname: project_drim_invloop_iter1\ndescription: run_MQN7mBg4AhvH invention-loop iter1 outcome + upd_hypo evolution mandate for iter2\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 82aeb028-c33b-4f87-aacf-63f1c6f1d482\n---\n\nRun run_MQN7mBg4AhvH, 3_invention_loop/iter_1 (the decoy-gated / knockoff+ label-free FDR gate at the LLM text-to-logic admission boundary — see [[project_knockoff_gated_neurosymbolic]] and [[project_clutrr_crispgold_anchor]]).\n\n**Iter-1 outcome:** strategy was \"Foundations only\" → built + reviewer-verified two anchors (190-doc crisp-gold CLUTRR, 236-doc Re-DocRED/96 relations) + two methodology specs, but ran NO experiment. review_paper scored the paper **3/10** solely because every central claim is unmeasured. Four major critiques: (1) no empirics, (2) circularity — same LLM generates AND scores decoys, (3) scope mismatch — anchors aren't the goal's ~3000-char professional legal/news docs + OpenCyc + LLM reasoner, (4) unproven statistical power for the diagonal.\n\n**upd_hypo deliverable** (`.terminal_claude_agent_struct_out.json`, built via `build_updated_hypo.py`): evolution hypothesis re-pointed from \"build+pre-register\" to **EXECUTE**. Mandates iter-2 produce 3 realized numbers (CLUTRR diagonal, Re-DocRED wedge vs plain threshold, quantified hallucination-reduction vs raw LLM on a NEW ~15-30 professional-doc slice). Folds the 4 critiques into pre-registered tests: generator≠scorer ablation + decoy-vs-spontaneous-error tail-CDF match (de-circularization); demonstrated-power precondition (≥20 admissions, ≥40 false admissions, scale regenerable CLUTRR set) before asserting the diagonal; one canonical knockoff+ signed-max W_i.\n\n**Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.\n", "numLines": 17, "startLine": 1, "totalLines": 17}}
```

### [16] TOOL CALL — Edit · 2026-06-16 06:03:41 UTC

```
File: /root/.claude/projects/-ai-inventor/memory/project_drim_invloop_iter1.md
OLD: **Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.
NEW: **Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.

**Iter-2 GEN_STRAT (gen_strat_1, 5 artifacts, all parallel, depend only on iter-1 artifacts):** EXECUTE strategy. (1) EXPERIMENT CLUTRR diagonal — S0 pilot + S2 diagonal + S3 entrapment + explicit pre-run power calc (which alphas clear the 1/k floor at what CI half-width; enrich/pool families if marginal); primary disconfirmation at alpha*, tau=0.05; canonical W_i=(Z∨Z̃)·sign(Z−Z̃). (2) EXPERIMENT decoy-mechanism validation — first-class S1 tail win-rate/CDF + decoy-vs-spontaneous-error tail match + generator≠scorer (G≠S, swap) ablation on labeled slice (answers circularity MAJOR). (3) EXPERIMENT Re-DocRED wedge — decoy-gating vs plain-threshold foil/CoT/RAG/labeled-conformal at matched recall + alignment-error sensitivity. (4) DATASET professional-doc anchor (~15-30 legal/news/regulatory ~3000-char docs w/ gold) — sets up next-iter application experiment (scope MAJOR). (5) RESEARCH novelty table + OpenCyc-substitute justification + LLM-probabilistic-reasoning (ProbLog) design. Per-experiment soft caps ($3/$1.5/$3) under shared $10 cap; model openai/gpt-4.1-nano + prompt caching.
```

### [17] TOOL RESULT — Edit · 2026-06-16 06:03:41 UTC

```
{"filePath": "/root/.claude/projects/-ai-inventor/memory/project_drim_invloop_iter1.md", "oldString": "**Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.", "newString": "**Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.\n\n**Iter-2 GEN_STRAT (gen_strat_1, 5 artifacts, all parallel, depend only on iter-1 artifacts):** EXECUTE strategy. (1) EXPERIMENT CLUTRR diagonal — S0 pilot + S2 diagonal + S3 entrapment + explicit pre-run power calc (which alphas clear the 1/k floor at what CI half-width; enrich/pool families if marginal); primary disconfirmation at alpha*, tau=0.05; canonical W_i=(Z∨Z̃)·sign(Z−Z̃). (2) EXPERIMENT decoy-mechanism validation — first-class S1 tail win-rate/CDF + decoy-vs-spontaneous-error tail match + generator≠scorer (G≠S, swap) ablation on labeled slice (answers circularity MAJOR). (3) EXPERIMENT Re-DocRED wedge — decoy-gating vs plain-threshold foil/CoT/RAG/labeled-conformal at matched recall + alignment-error sensitivity. (4) DATASET professional-doc anchor (~15-30 legal/news/regulatory ~3000-char docs w/ gold) — sets up next-iter application experiment (scope MAJOR). (5) RESEARCH novelty table + OpenCyc-substitute justification + LLM-probabilistic-reasoning (ProbLog) design. Per-experiment soft caps ($3/$1.5/$3) under shared $10 cap; model openai/gpt-4.1-nano + prompt caching.", "originalFile": "---\nname: project_drim_invloop_iter1\ndescription: run_MQN7mBg4AhvH invention-loop iter1 outcome + upd_hypo evolution mandate for iter2\nmetadata: \n  node_type: memory\n  type: project\n  originSessionId: 82aeb028-c33b-4f87-aacf-63f1c6f1d482\n---\n\nRun run_MQN7mBg4AhvH, 3_invention_loop/iter_1 (the decoy-gated / knockoff+ label-free FDR gate at the LLM text-to-logic admission boundary — see [[project_knockoff_gated_neurosymbolic]] and [[project_clutrr_crispgold_anchor]]).\n\n**Iter-1 outcome:** strategy was \"Foundations only\" → built + reviewer-verified two anchors (190-doc crisp-gold CLUTRR, 236-doc Re-DocRED/96 relations) + two methodology specs, but ran NO experiment. review_paper scored the paper **3/10** solely because every central claim is unmeasured. Four major critiques: (1) no empirics, (2) circularity — same LLM generates AND scores decoys, (3) scope mismatch — anchors aren't the goal's ~3000-char professional legal/news docs + OpenCyc + LLM reasoner, (4) unproven statistical power for the diagonal.\n\n**upd_hypo deliverable** (`.terminal_claude_agent_struct_out.json`, built via `build_updated_hypo.py`): evolution hypothesis re-pointed from \"build+pre-register\" to **EXECUTE**. Mandates iter-2 produce 3 realized numbers (CLUTRR diagonal, Re-DocRED wedge vs plain threshold, quantified hallucination-reduction vs raw LLM on a NEW ~15-30 professional-doc slice). Folds the 4 critiques into pre-registered tests: generator≠scorer ablation + decoy-vs-spontaneous-error tail-CDF match (de-circularization); demonstrated-power precondition (≥20 admissions, ≥40 false admissions, scale regenerable CLUTRR set) before asserting the diagonal; one canonical knockoff+ signed-max W_i.\n\n**Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.\n", "structuredPatch": [{"oldStart": 14, "oldLines": 3, "newStart": 14, "newLines": 5, "lines": [" **upd_hypo deliverable** (`.terminal_claude_agent_struct_out.json`, built via `build_updated_hypo.py`): evolution hypothesis re-pointed from \"build+pre-register\" to **EXECUTE**. Mandates iter-2 produce 3 realized numbers (CLUTRR diagonal, Re-DocRED wedge vs plain threshold, quantified hallucination-reduction vs raw LLM on a NEW ~15-30 professional-doc slice). Folds the 4 critiques into pre-registered tests: generator≠scorer ablation + decoy-vs-spontaneous-error tail-CDF match (de-circularization); demonstrated-power precondition (≥20 admissions, ≥40 false admissions, scale regenerable CLUTRR set) before asserting the diagonal; one canonical knockoff+ signed-max W_i.", " ", " **Why:** documents where this run stands so a later session doesn't re-derive it. **How to apply:** if iter-2 work appears, the hypothesis already commits to execution + the 4 fixes; don't re-plan infrastructure — it exists and is validated.", "+", "+**Iter-2 GEN_STRAT (gen_strat_1, 5 artifacts, all parallel, depend only on iter-1 artifacts):** EXECUTE strategy. (1) EXPERIMENT CLUTRR diagonal — S0 pilot + S2 diagonal + S3 entrapment + explicit pre-run power calc (which alphas clear the 1/k floor at what CI half-width; enrich/pool families if marginal); primary disconfirmation at alpha*, tau=0.05; canonical W_i=(Z∨Z̃)·sign(Z−Z̃). (2) EXPERIMENT decoy-mechanism validation — first-class S1 tail win-rate/CDF + decoy-vs-spontaneous-error tail match + generator≠scorer (G≠S, swap) ablation on labeled slice (answers circularity MAJOR). (3) EXPERIMENT Re-DocRED wedge — decoy-gating vs plain-threshold foil/CoT/RAG/labeled-conformal at matched recall + alignment-error sensitivity. (4) DATASET professional-doc anchor (~15-30 legal/news/regulatory ~3000-char docs w/ gold) — sets up next-iter application experiment (scope MAJOR). (5) RESEARCH novelty table + OpenCyc-substitute justification + LLM-probabilistic-reasoning (ProbLog) design. Per-experiment soft caps ($3/$1.5/$3) under shared $10 cap; model openai/gpt-4.1-nano + prompt caching."]}], "userModified": false, "replaceAll": false}
```

### [18] ASSISTANT · 2026-06-16 06:03:56 UTC

```
Done. The strategy is written, validated, and the continuity note is updated.

## Summary

I generated **1 focused strategy with 5 artifacts** for iteration 2. The diagnosis was unambiguous: iteration 1 built and reviewer-verified all infrastructure (2 datasets, 2 specs) but scored **3/10 for one decisive reason — zero empirical results**. So this strategy is **EXECUTE, not re-plan**, and every artifact maps to a specific reviewer MAJOR.

**The 5 artifacts (all parallel, depending only on iteration-1 artifacts):**

1. **EXPERIMENT — CLUTRR diagonal** (core headline): Phase-0 pilot + realized-FDR-vs-α diagonal + entrapment + an explicit **pre-run power calculation** (which α clear the 1/k floor, at what CI half-width, with family enrichment/pooling if marginal). Answers the *evidence* and *power* MAJORs. Uses the canonical knockoff+ signed-max W_i (fixes the clarity inconsistency).

2. **EXPERIMENT — Decoy-mechanism validation + de-circularization**: elevates the tail-exchangeability check to a first-class result, adds the **decoy-vs-spontaneous-error tail-CDF match** (the reviewer's exact crux) and the **generator≠scorer ablation**. Answers the *methodology* MAJOR.

3. **EXPERIMENT — Re-DocRED operational wedge**: decoy-gating vs the plain-threshold foil / CoT / RAG / labeled conformal at matched recall, plus an **alignment-error sensitivity check** to isolate the wedge. Answers the *evidence* MAJOR + alignment MINOR.

4. **DATASET — Professional-document anchor** (~15–30 genuine ~3000-char legal/news/regulatory docs with gold): closes the *scope* MAJOR structurally now; unblocks next iteration's application-faithful hallucination-reduction experiment.

5. **RESEARCH — Novelty table + OpenCyc-substitute justification + LLM-probabilistic-reasoning (ProbLog) design**: answers the *novelty* MINOR and the *scope* substitution objections.

**Key design decisions:**
- Three independent experiments (not one mega-run) for robustness and to keep each within its 6h budget — duplicated setup is bounded to cheap LLM-slice cost.
- Shared $10 cap handled by conservative per-experiment soft caps ($3/$1.5/$3 ≈ $7.5, with margin), cumulative cost logging, and gradual scaling.
- The professional-doc **experiment** is deferred to next iteration because parallel-execution rules forbid an experiment depending on a dataset created the same iteration — so the dataset is built now.

JSON validated (5 directions, correct dependency IDs/labels) and written to `.terminal_claude_agent_struct_out.json`.
```
