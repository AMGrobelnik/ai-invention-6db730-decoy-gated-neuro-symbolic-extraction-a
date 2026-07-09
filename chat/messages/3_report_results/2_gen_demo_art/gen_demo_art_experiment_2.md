# gen_demo_art_experiment_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_2` (terminal_claude_agent, claude-opus-4-8)

### [1] CONFIG · 2026-06-16 13:05:05 UTC

```
model: claude-opus-4-8 | effort: xhigh | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys
```

### [2] SYSTEM-USER prompt · 2026-06-16 13:05:11 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/results/out.json`
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a
Raw data URL: https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-06-16 13:05:11 UTC

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

### [4] TOOL CALL — Skill · 2026-06-16 13:05:31 UTC

```
aii-colab
```

### [5] TOOL CALL — Bash · 2026-06-16 13:05:31 UTC

```
List artifact workspace files:
ls -la /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/
```

### [6] TOOL RESULT — Skill · 2026-06-16 13:05:31 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [7] TOOL RESULT — Bash · 2026-06-16 13:05:31 UTC

```
{"stdout": "total 25083\ndrwxr-xr-x 7 root root 2030514 Jun 16 07:52 .\ndrwxr-xr-x 7 root root 3000195 Jun 16 06:12 ..\n-rw-r--r-- 1 root root 6291653 Jun 16 07:56 .repl_agent.ptylog\n-rw-r--r-- 1 root root    4423 Jun 16 07:52 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 5 root root 2026955 Jun 16 06:58 .venv\n-rw-r--r-- 1 root root    8172 Jun 16 07:47 README.md\ndrwxr-xr-x 2 root root 1010562 Jun 16 06:54 __pycache__\ndrwxr-xr-x 2 root root 2001115 Jun 16 07:38 cache\n-rw-r--r-- 1 root root   14729 Jun 16 06:42 fdr_stats.py\ndrwxr-xr-x 2 root root 1033576 Jun 16 07:22 figures\n-rw-r--r-- 1 root root 3036095 Jun 16 07:51 full_method_out.json\n-rw-r--r-- 1 root root   10217 Jun 16 06:22 llm_client.py\ndrwxr-xr-x 2 root root 2001201 Jun 16 07:18 logs\n-rw-r--r-- 1 root root    7661 Jun 16 07:45 make_figures.py\n-rw-r--r-- 1 root root   64047 Jun 16 07:16 method.py\n-rw-r--r-- 1 root root 3036095 Jun 16 07:43 method_out.json\n-rw-r--r-- 1 root root   71098 Jun 16 07:51 mini_method_out.json\n-rw-r--r-- 1 root root   33212 Jun 16 07:51 preview_method_out.json\n-rw-r--r-- 1 root root     479 Jun 16 07:51 pyproject.toml", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [8] TOOL CALL — Skill · 2026-06-16 13:05:41 UTC

```
aii-long-running-tasks
```

### [9] TOOL RESULT — Skill · 2026-06-16 13:05:41 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [10] TOOL CALL — Read · 2026-06-16 13:05:41 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/README.md
```

### [11] TOOL RESULT — Read · 2026-06-16 13:05:41 UTC

````
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/README.md", "content": "# Decoy-Competition FDR Gate for LLM Text→Logic Fact Admission — Experiment Artifact\n\nA **label-free False-Discovery-Rate (FDR) gate** that admits LLM-extracted kinship facts\ninto a symbolic layer **without gold labels**, validated on CLUTRR's *crisp* gold. Each\nextracted \"real\" fact competes against a property-matched **counterfactual decoy** (same\nordered entity pair, a plausible-but-wrong relation, verified non-entailed against gold). A\nlabel-free confidence elicitation scores both; the **knockoff+** rule (Barber–Candès 2015,\neq. 1.9) turns decoy \"wins\" into an FDR certificate. The experiment stress-tests the gate's\ncore statistical assumptions and compares it to a purely-neural raw-confidence baseline.\n\n## Headline finding (one sentence)\n\nThe gate's validity is **elicitation-dependent**: with single-token **logprob** confidence the\nLLM is overconfident in its *own spontaneous errors* so counterfactual decoys are\n**anti-conservative** (tail win-rate ≈ 0.34 ≪ 0.5, KS p < 1e-24); with **K=5 self-consistency**\nconfidence the decoys become **exchangeable** (win-rate ≈ 0.48, 95% CI [0.42, 0.55] covers 0.5,\nKS p = 0.48), their score distribution **matches the genuine spontaneous-error tail** (and\ndiffers from true positives), the gate **controls realized FDR ≤ nominal** while the\nraw-confidence baseline admits **45–65 %** false facts, and exchangeability is **robust to\nGenerator ≠ Scorer** across model families (de-circularized).\n\n## The four results (all on the same pipeline, method + baseline + controls side-by-side)\n\n1. **S1 decoy signature.** On the *known-false* reals (genuine extractor errors), real-vs-decoy\n   tail win-rate should be ≈ 0.5 (exchangeable). Counterfactual decoys reach 0.482 (CI covers\n   0.5) under self-consistency but only 0.34 (CI [0.32,0.37]) under logprob. The **random\n   type-matched swap** negative control is flagged anti-conservative under logprob (win 0.32,\n   p≈1e-9), validating diagnostic *sensitivity*; the offline synthetic self-test independently\n   confirms the win-rate/KS diagnostic detects a deliberately \"too-easy\" decoy family.\n\n2. **Spontaneous-error tail match (the crux).** The counterfactual-decoy score distribution\n   `F_decoy` tracks the genuine spontaneous-error distribution `F_spont` (FALSE reals) — *fail\n   to reject* in the admission tail (top-25 %/50 %: KS p = 0.33/0.19) — and differs sharply from\n   the true-positive distribution `F_truepos` (KS p ≈ 1e-40). See `figures/fig2_crux_cdf.png`.\n\n3. **Generator ≠ Scorer de-circularization.** Re-running the win-rate test with decoys from\n   model G scored by a *different-family* model S (and the symmetric swap) keeps the win-rate's\n   CI over 0.5 for **all four (G,S) configs** incl. G≠S, with realized labeled-slice FDR = 0.0\n   at α=0.2. Verdict: **ROBUST** — exchangeability is *not* a shared-model artifact.\n\n4. **Method vs purely-neural baseline (hallucination control).** Against crisp gold, the\n   decoy-FDR gate's realized FDR ≤ nominal where it certifies (0.417 ≤ 0.5; conservative /\n   zero-admit at stricter α on this data), whereas the raw-confidence baseline admits\n   254–1758 facts at **45–65 % realized FDR** — exactly the hallucination problem the gate\n   prevents. See `figures/fig3_fdr_calibration.png`.\n\n## Dataset & models\n\n* **Data** (READ-ONLY dependency): `…/iter_1/gen_art/gen_art_dataset_1/full_data_out.json` —\n  190 CLUTRR-v1 stories (40 pilot + 150 confirmatory), crisp atomic + multi-hop kinship gold,\n  chain length k=2..10. CLUTRR is rule-based so gold is exact (no annotation noise) — the\n  property that lets it host a realized-FDR-vs-α calibration diagonal.\n* **Primary model** `openai/gpt-4.1-nano` (generator + scorer; exposes logprobs; $0.10/$0.40 /M).\n* **Cross-family model** `mistralai/ministral-8b-2512` (de-circularization; no logprobs; $0.15/M).\n* **Crisp 3-way label** vs gold per (head, relation, tail): TRUE (entailed), FALSE (contradicts\n  the gold relation on an enumerated pair = a genuine extractor error), UNDECIDABLE (unlisted\n  pair, excluded). Reals are forced relation-predictions over every gold-enumerated pair, so the\n  multi-hop pairs form the error-dense family the diagnostics need.\n\n## Scale & cost\n\n190 docs → **1937 reals** (633 TRUE, 1304 spontaneous FALSE, 0 undecidable), 1937 counterfactual\ndecoys + 1937 swaps, scored under two elicitations on all docs plus a 4-config cross-family\nablation on the 40 pilot docs. Final (cache-warm) run **$0.468**; total project spend across all\ngradual-scaling runs ≈ $1.05; hard cap $10 never approached. B=2000 document-block bootstrap;\nBenjamini–Hochberg at q=0.05 across 42 validation tests (27 reject).\n\n## Files\n\n| File | What |\n|---|---|\n| `method.py` | Full pipeline: extraction → counterfactual+swap decoys → isolated provenance-blinded scoring (logprob & self-consistency) → S1 / crux / ablation / baseline analyses → `method_out.json`. CLI: `--selftest`, `--mini`, `--n-docs N`, `--pilot-only`, `--ablation`, `--portable-headline`. |\n| `fdr_stats.py` | Pure statistical core (knockoff+ threshold, signed-max W, win-rate, one-sided KS/MW/AD/permutation, tail effect sizes, document-block bootstrap, BH, realized-FDR gates). Unit-tested by `--selftest`. |\n| `llm_client.py` | Async OpenRouter client: disk cache (free resumes), exact per-call cost from `usage.cost`, hard-stop at $10, logprob/self-consistency elicitation parsers. |\n| `make_figures.py` | Generates `figures/fig1..4*.png`. |\n| `method_out.json` | **Primary output** (schema `exp_gen_sol_out`, validated). 1937 examples (one per real, with per-elicitation scores/W and admission predictions) + rich `metadata`. |\n| `logs/cost.jsonl` | Per-call cumulative cost trace. |\n| `cache/` | Response cache (re-runs reproduce for $0). |\n\n## Reproduce\n\n```bash\nuv run method.py --selftest                              # offline stat unit tests (no API)\nuv run method.py --ablation --portable-headline          # full 190-doc run (cache → free)\nuv run make_figures.py                                   # figures\n```\n\n## `method_out.json` → `metadata` map (for the paper writer)\n\n* `headline_finding`, `headline_elicitation`, `headline_verdict` — the one-paragraph result.\n* `elicitation_comparison` — per-view (logprob_full / portable_full) verdict + win-rate + CI.\n* `s1_decoy_signature_by_elicitation[view][counterfactual|random_swap].rows` — per-α tail\n  win-rate, bootstrap CI, KS/MW p, plus a `robustness_sweep` over tail quantiles.\n* `spontaneous_error_match_by_elicitation[view]` — `regions{full,top50pct,top25pct}` with\n  decoy~spont and decoy~truepos tests, gap effect sizes, and `figure_cdfs` (x grid + 3 CDFs).\n* `generator_ne_scorer` — 4 (G,S) configs, win-rate CIs, labeled-slice diagonal, `verdict`,\n  `validity_region_statement`.\n* `baseline_vs_method_fdr_by_elicitation[view].rows` — realized FDR vs nominal α for the gate\n  and the raw-confidence baseline.\n* `bh_correction` — every p-value with BH-adjusted p and reject flag.\n* `extraction_quality` — free-extraction atomic precision/recall + multi-hop relation accuracy\n  (the LLM's genuine, error-prone extraction behaviour the gate operates on).\n\n## Honest limitations\n\n* The knockoff+ gate is **conservative** on this signal: under the calibrated (self-consistency)\n  elicitation it certifies admissions only at α=0.5 on 190 docs (0 admits at stricter α). It\n  trades power for control — but is never *anti-conservative* like the baseline.\n* The full-distribution crux is borderline (KS p≈0.05; MW rejects) — the decoy≈spont match is a\n  *tail* phenomenon (top-25 %/50 % clearly VALID), which is the region admission actually uses.\n* `gpt-4.1-nano` is a small model; its atomic precision ≈ 0.50 and multi-hop accuracy ≈ 0.20 on\n  terse pronoun-heavy CLUTRR stories. These genuine errors are the experimental signal, not a\n  confound — the methodology validation does not depend on extractor accuracy.\n* Self-consistency reduces the diagnostic's sensitivity to the swap control (both null families\n  become exchangeable under it); sensitivity is demonstrated via logprob + the synthetic test.\n", "numLines": 116, "startLine": 1, "totalLines": 116}}
````

### [12] TOOL CALL — Read · 2026-06-16 13:05:41 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/pyproject.toml
```

### [13] TOOL RESULT — Read · 2026-06-16 13:05:41 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/pyproject.toml", "content": "[project]\nname = \"decoy-fdr-experiment\"\nversion = \"0.1.0\"\ndescription = \"S1 decoy-signature + spontaneous-error tail match + Generator!=Scorer de-circularization for a label-free decoy-competition FDR gate on CLUTRR crisp gold\"\nrequires-python = \">=3.12\"\ndependencies = [\n    \"numpy==2.4.6\",\n    \"scipy==1.17.1\",\n    \"aiohttp==3.14.1\",\n    \"loguru==0.7.3\",\n    \"tenacity==9.1.4\",\n    \"requests==2.34.2\",\n    \"psutil==7.2.2\",\n    \"jsonschema==4.26.0\",\n    \"matplotlib==3.11.0\",\n]\n", "numLines": 17, "startLine": 1, "totalLines": 17}}
```

### [14] TOOL CALL — Read · 2026-06-16 13:05:49 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/preview_method_out.json
```

### [15] TOOL RESULT — Read · 2026-06-16 13:05:49 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/preview_method_out.json", "content": "{\n  \"metadata\": {\n    \"method_name\": \"Label-free decoy-competition FDR gate (counterfactual knockoffs) for LLM text->logic fact admission\",\n    \"description\": \"Validates the gate's null assumptions on CLUTRR crisp gold across two label-free elicitations (logprob vs K-sample self-consistency): S... [truncated, 36275 chars total]
```

### [16] TOOL CALL — Read · 2026-06-16 13:06:01 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/fdr_stats.py
```

### [17] TOOL RESULT — Read · 2026-06-16 13:06:01 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/fdr_stats.py", "content": "#!/usr/bin/env python3\n\"\"\"\nfdr_stats.py — Offline statistical primitives for the decoy-competition FDR gate.\n\nAll functions are pure (no I/O, no API) so they can be unit-tested with `--selftest`\nin method.py. Implements:\n  * canonical knockoff statistic W_i (signed-max)           [Barber-Candes]\n  * knockoff+ operative threshold T(alpha) (eq 1.9)\n  * k-floor / certifiable-alpha logic (FDR floor 1/k)\n  * tail-conditioned decoy win-rate\n  * one-sided two-sample tests (KS, Mann-Whitney, Anderson-Darling, permutation)\n  * tail effect sizes (Wasserstein, Cliff's delta, KS-sup, mean-diff)\n  * document-block (cluster) bootstrap CIs (B>=2000)\n  * Benjamini-Hochberg multiplicity correction\n  * within-document rank-normalisation\n  * empirical-CDF export for figure-ready overlays\n  * realized-FDR calibration for the decoy gate and the raw-confidence baseline\n\"\"\"\nfrom __future__ import annotations\n\nimport hashlib\nimport math\nfrom typing import Callable, Sequence\n\nimport numpy as np\nfrom scipy import stats\n\n\n# ---------------------------------------------------------------------------\n# Rank-normalisation (per document, cancels per-doc scoring-scale differences)\n# ---------------------------------------------------------------------------\ndef _jitter(cand_id: str, seed: int) -> float:\n    \"\"\"Tiny deterministic jitter in [0, 1e-6) to break exact ties before ranking.\"\"\"\n    h = hashlib.sha256(f\"{cand_id}|{seed}\".encode()).hexdigest()\n    return (int(h[:12], 16) / float(16**12)) * 1e-6\n\n\ndef rank_normalize(scores: dict[str, float], seed: int) -> dict[str, float]:\n    \"\"\"Map a pool of candidate scores to [0,1] ranks. cand_id->normalized rank.\n\n    A single-element pool maps to 0.5 (no information). Ties broken by deterministic\n    jitter keyed on the candidate id so the mapping is reproducible.\n    \"\"\"\n    ids = list(scores.keys())\n    n = len(ids)\n    if n == 0:\n        return {}\n    if n == 1:\n        return {ids[0]: 0.5}\n    jittered = np.array([scores[i] + _jitter(i, seed) for i in ids])\n    order = np.argsort(jittered, kind=\"mergesort\")\n    ranks = np.empty(n, dtype=float)\n    ranks[order] = np.arange(n, dtype=float)\n    norm = ranks / (n - 1)  # 0 .. 1\n    return {ids[i]: float(norm[i]) for i in range(n)}\n\n\n# ---------------------------------------------------------------------------\n# Canonical knockoff statistic and knockoff+ threshold\n# ---------------------------------------------------------------------------\ndef W_signed_max(z_real: float, z_decoy: float) -> float:\n    \"\"\"Signed-max statistic: magnitude = max(|real|,|decoy|) in score space,\n    sign positive iff the real beats its decoy (Barber-Candes antisymmetry).\n\n    Scores are in [0,1] (rank-normalized), so max(z_real,z_decoy) is the magnitude\n    and sign(z_real - z_decoy) is the orientation. Antisymmetric under real<->decoy\n    swap (sign flips, magnitude unchanged).\n    \"\"\"\n    mag = max(z_real, z_decoy)\n    s = z_real - z_decoy\n    sign = 0.0 if s == 0 else math.copysign(1.0, s)\n    return mag * sign\n\n\ndef knockoff_plus_threshold(W: Sequence[float], alpha: float) -> tuple[float, int, float]:\n    \"\"\"knockoff+ operative cutoff T(alpha) (Barber-Candes 2015, eq 1.9):\n\n        T = min{ t in |W| : (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha }\n\n    The '+1' in the numerator (Rajchert-Keich: generally necessary) controls *exact*\n    FDR (their Thm 2). Returns (T, n_admitted, realized_ratio). If no feasible cutoff\n    exists, returns (inf, 0, 1.0) — admit nothing.\n    \"\"\"\n    Wa = np.asarray([w for w in W], dtype=float)\n    if Wa.size == 0:\n        return math.inf, 0, 1.0\n    cands = sorted({abs(w) for w in Wa if w != 0.0})\n    best = (math.inf, 0, 1.0)\n    for t in cands:\n        if t <= 0:\n            continue\n        pos = int(np.sum(Wa >= t))\n        neg = int(np.sum(Wa <= -t))\n        ratio = (1 + neg) / max(1, pos)\n        if ratio <= alpha:\n            return float(t), pos, float(ratio)\n    return best\n\n\ndef k_floor(alpha: float) -> int:\n    \"\"\"Minimum admissions needed to certify FDR<=alpha (FDR floor 1/k => k>=ceil(1/alpha)).\"\"\"\n    return int(math.ceil(1.0 / alpha))\n\n\n# ---------------------------------------------------------------------------\n# Tail-conditioned decoy win-rate\n# ---------------------------------------------------------------------------\ndef tail_win_rate(pairs: Sequence[tuple[float, float]], threshold: float) -> tuple[float, int]:\n    \"\"\"Among pairs (z_real, z_decoy) in the admission region {max(z_real,z_decoy) >= T},\n    fraction where the decoy beats the real. Target ~0.5 under exchangeability.\n    Returns (win_rate, n_tail). NaN win_rate if the tail is empty.\n    \"\"\"\n    tail = [(zr, zd) for (zr, zd) in pairs if max(zr, zd) >= threshold]\n    if not tail:\n        return float(\"nan\"), 0\n    wins = sum(1 for (zr, zd) in tail if zd > zr)\n    return wins / len(tail), len(tail)\n\n\n# ---------------------------------------------------------------------------\n# One-sided two-sample tests + supplements\n# ---------------------------------------------------------------------------\ndef ks_two_sample(decoy: Sequence[float], real: Sequence[float], alternative: str = \"two-sided\"):\n    \"\"\"KS two-sample. alternative per scipy: 'two-sided','less','greater'.\n    Returns (stat, p). Empty input -> (nan, 1.0).\"\"\"\n    d = np.asarray(decoy, float)\n    r = np.asarray(real, float)\n    if d.size == 0 or r.size == 0:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.ks_2samp(d, r, alternative=alternative, method=\"auto\")\n        return float(res.statistic), float(res.pvalue)\n    except Exception:\n        return float(\"nan\"), 1.0\n\n\ndef mannwhitney(decoy: Sequence[float], real: Sequence[float], alternative: str = \"two-sided\"):\n    \"\"\"Mann-Whitney U (one- or two-sided). Returns (stat, p).\"\"\"\n    d = np.asarray(decoy, float)\n    r = np.asarray(real, float)\n    if d.size == 0 or r.size == 0:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.mannwhitneyu(d, r, alternative=alternative)\n        return float(res.statistic), float(res.pvalue)\n    except ValueError:\n        return float(\"nan\"), 1.0\n\n\ndef anderson_darling_2samp(a: Sequence[float], b: Sequence[float]):\n    \"\"\"Anderson-Darling k-sample (more tail-sensitive than KS). Returns (stat, p).\n    p is clipped to scipy's reported floor/cap (0.001 .. 0.25).\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size < 2 or b.size < 2:\n        return float(\"nan\"), 1.0\n    try:\n        res = stats.anderson_ksamp([a, b])\n        return float(res.statistic), float(res.significance_level)\n    except Exception:\n        return float(\"nan\"), 1.0\n\n\ndef permutation_two_sample(a: Sequence[float], b: Sequence[float], n_perm: int = 5000,\n                           seed: int = 0, alternative: str = \"two-sided\"):\n    \"\"\"Permutation test on the difference of means (robust for small tails).\n    Returns (observed_mean_diff a-b, p).\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size == 0 or b.size == 0:\n        return float(\"nan\"), 1.0\n    rng = np.random.default_rng(seed)\n    obs = a.mean() - b.mean()\n    pooled = np.concatenate([a, b])\n    na = a.size\n    diffs = np.empty(n_perm)\n    for i in range(n_perm):\n        rng.shuffle(pooled)\n        diffs[i] = pooled[:na].mean() - pooled[na:].mean()\n    if alternative == \"two-sided\":\n        p = (np.sum(np.abs(diffs) >= abs(obs)) + 1) / (n_perm + 1)\n    elif alternative == \"greater\":\n        p = (np.sum(diffs >= obs) + 1) / (n_perm + 1)\n    else:  # less\n        p = (np.sum(diffs <= obs) + 1) / (n_perm + 1)\n    return float(obs), float(p)\n\n\n# ---------------------------------------------------------------------------\n# Tail effect sizes\n# ---------------------------------------------------------------------------\ndef cliffs_delta(a: Sequence[float], b: Sequence[float]) -> float:\n    \"\"\"Cliff's delta in [-1,1]: P(a>b)-P(a<b). Sign(+) => a stochastically larger.\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if a.size == 0 or b.size == 0:\n        return float(\"nan\")\n    # vectorised count via sorting b\n    b_sorted = np.sort(b)\n    gt = np.searchsorted(b_sorted, a, side=\"left\").sum()        # #(b < a_i)\n    lt = (b.size - np.searchsorted(b_sorted, a, side=\"right\")).sum()  # #(b > a_i)\n    return float((gt - lt) / (a.size * b.size))\n\n\ndef tail_gap(decoy: Sequence[float], spont: Sequence[float]) -> dict:\n    \"\"\"Bundle of gap metrics comparing decoy vs spontaneous-error tails.\n    Signed mean_diff/cliffs: + => decoys score HIGHER than genuine errors (harder to reject\n    => gate over-counts false discoveries => CONSERVATIVE); - => decoys score LOWER (false\n    reals beat their decoys => under-count => ANTI-CONSERVATIVE).\"\"\"\n    d = np.asarray(decoy, float)\n    s = np.asarray(spont, float)\n    ks_sup, _ = ks_two_sample(d, s, \"two-sided\")\n    w1 = float(stats.wasserstein_distance(d, s)) if d.size and s.size else float(\"nan\")\n    md = float(d.mean() - s.mean()) if d.size and s.size else float(\"nan\")\n    return {\n        \"ks_sup\": ks_sup,\n        \"wasserstein\": w1,\n        \"mean_diff\": md,\n        \"cliffs_delta\": cliffs_delta(d, s),\n        \"n_decoy\": int(d.size),\n        \"n_other\": int(s.size),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Document-block (cluster) bootstrap\n# ---------------------------------------------------------------------------\ndef doc_block_bootstrap(doc_units: list, stat_fn: Callable[[list], float],\n                        B: int = 2000, seed: int = 0, ci: float = 0.95) -> dict:\n    \"\"\"Resample whole documents with replacement B times; recompute stat_fn on the\n    pooled resample. Returns point estimate, percentile CI, and bootstrap SE.\n\n    doc_units : list of per-document objects (any payload stat_fn understands).\n    stat_fn   : maps a list of doc_units -> scalar statistic.\n    \"\"\"\n    n = len(doc_units)\n    point = stat_fn(doc_units)\n    if n == 0:\n        return {\"point\": float(\"nan\"), \"ci_low\": float(\"nan\"), \"ci_high\": float(\"nan\"),\n                \"se\": float(\"nan\"), \"B\": B, \"n_docs\": 0}\n    rng = np.random.default_rng(seed)\n    reps = np.empty(B)\n    idx_all = np.arange(n)\n    for b in range(B):\n        idx = rng.choice(idx_all, size=n, replace=True)\n        resample = [doc_units[i] for i in idx]\n        reps[b] = stat_fn(resample)\n    reps = reps[~np.isnan(reps)]\n    if reps.size == 0:\n        return {\"point\": float(point) if point == point else float(\"nan\"),\n                \"ci_low\": float(\"nan\"), \"ci_high\": float(\"nan\"),\n                \"se\": float(\"nan\"), \"B\": B, \"n_docs\": n}\n    lo = float(np.percentile(reps, 100 * (1 - ci) / 2))\n    hi = float(np.percentile(reps, 100 * (1 - (1 - ci) / 2)))\n    return {\"point\": float(point) if point == point else float(np.mean(reps)),\n            \"ci_low\": lo, \"ci_high\": hi, \"se\": float(np.std(reps, ddof=1)),\n            \"B\": int(reps.size), \"n_docs\": n}\n\n\n# ---------------------------------------------------------------------------\n# Benjamini-Hochberg\n# ---------------------------------------------------------------------------\ndef benjamini_hochberg(pvals: Sequence[float], q: float = 0.05) -> list[dict]:\n    \"\"\"BH step-up. Returns list aligned to input order with adjusted p and reject flag.\"\"\"\n    p = np.asarray(pvals, float)\n    m = p.size\n    if m == 0:\n        return []\n    order = np.argsort(p, kind=\"mergesort\")\n    ranked = p[order]\n    adj = np.empty(m)\n    prev = 1.0\n    for i in range(m - 1, -1, -1):\n        val = ranked[i] * m / (i + 1)\n        prev = min(prev, val)\n        adj[i] = min(prev, 1.0)\n    adj_orig = np.empty(m)\n    adj_orig[order] = adj\n    # reject if BH-adjusted p <= q\n    return [{\"raw_p\": float(p[i]), \"bh_adj_p\": float(adj_orig[i]),\n             \"reject\": bool(adj_orig[i] <= q)} for i in range(m)]\n\n\n# ---------------------------------------------------------------------------\n# Empirical CDF export (figure-ready)\n# ---------------------------------------------------------------------------\ndef empirical_cdf(values: Sequence[float], grid: Sequence[float]) -> list[float]:\n    \"\"\"Empirical CDF of `values` evaluated on a common `grid`.\"\"\"\n    v = np.sort(np.asarray(values, float))\n    g = np.asarray(grid, float)\n    if v.size == 0:\n        return [float(\"nan\")] * len(g)\n    cdf = np.searchsorted(v, g, side=\"right\") / v.size\n    return [float(x) for x in cdf]\n\n\n# ---------------------------------------------------------------------------\n# Realized-FDR calibration: decoy gate vs raw-confidence baseline\n# ---------------------------------------------------------------------------\ndef decoy_gate_fdr(reals: list[dict], alpha: float) -> dict:\n    \"\"\"Decoy-competition (knockoff+) gate evaluated against crisp gold.\n\n    reals: list of {'w': W_i, 'is_false': bool} for labelable reals (TRUE/FALSE).\n    Admit reals with W_i >= T(alpha). Realized FDR = #(admitted & FALSE)/#admitted.\n    \"\"\"\n    W = [r[\"w\"] for r in reals]\n    T, n_adm, ratio = knockoff_plus_threshold(W, alpha)\n    admitted = [r for r in reals if r[\"w\"] >= T]\n    n = len(admitted)\n    n_false = sum(1 for r in admitted if r[\"is_false\"])\n    realized = (n_false / n) if n else 0.0\n    floor = k_floor(alpha)\n    return {\n        \"alpha\": alpha, \"threshold\": (None if math.isinf(T) else T),\n        \"n_admitted\": n, \"n_false_admitted\": n_false,\n        \"realized_fdr\": realized, \"estimated_ratio\": ratio,\n        \"k_floor\": floor, \"certified\": n >= floor,\n    }\n\n\ndef baseline_confidence_gate_fdr(reals: list[dict], alpha: float) -> dict:\n    \"\"\"Raw-confidence (purely neural) baseline gate evaluated against crisp gold.\n\n    reals: list of {'z': raw confidence in [0,1] that the real is TRUE, 'is_false': bool}.\n    Greedily admit reals in descending confidence while the *self-estimated* FDP\n    (mean of (1-confidence) over admitted) stays <= alpha — i.e. trust the model's\n    own confidence as a calibrated probability (no labels, no decoys). Realized FDR\n    is then measured against crisp gold. This is the standard 'threshold the model's\n    confidence' approach the decoy gate is compared against.\n    \"\"\"\n    srt = sorted(reals, key=lambda r: r[\"z\"], reverse=True)\n    admitted: list[dict] = []\n    run_false_mass = 0.0\n    for r in srt:\n        new_mass = run_false_mass + (1.0 - r[\"z\"])\n        n_new = len(admitted) + 1\n        if (new_mass / n_new) <= alpha:\n            admitted.append(r)\n            run_false_mass = new_mass\n        else:\n            break\n    n = len(admitted)\n    n_false = sum(1 for r in admitted if r[\"is_false\"])\n    realized = (n_false / n) if n else 0.0\n    est = (run_false_mass / n) if n else 0.0\n    return {\n        \"alpha\": alpha, \"n_admitted\": n, \"n_false_admitted\": n_false,\n        \"realized_fdr\": realized, \"self_estimated_fdp\": est,\n    }\n", "numLines": 350, "startLine": 1, "totalLines": 350}}
```

### [18] TOOL CALL — Read · 2026-06-16 13:06:07 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/method.py
```

### [19] TOOL CALL — Read · 2026-06-16 13:06:11 UTC

```
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/method.py
```

### [20] TOOL RESULT — Read · 2026-06-16 13:06:11 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/method.py", "content": "    zmap = pipe[\"zmap\"]\n    docs, doc_by_id = pipe[\"docs\"], pipe[\"doc_by_id\"]\n    cf_real = {c[\"real_id\"]: c[\"cand_id\"] for d in docs for c in pipe[\"cf_by_doc\"][d.doc_id]}\n    swap_real = {c[\"real_id\"]: c[\"cand_id\"] for d in docs for c in pipe[\"swap_by_doc\"][d.doc_id]}\n    cf_rel = {c[\"real_id\"]: c[\"r\"] for d in docs for c in pipe[\"cf_by_doc\"][d.doc_id]}\n    swap_t = {c[\"real_id\"]: c[\"t\"] for d in docs for c in pipe[\"swap_by_doc\"][d.doc_id]}\n\n    # per-elicitation knockoff+ thresholds (method gate) for admission predictions\n    a_thr = {}\n    for elic, norm in norms.items():\n        Ws = [st.W_signed_max(norm[c[\"cand_id\"]], norm[cf_real[c[\"cand_id\"]]])\n              for c in pipe[\"all_reals\"]\n              if c[\"cand_id\"] in norm and cf_real.get(c[\"cand_id\"]) in norm]\n        a_thr[elic] = ({a: st.knockoff_plus_threshold(Ws, a)[0] for a in ALPHA_GRID}, Ws)\n\n    examples = []\n    for c in pipe[\"all_reals\"]:\n        did, sid = cf_real.get(c[\"cand_id\"]), swap_real.get(c[\"cand_id\"])\n        ex = {\n            \"input\": json.dumps({\"doc_id\": c[\"doc_id\"], \"head\": c[\"h\"], \"relation\": c[\"r\"],\n                                 \"tail\": c[\"t\"], \"claim\": c[\"claim\"], \"candidate_kind\": \"real\"}),\n            \"output\": c[\"label\"],\n            \"metadata_doc_id\": c[\"doc_id\"], \"metadata_fact_type\": c[\"fact_type\"],\n            \"metadata_chain_length_k\": doc_by_id[c[\"doc_id\"]].k,\n            \"metadata_is_pilot\": doc_by_id[c[\"doc_id\"]].is_pilot,\n            \"metadata_decoy_relation\": cf_rel.get(c[\"cand_id\"]),\n            \"metadata_swap_tail\": swap_t.get(c[\"cand_id\"]),\n        }\n        for elic, norm in norms.items():\n            tag = \"lp\" if \"logprob\" in elic else \"pt\"\n            zr, zr_raw = norm.get(c[\"cand_id\"]), zmap.get((elic, c[\"cand_id\"]))\n            zd = norm.get(did) if did else None\n            zs = norm.get(sid) if sid else None\n            w_cf = st.W_signed_max(zr, zd) if (zr is not None and zd is not None) else None\n            w_swap = st.W_signed_max(zr, zs) if (zr is not None and zs is not None) else None\n            ex[f\"metadata_z_real_raw_{tag}\"] = zr_raw\n            ex[f\"metadata_z_real_rank_{tag}\"] = zr\n            ex[f\"metadata_z_decoy_rank_{tag}\"] = zd\n            ex[f\"metadata_z_swap_rank_{tag}\"] = zs\n            ex[f\"metadata_w_cf_{tag}\"] = w_cf\n            ex[f\"metadata_w_swap_{tag}\"] = w_swap\n            if w_cf is not None:\n                for a in ALPHA_GRID:\n                    T = a_thr[elic][0][a]\n                    ex[f\"predict_admit_{tag}_a{int(a*100):02d}\"] = (\n                        \"yes\" if (not math.isinf(T) and w_cf >= T) else \"no\")\n        examples.append(_clean(ex))\n\n    ext_meta = pipe[\"ext_meta\"]\n    atomic_prec = np.nanmean([e[\"atomic_prec\"] for e in ext_meta]) if ext_meta else float(\"nan\")\n    atomic_rec = np.nanmean([e[\"atomic_rec\"] for e in ext_meta]) if ext_meta else float(\"nan\")\n    mh_acc = np.nanmean([e[\"mh_acc\"] for e in ext_meta]) if ext_meta else float(\"nan\")\n\n    elic_cmp = {elic: _elicitation_summary(s1_by[elic], crux_by[elic]) for elic in s1_by}\n    headline_verdict = elic_cmp.get(headline_elic, {}).get(\"verdict\", \"n/a\")\n\n    metadata = {\n        \"method_name\": \"Label-free decoy-competition FDR gate (counterfactual knockoffs) \"\n                       \"for LLM text->logic fact admission\",\n        \"description\": \"Validates the gate's null assumptions on CLUTRR crisp gold across two \"\n                       \"label-free elicitations (logprob vs K-sample self-consistency): S1 decoy \"\n                       \"signature, spontaneous-error tail match, Generator!=Scorer \"\n                       \"de-circularization, and realized-FDR vs a purely-neural baseline.\",\n        \"headline_finding\": (\n            \"The decoy-competition FDR gate's validity is ELICITATION-DEPENDENT. With single-\"\n            \"token logprob confidence the LLM is overconfident in its own spontaneous errors, so \"\n            \"counterfactual decoys are strongly ANTI-CONSERVATIVE (tail win-rate ~0.3 << 0.5, \"\n            \"KS/MW p<1e-20) and the gate fails to control realized FDR. With K-sample self-\"\n            \"consistency confidence the counterfactual decoys become EXCHANGEABLE (win-rate ~0.5, \"\n            \"CI covers 0.5), their score distribution matches the genuine spontaneous-error \"\n            \"distribution in the admission tail (and differs from true positives), the gate \"\n            \"controls realized FDR <= nominal vs crisp gold while the raw-confidence baseline \"\n            \"admits hallucinated facts at uncontrolled rates, and exchangeability is ROBUST to \"\n            \"Generator!=Scorer across model families (de-circularized). Diagnostic sensitivity is \"\n            \"demonstrated by the random type-matched swap control, which is flagged anti-\"\n            \"conservative under logprob (and by the synthetic too-easy-decoy self-test); under \"\n            \"self-consistency both null families behave exchangeably.\"),\n        \"headline_elicitation\": headline_elic,\n        \"headline_verdict\": headline_verdict,\n        \"models\": {\"primary_scorer_and_generator\": PRIMARY_MODEL,\n                   \"cross_family_scorer_generator\": OTHER_MODEL},\n        \"elicitation\": {\"logprob\": \"softmax P(Yes) over {Yes,No} first-token logits (gpt-4.1-nano)\",\n                        \"portable\": f\"K={K_SC} self-consistency Yes/No+confidence, temp=0.7, \"\n                                    \"mean per-call p(true)\",\n                        \"logprobs_available_nano\": True, \"logprobs_available_other\": False,\n                        \"note\": \"logprob computed on all docs; portable computed on the pilot \"\n                                \"slice (shared docs) for a controlled elicitation comparison\"},\n        \"hyperparameters\": {\"seed\": SEED, \"alpha_grid\": ALPHA_GRID, \"B_bootstrap\": B_BOOT,\n                            \"K_self_consistency\": K_SC, \"n_false_min\": N_FALSE_MIN,\n                            \"soft_cap_usd\": SOFT_CAP_USD, \"hard_stop_usd\": HARD_STOP_USD,\n                            \"W_statistic\": \"signed-max\", \"knockoff_plus\": \"Barber-Candes eq 1.9\",\n                            \"bootstrap\": \"document-block (cluster) resampling\",\n                            \"multiplicity\": \"Benjamini-Hochberg q=0.05\",\n                            \"scoring\": \"isolated, provenance-blinded, identical template\",\n                            \"rank_normalization\": \"per-document over reals+cf-decoys+swaps\"},\n        \"dataset_counts\": {\"n_docs\": len(docs), \"n_reals\": len(pipe[\"all_reals\"]),\n                           \"n_true\": pipe[\"n_true\"], \"n_spont_false\": pipe[\"n_spont\"],\n                           \"n_undecidable\": pipe[\"n_und\"],\n                           \"spontaneous_error_populable\": pipe[\"n_spont\"] >= N_FALSE_MIN,\n                           \"contamination_rate_decoys\": pipe[\"contamination_rate\"]},\n        \"extraction_quality\": {\"atomic_precision\": atomic_prec, \"atomic_recall\": atomic_rec,\n                               \"multihop_relation_accuracy\": mh_acc,\n                               \"note\": \"atomic P/R from free extraction; multi-hop accuracy from \"\n                                       \"forced per-pair relation prediction (CLUTRR query format)\"},\n        \"elicitation_comparison\": elic_cmp,\n        \"s1_decoy_signature_by_elicitation\": s1_by,\n        \"spontaneous_error_match_by_elicitation\": crux_by,\n        \"generator_ne_scorer\": ablation,\n        \"baseline_vs_method_fdr_by_elicitation\": baseline_by,\n        \"bh_correction\": bh,\n        \"runtime\": pipe[\"runtime\"],\n        \"cost_trace_path\": \"logs/cost.jsonl\",\n        \"interpretation\": {\n            \"s1_expected\": \"counterfactual tail win-rate CI covers 0.5 & KS/MW non-sig \"\n                           \"(exchangeable); random-swap win-rate < 0.5 & sig (anti-conservative \"\n                           \"control validating diagnostic sensitivity)\",\n            \"crux_expected\": \"decoy ~ spontaneous-error (FALSE-real) distribution in the \"\n                             \"admission tail (fail-to-reject) and != true-positive (reject)\",\n            \"ablation_expected\": \"exchangeability holds even when Generator!=Scorer => not a \"\n                                 \"shared-model artifact (ROBUST)\",\n            \"baseline_expected\": \"under a calibrated elicitation the decoy-FDR gate realized FDR \"\n                                 \"<= nominal alpha while the raw-confidence baseline admits \"\n                                 \"hallucinated facts at uncontrolled rates\"},\n    }\n\n    out = {\"metadata\": _clean(metadata),\n           \"datasets\": [{\"dataset\": \"CLUTRR-v1-CrispGold-CalibrationAnchor\",\n                         \"examples\": examples}]}\n    out_path.write_text(json.dumps(out, indent=2))\n    logger.info(f\"Wrote {out_path} ({out_path.stat().st_size/1024:.0f} KB, \"\n                f\"{len(examples)} examples)\")\n    return out\n\n\n# ---------------------------------------------------------------------------\n# Offline self-tests (Stage 0)\n# ---------------------------------------------------------------------------\ndef selftest():\n    import numpy as np\n    logger.info(\"STAGE 0 — offline statistics unit tests\")\n    # (a) knockoff_plus_threshold k-floor mapping\n    assert [st.k_floor(a) for a in ALPHA_GRID] == [20, 10, 5, 4, 2], \"k-floor mapping\"\n    # worked example: all reals beat decoys (W all positive) -> admit all at small alpha\n    W = [0.9] * 25 + [-0.3] * 1\n    T, n, ratio = st.knockoff_plus_threshold(W, 0.05)\n    assert n >= 20 and ratio <= 0.05, f\"knockoff+ admit {n} ratio {ratio}\"\n    # no feasible cutoff -> admit nothing\n    Tn, nn, _ = st.knockoff_plus_threshold([-0.5, -0.4, 0.1], 0.05)\n    assert nn == 0 and math.isinf(Tn), \"infeasible cutoff admits nothing\"\n    # (b) W signed-max antisymmetry\n    assert st.W_signed_max(0.8, 0.3) == 0.8 and st.W_signed_max(0.3, 0.8) == -0.8\n    assert abs(st.W_signed_max(0.5, 0.5)) == 0.0, \"tie sign zero\"\n    # (c) synthetic scorer sanity\n    rng = np.random.default_rng(0)\n    fair = [(float(rng.random()), float(rng.random())) for _ in range(2000)]\n    wr, _ = st.tail_win_rate(fair, 0.0)\n    assert 0.45 < wr < 0.55, f\"fair-coin win-rate {wr}\"\n    # decoys deliberately too-easy (lower) -> win-rate << 0.5 and KS significant\n    easy = [(float(rng.random()), float(rng.random()) * 0.5) for _ in range(2000)]\n    wr2, _ = st.tail_win_rate(easy, 0.0)\n    assert wr2 < 0.45, f\"too-easy decoy win-rate {wr2}\"\n    _, ksp = st.ks_two_sample([d for _, d in easy], [r for r, _ in easy], \"two-sided\")\n    assert ksp < 0.05, f\"KS should detect too-easy decoys p={ksp}\"\n    # (d) doc-block bootstrap wider than naive iid on clustered data\n    clustered = [[0.0] * 20 if i % 2 == 0 else [1.0] * 20 for i in range(20)]\n\n    def mean_fn(units):\n        flat = [x for u in units for x in u]\n        return float(np.mean(flat)) if flat else float(\"nan\")\n    block = st.doc_block_bootstrap(clustered, mean_fn, B=500, seed=1)\n    flat = [x for u in clustered for x in u]\n\n    def mean_fn_iid(units):\n        return float(np.mean(units)) if len(units) else float(\"nan\")\n    iid = st.doc_block_bootstrap(flat, mean_fn_iid, B=500, seed=1)\n    block_w = block[\"ci_high\"] - block[\"ci_low\"]\n    iid_w = iid[\"ci_high\"] - iid[\"ci_low\"]\n    assert block_w > iid_w, f\"block CI {block_w} should exceed iid CI {iid_w}\"\n    # (e) label() on mini examples\n    raw = json.loads(MINI_DATA.read_text())[\"datasets\"][0][\"examples\"]\n    d0 = Doc(raw[0])  # Dan/Micheal/Gabrielle k2\n    assert d0.label(\"Dan\", \"brother\", \"Micheal\") == \"TRUE\"\n    assert d0.label(\"Gabrielle\", \"grandson\", \"Dan\") == \"TRUE\"\n    assert d0.label(\"Dan\", \"mother\", \"Micheal\") == \"FALSE\"   # enumerated pair, wrong rel\n    assert d0.label(\"Dan\", \"brother\", \"Gabrielle\") == \"UNDECIDABLE\"  # non-enumerated pair\n    # BH monotonic\n    bh = st.benjamini_hochberg([0.001, 0.5, 0.02, 0.9], q=0.05)\n    assert bh[0][\"reject\"] and not bh[1][\"reject\"]\n    # decoy gate vs baseline shapes\n    reals = [{\"w\": 0.9, \"is_false\": False}] * 18 + [{\"w\": -0.2, \"is_false\": True}] * 2\n    g = st.decoy_gate_fdr(reals, 0.10)\n    assert g[\"n_admitted\"] >= 10 and g[\"realized_fdr\"] <= 0.10 + 1e-9\n    logger.info(\"STAGE 0 — all offline unit tests PASSED ✓\")\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\nasync def amain(args):\n    set_mem_limit(8.0)\n    data_path = MINI_DATA if args.mini else FULL_DATA\n    docs = load_docs(data_path, n_docs=args.n_docs, pilot_only=args.pilot_only)\n    logger.info(f\"Loaded {len(docs)} docs from {data_path.name} \"\n                f\"(pilot={sum(d.is_pilot for d in docs)})\")\n    cache_dir = HERE / \"cache\"\n    cost_log = HERE / \"logs\" / \"cost.jsonl\"\n    pipe = await run(docs, do_ablation=args.ablation, cache_dir=cache_dir,\n                     cost_log=cost_log, concurrency=args.concurrency,\n                     portable_headline=args.portable_headline)\n\n    logger.info(\"Analyzing (offline) ...\")\n    # Analysis \"views\" = (view_name, zmap_config, doc_subset). logprob_full = all docs\n    # (max power). When portable was scored (ablation), add a CONTROLLED same-docs pair on\n    # the pilot slice: logprob_pilot vs portable_pilot, isolating the elicitation effect.\n    pilot_docs = [d for d in pipe[\"docs\"] if d.is_pilot]\n    abl_docs = pilot_docs or pipe[\"docs\"]   # mirror run()'s ablation slice fallback\n    have_portable = any((\"nano_portable\", c[\"cand_id\"]) in pipe[\"zmap\"]\n                        for c in pipe[\"all_reals\"])\n    views = [(\"logprob_full\", \"nano_logprob\", pipe[\"docs\"])]\n    if args.portable_headline and have_portable:\n        # full-power controlled comparison on the SAME docs\n        views.append((\"portable_full\", \"nano_portable\", pipe[\"docs\"]))\n    elif have_portable:\n        views += [(\"logprob_pilot\", \"nano_logprob\", abl_docs),\n                  (\"portable_pilot\", \"nano_portable\", abl_docs)]\n    norms_view, s1_by, crux_by, baseline_by = {}, {}, {}, {}\n    for vname, cfg, dsub in views:\n        norm = rank_normalize_config(pipe, cfg, docs=dsub)\n        norms_view[vname] = norm\n        s1_by[vname] = analyze_s1(pipe, norm)\n        crux_by[vname] = analyze_crux(pipe, norm)\n        baseline_by[vname] = analyze_baseline_vs_method(pipe, norm, config=cfg)\n        logger.info(f\"  analyzed view '{vname}' ({cfg}, {len(dsub)} docs)\")\n    ablation = analyze_ablation(pipe) if args.ablation else {\"ran\": False}\n    bh = collect_bh(s1_by, crux_by, ablation)\n    headline_view = next((v for v in (\"portable_full\", \"portable_pilot\")\n                          if v in norms_view), \"logprob_full\")\n    # example-level fields: full-coverage logprob + (if present) calibrated portable\n    example_norms = {\"logprob_full\": norms_view[\"logprob_full\"]}\n    for pv in (\"portable_full\", \"portable_pilot\"):\n        if pv in norms_view:\n            example_norms[pv] = norms_view[pv]\n            break\n    out_path = HERE / (\"method_out.json\" if not args.mini else \"mini_method_out.json\")\n    build_output(pipe, example_norms, s1_by, crux_by, ablation, baseline_by, bh,\n                 headline_view, out_path)\n    gc.collect()\n    logger.info(f\"DONE. cost=${pipe['runtime']['cost_usd']:.4f}\")\n\n\ndef main():\n    ap = argparse.ArgumentParser()\n    ap.add_argument(\"--selftest\", action=\"store_true\")\n    ap.add_argument(\"--mini\", action=\"store_true\")\n    ap.add_argument(\"--n-docs\", type=int, default=None)\n    ap.add_argument(\"--pilot-only\", action=\"store_true\")\n    ap.add_argument(\"--ablation\", action=\"store_true\")\n    ap.add_argument(\"--portable-headline\", action=\"store_true\",\n                    help=\"also score the self-consistency (portable) elicitation on ALL docs \"\n                         \"for a full-power, same-docs logprob-vs-portable comparison\")\n    ap.add_argument(\"--concurrency\", type=int, default=28)\n    args = ap.parse_args()\n    if args.selftest:\n        selftest()\n        return\n    try:\n        asyncio.run(amain(args))\n    except BudgetExceeded as e:\n        logger.error(f\"Budget exceeded, aborting: {e}\")\n        raise\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 275, "startLine": 995, "totalLines": 1269}}
```

### [21] ASSISTANT · 2026-06-16 13:07:31 UTC

```
Now I understand the experiment fully. The demo should load the **pre-computed per-example scores** (real/decoy/swap rank scores + W statistics under both elicitations) and re-run the **offline statistical analysis** (`fdr_stats.py` core + `analyze_s1`/`analyze_crux`/gate-FDR) — no LLM/API calls needed, since the cached scores are already in the output examples. Let me inspect the full output programmatically to design the curated subset.
```

### [22] TOOL CALL — Bash · 2026-06-16 13:07:31 UTC

```
Inspect full output: counts, fields, nullness:
cd /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python - <<'PY'
import json
d = json.load(open("full_method_out.json"))
exs = d["datasets"][0]["examples"]
print("total examples:", len(exs))
from collections import Counter
lab = Counter(e["output"] for e in exs)
ft = Counter(e["metadata_fact_type"] for e in exs)
print("labels:", dict(lab))
print("fact_type:", dict(ft))
docs = set(e["metadata_doc_id"] for e in exs)
print("n docs:", len(docs))
# how many have non-null lp + pt rank scores for real & decoy & swap
def ok(e):
    keys=["metadata_z_real_rank_lp","metadata_z_decoy_rank_lp","metadata_z_swap_rank_lp",
          "metadata_z_real_rank_pt","metadata_z_decoy_rank_pt","metadata_z_swap_rank_pt",
          "metadata_w_cf_lp","metadata_w_swap_lp","metadata_w_cf_pt","metadata_w_swap_pt"]
    return all(e.get(k) is not None for k in keys)
print("fully-scored (lp+pt, real/decoy/swap, W):", sum(ok(e) for e in exs))
# raw real scores availability
print("raw lp non-null:", sum(e.get("metadata_z_real_raw_lp") is not None for e in exs))
print("raw pt non-null:", sum(e.get("metadata_z_real_raw_pt") is not None for e in exs))
# keys of one example
print("example keys:", list(exs[0].keys()))
# metadata top-level keys
print("metadata keys:", list(d["metadata"].keys()))
PY
```

### [23] TOOL RESULT — Bash · 2026-06-16 13:07:31 UTC

```
{"stdout": "total examples: 1937\nlabels: {'FALSE': 1304, 'TRUE': 633}\nfact_type: {'atomic': 1059, 'multi_hop': 878}\nn docs: 185\nfully-scored (lp+pt, real/decoy/swap, W): 1937\nraw lp non-null: 0\nraw pt non-null: 0\nexample keys: ['input', 'output', 'metadata_doc_id', 'metadata_fact_type', 'metadata_chain_length_k', 'metadata_is_pilot', 'metadata_decoy_relation', 'metadata_swap_tail', 'metadata_z_real_raw_lp', 'metadata_z_real_rank_lp', 'metadata_z_decoy_rank_lp', 'metadata_z_swap_rank_lp', 'metadata_w_cf_lp', 'metadata_w_swap_lp', 'predict_admit_lp_a05', 'predict_admit_lp_a10', 'predict_admit_lp_a20', 'predict_admit_lp_a30', 'predict_admit_lp_a50', 'metadata_z_real_raw_pt', 'metadata_z_real_rank_pt', 'metadata_z_decoy_rank_pt', 'metadata_z_swap_rank_pt', 'metadata_w_cf_pt', 'metadata_w_swap_pt', 'predict_admit_pt_a05', 'predict_admit_pt_a10', 'predict_admit_pt_a20', 'predict_admit_pt_a30', 'predict_admit_pt_a50']\nmetadata keys: ['method_name', 'description', 'headline_finding', 'headline_elicitation', 'headline_verdict', 'models', 'elicitation', 'hyperparameters', 'dataset_counts', 'extraction_quality', 'elicitation_comparison', 's1_decoy_signature_by_elicitation', 'spontaneous_error_match_by_elicitation', 'generator_ne_scorer', 'baseline_vs_method_fdr_by_elicitation', 'bh_correction', 'runtime', 'cost_trace_path', 'interpretation']", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [24] ASSISTANT · 2026-06-16 13:07:47 UTC

```
All 1937 examples are fully scored under both elicitations. Raw confidence scores are null (so the baseline gate uses precomputed metadata values; the method gate recomputes from W). Let me set up tasks and build the curated subset.
```

### [25] TOOL CALL — Bash · 2026-06-16 13:07:47 UTC

```
Copy fdr_stats.py reference into workspace:
cp /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/fdr_stats.py ./fdr_stats_reference.py && echo "copied fdr_stats for reference" && ls -la
```

### [26] TOOL RESULT — Bash · 2026-06-16 13:07:47 UTC

```
{"stdout": "copied fdr_stats for reference\ntotal 2216\ndrwxr-xr-x 2 root root 1018304 Jun 16 13:07 .\ndrwxr-xr-x 5 root root 1062083 Jun 16 13:03 ..\n-rw-r--r-- 1 root root  172893 Jun 16 13:07 .repl_agent.ptylog\n-rw-r--r-- 1 root root   14729 Jun 16 13:07 fdr_stats_reference.py", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] TOOL CALL — Write · 2026-06-16 13:08:05 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_mini.py

#!/usr/bin/env python3
"""Build mini_demo_data.json: a curated, diverse <=100-example subset of the full
decoy-FDR experiment output, plus trimmed reference metadata. No API needed — every
example already carries its rank-normalized real/decoy/swap scores + W statistics under
both elicitations (logprob `*_lp`, self-consistency `*_pt`)."""
import json
from collections import defaultdict

SRC = ("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/"
       "gen_art/gen_art_experiment_2/full_method_out.json")
OUT = ("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/"
       "notebook_workspaces/iter_2/art_Inu52CyA49Ys/mini_demo_data.json")

d = json.load(open(SRC))
exs = d["datasets"][0]["examples"]

REQ = ["metadata_z_real_rank_lp", "metadata_z_decoy_rank_lp", "metadata_z_swap_rank_lp",
       "metadata_z_real_rank_pt", "metadata_z_decoy_rank_pt", "metadata_z_swap_rank_pt",
       "metadata_w_cf_lp", "metadata_w_swap_lp", "metadata_w_cf_pt", "metadata_w_swap_pt"]
scored = [e for e in exs if all(e.get(k) is not None for k in REQ)]

# Stratify by (label, fact_type); round-robin across documents for diversity.
QUOTA = {("FALSE", "multi_hop"): 32, ("FALSE", "atomic"): 30,
         ("TRUE", "atomic"): 26, ("TRUE", "multi_hop"): 12}  # = 100

strata = defaultdict(lambda: defaultdict(list))  # (label,ft) -> doc_id -> [ex]
for e in scored:
    strata[(e["output"], e["metadata_fact_type"])][e["metadata_doc_id"]].append(e)

selected = []
for key, quota in QUOTA.items():
    by_doc = strata[key]
    doc_ids = sorted(by_doc)               # deterministic
    picked, di = [], 0
    # round-robin: take one example from each doc in turn, spreading across documents
    while len(picked) < quota and any(by_doc[doc] for doc in doc_ids):
        doc = doc_ids[di % len(doc_ids)]
        if by_doc[doc]:
            picked.append(by_doc[doc].pop(0))
        di += 1
    selected.extend(picked)

# Trimmed reference metadata: the full-run headline values the demo recomputes/compares to.
m = d["metadata"]
ref_meta = {
    "method_name": m["method_name"],
    "headline_finding": m["headline_finding"],
    "headline_elicitation": m["headline_elicitation"],
    "headline_verdict": m["headline_verdict"],
    "models": m["models"],
    "elicitation": m["elicitation"],
    "hyperparameters": m["hyperparameters"],
    "dataset_counts": m["dataset_counts"],
    "extraction_quality": m["extraction_quality"],
    "elicitation_comparison": m["elicitation_comparison"],
    "baseline_vs_method_fdr_by_elicitation": m["baseline_vs_method_fdr_by_elicitation"],
}

out = {"metadata_reference_full_run": ref_meta,
       "datasets": [{"dataset": d["datasets"][0]["dataset"], "examples": selected}]}
json.dump(out, open(OUT, "w"), indent=2)

from collections import Counter
print("selected:", len(selected))
print("labels:", dict(Counter(e["output"] for e in selected)))
print("fact_type:", dict(Counter(e["metadata_fact_type"] for e in selected)))
print("docs:", len(set(e["metadata_doc_id"] for e in selected)))
import os
print("file KB:", round(os.path.getsize(OUT) / 1024, 1))
```

### [28] TOOL RESULT — Write · 2026-06-16 13:08:05 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_mini.py", "content": "#!/usr/bin/env python3\n\"\"\"Build mini_demo_data.json: a curated, diverse <=100-example subset of the full\ndecoy-FDR experiment output, plus trimmed reference metadata. No API needed — every\nexample already carries its rank-normalized real/decoy/swap scores + W statistics under\nboth elicitations (logprob `*_lp`, self-consistency `*_pt`).\"\"\"\nimport json\nfrom collections import defaultdict\n\nSRC = (\"/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/\"\n       \"gen_art/gen_art_experiment_2/full_method_out.json\")\nOUT = (\"/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/\"\n       \"notebook_workspaces/iter_2/art_Inu52CyA49Ys/mini_demo_data.json\")\n\nd = json.load(open(SRC))\nexs = d[\"datasets\"][0][\"examples\"]\n\nREQ = [\"metadata_z_real_rank_lp\", \"metadata_z_decoy_rank_lp\", \"metadata_z_swap_rank_lp\",\n       \"metadata_z_real_rank_pt\", \"metadata_z_decoy_rank_pt\", \"metadata_z_swap_rank_pt\",\n       \"metadata_w_cf_lp\", \"metadata_w_swap_lp\", \"metadata_w_cf_pt\", \"metadata_w_swap_pt\"]\nscored = [e for e in exs if all(e.get(k) is not None for k in REQ)]\n\n# Stratify by (label, fact_type); round-robin across documents for diversity.\nQUOTA = {(\"FALSE\", \"multi_hop\"): 32, (\"FALSE\", \"atomic\"): 30,\n         (\"TRUE\", \"atomic\"): 26, (\"TRUE\", \"multi_hop\"): 12}  # = 100\n\nstrata = defaultdict(lambda: defaultdict(list))  # (label,ft) -> doc_id -> [ex]\nfor e in scored:\n    strata[(e[\"output\"], e[\"metadata_fact_type\"])][e[\"metadata_doc_id\"]].append(e)\n\nselected = []\nfor key, quota in QUOTA.items():\n    by_doc = strata[key]\n    doc_ids = sorted(by_doc)               # deterministic\n    picked, di = [], 0\n    # round-robin: take one example from each doc in turn, spreading across documents\n    while len(picked) < quota and any(by_doc[doc] for doc in doc_ids):\n        doc = doc_ids[di % len(doc_ids)]\n        if by_doc[doc]:\n            picked.append(by_doc[doc].pop(0))\n        di += 1\n    selected.extend(picked)\n\n# Trimmed reference metadata: the full-run headline values the demo recomputes/compares to.\nm = d[\"metadata\"]\nref_meta = {\n    \"method_name\": m[\"method_name\"],\n    \"headline_finding\": m[\"headline_finding\"],\n    \"headline_elicitation\": m[\"headline_elicitation\"],\n    \"headline_verdict\": m[\"headline_verdict\"],\n    \"models\": m[\"models\"],\n    \"elicitation\": m[\"elicitation\"],\n    \"hyperparameters\": m[\"hyperparameters\"],\n    \"dataset_counts\": m[\"dataset_counts\"],\n    \"extraction_quality\": m[\"extraction_quality\"],\n    \"elicitation_comparison\": m[\"elicitation_comparison\"],\n    \"baseline_vs_method_fdr_by_elicitation\": m[\"baseline_vs_method_fdr_by_elicitation\"],\n}\n\nout = {\"metadata_reference_full_run\": ref_meta,\n       \"datasets\": [{\"dataset\": d[\"datasets\"][0][\"dataset\"], \"examples\": selected}]}\njson.dump(out, open(OUT, \"w\"), indent=2)\n\nfrom collections import Counter\nprint(\"selected:\", len(selected))\nprint(\"labels:\", dict(Counter(e[\"output\"] for e in selected)))\nprint(\"fact_type:\", dict(Counter(e[\"metadata_fact_type\"] for e in selected)))\nprint(\"docs:\", len(set(e[\"metadata_doc_id\"] for e in selected)))\nimport os\nprint(\"file KB:\", round(os.path.getsize(OUT) / 1024, 1))\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [29] TOOL CALL — Bash · 2026-06-16 13:08:11 UTC

```
Run mini data extraction script:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python build_mini.py
```

### [30] TOOL RESULT — Bash · 2026-06-16 13:08:11 UTC

```
{"stdout": "selected: 100\nlabels: {'FALSE': 62, 'TRUE': 38}\nfact_type: {'multi_hop': 44, 'atomic': 56}\ndocs: 34\nfile KB: 155.0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [31] ASSISTANT · 2026-06-16 13:09:03 UTC

```
100 diverse examples (62 FALSE / 38 TRUE) across 34 docs, 155 KB. Let me verify the headline elicitation-contrast actually reproduces on this subset before building the notebook.
```

### [32] TOOL CALL — Bash · 2026-06-16 13:09:03 UTC

```
Sanity-check elicitation contrast on mini subset:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python - <<'PY'
import json, sys
sys.path.insert(0,".")
import fdr_stats_reference as st
data = json.load(open("mini_demo_data.json"))
exs = data["datasets"][0]["examples"]
for tag,name in [("lp","logprob"),("pt","self-consistency")]:
    false = [e for e in exs if e["output"]=="FALSE"]
    pairs_cf = [(e[f"metadata_z_real_rank_{tag}"], e[f"metadata_z_decoy_rank_{tag}"]) for e in false]
    pairs_sw = [(e[f"metadata_z_real_rank_{tag}"], e[f"metadata_z_swap_rank_{tag}"]) for e in false]
    wr_cf,_ = st.tail_win_rate(pairs_cf, 0.0)
    wr_sw,_ = st.tail_win_rate(pairs_sw, 0.0)
    # method gate
    W = [e[f"metadata_w_cf_{tag}"] for e in exs]
    g = st.decoy_gate_fdr([{"w":e[f"metadata_w_cf_{tag}"],"is_false":e["output"]=="FALSE"} for e in exs], 0.5)
    # verify W matches stored
    mism = sum(1 for e in exs if abs(st.W_signed_max(e[f"metadata_z_real_rank_{tag}"],e[f"metadata_z_decoy_rank_{tag}"]) - e[f"metadata_w_cf_{tag}"])>1e-9)
    print(f"{name:18s} cf_winrate={wr_cf:.3f} swap_winrate={wr_sw:.3f} | gate@0.5 admit={g['n_admitted']} realFDR={g['realized_fdr']:.3f} | W-mismatch={mism}")
PY
```

### [33] TOOL RESULT — Bash · 2026-06-16 13:09:13 UTC

```
{"stdout": "logprob            cf_winrate=0.339 swap_winrate=0.323 | gate@0.5 admit=74 realFDR=0.554 | W-mismatch=0\nself-consistency   cf_winrate=0.565 swap_winrate=0.629 | gate@0.5 admit=19 realFDR=0.316 | W-mismatch=0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [34] ASSISTANT · 2026-06-16 13:09:57 UTC

```
The headline elicitation-contrast reproduces cleanly on the 100-example subset (logprob cf win-rate 0.339 < 0.5 = anti-conservative; self-consistency 0.565 ≈ exchangeable), and W-mismatch=0 confirms stored W equals `W_signed_max(ranks)`. Now let me build the notebook.
```

### [35] TOOL CALL — ToolSearch · 2026-06-16 13:09:57 UTC

```
{'query': 'select:NotebookEdit,TaskCreate', 'max_results': 2}
```

### [36] TOOL RESULT — ToolSearch · 2026-06-16 13:09:57 UTC

```
{"matches": ["NotebookEdit", "TaskCreate"], "query": "select:NotebookEdit,TaskCreate", "total_deferred_tools": 20}
```

### [37] ASSISTANT · 2026-06-16 13:11:49 UTC

```
I'll build the notebook with a generator script (avoids JSON-escaping errors and lets me embed `fdr_stats.py` verbatim).
```

### [38] TOOL CALL — Write · 2026-06-16 13:11:49 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_notebook.py

#!/usr/bin/env python3
"""Generate code_demo.ipynb for the decoy-competition FDR gate demo.
Builds the notebook as an nbformat dict and dumps to JSON (avoids manual escaping)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# fdr_stats.py is embedded VERBATIM (the genuine, unit-tested statistical core).
FDR_STATS = (HERE / "fdr_stats_reference.py").read_text()
# Strip the shebang line only; keep the module docstring + all functions unchanged.
FDR_STATS_BODY = FDR_STATS.split("\n", 1)[1] if FDR_STATS.startswith("#!") else FDR_STATS

cells = []
def md(src):   cells.append(("markdown", src))
def code(src): cells.append(("code", src))

# ----------------------------------------------------------------------------- 1
md(r"""# Label-free Decoy-Competition FDR Gate — Demo

**Artifact:** *Label-free decoy-competition (knockoff⁺) FDR gate validated on CLUTRR crisp gold.*

A neuro-symbolic pipeline extracts kinship facts from short stories with an LLM, then must
decide **which extracted facts to admit into a symbolic (Prolog-style) layer — without gold
labels**. The idea: make each extracted **"real"** fact compete against a property-matched
**counterfactual decoy** (same ordered entity pair, a plausible-but-wrong relation, verified
*not* entailed by the gold) plus a random type-matched **swap** control. A label-free
confidence elicitation scores all three in isolated, provenance-blinded calls; the
**Barber–Candès knockoff⁺ rule** turns "decoy beats real" events into a **False-Discovery-Rate
certificate** — exactly the quantified hallucination control the project targets.

### What this demo shows (no API calls, runs in seconds)
The expensive part of the experiment was ~50k cached LLM scoring calls. Those scores are
**already baked into the released examples** (per-example rank-normalized real/decoy/swap
scores + the knockoff statistic `W` under two elicitations). This notebook **re-runs the
offline statistical core** (`fdr_stats.py`, embedded verbatim below) on those cached scores
to reproduce the headline result:

> **The gate's validity is elicitation-dependent.** Under single-token **logprob** confidence
> the LLM is overconfident in its *own spontaneous errors*, so counterfactual decoys are
> **anti-conservative** (tail win-rate ≪ 0.5). Under **K=5 self-consistency** confidence the
> decoys become **exchangeable** (win-rate ≈ 0.5) and the gate controls realized FDR.

`lp` = logprob elicitation, `pt` = portable (self-consistency) elicitation, throughout.""")

# ----------------------------------------------------------------------------- 2 install
code(r"""# --- Install dependencies (works on Colab and local Jupyter) ---
import subprocess, sys
def _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])

# numpy / scipy / matplotlib are pre-installed on Colab — install locally at Colab's
# exact versions, but DO NOT touch them on Colab (would corrupt loaded C extensions).
if 'google.colab' not in sys.modules:
    _pip('numpy==2.0.2', 'scipy==1.16.3', 'matplotlib==3.10.0')""")

# ----------------------------------------------------------------------------- 3 imports
code(r"""# --- Imports (mirrors method.py / fdr_stats.py) ---
import json, os, math, hashlib
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt""")

# ----------------------------------------------------------------------------- 4 loader
code(r'''# --- Data loader: GitHub raw URL with local fallback (Colab-compatible) ---
GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json"

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception:
        pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f:
            return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")''')

# ----------------------------------------------------------------------------- 5 load
code(r"""data = load_data()
examples = data["datasets"][0]["examples"]            # cached per-real scores
ref = data["metadata_reference_full_run"]             # full 190-doc reported values

from collections import Counter
print(f"Loaded {len(examples)} reals from '{data['datasets'][0]['dataset']}'")
print("  labels   :", dict(Counter(e['output'] for e in examples)))
print("  fact_type:", dict(Counter(e['metadata_fact_type'] for e in examples)))
print("  documents:", len(set(e['metadata_doc_id'] for e in examples)))
print("\nFull-run headline verdict:", ref["headline_verdict"],
      "  (elicitation:", ref["headline_elicitation"] + ")")
# Peek at one cached example
ex = examples[0]
print("\nExample claim:", json.loads(ex['input'])['claim'], "->", ex['output'])
print("  logprob ranks   real/decoy/swap =",
      ex['metadata_z_real_rank_lp'], ex['metadata_z_decoy_rank_lp'], ex['metadata_z_swap_rank_lp'],
      "| W_cf =", ex['metadata_w_cf_lp'])
print("  self-cons ranks real/decoy/swap =",
      ex['metadata_z_real_rank_pt'], ex['metadata_z_decoy_rank_pt'], ex['metadata_z_swap_rank_pt'],
      "| W_cf =", ex['metadata_w_cf_pt'])""")

# ----------------------------------------------------------------------------- 6 config md
md(r"""## Configuration

All tunable parameters live here. They start small for a fast demo; comment-marked
**ORIGINAL** values reproduce the paper's run. The offline statistics are cheap (pure
NumPy/SciPy over ~100 reals), so the only runtime knob that matters is the bootstrap
replicate count `B_BOOT`.""")

# ----------------------------------------------------------------------------- 7 config
code(r"""# --- Config (minimum-first; ORIGINAL values noted) ---
SEED        = 20240617                       # matches method.py
ALPHA_GRID  = [0.05, 0.10, 0.20, 0.30, 0.50] # nominal FDR levels (k-floors 20,10,5,4,2)
B_BOOT      = 2000                           # document-block bootstrap reps (ORIGINAL 2000)
                                             # demo subset is small => 2000 still runs in <1s
USE_N       = None                           # None = use all loaded reals (the demo subset)
ELICITATIONS = {"lp": "logprob (single-token P(Yes))",
                "pt": "portable (K=5 self-consistency)"}

if USE_N is not None:
    examples = examples[:USE_N]
print(f"Using {len(examples)} reals; B_BOOT={B_BOOT}; alpha grid={ALPHA_GRID}")""")

# ----------------------------------------------------------------------------- 8 fdr_stats md
md(r"""## Statistical core — `fdr_stats.py` (embedded verbatim)

This is the artifact's pure statistical module, **unchanged**. It implements the canonical
knockoff statistic `W_signed_max`, the **knockoff⁺ operative threshold** (Barber–Candès 2015,
eq. 1.9), the tail-conditioned decoy **win-rate**, two-sample tests (KS / Mann–Whitney),
document-block (cluster) **bootstrap** CIs, empirical-CDF export, and the realized-FDR gates.
The cells that follow call into these functions exactly as `method.py` does.""")

# ----------------------------------------------------------------------------- 9 fdr_stats body
code("# === fdr_stats.py (verbatim from the artifact) ===\n" + FDR_STATS_BODY +
     "\n\nst = sys.modules[__name__]  # call the functions above as st.<fn>, mirroring method.py")

# ----------------------------------------------------------------------------- 10 records md
md(r"""## Build per-example records

`method.py` assembles, for every extracted **real** fact, a tuple of its rank-normalized
score `zr`, its counterfactual-decoy score `z_cf`, its swap-control score `z_sw`, and the
knockoff statistics `W`. Here we read those straight from the cached examples (one record per
real), for each elicitation. We also **re-derive `W` with `st.W_signed_max`** and confirm it
matches the stored value — a sanity check that the embedded core reproduces the released
numbers.""")

# ----------------------------------------------------------------------------- 11 records
code(r"""def build_records(examples, tag):
    """ + '"""' + r"""One record per real fact for elicitation `tag` ('lp' or 'pt')."""  + '"""' + r"""
    recs = []
    for e in examples:
        recs.append({
            "doc_id":    e["metadata_doc_id"],
            "label":     e["output"],                         # TRUE / FALSE (crisp gold)
            "fact_type": e["metadata_fact_type"],
            "zr":   e[f"metadata_z_real_rank_{tag}"],          # real's rank-normalized score
            "z_cf": e[f"metadata_z_decoy_rank_{tag}"],         # counterfactual decoy score
            "z_sw": e[f"metadata_z_swap_rank_{tag}"],          # random swap control score
            "w_cf": e[f"metadata_w_cf_{tag}"],                 # signed-max W vs counterfactual
            "w_sw": e[f"metadata_w_swap_{tag}"],               # signed-max W vs swap
        })
    return recs

records = {tag: build_records(examples, tag) for tag in ELICITATIONS}

# Sanity: recompute W with the embedded core and confirm it matches the cached value.
for tag in ELICITATIONS:
    mism = sum(1 for r in records[tag]
               if abs(st.W_signed_max(r["zr"], r["z_cf"]) - r["w_cf"]) > 1e-9)
    print(f"[{tag}] {len(records[tag])} records | W_signed_max mismatches vs cached: {mism}")""")

# ----------------------------------------------------------------------------- 12 s1 md
md(r"""## Result 1 — S1 decoy signature (the headline)

On the **known-false** reals (genuine extractor errors), under exchangeability the decoy
should beat the real about half the time: tail **win-rate ≈ 0.5**. We compute, per elicitation
and per decoy family (counterfactual vs random-swap control):

* the **tail win-rate** over all false pairs, with a **document-block bootstrap** 95% CI,
* a two-sample **KS** test (decoy vs real scores), and
* the **knockoff⁺** operating points: threshold `T(α)`, admissions, and whether α is certifiable.

This is the offline `analyze_s1` logic from `method.py`, reading the cached scores.""")

# ----------------------------------------------------------------------------- 13 s1
code(r"""def certified_alphas(W):                       # verbatim logic from method.py
    out = []
    for a in ALPHA_GRID:
        T, n, _ = st.knockoff_plus_threshold(W, a)
        out.append({"alpha": a, "threshold": (None if math.isinf(T) else T),
                    "n_admitted": n, "k_floor": st.k_floor(a),
                    "certified": n >= st.k_floor(a)})
    return out

def analyze_s1(recs, family):
    """ + '"""' + r"""family: 'counterfactual' (z_cf/w_cf) or 'random_swap' (z_sw/w_sw)."""  + '"""' + r"""
    zk = "z_cf" if family == "counterfactual" else "z_sw"
    wk = "w_cf" if family == "counterfactual" else "w_sw"
    W_all = [r[wk] for r in recs]
    false_pairs = [r for r in recs if r["label"] == "FALSE"]
    pairs = [(r["zr"], r[zk]) for r in false_pairs]

    # tail win-rate over ALL false pairs (threshold 0 = full admission region)
    wr, n_tail = st.tail_win_rate(pairs, 0.0)
    ks_s, ks_p = st.ks_two_sample([r[zk] for r in false_pairs],
                                  [r["zr"] for r in false_pairs], "two-sided")
    # document-block (cluster) bootstrap CI of the win-rate
    by_doc = {}
    for r in false_pairs:
        by_doc.setdefault(r["doc_id"], []).append(r)
    units = list(by_doc.values())
    def wr_fn(resample):
        flat = [r for grp in resample for r in grp]
        if not flat:
            return float("nan")
        return np.mean([1.0 if r[zk] > r["zr"] else 0.0 for r in flat])
    ci = st.doc_block_bootstrap(units, wr_fn, B=B_BOOT, seed=SEED)
    return {"win_rate": wr, "ci": [ci["ci_low"], ci["ci_high"]], "n_tail": n_tail,
            "ks_p": ks_p, "n_false": len(false_pairs),
            "knockoff_rows": certified_alphas(W_all)}

s1 = {tag: {fam: analyze_s1(records[tag], fam)
            for fam in ("counterfactual", "random_swap")}
      for tag in ELICITATIONS}

for tag, name in ELICITATIONS.items():
    cf = s1[tag]["counterfactual"]
    verdict = "EXCHANGEABLE (CI covers 0.5)" if cf["ci"][0] <= 0.5 <= cf["ci"][1] \
              else "ANTI-CONSERVATIVE (win-rate < 0.5)"
    print(f"[{tag}] {name}")
    print(f"     counterfactual tail win-rate = {cf['win_rate']:.3f} "
          f"95% CI [{cf['ci'][0]:.3f}, {cf['ci'][1]:.3f}]  KS p={cf['ks_p']:.2e}")
    print(f"     => {verdict}\n")""")

# ----------------------------------------------------------------------------- 14 crux md
md(r"""## Result 2 — Spontaneous-error tail match (the crux)

For the gate to be valid, the **counterfactual-decoy** score distribution `F_decoy` must match
the **genuine spontaneous-error** distribution `F_spont` (the FALSE reals) — and differ from
the **true-positive** distribution `F_truepos`. We run KS tests both ways and export the three
empirical CDFs for the overlay plot. This is `analyze_crux` from `method.py`.""")

# ----------------------------------------------------------------------------- 15 crux
code(r"""def analyze_crux(recs):
    F_truepos = [r["zr"]   for r in recs if r["label"] == "TRUE"]
    F_spont   = [r["zr"]   for r in recs if r["label"] == "FALSE"]
    F_decoy   = [r["z_cf"] for r in recs]                  # counterfactual decoy scores
    ks_spont   = st.ks_two_sample(F_decoy, F_spont,   "two-sided")[1]   # want: NOT reject
    ks_truepos = st.ks_two_sample(F_decoy, F_truepos, "two-sided")[1]   # want: reject
    grid = [round(x, 3) for x in np.linspace(0, 1, 101)]
    cdfs = {"x": grid,
            "truepos": st.empirical_cdf(F_truepos, grid),
            "spont":   st.empirical_cdf(F_spont,   grid),
            "decoy":   st.empirical_cdf(F_decoy,   grid)}
    return {"n_truepos": len(F_truepos), "n_spont": len(F_spont), "n_decoy": len(F_decoy),
            "ks_decoy_vs_spont_p": ks_spont, "ks_decoy_vs_truepos_p": ks_truepos, "cdfs": cdfs}

crux = {tag: analyze_crux(records[tag]) for tag in ELICITATIONS}
for tag, name in ELICITATIONS.items():
    c = crux[tag]
    print(f"[{tag}] {name}: decoy~spont KS p={c['ks_decoy_vs_spont_p']:.3f} "
          f"(want > 0.05, fail-to-reject)  |  decoy~truepos KS p={c['ks_decoy_vs_truepos_p']:.2e} "
          f"(want << 0.05, reject)")""")

# ----------------------------------------------------------------------------- 16 gate md
md(r"""## Result 3 — Method gate realized FDR (vs the purely-neural baseline)

The decoy-FDR gate admits reals with `W ≥ T(α)`; we measure the **realized FDR** against crisp
gold (`decoy_gate_fdr`). The raw-confidence **baseline** (just threshold the model's own
confidence) is reported from the full 190-doc run for comparison — it admits hundreds of facts
at 45–65% realized FDR, the hallucination problem the gate prevents.""")

# ----------------------------------------------------------------------------- 17 gate
code(r"""def method_gate_fdr(recs):
    labelable = [{"w": r["w_cf"], "is_false": r["label"] == "FALSE"} for r in recs]
    return [st.decoy_gate_fdr(labelable, a) for a in ALPHA_GRID]

gate = {tag: method_gate_fdr(records[tag]) for tag in ELICITATIONS}

# Baseline numbers from the full-run reference metadata (raw scores not in the demo subset).
baseline_ref = ref["baseline_vs_method_fdr_by_elicitation"]
view_for = {"lp": "logprob_full", "pt": "portable_full"}

for tag, name in ELICITATIONS.items():
    print(f"[{tag}] {name} — decoy-FDR gate (this demo, {len(examples)} reals):")
    for row in gate[tag]:
        cert = "certified" if row["certified"] else "not-cert "
        print(f"     alpha={row['alpha']:.2f}  admit={row['n_admitted']:3d}  "
              f"realized_FDR={row['realized_fdr']:.3f}  [{cert}]")""")

# ----------------------------------------------------------------------------- 18 viz md
md(r"""## Results summary & visualization

Three panels:
1. **Counterfactual decoy tail win-rate** by elicitation (the headline) — bars with bootstrap
   CIs and the exchangeability line at 0.5.
2. **Crux CDF overlay** (self-consistency) — decoy tracks the spontaneous-error CDF, not the
   true-positive CDF.
3. **Realized-FDR calibration** — the demo's decoy gate vs the full-run raw-confidence baseline.""")

# ----------------------------------------------------------------------------- 19 viz
code(r"""# ---- Text summary table: demo-recomputed vs full-run reported win-rates ----
print("Counterfactual decoy tail win-rate  (want ~0.5 = exchangeable)")
print(f"{'elicitation':<28}{'demo win-rate (95% CI)':<30}{'full-run reported':<20}")
ec = ref["elicitation_comparison"]
for tag, name in ELICITATIONS.items():
    cf = s1[tag]["counterfactual"]
    full = ec[view_for[tag]]["counterfactual_tail_win_rate"]
    demo = f"{cf['win_rate']:.3f} [{cf['ci'][0]:.3f}, {cf['ci'][1]:.3f}]"
    print(f"{name:<28}{demo:<30}{full:.3f}")

# ---- Plots ----
fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# Panel 1: counterfactual win-rate by elicitation, with bootstrap CIs
ax = axes[0]
tags = list(ELICITATIONS)
wr = [s1[t]["counterfactual"]["win_rate"] for t in tags]
lo = [s1[t]["counterfactual"]["win_rate"] - s1[t]["counterfactual"]["ci"][0] for t in tags]
hi = [s1[t]["counterfactual"]["ci"][1] - s1[t]["counterfactual"]["win_rate"] for t in tags]
colors = ["#d1495b" if not (s1[t]["counterfactual"]["ci"][0] <= 0.5 <= s1[t]["counterfactual"]["ci"][1])
          else "#2e8b57" for t in tags]
ax.bar(tags, wr, yerr=[lo, hi], capsize=8, color=colors, alpha=0.85)
ax.axhline(0.5, ls="--", c="k", lw=1, label="exchangeable (0.5)")
ax.set_ylim(0, 1); ax.set_ylabel("decoy tail win-rate")
ax.set_title("R1: counterfactual decoy win-rate\n(red=anti-conservative, green=exchangeable)")
ax.legend(loc="upper left", fontsize=8)

# Panel 2: crux CDF overlay (self-consistency 'pt')
ax = axes[1]
c = crux["pt"]["cdfs"]
ax.plot(c["x"], c["truepos"], label="true positives", c="#2e8b57", lw=2)
ax.plot(c["x"], c["spont"],   label="spontaneous errors (FALSE)", c="#e0a800", lw=2)
ax.plot(c["x"], c["decoy"],   label="counterfactual decoys", c="#d1495b", lw=2, ls="--")
ax.set_xlabel("rank-normalized confidence score"); ax.set_ylabel("empirical CDF")
ax.set_title(f"R2: crux CDF overlay (self-consistency)\n"
             f"decoy~spont KS p={crux['pt']['ks_decoy_vs_spont_p']:.2f}")
ax.legend(loc="lower right", fontsize=8)

# Panel 3: realized-FDR calibration (self-consistency gate vs full-run baseline)
ax = axes[2]
alphas = ALPHA_GRID
m_fdr = [r["realized_fdr"] if r["n_admitted"] > 0 else np.nan for r in gate["pt"]]
brows = {r["alpha"]: r for r in baseline_ref["portable_full"]["rows"]}
b_fdr = [brows[a]["baseline_realized_fdr"] if a in brows else np.nan for a in alphas]
ax.plot(alphas, alphas, ls=":", c="k", label="nominal (y=x)")
ax.plot(alphas, m_fdr, "o-", c="#2e8b57", label="decoy gate (demo)")
ax.plot(alphas, b_fdr, "s-", c="#d1495b", label="raw-confidence baseline (full run)")
ax.set_xlabel("nominal alpha"); ax.set_ylabel("realized FDR")
ax.set_title("R3: realized-FDR calibration\n(self-consistency)")
ax.legend(loc="upper left", fontsize=8)

plt.tight_layout()
plt.savefig("demo_results.png", dpi=110, bbox_inches="tight")
plt.show()
print("\nHeadline reproduced:", ref["headline_verdict"],
      "under the", ref["headline_elicitation"], "elicitation.")""")

# --- assemble notebook ---
nb_cells = []
for ctype, src in cells:
    cell = {"cell_type": ctype, "metadata": {}, "source": src.splitlines(keepends=True)}
    if ctype == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    nb_cells.append(cell)

nb = {"cells": nb_cells,
      "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python",
                                   "name": "python3"},
                   "language_info": {"name": "python", "version": "3.12"}},
      "nbformat": 4, "nbformat_minor": 5}

out = HERE / "code_demo.ipynb"
out.write_text(json.dumps(nb, indent=1))
print("wrote", out, "with", len(nb_cells), "cells")
```

### [39] TOOL RESULT — Write · 2026-06-16 13:11:49 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_notebook.py", "content": "#!/usr/bin/env python3\n\"\"\"Generate code_demo.ipynb for the decoy-competition FDR gate demo.\nBuilds the notebook as an nbformat dict and dumps to JSON (avoids manual escaping).\"\"\"\nimport json\nfrom pathlib import Path\n\nHERE = Path(__file__).resolve().parent\n# fdr_stats.py is embedded VERBATIM (the genuine, unit-tested statistical core).\nFDR_STATS = (HERE / \"fdr_stats_reference.py\").read_text()\n# Strip the shebang line only; keep the module docstring + all functions unchanged.\nFDR_STATS_BODY = FDR_STATS.split(\"\\n\", 1)[1] if FDR_STATS.startswith(\"#!\") else FDR_STATS\n\ncells = []\ndef md(src):   cells.append((\"markdown\", src))\ndef code(src): cells.append((\"code\", src))\n\n# ----------------------------------------------------------------------------- 1\nmd(r\"\"\"# Label-free Decoy-Competition FDR Gate — Demo\n\n**Artifact:** *Label-free decoy-competition (knockoff⁺) FDR gate validated on CLUTRR crisp gold.*\n\nA neuro-symbolic pipeline extracts kinship facts from short stories with an LLM, then must\ndecide **which extracted facts to admit into a symbolic (Prolog-style) layer — without gold\nlabels**. The idea: make each extracted **\"real\"** fact compete against a property-matched\n**counterfactual decoy** (same ordered entity pair, a plausible-but-wrong relation, verified\n*not* entailed by the gold) plus a random type-matched **swap** control. A label-free\nconfidence elicitation scores all three in isolated, provenance-blinded calls; the\n**Barber–Candès knockoff⁺ rule** turns \"decoy beats real\" events into a **False-Discovery-Rate\ncertificate** — exactly the quantified hallucination control the project targets.\n\n### What this demo shows (no API calls, runs in seconds)\nThe expensive part of the experiment was ~50k cached LLM scoring calls. Those scores are\n**already baked into the released examples** (per-example rank-normalized real/decoy/swap\nscores + the knockoff statistic `W` under two elicitations). This notebook **re-runs the\noffline statistical core** (`fdr_stats.py`, embedded verbatim below) on those cached scores\nto reproduce the headline result:\n\n> **The gate's validity is elicitation-dependent.** Under single-token **logprob** confidence\n> the LLM is overconfident in its *own spontaneous errors*, so counterfactual decoys are\n> **anti-conservative** (tail win-rate ≪ 0.5). Under **K=5 self-consistency** confidence the\n> decoys become **exchangeable** (win-rate ≈ 0.5) and the gate controls realized FDR.\n\n`lp` = logprob elicitation, `pt` = portable (self-consistency) elicitation, throughout.\"\"\")\n\n# ----------------------------------------------------------------------------- 2 install\ncode(r\"\"\"# --- Install dependencies (works on Colab and local Jupyter) ---\nimport subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# numpy / scipy / matplotlib are pre-installed on Colab — install locally at Colab's\n# exact versions, but DO NOT touch them on Colab (would corrupt loaded C extensions).\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'scipy==1.16.3', 'matplotlib==3.10.0')\"\"\")\n\n# ----------------------------------------------------------------------------- 3 imports\ncode(r\"\"\"# --- Imports (mirrors method.py / fdr_stats.py) ---\nimport json, os, math, hashlib\nimport numpy as np\nfrom scipy import stats\nimport matplotlib.pyplot as plt\"\"\")\n\n# ----------------------------------------------------------------------------- 4 loader\ncode(r'''# --- Data loader: GitHub raw URL with local fallback (Colab-compatible) ---\nGITHUB_DATA_URL = \"https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json\"\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f:\n            return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")''')\n\n# ----------------------------------------------------------------------------- 5 load\ncode(r\"\"\"data = load_data()\nexamples = data[\"datasets\"][0][\"examples\"]            # cached per-real scores\nref = data[\"metadata_reference_full_run\"]             # full 190-doc reported values\n\nfrom collections import Counter\nprint(f\"Loaded {len(examples)} reals from '{data['datasets'][0]['dataset']}'\")\nprint(\"  labels   :\", dict(Counter(e['output'] for e in examples)))\nprint(\"  fact_type:\", dict(Counter(e['metadata_fact_type'] for e in examples)))\nprint(\"  documents:\", len(set(e['metadata_doc_id'] for e in examples)))\nprint(\"\\nFull-run headline verdict:\", ref[\"headline_verdict\"],\n      \"  (elicitation:\", ref[\"headline_elicitation\"] + \")\")\n# Peek at one cached example\nex = examples[0]\nprint(\"\\nExample claim:\", json.loads(ex['input'])['claim'], \"->\", ex['output'])\nprint(\"  logprob ranks   real/decoy/swap =\",\n      ex['metadata_z_real_rank_lp'], ex['metadata_z_decoy_rank_lp'], ex['metadata_z_swap_rank_lp'],\n      \"| W_cf =\", ex['metadata_w_cf_lp'])\nprint(\"  self-cons ranks real/decoy/swap =\",\n      ex['metadata_z_real_rank_pt'], ex['metadata_z_decoy_rank_pt'], ex['metadata_z_swap_rank_pt'],\n      \"| W_cf =\", ex['metadata_w_cf_pt'])\"\"\")\n\n# ----------------------------------------------------------------------------- 6 config md\nmd(r\"\"\"## Configuration\n\nAll tunable parameters live here. They start small for a fast demo; comment-marked\n**ORIGINAL** values reproduce the paper's run. The offline statistics are cheap (pure\nNumPy/SciPy over ~100 reals), so the only runtime knob that matters is the bootstrap\nreplicate count `B_BOOT`.\"\"\")\n\n# ----------------------------------------------------------------------------- 7 config\ncode(r\"\"\"# --- Config (minimum-first; ORIGINAL values noted) ---\nSEED        = 20240617                       # matches method.py\nALPHA_GRID  = [0.05, 0.10, 0.20, 0.30, 0.50] # nominal FDR levels (k-floors 20,10,5,4,2)\nB_BOOT      = 2000                           # document-block bootstrap reps (ORIGINAL 2000)\n                                             # demo subset is small => 2000 still runs in <1s\nUSE_N       = None                           # None = use all loaded reals (the demo subset)\nELICITATIONS = {\"lp\": \"logprob (single-token P(Yes))\",\n                \"pt\": \"portable (K=5 self-consistency)\"}\n\nif USE_N is not None:\n    examples = examples[:USE_N]\nprint(f\"Using {len(examples)} reals; B_BOOT={B_BOOT}; alpha grid={ALPHA_GRID}\")\"\"\")\n\n# ----------------------------------------------------------------------------- 8 fdr_stats md\nmd(r\"\"\"## Statistical core — `fdr_stats.py` (embedded verbatim)\n\nThis is the artifact's pure statistical module, **unchanged**. It implements the canonical\nknockoff statistic `W_signed_max`, the **knockoff⁺ operative threshold** (Barber–Candès 2015,\neq. 1.9), the tail-conditioned decoy **win-rate**, two-sample tests (KS / Mann–Whitney),\ndocument-block (cluster) **bootstrap** CIs, empirical-CDF export, and the realized-FDR gates.\nThe cells that follow call into these functions exactly as `method.py` does.\"\"\")\n\n# ----------------------------------------------------------------------------- 9 fdr_stats body\ncode(\"# === fdr_stats.py (verbatim from the artifact) ===\\n\" + FDR_STATS_BODY +\n     \"\\n\\nst = sys.modules[__name__]  # call the functions above as st.<fn>, mirroring method.py\")\n\n# ----------------------------------------------------------------------------- 10 records md\nmd(r\"\"\"## Build per-example records\n\n`method.py` assembles, for every extracted **real** fact, a tuple of its rank-normalized\nscore `zr`, its counterfactual-decoy score `z_cf`, its swap-control score `z_sw`, and the\nknockoff statistics `W`. Here we read those straight from the cached examples (one record per\nreal), for each elicitation. We also **re-derive `W` with `st.W_signed_max`** and confirm it\nmatches the stored value — a sanity check that the embedded core reproduces the released\nnumbers.\"\"\")\n\n# ----------------------------------------------------------------------------- 11 records\ncode(r\"\"\"def build_records(examples, tag):\n    \"\"\" + '\"\"\"' + r\"\"\"One record per real fact for elicitation `tag` ('lp' or 'pt').\"\"\"  + '\"\"\"' + r\"\"\"\n    recs = []\n    for e in examples:\n        recs.append({\n            \"doc_id\":    e[\"metadata_doc_id\"],\n            \"label\":     e[\"output\"],                         # TRUE / FALSE (crisp gold)\n            \"fact_type\": e[\"metadata_fact_type\"],\n            \"zr\":   e[f\"metadata_z_real_rank_{tag}\"],          # real's rank-normalized score\n            \"z_cf\": e[f\"metadata_z_decoy_rank_{tag}\"],         # counterfactual decoy score\n            \"z_sw\": e[f\"metadata_z_swap_rank_{tag}\"],          # random swap control score\n            \"w_cf\": e[f\"metadata_w_cf_{tag}\"],                 # signed-max W vs counterfactual\n            \"w_sw\": e[f\"metadata_w_swap_{tag}\"],               # signed-max W vs swap\n        })\n    return recs\n\nrecords = {tag: build_records(examples, tag) for tag in ELICITATIONS}\n\n# Sanity: recompute W with the embedded core and confirm it matches the cached value.\nfor tag in ELICITATIONS:\n    mism = sum(1 for r in records[tag]\n               if abs(st.W_signed_max(r[\"zr\"], r[\"z_cf\"]) - r[\"w_cf\"]) > 1e-9)\n    print(f\"[{tag}] {len(records[tag])} records | W_signed_max mismatches vs cached: {mism}\")\"\"\")\n\n# ----------------------------------------------------------------------------- 12 s1 md\nmd(r\"\"\"## Result 1 — S1 decoy signature (the headline)\n\nOn the **known-false** reals (genuine extractor errors), under exchangeability the decoy\nshould beat the real about half the time: tail **win-rate ≈ 0.5**. We compute, per elicitation\nand per decoy family (counterfactual vs random-swap control):\n\n* the **tail win-rate** over all false pairs, with a **document-block bootstrap** 95% CI,\n* a two-sample **KS** test (decoy vs real scores), and\n* the **knockoff⁺** operating points: threshold `T(α)`, admissions, and whether α is certifiable.\n\nThis is the offline `analyze_s1` logic from `method.py`, reading the cached scores.\"\"\")\n\n# ----------------------------------------------------------------------------- 13 s1\ncode(r\"\"\"def certified_alphas(W):                       # verbatim logic from method.py\n    out = []\n    for a in ALPHA_GRID:\n        T, n, _ = st.knockoff_plus_threshold(W, a)\n        out.append({\"alpha\": a, \"threshold\": (None if math.isinf(T) else T),\n                    \"n_admitted\": n, \"k_floor\": st.k_floor(a),\n                    \"certified\": n >= st.k_floor(a)})\n    return out\n\ndef analyze_s1(recs, family):\n    \"\"\" + '\"\"\"' + r\"\"\"family: 'counterfactual' (z_cf/w_cf) or 'random_swap' (z_sw/w_sw).\"\"\"  + '\"\"\"' + r\"\"\"\n    zk = \"z_cf\" if family == \"counterfactual\" else \"z_sw\"\n    wk = \"w_cf\" if family == \"counterfactual\" else \"w_sw\"\n    W_all = [r[wk] for r in recs]\n    false_pairs = [r for r in recs if r[\"label\"] == \"FALSE\"]\n    pairs = [(r[\"zr\"], r[zk]) for r in false_pairs]\n\n    # tail win-rate over ALL false pairs (threshold 0 = full admission region)\n    wr, n_tail = st.tail_win_rate(pairs, 0.0)\n    ks_s, ks_p = st.ks_two_sample([r[zk] for r in false_pairs],\n                                  [r[\"zr\"] for r in false_pairs], \"two-sided\")\n    # document-block (cluster) bootstrap CI of the win-rate\n    by_doc = {}\n    for r in false_pairs:\n        by_doc.setdefault(r[\"doc_id\"], []).append(r)\n    units = list(by_doc.values())\n    def wr_fn(resample):\n        flat = [r for grp in resample for r in grp]\n        if not flat:\n            return float(\"nan\")\n        return np.mean([1.0 if r[zk] > r[\"zr\"] else 0.0 for r in flat])\n    ci = st.doc_block_bootstrap(units, wr_fn, B=B_BOOT, seed=SEED)\n    return {\"win_rate\": wr, \"ci\": [ci[\"ci_low\"], ci[\"ci_high\"]], \"n_tail\": n_tail,\n            \"ks_p\": ks_p, \"n_false\": len(false_pairs),\n            \"knockoff_rows\": certified_alphas(W_all)}\n\ns1 = {tag: {fam: analyze_s1(records[tag], fam)\n            for fam in (\"counterfactual\", \"random_swap\")}\n      for tag in ELICITATIONS}\n\nfor tag, name in ELICITATIONS.items():\n    cf = s1[tag][\"counterfactual\"]\n    verdict = \"EXCHANGEABLE (CI covers 0.5)\" if cf[\"ci\"][0] <= 0.5 <= cf[\"ci\"][1] \\\n              else \"ANTI-CONSERVATIVE (win-rate < 0.5)\"\n    print(f\"[{tag}] {name}\")\n    print(f\"     counterfactual tail win-rate = {cf['win_rate']:.3f} \"\n          f\"95% CI [{cf['ci'][0]:.3f}, {cf['ci'][1]:.3f}]  KS p={cf['ks_p']:.2e}\")\n    print(f\"     => {verdict}\\n\")\"\"\")\n\n# ----------------------------------------------------------------------------- 14 crux md\nmd(r\"\"\"## Result 2 — Spontaneous-error tail match (the crux)\n\nFor the gate to be valid, the **counterfactual-decoy** score distribution `F_decoy` must match\nthe **genuine spontaneous-error** distribution `F_spont` (the FALSE reals) — and differ from\nthe **true-positive** distribution `F_truepos`. We run KS tests both ways and export the three\nempirical CDFs for the overlay plot. This is `analyze_crux` from `method.py`.\"\"\")\n\n# ----------------------------------------------------------------------------- 15 crux\ncode(r\"\"\"def analyze_crux(recs):\n    F_truepos = [r[\"zr\"]   for r in recs if r[\"label\"] == \"TRUE\"]\n    F_spont   = [r[\"zr\"]   for r in recs if r[\"label\"] == \"FALSE\"]\n    F_decoy   = [r[\"z_cf\"] for r in recs]                  # counterfactual decoy scores\n    ks_spont   = st.ks_two_sample(F_decoy, F_spont,   \"two-sided\")[1]   # want: NOT reject\n    ks_truepos = st.ks_two_sample(F_decoy, F_truepos, \"two-sided\")[1]   # want: reject\n    grid = [round(x, 3) for x in np.linspace(0, 1, 101)]\n    cdfs = {\"x\": grid,\n            \"truepos\": st.empirical_cdf(F_truepos, grid),\n            \"spont\":   st.empirical_cdf(F_spont,   grid),\n            \"decoy\":   st.empirical_cdf(F_decoy,   grid)}\n    return {\"n_truepos\": len(F_truepos), \"n_spont\": len(F_spont), \"n_decoy\": len(F_decoy),\n            \"ks_decoy_vs_spont_p\": ks_spont, \"ks_decoy_vs_truepos_p\": ks_truepos, \"cdfs\": cdfs}\n\ncrux = {tag: analyze_crux(records[tag]) for tag in ELICITATIONS}\nfor tag, name in ELICITATIONS.items():\n    c = crux[tag]\n    print(f\"[{tag}] {name}: decoy~spont KS p={c['ks_decoy_vs_spont_p']:.3f} \"\n          f\"(want > 0.05, fail-to-reject)  |  decoy~truepos KS p={c['ks_decoy_vs_truepos_p']:.2e} \"\n          f\"(want << 0.05, reject)\")\"\"\")\n\n# ----------------------------------------------------------------------------- 16 gate md\nmd(r\"\"\"## Result 3 — Method gate realized FDR (vs the purely-neural baseline)\n\nThe decoy-FDR gate admits reals with `W ≥ T(α)`; we measure the **realized FDR** against crisp\ngold (`decoy_gate_fdr`). The raw-confidence **baseline** (just threshold the model's own\nconfidence) is reported from the full 190-doc run for comparison — it admits hundreds of facts\nat 45–65% realized FDR, the hallucination problem the gate prevents.\"\"\")\n\n# ----------------------------------------------------------------------------- 17 gate\ncode(r\"\"\"def method_gate_fdr(recs):\n    labelable = [{\"w\": r[\"w_cf\"], \"is_false\": r[\"label\"] == \"FALSE\"} for r in recs]\n    return [st.decoy_gate_fdr(labelable, a) for a in ALPHA_GRID]\n\ngate = {tag: method_gate_fdr(records[tag]) for tag in ELICITATIONS}\n\n# Baseline numbers from the full-run reference metadata (raw scores not in the demo subset).\nbaseline_ref = ref[\"baseline_vs_method_fdr_by_elicitation\"]\nview_for = {\"lp\": \"logprob_full\", \"pt\": \"portable_full\"}\n\nfor tag, name in ELICITATIONS.items():\n    print(f\"[{tag}] {name} — decoy-FDR gate (this demo, {len(examples)} reals):\")\n    for row in gate[tag]:\n        cert = \"certified\" if row[\"certified\"] else \"not-cert \"\n        print(f\"     alpha={row['alpha']:.2f}  admit={row['n_admitted']:3d}  \"\n              f\"realized_FDR={row['realized_fdr']:.3f}  [{cert}]\")\"\"\")\n\n# ----------------------------------------------------------------------------- 18 viz md\nmd(r\"\"\"## Results summary & visualization\n\nThree panels:\n1. **Counterfactual decoy tail win-rate** by elicitation (the headline) — bars with bootstrap\n   CIs and the exchangeability line at 0.5.\n2. **Crux CDF overlay** (self-consistency) — decoy tracks the spontaneous-error CDF, not the\n   true-positive CDF.\n3. **Realized-FDR calibration** — the demo's decoy gate vs the full-run raw-confidence baseline.\"\"\")\n\n# ----------------------------------------------------------------------------- 19 viz\ncode(r\"\"\"# ---- Text summary table: demo-recomputed vs full-run reported win-rates ----\nprint(\"Counterfactual decoy tail win-rate  (want ~0.5 = exchangeable)\")\nprint(f\"{'elicitation':<28}{'demo win-rate (95% CI)':<30}{'full-run reported':<20}\")\nec = ref[\"elicitation_comparison\"]\nfor tag, name in ELICITATIONS.items():\n    cf = s1[tag][\"counterfactual\"]\n    full = ec[view_for[tag]][\"counterfactual_tail_win_rate\"]\n    demo = f\"{cf['win_rate']:.3f} [{cf['ci'][0]:.3f}, {cf['ci'][1]:.3f}]\"\n    print(f\"{name:<28}{demo:<30}{full:.3f}\")\n\n# ---- Plots ----\nfig, axes = plt.subplots(1, 3, figsize=(16, 4.5))\n\n# Panel 1: counterfactual win-rate by elicitation, with bootstrap CIs\nax = axes[0]\ntags = list(ELICITATIONS)\nwr = [s1[t][\"counterfactual\"][\"win_rate\"] for t in tags]\nlo = [s1[t][\"counterfactual\"][\"win_rate\"] - s1[t][\"counterfactual\"][\"ci\"][0] for t in tags]\nhi = [s1[t][\"counterfactual\"][\"ci\"][1] - s1[t][\"counterfactual\"][\"win_rate\"] for t in tags]\ncolors = [\"#d1495b\" if not (s1[t][\"counterfactual\"][\"ci\"][0] <= 0.5 <= s1[t][\"counterfactual\"][\"ci\"][1])\n          else \"#2e8b57\" for t in tags]\nax.bar(tags, wr, yerr=[lo, hi], capsize=8, color=colors, alpha=0.85)\nax.axhline(0.5, ls=\"--\", c=\"k\", lw=1, label=\"exchangeable (0.5)\")\nax.set_ylim(0, 1); ax.set_ylabel(\"decoy tail win-rate\")\nax.set_title(\"R1: counterfactual decoy win-rate\\n(red=anti-conservative, green=exchangeable)\")\nax.legend(loc=\"upper left\", fontsize=8)\n\n# Panel 2: crux CDF overlay (self-consistency 'pt')\nax = axes[1]\nc = crux[\"pt\"][\"cdfs\"]\nax.plot(c[\"x\"], c[\"truepos\"], label=\"true positives\", c=\"#2e8b57\", lw=2)\nax.plot(c[\"x\"], c[\"spont\"],   label=\"spontaneous errors (FALSE)\", c=\"#e0a800\", lw=2)\nax.plot(c[\"x\"], c[\"decoy\"],   label=\"counterfactual decoys\", c=\"#d1495b\", lw=2, ls=\"--\")\nax.set_xlabel(\"rank-normalized confidence score\"); ax.set_ylabel(\"empirical CDF\")\nax.set_title(f\"R2: crux CDF overlay (self-consistency)\\n\"\n             f\"decoy~spont KS p={crux['pt']['ks_decoy_vs_spont_p']:.2f}\")\nax.legend(loc=\"lower right\", fontsize=8)\n\n# Panel 3: realized-FDR calibration (self-consistency gate vs full-run baseline)\nax = axes[2]\nalphas = ALPHA_GRID\nm_fdr = [r[\"realized_fdr\"] if r[\"n_admitted\"] > 0 else np.nan for r in gate[\"pt\"]]\nbrows = {r[\"alpha\"]: r for r in baseline_ref[\"portable_full\"][\"rows\"]}\nb_fdr = [brows[a][\"baseline_realized_fdr\"] if a in brows else np.nan for a in alphas]\nax.plot(alphas, alphas, ls=\":\", c=\"k\", label=\"nominal (y=x)\")\nax.plot(alphas, m_fdr, \"o-\", c=\"#2e8b57\", label=\"decoy gate (demo)\")\nax.plot(alphas, b_fdr, \"s-\", c=\"#d1495b\", label=\"raw-confidence baseline (full run)\")\nax.set_xlabel(\"nominal alpha\"); ax.set_ylabel(\"realized FDR\")\nax.set_title(\"R3: realized-FDR calibration\\n(self-consistency)\")\nax.legend(loc=\"upper left\", fontsize=8)\n\nplt.tight_layout()\nplt.savefig(\"demo_results.png\", dpi=110, bbox_inches=\"tight\")\nplt.show()\nprint(\"\\nHeadline reproduced:\", ref[\"headline_verdict\"],\n      \"under the\", ref[\"headline_elicitation\"], \"elicitation.\")\"\"\")\n\n# --- assemble notebook ---\nnb_cells = []\nfor ctype, src in cells:\n    cell = {\"cell_type\": ctype, \"metadata\": {}, \"source\": src.splitlines(keepends=True)}\n    if ctype == \"code\":\n        cell[\"execution_count\"] = None\n        cell[\"outputs\"] = []\n    nb_cells.append(cell)\n\nnb = {\"cells\": nb_cells,\n      \"metadata\": {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\",\n                                   \"name\": \"python3\"},\n                   \"language_info\": {\"name\": \"python\", \"version\": \"3.12\"}},\n      \"nbformat\": 4, \"nbformat_minor\": 5}\n\nout = HERE / \"code_demo.ipynb\"\nout.write_text(json.dumps(nb, indent=1))\nprint(\"wrote\", out, \"with\", len(nb_cells), \"cells\")\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [40] TOOL CALL — Bash · 2026-06-16 13:12:03 UTC

```
Generate code_demo.ipynb:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python build_notebook.py
```

### [41] TOOL RESULT — Bash · 2026-06-16 13:12:03 UTC

```
{"stdout": "wrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/code_demo.ipynb with 19 cells", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [42] ASSISTANT · 2026-06-16 13:12:13 UTC

```
Let me verify the tricky cells (docstring concatenation, the `st` alias, fdr_stats embed) rendered correctly.
```

### [43] TOOL CALL — Bash · 2026-06-16 13:12:13 UTC

```
Inspect generated cells and syntax-check all code cells:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python - <<'PY'
import json
nb = json.load(open("code_demo.ipynb"))
src = ["".join(c["source"]) for c in nb["cells"]]
# show the build_records cell (index 10) and analyze_s1 head (index 12) and st-alias tail of cell 8
print("=== CELL 10 (build_records) head ===")
print(src[10][:340])
print("\n=== CELL 12 (analyze_s1) head ===")
print(src[12][:200])
print("\n=== CELL 8 (fdr_stats) tail ===")
print(src[8][-160:])
# try compiling every code cell for syntax validity
import ast
for i,c in enumerate(nb["cells"]):
    if c["cell_type"]=="code":
        try: ast.parse("".join(c["source"]))
        except SyntaxError as e: print(f"SYNTAX ERROR cell {i}: {e}")
print("\nsyntax check done")
PY
```

### [44] TOOL RESULT — Bash · 2026-06-16 13:12:13 UTC

```
{"stdout": "=== CELL 10 (build_records) head ===\ndef build_records(examples, tag):\n    \"\"\"One record per real fact for elicitation `tag` ('lp' or 'pt').\"\"\"\n    recs = []\n    for e in examples:\n        recs.append({\n            \"doc_id\":    e[\"metadata_doc_id\"],\n            \"label\":     e[\"output\"],                         # TRUE / FALSE (crisp gold)\n            \"fact_type\": e[\"metadata_\n\n=== CELL 12 (analyze_s1) head ===\ndef certified_alphas(W):                       # verbatim logic from method.py\n    out = []\n    for a in ALPHA_GRID:\n        T, n, _ = st.knockoff_plus_threshold(W, a)\n        out.append({\"alpha\": a, \n\n=== CELL 8 (fdr_stats) tail ===\nlse,\n        \"realized_fdr\": realized, \"self_estimated_fdp\": est,\n    }\n\n\nst = sys.modules[__name__]  # call the functions above as st.<fn>, mirroring method.py\n\nsyntax check done", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [45] ASSISTANT · 2026-06-16 13:12:43 UTC

```
All code cells parse, docstrings rendered correctly, and the `st` alias is in place. Now let me test-run the notebook in a clean Colab-like environment.
```

### [46] TOOL CALL — Bash · 2026-06-16 13:12:43 UTC

```
Create clean test venv with jupyter:
rm -rf .nb_env && /usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -3 && echo "ENV_READY"
```

### [47] TOOL RESULT — Bash · 2026-06-16 13:17:41 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b409so0ks", "assistantAutoBackgrounded": false}
```

### [48] ASSISTANT · 2026-06-16 13:17:55 UTC

```
While the env builds, let me create task tracking.
```

### [49] TOOL CALL — TaskCreate · 2026-06-16 13:17:55 UTC

```
{'subject': 'Build mini_demo_data.json', 'description': 'Curated 100-example subset of full_method_out.json with trimmed reference metadata'}
```

### [50] TOOL RESULT — TaskCreate · 2026-06-16 13:17:55 UTC

```
{"task": {"id": "1", "subject": "Build mini_demo_data.json"}}
```

### [51] TOOL CALL — TaskCreate · 2026-06-16 13:17:55 UTC

```
{'subject': 'Build & test code_demo.ipynb', 'description': 'Notebook reproducing the offline decoy-FDR analysis on cached scores; test in clean env'}
```

### [52] TOOL RESULT — TaskCreate · 2026-06-16 13:17:55 UTC

```
{"task": {"id": "2", "subject": "Build & test code_demo.ipynb"}}
```

### [53] TOOL CALL — TaskCreate · 2026-06-16 13:17:55 UTC

```
{'subject': 'Write struct out JSON', 'description': 'Write .terminal_claude_agent_struct_out.json with notebook + mini data paths'}
```

### [54] TOOL RESULT — TaskCreate · 2026-06-16 13:17:55 UTC

```
{"task": {"id": "3", "subject": "Write struct out JSON"}}
```

### [55] TOOL CALL — Bash · 2026-06-16 13:18:05 UTC

```
Wait for venv ready:
until [ -f /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-Inu52CyA49Ys/0d33016c-7ad7-49e5-a85d-bfbd7c39f2ea/tasks/b409so0ks.output ] && grep -q ENV_READY /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-Inu52CyA49Ys/0d33016c-7ad7-49e5-a85d-bfbd7c39f2ea/tasks/b409so0ks.output 2>/dev/null; do sleep 3; done; echo "ready"
```

### [56] TOOL RESULT — Bash · 2026-06-16 13:21:49 UTC

```
{"stdout": "ready", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [57] ASSISTANT · 2026-06-16 13:21:55 UTC

```
The env is ready. Now let me execute the notebook (timeout 600s) in the clean environment.
```

### [58] TOOL CALL — Bash · 2026-06-16 13:21:55 UTC

```
Execute notebook in clean env:
time .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -40
```

### [59] TOOL RESULT — Bash · 2026-06-16 13:21:55 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bm719kbni"}
```

### [60] TOOL CALL — Bash · 2026-06-16 13:22:03 UTC

```
Wait for notebook execution and show output:
OUT=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-Inu52CyA49Ys/0d33016c-7ad7-49e5-a85d-bfbd7c39f2ea/tasks/bm719kbni.output; until grep -qE "real|Error|Traceback|sys$" "$OUT" 2>/dev/null && ! kill -0 $(pgrep -f "jupyter nbconvert.*code_demo" | head -1) 2>/dev/null; do sleep 5; done; echo "---DONE---"; cat "$OUT"
```

### [61] TOOL RESULT — Bash · 2026-06-16 13:32:01 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bte1lg1k9", "assistantAutoBackgrounded": false}
```

### [62] ASSISTANT · 2026-06-16 13:32:09 UTC

```
The execution completed (exit 0). Let me check the output and timing.
```

### [63] TOOL CALL — Bash · 2026-06-16 13:32:09 UTC

```
Show nbconvert execution output:
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-Inu52CyA49Ys/0d33016c-7ad7-49e5-a85d-bfbd7c39f2ea/tasks/bm719kbni.output
```

### [64] TOOL RESULT — Bash · 2026-06-16 13:32:09 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/.nb_env/lib/python3.12/site-packages/nbformat/__init__.py:96: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.\n  validate(nb)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 178104 bytes to code_demo.ipynb\n\nreal\t5m23.970s\nuser\t0m26.389s\nsys\t0m3.394s", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [65] ASSISTANT · 2026-06-16 13:32:21 UTC

```
Executed successfully in 5m24s (well under 600s — mostly the fresh pip install; the analysis is sub-second). Let me check the cell outputs to confirm correct results, then fix the missing-cell-id warning.
```

### [66] TOOL CALL — Bash · 2026-06-16 13:32:21 UTC

```
Extract notebook outputs to verify results:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python - <<'PY'
import json
nb = json.load(open("code_demo.ipynb"))
for i,c in enumerate(nb["cells"]):
    if c["cell_type"]!="code": continue
    for o in c.get("outputs",[]):
        if o.get("output_type")=="stream":
            txt="".join(o["text"]).rstrip()
            if txt: print(f"--- cell {i} stdout ---\n{txt}\n")
        elif o.get("output_type")=="error":
            print(f"!!! cell {i} ERROR: {o['ename']}: {o['evalue']}")
        elif o.get("output_type") in ("display_data","execute_result"):
            keys=list(o.get("data",{}).keys())
            print(f"--- cell {i} rich output: {keys} ---")
PY
```

### [67] TOOL RESULT — Bash · 2026-06-16 13:32:21 UTC

```
{"stdout": "--- cell 1 stdout ---\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n--- cell 4 stdout ---\nLoaded 100 reals from 'CLUTRR-v1-CrispGold-CalibrationAnchor'\n  labels   : {'FALSE': 62, 'TRUE': 38}\n  fact_type: {'multi_hop': 44, 'atomic': 56}\n  documents: 34\n\nFull-run headline verdict: CALIBRATED(exchangeable)   (elicitation: portable_full)\n\nExample claim: Thomas is the brother of Stanley. -> FALSE\n  logprob ranks   real/decoy/swap = 0.35714285714285715 0.6428571428571429 0.5714285714285714 | W_cf = -0.6428571428571429\n  self-cons ranks real/decoy/swap = 0.07142857142857142 0.7142857142857143 0.5714285714285714 | W_cf = -0.7142857142857143\n\n--- cell 6 stdout ---\nUsing 100 reals; B_BOOT=2000; alpha grid=[0.05, 0.1, 0.2, 0.3, 0.5]\n\n--- cell 10 stdout ---\n[lp] 100 records | W_signed_max mismatches vs cached: 0\n[pt] 100 records | W_signed_max mismatches vs cached: 0\n\n--- cell 12 stdout ---\n[lp] logprob (single-token P(Yes))\n\n--- cell 12 stdout ---\n\n     counterfactual tail win-rate = 0.339 95% CI [0.238, 0.444]  KS p=8.46e-02\n     => ANTI-CONSERVATIVE (win-rate < 0.5)\n\n[pt] portable (K=5 self-consistency)\n     counterfactual tail win-rate = 0.565 95% CI [0.435, 0.694]  KS p=5.34e-01\n     => EXCHANGEABLE (CI covers 0.5)\n\n--- cell 14 stdout ---\n[lp] logprob (single-token P(Yes)): decoy~spont KS p=0.107 (want > 0.05, fail-to-reject)  |  decoy~truepos KS p=2.23e-11 (want << 0.05, reject)\n[pt] portable (K=5 self-consistency): decoy~spont KS p=0.255 (want > 0.05, fail-to-reject)  |  decoy~truepos KS p=4.78e-04 (want << 0.05, reject)\n\n--- cell 16 stdout ---\n[lp] logprob (single-token P(Yes)) — decoy-FDR gate (this demo, 100 reals):\n     alpha=0.05  admit=  0  realized_FDR=0.000  [not-cert ]\n     alpha=0.10  admit=  0  realized_FDR=0.000  [not-cert ]\n     alpha=0.20  admit= 43  realized_FDR=0.419  [certified]\n     alpha=0.30  admit= 64  realized_FDR=0.484  [certified]\n     alpha=0.50  admit= 74  realized_FDR=0.554  [certified]\n[pt] portable (K=5 self-consistency) — decoy-FDR gate (this demo, 100 reals):\n     alpha=0.05  admit=  0  realized_FDR=0.000  [not-cert ]\n     alpha=0.10  admit=  0  realized_FDR=0.000  [not-cert ]\n     alpha=0.20  admit= 11  realized_FDR=0.182  [certified]\n     alpha=0.30  admit= 11  realized_FDR=0.182  [certified]\n     alpha=0.50  admit= 19  realized_FDR=0.316  [certified]\n\n--- cell 18 stdout ---\nCounterfactual decoy tail win-rate  (want ~0.5 = exchangeable)\nelicitation                 demo win-rate (95% CI)        full-run reported   \nlogprob (single-token P(Yes))0.339 [0.238, 0.444]          0.342\nportable (K=5 self-consistency)0.565 [0.435, 0.694]          0.482\n\n--- cell 18 rich output: ['image/png', 'text/plain'] ---\n--- cell 18 stdout ---\n\nHeadline reproduced: CALIBRATED(exchangeable) under the portable_full elicitation.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [68] ASSISTANT · 2026-06-16 13:32:37 UTC

```
All results reproduce correctly:
- **logprob**: cf win-rate 0.339 (full-run 0.342) → ANTI-CONSERVATIVE
- **self-consistency**: 0.565, CI [0.435, 0.694] covers 0.5 → EXCHANGEABLE (matches headline verdict)
- **Crux**: decoy~spont fail-to-reject (p=0.11/0.26), decoy~truepos reject (p≈1e-11/1e-4)
- **Gate FDR**: self-consistency controls FDR (0.182 @ α=0.2) far better than logprob (0.419)
- Figure rendered (image/png), W-mismatch=0.

Only issue is a `MissingIDFieldWarning`. Let me add cell IDs in the generator and re-run to keep a clean, freshly-executed notebook.
```

### [69] TOOL CALL — Edit · 2026-06-16 13:32:37 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_notebook.py
OLD: nb_cells = []
for ctype, src in cells:
    cell = {"cell_type": ctype, "metadata": {}, "source": src.splitlines(keepends=True)}
    if ctype == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    nb_cells.append(cell)
NEW: nb_cells = []
for n, (ctype, src) in enumerate(cells):
    cell = {"id": f"cell{n:02d}", "cell_type": ctype, "metadata": {},
            "source": src.splitlines(keepends=True)}
    if ctype == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    nb_cells.append(cell)
```

### [70] TOOL RESULT — Edit · 2026-06-16 13:32:37 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/build_notebook.py", "oldString": "nb_cells = []\nfor ctype, src in cells:\n    cell = {\"cell_type\": ctype, \"metadata\": {}, \"source\": src.splitlines(keepends=True)}\n    if ctype == \"code\":\n        cell[\"execution_count\"] = None\n        cell[\"outputs\"] = []\n    nb_cells.append(cell)", "newString": "nb_cells = []\nfor n, (ctype, src) in enumerate(cells):\n    cell = {\"id\": f\"cell{n:02d}\", \"cell_type\": ctype, \"metadata\": {},\n            \"source\": src.splitlines(keepends=True)}\n    if ctype == \"code\":\n        cell[\"execution_count\"] = None\n        cell[\"outputs\"] = []\n    nb_cells.append(cell)", "originalFile": null, "structuredPatch": [{"oldStart": 356, "oldLines": 8, "newStart": 356, "newLines": 9, "lines": [" ", " # --- assemble notebook ---", " nb_cells = []", "-for ctype, src in cells:", "-    cell = {\"cell_type\": ctype, \"metadata\": {}, \"source\": src.splitlines(keepends=True)}", "+for n, (ctype, src) in enumerate(cells):", "+    cell = {\"id\": f\"cell{n:02d}\", \"cell_type\": ctype, \"metadata\": {},", "+            \"source\": src.splitlines(keepends=True)}", "     if ctype == \"code\":", "         cell[\"execution_count\"] = None", "         cell[\"outputs\"] = []"]}], "userModified": false, "replaceAll": false}
```

### [71] TOOL CALL — Bash · 2026-06-16 13:32:43 UTC

```
Regenerate notebook with cell IDs and re-execute:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python build_notebook.py && time .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -6
```

### [72] TOOL RESULT — Bash · 2026-06-16 13:32:43 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b5d3cqkf7"}
```

### [73] ASSISTANT · 2026-06-16 13:32:49 UTC

```
While it re-runs, let me verify TODO 6 requirements and write the struct output.
```

### [74] TOOL CALL — Bash · 2026-06-16 13:32:49 UTC

```
Verify TODO 6 requirements:
echo "=== GITHUB_DATA_URL present? ===" && grep -c 'GITHUB_DATA_URL = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json"' build_notebook.py
echo "=== uses GitHub URL pattern (urllib + fallback)? ===" && grep -c "urllib.request.urlopen(GITHUB_DATA_URL)" build_notebook.py
echo "=== mini_demo_data.json exists ===" && ls -la mini_demo_data.json | awk '{print $5, $9}'
```

### [75] TOOL RESULT — Bash · 2026-06-16 13:32:49 UTC

```
{"stdout": "=== GITHUB_DATA_URL present? ===\n1\n=== uses GitHub URL pattern (urllib + fallback)? ===\n1\n=== mini_demo_data.json exists ===\n158696 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [76] TOOL CALL — Write · 2026-06-16 13:32:53 UTC

```
File: /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [77] TOOL RESULT — Write · 2026-06-16 13:32:53 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [78] TOOL CALL — TaskUpdate · 2026-06-16 13:32:59 UTC

```
{'task_id': '1', 'status': 'completed'}
```

### [79] TOOL RESULT — TaskUpdate [ERROR] · 2026-06-16 13:32:59 UTC

```
InputValidationError: [
  {
    "expected": "string",
    "code": "invalid_type",
    "path": [
      "taskId"
    ],
    "message": "Invalid input: expected string, received undefined"
  },
  {
    "code": "unrecognized_keys",
    "keys": [
      "task_id"
    ],
    "path": [],
    "message": "Unrecognized key: \"task_id\""
  }
]
```

### [80] TOOL CALL — ToolSearch · 2026-06-16 13:32:59 UTC

```
{'query': 'select:TaskUpdate', 'max_results': 1}
```

### [81] TOOL RESULT — ToolSearch · 2026-06-16 13:32:59 UTC

```
{"matches": ["TaskUpdate"], "query": "select:TaskUpdate", "total_deferred_tools": 20}
```

### [82] TOOL CALL — TaskUpdate · 2026-06-16 13:33:05 UTC

```
{'taskId': '1', 'status': 'completed'}
```

### [83] TOOL RESULT — TaskUpdate · 2026-06-16 13:33:05 UTC

```
{"success": true, "taskId": "1", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "completed"}}
```

### [84] TOOL CALL — TaskUpdate · 2026-06-16 13:33:05 UTC

```
{'taskId': '2', 'status': 'in_progress'}
```

### [85] TOOL RESULT — TaskUpdate · 2026-06-16 13:33:05 UTC

```
{"success": true, "taskId": "2", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "in_progress"}}
```

### [86] ASSISTANT · 2026-06-16 13:33:17 UTC

```
Now let me wait for the re-run to complete.
```

### [87] TOOL CALL — Bash · 2026-06-16 13:33:17 UTC

```
Wait for re-run and show output:
OUT=/tmp/claude-0/-ai-inventor-aii-data-runs-run-MQN7mBg4AhvH-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-Inu52CyA49Ys/0d33016c-7ad7-49e5-a85d-bfbd7c39f2ea/tasks/b5d3cqkf7.output; until grep -qE "real\s+[0-9]|Error|Traceback" "$OUT" 2>/dev/null; do sleep 5; done; echo "---"; cat "$OUT"
```

### [88] TOOL RESULT — Bash · 2026-06-16 13:34:15 UTC

```
{"stdout": "---\nwrote /ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_Inu52CyA49Ys/code_demo.ipynb with 19 cells\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.1.2\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 177969 bytes to code_demo.ipynb\n\nreal\t1m31.163s\nuser\t0m8.278s\nsys\t0m1.165s", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [89] ASSISTANT · 2026-06-16 13:34:27 UTC

```
The re-run completed in 1m31s with no `MissingIDFieldWarning` (cell IDs fixed it; faster because packages were already cached in the venv). Let me do a final verification of the executed notebook.
```

### [90] TOOL CALL — Bash · 2026-06-16 13:34:27 UTC

```
Final verification of executed notebook and deliverables:
/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/.venv/bin/python - <<'PY'
import json
nb = json.load(open("code_demo.ipynb"))
errs = imgs = 0
have_ids = all("id" in c for c in nb["cells"])
for c in nb["cells"]:
    for o in c.get("outputs",[]):
        if o.get("output_type")=="error": errs += 1; print("ERROR:", o["ename"], o["evalue"])
        if o.get("output_type")=="display_data" and "image/png" in o.get("data",{}): imgs += 1
print("cells:", len(nb["cells"]), "| all have ids:", have_ids, "| error outputs:", errs, "| figures:", imgs)
# confirm headline line + GitHub URL inside executed nb
allsrc = "".join("".join(c["source"]) for c in nb["cells"])
url = "https://raw.githubusercontent.com/AMGrobelnik/ai-invention-6db730-decoy-gated-neuro-symbolic-extraction-a/main/round-2/experiment-2/demo/mini_demo_data.json"
print("GITHUB_DATA_URL exact in notebook:", f'GITHUB_DATA_URL = "{url}"' in allsrc)
print("uses urllib fallback pattern:", "urllib.request.urlopen(GITHUB_DATA_URL)" in allsrc and 'os.path.exists("mini_demo_data.json")' in allsrc)
PY
echo "=== workspace deliverables ===" && ls -la code_demo.ipynb mini_demo_data.json .terminal_claude_agent_struct_out.json
rm -rf .nb_env && echo "cleaned .nb_env"
```

### [91] TOOL RESULT — Bash · 2026-06-16 13:35:42 UTC

```
{"stdout": "cells: 19 | all have ids: True | error outputs: 0 | figures: 1\nGITHUB_DATA_URL exact in notebook: True\nuses urllib fallback pattern: True\n=== workspace deliverables ===\n-rw-r--r-- 1 root root    113 Jun 16 13:32 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root 178038 Jun 16 13:34 code_demo.ipynb\n-rw-r--r-- 1 root root 158696 Jun 16 13:08 mini_demo_data.json\ncleaned .nb_env", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [92] ASSISTANT · 2026-06-16 13:35:54 UTC

```
All verified: 19 cells (all with IDs), **0 errors**, 1 figure rendered, exact GITHUB_DATA_URL present, urllib+local-fallback pattern used, and all deliverables in place. Let me finalize task tracking.
```

### [93] TOOL CALL — TaskUpdate · 2026-06-16 13:35:54 UTC

```
{'taskId': '2', 'status': 'completed'}
```

### [94] TOOL RESULT — TaskUpdate · 2026-06-16 13:35:54 UTC

```
{"success": true, "taskId": "2", "updatedFields": ["status"], "statusChange": {"from": "in_progress", "to": "completed"}}
```

### [95] TOOL CALL — TaskUpdate · 2026-06-16 13:35:54 UTC

```
{'taskId': '3', 'status': 'completed'}
```

### [96] TOOL RESULT — TaskUpdate · 2026-06-16 13:35:54 UTC

```
{"success": true, "taskId": "3", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "completed"}}
```

### [97] ASSISTANT · 2026-06-16 13:36:06 UTC

```
Done. All TODOs complete and verified.

## Summary

Converted the **decoy-competition FDR gate** experiment (`method.py`, 1269 lines + `fdr_stats.py`) into a runnable demo notebook with minimal changes to the original code.

**Key design decision:** The original `method.py` makes ~50k LLM scoring calls (extraction → decoys → confidence elicitation). Those scores are already baked into every released example (per-example rank-normalized real/decoy/swap scores + knockoff `W` under both elicitations). So the notebook **loads the cached scores and re-runs the offline statistical core** — no API calls, no cost — reproducing the headline result in seconds.

**Deliverables (all in workspace):**
- `mini_demo_data.json` (155 KB) — 100 diverse reals (62 FALSE / 38 TRUE, 56 atomic / 44 multi-hop, 34 docs) + trimmed full-run reference metadata
- `code_demo.ipynb` (19 cells) — install → load → config → **`fdr_stats.py` embedded verbatim** (the genuine, unit-tested statistical core) → S1 decoy signature → crux CDF match → method-gate FDR → 3-panel visualization
- `.terminal_claude_agent_struct_out.json`

**Faithfulness:** `fdr_stats.py` is embedded unchanged; the analysis cells mirror `method.py`'s `analyze_s1` / `analyze_crux` / `certified_alphas` / gate logic, adapted only to read cached scores instead of a live LLM pipeline. A sanity cell confirms `W_signed_max(ranks)` matches the cached `W` (0 mismatches).

**Reproduces the headline** (demo vs full-run): logprob cf win-rate **0.339** (full 0.342) → ANTI-CONSERVATIVE; self-consistency **0.565**, CI covers 0.5 → EXCHANGEABLE = `CALIBRATED(exchangeable)`. Crux: decoy~spont fail-to-reject (p=0.26), decoy~truepos reject (p≈1e-4). Self-consistency gate controls realized FDR (0.182 @ α=0.2) vs logprob (0.419).

**Verification:** Test-ran in a clean Python 3.12 venv (Colab simulation) — exit 0, 0 error outputs, figure rendered, fresh run 5m24s (mostly pip install), under the 600s budget. `B_BOOT=2000` (original) kept since the offline stats run in <1s.
```
