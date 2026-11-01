#!/usr/bin/env python3
"""Check back on the new test papers: new arXiv versions, publication, and replies.

    python3 research/scripts/followup.py            # all papers in eval/papers.yaml "new"
    python3 research/scripts/followup.py 2607.09511 # one or more IDs

For each paper it prints the latest arXiv version and its comments field (authors often
note corrections there), the journal DOI and venue if OpenAlex knows one, how many works cite
it, and any citing work whose title suggests a comment, reply, erratum, correction or
retraction. Compare the output with eval/followup.md, which records the state on the day
the reports were written, and with the physicist's ratings in eval/ratings/.

Needs network access to export.arxiv.org and api.openalex.org (no keys). Plain Python and
PyYAML.
"""
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORDS = re.compile(r"\b(comment|reply|response|erratum|correction|corrigendum|retract|matters arising|revisit)", re.I)
UA = {"User-Agent": "cmp-assistant-followup"}


def get(url, tries=3):
    """Fetch a URL, backing off on rate limits (HTTP 429)."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read().decode("utf8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def arxiv(arxiv_id):
    xml = get(f"https://export.arxiv.org/api/query?id_list={arxiv_id}")
    entry = xml.split("<entry>")[1] if "<entry>" in xml else ""
    latest = re.search(r"<id>http://arxiv.org/abs/[^<]*?(v\d+)</id>", entry)
    comment = re.search(r"<arxiv:comment[^>]*>(.*?)</arxiv:comment>", entry, re.S)
    doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", entry)
    return {
        "latest_version": latest.group(1) if latest else "?",
        "comment": " ".join(comment.group(1).split()) if comment else "",
        "doi": doi.group(1) if doi else "",
    }


def openalex(arxiv_id, doi):
    if doi:
        url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}"
    else:
        url = f"https://api.openalex.org/works/doi:10.48550/arXiv.{arxiv_id}"
    try:
        work = json.loads(get(url))
    except Exception:
        return None
    out = {
        "venue": ((work.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
        "doi": work.get("doi") or "",
        "cited_by": work.get("cited_by_count", 0),
        "flagged": [],
    }
    if out["cited_by"]:
        oid = work["id"].rsplit("/", 1)[-1]
        try:
            citing = json.loads(get(f"https://api.openalex.org/works?filter=cites:{oid}&per-page=200"))
        except Exception as e:
            out["flagged"].append(f"citing works not checked ({e}); rerun later")
            return out
        for w in citing.get("results", []):
            if WORDS.search(w.get("title") or ""):
                out["flagged"].append(f"{w.get('title')} ({w.get('doi') or w.get('id')})")
    return out


if __name__ == "__main__":
    ids = sys.argv[1:] or [p["id"] for p in yaml.safe_load((ROOT / "eval" / "papers.yaml").read_text())["new"]]
    for arxiv_id in ids:
        a = arxiv(arxiv_id)
        time.sleep(3)
        o = openalex(arxiv_id, a["doi"])
        print(f"## {arxiv_id}")
        print(f"- latest arXiv version: {a['latest_version']}; comments: {a['comment'] or 'none'}")
        if o:
            print(f"- venue: {o['venue'] or 'not known'}; DOI: {o['doi'] or a['doi'] or 'none'}; cited by {o['cited_by']}")
            for f in o["flagged"]:
                print(f"- citing work to read: {f}")
        else:
            print("- OpenAlex has no record yet")
        print()
