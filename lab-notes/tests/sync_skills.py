#!/usr/bin/env python3
"""Copy scripts/ and docs/record-format.md into every skill folder, so each skill works when
imported on its own (Claude Science imports a skill's folder, not the whole plugin).

  python3 lab-notes/tests/sync_skills.py          write the copies
  python3 lab-notes/tests/sync_skills.py --check  exit 1 if any copy differs (run_tests.py does this)

The files in lab-notes/scripts/ and lab-notes/docs/ are the originals. Never edit the copies.
"""
import filecmp
import os
import shutil
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [os.path.join("scripts", f) for f in sorted(os.listdir(os.path.join(PLUGIN, "scripts")))
         if f.endswith(".py")] + [os.path.join("docs", "record-format.md")]


def main():
    check = "--check" in sys.argv
    stale = []
    for name in sorted(os.listdir(os.path.join(PLUGIN, "skills"))):
        skill = os.path.join(PLUGIN, "skills", name)
        if not os.path.isfile(os.path.join(skill, "SKILL.md")):
            continue
        for rel in FILES:
            src, dst = os.path.join(PLUGIN, rel), os.path.join(skill, rel)
            if os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False):
                continue
            stale.append(os.path.relpath(dst, PLUGIN))
            if not check:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    if check and stale:
        sys.exit("skill copies out of date (run tests/sync_skills.py): " + ", ".join(stale))
    print("%s %d file(s)" % ("stale:" if check else "copied", len(stale)))


if __name__ == "__main__":
    main()
