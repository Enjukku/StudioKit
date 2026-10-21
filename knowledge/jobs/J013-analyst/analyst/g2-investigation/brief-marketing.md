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
The creator video on 2026-10-04 brought many new players through the "Other" source (outside links). More players came back in total, but the extra players came back the next day far less often than our usual players, so the overall return rate fell. This is not a game fault and needs no fix from you. One question stays open, and it belongs to you: is this a different audience, or does the video promise something the first session does not show? The data cannot tell the two apart. Credit for a source is not proof the source caused the players.
</intent>
<spec>
id: J013-T05b-mkt
from: analyst
to: marketing
model: opus
effort: medium                                 # marketing roster, J012-D1
skills: [marketing-design, marketing-craft]
refs:
  - knowledge/jobs/J013-analyst/analyst/g2-investigation/retention-drop.md   # take: Part 2 §2.6 (source table, excess split), §2.8 row E3. avoid: the rough split numbers as measured values; they are estimates
fixed:
  sources: AcquisitionSource Friends, HomeRecommendations, Search, Other   # pull 3a0a68c06b50
  cohorts: first play 2026-09-27..10-13, D1 mature by stats maturity (lag 1, PROPOSAL)   # calc/maturity-all-cohorts.json
  other_d1: 16.8%-17.3% (2026-09-27..10-01) -> 10.0%-10.4% (2026-10-04..08) -> 10.5%-11.0% (2026-10-09..13)   # ForwardD1Retention by AcquisitionSource
  other_daily_players: 421-485 -> 875-993 -> 580 on 2026-10-20   # DailyActiveUsers by AcquisitionSource
  extra_players_first_5_days: about 2,201 new players, about 185 came back next day (8.4%), estimate   # calc/derived-counts.json excess_split_video_days
  usual_sources: Friends, Home, Search D1 unchanged on 2026-10-04..08; about 2 points lower from 2026-10-09 (version 112, a phone problem routed to engineering)
  label: observational, attributed source; no test
  break_crossed: yes, 2026-10-12 discovery recording change (Home, Search, Charts); no step seen on that date
open: [whether and how to check the video against the first session, any next marketing step]
avoid: [reading the video traffic's low return as a creative failure without a check; reading a pre-10-12 vs post-10-12 change in Home or Search as a marketing effect; comparing D1 levels after 2026-10-09 without the version-112 note]
owns: [campaign record, creative decisions]
not_in_scope: [analysis method, game changes, Creator Hub changes]
rules:
  - Paid and organic players stay apart; immature cohorts are "pending".
  - New players by source were not pulled (no key); per-source numbers are daily ranges, not counts. Do not average them.
  - Any test of a change gets the analyst's spec before it starts.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: your reading of the promise-match question (what the video shows vs what a new player sees in the first minutes) and any next step, as a ledger hand-back
checks:
  - C1: the hand-back uses the label given (observational, attributed) and mature cohorts only
  - C2: the hand-back says which of "different audience" or "promise mismatch" it supports, and on what observation
return: hand-back to analyst, copy to lead
</spec>
```
