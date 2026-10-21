---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J011 step 5
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J011 hidden evals (grader only)

Change from the brief (lead, 2026-10-21): the brief planned the Hearthstone track, the Clash of Clans bundle and survivor bias as hidden cases, but the paper teaches all three, so the skills now contain them (`cases.md`, `rewards-ethics.md` §5, `live-data.md` §1). These replacement cases are new symptoms that test whether the agent APPLIES the books to situations they do not describe. The agent gets only the "symptom brief"; the grader gets this file.

Run: progression-designer (Opus, high), fresh context, one brief at a time, writes to `output/progression/j011-t09/H<n>/`. Grader: Sonnet, high, scores each must-pass item pass / partial / fail from the files with a one-line reason.

## H1 — "More rewards, still boring"
Symptom brief: "Season 2's reward track pays 3× more coins in total than season 1, but players quit more between levels 14 and 26. Levels 14-26 give only coins. Coins buy nothing new until the level-27 shop unlocks. Make the track more rewarding."
| ID | Must pass |
| --- | --- |
| H1-1 | Diagnoses spacing of USABLE rewards (13 levels without a functional change), not the total; says more coins will not fix it |
| H1-2 | Uses the reward-ledger idea: what each level changes, its next use; separates feedback / completion / upgrade / content clocks |
| H1-3 | Asks for or plans the data with the right denominator (eligible players at 14, non-completers, active vs calendar) before claiming the quit cause |
| H1-4 | Proposes the smallest change (e.g. a usable unlock or sink inside 14-26, or move the shop earlier), re-simulated with gap lengths reported |
| H1-5 | Owner decision with options and a default; nothing tuned without labels |

## H2 — "The spins are free"
Symptom brief: "Daily spins cost 50 gems. Players earn gems by playing and can also buy gem packs for Robux. Gems from both go into one wallet. The owner says the spin is free because you can earn gems. Spin odds are not shown. Set the spin rewards."
| ID | Must pass |
| --- | --- |
| H2-1 | Recognizes Robux-buyable currency makes the spin a paid random item under Roblox rules; mixed wallet → stricter reading (treated as paid, marked as the studio's reading) |
| H2-2 | Requires odds before spending, totalling 100 % (rounding rule + disclaimer), every outcome of some benefit, `PolicyService` check per player with a working route for restricted players |
| H2-3 | Suggests keeping origin metadata or splitting earned vs bought currency as an engineering/owner decision; does not decide policy alone |
| H2-4 | Computes expected spins and the unlucky tail for any reward the progression needs; flags essential luck |
| H2-5 | Escalates to the owner (needs-decision) rather than "setting the rewards" as asked |

## H3 — "Upgrades stopped working"
Symptom brief: "Late-game players report that buying the cheapest upgrade (cost 3 coins) does not reduce their balance, and their income display sometimes jumps by a few hundred instead of smoothly. Balances are around 4 × 10^17 coins. Fix the curve."
| ID | Must pass |
| --- | --- |
| H3-1 | Identifies float precision (Luau numbers are doubles; integers exact only to 2^53 ≈ 9.0 × 10^15; at 4 × 10^17 the spacing between representable values is 64) rather than a curve error |
| H3-2 | Says the fix is a design + engineering decision: smallest meaningful unit, maximum balance, representation (rescale units, or a big-number type), not a cheaper upgrade |
| H3-3 | Uses the simulator precision flag (declares smallest_unit) to show where the game crosses 2^53 on the timeline |
| H3-4 | Brief to engineering (architect / data-saving for saved balances and migration) in `rules/messages.md` form; existing saves considered |

## H4 — "Ship variant B"
Symptom brief: "We ran a Roblox experiment on the first-zone XP curve for 9 days: control vs variant B (faster). The game has about 600 DAU. B shows +3 % D7, not statistically significant. The designer wants to ship B to everyone."
| ID | Must pass |
| --- | --- |
| H4-1 | Notes the planned duration minimum (14 days) was not met and D7 for late cohorts is immature |
| H4-2 | Notes the under-1,000-DAU warning, the minimum detectable effect, and that non-significance is neither a win nor equivalence |
| H4-3 | Asks for guardrails (later retention, non-payer progress, the next decision reached) and competing explanations |
| H4-4 | Recommends combining with instrumented playtests / longer observation; re-simulates B's timeline to show what changes for the player; owner decides with a default |

## H5 — first-game taste case (04:O01-O03; owner rulings D-174 2026-10-12, D-075 2026-10-02, D-018)
Symptom brief: "Each area pays a flat multiplier: area 1 ×1, area 2 ×2, area 3 ×3, for the same kinds of objects. Players with the best tool go back to area 1 because it clears fastest and pays almost as well per minute. Fix the pay."
Owner's real answer (game-neutral): the same content is tougher in each later area; pay follows that toughness through a smooth curve picked for fun (numbers need not be round); harder content pays more; farming an early area with top gear pays little while earlier gear stays usable; a rare variant keeps its own multiplier.
| ID | Must pass |
| --- | --- |
| H5-1 | Diagnoses reward per active minute by area × tool (not the multiplier alone): clear speed with top gear makes area 1 dominant |
| H5-2 | Proposes pay tied to the content's toughness / clear effort through a declared curve, not another flat per-area step; leaves the curve shape and values as PROPOSAL for the owner |
| H5-3 | Checks with the simulator or curves that early-area farming with top gear pays less per minute than the current area, for a named policy, while earlier gear remains usable in its own area |
| H5-4 | Notes any rare or special variant needs its own multiplier so it does not scale twice; re-derives dependent prices (gear, capacity) |
| H5-5 | Owner decision with options and a default |
