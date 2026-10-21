> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21. Kit reference: universal (J004). The registry `tools/trends/sources.json` is the single source of truth for what may run; this page explains it. Evidence: `knowledge/reference/trends/fact-check-roblox.md` (**FR** §1) and `fact-check-outside.md` (**FO** §3-§5), checked 2026-10-20/21. Re-check every ruling at least once a year and whenever a source changes its terms.

# Sources: what may be read, how, and for how long

## 1. Rulings (as of 2026-10-21)
| Source | Ruling | How | Auth | Storage | Why |
| --- | --- | --- | --- | --- | --- |
| Roblox Games API and all roblox.com pages | **not used** (owner J004-D10) | — | — | — | the owner does not want any risk to the studio's Roblox account: Terms from 2026-11-01 §9.2 ban automated data gathering in connection with AI. Roblox numbers come from RoTrends/SullyGnome on request or the owner's own reading |
| Roblox place → universe lookup | not allowed | look up by hand on the game page | — | — | route not in the documentation (FR §1.2) |
| Roblox servers list | not built | — | — | — | 3 calls per 60 s; carries player identifiers (FR §1.2) |
| Roblox charts | manual | read by hand | none | — | public pages; no documented chart API |
| Trackers (RoVitals, Statroblox; Rolimon's, RoTrends, RoStats) | manual | read by hand; **Rolimon's not used** for studio decisions without written consent | none | short notes | Rolimon's, RoTrends, RoStats forbid automation; Rolimon's licence is personal, non-commercial (FR §1.3) |
| Apple RSS top-free, top-paid | allowed | `collect-apple`, one fetch per country and feed per day | none | none stated | feed made for download (FO AP); no game filter, no verified top-grossing |
| YouTube Data API | allowed | `collect-youtube` on a fixed panel | env `YOUTUBE_API_KEY` | **30 days** for every value, pages included (`prune` daily) | developer policies (FO YT-03) |
| Steam current players | unclear (refused) | `collect-steam` once the owner rules | env `STEAM_WEB_API_KEY` | none stated | licence names end-user display (FO ST-03/04) |
| Steam store charts, SteamDB (view only), Google Play, TikTok Creative Center and Top Ads, Instagram, Google Trends, Twitch directory, YouTube website, Reddit, Discord, release calendars | manual | `import-manual` CSV | none | short dated notes | no allowed automated route (FO §3-§4) |
| Not used | — | Sensor Tower and other paid data (no contract), TikTok Research API (commercial users excluded), Twitch Helix (24 h cache), Instagram Graph API (gated), Google Trends alpha (application), Reddit and Discord APIs | | | FO §3 |

A 200 response is not permission. A blocked page is reported, never bypassed. Only the lead changes a ruling, after a dated check.

## 2. Manual entry (how to read by hand)

**Who may read.** An AI agent fetching a page counts as a robot. So "manual" splits in two:
| Agent may fetch one page as a visitor (no loops, no login, one read per page per scan) | Owner reads (the agent asks the owner for the figures, or the owner pastes them) |
| --- | --- |
| Official news, filings and release-calendar pages; Google Play top-chart pages (robots.txt allows `/store/apps/top`, but they are JavaScript shells, so in practice the owner reads them) | RoVitals (legal-only mode, J004-D12), Rolimon's, RoTrends, RoStats (ban robots), Statroblox (robots.txt bars AI crawlers), TikTok Creative Center and Top Ads (Terms bar scraping and crawling), Instagram (scraping needs written permission), Google Trends explore (robots.txt disallows), Reddit and Discord (ban scraping), Steam store charts and Twitch directory (Terms not checked), SullyGnome Twitch stats (ToS bar automated scraping; robots.txt bars GPTBot; snippets with credit allowed) |
**Legal-only mode (owner J004-D12).** The agent never reads RoTrends, SullyGnome or any site whose terms bar robots, even on request. The owner reads them in their own browser and pastes figures or gives an export file; the scout converts the file into the manual CSV (`kind` third_party_sampled, or third_party_estimate for money) and credits SullyGnome where its figures appear.

A page that blocks the fetch, asks for a login or shows a CAPTCHA is left alone and listed as "owner reads". Owner-pasted figures are recorded with `MAN` and the owner as reader.

- **JavaScript-only pages** (Roblox charts, Google Play charts) return an empty shell to an agent: treat them as owner reads every week (standing request R1: Roblox Most Popular, Top Trending and Up-and-Coming, top 50 each, with game URLs).
- **Universe IDs.** Taken from what the owner pastes or from the RoTrends page read on request (its game URLs carry the universe ID). No agent reads of roblox.com (J004-D10).
- **Search results** (WebSearch) are pointers only: label "3P secondary, unverified", never put a search-snippet number in a table; open the source page (if allowed) or ask the owner.
- **Summarising fetch tools** (WebFetch passes the page through a model): a number read that way is re-read from the raw page (one plain HTTP read) or pasted by the owner before it goes into a table; keep its read time.
Read the public page as any visitor: no login that bypasses a gate, no browser automation, no scripts, no screenshots of other people's content. Record facts only, in `tools/trends/manual/manual-entries.template.csv` (copy it):

see the header of the template file (includes `kind`)

| Source | Record | Must include |
| --- | --- | --- |
| roblox.charts | chart name, rank, universe ID if shown | chart name in `window`, read time |
| roblox.trackers (RoTrends: owner reads or exports, J004-D4; its history charts give 3P-S growth evidence when our own Roblox history is missing) | highest recorded sample and date, 24 h / 7 d means; a tracker revenue or playtime figure with `kind` = third_party_estimate | tracker name, read time; means only with read time |
| steam.charts | rank, app ID, free-to-play flag | region (country or global) |
| google.play | rank, app, category | region, chart |
| tiktok.creative-center / top-ads | hashtag, rank, figures as shown; advertiser and mechanic for ads | region, time window |
| google.trends | term or topic, 0-100 values | geography, category, interval; identical comparison set |
| instagram, youtube.website, twitch.directory | name, figures as shown | read time |
| twitch.sullygnome | game, change in watch time and stream time, window (3/7/14/30 d), language filter | read time; credit "SullyGnome.com" on the page; the owner's CSV/Excel export may be given to the scout to convert |
| reddit, discord | topic, date, link | no usernames, no message copies |
| release.calendars | title, date and its kind (announced / released) | URL |
Column `kind` sets the figure's label: blank = manual reading (MAN), or official, third_party_sampled, third_party_estimate, developer_statement; money figures (revenue, earnings, Robux) need third_party_estimate or developer_statement. Then run `python tools/trends/trends.py import-manual <file>`: rejected rows are listed with line and reason; an identical row imported again is skipped.

## 3. Keys and secrets
Keys live only in environment variables (`YOUTUBE_API_KEY`, `STEAM_WEB_API_KEY`) set by the owner on the machine that runs the tools. Never in the repo, notes, chat, records, fixtures or logs. The scout never creates accounts or keys; it asks the owner.

## 4. Storage
- Data dir: `TREND_DATA_DIR` (default `.tools/trend-data/`, gitignored). Pages in `<data_dir>/pages/`.
- YouTube values are deleted 30 days after fetch, and **every file in `<data_dir>/pages/` is deleted 30 days after its last change** (pages are working copies). Every tool command prunes first; the daily `prune` is a backstop (J004-T12).
- The scout's lasting record (cards, alerts, outcomes) is `<data_dir>/scout-log.md`: IDs, dates, labels and decisions only, no YouTube API values, so it may be kept.
