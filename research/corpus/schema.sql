-- The research corpus (research/data-plan.md, "Corpus schema"). DuckDB.
-- Built from the files in research/ by build.py; never edited by hand. Public data only:
-- a record with an unpublished version is loaded only into a private build (--private).

CREATE TABLE papers (
  arxiv_id     VARCHAR PRIMARY KEY,
  title        VARCHAR,
  journal      VARCHAR,
  doi          VARCHAR,
  subfield     VARCHAR,
  experimental BOOLEAN,
  received     DATE,
  accepted     DATE,
  published    DATE,
  pool         VARCHAR,   -- core, borderline, pending, rejected or other (from pool.json)
  time_window  VARCHAR,   -- post-cutoff or early (published from 2026-07-01, or before)
  peer_review_url VARCHAR,
  source       VARCHAR    -- where the paper entered the corpus: referee-pool, journal-club, revision
);

CREATE TABLE versions (
  arxiv_id VARCHAR,
  version  VARCHAR,       -- v1, v2, ...
  posted   DATE,
  kind     VARCHAR        -- first, before-acceptance, after-acceptance
);

-- Which evaluation set a paper belongs to (split.json and api/sets.json).
CREATE TABLE sets (
  set_name VARCHAR,
  arxiv_id VARCHAR,
  frozen   BOOLEAN        -- true for held-out sets: never used for tuning
);

-- First-round referee recommendations.
CREATE TABLE recommendations (
  arxiv_id VARCHAR,
  referee  VARCHAR,
  recommendation VARCHAR, -- accept, minor revision, major revision, reject
  explicit BOOLEAN
);

-- Referee concerns, extracted from the peer review files (experiment 11 and later).
CREATE TABLE concerns (
  arxiv_id  VARCHAR,
  concern_id VARCHAR,     -- C1, C2, ... within the paper
  round     INTEGER,      -- 1 first round, 2 later rounds
  referees  VARCHAR[],
  category  VARCHAR,
  severity  VARCHAR,      -- major or minor
  summary   VARCHAR,
  in_v1     BOOLEAN,      -- about material present in arXiv v1
  response  VARCHAR,      -- how the authors answered, as extracted
  eligible  BOOLEAN       -- counts towards recall (score.py's definition)
);

-- One review of one paper by one arm (prompt and model), one run.
CREATE TABLE reviews (
  review_id VARCHAR PRIMARY KEY,  -- <arxiv_id>/<arm>/r<k>
  arxiv_id  VARCHAR,
  arm       VARCHAR,              -- e.g. liangplus_cmp.opus, plain.opus, legacy.assistant
  run       INTEGER,
  words     INTEGER
);

-- A judge's verdict on whether a review raised a referee concern.
CREATE TABLE matches (
  review_id  VARCHAR,
  judge      VARCHAR,     -- gemini, sonnet, opus, gemini_flash
  concern_id VARCHAR,
  verdict    VARCHAR,     -- raised, partly, not raised
  fixed_in_v1 BOOLEAN
);

-- The review's own points as the judge saw them.
CREATE TABLE points (
  review_id VARCHAR,
  judge     VARCHAR,
  point_id  VARCHAR,
  quality   VARCHAR,      -- substantive or not
  severity  VARCHAR,
  rank      INTEGER,      -- the reviewer model's own ranking, when ranked
  matches   VARCHAR[],
  partly    VARCHAR[]
);

-- Revision records (docs/revisions.md): what changed between two versions and what referees
-- most likely asked.
CREATE TABLE revisions (
  revision_id VARCHAR PRIMARY KEY,  -- <old id>--<new id>
  old_id VARCHAR, old_arxiv VARCHAR,
  new_id VARCHAR, new_arxiv VARCHAR,
  public BOOLEAN,
  verdict VARCHAR,
  anticipation_rate DOUBLE
);
CREATE TABLE revision_changes (
  revision_id VARCHAR, change_id VARCHAR, area VARCHAR, kind VARCHAR, summary VARCHAR,
  old_page INTEGER, new_page INTEGER, referee_driven BOOLEAN
);
CREATE TABLE inferred_requests (
  revision_id VARCHAR, request_id VARCHAR, title VARCHAR, confidence VARCHAR,
  anticipated_by VARCHAR[], verdict VARCHAR
);

-- Papers the Journal Club for Condensed Matter Physics recommended. Links and DOIs only: the
-- commentaries carry no licence, so no commentary text is stored.
CREATE TABLE journal_club (
  arxiv_id VARCHAR,
  month    VARCHAR,       -- YYYY-MM of the commentary
  commentary_doi VARCHAR,
  commentary_url VARCHAR,
  topic    VARCHAR        -- the commentary's title
);
