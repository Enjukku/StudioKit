---
name: reference-roblox-live-checks
description: How to read live Roblox docs and what cannot be read; saves retries when fact-checking Roblox claims
metadata:
  type: reference
---

- Live API pages answer best through the `.md` form, e.g. `https://create.roblox.com/docs/reference/engine/classes/Camera.md` (full description text). The plain HTML URL often returns only property names and types.
- WebFetch gives a small-model extract, never a raw quote: label live reads "extract". Very large pages (Player.md, ~137k chars) need `offset`.
- Creator Store asset pages (`create.roblox.com/store/asset/<id>`) return empty (script-rendered): version strings and listing dates there cannot be verified by fetch. `roblox.com/library/<id>` only 301-redirects to the same page.
- DevForum threads fetch fine and give title, author, date and FAQ text. Mirror docs pages for beta features may carry no beta banner; status then comes only from the announcement post.
- Mirror vs live: one known path drift (mirror says `/docs/animation/expressions`, live is `/docs/animation/graph-editor-expression`). Mirror yaml tags (ReadOnly) can differ from live extracts; report, do not guess.
- GitHub `commits/main/<path>` for a docs file fetches fine and gives last-touch dates for "is this page current" questions.
