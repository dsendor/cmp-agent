"""Blinding and seeded ordering for judge calls, shared by run.py and score.py.

blind(text) strips what could tell a judge which reviewer wrote a review: model, product
and company names, the assistant's provenance line, and markdown cues (headings, bold and
italics, code ticks, tables, rules, bullet styles). Content is left alone.

shuffled(items, seed) gives the same permutation for the same seed string, so score.py can
map the judge's point ids back to the reviewer's ranks without storing the order.
"""
import hashlib
import random
import re

NAMES = [
    (r"\blookalike assistant\b", "reviewer"),
    (r"\blookalike library(?: version [\d.]+)?\b", "checklist"),
    (r"\b(?:Claude(?: Code| Science)?|Anthropic|Opus|Sonnet|Haiku|Fable|ChatGPT|OpenAI|GPT[-\w.]*|Gemini|Google"
     r"|OpenAIReview|MARG)(?:[ -]?\d+(?:\.\d+)*)?\b", "the reviewer"),
    (r"\b(?:large )?language model\b|\bLLM\b|\bAI (?:assistant|reviewer|model)\b", "the reviewer"),
]
PROVENANCE = re.compile(r"^\s*[*_]*\s*AI only\b.*?(?:\n\s*\n|\Z)", re.S | re.M)


def blind(text):
    t = PROVENANCE.sub("", text)
    for pat, rep in NAMES:
        t = re.sub(pat, rep, t, flags=re.I)
    out = []
    for line in t.splitlines():
        s = line.rstrip()
        if re.fullmatch(r"\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*", s) or re.fullmatch(r"\s*([-*_])\1{2,}\s*", s):
            continue  # table separator or horizontal rule
        s = re.sub(r"^\s{0,3}#{1,6}\s*", "", s)  # heading marks
        if s.strip().startswith("|"):
            s = "; ".join(c.strip() for c in s.strip().strip("|").split("|"))
        s = re.sub(r"^(\s*)[*+•]\s+", r"\1- ", s)  # one bullet style
        s = re.sub(r"(\*\*|__)(.+?)\1", r"\2", s)
        s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", s)
        s = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", r"\1", s)
        s = s.replace("`", "")
        out.append(s)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def shuffled(items, seed):
    rnd = random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:12], 16))
    items = list(items)
    rnd.shuffle(items)
    return items
