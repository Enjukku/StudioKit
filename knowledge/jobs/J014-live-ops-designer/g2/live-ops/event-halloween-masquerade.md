---
type: job
scope: game
status: draft
updated: 2026-10-21
source: J014-T08; plan-2026-10-21.md rank 1 (A2); test pack (SYNTHETIC); live-ops-design events-offers-rules.md (read 2026-10-21); platform-policy references/rules.md (read 2026-10-20)
supersedes: []
---
> Author: live-ops-designer · claude-opus-5-5 · high · 2026-10-21

SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

**DRAFT, pending owner decision.** No decision id exists. Every value here is a PROPOSAL until the owner approves it.

# Event design: Moth Masquerade (Halloween) · decision id pending · v1

## A. Proposition
| Field | Value |
| --- | --- |
| player promise | "Dress your moths for Halloween: finish the Masquerade quests at the Dusk Board and keep the Halloween dyes forever." (PROPOSAL; marketing writes the final words) |
| primary goal and target cohort | A reason for **active and returning** players to play over Halloween weekend and the week after, with a reachable goal. New players join only after the tutorial |
| evidence | Players ask for a goal and non-Dust rewards: rewards.not-motivating in-game 3 / 22, discord 4 / 32, comments 5 / 60; progress.nothing-new-after-pond discord 3 / 32, comments 2 / 60 (feedback sort 2026-10-20, tool output `counts-2026-10-20-full.md`). Only 30.5 % of 3+-day players ever opened the Dusk Board (analyst B6, 2026-10-20). The Parade was liked (liked.parade discord 3 / 32, comments 4 / 60) but felt too short (event.too-short discord 1 / 32, comments 1 / 60; 28.4 % of entrants finished, B5). Owner's preference for Halloween weekend (capacity §3, no decision id). Halloween = Sat 2026-10-31 (trend page, calendar fact) |
| mechanism | A goal that every post-tutorial player can reach in ordinary sessions, placed at the Dusk Board, so players (a) have a reason to come back during the window and (b) learn where the Board is, which also holds the Orchard quest (plan A1). Rewards are expression (the Terrarium is praised), not Dust (players hold too much) |
| core-game fit | Uses the existing loop only: catch at dusk, drop in the Jar, show moths. Uses existing systems only: Dusk Board quests, moth dyes |
| trend check | Not themed on a trend. Halloween is a calendar date. The "frog chorus" meme (TS2) is **not** used: falling since its 10-12 peak, and its audio belongs to its creators |

## B. Time
| Field | Value |
| --- | --- |
| start / gameplay end / reward-claim end | **Start Fri 2026-10-30 15:00 UTC. Gameplay end Mon 2026-11-09 15:00 UTC.** No separate claim end: each dye is granted when its step completes, so nothing is left to claim after the end. The game shows each player the times in their local time zone, computed by the client, never as typed text (US clocks change on Sun 2026-11-01; Europe changed on 2026-10-25). Examples: start 15:00 London, 16:00 Berlin, 11:00 New York; end 15:00 London, 16:00 Berlin, 10:00 New York. **Fallback** if the 10-27 window is missed: release Thu 10-29, start **Sat 2026-10-31 15:00 UTC**, same end |
| length rationale | Not from a "best length" (none exists, OQ-03). The Parade ran 4 days; 28.4 % of entrants finished its track, and players with work and school said it was too short. Weekend days had the most players (Sat 10-10 7,320; Sat 10-17 2,610 vs Fri 10-16 2,260; B2). 10 days covers two weekends, so a player who misses Halloween weekend still has the next one. The end is a Monday 15:00 UTC: a working day, so the team can handle end problems (the owner does not answer at weekends, capacity §2). Release windows 11-03 and 11-05 fall inside the event for urgent fixes |
| calendar beats | Tue 10-27 15:00: build released with the event dormant (time-gated). Wed 10-28 to Thu 10-29: announcement after the build passes the owner's look (owner publishes). Thu 10-29: go/no-go (U3 save-loss cause known and not on the reward-save path). Fri 10-30 15:00: start. Sat 10-31: Halloween; no special moment. Fri 11-06: one factual in-game line with the end time (no pressure words). Mon 11-09 15:00: end; quests leave the Board. From 11-16: analyst read |
| synchronized moment | None. The Parade Plaza lagged with crowds (perf.event-plaza-lag, comments 1 / 60) and a small team should not run a live show |

## C. Play
| Field | Value |
| --- | --- |
| eligibility and entrance | Every player who has finished the tutorial (step 4, game.md §2), all devices, all regions. No PolicyService gate is needed (no paid random item, no trading). Entrance: the **Dusk Board in the Grove hub**, which needs no zone gate. Because the Board has no menu shortcut and few players open it, a small banner points to it (PROPOSAL, small UI tweak; the ui-ux-designer checks it on a phone screen, where players already find "too many menus") |
| activity loop | Board → take the Masquerade quest chain → steps that use the core loop (for example: catch moths at dusk, drop moths in the Jar, catch one moth of a named rarity) → each step grants one Halloween dye at once → the last step's message names the next goal: "Light the three Beacons" for the Orchard (links A1). Exact steps: the game-designer (T-G1). Constraints: every step can be done in Meadow Edge (Zone 1, open to all); no step needs placing a lantern (phone players struggle there, B3), the Terrarium (open save incident U3), the Parade Plaza or Reed Pond (phone lag, B9), friends or friend visits (no reward for adding friends: a social reward can create spam friend requests, FR-52), Beads or the crate |
| effort and catch-up | All steps open at the start, at any pace. No daily lock, no streak, nothing lost for a missed day. Target (PROPOSAL; the progression-designer sets step sizes from observed catch rates and checks with a trace): a player who starts on Sat 11-07 can finish by Mon 11-09 15:00 through ordinary sessions (normal session 6-12 minutes, game.md §1), including a phone player |
| rewards | Deterministic, free, cosmetic (moth dyes in Halloween colours; names PROPOSAL, e.g. "Pumpkin Glow", "Midnight Violet", "Candle Gold"), bound to the account (the game has no trading), permanent. Whether the Masquerade returns: **not decided**; we say exactly that, never "never again" |
| economy impact (progression designer) | Intent: no Glow Dust, no Beads, no event currency, so no new issuance and no left-over currency (the Parade's Sparks lesson, B8). Abuse cases to check: alt accounts and auto-clickers can only earn cosmetics for themselves (no trading). **Not yet reviewed** (T-P1) |
| monetization | None. No paid item, discount or offer in or next to the event. The Dewdrop Crate stays hidden until U1 is fixed and must not be advertised from the event |

## D. Proof and safety
| Field | Value |
| --- | --- |
| success (analyst) | Proposal (analyst decides, T-A1): existing players active in the window who play again in the 7 days after 11-09 15:00, entrants vs non-entrants, beside the Parade's read (42.0 % vs 38.1 %, B5). Exposure: started step 1. Mechanism check: Dusk Board openers and Beacons-chain starts during vs before the event. Observational: a global holiday event has no clean control |
| guardrails | Returning players on matched weekdays before vs after (the Parade: -11.5 %, -25.9 %); D1 of new players who start during the event vs other days (Parade: 14.7 % vs 19.1 %), by platform; phone FPS at the Pond (B9); Dust in/out and median held (B8); Bead sales vs grants; save-loss reports in the next feedback sort; errors |
| production (builders) | **Builder estimate requested, not received** (T-E2). Kind of work: "data or config only (quick-builder)", earliest window Tue 10-27 (capacity §2b, assumes approval on 10-21), if the Board's quests, dyes and a start/end time are data. If any part needs code, the event cannot be built for Halloween without the feature-builder, who is reserved for U2/U3: then this design is dropped, not squeezed. Reuse: Dusk Board quest data, dye data. QA: start and end times, one grant per step, dyes still there after rejoin |
| communication (marketing) | After the release passes the owner's look: one update announcement (60 characters, at most once per 3 days, FR-13, FR-14), an experience event listing with exact UTC start and end (owner creates it in Creator Hub; "Notify Me", FR-11, FR-12), one Discord post (members 13+), the in-game banner. No personalized notifications (13+ opt-in only, and no player-specific reason, FR-16). No Discord link in the game (R13). No "hurry", "last chance" or countdown pressure (R4, R6, FR-57). The in-game route (banner, Board) carries every fact, so Discord is never the only place |
| failure plan | Disable: the end time can be moved earlier by data or config (builder confirms and QA tests before launch). Dyes already granted stay (no rewind). If the save fault (U3) also hits dye grants: stop the event, and the builders re-grant from the quest progress record if one exists; the state-safe response is written by the builders before launch. Fallback activity: none needed; the core game stays as it is. Incident owner: the lead (name confirmed at go/no-go) |
| exit | At the end the quests leave the Board; unfinished steps end with no penalty. Dyes stay. The Board returns to its 3 daily quests. Statement to players: "Your Halloween dyes are yours to keep. We have not decided if the Masquerade comes back." |
| decision after the event | repeat / revise / retire / investigate with the analyst after 2026-11-16 (`process.md` §6 review in `review-<decision id>.md`) |

## E. Launch checklist (a fail in a must row blocks release)
| # | Check | Must | Result | Evidence / source + read date |
| --- | --- | --- | --- | --- |
| L1 | content and audience approved by the owner | yes | **not passed: pending decision** (blocks) | decision id pending; plan §E |
| L2 | dates and prices true everywhere | yes | pass by design; to verify at Gate 3 | Times in data as UTC; local times computed in the client; no prices. Check banner, listing, announcement and Discord text against this file. events-offers-rules.md §1 Calendar (read 2026-10-21) |
| L3 | rewards and odds shown correctly; odds total 100 %; Robux → currency → roll chain | yes | pass by design (no random reward, no paid item). The separate crate fault is U1: crate hidden until fixed | platform-policy rules.md §A (`paid-random-items.md:53-57`, read 2026-10-20); R8 (FR-35..FR-41) |
| L4 | PolicyService gates for paid random items and paid trading | yes | pass by design: not applicable (none in the event); existing crate gate unchanged | rules.md §A, §E (`PolicyService.yaml:85-149`) |
| L5 | communications allowed per channel | yes | pass by design | FR-11..FR-16, FR-18, FR-19, FR-57; R4, R6, R7, R13 (events-offers-rules.md §3-§4, read 2026-10-21) |
| L6 | ad disclosures (brand events) | if any brand | not applicable (no brand) | R10 (FR-44) |
| L7 | asset and theme rights | yes | pass by design: own assets; generic Halloween; no meme audio | trend page §3 B (2026-10-20); rules.md §H (`ip-guidelines.md:25,45-52`) |
| L8 | sensitive real-world events not used commercially | yes | pass: Halloween is a seasonal holiday; nothing is sold | R11 (FR-45) |
| L9 | maturity questionnaire still true | yes | pass by design if the look stays Mild (cute costumes and colours, no fear imagery, no gore); owner confirms at Gate 3. No new paid random, trading, chat or AI feature, so no answer changes | rules.md §D (`content-maturity.md:18-35,67-73`); game.md label "Mild" |
| L10 | data collection safe | yes | pass by design: no new data, no text input | rules.md §F |
| L11 | expiry, conversion and entitlements tested | yes | **not yet**: QA test of start, end, one grant per step, dyes kept after rejoin. Depends on U3 | needs QA evidence |
| L12 | incident responder and disable path | yes | **not yet**: name at go/no-go; disable path tested | needs QA evidence |

### E-2. Same checks for the cheaper alternative (rank 2: Halloween dye set sold for Glow Dust, 10-30 15:00 to 11-09 15:00 UTC)
| # | Result | Source |
| --- | --- | --- |
| L1 | pending decision (blocks) | plan §E |
| L2 | true end date shown in local time; prices from the progression-designer, shown from data | R1-R3 (FR-54) |
| L3, L4 | not applicable: fixed-price soft-currency items, nothing random, not bought with Robux | rules.md §A |
| L5 | no countdown pressure, no "only X left", calm "View" wording | R2-R4 (FR-54, FR-57) |
| L6-L10 | as above | as above |
| L11 | QA: purchase with Dust grants once; item kept after rejoin (depends on U3) | needs QA evidence |
| L12 | remove items from the shop by data; bought dyes stay | needs QA evidence |

Roblox Terms of Use change on 2026-11-01 (Roblox as merchant of record, DF 4907620): the event has no Robux sales wording; marketing re-reads the terms before any sales wording after that date (rules.md §H).
