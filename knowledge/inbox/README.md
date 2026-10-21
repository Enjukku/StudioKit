# Inbox: lesson drafts

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: cause and layer fields); revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (lead decision LD11: lessons arrive in hand-backs; audit D R9: cause labels)

Drafts only. **Who writes them:** every hand-back may carry one optional `lesson` (`rules/messages.md` §3: `type`, `cause`, `layer`, `what_happened`, `proposed_change`); at each gate answer and at job end the lead writes one draft per lesson here, adds date, job, agent and the evidence link, and writes its own. An agent writes here itself only when its brief's `owns` names `knowledge/inbox/`.

The weekly `/improve` pass routes each draft by its cause to the layer that should change, and promotes it into `knowledge/lessons/`, a skill step, a rule, a recipe, a precedent or an overlay, with the owner's approval. Never edit a skill or rule from one unreviewed draft.

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
held_out: true       # only when the draft repeats held-out cases, keys, rubrics or answers (withheld from packets and indexes)
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
| cause | context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · defect found by the owner after internal review · owner taste change · win (the list in `rules/knowledge.md` §8, word for word) |
| layer | the file or skill step that should change (e.g. `vfx-craft` §3 step 4, `rules/messages.md` §2, the packet's ranking, `knowledge/design/vocabulary.md`) |
| what_happened | 1-3 sentences; owner corrections word for word |
| evidence link | file, screenshot, log, `evidence.md` row |
| proposed_change | one sentence |
| what more iteration would fix | optional, one line |

Processed drafts move to `knowledge/inbox/processed/YYYY-MM-DD/` (the date of the `/improve` run).
