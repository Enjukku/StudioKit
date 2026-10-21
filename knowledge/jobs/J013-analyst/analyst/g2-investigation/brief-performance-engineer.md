---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J013 G2 test (SYNTHETIC TEST DATA, universe 9000000001)
supersedes: []
---
**SYNTHETIC TEST DATA.** Universe 9000000001 does not exist (`.tools/analytics-data/9000000001/README-TEST.md`). This brief is a G2 test output: the lead holds it and does not send it to a real game.

> Author: analyst · claude-opus-5-5 · high · 2026-10-21

```text
<intent>
Next-day return fell from about 21% to about 16%. Most of that came from a wave of new players after a creator video, which is not a game problem. The part we can link to the game started with place version 112 on 2026-10-09: phone players crash about twice as often, hit out-of-memory exits about four times as often, and the slowest phone frames fell from about 31 to about 22 FPS. Phone players now come back the next day about 4 points less often than before, compared with computer players. Phones are the largest player group. You own the cause and the fix; I bring the evidence so you start in the right place. Look through the finding file and the calc folder before you act.
</intent>
<spec>
id: J013-T05b-eng
from: analyst
to: performance-engineer (the lead routes)
model: opus
effort: high                                   # performance-engineer role file (tier craft, effort high)
skills: [performance, engineering-craft, studio-mcp]
refs:
  - knowledge/jobs/J013-analyst/analyst/g2-investigation/retention-drop.md   # take: Part 2 §2.7 (before/after table by platform), §2.3 (data checks that failed), §2.8 row E2. avoid: the overall D1 numbers as your success measure; they mix in the video players
  - knowledge/jobs/J013-analyst/analyst/g2-investigation/calc/ranges-other-metrics.json   # take: exact daily ranges per period
fixed:
  version: place version 112, live 2026-10-09; previous 111     # calendar (lead), J013-T05b brief
  phone_crash_rate: 0.72%-0.88% of ended sessions on 2026-09-25..10-08 -> 1.82%-1.98% on 2026-10-09..10-20   # ClientCrashRate15m by Platform, pull aeb68b544ba4
  oom_exits_per_day: 10-12 -> 39-41                               # OomUnexpectedExits, pull aeb68b544ba4
  client_crashes_per_day: 34-42 -> 86-94                          # ClientCrashCount, pull aeb68b544ba4
  fps_p10_phone: 30.4-31.6 -> 21.4-22.6 FPS                      # ClientFpsP10 by Platform, pull aeb68b544ba4
  fps_p10_tablet: 32.4-33.7 -> 28.3-29.6 FPS                     # same pull
  client_memory_p90_all_platforms: 1,422-1,479 -> 1,571-1,628 (unit as Roblox reports it)   # ClientMemoryUsageP90, pull aeb68b544ba4
  unchanged: computer and console crash rate and FPS P10           # same pulls
  not_known: which phones (OS, memory group); crash rate by platform and version together; whether v111 still runs   # next measurements N3, N4 in the finding file
open: [the cause, the capture recipe, the fix, whether to fix forward or propose a rollback to the lead]
avoid: [a fix without a phone capture of version 112; changing several things at once so we cannot tell which one worked; using the overall next-day return as proof of the fix]
owns: [your capture notes, the fix and its change manifest]
not_in_scope: [analysis method, logging changes (ask the analyst for a measurement spec), Creator Hub changes (owner actions)]
rules:
  - Measure before and after with the same recipe, 3 or more runs, spread reported (performance skill, measure-loop).
  - Phone results need a phone or a phone-class capture; say BLOCKED if you have none (your role file).
  - The data shows where and when, not which code. Say which change in version 112 your fix assumes.
  - Every number in your hand-back cites its capture or file.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the fix (or a needs-decision for a rollback) as a ledger hand-back with before/after capture numbers
checks:
  - C1: the hand-back names the version-112 change the fix assumes and shows phone-class before/after captures (3+ runs each)
  - C2: the analyst can read success after release: phone crash rate back inside 0.72%-0.88% and phone FPS P10 at 30 or more in the first 3 full days after the fix (pull --set performance); review 2026-11-04 or 10 days after release, whichever is later
return: hand-back to lead, copy to analyst
</spec>
```
