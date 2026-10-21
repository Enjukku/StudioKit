---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J013-T05b (SYNTHETIC TEST DATA, universe 9000000001)
supersedes: []
---
**SYNTHETIC TEST DATA.** Universe 9000000001 does not exist. The lead generated this history through the real `tools/analytics` pull code with a fake transport (`.tools/analytics-data/9000000001/README-TEST.md`). Never report these numbers as a real game.

> Author: analyst · claude-opus-5-5 · high · 2026-10-21

# Why next-day return fell from about 21% to about 16%

Question (owner, J013 G2): "Our next-day retention dropped from about 21% to about 16% over the last few weeks. Why, and what should we do?"

## Part 1. For the owner

**What happened.** Most of the drop came from who arrived, not from a worse game. The creator video on Oct 4 brought many extra new players who rarely come back the next day. The only part we can link to the game is a phone problem that started with version 112 on Oct 9. That problem is still there.

**Why we think so.**
1. **The rate fell, but the number of players who came back did not.** In the week before the video (Sep 27 to Oct 3), 4,348 new players came and about 932 came back the next day (21.4%). In the latest full week we can read (Oct 11 to 17), 5,954 new players came and about 952 came back (16.0%). That is 5.4 points lower: about a quarter fewer returns per new player (likely range: 3.9 to 7.0 points lower). In the three weeks before the video, the rate moved by less than 0.1 point from week to week. [S6, S7, S8]
2. **The first drop came on the day of the video, from one source only.** On Oct 4, new players went from 582-692 per day to 1,188. Daily players from "Other" (the source that holds outside links) went from 421-485 to 993. In the first 5 video days, about 2,201 extra new players came, and only about 185 of them came back the next day (about 1 in 12). Players from Friends, Home and Search came back exactly as often as in the week before. Crashes and frame rate did not change on those days. [S6, S7, S9]
3. **The second drop came with version 112, on phones only.** From Oct 9, phone players crash about twice as often: 1.82%-1.98% of play sessions, against 0.72%-0.88% before. Out-of-memory exits went from 10-12 to 39-41 per day. On phones, the slowest frames fell from about 31 to about 22 frames per second. Computers and consoles did not change. [S9]
4. **Phone players now come back less often than before, compared with computer players.** Against the same weekday one week earlier, phone return fell about 4 points more than computer return (3.9 to 4.1 points), on all 7 days after Oct 9. The same check one week earlier shows no gap (less than 0.1 point). Players from Friends, Home and Search also came back about 2 points less from Oct 9 (Home: 22.1%-23.0% before, 19.9%-20.7% after). [S9, S10]
5. **A rough split (an estimate, not a measurement):** of the 5.4 points in the latest week, about 3.5 points come from who arrived. About 1.9 points remain, and the phone problem fits that size. [S6]
6. **Ruled out:** Roblox's counting change on Oct 12 (both drops started before it, and nothing moved on Oct 12). Normal week-to-week movement (much smaller). Money: Robux per day and the number of payers did not fall. [S6, S9]

**How sure we are: Medium.**
- Are the numbers right? Mostly. The groups are large, and every group of new players we used has had its full day to come back. But three data checks failed. The phone, computer, console and tablet values for next-day return do not add up to the total. Tablet and console values are identical every day from Oct 9. Four server and session series are exact copies of each other. We did not use the failed series for any main claim, and the crash and frame-rate numbers come from a separate source. [S4, S6]
- Do we know why? Partly. This is a before-and-after comparison with matched weekdays and a check one week earlier. It is not a fair test. The video and version 112 came 5 days apart, so we can separate them. We do not know *why* the video players leave: a different audience, or a video that promises something the game does not show. We do not know which part of version 112 hurts phones.
- Is acting worth the risk? Yes. A crash problem that affects the largest player group is worth a fix even without a test, and a fix is easy to check.

**What we recommend.** Engineering (the performance engineer, through the lead) finds and fixes what version 112 changed for phone players. Players: everybody on phones. How we will know it worked:
1. In the first 3 full days after the fix: the phone crash rate is back inside 0.72%-0.88% of sessions, and the slowest phone frames are back at 30 frames per second or more.
2. In the first 7 full days of new players after the fix: next-day return of Friends, Home and Search players is back inside its range from before Oct 9.

Review date: **2026-11-04**, or 10 days after the fix goes live, whichever is later.

What to expect: the total rate will not go back to 21% while extra video players still arrive. With the phone problem fixed and today's player mix, an estimate is near 18%. That is not a failure of the fix. [S6]

**Your decision.** None is needed now. One option for you: publish version 111 again for everybody until the fix is ready. If the crash rate then returns to its old level, that also confirms version 112 as the cause. Default if you do not answer: no rollback, engineering fixes version 112 forward.

---

## Part 2. For the team

### 2.1 Brief and metric contract

| Label | Value |
| --- | --- |
| decision | where to act on the D1 drop: game fix, marketing, or nothing |
| unit | player (new player, first-play cohort) |
| eligible population | all new players of universe 9000000001 (TEST), first play 2026-09-09..2026-10-18 UTC |
| window | first-play dates, UTC days, start inclusive; D1 = return on the 2nd day counting first play as day 1 |
| numerator / denominator | `ForwardD1Retention` value per first-play date; counts estimated as rate × new players (A1) |
| definition version | Roblox `ForwardD1Retention` (no event versions: this game has no telemetry plan); breaks crossed: 2026-10-12 discovery pipeline (not used for discovery metrics here) |
| source | pulls `da92f66a1c21` (weekly, 2026-10-21T06:01Z), `aeb68b544ba4` (performance, 06:03Z), `3a0a68c06b50` (ad-hoc, 06:05Z); `show` outputs in `calc/` |

Fixed by the brief: today 2026-10-21; calendar = version 112 live 2026-10-09, creator video 2026-10-04, nothing else; no key, no new pulls.

Assumptions (all labelled where used):
- **A1** The D1/D7 cohort of a date = `DailyActiveUsers` with `IsNewUser=true` that date. Roblox does not document the API denominator. Returner counts are estimates (`round(rate × new players)`).
- **A2** `Forward*` values sit on the first-play date (unknown to settle, `analysis-craft/references/data-tools.md` §4).
- **A3, A4** only for the rough split (§2.6): the latest week holds W0's number of usual new players; extra players return at the rate measured for the first 5 video days.

### 2.2 Sources (every number above cites one)

| Id | File (all in `calc/`) | Holds |
| --- | --- | --- |
| S1 | `show-*.json` (27 files) | raw `analytics.py show` output per metric; `show-stderr.txt` = bucket, not-final and revision counts |
| S2 | pull log `.tools/analytics-data/9000000001/pulls.jsonl` | the three pull ids above, all ok |
| S3 | `maturity-all-cohorts.json` | `stats maturity` for all 88 retention cohorts (lag 1, PROPOSAL) |
| S4 | `derived-counts.json` → `reconciliation` | segment sums, total inside segment range, identical series |
| S5 | `derive_counts.py`, `ranges_other_metrics.py` | the two calculation scripts (read only S1 files; rerun from `calc/`) |
| S6 | `derived-counts.json` → `periods`, `excess_split_video_days`, `latest_week_rough_split`, `daily` | weekly new players, estimated returners, the excess split, the rough split |
| S7 | `stats-diff-d1-*.json`, `stats-diff-d7-W0-vs-W1.json` | `stats diff` (Newcombe) for each period comparison |
| S8 | `stats-diff-d1-Wm2-vs-Wm1-normal-movement.json`, `stats-diff-d1-Wm1-vs-W0-normal-movement.json` | normal week-to-week movement |
| S9 | `ranges-other-metrics.json`, `derived-counts.json` → `segment_ranges` | min-max per period (never averages of daily rates) |
| S10 | `stats-did-d1-phone-vs-computer-v112.json`, `stats-did-d1-phone-vs-computer-placebo-week-before.json` | `stats did` per matched weekday |

### 2.3 Data checks (checklist rows 2-4)

| Check | Result | Evidence |
| --- | --- | --- |
| history fresh | PASS: weekly, performance, ad-hoc pulled 0.2 days before reading | `status` 2026-10-21T12:00Z (S2) |
| point status | `ForwardD1/D7/D30Retention`, DAU, performance: all final except `ClientCrashRate15m` Console = `NotStatisticallySignificant` on all 26 days (not used) and revenue metrics 2026-10-19, 10-20 = `Projected` (not used) | S1 `show-stderr.txt`; `ranges-other-metrics.json` `not_final_points` |
| revisions | 0 revised buckets in every metric | S1 `show-stderr.txt` |
| maturity | D1: 40 of 41 cohorts mature; 2026-10-19 not mature (readable from 2026-10-22T00Z) → excluded. D7: 2026-10-13 not mature → excluded. D30: only to 2026-09-20 → not used | S3 |
| maturity vs API | CONFLICT: the API already returned final values for D1 2026-10-19 and D7 2026-10-13; the tool's 1-day lag is a PROPOSAL. Kept the tool's stricter reading | S1, S3 |
| DAU segments add up | PASS: Platform sum and IsNewUser sum = total within ±1 player every day; AcquisitionSource sum − total within −1..+2 | S4 |
| D1 total inside platform range | **FAIL**: on 13 days (2026-10-04..10-16) the total D1 is below every platform's value (e.g. 10-04: total 0.1572, platform min 0.1793). Impossible for a complete split. A platform value may be missing (missing is not zero) or the split is wrong | S4 `d1_total_outside_platform_range` |
| D1 total inside source range | PASS on all 25 days with the split | S4 |
| identical segments | **FAIL**: `ForwardD1Retention` Tablet = Console exactly on all 11 days 2026-10-09..10-19 | S4 `d1_tablet_equals_console_days` |
| identical metrics | **FAIL**: `ServerFrameRateP10`, `ServerFrameRateP50`, `MemoryUsageP90`, `SessionDurationSecondsP50` hold the same value every day (e.g. 9.94 on 2026-09-25). Four different metrics cannot match → not used | S4, S1 |
| crash total vs version | **FAIL (bounded)**: from 2026-10-09 only version 112 is returned, but the total crash rate differs from it (10-09: total 0.0131, v112 0.0147). Version 111 may still run and be missing from the response | S4 `crash_total_ne_only_returned_version` |
| measurement breaks | 2026-10-12 discovery pipeline: crossed by the window. No step on 10-12 in D1 total, D1 by source or Home daily players (2,178 on 10-11, 2,119 on 10-12). Event version breaks: none (no events) | S1, S9 |

Effect on the claims: phone vs computer D1 (S10) comes from the failed platform split. It is used only as a within-split comparison, never for levels, and the version-112 claim rests first on crash, OOM and frame-rate data.

### 2.4 Timeline against the breaks

| Date (UTC) | What changed | Source | Seen in the data |
| --- | --- | --- | --- |
| 2026-09-09..10-03 | nothing | calendar (lead) | D1 0.2109-0.2173 every day; new players 582-692 per day (S9) |
| **2026-10-04** | creator video goes up | calendar (lead) | D1 0.1572; new players 1,188; Other daily players 993 (421-485 before); peak concurrent 478 (398-420 before) (S1, S9) |
| **2026-10-09** | place version 112 goes live | calendar (lead) | phone crash rate 1.97%; crashes 93; OOM exits 41; phone FPS P10 22.6 (S1) |
| 2026-10-12 | Roblox discovery recording change (Home, Search, Charts) | `metrics-roblox.md` §6 | no visible step (§2.3) |
| 2026-10-09..10-18 | video traffic fades | — | Other daily players 880 → 643; new players 959 → 814 (S1 `show-DailyActiveUsers.json`) |

### 2.5 Describe: the size of the drop (counts next to rates)

| Period (first play) | New players | Returned next day (est., A1) | D1 | Source |
| --- | --- | --- | --- | --- |
| W-2 2026-09-13..19 | 4,340 | 929 | 21.4% | S6 |
| W-1 2026-09-20..26 | 4,343 | 930 | 21.4% | S6 |
| W0 2026-09-27..10-03 (before video) | 4,348 | 932 | 21.4% | S6 |
| W1 2026-10-04..10 (video; v112 from Fri 10-09) | 7,223 | 1,143 | 15.8% | S6 |
| W2 2026-10-11..17 (latest mature whole week) | 5,954 | 952 | 16.0% | S6 |

| Comparison | Difference (points) | Likely range (95%) | Relative | Source |
| --- | --- | --- | --- | --- |
| W-2 → W-1 (normal movement) | +0.01 | −1.72 to +1.73 | 0.0% | S8 |
| W-1 → W0 (normal movement) | +0.02 | −1.70 to +1.75 | +0.1% | S8 |
| W0 → W1 | −5.61 | −7.10 to −4.14 | −26.2% | S7 |
| **W0 → W2 (the owner's question)** | **−5.45** | **−6.99 to −3.92** | **−25.4%** | S7 |
| D7, W0 → W1: 391 of 4,348 → 480 of 7,223 | −2.35 | −3.39 to −1.34 | −26.1% | S6, S7 |

D7 fell by the same relative amount as D1 for the video week. The returner count rose for both.

Weekly distinct players (`DailyActiveUsers` `OneWeek`, buckets start on the date shown): 16,351 (09-23), 20,088 (09-30), 22,158 (10-07), 19,575 (10-14) (S1). Session length: 13.77-14.62 minutes before the video, 12.18-13.02 in the video days, 11.37-12.22 after version 112 (S9). Session length falls when many new players arrive (`diagnosis.md` §1); it is not read as a separate signal.

### 2.6 Who arrived (checklist row 5)

Only "Other" changed on 2026-10-04. Ranges are daily min-max (no denominators by source were pulled, so no averages):

| Source | D1 2026-09-27..10-01 (B0) | D1 2026-10-04..08 (B1) | D1 2026-10-09..13 (C1) | Daily players B0 → B1 |
| --- | --- | --- | --- | --- |
| Friends | 27.6%-28.5% | 27.5%-28.6% | 25.4%-26.3% | 550-633 → 610-667 |
| Home recommendations | 22.2%-22.9% | 22.1%-23.0% | 20.0%-20.7% | 1,650-1,900 → 1,820-1,976 |
| Search | 23.7%-24.4% | 23.5%-24.5% | 21.5%-22.2% | 304-350 → 335-364 |
| Other (outside links) | 16.8%-17.3% | 10.0%-10.4% | 10.5%-11.0% | 421-485 → 875-993 |

Source: S9 (`derived-counts.json` `segment_ranges`). Every source holds its B0 rate in B1 except Other, whose volume doubled. That is the "recompute within comparable groups" answer: inside the usual sources nothing changed on 2026-10-04.

**Excess split, video days before v112** (S6 `excess_split_video_days`; S7): B0 = 3,087 new players, about 663 returned (21.5%). B1 = 5,288 new players, about 848 returned (16.0%). If the usual players kept B0's count and rate, the 2,201 extra players brought about 185 returners: **8.4%** (stats diff vs usual players: −13.1 points, range −14.9 to −11.2; the extra group is derived, not measured).

**Rough split of the latest week** (ESTIMATE, A1 + A3 + A4; S6 `latest_week_rough_split`): 1,606 extra new players in W2. Mix alone predicts 1,067 returners (17.9%). Observed 952 (16.0%). Mix explains about **3.52** points, **1.93** points remain (115 returners). Consistency check, not proof: a 4-point drop on phones (§2.7) spread over phone players, the largest group (1,884 of 3,216 daily players on 2026-10-20, S1), gives about that size.

Not available: new players by source (needed for an exact adjusted rate; next measurement N1).

### 2.7 Technical experience (checklist row 6)

| Measure | Before v112 (2026-09-25..10-08) | After v112 (2026-10-09..10-20) | Source |
| --- | --- | --- | --- |
| Crash rate, phone (crashes per ended session) | 0.72%-0.88% | 1.82%-1.98% | S9 |
| Crash rate, computer | 0.36%-0.44% | 0.36%-0.44% | S9 |
| Crash rate, tablet | 0.81%-0.99% | 0.81%-0.99% | S9 |
| Crash rate, console | `NotStatisticallySignificant` every day: not read | same | S1 |
| Client crashes per day (all) | 34-42 | 86-94 | S9 |
| Out-of-memory exits per day | 10-12 | 39-41 | S9 |
| Client memory P90 (all; unit as Roblox reports it) | 1,422-1,479 | 1,571-1,628 | S9 |
| FPS P10, phone | 30.4-31.6 | 21.4-22.6 | S9 |
| FPS P10, tablet | 32.4-33.7 | 28.3-29.6 | S9 |
| FPS P10, computer / console | 51.0-53.0 / 47.1-49.0 | 51.0-53.0 / 47.0-48.9 | S9 |
| FPS P50 (all) | 53.7-55.9 | 48.7-50.9 | S9 |

The video days (2026-10-04..08) show no change in any of these, so the extra players did not bring the crashes.

**Phone vs computer D1, per matched weekday** (S10; `stats did`, rates only, no interval because new players by platform were not pulled):
- After v112 (2026-10-09..15 vs the same weekdays 7 days earlier): −0.0390 to −0.0409 on all 7 days.
- Placebo, one week earlier (2026-10-02..08 vs 2026-09-25..10-01): −0.0005 to +0.0004.
- Limits: the platform split failed reconciliation (§2.3); place version equals date (no day with both 111 and 112 returned), so any other change on 2026-10-09 would look the same. The calendar names none.

**Overall step at v112** (S7): B1 → C1 = −0.53 points (range −1.97 to +0.91). The total does not show the step on its own, because the video players were leaving the mix in the same days. The step shows inside each usual source (§2.6) and on phones (above).

### 2.8 Competing explanations (checklist row 10)

| # | Explanation | If true we would see | Evidence for (data) | Evidence against (data) | Verdict | Who acts |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | **Player mix**: the video brought new players who return less | a step on 10-04 in one source; usual sources unchanged; more returners in total | 10-04 step; new players 1,188 vs 582-692; Other 993 vs 421-485; Friends/Home/Search unchanged in B1; returners up (932 → 1,143 in W1); extra players 8.4% (S6, S9) | Other's own rate also fell (expected: the video players sit inside Other); exact mix-adjusted rate needs new players by source; the platform split shows no 10-04 change, but that split failed reconciliation | **Supported** for the 10-04 step; "linked to" | marketing (information) |
| E2 | **Phone performance regression in v112** | crash, OOM, FPS change on phones from 10-09; phone D1 falls against computer; usual sources fall | phone crash 0.72-0.88% → 1.82-1.98%; OOM 10-12 → 39-41/day; phone FPS P10 ~31 → ~22; computer unchanged; phone DiD −3.9 to −4.1 points on 7 of 7 days, placebo ~0; Friends/Home/Search −2 points from 10-09 (S9, S10) | explains only the second, smaller part; version = date (no overlap); phone D1 from a failed split; total shows no clear 10-09 step (−0.53, range −1.97 to +0.91) | **Supported** for the remaining ~2 points; "linked to"; the technical defect itself is measured | performance engineer (via lead) |
| E3 | **Promise mismatch**: the video shows something the first session does not give | extra players leave early in the first session; feedback about it | extra players return at 8.4%, half of Other's pre-video 16.8-17.3% | nothing in the data separates "a different audience" from "a broken promise": no funnel, no feedback, no session data by source | **Open** | marketing + game designer, after observed play |
| E4 | **The game got worse for everyone on 10-04** (bug, config, content) | all sources and platforms drop on 10-04 | the date | no build, config or event on 10-04 (calendar); usual sources unchanged in B1; crashes and FPS unchanged 10-04..08 | **Rejected** | — |
| E5 | **Measurement change** (2026-10-12 discovery pipeline) | the step lines up with 10-12 | — | both steps (10-04, 10-09) come before 10-12; no step on 10-12 in D1 total, D1 by source or Home daily players | **Rejected** for the drop; separate data-quality failures noted in §2.3 | analyst |
| E6 | **Normal movement or season** | similar moves in earlier weeks | — | earlier weeks moved +0.01 and +0.02 points; the drop is −5.45 (S7, S8) | **Rejected** | — |
| E7 | **Progression wall or content exhausted** | slow decline among advanced players; late-funnel losses | D7 fell (8.99% → 6.65%) | a one-day step on 10-04 in new players' first return does not fit a wall; D7 fell by the same relative amount as D1 (−26%), as expected from mix; no progression or funnel events exist to test it | **Not tested** (no data), not supported | progression designer, if events are added |

### 2.9 Diagnosis checklist (`diagnosis.md` §10)

| # | Step | Result | Evidence and judgment |
| --- | --- | --- | --- |
| 1 | Define the loss | PASS | §2.1: D1 of new players, first play 2026-09-09..10-18, baseline W0 932 of 4,348, now W2 952 of 5,954 |
| 2 | Verify measurement | **FAIL** (bounded) | §2.3: platform D1 split does not reconcile; Tablet = Console; four identical performance series; v111 crash rate missing after 10-09; A1 denominator undocumented. Bounded: failed series not used for levels or main claims. FAIL action: re-pull and settle (N2, N3, N5) |
| 3 | Check maturity | PASS | S3: every D1 cohort used (to 2026-10-18) and D7 cohort used (to 2026-10-10) mature by the tool; non-mature 10-19 (D1) and 10-13 (D7) excluded |
| 4 | Check reliability | PASS for totals, **FAIL** for segments | totals: thousands of new players per week, Newcombe ranges exclude 0 (S7). Segments: no denominators by source or platform → no ranges for segment effects. FAIL action: N1, N2 |
| 5 | Check who arrived | PASS | §2.6: source mix, new vs returning, retained counts next to rates, within-source comparison |
| 6 | Check technical experience | PASS (checked; defect found) | §2.7: crash count and rate, OOM, FPS P10/P50, memory P90 by platform and version. Join failures not measured |
| 7 | Locate the break | **FAIL** | located in time (10-04, 10-09) and segment (Other; phones), not in the first session: the game has no funnel or onboarding events (no `knowledge/design/telemetry.md`). FAIL action: name the missing measurement (N7) |
| 8 | Check progression | **FAIL** | no progression events. FAIL action: N7; E7 stays "not tested" |
| 9 | Check economy and purchases | **FAIL** (partly read) | no economy events. Revenue read only: Robux per day 10,486-12,094 before the video, 10,888-12,744 after (to 10-18); payers per day 93-98 → 97-103; payer share fell 3.06-3.26% → 2.33-2.84% because more non-paying new players arrived; ARPPU unchanged 112.4-122.9 → 112.1-123.9 Robux (S9). No sign that purchases drive the drop |
| 10 | Competing explanations | PASS | §2.8: 7 explanations, predictions, evidence against each |
| 11 | Triangulate | **FAIL** | no observed play, no player feedback in this task. FAIL action: playtest on a phone with v112 (performance engineer's recipe) and a first-session observation of video-like players; owner Feedback export (§2.11) |
| 12 | Bound the cause | PASS | wording: "linked to" for E1 and E2; "we do not know why the video players leave" for E3; no "caused" (no test) |
| 13 | One decision | PASS | Part 1: one action, owner, players, measure, review date 2026-11-04 |

Rows still FAIL (they cap "how sure" at Medium): 2, 4 (segments), 7, 8, 9, 11.

### 2.10 Claim strength

- Design: matched-weekday before/after, within-segment comparison, difference in differences with a placebo week. Game-wide release, no untreated group, no test → description plus "linked to" (`experiments-updates.md` §7; `diagnosis.md` §5).
- A rollback to version 111 (owner option) would be a reversal design: a stronger check of E2 than anything we have now.

### 2.11 Next measurements (when the key is set: "set the key (see tools/analytics/README.md)")

| Id | Pull | Settles |
| --- | --- | --- |
| N1 | `DailyActiveUsers`, `OneDay`, breakdown `AcquisitionSource`, filter `IsNewUser` = true, 2026-09-09..10-21 (check the filter format in `tools/analytics/README.md` and the catalog first) | exact mix-adjusted D1 (replaces the A3/A4 estimate) |
| N2 | `dims --metric ForwardD1Retention --dimension Platform`; `DailyActiveUsers` new players by `Platform` | which platform value is missing; counts for phone vs computer ranges |
| N3 | `ClientCrashRate15m`, `ClientCrashCount`, `OomUnexpectedExits` by `Platform` and `PlaceVersion` together; `ClientMemoryUsageP90` by `Platform`, `MemoryGroup` | whether the crash rise is phones-on-112 only, low-memory phones in particular; whether v111 is missing or zero after 10-09 |
| N4 | `ClientFpsP10` by `OperatingSystem` | device group for the performance engineer |
| N5 | re-pull `ServerFrameRateP10`, `ServerFrameRateP50`, `MemoryUsageP90`, `SessionDurationSecondsP50`, then `show --revisions` | whether the identical values are a pull fault |
| N6 | after the fix: `pull --set performance`, then `ForwardD1Retention` by `AcquisitionSource` and `Platform` | the recommendation's success measures |
| N7 | measurement spec for first-session funnel events (via `analysis-craft/references/event-planning.md`) — a separate job, not started | checklist rows 7, 8; E3, E7 |

Owner export (optional): Audience → Feedback CSV for 2026-10-01..10-20, to read phone complaints and comments from new players (counted as people, `diagnosis.md` §6).

### 2.12 Owner actions
1. Set `ROBLOX_ANALYTICS_API_KEY` so the analyst can pull N1-N5 (`tools/analytics/README.md` §1).
2. Optional: decide on a rollback to version 111 (Part 1, "Your decision"). No other Creator Hub action is needed. The analyst changed nothing in Creator Hub.

### 2.13 Hand-offs
- `brief-performance-engineer.md`: the v112 phone regression (through the lead). The recommendation.
- `brief-marketing.md`: source quality of the video traffic; promise match still open (E3). Information and one check, not the recommendation.
- Game designer, progression designer, live-ops: no brief. Nothing in this data locates a first-session or progression problem (rows 7-8 FAIL for lack of events).

### 2.14 Questions tried (all of them, nulls included)
1. Did D1 move by weekday or week before the video? No (S8).
2. Did any source other than Other change on 10-04? No (S9).
3. Did any platform change on 10-04? Not in the platform split, but that split fails reconciliation (S4).
4. Did crashes or FPS change on 10-04? No (S9).
5. Did the total D1 step at 10-09? Not clearly (−0.53, range −1.97 to +0.91; S7).
6. Did usual sources step at 10-09? Yes, about 2 points each (S9).
7. Did phones step against computers at 10-09? Yes, about 4 points, 7 of 7 days; placebo week no (S10).
8. Did anything step at the 2026-10-12 break? No (S1, S9).
9. Did revenue or payers fall? No; payer share fell only because the denominator grew (S9).
10. Can D30 help? No: only cohorts to 2026-09-20, before both events (S1, S3).
