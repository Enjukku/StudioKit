---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J014 digest item 5 (default applied, J014-D4)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J014-T06 brief: feedback count tool

<intent>
The live-ops designer sorts player feedback by theme and tells the owner how many players raise each theme. The owner asked it to "sort and count player feedback by theme, and weigh loud players against the silent majority". A language model that reads 300 messages and says "about 40 players want X" is guessing; a busy player who posts 25 times looks like 25 players; a Discord share gets reported as "% of all players". All three mislead the owner into building the wrong update. The owner's research paper sets the rule: count distinct authors per theme within one source and one time window, keep message volume as a separate intensity signal, never use a model's estimate where an exact count is possible, and report possible cross-source overlap instead of guessing it.

So the agent needs a small, exact tool: it reads feedback items that the agent has already tagged with themes, and prints the counts. The agent does the reading and tagging; the tool does the arithmetic and the warnings. It must be boring and impossible to fool: a planted double-count must fail its tests. Look through the refs and the nearby tools (`tools/trends/`) before you start; copy their conventions (standard library only, data dir from an environment variable with a gitignored default, CLI with subcommands, offline unittest tests).
</intent>

<spec>
id: J014-T06
from: lead
to: feature-builder (tool builder)
model: opus
effort: medium
skills: [engineering-craft, testing]
refs:
  - templates/live-ops/feedback-sort.md   # take: the sort's columns (§A sampling, §C themes, §D loud vs silent, §E Q1); the tool's output must fill §A counts and the §C "distinct authors / sampled authors" and "messages" columns
  - tools/trends/README.md, tools/trends/trend_store.py, tools/trends/manual_import.py   # take: data dir env var + gitignored default, JSONL store, validation with line numbers, no silent zeros; avoid: network code (this tool has none)
  - tools/tests/test_trends_store.py   # take: test style
  - C:\Users\Firew\Downloads\live-ops-designer-research.txt lines 258-276   # the taxonomy and counting rules (outside git; read only)
fixed:
  files: tools/liveops/feedback_count.py (+ tools/liveops/README.md, tools/liveops/items.example.jsonl), tools/tests/test_feedback_count.py
  runtime: Python 3.11+, standard library only
  data_dir: env FEEDBACK_DATA_DIR, default <repo>/.tools/feedback-data/ (.tools/ is already gitignored)   # player text and ids never enter git (AGENTS.md §3.4 spirit; owner J014-D3)
  input: JSONL items, one per line. Required: item_id (unique), source (in-game | discord | comments | reviews | support | survey | other), author_key (opaque string; a pseudonym or hashed id, never a username), occurred_at_utc (ISO, Z), themes (list of theme ids, may be empty = untagged). Optional: severity (low|medium|high|critical), cohort (string, observed only), build (string), urgent (bool), excerpt (string, ≤ 280 chars). Unknown fields are kept and ignored.
  counts: per theme × source × window: distinct authors, messages; per source × window: sampled authors (distinct authors with ≥ 1 item in the window, tagged or not) and items; share = theme authors / sampled authors of the same source (never across sources, never over DAU)
  window: --start / --end (start inclusive, end exclusive, UTC)
  overlap: an author_key seen in 2+ sources is reported as "possible cross-source overlap" (count per theme) — only when the sources share a key scheme declared with --same-key-scheme a,b; otherwise the output says overlap "unknown"
  combined_total: a theme's all-source author count is printed only under --same-key-scheme and labelled "distinct across <sources>"; otherwise per source only
  validation: a bad line (missing field, bad date, duplicate item_id, author_key that looks like a raw Roblox username is NOT checkable — skip that), is reported with its line number and excluded; exit 1 if any line was rejected; the good lines are still counted
  urgent: items with urgent=true are listed by item_id in their own section and also counted
  output: markdown tables (stdout or --out file) matching feedback-sort.md §A and §C count columns, plus --json for machines; output never prints author_key values
  cli: python tools/liveops/feedback_count.py count ITEMS.jsonl [ITEMS2.jsonl ...] --start --end [--same-key-scheme a,b] [--json] [--out PATH]; and `validate ITEMS.jsonl`
open: [module structure inside the file, table layout details, extra warnings that help (for example a theme with 1 author and 20 messages flagged "one loud author")]
avoid: [any network call, any model call, weighting or extrapolating to all players, printing author keys, rounding counts]
owns: [tools/liveops/, tools/tests/test_feedback_count.py]
not_in_scope: [importers from Discord, Roblox or any service; theme tagging; any change to other tools, skills or templates; creating the data dir contents beyond the example file]
rules:
  - Never write zero for a value you did not observe: a source with no items in the window is absent or "no data", not 0 %.
  - One author counts once per theme per source per window, whatever the number of items or tags.
  - Shares are only within one source.
  - No secrets, tokens or real player data anywhere, including tests and the example file (use obviously fake keys like "a-001").
  - Generated files are never edited by hand.
deliver: the files above; tests pass with `python -m unittest discover -s tools/tests -p "test_feedback_count.py" -t tools/tests`
checks:
  - C1 planted faults the tests must catch (each test fails if the counting rule is broken): one author with 25 items on one theme counts 1; one author with 2 tags counts once in each theme; the same author_key in two sources without --same-key-scheme gives overlap "unknown" and no combined total; with it, combined distinct = 1; window boundaries (start in, end out); duplicate item_id rejected with its line number and exit 1; untagged items count in sampled authors but in no theme
  - C2 output never contains any author_key (test greps the output)
  - C3 `python tools/verify.py` passes the tests step (other jobs' failures named, not fixed)
return: rules/messages.md §3 hand-back to lead — STATUS, coverage C1-C3 with evidence (test names, run output line), the open choices you took, files written
</spec>
