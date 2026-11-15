#!/usr/bin/env python3
"""Read a QCoDeS database without QCoDeS and without touching it.

The database is opened read-only (sqlite URI mode=ro). Nothing is ever written.

  qcodes_runs.py list  DB [--since YYYY-MM-DD] [--json]
  qcodes_runs.py show  DB RUN_ID [--json]
  qcodes_runs.py diff  DB RUN_A RUN_B [--json]
  qcodes_runs.py get   DB RUN_ID FIELD          (FIELD: instrument.param, or name,
                                               sample_name, experiment, completed, points,
                                               started, finished, guid)
  qcodes_runs.py copy  DB [--to DIR]           make a consistent copy (default: a new temp
                                               folder) and print its path. Give QCoDeS or the
                                               lab's loader the copy, never the original: they
                                               open it read-write and can upgrade it in place.

Exit codes: 0 ok, 1 not found, 2 bad input.
"""
import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone


def connect(path):
    """Open read-only. QCoDeS uses WAL mode; a copied database without its -wal/-shm files
    can't be opened with mode=ro alone, so fall back to immutable=1 (no locks, no writes)."""
    from urllib.parse import quote
    if not os.path.isfile(path):
        sys.exit("no such file: %s" % path)
    err = None
    for opts in ("mode=ro", "mode=ro&immutable=1"):
        try:
            con = sqlite3.connect("file:%s?%s" % (quote(os.path.abspath(path)), opts), uri=True)
            con.row_factory = sqlite3.Row
            con.execute("select 1 from runs limit 1")
            return con
        except sqlite3.Error as e:
            err = e
    sys.exit("not a readable QCoDeS database: %s (%s)" % (path, err))


def columns(con, table):
    return {r[1] for r in con.execute("pragma table_info(%s)" % table)}


def ts(x):
    if x is None:
        return None
    try:
        return datetime.fromtimestamp(float(x), tz=timezone.utc).isoformat()
    except (TypeError, ValueError):
        return str(x)


def run_rows(con):
    rc = columns(con, "runs")
    ec = columns(con, "experiments") if con.execute(
        "select name from sqlite_master where name='experiments'").fetchone() else set()
    sel = ["r.run_id", "r.name", "r.result_table_name", "r.run_timestamp",
           "r.completed_timestamp"]
    for c in ("guid", "is_completed", "captured_run_id", "exp_id", "measurement_exception"):
        if c in rc:
            sel.append("r." + c)
    join = ""
    if ec and "exp_id" in rc:
        sel += ["e.name as experiment", "e.sample_name as sample_name"]
        join = " left join experiments e on e.exp_id = r.exp_id"
    return con.execute("select %s from runs r%s order by r.run_id" % (", ".join(sel), join))


def points(con, table):
    try:
        return con.execute('select count(*) from "%s"' % table).fetchone()[0]
    except sqlite3.Error:
        return None


def summary(con, r):
    d = dict(r)
    completed = d.get("is_completed")
    if completed is None:
        completed = d.get("completed_timestamp") is not None
    exc = d.get("measurement_exception")
    # QCoDeS marks a run completed even when the measurement raised; the traceback is kept
    # in the measurement_exception metadata column. Treat that as aborted.
    aborted = bool(exc) or not completed
    last = exc.strip().splitlines()[-1] if exc else None
    if last and last.startswith("KeyboardInterrupt"):
        last = "stopped by hand (KeyboardInterrupt)"
    return {
        "run_id": d["run_id"],
        "captured_run_id": d.get("captured_run_id"),
        "name": d.get("name"),
        "experiment": d.get("experiment"),
        "sample_name": d.get("sample_name"),
        "guid": d.get("guid"),
        "started": ts(d.get("run_timestamp")),
        "finished": ts(d.get("completed_timestamp")),
        "completed": bool(completed),
        "aborted": aborted,
        "exception": last,
        "points": points(con, d.get("result_table_name")),
    }


def flatten_snapshot(snap):
    """{'instrument.param': {'value': v, 'unit': u}} from a QCoDeS station snapshot."""
    out = {}

    def walk(prefix, node):
        if not isinstance(node, dict):
            return
        for pname, p in (node.get("parameters") or {}).items():
            if isinstance(p, dict) and "value" in p:
                out[prefix + pname] = {"value": p.get("value"), "unit": p.get("unit") or ""}
        for sname, sub in (node.get("submodules") or {}).items():
            walk(prefix + sname + ".", sub)

    station = (snap or {}).get("station", snap or {})
    for iname, inst in (station.get("instruments") or {}).items():
        walk(iname + ".", inst)
    # Some labs never add instruments to the station, so the snapshot is empty, but the
    # station YAML config is stored. Its values are configured initial values, not the state
    # during the run: mark them so they are never cited as measured.
    if not out:
        for iname, inst in ((station.get("config") or {}).get("instruments") or {}).items():
            for pname, p in (inst.get("parameters") or {}).items():
                if isinstance(p, dict):
                    key = iname + "." + pname
                    out[key] = {"value": p.get("initial_value"), "unit": p.get("unit") or "",
                                "alias": p.get("alias"), "label": p.get("label"),
                                "kind": "configured initial value, not the state during the run"}
    for pname, p in (station.get("parameters") or {}).items():
        if isinstance(p, dict) and "value" in p:
            out["station." + pname] = {"value": p.get("value"), "unit": p.get("unit") or ""}
    return out


def detail(con, run_id):
    rc = columns(con, "runs")
    row = None
    for r in run_rows(con):
        if r["run_id"] == run_id:
            row = r
            break
    if row is None:
        return None
    out = summary(con, row)
    extra = ["snapshot"] + [c for c in ("run_description",) if c in rc]
    raw = con.execute("select %s from runs where run_id=?" % ", ".join(extra), (run_id,)).fetchone()
    snap = None
    if raw["snapshot"]:
        try:
            snap = json.loads(raw["snapshot"])
        except ValueError:
            snap = None
    out["settings"] = flatten_snapshot(snap)
    out["settings_source"] = ("station config (configured values, not measured)"
                              if any("kind" in v for v in out["settings"].values()) else "snapshot at run start")
    standard = {"run_id", "exp_id", "name", "result_table_name", "result_counter", "run_timestamp",
                "completed_timestamp", "is_completed", "parameters", "guid", "run_description",
                "snapshot", "captured_run_id", "captured_counter", "parent_datasets",
                "measurement_exception"}
    extra_cols = [c for c in rc if c not in standard]
    if extra_cols:
        vals = con.execute('select %s from runs where run_id=?' % ", ".join('"%s"' % c for c in extra_cols), (run_id,)).fetchone()
        out["metadata"] = {c: vals[c] for c in extra_cols if vals[c] not in (None, "")}
    else:
        out["metadata"] = {}
    out["measured"] = []
    if "run_description" in rc and raw["run_description"]:
        try:
            desc = json.loads(raw["run_description"])
            deps = desc.get("interdependencies") or desc.get("interdependencies_") or {}
            specs = deps.get("paramspecs") or deps.get("parameters") or []
            if isinstance(specs, dict):
                specs = list(specs.values())
            for s in specs:
                if isinstance(s, dict):
                    dep = s.get("depends_on") or []
                    if isinstance(dep, str):
                        dep = [x.strip() for x in dep.split(",") if x.strip()]
                    out["measured"].append({
                        "name": s.get("name"), "label": s.get("label"),
                        "unit": s.get("unit"), "depends_on": dep,
                    })
        except ValueError:
            pass
    return out


def get_field(con, run_id, field):
    d = detail(con, run_id)
    if d is None:
        return None, None
    if field in ("name", "sample_name", "experiment", "completed", "aborted", "exception", "points", "started",
                 "finished", "guid", "captured_run_id"):
        return d.get(field), ""
    s = d["settings"].get(field)
    if s is None:
        return None, None
    return s["value"], s["unit"]


def same(a, b):
    try:
        return float(a) == float(b)
    except (TypeError, ValueError):
        return a == b


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list"); p.add_argument("db"); p.add_argument("--since"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("show"); p.add_argument("db"); p.add_argument("run", type=int); p.add_argument("--json", action="store_true")
    p = sub.add_parser("diff"); p.add_argument("db"); p.add_argument("a", type=int); p.add_argument("b", type=int); p.add_argument("--json", action="store_true")
    p = sub.add_parser("get"); p.add_argument("db"); p.add_argument("run", type=int); p.add_argument("field")
    p = sub.add_parser("copy"); p.add_argument("db"); p.add_argument("--to")
    a = ap.parse_args()
    con = connect(a.db)

    if a.cmd == "copy":
        import tempfile
        d = a.to or tempfile.mkdtemp(prefix="qcodes-copy-")
        os.makedirs(d, exist_ok=True)
        dest = os.path.join(d, os.path.basename(a.db))
        if os.path.exists(dest):
            sys.exit("refusing to overwrite %s" % dest)
        out = sqlite3.connect(dest)
        con.backup(out)  # includes anything still in the -wal file
        out.close()
        print(dest)
        return 0

    if a.cmd == "list":
        runs = [summary(con, r) for r in run_rows(con)]
        if a.since:
            runs = [r for r in runs if (r["started"] or "") >= a.since]
        if a.json:
            print(json.dumps(runs, indent=1))
        else:
            for r in runs:
                flag = ""
                if r["aborted"]:
                    flag = "  ** ABORTED: %s" % (r["exception"] or "not completed")
                print("%5s  %-19s  %-28s  %-14s  %-12s  %6s pts%s" % (
                    r["run_id"], (r["started"] or "")[:19], (r["name"] or "")[:28],
                    (r["experiment"] or "")[:14], (r["sample_name"] or "")[:12],
                    r["points"], flag))
        return 0

    if a.cmd == "show":
        d = detail(con, a.run)
        if d is None:
            print("run %d not found" % a.run, file=sys.stderr); return 1
        if a.json:
            print(json.dumps(d, indent=1, default=str)); return 0
        for k in ("run_id", "name", "experiment", "sample_name", "started", "finished",
                  "completed", "aborted", "exception", "points", "guid"):
            print("%-12s %s" % (k, d.get(k)))
        print("measured:")
        for m in d["measured"]:
            print("  %s [%s]%s" % (m["name"], m["unit"], ("  vs " + ", ".join(m["depends_on"])) if m["depends_on"] else ""))
        if d["metadata"]:
            print("metadata the lab added:")
            for k, v in d["metadata"].items():
                print("  %s = %s" % (k, str(v)[:200]))
        print("settings (%d, from %s):" % (len(d["settings"]), d["settings_source"]))
        for k, v in sorted(d["settings"].items()):
            extra = ("  [%s]" % v["alias"]) if v.get("alias") else ""
            print("  %s = %s %s%s" % (k, v["value"], v["unit"], extra))
        return 0

    if a.cmd == "diff":
        da, db_ = detail(con, a.a), detail(con, a.b)
        if da is None or db_ is None:
            print("run not found", file=sys.stderr); return 1
        sa, sb = da["settings"], db_["settings"]
        changes = []
        for k in sorted(set(sa) | set(sb)):
            va, vb = sa.get(k, {}).get("value"), sb.get(k, {}).get("value")
            if k not in sa or k not in sb or not same(va, vb):
                changes.append({"setting": k, "a": va, "b": vb,
                                "unit": (sb.get(k) or sa.get(k) or {}).get("unit", "")})
        if a.json:
            print(json.dumps(changes, indent=1, default=str))
        else:
            print("settings that differ, run %d -> run %d (%d):" % (a.a, a.b, len(changes)))
            for c in changes:
                print("  %s: %s -> %s %s" % (c["setting"], c["a"], c["b"], c["unit"]))
        return 0

    if a.cmd == "get":
        v, u = get_field(con, a.run, a.field)
        if u is None:
            print("not found: run %d %s" % (a.run, a.field), file=sys.stderr); return 1
        print(json.dumps({"value": v, "unit": u}, default=str))
        return 0


if __name__ == "__main__":
    sys.exit(main())
