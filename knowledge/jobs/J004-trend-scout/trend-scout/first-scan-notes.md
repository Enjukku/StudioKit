---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J004-T08"
supersedes: []
---
> Author: trend-scout · claude-sonnet-5-5 · high · 2026-10-21

# J004-T08 first scan: what I ran, what came out, what was wrong

## 1. What I ran (in order)

| # | Step | Result |
| --- | --- | --- |
| 1 | Read role, `market-trends`, `trend-scan` and their references, `tools/trends/README.md`, the weekly template, `sources.md`. Did not open the J004 job files or any evals folder. | done |
| 2 | `python tools/trends/trends.py registry` | 20 rows. `roblox.games`, `roblox.votes`, `apple.rss`, `youtube.data` allowed; `steam.current_players` unclear; `roblox.place-universe` not_allowed; the rest manual. |
| 3 | Roblox charts page, one read (WebFetch) | Empty shell (navigation and a "Processing" image). No chart data. Listed as owner read R1. |
| 4 | RoVitals top-by-players page, one read (WebFetch) | 25 rows with a place ID per game (links `/game/<id>`), current players, 24 h change, no timestamp. The IDs are **root place IDs, not universe IDs** (e.g. the Adopt Me ID matched the page's `data-place-id`). |
| 5 | Roblox public game pages, 16 reads (1 per game), with an HTTP client (`curl`, honest User-Agent, 3 s pause, fixed list, no login) | HTTP 200 each; `data-universe-id` found in the HTML for all 16. WebFetch was not used for this because it converts the page to text and drops attributes. |
| 6 | Watchlist written to `.tools/trend-data/watchlist.json`: 17 universes (16 from step 5, plus Grow a Garden from `watchlist.example.json`) | Grow a Garden confirmed after the run: API name and `created` 2025-03-25 match `loops.md`. |
| 7 | `collect-roblox` once | exit 0; **stored 85 observations** (17 games x 5 metrics: playing, visits, favorites, upvotes, downvotes). Samples 2026-10-21T04:25:42Z and 04:25:46Z. 0 failures. |
| 8 | `collect-apple` once | exit 0; **stored 222 observations**; 1 failure: `https://rss.marketingtools.apple.com/api/v2/br/apps/top-free/25/apps.json` timed out (tool makes 0 retries by design). 9 of 10 feeds. `gb` top-paid returned 23 rows and `jp` top-paid 24 (not 25). |
| 9 | `collect-steam` once (expected refusal) | `REFUSED: steam.current_players: registry ruling is 'unclear' ... no request made`, exit 2. Not worked around. |
| 10 | `collect-youtube` once (expected refusal) | `FAILED: environment variable YOUTUBE_API_KEY is not set; no request made`, exit 1. Registry says `allowed`, so this is a missing key, not a ruling. I did not look for, set or ask for a key. |
| 11 | Google Play top page, one read | Shell only (menus, no chart). Owner read R7. |
| 12 | Netflix news page (the registry's example route), one read | HTTP 404. |
| 13 | 4 web searches (to find place IDs of loop-reference games; to look for context on the leads and the Halloween event) | Three searches for Grow a Garden 2, the risky-retrieval game and Dead Rails gave no usable place ID. Two searches gave context snippets, used only as pointers and labelled 3P secondary, unverified. |
| 14 | `prune` | `youtube.data: removed 0`. |
| 15 | `page` (twice; the second after I fixed one watchlist label) | Wrote `trend-week-2026-10-20.md` and `.html` in `.tools/trend-data/pages/`. No SVG charts (no history). |
| 16 | Scout page written | `.tools/trend-data/pages/trend-week-2026-10-20-scout.md` (12 sections: the 10 of the template plus owner request and open points). |
| 17 | `scout-log.md` written | `.tools/trend-data/scout-log.md` |

No key, username or viewer data was written anywhere. Creators were not tracked this week.

## 2. Results in one paragraph

17 universes, 1 sample each, coverage 0 %. No growth, flag or chart is possible. 0 cards; 2 emerging leads (L1 egg-steal cluster, L2 dice-roll newcomer), both with rights gate HOLD and no score. Apple ranks show no Roblox app. Everything else is in the owner read request (section 11 of the scout page, R1-R10).

## 3. Problems with the skills, tools and brief (C4)

Format: **where** | what is unclear, wrong or missing | what I did | suggested fix.

### 3.1 trend-scan (skill and tools)

| # | Where | Problem | What I did | Suggested fix |
| --- | --- | --- | --- | --- |
| T1 | `trend-scan` §3 step 2 vs `formulas.md` §1 and `config.json` | **The weekly steps say "run collect-roblox" as one action, but the formulas need samples at most 60 minutes apart and 90 % coverage.** One run per week gives 0 % coverage for ever. Nothing runs on a timer. The skill never says how often to sample. | Reported as Q1. | State the sampling rule in `trend-scan` (about 24 runs a day) and link it to the schedule plan; or say plainly that weekly pages need a scheduler. |
| T2 | `sources.json` `valid_until` 2026-10-31 | Roblox collection stops 2026-10-31. Complete UTC days left after this scan: 10-22 to 10-31 = 10. Two non-overlapping weeks need 14. So no valid g7 can exist before the ruling ends, even with hourly sampling from tomorrow. (My arithmetic from the tool rules; I did not simulate it.) | Reported as Q2. | Owner decision on data after 2026-10-31 (the skill says "owner decides"); until then the skill should say the first g7 is out of reach. |
| T3 | `trends.py page` and `outside_page.build` | The page's week is the 7 complete days **before** `--as-of`. A scan run on the day after the week ends puts every sample outside the week, so the tool page shows `current-week coverage min 0%` and, in the Apple section, **"No data this week" although 222 Apple rows were stored**. Misleading. | Described the real state in the scout page (section 5). Did not change `--as-of` (the brief fixes week_ending 2026-10-20). | Show the newest snapshot even when it falls outside the week, labelled "latest snapshot (outside the week window)". |
| T4 | `sources.md` §2, "agent may fetch" column | (a) The Roblox charts page and the Google Play top page are JavaScript shells: an agent fetch returns no chart. So these are always owner reads in practice. (b) `sources.md` and the brief say to take universe IDs "from the public game page", but never say **how**: WebFetch text drops the `data-universe-id` attribute; `resolve-place` is refused. I used an HTTP client on the raw HTML (16 reads, 3 s pause, fixed list). "No scripts" in the same section could be read as forbidding that. | Did (b) as above; recorded it as E12 and here. | Add a documented, allowed step for universe ID from the game page (or a tool command for it) and say whether a shell HTTP client counts as a visitor read. Move charts and Google Play to the owner column or mark them "needs JavaScript". |
| T5 | `sources.json` row `release.calendars` | The example route `https://about.netflix.com/en/news` returns 404. | Listed as an access failure. | Lead fixes the route (I may not edit `sources.json`). |
| T6 | `sources.md` / role tools | The role has `WebSearch`, but no registry row or skill rule says whether search results may be used, or how to label them. | Used 4 searches; labelled results "3P secondary, unverified" and used them only as pointers to check (E09, E10). Two results disagreed with each other on a peak. | Add a ruling and a label for search snippets, or forbid them. |
| T7 | `WebFetch` for RoVitals | The fetch tool runs a small model over the page, so numbers reach me as a summary. I cross-checked only by magnitude against the Games API (e.g. Brookhaven 210,017 vs 197,767 read at different times, RoVitals time not recorded). | Used only ranks 1, 9, 12 and the seed list; not the 24 h change column (definition not stated on the page). | A rule for how to verify hand-read tracker figures (second read, or owner paste). |
| T8 | `apple_collector.py` `parse` | An item whose id is not all digits is skipped silently, with no count in the log. `gb` and `jp` top-paid returned 23 and 24 rows, not 25. I did not check whether items were dropped or the feed was short. | Recorded in E06 as a doubt. | Log the count of skipped items and the feed's own length. |
| T9 | `trend-scan` §3 step 8, `scout-log.md` | The skill names `<data_dir>/scout-log.md` but gives no columns. | Invented a small table (IDs, dates, labels, decisions). | Add the columns to `handoffs.md` or the template. |
| T10 | `README.md` / `watchlist.example.json` | The example holds a universe ID (Grow a Garden) with a kit label; the page prints the **watchlist label**, but the records store the **API name** (API wins). My first label contained a note and leaked into the first page render (fixed, page re-rendered). | Fixed the label. | Say which name each output uses. |
| T11 | `trend-scan` §3 step 7 | "Add rising games seen on charts" assumes the scout can read charts; it cannot (T4a). Without R1 the watchlist can only grow by size ranking. | Reported as Q3. | Make R1 a standing owner read in the weekly steps. |
| T12 | `trends.py page` PERMISSION STATUS line | Lists only the two Roblox rows; Apple, YouTube and Steam appear only inside their section. The template says per source group. | Wrote the full status in the scout page. | List every registry row used. |

### 3.2 market-trends

| # | Where | Problem | What I did | Suggested fix |
| --- | --- | --- | --- | --- |
| M1 | `opportunities.md` and the template §2 | There is **no form for a day-0 week**. Cards need 9 fields that need a comparison period; "emerging lead" is named in `trend-scan` §3 but has no format. | Wrote 0 cards and a two-column "emerging leads" table with the same fields, marked not scored and not a card. | Add an "emerging lead" form (shorter than a card, with the missing evidence listed) to `opportunities.md` and the template. |
| M2 | `loops.md` §3 | The reference games have **no universe or place IDs**, and I may not use numbers from memory. The brief wanted them on the watchlist. Only Grow a Garden had an ID (from the example file). Dig it! is "one universe" without saying which. | Put the missing games in R10 (owner supplies game URLs). | Add the IDs (with the date checked) to `loops.md`. |
| M3 | `loops.md` §3 vs `signals-and-metrics.md` §4 | The family table gives "highest recorded sample" numbers (3P-S) taken from trackers, while `sources.md` says Rolimon's is not used for studio decisions without consent. The note only says "tracker". Which tracker made these numbers is not stated. | Did not reuse them. | Name the tracker and read date per row. |
| M4 | Template §3 | No column holds a **single-sample level**, the only measured number on day 0. The tool page has one (Current CCU). | Added one column "Single sample playing" to the template table (a deviation, stated in the page). | Add it to the template. |
| M5 | Template header | "(<studio timezone>)" but `game-profile.md` is empty. | Used UTC and said so. | Fix the profile or default to UTC in the template. |
| M6 | `market-trends` §3 step 4 vs day 0 | Steps 4 to 7 (alternative explanation, breadth, timing) assume data that does not exist on day 0; there is no instruction to write "not checked". | Wrote "Not checked" with the list of causes. | One line: "on day 0 list the checks as not done". |
| M7 | Role file vs brief | The role file says effort medium; J004-D2 says high inside J004. The brief resolved it. | Followed the brief. | none |

## 4. Choices I made that the lead may reverse

| # | Choice | Reason |
| --- | --- | --- |
| 1 | 17 games, not 30 | The brief's cap is "at most 30"; the loop references without IDs could not be added; I kept the volume low. |
| 2 | 0 cards, 2 leads | No gate can pass on one sample; a card would need invented values. |
| 3 | R1-R10 owner reads | The agent could not read charts or Play; the other sources are owner-only by `sources.md`. |
| 4 | Used an HTTP client for the 16 game pages | See T4. If the lead rules this out, the universe IDs should be treated as unverified (they were confirmed afterwards: 16 of 16 names match their RoVitals titles apart from event prefixes; the API returned data for all 17). |
| 5 | Did not add the "The Hollow" event to `event_windows` | Not confirmed by Roblox (R9). |
| 6 | Did not open `schedule-plan.md` | The brief forbids opening J004 files outside my folder. Q1 may already be answered there. |
| 7 | Left the first `page` label fix as one re-render | Cost: 1 extra local run; no network. |

## 5. Checks

| Check | Result | Evidence |
| --- | --- | --- |
| C1 collect-roblox and collect-apple once each; counts and failures noted | pass | section 1 steps 7 and 8; stores in `.tools/trend-data/observations/` |
| C2 every number in the scout page has a label and read time | pass, with one judgement call | labels in cells and column headers; the section 4 "Leaders" column carries its label and time in the header; counts of our own items (17 games, 8 titles) are counts, not market numbers |
| C3 owner-read request lists page, region, window, fields per source | pass | scout page section 11, R1-R10 |
| C4 notes list every unclear, wrong or missing place per skill | pass | section 3 (trend-scan T1-T12; market-trends M1-M7) |
