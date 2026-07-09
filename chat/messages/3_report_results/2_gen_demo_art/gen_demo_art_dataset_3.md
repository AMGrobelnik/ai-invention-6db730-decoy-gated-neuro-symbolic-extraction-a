# gen_demo_art_dataset_3 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_dataset_3` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 13:24:53 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
```

### [2] SYSTEM-USER prompt · 2026-06-16 13:24:59 UTC

````
<conversion_philosophy>
**MINIMAL CHANGES — PRESERVE THE ORIGINAL CODE**

The goal is to make the artifact's code READABLE, UNDERSTANDABLE, and RUNNABLE in a short time
to someone reviewing the research, with the option to easily scale parameters back to original
values for a full run (which can take much longer). Think of this as annotating and reformatting,
not refactoring.

**DO:**
- Split the original script into logical notebook cells (imports, setup, processing, results)
- Add markdown cells BETWEEN code cells explaining what each section does and why
- Add inline comments where the logic is non-obvious
- Add a visualization/summary cell at the end showing key outputs
- Fix hardcoded file paths to use the GitHub data loading pattern

**DO NOT:**
- Rewrite functions or change algorithms
- Rename variables or restructure logic
- Add error handling, type hints, or "improvements" that weren't in the original
- Simplify or "clean up" the original code
- Remove any original comments or logic
- Change the computational approach

The reader should recognize the original script when looking at the notebook — it's the
same code, just split into cells with explanatory markdown between sections.
</conversion_philosophy>

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<task>
Convert this artifact's Python script into a demo notebook with MINIMAL changes to the original code.
Split into cells, add markdown explanations between sections, add a visualization cell at the end.
Output: mini_demo_data.json + code_demo.ipynb (notebook that loads data from GitHub URL)
</task>

<artifact_info>
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
out_demo_files:
- path: data.py
  description: Dataset fetching/generation script
</artifact_info>

<github_repo>
Repo URL: https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a
Raw data URL: https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json

URLs won't work yet — files pushed to GitHub AFTER notebook creation.
Use local fallback pattern so notebook works locally (now) and in Colab (after deployment).
</github_repo>

<data_file_sizes>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_file_sizes>

<install_dependencies_pattern>
Follow the aii-colab skill exactly. It has the install cell pattern, pre-installed package list, numpy 2.0 compat shims, and all Colab-specific rules.
</install_dependencies_pattern>

<data_loading_pattern>
`mini_demo_data.json` = curated subset for the demo.
Use this pattern for Colab compatibility (GitHub URL with local fallback):
```python
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")
```
</data_loading_pattern>

<notebook_structure>
--- Setup ---
Cell 1 (markdown): Title, description, what this artifact does.
Cell 2 (code): Install dependencies — follow the aii-colab skill's install cell pattern exactly. Fill in all packages imported by the artifact's code.
Cell 3 (code): Imports — copy original import block as-is, plus any additional imports needed for the notebook (e.g. matplotlib for visualization).
Cell 4 (code): Data loading helper — use the <data_loading_pattern> above.
Cell 5 (code): `data = load_data()`

--- Config ---
Config cell (code): Define ALL tunable parameters (iterations, epochs, n_samples, hidden_size, etc.) as variables at the top of this cell. Start with the ABSOLUTE MINIMUM values — the smallest that produce any output at all (e.g. 1 iteration, 2 samples, smallest array size). These get gradually increased during testing — see TODOs.

--- Processing ---
Remaining cells: One code cell per logical section of the original script. Add a markdown cell BEFORE each code cell. Copy code as closely as possible, with these changes:
  1. Replace file paths to use the loaded `data` variable.
  2. Use the config variables from the config cell (NOT hardcoded values).
  3. Minimal fixes are allowed if something doesn't work in notebook context (e.g. adjusting paths, removing CLI args, fixing imports), but keep changes to the absolute minimum.

--- Results ---
Visualization cell (code): Print key results in a readable table, plot numeric data with matplotlib if appropriate.
</notebook_structure>

<priority>
WORKING > OPTIMIZED. A small-scale demo that runs correctly is the goal. Once the notebook passes with minimum config values, scale up only if time permits — do NOT spend multiple retries chasing larger parameters. If a working version exists, finish and move on.
</priority>

<max_notebook_total_runtime>600s (10 min)</max_notebook_total_runtime>

<test_environment>
To test-run the notebook in a clean environment (simulating Colab), create a disposable `.nb_env` in your workspace:
```bash
/usr/local/bin/python3.12 -m venv .nb_env
.nb_env/bin/pip install -q pip jupyter ipykernel
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb
rm -rf .nb_env
```
The timeout is set to <max_notebook_total_runtime>. The entire notebook must finish within this time.

What happens: the .venv starts empty (just jupyter). When the notebook's install cell runs, `google.colab` is NOT in sys.modules, so ALL packages get installed — non-Colab packages unconditionally, and Colab packages (numpy, pandas, etc.) at Colab's exact versions via the guard block. The result mirrors Colab's environment as closely as possible. If a cell fails, fix the notebook and re-run.
</test_environment>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.


<todos>
TODO 1. Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.
TODO 2. Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.
TODO 3. Create `mini_demo_data.json`: curated subset from at most ONE dataset (no more than 100 diverse examples). CRITICAL: do NOT read/grep full output file — may crash. Use `head -c 5000` or stream first entries with Python to pick examples.
TODO 4. Create `code_demo.ipynb` via NotebookEdit following <notebook_structure>. Set ALL config parameters to ABSOLUTE MINIMUM values — the smallest that produce any output (e.g. 1 iteration, 2 samples, smallest array sizes). Test-run using <test_environment>. Fix all errors until it passes.
TODO 5. GRADUALLY SCALE (but don't overdo it): increase config params step by step (e.g. ~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful — a working small-scale demo beats a failed large-scale one. If full original params fit within <max_notebook_total_runtime> (10% margin), use them. Otherwise keep whatever works and comment out the true original values. Do NOT spend more than 2-3 scaling rounds.
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DemoExpectedFiles": {
      "description": "Expected output files from code demo notebook generation.",
      "properties": {
        "notebook": {
          "default": "",
          "description": "Path to the generated demo notebook. Example: 'code_demo.ipynb'",
          "title": "Notebook",
          "type": "string"
        },
        "mini_data_file": {
          "default": "",
          "description": "Path to the mini demo data JSON (curated subset). Example: 'mini_demo_data.json'",
          "title": "Mini Data File",
          "type": "string"
        }
      },
      "title": "DemoExpectedFiles",
      "type": "object"
    }
  },
  "description": "Dataset/experiment/evaluation \u2192 Jupyter notebook demo.\n\nTitle and summary come from the parent artifact (gen_art step),\nnot from the demo agent. The agent only outputs expected files.",
  "properties": {
    "out_expected_files": {
      "$ref": "#/$defs/DemoExpectedFiles",
      "description": "All output files you created. Must include the demo notebook."
    }
  },
  "required": [],
  "title": "CodeDemo",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 13:24:59 UTC

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

### [4] ASSISTANT · 2026-06-16 13:25:07 UTC

```
I'll start by setting up my todos and reading the required skills and artifact files.
```

### [5] TOOL CALL — Skill · 2026-06-16 13:25:07 UTC

```
aii-colab
```

### [6] TOOL CALL — Skill · 2026-06-16 13:25:07 UTC

```
aii-long-running-tasks
```

### [7] TOOL RESULT — Skill · 2026-06-16 13:25:07 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [8] TOOL RESULT — Skill · 2026-06-16 13:25:07 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [9] TOOL CALL — Bash · 2026-06-16 13:25:07 UTC

```
List artifact workspace files:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/
```

### [10] TOOL RESULT — Bash · 2026-06-16 13:25:07 UTC

```
{"stdout": "total 15757\ndrwxr-xr-x 7 root root 2040245 Jun 16 07:13 .\ndrwxr-xr-x 7 root root 3000195 Jun 16 06:12 ..\n-rw-r--r-- 1 root root    1271 Jun 16 06:16 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 root root 3445825 Jun 16 07:13 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4236 Jun 16 07:13 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 4 root root 2024334 Jun 16 06:19 .venv\n-rw-r--r-- 1 root root    4466 Jun 16 07:07 README.md\ndrwxr-xr-x 3 root root 1010607 Jun 16 07:06 build\n-rw-r--r-- 1 root root   10970 Jun 16 07:10 data.py\n-rw-r--r-- 1 root root  213550 Jun 16 07:10 data_out.json\n-rw-r--r-- 1 root root    6159 Jun 16 07:10 dataset_meta.json\n-rw-r--r-- 1 root root  213550 Jun 16 07:10 full_data_out.json\ndrwxr-xr-x 2 root root 1003487 Jun 16 06:24 logs\n-rw-r--r-- 1 root root   98348 Jun 16 07:11 mini_data_out.json\n-rw-r--r-- 1 root root   33994 Jun 16 07:11 preview_data_out.json\n-rw-r--r-- 1 root root    1944 Jun 16 07:12 pyproject.toml\ndrwxr-xr-x 7 root root 2015512 Jun 16 06:57 raw\n-rwxr-xr-x 1 root root     554 Jun 16 07:04 regenerate.sh\n-rw-r--r-- 1 root root     154 Jun 16 06:21 requirements.txt\ndrwxr-xr-x 2 root root 1000265 Jun 16 06:57 schema", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] TOOL CALL — Bash · 2026-06-16 13:25:07 UTC

```
List my workspace files:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/
```

### [12] TOOL RESULT — Bash · 2026-06-16 13:25:07 UTC

```
{"stdout": "total 3075\ndrwxr-xr-x 2 root root 1004134 Jun 16 13:24 .\ndrwxr-xr-x 6 root root 2100829 Jun 16 13:24 ..\n-rw-r--r-- 1 root root   42543 Jun 16 13:25 .repl_agent.ptylog", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] ASSISTANT · 2026-06-16 13:25:21 UTC

```
Now let me read the artifact's script, preview data, schema, and metadata.
```

### [14] TOOL CALL — Read · 2026-06-16 13:25:21 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/data.py
```

### [15] TOOL CALL — Read · 2026-06-16 13:25:21 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/preview_data_out.json
```

### [16] TOOL RESULT — Read · 2026-06-16 13:25:21 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/data.py", "content": "#!/usr/bin/env python3\n\"\"\"Canonical standardization entrypoint for the APPLICATION ANCHOR dataset.\n\nBuilds the genre row-sets deterministically from the cached raw/ snapshot\n(no network) and standardizes them into the exp_sel_data_out schema, GROUPED BY\nSOURCE DATASET (each document is ONE example):\n\n  datasets = [ {dataset: \"CUAD\",     examples:[...8 legal docs...]},\n               {dataset: \"Wikinews\", examples:[...8 news docs...]},\n               {dataset: \"GDPR\",     examples:[...5 regulatory EU docs...]},\n               {dataset: \"eCFR\",     examples:[...3 regulatory US docs...]} ]\n\nEvery example carries metadata_fold = genre (enables leave-one-genre-out), a\ncrisp/silver gold_quality flag, per-row license, and the relation vocabulary.\nNO LLM is used in gold construction. Outputs:\n  data_out.json, full_data_out.json, mini_data_out.json, preview_data_out.json,\n  dataset_meta.json.\n\nRun:  python data.py   (or: bash regenerate.sh)\n\"\"\"\nfrom __future__ import annotations\nimport os, sys, json, glob, statistics, hashlib\nfrom pathlib import Path\nfrom collections import Counter, defaultdict\nfrom loguru import logger\n\nROOT = Path(__file__).resolve().parent\nos.environ.setdefault(\"NLTK_DATA\", str(ROOT / \"raw\" / \"nltk_data\"))\nsys.path.insert(0, str(ROOT / \"build\"))\n\nimport build_legal, build_news, build_regulatory  # noqa: E402\n\nSEED = 42\n# stable source-corpus -> dataset-group order\nCORPUS_ORDER = [\"CUAD\", \"Wikinews\", \"GDPR\", \"eCFR\"]\nTOOL_VERSIONS = {\n    \"python\": \"3.12\", \"spacy\": \"3.7.5\", \"spacy_model\": \"en_core_web_sm==3.7.1\",\n    \"nltk\": \"3.9.1 (wordnet, omw-1.4)\", \"numpy\": \"1.26.4\",\n    \"beautifulsoup4\": \"4.12.3 (lxml 5.3.0 parser)\",\n    \"reserved_next_iteration\": \"sentence-transformers all-MiniLM-L6-v2, rank_bm25 \"\n                               \"(NOT used for gold here; reserved for next-iteration \"\n                               \"relation-alignment / retrieval)\",\n}\n\n\ndef corpus_of(source: str) -> str:\n    return source.split(\":\")[0]\n\n\ndef raw_manifest():\n    man = {}\n    cu = ROOT / \"raw\" / \"cuad_data\" / \"CUADv1.json\"\n    if cu.exists():\n        man[\"CUADv1.json\"] = {\"bytes\": cu.stat().st_size,\n                              \"sha256_16\": hashlib.sha256(cu.read_bytes()).hexdigest()[:16]}\n    man[\"gdpr_html_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"gdpr\" / \"art-*.html\")))\n    man[\"wikinews_article_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"wikinews\" / \"article_*.json\")))\n    man[\"ecfr_xml_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"ecfr\" / \"*.xml\")))\n    return man\n\n\ndef build_meta(rows):\n    genres = Counter(r[\"metadata_genre\"] for r in rows)\n    quality = Counter(r[\"metadata_gold_quality\"] for r in rows)\n    qbyg = defaultdict(Counter); cbyg = Counter(); lic = Counter()\n    relvocab = defaultdict(set); lens = []; nfacts = []; nents = []\n    for r in rows:\n        gg = r[\"metadata_genre\"]\n        qbyg[gg][r[\"metadata_gold_quality\"]] += 1\n        cbyg[corpus_of(r[\"metadata_source\"])] += 1\n        lic[r[\"metadata_license\"]] += 1\n        for rel in r[\"metadata_relation_vocab\"]:\n            relvocab[gg].add(rel)\n        lens.append(r[\"metadata_char_length\"]); nfacts.append(r[\"metadata_num_facts\"])\n        nents.append(r[\"metadata_num_entities\"])\n    return {\n        \"name\": \"application_anchor\",\n        \"description\": (\n            \"Genre-faithful APPLICATION anchor: short, professionally-written legal / \"\n            \"news / regulatory documents standardized to a shared (head, relation, tail) \"\n            \"triple schema with char-span provenance, coarse {PER,LOC,ORG,TIME,NUM,MISC} \"\n            \"entity typing, a crisp-vs-silver gold_quality flag, per-row license, and a \"\n            \"genre fold (metadata_fold) for leave-one-genre-out. ONE merged file assembled \"\n            \"from multiple source corpora; the datasets[] array is grouped by source \"\n            \"corpus. Built for a text->FOL->Prolog neuro-symbolic atomic-fact-extraction & \"\n            \"hallucination-control experiment. NO LLM in gold construction (non-circularity).\"),\n        \"schema_per_example\": {\n            \"grouping\": \"datasets[] is grouped by SOURCE CORPUS; each document is ONE example.\",\n            \"input\": \"JSON string: {doc_id, document_text, genre, source, char_length, \"\n                     \"entities:[{name,type in {PER,LOC,ORG,TIME,NUM,MISC},char_span:[s,e]}]}\",\n            \"output\": \"JSON string: {gold_atomic_facts:[{head,relation,tail,\"\n                      \"provenance_char_span:[s,e]}]}\",\n            \"metadata\": \"metadata_fold(genre), metadata_gold_quality(crisp|silver), \"\n                        \"metadata_source, metadata_license, metadata_relation_vocab, \"\n                        \"metadata_char_length, metadata_num_facts, metadata_num_entities, \"\n                        \"metadata_entity_types_fine(spaCy fine NER labels, optional)\",\n        },\n        \"n_documents\": len(rows),\n        \"n_source_datasets\": len(set(corpus_of(r[\"metadata_source\"]) for r in rows)),\n        \"dataset_selection_rationale\": (\n            \"4 source corpora CHOSEN from 7 evaluated. Kept (free license + \"\n            \"genre-faithful short documents + supports deterministic no-LLM gold): \"\n            \"CUAD, Wikinews, GDPR, eCFR. Excluded: REDFM (CC BY-SA-NC, NonCommercial), \"\n            \"ContractNLI-HF (CC BY-NC-SA, NonCommercial), WebRED (free CC BY-SA but \"\n            \"sentence-level TFRecord, not genre-faithful documents), LDC ACE/TACRED \"\n            \"(research-restricted). Count is 4 (not 6) because the plan's HARD \"\n            \"free-license + genre-faithfulness gates legitimately exclude the rest; \"\n            \"the binding deliverable (~24 docs balanced 8/8/8 across 3 genres) is met.\"),\n        \"genre_counts\": dict(genres),\n        \"source_dataset_counts\": dict(cbyg),\n        \"gold_quality_counts\": dict(quality),\n        \"gold_quality_by_genre\": {k: dict(v) for k, v in qbyg.items()},\n        \"license_counts\": dict(lic),\n        \"relation_vocab_by_genre\": {k: sorted(v) for k, v in relvocab.items()},\n        \"total_facts\": sum(nfacts), \"total_entities\": sum(nents),\n        \"facts_per_doc\": {\"min\": min(nfacts), \"max\": max(nfacts),\n                          \"mean\": round(statistics.mean(nfacts), 2)},\n        \"char_length\": {\"min\": min(lens), \"max\": max(lens),\n                        \"mean\": round(statistics.mean(lens), 1),\n                        \"median\": int(statistics.median(lens))},\n        \"sources\": {\n            \"CUAD (legal)\": \"CUAD v1 (theatticusproject) — CC BY 4.0 — human-annotated \"\n                            \"clause spans (CRISP). https://zenodo.org/records/4595826\",\n            \"Wikinews (news)\": \"en.wikinews.org — CC BY 2.5 — deterministic spaCy SVO+5W \"\n                               \"rule-based curation (SILVER).\",\n            \"GDPR (regulatory, EU)\": \"Regulation (EU) 2016/679 (EUR-Lex CELEX:32016R0679; \"\n                                     \"text via gdpr-info.eu) — EUR-Lex free reuse — \"\n                                     \"deterministic structural regex curation (SILVER).\",\n            \"eCFR (regulatory, US)\": \"Electronic Code of Federal Regulations (ecfr.gov) — \"\n                                     \"US Government public domain — deterministic structural \"\n                                     \"regex curation (SILVER).\",\n        },\n        \"evaluated_but_excluded\": {\n            \"REDFM (Babelscape)\": \"CC BY-SA-NC 4.0 (NonCommercial) — fails free-license rule; \"\n                                  \"Wikipedia-genre overlap with the Re-DocRED anchor.\",\n            \"ContractNLI (HF kiddothe2b)\": \"CC BY-NC-SA 4.0 (NonCommercial) — fails free-license rule.\",\n            \"WebRED (google-research)\": \"CC BY-SA 3.0 (usable) but sentence-level TFRecord, not \"\n                                        \"genre-faithful short documents; Wikinews preferred.\",\n            \"LDC ACE / TACRED\": \"research-restricted / non-free — excluded per plan.\",\n        },\n        \"determinism\": {\n            \"seed\": SEED, \"tool_versions\": TOOL_VERSIONS,\n            \"regeneration\": \"Deterministic from cached raw/ with no network: python data.py \"\n                            \"(build_legal+build_news+build_regulatory). Stable sort within \"\n                            \"each source group by doc_id; source groups in fixed order \"\n                            f\"{CORPUS_ORDER}.\",\n            \"raw_cache_manifest\": raw_manifest(),\n        },\n        \"verification\": \"Every entity char_span and fact provenance_char_span is re-verified \"\n                        \"against document_text (build/verify_dataset.py). Value-tail facts: \"\n                        \"tail is a substring of the provenance span; clause/label facts: the \"\n                        \"provenance span is the annotated supporting evidence.\",\n        \"limitations\": \"Legal gold is CRISP (CUAD human annotation). News and regulatory gold \"\n                       \"are SILVER (deterministic rule/structure curation, no LLM): facts are \"\n                       \"span-supported and high-precision but rule-based recall is partial. The \"\n                       \"gold_quality flag carries this per row.\",\n    }\n\n\ndef main():\n    logger.remove(); logger.add(sys.stdout, level=\"INFO\",\n                                format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\n    logger.info(\"building genre row-sets from cached raw/ ...\")\n    rows = build_legal.build() + build_news.build() + build_regulatory.build()\n    logger.info(f\"built {len(rows)} document rows\")\n\n    # group by source corpus (stable order), sort within group by doc_id\n    groups = defaultdict(list)\n    for r in rows:\n        groups[corpus_of(r[\"metadata_source\"])].append(r)\n    datasets = []\n    for c in CORPUS_ORDER:\n        if groups.get(c):\n            ex = sorted(groups[c], key=lambda r: r[\"metadata_doc_id\"])\n            datasets.append({\"dataset\": c, \"examples\": ex})\n    # any unexpected corpus -> append deterministically\n    for c in sorted(groups):\n        if c not in CORPUS_ORDER:\n            datasets.append({\"dataset\": c,\n                             \"examples\": sorted(groups[c], key=lambda r: r[\"metadata_doc_id\"])})\n\n    meta = build_meta(rows)\n    out = {\"metadata\": meta, \"datasets\": datasets}\n    # data_out.json (canonical) and full_data_out.json (identical full copy).\n    # mini/preview variants are produced by the aii-json format script downstream.\n    (ROOT / \"data_out.json\").write_text(json.dumps(out, ensure_ascii=False, indent=2))\n    (ROOT / \"full_data_out.json\").write_text(json.dumps(out, ensure_ascii=False, indent=2))\n    (ROOT / \"dataset_meta.json\").write_text(json.dumps(meta, ensure_ascii=False, indent=2))\n\n    logger.info(f\"datasets(by corpus)={[(d['dataset'], len(d['examples'])) for d in datasets]}\")\n    logger.info(f\"genres={meta['genre_counts']} quality={meta['gold_quality_counts']} \"\n                f\"facts={meta['total_facts']} ents={meta['total_entities']}\")\n    logger.info(\"wrote data_out.json + full_data_out.json + dataset_meta.json\")\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 198, "startLine": 1, "totalLines": 198}}
```

### [17] TOOL RESULT — Read · 2026-06-16 13:25:21 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/preview_data_out.json", "content": "{\n  \"metadata\": {\n    \"name\": \"application_anchor\",\n    \"description\": \"Genre-faithful APPLICATION anchor: short, professionally-written legal / news / regulatory documents standardized to a shared (head, relation, tail) triple schema with char-span provenance, coarse {PER,LOC,ORG,TIME,NUM,MISC} ent... [truncated, 37798 chars total]
```

### [18] ASSISTANT · 2026-06-16 13:25:37 UTC

```
Let me look at the verification script and schema to understand what analysis code I can reuse.
```

### [19] TOOL CALL — Bash · 2026-06-16 13:25:37 UTC

```
List build and schema dirs:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/build/ /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/schema/
```

### [20] TOOL RESULT — Bash · 2026-06-16 13:25:37 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/build/:\ntotal 4016\ndrwxr-xr-x 3 root root 1010607 Jun 16 07:06 .\ndrwxr-xr-x 7 root root 2040245 Jun 16 07:13 ..\ndrwxr-xr-x 2 root root 1005312 Jun 16 07:04 __pycache__\n-rw-r--r-- 1 root root   11353 Jun 16 07:02 build_legal.py\n-rw-r--r-- 1 root root   10149 Jun 16 06:48 build_news.py\n-rw-r--r-- 1 root root   12207 Jun 16 06:48 build_regulatory.py\n-rw-r--r-- 1 root root    8911 Jun 16 07:02 common.py\n-rw-r--r-- 1 root root    6547 Jun 16 06:28 fetch_sources.py\n-rw-r--r-- 1 root root    5054 Jun 16 07:04 verify_dataset.py\n\n/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/schema/:\ntotal 2973\ndrwxr-xr-x 2 root root 1000265 Jun 16 06:57 .\ndrwxr-xr-x 7 root root 2040245 Jun 16 07:13 ..\n-rw-r--r-- 1 root root    2719 Jun 16 06:57 row_payload_schema.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [21] TOOL CALL — Read · 2026-06-16 13:25:37 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/build/verify_dataset.py
```

### [22] TOOL RESULT — Read · 2026-06-16 13:25:37 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/build/verify_dataset.py", "content": "#!/usr/bin/env python3\n\"\"\"Independent, from-scratch verification of the final data_out.json.\n\nRe-checks every invariant the dataset claims, with NO reliance on the build code:\n  1. JSON parse of every input/output string.\n  2. char_length == len(document_text); length band sanity.\n  3. Every entity char_span verifies: document_text[s:e] == name.\n  4. Every entity type in {PER,LOC,ORG,TIME,NUM,MISC}.\n  5. Every fact provenance_char_span valid; value-tail facts have tail in span;\n     EVERY fact's provenance span non-empty.\n  6. Head/tail entity-linking coverage (how many fact endpoints appear in the\n     document text -> the dataset is usable for span-grounded extraction).\n  7. Genre / quality / license balance + relation-vocab report.\nAlso runs a trivial substring \"baseline\" recall to confirm the gold is\nrecoverable from the raw document (signal check, not an LLM).\n\"\"\"\nfrom __future__ import annotations\nimport json\nfrom pathlib import Path\nfrom collections import Counter, defaultdict\n\nROOT = Path(__file__).resolve().parent.parent\nCOARSE = {\"PER\", \"LOC\", \"ORG\", \"TIME\", \"NUM\", \"MISC\"}\n\n\ndef main():\n    data = json.loads((ROOT / \"data_out.json\").read_text())\n    assert \"datasets\" in data and len(data[\"datasets\"]) >= 1\n    exs = [e for d in data[\"datasets\"] for e in d[\"examples\"]]\n    group_sizes = {d[\"dataset\"]: len(d[\"examples\"]) for d in data[\"datasets\"]}\n    errors, warns = [], []\n    n_ent = n_ent_ok = 0\n    n_fact = n_fact_tail_in_span = 0\n    head_linked = tail_linked = 0\n    genres, quality, lic = Counter(), Counter(), Counter()\n    rels = Counter()\n    type_counts = Counter()\n    lens = []\n\n    for ex in exs:\n        inp = json.loads(ex[\"input\"])\n        out = json.loads(ex[\"output\"])\n        did = inp[\"doc_id\"]\n        dt = inp[\"document_text\"]\n        genres[inp[\"genre\"]] += 1\n        quality[ex[\"metadata_gold_quality\"]] += 1\n        lic[ex[\"metadata_license\"]] += 1\n        lens.append(len(dt))\n\n        # length consistency\n        if inp[\"char_length\"] != len(dt):\n            errors.append(f\"{did}: char_length {inp['char_length']} != len {len(dt)}\")\n        if ex[\"metadata_char_length\"] != len(dt):\n            errors.append(f\"{did}: metadata_char_length mismatch\")\n        if not (1100 <= len(dt) <= 3600):\n            warns.append(f\"{did}: length {len(dt)} outside ~1150-3550 band\")\n\n        ent_surfaces = set()\n        for e in inp[\"entities\"]:\n            n_ent += 1\n            s, ee = e[\"char_span\"]\n            type_counts[e[\"type\"]] += 1\n            if e[\"type\"] not in COARSE:\n                errors.append(f\"{did}: bad entity type {e['type']}\")\n            if 0 <= s <= ee <= len(dt) and dt[s:ee] == e[\"name\"]:\n                n_ent_ok += 1\n                ent_surfaces.add(e[\"name\"])\n            else:\n                errors.append(f\"{did}: entity span FAIL {e['name']!r} {e['char_span']}\")\n\n        facts = out[\"gold_atomic_facts\"]\n        if len(facts) < 3:\n            warns.append(f\"{did}: only {len(facts)} facts\")\n        for f in facts:\n            n_fact += 1\n            rels[f[\"relation\"]] += 1\n            s, ee = f[\"provenance_char_span\"]\n            if not (0 <= s < ee <= len(dt)):\n                errors.append(f\"{did}: bad provenance span {f['provenance_char_span']}\")\n                continue\n            prov = dt[s:ee]\n            if not prov.strip():\n                errors.append(f\"{did}: empty provenance for {f}\")\n            if f[\"tail\"] in prov:\n                n_fact_tail_in_span += 1\n            # entity-linking coverage: do head/tail appear in the document?\n            if f[\"head\"] in dt:\n                head_linked += 1\n            if f[\"tail\"] in dt:\n                tail_linked += 1\n\n    print(\"=\" * 64)\n    print(f\"documents: {len(exs)}  | source-dataset groups: {group_sizes}\")\n    print(f\"genres={dict(genres)}\")\n    print(f\"gold_quality={dict(quality)}\")\n    print(f\"licenses:\")\n    for k, v in lic.items():\n        print(f\"   {v:2d}  {k[:70]}\")\n    print(f\"char_length: min={min(lens)} max={max(lens)} mean={sum(lens)//len(lens)}\")\n    print(\"-\" * 64)\n    print(f\"entities: {n_ent} | spans verified: {n_ent_ok}/{n_ent} \"\n          f\"({100*n_ent_ok/n_ent:.1f}%)\")\n    print(f\"entity type dist: {dict(type_counts)}\")\n    print(f\"facts: {n_fact} | tail-in-provenance: {n_fact_tail_in_span}/{n_fact} \"\n          f\"({100*n_fact_tail_in_span/n_fact:.1f}%) [rest are clause/label facts]\")\n    print(f\"fact head appears in doc: {head_linked}/{n_fact} ({100*head_linked/n_fact:.1f}%)\")\n    print(f\"fact tail appears in doc: {tail_linked}/{n_fact} ({100*tail_linked/n_fact:.1f}%)\")\n    print(f\"distinct relations: {len(rels)}\")\n    print(f\"top relations: {rels.most_common(12)}\")\n    print(\"-\" * 64)\n    print(f\"ERRORS: {len(errors)}\")\n    for e in errors[:30]:\n        print(\"   ERR\", e)\n    print(f\"WARNINGS: {len(warns)}\")\n    for w in warns[:20]:\n        print(\"   warn\", w)\n    print(\"=\" * 64)\n    print(\"RESULT:\", \"PASS — all spans/types/lengths verified\" if not errors\n          else f\"FAIL — {len(errors)} errors\")\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 124, "startLine": 1, "totalLines": 124}}
```

### [23] ASSISTANT · 2026-06-16 13:26:25 UTC

```
This is a dataset artifact. The ideal "original script" to convert is `verify_dataset.py` (pure-Python analysis of the dataset's guarantees) plus the `build_meta`/`corpus_of` analysis functions from `data.py`. Both run with zero heavy dependencies and demonstrate the dataset. Let me check the schema and the mini file's structure first.
```

### [24] TOOL CALL — Read · 2026-06-16 13:26:25 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/schema/row_payload_schema.json
```

### [25] TOOL RESULT — Read · 2026-06-16 13:26:25 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/schema/row_payload_schema.json", "content": "{\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\",\n  \"title\": \"Application-anchor row payloads (the JSON-encoded input and output strings)\",\n  \"description\": \"Each example's `input` and `output` fields are JSON STRINGS. After json.loads, they must satisfy input_payload / output_payload below. This is the inner contract aligned to the (head, relation, tail) space and {PER,LOC,ORG,TIME,NUM,MISC} typing of the dependency spec (research_out.json).\",\n  \"definitions\": {\n    \"input_payload\": {\n      \"type\": \"object\",\n      \"required\": [\"doc_id\", \"document_text\", \"genre\", \"source\", \"char_length\", \"entities\"],\n      \"additionalProperties\": false,\n      \"properties\": {\n        \"doc_id\": {\"type\": \"string\"},\n        \"document_text\": {\"type\": \"string\", \"description\": \"verbatim native document (UTF-8)\"},\n        \"genre\": {\"enum\": [\"legal\", \"news\", \"regulatory\"]},\n        \"source\": {\"type\": \"string\", \"description\": \"corpus name + record id\"},\n        \"char_length\": {\"type\": \"integer\", \"description\": \"== len(document_text)\"},\n        \"entities\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"required\": [\"name\", \"type\", \"char_span\"],\n            \"additionalProperties\": false,\n            \"properties\": {\n              \"name\": {\"type\": \"string\"},\n              \"type\": {\"enum\": [\"PER\", \"LOC\", \"ORG\", \"TIME\", \"NUM\", \"MISC\"]},\n              \"char_span\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}, \"minItems\": 2, \"maxItems\": 2,\n                            \"description\": \"[start,end] with document_text[start:end] == name\"}\n            }\n          }\n        }\n      }\n    },\n    \"output_payload\": {\n      \"type\": \"object\",\n      \"required\": [\"gold_atomic_facts\"],\n      \"additionalProperties\": false,\n      \"properties\": {\n        \"gold_atomic_facts\": {\n          \"type\": \"array\",\n          \"minItems\": 1,\n          \"items\": {\n            \"type\": \"object\",\n            \"required\": [\"head\", \"relation\", \"tail\", \"provenance_char_span\"],\n            \"additionalProperties\": false,\n            \"properties\": {\n              \"head\": {\"type\": \"string\", \"description\": \"subject surface (reuses an entity surface form)\"},\n              \"relation\": {\"type\": \"string\", \"description\": \"open-vocab string from the documented per-genre controlled vocabulary\"},\n              \"tail\": {\"type\": \"string\", \"description\": \"object surface (entity/value) or normalized clause-type token\"},\n              \"provenance_char_span\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}, \"minItems\": 2, \"maxItems\": 2,\n                                       \"description\": \"[start,end] containing the surface evidence supporting the fact\"}\n            }\n          }\n        }\n      }\n    }\n  }\n}\n", "numLines": 57, "startLine": 1, "totalLines": 57}}
```

### [26] TOOL CALL — Bash · 2026-06-16 13:26:25 UTC

```
Inspect mini_data_out.json structure:
head -c 1200 /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json; echo; echo "=== top-level keys ==="; python3 -c "import json; d=json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json')); print(list(d.keys())); print([(g['dataset'], len(g['examples'])) for g in d['datasets']])"
```

### [27] TOOL RESULT — Bash · 2026-06-16 13:26:25 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"name\": \"application_anchor\",\n    \"description\": \"Genre-faithful APPLICATION anchor: short, professionally-written legal / news / regulatory documents standardized to a shared (head, relation, tail) triple schema with char-span provenance, coarse {PER,LOC,ORG,TIME,NUM,MISC} entity typing, a crisp-vs-silver gold_quality flag, per-row license, and a genre fold (metadata_fold) for leave-one-genre-out. ONE merged file assembled from multiple source corpora; the datasets[] array is grouped by source corpus. Built for a text->FOL->Prolog neuro-symbolic atomic-fact-extraction & hallucination-control experiment. NO LLM in gold construction (non-circularity).\",\n    \"schema_per_example\": {\n      \"grouping\": \"datasets[] is grouped by SOURCE CORPUS; each document is ONE example.\",\n      \"input\": \"JSON string: {doc_id, document_text, genre, source, char_length, entities:[{name,type in {PER,LOC,ORG,TIME,NUM,MISC},char_span:[s,e]}]}\",\n      \"output\": \"JSON string: {gold_atomic_facts:[{head,relation,tail,provenance_char_span:[s,e]}]}\",\n      \"metadata\": \"metadata_fold(genre), metadata_gold_quality(crisp|silver), metadata_source, metadata_license, metadata_relation_vocab, meta\n=== top-level keys ===\n['metadata', 'datasets']\n[('CUAD', 3), ('Wikinews', 3), ('GDPR', 3), ('eCFR', 3)]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [28] ASSISTANT · 2026-06-16 13:27:15 UTC

```
The existing `mini_data_out.json` is already an ideal curated subset: 12 examples (3 per corpus group), full untruncated strings, all genres represented, plus the metadata block. I'll use it as `mini_demo_data.json`. Let me copy it and load the NotebookEdit tool schema.
```

### [29] TOOL CALL — Bash · 2026-06-16 13:27:15 UTC

```
Copy mini data to workspace and verify:
cp /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/mini_demo_data.json
python3 -c "
import json
p='/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/mini_demo_data.json'
d=json.load(open(p))
exs=[e for g in d['datasets'] for e in g['examples']]
print('top keys:', list(d.keys()))
print('groups:', [(g['dataset'], len(g['examples'])) for g in d['datasets']])
print('total examples:', len(exs))
import os; print('bytes:', os.path.getsize(p))
"
```

### [30] TOOL CALL — ToolSearch · 2026-06-16 13:27:15 UTC

```
{'query': 'select:NotebookEdit', 'max_results': 3}
```

### [31] TOOL RESULT — Bash · 2026-06-16 13:27:15 UTC

```
{"stdout": "top keys: ['metadata', 'datasets']\ngroups: [('CUAD', 3), ('Wikinews', 3), ('GDPR', 3), ('eCFR', 3)]\ntotal examples: 12\nbytes: 98348", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [32] TOOL RESULT — ToolSearch · 2026-06-16 13:27:15 UTC

```
{"matches": ["NotebookEdit"], "query": "select:NotebookEdit", "total_deferred_tools": 20}
```

### [33] ASSISTANT · 2026-06-16 13:30:01 UTC

```
Both `verify_dataset.py` and `data.py`'s `build_meta` are pure-Python analysis tools (stdlib only) — perfect to convert faithfully. `mini_demo_data.json` (12 examples, all genres) is ready. Now I'll build the notebook via a Python generator script to avoid JSON-escaping errors.
```

### [34] TOOL CALL — Write · 2026-06-16 13:30:01 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/build_nb.py

#!/usr/bin/env python3
"""Generate code_demo.ipynb for the Application-Anchor dataset demo.

The demo faithfully reuses the artifact's OWN analysis code with minimal changes:
  * verify_dataset.py  -> the verification cell (re-checks every span/type/length
    invariant the dataset claims)
  * data.py build_meta() / corpus_of()  -> the composition-summary cell

Only file-path / CLI plumbing is changed so the code runs against the
GitHub-hosted mini_demo_data.json instead of the local data_out.json.
"""
import json

NB_PATH = "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/code_demo.ipynb"

cells = []


def md(cid, text):
    cells.append({"cell_type": "markdown", "id": cid, "metadata": {}, "source": text})


def code(cid, text):
    cells.append({"cell_type": "code", "id": cid, "metadata": {},
                  "execution_count": None, "outputs": [], "source": text})


# ----------------------------------------------------------------------------- title
md("md-title", """\
# Application Anchor — 24 short legal / news / regulatory docs (triple gold + provenance)

This notebook is a **runnable demo of the `Application Anchor` dataset**: a merged,
schema-validated corpus of short, professionally-written documents standardized to a
shared **`(head, relation, tail)`** triple space with **character-span provenance** and
coarse **`{PER, LOC, ORG, TIME, NUM, MISC}`** entity typing.

Each document is **one example**. The dataset is grouped by source corpus:

| Genre | Source corpus | Gold quality | License |
|-------|---------------|--------------|---------|
| legal | CUAD v1 (human-annotated clause spans) | **crisp** | CC BY 4.0 |
| news | Wikinews (deterministic spaCy SVO+5W) | silver | CC BY 2.5 |
| regulatory (EU) | GDPR / Reg (EU) 2016/679 | silver | EUR-Lex free reuse |
| regulatory (US) | eCFR | silver | US public domain |

It is the genre-faithful real-document slice that a downstream
**text → FOL → Prolog neuro-symbolic atomic-fact-extraction & hallucination-control**
experiment depends on. **No LLM is used anywhere in gold construction** (this preserves
non-circularity for the next-iteration hallucination experiment).

**What this demo does** — it loads a 12-document subset (3 per source corpus, all 3
genres) and runs the dataset's *own* tooling on it:

1. Inspect the per-example schema (the JSON-string `input` / `output` payloads).
2. **`verify_dataset.py`** — independently re-check every entity char-span, every fact
   provenance span, entity/type validity, and head/tail entity-linking coverage.
3. **`data.py : build_meta()`** — recompute the dataset composition summary.
4. Visualize the composition (genre / entity-type / relation / facts distributions).
""")

# ----------------------------------------------------------------------------- install
md("md-install", "## Setup\n\nInstall dependencies. On Colab the core scientific packages are "
   "pre-installed, so they are only installed locally (at Colab's exact versions) to mirror "
   "the Colab environment. The dataset's analysis code itself is pure Python standard library.")

code("code-install", """\
import subprocess, sys
def _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])

# matplotlib + pandas are pre-installed on Colab -> only install locally (Colab's versions).
# (The verification / build_meta code uses only the Python standard library.)
if 'google.colab' not in sys.modules:
    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')
""")

# ----------------------------------------------------------------------------- imports
md("md-imports", "Imports. The first block is copied verbatim from the artifact's "
   "`data.py` / `verify_dataset.py` (the `loguru` logger is dropped — it was only used by "
   "`data.py:main()`, which rebuilds the corpus from a raw snapshot and is not part of this "
   "demo). The second block adds plotting / table helpers for the notebook.")

code("code-imports", """\
# --- original imports from data.py / verify_dataset.py ---
from __future__ import annotations
import os, sys, json, glob, statistics, hashlib
from pathlib import Path
from collections import Counter, defaultdict

# --- added for the notebook demo (tables + plots) ---
import pandas as pd
import matplotlib.pyplot as plt
""")

# ----------------------------------------------------------------------------- data load
md("md-loader", "### Load the dataset\n\nLoads the curated demo subset from GitHub, with a local "
   "fallback to `mini_demo_data.json` so the notebook works both in Colab (after deployment) and "
   "locally (now).")

code("code-loader", """\
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")
""")

code("code-loaddata", """\
data = load_data()
print("top-level keys :", list(data.keys()))
print("source corpora :", [(g["dataset"], len(g["examples"])) for g in data["datasets"]])
print("dataset name   :", data["metadata"]["name"])
""")

# ----------------------------------------------------------------------------- config
md("md-config", "## Config\n\nAll tunable demo parameters live here. `N_PER_GROUP` controls how "
   "many documents are taken from **each** source corpus (the curated demo file holds 3 per "
   "corpus = 12 docs across all 3 genres; the full dataset has 8 per genre = 24). Start at the "
   "minimum and scale up — the whole demo runs in well under a second at any setting.")

code("code-config", """\
# --- tunable demo parameters (start minimal, scale up freely) ---
N_PER_GROUP = 3          # docs to take from EACH source corpus. mini file has 3/group (max).
N_PREVIEW   = 1          # how many full example payloads to print in detail

# --- constants copied from the artifact's verify_dataset.py / data.py ---
COARSE       = {"PER", "LOC", "ORG", "TIME", "NUM", "MISC"}   # coarse entity-type set
SEED         = 42                                             # data.py determinism seed
CORPUS_ORDER = ["CUAD", "Wikinews", "GDPR", "eCFR"]           # stable source-group order
TOOL_VERSIONS = {
    "python": "3.12", "spacy": "3.7.5", "spacy_model": "en_core_web_sm==3.7.1",
    "nltk": "3.9.1 (wordnet, omw-1.4)", "numpy": "1.26.4",
    "beautifulsoup4": "4.12.3 (lxml 5.3.0 parser)",
    "reserved_next_iteration": "sentence-transformers all-MiniLM-L6-v2, rank_bm25 "
                               "(NOT used for gold here; reserved for next-iteration "
                               "relation-alignment / retrieval)",
}
""")

# ----------------------------------------------------------------------------- flatten
md("md-flatten", "## Build the document row-set\n\nThe published file groups examples by source "
   "corpus (`datasets[]`). Flatten it back into a flat list of document *rows*, taking the first "
   "`N_PER_GROUP` documents from each corpus. Each row is **one document = one example**.")

code("code-flatten", """\
rows = []
for group in data["datasets"]:
    rows.extend(group["examples"][:N_PER_GROUP])

print(f"using {len(rows)} document rows from {len(data['datasets'])} source corpora")
print("per-corpus counts:",
      [(g["dataset"], min(N_PER_GROUP, len(g["examples"]))) for g in data["datasets"]])
""")

# ----------------------------------------------------------------------------- inspect schema
md("md-inspect", "## Inspect the per-example schema\n\nEach example's `input` and `output` are "
   "**JSON strings**. After `json.loads`:\n\n* **input**  → `{doc_id, document_text, genre, "
   "source, char_length, entities:[{name, type, char_span}]}`\n* **output** → `{gold_atomic_facts:"
   "[{head, relation, tail, provenance_char_span}]}`\n\nThe `corpus_of` helper below is copied "
   "verbatim from `data.py`.")

code("code-inspect", """\
def corpus_of(source: str) -> str:        # copied verbatim from data.py
    return source.split(":")[0]

for ex in rows[:N_PREVIEW]:
    inp = json.loads(ex["input"])         # input is a JSON STRING
    out = json.loads(ex["output"])        # output is a JSON STRING
    print("=" * 78)
    print("doc_id      :", inp["doc_id"], "| genre:", inp["genre"], "| corpus:", corpus_of(ex["metadata_source"]))
    print("gold_quality:", ex["metadata_gold_quality"], "| license:", ex["metadata_license"][:48], "...")
    print("char_length :", inp["char_length"],
          "| #entities:", len(inp["entities"]), "| #facts:", len(out["gold_atomic_facts"]))
    print("-- document_text (first 280 chars) --")
    print("  ", inp["document_text"][:280].replace("\\n", " "))
    print("-- first 5 typed entities (name | coarse type | char_span -> verbatim slice) --")
    for e in inp["entities"][:5]:
        s, end = e["char_span"]
        print(f"   {e['name']!r:>42}  {e['type']:5} {e['char_span']}  ->  {inp['document_text'][s:end]!r}")
    print("-- gold_atomic_facts: head -[relation]-> tail (with provenance span) --")
    for f in out["gold_atomic_facts"]:
        print(f"   {f['head']!r} -[{f['relation']}]-> {f['tail']!r}   prov={f['provenance_char_span']}")
""")

# ----------------------------------------------------------------------------- verify
md("md-verify", "## Verify every invariant (`verify_dataset.py`)\n\nThis cell is the core of the "
   "artifact's **independent** verifier (`build/verify_dataset.py`), adapted only to iterate over "
   "the loaded `rows` instead of reading `data_out.json` from disk. It re-checks, from scratch, "
   "every claim the dataset makes:\n\n1. JSON-parse every `input` / `output` string.\n2. "
   "`char_length == len(document_text)` and length-band sanity.\n3. Every entity `char_span` "
   "satisfies `document_text[s:e] == name`.\n4. Every entity type is in the coarse set.\n5. Every "
   "fact provenance span is valid & non-empty; value-tail facts have `tail` inside the span.\n6. "
   "Head/tail entity-linking coverage (how many fact endpoints appear in the document text).")

code("code-verify", """\
# --- verify_dataset.py main(), adapted to run over the loaded `rows` ---
exs = rows
group_sizes = {g["dataset"]: min(N_PER_GROUP, len(g["examples"])) for g in data["datasets"]}
errors, warns = [], []
n_ent = n_ent_ok = 0
n_fact = n_fact_tail_in_span = 0
head_linked = tail_linked = 0
genres, quality, lic = Counter(), Counter(), Counter()
rels = Counter()
type_counts = Counter()
lens = []

for ex in exs:
    inp = json.loads(ex["input"])
    out = json.loads(ex["output"])
    did = inp["doc_id"]
    dt = inp["document_text"]
    genres[inp["genre"]] += 1
    quality[ex["metadata_gold_quality"]] += 1
    lic[ex["metadata_license"]] += 1
    lens.append(len(dt))

    # length consistency
    if inp["char_length"] != len(dt):
        errors.append(f"{did}: char_length {inp['char_length']} != len {len(dt)}")
    if ex["metadata_char_length"] != len(dt):
        errors.append(f"{did}: metadata_char_length mismatch")
    if not (1100 <= len(dt) <= 3600):
        warns.append(f"{did}: length {len(dt)} outside ~1150-3550 band")

    ent_surfaces = set()
    for e in inp["entities"]:
        n_ent += 1
        s, ee = e["char_span"]
        type_counts[e["type"]] += 1
        if e["type"] not in COARSE:
            errors.append(f"{did}: bad entity type {e['type']}")
        if 0 <= s <= ee <= len(dt) and dt[s:ee] == e["name"]:
            n_ent_ok += 1
            ent_surfaces.add(e["name"])
        else:
            errors.append(f"{did}: entity span FAIL {e['name']!r} {e['char_span']}")

    facts = out["gold_atomic_facts"]
    if len(facts) < 3:
        warns.append(f"{did}: only {len(facts)} facts")
    for f in facts:
        n_fact += 1
        rels[f["relation"]] += 1
        s, ee = f["provenance_char_span"]
        if not (0 <= s < ee <= len(dt)):
            errors.append(f"{did}: bad provenance span {f['provenance_char_span']}")
            continue
        prov = dt[s:ee]
        if not prov.strip():
            errors.append(f"{did}: empty provenance for {f}")
        if f["tail"] in prov:
            n_fact_tail_in_span += 1
        # entity-linking coverage: do head/tail appear in the document?
        if f["head"] in dt:
            head_linked += 1
        if f["tail"] in dt:
            tail_linked += 1

print("=" * 64)
print(f"documents: {len(exs)}  | source-dataset groups: {group_sizes}")
print(f"genres={dict(genres)}")
print(f"gold_quality={dict(quality)}")
print("licenses:")
for k, v in lic.items():
    print(f"   {v:2d}  {k[:70]}")
print(f"char_length: min={min(lens)} max={max(lens)} mean={sum(lens)//len(lens)}")
print("-" * 64)
print(f"entities: {n_ent} | spans verified: {n_ent_ok}/{n_ent} ({100*n_ent_ok/n_ent:.1f}%)")
print(f"entity type dist: {dict(type_counts)}")
print(f"facts: {n_fact} | tail-in-provenance: {n_fact_tail_in_span}/{n_fact} "
      f"({100*n_fact_tail_in_span/n_fact:.1f}%) [rest are clause/label facts]")
print(f"fact head appears in doc: {head_linked}/{n_fact} ({100*head_linked/n_fact:.1f}%)")
print(f"fact tail appears in doc: {tail_linked}/{n_fact} ({100*tail_linked/n_fact:.1f}%)")
print(f"distinct relations: {len(rels)}")
print(f"top relations: {rels.most_common(12)}")
print("-" * 64)
print(f"ERRORS: {len(errors)}")
for e in errors[:30]:
    print("   ERR", e)
print(f"WARNINGS: {len(warns)}")
for w in warns[:20]:
    print("   warn", w)
print("=" * 64)
print("RESULT:", "PASS - all spans/types/lengths verified" if not errors
      else f"FAIL - {len(errors)} errors")
""")

# ----------------------------------------------------------------------------- build_meta
md("md-meta", "## Recompute the composition summary (`data.py : build_meta`)\n\nThis cell is the "
   "artifact's own `build_meta()` from `data.py`, copied with one minimal change: `ROOT` points "
   "at the current working directory (the original used the script's own folder to fingerprint "
   "the raw snapshot). The `raw/` snapshot is not shipped with the demo, so the determinism "
   "manifest simply reports an empty cache — every *statistical* field is still computed live "
   "from the loaded rows.")

code("code-meta", """\
ROOT = Path.cwd()        # minimal path fix: original used the script's own directory


def raw_manifest():      # copied from data.py (reports the cached raw/ snapshot, if present)
    man = {}
    cu = ROOT / "raw" / "cuad_data" / "CUADv1.json"
    if cu.exists():
        man["CUADv1.json"] = {"bytes": cu.stat().st_size,
                              "sha256_16": hashlib.sha256(cu.read_bytes()).hexdigest()[:16]}
    man["gdpr_html_files"] = len(glob.glob(str(ROOT / "raw" / "gdpr" / "art-*.html")))
    man["wikinews_article_files"] = len(glob.glob(str(ROOT / "raw" / "wikinews" / "article_*.json")))
    man["ecfr_xml_files"] = len(glob.glob(str(ROOT / "raw" / "ecfr" / "*.xml")))
    return man


def build_meta(rows):    # copied verbatim from data.py
    genres = Counter(r["metadata_genre"] for r in rows)
    quality = Counter(r["metadata_gold_quality"] for r in rows)
    qbyg = defaultdict(Counter); cbyg = Counter(); lic = Counter()
    relvocab = defaultdict(set); lens = []; nfacts = []; nents = []
    for r in rows:
        gg = r["metadata_genre"]
        qbyg[gg][r["metadata_gold_quality"]] += 1
        cbyg[corpus_of(r["metadata_source"])] += 1
        lic[r["metadata_license"]] += 1
        for rel in r["metadata_relation_vocab"]:
            relvocab[gg].add(rel)
        lens.append(r["metadata_char_length"]); nfacts.append(r["metadata_num_facts"])
        nents.append(r["metadata_num_entities"])
    return {
        "name": "application_anchor",
        "n_documents": len(rows),
        "n_source_datasets": len(set(corpus_of(r["metadata_source"]) for r in rows)),
        "genre_counts": dict(genres),
        "source_dataset_counts": dict(cbyg),
        "gold_quality_counts": dict(quality),
        "gold_quality_by_genre": {k: dict(v) for k, v in qbyg.items()},
        "license_counts": dict(lic),
        "relation_vocab_by_genre": {k: sorted(v) for k, v in relvocab.items()},
        "total_facts": sum(nfacts), "total_entities": sum(nents),
        "facts_per_doc": {"min": min(nfacts), "max": max(nfacts),
                          "mean": round(statistics.mean(nfacts), 2)},
        "char_length": {"min": min(lens), "max": max(lens),
                        "mean": round(statistics.mean(lens), 1),
                        "median": int(statistics.median(lens))},
        "determinism": {"seed": SEED, "tool_versions": TOOL_VERSIONS,
                        "raw_cache_manifest": raw_manifest()},
    }


meta = build_meta(rows)
for k in ["n_documents", "n_source_datasets", "genre_counts", "source_dataset_counts",
          "gold_quality_counts", "gold_quality_by_genre", "license_counts",
          "total_facts", "total_entities", "facts_per_doc", "char_length"]:
    print(f"{k:24}: {meta[k]}")
print("\\nrelation_vocab_by_genre:")
for g, v in meta["relation_vocab_by_genre"].items():
    print(f"   {g:11}: {v}")
""")

# ----------------------------------------------------------------------------- viz
md("md-viz", "## Visualize the dataset\n\nA per-document summary table plus four composition charts: "
   "documents per genre, coarse entity-type distribution, total gold facts per genre, and the most "
   "frequent relations. (`type_counts` and `rels` were computed in the verification cell above.)")

code("code-viz", """\
# per-document summary table
recs = []
for ex in rows:
    inp = json.loads(ex["input"]); out = json.loads(ex["output"])
    recs.append({
        "doc_id": inp["doc_id"], "corpus": corpus_of(ex["metadata_source"]),
        "genre": inp["genre"], "quality": ex["metadata_gold_quality"],
        "char_length": inp["char_length"],
        "n_entities": len(inp["entities"]), "n_facts": len(out["gold_atomic_facts"]),
    })
df = pd.DataFrame(recs)
print("Per-document summary:")
print(df.to_string(index=False))

# four composition charts
fig, ax = plt.subplots(2, 2, figsize=(13, 8))

df["genre"].value_counts().reindex(["legal", "news", "regulatory"]).plot(
    kind="bar", ax=ax[0, 0], color="steelblue", rot=0)
ax[0, 0].set_title("Documents per genre"); ax[0, 0].set_ylabel("# documents")

pd.Series(dict(type_counts)).reindex(sorted(COARSE)).fillna(0).plot(
    kind="bar", ax=ax[0, 1], color="darkorange", rot=0)
ax[0, 1].set_title("Coarse entity-type distribution"); ax[0, 1].set_ylabel("# entities")

df.groupby("genre")["n_facts"].sum().reindex(["legal", "news", "regulatory"]).plot(
    kind="bar", ax=ax[1, 0], color="seagreen", rot=0)
ax[1, 0].set_title("Total gold atomic-facts per genre"); ax[1, 0].set_ylabel("# facts")

top_rel = pd.Series(dict(rels.most_common(10)))[::-1]
top_rel.plot(kind="barh", ax=ax[1, 1], color="mediumpurple")
ax[1, 1].set_title("Top relations (gold vocabulary)"); ax[1, 1].set_xlabel("# facts")

plt.tight_layout()
plt.savefig("demo_summary.png", dpi=90, bbox_inches="tight")
plt.show()
print("\\nSaved figure -> demo_summary.png")
""")

# ----------------------------------------------------------------------------- summary md
md("md-done", """\
## Summary

The demo loaded a 12-document, all-genre subset of the **Application Anchor** dataset and ran the
artifact's own tooling on it:

* **Verification** independently confirmed every entity char-span (`document_text[s:e] == name`),
  every fact provenance span, coarse-type validity, and head/tail entity-linking coverage — with
  **zero errors**, reproducing the dataset's headline guarantee.
* **`build_meta`** recomputed the composition: balanced genres, crisp (legal) vs silver
  (news/regulatory) gold, per-genre relation vocabularies, and char-length / facts-per-doc stats.

To scale up, raise `N_PER_GROUP` in the Config cell (3 = all of the demo file). The full dataset
(`full_data_out.json`, 24 docs, 8 per genre, 140 gold facts) is regenerated deterministically and
byte-identically from a cached raw snapshot via `python data.py` — **no network and no LLM** in
gold construction, which is what keeps the downstream hallucination-control experiment
non-circular.
""")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

with open(NB_PATH, "w") as f:
    json.dump(nb, f, indent=1)
print("wrote", NB_PATH, "with", len(cells), "cells")
```

### [35] TOOL RESULT — Write · 2026-06-16 13:30:01 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/build_nb.py", "content": "#!/usr/bin/env python3\n\"\"\"Generate code_demo.ipynb for the Application-Anchor dataset demo.\n\nThe demo faithfully reuses the artifact's OWN analysis code with minimal changes:\n  * verify_dataset.py  -> the verification cell (re-checks every span/type/length\n    invariant the dataset claims)\n  * data.py build_meta() / corpus_of()  -> the composition-summary cell\n\nOnly file-path / CLI plumbing is changed so the code runs against the\nGitHub-hosted mini_demo_data.json instead of the local data_out.json.\n\"\"\"\nimport json\n\nNB_PATH = \"/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/code_demo.ipynb\"\n\ncells = []\n\n\ndef md(cid, text):\n    cells.append({\"cell_type\": \"markdown\", \"id\": cid, \"metadata\": {}, \"source\": text})\n\n\ndef code(cid, text):\n    cells.append({\"cell_type\": \"code\", \"id\": cid, \"metadata\": {},\n                  \"execution_count\": None, \"outputs\": [], \"source\": text})\n\n\n# ----------------------------------------------------------------------------- title\nmd(\"md-title\", \"\"\"\\\n# Application Anchor — 24 short legal / news / regulatory docs (triple gold + provenance)\n\nThis notebook is a **runnable demo of the `Application Anchor` dataset**: a merged,\nschema-validated corpus of short, professionally-written documents standardized to a\nshared **`(head, relation, tail)`** triple space with **character-span provenance** and\ncoarse **`{PER, LOC, ORG, TIME, NUM, MISC}`** entity typing.\n\nEach document is **one example**. The dataset is grouped by source corpus:\n\n| Genre | Source corpus | Gold quality | License |\n|-------|---------------|--------------|---------|\n| legal | CUAD v1 (human-annotated clause spans) | **crisp** | CC BY 4.0 |\n| news | Wikinews (deterministic spaCy SVO+5W) | silver | CC BY 2.5 |\n| regulatory (EU) | GDPR / Reg (EU) 2016/679 | silver | EUR-Lex free reuse |\n| regulatory (US) | eCFR | silver | US public domain |\n\nIt is the genre-faithful real-document slice that a downstream\n**text → FOL → Prolog neuro-symbolic atomic-fact-extraction & hallucination-control**\nexperiment depends on. **No LLM is used anywhere in gold construction** (this preserves\nnon-circularity for the next-iteration hallucination experiment).\n\n**What this demo does** — it loads a 12-document subset (3 per source corpus, all 3\ngenres) and runs the dataset's *own* tooling on it:\n\n1. Inspect the per-example schema (the JSON-string `input` / `output` payloads).\n2. **`verify_dataset.py`** — independently re-check every entity char-span, every fact\n   provenance span, entity/type validity, and head/tail entity-linking coverage.\n3. **`data.py : build_meta()`** — recompute the dataset composition summary.\n4. Visualize the composition (genre / entity-type / relation / facts distributions).\n\"\"\")\n\n# ----------------------------------------------------------------------------- install\nmd(\"md-install\", \"## Setup\\n\\nInstall dependencies. On Colab the core scientific packages are \"\n   \"pre-installed, so they are only installed locally (at Colab's exact versions) to mirror \"\n   \"the Colab environment. The dataset's analysis code itself is pure Python standard library.\")\n\ncode(\"code-install\", \"\"\"\\\nimport subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# matplotlib + pandas are pre-installed on Colab -> only install locally (Colab's versions).\n# (The verification / build_meta code uses only the Python standard library.)\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\n\"\"\")\n\n# ----------------------------------------------------------------------------- imports\nmd(\"md-imports\", \"Imports. The first block is copied verbatim from the artifact's \"\n   \"`data.py` / `verify_dataset.py` (the `loguru` logger is dropped — it was only used by \"\n   \"`data.py:main()`, which rebuilds the corpus from a raw snapshot and is not part of this \"\n   \"demo). The second block adds plotting / table helpers for the notebook.\")\n\ncode(\"code-imports\", \"\"\"\\\n# --- original imports from data.py / verify_dataset.py ---\nfrom __future__ import annotations\nimport os, sys, json, glob, statistics, hashlib\nfrom pathlib import Path\nfrom collections import Counter, defaultdict\n\n# --- added for the notebook demo (tables + plots) ---\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\"\"\")\n\n# ----------------------------------------------------------------------------- data load\nmd(\"md-loader\", \"### Load the dataset\\n\\nLoads the curated demo subset from GitHub, with a local \"\n   \"fallback to `mini_demo_data.json` so the notebook works both in Colab (after deployment) and \"\n   \"locally (now).\")\n\ncode(\"code-loader\", \"\"\"\\\nGITHUB_DATA_URL = \"https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json\"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f: return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")\n\"\"\")\n\ncode(\"code-loaddata\", \"\"\"\\\ndata = load_data()\nprint(\"top-level keys :\", list(data.keys()))\nprint(\"source corpora :\", [(g[\"dataset\"], len(g[\"examples\"])) for g in data[\"datasets\"]])\nprint(\"dataset name   :\", data[\"metadata\"][\"name\"])\n\"\"\")\n\n# ----------------------------------------------------------------------------- config\nmd(\"md-config\", \"## Config\\n\\nAll tunable demo parameters live here. `N_PER_GROUP` controls how \"\n   \"many documents are taken from **each** source corpus (the curated demo file holds 3 per \"\n   \"corpus = 12 docs across all 3 genres; the full dataset has 8 per genre = 24). Start at the \"\n   \"minimum and scale up — the whole demo runs in well under a second at any setting.\")\n\ncode(\"code-config\", \"\"\"\\\n# --- tunable demo parameters (start minimal, scale up freely) ---\nN_PER_GROUP = 3          # docs to take from EACH source corpus. mini file has 3/group (max).\nN_PREVIEW   = 1          # how many full example payloads to print in detail\n\n# --- constants copied from the artifact's verify_dataset.py / data.py ---\nCOARSE       = {\"PER\", \"LOC\", \"ORG\", \"TIME\", \"NUM\", \"MISC\"}   # coarse entity-type set\nSEED         = 42                                             # data.py determinism seed\nCORPUS_ORDER = [\"CUAD\", \"Wikinews\", \"GDPR\", \"eCFR\"]           # stable source-group order\nTOOL_VERSIONS = {\n    \"python\": \"3.12\", \"spacy\": \"3.7.5\", \"spacy_model\": \"en_core_web_sm==3.7.1\",\n    \"nltk\": \"3.9.1 (wordnet, omw-1.4)\", \"numpy\": \"1.26.4\",\n    \"beautifulsoup4\": \"4.12.3 (lxml 5.3.0 parser)\",\n    \"reserved_next_iteration\": \"sentence-transformers all-MiniLM-L6-v2, rank_bm25 \"\n                               \"(NOT used for gold here; reserved for next-iteration \"\n                               \"relation-alignment / retrieval)\",\n}\n\"\"\")\n\n# ----------------------------------------------------------------------------- flatten\nmd(\"md-flatten\", \"## Build the document row-set\\n\\nThe published file groups examples by source \"\n   \"corpus (`datasets[]`). Flatten it back into a flat list of document *rows*, taking the first \"\n   \"`N_PER_GROUP` documents from each corpus. Each row is **one document = one example**.\")\n\ncode(\"code-flatten\", \"\"\"\\\nrows = []\nfor group in data[\"datasets\"]:\n    rows.extend(group[\"examples\"][:N_PER_GROUP])\n\nprint(f\"using {len(rows)} document rows from {len(data['datasets'])} source corpora\")\nprint(\"per-corpus counts:\",\n      [(g[\"dataset\"], min(N_PER_GROUP, len(g[\"examples\"]))) for g in data[\"datasets\"]])\n\"\"\")\n\n# ----------------------------------------------------------------------------- inspect schema\nmd(\"md-inspect\", \"## Inspect the per-example schema\\n\\nEach example's `input` and `output` are \"\n   \"**JSON strings**. After `json.loads`:\\n\\n* **input**  → `{doc_id, document_text, genre, \"\n   \"source, char_length, entities:[{name, type, char_span}]}`\\n* **output** → `{gold_atomic_facts:\"\n   \"[{head, relation, tail, provenance_char_span}]}`\\n\\nThe `corpus_of` helper below is copied \"\n   \"verbatim from `data.py`.\")\n\ncode(\"code-inspect\", \"\"\"\\\ndef corpus_of(source: str) -> str:        # copied verbatim from data.py\n    return source.split(\":\")[0]\n\nfor ex in rows[:N_PREVIEW]:\n    inp = json.loads(ex[\"input\"])         # input is a JSON STRING\n    out = json.loads(ex[\"output\"])        # output is a JSON STRING\n    print(\"=\" * 78)\n    print(\"doc_id      :\", inp[\"doc_id\"], \"| genre:\", inp[\"genre\"], \"| corpus:\", corpus_of(ex[\"metadata_source\"]))\n    print(\"gold_quality:\", ex[\"metadata_gold_quality\"], \"| license:\", ex[\"metadata_license\"][:48], \"...\")\n    print(\"char_length :\", inp[\"char_length\"],\n          \"| #entities:\", len(inp[\"entities\"]), \"| #facts:\", len(out[\"gold_atomic_facts\"]))\n    print(\"-- document_text (first 280 chars) --\")\n    print(\"  \", inp[\"document_text\"][:280].replace(\"\\\\n\", \" \"))\n    print(\"-- first 5 typed entities (name | coarse type | char_span -> verbatim slice) --\")\n    for e in inp[\"entities\"][:5]:\n        s, end = e[\"char_span\"]\n        print(f\"   {e['name']!r:>42}  {e['type']:5} {e['char_span']}  ->  {inp['document_text'][s:end]!r}\")\n    print(\"-- gold_atomic_facts: head -[relation]-> tail (with provenance span) --\")\n    for f in out[\"gold_atomic_facts\"]:\n        print(f\"   {f['head']!r} -[{f['relation']}]-> {f['tail']!r}   prov={f['provenance_char_span']}\")\n\"\"\")\n\n# ----------------------------------------------------------------------------- verify\nmd(\"md-verify\", \"## Verify every invariant (`verify_dataset.py`)\\n\\nThis cell is the core of the \"\n   \"artifact's **independent** verifier (`build/verify_dataset.py`), adapted only to iterate over \"\n   \"the loaded `rows` instead of reading `data_out.json` from disk. It re-checks, from scratch, \"\n   \"every claim the dataset makes:\\n\\n1. JSON-parse every `input` / `output` string.\\n2. \"\n   \"`char_length == len(document_text)` and length-band sanity.\\n3. Every entity `char_span` \"\n   \"satisfies `document_text[s:e] == name`.\\n4. Every entity type is in the coarse set.\\n5. Every \"\n   \"fact provenance span is valid & non-empty; value-tail facts have `tail` inside the span.\\n6. \"\n   \"Head/tail entity-linking coverage (how many fact endpoints appear in the document text).\")\n\ncode(\"code-verify\", \"\"\"\\\n# --- verify_dataset.py main(), adapted to run over the loaded `rows` ---\nexs = rows\ngroup_sizes = {g[\"dataset\"]: min(N_PER_GROUP, len(g[\"examples\"])) for g in data[\"datasets\"]}\nerrors, warns = [], []\nn_ent = n_ent_ok = 0\nn_fact = n_fact_tail_in_span = 0\nhead_linked = tail_linked = 0\ngenres, quality, lic = Counter(), Counter(), Counter()\nrels = Counter()\ntype_counts = Counter()\nlens = []\n\nfor ex in exs:\n    inp = json.loads(ex[\"input\"])\n    out = json.loads(ex[\"output\"])\n    did = inp[\"doc_id\"]\n    dt = inp[\"document_text\"]\n    genres[inp[\"genre\"]] += 1\n    quality[ex[\"metadata_gold_quality\"]] += 1\n    lic[ex[\"metadata_license\"]] += 1\n    lens.append(len(dt))\n\n    # length consistency\n    if inp[\"char_length\"] != len(dt):\n        errors.append(f\"{did}: char_length {inp['char_length']} != len {len(dt)}\")\n    if ex[\"metadata_char_length\"] != len(dt):\n        errors.append(f\"{did}: metadata_char_length mismatch\")\n    if not (1100 <= len(dt) <= 3600):\n        warns.append(f\"{did}: length {len(dt)} outside ~1150-3550 band\")\n\n    ent_surfaces = set()\n    for e in inp[\"entities\"]:\n        n_ent += 1\n        s, ee = e[\"char_span\"]\n        type_counts[e[\"type\"]] += 1\n        if e[\"type\"] not in COARSE:\n            errors.append(f\"{did}: bad entity type {e['type']}\")\n        if 0 <= s <= ee <= len(dt) and dt[s:ee] == e[\"name\"]:\n            n_ent_ok += 1\n            ent_surfaces.add(e[\"name\"])\n        else:\n            errors.append(f\"{did}: entity span FAIL {e['name']!r} {e['char_span']}\")\n\n    facts = out[\"gold_atomic_facts\"]\n    if len(facts) < 3:\n        warns.append(f\"{did}: only {len(facts)} facts\")\n    for f in facts:\n        n_fact += 1\n        rels[f[\"relation\"]] += 1\n        s, ee = f[\"provenance_char_span\"]\n        if not (0 <= s < ee <= len(dt)):\n            errors.append(f\"{did}: bad provenance span {f['provenance_char_span']}\")\n            continue\n        prov = dt[s:ee]\n        if not prov.strip():\n            errors.append(f\"{did}: empty provenance for {f}\")\n        if f[\"tail\"] in prov:\n            n_fact_tail_in_span += 1\n        # entity-linking coverage: do head/tail appear in the document?\n        if f[\"head\"] in dt:\n            head_linked += 1\n        if f[\"tail\"] in dt:\n            tail_linked += 1\n\nprint(\"=\" * 64)\nprint(f\"documents: {len(exs)}  | source-dataset groups: {group_sizes}\")\nprint(f\"genres={dict(genres)}\")\nprint(f\"gold_quality={dict(quality)}\")\nprint(\"licenses:\")\nfor k, v in lic.items():\n    print(f\"   {v:2d}  {k[:70]}\")\nprint(f\"char_length: min={min(lens)} max={max(lens)} mean={sum(lens)//len(lens)}\")\nprint(\"-\" * 64)\nprint(f\"entities: {n_ent} | spans verified: {n_ent_ok}/{n_ent} ({100*n_ent_ok/n_ent:.1f}%)\")\nprint(f\"entity type dist: {dict(type_counts)}\")\nprint(f\"facts: {n_fact} | tail-in-provenance: {n_fact_tail_in_span}/{n_fact} \"\n      f\"({100*n_fact_tail_in_span/n_fact:.1f}%) [rest are clause/label facts]\")\nprint(f\"fact head appears in doc: {head_linked}/{n_fact} ({100*head_linked/n_fact:.1f}%)\")\nprint(f\"fact tail appears in doc: {tail_linked}/{n_fact} ({100*tail_linked/n_fact:.1f}%)\")\nprint(f\"distinct relations: {len(rels)}\")\nprint(f\"top relations: {rels.most_common(12)}\")\nprint(\"-\" * 64)\nprint(f\"ERRORS: {len(errors)}\")\nfor e in errors[:30]:\n    print(\"   ERR\", e)\nprint(f\"WARNINGS: {len(warns)}\")\nfor w in warns[:20]:\n    print(\"   warn\", w)\nprint(\"=\" * 64)\nprint(\"RESULT:\", \"PASS - all spans/types/lengths verified\" if not errors\n      else f\"FAIL - {len(errors)} errors\")\n\"\"\")\n\n# ----------------------------------------------------------------------------- build_meta\nmd(\"md-meta\", \"## Recompute the composition summary (`data.py : build_meta`)\\n\\nThis cell is the \"\n   \"artifact's own `build_meta()` from `data.py`, copied with one minimal change: `ROOT` points \"\n   \"at the current working directory (the original used the script's own folder to fingerprint \"\n   \"the raw snapshot). The `raw/` snapshot is not shipped with the demo, so the determinism \"\n   \"manifest simply reports an empty cache — every *statistical* field is still computed live \"\n   \"from the loaded rows.\")\n\ncode(\"code-meta\", \"\"\"\\\nROOT = Path.cwd()        # minimal path fix: original used the script's own directory\n\n\ndef raw_manifest():      # copied from data.py (reports the cached raw/ snapshot, if present)\n    man = {}\n    cu = ROOT / \"raw\" / \"cuad_data\" / \"CUADv1.json\"\n    if cu.exists():\n        man[\"CUADv1.json\"] = {\"bytes\": cu.stat().st_size,\n                              \"sha256_16\": hashlib.sha256(cu.read_bytes()).hexdigest()[:16]}\n    man[\"gdpr_html_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"gdpr\" / \"art-*.html\")))\n    man[\"wikinews_article_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"wikinews\" / \"article_*.json\")))\n    man[\"ecfr_xml_files\"] = len(glob.glob(str(ROOT / \"raw\" / \"ecfr\" / \"*.xml\")))\n    return man\n\n\ndef build_meta(rows):    # copied verbatim from data.py\n    genres = Counter(r[\"metadata_genre\"] for r in rows)\n    quality = Counter(r[\"metadata_gold_quality\"] for r in rows)\n    qbyg = defaultdict(Counter); cbyg = Counter(); lic = Counter()\n    relvocab = defaultdict(set); lens = []; nfacts = []; nents = []\n    for r in rows:\n        gg = r[\"metadata_genre\"]\n        qbyg[gg][r[\"metadata_gold_quality\"]] += 1\n        cbyg[corpus_of(r[\"metadata_source\"])] += 1\n        lic[r[\"metadata_license\"]] += 1\n        for rel in r[\"metadata_relation_vocab\"]:\n            relvocab[gg].add(rel)\n        lens.append(r[\"metadata_char_length\"]); nfacts.append(r[\"metadata_num_facts\"])\n        nents.append(r[\"metadata_num_entities\"])\n    return {\n        \"name\": \"application_anchor\",\n        \"n_documents\": len(rows),\n        \"n_source_datasets\": len(set(corpus_of(r[\"metadata_source\"]) for r in rows)),\n        \"genre_counts\": dict(genres),\n        \"source_dataset_counts\": dict(cbyg),\n        \"gold_quality_counts\": dict(quality),\n        \"gold_quality_by_genre\": {k: dict(v) for k, v in qbyg.items()},\n        \"license_counts\": dict(lic),\n        \"relation_vocab_by_genre\": {k: sorted(v) for k, v in relvocab.items()},\n        \"total_facts\": sum(nfacts), \"total_entities\": sum(nents),\n        \"facts_per_doc\": {\"min\": min(nfacts), \"max\": max(nfacts),\n                          \"mean\": round(statistics.mean(nfacts), 2)},\n        \"char_length\": {\"min\": min(lens), \"max\": max(lens),\n                        \"mean\": round(statistics.mean(lens), 1),\n                        \"median\": int(statistics.median(lens))},\n        \"determinism\": {\"seed\": SEED, \"tool_versions\": TOOL_VERSIONS,\n                        \"raw_cache_manifest\": raw_manifest()},\n    }\n\n\nmeta = build_meta(rows)\nfor k in [\"n_documents\", \"n_source_datasets\", \"genre_counts\", \"source_dataset_counts\",\n          \"gold_quality_counts\", \"gold_quality_by_genre\", \"license_counts\",\n          \"total_facts\", \"total_entities\", \"facts_per_doc\", \"char_length\"]:\n    print(f\"{k:24}: {meta[k]}\")\nprint(\"\\\\nrelation_vocab_by_genre:\")\nfor g, v in meta[\"relation_vocab_by_genre\"].items():\n    print(f\"   {g:11}: {v}\")\n\"\"\")\n\n# ----------------------------------------------------------------------------- viz\nmd(\"md-viz\", \"## Visualize the dataset\\n\\nA per-document summary table plus four composition charts: \"\n   \"documents per genre, coarse entity-type distribution, total gold facts per genre, and the most \"\n   \"frequent relations. (`type_counts` and `rels` were computed in the verification cell above.)\")\n\ncode(\"code-viz\", \"\"\"\\\n# per-document summary table\nrecs = []\nfor ex in rows:\n    inp = json.loads(ex[\"input\"]); out = json.loads(ex[\"output\"])\n    recs.append({\n        \"doc_id\": inp[\"doc_id\"], \"corpus\": corpus_of(ex[\"metadata_source\"]),\n        \"genre\": inp[\"genre\"], \"quality\": ex[\"metadata_gold_quality\"],\n        \"char_length\": inp[\"char_length\"],\n        \"n_entities\": len(inp[\"entities\"]), \"n_facts\": len(out[\"gold_atomic_facts\"]),\n    })\ndf = pd.DataFrame(recs)\nprint(\"Per-document summary:\")\nprint(df.to_string(index=False))\n\n# four composition charts\nfig, ax = plt.subplots(2, 2, figsize=(13, 8))\n\ndf[\"genre\"].value_counts().reindex([\"legal\", \"news\", \"regulatory\"]).plot(\n    kind=\"bar\", ax=ax[0, 0], color=\"steelblue\", rot=0)\nax[0, 0].set_title(\"Documents per genre\"); ax[0, 0].set_ylabel(\"# documents\")\n\npd.Series(dict(type_counts)).reindex(sorted(COARSE)).fillna(0).plot(\n    kind=\"bar\", ax=ax[0, 1], color=\"darkorange\", rot=0)\nax[0, 1].set_title(\"Coarse entity-type distribution\"); ax[0, 1].set_ylabel(\"# entities\")\n\ndf.groupby(\"genre\")[\"n_facts\"].sum().reindex([\"legal\", \"news\", \"regulatory\"]).plot(\n    kind=\"bar\", ax=ax[1, 0], color=\"seagreen\", rot=0)\nax[1, 0].set_title(\"Total gold atomic-facts per genre\"); ax[1, 0].set_ylabel(\"# facts\")\n\ntop_rel = pd.Series(dict(rels.most_common(10)))[::-1]\ntop_rel.plot(kind=\"barh\", ax=ax[1, 1], color=\"mediumpurple\")\nax[1, 1].set_title(\"Top relations (gold vocabulary)\"); ax[1, 1].set_xlabel(\"# facts\")\n\nplt.tight_layout()\nplt.savefig(\"demo_summary.png\", dpi=90, bbox_inches=\"tight\")\nplt.show()\nprint(\"\\\\nSaved figure -> demo_summary.png\")\n\"\"\")\n\n# ----------------------------------------------------------------------------- summary md\nmd(\"md-done\", \"\"\"\\\n## Summary\n\nThe demo loaded a 12-document, all-genre subset of the **Application Anchor** dataset and ran the\nartifact's own tooling on it:\n\n* **Verification** independently confirmed every entity char-span (`document_text[s:e] == name`),\n  every fact provenance span, coarse-type validity, and head/tail entity-linking coverage — with\n  **zero errors**, reproducing the dataset's headline guarantee.\n* **`build_meta`** recomputed the composition: balanced genres, crisp (legal) vs silver\n  (news/regulatory) gold, per-genre relation vocabularies, and char-length / facts-per-doc stats.\n\nTo scale up, raise `N_PER_GROUP` in the Config cell (3 = all of the demo file). The full dataset\n(`full_data_out.json`, 24 docs, 8 per genre, 140 gold facts) is regenerated deterministically and\nbyte-identically from a cached raw snapshot via `python data.py` — **no network and no LLM** in\ngold construction, which is what keeps the downstream hallucination-control experiment\nnon-circular.\n\"\"\")\n\nnb = {\n    \"cells\": cells,\n    \"metadata\": {\n        \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n        \"language_info\": {\"name\": \"python\", \"version\": \"3.12\"},\n    },\n    \"nbformat\": 4,\n    \"nbformat_minor\": 5,\n}\n\nwith open(NB_PATH, \"w\") as f:\n    json.dump(nb, f, indent=1)\nprint(\"wrote\", NB_PATH, \"with\", len(cells), \"cells\")\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [36] ASSISTANT · 2026-06-16 13:30:21 UTC

```
Now generate the notebook and validate its JSON, then set up the clean test environment.
```

### [37] TOOL CALL — Bash · 2026-06-16 13:30:21 UTC

```
Generate notebook and validate JSON:
python3 build_nb.py && python3 -c "import json; nb=json.load(open('code_demo.ipynb')); print('valid ipynb, cells:', len(nb['cells'])); print('types:', [c['cell_type'][0] for c in nb['cells']])"
```

### [38] TOOL RESULT — Bash · 2026-06-16 13:30:21 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/code_demo.ipynb with 21 cells\nvalid ipynb, cells: 21\ntypes: ['m', 'm', 'c', 'm', 'c', 'm', 'c', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm']", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [39] ASSISTANT · 2026-06-16 13:30:27 UTC

```
Notebook generated. Now let me test-run it in a clean environment simulating Colab. This takes a while (venv + pip), so I'll run it in the background.
```

### [40] TOOL CALL — Bash · 2026-06-16 13:30:27 UTC

```
Create clean venv and execute notebook:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
rm -rf .nb_env
/usr/local/bin/python3.12 -m venv .nb_env
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -3
echo "=== jupyter installed, executing notebook ==="
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -40
echo "=== EXIT: $? ==="
```

### [41] TOOL RESULT — Bash · 2026-06-16 13:30:27 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bjzibic4y"}
```

### [42] ASSISTANT · 2026-06-16 13:30:41 UTC

```
The test is running in the background. Let me monitor its progress.
```

### [43] TOOL CALL — Bash · 2026-06-16 13:30:41 UTC

```
Wait for notebook test run to finish:
until [ -s /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output ] && grep -q "EXIT:" /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output 2>/dev/null; do sleep 5; done; echo "DONE"; cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [44] TOOL RESULT — Bash · 2026-06-16 13:40:37 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "byzkcfo63", "assistantAutoBackgrounded": false}
```

### [45] TOOL CALL — Read · 2026-06-16 13:40:45 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [46] TOOL RESULT — Read · 2026-06-16 13:40:45 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output", "content": "\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: python3.12 -m pip install --upgrade pip\n=== jupyter installed, executing notebook ===\n", "numLines": 5, "startLine": 1, "totalLines": 5}}
```

### [47] TOOL CALL — Read · 2026-06-16 13:40:51 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [48] TOOL RESULT — Read · 2026-06-16 13:40:51 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output"}}
```

### [49] ASSISTANT · 2026-06-16 13:40:57 UTC

```
Both the test run and my watcher loop are running in the background. I'll wait for the completion notification rather than polling wastefully.
```

### [50] TOOL CALL — Read · 2026-06-16 13:40:57 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/byzkcfo63.output
```

### [51] TOOL RESULT — Read · 2026-06-16 13:40:57 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/byzkcfo63.output", "content": "", "numLines": 1, "startLine": 1, "totalLines": 1}}
```

### [52] ASSISTANT · 2026-06-16 13:41:11 UTC

```
While the test runs, let me verify TODO 6 requirements against the generated notebook in parallel.
```

### [53] TOOL CALL — Bash · 2026-06-16 13:41:11 UTC

```
Verify TODO 6 requirements on notebook:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
echo "=== mini_demo_data.json exists? ==="; ls -la mini_demo_data.json
echo "=== GITHUB_DATA_URL exact match? ==="
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
src='\n'.join(c['source'] for c in nb['cells'] if c['cell_type']=='code')
url='https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json'
print('URL present exact:', ('GITHUB_DATA_URL = \"%s\"'%url) in src)
print('urlopen pattern present:', 'urllib.request.urlopen(GITHUB_DATA_URL)' in src)
print('local fallback present:', 'mini_demo_data.json' in src and 'os.path.exists' in src)
print('uses GitHub URL not just open():', 'load_data()' in src)
"
```

### [54] TOOL RESULT — Bash · 2026-06-16 13:41:11 UTC

```
{"stdout": "=== mini_demo_data.json exists? ===\n-rw-r--r-- 1 root root 98348 Jun 16 13:27 mini_demo_data.json\n=== GITHUB_DATA_URL exact match? ===\nURL present exact: True\nurlopen pattern present: True\nlocal fallback present: True\nuses GitHub URL not just open(): True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [55] ASSISTANT · 2026-06-16 13:41:15 UTC

```
All TODO 6 requirements pass. Now let me check the test run status.
```

### [56] TOOL CALL — Read · 2026-06-16 13:41:15 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [57] TOOL RESULT — Read · 2026-06-16 13:41:15 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output"}}
```

### [58] ASSISTANT · 2026-06-16 13:41:21 UTC

```
The notebook is still executing in the clean venv (pip install of numpy/pandas/matplotlib takes a bit). I've verified all TODO 6 requirements pass. I'll wait for the test run to complete and report results.
```

### [59] TOOL CALL — Read · 2026-06-16 13:41:21 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [60] TOOL RESULT — Read · 2026-06-16 13:41:21 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output"}}
```

### [61] ASSISTANT · 2026-06-16 13:41:25 UTC

```
I'll wait for the background test to complete — the harness will notify me when the notebook execution finishes. Standing by for the result.
```

### [62] SYSTEM-USER prompt · 2026-06-16 13:41:27 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [63] ASSISTANT · 2026-06-16 13:41:31 UTC

```
Let me check the test run result before finalizing.
```

### [64] TOOL CALL — Read · 2026-06-16 13:41:31 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
```

### [65] TOOL RESULT — Read · 2026-06-16 13:41:31 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output"}}
```

### [66] ASSISTANT · 2026-06-16 13:41:41 UTC

```
The cached Read isn't updating. Let me check the actual current state of the background processes and output files directly.
```

### [67] TOOL CALL — Bash · 2026-06-16 13:41:41 UTC

```
Check test run state and notebook execution outputs:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
echo "=== bjzibic4y output (test run) ==="
tail -50 /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
echo "=== is .nb_env still being used / executed notebook present? ==="
ls -la .nb_env 2>/dev/null | head -2
echo "=== executed notebook cell outputs check ==="
python3 -c "
import json,os
nb=json.load(open('code_demo.ipynb'))
ec=[c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code']
print('execution_counts:', ec)
errs=[]
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error':
                errs.append(o.get('ename'))
print('errors in notebook outputs:', errs)
"
```

### [68] TOOL RESULT — Bash · 2026-06-16 13:41:41 UTC

```
{"stdout": "=== bjzibic4y output (test run) ===\n\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: python3.12 -m pip install --upgrade pip\n=== jupyter installed, executing notebook ===\n=== is .nb_env still being used / executed notebook present? ===\ntotal 8931\ndrwxr-xr-x 7 root root 2025721 Jun 16 13:31 .\n=== executed notebook cell outputs check ===\nexecution_counts: [None, None, None, None, None, None, None, None, None, None]\nerrors in notebook outputs: []", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [69] ASSISTANT · 2026-06-16 13:41:49 UTC

```
The notebook is still executing (the install cell is pip-installing numpy/pandas/matplotlib inside the kernel — the slow part). No errors so far. Let me write the required output file now, then continue verifying the test passes.
```

### [70] TOOL CALL — Write · 2026-06-16 13:41:49 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [71] TOOL RESULT — Write · 2026-06-16 13:41:49 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [72] ASSISTANT · 2026-06-16 13:41:59 UTC

```
Output file written. Now let me wait for the test run to finish and confirm it passes.
```

### [73] TOOL CALL — Bash · 2026-06-16 13:41:59 UTC

```
Wait for and show final test run output:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
OUT=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-UBTwyePql8NQ/2b8fd860-570c-4beb-86e0-8ea1e6bdc068/tasks/bjzibic4y.output
for i in $(seq 1 90); do
  if grep -q "=== EXIT:" "$OUT" 2>/dev/null; then break; fi
  /usr/local/bin/python3.12 -c "import time; time.sleep(5)"
done
echo "=== FINAL TEST OUTPUT ==="
tail -45 "$OUT"
```

### [74] TOOL RESULT — Bash · 2026-06-16 13:46:27 UTC

```
{"stdout": "=== FINAL TEST OUTPUT ===\n\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: python3.12 -m pip install --upgrade pip\n=== jupyter installed, executing notebook ===\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 126232 bytes to code_demo.ipynb\n=== EXIT: 0 ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [75] ASSISTANT · 2026-06-16 13:46:37 UTC

```
Test run passed (exit 0). Let me verify the executed notebook's actual cell outputs to confirm the verification cell shows PASS and there are no silent errors.
```

### [76] TOOL CALL — Bash · 2026-06-16 13:46:37 UTC

```
Inspect executed notebook cell outputs:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
ec=[c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code']
print('execution_counts:', ec)
errs=[]
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error':
                errs.append((i,o.get('ename'),o.get('evalue')))
print('ERRORS:', errs)
print('='*70)
# print stdout text from key cells
def txt(o):
    if o.get('output_type')=='stream': return ''.join(o.get('text',''))
    if o.get('output_type') in ('execute_result','display_data'):
        return ''.join(o.get('data',{}).get('text/plain',''))
    return ''
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        out=''.join(txt(o) for o in c.get('outputs',[]))
        if out.strip():
            print(f'--- cell {i} output (truncated) ---')
            print(out[:1500])
" 2>&1 | head -120
```

### [77] TOOL RESULT — Bash · 2026-06-16 13:46:37 UTC

```
{"stdout": "execution_counts: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nERRORS: []\n======================================================================\n--- cell 2 output (truncated) ---\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n--- cell 7 output (truncated) ---\ntop-level keys : ['metadata', 'datasets']\nsource corpora : [('CUAD', 3), ('Wikinews', 3), ('GDPR', 3), ('eCFR', 3)]\ndataset name   : application_anchor\n\n--- cell 11 output (truncated) ---\nusing 12 document rows from 4 source corpora\nper-corpus counts: [('CUAD', 3), ('Wikinews', 3), ('GDPR', 3), ('eCFR', 3)]\n\n--- cell 13 output (truncated) ---\n==============================================================================\ndoc_id      : legal_cuad_00 | genre: legal | corpus: CUAD\ngold_quality: crisp | license: CC BY 4.0 (Atticus Project / CUAD v1; Zenodo 459 ...\nchar_length : 2010 | #entities: 34 | #facts: 6\n-- document_text (first 280 chars) --\n   03/01/05  607-1295 Richards Street   604.684.2255  Vancouver, BC V6B1B7   deep@rrt.ca   deep systems      Premium Managed Hosting Agreement  This is a managed hosting agreement between AstroNutrition.com and deep systems.  The effective term is 12 months beginning March 1, 2005 a\n-- first 5 typed entities (name | coarse type | char_span -> verbatim slice) --\n          'Premium Managed Hosting Agreement'  MISC  [106, 139]  ->  'Premium Managed Hosting Agreement'\n                                  'Vancouver'  LOC   [51, 60]  ->  'Vancouver'\n                                  'BC V6B1B7'  LOC   [62, 71]  ->  'BC V6B1B7'\n                         'AstroNutrition.com'  ORG   [185, 203]  ->  'AstroNutrition.com'\n          '12 months beginning March 1, 2005'  TIME  [245, 278]  ->  '12 months beginning March 1, 2005'\n-- gold_atomic_facts: head -[relation]-> tail (with provenance span) --\n   'Premium Managed Hosting Agreement' -[agreement_date]-> '03/01/05'   prov=[0, 8]\n   'Premium Managed Hosting Agreement' -[has_party]-> 'deep systems'   prov=[88, 100]\n   'Premium Managed Hosting Agreement' -[has_title]-> 'Premium Managed Hosting Agreement'   prov=[106, 139]\n   'Premium Managed Ho\n--- cell 15 output (truncated) ---\n================================================================\ndocuments: 12  | source-dataset groups: {'CUAD': 3, 'Wikinews': 3, 'GDPR': 3, 'eCFR': 3}\ngenres={'legal': 3, 'news': 3, 'regulatory': 6}\ngold_quality={'crisp': 3, 'silver': 9}\nlicenses:\n    3  CC BY 4.0 (Atticus Project / CUAD v1; Zenodo 4595826)\n    3  CC BY 2.5 (Wikinews / Wikimedia Foundation)\n    3  EUR-Lex reuse (© European Union; Regulation (EU) 2016/679, CELEX:32016\n    3  Public domain (US Government work; eCFR / GPO, ecfr.gov)\nchar_length: min=1239 max=3422 mean=2322\n----------------------------------------------------------------\nentities: 374 | spans verified: 374/374 (100.0%)\nentity type dist: {'MISC': 66, 'LOC': 46, 'ORG': 74, 'TIME': 59, 'NUM': 69, 'PER': 60}\nfacts: 62 | tail-in-provenance: 61/62 (98.4%) [rest are clause/label facts]\nfact head appears in doc: 62/62 (100.0%)\nfact tail appears in doc: 61/62 (98.4%)\ndistinct relations: 19\ntop relations: [('cross_references', 16), ('has_party', 10), ('has_title', 9), ('occurred_on', 5), ('agreement_date', 3), ('obligates', 3), ('grants_right', 3), ('effective_date', 2), ('expiration_date', 1), ('minimum_commitment', 1), ('contains_license_grant', 1), ('revenue_profit_sharing', 1)]\n----------------------------------------------------------------\nERRORS: 0\nWARNINGS: 0\n================================================================\nRESULT: PASS - all spans/types/lengths verified\n\n--- cell 17 output (truncated) ---\nn_documents             : 12\nn_source_datasets       : 4\ngenre_counts            : {'legal': 3, 'news': 3, 'regulatory': 6}\nsource_dataset_counts   : {'CUAD': 3, 'Wikinews': 3, 'GDPR': 3, 'eCFR': 3}\ngold_quality_counts     : {'crisp': 3, 'silver': 9}\ngold_quality_by_genre   : {'legal': {'crisp': 3}, 'news': {'silver': 3}, 'regulatory': {'silver': 6}}\nlicense_counts          : {'CC BY 4.0 (Atticus Project / CUAD v1; Zenodo 4595826)': 3, 'CC BY 2.5 (Wikinews / Wikimedia Foundation)': 3, 'EUR-Lex reuse (© European Union; Regulation (EU) 2016/679, CELEX:32016R0679; free reuse with attribution); text via gdpr-info.eu': 3, 'Public domain (US Government work; eCFR / GPO, ecfr.gov)': 3}\ntotal_facts             : 62\ntotal_entities          : 374\nfacts_per_doc           : {'min': 3, 'max': 10, 'mean': 5.17}\nchar_length             : {'min': 1239, 'max': 3422, 'mean': 2322.2, 'median': 2209}\n\nrelation_vocab_by_genre:\n   legal      : ['agreement_date', 'contains_license_grant', 'effective_date', 'expiration_date', 'has_party', 'has_title', 'minimum_commitment', 'revenue_profit_sharing']\n   news       : ['choose', 'draw', 'head', 'join', 'occurred_on']\n   regulatory : ['cross_references', 'defined_as', 'grants_right', 'has_exception', 'has_title', 'obligates', 'requires']\n\n--- cell 19 output (truncated) ---\nPer-document summary:\n          doc_id   corpus      genre quality  char_length  n_entities  n_facts\n   legal_cuad_00     CUAD      legal   crisp         2010          34        6\n   legal_cuad_01     CUAD      legal   crisp         2274          39        8\n   legal_cuad_02     CUAD      legal   crisp         3422          64        8\nnews_wikinews_00 Wikinews       news  silver         2867          46        3\nnews_wikinews_01 Wikinews       news  silver         2509          82        3\nnews_wikinews_02 Wikinews       news  silver         2144          43        3\n     reg_gdpr_05     GDPR regulatory  silver         2006           5        3\n     reg_gdpr_07     GDPR regulatory  silver         1239           3        3\n     reg_gdpr_13     GDPR regulatory  silver         3186          16       10\nreg_ecfr_1016_10     eCFR regulatory  silver         2796          14        6\nreg_ecfr_1016_13     eCFR regulatory  silver         1807          15        5\n reg_ecfr_1016_8     eCFR regulatory  silver         1606          13        4\n<Figure size 1300x800 with 4 Axes>\nSaved figure -> demo_summary.png", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [78] ASSISTANT · 2026-06-16 13:46:57 UTC

```
The notebook executed cleanly end-to-end — all 10 code cells ran (execution_counts 1–10), **zero errors**, verification cell reports **`RESULT: PASS`** with 374/374 entity spans verified (100%), and the visualization figure was produced. Let me clean up the disposable venv and confirm final deliverables.
```

### [79] TOOL CALL — Bash · 2026-06-16 13:46:57 UTC

```
Clean up venv and confirm final deliverables:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
rm -rf .nb_env
echo "=== final workspace deliverables ==="
ls -la code_demo.ipynb mini_demo_data.json .terminal_claude_agent_struct_out.json
echo "=== struct out content ==="
cat .terminal_claude_agent_struct_out.json
echo "=== confirm notebook has all required pieces ==="
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
src='\n'.join(c['source'] for c in nb['cells'] if c['cell_type']=='code')
url='https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json'
print('exact GITHUB_DATA_URL:', ('GITHUB_DATA_URL = \"%s\"'%url) in src)
print('GitHub-URL load pattern (not just open):', 'urllib.request.urlopen(GITHUB_DATA_URL)' in src and 'load_data()' in src)
print('cells:', len(nb['cells']), '| all code cells executed:', all(c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code'))
"
```

### [80] TOOL RESULT — Bash [ERROR] · 2026-06-16 13:48:11 UTC

```
Error: Exit code 1
=== final workspace deliverables ===
-rw-r--r-- 1 root root    113 Jun 16 13:41 .terminal_claude_agent_struct_out.json
-rw-r--r-- 1 root root 126260 Jun 16 13:46 code_demo.ipynb
-rw-r--r-- 1 root root  98348 Jun 16 13:27 mini_demo_data.json
=== struct out content ===
{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
=== confirm notebook has all required pieces ===
Traceback (most recent call last):
  File "<string>", line 4, in <module>
TypeError: sequence item 0: expected str instance, list found
```

### [81] ASSISTANT · 2026-06-16 13:48:25 UTC

```
The deliverables are all present — the error is just my verification snippet (nbconvert re-saved cell `source` as a list of strings). Let me fix the check.
```

### [82] TOOL CALL — Bash · 2026-06-16 13:48:25 UTC

```
Re-run notebook verification with list-safe join:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_UBTwyePql8NQ
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
def s(c):
    src=c['source']
    return src if isinstance(src,str) else ''.join(src)
src='\n'.join(s(c) for c in nb['cells'] if c['cell_type']=='code')
url='https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/dataset-1/demo/mini_demo_data.json'
print('exact GITHUB_DATA_URL present:', ('GITHUB_DATA_URL = \"%s\"'%url) in src)
print('GitHub-URL load pattern (not just open):', 'urllib.request.urlopen(GITHUB_DATA_URL)' in src and 'load_data()' in src)
print('local fallback present:', 'os.path.exists(\"mini_demo_data.json\")' in src)
print('total cells:', len(nb['cells']))
print('all code cells executed:', all(c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code'))
print('no error outputs:', not any(o.get('output_type')=='error' for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[])))
"
```

### [83] TOOL RESULT — Bash · 2026-06-16 13:48:25 UTC

```
{"stdout": "exact GITHUB_DATA_URL present: True\nGitHub-URL load pattern (not just open): True\nlocal fallback present: True\ntotal cells: 21\nall code cells executed: True\nno error outputs: True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [84] ASSISTANT · 2026-06-16 13:48:42 UTC

```
Everything is complete and verified. Final summary:

## Done — Application Anchor dataset demo

**Deliverables** (both in workspace):
- `code_demo.ipynb` — 21 cells, executed clean in a Colab-simulating venv (**0 errors**, all 10 code cells ran)
- `mini_demo_data.json` — 12-doc curated subset (3 per source corpus: CUAD/Wikinews/GDPR/eCFR), all 3 genres, full untruncated payloads, 96 KB
- `.terminal_claude_agent_struct_out.json` — written

**Approach** — minimal-change conversion of the artifact's own analysis code:
- The notebook reuses `verify_dataset.py`'s verification loop and `data.py`'s `build_meta()`/`corpus_of()` **nearly verbatim** — the only changes are path/CLI plumbing (load from the GitHub URL instead of `data_out.json`) and dropping `loguru` (only used by `data.py:main()`, which rebuilds from a raw snapshot not shipped with the demo).
- Structure follows the spec: title → install (Colab-guarded) → imports → GitHub-URL loader with local fallback → config → flatten → schema inspection → **verification** → **build_meta** → visualization (per-doc table + 4-chart figure).

**Verified results from the executed notebook:**
- Entity char-spans: **374/374 (100%)** verified (`document_text[s:e] == name`)
- Fact tail-in-provenance 98.4%, fact-head-in-doc 100% → `RESULT: PASS`
- Composition recomputed live: legal(crisp)/news+regulatory(silver), per-genre relation vocabularies, char-length & facts-per-doc stats

**Config / scaling:** `N_PER_GROUP=3` (all of the mini file = 12 docs) is the final value — the entire demo runs in well under a second of compute (the ~10 min wall-clock was venv setup + pip, skipped on Colab), so it sits comfortably inside the 600 s budget with no scaling tradeoff needed. A reader can lower `N_PER_GROUP` to 1 for a 4-doc smoke test or note the full dataset's 24 docs (8/genre).

**TODO 6 checks all pass:** exact `GITHUB_DATA_URL` present, `mini_demo_data.json` exists, loads via the `urllib.request.urlopen(GITHUB_DATA_URL)` pattern with local fallback (not a bare `open()`).
```
