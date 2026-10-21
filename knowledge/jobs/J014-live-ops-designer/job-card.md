---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent live-ops-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J014 — Build the live-ops designer agent

| Field | Value |
| --- | --- |
| Job id | J014-live-ops-designer (opened as J013 at 05:18; renamed 2026-10-21 because J013-analyst and J013-film-director, opened by other chats minutes later, reuse J013 ticket and decision ids) |
| Size | L (new role, 2 skill books, a 749-line paper with 51 dated sources (R01-R22 Roblox, G01-G29 studios) to extract and fact-check, 4 templates, a feedback-collection plan for owner review, a real test on a synthetic live game) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J014-D4). Steps 2-6 done 2026-10-21: notes, fact-checks FR 58 / FG 36, feedback fact sheet, count tool (19 tests), 2 skills, 4 templates, role, evals, roster; G2 test T08 on a synthetic game graded 24.5 / 26 (T09), 14 + 4 skill gaps fixed. G1b feedback plan and G2 wait for the owner (`digest.md` items 9-14). Gate: RESULT FAIL only from other jobs' files (J005, J013-analyst, J015) |
| Depends on | `analytics`, `platform-policy`, `game-design`, `progression-design`/`progression-craft`, `market-trends`/`trend-scan`, `marketing-design`/`marketing-craft` skills (exist); analyst role (planned, not built) |

## Owner's words (2026-10-21, excerpts)
- "It starts when a game is live, and plans what comes next: updates, events, seasons, limited-time content, new features and fixes, so players keep coming back and the game keeps growing."
- "It decides from evidence: the analyst's numbers and weekly report, player feedback (in-game feedback, Discord, comments, reviews) and the trend scout's reports."
- "It sorts and counts player feedback by theme, and weighs loud players against the silent majority."
- "It proposes a ranked update plan to me (evidence, expected impact, effort, who builds it), with one recommendation. After I pick, it writes the update brief for the game designer, progression designer, marketing and the builders."
- "After each update, it checks the results with the analyst and records what worked and what did not."
- "It follows Roblox's rules on events, paid random items, limited-time offers and younger players, and it never promises what the studio cannot build in time."
- "Templates: an update plan, an event design, a player feedback sort, and patch notes."
- "A plan for collecting player feedback from the game and from Discord into one place the agent can read. Show it to me before setting anything up. No bot tokens or passwords in the repo or in chat."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially update rhythms, event effects and Roblox rules, and drop what you cannot back up."
- "Model: Opus, medium effort; high effort for a season plan or a big update."

## Goal
One `live-ops-designer` agent that, once a game is live, owns the argument for what the game does next. It reads the analyst's numbers, the sorted player feedback and the trend scout's signals; proposes a ranked update plan with one recommendation; after the owner picks, writes the update brief and hand-offs; and after release reads the result with the analyst and records repeat / revise / retire / investigate. It plans only what the studio can build, test and support in time, and keeps every event and offer inside Roblox rules.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\live-ops-designer-research.txt` (outside git; owner wrote it) | Mandate + evidence contract; 15 rules; 10 studied games; update rhythm and production economics; content types; events (return reasons, duration, calendars, ethical urgency) + event template; ranking evidence into a plan + plan template; player feedback (collection, taxonomy, distinct-author counts, loud vs silent) + sort template; communication + patch-notes template; measuring an update (observational vs Roblox experiments, failure response); long-term health (economy, power creep, catch-up, burnout); Roblox rules (events, offers, paid random items, younger players, links, notifications); 11-step process, update brief contract, post-update review template, don'ts; open questions; source register | 749 lines, 99 KB | high: VERIFIED / EXPERIENCE / OPINION on every claim, dated sources with quotes. The paper had no studio data, no feedback corpus and no capacity numbers. Many Roblox pages are "undated; checked 2026-10-21" → live check |
| Kit: `analytics` (events, funnels, Experiments), `platform-policy`, `game-design` (§live updates), `progression-craft` (live tuning), `market-trends`/`trend-scan`, `marketing-craft` (update and event announcements; hand-off §5 to live-ops), local docs mirror (`production/game-design/content-updates.md`, `liveops-essentials`, `analytics-essentials`) | What neighbours already own, so the live-ops books point to them and do not repeat them | — | owner-approved |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/live-ops/` + fact-check tables (Roblox cadence, events, Experiments, notifications, links, paid random items, offers, younger players; studio cases G01-G29) | Running a real game's live ops (no live game yet) |
| Skills `live-ops-design` (what and why) and `live-ops-craft` (how) — names: digest item 2 | Setting up any feedback route, bot, webhook, Open Cloud key or Discord server (plan only; owner decides first) |
| 4 templates in `templates/live-ops/`: update plan, event design, player feedback sort, patch notes (+ update brief and post-update review inside the craft skill if they fit there) | Building the analyst role (hand-off briefs only; lead holds tickets) |
| Feedback-collection plan `knowledge/jobs/J014-live-ops-designer/feedback-plan.md`: in-game route, Discord route, other sources, one store the agent reads, privacy and younger-player rules, where secrets live, owner actions — shown to the owner before anything is built | Changes to other roles' skills beyond one pointer line each where they say "live-ops-designer (planned)" |
| Small offline tool for deterministic feedback counts (distinct authors per theme, per source and window) + tests — digest item 5 | Paid surveys, player studies, contacting players |
| Role file `live-ops-designer`; roster row update | Publishing patch notes or posts (marketing prepares, owner publishes) |
| Hand-off briefs to analyst (planned), game designer, progression designer, trend scout, marketing, engineering (architect / builders) in `rules/messages.md` format | |
| Eval briefs + hidden cases; 1 real test (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×2 (paper mandate, rules, §1-§5: cases, rhythm, content types, events, ranking; §6-§11 + templates + don'ts + open questions: feedback, communication, measurement, health, Roblox rules, process) | Sonnet | high (J012 precedent) | dense notes per part |
| fact-checkers ×2 (Roblox R01-R22 + every rule in §10: local docs mirror first, then live docs, DevForum, `platform-policy`; studio cases G01-G29: official posts, dates, numbers, scope) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| researcher (feedback routes: Roblox native in-experience surveys, in-game text input + filtering + under-13 rules, DataStore/MemoryStore + Open Cloud read, HttpService limits, Discord API and terms, Discord export, privacy) | Sonnet | high | fact sheet for the feedback plan |
| tool builder (feedback count tool + tests) | Opus | medium | script + tests |
| lead (merge, skills, templates, feedback plan, role, hand-offs, evals, review) | Opus | high | 2 skills, 4 templates, plan, role, hand-offs, evals, roster |
| test-pack builder (synthetic live game: analyst weekly report, ~150 feedback items across 4 sources, trend note, capacity; labelled synthetic; separate context so the hidden set stays hidden) | Sonnet | high | test pack |
| live-ops test (new agent) | Opus | high (big update) | G2 package |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time. Wave 1: 2 extractors + feedback-route researcher. Wave 2: 2 fact-checkers + tool builder. The lead writes the skills, templates and the feedback plan (it needs the paper, the fact-checks and the neighbour skills together). Wave 3: test-pack builder, then the new agent runs the G2 test, then the grader.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | 1 |
| Agents | 2 extract + 2 fact-check + 1 research + 1 tool + 1 test pack + 1 test + 1 grader = 9 | 9 (T01-T09) |
| Models / effort | Sonnet high ×7; Opus medium ×1; Opus high ×1 + lead | as estimated |

## Acceptance checks
- [ ] Every cadence, event-effect, case number and Roblox rule in a skill has a source, a date and a fact-check verdict (confirmed / corrected / unverified-kept-with-label / dropped); dropped claims listed with the reason.
- [ ] No invented numbers: no best cadence, event length, retention lift, multiplier or price. Case results stay EXPERIENCE with their scope; announcements are never treated as proof of effect.
- [ ] Feedback sort counts distinct authors per theme per source and window, keeps message volume separate, never reports a Discord share as "% of players"; the tool's tests prove it (including a planted double-count).
- [ ] Ranked plan: each option has evidence with labels, expected impact as a range or "unknown", effort from the builders (not guessed), who builds, risks, policy flags; exactly one recommendation; capacity check before any date.
- [ ] Every measurement is predeclared with the analyst: cohort, primary metric, guardrails, comparison, window; observational vs Roblox Experiment named; "insufficient evidence" allowed.
- [ ] Policy: events, limited-time offers, paid random items (odds total 100%, indirect Robux), younger players, links and notifications restated from `platform-policy` and the fact-check, with owner actions listed.
- [ ] Feedback plan: shown to the owner, nothing set up; no token, key or password in the repo or chat; secrets in environment variables or the place's Secrets store; younger-player and privacy rules named.
- [ ] 4 templates exist and each one is used in the G2 test or an eval.
- [ ] Hand-off briefs to the 6 roles follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "You may go ahead and begin." |
| G1b feedback plan (before any setup) | | |
| G2 first real test | | |
| G3 final approval | | |
