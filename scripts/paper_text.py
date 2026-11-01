#!/usr/bin/env python3
"""Extract the text of a PDF page by page, for the evidence check.

    python3 paper_text.py paper.pdf            # writes paper.pages.json next to it

Needs `pdftotext` (poppler). Exits 2 with a message when it is missing, so the
review can go on and mark quotes "unchecked".
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pdf = Path(sys.argv[1])
    if not shutil.which("pdftotext"):
        print("pdftotext not found (install poppler); quotes will be marked unchecked", file=sys.stderr)
        sys.exit(2)
    text = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
                          capture_output=True, text=True, check=True).stdout
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    out = pdf.with_suffix(".pages.json")
    out.write_text(json.dumps({"pdf": pdf.name, "pages": pages}, ensure_ascii=False))
    print(f"{out}: {len(pages)} pages")


if __name__ == "__main__":
    main()
