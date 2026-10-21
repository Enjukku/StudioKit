# Hand-offs: the analyst and the roles it works with

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-craft`. Format: `rules/messages.md` §2 (brief) and §3 (hand-back). Owner J013 brief 2026-10-21: hand-offs to the game designer, progression designer, marketing, live-ops designer (built in J014) and the engineering team (logging requests), in the brief format. The other sides: `marketing-craft/references/handoffs.md` §4 (marketing → analyst), `progression-craft/references/data-handoff.md` (progression designer → analyst), `progression-design/references/live-data.md` (how the progression designer reads our data).

The analyst sends **files, not chat**: the finding file (weekly page, investigation file or test result) holds the evidence; the brief points to it. Asks are tickets in the job ledger, inside the approved brief. A role marked *planned* does not exist yet: the brief goes to the lead, who holds it (J013-D6). The live-ops designer exists since J014 (its side: `live-ops-craft/references/handoffs.md` §2).

| To | When | The analyst gives | The analyst never gives |
| --- | --- | --- | --- |
| game-designer | a comprehension, challenge or first-session problem located | the affected journey, step, players, counts, competing explanations still open, observed-play evidence | a redesign, a feature list |
| progression-designer | a pace, cost or resource wall; after a curve change | the milestone, the share reaching it in a fixed window (non-finishers kept), time and attempts, affordability, the affected cohort | a global pacing change from survivors |
| marketing | source quality, promise match, a creative or title change to read | per-source mature cohort outcomes, the 2026-10-12 break, the test or observation label | "this thumbnail won" without counts and method |
| live-ops-designer | after an event or update | reach, use, displacement of normal play, return after the event, spending pulled forward | a launch spike as lasting engagement |
| engineering via the lead (feature-builder / quick-builder for events; performance-engineer for regressions) | a feature needs events; an event is broken; a performance or stability regression | the measurement spec (`event-planning.md` §3) and acceptance walk (§5), or the regression evidence (§6) | logging code; the fix |
| owner | every finding, every test plan before it starts | the answer shape (`analysis-design/references/reporting.md` §1), owner actions in Creator Hub | a decision taken for the owner |

## 1. Analyst → game-designer (a located problem)
```text
<intent>
New players are lost at one point of the first session, and the data shows where but not yet why. You own the design; I bring the evidence so you can choose the fix. The numbers, the comparisons and the explanations I could not rule out are in the finding file.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: game-designer
model: opus
effort: high                                   # game-designer, owner J003-D3
skills: [game-design]
refs:
  - <finding file path>   # take: the step, the eligible players and counts, the comparison, the explanations still open
  - <playtest or feedback file, if any>   # take: what players did; avoid: reading comments as how common the problem is
fixed:
  step: <funnel name / step id>                # pull <id>
  players: <eligible population, dates UTC>     # metric contract
  measured: <reached N of eligible N; baseline reached N of N>   # pull <id>
  open_explanations: [<from the competing-explanations table>]
open: [the fix, whether a playtest comes first, the order of changes]
avoid: [a redesign of the whole flow from one data point; changing several things at once if a test must read them]
owns: [design notes and briefs you write]
not_in_scope: [code, logging (the analyst sends engineering a measurement spec if the fix needs one)]
rules:
  - The finding says where players are lost; it does not prove why. Say which explanation your fix assumes.
  - If the fix should be tested, ask the analyst for the test plan before it ships (templates/analytics/ab-test-plan.md).
  - Never name a file report*, summary*, findings* or analysis*.
deliver: your chosen fix and the explanation it assumes, as a ledger hand-back
checks:
  - C1: the hand-back names the explanation the fix assumes and how we will know it worked (measure + date)
return: hand-back to analyst, copy to lead
</spec>
```

## 2. Analyst → progression-designer (a wall or a pace problem)
```text
<intent>
Players are slowing or stopping at one milestone. The data separates players who reached it from those who did not within the same window, so a hard step does not look easy. I need you to say whether this is difficulty, cost, clarity or nothing left to do, and the smallest lever to test.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: progression-designer
model: opus
effort: high                                   # progression-designer, owner J011-D1
skills: [progression-design, progression-craft]
refs:
  - <finding file path>   # take: share reaching the milestone in the fixed window, time and attempts, wallet vs price, cohort
  - <current curve revision>   # take: the predicted time to this milestone
fixed:
  milestone: <id>                              # telemetry plan row
  window: <N days after first play>            # metric contract
  measured: <reached N of eligible N; median active minutes among reachers; share short of the price>   # pull <id> / stats output
  predicted: <the curve's prediction for this milestone>   # curve revision
open: [the lever, re-simulation, whether to test]
avoid: [tuning the whole curve from survivors; adding sinks without naming the bottleneck]
owns: [curve revisions and data tables]
not_in_scope: [code changes, logging]
rules:
  - Keep non-finishers in every number (progression-design/references/live-data.md).
  - Name what the analyst must measure to confirm the change worked.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the proposed lever with its re-simulated outcome and the confirming measure
checks:
  - C1: the hand-back states the lever, the predicted change in share reaching and time, and the confirming measure
return: hand-back to analyst, copy to lead
</spec>
```

## 3. Analyst → marketing (source quality and promise match)
```text
<intent>
Marketing brings players; the data says which sources bring players who stay. Credit for a source is not proof it caused the players, and the 2026-10-12 recording change makes discovery numbers before and after not comparable. This is what the mature cohorts show by source.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: marketing
model: opus
effort: medium                                 # marketing roster, J012-D1
skills: [marketing-design, marketing-craft]
refs:
  - <finding file path>   # take: per-source cohorts with counts, maturity, the label (randomized / adaptive / attributed / observational)
fixed:
  sources: <AcquisitionSource values>          # pull <id>
  cohorts: <first-play dates, mature only>
  label: <observational / attributed / adaptive / randomized>   # how the data was produced
  break_crossed: <yes: 2026-10-12 / no>       # RF-55
open: [what marketing changes next]
avoid: [reading attributed numbers as caused; reading a pre-break vs post-break change as a creative effect]
owns: [campaign record, creative decisions]
not_in_scope: [analysis method]
rules:
  - Paid and organic players stay apart; immature cohorts are "pending".
  - Any test of a change gets the analyst's spec before it starts.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the marketing decision and its test or observation spec request, if any
checks:
  - C1: the hand-back uses the label given and mature cohorts only
return: hand-back to analyst, copy to lead
</spec>
```

## 4. Analyst → live-ops-designer
```text
<intent>
An event or update ran. Its launch spike is not the result: what matters is who joined it, what normal play it replaced, whether spending was only pulled forward, and whether players came back after it ended.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: live-ops-designer
model: opus
effort: medium                                 # live-ops-designer, owner J014-D1
skills: [live-ops-design, live-ops-craft]
refs:
  - <finding file path>   # take: reach among eligible players, use, displacement, post-event return, spend before/during/after
fixed:
  event: <id, start, end UTC>                  # event calendar (Events API or decision log)
  eligible: <population>                       # metric contract
  comparison: <same weekdays before; returning players' baseline>
open: [the next event's changes]
avoid: [comparing event players with non-players as if randomly chosen]
not_in_scope: [analysis method]
rules:
  - Event participants chose to join; compare with the eligible group, not with non-participants.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the live-ops decision and what the next event should measure
checks:
  - C1: the hand-back names the measure for the next event
return: hand-back to analyst, copy to lead
</spec>
```

## 5. Analyst → engineering (measurement spec; via the lead)
```text
<intent>
A new feature needs data that can answer one design question. The measurement spec says what each event means and which decision it serves; you choose how to log it within the analytics skill's rules and limits. Without it, after launch we will not be able to tell <explanation A> from <explanation B>.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: feature-builder (or quick-builder for one small event; the lead routes)
model: opus
effort: medium                                 # roster, owner J010
skills: [analytics, engineering-craft]
refs:
  - <measurement spec path>   # take: the event contracts (16 fields), ranked properties, acceptance walk
  - knowledge/design/telemetry.md   # take: existing events, names, versions
fixed:
  events: [<semantic names>]                   # measurement spec
  properties_ranked: {<event>: [<p1>, <p2>, <p3>]}   # measurement spec; max 3 custom fields (analytics T-05)
  version: <v1 / v2 + comparability note>
open: [method per event, call sites, module structure, bucket edges inside the spec's meaning]
avoid: [logging per frame, hit or pickup; client-side attempts; new event names for changing ids]
owns: [the telemetry module and plan rows]
not_in_scope: [dashboards, analysis]
rules:
  - Server only, after the server decided; one telemetry module; every call in pcall (analytics T-01..T-03).
  - No typed text, chat or personal data in any field (platform-policy).
  - Each event gets a row in knowledge/design/telemetry.md naming the question it answers.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: code + telemetry plan rows + the acceptance walk results
checks:
  - C1: each journey in the acceptance walk (success, cancel, retry, interruption, returning player) logs as the spec says, shown in Creator Hub View Events or a test log
return: hand-back to lead, copy to analyst
</spec>
```

## 6. Analyst → performance-engineer (a performance or stability regression; via the lead)
```text
<intent>
Since <version> went live, players on <devices> crash more and get slower frames, and they come back less often than players on other devices. The data shows where and when; it cannot show which part of the build costs the frames or memory. You find and fix the cause; the finding file has the numbers and the control devices.
</intent>
<spec>
id: <job>-T<nn>
from: analyst
to: performance-engineer (the lead routes)
model: opus
effort: high                                   # performance-engineer, owner J010
skills: [performance, engineering-craft]
refs:
  - <finding file path>   # take: before/after ranges per device for crash rate, OOM exits, P10 FPS, P90 memory; the version split; the control devices
fixed:
  version: <place version, live date UTC>      # release calendar / PlaceVersion pull
  devices: <Platform / OperatingSystem / MemoryGroup values affected>   # pull <id>
  before_after: {crash_rate: <range -> range>, oom_exits_per_day: <...>, fps_p10: <...>, memory_p90: <...>}   # pull <id>
  success: <crash rate back inside the before range; P10 FPS >= <value>, measured over 3 full days>   # finding file
open: [capture recipe, cause, fix, rollback advice]
avoid: [a fix measured on a computer only; judging by averages instead of the low and high tails]
not_in_scope: [analysis method, logging]
rules:
  - Roblox keeps performance data 28 days: the analyst's pulls are the history; ask the analyst for a fresh pull after the fix.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the cause, the change, before/after captures on the affected device class
checks:
  - C1: the hand-back names the cause and the fix, and the date it goes live, so the analyst can measure the success rule
return: hand-back to lead, copy to analyst
</spec>
```

## 7. What the analyst receives
| From | Ask | The analyst returns |
| --- | --- | --- |
| marketing | test spec before a change; reading at the date | `ab-test-plan.md` or an observational spec; the reading with its label |
| progression-designer | events and denominators for timeline targets; predicted values | a measurement spec per target; after launch, measured vs predicted |
| game-designer | "is this fun / where do players quit" | the answer shape; the diagnosis file |
| owner | any question; the weekly page | the answer shape; `templates/analytics/weekly-report.md` |
