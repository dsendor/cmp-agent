#!/usr/bin/env python3
"""Search arXiv for prior work on a research idea, and count papers per year. Standard library only.

  python3 search.py papers QUERY [--max 15] [--cat cond-mat]      closest papers, as JSON
  python3 search.py counts QUERY [--from 2019] [--to 2026] [--cat cond-mat]
                                                                  papers per year, as JSON

QUERY uses arXiv's search syntax (https://info.arxiv.org/help/api/user-manual.html):
  'abs:"twisted bilayer" AND abs:"thermal conductance"'
  '(abs:moire OR abs:"moiré" OR abs:"magic-angle") AND abs:nanoSQUID'
Spell out synonyms and both spellings: arXiv matches words, not meanings.

The arXiv API asks for at most one request every 3 seconds; this script waits between calls
and retries a failed call twice. Counts are what the arXiv API reports and are useful
relative to each other (this idea against that one, this year against last), not as a
census of the field.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
WAIT = 3.1
_last = [0.0]


def _get(params):
    url = API + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)
    for attempt in range(3):
        delay = WAIT - (time.time() - _last[0])
        if delay > 0:
            time.sleep(delay)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "cmp-agent-project-advisor/0.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                root = ET.fromstring(r.read())
        except Exception as e:  # network or parse failure
            err = str(e)
        else:
            entries = root.findall("a:entry", NS)
            # The API reports its own failures as a single entry titled "Error".
            if len(entries) == 1 and (entries[0].findtext("a:title", "", NS).strip() == "Error"):
                err = entries[0].findtext("a:summary", "", NS).strip()
            else:
                return root
        time.sleep(WAIT * (attempt + 2))
    raise SystemExit("arXiv API failed for %r: %s" % (params.get("search_query"), err))


def _scoped(query, cat):
    return "(%s) AND cat:%s*" % (query, cat) if cat else query


def _clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


def papers(query, n=15, cat=None):
    root = _get({"search_query": _scoped(query, cat), "start": 0, "max_results": n,
                 "sortBy": "relevance", "sortOrder": "descending"})
    out = []
    for e in root.findall("a:entry", NS):
        arxiv_id = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1]
        out.append({
            "arxiv": re.sub(r"v\d+$", "", arxiv_id),
            "url": "https://arxiv.org/abs/" + re.sub(r"v\d+$", "", arxiv_id),
            "title": _clean(e.findtext("a:title", "", NS)),
            "year": int(e.findtext("a:published", "0000", NS)[:4]),
            "first_author": _clean(e.findtext("a:author/a:name", "", NS)),
            "n_authors": len(e.findall("a:author", NS)),
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "abstract": _clean(e.findtext("a:summary", "", NS)),
        })
    return {"source": "arXiv API", "query": query, "category": cat,
            "searched": time.strftime("%Y-%m-%d"), "papers": out}


def counts(query, y0=2019, y1=None, cat=None):
    y1 = y1 or int(time.strftime("%Y"))
    years = {}
    for y in range(y0, y1 + 1):
        q = "(%s) AND submittedDate:[%d01010000 TO %d12312359]" % (_scoped(query, cat), y, y)
        # max_results=0 makes the API fail; ask for one result and read the total.
        root = _get({"search_query": q, "start": 0, "max_results": 1})
        years[str(y)] = int(root.findtext("o:totalResults", "0", NS))
    note = None
    if y1 == int(time.strftime("%Y")):
        note = "%d is a partial year (to %s)." % (y1, time.strftime("%Y-%m-%d"))
    return {"source": "arXiv API", "query": query, "category": cat,
            "searched": time.strftime("%Y-%m-%d"), "per_year": years, "note": note}


def main():
    args, opts = [], {}
    it = iter(sys.argv[1:])
    for a in it:
        if a.startswith("--"):
            opts[a[2:]] = next(it, None)
        else:
            args.append(a)
    if len(args) != 2 or args[0] not in ("papers", "counts"):
        sys.exit(__doc__)
    mode, query = args
    cat = opts.get("cat")
    if mode == "papers":
        res = papers(query, int(opts.get("max") or 15), cat)
    else:
        res = counts(query, int(opts.get("from") or 2019),
                     int(opts["to"]) if opts.get("to") else None, cat)
    json.dump(res, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
