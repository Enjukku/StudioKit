---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013 G1 (J013-D4, J013-D6)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Brief J013-T04: analytics data tool + stats helper

```text
<intent>
The studio's new analyst agent reads each Roblox game's own player data and tells a non-expert owner what changed and how sure we are. Its rule: no number may come from writing; every number comes from a saved data pull or a deterministic calculation. This tool is both halves.

1. Pull. Read the game's aggregated metrics and its experiment results through Roblox's official Open Cloud APIs (Analytics Query API; Experiments API read endpoints) and save every pull as history, so this month can be compared with last month. Roblox keeps performance metrics only 28 days and standard metrics about 4 years, so our history is the only long record of performance. Values can be revised (points marked Projected) and some points are flagged NotStatisticallySignificant: keep the status and every revision; never overwrite.
2. Calculate. A small stats helper the analyst calls instead of doing arithmetic in prose: cohort maturity (can a D7 number be read yet?), difference between two rates with an honest interval, players needed per arm for an A/B test, sample-ratio check, difference-in-differences arithmetic.

The owner's API key lives only in the owner's environment. A leaked key is the worst failure of this tool: it must never be printed, logged, saved, put in a URL or kept in an error text. The owner runs pulls on demand (no scheduler), so the tool must say clearly when the last pull is old enough that performance history now has a gap.
</intent>
<spec>
id: J013-T04
from: lead
to: tool builder
model: opus
effort: medium
skills: [engineering-craft, testing]
refs:
  - knowledge/external/roblox-creator-docs/cloud/guides/analytics/index.md    # take: endpoints, x-api-key header, request fields, UTC buckets, inclusive start / exclusive end, granularities, 2-year rule, long-running operations (202, poll GET https://apis.roblox.com/analytics-query-api/{path}), point status values, stringValues, errors table (2001 no retry, 3000 data-point budget, 2000/2002 retry, 1000 timeout, 401, 404)
  - knowledge/external/roblox-creator-docs/cloud/guides/analytics/metrics.md  # take: exact metric names, type (standard / performance), granularities, breakdowns, retention. Use names exactly as written there
  - knowledge/external/roblox-creator-docs/cloud/guides/experiments.md        # take: the read endpoints (list, get, results / goal metrics), async operations, scope needed. Read only: never create, start, stop or complete
  - tools/trends/trend_keys.py, tools/trends/trend_store.py, tools/tests/test_trends_store.py   # take: env-only key, redaction, append-only JSONL, data dir outside git with env override, unittest style. avoid: the URL-parameter key (Open Cloud uses a header), collector politeness code
  - knowledge/reference/analyst/   # 01-roblox-platform-facts.md §4 (API facts, in progress) and 02-statistics-experiments.md §4 (formulas with worked check values, in progress) may appear while you work: read them if present and use their check values in tests; if a fact there disagrees with the mirror, follow the mirror and say so in the hand-back
  - Before you design, look through tools/trends/ and tools/tests/ for conventions (CLI shape, README style, how verify.py runs tests).
fixed:
  location: tools/analytics/ (code + README.md + a metric-set config file) and tools/tests/test_analytics_*.py   # J013 brief owns
  key_env: ROBLOX_ANALYTICS_API_KEY   # J013-D6
  key_transport: x-api-key request header only   # Open Cloud docs
  key_scope_needed: universe.analytics:read (and whatever the Experiments read endpoints need; report the exact scope names for the owner)   # docs
  data_dir: ANALYTICS_DATA_DIR if set, else <repo>/.tools/analytics-data/<universe id>/ (.tools/ is git-ignored)   # J013-D6
  stale_warning_days: 21   # J013-D6; performance retention 28 days (docs)
  pulls: on demand only; no scheduler, no background service   # J013-D6 (as J004-D8)
  apis: Analytics Query (metrics, dimension-values) + Experiments (read endpoints only); Events API out unless the lead adds it   # J013-D6
  runtime: Python 3.11+ standard library only (urllib); Windows and POSIX   # kit tools convention
  universe_id: a CLI argument or a value in a game-side config file; never hard-coded in kit files   # no game content in kit
open: [module split, CLI subcommand names and flags, record schema field names, metric-set contents (a weekly set, a performance set, a funnel discovery flow; built only from metrics.md names), polling and retry timings within the docs' advice, which interval methods (state why), output formats (JSON + a short human line), README wording]
avoid: [the key in any URL, log line, exception text, file, test fixture or snapshot; overwriting earlier pulls; treating a Projected or NotStatisticallySignificant point as final; summing daily DAU into "unique players"; a statistics formula without a test; real game data in fixtures (use the docs' example payloads or synthetic values labelled TEST); network access in tests; a third-party package]
owns: [tools/analytics/, tools/tests/test_analytics_*.py, tools/tests/fixtures/analytics/]
not_in_scope: [skills, templates, role files, scheduling, any write call to Roblox (experiments, configs, keys), the Events API, charts]
rules:
  - The key is read only from the environment variable at request time. It is never printed, logged, written to disk, put in a URL, or left in an exception or error text (redact before re-raising). A missing key stops before any request with a message naming the variable, not a value.
  - History is append-only. Each saved observation keeps: universe id, metric, granularity, breakdown and filter, bucket time (UTC), value or stringValues, point status (or none), the request body (no key), the operation path, pulled-at time (UTC), and tool version. A re-pull of the same bucket is a new observation; a reader picks the latest and can list revisions.
  - Follow the docs' limits: retry only on 500 code 2000 and 503 code 2002 (bounded, with backoff), poll 202 operations until done or a bounded timeout, never retry 400 code 2001 or 401; on 429 code 3000 (data-point budget) split the date range or report it; respect the 2-year granularity rule and the 28-day performance window (do not request what will fail).
  - A `status` command reports the last successful pull per metric set and warns when it is older than 21 days.
  - Stats helper: every formula has a docstring with its assumptions, and a test against a published value or a hand-computed case (arithmetic in the test comment). Report absolute and relative differences separately; percentage points are not percent.
  - Cohort maturity: a DN retention value for first-play date d is readable only after d + N days have fully passed in UTC plus the reporting lag the docs or fact-check give; otherwise the helper says "not mature" (never a number).
  - Sample-ratio check: chi-square goodness-of-fit against the planned split; the default alarm threshold is p < 0.0005 (Microsoft ExP practice; configurable) and the output says "invalid test: investigate" not "adjust".
  - Sample size: two-proportion (normal approximation, two-sided alpha, power) and the mean-based approximation n = 16 sigma^2 / delta^2 per arm (21 for 90% power), with a warning that skewed revenue data needs care. Never output a sample size without its inputs.
  - Tests are offline unittest files that `python tools/verify.py` discovers; one test plants a fake key and proves it appears in no output, file or exception text, including on HTTP errors and failed polls.
  - No game-specific content in kit files. Never name a file report*, summary*, findings* or analysis*.
deliver: tools/analytics/ with README.md (how the owner makes the key and sets the variable themselves — the agent never sees the key — how to run a pull, where data goes, the 21-day warning), tests in tools/tests/, a short hand-back
checks:
  - C1: python -m unittest discover -s tools/tests -p "test_analytics_*.py" -t tools/tests passes with no network
  - C2: the planted-key test fails if you add a print of the key anywhere (show you tried it)
  - C3: a fixture with a 202 then a done response is read into history with statuses kept; a second pull of the same bucket with a revised value keeps both
  - C4: each stats formula has at least one test with a checked value
  - C5: python tools/verify.py shows the tests and sync checks passing (other jobs' files may fail; name them)
return: hand-back per rules/messages.md §3 to the lead: STATUS first, coverage of every item above (done / not done), files, checks with evidence, decisions_made, the exact key scopes the owner must grant, the CLI commands the analyst will use.
</spec>
```
