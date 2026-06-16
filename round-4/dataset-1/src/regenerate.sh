#!/usr/bin/env bash
# Deterministic regeneration of the application anchor from the cached raw/
# snapshot. NO network is used here (fetch_sources.py is the only network step
# and only needs re-running to refresh raw/). Seed=42, pinned tool versions ->
# byte-identical data_out.json.
set -euo pipefail
cd "$(dirname "$0")"
source .venv/bin/activate
export NLTK_DATA="$PWD/raw/nltk_data"
export PYTHONHASHSEED=42
export SEED=42

echo "[1/3] build + standardize -> data_out.json + full_data_out.json (grouped by source corpus)"
python data.py 2>&1 | tail -4

echo "[2/3] independent verification (re-parses every input/output string)"
python build/verify_dataset.py 2>&1 | tail -12

echo "[3/3] mini/preview variants"
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
PY="$SKILL_DIR/../.ability_client_venv/bin/python"
if [ -x "$PY" ]; then
  "$PY" "$SKILL_DIR/scripts/aii_json_format_mini_preview.py" --input "$PWD/data_out.json" 2>&1 | tail -4
else
  echo "  (aii-json skill not found; skipping variant generation)"
fi
echo "done."
