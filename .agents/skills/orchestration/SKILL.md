---
name: orchestration
description: Use at the start of every owner request in the lead chat, and whenever an agent must delegate, brief another agent, start a production chat or workflow, report to the owner, or handle a blocked or needs-decision status. Covers sizing jobs (S/M/L), owner gates, job folders, intent briefs (what and why, never how), choosing who does the work (self, subagent, production chat, workflow), model and usage rules, tickets and escalation, the owner's decision digest, verification and lesson capture. Universal for any Roblox game made with this kit.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. Binding rules live in `rules/company.md`; this skill is how the lead applies them.

# Orchestration: running the studio

## 1. The lead's loop for every owner message

1. **Read** the message twice; note what the owner wants to see, not only what to build. Check the crew board / other chats for overlap.
2. **Size it** (`rules/company.md` §2): S, M or L. Say the size and why in one line.
3. **S:** do it yourself or give it to one agent; report the result. Stop here.
4. **M / L:** open `knowledge/jobs/<job-id>/` from `templates/jobs/`, write the **job card** and **intent brief** (§3), estimate the budget, and put them to the owner as **Gate 1**. Nothing expensive before the owner's yes.
5. After G1: pick the job owner (yourself or a production lead), the crew and the mechanism (§4). Brief each specialist with a ticket.
6. **L:** collect one cheap **first sample** per craft and show them in **one batched Gate 2 review**. Record the owner's picks and words in the decision log.
7. Full build. Specialists hand back with a status block; checkers run the measurable checks.
8. **Gate 3:** show the result (renders, clips, screenshots), with what was checked and what was not.
9. **Close:** ledger statuses final, lesson drafts in `knowledge/inbox/`, decisions in the ledger, one-paragraph report.

## 2. Talking to the owner

- Follow `rules/owner-profile.md` (plain language, one recommendation, decisions recorded with the owner's words).
- **One decision digest per turn**, not a question per agent (`templates/jobs/decision-digest.md`): item, options, recommendation, default if no answer.
- Report usage at every gate: estimate vs actual (sessions, agents, models).

## 3. Intent briefs: what and why, never how

A brief gives the specialist everything it needs to make **its own best craft choices**. Template: `templates/jobs/intent-brief.md`. Every brief has:

| Part | Content | Example (cutscene beat → animator) |
| --- | --- | --- |
| Goal and feeling | what the player must feel or understand | "The player must feel the dragon is too big to fight." |
| Context | where it sits: story beat, before/after, references (owner-approved) | "Beat 3 of 6; after the gate opens; ref: shot 4 of the approved shot list" |
| Fixed | what is not the specialist's choice: timing, camera, style locks, gameplay truth, budget | "4.0-6.5 s; low tracking camera; game art-style lock; dragon rig v2" |
| Open | what the specialist decides | "Flight path, wing timing, how it lands, any secondary motion" |
| Deliverable | files, format, where | "clip + key poses at knowledge/jobs/J07/animator/" |
| Acceptance checks | measurable pass rules | "Lands on the tower ledge mark; no foot sliding; 30 fps clip from the shot camera" |
| Status return | to whom, by when in the job | "Report to cutscene director; sample first (G2)" |

**Never** prescribe the craft ("use 3 flaps per second", "use a sine ease") unless it is a locked owner decision. If the brief cannot say *why*, it is not ready.

## 4. Who does the work

| Situation | Mechanism | Notes |
| --- | --- | --- |
| Quick lookup, one file, a question the lead can answer | **Lead itself** | cheapest |
| A side task with verbose output, or a specialist craft task | **Subagent** (named role from `.agents/roles/`) | result returns as a summary; pin the model |
| A long, independent production (L job) | **Production chat** led by a production lead | the production lead runs its own specialists as subagents; reports to the lead |
| Same step over many items, or findings that must be cross-checked | **Dynamic workflow** (saved script) | set model/effort per agent call; small slice first |
| Agents debating in a shared task list | **Agent teams: do not use** | experimental, ~7× tokens, plans auto-approved |

Parallel only when parts are **independent** (separate files, separate questions). Split by **context**, not by role: one agent per independent piece of work, not a planner → builder → tester chain (each hand-over loses detail).

## 5. Models and usage

| Work | Model · effort |
| --- | --- |
| Lead decisions, architecture, taste-critical design, risky code reviews | Opus · medium (high only for core design/wiring the owner asked for) |
| Specialist craft, building, most research | Sonnet · medium (high when needed) |
| Search, copying, moving data, formatting, templates from a spec, data entry | Haiku or Sonnet · low |

- The lead never spends high effort on mechanical work: delegate it.
- Every brief names the model and effort. Every workflow `agent()` call sets `model` and `effort`.
- Messages are pointers to files; batch updates; do not wake idle chats for FYI.
- Shut down helpers when their ticket is done.

## 6. Handling statuses

- `blocked` / `failed`: fix it if you can (missing file, unclear brief); otherwise send one level up with the reason.
- `needs-decision`: add to the owner's digest with a recommendation and a default.
- `inside: no` requests: never start them; digest them.
- Two retries, then `failed`. Three hops, then stop and report.

## 7. Verification before reporting

- Gate PASS for code; measurable checks for content (budgets, screen-size math, clip metrics, rubric with a separate grader).
- Visual work: the agent's own multi-angle review first; then the owner.
- Say exactly what was checked and what was not. Never claim the owner's approval from an agent's message.

## 8. Self-check before every report to the owner

- [ ] Size stated; gates followed for that size.
- [ ] Every owner answer recorded with the owner's words.
- [ ] Ledger statuses current; no ticket left `working` without a reason.
- [ ] Usage: estimate vs actual given at the gate.
- [ ] One digest with all open decisions; defaults stated.
- [ ] Lesson drafts written for the job's wins, failures and owner corrections.

## Read this file when
| You need | Open |
| --- | --- |
| The binding rules (roles, gates, tickets, statuses, limits) | `rules/company.md` |
| Job folder templates | `templates/jobs/` |
| The roster of agents and what each is for | `.agents/roles/README.md` |
| How the owner wants to be talked to | `rules/owner-profile.md` |
| Harness specifics (Claude subagents and chats; Codex agents) | `rules/assistants/claude.md`, `rules/assistants/codex.md` |
