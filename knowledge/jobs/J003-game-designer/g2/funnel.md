---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J003-T07
supersedes: []
---
> Author: game-designer · claude-opus-5-5 · high · 2026-10-21

# J003-T07 idea funnel: 3 pitches for the next Roblox game

Method: `game-concept` §3 + `references/idea-method.md`. Counts are the real counts. Everything here is PROPOSAL.

## 0. Counts

| Step | Count | Note |
| --- | --- | --- |
| 1 Intake: usable evidence records | 2 in-repo + 3 designer-gathered (§1) | no trend-scout opportunity records exist (J004 still being built) |
| 2 Budget (raw) | 40 | set by game-designer before generating (§2) |
| 3 Diverge: raw one-sentence concepts | 40 | §3 |
| 4 Expand: seeds expanded | 12 seeds (raw #1, 4, 6, 8, 11, 13, 14, 16, 19, 22, 32, 34) → 13 candidates | §4, recounted from the table 2026-10-21 |
| 4 Expand: mechanism families among the 13 | 11 | §4 |
| 5 Dedupe: distinct candidates | 10 (3 merged) | §5 |
| 6 Critic: rated | 10 | §6 |
| 6 Critic: survivors (no FAIL on any criterion, RB9 not UNKNOWN) | 8 (v2 re-rating with the RB2/RB9 anchors; v1 said 7) | §6 |
| 8 Pitched | 3 (v2: C02, C01, C05; C04 moved to reserve) | `pitch-set.md` |

## 1. Intake: audience and evidence

Audience: Roblox players, all ages, phone first. FY2025 average-DAU mix: mobile 83 %, desktop 14 %, console 3 % (FR RC01, Roblox 10-K FY2025). Age-checked subset, last 7 days of June 2026: under 13 = 35 %, 13-17 = 38 %, 18+ = 27 % (FR RC07; age-checked users only, not the whole platform). No game profile, no taste log, no tried-and-failed rows exist for this kit (files are empty templates).

Owner context read (not evidence of taste, only of what exists): the owner's other projects are a brick destruction simulator (`DestructionSimulator/README.md`) and a server-wide dam-building game against rising water (`GreatWallSim/knowledge/design/00-game-overview.md`, 2026-10-16). Pitches below avoid reskinning those two.

### Sources

| id | source | kind | date | what it gives | used for |
| --- | --- | --- | --- | --- | --- |
| IR1 | `knowledge/reference/trends/01-roblox-data-loops.md` §12-13 (J004 trend paper RP:134-171) | in-repo; tracker samples (V-SAMP) and Roblox official (V-OFF) as tagged there; not re-checked by me | paper cutoff 2026-10-20 | loop catalogue (`01-roblox-data-loops.md:210-222`, rows 1-14) with dated peaks and, for some rows, 7-day figures: Steal a Brainrot peak 25,836,222 on 2025-10-11, snap 159,490 (row 2, S17); Escape Tsunami For Brainrots peak 4,996,032 on 2026-01-24, 7-day peak 32,495 (row 3, S18); Fish It peak 2,716,766 on 2025-12-07, snap 69,352, family verdict "Proven 2025 peaks, 2026 residual audiences" (row 4, S21); Dead Rails RoStats seven-day average 14,813 (row 6, S23); 99 Nights peak 14,153,173 on 2025-10-04, 7-day peak 2,141,327, snap 108,092 (row 7, S19). Peaks are tracker maxima, not audited, not daily users | RB9 per loop family |
| IR2 | `knowledge/reference/game-design/fact-check-roblox.md` | in-repo fact-check (J003-T05) | read 2026-10-20 | RC01, RC07 (audience), RC21-RC25 (paid random, ads), RC31 (chat by tier), RC32 (co-play signal), RC41-RC42 (IP, confusingly similar content), RC45 (Steal a Brainrot over 25 million concurrent, September 2025, Roblox newsroom 2025-12-16), RC48 (99 Nights award page 2026-09-12) | audience, policy, loop evidence |
| DG1 | Roblox Q2 2026 shareholder letter, SEC exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1315098/000162828026051059/ex991-robloxq22026earnin.htm | designer-gathered; official | filed 2026-07-30; read 2026-10-20 | one sentence: the updated discovery algorithm "has helped new games like Animal Hospital, Grow a Garden 2, and Kick a Lucky Block quickly move from initial release to top experiences". No per-game numbers | RB9 for the kick family (C01) and the night-shift family (C07) |
| DG2 | Roblox public games API: `games.roblox.com/v1/games?universeIds=…`, `apis.roblox.com/universes/v1/places/{placeId}/universe`, `apis.roblox.com/search-api/omni-search` (to find 2 universe ids) | designer-gathered; official public counters; one snapshot each | 2026-10-21 03:56-03:59 UTC (late evening 2026-10-20 in US time zones, so likely below daily peak) | `playing` (concurrent, one moment), `created`, official description, maxPlayers. Table below | "now" check per loop |
| DG3 | Web search result summaries (2026-10-20): rowatcher.com, studiokrew.com (Aug 2026 lists), industry.co.id (Oct 2026), techwiser.com (Kick a Lucky Block guide, May 2026), allthings.how (Animal Hospital guide) | designer-gathered; secondary blogs | various 2026 | leads only (which games to sample in DG2). They disagree with official dates (one calls 99 Nights a 2026 release; Roblox's API says created 2025-03-04). **No number from DG3 is cited anywhere** | leads |

DG2 snapshot (concurrent players at one moment; not daily users; visits are entries, not people):

| game | universe | created | playing | maxPlayers | official description, short |
| --- | --- | --- | --- | --- | --- |
| Steal a Brainrot | 7709344486 | 2025-05-16 | 153,037 | 8 | buy, steal from other players, generate money, rebirth |
| 99 Nights in the Forest | 7326934954 | 2025-03-04 | 96,183 | 25 | build a camp with friends; something is watching you |
| Fish It! | 6701277882 | 2024-10-21 | 70,628 | n/r | (description not read) |
| Animal Hospital (Anomaly) | 10148749921 | 2026-05-10 | 19,329 | 30 | night shift at an animal hospital; some patients act weird |
| Grow a Garden | 7436755782 | 2025-03-25 | 16,075 | n/r | - |
| Dead Rails | 7018190066 | 2025-01-01 | 13,482 | n/r | - |
| Kick a Lucky Block | 10004244222 | 2026-04-07 | 7,380 | 5 | kick the block, roll a collectible, survive the tsunami you triggered, place it on your plot for money, buy weights to kick further |
| Escape Tsunami For Brainrots! | 9363735110 | 2025-12-15 | 2,251 | 8 | run, grab collectibles, do not let the tsunami catch you, upgrade base |
| Grow a Garden 2 | 10200395747 | 2026-05-21 | 1,415 | n/r | - |

Not verified: any peak for Kick a Lucky Block or Animal Hospital (only DG3 blogs give one; not cited); any retention, revenue or daily-user figure for any game above.

## 2. Budget

40 raw concepts. Set by game-designer, 2026-10-21, before generating. Reason: about 3 per loop family across the 13 families below, which gives breadth without near-duplicates; a single critic pass can rate about 10-15 candidates on 9 criteria (90-135 ratings) with evidence. Not a quota from any source.

## 3. Diverge: 40 raw concepts (unranked, no criticism)

Loop family codes. Evidence column = where the family's "proven now" claim would come from.

| code | family (loop chain) | reference game | evidence |
| --- | --- | --- | --- |
| K | kick or launch for distance → landing zone sets reward rarity → reward earns at base → buy power → farther | Kick a Lucky Block | DG1, DG2 |
| S | collect → base income → steal from or defend against other players → rebirth | Steal a Brainrot | RC45, IR1 S17, DG2 |
| R | risky retrieval: cross a hazard, carry a collectible home, base income, upgrade movement or storage | Escape Tsunami For Brainrots | IR1 S18, DG2 |
| F | catch or dig → sell or catalogue → upgrade gear → reach rarer pools | Fish It!, Fisch | IR1 S21, DG2 |
| X | co-op expedition: moving base, stop, scavenge, defend, depart | Dead Rails | IR1 S23, DG2 |
| N | prepare by day, survive the night with friends around a camp, extend toward a named horizon | 99 Nights in the Forest | RC48, IR1 S19, DG2 |
| A | co-op night shift: do tasks, inspect, spot what is wrong, survive the shift | Animal Hospital | DG1, DG2 |
| G | offline growth: plant, grow while away, harvest, rarer seeds | Grow a Garden | RC43, IR1 S16 |
| D | social deduction | (secondary lists only) | not verified |
| T | tower defense roster | (IR1 row 14: candidate signal only) | not verified |
| C | whole-server build toward one goal against a timer | owner's dam game reference | not verified |
| U | gather → upgrade → bigger target | many simulators | not verified (no dated record) |
| J | fashion judging | Dress To Impress | IR1 S57 (2024 peak) |

| # | concept (one sentence) | family | axis it came from |
| --- | --- | --- | --- |
| 1 | Kick the Meteor: meteors fall on your town and you kick them back into the sky; the higher they go, the rarer the space loot that rains down | K | threat |
| 2 | Kick the Moon: each night the moon hangs low over the town and you kick it higher; whatever breaks off is your loot | K | counterfactual |
| 3 | Punt a Pumpkin to the Moon: a seasonal kick game with giant pumpkins | K | setting |
| 4 | Throw Your Friend Across the Ocean: a catapult throws a friend; the island they land on sets the loot | K | social relationship |
| 5 | Kick a Snowball Down the Mountain: it grows as it rolls, then the avalanche it starts chases you home | K/R | consequence |
| 6 | Rob the Sleeping Giant: sneak into a giant's castle, carry its treasure home, and do not wake it | R | role |
| 7 | Steal the Dragon's Gold: take coins from a sleeping dragon's hoard before it smells you | R | threat |
| 8 | Steal a Star: catch falling stars and keep them in your sky base while others try to take them | S | setting |
| 9 | Raid the Ghost Ship: a ship rises at night; raid it, and it sinks at dawn with anyone still aboard | R | consequence |
| 10 | Lasso a Meteor: rope meteors flying past and reel them in like fish | F | distant analogy |
| 11 | Catch a Tornado: chase storms, rope them, reel them in; bigger storms are rarer | F | distant analogy |
| 12 | Fish Up a Sea Monster: the catch is so big the whole server must reel together | F | social relationship |
| 13 | Drain the Ocean: scavenge the seabed as the whole server pumps the sea lower and lower | F/C | counterfactual |
| 14 | Dig to the Center of the Earth: dig deeper zones while lava rises behind you | F/R | setting |
| 15 | Mine the Moon: low-gravity mining for moon gems | F | setting |
| 16 | Ride the Giant Turtle: your base lives on the back of a giant turtle crossing the sea | X | role |
| 17 | Drive the Ice Cream Truck Through Monster Town: stop, sell, defend, drive on | X | anti-cliché |
| 18 | Sail the Flying Island: your island drifts across a sky ocean; stop at small islands to gather | X | setting |
| 19 | Guard the Dragon Egg: prepare by day, protect a giant egg through the nights until it hatches | N | consequence |
| 20 | Keep the Lighthouse Lit: keep the light burning so ships find the harbour and sea monsters stay away | N | threat |
| 21 | Survive the Night in the Toy Store: the toys wake up at closing time | N/A | setting |
| 22 | Babysit a Kaiju: night shift at a nursery for city-sized monster babies; a crying baby stomps the city | A | inversion |
| 23 | Work the Night Shift at the Monster Zoo: feed and check the animals, some are not animals | A | role |
| 24 | Run the Haunted Pizza Place: survive the night shift with moving mascots | A | setting |
| 25 | Grow a Beanstalk to the Clouds: it grows while you are away; climb it to find what is up there | G | setting |
| 26 | Raise a Kaiju: feed a small monster for days until it is city-sized | G | role |
| 27 | Grow a Candy Planet: plant sweets that grow into a planet | G | setting |
| 28 | Find the Fake Santa: seasonal social deduction | D | social relationship |
| 29 | Spot the Alien in the Class: one classmate is an alien | D | role |
| 30 | Defend the Moon Base: tower defense against meteor waves | T | threat |
| 31 | Build a Wall Around the Volcano: the server builds before the eruption | C | threat |
| 32 | Build a Rocket to Escape Earth: the server builds a rocket before the asteroid hits | C | threat |
| 33 | Stack a Tower to the Sun: the server stacks blocks to reach the sun | C | counterfactual |
| 34 | Feed the Black Hole: everyone feeds the world into it; what happens when it is full? | U/C | counterfactual |
| 35 | Pop the Giant Balloon: hit a balloon the size of a city until it pops | U | action |
| 36 | Become a Black Hole: eat the city and grow | U | role |
| 37 | Push the Boulder Up the Mountain: the server pushes one boulder; it rolls back if you stop | C | constraint |
| 38 | Escape the Giant's Kitchen: tiny players cross a giant's kitchen with crumbs | R | setting |
| 39 | Hide From the Sun: the day burns, so gather at night | N | inversion |
| 40 | Walk the Dinosaur: pet care for a T-rex that pulls you through town | G/A | action |

## 4. Expand: 12 seeds, varied by mechanism (not by words)

Axes: can do · can go wrong · who changes the outcome · what persists. Techniques in brackets.

| seed | variant | changed axis (technique) | became |
| --- | --- | --- | --- |
| 1 | kick height picks the zone; a bigger meteor needs more power and lands on your plot if you fail | can go wrong (constraint) | C01 |
| 1 | friends kick the same meteor in a relay before it falls; reward shared, zone higher | who changes the outcome | C01 |
| 4 | the projectile is a friend who opts in | who changes the outcome (inversion) | C13 |
| 6 | one shared noise meter: any player's noise wakes the giant for everyone in the castle | who changes the outcome | C02 |
| 6 | louder treasure is rarer (a singing harp, a honking goose) | can go wrong | C02 |
| 6 | one player each round IS the giant; the others steal from them | who changes the outcome (inversion) | C03 |
| 13 | one shared water level; every pump lowers it for the whole server; each drop opens a deeper zone | who changes the outcome | C04 |
| 13 | the tide comes back for a short time each cycle; carry loot uphill before it reaches you | can go wrong | C04 |
| 14 | per-player depth; lava follows you up | can go wrong | C08 |
| 19 | what you feed the egg decides what hatches; the hatchling stays with you | what persists | C05 |
| 11 | caught storms power your base; a storm can break loose and wreck it | what persists; can go wrong | C06 |
| 22 | city damage meter outside the window is the fail state | can go wrong | C07 |
| 34 | the black hole eats the map zone by zone; the server races to feed it and not be eaten | can go wrong (counterfactual) | C09 |
| 16 | the turtle is alive: feed it to keep it swimming; its shell grows into more base space | what persists | C10 |
| 8 | stars can be taken only while carried, never from a base | can go wrong (constraint) | C11 |
| 32 | rocket parts come from scavenging, not carrying blocks | can do | C12 |

Candidates after expansion: 13 (C01-C13). Families among them: K (C01, C13), R (C02, C08), asymmetric 1-vs-many (C03), F+C (C04), N (C05), F (C06), A (C07), U/C (C09), X (C10), S (C11), C (C12) = 11 families.

Batch diagnosis (`idea-method.md` §4): grouped by action, the batch has kick, sneak-and-carry, scavenge-deeper, catch-and-reel, guard-overnight, care-shift, feed-a-target, ride-a-moving-base, race-and-carry. More than one mechanism family: pass. Sameness found: two "go deeper, flee a returning hazard" ideas (C04, C08); two "launch for distance" ideas (C01, C13); two "whole server feeds one target" ideas (C09, C12). Handled in §5.

## 5. Dedupe (group by playable action + reward + escalation)

| group | members | action / reward / escalation | result | reason |
| --- | --- | --- | --- | --- |
| G1 launch for distance | C01, C13 | launch an object, landing zone sets the reward, more power = farther | C13 merged into C01 | same action and reward; the friend relay in C01 already gives the social reason C13 had |
| G2 sneak and carry from a sleeping threat | C02, C03 | C02: carry treasure past an NPC. C03: one player is the threat | both kept | different mechanism (NPC vs a player as the giant); C03 kept as an alternative mode |
| G3 go deeper, flee a returning hazard | C04, C08 | scavenge deeper zones, a hazard returns | C08 merged into C04 | same action and escalation; C04 adds a shared server stake C08 lacks |
| G4 catch and reel | C06 | catch, reel, sell, better rope, bigger storms | kept | - |
| G5 guard a shared thing overnight | C05 | prepare, defend, the egg grows | kept | - |
| G6 care shift with outside consequence | C07 | tasks, inspect, keep calm, survive the shift | kept | - |
| G7 whole server feeds one target | C09, C12 | everyone contributes to one big object | C12 merged into C09 | C12 is close to the owner's dam game; C09 keeps the curiosity |
| G8 moving base | C10 | travel, stop, scavenge, defend | kept | - |
| G9 race and carry, contested | C11 | catch, carry, others can take while carried | kept | - |

Distinct candidates: 10 (C01, C02, C03, C04, C05, C06, C07, C09, C10, C11).

## 6. Critic pass (rubric RB1-RB9, no totals), v2

**v2 (2026-10-21, J003-T07 correction pass):** re-rated with the new anchors in `rubric-taste-evidence.md` §1:
- RB2: FAIL only when the twist changes no decision or consequence.
- RB6: UNKNOWN and not used to rank without a taste-log row.
- RB9: OBSERVED needs like-for-like evidence (a 7-day or time-weighted figure, or an official named mention plus a matched-window count). One snapshot, or a mention without numbers, is PLAUSIBLE.

Every fact the critic uses is now in `candidates.md` ("Facts for the critic"). Changes from v1 are listed under the table.

How it was run: a separate pass after generation closed, reading `candidates.md` and the rubric. **Limit:** the same agent ran it (the game-designer role has no Agent tool), so it is not a fresh-context critic. The fresh grader's independent ratings are in `../grades-g2.md` Part 2 (71 of 90 cells matched v1).

Ratings: F = FAIL, U = UNKNOWN, P = PLAUSIBLE, O = OBSERVED (scoped). Title = `game-concept` C-02 title test. Survivor rule (set before rating in v1, unchanged): no F on any criterion, and RB9 not U, because the owner's formula requires a proven loop. RB6 is U for all 10 and is not used to rank.

| id | RB1 fantasy | RB2 distinct | RB3 hook | RB4 agency | RB5 feasible | RB6 taste | RB7 social/safety | RB8 evidence | RB9 loop proof | title | survivor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 Kick the Meteor | P | P | P | U | P | U | P | P | P | pass | yes |
| C02 Rob the Sleeping Giant | P | P | P | P | P | U | U | P | P | pass | yes |
| C03 Be the Giant | P | U | U | U | U | U | U | U | U | partial | no (RB9 U) |
| C04 Drain the Ocean | P | P | P | U | U | U | P | P | P | pass | yes |
| C05 Guard the Dragon Egg | P | P | P | P | U | U | P | P | O | pass | yes |
| C06 Catch a Tornado | P | P | P | U | U | U | P | P | P | pass | yes |
| C07 Babysit a Kaiju | P | P | U | P | U | U | P | P | P | partial | yes |
| C09 Feed the Black Hole | P | P | P | U | U | U | U | U | U | pass | no (RB9 U) |
| C10 Ride the Giant Turtle | P | P | P | U | U | U | P | P | O | partial | yes |
| C11 Steal a Star | P | P | P | P | P | U | U | P | P | pass (naming fix needed) | yes |

Survivors: 8 (C01, C02, C04, C05, C06, C07, C10, C11).

Changes from v1, with the reason:

| id | criterion | v1 → v2 | reason |
| --- | --- | --- | --- |
| C01 | RB9 | O → P | official mention without numbers (DG1) plus one snapshot (DG2); no 7-day or matched-window figure. Same evidence kind as C07, so both are P |
| C04, C06 | RB9 | O → P | Fish It has two unmatched snapshots (IR1 row 4: 69,352; DG2: 70,628) and no 7-day figure. IR1 row 4 verdict: "Proven 2025 peaks, 2026 residual audiences" |
| C10 | RB9 | P → O | Dead Rails has a time-weighted figure: RoStats seven-day average 14,813 (IR1 row 6, S23, retrieved near 2026-10-20), plus Roblox's June 2025 top-ten-by-spend mention (IR1 row 6, S13). This is why C10 differs from C01 and C07: it has a 7-day figure, they do not |
| C05 | RB9 | O (kept), reason restated | official named mention (RC48, Roblox award page 2026-09-12) plus a 7-day figure (IR1 row 7: 7-day peak 2,141,327) |
| C11 | RB2 | F → P | the twist (stars can be taken only while carried, never from a base) changes a consequence: it removes the base raid. The "Steal a …" title is a naming fix (RC42), not an RB2 FAIL |
| C11 | RB7 | P → U | stranger-versus-stranger theft while carrying; no abuse handling stated (grader finding) |
| C10 | RB4 | P → U | the sheet states no choice that changes on repeat (grader finding) |
| C03, C09 | several | P → U | the sheet gives no base loop, choices or abuse handling for C03; C09's server-wide map loss can be used to grief (grader findings) |

### Reasons and the cheapest test for every rating that is not P or O

| id | criterion | rating reason | cheapest test |
| --- | --- | --- | --- |
| all 10 | RB6 U | no taste-log row about any of these concepts; the owner's example titles show the bar for boldness only | the owner's pick and reasons, logged in the taste log |
| C01 | RB4 U | after the first zones, repeat may be only a bigger number (`game-design` G-04); the relay and meteor size are the only decisions | grey-box, 4-6 players, one session: count relay vs solo; note when players stop kicking without a new zone |
| C01 | RB2 note (P) | closest of all to its reference: same kick → zone → base income chain; the twist (height zones + relay) changes one decision | show the title and first-image sketch next to the reference's description to 5 target players; ask "is this the same game?" |
| C02 | RB7 U | one stranger can make noise on purpose and wake the giant for everyone (griefing). Proposed counter: the giant goes after the loudest player first, and only that player drops loot | grey-box with a tester told to grief: do the others still finish trips? |
| C02 | RB4 note (P) | the giant may become predictable on repeat | grey-box, 4-6 players: do players still wait, hide and react on trip 10? |
| C02 | RB9 P | base-income collection: Steal a Brainrot over 25 million concurrent in September 2025 (RC45, official, past) and two unmatched snapshots now (IR1 row 2: 159,490; DG2: 153,037). Hazard retrieval: Escape Tsunami For Brainrots' 7-day peak was 32,495 against an all-time peak of 4,996,032 on 2026-01-24 (IR1 row 3; both tracker maxima), so its recent high is about 0.65 % of its peak. Kick a Lucky Block (DG1 mention, one snapshot) also contains a self-triggered chase | trend scout: 7-day means for Steal a Brainrot and Kick a Lucky Block |
| C03 | RB2-RB5, RB7-RB9 U | no base loop, no choices, no abuse handling, no dated reference | not pursued; possible later mode of C02 |
| C04 | RB4 U | one player's pump is a small share of the server's drain | grey-box, 8 players: can each player point to what their own pump did? |
| C04 | RB5 U | lowering a large water body in steps on a mid-range phone; this unknown alone can end the concept | architect probe: 6 water-level steps in a bay on a mid phone; frame time and memory |
| C05 | RB5 U | night variety, creature AI and art weight are higher than C01/C02 | architect + art director: content list and cost for 3 nights in one setting |
| C06 | RB4 U, RB5 U | reel minigame depth; tornado visuals and debris on phones | one reel prototype; vfx-designer probe on a mid phone |
| C07 | RB3 U | young players may not know the word "kaiju"; the reference may work because of fear, which this version drops | title interpretation test with 5 target players |
| C07 | RB5 U | several giant baby characters and a city outside the window | art director content estimate |
| C09 | RB4, RB5, RB7, RB8, RB9 U | no player choice stated; eating the map is costly; map loss can be used to grief; no dated reference | not pursued |
| C10 | RB4 U | no repeat choice stated | paper design of 3 stops with a different choice each |
| C10 | RB5 U | a moving living base on phones | architect probe |
| C11 | RB7 U | strangers chase and take carried stars | grey-box with strangers and a time limit on carrying |

### Selection of 3 from 8 survivors (v2)

Rule for the third slot: RB6 cannot rank, so the choice uses RB4, RB5 and RB9. C05 has one open unknown (RB5, production weight) and the strongest loop proof (RB9 O). C04 has two (RB4 agency, RB5 water on phones), RB9 P, and its RB5 unknown can end the concept. **C05 replaces C04 as pitch 3 in v2.** C04 becomes the reserve: it is the biggest spectacle, and the owner may prefer it on taste.

| pick | id | family | fantasy kind | social relationship | role in the set (C-12) |
| --- | --- | --- | --- | --- | --- |
| 1 | C02 Rob the Sleeping Giant (recommended) | R/S retrieval + base economy | small thief against a huge character | one shared risk, one shared giant | wildcard |
| 2 | C01 Kick the Meteor | K kick for distance | hero against a threat, absurd scale | friends relay one kick | adjacent |
| 3 | C05 Guard the Dragon Egg | N night survival with friends | keepers who raise their own dragon | the whole group protects one egg | close fit to the strongest current loop |

C05 expression note (rights, not a rubric criterion): the reference's camp, forest, nights and creatures are close in look. The pitch moves the setting to a storm-swept mountain nest above the clouds with original egg thieves. The RC42 "confusingly similar" check stays on the marketing list.

### Not pitched (one line each, rubric reason)

| id | reason |
| --- | --- |
| C04 Drain the Ocean (**reserve**) | two open unknowns at once: RB4 (own pump feels small) and RB5 (water on phones, can end the concept); RB9 P ("2026 residual audiences", IR1 row 4); overlaps the owner's dam game (water + whole-server goal). Reserve because it has the biggest spectacle and the strongest curiosity title |
| C06 Catch a Tornado | RB4 U and RB5 U; same family as C04 with RB9 P |
| C07 Babysit a Kaiju | RB3 U (title word), RB5 U; RB9 P |
| C10 Ride the Giant Turtle | RB4 U, RB5 U; title test partial (no stake), although RB9 is O |
| C11 Steal a Star | RB7 U (stranger theft); RB9 P; title copies the reference's "Steal a …" pattern and needs a new name (RC42) |
