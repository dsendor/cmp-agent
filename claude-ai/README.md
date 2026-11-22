# Referee preview in claude.ai (no Claude Code needed)

Referee preview reviews a condensed matter physics paper the way journal referees will, and
gives you a dashboard to work through every likely objection. This page is for running it in
the ordinary Claude app or website. Everything it produces is AI-generated.

## Install (about 2 minutes, once)

1. **Download the skill:**
   [referee-preview-skill.zip](https://github.com/dsendor/cmp-agent/raw/main/claude-ai/referee-preview-skill.zip).
   Don't unzip it.
2. **Turn on file creation.** In Claude, open **Settings > Capabilities** and switch on
   **Code execution and file creation** (in newer layouts it is called **Create and edit
   files**). On a Team or Enterprise plan, an admin turns this on, along with **Skills**, in
   Organization settings.
3. **Upload the skill.** Open **Customize > Skills**, click **+**, then **Create skill**, then
   **Upload a skill**, and choose the zip. It is private to your account.

If you don't see Skills or the upload option, your plan or organization may not include
custom skills yet.

## Use

Start a new chat, attach your paper's PDF (and the supplement, if it is a separate file), and
paste:

> Run a referee preview on this paper. The target journal is ___ (or: no target journal).

For a more thorough review (slower, uses more of your plan), add: "Make it a thorough review."

Claude reads the paper several times, so a review takes a while and uses your plan's usage.
When it finishes, download **dashboard.html** and open it in your browser. If your paper is not
on arXiv, also download **paper.pdf** and keep the two files in the same folder, so the paper
shows beside the review.

In the dashboard, **Start here** shows what the paper does well, the major points and where
the paper sits in the literature. Your decisions on each item are saved in that browser.

You can keep asking in the same chat: "Is item S03 right?", "Which must-address items does
the paper already answer?", "We already say this on page 4: check it."

## Good to know

- This is a basic version: one Claude does every part of the review in turn. The Claude Code
  plugin (main [README](../README.md)) runs independent reviews in parallel, can apply your
  decisions to your LaTeX source, and publishes the dashboard as a shareable link.
- The novelty check searches arXiv, which needs network access in the sandbox. If it can't
  connect, Claude uses web search instead or skips that part and says so.
- Your paper goes only to Claude, as in any chat.
- Problems or ideas: [open an issue](https://github.com/dsendor/cmp-agent/issues) or tell the
  person who sent you this.
