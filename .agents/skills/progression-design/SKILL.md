---
name: progression-design
description: Decide what a Roblox game's progression must feel like and why, before any number is tuned - the feeling timeline from the first minute to the first month (fast start, slowdown, soft and hard walls, power spikes, plateaus, resets, catch-up), what each milestone lets the player do, reward clocks and spacing, prestige and reset design, gear and enemy scaling by breakpoints, premium fairness, Roblox rules for paid random items, ads and younger players, and reading live data with the right denominator. Universal - incremental and simulator games, tycoons, RPGs and action games, obbies, competitive and collection games. Use when progression or an economy is planned, changed or reviewed, or when the owner says "it's too grindy", "players quit at level X", "the upgrade doesn't feel stronger", "early game is too slow", "prestige feels pointless", "the reward track feels empty", "balance this". Read by the progression designer first; the game designer, UI, analyst and live-ops read it for the shared rules. Proposes; the owner decides every target and value.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J011 from the owner's progression research paper (2026-10-21, fact-checked) and the first game's economy rulings. Evidence ids point to `knowledge/reference/progression/` notes (`01:`, `02:`, `03:`, `04:`) and fact-checks (`FC-M` = fact-check-cases-math.md, `FC-R` = fact-check-roblox.md). Tags: V = VERIFIED (a source publishes it), E = EXPERIENCE (a studio's or designer's account), O = OPINION (the paper's or the kit's proposal).

# Progression design: what progress must feel like, and why

Progression is not one growth curve. It is the interaction of what the player can do, what things cost, what rewards arrive, which choices are open and how long the next meaningful change takes (01:IN, O). A smooth curve can hide a discrete breakpoint or an action repeated too long. So this book keeps three things apart: **the intended feeling** (the owner's), **the model** (exact numbers under stated assumptions) and **the evidence** (playtests and live data). The model says what happens under its assumptions; only people say how it feels (01:R14, O).

## 1. When this skill starts
It answers: what should the player feel at each point from the first minute to the first month · what changes for the player at each milestone · where progress is quick, slows, hits a wall or spikes, and why · what a reset, a cap or a catch-up keeps and removes · what may be bought and what must stay earnable · what the live data says and which change is smallest. The how (curves, formulas, simulation, data tables) is `progression-craft`. Whether the whole design is fun and fair (loops, systems check, social) is `game-design`; this book does not repeat it.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The feeling timeline template, the vocabulary, placing walls, spikes and plateaus, genre patterns | `references/timeline-genres.md` |
| The 12 published cases as alternatives per design question (prestige, infinite sinks, character vs account, reward spacing, caps, levels as thresholds, movement unlocks) | `references/cases.md` |
| Reward clocks, randomness, the studies behind them, ethical pacing, premium fairness, Roblox rules for paid random items, ads and younger players | `references/rewards-ethics.md` |
| After launch: denominators, retention and benchmark definitions, the diagnostic matrix, survivor bias, Experiments | `references/live-data.md` |
| The math, tools, data tables and hand-offs | `progression-craft` |
| Resources, sources and sinks, the 10-item systems check, balance workflow | `game-design` → `references/systems-economy.md` |
| The current platform rule, API and owner actions | `platform-policy` |
| Event names, limits and dashboards | `analytics` |

## 3. Steps
1. **Get the experience first.** From the owner and the game designer: what should become easier, what should stay hard, which choices should open, what must never be bought away, who the players are, how long they play and on what device (01:R01, 03:PS1, O). Missing → ask; never fill it with a genre habit.
2. **Write the feeling timeline** (`references/timeline-genres.md` §1): per checkpoint the target feeling, the observable sign, the state the player should be in, and whether the clock is active play or calendar age. Every target is a hypothesis until a person plays the build (01:S4-S5, O).
3. **Name each milestone's benefit:** capability, choice, understanding, expressive ownership, access or recognizable accomplishment, with what the player can now do that they could not before (01:B1, R03, O). "The number got bigger" is not a benefit unless an unchanged reference (the same enemy, the same stage, the same purchase) now plays differently (01:R07, S3).
4. **Place the shape on purpose:** fast starts, slowdowns, soft walls (affordable but expensive), hard walls (need a key, unlock or skill), spikes and plateaus, each with its reason and exit (`references/timeline-genres.md` §2-3). A plateau needs a stated learning goal and exit condition; "the economy must last longer" is not one (01:PL1, O).
5. **Pick the job of each track:** teaching, dedication, account convenience, competitive power, optional challenge, surplus sink; keep tracks with different jobs apart (01:KX1, Q1-Q7; `references/cases.md`).
6. **Check rewards and ethics** (`references/rewards-ethics.md`): the four clocks, spacing between usable rewards (not only the total), luck with a bounded fallback for anything essential, stopping freedom, no friction designed to sell an escape. Paid random items, ads and younger players: `platform-policy`, every time.
7. **Hand the targets to `progression-craft`:** it builds the model, proves the timeline and returns options with trade-offs. The owner chooses between concrete experiences, never between unexplained coefficients (01:R15; 03:PS8, O).
8. **After launch:** read the analyst's data with the right denominator, name competing explanations, change the smallest lever (`references/live-data.md`).

## 4. Craft core (what separates great progression design from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **Experience before math.** The math implements an approved feeling; never pick exponential growth because the genre usually has big numbers | 01:R01; 03:PS4 (O) |
| D-02 | **A milestone changes what the player can do.** Six benefits: capability, choice, understanding, expressive ownership, access, recognizable accomplishment. Keep a reward ledger per milestone: functional change, presentation, next use, optional or not | 01:B1, B4 (O; synthesis, no source states the list: FC-M OL1) |
| D-03 | **Learning ≠ unlocking.** Hand over the unlock condition AND a situation that makes the unlock useful (a generator brings a production trade-off; an ability opens a build; a movement verb opens a route) | 01:B2 (O, lens from Cook H06 and Koster H07, E) |
| D-04 | **Early win = understandable causality:** I acted, the result changed, I know the next action. Easy is not incompetent; hard is not deep; offer challenge choice | 01:B3 (O; H01 association, H05 meta-analysis, FC-M confirmed) |
| D-05 | **Grind is defined by the audience,** not by repetition: activity players report as low-value for the time it takes. First tell apart comprehension, skill, resource bottleneck and unavoidable wait; more earnings do not fix an unreadable objective | 01:B5 (O) |
| D-06 | **Spikes are measured on unchanged content the player can reach.** If the enemy scales at the same moment as the weapon, the spike may not exist; if cost and income both rise, the ratio decides speed | 01:S3, R07 (O); 4 → 5 damage on a 5-HP enemy is +25 % damage but halves the hits (02:RP6, FC-M) |
| D-07 | **Soft wall ≠ hard wall.** Affordability (reachable by repeating) and a prerequisite (a key, an unlock, a skill test) are different walls with different fixes | 01:VC3-VC4, ST2 (O) |
| D-08 | **Spacing beats totals.** A generous track can still feel empty; Blizzard cut the Hearthstone track by 37,000 XP (nearly 20 %), cut weekly wins 7 → 5, added gold and spread bonus levels 150 → 350, changing total AND spacing | 01:K7 (V/E, C05 2020-12-07; corrected FC-M #6) |
| D-09 | **Exponential costs belong in voluntary sinks,** not in the gate to ordinary content (Factorio's optional infinite research after finite goals) | 01:K4 (V/E, C02 2016-10-21; transfer O) |
| D-10 | **Resets are designed by what they keep.** Write what a reset removes, keeps, merges and grants, and what the next run looks like, before choosing a formula; pick lifetime-, maximum- or since-reset-based prestige for the behaviour you want | 01:R08, VC9, Q1 (O); Pecorella's four bases in two categories (FC-M #1) |
| D-11 | **Separate tracks by job:** first-character teaching, alt catch-up, optional challenge (Diablo IV 2024); dedication identity vs short skill goals vs combat power (LoL mastery 2024 plan, Overwatch 2025); define max-merge vs sum vs per-character for shared progress (WoW Renown 5 + 10 → 10) | 01:K5, K6, K9, K11 (V/E; FC-M confirmed, LoL = pre-release plan) |
| D-12 | **A level should change feasible decisions,** not only stats (TFT 13.23 gave each level a composition identity); an unlock can be a movement verb or route, not a percentage (Mario Wonder badges) | 01:K10, K12 (V/E; transfer O) |
| D-13 | **Caps shape where account power meets competition;** move the supply of the upgrade resource and the cap together (Clash Royale 2023) | 01:K8 (V/E, C06-C07; FC-M: caps effective 2023-12-04) |
| D-14 | **Calendar ≠ active play.** "First day" and "first week" are calendar age; targets need a session model; no universal minutes-per-level, rewards-per-session or time-to-prestige exists | 01:S4, ST3, U1 (O) |
| D-15 | **Essential progress never waits on unbounded luck.** Deterministic path or a visible bounded fallback; test unlucky paths, not the average | 02:W6 (O) |
| D-16 | **Never sell the escape from designed friction;** never tailor bad luck to push a purchase; never punish a missed day by taking earned progress | 02:W7 (O, motivated by H11, not proven by it) |
| D-17 | **Reward follows the content's difficulty, through a curve chosen for fun.** When the same content gets tougher in later areas, its pay follows that toughness smoothly (not a flat step per area, no need for round numbers); bigger and harder things pay more; a rare variant gets its own multiplier so it does not scale twice; farming an early area with top gear pays little, and earlier gear stays usable | first game, owner rulings 2026-10-02 to 10-12 (04:O01-O03, O06-O07) |
| D-18 | **Removing a chore changes the economy.** Crediting rewards at once instead of a collect step raised real income and opened a camping route; re-measure income per minute on the same route and re-derive every dependent price, cap and product | first game (04:O04, F03, F07) |
| D-19 | **Young audience → one-line rules.** Each reward rule explainable in one line; odds shown | first game, owner ruling 2026-10-09 (04:O15) |
| D-20 | **A model pass is not fun.** Arithmetic, observed play and policy compliance are three separate gates; the owner can reject a model that passes every arithmetic check | 01:R14; 03:PC2-PC3 (O) |

## 5. Rules (final check, short)
- Every target feeling, time window, price and pacing number is a PROPOSAL until the owner decides it (decision id and words in `knowledge/design/decisions.md`). No universal pacing number exists; never invent one (01:U1; 03:OQ1).
- Published game numbers are evidence of that game's stated version only, never Roblox tuning (01:R02, KT3).
- Paid random items, paid currency, ads, trading and younger players: load `platform-policy` at design time and at review; check `PolicyService` per player; never design a paid luck system the free route needs.
- Feelings are hypotheses; simulated players are strategies, not the population (01:R12).
- Hand-offs follow `rules/messages.md`; the owner approves the experience and the trade-offs, not thousands of cells (03:PS8).

## 6. Self-check before returning
- [ ] The intended experience is written with the owner's words; every timeline target has an observable sign and says active play or calendar.
- [ ] Each milestone names its benefit and the unchanged reference it is measured on.
- [ ] Every wall says soft or hard, why it is there and how the player leaves it; every plateau has a learning goal and exit.
- [ ] Resets, caps and catch-up list what is kept, removed, merged and granted.
- [ ] Reward spacing checked, not only totals; essential luck has a bounded fallback.
- [ ] Reward problems diagnosed with the reward ledger (what each step changes) and the four clocks, not only totals.
- [ ] Monetized or random parts checked against `platform-policy`, written out in full: odds before purchase with the rounding rule and disclaimer, luck-boost display, `PolicyService` per player, the restricted-player treatment chosen; younger players have a working route.
- [ ] Pay or reward changes keep special variants on their own multiplier and re-derive every dependent price.
- [ ] Every number labelled: owner decision, PROPOSAL, EXAMPLE ASSUMPTION, published (with version) or measured (with dataset).

Project overlay: if `knowledge/overlays/progression-design.md` exists, read it after this file; it wins for this game.
