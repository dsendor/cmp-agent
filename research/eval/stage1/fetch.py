#!/usr/bin/env python3
"""Assemble the stage 1 triples for dev2 and test2: arXiv v1, the peer review file, and the
accepted version.

    python3 research/eval/stage1/fetch.py            # both sets
    python3 research/eval/stage1/fetch.py --set dev2

The accepted version is, in order of preference:
  1. the last arXiv version, if it was posted on or after the journal's acceptance date;
  2. the journal PDF from nature.com (all dev2 and test2 papers are Nature-family; the
     maintainer approved downloading them, 2026-11-22);
  3. the open-access journal PDF from Europe PMC (found by DOI);
otherwise it is marked missing. Files go to ~/.cache/cmp-assistant/stage1/<arXiv id>/, outside
the repository (papers are not committed); manifest.json here records where each one came from.
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL = HERE.parent
sys.path.insert(0, str(EVAL / "api"))
import providers  # noqa: E402
import run  # noqa: E402

OUT = providers.CACHE / "stage1"
UA = {"User-Agent": "cmp-assistant-eval (research; public papers only)"}
MANIFEST = HERE / "manifest.json"


def get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def arxiv_versions(ids):
    """Latest version and its date for each id, from the arXiv API."""
    out = {}
    for i in range(0, len(ids), 50):
        q = urllib.parse.urlencode({"id_list": ",".join(ids[i:i + 50]), "max_results": 50})
        root = ET.fromstring(get(f"http://export.arxiv.org/api/query?{q}"))
        ns = {"a": "http://www.w3.org/2005/Atom"}
        for e in root.findall("a:entry", ns):
            m = re.search(r"abs/([\d.]+)v(\d+)$", e.find("a:id", ns).text)
            out[m.group(1)] = {"latest": int(m.group(2)), "date": e.find("a:updated", ns).text[:10]}
        time.sleep(3)
    return out


def europepmc(doi):
    q = urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"})
    hits = json.loads(get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{q}"))["resultList"]["result"]
    for h in hits:
        if h.get("pmcid") and h.get("isOpenAccess") == "Y":
            return h["pmcid"]
    return None


def is_pdf(p):
    return p.exists() and p.read_bytes()[:4] == b"%PDF"


def fetch(pid, meta, av):
    d = OUT / pid
    d.mkdir(parents=True, exist_ok=True)
    rec = {"journal": meta["journal"], "doi": meta["doi"], "accepted_date": meta["accepted"]}
    v1 = run.v1_pdf(pid)
    rec["v1"] = str(v1)
    try:
        rec["peer_review"] = str(run.peer_review_pdf(pid))
    except Exception as e:  # noqa: BLE001
        rec["peer_review"] = None
        rec["peer_review_error"] = str(e)[:200]
    acc = d / "accepted.pdf"
    a = av.get(pid)
    if a and a["latest"] > 1 and a["date"] >= meta["accepted"]:
        rec["accepted_source"] = f"arXiv v{a['latest']} ({a['date']})"
        if not is_pdf(acc):
            acc.write_bytes(get(f"https://arxiv.org/pdf/{pid}v{a['latest']}"))
            time.sleep(3)
    elif meta["doi"].startswith("10.1038/"):
        rec["accepted_source"] = "journal PDF (nature.com)"
        if not is_pdf(acc):
            try:
                acc.write_bytes(get(f"https://www.nature.com/articles/{meta['doi'].split('/', 1)[1]}.pdf", timeout=120))
            except Exception as e:  # noqa: BLE001
                rec["accepted_error"] = str(e)[:200]
            time.sleep(2)
    else:
        pmc = europepmc(meta["doi"])
        if pmc:
            rec["accepted_source"] = f"Europe PMC {pmc}"
            if not is_pdf(acc):
                try:
                    acc.write_bytes(get(f"https://europepmc.org/articles/{pmc}?pdf=render", timeout=120))
                except Exception as e:  # noqa: BLE001
                    rec["accepted_error"] = str(e)[:200]
        else:
            rec["accepted_source"] = None
    rec["accepted"] = str(acc) if is_pdf(acc) else None
    if acc.exists() and not is_pdf(acc):
        acc.unlink()
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", choices=["dev2", "test2"])
    a = ap.parse_args()
    split = json.loads((EVAL / "referee" / "split.json").read_text())
    pool = {p["arxiv_id"]: p for p in json.loads((EVAL / "referee" / "pool.json").read_text())["papers"]}
    sets = [a.set] if a.set else ["dev2", "test2"]
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    ids = [pid for s in sets for pid in split[s]]
    av = arxiv_versions(ids)
    for s in sets:
        for pid in split[s]:
            rec = fetch(pid, pool[pid], av)
            rec["set"] = s
            man[pid] = {k: (v.replace(str(Path.home()), "~") if isinstance(v, str) else v) for k, v in rec.items()}
            print(s, pid, "peer review" if rec["peer_review"] else "NO PEER REVIEW",
                  "| accepted:", rec["accepted_source"] if rec["accepted"] else "MISSING", flush=True)
            MANIFEST.write_text(json.dumps(man, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
