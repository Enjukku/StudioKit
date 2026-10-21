# Metrics on Roblox: what each number means and how to read it

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-design`. Sources: owner's analyst paper (AP), fact-checked in `knowledge/reference/analyst/01-roblox-platform-facts.md` (RF ids, Roblox docs mirror rev 7400643 + live reads 2026-10-21) and `03-practice-diagnosis-reporting.md` (PR ids). Tags: **V** documented platform fact · **E** someone's reported result, never a target · **O** the paper's or studio's practice. Roblox pages change: re-read the live page when a decision depends on a fact older than a month.

## 1. The metric contract (write it before any number)
Every number we report carries seven labels (O, AP:38; PR-R03). Plain form for the owner: *what we counted, out of whom, which days, which players, which version of the rule.*

| Label | Example |
| --- | --- |
| decision | "keep or revert the new tutorial" |
| unit | player · session · attempt · transaction · server (a returning player makes many sessions: they are not independent people) |
| eligible population | new players on phones in the US, first play 2026-10-01..07 |
| window | UTC dates, start inclusive, end exclusive (V, RF-07) |
| numerator / denominator | returned on day 7 / cohort size |
| definition version | Roblox metric name + our event version + measurement breaks crossed |
| source | pull id or dashboard export + pulled-at time (UTC) |

Arithmetic traps (O, AP:55): sum counts before computing a ratio; never average daily percentages without their denominators; summed DAU is player-days, not unique players (a `OneWeek` DAU bucket from the API *is* distinct users: V, RF-12); peak CCU is an instant maximum, not DAU. The identities playtime = sessions × mean session length and revenue = active players × payer share × revenue per payer hold only for the same population, period and revenue scope; they describe composition, not cause.

## 2. Roblox metrics the analyst reads
API names are exact and case-sensitive (catalog with granularities, dimensions and history: `knowledge/reference/analyst/01-roblox-platform-facts.md` §4.2).

| Question | Metric (API name) | Definition and traps | Peer band? | Src |
| --- | --- | --- | --- | --- |
| Do players come back? | `ForwardD1Retention`, `ForwardD7Retention`, `ForwardD30Retention`; `DailyCohortRetention`, `WeeklyCohortRetention` | Indexed by first-play date. D7 = return on the 8th day counting the first-play day as day 1; D30 = the 31st (docs example: cohort 06/20 → D7 on 06/27, D30 on 07/20). A return *on that day*, not "any time in the week". Recent cohorts are empty until the window passes. The Acquisition page still labels the same idea "8th day (D8)": a doc wording clash, not a different metric. The API's date for `Forward*` values is undocumented (probably the first-play date): confirm with one known cohort before trusting it. The API gives rates without cohort counts: estimate counts per `analysis-craft/references/data-tools.md` §4 and label them | yes | V RF-13..16; RF-11 §4.1 |
| How long do they stay? | `AverageSessionLengthMinutes` (total time ÷ sessions), `AveragePlayTimeMinutesPerDAU`, `TotalPlayTimeHours`, `Visits` (shown as "Sessions") | Session length can fall because many new players arrived, not because the game got worse. Performance `SessionDurationSeconds*` is a different metric (seconds, 28-day history): never mix them | session time yes; playtime, sessions no | V RF-21, RF-25 |
| How many play? | `DailyActiveUsers` (+ `IsNewUser`, `AcquisitionSource`), `MonthlyActiveUsers`, `DauMauStickiness`, `PeakConcurrentPlayers` | Keep new, active and returning-after-a-gap players apart: a reactivation spike is not better onboarding (O, AP:95) | no | V RF-25, RF-37 |
| Who pays, how much? | `PayingUsersCVR` (paying users ÷ DAU), `AverageRevenuePerPayingUser` (ARPPU), `AverageRevenuePerUser` (= ARPDAU), `PayingUsers`, `DailyRevenue` (Robux; by `RevenueSource`) | Robux, not cash, not DevEx. Higher ARPPU can mean small spenders left. Acquisition's 30-day revenue excludes subscriptions, engagement payouts and immersive ads: reconcile scope before comparing | conversion, ARPPU, ARPDAU yes | V RF-17, RF-26..28 |
| Where do they come from? | Acquisition page; `UniqueUsersWithImpressions`, `ImpressionCVR`, `ClickCVR`, `EndToEndCVR`, `UniqueUsersWithPlaySessions` (+ `AcquisitionSource`) | Sources: Home recommendations, Continue, Today's Picks, Friends, Search, Charts, ads, Teleport, Other (Other includes outside links). **2026-10-12 break**: Home, Search and Charts impressions, clicks and plays moved to a new recording pipeline; counts rise, play-through rate may dip; earlier data unchanged. Never compare across that date as if it were player behaviour | PTR yes | V RF-29, RF-55..57 |
| How does it run? | `ClientFps{Avg,P10,P50,P90}`, `ClientMemoryUsage*`, `ClientCrashRate15m` (crashes ÷ ended sessions), `ClientCrashCount`, `OomUnexpectedExits`, `ServerFrameRate*`, `CpuTime*`, `MemoryUsage*`, `ServerCrashCount` (by `Platform`, `OperatingSystem`, `MemoryGroup`, `PlaceVersion`) | **28-day history only**: our pulls are the long record. Read the low tail (P10 FPS) and high tail (P90 memory), not the average: an average can improve because weak phones stopped coming. At low volume the crash rate is noisy; read the count. OOM telemetry misses some crashes. Charts need 100+ DAU | no | V RF-02, RF-33..36 |
| Is the currency healthy? | `EconomyTransactionAmount`, `EconomyTransactionCount` (+ `FlowType`, `CurrencyType`, `TransactionType`, `ItemSku`), `EconomyAverageWalletBalance` | Needs economy events (the `analytics` skill). The dashboard shows up to 5 currencies. Roblox's heuristic "sources minus sinks near zero" is Roblox's balance hint, not a law: a positive net flow is not automatically inflation (see `diagnosis.md` §4) | no | V RF-38; O AP:208 |
| Where do they stop? | `FunnelUser*` (players) and `FunnelStep*` (sessions): `TotalCount`, `CompletionRate`, `OverallCompletionRate`, `ChurnRate`; `FunnelCohort*` | Needs funnel events. Only the first instance of a step counts; a skipped step auto-completes earlier ones; filters apply to step 1 only; funnels group by entry date; step ids are dynamic (discover first, 90-day lookback). A funnel shows *where*, never *why* | no | V RF-39 |
| Anything else we log | `CustomEvent{Count,CountUser,SumValue,AvgValue,AvgPerUserValue,MinValue,MaxValue}` | No percentiles or distributions from the dashboard | no | V catalog |
| What do players say? | Audience → Feedback CSV (votes from 2025-02-01, comments from 2025-03-17; filtered comments absent; ratings change daily) | A reviewer filter, not the player base (see `diagnosis.md` §6) | no | V RF-51..52 |

Not readable through the API: Roblox's own AI analytics and feedback reports (1000+ DAU; 20+ comments) — they "can make mistakes": leads to check, never evidence (V RF-53).

## 3. When numbers exist at all
| Gate | Rule | Src |
| --- | --- | --- |
| Main dashboard KPIs | more than 10 DAU and 10 play hours for 7 days in a row | V RF-01 |
| Performance charts | 100+ DAU (the header shows without it) | V RF-02 |
| Benchmarks | peer games need 100+ DAU | V RF-19 |
| AI reports | 1000+ DAU weekly; feedback report 20+ comments | V RF-53 |
| Experiments | 14-60 days; under about 1,000 DAU useful results may be hard (the MDE at setup tells) | V RF-40..41 |
| API history | most standard metrics 1468 days; performance 28 days; thumbnails 30; matchmaking 90 | V RF-11 |
| Blank chart or missing day | not zero: a window not yet passed, too few sessions, or a day with no activity omitted by the API | V RF-04 |
| Point status | `Projected` = estimate that may change; `NotStatisticallySignificant` = too few players for a reliable value. Show both labels; never treat as final | V RF-09..10 |

## 4. Benchmarks: what "good" means
- Roblox compares the game with similar games (by player overlap, else genre, else all games; peers have 100+ DAU; updated daily) and shows the **50th-90th percentile band** (V RF-19..20). Benchmarks exist for retention, session time, conversion, ARPPU, ARPDAU and play-through rate, not for playtime, sessions or CCU (V RF-21).
- The docs' D1 example band (12.11%-18.73%) is an illustration, never a target (V RF-20).
- **No public table of good / average / weak values by genre and game age exists** (O, AP:110; checked). Do not borrow mobile-game numbers, DevForum anecdotes or a screenshot from another game. The right answer is "unknown publicly; here is this game's current peer band" (O, AP:619).
- Report the raw value next to the band, the read date and the pool. Save the band with each pull: a band change caused by a new peer pool is not a change in player behaviour (O, AP:120).
- Plain labels for the owner (studio convention, O): below the band's bottom = "weaker than most similar games: worth a look"; inside = "typical to strong"; at or above the top = "among the best 10% of similar games on this number". None of these says the game is healthy or broken.
- Creator case uplifts (Build a Crazy Tower +50% payer conversion; Trolls cannot break this tower +12.5% playtime, +5.3% D1; Roblox: ~1 in 4 of 1000+ Q1-2026 experiments had a significant playtime lift, average detected positive lift ~5%) are **E**: no baselines, no units, selected winners. Never a forecast for our test (RF-59).
- Game age and player age differ. A new game's first fans and an old game's survivors are both unlike the next cohort. A marketing push can lower the retention *rate* while raising the retained *count*: report both (O, AP:136).

## 5. What to watch first
Roblox's order: D1 retention and average session time first, then D7/D30, then payer conversion and ARPPU (V RF-23).

| Game state | Order (O, AP:93-97; PR-W01..04) |
| --- | --- |
| New game | players can join and the game runs → the first session delivers the activity the page promised → the core loop is understood and completed → D1 → progression and D7. Record purchase delivery and economy integrity from day one. Buying traffic before the first session works mainly buys more evidence of the same problem |
| Live game | service health and logging every pull → comparable retention cohorts → who is playing (new / active / returning) → content use → economy stocks and flows → payer breadth → revenue quality |

## 6. Measurement breaks (mark every one on charts and in reports)
| Date | What changed | Effect | Src |
| --- | --- | --- | --- |
| 2025-07 (community report) | retention charts indexed by first-play date | older posts may mean return-date indexing | RF-13 (role unconfirmed) |
| 2026-10-12 | discovery impressions, clicks, plays on Home, Search, Charts: new pipeline | higher counts, PTR may dip, history unchanged, RFY ranking unchanged (Roblox) | V RF-55..56 |
| our own | every event version change, logging bug, new funnel numbering | a version boundary with a comparability note | O, AP:377 |

Roadmap items (RDC 2026: Observability Platform, Early testing, "Late 2026") are announcements, not tools we have (V RF-58).
