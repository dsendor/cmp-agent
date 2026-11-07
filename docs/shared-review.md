# Shared review: decisions and discussion on a Claude artifact

`/referee-preview:publish` publishes the dashboard as a Claude artifact. There, co-authors
can each mark items, see each other's choices, agree one decision per item, and discuss items
in claude.ai comment threads. Everything here needs the artifact; the local `dashboard.html`
keeps decisions in the browser only.

## Capability declaration

Declared with `declare_capabilities` after the first publish (a new page: publish, then
declare):

```json
{
  "db": { "rules": [
    { "path": "decisions",        "read": "view", "write": "owner" },
    { "path": "decisions/{self}", "read": "view", "write": "interact" },
    { "path": "agreed",           "read": "view", "write": "admin" }
  ] },
  "user": { "scopes": ["profile"] },
  "comments": { "composer_only": true }
}
```

## Data

| Path | Written by | Body |
|---|---|---|
| `decisions/<user id>` | that person (the owner can correct it) | `{review, at, items: {<item id>: {decision, note, after, at}}}`, the same shape as the browser's saved decisions |
| `agreed/<item id>` | owner and editors | `{decision, by, at, after}`: the decision that gets applied |

User ids are opaque claude.ai ids. The page resolves them to names when it draws; names are
never stored.

## In the page

- Each card shows co-authors' choices (a person's note shows on hover), a "Set agreed
  decision" menu for the owner and editors, and Discuss, which opens claude.ai's comment
  composer on the card. Threads are claude.ai's: the page never lists or stores them.
- Filters add "Co-authors differ" and "No agreed decision".
- A person's saved decisions replace this browser's on load; on a first visit the browser's
  decisions are uploaded.
- Send to Claude and the revision plan use the agreed decision where there is one, otherwise
  the viewer's own.
- If `db` or `user` is unavailable (signed out, an older host), the page works as before with
  the browser alone.

## Who can do what (claude.ai sharing levels)

| Level | Marks items | Sets agreed | Discusses |
|---|---|---|---|
| Owner, Editor | yes | yes | yes |
| Contributor | yes | no | yes |
| Commenter, Viewer | no, read only | no | Commenter yes |

Anyone outside the owner's organization holds Viewer-level data access unless invited by
email as an Editor, and only while the artifact is not also shared by link.

## Reading it back

`/referee-preview:apply` reads `agreed` and `decisions` with the artifacts tools
(`db_list`) and the threads with `read_comments`, using the slug in
`<review folder>/artifact/published.json`.
