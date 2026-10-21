# Testing and measurement with the analyst

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-craft`. Sources: `knowledge/reference/marketing/03-...md` §2 (ME ids), §8 (OQ ids); `01-...md` §4-5 (TI, IM); fact-check `fact-check-roblox-discovery.md` (FD ids, read 2026-10-21). The analyst role is planned: until it exists, use the `analytics` skill yourself and send the test spec to the lead, who holds the analyst ticket (J012-D6).

## 1. What each "test" really is
| What changes | Roblox tool | What the result can show | Label in every report |
| --- | --- | --- | --- |
| Home thumbnails (2-5 active) | thumbnail personalization (Creator Hub; Open Cloud API labelled Experimental) | which images Roblox's bandit favours per audience, by qPTR | **adaptive allocation**, not A/B (FD-35..36) |
| Title, description | none (searched 2026-10-21) | a before/after change around a logged rename | **observational** (TI-15) |
| Icon | none; one icon per locale | before/after around a logged swap | **observational** (FD-21, IM-22) |
| Gallery order, native video | none; video annotations in Acquisition, Engagement, Retention | before/after with the annotation | **observational** (FD-50) |
| Sponsored ads creatives | Ads Manager (delivery logic: see `marketing-design/references/channels.md` §3) | attributed results per creative | **attributed**; never "incremental" without a holdout |
| In-game onboarding, offers, config | Creator Hub Experiments (in-game config and matchmaking) | a real randomized A/B inside the game | **randomized**; owned by the analyst and the builders, not marketing (FD-73) |
| Notification text variants | a new string per variant; `category` splits analytics | CTR per string, 100 impressions needed per notification | **randomized** only if the tool assigns at random; check the page (FD-63..64) |
| Title / icon understanding | none: a comprehension check you run | misreadings, competing readings | **self-report**; never a click-rate estimate (TI-16) |

A title with no native test still gets tested honestly: comprehension check first, then one logged change at a time, other packaging held still where possible, results split by acquisition source, read as observational (TI-15..16, OQ-04).

## 2. Before any test: the analyst's spec (write it first)
| Field | Content |
| --- | --- |
| decision | what the owner will decide from this result |
| surface and population | Home RFY / Search / ads / share link; new vs returning; eligible cohort |
| primary metric | the exact dashboard label (qPTR as labelled today, not "CTR"), numerator, denominator |
| guardrails | first-play bounce bands (< 60 s, 61-180 s), playtime, D1 / D7 of the arriving cohort; unsubscribes or opt-outs for messages |
| window and maturity | earliest read date; D7 = return on the 8th day after the first session ended (FD-66); 30-day metrics need 30 days (FD-67) |
| what stays still | other packaging, prices, events; what else ships in the window |
| what would count as misleading traffic | for example clicks up while first-play bounce rises |
| what would change the decision | stated before looking |

## 3. Reading results
1. **Counts beside every rate.** Low volume, adaptive allocation or a missing breakdown = "inconclusive", never "winner" (ME-19, OQ-12).
2. **Mark measurement breaks.** 2026-10-12: Roblox changed how Home, Search and Charts impressions, clicks and plays are recorded; counts can rise and PTR can dip a little; history unchanged (FD-51..52). Any review across that date says so. Same for dashboard renames (qPTR vs PTR, FD-42..43).
3. **Keep metric names exact.** Never relabel qPTR as PTR; never compute a "conversion" from two metrics with different denominators (ME-24).
4. **Separate cohorts.** Organic RFY players, ad players, share-link players, returning players: never mixed in one rate. Immature cohorts are "pending" (ME-10).
5. **Patterns are leads, not diagnoses** (ME-25): poor early hold → inspect the opening; good hold, weak clicks to play → game fit or call to action; clicks up but bounce up → promise mismatch or onboarding.
6. **Attribution is not incrementality.** A share link or ad attribution says where players came from, not whether they would have come anyway (ME-14). A before/after rise alone proves nothing about cause.
7. **Never buy views or fake engagement** to improve a number (ME-26).

## 4. Tracking tools
| Tool | Facts (V) | Use |
| --- | --- | --- |
| Share links | tracked links, no per-game limit; group-owned games need the Manage share links permission; custom LaunchData optional (FD-68) | one link per creator, channel and creative; keep the campaign key in the campaign record |
| Acquisition dashboard | sources: Home recommendations, Continue, Search, Charts, sponsored/search/portal ads, teleport, Other (includes external); the live page also lists Today's Picks, Home other and Friends (FD-65) | read new users by source; never add sources up as if disjoint |
| Open Cloud APIs (2026-08-24) | Analytics Query (Beta, asynchronous, poll for results), Events/Updates and Experiments (Experimental), Thumbnail Personalization (Experimental: creating a configuration deactivates the old one and starts new statistics; updating keeps id and statistics) (FD-69..71) | only with an owner-provided key outside the repo; log create and update as different operations; verify the live state after any change. No native MCP yet |

## 5. Weekly report
Use `templates/marketing/weekly-report.md`. An unavailable value is `UNAVAILABLE`, never 0. Spend, creator fees and production cost stay in separate lines before any cost-per-player figure. Urgent problems (policy, spend, misleading creative, player harm) go to the owner at once, not in the weekly report.
