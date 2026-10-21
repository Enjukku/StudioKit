# tools/liveops: feedback count tool

> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-21. Job J014-T06. Python 3.11+ standard library only. No network, no model.

The live-ops designer reads and tags player feedback. This tool does only the arithmetic: exact distinct-author counts per theme, per source, per time window, and the warnings. Its output fills `templates/live-ops/feedback-sort.md` §A (sampling counts), §B (urgent item ids) and the §C columns "distinct authors / sampled authors" and "messages".

## Commands

| Command | Does |
| --- | --- |
| `python tools/liveops/feedback_count.py count ITEMS.jsonl [ITEMS2.jsonl ...] --start ISO --end ISO [--same-key-scheme a,b] [--json] [--out PATH]` | Counts for the window (start inclusive, end exclusive, UTC; `2026-10-01T00:00:00Z` or `2026-10-01`). Markdown to stdout, or JSON with `--json`, or to a file with `--out`. Rejected lines go to stderr and into the output; exit 1 if any line was rejected (the good lines are still counted) |
| `python tools/liveops/feedback_count.py validate ITEMS.jsonl [...]` | Check files only. Exit 1 if any line is rejected |
| `python -m unittest discover -s tools/tests -p "test_feedback_count.py" -t tools/tests` | Offline tests |

Exit 2: bad arguments (missing file, bad time, start not before end, unknown source in `--same-key-scheme`).

Data dir: env `FEEDBACK_DATA_DIR`, default `<repo>/.tools/feedback-data/` (gitignored). Player text and ids stay there, never in git (owner J014-D3). An ITEMS path that does not exist as given is looked up in the data dir.

## Item shape (one JSON object per line; example: `items.example.jsonl`, fake keys only)

| Field | Required | Rule |
| --- | --- | --- |
| item_id | yes | Non-empty string, unique across all files of one run (a repeat is rejected with its line number) |
| source | yes | `in-game`, `discord`, `comments`, `reviews`, `support`, `survey`, `other` |
| author_key | yes | Opaque non-empty string: a pseudonym or hashed id, never a username. Never printed |
| occurred_at_utc | yes | ISO 8601 time ending in `Z` |
| themes | yes | List of theme id strings; `[]` = untagged. A theme repeated in one item counts once |
| severity | no | `low`, `medium`, `high`, `critical` |
| cohort, build | no | Strings (cohort: observed, never inferred) |
| urgent | no | `true` or `false` |
| excerpt | no | String, at most 280 characters. Never printed |

Unknown fields are kept and ignored. The tool cannot check whether an author_key is a raw username; the tagger must not write one.

## Counting rules

| Value | Rule |
| --- | --- |
| Distinct authors (theme, source) | Authors with at least 1 item carrying the theme in the window. One author counts once per theme per source, whatever the number of items or tags |
| Messages (theme, source) | Items carrying the theme: intensity, not prevalence |
| Sampled authors (source) | Distinct authors with at least 1 item in the window, tagged or not |
| Share | Theme authors / sampled authors of the same source. Never across sources, never over DAU |
| No data | A source in the input with no item in the window is `no data in window`, never 0. A source not in the input is absent |
| Cross-source overlap | `unknown` unless `--same-key-scheme a,b` says those sources use one key scheme. Then per theme: `distinct across <sources>` (the combined count) and `possible cross-source overlap` (authors in 2+ of those sources). Sources outside the scheme stay `unknown` |
| Urgent | Items with `urgent: true` are listed by item_id per source and are also counted in their themes |
| Loud author flag | PROPOSAL: one author wrote at least 5 messages of a theme in a source and at least half of them. A warning only; counts do not change |

The tool never weights, extrapolates to all players or rounds a count. The share column is a percentage with one decimal; the exact fraction is beside it.
