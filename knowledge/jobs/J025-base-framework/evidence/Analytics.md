---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B1
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Analytics: Q1-Q9 evidence

Code: `roblox-game-framework/src/Analytics/init.luau`. Specs: `Analytics.spec.luau` (Lune) and `Analytics.engine.spec.luau` (Jest, written, NOT RUN). Contract: `contracts/Analytics.md`, as of 2026-10-24.

**Red run before code** (`lune run tools/spec/run.luau src/Analytics`):
```
FAIL src/Analytics/Analytics.spec.luau: could not load: require "../Analytics" from src/Analytics/Analytics.spec.luau: no module script there in sourcemap.json
specs: 1 files, 0 passed, 1 failed
```
Green: `specs: 1 files, 11 passed, 0 failed`.

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | pass | the 5 contract functions. There are 2 spec-only hooks: `_reset(fakes?)` swaps the engine for fakes and clears all state, and `_debugCounts()` returns `{dropped, errors}` (the README leak-hook pattern) |
| Q2 | pass (gate-verified for my files) | `--!strict`; luau-lsp gives 0 errors on `init`, the spec and the engine spec. The only exported type is `Def` (no `any`). The `:: any` casts are only in the spec, on fakes |
| Q3 | pass | row table below; 11 of 11 planted faults turned a spec red |
| Q4 | pass | engine throws → An-T5 (no error reaches the caller, 1 sampled warn, errors counted); over the limit → An-T4 (dropped and counted); unknown name → An-T1; NaN, inf or negative amount → An-T3; player left → An-T5 "a player who left is skipped"; call before `start` → nothing is sent, no error |
| Q5 | pass (by construction) | no connections, no per-player tables. State is 60 buckets plus name sets. The warn times are keyed by declared or unknown name, which come from game code, not players |
| Q6 | pass in Lune; engine not verified | Lune 0.11.1, fake engine, 3 runs: `custom` 0.37-0.38 µs, `economy` 0.80-0.82 µs, 0 KB `gcinfo` growth over 50k calls (budget ≤ 50 µs, 0 allocations). Engine calls go through `pcall(service.Method, service, ...)`, so no closure is made per call. `#Players:GetPlayers()` (it allocates a list) runs at most once per clock second, when the window moves. The real engine call cost is not verified (An-T7 lane) |
| Q7 | n/a | no client input (contract). Names are declared constants; `stepName` and `sku` come from game data (An6, a review row) |
| Q8 | pass | `_api-reference/classes/AnalyticsService.yaml:405` LogCustomEvent, `:448` LogEconomyEvent (`:488` transactionType is a string, so `.Name` of the enum is passed), `:528` LogFunnelStepEvent (`:567` steps 1-100), `:658` LogOnboardingFunnelStepEvent. Limits: `production/analytics/event-types.md:78` (120 + 20 × CCU per minute), `custom-events.md:17` (100), `economy-events.md:121` (5), `funnel-events.md:17` (10). The player count uses `GetPlayers`, because `Players.NumPlayers` is deprecated (`Players.yaml:220-235`) |
| Q9 | pass | the contract Usage block runs as "Q9 the contract's usage example runs" (fake engine) |

## Test row → spec (Analytics.spec.luau unless named)
| Row | Spec name |
| --- | --- |
| An-T1 | "An-T1 unknown currency, funnel and event are never sent; one warn per name for 10 calls" (10 s later one more warn) |
| An-T2 | "An-T2 start errors on lists over the dashboard limits or with duplicates" (5/10/100 allowed; a second `start` errors) |
| An-T3 | "An-T3 amounts go through Amount.whole; 0 is not sent; steps clamp to 1-100" |
| An-T4 | "An-T4 1 player: 200 calls in one minute send 126, drop and count 74; the next minute sends again"; "An-T4 the window rolls..."; "An-T4 the budget grows with players: 10 players ... = 288" |
| An-T5 | "An-T5 an engine error never reaches the caller; one sampled warn"; "An-T5 a player who left is skipped" |
| An-T6 | "An-T6 start on the client errors" |
| An-T7 | `Analytics.engine.spec.luau` "An-T7 one call of each kind raises no engine error". NOT RUN: it needs a play-test Server DM with one joined client (an Edit DM has no Player) |
| An6 | review row (no spec): no parameter is user-entered text |

## Planted faults (script: scratchpad `b1-helpers/plant_b1.py`)
Unknown names sent → An-T1 · no request budget → An-T4 · no 10 % margin → An-T4 · zero amount sent → An-T3 · raw ending balance → An-T3 · left player not skipped → An-T5 · client start allowed → An-T6 · off-by-one list limit → An-T2 · NaN step passed → An-T3 · window never rolls → An-T4 window · error warn not sampled → An-T5. Caught 11/11; no false alarms on the correct build.

## Decisions inside the contract
- The budget counts only calls that went to the engine (a call that failed inside `pcall` still counts; unknown names and zeros do not). Budget = `(120 + 20 × players) × 90 // 100`, recomputed once per second.
- Sampled warns: one line per unknown name per 10 s, one per kind (budget, engine error) per 10 s. A drop that lasts 21 s gives 3 lines (An-T4 asserts this).
- `start` errors on a second call. A clock reading that goes back or is NaN does not move the window.
- The engine is looked up in `start`, not at require time, so the module loads in Lune.

## Repair round 1 (review code-g1-r1 F2; feature-builder · claude-opus-5-5 · medium · 2026-10-24)
- Fix (`src/Analytics/init.luau`, sha256 e53bdc0846dc313b): first line of `custom`: `if value ~= nil and value - value ~= 0 then return end` (NaN and ±inf not sent; no budget used; negative and fractional values still sent). No API change.
- Spec `An-T3 (review F2) custom values NaN, inf, -inf are not sent; -2.5 is sent as -2.5`: red before at :149 "expected 0, got 3"; green after (29 passed with Screens, 0 failed).
