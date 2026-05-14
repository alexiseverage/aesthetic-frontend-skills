#!/usr/bin/env env bash
# doctor.sh — Readiness check for aesthetic-frontend-skills
#
# Usage: bash scripts/doctor.sh
#
# Checks:
#   1. knowledge/aesthetics/ exists at expected path(s)
#   2. The directory is writable
#   3. Lists discovered profiles
#   4. Verifies all required skill files are present

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS="  [OK]"
FAIL="  [FAIL]"
WARN="  [WARN]"
INFO="  [INFO]"

errors=0
warnings=0

echo "aesthetic-frontend-skills — doctor"
echo "==================================="
echo ""

# ── 1. Locate knowledge base ────────────────────────────────────────────────

PROJECT_KB="$REPO_ROOT/knowledge/aesthetics"
GLOBAL_KB="$HOME/.agents/skills/knowledge/aesthetics"

echo "1. Knowledge base"

if [ -d "$PROJECT_KB" ]; then
  echo "$PASS  Project-level path exists: $PROJECT_KB"
  KB_PATH="$PROJECT_KB"
elif [ -d "$GLOBAL_KB" ]; then
  echo "$WARN  Project-level path missing; using global: $GLOBAL_KB"
  echo "       Run: mkdir -p \"$PROJECT_KB\" to create a project-level knowledge base."
  KB_PATH="$GLOBAL_KB"
  warnings=$((warnings + 1))
else
  echo "$FAIL  No knowledge base found."
  echo "       Run: mkdir -p \"$PROJECT_KB\"  (project install)"
  echo "       Or:  mkdir -p \"$GLOBAL_KB\"   (global install)"
  KB_PATH=""
  errors=$((errors + 1))
fi

# ── 2. Writability ──────────────────────────────────────────────────────────

echo ""
echo "2. Write permissions"

if [ -n "$KB_PATH" ]; then
  if [ -w "$KB_PATH" ]; then
    echo "$PASS  $KB_PATH is writable"
  else
    echo "$FAIL  $KB_PATH is not writable"
    errors=$((errors + 1))
  fi
else
  echo "$INFO  Skipped (no knowledge base found)"
fi

# ── 3. Discovered profiles ──────────────────────────────────────────────────

echo ""
echo "3. Discovered profiles"

if [ -n "$KB_PATH" ]; then
  profile_count=0
  while IFS= read -r -d '' profile; do
    echo "$INFO  $(basename "$profile")"
    profile_count=$((profile_count + 1))
  done < <(find "$KB_PATH" -maxdepth 1 -name "*.md" -print0 2>/dev/null | sort -z)

  if [ "$profile_count" -eq 0 ]; then
    echo "$INFO  No profiles found — run aesthetic-research to create the first one."
  else
    echo "$PASS  $profile_count profile(s) found"
  fi
else
  echo "$INFO  Skipped (no knowledge base found)"
fi

# ── 4. Skill files present ──────────────────────────────────────────────────

echo ""
echo "4. Skill files"

skills=(
  "aesthetic-literacy/SKILL.md"
  "aesthetic-literacy/REFERENCES.md"
  "aesthetic-research/SKILL.md"
  "aesthetic-research/REFERENCES.md"
  "aesthetic-research/knowledge/schema.json"
  "image-analysis/SKILL.md"
  "image-analysis/REFERENCES.md"
  "asset-creation/SKILL.md"
  "asset-creation/REFERENCES.md"
  "aesthetic-application/SKILL.md"
  "aesthetic-application/REFERENCES.md"
)

skills_dir="$REPO_ROOT/skills"
for skill_file in "${skills[@]}"; do
  full_path="$skills_dir/$skill_file"
  if [ -f "$full_path" ]; then
    echo "$PASS  skills/$skill_file"
  else
    echo "$FAIL  skills/$skill_file — missing"
    errors=$((errors + 1))
  fi
done

# ── 5. Scripts present ──────────────────────────────────────────────────────

echo ""
echo "5. Scripts"

if [ -f "$REPO_ROOT/scripts/validate_profile.py" ]; then
  echo "$PASS  scripts/validate_profile.py"
else
  echo "$WARN  scripts/validate_profile.py — missing"
  warnings=$((warnings + 1))
fi

# ── Summary ─────────────────────────────────────────────────────────────────

echo ""
echo "==================================="
if [ "$errors" -eq 0 ] && [ "$warnings" -eq 0 ]; then
  echo "All checks passed. Ready to use."
elif [ "$errors" -eq 0 ]; then
  echo "$warnings warning(s), 0 errors. Mostly ready — see warnings above."
else
  echo "$errors error(s), $warnings warning(s). Fix errors before use."
  exit 1
fi
