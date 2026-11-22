#!/usr/bin/env python3
"""Recheck the pool's pending papers: has a peer review file appeared since the pool was built?

    python3 research/eval/recheck_pending.py              # report only
    python3 research/eval/recheck_pending.py --write      # also move found papers into pool.json

A pending paper has no peer review file yet (eval.md, "Pool"). For each one this looks in two
places, as the pool did: the PMC open-data bucket (when Europe PMC lists a PMC id) and Springer
Nature's static content, MOESM1 to MOESM12. A supplementary PDF counts as the peer review file
when its first page says so. With --write, found papers move from `pending` to `papers` in
referee/pool.json with the file's URL, ready for `split.py --keep --write`, which adds new
post-cutoff papers to the reserve. Needs pdftotext. Standard library otherwise.
"""
import argparse
import json
import re
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = HERE / "referee"
UA = {"User-Agent": "cmp-agent-research/1.0 (pool recheck)"}
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com"


def get(url, head=False, timeout=60):
    req = urllib.request.Request(url, headers=UA, method="HEAD" if head else "GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, (b"" if head else r.read())
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:
        return None, b""


def is_review_file(pdf_bytes):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(pdf_bytes)
        f.flush()
        out = subprocess.run(["pdftotext", "-l", "2", f.name, "-"], capture_output=True, text=True).stdout
    return bool(re.search(r"peer review file|reviewer comments|reviewers' comments|referee", out, re.I))


def pmc_candidates(doi):
    q = urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"})
    st, body = get(f"{EPMC}?{q}")
    if st != 200:
        return None, []
    res = json.loads(body).get("resultList", {}).get("result", [])
    pmcid = next((r.get("pmcid") for r in res if r.get("pmcid")), None)
    if not pmcid:
        return None, []
    st, body = get(f"{BUCKET}/?list-type=2&prefix={pmcid}.")
    keys = re.findall(r"<Key>([^<]*MOESM\d+_ESM\.pdf)</Key>", body.decode(errors="ignore")) if st == 200 else []
    return pmcid, [f"{BUCKET}/{k}" for k in keys]


def springer_candidates(doi):
    m = re.match(r"10\.1038/s(\d{5})-(\d{3})-(\d{5})-", doi)
    if not m:
        return []
    jid, yr, num = m.group(1), "2" + m.group(2), str(int(m.group(3)))
    art = urllib.parse.quote(f"art:{doi}", safe="")
    return [f"https://static-content.springer.com/esm/{art}/MediaObjects/{jid}_{yr}_{num}_MOESM{k}_ESM.pdf"
            for k in range(1, 13)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    pool = json.loads((REF / "pool.json").read_text())
    found, still = [], []
    for r in pool["pending"]:
        url, pmcid = None, None
        if r.get("doi"):
            pmcid, urls = pmc_candidates(r["doi"])
            for u in urls + springer_candidates(r["doi"]):
                st, _ = get(u, head=True)
                time.sleep(0.3)
                if st != 200:
                    continue
                st, body = get(u)
                if st == 200 and body[:4] == b"%PDF" and is_review_file(body):
                    url = u
                    break
        (found if url else still).append((r, url, pmcid))
        print(f"{r['arxiv_id']:12} {r.get('journal', ''):26} {'FOUND ' + url if url else 'none'}", flush=True)
    print(f"\n{len(found)} of {len(pool['pending'])} pending papers now have a peer review file")
    if a.write and found:
        stamp = time.strftime("%Y-%m-%d")
        for r, url, pmcid in found:
            r["peer_review_url"] = url
            r["pmcid"] = pmcid or r.get("pmcid")
            r["flags"] = [f for f in r.get("flags", []) if not f.startswith("not yet in PMC")]
            r["flags"].append(f"peer review file found on recheck {stamp}")
            pool["papers"].append(r)
        ids = {r["arxiv_id"] for r, _, _ in found}
        pool["pending"] = [r for r in pool["pending"] if r["arxiv_id"] not in ids]
        pool["rechecked"] = stamp
        (REF / "pool.json").write_text(json.dumps(pool, indent=1, ensure_ascii=False))
        print("wrote referee/pool.json; next: python3 research/eval/split.py --keep --write")


if __name__ == "__main__":
    main()
