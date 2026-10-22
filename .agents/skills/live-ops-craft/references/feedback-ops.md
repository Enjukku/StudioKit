> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-craft`. What and why: `live-ops-design/references/evidence-feedback.md`. Tool: `tools/liveops/feedback_count.py` (J014-T06, 19 offline tests). Collection setup: `knowledge/jobs/J014-live-ops-designer/feedback-plan.md` (owner gate G1b) and, per game once approved, `knowledge/design/feedback-setup.md`. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§3 step 4 event-review themes, §4 known false readings).

# Feedback operations: from raw exports to a counted sort

## 1. The folder (one place)
`FEEDBACK_DATA_DIR` (default `<repo>/.tools/feedback-data/`, gitignored). Player text and ids never enter git.

| Sub-folder | Holds | Written by |
| --- | --- | --- |
| `inbox/` | raw dated exports: Roblox Feedback `.csv`, in-game pulls, Discord pulls, pasted comments | the owner (by hand) or the approved import scripts |
| `items/` | one JSON line per feedback item, ids replaced by pseudonyms | import scripts, then the agent's theme tags |
| `sorts/` | the agent's sorts and count outputs | the agent |

Until the import scripts exist (feedback plan stage 2), the agent turns inbox files into `items/` lines by hand, taking each `item_id` from the export's own message or row id so that overlapping exports cannot add the same message twice.

**Source and author rules (from the J014 G2 test):**
| Case | Rule |
| --- | --- |
| Roblox built-in rating prompt export (Creator Hub Feedback `.csv`) | source `reviews`. Other public comments (social posts, video comments) are `comments` |
| A row with no author id (the Roblox `.csv` has none) | key `anon-<file>-<row>`; report the source as "at most N authors (rows, no author id; one rating per player per day)"; the denominator is the row count; say whether rating-only rows are in the denominator |
| The studio's own posts (staff, moderators, bots) | excluded; count them in the sampling table's "excluded" column |
| Discord author | one pseudonym per Discord user id when the export has ids (stage 2: salted hash); otherwise one per display name across all channels of that export, with the limit "a renamed user may count twice". The name-to-pseudonym map lives only in `FEEDBACK_DATA_DIR/keys/` (local, gitignored) and is never copied into items, sorts or any output |
| Several places in one service (Discord forum + general chat) | one source, one author scheme; note each place in the sampling table |
| Split windows | when a build or event changes mid-window, also count before and after the change (two `count` runs); report both |

## 2. Item format (the tool validates it)
Required: `item_id` (unique) · `source` (`in-game` | `discord` | `comments` | `reviews` | `support` | `survey` | `other`) · `author_key` (opaque pseudonym) · `occurred_at_utc` (ISO, `Z`) · `themes` (list of theme ids; empty = untagged). Optional: `severity` (`low` | `medium` | `high` | `critical`), `cohort` (observed only), `build`, `urgent` (bool), `excerpt` (≤ 280 characters, no personal data). Example: `tools/liveops/items.example.jsonl`.

## 3. Weekly sort, step by step
1. **Window.** Fix start (in) and end (out), UTC, and the build versions live in it.
2. **Sampling table** (template §A): for each source, who could answer and how (prompt rules, exposure counts from the analyst's events, channel membership).
3. **Urgent first.** Safety, exploit, purchase and data-loss items, and any post that exposes personal data → `urgent: true`, routed to the lead the same day (process.md §5). They still count in their themes. Personal data is never copied into an excerpt.
4. **Codebook.** Reuse the game's codebook (`sorts/codebook.md`, versioned); add a theme only with a definition and two examples. Theme ids: `area.problem` (for example `event.entrance-hard-to-find`), problem words, never solution words. After an event, keep the themes that test its promise apart: `event.promise-mismatch` (players expected what the look, sound or announcement promised, and the activity did not give it), `event.rare-feels-same` (a rare reward felt like a common one), `variant.not-recognised` (players did not know which pet or item the variant was). A request ("add PvP") is tagged with the problem it points to ("veterans run out of goals") and kept as data.
5. **Tag.** Read each item; tag the problem, not the request; several tags allowed. Leave unclear items untagged and list them for review rather than forcing a theme.
6. **Validate:** `python tools/liveops/feedback_count.py validate <items.jsonl>`. Fix every rejected line (the tool names it); exit 1 means something was rejected.
7. **Count:** `python tools/liveops/feedback_count.py count <items files> --start <ISO> --end <ISO> --out <sorts/counts-<date>.md>` (add `--json` for machines). Silent rules: start in, end out; a date-only `--start` is 00:00Z of that day and a date-only `--end` includes its whole day; the loud flags need at least 5 messages from one author and half of the theme's messages ("one loud author"), or the top 3 authors with at least 5 each holding half ("a few loud authors", §4). Use `--same-key-scheme a,b` only when two sources truly share one id scheme; otherwise overlap stays "unknown" and no all-source total is printed.
8. **Fill the sort** (`templates/live-ops/feedback-sort.md`): copy counts from the tool output, never retype them from memory; add excerpts, cohort and severity, the analyst's behaviour check (or "unknown"), contradicting sub-themes, candidate response.
9. **Loud vs silent** (template §D): for each theme with a loud-author flag or a single source, ask the analyst whether silent cohorts show the same friction.
10. **Quality checks** Q1-Q7; then hand the sort to the plan (process.md step 1).

## 4. Reading the count output
| Column | Means | Never say |
| --- | --- | --- |
| distinct authors / sampled authors | players in this source who raised the theme ÷ players in this source who wrote anything in the window | "% of players", "% of the community" |
| messages | intensity | "players" |
| flag "one loud author" | most of the messages come from one author (PROPOSAL threshold) | "many players" |
| flag "a few loud authors" | the top 3 authors, each with at least 5 messages, hold half the theme's messages (PROPOSAL threshold) | "many players" |
| no data in window | the source had nothing in the window | 0 % |
| overlap unknown | the same person may be in two sources | an added-up total |

**The count is a screening aid; known false readings (each gives a wrong number with no error).** Checked on synthetic event samples (2026-10-22): the tool's arithmetic was exact; the errors below come from the items, not the tool. Before a count drives a decision, read the raw items of that theme and check these by eye:
| Case | What the tool does | What I do |
| --- | --- | --- |
| a time written in local time but ending in `Z` | moves the item across the window or split boundary silently | convert every export to UTC before writing `occurred_at_utc`; re-check items near a boundary |
| an item at exactly `--end` | excluded (end is exclusive, by design) | keep the end at the window boundary: an item at exactly the end belongs to the next window. Never move the end past the window: items files hold every week, so a later end silently counts the next window's items too |
| one theme spelled two ways (`event.pvp-wanted`, `event.pvp_wanted`) | two rows with split counts | tag only from the codebook; scan section C for near-duplicate ids |
| rows with no author id (`anon-<file>-<row>`) | each row counts as one author | report "at most N authors" (§1) |
| a renamed Discord user without an id in the export | counted twice | state the limit in the sampling table (§1) |
| one author with 4 or fewer messages on a theme | no loud-author flag (the flag needs at least 5 messages and at least half) | read the message column next to the author column; a theme carried by one or two authors is said so in words |
| several loud authors, none with half the messages (60 messages, 52 from 4 authors) | flagged "a few loud authors" when 3 of them hold half; spread over more authors, no flag | compare messages with distinct authors; above about 3 messages per author (a starting value), read the per-author spread by eye and say it in words ("most messages come from 4 of 12 authors") |
| the same message in two overlapping exports, turned into items by hand | counted twice in messages (and in the loud flag), no error: hand-minted `item_id`s differ, so the duplicate check passes | take each `item_id` from the export's own message id, or de-duplicate overlapping exports before tagging |
| untagged items | counted in sampled authors (the denominator), not in any theme | list unclear items for review (§3 step 5) instead of leaving real themes untagged |
