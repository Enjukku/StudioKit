> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-design`. Sources: 03:DB1-DB5, DR1-DR6, DI1-DI9, DM1-DM7, DX1-DX3 (paper; Roblox definitions checked in FC-R against the docs mirror rev 7400643, 2026-10-21). Event code, dashboards and limits: `analytics` (it owns them); the analyst's own method: `analysis-design`. This file is how the progression designer reads the analyst's data. Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the problem behind a requested fix; one lever per change).

# After launch: reading progression data

## 1. Read the denominator first (03:DR1-DR6, DB3, DB5)
| Number | What it really is (FC-R) | Trap |
| --- | --- | --- |
| D1 / D7 / D30 retention | cohort by the new player's first play date; returned the next day / after 1 week / after 1 month; recent cohorts are empty, not zero (FB24a) | treating an immature cohort as 0; reading D7 as "came back any day in week one" (that exclusion is the paper's reading, not on the page: FB24b) |
| Average session time | total playtime ÷ sessions | a better tutorial can shorten sessions and raise completion; a long session can hide idling or confusion |
| First-session retention chart | share of new players still in their first session after X minutes | not a measure of fun |
| Benchmarks | similar-player games (then genre, then all), comparison games ≥ 100 DAU, updated daily; shown as 50th-90th percentile (the docs' 12.11 %-18.73 % D1 is an example); a separate overall pool from the top 1,000 games by 30-day playtime, excluding games under 30 days (FB26-FB27) | a benchmark is descriptive and survivor-selected; the pool can move without your game changing; never a target |
| Time to milestone | only meaningful with everyone eligible, the non-completers and each player's observation window | **survivor bias:** a harsher gate makes the remaining experts look faster while everyone else quits (DB5) |

Every chart you cite records: eligible population, numerator, denominator, window, acquisition source, cohort rule, build and balance revision (DR3). Active time and calendar time are separate charts. A player not back at the cutoff is unobserved, not churned (DB5).

## 2. What the instrumentation can show (03:DI1-DI9; FC-R)
- Economy: `LogEconomyEvent` (player, source or sink, currency, positive amount, ending balance, transaction type, optional SKU, custom fields). Log after the authoritative grant or purchase succeeds; purchase attempts are a separate event (DI2).
- Economy, funnel and custom events must be sent from the server in published games (stated on the three guide pages, FC-R FB29).
- Funnels: first instance of a step counts; skipped later steps complete earlier ones; filters use entry-time values; recurring funnels use `funnelSessionId` (`LogFunnelStepEvent` only; 10 recent ids per player per funnel). Optional RPG branches are not one ordered funnel; use separate paths or custom events (DI3-DI4).
- `LogProgressionEvent` exists but has no Roblox-provided chart: never promise a progression dashboard from it (DI5).
- Custom events aggregate count, distinct users, mean, sum, min, max; no percentiles or survival curves built in (DI6) → the analyst exports raw events for distributions.
- Currencies: the docs disagree (5 vs 10 resource types); plan for **5 or fewer** until a published game's dashboard shows otherwise (FC-R FB36, unverified). Up to 3 custom fields per event; charts about 24 hours behind; View Events for near-real-time checks (FB37a-FB38).
- Validate instrumentation (View Events, a known test path) before any curve change (03:DT6).

## 3. Diagnostic matrix: signals are questions, not verdicts (03:DM1-DM7, O)
Thresholds come from the game's own timeline and its uncertainty, never from a universal benchmark.
| Suspicion | Numbers and denominator | Rule out first | Smallest next test |
| --- | --- | --- | --- |
| First reward too late | entry → first meaningful reward, active-time distribution over all entrants, unfinished players kept (censored) | loading failures, device performance, acquisition mismatch, missing events | change reward access or onboarding, not the whole XP curve |
| A level is a grind wall | eligible → next unlock conversion; earned currency per active minute; net remaining price; failures | optional detours, interrupted sessions, returning veterans, trading gifts | test cost and earning activity separately; keep the intended skill test |
| Content runs out too fast | time to the last meaningful unlock, then return rate and activity mix | experts self-selecting, exploit farming, little content yet | add breadth or later goals before slowing new players |
| Apparent inflation | wallet percentiles by tenure; executed fixed-basket price index; new currency per person-hour; sink uptake | new-player inflow, transfers, deliberate scaling, rare-item shock | fix the dominant unwanted source or add a wanted sink, not a blanket tax |
| Premium creates a wall | completion and time-to-unlock by spender cohort defined before treatment; non-payer return | payers were more engaged before paying; regional price and tenure mix | randomized offer or interface test plus fairness review; never "payment caused retention" |
| One reward route dominates | reward per hour and selection share per route and stage, plus failure and enjoyment feedback | the best route may also be the most fun; class or device bias | improve alternatives; do not punish competence |
| Retention fell after an update | mature first-play cohorts by device, region, acquisition, version | weekends, holidays, ad bursts, crashes, changed eligibility | verify operations first, then isolate the progression change |

A request that names its own fix ("lower the price", "more rewards", "make it faster") is a pointer to a problem: restate the problem first ("players cannot see the next goal"), then choose the fix from the explanations below; after the change, re-check the problem, not only that the requested number moved. Before proposing a change, list the competing explanations: unaffordable cost, confusing objective, uninteresting activity, combat failure, too little session time left (DB4). Change the smallest justified lever; compare an identified cohort and revision; inspect distributions and individual paths. Separate resource bottlenecks: currency but no material; material but no unlock; power but unclear objective (DB2).

## 4. Experiments (03:DX1-DX3; FC-R FB39-FB41)
- Roblox in-game Experiments test config values: planned 14-60 days, up to 2 variants + control, one active experiment per config key (locked while it runs).
- Code calls `ConfigService:GetConfigForPlayerAsync` then `GetValue`; `GetConfigAsync` does not apply experiments; the first `GetValue` enrolls the player, so call it where the changed feature is met. Targeting is re-evaluated per session: persist the value for multi-session progression.
- Under 1,000 DAU "might struggle" (a warning, not a bar); targeting shrinks the sample; read the minimum detectable effect and sample-ratio-mismatch banner; early-harm results are not early winners.
- Before proposing an experiment, size it: the minimum detectable effect Roblox shows at setup is the authority; for a planning estimate use a standard two-proportion sample-size calculation (state α, power, baseline rate, and that it is the studio's estimate, not Roblox's method) against the mature new players per arm the game gets in the planned duration. A small game often cannot detect the change it cares about: say so and recommend playtests and longer observation instead (J011-T09 H4: about 600 DAU could not detect +3 % relative D7).
- Predeclare the win criterion and guardrails (e.g. more eligible players reach the next interesting decision without hurting later return, competitive fairness or non-payer progress); the effect size comes from the owner's goals and the feasible sample. Non-significance is not equivalence. Small games: instrumented playtests, player explanations and longer observation instead of a confident fake A/B result (DX3).

## 5. The proposal you return (O)
Observation (with denominator and revision) → the problem behind any requested fix → competing explanations → the one you test first and why → the smallest lever → re-simulated outcome under the same named policies (`progression-craft`) → what the analyst must measure to confirm → owner decision with a default.
