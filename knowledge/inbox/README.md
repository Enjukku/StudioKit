# Inbox: lesson drafts

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: cause and layer fields)

Drafts only. The weekly `/improve` pass routes each draft by its cause to the layer that should change, and promotes it into `knowledge/lessons/`, a skill step, a rule, a recipe, a precedent or an overlay, with the owner's approval. Never edit a skill or rule from one unreviewed draft.

File name: `YYYY-MM-DD-<job>-<agent>.md`. Draft frontmatter:

```yaml
---
type: lesson
scope: game          # or universal when it holds for any game
status: draft
updated: YYYY-MM-DD
source: <job id>
supersedes: []
roles: [<roles this lesson is for>]   # optional; ranks it higher in their context packet
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
| cause | context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · found by the owner after internal review · owner taste change · win |
| layer | the file or skill step that should change (e.g. `vfx-craft` §3 step 4, `rules/messages.md` §2, the packet's ranking, `knowledge/design/vocabulary.md`) |
| what happened | 1-3 sentences; owner corrections word for word |
| evidence link | file, screenshot, log, `evidence.md` row |
| proposed change | one sentence |
| what more iteration would fix | optional, one line |

Processed drafts move to `knowledge/inbox/processed/YYYY-MM-DD/` (the date of the `/improve` run).
