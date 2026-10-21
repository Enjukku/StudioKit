> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-design`. Sources: `knowledge/reference/progression/01-cases-shapes-curves.md` (01:), `02-incremental-rpg-rewards.md` (02:), `03-economy-tools-data-process.md` (03:), fact-check FC-M. Tags V / E / O as in SKILL.md.

# Feeling timeline, vocabulary, shape placement, genre patterns

## 1. The feeling timeline (the progression designer's main design document)

Written with the game designer, approved by the owner, then turned into goals the simulator checks (`progression-craft`). The five checkpoints come from the owner's brief; the candidate feelings are the paper's proposals for the owner, not research findings (01:FT1-FT5, S5, O). Add checkpoints where the game needs them (first boss, first prestige, first trade).

| Checkpoint | Clock | Candidate feeling (paper, O) | Design question | Evidence to gather |
| --- | --- | --- | --- | --- |
| First minute | active | "I understand what my action changed." | Is the first meaningful action readable and consequential? | action done, feedback noticed, player can explain it |
| First session | active | "I made a choice and can name my next goal." | Did progress show agency, not only a bigger counter? | route chosen, first upgrade/unlock, next goal recalled, time distribution |
| First day | calendar | "Returning gives me a new possibility." | What changes on return, without punishing absence? | state on return, new choices, how offline reward reads |
| First week | calendar | "My build or approach expresses a preference." | Is there specialization, mastery or a new problem? | route diversity, viable alternatives, bottleneck traces |
| First month | calendar | "I still have goals, or a satisfying completion." | Depth, optional reset, social purpose or a clean ending? | long paths, completion quality, repetition complaints, reset uptake |

**Row format** (one row per target; every field filled or marked missing):

| Field | Holds |
| --- | --- |
| id | `TL-<nn>`, stable; the simulator goal uses the same id |
| checkpoint | first minute · first session · first day · first week · first month · named moment |
| clock | active play (seconds of play) or calendar age (days since first play); calendar needs a session model (D-14) |
| feeling | the owner's words, or `PROPOSAL: <wording>` |
| observable sign | what a tester or the data would show if the feeling is there ("player names the next upgrade without help") |
| intended state | what the player owns, has unlocked or can do at that point |
| shape | fast start · slowdown · soft wall · hard wall · spike · plateau · reset · catch-up · none |
| purpose | why this shape is here (what the player learns, chooses or optimizes) |
| window | target time range with its clock: owner decision id, or `PROPOSAL`, or `EXAMPLE ASSUMPTION` |
| model check | the goal predicate and metric the simulator reports (`progression-craft`) |
| player check | playtest question or telemetry signal that tests the feeling |

Rules: a "day/week/month" target is defined as calendar age or active play before it gets a number (01:S5); a window is never presented as a forecast until real reachable state, play time and measured distributions are entered (01:S4); the owner may move or delete any checkpoint.

## 2. Vocabulary (operational definitions, the paper's, 01:VC1-VC9, O)
| Term | Means | Tell it by |
| --- | --- | --- |
| Fast start | a meaningful next state reachable with little prior investment on the stated starting path | short time to the first benefit (§3 of SKILL), not "every cost is small" |
| Slowdown | required effort rises relative to the player's capacity | wait or attempts per step rising, income-to-cost ratio falling |
| Soft wall | reachable by the current earning process, but expensive relative to the intended route | affordability: time to afford ≫ recent steps |
| Hard wall | needs a separate condition (key, content unlock, prerequisite, skill test) that repeating the current action cannot give | an unlock predicate unmet while affordability is met |
| Spike | a jump in useful capability: one hit fewer on a known enemy, a new route possible, a multiplier unlocked | a discrete change in a reference metric on unchanged content |
| Plateau | an important result held roughly constant while other things change | flat reference metric; needs a learning goal and exit (01:PL1) |
| Reset | removes some state on purpose and keeps other state | list removed / kept / merged / granted (01:VC9) |
| Catch-up | lowers the repeated cost of reaching an earned capability or an intended entry point | cost of the second time vs the first |

Kit addition (O): a **skill gate** is a hard wall that the player passes by learning, not by earning. Measure attempts, deaths and time per attempt, never currency; its fix is teaching, assists or an optional route, not a cheaper price.

## 3. Placing changes
1. **Place by purpose before time.** The cases are alternatives, not one schedule: Overwatch flattens a cosmetic track after an introduction; Factorio's optional research grows dearer forever; Hearthstone fixed spacing between useful rewards; WoW removed repeated character work. None says a simulator should prestige on day one or an RPG should unlock its whole kit in session one (01:S2, O).
2. **Spikes:** compare before and after against the same encounter or earning chance; when both cost and income rise, the ratio decides speed (01:S3, O). A smooth damage curve does not give smooth fight length: hit counts move in steps (02:RP6, V derivation).
3. **Walls:** say soft or hard; a soft wall's exit is income or a cheaper route, a hard wall's exit is the prerequisite (01:ST2, O). An exponential price as the gate to ordinary content is the riskiest soft wall; prefer it in voluntary sinks (01:K4.O, Q2).
4. **Plateaus:** name what the player learns, chooses or optimizes meanwhile, and the exit. If the only reason is length, show the owner alternatives: varied goals, a different content gate, an optional challenge, a shorter progression (01:PL1, O).
5. **Resets and catch-up:** write removed, kept, merged and granted state and what the next run offers before any formula (01:R08, VC9, O). Decide how the reset requirement grows with the reset count: a fixed requirement makes every later run shorter as kept power grows, and the reward per reset collapses (J011-T08 example: 119 → 8 seeds per reset by day 22). Decide whether offline income counts toward the reset basis; if it does, returns can trigger resets by themselves.
6. **Early waits can fall even with exponential prices** when output grows faster at first; in the paper's idle example (1.07 price growth, linear output) waits fall until about 15 owned and rise after, before the next milestone multiplier (02:L9, L13, V arithmetic). Check where the turn lands; do not assume it.

## 4. Genre patterns (O unless marked; each is a starting hypothesis, not a template)
| Genre | What progresses | Usual math (craft) | Spikes and walls | Watch for |
| --- | --- | --- | --- | --- |
| Incremental, idle, Roblox simulator (act → currency → upgrades → rebirth) | owned producers, multipliers, unlocked tiers, prestige currency | exponential price per producer, linear output per owned, milestone multipliers at counts (M01: ×2 at 25 and 50, E), prestige by fractional power (C01, V), offline policy | spike: milestone multiplier or new tier, measured as income/s or time to next tier; soft wall: waits rising before the next milestone; hard wall: area or tier unlock | repeated runs pushing out discovery (01:K1.O); a reset that only repeats familiar labor (03:OQ3); numbers past 2^53 (craft §precision) |
| Tycoon | finite build journey (buy the next piece), then surplus | per-piece prices and income per piece; optional infinite sink after the finite journey | spike: a piece that changes income or opens an area; wall: next floor or area | exponentially priced basics as the gate to ordinary content (01:K4.O) |
| RPG, action, adventure | level, stats, gear, abilities, zones, story gates | per-level XP vs cumulative XP, XP rate per activity, hits-to-kill and TTK/TTD per build and enemy, gear stacking | spike: one hit fewer on a named reference enemy, a new ability; walls: zone level, boss (mechanics apart from stats) | enemy scaling cancelling player power (01:B1); continuous DPS hiding breakpoints (02:RP5-RP7); M03's area → small gains → boss → power pattern is one option, not universal (02:RP10, E) |
| Obby, platformer, parkour | stages reached, movement verbs, assists, cosmetics | time per stage, attempts and fail rate per stage, checkpoints | spike: a new movement verb that opens a route (Mario Wonder badges, 01:K12); skill gates | mandatory movement upgrades that make old obstacles trivial; an assist and an optional constraint can coexist (01:K12.O) |
| Competitive, match-based | in-match level/economy; account power; mastery identity | match economy as choices (TFT level vs build, 01:K10); caps by league (01:K8) | spike: a level that changes feasible decisions; wall: league caps | account power deciding matches; dedication tracks pulling players off team goals (01:K9.O) |
| Collection, pets, gacha | owned set, rarity, duplicates, pity | drop odds, expected attempts and quantiles, pity counters (craft) | spike: a rare unlock; wall: an essential item behind luck (avoid, D-15) | paid random rules every time (`platform-policy`); duplicates with no use |
| Cosmetic and dedication tracks | recognition, borders, titles | fast early levels, then flat cost per level (Overwatch 2025 plan: flattens at 20, milestone at 60, 01:K11) | spike: visible milestone rewards; no combat power | veteran age becoming a combat advantage; empty levels (01:B4) |

Mixed games combine rows; keep each track's job separate (D-11).
