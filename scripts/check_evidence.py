#!/usr/bin/env python3
"""Check that every quote in review.json appears in the paper, and on the cited page.

    python3 check_evidence.py review.json paper.pages.json

Sets each issue's `evidence_found` to "exact" (the letters and digits appear in order),
"close" (at least 80% of the quote's 8-character runs appear on one page, which
allows for hyphenation, ligatures and symbols extracted differently) or
"not_found", and `found_page` to the page where it matched best. Rewrites
review.json in place and prints the share verified per lane.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path


GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "ϵ": "epsilon", "ζ": "zeta",
         "η": "eta", "θ": "theta", "κ": "kappa", "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "π": "pi",
         "ρ": "rho", "σ": "sigma", "τ": "tau", "φ": "phi", "ϕ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
         "∆": "delta", "Ω": "omega"}


def chars(text):
    """Letters and digits only, lower case, Greek spelled out: spacing, hyphenation and
    symbols extracted differently from the PDF no longer matter."""
    text = unicodedata.normalize("NFKC", text).lower()
    text = re.sub(r"-\s*\n\s*", "", text)          # words split across lines
    text = "".join(GREEK.get(ch, ch) for ch in text)
    return re.sub(r"[^a-z0-9]", "", text)


def match(quote, pages, n=8):
    """Return (status, page) for the best page."""
    if len(quote) < n:
        return "unchecked", None
    for k, page in enumerate(pages, 1):
        if quote in page:
            return "exact", k
    q = {quote[i:i + n] for i in range(len(quote) - n + 1)}
    best, best_page = 0.0, None
    for k, page in enumerate(pages, 1):
        score = sum(g in page for g in q) / len(q)
        if score > best:
            best, best_page = score, k
    return ("close" if best >= 0.8 else "not_found"), best_page


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    rpath = Path(sys.argv[1])
    review = json.loads(rpath.read_text())
    pages = [chars(p) for p in json.loads(Path(sys.argv[2]).read_text())["pages"]]
    tally = {}
    for it in review["issues"]:
        status, page = match(chars(it["evidence"]["quote"]), pages)
        it["evidence_found"], it["found_page"] = status, page
        if status in ("exact", "close") and page and it["evidence"].get("page") != page:
            it["evidence"]["cited_page"] = it["evidence"].get("page")
            it["evidence"]["page"] = page           # point the PDF view at the page where the quote is
        t = tally.setdefault(it["lane"], {"exact": 0, "close": 0, "not_found": 0, "unchecked": 0})
        t[status] += 1
    review["evidence_check"] = tally
    rpath.write_text(json.dumps(review, indent=1, ensure_ascii=False))
    for lane, t in tally.items():
        n = sum(t.values())
        ok = t["exact"] + t["close"]
        print(f"{lane}: {ok}/{n} quotes found ({t['exact']} exact, {t['close']} close, {t['not_found']} not found)")


if __name__ == "__main__":
    main()
