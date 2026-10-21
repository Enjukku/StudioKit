---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J013 G2 test (SYNTHETIC TEST DATA, universe 9000000001)
supersedes: []
---
> Author: analyst · claude-sonnet-5-5 · medium · 2026-10-21

SYNTHETIC TEST DATA (universe 9000000001, not a real game).

```text
<intent>
Since place version 112 went live on 2026-10-09, phone players crash more, run slower and leave sooner. Computers and consoles did not change. You own the cause and the fix; I bring the evidence so you can start in the right place. Players on phones are about 59% of daily players, so this is the main player-facing problem in the data this week.
</intent>
<spec>
id: J013-T05a-eng
from: analyst
to: performance-engineer (the lead routes)
model: opus
effort: high
skills: [performance, code-review]
refs:
  - knowledge/jobs/J013-analyst/analyst/g2-weekly/2026-10-19.md   # take: Part 2 B (device performance), E (explanations); avoid: reading it as proof of the cause
  - knowledge/jobs/J013-analyst/analyst/g2-weekly/calc/weekly-numbers.json   # take: "phases" block
fixed:
  version: place version 112, live 2026-10-09 (lead's calendar)
  phone_crash_rate: 0.0072-0.0088 before (4-8 Oct) -> 0.0182-0.0198 since (13-18 Oct)   # pull aeb68b544ba4
  phone_fps_p10: 30.4-31.6 before -> 21.4-22.6 since   # pull aeb68b544ba4
  client_crashes_per_day: 34-42 before -> 86-94 since; memory-related exits 10-12 -> 39-41 per day   # pull aeb68b544ba4
  memory_p90_all_devices: 1,422-1,479 before -> 1,571-1,628 since (unit as returned)   # pull aeb68b544ba4
  not_changed: computer and console crash rate and FPS; tablet FPS P10 fell 32.4-33.7 -> 28.3-29.6, tablet crash rate flat   # pull aeb68b544ba4
  phone_next_day_return: 20.1%-20.9% before -> 16.2%-16.8% since   # pull da92f66a1c21 / adhoc 3a0a68c06b50
open: [the cause, the fix, whether to roll back first, what to measure on a phone before shipping]
avoid: [assuming the cause is memory only (the data shows memory and crashes, not why); changing several things at once if the analyst must read the result]
owns: [game code and performance fixes]
not_in_scope: [changing analytics or telemetry, Creator Hub actions]
rules:
  - Tell the analyst the date the fix goes live and the place version number, so the next page marks it.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the cause, the fix (or a rollback proposal for the owner) and the live date, as a ledger hand-back
checks:
  - C1: the hand-back names the live version and date
  - C2: the hand-back says which phone devices you tested
return: hand-back to analyst, copy to lead
</spec>
```

Owner action (not yours, not mine): rollback of v112 is the owner's decision (Creator Hub).
