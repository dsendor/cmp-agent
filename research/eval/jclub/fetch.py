#!/usr/bin/env python3
"""List the papers the Journal Club for Condensed Matter Physics recommended, with their
commentaries' DOIs. Links and identifiers only: the commentaries carry no licence (checked
2026-11-22: none on the site, and no licence in their Crossref metadata), so no commentary
text is stored.

    python3 research/eval/jclub/fetch.py --months 12     # writes research/eval/jclub/selections.json

Standard library only. Walks the site's pages from the newest until a commentary is older than
the window. Recommended papers without an arXiv identifier are kept as `other` links.
"""
import argparse
import datetime
import html
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = "https://www.condmatjclub.org"
UA = {"User-Agent": "cmp-agent-research/1.0 (journal club index)"}
MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                      "September", "October", "November", "December"], 1)}


def page(n):
    url = SITE + ("/" if n == 1 else f"/page/{n}/")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="ignore")


def posts(text):
    for p in re.split(r'<div class="post', text)[1:]:
        doi = re.search(r"10\.36471/(JCCM_([A-Za-z]+)_(\d{4})_(\d+))", p)
        if not doi:
            continue
        title = re.search(r"<h2[^>]*>\s*<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", p, re.S)
        arxiv = sorted(set(re.findall(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", p)))
        other = sorted(set(u for u in re.findall(r'href="(https?://(?:doi\.org|dx\.doi\.org)/[^"]+)"', p)
                           if "10.36471" not in u and "10.48550" not in u))
        yield {"doi": "10.36471/" + doi.group(1), "month": f"{doi.group(3)}-{MONTHS[doi.group(2)]:02d}",
               "url": title.group(1) if title else None,
               "topic": html.unescape(re.sub(r"<[^>]+>", "", title.group(2))).strip() if title else None,
               "arxiv": arxiv, "other": other}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=12)
    a = ap.parse_args()
    today = datetime.date.today()
    y, m = today.year, today.month - a.months
    while m <= 0:
        y, m = y - 1, m + 12
    since = f"{y}-{m:02d}"
    out, seen, n = [], set(), 1
    while True:
        batch = list(posts(page(n)))
        if not batch:
            break
        for p in batch:
            if p["month"] >= since and p["doi"] not in seen:
                out.append(p)
                seen.add(p["doi"])
        if min(p["month"] for p in batch) < since:
            break
        n += 1
        time.sleep(1)
    out.sort(key=lambda p: (p["month"], p["doi"]), reverse=True)
    res = {"source": SITE, "fetched": today.isoformat(), "since": since,
           "licence": "None stated (site and Crossref metadata, checked 2026-11-22): store links and DOIs only.",
           "selections": out}
    (HERE / "selections.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    n_ax = sum(len(p["arxiv"]) for p in out)
    print(f"{len(out)} commentaries since {since}; {n_ax} arXiv papers; "
          f"{sum(1 for p in out if not p['arxiv'])} commentaries without an arXiv paper")


if __name__ == "__main__":
    main()
