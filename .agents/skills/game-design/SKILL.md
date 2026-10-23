---
name: game-design
description: Judge and improve a Roblox game design before it is built - core loop, design principles as tests, systems, economy, rewards, balance, ranked minimal fixes. Use when a loop, system, economy, feature or update is proposed or changed, for "is this fun", "it isn't fun and I don't know why", "players quit after X", "review this design", "balance this". The owner decides targets.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J003. Evidence: owner research paper Part 2 (notes `knowledge/reference/game-design/03-loops-systems.md` = **N3**, `04-levels-social-review.md` = **N4**), the DestructionSimulator `game-design` skill (Riot "So You Wanna Make Games??" transcripts, 2026-10-15) = **DS**, fact-checks **FR** / **FI**. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION. Rebuilt by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (feedback that follows the real outcome, readable threats, behaviour before art, maps as the board, cosmetics and paid reveals, craft-output reviews, §7 core principles). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): belief check in the claim ledger.

# Game design: find what will confuse, bore or frustrate, and fix the cause

## 1. When this skill starts
A loop, system, economy, feature, level plan or update exists as a proposal, a spec, a build or player data, and someone must judge it. It answers: what experience is intended, does the causal model deliver it, where does it break, how sure are we, and what is the smallest fix. It never replaces the owner's intended experience with the reviewer's favourite genre. It also runs when I judge another craft's output in a job recipe's review slot (role reads, play captures, "does this effect hide what players need", truth to play): `references/review.md` §7. §7 of this file (core principles) applies to every task I do: pitch, pre-production, spec, review.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Four parts of a game, naming the fun, goals vs tactics, the three loop scales and their coupling, the experiment card, the plain-block test, the 12-item core loop check | `references/loops.md` |
| The 10 principles as tests, fairness, luck vs skill, mechanics that carry the theme, progress and arcs, feedback that follows the outcome, readable threats, what is read first | `references/principles.md` |
| Resources, sources and sinks, economy scenarios, balance workflow, progression, reward schedules, prices, Roblox monetization and young players, the 10-item systems check, cosmetics and variants, honest paid random reveals | `references/systems-economy.md` |
| Maps and modes as gameplay: the board, the stage's job, round starts, neutral space, cover, hazards and their rules, the blockout limit, secrets, player metrics | `references/spaces.md` |
| Groups and friends, competition, status, abuse, Roblox age tiers and chat | `references/social.md` |
| Playtest protocol and record, what each input can prove, Roblox analytics definitions, live updates and events, the update evaluation | `references/playtest-live.md` |
| The 12-step review, critique order, severity, fix ranking, the 9-item feature check, the finding template, the do-not list, reviewing a craft's output per job recipe | `references/review.md` |
| Levels, routes, encounters (the full level review) | `level-design` skill |
| Concepts and pitches | `game-concept` skill |
| Feature spec, feedback stack, threat and hazard sheets, role card, tuning table formats | `preproduction/references/documents.md` |
| Purchases, paid random items, ads, chat, player data | `platform-policy` skill |
| Funnels, retention, A/B tests in Roblox | `analytics` skill |

## 3. Steps (the review, short form of `review.md` §1)
1. **Identify** the artifact, version, the owner's approved intent and the question. Keep approved intent apart from suggestions and discarded variants. Write the target experience (one or two kinds of fun, `loops.md` §2) and the game's parameters (camera, device, player count, input, session shape); no review starts without them, or without assumed values written down as assumptions.
2. **Extract the causal model:** the four parts in one line each (goal, opposition, decisions, rules; an empty "decisions" line is a finding); loop = goal, action, state change, feedback, next decision; system = stocks, flows, dependencies, incentives; feature = inputs, states, outputs.
3. **Claim ledger:** tag every claim V / E / O with source, date and scope; unsourced numbers go into the assumptions list. A claim about what this game's current players do, which player data could settle, stays O and goes to the assumptions list with "analyst belief check" as its test; ask the lead for the check (`orchestration` SKILL §1 step 1) only when a different answer would change the verdict. Label what each input can prove (a spec shows values, not a read; one screenshot shows no timing; a frame sequence shows timing; a play-test shows behaviour): `playtest-live.md` §1b.
4. **Consistency before taste:** walk a success path, a failure path, a boundary and a multiplayer disagreement; find contradictions between documents, tuning, marketing and the build, and between what a thing looks like and what it does.
5. **Against the fantasy and the target players, where they meet it:** what does the player do, see, choose, learn and repeat, at the game camera, on a phone, in the busiest moment? What does each object or enemy say by its behaviour alone?
6. **Checklists** that apply (loop, principles, feedback and threats, systems, cosmetics, social, spaces, level, feature). Each failure cites an observed example or a missing artifact.
7. **Adversarial pass:** optimal-but-unfun strategies, griefing, collusion, dominant builds, resource runaway, reward farming, interrupted saves, a request the server rejects, the worst-case crowd of effects.
8. **Rank fixes** (`review.md` §3): name one problem at a time, fix the enabling cause first; propose the minimal fix and one alternative with a different tradeoff; one recommendation to the owner. When a note or request carries its own solution, restate the problem behind it first.
9. **Close:** every finding gets a disposition; failed hypotheses go to `knowledge/design/tried-and-failed.md`; end with an honest recap (what works, the weakest point, what could not be checked and which capture or test would close it).

Craft-output reviews (my slot in a job recipe): same evidence rules, the per-recipe lists in `review.md` §7, judged on the captures the recipe names, never on the maker's hand-back alone.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| G-01 | **Judge the intended experience, not content volume.** Name one or two target experiences (fantasy, thrill, fellowship, mastery, discovery, expression, collection, competition, comfort), never "fun"; every brief quotes them. A feature that serves another kind of fun can make the game worse: file it as a proposal, do not build it | S1 O (N3); DS §2; E |
| G-02 | **Goal before tactics.** Agree what the player should feel and do, then compare rules and numbers against it. Most stuck debates are two tactics serving different goals; tag each note goal or tactic | DS §3; E |
| G-03 | **Loops at three scales, coupled on paper.** Moment (what information changes the next decision), session (purpose → bounded activity → outcome → stop or continue), long term (aspiration → growth → changed possibilities). Draw entry state → moment decisions → session outcome → what persists → changed next-session options | N3 §2.2-2.3 O; Cook D01 O |
| G-04 | **A bigger multiplier is not a new experience by itself.** If the only lasting change is a larger number meeting larger costs, ask what the player now anticipates, expresses or enjoys differently; if meta rewards make the best route skip the core play, the systems conflict | N3 §2.3 O |
| G-05 | **Prototype the risk that can kill the game first, in the crudest form.** Paper or plain Studio Parts with stand-in colours nobody mistakes for final art. One-page experiment card; PASS when the build answers the risky question and the team named a result that would change the plan. "Testers liked it" and "the designer played it well" are FAIL. No production art brief for a mechanic before its grey-box verdict exists | S5 O; N3 §2.5 O; E |
| G-06 | **Counts are scoped history, not quotas.** Wonder's 2,000+ were sticky-note ideas; Supercell cancelled nine games during Clash Royale's development (2016) and counted five hits vs 30+ killed (2023). No prototype quota or kill rate transfers | D02, D04, D05 V as reported (FI IC54-IC57) |
| G-07 | **Principles are tests with fail conditions** (clarity, meaningful choice, fairness, learnability, feedback, pacing, difficulty, discovery, expression, time respect). A particle burst cannot repair unclear cause and effect | N3 §3.2 O |
| G-08 | **Fair frustration only.** A loss must be rebuildable from information the player had: learnable rule, counterplay or a knowingly accepted risk. Every obstacle names its counter; the same threat always gives the same tell. Pacing frequency and difficulty amplitude are separate dials | DS §6; N3 §3.2; L4D D11 V (FI); E |
| G-09 | **Model every resource's creation, destruction, conversion and transfer** before tuning rewards; a payment between players is not a sink unless a fee is destroyed; judge distributions, not one income curve | S10 O; Dormans D28 V |
| G-10 | **Fast reward routes can kill the core loop.** Blizzard judged the Diablo III auction house pulled players away from the intended reward loop and removed it | S11 E (D17, FI) |
| G-11 | **Every unlock has a purpose:** new verb, new tradeoff, expression, world access, mastery test, social role, or a wanted convenience. No streak loss, absence penalties, fake scarcity or exhaustion loops as "engagement" | N3 §4.5 O |
| G-12 | **Social design is structure, not moderation.** Pair every harmful affordance with prevention, visibility, recovery and a safe exit; cooperation must work without open chat | S13 O; N4 §2 |
| G-13 | **Test the real audience at the real stage.** Short beta retention does not validate long-term systems (Squad Busters); no universal tester count exists; an AI's imagined playthrough is not a playtest | S14 O; D29 V as reported (FI); N4 X9 |
| G-14 | **Metrics with context.** "Data is evidence, but not a conclusion" (Mega Crit); averages hide extremes; a low pick rate can mean unfamiliar, badly shown, narrow or weak | S9 E (D16); D13 E |
| G-15 | **Fix the enabling cause, smallest change first.** Unreadable attack → telegraph and camera before more health; no strategic choice → new situations before more upgrades; empty transit → route and activity placement before faster movement; a flat effect → outcome link and timing before more size or brightness | N4 7.06 O; E |
| G-16 | **Evidence, mechanism, options, a test; the owner decides.** A critique without a mechanism or an observable test is incomplete; never average a blocker away with good art or content volume | S15 O; N4 7.02-7.03 |
| G-17 | **Behaviour sets the read before art does.** What a thing does says what it is (a hop is a frog, dash-and-stop a ninja, area damage then gone a bomb); write behaviour first; tuning numbers set tone as well as balance. Test: plain-block test (`loops.md` §5b) | E |
| G-18 | **Art and mechanics promise the same thing.** Solid-looking things block, open doorways open, a big heavy unit is tough. Every craft brief passes the mechanic and its numbers so the look expresses them; every mismatch found in play is fixed or justified (`principles.md` §3) | E |
| G-19 | **Feedback follows the real outcome.** A small cue on every input at once; the big layer only on the confirmed result, sized by a cause the player can learn, never random, never early; refusals say what is wrong and how to fix it; frequent events short, merged, capped (`principles.md` §7) | E |
| G-20 | **Threats read before they hit.** I set each reaction window; the tell has two channels, is identical every time and ends on the damage frame; the drawn area is the hit area (`principles.md` §8) | E |
| G-21 | **Rank what must be read, and how loud.** Threat to me, own action, objective and pickups, others' effects, ambient; importance tiers cap effects, sounds and celebrations; only the rare top tier fills the screen; others' effects never shake or tint my screen (`principles.md` §9) | E |
| G-22 | **Cosmetics never cost gameplay; paid reveals never mislead.** A skin keeps the role read, footprint and stats; a paid random reveal has one windup for every result and celebrates only what the player really got (`systems-economy.md` §8-§9) | E |
| G-23 | **The map is the board.** Map mechanics stay in the background except at planned moments; a level is a puzzle shaped for the player's tools; conflict sits in the objective; every hazard has written rules (`spaces.md`) | E |

## 5. Rules (final check, short)
- No invented targets: retention, session length, drop rates, prices, difficulty tolerances. Unsupported numbers go into the assumptions list as PROPOSAL with a test. Starting values in my references (reaction windows, celebration lengths, merge windows) are PROPOSAL defaults a test may change.
- Roblox benchmark bands and examples are not targets; Roblox's discovery caps and windows are not session rules (`references/playtest-live.md`).
- Paid randomness, prices, ads, age tiers and chat: `platform-policy` decides, before and after design. A design preference cannot waive platform policy.
- No dark patterns: false scarcity, restarting timers, pressured purchases, punishing absence, essential progress behind an ad, a near-miss reveal, a celebration before the purchase or result is confirmed.
- Never present an AI walkthrough, invented persona or numerical model as player evidence.
- Do not reopen an owner decision or a closed direction without material new evidence; propose, never edit locked decisions.
- Safety and comfort faults (flash rate, no off path for shake or flashes, a reduced mode that deletes a warning) block release at any priority.

## 6. Self-check before returning (review and verdict work)
- [ ] Intended experience, game parameters and the question stated; approved intent kept apart from suggestions.
- [ ] Causal model written with the four parts; success, failure, boundary, multiplayer and rejected-request paths walked.
- [ ] Every claim tagged with source, date and scope; every finding cites evidence (observation, `path:line`, capture frame, missing artifact); each input labelled with what it can prove (gate-verified, MCP-verified, owner-confirmed, not verified).
- [ ] Judged at the game camera, phone size, busiest expected moment; no verdict rests only on a spec, a turnaround or an editor view.
- [ ] Threats: each has a counter, a two-channel tell inside its reaction window, the same tell every time, a drawn area equal to the hit area.
- [ ] Feedback: every action has an attempt cue and a confirmed-outcome layer; a rejected request shows no success layer; miss, hit, blocked and big outcomes differ with sound off.
- [ ] Read order: the capture's first-noticed element is the brief's rank 1; no environment or cosmetic element out-shouts a threat or pickup.
- [ ] Ratings are Pass / Fail / Unproven per check; no weighted total.
- [ ] Fixes ranked with the components shown; one named problem per fix; minimal fix + one alternative + the test that tells them apart; one recommendation.
- [ ] Notes written as problems with the goal they serve, not as bare solutions; each requested fix restated as its underlying problem.
- [ ] Honest recap: at least one named weakness (or why none), a "keep" list, a "could not check" list with the input that would close each item; dispositions for every finding.

Project overlay: if `knowledge/overlays/game-design.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's universal principles (master numbers), stated for my work: rules, loops, specs, briefs and verdicts. Depth lives in the references each row names. Principles 9 (push what must read past real) and 12 (controlled variation) are craft execution; my side of them is rows 1 and 3 and "variety must change decisions" (`references/loops.md` §6 item 8).

| # | Principle, for my work | Example from my craft | My check |
| --- | --- | --- | --- |
| 1 | **The gameplay read comes first.** Every rule I write reads in play: where to go, what hurts, what just happened, what I can do | A lava moat's soft glowing edge hides the kill line: I fix the read (a hard edge on the real line) before any glow | Busiest capture, game camera, phone viewport: route, ally or enemy, threat, objective and own state named at a glance |
| 2 | **Judge where players meet it.** Real build, real camera, phone size, full server, effects and UI on; paper shows systems, not feel | The phone play-test shows the sell pad sits under the thumbstick | Every verdict names its capture (build, device, camera, players); paper-only = Unproven |
| 3 | **Decide what is read first.** I rank what must be noticed per scene and screen and tier rewards and celebrations (G-21) | Boss arena: 1 wind-up, 2 my hit, 3 weak point, 4 others' effects, 5 arena | The brief carries the rank; blurred capture: first-noticed = rank 1 |
| 4 | **Big before small.** The core loop is proven in a grey box before feature specs, systems or production art | "Fly or Die": launch-and-fall feel tested with a plain Part and a force script before any wing model | A dated grey-box verdict for the loop exists before feature specs (`preproduction/references/growth-order.md` step 7) and before the first production art brief |
| 5 | **Shape and size carry meaning.** Bigger reads more important, sharp dangerous, round safe; I set the intent in the role card | A tiny boss and a huge harmless slime contradict their threat | Flat-key lineup capture: screen-size rank (`tools/art/look_check.py silhouette` area) = threat rank; a fresh reader names each role from the black-fill |
| 6 | **Less is more.** A feature earns its place against the target experience; the HUD carries only what a moment needs; "cooler" is new scope | A story cutscene "for depth" in a tycoon serves no target experience: filed, not built | Each feature traces to a target experience; each HUD item to a listed need; additions after a gate are tickets with a cost |
| 7 | **One code for meaning.** Same threat, same tell; one physics; reserved colours and shapes; written hazard rules; one orientation (`references/principles.md` §10) | Green heals, so the poison zone cannot be green | Hazard sheet complete; same tell in two captures; no colour or shape role with two meanings |
| 8 | **Timing tells cause and effect.** I set the windows (telegraph lead, contact, result, celebration length) and the stage names the crafts key to; tension rises to the climax | Rebirth: tell, build, beat, peak (the reset), result (new multiplier), then control returns | Named stages with windows in the spec; intensity plot rises toward the end; each celebration ends before the next decision (`references/principles.md` §7 checks) |
| 10 | **The subject's character drives every choice.** Verb, movement pattern and tuning say what a thing is before art | A "heavy" golem moves slowly with long settles and a wide slam | Plain-block test (`references/loops.md` §5b): a tester names the thing, theme and weight from behaviour alone |
| 11 | **One world, one style; identity survives every variant.** Themes fit the tone; variants keep role read, footprint, stats; a top tier breaks the style only by decision | A sci-fi skin in a whimsical farm game is rejected at brief stage | Each theme or variant brief cites the tone words and lists the anchors kept |
| 13 | **Problem, constraints and target before making anything.** Every spec and brief opens with problem, target experience, parameters, success test | "Make the shop fun" becomes "the player decides what to buy next in under 5 s on a phone; sign: no back-and-forth taps" | Those four items stand before any output; deviations from references listed with reasons |
| 14 | **Research, many distinct options, a reasoned pick.** Warm-up first; options differ in mechanism or hook, one atypical, equal finish; one recommendation | A dam game's flood: rising water, timed waves, or rain players redirect; I pick one and say why the others lost | Option count, distinct families, one atypical, one pick with a reason tied to the brief, a reason per rejection |
| 15 | **Cheap stages first; gates freeze decisions; do not be precious** | The owner closed "PvP theft" at step 1; later briefs do not bring it back | Closed-doors list current; nothing closed re-proposed without new owner words |
| 16 | **Critique against the goal, one named problem at a time** (`references/review.md` §8) | "Make the boss easier" becomes "players die without knowing why": a longer, clearer tell, not less damage | Each finding has goal, mechanism, evidence; each owner question has the goal word; the hand-back names one weakness |
| 17 | **Build for the next craft and the engine.** States, windows, numbers as tuning keys, the read rank; the how stays open; costs written | The VFX brief gets the slam radius as a tuning key the effect reads | Receivers restate the behaviour with no open questions; no hand-copied numbers; each costly element has a reason |
| 18 | **Know when it is done.** Stop criteria; documents go only as far as the next craft needs | A feature spec stops at its 15 fields; it does not draft the UI designer's layout | Stop criteria in the brief, each shown passing; a review round with no new notes ends |
| 19 | **Feedback follows the real outcome** (G-19, `references/principles.md` §7; paid reveals `references/systems-economy.md` §9) | Sell flow: a tick on the tap; coin burst and "+N" only on the server's confirmation; three burst sizes by sale size | Rejected-request capture shows no success layer; outcomes distinct with sound off; lowest and highest paid results share one windup |
| 20 | **Every player can read it.** No meaning on one channel; comfort settings with off paths are part of the spec | Low health: red edge pulse + heartbeat + the bar; reduced motion keeps bar and sound | Grayscale + sound off + reduced motion capture: every threat, pickup, team, tier and outcome still found; each intense channel names its off path |
