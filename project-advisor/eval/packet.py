#!/usr/bin/env python3
"""Make the blind packet: two pages that look alike, labeled A and B at random. Standard library only.

  python3 packet.py baseline.md project-choice/<date> packet/ [--seed N]

Writes:
  packet/A.html, packet/B.html   the plain-prompt answer and the advisor's output, rendered
                                 the same way: same layout, no tool names, no labels, no chart
  packet/papers.md               every arXiv paper either page cites, for the paper check
  packet/key.json                which page is which. Don't open it until the ratings are in.

The advisor's output is rewritten as plain Markdown from advisor.json and decision.json, so
both pages go through the same renderer. Its content is kept in full; only its look goes.
"""
import html
import json
import re
import secrets
import sys
from pathlib import Path

PARAM = {"p_success": "odds of success", "impact": "impact if it works",
         "fallback": "value if it fails", "months": "months of work"}
ARXIV = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])")


def rng(e, pct=False):
    f = (lambda v: "%d%%" % round(100 * v)) if pct else (lambda v: "%g" % v)
    s = "%s to %s" % (f(e["low"]), f(e["high"]))
    return s + (" (best guess %s)" % f(e["best"]) if e.get("best") is not None else "")


def advisor_markdown(folder):
    adv = json.loads((folder / "advisor.json").read_text())
    dec = json.loads((folder / "decision.json").read_text())
    ideas = {i["id"]: i for i in adv["ideas"]}
    t = lambda k: ideas[k].get("title", k)
    top = dec["top"]
    share = {d["id"]: d for d in dec["ideas"]}
    out = ["# Choosing between your ideas", ""]
    out.append("On your own estimates, **%s** has the highest expected value; it comes out on top in "
               "%d%% of draws across your ranges." % (t(top), round(100 * share[top]["p_top"])))
    if dec["robust"]:
        out.append("That holds if any one of your estimates moves by 20%.")
    else:
        out.append("It is a close call: " + "; ".join(
            "%s's %s %s puts %s on top" % (t(f["idea"]), PARAM[f["estimate"]], f["change"], t(f["new_top"]))
            for f in dec["flips"][:3]) + ".")
    v = (dec.get("value_of_information") or [None])[0]
    if v and v["p_changes_pick"] >= 0.1:
        out.append("")
        out.append("The uncertainty that would most change your choice: the %s of %s. Knowing it would "
                   "change the pick %d%% of the time." % (v["label"], t(v["idea"]), round(100 * v["p_changes_pick"])))
        ct = ideas[v["idea"]].get("cheapest_test")
        if ct:
            out.append("The cheapest test for it: " + ct["text"])
    else:
        out.append("")
        out.append("No single estimate is likely to change the pick.")
    out += ["", "## The ideas, by expected value", ""]
    out.append("| Idea | Odds | Impact if it works | Value if it fails | Months | Expected value | On top |")
    out.append("|---|---|---|---|---|---|---|")
    for d in dec["ideas"]:
        e = ideas[d["id"]]["estimates"]
        out.append("| %s | %s | %s | %s | %s | %.2f | %d%% |" % (
            t(d["id"]), rng(e["p_success"], True), rng(e["impact"]), rng(e["fallback"]), rng(e["months"]),
            d["expected_value"], round(100 * d["p_top"])))
    for d in dec["ideas"]:
        i = ideas[d["id"]]
        out += ["", "## " + t(d["id"]), "", i.get("summary", "")]
        for f in d["flags"]:
            out.append("")
            out.append("- " + f["text"])
        if i.get("assumptions"):
            out += ["", "**Assumptions** (risk 1 = very likely true, 5 = very unlikely; months until you'd know):", ""]
            for a in sorted(i["assumptions"], key=lambda a: -a.get("risk", 0)):
                out.append("- %s (%s; risk %s; %s months)%s" % (
                    a["text"], "nature" if a.get("kind") == "nature" else "capability",
                    a.get("risk", "?"), a.get("readout_months", "?"), " Scariest." if a.get("scariest") else ""))
        pw = i.get("prior_work") or {}
        if pw.get("closest"):
            out += ["", "**Closest prior work found:**", ""]
            for c in pw["closest"]:
                out.append("- [%s](https://arxiv.org/abs/%s) (%s). Same: %s Different: %s" % (
                    c["title"], c["arxiv"], c.get("year", ""), c.get("overlap", ""), c.get("difference", "")))
        elif pw:
            out += ["", "No close paper turned up in the searches."]
        cnt = (pw.get("counts") or {}).get("per_year")
        if cnt:
            out += ["", "Papers per year on arXiv on its core terms: " +
                    ", ".join("%s: %d" % kv for kv in sorted(cnt.items())) + "."]
        if i.get("cheapest_test"):
            out += ["", "**Cheapest test:** " + i["cheapest_test"]["text"]]
        if i.get("inversion"):
            out += ["", "**If it fails:** " + i["inversion"]]
    if adv.get("pi_questions"):
        out += ["", "## Questions to take to your PI", ""] + ["- " + q for q in adv["pi_questions"]]
    return "\n".join(out) + "\n"


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"(?<![\"'>])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def render(md):
    """A small Markdown renderer: headings, lists, tables, paragraphs, emphasis, links."""
    out, para, lst, table = [], [], None, []

    def flush():
        nonlocal para, lst, table
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para = []
        if lst:
            out.append("<%s>%s</%s>" % (lst[0], "".join("<li>%s</li>" % inline(x) for x in lst[1]), lst[0]))
            lst = None
        if table:
            rows = [r for r in table if not re.match(r"^\|?\s*:?-{2,}", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            body = "".join("<tr>%s</tr>" % "".join(("<th>%s</th>" if n == 0 else "<td>%s</td>") % inline(c) for c in row)
                           for n, row in enumerate(cells))
            out.append("<table>%s</table>" % body)
            table = []

    for line in md.splitlines():
        s = line.rstrip()
        if s.startswith("```"):
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            flush()
            n = min(len(m.group(1)) + 1, 4)
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
        elif s.lstrip().startswith("|"):
            if para or lst:
                flush()
            table.append(s)
        elif re.match(r"^\s*([-*+]|\d+[.)])\s+", s):
            kind = "ol" if re.match(r"^\s*\d", s) else "ul"
            if para or table:
                flush()
            if lst and lst[0] != kind:
                flush()
            lst = lst or (kind, [])
            lst[1].append(re.sub(r"^\s*([-*+]|\d+[.)])\s+", "", s))
        elif not s.strip():
            flush()
        elif lst and line.startswith(("  ", "\t")):
            lst[1][-1] += " " + s.strip()
        else:
            if lst or table:
                flush()
            para.append(s.strip())
    flush()
    return "\n".join(out)


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Page %s</title><style>
body{margin:0;background:#fbfaf7;color:#1d1d1b;font:16px/1.55 Georgia,serif}
main{max-width:820px;margin:0 auto;padding:40px 28px 80px}
.label{font:600 13px -apple-system,Arial,sans-serif;letter-spacing:.06em;color:#5f5d57}
h1,h2,h3,h4{font-weight:600;line-height:1.25}h1{font-size:28px}h2{font-size:21px;margin-top:32px}
table{border-collapse:collapse;font:14px -apple-system,Arial,sans-serif;margin:12px 0}
th,td{border-bottom:1px solid #d9d5cc;padding:6px 8px;text-align:left;vertical-align:top}
a{color:#3b5a8a}code{font-size:14px}
</style></head><body><main><p class="label">PAGE %s</p>
%s
</main></body></html>"""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        sys.exit(__doc__)
    baseline_md = Path(args[0]).read_text()
    advisor_md = advisor_markdown(Path(args[1]))
    dst = Path(args[2])
    dst.mkdir(parents=True, exist_ok=True)
    if "--seed" in sys.argv:
        import random
        flip = random.Random(int(sys.argv[sys.argv.index("--seed") + 1])).random() < 0.5
    else:
        flip = secrets.randbelow(2) == 1
    pages = {"A": ("advisor", advisor_md), "B": ("plain prompt", baseline_md)}
    if flip:
        pages = {"A": pages["B"], "B": pages["A"]}
    papers = {}
    for label, (_, md) in pages.items():
        (dst / ("%s.html" % label)).write_text(PAGE % (label, label, render(md)))
        for a in ARXIV.findall(md):
            papers.setdefault(a, []).append(label)
    lines = ["# Papers cited on pages A and B", "",
             "For each: does it exist and is it described correctly on the page? Did you already "
             "know it? Is it relevant?", "",
             "| arXiv | Cited on | Exists, described correctly? | Knew it already? | Relevant? |",
             "|---|---|---|---|---|"]
    for a in sorted(papers):
        lines.append("| [%s](https://arxiv.org/abs/%s) | %s | | | |" % (a, a, ", ".join(sorted(set(papers[a])))))
    if not papers:
        lines.append("| (none) | | | | |")
    (dst / "papers.md").write_text("\n".join(lines) + "\n")
    (dst / "key.json").write_text(json.dumps({k: v[0] for k, v in pages.items()}, indent=1) + "\n")
    print("Wrote %s: A.html, B.html, papers.md (%d papers) and key.json. Put key.json away unopened."
          % (dst, len(papers)))


if __name__ == "__main__":
    main()
