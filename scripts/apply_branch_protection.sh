#!/usr/bin/env bash
set -euo pipefail

# Script to apply branch protection to `main` using GitHub API.
# Requires: export GITHUB_TOKEN with `repo` scope, and `jq` for pretty output (optional).

REPO="robertsoft/xmova-knowledge-base"
BRANCH="main"

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "ERROR: GITHUB_TOKEN not set. Export GITHUB_TOKEN with repo scope and retry." >&2
  exit 1
fi

payload=$(cat <<JSON
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["ci/build"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
)

echo "Applying branch protection to ${REPO} branch ${BRANCH}..."
resp=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X PUT \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/${REPO}/branches/${BRANCH}/protection \
  -d "${payload}")

status=$(echo "$resp" | sed -n 's/.*HTTP_STATUS:\([0-9]*\)$/\1/p')
body=$(echo "$resp" | sed '/HTTP_STATUS:/d')

if [ "$status" -ge 200 ] && [ "$status" -lt 300 ]; then
  echo "Success: branch protection applied (HTTP $status)"
  if command -v jq >/dev/null 2>&1; then
    echo "$body" | jq .
  else
    echo "$body"
  fi
  exit 0
else
  echo "Failed to apply branch protection (HTTP $status)" >&2
  echo "$body" >&2
  exit 2
fi
