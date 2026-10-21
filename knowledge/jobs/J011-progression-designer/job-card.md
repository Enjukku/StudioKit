---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent progression-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J011 — Build the progression-designer agent

| Field | Value |
| --- | --- |
| Job id | J011-progression-designer (J006 stays reserved for the animator) |
| Size | L (new role that replaces economy-designer, 2 skill books, a 1,310-line paper with about 60 dated sources to extract and fact-check, 3 tools with tests, 2 worked examples with charts, a real test) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J011-D5). Steps 2-5 done 2026-10-21: 4 notes + 2 fact-checks in `knowledge/reference/progression/`; tools `tools/progression/` (curves, sim, chart 1.1.0; 91 tests); skills progression-design, progression-craft; role progression-designer (replaces economy-designer); evals + hidden evals; hand-offs. Step 6 done: worked examples (T08, refreshed T12 on tools 1.1.0), hidden evals (T09), grader (T10: examples 8/8, hidden 14 pass / 8 partial / 1 fail), tool fixes (T11). G2 sent to owner 2026-10-21 |
| Depends on | `game-design` (systems-economy reference), `platform-policy`, `analytics`, `data-saving` skills (exist); J003 game-designer (G2 sent) for the real G2 task |

## Owner's words (2026-10-21, excerpts)
- "It understands what fun progression is, and turns it into exact math with the game designer: where early progress feels quick, where it slows down, where a soft wall or slowing point lands, and where a power spike comes, on a timeline from the first minute to the first month."
- "It is universal: incremental and simulator games (production, costs, multipliers, prestige), RPGs and action games (player power vs enemy HP and damage, time-to-kill, gear scaling, boss tuning), tycoons, obbies and more."
- "It builds the numbers as data tables the game reads, and hands them to engineering in the brief format (rules/messages.md)."
- "It proves a progression before players see it: simulations of player paths, charts of the curves, and a check of every target feeling on the timeline."
- "After launch, it reads the analyst's data (where players quit, time per level, spending) and proposes curve changes."
- "It follows Roblox's rules on paid random items and for younger players."
- "Tools in tools/ (Python, standard library where possible) with tests: a curve library (the formulas from the paper), a progression simulator that plays a model player through the game's data tables and reports the timeline (time to each goal, where walls and power spikes land), and a chart output I can look at."
- "A worked example for each: one incremental game and one RPG, run through the simulator, with the charts."
- "This agent replaces economy-designer in the roster."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially formulas, numbers and Roblox monetization rules, and drop what you cannot back up."
- "Model: Opus, high effort. Tools and scripts are built on Opus at medium effort or higher."

## Goal
One `progression-designer` agent that turns the owner's intended player experience (agreed with the game designer) into exact, inspectable math: a feeling timeline from the first minute to the first month, the curves and data tables that produce it, and proof before players see it (deterministic traces, named player-path simulations, charts, a pass/fail check of every target on the timeline). It hands engineering versioned data tables with fixtures, tells UI what progress must be shown, and after launch reads the analyst's data and proposes the smallest curve change. It keeps paid random items and younger players inside Roblox's current rules, and never turns a passed calculation into a claim that the game is fun.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Progression_Designer_Research_2026.txt` (outside git) | 15 rules; 12 versioned game cases (AdVenture Capitalist, Cookie Clicker, Realm Grinder prestige formulas; Factorio infinite research; Diablo IV; WoW Warbands; Hearthstone reward track; Clash Royale caps; LoL mastery; TFT levels; Overwatch 2; Mario Wonder); shapes and the feeling timeline (first minute → first month); curve library (9 curves, cumulative vs per-level); incremental math (bulk buy, wait time, payback, prestige accounting, offline policy) with an exact worked model; RPG math (XP tables, hit breakpoints, TTK, effective health, stacking) with a symbolic-time worked model; reward timing and ethics (H01-H12 studies); economy ledger and Roblox rules (paid random items, PolicyService, Kids/Select, ads, regional pricing); simulator spec, precision and rounding; analytics diagnosis (retention denominators, LogEconomyEvent, funnels, Experiments); hand-off contract; 10-step process; 15-row review checklist; don'ts; source register (C01-C11, M01-M06, H01-H12, R01-R17, W01-W08) | 1,310 lines, 115 KB | high: VERIFIED / EXPERIENCE / OPINION tag on every claim, dated sources; the paper itself refuses to invent earning rates or pacing targets. Sources dated 2026-07 to 2026-10 (R08 Kids/Select 2026-06-16, R09 ad standards 2026-10-09) are near or after the model cutoff → live check |
| DestructionSimulator `knowledge/design/economy.md`, `gear.md`, `pets.md`, `brick-strength-stages.md`, `telemetry.md`, economy rows of `decisions.md`, `tried-and-failed.md` (read-only; digest item 5) | First-game economy, gear and stage-strength progression, telemetry plan, owner economy rulings | to measure | medium-high: owner practice; game names, stages and numbers → drop, keep the universal lesson |
| Kit: `game-design` (`references/systems-economy.md`, checked 2026-10-20), `platform-policy`, `analytics`, `data-saving` | What the studio already says about economies, monetization rules, analytics events and saved data | — | owner-approved |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/progression/` + fact-check tables (game-case numbers and formulas, studies, Roblox rules against the local docs mirror and live pages) | Writing game code (engineering reads the tables) |
| Skills `progression-design` (design) and `progression-craft` (craft), each with evals | Approving any curve, price or target feeling (owner only) |
| Tools: `tools/progression/curves.py` (curve library), `sim.py` (simulator over data tables, timeline report), `chart.py` (HTML/SVG charts, standard library) + offline tests reproducing the paper's exact arithmetic | Real analytics pulls (the analyst, planned) |
| Two worked examples (incremental, RPG): data tables, simulator runs, timeline reports, charts | Tuning a real game's economy (that is the agent's first job after G3) |
| Role file `progression-designer`; roster row replaces economy-designer; references to economy-designer in other roles and skills updated | The analyst and live-ops designer roles (planned; hand-off briefs only) |
| Hand-off briefs to game designer, engineering, UI, analyst, live-ops designer, `rules/messages.md` format | Changing `platform-policy`, `analytics` or `game-design` beyond pointer lines |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×3 (paper lines 1-230; 230-440; 440-727) | Sonnet | high (J004-J009 precedent; digest item 9) | dense notes per part |
| extractor (first-game economy and progression, read-only) | Sonnet | high | kit-neutral lessons |
| fact-checkers ×2 (game cases, formulas and studies C/M/H/W, web; Roblox rules R01-R17 + Luau numbers W06-W07, local docs mirror + web) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (curve library, simulator, charts, tests) | Opus | medium (owner: "medium effort or higher") | `tools/progression/*`, `tools/tests/test_progression_*.py` |
| lead (merge, skills, role, hand-offs, evals, review) | Opus | high | 2 skills, role, hand-offs, evals, roster |
| progression-designer test (new agent, first real task) | Opus | high (owner) | the 2 worked examples: brief → feeling timeline → data tables → sim runs → charts → timeline check |
| progression-designer hidden evals | Opus | high | answers to held-out symptom briefs |
| grader (separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time (company limit). Wave 1: 3 paper extractors. Wave 2: first-game extractor + tool builder (it needs only the paper's math sections, which the lead has read and will cite by line) + fact-checker A. Wave 3: fact-checker B. The lead writes the skills (needs the paper, the fact-checks and the existing game-design/platform-policy/analytics books together). Step 6: the new agent builds both worked examples with the tools (this is its first real task and the tools' acceptance test), then runs the hidden evals; a separate grader scores both.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | 1 |
| Agents | 4 extract + 2 fact-check + 1 tool (+1 push) + 2 agent tests + 1 grader = 10-11 | 10 agents + 2 resumed follow-ups (T11 tool fixes, T12 example refresh) = 12 runs |
| Models / effort | Sonnet high ×7; Opus medium ×1-2; Opus high ×2 + lead | Sonnet high ×7; tool builder on Opus high ×2 (owner allowed "medium or higher"; chosen for the simulator's size); progression designer Opus high ×3; lead |
| Image generations | 0 | |

## Acceptance checks
- [ ] Every formula in the curve library reproduces the paper's exact sample values in a test (Lemonade waits 400/167, 214/167, ...; T_K closed form = step sum; M05 C(t)=t²/2 vs a declared discrete tick model; X_l=500l(l−1) and X_l=1000A_l; N=ceil(H/d) and TTK for both first-hit conventions; bulk-buy closed form = direct sum and max-affordable by inequality; n_q quantile; prestige formulas C01 and the z^(1/α) rule; 41.6 % stacking example). A formula the fact-check cannot back is dropped or relabelled, and the drop is listed.
- [ ] Simulator: deterministic given data + policy + seed; reads JSON data tables; reports time to each goal in active and calendar time, walls (soft: affordability; hard: prerequisite), power spikes (discrete breakpoint changes against unchanged reference content), blocked or unreachable paths (zero income = unreachable, never 0 or a crash), and the currency ledger closes (end = start + sources − sinks ± named adjustments) with zero residual; every run records data revision, policy and assumptions.
- [ ] Charts: one self-contained HTML file per run, standard library only, opens offline; shows curves, the timeline with goals, walls and spikes marked, and the assumptions; readable on a phone width.
- [ ] Worked examples: every input labelled `published` (paper source) or `EXAMPLE ASSUMPTION` (not a tuning proposal for any game); both run end to end; each target feeling on the timeline checked pass/fail/not testable with its evidence.
- [ ] No invented targets: seconds per reward, session lengths, D1/D7 numbers, first-prestige times stay owner decisions or labelled assumptions; only scoped facts are numbers.
- [ ] Roblox rules: every paid-random, PolicyService, ads, Kids/Select and pricing fact in a skill matches `platform-policy` or a dated fact-check against the docs mirror or a live page; no conflict with `platform-policy`.
- [ ] Nothing specific to DestructionSimulator in kit files (grep for its game terms = 0 hits outside source tables).
- [ ] economy-designer replaced: roster row, game-designer role, preproduction hand-offs; no stale reference left (grep = 0 outside history rows).
- [ ] Hand-off briefs to game designer, engineering, UI, analyst, live-ops designer follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "All right, go ahead. You can begin." |
| G2 first real task (worked examples + charts) | | |
| G3 final approval | | |
