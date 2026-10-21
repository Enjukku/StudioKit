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
The 2026-10-04 creator video brought a wave of new players. They come back less often than earlier players, and the wave is fading. This is information for your next choice; the numbers are observational, and v112 hurt phones from 2026-10-09, which is a separate reason for the whole-game drop. I do not claim the video caused low quality; a different audience arrived.
</intent>
<spec>
id: J013-T05a-mkt
from: analyst
to: marketing
model: opus
effort: medium
skills: [marketing-design, marketing-craft]
refs:
  - knowledge/jobs/J013-analyst/analyst/g2-weekly/2026-10-19.md   # take: Part 2 B rows "New players" and "D1, source Other", E
fixed:
  sources: AcquisitionSource Home, Friends, Search, Other   # pull 3a0a68c06b50
  cohorts: first-play 13-18 Oct (D1 mature); D7 and D30 not readable until 22 Oct and 14 Nov
  label: observational (the video is inferred from the jump in source "Other" on 4 Oct: 459 -> 993 player-days)
  break_crossed: yes, 2026-10-12 (source rows not comparable across it)
  measured: source Other next-day return 10.7%-11.5% (13-18 Oct) vs 16.7% on 3 Oct and 10.0% on 4 Oct; new players 653 (3 Oct) -> 1,188 (4 Oct)
open: [whether and how to run another creator push, what to track]
avoid: [reading source Other as the video alone; comparing across 12 Oct for sources]
owns: [campaign record, creative decisions]
not_in_scope: [analysis method]
rules:
  - Immature cohorts are pending. Paid and organic stay apart.
  - Any test of a change needs the analyst's plan first.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: your decision on the next creator push, and a test request if any
checks:
  - C1: the hand-back uses the label above and mature cohorts only
return: hand-back to analyst, copy to lead
</spec>
```
