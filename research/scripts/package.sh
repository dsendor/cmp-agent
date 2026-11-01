#!/usr/bin/env bash
# Build the skill package: one folder (and a zip of it) with SKILL.md, the report
# template, the library and the .mtx reader side by side, the layout Claude Code and
# Claude Science load.
#
#   bash research/scripts/package.sh
#
# Output (generated, not committed): research/dist/lookalike-assistant/ and
# research/dist/lookalike-assistant.zip
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$here/scripts/check.py"
out="$here/dist/lookalike-assistant"
rm -rf "$here/dist"
mkdir -p "$out"
cp "$here/skill/SKILL.md" "$here/skill/report-template.md" "$here/library/lookalikes.yaml" "$here/scripts/read_mtx.py" "$out/"
(cd "$here/dist" && zip -qr lookalike-assistant.zip lookalike-assistant)
echo "Packaged: $out and $here/dist/lookalike-assistant.zip"
