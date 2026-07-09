# gen_demo_art_experiment_5 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_5` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 13:28:13 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx
```

### [2] SYSTEM-USER prompt · 2026-06-16 13:28:19 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/results/out.json`
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a
Raw data URL: https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-3/experiment-2/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-3/experiment-2/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-3/experiment-2/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-06-16 13:28:19 UTC

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

### [4] ASSISTANT · 2026-06-16 13:28:29 UTC

```
I'll start by reading the required skills and exploring the artifact's source files.
```

### [5] TOOL CALL — Skill · 2026-06-16 13:28:29 UTC

```
aii-colab
```

### [6] TOOL RESULT — Skill · 2026-06-16 13:28:29 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [7] TOOL CALL — Skill · 2026-06-16 13:28:29 UTC

```
aii-long-running-tasks
```

### [8] TOOL RESULT — Skill · 2026-06-16 13:28:29 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [9] TOOL CALL — Bash · 2026-06-16 13:28:29 UTC

```
List artifact source workspace files:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/
```

### [10] TOOL RESULT — Bash · 2026-06-16 13:28:29 UTC

```
{"stdout": "total 17583\ndrwxr-xr-x 9 root root 2033846 Jun 16 09:28 .\ndrwxr-xr-x 5 root root 3000566 Jun 16 08:46 ..\ndrwxr-xr-x 2 root root       1 Jun 16 09:29 .claude\n-rw-r--r-- 1 root root 2735726 Jun 16 09:29 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4610 Jun 16 09:28 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 6 root root 2032860 Jun 16 08:54 .venv\n-rw-r--r-- 1 root root    3918 Jun 16 09:22 README.md\ndrwxr-xr-x 2 root root 1007519 Jun 16 09:20 __pycache__\ndrwxr-xr-x 2 root root 2000212 Jun 16 09:25 cache\n-rw-r--r-- 1 root root   14729 Jun 16 08:52 fdr_stats.py\ndrwxr-xr-x 2 root root 1058290 Jun 16 09:27 figures\n-rw-r--r-- 1 root root  435519 Jun 16 09:27 full_method_out.json\n-rw-r--r-- 1 root root   11390 Jun 16 09:00 kb_engine.py\n-rw-r--r-- 1 root root   10217 Jun 16 08:52 llm_client.py\ndrwxr-xr-x 2 root root 2000336 Jun 16 09:18 logs\n-rw-r--r-- 1 root root   10040 Jun 16 09:20 make_figures.py\n-rw-r--r-- 1 root root   80044 Jun 16 09:17 method.py\n-rw-r--r-- 1 root root  435677 Jun 16 09:25 method_out.json\n-rw-r--r-- 1 root root   80466 Jun 16 09:27 mini_method_out.json\n-rw-r--r-- 1 root root   31689 Jun 16 09:27 preview_method_out.json\n-rw-r--r-- 1 root root     586 Jun 16 08:52 pyproject.toml\ndrwxr-xr-x 2 root root 1005174 Jun 16 09:25 trace_graphs\n-rw-r--r-- 1 root root    5722 Jun 16 08:57 typing_sumo.py", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] TOOL CALL — Bash · 2026-06-16 13:28:29 UTC

```
List current notebook workspace:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/
```

### [12] TOOL RESULT — Bash · 2026-06-16 13:28:29 UTC

```
{"stdout": "total 2015\ndrwxr-xr-x 2 root root 1004200 Jun 16 13:28 .\ndrwxr-xr-x 4 root root 1014539 Jun 16 13:27 ..\n-rw-r--r-- 1 root root   43200 Jun 16 13:28 .repl_agent.ptylog", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] TOOL CALL — Read · 2026-06-16 13:28:43 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/README.md
```

### [14] TOOL RESULT — Read · 2026-06-16 13:28:43 UTC

````
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/README.md", "content": "# P2 — Hallucination-reduction of a decoy-gated neuro-symbolic text→logic pipeline\n\nExecutes the goal's binding deliverable on the **24-doc legal/news/regulatory application\nanchor** (8 legal CUAD-crisp / 8 news Wikinews-silver / 8 regulatory GDPR+eCFR-silver):\na **label-free decoy-competition (knockoff+) FDR gate** that admits LLM-extracted\n`(head, relation, tail)` facts into a running logic engine, measured against **raw LLM**,\n**RAG (BM25)**, and **chain-of-thought** baselines, with **human-auditable trace-graphs**.\n\n## What runs\n\n`method.py` (one implementation; method + baselines + controls side-by-side):\n\n| Stage | What |\n|-------|------|\n| 1 | Over-generating extraction (n=3 sample union) → WordNet→SUMO typing → open→gold relation alignment (`+ \"other:\"` escape) → entity linking → crisp/silver labelling vs gold. |\n| 2 | Document-conditioned **counterfactual decoys** + type-matched **swap** control + deterministic **entrapment** (r=1) + **dual elicitation** scoring (single-token logprob softmax P(Yes) **and** K=5 self-consistency) + **knockoff+** gate at every α, per genre × elicitation, with the gate's own `decoy_fdr_hat`, realized FDR vs gold, and the entrapment `FDP_hat` bound + the second-order `self_report_anticonservative` flag. |\n| 2b | **PRIMARY METRIC**: hallucinated-fact rate (decoy-gate vs RAW LLM) per genre × elicitation × α, with a **non-circular cross-family adjudicator** (`mistralai/ministral-8b`, validated on legal crisp gold by Cohen's κ), document-block bootstrap CIs, regime tags, and silver lower/upper bounds. |\n| 2c | **SECONDARY**: matched-recall precision / hallucination-rate vs RAW / GATE / RAG / CoT. |\n| 3 | Reasoning + **auditable trace-graphs**: pure-Python backward-chaining meta-interpreter over admitted facts + hand-authored genre bridge rules; every leaf carries provenance + decoy (`W_i,T,α`) + entrapment (`FDP_hat,r`) certificates; multi-hop corrupted-conclusion rate RAW-KB vs GATE-KB across α. |\n| 4 | Benjamini–Hochberg correction, schema-valid `method_out.json`, figures. |\n\nCPU-only. Soft cap $3 (warn), hard stop $10 (`BudgetExceeded`). On-disk cache → free resumes.\n\n## Files\n- `method.py` — full pipeline (`fdr_stats.py`, `llm_client.py` reused verbatim from iter-2; `typing_sumo.py` WordNet→SUMO typing; `kb_engine.py` proof engine + DOT/JSON export).\n- `method_out.json` (+ `mini_`/`preview_`) — `exp_gen_sol_out` schema: one row per admitted/extracted real fact; metadata holds `hallucination_grid`, `s1_decoy_signature`, `matched_recall_curves`, `extraction_quality`, `multihop_corruption`, `adjudicator_validation`, `trace_graphs`, `bh_correction`.\n- `trace_graphs/` — per-doc proof JSON + Graphviz DOT (≥2 per genre).\n- `figures/` — `fig1_hallucination_grid`, `fig2_fdr_selfreport`, `fig3_matched_recall`, `fig4_tracegraph_<genre>`, `fig5_multihop_corruption`.\n\n## Reproduce\n```bash\nuv run method.py --selftest                          # offline unit tests (no API)\nuv run method.py --mini --elic logprob --k-sc 2      # 12-doc smoke\nPYTHONHASHSEED=0 uv run method.py                    # full 24 docs, both elicitations\nuv run make_figures.py\n```\n`OPENROUTER_API_KEY` must be set. Models: `openai/gpt-4.1-nano` (primary scorer/generator,\nlogprobs + prompt caching) and `mistralai/ministral-8b` (cross-family adjudicator).\n\n## Honest scope\n- Legal gold is **crisp** (CUAD); news/regulatory gold is **silver** (partial recall) — carried per row by `gold_quality` and bracketed by silver lower/upper hallucination bounds.\n- SWI-Prolog/janus-swi attempted, **fell back** to the pure-Python engine (identical JSON+DOT trace-graph schema with per-leaf certificates).\n- Relation extraction uses open over-generation + LLM alignment to the per-genre gold vocab with an `\"other:\"` escape; the regime map (where the gate helps / is null / is worse) is reported across the **full** grid, never obscured.\n", "numLines": 44, "startLine": 1, "totalLines": 44}}
````

### [15] TOOL CALL — Read · 2026-06-16 13:28:43 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/preview_method_out.json
```

### [16] TOOL RESULT — Read · 2026-06-16 13:28:43 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/preview_method_out.json", "content": "{\n  \"metadata\": {\n    \"method_name\": \"Label-free decoy-competition (knockoff+) FDR gate for LLM text->logic fact admission, with auditable trace-graphs\",\n    \"task\": \"Operational neuro-symbolic translation of short legal/news/regulatory documents into gated (head, relation, tail) facts that fee... [truncated, 34855 chars total]
```

### [17] ASSISTANT · 2026-06-16 13:29:07 UTC

```
Let me read the core code files to understand the structure.
```

### [18] TOOL CALL — Read · 2026-06-16 13:29:07 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/fdr_stats.py
```

### [19] TOOL RESULT — Read · 2026-06-16 13:29:07 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/fdr_stats.py", "content": "#!/usr/bin/env python3\n\"\"\"\nfdr_stats.py — Offline statistical primitives for the decoy-competition FDR gate.\n\nAll functions are pure (no I/O, no API) so they can be unit-tested with `--selftest`\nin method.py. Implements:\n  * canonical knockoff statistic W_i (signed-max)           [Barber-Candes]\n  * knockoff+ operative threshold T(alpha) (eq 1.9)\n  * k-floor / certifiable-alpha logic (FDR floor 1/k)\n  * tail-conditioned decoy win-rate\n  * one-sided two-sample tests (KS, Mann-Whitney, Anderson-Darling, permutation)\n  * tail effect sizes (Wasserstein, Cliff's delta, KS-sup, mean-diff)\n  * document-block (cluster) bootstrap CIs (B>=2000)\n  * Benjamini-Hochberg multiplicity correction\n  * within-document rank-normalisation\n  * empirical-CDF export for figure-ready overlays\n  * realized-FDR calibration for the decoy gate and the raw-confidence baseline\n\"\"\"\nfrom __future__ import annotations\n\nimport hashlib\nimport math\nfrom typing import Callable, Sequence\n\nimport numpy as np\nfrom scipy import stats\n\n\n# ---------------------------------------------------------------------------\n# Rank-normalisation (per document, cancels per-doc scoring-scale differences)\n# ---------------------------------------------------------------------------\ndef _jitter(cand_id: str, seed: int) -> float:\n    \"\"\"Tiny deterministic jitter in [0, 1e-6) to break exact ties before ranking.\"\"\"\n    h = hashlib.sha256(f\"{cand_id}|{seed}\".encode()).hexdigest()\n    return (int(h[:12], 16) / float(16**12)) * 1e-6\n\n\ndef rank_normalize(scores: dict[str, float], seed: int) -> dict[str, float]:\n    \"\"\"Map a pool of candidate scores to [0,1] ranks. cand_id->normalized rank.\n\n    A single-element pool maps to 0.5 (no information). Ties broken by deterministic\n    jitter keyed on the candidate id so the mapping is reproducible.\n    \"\"\"\n    ids = list(scores.keys())\n    n = len(ids)\n    if n == 0:\n        return {}\n    if n == 1:\n        return {ids[0]: 0.5}\n    jittered = np.array([scores[i] + _jitter(i, seed) for i in ids])\n    order = np.argsort(jittered, kind=\"mergesort\")\n    ranks = np.empty(n, dtype=float)\n    ranks[order] = np.arange(n, dtype=float)\n    norm = ranks / (n - 1)  # 0 .. 1\n    return {ids[i]: float(norm[i]) for i in range(n)}\n\n\n# ---------------------------------------------------------------------------\n# Canonical knockoff statistic and knockoff+ threshold\n# ---------------------------------------------------------------------------\ndef W_signed_max(z_real: float, z_decoy: float) -> float:\n    \"\"\"Signed-max statistic: magnitude = max(|real|,|decoy|) in score space,\n    sign positive iff the real beats its decoy (Barber-Candes antisymmetry).\n\n    Scores are in [0,1] (rank-normalized), so max(z_real,z_decoy) is the magnitude\n    and sign(z_real - z_decoy) is the orientation. Antisymmetric under real<->decoy\n    swap (sign flips, magnitude unchanged).\n    \"\"\"\n    mag = max(z_real, z_decoy)\n    s = z_real - z_decoy\n    sign = 0.0 if s == 0 else math.copysign(1.0, s)\n    return mag * sign\n\n\ndef knockoff_plus_threshold(W: Sequence[float], alpha: float) -> tuple[float, int, float]:\n    \"\"\"knockoff+ operative cutoff T(alpha) (Barber-Candes 2015, eq 1.9):\n\n        T = min{ t in |W| : (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha }\n\n    The '+1' in the numerator (Rajchert-Keich: generally necessary) controls *exact*\n    FDR (their Thm 2). Returns (T, n_admitted, realized_ratio). If no feasible cutoff\n    exists, returns (inf, 0, 1.0) — admit nothing.\n    \"\"\"\n    Wa = np.asarray([w for w in W], dtype=float)\n    if Wa.size == 0:\n        return math.inf, 0, 1.0\n    cands = sorted({abs(w) for w in Wa if w != 0.0})\n    best = (math.inf, 0, 1.0)\n    for t in cands:\n        if t <= 0:\n            continue\n        pos = int(np.sum(Wa >= t))\n        neg = int(np.sum(Wa <= -t))\n        ratio = (1 + neg) / max(1, pos)\n        if ratio <= alpha:\n            return float(t), pos, float(ratio)\n    return best\n\n\ndef k_floor(alpha: float) -> int:\n    \"\"\"Minimum admissions needed to certify FDR<=alpha (FDR floor 1/k => k>=ceil(1/alpha)).\"\"\"\n    return int(math.ceil(1.0 / alpha))\n\n\n# ---------------------------------------------------------------------------\n# Tail-conditioned decoy win-rate\n# ---------------------------------------------------------------------------\ndef tail_win_rate(pairs: Sequence[tuple[float, float]], threshold: float) -> tuple[float, int]:\n    \"\"\"Among pairs (z_real, z_decoy) in the admission region {max(z_real,z_decoy) >= T},\n    fraction where the decoy beats the real. Target ~0.5 under exchangeability.\n    Returns (win_rate, n_tail). NaN win_rate if the tail is empty.\n    \"\"\"\n    tail = [(zr, zd) for (zr, zd) in pairs if max(zr, zd) >= threshold]\n    if not tail:\n        return float(\"nan\"), 0\n    wins = sum(1 for (zr, zd) in tail if zd > zr)\n    return wins / len(tail), len(tail)\n\n\n# ---------------------------------------------------------------------------\n# One-sided two-sample tests + supplements\n# ---------------------------------------------------------------------------\ndef ks_two_sample(decoy: Sequence[float], real: Sequence[float], alternative: str = \"two-sided\"):\n    \"\"\"KS two-sample. alternative per scipy: 'two-sided','less','greater'.\n    Returns (stat, p). Empty input -> (nan, 1.0).\"\"\"\n    d = np.asarray(decoy, float)\n    r = np.asarray(real, float)\n    if d.size == 0 or r.size == 0:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.ks_2samp(d, r, alternative=alternative, method=\"auto\")\n        return float(res.statistic), float(res.pvalue)\n    except Exception:\n        return float(\"nan\"), 1.0\n\n\ndef mannwhitney(decoy: Sequence[float], real: Sequence[float], alternative: str = \"two-sided\"):\n    \"\"\"Mann-Whitney U (one- or two-sided). Returns (stat, p).\"\"\"\n    d = np.asarray(decoy, float)\n    r = np.asarray(real, float)\n    if d.size == 0 or r.size == 0:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.mannwhitneyu(d, r, alternative=alternative)\n        return float(res.statistic), float(res.pvalue)\n    except ValueError:\n        return float(\"nan\"), 1.0\n\n\ndef anderson_darling_2samp(a: Sequence[float], b: Sequence[float]):\n    \"\"\"Anderson-Darling k-sample (more tail-sensitive than KS). Returns (stat, p).\n    p is clipped to scipy's reported floor/cap (0.001 .. 0.25).\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size < 2 or b.size < 2:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.anderson_ksamp([a, b])\n        return float(res.statistic), float(res.significance_level)\n    except Exception:\n        return float(\"nan\"), 1.0\n\n\ndef permutation_two_sample(a: Sequence[float], b: Sequence[float], n_perm: int = 5000,\n                           seed: int = 0, alternative: str = \"two-sided\"):\n    \"\"\"Permutation test on the difference of means (robust for small tails).\n    Returns (observed_mean_diff a-b, p).\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size == 0 or b.size == 0:\n        return float(\"nan\"), 1.0\n    rng = np.random.default_rng(seed)\n    obs = a.mean() - b.mean()\n    pooled = np.concatenate([a, b])\n    na = a.size\n    diffs = np.empty(n_perm)\n    for i in range(n_perm):\n        rng.shuffle(pooled)\n        diffs[i] = pooled[:na].mean() - pooled[na:].mean()\n    if alternative == \"two-sided\":\n        p = (np.sum(np.abs(diffs) >= abs(obs)) + 1) / (n_perm + 1)\n    elif alternative == \"greater\":\n        p = (np.sum(diffs >= obs) + 1) / (n_perm + 1)\n    else:  # less\n        p = (np.sum(diffs <= obs) + 1) / (n_perm + 1)\n    return float(obs), float(p)\n\n\n# ---------------------------------------------------------------------------\n# Tail effect sizes\n# ---------------------------------------------------------------------------\ndef cliffs_delta(a: Sequence[float], b: Sequence[float]) -> float:\n    \"\"\"Cliff's delta in [-1,1]: P(a>b)-P(a<b). Sign(+) => a stochastically larger.\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size == 0 or b.size == 0:\n        return float(\"nan\")\n    # vectorised count via sorting b\n    b_sorted = np.sort(b)\n    gt = np.searchsorted(b_sorted, a, side=\"left\").sum()        # #(b < a_i)\n    lt = (b.size - np.searchsorted(b_sorted, a, side=\"right\")).sum()  # #(b > a_i)\n    return float((gt - lt) / (a.size * b.size))\n\n\ndef tail_gap(decoy: Sequence[float], spont: Sequence[float]) -> dict:\n    \"\"\"Bundle of gap metrics comparing decoy vs spontaneous-error tails.\n    Signed mean_diff/cliffs: + => decoys score HIGHER than genuine errors (harder to reject\n    => gate over-counts false discoveries => CONSERVATIVE); - => decoys score LOWER (false\n    reals beat their decoys => under-count => ANTI-CONSERVATIVE).\"\"\"\n    d = np.asarray(decoy, float)\n    s = np.asarray(spont, float)\n    ks_sup, _ = ks_two_sample(d, s, \"two-sided\")\n    w1 = float(stats.wasserstein_distance(d, s)) if d.size and s.size else float(\"nan\")\n    md = float(d.mean() - s.mean()) if d.size and s.size else float(\"nan\")\n    return {\n        \"ks_sup\": ks_sup,\n        \"wasserstein\": w1,\n        \"mean_diff\": md,\n        \"cliffs_delta\": cliffs_delta(d, s),\n        \"n_decoy\": int(d.size),\n        \"n_other\": int(s.size),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Document-block (cluster) bootstrap\n# ---------------------------------------------------------------------------\ndef doc_block_bootstrap(doc_units: list, stat_fn: Callable[[list], float],\n                        B: int = 2000, seed: int = 0, ci: float = 0.95) -> dict:\n    \"\"\"Resample whole documents with replacement B times; recompute stat_fn on the\n    pooled resample. Returns point estimate, percentile CI, and bootstrap SE.\n\n    doc_units : list of per-document objects (any payload stat_fn understands).\n    stat_fn   : maps a list of doc_units -> scalar statistic.\n    \"\"\"\n    n = len(doc_units)\n    point = stat_fn(doc_units)\n    if n == 0:\n        return {\"point\": float(\"nan\"), \"ci_low\": float(\"nan\"), \"ci_high\": float(\"nan\"),\n                \"se\": float(\"nan\"), \"B\": B, \"n_docs\": 0}\n    rng = np.random.default_rng(seed)\n    reps = np.empty(B)\n    idx_all = np.arange(n)\n    for b in range(B):\n        idx = rng.choice(idx_all, size=n, replace=True)\n        resample = [doc_units[i] for i in idx]\n        reps[b] = stat_fn(resample)\n    reps = reps[~np.isnan(reps)]\n    if reps.size == 0:\n        return {\"point\": float(point) if point == point else float(\"nan\"),\n                \"ci_low\": float(\"nan\"), \"ci_high\": float(\"nan\"),\n                \"se\": float(\"nan\"), \"B\": B, \"n_docs\": n}\n    lo = float(np.percentile(reps, 100 * (1 - ci) / 2))\n    hi = float(np.percentile(reps, 100 * (1 - (1 - ci) / 2)))\n    return {\"point\": float(point) if point == point else float(np.mean(reps)),\n            \"ci_low\": lo, \"ci_high\": hi, \"se\": float(np.std(reps, ddof=1)),\n            \"B\": int(reps.size), \"n_docs\": n}\n\n\n# ---------------------------------------------------------------------------\n# Benjamini-Hochberg\n# ---------------------------------------------------------------------------\ndef benjamini_hochberg(pvals: Sequence[float], q: float = 0.05) -> list[dict]:\n    \"\"\"BH step-up. Returns list aligned to input order with adjusted p and reject flag.\"\"\"\n    p = np.asarray(pvals, float)\n    m = p.size\n    if m == 0:\n        return []\n    order = np.argsort(p, kind=\"mergesort\")\n    ranked = p[order]\n    adj = np.empty(m)\n    prev = 1.0\n    for i in range(m - 1, -1, -1):\n        val = ranked[i] * m / (i + 1)\n        prev = min(prev, val)\n        adj[i] = min(prev, 1.0)\n    adj_orig = np.empty(m)\n    adj_orig[order] = adj\n    # reject if BH-adjusted p <= q\n    return [{\"raw_p\": float(p[i]), \"bh_adj_p\": float(adj_orig[i]),\n             \"reject\": bool(adj_orig[i] <= q)} for i in range(m)]\n\n\n# ---------------------------------------------------------------------------\n# Empirical CDF export (figure-ready)\n# ---------------------------------------------------------------------------\ndef empirical_cdf(values: Sequence[float], grid: Sequence[float]) -> list[float]:\n    \"\"\"Empirical CDF of `values` evaluated on a common `grid`.\"\"\"\n    v = np.sort(np.asarray(values, float))\n    g = np.asarray(grid, float)\n    if v.size == 0:\n        return [float(\"nan\")] * len(g)\n    cdf = np.searchsorted(v, g, side=\"right\") / v.size\n    return [float(x) for x in cdf]\n\n\n# ---------------------------------------------------------------------------\n# Realized-FDR calibration: decoy gate vs raw-confidence baseline\n# ---------------------------------------------------------------------------\ndef decoy_gate_fdr(reals: list[dict], alpha: float) -> dict:\n    \"\"\"Decoy-competition (knockoff+) gate evaluated against crisp gold.\n\n    reals: list of {'w': W_i, 'is_false': bool} for labelable reals (TRUE/FALSE).\n    Admit reals with W_i >= T(alpha). Realized FDR = #(admitted & FALSE)/#admitted.\n    \"\"\"\n    W = [r[\"w\"] for r in reals]\n    T, n_adm, ratio = knockoff_plus_threshold(W, alpha)\n    admitted = [r for r in reals if r[\"w\"] >= T]\n    n = len(admitted)\n    n_false = sum(1 for r in admitted if r[\"is_false\"])\n    realized = (n_false / n) if n else 0.0\n    floor = k_floor(alpha)\n    return {\n        \"alpha\": alpha, \"threshold\": (None if math.isinf(T) else T),\n        \"n_admitted\": n, \"n_false_admitted\": n_false,\n        \"realized_fdr\": realized, \"estimated_ratio\": ratio,\n        \"k_floor\": floor, \"certified\": n >= floor,\n    }\n\n\ndef baseline_confidence_gate_fdr(reals: list[dict], alpha: float) -> dict:\n    \"\"\"Raw-confidence (purely neural) baseline gate evaluated against crisp gold.\n\n    reals: list of {'z': raw confidence in [0,1] that the real is TRUE, 'is_false': bool}.\n    Greedily admit reals in descending confidence while the *self-estimated* FDP\n    (mean of (1-confidence) over admitted) stays <= alpha — i.e. trust the model's\n    own confidence as a calibrated probability (no labels, no decoys). Realized FDR\n    is then measured against crisp gold. This is the standard 'threshold the model's\n    confidence' approach the decoy gate is compared against.\n    \"\"\"\n    srt = sorted(reals, key=lambda r: r[\"z\"], reverse=True)\n    admitted: list[dict] = []\n    run_false_mass = 0.0\n    for r in srt:\n        new_mass = run_false_mass + (1.0 - r[\"z\"])\n        n_new = len(admitted) + 1\n        if (new_mass / n_new) <= alpha:\n            admitted.append(r)\n            run_false_mass = new_mass\n        else:\n            break\n    n = len(admitted)\n    n_false = sum(1 for r in admitted if r[\"is_false\"])\n    realized = (n_false / n) if n else 0.0\n    est = (run_false_mass / n) if n else 0.0\n    return {\n        \"alpha\": alpha, \"n_admitted\": n, \"n_false_admitted\": n_false,\n        \"realized_fdr\": realized, \"self_estimated_fdp\": est,\n    }\n", "numLines": 350, "startLine": 1, "totalLines": 350}}
```

### [20] TOOL CALL — Read · 2026-06-16 13:29:07 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/kb_engine.py
```

### [21] TOOL RESULT — Read · 2026-06-16 13:29:07 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/kb_engine.py", "content": "#!/usr/bin/env python3\n\"\"\"\nkb_engine.py — pure-Python backward-chaining meta-interpreter over admitted facts +\nhand-authored genre bridge rules, with auditable trace-graph export (JSON + Graphviz DOT).\n\nThis is the DEFAULT reasoning engine (the plan's deliverable): it satisfies the goal's\n\"running logic interpreter + human-auditable trace-graphs\" requirement without a system\nSWI-Prolog. It mirrors the classic vanilla meta-interpreter\n\n    solve(true, true).\n    solve((A,B), (PA,PB)) :- solve(A,PA), solve(B,PB).\n    solve(A, node(A, Rule, Proof)) :- (A :- Body), solve(Body, Proof).\n    solve(A, leaf(A, Cert)) :- admitted_fact(A, Cert).\n\nEach leaf resolves against the admitted-fact table and carries a certificate\n    cert = {provenance_char_span, decoy_certificate:{W_i,T,alpha}, entrapment_certificate:{FDP_hat,r}}\nso every derived conclusion is traceable to gated, provenance-bearing base facts.\n\nA Fact is a ground atom: (pred, (arg1, arg2, ...)).\nA Rule is (head_pred, head_args, body) where head_args/body atoms use string VARIABLES\n(identifiers starting with an uppercase letter) and constants (anything else).\nRules here are non-recursive and range-restricted, so SLD resolution terminates.\n\"\"\"\nfrom __future__ import annotations\n\nimport html\nimport itertools\nfrom pathlib import Path\n\n# ---------------------------------------------------------------------------\n# Term helpers — explicit logic variables (entity constants are arbitrary strings,\n# so a capitalization convention cannot distinguish vars from constants).\n# ---------------------------------------------------------------------------\nclass Var:\n    __slots__ = (\"name\",)\n\n    def __init__(self, name: str):\n        self.name = name\n\n    def __eq__(self, other):\n        return isinstance(other, Var) and other.name == self.name\n\n    def __hash__(self):\n        return hash((\"Var\", self.name))\n\n    def __repr__(self):\n        return f\"?{self.name}\"\n\n\ndef V(name: str) -> Var:\n    return Var(name)\n\n\ndef is_var(x) -> bool:\n    return isinstance(x, Var)\n\n\ndef unify(pat, val, subst: dict) -> dict | None:\n    \"\"\"Unify a (possibly variable-bearing) arg tuple `pat` with ground tuple `val`.\"\"\"\n    s = dict(subst)\n    for p, v in zip(pat, val):\n        if is_var(p):\n            if p in s:\n                if s[p] != v:\n                    return None\n            else:\n                s[p] = v\n        elif p != v:\n            return None\n    return s\n\n\ndef subst_args(args, subst: dict) -> tuple:\n    return tuple(subst.get(a, a) if is_var(a) else a for a in args)\n\n\nclass KB:\n    \"\"\"Admitted facts + bridge rules + a backward-chaining solver with proof capture.\"\"\"\n\n    def __init__(self) -> None:\n        # (pred, args_tuple) -> certificate dict\n        self.facts: dict[tuple, dict] = {}\n        self.by_pred: dict[str, list[tuple]] = {}\n        self.rules: list[dict] = []\n\n    def add_fact(self, pred: str, args: tuple, cert: dict) -> None:\n        key = (pred, tuple(args))\n        if key not in self.facts:\n            self.facts[key] = cert\n            self.by_pred.setdefault(pred, []).append(tuple(args))\n\n    def add_rule(self, name: str, head_pred: str, head_args: tuple, body: list) -> None:\n        \"\"\"body: list of (pred, args) atoms; vars are shared across head+body.\"\"\"\n        self.rules.append({\"name\": name, \"head_pred\": head_pred,\n                           \"head_args\": tuple(head_args), \"body\": list(body)})\n\n    # -- backward chaining ---------------------------------------------------\n    @staticmethod\n    def _rename(atom_args, tag: str):\n        \"\"\"Rename variables in an arg tuple with a unique tag to avoid clashes.\"\"\"\n        return tuple(Var(f\"{a.name}_{tag}\") if is_var(a) else a for a in atom_args)\n\n    def _solve_atom(self, pred: str, args: tuple, subst: dict, depth: int):\n        \"\"\"Yield (new_subst, proof_node) for goal pred(args) under subst.\n\n        Goal args are first grounded through subst; remaining unbound vars are matched\n        against facts (binding them) or expanded via rules with fresh-renamed variables.\n        \"\"\"\n        g_args = subst_args(args, subst)\n        # 1) base facts\n        for fact_args in self.by_pred.get(pred, []):\n            s2 = unify(g_args, fact_args, subst)\n            if s2 is not None:\n                cert = self.facts[(pred, fact_args)]\n                yield s2, {\"type\": \"leaf\", \"atom\": [pred, list(fact_args)], \"cert\": cert}\n        # 2) rule expansion (non-recursive bridges; depth cap is a safety net)\n        if depth <= 0:\n            return\n        for ri, rule in enumerate(self.rules):\n            if rule[\"head_pred\"] != pred:\n                continue\n            tag = f\"{depth}_{ri}\"\n            head = self._rename(rule[\"head_args\"], tag)\n            s_head = unify(head, g_args, subst)  # bind renamed head vars to the (ground) goal\n            if s_head is None:\n                continue\n            body = [(p, self._rename(a, tag)) for (p, a) in rule[\"body\"]]\n            for sb, child_proofs in self._solve_body(body, s_head, depth - 1):\n                head_ground = subst_args(head, sb)\n                if any(is_var(a) for a in head_ground):\n                    continue\n                yield sb, {\"type\": \"derived\", \"atom\": [pred, list(head_ground)],\n                           \"rule\": rule[\"name\"], \"children\": child_proofs}\n\n    def _solve_body(self, body: list, subst: dict, depth: int):\n        if not body:\n            yield subst, []\n            return\n        first, rest = body[0], body[1:]\n        for s2, proof in self._solve_atom(first[0], first[1], subst, depth):\n            for s3, proofs in self._solve_body(rest, s2, depth):\n                yield s3, [proof] + proofs\n\n    def run_rule(self, rule: dict, max_depth: int = 4):\n        \"\"\"Solve a rule's body over the KB and yield fully-ground derived proofs.\"\"\"\n        body = list(rule[\"body\"])\n        for sb, child_proofs in self._solve_body(body, {}, max_depth):\n            head_ground = subst_args(rule[\"head_args\"], sb)\n            if any(is_var(a) for a in head_ground):\n                continue\n            yield {\"type\": \"derived\", \"atom\": [rule[\"head_pred\"], list(head_ground)],\n                   \"rule\": rule[\"name\"], \"children\": child_proofs}\n\n    def derive_all(self, max_depth: int = 4) -> list[dict]:\n        \"\"\"Run every rule and collect distinct derived conclusions with one proof each.\"\"\"\n        seen, out = set(), []\n        for rule in self.rules:\n            for proof in self.run_rule(rule, max_depth):\n                key = (proof[\"atom\"][0], tuple(proof[\"atom\"][1]))\n                if key in seen:\n                    continue\n                seen.add(key)\n                out.append(proof)\n        return out\n\n\n# ---------------------------------------------------------------------------\n# Proof-graph flattening + leaf walk\n# ---------------------------------------------------------------------------\ndef iter_leaves(proof: dict):\n    if proof[\"type\"] == \"leaf\":\n        yield proof\n    else:\n        for c in proof.get(\"children\", []):\n            yield from iter_leaves(c)\n\n\ndef proof_to_graph(proof: dict) -> dict:\n    \"\"\"Flatten a proof tree into {nodes:[{id,label,kind,cert?}], edges:[{src,dst,rule}]}.\"\"\"\n    nodes, edges = [], []\n    counter = itertools.count()\n\n    def atom_str(atom):\n        pred, args = atom[0], atom[1]\n        return f\"{pred}({', '.join(map(str, args))})\"\n\n    def walk(node) -> int:\n        nid = next(counter)\n        if node[\"type\"] == \"leaf\":\n            nodes.append({\"id\": nid, \"label\": atom_str(node[\"atom\"]),\n                          \"kind\": \"leaf\", \"cert\": node.get(\"cert\")})\n        else:\n            nodes.append({\"id\": nid, \"label\": atom_str(node[\"atom\"]),\n                          \"kind\": \"derived\", \"rule\": node.get(\"rule\")})\n            for c in node.get(\"children\", []):\n                cid = walk(c)\n                edges.append({\"src\": nid, \"dst\": cid, \"rule\": node.get(\"rule\")})\n        return nid\n\n    walk(proof)\n    return {\"nodes\": nodes, \"edges\": edges}\n\n\ndef graph_to_dot(graph: dict, title: str = \"\") -> str:\n    \"\"\"Render a flattened proof graph to Graphviz DOT.\n\n    Node colour encodes gate status: derived=lightblue, admitted-entailed leaf=palegreen,\n    hallucinated leaf=lightsalmon. Leaf tooltip carries provenance + W_i + FDP_hat.\n    \"\"\"\n    lines = [\"digraph proof {\", '  rankdir=TB;', '  node [style=filled, fontname=\"Helvetica\", fontsize=10];']\n    if title:\n        lines.append(f'  labelloc=\"t\"; label=\"{html.escape(title)}\";')\n    for n in graph[\"nodes\"]:\n        label = html.escape(n[\"label\"])\n        if n[\"kind\"] == \"derived\":\n            color, extra = \"lightblue\", f'\\\\nrule: {html.escape(str(n.get(\"rule\")))}'\n            tooltip = \"derived conclusion\"\n        else:\n            cert = n.get(\"cert\") or {}\n            hv = cert.get(\"hallucination_verdict\", \"?\")\n            color = \"lightsalmon\" if hv == \"HALLUCINATED\" else \"palegreen\"\n            dc = cert.get(\"decoy_certificate\") or {}\n            ec = cert.get(\"entrapment_certificate\") or {}\n            extra = (f'\\\\nW={dc.get(\"W_i\")} T={dc.get(\"T\")} a={dc.get(\"alpha\")}'\n                     f'\\\\nFDP_hat={ec.get(\"FDP_hat\")} r={ec.get(\"r\")}')\n            tooltip = html.escape(str(cert.get(\"provenance\", \"\"))[:200] or \"leaf fact\")\n        lines.append(f'  n{n[\"id\"]} [label=\"{label}{extra}\", fillcolor=\"{color}\", '\n                     f'tooltip=\"{tooltip}\"];')\n    for e in graph[\"edges\"]:\n        lines.append(f'  n{e[\"src\"]} -> n{e[\"dst\"]} [label=\"{html.escape(str(e.get(\"rule\") or \"\"))}\", '\n                     f'fontsize=8];')\n    lines.append(\"}\")\n    return \"\\n\".join(lines)\n\n\ndef selftest() -> None:\n    kb = KB()\n    # toy 2-hop derivation: cross_references(a,b), grants_right(b,r) => relevant_right(a,r)\n    kb.add_fact(\"cross_references\", (\"Art13\", \"Art6\"),\n                {\"provenance\": \"Art.13 refers to Art.6\", \"hallucination_verdict\": \"ENTAILED\",\n                 \"decoy_certificate\": {\"W_i\": 0.9, \"T\": 0.4, \"alpha\": 0.2},\n                 \"entrapment_certificate\": {\"FDP_hat\": 0.05, \"r\": 1}})\n    kb.add_fact(\"grants_right\", (\"Art6\", \"lawful_processing\"),\n                {\"provenance\": \"Art.6 grants the right to lawful processing\",\n                 \"hallucination_verdict\": \"ENTAILED\",\n                 \"decoy_certificate\": {\"W_i\": 0.7, \"T\": 0.4, \"alpha\": 0.2},\n                 \"entrapment_certificate\": {\"FDP_hat\": 0.05, \"r\": 1}})\n    kb.add_rule(\"relevant_right\", \"relevant_right\", (V(\"A\"), V(\"R\")),\n                [(\"cross_references\", (V(\"A\"), V(\"B\"))), (\"grants_right\", (V(\"B\"), V(\"R\")))])\n    derived = kb.derive_all()\n    assert len(derived) == 1, f\"expected 1 derived, got {len(derived)}\"\n    d = derived[0]\n    assert d[\"atom\"][0] == \"relevant_right\" and d[\"atom\"][1] == [\"Art13\", \"lawful_processing\"], d[\"atom\"]\n    leaves = list(iter_leaves(d))\n    assert len(leaves) == 2 and all(\"cert\" in lf and lf[\"cert\"].get(\"decoy_certificate\")\n                                    and lf[\"cert\"].get(\"entrapment_certificate\")\n                                    and \"provenance\" in lf[\"cert\"] for lf in leaves), \\\n        \"every leaf must carry all three certificate fields\"\n    g = proof_to_graph(d)\n    dot = graph_to_dot(g, title=\"toy\")\n    assert dot.startswith(\"digraph proof {\") and \"relevant_right\" in dot\n    assert \"->\" in dot and \"fillcolor\" in dot\n    print(\"kb_engine selftest PASSED\")\n\n\nif __name__ == \"__main__\":\n    selftest()\n", "numLines": 268, "startLine": 1, "totalLines": 268}}
```

### [22] ASSISTANT · 2026-06-16 13:29:15 UTC

```
Let me set up my task list and examine method.py's structure.
```

### [23] TOOL CALL — ToolSearch · 2026-06-16 13:29:15 UTC

```
{'query': 'select:TaskCreate,NotebookEdit', 'max_results': 5}
```

### [24] TOOL RESULT — ToolSearch · 2026-06-16 13:29:15 UTC

```
{"matches": ["TaskCreate", "NotebookEdit"], "query": "select:TaskCreate,NotebookEdit", "total_deferred_tools": 20}
```

### [25] TOOL CALL — Bash · 2026-06-16 13:29:15 UTC

```
Map method.py structure:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && grep -n "^def \|^class \|^    def \|^# ---\|argparse\|add_argument\|def main\|if __name__" method.py | head -120
```

### [26] TOOL RESULT — Bash · 2026-06-16 13:29:15 UTC

```
{"stdout": "36:import argparse\n60:# ---------------------------------------------------------------------------\n62:# ---------------------------------------------------------------------------\n94:def set_mem_limit(gb: float = 8.0):\n102:def _doc_seed(doc_id: str, salt: int = 0) -> int:\n107:# ---------------------------------------------------------------------------\n109:# ---------------------------------------------------------------------------\n114:def norm(s: str) -> str:\n122:def norm_match(a: str, b: str) -> bool:\n134:# ---------------------------------------------------------------------------\n136:# ---------------------------------------------------------------------------\n137:class AnchorDoc:\n142:    def __init__(self, raw: dict):\n172:    def grounded(self, endpoint: str) -> bool:\n185:    def gold_exact(self, h: str, r: str, t: str) -> bool:\n191:    def covered_pair_rels(self, h: str, t: str) -> set:\n198:    def label(self, h: str, r: str, t: str) -> str:\n209:    def entity_type(self, name: str) -> str:\n215:def load_anchor(path: Path, genres=None, n_docs: int | None = None,\n235:# ---------------------------------------------------------------------------\n237:# ---------------------------------------------------------------------------\n238:def verbalize(h: str, r: str, t: str) -> str:\n242:# ---------------------------------------------------------------------------\n244:# ---------------------------------------------------------------------------\n245:def _extract_json(text: str | None):\n274:# ---------------------------------------------------------------------------\n276:# ---------------------------------------------------------------------------\n277:def _vocab_block(doc: AnchorDoc) -> str:\n281:def extract_messages(doc: AnchorDoc, mode: str = \"raw\", retrieved: str | None = None) -> list[dict]:\n307:def align_messages(doc: AnchorDoc, phrases: list[str]) -> list[dict]:\n320:def decoy_messages(doc: AnchorDoc, items: list[tuple]) -> list[dict]:\n336:def score_messages_logprob(doc_text: str, claim: str) -> list[dict]:\n347:def score_messages_portable(doc_text: str, claim: str) -> list[dict]:\n359:def judge_messages(doc_text: str, h: str, r: str, t: str, prov: str) -> list[dict]:\n373:# ---------------------------------------------------------------------------\n375:# ---------------------------------------------------------------------------\n376:def sentence_chunks(text: str) -> list[str]:\n381:def bm25_retrieve(doc: AnchorDoc, k: int = 6) -> str:\n427:def _vocab_relation(r_raw: str, vocab: list[str]) -> str | None:\n435:# ---------------------------------------------------------------------------\n437:# ---------------------------------------------------------------------------\n438:def verify_nonentailed(doc: AnchorDoc, h: str, r: str, t: str, avoid: set) -> bool:\n449:def deterministic_decoy_relation(doc: AnchorDoc, h: str, r: str, t: str,\n491:def gen_swaps(doc: AnchorDoc, reals: list[dict], rng: random.Random) -> list[dict]:\n512:def gen_entrapment(doc: AnchorDoc, reals: list[dict], global_pool: dict,\n560:def _perturb_number(t: str, rng: random.Random) -> str:\n572:# ---------------------------------------------------------------------------\n574:# ---------------------------------------------------------------------------\n593:# ---------------------------------------------------------------------------\n595:# ---------------------------------------------------------------------------\n616:# ---------------------------------------------------------------------------\n618:# ---------------------------------------------------------------------------\n641:def _degenerate(proof: dict) -> bool:\n650:# ---------------------------------------------------------------------------\n652:# ---------------------------------------------------------------------------\n848:def rank_normalize_elic(pipe: dict, elic: str) -> dict:\n865:def cohen_kappa(pairs: list[tuple[bool, bool]]) -> tuple[float, float]:\n877:def adjudicator_validation(pipe: dict) -> dict:\n898:def annotate_hallucination(pipe: dict, trust_judge: bool) -> None:\n902:    def ann(f, doc_id):\n931:def W_cf_of(pipe: dict, normm: dict, real: dict):\n941:def W_entrap_of(pipe: dict, normm: dict, entrap: dict):\n948:def _rate(units, key):\n955:def gate_and_hall_grid(pipe: dict, norms_by_elic: dict) -> list[dict]:\n1021:def matched_recall_curves(pipe: dict, headline_norm: dict) -> dict:\n1026:    def matched_gold_id(d: AnchorDoc, f: dict):\n1032:    def system_facts(system: str) -> list[dict]:\n1104:def extraction_quality(pipe: dict) -> dict:\n1129:# ---------------------------------------------------------------------------\n1131:# ---------------------------------------------------------------------------\n1132:def build_kb(doc: AnchorDoc, facts: list[dict], headline_norm: dict, pipe: dict,\n1152:def derive_doc(kb: kbe.KB) -> list[dict]:\n1156:def multihop_corruption(pipe: dict, headline_norm: dict, grid: list[dict],\n1206:def _admission_trace(real: dict, cert: dict) -> dict:\n1215:def export_trace_graphs(pipe: dict, headline_norm: dict, grid: list[dict],\n1224:    def write_doc(d, genre, proofs, gate_cell, kind):\n1273:def s1_signature(pipe: dict, norms_by_elic: dict) -> dict:\n1307:def collect_bh(grid: list[dict], adj: dict) -> list[dict]:\n1337:# ---------------------------------------------------------------------------\n1339:# ---------------------------------------------------------------------------\n1340:def _clean(o):\n1356:def compute_headline(grid: list[dict]) -> dict:\n1384:def build_output(pipe: dict, norms_by_elic: dict, grid: list[dict], headline: dict,\n1503:# ---------------------------------------------------------------------------\n1505:# ---------------------------------------------------------------------------\n1506:def selftest():\n1573:# ---------------------------------------------------------------------------\n1575:# ---------------------------------------------------------------------------\n1621:def main():\n1622:    ap = argparse.ArgumentParser()\n1623:    ap.add_argument(\"--selftest\", action=\"store_true\")\n1624:    ap.add_argument(\"--mini\", action=\"store_true\")\n1625:    ap.add_argument(\"--n-docs\", type=int, default=None)\n1626:    ap.add_argument(\"--per-genre\", type=int, default=None)\n1627:    ap.add_argument(\"--elic\", choices=[\"both\", \"logprob\", \"portable\"], default=\"both\")\n1628:    ap.add_argument(\"--k-sc\", type=int, default=K_SC)\n1629:    ap.add_argument(\"--n-samples\", type=int, default=N_SAMPLES_EXTRACT)\n1630:    ap.add_argument(\"--no-matched-recall\", action=\"store_true\")\n1631:    ap.add_argument(\"--concurrency\", type=int, default=28)\n1632:    ap.add_argument(\"--soft-cap\", type=float, default=SOFT_CAP_USD)\n1644:if __name__ == \"__main__\":", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] ASSISTANT · 2026-06-16 13:29:37 UTC

```
This is an LLM-API-heavy pipeline. The demo must run offline (no API key in Colab), so it will load the precomputed per-fact scores and re-run the deterministic, no-API core: the knockoff+ FDR gate (`fdr_stats.py`) and the proof engine (`kb_engine.py`). Let me read the config constants and the key analysis functions.
```

### [28] TOOL CALL — Read · 2026-06-16 13:29:37 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py
```

### [29] TOOL RESULT — Read · 2026-06-16 13:29:37 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py", "content": "import argparse\nimport asyncio\nimport gc\nimport hashlib\nimport json\nimport math\nimport random\nimport re\nimport resource\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom loguru import logger\n\nimport fdr_stats as st\nimport kb_engine as kbe\nimport typing_sumo as tsumo\nfrom kb_engine import V\nfrom llm_client import (BudgetExceeded, OpenRouterClient, parse_yes_conf,\n                        yes_prob_from_logprobs)\n\n# ---------------------------------------------------------------------------\n# Constants / guardrails\n# ---------------------------------------------------------------------------\nHERE = Path(__file__).resolve().parent\nDEP_DATA = Path(\"/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/\"\n                \"iter_2/gen_art/gen_art_dataset_1\")\nFULL_DATA = DEP_DATA / \"full_data_out.json\"\nMINI_DATA = DEP_DATA / \"mini_data_out.json\"\n\nSEED = 20240617\nALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]      # k-floors {20,10,5,4,2}\nB_BOOT = 2000\nK_SC = 5                                          # self-consistency samples (portable)\nR_ENTRAP = 1                                      # paired entrapment (one per real)\nN_SAMPLES_EXTRACT = 3                             # over-generation: union of n samples\nEXTRACT_TEMP = 0.7\nREALS_CAP = 20                                    # cap aligned reals/doc (cost bound)\nCAND_CAP = 40                                     # cap raw candidates/doc before alignment\nRECALL_GRID = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]\nKAPPA_TRUST = 0.4                                 # adjudicator-trust threshold (legal kappa)\nSOFT_CAP_USD = 3.0\nHARD_STOP_USD = 10.0\n\nPRIMARY_MODEL = \"openai/gpt-4.1-nano\"             # logprobs + cheap, doc-prefix caching\nCROSS_MODEL = \"mistralai/ministral-8b-2512\"       # cross-family judge / generator ($0.15/M)\n\nGENRES = [\"legal\", \"news\", \"regulatory\"]\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\n(HERE / \"logs\").mkdir(exist_ok=True)\nlogger.add(HERE / \"logs\" / \"run.log\", rotation=\"30 MB\", level=\"DEBUG\")\n\n\ndef set_mem_limit(gb: float = 8.0):\n    try:\n        soft = int(gb * 1024**3)\n        resource.setrlimit(resource.RLIMIT_AS, (soft, soft))\n    except (ValueError, OSError) as e:\n        logger.warning(f\"could not set RLIMIT_AS: {e}\")\n\n\ndef _doc_seed(doc_id: str, salt: int = 0) -> int:\n    h = hashlib.sha256(f\"{doc_id}|{SEED}|{salt}\".encode()).hexdigest()\n    return int(h[:12], 16)\n\n\n# ---------------------------------------------------------------------------\n# Normalisation + matching helpers\n# ---------------------------------------------------------------------------\n_WS = re.compile(r\"\\s+\")\n_EDGE = re.compile(r\"^[\\s\\\"'`.,;:()\\[\\]]+|[\\s\\\"'`.,;:()\\[\\]]+$\")\n\n\ndef norm(s: str) -> str:\n    if not isinstance(s, str):\n        s = str(s)\n    s = _EDGE.sub(\"\", s)\n    s = _WS.sub(\" \", s).strip().lower()\n    return s\n\n\ndef norm_match(a: str, b: str) -> bool:\n    \"\"\"Normalised equality OR substring containment (>=3 chars) — surface-robust.\"\"\"\n    na, nb = norm(a), norm(b)\n    if not na or not nb:\n        return False\n    if na == nb:\n        return True\n    if len(na) >= 3 and len(nb) >= 3 and (na in nb or nb in na):\n        return True\n    return False\n\n\n# ---------------------------------------------------------------------------\n# Data model\n# ---------------------------------------------------------------------------\nclass AnchorDoc:\n    __slots__ = (\"doc_id\", \"text\", \"genre\", \"gold_quality\", \"source\", \"relation_vocab\",\n                 \"char_length\", \"entities\", \"entity_names\", \"gold_facts\", \"gold_set\",\n                 \"gold_pair_rel\", \"sumo_by_entity\", \"entities_by_type\", \"ntext\")\n\n    def __init__(self, raw: dict):\n        inp = json.loads(raw[\"input\"])\n        out = json.loads(raw[\"output\"])\n        self.doc_id = inp[\"doc_id\"]", "numLines": 110, "startLine": 36, "totalLines": 1647}}
```

### [30] TOOL CALL — Read · 2026-06-16 13:29:37 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py
```

### [31] TOOL RESULT — Read · 2026-06-16 13:29:37 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py", "content": "\ndef W_entrap_of(pipe: dict, normm: dict, entrap: dict):\n    ze, zd = normm.get(entrap[\"cand_id\"]), normm.get(entrap[\"decoy\"][\"cand_id\"])\n    if ze is None or zd is None:\n        return None\n    return st.W_signed_max(ze, zd)\n\n\ndef _rate(units, key):\n    flat = [f for u in units for f in u]\n    if not flat:\n        return float(\"nan\")\n    return float(np.mean([1.0 if f[key] else 0.0 for f in flat]))\n\n\ndef gate_and_hall_grid(pipe: dict, norms_by_elic: dict) -> list[dict]:\n    \"\"\"The headline grid: one cell per (genre, elicitation, alpha).\"\"\"\n    grid = []\n    for elic, normm in norms_by_elic.items():\n        # precompute W per real and per entrapment item\n        for real in pipe[\"all_reals\"]:\n            real[\"_w\"] = W_cf_of(pipe, normm, real)\n        entraps = [e for d in pipe[\"docs\"] for e in pipe[\"entrap_by_doc\"][d.doc_id]]\n        for e in entraps:\n            e[\"_w\"] = W_entrap_of(pipe, normm, e)\n        for genre in GENRES + [\"pooled\"]:\n            sel = (lambda d: True) if genre == \"pooled\" else (lambda d, g=genre: d.genre == g)\n            reals_g = [c for c in pipe[\"all_reals\"]\n                       if sel(pipe[\"doc_by_id\"][c[\"doc_id\"]]) and c.get(\"_w\") is not None]\n            entrap_g = [e for e in entraps\n                        if sel(pipe[\"doc_by_id\"][e[\"doc_id\"]]) and e.get(\"_w\") is not None]\n            Wr = [c[\"_w\"] for c in reals_g]\n            # doc-block bootstrap units (raw = all reals; gate = admitted reals at T)\n            docs_in = sorted({c[\"doc_id\"] for c in reals_g})\n            for alpha in ALPHA_GRID:\n                T, n_pos, ratio = st.knockoff_plus_threshold(Wr, alpha)\n                admit = [] if math.isinf(T) else [c for c in reals_g if c[\"_w\"] >= T]\n                N_T = len(admit)\n                N_E = 0 if math.isinf(T) else sum(1 for e in entrap_g if e[\"_w\"] >= T)\n                realized = (sum(1 for c in admit if c[\"label\"] == \"FALSE\") / N_T) if N_T else 0.0\n                fdp = (N_E * (1 + 1.0 / R_ENTRAP) / (N_T + N_E)) if (N_T + N_E) else None\n                kf = st.k_floor(alpha)\n                # bootstrap CIs\n                raw_units = [[c for c in reals_g if c[\"doc_id\"] == did] for did in docs_in]\n                gate_units = [[c for c in admit if c[\"doc_id\"] == did] for did in docs_in]\n                raw_ci = st.doc_block_bootstrap(raw_units, lambda u: _rate(u, \"hall_adj\"),\n                                                B=B_BOOT, seed=SEED)\n                gate_ci = st.doc_block_bootstrap(gate_units, lambda u: _rate(u, \"hall_adj\"),\n                                                 B=B_BOOT, seed=SEED)\n                regime = (\"anti_conservative_expected\" if elic == \"logprob\"\n                          else (\"certified\" if N_T >= kf else \"uncertified(n<1/alpha)\"))\n                cell = {\n                    \"genre\": genre, \"elicitation\": elic, \"alpha\": alpha,\n                    \"n_reals\": len(reals_g), \"n_admitted\": N_T, \"k_floor\": kf,\n                    \"certified\": bool(N_T >= kf),\n                    \"threshold\": (None if math.isinf(T) else round(T, 6)),\n                    \"decoy_fdr_hat\": round(ratio, 6),\n                    \"realized_fdr\": round(realized, 6),\n                    \"self_report_anticonservative\": bool(ratio < realized),\n                    \"entrapment\": {\"N_T\": N_T, \"N_E\": N_E, \"r\": R_ENTRAP,\n                                   \"FDP_hat\": (round(fdp, 6) if fdp is not None else None)},\n                    \"gate_hall_rate\": (round(gate_ci[\"point\"], 6)\n                                       if not math.isnan(gate_ci[\"point\"]) else None),\n                    \"gate_hall_ci\": [gate_ci[\"ci_low\"], gate_ci[\"ci_high\"]],\n                    \"raw_hall_rate\": (round(raw_ci[\"point\"], 6)\n                                      if not math.isnan(raw_ci[\"point\"]) else None),\n                    \"raw_hall_ci\": [raw_ci[\"ci_low\"], raw_ci[\"ci_high\"]],\n                    \"silver_bounds\": {\n                        \"gate_lower\": _rate(gate_units, \"hall_strict\"),\n                        \"gate_upper\": _rate(gate_units, \"hall_loose\"),\n                        \"raw_lower\": _rate(raw_units, \"hall_strict\"),\n                        \"raw_upper\": _rate(raw_units, \"hall_loose\")},\n                    \"regime_tag\": regime,\n                    \"ci_separation_gate_below_raw\": bool(\n                        not math.isnan(gate_ci[\"ci_high\"]) and not math.isnan(raw_ci[\"ci_low\"])\n                        and gate_ci[\"ci_high\"] < raw_ci[\"ci_low\"]),\n                }\n                grid.append(cell)\n    return grid\n\n\ndef matched_recall_curves(pipe: dict, headline_norm: dict) -> dict:\n    \"\"\"Matched-recall precision / hallucination-rate for RAW / GATE / RAG / CoT.\"\"\"\n    docs = pipe[\"docs\"]\n    gold_total = sum(len(d.gold_set) for d in docs)\n\n    def matched_gold_id(d: AnchorDoc, f: dict):\n        for (gh, gr, gt) in d.gold_set:\n            if gr == f[\"r\"] and norm_match(f[\"h\"], gh) and norm_match(f[\"t\"], gt):\n                return (d.doc_id, gh, gr, gt)\n        return None\n\n    def system_facts(system: str) -> list[dict]:\n        out = []\n        for d in docs:\n            if system in (\"raw\", \"gate\"):\n                base = pipe[\"reals_by_doc\"][d.doc_id]\n            else:\n                base = pipe[\"sys_facts\"][system][d.doc_id]\n            for f in base:\n                if system == \"gate\":\n                    sc = W_cf_of(pipe, headline_norm, f)\n                    if sc is None:\n                        continue\n                else:\n                    sc = f.get(\"conf\", 0.0)\n                out.append({\"doc_id\": d.doc_id, \"score\": sc, \"hall_adj\": f[\"hall_adj\"],\n                            \"gold\": matched_gold_id(d, f)})\n        return out\n\n    curves = {}\n    for system in [\"raw\", \"gate\", \"rag\", \"cot\"]:\n        if system in (\"rag\", \"cot\") and system not in pipe[\"systems\"]:\n            continue\n        facts = system_facts(system)\n        facts.sort(key=lambda x: x[\"score\"], reverse=True)\n        pts = []\n        for target in RECALL_GRID:\n            covered, admitted, halluc = set(), 0, 0\n            thr = None\n            for f in facts:\n                admitted += 1\n                if f[\"gold\"]:\n                    covered.add(f[\"gold\"])\n                if f[\"hall_adj\"]:\n                    halluc += 1\n                rec = len(covered) / gold_total if gold_total else 0.0\n                if rec >= target:\n                    thr = f[\"score\"]\n                    break", "numLines": 130, "startLine": 940, "totalLines": 1647}}
```

### [32] ASSISTANT · 2026-06-16 13:30:39 UTC

```
This is an LLM-heavy pipeline whose deterministic, no-API core is the **knockoff+ FDR gate** (`fdr_stats.py`) and the **proof engine** (`kb_engine.py`). The demo will load the precomputed per-fact scores (W statistics + gold labels) and re-run that gate offline, exactly as `method.py`'s `gate_and_hall_grid` does. Let me set up tasks and inspect the full output programmatically.
```

### [33] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Read skills aii-colab + aii-long-running-tasks', 'description': 'Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.'}
```

### [34] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "1", "subject": "Read skills aii-colab + aii-long-running-tasks"}}
```

### [35] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Understand script structure + params', 'description': 'Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.'}
```

### [36] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "2", "subject": "Understand script structure + params"}}
```

### [37] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Create mini_demo_data.json', 'description': 'Create mini_demo_data.json: curated subset from at most ONE dataset (no more than 100 diverse examples). Do NOT read/grep full output file. Use head -c or stream first entries with Python to pick examples.'}
```

### [38] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "3", "subject": "Create mini_demo_data.json"}}
```

### [39] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Create + test code_demo.ipynb at minimum config', 'description': 'Create code_demo.ipynb via NotebookEdit following notebook_structure. Set ALL config params to ABSOLUTE MINIMUM values. Test-run using test_environment. Fix all errors until it passes.'}
```

### [40] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "4", "subject": "Create + test code_demo.ipynb at minimum config"}}
```

### [41] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Gradually scale config params', 'description': 'GRADUALLY SCALE: increase config params step by step (~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful. Do NOT spend more than 2-3 scaling rounds.'}
```

### [42] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "5", "subject": "Gradually scale config params"}}
```

### [43] TOOL CALL — TaskCreate · 2026-06-16 13:30:39 UTC

```
{'subject': 'Verify GitHub URL + data file + struct out', 'description': 'Verify: (1) code_demo.ipynb contains exact GITHUB_DATA_URL, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open(). Write .terminal_claude_agent_struct_out.json.'}
```

### [44] TOOL RESULT — TaskCreate · 2026-06-16 13:30:39 UTC

```
{"task": {"id": "6", "subject": "Verify GitHub URL + data file + struct out"}}
```

### [45] TOOL CALL — Bash · 2026-06-16 13:30:39 UTC

```
Inspect full output structure programmatically:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && python3 -c "
import json,sys
d=json.load(open('full_method_out.json'))
exs=d['datasets'][0]['examples']
print('total examples:', len(exs))
from collections import Counter
genres=Counter(); kinds=Counter()
for e in exs:
    inp=json.loads(e['input'])
    genres[inp.get('genre')]+=1
    kinds[inp.get('candidate_kind')]+=1
print('by genre:', dict(genres))
print('by kind:', dict(kinds))
# legal reals
legal=[e for e in exs if json.loads(e['input']).get('genre')=='legal']
print('legal rows:', len(legal))
print('sample legal keys:', sorted(legal[0].keys()))
# count grid cells for legal
grid=d['metadata']['hallucination_grid']
legal_cells=[c for c in grid if c['genre']=='legal']
print('legal grid cells:', len(legal_cells), 'elics:', set(c['elicitation'] for c in legal_cells), 'alphas:', sorted(set(c['alpha'] for c in legal_cells)))
print('grid total cells:', len(grid))
"
```

### [46] TOOL RESULT — Bash · 2026-06-16 13:30:39 UTC

```
{"stdout": "total examples: 210\nby genre: {'legal': 71, 'news': 32, 'regulatory': 107}\nby kind: {'real': 210}\nlegal rows: 71\nsample legal keys: ['input', 'metadata_decoy_relation', 'metadata_doc_id', 'metadata_extraction_freq', 'metadata_genre', 'metadata_gold_exact', 'metadata_gold_quality', 'metadata_hall_adj', 'metadata_hallucination_verdict', 'metadata_provenance_quote', 'metadata_sumo_type_head', 'metadata_sumo_type_tail', 'metadata_w_cf_lp', 'metadata_w_cf_pt', 'metadata_z_decoy_rank_lp', 'metadata_z_decoy_rank_pt', 'metadata_z_real_rank_lp', 'metadata_z_real_rank_pt', 'metadata_z_real_raw_lp', 'metadata_z_real_raw_pt', 'output', 'predict_admit_lp_a05', 'predict_admit_lp_a10', 'predict_admit_lp_a20', 'predict_admit_lp_a30', 'predict_admit_lp_a50', 'predict_admit_pt_a05', 'predict_admit_pt_a10', 'predict_admit_pt_a20', 'predict_admit_pt_a30', 'predict_admit_pt_a50']\nlegal grid cells: 10 elics: {'logprob', 'portable'} alphas: [0.05, 0.1, 0.2, 0.3, 0.5]\ngrid total cells: 40", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [47] ASSISTANT · 2026-06-16 13:30:57 UTC

```
71 legal reals (all `real` kind), 10 legal grid cells (2 elicitations × 5 alphas). Let me verify I can reproduce the gate's admission decisions offline from the cached W statistics — this confirms the demo faithfully re-runs the method core.
```

### [48] TOOL CALL — Bash · 2026-06-16 13:30:57 UTC

```
Verify gate reproduction matches precomputed admissions:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && python3 -c "
import json
import fdr_stats as st
d=json.load(open('full_method_out.json'))
exs=[e for e in d['datasets'][0]['examples'] if json.loads(e['input'])['genre']=='legal']
ALPHAS=[0.05,0.10,0.20,0.30,0.50]
amap={0.05:'a05',0.10:'a10',0.20:'a20',0.30:'a30',0.50:'a50'}
W=[e['metadata_w_cf_lp'] for e in exs]
print('n legal reals:', len(W))
print('W sample:', [round(w,3) for w in W[:8]])
for a in ALPHAS:
    T,npos,ratio=st.knockoff_plus_threshold(W,a)
    admit=[] if T==float('inf') else [e for e in exs if e['metadata_w_cf_lp']>=T]
    # compare to precomputed predict_admit_lp_aXX
    nyes=sum(1 for e in exs if e['predict_admit_lp_'+amap[a]]=='yes')
    Tdisp = 'inf' if T==float('inf') else round(T,5)
    print(f'alpha={a}: T={Tdisp} recomputed_admit={len(admit)} precomputed_yes={nyes} ratio={round(ratio,4)}')
"
```

### [49] TOOL RESULT — Bash · 2026-06-16 13:30:57 UTC

```
{"stdout": "n legal reals: 71\nW sample: [0.833, -1.0, 0.917, 0.792, 0.875, 0.846, 1.0, 0.769]\nalpha=0.05: T=inf recomputed_admit=0 precomputed_yes=0 ratio=1.0\nalpha=0.1: T=inf recomputed_admit=0 precomputed_yes=0 ratio=1.0\nalpha=0.2: T=0.22973 recomputed_admit=61 precomputed_yes=61 ratio=0.1803\nalpha=0.3: T=0.22973 recomputed_admit=61 precomputed_yes=61 ratio=0.1803\nalpha=0.5: T=0.22973 recomputed_admit=61 precomputed_yes=61 ratio=0.1803", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [50] ASSISTANT · 2026-06-16 13:31:15 UTC

```
The gate reproduction matches the precomputed admissions exactly for all 5 alphas. Let me confirm the realized-FDR / hallucination-rate / bootstrap-CI computation also reproduces the grid, then grab a legal trace-graph example.
```

### [51] TOOL CALL — Bash · 2026-06-16 13:31:15 UTC

```
Verify FDR/hall-rate/bootstrap reproduction and list legal trace graphs:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && python3 -c "
import json, math
import fdr_stats as st
d=json.load(open('full_method_out.json'))
exs=[e for e in d['datasets'][0]['examples'] if json.loads(e['input'])['genre']=='legal']
for e in exs:
    e['_doc']=e['metadata_doc_id']
W=[e['metadata_w_cf_lp'] for e in exs]
a=0.20
T,npos,ratio=st.knockoff_plus_threshold(W,a)
admit=[e for e in exs if e['metadata_w_cf_lp']>=T]
n_false=sum(1 for e in admit if e['output']=='FALSE')
realized=n_false/len(admit)
print('a=0.2 T=%.5f n_admit=%d realized_fdr=%.6f (grid expects 0.016393)'%(T,len(admit),realized))
# hall rate via doc-block bootstrap on hall_adj
docs=sorted({e['_doc'] for e in exs})
def rate(units,key):
    flat=[f for u in units for f in u]
    if not flat: return float('nan')
    return float(sum(1.0 if f[key] else 0.0 for f in flat)/len(flat))
raw_units=[[e for e in exs if e['_doc']==did] for did in docs]
gate_units=[[e for e in admit if e['_doc']==did] for did in docs]
raw_ci=st.doc_block_bootstrap(raw_units, lambda u: rate(u,'metadata_hall_adj'), B=2000, seed=20240617)
gate_ci=st.doc_block_bootstrap(gate_units, lambda u: rate(u,'metadata_hall_adj'), B=2000, seed=20240617)
print('raw_hall=%.6f ci=[%.4f,%.4f] (grid raw expects 0.028169)'%(raw_ci['point'],raw_ci['ci_low'],raw_ci['ci_high']))
print('gate_hall=%.6f ci=[%.4f,%.4f] (grid gate expects 0.016393)'%(gate_ci['point'],gate_ci['ci_low'],gate_ci['ci_high']))
# trace graph examples
tg=d['metadata']['trace_graphs']['examples']
legal_tg=[t for t in tg if t['genre']=='legal']
print('legal trace graphs:', [t['doc_id'] for t in legal_tg], 'kinds:', [t['kind'] for t in legal_tg])
"
```

### [52] TOOL RESULT — Bash · 2026-06-16 13:31:15 UTC

```
{"stdout": "a=0.2 T=0.22973 n_admit=61 realized_fdr=0.016393 (grid expects 0.016393)\nraw_hall=0.028169 ci=[0.0000,0.0759] (grid raw expects 0.028169)\ngate_hall=0.016393 ci=[0.0000,0.0435] (grid gate expects 0.016393)\nlegal trace graphs: ['legal_cuad_00', 'legal_cuad_04'] kinds: ['multi_hop', 'multi_hop']", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [53] ASSISTANT · 2026-06-16 13:31:37 UTC

```
Everything reproduces exactly (admissions, realized FDR, hall rates, bootstrap CIs all match the grid). Now let me read the bridge rules and KB-building code so the proof-engine cell is faithful.
```

### [54] TOOL CALL — Read · 2026-06-16 13:31:37 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py
```

### [55] TOOL RESULT — Read · 2026-06-16 13:31:37 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py", "content": "# ---------------------------------------------------------------------------\n# Scoring\n# ---------------------------------------------------------------------------\nasync def score_logprob(client: OpenRouterClient, doc_text: str, claim: str) -> float:\n    res = await client.call(PRIMARY_MODEL, score_messages_logprob(doc_text, claim),\n                            max_tokens=16, temperature=0.0, logprobs=True, top_logprobs=5)\n    z = yes_prob_from_logprobs(res[\"top_logprobs\"], res[\"content\"])\n    return float(z) if z is not None else 0.5\n\n\nasync def score_portable(client: OpenRouterClient, doc_text: str, claim: str, k: int) -> float:\n    ps = []\n    for i in range(k):\n        res = await client.call(PRIMARY_MODEL, score_messages_portable(doc_text, claim),\n                                max_tokens=24, temperature=0.7, seed=SEED + i, sample_idx=i)\n        p = parse_yes_conf(res[\"content\"])\n        if p is not None:\n            ps.append(p)\n    return float(np.mean(ps)) if ps else 0.5\n\n\n# ---------------------------------------------------------------------------\n# Orchestration helper\n# ---------------------------------------------------------------------------\nasync def run_batched(coros: list, batch: int, label: str, client: OpenRouterClient):\n    out = []\n    for i in range(0, len(coros), batch):\n        chunk = coros[i:i + batch]\n        res = await asyncio.gather(*chunk, return_exceptions=True)\n        for r in res:\n            if isinstance(r, BudgetExceeded):\n                raise r\n            out.append(None if isinstance(r, Exception) else r)\n        n_err = sum(1 for r in res if isinstance(r, Exception))\n        if n_err:\n            for r in res:\n                if isinstance(r, Exception) and not isinstance(r, BudgetExceeded):\n                    logger.debug(f\"  [{label}] task error: {type(r).__name__}: {r}\")\n        logger.info(f\"  [{label}] {min(i+batch, len(coros))}/{len(coros)} | \"\n                    f\"cost=${client.cost_usd:.4f} | live={client.n_calls_live} \"\n                    f\"cached={client.n_calls_cached} | errs={n_err}\")\n    return out\n\n\n# ---------------------------------------------------------------------------\n# Genre bridge rules (hand-authored, in-genre common-sense gap-filling = multi-hop)\n# ---------------------------------------------------------------------------\nBRIDGE_RULES = {\n    \"legal\": [\n        (\"party_bound_effective\", \"party_bound_effective\", (V(\"A\"), V(\"P\"), V(\"D\")),\n         [(\"has_party\", (V(\"A\"), V(\"P\"))), (\"effective_date\", (V(\"A\"), V(\"D\")))]),\n        (\"titled_dated\", \"titled_dated\", (V(\"A\"), V(\"T\"), V(\"D\")),\n         [(\"has_title\", (V(\"A\"), V(\"T\"))), (\"agreement_date\", (V(\"A\"), V(\"D\")))]),\n    ],\n    \"news\": [\n        (\"co_occurring\", \"co_occurring\", (V(\"X\"), V(\"Y\"), V(\"D\")),\n         [(\"occurred_on\", (V(\"X\"), V(\"D\"))), (\"occurred_on\", (V(\"Y\"), V(\"D\")))]),\n    ],\n    \"regulatory\": [\n        (\"relevant_right\", \"relevant_right\", (V(\"A\"), V(\"R\")),\n         [(\"cross_references\", (V(\"A\"), V(\"B\"))), (\"grants_right\", (V(\"B\"), V(\"R\")))]),\n        (\"obligation_with_exception\", \"obligation_with_exception\", (V(\"A\"), V(\"O\"), V(\"E\")),\n         [(\"obligates\", (V(\"A\"), V(\"O\"))), (\"has_exception\", (V(\"A\"), V(\"E\")))]),\n        (\"titled_obligation\", \"titled_obligation\", (V(\"A\"), V(\"T\"), V(\"O\")),\n         [(\"has_title\", (V(\"A\"), V(\"T\"))), (\"obligates\", (V(\"A\"), V(\"O\")))]),\n    ],\n}\n\n\ndef _degenerate(proof: dict) -> bool:\n    \"\"\"Drop trivial self-derivations (e.g. co_occurring(X,X,D)).\"\"\"\n    name = proof.get(\"rule\")\n    args = proof[\"atom\"][1]\n    if name == \"co_occurring\" and len(args) >= 2 and norm_match(args[0], args[1]):\n        return True\n    return False\n\n\n# ---------------------------------------------------------------------------\n# MAIN PIPELINE\n# ---------------------------------------------------------------------------\nasync def run(docs: list[AnchorDoc], cache_dir: Path, cost_log: Path, *, elic: str,\n              k_sc: int, n_samples: int, concurrency: int, do_matched_recall: bool,\n              soft_cap: float) -> dict:\n    t0 = time.time()\n    elics = ([\"logprob\", \"portable\"] if elic == \"both\" else [elic])\n    async with OpenRouterClient(cache_dir, cost_log, concurrency=concurrency,\n                                soft_cap_usd=soft_cap, hard_stop_usd=HARD_STOP_USD) as client:\n        doc_by_id = {d.doc_id: d for d in docs}\n", "numLines": 90, "startLine": 572, "totalLines": 1647}}
```

### [56] TOOL CALL — Read · 2026-06-16 13:31:37 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py
```

### [57] TOOL RESULT — Read · 2026-06-16 13:31:37 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/method.py", "content": "# ---------------------------------------------------------------------------\n# STAGE 3 — KB / trace-graphs / multi-hop corruption\n# ---------------------------------------------------------------------------\ndef build_kb(doc: AnchorDoc, facts: list[dict], headline_norm: dict, pipe: dict,\n             gate_cell: dict | None) -> kbe.KB:\n    kb = kbe.KB()\n    for f in facts:\n        w = W_cf_of(pipe, headline_norm, f) if \"cand_id\" in f else None\n        cert = {\"provenance\": f.get(\"prov\", \"\"),\n                \"provenance_char_span\": None,\n                \"hallucination_verdict\": \"HALLUCINATED\" if f.get(\"hall_adj\") else \"ENTAILED\",\n                \"decoy_certificate\": {\"W_i\": (round(w, 4) if w is not None else None),\n                                      \"T\": (gate_cell or {}).get(\"threshold\"),\n                                      \"alpha\": (gate_cell or {}).get(\"alpha\")},\n                \"entrapment_certificate\": {\n                    \"FDP_hat\": ((gate_cell or {}).get(\"entrapment\") or {}).get(\"FDP_hat\"),\n                    \"r\": R_ENTRAP}}\n        kb.add_fact(f[\"r\"], (f[\"h\"], f[\"t\"]), cert)\n    for spec in BRIDGE_RULES.get(doc.genre, []):\n        kb.add_rule(*spec)\n    return kb\n\n\ndef derive_doc(kb: kbe.KB) -> list[dict]:\n    return [p for p in kb.derive_all(max_depth=4) if not _degenerate(p)]\n\n\ndef multihop_corruption(pipe: dict, headline_norm: dict, grid: list[dict],\n                        headline_elic: str) -> dict:\n    \"\"\"Corrupted-conclusion rate (any supporting leaf HALLUCINATED) RAW-KB vs GATE-KB.\"\"\"\n    out = {\"by_genre\": {}, \"pooled\": {}}\n    cell_by = {(c[\"genre\"], c[\"alpha\"]): c for c in grid if c[\"elicitation\"] == headline_elic}\n    pooled = {\"raw\": {\"derived\": 0, \"corrupt\": 0}}\n    for a in ALPHA_GRID:\n        pooled[f\"gate_a{a}\"] = {\"derived\": 0, \"corrupt\": 0}\n    for genre in GENRES:\n        docs = [d for d in pipe[\"docs\"] if d.genre == genre]\n        g = {\"raw\": {\"derived\": 0, \"corrupt\": 0}}\n        for a in ALPHA_GRID:\n            g[f\"gate_a{a}\"] = {\"derived\": 0, \"corrupt\": 0}\n        for d in docs:\n            reals = pipe[\"reals_by_doc\"][d.doc_id]\n            # RAW-KB: all reals\n            kb = build_kb(d, reals, headline_norm, pipe, None)\n            for p in derive_doc(kb):\n                corrupt = any((lf[\"cert\"] or {}).get(\"hallucination_verdict\") == \"HALLUCINATED\"\n                              for lf in kbe.iter_leaves(p))\n                g[\"raw\"][\"derived\"] += 1\n                g[\"raw\"][\"corrupt\"] += int(corrupt)\n                pooled[\"raw\"][\"derived\"] += 1\n                pooled[\"raw\"][\"corrupt\"] += int(corrupt)\n            # GATE-KB per alpha\n            for a in ALPHA_GRID:\n                cell = cell_by.get((genre, a))\n                T = cell[\"threshold\"] if cell else None\n                if T is None:\n                    continue\n                admit = [r for r in reals if (r.get(\"_w\") is not None and r[\"_w\"] >= T)]\n                kb2 = build_kb(d, admit, headline_norm, pipe, cell)\n                for p in derive_doc(kb2):\n                    corrupt = any((lf[\"cert\"] or {}).get(\"hallucination_verdict\") == \"HALLUCINATED\"\n                                  for lf in kbe.iter_leaves(p))\n                    g[f\"gate_a{a}\"][\"derived\"] += 1\n                    g[f\"gate_a{a}\"][\"corrupt\"] += int(corrupt)\n                    pooled[f\"gate_a{a}\"][\"derived\"] += 1\n                    pooled[f\"gate_a{a}\"][\"corrupt\"] += int(corrupt)\n\n        def rate(x):\n            return (x[\"corrupt\"] / x[\"derived\"]) if x[\"derived\"] else None\n        out[\"by_genre\"][genre] = {k: {\"derived\": v[\"derived\"], \"corrupt\": v[\"corrupt\"],\n                                      \"corrupted_rate\": rate(v)} for k, v in g.items()}\n    out[\"pooled\"] = {k: {\"derived\": v[\"derived\"], \"corrupt\": v[\"corrupt\"],\n                         \"corrupted_rate\": (v[\"corrupt\"] / v[\"derived\"]) if v[\"derived\"] else None}\n                     for k, v in pooled.items()}\n    return out\n\n\ndef _admission_trace(real: dict, cert: dict) -> dict:\n    \"\"\"Depth-1 trace for the admission boundary: admitted_fact(...) <- leaf with certificate.\n    Used to guarantee per-genre auditable artifacts when no multi-hop bridge fires.\"\"\"\n    concl = f\"{real['r']}({real['h']},{real['t']})\"\n    return {\"type\": \"derived\", \"atom\": [\"admitted_fact\", [concl]], \"rule\": \"admission\",\n            \"children\": [{\"type\": \"leaf\", \"atom\": [real[\"r\"], [real[\"h\"], real[\"t\"]]],\n                          \"cert\": cert}]}\n\n\ndef export_trace_graphs(pipe: dict, headline_norm: dict, grid: list[dict],\n                        headline_elic: str, out_dir: Path) -> dict:\n    \"\"\"Export >=2 docs/genre as JSON + DOT trace-graphs with certificate leaves.\n    Real multi-hop proofs are exported first; genres without (enough) firing bridges are\n    topped up with depth-1 admission traces so every genre has auditable artifacts.\"\"\"\n    out_dir.mkdir(exist_ok=True)\n    cell_by = {(c[\"genre\"], c[\"alpha\"]): c for c in grid if c[\"elicitation\"] == headline_elic}\n    serialized, dot_paths = [], []\n\n    def write_doc(d, genre, proofs, gate_cell, kind):\n        graphs = [kbe.proof_to_graph(p) for p in proofs[:6]]\n        jpath = out_dir / f\"trace_{d.doc_id}.json\"\n        jpath.write_text(json.dumps({\"doc_id\": d.doc_id, \"genre\": genre, \"kind\": kind,\n                                     \"n_proofs\": len(proofs), \"graphs\": graphs,\n                                     \"proofs\": proofs[:6]}, indent=2))\n        dot = kbe.graph_to_dot(graphs[0], title=f\"{d.doc_id} [{genre}] {proofs[0]['rule']}\")\n        dpath = out_dir / f\"trace_{d.doc_id}.dot\"\n        dpath.write_text(dot)\n        dot_paths.append(str(dpath.relative_to(HERE)))\n        serialized.append({\"doc_id\": d.doc_id, \"genre\": genre, \"kind\": kind,\n                           \"rule\": proofs[0][\"rule\"], \"conclusion\": proofs[0][\"atom\"],\n                           \"graph\": graphs[0], \"json_path\": str(jpath.relative_to(HERE)),\n                           \"dot_path\": str(dpath.relative_to(HERE))})\n\n    for genre in GENRES:\n        docs = [d for d in pipe[\"docs\"] if d.genre == genre]\n        cells = [cell_by.get((genre, a)) for a in ALPHA_GRID]\n        gate_cell = next((c for c in reversed(cells) if c and c[\"certified\"]),\n                         cells[-1] if cells else None)\n        done = set()\n        # 1) real multi-hop proofs\n        for d in docs:\n            if len([s for s in serialized if s[\"genre\"] == genre]) >= 2:\n                break\n            kb = build_kb(d, pipe[\"reals_by_doc\"][d.doc_id], headline_norm, pipe, gate_cell)\n            proofs = derive_doc(kb)\n            if proofs:\n                write_doc(d, genre, proofs, gate_cell, \"multi_hop\")\n                done.add(d.doc_id)\n        # 2) top up with admission traces so each genre has >=2 artifacts\n        for d in docs:\n            if len([s for s in serialized if s[\"genre\"] == genre]) >= 2:\n                break\n            if d.doc_id in done:\n                continue\n            reals = sorted(pipe[\"reals_by_doc\"][d.doc_id],\n                           key=lambda r: (r.get(\"_w\") if r.get(\"_w\") is not None else -9))\n            reals = [r for r in reals if r.get(\"_w\") is not None] or pipe[\"reals_by_doc\"][d.doc_id]\n            if not reals:\n                continue\n            kb = build_kb(d, [reals[-1]], headline_norm, pipe, gate_cell)\n            cert = list(kb.facts.values())[0] if kb.facts else {\"provenance\": reals[-1].get(\"prov\", \"\")}\n            write_doc(d, genre, [_admission_trace(reals[-1], cert)], gate_cell, \"admission\")\n    return {\"n_exported\": len(serialized), \"examples\": serialized, \"dot_paths\": dot_paths,\n            \"note\": \"multi_hop = real bridge derivation; admission = depth-1 admission-boundary \"\n                    \"trace with full per-leaf certificate (used where no bridge fires).\"}\n\n\ndef s1_signature(pipe: dict, norms_by_elic: dict) -> dict:\n    \"\"\"Counterfactual vs random-swap tail decoy win-rate (the S1 diagnostic-sensitivity\n    control). Win-rate ~0.5 => exchangeable; <0.5 => anti-conservative. Swaps are scored\n    under logprob only (the documented anti-conservative negative control).\"\"\"\n    out = {}\n    for elic, normm in norms_by_elic.items():\n        fam_out = {}\n        for fam, lookup in ((\"counterfactual\", pipe[\"cf_real\"]),\n                            (\"random_swap\", pipe[\"swap_real\"])):\n            pairs = []\n            for c in pipe[\"all_reals\"]:\n                dec = lookup.get(c[\"cand_id\"])\n                if not dec:\n                    continue\n                zr, zd = normm.get(c[\"cand_id\"]), normm.get(dec[\"cand_id\"])\n                if zr is None or zd is None:", "numLines": 160, "startLine": 1129, "totalLines": 1647}}
```

### [58] ASSISTANT · 2026-06-16 13:32:11 UTC

```
I now have the full picture. The legal bridge rule `party_bound_effective` matches the trace example. Let me verify the portable elicitation also reproduces, then build `mini_demo_data.json`.
```

### [59] TOOL CALL — Bash · 2026-06-16 13:32:11 UTC

```
Verify portable + logprob gate reproduction matches precomputed:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && python3 -c "
import json, math
import fdr_stats as st
d=json.load(open('full_method_out.json'))
exs=[e for e in d['datasets'][0]['examples'] if json.loads(e['input'])['genre']=='legal']
amap={0.05:'a05',0.10:'a10',0.20:'a20',0.30:'a30',0.50:'a50'}
for elic,wk,pk in [('logprob','metadata_w_cf_lp','predict_admit_lp_'),('portable','metadata_w_cf_pt','predict_admit_pt_')]:
    W=[e[wk] for e in exs]
    ok=True
    for a in [0.05,0.10,0.20,0.30,0.50]:
        T,npos,ratio=st.knockoff_plus_threshold(W,a)
        admit=set(id(e) for e in exs if e[wk]>=T) if T!=float('inf') else set()
        for e in exs:
            pred = (e[pk+amap[a]]=='yes')
            rec = (id(e) in admit)
            if pred!=rec: ok=False
    print(elic,'reproduction matches precomputed predict_admit:',ok)
"
```

### [60] TOOL RESULT — Bash · 2026-06-16 13:32:11 UTC

```
{"stdout": "logprob reproduction matches precomputed predict_admit: True\nportable reproduction matches precomputed predict_admit: True", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [61] ASSISTANT · 2026-06-16 13:32:17 UTC

```
Both elicitations reproduce exactly. Now let me build `mini_demo_data.json`.
```

### [62] TOOL CALL — ToolSearch · 2026-06-16 13:32:17 UTC

```
{'query': 'select:TaskUpdate', 'max_results': 3}
```

### [63] TOOL RESULT — ToolSearch · 2026-06-16 13:32:17 UTC

```
{"matches": ["TaskUpdate"], "query": "select:TaskUpdate", "total_deferred_tools": 20}
```

### [64] TOOL CALL — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{'taskId': '1', 'status': 'completed'}
```

### [65] TOOL RESULT — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{"success": true, "taskId": "1", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "completed"}}
```

### [66] TOOL CALL — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{'taskId': '2', 'status': 'completed'}
```

### [67] TOOL RESULT — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{"success": true, "taskId": "2", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "completed"}}
```

### [68] TOOL CALL — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{'taskId': '3', 'status': 'in_progress'}
```

### [69] TOOL RESULT — TaskUpdate · 2026-06-16 13:32:21 UTC

```
{"success": true, "taskId": "3", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "in_progress"}}
```

### [70] TOOL CALL — Bash · 2026-06-16 13:32:43 UTC

```
Build mini_demo_data.json (legal slice):
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/ && python3 -c "
import json
WS='/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx'
d=json.load(open('full_method_out.json'))
md=d['metadata']
exs=[e for e in d['datasets'][0]['examples'] if json.loads(e['input'])['genre']=='legal']

# legal grid cells (10: 2 elic x 5 alpha)
legal_grid=[c for c in md['hallucination_grid'] if c['genre']=='legal']
# legal trace-graph example (multi_hop, carries leaf certs)
legal_tg=[t for t in md['trace_graphs']['examples'] if t['genre']=='legal']
# slim multihop corruption: keep legal + pooled
mh=md['multihop_corruption']
mh_slim={'by_genre':{'legal':mh['by_genre']['legal']}, 'pooled':mh['pooled']}

mini={
  'metadata':{
    'method_name': md['method_name'],
    'task': md['task'],
    'primary_metric': md['primary_metric'],
    'headline_finding': md['headline_finding'],
    'models': md['models'],
    'elicitation': md['elicitation'],
    'hyperparameters': md['hyperparameters'],
    'demo_subset': {
      'genre': 'legal',
      'gold_quality': 'crisp (CUAD)',
      'n_reals': len(exs),
      'note': 'This mini file is the LEGAL slice of the 24-doc anchor. Each example row '
              'carries the precomputed per-fact decoy-competition statistics (W_i for both '
              'elicitations, gold label, hallucination flag). The demo RE-RUNS the knockoff+ '
              'FDR gate (fdr_stats.knockoff_plus_threshold) on these cached W_i values, exactly '
              'as method.py gate_and_hall_grid does, reproducing the published legal grid cells '
              'WITHOUT any LLM API calls.'
    },
    'dataset_counts_full': md['dataset_counts'],
    'hallucination_grid_legal': legal_grid,
    'trace_graph_legal_example': (legal_tg[0] if legal_tg else None),
    'multihop_corruption_slim': mh_slim,
  },
  'datasets':[{
    'dataset': 'ApplicationAnchor-24doc-Legal (crisp-gold slice)',
    'examples': exs,
  }]
}
out=WS+'/mini_demo_data.json'
json.dump(mini, open(out,'w'), indent=2)
import os
print('wrote', out, round(os.path.getsize(out)/1024,1),'KB')
print('n legal examples:', len(exs))
print('legal grid cells:', len(legal_grid))
print('trace example doc:', legal_tg[0]['doc_id'] if legal_tg else None, '| n leaf nodes:', sum(1 for n in legal_tg[0]['graph']['nodes'] if n['kind']=='leaf') if legal_tg else 0)
"
```

### [71] TOOL RESULT — Bash · 2026-06-16 13:32:43 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/mini_demo_data.json 133.5 KB\nn legal examples: 71\nlegal grid cells: 10\ntrace example doc: legal_cuad_00 | n leaf nodes: 2", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [72] ASSISTANT · 2026-06-16 13:35:31 UTC

```
`mini_demo_data.json` written (133.5 KB, 71 legal examples — the full legal slice needed for exact gate reproduction). Now let me build the notebook via a builder script.
```

### [73] TOOL CALL — Write · 2026-06-16 13:35:31 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py

#!/usr/bin/env python3
"""Builder: assemble code_demo.ipynb (nbformat v4) from cell sources."""
import json, sys

cells = []

def md(src):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": src.splitlines(keepends=True)})

def code(src):
    cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
            ... [truncated, 31275 chars total]
```

### [74] TOOL RESULT — Write · 2026-06-16 13:35:31 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py", "content": "#!/usr/bin/env python3\n\"\"\"Builder: assemble code_demo.ipynb (nbformat v4) from cell sources.\"\"\"\nimport json, sys\n\ncells = []\n\ndef md(src):\n    cells.append({\"cell_type\": \"markdown\", \"metadata\": {}, \"source\": src.splitlines(keepends=True)})\n\ndef code(src):\n    cells.append({\"c... [truncated, 33035 chars total]
```

### [75] TOOL CALL — Bash · 2026-06-16 13:35:35 UTC

```
Build notebook and verify cell structure:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 build_nb.py && python3 -c "import json; nb=json.load(open('code_demo.ipynb')); print('cells:', len(nb['cells']), '| types:', [c['cell_type'][0] for c in nb['cells']])"
```

### [76] TOOL RESULT — Bash · 2026-06-16 13:35:35 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/code_demo.ipynb with 21 cells\ncells: 21 | types: ['m', 'c', 'c', 'c', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c', 'm', 'c']", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [77] ASSISTANT · 2026-06-16 13:35:47 UTC

```
Notebook built (21 cells). Let me do a fast logic check with the system Python before the full clean-env test.
```

### [78] TOOL CALL — Bash · 2026-06-16 13:35:47 UTC

```
Check scientific packages available in system python:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "import numpy, scipy, matplotlib; print('numpy', numpy.__version__, 'scipy', scipy.__version__, 'matplotlib', matplotlib.__version__)" 2>&1 | head -5
```

### [79] TOOL RESULT — Bash · 2026-06-16 13:35:47 UTC

```
{"stdout": "numpy 2.4.6 scipy 1.17.1 matplotlib 3.11.0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [80] ASSISTANT · 2026-06-16 13:35:59 UTC

```
Let me run the notebook's logic cells (skipping the install cell) in the system Python to catch logic bugs fast before the full clean-env test.
```

### [81] TOOL CALL — Bash · 2026-06-16 13:35:59 UTC

```
Run notebook logic cells in system python:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json, matplotlib
matplotlib.use('Agg')
nb=json.load(open('code_demo.ipynb'))
ns={}
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i==1:  # skip install cell (index 1)
        continue
    src=''.join(c['source'])
    try:
        exec(src, ns)
    except Exception as e:
        import traceback
        print(f'=== CELL {i} FAILED ===')
        traceback.print_exc()
        break
else:
    print('=== ALL CODE CELLS RAN OK ===')
" 2>&1 | tail -60
```

### [82] TOOL RESULT — Bash · 2026-06-16 13:35:59 UTC

```
{"stdout": "  logprob  a=0.10  T=    None  admit=  0  decoy_fdr_hat=1.000  realized_fdr=0.000  certified=False\n  logprob  a=0.20  T= 0.22973  admit= 61  decoy_fdr_hat=0.180  realized_fdr=0.016  certified=True\n  logprob  a=0.30  T= 0.22973  admit= 61  decoy_fdr_hat=0.180  realized_fdr=0.016  certified=True\n  logprob  a=0.50  T= 0.22973  admit= 61  decoy_fdr_hat=0.180  realized_fdr=0.016  certified=True\n  portable a=0.05  T=    None  admit=  0  decoy_fdr_hat=1.000  realized_fdr=0.000  certified=False\n  portable a=0.10  T=    None  admit=  0  decoy_fdr_hat=1.000  realized_fdr=0.000  certified=False\n  portable a=0.20  T=    None  admit=  0  decoy_fdr_hat=1.000  realized_fdr=0.000  certified=False\n  portable a=0.30  T=    None  admit=  0  decoy_fdr_hat=1.000  realized_fdr=0.000  certified=False\n  portable a=0.50  T=0.129032  admit= 50  decoy_fdr_hat=0.440  realized_fdr=0.020  certified=True\nCheck 1 — per-fact admission mismatches vs published flags: 0  (PASS)\n\\nCheck 2 — recomputed grid vs published grid:\n  elic        a |       admit |          decoy_fdr_hat |            gate_hall\n  logprob  0.05 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  logprob  0.10 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  logprob  0.20 |   61 vs 61   OK |    0.1803 vs 0.1803    OK | 0.016393 vs 0.016393 OK\n  logprob  0.30 |   61 vs 61   OK |    0.1803 vs 0.1803    OK | 0.016393 vs 0.016393 OK\n  logprob  0.50 |   61 vs 61   OK |    0.1803 vs 0.1803    OK | 0.016393 vs 0.016393 OK\n  portable 0.05 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  portable 0.10 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  portable 0.20 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  portable 0.30 |    0 vs 0    OK |    1.0000 vs 1.0000    OK |     None vs None     OK\n  portable 0.50 |   50 vs 50   OK |    0.4400 vs 0.4400    OK |     0.02 vs 0.02     OK\n\\nGrid reproduction: PASS — exact match\nDerived 1 multi-hop conclusion(s) from 2 admitted leaf facts:\n\n  CONCLUSION: party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1)  [rule: party_bound_effective ]\n     <- has_party(Premium Managed Hosting Agreement, AstroNutrition.com)\n        verdict=ENTAILED  W_i=0.8421 T=0.129032 alpha=0.5\n        provenance: \"This is a managed hosting agreement between AstroNutrition.com and deep systems....\"\n     <- effective_date(Premium Managed Hosting Agreement, March 1, 2005)\n        verdict=ENTAILED  W_i=0.7895 T=0.129032 alpha=0.5\n        provenance: \"The effective term is 12 months beginning March 1, 2005...\"\n\n----- trace-graph (Graphviz DOT) -----\ndigraph proof {\n  rankdir=TB;\n  node [style=filled, fontname=\"Helvetica\", fontsize=10];\n  labelloc=\"t\"; label=\"legal_cuad_00 [legal] party_bound_effective\";\n  n0 [label=\"party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1)\\nrule: party_bound_effective\", fillcolor=\"lightblue\", tooltip=\"derived conclusion\"];\n  n1 [label=\"has_party(Premium Managed Hosting Agreement, AstroNutrition.com)\\nW=0.8421 T=0.129032 a=0.5\\nFDP_hat=0.666667 r=1\", fillcolor=\"palegreen\", tooltip=\"This is a managed hosting agreement between AstroNutrition.com and deep systems.\"];\n  n2 [label=\"effective_date(Premium Managed Hosting Agreement, March 1, 2005)\\nW=0.7895 T=0.129032 a=0.5\\nFDP_hat=0.666667 r=1\", fillcolor=\"palegreen\", tooltip=\"The effective term is 12 months beginning March 1, 2005\"];\n  n0 -> n1 [label=\"party_bound_effective\", fontsize=8];\n  n0 -> n2 [label=\"party_bound_effective\", fontsize=8];\n}\n\n=== Legal-slice headline (recomputed from cached scores) ===\nelic      alpha  admit  cert decoy_fdr_hat  realized  raw_hall gate_hall\nlogprob    0.05      0 False        1.0000    0.0000  0.028169      None\nlogprob    0.10      0 False        1.0000    0.0000  0.028169      None\nlogprob    0.20     61  True        0.1803    0.0164  0.028169  0.016393\nlogprob    0.30     61  True        0.1803    0.0164  0.028169  0.016393\nlogprob    0.50     61  True        0.1803    0.0164  0.028169  0.016393\nportable   0.05      0 False        1.0000    0.0000  0.028169      None\nportable   0.10      0 False        1.0000    0.0000  0.028169      None\nportable   0.20      0 False        1.0000    0.0000  0.028169      None\nportable   0.30      0 False        1.0000    0.0000  0.028169      None\nportable   0.50     50  True        0.4400    0.0200  0.028169      0.02\n\nFull-run context (24-doc anchor): Decoy-gating reduces the hallucinated-fact rate vs raw LLM in 0 of the grid cells with CI separation; the largest CI-separated reduction is at regulatory/portable/alpha=0.5: raw=0.439 -> gate=0.360 (a ...\n=== ALL CODE CELLS RAN OK ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [83] ASSISTANT · 2026-06-16 13:36:29 UTC

```
The grid reproduces **exactly** and all checks pass. But there's a cosmetic parsing bug: the proof reconstruction splits the date tail `"March 1, 2005"` on the comma. The faithful fix is to build the KB directly from the example rows (`h`, `r`, `t`) like `method.py`'s `build_kb` does, rather than parsing label strings. Let me check what relations exist for the trace doc.
```

### [84] TOOL CALL — Bash · 2026-06-16 13:36:29 UTC

```
Inspect relations for trace doc legal_cuad_00:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json
d=json.load(open('mini_demo_data.json'))
exs=d['datasets'][0]['examples']
doc='legal_cuad_00'
rows=[e for e in exs if e['metadata_doc_id']==doc]
print('legal_cuad_00 reals: relations ->')
for e in rows:
    inp=json.loads(e['input'])
    print(f\"  {inp['relation']:20s} | head={inp['head']!r} tail={inp['tail']!r} | label={e['output']} hall_adj={e['metadata_hall_adj']} W_lp={round(e['metadata_w_cf_lp'],3)}\")
" 
```

### [85] TOOL RESULT — Bash · 2026-06-16 13:36:29 UTC

```
{"stdout": "legal_cuad_00 reals: relations ->\n  agreement_date       | head='Premium Managed Hosting Agreement' tail='03/01/05' | label=TRUE hall_adj=False W_lp=0.833\n  effective_date       | head='Premium Managed Hosting Agreement' tail='March 1, 2005' | label=TRUE hall_adj=False W_lp=-1.0\n  expiration_date      | head='Premium Managed Hosting Agreement' tail='February 28, 2006' | label=TRUE hall_adj=False W_lp=0.917\n  has_party            | head='Premium Managed Hosting Agreement' tail='AstroNutrition.com' | label=TRUE hall_adj=False W_lp=0.792\n  has_party            | head='Premium Managed Hosting Agreement' tail='deep systems' | label=TRUE hall_adj=False W_lp=0.875", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [86] ASSISTANT · 2026-06-16 13:37:09 UTC

```
The trace doc's reals include `has_party` and `effective_date` — so I can build the KB directly from example rows exactly as `method.py`'s `build_kb` does (more faithful, no label parsing). The published trace used the **portable** elicitation (T=0.129032 matches). Let me verify the portable W values match the published certs, then rewrite Step 6.
```

### [87] TOOL CALL — Bash · 2026-06-16 13:37:09 UTC

```
Verify portable W and FDP_hat match published trace certs:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json
d=json.load(open('mini_demo_data.json'))
exs=d['datasets'][0]['examples']
for e in exs:
    if e['metadata_doc_id']=='legal_cuad_00' and json.loads(e['input'])['relation'] in ('has_party','effective_date'):
        inp=json.loads(e['input'])
        print(f\"{inp['relation']:14s} tail={inp['tail']!r:24s} w_portable={round(e['metadata_w_cf_pt'],4)}\")
# published trace certs
tg=d['metadata']['trace_graph_legal_example']
print('--- published trace leaf certs ---')
for n in tg['graph']['nodes']:
    if n['kind']=='leaf':
        print(n['label'], '->', n['cert']['decoy_certificate'], n['cert']['entrapment_certificate'])
# certified legal/portable cell
for c in d['metadata']['hallucination_grid_legal']:
    if c['elicitation']=='portable' and c['certified']:
        print('certified portable cell: alpha',c['alpha'],'T',c['threshold'],'FDP_hat',c['entrapment']['FDP_hat'])
"
```

### [88] TOOL RESULT — Bash · 2026-06-16 13:37:09 UTC

```
{"stdout": "effective_date tail='March 1, 2005'          w_portable=0.7895\nhas_party      tail='AstroNutrition.com'     w_portable=0.8421\nhas_party      tail='deep systems'           w_portable=0.9474\n--- published trace leaf certs ---\nhas_party(Premium Managed Hosting Agreement, AstroNutrition.com) -> {'W_i': 0.8421, 'T': 0.129032, 'alpha': 0.5} {'FDP_hat': 0.666667, 'r': 1}\neffective_date(Premium Managed Hosting Agreement, March 1, 2005) -> {'W_i': 0.7895, 'T': 0.129032, 'alpha': 0.5} {'FDP_hat': 0.666667, 'r': 1}\ncertified portable cell: alpha 0.5 T 0.129032 FDP_hat 0.666667", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [89] ASSISTANT · 2026-06-16 13:37:31 UTC

```
Portable W values and the certified cell match the published trace certs exactly. Let me rewrite Step 6 to build the KB faithfully from example rows (like `method.py`'s `build_kb`), and add `prov` to the parse cell. Editing the builder.
```

### [90] TOOL CALL — Edit · 2026-06-16 13:37:31 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py
OLD:         "label": e["output"],                       # TRUE / FALSE / UNDECIDABLE (crisp gold)
        "hall_adj": bool(e["metadata_hall_adj"]),    # adjudicated hallucination flag
        "w_logprob": e["metadata_w_cf_lp"],          # signed-max W_i (logprob elicitation)
        "w_portable": e["metadata_w_cf_pt"],         # signed-max W_i (portable elicitation)
        "predict": e,                                # keep the row for validation vs published flags
NEW:         "label": e["output"],                        # TRUE / FALSE / UNDECIDABLE (crisp gold)
        "hall_adj": bool(e["metadata_hall_adj"]),     # adjudicated hallucination flag
        "prov": e["metadata_provenance_quote"],       # provenance quote (for leaf certificates)
        "w_logprob": e["metadata_w_cf_lp"],           # signed-max W_i (logprob elicitation)
        "w_portable": e["metadata_w_cf_pt"],          # signed-max W_i (portable elicitation)
        "predict": e,                                 # keep the row for validation vs published flags
```

### [91] TOOL RESULT — Edit · 2026-06-16 13:37:31 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py", "oldString": "        \"label\": e[\"output\"],                       # TRUE / FALSE / UNDECIDABLE (crisp gold)\n        \"hall_adj\": bool(e[\"metadata_hall_adj\"]),    # adjudicated hallucination flag\n        \"w_logprob\": e[\"metadata_w_cf_lp\"],          # signed-max W_i (logprob elicitation)\n        \"w_portable\": e[\"metadata_w_cf_pt\"],         # signed-max W_i (portable elicitation)\n        \"predict\": e,                                # keep the row for validation vs published flags", "newString": "        \"label\": e[\"output\"],                        # TRUE / FALSE / UNDECIDABLE (crisp gold)\n        \"hall_adj\": bool(e[\"metadata_hall_adj\"]),     # adjudicated hallucination flag\n        \"prov\": e[\"metadata_provenance_quote\"],       # provenance quote (for leaf certificates)\n        \"w_logprob\": e[\"metadata_w_cf_lp\"],           # signed-max W_i (logprob elicitation)\n        \"w_portable\": e[\"metadata_w_cf_pt\"],          # signed-max W_i (portable elicitation)\n        \"predict\": e,                                 # keep the row for validation vs published flags", "originalFile": null, "structuredPatch": [{"oldStart": 415, "oldLines": 11, "newStart": 415, "newLines": 12, "lines": ["     reals.append({", "         \"doc_id\": e[\"metadata_doc_id\"],", "         \"h\": inp[\"head\"], \"r\": inp[\"relation\"], \"t\": inp[\"tail\"],", "-        \"label\": e[\"output\"],                       # TRUE / FALSE / UNDECIDABLE (crisp gold)", "-        \"hall_adj\": bool(e[\"metadata_hall_adj\"]),    # adjudicated hallucination flag", "-        \"w_logprob\": e[\"metadata_w_cf_lp\"],          # signed-max W_i (logprob elicitation)", "-        \"w_portable\": e[\"metadata_w_cf_pt\"],         # signed-max W_i (portable elicitation)", "-        \"predict\": e,                                # keep the row for validation vs published flags", "+        \"label\": e[\"output\"],                        # TRUE / FALSE / UNDECIDABLE (crisp gold)", "+        \"hall_adj\": bool(e[\"metadata_hall_adj\"]),     # adjudicated hallucination flag", "+        \"prov\": e[\"metadata_provenance_quote\"],       # provenance quote (for leaf certificates)", "+        \"w_logprob\": e[\"metadata_w_cf_lp\"],           # signed-max W_i (logprob elicitation)", "+        \"w_portable\": e[\"metadata_w_cf_pt\"],          # signed-max W_i (portable elicitation)", "+        \"predict\": e,                                 # keep the row for validation vs published flags", "     })", " ", " n_docs = len({r[\"doc_id\"] for r in reals})"]}], "userModified": false, "replaceAll": false}
```

### [92] TOOL CALL — Edit · 2026-06-16 13:37:59 UTC

````
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py
OLD: md(r"""## Step 6 — Auditable proof trace-graph (`kb_engine` live)

The pipeline's deliverable is a **human-auditable reasoning trace**. Here we rebuild a real
2-hop legal derivation from the cached trace-graph leaves and the hand-authored legal bridge rule
(verbatim from `method.py: BRIDGE_RULES["legal"]`):

```
party_bound_effective(A, P, D) :- has_party(A, P), effective_date(A, D).
```

We load the two leaf facts (with their full certificates) from the cached trace, add the rule,
run the backward-chaining engine, and export the proof as Graphviz DOT — every leaf shows its
provenance and decoy/entrapment certificate.
""")

code(r"""# Legal bridge rule, verbatim from method.py BRIDGE_RULES["legal"][0]
LEGAL_BRIDGE = ("party_bound_effective", "party_bound_effective", (V("A"), V("P"), V("D")),
                [("has_party", (V("A"), V("P"))), ("effective_date", (V("A"), V("D")))])

# Reconstruct the KB from the cached trace-graph leaves (each carries its certificate).
trace_ex = meta["trace_graph_legal_example"]
kb = KB()
for node in trace_ex["graph"]["nodes"]:
    if node["kind"] != "leaf":
        continue
    # label looks like 'has_party(Agreement, Party)' -> recover pred + args
    pred, rest = node["label"].split("(", 1)
    args = tuple(a.strip() for a in rest.rstrip(")").split(","))
    kb.add_fact(pred, args, node["cert"])
kb.add_rule(*LEGAL_BRIDGE)

derived = kb.derive_all(max_depth=4)
print(f"Derived {len(derived)} multi-hop conclusion(s) from {len(kb.facts)} admitted leaf facts:\n")
for p in derived:
    print("  CONCLUSION:", f"{p['atom'][0]}({', '.join(p['atom'][1])})", " [rule:", p["rule"], "]")
    for lf in iter_leaves(p):
        cert = lf["cert"]
        dc = cert.get("decoy_certificate", {})
        print(f"     <- {lf['atom'][0]}({', '.join(lf['atom'][1])})")
        print(f"        verdict={cert.get('hallucination_verdict')}  "
              f"W_i={dc.get('W_i')} T={dc.get('T')} alpha={dc.get('alpha')}")
        print(f"        provenance: \"{str(cert.get('provenance',''))[:80]}...\"")

# Export the trace-graph as Graphviz DOT
graph = proof_to_graph(derived[0])
dot = graph_to_dot(graph, title=f"{trace_ex['doc_id']} [legal] {derived[0]['rule']}")
print("\n----- trace-graph (Graphviz DOT) -----")
print(dot)
""")
NEW: md(r"""## Step 6 — Auditable proof trace-graph (`kb_engine` live)

The pipeline's deliverable is a **human-auditable reasoning trace**. We rebuild a real 2-hop
legal derivation end-to-end: load every extracted fact for one document, attach each leaf's
**certificate** (provenance + decoy `W_i,T,α` + entrapment `FDP_hat,r`), add the hand-authored
legal bridge rules (verbatim from `method.py: BRIDGE_RULES["legal"]`), and run the backward-chaining
engine. This mirrors `method.py: build_kb` exactly. The headline elicitation is **portable** and
the gate cell is the certified `α=0.5` cell, so the reproduced certificates match the published trace.

```
party_bound_effective(A, P, D) :- has_party(A, P), effective_date(A, D).
titled_dated(A, T, D)          :- has_title(A, T), agreement_date(A, D).
```
""")

code(r"""# Legal bridge rules, verbatim from method.py BRIDGE_RULES["legal"]
BRIDGE_RULES_LEGAL = [
    ("party_bound_effective", "party_bound_effective", (V("A"), V("P"), V("D")),
     [("has_party", (V("A"), V("P"))), ("effective_date", (V("A"), V("D")))]),
    ("titled_dated", "titled_dated", (V("A"), V("T"), V("D")),
     [("has_title", (V("A"), V("T"))), ("agreement_date", (V("A"), V("D")))]),
]

# Headline elicitation + its certified gate cell (carries threshold T and alpha for the certs).
DEMO_DOC      = meta["trace_graph_legal_example"]["doc_id"]    # legal_cuad_00
HEADLINE_ELIC = "portable"
WKEY          = "w_portable"
gate_cell = next(c for c in reversed([g for g in grid if g["elicitation"] == HEADLINE_ELIC])
                 if c["certified"])
# entrapment FDP_hat comes from the full entrapment pool (published grid; not in the mini subset)
pub_cell = next(c for c in meta["hallucination_grid_legal"]
                if c["elicitation"] == HEADLINE_ELIC and c["alpha"] == gate_cell["alpha"])
fdp_hat = pub_cell["entrapment"]["FDP_hat"]

def build_kb(doc_reals, gate_cell, fdp_hat):
    # verbatim logic from method.py build_kb: each extracted fact -> a leaf with a certificate.
    kb = KB()
    for f in doc_reals:
        w = f[WKEY]
        cert = {"provenance": f["prov"],
                "provenance_char_span": None,
                "hallucination_verdict": "HALLUCINATED" if f["hall_adj"] else "ENTAILED",
                "decoy_certificate": {"W_i": round(w, 4),
                                      "T": gate_cell["threshold"], "alpha": gate_cell["alpha"]},
                "entrapment_certificate": {"FDP_hat": fdp_hat, "r": R_ENTRAP}}
        kb.add_fact(f["r"], (f["h"], f["t"]), cert)
    for spec in BRIDGE_RULES_LEGAL:
        kb.add_rule(*spec)
    return kb

doc_reals = [r for r in reals if r["doc_id"] == DEMO_DOC]
kb = build_kb(doc_reals, gate_cell, fdp_hat)
derived = kb.derive_all(max_depth=4)

print(f"Document {DEMO_DOC}: {len(doc_reals)} extracted facts -> "
      f"{len(derived)} multi-hop conclusion(s) (gate α={gate_cell['alpha']}, T={gate_cell['threshold']}):\n")
for p in derived:
    print("  CONCLUSION:", f"{p['atom'][0]}({', '.join(p['atom'][1])})", "[rule:", p["rule"] + "]")
    for lf in iter_leaves(p):
        cert = lf["cert"]; dc = cert.get("decoy_certificate", {})
        print(f"     <- {lf['atom'][0]}({', '.join(lf['atom'][1])})")
        print(f"        verdict={cert.get('hallucination_verdict')}  "
              f"W_i={dc.get('W_i')} T={dc.get('T')} alpha={dc.get('alpha')}")
        print(f"        provenance: \"{str(cert.get('provenance',''))[:80]}...\"")

# Export the first derivation's trace-graph as Graphviz DOT
graph = proof_to_graph(derived[0])
dot = graph_to_dot(graph, title=f"{DEMO_DOC} [legal] {derived[0]['rule']}")
print("\n----- trace-graph (Graphviz DOT) -----")
print(dot)
""")
````

### [93] TOOL RESULT — Edit · 2026-06-16 13:37:59 UTC

````
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py", "oldString": "md(r\"\"\"## Step 6 — Auditable proof trace-graph (`kb_engine` live)\n\nThe pipeline's deliverable is a **human-auditable reasoning trace**. Here we rebuild a real\n2-hop legal derivation from the cached trace-graph leaves and the hand-authored legal bridge rule\n(verbatim from `method.py: BRIDGE_RULES[\"legal\"]`):\n\n```\nparty_bound_effective(A, P, D) :- has_party(A, P), effective_date(A, D).\n```\n\nWe load the two leaf facts (with their full certificates) from the cached trace, add the rule,\nrun the backward-chaining engine, and export the proof as Graphviz DOT — every leaf shows its\nprovenance and decoy/entrapment certificate.\n\"\"\")\n\ncode(r\"\"\"# Legal bridge rule, verbatim from method.py BRIDGE_RULES[\"legal\"][0]\nLEGAL_BRIDGE = (\"party_bound_effective\", \"party_bound_effective\", (V(\"A\"), V(\"P\"), V(\"D\")),\n                [(\"has_party\", (V(\"A\"), V(\"P\"))), (\"effective_date\", (V(\"A\"), V(\"D\")))])\n\n# Reconstruct the KB from the cached trace-graph leaves (each carries its certificate).\ntrace_ex = meta[\"trace_graph_legal_example\"]\nkb = KB()\nfor node in trace_ex[\"graph\"][\"nodes\"]:\n    if node[\"kind\"] != \"leaf\":\n        continue\n    # label looks like 'has_party(Agreement, Party)' -> recover pred + args\n    pred, rest = node[\"label\"].split(\"(\", 1)\n    args = tuple(a.strip() for a in rest.rstrip(\")\").split(\",\"))\n    kb.add_fact(pred, args, node[\"cert\"])\nkb.add_rule(*LEGAL_BRIDGE)\n\nderived = kb.derive_all(max_depth=4)\nprint(f\"Derived {len(derived)} multi-hop conclusion(s) from {len(kb.facts)} admitted leaf facts:\\n\")\nfor p in derived:\n    print(\"  CONCLUSION:\", f\"{p['atom'][0]}({', '.join(p['atom'][1])})\", \" [rule:\", p[\"rule\"], \"]\")\n    for lf in iter_leaves(p):\n        cert = lf[\"cert\"]\n        dc = cert.get(\"decoy_certificate\", {})\n        print(f\"     <- {lf['atom'][0]}({', '.join(lf['atom'][1])})\")\n        print(f\"        verdict={cert.get('hallucination_verdict')}  \"\n              f\"W_i={dc.get('W_i')} T={dc.get('T')} alpha={dc.get('alpha')}\")\n        print(f\"        provenance: \\\"{str(cert.get('provenance',''))[:80]}...\\\"\")\n\n# Export the trace-graph as Graphviz DOT\ngraph = proof_to_graph(derived[0])\ndot = graph_to_dot(graph, title=f\"{trace_ex['doc_id']} [legal] {derived[0]['rule']}\")\nprint(\"\\n----- trace-graph (Graphviz DOT) -----\")\nprint(dot)\n\"\"\")", "newString": "md(r\"\"\"## Step 6 — Auditable proof trace-graph (`kb_engine` live)\n\nThe pipeline's deliverable is a **human-auditable reasoning trace**. We rebuild a real 2-hop\nlegal derivation end-to-end: load every extracted fact for one document, attach each leaf's\n**certificate** (provenance + decoy `W_i,T,α` + entrapment `FDP_hat,r`), add the hand-authored\nlegal bridge rules (verbatim from `method.py: BRIDGE_RULES[\"legal\"]`), and run the backward-chaining\nengine. This mirrors `method.py: build_kb` exactly. The headline elicitation is **portable** and\nthe gate cell is the certified `α=0.5` cell, so the reproduced certificates match the published trace.\n\n```\nparty_bound_effective(A, P, D) :- has_party(A, P), effective_date(A, D).\ntitled_dated(A, T, D)          :- has_title(A, T), agreement_date(A, D).\n```\n\"\"\")\n\ncode(r\"\"\"# Legal bridge rules, verbatim from method.py BRIDGE_RULES[\"legal\"]\nBRIDGE_RULES_LEGAL = [\n    (\"party_bound_effective\", \"party_bound_effective\", (V(\"A\"), V(\"P\"), V(\"D\")),\n     [(\"has_party\", (V(\"A\"), V(\"P\"))), (\"effective_date\", (V(\"A\"), V(\"D\")))]),\n    (\"titled_dated\", \"titled_dated\", (V(\"A\"), V(\"T\"), V(\"D\")),\n     [(\"has_title\", (V(\"A\"), V(\"T\"))), (\"agreement_date\", (V(\"A\"), V(\"D\")))]),\n]\n\n# Headline elicitation + its certified gate cell (carries threshold T and alpha for the certs).\nDEMO_DOC      = meta[\"trace_graph_legal_example\"][\"doc_id\"]    # legal_cuad_00\nHEADLINE_ELIC = \"portable\"\nWKEY          = \"w_portable\"\ngate_cell = next(c for c in reversed([g for g in grid if g[\"elicitation\"] == HEADLINE_ELIC])\n                 if c[\"certified\"])\n# entrapment FDP_hat comes from the full entrapment pool (published grid; not in the mini subset)\npub_cell = next(c for c in meta[\"hallucination_grid_legal\"]\n                if c[\"elicitation\"] == HEADLINE_ELIC and c[\"alpha\"] == gate_cell[\"alpha\"])\nfdp_hat = pub_cell[\"entrapment\"][\"FDP_hat\"]\n\ndef build_kb(doc_reals, gate_cell, fdp_hat):\n    # verbatim logic from method.py build_kb: each extracted fact -> a leaf with a certificate.\n    kb = KB()\n    for f in doc_reals:\n        w = f[WKEY]\n        cert = {\"provenance\": f[\"prov\"],\n                \"provenance_char_span\": None,\n                \"hallucination_verdict\": \"HALLUCINATED\" if f[\"hall_adj\"] else \"ENTAILED\",\n                \"decoy_certificate\": {\"W_i\": round(w, 4),\n                                      \"T\": gate_cell[\"threshold\"], \"alpha\": gate_cell[\"alpha\"]},\n                \"entrapment_certificate\": {\"FDP_hat\": fdp_hat, \"r\": R_ENTRAP}}\n        kb.add_fact(f[\"r\"], (f[\"h\"], f[\"t\"]), cert)\n    for spec in BRIDGE_RULES_LEGAL:\n        kb.add_rule(*spec)\n    return kb\n\ndoc_reals = [r for r in reals if r[\"doc_id\"] == DEMO_DOC]\nkb = build_kb(doc_reals, gate_cell, fdp_hat)\nderived = kb.derive_all(max_depth=4)\n\nprint(f\"Document {DEMO_DOC}: {len(doc_reals)} extracted facts -> \"\n      f\"{len(derived)} multi-hop conclusion(s) (gate α={gate_cell['alpha']}, T={gate_cell['threshold']}):\\n\")\nfor p in derived:\n    print(\"  CONCLUSION:\", f\"{p['atom'][0]}({', '.join(p['atom'][1])})\", \"[rule:\", p[\"rule\"] + \"]\")\n    for lf in iter_leaves(p):\n        cert = lf[\"cert\"]; dc = cert.get(\"decoy_certificate\", {})\n        print(f\"     <- {lf['atom'][0]}({', '.join(lf['atom'][1])})\")\n        print(f\"        verdict={cert.get('hallucination_verdict')}  \"\n              f\"W_i={dc.get('W_i')} T={dc.get('T')} alpha={dc.get('alpha')}\")\n        print(f\"        provenance: \\\"{str(cert.get('provenance',''))[:80]}...\\\"\")\n\n# Export the first derivation's trace-graph as Graphviz DOT\ngraph = proof_to_graph(derived[0])\ndot = graph_to_dot(graph, title=f\"{DEMO_DOC} [legal] {derived[0]['rule']}\")\nprint(\"\\n----- trace-graph (Graphviz DOT) -----\")\nprint(dot)\n\"\"\")", "originalFile": null, "structuredPatch": [{"oldStart": 548, "oldLines": 50, "newStart": 548, "newLines": 72, "lines": [" # ---------------------------------------------------------------------------", " md(r\"\"\"## Step 6 — Auditable proof trace-graph (`kb_engine` live)", " ", "-The pipeline's deliverable is a **human-auditable reasoning trace**. Here we rebuild a real", "-2-hop legal derivation from the cached trace-graph leaves and the hand-authored legal bridge rule", "-(verbatim from `method.py: BRIDGE_RULES[\"legal\"]`):", "+The pipeline's deliverable is a **human-auditable reasoning trace**. We rebuild a real 2-hop", "+legal derivation end-to-end: load every extracted fact for one document, attach each leaf's", "+**certificate** (provenance + decoy `W_i,T,α` + entrapment `FDP_hat,r`), add the hand-authored", "+legal bridge rules (verbatim from `method.py: BRIDGE_RULES[\"legal\"]`), and run the backward-chaining", "+engine. This mirrors `method.py: build_kb` exactly. The headline elicitation is **portable** and", "+the gate cell is the certified `α=0.5` cell, so the reproduced certificates match the published trace.", " ", " ```", " party_bound_effective(A, P, D) :- has_party(A, P), effective_date(A, D).", "+titled_dated(A, T, D)          :- has_title(A, T), agreement_date(A, D).", " ```", "-", "-We load the two leaf facts (with their full certificates) from the cached trace, add the rule,", "-run the backward-chaining engine, and export the proof as Graphviz DOT — every leaf shows its", "-provenance and decoy/entrapment certificate.", " \"\"\")", " ", "-code(r\"\"\"# Legal bridge rule, verbatim from method.py BRIDGE_RULES[\"legal\"][0]", "-LEGAL_BRIDGE = (\"party_bound_effective\", \"party_bound_effective\", (V(\"A\"), V(\"P\"), V(\"D\")),", "-                [(\"has_party\", (V(\"A\"), V(\"P\"))), (\"effective_date\", (V(\"A\"), V(\"D\")))])", "+code(r\"\"\"# Legal bridge rules, verbatim from method.py BRIDGE_RULES[\"legal\"]", "+BRIDGE_RULES_LEGAL = [", "+    (\"party_bound_effective\", \"party_bound_effective\", (V(\"A\"), V(\"P\"), V(\"D\")),", "+     [(\"has_party\", (V(\"A\"), V(\"P\"))), (\"effective_date\", (V(\"A\"), V(\"D\")))]),", "+    (\"titled_dated\", \"titled_dated\", (V(\"A\"), V(\"T\"), V(\"D\")),", "+     [(\"has_title\", (V(\"A\"), V(\"T\"))), (\"agreement_date\", (V(\"A\"), V(\"D\")))]),", "+]", " ", "-# Reconstruct the KB from the cached trace-graph leaves (each carries its certificate).", "-trace_ex = meta[\"trace_graph_legal_example\"]", "-kb = KB()", "-for node in trace_ex[\"graph\"][\"nodes\"]:", "-    if node[\"kind\"] != \"leaf\":", "-        continue", "-    # label looks like 'has_party(Agreement, Party)' -> recover pred + args", "-    pred, rest = node[\"label\"].split(\"(\", 1)", "-    args = tuple(a.strip() for a in rest.rstrip(\")\").split(\",\"))", "-    kb.add_fact(pred, args, node[\"cert\"])", "-kb.add_rule(*LEGAL_BRIDGE)", "+# Headline elicitation + its certified gate cell (carries threshold T and alpha for the certs).", "+DEMO_DOC      = meta[\"trace_graph_legal_example\"][\"doc_id\"]    # legal_cuad_00", "+HEADLINE_ELIC = \"portable\"", "+WKEY          = \"w_portable\"", "+gate_cell = next(c for c in reversed([g for g in grid if g[\"elicitation\"] == HEADLINE_ELIC])", "+                 if c[\"certified\"])", "+# entrapment FDP_hat comes from the full entrapment pool (published grid; not in the mini subset)", "+pub_cell = next(c for c in meta[\"hallucination_grid_legal\"]", "+                if c[\"elicitation\"] == HEADLINE_ELIC and c[\"alpha\"] == gate_cell[\"alpha\"])", "+fdp_hat = pub_cell[\"entrapment\"][\"FDP_hat\"]", " ", "+def build_kb(doc_reals, gate_cell, fdp_hat):", "+    # verbatim logic from method.py build_kb: each extracted fact -> a leaf with a certificate.", "+    kb = KB()", "+    for f in doc_reals:", "+        w = f[WKEY]", "+        cert = {\"provenance\": f[\"prov\"],", "+                \"provenance_char_span\": None,", "+                \"hallucination_verdict\": \"HALLUCINATED\" if f[\"hall_adj\"] else \"ENTAILED\",", "+                \"decoy_certificate\": {\"W_i\": round(w, 4),", "+                                      \"T\": gate_cell[\"threshold\"], \"alpha\": gate_cell[\"alpha\"]},", "+                \"entrapment_certificate\": {\"FDP_hat\": fdp_hat, \"r\": R_ENTRAP}}", "+        kb.add_fact(f[\"r\"], (f[\"h\"], f[\"t\"]), cert)", "+    for spec in BRIDGE_RULES_LEGAL:", "+        kb.add_rule(*spec)", "+    return kb", "+", "+doc_reals = [r for r in reals if r[\"doc_id\"] == DEMO_DOC]", "+kb = build_kb(doc_reals, gate_cell, fdp_hat)", " derived = kb.derive_all(max_depth=4)", "-print(f\"Derived {len(derived)} multi-hop conclusion(s) from {len(kb.facts)} admitted leaf facts:\\n\")", "+", "+print(f\"Document {DEMO_DOC}: {len(doc_reals)} extracted facts -> \"", "+      f\"{len(derived)} multi-hop conclusion(s) (gate α={gate_cell['alpha']}, T={gate_cell['threshold']}):\\n\")", " for p in derived:", "-    print(\"  CONCLUSION:\", f\"{p['atom'][0]}({', '.join(p['atom'][1])})\", \" [rule:\", p[\"rule\"], \"]\")", "+    print(\"  CONCLUSION:\", f\"{p['atom'][0]}({', '.join(p['atom'][1])})\", \"[rule:\", p[\"rule\"] + \"]\")", "     for lf in iter_leaves(p):", "-        cert = lf[\"cert\"]", "-        dc = cert.get(\"decoy_certificate\", {})", "+        cert = lf[\"cert\"]; dc = cert.get(\"decoy_certificate\", {})", "         print(f\"     <- {lf['atom'][0]}({', '.join(lf['atom'][1])})\")", "         print(f\"        verdict={cert.get('hallucination_verdict')}  \"", "               f\"W_i={dc.get('W_i')} T={dc.get('T')} alpha={dc.get('alpha')}\")", "         print(f\"        provenance: \\\"{str(cert.get('provenance',''))[:80]}...\\\"\")", " ", "-# Export the trace-graph as Graphviz DOT", "+# Export the first derivation's trace-graph as Graphviz DOT", " graph = proof_to_graph(derived[0])", "-dot = graph_to_dot(graph, title=f\"{trace_ex['doc_id']} [legal] {derived[0]['rule']}\")", "+dot = graph_to_dot(graph, title=f\"{DEMO_DOC} [legal] {derived[0]['rule']}\")", " print(\"\\n----- trace-graph (Graphviz DOT) -----\")", " print(dot)", " \"\"\")"]}], "userModified": false, "replaceAll": false}
````

### [94] ASSISTANT · 2026-06-16 13:38:09 UTC

```
Now rebuild and re-run the logic check.
```

### [95] TOOL CALL — Bash · 2026-06-16 13:38:09 UTC

```
Rebuild notebook and re-run logic check (focus on Step 6):
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 build_nb.py && python3 -c "
import json, matplotlib
matplotlib.use('Agg')
nb=json.load(open('code_demo.ipynb'))
ns={}
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i==1: continue
    src=''.join(c['source'])
    try:
        exec(src, ns)
    except Exception:
        import traceback; print(f'=== CELL {i} FAILED ==='); traceback.print_exc(); break
else:
    print('=== ALL CODE CELLS RAN OK ===')
" 2>&1 | sed -n '/Document legal_cuad_00/,$p' | head -40
```

### [96] TOOL RESULT — Bash · 2026-06-16 13:38:09 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/code_demo.ipynb with 21 cells\nDocument legal_cuad_00: 5 extracted facts -> 2 multi-hop conclusion(s) (gate α=0.5, T=0.129032):\n\n  CONCLUSION: party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1, 2005) [rule: party_bound_effective]\n     <- has_party(Premium Managed Hosting Agreement, AstroNutrition.com)\n        verdict=ENTAILED  W_i=0.8421 T=0.129032 alpha=0.5\n        provenance: \"This is a managed hosting agreement between AstroNutrition.com and deep systems....\"\n     <- effective_date(Premium Managed Hosting Agreement, March 1, 2005)\n        verdict=ENTAILED  W_i=0.7895 T=0.129032 alpha=0.5\n        provenance: \"The effective term is 12 months beginning March 1, 2005...\"\n  CONCLUSION: party_bound_effective(Premium Managed Hosting Agreement, deep systems, March 1, 2005) [rule: party_bound_effective]\n     <- has_party(Premium Managed Hosting Agreement, deep systems)\n        verdict=ENTAILED  W_i=0.9474 T=0.129032 alpha=0.5\n        provenance: \"This is a managed hosting agreement between AstroNutrition.com and deep systems....\"\n     <- effective_date(Premium Managed Hosting Agreement, March 1, 2005)\n        verdict=ENTAILED  W_i=0.7895 T=0.129032 alpha=0.5\n        provenance: \"The effective term is 12 months beginning March 1, 2005...\"\n\n----- trace-graph (Graphviz DOT) -----\ndigraph proof {\n  rankdir=TB;\n  node [style=filled, fontname=\"Helvetica\", fontsize=10];\n  labelloc=\"t\"; label=\"legal_cuad_00 [legal] party_bound_effective\";\n  n0 [label=\"party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1, 2005)\\nrule: party_bound_effective\", fillcolor=\"lightblue\", tooltip=\"derived conclusion\"];\n  n1 [label=\"has_party(Premium Managed Hosting Agreement, AstroNutrition.com)\\nW=0.8421 T=0.129032 a=0.5\\nFDP_hat=0.666667 r=1\", fillcolor=\"palegreen\", tooltip=\"This is a managed hosting agreement between AstroNutrition.com and deep systems.\"];\n  n2 [label=\"effective_date(Premium Managed Hosting Agreement, March 1, 2005)\\nW=0.7895 T=0.129032 a=0.5\\nFDP_hat=0.666667 r=1\", fillcolor=\"palegreen\", tooltip=\"The effective term is 12 months beginning March 1, 2005\"];\n  n0 -> n1 [label=\"party_bound_effective\", fontsize=8];\n  n0 -> n2 [label=\"party_bound_effective\", fontsize=8];\n}\n\n=== Legal-slice headline (recomputed from cached scores) ===\nelic      alpha  admit  cert decoy_fdr_hat  realized  raw_hall gate_hall\nlogprob    0.05      0 False        1.0000    0.0000  0.028169      None\nlogprob    0.10      0 False        1.0000    0.0000  0.028169      None\nlogprob    0.20     61  True        0.1803    0.0164  0.028169  0.016393\nlogprob    0.30     61  True        0.1803    0.0164  0.028169  0.016393\nlogprob    0.50     61  True        0.1803    0.0164  0.028169  0.016393\nportable   0.05      0 False        1.0000    0.0000  0.028169      None\nportable   0.10      0 False        1.0000    0.0000  0.028169      None\nportable   0.20      0 False        1.0000    0.0000  0.028169      None\nportable   0.30      0 False        1.0000    0.0000  0.028169      None", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [97] ASSISTANT · 2026-06-16 13:38:19 UTC

```
Step 6 now reproduces the published trace exactly (correct date tail, matching certs, both parties derived). Now the real validation: run the full clean-environment test as specified. Let me launch it in the background.
```

### [98] TOOL CALL — Bash · 2026-06-16 13:38:19 UTC

```
Create clean .nb_env and install jupyter:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && rm -rf .nb_env && /usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -3 && echo "ENV_READY"
```

### [99] TOOL RESULT — Bash · 2026-06-16 13:43:17 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bs6o5ywix", "assistantAutoBackgrounded": false}
```

### [100] ASSISTANT · 2026-06-16 13:43:45 UTC

```
While the env installs, let me check a `\n` escaping issue I noticed in the Step 5 output (literal `\n` printed instead of a newline).
```

### [101] TOOL CALL — Bash · 2026-06-16 13:43:45 UTC

```
Find double-backslash-n occurrences in builder:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && grep -n '\\\\n' build_nb.py
```

### [102] TOOL RESULT — Bash · 2026-06-16 13:43:45 UTC

```
{"stdout": "377:            color, extra = \"lightblue\", f'\\\\nrule: {html.escape(str(n.get(\"rule\")))}'\n385:            extra = (f'\\\\nW={dc.get(\"W_i\")} T={dc.get(\"T\")} a={dc.get(\"alpha\")}'\n386:                     f'\\\\nFDP_hat={ec.get(\"FDP_hat\")} r={ec.get(\"r\")}')\n527:print(\"\\\\nCheck 2 — recomputed grid vs published grid:\")\n545:print(f\"\\\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}\")", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [103] ASSISTANT · 2026-06-16 13:43:55 UTC

```
Lines 377/385/386 are correct — those are literal `\n` for Graphviz DOT labels (verbatim from `kb_engine.py`). Lines 527/545 are the bug: they print a literal `\n` instead of a newline. Let me fix those two.
```

### [104] TOOL CALL — Edit · 2026-06-16 13:43:55 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py
OLD: print("\\nCheck 2 — recomputed grid vs published grid:")
NEW: print("\nCheck 2 — recomputed grid vs published grid:")
```

### [105] TOOL RESULT — Edit · 2026-06-16 13:43:55 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py", "oldString": "print(\"\\\\nCheck 2 — recomputed grid vs published grid:\")", "newString": "print(\"\\nCheck 2 — recomputed grid vs published grid:\")", "originalFile": null, "structuredPatch": [{"oldStart": 524, "oldLines": 7, "newStart": 524, "newLines": 7, "lines": [" ", " # --- Check 2: grid cells match the published legal hallucination_grid ---", " pub = {(c[\"genre\"], c[\"elicitation\"], c[\"alpha\"]): c for c in meta[\"hallucination_grid_legal\"]}", "-print(\"\\\\nCheck 2 — recomputed grid vs published grid:\")", "+print(\"\\nCheck 2 — recomputed grid vs published grid:\")", " print(f\"  {'elic':8s} {'a':>4s} | {'admit':>11s} | {'decoy_fdr_hat':>22s} | {'gate_hall':>20s}\")", " all_ok = True", " for c in grid:"]}], "userModified": false, "replaceAll": false}
```

### [106] TOOL CALL — Edit · 2026-06-16 13:43:55 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py
OLD: print(f"\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}")
NEW: print(f"\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}")
```

### [107] TOOL RESULT — Edit · 2026-06-16 13:43:55 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/build_nb.py", "oldString": "print(f\"\\\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}\")", "newString": "print(f\"\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}\")", "originalFile": null, "structuredPatch": [{"oldStart": 542, "oldLines": 7, "newStart": 542, "newLines": 7, "lines": ["           f\"{c['decoy_fdr_hat']:>9.4f} vs {p['decoy_fdr_hat']:<9.4f} \"", "           f\"{'OK' if fdr_ok else 'XX'} | \"", "           f\"{str(c['gate_hall_rate']):>8} vs {str(gh_pub):<8} {'OK' if gh_ok else 'XX'}\")", "-print(f\"\\\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}\")", "+print(f\"\\nGrid reproduction: {'PASS — exact match' if all_ok else 'FAIL'}\")", " \"\"\")", " ", " # ---------------------------------------------------------------------------"]}], "userModified": false, "replaceAll": false}
```

### [108] ASSISTANT · 2026-06-16 13:44:09 UTC

```
Now rebuild the notebook with the fix while the env installs.
```

### [109] TOOL CALL — Bash · 2026-06-16 13:44:09 UTC

```
Rebuild notebook and verify newline fix:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 build_nb.py && echo "---check ipynb valid json + newline in Step5---" && python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
src=''.join(nb['cells'][16]['source'])  # Step 5 validation cell
print('contains real newline before Check 2:', '\nCheck 2' in src)
print('contains literal backslash-n:', '\\\\nCheck 2' in src)
"
```

### [110] TOOL RESULT — Bash · 2026-06-16 13:44:09 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/code_demo.ipynb with 21 cells\n---check ipynb valid json + newline in Step5---\ncontains real newline before Check 2: False\ncontains literal backslash-n: True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [111] ASSISTANT · 2026-06-16 13:44:23 UTC

```
Source is correct — the cell contains the code text `print("\nCheck 2")` (which Python turns into a newline at runtime). Let me confirm the actual printed output now has real newlines via a quick system-Python run.
```

### [112] TOOL CALL — Bash · 2026-06-16 13:44:23 UTC

```
Confirm output newlines render correctly:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json, matplotlib
matplotlib.use('Agg')
nb=json.load(open('code_demo.ipynb'))
ns={}
import io, contextlib
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    for i,c in enumerate(nb['cells']):
        if c['cell_type']!='code' or i==1: continue
        exec(''.join(c['source']), ns)
out=buf.getvalue()
# check no literal backslash-n in output
print('literal \\\\n in output:', '\\\\nCheck' in out or '\\\\nGrid' in out)
print('--- snippet around Check 2 ---')
idx=out.find('Check 2'); print(out[idx-2:idx+60])
print('--- PASS lines ---')
for line in out.splitlines():
    if 'PASS' in line or 'FAIL' in line or 'reproduction' in line: print(' ', line)
"
```

### [113] TOOL RESULT — Bash · 2026-06-16 13:44:23 UTC

```
{"stdout": "literal \\n in output: False\n--- snippet around Check 2 ---\n\n\nCheck 2 — recomputed grid vs published grid:\n  elic        a\n--- PASS lines ---\n  Check 1 — per-fact admission mismatches vs published flags: 0  (PASS)\n  Grid reproduction: PASS — exact match", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [114] ASSISTANT · 2026-06-16 13:44:37 UTC

```
Newlines render correctly now. Let me check the env install status.
```

### [115] TOOL CALL — Bash · 2026-06-16 13:44:37 UTC

```
Check env install background output:
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-3-art-vkfyOl2OQNVx/cd18fcd7-692e-4ce1-a8a4-1255d4eefe88/tasks/bs6o5ywix.output 2>/dev/null | tail -5
```

### [116] TOOL RESULT — Bash · 2026-06-16 13:44:37 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [117] TOOL CALL — Bash · 2026-06-16 13:44:41 UTC

```
Check env install output file:
f=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-3-art-vkfyOl2OQNVx/cd18fcd7-692e-4ce1-a8a4-1255d4eefe88/tasks/bs6o5ywix.output; ls -la "$f"; echo "---tail---"; tail -8 "$f"
```

### [118] TOOL RESULT — Bash · 2026-06-16 13:44:41 UTC

```
{"stdout": "-rw-r--r-- 1 root root 0 Jun 16 13:38 /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-3-art-vkfyOl2OQNVx/cd18fcd7-692e-4ce1-a8a4-1255d4eefe88/tasks/bs6o5ywix.output\n---tail---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [119] TOOL CALL — TaskUpdate · 2026-06-16 13:44:49 UTC

```
{'taskId': '3', 'status': 'completed'}
```

### [120] TOOL RESULT — TaskUpdate · 2026-06-16 13:44:49 UTC

```
{"success": true, "taskId": "3", "updatedFields": ["status"], "statusChange": {"from": "in_progress", "to": "completed"}}
```

### [121] TOOL CALL — TaskUpdate · 2026-06-16 13:44:49 UTC

```
{'taskId': '4', 'status': 'in_progress'}
```

### [122] TOOL RESULT — TaskUpdate · 2026-06-16 13:44:49 UTC

```
{"success": true, "taskId": "4", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "in_progress"}}
```

### [123] ASSISTANT · 2026-06-16 13:44:59 UTC

```
Let me wait for the env install to finish, then run the notebook in the clean env.
```

### [124] TOOL CALL — Bash · 2026-06-16 13:44:59 UTC

```
Wait for env install to complete:
f=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-3-art-vkfyOl2OQNVx/cd18fcd7-692e-4ce1-a8a4-1255d4eefe88/tasks/bs6o5ywix.output
for i in $(seq 1 60); do
  if grep -q ENV_READY "$f" 2>/dev/null; then echo "READY after ~$((i*5))s"; break; fi
  sleep 5
done
tail -4 "$f"; ls /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/.nb_env/bin/jupyter 2>/dev/null && echo "jupyter present"
```

### [125] TOOL RESULT — Bash · 2026-06-16 13:48:12 UTC

```
{"stdout": "READY after ~200s\n\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: python3.12 -m pip install --upgrade pip\nENV_READY\n/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/.nb_env/bin/jupyter\njupyter present", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [126] ASSISTANT · 2026-06-16 13:48:18 UTC

```
Env is ready. Now run the notebook in the clean environment (the install cell will install numpy/scipy/matplotlib at Colab versions). Running in background with timing.
```

### [127] TOOL CALL — Bash · 2026-06-16 13:48:18 UTC

```
Execute notebook in clean env, measure runtime:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && t0=$(date +%s) && .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -20; echo "EXIT=${PIPESTATUS[0]}"; t1=$(date +%s); echo "RUNTIME=$((t1-t0))s"
```

### [128] TOOL RESULT — Bash · 2026-06-16 13:48:18 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bv2txene2"}
```

### [129] ASSISTANT · 2026-06-16 13:48:30 UTC

```
The notebook is executing in the clean env (background). Let me poll for completion.
```

### [130] TOOL CALL — Bash · 2026-06-16 13:48:30 UTC

```
Wait for notebook execution and show result:
f=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-3-art-vkfyOl2OQNVx/cd18fcd7-692e-4ce1-a8a4-1255d4eefe88/tasks/bv2txene2.output
for i in $(seq 1 80); do
  if grep -q "RUNTIME=" "$f" 2>/dev/null; then echo "DONE"; break; fi
  sleep 5
done
echo "=== output ==="; cat "$f"
```

### [131] TOOL RESULT — Bash · 2026-06-16 13:53:48 UTC

```
{"stdout": "DONE\n=== output ===\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/.nb_env/lib/python3.12/site-packages/nbformat/__init__.py:96: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.\n  validate(nb)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 130715 bytes to code_demo.ipynb\nEXIT=0\nRUNTIME=327s", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [132] ASSISTANT · 2026-06-16 13:54:00 UTC

```
Notebook executed successfully (exit 0) in the clean env, total 327s (mostly the one-time numpy/scipy/matplotlib install — on Colab those are pre-installed, so actual runtime is seconds). Well within the 600s budget. Let me verify the executed outputs are correct.
```

### [133] TOOL CALL — Bash · 2026-06-16 13:54:00 UTC

```
Inspect executed notebook outputs for errors and figures:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
errs=0; nfig=0; ntext=0
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error':
            errs+=1; print('ERROR in cell',i,':',o.get('ename'),o.get('evalue'))
        if o.get('output_type')=='display_data' and 'image/png' in o.get('data',{}): nfig+=1
        if o.get('output_type')=='stream': ntext+=1
print('errors:',errs,'| figures(png):',nfig,'| stream outputs:',ntext)
# print key validation lines from outputs
for c in nb['cells']:
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream':
            for line in ''.join(o.get('text','')).splitlines():
                if any(k in line for k in ['PASS','FAIL','reproduction','mismatches','CONCLUSION','Derived','-> ']):
                    print('  ',line)
"
```

### [134] TOOL RESULT — Bash · 2026-06-16 13:54:00 UTC

```
{"stdout": "errors: 0 | figures(png): 1 | stream outputs: 10\n   \u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n   Check 1 — per-fact admission mismatches vs published flags: 0  (PASS)\n   Grid reproduction: PASS — exact match\n   Document legal_cuad_00: 5 extracted facts -> 2 multi-hop conclusion(s) (gate α=0.5, T=0.129032):\n     CONCLUSION: party_bound_effective(Premium Managed Hosting Agreement, AstroNutrition.com, March 1, 2005) [rule: party_bound_effective]\n     CONCLUSION: party_bound_effective(Premium Managed Hosting Agreement, deep systems, March 1, 2005) [rule: party_bound_effective]\n     n0 -> n1 [label=\"party_bound_effective\", fontsize=8];\n     n0 -> n2 [label=\"party_bound_effective\", fontsize=8];\n   Full-run context (24-doc anchor): Decoy-gating reduces the hallucinated-fact rate vs raw LLM in 0 of the grid cells with CI separation; the largest CI-separated reduction is at regulatory/portable/alpha=0.5: raw=0.439 -> gate=0.360 (a ...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [135] ASSISTANT · 2026-06-16 13:54:26 UTC

```
Zero errors, 1 figure, both validation checks PASS, and the proof engine derives the correct multi-hop conclusions. The notebook uses the **original** parameters (`B_BOOT=2000`, all alphas, both elicitations, all 71 legal reals) and runs in 327s total in the clean env — comfortably within budget — so no scaling-down is needed. Let me add cell IDs (to clear the nbformat warning) and verify the GitHub URL + load pattern.
```

### [136] TOOL CALL — Bash · 2026-06-16 13:54:26 UTC

```
Add cell ids and verify GitHub URL + load pattern + files exist:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json
p='code_demo.ipynb'
nb=json.load(open(p))
miss=sum(1 for c in nb['cells'] if 'id' not in c)
for i,c in enumerate(nb['cells']):
    if 'id' not in c: c['id']=f'cell{i:02d}'
json.dump(nb, open(p,'w'), indent=1)
print('added ids to', miss, 'cells; total cells', len(nb['cells']))
" && echo "--- URL + pattern checks ---" && grep -c 'GITHUB_DATA_URL = \"https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-3/experiment-2/demo/mini_demo_data.json\"' code_demo.ipynb && grep -c 'urllib.request.urlopen(GITHUB_DATA_URL)' code_demo.ipynb && grep -c 'os.path.exists("mini_demo_data.json")' code_demo.ipynb && ls -la mini_demo_data.json code_demo.ipynb
```

### [137] TOOL RESULT — Bash [ERROR] · 2026-06-16 13:54:26 UTC

```
Error: Exit code 1
added ids to 0 cells; total cells 21
--- URL + pattern checks ---
0
```

### [138] ASSISTANT · 2026-06-16 13:54:38 UTC

```
nbconvert already added ids. The exact-string grep failed only because of shell quote-escaping (the URL is JSON-encoded with escaped quotes). Let me verify with a Python check on the parsed cell source.
```

### [139] TOOL CALL — Bash · 2026-06-16 13:54:38 UTC

```
Verify GitHub URL, load pattern, ids, files via parsed JSON:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
allsrc='\n'.join(''.join(c['source']) for c in nb['cells'])
url='https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-3/experiment-2/demo/mini_demo_data.json'
print('exact GITHUB_DATA_URL assignment present:', ('GITHUB_DATA_URL = \"'+url+'\"') in allsrc)
print('urlopen(GITHUB_DATA_URL) present:', 'urllib.request.urlopen(GITHUB_DATA_URL)' in allsrc)
print('local fallback open(mini_demo_data.json) present:', 'os.path.exists(\"mini_demo_data.json\")' in allsrc)
print('data=load_data() present:', 'data = load_data()' in allsrc)
print('cells all have ids:', all('id' in c for c in nb['cells']))
import os
print('mini exists:', os.path.exists('mini_demo_data.json'), '| size KB:', round(os.path.getsize('mini_demo_data.json')/1024,1))
print('ipynb size KB:', round(os.path.getsize('code_demo.ipynb')/1024,1))
"
```

### [140] TOOL RESULT — Bash · 2026-06-16 13:54:38 UTC

```
{"stdout": "exact GITHUB_DATA_URL assignment present: True\nurlopen(GITHUB_DATA_URL) present: True\nlocal fallback open(mini_demo_data.json) present: True\ndata=load_data() present: True\ncells all have ids: True\nmini exists: True | size KB: 133.5\nipynb size KB: 127.9", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [141] ASSISTANT · 2026-06-16 13:54:58 UTC

```
All verifications pass. Let me update tasks, clean up the disposable test env, and write the struct output.
```

### [142] TOOL CALL — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{'taskId': '4', 'status': 'completed'}
```

### [143] TOOL RESULT — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{"success": true, "taskId": "4", "updatedFields": ["status"], "statusChange": {"from": "in_progress", "to": "completed"}}
```

### [144] TOOL CALL — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{'taskId': '5', 'status': 'completed'}
```

### [145] TOOL RESULT — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{"success": true, "taskId": "5", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "completed"}}
```

### [146] TOOL CALL — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{'taskId': '6', 'status': 'in_progress'}
```

### [147] TOOL RESULT — TaskUpdate · 2026-06-16 13:54:58 UTC

```
{"success": true, "taskId": "6", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "in_progress"}}
```

### [148] TOOL CALL — Bash · 2026-06-16 13:54:58 UTC

```
Remove disposable test env and list workspace:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/ && rm -rf .nb_env && echo "removed .nb_env" && ls -la
```

### [149] TOOL RESULT — Bash · 2026-06-16 13:56:22 UTC

```
{"stdout": "removed .nb_env\ntotal 5898\ndrwxr-xr-x 2 root root 2000191 Jun 16 13:56 .\ndrwxr-xr-x 5 root root 2029133 Jun 16 13:32 ..\n-rw-r--r-- 1 root root 1708251 Jun 16 13:56 .repl_agent.ptylog\n-rw-r--r-- 1 root root   32714 Jun 16 13:43 build_nb.py\n-rw-r--r-- 1 root root  130979 Jun 16 13:54 code_demo.ipynb\n-rw-r--r-- 1 root root  136657 Jun 16 13:32 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [150] ASSISTANT · 2026-06-16 13:56:26 UTC

```
Now let me write the required struct output JSON.
```

### [151] TOOL CALL — Write · 2026-06-16 13:56:26 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [152] TOOL RESULT — Write · 2026-06-16 13:56:26 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_3/art_vkfyOl2OQNVx/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [153] TOOL CALL — TaskUpdate · 2026-06-16 13:56:30 UTC

```
{'taskId': '6', 'status': 'completed'}
```

### [154] TOOL RESULT — TaskUpdate · 2026-06-16 13:56:30 UTC

```
{"success": true, "taskId": "6", "updatedFields": ["status"], "statusChange": {"from": "in_progress", "to": "completed"}}
```

### [155] ASSISTANT · 2026-06-16 13:56:48 UTC

```
All tasks complete. Here's a summary of what I delivered.

## Summary

Converted the LLM-heavy `method.py` pipeline into a faithful, **offline** demo notebook. Since the full pipeline makes ~5000 paid LLM calls to extract and score facts, the demo loads the **cached per-fact scores** and re-runs the pipeline's deterministic, no-API core verbatim — reproducing the published results exactly.

### Deliverables (in workspace)
- **`mini_demo_data.json`** (133 KB) — the **legal / CUAD-crisp slice**: all 71 extracted real facts with their precomputed signed-max knockoff statistic `W_i` (both elicitations), gold label, and hallucination flag; plus the 10 published legal grid cells and a legal trace-graph example for validation.
- **`code_demo.ipynb`** (21 cells, executed with outputs) — splits the script into logical cells with markdown between each section.

### What the notebook does (minimal changes — original code preserved)
1. **`fdr_stats.py` core, verbatim** — the knockoff+ threshold `T(α)` (Barber–Candès eq 1.9) + document-block bootstrap.
2. **`kb_engine.py` core, verbatim** — the backward-chaining proof engine + DOT trace-graph export.
3. **Re-runs `gate_and_hall_grid`** on the cached `W_i`: thresholds, admissions, `decoy_fdr_hat`, realized FDR, and gate-vs-raw hallucination rates with bootstrap CIs.
4. **Validation** — recomputed admissions match the published `predict_admit_*` flags (0 mismatches) and the grid cells match the published `hallucination_grid` **exactly** (PASS).
5. **Proof engine live** — builds the KB from `legal_cuad_00`'s facts (mirroring `build_kb`) + the legal bridge rule, derives `party_bound_effective(...)`, and emits the certificate-bearing trace-graph.
6. **3-panel visualization** — `W_i` distribution + thresholds, self-reported vs realized FDR, and gate-vs-raw hallucination rate.

### Verification
- Clean-env (`.nb_env`) run: **exit 0, 0 errors, 1 figure**, total **327s** (mostly one-time numpy/scipy/matplotlib install; on Colab those are pre-installed). Comfortably under the 600s budget.
- Uses the **original** parameters (`B_BOOT=2000`, full α-grid, both elicitations, all 71 reals) — no scaling-down needed.
- `GITHUB_DATA_URL` exact match ✓, `urlopen(GITHUB_DATA_URL)` with local fallback ✓, `mini_demo_data.json` present ✓.

`.terminal_claude_agent_struct_out.json` written with the expected files.
```
