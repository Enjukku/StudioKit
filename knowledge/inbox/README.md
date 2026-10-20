# Inbox: lesson drafts

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Drafts only. The weekly `/improve` pass promotes them into `knowledge/lessons/`, skills, rules or overlays, with the owner's approval. Never edit a skill or rule from one unreviewed draft.

File name: `YYYY-MM-DD-<job>-<agent>.md`. Draft frontmatter:

```yaml
---
type: lesson
scope: game          # or universal when it holds for any game
status: draft
updated: YYYY-MM-DD
source: <job id>
supersedes: []
---
> Author: <role> · <model id> · <effort> · <date>
```

Body fields:

| Field | Content |
| --- | --- |
| date | |
| job | job id |
| agent | role |
| type | win / failure / owner-correction |
| what happened | 1-3 sentences; owner corrections word for word |
| evidence link | file, screenshot, log |
| proposed rule | one sentence |

Processed drafts move to `knowledge/inbox/processed/YYYY-MM-DD/` (the date of the `/improve` run).
