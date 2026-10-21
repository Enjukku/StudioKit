# tools/trends: trend scout data tools

> Author: tool builder A · claude-opus-5-5 · medium · 2026-10-20. Job J004-T05. Python 3.11+ standard library only.

## Commands

| Command | Does |
| --- | --- |
| `python tools/trends/trends.py registry` | List sources, rulings, storage limits |
| `python tools/trends/trends.py collect-roblox [--watchlist P]` | One sample of every watched universe (R1 details + R2 votes), at most 50 ids per call whatever `config.json` says. Exit 2, no request, if a row is not `allowed`. A 429 that says stop ends the run (no further request); batches already fetched are stored |
| `python tools/trends/trends.py page [--as-of ISO] [--out DIR]` | Write `trend-week-<last complete UTC day>.md` and `.html` to `<data_dir>/pages/`. Uses only samples at or before `--as-of`. PERMISSION STATUS lists every registry row the page draws on |
| `python tools/trends/trends.py prune [--now ISO]` | Delete records older than `storage_limit_days` for every source that has one, and expired pages (see the 30-day rule below). A file it cannot open is skipped and reported (exit 1); the rest is still pruned |
| `python tools/trends/trends.py collect-apple [--watchlist P]` | Apple RSS ranks: one fetch per country and feed of the panel. Exit 2, no request, unless `apple.rss` is `allowed` |
| `python tools/trends/trends.py collect-steam [--watchlist P]` | Steam current players, one call per watched app (key: env `STEAM_WEB_API_KEY`). Same refusal rule; fail soft per app; skips an app until its `Cache-Control` max-age has passed |
| `python tools/trends/trends.py collect-youtube [--watchlist P]` | YouTube panel statistics (key: env `YOUTUBE_API_KEY`). Same refusal rule; `search.list` capped by `youtube_search_daily_budget` over any trailing 24 h |
| `python tools/trends/trends.py import-manual CSV` | Rows read by hand (template `manual/manual-entries.template.csv`). Exit 1 if any row is rejected (with its line number); good rows are still written; a row already imported is skipped and counted |
| `python -m unittest discover -s tools/tests -p "test_trends_*.py"` | Offline tests |

Data dir: env `TREND_DATA_DIR`, default `<repo>/.tools/trend-data/` (gitignored). Watchlist: `<data_dir>/watchlist.json` (copy `watchlist.example.json`). Nothing runs on a timer. **Every command except `registry` first prunes** (records and pages, as `prune` does), so a storage limit holds even when nobody runs `prune`.

## Files

| File | Holds |
| --- | --- |
| `sources.json` | Source-permission registry (one row per source) |
| `config.json` | Thresholds and collector settings; every value labelled PROPOSAL with its paper line |
| `trend_store.py` | Record shape, `make_record`, `validate`, `append`, `read`, `prune`, `series`, `load_config`, `data_dir` |
| `trend_registry.py` | `load`, `require_allowed` (raises `PermissionRefused`), `permission_version`, `prune_all` |
| `trend_http.py` | `PoliteClient(settings, fetch=..., sleep=..., clock=..., rng=...)`: interval, 429 + Retry-After, backoff with jitter, bounded retries, User-Agent. After a 429 that says stop (Retry-After over `max_retry_after_s`, or 429 after the last retry) the client makes no further request this run |
| `roblox_collector.py` | Roblox parse and collect |
| `trend_metrics.py` | Pure formulas (player-hours, coverage, g7, momentum, breakout, fade, playtime estimate) |
| `trend_page.py` | Weekly page (markdown + self-contained HTML, inline SVG charts, no network) |
| `trend_keys.py` | `key_from_env`, `KeyedFetch` (adds the key at fetch time, redacts it from errors), `MissingKey` |
| `apple_collector.py`, `steam_collector.py`, `youtube_collector.py` | Outside collectors (builder B, J004-T06) |
| `manual_import.py`, `manual/manual-entries.template.csv` | Manual-entry import: columns, checks, notes file |
| `outside_page.py` | Outside page sections; `prune_pages` (pages/ folder age, storage-limit markers) |

## Store contract (for every collector)

- Layout: `<data_dir>/observations/<source>.jsonl`, append-only, one record per line. `<source>` is the registry row id.
- Write only through `trend_store.make_record(...)` then `trend_store.append(records)`. An unreadable line (a torn write) is skipped with a warning by `read`, dropped by `prune`, and never breaks `append` (it always starts on a new line). Read with `trend_store.read(source=, entity_id=, metric=, start=, end=)` (sorted by time; start inclusive, end exclusive).
- One record per metric value (long format). A value you did not observe is **no record**: never write zero, never interpolate. `observed_or_imputed="imputed"` exists for a future, labelled use; collectors never write it.
- Before any network call: `row = trend_registry.require_allowed(rows, "<source id>")`; put `trend_registry.permission_version(row)` on every record. Network code takes an injectable `fetch`; use `PoliteClient`.
- A change to the record shape bumps `SCHEMA_VERSION` in `trend_store.py`.

## Record shape (schema_version 1)

| Field | Type | Rule |
| --- | --- | --- |
| source | str | Registry row id, e.g. `roblox.games` |
| entity_type | str | e.g. `roblox_universe`, `steam_app`, `youtube_video` |
| entity_id | str | Stable key. Roblox: universe id. Never a name |
| metric | str | Roblox: `playing`, `visits`, `favorites`, `upvotes`, `downvotes` |
| value | number | Finite; NaN, inf, bool, null are rejected |
| unit | str | e.g. `players`, `visits`, `votes`, `views` |
| observed_at_utc | ISO str, `Z` | Collector clock when the response arrived |
| source_sample_at_utc | ISO str or null | Source clock, only if the source states one |
| provenance | enum | `official`, `third_party_sampled`, `third_party_estimate`, `developer_statement`, `derived`, `manual_entry` |
| observed_or_imputed | enum | `observed` (default) or `imputed` |
| event_flag | bool | Inside a known event window (watchlist `event_windows`) **at collection time**. Pages do not use it: they take the windows from the current watchlist, so a window added later reaches old samples |
| outage_flag | bool | Source reported an outage around this value (set by importers or manual entry) |
| schema_version | int | 1 |
| permission_version | str | `<id>:<ruling>:<checked_on>` of the registry row at collection time |
| collector_version | str | e.g. `roblox_collector/0.1.0` |
| labels | dict | Mutable labels; never keys. Roblox: `name` = the API name (R1 records only), `watchlist_label` = the studio's own label, `root_place_id`, `created`, `updated` |

## Registry fields (`sources.json`, all required)

| Field | Meaning |
| --- | --- |
| id | Unique source id; also the store file name |
| name | Human name |
| route | Method and URL template (or page URL) |
| purpose | Approved purpose |
| auth | `none` or the env var names that hold credentials (never the value) |
| quota | Known quota or `UNKNOWN` with the reason |
| storage_limit_days | Integer, or null for no limit; `prune` enforces it |
| valid_until | Optional `YYYY-MM-DD` (UTC, inclusive): after it `require_allowed` refuses even an `allowed` row (Roblox rows end 2026-10-31, J004-T03) |
| terms_url | Terms page checked |
| ruling | `allowed` (automatic runs), `manual` (owner enters data by hand), `not_allowed`, `unclear` |
| checked_on | Date of the last terms check |
| notes | Evidence, caveats, job id of the ruling |

Only the lead changes `ruling`. The `roblox.place-universe` row stays as the record of its `not_allowed` ruling; no command uses it (resolve a place to a universe by hand). Roblox rows (J004-T03): `roblox.games` and `roblox.votes` are `allowed` with `valid_until` 2026-10-31 (new Roblox Terms from 2026-11-01, owner digest); `roblox.place-universe` is `not_allowed`.

## Metric rules (knowledge/reference/trends/01-roblox-data-loops.md §8)

- Weeks are 7 complete UTC days ending at 00:00 UTC on or before `--as-of`; compared weeks never overlap.
- Player-hours: trapezoids between adjacent samples at most `max_gap_minutes` apart; longer gaps add nothing. Every window reports coverage and its longest gap.
- g7 with zero or missing baseline: `new / insufficient baseline`. A game with fewer than `emerging_lead_days` (14) complete days of our history: `emerging lead (n days)`, no g7 or acceleration. A g7 from a week under the coverage gate is marked `low coverage`; added CCU is always next to g7; rows sort by g7 only when it passes the gate. No samples this week: `no recent data`.
- 24 h mean CCU and the 24 h / 7 d ratio (labelled `momentum, not week-over-week`) carry the 24 h coverage; momentum is held (`insufficient coverage`) when either window fails the gate.
- Off-event trough = lowest daily mean CCU of the week, event hours removed; a day counts only when it passes the coverage gate. Fade compares weekly means and troughs of the off-event series (coverage gated on the full series).
- Approval = up / (up + down) of the votes **added** in the week (`approval of votes added (7d)`); lifetime approval is not shown.
- Breakout and fade are suppressed when a compared window fails the coverage gate. Matched days: a complete UTC day whose mean beats the same weekday one week earlier, counted back from the newest day.
- Playtime = 60 x player-hours / added visits between the first and last visits sample of the week; always labelled an estimate. No revenue is computed.

## Names on the page

| Output | Name it uses |
| --- | --- |
| Roblox records | label `name` = API name (games details); label `watchlist_label` = watchlist `label` |
| Weekly page, Roblox table, charts, flags | the API name; the watchlist label only as a note (`; watchlist label: ...`) when it differs; `API name not collected` before the first games sample |
| Steam rows | the watchlist `label` (the API returns no name) |
| Apple, YouTube rows | the name or title in the feed |

## Outside sources (J004-T06, builder B)

Rulings: `knowledge/reference/trends/fact-check-outside.md` §3. Only `apple.rss` and `youtube.data` are `allowed`; `steam.current_players` is `unclear` until the owner decides (Steam licence names end-user display). Manual rows (`ruling: manual`) take data only through `import-manual`. Not built: Twitch Helix, Google Trends RSS and alpha API, Instagram Graph API, Apple top-grossing, Google Play, Sensor Tower, Reddit, Discord, TikTok APIs.

| Source | Records (entity_type / metric / unit) | Rules |
| --- | --- | --- |
| apple.rss | `apple_app` / `rank` / `rank`; labels `country`, `feed`, `name` | Rank movement is positions, never download growth. No game filter in the feed; `genres` only when the feed lists them. `apple_max_retries` 0: a 504 waits for the next run. Each feed logs items listed, stored and skipped (id not numeric) |
| steam.current_players | `steam_app` / `current_players` / `players`; label `fresh_until_utc` | Key only from env, added at fetch time, redacted from errors, never on disk |
| youtube.data | `youtube_video` / `views`, `likes`, `comments`; labels `channel_id`, `published_at`, `title`, `panel` | Per-video arithmetic only. Every value, and every page that shows one, is deleted 30 days after fetch by `prune`. Search-call times (no API data) are in `<data_dir>/state/youtube_search_calls.json` |
| manual rows | as entered; provenance = column `kind` (`official`, `third_party_sampled`, `third_party_estimate`, `developer_statement`; blank = `manual_entry`) | A row without a value goes to `<data_dir>/manual/notes.jsonl`. A money metric (metric or unit names revenue, earnings or robux) needs `kind` `third_party_estimate` or `developer_statement`. A row with more or fewer fields than the header is rejected (quote a field that holds a comma). An identical row (source, entity_id, metric, read_date, value, page) is skipped. No usernames or message copies from reddit or discord: `/user/`, `/u/`, `u/name` and `@name` are rejected in any field |

Watchlist key `outside` (see `watchlist.example.json`): `apple` (countries, feeds, limit), `steam.apps`, `youtube` (channels, videos, queries, uploads_per_channel).

**Latest snapshot.** Each section uses records at or before `--as-of`. When the week holds no snapshot, it shows the latest one, labelled `latest snapshot (outside the week window, <UTC>)`, with no movement or velocity: growth numbers use complete weeks only.

**30-day rule for pages.** (1) Every file under `<data_dir>/pages/` is deleted 30 days after its last change, whatever it holds (tool pages and the scout's copies alike). (2) A page that shows YouTube values carries `<!-- storage-limit source=youtube.data oldest=<UTC> -->`; every `.md` or `.html` under the data dir whose marker is older than the source's `storage_limit_days` is deleted, wherever it is. The scout's lasting record is `<data_dir>/scout-log.md` (not in `pages/`): never paste a page section with its marker into it. A page written with `--out` outside the data dir is not reached by `prune`; the command prints a warning. Every command prunes first; keep a daily `prune` as a second line while YouTube data is collected.
