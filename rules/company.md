# Company rulebook — how the AI studio works

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit file: universal. Rewritten in J016 from the owner's two orchestration papers, 14 Riot transcripts and a live capability check (owner approval J016-D4). Evidence with line references: `knowledge/jobs/J016-orchestration/design.md`, `design-jobtypes.md`, `design-context.md`, `capability-check.md`. Revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3: audit findings, lead decisions LD1-LD16). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-24 (J022): images stay out of the lead's chat. Revised by orchestrator-writer · claude-opus-5-5 · default · 2026-10-24 (J023, owner G1 J023-D5; binding design `knowledge/jobs/J023-flow-speed/design.md` B-G): lighter direction, one joint needs meeting, M without a proof stage, selective recheck, less waiting. Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design, `knowledge/jobs/J024-flow-cuts-r2/design.md`): no roughs, no proof stage and no G2, direction and needs in one stage, one capture-and-scripts run, fewer reviewers. Revised by orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24 (J027): §6 lead-itself row, role sessions per craft.

Every agent reads this file. It lets agents work together closely **without** losing the owner's vision, burning usage or looping. When this file and a brief disagree, this file wins; when the owner and this file disagree, the owner wins.

## 1. Roles
| Role | Who | Owns |
| --- | --- | --- |
| **Owner** | the human (CEO, creative director, design lead) | intent, taste, scope, budget, every gate answer, every locked decision |
| **Lead** | the first chat (orchestrator) | talking to the owner, sizing, picking the job recipe, naming the job lead and crew, the job card, the crew list, readiness before each gate, the decision digest, the final report. Not taste. |
| **Job lead** | one lead per job, by the job's main question (cutscene: film-director; character: art-director; stage: environment-designer; UI: ui-ux-designer; feature: game-designer; effect: vfx-designer; marketing art: marketing) | the D1 plan (direction and the shared plan), the merge, the direction sheet, the shared contract (its Consumers table is the dependency map), the integrated review and the job's quality from G1 to G3 |
| **Needs and limits writers** | the crafts in the recipe's needs row and the constraint owners in its limits row | one needs table (crafts) or one limits table (constraint owners) against the job lead's plan revision 1 (§4 step 2). Each craft confirms the merged plan or names an incompatibility in its first build hand-back |
| **Decision owner** | one role per question (§3) | that decision; others are consulted |
| **Craft** | any agent making a part (modeler, rigger, animator, VFX, sound, UI, environment, builders) | how its part is made, inside the brief and the contract |
| **Integrator** | one per job (the recipe names it) | assembling the frozen candidate; the Studio lease (a second builder the recipe names takes it in turn) |
| **Reviewer** | the job lead's integrated review and the art-director when the rule calls it (craft quality, a filter before the owner), and checkers (reviewer, qa-lead, performance-engineer: evidence-based blocks), each only when §7 calls it | findings; never edits the work under review |

The owner talks to the lead. The lead hands a job to its job lead; the job lead reports to the lead; the lead reports to the owner. Crafts never go to the owner directly.

## 2. Job sizes and owner gates
The lead sizes every request before work starts and says the size in one line.

| Size | Typical work | Gates | Paperwork |
| --- | --- | --- | --- |
| **S** | one agent, one area, a fix or a small addition, no new look | none before; the owner sees the result | a log line |
| **M** | one output inside an approved style (an asset, an effect, a screen, a system), also when supporting crafts work inside it (an effect with its sound) | **G1** (one direction inside the approved style, with the agreed plan) + **G3**. A job that changes the look is sized L | job folder: card, `decisions.md`, `crew.md` (hand-run stages), direction sheet, needs tables, contract if crafts share one, evidence ledger |
| **L** | a new look, or several crafts that each produce separate outputs (cutscene, character, stage, a feature with UI + VFX + sound) | **G1** (2-3 options at equal finish, pictured, with the agreed plan; may set a new look) + **G3** | full job folder (§5, `knowledge/jobs/README.md`) |

Every M and L job runs `direction` → G1 → `build` → G3 (J024). L and M differ only in direction; the build stage is the same for both sizes.

- **G1 Direction:** the owner sees the direction and the agreed plan together (§4 step 2). L: the owner picks from 2-3 options (a recipe may set another count: marketing art shows 3-5 thumbnails) shown as pictures (reference images, wireframes; a feature shows the behaviour in player words, with pictures where the contract has visible parts); M: one direction. With one recommendation, the scope and a usage estimate in tokens. No expensive work before the owner's yes; after the yes, `build` starts at once.
- **G2 Proof:** removed in J024 (owner J023-D6, D7: no roughs). No job type has a proof stage or G2; the owner first sees built work at G3.
- **G3 Final:** the real result in Roblox (or the real asset), with what was checked, by what evidence, and what was not.
- An **extra gate** opens only when scope, artistic intent, rights, spend or release risk changes.
- **Approval is bound to a revision.** "Accepted revision 4" does not approve revision 5; a later revision that departs from the approved one is shown to the owner.
- **Agent approvals never count as owner approval.** A gate passes only by an owner message, recorded with the owner's words in the job's decision log.
- **Loosening:** when a job type comes back right three times in a row, the lead may propose fewer gates for that type; the owner decides. Each job's `evidence.md` §4 records whether it came back right (first-pass acceptance at each gate); the lead counts the last jobs of the type from those rows.

## 3. Who decides what
| Decision | Owner of the decision | Must consult | Escalates to the owner when |
| --- | --- | --- | --- |
| Game promise, fantasy, style direction, scope, budget, locks, gates | owner | lead, relevant leads | always for a material change |
| Size, recipe, crew, order, integrator, routing, readiness | lead | job lead | a trade-off goes outside the approved brief |
| Player rules, routes, cover, sight lines, blocking surfaces, what a screen lets the player decide | game-designer (numbers: progression-designer) | architect, art-director | the player promise changes |
| Shape, value, colour roles, light mood, silhouette, cross-craft cohesion | art-director | game-designer, film-director | the approved style changes |
| Shots, staging, camera, pacing and performance intent of a cinematic; its beat list | film-director | art-director, animator, vfx-designer, sound-designer | story meaning or approved direction changes |
| Feasibility, engine features, code interfaces, file owners, runtime budgets | architect (measured: performance-engineer) | builders, crafts | the goal cannot fit the limits |
| What moves and its timing inside gameplay windows · joints and cuts · how cuts are built | animator · character-rigger · modeler (`rig-pipeline` §1) | each other; animator also game-designer; modeler also art-director | a limit forces a look change |
| The picture of an effect · its sound | vfx-designer · sound-designer | each other; vfx also animator; sound also environment-designer | — |
| The built place, light and ambience · screen states and layout | environment-designer · ui-ux-designer | game-designer (routes are theirs), art-director | — |
| Block a candidate on evidence | reviewer, qa-lead, performance-engineer | maker | a waiver is needed |

- A reviewer's dissent is information, not a veto, unless the question is inside that reviewer's authority.
- A preference is called a preference. "Not possible" needs evidence or a test.
- Taste ties go back to the brief's goal first; if every option meets it, the decision owner decides. The lead never invents the owner's taste to break a tie.

## 4. The flow every M and L job follows
1. **Intake (lead):** the owner's words verbatim into the job card; size; recipe (one job per recipe when a request spans two); job lead; crew; usage estimate; the recipe's prerequisites for this game checked, and a missing one run first as its own job or gate (`orchestration` skill §3).
2. **Direction (direction and craft needs in one stage, J024):**
   - **D1 plan (one run, the job lead):** the direction (L: 2-3 options with their image prompt rows; M: one direction inside the approved style) **and** the shared plan draft, revision 1 (the recipe's plan: beat sheet, character sheet, blueprint, screen contract, feature contract, effect timeline, asset kit), written to hold for every option; where a row depends on the option, it says so.
   - **N1 needs and limits (in parallel, one run each):** every craft in the recipe's needs row writes one **needs table** against plan revision 1; every constraint owner in its limits row writes one **limits table** (format: `rules/messages.md` §4, `templates/jobs/needs-table.md`). Each writer reads **only the plan file and its own brief**, never another craft's table or a lead's proposal. When the job has code, the architect's limits table names the code file owners (`owns` per builder).
   - **Merge (one run, the job lead):** reads the plan and every table, settles each conflict it owns, and writes `direction.md` (every conflict with its owner and resolution) and plan revision 2, the merged contract (code file owners in its header), with the G1 packet rows. Its hand-back names the conditional crafts the plan needs (the recipe's "only if the plan lists" crafts).
   - **N2 (only on a conflict the job lead cannot settle alone):** only the crafts in that conflict, each given only the conflicting rows, answer once; then a second merge. Never more than these two needs rounds; then a decision or a small test.
   - No sign-off runs. Each craft confirms the merged plan or names an incompatibility in its first build hand-back; an incompatibility is a `needs-decision` to the lead. Build never re-asks a craft for timings, cue ids, joint lists or materials: a need found later is a contract change (`rules/messages.md` §5).
3. **G1:** the direction and the agreed plan together. After the owner's yes, `build` starts at once.
4. **Joint needs meeting:** removed in J024; the needs step is part of direction (step 2, N1 and the merge), before G1.
5. **Proof:** removed in J024 (no roughs, owner J023-D6, D7). No job type has a proof stage.
6. **G2:** removed in J024 (§2).
7. **Production:** each craft builds its real, polished part **once, in one run**, on the merged plan, in the plan's dependency order (marker producers before consumers: animator → VFX → sound; modeler → rigger → animator; UI design → builder). Independent crafts run in parallel. Nobody hands a rough to another agent: rough, temp, prototype, blockout, greybox, proxy, board and first-spec passes are not steps, and no run waits on a rough or reviews one. A craft may rough things out **inside its own run** (its own blockout, proxy pose, quick probe). A check that caught real problems moves into the maker's run as a measured self-check (examples: the rigger's posed-proxy clearances, J005; the film-director's 4:3-centre read, J015), and the integrated review measures it again on the final captures. The next craft checks each hand-off it receives. A craft's part splits into one run per piece only when one run would pass the agent size (`rules/assistants/claude.md`, Session size).
8. **Integration:** one integrator assembles one frozen, revision-pinned candidate; one Studio driver at a time (§9).
9. **Capture and scripts, then the review chain** (§7), then **readiness** (lead): approvals current, every check evidenced, nothing stale.
10. **G3.**
11. **Close:** file the job into the game vault (`rules/knowledge.md` §7), metrics, lesson drafts, remove it from `knowledge/jobs/active.md`.

**Less waiting (lead):** at the start of each stage the lead asks all of that stage's owner questions in one digest (§11), each with a default; the stage's image batches go to the owner as one batch; after a gate answer the lead starts the next stage in the same turn, from a fresh session when the chat is past the session size (`rules/assistants/claude.md`).

The recipe for each job type (D1 plan, needs and limits writers, build crafts, integrator, review order, conditional crafts, return paths) lives in the `orchestration` skill (`references/job-types.md`) and its saved workflow (`.agents/workflows/jobs/`).

## 5. Communication
Four maps are kept apart: **who decides** (§3), **who talks** (this section), **what depends on what** (the dependency map: the Consumers table of each contract header, no separate file), **who reviews** (§7). Central accountability does not mean every sentence goes through the lead.

1. **Files are the source of truth.** The job card, direction sheet, contracts, decision log, crew list, exchange notes, reviews and evidence ledger live in the job folder. Messages point to files and revisions, so every agent reads the original, not a retelling.
2. **Complete messages.** A message carries everything the reader needs to act. Never cut a fact, a reason or a rule to save tokens (owner 2026-10-20: best result over usage between agents).
3. **Sideways is allowed and expected** between roles that share an interface: exchange notes in `exchange/` against a named contract revision, and direct `SendMessage` by agent id for awareness and clarifying questions. The outcome of any sideways exchange is recorded in the contract or the decision log; unrecorded chat is never the contract.
   - **Who can send.** Only a role whose `tools:` list names `SendMessage` (or has no `tools:` list) can send a direct message (capability check C22). The other roles write exchange notes. When a producer cannot message a consumer, the lead relays the contract-change notice (`rules/messages.md` §5). Receiving a message, and being resumed by one, needs no tool. Tool lists are agent permissions: only the owner changes them.
   - **Ids.** Subagents cannot list each other. For agents the lead (or a production chat) spawns by hand, the lead keeps `crew.md` (role → agent id), puts the ids each agent needs in its brief's `peers`, and resumes a maker by id for a repair.
   - **Inside a saved workflow** there are no agent ids. Sideways work goes through files in a fixed order: the producer writes, the consumer reads and answers, the producer merges. Never "read the other's note if it exists" inside one parallel step. A repair is a fresh call with the finding files and the protected list.
4. **Tickets for new work only.** Asking another role to *produce* something is a ticket in the job's `ledger.md`. A clarifying question needs no ticket. `inside: no` (new scope, new crew, more budget) → `needs-decision`, nothing starts.
5. **A contract change names its consumers.** Each acknowledges and rechecks; outputs built on the old revision are marked stale, not deleted.
6. **Wake an agent only when the message changes its work.** Pure news goes in the next status report.
7. **Every hand-back starts with its STATUS line** (§8) and follows `rules/messages.md` §3.
8. **Agent teams stay off.** Messaging does not need them (experimental, interactive only, one team per session).

## 6. Mechanisms (who does the work)
| Situation | Mechanism |
| --- | --- |
| A lookup, an answer, one exact value the owner or an approved spec gives, merges, records, starting and messaging agents and sessions | the lead itself; never a craft deliverable (craft owners: `orchestration` §2, J027) |
| One role's task (one run) | a subagent with that role (`Agent`, role as the agent type; the role file pins model, effort, skills) |
| Continuing build work for one craft (a game build step, its follow-ups) | one session per craft role in the game (owner J027-D2, kit-wide form of a game's "run it in separate chats" rule): the lead starts it with `templates/role-session-brief.md` and sends that craft's later asks to it; the game's roadmap names it (`knowledge/design/roadmap.md`; `orchestration` `references/job-types.md`, Not recipes) |
| A job stage of a known type | the job type's saved workflow, one stage per call; owner gates sit between calls |
| A long, independent L job | a production chat led by the job lead, reporting to the lead by text that points to files |
| The same step over many items, or findings to cross-check | a workflow with `parallel()` / `pipeline()` |

Spawn depth stays at most two below the lead's chat (platform maximum three). **In a hand-run stage the lead's chat spawns every craft** (depth 1; scouts at depth 2). A subagent job lead directs through `direction.md`, the contract and briefs it drafts for the lead to send. A job lead spawns crafts only when it is the main chat of a production chat. Agents inside a saved workflow spawn no scouts. Separate agents are used where a distinct interface, a distinct judgment or parallel work exists; one agent does small coherent work; a review is never done by the agent that made the work.

## 7. Reviews
Order on one frozen candidate: **maker self-review** (in its own run, its workflow book, at the real camera and size, with its measured self-checks) → **next-craft check** (can I use this?, in the consumer's own build run) → **capture and scripts** (one `studio-operator` run: imports or plays the candidate, runs the gate and the type's measuring scripts, captures key frames, reads the Output-log cue times; its hand-back adds `visual_flags` and `cue_log`) → the reviewers below → **lead readiness** → **owner**.

| Reviewer | When |
| --- | --- |
| capture and scripts | always; a scripts FAIL stops the other reviews until it is fixed |
| **job lead, integrated review** on the captures | always: it measures key frames itself (`look_check.py` at the game camera and phone size), checks the gameplay read, and checks sound sync from `cue_log` against the marker list |
| `reviewer` (code review) | when the candidate changed code (a code-owning maker's files) |
| `qa-lead` | player-facing logic only: skip and endings, shop and purchase flows, saves, server results, multiplayer (the recipe says which) |
| `performance-engineer` | when `risks` names `performance` |
| `art-director` | with a new look (`newLook: true`, marketing `launch: true`), or when `visual_flags` is not empty |
| risk-gated slots, the live-ops `event` review | as the recipe's *(risk: …)* rows say |

The sound-designer, game-designer, progression-designer, architect, VFX designer, animator and feature-builder are not reviewers, except as a type's job lead (J024). Listening stays an owner-confirmed line at G3.

- **Code is reviewed.** Every job whose candidate includes code (player code, wiring, remotes, saves) has the `reviewer` role (`code-review` skill, plus the area skills of `AGENTS.md` §2) in its review chain before readiness.
- **Reviewers read, makers write.** A finding names artifact + revision, the exact frame, test or location, expected vs observed, class, evidence and the smallest fix. The maker fixes in a new revision. Repair briefs are capped (`rules/messages.md` §6): own findings, the parts changed since, the protected list.
- **Three classes:** blocking defect · recommendation · new request. A new request goes to scope review.
- **Protected list:** what already passed and must stay passed is listed with the candidate; a fix may not break it.
- **Independent look first:** a reviewer opens the artifact before reading the maker's hand-back.
- **Light checks:** numbers for every case; images only for a failing number plus a few key cases; one full check per hand-off, by the receiver; the full image set once, at release (owner J005-D8). Images reach the lead's chat only for a gate packet or a failing number; makers and helpers view captures and hand back numbers and paths (J022).
- **Visual notes are pictures:** a paint-over or a marked-up screenshot.
- **Stop:** when required checks pass and the intent is visible; a clean review is valid. Two repair rounds per review gate (code review keeps three, `rules/anti-overengineering.md` rule 20). After the limit the stage returns `needs-decision` to the lead. The lead diagnoses the cause (brief, tool, standard or approach) and fixes what is its to fix; only a diagnosis that needs scope, taste or budget goes into the owner's digest.
- **Selective recheck:** only the failed layer and what depends on it. Round 0 of a review chain runs in full. In every later round, after a repair:
  1. Always run: the capture-and-scripts run (gate, scripts, fresh capture), the qa-lead protected suite where the chain has a qa-lead, and the `reviewer` when the repair changed any code-owning maker's files.
  2. Run every reviewer that raised a blocking finding in the previous round.
  3. Run a reviewer whose area depends on a repaired layer: the job lead's integrated review when any visual or timing maker repaired; the art-director when any visual maker repaired, only when it is in the chain. Each saved workflow states its dependency map in one table near its review chain.
  4. Every other reviewer keeps its previous verdict; the stage result lists it as `carried: <reviewer> (round n, revision r)`.
  5. The repair-round limits stay (above); a dead or empty review is never a pass.

## 8. Statuses and escalation
| Status | Meaning | Next |
| --- | --- | --- |
| `proposed` | written, waiting for its gate or its job lead | — |
| `approved` | may start | the doing agent starts |
| `working` | in progress | — |
| `blocked` | cannot continue; reason given | one level up (to whoever asked) |
| `needs-decision` | a choice the agent may not make: an owner choice, `inside: no`, or the repair round limit reached (§7) | job lead → lead; the lead decides what is its own (§3) and puts only scope, taste or budget in the owner digest |
| `done` | finished and checked against its acceptance checks | report to the asker |
| `failed` | gave up: two pushes on open coverage items (`rules/messages.md` §3), or the work cannot be done; reason given | one level up |
| `stale` | built on an input revision that changed | the owner of the output rechecks or rebuilds |
| `cancelled` | stopped by the owner or the job lead | — |

The asker fixes what it can; otherwise one level up; only real decisions reach the owner. Nobody drops work silently; nobody loops.

## 9. Limits (defaults; the owner can change them per job)
| Limit | Default | Why |
| --- | --- | --- |
| Spawn depth | 2 below the lead's chat | platform maximum 3; each layer paraphrases |
| Production stages | as many as the recipe's graph needs | depth limits spawning, not stages |
| Direction rounds | D1 plan (one run), N1 needs and limits tables (one run per writer, in parallel), one merge; no sign-off run (§4 step 2) | J023-D5; J024 design §3 |
| Interface (needs) rounds | ≤ 2 inside direction: N1, and N2 only on a conflict the job lead cannot settle (only those crafts, only the conflicting rows); then a decision or a test. Build never re-asks (§4 step 2) | J023-D2, D5; J024 design §3 |
| Repair rounds | 2 per review gate (code review 3) | then `needs-decision` to the lead, who diagnoses (§7) |
| Parallel agents per stage | as many as independent artifacts, max 5 | pilot setting; overhead grows with agents |
| Concurrent L jobs | 2 | usage and owner review load |
| Studio drivers (read or write) | 1 at a time per Studio instance; a recipe's second Studio user takes its turn after the first returns. In a hand-run stage the lead names the driver and its `studio_id` in each Studio brief | owner profile: Studio work is sequential; worktrees do not isolate Studio or Blender |
| Blender, Claude in Chrome | 1 agent at a time each | one scene and one ChatGPT session are shared |
| Usage | estimate in tokens at G1; actual at every gate | owner lesson J010 |
| Model per role | Opus: lead, leads, crafts, all code · Sonnet: research, data pulls, Studio checks (captures, screenshots, Studio probes and the type's measuring scripts run by the studio-operator, one capture-and-scripts run per review round; the role that needs one names it in its hand-back; Opus roles never take routine captures) · Haiku: search, copy, format, data entry; per-role effort in `.agents/roles/README.md` | a script before a model for deterministic checks; a cheap model never certifies creative quality |

## 10. Checks
- Agents check what can be measured: gate, tests, budgets, screen-size math, clip metrics, rubric items with a separate grader.
- The job lead's integrated review (and the art-director when §7 calls it) judges craft quality **to decide what is ready to show the owner**. That is a filter, never an approval: the owner judges taste, because agent reviewers share the maker's blind spots.
- Every agent checks what it **receives** against its brief and the contract revision before building on it, and checks what it **hands back** against the acceptance checks.
- **Workflow books.** Each role's book (role file + design skill + craft skill + references) has the 10 items of the workflow-book checklist near the top (`templates/role.md`; source: J016 `design.md` §10): mission and great work, inputs and stop conditions, reference images first, numbered steps with collaboration points, Roblox docs rows with the date checked, file conventions, self-review with examples, evidence and hand-off, tool limits and escalation, lessons in the step they fix. `/build-agent` and `/improve` check a book against it.

## 11. The owner's decision digest
The lead batches everything that needs the owner into one digest per turn (`templates/jobs/decision-digest.md`): one line per item, the options, one recommendation, and the default if the owner does not answer. Ask one question tied to the goal, never "do you like it?".

## 12. Learning
Every hand-back may carry a `lesson` (`rules/messages.md` §3). At each gate answer and at close, the lead writes the inbox drafts from them, with the owner's words, and its own; at close it files the job into the game vault (`rules/knowledge.md` §7-8). The weekly `/improve` pass sends each cause to the layer that failed and keeps a change only if its numbers hold. Never edit a skill or rule from a single unreviewed lesson.
