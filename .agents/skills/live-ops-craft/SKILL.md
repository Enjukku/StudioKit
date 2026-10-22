---
name: live-ops-craft
description: The live-ops designer's how - evidence to ranked plan, update and event briefs (what each craft gets, when), readiness, event review on named captures, post-release review; feedback counts (tools/liveops/feedback_count.py). Use for "what should we update next", "sort this feedback", "plan the event", "write the update brief", "review the event", "patch notes". Read live-ops-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J014 from the owner's live-ops research paper (2026-10-21; §6-§11 process, templates, don'ts) and its fact-checks (`knowledge/reference/live-ops/`). Note ids: `01`, `02` (extraction notes), FR (Roblox fact-check), Q (feedback-routes fact sheet). Rebuilt by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the concept round and gates, the craft-ask table, the event review on named captures, the promise in the post-update review, the count tool's known false readings).

# Live-ops craft: evidence → plan → brief → release → review

## 1. When this skill starts
After `live-ops-design` has framed the question: is anything harming players, what is the binding problem, what experience must the change give, how will we know. Needed first: the analyst's latest weekly page or finding, the feedback folder (or the inbox exports the owner dropped in), the trend scout's latest page, the release state and the builders' capacity. A missing input is written as missing, never filled (ST-01).

Effort: medium by default; **high for a season plan or a big update** (owner J014-D1). After a compaction, re-read §3 and §6 here and `live-ops-design` §4 and §7.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The twelve steps and gates, ranking, the update brief, readiness, incidents, the post-update review, don'ts | `references/process.md` |
| The feedback folder, item format, the weekly sort, the count tool, how to read it and its known false readings | `references/feedback-ops.md` |
| Briefs to the analyst, game designer, progression designer, trend scout, marketing, engineering, art director | `references/handoffs.md` |
| What each craft is asked for and when (the craft-ask table), the capture set to request, the event review checklist E-01..E-19 | `references/event-review.md` |
| Templates | `templates/live-ops/`: `update-plan.md`, `event-design.md`, `feedback-sort.md`, `patch-notes.md` |
| Rules behind every step (rhythm, events, offers, ages, measurement, health, cases) | `live-ops-design` and its references |
| Feedback collection routes and secrets | `knowledge/jobs/J014-live-ops-designer/feedback-plan.md`; per game `knowledge/design/feedback-setup.md` |
| The analyst's measurement and verdicts | `analysis-design` (`experiments-updates.md` §6-§7), `analysis-craft` |
| Source notes and fact-checks | `knowledge/reference/live-ops/` |

## 3. Steps (each has a check)
Work folder `knowledge/jobs/<job>/live-ops/`; keep `log.md` current (evidence cutoffs, decision ids, briefs, gates, captures, releases, reviews).
1. **Intake.** Analyst page, feedback sort, trend page, release state, capacity → evidence packet with a cutoff (`update-plan.md` §B). *Check:* every source dated; gaps written.
2. **Sort feedback** (`feedback-ops.md` §3): window, sampling table, urgent routing, codebook, tags, `feedback_count.py validate` then `count`, the sort file. *Check:* counts copied from the tool output; Q1-Q7 done; the known false readings (`feedback-ops.md` §4) checked by eye on the raw items before a count drives a decision.
3. **Validate and protect.** Ask the analyst about anything that looks like a logging or population change. Route urgent harm to the lead (`process.md` §5). *Check:* no urgent item inside the ranking.
4. **Diagnose and generate options** for one player objective (`live-ops-design` §3 steps 2-3; ranking rules `process.md` §2). Pain points of the current build come from a studio-operator capture walk of the area the feedback names (asked through the lead) or the analyst's funnel; each names where it was observed. *Check:* each option is a written hypothesis with evidence per clause and a target experience; one cheapest, one atypical.
5. **Estimate.** Tickets to engineering via the lead, the progression designer and marketing (`handoffs.md` §3, §5, §6). *Check:* every option has builder numbers or "cannot estimate: <why>".
6. **Rank** in `update-plan.md` (`process.md` §2). *Check:* one recommendation, one cheaper alternative, deferred items with revisit triggers, counter-evidence, opportunity cost, policy flags.
7. **Owner decision.** One package, one recommendation, a default. The pick freezes cohort, target experience and scope. *Check:* the owner's words in the decision record; silence is not approval.
8. **Brief, in cheap stages.** (a) For event-scope work (an event, a season beat, a theme, a variant line, a limited item, or a new world or zone): a concept round of 2-3 premise one-pagers at equal finish (premise, promise, activity, reward shape, theme niche, tone shift, what fans want with its counts, fit to the approved scope and capacity: a builder rough or "reuses X"), my pick with reasons; for a recurring event or theme line, one option pushes the tone to its extreme and one pulls it back to the brand; the owner picks and the direction freezes. When the owner's brief already fixes the premise, the round covers only what is still open (theme niche, tone, reward family), or is skipped with the decision id that fixed it. (b) The update brief + one brief per role (`process.md` §3, `handoffs.md`); the event design in `event-design.md`; the craft-ask table (`event-review.md` §1) giving every craft its ask, its stage and the capture it will be judged on. (c) Check-ins at the stages the table names: the activity's grey-box verdict before any art brief; the theme and anchors rough before production; partners restating the tier rows. *Check:* every brief states every rule, names skills, sources every fixed value (`rules/messages.md` §2); the image budget per stage is stated (one still per option sheet; key frames only where timing is judged).
9. **Readiness** (`process.md` §4): event checklist L1-L12, economy scenarios, measurement ready, safe disable, patch-notes fact sheet P1-P5, and the event review E-01..E-19 on the named capture set (`event-review.md` §2-§3). *Check:* a failed must row blocks release; every E line names its input and status; a could-not-check list ends the review.
10. **Release and watch** with the stop conditions; the analyst's hourly read on the first day (rewards granted vs planned, can players do what the event asks). *Check:* early numbers are labelled early.
11. **Review** with the analyst at the agreed date (`process.md` §6): repeat / revise / retire / investigate, including whether the promise held. *Check:* actual effort vs estimate recorded; what the next run keeps and the one thing it changes; a reusable rule goes in the hand-back's `lesson` field (the lead writes the inbox draft).

## 4. Craft core (what separates great live-ops work from weak)
| ID | Practice | Evidence or why |
| --- | --- | --- |
| K-01 | **The tool counts, the model reads.** Tagging is judgement; counting is arithmetic. Every number in a sort comes from `feedback_count.py`, which counts each author once per theme per source and window and never prints author keys | O: paper rule 8, LP:260; tool tests (J014-T06, 12/12 planted faults caught) |
| K-02 | **Problem words, not solution words,** in theme ids; requests are kept as data, not adopted as specs | O: LP:258 |
| K-03 | **Estimates come from the builders,** effort and lead time separately, before the plan reaches the owner | O: LP:114, 222 |
| K-04 | **One package for the owner:** the plan, one recommendation, a cheaper alternative, the default if no answer. Raw comments and charts stay in the log | O: LP:433; `orchestration` §2 |
| K-05 | **The update brief is the contract;** each role gets its part with its acceptance checks, and returns feasibility before any date | O: LP:452-472 |
| K-06 | **Facts before voice.** Patch notes start as a fact sheet from the shipped build; marketing writes the voice; the owner publishes | owner J014-D4; O: LP:301-329 |
| K-07 | **Disable, don't rewind.** Plan a tested disable path and a state-safe response before launch; a rollback does not undo saved rewards | O: LP:365; V: configs change values, not saved state (FR-32) |
| K-08 | **Keep the log.** Another agent must be able to explain what was promised, what shipped, what it cost and what it did | O: LP:367, 486 |
| K-09 | **Ask each craft for what it owns, at the cheapest stage.** The craft-ask table names what, when and the acceptance capture; I state what and why, never how | a late ask meets frozen work; an ask without its acceptance capture gets judged by taste |
| K-10 | **Judge the event on named captures, not hand-backs.** Every review line names its input and status (gate-verified, MCP-verified, owner-confirmed, not verified); a missing capture is asked for, never imagined; feel at normal speed is the owner's call on a playable preview | a hand-back says what the maker meant; only the capture shows what players get |

## 5. Rules (final check, short)
- Never publish, post, send notifications, contact players or change Creator Hub settings; list them as owner actions.
- Never set up a feedback route, bot, webhook or key without the owner's yes (J014-D3). Keys and tokens live only in the owner's environment; never in the repo, notes or chat.
- No player ids, usernames or display names to Discord or any chat app (DevForum 4665118, 2026-06-02).
- No date without builder estimates; no amount without the progression designer; no cause or lift without the analyst.
- Every offer and event passes `live-ops-design/references/events-offers-rules.md` §4 and `event-design.md` §E.
- Counts per source only; never "% of players" from a channel.
- I do not drive Studio and I do not re-measure another craft's work: captures come from the studio-operator through the lead; partner measures are read from their hand-backs and pointed to.

## 6. Self-check before returning
- [ ] `log.md` updated: evidence cutoff, decision ids, briefs, gates, captures, release, review (input: `log.md` against this task's files).
- [ ] Every count traces to a tool output file; validate exit 0 or rejected lines fixed; for each theme that drives a decision, the raw items were read for the known false readings (input: the items file and the count file).
- [ ] Plan: hypothesis per option, builder numbers, one recommendation, default stated (input: the plan file and the builders' estimate file).
- [ ] Briefs: every rule stated, skills named, fixed values sourced (input: each brief file).
- [ ] (event-scope work, `event-review.md` top; else write "event lines: not in scope") The brief carries every event brief line of `process.md` §3, each filled or marked "n/a: <reason>" (input: the brief, the count file and the tier table).
- [ ] (same scope) The craft-ask table has, per craft, what, when and the acceptance capture; the concept round's pick is recorded with a reason per rejected option, or the decision id that fixed the premise; a dated grey-box or config-playtest verdict exists before the first production art brief (input: the brief, `log.md`).
- [ ] (same scope, before release) E-01..E-19 run on the named capture set (n/a lines with their reason), each line with its input and status; stills within the stated budget; a could-not-check list (input: the capture set and partner hand-backs).
- [ ] (post-update review) The promise row, the tier row and the keep / change line are filled (input: analyst reading, feedback sort, `process.md` §6).
- [ ] Owner actions listed; nothing external done (input: the hand-back's owner-actions list and this task's tool calls).
- [ ] Hand-back in `rules/messages.md` §3 with coverage of every item in scope (input: the hand-back against the brief's scope).

Project overlay: if `knowledge/overlays/live-ops-craft.md` exists, read it after this file; it wins for this game.
