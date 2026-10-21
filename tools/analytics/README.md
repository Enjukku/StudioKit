# tools/analytics: the analyst's data tool

> Author: tool builder · claude-opus-5-5 · medium · 2026-10-21. Job J013-T04. Python 3.11+ standard library only.

The analyst reads the game's own player data and says what changed and how sure we are. Rule: **no number comes from writing**. Every number comes from a saved pull (this tool's history) or a stats-helper calculation (this tool's `stats` commands).

## 1. Owner setup (once; the agent never sees the key)

1. Creator Dashboard → **Credentials** → **Create API key**.
2. **Access Permissions**: add the experience, then grant
   - system `universe-analytics`, operation **`universe.analytics:read`** (Analytics Query API), and
   - **`universe:read`** (Experiments API reads: list, get, stats). Do not grant `universe:write`: this tool never writes.
3. Optional and advised: an expiry date and an IP allow-list.
4. Put the key in **your** environment, not in a file in the repo and not in chat:
   - Windows (persists for new terminals): `setx ROBLOX_ANALYTICS_API_KEY "<paste key>"`, then open a new terminal.
   - PowerShell, this session only: `$env:ROBLOX_ANALYTICS_API_KEY = "<paste key>"`
   - macOS / Linux: `export ROBLOX_ANALYTICS_API_KEY="<paste key>"` (add to your shell profile to keep it).
5. Find the **Universe ID**: Creator Dashboard → the experience → copy Universe ID.

The tool reads the variable at each request and sends it only in the `x-api-key` header. It never prints, logs or saves it, never puts it in a URL, and removes it from every error text. If the variable is missing, every network command stops before any request (exit 2) and names the variable.

## 2. Commands

`python tools/analytics/analytics.py <command>`. Output: JSON on stdout, one short human line on stderr. Exit 0 ok, 1 a pull failed (partly), 2 refused before any request. Network commands take `--universe ID` or `--game-config PATH` (a game-side JSON file with `"universe_id"`); `--now ISO` overrides the clock.

| Command | Does |
| --- | --- |
| `pull --set weekly --universe ID` | Engagement, retention, monetization, last 42 full UTC days |
| `pull --set performance --universe ID` | Crashes, frame rate, memory, last 26 full UTC days (Roblox keeps 28) |
| `pull-funnel --funnel NAME --universe ID` | Docs two-step: find step ids over 90 days, then per-step user metrics over 28 days |
| `pull-metric --metric M --granularity G --start ISO --end ISO [--breakdown D ...] [--filter JSON] [--limit N] --universe ID` | One ad-hoc query (start inclusive, end exclusive, UTC buckets) |
| `dims --metric M --dimension D [--days 90] --universe ID` | Valid values of a dimension (e.g. `Country`, `FunnelName`) |
| `experiments list\|get\|stats [--id EXP] --universe ID` | Raw Experiments API reads, saved with pulled-at time. `stats` holds `isSrmDetected` (only after 24 h of running). Per-metric results have no documented endpoint |
| `status --universe ID` | Last successful pull per set; **warning when older than 21 days**; GAP note when data already expired |
| `show --metric M [--granularity G] [--breakdown D\|none] [--start ISO] [--end ISO] [--revisions] --universe ID` | Latest value per bucket, not-final flags, revision history. Without `--breakdown` every series is mixed in one list: use `--breakdown none` for the total, `--breakdown Platform` for that split |
| `sets` | The metric sets and catalog |
| `stats maturity --first-play YYYY-MM-DD --n 7 [--lag-days 1]` | Can a DN cohort value be read yet ("not mature" otherwise) |
| `stats diff --xa --na --xb --nb [--method newcombe\|wald]` | Two rates B - A: pp difference with Newcombe interval, relative % separately |
| `stats welch --ma --sa --na --mb --sb --nb` | Two means B - A, Welch interval (revenue warning) |
| `stats samplesize --pa --pb [--alpha] [--power]` | Players per arm, two-proportion |
| `stats samplesize-mean --sigma --delta [--power 0.8\|0.9]` | Players per arm, 16 (21) sigma^2/delta^2 |
| `stats srm --counts N1 N2 [...] [--planned W1 W2 ...] [--alarm-p 0.0005]` | Sample-ratio check; p < threshold → "invalid test: investigate" |
| `stats did --tb --ta --cb --ca [--se S1 S2 S3 S4]` | Difference in differences |
| `stats verdict --lower --upper --point --benefit --harm [...] [--rule default\|strict]` | PROPOSAL verdict rules (fact-check 02 §5) |
| `stats mix --segments JSON\|file.json` | Split a rate change into a segment-rate part and a player-mix part (the standardized rate; both weightings shown; identity, not a cause) |

`--filter` takes the API's filter list as JSON, for example `--filter '[{"dimension": "Platform", "values": ["Phone", "Tablet"], "operation": "In"}]'` (operations: `In`, `NotIn`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`, `Match`). How Roblox aligns `OneWeek` buckets is not documented (settle it with the first real pull). For distinct players in one exact week, query `DailyActiveUsers` with `--granularity None` from that week's first day to the day after its last.

Offline tests: `python -m unittest discover -s tools/tests -p "test_analytics_*.py" -t tools/tests`.

## 3. Pull on demand; the 21-day warning

No scheduler, no background service: the owner (or the analyst on request) runs pulls. Roblox keeps **performance metrics 28 days** (thumbnails 30, matchmaking 90, `RotraceTotalCalls` 365; standard metrics 1468). Our history is the only long record of performance. `status` warns when a set's last successful pull is older than 21 days, says how many days remain before a gap, or says which dates are already lost. Pull `performance` at least every 3 weeks.

## 4. Where data goes

`ANALYTICS_DATA_DIR/<universe id>/` if that variable is set, else `<repo>/.tools/analytics-data/<universe id>/` (`.tools/` is git-ignored). Append-only JSON lines; nothing is overwritten or deleted.

| File | Holds |
| --- | --- |
| `observations/metrics/<metric>.jsonl` | One record per returned data point: universe, metric, granularity, breakdown, series, filter, bucket time (UTC), value or `string_values`, `point_status`, the request body, operation path, pulled-at time, tool version, pull id |
| `observations/dimension-values.jsonl` | Dimension values found |
| `experiments/list.jsonl`, `get.jsonl`, `stats.jsonl` | Raw responses with pulled-at time |
| `pulls.jsonl` | One row per pull run: set, window, per-query result and error (redacted), points, not-final count |

## 5. Reading rules built in

- A re-pull of a bucket is a new record. `show` gives the newest per bucket and `--revisions` lists all.
- `Projected` and `NotStatisticallySignificant` points are kept with their status and marked `final: false`.
- A bucket the API did not return stays missing: never 0 (days with no activity may be omitted).
- Daily `DailyActiveUsers` values are never summed into unique players: pull `OneWeek` or `OneMonth` for distinct users.
- Requests the docs say fail are refused before sending: metric not in the catalog, unsupported granularity, start older than the metric's retention, over 2 years at a fine granularity, `limit` without `None` + breakdown.
- Errors: 500/2000 and 503/2002 retried (3 times, 1-2-4 s); a plain 429 waits for `retry-after`, else backs off from 1 s; 429/3000 (data-point budget) and 504/1000 split the date range in halves down to one bucket, then report; 400/2001, 401, 403, 404 never retried. 202 operations are polled up to 5 minutes. Pace: 2 s between metric POSTs (30/min), 0.6 s between experiment reads (100/min).

## 6. Files

| File | Holds |
| --- | --- |
| `analytics.py` | Command line |
| `ax_client.py` | Open Cloud client: key from env, header only, redaction, retries, polling, pacing; experiments GET only |
| `ax_pull.py` | Metric sets, request checks, range split, pull log, `status`, `show`, funnel, experiments save |
| `ax_store.py` | Record shape, append-only JSONL, latest and revisions, data dir |
| `ax_stats.py` | Stats helper; each formula's assumptions in its docstring |
| `metric_sets.json` | Catalog (names, granularities, retention from the docs) and the sets (PROPOSAL contents) |
