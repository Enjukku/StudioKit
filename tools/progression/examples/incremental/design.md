# Bloom Valley: worked example of an incremental game

> Author: progression-designer · claude-opus-5-5 · high · 2026-10-21 (J011-T08, refreshed in J011-T12 on sim and chart 1.1.0; runs regenerated on 1.2.0 in J011-T13 with no value changed). Model `example-incremental-r2`, SHA-256 `fc64e5d6c02f3eb0…` (the full hash is in every run file).

**For learning, not tuning.** This is a teaching example. Only the flower pot uses published numbers (source M01, a 2016 article about an idle game, as re-checked in the owner's research paper). Every other number is an `EXAMPLE ASSUMPTION`. No number here is a target or a value for a real game. A "pass" below means that the simulator measured a time inside a window that I chose. It does not show that the game is fun.

**How to read the codes.** `TL-03` is row 3 of the feeling timeline; the same id is the goal id in `model.json` and in every run file. `G-01` is a row in the skill-gap list (`knowledge/jobs/J011-progression-designer/skill-gaps-T08.md`). Section 10 lists the files.

## 1. The game in short

- **What the player does.** Buys flower pots, then greenhouses. Both grow petals every second. Across a bridge lies the Sky Orchard, which grows much more.
- **The rebirth.** A **Replant** (this game's rebirth) resets the build-up and pays golden seeds. Each seed adds 0.1 % petals for ever. The first Replant also opens the bridge.
- **What a Replant keeps.** Seeds, pots, the watering can and the bridge pass. It removes petals, greenhouses, Sky Orchards and the bee hive. Kept pots make every later run start fast.
- **When it happens.** The model Replants by itself once a run has earned 7,000,000 petals. The player does not choose the moment (a model limit).
- **Sessions** (`EXAMPLE ASSUMPTION`). One 20-minute session a day. A second player plays days 1 and 2, is away for 6 days and returns on day 9.
- **Offline.** On return the player gets 5 % of the last petal rate for up to 2 hours of absence.
- **Monetization.** None. A real game that sells anything here must load the `platform-policy` skill.

The full inputs, with a label on every number, are in `model.json`.

## 2. The feeling timeline

All wording is a proposal; all windows are `EXAMPLE ASSUMPTION`s. In a real game the owner decides each row. "Active" = minutes of play; "calendar" = days since the first session. Appendix A has the full rows (sign to watch, purpose, playtest question).

| Row | When | What the player should feel | Shape | Window |
| --- | --- | --- | --- | --- |
| TL-01 | first minute | "I tap buy, and petals come faster." | fast start, power spikes | 2nd pot ≤ 10 s; 3 spikes ≤ 60 s |
| TL-02 | minutes 1-2 | "There is a second kind of thing to build." | new choice | first greenhouse ≤ 2 min |
| TL-03 | minutes 12-20 | "The garden is full. Buying slows down." | soft wall | first soft wall in 12-20 min |
| TL-04 | first Replant | "I give up my garden for something better." | reset | 20-30 min of play |
| TL-05 | the bridge | "The bridge I saw from the start finally opens." | hard wall | locked bridge seen ≤ 2 min; first Sky Orchard ≤ 30 min |
| TL-06 | first day | "Coming back gives me something new." | — | bridge open by day 2 |
| TL-07 | first week | "I have a rhythm." | — | 10 Replants by day 7 |
| TL-08 | first month | "I still have a goal." | — | 900 seeds between day 21 and day 30 |
| TL-09 | after a break | "Coming back costs me nothing." | catch-up | 10 Replants within 14 days |

**Thresholds** (in `model.json` → `analysis`, taken from the rows): a **soft wall** is a wait of 45 s or more between two purchases (TL-03). A **power spike** is one purchase that raises petals per second by 50 % or more (TL-01). A **hard wall** is the simulator's own definition: something the player can afford but may not buy yet.

## 3. The exact trace first

Before any simulation, `curves.py` computed the pot alone in exact fractions (Appendix B). The wait for the next pot falls until 15 pots (0.41 s), rises, halves at each x2 milestone (25 and 50 pots), then climbs without stop: 49 s at 139 pots. The first four waits (400/167 s, 214/167 s …) match the paper's check exactly. So the shape "waits shrink, then grow" comes from the published inputs, not from my tuning.

## 4. The model players

Each run is one named strategy, not the player population. All runs are exact mode and `--lean` (the event trace is left out to keep files small).

| Run file | Who | Play time simulated |
| --- | --- | --- |
| `runs/efficient.json` | Efficient: buys the most petals per second per petal (a rule of thumb, not the best possible play) | 1 h |
| `runs/explorer.json` | Explorer: always buys the cheapest thing | 1 h |
| `runs/one-track.json` | One-track: only ever buys pots | 1 h |
| `runs/daily.json` | Efficient, one 20-min session a day | up to 30 sessions; all goals reached on day 26 |
| `runs/returning.json` | Efficient, away from day 3 to day 8 | 10 sessions (to day 16) |

The T08 "rusher" run is gone: the new simulator finds the hard wall in every normal run.

## 5. Results

Each verdict comes from the simulator's goal with the same id. Evidence = run file, goal id, measured time.

| Row | Verdict | Evidence |
| --- | --- | --- |
| TL-01 | pass | `efficient.json`: TL-01a 3 s; TL-01b (third spike, the 25-pot milestone) 17 s |
| TL-02 | pass; **fail** for one-track | efficient 43 s; one-track never builds a greenhouse |
| TL-03 | pass; **fail** for explorer | efficient and daily: first soft wall ends at 992 s (16.5 min, greenhouse 72, wait 49 s); one-track 824 s; explorer 1593 s (26.6 min) |
| TL-04 | pass | efficient 1539 s (25.6 min, 118 seeds); daily 1201 s (offline petals finish the run at the start of day 2) |
| TL-05 | pass; **fail** for explorer by 1 s | TL-05a: the bridge pass is affordable but locked at 24 s; `walls.hard` keeps it locked for 1515 s. TL-05: first Sky Orchard at 1589 s; explorer 1801 s against 1800 s |
| TL-06 | pass | `daily.json` 86,402 s (day 2, second 2) |
| TL-07 | pass; **fail** for returning | daily 6.01 days; returning 12.01 days (by design: away for most of week 1) |
| TL-08 | pass, with a finding | daily 2,246,401 s (day 26). See finding 1. |
| TL-09 | pass | returning 12.01 days. Its Replants come at the same play times as the daily player's: the 6-day absence earned the same 2-hour offline cap as one night. Nothing lost, nothing extra. |

Calendar rows are "not testable" in the three runs without sessions, because calendar time needs a session pattern. Ledgers close with residual 0 in every run; no precision flag (the largest petal value is about 4 x 10^8, far below the 2^53 limit of Luau numbers).

## 6. Walls and spikes: planned or found

| What the simulator found | Where | Planned? |
| --- | --- | --- |
| 5 power spikes in the first 33 s: pots 2, 3, 25 and 50 and the watering can | every buying run | yes (TL-01). The 25 and 50 spikes are M01's published milestones. |
| Soft walls at the end of run 1 (greenhouses 72-77, waits 49-77 s) and at the end of every later run (Sky Orchards, waits 45-81 s) | efficient 7 walls in run 1; daily 82 walls in 26 days | yes (TL-03): every run ends in a wall, and the Replant is the exit |
| Hard wall: bridge pass affordable from 24 s, locked until the first Replant | every run (one-track: never opens) | yes (TL-05) |
| Hard wall: Sky Orchard affordable from 6.1 min, locked behind the bridge pass | every run | yes, the same gate seen one step later |
| No power spike after run 1 | all runs | found: kept pots remove the "first purchases double my income" moment. Option C adds one. |

## 7. Findings I did not plan

1. **The Replant loop weakens after week 1.** Seeds per Replant fall from 119 (day 2) to 8-9 (day 22). Each late Replant adds less than 1 % petals, and most sessions hold two Replants. TL-08 passes, but the reward behind it is thin. Cause: the requirement stays at 7,000,000 petals while the player gets stronger. Option B tests a rising requirement.
2. **Most sessions open with a Replant.** From day 8 to day 21, the offline petals finish the run in the first second of the session (18 session-start Replants in `daily.json`, also on days 2 and 4). Offline gives about 24.5 % of all petals up to day 26. That reads as "welcome back", but the first action of each day is always the same.
3. **One second decides a fail.** The explorer misses TL-05 by 1 s. A window is a proposal, not a law.
4. **The one-track player stalls at 13.7 min** with about 930 petals per second (139 pots). The greenhouse must be visible and named on screen in the first minute.

## 8. Options for the owner

Same player (efficient, daily sessions), same 30-session horizon, all three re-simulated (`options/runs/`).

| Option | What changes | What the player feels, and when | Evidence | Trade-off |
| --- | --- | --- | --- | --- |
| A. As is | — | Week 1: 1-2 Replants per session. Week 2: each adds 1-3 % petals; week 3: about 1-2 %. | `runs/daily.json`: 40 Replants by day 21; 900 seeds on day 26 | Thin late loop (finding 1). |
| B. Rising requirement | Each Replant needs 10 % more petals than the one before (`options/model-B.json`) | About one Replant per session. Each one is bigger and grows: week 2 adds 3.6-4.1 %, week 3 4.2-5.2 %. Only 3 sessions open with a Replant. | `options/runs/B-daily.json`: 20 Replants and 905 seeds by day 21 (A: 40 and 807); 900 seeds at day 21 plus 6 s | TL-07 (10 Replants in week 1) fails: day 8. The week-1 target must be re-stated. TL-08 passes by 6 s. |
| C. Moon Garden | A new area opens at the 10th Replant (`options/model-C.json`) | From day 6, every run has a second big moment: the first Moon Garden lifts petals per second x1.77. The loop stays thin. | `options/runs/C-daily.json`: 42 Moon Garden spikes; 45 Replants by day 21; 900 seeds on day 24 | One more area to make (art, UI). Does not fix finding 1. |

Uncertainty: each option is one strategy on assumed numbers. Whether players prefer many small Replants or fewer large ones is a playtest question.

**Recommendation: B.** It fixes the cause of finding 1 with one number, needs no new content, and mostly removes finding 2. Fewer resets also lose less build-up, so seeds arrive faster than in A. Re-state TL-07 as "about one Replant per session in week 1". C stays a good later content step. (T08 recommended C. The new simulator can raise the requirement per Replant, which was impossible before (gap G-01), so the recommendation changed.)

**Owner decision needed:** which option this example presents as its fix. **Default if no answer: B**, with the note that nothing here ships to a game.

## 9. What the charts show

- `chart.html`, **Timeline**: one row per player. Purple triangles in the first 33 s are the TL-01 spikes. Orange blocks are soft walls; hatched red blocks are hard walls (the bridge, from 24 s to the first Replant); black diamonds are Replants. Green and red bands are the windows with their verdicts.
- `chart.html`, **Wait per step**: each dot is the wait before one step, with the 45 s soft-wall line. Lean runs keep only walls, Replants and goals, so the early "waits shrink" part is not plotted (gap G-16); Appendix B has it.
- `chart.html`, **Curves**: pot price (log scale) and output with the x2 steps at 25 and 50 pots.
- `options/chart.html`: rows A, B, C (each row title names its model). In B, the diamonds are far apart and evenly spaced; in A and C they crowd together after day 8.

## 10. Hand-off, playtest, limits

- **UI**: from the first minute, show the next pot price, the greenhouse button, and the bridge with "opens after your first Replant". Before a Replant, show what it keeps and removes.
- **Analyst**: one event per purchase step, per Replant (seeds, run length) and per offline reward.
- **Engineering**: nothing is exported; an example never becomes definition tables.
- **A playtest must check**: does the player connect the jump to the purchase (TL-01)? Does the slowdown lead to the Replant or out of the game (TL-03)? Is the locked bridge exciting or annoying (TL-05)? In week 3, why do players still Replant?
- **Limits**: one strategy per run; Replants are automatic; no randomness; no measured player data. Every result depends on all 65 `EXAMPLE ASSUMPTION` inputs (listed in each chart's assumptions panel).

Files: `model.json`, `runs/*.json`, `chart.html`, `options/model-B.json`, `options/model-C.json`, `options/runs/*.json`, `options/chart.html`. Re-run commands: `../README.md`.

## Appendix A: full timeline rows

| Row | Sign to watch | Intended state | Purpose | Model check | Playtest question |
| --- | --- | --- | --- | --- | --- |
| TL-01 | buys the 2nd pot within 10 s without help | 25-50 pots, watering can | teach cause and effect | goals TL-01a (2 pots), TL-01b (`spikes` petal_rate ≥ 3) | Can the player say what the 25th pot did? |
| TL-02 | a greenhouse before 2 min | first greenhouse | open a second track before pots slow down | goal TL-02 | Does the player notice the greenhouse? |
| TL-03 | waits of 45 s or more | about 70 greenhouses | make the Replant the next step | goal TL-03 (`soft_walls` ≥ 1) | Does the player look for something new, or quit? |
| TL-04 | Replants without a prompt | 1 Replant, about 118 seeds | trade the build-up for seeds and the bridge | goal TL-04 | Does the player understand the keep list? |
| TL-05 | sees the locked bridge early, crosses it after the Replant | bridge pass, Sky Orchards | give the first Replant a visible prize | goals TL-05a (affordable and not yet Replanted), TL-05; `walls.hard` | Curious or annoyed? |
| TL-06 | the bridge opens in the first seconds of day 2 | bridge pass | reward the first return | goal TL-06 | What does the player do in the first minute back? |
| TL-07 | 10 Replants by day 7 | 10 Replants | a steady loop | goal TL-07 | Do players choose different orders? (not testable in this model) |
| TL-08 | 900 seeds between day 21 and 30 | about 900 seeds | a long goal, not finished early | goal TL-08 | Is a Replant still worth it in week 4? |
| TL-09 | 10 Replants within 14 days after a break | 10 Replants | no decay, no lost progress | goal TL-09 | Does the return screen feel like a welcome? |

## Appendix B: the pot alone (exact trace, M01)

Continuous model, no rounding, buy as soon as affordable. The last two columns are the simulator's version (1-second payouts, prices rounded up): the `one-track` run without `--lean`, re-run on sim 1.1.0 for this table (not committed; command in `../README.md`).

| Pots | Next price | Petals/s | Wait (exact) | Wait | Time since start | Sim wait | Sim time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.67 | 400/167 | 2.395 s | 2.40 s | 3 s | 3 s |
| 2 | 4.28 | 3.34 | 214/167 | 1.281 s | 3.68 s | 2 s | 5 s |
| 3 | 4.5796 | 5.01 | 11449/12525 | 0.914 s | 4.59 s | 1 s | 6 s |
| 15 | 10.3141 | 25.05 | | 0.412 s (smallest) | 10.49 s | 0 s | 13 s |
| 24 | 18.9621 | 40.08 | | 0.473 s | 14.43 s | 0 s | 17 s |
| 25 | 20.2895 | 83.50 (x2) | | 0.243 s | 14.67 s | 1 s | 18 s |
| 49 | 102.9156 | 163.66 | | 0.629 s | 24.26 s | 1 s | 28 s |
| 50 | 110.1197 | 334.00 (x2) | | 0.330 s | 24.59 s | 0 s | 28 s |
| 100 | 3243.80 | 668.00 | | 4.86 s | 108.3 s | 4 s | 112 s |
| 139 | 45396.39 | 928.52 | | 48.9 s | 868.1 s | 49 s | 873 s |
| 150 | 95552.68 | 1002.00 | | 95.4 s | 1656 s | 96 s | 1661 s |

Both the exact waits and the sim columns re-run with the commands in `../README.md`.
