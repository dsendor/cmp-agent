// POST /api/contribute: one redacted contribution from the Referee preview plugin.
// Each accepted contribution becomes a pull request in the private feedback repository,
// so the maintainer reviews it before it joins the shared data. The GitHub token lives
// only in this server's environment; contributors need no GitHub account.
//
// Environment: GITHUB_TOKEN (fine-grained, the feedback repository only: contents and
// pull requests read and write), FEEDBACK_REPO ("owner/name"), FEEDBACK_BASE (default "main").

import { randomUUID } from "node:crypto";

const MAX_BYTES = 200_000;
const MAX_ITEMS = 500;
const MAX_TEXT = 2_000;
const LEVELS = [0, 1, 2, 3];
const ITEM_FIELDS = new Set(["lane", "topic", "tier", "effort", "decision", "reason", "referee_raised", "text", "quote"]);
const META_FIELDS = new Set(["reviewer_version", "mode", "model", "runs", "plugin_version", "counts"]);

function bad(res, code, msg) { res.status(code).json({ ok: false, error: msg }); }

// Accept only the fields the plugin sends, at the lengths it sends them. Text is allowed
// only at level 1 and above, quotes only at level 3.
function validate(body) {
  if (!body || body.schema !== "referee-preview/contribution/1") return "unknown schema";
  if (!LEVELS.includes(body.level)) return "level must be 0 to 3";
  if (!Array.isArray(body.items) || body.items.length === 0 || body.items.length > MAX_ITEMS) return "items must be a non-empty list";
  for (const k of Object.keys(body.meta || {})) if (!META_FIELDS.has(k)) return "unexpected meta field " + k;
  for (const it of body.items) {
    if (typeof it !== "object" || it === null) return "item must be an object";
    for (const [k, v] of Object.entries(it)) {
      if (!ITEM_FIELDS.has(k)) return "unexpected item field " + k;
      if (typeof v === "string" && v.length > MAX_TEXT) return "text too long";
    }
    if (it.text != null && body.level < 1) return "text is not allowed at level 0";
    if (it.quote != null && body.level < 3) return "quotes are allowed only at level 3";
  }
  return null;
}

async function gh(path, init = {}) {
  const r = await fetch("https://api.github.com" + path, {
    ...init,
    headers: { Authorization: "Bearer " + process.env.GITHUB_TOKEN, Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "referee-preview-feedback", ...(init.headers || {}) },
  });
  if (!r.ok) throw new Error("GitHub " + r.status + " on " + path);
  return r.json();
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");            // the dashboard runs from a local file
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  if (!process.env.GITHUB_TOKEN || !process.env.FEEDBACK_REPO) return bad(res, 503, "not configured");

  const raw = typeof req.body === "string" ? req.body : JSON.stringify(req.body || null);
  if (Buffer.byteLength(raw) > MAX_BYTES) return bad(res, 413, "too large");
  let body;
  try { body = typeof req.body === "string" ? JSON.parse(req.body) : req.body; } catch { return bad(res, 400, "not JSON"); }
  const err = validate(body);
  if (err) return bad(res, 400, err);

  const id = randomUUID();
  const day = new Date().toISOString().slice(0, 10);
  const record = { ...body, id, received: new Date().toISOString() };   // no IP, no headers, no name unless given
  const repo = process.env.FEEDBACK_REPO, base = process.env.FEEDBACK_BASE || "main";
  const branch = "contribution/" + day + "-" + id.slice(0, 8);
  try {
    const ref = await gh(`/repos/${repo}/git/ref/heads/${base}`);
    await gh(`/repos/${repo}/git/refs`, { method: "POST", body: JSON.stringify({ ref: "refs/heads/" + branch, sha: ref.object.sha }) });
    await gh(`/repos/${repo}/contents/contributions/${day}/${id}.json`, { method: "PUT", body: JSON.stringify({
      message: "Contribution " + id.slice(0, 8) + " (level " + body.level + ", " + body.items.length + " items)",
      content: Buffer.from(JSON.stringify(record, null, 1)).toString("base64"), branch }) });
    await gh(`/repos/${repo}/pulls`, { method: "POST", body: JSON.stringify({
      title: "Contribution " + id.slice(0, 8) + ": level " + body.level + ", " + body.items.length + " items",
      head: branch, base, body: "Received " + record.received + " from the Referee preview plugin. Review before merging." }) });
  } catch (e) {
    return bad(res, 502, "could not file the contribution");
  }
  return res.status(200).json({ ok: true, id });
}
