#!/usr/bin/env python3
"""Build a one-file dashboard from advisor.json and decision.json. Standard library only.

  python3 build_dashboard.py <folder> [--open]

Reads <folder>/advisor.json and <folder>/decision.json (run decide.py first) and writes
<folder>/dashboard.html. The page needs no network and no server: open it from disk.
"""
import html
import json
import sys
import webbrowser
from pathlib import Path

E = lambda s: html.escape(str(s if s is not None else ""))
PARAM_LABEL = {"p_success": "odds of success", "impact": "impact if it works",
               "fallback": "value if it fails", "months": "months of work"}
HEIL = [("what", "What are you trying to do?"), ("today", "How is it done today, and what are the limits?"),
        ("new", "What is new in your approach?"), ("who_cares", "Who cares, if it works?"),
        ("risks", "What are the risks?"), ("cost", "What will it cost?"), ("time", "How long?"),
        ("midterm", "Midterm exam: the first check it is working"), ("final", "Final exam: what success looks like")]

CSS = """
:root{--ink:#1d1d1b;--muted:#5f5d57;--rule:#d9d5cc;--paper:#fbfaf7;--card:#ffffff;
--accent:#9a3b1f;--front:#9a3b1f;--other:#8f8b82;--good:#2f6b3a;--warn:#8a5a00;--bad:#9a2a1f}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);
font:16px/1.55 Charter,"Iowan Old Style",Georgia,serif}
main{max-width:1040px;margin:0 auto;padding:40px 28px 80px}
h1{font-size:34px;line-height:1.15;margin:0 0 6px;font-weight:600}
h2{font-size:22px;margin:44px 0 12px;font-weight:600;border-top:1px solid var(--rule);padding-top:18px}
h3{font-size:19px;margin:0 0 4px}
.sans,table,.tag,.meta,.small,button{font-family:-apple-system,"Helvetica Neue",Arial,sans-serif}
.meta{color:var(--muted);font-size:14px}.small{font-size:13px;color:var(--muted)}
.ai{display:inline-block;font-size:12px;letter-spacing:.02em;padding:2px 8px;border:1px solid var(--accent);
color:var(--accent);border-radius:3px;margin-right:6px}
.you{display:inline-block;font-size:12px;padding:2px 8px;border:1px solid var(--good);color:var(--good);border-radius:3px}
.lead{font-size:20px;line-height:1.45;margin:18px 0}
.callout{background:var(--card);border-left:3px solid var(--accent);padding:14px 18px;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-weight:600;cursor:pointer;white-space:nowrap}th:hover{color:var(--accent)}td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.card{background:var(--card);border:1px solid var(--rule);padding:20px 22px;margin:18px 0}
.tag{display:inline-block;font-size:12px;padding:1px 7px;border-radius:3px;margin:2px 4px 2px 0;background:#f1eee8}
.tag.bad{color:var(--bad)}.tag.good{color:var(--good)}.tag.warn{color:var(--warn)}
dl{margin:8px 0}dt{font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;font-size:13px;color:var(--muted);margin-top:8px}dd{margin:2px 0 0}
details summary{cursor:pointer;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;font-size:14px;color:var(--accent);margin-top:12px}
a{color:var(--accent)}svg text{font-family:-apple-system,"Helvetica Neue",Arial,sans-serif}
.scary{font-weight:600}
"""

JS = """
document.querySelectorAll('table.sort th').forEach(function(th,i){th.addEventListener('click',function(){
var tb=th.closest('table').tBodies[0],rows=[].slice.call(tb.rows),dir=th.dataset.dir==='a'?'d':'a';th.dataset.dir=dir;
rows.sort(function(a,b){var x=a.cells[i].dataset.v||a.cells[i].textContent,y=b.cells[i].dataset.v||b.cells[i].textContent;
var nx=parseFloat(x),ny=parseFloat(y);var c=(!isNaN(nx)&&!isNaN(ny))?nx-ny:x.localeCompare(y);return dir==='a'?c:-c});
rows.forEach(function(r){tb.appendChild(r)})})});
"""


def rng(e, fmt="{:g}"):
    lo, hi = e["low"], e["high"]
    best = e.get("best")
    s = fmt.format(lo) + " to " + fmt.format(hi)
    if best is not None:
        s += " (best " + fmt.format(best) + ")"
    return s


def pct(e):
    return rng({k: (round(100 * v) if isinstance(v, (int, float)) else v) for k, v in e.items()}, "{}%")


def by(e):
    return "" if e.get("by", "researcher") == "researcher" else ' <span class="ai">model\'s guess</span>'


def chart(ideas, dec):
    W, H, L, B, T, R = 640, 400, 56, 46, 16, 20
    pw, ph = W - L - R, H - T - B
    x = lambda p: L + p * pw
    y = lambda v: T + ph - v / 10.0 * ph
    front = set(dec["pareto_front"])
    out = ['<svg viewBox="0 0 %d %d" width="100%%" role="img" aria-label="Odds of success against impact">' % (W, H)]
    for t in range(0, 11, 2):
        out.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#ece8e0"/>' % (L, W - R, y(t), y(t)))
        out.append('<text x="%d" y="%.1f" font-size="11" fill="#5f5d57" text-anchor="end">%d</text>' % (L - 8, y(t) + 4, t))
    for t in range(0, 101, 20):
        out.append('<line y1="%d" y2="%d" x1="%.1f" x2="%.1f" stroke="#ece8e0"/>' % (T, T + ph, x(t / 100), x(t / 100)))
        out.append('<text y="%d" x="%.1f" font-size="11" fill="#5f5d57" text-anchor="middle">%d%%</text>' % (T + ph + 16, x(t / 100), t))
    out.append('<text x="%.1f" y="%d" font-size="12" fill="#1d1d1b" text-anchor="middle">odds of success</text>' % (L + pw / 2, H - 6))
    out.append('<text transform="translate(14,%.1f) rotate(-90)" font-size="12" fill="#1d1d1b" text-anchor="middle">impact if it works (0 to 10)</text>' % (T + ph / 2))
    for i in ideas:
        e = i["estimates"]
        p, im = e["p_success"], e["impact"]
        pm = p.get("best", (p["low"] + p["high"]) / 2)
        imm = im.get("best", (im["low"] + im["high"]) / 2)
        m = e["months"].get("best", (e["months"]["low"] + e["months"]["high"]) / 2)
        col = "#9a3b1f" if i["id"] in front else "#8f8b82"
        r = 4 + min(m, 36) / 36.0 * 12
        out.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s" stroke-opacity=".45"/>' % (x(p["low"]), x(p["high"]), y(imm), y(imm), col))
        out.append('<line y1="%.1f" y2="%.1f" x1="%.1f" x2="%.1f" stroke="%s" stroke-opacity=".45"/>' % (y(im["low"]), y(im["high"]), x(pm), x(pm), col))
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" fill-opacity="%s" stroke="%s"><title>%s</title></circle>'
                   % (x(pm), y(imm), r, col, ".85" if i["id"] in front else ".35", col, E(i["title"])))
        anchor = "end" if pm > 0.7 else "start"
        dx = -(r + 4) if anchor == "end" else r + 4
        out.append('<text x="%.1f" y="%.1f" font-size="12" fill="#1d1d1b" text-anchor="%s">%s</text>'
                   % (x(pm) + dx, y(imm) - 2, anchor, E(i["title"][:42] + ("…" if len(i["title"]) > 42 else ""))))
    out.append("</svg>")
    return "".join(out)


def spark(counts):
    if not counts or not counts.get("per_year"):
        return ""
    ys = sorted(counts["per_year"].items())
    mx = max(v for _, v in ys) or 1
    w, h, bw = 16 * len(ys), 44, 12
    bars = "".join('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="#9a3b1f" fill-opacity=".7"><title>%s: %d</title></rect>'
                   % (k * 16, h - 14 - v / mx * (h - 18), bw, v / mx * (h - 18), yr, v) for k, (yr, v) in enumerate(ys))
    labels = '<text x="0" y="%d" font-size="10" fill="#5f5d57">%s</text><text x="%d" y="%d" font-size="10" fill="#5f5d57" text-anchor="end">%s</text>' % (
        h - 2, ys[0][0], w - 4, h - 2, ys[-1][0])
    total = sum(v for _, v in ys)
    note = " " + E(counts["note"]) if counts.get("note") else ""
    return ('<p class="small">Crowding and momentum: arXiv papers per year matching <code>%s</code> (%d in total).%s '
            'Relative, not a census.</p><svg width="%d" height="%d">%s%s</svg>' % (E(counts.get("query", "")), total, note, w, h, bars, labels))


FLAG_CLASS = {"late_high_risk": "bad", "multiple_miracles": "bad", "past_horizon": "warn",
              "model_estimates": "warn", "early_go_no_go": "good"}


def card(i, d, title):
    e = i["estimates"]
    parts = ['<div class="card" id="%s"><h3>%s</h3><p>%s</p>' % (E(i["id"]), E(i["title"]), E(i.get("summary", "")))]
    parts.append('<p class="small sans">Your estimates: odds %s%s · impact %s%s · if it fails %s%s · %s months%s</p>'
                 % (pct(e["p_success"]), by(e["p_success"]), rng(e["impact"]), by(e["impact"]),
                    rng(e["fallback"]), by(e["fallback"]), rng(e["months"]), by(e["months"])))
    for f in d["flags"]:
        parts.append('<span class="tag %s">%s</span>' % (FLAG_CLASS.get(f["kind"], ""), E(f["text"])))
    a = i.get("assumptions") or []
    if a:
        parts.append('<p class="small sans" style="margin-top:14px"><span class="ai">AI-drafted</span>Assumptions, '
                     'with the risk you gave each (1 likely true, 5 very unlikely) and months until it reads out</p><table><tr><th>Assumption</th><th>About</th><th>Risk</th><th>Reads out</th></tr>')
        for x in sorted(a, key=lambda x: (-x.get("risk", 0), x.get("readout_months", 0))):
            parts.append('<tr%s><td>%s%s</td><td>%s</td><td class="num">%s</td><td class="num">%s mo</td></tr>' % (
                ' class="scary"' if x.get("scariest") else "", E(x["text"]), " (scariest)" if x.get("scariest") else "",
                "nature" if x.get("kind") == "nature" else "our capability", E(x.get("risk", "")), E(x.get("readout_months", ""))))
        parts.append("</table>")
    t = i.get("cheapest_test")
    if t:
        parts.append('<div class="callout"><span class="ai">AI-drafted</span><b>Cheapest test.</b> %s <span class="small">(about %s; resolves %s)</span></div>'
                     % (E(t["text"]), E("%g month%s" % (t["months"], "" if t["months"] == 1 else "s") if t.get("months") is not None else "? months"), E(PARAM_LABEL.get(t.get("resolves"), t.get("resolves", "")))))
    pw = i.get("prior_work")
    if pw:
        parts.append('<p class="small sans" style="margin-top:14px"><span class="ai">AI-found</span>Closest prior work found. '
                     'This is what the search turned up, not proof that nothing closer exists. Searched %s in %s.</p>'
                     % (E(pw.get("searched", "")), E(", ".join(pw.get("sources", [])))))
        if pw.get("closest"):
            parts.append("<table><tr><th>Paper</th><th>Overlap</th><th>Difference</th><th>Similarity</th></tr>")
            for c in pw["closest"]:
                link = c.get("url") or ("https://arxiv.org/abs/" + c["arxiv"] if c.get("arxiv") else "")
                parts.append('<tr><td><a href="%s" target="_blank" rel="noopener">%s</a> <span class="small">(%s)</span></td><td>%s</td><td>%s</td><td class="num">%s/10</td></tr>'
                             % (E(link), E(c["title"]), E(c.get("year", "")), E(c.get("overlap", "")), E(c.get("difference", "")), E(c.get("similarity", ""))))
            parts.append("</table>")
        else:
            parts.append('<p class="small">No close paper turned up in these searches.</p>')
        parts.append(spark(pw.get("counts")))
        if pw.get("queries"):
            parts.append('<details><summary>Queries run</summary><ul class="small">%s</ul></details>'
                         % "".join("<li><code>%s</code></li>" % E(q) for q in pw["queries"]))
    if i.get("inversion"):
        parts.append('<p><span class="ai">AI-drafted</span><b>If it fails:</b> %s</p>' % E(i["inversion"]))
    h = i.get("heilmeier") or {}
    if any(h.get(k) for k, _ in HEIL):
        parts.append("<details><summary>The idea in nine questions (Heilmeier)</summary><dl>%s</dl></details>"
                     % "".join("<dt>%s</dt><dd>%s</dd>" % (E(q), E(h[k])) for k, q in HEIL if h.get(k)))
    parts.append("</div>")
    return "".join(parts)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    folder = Path(args[0])
    adv = json.loads((folder / "advisor.json").read_text())
    dec = json.loads((folder / "decision.json").read_text())
    ideas = {i["id"]: i for i in adv["ideas"]}
    title = {k: v.get("title", k) for k, v in ideas.items()}
    dmap = {d["id"]: d for d in dec["ideas"]}
    who = adv.get("researcher") or {}
    top = dec["top"]

    s = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>Project choice, %s</title><style>%s</style></head><body><main>" % (E(adv.get("created", "")), CSS)]
    s.append('<p class="meta">Project choice · %s%s%s</p><h1>Which project first</h1>' % (
        E(adv.get("created", "")), " · " + E(who["stage"]) if who.get("stage") else "",
        " · %s-month horizon" % E(who["horizon_months"]) if who.get("horizon_months") else ""))
    s.append('<p class="small sans"><span class="you">yours</span> the ideas and the estimates (odds, impact, fallback, months) are yours, '
             'except where marked "model\'s guess". <span class="ai">AI</span> the assumptions, prior-work search, cheapest tests '
             'and questions were drafted by Claude and have not been checked by anyone. The numbers below are computed from your '
             'estimates by a script, not judged by the model.</p>')
    if adv.get("note"):
        s.append('<p class="callout">%s</p>' % E(adv["note"]))

    # Summary
    top_d = dmap[top]
    s.append('<p class="lead">On your own estimates, <b>%s</b> has the highest expected value and comes out on top in %d%% of draws across your ranges.'
             % (E(title[top]), round(100 * top_d["p_top"])))
    s.append(" %s</p>" % ("The pick holds if any one estimate moves by 20%." if dec["robust"] else
                         "It is a close call: %s." % "; ".join("%s's %s %s puts %s on top" % (
                             E(title[f["idea"]]), PARAM_LABEL[f["estimate"]], f["change"], E(title[f["new_top"]])) for f in dec["flips"][:3])))
    v = (dec.get("value_of_information") or [None])[0]
    if v and v["p_changes_pick"] >= 0.1:
        s.append('<div class="callout"><b>The uncertainty that would most change your choice:</b> %s for %s (now %s). '
                 'Knowing it would change the pick %d%% of the time%s.'
                 % (E(v["label"]), E(title[v["idea"]]), E(" to ".join("%g" % x for x in v["range"])), round(100 * v["p_changes_pick"]),
                    ", toward " + E(title[v["new_top"]]) if v.get("new_top") and v["new_top"] != top else ""))
        t = ideas[v["idea"]].get("cheapest_test")
        if t:
            s.append(" The cheapest test drafted for that idea: %s" % E(t["text"]))
        s.append("</div>")
    else:
        s.append('<div class="callout">No single estimate is likely to change your pick: the most informative one '
                 'changes it in under 10% of cases. More information is unlikely to be worth a delay; the open question is '
                 'whether your estimates are right, which is one to take to your PI.</div>')

    s.append("<h2>Odds against impact</h2>")
    s.append('<p class="small sans">Each circle is an idea at your best guess; lines show your ranges; size shows months of work. '
             'Dark circles are the Pareto front: no other idea beats them on both odds and impact. Choosing among them is a matter of '
             'taste and career stage, which is yours to weigh.</p>')
    s.append(chart([ideas[d["id"]] for d in dec["ideas"]], dec))

    s.append("<h2>All ideas</h2><p class=\"small sans\">Click a column to sort. Expected value = odds × impact + (1 − odds) × value if it fails%s, on your 0 to 10 scale.</p>"
             % (", per year of work" if dec["utility"] == "per_year" else ""))
    s.append('<table class="sort"><thead><tr><th>Idea</th><th>Odds</th><th>Impact</th><th>If it fails</th><th>Months</th><th>Expected value</th><th>On top</th><th>Front</th><th>Flags</th></tr></thead><tbody>')
    for d in dec["ideas"]:
        i = ideas[d["id"]]
        e = i["estimates"]
        nflag = sum(1 for f in d["flags"] if not f.get("good"))
        s.append('<tr><td><a href="#%s">%s</a></td><td class="num" data-v="%s">%s</td><td class="num" data-v="%s">%s</td><td class="num" data-v="%s">%s</td>'
                 '<td class="num" data-v="%s">%s</td><td class="num">%.2f</td><td class="num" data-v="%s">%d%%</td><td>%s</td><td class="num">%s</td></tr>'
                 % (E(d["id"]), E(i["title"]), d["mid"]["p_success"], pct(e["p_success"]), d["mid"]["impact"], rng(e["impact"]),
                    d["mid"]["fallback"], rng(e["fallback"]), d["mid"]["months"], rng(e["months"]), d["expected_value"],
                    d["p_top"], round(100 * d["p_top"]), "yes" if d["id"] in dec["pareto_front"] else "", nflag or ""))
    s.append("</tbody></table>")

    s.append("<h2>Each idea</h2>")
    for d in dec["ideas"]:
        s.append(card(ideas[d["id"]], d, title))

    if adv.get("pi_questions"):
        s.append('<h2>Questions to take to your PI</h2><p class="small sans"><span class="ai">AI-drafted</span></p><ol>%s</ol>'
                 % "".join("<li>%s</li>" % E(q) for q in adv["pi_questions"]))

    s.append('<h2>How this was made</h2><p class="small sans">Assumption analysis and the odds-against-impact axes follow Fischbach and Walsh, '
             '"Problem choice and decision trees in science and engineering", Cell 2024, as adapted from Anthropic\'s scientific-problem-selection skill '
             '(Apache-2.0). The two-axis view follows Alon, "How to choose a good scientific problem", Mol Cell 2009. The intake questions are the '
             'Heilmeier Catechism. The prior-work loop is modelled on the literature check in Si et al.\'s AI-Researcher. Expected values, the share of '
             'draws on top, the 20%% robustness check and the value of information are computed by decide.py from %d draws over your ranges '
             '(triangular distributions, seed %d). Total value of perfect information on all estimates: %.2f on your 0 to 10 scale.</p>'
             % (dec["samples"], dec["seed"], dec["evpi"]))
    s.append("<script>%s</script></main></body></html>" % JS)

    dst = folder / "dashboard.html"
    dst.write_text("".join(s))
    print("Wrote " + str(dst))
    if "--open" in sys.argv:
        webbrowser.open(dst.resolve().as_uri())


if __name__ == "__main__":
    main()
