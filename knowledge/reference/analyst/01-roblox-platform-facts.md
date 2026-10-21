---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J013-T01, Roblox_Analyst_Research_2026.txt + local docs mirror + live checks 2026-10-21"
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · high · 2026-10-21

# Roblox platform facts for the analyst (fact-check of the analyst paper, R1-R21 and the Open Cloud APIs)

Scope: every Roblox analytics fact, limit, threshold, date and API detail the analyst paper (AP) states, checked against the docs mirror and live pages on 2026-10-21. Statistics methodology, studio-practice claims (I1-I12) and the paper's OPINION rows are not checked here. The paper stays outside git; this note paraphrases it.

## 1. How I checked (sources, tags, dates)

All reads on 2026-10-21. No verdict comes from memory. Quotes are 15 words or fewer. AP:n = line n of the paper file.

| Tag | Source | Note |
| --- | --- | --- |
| M | Mirror `knowledge/external/roblox-creator-docs/` (revision 7400643, refreshed 2026-10-20, `README.md:6-7`). Paths are relative to the mirror root. `PA/` = `production/analytics/`, `CG/` = `cloud/guides/`, `PE` = `production/experiments.md`, `PM/` = `production/monetization/` | Mirror pages carry no per-page date. The mirror has no `cloud/reference/features/*` pages (grep: no match for analytics-query-api in `cloud/reference/`) |
| L | WebFetch of the live create.roblox.com page (extract, small-model summary). URLs: `/docs/production/analytics` (+ `/analytics-dashboard`, `/retention`, `/acquisition`, `/performance`, `/feedback`, `/insights`, `/custom-dashboards`, `/funnel-events`, `/economy-events`), `/docs/production/experiments`, `/docs/production/monetization/price-optimization`, `/docs/production/monetization/paid-random-items`, `/docs/cloud/guides/analytics`, `/docs/cloud/guides/experiments`, `/docs/cloud/reference/features/{analytics,experiments,virtual-events}.md` (front matter last updated 2026-10-20T22:18:21Z), `/docs/cloud/reference/domains/apis`, `/docs/cloud/llms.txt` | Every L row says "extract". Where the mirror and L agree, I say so. L for the five dated posts below is the only evidence for post wording |
| DF | WebFetch extract of a DevForum post. DF-4907734 = `devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734` (R11). DF-4930122 = `.../improved-discovery-measurement-in-creator-analytics/4930122` (R18). DF-4549276 = `.../running-successful-experiments-insights-from-top-creators/4549276` (R19). DF-4865880 = `.../rdc26-what-we-announced/4865880` (R20). DF-4828676 = `.../new-opencloud-apis-for-analytics-events-experiments-and-thumbnail-personalization/4828676`. DF-3983866 = `.../day-7-retention-data-not-updating-since-september-30/3983866`. DF-4753664 = `.../open-cloud-analytics-query-api-is-live-beta-.../4753664` | I could not read the raw posts. Dates and authors come from the extracts |
| S | `.agents/skills/analytics/SKILL.md` (T-05, T-09..T-12) and `knowledge/reference/roblox/whats-new.md:132-140` | compared, not used as evidence |
| FC | `knowledge/reference/marketing/fact-check-roblox-discovery.md` (FD rows) | context only; each fact I use was re-read today |
| W | WebSearch | used only to find pages (two searches). No search summary is evidence |

Counts: 80 rows (59 RF + 21 register quotes). Confirmed 73, corrected 2 (RF-40, RF-44), unverified-kept-with-label 5 (RF-04, RF-57, R11, R18, R19 wording), dropped 0.

Verdicts: confirmed = the source says it. corrected = the paper's wording needs the fix shown. unverified-kept-with-label = could not be proven, kept with the label. dropped = removed. Source vocabulary: DOC = Roblox documentation, POST = Roblox DevForum announcement, COMMUNITY = non-Roblox post, INFERENCE = mine.

## 2. Notes: Roblox facts to use (paraphrased; corrected where the check says so)

### 2.1 Dashboards, eligibility, Open Cloud basics
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-01 | Full dashboard KPIs need more than 10 DAU and 10 play hours for 7 consecutive days. The page does not say whether "10 play hours" is per day or in total | 40 | VERIFIED |
| RF-02 | Client and server performance charts need at least 100 DAU. The header (current users, servers, device split) shows without it | 40 | VERIFIED |
| RF-03 | Creator Hub shows retention, engagement, acquisition, demographics, feedback, monetization KPIs, plus Economy and Funnel pages once events exist | 40 | VERIFIED |
| RF-04 | Blank or missing data has documented causes: recent D7/D30 days are empty until the window passes; crash-rate lines turn dashed at low session counts; export is blocked with no data. COMMUNITY: one tester saw no-activity days omitted from API output, not zero | 40 | VERIFIED |
| RF-05 | The Analytics Query API returns aggregated metrics over a date range with breakdown and filter by supported dimensions | 42 | VERIFIED |
| RF-06 | Key needs your experience in Access Permissions and `universe.analytics:read` in system `universe-analytics`; header `x-api-key` | 42 | VERIFIED |
| RF-07 | Buckets are UTC. `startTime` inclusive, `endTime` exclusive, any UTC offset accepted then normalized | 42 | VERIFIED |
| RF-08 | Most queries return 200 `done:true`; large ones return 202 `done:false` and a `path` to poll | 42 | VERIFIED |
| RF-09 | Data points can carry `status`: `Valid`, `Projected` (estimate, may change), `NotStatisticallySignificant`. Field is omitted when none applies | 42 | VERIFIED |
| RF-10 | A 200 with `Projected` is still an estimate (the paper's reading of RF-09) | 42 | VERIFIED |
| RF-11 | History per metric (not one number): 1468 days for most standard metrics, 28 days for performance, 30 days thumbnails, 90 days matchmaking, 365 days client-API-calls. The guide's "up to 4 years" is the approximate form. Over 2 years only OneWeek, OneMonth, None are allowed | 645 | VERIFIED |
| RF-12 | (extra) API is labelled Beta. Limits: 30 POST/min and 3000 GET-poll/min per API-key owner. A weekly DAU bucket counts distinct users, not a sum of days | - | - |

### 2.2 Retention definitions and maturity
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-13 | Retention charts are indexed by the cohort's first-play date. COMMUNITY (role unconfirmed): this switch was announced in July 2025, so older posts may assume return-date indexing | 57 | VERIFIED |
| RF-14 | D7 = return on the 8th day counting first-play day as day 1; D30 = the 31st. Example in the docs: cohort 06/20 shows D7 on 06/27 and D30 on 07/20 | 57 | VERIFIED |
| RF-15 | D7/D30 for recent cohorts are empty until the window has passed; compare cohorts of equal age | 19 | VERIFIED |
| RF-16 | Doc inconsistency persists today: Acquisition calls the D7 measure "the 8th day (D8) after their first session ended"; the Retention page says 8th day = Day 7; Retention intro and Experiments say "after 1 week" | 641 | VERIFIED |
| RF-17 | Acquisition 30-day revenue per user excludes subscriptions, engagement payouts and immersive ads | 641 | VERIFIED |
| RF-18 | (extra) Retention cohort table: daily cohorts show 10 days, weekly cohorts 10 weeks (Monday-Sunday). Per cohort: 7D playtime, 7D payer conversion, 7D and 30D revenue per user, all cumulative | - | - |

### 2.3 Benchmarks and peer band
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-19 | Peer set: players-similar games, else genre (if the game has one), else all experiences. Benchmark games have at least 100 DAU. Updated daily | 108 | VERIFIED |
| RF-20 | Displayed band is the 50th-90th percentile. Example: D1 12.11%-18.73% means 50% of similar games are at or below 12.11% and 10% at or above 18.73%. The example is illustrative | 108, 141 | VERIFIED |
| RF-21 | Peer benchmarks exist for: all retention KPIs, average session time, ARPPU, ARPDAU, payer conversion, play-through rate. Not for total playtime, sessions or CCU | 67-77 | VERIFIED |
| RF-22 | The chart gets an annotation when the game moves from one benchmark set to another | 120 | OPINION (uses a doc fact) |
| RF-23 | Roblox recommends D1 retention and average session time first, then D7/D30, then payer conversion and ARPPU. Benchmarks are not a direct discovery-algorithm signal | 18 | VERIFIED |
| RF-24 | (extra) A second benchmark family for "overall success" KPIs uses the top 1000 games by 30-day playtime (excluding games under 30 days) with Top 200/500/1000 tiers | - | - |

### 2.4 Engagement, monetization, acquisition
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-25 | Average session time = total time in game divided by number of sessions. API names: `AverageSessionLengthMinutes`, `Visits` (shown as "Sessions"), `TotalPlayTimeHours`, `AveragePlayTimeMinutesPerDAU` | 68-71 | VERIFIED |
| RF-26 | Payer conversion = share of DAU who are paying users. ARPPU = revenue per paying user. ARPDAU = revenue per DAU. The API metric `AverageRevenuePerUser` is the ARPDAU row | 75-77 | VERIFIED |
| RF-27 | Monetization page: revenue (hourly and daily, split by developer products, passes, commissions), conversion, paying users, ARPPU, ARPDAU | 200 | VERIFIED |
| RF-28 | Cohort revenue views are cumulative per new player: Retention page 7D and 30D, Acquisition 7D playtime, 30D payer conversion, 30D revenue | 78 | VERIFIED |
| RF-29 | Acquisition shows source-attributed users (Home recommendations, Continue, Today's Picks, Home other, Friends, Search, Charts, three ad types, Teleport, Other), play-through rate and a share-link funnel. "Other" includes external traffic | 88 | VERIFIED |
| RF-30 | Price optimization: needs about 60,000 transactions in the previous 30 days "in most cases" | 222 | VERIFIED |
| RF-31 | Managed pricing shows subsets of users different prices; applies prices only on positive incremental total revenue; re-tests at least every 90 days "or sooner". A test takes about 3 weeks; the review period is 4 weeks with 98% on new prices and 2% on originals | 222 | VERIFIED |
| RF-32 | Paid random items include indirect Robux-funded currency and probability modifiers. Odds must be shown as percentages summing to exactly 100%, with a documented rounding disclaimer. `PolicyService` gives `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed` per player | 226 | VERIFIED |

### 2.5 Performance, economy, funnels
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-33 | Client metrics break down by platform, OS, memory group, place, place version. Crash rate = crashes / ended sessions; at low volume the line is dashed and the crash count is the better read | 84-85 | VERIFIED |
| RF-34 | Out-of-memory chart may miss some crashes (telemetry limits) but is directionally accurate | 86 | VERIFIED |
| RF-35 | Server charts: CPU time, frame rate (cap 60), memory, memory by age, cores, compute efficiency; crash detail on its own page | 87 | VERIFIED |
| RF-36 | P10/P50/P90 exist for FPS, memory, memory percentage, CPU time, session duration, server frame rate, server memory. No percentiles for crash rate or crash count. History 28 days | 104 | VERIFIED |
| RF-37 | Peak CCU: `PeakConcurrentPlayers`, 28 days of history | 74 | VERIFIED |
| RF-38 | Economy page shows top sources, top sinks, average wallet balance (five charts, up to five currencies on the dashboard). Roblox heuristic: total sources minus total sinks should be close to zero; growing net means add sinks | 82, 200 | VERIFIED |
| RF-39 | Funnel page needs logged funnel events (up to 10 funnels). Only the first instance of a step counts; a skipped step auto-completes earlier ones; filters apply to step 1 only; funnels group by entry date; state expires after 180 days of silence | 80, 196 | VERIFIED |

### 2.6 Experiments and Early Harm Detection
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-40 | Experiments: in-game (config values) and matchmaking tests, 14-60 days. In-game: up to two variants plus control. Matchmaking: up to three variants, equal split, one running test per universe. Roblox recommends simple 50/50 on large rollouts | 243 | VERIFIED |
| RF-41 | MDE is computed from goal metric and players per variant (DAU, rollout, duration, split). An MDE above 100% means significance is unlikely. Under 1,000 DAU may be hard | 243 | VERIFIED |
| RF-42 | Tracked metrics: D1, D7, playtime, ARPU, ARPPU, payer conversion, session time. Playtime, ARPU, payer conversion, ARPPU, session time are cumulative over the experiment. Goal metric picks one of seven (no D30, no custom) | 243, 261 | VERIFIED |
| RF-43 | Targeting is re-evaluated each session. A player stays attributed to the enrolled arm after they stop matching, but the value stops being served | 243 | VERIFIED |
| RF-44 | EHD runs in the first 24 hours (or until first daily results), refreshing every 5 minutes, for **three metrics only**: playtime (-10%), ARPU (-20%), payer conversion (-20%). Retention, ARPPU and session time are not checked | 273 | VERIFIED |
| RF-45 | Critical harm needs the whole confidence interval below the threshold. The interval is one-sided (upper bound only) | 273 | VERIFIED |
| RF-46 | With under 10,000 players enrolled across the variant and the control, lift is shown but harm is not judged, so silence is not safety | 273, 625 | VERIFIED |
| RF-47 | EHD is for stopping early, not for launch decisions. Launch on daily results | 27, 273 | VERIFIED |
| RF-48 | SRM is checked every 5 minutes for 24 hours then daily; a banner appears; Roblox says stop and restart. Docs give no Roblox SRM p-value cutoff | 271 | VERIFIED |
| RF-49 | Roblox says to ignore changes that are not statistically significant; significance is "confidence interval does not overlap 0%" | 478 | VERIFIED |
| RF-50 | (extra) A config key is locked while its experiment runs; one active experiment per key. In-game experiments auto-complete 14 days after the decision date. EHD notifies by email, tray and optional webhook | - | - |

### 2.7 Feedback, AI reports, dashboards
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-51 | Feedback (Audience menu): CSV export, up/down ratings, device type, platform, comment | 346 | VERIFIED |
| RF-52 | Coverage: votes from 2025-02-01, comments from 2025-03-17. Ratings update at end of each day and can change. Filtered comments do not appear | 346 | VERIFIED |
| RF-53 | AI analytics reports need 1000+ DAU (weekly, monthly in first week); feedback reports need 20+ comments; page warns the AI can make mistakes. (extra) Insights panel needs 100+ DAU; models named: Gemini 2.5 and Llama 3 | 364 | VERIFIED |
| RF-54 | Custom dashboards: charts, tables, summary cards; published ones visible to anyone with analytics permission; saved only on Publish; up to 20 per experience | 434 | VERIFIED |

### 2.8 Discovery break, roadmap, creator report
| RF | Fact | AP | Tag |
| --- | --- | --- | --- |
| RF-55 | On 2026-10-12 Roblox moved Home, Search and Charts impression, click and play recording to a new delivery pipeline (fewer lost events on app close or crash) | 329 | VERIFIED |
| RF-56 | Expected: higher counts, PTR may dip slightly. Data before 2026-10-12 is unchanged. Roblox says: applied to all games at once, similar across games, no change to RFY ranking. Creator replies report PTR drops; no staff answer in the extract | 329 | VERIFIED |
| RF-57 | (inference) The break touches discovery-recorded counts and rates: acquisition impressions/clicks/plays and PTR. The post does not name retention, DAU or revenue | - | OPINION |
| RF-58 | RDC26 (2026-09-11) lists Observability Platform (trace client sessions and logs) and Early testing (up to 10 age-checked friends) for Late 2026; Test Teleports Early 2027. No analytics-agent, experiments or MCP item in the post | 331 | VERIFIED |
| RF-59 | Creator report 2026-03-31 (OrogeneIstari): over 1000 experiments in Q1 2026, nearly 1 in 4 with significant playtime lift, average detected positive lift about 5%. Case: Build a Crazy Tower (block pools) +50% payer conversion, +10% session time. Trolls cannot break this tower (free item at end of obby) +12.5% playtime, +5.3% D1. No baselines, no units | 132-134 | EXPERIENCE (cases), VERIFIED (aggregates) |

## 3. Fact-check table

M and L rows: "M" means mirror line, "L" means live extract read 2026-10-21, both agree unless stated. DF rows name the post and its date.

| RF | claim (short) | AP | checked against | verdict | corrected text or reason |
| --- | --- | --- | --- | --- | --- |
| RF-01 | >10 DAU, 10 play hours, 7 consecutive days | 40 | M `PA/analytics-dashboard.md:22`; L dashboard page | confirmed | "10 play hours" scope (per day or total) is not stated |
| RF-02 | performance charts need 100 DAU | 40 | M `PA/performance.md:24`; L performance page | confirmed | Applies to client and server charts; Client API calls metric is only for "a small number of top games" (:233) |
| RF-03 | Hub shows retention, engagement, acquisition, monetization, performance, economy, funnel | 40 | M `PA/analytics-dashboard.md:13-20`, `PA/economy-events.md:17`, `PA/funnel-events.md:17` | confirmed | Also demographics and feedback |
| RF-04 | blank chart is not zero | 40 | M `PA/retention.md:33`, `PA/performance.md:101`, `PA/analytics-dashboard.md:239`; DF-4753664 (2026-07-23, COMMUNITY) | unverified-kept-with-label | Paper's inference; docs give three causes. Omitted-day behavior in the API is one community tester's observation, not documented |
| RF-05 | API returns aggregated metrics; breakdown and filter | 42 | M `CG/analytics/index.md:11-15,69-79` | confirmed | |
| RF-06 | scope `universe.analytics:read` | 42 | M `CG/analytics/index.md:17`; L guide; L reference analytics page | confirmed | Experiments and Events use other scopes (RF-40 row in section 4) |
| RF-07 | UTC buckets, inclusive start, exclusive end | 42 | M `CG/analytics/index.md:75-76,190`; L guide | confirmed | |
| RF-08 | asynchronous operations | 42 | M `CG/analytics/index.md:88-104`; DF-4828676 (2026-08-24) | confirmed | Poll with GET; see section 4 |
| RF-09 | statuses Projected, NotStatisticallySignificant | 42 | M `CG/analytics/index.md:180-186` | confirmed | Third value `Valid` |
| RF-10 | success does not finalize an estimate | 42 | M `CG/analytics/index.md:185` | confirmed | Follows from `Projected` |
| RF-11 | 28 days performance, 1468 days standard; guide approximates | 645 | M `CG/analytics/metrics.md:21-260` (per row), `CG/analytics/index.md:81-86,205`; L guide | confirmed | Adds exceptions: thumbnails 30 d (:161-166), matchmaking 90 d (:193-203), `RotraceTotalCalls` 365 d (:112). 4 years = 1461 days, so 1468 is slightly more (arithmetic) |
| RF-12 | (extra) Beta label, rate limits, weekly distinct | - | L `/cloud/reference/features/analytics.md` (2026-10-20 update stamp); M `CG/analytics/index.md:408`; DF-4753664 | confirmed | Rate limits come only from the live reference page (extract); the mirror lacks it. DF-4753664 (COMMUNITY) repeats 30 and 3000 |
| RF-13 | cohort indexed by first play date | 57 | M `PA/retention.md:24`; L retention page; DF-3983866 reply 2025-10-08 | confirmed | The reply's author role is not shown, so July 2025 change date is COMMUNITY |
| RF-14 | D7 = 8th day, D30 = 31st | 57 | M `PA/retention.md:126,152,33`; L retention page | confirmed | Chart text also says "after 1 week" (:29). Calendar vs 24-hour day, and which timezone, is not stated |
| RF-15 | immature D7/D30 empty | 19, 620 | M `PA/retention.md:33`; L | confirmed | |
| RF-16 | D7 vs "8th day (D8)" label | 641 | M `PA/acquisition.md:115`, `PA/retention.md:126`; L acquisition page | confirmed | Inconsistency persists live 2026-10-21. Treat first-play date as day zero; verify against a known cohort |
| RF-17 | 30D revenue excludes subs, payouts, immersive ads | 641 | M `PA/acquisition.md:127`; L | confirmed | |
| RF-18 | (extra) cohort table sizes | - | M `PA/retention.md:47-61`; L | confirmed | |
| RF-19 | fallback order; >=100 DAU; daily | 108 | M `PA/analytics-dashboard.md:246-252`; L | confirmed | Genre only if the game has an internal genre label |
| RF-20 | 50th-90th; D1 example illustrative | 108, 141 | M `PA/analytics-dashboard.md:265-268`; L | confirmed | |
| RF-21 | which KPIs have peer benchmarks | 67-77 | M `PA/analytics-dashboard.md:258-263` | confirmed | Matches the paper's PEER rows. LOCAL rows (sessions, total playtime, CCU) have no peer band |
| RF-22 | annotation on benchmark transition | 120 | M `PA/analytics-dashboard.md:254` | confirmed | |
| RF-23 | recommended order; benchmarks not a direct discovery signal | 18, 102 | M `PA/index.md:19-27,68`; L analytics overview | confirmed | |
| RF-24 | (extra) top 200/500/1000 tiers | - | M `PA/analytics-dashboard.md:272`; L | confirmed | |
| RF-25 | session time definition; API names | 68-71 | M `PA/engagement.md:26`; `CG/analytics/metrics.md:34-40` | confirmed | |
| RF-26 | conversion, ARPPU, ARPDAU defs; metric names | 75-77 | M `PA/monetization.md:29-32`; `CG/analytics/metrics.md:48-53` | confirmed | Doc defines ARPPU only by its name; "in the metric's period" is the paper's gloss |
| RF-27 | monetization page contents | 200 | M `PA/monetization.md:26-32` | confirmed | |
| RF-28 | cohort revenue cumulative | 78 | M `PA/retention.md:56-61`, `PA/acquisition.md:119-127` | confirmed | |
| RF-29 | acquisition sources, PTR, share links | 88 | M `PA/acquisition.md:28-90,173-178`; L | confirmed | Paper lists no sources; this list is the doc's |
| RF-30 | 60,000 transactions / 30 days | 222, 235 | M `PM/price-optimization.md:18`; L | confirmed | "in most cases" is the doc's hedge |
| RF-31 | managed pricing mechanism, 90 days | 222 | M `PM/price-optimization.md:31-35,78,124-136`; L | confirmed | Paper omits "or sooner when prices may no longer be optimized" |
| RF-32 | paid random items rules | 226, 236 | M `PM/paid-random-items.md:11-14,47,55,72-75,83-130`; L | confirmed | Page shows no date |
| RF-33 | client FPS dims; crash rate | 84-85 | M `PA/performance.md:40-44,101`; `CG/analytics/metrics.md:104-106` | confirmed | API crash metric is `ClientCrashRate15m`; the "15m" is not explained in the docs |
| RF-34 | OOM incomplete | 86 | M `PA/performance.md:78`; L | confirmed | |
| RF-35 | server metrics | 87 | M `PA/performance.md:111-143`; `CG/analytics/metrics.md:113-117` | confirmed | |
| RF-36 | P10/P50/P90 where supported | 104 | M `PA/performance.md:34-38`; `CG/analytics/metrics.md:106-118` | confirmed | Percentile metrics are marked per row; crash metrics have none |
| RF-37 | peak CCU metric | 74 | M `CG/analytics/metrics.md:111` | confirmed | 28 days only |
| RF-38 | Economy view; sources vs sinks | 82, 200 | M `PA/economy-events.md:11-17,121-123`; L | confirmed | Paper's OPINION (positive net is not automatically inflation) is stricter than Roblox's heuristic; see section 5 |
| RF-39 | Funnel view and its semantics | 80, 196 | M `PA/funnel-events.md:17-19,107,128,134,140,142`; L | confirmed | Skipped-step rule can inflate early-step completion if steps are skipped |
| RF-40 | experiments types, 14-60 d, variants, 50/50 | 243 | M `PE:11,22-25,34,48,58,89`; `CG/experiments.md:265-271`; L experiments page | corrected | In-game only: "two variants plus control". Matchmaking allows up to three (`PE:89`). The live extract did not repeat the matchmaking limit; the mirror is explicit |
| RF-41 | MDE and 1,000 DAU | 243 | M `PE:316`; L | confirmed | Goal metric is also an MDE input |
| RF-42 | native metrics; no D30 | 243, 261 | M `PE:105-115`; `CG/experiments.md:251-261` | confirmed | Cumulative scope per metric; D1 and D7 are for new players |
| RF-43 | targeting per session | 243 | M `PE:156-163`; L | confirmed | "Cumulative conversion is not daily dashboard conversion" is the paper's inference from "cumulative for the duration" (:114); kept as INFERENCE |
| RF-44 | EHD window, refresh, thresholds | 273 | DF-4907734 (2026-10-01, quazotheduck); M `PE:105,245,261-265`; L experiments page | corrected | Add: only playtime, ARPU, payer conversion are monitored (`PE:107-115` Early harm column). The paper's "ARPU/payer conversion" thresholds are right |
| RF-45 | whole interval below threshold | 273 | DF-4907734; M `PE:251` | confirmed | One-sided interval (no lower bound) during the early window |
| RF-46 | 10,000 across control and variant | 273 | DF-4907734; M `PE:259`; L | confirmed | Per comparison; lift still shown |
| RF-47 | stop early, not launch | 27, 273 | DF-4907734; M `PE:255` | confirmed | |
| RF-48 | SRM cadence; no Roblox cutoff | 271 | M `PE:287-289`; DF-4907734 | confirmed | Docs state no numeric SRM threshold. API stats show only `isSrmDetected` |
| RF-49 | ignore non-significant | 478 | M `PE:325,279` | confirmed | Roblox: ignore. Paper (ASA) disagrees; see section 5 |
| RF-50 | (extra) lock, auto-complete, notifications | - | M `PE:123,154,167,269`; DF-4907734 | confirmed | |
| RF-51 | feedback features | 346 | M `PA/feedback.md:36,73-78,92`; L | confirmed | |
| RF-52 | feedback coverage dates | 346 | M `PA/feedback.md:14,60,78`; L | confirmed | |
| RF-53 | AI reports thresholds | 364 | M `PA/insights.md:13,34,38,68,71,88`; L | confirmed | Models named in the page may change |
| RF-54 | custom dashboards | 434, 441 | M `PA/custom-dashboards.md:11,17,30-34,63-66`; L | confirmed | |
| RF-55 | 2026-10-12 pipeline change | 329, 621 | DF-4930122 (2026-10-12, itsblueberrycoffee) | confirmed | Extract |
| RF-56 | higher counts, lower PTR, history unchanged | 329 | DF-4930122 | confirmed | Extract. Ranking and benchmark statements are Roblox's; thread complaints are creators' |
| RF-57 | which metrics the break touches | - | DF-4930122; `CG/analytics/metrics.md:61-68` | unverified-kept-with-label | INFERENCE. Post names impressions, clicks, plays on Home, Search, Charts only |
| RF-58 | RDC26 observability and early testing, Late 2026 | 331, 340 | DF-4865880 (2026-09-11, skywise84) | confirmed | Extract. Roadmap, not shipped |
| RF-59 | creator report figures and cases | 132-134, 142 | DF-4549276 (2026-03-31, OrogeneIstari) | confirmed | Extract. Relative or percentage-point: the post does not say, as the paper warns |

Register quote check (the paper's "key quote" per source). Mirror line or post extract. Exact wording of posts cannot be proven from an extract.

| RQ | quote found | checked against | verdict | note |
| --- | --- | --- | --- | --- |
| R1 | yes | M `PA/index.md:23` | confirmed | |
| R2 | yes | M `PA/analytics-dashboard.md:265` | confirmed | |
| R3 | yes | M `PA/retention.md:24` | confirmed | |
| R4 | yes | M `PA/engagement.md:26` | confirmed | |
| R5 | yes | M `PA/monetization.md:29` | confirmed | |
| R6 | yes | M `PA/acquisition.md:176` | confirmed | |
| R7 | yes | M `PA/performance.md:30` | confirmed | |
| R8 | yes | M `PA/economy-events.md:13` | confirmed | |
| R9 | yes | M `PA/funnel-events.md:11` | confirmed | |
| R10 | yes | M `PE:34` | confirmed | |
| R11 | claim yes, wording not provable | DF-4907734 extract: "only meant to help you decide whether to stop" | unverified-kept-with-label | Meaning confirmed; the register's exact sentence not seen |
| R12 | yes | M `CG/analytics/index.md:11` | confirmed | |
| R13 | yes | M `CG/analytics/metrics.md:103` ("Data retention: 28 days") | confirmed | |
| R14 | yes | M `PM/price-optimization.md:18` | confirmed | |
| R15 | yes | M `PM/paid-random-items.md:55` | confirmed | |
| R16 | yes | M `PA/feedback.md:60` | confirmed | |
| R17 | yes | M `PA/insights.md:88` | confirmed | |
| R18 | claim yes, wording not provable | DF-4930122 extract: pre-change data "is not being changed" | unverified-kept-with-label | Meaning confirmed |
| R19 | not checked word for word | DF-4549276 extract | unverified-kept-with-label | Figures confirmed (RF-59) |
| R20 | yes | DF-4865880 extract: "Observability Platform (Late 2026)" | confirmed | |
| R21 | yes | M `PA/custom-dashboards.md:11` | confirmed | |

## 4. Open Cloud for the tool

All endpoint, scope and limit facts below are DOC unless marked. Mirror = `CG/analytics/index.md` (called IDX) and `CG/analytics/metrics.md` (called MET). Reference = live `cloud/reference/features/*` pages read 2026-10-21 (extract; the mirror does not have them).

### 4.1 Analytics Query API
| Item | Fact | Source |
| --- | --- | --- |
| Status | Beta (4 endpoints). Auth: API key or OAuth 2.0 | Reference analytics page; `/cloud/reference/domains/apis` (extract) |
| Metrics query | `POST https://apis.roblox.com/analytics-query-api/v1/universes/{UniverseId}/metrics` | IDX:33 |
| Dimension values | `POST .../v1/universes/{UniverseId}/dimension-values`; body `metric`, `dimensions` (array), `startTime`, `endTime` required; `filter`, `granularity`, `limit` optional | IDX:291-326 |
| Auth | Header `x-api-key`; permission `universe.analytics:read` in system `universe-analytics`; experience in Access Permissions | IDX:17 |
| Request fields | `metric`, `granularity`, `startTime`, `endTime` required; `breakdown` (string array), `filter` (objects: `dimension`, `values`, `operation`), `limit` optional. Values are case-sensitive | IDX:69-79; MET:11 |
| Time | RFC 3339; start inclusive, end exclusive; any offset, result buckets are UTC; `OneDay` runs UTC midnight to midnight | IDX:75-76,190 |
| Granularity | `OneMinute`, `HalfHour` (performance only); `OneHour` (performance plus some monetization and recommended-events metrics); `OneDay` (all); `OneWeek`, `OneMonth`, `None` (most engagement, monetization; the catalog rows decide). Ranges over 2 years: only `OneWeek`, `OneMonth`, `None` | IDX:194-206 |
| Filter operations | `In`, `NotIn`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`, `Match` | IDX:279-287 |
| `limit` | Caps breakdown series, ranked by total descending. Only valid with `granularity:"None"` and `breakdown` set. Omitted or 0 applies a metric-dependent default cap | IDX:79,426-440 |
| History | Standard metrics "up to 4 years" (use per-metric days in 4.2); performance 28 days. Too early a `startTime` returns 400 code 2001 | IDX:81-86 |
| Long-running | 200 with `done:true`, or 202 with `done:false` and `path`. Poll `GET https://apis.roblox.com/analytics-query-api/{path}` with the same key until `done:true`. Reference path: `/v1/universes/{universeId}/operations/metrics/{operationId}` (dimension values: `.../operations/dimension-values/{operationId}`). Failure arrives as `done:true` with `error{code,message}` | IDX:88-157,328; reference page |
| Data point | `time` (UTC bucket start), `value`, `stringValues` (text metrics, e.g. `ThumbnailWinningSegments`; `value` then meaningless), `status` (`Valid`, `Projected`, `NotStatisticallySignificant`; omitted if none). Breakdown entries: `dimension`, `value` (use in filters), `displayValue` (optional) | IDX:157-186,246-252 |
| Rate limits | POST metrics 30/min, POST dimension-values 30/min, GET operation polls 3000/min each. Per API-key owner (all keys of one owner share it) and per OAuth authorization | Reference page (extract); `cloud/reference/rate-limits.md:56` |
| Errors | 400/2001 bad field, bad granularity, bad dimension, `startTime` beyond retention. 401 (no body) key missing, invalid or lacking permission (reference page says 403 for missing scope: unresolved). 404 operation id unknown. 429/3000 data point budget exceeded: shorten range, coarser granularity, use `limit`. 500/2000 retry, then DevForum post. 503/2002 transient: retry after a short delay. 504/1000 timed out: shorter range, fewer breakdowns | IDX:517-532; reference page |
| Retry advice | For 429 rate limits: Roblox's rate-limit page says read `retry-after`, else exponential backoff; the analytics reference page says start at 1 s. Headers `x-ratelimit-limit/remaining/reset` appear on many responses | `cloud/reference/rate-limits.md:29-68`; reference page |
| Data point budget | Number not documented anywhere I read (mirror, live guide, live reference). Only the 429/3000 error exists | IDX:529 |
| Data lag | Not documented. A staff reply (2026-09-01, fbttz) says teams are tuning pipelines to cut lag and looking at an endpoint for data landing times | DF-4828676 (extract) |
| Date semantics of `Forward*` retention | Not documented. "Forward" and the dashboard's first-play-date indexing suggest the value sits on the cohort's first-play date (INFERENCE). Test with a known cohort before relying on it | MET:21-23 |
| Adjacent | Alerts API (`universe.analytics.alert:read/write`, 30 days of incidents) is separate | `CG/alerts/index.md:11-30` |

### 4.2 Supported metrics catalog (every metric in MET)
Dimension sets (names exact, case-sensitive). SEG6 = UserSegmentationAccountAge, UserSegmentationActivationStatus, UserSegmentationEngagementLevel, UserSegmentationPayerStatus, UserSegmentationPlatformActivationStatus, UserSegmentationPlatformSpenderStatus. U13 = AgeGroupV2, Country, Gender, Locale, OperatingSystem, Platform, UserO18Eligibility + SEG6. A8 = AcquisitionSource, AgeGroupV2, Gender, IsNewUser, OperatingSystem, Platform, UserSegmentationPlatformActivationStatus, UserSegmentationPlatformSpenderStatus. PC = MemoryGroup, OperatingSystem, Place, PlaceVersion, Platform. ECO = AgeGroup, CurrencyType, CustomField1-3, Gender, IsNewUser, OperatingSystem, PayerStatus, Platform. FUN = AgeGroup, CustomField1-3, FunnelName, FunnelStep, Gender, IsNewUser, OperatingSystem, PayerStatus, Platform. Note `AgeGroupV2` vs `AgeGroup`, and `PayerStatus` vs `UserSegmentationPayerStatus`: they differ by family. Type: std = standard, perf = performance and stability, other.

| Metric name(s) | Type | Granularities | Breakdown dimensions | Retention | Notes | MET line |
| --- | --- | --- | --- | --- | --- | --- |
| `ForwardD1Retention`, `ForwardD7Retention`, `ForwardD30Retention` | std | OneDay | U13 + AcquisitionSource | 1468 d | one metric per day-N; date semantics see 4.1 | 21-23 |
| `DailyCohortRetention` | std | None, OneDay | U13 minus UserO18Eligibility, + AcquisitionSource, CohortDay | 1468 d | | 24 |
| `WeeklyCohortRetention` | std | None, OneWeek | same as above with CohortWeek | 1468 d | | 25 |
| `DauMauStickiness` | std | OneDay | U13 | 1468 d | | 26 |
| `AveragePlayTimeMinutesPerDAU`, `AverageSessionLengthMinutes`, `MonthlyActiveUsers`, `TotalPlayTimeHours`, `Visits` | std | OneDay, OneWeek, OneMonth, None (`MonthlyActiveUsers`: OneDay only) | U13 + IsNewUser | 1468 d | `Visits` = "Sessions" | 34,35,37,38,40 |
| `DailyActiveUsers` | std | OneDay, OneWeek, OneMonth, None | U13 + IsNewUser + AcquisitionSource | 1468 d | weekly bucket = distinct users (IDX:408) | 36 |
| `TotalSessionsEndedInBucket` | std | OneDay, OneWeek, OneMonth, None | AgeGroupV2, Gender, OperatingSystem, Platform, SessionTimeBucket, SEG6 | 1468 d | "new user first session retention" | 39 |
| `AverageRevenuePerPayingUser`, `AverageRevenuePerUser` (ARPDAU), `PayingUsers`, `PayingUsersCVR` | std | OneDay, OneWeek, OneMonth, None | U13 | 1468 d | | 48,49,52,53 |
| `DailyRevenue` | std | OneDay, OneWeek, OneMonth, None | U13 + BalanceType, RevenueSource | 1468 d | Robux | 50 |
| `ItemMonetizationRevenue` | std | OneHour, OneDay, None | CollectibleItemTargetType, CollectibleItemTargetTypeId, CollectibleItemType, ProductKey, ProductType, SalesLocation | 1468 d | "Robux Spent (Realtime)" | 51 |
| `ClickCVR`, `EndToEndCVR`, `ImpressionCVR`, `QualifiedEndToEndCVR`, `UniqueUsersWithClicks`, `UniqueUsersWithImpressions` | std | OneDay, None | A8 | 1468 d | affected by the 2026-10-12 pipeline change (inference) | 61-64,66,67 |
| `QualifiedUniqueUsersWithPlaySessions`, `UniqueUsersWithPlaySessions` | std | OneDay, None, OneWeek | A8 + FunnelSource | 1468 d | | 65,68 |
| 20 RFY signals: `RFYPlayThroughRate`, `RFYDuration0To60`, `RFYDuration61To180`, `RFYD2To7PlayDays`, `RFYD8To28PlayDays`, `RFYD1Playtime`, `RFYD2To7Playtime`, `RFYD8To28Playtime`, `RFYD1CoplayDays`, `RFYD2To7CoplayDays`, `RFYD8To28CoplayDays`, `RFYD1QualifiedPlaySessions`, `RFYD2To7QualifiedPlaySessions`, `RFYD8To28QualifiedPlaySessions`, `RFYD1SpendDay`, `RFYD2To7SpendDays`, `RFYD8To28SpendDays`, `RFYD1RobuxSpend`, `RFYD2To7RobuxSpend`, `RFYD8To28RobuxSpend` | std | OneDay | AgeGroupV2, Gender | 1468 d | Home recommendation signals; only RFY-sourced users (discovery doc) | 76-95 |
| `ClientCpuTimeAvg` | perf | OneMinute, HalfHour, OneHour, OneDay | PC + ClientCpuTimeCategory, ClientCpuTimeSubCategory | 28 d | | 103 |
| `ClientCrashCount`, `ClientCrashRate15m`, `OomUnexpectedExits`, `PeakConcurrentPlayers` | perf | OneMinute, HalfHour, OneHour, OneDay | PC | 28 d | no percentile variants | 104,105,110,111 |
| `ClientFps{Avg,P10,P50,P90}`, `ClientMemoryUsage{Avg,P10,P50,P90}`, `ClientMemoryUsagePercentage{Avg,P10,P50,P90}`, `SessionDurationSeconds{Avg,P10,P50,P90}` | perf | OneMinute, HalfHour, OneHour, OneDay | PC | 28 d | session time here is seconds, 28 d; do not mix with `AverageSessionLengthMinutes` | 106-108,118 |
| `CpuCoreUtilization` | perf | OneMinute, HalfHour, OneHour, OneDay | Place | 28 d | | 109 |
| `RotraceTotalCalls` | perf | OneDay, OneHour, None | SimplifiedUrl | 365 d | "Client API calls in first 60s"; top games only | 112 |
| `CpuTime{Avg,P10,P50,P90}` | perf | OneMinute, HalfHour, OneHour, OneDay | CpuTimeCategory, CpuTimeSubCategory, Place | 28 d | server CPU | 113 |
| `ServerCrashCount` | perf | OneMinute, HalfHour, OneHour, OneDay | CrashType, Place | 28 d | | 114 |
| `ServerFrameRate{Avg,P10,P50,P90}` | perf | OneMinute, HalfHour, OneHour, OneDay | Place | 28 d | | 115 |
| `MemoryUsage{Avg,P10,P50,P90}` | perf | OneMinute, HalfHour, OneHour, OneDay, None | MemoryUsageCategory, MemoryUsageSubCategory, Place, ServerAgeBucket | 28 d | listed twice (by age, and plain) with identical names and dimensions | 116,117 |
| `EconomyAverageWalletBalance` | std | OneDay, OneHour, OneWeek, OneMonth, None | ECO | 1468 d | | 126 |
| `EconomyTransactionAmount`, `EconomyTransactionCount` | std | OneDay, OneHour, OneWeek, OneMonth, None | ECO + FlowType, ItemSku, TransactionType | 1468 d | | 127,128 |
| `FunnelCohortCompletionRate`, `FunnelCohortSessionCompletionRate` | std | OneDay | FUN | 1468 d | | 136,137 |
| `FunnelStepChurnRate`, `FunnelStepCompletionRate`, `FunnelStepOverallCompletionRate`, `FunnelStepTotalCount`, `FunnelUserChurnRate`, `FunnelUserOverallCompletionRate`, `FunnelUserStepCompletionRate`, `FunnelUserTotalCount` | std | None | FUN | 1468 d | `FunnelStep*` counts sessions, `FunnelUser*` counts users; step ids are dynamic (two-request pattern, IDX:464-515) | 138-145 |
| `CustomEventAvgPerUserValue`, `CustomEventAvgValue`, `CustomEventCount`, `CustomEventCountUser`, `CustomEventMaxValue`, `CustomEventMinValue`, `CustomEventSumValue` | std | OneDay, OneHour, OneWeek, OneMonth, None | AgeGroup, CustomEventName, CustomField1-3, Gender, IsNewUser, OperatingSystem, PayerStatus, Platform | 1468 d | | 153 |
| `ThumbnailAverageSessionLengthMinutes`, `ThumbnailImpressions`, `ThumbnailL7QualifiedPTR`, `ThumbnailQualifiedPTR`, `ThumbnailQualifiedPlays`, `ThumbnailWinningSegments` | other | OneDay, OneHour, None | ThumbnailAsset, ThumbnailList | 30 d | `ThumbnailWinningSegments` is text (`stringValues`) | 161-166 |
| `SpeechToTextTranscriptionStatuses`, `SpeechToTextTranscriptionUsage` | other | OneMinute, HalfHour, OneHour, OneDay | SpeechToTextTranscriptionStatus | 28 d | | 174,175 |
| `TextToSpeechAssetSuccesses`; `TextToSpeechRawAudioErrors`, `TextToSpeechRawAudioSuccesses` | other | OneMinute, HalfHour, OneHour, OneDay | none; TextToSpeechRawAudioStatus | 28 d | | 183-185 |
| Matchmaking: `MatchmakingCategoricalCustomSignalsSimilarityRatio{Avg,P10,P50,P90}`, `MatchmakingNumericCustomSignalsDifference{Avg,P10,P50,P90}` | other | OneHour, OneDay, None | AgeGroup, Locale, MatchmakingCategoricalCustomSignal or MatchmakingNumericCustomSignal, Place, Platform | 90 d | | 193,194 |
| Matchmaking signals: `MatchmakingSignalsAgeDifference`, `...CommonChatGroupRatio`, `...CommonDeviceTypeRatio`, `...CommonLanguageRatio`, `...EstimatePing`, `...OccupancyRatio`, `...PlayHistoryDifference`, `...VoiceChatRatio` (each Avg, P10, P50, P90), `MatchmakingSignalsPreferredPlayerMatchRatioAvg` | other | OneHour, OneDay | AgeGroup, Country, Locale, Place, Platform | 90 d | | 195-203 |
| Data Store: `DataStoreConsumed{List,Read,Remove,Write}Requests`, `DataStore{List,Read,Remove,Write}Requests`, `DataStore{List,Read,Remove,Write}RequestsByEndpoint`, `DataStoreRequests`, `DataStoreRequestsByEndpoint`, `DataStoreRequestsByStatus`, `DataStoreStorageUsageBytes` | other | OneMinute, HalfHour, OneHour, OneDay | DataStoreRequestSource, DataStoreTypeV2, DataStoreOperation, DataStoreStatus (varies per row) | 28 d | | 211-226 |
| Memory Stores: `MemoryStoreMemoryUsageBytes`, `MemoryStoreRequestUnitsByEndpoint`, `MemoryStoreRequests`, `MemoryStoreRequestsByEndpoint`, `MemoryStoreRequestsByStatus` | other | OneMinute, HalfHour, OneHour, OneDay | MemoryStoreOperation, MemoryStoreStatus (varies) | 28 d | | 234-238 |
| Safety: `TotalAbuseReports`, `UniqueAbuseReportSubmittersPer1000PlaytimeHours` | std | OneDay | AbuseCategory, AbuseChannel | 1468 d | | 246,247 |
| Ads: `AdsPublisherReportingTotalImpressions`, `AdsPublisherReportingTotalRevenueRobux`, `AdsPublisherReportingVideo2DEpmNoUnvalidatedPc`, `AdsPublisherReportingVideo2DImpressions`, `AdsPublisherReportingVideo2DRevenueRobux` | other | OneDay, OneHour, None | AdFormat, AdInstanceName, AdPlacementId, AdsPublisherReportingDataVersion, Country, Gender, OperatingSystem, Platform (+ AdRewardId, PlacementType on video rows) | 1468 d | | 255,256,258-260 |
| `AdsPublisherReportingVideo2DDailyUniqueViewer` | other | OneDay, None | as ads + PlacementType | 1468 d | | 257 |

The guide's granularity table says OneWeek, OneMonth and None work for "most ... acquisition" metrics; the catalog allows them only for the two play-session acquisition metrics. The catalog wins.

### 4.3 Experiments API (read side) and Events API
| Item | Fact | Source |
| --- | --- | --- |
| Status, auth | All 11 Experiments endpoints Experimental. API key (`x-api-key`) or OAuth 2.0 | Reference experiments page (extract, updated 2026-10-20) |
| Base | `https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{universeId}` | `CG/experiments.md:55,115` |
| Scopes | Read (Get, List, stats) `universe:read`; write (Create, Update, Discard, Start, Schedule, Complete) `universe:write`. `calculateMde` needs read | `CG/experiments.md:18`; reference page |
| Rate limits | Reads 100/min, writes 10/min per key owner and per OAuth authorization | Reference page (extract) |
| List | `GET .../experiments?maxPageSize=20&skip=0&sortKey=LIST_EXPERIMENT_SORT_KEY_RELEVANCE&sortOrder=SORT_ORDER_DESCENDING`; rows are `ExperimentSummary` (id, name, state, timestamps, product type) plus `total` | `CG/experiments.md:231-239` |
| Get | `GET .../experiments/{experimentId}` returns the full experiment with variants and configuration; `variantMeta.variantId` is assigned once running | `CG/experiments.md:197,241-247` |
| Stats | `GET .../experiments/{experimentId}/stats`: only after 24 hours of running; async; the documented field is `experimentStats.isSrmDetected` | `CG/experiments.md:172-191` |
| Results and goal metrics | No endpoint for per-metric lift, interval or significance is documented in the guide. The reference page lists "diagnostic stats" only; its `operation` field is untyped (`any`). DF-4828676 (extract) mentions "results retrieval". Treat result retrieval as unverified and test with a real key | `CG/experiments.md:249-263`; reference page; DF-4828676 |
| Goal metric enum | `UNIVERSE_EXPERIMENT_METRIC_` + `AVERAGE_SESSION_TIME`, `PLAYTIME_PER_USER`, `DAY_1_RETENTION`, `DAY_7_RETENTION`, `PAYER_CONVERSION_RATE`, `AVERAGE_REVENUE_PER_USER`, `AVERAGE_REVENUE_PER_PAYING_USER` | `CG/experiments.md:253-261` |
| States | `EXPERIMENT_STATE_DRAFT`, `_SCHEDULED`, `_RUNNING`, `_COMPLETED` (reference extract also names a discarded `Deleted` state). The UI's "Decision needed" is not in the documented enum | `CG/experiments.md:139,168,229`; `PE:119-127` |
| Async operations | Mutating calls return `operation{operationId,status,done}`. Poll `GET .../operations/{operationId}` until `done:true`. Success carries `experiment`; failure carries `error{errorType,errorCode,errorMessage}`. Example poll interval 2 s (guide), 1 s up to 30 tries (DF-4828676) | `CG/experiments.md:26-40,98-106` |
| MDE | `POST .../experiments:calculateMde`, returns an async operation; request schema not documented | Reference page |
| Limits | 14-60 days; 1 baseline + up to 2 treatments (in-game); 1 running matchmaking experiment per universe | `CG/experiments.md:265-271` |
| Events API (Game Events) | What it is: create, get, list, update, delete scheduled game events under `https://apis.roblox.com/virtual-events/v3` (`/universes/{universeId}/game-events`, `/game-events/{eventId}`). Experimental. Scopes `universe.event:read/write`. Limits 100/min reads, 20/min writes. Response has no RSVP, view or attendance numbers (only the caller's own RSVP status) | DF-4828676 (2026-08-24); reference virtual-events page (extract) |
| Does Events add read data? | No analytics numbers. It only gives the event calendar (start, end, visibility). Use it to mark event dates when explaining a change. Event statistics (views, visit rate, unfollow rate) stay in Creator Hub | reference page; FC FD-56 |
| Thumbnail Personalization | Separate Experimental API; its metrics are in the catalog (30 days) | DF-4828676; MET:161-166 |

## 5. Disagreements

| Kind | Disagreement | Resolution |
| --- | --- | --- |
| paper vs docs | RF-40: "two variants plus control" is in-game only; matchmaking allows three | Use the doc split |
| paper vs docs | RF-44: paper never says EHD watches only playtime, ARPU and payer conversion | Say it in the skill: no EHD flag says nothing about D1, D7, ARPPU or session time |
| paper vs docs | RF-11: paper says 28 days and 1468 days; docs add 30, 90 and 365 days for some metrics | Use per-metric retention (4.2) |
| paper vs docs | RF-31: paper omits "or sooner" on the 90-day re-test | Add it |
| paper vs docs | RF-49 and AP:478: Roblox says ignore non-significant changes; the paper prefers interval and margin reasoning | Roblox's text is a platform instruction; paper's resolution is analytic advice (statistics agent's area) |
| paper vs docs | RF-38: Roblox says sources minus sinks should be near zero; paper (OPINION, AP:208-210) says positive net flow is not automatically inflation | Both can hold: Roblox gives a balance heuristic, the paper warns against calling it inflation. Report the doc heuristic as Roblox's, not as a law |
| paper vs docs | RF-16: D7 wording differs across pages (8th day, D8, after 1 week), same on mirror and live | Keep the paper's rule; verify with a known cohort (06/20 -> 06/27 example) |
| docs vs skill | T-10 cites "DF 4907734 (2026-09)". The post is dated 2026-10-01; whats-new:138 calls it "rolling out, 2026-09-28 week". Post says it "just launched" 2026-10-01 | Fix the date; status = launched on 2026-10-01 (extract) |
| docs vs skill | T-11: "Analytics Query, Events and Experiments APIs ... key scoped `universe.analytics:read`". Only the Analytics Query API uses that scope. Experiments use `universe:read/write`; Events use `universe.event:read/write`. "Agents can read results": experiment results are not a documented read endpoint, only stats with the SRM flag; Events returns no metrics | Rewrite T-11 from section 4. APIs are Beta/Experimental, with the rate limits in 4.1 and 4.3 |
| docs vs skill | T-12: "retention, playtime, crashes and client CPU on the Performance page". Retention is on the Retention page; Place Version breakdown covers client performance metrics only (`PA/performance.md:40-44`) | Reword |
| docs vs skill | T-05 "10 economy currencies" is the event limit (`PA/event-types.md:100`); the Economy dashboard shows up to five currencies (`PA/economy-events.md:121`) | Both true; skill should say which |
| docs vs skill | T-09 "baseline + up to 2 variants" holds for in-game only (see RF-40) | Add the matchmaking case if matchmaking is ever used |
| mirror vs live | Mirror lacks the three `cloud/reference/features/*` pages; rate limits, stability labels, `calculateMde` and 11 experiment endpoints exist only live | Re-read the live pages when the tool is built; refresh the mirror if it should hold them |
| mirror vs live | Live extract of `/docs/production/experiments` omitted the matchmaking variant limit and said duration was stated for in-game only; the mirror states both | Extract artifact (small-model summary); mirror is the raw text |
| mirror vs live | Analytics guide says 401 for a key without permission; the reference page says 403 means missing scopes | Unresolved; the tool should treat 401 and 403 as an auth error and read `error.message` |
| mirror vs live | Everything else I compared (eligibility, benchmark rules, retention wording, EHD, price optimization, paid random items, feedback, insights, funnel, economy, custom dashboards, analytics guide, experiments guide) matched | none |

## 6. Dropped claims with reasons

None dropped. Nothing in the paper's Roblox facts was contradicted outright. Kept with a label: RF-04 (blank is not zero: paper's inference, partly documented), RF-57 (which metrics the 2026-10-12 break touches: inference), R11, R18, R19 register wording (meaning confirmed, exact sentence not provable from an extract). Not checked on purpose: the paper's OPINION rows, I1-I12, S1-S8.

Also open (not in the paper): the data point budget number, API data freshness, `Forward*` date semantics, whether experiment per-metric results can be read through the API, and the 401 vs 403 question. Each needs a test with a real owner-made key, or a staff answer.
