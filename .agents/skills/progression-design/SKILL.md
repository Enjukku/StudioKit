---
name: progression-design
description: What and why of progression - the feeling timeline from minute one to month one, walls, power spikes, prestige, reward clocks, premium fairness. Use when progression or an economy is planned or changed, for "it's too grindy", "players quit at level X", "the upgrade doesn't feel stronger", "early game is too slow", "balance this". The owner decides targets; progression-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J011 from the owner's progression research paper (2026-10-21, fact-checked) and the first game's economy rulings. Evidence ids point to `knowledge/reference/progression/` notes (`01:`, `02:`, `03:`, `04:`) and fact-checks (`FC-M` = fact-check-cases-math.md, `FC-R` = fact-check-roblox.md). Tags: V = VERIFIED (a source publishes it), E = EXPERIENCE (a studio's or designer's account), O = OPINION (the paper's or the kit's proposal). Rebuilt by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (experience named, tracks as games, the reward tier table, confirmed celebrations, §7 core principles; repaired after review round 1). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): belief check consumer.

# Progression design: what progress must feel like, and why

Progression is not one growth curve. It is the interaction of what the player can do, what things cost, what rewards arrive, which choices are open and how long the next meaningful change takes (01:IN, O). A smooth curve can hide a discrete breakpoint or an action repeated too long. So this book keeps three things apart: **the intended feeling** (the owner's), **the model** (exact numbers under stated assumptions) and **the evidence** (playtests and live data). The model says what happens under its assumptions; only people say how it feels (01:R14, O).

## 1. When this skill starts
It answers: what should the player feel at each point from the first minute to the first month · what changes for the player at each milestone · where progress is quick, slows, hits a wall or spikes, and why · what a reset, a cap or a catch-up keeps and removes · how big each reward feels next to the others · what may be bought and what must stay earnable · what the live data says and which change is smallest. The how (curves, formulas, simulation, data tables, measuring reward rates) is `progression-craft`. Whether the whole design is fun and fair (loops, systems check, social) is `game-design`; this book does not repeat it. §7 (core principles for this craft) applies to every task; it sits after the self-check, so re-read §7 after a compaction.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Feeling timeline template, vocabulary, placing walls, spikes, plateaus, rhythm and the capstone, genre patterns | `references/timeline-genres.md` |
| Reward and celebration tier table: tiers, columns, rules, what each craft gets, worked example | `references/reward-tiers.md` |
| The 12 published cases as alternatives per design question (prestige, infinite sinks, character vs account, reward spacing, caps, levels as thresholds, movement unlocks) | `references/cases.md` |
| Reward clocks, randomness and where luck sits, the studies behind them, ethical pacing, premium fairness, Roblox rules for paid random items, ads and younger players | `references/rewards-ethics.md` |
| After launch: denominators, retention and benchmark definitions, the diagnostic matrix, survivor bias, Experiments | `references/live-data.md` |
| The math, tools, reward rates, data tables and hand-offs | `progression-craft` |
| Resources, sources and sinks, the 10-item systems check, balance workflow, cosmetics, honest paid random reveals (§8-§9) | `game-design` → `references/systems-economy.md` |
| The feature spec's feedback stack my tiers feed | `preproduction` → `references/documents.md` §6 |
| The current platform rule, API and owner actions | `platform-policy` |
| Event names, limits and dashboards | `analytics` |

## 3. Steps
1. **Get the experience first.** From the owner and the game designer: the named target experience (mastery, collection, expression, fellowship, discovery, competition; never "fun"), what should become easier, what should stay hard, which choices should open, what must never be bought away, who the players are, how long they play and on what device (01:R01, 03:PS1, O). Write problem, constraints and success test in the working file before any number. A request that already names its fix ("lower the price") is first restated as the problem it points to. If that problem is a claim about where this game's players stall or quit, its test is the analyst's belief check (`orchestration` SKILL §1 step 1), not the model; no data: keep it as a hypothesis labelled O and carry on with `EXAMPLE ASSUMPTION` labels. Missing → ask; never fill it with a genre habit.
2. **Write the feeling timeline** (`references/timeline-genres.md` §1): per checkpoint the target feeling, the observable sign, the state the player should be in, whether the clock is active play or calendar age, and what on screen shows the distance to the next goal. Every target is a hypothesis until a person plays the build (01:S4-S5, O).
3. **Name each milestone's benefit:** capability, choice, understanding, expressive ownership, access or recognizable accomplishment, with what the player can now do that they could not before (01:B1, R03, O). "The number got bigger" is not a benefit unless an unchanged reference (the same enemy, the same stage, the same purchase) now plays differently (01:R07, S3). Items join a named theme family the player can collect or build around.
4. **Make every track a game:** its goal, opposition (cost, enemy, skill test), decisions (what to buy, when to reset, which route) and rules, one line each in the working file's track sheet. A stretch where every strategy buys the same things in order has no decision: keep it only on purpose (a tutorial), else open a choice.
5. **Place the shape on purpose:** fast starts, slowdowns, soft walls (affordable but expensive), hard walls (need a key, unlock or skill), spikes and plateaus, each with its reason and exit (`references/timeline-genres.md` §2-3). Every wall names its counter: the income, route, gear or skill that beats it. A plateau needs a stated learning goal and exit condition; "the economy must last longer" is not one (01:PL1, O). Gaps between rewards vary; each finite track rises to its capstone.
6. **Pick the job of each track:** teaching, dedication, account convenience, competitive power, optional challenge, surplus sink, cosmetic expression; keep tracks with different jobs apart (01:KX1, Q1-Q7; `references/cases.md`). Cosmetic tracks carry no stats.
7. **Check rewards, luck and ethics** (`references/rewards-ethics.md`): the four clocks, spacing between usable rewards (not only the total), where luck sits and where skill decides, luck with a bounded fallback for anything essential, stopping freedom, no friction designed to sell an escape. Paid random items, ads and younger players: `platform-policy`, every time.
8. **Hand the targets to `progression-craft`:** it builds the model, proves the timeline, measures each reward's rate and returns options with trade-offs. The owner chooses between concrete experiences, never between unexplained coefficients (01:R15; 03:PS8, O).
9. **Tier the rewards and celebrations** when the task adds or changes rewards (`references/reward-tiers.md`; otherwise write "tier table: not in scope"): each reward event gets a tier from its benefit, checked against its measured rate per named policy; rarer means bigger; celebrations fire only on the confirmed result. The table reaches each partner before it builds a reward moment (`references/reward-tiers.md` §6).
10. **After launch:** read the analyst's data with the right denominator, name competing explanations, change the smallest lever (`references/live-data.md`).

## 4. Craft core (what separates great progression design from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **Experience before math.** The math implements an approved feeling; never pick exponential growth because the genre usually has big numbers. Pacing numbers set tone too (§7 row 10) | 01:R01; 03:PS4 (O); E |
| D-02 | **A milestone changes what the player can do.** Six benefits: capability, choice, understanding, expressive ownership, access, recognizable accomplishment. Keep a reward ledger per milestone: functional change, presentation (its tier), next use, optional or not | 01:B1, B4 (O; synthesis, no source states the list: FC-M OL1) |
| D-03 | **Learning ≠ unlocking.** Hand over the unlock condition AND a situation that makes the unlock useful (a generator brings a production trade-off; an ability opens a build; a movement verb opens a route): the next stage has a hole shaped for the new tool | 01:B2 (O, lens from Cook H06 and Koster H07, E); E |
| D-04 | **Early win = understandable causality:** I acted, the result changed, I know the next action. Easy is not incompetent; hard is not deep; offer challenge choice | 01:B3 (O; H01 association, H05 meta-analysis, FC-M confirmed) |
| D-05 | **Grind is defined by the audience,** not by repetition: activity players report as low-value for the time it takes. First tell apart comprehension, skill, resource bottleneck and unavoidable wait; more earnings do not fix an unreadable objective; a requested fix is restated as its problem (§3 step 1) | 01:B5 (O); E |
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
| D-21 | **Rarer feels bigger** (§3 step 9) | E |
| D-22 | **Celebrate the confirmed result, sized by a learnable cause,** escalating at real thresholds (`references/reward-tiers.md` §5) | E |
| D-23 | **Counters tell the truth** (`progression-craft/references/data-handoff.md` §5) | E |
| D-24 | **Numbers become a fantasy:** theme families with rank ladders (§3 step 3; `references/reward-tiers.md` §4-§5) | E |
| D-25 | **Every track is a game** (§3 step 4) | E |
| D-26 | **Place luck and skill on purpose** (§3 step 7; `references/rewards-ethics.md` §3) | E |
| D-27 | **Progress is always visible** (§3 step 2; `progression-craft` C-19) | E |
| D-28 | **Time is the player's seconds** (`progression-craft` §3 step 2) | E |

## 5. Rules (final check, short)
- Every target feeling, time window, price and pacing number is a PROPOSAL until the owner decides it (decision id and words in `knowledge/design/decisions.md`). No universal pacing number exists; never invent one (01:U1; 03:OQ1). Starting values in my references (tier rate ceilings, midpoint events) are PROPOSAL defaults a test may change.
- Published game numbers are evidence of that game's stated version only, never Roblox tuning (01:R02, KT3).
- Paid random items, paid currency, ads, trading and younger players: load `platform-policy` at design time and at review; check `PolicyService` per player; never design a paid luck system the free route needs. How a paid result is revealed: `game-design/references/systems-economy.md` §9; `platform-policy` wins over any line here.
- Feelings are hypotheses; simulated players are strategies, not the population (01:R12). Feel at normal speed is the owner's call on a playable preview; I never claim it from a model.
- Hand-offs follow `rules/messages.md`; the owner approves the experience and the trade-offs, not thousands of cells (03:PS8).

## 6. Self-check before returning
Each line names its input. "Report" = a `sim.py` report of this model revision; "table" = my working-folder table; `tools.md` = `progression-craft/references/tools.md`.
- [ ] (working file) The owner's words, the named target experience, problem, constraints, success test; every requested fix restated as its problem.
- [ ] (timeline) Every target: observable sign, active or calendar clock, what shows progress to the next goal; long goals have a midpoint event.
- [ ] (reward ledger + model) Each milestone names its benefit, the unchanged reference it is measured on and, for an unlock, the next situation that uses it; every item has a theme family; cosmetic items carry no stat effects; empty milestones: 0.
- [ ] (track sheet + two reports) Each track has goal, opposition, decisions, rules; decision check run (`tools.md` §6b); each identical stretch is on purpose or reopened.
- [ ] (timeline + report) Every wall says soft or hard, why it is there and its counter; every plateau has a learning goal and exit; boss walls: the struggling profile's attempts to first win inside the row's tolerance.
- [ ] (timeline) Resets, caps and catch-up list what is kept, removed, merged and granted.
- [ ] (full report) Reward spacing checked, not only totals: gaps and the longest stretch with no step, completion or win (`tools.md` §6a); essential luck has a bounded fallback.
- [ ] (seeded reports) Where luck sits is written per track; skill profiles over seeds (`tools.md` §6c): the spread matches the intent.
- [ ] (tier table + full single-run reports; only when rewards change, else "tier table: not in scope") Every reward event tiered by its benefit, repeats apart from first times; the rate, order and capstone checks of `reward-tiers.md` §8 pass for every named policy.
- [ ] (tier table + model) Every celebrated trigger is a confirmed grant (ledger source or goal); no size from a random roll; paid rows through the odds check (`tools.md` §6d).
- [ ] (UI brief) Counters use the true value; the number display rule and its fixtures are in the brief; each locked item carries its readable requirement.
- [ ] (reward ledger + full report) Reward problems diagnosed with the reward ledger (what each step changes) and the four clocks, not only totals.
- [ ] (odds table + `platform-policy` rules §A) Monetized or random parts checked against `platform-policy`, written out in full: no paid random outcome sells back into its price currency; odds before purchase with the rounding rule and disclaimer, luck-boost display, odds updated after a once-only win, `PolicyService` per player, the restricted-player treatment chosen; younger players have a working route.
- [ ] (old vs new model) Pay or reward changes keep special variants on their own multiplier and re-derive every dependent price.
- [ ] (partner exchange notes) Game designer, VFX, sound, UI and art restated the tiers, rates and look ranks they use with no open question; else not verified.
- [ ] Every number labelled: owner decision, PROPOSAL, EXAMPLE ASSUMPTION, published (with version) or measured (with dataset); every check labelled gate-verified, MCP-verified, owner-confirmed or not verified; a could-not-check list ends the hand-back.

Project overlay: if `knowledge/overlays/progression-design.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's universal principles (master numbers), stated for my work: timelines, curves, tiers and tables. Principles 5 (shape and silhouette), 9 (push past real) and 12 (controlled variation) are craft execution; my side of them is the look rank I hand the art director (row 11), readable spikes (row 1) and tiers that never come from a random roll (rows 3, 19).

| # | Principle, for my work | Example from my craft | My check (input) |
| --- | --- | --- | --- |
| 1 | **The gameplay read comes first.** Progress reads in play: what changed, what is next, how far; a spike changes an outcome the player sees | +4 % damage that leaves a wolf at 3 hits is invisible; the step that makes it 2 hits reads | Each spike names its reference outcome change (report); each timeline row names what shows progress |
| 2 | **Judge where players meet it.** Pacing in the real session shape and device: short phone sessions, returners; arithmetic is not the experience | A gate at 25 active minutes passes a 60-minute session and fails a 10-minute phone session | Session-pattern runs for the brief's session shape (report); feel = owner on a playable preview, else not verified |
| 3 | **Decide what is read first.** Rewards and celebrations are tiered so the rare and important feel bigger | A common pet from an egg gets a plain reveal; the secret pet gets the top tier | Tier table: each tier's summed rate inside its ceiling and below the tier under it (full reports) |
| 4 | **Big before small.** Experience, timeline, graph and the places of walls and spikes before any coefficient | Where the rebirth wall sits is decided before its price constant | Dated timeline and graph exist before the first model value (working folder) |
| 6 | **Less is more.** The fewest currencies, tracks and milestones, each changing something; one-line rules for a young audience | A third currency that only converts to coins is cut | Currency count, one job per track, empty milestones 0 (model, ledger) |
| 7 | **One code for meaning.** One rounding and modifier order, one pay rule by difficulty, one tier code across the game, one home per number | A zone-3 boss pays by the same difficulty curve as zone 1 | Fixtures equal in model, export and runtime; tier names identical in every feature |
| 8 | **Timing tells cause and effect.** Fast start, varied gaps, rising to each track's capstone; a celebration follows its cause | A reward every 60 s like a clock flattens; vary the gaps and end on the rebirth | Gaps between steps not all equal (report); each finite track's planned finish row holds its top tier, read at that row's goal time, not at the report's last step |
| 10 | **The subject's character drives every choice.** The fantasy picks the curve; numbers set tone | A dragon-tamer game wants rare heavy power jumps; a cosy farm, frequent small growth | Each curve choice cites the timeline feeling it serves (design file) |
| 11 | **One world, one style; identity survives every variant.** Items in theme families with rank ladders; only the top tier breaks the style, by decision | "Lava" and "Ocean" pet families, each ranked 1-5 | Every item row has family and rank; break rows carry an owner decision id (table) |
| 13 | **Problem, constraints and target first.** Experience, session model, device, policy limits and success test before numbers | "Make upgrades feel better" becomes "a bought sword drops a known enemy by one hit" | The restated brief stands before the model (working file) |
| 14 | **Research, distinct options, a reasoned pick.** Published cases as alternatives; options bracket the key number; one recommendation | Rebirth requirement low, high and between, each simulated | Options page from the same runs; a reason per rejection (charts) |
| 15 | **Cheap stages first; gates freeze decisions.** Trace and simulation before export; tables freeze at the owner's pick; closed options logged | A rejected "daily streak" option is not brought back next round | Export only after a decision id; closed-options list current |
| 16 | **Critique against the goal, one named problem at a time.** Diagnose the problem behind a note; change one lever, re-simulate | "Too grindy at level 12" turns out to be an unclear next goal, not the XP cost | Each change names its problem, one lever and an outcome diff (reports) |
| 17 | **Build for the next craft and the engine.** Contract, fixtures, precision, readable requirements, the tier table | Engineering's tests reproduce cost at n; UI shows "need level 12" from the export | Fixtures pass in engineering's tests; crafts restate with no open question |
| 18 | **Know when it is done.** A pass budget (tuning rounds before the owner sees options) in the restated brief; every timeline row has a verdict, options and a recommendation exist, the tier table is filled when rewards changed; stop when a pass changes no verdict | A fourth tuning pass that moves no verdict is not run | Hand-back shows each stop criterion passing and the rounds used against the budget |
| 19 | **Feedback follows the real outcome.** Celebrations on the confirmed grant, sized by benefit and rarity; paid results honest | Offline earnings celebrate the granted amount after the grant | Every celebrated trigger is a ledger source or goal; paid rows checked (`tools.md` §6d) |
| 20 | **Every player can read it.** Tiers have written names, odds are numbers, never colour or motion alone | "Secret" is written on the reveal, not only shown in gold | Every tier row has a text name; odds rows are numbers (table) |
