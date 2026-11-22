# The research corpus

*AI-built, 2026-11-22. Stage 1 of `../data-plan.md`.*

One DuckDB database built from the files in `research/`: papers and their versions, the
evaluation sets, referee concerns and recommendations, every review the evaluation ran with
the judge's verdicts, revision records, and the Journal Club selections. It is derived, so it
is rebuilt from scratch each time and not committed.

```bash
pip install -r research/corpus/requirements.txt
python3 research/corpus/build.py                    # research/corpus/corpus.duckdb
python3 research/corpus/build.py --parquet out/     # also every table as Parquet (public data only)
```

The schema is `schema.sql`. Notes:
- `concerns.eligible` uses `eval/api/score.py`'s definition (first round, not presentation or
  novelty, not fixed in v1), so recall computed from the corpus matches `score.py`. Checked on
  2026-11-22: plain prompt 42.4%, Liang 42.3%, three Liang runs merged 53.2%, reviewer v1.0
  (`liangplus_cmp`) 49.1%, MARG 61.7%, the plain prompt asked for 70 concerns 60.9% (Gemini
  judge, dev30), as in `EVALUATION.md`.
- `sets.frozen` marks held-out sets (`test`, `test22`, `test2`): never tune on them.
- `papers.time_window` is `post-cutoff` for papers published from 2026-07-01, after the reviewer
  models' training cutoff.
- `journal_club` holds links and DOIs only. The commentaries carry no licence, so their text is
  not stored.

**Privacy.** The default build reads only what is in this repository. `--private` also loads
revision records from `~/.referee-preview/revisions/`, which can describe unpublished papers:
such a build stays on the machine that made it, and `--parquet` refuses to run with it.

Recall from the corpus, as a check:

```sql
WITH elig AS (SELECT arxiv_id, concern_id FROM concerns WHERE eligible),
per_run AS (
  SELECT r.arxiv_id, r.arm, r.run, count(*) FILTER (WHERE m.verdict = 'raised') AS hit
  FROM reviews r JOIN elig e ON e.arxiv_id = r.arxiv_id
  LEFT JOIN matches m ON m.review_id = r.review_id AND m.judge = 'gemini' AND m.concern_id = e.concern_id
  WHERE r.review_id IN (SELECT review_id FROM matches WHERE judge = 'gemini')
  GROUP BY 1, 2, 3),
per_paper AS (SELECT arxiv_id, arm, avg(hit) AS hit FROM per_run GROUP BY 1, 2)
SELECT p.arm, count(*) AS papers, round(100 * sum(p.hit) / sum(n.n), 1) AS recall
FROM per_paper p JOIN (SELECT arxiv_id, count(*) AS n FROM elig GROUP BY 1) n USING (arxiv_id)
WHERE p.arxiv_id IN (SELECT arxiv_id FROM sets WHERE set_name = 'dev30')
GROUP BY 1 ORDER BY 1;
```
