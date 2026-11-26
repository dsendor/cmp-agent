# The plain prompt

Paste this in a fresh Claude Code session with no plugins enabled, then paste the contents of
`dictation.md` directly below it. Use the same model as the advisor session. Don't add
anything else.

```text
I'm a physicist choosing which research project to work on next. Below are my ideas, my
career stage, how much time I have and my setup. Help me choose between these. Where it
helps, point me to relevant prior work with arXiv links.
```

The last sentence is there so the comparison is fair: the advisor searches the literature,
and a researcher who wanted that would ask for it. The plain prompt may search the web if
the session allows it; note whether it did.
