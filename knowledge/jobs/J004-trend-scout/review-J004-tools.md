---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J004-T07
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-21

# J004-T07 code review: tools/trends (T05, T06, lead edits)

Depth: deep (terms, secrets, stored data). Scope read: `tools/trends/*.py`, `sources.json`, `config.json`, `manual/`, `tools/tests/test_trends_*.py`. Ground truth: `.agents/skills/trend-scan/references/formulas.md` (**F**), `knowledge/reference/trends/01-roblox-data-loops.md` §8 (**N1**), `.agents/skills/trend-scan/references/sources.md` (**S**), `sources.json`. Also read for context only: `trend-scan/SKILL.md` §3, `templates/trends/weekly-report.md`, `knowledge/jobs/J004-trend-scout/schedule-plan.md`.
Method: code read of every path; `python -m unittest discover -s tools/tests -p "test_trends_*.py"` → 45 tests OK; 8 throw-away scripts in the scratchpad with injected `fetch`/clock and temp data dirs (no network), deleted after. Every finding below was reproduced unless marked "code read".

## 1. What was checked (C2)

| Item | Result | How |
| --- | --- | --- |
| Refusal before any request, every collector | **OK** | Code read: `require_allowed` is the first call in `roblox_collector.collect` :101-102, `resolve_place` :122, `apple_collector.collect` :75, `steam_collector.collect` :74 (before the key is read), `youtube_collector.collect` :84. Only network path is `trend_http.urllib_fetch` (grep). Tests `test_unclear_ruling_refuses_without_any_request`, `test_each_collector_refuses_without_request_when_not_allowed`, `test_steam_unclear_cli_exits_refused_with_key_set` |
| `valid_until` | **OK** | Script: CLI `collect-roblox` with clock 2026-11-01 00:00:01 → exit 2, 0 requests; 2026-10-31 23:59 → 2 requests. `trend_registry.py:57` inclusive UTC |
| Key redaction | **OK** | Code read `trend_keys.py` (key added inside `KeyedFetch`, errors re-raised redacted `from None`; `PoliteClient` and logs see only the key-less URL); test `test_key_never_in_records_logs_or_errors`; fixtures grep: no key |
| YouTube 30-day prune incl. pages | **Gaps** | Works in the happy path (test `test_prune_removes_youtube_records_and_pages_after_30_days`, marker boundary checked). Fails when prune is not run, is aborted, or the page has no marker: findings 2, 3, 4 |
| g7 non-overlap | **OK** | `trend_metrics.weeks` :68-71: `[end-7d, end)` and `[end-14d, end-7d)`; boundary segments are clipped, not shared |
| Gap handling | **OK** | `integrate` :39 skips segments > `max_gap`; `_svg` :226 breaks lines at the same rule; test `test_gap_not_bridged` |
| Coverage | **OK math, gaps in display** | `integrate` coverage and longest gap correct (script + test). 24 h window coverage is never printed: finding 8 |
| Momentum label | **OK label, number unguarded** | Label printed in every cell (`trend_page.py:107`); coverage missing: finding 8 |
| Zero baseline | **OK, one mislabel** | `g7` :80 returns "new / insufficient baseline" for 0 or None, never ∞. Same label is shown for a game with history but no recent samples: finding 7 |
| Manual import validation | **Gaps** | Ruling must be `manual`, finite value, unit, region, future date: OK. Findings 6, 11, 13, 14 |

## 2. Findings (most harmful first)

Severity: **High** = a terms/storage breach or a wrong number a reader will act on, likely in the first scans; **Medium** = real but needs a less common input or a later step.

### Terms, permission, secret, storage

**1. High · `trend_http.py:93-94` + `roblox_collector.py:111-113` (also `apple_collector.py:84`) · Retry-After is not honoured across requests.**
A 429 whose Retry-After exceeds `max_retry_after_s` (or a 429 that survives all retries) raises `FetchFailed`; the collector logs "skip" and sends the next request to the same host 2 s later.
Scenario (script): 30 games, server answers `429, Retry-After: 900` → 6 requests in 10 s (games + votes for 3 batches), sleeps `[2.0 ×5]`. The Roblox ruling's condition is "honour 429 and retry-after" (`sources.json` roblox.games notes).
Fix: on a 429 that stops, stop the run for that host (re-raise out of the batch loop), or keep `blocked_until` in `PoliteClient` and refuse further `get()` calls before it.

**2. High · `trends.py:148-151`, `trend_registry.prune_all` · The 30-day YouTube limit is enforced only when someone runs `prune`.**
No other command prunes. The weekly steps run `prune` once a week (`trend-scan/SKILL.md` §3 step 4); the schedule plan's option B (on demand) has no daily prune, and option A stops while the PC sleeps (`schedule-plan.md` §2-§3).
Scenario: record fetched Mon 09:00; weekly prune on Mon 09:00 four weeks later sees it at 28 d; the next prune is 35 d after fetch → 5 days over the limit (YouTube Developer Policies, `sources.json` youtube.data notes). If the YouTube panel is emptied and prunes stop, the data stays forever.
Fix: run `prune_all` + `prune_pages` at the start of every `trends.py` command (cheap, idempotent); keep the daily task as a second line.

**3. High · `trend_store.py:151-160` (prune), `:128-131` (read), `:112-114` (append); `trends.py:149-151` · One unreadable line or a locked file aborts all pruning, and `prune_pages` is never reached.**
`prune` and `read` call `json.loads` on every line with no recovery; `prune_all` runs before `prune_pages` with no `try`.
Scenario A (script): `youtube.data.jsonl` ends in a torn line (process killed mid-write, disk full, or a reader catching a buffered write half-done; under the 15-min schedule, `collect-roblox` writes ~60 KB per run in 8 KB flushes) → `prune` raises `JSONDecodeError`; the 2026-08-01 record and its page both survive. The same line makes `page` crash (`read`), and the next `append` concatenates a valid record onto the torn line, so that record is lost too.
Scenario B (script, Windows): `prune` while a `collect-youtube` run holds the file open → `os.replace` raises `PermissionError [WinError 5]`; nothing pruned, `.jsonl.tmp` left behind. On POSIX the same overlap silently drops the records appended between the read and the replace.
Fix: in `prune`, count and quarantine unreadable lines (a source with a limit deletes them), retry/skip a locked file and report it; always run `prune_pages` (`finally`); `append` writes one joined string and first adds a newline if the file does not end with one; `read` reports and skips bad lines.

**4. High · `outside_page.py:218-228` + `templates/trends/weekly-report.md` · The scout's own weekly page carries no storage marker, so `prune` never deletes it.**
`prune_pages` deletes only files that contain `<!-- storage-limit ... -->`. The skill (§3 step 6) has the scout fill a copy of the template as `<data_dir>/pages/trend-week-<date>-scout.md` including "outside trends"; the template has no marker (grep).
Scenario: the scout copies three YouTube view velocities from the tool page into the scout page → page kept indefinitely.
Fix (part outside this review's scope): the template starts with a marker line the scout fills; or `prune_pages` also deletes any `trend-week-<date>*` file whose sibling tool page carried a marker. Lead decides which.

**5. Medium · `roblox_collector.py:106`, `config.json` `collector.batch_size` · The "at most 50 ids per call" condition is not enforced in code.**
Scenario (code read): `batch_size` set to 100 in config ("change values here, never in code") → 100 ids per games call, outside the ruling's conditions.
Fix: reject or clamp `batch_size > 50` in `collect`.

**6. Medium · `manual_import.py:45, :81` · The no-usernames rule for reddit and discord misses profile links and unchecked columns.**
Scenario (script): reddit row with `page=https://www.reddit.com/user/SomeRealPerson/comments/abc` is accepted and stored (`/user/` is not matched by `u/\w`). `window`, `metric` and `entity_type` are not checked at all. Breaks S §2 "no usernames".
Fix: match `/user/` and `/u/` too, and check every free-text column for these two sources.

### Wrong numbers shown as right

**7. High · `trend_page.py:57, :68, :98-100`; `trend_metrics.py:78-82, :109-119` · g7, acceleration and weekly means are shown, and rows ranked, from weeks that fail the coverage gate; young games never get "emerging lead (n days)".**
F §2 and N1 RP:97: a game with < 14 days of history shows "emerging lead (n days)", daily numbers only; F: added CCU is always shown next to g7.
Scenario (script): game first sampled 8 days before the week end (1 day in the previous week, at 200; this week 1,000) → table shows `g7 +393.2%`, no added CCU, previous coverage 14 %; the row sorts to the top of "Rising games"; Breakout reads "suppressed: coverage". A game with long history but no samples in the last 24 h or none in a week shows "new / insufficient baseline" (wrong: it is not new).
Fix: compute history days; under 14 → "emerging lead (n days)" and hide g7/acceleration; show g7 only with both weeks gated (else a "low coverage" status), always with added CCU; sort by gated g7; use a "no recent data" status when the current window is empty.

**8. High · `trend_page.py:56, :96, :106`; `trend_metrics.py:85-91` · 24 h mean and momentum are printed without their coverage.**
F §1: "print coverage next to every windowed number". `momentum` returns `coverage_24h` but the page drops it.
Scenario (script): steady 1,000 CCU all week; the last 24 h hold one hour of samples at a 3,000 peak → "24h mean CCU 3,000", "Momentum 2.96" with 4 % coverage, nothing on the page says so.
Fix: print coverage next to both, or hold them under the gate as breakout is held.

**9. High · `trend_page.py:47-48, :62, :103`; `trend_metrics.py:178-179` · "Approval" is the all-time cumulative ratio, printed under "Votes added (7d) / approval".**
F §2: cumulative votes are dominated by old players; use votes added in the window. The column header makes the reader take it as this week's approval.
Scenario (script): totals 910 up / 190 down; this week +10 up / +90 down → cell `100 / 82.7%`; this week's approval is 10 %.
Fix: approval = up_added / (up_added + down_added), header "approval of votes added (7d)"; if a lifetime ratio is kept, label it "lifetime".

**10. Medium · `trend_metrics.py:59, :134, :141`; `trend_page.py:59` · "Trough" is the single lowest sample, and fade's weekly changes use the event-inclusive series.**
F §2: trough = lowest daily (or matched-hour) mean; N1 RP:99: fade means a defined baseline fell, keep event peaks and event-free series apart.
Scenario (script): daily means 400 → 300 → 200 over three weeks, one sample of 0 in the middle week (API glitch; the collector never sets `outage_flag`) → `no fade`, reason "trough 200.0 vs 0.0"; with daily-mean troughs it is a fade. The "Off-event trough" column shows that glitch or the nightly low as the week's trough. Second path (code read): an event in the oldest compared week makes the next change negative, so its end counts as one of the two falling weeks.
Fix: trough = min of complete-day means (gated) on the off-event series; compute fade's g7 changes on the off-event series.

**11. Medium · `trend_store.py:164-168` + `roblox_collector.py:75` (`_in_event` at collection time) · Event windows added after the fact never reach stored records.**
`event_flag` is frozen when the sample is written; `game_rows` and `fade` read it, not the watchlist. The skill (§3 step 7) has the scout add event windows when it learns of them, usually after.
Scenario (code read): event 10-15 to 10-17 added to the watchlist on 10-20 → those samples keep `event_flag=false`; off-event trough and fade include the event.
Fix: compute event membership at read time from the watchlist windows (keep the stored flag as "known at collection").

**12. Medium · `manual_import.py:85`; `outside_page.py:136` · Tracker estimates and money figures enter as plain manual values with no estimate label.**
F §5: other games' revenue is always a third-party estimate (3P-E, vendor, range, method). Import forces `provenance=manual_entry`; nothing requires the label.
Scenario (script): `roblox.trackers,...,revenue_robux_per_day,50000,robux,` (blank note) → accepted; page row "50,000 robux" under [MAN] with no 3P-E, vendor or range.
Fix: a required label column (OFF / 3P-S / 3P-E) for tracker rows, mapped to `provenance`; reject money-like metrics without 3P-E.

**13. Medium · `trend_page.py:39-43, :54-55` · A page for a past week takes "Current CCU" and labels from samples after `--as-of`.**
Scenario (script): page `--as-of 2026-10-22T06:00Z`, a sample exists on 10-25 → "Current CCU 5,000 (2026-10-25T06:00:00Z)" on the week ending 10-21 page.
Fix: filter `recs` to `observed_at < as_of` (or `< end`) before building the row.

### Data loss or corruption

**14. Medium · `manual_import.py:111` · Extra CSV fields are dropped silently and the row is accepted.**
`DictReader` puts surplus fields under key `None`; the comprehension drops them.
Scenario (script): `...,rank,1,rank,free-to-play, but top seller only in EU` → stored note "free-to-play"; the rest is lost with no rejection.
Fix: reject a row with a `None` key or `None` values ("unquoted comma: wrap the field in quotes").

**15. Medium · `manual_import.py:101-127` · Re-importing a file duplicates every row.**
Documented in S §2, but the tool exits 1 on any rejected row, which invites re-running the whole file.
Scenario (script): import 3 rows, import again → 6 records; the page lists each manual entry twice.
Fix: skip rows whose (source, entity_id, metric, observed_at_utc, value) already exist, and report them as "already imported".

### Crash on real input

**16. Medium · `trend_http.py:78`; `roblox_collector.py:111-117`; `trends.py:100-107` · A dropped connection mid-body crashes the whole Roblox or Apple run and loses the batches already fetched.**
`PoliteClient` treats only `OSError` as a network error; `http.client.IncompleteRead` (an `HTTPException`, not `OSError`) escapes; records are appended only after the loop.
Scenario (script): 2 batches; the 3rd request raises `IncompleteRead` → `collect` raises, the 50 records of batch 1 are never stored, CLI prints a traceback. (Steam and YouTube are safe: `KeyedFetch` converts every error to `OSError`.)
Fix: catch `http.client.HTTPException` with `OSError` in `PoliteClient.get`; optionally append per batch.

### Structure

No finding with a failure scenario beyond the ownership issue in finding 11.

### Over-building

**17. Medium · `roblox_collector.py:31, :88-94, :121-125`; `trends.py:68-69, :96-99`; test `test_place_to_universe_parse` · A command, parser and URL exist for a route ruled `not_allowed` under both Terms versions.**
`resolve-place` can only print REFUSED; its parser and test are maintained for no caller (`rules/anti-overengineering.md` 5, "a stub that ... does nothing").
Fix: remove the command, `resolve_place`, `parse_place_universe`, `PLACE_URL` and the parse test; keep the registry row (it documents the ruling). Keep only if the lead expects a re-ruling soon.

## 3. Tests (lane and quality)

Lane right (pure offline unit tests, injected fetch/clock, recorded and synthetic fixtures; the gate runs them, `tools/verify.py:143`). They can fail (spot-checked: the refusal and redaction tests assert on spy calls and stored text). Missing cases, one per finding: Retry-After across requests (1), prune with a bad line / locked file (3), young game and low-coverage g7 display (7), 24 h coverage (8), approval of added votes (9), daily-mean trough (10), extra CSV fields and re-import (14, 15), non-`OSError` transport error (16). `test_trends_page.test_renders_with_data` asserts only the happy path.

## 4. Questions (no finding without more evidence)

| # | Question | Why it matters | Default if unanswered |
| --- | --- | --- | --- |
| Q1 | How will Roblox samples be scheduled for the first scan (schedule-plan option A not set up yet)? | On demand, samples are hours or days apart → coverage near 0 → every flag held and g7 drawn from scraps (finding 7 makes it visible) | Treat findings 7-8 as blockers for the first page |
| Q2 | Can Roblox return 200 with `"data": null` or non-dict items? | `parse_games` would raise `TypeError` (`roblox_collector.py:57`), caught by nothing (only `ValueError` at :116) | No evidence: not reported |
| Q3 | `prune_pages` deletes a whole `.md` that contains a marker anywhere, e.g. `scout-log.md` if a page section with its marker is pasted into it | Loss of the scout's lasting record | Tell the scout never to paste page sections into the log |
| Q4 | Rolimon's rows (no consent yet) cannot be told apart from other trackers at import (`roblox.trackers` is one row) | Rolimon's licence: personal, non-commercial | Split the registry row per tracker |
| Q5 | `require_allowed` is checked once per run; a run that starts 2026-10-31 23:59:50 sends requests after the cut-off | ~20 s window | Accept |
| Q6 | Ten fetched evidence files in `tools/tests/fixtures/trends/` are referenced by no test (cited by the fact-check notes instead) | Not over-building if they are evidence; they live under tests | Leave; lead may move them to `knowledge/reference/trends/` |

## 5. Not checked

Live endpoints (no network by brief); real response shapes beyond the recorded fixtures; performance of `page` on months of 15-min samples (every `integrate` walks the full series, ~30 calls per game: not measured); Linux/macOS behaviour of finding 3B (reasoned, not run). Labels: all results gate-verified (unit tests) or reproduced by scratch script; nothing MCP- or owner-confirmed.

## Fixes (J004-T12)

> Author: tool fixer · claude-opus-5-5 · high · 2026-10-21

Every test below failed on the code as reviewed (run against a copy taken before the first edit) and passes now. Lines are in `tools/trends/`, tests in `tools/tests/`.

| Finding | Fix (file:line) | Test |
| --- | --- | --- |
| 1 429 not honoured across requests | `trend_http.py:79, :103, :107` (client stops after a 429 that says stop); `roblox_collector.py:109`, `apple_collector.py:90` end the run | `test_trends_roblox.test_429_stop_ends_the_run_for_the_source` |
| 2 30-day limit only when `prune` runs | `trends.py:62` `_prune`, called at `:109` before every command except `registry` | `test_trends_outside_page.test_every_data_command_prunes_first` |
| 3 torn line / locked file stop prune | `trend_store.py:107` `read_jsonl` (skip + warn), `:124` `append_jsonl` (new line first), `:171` `prune` (drops unreadable lines, no `.tmp` left); `trend_registry.py:63` `prune_all` continues and reports; `outside_page.py:256` `prune_pages` always runs | `test_trends_store.test_torn_line_is_skipped_by_read_and_dropped_by_prune`, `test_append_after_torn_line_starts_a_new_line`, `test_prune_continues_past_a_locked_file` |
| 4 scout page has no marker | `outside_page.py:37, :256`: every file under `pages/` deleted 30 days after last change; markers still apply anywhere; README 30-day rule | `test_trends_outside_page.test_pages_folder_files_expire_30_days_after_last_change` |
| 5 batch size not capped | `roblox_collector.py:34, :101` (`MAX_IDS` 50) | `test_trends_roblox.test_batch_never_exceeds_50_ids` |
| 6 reddit/discord user paths | `manual_import.py:52, :92` (`/user/`, `/u/`, `u/`, `@`, every field) | `test_trends_manual.test_reddit_discord_user_paths_rejected_in_any_field` |
| 7 g7 for young games, ranking | `trend_page.py:31` `_g7_shown`, `:68-72` history days, `:95` sort by gated g7; `config.json` `emerging_lead_days` | `test_trends_page.test_young_game_is_an_emerging_lead_not_ranked_by_g7` |
| 8 24 h coverage missing | `trend_metrics.py:86` `momentum` held under the gate; `trend_page.py:150` and 24 h mean cell print coverage | `test_trends_metrics.test_momentum_held_under_coverage_gate`, `test_trends_page.test_24h_coverage_printed_and_momentum_held` |
| 9 lifetime approval as weekly | `trend_page.py:89`; header "approval of votes added (7d)" | `test_trends_page.test_approval_uses_votes_added_in_the_week` |
| 10 trough = one sample; fade on event series | `trend_metrics.py:138` `daily_trough`, `:163` fade changes on the off-event series | `test_trends_metrics.test_trough_is_lowest_daily_mean_not_one_sample`, `test_fade_changes_use_the_off_event_series` |
| 11 event flag frozen at collection | `trend_page.py:60` off-event series from watchlist windows at read time; `trend_store.series` no longer filters on `event_flag` | `test_trends_page.test_event_windows_added_later_reach_old_records` |
| 12 money figures without 3P-E | `manual_import.py:44, :94-97` column `kind` → provenance; money metrics need `third_party_estimate` or `developer_statement`; page column "Kind" | `test_trends_manual.test_money_metric_needs_estimate_kind` |
| 13 page uses samples after as-of | `trend_page.py:53`, `outside_page.py:196-198` | `test_trends_page.test_samples_after_as_of_are_not_used` |
| 14 extra CSV fields dropped | `manual_import.py:130` (rejected with line number and field count) | `test_trends_manual.test_row_with_wrong_field_count_rejected_with_line` |
| 15 re-import duplicates | `manual_import.py:64, :149` (skipped and counted; CLI prints the count) | `test_trends_manual.test_reimport_skips_identical_rows` |
| 16 IncompleteRead crashes the run | `trend_http.py:86` (`http.client.HTTPException` is a network error) | `test_trends_roblox.test_dropped_connection_fails_only_that_request` |
| 17 dead `resolve-place` | command, `resolve_place`, `parse_place_universe`, `PLACE_URL` and the parse test removed; registry row kept | `test_trends_roblox.test_resolve_place_command_removed` |
| F18 (scan T3) no data shown after the week | `outside_page.py:52` latest snapshot label in Apple, Steam, YouTube, manual; Roblox current CCU labelled (`trend_page.py` `_current_text`) | `test_trends_outside_page.test_latest_snapshot_shown_when_outside_the_week` |
| F19 (scan T8) silent Apple skips | `apple_collector.py:72` logs items listed, stored, skipped per country/feed | `test_trends_outside.test_skipped_items_and_feed_length_are_logged` |
| F20 (scan T10) which name | `roblox_collector.py` labels `name` (API) and `watchlist_label`; `trend_page.py:64, :137`; README "Names on the page" | `test_trends_page.test_api_name_shown_watchlist_label_only_a_note` |
| F21 (scan T12) permission status | `trend_page.py:105`, `trends.py:157` pass every source the page draws on | `test_trends_outside_page.test_permission_status_lists_every_source_used` |

End-to-end: `page --as-of 2026-10-21T06:00:00Z` on a scratch copy of the first scan's data: 222 Apple rows shown as "latest snapshot (outside the week window, 2026-10-21 04:26 UTC)", 17 games as "emerging lead (0 days)", API names first, full PERMISSION STATUS. The copy was deleted after; `.tools/trend-data/` was not touched.
