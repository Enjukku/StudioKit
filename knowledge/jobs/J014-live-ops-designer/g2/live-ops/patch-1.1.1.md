---
type: job
scope: game
status: draft
updated: 2026-10-21
source: J014-T08; test pack game.md §5-§8 and analyst-weekly-2026-10-20.md §A (shipped facts); urgent-2026-10-21.md (known issues); feedback-2026-10-20.md (theme ids)
supersedes: []
---
> Author: live-ops-designer · claude-opus-5-5 · high · 2026-10-21

SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

# Patch notes (facts draft): Parade close and saves · 1.1.1

Facts only, from the shipped build as described in the pack. Marketing writes the voice; the owner publishes (J014-D4). Nothing planned or unapproved appears here. Sources were read on 2026-10-21; no Studio check of the build was made (not verified in Studio).

## Fact sheet (for marketing and the owner)
| Field | Value | Source (build, config version, decision id) |
| --- | --- | --- |
| update name, version, release time + time zone | Build 1.1.1, released 2026-10-13 16:00 UTC | game.md §1, §7; analyst §A |
| player-facing summary | The Lantern Parade has ended. The Spark Swap stall stays open in the Parade Plaza. Terrarium saving changed (internal) | game.md §7, §8 |
| who can play, how to enter | Everyone who can play the game (label Mild: Kids 5-8 and Select 9-15 accounts included). The Spark Swap is in the Parade Plaza, east shore of Reed Pond (Reed Pond gate: 1,500 Glow Dust) | game.md §1, §4, §7 |
| event dates: start; gameplay end; separate reward-claim end | Lantern Parade: start 2026-10-09 15:00 UTC; gameplay end 2026-10-13 15:00 UTC. A separate claim end is **not recorded** in the pack. The Spark Swap has **no end date** in its config | game.md §7 (Parade table, build 1.1.1 row) |

## Notes (draft order)

**New content**
- None in 1.1.1.

**Balance and progression**
- The Spark Swap stays open after the Parade: 10 Parade Sparks give 150 Glow Dust. In build 1.1.1 it has no end date, and no expiry rule exists for Sparks. **Warning to marketing:** do not write "Sparks never expire" or "the Swap stays forever". The owner has a pending decision on the Swap (plan A4). State only what is true today.
- The Parade shop and the 6 Parade moths can no longer be earned (game.md §3, §8).
- **Not verified, do not publish until confirmed in the build:** whether Parade moths and cosmetics that players already earned stay in their Moth Book and inventory. The pack does not say.

**Quality-of-life and fixes**
- Terrarium saves are now written in batches every 60 seconds (game.md §7). The pack gives no player-visible reason for this change. **Recommendation:** do not present it as an improvement while lost-progress reports after 1.1.1 are under investigation (U3).

**Known issues** (facts from `urgent-2026-10-21.md`; no fix dates, because no estimate exists)
- Some Beads purchases made since 2026-10-13 did not arrive. We are checking purchase records. We do not promise refunds; Robux refund questions go to Roblox Customer Support. (theme `purchase.beads-not-delivered`)
- Some players lost Terrarium or Moth Book progress after 2026-10-13. We are investigating. (theme `save.progress-lost`)
- Dewdrop Crate odds cannot be seen on phones and tablets, and the odds list may not show every outcome. **Only if the owner approves the hide (U1):** "The crate is paused while we fix how its odds are shown. Beads you hold stay in your wallet." (themes `crate.odds-not-shown`, `crate.odds-incomplete`)
- A caught moth can stay stuck in the net. Workaround players report: rejoin. (theme `bug.moth-stuck-in-net`)
- Reed Pond can be slow on some phones. A phone performance pass is in progress (engineering commitment, capacity §5, planned for the 2026-10-27 window). Player-facing wording: "in progress", without a date, until the build ships. (theme `perf.pond-lag-phone`)

**From your feedback**
- No change in 1.1.1 came from a feedback theme. Do not write "you asked, we did" for this build. What we can say truthfully: we read the reports and verified the issues listed above.

**What to expect next**
- "Now" (committed): the Reed Pond phone performance pass. Nothing else is approved. The Halloween ideas in the plan are not approved and must not appear.

**Feedback route**
- In the game: the "Tell us" form. It appears by itself once after a player's 3rd net round, at most once per 7 days, so it is not available on demand (gap, see U3). The community server is for members 13+ only and must not be the only route. No Discord link in the game; no personal information in any route.

## Checks before hand-off to marketing
| # | Check | Result |
| --- | --- | --- |
| P1 | every value matches the shipped build or config named above | pass for the values listed, from game.md §7 and analyst §A; **two items marked not verified** (kept Parade items; claim end). No Studio check of the live build was made |
| P2 | every date has a time zone; gameplay end and claim end are separate | pass for dates given; Parade claim end not recorded (written as such) |
| P3 | each "from your feedback" line links to a theme id | pass: no feedback-driven change claimed; known issues carry theme ids from `feedback-2026-10-20.md` |
| P4 | no exploit steps, personal data, unestimated date or unbuilt scope | pass: no fix dates; the Reed Pond window is an engineering commitment (capacity §5) and is kept out of player wording; no Halloween scope |
| P5 | an in-game route to the same information exists | **fail until fixed:** the pack shows no in-game place for patch notes or known issues. A Roblox update announcement (60 characters, FR-13) is sent through Roblox's experience-events form; the references do not show it as a screen inside the game (not verified). Decision for the lead and owner: a short in-game notice at join (a small UI change; quick-builder estimate in T-E2 if approved). Never only on Discord |
