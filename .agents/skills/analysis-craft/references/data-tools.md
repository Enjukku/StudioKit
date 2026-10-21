# Data tools: pulling, storing and calculating

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-craft`. Tool: `tools/analytics/` (J013-T04; full command table and owner setup in `tools/analytics/README.md`). API facts: `knowledge/reference/analyst/01-roblox-platform-facts.md` §4 (docs mirror rev 7400643 + live reads 2026-10-21). Formulas and check values: `02-statistics-experiments.md` §4-5. Owner decisions J013-D4, J013-D6.

## 1. The key (read this first, every time)
- The owner's key lives only in the environment variable `ROBLOX_ANALYTICS_API_KEY`. The tool reads it at each request and sends it only in the `x-api-key` header.
- **You never see it.** Never ask for it, never print the environment (`env`, `set`, `Get-ChildItem env:`), never read shell profiles, never put it in a file, command line, URL or message. If a pull stops with exit 2 "environment variable ROBLOX_ANALYTICS_API_KEY is not set", report it as an owner action: "set the key (tools/analytics/README.md §1)".
- Scopes the owner grants: `universe.analytics:read` (Analytics Query) and `universe:read` (Experiments reads). Never ask for write scopes.

## 2. Which command answers which question
All commands: `python tools/analytics/analytics.py <command> --universe <id>` (or `--game-config <path>`). JSON on stdout, one human line on stderr; exit 0 ok, 1 a pull partly failed, 2 refused before any request.

| Question | Command | Notes |
| --- | --- | --- |
| Is our history fresh? | `status` | run first, every task; >21 days → warn the owner (performance data lives 28 days at Roblox) |
| Weekly page | `pull --set weekly`, `pull --set performance`, `pull-funnel --funnel <name>` per funnel | then `show` per metric |
| One metric, a breakdown, a filter | `pull-metric --metric M --granularity G --start ISO --end ISO [--breakdown D] [--filter JSON] [--limit N]` | start inclusive, end exclusive, UTC; names exact (catalog in `metric_sets.json`) |
| Valid values of a dimension (countries, funnel names, product ids) | `dims --metric M --dimension D` | |
| What did we get, and was it revised? | `show --metric M [--granularity G] [--breakdown D\|none] [--revisions]` | not-final points (`Projected`, `NotStatisticallySignificant`) are flagged. Without `--breakdown` every series (total and each split) is mixed in one list: use `--breakdown none` for the total, `--breakdown Platform` for that split |
| Running experiments, their state and SRM flag | `experiments list` · `experiments get --id` · `experiments stats --id` | per-metric results are not in the API docs: read the Creator Hub results page or the owner's export |
| Distinct players in one week | `pull-metric --metric DailyActiveUsers --granularity None --start <first day> --end <day after last>` | never sum daily DAU; how Roblox aligns `OneWeek` buckets is undocumented |

Calculations (no network, no key):

| Need | Command |
| --- | --- |
| Can this DN cohort be read yet? | `stats maturity --first-play YYYY-MM-DD --n 7 [--lag-days 1]` (lag 1 = PROPOSAL until measured) |
| Two rates, difference and likely range | `stats diff --xa --na --xb --nb` (B − A in points, Newcombe interval; relative % separately) |
| Two means | `stats welch --ma --sa --na --mb --sb --nb` (prints a warning for revenue-like data) |
| Players needed per arm (yes/no outcome) | `stats samplesize --pa --pb [--alpha 0.05] [--power 0.8]` |
| Players needed per arm (mean outcome) | `stats samplesize-mean --sigma --delta [--power 0.8\|0.9]` |
| Was the split fair? | `stats srm --counts N1 N2 [--planned W1 W2] [--alarm-p 0.0005]` |
| Update vs a comparison group | `stats did --tb --ta --cb --ca [--se ...]` |
| Did the rate fall because segments got worse, or because the player mix changed? | `stats mix --segments <json or file>` (the standardized rate: both weightings; an identity, not a cause) |
| Which verdict? | `stats verdict --lower --upper --point --benefit --harm [--guardrails JSON] [--integrity-failed] [--not-mature] [--stopping-failed] [--rule default\|strict]` |

A `stats` run on hypothetical inputs (to illustrate a mechanism) is saved with `hypothetical` in its file name and stays in Part 2. Save every `show` and `stats` output you use under a `calc/` folder next to the finding (the brief's folder wins) and cite it. Where no command fits (period sums, joins of saved outputs), write a short script in `calc/`, save its output, and cite both; rerun it once to confirm the same output.

## 3. Reading rules the tool enforces (and you keep in prose)
- History is append-only; a re-pull is a new record; `show` gives the newest per bucket.
- A bucket the API did not return is **missing**, never 0 (days with no activity may be omitted: unconfirmed).
- The tool refuses requests the docs say fail (metric not in catalog, wrong granularity, start beyond retention, >2 years at fine granularity). Add a new metric to `metric_sets.json` only from the docs' `metrics.md`, with its exact name.
- Errors: 401/403 = key or scope problem (owner action); 429/3000 = range split automatically; 400/2001 = a wrong field or dimension (read the message; dimension names differ by metric family: `AgeGroupV2` vs `AgeGroup`, `PayerStatus` vs `UserSegmentationPayerStatus`).

## 4. Reading rules for gaps in the data
| Situation | Rule |
| --- | --- |
| Retention comes as a rate with no cohort count (`Forward*Retention`) | cohort size ≈ `DailyActiveUsers` with `IsNewUser` = true on the first-play date; returners ≈ rate × that size; label both "estimate" until the first real pull confirms the denominator (§5). Never present an estimated count as measured |
| The API returns a value the tool calls immature | `stats maturity` wins for comparisons: show the API value as "early, may change" and leave it out of trends and tests until mature. While the 1-day lag is a PROPOSAL, readable dates in Part 1 say "about <date>" |
| A metric's unit is not stated (memory, crash rate) | write the unit as the docs' `metrics.md` gives it; if absent, "unit not documented" and keep comparisons within the same metric |
| A segment split does not add up to its total | report it as a data fault (checklist row 2 FAIL), use the split only for within-split comparisons, never for levels |
| Segment rates without counts | show the daily range (min-max) per segment, not an average of daily rates |
| Telemetry plan or game profile missing | the rows that need them say UNAVAILABLE; list "create `knowledge/design/telemetry.md` / fill `game-profile.md`" as an owner or lead action |

## 5. Unknowns to settle with the first real pull (record the answers in the game's overlay)
| Unknown | How to settle |
| --- | --- |
| Which date a `ForwardD7Retention` value sits on (first-play date or return date) | compare one known cohort with the Creator Hub retention table |
| Reporting lag (when yesterday's bucket appears) | note the newest bucket's time vs the pull time over two pulls |
| Whether no-activity days are omitted or 0 | pull a range that includes a known empty day |
| Whether experiment stats hold per-metric results | `experiments stats --id` on a running test; save the raw response |
| 401 vs 403 for a missing scope | the first auth error's message |
| `Forward*Retention` denominator (new users that day?) | compare one cohort's rate × `IsNewUser` DAU with the Creator Hub retention table's cohort size |
| How `OneWeek` buckets are aligned (Monday?) | one `OneWeek` pull; read the bucket start dates |
