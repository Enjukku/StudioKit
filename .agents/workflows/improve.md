---
description: Weekly self-improvement pass. Finds the week's mistakes, consolidates lesson drafts into the knowledge base (merge, supersede, prune, promote), checks context health, applies safe fixes, proposes the rest to the owner, and coaches the owner with the newest official guidance.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit workflow: universal. Merges the earlier `/improve` (owner request 2026-10-09) with the learning loop (`rules/knowledge.md` §8). Revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D R6, R7, R9, R18; lead decision LD11: lessons arrive in hand-backs).

# /improve — the weekly review and learning pass

Run once a week (or `/improve 14` for a 14-day window). Lead model at medium effort; mechanical steps go to cheap agents. Write to the owner per `rules/owner-profile.md`.

## Step 1: Gather (scripts, cheap)

1. Window: since the newest `knowledge/logs/improve/*.md`, else 7 days.
2. `python tools/improve_scan.py --since <date>`: owner messages (corrections flagged), interrupts, rejected or dismissed questions, tool errors, repeated commands, tokens by model and agent.
   2b. `python tools/usage_report.py --since <date>` (kit) and `--root <game repo>` for each game worked on this week: context per session and subagent, worktrees included; its flags (big context, no compaction, many images, many calls, helper on Opus) go into step 2.
3. `git log --since=<date> --stat --oneline`; new rows in `decisions.md`, `tried-and-failed.md`, `open-questions.md`; job ledgers closed this week.
4. `knowledge/inbox/` drafts (with their `cause` and `layer` fields; the lead writes them from the `lesson` field of hand-backs, `rules/messages.md` §3); `python tools/kb_index.py --lint`; `python tools/eval_context.py --compare <last week's knowledge/logs/improve/*-retrieval.json> --save knowledge/logs/improve/YYYY-MM-DD-retrieval.json` (score vs last week; exit 1 when recall@10 drops).
5. Closed jobs' `evidence.md`: defects by cause and the metrics at close (first-pass acceptance, repair rounds by cause, defects the owner found after internal review, stale hand-offs, unsupported "done" claims, usage vs estimate). Compare with earlier jobs of the same type.
6. Last week's improve log: did each change hold, or did the same mistake return?
7. Claude Code version (`claude --version`): if it changed since the last run, re-run the capability probes listed in `rules/knowledge.md` §8.5 and update the capability record it names.

## Step 2: Find the mistakes

One row per owner correction, redo, interrupt, rejection, gate "no", and each tool-error cluster: what happened, root cause, layer to fix. The first ten causes are the draft `cause` values of `rules/knowledge.md` §8, word for word.

| Root cause (draft `cause`) | Fix layer | Proof the fix works |
| --- | --- | --- |
| Context missed (it existed, nobody read it) | retrieval: packet ranking, a `roles:` tag, an index link; **a new case in `knowledge/evals/retrieval.jsonl`** | retrieval score holds or rises |
| Context missing | a vault entry: decision, vocabulary, precedent, catalog, game profile or owner profile | the next packet for that task shows it |
| Brief gap | `rules/messages.md`, the brief template or the recipe stage's brief | the next brief passes `rules/messages.md` §9 |
| Interface conflict | the recipe's interface stage or the contract template | fewer late conflicts in the next job of that type |
| Craft error | **the step** of that role's book that should have caught it, plus an eval brief | skill evals; monthly scorecard |
| Defect found by the owner after internal review | a seeded fault for reviewer evals (code: `.agents/skills/code-review/evals/briefs.md`; visual crafts: the evals of that craft's review skill, e.g. `.agents/skills/art-review/evals/`) and a check in the reviewer's book | the reviewer catches the seeded fault |
| Review broke correct work | protected-list rule; the reviewer's book | fewer collateral regressions |
| Tool failure | the tool, or the capability record | the probe or test passes |
| Owner taste change | `knowledge/design/taste-log.md` → overlay or art bible proposal | fewer change requests at the next gate |
| Win | step 3 item 2b: a recipe step, a worked example in the role's book, or a precedent | first-pass acceptance holds |
| A rule or skill line is stale, wrong or too narrow | edit or delete that line (pruning beats adding) | — |
| Same mistake a second time | promote: rule line, then a hook if it must always hold | the mistake does not return |
| Brief, routing or gate problem | orchestration skill, a recipe, or `rules/company.md` | — |
| Overcomplication (rounds of patches, size far over estimate) | a simplification review, not another patch | — |
| Oversized context (usage report flags) | `rules/assistants/claude.md` rows Session size, Images, Tool calls, Helper models; or the book step that loads too much; a settings proposal for the owner (`knowledge/jobs/J022-context-and-usage/settings-proposal.md`) | next week's report: median context and calls per session fall, repair rounds do not rise |

Check `tried-and-failed.md` first: repeating a recorded failure is the most important finding.

## Step 3: Consolidate the knowledge base (the "dreaming" pass)

Delegate the mechanical part to a Sonnet agent with this list; the lead decides promotions.
1. **Inbox:** group drafts by topic; merge duplicates; drop drafts with no evidence. A hand-back `lesson` that reached no draft (the lead missed it at the gate) is written now from the job's hand-backs.
2. **Promote** a lesson to `knowledge/lessons/<area>/`, a skill step, a rule line, a recipe stage or an overlay **only if** it happened twice or the owner said or confirmed it. Link the evidence. Mark its scope: universal (kit candidate) or game. Put a craft lesson into **the step it fixes**, not a growing warning list.
2b. **Wins:** a method that passed first time in two jobs becomes a recipe step or a worked example in that role's book; an accepted artifact the vault lacks goes to `knowledge/design/precedents.md`.
3. **Supersede** notes the week contradicted (`status: superseded`, link the replacement). Convert relative dates to absolute.
4. **Agent memories** (`.claude/agent-memory/*/MEMORY.md`): merge duplicates, remove what moved into the vault, keep each under 200 lines.
5. **Prune:** notes unused and unlinked for 60+ days, stale facts after a model or engine update, duplicated rules.
6. Move processed drafts to `knowledge/inbox/processed/YYYY-MM-DD/`.

## Step 4: Context health

- Always-loaded size ≤ 200 lines; skills under 500 lines; skill descriptions ≤ 400 characters; lint clean; retrieval score not lower than last week.
- `knowledge/jobs/active.md` lists only open jobs; every closed job was filed into the vault (`orchestration` skill §9).
- After a new model or harness release: re-check the orchestration skill and role files; suggest `/doctor prompt-audit` (Claude).

## Step 5: Apply, one change at a time

- Apply now: dead links, stale facts, ledger rows, retrieval scope, lesson notes, typo-level rule fixes. Run the gate.
- Changes to rules, skills, roles, hooks or code behavior: one recommendation each in the owner's decision digest (`templates/jobs/decision-digest.md`). Apply only what the owner approves. A rejected or reverted change gets a `tried-and-failed` row.

## Step 6: Coach the owner

- **Prompt score:** 10-15 owner requests that started work, 0-2 each on outcome, why, done-when, one job, feedback-with-reference. Week score out of 10, trend, and one real request rewritten to score 10 in the owner's voice.
- **Tips:** one research agent (cheap model) reads the official changelog and docs since the last run (official sources only, newest first, with dates). At most 3 tips that fit what the owner did this week, and at most 3 automation ideas from repeated work, each with a build / don't-build recommendation.

## Step 6b: Monthly agent review (first run of each month)

`python tools/agent_scorecard.py --days 30 --json knowledge/logs/agent-review/<date>.json`; compare with the last saved run. Roles whose score fell after a change get a revert proposal and a `tried-and-failed` row; roles whose score is low or stale (older than the newest model or harness release) get one improvement proposal each in the owner digest. Keep a role change only if the next month's score holds.

## Step 7: Report and log

1. `knowledge/logs/improve/YYYY-MM-DD.md` (≤ 60 lines): window, numbers, mistakes table, consolidation summary (merged / promoted / superseded / pruned), retrieval score, prompt score, applied and proposed changes with the owner's answers, tips.
2. Tell the owner in ≤ 15 lines: the 3 biggest mistakes and what changed, what the knowledge base learned, decisions needed, tips.
3. Commit only your own paths, with the attribution trailers.
