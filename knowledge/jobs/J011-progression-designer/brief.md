---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent progression-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J011 intent brief — progression-designer agent

<intent>
The studio needs one agent that makes progression feel good on purpose, and can prove it before players see it. Today the game designer decides what the player should feel and when ("the first minute shows what my action changed", "the first boss feels like a wall, then the new weapon makes the old area easy"), but nobody turns that into exact numbers, checks that the numbers really produce that timeline, and hands engineering the tables the game reads.

The progression designer starts from the experience, not from a formula. With the game designer it writes a feeling timeline from the first minute to the first month: where progress is quick, where it slows, where a soft wall (reachable but expensive) or a hard wall (needs a key, unlock or skill) lands, where a power spike comes, and what each milestone lets the player do that they could not do before. Then it picks the simplest curves that make that happen and builds them as data tables.

It proves the result with arithmetic and simulation: exact traces of purchases, levels and resets; named model players (efficient, saver, explorer, struggling, returning after a break) played through the tables; charts the owner can look at; and a pass or fail for every target on the timeline. A simulated path is one strategy, not the population, and a passed calculation is not proof of fun: playtests and later the analyst's data decide that. After launch it reads where players quit, time per level and spending, and proposes the smallest curve change with the evidence.

It works for any genre: incremental and simulator games (production, costs, multipliers, prestige), RPGs and action games (player power against enemy health and damage, hit breakpoints, time-to-kill, gear, bosses), tycoons, obbies and more. It keeps paid random items, ads and younger players inside Roblox's current rules and never designs friction to sell an escape.

The owner's paper is strong evidence but not gospel: formulas, numbers and Roblox rules are checked, and anything that cannot be backed up is dropped. This agent replaces economy-designer in the roster.
</intent>

<spec>
id: J011
from: owner
to: lead
skills: [orchestration, ste-writing, game-design, platform-policy, analytics, data-saving, architecture]
refs:
  - C:\Users\Firew\Downloads\Progression_Designer_Research_2026.txt   # take: 15 rules; 12 cases as alternatives (prestige accounting bases, optional infinite sink, character vs account progress, reward spacing, staged caps, levels as strategic thresholds, movement unlocks); vocabulary (fast start, slowdown, soft wall, hard wall, spike, plateau, reset, catch-up); feeling timeline template; curve library and cumulative vs per-level; bulk buy, waits, payback, prestige, offline contract; hit breakpoints, TTK, effective health, stacking; reward clocks and ethics; ledger identity and affordability; Roblox rules; simulator spec, precision and rounding; diagnostic matrix and denominators; hand-off contract; process; checklist; don'ts. avoid: worked-example numbers as tuning for any game, any universal pacing number, the paper's text verbatim
  - .agents/skills/game-design/references/systems-economy.md   # take: resource roles, 9 scenario groups, reward schedule rule, systems check; avoid: duplicating it (game-design judges, progression-design does the math)
  - .agents/skills/platform-policy/, .agents/skills/analytics/, .agents/skills/data-saving/   # take: the current Roblox rules, event names and limits, save migration rules; avoid: restating them in full (point to them)
  - DestructionSimulator knowledge/design/{economy, gear, pets, brick-strength-stages, telemetry, decisions, tried-and-failed}.md (read-only)   # take: universal lessons and owner economy rulings as cases; avoid: game names, stages, numbers
fixed:
  role_name: progression-designer                     # owner 2026-10-21
  replaces: economy-designer                          # owner 2026-10-21
  model: opus                                         # owner 2026-10-21
  effort: high                                        # owner 2026-10-21
  tools_model: opus, effort medium or higher          # owner 2026-10-21
  tools: curve library, progression simulator over the game's data tables with a timeline report (time to each goal, walls, power spikes), chart output the owner can look at; Python, standard library where possible, with tests   # owner 2026-10-21
  worked_examples: one incremental game, one RPG, run through the simulator, with charts   # owner 2026-10-21
  timeline: first minute to first month                # owner 2026-10-21
  genres: incremental/simulator, RPG/action, tycoon, obby and more   # owner 2026-10-21
  hand_offs: game designer (goals in, curves out), engineering (data tables), UI (how progress is shown), analyst and live-ops designer (planned); rules/messages.md format   # owner 2026-10-21
  after_launch: reads the analyst's data (quit points, time per level, spending) and proposes curve changes   # owner 2026-10-21
  policy: Roblox rules on paid random items and younger players   # owner 2026-10-21
open: [book structure inside the two skills, tool structure and data-table schema, chart design, policy names, hand-off wording, the worked examples' game concepts]
not_in_scope: [game code, approving curves or targets, real analytics pulls, the analyst and live-ops roles, tuning a real game]
rules:
  - Paraphrase sources; never copy paper text; the paper stays outside git. Short quotes ≤ 15 words, attributed.
  - Evidence tags kept (VERIFIED / EXPERIENCE / OPINION). A number without a scoped source is PROPOSAL, EXAMPLE ASSUMPTION or a per-project owner decision, never a rule.
  - No invented pacing targets: seconds per reward, session length, time to first prestige, D1/D7/D30 values are owner decisions or labelled assumptions.
  - Feelings are hypotheses until a person plays the build; a model pass is never reported as fun.
  - Roblox policy facts come from `platform-policy` or a dated check against the docs mirror or a live page; no conflict with `platform-policy`.
  - Nothing specific to DestructionSimulator in kit files.
  - Tools: Python standard library where possible; deterministic; offline tests; every exported table carries a revision.
  - Label each check gate-verified, MCP-verified, owner-confirmed or not verified.
  - Skills ≤ 500 lines, kit template, "Read this file when" table, project-overlay line.
deliver: knowledge/reference/progression/*, .agents/skills/progression-design/*, .agents/skills/progression-craft/* (evals/briefs.md included), .agents/roles/progression-designer.md, tools/progression/*, tools/tests/test_progression_*.py, examples under tools/progression/examples/, knowledge/jobs/J011-progression-designer/handoffs.md
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 worked examples with charts; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `progression-design` | design | What makes progression worth pursuing (six kinds of benefit, learning vs unlocking, grind defined operationally); the vocabulary (fast start, slowdown, soft and hard wall, spike, plateau, reset, catch-up); the feeling timeline (first minute → first month) and how to write targets as testable hypotheses; the 12 cases as alternatives per design question; genre patterns (incremental, simulator, tycoon, RPG/action, obby, competitive); reward clocks and ethics; premium fairness and Roblox rules (pointing to `platform-policy`); after launch: reading data with the right denominator; the don'ts | progression designer, game designer, UI, analyst, live-ops, lead |
| `progression-craft` | craft | The procedure: experience → resource and unlock graph → curve choice → exact traces → simulation with named policies → failure-mode review → options for the owner → data tables and fixtures → after-launch tuning. Curve library and formulas with units and index origins; incremental math (bulk, waits, payback, prestige accounting, offline contract); RPG math (breakpoints, TTK/TTD, effective health, stacking, bands); probability (expected spend vs quantile, pity); ledger and affordability; precision and rounding in Luau; the tools and how to read their output; data-table contract; hand-off briefs; review checklist; self-check | progression designer |

## Proposed tools (`tools/progression/`, standard library)
| Tool | Does | Never does |
| --- | --- | --- |
| `curves.py` | The paper's curve library (affine, polynomial, triangular, exponential, logarithmic, fractional power, saturating, piecewise, milestone step); per-level ↔ cumulative; bulk-buy closed form and max affordable (checked by the inequality); wait and payback; prestige formulas with accounting bases; hit breakpoints, TTK both conventions, effective health, additive vs multiplicative stacking; constant-p quantile; exact `Fraction` mode | pick coefficients |
| `sim.py` | Plays a named policy through JSON data tables (currencies, producers, upgrades, unlocks, milestones, enemies, gear, prestige, session model) with a declared event order; reports a timeline (active and calendar time to each goal), soft walls, hard walls, power spikes, blocked paths, ledger reconciliation; seeded Monte Carlo only where the data has randomness | claim a population forecast |
| `chart.py` | Self-contained HTML with inline SVG from a sim report: curves, timeline with goals, walls and spikes marked, policy comparison, assumptions panel | need any package or network |

## Known risks (to resolve in step 2)
1. The paper deliberately refuses to invent earning rates, so its RPG timeline is symbolic. The worked examples need rates, session lengths and combat stats to produce a minute-to-month timeline: each one is labelled `EXAMPLE ASSUMPTION` in the data (digest item 4).
2. Recent Roblox facts (Kids/Select 2026-06-16, ad standards 2026-10-09, analytics limits with a documented 5-vs-10 disagreement, Experiments) → docs mirror + live check; `platform-policy` wins on conflict and gets a follow-up note if it is stale.
3. Overlap: `game-design` already holds an economy section and a systems check. Split: game-design judges whether a system is fun and fair; progression-design owns the math, timelines, simulation and tables. Pointer lines only, no copies.
4. Precision: incremental games pass 2^53 fast. The tools must flag precision loss at the planned maximum balance, not silently print big numbers.

## Hidden test set (evals)
Held out of the skills: the Hearthstone reward-track correction (generous total, dead stretches), the Clash of Clans bundle rebalance (one reward cut amid several changes), and the survivor-bias trap (a harsher gate makes completers look faster). The eval gives the agent a symptom and data, and asks for the diagnosis, the smallest curve change and the briefs. A separate grader scores it.

## First real task (G2), proposed
The new agent builds the two worked examples as if for a real game: a short design brief for each (a small incremental/simulator and a small RPG), the feeling timeline, the data tables, simulator runs for 3+ named policies, charts, and the pass/fail check of every target. Shown to the owner with the charts. When the owner picks a J003 concept, the agent's first real game job follows.
