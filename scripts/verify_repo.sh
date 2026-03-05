#!/usr/bin/env bash
set -euo pipefail

required=(LICENSE README.md CODE_OF_CONDUCT.md .cursorrules .github/CODEOWNERS .github/agents/xmova-expert.md)
missing=0
for f in "${required[@]}"; do
  if [ ! -e "$f" ]; then
    echo "MISSING: $f"
    missing=1
  fi
done

if [ $missing -eq 1 ]; then
  echo "Repository structure verification failed." >&2
  exit 2
fi

echo "Repository structure OK."
exit 0
