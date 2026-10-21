---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 synthetic test data (test-pack/analyst-weekly-2026-10-20.md)"
supersedes: []
---
SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

# Weekly player data: Mothlight Meadow · Mon 2026-10-12 to Sun 2026-10-18 (UTC)

Written by the analyst on 2026-10-20 for the owner and the team. Data complete through Mon 2026-10-19. A value we do not have is `UNAVAILABLE`. Every rate shows its counts.

---

## Part 1: For the owner

| | |
| --- | --- |
| **What happened** | Fewer players are back after the Lantern Parade ended: on the Wednesday and Thursday after the event, 1,460 and 1,370 returning players played, against 1,650 and 1,850 on the same weekdays before it. On phones, 39% of new players place their first lantern; on PC it is 80%. |
| **Why we think so** | Players who were new during the event came back the next day 14.7% of the time (780 of 5,290); new players on other days did so 19.1% (1,512 of 7,900). In the first session, 3,700 of 6,910 phone players who dropped the first moth in the Jar did not place a lantern. |
| **How sure we are** | Medium for the post-event drop (matched weekdays, but only two pairs and the event itself moved traffic). Medium for the phone step (server events, large counts), Low for the reason: we do not log what phone players do in build mode. Week-3 players have not finished 7 days. No 30-day numbers exist yet. |
| **What we recommend** | Add client-side logging for the build-mode steps on phone, then read the funnel again · who: engineering, with the analyst's spec · for which players: new phone and tablet players · how we will know it worked: we can say where in build mode phone players stop · check again on: 2026-10-27 |
| **Your decision needed** | None this week |

---

## Part 2: For the team and for checking

### A. Data used
| Field | Value |
| --- | --- |
| Pull | Analytics pull run ids `ana-20261020-0905`, `ana-20261020-0912` (synthetic). Pulled 2026-10-20 09:05 UTC |
| Last pull before this one | 2026-10-13 (7 days ago) |
| Data complete through | Mon 2026-10-19 (last full UTC day). D1 for 2026-10-19 is not available yet. No `Projected` points used |
| Measurement breaks in or near this period | **2026-10-12**: Roblox changed how discovery sources are recorded, so traffic-source shares before and after that day are not comparable. **2026-10-02**: tutorial step events exist only from build 1.0.2, so first-session funnels start on 2026-10-05 here. Event name changes: none |
| Builds and changes live this week | 1.1.0 (2026-10-08): Lantern Parade content, "Tell us" form. Lantern Parade 2026-10-09 15:00 to 2026-10-13 15:00 UTC. 1.1.1 (2026-10-13 16:00): Parade closed, Terrarium saves batched every 60 s, Spark Swap stall kept. No marketing push other than the Parade announcement |

### B. Numbers

**B1. New players by start week (cohort), with platform split**

| Cohort (first session) | New players | Phone | Tablet | PC | Console |
| --- | --- | --- | --- | --- | --- |
| Week 1: Tue 09-29 to Sun 10-04 (6 days) | 9,840 (1,640 per day) | 5,764 / 9,840 (58.6%) | 598 / 9,840 (6.1%) | 3,180 / 9,840 (32.3%) | 298 / 9,840 (3.0%) |
| Week 2: Mon 10-05 to Sun 10-11 | 7,260 (1,037 per day) | 4,420 / 7,260 (60.9%) | 470 / 7,260 (6.5%) | 2,160 / 7,260 (29.8%) | 210 / 7,260 (2.9%) |
| Week 3: Mon 10-12 to Sun 10-18 | 5,930 (847 per day) | 3,730 / 5,930 (62.9%) | 380 / 5,930 (6.4%) | 1,640 / 5,930 (27.7%) | 180 / 5,930 (3.0%) |

Where week-3 new players came from (after the 2026-10-12 recording change; do not compare with earlier weeks): Home recommendations 2,390 / 5,930 (40.3%), friend joins 1,440 (24.3%), search 1,070 (18.0%), other 1,030 (17.4%). Week-2 counts use the old recording: Home recommendations 3,380 / 7,260 (46.6%), friend joins 1,500 (20.7%), search 1,190 (16.4%), other 1,190 (16.4%).

**B2. Daily active players (DAU) and new players per day**

| Date | Day | DAU | New that day | Returning (DAU minus new) |
| --- | --- | --- | --- | --- |
| 2026-10-05 | Mon | 3,200 | 1,060 | 2,140 |
| 2026-10-06 | Tue | 3,000 | 1,000 | 2,000 |
| 2026-10-07 | Wed | 2,610 | 960 | 1,650 |
| 2026-10-08 | Thu | 2,780 | 930 | 1,850 |
| 2026-10-09 (Parade) | Fri | 4,950 | 1,090 | 3,860 |
| 2026-10-10 (Parade) | Sat | 7,320 | 1,260 | 6,060 |
| 2026-10-11 (Parade) | Sun | 6,980 | 960 | 6,020 |
| 2026-10-12 (Parade) | Mon | 5,840 | 1,020 | 4,820 |
| 2026-10-13 (Parade) | Tue | 4,120 | 960 | 3,160 |
| 2026-10-14 | Wed | 2,240 | 780 | 1,460 |
| 2026-10-15 | Thu | 2,130 | 760 | 1,370 |
| 2026-10-16 | Fri | 2,260 | 790 | 1,470 |
| 2026-10-17 | Sat | 2,610 | 880 | 1,730 |
| 2026-10-18 | Sun | 2,480 | 740 | 1,740 |
| 2026-10-19 | Mon | 2,050 | 700 | 1,350 |

Matched weekdays, before the Parade and after it: Wed 10-07 returning 1,650 against Wed 10-14 returning 1,460 (-11.5%); Thu 10-08 1,850 against Thu 10-15 1,370 (-25.9%). Weekly active players: week 2 (10-05 to 10-11) 15,310; week 3 (10-12 to 10-18) 9,640. Week 3 by platform: phone 6,010 (62.3%), PC 2,830 (29.4%), tablet 520 (5.4%), console 280 (2.9%).

**B3. First session, new players of weeks 2 and 3 (2026-10-05 to 2026-10-18), by platform**

Steps are the four tutorial steps in `game.md`, logged by the server. Percent of all new players of that platform; the last column is the step-3-to-step-4 conversion.

| Platform | New players | 1. Caught first moth | 2. Moth in the Jar (first Dust) | 3. Placed first lantern | 4. Bought first upgrade | From step 2 to step 3 |
| --- | --- | --- | --- | --- | --- | --- |
| phone | 8,150 | 7,420 / 8,150 (91.0%) | 6,910 / 8,150 (84.8%) | 3,210 / 8,150 (39.4%) | 2,870 / 8,150 (35.2%) | 3,210 / 6,910 (46.5%) |
| tablet | 850 | 790 / 850 (92.9%) | 748 / 850 (88.0%) | 442 / 850 (52.0%) | 401 / 850 (47.2%) | 442 / 748 (59.1%) |
| PC | 3,800 | 3,610 / 3,800 (95.0%) | 3,420 / 3,800 (90.0%) | 3,040 / 3,800 (80.0%) | 2,810 / 3,800 (73.9%) | 3,040 / 3,420 (88.9%) |
| console | 390 | 361 / 390 (92.6%) | 337 / 390 (86.4%) | 281 / 390 (72.1%) | 262 / 390 (67.2%) | 281 / 337 (83.4%) |
| All | 13,190 | 12,181 / 13,190 (92.4%) | 11,415 / 13,190 (86.5%) | 6,973 / 13,190 (52.9%) | 6,343 / 13,190 (48.1%) | 6,973 / 11,415 (61.1%) |

Median first-session length (same players): phone 4.1 min (n = 8,150), tablet 5.6 min (n = 850), PC 9.8 min (n = 3,800), console 8.9 min (n = 390). Of the 3,700 phone players who dropped a moth in the Jar and did not place a lantern, 2,510 (67.8%) ended the session within 3 minutes of the Jar step. We have no client-side events for build mode (opening the Satchel, picking up a lantern, dragging it), so we cannot see where in step 3 phone players stop.

**B4. Came back, by cohort**

| Measure | Week 1 cohort | Week 2 cohort | Week 3 cohort |
| --- | --- | --- | --- |
| D1 (returned the next UTC day), all platforms | 2,010 / 9,840 (20.4%) | 1,280 / 7,260 (17.6%) | 1,012 / 5,930 (17.1%) |
| D1, phone | 1,100 / 5,764 (19.1%) | 690 / 4,420 (15.6%) | 560 / 3,730 (15.0%) |
| D1, tablet | 119 / 598 (19.9%) | 90 / 470 (19.1%) | 72 / 380 (18.9%) |
| D1, PC | 720 / 3,180 (22.6%) | 450 / 2,160 (20.8%) | 340 / 1,640 (20.7%) |
| D1, console | 71 / 298 (23.8%) | 50 / 210 (23.8%) | 40 / 180 (22.2%) |
| D7 (played on day 7), all platforms | 712 / 9,840 (7.2%) | 439 / 7,260 (6.0%) | **immature** (only the 10-12 start day has reached day 7: 56 / 1,020, 5.5%; not a cohort value) |
| D7, phone | 378 / 5,764 (6.6%) | 238 / 4,420 (5.4%) | immature |
| D7, tablet | 41 / 598 (6.9%) | 29 / 470 (6.2%) | immature |
| D7, PC | 266 / 3,180 (8.4%) | 154 / 2,160 (7.1%) | immature |
| D7, console | 27 / 298 (9.1%) | 18 / 210 (8.6%) | immature |
| D30 | UNAVAILABLE (the first cohort reaches day 30 on 2026-10-29) | UNAVAILABLE | UNAVAILABLE |

Week 2 phone players by first-session lantern: placed a lantern 540 / 1,760 (30.7%) came back on D1; did not place one 150 / 2,660 (5.6%). (Week 2 phone new players: 4,420 = 1,760 + 2,660.)

**B5. Lantern Parade (2026-10-09 15:00 to 2026-10-13 15:00 UTC): reach, and what came after**

| Measure | Value and counts | Basis |
| --- | --- | --- |
| Players active in the event window | 15,960: 4,980 new, 10,980 with a first session before the window | Any session in the window |
| Entered the Parade Plaza | 11,420 / 15,960 (71.6%); new players 4,140 / 4,980 (83.1%); earlier players 7,280 / 10,980 (66.3%) | Reach |
| Finished the 12-stage track | 3,240 / 11,420 (28.4%) of entrants | |
| Peak DAU | 7,320 on Sat 10-10, 2.8 times Wed 10-07 (2,610) | |
| Played again 10-14 to 10-19 (6 days after the event) | Earlier-player entrants 3,060 / 7,280 (42.0%); new-player entrants 1,320 / 4,140 (31.9%); earlier players active in the window who did not enter 1,410 / 3,700 (38.1%) | Observational. Entrants are more engaged to begin with; no test |
| New players who started during the event days (10-09 to 10-13) | D1 780 / 5,290 (14.7%); D7 for the week-2 part only (10-09 to 10-11) 181 / 3,310 (5.5%) | Whole UTC days |
| New players who started on other days of weeks 2 and 3 | D1 1,512 / 7,900 (19.1%); D7 for the week-2 part (10-05 to 10-08) 258 / 3,950 (6.5%) | Same cohort age |
| DAU after the event, matched to before | Wed 10-14 2,240 against Wed 10-07 2,610; Thu 10-15 2,130 against Thu 10-08 2,780 | New players per day also fell (see B2) |

**B6. Progress: how far players get (players with at least 3 distinct active days, first session 09-29 to 10-11, as of 10-19)**

| Cohort | Players | Entered Reed Pond | Opened the Dusk Board at least once | Entered Old Orchard | Entered Hollow Cave |
| --- | --- | --- | --- | --- | --- |
| Week 1 | 3,420 | 2,980 / 3,420 (87.1%) | 1,060 / 3,420 (31.0%) | 410 / 3,420 (12.0%) | 61 / 3,420 (1.8%) |
| Week 2 | 1,440 | 1,170 / 1,440 (81.2%) | 420 / 1,440 (29.2%) | 110 / 1,440 (7.6%) | 13 / 1,440 (0.9%) |
| Both | 4,860 | 4,150 / 4,860 (85.4%) | 1,480 / 4,860 (30.5%) | 520 / 4,860 (10.7%) | 74 / 4,860 (1.5%) |

Of these 4,860 players: 3,610 (74.3%) held at least 6,000 Glow Dust at some point (the Orchard gate price); of those 3,610, 490 (13.6%) entered the Orchard. Started the "Light the three Beacons" chain: 1,030 (21.2%); finished it: 560 (11.5%). Median Glow Dust held at the end of 10-18: 12,300 (n = 4,860). Week-3 players are left out: most have not had 3 active days yet.

**B7. Money: Starlight Beads and the Dewdrop Crate**

| Measure | Week 2 (10-05 to 10-11) | Week 3 (10-12 to 10-18) |
| --- | --- | --- |
| Paying players | 219 / 15,310 (1.43%) of weekly actives | 141 / 9,640 (1.46%) of weekly actives |
| Bead pack sales (Creator Hub sales report) | 262: Small 118, Medium 91, Large 53 | 188: Small 96, Medium 68, Large 24 |
| Robux from Bead packs | 33,368 | 20,652 |
| Robux per paying player | 152.4 (n = 219) | 146.5 (n = 141) |
| Robux per weekly active player | 2.18 (n = 15,310) | 2.14 (n = 9,640) |
| Beads granted, game events (`beads_granted`) | 261 events | 181 events |
| Beads bought (from sales) | 71,730 | 44,240 |
| Beads spent: Dewdrop Crate opens | 51,000 | 32,000 |
| Beads spent: Cosmetics | 14,100 | 8,300 |
| Beads spent: Skip timers | 5,200 | 2,950 |
| Beads spent, total | 70,300 | 43,250 |

Dewdrop Crate, since launch (2026-09-29 to 2026-10-19), players who opened at least one crate, and players who opened the crate info panel (`crate_info_opened`):

| Platform | Players who opened a crate | Players who opened the info panel | Info panel events |
| --- | --- | --- | --- |
| Phone | 1,240 | 0 (0.0%) | 0 |
| Tablet | 120 | 0 (0.0%) | 0 |
| PC | 640 | 281 (43.9%) | 436 |
| Console | 55 | 17 (30.9%) | 22 |
| All | 2,055 | 298 (14.5%) | 458 |

**B8. Economy: Glow Dust and Parade Sparks**

| Glow Dust, in | Week 2 | Week 3 |
| --- | --- | --- |
| Catches and Jar | 14,200,000 | 9,800,000 |
| Terrarium (passive) | 8,900,000 | 6,700,000 |
| Dusk Board quests | 2,100,000 | 1,500,000 |
| Spark Swap | 621,000 | 2,841,000 |
| **Total in** | 25,821,000 | 20,841,000 |

| Glow Dust, out | Week 2 | Week 3 |
| --- | --- | --- |
| Lantern upgrades | 11,300,000 | 7,600,000 |
| Zone gates | 3,100,000 | 1,200,000 |
| Net upgrades | 2,200,000 | 1,500,000 |
| Terrarium Shop items | 2,400,000 | 5,600,000 |
| **Total out** | 19,000,000 | 15,900,000 |
| Net (in minus out) | 6,821,000 | 4,941,000 |
| Players behind the totals (weekly actives) | 15,310 | 9,640 |
| Median Glow Dust held at end of week, weekly actives | 4,900 (n = 15,310) | 7,600 (n = 9,640) |
| 90th percentile held | 17,500 | 41,000 |

Terrarium Shop (Glow Dust items) purchases: week 2 18,250 items, week 3 41,820 items (+129%).

Parade Sparks (event currency, no expiry rule):

| Measure | Sparks |
| --- | --- |
| Issued during the event | 4,010,000 |
| Spent in the Parade shop | 2,760,000 |
| Swapped to Glow Dust at the Spark Swap (10 Sparks = 150 Dust), through Sun 10-11 | 41,400 |
| Swapped to Glow Dust at the Spark Swap (10 Sparks = 150 Dust), Mon 10-12 to Tue 10-13 15:00 (event still open) | 77,100 |
| Swapped to Glow Dust at the Spark Swap (10 Sparks = 150 Dust), Tue 10-13 15:00 to Sun 10-18 (event closed) | 112,300 |
| Swapped to Glow Dust at the Spark Swap (10 Sparks = 150 Dust), Mon 10-19 | 14,200 |
| Still held on 2026-10-19 | 1,005,000 by 6,120 players |

**B9. Device performance (Reed Pond area, sessions with at least 60 s there, week 3)**

| Group | Sessions | Sessions with 10th-percentile FPS below 24 |
| --- | --- | --- |
| Phone | 6,120 | 790 / 6,120 (12.9%) (week 2: 1,010 / 9,880, 10.2%) |
| PC | 2,380 | 41 / 2,380 (1.7%) |

**B10. Peer band (Roblox benchmark):** UNAVAILABLE this week (not pulled; the game is three weeks old, so the pool comparison would be weak).

### C. Tests and updates
| Item | Status | Players / days so far vs plan | Readable on | Note |
| --- | --- | --- | --- | --- |
| Lantern Parade (1.1.0) | done | 11,420 entrants; 6 days after the event are in | Return numbers readable now; D7 for the 10-12 start day is in (56 / 1,020), the 10-13 start day is readable on 2026-10-21 | Observational only; no test ran |
| "Tell us" in-game form (1.1.0) | running | Shown to 1,460 players since 2026-10-08; 22 answered (1.5%) | n/a | Shown after a player's 3rd net round, at most once per 7 days |
| Terrarium save batching (1.1.1) | live | n/a | n/a | No before/after plan was written |
| Reed Pond phone performance pass | planned | not started | after release | Committed by engineering (see capacity) |

### D. Player voice
Not used in this page. The analyst did not read the raw feedback this week; the live-ops designer owns the feedback sort. The only feedback number here is the form exposure in section C.

### E. Other explanations we checked
| Explanation | What we would see if true | What we saw |
| --- | --- | --- |
| The post-event drop is only the launch spike fading | New players per day falling and returning players steady | New per day fell from 930 (Thu 10-08) to 760 (Thu 10-15), but returning players fell too (1,850 to 1,370). The launch spike alone does not explain it, but we cannot split the two with this data |
| Event-day new players are lower quality because of where they came from | A different traffic-source mix | Source shares are not comparable across the 2026-10-12 recording change, so we cannot rule this in or out |
| The lantern step is a logging problem on phone | `lantern_placed` rates low everywhere | `lantern_placed` is logged by the server for all platforms; PC places a lantern for 80.0% of its new players and console for 72.1%; tablet is in between at 52.0%. These are in line with how far each group got in earlier steps |
| Phone players are simply less committed | Low D1 even for players who got through the step | Phone players who placed a lantern came back at 30.7% (week 2); PC overall was 20.8%. The step looks like the difference |

### F. Limits
- The reason phone players stop at the lantern step is unknown. The page shows where, not why.
- Bead grants: sales report 188 against 181 `beads_granted` events in week 3 (7 fewer, 3.7%); week 2 was 262 against 261. The sales report is by UTC day and can be a day late; `beads_granted` is written by the game server after it grants, and a log call can be lost if the server closes at that moment. We have not looked at individual transactions.
- `crate_info_opened` shows 0 events from phone and tablet since launch. It is not clear if the panel is not opened, not reachable, or not logged on those devices.
- Week-3 cohorts have not finished 7 days. No cohort has 30 days.
- Discovery-source counts changed on 2026-10-12. Console numbers are small (n under 400 per cohort); do not read their rates closely.
- Event return numbers are observational. People who enter events are different from people who do not.
- Funnel starts 2026-10-05 because tutorial events exist from build 1.0.2 (2026-10-02).

### G. Routing
| To | What they need from this week | Ticket |
| --- | --- | --- |
| owner | Part 1 | none |
| game-designer | Phone first-session step 3 (placing a lantern) and the Zone 3 and Zone 4 access numbers in B6 | none yet |
| progression-designer | Glow Dust in and out (B8), Spark Swap Dust issued, median held Dust | none yet |
| marketing | Event-day new players came back less often; source mix not comparable after 10-12 | none yet |
| live-ops-designer | Event reach, displacement and return after the event (B5), Spark balances (B8) | none yet |
| engineering | Client-side build-mode events on phone; a check of the bead grant events against the sales report; info-panel logging on phone | none yet |
