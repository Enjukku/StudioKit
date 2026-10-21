---
name: game-design
description: Judge and improve a Roblox game design before it is built - core loop, design principles as tests, systems, economy, rewards, balance, ranked minimal fixes. Use when a loop, system, economy, feature or update is proposed or changed, for "is this fun", "it isn't fun and I don't know why", "players quit after X", "review this design", "balance this". The owner decides targets.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J003. Evidence: owner research paper Part 2 (notes `knowledge/reference/game-design/03-loops-systems.md` = **N3**, `04-levels-social-review.md` = **N4**), the DestructionSimulator `game-design` skill (Riot "So You Wanna Make Games??" transcripts, 2026-10-15) = **DS**, fact-checks **FR** / **FI**. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION.

# Game design: find what will confuse, bore or frustrate, and fix the cause

## 1. When this skill starts
A loop, system, economy, feature, level plan or update exists as a proposal, a spec, a build or player data, and someone must judge it. It answers: what experience is intended, does the causal model deliver it, where does it break, how sure are we, and what is the smallest fix. It never replaces the owner's intended experience with the reviewer's favourite genre.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Four parts of a game, naming the fun, goals vs tactics, the three loop scales and their coupling, the experiment card, the 12-item core loop check | `references/loops.md` |
| The 10 principles as tests, fairness, luck vs skill, mechanics that carry the theme, where experts disagree | `references/principles.md` |
| Resources, sources and sinks, economy scenarios, balance workflow, progression, reward schedules, prices, Roblox monetization and young players, the 10-item systems check | `references/systems-economy.md` |
| Groups and friends, competition, status, abuse, Roblox age tiers and chat | `references/social.md` |
| Playtest protocol and record, Roblox analytics definitions, live updates and events, the update evaluation | `references/playtest-live.md` |
| The 12-step review, critique order, severity, fix ranking, the 9-item feature check, the finding template, the do-not list | `references/review.md` |
| Levels, routes, encounters | `level-design` skill |
| Concepts and pitches | `game-concept` skill |
| Feature spec and tuning table formats | `preproduction/references/documents.md` |
| Purchases, paid random items, ads, chat, player data | `platform-policy` skill |
| Funnels, retention, A/B tests in Roblox | `analytics` skill |

## 3. Steps (the review, short form of `review.md` §1)
1. **Identify** the artifact, version, the owner's approved intent and the question. Keep approved intent apart from suggestions and discarded variants.
2. **Extract the causal model:** loop = goal, action, state change, feedback, next decision; system = stocks, flows, dependencies, incentives; feature = inputs, states, outputs.
3. **Claim ledger:** tag every claim V / E / O with source, date and scope; unsourced numbers go into the assumptions list.
4. **Consistency before taste:** walk a success path, a failure path, a boundary and a multiplayer disagreement; find contradictions between documents, tuning, marketing and the build.
5. **Against the fantasy and the target players:** what does the player do, see, choose, learn and repeat?
6. **Checklists** that apply (loop, principles, systems, social, level, feature). Each failure cites an observed example or a missing artifact.
7. **Adversarial pass:** optimal-but-unfun strategies, griefing, collusion, dominant builds, resource runaway, reward farming, interrupted saves.
8. **Rank fixes** (`review.md` §3); propose the minimal fix and one alternative with a different tradeoff; one recommendation to the owner.
9. **Close:** every finding gets a disposition; failed hypotheses go to `knowledge/design/tried-and-failed.md`.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| G-01 | **Judge the intended experience, not content volume.** Name one or two target experiences (fantasy, thrill, fellowship, mastery, discovery, expression, collection, competition, comfort); a feature that serves another kind of fun can make the game worse | S1 O (N3); DS §2 |
| G-02 | **Goal before tactics.** Agree what the player should feel and do, then compare rules and numbers against it. Most stuck debates are two tactics serving different goals | DS §3 |
| G-03 | **Loops at three scales, coupled on paper.** Moment (what information changes the next decision), session (purpose → bounded activity → outcome → stop or continue), long term (aspiration → growth → changed possibilities). Draw entry state → moment decisions → session outcome → what persists → changed next-session options | N3 §2.2-2.3 O; Cook D01 O |
| G-04 | **A bigger multiplier is not a new experience by itself.** If the only lasting change is a larger number meeting larger costs, ask what the player now anticipates, expresses or enjoys differently; if meta rewards make the best route skip the core play, the systems conflict | N3 §2.3 O |
| G-05 | **Prototype the risk that can kill the game first.** One-page experiment card; PASS when the build answers the risky question and the team named a result that would change the plan. "Testers liked it" and "the designer played it well" are FAIL | S5 O; N3 §2.5 O |
| G-06 | **Counts are scoped history, not quotas.** Wonder's 2,000+ were sticky-note ideas; Supercell cancelled nine games during Clash Royale's development (2016) and counted five hits vs 30+ killed (2023). No prototype quota or kill rate transfers | D02, D04, D05 V as reported (FI IC54-IC57) |
| G-07 | **Principles are tests with fail conditions** (clarity, meaningful choice, fairness, learnability, feedback, pacing, difficulty, discovery, expression, time respect). A particle burst cannot repair unclear cause and effect | N3 §3.2 O |
| G-08 | **Fair frustration only.** A loss must be rebuildable from information the player had: learnable rule, counterplay or a knowingly accepted risk. Pacing frequency and difficulty amplitude are separate dials | DS §6; N3 §3.2; L4D D11 V (FI) |
| G-09 | **Model every resource's creation, destruction, conversion and transfer** before tuning rewards; a payment between players is not a sink unless a fee is destroyed; judge distributions, not one income curve | S10 O; Dormans D28 V |
| G-10 | **Fast reward routes can kill the core loop.** Blizzard judged the Diablo III auction house pulled players away from the intended reward loop and removed it | S11 E (D17, FI) |
| G-11 | **Every unlock has a purpose:** new verb, new tradeoff, expression, world access, mastery test, social role, or a wanted convenience. No streak loss, absence penalties, fake scarcity or exhaustion loops as "engagement" | N3 §4.5 O |
| G-12 | **Social design is structure, not moderation.** Pair every harmful affordance with prevention, visibility, recovery and a safe exit; cooperation must work without open chat | S13 O; N4 §2 |
| G-13 | **Test the real audience at the real stage.** Short beta retention does not validate long-term systems (Squad Busters); no universal tester count exists; an AI's imagined playthrough is not a playtest | S14 O; D29 V as reported (FI); N4 X9 |
| G-14 | **Metrics with context.** "Data is evidence, but not a conclusion" (Mega Crit); averages hide extremes; a low pick rate can mean unfamiliar, badly shown, narrow or weak | S9 E (D16); D13 E |
| G-15 | **Fix the enabling cause, smallest change first.** Unreadable attack → telegraph and camera before more health; no strategic choice → new situations before more upgrades; empty transit → route and activity placement before faster movement | N4 7.06 O |
| G-16 | **Evidence, mechanism, options, a test; the owner decides.** A critique without a mechanism or an observable test is incomplete; never average a blocker away with good art or content volume | S15 O; N4 7.02-7.03 |

## 5. Rules (final check, short)
- No invented targets: retention, session length, drop rates, prices, difficulty tolerances. Unsupported numbers go into the assumptions list as PROPOSAL with a test.
- Roblox benchmark bands and examples are not targets; Roblox's discovery caps and windows are not session rules (`references/playtest-live.md`).
- Paid randomness, prices, ads, age tiers and chat: `platform-policy` decides, before and after design. A design preference cannot waive platform policy.
- No dark patterns: false scarcity, restarting timers, pressured purchases, punishing absence, essential progress behind an ad.
- Never present an AI walkthrough, invented persona or numerical model as player evidence.
- Do not reopen an owner decision without material new evidence; propose, never edit locked decisions.

## 6. Self-check before returning
- [ ] Intended experience and the question stated; approved intent kept apart from suggestions.
- [ ] Causal model written; success, failure, boundary and multiplayer paths walked.
- [ ] Every claim tagged with source, date and scope; every finding cites evidence (observation, `path:line`, missing artifact).
- [ ] Ratings are Pass / Fail / Unproven per check; no weighted total.
- [ ] Fixes ranked with the components shown; minimal fix + one alternative + the test that tells them apart; one recommendation.
- [ ] "Could not check" list; dispositions for every finding.

Project overlay: if `knowledge/overlays/game-design.md` exists, read it after this file; it wins for this game.
