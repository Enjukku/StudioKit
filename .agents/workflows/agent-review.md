---
description: Score every subagent on freshness and real performance, pick the ones that need work with the owner, review them against the newest Anthropic guidance and their own failures, and keep a change only if the next score holds.
---

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20 (ported)

# /agent-review: score and update the agents

Run when the owner asks, after a new model or harness release, or when `/improve` flags an agent. Lead tier at medium effort. Write to the owner per `rules/owner-profile.md`.

## Step 1: Score

1. `python tools/agent_scorecard.py --days 30 --json knowledge/logs/agent-review/<today>.json` (create the folder if missing).
2. Compare with the newest earlier JSON in `knowledge/logs/agent-review/`: per agent, score and each metric up or down. An agent changed at the last review whose score fell gets a revert proposal and a row in `knowledge/design/tried-and-failed.md`.
3. Score parts: freshness /40 (edited since the newest model release, prompt-style lint, dead path or skill references, frontmatter vs the orchestration roster) and performance /60 (finished runs, tool error rate, re-briefs, owner pushback after a run). A `?` score has under 3 runs: no evidence from use. Re-brief and pushback are approximations; read the runs before blaming the agent.

## Step 2: New information

Spawn one research agent (craft tier; the harness's guide agent if it has one): the harness's subagent docs, the prompting guides for the models in the roster, and release notes since the last review (newest wins, official sources only, claim + URL + date). Ask for new frontmatter fields, new model releases and anything that makes a line in our role files obsolete. If a model shipped, propose an update to the model release list in `tools/agent_scorecard.py` (the tool owner applies it).

## Step 3: Choose with the owner

Show the scorecard (only the table and each flagged agent's top 2 flags, in plain words). Recommend which agents to review: the "Review? YES" rows, plus any agent the new information touches. Ask in one decision digest item (`templates/jobs/decision-digest.md`) with a default. Agents with no runs in 30 days: propose deleting or merging them (fewer agents is the safer default; the orchestration skill is the roster).

## Step 4: Review each chosen agent

For each one, read:
- the role file (`.agents/roles/`) and the skills it loads;
- 2–3 of its recent runs where the owner pushed back or it was re-briefed (transcripts of its subagent runs, matched by description), to see what went wrong;
- its rows in `knowledge/design/tried-and-failed.md` and matching lessons in `knowledge/lessons/`.

Then propose edits: delete stale or duplicated lines first, then fix what the failures show, then apply the new guidance. Keep files short; the brief carries the task, the file carries only what holds for every task. Check model and effort against the orchestration skill and the `kit.json` tiers (lead / craft / mechanical; change role file and roster in one edit). Also check that the agent's tools and skills are still the right ones.

## Step 4b: Planted-mistake test (every run)

For each chosen agent, give one small task with a known, planted flaw in its own area (a wrong placement, a missing validation, a rule from `rules/` the brief does not mention). Write the test and its pass rule into the review log. Pass = the agent finds or avoids the flaw and cites the rule. A miss is a performance flag for that agent in Step 5. Use a scratch copy; never merge test material.

## Step 5: Apply and keep score

1. Apply the edits the owner approves, one agent at a time. Edit canonical files in `.agents/`; regenerate harness files with `python tools/sync_harness.py`. Run `python tools/verify.py`.
2. Write `knowledge/logs/agent-review/<today>.md` (at most 40 lines): scores, chosen agents, each change and the metric it should move, new guidance used (URL + date). The next review checks those metrics: a change is kept only if its metric held or improved.
3. Tell the owner in at most 10 lines: which agents changed, why, what the owner will notice. Commit only your own paths, with the attribution trailers.

---

Optional focus from the owner (agent names, or a window in days) follows.
