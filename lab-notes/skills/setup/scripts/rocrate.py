#!/usr/bin/env python3
"""Package figures, the code that made them and the data behind them as an RO-Crate
(https://www.researchobject.org/ro-crate/), ready for a data deposit (Zenodo or an
institutional repository). Standard library only. Uploads nothing.

  rocrate.py build ROOT NAME FIGURE_DIR [FIGURE_DIR ...] [--title T] [--description D]
                   [--license URL] [--label FIGURE_DIR=LABEL ...] [--no-data]
  rocrate.py check CRATE_DIR

ROOT is the lab-record folder. Each FIGURE_DIR is a folder the plot skill wrote
(lab-record/figures/<date>-<slug>/) with figure.png or .pdf, plot.py, data.csv and
figure.json, which names the data the figure used:

  {"title": "...", "sources": [{"type": "qcodes", "path": "data/experiments.db",
                                "run_id": 1, "guid": "..."},
                               {"type": "file", "path": "data/iv.csv"}]}

The crate goes to lab-record/deposits/NAME/. For each figure it records a CreateAction:
this script (instrument), applied to these runs or files (object), made this figure and
CSV (result). Every run in each cited database is listed too, so a run that no figure used
shows up as measured but not shown, and the README says which. Aborted runs say so.
Databases are copied in unless --no-data (then they're referenced by path).
"""
import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qcodes_runs  # noqa: E402

CONTEXT = "https://w3id.org/ro/crate/1.1/context"
CONFORMS = "https://w3id.org/ro/crate/1.1"
CC_BY = "https://creativecommons.org/licenses/by/4.0/"
FORMATS = {".png": "image/png", ".pdf": "application/pdf", ".svg": "image/svg+xml",
           ".csv": "text/csv", ".py": "text/x-python", ".json": "application/json",
           ".db": "application/vnd.sqlite3", ".h5": "application/x-hdf5", ".txt": "text/plain",
           ".md": "text/markdown"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def file_entity(crate, rel, name=None, extra=None):
    full = os.path.join(crate, rel)
    e = {"@id": rel, "@type": "File", "name": name or os.path.basename(rel),
         "encodingFormat": FORMATS.get(os.path.splitext(rel)[1].lower(), "application/octet-stream"),
         "contentSize": str(os.path.getsize(full)),
         "identifier": "sha256:" + sha256(full)}
    e.update(extra or {})
    return e


def build(a):
    root = os.path.abspath(a.root)
    project = os.path.dirname(root)
    crate = os.path.join(root, "deposits", a.name)
    if os.path.exists(crate):
        sys.exit("refusing to overwrite %s; pick another name" % crate)
    labels = {}
    for x in a.label:
        k, v = x.split("=", 1)
        labels[os.path.abspath(k)] = labels[os.path.basename(k.rstrip("/"))] = v
    graph, parts, actions, used_runs, dbs = [], [], [], {}, {}
    graph.append({"@id": "#python", "@type": "ComputerLanguage", "name": "Python",
                  "url": {"@id": "https://www.python.org/"}})

    for fd in a.figures:
        fd = os.path.abspath(fd)
        meta_path = os.path.join(fd, "figure.json")
        meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
        if not meta:
            print("warning: %s has no figure.json; its data sources are unknown" % fd, file=sys.stderr)
        slug = os.path.basename(fd.rstrip("/"))
        dest = os.path.join(crate, "figures", slug)
        shutil.copytree(fd, dest, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
        rels = sorted(os.path.join("figures", slug, f) for f in os.listdir(dest))
        label = labels.get(fd) or labels.get(slug) or meta.get("label")
        title = meta.get("title") or slug
        results, script = [], None
        for r in rels:
            ext = os.path.splitext(r)[1].lower()
            extra = {}
            if r.endswith("plot.py"):
                extra = {"@type": ["File", "SoftwareSourceCode"], "programmingLanguage": {"@id": "#python"},
                         "description": "Makes the figure from the data, with every correction on its own line."}
                script = r
            elif r.endswith("data.csv"):
                extra = {"description": "The numbers plotted, exactly."}
                results.append(r)
            elif ext in (".png", ".pdf", ".svg"):
                extra = {"@type": ["File", "ImageObject"], "name": (label + ": " if label else "") + title}
                results.append(r)
            graph.append(file_entity(crate, r, extra=extra))
            parts.append(r)

        objects = []
        for s in meta.get("sources", []):
            src = s.get("path")
            if not src:
                continue
            full = src if os.path.isabs(src) else os.path.join(project, src)
            in_crate = os.path.join("data", os.path.basename(src))
            if s.get("type") == "qcodes":
                dbs.setdefault(full, in_crate)
                rid = "#%s-run-%s" % (os.path.basename(src), s.get("run_id"))
                used_runs.setdefault(rid, []).append(label or title)
                objects.append({"@id": rid})
            else:
                dbs.setdefault(full, in_crate)
                objects.append({"@id": in_crate if not a.no_data else src})
        act = {"@id": "#make-" + slug, "@type": "CreateAction",
               "name": "Made " + (label or title), "result": [{"@id": r} for r in results],
               "object": objects}
        if script:
            act["instrument"] = {"@id": script}
        if meta.get("corrections"):
            act["description"] = "Corrections: " + "; ".join(meta["corrections"])
        actions.append(act)

    not_shown = []
    for full, in_crate in dbs.items():
        ref = in_crate
        if not os.path.exists(full):
            print("warning: source missing: %s" % full, file=sys.stderr)
            continue
        if a.no_data:
            ref = os.path.relpath(full, project)
            db_ent = {"@id": ref, "@type": "File", "name": os.path.basename(full),
                      "description": "Referenced, not included in this crate.",
                      "identifier": "sha256:" + sha256(full)}
        else:
            os.makedirs(os.path.join(crate, "data"), exist_ok=True)
            # A consistent copy, including anything still in a -wal file; the original is
            # opened read-only.
            if full.endswith(".db"):
                src = qcodes_runs.connect(full)
                import sqlite3
                out = sqlite3.connect(os.path.join(crate, in_crate))
                src.backup(out)
                out.close()
            else:
                shutil.copy2(full, os.path.join(crate, in_crate))
            db_ent = file_entity(crate, in_crate)
            parts.append(in_crate)
        if full.endswith(".db"):
            con = qcodes_runs.connect(full)
            runs = []
            for r in qcodes_runs.run_rows(con):
                s = qcodes_runs.summary(con, r)
                rid = "#%s-run-%s" % (os.path.basename(full), s["run_id"])
                desc = "%s points" % s["points"]
                if s["aborted"]:
                    desc += "; aborted: %s" % (s["exception"] or "not completed")
                if rid not in used_runs:
                    desc += "; not used by any figure in this crate"
                    not_shown.append((rid, s))
                runs.append({"@id": rid, "@type": "Dataset",
                             "name": "Run %s: %s" % (s["run_id"], s["name"]),
                             "identifier": s.get("guid") or str(s["run_id"]),
                             "temporalCoverage": "/".join(x for x in (s.get("started"), s.get("finished")) if x) or None,
                             "description": desc, "isPartOf": {"@id": ref}})
            db_ent["description"] = (db_ent.get("description", "") + " QCoDeS database, %d runs." % len(runs)).strip()
            graph.append(db_ent)
            for r in runs:
                graph.append({k: v for k, v in r.items() if v is not None})
        else:
            graph.append(db_ent)

    title = a.title or a.name
    readme = os.path.join(crate, "README.md")
    lines = ["# " + title, "", a.description or "", "",
             "An [RO-Crate](https://www.researchobject.org/ro-crate/): `ro-crate-metadata.json` says "
             "which data, code and corrections made each figure.", "", "## Figures", ""]
    for act in actions:
        objs = ", ".join(o["@id"].lstrip("#") for o in act["object"]) or "sources not recorded"
        lines.append("- %s, from %s" % (act["name"].replace("Made ", "", 1), objs))
    if not_shown:
        lines += ["", "## Measured but not shown", "",
                  "Runs in the included databases that no figure here uses (%d):" % len(not_shown), ""]
        lines += ["- run %s: %s, %s points%s" % (s["run_id"], s["name"], s["points"],
                                                  "; aborted" if s["aborted"] else "") for _, s in not_shown]
    lines += ["", "Made with lab-notes (AI-assisted); check before publishing.", ""]
    open(readme, "w").write("\n".join(lines))
    graph.append(file_entity(crate, "README.md", extra={"description": "What is in this crate, for people."}))
    parts.append("README.md")

    root_ent = {"@id": "./", "@type": "Dataset", "name": title,
                "description": a.description or "Figures with the code and data that made them.",
                "datePublished": date.today().isoformat(),
                "license": {"@id": a.license}, "hasPart": [{"@id": p} for p in parts],
                "mentions": [{"@id": x["@id"]} for x in actions]}
    meta = {"@id": "ro-crate-metadata.json", "@type": "CreativeWork",
            "conformsTo": {"@id": CONFORMS}, "about": {"@id": "./"}}
    lic = {"@id": a.license, "@type": "CreativeWork", "name": "CC BY 4.0" if a.license == CC_BY else a.license}
    doc = {"@context": CONTEXT, "@graph": [meta, root_ent, lic] + graph + actions}
    json.dump(doc, open(os.path.join(crate, "ro-crate-metadata.json"), "w"), indent=1, ensure_ascii=False)
    problems = check_crate(crate)
    print(json.dumps({"crate": os.path.relpath(crate, project), "figures": len(actions),
                      "runs_not_shown": len(not_shown), "problems": problems}, indent=1))
    return 1 if problems else 0


def check_crate(crate):
    """The structural rules a crate must meet: metadata descriptor, root Dataset, every file
    listed exists (and every file present is listed), every reference resolves."""
    p = []
    doc = json.load(open(os.path.join(crate, "ro-crate-metadata.json")))
    if doc.get("@context") != CONTEXT:
        p.append("@context is not the RO-Crate 1.1 context")
    ents = {e["@id"]: e for e in doc.get("@graph", [])}
    md = ents.get("ro-crate-metadata.json")
    if not md or md.get("about", {}).get("@id") != "./" or md.get("conformsTo", {}).get("@id") != CONFORMS:
        p.append("metadata descriptor missing or wrong")
    rootd = ents.get("./")
    if not rootd or "Dataset" not in str(rootd.get("@type")):
        p.append("root Dataset missing")
        return p
    for k in ("name", "description", "datePublished", "license"):
        if k not in rootd:
            p.append("root Dataset has no %s" % k)
    listed = {x["@id"] for x in rootd.get("hasPart", [])}
    for i in listed:
        if not os.path.exists(os.path.join(crate, i)):
            p.append("listed but missing: %s" % i)
        if i not in ents:
            p.append("listed but not described: %s" % i)
    for dp, _, fs in os.walk(crate):
        for f in fs:
            r = os.path.relpath(os.path.join(dp, f), crate)
            if r != "ro-crate-metadata.json" and r not in listed:
                p.append("present but not listed: %s" % r)

    def refs(v):
        if isinstance(v, dict):
            if set(v) == {"@id"}:
                yield v["@id"]
            else:
                for x in v.values():
                    yield from refs(x)
        elif isinstance(v, list):
            for x in v:
                yield from refs(x)
    for e in doc["@graph"]:
        for k, v in e.items():
            if k in ("@id", "@type", "conformsTo", "url"):
                continue
            for r in refs(v):
                if r not in ents and not r.startswith("http"):
                    p.append("%s.%s points to %s, which isn't described" % (e["@id"], k, r))
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("root"); b.add_argument("name"); b.add_argument("figures", nargs="+")
    b.add_argument("--title"); b.add_argument("--description")
    b.add_argument("--license", default=CC_BY)
    b.add_argument("--label", action="append", default=[], help="FIGURE_DIR=LABEL, e.g. ...=Fig. 2a")
    b.add_argument("--no-data", action="store_true")
    c = sub.add_parser("check"); c.add_argument("crate")
    a = ap.parse_args()
    if a.cmd == "build":
        sys.exit(build(a))
    probs = check_crate(a.crate)
    print("\n".join(probs) or "ok: a valid RO-Crate (structure)")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
