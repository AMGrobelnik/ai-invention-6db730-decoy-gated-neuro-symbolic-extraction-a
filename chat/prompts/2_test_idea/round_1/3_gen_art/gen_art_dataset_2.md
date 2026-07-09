# gen_art_dataset_2 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 04:55:05 UTC

```
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
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_2_idx2
type: dataset
title: >-
  Re-DocRED Operational Anchor: Standardized Triple-Schema Corpus with Entity Inventory, Evidence, Per-Document S5 Features,
  and >=4 Cross-Document Clusters
summary: >-
  Acquire Re-DocRED (Tan et al., EMNLP 2022) and standardize it into one operational anchor dataset for the label-free FDR-gating
  hypothesis. Each row is one Wikipedia document carrying: (1) the reconstructed ~200-word text, (2) the full annotated entity
  inventory (6 types, mention spans), (3) the human-gold (head, relation, tail) triples mapped into a SHARED canonical triple
  schema with relation names + evidence sentences, (4) per-document descriptive features that vary across documents (length,
  entity/triple density, relation/entity-type profiles, multi-hop/evidence-span proxies) for the S5 GAP regression, and (5)
  a cluster label (metadata_fold) giving >=4 entity-type/topic clusters for leave-one-cluster-out CV, plus a flag splitting
  a ~30-40-doc Phase-0 pilot slice from ~150 balanced confirmatory documents. The dataset supplies the SAME triple space and
  entity set into which every system (neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal) is later mapped
  at matched recall; it asserts only RELATIVE operational comparisons (residual false negatives affect all systems equally).
  Raw data is ~25MB; standardized output is well under 300MB. Pure CPU data-prep: download, parse, compute per-document descriptive
  features, cluster, flag, validate, split full/mini/preview.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  SINGLE SOURCE, deeply standardized (this is a one-dataset standardization task, not a broad search). The dataset is Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022). It is the operational anchor: it hosts the S4 operational-usefulness wedge and the S5 document-level predictive account. It is NOT used for the absolute calibration diagonal (that is CLUTRR, a separate artifact); on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted, because Re-DocRED still has residual false negatives that affect all systems equally.

  WHY RE-DocRED IS IDEAL: (a) realistic open-vocabulary Wikipedia prose (not a toy closed vocabulary), so the relation-to-schema alignment that the neuro-symbolic 'bridge' must perform is genuine; (b) 96 Wikidata relation types + 6 entity types -> a large open relation space where plausible hallucinations actually bite; (c) human-revised gold triples WITH evidence sentences (~13 F1 of recovered false negatives over original DocRED), giving the cleanest available document-level gold for relative precision/recall; (d) SHORT documents (avg 198.4 words, ~8 sentences, ~19.4 entities, ~28-35 triples) -> roughly the ~3000-character target in the goal, CPU-friendly, and cheap to score under the $10 LLM budget; (e) document-level multi-hop structure (triples whose evidence spans multiple sentences) supports the hallucinated-conclusion-rate measurement; (f) heterogeneous topics (biographies, organizations, places, creative works/events) yield the >=4 entity-type/topic clusters needed so S5 input features genuinely VARY across documents (CLUTRR cannot supply this variance -- that is precisely why this anchor exists).

  SIZE / SHAPE OF THE DELIVERED DATASET: ~150 CONFIRMATORY documents balanced across >=4 clusters (target ~35-40 per cluster for 4 clusters) PLUS a ~30-40-document PILOT slice (disjoint from confirmatory, also spread across clusters) flagged for Phase-0 elicitation selection / tail-AUC power analysis and the S5 GAP-regression power analysis. Total ~180-200 standardized rows. Optionally retain a small reserve pool (another ~30-60 docs, flagged is_reserve) so the experiment can top up any under-powered cluster without re-running this artifact. Raw Re-DocRED is ~25MB across three JSON files; the standardized data_out.json (full) will be on the order of tens of MB -- comfortably under the 300MB hard limit (still run the aii-file-size-limit check and split if needed).

  EACH ROW MUST CARRY (raw data only -- NO experiment outputs, NO scores, NO FDR, NO decoys): the reconstructed document text; the complete annotated entity inventory with entity types and mention spans; the gold (head, relation, tail) triples in a single SHARED canonical schema with human-readable relation names + per-triple evidence sentence ids and resolved evidence text; per-document descriptive features (these are simple properties of the data -- length, counts, densities, profiles -- NOT derived experimental statistics); a cluster label as metadata_fold; and pilot/confirmatory/reserve flags. The relation inventory (the 96 P-ids with names and descriptions) and entity-type inventory are emitted as a companion reference so all downstream systems align to the identical triple space.

  GOLD CAVEAT (must be recorded in dataset-level metadata): Re-DocRED gold has residual false negatives; therefore this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) -- never an absolute realized-FDR diagonal. State this explicitly so the experiment does not misuse it.
dataset_search_plan: "STEP 1 -- ACQUIRE Re-DocRED (single source; verify first, then download).\n  Primary source (CONFIRMED\
  \ to exist, public, no auth): HuggingFace dataset 'tonytan48/Re-DocRED'. The three data files sit at the repo ROOT (not\
  \ under data/). Download directly via the resolve URLs:\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/train_revised.json\
  \  (~18.6 MB, 3,053 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/dev_revised.json    (~3.1\
  \ MB, 500 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/test_revised.json   (~3.1 MB, 500\
  \ docs)\n  Use either the aii-hf-datasets skill (huggingface_hub.hf_hub_download with repo_type='dataset') or plain requests.get\
  \ on the resolve URLs. Total ~25 MB -> trivially within 300MB and within memory.\n  Fallback A (if HF is down): GitHub raw\
  \ from tonytan48/Re-DocRED, files under the data/ folder: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/train_revised.json\
  \ (and dev_revised.json, test_revised.json).\n  Fallback B: the GitHub release / repo zip of github.com/tonytan48/Re-DocRED.\
  \ Do NOT substitute the original noisy thunlp/DocRED gold for the confirmatory set (it has the false-negative problem Re-DocRED\
  \ fixes); the original DocRED may only be used, optionally, for a residual-FN sensitivity note.\n  After download, assert\
  \ each file parses as JSON and is a list of document objects; log counts (expect 3053 / 500 / 500). Pool all 4,053 documents\
  \ into one working list tagged by split_origin.\n\nSTEP 2 -- CONFIRM the source schema on a few documents before mass processing.\n\
  \  Each document object has: 'title' (str); 'sents' (list of sentences, each a list of word tokens); 'vertexSet' (list of\
  \ ENTITIES; each entity is a list of MENTIONS; each mention = {'name': str, 'sent_id': int, 'pos': [start_token, end_token]\
  \ HALF-OPEN token offsets within that sentence, 'type': one of PER/ORG/LOC/TIME/NUM/MISC}); 'labels' (list of TRIPLES; each\
  \ = {'h': head entity index into vertexSet, 't': tail entity index into vertexSet, 'r': relation Wikidata P-id string e.g.\
  \ 'P26', 'evidence': list of sentence ids}). Print one full example and assert these keys/types exist; abort with a clear\
  \ message if the schema differs (so a silently-changed mirror is caught early).\n\nSTEP 3 -- BUILD the relation inventory\
  \ (the shared canonical relation space; 96 Wikidata relations).\n  The HF mirror does NOT ship rel_info.json, so resolve\
  \ relation P-id -> human-readable name (+ description) by, in priority order:\n    (i) Try to download a DocRED rel_info.json\
  \ (P-id->name map) from the original repo, e.g. github.com/thunlp/DocRED (search the repo tree for 'rel_info.json'; it is\
  \ part of the original DocRED meta). If found, use its names.\n    (ii) ROBUST DEFAULT -- collect the set of unique P-ids\
  \ actually appearing across all documents' labels, then batch-query the Wikidata API for English label + description: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P26|P17|...&props=labels|descriptions&languages=en&format=json\
  \ (chunk ids to <=50 per call; this is free, public, no LLM budget). Cache the result to a local relation_schema.json.\n\
  \    (iii) Fallback: hardcode the well-known DocRED 96-relation name map (e.g. P6=head of government, P17=country, P19=place\
  \ of birth, P26=spouse, P27=country of citizenship, P569=date of birth, P570=date of death, ...). \n  Emit a companion file\
  \ relation_schema.json: a list of {relation_pid, relation_name, relation_description} for every P-id present (expect ~96).\
  \ The DESCRIPTION is valuable downstream for the relation-alignment step that maps every system's raw output into this triple\
  \ space -- include it. Also emit entity_type_schema = the 6 types with short glosses.\n\nSTEP 4 -- STANDARDIZE each document\
  \ into one row. For every document compute and store:\n  4a. TEXT RECONSTRUCTION: build 'text' deterministically. Per sentence,\
  \ join its tokens; apply light, deterministic detokenization (no space before ,.!?;:)]} or before a closing quote/possessive;\
  \ no space after ([{ or opening quote) so the prose reads naturally for the LLM extractor; then join sentences with a single\
  \ space. Record 'sent_char_offsets' = the character offset in 'text' where each sentence begins. ALSO keep the original\
  \ tokenized 'sents' verbatim (token offsets are the authoritative grounding; char spans are convenience).\n  4b. ENTITY\
  \ INVENTORY ('entities'): for each vertexSet entity i emit {entity_id: i, type: <entity type>, canonical_name: <pick the\
  \ longest or most frequent mention surface>, mentions: [{name, sent_id, pos:[start_tok,end_tok], char_span:[start_char,end_char]\
  \ computed from sent_char_offsets + the detokenized token positions}]}. If char-span computation is fragile for any mention,\
  \ fall back to leaving char_span null but ALWAYS keep the token pos. Record n_mentions per entity.\n  4c. GOLD TRIPLES ('gold_triples',\
  \ the SHARED schema): for each label emit {head_id, head_name(=canonical_name of head), head_type, relation_pid, relation_name(from\
  \ STEP 3), tail_id, tail_name, tail_type, evidence_sent_ids: [...], evidence_text: [the reconstructed text of each evidence\
  \ sentence]}. If a triple has empty evidence (can happen for re-annotated triples), keep evidence_sent_ids=[] and evidence_text=[]\
  \ (do not drop the triple). De-duplicate identical (head_id, relation_pid, tail_id) triples if any.\n  Keep this row as\
  \ raw data only: NO candidate generation, NO decoys, NO scoring, NO derived FDR. Those belong to the experiment.\n\nSTEP\
  \ 5 -- COMPUTE per-document descriptive features (raw properties of the data, stored under metadata; these are the S5 GAP-regression\
  \ inputs, NOT experiment results). For each document record: num_words (token count of text), num_chars, num_sents, num_entities,\
  \ num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts (dict over the 6 types), dominant_entity_type\
  \ (argmax of entity_type_counts; break ties by a fixed type priority PER>ORG>LOC>MISC>TIME>NUM), relation_pid_counts (dict),\
  \ avg_mentions_per_entity, entity_density (num_entities/num_words), mention_density (total_mentions/num_words), triple_density\
  \ (num_triples/num_sents), frac_singleton_entities (entities with exactly 1 mention), and TWO multi-hop / cross-sentence\
  \ proxies: frac_multi_evidence_triples (fraction of triples with >1 evidence sentence) and max_evidence_sentence_gap (max\
  \ over triples of (max evidence sent_id - min evidence sent_id); 0 if all single-sentence). These features deliberately\
  \ VARY across documents/clusters -- that variance is the reason Re-DocRED (not CLUTRR) hosts S5.\n\nSTEP 6 -- CLUSTER documents\
  \ into >=4 clusters (metadata_fold for leave-one-cluster-out CV).\n  PRIMARY scheme (interpretable, recommended as metadata_fold):\
  \ cluster_by = dominant_entity_type, collapsed to FOUR genre-like clusters -> {PER-dominant (biographies), ORG-dominant\
  \ (organizations/bands/companies), LOC-dominant (places/geography), MISC-dominant (creative works/events/other)}. Map the\
  \ rare TIME/NUM-dominant documents into MISC (or their nearest non-rare dominant type) so exactly >=4 well-populated clusters\
  \ result. Set metadata_fold = 'cluster_PER' | 'cluster_ORG' | 'cluster_LOC' | 'cluster_MISC'.\n  SECONDARY scheme (store\
  \ ALSO, for robustness, under metadata.kmeans_cluster): run k-means (k=5 or 6, fixed random_state for reproducibility) on\
  \ a per-document feature vector = normalized 6-dim entity-type histogram concatenated with the normalized top-relation profile\
  \ (and standardized length). This gives a topical clustering independent of the entity-type rule; the experiment can switch\
  \ to it if the entity-type folds prove too correlated.\n  VALIDATE the primary scheme: confirm >=4 clusters each have enough\
  \ source documents to fill the balanced confirmatory quota (target ~35-40/cluster for ~150 confirmatory + pilot). If any\
  \ primary cluster is too small, top it up from the secondary k-means clusters or relax the collapse (e.g. split MISC), but\
  \ ALWAYS keep >=4 clusters and record which scheme produced metadata_fold.\n\nSTEP 7 -- SELECT and FLAG the confirmatory\
  \ set, pilot slice, and reserve.\n  Eligibility filter (keep documents that are useful and on-spec): num_words roughly in\
  \ [80, 400] (most Re-DocRED docs are ~200; this trims outliers while keeping the ~3000-char target), num_entities >= 4,\
  \ num_triples >= 5 (so each document can actually host enough candidates to matter). Do not over-filter -- record num_words\
  \ as a feature rather than discarding moderately long docs.\n  CONFIRMATORY: sample ~150 documents BALANCED across the >=4\
  \ primary clusters (e.g. 4 clusters x ~38 = 152). Within each cluster prefer documents spanning the feature range (do not\
  \ pick only the densest) so cross-document feature variance is preserved for S5. Set metadata.is_confirmatory=true.\n  PILOT:\
  \ sample a DISJOINT ~30-40 documents, also spread across clusters, for Phase-0 (elicitation/tail-AUC selection) and the\
  \ S5 power analysis. Set metadata.is_pilot=true, is_confirmatory=false. Pilot docs are 'labeled' simply in that gold is\
  \ available (all Re-DocRED docs have gold) -- do NOT fabricate negative/decoy triples here; candidate and decoy generation\
  \ is the experiment's job.\n  RESERVE (optional): flag another ~30-60 disjoint docs is_reserve=true so the experiment can\
  \ top up an under-powered cluster without re-running this artifact.\n  Use a FIXED random seed for all sampling and record\
  \ it in dataset-level metadata for reproducibility. Ensure confirmatory / pilot / reserve are mutually exclusive (no document\
  \ appears twice).\n\nSTEP 8 -- ASSEMBLE the output row schema. Each row in data_out.json:\n  {\n    'id': 'redocred_<split_origin>_<orig_index>',\n\
  \    'input': { 'title', 'text', 'sents', 'sent_char_offsets', 'entities': [ {entity_id, type, canonical_name, n_mentions,\
  \ mentions:[{name, sent_id, pos, char_span}]} ] },\n    'output': { 'gold_triples': [ {head_id, head_name, head_type, relation_pid,\
  \ relation_name, tail_id, tail_name, tail_type, evidence_sent_ids, evidence_text} ] },\n    'metadata_fold': '<cluster label\
  \ from STEP 6 primary scheme>',\n    'metadata': { 'split_origin', 'orig_index', 'is_confirmatory', 'is_pilot', 'is_reserve',\
  \ 'kmeans_cluster', 'cluster_scheme', 'seed', plus ALL per-document features from STEP 5 (num_words, num_chars, num_sents,\
  \ num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts, dominant_entity_type,\
  \ relation_pid_counts, avg_mentions_per_entity, entity_density, mention_density, triple_density, frac_singleton_entities,\
  \ frac_multi_evidence_triples, max_evidence_sentence_gap), 'gold_caveat': 'Re-DocRED has residual false negatives; supports\
  \ RELATIVE operational comparisons only, not an absolute FDR diagonal.' }\n  }\n  Keep field names exactly aligned with\
  \ the standard DATASET output contract {input, output, metadata_fold, ...}. Also write companion files: relation_schema.json\
  \ (96 P-ids), entity_type_schema.json (6 types), and a top-level dataset_meta object (source citation + URLs, split counts,\
  \ seed, cluster scheme, per-cluster doc counts, the gold_caveat, and a one-line statement that this is the shared triple\
  \ space all systems map into at matched recall).\n\nSTEP 9 -- VALIDATE and SPLIT. Author a JSON Schema for the row and run\
  \ the aii-json skill to validate every row in data_out.json against it (fail loudly on any missing/extra field or type mismatch).\
  \ Then use aii-json to generate the full / mini / preview variants (mini = a few rows per cluster incl. at least one pilot\
  \ row; preview = 1-2 illustrative rows with all fields populated). Run the aii-file-size-limit skill on data_out.json (expected\
  \ tens of MB, under 300MB) and split only if it exceeds the limit.\n\nSTEP 10 -- SANITY REPORT (log, do not put in data_out\
  \ as derived stats): print final counts (total rows, confirmatory/pilot/reserve, per-cluster), the realized feature ranges\
  \ per cluster (to confirm cross-document variance exists -- the S5 precondition), the number of unique relation P-ids covered\
  \ vs 96 and unique entity types covered vs 6, and a handful of fully-rendered example rows (text + entities + a few gold\
  \ triples with evidence) for eyeball QA. Confirm no document appears in more than one of confirmatory/pilot/reserve, and\
  \ that every gold triple's head_id/tail_id index a valid entity.\n\nFAILURE SCENARIOS & MITIGATIONS:\n  - HF mirror missing/changed\
  \ -> GitHub raw fallback (Step 1 fallback A/B); assert schema in Step 2 to catch silent format drift.\n  - rel_info.json\
  \ unavailable -> Wikidata wbgetentities API (free, no LLM budget) then hardcoded map (Step 3).\n  - Cluster imbalance (PER-dominant\
  \ dominates) -> collapse rare TIME/NUM into MISC, top up from k-means secondary scheme, or split MISC; always keep >=4 balanced,\
  \ populated clusters (Step 6).\n  - Documents too short/long or too few triples -> eligibility filter in Step 7 (keep ~80-400\
  \ words, >=5 triples) but record length as a feature rather than aggressively discarding.\n  - Empty evidence on re-annotated\
  \ triples -> keep the triple with empty evidence arrays (Step 4c); do not drop.\n  - char_span computation fragile for odd\
  \ tokenization -> leave char_span null but always retain authoritative token pos (Step 4b).\n  - Temptation to manufacture\
  \ negatives/decoys for the pilot -> DO NOT; this is a raw-data artifact. Candidate/decoy/scoring generation is the downstream\
  \ experiment's responsibility (keeps this strictly within DATASET executor scope)."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-16 04:55:05 UTC

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

### [3] SKILL-INPUT — aii-hf-datasets · 2026-06-16 04:55:27 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [4] SKILL-INPUT — aii-json · 2026-06-16 04:55:28 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-use-hardware · 2026-06-16 04:55:28 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [6] SKILL-INPUT — aii-python · 2026-06-16 04:55:34 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [7] SKILL-INPUT — aii-file-size-limit · 2026-06-16 04:55:34 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [8] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 04:55:34 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [9] SKILL-INPUT — aii-web-tools · 2026-06-16 04:56:14 UTC

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

### [10] SYSTEM-USER prompt · 2026-06-16 05:06:08 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_2_idx2
type: dataset
title: >-
  Re-DocRED Operational Anchor: Standardized Triple-Schema Corpus with Entity Inventory, Evidence, Per-Document S5 Features,
  and >=4 Cross-Document Clusters
summary: >-
  Acquire Re-DocRED (Tan et al., EMNLP 2022) and standardize it into one operational anchor dataset for the label-free FDR-gating
  hypothesis. Each row is one Wikipedia document carrying: (1) the reconstructed ~200-word text, (2) the full annotated entity
  inventory (6 types, mention spans), (3) the human-gold (head, relation, tail) triples mapped into a SHARED canonical triple
  schema with relation names + evidence sentences, (4) per-document descriptive features that vary across documents (length,
  entity/triple density, relation/entity-type profiles, multi-hop/evidence-span proxies) for the S5 GAP regression, and (5)
  a cluster label (metadata_fold) giving >=4 entity-type/topic clusters for leave-one-cluster-out CV, plus a flag splitting
  a ~30-40-doc Phase-0 pilot slice from ~150 balanced confirmatory documents. The dataset supplies the SAME triple space and
  entity set into which every system (neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal) is later mapped
  at matched recall; it asserts only RELATIVE operational comparisons (residual false negatives affect all systems equally).
  Raw data is ~25MB; standardized output is well under 300MB. Pure CPU data-prep: download, parse, compute per-document descriptive
  features, cluster, flag, validate, split full/mini/preview.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  SINGLE SOURCE, deeply standardized (this is a one-dataset standardization task, not a broad search). The dataset is Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022). It is the operational anchor: it hosts the S4 operational-usefulness wedge and the S5 document-level predictive account. It is NOT used for the absolute calibration diagonal (that is CLUTRR, a separate artifact); on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted, because Re-DocRED still has residual false negatives that affect all systems equally.

  WHY RE-DocRED IS IDEAL: (a) realistic open-vocabulary Wikipedia prose (not a toy closed vocabulary), so the relation-to-schema alignment that the neuro-symbolic 'bridge' must perform is genuine; (b) 96 Wikidata relation types + 6 entity types -> a large open relation space where plausible hallucinations actually bite; (c) human-revised gold triples WITH evidence sentences (~13 F1 of recovered false negatives over original DocRED), giving the cleanest available document-level gold for relative precision/recall; (d) SHORT documents (avg 198.4 words, ~8 sentences, ~19.4 entities, ~28-35 triples) -> roughly the ~3000-character target in the goal, CPU-friendly, and cheap to score under the $10 LLM budget; (e) document-level multi-hop structure (triples whose evidence spans multiple sentences) supports the hallucinated-conclusion-rate measurement; (f) heterogeneous topics (biographies, organizations, places, creative works/events) yield the >=4 entity-type/topic clusters needed so S5 input features genuinely VARY across documents (CLUTRR cannot supply this variance -- that is precisely why this anchor exists).

  SIZE / SHAPE OF THE DELIVERED DATASET: ~150 CONFIRMATORY documents balanced across >=4 clusters (target ~35-40 per cluster for 4 clusters) PLUS a ~30-40-document PILOT slice (disjoint from confirmatory, also spread across clusters) flagged for Phase-0 elicitation selection / tail-AUC power analysis and the S5 GAP-regression power analysis. Total ~180-200 standardized rows. Optionally retain a small reserve pool (another ~30-60 docs, flagged is_reserve) so the experiment can top up any under-powered cluster without re-running this artifact. Raw Re-DocRED is ~25MB across three JSON files; the standardized data_out.json (full) will be on the order of tens of MB -- comfortably under the 300MB hard limit (still run the aii-file-size-limit check and split if needed).

  EACH ROW MUST CARRY (raw data only -- NO experiment outputs, NO scores, NO FDR, NO decoys): the reconstructed document text; the complete annotated entity inventory with entity types and mention spans; the gold (head, relation, tail) triples in a single SHARED canonical schema with human-readable relation names + per-triple evidence sentence ids and resolved evidence text; per-document descriptive features (these are simple properties of the data -- length, counts, densities, profiles -- NOT derived experimental statistics); a cluster label as metadata_fold; and pilot/confirmatory/reserve flags. The relation inventory (the 96 P-ids with names and descriptions) and entity-type inventory are emitted as a companion reference so all downstream systems align to the identical triple space.

  GOLD CAVEAT (must be recorded in dataset-level metadata): Re-DocRED gold has residual false negatives; therefore this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) -- never an absolute realized-FDR diagonal. State this explicitly so the experiment does not misuse it.
dataset_search_plan: "STEP 1 -- ACQUIRE Re-DocRED (single source; verify first, then download).\n  Primary source (CONFIRMED\
  \ to exist, public, no auth): HuggingFace dataset 'tonytan48/Re-DocRED'. The three data files sit at the repo ROOT (not\
  \ under data/). Download directly via the resolve URLs:\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/train_revised.json\
  \  (~18.6 MB, 3,053 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/dev_revised.json    (~3.1\
  \ MB, 500 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/test_revised.json   (~3.1 MB, 500\
  \ docs)\n  Use either the aii-hf-datasets skill (huggingface_hub.hf_hub_download with repo_type='dataset') or plain requests.get\
  \ on the resolve URLs. Total ~25 MB -> trivially within 300MB and within memory.\n  Fallback A (if HF is down): GitHub raw\
  \ from tonytan48/Re-DocRED, files under the data/ folder: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/train_revised.json\
  \ (and dev_revised.json, test_revised.json).\n  Fallback B: the GitHub release / repo zip of github.com/tonytan48/Re-DocRED.\
  \ Do NOT substitute the original noisy thunlp/DocRED gold for the confirmatory set (it has the false-negative problem Re-DocRED\
  \ fixes); the original DocRED may only be used, optionally, for a residual-FN sensitivity note.\n  After download, assert\
  \ each file parses as JSON and is a list of document objects; log counts (expect 3053 / 500 / 500). Pool all 4,053 documents\
  \ into one working list tagged by split_origin.\n\nSTEP 2 -- CONFIRM the source schema on a few documents before mass processing.\n\
  \  Each document object has: 'title' (str); 'sents' (list of sentences, each a list of word tokens); 'vertexSet' (list of\
  \ ENTITIES; each entity is a list of MENTIONS; each mention = {'name': str, 'sent_id': int, 'pos': [start_token, end_token]\
  \ HALF-OPEN token offsets within that sentence, 'type': one of PER/ORG/LOC/TIME/NUM/MISC}); 'labels' (list of TRIPLES; each\
  \ = {'h': head entity index into vertexSet, 't': tail entity index into vertexSet, 'r': relation Wikidata P-id string e.g.\
  \ 'P26', 'evidence': list of sentence ids}). Print one full example and assert these keys/types exist; abort with a clear\
  \ message if the schema differs (so a silently-changed mirror is caught early).\n\nSTEP 3 -- BUILD the relation inventory\
  \ (the shared canonical relation space; 96 Wikidata relations).\n  The HF mirror does NOT ship rel_info.json, so resolve\
  \ relation P-id -> human-readable name (+ description) by, in priority order:\n    (i) Try to download a DocRED rel_info.json\
  \ (P-id->name map) from the original repo, e.g. github.com/thunlp/DocRED (search the repo tree for 'rel_info.json'; it is\
  \ part of the original DocRED meta). If found, use its names.\n    (ii) ROBUST DEFAULT -- collect the set of unique P-ids\
  \ actually appearing across all documents' labels, then batch-query the Wikidata API for English label + description: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P26|P17|...&props=labels|descriptions&languages=en&format=json\
  \ (chunk ids to <=50 per call; this is free, public, no LLM budget). Cache the result to a local relation_schema.json.\n\
  \    (iii) Fallback: hardcode the well-known DocRED 96-relation name map (e.g. P6=head of government, P17=country, P19=place\
  \ of birth, P26=spouse, P27=country of citizenship, P569=date of birth, P570=date of death, ...). \n  Emit a companion file\
  \ relation_schema.json: a list of {relation_pid, relation_name, relation_description} for every P-id present (expect ~96).\
  \ The DESCRIPTION is valuable downstream for the relation-alignment step that maps every system's raw output into this triple\
  \ space -- include it. Also emit entity_type_schema = the 6 types with short glosses.\n\nSTEP 4 -- STANDARDIZE each document\
  \ into one row. For every document compute and store:\n  4a. TEXT RECONSTRUCTION: build 'text' deterministically. Per sentence,\
  \ join its tokens; apply light, deterministic detokenization (no space before ,.!?;:)]} or before a closing quote/possessive;\
  \ no space after ([{ or opening quote) so the prose reads naturally for the LLM extractor; then join sentences with a single\
  \ space. Record 'sent_char_offsets' = the character offset in 'text' where each sentence begins. ALSO keep the original\
  \ tokenized 'sents' verbatim (token offsets are the authoritative grounding; char spans are convenience).\n  4b. ENTITY\
  \ INVENTORY ('entities'): for each vertexSet entity i emit {entity_id: i, type: <entity type>, canonical_name: <pick the\
  \ longest or most frequent mention surface>, mentions: [{name, sent_id, pos:[start_tok,end_tok], char_span:[start_char,end_char]\
  \ computed from sent_char_offsets + the detokenized token positions}]}. If char-span computation is fragile for any mention,\
  \ fall back to leaving char_span null but ALWAYS keep the token pos. Record n_mentions per entity.\n  4c. GOLD TRIPLES ('gold_triples',\
  \ the SHARED schema): for each label emit {head_id, head_name(=canonical_name of head), head_type, relation_pid, relation_name(from\
  \ STEP 3), tail_id, tail_name, tail_type, evidence_sent_ids: [...], evidence_text: [the reconstructed text of each evidence\
  \ sentence]}. If a triple has empty evidence (can happen for re-annotated triples), keep evidence_sent_ids=[] and evidence_text=[]\
  \ (do not drop the triple). De-duplicate identical (head_id, relation_pid, tail_id) triples if any.\n  Keep this row as\
  \ raw data only: NO candidate generation, NO decoys, NO scoring, NO derived FDR. Those belong to the experiment.\n\nSTEP\
  \ 5 -- COMPUTE per-document descriptive features (raw properties of the data, stored under metadata; these are the S5 GAP-regression\
  \ inputs, NOT experiment results). For each document record: num_words (token count of text), num_chars, num_sents, num_entities,\
  \ num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts (dict over the 6 types), dominant_entity_type\
  \ (argmax of entity_type_counts; break ties by a fixed type priority PER>ORG>LOC>MISC>TIME>NUM), relation_pid_counts (dict),\
  \ avg_mentions_per_entity, entity_density (num_entities/num_words), mention_density (total_mentions/num_words), triple_density\
  \ (num_triples/num_sents), frac_singleton_entities (entities with exactly 1 mention), and TWO multi-hop / cross-sentence\
  \ proxies: frac_multi_evidence_triples (fraction of triples with >1 evidence sentence) and max_evidence_sentence_gap (max\
  \ over triples of (max evidence sent_id - min evidence sent_id); 0 if all single-sentence). These features deliberately\
  \ VARY across documents/clusters -- that variance is the reason Re-DocRED (not CLUTRR) hosts S5.\n\nSTEP 6 -- CLUSTER documents\
  \ into >=4 clusters (metadata_fold for leave-one-cluster-out CV).\n  PRIMARY scheme (interpretable, recommended as metadata_fold):\
  \ cluster_by = dominant_entity_type, collapsed to FOUR genre-like clusters -> {PER-dominant (biographies), ORG-dominant\
  \ (organizations/bands/companies), LOC-dominant (places/geography), MISC-dominant (creative works/events/other)}. Map the\
  \ rare TIME/NUM-dominant documents into MISC (or their nearest non-rare dominant type) so exactly >=4 well-populated clusters\
  \ result. Set metadata_fold = 'cluster_PER' | 'cluster_ORG' | 'cluster_LOC' | 'cluster_MISC'.\n  SECONDARY scheme (store\
  \ ALSO, for robustness, under metadata.kmeans_cluster): run k-means (k=5 or 6, fixed random_state for reproducibility) on\
  \ a per-document feature vector = normalized 6-dim entity-type histogram concatenated with the normalized top-relation profile\
  \ (and standardized length). This gives a topical clustering independent of the entity-type rule; the experiment can switch\
  \ to it if the entity-type folds prove too correlated.\n  VALIDATE the primary scheme: confirm >=4 clusters each have enough\
  \ source documents to fill the balanced confirmatory quota (target ~35-40/cluster for ~150 confirmatory + pilot). If any\
  \ primary cluster is too small, top it up from the secondary k-means clusters or relax the collapse (e.g. split MISC), but\
  \ ALWAYS keep >=4 clusters and record which scheme produced metadata_fold.\n\nSTEP 7 -- SELECT and FLAG the confirmatory\
  \ set, pilot slice, and reserve.\n  Eligibility filter (keep documents that are useful and on-spec): num_words roughly in\
  \ [80, 400] (most Re-DocRED docs are ~200; this trims outliers while keeping the ~3000-char target), num_entities >= 4,\
  \ num_triples >= 5 (so each document can actually host enough candidates to matter). Do not over-filter -- record num_words\
  \ as a feature rather than discarding moderately long docs.\n  CONFIRMATORY: sample ~150 documents BALANCED across the >=4\
  \ primary clusters (e.g. 4 clusters x ~38 = 152). Within each cluster prefer documents spanning the feature range (do not\
  \ pick only the densest) so cross-document feature variance is preserved for S5. Set metadata.is_confirmatory=true.\n  PILOT:\
  \ sample a DISJOINT ~30-40 documents, also spread across clusters, for Phase-0 (elicitation/tail-AUC selection) and the\
  \ S5 power analysis. Set metadata.is_pilot=true, is_confirmatory=false. Pilot docs are 'labeled' simply in that gold is\
  \ available (all Re-DocRED docs have gold) -- do NOT fabricate negative/decoy triples here; candidate and decoy generation\
  \ is the experiment's job.\n  RESERVE (optional): flag another ~30-60 disjoint docs is_reserve=true so the experiment can\
  \ top up an under-powered cluster without re-running this artifact.\n  Use a FIXED random seed for all sampling and record\
  \ it in dataset-level metadata for reproducibility. Ensure confirmatory / pilot / reserve are mutually exclusive (no document\
  \ appears twice).\n\nSTEP 8 -- ASSEMBLE the output row schema. Each row in data_out.json:\n  {\n    'id': 'redocred_<split_origin>_<orig_index>',\n\
  \    'input': { 'title', 'text', 'sents', 'sent_char_offsets', 'entities': [ {entity_id, type, canonical_name, n_mentions,\
  \ mentions:[{name, sent_id, pos, char_span}]} ] },\n    'output': { 'gold_triples': [ {head_id, head_name, head_type, relation_pid,\
  \ relation_name, tail_id, tail_name, tail_type, evidence_sent_ids, evidence_text} ] },\n    'metadata_fold': '<cluster label\
  \ from STEP 6 primary scheme>',\n    'metadata': { 'split_origin', 'orig_index', 'is_confirmatory', 'is_pilot', 'is_reserve',\
  \ 'kmeans_cluster', 'cluster_scheme', 'seed', plus ALL per-document features from STEP 5 (num_words, num_chars, num_sents,\
  \ num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts, dominant_entity_type,\
  \ relation_pid_counts, avg_mentions_per_entity, entity_density, mention_density, triple_density, frac_singleton_entities,\
  \ frac_multi_evidence_triples, max_evidence_sentence_gap), 'gold_caveat': 'Re-DocRED has residual false negatives; supports\
  \ RELATIVE operational comparisons only, not an absolute FDR diagonal.' }\n  }\n  Keep field names exactly aligned with\
  \ the standard DATASET output contract {input, output, metadata_fold, ...}. Also write companion files: relation_schema.json\
  \ (96 P-ids), entity_type_schema.json (6 types), and a top-level dataset_meta object (source citation + URLs, split counts,\
  \ seed, cluster scheme, per-cluster doc counts, the gold_caveat, and a one-line statement that this is the shared triple\
  \ space all systems map into at matched recall).\n\nSTEP 9 -- VALIDATE and SPLIT. Author a JSON Schema for the row and run\
  \ the aii-json skill to validate every row in data_out.json against it (fail loudly on any missing/extra field or type mismatch).\
  \ Then use aii-json to generate the full / mini / preview variants (mini = a few rows per cluster incl. at least one pilot\
  \ row; preview = 1-2 illustrative rows with all fields populated). Run the aii-file-size-limit skill on data_out.json (expected\
  \ tens of MB, under 300MB) and split only if it exceeds the limit.\n\nSTEP 10 -- SANITY REPORT (log, do not put in data_out\
  \ as derived stats): print final counts (total rows, confirmatory/pilot/reserve, per-cluster), the realized feature ranges\
  \ per cluster (to confirm cross-document variance exists -- the S5 precondition), the number of unique relation P-ids covered\
  \ vs 96 and unique entity types covered vs 6, and a handful of fully-rendered example rows (text + entities + a few gold\
  \ triples with evidence) for eyeball QA. Confirm no document appears in more than one of confirmatory/pilot/reserve, and\
  \ that every gold triple's head_id/tail_id index a valid entity.\n\nFAILURE SCENARIOS & MITIGATIONS:\n  - HF mirror missing/changed\
  \ -> GitHub raw fallback (Step 1 fallback A/B); assert schema in Step 2 to catch silent format drift.\n  - rel_info.json\
  \ unavailable -> Wikidata wbgetentities API (free, no LLM budget) then hardcoded map (Step 3).\n  - Cluster imbalance (PER-dominant\
  \ dominates) -> collapse rare TIME/NUM into MISC, top up from k-means secondary scheme, or split MISC; always keep >=4 balanced,\
  \ populated clusters (Step 6).\n  - Documents too short/long or too few triples -> eligibility filter in Step 7 (keep ~80-400\
  \ words, >=5 triples) but record length as a feature rather than aggressively discarding.\n  - Empty evidence on re-annotated\
  \ triples -> keep the triple with empty evidence arrays (Step 4c); do not drop.\n  - char_span computation fragile for odd\
  \ tokenization -> leave char_span null but always retain authoritative token pos (Step 4b).\n  - Temptation to manufacture\
  \ negatives/decoys for the pilot -> DO NOT; this is a raw-data artifact. Candidate/decoy/scoring generation is the downstream\
  \ experiment's responsibility (keeps this strictly within DATASET executor scope)."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 2 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 1 DATASET based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [11] SYSTEM-USER prompt · 2026-06-16 05:09:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_2_idx2
type: dataset
title: >-
  Re-DocRED Operational Anchor: Standardized Triple-Schema Corpus with Entity Inventory, Evidence, Per-Document S5 Features,
  and >=4 Cross-Document Clusters
summary: >-
  Acquire Re-DocRED (Tan et al., EMNLP 2022) and standardize it into one operational anchor dataset for the label-free FDR-gating
  hypothesis. Each row is one Wikipedia document carrying: (1) the reconstructed ~200-word text, (2) the full annotated entity
  inventory (6 types, mention spans), (3) the human-gold (head, relation, tail) triples mapped into a SHARED canonical triple
  schema with relation names + evidence sentences, (4) per-document descriptive features that vary across documents (length,
  entity/triple density, relation/entity-type profiles, multi-hop/evidence-span proxies) for the S5 GAP regression, and (5)
  a cluster label (metadata_fold) giving >=4 entity-type/topic clusters for leave-one-cluster-out CV, plus a flag splitting
  a ~30-40-doc Phase-0 pilot slice from ~150 balanced confirmatory documents. The dataset supplies the SAME triple space and
  entity set into which every system (neuro-symbolic, plain confidence threshold, CoT, RAG, labeled conformal) is later mapped
  at matched recall; it asserts only RELATIVE operational comparisons (residual false negatives affect all systems equally).
  Raw data is ~25MB; standardized output is well under 300MB. Pure CPU data-prep: download, parse, compute per-document descriptive
  features, cluster, flag, validate, split full/mini/preview.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  SINGLE SOURCE, deeply standardized (this is a one-dataset standardization task, not a broad search). The dataset is Re-DocRED (Tan, Xu, Bing et al., 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022). It is the operational anchor: it hosts the S4 operational-usefulness wedge and the S5 document-level predictive account. It is NOT used for the absolute calibration diagonal (that is CLUTRR, a separate artifact); on Re-DocRED only RELATIVE operational comparisons under shared gold are asserted, because Re-DocRED still has residual false negatives that affect all systems equally.

  WHY RE-DocRED IS IDEAL: (a) realistic open-vocabulary Wikipedia prose (not a toy closed vocabulary), so the relation-to-schema alignment that the neuro-symbolic 'bridge' must perform is genuine; (b) 96 Wikidata relation types + 6 entity types -> a large open relation space where plausible hallucinations actually bite; (c) human-revised gold triples WITH evidence sentences (~13 F1 of recovered false negatives over original DocRED), giving the cleanest available document-level gold for relative precision/recall; (d) SHORT documents (avg 198.4 words, ~8 sentences, ~19.4 entities, ~28-35 triples) -> roughly the ~3000-character target in the goal, CPU-friendly, and cheap to score under the $10 LLM budget; (e) document-level multi-hop structure (triples whose evidence spans multiple sentences) supports the hallucinated-conclusion-rate measurement; (f) heterogeneous topics (biographies, organizations, places, creative works/events) yield the >=4 entity-type/topic clusters needed so S5 input features genuinely VARY across documents (CLUTRR cannot supply this variance -- that is precisely why this anchor exists).

  SIZE / SHAPE OF THE DELIVERED DATASET: ~150 CONFIRMATORY documents balanced across >=4 clusters (target ~35-40 per cluster for 4 clusters) PLUS a ~30-40-document PILOT slice (disjoint from confirmatory, also spread across clusters) flagged for Phase-0 elicitation selection / tail-AUC power analysis and the S5 GAP-regression power analysis. Total ~180-200 standardized rows. Optionally retain a small reserve pool (another ~30-60 docs, flagged is_reserve) so the experiment can top up any under-powered cluster without re-running this artifact. Raw Re-DocRED is ~25MB across three JSON files; the standardized data_out.json (full) will be on the order of tens of MB -- comfortably under the 300MB hard limit (still run the aii-file-size-limit check and split if needed).

  EACH ROW MUST CARRY (raw data only -- NO experiment outputs, NO scores, NO FDR, NO decoys): the reconstructed document text; the complete annotated entity inventory with entity types and mention spans; the gold (head, relation, tail) triples in a single SHARED canonical schema with human-readable relation names + per-triple evidence sentence ids and resolved evidence text; per-document descriptive features (these are simple properties of the data -- length, counts, densities, profiles -- NOT derived experimental statistics); a cluster label as metadata_fold; and pilot/confirmatory/reserve flags. The relation inventory (the 96 P-ids with names and descriptions) and entity-type inventory are emitted as a companion reference so all downstream systems align to the identical triple space.

  GOLD CAVEAT (must be recorded in dataset-level metadata): Re-DocRED gold has residual false negatives; therefore this dataset licenses ONLY relative operational comparisons at matched recall (precision, hallucinated-conclusion rate) -- never an absolute realized-FDR diagonal. State this explicitly so the experiment does not misuse it.
dataset_search_plan: "STEP 1 -- ACQUIRE Re-DocRED (single source; verify first, then download).\n  Primary source (CONFIRMED\
  \ to exist, public, no auth): HuggingFace dataset 'tonytan48/Re-DocRED'. The three data files sit at the repo ROOT (not\
  \ under data/). Download directly via the resolve URLs:\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/train_revised.json\
  \  (~18.6 MB, 3,053 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/dev_revised.json    (~3.1\
  \ MB, 500 docs)\n    - https://huggingface.co/datasets/tonytan48/Re-DocRED/resolve/main/test_revised.json   (~3.1 MB, 500\
  \ docs)\n  Use either the aii-hf-datasets skill (huggingface_hub.hf_hub_download with repo_type='dataset') or plain requests.get\
  \ on the resolve URLs. Total ~25 MB -> trivially within 300MB and within memory.\n  Fallback A (if HF is down): GitHub raw\
  \ from tonytan48/Re-DocRED, files under the data/ folder: https://raw.githubusercontent.com/tonytan48/Re-DocRED/main/data/train_revised.json\
  \ (and dev_revised.json, test_revised.json).\n  Fallback B: the GitHub release / repo zip of github.com/tonytan48/Re-DocRED.\
  \ Do NOT substitute the original noisy thunlp/DocRED gold for the confirmatory set (it has the false-negative problem Re-DocRED\
  \ fixes); the original DocRED may only be used, optionally, for a residual-FN sensitivity note.\n  After download, assert\
  \ each file parses as JSON and is a list of document objects; log counts (expect 3053 / 500 / 500). Pool all 4,053 documents\
  \ into one working list tagged by split_origin.\n\nSTEP 2 -- CONFIRM the source schema on a few documents before mass processing.\n\
  \  Each document object has: 'title' (str); 'sents' (list of sentences, each a list of word tokens); 'vertexSet' (list of\
  \ ENTITIES; each entity is a list of MENTIONS; each mention = {'name': str, 'sent_id': int, 'pos': [start_token, end_token]\
  \ HALF-OPEN token offsets within that sentence, 'type': one of PER/ORG/LOC/TIME/NUM/MISC}); 'labels' (list of TRIPLES; each\
  \ = {'h': head entity index into vertexSet, 't': tail entity index into vertexSet, 'r': relation Wikidata P-id string e.g.\
  \ 'P26', 'evidence': list of sentence ids}). Print one full example and assert these keys/types exist; abort with a clear\
  \ message if the schema differs (so a silently-changed mirror is caught early).\n\nSTEP 3 -- BUILD the relation inventory\
  \ (the shared canonical relation space; 96 Wikidata relations).\n  The HF mirror does NOT ship rel_info.json, so resolve\
  \ relation P-id -> human-readable name (+ description) by, in priority order:\n    (i) Try to download a DocRED rel_info.json\
  \ (P-id->name map) from the original repo, e.g. github.com/thunlp/DocRED (search the repo tree for 'rel_info.json'; it is\
  \ part of the original DocRED meta). If found, use its names.\n    (ii) ROBUST DEFAULT -- collect the set of unique P-ids\
  \ actually appearing across all documents' labels, then batch-query the Wikidata API for English label + description: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P26|P17|...&props=labels|descriptions&languages=en&format=json\
  \ (chunk ids to <=50 per call; this is free, public, no LLM budget). Cache the result to a local relation_schema.json.\n\
  \    (iii) Fallback: hardcode the well-known DocRED 96-relation name map (e.g. P6=head of government, P17=country, P19=place\
  \ of birth, P26=spouse, P27=country of citizenship, P569=date of birth, P570=date of death, ...). \n  Emit a companion file\
  \ relation_schema.json: a list of {relation_pid, relation_name, relation_description} for every P-id present (expect ~96).\
  \ The DESCRIPTION is valuable downstream for the relation-alignment step that maps every system's raw output into this triple\
  \ space -- include it. Also emit entity_type_schema = the 6 types with short glosses.\n\nSTEP 4 -- STANDARDIZE each document\
  \ into one row. For every document compute and store:\n  4a. TEXT RECONSTRUCTION: build 'text' deterministically. Per sentence,\
  \ join its tokens; apply light, deterministic detokenization (no space before ,.!?;:)]} or before a closing quote/possessive;\
  \ no space after ([{ or opening quote) so the prose reads naturally for the LLM extractor; then join sentences with a single\
  \ space. Record 'sent_char_offsets' = the character offset in 'text' where each sentence begins. ALSO keep the original\
  \ tokenized 'sents' verbatim (token offsets are the authoritative grounding; char spans are convenience).\n  4b. ENTITY\
  \ INVENTORY ('entities'): for each vertexSet entity i emit {entity_id: i, type: <entity type>, canonical_name: <pick the\
  \ longest or most frequent mention surface>, mentions: [{name, sent_id, pos:[start_tok,end_tok], char_span:[start_char,end_char]\
  \ computed from sent_char_offsets + the detokenized token positions}]}. If char-span computation is fragile for any mention,\
  \ fall back to leaving char_span null but ALWAYS keep the token pos. Record n_mentions per entity.\n  4c. GOLD TRIPLES ('gold_triples',\
  \ the SHARED schema): for each label emit {head_id, head_name(=canonical_name of head), head_type, relation_pid, relation_name(from\
  \ STEP 3), tail_id, tail_name, tail_type, evidence_sent_ids: [...], evidence_text: [the reconstructed text of each evidence\
  \ sentence]}. If a triple has empty evidence (can happen for re-annotated triples), keep evidence_sent_ids=[] and evidence_text=[]\
  \ (do not drop the triple). De-duplicate identical (head_id, relation_pid, tail_id) triples if any.\n  Keep this row as\
  \ raw data only: NO candidate generation, NO decoys, NO scoring, NO derived FDR. Those belong to the experiment.\n\nSTEP\
  \ 5 -- COMPUTE per-document descriptive features (raw properties of the data, stored under metadata; these are the S5 GAP-regression\
  \ inputs, NOT experiment results). For each document record: num_words (token count of text), num_chars, num_sents, num_entities,\
  \ num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts (dict over the 6 types), dominant_entity_type\
  \ (argmax of entity_type_counts; break ties by a fixed type priority PER>ORG>LOC>MISC>TIME>NUM), relation_pid_counts (dict),\
  \ avg_mentions_per_entity, entity_density (num_entities/num_words), mention_density (total_mentions/num_words), triple_density\
  \ (num_triples/num_sents), frac_singleton_entities (entities with exactly 1 mention), and TWO multi-hop / cross-sentence\
  \ proxies: frac_multi_evidence_triples (fraction of triples with >1 evidence sentence) and max_evidence_sentence_gap (max\
  \ over triples of (max evidence sent_id - min evidence sent_id); 0 if all single-sentence). These features deliberately\
  \ VARY across documents/clusters -- that variance is the reason Re-DocRED (not CLUTRR) hosts S5.\n\nSTEP 6 -- CLUSTER documents\
  \ into >=4 clusters (metadata_fold for leave-one-cluster-out CV).\n  PRIMARY scheme (interpretable, recommended as metadata_fold):\
  \ cluster_by = dominant_entity_type, collapsed to FOUR genre-like clusters -> {PER-dominant (biographies), ORG-dominant\
  \ (organizations/bands/companies), LOC-dominant (places/geography), MISC-dominant (creative works/events/other)}. Map the\
  \ rare TIME/NUM-dominant documents into MISC (or their nearest non-rare dominant type) so exactly >=4 well-populated clusters\
  \ result. Set metadata_fold = 'cluster_PER' | 'cluster_ORG' | 'cluster_LOC' | 'cluster_MISC'.\n  SECONDARY scheme (store\
  \ ALSO, for robustness, under metadata.kmeans_cluster): run k-means (k=5 or 6, fixed random_state for reproducibility) on\
  \ a per-document feature vector = normalized 6-dim entity-type histogram concatenated with the normalized top-relation profile\
  \ (and standardized length). This gives a topical clustering independent of the entity-type rule; the experiment can switch\
  \ to it if the entity-type folds prove too correlated.\n  VALIDATE the primary scheme: confirm >=4 clusters each have enough\
  \ source documents to fill the balanced confirmatory quota (target ~35-40/cluster for ~150 confirmatory + pilot). If any\
  \ primary cluster is too small, top it up from the secondary k-means clusters or relax the collapse (e.g. split MISC), but\
  \ ALWAYS keep >=4 clusters and record which scheme produced metadata_fold.\n\nSTEP 7 -- SELECT and FLAG the confirmatory\
  \ set, pilot slice, and reserve.\n  Eligibility filter (keep documents that are useful and on-spec): num_words roughly in\
  \ [80, 400] (most Re-DocRED docs are ~200; this trims outliers while keeping the ~3000-char target), num_entities >= 4,\
  \ num_triples >= 5 (so each document can actually host enough candidates to matter). Do not over-filter -- record num_words\
  \ as a feature rather than discarding moderately long docs.\n  CONFIRMATORY: sample ~150 documents BALANCED across the >=4\
  \ primary clusters (e.g. 4 clusters x ~38 = 152). Within each cluster prefer documents spanning the feature range (do not\
  \ pick only the densest) so cross-document feature variance is preserved for S5. Set metadata.is_confirmatory=true.\n  PILOT:\
  \ sample a DISJOINT ~30-40 documents, also spread across clusters, for Phase-0 (elicitation/tail-AUC selection) and the\
  \ S5 power analysis. Set metadata.is_pilot=true, is_confirmatory=false. Pilot docs are 'labeled' simply in that gold is\
  \ available (all Re-DocRED docs have gold) -- do NOT fabricate negative/decoy triples here; candidate and decoy generation\
  \ is the experiment's job.\n  RESERVE (optional): flag another ~30-60 disjoint docs is_reserve=true so the experiment can\
  \ top up an under-powered cluster without re-running this artifact.\n  Use a FIXED random seed for all sampling and record\
  \ it in dataset-level metadata for reproducibility. Ensure confirmatory / pilot / reserve are mutually exclusive (no document\
  \ appears twice).\n\nSTEP 8 -- ASSEMBLE the output row schema. Each row in data_out.json:\n  {\n    'id': 'redocred_<split_origin>_<orig_index>',\n\
  \    'input': { 'title', 'text', 'sents', 'sent_char_offsets', 'entities': [ {entity_id, type, canonical_name, n_mentions,\
  \ mentions:[{name, sent_id, pos, char_span}]} ] },\n    'output': { 'gold_triples': [ {head_id, head_name, head_type, relation_pid,\
  \ relation_name, tail_id, tail_name, tail_type, evidence_sent_ids, evidence_text} ] },\n    'metadata_fold': '<cluster label\
  \ from STEP 6 primary scheme>',\n    'metadata': { 'split_origin', 'orig_index', 'is_confirmatory', 'is_pilot', 'is_reserve',\
  \ 'kmeans_cluster', 'cluster_scheme', 'seed', plus ALL per-document features from STEP 5 (num_words, num_chars, num_sents,\
  \ num_entities, num_triples, num_relation_types_present, num_entity_types_present, entity_type_counts, dominant_entity_type,\
  \ relation_pid_counts, avg_mentions_per_entity, entity_density, mention_density, triple_density, frac_singleton_entities,\
  \ frac_multi_evidence_triples, max_evidence_sentence_gap), 'gold_caveat': 'Re-DocRED has residual false negatives; supports\
  \ RELATIVE operational comparisons only, not an absolute FDR diagonal.' }\n  }\n  Keep field names exactly aligned with\
  \ the standard DATASET output contract {input, output, metadata_fold, ...}. Also write companion files: relation_schema.json\
  \ (96 P-ids), entity_type_schema.json (6 types), and a top-level dataset_meta object (source citation + URLs, split counts,\
  \ seed, cluster scheme, per-cluster doc counts, the gold_caveat, and a one-line statement that this is the shared triple\
  \ space all systems map into at matched recall).\n\nSTEP 9 -- VALIDATE and SPLIT. Author a JSON Schema for the row and run\
  \ the aii-json skill to validate every row in data_out.json against it (fail loudly on any missing/extra field or type mismatch).\
  \ Then use aii-json to generate the full / mini / preview variants (mini = a few rows per cluster incl. at least one pilot\
  \ row; preview = 1-2 illustrative rows with all fields populated). Run the aii-file-size-limit skill on data_out.json (expected\
  \ tens of MB, under 300MB) and split only if it exceeds the limit.\n\nSTEP 10 -- SANITY REPORT (log, do not put in data_out\
  \ as derived stats): print final counts (total rows, confirmatory/pilot/reserve, per-cluster), the realized feature ranges\
  \ per cluster (to confirm cross-document variance exists -- the S5 precondition), the number of unique relation P-ids covered\
  \ vs 96 and unique entity types covered vs 6, and a handful of fully-rendered example rows (text + entities + a few gold\
  \ triples with evidence) for eyeball QA. Confirm no document appears in more than one of confirmatory/pilot/reserve, and\
  \ that every gold triple's head_id/tail_id index a valid entity.\n\nFAILURE SCENARIOS & MITIGATIONS:\n  - HF mirror missing/changed\
  \ -> GitHub raw fallback (Step 1 fallback A/B); assert schema in Step 2 to catch silent format drift.\n  - rel_info.json\
  \ unavailable -> Wikidata wbgetentities API (free, no LLM budget) then hardcoded map (Step 3).\n  - Cluster imbalance (PER-dominant\
  \ dominates) -> collapse rare TIME/NUM into MISC, top up from k-means secondary scheme, or split MISC; always keep >=4 balanced,\
  \ populated clusters (Step 6).\n  - Documents too short/long or too few triples -> eligibility filter in Step 7 (keep ~80-400\
  \ words, >=5 triples) but record length as a feature rather than aggressively discarding.\n  - Empty evidence on re-annotated\
  \ triples -> keep the triple with empty evidence arrays (Step 4c); do not drop.\n  - char_span computation fragile for odd\
  \ tokenization -> leave char_span null but always retain authoritative token pos (Step 4b).\n  - Temptation to manufacture\
  \ negatives/decoys for the pilot -> DO NOT; this is a raw-data artifact. Candidate/decoy/scoring generation is the downstream\
  \ experiment's responsibility (keeps this strictly within DATASET executor scope)."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
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
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
