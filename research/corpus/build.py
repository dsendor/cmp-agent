#!/usr/bin/env python3
"""Build the research corpus (DuckDB) from the files in research/.

    pip install -r research/corpus/requirements.txt
    python3 research/corpus/build.py                      # research/corpus/corpus.duckdb
    python3 research/corpus/build.py --parquet DIR        # also export every table as Parquet
    python3 research/corpus/build.py --private            # also load ~/.referee-preview/revisions/

Sources (research/data-plan.md, "Corpus schema"):
  eval/referee/pool.json, candidates.json, papers.json   papers, versions
  eval/referee/split.json, eval/api/sets.json            sets (held-out sets marked frozen)
  eval/referee/<id>/referee.json                         referee concerns and recommendations
  eval/referee/<id>/api/<arm>/r<k>.txt and .judge.*.json reviews, judge verdicts, points
  eval/revisions/*.json                                  public revision records
  eval/jclub/selections.json                             Journal Club for Condensed Matter Physics

The database is rebuilt from scratch every time and is not committed (it is derived). A build
with --private holds unpublished material: never export or commit it.
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent
EVAL = RESEARCH / "eval"
REF = EVAL / "referee"
CUTOFF = "2026-07-01"   # published from here on: after the reviewer models' June 2026 training cutoff
FROZEN = {"test", "test22", "test2"}
LEGACY = {"legacy.assistant": "assistant-r1/report.md", "legacy.plain": "plain/review.txt"}


def load(p):
    return json.loads(p.read_text()) if p.exists() else None


def score_module():
    """eval/api/score.py, for its definition of an eligible concern."""
    spec = importlib.util.spec_from_file_location("score", EVAL / "api" / "score.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def papers_and_versions(db):
    pool = load(REF / "pool.json")
    cand = load(REF / "candidates.json")
    older = load(REF / "papers.json")
    seen = {}
    for name, rows in [("core", pool["papers"]), ("borderline", pool["borderline"]), ("pending", pool["pending"]),
                       ("candidate", cand["candidates"] + cand.get("early_candidates", []))]:
        for r in rows:
            if r["arxiv_id"] not in seen:
                seen[r["arxiv_id"]] = (name, r)
    for r in older["papers"]:   # the 31 papers judged before the pool existed
        if r["id"] not in seen:
            seen[r["id"]] = ("judged-early", {"arxiv_id": r["id"], "title": r.get("title"), "journal": r.get("journal"),
                                               "pub_date": r.get("pub_date")})
    for d in REF.iterdir():     # any paper folder still missing
        if d.is_dir() and d.name not in seen:
            seen[d.name] = ("other", {"arxiv_id": d.name})
    for aid, (name, r) in sorted(seen.items()):
        pub = r.get("pub_date")
        db.execute("INSERT INTO papers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", [
            aid, r.get("title"), r.get("journal"), r.get("doi"), r.get("subfield"), r.get("experimental"),
            r.get("received"), r.get("accepted"), pub, name,
            None if not pub else ("post-cutoff" if pub >= CUTOFF else "early"), r.get("peer_review_url"), "referee-pool"])
        if r.get("v1_date"):
            db.execute("INSERT INTO versions VALUES (?,?,?,?)", [aid, "v1", r["v1_date"], "first"])
        for n, v in enumerate(r.get("later_versions") or [], 2):
            if not isinstance(v, dict):   # candidates.json lists bare dates, in order
                v = {"version": f"v{n}", "date": v}
            kind = "after-acceptance" if r.get("accepted") and v["date"] > r["accepted"] else "before-acceptance"
            db.execute("INSERT INTO versions VALUES (?,?,?,?)", [aid, v["version"], v["date"], kind])
    return set(seen)


def sets(db, known):
    split = load(REF / "split.json")
    rows = set()
    for k, v in split.items():
        if isinstance(v, list):
            rows |= {(k, a) for a in v}
    for k, v in (load(EVAL / "api" / "sets.json") or {}).items():
        if isinstance(v, list):
            rows |= {(k, a) for a in v}
    for name, aid in sorted(rows):
        db.execute("INSERT INTO sets VALUES (?,?,?)", [name, aid, name in FROZEN])
    missing = {a for _, a in rows} - known
    return missing


def concerns(db, score):
    n = 0
    for f in sorted(REF.glob("*/referee.json")):
        aid = f.parent.name
        r = load(f)
        elig = {c["id"] for c in score.eligible(aid)}
        for rnd, key in [(1, "concerns"), (2, "later_concerns")]:
            for c in r.get(key) or []:
                db.execute("INSERT INTO concerns VALUES (?,?,?,?,?,?,?,?,?,?)", [
                    aid, c["id"], rnd, c.get("referees") or [], c.get("category"), c.get("severity"), c.get("summary"),
                    c.get("in_v1"), c.get("response"), rnd == 1 and c["id"] in elig])
                n += 1
        for rec in ((r.get("recommendations") or {}).get("first_round") or []):
            db.execute("INSERT INTO recommendations VALUES (?,?,?,?)",
                       [aid, rec.get("referee"), rec.get("recommendation"), rec.get("explicit")])
    return n


def reviews(db):
    n = 0
    for d in sorted(REF.iterdir()):
        if not d.is_dir():
            continue
        aid = d.name
        arms = [(p.name, p) for p in sorted((d / "api").glob("*")) if p.is_dir() and p.name not in LEGACY]
        arms += [(name, d) for name, rel in LEGACY.items() if (d / rel).exists()]
        for arm, adir in arms:
            if arm in LEGACY:
                runs = {1: d / LEGACY[arm]}
                judges = {(1, jf.name.split(".judge.")[1][:-5]): jf
                          for jf in (d / "api" / arm).glob("r1.judge.*.json")} if (d / "api" / arm).exists() else {}
            else:
                runs = {int(p.stem[1:]): p for p in adir.glob("r*.txt") if p.stem[1:].isdigit()}
                judges = {(int(jf.name.split(".")[0][1:]), jf.name.split(".judge.")[1][:-5]): jf
                          for jf in adir.glob("r*.judge.*.json") if jf.name.split(".")[0][1:].isdigit()}
            for k, rf in sorted(runs.items()):
                rid = f"{aid}/{arm}/r{k}"
                db.execute("INSERT INTO reviews VALUES (?,?,?,?,?)", [rid, aid, arm, k, len(rf.read_text().split())])
                n += 1
                for (jk, judge), jf in judges.items():
                    if jk != k:
                        continue
                    j = load(jf)
                    for m in j.get("matches", []):
                        db.execute("INSERT INTO matches VALUES (?,?,?,?,?)",
                                   [rid, judge, m["concern"], m["verdict"], m.get("fixed_in_v1")])
                    pr = j.get("_points_rank", {})
                    for p in j.get("points", []):
                        db.execute("INSERT INTO points VALUES (?,?,?,?,?,?,?,?)", [
                            rid, judge, p["id"], p.get("quality"), p.get("severity"), pr.get(p["id"]),
                            p.get("matches") or [], p.get("partly") or []])
    return n


def revisions(db, private):
    files = sorted((EVAL / "revisions").glob("*.json"))
    if private:
        files += sorted((Path.home() / ".referee-preview" / "revisions").glob("*.json"))
    n = 0
    for f in files:
        r = load(f)
        if r.get("schema") != "referee-preview/revision@1" or (not r.get("public") and not private):
            continue
        rid = f"{r['old']['id']}--{r['new']['id']}"
        db.execute("INSERT INTO revisions VALUES (?,?,?,?,?,?,?,?)", [
            rid, r["old"]["id"], r["old"].get("arxiv"), r["new"]["id"], r["new"].get("arxiv"), r.get("public"),
            r.get("verdict"), (r.get("metrics") or {}).get("anticipation_rate")])
        for c in r.get("changes", []):
            db.execute("INSERT INTO revision_changes VALUES (?,?,?,?,?,?,?,?)", [
                rid, c["id"], c.get("area"), c.get("kind"), c.get("summary"), (c.get("old_ref") or {}).get("page"),
                (c.get("new_ref") or {}).get("page"), c.get("likely_referee_driven")])
        verdict = {w["id"]: w.get("verdict") for w in r.get("walkthrough", [])}
        for q in r.get("inferred_requests", []):
            db.execute("INSERT INTO inferred_requests VALUES (?,?,?,?,?,?)", [
                rid, q["id"], q.get("title"), q.get("confidence"), q.get("anticipated_by") or [], verdict.get(q["id"])])
        n += 1
    return n


def journal_club(db, known):
    sel = load(EVAL / "jclub" / "selections.json")
    n = 0
    for s in (sel or {}).get("selections", []):
        for aid in s.get("arxiv", []):
            db.execute("INSERT INTO journal_club VALUES (?,?,?,?,?)",
                       [aid, s.get("month"), s.get("doi"), s.get("url"), s.get("topic")])
            if aid not in known:
                db.execute("INSERT INTO papers (arxiv_id, source) VALUES (?, 'journal-club')", [aid])
                known.add(aid)
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(HERE / "corpus.duckdb"))
    ap.add_argument("--parquet")
    ap.add_argument("--private", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    if out.exists():
        out.unlink()
    db = duckdb.connect(str(out))
    db.execute((HERE / "schema.sql").read_text())
    known = papers_and_versions(db)
    missing = sets(db, known)
    nc = concerns(db, score_module())
    nr = reviews(db)
    nrev = revisions(db, a.private)
    nj = journal_club(db, known)
    counts = {t: db.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
              for t in ["papers", "versions", "sets", "recommendations", "concerns", "reviews", "matches", "points",
                        "revisions", "revision_changes", "inferred_requests", "journal_club"]}
    print(f"{out}: " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    if missing:
        print(f"problem: {len(missing)} set members have no paper record: {sorted(missing)[:10]}")
    if a.parquet:
        if a.private:
            sys.exit("--parquet with --private would export unpublished material; build without --private")
        p = Path(a.parquet)
        p.mkdir(parents=True, exist_ok=True)
        for t in counts:
            db.execute(f"COPY {t} TO '{p / (t + '.parquet')}' (FORMAT parquet)")
        print(f"Parquet: {p}")
    db.close()


if __name__ == "__main__":
    main()
