---
name: publish
description: Publishes a Referee preview dashboard as a private Claude artifact, so the author can open it on any device or share it with co-authors as a claude.ai link. Uploads the dashboard and the paper's PDF to claude.ai, only after the author says yes. Use when the user asks to publish, share or put the dashboard online, asks for a link to it, or invokes /referee-preview:publish.
---

# Referee preview: publish the dashboard as a Claude artifact

The local `dashboard.html` stays the default. Publishing is the author's choice, because it
sends the review and the paper to claude.ai, which the rest of this plugin never does.

## 1. Check that it can be done

- **The tool.** This needs a tool that publishes artifacts from files, named `publish_files`
  (for example `mcp__claude-artifacts__publish_files`; search your tools for it). If there is
  none, say that publishing needs the Claude desktop app or another client with Claude
  artifacts, and stop. The local dashboard is unaffected.
- **The review.** The review folder the user names, or the most recent
  `referee-preview/*/review.json` under the current directory.

## 2. Ask once

Tell the author, in two or three lines, and wait for a yes:

- what is uploaded: the review and the paper's PDF (`paper.pdf`), to their claude.ai account;
- who sees it: only them, until they share it from the artifact's page on claude.ai;
- that it is the author's call for an unpublished paper, and their co-authors' too.

## 3. Build and publish

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/build_dashboard.py <folder> --artifact
```

This writes `<folder>/artifact/index.html` (the dashboard in hosted mode) and
`<folder>/artifact/paper.pdf`. Publish both with `publish_files`: `index.html` as `index.html`
and `paper.pdf` as `paper.pdf`, title "Referee preview: <paper title>", icon "review". If the
client refuses a path it may not read, ask the user to add the review folder to the session.

To republish after a rebuild, pass the artifact's `slug` and the `version` from the last
publish as `base_version`. Record both in `<folder>/artifact/published.json`
(`{"slug", "version", "url"}`) so a later run can find them.

## 4. Report

Give the link and say, briefly:

- the paper shows in the PDF pane, drawn page by page (an artifact's sandbox blocks the browser's own PDF viewer, so the page uses pdf.js); arXiv links (an earlier version or its supplement) open in
  a new tab, because an artifact cannot show other sites inside the page;
- decisions are kept in each viewer's own browser. Send to Claude shows them as text with a
  Copy button: paste that into Claude Code to apply them, or a co-author sends it back to the
  author;
- to share it, open the link and use Share on claude.ai.
