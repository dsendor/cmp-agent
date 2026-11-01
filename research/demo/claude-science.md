# Running the lookalike assistant in Claude Science

*AI only. Written 2026-10-23. These steps aren't tested: Claude Science is a desktop app
and this skill was built and run in Claude Code in the cloud. David runs this step and
records the result below.*

Claude Science (beta, macOS, Windows and Linux, Pro, Max, Team and Enterprise plans) is
Anthropic's workbench for scientists. The product page says you can "save any pipeline as
a reusable skill" and "every future session inherits it automatically"
([product page](https://claude.com/product/claude-science),
[announcement](https://www.anthropic.com/news/claude-science-ai-workbench)). Neither page
documents a skill import format, so the steps below try the standard Agent Skills folder
first and fall back to asking the agent to save it.

## 1. Build the package

From the repository root:

```bash
bash research/scripts/package.sh
```

This runs the library check and writes `research/dist/lookalike-assistant/` (with
`SKILL.md`, `report-template.md` and `lookalikes.yaml` side by side) and
`research/dist/lookalike-assistant.zip`.

## 2. Load it

Try these in order and note which worked.

1. **Skills settings.** If Claude Science has a skills or capabilities page with an
   upload or "add skill" button, upload `lookalike-assistant.zip`.
2. **Skills folder.** If it reads skills from a folder (Claude Code uses
   `~/.claude/skills/<name>/SKILL.md`), copy the `lookalike-assistant` folder there and
   restart the app.
3. **Save as a skill from chat.** Start a session in a folder that contains
   `dist/lookalike-assistant/`, then say: "Read `lookalike-assistant/SKILL.md` and the
   two files next to it, and save this as a reusable skill called lookalike-assistant."

## 3. Run it

Start a new session (so the skill loads the way a colleague's would) and say:

> Run the lookalike-assistant skill on arXiv 1710.10701v1. Write the report and the run
> notes as the skill describes.

Use `1710.10701v1` first: the Claude Code report for it is in
`../eval/runs/1710.10701/skill-r1/report.md`, so the two can be compared side by side.

## 4. What to record

| Question | Result |
|---|---|
| Which load route worked (1, 2 or 3)? | |
| Did the skill trigger by name, or did it need the files pasted in? | |
| Could it fetch arXiv abstract pages and PDFs, or did you attach the PDF? | |
| Did it write files (report and run notes), or only reply in chat? | |
| Did the reviewer agent flag anything (citations, quotes)? | |
| Statuses that differ from the Claude Code report | |
| Related-work links: all resolved? | |
| Time from prompt to report | |

## 5. What may not carry over

- **Skill format.** The `name` and `description` frontmatter is the Agent Skills format
  Claude Code uses. Claude Science's curated skills are for life sciences; whether it
  loads a user skill from a file is the open question this demo answers.
- **Connectors.** Its 60+ database connectors are mostly biology and chemistry. arXiv
  access depends on its web tools; the skill only needs plain HTTPS to arxiv.org.
- **File handling.** The skill writes `reports/<id>.md` and `reports/<id>.notes.md`. If
  the app keeps outputs as artifacts, save the report artifact as markdown by hand.
- **Paths.** In the repository the library is at `../library/lookalikes.yaml`; in the
  package it sits next to `SKILL.md`. `SKILL.md` says to look in both places.

## Result

*Not run yet.*
