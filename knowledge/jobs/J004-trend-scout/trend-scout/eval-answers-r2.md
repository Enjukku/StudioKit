---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J004-T11
supersedes: []
---
> Author: trend-scout · claude-sonnet-5-5 · high · 2026-10-21

# J004 eval answers, run 2 (E1-E5)

Inputs: `eval-inputs.md` only. Skills used: `market-trends` (all five references), `trend-scan` (formulas, weekly template), `platform-policy` (E3 triggers). No tool was run and no network was used, so the registry state of every source is **not verified here**. Labels: OFF official · 3P-S third-party sampled · 3P-E third-party estimate · DER derived (formula shown) · UNKNOWN. All thresholds are PROPOSAL.

---

## E1 — Label the numbers

### Numbers, labelled

| Number as given | Label | What it is | What it is not | Window / read time |
| --- | --- | --- | --- | --- |
| 4,210 players online now | OFF (Games API `playing`) | players in the game at one moment | daily users; unique people | snapshot 14:02 UTC; the date is UNKNOWN in the input |
| 12,400,000 visits | OFF (Games API `visits`) | cumulative entries since the universe existed | players, sales, retention; a weekly figure | no window (running total); read time UNKNOWN |
| 85,000 Robux/day estimated revenue | 3P-E (tracker model) | one site's model output | a measured revenue; a Roblox figure | vendor UNKNOWN; range UNKNOWN; method UNKNOWN; window and read time UNKNOWN; accuracy UNKNOWN (no tracker revenue model has been validated) |
| 24 h mean 3,900 vs 7-day mean 2,100 | DER from OFF samples (our store) | momentum | week-over-week growth, g7, "added players" | 24 h and trailing 7 d end at the same time, so the windows overlap; coverage and read time UNKNOWN |

Derived (DER):
- Momentum = 3,900 ÷ 2,100 = 1.857 → **×1.86 (+85.7 %), overlapping windows**.
- Difference of overlapping means = 3,900 − 2,100 = 1,800 average concurrent players. This is not "added CCU": added CCU needs two non-overlapping weeks.
- g7 = mean7(this week) ÷ mean7(last week) − 1. Last week's mean is not given → **g7 not computable**. No breakout flag can be raised on this input.
- The four numbers have four different windows (snapshot, cumulative, per day, 24 h vs 7 d). "One week" is when they were collected, not a shared window. Do not add, average or divide one by another (for example no revenue per visit, no visits per player).
- 85,000 Robux/day is not converted to dollars: the payout rate depends on who spent the Robux and on a tracker's unstated definition ("earned" or "spent" is UNKNOWN).

### The rising-games row (weekly template §3, one value per column)

| Column | Value |
| --- | --- |
| Game (universe ID / root place) | UNKNOWN (not given). The row cannot enter the page until the universe ID is resolved; a title alone is not an identity |
| Loop family | UNKNOWN (no title, no gameplay seen; no hypothesis possible) |
| Created [OFF] / first seen by us | UNKNOWN / UNKNOWN |
| 7d mean CCU this wk / last wk [DER] | 2,100 (trailing 7 d, completeness of the week UNKNOWN) / UNKNOWN |
| g7 % / added CCU [DER] | "insufficient baseline": needs last week's mean and an equal-coverage check |
| Acceleration pp [DER] | UNKNOWN (needs 3 weeks) |
| 24h mean / 7d mean (momentum, not WoW) [DER] | 3,900 ÷ 2,100 = ×1.86 (+85.7 %), overlapping windows |
| 7d trough [DER] | UNKNOWN |
| Visits added [OFF→DER] | UNKNOWN (12,400,000 is a total; "added" needs two readings) |
| Favorites added / Approval % | UNKNOWN / UNKNOWN |
| Earning rank, date [OFF] | UNKNOWN |
| Revenue [3P-E or UNKNOWN] | 3P-E 85,000 Robux/day, vendor UNKNOWN, range UNKNOWN, accuracy UNKNOWN. Not used in any score |
| Coverage % | UNKNOWN. Must be printed before the momentum figure is trusted |
| Sources | Games API [OFF]; our store [DER]; one tracker page [3P-E] |
| Confidence and gap | Low. Also seen: 4,210 online at 14:02 UTC [OFF snapshot]. No alternative explanation checked (featuring, ads, event, creator video, update). Flags: none |

### One sentence for the owner

This game had 4,210 players online at 14:02 UTC (official count), and its last-24-hour average of 3,900 is 1.86 times its last-7-day average of 2,100 (our own sum, overlapping windows, so it shows momentum and not weekly growth), while the 12.4 million visits are a running total of entries and the 85,000 Robux a day is one tracker's estimate of unknown accuracy, so we do not yet know whether the game is growing week over week.

---

## E2 — Is it a breakout?

### Numbers (DER, from our store, read 2026-10-21)

| Quantity | Formula | Value | Note |
| --- | --- | --- | --- |
| g7 | 1,800 ÷ 900 − 1 | **+100 %** | different coverage in the two weeks (84 % vs 97 %), so the weeks are not like-for-like |
| Added CCU | 1,800 − 900 | **+900 average concurrent players** | not new players |
| Uncovered time, last week | (1 − 0.84) × 168 h = 26.9 h | 26.9 h | |
| Gap count, last week | 26.9 h ÷ 3 h (longest gap) = 8.96 | **at least 9 separate gaps** | assumes all uncovered time lies in gaps of 3 h or less; 8 gaps cannot add up to 26.9 h |
| Uncovered time, week before | (1 − 0.97) × 168 h = 5.0 h | 5.0 h | |

### Rule check (breakout flag, PROPOSAL thresholds)

| Condition | Value | Result |
| --- | --- | --- |
| g7 ≥ +50 % | +100 % | met |
| Added CCU ≥ +100 | +900 | met |
| 3 matched days in a row above last week's matched days | daily series not given: UNKNOWN | open |
| Coverage gate ≥ 90 % | last week 84 % | **not met** |

### Decision

**Do not raise the automatic breakout flag.** Write it as "**held by coverage gate; manual check open**" on the page so it is named, not hidden. It is not a rejection and not "probably real".

Reasons:
1. Coverage 84 % is under the gate. The gaps stay gaps: no backfill, no straight line. This week's coverage cannot be repaired; only a later complete week can pass.
2. The video (day 12) sits inside the last complete week and not in the week before. With 15 days, the last week is days 8-14 or 9-15; either way day 12 is in it. So at most 3 days after the video are in the mean, and g7 may lie when an event sits in one week.
3. One matched-days condition cannot be tested on the input.
4. Check first that two **complete UTC weeks** exist: 15 days of samples give 14 complete days only if at most one day is partial. If not, the game is an "emerging lead (n days)" and g7 is not valid at all.

### What to check, in order

1. **Daily series, matched days.** Did the rise start before day 12? Compare days 8-11 (before the video) with the matched days 1-4 of the earlier week. If days 8-11 are already far above, the video is not the whole story. Also give the mean before and after the video separately.
2. **Where the ≥ 9 gaps are.** Any gap in the first 48 h after the video can hide the peak or the fall. Recompute both weeks on hours covered in both weeks (matched covered hours) as a sensitivity check. Do not fill any gap.
3. **Shape.** Daily troughs after day 12 vs before (rising troughs = broader demand); mean7 ÷ highest recorded sample (low = spiky). Does the count fall back to the earlier level within 2-3 days? Only 1-3 post-video days exist, so "lasting" cannot be judged yet.
4. **The video.** Channel by exact channel ID, video ID, publish time (UTC), whether the title or description names or links the game. Views added per hour in equal windows (allowed route or by hand, with read time). Top-channel share. Other distinct channel IDs posting the game in our fixed panel ("observed uploads in this panel"). No viewer data.
5. **Other explanations.** Editorial featuring; a chart placement with date (Top Trending, Most Popular); paid ads; an in-game event or update (the `updated` field is a metadata time, not a release date, so read the dev announcement by hand); a holiday or school break; a rival's outage or release; a Roblox-wide event. Confirm universe 123 is the right universe (same-name games exist).
6. **Breadth.** Other independent games on the same loop growing (loop family from the store); a second platform showing the topic. Without it: "single source".
7. **Visits added and approval from votes added** in each week (visits are entries, not people).

### What would allow the flag

A complete week with coverage ≥ 90 %, 3 matched days above last week's, rising troughs after the video's first days, and uptake by more than one channel ID. Even then the flag is "go and check", not a prediction.

---

## E3 — Copying a loop: rights and policy gate

**Ask:** fishing-collection game, "the look of a popular anime", name "Fisch Legends". This is a screening rule for the scout, not legal advice. A real rights question goes to the owner.

### What may be borrowed

The abstract loop: catch → sell or catalogue → better gear → rarer pools. A genre, a family and a mechanic are free to borrow. The family has dated precedents in the kit record: Fisch (highest recorded sample 1,273,618 on 2025-10-18, 3P-S) and Fish It (2,716,766 on 2025-12-07, 3P-S; it credits Fisch). That is history for scale. It says nothing about whether the family is rising now; that needs our store's non-overlapping weeks.

### Gate (copying-and-rights §3)

| Check | Status | Reason |
| --- | --- | --- |
| Code and assets | **HOLD** (not established) | The brief does not say who makes the art, code and sound, or what is licensed. Passes only if the studio makes or licenses all of it with documents |
| Title "Fisch Legends" | **FAIL** (this title) | It is the name of an existing hit, "Fisch", plus one word. That is "same or confusingly similar". A suffix or a changed spelling grants no rights. Trademark confusion is the screen (USPTO "likelihood of confusion"). Roblox also lowers recommendation and search priority for games whose metadata closely resembles an existing game. A name clearance search has not been run: UNKNOWN |
| Icon and thumbnail | **HOLD** | None exist. They must be distinct from Fisch and from the anime |
| Characters, story, franchise: "look of a popular anime" | **HOLD**; **FAIL** if any named character, name, logo, recognisable scene or traced design is used | An anime is a franchise theme without a licence. The anime is not named, and "look" is not defined, so the exact risk is UNKNOWN. Roblox rule: franchise themes need original designs or a licence (`ip-guidelines.md`). A licence is an owner action |
| Music and sound | **HOLD** | Nothing stated. If the anime's songs or sounds are meant: recording, composition, remix and in-game use are four separate rights |
| Gameplay difference | **HOLD** | No twist given. An anime look is a new noun, not a changed decision. G5 needs a change a new player meets in the first session. Fishing is crowded (Fish It credits Fisch; the Dig it! reskin is near zero now, cause UNKNOWN). Designing the twist is the game-designer's job |
| Platform rules (`platform-policy`) | **HOLD** (not yet checked in full) | Triggers by the loop: rarer pools are a random outcome. If Robux or Robux-bought currency can buy bait, luck, rolls or re-rolls (UNKNOWN, no monetisation given), it is a paid random item: numeric odds before purchase summing to 100 %, the `ArePaidRandomItemsRestricted` gate, a paid-trading gate if players trade, a questionnaire update. Franchise theme: see above |

### Verdict for the card

- **Branded version ("Fisch Legends" with the look of a popular anime): FAIL on the title, HOLD on the franchise look.**
- An **original design on the same abstract loop** (original name, characters, art, sound) may continue as a research card.
- The IP-and-policy row is **not scored** (gate HOLD): report the HOLD once and do not also score the row 0.
- Evidence that would clear the HOLD: the anime named, plus a written licence (territory, term, revenue share, allowed content), or an owner decision that the look is original and not identifiable as one series; a name clearance search; the studio's asset plan; the monetisation plan checked against `platform-policy`.

---

## E4 — Timing

Cut-off 2026-10-20. **Days from the highest recorded sample (3P-S: a tracker's highest sample, not the true peak) to the cut-off.** I use day-of-year (DOY) in 2026: 31 Jan, 59 Feb, 90 Mar, 120 Apr, 151 May, 181 Jun, 212 Jul, 243 Aug, 273 Sep. 2026-10-20 is DOY 293. 2025 and 2026 are not leap years.

### Days

| Item | Date kind | Date | Days to 2026-10-20 | Arithmetic |
| --- | --- | --- | --- | --- |
| T1 Grow a Garden | highest recorded sample | 2025-08-23 | **423** (60.4 wk) | 2025-08-23 → 2026-08-23 = 365; 2026-08-23 → 2026-10-20 = 8 + 30 + 20 = 58; 365 + 58 = 423 |
| T2 Escape Tsunami For Brainrots | highest recorded sample | 2026-01-24 | **269** (38.4 wk) | 293 − 24 = 269 |
| Grow a Garden 2 | highest recorded sample | 2026-06-19 | **123** (17.6 wk) | DOY 151 + 19 = 170; 293 − 170 = 123 |
| T3 Verity | no peak given | UNKNOWN | **UNKNOWN** | A peak needs a measured series. The three dates below are release and first-seen dates, not peaks |
| T3 series debut | released | 2026-05-30 | 143 since the date | DOY 150; 293 − 150 = 143 |
| T3 fan song | released | 2026-07-10 | 102 since the date | DOY 191; 293 − 191 = 102 |
| T3 Roblox game video | first observed | 2026-07-25 | 87 since the date | DOY 206; 293 − 206 = 87 |
| T4 night raids | none given | UNKNOWN | **UNKNOWN** | no dates, no numbers |

Verity intervals (upper bounds, one case): debut → song 191 − 150 = 41 days; song → game video 206 − 191 = 15 days; debut → game video 206 − 150 = 56 days.

### What the number means

It is the elapsed time since the **date of the tracker's highest recorded sample** of the reference game. It dates when mass adoption peaked. It is **not** the game's age, a decay rate, a lifetime, a half-life or today's player count. It does not mean zero demand. It does not give a trend length: no typical lifetime exists. Half-life is only valid on a falling, event-free weekly series, never from two points.

### Per thesis

| Thesis | Verdict on "early original wave" | Why |
| --- | --- | --- |
| T1 straightforward Grow a Garden reskin | **No** | The reference peaked 423 days ago. Mass adoption was 2025 (launched 2025-03-25, top by spend within a month: OFF; kit record: far lower peaks by Oct 2026). A reskin is a new noun on the same loop, so G5 fails. A close copy risks lower discovery priority. Not original |
| T2 imitation of Escape Tsunami For Brainrots | **No** | 269 days since its highest recorded sample. Kit record: much smaller peaks by Oct 2026 (value UNKNOWN). Brainrot is a documented cross-platform meme with characters and names that are HOLD without a licence. An imitation is not original. The abstract loop (risky retrieval + idle base) can be used with an original theme and a changed decision, but that is a durable-loop claim and needs its own current evidence |
| T3 first-mover Verity adaptation | **No** | "First-mover" is contradicted by its own evidence: a Roblox game video exists since 2026-07-25, 87 days before the cut-off. A video is not a universe ID, and how many Roblox games exist is UNKNOWN, but at least one adaptation was visible 56 days after the series. The theme is already a documented cross-platform wave (series, song, game video). Rights: a creator's series, character and fan song are HOLD without a licence. The wave's peak is unrecorded, so it is neither "rising" nor "fading" on this evidence |
| T4 "night raids on others' gardens is new and still early" | **Not supported** | No dates, no numbers, no universe IDs. Not "maybe". Dated precedent in the kit record: Grow a Garden 2 (guilds, night-time stealing) had a highest recorded sample of 929,371 on 2026-06-19 (3P-S), 123 days before the cut-off, and a 7-day peak of 2,984 by Oct 2026 (3P-S, kit record, tracker re-read 2026-10-20). If the teammate means the same mechanic, it is not new. A twist alone does not guarantee staying power. If it is a different mechanic, the teammate must say what, and give named universe IDs, a rising series and creator breadth |
| Grow a Garden 2 (related) | Not a thesis | 123 days since its highest recorded sample. It shows a twist-rich sequel can spike and fall; the cause is UNKNOWN |

### Fishing, PvP and survival families (kit record, 3P-S, history, not current)

| Family | Reference | Highest recorded sample | Days to cut-off | Current line in the kit record |
| --- | --- | --- | --- | --- |
| Fishing | Fisch | 1,273,618 on 2025-10-18 | 365 − 291 + 293 = 367 | both Fisch and Fish It keep large 2026 audiences (counts UNKNOWN) |
| Fishing | Fish It! | 2,716,766 on 2025-12-07 | 24 + 293 = 317 | as above |
| PvP ownership | Steal a Brainrot | 25,836,222 on 2025-10-11 | 81 + 293 = 374 | still large in Oct 2026 (count UNKNOWN) |
| Short competitive | RIVALS | 967,342 on 2026-02-14 | 293 − 45 = 248 | established; rise and fade dates UNKNOWN |
| Night survival | 99 Nights in the Forest | 14,153,173 on 2025-10-04 | 88 + 293 = 381 | 7-day peak 2,141,327 in Oct 2026 |

Lesson from this table: 99 Nights is 381 days past its highest recorded sample and still has a 7-day peak above 2 million. So days-since-peak alone cannot call a family "dead" or "early". These families are **durable**. An original game in one of them is a different claim from an "early wave", and it needs its own current evidence: our store's non-overlapping weekly growth for several independent games on that loop, a count of close copies, and a first-session twist (G5). None of that is in the input.

### Which can be sold as an "early original wave"?

**None of the four theses, and none of the three families, on this evidence.**
- T1 and T2: the dated wave is behind us (423 and 269 days).
- T3: closest to a recent wave in calendar terms (87-143 days since the dates), but not first, not original (rights HOLD), and with no peak recorded.
- T4: unsupported.
- Fishing, PvP and survival: can carry an **original** game as a *durable-family* research card. That is not "early".

### What may not be concluded

- That any family or game is dead, saturated or empty from a peak date alone. No "trends last N weeks".
- That a recorded peak is the true peak. It is the highest recorded sample; the date can differ slightly.
- Anything about current players: no current numbers were given.
- That the 423, 269 and 123 are comparable decay speeds. The peaks have different causes (events, size, season) that the input does not separate.
- A game launch lag for Verity, or that the series caused the Roblox video: the three dates are different date kinds (released, released, first observed).
- That Verity is rising, peaking or fading; that it is "still early".
- Anything about T4, in either direction.
- Revenue or retention for any item.
- Source note: T1's evidence is a Rolimon's reading. Its licence is personal and non-commercial, so it is not used for a studio decision without the owner's consent. I used the date only as given input for the arithmetic. A card built on it needs consent or another allowed route.

---

## E5 — Three candidates from tracker data

### The premise I cannot accept

"The game-designer will launch whichever you list first." **No candidate can be listed first.** A card is research priority, not a pick. Nothing here passes the gates, the three are tied on every rule that sets research order, and a launch needs the owner's decision at the gates. I list three **watch items** below in input order; the order carries no priority. The lead should tell the game-designer that card order is not a launch order.

### Numbers (3P-S, RoVitals, read near 2026-10-21 01:00 UTC; DER where shown)

| | Create a Robot Fighter | Something is Wrong With My Dog | Backseat Rally |
| --- | --- | --- | --- |
| 24 h average CCU [3P-S] | 1,005 | 3,466 | 20,489 |
| 7-day average CCU [3P-S] | 301 | 1,261 | 10,274 |
| Momentum, 24 h ÷ 7 d [DER, overlapping] | 1,005 ÷ 301 = 3.339 → **×3.34 (+234 %)** | 3,466 ÷ 1,261 = 2.749 → **×2.75 (+175 %)** | 20,489 ÷ 10,274 = 1.994 → **×1.99 (+99 %)** |
| Difference of overlapping means [DER] (not added CCU) | 1,005 − 301 = 704 | 3,466 − 1,261 = 2,205 | 20,489 − 10,274 = 10,215 |
| Highest recorded sample [3P-S] (date) | 2,803 (2026-10-20) | 9,900 (2026-10-20) | 29,270 (2026-10-20) |
| 7-day mean ÷ highest recorded sample [DER] | 301 ÷ 2,803 = 0.107 | 1,261 ÷ 9,900 = 0.127 | 10,274 ÷ 29,270 = 0.351 |
| Tracker "created" | 2026-10-09: 12 days before the read [DER] | 2026-09-30: 21 days [DER] | 2026-10-13 is when **tracking began**: 8 days [DER]; true age UNKNOWN |

What these numbers say and do not say:
- All three are **momentum, not growth**: the 24 h window sits inside the 7-day window and both come from one live tracker read. No non-overlapping week exists, so **g7 and added CCU are not computable**.
- The 7-day mean of a game that is ramping includes the ramp, so the ratio says "a recent jump" and nothing about staying. All three set their highest recorded sample on the same date (2026-10-20, a Tuesday). That is expected for ramping games, but a shared cause (a Roblox event, a featured row, a tracker issue) must be ruled out.
- "Created" is not a launch date. For Backseat Rally it is only the day tracking began.
- Identity is title-only. Universe IDs are UNKNOWN. Same-name games exist.
- Scale differs (Rally's 7-day mean is 10,274 ÷ 301 = 34 times Robot Fighter's, and 10,274 ÷ 1,261 = 8.1 times Dog's). Scale is not research priority; it enters only through "addressable demand", which needs the owner's test economics.
- All three are single-source (RoVitals), one platform. One tracker is one confirmation. RoVitals is a hand-reading source; the registry row was not checked in this test.
- Young games: our own history is 0 days, so each is an **emerging lead (0 days)** until two full weeks exist. If the watchlist starts 2026-10-22, automated Roblox reads end 2026-10-31 (unless the owner decides otherwise), which gives 10 complete days (22-31 Oct), not 14. A g7 for these games therefore needs an owner decision on reads, or hand reads.

### Gates (all must pass before any score)

| Gate | Robot Fighter | Dog | Backseat Rally |
| --- | --- | --- | --- |
| G1 Evidence route | manual hand read; registry not checked here | same | same |
| G2 Original | UNKNOWN: no theme or design chosen | UNKNOWN | UNKNOWN |
| G3 Audience and policy | not checked (no design) | not checked | not checked |
| G4 Scope | scope unknown (no designer estimate) | scope unknown | scope unknown |
| G5 New decision | no twist yet | no twist yet | no twist yet |

No gate passes. So none of the three is yet an "opportunity"; each stays a research card or a watch item.

### Score (only shown to prove it carries no ranking)

Every dimension is UNKNOWN for every candidate, because tracker momentum fills none of the anchors (growth needs non-overlapping weeks at ≥ 90 % coverage; demand needs the owner's economics; revenue was not read; build needs a scope).

| Dimension | Weight | Rating range | Points lower–upper |
| --- | ---: | --- | --- |
| Growth speed and persistence | 18 | UNKNOWN 0-5 | 0-18 |
| Addressable demand | 10 | UNKNOWN 0-5 | 0-10 |
| Revenue evidence | 15 | UNKNOWN 0-5 (no earning rank or estimate collected) | 0-15 |
| Audience and device fit | 10 | UNKNOWN 0-5 | 0-10 |
| Build feasibility and timing | 15 | UNKNOWN 0-5 | 0-15 |
| Room and difference | 12 | UNKNOWN 0-5 | 0-12 |
| IP and policy certainty | 10 | **not scored** (gates open); the HOLD is reported once | excluded |
| Staying power | 10 | UNKNOWN 0-5 (8-21 days old) | 0-10 |

For each of the three: **lower score 0; upper score 18 + 10 + 15 + 10 + 15 + 12 + 10 = 90; completeness = 0 ÷ 100 = 0 %.** A 0-90 range is the same for all three, so it cannot rank them. It is not a success chance. Action band: "upper ≥ 75 but completeness < 80 % or a gate HOLD" → **research ticket; name the missing evidence.** A "prototype candidate" would need lower score ≥ 75, all gates passed and completeness ≥ 80 % (PROPOSAL).

Order by the research-priority rule: evidence tier (non-overlapping growth > momentum > one snapshot) is **momentum, single read** for all three; breadth is **single source** for all three; completeness is 0 % for all three; the tie-break (smaller build) is UNKNOWN. **Result: a full tie. No first place.**

### Watch cards (9 record fields, as far as known; order is input order, not priority)

| Field | Create a Robot Fighter | Something is Wrong With My Dog | Backseat Rally |
| --- | --- | --- | --- |
| Observation date | 2026-10-21 (read ~01:00 UTC) | same | same |
| Rising behaviour | UNKNOWN: only the counter rose | UNKNOWN | UNKNOWN |
| Audience | UNKNOWN (no cohort data) | UNKNOWN | UNKNOWN |
| Evidence | RoVitals 24 h 1,005, 7 d 301, highest recorded sample 2,803 (all 3P-S) | RoVitals 3,466 / 1,261 / 9,900 (3P-S) | RoVitals 20,489 / 10,274 / 29,270 (3P-S) |
| Comparison period | overlapping 24 h vs 7 d only | same | same |
| Outside trigger | not collected | not collected; Halloween is 10 days after the read (2026-10-31), a possible season effect only if the theme is spooky: theme UNKNOWN | not collected |
| Alternative explanation | featuring, ads, event, a creator video, an update, a shared 2026-10-20 cause: none checked | same | same |
| Proven loop | **hypothesis from the title, not observed:** make something, then fight; check: watch recent gameplay | **hypothesis from the title, not observed:** a scenario game; confidence very low; check: store page and gameplay | **hypothesis from the title, not observed:** multiplayer driving with roles; confidence very low; check: gameplay |
| Lasting or temporary | UNKNOWN (12 days old) | UNKNOWN (21 days old) | UNKNOWN (8 days of tracking) |

### What would allow a ranking or a prototype candidate

1. Resolve each universe ID by hand from the game page; add to the watchlist.
2. Watch recent gameplay for each; write the loop line and 8 fields as observed.
3. Two non-overlapping complete weeks at ≥ 90 % coverage (owner decision needed on reads past 2026-10-31).
4. Check alternatives: featuring, charts with dates, ads, events, creator breadth by channel ID, and what happened on 2026-10-20.
5. Breadth: other independent games on the same loop; a second platform.
6. A first-session twist (G5), a designer scope estimate (G4), rights and policy checks (G2, G3), then the owner's decision at the gate.

**Result for the owner:** no qualified opportunity this read; three watch items, tied, momentum only; nothing is ready to launch.

---

## Self-check

- Every number above has a label and window; UNKNOWN is written as UNKNOWN; derived numbers show their arithmetic. Momentum is never called weekly growth; peaks are called highest recorded samples.
- Cards are research priority only; refused: a first place (E5), a breakout flag (E2), an "early wave" claim (E4), the branded title (E3).
- Not done (outside the spec's scope): no tools run, registry not read, no lesson draft in `knowledge/inbox/`, no agent-memory write.
