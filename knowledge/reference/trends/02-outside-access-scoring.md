---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J004
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source: `Roblox_Trend_Scout_Research_2026.txt`, lines 189-491 (sections 3-10 and the open questions) plus register entries (lines 498-646) for the cited S-ids. Paraphrased; the paper stays outside git. Held out by order (ticket J004-T02): the timing-table rows, one "already too late" paragraph, the dated candidate example with its rule table, and one rule row that repeats a held-out number. They are not in this file.

# Trend scout research, part 2 (paper lines 189-491): outside trends, access, timing, scoring, report

Reading rule: keep the tag beside every claim. VERIFIED official = a platform's own document or counter. VERIFIED sampled = a third party's repeated reading of public counters (gaps, not the true peak). VERIFIED third-party model = a vendor estimate. VERIFIED secondary = a later account of an earlier event. EXPERIENCE = a practitioner's report. OPINION = the paper's proposal, never a platform rule and never a measurement. derived = arithmetic done on dated inputs. PROPOSAL = a number or cut-off the owner has not confirmed. Cite as `RP:<line>` plus the paper's own S-id. "Check" = a possible paper problem; nothing was fixed. Paper cutoff date 2026-10-20 (RP:494). An access date is not a publication date (RP:494, 496).

## 1. Transmission chain and date kinds (RP:191)

| item | content | tag |
| --- | --- | --- |
| Chain | source release -> repeat creators/remixes -> search curiosity -> Roblox search and prototypes -> sustained play -> optional money/retention confirmation | OPINION S32-S34, S56 |
| Direction | Both ways. Roblox play can make the clips that grow the outside meme | OPINION |
| Order vs cause | Earlier outside date is necessary for a lead signal; it does not prove cause | OPINION |
| Five dates, never merged | announced; released; first observed; broke out; peaked | OPINION |

## 2. Outside-trend cases (RP:193-199, 211-214)

All lags below are calendar-day differences. Every lag is an upper bound on when an adaptation became visible. None is a launch lag, a peak lag or a lead-time distribution.

| case | dated facts (source) | derived lag | what may be said | what may not be said | tag | RP |
| --- | --- | --- | --- | --- | --- | --- |
| Squid Game | Netflix release 2021-09-17 (S32; announcement publish date not established). Developer update log with a working minigame sequence, posted 2021-09-30 06:22 UTC (S33) | 2021-09-30 - 2021-09-17 = 13 days | Theme adaptations can become visible fast: at most 13 days to that dated update | First adaptation; time to peak; player counts (S33 is a developer post, not a measurement) | VERIFIED primary + derived | 195, 211 |
| Italian brainrot -> ownership economy | GMA article 2025-05-16, says origin was early 2025 (S34a; no first-post proof). Steal a Brainrot universe created 2025-05-16 (S17, Rolimon's table). Roblox later confirms a record of more than 25 million concurrent in Sep 2025 (S56, published 2025-12-16) | none. Origin to creation is "several months", no exact day | Broad ordering only | Exact day lag; public breakout date; first playable date (need stronger evidence) | VERIFIED contemporary account + official/sampled | 196 |
| Verity (fan song, remixes, Roblox adaptations) | Series debut 2026-05-30 and fan song 2026-07-10 and July/August spread (Know Your Meme, S34b-S34c; KYM entry added/updated 2026-08-26). Fan song over 17 million views in about a month. Remix on July 22 reached nine million views in four days (RP:201). Roblox game video date shown 2026-07-25 (S34d, third-party record) | series -> video: 2026-07-25 - 2026-05-30 = 56 days. Song -> video: 2026-07-25 - 2026-07-10 = 15 days | Cross-platform wave documented by the cutoff | Game launch lag; live official view series (counts are retrospective third-party captures) | VERIFIED secondary + derived | 197, 201, 212 |
| Bruno Mars concert inside an existing hit | Event 2026-01-17 in Steal a Brainrot. Guinness record published 2026-02-06: 12,862,161 concurrent viewers (S34e) | none | A concert can activate players already inside a game | Retention or revenue lift (none shown); enduring demand | VERIFIED record authority | 198, 213 |
| Online/PC horror -> Roblox | Historical 2024 guide calls a dusty trip Roblox's answer to The Long Drive (S40; exact day unknown). Dead Rails (S23) has a similar expedition-survival structure | none | Design migration happened (guide) / similar structure (paper's own comparison) | A lead-time distribution; first-inspiration date; developer intent | EXPERIENCE contemporary coverage / OPINION structure | 199, 228 |

Verity identity note (VERIFIED secondary S34b-S34c, RP:201): the evidence concerns a Minecraft horror character/web series linked to ThatMob and a Horror Skunx fan song. It does not show a child creator. A different channel with the same name exists. Write down the exact channel ID or handle before monitoring. Verity is a documented cross-platform wave by the cutoff, so it is not an undiscovered August-to-October find (OPINION S34b-S34d, RP:205). An original "helpful companion turns unreliable" mechanic can be tested without the character, name, song or copied scenarios. A claim of a fresh Verity sub-trend needs a new dated growth series and a clearance path.

Creator, song and rights rules (OPINION S34b-S34e, RP:203):

| rule | detail |
| --- | --- |
| Creator roster | Watch channels popular with the intended audience. Do not infer individual viewers' ages. Do not collect children's personal data |
| Track | topic repeats across channels; new derivatives; play requests |
| Songs | Recording rights, composition rights, remix rights and gameplay use are four separate things. A sound's popularity in a social app gives no Roblox music licence |
| Real-world events | Same demand tests and same content/IP review. A public event does not by itself make a playable opportunity |
| Name ambiguity | Exact channel ID required; age unknown (OPINION S34b, S41; RP:214) |

Channel roles (OPINION S41-S45, RP:207): TikTok/Reels show remixable hooks. YouTube shows lasting formats and explainable play. Twitch shows live spectator appeal. Discord gives permissioned community feedback and announced updates. Reddit gives discussion among its own audience. No one audience stands for all Roblox users. Hashtag size is neither Roblox demand nor product-market fit.

## 3. Steam and PC (RP:218-235)

| topic | fact | tag | S | RP |
| --- | --- | --- | --- | --- |
| Top Sellers | Real-time ranking of revenue from base games, DLC and in-game purchases. Trailing 24 hours, extra weight on the last 3 hours. Global and country lists differ; a logged-in user's preferences can change the display. A free-to-play game can lead. A rank change is ordinal: no dollar growth from it without more data | VERIFIED official (docs undated, accessed 2026-10-20) | S36 | 218, 232 |
| Current players | Web API method GetNumberOfCurrentPlayers returns current players of an app. Public vs partner methods differ | VERIFIED official | S37 | 220 |
| Wishlists | Authorized Steamworks accounts see their own sales/wishlist reports. A rival's exact wishlist total is not generally public. Keep four things apart: public wishlist rank, follower counts, developer-stated totals, third-party estimates. Never multiply followers by a fixed factor and call it official wishlists | VERIFIED official scope / OPINION | S38 | 220, 233 |
| SteamDB | FAQ forbids scraping/crawling and points to Steam itself. A partnership/API route is described as prospective, not an open public API. Manual viewing where allowed, Valve sources or a licensed feed only. A public chart is not a licence to scrape | VERIFIED service policy (accessed 2026-10-20) | S39 | 222, 234 |
| Weekly PC scan | Split released games, demos, upcoming titles. Capture per title: revenue rank; mean CCU over 24 h and 7 d where available; dated demo/release; recent review increments; patch and promo calendar; number of different broadcasters. Leave out sale-driven re-entries unless demand also lasts. Demo = low-friction interest; wishlist = intent; paid sale = spending; continuing concurrency = play. None alone proves Roblox fit | OPINION | S36-S40 | 224 |
| Next Fest | Gives an earlier read of mechanics than waiting for a paid hit. Record what demo mechanics people repeat and share; whether solo or group play is the draw; whether a smaller Roblox version works with touch and short onboarding. Do not add demo CCU to full-game CCU without checking app IDs. Use the official festival calendar, not a search result's "live now" label, as the date authority | OPINION (Next Fest page live/undated) | S38, S40 | 226 |
| PC -> Roblox lag | No universal lag is verified. Other hypotheses to test with paired launch/observation histories: co-op expedition horror, physical teamwork, escalating survival runs | OPINION | S36, S40 | 228, 235 |

## 4. Mobile (RP:239-254)

| topic | fact | tag | S | RP |
| --- | --- | --- | --- | --- |
| Apple | RSS feed builder: pick storefront, feed, limit, format. Generate from Apple's current builder. Do not trust an old blog endpoint or an old "top grossing" feed | VERIFIED official | S46 | 239 |
| Google Play | Public games and storefront pages with top charts. Discovery surface, not a per-game revenue ledger | VERIFIED official | S47 | 239 |
| Rank context | Country, platform and category go with every rank | OPINION | S46-S47 | 239 |
| Vendor data | Sensor Tower says it mixes panel, first-party and public data and models population behaviour. Estimates are not full counts. Terms condition access/downloads on strict compliance with the contract and give no guarantee. data.ai is named among services in its current terms. Two products in that group are not independent proof until shared inputs are checked. Current price: UNKNOWN. Per-game error percentage: UNKNOWN | VERIFIED vendor description (terms: June 2026 per search metadata, day unknown) | S48 | 241, 253 |
| Panel design | Fixed storefront/category panel: new entries, rank persistence, country breadth, rating-count increments, age rating, visible controls, update history, licensed download/revenue estimates. Daily rank panel, 7-day and 28-day histories (PROPOSAL) | OPINION | S46-S48 | 243, 251 |
| Rank math | Rank 100 -> 10 = 90 positions, not +900% downloads | OPINION (arithmetic) | S46-S47 | 243, 252 |
| Separate quantities | installs; active players; total store consumer spending; developer receipts; advertising revenue | OPINION | S46-S48 | 243 |
| TikTok Top Ads | Selection of creatives the advertisers authorized. Count distinct advertisers, recurring mechanics, first/last seen, localization. A creative running 30 days is not proof of positive return on ad spend. Store the advertised action apart from the real gameplay | VERIFIED official scope + OPINION | S42, S43, S48 | 245, 254 |
| Translating a mobile loop | Translate the mechanic, not an assumed business model (a single-player ad-funded loop may need co-op or progression on Roblox). Do not forecast Roblox income from mobile revenue per download, an App Store rank, or a publisher's company revenue. Before comparing a vendor estimate with disclosed receipts, reconcile store fees, taxes, refunds, web payments and ads | OPINION | S07, S48 | 247 |

## 5. Social, search and community (RP:258-274, 278-282)

| source | facts and rules | tag | S | RP |
| --- | --- | --- | --- | --- |
| YouTube quotas | Default 100 search.list calls/day plus a separate 10,000 units/day for other endpoints (upload quota irrelevant here). Old advice "search costs 100 of 10,000 units" does not match the retrieved overview; re-read the real project quotas. Public statistics can be fetched. Search returns a selected set, not every upload | VERIFIED official (page-update date not established) | S41 | 258, 278 |
| YouTube panel | Fixed documented query/channel panel. Topic search with publishedAfter/publishedBefore and type=video. Known channels via uploads playlists. Deduplicate video IDs. Statistics in supported batches. Save query language, country, window, rank/pagination. Report counts as "observed uploads in this panel", never platform supply. View increments = same-source arithmetic; watch time and audience age are different and not obtainable this way | OPINION | S41, S35 | 260, 282 |
| View velocity | For a permitted fixed video cohort: velocity = added views / elapsed hours (input: view counts at two timestamps; unit views per hour). Compare the recent window with the equal window before it. Add the median of age-matched videos next to totals. Old videos can gain views with no new creators. Track unique participating channels and concentration. Get any needed analytics permission before custom channel scores or heavier derived metrics. A channel's usual baseline helps read an outlier. Public views show neither unique people nor Roblox conversion | OPINION | S35, S41 | 262 |
| YouTube policy | The 2026-09-14 guide allows simple arithmetic using only YouTube API data and bars some inferences. Extra metrics/storage need an audited developer with explicit approval. Accepted statistics/derived values may be kept up to 36 months. Other cached data: refresh or delete, generally after 30 calendar days. This paper does not grant the exception | VERIFIED official policy | S35 | 264, 279 |
| TikTok Creative Center | Hashtag trendline, related videos, audience and regional data; described as free and public. Hashtag lifetime views are stock, not velocity. A big sound can be falling. Prefer measured additions, wider creator spread, persistence beyond one account. Split sound IDs/remixes carefully: equal titles do not mean the same sound. Manually record country and window | VERIFIED official (S42) + OPINION | S42 | 266, 268 |
| TikTok Research API | Research Tools FAQ answers "No" for commercial users. New videos can take up to 48 hours to appear; statistics up to 10 days to update. Display API covers authorized accounts, not global topic search. Not an early-warning feed even if access existed | VERIFIED official | S49 | 266, 280 |
| Instagram | Docs not retrieved. No hashtag cap and no global sound-data right certified. Manual shortlist or approved Graph features only | OPINION / UNKNOWN | none | 268, 318, 488 |
| Google Trends | UI shows relative interest 0-100, not search counts. Official API: application-gated alpha in the retrieved docs, rolling five years, regular aggregations, consistently scaled, not absolute counts. The line "no official Trends API" is obsolete. An alpha is not general production access | VERIFIED official status (blog 2025-07-24; docs undated) | S50, S51 | 270, 281 |
| Trends method | Same geography, search type, category, interval. UI: rerun the whole comparison window or use a documented anchor. Zero can mean too little volume. Topic entity vs text term: compare on purpose ("Fisch" is not "Fish"). Plot rise speed and geographic breadth apart. A doubled index is not doubled searches. "Breakout" gives no absolute size | OPINION | S50, S51 | 272 |
| Twitch Helix | Top games and streams (Client ID + OAuth). Sample streams to add viewer-hours and count broadcasters; separate event/raid spikes from lasting category growth. Category viewers do not name a universe: need reliable stream metadata or permitted manual classification | VERIFIED official scope + OPINION | S44 | 274 |
| Reddit, Discord | Use only inside their access terms. A quiet subreddit or private server is no proof of low Roblox demand | OPINION | S45 | 274 |
| Report honesty | Sampled upload counts are not a topic census | OPINION | S41 | 282 |

## 6. Legal and reliable access (RP:286-292, 296, 325, 329-332)

| rule | detail | tag | S | RP |
| --- | --- | --- | --- | --- |
| Source-permission registry (before any schedule) | 12 fields per source: owner; route; approved purpose; commercial permission; AI/runtime permission; retention/deletion terms; redistribution; credential scope; quota; cost cap; effective date; last verification | OPINION | S11, S12, S31, S35, S39, S45 | 286 |
| HTTP 200 | Proves the page opened, not that use is allowed. A paid scraper/proxy gives no upstream rights | OPINION | | 286 |
| Blocked source | Report it, use a permitted substitute. Never bypass logins, CAPTCHA or rate limits. Roblox cloud APIs: expect and handle HTTP 429; stability guarantees are minimal | OPINION + VERIFIED official | S11, S12 | 286, 514-516 |
| Roblox terms caveat | The retrieved terms page says effective 2026-11-01 and adds limits on Virtual Content and AI use. At the cutoff it is future-effective, so it cannot alone prove the October contract. The earlier text was not resolved. Review counter/API access and Virtual Content intake separately against the terms in force. No blanket AI-scraping permission is certified | VERIFIED page observation (retrieved 2026-10-20) | S31 | 288, 331 |
| Reddit | Commercial API use needs a separate agreement. The wiki's 100 queries per minute (eligible OAuth clients) is not commercial approval | VERIFIED official (revision date not established) | S45 | 290, 330 |
| Discord | Policy forbids mining/scraping. Message content for model training needs express permission. A server invite or an admin's willingness is not a waiver | VERIFIED official policy (revision date not established) | S45 | 290 |
| Human research notes | Keep source reference and permission scope; no bulk comment import. No person-directed messages, no automatic solicitation. Owner exports via the studio process; aggregates only. Default to published docs/news, authorized owner analytics, licensed datasets | OPINION | S35, S45 | 292 |
| Public page | Public access is not blanket automated-use permission; permission and retention fields per route | OPINION | S31, S35, S39, S45 | 329 |
| AI ingestion vs training | Keep separate; no universal permission inferred | OPINION | S31, S35, S45 | 332 |
| Buying data | Start with free/authorized counters, official releases, manual dashboards, a small repeatable panel. Buy only once you can show which missing field would change a decision, and export, history and AI rights are confirmed. Monthly cap and human review. No guessed prices; need a dated current quote | OPINION | S35, S42, S48 | 325 |

## 7. Data-source table (RP:298-323), all six paper columns

Cadences are proposed, not provider promises. "$0 public" = no source-access charge established for that public surface; it excludes staff, hosting, other subscriptions and any commercial licence. "Quote" = price not verified, which does not mean free. If automation is unresolved: permitted manual work, or leave the source out (RP:296).

| Source (S-id) | What it shows | Official or estimate | How to access | Cost | How often to check | RP |
| --- | --- | --- | --- | --- | --- | --- |
| Roblox Games API (S01-S02) | players now, cumulative counters, metadata | Official counters | Listed API routes; review terms and rate limits | $0 public route; compute extra | Proposed every 5-15 min for a watchlist; daily broad scan | 300 |
| Roblox Charts (S05-S06) | scale, trending engagement, earning rank | Official ranks; some formulas unresolved | Public pages / permitted UI; do not invent an undocumented chart API | $0 public | Daily; annotate events | 301 |
| Creator Hub analytics (S07) | true owned-game cohorts, money, acquisition | Official permissioned telemetry | Authorized dashboard/export/API where granted | No separate dashboard price established | Daily; weekly cohort review | 302 |
| Roblox docs/news/RDC/IR (S03-S04, S13-S15, S54-S55) | discovery, economics, rules, dated cases | Official claims/disclosures | Public docs, news, filings | $0 public | Weekly; at once on policy releases | 303 |
| Rolimon's (S08, S16-S24) | recorded CCU peaks and history | Public counters sampled by a third party; playtime estimated | Public pages; get permission/licence for bulk recurring use | Public viewing $0; automation terms not verified | Daily review; do not assume a licensed bulk API | 304 |
| RoTrends (S53) | emerging experiences, comparison | Third-party observations/models | Public service; verify current plan/export access | Unknown current plan price | Daily if permitted | 305 |
| RoVitals (S25-S26, S60, S62) | growth, daily sampled curves, scenario income | Third-party sampled; modeled income | Public pages; verify recurring automated rights | Public viewing; data-feed terms unknown | Daily leads; verify on another source | 306 |
| GameAnalytics (S10) | benchmarks of selected large games | Vendor instrumented sample | Public report; own SDK telemetry if installed | Report public; other products: verify plan | On report release; quarterly context | 307 |
| Steam charts (S36) | revenue ranks and concurrent scale | Official | Store charts; permitted collection | $0 public | Daily; separate weekly chart | 308 |
| Valve Web API (S37) | current players, news | Official | api.steampowered.com documented interface | No fee established; real quota/terms govern | Proposed every 15-60 min for a shortlist | 309 |
| Steamworks (S38) | own wishlists/sales; festival rules | Official permissioned | Studio partner account; public docs/calendar | Account/product conditions apply | Weekly; daily during relevant demo events | 310 |
| SteamDB (S39) | historical CCU/ranks | Third-party recorded | Permitted manual use; partnership inquiry for data | Public viewing; contracted access unknown | Weekly manual; no scraping | 311 |
| Apple RSS/store (S46) | storefront chart lists, app metadata | Official ranking, not income | Current official feed builder | $0 public feed; no SLA established | Daily per fixed country panel | 312 |
| Google Play (S47) | chart/category pages, visible metadata and install bands | Official public presentation | Public UI; no verified unrestricted competitor analytics API | $0 public UI | Daily; licensed feed for repeat bulk work | 313 |
| Sensor Tower incl. contracted data.ai scope (S48) | downloads, spending, ads, usage estimates | Third-party models | Licensed UI/API/export with permitted AI use | Sales quote; not verified | Daily shortlist; weekly export | 314 |
| YouTube Data API (S41) | publish timestamps, public video statistics | Official counters; search = sampled discovery | Project credentials; approved use; current quota | No per-call price established within default quota | Daily; extra checks on shortlisted videos | 315 |
| TikTok Creative Center (S42-S43) | trending hashtags/sounds, selected ads | Official dashboard, selected coverage | Public dashboard / approved export workflow | Described as free | Daily country/window review | 316 |
| TikTok Research Tools (S49) | archived research dataset | Official dataset, restricted access | Not open to this commercial scout | Not an available studio route | Do not use as default pipeline | 317 |
| Instagram public trends / approved Graph features (no S-id) | selected posts, reels, hashtag signals | Official counters if provided; limited coverage | Approved app/permissions or permitted manual review | Access and current scope unverified | Daily manual shortlist; no assumed global sound API | 318 |
| Twitch Helix (S44) | live streams, viewers, category spread | Official snapshots | Client ID + OAuth; current headers and scope | No per-call price established | Proposed hourly shortlist | 319 |
| Google Trends (S50-S51) | relative search interest, related topics | Official sampled/normalized index | UI export; alpha application if approved | Public UI $0; alpha price/SLA not established | Daily fast trends; weekly slower terms | 320 |
| Reddit (S45) | selected discussions, engagement | Official counters within approved scope | Commercial agreement / authorized API, or permitted manual reading | Negotiated commercial access; no public fixed price | Weekly; no bulk without licence | 321 |
| Discord (S45) | permissioned community announcements/feedback | Community statements, not a market census | Approved bot/use case and permissions; no scraping | Implementation cost; scope-specific | Daily, authorized announcements only | 322 |
| Netflix / rights-holder calendars (S32) | announced release dates, official properties | Official calendar/news | Public news; licence catalogue / rights holder | Public news $0; IP deal variable | Weekly upcoming-event horizon | 323 |

### Access terms per source (from the same paper lines; UNKNOWN = the paper does not say)

Class = extractor's four-way map: OFF official; 3P-S third-party sampled; 3P-E third-party estimate/model; MIX more than one. Paper cell wording stays the authority.

| Source | class | allowed | not allowed / limits | auth | quota | storage limit | cost status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Roblox Games API | OFF | listed routes, after terms review | undocumented routes; AI/Virtual Content use not certified (S31 future-effective) | UNKNOWN for public routes | public batch limits UNKNOWN (RP:480); expect HTTP 429 (S12) | UNKNOWN | $0 public; compute extra |
| Roblox Charts | OFF | public pages / permitted UI | invented chart API | none stated | UNKNOWN | UNKNOWN | $0 public |
| Creator Hub analytics | OFF | granted dashboard/export/API, own games | other studios' data | authorized account | UNKNOWN | UNKNOWN | no separate price established |
| Roblox docs/news/IR | OFF | public reading | none stated | none | n/a | UNKNOWN | $0 public |
| Rolimon's | 3P-S (CCU), est. (playtime) | public viewing | bulk recurring use without permission/licence; do not assume a bulk API | permission/licence for bulk | UNKNOWN | UNKNOWN | public viewing $0; automation terms unknown |
| RoTrends | 3P-S/3P-E | public service | export beyond current plan: unverified | UNKNOWN | UNKNOWN | UNKNOWN | unknown plan price |
| RoVitals | 3P-S + modeled income | public pages | recurring automated use: rights unverified | UNKNOWN | UNKNOWN | UNKNOWN | viewing free; feed terms unknown |
| GameAnalytics | 3P-S (vendor sample) | public report; own SDK data | other products: plan unknown | own SDK | n/a | UNKNOWN | report public; rest verify |
| Steam charts | OFF | store charts, permitted collection | dollar growth from rank | none stated | UNKNOWN | UNKNOWN | $0 public |
| Valve Web API | OFF | public methods, documented interface | partner-only methods | UNKNOWN | UNKNOWN; terms govern | UNKNOWN | no fee established |
| Steamworks | OFF | own wishlists/sales | rivals' exact wishlists | studio partner account | UNKNOWN | UNKNOWN | conditions apply |
| SteamDB | 3P-S recorded | manual viewing where allowed | scraping/crawling | partnership for data | n/a | UNKNOWN | viewing free; contract unknown |
| Apple RSS | OFF | current builder feeds | old endpoints; old top-grossing feed; income claims | none stated | no SLA established | UNKNOWN | $0 public |
| Google Play | OFF (presentation) | public UI | unrestricted competitor API (none verified) | none | UNKNOWN | UNKNOWN | $0 public UI |
| Sensor Tower / data.ai | 3P-E | licensed UI/API/export, AI use only if the contract permits | use outside the contract; treating estimates as counts | contract | UNKNOWN | UNKNOWN | quote |
| YouTube Data API | OFF counters; search sampled | simple arithmetic on YouTube API data only | unapproved derived metrics/inferences; claiming exception | project credentials | 100 search.list/day; 10,000 other units/day (defaults) | cached data: refresh/delete about 30 calendar days; approved derived stats up to 36 months | no per-call price in default quota |
| TikTok Creative Center | OFF dashboard | manual record of country/window | treating as full coverage; commercial-use right not stated | none stated | UNKNOWN | UNKNOWN | described as free |
| TikTok Research Tools | OFF dataset | academic use only | any commercial use | eligibility | up to 48 h video delay; up to 10 d stats delay | UNKNOWN | not available |
| Instagram | OFF if provided | approved Graph features; manual review | assumed global sound API | approved app | hashtag cap UNKNOWN | UNKNOWN | unverified |
| Twitch Helix | OFF snapshots | top games/streams | naming a Roblox universe from category data | Client ID + OAuth | rate-limit headers exist; numbers UNKNOWN | UNKNOWN | no per-call price established |
| Google Trends | OFF index | UI export; alpha if accepted | counts from index; production use of alpha | alpha application | UNKNOWN | UNKNOWN | UI $0; alpha UNKNOWN |
| Reddit | OFF within scope | authorized API; manual reading | commercial use without separate agreement | agreement/OAuth | 100 per minute for eligible OAuth clients (not approval) | UNKNOWN | negotiated |
| Discord | community statements | approved bot, permissioned announcements | mining/scraping; message content for model training without express permission | bot permissions | UNKNOWN | UNKNOWN | implementation cost |
| Netflix / rights holders | OFF news | public news | assuming an IP right | licence deal for IP | n/a | UNKNOWN | news $0; IP variable |

## 8. Timing method (RP:336-337, 347-355, 360-361, 363; held-out rows removed)

| item | rule | tag | S | RP |
| --- | --- | --- | --- | --- |
| No typical lifetime | No single "trend lasts X weeks" is defensible: survivor bias; origins interval-censored; event peaks not comparable; live waves right-censored; memes, mechanics, franchises, one game's audience live differently. A three-day prototype story cannot give a studio's delivery time | OPINION | S13, S17a, S24, S34 | 336, 360 |
| Prototype vs live game | A reported build time of three months for a successful co-op survival game is one case, not a platform average | EXPERIENCE (S24 posted 2025-10-31) | S24 | 361, 484 |
| Trend start | Pre-registered baseline. Example: first of 3 matched days above 2 x the median of the preceding 4 weeks, with a minimum absolute audience. Example numbers are the author's choice, not natural boundaries (PROPOSAL) | OPINION | S03, S08 | 347 |
| Local peak | Maximum inside a fixed observed interval. Publish definitions, censoring and coverage | OPINION | S03, S08 | 347 |
| Half-life | Use event-free weekly averages, not one event spike. Fit the log of a smoothed event-free signal over a stated interval. half-life = ln(2) / absolute decay slope. Noisy history and small n: publish a broad prediction interval and a scenario, not a precise peak date. Do not fit a half-life to a rising curve and call it remaining lifetime. New waves: short/medium/long scenarios, to be compared with a validated historical cohort later | OPINION | S08, S24 | 347, 352 |
| Delivery estimate | From the studio's own completed work: spec, core prototype, persistence, multiplayer authority, device performance, UX, content, localization, policy/IP work, QA, acquisition tests, launch operations. Record low/mid/high date and the named designer/engineer estimate. No universal Roblox production median or AI-agent speed factor was found | OPINION | S03, S24 | 350 |
| Remaining runway | conservative date when relevant demand falls below the studio's economic threshold - current date | OPINION | S03, S08 | 354 |
| Delivery slack | runway - high-case launch duration - post-launch learning allowance. Until demand threshold and revenue are validated, slack is qualitative only | OPINION | S03, S08 | 354, 363 |
| If high case > runway | Pick one: an update/event in an existing game; a reusable prototype; reject | OPINION | S03, S08 | 354 |

## 9. Opportunity gates and scoring (RP:367-385)

Gates come before any score (OPINION S03, S07, S27-S30, RP:367). Five must clear: G1 accessible, permitted evidence; G2 content independently made or licensed; G3 playable age and policy fit; G4 credible technical scope; G5 a specific new player decision. Unknown material IP rights: HOLD that branded proposal. Not a small deduction a big trend can outweigh. An independently original design inspired by an abstract mechanic is not blocked (S27-S28 per the US Copyright Office: ideas, logic, methods are not covered by copyright; a US baseline, not a personal clearance; RP:542-544).

Scoring rules (OPINION S03, S07-S09, RP:369; PROPOSAL, not a validated predictor): each dimension is rated 0-5. Score = sum over dimensions of (weight x rating / 5), maximum 100. An UNKNOWN dimension: publish a lower score (rating 0 for it) and an upper score (rating 5 for it). Evidence completeness = assessed weight / 100. Never fill a missing revenue or build-time rating with a neutral 3.

| Dimension | Weight | 0 or low anchor | 3 anchor | 5 anchor | Evidence required |
| --- | ---: | --- | --- | --- | --- |
| Growth speed and persistence | 18 | falling, or a spike only | matched-week growth is positive, with coverage | repeated accelerating growth in non-overlapping windows, rising troughs | timestamped occupancy series, events, coverage |
| Addressable demand size | 10 | below the studio's test economics | enough relevant audience for a bounded test | broad yet relevant audience, shown by independent signals | average players / relevant search, geography, audience scope |
| Revenue evidence | 15 | contradictory or weak money signal | lasting official earning rank, cash openly unknown | authorized comparable unit economics and a feasible monetization | gross/net definition, period, payer/ARPU data if any |
| Roblox audience and device fit | 10 | inaccessible or unsuitable | fits one named cohort and touch controls | appeal tested; input/UI usable on all intended devices | cohort definition, maturity/access needs, playtest evidence |
| Build feasibility and timing | 15 | high-case delivery is longer than runway | existing systems support a scoped launch | working prototype; measured plan leaves ample learning time | owner-approved scope, reusable systems, delivery range |
| Competitive room and differentiation | 12 | many close substitutes, no new decision | clear first-session twist, identifiable gap | gap confirmed by competitor review and tests | candidate census, main loop, real twist, acquisition angle |
| IP and platform-policy certainty | 10 | fails the gate or unresolved branded rights | original content, dependencies reviewed | rights documented; content and discovery rules checked | asset/code provenance, licences, naming and policy review |
| Staying power | 10 | only a passing reference | a return trigger that does not depend on the meme | several tested progression or social reasons to return | replay/retention tests, content-operating plan |
| TOTAL | 100 | | | | |

Weights sum: 18+10+15+10+15+12+10+10 = 100 (derived check).

Score actions (OPINION S03, S07, RP:383; all cut-offs PROPOSAL, not probabilities; an 85 is not an 85% success rate):

| band | action |
| --- | --- |
| 75 or more, all gates clear, evidence completeness at least 80% | qualifies for a funded-prototype proposal |
| 60-74, or wide uncertainty | limited research or playtest ticket |
| below 60 | normally watch or reject |

Roles: creative director owns the creative/IP choice; designer owns loop and scope; scout owns evidence integrity and timely follow-up.

Test card, 12 fields (OPINION S07, S25, RP:385): hypothesis; audience; first-session promise; new decision; reusable systems; high-case delivery; evidence needed; cost/time cap; success metric; guardrail; stop condition; next review date. Success thresholds come from the studio's economics and baseline, not an invented universal D1 or CCU target. Check alert precision and decision value over time, rejected and failed candidates included.

## 10. Weekly report template (RP:408-465; tags and columns as in the paper)

Purpose: a short decision brief plus a reproducible evidence appendix. Creative director needs why now, audience, original hook, risk, effort. Designer needs loop, first-session decisions, reusable systems, progression, evidence gaps. Show changes since last week including wrong predictions and fading games. Say "no qualified build opportunity" when that is the evidence (OPINION S03, S07, S08, RP:408).

Header lines (RP:412-414): WEEK ENDING [date and timezone]; AS OF [exact timestamp] | DATA COVERAGE [windows and percentage] | PERMISSION STATUS [approved/limited/blocked]; DECISION REQUEST [approve bounded prototype / research / watch / reject].

| # | section [tag] | content or columns | RP |
| --- | --- | --- | --- |
| 1 | Three sentence brief [OPINION] | (a) the most consequential measured demand change; (b) the loop/theme combination worth investigating and its delivery window; (c) the largest open assumption that could reverse the recommendation | 416-419 |
| 2 | Rising games table [each row VERIFIED official, VERIFIED sampled, EXPERIENCE or OPINION] | 16 columns: game + universe/root-place IDs; repeated-action loop; created / confirmed launch / first observed; current CCU timestamp; 24h mean; non-overlapping 7d means; g7 % and absolute added CCU; acceleration pp; off-event trough; recent event and update; earning rank with date; revenue status and units; votes added; data coverage; independent source; confidence and gap | 421-425 |
| 3 | Rising loop families [OPINION interpretation, VERIFIED inputs] | 9 columns: family; aggregate seven-day player-hours; same-panel share change; number of independently growing games; dominant incumbents; new entrants; theme versus mechanic; evidence for saturation; counterexample | 427-429 |
| 4 | Outside trends [separate platforms] | 9 columns: entity/topic; first source date; newly rising derivative; region/language; dated views/interest/creator participation; trend velocity and exact denominator; actual Roblox adaptation evidence; IP route; estimated remaining window and uncertainty | 431-434 |
| 5 | Steam and mobile transfer watch | 8 columns: app ID/store country; demo or full game; revenue rank definition; mean CCU or licensed estimate; underlying repeated behavior; fit to touch/co-play; existing Roblox competitors; next evidence check | 436-438 |
| 6 | Top three opportunity cards [OPINION] | 11 fields A-K: A working title (original identity); B proven loop (1 line) + new theme (1 line) + new decision (1 line); C why now (dated observations, not only cumulative views); D money (official rank / owner disclosure / unvalidated estimate / unknown); E audience and device (specific cohort, no inferred child profiles); F scope (reused systems, new systems, low/mid/high delivery dates, owner estimate); G competition (named universe IDs, close-substitute count with sampling method); H rights/policy gate (pass/hold/fail, evidence); I score (known contributions, unknown range, completeness; not a success probability); J experiment (time/budget cap, success metric, stop condition, evidence needed); K decision owner (creative director/designer) and next review date | 440-451 |
| 7 | Fading, rejected and disconfirmed | 5 columns: previous claim; new evidence; source/correction; why inference changed; stop/update action | 453-454 |
| 8 | Evidence ledger | 14 columns: claim ID; evidence mark + provenance; metric and units; event period; observed at; source sample at; publication/update/effective date; URL; exact quote under 20 words; raw response/export reference if permitted; model assumptions; uncertainty; storage/licence expiry; next verification | 456-460 |
| 9 | Scout performance | 9 columns: prior alerts evaluated; false alerts; missed breakouts found later; lead time before defined breakout; test cost; decisions changed; retained rejected candidates; policy/access failures; next methodological fix | 462-465 |

Report rules (OPINION, RP:469-474): rank research priority with up to three cards and no invented approvals; every report lists previous decisions, declining and rejected examples; claim blocks carry a quote under 20 words, URL and source/effective date; evaluate early detection on matured cases without hindsight.

## 11. Evaluation definitions (OPINION S03, S08, S25, RP:467)

- breakout = a studio-chosen sustained player-hour threshold over a stated number of days.
- lead time = breakout timestamp - first qualifying alert timestamp.
- precision = qualifying breakouts / matured alerts. Recall needs a defined candidate universe and a later census.
- Calibration periods stay apart from evaluation periods. A backtest may not use a future all-time peak, a future title or a creator disclosure unknown on the historical decision date.

## 12. Open questions and limits (OPINION, RP:478-490)

| area | unresolved | RP |
| --- | --- | --- |
| Revenue (S07, S09, S25) | Need matched owner-authorized actuals for several games before trusting tracker cash estimates. Unknown: title-level error, fee/reward coverage, ownership splits, paid traffic, true profit. No candidate in the paper has validated net income. A large player count alone does not show "earning well" | 478 |
| Platform (S01, S06, S11) | Route-specific public Games batch limits; terms and AI permissions; Top Earning's complete official formula; chart refresh cadence; ranking filters and update logs. Some pages need JavaScript; some docs are undated | 480 |
| History (S08, S13, S55) | No full raw 2025-2026 panel. The loop catalogue mixes dated milestones with current observations. Several rise/fade cells are UNKNOWN. Snapshots show scale, not cohort retention | 482 |
| Copying and development (S17a, S21-S24) | Exact ship lags and controlled winner-versus-copy comparisons are rare. Need interviews, first releases, milestone dates, staffing, budgets. A low current audience alone does not prove failure | 484 |
| Social (S34b-S34d, S41) | Verify the intended Verity identity, source-video timestamps, official view histories before any production watchlist. Counts are third-party captures. YouTube sampled search and hashtag dashboards give no total reach, ages, overlap or conversion. Keep platform metrics apart | 486 |
| Access (S35, S39, S45, S48-S51) | Need current commercial/AI-use and retention permissions for recurring third-party feeds. Instagram docs not retrieved; no hashtag cap or global sound entitlement certified. Paid prices, limits, model error rates are quote/contract-specific. Check the October Roblox terms, not the November ones | 488 |
| Studio (S03, S07) | Not supplied: delivery estimates, budget, target cohort, accepted downside, economic test threshold, reusable systems. The rubric is usable but not calibrated. Ask internally before recommending production funding; keep gathering permitted evidence | 490 |

## 13. Internal inconsistencies and gaps (extractor checks; nothing fixed)

| # | RP | issue |
| --- | --- | --- |
| 1 | 304 vs 535, 629 | The Rolimon's row lists S16-S24, but S23 is RoStats and S24 is a DevForum creator spotlight. Neither is a Rolimon's page |
| 2 | 308 vs 309, 560 | Steam charts row says "concurrent scale" but cites only S36 (revenue Top Sellers). The concurrency source is S37 (row 309) |
| 3 | 318, 488 | Instagram row has no S-id and docs were not retrieved. Every cell is unverified |
| 4 | 196 vs 523, 627, 638 | The Sep 2025 ">25 million concurrent" record (S56) does not say if it is a platform or a game figure; S17 shows a different sampled max date (2025-10-11) for Steal a Brainrot; "universe created 2025-05-16" is the same day as the GMA article (S34a). Confirm before use |
| 5 | 197, 201 vs 555-558, 620 | July 10 (fan song) and July 22 (remix) dates, "nine million in four days" and "17 million in about a month" have no register date or quote. The register shows only the 2026-05-30 debut and a "July/August" spread. The linked original video showed no date or statistics. The 2026-07-25 date comes from an aggregator page. So 56 and 15 days rest on third-party dates |
| 6 | 195, 644 | The 13-day lag uses the UTC date of a post made 06:22 UTC. In US time zones that post falls on 2021-09-29, so the count could be 12 in local dates. Release time zone not given. The paper words it "at most" |
| 7 | 264, 279 vs 610-612 | The 30-day and 36-month rules come from two different policy pages (one undated); the rule row dates them with the guide's 2026-09-14 date. No register quote shows "36 months" |
| 8 | 258, 266, 218 vs 569, 589, 560 | The 10,000 units/day figure, the 10-day statistics delay and the 3-hour extra weight are not in the register quotes (only "100 search.list calls", "48 hours", "trailing 24 hours") |
| 9 | 369, 383 | Cut-offs (75, 60) do not say which value to test when dimensions are UNKNOWN: lower score, upper score or a mid value. A 75+ score with a gate not clear, or with completeness under 80%, has no stated action |
| 10 | 371-381 | Anchors exist only for ratings 0 (or "low"), 3 and 5. Ratings 1, 2, 4 are not defined. "0 or low" mixes two values |
| 11 | 367, 379 | An unresolved branded right is a gate HOLD and also an IP-row rating anchor of 0. Not contradictory, but a double penalty unless the sheet is told to skip scoring on HOLD |
| 12 | 421-425 | Report columns "g7 %", "acceleration pp", "non-overlapping 7d means", "votes added" are not defined in lines 189-491 (likely before line 189) |
| 13 | 459, 473 | Evidence-ledger quote cap is under 20 words; the kit's extraction rule is under 15. Choose one cap when the skills are written |
| 14 | 473 | One rule row cites "User requirements" as its source, not an S-id |
| 15 | 241, 314, 316 | data.ai is named in Sensor Tower's terms, but owner and shared inputs are not resolved. The TikTok Creative Center row says "described as free"; free is not a commercial-use permission (RP:286) |
| 16 | 361, 484 | The three-month build figure appears in two non-held-out spots (rule row, open question) while the matching timing-table row is withheld. Lead may want to remove these two |
| 17 | 288 | The prior Roblox terms were never read, so no statement on AI scraping under the October contract can be made |

## 14. Cited sources outside the access table (S-id, nature, date status, URL)

| S | what | date status | URL |
| --- | --- | --- | --- |
| S03 | Creator Hub Discovery FAQ, official ranking/cohort guidance | undated, accessed 2026-10-20 | create.roblox.com/docs/discovery-faq |
| S04 | Roblox announcement on discovery (7-day view changed to 28-day view) | published 2026-06-15 | about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox |
| S09 | Statroblox methodology, vendor model (range never narrower than divide/multiply by 1.6), not validation | undated, October 2026 survey label | statroblox.com/methodology |
| S10 | GameAnalytics 2026 Roblox Benchmark Report, instrumented dataset Aug 2025-Jul 2026, selected 500+ titles with 1M+ MAU | last updated 2026-09-01 | gameanalytics.com/reports/2026-roblox-report |
| S11, S12 | Cloud API stability, rate limits | undated, accessed 2026-10-20 | create.roblox.com/docs/cloud ; .../cloud/reference/rate-limits |
| S14, S15 | Creator-earnings disclosure; Developer Exchange rates (rate effective 2026-06-08 per help page) | S14 published 2026-09-03; S15 undated | about.roblox.com/newsroom/2026/09/global-impact-of-creation-on-roblox |
| S13, S17a, S24 | Roblox Q2 2025 letter (filed 2025-07-31); GamesBeat interview (2025-09-07, developer recollection); DevForum spotlight (2025-10-31). Quotes of S13 and S17a are withheld | dated | sec.gov (S13); gamesbeat.com/janzen-madsen-interview/ |
| S27-S30 | US Copyright Office (games, programs), USPTO confusion, Roblox IP guidelines and rights-holder guide | undated, accessed 2026-10-20 | copyright.gov/register/tx-games.html ; tx-programs.html ; uspto.gov ; create.roblox.com/docs/production/publishing/ip-guidelines |
| S31 | Roblox Terms of Use and update notice; effective-date 2026-11-01 header | retrieved 2026-10-20 | en.help.roblox.com (articles 115004647846, 14663412502676) |
| S32, S33 | Netflix release notice; DevForum "Squid Game Update Log" | release 2021-09-17; post 2021-09-30 06:22 UTC | about.netflix.com/en/news/squid-game-invites-you-to-deadly-childhood-games-on-september-17 ; devforum.roblox.com/t/squid-game-update-log/1488720 |
| S34a-S34e | GMA 2025-05-16; KYM Verity entry (undated) and KYM "It's Me It's Verity" (2026-08-26); mostviewed.today record (video 2026-07-25); Guinness (2026-02-06) | as listed | goodmorningamerica.com ; knowyourmeme.com/memes/subcultures/verity-minecraft-arg ; knowyourmeme.com/memes/its-me-its-verity ; mostviewed.today ; guinnessworldrecords.com |
| S40 | Droid Gamers guide on a dusty trip | historical 2024, day unknown | droidgamers.com/guides/a-dusty-trip-tutorial/ |
| S54-S56 | RDC 2026 post (2026-09-11); Q2 2026 shareholder letter (2026-07-30: adults over 18 monetize over 50% more than under-18s); 2025 Replay (2025-12-16) | dated | about.roblox.com/newsroom/... ; sec.gov |
| S60 | RoVitals trending page: ratio of 24-hour average CCU to 7-day average, selected rows, not an official market ranking | undated | rovitals.com/trending |
