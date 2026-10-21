---
type: job
scope: game
status: draft
updated: 2026-10-21
source: J014-T08; plan-2026-10-21.md rank 1; event-halloween-masquerade.md; urgent-2026-10-21.md; live-ops-craft process.md §3
supersedes: []
---
> Author: live-ops-designer · claude-opus-5-5 · high · 2026-10-21

SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

**DRAFT, pending owner decision.** This brief becomes the contract only after the owner chooses rank 1 and the lead records the decision id. Nothing is sent.

# Update brief: "Find the way + Moth Masquerade"

| Field | Value |
| --- | --- |
| identity | decision id: pending · title: Find the way + Moth Masquerade (PROPOSAL) · version: build after 1.1.1 in the Tue 2026-10-27 15:00 UTC window (kind-level estimate, capacity §2b; scope estimate pending T-E2) · owner approval: pending · responsible lead: orchestrator (lead) |
| precondition | U1-U4 in `urgent-2026-10-21.md` go first. The feature-builder works on U2/U3 only. A2 starts only if the Thu 2026-10-29 go/no-go passes (U3's cause known and not on the reward-save path) |
| player problem | (1) Players who hold the Dust do not find the Orchard quest: 3,610 of 4,860 players with 3+ days held 6,000 Dust, 490 of them entered the Orchard; 30.5 % ever opened the Dusk Board (analyst B6, 2026-10-20; data through 10-19). (2) Players ask for a goal and non-Dust rewards (rewards.not-motivating in-game 3 / 22, discord 4 / 32, comments 5 / 60; tool output 2026-10-20). (3) New phone players stop at the first lantern: 3,210 / 6,910 (46.5 %) vs PC 88.9 % (B3); reason unknown (analyst: Low). Uncertainty: the event mechanism is unproven, and the Parade was followed by fewer returning players (B2, B5) |
| objective | Players reach the next goal (Orchard) and existing players have a reason to play over Halloween, without new harm. Why now: Halloween is Sat 2026-10-31; the owner wants that weekend (capacity §3, preference, no decision id); A1 and A3 cost little and do not depend on the date |
| hypothesis | A1: naming the Dusk Board quest at the sealed gate → players know the next step → more Beacons-chain starts among 6,000-Dust holders. A2: a reachable Halloween goal at the Dusk Board with cosmetic rewards → reason to return + the Board becomes known → existing players keep their return level after the event (no Parade-style fall). A3: build-mode events and a phone playtest → the failing sub-step → the right fix next period. Alternatives: the Orchard price, not the quest, stops players (A1 would then show no change); Halloween attention fades like the Parade (A2's guardrail shows it) |
| scope: must deliver | A1: the gate message for Old Orchard and Hollow Cave names the quest chain and the Dusk Board in the Grove (text in data, PROPOSAL). A2: the Masquerade quest chain at the Dusk Board, Halloween dyes as step rewards, start Fri 10-30 15:00 UTC, end Mon 11-09 15:00 UTC, a banner after the tutorial, all per `event-halloween-masquerade.md`. A3: the phone playtest (Studio check) and the analyst's build-mode event spec |
| scope: optional only if capacity remains | A1 in the same window as A2 (else the next window). The build-mode events (feature-builder, only after U2/U3). Music loop length (sound-designer) |
| scope: excluded | Paid items, discounts, the crate, Beads offers, new currency, Glow Dust rewards, friend-based rewards, scary content, meme audio, frog content, trading, PvP, Parade moths, tutorial changes, Spark Swap changes (A4 is a separate owner decision) |
| player journey | Entry: the banner after the tutorial, or the announcement → the Dusk Board in the Grove. First meaningful action: take the Masquerade chain and catch moths at dusk. Repeat: steps in ordinary sessions, any pace. Completion: the last dye, and a message naming "Light the three Beacons". Next core action: the Orchard path (A1) |
| new players | The banner appears only after tutorial step 4, so it does not compete with the lantern step. Steps can be done in Meadow Edge. A3 is the work for the phone players who stop earlier |
| returning players | No prerequisite: the Board is in the Grove hub. A1 tells them where the next zone starts. No penalty for days missed |
| veterans | Dyes are expression for the Terrarium. Earned dyes are kept. No Dust or power change, so their progress keeps its value |
| measurement | Proposal in plan §D; the analyst confirms or changes it before release (T-A1) |
| disable and state | The event end can be moved earlier by data (builder confirms, QA tests). Granted dyes stay. No rollback of saved state |
| communication | Facts from the live-ops fact sheet; voice by marketing; the owner publishes. Nothing is announced before the build passes Gate 3 |

## Role briefs
Draft briefs for each role are in `handoffs-draft.md`: T-E1 and T-E2 (engineering estimates, via the lead), T-A1 (analyst), T-P1 (progression-designer), T-G1 (game-designer), T-M1 (marketing), and the Studio checks the lead routes (S-1, S-2).
