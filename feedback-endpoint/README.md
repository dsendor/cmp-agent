# Feedback endpoint

A single serverless function that receives redacted contributions from the plugin's
`contribute` skill and files each one as a pull request in a private GitHub repository. The
GitHub token lives only in the server's environment; contributors need no GitHub account and
cannot see each other's contributions. The maintainer reviews each pull request before merging.

It stores no IP address or request headers, only the contribution, a random id and the time.

## Deploy on Vercel

1. Create a private repository for the feedback (for example `cmp-agent-feedback`) with a
   first commit on `main`.
2. Create a fine-grained GitHub token limited to that one repository, with *Contents* and
   *Pull requests* set to read and write. Give it an expiry date.
3. Create a Vercel project from this repository with **Root Directory** `feedback-endpoint`, and
   set the environment variables `GITHUB_TOKEN` (the token) and `FEEDBACK_REPO`
   (`owner/cmp-agent-feedback`). Deploy.
4. Set `ENDPOINT` in `scripts/contribute.py` to `https://<project>.vercel.app/api/contribute`,
   or have users set `REFEREE_PREVIEW_FEEDBACK_URL`.
5. In the project's Deployment Protection settings, limit Vercel Authentication to preview
   deployments; the default also blocks production, which would stop contributions.

The live instance is `https://cmp-agent-feedback-dsendor-gmailcoms-projects.vercel.app/api/contribute`,
filing into `dsendor/cmp-agent-feedback`.

## Limits

Requests over 200 KB, with more than 500 items, with fields the plugin does not send, with text
at level 0 or quotes below level 3 are refused. There is no rate limit yet: if the inbox gets
spam, rotate the token and add one.
