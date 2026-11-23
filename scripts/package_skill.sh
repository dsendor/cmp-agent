#!/usr/bin/env bash
# Build the claude.ai plugin: skill-bundle/SKILL.md with the engine prompts, the scripts the
# review needs and the dashboard template, in the layout the scripts expect.
# Install steps for users: claude-ai/README.md.
#
#   bash scripts/package_skill.sh            build, and refresh the committed claude-ai/ zip
#   bash scripts/package_skill.sh --check    fail if the committed zip is out of date
#
# Output: dist/referee-preview-claude-ai/ (not committed) and claude-ai/referee-preview-skill.zip
# (committed, so users can download it). Rerun after changing engine/, the scripts it copies
# or dashboard/template.html.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
# A plugin layout: .claude-plugin/plugin.json at the top of the zip, the skill under
# skills/referee-preview/. Some claude.ai uploaders reject a zip whose SKILL.md sits in a folder.
# The plugin has its own name so it does not shadow the Claude Code plugin, referee-preview.
out="$root/dist/referee-preview-claude-ai"
skill="$out/skills/referee-preview"
rm -rf "$root/dist/referee-preview" "$out" "$root/dist/referee-preview-skill.zip"
mkdir -p "$out/.claude-plugin" "$skill/engine" "$skill/scripts" "$skill/dashboard"
version="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['version'])" "$root/.claude-plugin/plugin.json")"
cat > "$out/.claude-plugin/plugin.json" <<JSON
{
  "name": "referee-preview-claude-ai",
  "displayName": "Referee preview (claude.ai)",
  "version": "$version",
  "description": "Reviews a condensed matter physics paper the way journal referees will and makes a one-file dashboard of every likely objection: science, presentation, novelty against prior work, and copy. The claude.ai version of the referee-preview Claude Code plugin. AI-generated.",
  "author": {"name": "David Sendor"},
  "license": "Apache-2.0",
  "repository": "https://github.com/dsendor/cmp-agent",
  "homepage": "https://github.com/dsendor/cmp-agent/tree/main/claude-ai"
}
JSON
cp "$root/skill-bundle/SKILL.md" "$skill/"
cp "$root"/engine/*.md "$root/engine/VERSION" "$skill/engine/"
for f in paper_text.py assemble.py check_evidence.py build_dashboard.py arxiv_search.py; do
  cp "$root/scripts/$f" "$skill/scripts/"
done
cp "$root/dashboard/template.html" "$skill/dashboard/"
cp "$root/LICENSE" "$root/NOTICE" "$out/"
# -X and fixed times keep the zip byte-identical when nothing changed, so --check can compare
find "$out" -exec touch -t 202601010000 {} +
(cd "$out" && zip -qrX "$root/dist/referee-preview-skill.zip" .claude-plugin skills LICENSE NOTICE)
if [ "${1:-}" = "--check" ]; then
  cmp -s "$root/dist/referee-preview-skill.zip" "$root/claude-ai/referee-preview-skill.zip" \
    || { echo "claude-ai/referee-preview-skill.zip is out of date: run bash scripts/package_skill.sh"; exit 1; }
  echo "claude-ai/referee-preview-skill.zip is up to date"
else
  cp "$root/dist/referee-preview-skill.zip" "$root/claude-ai/"
  echo "Packaged: $out and claude-ai/referee-preview-skill.zip"
fi
