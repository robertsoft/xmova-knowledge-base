#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <manifest.yaml>"
  exit 2
fi
MANIFEST="$1"
PY=$(command -v python3 || command -v python || true)
if [ -z "$PY" ]; then
  echo "Python não encontrado. Instale Python 3." >&2
  exit 2
fi
"$PY" scripts/validate_manifest.py "$MANIFEST"
