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
# Optionally validate example manifests if present
if [ -x "scripts/validate_manifest.sh" ]; then
  if [ -e "examples/starter-templates/manifest-example.yaml" ]; then
    echo "Validating example manifest..."
    scripts/validate_manifest.sh examples/starter-templates/manifest-example.yaml || exit 3
  fi
fi

exit 0
