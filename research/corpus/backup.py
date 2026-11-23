#!/usr/bin/env python3
"""Back up the research corpus and the cached paper PDFs to a private Hugging Face dataset repo.

    python3 research/corpus/backup.py             # rebuild, export Parquet, upload
    python3 research/corpus/backup.py --dry-run   # build and list what would be uploaded

Needs HF_TOKEN (write access) and HF_DATASET_REPO (e.g. user/cmp-agent-research) in the
environment or in `.env` (gitignored; names in `.env.example`). The repo must be private.

Uploads, under one commit per run:
- `corpus/<table>.parquet`: every corpus table, from a public build (never `--private`: that
  build can describe unpublished papers and must stay on the machine that made it);
- `corpus/corpus.duckdb`: the same database, for querying directly;
- `pdfs/<kind>/<file>.pdf`: the PDFs in ~/.cache/cmp-assistant/ (arXiv versions, peer review
  files, accepted versions). They are published papers, but some are not openly licensed, which
  is why the repo stays private.

Uploads are content-addressed, so unchanged files are not sent again. History stays in the repo's
commits, so an earlier backup can be restored with `hf download --revision <commit>`.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CACHE = Path.home() / ".cache" / "cmp-assistant"
sys.path.insert(0, str(ROOT / "research" / "eval"))
from langfuse_sync import load_env  # noqa: E402  (reads .env from this or the main checkout)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-pdfs", action="store_true", help="upload the corpus only")
    a = ap.parse_args()
    os.environ.pop("LANGFUSE_PUBLIC_KEY", None)  # make load_env read .env even if Langfuse keys are set
    load_env()
    token, repo = os.environ.get("HF_TOKEN"), os.environ.get("HF_DATASET_REPO")
    if not (token and repo):
        sys.exit("Set HF_TOKEN and HF_DATASET_REPO (in .env)")

    from huggingface_hub import HfApi, CommitOperationAdd
    api = HfApi(token=token)
    if not api.repo_info(repo, repo_type="dataset").private:
        sys.exit(f"{repo} is public; this backup holds PDFs that are not openly licensed. Make it private first.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        db = tmp / "corpus.duckdb"
        subprocess.run([sys.executable, str(HERE / "build.py"), "--out", str(db), "--parquet", str(tmp / "parquet")],
                       check=True)
        files = [(p, f"corpus/{p.name}") for p in sorted((tmp / "parquet").glob("*.parquet"))]
        files.append((db, "corpus/corpus.duckdb"))
        if not a.no_pdfs and CACHE.exists():
            files += [(p, f"pdfs/{p.relative_to(CACHE).as_posix()}") for p in sorted(CACHE.rglob("*.pdf"))]
        size = sum(p.stat().st_size for p, _ in files)
        print(f"{len(files)} files, {size / 1e6:.0f} MB -> {repo}")
        if a.dry_run:
            for p, dest in files[:15]:
                print("  ", dest)
            return
        head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
        info = api.create_commit(repo, repo_type="dataset",
                                 operations=[CommitOperationAdd(path_in_repo=d, path_or_fileobj=str(p)) for p, d in files],
                                 commit_message=f"Backup from cmp-agent {head}")
        print("done:", info.commit_url)


if __name__ == "__main__":
    main()
