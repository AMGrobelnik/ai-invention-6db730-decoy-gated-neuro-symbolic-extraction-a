# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 06:13:51 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

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

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

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

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<context>
<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
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
out_dependency_files:
  file_list:
  - research_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>
</context>

<artifact_plan>
id: gen_plan_research_1_idx5
type: research
title: >-
  Research Plan: Novelty-Delta Table, Real Upper-Ontology Grounding Recipe, and the LLM-as-Probabilistic-Reasoner Design at
  Fuzzy Unifications
summary: >-
  A step-by-step web-research plan that closes three reviewer gaps for the decoy-gated neuro-symbolic extraction hypothesis:
  (A) a crisp NOVELTY comparison table preempting the 'this is just labeled conformal selection at the fact level' rebuttal,
  with the one-sentence delta; (B) a concrete REAL upper-ontology argument-typing recipe (with library/API) plus an explicit
  justification of the OpenCyc commodity substitution (what taxonomic grounding is lost, why typing-only usage suffices, what
  is descoped vs deferred); and (C) a concrete LLM-as-probabilistic-reasoning-engine design at the fuzzy-unification boundary
  (ProbLog / fuzzy-unification layer), mapping the decoy-competition + entrapment certificates onto probabilistic weights,
  producing probabilistic trace-graphs, and giving the implementable upgrade path from iteration-1's deterministic backward-chaining.
  Pure web research; output is research_out.json + research_report.md with source-traceable tables, recipes, and a positioning
  note.
runpod_compute_profile: cpu_light
question: >-
  What is the precise, source-traceable novelty delta of label-free decoy-gated text-to-logic admission versus its nearest
  conformal/FDR neighbors; what is a concrete, implementable REAL upper-ontology argument-typing recipe (and how is the OpenCyc
  commodity substitution honestly justified — loss, sufficiency, descope-vs-defer); and how should an LLM act as a probabilistic
  reasoning engine at fuzzy unifications (ProbLog or fuzzy-unification layer) such that the decoy/entrapment certificates
  become probabilistic weights and the proof exports as an auditable probabilistic trace-graph?
research_plan: |-
  GOAL & DELIVERABLE. Produce research_out.json (fields: title, summary, answer [long markdown], sources [{index,url,title,summary}], follow_up_questions) and a mirrored research_report.md. The `answer` must contain three self-contained sections — PART A (novelty table + one-sentence delta), PART B (upper-ontology grounding recipe + OpenCyc-substitution justification), PART C (LLM-as-probabilistic-reasoner design + certificate->weight mapping + probabilistic trace-graphs + upgrade path) — each with concrete tables, named libraries/APIs/versions, and [n] citations to primary sources. This is PURE WEB RESEARCH: no code execution, no downloads. Use the aii-web-tools skill: web search -> web fetch (understand) -> fetch_grep (extract exact claims/numbers/equations). Maximize parallel calls for independent lookups.

  === STEP 0 — PRE-FLIGHT: READ DEPENDENCIES, DO NOT DUPLICATE (do first) ===
  Read the two dependency specs to inherit terminology and avoid re-deriving settled material:
    - /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json (Spec A: the FDR gate — gives knockoff+ statistic W_i=(Z_i v Z~_i)*sign(Z_i-Z~_i), threshold T=min{t:(1+#{W<=-t})/(#{W>=t} v 1)<=alpha}, entrapment FDP_hat=N_E(1+1/r)/(N_T+N_E), the certificate fields cert(W_i,T,q/alpha,FDP_hat,r), DINCO/FactSelfCheck elicitation, model openai/gpt-4.1-nano, and a Section-H novelty note that ALREADY contrasts Mohri-Hashimoto / Jin-Candes / coherent factuality. PART A EXTENDS that note into a full table; do not contradict it.)
    - /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_research_2/research_out.json (Spec B: the pipeline — gives the janus-swi deterministic solve/2 meta-interpreter, the trace-graph JSON/Graphviz-DOT format with provenance+decoy+entrapment leaves, the WordNet-hypernym coarse typing into {PER,LOC,ORG,TIME,NUM,MISC}, and the shared Re-DocRED triple comparison. PART B EXTENDS the typing block; PART C EXTENDS the deterministic meta-interpreter into a probabilistic engine. Reuse exact symbol names and the certificate schema so the new design is drop-in compatible.)
  State in the report which prior claims you build on so reviewers see continuity, not churn.

  === PART A — THE NOVELTY DELTA TABLE (reviewer: novelty MINOR) ===
  Objective: a one-page table that makes the rebuttal 'this is just labeled conformal selection at the fact level' impossible, by pinning each nearest neighbor on the dimensions where our method differs.
  A1. Fetch and fetch_grep each nearest-neighbor primary source; extract VERBATIM (quote + arXiv ID) the four facts per row: (1) label requirement — does it need a labeled/annotated calibration or reference set? (2) unit certified — final answer / emitted claim set / predicted link / OUTPUT, vs an INTERMEDIATE admission/bridge into a downstream symbolic layer; (3) exchangeability mechanism — conformal exchangeability of labeled calibration vs test, graphon exchangeability, or engineered decoy sign-flip; (4) is it decoy/competition-based? (5) does it control FDR or COVERAGE (or mFDR/bFDR)? Confirmed targets and URLs (verify each, do not trust snippets):
    - Jin & Candes, Conformal Selection / Selection by Prediction with Conformal p-values, JMLR 2023 — https://arxiv.org/pdf/2210.01408 (labeled calibration; FDR via BH on conformal p-values; certifies selected candidates; exchangeability of labeled calib/test; NOT decoy).
    - Li, Magesh & Veeravalli, Principled Detection of Hallucinations via Multiple Testing — https://arxiv.org/abs/2508.18473 (labeled small calibration set of non-hallucinated prompts; conformal p-values + BH/BY; controls false-alarm rate at PROMPT/generation level; NOT decoy).
    - COCOCO — Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models — https://arxiv.org/abs/2605.18202 (conformal prediction SETS over concepts+labels; distribution-free COVERAGE not FDR; labeled calibration; post-hoc deduction-abduction revision; certifies concept/label sets = OUTPUT of a NeSy concept model; NOT decoy. This is the closest 'neuro-symbolic + conformal' neighbor — position carefully: it conformalizes the concept-bottleneck OUTPUT under fixed logical constraints, we gate the text->logic ADMISSION boundary label-free).
    - Conformal novelty detection with FDR control via conformal e-values — https://arxiv.org/abs/2302.07294 (derandomized; FDR via conformal e-values + e-BH; needs an inlier/reference set = labeled-ish; certifies which TEST points are novel; exchangeability conformal; NOT decoy). Optionally note follow-ons https://arxiv.org/abs/2501.02703 (full-conformal e-values) and https://arxiv.org/abs/2601.02610 (bFDR at the boundary) as the active frontier.
    - Conformal link prediction with FDR control — https://arxiv.org/abs/2306.14693 (Marandon; wrapper turning any link predictor into FDR-controlling; conformal p-values; needs observed-edge calibration) and https://arxiv.org/abs/2404.02542 (FDR control + FDP bounds) and https://arxiv.org/abs/2507.07025 (e-value aggregation under dependence). These certify PREDICTED KG LINKS (output), labeled/observed-graph exchangeability, NOT decoy.
    - Mohri & Hashimoto, Conformal Factuality — https://arxiv.org/abs/2402.10978 (labeled calibration; back-off removes sub-claims; certifies emitted OUTPUT; controls factuality/coverage; NOT decoy) — reuse the dep-A summary, add the row.
  A2. Build the table with EXACTLY the column set from the artifact direction: {label requirement (labeled vs label-free), unit certified (final answer/claim set vs INTERMEDIATE admission/bridge), exchangeability mechanism, decoy/competition-based?, controls FDR vs coverage}. Add a final OURS row asserting: label-free | certifies the INTERMEDIATE text->logic admission of facts/bridges | engineered+empirically-tested decoy sign-flip (knockoff+/TDC) corroborated by independent entrapment | YES decoy-competition | controls FDR. Mark every cell with a [n] citation.
  A3. Write the precise one-sentence delta verbatim for the paper: e.g., 'Unlike all conformal selection/factuality/novelty/link methods — which require a LABELED calibration or reference set and certify a model OUTPUT (answer, claim set, predicted link, or concept set) under conformal/graphon exchangeability — ours is the first LABEL-FREE, DECOY-COMPETITION FDR knob that gates the INTERMEDIATE neural-to-symbolic admission boundary, with exchangeability engineered and empirically tested in the tail rather than assumed from labeled data.' Also write a 2-3 sentence rebuttal paragraph specifically defusing 'just conformal selection at the fact level': name that conformal selection (Jin-Candes) needs labeled outcomes and certifies selected outputs, whereas we have zero operation labels and place the gate before symbolic propagation.
  A4. Run 2-3 confirmatory adversarial searches to ensure no 2025-2026 preprint already does label-free decoy/knockoff FDR at an LLM text->logic boundary (queries: 'knockoff filter LLM hallucination admission', 'target-decoy competition language model fact extraction FDR', 'label-free FDR neuro-symbolic knowledge base admission'). Report the result honestly; if a near-collision appears, add it as a row and sharpen the delta.

  === PART B — REAL UPPER-ONTOLOGY GROUNDING RECIPE + OPENCYC-SUBSTITUTION JUSTIFICATION (reviewer: scope MAJOR) ===
  Objective: survey the REAL options for OpenCyc-style taxonomic grounding, specify ONE concrete argument-typing recipe with library/API, and justify the commodity substitute (loss, sufficiency, descope vs defer). The goal text explicitly names 'OpenCyc to supply necessary background structure and taxonomic grounding,' so the substitution must be argued, not glossed.
  B1. ESTABLISH OPENCYC STATUS & ACCESS (verify, cite): OpenCyc distribution discontinued early 2017 (Cycorp ceased online support March 2017) — confirm via https://www.mkbergman.com/2034/fare-thee-well-opencyc/ and https://kbpedia.org/resources/opencyc/. Note that legacy OpenCyc 4.0 OWL dumps survive only via third-party mirrors (SourceForge opencyc; GitHub asanchez75/opencyc) with no maintenance/support — NOT a reproducible commodity dependency. ResearchCyc is free FOR RESEARCH but requires a license application to Cycorp (info@cyc.com), is not pip/anonymous-downloadable, and ships a far larger curated KB — confirm the access route via https://cyc.com/ (or current Cycorp/ResearchCyc page via search). Conclusion to state: OpenCyc/ResearchCyc cannot be a reproducible, commodity, offline dependency for a public pipeline; a commodity substitute is required.
  B2. SURVEY REAL SUBSTITUTE OPTIONS (one fetch each; extract access route + license + offline-ness + Python library + what taxonomy they give):
    - WordNet hypernyms via NLTK — offline, BSD; nltk.corpus.wordnet, synset.hypernym_paths(); already the dep-B default coarse typer. https://www.nltk.org/howto/wordnet.html
    - SUMO (Suggested Upper Merged Ontology) — the strongest genuine OPEN 'upper ontology' OpenCyc-analogue: SUO-KIF formal upper ontology with ALL WordNet synsets mapped. Files: https://github.com/ontologyportal/sumo (WordNetMappings/WordNetMappings30-{noun,verb,adj,adv}.txt) and portal https://www.ontologyportal.org/ ; Sigma is its inference/dev environment. Offline, Apache/GNU-style license. This gives a real upper-ontology class for each WordNet sense — the recipe can ANCHOR coarse types to SUMO classes to make a legitimate 'upper-ontology grounding' claim.
    - YAGO 4 / 4.5 — clean RDF taxonomy (schema.org top + Wikidata lower), downloadable, triple-store loadable. https://yago-knowledge.org/downloads/yago-4-5 . Good for named-entity INSTANCE typing on professional docs.
    - Wikidata class hierarchy — live SPARQL endpoint (query.wikidata.org), instance-of P31 / subclass-of P279* property paths; Python via SPARQLWrapper (sparql.setQuery/setReturnFormat(JSON)/query().convert()). https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/en . Network-dependent (reproducibility caveat) — use as enricher or pre-cache.
    - DBpedia ontology — dbo:Person/Place/Organisation via SPARQL; optional named-entity typing. (Reuse dep-B note.)
    - For offline OWL/RDF loading in Python, name owlready2 (OWL reasoning over local .owl) and rdflib/SPARQLWrapper (RDF/SPARQL) so the executor specifies a concrete library, not 'an ontology.'
  B3. SPECIFY ONE CONCRETE TWO-LAYER ARGUMENT-TYPING RECIPE (the deliverable). Recommended (the executor should present this as the primary recipe with the exact API surface):
    - LAYER 1 (argument typing, offline, used for decoy generation + entity linking): map each extracted argument's head noun via NLTK WordNet hypernym_paths() to the coarse set {PER,LOC,ORG,TIME,NUM,MISC} using the dep-B anchor synsets (person.n.01, location.n.01/region.n.03, organization.n.01/social_group.n.01, time_period.n.01, number.n.02/measure.n.02), THEN anchor each coarse type to its SUMO upper-ontology class via the WordNetMappings30 files (e.g., Human, GeographicArea, Organization, TimePosition, Number) so the pipeline can legitimately claim 'upper-ontology taxonomic grounding' rather than ad-hoc labels.
    - LAYER 2 (named-entity instance typing for the ~15-30 professional-doc slice): resolve linked entities to a class via Wikidata P31/P279* (SPARQLWrapper, with a small on-disk cache for reproducibility) or offline YAGO 4.5 rdf:type. State the exact query path '?e wdt:P31/wdt:P279* ?class'.
    Give a short worked example per layer (e.g., 'plaintiff' -> WordNet person.n.01 -> PER -> SUMO Human; 'the District Court' -> Wikidata Q -> court -> ORG/Organization).
  B4. JUSTIFY THE SUBSTITUTION HONESTLY (the reviewer-critical paragraph):
    - WHAT IS LOST vs OpenCyc: OpenCyc/Cyc provides microtheories/contextualized assertions, a vast hand-curated commonsense assertion base, rich disjointness/cardinality/domain-range axioms, fine-grained collections, and higher-order/contextual inference — none of which WordNet+SUMO+Wikidata typing reproduces. The substitute provides the TAXONOMIC class hierarchy (the 'taxonomic grounding' the goal names) but NOT OpenCyc's assertional commonsense KB or its contextual logic.
    - WHY TYPING-ONLY USAGE SUFFICES: in this method the ontology is used ONLY to (i) constrain decoy generation (type-matched plausible counterfactuals) and (ii) support entity linking — it NEVER filters or vetoes admissions. The FDR gate's validity rests on decoy competition (the tested sign-flip property) and independent entrapment, NOT on ontology completeness; therefore a thin taxonomy cannot break the guarantee, it can at worst make decoys slightly less type-precise (a measurable, bounded effect), unlike ontology-constraint filtering (ODKE+/SHACL) which DOES depend on rich trusted axioms. State this contrast explicitly — it is the reason typing-only is principled here.
    - DESCOPE vs DEFER: DESCOPE OpenCyc's full microtheory/commonsense-assertion reasoning (out of commodity-reproducibility scope; not required because common-sense gaps are handled by the LLM probabilistic-reasoning step of PART C, not the ontology). DEFER richer SUMO/YAGO axiom-based consistency checks (disjointness/domain-range) as a complementary leftover-budget upgrade that would sit ALONGSIDE the decoy gate, not replace it. Map back to the goal: the goal's 'taxonomic grounding' requirement is MET by the substitute; the goal's 'OpenCyc background structure' (full assertional KB) is descoped with stated rationale.

  === PART C — LLM-AS-PROBABILISTIC-REASONING-ENGINE AT FUZZY UNIFICATIONS (reviewer: scope MAJOR; goal hard requirement) ===
  Objective: specify a concrete, implementable design in which an LLM supplies calibrated probabilities at fuzzy unifications, those probabilities (plus the decoy/entrapment certificates) feed a probabilistic logic engine, and the proof exports as an auditable PROBABILISTIC trace-graph. Justify iteration-1's deterministic backward-chaining substitution and give the upgrade path.
  C1. EXTRACT THE ProbLog PYTHON API (primary engine candidate). Fetch the official docs and tutorial; fetch_grep for exact call signatures:
    - Landing/install: https://dtai.cs.kuleuven.be/problog/ and https://github.com/ML-KULeuven/problog (pip install problog; Python 3.6+).
    - Inference tutorial: https://dtai.cs.kuleuven.be/problog/tutorial/advanced/00_inference.html and https://dtai.cs.kuleuven.be/problog/wasp2017/session3.html — extract the canonical Python pattern: from problog.program import PrologString; from problog import get_evaluatable; model=PrologString(src); result=get_evaluatable().create_from(model).evaluate() -> dict {Term: probability}. Capture how to add probabilistic facts 'p::fact.', annotated disjunctions 'p1::a; p2::b.', rules, and query(...)/evidence(...). Note the readthedocs library API (problog.readthedocs.io) for Term/SimpleProgram construction.
    - Weight learning: confirm LFI (Learning From Interpretations) exists (problog.learning.lfi) for fitting fact probabilities from data — relevant if Phase-0 wants to calibrate weights.
  C2. SURVEY THE ENGINE OPTIONS so the design names alternatives and justifies the pick (one fetch/search each):
    - DeepProbLog / DeepStochLog (arXiv 1805.10872 and follow-ons) — neural predicates supplying probabilities; the closest 'LLM-supplies-probabilities-into-ProbLog' precedent. Cite as the methodological template (replace the neural net with the LLM as the probability source).
    - aProbLog (algebraic ProbLog) — general semirings, useful if weights are not plain probabilities (e.g., to propagate the W_i magnitude or an FDR-derived weight).
    - FUZZY-UNIFICATION engines for the literal 'fuzzy unifications / semantic similarities' requirement: Bousi~Prolog and FASILL (proximity/similarity-based WEAK unification with a lambda-cut threshold). Search 'Bousi-Prolog weak unification proximity relations' and 'FASILL fuzzy logic programming similarity'. These let the LLM supply PROXIMITY DEGREES between predicates/constants where strict symbolic match fails — a direct realization of 'fuzzy unification.' Present ProbLog (probabilistic) and Bousi~Prolog (fuzzy/proximity) as the two concrete instantiations and recommend ONE primary (recommend ProbLog for marginal-probability trace-graphs + the cleanest certificate->weight mapping; name Bousi~Prolog as the fuzzy-unification alternative if the semantics call for similarity degrees rather than probabilities).
  C3. SPECIFY THE CERTIFICATE -> PROBABILISTIC-WEIGHT MAPPING (the core design contribution). Define precisely how each admitted fact/bridge becomes a weighted ProbLog clause:
    - Per-fact weight from the elicitation: take the Phase-0 calibrated probability p_i = calibrate(Z_i) (Platt/isotonic on the elicited score Z_i -> P(entailed)), so the LLM's fuzzy-unification confidence becomes a real probability. Write the admitted fact as 'p_i :: fact(rel,a,b).' and an admitted bridge as a probabilistic/annotated rule.
    - Decoy-competition certificate -> weight: state two principled options for the executor to compare and recommend one: (i) gate-consistent shrinkage — admitted facts share a corpus-level falsity prior equal to the estimated FDR at the operative cutoff (alpha_hat), so weight = (1 - alpha_hat) * p_i, making the probabilistic KB consistent with the FDR certificate; (ii) per-pair margin weight — map the knockoff statistic margin (W_i, or the rank-normalized Z_i - Z~_i) through a monotone calibrated link to P(true), so larger real-vs-decoy wins carry higher weight. Keep W_i/T/alpha in the leaf certificate either way (do NOT discard the gate's binary admission; the weight is layered ON TOP of admission).
    - Entrapment certificate -> prior: the entrapment bound FDP_hat(r) gives an independent corpus falsity estimate; use it as a Bayesian prior / sanity bound on the aggregate weight mass (e.g., expected admitted-false fraction should match FDP_hat). State this as a consistency check, not a second weighting.
    Provide a small table: certificate field -> probabilistic role.
  C4. PROBABILISTIC INFERENCE + TRACE-GRAPH. Specify that ProbLog computes the MARGINAL success probability of each multi-hop derived conclusion (query(conclusion) -> probability), and that the proof structure (ProbLog's grounding / the explanation, or an SDD/d-DNNF) yields a PROBABILISTIC trace-graph: same node/edge shape as dep-B's deterministic Graphviz trace, but every derived node now carries its marginal probability and every leaf carries provenance + decoy_certificate(W_i,T,alpha) + entrapment_certificate(FDP_hat,r) + the calibrated weight p_i. Specify the export: reuse dep-B's JSON + Graphviz-DOT format, adding a 'prob' attribute per node and edge. Note how to obtain per-proof explanations (ProbLog's 'explain'/MPE or enumerating proofs); if ProbLog's native explanation is thin, the fallback is to run ProbLog for the marginal and reuse the janus-swi solve/2 meta-interpreter for the proof DAG, annotating each node with the ProbLog marginal — state this fallback explicitly.
  C5. JUSTIFY THE ITERATION-1 DETERMINISTIC SUBSTITUTION + UPGRADE PATH. Explain WHY iter-1 used deterministic janus-swi backward-chaining (binary admit/reject): (i) the FDR gate already emits a binary admission decision, so binary proof trees suffice for the crisp-gold CLUTRR diagonal and the Re-DocRED wedge; (ii) determinism maximizes reproducibility on commodity CPU and avoids extra inference cost/budget; (iii) it isolates the FDR contribution from probabilistic-inference confounds. Then give the MINIMAL, implementable upgrade for the goal-faithful professional-doc slice (where fuzzy unifications dominate): replace the solve/2 meta-interpreter call with a ProbLog program generated from the admitted clauses (one 'p_i :: fact(...).' / weighted rule per admission), call get_evaluatable().create_from(PrologString(prog)).evaluate() for marginals, and emit the probabilistic trace-graph of C4. Give the exact swap (janus-swi query_once -> problog get_evaluatable/evaluate) and note CPU-only feasibility (ProbLog grounding is light for short docs / few-hop proofs). Add the Bousi~Prolog alternative one-liner for the fuzzy-unification semantics if proximity degrees are preferred over probabilities.

  === OUTPUT FORMAT, RIGOR, CONTINGENCIES ===
  O1. research_out.json `answer` = markdown with the three PARTS above, each containing the concrete tables/recipes/library choices and a short source-traceable positioning note. Include: the PART-A novelty table + one-sentence delta + rebuttal paragraph; the PART-B options-survey table + the chosen two-layer recipe with exact APIs + the loss/sufficiency/descope-vs-defer paragraph; the PART-C engine-options table + certificate->weight mapping table + the trace-graph export spec + the deterministic-justification + upgrade-path code-shaped steps. End `answer` with a 3-5 bullet positioning note tying all three back to the named reviewer gaps (novelty MINOR, scope MAJOR x2) and the goal's literal phrases ('OpenCyc... taxonomic grounding', 'LLM... probabilistic reasoning engine... fuzzy unifications').
  O2. SOURCE-TRACEABILITY (hard requirement): every non-obvious claim, every table cell, every library/API, and every equation carries a [n] citation to a primary source in `sources` (arXiv PDF/HTML, official docs, GitHub repo, ontology portal). Do NOT cite blog summaries for technical claims — use them only for OpenCyc-status corroboration. Use fetch_grep to confirm exact wording/numbers/equations before quoting; flag any claim you could not verify with a confidence note rather than asserting it.
  O3. CONFIDENCE & FOLLOW-UPS: in `follow_up_questions`, record runtime-only unknowns the executor of the METHOD will need to probe (e.g., does ProbLog grounding stay cheap on the longest professional doc; does the chosen calibration link keep weights monotone in Z_i; is the WordNet->SUMO mapping coverage adequate for legal/regulatory nouns; is Wikidata SPARQL latency acceptable or must types be pre-cached offline). Give a short Confidence section in the report (high for ProbLog API / OpenCyc-status / novelty rows verified by fetch_grep; medium where only abstracts were available).
  O4. CONTINGENCIES: if a paper PDF is paywalled, use the arXiv abstract + HTML (ar5iv) + fetch_grep on the PDF URL; if ResearchCyc access details are stale, report the licensing route honestly and lean on the open SUMO/WordNet/Wikidata stack as the recommendation; if the ProbLog README lacks API detail, pull problog.readthedocs.io and the tutorial/session pages and the online-editor examples; if Bousi~Prolog docs are sparse, cite the founding papers (Julian-Iranzo & Rubio-Manzano, weak unification / proximity relations) and present it as the named alternative rather than the primary. Never invent an API signature — quote it from docs or mark it as to-be-verified at runtime.
  O5. SCOPE DISCIPLINE: do NOT re-survey the FDR gate, decoy construction, elicitation, or the Re-DocRED comparison (settled in deps). Stay strictly on the three PARTS. Keep the report tight and decision-oriented: tables and recipes over prose.
explanation: >-
  The iteration-1 paper scored 3/10 chiefly for reporting no empirical results, but the review also left three specific gaps
  that this research artifact must close BEFORE the executor commits compute, because they shape the paper's framing and the
  professional-doc slice that hosts the goal's hard-required hallucination-reduction headline. (A) The novelty MINOR gap:
  reviewers will reach for 'this is just labeled conformal selection / conformal factuality at the fact level.' A crisp table
  that pins each nearest neighbor (Jin-Candes conformal selection, Li-Magesh-Veeravalli multiple-testing detection, COCOCO
  neuro-symbolic conformal sets, conformal e-value novelty detection, conformal link-prediction FDR, Mohri-Hashimoto conformal
  factuality) on label-requirement / unit-certified / exchangeability / decoy? / FDR-vs-coverage isolates the exact delta
  (label-free + decoy competition + intermediate text->logic admission boundary) and preempts the rebuttal. (B) The scope
  MAJOR gap on OpenCyc: the goal literally names OpenCyc for taxonomic grounding, but OpenCyc was discontinued in 2017 and
  ResearchCyc needs a license — so the substitution must be argued with a concrete, reproducible, offline typing recipe (WordNet
  hypernyms anchored to SUMO upper-ontology classes, plus Wikidata/YAGO instance typing) and an honest loss/sufficiency/descope-vs-defer
  analysis, including why typing-only usage cannot break the FDR guarantee (unlike ontology-constraint filtering). (C) The
  scope MAJOR gap on probabilistic reasoning: the goal demands an LLM probabilistic reasoning engine at fuzzy unifications,
  but iteration-1 used deterministic backward-chaining; the artifact must specify a concrete ProbLog (or Bousi~Prolog fuzzy-unification)
  design in which the LLM supplies calibrated unification probabilities, the decoy and entrapment certificates map onto probabilistic
  weights, marginals are computed, and auditable probabilistic trace-graphs are exported — with the implementable upgrade
  path from the deterministic baseline. Answering these three questions now gives the method executor and the paper writer
  concrete tables, libraries, APIs, and a defensible positioning so the next iteration's empirical results land inside a framing
  that survives review.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 06:13:51 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-16 06:14:01 UTC

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
