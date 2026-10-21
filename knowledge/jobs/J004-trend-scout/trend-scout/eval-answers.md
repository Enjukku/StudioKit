---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J004-T09
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: trend-scout · claude-sonnet-5-5 · high · 2026-10-21

# J004-T09 eval answers (trend-scout, five cases)

Skills used: `market-trends` (+ `signals-and-metrics`, `opportunities`, `copying-and-rights`, `loops`, `outside-trends` references), `trend-scan` (+ `formulas`). Inputs only from `eval-inputs.md`. No web, no tools run. Labels: OFF, 3P-S, 3P-E, DEV, DER, MAN, UNKNOWN. All thresholds named here are PROPOSAL values from the skills.

---

## E1 — Label the numbers

### Labelled inputs
| Input | Value | Label | Window / read time | What it is | What it is not |
| --- | --- | --- | --- | --- | --- |
| Players online | 4,210 | OFF (Games API `playing`) | one snapshot, 14:02 UTC; date not given (UNKNOWN, "one week") | players online at that moment | daily users, unique people |
| Visits | 12,400,000 | OFF (Games API `visits`) | cumulative since creation; read time not given (UNKNOWN) | total entries | players, sales, retention |
| Revenue | 85,000 Robux/day | 3P-E (tracker; name UNKNOWN) | window UNKNOWN; range UNKNOWN; method UNKNOWN; accuracy UNKNOWN | a model output | a fact; spent vs earned Robux is not stated, so no dollar value |
| 24 h mean 3,900 and 7-day mean 2,100 | 3,900 / 2,100 | our store (samples, so 3P-S-class sampling of an OFF counter); coverage UNKNOWN | 24 h and 7 d windows ending at an unknown read time | two means | two separate weeks |

### Derived numbers
| Number | Arithmetic | Label | Reading |
| --- | --- | --- | --- |
| Momentum | 3,900 / 2,100 = 1.857, so x1.86 (+86 %) | DER, momentum | The 24 h window sits inside the 7 d window. It is momentum. It is NOT week-over-week growth and NOT g7. |
| Added players, 24 h vs 7 d | 3,900 - 2,100 = +1,800 | DER | Shown next to the percent. Same overlap caveat. |
| Implied mean of the other 6 days | (2,100 x 7 - 3,900) / 6 = 10,800 / 6 = 1,800 | DER, assumes equal coverage in all 7 days | Says the rise is recent. Not a weekly comparison either (6 days vs 1 day). |
| Now vs 24 h mean | 4,210 / 3,900 = 1.08 | DER | One snapshot against a mean. No meaning by itself. |
| g7, added CCU, acceleration, trough | needs two non-overlapping complete weeks with coverage | UNKNOWN | Not computable from these four numbers. |
| Playtime estimate | needs visits added between two readings | UNKNOWN | One cumulative visits figure gives no window. |

### Rising-games row
| Game (universe ID) | CCU now (OFF) | Visits (OFF, cumulative) | Momentum 24 h / 7 d (DER) | g7 | Added CCU (g7 basis) | Revenue | Flag | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UNKNOWN (name and universe ID not given; key by universe ID before the row is filed) | 4,210 at 14:02 UTC (date UNKNOWN) | 12,400,000 (read time UNKNOWN) | x1.86 (3,900 / 2,100); coverage UNKNOWN | UNKNOWN | UNKNOWN (1,800 is the 24 h vs 7 d gap, not weekly) | 85,000 Robux/day, 3P-E, vendor and range UNKNOWN, accuracy UNKNOWN; not used for ranking | none; no breakout flag can be set | watch: possible riser, momentum only; alternative explanations (featuring, ads, event, one creator video, update) not checked; age of data UNKNOWN (under 14 days = "emerging lead") |

### One sentence for the owner
"This game had 4,210 players online at 14:02 UTC (Roblox Games API, one snapshot) and its last 24 h average of 3,900 is 1.86 times its 7-day average of 2,100 (our store, momentum, not weekly growth), so it is a watch item and not a confirmed riser; the 85,000 Robux/day figure is one tracker's estimate with unknown accuracy and I do not use it."

### Evidence that would allow more
Two complete non-overlapping UTC weeks from our store with coverage of 90 % or more (gives g7 and added CCU); the universe ID; two dated visits readings (gives visits added and the playtime estimate); the creator/featuring/event check. A revenue claim needs the owner's own data or a disclosure; a tracker estimate stays 3P-E.

---

## E2 — Is it a breakout?

### Arithmetic (DER; universe 123, our store)
| Item | Value |
| --- | --- |
| Weeks used (assumption) | 15 days = days 1-7 (week before), days 8-14 (last complete week), day 15 (partial, excluded) |
| g7 | 1,800 / 900 - 1 = +100 % |
| Added CCU | 1,800 - 900 = +900 |
| Coverage | last week 84 %, week before 97 %: the two weeks are not equally covered |
| Longest gap | 3 h; gap limit is 60 min (PROPOSAL), so it stays a gap: no bridge, no backfill |
| Video | day 12 is inside the last week: 4 days before it (8-11), 3 days from it (12-14) |

### Rule check (PROPOSAL flag rule, `formulas.md` §3)
| Condition | Result |
| --- | --- |
| g7 >= +50 % | pass (+100 %) |
| Added CCU >= +100 | pass (+900) |
| 3 matched days in a row above last week's matched days | UNKNOWN (needs the daily series) |
| Coverage gate >= 90 % | FAIL (84 %) |

### Decision
**Do not set a breakout flag.** The coverage gate holds it, and the gate is the rule, not a detail. Record it as "candidate, flag held by coverage gate (84 % < 90 %)" and watch it. The size of the jump is big enough that it should stay on the list, but this week's evidence is "a rise with one big, named alternative explanation", not a breakout. It is also not an "emerging lead" by the 14-day rule (15 days exist), but there is only one weekly change and no acceleration (needs 3 weeks).

Illustration, not a corrected figure: if every missing minute held 0 players, the last week would still average 0.84 x 1,800 = 1,512, which is +68 % on 900. So the rise is probably real. The size is not known, because the 3 h gap may sit on the video spike or on a trough, and the week before has its own 3 % hole.

### What to check
1. **Where the 3 h gap sits** (relative to day 12 and to the daily peak). Also whether it was our collector or a Roblox outage.
2. **Daily series, matched weekdays:** days 8-11 (before the video) against days 1-4. If they are already up, the rise started before the video. If they are flat, the video caused most of the week.
3. **Troughs and decay:** lowest daily mean in each week; days 13-15 against day 12. A fast fall back to the old trough = spike. Troughs that stay higher = stronger evidence.
4. **Mean/peak ratio** of the last week: low = spiky.
5. **Other explanations:** featuring or editorial pick, ads, an in-game event or update, a holiday, a chart placement (Top Trending). Name each as checked or not.
6. **The video:** exact channel ID, date-kind (posted), view count with read time. It is an alternative explanation and also a possible cause. One video is a single source.
7. **Breadth:** other independent creators on the same game; visits added, favourites added and votes added in each week (cumulative totals are no use).
8. **Next complete week:** coverage of 90 % or more, and still above the 1,800 level, would support a flag. Gaps cannot be filled later.

Not concluded: that the video caused it; that the rise will hold; any forecast.

---

## E3 — Copying a loop: rights and policy gate (card fields)

Idea as given: fishing-collection game, "the look of a popular anime", name "Fisch Legends". Anime title: UNKNOWN. Studio code and art: not yet made.

| Gate row | Result | Reason |
| --- | --- | --- |
| Loop (abstract) | pass | A fishing-collection loop (catch, sell or catalogue, better gear, rarer pools) is a family in the kit's records (Fisch and Fish It, both with large 2026 audiences). A loop idea is free to borrow. |
| Code and assets | HOLD until stated | Pass only if made by the studio or licensed. Nothing in the brief says so. Nothing may come from another game. |
| Title "Fisch Legends" | **FAIL for this name** | It contains the full name of an existing hit (Fisch). That is a "same or confusingly similar name", with a word added. A new spelling or a suffix grants no rights. The risk is trademark confusion and, on Roblox, lower discovery for games that closely resemble existing ones. I did not check any trademark register (UNKNOWN). Use a distinct name. |
| Look of a popular anime | **HOLD** | Which anime is UNKNOWN. A franchise theme without a licence is HOLD. Characters, names, logos, catchphrases and recognisable scenes are not free. A general anime-inspired art direction made by the studio is a different, original thing. The brief does not say which. Popularity grants nothing. |
| Music and sound | HOLD until stated | Anime songs and sound are separate rights (recording, composition, remix, in-game use). Original or licensed only. |
| Thumbnail and icon | HOLD until made | Must not resemble the Fisch icon or the anime's key art. |
| Gameplay difference (G5 twist) | not passed | Anime look and a new name are a new noun on a proven loop. A twist must change a player decision, stake, cooperation or expression. None is stated. |
| Platform rules (`platform-policy`) | HOLD, not yet checked | A fishing-collection loop usually has rolled rarity: paid random items, luck boosts, and odds disclosure need the policy check. A franchise or mature theme and the target age group also need it. |

**Card verdict:** the branded version (anime look + "Fisch Legends") is HOLD for rights and FAIL for the name. HOLD is reported once; the IP row is not scored at 0 as well. No score is given while gates are open. An original design on the abstract fishing-collection loop may continue with its own name, original art and a stated twist.

**What would clear it:** the owner or game-designer names the anime and what is borrowed. If a franchise is wanted: a written licence, or a rights-holder offer through Roblox's licensing tools (territory, term, revenue share, allowed content checked). If not: a general style with original characters. A distinct title; documented asset sources; `platform-policy` run at design time and at review.

Not concluded: that the anime is "free" because it is popular; that "Legends" makes the name safe; legal advice (this is a screening rule; a real rights question goes to the owner).

---

## E4 — Timing (cut-off 2026-10-20)

Meaning of the number: days from the **highest recorded sample** (3P-S, tracker, not the true peak) to the cut-off. DER = cut-off - sample date.

### Days since recorded peak
| Item | Event (kind) | Arithmetic | Days | Weeks |
| --- | --- | --- | ---: | ---: |
| Thesis 1: Grow a Garden | highest recorded sample 2025-08-23 (3P-S) | 2025-08-23 to 2026-08-23 = 365; to 2026-10-20 = 8 + 30 + 20 = 58; total 365 + 58 | **423** | 60.4 |
| Thesis 2: Escape Tsunami For Brainrots | highest recorded sample 2026-01-24 (3P-S) | 2026-01-24 to 2026-10-24 = 273; minus 4 | **269** | 38.4 |
| Related: Grow a Garden 2 | highest recorded sample 2026-06-19 (3P-S) | 2026-06-19 to 2026-10-19 = 122; plus 1 | **123** | 17.6 |
| Thesis 3: Verity | no recorded peak (UNKNOWN). Only dated events, not peaks: series debut 2026-05-30 (released); fan song 2026-07-10; Roblox game video 2026-07-25 (first observed) | 05-30 to 10-20: 31 + 30 + 31 + 31 + 20 = 143; 07-10 to 10-20: 31 + 31 + 30 + 10 = 102; 07-25 to 10-20: 31 + 31 + 30 - 5 = 87 | 143 / 102 / 87 | 20.4 / 14.6 / 12.4 |

Lags inside the Verity record (DER, single case, upper bounds on when the adaptation became visible; not forecasts): debut to song 41 days; debut to Roblox video 56 days; song to Roblox video 15 days.

### What the number means
- It says how long ago the dated mass-adoption high point was. For thesis 1 and 2 the early window, by the kit's rule, is closed: the reference game's peak is months back.
- It does NOT say current CCU, how steeply the game fell, or that demand is gone. A peak is one sampled point; an event or ad can make it. The kit records show large old-peak games that still hold big 2026 audiences (history from `loops.md`, 3P-S, not re-read now): Fisch peak 2025-10-18 = 367 days; Fish It 2025-12-07 = 317 days; Steal a Brainrot 2025-10-11 = 374 days; 99 Nights 2025-10-04 = 381 days; RIVALS 2026-02-14 = 248 days. So "days since peak" alone cannot separate "fading" from "durable family".
- Grow a Garden 2 at 123 days shows a sequel with a new twist also peaked months ago. A twist alone does not guarantee staying power.
- No half-life: that needs a falling, event-free weekly series. We have none.

### Which can be sold as an "early original wave"?
| Thesis | Early original wave? | Why |
| --- | --- | --- |
| 1: Grow a Garden reskin | **No** | Dated mass adoption 423 days ago. A "straightforward reskin" is not original and has no decision-changing twist (G5 fails). |
| 2: imitation of Escape Tsunami | **No** | 269 days since its record sample. An imitation is not original. |
| 3: first-mover Verity adaptation | **Not as worded** | "Spread across platforms" is a documented cross-platform wave, which already closes an "early wave" claim. A Roblox game video exists 87 days ago, so "first-mover" is contradicted or at least unproven (one third-party record, not checked; number of Roblox games on the theme UNKNOWN). Verity is a franchise character: an adaptation is rights HOLD. There is no Roblox number and no peak, so rising, flat or fading is UNKNOWN. |
| Fishing, PvP, survival families | Not "early", but **durable** | An original game can still enter, if it has its own current evidence and a stated twist. This is a family claim, not a wave claim. |

Best supported path (research priority only): Verity as a **watch** item, with an original design built on the abstract tension (a helpful companion turns unreliable), not the character, name, song or scenes. It stays research-only until the evidence below exists.

### What may not be concluded
- That thesis 1 or 2 have no demand now, or that reskins/imitations "never work". Current evidence is missing.
- That the days-since-peak figure gives a decay rate, a safe date or a forecast.
- That Verity is early, first, rising or fading on Roblox; that 56 or 15 days is a lead time for other trends.
- That the families fishing, PvP or survival are open or saturated from peak dates. That needs current counts, troughs, new entrants and a loop line.
- That the tracker date is exact (sampled, highest recorded sample only).
- Timing slack (window - build time - learning time): no build time and no demand threshold exist, so it stays qualitative.

### Evidence that would allow more
Current 24 h and 7 d CCU and weekly troughs for each reference game (store, with coverage); universe IDs of Roblox games already using the Verity theme with their own histories; Verity view velocity from independent channel IDs in equal windows and on 2 or more platforms; rights status; a build estimate from the architect.

---

## E5 — Three candidates from tracker data

Source: RoVitals, 3P-S, hand-read near 2026-10-21 01:00 UTC. Tracker means move live; the read time is approximate. The peak window and the game age are UNKNOWN.

### Arithmetic (DER)
| Quantity | Formula | Create a Robot Fighter | Something is Wrong With My Dog | Backseat Rally |
| --- | --- | ---: | ---: | ---: |
| Momentum (24 h / 7 d) | 24 h mean / 7 d mean | 1,005 / 301 = x3.34 | 3,466 / 1,261 = x2.75 | 20,489 / 10,274 = x1.99 |
| Added players, 24 h vs 7 d | difference | +704 | +2,205 | +10,215 |
| Implied mean of the other 6 days (assumes equal coverage) | (7 x mean7 - mean24) / 6 | (2,107 - 1,005) / 6 = about 184 | (8,827 - 3,466) / 6 = about 894 | (71,918 - 20,489) / 6 = about 8,572 |
| 24 h mean / observed peak | | 1,005 / 2,803 = 0.36 | 3,466 / 9,900 = 0.35 | 20,489 / 29,270 = 0.70 |
| 7 d mean / observed peak (peak date 2026-10-20 lies inside the 7 days) | | 301 / 2,803 = 0.11 | 1,261 / 9,900 = 0.13 | 10,274 / 29,270 = 0.35 |

All momentum values are momentum, **not** weekly growth. g7, coverage, troughs and acceleration are UNKNOWN for all three (tracker data gives no non-overlapping weeks and no coverage). Robot Fighter has the highest momentum on the smallest base: a high ratio on a small base is weak evidence.

### Gates (all three)
| Gate | Status |
| --- | --- |
| G1 Evidence route | pass only if read by hand (RoVitals is hand-reading only); the read is MAN/3P-S. Confirm. |
| G2 Original | not assessable; the opportunity is the loop, and the rights check has not run. Titles may point to outside IP or a meme: not assessed, no title-only identity. |
| G3 Audience and policy | not checked |
| G4 Scope | UNKNOWN (no estimate from the architect or designer) |
| G5 New decision (twist) | none defined: loop line, twist and theme are all UNKNOWN. Universe IDs are UNKNOWN. |

### Score
Gates are open, so **no score is given**. Under the UNKNOWN rule (UNKNOWN is a range, never a neutral 3):

| Candidate | Lower score | Upper score | Completeness |
| --- | ---: | ---: | ---: |
| Create a Robot Fighter | 0 | 100 | 0 % |
| Something is Wrong With My Dog | 0 | 100 | 0 % |
| Backseat Rally | 0 | 100 | 0 % |

Reason: not one dimension can be rated from this table. "Growth speed and persistence" needs weekly growth with coverage of 90 % or more (we have momentum). Demand needs the studio's test economics (UNKNOWN). Revenue evidence is none (tracker CCU is not money). Fit, build, room, IP and staying power need a loop, a twist and a build estimate. A 0 to 100 range with 0 % completeness is the honest result; any single number would be invented. A score is not a success chance either way.

### Top 3 as research priority (not opportunities, not green lights)
The table has exactly three games, so "top 3" is all three. Ordering rule: higher 24 h / peak ratio first (more of a plateau, less of a spike), then larger added players, with momentum read last because small bases inflate it. This order may change with the checks below.

| Rank | Candidate | Why this place | Action |
| ---: | --- | --- | --- |
| 1 | Backseat Rally | Largest base (20,489 24 h; +10,215), and its 24 h mean is 0.70 of its highest recorded sample, the least spiky of the three. Lowest momentum (x1.99) because the base is high. | Research ticket |
| 2 | Something is Wrong With My Dog | Mid base (3,466; +2,205), x2.75; 24 h / peak 0.35, spiky. | Research ticket |
| 3 | Create a Robot Fighter | Highest momentum (x3.34) on the smallest base (1,005; +704); 24 h / peak 0.36; implied prior-6-day mean about 184. | Research ticket (lowest priority) |

Week status: **no qualified build opportunity**; three research leads. Ticket reason (upper score > 75 with completeness < 80 %): name the missing evidence.

### Missing evidence per lead
1. Universe ID and `created` date for each (young game under 14 days of data = "emerging lead").
2. Our own store samples: two complete weeks, coverage, matched-day troughs, mean/peak, g7 and added CCU.
3. **Shared cause:** all three show their highest recorded sample on the same day (2026-10-20, a Tuesday). Check for a platform-wide rise that day, a chart or featuring change, an event, or a season effect. If all three rose together, they are not three independent signals. Also check whether the tracker's "observed peak" window is long or short.
4. Alternative explanation per game: featuring, ads, update, creator video (exact channel ID), holiday.
5. Breadth: other games on the same loop rising; independent creators; 2 or more platforms.
6. Loop line and 8 fields from store page, trailer and unedited gameplay (promise vs observed log). Not from titles.
7. Rights and policy gate (names and themes), and `platform-policy` if rolls or purchases exist.
8. Smallest test, build estimate, kill condition, and the studio's economics. Revenue stays UNKNOWN or a labelled 3P-E; never from CCU.

Not concluded: any of the three will keep its players; momentum equals growth; CCU equals users or money; a rank or score between them beyond research order.
