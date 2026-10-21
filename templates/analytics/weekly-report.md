---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J013; owner's analyst paper Appendix D (knowledge/reference/analyst/03-practice-diagnosis-reporting.md §4); analysis-design, analysis-craft
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Weekly player data: <game> · <first day yyyy-mm-dd> to <last day yyyy-mm-dd> (UTC)

Workflow: `analysis-craft` §3 (weekly). Copy to `knowledge/jobs/<job>/analyst/weekly/<yyyy-mm-dd>.md`, or the game's `knowledge/analytics/weekly/<yyyy-mm-dd>.md` (name it by date, never `report*`).

**Rules of use.** Part 1 is for the owner: plain words, no statistics terms, one page. Part 2 is for the team and for checking: every number there has a source. A value we do not have is `UNAVAILABLE`, never 0. Every rate shows its counts. A D7 or D30 number is shown only for cohorts that have finished their 7 or 30 days. A quiet week is a valid result: "no real change" is a finding. Urgent problems (crashes, broken purchases, lost saves) go to the owner at once, not here.

---

## Part 1 — For the owner (read this, skip the rest if you like)

| | |
| --- | --- |
| **What happened** | <one plain sentence: which players, what changed, how much, compared with what. Example shape: "New players this week came back the next day less often than last week: 1 in 6 instead of 1 in 5."> |
| **Why we think so** | <the evidence in 1-3 short lines: counts, the comparison, what we ruled out> |
| **How sure we are** | <High / Medium / Low> because <the reason in plain words: enough players or not, finished cohorts or not, a test or only a before/after, data problems> |
| **What we recommend** | <one action> · who: <role> · for which players: <...> · how we will know it worked: <measure> · check again on: <date> |
| **Your decision needed** | <the choice, or "none this week"> |

<one chart, only if it answers the main question; caption = the finding and its limit>

---

## Part 2 — For the team and for checking

### A. Data used
| Field | Value |
| --- | --- |
| Pull | `tools/analytics/analytics.py` run id(s), pulled at (UTC) |
| Last pull before this one | date; warn if more than 21 days ago (performance data is kept 28 days only) |
| Data complete through | last full UTC day; days with `Projected` or `NotStatisticallySignificant` points named |
| Measurement breaks in or near this period | for example 2026-10-12 (discovery counting changed); logging changes; new event versions |
| Builds and changes live this week | place versions, config changes, events, marketing pushes, with dates |
| Week and comparison basis | 7 full UTC days (default Monday to Sunday; the brief's dates win); comparison windows with their dates, same weekdays |

### B. Numbers
Each row: this week's value with its counts, the comparison (same weekdays, same cohort age), and what it means. Where a segment has rates but no counts, give the daily range (min-max), never an average of daily rates; estimated counts (rate × new players) say "estimate".

| Measure | This week (value + counts) | Comparison (value + counts, basis) | Plain meaning |
| --- | --- | --- | --- |
| New players and where they came from | | | Did the audience change? |
| First session: reached the core loop | eligible N, reached N | | Where are new players stuck? |
| Came back: D1 (finished cohorts) | cohort dates, N, returned N | | |
| Came back: D7 / D30 (finished cohorts only) | cohort dates, N, returned N | | |
| Session length / sessions per player | same population | | Longer visits or more visits? |
| Progress milestone reached (with non-finishers) | share + time, follow-up window | | Clear, hard, too expensive, or nothing left? |
| Paying players / spend per payer / spend per daily player | revenue basis, period | | More buyers or bigger buys? |
| Currency in, out, held | currency, population | | Are sinks used? |
| Device performance | device group, crash count, FPS low tail, memory high tail | matched devices | Who has a bad technical experience? |
| Peer band (Roblox benchmark) | raw value, band 50th-90th, pool, read date | | Position in this week's pool, not a target |

### C. Tests and updates
| Item | Status | Players / days so far vs plan | Readable on | Note |
| --- | --- | --- | --- | --- |
| <experiment or update> | running / readable / done | | <date> | early numbers are not results |

### D. Player voice
| Theme | Contributors / contributors read | Source and window | Matches the numbers? | Example (id) |
| --- | --- | --- | --- | --- |

### E. Other explanations we checked
| Explanation | What we would see if true | What we saw |
| --- | --- | --- |

### F. Limits
<missing data, traffic shifts, immature cohorts, unresolved alternatives>

### G. Routing
| To | What they need from this week | Ticket |
| --- | --- | --- |
| owner | priority and trade-off | Part 1 |
| game-designer | comprehension or challenge problems, where | |
| progression-designer | pace, cost or resource walls, which cohort | |
| marketing | source quality, promise match, mature cohort value | |
| live-ops-designer | event reach, displacement, return after the event | |
| engineering | logging gaps or broken events | |
