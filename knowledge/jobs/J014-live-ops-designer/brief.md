---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent live-ops-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J014 intent brief — live-ops designer agent

<intent>
A launched game lives or dies on what it does next. Players come back when there is a real reason to return, and they leave when an update breaks trust, buries them in chores or promises what never arrives. The studio needs one agent that owns that question once a game is live: what should we ship next, and why.

It decides from evidence, not from the loudest message. It reads the analyst's numbers and weekly report, the trend scout's dated signals, and player feedback from the game, Discord, comments and reviews. It sorts feedback by theme and counts distinct players per theme in each source, so a busy Discord thread is not mistaken for the whole player base, and silent players are checked through behaviour data, not assumed happy.

It proposes a ranked update plan with one recommendation: evidence, expected impact, effort as the builders estimate it, and who builds it. It fixes blockers before it buys attention for new content. It never promises a date the studio cannot build, test and support. After the owner picks, it writes the update brief for the game designer, progression designer, marketing and the builders. After release it reads the result with the analyst against what was predeclared, and records repeat, revise, retire or investigate. "Insufficient evidence" is an allowed answer.

It keeps events, limited-time offers and paid random items honest and inside Roblox rules, with younger players in mind. Urgency comes from a real reason to play now, not from pressure.

The owner's research paper is strong evidence, not gospel. Update rhythms, event effects and Roblox rules get a live check. A number the research cannot back up is dropped, not guessed.
</intent>

<spec>
id: J014
from: owner
to: lead
skills: [orchestration, ste-writing, analytics, platform-policy, game-design, progression-design, market-trends, marketing-design]
refs:
  - C:\Users\Firew\Downloads\live-ops-designer-research.txt   # take: mandate and role split; 15 rules; cases as mechanisms (not benchmarks); cadence vs capacity; content-type jobs; event design + ethical urgency; ranking (reach, effect, duration, confidence, effort incl. ongoing cost); feedback taxonomy + distinct-author counting + loud/silent; communication sequence; measurement discipline + failure-response table; economy/power/catch-up/burnout; §10 Roblox rules; 11-step process, update brief contract, post-update review, don'ts; open questions. avoid: case numbers as forecasts, announced schedules as development time, averaging cadences into a "best" cadence
  - knowledge/external/roblox-creator-docs/production/game-design/   # content-updates, liveops-essentials, analytics-essentials: local mirror first
  - .agents/skills/{analytics, platform-policy, game-design, progression-craft, trend-scan, marketing-craft}   # take: what each neighbour owns (metrics and Experiments; policy flags; live-update design review; live tuning; scout hand-offs; announcements and hand-off §5 to live-ops), so the live-ops books point to them and do not repeat them
fixed:
  role_name: live-ops-designer                                   # roster row (planned, "later")
  model: opus                                                    # owner 2026-10-21
  effort: medium; high for a season plan or a big update         # owner 2026-10-21
  starts: when a game is live                                    # owner 2026-10-21
  plans: updates, events, seasons, limited-time content, new features, fixes   # owner 2026-10-21
  evidence: analyst numbers + weekly report; feedback (in-game, Discord, comments, reviews); trend scout reports   # owner 2026-10-21
  feedback: sort and count by theme; weigh loud players against the silent majority   # owner 2026-10-21
  plan_output: ranked plan (evidence, expected impact, effort, who builds) + one recommendation; owner picks   # owner 2026-10-21
  after_pick: update brief to game designer, progression designer, marketing, builders   # owner 2026-10-21
  after_update: results read with the analyst; what worked and what did not recorded   # owner 2026-10-21
  rules: Roblox rules on events, paid random items, limited-time offers, younger players; no promise the studio cannot build in time   # owner 2026-10-21
  templates: update plan, event design, player feedback sort, patch notes   # owner 2026-10-21
  feedback_plan: game + Discord into one place the agent reads; shown to the owner before any setup; no bot tokens or passwords in repo or chat   # owner 2026-10-21
  hand_offs: analyst, game designer, progression designer, trend scout, marketing, engineering; rules/messages.md brief format   # owner 2026-10-21
open: [book structure inside the two skills, template field names, feedback taxonomy wording, count tool shape, feedback-plan options, hand-off wording, eval cases]
avoid: [invented optima (cadence, event length, multipliers, retention lift), case numbers as forecasts, "% of players" from Discord, fear-of-missing-out pressure as a tactic, dates without builder estimates]
owns: [knowledge/reference/live-ops/, .agents/skills/<two books>/, templates/live-ops/, the count tool + its test, knowledge/jobs/J014-live-ops-designer/ (incl. feedback-plan.md), .agents/roles/live-ops-designer.md, roster row, one pointer line in each neighbour role or hand-off file that says "live-ops-designer (planned)"]
not_in_scope: [setting up any feedback route, bot, webhook or key; building the analyst role; publishing; contacting players; a real game's live plan]
rules:
  - Paraphrase sources; the paper stays outside git. Quotes ≤ 15 words, attributed.
  - Evidence tags kept (VERIFIED / EXPERIENCE / OPINION). A number without a scoped, dated source is dropped or marked PROPOSAL; platform numbers that move go in as link + date read.
  - Facts dated after 2026-06 or "undated; checked 2026-10-21" get a live check before they enter a skill.
  - Secrets (bot tokens, API keys, passwords) never in the repo, notes or chat; environment variables or the place's Secrets store (AGENTS.md §3.4).
  - No game-specific content in kit files.
  - Skills ≤ 500 lines, "Read this file when" table, overlay line (templates/skill/SKILL.md).
  - Generated files are never edited by hand; run tools/sync_harness.py.
deliver: [notes + fact-checks, feedback-route fact sheet, feedback plan (owner review), 2 skills, 4 templates, count tool + tests, role file, hand-offs, evals, G2 package]
checks: job-card.md acceptance checks
return: rules/messages.md §3 hand-back (STATUS, coverage, evidence)
</spec>
