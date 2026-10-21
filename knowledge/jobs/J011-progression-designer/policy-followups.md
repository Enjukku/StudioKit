---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J011 fact-check follow-ups (FC-R PP-1..PP-8, AN-1..AN-4, WN-1; lead-notes N2 G6)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-21

# J011 follow-ups: platform-policy, analytics, whats-new

Source list: `knowledge/reference/progression/fact-check-roblox.md` ("platform-policy follow-ups", "Other kit files"); `lead-notes.md` N2 G6. Every claim re-checked on 2026-10-21 against the docs mirror (`M/` = `knowledge/external/roblox-creator-docs/`, upstream 7400643) or, for sources outside the mirror, re-read with curl (DF 4654622 Discourse JSON; Help Center API copies of articles 13722260778260 and 47965190783892). Files: `PP-S` = `.agents/skills/platform-policy/SKILL.md`, `PP-R` = `.../references/rules.md`, `AN` = `.agents/skills/analytics/SKILL.md`, `WN` = `knowledge/reference/roblox/whats-new.md`.

| id | verdict | evidence re-checked | change |
| --- | --- | --- | --- |
| PP-1 | applied | Ad Standards API copy: first paragraph says ads may not be personalized for users under 18; "Last Updated: Oct 9, 2026". No sentence on engagement data to advertisers (searched "shar", "collect", "engagement", "data") | PP-R header: Help Center readable by curl/API. Ads row "personalised to under-18" re-sourced to Ad Standards; "no engagement data" half dropped and listed under "Not verified". Rewarded-video row also cites Ad Standards § Publisher Integrity |
| PP-2 | applied | DF 4654622 JSON: post 1 by `dinobotsnarl824`, `staff=false`, no title or group, category 36, Roblox voice ("our Community Standards") | "staff" → "official Roblox announcement" in PP-S header and P-03, PP-R header and § A |
| PP-3 | applied | `M/production/monetization/paid-random-items.md:96-123`: six treatments, one is "Blocking the purchase ... with an error message" (:116). DF FAQ: error after Buy is "technically compliant" but confusing; hide or replace instead | PP-R § A lists all six; error-message block = player-experience issue, not a violation. PP-S P-03 says the same |
| PP-4 | applied | `paid-random-items.md:130` ("or other paid items"); `M/_api-reference/classes/PolicyService.yaml:118`; DF post 31: false restricts all paid items, including direct Robux and paid-currency buys. DF post 1: trading and acquiring are separate checks | PP-R trading row states the rule (no longer "ours"); removed from "Not verified" |
| PP-5 | applied | DF posts 29, 54 (previewed next outcome counts; contents that reload each minute count; random cosmetic visuals do not), 30 (skill-based variance does not), 60 (luck game pass counts) | PP-R § A definition row: counted and not-counted cases with post numbers |
| PP-6 | applied | `paid-random-items.md:55`: exact disclaimer and "four or more decimal places lower" rule; DF FAQ repeats it | PP-R odds row: disclaimer text (12 words) and worked example 0.0123456 % → 0.012346 % |
| PP-7 | applied | Help Center 47965190783892 (updated 2026-10-08): "must integrate the PolicyService API" (5 areas); pushy wording "not considered a best practice", with the avoid/use table. `M/production/publishing/kids-and-select.md:48-51`: full parental controls through age 12. Newsroom 2026-06-16 not re-read (FC-R FB17) | PP-R § D new row (MUST PolicyService; SHOULD NOT pushy wording; parent spend limits until 13 → handle a declined prompt, ours). PP-S § 6 new line on pushy wording |
| PP-8 | applied | `M/production/monetization/regional-pricing.md:103` (1-1000), `:116` (call at join), `:119-126` (array of `{UserId, PriceLevel}`); `M/_api-reference/classes/MarketplaceService.yaml:769-795` (dictionary keyed by user id strings; level 100 = 100 Robux suggested) | PP-R price-level row: owner class `MarketplaceService`, scale, both shapes, the meaning conflict, test in Studio |
| G6 | applied, stance marked "ours" | `M/production/promotion/content-maturity.md:367`: gambling = exchanging money, Robux or in-game items of value for a game of chance; no playable or simulated gambling. `paid-random-items.md:104-105`: currency prizes from a fixed-order spin are a permitted treatment, so currency prizes are not banned as such | PP-R § A new row: a paid roll that pays back the currency it was paid with = treat as simulated gambling, do not build (ours); unclear cases to the owner. § D gambling row and PP-S § 6 link to it |
| AN-1 | applied | `M/production/analytics/event-types.md:93` (resource types 10); `economy-events.md:121` (up to five currencies); `AnalyticsService.yaml:474` (5 per experience) | AN T-05: plan 5 or fewer, conflict named |
| AN-2 | applied | `event-types.md:76-78`: "Total AnalyticsService requests per minute", 120 + (20 * CCU); no scope, no CCU definition | AN T-05 drops "per server"; budget under 20 calls per player per minute (safe under both readings, ours). Self-check updated |
| AN-3 | applied | `AnalyticsService.yaml:598-656`: `LogJourneyEvent(player, journeyName, nodeName, journeySessionId, customFields)`, Sankey in Creator Hub. No guide page in `M/production/` (grep "journey") | AN T-04 adds the method with "reference only, check the chart exists". WN roadmap row updated |
| AN-4 | applied | `funnel-events.md:107` (10 most recent `funnelSessionId` per user per funnel), `:19` (180-day expiry); `funnelSessionId` is a parameter of `LogFunnelStepEvent` only (`AnalyticsService.yaml:551`) | AN T-04 adds both facts |
| WN-1 | applied | WN:114 row (2026-05-26 clarification) vs WN:147 | WN:147 reworded: the clarification is the one 2026 paid-random change found |
| X-1 | applied (found in passing) | `content-maturity.md:50` is the age-restricted alert, not the gambling rule (`:363-367`) | PP-R § D gambling row citation fixed |

## Not done (out of this ticket's list)
- FC-R "Changes the skills must make" items that name other skills (FB13 64.15 % example, FB29 three server-only guide pages, FB24b retention formula, Luau numbers): not in PP/AN/WN/G6; left for the progression and analyst skills' owners.
- `.claude/` copies regenerated by `python tools/sync_harness.py`, not edited by hand.

## Status
done. Gate `python tools/verify.py` 2026-10-21: RESULT FAIL, one failure, not from these files: `kb_index --lint` ERROR `knowledge/jobs/J007-modeler/ledger.md:1` missing frontmatter (another job's untracked file). These files have no lint error or warning. `kb_index --check` was stale (J007, modeler papers, docs-map and these edits); regenerated with `python tools/kb_index.py`, now PASS. sync_harness, tests (485), size checks PASS.
