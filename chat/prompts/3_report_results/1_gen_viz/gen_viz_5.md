# gen_viz_5 — report_results

> Phase: `gen_paper_repo` · `gen_viz`
> Run: `run_MQN7mBg4AhvH` — Neuro Symbolic Pipeline
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_viz_5` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 12:56:55 UTC

````
<research_methodology>
Create figures that belong in a top-venue paper.

- Every figure needs a clear takeaway visible at a glance.
- Choose chart types that match the data relationship (comparisons, trends, correlations, distributions).
- Include uncertainty (error bars, confidence intervals) when showing experimental results.
- Keep it clean — no clutter, clear labels with units, readable at print size.
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
Your workspace: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_2_gen_viz/gen_viz_5`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_2_gen_viz/gen_viz_5/`:
GOOD: `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_2_gen_viz/gen_viz_5/file.py`, `/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/4_gen_paper_repo/_2_gen_viz/gen_viz_5/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Generate a publication-quality figure for a top-tier venue research paper that exactly follows the provided specification.

Use the aii-image-gen skill (Gemini 3 Pro Image / Nano Banana Pro) to generate the figure in the aspect ratio from the spec. Be as detailed as possible in your image generation prompt: include all data values, axis labels, ranges, legend entries, preferred colors, and describe where each element should be positioned.

IMPORTANT — Two-phase workflow: explore cheaply at 1K, then finalize at 2K. Create a subfolder `fig5_all/` in your workspace for ALL attempts.

PHASE 1 — Explore at 1K (HARD LIMIT: 5 attempts):
- Generate at `--image-size 1K` (fast and cheap). Save attempts as `fig5_all/fig5_v0_it1.jpg`, `fig5_all/fig5_v0_it2.jpg`, … up to `_it5.jpg`.
- After EACH attempt, read the image back and verify it against the checklist below. If it has issues, regenerate with a corrected prompt.
- Do AT MOST 5 generations in this phase — stop early as soon as one is clean. Then pick the single best 1K attempt (the "chosen base").

PHASE 2 — Finalize at 2K (EXACTLY 2 upscale passes of the chosen base):
- Run EXACTLY TWO generations at `--image-size 2K`, each in edit mode passing the chosen base as the input image (`--edit` the chosen base .jpg). Instruct it to upscale and sharpen while preserving the exact layout, data values, labels, and composition — and to fix any remaining issues from the checklist.
- Save them as `fig5_all/fig5_v0_2k_1.jpg` and `fig5_all/fig5_v0_2k_2.jpg`.
- Read both back, verify both, and choose the better of the two as the final figure.

DELIVERABLE:
- Copy ONLY the chosen final 2K image to your workspace root as: fig5_v0.jpg
- The file `fig5_v0.jpg` is the deliverable — everything in `fig5_all/` is reference only.

Verification checklist (apply after EVERY generation in BOTH phases). Check for:
- Layout issues (e.g. text too close together, figure looks cluttered, elements crammed into corners)
- Overlapping or touching labels, legends, or annotations
- Cut-off or truncated text, axis labels, or titles
- Wrong or missing data values, bars, lines, or data points
- Incorrect axis ranges, tick marks, or scales
- Missing or misplaced legend entries
- Blurry text, unreadable font sizes, or poor contrast
- Wrong font family (MUST be sans-serif like Helvetica/Arial — reject any serif fonts like Times New Roman)

In Phase 1, if ANY issue is found — even minor — regenerate with a corrected prompt (within the 5-attempt limit). Do NOT accept a figure with problems as the chosen base.
</task>

<figure_specification>
Figure ID: fig5
Title: Re-DocRED Operational Wedge and Gold-Free Regime-Diagnostic
Caption: Left: matched-recall precision on 152 Re-DocRED documents (recall ceiling $0.075$). METHOD (knockoff+ $W_i$) and PLAIN (raw $Z_i$) are indistinguishable; CoT and RAG are recall-limited; the wedge is disconfirmed (no point with $\Delta$ CI $>0$). Right: the label-free regime-diagnostic places each anchor/elicitation on (decoy tail win-rate $\times$ base-scorer calibration) and predicts the wedge sign gold-free. Re-DocRED is predicted REDUNDANT (correct). The CLUTRR self-consistency point (win-rate $0.482$) would predict POSITIVE, yet the powered paired diagonal disconfirms it---the marginal diagnostic's blind spot.
Image Generation Description: Two-panel figure, 16:9, white background, sans-serif. LEFT panel: line plot, X-axis 'matched recall' 0.034 to 0.075, Y-axis 'precision' 0.15 to 0.28. METHOD (green solid) points approx: (0.034,0.265),(0.05,0.239),(0.063,0.191),(0.075,0.162). PLAIN (red dashed) nearly identical: (0.034,0.269),(0.05,0.246),(0.063,0.195),(0.075,0.161). CoT (blue dotted) short segment only from 0.034 to 0.051 around 0.25-0.26 then stops (label 'recall-limited, max 0.051'). RAG (purple dotted) single point at (0.034, 0.211) (label 'max 0.034'). Shaded gray band around METHOD-PLAIN difference labeled 'delta CI includes 0 at every recall => DISCONFIRMED'. Title 'Matched-recall wedge (152 docs, recall<=0.075)'. RIGHT panel: 2-axis scatter 'regime map'. X-axis 'decoy tail win-rate' 0 to 0.6 (vertical dashed line at 0.5 labeled 'exchangeable'). Y-axis 'base-scorer calibrated?' shown as two rows 'No' (bottom) and 'Yes' (top). Points (all base-scorer 'No' row here): 'Re-DocRED logprob' at x=0.045 labeled 'predicted NULL / realized null (correct)'; 'CLUTRR verbalized' at x=0.103 labeled 'predicted NEGATIVE'; 'CLUTRR logprob' at x=0.34 labeled 'predicted NEGATIVE'; 'CLUTRR self-consistency' at x=0.482 labeled 'predicted POSITIVE but paired diagonal DISCONFIRMS (blind spot)' drawn as a red-circled point. Title 'Gold-free regime-diagnostic'. Use green for correct predictions, red ring for the over-prediction.
Aspect Ratio: 21:9
Summary: Re-DocRED matched-recall wedge (disconfirmed) and the gold-free regime-diagnostic with its CLUTRR self-consistency blind spot.
</figure_specification>

<critical_requirements>
1. Accurately represent ALL data values described above — include every number mentioned
2. Do NOT invent additional data points beyond what is described
3. Include clear axis labels only if the figure has axes (not for diagrams/flowcharts)
4. FONT: ALL text MUST use sans-serif font (Helvetica/Arial). NO serif fonts (Times New Roman). Always include "Sans-serif font throughout (Helvetica/Arial style, NOT Times New Roman)" in your image generation prompt. This is the #1 most common issue — check it first during verification
5. Publication camera-ready style: white backgrounds, properly formatted axes, no 3D effects/shadows/gradients. Follow aii-image-gen skill for image generation, prompting best practices, and figure type templates
6. TEXT SPACING: Ensure generous spacing between ALL text labels. Labels MUST NOT overlap or touch. Use large readable font sizes (minimum 12pt equivalent). If labels would overlap, stagger them vertically, use leader lines, or abbreviate. For multi-panel figures, add clear padding between panels
7. RESOLUTION: Explore at 1K (Phase 1), then finalize with two 2K upscale passes of the chosen base (Phase 2) — see the two-phase workflow above. Do NOT use 4K. For multi-panel or detail-heavy figures, use wider aspect ratios to give elements room
8. MANDATORY VERIFICATION: After EVERY generation attempt, read the image and check font first (sans-serif?), then layout, data accuracy, and readability. If anything is wrong, regenerate. Do NOT stop at the first attempt
</critical_requirements>


---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "VizExpectedFiles": {
      "description": "Expected output files from viz generation.",
      "properties": {
        "image_path": {
          "description": "Path to the generated figure image file. Example: 'fig1_v0.jpg'",
          "title": "Image Path",
          "type": "string"
        }
      },
      "required": [
        "image_path"
      ],
      "title": "VizExpectedFiles",
      "type": "object"
    }
  },
  "description": "Structured output from viz figure generation agent.",
  "properties": {
    "title": {
      "description": "Short descriptive title for the generated figure (roughly 30-90 characters)",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated figure: what it shows, style, any issues fixed",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/VizExpectedFiles",
      "description": "Output file you created. Must include the generated figure image path."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "VizFigureOutput",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 12:56:55 UTC

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

### [3] SKILL-INPUT — aii-image-gen · 2026-06-16 12:56:59 UTC

The agent loaded the **aii-image-gen** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-image-gen
description: AI image generation and editing via Gemini API (gemini-3-pro-image-preview). Generate and edit images with aspect ratio control, retries, and parallel batch support. Use for research figures, diagrams, illustrations, and any visual content.
---

# Image Generation & Editing (nano_banana)

Generate images via Gemini API through the ability server. The API key lives on the ability server — this skill routes requests through `call_server()`.

## Setup

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-image-gen"
G="$SKILL_DIR/scripts/image_gen_nano_banana.py"
PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

## Generate Image

```bash
$PY $G --prompt "prompt describing the image" --output output.jpg --aspect-ratio 16:9
```

## Edit Image

```bash
$PY $G --edit input.jpg --prompt "Make the background blue" --output edited.jpg
```

**Parameters:**
- `--prompt` / `-p` (required) — image description or edit instruction
- `--output` / `-o` (default: `./generated_image.jpg`) — output file path (always saved as `.jpg`; suffix is forced)
- `--edit` — path to source image for editing (omit for generation)
- `--aspect-ratio` (default: `16:9`) — valid: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- `--image-size` (default: `1K`) — resolution: `1K`, `2K`, `4K`
- `--style neurips` — appends NeurIPS academic style guidance
- `--negative-prompt` — things to exclude from the image
- `--system` — system-level style instruction

## Parallel Batch Generation

Use GNU `parallel` for multiple images:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-image-gen"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
export G="$SKILL_DIR/scripts/image_gen_nano_banana.py"
parallel -j 5 -k --group --will-cite 'eval {}' ::: \
  "\$PY \$G -p \"prompt 1\" -o output_1.jpg --aspect-ratio 21:9" \
  "\$PY \$G -p \"prompt 2\" -o output_2.jpg --aspect-ratio 16:9" \
  "\$PY \$G -p \"prompt 3\" -o output_3.jpg --aspect-ratio 1:1"
```

## Preview

Do **NOT** open generated images in a GUI viewer (`loupe`, `xdg-open`, `eog`,
etc.). This skill is for automated / headless generation (e.g. pipeline figure
steps), and popping image windows clutters the user's desktop. Inspect images
programmatically if needed (read the file, check the returned JSON), not by
opening a viewer.

For interactive, human-curated review of multiple figure variants — where the
user wants to arrow-navigate batches in `loupe` — use the
`amg-iter-image-gen-human` skill instead; loupe-driven review is its job, not
this one's.

## Features

- **Model**: `gemini-3-pro-image-preview` (fallback: `gemini-3.1-flash-image-preview`)
- **Auth**: API key on ability server (routed via `call_server()`)
- **Retries**: 3 attempts with exponential backoff, then fallback model
- **Edit mode**: Edit existing images with text instructions
- **Parallel**: GNU `parallel` with `-j 5` for batch generation
- **Headless**: never auto-opens a viewer (use `amg-iter-image-gen-human` for human review)

## Prompting Tips

- Include ALL numeric values explicitly (axis ranges, bar values, labels)
- Specify colors, fonts, layout, and what to exclude
- Use `--style neurips` for academic papers
- For data figures: list every data point, axis label, legend entry
- 1K resolution is default and most reliable

## Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| `21:9` | Ultra-wide panoramic (presentations) |
| `16:9` | Wide (slides, video) |
| `4:3` | Standard |
| `1:1` | Square (social, heatmaps) |
| `9:16` | Vertical (stories, posters) |

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
