---
type: job
scope: game
status: draft
updated: 2026-10-21
source: J014-T08; live-ops-craft handoffs.md §2-§7; rules/messages.md §2; plan-2026-10-21.md; urgent-2026-10-21.md; event-halloween-masquerade.md
supersedes: []
---
> Author: live-ops-designer · claude-opus-5-5 · high · 2026-10-21

SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

# Draft hand-off briefs (nothing sent)

**DRAFT, pending owner decision.** In this test I am the only agent: none of these was sent. The lead assigns real ledger ids; `T-xx` below are placeholders. Two kinds:
- **Before the decision** (allowed inside an approved plan only after the owner's go-ahead; here they show what I would ask): T-E1 urgent estimates, T-E2 option estimates, S-1 and S-2 Studio checks.
- **After the owner picks rank 1**: T-A1, T-P1, T-G1, T-M1. Their `decision_id` stays `pending` until the lead records the owner's words.

No trend-scout brief: the recommended package uses no trend (the frog-chorus idea is deferred), so there is no trend question to ask.

---

## T-E1 → feature-builder (via the lead): urgent investigation and estimates

```text
<intent>
Players paid Robux for Beads and got nothing, and some lost Terrarium and Moth Book progress. Both started after build 1.1.1. We need to know what happened, how many players it hit, and how long a safe fix takes, before anything else uses the builder lane. Harm comes before every feature.
</intent>
<spec>
id: T-E1 (lead assigns)
from: live-ops-designer
to: feature-builder        # money and saves; the lead routes
model: opus
effort: high               # money and saves work (feature-builder role note, owner 2026-10-21)
skills: [engineering-craft, testing, data-saving, platform-policy]
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/urgent-2026-10-21.md   # take: U2, U3 facts, warnings, player message facts
  - knowledge/jobs/J014-live-ops-designer/test-pack/analyst-weekly-2026-10-20.md   # take: B7 and F (188 sales vs 181 grants in week 3)
  - knowledge/jobs/J014-live-ops-designer/test-pack/game.md   # take: §7 build 1.1.1 (Terrarium saves batched every 60 s)
fixed:
  window_of_reports: 2026-10-13 16:00 UTC (build 1.1.1) to 2026-10-20 23:59 UTC   # feedback sort
  owner_go_ahead: pending   # capacity §2: investigations are outside maintenance
open: [how to investigate, the fix, whether batching is reverted or repaired]
avoid: [a blind rollback of build 1.1.1 or a save restore that overwrites newer progress; granting Beads without a PurchaseId record]
owns: [an estimate and findings file named by the lead]
not_in_scope: [any player contact; refunds; the crate odds UI (T-E2); Halloween work]
rules:
  - Developer products are granted only in one ProcessReceipt handler; grant only after the save is loaded; store PurchaseId in the same write as the grant; return PurchaseGranted only after the save succeeds (platform-policy P-04, rules.md §B).
  - Grants of missing Beads are idempotent on PurchaseId, so no player gets them twice.
  - Never promise or imply a Robux refund; creators cannot give one (FR-46).
  - Player data stays keyed by UserId (P-09). No player names or ids leave the game's systems.
  - Changes that touch purchases or saves need the reviewer and QA before release (capacity §2).
deliver: per incident (U2, U3): cause or best explanation with evidence, affected-player count, fix options, active effort and elapsed lead time separately with a confidence label, the state-safe response for players already affected, and whether a config switch can stop the harm now
checks:
  - C1: each incident has both numbers (effort, lead time) or "cannot estimate: <missing input>"
  - C2: the U2 answer lists receipts (PurchaseId) without a matching grant for 2026-10-12 to 2026-10-20, as a count
return: hand-back to live-ops-designer, copy to lead; first result (cause or "not found yet") within the first working day
</spec>
```

## T-E2 → quick-builder and ui-ux-designer (via the lead): estimates for the plan's options

```text
<intent>
The owner will choose between a small free Halloween quest plus an Orchard signpost (rank 1), a Halloween dye set for Glow Dust (rank 2), or no Halloween. I need honest effort and lead time for each before any date reaches players, because a promise the team cannot keep breaks trust. The feature-builder is reserved for the urgent fixes, so I need to know what is truly data or config only.
</intent>
<spec>
id: T-E2 (lead assigns)
from: live-ops-designer
to: quick-builder (data, config, small UI); ui-ux-designer (crate odds panel, banner)   # the lead routes; architect only if something needs a new system
model: opus
effort: medium
skills: [engineering-craft]          # quick-builder; ui-ux-designer loads ui-design, ui-basics, platform-policy
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/plan-2026-10-21.md   # take: §C rank 0 (U1), 1 (A1, A2), 2; exclusions in §D
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/event-halloween-masquerade.md   # take: §B times, §C constraints, §D failure plan
  - knowledge/jobs/J014-live-ops-designer/test-pack/capacity.md   # take: release windows, the 24 h rule, owner-look time
fixed:
  options:
    - U1-hide: hide the Dewdrop Crate for every player and show the Moth Cabinet path, until the odds are fixed   # urgent-2026-10-21.md U1
    - U1-fix: odds for all 5 outcomes as numbers, total 100 %, a visible "Odds" label (not a bare i icon), reachable by touch, before purchase, on every platform
    - A1: gate messages for Old Orchard and Hollow Cave name the Dusk Board quest chain and where the Board is
    - A2: Masquerade quest chain at the Dusk Board, dye rewards, start 2026-10-30 15:00 UTC, end 2026-11-09 15:00 UTC, dormant until start, a post-tutorial banner
    - R2: a Halloween dye set sold for Glow Dust in the Terrarium Shop, same dates
  release_windows: Tue and Thu 15:00 UTC; no planned release within 24 h before an event starts   # capacity.md header
open: [how to build each option, reuse, risks]
avoid: [an estimate without testing, owner-look and safe-disable time; counting on the feature-builder]
owns: [the estimate file]
not_in_scope: [building anything before the owner's decision, except U1-hide if the owner approves it as urgent]
rules:
  - Active effort and elapsed lead time separately; ranges with a confidence label.
  - Say for each option whether it is data or config only, or needs code (and who would write it).
  - State what saved state each option changes and whether a config switch can disable it.
  - Paid random items: odds before purchase, numeric, total 100 %, visible Info/Details label; restricted players do not see the generator (platform-policy rules.md §A, P-01, P-03).
deliver: per option: effort range, lead time, earliest release window, data-only yes or no, dependencies, risks, persistent-state impact, disable path
checks:
  - C1: every option has both numbers or "cannot estimate: <missing input>"
  - C2: A2's answer says if a start and end time can be set in data and tested before 2026-10-30
return: hand-back to live-ops-designer, copy to lead, by Thu 2026-10-22 if A2 is to make the 10-27 window
</spec>
```

## S-1 and S-2: Studio checks I need (the lead routes them to the studio-operator; I do not drive Studio)

| Id | Build / scene | What to observe | Evidence needed |
| --- | --- | --- | --- |
| S-1 | Build 1.1.1, crate screen, a test player for whom paid random items are allowed; phone-sized touch emulation and PC | Is a way to see odds visible before the buy button? Which outcomes and percentages show? Total? Is the label a bare "i"? | Screenshots of each screen per device; the listed values. Model: sonnet, effort medium (studio-operator role) |
| S-2 | Build 1.1.1, a new player's first session, phone-sized touch emulation (and tablet), tutorial step 3 | After the first Jar drop: is the next step shown? Can the Satchel be opened, the lantern picked up, dragged and placed on a Lantern Post by touch? Where does it fail, if it fails? | Short notes per sub-step with screenshots; Output errors. Read by the game-designer (T-G1) |

---

## T-A1 → analyst: measurement plan and the phone build-mode spec (after the pick)

```text
<intent>
We will ship an Orchard signpost and a free Halloween quest to give players a reachable next goal, and we must find out why phone players stop at the lantern step. Before players see anything, we must agree what result would mean it worked, what would mean harm, and what we do in each case, so nobody reads the Halloween spike as success. The Parade taught us that a spike can be followed by fewer returning players.
</intent>
<spec>
id: T-A1 (lead assigns)
from: live-ops-designer
to: analyst
model: sonnet
effort: medium                                   # analyst role
skills: [analysis-design, analysis-craft, analytics]
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/plan-2026-10-21.md   # take: rank-1 hypotheses, §D measurement proposal and guardrails
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/brief-draft-find-the-way-masquerade.md   # take: scope, exposure, dates
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/urgent-2026-10-21.md   # take: the save-loss measure request (U3)
fixed:
  decision_id: pending                           # owner decision not yet made
  release: Tue 2026-10-27 15:00 UTC window (kind-level estimate, capacity §2b); event 2026-10-30 15:00 to 2026-11-09 15:00 UTC   # plan, PROPOSAL until decided
  eligible_players: A1 = players with 3+ active days who held 6,000 Glow Dust; A2 = players who finished tutorial step 4 and were active in the event window; A3 = new phone and tablet players
  capacity: 1 free analyst day in 2026-10-21 to 11-17   # capacity.md §1
open: [comparison design (observational, or a Roblox Experiment for the A1 gate text), windows, metric labels, guardrail margins, which item drops if one free day is not enough]
avoid: [a verdict before the window ends; blending new, continuing and reactivated players; reading peak DAU as success]
owns: [the measurement plan file; the build-mode event spec]
not_in_scope: [logging code (engineering); the feedback sort (live-ops)]
rules:
  - Name the method label: randomized (Roblox Experiment) or observational (before/after, event chart).
  - Every rate shows its counts and denominator.
  - Report new, continuing and returning players apart; no D7 for cohorts younger than 7 days.
deliver: (1) the build-mode client event spec for phone and tablet (open Satchel, pick up lantern, drag, drop on a post: success or fail, cancel); (2) the measurement plan for A1 and A2 (analysis-design experiments-updates §7); (3) a save-loss measure since 2026-10-13 for U3; (4) whether the A2 read fits into the weekly page as the Parade's B5 table did
checks:
  - C1: cohort, exposure, primary outcome, guardrails, comparison, windows and decision rule filled for A1 and A2, or the reason one cannot be measured
  - C2: the spec names each event, its fields and the platforms
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## T-P1 → progression-designer: Masquerade step sizes, the Spark Swap, rank-2 prices

```text
<intent>
The Masquerade must be finishable through ordinary play by a player who starts on the last weekend, including a phone player, and must not add Glow Dust to an economy that already has too much. Separately, the owner needs your advice on the Spark Swap: 1,005,000 Sparks are still held, and players were never told they expire.
</intent>
<spec>
id: T-P1 (lead assigns)
from: live-ops-designer
to: progression-designer
model: opus
effort: high                                     # progression-designer role
skills: [progression-design, progression-craft, platform-policy]
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/event-halloween-masquerade.md   # take: §B window, §C activity constraints and catch-up target
  - knowledge/jobs/J014-live-ops-designer/test-pack/analyst-weekly-2026-10-20.md   # take: B8 Dust in/out, Spark balances, median and p90 Dust held; B3 session lengths
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/feedback-2026-10-20.md   # take: dust-surplus vs dust-too-scarce (two groups); avoid: treating requests as specs
fixed:
  window: start 2026-10-30 15:00 UTC, gameplay end 2026-11-09 15:00 UTC, no separate claim end   # plan, PROPOSAL until decided
  target_cohort: active and returning players after the tutorial; late starter = starts Sat 2026-11-07
  reward_purpose: expression (dyes for moths); no Glow Dust, no Beads, no event currency   # plan §D exclusions
  spark_facts: 1,005,000 Sparks held by 6,120 players on 2026-10-19; Swap 10 Sparks = 150 Dust; no expiry rule was ever written   # analyst B8, game.md §5
open: [step sizes, number of steps, rank-2 dye prices in Dust, Spark Swap options and recommendation]
avoid: [a multiplier chosen to look exciting; any Dust reward in the Masquerade; removing or devaluing held Sparks without notice]
owns: [the Masquerade economy section; the Spark Swap note]
not_in_scope: [the activity design (game-designer); dates]
rules:
  - Completion must be reachable through healthy play; model late starters, low-frequency players and phone players, from observed catch rates (events-offers-rules.md §1).
  - Model alt accounts and automation; there is no trading.
  - Protect existing progress: held currency is not removed or devalued silently; any end date is true, announced and not restarted (L-09, L-13, R3).
  - Paid random items follow platform-policy §A (the crate is not part of this work).
deliver: step sizes with a trace for the Sat 11-07 starter on phone; abuse cases; rank-2 prices; Spark Swap options (keep, end with notice at the current rate, other) with the effect on Dust and the recommendation
checks:
  - C1: a player who starts on Sat 2026-11-07 finishes by 2026-11-09 15:00 UTC through ordinary sessions (show the trace)
  - C2: the Masquerade adds zero Glow Dust
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## T-G1 → game-designer: Masquerade play spec, A1 gate message, phone playtest read

```text
<intent>
Active and returning players should find a small Halloween goal at the Dusk Board and, at the end of it, know where the Orchard path starts. The update must answer: does giving players a reachable goal at the Board bring them back without a Parade-style drop afterwards? It must feel like this game: a cozy dusk walk with a net, not a bolted-on mode. Separately, read the phone playtest (S-2) and say whether the lantern step fails as a mechanic or as an instruction.
</intent>
<spec>
id: T-G1 (lead assigns)
from: live-ops-designer
to: game-designer
model: opus
effort: high                                     # game-designer role
skills: [game-design, platform-policy]
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/brief-draft-find-the-way-masquerade.md   # take: problem, hypothesis, player journey, new/returning/veteran paths
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/event-halloween-masquerade.md   # take: §C constraints and rewards
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/feedback-2026-10-20.md   # take: onboarding and zone-access themes with excerpts; avoid: treating requests as specs
fixed:
  scope: A1 gate message (Orchard, Cave) + A2 Masquerade chain at the Dusk Board; excluded: plan §D exclusions   # owner decision pending
  window: 2026-10-30 15:00 UTC to 2026-11-09 15:00 UTC   # PROPOSAL until decided
  step_constraints: every step doable in Meadow Edge; no lantern placing, Terrarium, Parade Plaza, Reed Pond, friends, Beads or crate   # event §C
open: [the steps, the banner and Board presentation, the gate message wording and placement, edge cases]
avoid: [a new system where the Dusk Board quests can carry it; any step that rewards adding friends; scary imagery beyond the Mild label]
owns: [the play spec; the S-2 playtest read]
not_in_scope: [reward amounts (progression-designer), dates, building]
rules:
  - Returning players do not need any system added while they were away.
  - Cooperation and social steps must work without chat; Kids and Select players have chat off by default (platform-policy rules.md §D).
  - No streak loss, absence penalty or fake scarcity (G-11).
deliver: play spec with interaction acceptance criteria and edge cases; the A1 message; the S-2 reading (mechanic vs instruction, with evidence)
checks:
  - C1: the entrance is findable by a new player after the tutorial and by a returning player (state how it is tested)
  - C2: each step can be finished on a phone in Meadow Edge
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## T-M1 → marketing: known-issues message, Masquerade announcement, 1.1.1 facts

```text
<intent>
Players should hear first, plainly, that we know about the missing Beads, the lost progress and the paused crate, and only then hear about Halloween, in words that match what they will find. Here are the facts; the voice is yours; the owner publishes. Many players are young: calm words, no pressure.
</intent>
<spec>
id: T-M1 (lead assigns)
from: live-ops-designer
to: marketing
model: opus
effort: medium                                   # marketing role
skills: [marketing-design, marketing-craft, platform-policy]
refs:
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/urgent-2026-10-21.md   # take: "player message facts" rows only
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/patch-1.1.1.md   # take: the fact sheet and checks P1-P5
  - knowledge/jobs/J014-live-ops-designer/g2/live-ops/event-halloween-masquerade.md   # take: dates, eligibility, reward terms, exit statement
fixed:
  calendar:
    - known issues (U1-U3): as soon as the owner approves the facts; no fix dates
    - Masquerade: announce only after the build is in a release and passed Gate 3; live 2026-10-30 15:00 UTC to 2026-11-09 15:00 UTC   # PROPOSAL until decided
  limits: up to 10 ongoing or upcoming experience events; update announcements 60 characters, once per 3 days; personalized notifications 13+ opted in, one per user per day (FR-12..FR-16, read 2026-10-21)
  audience: label Mild; Kids (5-8) and Select (9-15) accounts can play   # game.md
open: [wording, channel choice, images]
avoid: [present tense for unbuilt scope; urgency words ("hurry", "last chance", countdowns); a Discord link inside the game; any refund promise; exploit details; player names or contact details]
owns: [announcement and known-issues drafts]
not_in_scope: [publishing (owner), dates, the crate's return date]
rules:
  - Every item has a build version and the date it is live.
  - No false scarcity or restarting timers in any copy (FR-54); calm wording for younger players (FR-57).
  - Times as UTC with a pointer to local time in the game.
  - Discord is never the only place for a fact; the in-game route carries it too.
  - Roblox Terms of Use change on 2026-11-01 (merchant of record, DF 4907620): re-read before any sales wording.
deliver: known-issues drafts (in-game, update announcement, Discord); Masquerade announcement and event-listing drafts; 1.1.1 notes in voice
checks:
  - C1: every claim maps to a fact-sheet line or an urgent-note "player message facts" row
return: hand-back to live-ops-designer, copy to lead
</spec>
```
