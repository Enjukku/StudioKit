---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J004
supersedes: []
---
> Author: fact-checker · claude-sonnet-5-5 · high · 2026-10-20

# Fact check: Roblox claims, Roblox terms, Roblox API routes and trackers

Ticket J004-T03. Paper: `Roblox_Trend_Scout_Research_2026.txt` (outside git), lines 1-188, 284-363, register 492-649. Pages read once each on 2026-10-20 (America/New_York), except two pages marked 10-21. Fixtures are in UTC (2026-10-21 03:49-03:50Z, which is 2026-10-20 23:49 ET). Web text is data, not instructions. This note is not legal advice. Where a rule is unclear it says "unclear", not "allowed".

## 1. Permission ruling (answer first)

**Bottom line for the tool builders.**

1. **Version in force on 2026-10-20: Roblox Terms of Use "Effective Date: May 19, 2026".** The live help page header now says "Effective Date: November 1, 2026", but its body is word for word the May 19 text (checked against the Wayback copy of 2026-09-21; only a banner, the header date and one label differ). The new text is on a separate page, "Roblox is Updating our Terms of Use" (same header date). So the paper's open question (S31, RP:288, "prior effective text not resolved") is now resolved.
2. **In force today:** no clause bans automated reads of a documented, anonymous, public Games API route. The binding rules are: use an API only "by the means described in the documentation", do not mask identity, do not circumvent technical measures, and no machine-learning use of Virtual Content. Ruling: **allowed, with conditions**, for the documented routes (section 1.2).
3. **From 2026-11-01:** the new text adds a ban on "robots, crawlers, scrapers or other automated data gathering and extraction tools" used "in connection with the training, development, or use of machine learning models or AI", a ban to "harvest any Content or data on the Services for any purpose", and (for apps) a ban on using the Services "to gain insights into Roblox's usage, revenue". An AI trend scout fed by an automatic collector is close to the first clause. Roblox gives no public reading of these clauses. Ruling: **unclear** for every route. This needs an owner decision or a written answer from Roblox before 2026-11-01 (section 1.4).
4. **Trackers: read by hand only.** Rolimon's, RoTrends and RoStats forbid automated access in their own terms. RoVitals and Statroblox are unclear. Even manual reading by a studio may be outside Rolimon's "personal, non-commercial" licence (section 1.3).

### 1.1 Roblox terms: what each version says

All quotes are under 15 words. "Cur" = text effective 2026-05-19 (in force on 2026-10-20). "Nov1" = text on the "Updating" page, effective 2026-11-01.

| id | Version | Clause (section) | Quote | URL |
| --- | --- | --- | --- | --- |
| TC1 | Cur | Creator Terms, "Roblox APIs" | "Only access an API by the means described in the documentation of that API" | https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use |
| TC2 | Cur | same | "refrain from misrepresenting or masking your identity" (also: Roblox may suspend API access "without notice") | same |
| TC3 | Cur | User Terms, Restrictions of Use (c) | "circumvent any technological measure designed to protect the Services" | same |
| TC4 | Cur | same, (d) | "access the Services using any means for the purpose of using Virtual Content" + "in connection with the training, development, or use of machine learning models" (clause continues "or artificial intelligence") | same |
| TC5 | Cur | Account | "You may only access the Services through your own Account" (anonymous reads need no account) | same |
| TC6 | Cur | Appendix C (EU/EEA) | "reserves the right to text and data mining of the Platform" | same |
| TC7 | Cur | whole text | No clause with the words scrape, crawl, spider, bot or "automated means" aimed at users (searched 230k characters). "Virtual Content" is defined as items "offered by Roblox and/or Creators" incl. Experience access, so TC4 is arguably about using the content, not reading play counts. | same + archive https://web.archive.org/web/20260921/https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use |
| TN1 | Nov1 | User Terms 9.2 Restrictions on use | "robots, crawlers, scrapers or other automated data gathering and extraction tools" (the sentence says: accessing the Services by any means "in connection with the training, development, or use of machine learning models or AI") | https://en.help.roblox.com/hc/en-us/articles/14663412502676-Roblox-is-Updating-our-Terms-of-Use |
| TN2 | Nov1 | 9.2 | "harvest any Content or data on the Services for any purpose" | same |
| TN3 | Nov1 | 9.2 | any use of the Service or Content only "as expressly authorized by the Service" or with written permission | same |
| TN4 | Nov1 | 9.3 Reservation of use | "expressly reserves all rights to use any Content on the Service for such purposes" (commercial use, incl. AI training) | same |
| TN5 | Nov1 | Creator Terms 3.7 Use of Roblox APIs | "only access an API by the means described in the documentation of that API" | same |
| TN6 | Nov1 | Creator Terms 4.3 | API use must not be "not in accordance with the applicable Documentation" and must not exceed "any API rate, call, or other usage limits" | same |
| TN7 | Nov1 | Creator Terms 3.8.2 (apps that use "Roblox systems, data, or services") | "to gain insights into Roblox's usage, revenue" (apps are "expressly prohibited from collecting or aggregating" such data to do so) | same |
| TN8 | Nov1 | 3.9 Game data | Roblox and the creator may use data about their own Game. No right for outsiders. | same |
| TW1 | both | Community Standards, Disruptive Content | "Using bots or other automation that is programmed to run disruptive tasks" | https://about.roblox.com/community-standards |
| TW2 | both | Creator Third Party App Policy (apps with API access) | "You may not sell any data obtained through Roblox APIs"; app must not "abuse our APIs" | https://en.help.roblox.com/hc/en-us/articles/37924211313044-Creator-Third-Party-App-Policy |
| TW3 | both | robots.txt | api hosts (games, apis) return HTTP 404 for /robots.txt, so no crawl rules; www.roblox.com robots.txt does not disallow /charts. A robots file is not a licence in any case. | https://www.roblox.com/robots.txt |

Key differences Cur to Nov1: Nov1 names automated tools, adds "harvest ... for any purpose", drops the "Virtual Content" limit on the AI clause, adds the app clause TN7 and API-limit clause TN6. Nov1 keeps the "documented means" rule (TN5).

### 1.2 Ruling per Roblox route

Permission is separate from the HTTP result (all seven returned HTTP 200 without a login). "Documented" means listed on the Creator Hub reference page https://create.roblox.com/docs/cloud/reference/domains/games (breadcrumb "Open Cloud API", read 2026-10-20), where the lock icons show "Cookie" and "None" (anonymous accepted).

| Route | Documented / auth / batch | Response fields (fixture) | Observed rate header (not a guarantee) | Ruling Cur (in force) | Ruling Nov1 |
| --- | --- | --- | --- | --- | --- |
| GET games.roblox.com/v1/games?universeIds= | Yes, Experimental; auth None; "Cannot exceed a maximum of 50 IDs"; optional `fields`; 400 for invalid or too many IDs, 429 for rate | `id, rootPlaceId, name, description, creator{id,name,type,...}, playing, visits, maxPlayers, created, updated, genre fields, favoritedCount, canonicalUrlPath, isContentRestricted` | 300 per 60 s (`x-ratelimit-limit: 300, 300;w=60`) | **allowed** (conditions below) | **unclear** |
| GET /v1/games/votes?universeIds= | Listed, auth None; no parameter table on the page, batch maximum not documented | `data[{id, upVotes, downVotes}]` | 200 per 60 s | **allowed** (conditions) | **unclear** |
| GET /v1/games/{universeId}/favorites/count | Yes, Experimental; auth None; single universe | `{favoritesCount}`; 400 "root place is invalid", 404 unknown universe | 200 per 60 s | **allowed** (conditions) | **unclear** |
| GET /v1/games/{placeId}/servers/Public | Listed, auth None; no parameter table | `data[{id, maxPlayers, playing, playerTokens, players, fps, ping}]` + cursors | **3 per 60 s** | **allowed** but not recommended: tiny quota; `playerTokens` and `players` are player identifiers (empty in our sample) | **unclear**; do not use |
| GET /v2/users/{userId}/games | Yes, Experimental; auth None; `limit` 10/25/50 | `data[{id,name,description,creator{id,type,name},rootPlace,created,updated,placeVisits}]` + cursors | 200 per 60 s | **allowed** (conditions); returns a developer's public user ID | **unclear** |
| GET /v2/groups/{groupId}/gamesV2 | Yes (the page also marks `/v2/groups/{id}/games` "Not Recommended", the doc lists a 501 "not implemented" code, yet it returned 200); `limit` up to 100 | same shape as user games | **3 per 1 s** (`3, 3;w=1`) | **allowed** (conditions) | **unclear** |
| GET apis.roblox.com/universes/v1/places/{placeId}/universe | **Not documented**: absent from the apis.roblox.com and Universes reference pages (searched 2026-10-21). Only DevForum use (S52). | `{universeId}` | 60 per 60 s | **not allowed** (TC1: only documented means) | **not allowed** (TN5) |
| Open Cloud keyed (apis.roblox.com/cloud/v2/...) | see section 1.5 | n/a | n/a | not usable for other studios' games | same |

Conditions for the "allowed" rows (these are Roblox's own wording or the studio's rule):
- Anonymous GET only. No login, no cookie, no key (TC5).
- Use only documented parameters; at most 50 IDs per `/v1/games` call.
- Honour HTTP 429, `retry-after` and `x-ratelimit-*` (S12 quotes: "Write your code to expect and handle HTTP 429"). Do not rotate IP or masks (TC2, TC3).
- Send an honest User-Agent that names the studio tool (TC2).
- Keep volume low. Studio rule (not a Roblox number): the plan of a few requests per hour or day is well inside every observed limit.
- Never store `playerTokens` or `players`. Store counters and IDs only.
- Counters are not Virtual Content. Do not feed Roblox descriptions, thumbnails or place files to a model (TC4).

Why Nov1 is "unclear" and not "not allowed": the collector reads documented, anonymous routes, and TN3 allows use "as expressly authorized by the Service". Against that: TN1 is broad ("in connection with ... use of machine learning models or AI") and the studio's reader is an AI agent; TN2 says "any purpose". Roblox has not published how it reads these. I found no Roblox statement that outside tools may call the legacy routes (the docs only say legacy APIs are not recommended for production, row L01).

### 1.3 Ruling per tracker (hand reading only)

| Tracker | Automated access | Clause (quote, under 15 words) | URL, date | Manual reading by a studio |
| --- | --- | --- | --- | --- |
| Rolimon's | **not allowed** | "Use any robot, spider, scraper, or automated tool"; "scrape, or systematically collect the materials or data"; "for any commercial purpose without prior written consent" (ToS "Last updated: August 21, 2025") | https://www.rolimons.com/termsandprivacy, 2026-10-20 | **unclear**: licence is "for personal, non-commercial transitory viewing only". A studio using it for a business decision may need written consent (contact page). robots.txt allows `*` with crawl-delay 2, but ToS decides. |
| RoVitals | **unclear** | "scrape or automate requests at a volume that degrades the service"; also bars wholesale republishing of its history, "individual figures, with attribution, are fine" (ToU "Last updated: October 15, 2026") | https://rovitals.com/terms, 2026-10-20 | allowed (individual figures with attribution) |
| RoTrends | **not allowed** | "Use any data-mining, robots, or similar data-gathering tools" ... "except via documented APIs or with our written consent". No documented API found (DevForum thread lists none). Caution: the terms page footer says "Chartis", so confirm it governs rotrends.com. | https://www.rotrends.com/terms-of-use, 2026-10-20 | allowed for "personal or internal business purposes" per same section |
| RoStats | **not allowed** | "Do not scrape, bulk-download or resell the data."; "use automated access beyond ordinary browsing"; "API access is available on request." (ToS "16 October 2026") | https://rostats.io/terms, 2026-10-20 | allowed (ordinary browsing). Site pages did not render data in the browser pane, so some rows are unverified (K13). |
| Statroblox | **unclear** | Terms have only Estimates, Marketplace and User content sections. No automated-access clause found (read twice). robots.txt disallows `/api/`, `/compare`, filtered search and many AI crawlers. | https://statroblox.com/terms and https://statroblox.com/robots.txt, 2026-10-20 | allowed (no restriction found) |

Third-party evidence only (not permission): RoVitals writes that its figures "are gathered from Roblox's public API on a recurring schedule" and Statroblox writes it snapshots "every five minutes" and crawls the Top Earning chart every 30 minutes. This shows the pattern is common; it does not give the studio a right.

### 1.4 Recommendation for the tool builders (one line each)

- **Now (until 2026-10-31):** the collector may call only the documented anonymous routes `/v1/games`, `/v1/games/votes`, `/v1/games/{id}/favorites/count` and the user and group game lists, at the studio's own low rate, with 429 and `retry-after` handling, an honest User-Agent and no `playerTokens`. Do not call `/universes/v1/places/{placeId}/universe` or `/servers/Public`.
- **From 2026-11-01: needs-decision (owner).** Keep the collector off by default. The owner either (a) asks Roblox in writing (Creator Support or the DevForum) whether public Games API reads that feed an AI analysis tool are allowed under 9.2, or (b) accepts the risk (suspension of the studio account's API access is the stated remedy; the rows cite "suspend access without notice"), or (c) pauses collection and uses the Roblox charts and tracker pages by hand.
- **Trackers:** hand reading only. Ask Rolimon's for written consent before the studio relies on it for decisions. No tracker is ever the "official" source for a number.

### 1.5 Open Cloud: any keyed route for other studios' public counters?

**No such route found (verdict: confirmed absence, with limits).**
- The Open Cloud `Universe` resource (GET /cloud/v2/universes/{universe_id}, Stable, API key or OAuth) has `displayName, description, visibility, ageRating, voiceChatEnabled, platform flags, rootPlace, privateServerPriceRobux` and **no** `playing`, `visits`, favorites or votes field. Source: https://create.roblox.com/docs/cloud/reference/features/universes (read 2026-10-20).
- API keys reach only what "the user who owns it" can access (own experiences and groups where the owner has a role). Source: https://create.roblox.com/docs/cloud/auth/api-keys (2026-10-20).
- The Analytics Query API needs `universe.analytics:read` on "your experience" and returns metrics such as DailyActiveUsers and retention; the page lists no concurrent-users metric. Source: https://create.roblox.com/docs/cloud/guides/analytics (2026-10-20).
- Limit: I read the Universe schema and the guides, not every Open Cloud page. An undocumented keyed route could exist.

## 2. Claims table

Provenance labels: official / third-party sampled / third-party estimate / developer statement / derived. "A" = access date (ET). Verdicts: confirmed, corrected, unverified (keep as OPINION), dropped.

### 2a. Terms, routes, limits (RP:21, 31, 39-56, 286-288)

| id | RP line | Claim as stated | Provenance | Checked against (URL + A) | Verdict | Corrected value or note |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | 31, 288 | Roblox terms page advertises Nov 1, 2026; text has Virtual Content and AI restrictions; prior text unresolved | official | https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use, https://en.help.roblox.com/hc/en-us/articles/14663412502676-Roblox-is-Updating-our-Terms-of-Use, Wayback 20260921 (A 2026-10-20) | corrected | Header "Effective Date: November 1, 2026" is on both pages. Body of the main page = May 19, 2026 text (in force). The Nov 1 text is on the "Updating" page and is stricter (section 1.1). |
| T02 | 21 | "Public visibility does not itself grant scraping, AI-use or historical-storage rights" | official / opinion | same (A 2026-10-20) | corrected | True for Nov1 (9.2, 9.3). For the in-force text there is no scraping ban; documented routes are usable under TC1 conditions. Say "rights are stated per version". |
| T03 | 286 | "An HTTP 200 establishes technical accessibility, not permission" | opinion | Rolimon's robots.txt allows `*`, ToS forbids bots (A 2026-10-20) | confirmed (OPINION) | Example found: robots.txt allow plus ToS ban at Rolimon's. |
| T04 | 56 | "An in-game HttpService limit is not permission for an external crawler" | official | https://create.roblox.com/docs/cloud/reference/rate-limits (A 2026-10-20) | confirmed | Doc states 500 HTTP requests per minute per game server for HttpService; it covers Open Cloud, not the games.roblox.com web routes. |
| R01 | 39, 43 | `/v1/games?universeIds=` is unauthenticated game-details; fields id, rootPlaceId, creator, playing, visits, favoritedCount, created, updated, maxPlayers, genre, canonicalUrlPath | official | https://create.roblox.com/docs/cloud/reference/domains/games (A 2026-10-20); fixture `games_v1_games.json` | confirmed | Batch max documented: **50**. Auth: Cookie or None. Marked Experimental. |
| R02 | 44 | `/v1/games/votes?universeIds={ids}` gives up/down votes | official | same + fixture `games_v1_votes.json` | confirmed | Fields `id, upVotes, downVotes`. Batch maximum not documented on the page (do not assume 50). The page marks `/v1/games/{id}/votes` "Not Recommended". |
| R03 | 45 | `/v1/games/{universeId}/favorites/count` | official | same + fixture | confirmed | Field `favoritesCount`. Experimental. |
| R04 | 46 | Place-to-universe route is "common ... DevForum"; browser could not retrieve it; test first | developer statement (S52) | live call, HTTP 200 (A 2026-10-20, 03:50:12Z) | corrected | Route works anonymously (`{universeId}`), but it is **not in Creator Hub reference**. Ruling: not allowed (TC1, TN5). |
| R05 | 47 | `/v1/games/{placeId}/servers/Public` listed | official | same + fixture | confirmed | Listed, auth None, no parameter table. Observed limit 3 per 60 s. Fields incl. `playerTokens`, `players` (empty in sample). |
| R06 | 48 | `/v2/users/{id}/games` and `/v2/groups/{id}/gamesV2` enumerate games | official | same + fixtures | confirmed | Users route Experimental; `limit` 10/25/50 (groups up to 100); cursor paging; fields include `placeVisits`. gamesV2 docs list a 501 code but live returned 200. |
| R07 | 39 | "Many legacy routes labelled Experimental" | official | same | corrected | Page is under "Open Cloud API" breadcrumb, not labelled legacy. Some routes (votes, servers, groups) are not Experimental. Stability wording is in L01. |
| R08 | 50 | Sample response: 15,757 playing; 35,981,794,210 visits; 11,452,804 favorites; created 2025-03-25T22:32:09.437Z; updated 2026-10-20T01:28:46.738Z | official (public counter) | fixture `games_v1_games.json`, 2026-10-21T03:49:43Z | confirmed | Same schema and same `created`/`updated`. Counters moved: playing 16,012; visits 35,982,033,613; favorites 11,452,892 (live counters change). Creator = group "The Garden Game" (id 35789249). |
| R09 | 52 | maxPlayers is server capacity; same-name games exist | official | fixture: maxPlayers 4 | confirmed | |
| O01 | 39, 54 | (implied) a keyed Open Cloud route can give public counters for games the studio does not own | official | https://create.roblox.com/docs/cloud/reference/features/universes, https://create.roblox.com/docs/cloud/auth/api-keys, https://create.roblox.com/docs/cloud/guides/analytics (A 2026-10-20) | confirmed (negative, limited) | No Open Cloud route returns `playing`, `visits`, favorites or votes for another creator's experience. Details in section 1.5. |
| L01 | 54 | Legacy APIs have "minimal stability guarantees" and can change without notice | official | https://create.roblox.com/docs/cloud (A 2026-10-20) | confirmed | Exact: legacy APIs "can incorporate breaking changes without notice"; "We don't recommend them for production applications." The page does not say whether outside tools may call games.roblox.com. |
| L02 | 54, 56 | Handle HTTP 429; honour Retry-After; else exponential backoff | official | https://create.roblox.com/docs/cloud/reference/rate-limits (A 2026-10-20) | confirmed | Doc: check `retry-after`; headers `x-ratelimit-limit/remaining/reset`. The page covers Open Cloud; the games routes send the same headers (fixtures). |
| L03 | 54 | "No universal numeric requests-per-minute entitlement ... verified" | official | fixture response headers (A 2026-10-20) | corrected | No published number, but live headers show per-route limits: /v1/games 300/60 s; votes 200/60 s; favorites 200/60 s; users games 200/60 s; place-universe 60/60 s; servers 3/60 s; groups gamesV2 3/1 s. Observed once, may change; read headers each call. |
| L04 | 56 | Suggested 5-minute collection interval is a studio choice | opinion | n/a | confirmed (OPINION) | 5 minutes on 50 IDs = 12 calls/hour, far under 300/60 s. Roblox gave no guarantee. Terms status in section 1. |

### 2b. Charts and discovery (RP:76-87)

| id | RP line | Claim | Provenance | Checked against (URL + A) | Verdict | Corrected value or note |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | 80, 13 | Most Popular = "highest number of players currently online" | official | https://www.roblox.com/charts/top-playing-now (A 2026-10-20); DevForum https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809 | confirmed | Chart title "Most Popular Games on Roblox". DevForum staff post (2025-03-05): "based on concurrent users (CCU)". No refresh cadence stated. |
| C02 | 81, 13 | Top Trending = more time spent "over the past two weeks" | official | https://www.roblox.com/charts/top-trending (A 2026-10-20) | confirmed | FAQ text: games "players have been spending more time in over the past two weeks". No formula, no cadence. |
| C03 | 82 | Top Earning = revenue/spend order; trailing seven-day Robux spend | third-party estimate (Statroblox) | https://statroblox.com/methodology (A 2026-10-20); chart page fetch | unverified (keep as OPINION) | No official definition on any Roblox page I could read (the chart page has no FAQ text). "Last 7 days" comes only from Statroblox's own limitation note. S13 (SEC letter) ranks games by spend but does not define the chart. |
| C04 | 83 | Top Revisited / Fun with Friends: formulas not verified | official (existence) | https://www.roblox.com/charts (links to `/charts/top-revisited`, `/charts/fun-with-friends`, A 2026-10-20) | confirmed as "unverified" | Both charts exist. No Roblox definition found; keep as OPINION. Also seen: Up-and-Coming chart, no official definition (DevForum commenter doubted its name). |
| D01 | 87 | Signals: day 1, day 2-7, day 8-28 | official | https://create.roblox.com/docs/discovery-faq (A 2026-10-20) | confirmed | Day 1 signals: playtime, play days, Robux spend, co-play. |
| D02 | 87, 13 | 2026-06-15 change from 7 to 28 days | official | https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox | confirmed | Published 2026-06-15; "from its previous 7-day view to a 28-day view" for Recommended For You. No separate effective date stated. |
| D03 | 87 | Signals are "averages per user, not total values" | official | Discovery FAQ (A 2026-10-20) | confirmed | The newsroom post does not use this phrase; the FAQ does. |
| D04 | 87 | Signals use users acquired organically through RFY; daily retest | official | Discovery FAQ | confirmed | "users who organically joined from the RFY sort on Home"; "The algorithm tests your game daily". |
| D05 | 87, 177 | Non-unique metadata and place files are not prioritised | official | https://create.roblox.com/docs/discovery (A 2026-10-20) | confirmed | "are no longer prioritized for recommendations and might rank lower in search results". |
| D06 | 87 | RDC 2026 (Sept): age-aware discovery; Moments in the U.S. with age/region variation | official | https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play (published 2026-09-11) | confirmed | "Our discovery ranking system is increasingly age-aware"; Moments "fully available in the United States"; footnote: availability "will vary by age and region". |

### 2c. Money and official disclosures (RP:103-113)

| id | RP line | Claim | Provenance | Checked against (URL + A) | Verdict | Corrected value or note |
| --- | --- | --- | --- | --- | --- | --- |
| M01 | 103 | Creators earned over $1.5 billion in 2025 vs $923 million in 2024 | official (Roblox disclosure) | https://about.roblox.com/newsroom/2026/09/global-impact-of-creation-on-roblox (published 2026-09-03; A 2026-10-20) | confirmed | Roblox figures, not Nordicity (Nordicity covers only the U.S. impact report). |
| M02 | 103 | Over 42,000 DevEx participants; about $1,500 median, 12 months to 2026-06-30 | official | same page, footnote 3 | corrected | Footnote: "over 42,000 are part of our DevEx program" and "median creator receiving approximately $1,500 USD". The footnote does not say who the median covers; it reads as DevEx participants. Keep "approximately". |
| M03 | 105 | Standard DevEx $0.0038 per Earned Robux | official | https://create.roblox.com/docs/production/monetization/developer-exchange (A 2026-10-20) | confirmed | "0.0038 per 1 Earned Robux" = $114 for 30,000. Page also shows the earlier 0.0035 (before 2025-09-05). |
| M04 | 105 | $0.0054 for qualifying adult spend from 2026-06-08 | official | same + https://create.roblox.com/docs/production/monetization/18-plus-devex-rate | confirmed | Applies to developer products, passes, subscriptions, private servers bought by U.S. players verified 18+. The game must also meet character rules (no R6 switch). The date 2026-06-08 is on the 18+ page, not the main DevEx page. |
| M05 | 107 | Q2 2026 letter: O18 users "monetize over 50% higher" | official (SEC) | https://www.sec.gov/Archives/edgar/data/1315098/000162828026051059/ex991-robloxq22026earnin.htm (A 2026-10-20) | corrected | Sentence is "U.S. O18 users monetize over 50% higher than U18 users." Add: U.S. only; metric not named; age data extrapolated from age-checked users (letter warns the split "may not fairly represent" non-checked users). Letter tied to 2026-07-30. |
| M06 | 167 | Q2 2026 letter names Grow a Garden 2 as quickly growing | official | same letter | confirmed | Named with "Animal Hospital" and "Kick a Lucky Block" as new games that "quickly move from initial release to top experiences". No spend or DAU figure. |
| M07 | 140, 340 | Q2 2025 letter: Grow a Garden top by spend within a month; launch 2025-03-25 | official (SEC) | https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm (A 2026-10-20) | confirmed | Fragment: "top experience based on spending within one month of its creation". Letter gives launch March 25, 2025. |
| M08 | 111 | June 2025 top-10 by Robux spend includes Grow a Garden, Steal a Brainrot, Dead Rails | official | same letter | confirmed | "Three out of our top 10 experiences by Robux spend in June 2025"; names the three as examples. Full top 10 not listed. |
| M09 | 141, 197 | 2025 Replay: over 25 million concurrent | official | https://about.roblox.com/newsroom/2025/12/roblox-replay-decoded-search-style (published 2025-12-16) | confirmed | Steal a Brainrot, September. Same page: Grow a Garden record 21.6 million in July (Guinness). Q2 2025 letter says "nearly 22 million" for July. |
| M10 | 152 | Brookhaven was #1 search in the 2025 recap | official | same Replay page | confirmed | Top searches: Brookhaven, Grow a Garden, Steal a Brainrot. |
| G01 | 109 | GameAnalytics 2026: median session 9.8 min, p90 14.7, p99 21.1 | third-party (vendor SDK sample) | https://www.gameanalytics.com/reports/2026-roblox-report (last updated 2026-09-01; A 2026-10-20) | confirmed | Per-game medians across the sample, not per-session medians. Page: "It is not a census of Roblox." |
| G02 | 109 | Median D1 retention 10.3% | third-party (vendor) | same | confirmed | "only 10.3% of players return the day after their first session". No formal formula on the page. |
| G03 | 70, 109 | Sample 500+ titles with 1M+ MAU, Aug 2025 to Jul 2026 | third-party (vendor) | same | confirmed | "over 500 Roblox titles that reached at least 1 million monthly active users"; data 2025-08-01 to 2026-07-31. Games must be integrated with GameAnalytics. |

### 2d. Developer statements and IP (RP:159-179)

| id | RP line | Claim | Provenance | Checked against (URL + A) | Verdict | Corrected value or note |
| --- | --- | --- | --- | --- | --- | --- |
| J01 | 159, 183 | Grow a Garden about 500 CCU, then about 100,000 in two weeks, about 1M in a month | developer statement | https://gamesbeat.com/janzen-madsen-interview/ (published 2025-09-07, updated 09-08; A 2026-10-20) | confirmed (as developer recollection) | Quotes: "around maybe 500 CCUs, 10,000 to 20,000 DAUs"; "Maybe within two weeks we were at about 100,000 CCUs"; "we hit a million CCUs in about a month". He says he could get exact figures later. Do not treat as audited. |
| J02 | 161 | GamesBeat opening "104 days" error | derived | same page | confirmed | Article says debut March 26, 2025, "just 104 days ago"; March 26 to September 7 is 165 days. Paper is right to avoid it. |
| J03 | 146, 185 | 99 Nights: three-month sprint; ~14M peak | developer statement | https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940 (2025-10-31, Ozamanthus) | confirmed | "built in a sprint of three months"; launched June 2025; "peak CCU of 14 million". Tracker peak is 14,153,173 (K04). |
| I01 | 175 | Copyright Office: game ideas and methods of play not protected | official (U.S.) | https://www.copyright.gov/register/tx-games.html (A 2026-10-20) | confirmed | "The idea for a game is not protected by copyright." Rule text and artwork can be. |
| I02 | 175 | Computer programs: no protection for abstract algorithms; code expression protected | official (U.S.) | https://www.copyright.gov/register/tx-programs.html | confirmed | "Copyright protection is not available for ideas, program logic, algorithms". The page speaks of "copyrightable expression embodied in the computer program"; it does not use the words source code. |
| I03 | 175 | USPTO likelihood of confusion about source | official (U.S.) | https://www.uspto.gov/trademarks/search/likelihood-confusion | confirmed | "consumers are likely to mistakenly believe"; related goods may be "identical, similar or competitive". |
| I04 | 177 | Roblox IP guidelines: account action for repeated or serious infringement | official | https://create.roblox.com/docs/production/publishing/ip-guidelines | confirmed | "suspends or terminates the accounts"; users who "repeatedly or egregiously infringe". The page does not address copying game mechanics. |
| I05 | 177 | Non-unique metadata gets reduced priority | official | see D05 | confirmed | |

## 3. Tracker spot-check (RP:140-153, loop catalogue)

Each page read once with a browser (as a person would). All numbers: **third-party sampled** counts, never official. "Page now" = value on the page at read time (2026-10-20 evening ET). 12 of 13 rows checked on their cited tracker page.

| id | RP row | Claim as stated | Checked against (URL, A 2026-10-20) | Page now | Verdict |
| --- | --- | --- | --- | --- | --- |
| K01 | 140 Grow a Garden | peak 22,375,597 on 2025-08-23; snapshot 16,559; 7-day peak 107,178 | https://www.rolimons.com/game/126884695634066 | All-time 22,375,597, Aug 23, 2025; 7-day 107,178; players 16,012 | confirmed (snapshot moved). Cross-check: RoTrends shows 22.3M peak. |
| K02 | 141 Steal a Brainrot | peak 25,836,222 on 2025-10-11; snapshot 159,490 | https://www.rolimons.com/game/109983668079237 | 25,836,222, October 11, 2025; players 157,691 | confirmed |
| K03 | 142 Escape Tsunami | peak 4,996,032 on 2026-01-24; snapshot 2,823; 7-day peak 32,495 | https://www.rolimons.com/game/131623223084840 | 4,996,032, January 24, 2026; 7-day 32,495; players 2,314 | confirmed |
| K04 | 146 99 Nights | peak 14,153,173 on 2025-10-04; snapshot 108,092; 7-day peak 2,141,327 | https://www.rolimons.com/game/79546208627805 | 14,153,173, October 4, 2025; 7-day 2,141,327; players 96,463 | confirmed |
| K05 | 143 Fisch | peak 1,273,618 on 2025-10-18; snapshot 64,244 | https://www.rolimons.com/game/16732694052 | 1,273,618, October 18, 2025; players 51,672 | confirmed |
| K06 | 143 Fish It | peak 2,716,766 on 2025-12-07; snapshot 69,352; "Inspired by Fisch and Fishing Simulator" | https://www.rolimons.com/game/121864768012064 | 2,716,766, December 7, 2025; players 70,376; description has the credit line | confirmed |
| K07 | 144 Dig it! | peak 28,135 on 2025-02-01; snapshot 3; "Inspired by Fisch" | https://www.rolimons.com/game/76455837887178 | 28,135, February 1, 2025; players 8; credit line present | confirmed. Note: page shows "Average Playtime -20.00 Minutes", a tracker artefact (see TR3). |
| K08 | 147 Dress To Impress | peak 1,743,147 on 2024-12-14; 7-day peak 539,298 | https://www.rolimons.com/game/15101393044 | 1,743,147, December 14, 2024; 7-day 539,298 | confirmed |
| K09 | 148 RIVALS | peak 967,342 on 2026-02-14; snapshot 114,917 | https://www.rolimons.com/game/17625359962 | 967,342, February 14, 2026; players 89,031 | confirmed |
| K10 | 149 Blox Fruits | peak 2,781,531 on 2024-12-31; snapshot 112,675 | https://www.rolimons.com/game/2753915549 | 2,781,531, December 31, 2024; players 105,316 | confirmed |
| K11 | 150 Create a Robot Fighter | 24h mean 1,005 vs 7-day mean 301; peak 2,803 on 2026-10-20 | https://rovitals.com/game/81559365630003 | observed peak 2,803, Oct 20, 2026; 24h avg 1,235; 7-day avg 355 | confirmed (peak); page now differs on the means (live rolling windows). Do not cite the old means as current. |
| K12 | 151 Something is Wrong With My Dog | 24h mean 3,466 vs 7-day 1,261; peak 9,900 on 2026-10-20 | https://rovitals.com/game/133409496563091 | observed peak 9,900, Oct 20, 2026; 24h avg 3,812; 7-day avg 1,365 | confirmed (peak); means differ now. |
| K13 | 153 Anime Adventures | RoVitals 24h mean 6,413 vs 7-day 2,186 | https://rovitals.com/trending | listed as "[APRIL FOOL'S] Anime Adventures": 24h 6,710; 7-day 2,268 | confirmed (direction); numbers moved; listing is a growth-velocity rank, not official. |
| K14 | 145 Dead Rails | RoStats 7-day mean 14,813 | https://rostats.io/games/7018190066?range=all | page stuck on "Loading the latest data" in the browser pane | unverified (not re-checkable). Dead Rails in the June 2025 top-10 list is official (M08). |
| K15 | 167 Grow a Garden 2 | peak 929,371 on 2026-06-19; 7-day peak 2,984 | https://www.rolimons.com/game/97598239454123 | 929,371, June 19, 2026; 7-day 2,984; players 1,467 | confirmed |

Reading notes for the scout (derived):
- Rolimon's all-time peak for Grow a Garden (22.38M, Aug 2025) is higher than Roblox's July 2025 "nearly 22 million" and the 21.6 million Guinness figure. These are different dates, so there is no conflict, but a tracker record is not an official record. Label tracker peaks "highest recorded sample".
- Rolimon's "Average Playtime" values range from -20.00 minutes (Dig it!) to 78.71 minutes (Fish It!). These are tracker estimates and are not comparable with the GameAnalytics median session (G01). Do not store them as measurements.
- Rolimon's upvote count on the Grow a Garden page (9,439,083) differs from the Roblox API (9,439,081) by 2: the tracker reads the same API a few minutes earlier or later.

## 4. Tracker methods and model claims

| id | RP line | Claim | Provenance | Checked against (URL + A) | Verdict | Corrected value or note |
| --- | --- | --- | --- | --- | --- | --- |
| TR1 | 66, 119 | Rolimon's: "Most details are usually updated approximately every ten minutes" | third-party | https://www.rolimons.com/gametable (A 2026-10-20) | confirmed | Same footer: "Peak Players is Rolimon's highest recorded data point, and may not reflect a game's true peak". |
| TR2 | 68 | Statroblox: weighted geometric mean; range "never narrower than ÷/× 1.6" | third-party estimate | https://statroblox.com/methodology | confirmed | Exact sentence: "The range spans the strategies and is never narrower than ÷/× 1.6." The page reports no measured error rate; it says estimates are "modeled values, not audited income". The page's survey label is "Survey of 13 public trackers, October 2026". |
| TR3 | 66 | Rolimon's displayed playtime has no audited error rate | third-party | K07 page | confirmed (OPINION) | Evidence of at least one impossible value (-20.00 min). |
| TR4 | 69 | RoVitals Robot Fighter: 2 earned Robux per player-hour; central model divided and multiplied by three; not a confidence interval | third-party estimate | https://rovitals.com/game/81559365630003, "Earnings model & assumptions" panel | confirmed | Panel text: "2 earned Robux per player-hour", fixed "$0.0038 per earned Robux", "not a confidence interval; actual earnings may fall outside it". Illustrative daily range $75 to $680 (page now). |
| TR5 | 67, 305 | RoTrends: no verified export licence, price or error rate | third-party | https://devforum.roblox.com/t/rotrends-%E2%80%93-analyze-trends-keywords-and-game-stats/3471292 (posted 2025-02-13) | confirmed | Core features free; "Rotrends Pro" adds metrics and exporting. FAQ: "relies on public data collected from Roblox". No documented API. Game page shows Earning Rank, not a dollar revenue. |
| TR6 | 535 | RoStats quote "players × hours ÷ visits" for session length | third-party | https://rostats.io/methodology (A 2026-10-20) | unverified | Methodology page does not show this formula; it says session length is an estimate. |
| TR7 | 604 | RoVitals Trending quote "24-hour average concurrent players against its 7-day average" | third-party | https://rovitals.com/trending | corrected | Not verbatim. Page says "averaging 526 concurrent players over the last 24 hours against a 7-day average of 122" and ranks "by growth velocity, not by who is biggest". The idea is correct. |

## 5. Fixtures (raw JSON, one request per route)

Folder: `tools/tests/fixtures/trends/roblox/`. Saved exactly as returned (byte copy of the response body). Request header: honest User-Agent "StudioKit-fact-check/1.0 (research of public counters; single request per route)". No login, cookie or key. All answered HTTP 200. Player data check: no player names or IDs; `playerTokens` and `players` arrays were empty; the only people-like fields are the creator group "The Garden Game" (id 35789249) and user id 1 (the Roblox company account, creator of three old Roblox maps). No fixture dropped.

| File | URL (query as sent) | Fetch time (UTC, from response `date` header) | Rate header seen |
| --- | --- | --- | --- |
| `games_v1_games.json` | https://games.roblox.com/v1/games?universeIds=7436755782 | 2026-10-21T03:49:43Z | 300, 300;w=60 |
| `games_v1_votes.json` | https://games.roblox.com/v1/games/votes?universeIds=7436755782 | 2026-10-21T03:50:01Z | 200, 200;w=60 |
| `games_v1_favorites_count.json` | https://games.roblox.com/v1/games/7436755782/favorites/count | 2026-10-21T03:50:06Z | 200, 200;w=60 |
| `apis_universes_v1_places_universe.json` | https://apis.roblox.com/universes/v1/places/126884695634066/universe | 2026-10-21T03:50:12Z | 60, 60;w=60 |
| `games_v2_groups_gamesV2.json` | https://games.roblox.com/v2/groups/35789249/gamesV2?limit=10 | 2026-10-21T03:50:18Z | 3, 3;w=1 |
| `games_v2_users_games.json` | https://games.roblox.com/v2/users/1/games?limit=10 | 2026-10-21T03:50:22Z | 200, 200;w=60 |
| `games_v1_servers_public.json` | https://games.roblox.com/v1/games/126884695634066/servers/Public?limit=10 | 2026-10-21T03:50:29Z | 3, 3;w=60 |

Other requests, once each: `robots.txt` of games.roblox.com, apis.roblox.com (both HTTP 404), www.roblox.com, and the five trackers; chart pages top-playing-now, top-trending, up-and-coming, top-earning, top-revisited, fun-with-friends, top-rated (HTML read by curl to read the FAQ text).

Files `synthetic_games_votes.json` and `synthetic_place_universe.json` in the same folder were not made by this check (they appeared during the work). They are not raw responses.

Universe 7436755782 maps to root place 126884695634066 (fixture and Rolimon's page agree).

## 6. What I could not check, and limits

- Roblox has not published a reading of the new clauses TN1/TN2/TN7. The ruling "unclear" is my reading of the text, not Roblox's. A lawyer or a written Roblox answer is the only way to settle it.
- Official definitions of Top Earning, Top Revisited, Fun with Friends: not found (C03, C04). A DevForum thread is the only Roblox page that defines a chart beyond the two FAQ texts.
- RoStats data pages did not render in the browser pane (K14, TR6). Its terms were read through a plain fetch.
- Statroblox terms were read twice (browser-free fetches) and showed three short sections; they may be shorter than a full legal text.
- Open Cloud: schema and guides read, not every page (section 1.5).
- The paper's other sources (Steam, YouTube, Reddit, Discord, Google Trends, TikTok, mobile) are out of scope here (ticket J004-T04).
- Rate headers and the 50-ID batch limit are observed or documented today; Roblox can change them without notice (L01).
