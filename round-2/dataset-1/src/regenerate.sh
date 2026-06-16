#!/usr/bin/env bash
# Deterministic regeneration of the application anchor from the cached raw/
# snapshot. NO network is used here (fetch_sources.py is the only network step
# and only needs re-running to refresh raw/). Seed=42, pinned tool versions.
set -euo pipefail
cd "$(dirname "$0")"
source .venv/bin/activate
export NLTK_DATA="$PWD/raw/nltk_data"
export PYTHONHASHSEED=42

echo "[1/2] build + standardize -> data_out.json (grouped by source corpus)"
python data.py 2>&1 | tail -4
echo "[2/2] verify"
python build/verify_dataset.py 2>&1 | tail -4
