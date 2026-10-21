---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J004
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source: `Roblox_Trend_Scout_Research_2026.txt` (owner paper, outside git), lines 1-188 (summary, evidence contract, section 1 Roblox game data, section 2 loops) plus the register entries (lines 492-649) of every S-id cited there. Paraphrased. Section 3 onward (lines 189-491) is not in this file.

# Trend scout research, part 1 (RP:1-188): Roblox data and gameplay loops

Reading rule: keep the tag next to every number. Never merge official, sampled, model and derived values. UNK = the paper says it is not established; it is never zero. "PROPOSAL" = the paper's own operating threshold or design (tag OPN), not a platform rule, not backtested. Cite as `RP:<line>` (paper line) and `S##` (paper source id, entries in section 15). Extractor remarks are marked "(extractor)". Issues found in the paper: section 16.

| Tag | Meaning (RP:27) |
| --- | --- |
| V-OFF | VERIFIED, official platform or government source |
| V-SAMP | VERIFIED, sampled third-party counter (tracker); a sample, not a census |
| V-3PM | VERIFIED, third-party model or methodology description (the description is verified, the model output is not) |
| V-VEND | VERIFIED, vendor dataset (instrumented sample) |
| EXP | EXPERIENCE: attributed developer testimony, no independent audit |
| OPN | OPINION: author interpretation, rubric, threshold, hypothesis or test design |
| DER | derived calculation (inputs and formula must be named) |
| UNK | not established by the inspected evidence |

Paper cutoff: 2026-10-20, America/New_York (RP:3). Some tracker samples carry 2026-10-21 UTC stamps (same NY day). Purpose of the paper: find rising demand early enough to ship an original game; the unit is a repeatable player behaviour, its channel and its remaining production window; a popular name is not an opportunity (RP:5, OPN, S03 S04).

## 1. The 15-line summary (RP:7-23)

| id | rule (my words) | tag | S | RP |
| --- | --- | --- | --- | --- |
| 01 | Store official observations, tracker observations, model estimates and developer testimony in separate stores | OPN | S01 S08 | 9 |
| 02 | Key games by universe ID and root place ID; names and thumbnails change | OPN | S01 S02 | 10 |
| 03 | Concurrent accounts are not daily unique people; visits are not unique players or sales | OPN | S01 S02 | 11 |
| 04 | Compare time-weighted averages and matched weekdays, not a live count against an event record | OPN | S03 S08 | 12 |
| 05 | Roblox Trending describes more time spent over two weeks; it is not a revenue ranking | V-OFF | S06 | 13 |
| 06 | Roblox recommendations now look at behaviour through days 8-28; a short spike is not enough | V-OFF | S03 S04 | 14 |
| 07 | Public game revenue is an estimate unless an authorised owner or official disclosure gives it | OPN | S07 S09 | 15 |
| 08 | No universal multiplier from CCU to DAU or to dollars | OPN | S09 S10 | 16 |
| 09 | Describe every loop as action, reward, reinvestment, next goal, plus a return trigger | OPN | S16 S19 | 17 |
| 10 | Borrow an abstract loop; make own code, assets, identity and a meaningful gameplay change | OPN | S04 S27-S30 | 18 |
| 11 | Count independent creators and repeat interest, not one viral upload or cumulative hashtag views | OPN | S34 S35 S41 | 19 |
| 12 | Steam revenue rank, CCU and wishlists answer different questions; keep their definitions | V-OFF | S36-S38 | 20 |
| 13 | Public visibility alone gives no right to scrape, use for AI, or store history | V-OFF | S31 S35 S39 S44-S45 | 21 |
| 14 | Use build-time ranges and a forecast of demand at launch date; no reliable universal Roblox trend lifetime was found | OPN | S14 S15 | 22 |
| 15 | Recommend three bounded tests, each with evidence and a kill condition; never invent three green lights | OPN | S03 S07 | 23 |

## 2. Evidence contract and accuracy hierarchy

| Item | Content | RP |
| --- | --- | --- |
| Three marks | VERIFIED = the cited source directly supports the statement (not that all sources are equally authoritative); add a provenance label (one of: official; sampled third party; third-party model; secondary historical account; derived calculation). EXPERIENCE = attributed testimony, unaudited. OPINION = author-proposed reading, rubric, hypothesis, threshold or test design. Unknown = not established, never replaced with zero | 27 |
| Claim block | Each marked paragraph or table row. Its S-number points to a register record (title, publication/update date if known, access date, quote under 20 words, URL). The quote is a locator, not a substitute for the source. OPN blocks cite factual motivation only; the source does not endorse the rule. A DER block names inputs and formula. No quotes invented for recommendations | 29 |
| Use limits | The paper is a reference for the agent, not a licence to train model weights on third-party content. Runtime retrieval, screenshots, history storage, inference and training are different permissions. Keep the source effective date and the retrieval date | 31 |
| Terms caveat | Roblox terms page advertises effective date 2026-11-01. Do not treat upcoming wording as in force on 2026-10-20. Use the applicable archived or current contract before collecting (S31) | 31 |
| Accuracy order (1 = best) | 1 authorised transaction/export data for the exact game and period; 2 official aggregate or rank for its stated scope; 3 attributed owner disclosure; 4 timestamped public-counter observations; 5 inferred metrics with disclosed assumptions; 6 opaque estimates | 33 |
| Independence | Official aggregate economics cannot validate one game's inferred income. Two sites reusing one source are not two confirmations | 33 |
| Tag note (extractor) | The paper also uses combined or extra labels (for example "V-OFF + V-SAMP", "tracker description", "vendor dataset"); all kept as written in the tables below | 70 109 119 |

## 3. Endpoint map (RP:35-52)

RP:39 (V-OFF, S01 S02): the Games domain lists unauthenticated game-details, votes, favorites-count and server-list endpoints. Many legacy routes are labelled Experimental in the docs. A retrieved game-details response for Grow a Garden has: id, rootPlaceId, creator, playing, visits, favoritedCount, created, updated, maxPlayers, genre fields, canonicalUrlPath. These are public observations, not owner analytics. Availability depends on access, restrictions and API change.

| # | Task | Route (as written) | Limitation (paper) | Mark | S | RP |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Game details: online count, visits, favorites, timestamps, creator, root place | GET `https://games.roblox.com/v1/games?universeIds=7436755782` (example is one universe ID, Grow a Garden) | Query by universe IDs. `playing` is a snapshot. `visits` accumulate entries. `created` is universe creation time, not proof of public release | V-OFF | S01 S02 | 43 |
| R2 | Up and down votes | GET `https://games.roblox.com/v1/games/votes?universeIds={ids}` | Store both counts. approval = up / (up + down); undefined when there are no votes | V-OFF / DER | S01 | 44 |
| R3 | Favorite count | GET `https://games.roblox.com/v1/games/{universeId}/favorites/count` | A count, not loyalty or retention | V-OFF | S01 | 45 |
| R4 | Place to universe | `https://apis.roblox.com/universes/v1/places/{placeId}/universe` | Common route reported on DevForum; the research browser could not retrieve it; test before building on it | EXP | S52 | 46 |
| R5 | Public server list | GET `https://games.roblox.com/v1/games/{placeId}/servers/Public` | Per-place pagination; not a reliable rebuild of all activity in a universe | V-OFF route; OPN limitation | S01 | 47 |
| R6 | Games of a developer or group | GET `/v2/users/{userId}/games` and `/v2/groups/{groupId}/gamesV2` on games.roblox.com | Grows the candidate universe registry; public inventory is not a complete historical census | V-OFF route; OPN scope | S01 | 48 |

UNK (paper silent): batch maximum for any route; authentication need of R4 to R6 (RP:39 says unauthenticated only for details, votes, favorites, server list); request-per-minute entitlement (RP:54).

### Raw fields and identity (RP:50, 52)

| Field | Meaning and rule (paper) | Tag | RP |
| --- | --- | --- | --- |
| Observed response (S02) | One retrieved Grow a Garden response: playing 15,757; visits 35,981,794,210; favorites 11,452,804; created 2025-03-25T22:32:09.437Z; updated 2026-10-20T01:28:46.738Z. Shows the schema only. No verified upstream sample time. Not simultaneous with the tracker tables | V-OFF observation | 50 |
| Keep raw names | Use the field names as returned | OPN S01 S02 | 52 |
| playing | Snapshot of current online count | V-OFF | 43 |
| visits | Cumulative entries; not unique players or sales | V-OFF / OPN | 43 |
| favoritedCount | Cumulative; may be dominated by old cohorts; not retention | OPN | 45 52 |
| votes | Cumulative; same cohort caveat | OPN | 52 |
| maxPlayers | Server capacity, not a universe's total audience | OPN | 52 |
| created | Universe creation timestamp; not release proof | V-OFF | 43 |
| updated | Can change for administrative reasons; treat as metadata/update evidence, never as a content-release date | OPN | 52 |
| Identity | A game can rename, change owner or be repurposed: keep identity history; require owner and root-place checks before joining records; same-name games exist, so title-only matching is not acceptable | OPN | 52 |
| ID kinds (extractor) | Paper IDs seen: GaG universe 7436755782 (S02 S53); Dead Rails universe 7018190066 and root place 116495829188952 (S23); Dig it place 76455837887178 stated as one place, not a title-wide identity (S22). Tracker URL numbers for other games are not stated to be universe or place IDs | - | 43 535 533 |

## 4. Rate limits and stability (RP:54-56)

| Item | Content | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Stability | Roblox separates Open Cloud from legacy APIs; legacy interfaces carry minimal stability guarantees and may change without notice | V-OFF | S11 S12 | 54 |
| Rate limits | Depend on endpoint and authentication context; handle HTTP 429. No universal numeric requests-per-minute figure for public Games routes was verified (UNK). The in-game HttpService limit does not permit an outside crawler to use that rate | V-OFF; UNK | S11 S12 | 54 |
| Per-route config (PROPOSAL) | Record per route: documentation URL, permitted purpose, authentication, batch maximum, observed headers, cache TTL, retry policy. Read current schemas; do not hard-code an unverified batch maximum | OPN | S11 S12 | 56 |
| Retry (PROPOSAL) | Honour Retry-After if present; else exponential backoff with jitter; bounded queue; circuit breaker. No account or IP rotation to dodge limits | OPN | S11 S12 | 56 |
| Interval (PROPOSAL) | Five-minute collection is a studio design choice, not a Roblox guarantee | OPN | S11 S12 | 56 |

## 5. Private metrics versus public estimates (RP:58-74)

| Item | Content | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Private to the owner | Creator analytics give retention, monetization, acquisition and behaviour analysis for games the creator can access. From the public Games response a scout cannot get a competitor's real D1, D7 or D30 retention, payer conversion, ARPDAU, country split, acquisition-source split or net profit. Ask for authorised exports for the studio's own games and keep them apart from competitor observations | V-OFF | S07 | 60 |
| Playtime formula | estimated minutes per entry = 60 x observed player-hours / added visits. An occupancy-to-arrival approximation. Needs matched population and time boundaries, reliable visits, enough coverage. Not session telemetry. Bias sources: sessions crossing the boundary, idle accounts, teleports, delayed counters, outages. Cannot give a cohort retention curve or unique users | OPN / DER | S08 S09 | 62 |
| Validation status | No matched independent Roblox panel was found that compares dated tracker forecasts with later owner-published actuals (same game, period, currency, revenue definition). Report accuracy as UNKNOWN, not "within 10%", "95% accurate" or "roughly correct". A vendor confidence label, narrow range or agreement with platform totals is not game-level accuracy | OPN | S09 S10 S25 | 72 |
| Validation ledger fields (PROPOSAL) | game ID; prediction publication timestamp; period forecast; model version; gross player spend vs earned Robux vs cash; later owner disclosure or export; fees; rewards; exchange-rate vintage; payout splits; relative error | OPN | S07 S09 | 74 |
| Ledger metrics (PROPOSAL) | For actual A and estimate E: log(E/A); absolute percentage error when A > 0; median multiplicative error; interval coverage. Use held-out games and periods; split by genre and size; never calibrate and validate on the same disclosures. An owner screenshot stays EXP unless authenticated enough for the decision | OPN | S07 S09 | 74 |

## 6. Tracker and estimate providers (RP:64-70)

| Provider | Offers or claims | Method and validation status (paper) | Tag | S | RP |
| --- | --- | --- | --- | --- | --- |
| Rolimon's | Public counters, sampled peaks and history, displayed average playtime | Table says updates about every ten minutes (register quote: most details, usually); recorded peak can miss the true maximum. No owner-audited error rate for displayed playtime in the inspected pages | V-SAMP | S08 S16-S24 | 66 |
| RoTrends | Experience comparison, public trend and history pages | Useful for discovery. Current export licence, price, published revenue-error distribution and validated retention estimator not established (bounded research gap) | V-OFF scope / bounded research gap (paper: "VERIFIED source scope") | S53 | 67 |
| Statroblox | Revenue model from earning rank, player-hours and visits | Vendor describes a weighted geometric combination and creator-level payout calibration; range floor of divide/multiply 1.6. The floor is not shown to be 95% coverage. Creator-to-game mapping is an assumption | V-3PM | S09 | 68 |
| RoVitals | Sampled history; illustrative earnings scenarios | Robot Fighter page assumes 2 earned Robux per player-hour and multiplies/divides the central model by three; stated not to be a confidence interval | V-3PM | S25 | 69 |
| GameAnalytics | Instrumented SDK sample, not public telemetry of arbitrary games | 2026 report: 500+ titles with 1M+ MAU, Aug 2025 to Jul 2026. A selected large-game sample, not a random census | V-VEND (paper: "first-party vendor dataset") | S10 | 70 |
| RoStats (extractor) | Seven-day mean and metadata used for Dead Rails (RP:145) | Page not synchronised with other pages; register quote shows a players x hours / visits expression (S23). The paper does not discuss RoStats method in section 1 | V-SAMP | S23 | 145 |

## 7. Charts and discovery (RP:76-87)

| Surface | Ranking meaning (verified) | Update frequency established | Infer | Tag | S | RP |
| --- | --- | --- | --- | --- | --- | --- |
| Most Popular / top playing now | Most players currently online | Live label; no numeric refresh SLA | Scale at observation time | V-OFF | S05 | 80 |
| Top Trending | Ranks games by growth in player time across the last two weeks | No numeric cadence | Recent engagement growth; formula and normalisation not fully disclosed | V-OFF | S06 | 81 |
| Top Earning | Revenue or spend order; third-party method describes trailing seven-day Robux spend | Current official FAQ formula and cadence not retrieved (UNK) | Ordinal monetisation signal, not dollar income | V-3PM description; official scope corroborated | S09 S13 | 82 |
| Top Revisited / Fun with Friends | Labels hint at repeat or social use; full formulas not verified | UNK | Investigate; do not turn labels into exact retention or co-play rates | OPN | S03 S04 | 83 |
| Recommended For You | Personalised ranking using per-user behaviour after organic RFY acquisition | Daily retesting described in FAQ; wider refresh SLA UNK | A game can grow without topping global charts | V-OFF | S03 | 84 |
| Today's Picks / editorial | Curation can push selected games | No common cadence | Mark exposure as a confounder, not proof of organic emergence | V-OFF case; OPN reading | S13 | 85 |

Discovery horizon (RP:87, V-OFF, S03 S04; extra cite S54): current guidance separates first-play signals from day 2-7 and day 8-28 behaviour. Stresses playthrough, first-play bounce, play days and playtime; social and spending signals also matter. Signals use users acquired organically through RFY, including their later return; they are averages per user; total CCU is not the formula. Guidance of 2026-06-15 widened the horizon from 7 to 28 days. September RDC guidance (published 2026-09-11) adds age-aware discovery and says Moments are available in the U.S., with age and region variation (rollout qualifiers kept; S54).

## 8. History, breakout and fade (RP:89-99)

All items in this section are OPN (PROPOSAL) unless noted.

| Topic | Content | S | RP |
| --- | --- | --- | --- |
| Time handling | Store UTC; report in studio timezone; record collector clock and source clock | S03 S08 | 91 |
| Raw schema | universe_id, root_place_id, observed_at_utc, source_sample_at_utc, playing, visits, upvotes, downvotes, favorites, source, schema_version, permission_version, observed_or_imputed, event_flag, outage_flag. Gaps stay gaps; never backfill historical CCU by formula and label it observed | S03 S08 | 91 |
| Player-hours | Integrate over time, preferably with trapezoids between adjacent observations | S08 S25 | 93 |
| Time-weighted average CCU | = integrated player-hours / covered hours. Publish coverage with every window | S08 S25 | 93 |
| Coverage gate | Suppress automated promotion if a seven-day window covers under 90% of intended minutes, or holds a gap over 60 minutes. Proposed controls, not measured optima. Do not bridge a long outage with a straight line | S08 S25 | 93 |
| g7 | g7 = meanCCU(last 7 complete days) / meanCCU(previous 7 complete days) - 1. Non-overlapping periods | S03 | 95 |
| Acceleration | = g7(current) - g7(previous week), in percentage points | S03 | 95 |
| Also show | Absolute added average CCU; matched weekday/hour; 24-hour and seven-day troughs; visit increments; mean/peak ratio | S03 | 95 |
| Momentum ratio | Recent 24-hour average / an overlapping seven-day average. It is a momentum ratio, not week-over-week growth | S03 | 95 |
| Zero baseline | Show "new / insufficient baseline", never infinity | S03 | 95 |
| Breakout alert (PROPOSAL) | +50% non-overlapping g7, and at least +100 average CCU, and three consecutive matched days above baseline. Needs backtesting; not a proven predictor. Qualify with independent creator uptake, improving off-event troughs, monetisation rank if known. Spike then reversion, flat troughs, or falling visit increments is weaker evidence than sustained broad growth | S03 S25 S26 | 97 |
| Young games | No two-week history: publish daily observations and call it an emerging lead | S03 S25 S26 | 97 |
| Fade flag (PROPOSAL) | Needs two negative weekly changes in a row (periods do not overlap) and also a lower matched trough; check against platform seasonality and rival releases. Fade means a defined baseline fell, not that an event record ended. Keep event peaks and event-free occupancy as separate series | S08 S16 S19 | 99 |
| Peak-vs-weekday | A 99% fall from a one-hour record to a weekday count is true arithmetic but misleading as a retention statistic | S08 S16 S19 | 99 |

## 9. Money facts (RP:101-113)

| Fact | Value and date | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Creator earnings | Over USD 1.5 billion earned by creators in 2025; USD 923 million in 2024 (Roblox announcement 2026-09-03) | V-OFF | S14 | 103 |
| DevEx participants | Over 42,000; approximately USD 1,500 median receipt; twelve months ended 2026-06-30 | V-OFF | S14 | 103 |
| Scope warning | Creator-economy context, not expected income per new game; owners, creators, games, participants and surveyed businesses are different populations | OPN | S14 | 103 |
| DevEx standard rate | USD 0.0038 per eligible Earned Robux | V-OFF | S15 | 105 |
| DevEx adult rate | USD 0.0054 for certain eligible in-game spending by age-verified U.S. adults; support page dates this rate to 2026-06-08 | V-OFF | S15 | 105 |
| Vintage warning | Older earned balances can use a different rate. Do not value all Robux at the adult rate or at the consumer purchase price | V-OFF / OPN | S15 | 105 |
| O18 vs U18 | Q2 2026 shareholder letter (2026-07-30): U.S. O18 users monetise over 50% higher than U18 in its stated comparison. A cohort signal; not proof any adult genre or future studio game monetises 50% better | V-OFF | S55 | 107 |
| GameAnalytics medians | Median per-game session length 9.8 min; p90 14.7; p99 21.1 (units minutes); median D1 retention 10.3%. Sample: 500+ titles, 1M+ MAU, Aug 2025-Jul 2026. Comparison context only; do not infer a competitor's retention from CCU or a new game's attainable monetisation | V-VEND | S10 | 109 |
| Genre profit | No defensible universal genre ranking of net profit per player. Collection/trading, progression and repeat-purchase games are monetisation hypotheses | OPN | S07 S09 S13 | 111 |
| June 2025 top ten | Roblox disclosed Grow a Garden, Steal a Brainrot and Dead Rails among the ten largest games by Robux spend in June 2025: proves high aggregate spend, not best ARPDAU or margin. Small-audience games can beat larger ones per player; paid acquisition, geography, idle time, payer share, product mix must be reconciled | OPN (paper tag) | S07 S09 S13 | 111 |

Cash contribution (RP:113, OPN/DER, S07 S15), for an owned game:
cash contribution = eligible earned-Robux cash value + applicable cash ad/other receipts - refunds/adjustments - publisher/owner obligations - acquisition - development - live operations - moderation/support - other attributable costs. Do not double count a receipt already in earned Robux.
Monthly spend = DAU x payer conversion x spend per payer per day x days, only when all definitions and time windows match. Public CCU identifies none of the missing factors. Any money calculation shown must be labelled a scenario, never predicted profit.

## 10. Rule tables (RP:115-122 and 181-187)

| Rule | Number | Tag | Source and date | RP |
| --- | --- | --- | --- | --- |
| Trend separate from size | Trending looks back two weeks | V-OFF | S06, undated, accessed 2026-10-20 | 117 |
| Current discovery horizon | Day 1, 2-7, 8-28 | V-OFF | S03-S04, current docs / 2026-06-15 | 118 |
| Tracker peaks are sampled maxima | Rolimon's about ten-minute updates | V-3P tracker description | S08, accessed 2026-10-20 | 119 |
| No invented revenue precision | Game-level validated error rate unknown | OPN research conclusion | S09-S10, S25, accessed 2026-10-20 | 120 |
| Exchange-rate tier | USD 0.0038 standard; USD 0.0054 qualifying adult spend | V-OFF | S15, current docs, accessed 2026-10-20 | 121 |
| Growth flag with coverage controls | Proposed 90% coverage; +50% g7; +100 average CCU | OPN starting policy (PROPOSAL) | S03, S08; author policy dated 2026-10-20 | 122 |
| Tiny product can precede fast growth | ~500 to ~100,000 CCU in ~two weeks | EXP | S17a, interview 2025-09-07, updated 2025-09-08 | 183 |
| No build lag from peak dates | Fishing adaptation launch lag UNK | OPN | S20-S22, accessed 2026-10-20 | 184 |
| Budget for operations after launch | 99 Nights reported a three-month build sprint | EXP | S24, 2025-10-31 | 185 |
| A twist does not guarantee endurance | Garden 2 sampled 929,371 peak, 2026-06-19 | V-SAMP | S61, accessed 2026-10-20 | 186 |
| Separate mechanic from protected expression | No safe percentage of copying established | V baseline / OPN policy | S27-S30, current official pages, accessed 2026-10-20 | 187 |

## 11. Extracting a loop (RP:126-132)

| Item | Content | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Loop line (slot template) | One line with slots: player does [repeated action] to gain [reward]; spends it on [persistent change]; repeats against [harder goal, rarity or social contest]; returns because [trigger]. Theme and monetisation stay outside the core-action slot. "Anime simulator" is packaging, not a loop. Also note what the player controls, what can be lost, who creates opposition, how the next goal shows | OPN | S16 S19 S21 | 128 |
| Evidence order | 1 page and trailer = the advertised promise; 2 unedited recent gameplay = real first-session order; 3 permitted direct play by a human or authorised test setup = friction and return triggers. Do not claim a playtest if only a video was seen. Record observational confidence | OPN | S01 S03 | 130 |
| Promise-vs-observed log | Two columns. Pages can omit paid shortcuts, resets and failure conditions | OPN | S01 S03 | 130 |
| Eight fields | 1 action; 2 reward; 3 reinvestment; 4 escalation; 5 session ending; 6 return trigger; 7 social relationship; 8 monetisation insertion | OPN | S16 S19 | 132 |
| Layers | Keep the core loop apart from the metagame and live operations. A weekly admin event can bring players in or back, yet it may not describe a normal day of play | OPN | S16 S19 | 132 |

## 12. Loop catalogue 2025-2026 (RP:134-155)

Catalogue rules (RP:136, OPN, S13 S16-S24 S54-S55): a taxonomy of evidenced families, not a market-share claim. Roblox gave spend or search evidence for some families; tracker numbers show example scale. Paper says all current counts are single retrieved tracker snapshots near the cutoff, not synchronised averages, and all exact peaks are Rolimon's highest recorded points, not audited records. Rise and fade dates are UNK where no full time series was obtained. (Extractor: some rows below contradict these two statements; see I4.) The table has 14 rows (RP:140-153), not 13.
Units: "peak" = recorded highest concurrent players on the date; "snap" = one retrieved current-players snapshot (no timestamp given); "7d peak" = recent seven-day peak; "24h/7d mean" = tracker mean concurrent players.

| # | Family: loop chain | Example | Numbers | Rise and fade evidence | Tag, S, RP |
| --- | --- | --- | --- | --- | --- |
| 1 | Offline growth tycoon: buy inputs, grow while away, harvest/sell, buy rarer production | Grow a Garden | peak 22,375,597 on 2025-08-23; snap 16,559; 7d peak 107,178 | Official launch 2025-03-25; #1 by spending within a month. Record scale summer 2025; far lower peak scale by Oct 2026. Start of sustained decline UNK | V-OFF + V-SAMP; S13 S16; 140 |
| 2 | PvP ownership economy: buy/steal collectors, produce income, defend/rebirth, contest rarer collectors | Steal a Brainrot | peak 25,836,222 on 2025-10-11; snap 159,490 | Created 2025-05-16 (tracker table). Official over-25M record reported for Sep 2025; later sampled max need not conflict. Peak-scale fade date UNK | V-OFF + V-SAMP; S17 S56; 141 |
| 3 | Risky retrieval plus idle base: cross hazards, bring collectible home, earn, improve movement/storage | Escape Tsunami For Brainrots | peak 4,996,032 on 2026-01-24; snap 2,823; 7d peak 32,495 | Large Jan 2026 peak; much smaller recent event scale by Oct 2026; rise and decline inflection dates UNK | V-SAMP; S18; 142 |
| 4 | Fishing collection progression: catch, sell/catalogue, upgrade gear, reach rarer pools | Fisch; Fish It! | Fisch: peak 1,273,618 on 2025-10-18; snap 64,244. Fish It: peak 2,716,766 on 2025-12-07; snap 69,352 | Proven 2025 peaks, 2026 residual audiences. Fish It credits Fisch and Fishing Simulator. First breakouts and recoveries in between not rebuilt | V-SAMP; S20 S21; 143 |
| 5 | Excavation reskin: dig, sell discoveries, buy shovels, explore new rarity pools | Dig it! by Biodegradable Inc. | peak 28,135 on 2025-02-01; snap 3 | Credits Fisch. Little current activity in this universe. Not to be confused with another Dig It title; cause of decline UNK | V-SAMP; S22; 144 |
| 6 | Cooperative expedition survival: scavenge fuel/loot, maintain transport, survive route, unlock run options | Dead Rails; a dusty trip | Dead Rails: in Roblox's June 2025 top ten by spend; RoStats seven-day average 14,813 (retrieval date not given beyond near cutoff). a dusty trip: no number in paper | Dead Rails created Jan 2025 per tracker; high official spend June 2025; peak and fade timeline UNK | V-OFF + V-SAMP; S13 S23; 145 |
| 7 | Night survival crafting: gather, build/refuel camp, survive escalating nights, improve next attempt | 99 Nights in the Forest | peak 14,153,173 on 2025-10-04; snap 108,092; 7d peak 2,141,327 | Official spotlight: June 2025 launch after a three-month sprint, about 14M peak by Oct 2025. "Not dead" (paper) | V-SAMP / EXP (development); S19 S24; 146 |
| 8 | Fashion social judging: interpret prompt, assemble outfit, present/vote, gain status, next prompt | Dress To Impress | peak 1,743,147 on 2024-12-14; snap 82,360; 7d peak 539,298 | Predates the requested period; persisted 2025-2026; fade start not established | V-SAMP; S57; 147 |
| 9 | Short competitive mastery: duel, win keys/contracts, unlock options/cosmetics, rematch | RIVALS | peak 967,342 on 2026-02-14; snap 114,917 | Established competitive family with a 2026 peak; evidence too thin to date rise or fade | V-SAMP; S58; 148 |
| 10 | Combat RPG grind: defeat enemies/quests, gain power, unlock zones/bosses, improve build | Blox Fruits | peak 2,781,531 on 2024-12-31; snap 112,675 | Long-lived predecessor active 2025-2026; decline and recovery periods not established | V-SAMP; S59; 149 |
| 11 | RNG assembly incremental: roll components, assemble/train unit, fight waves, buy luck/rebirth | Create a Robot Fighter | 24h mean 1,005 vs 7d mean 301 (third party); peak 2,803 on 2026-10-20 | Early observed rise; "ten-plus-day" tracking window (start date not given); no fade date yet | V-SAMP; S25; 150 |
| 12 | Familiar-companion anomaly horror: explore/maintain shelter, notice changes, survive/reveal endings, replay | Something is Wrong With My Dog | 24h mean 3,466 vs 7d mean 1,261; peak 9,900 on 2026-10-20 | Observed Oct 2026 rise; earlier creator-source dates and causality unverified here | V-SAMP; S26; 151 |
| 13 | Social roleplay and pet collection: inhabit setting, personalise/collect, trade or perform social scenarios, return for friends/content | Brookhaven; Adopt Me | Brookhaven #1 search in Roblox's 2025 recap; current matched player-count series not collected | Evidence of durable demand; not an early wave or a new 2026 breakout | V-OFF; S56; 152 |
| 14 | Tower defense roster progression: acquire units, place/upgrade against waves, earn, improve roster, harder stage | Anime Adventures and other TD titles | RoVitals: Anime Adventures 24h mean 6,413 vs 7d mean 2,186 in the inspected list | Candidate reactivation signal; not proof the TD family is rising | V-SAMP; S60; 153 |

Extractor arithmetic (not in the paper): 24h/7d ratios of rows 11, 12, 14 are about 3.34, 2.75, 2.93. They are momentum ratios in the sense of RP:95 (24-hour window overlaps the 7-day window), not week-over-week growth.

### Taxonomy rules (RP:155, OPN, S13 S55 S56)

| Rule | Content |
| --- | --- |
| Separate axes | Keep theme, input complexity, progression model and social relationship apart |
| Theme vs loop | Brainrot is a theme and collection universe; it can sit on stealing, hazard retrieval, RNG or tower defense |
| No double count | Never add one game's CCU twice when estimating family share |
| Labelling | Multi-label for design questions; one exclusive primary-loop label for market-share maths; an explicit unclassified bucket |

## 13. Proven loop plus new theme and twist (RP:157-171)

| Case | Facts (paper) | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Grow a Garden interview | Jandel says the team partnered at about 500 CCU; about two weeks later about 100,000; about a month later one million. Weekly updates and offline growth described as important. Recollections, not a daily audited dataset. Derived: 500 to 100,000 = about 200x in two weeks (DER); must not become a target for new games | EXP; DER | S17a | 159 |
| Lesson claimed | Familiar farming economy, visible persistent progress, low-friction return, and a team that expanded a small working product. No controlled counterfactual shows which feature caused growth. The article's opening arithmetic ("104 days" from March 26 to a September interview) is called wrong by the paper; use Roblox's March 25 launch statement and attribute recollections | OPN | S17a S13 | 161 |
| Fish It and Dig it | Fish It credits Fisch and Fishing Simulator; the inspected Dig it universe credits Fisch. Both reuse collection, selling, upgrades, exploration; repeated action changes from fishing to digging in Dig it. Peaks differ greatly (Fish It 2,716,766 on 2025-12-07; Dig it 28,135 on 2025-02-01). Public counts cannot separate theme, quality, promotion, ownership, timing or live ops as cause | V-SAMP | S21 S22 | 163 |
| Reading the pair | Same structural family, very different outcomes; not a matched winner-vs-clone experiment. Fish It = major historical success by sampled audience. This Dig it universe = past audience, very low current activity; profitability, budget, reason for decline UNK. Not every low-CCU game is a commercial failure | OPN | S21 S22 | 165 |
| Grow a Garden 2 | Named by Roblox as a quickly growing Q2 2026 experience. Tracker: peak 929,371 CCU on 2026-06-19; recent seven-day peak 2,984. Description adds guild competition and night-time stealing. A twist can coincide with a big launch and still not hold peak-scale traffic; owner profit and full cause unavailable | V-OFF + V-SAMP | S55 S61 | 167 |
| Twist hypotheses (PROPOSAL) | Risky retrieval turns an idle collector's choice from waiting for income into how far it is safe to go. Cooperative survival turns linear accumulation into division of labour and shared failure. A good twist changes decisions, stakes, cooperation or expression; a new noun on the same assets and onboarding gives little reason to switch. Check by play and tests before claiming it is better | OPN | S16 S18 S19 S21 | 169 |
| Launch-lag record | "How fast did winners ship" is not the same as universe creation date, time between records, or dev duration. No exact lag evidence for the fishing pair. Record four fields apart: launch_date, predecessor_breakout_date, public_evidence_date, development_start. With gaps publish a bounded interval or UNKNOWN, never an invented "built in a week" | OPN | S13 S17a S21 | 171 |

## 14. Copying mechanics versus expression (RP:173-179)

| Topic | Content | Tag | S | RP |
| --- | --- | --- | --- | --- |
| Copyright (U.S.) | Game ideas and methods of play are not protected by copyright; expression such as art and text can be. Program copyright does not cover abstract algorithms, but that does not allow copying another developer's source | V-OFF | S27 S28 | 175 |
| Trademark (U.S.) | Names can be outside copyright yet raise trademark confusion. USPTO looks at confusion about source for related goods or services | V-OFF | S29 | 175 |
| Scope | U.S. baseline only; not clearance for a whole presentation, other jurisdictions, patents or contracts | V-OFF | S27-S29 | 175 |
| Roblox platform | Non-unique metadata and place files can get lower recommendation and search priority. IP guidelines allow removal and account action for repeated or serious infringement. Legal inspiration and discoverability are two separate tests. Altered spelling or "inspired by" grants no rights to characters, songs, graphics or code | V-OFF | S04 S30 | 177 |
| Originality checklist (PROPOSAL) | 1 independently made code and assets; 2 distinct title and thumbnails; 3 licensed music; 4 documented third-party asset licences; 5 a gameplay change visible in the first-session experience | OPN | S27-S30 | 179 |
| Licensing | Use IP License Manager or Catalog only when a licence for the property exists; check territory, term, revenue share, allowed content. A catalog is not a blanket licence for Squid Game, anime, Verity or memes | OPN | S27-S30 | 179 |
| Community dislike | May be studied with a disclosed sample of reviews or comments. No platform-wide numeric copying penalty from community sentiment was found | OPN | S27-S30 | 179 |
| Percentage | No safe percentage of copying established (RP:187) | V baseline / OPN | S27-S30 | 187 |

Source register and paper inconsistencies (I1-I26): [[reference/trends/01b-register-and-issues]].
