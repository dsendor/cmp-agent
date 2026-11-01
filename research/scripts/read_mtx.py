#!/usr/bin/env python3
"""Summarize Spyview .mtx figure-data files (the format QCoDeS-era labs often attach to arXiv).

    python3 research/scripts/read_mtx.py <file-or-folder> [...]

For each file it prints the axes, their ranges and the grid size, and the range of the
measured values. The skill uses this in step 1 to count datasets and compare the measured
ranges with the ranges shown in the figures. Needs numpy.

The format: a text header line "Units, <value>, <x axis>, xmin, xmax, <y axis>, ymin, ymax,
<z axis>, zmin, zmax", a line "nx ny nz bytes", then the values as little-endian floats
(8 bytes for doubles), z fastest, then y, then x (as Spyview and qtplot write them).
"""
import sys
from pathlib import Path

import numpy as np


def read_mtx(path):
    raw = Path(path).read_bytes()
    first = raw.index(b"\n")
    second = raw.index(b"\n", first + 1)
    header = [h.strip() for h in raw[:first].decode("latin-1").split(",")]
    nx, ny, nz, nbytes = (int(v) for v in raw[first + 1:second].split())
    dtype = "<f8" if nbytes == 8 else "<f4"
    values = np.frombuffer(raw[second + 1:], dtype=dtype, count=nx * ny * nz)
    # Stored with x slowest; transpose to index as data[z, y, x].
    data = values.reshape((nx, ny, nz)).T
    axes = []
    for i, n in zip((2, 5, 8), (nx, ny, nz)):
        if len(header) > i + 2:
            axes.append((header[i], float(header[i + 1]), float(header[i + 2]), n))
    return header[1] if len(header) > 1 else "value", axes, data


def summarize(path):
    name, axes, data = read_mtx(path)
    parts = [f"{a} from {lo:g} to {hi:g} ({n} points)" for a, lo, hi, n in axes if n > 1]
    finite = data[np.isfinite(data)]
    vrange = f"{finite.min():.4g} to {finite.max():.4g}" if finite.size else "no finite values"
    return f"{Path(path).name}: {name}, {vrange}; " + "; ".join(parts)


if __name__ == "__main__":
    files = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        files += sorted(p.glob("*.mtx")) if p.is_dir() else [p]
    for f in files:
        try:
            print(summarize(f))
        except Exception as e:  # report and keep going: one bad file shouldn't stop the count
            print(f"{f.name}: could not read ({e})")
    print(f"{len(files)} files")
