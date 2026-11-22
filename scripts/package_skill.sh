#!/usr/bin/env bash
# Build the claude.ai skill bundle: skill-bundle/SKILL.md with the engine prompts, the
# scripts the review needs and the dashboard template, in the layout the scripts expect.
# Install steps for users: claude-ai/README.md.
#
#   bash scripts/package_skill.sh            build, and refresh the committed claude-ai/ zip
#   bash scripts/package_skill.sh --check    fail if the committed zip is out of date
#
# Output: dist/referee-preview/ (not committed) and claude-ai/referee-preview-skill.zip
# (committed, so users can download it). Rerun after changing engine/, the scripts it copies
# or dashboard/template.html.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="$root/dist/referee-preview"
rm -rf "$out" "$root/dist/referee-preview-skill.zip"
mkdir -p "$out/engine" "$out/scripts" "$out/dashboard"
cp "$root/skill-bundle/SKILL.md" "$out/"
cp "$root"/engine/*.md "$root/engine/VERSION" "$out/engine/"
for f in paper_text.py assemble.py check_evidence.py build_dashboard.py arxiv_search.py; do
  cp "$root/scripts/$f" "$out/scripts/"
done
cp "$root/dashboard/template.html" "$out/dashboard/"
cp "$root/LICENSE" "$root/NOTICE" "$out/"
# -X and fixed times keep the zip byte-identical when nothing changed, so --check can compare
find "$out" -exec touch -t 202601010000 {} +
(cd "$root/dist" && zip -qrX referee-preview-skill.zip referee-preview)
if [ "${1:-}" = "--check" ]; then
  cmp -s "$root/dist/referee-preview-skill.zip" "$root/claude-ai/referee-preview-skill.zip" \
    || { echo "claude-ai/referee-preview-skill.zip is out of date: run bash scripts/package_skill.sh"; exit 1; }
  echo "claude-ai/referee-preview-skill.zip is up to date"
else
  cp "$root/dist/referee-preview-skill.zip" "$root/claude-ai/"
  echo "Packaged: $out and claude-ai/referee-preview-skill.zip"
fi
