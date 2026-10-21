---
name: live-ops-craft
description: The live-ops designer's procedure for a live Roblox game - from an evidence packet to a ranked update plan, an owner decision, update briefs, a release-readiness record and a post-update review. Covers the twelve-step cycle with gates, the weekly evidence review (not a weekly release), sorting player feedback and counting distinct players per theme with tools/liveops/feedback_count.py, the one feedback folder, ranking without fake precision, capacity checks before any date, the update brief and what each role receives, hand-off briefs to the analyst, game designer, progression designer, trend scout, marketing and engineering, the event checklist, patch-notes facts, incidents and safe disabling, and the templates (update plan, event design, feedback sort, patch notes). Use for "what should we update next", "sort this feedback", "how many players want X", "plan the event", "write the update brief", "write the patch notes", "the update broke something", "review the event". Read live-ops-design first (what and why); this is how. Never publishes, posts or contacts players; the owner does.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J014 from the owner's live-ops research paper (2026-10-21; §6-§11 process, templates, don'ts) and its fact-checks (`knowledge/reference/live-ops/`). Note ids: `01`, `02` (extraction notes), FR (Roblox fact-check), Q (feedback-routes fact sheet).

# Live-ops craft: evidence → plan → brief → release → review

## 1. When this skill starts
After `live-ops-design` has framed the question: is anything harming players, what is the binding problem, how will we know. Needed first: the analyst's latest weekly page or finding, the feedback folder (or the inbox exports the owner dropped in), the trend scout's latest page, the release state and the builders' capacity. A missing input is written as missing, never filled (ST-01).

Effort: medium by default; **high for a season plan or a big update** (owner J014-D1).

## 2. Read this file when
| You need | Open |
| --- | --- |
| The twelve steps and gates, ranking, the update brief, readiness, incidents, the post-update review, don'ts | `references/process.md` |
| The feedback folder, item format, the weekly sort, the count tool and how to read it | `references/feedback-ops.md` |
| Briefs to the analyst, game designer, progression designer, trend scout, marketing, engineering | `references/handoffs.md` |
| Templates | `templates/live-ops/`: `update-plan.md`, `event-design.md`, `feedback-sort.md`, `patch-notes.md` |
| Rules behind every step (rhythm, events, offers, ages, measurement, health, cases) | `live-ops-design` and its references |
| Feedback collection routes and secrets | `knowledge/jobs/J014-live-ops-designer/feedback-plan.md`; per game `knowledge/design/feedback-setup.md` |
| The analyst's measurement and verdicts | `analysis-design` (`experiments-updates.md` §6-§7), `analysis-craft` |
| Source notes and fact-checks | `knowledge/reference/live-ops/` |

## 3. Steps (each has a check)
Work folder `knowledge/jobs/<job>/live-ops/`; keep `log.md` current (evidence cutoffs, decision ids, briefs, releases, reviews).
1. **Intake.** Analyst page, feedback sort, trend page, release state, capacity → evidence packet with a cutoff (`update-plan.md` §B). *Check:* every source dated; gaps written.
2. **Sort feedback** (`feedback-ops.md` §3): window, sampling table, urgent routing, codebook, tags, `feedback_count.py validate` then `count`, the sort file. *Check:* counts copied from the tool output; Q1-Q7 done.
3. **Validate and protect.** Ask the analyst about anything that looks like a logging or population change. Route urgent harm to the lead (`process.md` §5). *Check:* no urgent item inside the ranking.
4. **Diagnose and generate options** (improve / add / simplify or remove / communicate / investigate) for one player objective. *Check:* each option is a written hypothesis with evidence per clause.
5. **Estimate.** Tickets to engineering via the lead, the progression designer and marketing (`handoffs.md` §3, §5, §6). *Check:* every option has builder numbers or "cannot estimate: <why>".
6. **Rank** in `update-plan.md` (`process.md` §2). *Check:* one recommendation, one cheaper alternative, deferred items with revisit triggers, counter-evidence, opportunity cost, policy flags.
7. **Owner decision.** One package, one recommendation, a default. *Check:* the owner's words in the decision record; silence is not approval.
8. **Brief.** Update brief + one brief per role (`process.md` §3, `handoffs.md`); event designs in `event-design.md`. *Check:* every brief states every rule, names skills, sources every fixed value (`rules/messages.md` §6).
9. **Readiness** (`process.md` §4): event checklist L1-L12, economy scenarios, measurement ready, safe disable, patch-notes fact sheet P1-P5. *Check:* a failed must row blocks release.
10. **Release and watch** with the stop conditions. *Check:* early numbers are labelled early.
11. **Review** with the analyst at the agreed date (`process.md` §6): repeat / revise / retire / investigate. *Check:* actual effort vs estimate recorded; lesson draft written.

## 4. Craft core (what separates great live-ops work from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| K-01 | **The tool counts, the model reads.** Tagging is judgement; counting is arithmetic. Every number in a sort comes from `feedback_count.py`, which counts each author once per theme per source and window and never prints author keys | O: paper rule 8, LP:260; tool tests (J014-T06, 12/12 planted faults caught) |
| K-02 | **Problem words, not solution words,** in theme ids; requests are kept as data, not adopted as specs | O: LP:258 |
| K-03 | **Estimates come from the builders,** effort and lead time separately, before the plan reaches the owner | O: LP:114, 222 |
| K-04 | **One package for the owner:** the plan, one recommendation, a cheaper alternative, the default if no answer. Raw comments and charts stay in the log | O: LP:433; `orchestration` §2 |
| K-05 | **The update brief is the contract;** each role gets its part with its acceptance checks, and returns feasibility before any date | O: LP:452-472 |
| K-06 | **Facts before voice.** Patch notes start as a fact sheet from the shipped build; marketing writes the voice; the owner publishes | owner J014-D4; O: LP:301-329 |
| K-07 | **Disable, don't rewind.** Plan a tested disable path and a state-safe response before launch; a rollback does not undo saved rewards | O: LP:365; V: configs change values, not saved state (FR-32) |
| K-08 | **Keep the log.** Another agent must be able to explain what was promised, what shipped, what it cost and what it did | O: LP:367, 486 |

## 5. Rules (final check, short)
- Never publish, post, send notifications, contact players or change Creator Hub settings; list them as owner actions.
- Never set up a feedback route, bot, webhook or key without the owner's yes (J014-D3). Keys and tokens live only in the owner's environment; never in the repo, notes or chat.
- No player ids, usernames or display names to Discord or any chat app (DevForum 4665118, 2026-06-02).
- No date without builder estimates; no amount without the progression designer; no cause or lift without the analyst.
- Every offer and event passes `live-ops-design/references/events-offers-rules.md` §4 and `event-design.md` §E.
- Counts per source only; never "% of players" from a channel.

## 6. Self-check before returning
- [ ] `log.md` updated: evidence cutoff, decision ids, briefs, release, review.
- [ ] Every count traces to a tool output file; validate exit 0 or rejected lines fixed.
- [ ] Plan: hypothesis per option, builder numbers, one recommendation, default stated.
- [ ] Briefs: every rule stated, skills named, fixed values sourced.
- [ ] Owner actions listed; nothing external done.
- [ ] Hand-back in `rules/messages.md` §3 with coverage of every item in scope.

Project overlay: if `knowledge/overlays/live-ops-craft.md` exists, read it after this file; it wins for this game.
