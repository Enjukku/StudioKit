---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J027
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24

# J027 proposal 2: one roadmap per game (replaces the build board)

Owner words (relayed verbatim by the lead chat): "we are creating all these small step goals, but we're not like layering into our overall goal... we're creating to-do lists, but the to-do list is not in a overarching goal list... like a goal page." And: "it's like we're creating the milestones without having updating or creating our roadmap."

Found: the kit has no per-game goal page. `game-profile.md` says what the game is; `knowledge/jobs/active.md` is a flat list; a job card has its own success test but names no game goal; pre-production ends with craft briefs and no milestones (lead chat grep of `.agents/skills/preproduction` and `templates/`).

## The roadmap: `knowledge/design/roadmap.md` (template `templates/roadmap.md`)

Written in pre-production (its last step), updated by the lead at every gate (G1, G3) and every job close, read at session start and after compaction.

| Part | Holds |
| --- | --- |
| Goal | the overall goal in the owner's words, its success test (numbers), the target experience |
| Now | the current milestone and what blocks it, one line |
| Milestones, in order | PROPOSAL defaults: grey box, vertical slice, content, polish, launch. Each: exit test, status. The owner sets the list |
| Under each milestone | the craft rows (area, owner role, route, start trigger, status, stand-ins) and the jobs that serve it (job id, status) |

## What changes in the built work

| Fix | Change |
| --- | --- |
| F2 craft owners | No change to the table. The lead's loop step 1 adds: find the milestone the ask serves on the roadmap. An ask that serves no milestone: add it to a milestone, or one digest question with a default |
| F3 build board | Becomes the roadmap. `build-board.md` and its template are removed; the craft rows move under milestones. A start trigger can be a milestone ("with the vertical slice"). Pre-production ends by writing the roadmap |
| F4 role sessions | The session brief's "Board row" line becomes "Roadmap row: <milestone>, <area>". No other change |
| Job card | New row "Serves: <milestone> on `knowledge/design/roadmap.md`" |
| Gates | Each gate packet and status report carries one line: milestone progress (rows done / total, exit test pass or pending) |

## Cost

0 agent runs. One roadmap file per game. The lead reads it at session start and after compaction, and re-reads it only when it changes (a full read every message would cost its size on every call).
