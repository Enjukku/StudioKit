---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent analyst)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J013 intent brief — analyst agent

<intent>
The owner makes the calls on design, progression, marketing and live events, but is not a data expert. The studio needs one agent that reads each game's own player data and turns it into a decision: what changed, for which players, how sure we are, and the one thing to do next. Wrong readings are worse than no reading: a D7 number from a cohort that has not finished its seven days, a "win" from a test that stopped early, or a benchmark copied from mobile games sends the team to fix the wrong thing.

So the agent reads carefully and talks simply. It splits "players are leaving" into a measurable symptom, finds where it starts, lists the competing explanations and looks for evidence against its own favourite. It uses causal words only when the design supports them. It plans Roblox Experiments before they start, says up front how many players and days a useful answer needs, and calls a result "inconclusive" or "invalid" when that is the truth. It says what a new feature must log to answer its design question; the logging code belongs to the `analytics` skill and engineering.

Every number it reports comes from a saved data pull or a deterministic calculation, never from writing. The pull tool uses only Roblox's official Open Cloud APIs with a key that lives in the owner's environment; it keeps the history so this month can be compared with last month.

Each week it writes one report for the owner and routes the parts that matter to the game designer, progression designer, marketing and the live-ops designer. The specialists decide the fixes; the analyst brings the evidence.

The owner's research paper is strong evidence, not gospel. Roblox analytics facts, benchmarks and statistics rules are checked; what cannot be backed up is dropped.
</intent>

<spec>
id: J013
from: owner
to: lead
skills: [orchestration, ste-writing, analytics, platform-policy, networking-security, dataviz]
refs:
  - C:\Users\Firew\Downloads\Roblox_Analyst_Research_2026.txt   # take: 15 rules, metric contract, metric table, peer-band reading, symptom split, competing-explanations table, funnel rules, causal ladder, economy accounting, purchase trace, native Experiments limits, power and duration rules, SRM, EHD, 5 verdicts, update-measurement hierarchy, 3 clocks, feedback coding, event contract, reporting shape, 12-step process, diagnosis checklist, 3 templates, don'ts. avoid: case uplifts as targets, Microsoft or King numbers as Roblox numbers, the illustrative D1 band as a benchmark
  - knowledge/external/roblox-creator-docs/cloud/guides/analytics/{index,metrics}.md + cloud/guides/experiments.md   # take: endpoints, auth scope, granularity, retention windows, status values, errors. avoid: guessing fields not in the docs
  - .agents/skills/analytics/SKILL.md   # take: what the logging side owns (T-01..T-12), so the analyst books point to it and do not repeat it
  - tools/trends/trend_keys.py, tools/trends/trend_store.py   # take: env-only key, redaction, append-only JSONL store, data dir outside git. avoid: copying collector politeness code that Open Cloud does not need
fixed:
  role_name: analyst                                    # roster (planned row)
  model: sonnet, medium; opus high for a deep investigation such as a big retention drop   # owner 2026-10-21
  scope: player data of our own games: quits, progress, session length, return, economy, purchases, device performance   # owner 2026-10-21
  answer_shape: one main finding, evidence, how sure, one recommendation, plain words   # owner 2026-10-21
  experiments: Roblox Experiments, planned and read correctly; no result called real without enough players and time   # owner 2026-10-21
  event_planning: the analyst decides what to log; the J001 analytics skill covers the logging code   # owner 2026-10-21
  weekly_report_to: owner, game-designer, progression-designer, marketing, live-ops-designer   # owner 2026-10-21
  tool: tools/ script on Roblox's official Open Cloud analytics APIs, saves history, with tests   # owner 2026-10-21
  key: owner's environment only; never in repo, notes, logs or chat   # owner 2026-10-21; AGENTS.md §3.4
  templates: weekly report for a non-expert owner, A/B test plan, A/B test result with plain-language verdict   # owner 2026-10-21
  hand_offs: game-designer, progression-designer, marketing, live-ops-designer (planned), engineering (logging requests); rules/messages.md format   # owner 2026-10-21
open: [book structure inside the two skills, tool module layout and CLI, metric set per pull, stats helper list, template field names, hand-off wording, eval cases]
avoid: [invented benchmarks or "good" values, p-value as "chance we are wrong", winners from early or harm-screen data, averaging daily rates without denominators, summed DAU as unique players, causal words for before/after comparisons, numbers written without a saved source]
owns: [knowledge/reference/analyst/, .agents/skills/<two books>/, tools/analytics/, tools/tests/test_analytics_*.py, templates/analytics/, .agents/roles/analyst.md, roster row, the description line of .agents/skills/analytics/SKILL.md (digest item 7), J013 job folder]
not_in_scope: [logging code, Creator Hub changes, live-ops role, raw player-level data, scraping, a real game diagnosis before G2]
rules:
  - Paraphrase sources; the paper stays outside git. Quotes ≤ 15 words, attributed.
  - Evidence tags kept (VERIFIED / EXPERIENCE / OPINION). A number without a scoped, dated source is dropped or marked PROPOSAL; platform numbers that move go in as link + date read.
  - Facts dated after 2026-06 are checked live before they enter a skill.
  - Keys: environment variable only; never printed, logged, saved or put in a URL; redacted from every error (networking-security N-11).
  - No game-specific content in kit files; game data lives outside git or in the game's own repo.
  - Skills ≤ 500 lines, "Read this file when" table, overlay line (templates/skill/SKILL.md).
  - Generated files are never edited by hand; run tools/sync_harness.py.
deliver: [notes + fact-checks, 2 skills, tools + tests, 3 templates, role file, hand-offs, evals, G2 package]
checks: job-card.md acceptance checks
return: rules/messages.md §3 hand-back (STATUS, coverage, evidence)
</spec>
