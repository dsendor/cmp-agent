#!/usr/bin/env python3
"""Fill the dashboard template with review.json and write dashboard.html.

    python3 build_dashboard.py <review-folder> [--open]

The folder must hold review.json; paper.pdf beside it is shown in the PDF pane.
With --open, opens the dashboard in the default browser.
"""
import json
import subprocess
import sys
import webbrowser
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "dashboard" / "template.html"
MARK = "/*REVIEW_JSON*/null"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    folder = Path(args[0]).resolve()
    review = json.loads((folder / "review.json").read_text())
    review["paper"]["pdf_local"] = (folder / "paper.pdf").exists()
    data = json.dumps(review, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text()
    if MARK not in html:
        sys.exit("template is missing the data marker")
    out = folder / "dashboard.html"
    out.write_text(html.replace(MARK, data))
    print(out)
    if "--open" in sys.argv:
        opener = {"darwin": ["open"], "win32": ["cmd", "/c", "start", ""]}.get(sys.platform, ["xdg-open"])
        try:
            subprocess.run(opener + [str(out)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            webbrowser.open(out.as_uri())


if __name__ == "__main__":
    main()
