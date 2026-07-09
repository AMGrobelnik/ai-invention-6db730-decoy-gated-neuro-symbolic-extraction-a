# gen_demo_art_experiment_3 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_3` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 13:05:02 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh
```

### [2] SYSTEM-USER prompt · 2026-06-16 13:05:08 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/results/out.json`
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a
Raw data URL: https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-3/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-3/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-3/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-06-16 13:05:08 UTC

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

### [4] ASSISTANT · 2026-06-16 13:05:20 UTC

```
I'll start by reading the required skills and exploring the source artifact in parallel.
```

### [5] TOOL CALL — Skill · 2026-06-16 13:05:20 UTC

```
aii-colab
```

### [6] TOOL RESULT — Skill · 2026-06-16 13:05:20 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [7] TOOL CALL — Skill · 2026-06-16 13:05:20 UTC

```
aii-long-running-tasks
```

### [8] TOOL RESULT — Skill · 2026-06-16 13:05:20 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [9] TOOL CALL — Bash · 2026-06-16 13:05:20 UTC

```
List source artifact directory and file sizes:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3 && echo "=== DIR LISTING ===" && ls -la && echo "=== FILE SIZES ===" && du -h method.py *.json 2>/dev/null
```

### [10] TOOL RESULT — Bash · 2026-06-16 13:05:20 UTC

```
{"stdout": "=== DIR LISTING ===\ntotal 21984\ndrwxr-xr-x 7 root root 3000105 Jun 16 07:06 .\ndrwxr-xr-x 7 root root 3000195 Jun 16 06:12 ..\n-rw-r--r-- 1 root root 6973905 Jun 16 07:06 .repl_agent.ptylog\n-rw-r--r-- 1 root root    3206 Jun 16 07:06 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 5 root root 3000104 Jun 16 06:17 .venv\n-rw-r--r-- 1 root root    4756 Jun 16 06:52 README.md\ndrwxr-xr-x 2 root root 1011933 Jun 16 07:04 __pycache__\n-rw-r--r-- 1 root root   17595 Jun 16 06:46 analyze.py\ndrwxr-xr-x 2 root root 1018732 Jun 16 06:37 cache\ndrwxr-xr-x 5 root root 2000255 Jun 16 06:54 checkpoints\n-rw-r--r-- 1 root root   16108 Jun 16 06:44 common.py\n-rw-r--r-- 1 root root   11116 Jun 16 07:03 extract.py\n-rw-r--r-- 1 root root  164529 Jun 16 07:05 full_method_out.json\n-rw-r--r-- 1 root root    4001 Jun 16 06:21 llm.py\ndrwxr-xr-x 2 root root 2000182 Jun 16 07:04 logs\n-rw-r--r-- 1 root root   27463 Jun 16 06:48 method.py\n-rw-r--r-- 1 root root  164623 Jun 16 06:58 method_out.json\n-rw-r--r-- 1 root root   57215 Jun 16 07:05 mini_method_out.json\n-rw-r--r-- 1 root root   16623 Jun 16 07:05 preview_method_out.json\n-rw-r--r-- 1 root root    8039 Jun 16 07:02 prompts.py\n-rw-r--r-- 1 root root     834 Jun 16 06:57 pyproject.toml\n-rw-r--r-- 1 root root    2615 Jun 16 06:41 summarize.py\n-rw-r--r-- 1 root root    2134 Jun 16 06:28 test_plumbing.py\n=== FILE SIZES ===\n27K\tmethod.py\n161K\tfull_method_out.json\n161K\tmethod_out.json\n56K\tmini_method_out.json\n17K\tpreview_method_out.json", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] ASSISTANT · 2026-06-16 13:05:36 UTC

```
Let me read the source files to understand the structure.
```

### [12] TOOL CALL — Read · 2026-06-16 13:05:36 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/method.py
```

### [13] TOOL CALL — Read · 2026-06-16 13:05:36 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/preview_method_out.json
```

### [14] TOOL RESULT — Read · 2026-06-16 13:05:36 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/method.py", "content": "#!/usr/bin/env python3\n\"\"\"Re-DocRED OPERATIONAL WEDGE (S4): does decoy-gating (knockoff+ competition statistic W_i)\nbeat a PLAIN confidence threshold (raw Z_i) at MATCHED RECALL on atomic-fact precision and\nmulti-hop hallucinated-conclusion rate? Compares 5 systems (METHOD, PLAIN foil, CoT, RAG,\nlabeled conformal... [truncated, 28928 chars total]
```

### [15] TOOL RESULT — Read · 2026-06-16 13:05:36 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/preview_method_out.json", "content": "{\n  \"metadata\": {\n    \"method_name\": \"Decoy-gating (knockoff+ W_i) vs plain confidence threshold (Z_i)\",\n    \"description\": \"Operational wedge on Re-DocRED at matched recall: atomic-fact precision, multi-hop hallucinated-conclusion rate, knockoff+ operating points.\",\n    \"n_docs_used\": 36,\n    \"split_role\": \"confirmatory\",\n    \"model\": \"openai/gpt-4.1-nano\",\n    \"elicitation\": \"logprob_yes_token (verbalized_[0,1] fallback)\",\n    \"logprobs_available\": true,\n    \"caching_ok\": false,\n    \"cost_usd\": 0.34744,\n    \"n_api_calls\": 8005,\n    \"n_calibration_labels_conformal\": 259,\n    \"seed\": 20240617,\n    \"bootstrap_B\": 300,\n    \"systems\": [\n      \"METHOD\",\n      \"PLAIN\",\n      \"CoT\"\n    ],\n    \"rules_list\": [\n      \"transitive_located_in_admin (P131;P131->P131)\",\n      \"located_in_admin_then_country (P131;P17->P17)\",\n      \"transitive_contains_admin (P150;P150->P150)\"\n    ],\n    \"config\": {\n      \"cand_cap\": 30,\n      \"n_overgen\": 3,\n      \"n_conf_samples\": 5,\n      \"alpha_grid\": [\n        0.05,\n        0.1,\n        0.2\n      ],\n      \"W_floor_k\": {\n        \"0.05\": 20,\n        \"0.1\": 10,\n        \"0.2\": 5,\n        \"0.3\": 4,\n        \"0.5\": 2\n      },\n      \"align_shortlist_k\": 8,\n      \"el_embed_floor\": 0.6,\n      \"decoy_max_regen\": 3\n    },\n    \"max_recall_per_system\": {\n      \"METHOD\": 0.08555,\n      \"PLAIN\": 0.08555,\n      \"CoT\": 0.04943,\n      \"RAG\": 0.04087,\n      \"CONF\": 0.08555\n    },\n    \"max_common_recall\": 0.04087,\n    \"pr_curves\": {\n      \"METHOD\": [\n        [\n          0.0,\n          0.0,\n          1.0\n        ],\n        [\n          0.0038,\n          0.44444,\n          1.0\n        ],\n        [\n          0.00665,\n          0.41176,\n          1.0\n        ]\n      ],\n      \"PLAIN\": [\n        [\n          0.0,\n          0.0,\n          1.0\n        ],\n        [\n          0.0038,\n          0.44444,\n          1.0\n        ],\n        [\n          0.00665,\n          0.41176,\n          1.0\n        ]\n      ],\n      \"CoT\": [\n        [\n          0.00095,\n          1.0,\n          1.0\n        ],\n        [\n          0.00285,\n          0.6,\n          1.0\n        ],\n        [\n          0.00475,\n          0.55556,\n          1.0\n        ]\n      ],\n      \"RAG\": [\n        [\n          0.00095,\n          1.0,\n          1.0\n        ],\n        [\n          0.00095,\n          0.25,\n          1.0\n        ],\n        [\n          0.0019,\n          0.28571,\n          1.0\n        ]\n      ],\n      \"CONF\": [\n        [\n          0.00095,\n          1.0,\n          1.0\n        ],\n        [\n          0.00475,\n          0.55556,\n          1.0\n        ],\n        [\n          0.0076,\n          0.47059,\n          1.0\n        ]\n      ]\n    },\n    \"matched_recall\": {\n      \"recall_grid\": [\n        0.05,\n        0.05148,\n        0.05296\n      ],\n      \"precision\": {\n        \"METHOD\": [\n          0.26108,\n          0.25822,\n          0.25339\n        ],\n        \"PLAIN\": [\n          0.26368,\n          0.25822,\n          0.25688\n        ],\n        \"CoT\": [\n          null,\n          null,\n          null\n        ],\n        \"RAG\": [\n          null,\n          null,\n          null\n        ],\n        \"CONF\": [\n          0.22944,\n          0.23305,\n          0.23629\n        ]\n      },\n      \"precision_ci\": {\n        \"METHOD\": [\n          [\n            0.19803,\n            0.32037\n          ],\n          [\n            0.19157,\n            0.32129\n          ],\n          [\n            0.18878,\n            0.31839\n          ]\n        ],\n        \"PLAIN\": [\n          [\n            0.20525,\n            0.31913\n          ],\n          [\n            0.19787,\n            0.31644\n          ],\n          [\n            0.19578,\n            0.31591\n          ]\n        ],\n        \"CoT\": [\n          [\n            null,\n            null\n          ],\n          [\n            null,\n            null\n          ],\n          [\n            null,\n            null\n          ]\n        ],\n        \"RAG\": [\n          [\n            null,\n            null\n          ],\n          [\n            null,\n            null\n          ],\n          [\n            null,\n            null\n          ]\n        ],\n        \"CONF\": [\n          [\n            0.19756,\n            0.26774\n          ],\n          [\n            0.1956,\n            0.27315\n          ],\n          [\n            0.19665,\n            0.2777\n          ]\n        ]\n      },\n      \"delta_method_minus_plain\": [\n        -0.00252,\n        -0.00029,\n        -0.00337\n      ],\n      \"delta_ci\": [\n        [\n          -0.0159,\n          0.01208\n        ],\n        [\n          -0.01122,\n          0.01132\n        ],\n        [\n          -0.01612,\n          0.01021\n        ]\n      ],\n      \"delta_bootstrap_p_value\": [\n        0.64667,\n        0.57333,\n        0.70333\n      ],\n      \"bh_significant\": [\n        false,\n        false,\n        false\n      ],\n      \"confirmed_recall_points\": []\n    },\n    \"knockoff_operating_points\": {\n      \"0.05\": {\n        \"recall\": 0.08079847908745247,\n        \"precision\": 0.19362186788154898,\n        \"n_admit\": 439,\n        \"T\": 0.22272606129801784,\n        \"k_floor\": 20,\n        \"k_floor_met\": true\n      },\n      \"0.1\": {\n        \"recall\": 0.0817490494296578,\n        \"precision\": 0.18336886993603413,\n        \"n_admit\": 469,\n        \"T\": 0.0,\n        \"k_floor\": 10,\n        \"k_floor_met\": true\n      },\n      \"0.2\": {\n        \"recall\": 0.0817490494296578,\n        \"precision\": 0.18336886993603413,\n        \"n_admit\": 469,\n        \"T\": 0.0,\n        \"k_floor\": 5,\n        \"k_floor_met\": true\n      },\n      \"0.3\": {\n        \"recall\": 0.0817490494296578,\n        \"precision\": 0.18336886993603413,\n        \"n_admit\": 469,\n        \"T\": 0.0,\n        \"k_floor\": 4,\n        \"k_floor_met\": true\n      },\n      \"0.5\": {\n        \"recall\": 0.0817490494296578,\n        \"precision\": 0.18336886993603413,\n        \"n_admit\": 469,\n        \"T\": 0.0,\n        \"k_floor\": 2,\n        \"k_floor_met\": true\n      }\n    },\n    \"conformal_operating_points\": {\n      \"calibrated_on\": \"pilot\",\n      \"n_calibration_labels\": 259,\n      \"by_alpha\": {\n        \"0.05\": {\n          \"q_hat\": 1.0,\n          \"recall\": 0.0028517110266159697,\n          \"precision\": 0.6,\n          \"n_retained\": 5\n        },\n        \"0.1\": {\n          \"q_hat\": 1.0,\n          \"recall\": 0.0028517110266159697,\n          \"precision\": 0.6,\n          \"n_retained\": 5\n        },\n        \"0.2\": {\n          \"q_hat\": 1.0,\n          \"recall\": 0.0038022813688212928,\n          \"precision\": 0.5,\n          \"n_retained\": 8\n        },\n        \"0.3\": {\n          \"q_hat\": 1.0,\n          \"recall\": 0.011406844106463879,\n          \"precision\": 0.5217391304347826,\n          \"n_retained\": 23\n        },\n        \"0.5\": {\n          \"q_hat\": 1.0,\n          \"recall\": 0.015209125475285171,\n          \"precision\": 0.47058823529411764,\n          \"n_retained\": 34\n        }\n      },\n      \"note\": \"CONF is the LABELED reference (Mohri-Hashimoto conformal back-off): q-hat calibrated on the pilot split; the label-free decoy gate (METHOD) uses 0 labels. In the matched-recall grid CONF is swept by i...\"\n    },\n    \"hallucinated_conclusion_rate\": {\n      \"representative_recall\": 0.07518,\n      \"by_system\": {\n        \"METHOD\": {\n          \"point\": 0.5,\n          \"ci_lo\": 0.2857142857142857,\n          \"ci_hi\": 1.0,\n          \"n_derived\": 24,\n          \"n_hallucinated\": 12\n        },\n        \"PLAIN\": {\n          \"point\": 0.4782608695652174,\n          \"ci_lo\": 0.2820598006644518,\n          \"ci_hi\": 1.0,\n          \"n_derived\": 23,\n          \"n_hallucinated\": 11\n        },\n        \"CoT\": {\n          \"point\": null,\n          \"ci_lo\": null,\n          \"ci_hi\": null,\n          \"n_derived\": 0,\n          \"n_hallucinated\": 0\n        },\n        \"RAG\": {\n          \"point\": null,\n          \"ci_lo\": null,\n          \"ci_hi\": null,\n          \"n_derived\": 0,\n          \"n_hallucinated\": 0\n        },\n        \"CONF\": {\n          \"point\": 0.5,\n          \"ci_lo\": 0.1951923076923077,\n          \"ci_hi\": 1.0,\n          \"n_derived\": 18,\n          \"n_hallucinated\": 9\n        }\n      },\n      \"delta_method_minus_plain\": {\n        \"point\": 0.014187005234364981,\n        \"ci_lo\": 0.0,\n        \"ci_hi\": 0.04761904761904767\n      },\n      \"recall_grid\": [\n        0.05,\n        0.05148,\n        0.05296\n      ],\n      \"rate_by_system_grid\": {\n        \"METHOD\": [\n          0.375,\n          0.35294,\n          0.35294\n        ],\n        \"PLAIN\": [\n          0.33333,\n          0.35294,\n          0.35294\n        ],\n        \"CoT\": [\n          null,\n          null,\n          null\n        ],\n        \"RAG\": [\n          null,\n          null,\n          null\n        ],\n        \"CONF\": [\n          0.66667,\n          0.7,\n          0.7\n        ]\n      },\n      \"delta_grid\": [\n        0.04046,\n        0.0,\n        0.0\n      ],\n      \"delta_ci_grid\": [\n        [\n          0.0,\n          0.16667\n        ],\n        [\n          0.0,\n          0.0\n        ],\n        [\n          0.0,\n          0.0\n        ]\n      ],\n      \"note\": \"Read the METHOD-vs-PLAIN hallucination wedge at PARTIAL admission (representative_recall, ~70% of max): at max recall both admit the identical shared candidate pool so the delta is structurally 0. Abs...\"\n    },\n    \"alignment_check\": {\n      \"aligner_relation_accuracy\": 0.97814,\n      \"aligner_entitylink_accuracy\": 0.9943,\n      \"sensitivity\": {\n        \"baseline\": {\n          \"r_star\": 0.07518219264892269,\n          \"delta\": 0.0010567383243161518,\n          \"ci\": [\n            -0.0077429139019032905,\n            0.01103847262316117\n          ]\n        },\n        \"noise_5pct\": {\n          \"delta\": 0.003830948001447097,\n          \"ci\": [\n            -0.005043369795203653,\n            0.012641272173905775\n          ]\n        },\n        \"noise_10pct\": {\n          \"delta\": -0.01177826220064749,\n          \"ci\": [\n            -0.021053115770818157,\n            -0.0025272196653715125\n          ]\n        },\n        \"noise_20pct\": {\n          \"delta\": 0.0,\n          \"ci\": [\n            0.0,\n            0.0\n          ]\n        },\n        \"embed_only_aligner\": {\n          \"delta\": 0.0,\n          \"ci\": [\n            0.0,\n            0.0\n          ]\n        },\n        \"strict_el_floor_0.7\": {\n          \"delta\": 0.0005713551489344832,\n          \"ci\": [\n            -0.008358190489382779,\n            0.010099332053817398\n          ]\n        }\n      }\n    },\n    \"contamination_rate_decoys\": 0.12913,\n    \"verdict\": {\n      \"wedge_confirmed\": false,\n      \"disconfirmed\": true,\n      \"n_confirmed_points\": 0,\n      \"message\": \"OPERATIONAL DISCONFIRMATION (pre-registered): the wedge collapses to 'thresholding-is-enough' — no recall point shows a precision advantage of decoy-gating over the plain confidence threshold with CI ...\",\n      \"notes\": \"RELATIVE comparison only: Re-DocRED residual false negatives depress recall for ALL systems equally and inflate hallucinated-conclusion counts for ALL systems equally; no absolute realized-FDR diagona...\"\n    },\n    \"cost_log_summary\": {\n      \"total_usd\": 0.34744,\n      \"n_calls\": 8005,\n      \"soft_cap\": 3.0,\n      \"hard_stop\": 10.0\n    }\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"Re-DocRED\",\n      \"examples\": [\n        {\n          \"input\": \"Mikhail Borisovich Kogan (; September 5, 1893 in Zhitomir, Russian Empire – November 26, 1951 in Moscow, USSR) was a well - known medical doctor, a head of the therapy department of 2nd Moscow Medical...\",\n          \"output\": \"[[\\\"P569\\\", 0, 1], [\\\"P19\\\", 0, 2], [\\\"P570\\\", 0, 4], [\\\"P20\\\", 0, 5], [\\\"P17\\\", 2, 3], [\\\"P17\\\", 5, 6], [\\\"P577\\\", 13, 14], [\\\"P937\\\", 12, 5], [\\\"P27\\\", 0, 6], [\\\"P131\\\", 7, 5], [\\\"P27\\\", 12, 6], [\\\"P17\\\", 7, 6], [\\\"P131\\\", 5...\",\n          \"metadata_doc_id\": \"redocred_test_477\",\n          \"metadata_title\": \"Mikhail Kogan\",\n          \"metadata_fold\": \"cluster_PER\",\n          \"metadata_n_candidates\": 27,\n          \"metadata_n_gold\": 24,\n          \"predict_METHOD\": \"[[\\\"P569\\\", 0, 1, 0.9998], [\\\"P19\\\", 0, 2, 0.9981], [\\\"P131\\\", 2, 3, 0.9933], [\\\"P570\\\", 0, 4, 1.0], [\\\"P570\\\", 0, 5, 0.989], [\\\"P131\\\", 5, 6, 0.977], [\\\"P31\\\", 0, 13, 1.0], [\\\"P488\\\", 0, 7, -0.9999], [\\\"P108\\\", 0, 13,...\",\n          \"predict_PLAIN\": \"[[\\\"P569\\\", 0, 1, 0.9998], [\\\"P19\\\", 0, 2, 0.9981], [\\\"P131\\\", 2, 3, 0.9933], [\\\"P570\\\", 0, 4, 1.0], [\\\"P570\\\", 0, 5, 0.989], [\\\"P131\\\", 5, 6, 0.977], [\\\"P31\\\", 0, 13, 1.0], [\\\"P488\\\", 0, 7, 0.9998], [\\\"P108\\\", 0, 13, ...\",\n          \"predict_CoT\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P19\\\", 0, 2, 1.0], [\\\"P570\\\", 0, 4, 1.0], [\\\"P570\\\", 0, 5, 1.0], [\\\"P137\\\", 0, 13, 1.0], [\\\"P39\\\", 0, 7, 1.0], [\\\"P570\\\", 0, 13, 1.0], [\\\"P3373\\\", 0, 13, 0.8]]\",\n          \"predict_RAG\": \"[[\\\"P19\\\", 0, 2, 1.0], [\\\"P570\\\", 0, 5, 1.0], [\\\"P108\\\", 0, 7, 1.0], [\\\"P570\\\", 0, 14, 1.0], [\\\"P3373\\\", 0, 13, 0.7]]\",\n          \"predict_CONF\": \"[[\\\"P569\\\", 0, 1, 0.8999], [\\\"P19\\\", 0, 2, 0.999], [\\\"P131\\\", 2, 3, 0.7967], [\\\"P570\\\", 0, 4, 0.9], [\\\"P570\\\", 0, 5, 0.9945], [\\\"P131\\\", 5, 6, 0.7885], [\\\"P31\\\", 0, 13, 0.9], [\\\"P488\\\", 0, 7, 0.8999], [\\\"P108\\\", 0, 13,...\"\n        },\n        {\n          \"input\": \"Julian Reinard (born 5 March 1983) is a German footballer. He first appeared in the German Bundesliga on 21 March 2004 while SC Freiburg's first and second keepers had been injured. A year later media...\",\n          \"output\": \"[[\\\"P569\\\", 0, 1], [\\\"P54\\\", 0, 12], [\\\"P118\\\", 0, 3], [\\\"P54\\\", 0, 8], [\\\"P27\\\", 0, 2], [\\\"P54\\\", 0, 9], [\\\"P17\\\", 3, 2], [\\\"P118\\\", 5, 3], [\\\"P463\\\", 0, 5], [\\\"P17\\\", 5, 2], [\\\"P17\\\", 8, 11], [\\\"P118\\\", 7, 3], [\\\"P17\\\", 9, 1...\",\n          \"metadata_doc_id\": \"redocred_test_445\",\n          \"metadata_title\": \"Julian Reinard\",\n          \"metadata_fold\": \"cluster_ORG\",\n          \"metadata_n_candidates\": 29,\n          \"metadata_n_gold\": 17,\n          \"predict_METHOD\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P279\\\", 0, 2, 1.0], [\\\"P1344\\\", 0, 3, 1.0], [\\\"P571\\\", 0, 4, 1.0], [\\\"P118\\\", 0, 8, 1.0], [\\\"P118\\\", 0, 11, 1.0], [\\\"P118\\\", 0, 9, 1.0], [\\\"P576\\\", 0, 9, 0.9914], [\\\"P571\\\", 0, 4, 0.9999], [\\\"...\",\n          \"predict_PLAIN\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P279\\\", 0, 2, 1.0], [\\\"P1344\\\", 0, 3, 1.0], [\\\"P571\\\", 0, 4, 1.0], [\\\"P118\\\", 0, 8, 1.0], [\\\"P118\\\", 0, 11, 1.0], [\\\"P118\\\", 0, 9, 1.0], [\\\"P576\\\", 0, 9, 0.9914], [\\\"P571\\\", 0, 4, 0.9999], [\\\"...\",\n          \"predict_CoT\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P27\\\", 0, 2, 1.0], [\\\"P54\\\", 0, 5, 1.0], [\\\"P54\\\", 0, 7, 0.9], [\\\"P54\\\", 0, 8, 1.0], [\\\"P54\\\", 0, 12, 0.8]]\",\n          \"predict_RAG\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P279\\\", 0, 2, 1.0], [\\\"P1344\\\", 0, 3, 1.0], [\\\"P54\\\", 0, 5, 1.0], [\\\"P118\\\", 0, 11, 1.0], [\\\"P118\\\", 0, 8, 1.0], [\\\"P118\\\", 0, 12, 1.0]]\",\n          \"predict_CONF\": \"[[\\\"P569\\\", 0, 1, 1.0], [\\\"P279\\\", 0, 2, 1.0], [\\\"P1344\\\", 0, 3, 1.0], [\\\"P571\\\", 0, 4, 0.9], [\\\"P118\\\", 0, 8, 1.0], [\\\"P118\\\", 0, 11, 0.9], [\\\"P118\\\", 0, 9, 0.9], [\\\"P576\\\", 0, 9, 0.8957], [\\\"P571\\\", 0, 4, 0.9], [\\\"P60...\"\n        },\n        {\n          \"input\": \"Baltimore and Ohio Railroad Martinsburg Shops is a historic industrial district in Martinsburg, West Virginia. It is significant both for its railroading architecture by Albert Fink and John Rudolph N...\",\n          \"output\": \"[[\\\"P17\\\", 1, 8], [\\\"P17\\\", 2, 8], [\\\"P131\\\", 2, 8], [\\\"P585\\\", 5, 6], [\\\"P150\\\", 8, 2], [\\\"P131\\\", 0, 2], [\\\"P17\\\", 0, 8], [\\\"P17\\\", 12, 8], [\\\"P17\\\", 9, 8], [\\\"P279\\\", 11, 12], [\\\"P17\\\", 5, 8], [\\\"P131\\\", 0, 1], [\\\"P17\\\", 11...\",\n          \"metadata_doc_id\": \"redocred_dev_459\",\n          \"metadata_title\": \"Baltimore and Ohio Railroad Martinsburg Shops\",\n          \"metadata_fold\": \"cluster_LOC\",\n          \"metadata_n_candidates\": 25,\n          \"metadata_n_gold\": 19,\n          \"predict_METHOD\": \"[[\\\"P131\\\", 0, 2, 1.0], [\\\"P800\\\", 0, 4, 0.6792], [\\\"P710\\\", 0, 5, 0.852], [\\\"P527\\\", 0, 7, 0.9998], [\\\"P569\\\", 0, 8, 0.9985], [\\\"P1441\\\", 9, 1, 0.9998], [\\\"P585\\\", 9, 10, 0.9994], [\\\"P37\\\", 0, 11, 0.982], [\\\"P706\\\", 0...\",\n          \"predict_PLAIN\": \"[[\\\"P131\\\", 0, 2, 1.0], [\\\"P800\\\", 0, 4, 0.6792], [\\\"P710\\\", 0, 5, 0.852], [\\\"P527\\\", 0, 7, 0.9998], [\\\"P569\\\", 0, 8, 0.9985], [\\\"P1441\\\", 9, 1, 0.9998], [\\\"P585\\\", 9, 10, 0.9994], [\\\"P37\\\", 0, 11, 0.982], [\\\"P706\\\", 0...\",\n          \"predict_CoT\": \"[[\\\"P131\\\", 0, 2, 1.0], [\\\"P1441\\\", 9, 1, 1.0], [\\\"P571\\\", 9, 10, 1.0], [\\\"P37\\\", 0, 11, 1.0], [\\\"P131\\\", 0, 12, 1.0], [\\\"P361\\\", 0, 8, 0.9]]\",\n          \"predict_RAG\": \"[[\\\"P131\\\", 0, 2, 1.0], [\\\"P131\\\", 9, 1, 1.0], [\\\"P585\\\", 9, 10, 1.0], [\\\"P170\\\", 0, 4, 1.0], [\\\"P161\\\", 0, 5, 1.0], [\\\"P37\\\", 0, 11, 1.0], [\\\"P131\\\", 0, 12, 1.0], [\\\"P527\\\", 0, 7, 1.0]]\",\n          \"predict_CONF\": \"[[\\\"P131\\\", 0, 2, 0.9], [\\\"P800\\\", 0, 4, 0.4396], [\\\"P710\\\", 0, 5, 0.726], [\\\"P527\\\", 0, 7, 0.4999], [\\\"P569\\\", 0, 8, 0.5992], [\\\"P1441\\\", 9, 1, 0.9999], [\\\"P585\\\", 9, 10, 0.6997], [\\\"P37\\\", 0, 11, 0.891], [\\\"P706\\\", 0...\"\n        }\n      ]\n    }\n  ]\n}", "numLines": 566, "startLine": 1, "totalLines": 566}}
```

### [16] ASSISTANT · 2026-06-16 13:06:00 UTC

```
Let me read the analysis and common modules to understand the data structures and pure-analysis functions.
```

### [17] TOOL CALL — Read · 2026-06-16 13:06:00 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/analyze.py
```

### [18] TOOL RESULT — Read · 2026-06-16 13:06:00 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/analyze.py", "content": "#!/usr/bin/env python3\n\"\"\"Stage 2 (pure-Python + small memoized relation-pick API): map every system into the\nshared (title, P-code, head_id, tail_id) space via ONE fixed aligner, score by the official\ntuple-matching metric, and produce the matched-recall wedge, multi-hop hallucination rate,\nknockoff+ operating points, document-block bootstrap CIs, and the alignment confound check.\"\"\"\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport math\nimport random\nfrom pathlib import Path\n\nimport numpy as np\nfrom loguru import logger\n\nimport prompts\nfrom common import (ALIGN_CACHE_FILE, CONFIG, RULES, Embedder, build_pcode_embeddings,\n                    load_relation_schema, norm)\nfrom llm import LLM\n\nSYSTEMS = [\"METHOD\", \"PLAIN\", \"CoT\", \"RAG\", \"CONF\"]\n\n\n# ======================================================================================\n# RELATION ALIGNMENT (hybrid: MiniLM shortlist + temp-0 LLM pick; embedding fallback)\n# ======================================================================================\nclass Aligner:\n    def __init__(self, embedder: Embedder, rel_schema: list[dict]):\n        self.emb = embedder\n        self.np = np\n        self.pcodes, self.pcode_emb, self.pmap = build_pcode_embeddings(embedder, rel_schema)\n        self.rel_cache: dict[str, str] = {}\n        if ALIGN_CACHE_FILE.exists():\n            try:\n                self.rel_cache = json.loads(ALIGN_CACHE_FILE.read_text())\n            except Exception:\n                self.rel_cache = {}\n\n    def _shortlist(self, phrase: str):\n        e = self.emb.encode_cached([phrase])[0]\n        sims = self.pcode_emb @ e\n        idx = np.argsort(-sims)[: CONFIG[\"align_shortlist_k\"]]\n        return [(self.pcodes[i], self.pmap[self.pcodes[i]][\"relation_name\"],\n                 self.pmap[self.pcodes[i]][\"relation_description\"], float(sims[i])) for i in idx]\n\n    def embed_only_pcode(self, phrase: str) -> str | None:\n        e = self.emb.encode_cached([phrase])[0]\n        sims = self.pcode_emb @ e\n        i = int(np.argmax(sims))\n        return self.pcodes[i] if sims[i] >= CONFIG[\"align_embed_floor\"] else None\n\n    async def resolve_phrases(self, phrases: list[str], cost_meter):\n        \"\"\"Resolve unique relation phrases to P-codes via the LLM picker (memoized+cached).\"\"\"\n        uniq = sorted({norm(p) for p in phrases if p and p.strip()})\n        todo = [p for p in uniq if p not in self.rel_cache]\n        logger.info(f\"Relation alignment: {len(uniq)} unique phrases, {len(todo)} need LLM pick\")\n        if not todo:\n            return\n        async with LLM(cost_meter) as llm:\n            sem = asyncio.Semaphore(CONFIG[\"global_concurrency\"])\n\n            async def pick(phrase):\n                async with sem:\n                    shortlist = self._shortlist(phrase)\n                    from common import parse_json_obj\n                    content, _ = await llm.chat(\n                        prompts.relation_pick_prompt(phrase, [(p, n, d) for p, n, d, _ in shortlist]),\n                        max_tokens=20, temperature=CONFIG[\"temperature_align\"], tag=\"rel_pick\")\n                    obj = parse_json_obj(content) if content else None\n                    pc = obj.get(\"pcode\") if isinstance(obj, dict) else None\n                    valid = {p for p, _, _, _ in shortlist}\n                    if pc == \"NO_RELATION\":\n                        result = None\n                    elif pc in valid:\n                        result = pc\n                    else:  # embedding fallback\n                        top_pc, _, _, top_sim = shortlist[0]\n                        result = top_pc if top_sim >= CONFIG[\"align_embed_floor\"] else None\n                    self.rel_cache[phrase] = result if result else \"NO_RELATION\"\n\n            await asyncio.gather(*(pick(p) for p in todo))\n        ALIGN_CACHE_FILE.write_text(json.dumps(self.rel_cache))\n\n    def relation_pcode(self, phrase: str, mode: str = \"hybrid\") -> str | None:\n        if mode == \"embed_only\":\n            return self.embed_only_pcode(phrase)\n        pc = self.rel_cache.get(norm(phrase))\n        if pc is None:  # not resolved -> embedding fallback\n            return self.embed_only_pcode(phrase)\n        return None if pc == \"NO_RELATION\" else pc\n\n\n# ======================================================================================\n# ENTITY LINKING (three tiers: exact -> alias/substring -> embedding floor)\n# ======================================================================================\ndef build_doc_entity_index(embedder: Embedder, entities: list[dict]):\n    exact = {}\n    alias = []  # (norm_name, entity_id, length)\n    canon_names, canon_ids = [], []\n    for e in entities:\n        eid = e[\"entity_id\"]\n        names = set(e.get(\"aliases\") or []) | {e.get(\"canonical_name\", \"\")}\n        for nm in names:\n            nn = norm(nm)\n            if not nn:\n                continue\n            exact.setdefault(nn, eid)\n            alias.append((nn, eid, len(nn)))\n        canon_names.append(e.get(\"canonical_name\", \"\") or (e.get(\"aliases\") or [\"\"])[0])\n        canon_ids.append(eid)\n    canon_emb = embedder.encode_cached(canon_names) if canon_names else np.zeros((0, 384))\n    return {\"exact\": exact, \"alias\": alias, \"canon_emb\": canon_emb, \"canon_ids\": canon_ids}\n\n\ndef link_entity(surface: str, idx: dict, embedder: Embedder, floor: float) -> int | None:\n    s = norm(surface)\n    if not s:\n        return None\n    if s in idx[\"exact\"]:\n        return idx[\"exact\"][s]\n    # tier 2: substring (longest matching alias)\n    best = None\n    for nn, eid, ln in idx[\"alias\"]:\n        if ln < 3 or len(s) < 3:\n            continue\n        if s in nn or nn in s:\n            score = min(len(s), ln)\n            if best is None or score > best[0]:\n                best = (score, eid)\n    if best is not None:\n        return best[1]\n    # tier 3: embedding\n    if len(idx[\"canon_ids\"]) == 0:\n        return None\n    e = embedder.encode_cached([surface])[0]\n    sims = idx[\"canon_emb\"] @ e\n    i = int(np.argmax(sims))\n    return idx[\"canon_ids\"][i] if sims[i] >= floor else None\n\n\n# ======================================================================================\n# BUILD PER-SYSTEM ALIGNED ITEMS  (title, pcode, h_id, t_id, score)\n# ======================================================================================\ndef conf_frequency(cand: dict, samples: list[list[dict]]) -> float:\n    \"\"\"Fraction of stochastic samples containing a triple matching the candidate\n    (token-Jaccard >= 0.5 on both head and tail).\"\"\"\n    if not samples:\n        return 0.0\n    ch, ct = set(norm(cand[\"head\"]).split()), set(norm(cand[\"tail\"]).split())\n    if not ch or not ct:\n        return 0.0\n    def jac(a, b):\n        return len(a & b) / max(1, len(a | b))\n    hits = 0\n    for samp in samples:\n        found = False\n        for tr in samp:\n            sh, st = set(norm(tr.get(\"head\", \"\")).split()), set(norm(tr.get(\"tail\", \"\")).split())\n            if jac(ch, sh) >= 0.5 and jac(ct, st) >= 0.5:\n                found = True\n                break\n        if found:\n            hits += 1\n    return hits / len(samples)\n\n\ndef align_records(records: list[dict], aligner: Aligner, embedder: Embedder,\n                  mode: str = \"hybrid\", el_floor: float | None = None):\n    \"\"\"Returns dict: system -> list of items {title,pcode,h_id,t_id,score,doc}. Items keep\n    pcode separate so alignment-noise sensitivity can be applied downstream.\"\"\"\n    el_floor = el_floor if el_floor is not None else CONFIG[\"el_embed_floor\"]\n    out = {s: [] for s in SYSTEMS}\n    for rec in records:\n        title = rec[\"title\"]\n        eidx = build_doc_entity_index(embedder, rec[\"entities\"])\n\n        def align(h, r, t):\n            pc = aligner.relation_pcode(r, mode=mode)\n            if pc is None:\n                return None\n            hid = link_entity(h, eidx, embedder, el_floor)\n            tid = link_entity(t, eidx, embedder, el_floor)\n            if hid is None or tid is None:\n                return None\n            return (pc, hid, tid)\n\n        # METHOD + PLAIN share the SAME candidate pool (W computable) -> identical recall ceiling\n        for c in rec[\"candidates\"]:\n            if c.get(\"W\") is None:\n                continue\n            a = align(c[\"head\"], c[\"relation\"], c[\"tail\"])\n            if a is None:\n                continue\n            pc, hid, tid = a\n            base = {\"title\": title, \"pcode\": pc, \"h_id\": hid, \"t_id\": tid, \"doc\": title}\n            out[\"METHOD\"].append({**base, \"score\": c[\"W\"]})\n            out[\"PLAIN\"].append({**base, \"score\": c[\"Z\"]})\n            # CONF: combined frequency + gpt(Z)\n            freq = conf_frequency(c, rec.get(\"conf_samples\", []))\n            combined = 0.5 * freq + 0.5 * (c[\"Z\"] if c[\"Z\"] is not None else 0.0)\n            out[\"CONF\"].append({**base, \"score\": combined})\n        for sysname, key in ((\"CoT\", \"cot\"), (\"RAG\", \"rag\")):\n            for tr in rec.get(key, []):\n                a = align(tr[\"head\"], tr[\"relation\"], tr[\"tail\"])\n                if a is None:\n                    continue\n                pc, hid, tid = a\n                out[sysname].append({\"title\": title, \"pcode\": pc, \"h_id\": hid, \"t_id\": tid,\n                                     \"doc\": title, \"score\": float(tr.get(\"confidence\", 0.5))})\n    return out\n\n\ndef build_gold(records: list[dict]):\n    gold = set()\n    gold_by_doc = {}\n    for rec in records:\n        title = rec[\"title\"]\n        gset = gold_by_doc.setdefault(title, set())\n        for g in rec[\"gold_triples\"]:\n            tup = (title, g[\"relation_pid\"], g[\"head_id\"], g[\"tail_id\"])\n            gold.add(tup)\n            gset.add(tup)\n    return gold, gold_by_doc\n\n\n# ======================================================================================\n# METRIC: PR CURVE + matched-recall machinery\n# ======================================================================================\ndef materialize(items, gold, noise_p=0.0, seed=0, pcodes=None):\n    \"\"\"Collapse aligned items to unique tuples with max score; mark correctness. Optional\n    uniform P-code corruption (alignment-noise sensitivity).\"\"\"\n    rng = random.Random(seed)\n    tuples = {}\n    for it in items:\n        pc = it[\"pcode\"]\n        if noise_p > 0 and pcodes and rng.random() < noise_p:\n            pc = rng.choice([p for p in pcodes if p != pc])\n        tup = (it[\"title\"], pc, it[\"h_id\"], it[\"t_id\"])\n        sc = it[\"score\"]\n        if sc is None:\n            continue\n        if tup not in tuples or sc > tuples[tup][0]:\n            tuples[tup] = (sc, it[\"doc\"])\n    recs = [{\"tuple\": k, \"score\": v[0], \"doc\": v[1], \"correct\": k in gold}\n            for k, v in tuples.items()]\n    recs.sort(key=lambda r: r[\"score\"], reverse=True)\n    return recs\n\n\ndef pr_curve(recs, total_gold):\n    pts = []\n    correct = sub = 0\n    for r in recs:\n        sub += 1\n        if r[\"correct\"]:\n            correct += 1\n        pts.append((correct / max(1, total_gold), correct / sub, r[\"score\"]))\n    return pts\n\n\ndef threshold_for_recall(recs, total_gold, r_star):\n    \"\"\"Smallest score-threshold (most permissive) whose admitted set reaches recall>=r_star.\"\"\"\n    correct = sub = 0\n    for r in recs:\n        sub += 1\n        if r[\"correct\"]:\n            correct += 1\n        if correct / max(1, total_gold) >= r_star:\n            return r[\"score\"], correct / sub  # (threshold, precision at that point)\n    return (recs[-1][\"score\"] if recs else 0.0), (correct / max(1, sub))\n\n\ndef per_doc_stats(recs, thr, doc_list):\n    \"\"\"For a fixed threshold, per-doc (submitted, correct) counts over admitted tuples.\"\"\"\n    sub = {d: 0 for d in doc_list}\n    cor = {d: 0 for d in doc_list}\n    for r in recs:\n        if r[\"score\"] >= thr:\n            sub[r[\"doc\"]] += 1\n            if r[\"correct\"]:\n                cor[r[\"doc\"]] += 1\n    return (np.array([sub[d] for d in doc_list], float),\n            np.array([cor[d] for d in doc_list], float))\n\n\ndef admitted_by_doc(recs, thr):\n    by = {}\n    for r in recs:\n        if r[\"score\"] >= thr:\n            by.setdefault(r[\"doc\"], []).append(r[\"tuple\"])\n    return by\n\n\n# ======================================================================================\n# MULTI-HOP FORWARD CHAINING (hallucinated-conclusion rate)\n# ======================================================================================\ndef forward_chain(facts: set, max_iter: int = 6) -> set:\n    facts = set(facts)\n    by_rel = {}\n    for (r, h, t) in facts:\n        by_rel.setdefault(r, set()).add((h, t))\n    derived = set()\n    changed = True\n    it = 0\n    while changed and it < max_iter:\n        changed = False\n        it += 1\n        for rule in RULES:\n            subs = [{}]\n            for (r, a, b) in rule[\"body\"]:\n                nxt = []\n                for s in subs:\n                    for (h, t) in by_rel.get(r, ()):\n                        s2 = dict(s)\n                        ok = True\n                        for var, val in ((a, h), (b, t)):\n                            if var in s2 and s2[var] != val:\n                                ok = False\n                                break\n                            s2[var] = val\n                        if ok:\n                            nxt.append(s2)\n                subs = nxt\n                if not subs:\n                    break\n            r, a, b = rule[\"head\"]\n            for s in subs:\n                if a in s and b in s and s[a] != s[b]:\n                    f = (r, s[a], s[b])\n                    if f not in facts:\n                        facts.add(f)\n                        by_rel.setdefault(r, set()).add((s[a], s[b]))\n                        derived.add(f)\n                        changed = True\n    return derived\n\n\ndef hallu_per_doc(admitted, gold_by_doc, doc_list):\n    \"\"\"Per-doc (n_derived, n_hallucinated) from forward chaining admitted atomic facts.\"\"\"\n    nd = {d: 0 for d in doc_list}\n    nh = {d: 0 for d in doc_list}\n    for d, tuples in admitted.items():\n        facts = {(pc, h, t) for (_, pc, h, t) in tuples}\n        derived = forward_chain(facts)\n        gset = gold_by_doc.get(d, set())\n        nd[d] = len(derived)\n        nh[d] = sum(1 for (pc, h, t) in derived if (d, pc, h, t) not in gset)\n    return (np.array([nd[x] for x in doc_list], float),\n            np.array([nh[x] for x in doc_list], float))\n\n\n# ======================================================================================\n# KNOCKOFF+ THRESHOLD (research_1 A.6, eq. 1.9)\n# ======================================================================================\ndef knockoff_plus_threshold(W: list[float], alpha: float):\n    if not W:\n        return None\n    mags = sorted({abs(w) for w in W})\n    for t in mags:\n        pos = sum(1 for w in W if w >= t)\n        neg = sum(1 for w in W if w <= -t)\n        fdr_hat = (1 + neg) / max(1, pos)\n        if fdr_hat <= alpha:\n            return t\n    return None\n\n\n# ======================================================================================\n# CONFORMAL (Mohri-Hashimoto) calibrated operating points for the LABELED reference (CONF)\n# ======================================================================================\ndef conformal_operating_points(calib_items_by_doc, test_items, gold_total, alphas):\n    \"\"\"q-hat = ceil((n+1)(1-alpha))/n quantile of per-doc back-off scores; retain sub-claims\n    with combined score > q-hat. calib_items_by_doc: {doc: [(score, correct)...]}.\n    test_items: [(score, correct)...] (materialized unique CONF tuples on the test split).\"\"\"\n    r_list = []\n    for doc, items in calib_items_by_doc.items():\n        inc = [s for s, c in items if not c]\n        # r_doc = smallest cutoff that excludes every incorrect retained claim\n        r_list.append(max(inc) if inc else -1.0)\n    n = max(1, len(r_list))\n    r_sorted = sorted(r_list)\n    out = {}\n    for alpha in alphas:\n        k = math.ceil((n + 1) * (1 - alpha))\n        k = min(max(k, 1), n)\n        qhat = r_sorted[k - 1]\n        retained = [(s, c) for (s, c) in test_items if s > qhat]\n        n_ret = len(retained)\n        cor = sum(1 for s, c in retained if c)\n        out[str(alpha)] = {\"q_hat\": round(float(qhat), 5),\n                           \"recall\": cor / max(1, gold_total),\n                           \"precision\": cor / max(1, n_ret), \"n_retained\": n_ret}\n    return out\n\n\n# ======================================================================================\n# DOCUMENT-BLOCK BOOTSTRAP (B>=2000), vectorized via shared multinomial count matrix\n# ======================================================================================\ndef make_boot_counts(n_docs, B, seed):\n    rng = np.random.default_rng(seed)\n    return rng.multinomial(n_docs, [1.0 / n_docs] * n_docs, size=B).astype(float)  # (B, D)\n\n\ndef ratio_ci(counts, num_vec, den_vec):\n    num = counts @ num_vec\n    den = counts @ den_vec\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        vals = np.where(den > 0, num / den, np.nan)\n    vals = vals[~np.isnan(vals)]\n    if len(vals) == 0:\n        return (float(\"nan\"), float(\"nan\"))\n    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))\n\n\ndef diff_ci(counts, numA, denA, numB, denB):\n    a = counts @ numA\n    da = counts @ denA\n    b = counts @ numB\n    db = counts @ denB\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        va = np.where(da > 0, a / da, np.nan)\n        vb = np.where(db > 0, b / db, np.nan)\n    d = va - vb\n    d = d[~np.isnan(d)]\n    if len(d) == 0:\n        return (float(\"nan\"), float(\"nan\"), float(\"nan\"))\n    return (float(np.mean(d)), float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5)))\n", "numLines": 429, "startLine": 1, "totalLines": 429}}
```

### [19] TOOL CALL — Read · 2026-06-16 13:06:00 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/common.py
```

### [20] TOOL RESULT — Read · 2026-06-16 13:06:00 UTC

````
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/common.py", "content": "#!/usr/bin/env python3\n\"\"\"Shared config, cost meter, parsing helpers, embedding + alignment core for the\nRe-DocRED operational-wedge experiment (decoy-gating vs plain confidence threshold).\n\nThis module is imported by both the extraction stage (method.py --stage extract)\nand the analysis stage (method.py --stage analyze).\n\"\"\"\nfrom __future__ import annotations\n\nimport json\nimport math\nimport re\nimport sys\nimport threading\nfrom pathlib import Path\n\nfrom loguru import logger\n\n# --------------------------------------------------------------------------------------\n# PATHS\n# --------------------------------------------------------------------------------------\nWORKSPACE = Path(__file__).resolve().parent\nDEP_DATA_DIR = Path(\n    \"/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_1/gen_art/gen_art_dataset_2\"\n)\nFULL_DATA = DEP_DATA_DIR / \"full_data_out.json\"\nMINI_DATA = DEP_DATA_DIR / \"mini_data_out.json\"\nRELATION_SCHEMA = DEP_DATA_DIR / \"relation_schema.json\"\nENTITY_TYPE_SCHEMA = DEP_DATA_DIR / \"entity_type_schema.json\"\n\nCKPT_DIR = WORKSPACE / \"checkpoints\"\nLOGS_DIR = WORKSPACE / \"logs\"\nCACHE_DIR = WORKSPACE / \"cache\"\nfor _d in (CKPT_DIR, LOGS_DIR, CACHE_DIR):\n    _d.mkdir(parents=True, exist_ok=True)\n\nCOST_LOG = LOGS_DIR / \"cost.jsonl\"\nALIGN_CACHE_FILE = CACHE_DIR / \"align_relation_cache.json\"\nPCODE_EMB_FILE = CACHE_DIR / \"pcode_embeddings.npz\"\n\n# --------------------------------------------------------------------------------------\n# CONFIG\n# --------------------------------------------------------------------------------------\nCONFIG = dict(\n    model_primary=\"openai/gpt-4.1-nano\",\n    model_fallbacks=[\"openai/gpt-4o-mini\"],\n    # extraction / scoring\n    temperature_extract=0.7,\n    n_overgen=3,\n    cand_cap=30,\n    temperature_score=0.0,\n    temperature_decoy=0.9,\n    temperature_align=0.0,\n    elicitation=\"logprob_yes_token (verbalized_[0,1] fallback)\",\n    n_conf_samples=5,\n    decoy_max_regen=3,\n    # FDR gate\n    alpha_grid=[0.05, 0.10, 0.20, 0.30, 0.50],\n    W_floor_k={0.05: 20, 0.10: 10, 0.20: 5, 0.30: 4, 0.50: 2},\n    # alignment / entity linking\n    align_shortlist_k=8,\n    align_embed_floor=0.45,\n    el_embed_floor=0.6,\n    el_strict_floor=0.7,\n    conf_match_floor=0.7,\n    # evaluation\n    bootstrap_B=2000,\n    recall_grid_n=25,\n    noise_levels=[0.05, 0.10, 0.20],\n    # budget / concurrency\n    soft_cap_usd=3.0,\n    hard_stop_usd=10.0,\n    global_concurrency=32,\n    doc_concurrency=10,\n    seed=20240617,\n    embed_model=\"sentence-transformers/all-MiniLM-L6-v2\",\n)\n\n# gpt-4.1-nano fallback pricing (USD per token) if usage.cost ever missing\nPRICE = {\n    \"openai/gpt-4.1-nano\": (0.10e-6, 0.40e-6),\n    \"openai/gpt-4o-mini\": (0.15e-6, 0.60e-6),\n}\n\n# Multi-hop Datalog rules over Re-DocRED relations (gold-justified, well-known).\n# Each: name, body list of (pcode, var_head, var_tail), head (pcode, var_head, var_tail).\nRULES = [\n    {\"name\": \"transitive_located_in_admin (P131;P131->P131)\",\n     \"body\": [(\"P131\", \"X\", \"Y\"), (\"P131\", \"Y\", \"Z\")], \"head\": (\"P131\", \"X\", \"Z\")},\n    {\"name\": \"located_in_admin_then_country (P131;P17->P17)\",\n     \"body\": [(\"P131\", \"X\", \"Y\"), (\"P17\", \"Y\", \"Z\")], \"head\": (\"P17\", \"X\", \"Z\")},\n    {\"name\": \"transitive_contains_admin (P150;P150->P150)\",\n     \"body\": [(\"P150\", \"X\", \"Y\"), (\"P150\", \"Y\", \"Z\")], \"head\": (\"P150\", \"X\", \"Z\")},\n    {\"name\": \"transitive_part_of (P361;P361->P361)\",\n     \"body\": [(\"P361\", \"X\", \"Y\"), (\"P361\", \"Y\", \"Z\")], \"head\": (\"P361\", \"X\", \"Z\")},\n    {\"name\": \"transitive_has_part (P527;P527->P527)\",\n     \"body\": [(\"P527\", \"X\", \"Y\"), (\"P527\", \"Y\", \"Z\")], \"head\": (\"P527\", \"X\", \"Z\")},\n    {\"name\": \"sibling_shares_father (P3373;P22->P22)\",\n     \"body\": [(\"P3373\", \"X\", \"Y\"), (\"P22\", \"Y\", \"Z\")], \"head\": (\"P22\", \"X\", \"Z\")},\n    {\"name\": \"sibling_shares_mother (P3373;P25->P25)\",\n     \"body\": [(\"P3373\", \"X\", \"Y\"), (\"P25\", \"Y\", \"Z\")], \"head\": (\"P25\", \"X\", \"Z\")},\n    {\"name\": \"capital_of_implies_located_in (P36->P131)\",\n     \"body\": [(\"P36\", \"X\", \"Y\")], \"head\": (\"P131\", \"X\", \"Y\")},\n    {\"name\": \"sibling_symmetric (P3373->P3373)\",\n     \"body\": [(\"P3373\", \"X\", \"Y\")], \"head\": (\"P3373\", \"Y\", \"X\")},\n    {\"name\": \"spouse_symmetric (P26->P26)\",\n     \"body\": [(\"P26\", \"X\", \"Y\")], \"head\": (\"P26\", \"Y\", \"X\")},\n]\n\n\n# --------------------------------------------------------------------------------------\n# LOGGING\n# --------------------------------------------------------------------------------------\ndef setup_logging(tag: str = \"run\") -> None:\n    logger.remove()\n    logger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\n    logger.add(LOGS_DIR / f\"{tag}.log\", rotation=\"30 MB\", level=\"DEBUG\", enqueue=True)\n\n\n# --------------------------------------------------------------------------------------\n# COST METER  (thread/async safe; OpenRouter returns exact usage.cost in USD)\n# --------------------------------------------------------------------------------------\nclass BudgetExceeded(Exception):\n    pass\n\n\nclass CostMeter:\n    def __init__(self, hard_stop: float, soft_cap: float, persist: bool = True):\n        self.hard_stop = hard_stop\n        self.soft_cap = soft_cap\n        self.total = 0.0\n        self.n_calls = 0\n        self._lock = threading.Lock()\n        self._persist = persist\n        # resume cumulative total across stages/runs from cost.jsonl\n        if persist and COST_LOG.exists():\n            try:\n                for line in COST_LOG.read_text().splitlines():\n                    rec = json.loads(line)\n                    self.total = rec.get(\"cumulative\", self.total)\n                    self.n_calls += 1\n                logger.info(f\"Resumed cost meter: ${self.total:.4f} over {self.n_calls} prior calls\")\n            except Exception:\n                logger.warning(\"Could not parse existing cost.jsonl; starting fresh counter\")\n\n    def add(self, usage: dict, model: str, tag: str = \"\") -> float:\n        cost = usage.get(\"cost\")\n        if cost is None:\n            pin, pout = PRICE.get(model, (0.10e-6, 0.40e-6))\n            cost = usage.get(\"prompt_tokens\", 0) * pin + usage.get(\"completion_tokens\", 0) * pout\n        with self._lock:\n            self.total += cost\n            self.n_calls += 1\n            cum = self.total\n            n = self.n_calls\n        if self._persist:\n            with self._lock:\n                with COST_LOG.open(\"a\") as f:\n                    f.write(json.dumps({\"tag\": tag, \"cost\": cost, \"cumulative\": cum,\n                                        \"model\": model, \"n\": n}) + \"\\n\")\n        if cum >= self.hard_stop:\n            raise BudgetExceeded(f\"HARD STOP: cumulative ${cum:.4f} >= ${self.hard_stop}\")\n        return cost\n\n    def over_soft(self) -> bool:\n        return self.total >= self.soft_cap\n\n\n# --------------------------------------------------------------------------------------\n# PARSING HELPERS (robust to LLM formatting noise)\n# --------------------------------------------------------------------------------------\n_FENCE = re.compile(r\"^```[a-zA-Z]*\\n?|```$\", re.MULTILINE)\n\n\ndef strip_fences(s: str) -> str:\n    return _FENCE.sub(\"\", s).strip()\n\n\ndef parse_json_obj(text: str):\n    \"\"\"Extract the first JSON object from a possibly noisy LLM response.\"\"\"\n    if not text:\n        return None\n    t = strip_fences(text)\n    try:\n        return json.loads(t)\n    except Exception:\n        pass\n    # find first {...} balanced\n    start = t.find(\"{\")\n    while start != -1:\n        depth = 0\n        for i in range(start, len(t)):\n            if t[i] == \"{\":\n                depth += 1\n            elif t[i] == \"}\":\n                depth -= 1\n                if depth == 0:\n                    frag = t[start:i + 1]\n                    try:\n                        return json.loads(frag)\n                    except Exception:\n                        break\n        start = t.find(\"{\", start + 1)\n    return None\n\n\ndef parse_prob(text: str) -> float | None:\n    \"\"\"Parse a probability in [0,1] from an LLM response (json {'p':..} or bare number).\"\"\"\n    obj = parse_json_obj(text)\n    if isinstance(obj, dict):\n        for k in (\"p\", \"probability\", \"prob\", \"confidence\", \"score\"):\n            if k in obj:\n                try:\n                    v = float(obj[k])\n                    if v > 1.0:  # model may give 0..100\n                        v = v / 100.0\n                    return min(1.0, max(0.0, v))\n                except Exception:\n                    pass\n    if text:\n        m = re.search(r\"(\\d+\\.\\d+|\\d+)\", strip_fences(text))\n        if m:\n            try:\n                v = float(m.group(1))\n                if v > 1.0:\n                    v = v / 100.0\n                return min(1.0, max(0.0, v))\n            except Exception:\n                return None\n    return None\n\n\n_YES = {\"yes\", \"y\", \"true\", \"yeah\", \"yep\", \"supported\", \"entailed\", \"correct\"}\n_NO = {\"no\", \"n\", \"false\", \"nope\", \"not\", \"unsupported\", \"incorrect\"}\n\n\ndef parse_yes_logprob(lp) -> float | None:\n    \"\"\"Graded P(yes) from the first-token top_logprobs of a yes/no entailment prompt.\"\"\"\n    if not isinstance(lp, dict):\n        return None\n    content = lp.get(\"content\")\n    if not content:\n        return None\n    tok = content[0]\n    tops = tok.get(\"top_logprobs\") or []\n    yes = no = 0.0\n    for o in tops:\n        t = (o.get(\"token\") or \"\").strip().lower()\n        try:\n            p = math.exp(o.get(\"logprob\", -50.0))\n        except Exception:\n            continue\n        if t in _YES:\n            yes += p\n        elif t in _NO:\n            no += p\n    if yes + no > 0:\n        return yes / (yes + no)\n    t0 = (tok.get(\"token\") or \"\").strip().lower()\n    if t0[:1] == \"y\":\n        return 0.85\n    if t0[:1] == \"n\":\n        return 0.15\n    return None\n\n\ndef parse_triples_jsonl(text: str) -> list[dict]:\n    \"\"\"Parse a list of {head,relation,tail,(confidence)} triples from JSONL or a JSON array.\"\"\"\n    if not text:\n        return []\n    t = strip_fences(text)\n    out = []\n    # try whole-text JSON array first\n    try:\n        arr = json.loads(t)\n        if isinstance(arr, list):\n            for o in arr:\n                if isinstance(o, dict):\n                    out.append(o)\n            if out:\n                return _clean_triples(out)\n    except Exception:\n        pass\n    for line in t.splitlines():\n        line = line.strip().rstrip(\",\")\n        if not line or not line.startswith(\"{\"):\n            continue\n        try:\n            o = json.loads(line)\n            if isinstance(o, dict):\n                out.append(o)\n        except Exception:\n            continue\n    return _clean_triples(out)\n\n\ndef _clean_triples(raw: list[dict]) -> list[dict]:\n    out = []\n    for o in raw:\n        h = o.get(\"head\") or o.get(\"subject\") or o.get(\"h\")\n        r = o.get(\"relation\") or o.get(\"rel\") or o.get(\"r\") or o.get(\"relation_phrase\")\n        ta = o.get(\"tail\") or o.get(\"object\") or o.get(\"t\")\n        if not (h and r and ta):\n            continue\n        rec = {\"head\": str(h).strip(), \"relation\": str(r).strip(), \"tail\": str(ta).strip()}\n        if \"confidence\" in o or \"conf\" in o or \"p\" in o:\n            try:\n                c = float(o.get(\"confidence\", o.get(\"conf\", o.get(\"p\"))))\n                if c > 1.0:\n                    c = c / 100.0\n                rec[\"confidence\"] = min(1.0, max(0.0, c))\n            except Exception:\n                rec[\"confidence\"] = 0.5\n        for tk in (\"head_type\", \"tail_type\"):\n            if tk in o:\n                rec[tk] = str(o[tk]).strip().upper()\n        out.append(rec)\n    return out\n\n\n# --------------------------------------------------------------------------------------\n# NORMALIZATION\n# --------------------------------------------------------------------------------------\n_PUNCT = re.compile(r\"[^\\w\\s]\")\n_WS = re.compile(r\"\\s+\")\n_STOP_PREFIX = re.compile(r\"^(the|a|an|los|las|el|la)\\s+\", re.IGNORECASE)\n\n\ndef norm(s: str) -> str:\n    if not s:\n        return \"\"\n    s = s.lower().strip()\n    s = _PUNCT.sub(\" \", s)\n    s = _STOP_PREFIX.sub(\"\", s)\n    s = _WS.sub(\" \", s).strip()\n    return s\n\n\n# --------------------------------------------------------------------------------------\n# DATA LOADING (slim projection of only required fields)\n# --------------------------------------------------------------------------------------\ndef load_docs(data_path: Path, split_role: str | None, limit: int | None) -> list[dict]:\n    \"\"\"Load Re-DocRED examples, projecting only the fields we need.\"\"\"\n    logger.info(f\"Loading data from {data_path} (split_role={split_role}, limit={limit})\")\n    blob = json.loads(data_path.read_text())\n    examples = blob[\"datasets\"][0][\"examples\"]\n    docs = []\n    for ex in examples:\n        role = ex.get(\"metadata_split_role\")\n        if split_role and role != split_role:\n            continue\n        gold = ex.get(\"metadata_gold_triples\", [])\n        ents = ex.get(\"metadata_entities\", [])\n        docs.append({\n            \"doc_id\": ex.get(\"metadata_id\"),\n            \"title\": ex.get(\"metadata_title\"),\n            \"fold\": ex.get(\"metadata_fold\"),\n            \"split_role\": role,\n            \"input\": ex.get(\"input\", \"\"),\n            \"sent_char_offsets\": ex.get(\"metadata_sent_char_offsets\", []),\n            \"entities\": [{\n                \"entity_id\": e[\"entity_id\"],\n                \"type\": e.get(\"type\", \"MISC\"),\n                \"canonical_name\": e.get(\"canonical_name\", \"\"),\n                \"aliases\": list({m.get(\"name\", \"\") for m in e.get(\"mentions\", [])}\n                                | {e.get(\"canonical_name\", \"\")}),\n            } for e in ents],\n            \"gold_triples\": [{\n                \"head_id\": g[\"head_id\"], \"tail_id\": g[\"tail_id\"],\n                \"relation_pid\": g[\"relation_pid\"], \"relation_name\": g.get(\"relation_name\", \"\"),\n                \"head_name\": g.get(\"head_name\", \"\"), \"tail_name\": g.get(\"tail_name\", \"\"),\n                \"head_type\": g.get(\"head_type\", \"MISC\"), \"tail_type\": g.get(\"tail_type\", \"MISC\"),\n            } for g in gold],\n        })\n        if limit and len(docs) >= limit:\n            break\n    del blob\n    logger.info(f\"Loaded {len(docs)} docs\")\n    return docs\n\n\ndef load_relation_schema() -> list[dict]:\n    return json.loads(RELATION_SCHEMA.read_text())\n\n\n# --------------------------------------------------------------------------------------\n# EMBEDDING MODEL + alignment primitives  (CPU, sentence-transformers MiniLM)\n# --------------------------------------------------------------------------------------\nclass Embedder:\n    def __init__(self):\n        from sentence_transformers import SentenceTransformer\n        import numpy as np\n        self.np = np\n        logger.info(f\"Loading embedding model {CONFIG['embed_model']} (CPU)\")\n        self.model = SentenceTransformer(CONFIG[\"embed_model\"], device=\"cpu\")\n        self._cache: dict[str, \"np.ndarray\"] = {}\n\n    def encode(self, texts: list[str]):\n        return self.model.encode(texts, normalize_embeddings=True, convert_to_numpy=True,\n                                 show_progress_bar=False, batch_size=64)\n\n    def encode_cached(self, texts: list[str]):\n        np = self.np\n        missing = [t for t in texts if t not in self._cache]\n        if missing:\n            embs = self.encode(missing)\n            for t, e in zip(missing, embs):\n                self._cache[t] = e\n        return np.vstack([self._cache[t] for t in texts])\n\n\ndef build_pcode_embeddings(embedder: Embedder, rel_schema: list[dict]):\n    \"\"\"Precompute (and cache to disk) the 96 P-code embeddings from name + description.\"\"\"\n    np = embedder.np\n    pcodes = [r[\"relation_pid\"] for r in rel_schema]\n    if PCODE_EMB_FILE.exists():\n        z = np.load(PCODE_EMB_FILE, allow_pickle=True)\n        if list(z[\"pcodes\"]) == pcodes:\n            logger.info(\"Loaded cached P-code embeddings\")\n            return pcodes, z[\"emb\"], {r[\"relation_pid\"]: r for r in rel_schema}\n    texts = [f\"{r['relation_name']}: {r['relation_description']}\" for r in rel_schema]\n    emb = embedder.encode(texts)\n    np.savez(PCODE_EMB_FILE, pcodes=np.array(pcodes), emb=emb)\n    logger.info(f\"Computed {len(pcodes)} P-code embeddings\")\n    return pcodes, emb, {r[\"relation_pid\"]: r for r in rel_schema}\n", "numLines": 426, "startLine": 1, "totalLines": 426}}
````

### [21] ASSISTANT · 2026-06-16 13:06:56 UTC

```
I now fully understand the structure. The expensive part (LLM extraction + embedding alignment) produces per-system **aligned predictions** that are already stored in `method_out.json` examples (`predict_METHOD/PLAIN/CoT/RAG/CONF` + gold `output`). The demo can faithfully reproduce the **downstream wedge analysis** (PR curves, matched-recall precision wedge with bootstrap CIs, knockoff+ operating points, multi-hop hallucination rate, verdict) using the verbatim pure-numpy functions from `analyze.py` — with **no API calls, no network, no embedding model**.

Let me inspect the full output file's example count and build the demo data.
```

### [22] TOOL CALL — Bash · 2026-06-16 13:06:56 UTC

```
Inspect full output example count and structure:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3 && /usr/local/bin/python3.12 -c "
import json
blob = json.load(open('full_method_out.json'))
exs = blob['datasets'][0]['examples']
print('n_examples:', len(exs))
print('systems(meta):', blob['metadata'].get('systems'))
print('n_docs_used:', blob['metadata'].get('n_docs_used'))
folds = {}
for e in exs:
    folds[e.get('metadata_fold')] = folds.get(e.get('metadata_fold'),0)+1
print('folds:', folds)
e0 = exs[0]
print('keys:', list(e0.keys()))
print('input_len:', len(e0.get('input','')))
print('output sample:', e0['output'][:120])
print('predict_METHOD sample:', e0['predict_METHOD'][:120])
import sys
# how many have nonempty predicts
for k in ['predict_METHOD','predict_PLAIN','predict_CoT','predict_RAG','predict_CONF']:
    nonempty = sum(1 for e in exs if e.get(k) and e[k] not in ('[]',''))
    print(k, 'nonempty:', nonempty)
"
```

### [23] TOOL RESULT — Bash · 2026-06-16 13:06:56 UTC

```
{"stdout": "n_examples: 36\nsystems(meta): ['METHOD', 'PLAIN', 'CoT', 'RAG', 'CONF']\nn_docs_used: 36\nfolds: {'cluster_PER': 9, 'cluster_ORG': 9, 'cluster_LOC': 9, 'cluster_MISC': 9}\nkeys: ['input', 'output', 'metadata_doc_id', 'metadata_title', 'metadata_fold', 'metadata_n_candidates', 'metadata_n_gold', 'predict_METHOD', 'predict_PLAIN', 'predict_CoT', 'predict_RAG', 'predict_CONF']\ninput_len: 633\noutput sample: [[\"P569\", 0, 1], [\"P19\", 0, 2], [\"P570\", 0, 4], [\"P20\", 0, 5], [\"P17\", 2, 3], [\"P17\", 5, 6], [\"P577\", 13, 14], [\"P937\", \npredict_METHOD sample: [[\"P569\", 0, 1, 0.9998], [\"P19\", 0, 2, 0.9981], [\"P131\", 2, 3, 0.9933], [\"P570\", 0, 4, 1.0], [\"P570\", 0, 5, 0.989], [\"P1\npredict_METHOD nonempty: 36\npredict_PLAIN nonempty: 36\npredict_CoT nonempty: 36\npredict_RAG nonempty: 36\npredict_CONF nonempty: 36", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [24] ASSISTANT · 2026-06-16 13:07:10 UTC

```
All 36 examples have nonempty predictions, balanced across 4 folds. 36 ≤ 100, so I'll include all of them — keeping `input` truncated for display. Let me build `mini_demo_data.json`.
```

### [25] TOOL CALL — Bash · 2026-06-16 13:07:10 UTC

```
Build mini_demo_data.json with 36 examples and slim metadata:
/usr/local/bin/python3.12 -c "
import json
src = json.load(open('/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/full_method_out.json'))
exs = src['datasets'][0]['examples']
M = src['metadata']

# slim metadata: keep fields relevant to the demo + the full-run headline result for comparison
slim_meta = {
    'method_name': M['method_name'],
    'description': M['description'],
    'model': M['model'],
    'elicitation': M['elicitation'],
    'systems': M['systems'],
    'rules_list': M['rules_list'],
    'config': M['config'],
    'seed': M['seed'],
    'full_run_reference': {
        'n_docs_used': M['n_docs_used'],
        'bootstrap_B': M['bootstrap_B'],
        'max_recall_per_system': M['max_recall_per_system'],
        'verdict': M['verdict'],
        'contamination_rate_decoys': M['contamination_rate_decoys'],
        'cost_usd': M['cost_usd'],
        'n_api_calls': M['n_api_calls'],
    },
}

# keep ALL 36 examples (balanced 4 folds x 9); truncate input to 500 chars for display only
out_exs = []
for e in exs:
    out_exs.append({
        'input': e.get('input','')[:500],
        'output': e['output'],
        'metadata_doc_id': e['metadata_doc_id'],
        'metadata_title': e['metadata_title'],
        'metadata_fold': e['metadata_fold'],
        'metadata_n_candidates': e['metadata_n_candidates'],
        'metadata_n_gold': e['metadata_n_gold'],
        'predict_METHOD': e['predict_METHOD'],
        'predict_PLAIN': e['predict_PLAIN'],
        'predict_CoT': e['predict_CoT'],
        'predict_RAG': e['predict_RAG'],
        'predict_CONF': e['predict_CONF'],
    })

demo = {'metadata': slim_meta, 'datasets': [{'dataset': 'Re-DocRED', 'examples': out_exs}]}
json.dump(demo, open('mini_demo_data.json','w'), indent=2)
import os
print('wrote mini_demo_data.json', round(os.path.getsize('mini_demo_data.json')/1024,1), 'KB; n_examples:', len(out_exs))
"
```

### [26] TOOL RESULT — Bash · 2026-06-16 13:07:10 UTC

```
{"stdout": "wrote mini_demo_data.json 108.2 KB; n_examples: 36", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] ASSISTANT · 2026-06-16 13:12:06 UTC

```
The structure is clear. The demo will load precomputed aligned predictions and reproduce the downstream wedge analysis using the verbatim pure-numpy functions from `analyze.py` — no API/network/model needed. Let me write a notebook generator script (cleaner than hand-building ipynb JSON), starting with minimum config values.
```

### [28] TOOL CALL — Write · 2026-06-16 13:12:06 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/build_nb.py

#!/usr/bin/env python3
"""Generate code_demo.ipynb. Cell sources are plain (non-f) triple-quoted strings so nothing
is interpolated; the two scale knobs below are substituted into the config cell."""
import json

# ---- scale knobs (substituted into the config cell) ----
BOOTSTRAP_B = 2000
RECALL_GRID_N = 25

cells = []

def md(src):
    cells.ap... [truncated, 35435 chars total]
```

### [29] TOOL RESULT — Write · 2026-06-16 13:12:06 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/build_nb.py", "content": "#!/usr/bin/env python3\n\"\"\"Generate code_demo.ipynb. Cell sources are plain (non-f) triple-quoted strings so nothing\nis interpolated; the two scale knobs below are substituted into the config cell.\"\"\"\nimport json\n\n# ---- scale knobs (substituted into the config cell) ----\nBOOTSTRAP_B = 200... [truncated, 37250 chars total]
```

### [30] ASSISTANT · 2026-06-16 13:12:20 UTC

```
I set full values directly since the analysis is pure-numpy. Let me generate the notebook, then quickly validate the core analysis logic standalone (fast) before the slower clean-env nbconvert test.
```

### [31] TOOL CALL — Bash · 2026-06-16 13:12:20 UTC

```
Generate notebook and verify cell structure:
/usr/local/bin/python3.12 build_nb.py && /usr/local/bin/python3.12 -c "import json; nb=json.load(open('code_demo.ipynb')); print('cells:', len(nb['cells'])); print('types:', [c['cell_type'][:2] for c in nb['cells']])"
```

### [32] TOOL RESULT — Bash · 2026-06-16 13:12:20 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/code_demo.ipynb with 36 cells\ncells: 36\ntypes: ['ma', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co', 'ma', 'co']", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [33] ASSISTANT · 2026-06-16 13:12:34 UTC

```
Let me validate the analysis logic quickly by running the notebook's code cells (minus install) with the system Python against the local data file.
```

### [34] TOOL CALL — Bash · 2026-06-16 13:12:34 UTC

```
Run notebook code cells standalone to validate logic and time it:
/usr/local/bin/python3.12 -c "import numpy, matplotlib; print('numpy', numpy.__version__, 'mpl', matplotlib.__version__)" && /usr/local/bin/python3.12 << 'EOF'
import json, time
nb = json.load(open('code_demo.ipynb'))
code_cells = [ ''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code' ]
# skip the install cell (index 0 of code cells)
src = '\n'.join(code_cells[1:])
import matplotlib
matplotlib.use('Agg')  # headless for the test
g = {'__name__':'__main__'}
t0=time.time()
exec(src, g)
print('\n=== TOTAL ANALYSIS RUNTIME: %.2fs ===' % (time.time()-t0))
EOF
```

### [35] TOOL RESULT — Bash · 2026-06-16 13:12:34 UTC

```
{"stdout": "numpy 2.4.6 mpl 3.11.0\nLoaded 36 Re-DocRED documents\nMethod : Decoy-gating (knockoff+ W_i) vs plain confidence threshold (Z_i)\nModel  : openai/gpt-4.1-nano | elicitation: logprob_yes_token (verbalized_[0,1] fallback)\nSystems: ['METHOD', 'PLAIN', 'CoT', 'RAG', 'CONF']\nFolds  : ['cluster_LOC', 'cluster_MISC', 'cluster_ORG', 'cluster_PER']\nMulti-hop rules:\n   - transitive_located_in_admin (P131;P131->P131)\n   - located_in_admin_then_country (P131;P17->P17)\n   - transitive_contains_admin (P150;P150->P150)\n   - transitive_part_of (P361;P361->P361)\n   - transitive_has_part (P527;P527->P527)\n   - sibling_shares_father (P3373;P22->P22)\n   - sibling_shares_mother (P3373;P25->P25)\n   - capital_of_implies_located_in (P36->P131)\n   - sibling_symmetric (P3373->P3373)\n   - spouse_symmetric (P26->P26)\ndocuments          : 36\ngold tuples         : 1052\npredicted pool sizes: METHOD=584, PLAIN=584, CoT=261, RAG=201, CONF=584\nTITLE : Mikhail Kogan | fold: cluster_PER\nINPUT : Mikhail Borisovich Kogan (; September 5, 1893 in Zhitomir, Russian Empire – November 26, 1951 in Moscow, USSR) was a well - known medical doctor, a head of the therapy department of 2nd Moscow Medical Institute. He treated well - known people as Samuel Marshak, Martiros Saryan, Dmitri Shostakovich,  ...\nGOLD  : [[\"P569\", 0, 1], [\"P19\", 0, 2], [\"P570\", 0, 4], [\"P20\", 0, 5], [\"P17\", 2, 3], [\"P17\", 5, 6], [\"P577\", 13, 14], [\"P937\", 12, 5], [\"P27\", 0, 6], [\"P131\", 7, 5], [\"P27\", 12, 6], [\"P17\", 7, 6], [\"P131\", 5 ...\n\nfirst 6 candidates  (P-code, head_id, tail_id):\n  METHOD W_i: [('P569', 0, 1, 0.9998), ('P19', 0, 2, 0.9981), ('P131', 2, 3, 0.9933), ('P570', 0, 4, 1.0), ('P570', 0, 5, 0.989), ('P131', 5, 6, 0.977)]\n  PLAIN  Z_i: [('P569', 0, 1, 0.9998), ('P19', 0, 2, 0.9981), ('P131', 2, 3, 0.9933), ('P570', 0, 4, 1.0), ('P570', 0, 5, 0.989), ('P131', 5, 6, 0.977)]\nmax recall per system: METHOD=0.086, PLAIN=0.086, CoT=0.049, RAG=0.041, CONF=0.086\nmax_common_recall = 0.041\nFairness invariant OK: METHOD and PLAIN share identical max recall\nbootstrap count matrix: (2000, 36)  (B x documents)\nrecall grid points: 25  (recall 0.0500 .. 0.0856)\nr_star   precM    precP    delta      delta_CI            p\n0.0500    0.265    0.265  +0.00137   [-0.0081,+0.0094]  0.359\n0.0515  0.25943  0.26699  +0.00137   [-0.0081,+0.0094]  0.359\n0.0530  0.25112  0.25806  +0.00113   [-0.0149,+0.0171]  0.441\n0.0544  0.25217  0.24786  +0.00013   [-0.0082,+0.0069]  0.466\n0.0559  0.24686  0.25106  -0.00417   [-0.0198,+0.0120]  0.690\n0.0574  0.24596  0.24596  +0.00007   [-0.0077,+0.0063]  0.469\n0.0589    0.248  0.24603  +0.00007   [-0.0077,+0.0063]  0.469\n0.0604  0.23970  0.24710  -0.00959   [-0.0174,-0.0002]  0.976\n0.0619  0.22916  0.22680  +0.00045   [-0.0097,+0.0126]  0.496\n0.0633  0.23183  0.22866  +0.00058   [-0.0066,+0.0069]  0.427\n0.0648  0.20720  0.20658  +0.00086   [-0.0057,+0.0064]  0.367\n0.0663  0.20833  0.20710  +0.00427   [-0.0040,+0.0129]  0.175\n0.0678  0.21114  0.20930  +0.00005   [-0.0075,+0.0077]  0.509\n0.0693  0.19891  0.20977  -0.00847   [-0.0192,+0.0014]  0.948\n0.0707  0.19788  0.19736  -0.00044   [-0.0092,+0.0114]  0.580\n0.0722      0.2  0.19638  +0.00259   [-0.0035,+0.0086]  0.197\n0.0737  0.19548  0.19548  +0.00115   [-0.0084,+0.0106]  0.409\n0.0752  0.19559  0.19417  -0.00033   [-0.0093,+0.0087]  0.535\n0.0767  0.19708  0.19612  +0.00159   [-0.0058,+0.0098]  0.368\n0.0781  0.19951  0.19575  +0.00407   [-0.0048,+0.0134]  0.186\n0.0796      0.2  0.19672  +0.00348   [-0.0055,+0.0123]  0.233\n0.0811  0.18494  0.19724  -0.01393   [-0.0257,-0.0029]  0.995\n0.0826  0.18012  0.19683  -0.01637   [-0.0288,-0.0053]  0.997\n0.0841  0.18350  0.19517  -0.01099   [-0.0199,-0.0027]  0.997\n0.0856  0.18292  0.19271  -0.00923   [-0.0166,-0.0026]  0.996\n\nconfirmed_recall_points (CI>0 & BH-significant): 0\nalpha    T         n_admit  precision  recall   k_floor_met\n0.05      0.2688     438     0.1941   0.0808   True\n0.1       0.0000     470     0.1830   0.0817   True\n0.2       0.0000     470     0.1830   0.0817   True\n0.3       0.0000     470     0.1830   0.0817   True\n0.5       0.0000     470     0.1830   0.0817   True\nrepresentative recall r_rep = 0.0752\n\nsystem   rate     n_derived  n_hallucinated   CI\nMETHOD   0.5000         24             12    [0.286, 1.000]\nPLAIN    0.4783         23             11    [0.286, 1.000]\nCoT        None          0              0    [nan, nan]\nRAG        None          0              0    [nan, nan]\nCONF     0.5000         18              9    [0.192, 1.000]\n\ndelta(METHOD-PLAIN) hallucination rate = +0.01629  CI=[+0.00000, +0.04762]\nP-code universe size: 90\n\nvariant            delta       CI\nbaseline          -0.00033   [-0.00926, +0.00869]\nnoise_5pct        +0.00378   [-0.00498, +0.01289]\nnoise_10pct       -0.01237   [-0.02347, -0.00251]\nnoise_20pct       +0.00000   [+0.00000, +0.00000]\nDEMO-SUBSET VERDICT\n  wedge_confirmed   : False\n  disconfirmed      : True\n  n_confirmed_points: 0\n  OPERATIONAL DISCONFIRMATION (pre-registered): the wedge collapses to 'thresholding-is-enough' — no recall point shows a precision advantage of decoy-gating over the plain confidence threshold with CI entirely > 0.\n\nFULL-RUN REFERENCE (36 docs, B=300):\n  wedge_confirmed   : False\n  n_confirmed_points: 0\n  decoy contamination rate: 0.12913\n  cost: $0.34744 over 8005 API calls\n  OPERATIONAL DISCONFIRMATION (pre-registered): the wedge collapses to 'thresholding-is-enough' — no recall point shows a precision advantage of decoy-gating over the plain confidence threshold with CI entirely > 0.\n\nDemo verdict: OPERATIONAL DISCONFIRMATION (0/25 recall points confirmed)\n\n=== TOTAL ANALYSIS RUNTIME: 1.19s ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [36] ASSISTANT · 2026-06-16 13:12:54 UTC

```
The analysis runs in **1.19s** with full original params (B=2000, grid=25, all 36 docs) and faithfully reproduces the full-run verdict (OPERATIONAL DISCONFIRMATION, 0 confirmed points). No scaling needed — already at full params. Now the clean-environment nbconvert test (simulating Colab). Let me run it in the background.
```

### [37] TOOL CALL — Bash · 2026-06-16 13:12:54 UTC

```
Run clean-env nbconvert test simulating Colab:
rm -rf .nb_env && /usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -3 && echo "=== ENV READY, RUNNING NBCONVERT ===" && time .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -25 && echo "=== EXIT $? ===" && rm -rf .nb_env
```

### [38] TOOL RESULT — Bash · 2026-06-16 13:12:54 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bpo46ppt2"}
```

### [39] ASSISTANT · 2026-06-16 13:13:02 UTC

```
While that runs, let me prepare the output struct JSON and verify the notebook contains the required GITHUB_DATA_URL.
```

### [40] TOOL CALL — Bash · 2026-06-16 13:13:02 UTC

```
Verify GITHUB_DATA_URL and data file presence:
echo "=== GITHUB_DATA_URL present? ===" && grep -c 'https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-3/demo/mini_demo_data.json' code_demo.ipynb && echo "=== open() local fallback present? ===" && grep -c 'mini_demo_data.json' code_demo.ipynb && echo "=== files in workspace ===" && ls -la mini_demo_data.json code_demo.ipynb
```

### [41] TOOL RESULT — Bash · 2026-06-16 13:13:02 UTC

```
{"stdout": "=== GITHUB_DATA_URL present? ===\n1\n=== open() local fallback present? ===\n5\n=== files in workspace ===\n-rw-r--r-- 1 root root  42668 Jun 16 13:12 code_demo.ipynb\n-rw-r--r-- 1 root root 110757 Jun 16 13:07 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [42] ASSISTANT · 2026-06-16 13:13:10 UTC

```
Verification passes. Let me monitor the nbconvert background test.
```

### [43] TOOL CALL — Bash · 2026-06-16 13:13:10 UTC

```
Wait and check nbconvert interim output:
sleep 60; echo "--- interim output ---"; cat "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output" 2>/dev/null
```

### [44] TOOL RESULT — Bash [ERROR] · 2026-06-16 13:13:10 UTC

```
Error: Blocked: sleep 60 followed by: echo "--- interim output ---" cat "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output". To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [45] ASSISTANT · 2026-06-16 13:13:12 UTC

```
I'll check the background output directly.
```

### [46] TOOL CALL — Read · 2026-06-16 13:13:12 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output
```

### [47] TOOL RESULT — Read · 2026-06-16 13:13:12 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output", "content": "", "numLines": 1, "startLine": 1, "totalLines": 1}}
```

### [48] ASSISTANT · 2026-06-16 13:13:24 UTC

```
The env is still being set up (output is sparse with `-q`). Let me wait for the background task to complete using a Monitor loop.
```

### [49] TOOL CALL — Bash · 2026-06-16 13:13:24 UTC

```
Wait loop placeholder check:
until [ -f code_demo.ipynb ] && .nb_env/bin/jupyter --version >/dev/null 2>&1 && ! pgrep -f "nbconvert.*code_demo" >/dev/null 2>&1; do sleep 5; done 2>/dev/null; echo "checking..."; ls -la code_demo.ipynb
```

### [50] TOOL RESULT — Bash · 2026-06-16 13:18:23 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b6dh53u5n", "assistantAutoBackgrounded": false}
```

### [51] ASSISTANT · 2026-06-16 13:18:33 UTC

```
That second loop accidentally used a name-based check — let me ignore it (it's read-only and will time out harmlessly) and just wait for the authoritative nbconvert task (`bpo46ppt2`) to notify on completion. Meanwhile, let me write the required struct output JSON.
```

### [52] TOOL CALL — Write · 2026-06-16 13:18:33 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [53] TOOL RESULT — Write · 2026-06-16 13:18:33 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [54] ASSISTANT · 2026-06-16 13:18:37 UTC

```
Now let me check the nbconvert test output.
```

### [55] TOOL CALL — Read · 2026-06-16 13:18:37 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output
```

### [56] TOOL RESULT — Read · 2026-06-16 13:18:37 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output"}}
```

### [57] ASSISTANT · 2026-06-16 13:18:51 UTC

```
Let me wait for the nbconvert task to finish by monitoring its output file for the completion marker (file-based, not process-name-based).
```

### [58] TOOL CALL — Bash · 2026-06-16 13:18:51 UTC

```
Wait for nbconvert completion marker then show output:
OUT="/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-sHNuY68d4-Wh/8511a227-71bb-4c90-a6d3-6d2e648c94ef/tasks/bpo46ppt2.output"; until grep -q "=== EXIT" "$OUT" 2>/dev/null; do sleep 5; done; echo "=== DONE ==="; cat "$OUT"
```

### [59] TOOL RESULT — Bash · 2026-06-16 13:25:43 UTC

```
{"stdout": "=== DONE ===\n\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: python3.12 -m pip install --upgrade pip\n=== ENV READY, RUNNING NBCONVERT ===\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_sHNuY68d4-Wh/.nb_env/lib/python3.12/site-packages/nbformat/__init__.py:96: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.\n  validate(nb)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 348366 bytes to code_demo.ipynb\n\nreal\t3m33.691s\nuser\t0m18.286s\nsys\t0m2.326s\n=== EXIT 0 ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [60] ASSISTANT · 2026-06-16 13:25:59 UTC

```
nbconvert succeeded (EXIT 0), executed in ~2s (the 3m33s was mostly the fresh-venv pip installs). Let me verify the executed notebook has no error outputs and check the cell-id warning.
```

### [61] TOOL CALL — Bash · 2026-06-16 13:25:59 UTC

```
Check executed notebook for errors, figures, and cell ids:
/usr/local/bin/python3.12 -c "
import json
nb = json.load(open('code_demo.ipynb'))
errs = 0; imgs = 0; nout = 0
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        nout += 1
        if o.get('output_type')=='error':
            errs += 1
            print('ERROR in cell', i, ':', o.get('ename'), o.get('evalue'))
        if o.get('output_type')=='display_data' and 'image/png' in o.get('data',{}):
            imgs += 1
print('code cells with outputs total outputs:', nout)
print('error outputs:', errs)
print('embedded PNG figures:', imgs)
print('any cell missing id:', any('id' not in c for c in nb['cells']))
"
```

### [62] TOOL RESULT — Bash · 2026-06-16 13:25:59 UTC

```
{"stdout": "code cells with outputs total outputs: 13\nerror outputs: 0\nembedded PNG figures: 1\nany cell missing id: False", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [63] ASSISTANT · 2026-06-16 13:26:23 UTC

```
The executed notebook is clean: **0 errors, 1 embedded figure, all cells have ids** (nbconvert normalized them). The notebook loads via the GitHub URL with local fallback. Let me do final verification that the rewritten notebook still contains the exact URL and check final file sizes.
```

### [64] TOOL CALL — Bash · 2026-06-16 13:26:23 UTC

```
Final verification of URL, data file, and outputs:
echo "=== exact GITHUB_DATA_URL in final notebook ===" && grep -c 'https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-3/demo/mini_demo_data.json' code_demo.ipynb && echo "=== urllib URL-first pattern present ===" && grep -c 'urllib.request.urlopen(GITHUB_DATA_URL)' code_demo.ipynb && echo "=== mini_demo_data.json valid JSON ===" && /usr/local/bin/python3.12 -c "import json; d=json.load(open('mini_demo_data.json')); print('examples:', len(d['datasets'][0]['examples']), '| has metadata:', 'metadata' in d)" && echo "=== final file sizes ===" && ls -la code_demo.ipynb mini_demo_data.json .terminal_claude_agent_struct_out.json
```

### [65] TOOL RESULT — Bash · 2026-06-16 13:26:23 UTC

```
{"stdout": "=== exact GITHUB_DATA_URL in final notebook ===\n1\n=== urllib URL-first pattern present ===\n1\n=== mini_demo_data.json valid JSON ===\nexamples: 36 | has metadata: True\n=== final file sizes ===\n-rw-r--r-- 1 root root    113 Jun 16 13:18 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root 348433 Jun 16 13:25 code_demo.ipynb\n-rw-r--r-- 1 root root 110757 Jun 16 13:07 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [66] ASSISTANT · 2026-06-16 13:26:35 UTC

```
All verifications pass. Let me confirm the disposable test env was cleaned up.
```

### [67] TOOL CALL — Bash · 2026-06-16 13:26:35 UTC

```
Confirm test env cleanup and list workspace:
ls -la .nb_env 2>/dev/null && echo ".nb_env still present" || echo ".nb_env cleaned up OK"; echo "---workspace contents---"; ls -1
```

### [68] TOOL RESULT — Bash · 2026-06-16 13:26:35 UTC

```
{"stdout": "total 5875\ndrwxr-xr-x 4 root root 2004857 Jun 16 13:25 .\ndrwxr-xr-x 3 root root 2004998 Jun 16 13:18 ..\ndrwxr-xr-x 3 root root       1 Jun 16 13:12 include\ndrwxr-xr-x 3 root root 2004857 Jun 16 13:12 lib\n.nb_env still present\n---workspace contents---\nbuild_nb.py\ncode_demo.ipynb\nmini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [69] ASSISTANT · 2026-06-16 13:26:53 UTC

```
There's a leftover partial `.nb_env` (the orphan wait-loop may be interfering). Let me stop that orphan loop and clean up.
```

### [70] TOOL CALL — ToolSearch · 2026-06-16 13:26:53 UTC

```
{'query': 'select:TaskStop,TaskList', 'max_results': 5}
```

### [71] TOOL RESULT — ToolSearch · 2026-06-16 13:26:53 UTC

```
{"matches": ["TaskStop", "TaskList"], "query": "select:TaskStop,TaskList", "total_deferred_tools": 20}
```

### [72] TOOL CALL — TaskStop · 2026-06-16 13:26:59 UTC

```
{'task_id': 'b6dh53u5n'}
```

### [73] TOOL RESULT — TaskStop · 2026-06-16 13:26:59 UTC

```
{"message": "Successfully stopped task: b6dh53u5n (until [ -f code_demo.ipynb ] && .nb_env/bin/jupyter --version >/dev/null 2>&1 && ! pgrep -f \"nbconvert.*code_demo\" >/dev/null 2>&1; do sleep 5; done 2>/dev/null; echo \"checking...\"; ls -la code_demo.ipynb)", "task_id": "b6dh53u5n", "task_type": "local_bash", "command": "until [ -f code_demo.ipynb ] && .nb_env/bin/jupyter --version >/dev/null 2>&1 && ! pgrep -f \"nbconvert.*code_demo\" >/dev/null 2>&1; do sleep 5; done 2>/dev/null; echo \"checking...\"; ls -la code_demo.ipynb"}
```

### [74] TOOL CALL — Bash · 2026-06-16 13:27:05 UTC

```
Remove leftover test env and list workspace:
rm -rf .nb_env; sync; echo "removed"; ls -1a | grep -v '^\.$\|^\.\.$'
```

### [75] TOOL RESULT — Bash · 2026-06-16 13:27:05 UTC

```
{"stdout": "removed\n.repl_agent.ptylog\n.terminal_claude_agent_struct_out.json\nbuild_nb.py\ncode_demo.ipynb\nmini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [76] ASSISTANT · 2026-06-16 13:27:22 UTC

```
The task is complete. Workspace is clean with all deliverables in place.

## Summary

I converted the Re-DocRED operational-wedge experiment (`method.py`) into a minimal-change demo notebook.

**Key insight:** the expensive pipeline stages (LLM extraction, decoy generation, MiniLM+LLM relation alignment, three-tier entity linking) had **already produced** the aligned per-system predictions, which are stored in `method_out.json` (`predict_METHOD/PLAIN/CoT/RAG/CONF` + gold `output`). So the demo loads those precomputed predictions and reproduces the **downstream analysis verbatim** — making it pure-CPU with **no API key, no network, no model download**.

**Deliverables:**
- **`mini_demo_data.json`** (110 KB) — all 36 Re-DocRED documents (balanced across the PER/ORG/LOC/MISC folds), each with gold triples + the 5 systems' aligned predictions, plus a slim `full_run_reference` block for comparison.
- **`code_demo.ipynb`** (executed, with embedded figure) — follows the required structure: title → install (numpy/matplotlib behind the Colab guard) → imports → GitHub-URL data loader with local fallback → config cell → analysis functions copied **verbatim** from `analyze.py`/`method.py` (materialize, PR curve, bootstrap CIs, knockoff+ threshold, Datalog forward-chainer) → reconstruct shared triple space → Phase F/G/G2 (PR curves, matched-recall precision wedge with BH-corrected bootstrap CIs, knockoff+ operating points, multi-hop hallucination rate) → alignment-noise sensitivity → verdict → 4-panel visualization.

**Verification:**
- Clean-env nbconvert (simulating Colab): **EXIT 0**, notebook execution ~2s, total 3m33s (mostly fresh-venv pip installs) — well under the 600s limit.
- **0 error outputs**, 1 embedded figure, all cells have IDs.
- Demo-subset result faithfully reproduces the full run: **OPERATIONAL DISCONFIRMATION, 0/25 confirmed recall points** ("thresholding-is-enough").
- Contains the exact `GITHUB_DATA_URL` and the URL-first `urllib` load pattern with local fallback.

No scaling rounds were needed — the analysis is pure-numpy and runs at the **full original parameters** (B=2000 bootstrap, 25-point recall grid, all 36 docs) in ~1.2s.

`.terminal_claude_agent_struct_out.json` written with the expected output files.
```
