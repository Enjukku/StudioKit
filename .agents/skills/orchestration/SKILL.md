---
name: orchestration
description: The lead's playbook for running the AI studio. Use at the start of every owner request, and whenever an agent must size a job, pick a job recipe, run leads' direction, gates, sideways exchange, reviews, a job workflow stage, briefs, statuses, the owner digest or job close-out.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; rewritten in J016 (owner approval J016-D4, 2026-10-21). Kit skill: universal. Binding rules: `rules/company.md` (flow, roles, gates, limits), `rules/messages.md` (formats), `rules/knowledge.md` (context). Evidence: `knowledge/jobs/J016-orchestration/`.

# Orchestration: running the studio

## 1. The lead's loop for every owner message
1. **Read** the message twice: what the owner wants to see and feel, not only what to build. Check `knowledge/jobs/active.md`, other chats and `git status` for overlap.
2. **Size it** (`rules/company.md` §2): S, M or L, with one line of why. **Pick the recipe** (§2 below).
3. **S:** do it yourself or give it to one role; self-review + one domain check; report. Stop here.
4. **M / L: open the job** (§3), then run the stages in order. Each stage is one call of the job type's saved workflow (`/job-<type>`, args `{job, stage}`) or the same steps by hand with subagents:
   `direction` → **G1** → `proof` → **G2** (L only) → `build` → **G3** → close. M jobs: `direction` → G1 → `build` (the proof runs inside `build`) → G3.
5. **Between stages:** read every hand-back's `coverage` against the files, record the owner's words, update `crew.md` and `active.md`, then start the next stage with the gate decision as input. A workflow cannot pause for the owner: never start the next stage before the gate answer.
6. **G3 change request:** stage `repair` reopens only the affected crafts and rechecks only what depends on them.
7. **Close** (§9).

## 2. Recipes (job type → job lead, saved workflow, details)
| Type | Job lead | Workflow | Recipe |
| --- | --- | --- | --- |
| Cutscene (story scene, boss intro, reveal, ending, camera moment) | film-director | `job-cutscene` | `references/job-types.md` §1 |
| Character or creature (variant mode for skins and recolours) | art-director | `job-character` | §2 |
| Stage (level, hub, arena, world area) | environment-designer | `job-stage` | §3 |
| UI screen | ui-ux-designer | `job-ui-screen` | §4 |
| Gameplay feature | game-designer (technical lead: architect) | `job-feature` | §5 |
| Effect (hit, pickup, reveal, telegraph, with its sound) | vfx-designer | `job-effect` | §6 |
| Marketing art (icon, thumbnails, key art family) | marketing | `job-marketing-art` | §7 |
| New game pre-production | game-designer | none: `preproduction` skill, one owner decision per step | — |
| Live update or event | live-ops-designer plans; the lead splits it into jobs of the types above | none | — |
| Mixed or unclear | the lead picks the closest type and says why in the job card | — | — |

A role that is still planned (the animator, J006) runs as a stand-in: a general subagent on Opus high with that role's brief and the skills it would load (same pattern as J005-D2).

## 3. Opening a job (M and L)
1. Re-list `knowledge/jobs/` right before creating the folder (parallel chats take numbers). Copy `templates/jobs/`.
2. **Job card:** the owner's words verbatim first, then size, type, job lead, direction leads, crew, mechanism, usage estimate **in tokens**, acceptance checks, gates.
3. Add the job to `knowledge/jobs/active.md`. Start `crew.md` (role → agent id, filled as agents start).
4. Brief the direction leads (§4). Every brief carries the packet line `--role <role> --job <job-id>`.

## 4. Direction stage (the right leads agree before crafts start)
1. **D1 independent proposals, in parallel:** each direction lead gets the same job card, references and constraints, and **not** the others' proposals. Each returns: 2-3 reference images or rough options, the intended player experience, non-negotiables, uncertain assumptions, limits it knows (rig cost, sound time, tech risk, budget).
2. **D2 one exchange:** each lead reads the others' files and lists **only conflicts that would change production** (exchange notes, `rules/messages.md` §4).
3. **D3 synthesis:** the job lead writes `direction.md` (`templates/jobs/direction-sheet.md`) with a decision record per consequential question (question, options, decision owner, evidence, affected assets, dissent, revisit trigger). Each other lead signs its part or names an incompatibility.
4. Unresolved taste or a material trade-off → the owner digest with pictures. A tie is not by itself a reason to ask the owner; the decision owner decides inside the brief.
5. **G1 packet** (§8).

## 5. Interfaces and proof
1. The job lead drafts the **contract** (beat list + shot list, rig sheet, route graph + blueprint, state map + spec, feature contract, event timeline: per recipe) with stable ids and a revision.
2. Crafts that depend on each other write needs against it; consumers check producers; the decision owner merges the next revision. ≤ 2 rounds; then a decision or a small test.
3. The proof: only the crafts it needs. Domain lead → art-director → architect review it before the owner (`rules/company.md` §7).
4. **G2 packet** (§8). After G2 the big shapes stop moving.

## 6. Production, sideways work and contract changes
- Crafts work in parallel along the dependency map. Give each brief the `peers` ids it needs from `crew.md`; subagents cannot list each other.
- Decision owners check in at the recipe's named points (e.g. film reviews blocking before polish; the game-designer checks the stage build as it grows). Visual notes are paint-overs.
- A contract change: new revision, change table row, a notice to each consumer (`rules/messages.md` §5), stale outputs marked. On Claude Code 2.1.306 a message reaches a working agent at its next tool step; a message to a finished agent resumes it with its context.
- Repairs go back to the maker (resume it by id) with the finding file; the protected list travels with the repair.
- One Studio writer at a time; name the `studio_id` in every Studio brief.

## 7. Integration, review chain, readiness
1. The recipe's integrator assembles one frozen, revision-pinned candidate.
2. Scripts first; then the recipe's review order (`references/job-types.md`), technical checks in parallel with the creative order. Reviewers open the artifact before the maker's hand-back; findings follow `rules/messages.md` §6.
3. Two repair rounds per review gate, then diagnose (brief, tool, standard or approach) instead of "try harder".
4. **Readiness (lead):** every acceptance check has evidence at the candidate's revision; approvals are current; no stale input; open limits listed. Look at key frames or captures yourself, not only the reviews (J015 lesson).

## 8. Talking to the owner and gate packets
- Follow `rules/owner-profile.md` and `ste-writing`. **One decision digest per turn** (`templates/jobs/decision-digest.md`). Ask one question tied to the goal, never "do you like it?".
- **Gate packet, one screen:** the artifact first (pictures, capture, playable); the decision in one sentence; the recommendation and one real alternative; the trade-off in player terms; what changed since the last approval; what was checked, by what evidence, and what was not; usage estimate vs actual.
- Record the answer with the owner's words **and the revision it approves** in the job's `decisions.md`. Never show a polished picture as if it were the in-game result.

## 9. Close: file the job into the vault
Give a doc-keeper (Haiku or Sonnet) the list; check its result.
1. Owner decisions → `knowledge/design/decisions.md` with a revisit trigger.
2. Accepted artifacts → `knowledge/design/precedents.md` (what, why accepted, owner's words, path@revision).
3. New names (states, events, cues, assets) → `knowledge/design/vocabulary.md`.
4. Finished systems → `knowledge/systems/<system>.md` with a contract card + index row.
5. Rejected options → `tried-and-failed.md` with a retry condition. Owner corrections → `taste-log.md`, word for word.
6. New reusable assets → their catalog.
7. Job metrics in `evidence.md`: first-pass acceptance, repair rounds by cause, defects the owner found after internal review, stale handoffs, unsupported "done" claims, usage vs estimate, owner decisions.
8. Lesson drafts with `cause` and `layer` from every agent; remove the job from `active.md`; final ledger statuses; a short retrospective line: what more iteration would fix.

## 10. Briefs: what and why, never how
A brief gives the receiver everything it needs to make **its own best craft choices**, in the `rules/messages.md` §2 format: `<intent>` prose (goal, feeling, context, why), then `<spec>` with `packet`, `owner_words`, `refs` with notes, `inputs@rev`, `fixed` (each value with its source), `open`, `avoid`, `protected`, `consumers`, `peers`, `owns`, `not_in_scope`, every `rule`, `deliver`, `checks`, `return`. Send it whole, in one message.
- **Exact where another system, craft or the owner depends on the value; open where the role is the expert.** A feeling is a target plus an observable sign, never a method. Never prescribe craft ("use 3 flaps per second") unless it is a locked owner decision. If the brief cannot say *why*, it is not ready.
- **Every brief names the Roblox docs** the work touches: the packet's "Roblox docs" section and the receiver's rows in `knowledge/reference/roblox/docs-map.md` (a brief without docs pointers led to invented class names and a rebuilt lighting system: `knowledge/reference/engineering/rework-study.md` B08).
- **Code briefs** also state the files owned, the public interface to keep, invariants, allowed dependencies and non-goals; the briefer writes the acceptance checks, including failure cases. One runnable check per rule, never "double-check everything".
- Set effort before adding prompt text (Opus medium default, high for hard work, xhigh only for measured gains). Put `fixed`, non-goals and scope at the **end**, next to the task.
- Direction briefs never include another lead's proposal; review briefs point to the artifact before the maker's hand-back.

## 11. Models and usage
Per-role defaults: `.agents/roles/README.md` (owner-approved). Helpers without a role file:

| Work | Model · effort |
| --- | --- |
| Lead decisions, direction, architecture, risky code review (money, saves, remotes) | Opus · high |
| Game code, scripts, tools | Opus · medium (high for money, saves, remotes) |
| Craft and creative judgment, integrated reviews | Opus · per role table |
| Reading docs into fact sheets; data pulls; Studio checks | Sonnet · medium |
| Search, copying, formatting, filing, data entry | Haiku · low (medium if the job ends with a check) |

- A script before a model for any deterministic check. A cheap model never certifies creative quality or safety.
- Every brief and every workflow `agent()` call names the role (`agentType`), model and effort.
- Report usage at every gate: estimate vs actual, in tokens.

## 12. Statuses
- `blocked` / `failed`: fix it if you can (missing file, unclear brief); otherwise send it one level up with the reason.
- `needs-decision`: into the owner digest with a recommendation and a default. `inside: no` requests: never start them; digest them.
- `stale`: the output's owner rechecks or rebuilds against the new revision.
- Two pushes on open coverage items, then `failed`. Two repair rounds per review gate, then diagnose.

## 13. Verification before reporting
- Gate PASS for code; measurable checks for content (budgets, screen-size math, clip metrics, `look_check.py`, `thumb_check.py`); reviews in the recipe's order.
- **Read each hand-back's `coverage` against the files, not the summary.** A missing item or a `pass` without evidence goes back with one line naming it.
- Say exactly what was checked and what was not, with its label: gate-verified, MCP-verified, owner-confirmed, not verified. Never claim the owner's approval from an agent's message.

## 14. Self-check before every report to the owner
- [ ] Size and recipe stated; gates followed for that size; no stage started before its gate answer.
- [ ] Every owner answer recorded with the owner's words and the approved revision.
- [ ] `active.md`, `crew.md`, ledger statuses current; no ticket left `working` without a reason.
- [ ] Usage: estimate vs actual in tokens.
- [ ] One digest with all open decisions; defaults stated.
- [ ] Every brief this job: every rule stated, skills named, `fixed` values sourced, inputs with revisions (`rules/messages.md` §9).
- [ ] At close: the job filed into the vault (§9) and lesson drafts written with cause and layer.

## Read this file when
| You need | Open |
| --- | --- |
| The recipe for a job type (leads, contract, proof, crafts, integrator, review order, return paths) | `references/job-types.md` |
| The binding rules (roles, gates, decisions, limits, reviews, statuses) | `rules/company.md` |
| Brief, exchange, review and hand-back formats | `rules/messages.md` |
| How context is layered, routed, passed and learned | `rules/knowledge.md` |
| Job folder templates | `templates/jobs/` |
| The roster and per-role effort | `.agents/roles/README.md` |
| How the owner wants to be talked to | `rules/owner-profile.md` |
| Claude Code and Codex specifics | `rules/assistants/claude.md`, `rules/assistants/codex.md` |
| The evidence behind this design | `knowledge/jobs/J016-orchestration/design.md` |

Project overlay: if `knowledge/overlays/orchestration.md` exists, read it after this file; it wins for this game.
