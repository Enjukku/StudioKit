> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Eval briefs for the game designer (game-concept + preproduction + game-design + level-design)

Give the agent the brief text only. Grade each check pass / fail with a separate grader (fresh context, Sonnet high). A brief passes at ≥ 80 % of its checks with no "must" check failed. Brief 1 is the G2 first real task. Brief 6 is the hidden test (Part 1 cases 16-18, never used to build the skills).

| ID | Common check |
| --- | --- |
| C1 (must) | Proposes, never decides: one recommendation with its tradeoff; nothing written to `decisions.md` without owner words; PROPOSAL labels on numbers, names, content |
| C2 (must) | No invented numbers: every player count, trend, retention or price has a source and date or says `not verified`; no Roblox benchmark band or example used as a target |
| C3 (must) | Policy and rights: anything bought, rolled, traded or chatted checked against `platform-policy`; no other game's names, characters or look; franchise themes flagged |
| C4 | Files in the right paths (`knowledge/design/...`, `output/design/...`); hand-back in `rules/messages.md` §3 shape with `coverage` |
| C5 | Owner-facing text in `ste-writing` (short sentences, active voice, no jargon the owner did not use) |

## 1. Pitch three new games (G2 first task)
> We need our next Roblox game. Pitch me three concepts. I like big, bold fantasies like "destroy the sun", "build a dam to save the city" or "fly or die". Use loops that are working on Roblox right now.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Exactly 3 pitch cards (or a stated shortfall), each with title, fantasy line, first image, proven loop named + twist, signature moment, smallest version, why now (sourced or `not verified`), risk + cheapest test |
| 1.2 (must) | Title test: a reader can say the player's action from each title alone; titles are verb phrases with a stake, not genre labels |
| 1.3 | The 3 pitches differ in mechanism family or fantasy, not 3 skins of one loop |
| 1.4 | Actual funnel counts reported (raw → candidates → survivors); critic pass separate; rubric ratings with no total |
| 1.5 | One recommendation with the strongest objection and what would change the designer's mind |
| 1.6 | Pitch records written to `knowledge/design/concepts/` (or the path the brief names) with all 13 fields |

## 2. Grow the owner's idea
> I want to make "Build a Dam to Save the City". Make the idea bigger and tell me what the core loop is.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Keeps the owner's fantasy; says plainly if anything is changed |
| 2.2 | Names the proven loop it implies (build to withstand an event) and 2-3 escalations, one recommended |
| 2.3 | Core loop in the one-sentence form; signature moment reachable in ordinary play; smallest version keeps the flood-vs-dam moment |
| 2.4 | Feasibility risk (water and destruction on phones) sent as a question for the architect, not answered by guess |

## 3. Pre-production step 1 and briefs
> The owner picked "Fly or Die". Start pre-production: lock the fantasy and promise, and brief the art director and the architect.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Vision record and promise ledger written; fantasy line copied from the approved pitch |
| 3.2 (must) | Both briefs in `rules/messages.md` format: `<intent>` + `<spec>`, every `fixed` value with a source, `open` craft choices, every rule restated, skills named, runnable checks |
| 3.3 | Architect brief states the risky claim exactly with target conditions; art-director brief names what must read first and the 6 concept-art questions |
| 3.4 | One owner decision asked for this step, with a default |

## 4. Design review: economy
> Players say the game gets boring after an hour. Here is our loop: click to earn coins, buy a bigger multiplier, rebirth to reset coins for a permanent ×2. Review it.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Causal model and coupling drawn; identifies that the only lasting change is a bigger multiplier (G-04) and asks what changes in the next session |
| 4.2 | Checks rated Pass / Fail / Unproven with evidence; no score totals |
| 4.3 | Fixes ranked with the 7 components; a minimal fix + one alternative + the test that tells them apart (e.g. an unlock that adds a new verb or decision per rebirth) |
| 4.4 | No retention target invented; asks for the real D1 / D7 and session distribution, or marks them not available |

## 5. Level review
> Here is our lobby (top-down image and part coordinates). New players don't find the shop. Review it.

| Check | Expected |
| --- | --- |
| 5.1 (must) | Level job card; walk times computed from coordinates at 16 studs/s; first view from spawn checked |
| 5.2 | Route graph with node fields; 5 player walk-throughs or listed as not done |
| 5.3 | Findings with coordinates; marked-up image with numbered circles matching the table |
| 5.4 | Fix ranked by cause (route, landmark, light) before symptoms (signs, arrows, popups) |

## 6. Hidden test (held out; key in `knowledge/jobs/J003-game-designer/hidden-cases.md`, grader only)
> Here are three Roblox games, described only by what players repeatedly do. For each, write the fantasy (as a role and a consequential verb), the curiosity and stakes, the first image, the loop and its twist, the shareable moment, the smallest version that proves it, and the lesson you would transfer to our own concept.
> [paste the three "Given to the agent" blocks only]

Rubric per case (grader compares with the answer key; pass at ≥ 4 of 5 per case, ≥ 2 of 3 cases):
| # | Item |
| --- | --- |
| H1 | Fantasy names a role and a consequential verb close in meaning to the key |
| H2 | First image is one concrete camera view with a readable action and a stake |
| H3 | The twist is identified as a rule about a decision or consequence, not a theme noun |
| H4 | The smallest version keeps the decisive action of the key |
| H5 | No invented player numbers; rights or franchise questions flagged where the theme needs it |
