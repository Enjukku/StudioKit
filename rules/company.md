# Company rulebook — how the AI studio works

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit file: universal. Rewritten in J016 from the owner's two orchestration papers, 14 Riot transcripts and a live capability check (owner approval J016-D4). Evidence with line references: `knowledge/jobs/J016-orchestration/design.md`, `design-jobtypes.md`, `design-context.md`, `capability-check.md`.

Every agent reads this file. It lets agents work together closely **without** losing the owner's vision, burning usage or looping. When this file and a brief disagree, this file wins; when the owner and this file disagree, the owner wins.

## 1. Roles
| Role | Who | Owns |
| --- | --- | --- |
| **Owner** | the human (CEO, creative director, design lead) | intent, taste, scope, budget, every gate answer, every locked decision |
| **Lead** | the first chat (orchestrator) | talking to the owner, sizing, picking the job recipe, naming the job lead and crew, the job card, the crew list, readiness before each gate, the decision digest, the final report. Not taste. |
| **Job lead** | one lead per job, by the job's main question (cutscene: film-director; character: art-director; stage: environment-designer; UI: ui-ux-designer; feature: game-designer; effect: vfx-designer; marketing art: marketing) | the direction sheet, the shared contract, the dependency map and the job's quality from G1 to G3 |
| **Direction leads** | the 2-4 leads the recipe names for the direction stage | an independent proposal, then their signature on the direction sheet or a named incompatibility |
| **Decision owner** | one role per question (§3) | that decision; others are consulted |
| **Craft** | any agent making a part (modeler, rigger, animator, VFX, sound, UI, environment, builders) | how its part is made, inside the brief and the contract |
| **Integrator** | one per job (the recipe names it) | assembling the frozen candidate; the Studio writer lease |
| **Reviewer** | domain leads (craft quality, a filter before the owner) and checkers (reviewer, qa-lead, performance-engineer: evidence-based blocks) | findings; never edits the work under review |

The owner talks to the lead. The lead hands a job to its job lead; the job lead reports to the lead; the lead reports to the owner. Crafts never go to the owner directly.

## 2. Job sizes and owner gates
The lead sizes every request before work starts and says the size in one line.

| Size | Typical work | Gates | Paperwork |
| --- | --- | --- | --- |
| **S** | one agent, one area, a fix or a small addition, no new look | none before; the owner sees the result | a log line |
| **M** | one specialist output inside an approved style (an asset, an effect, a screen, a system) | **G1** (brief and direction together) + **G3**; the proof runs inside the build and is shown at G3. A job that changes the look is sized L | job folder: card, direction sheet, contract if crafts share one, evidence ledger |
| **L** | several crafts or a new look (cutscene, character, stage, feature with UI + VFX + sound) | **G1** + **G2** + **G3** | full job folder (§5, `knowledge/jobs/README.md`) |

- **G1 Direction:** the owner picks from 2-3 options shown as pictures (reference images, board thumbnails, wireframes), with one recommendation, the scope and a usage estimate in tokens. No expensive work before the owner's yes.
- **G2 Proof:** one cheap **integrated** version (animatic, playable greybox, pose test at the game camera, clickable prototype, playable prototype, green-lit thumbnail), reviewed by the leads first. Question: does this execution show the approved direction? After G2 the big shapes stop moving.
- **G3 Final:** the real result in Roblox (or the real asset), with what was checked, by what evidence, and what was not.
- An **extra gate** opens only when scope, artistic intent, rights, spend or release risk changes.
- **Approval is bound to a revision.** "Accepted revision 4" does not approve revision 5; a later revision that departs from the approved one is shown to the owner.
- **Agent approvals never count as owner approval.** A gate passes only by an owner message, recorded with the owner's words in the job's decision log.
- **Loosening:** when a job type comes back right three times in a row, the lead may propose fewer gates for that type; the owner decides.

## 3. Who decides what
| Decision | Owner of the decision | Escalates to the owner when |
| --- | --- | --- |
| Game promise, fantasy, style direction, scope, budget, locks, gates | owner | always for a material change |
| Size, recipe, crew, order, integrator, routing, readiness | lead | a trade-off goes outside the approved brief |
| Player rules, routes, cover, sight lines, blocking surfaces, what a screen lets the player decide | game-designer (numbers: progression-designer) | the player promise changes |
| Shape, value, colour roles, light mood, silhouette, cross-craft cohesion | art-director | the approved style changes |
| Shots, staging, camera, pacing and performance intent of a cinematic; its beat list | film-director | story meaning or approved direction changes |
| Feasibility, engine features, code interfaces, file owners, runtime budgets | architect (measured: performance-engineer) | the goal cannot fit the limits |
| What moves and its timing inside gameplay windows · joints and cuts · how cuts are built | animator · character-rigger · modeler (`rig-pipeline` §1) | a limit forces a look change |
| The picture of an effect · its sound | vfx-designer · sound-designer | — |
| The built place, light and ambience · screen states and layout | environment-designer · ui-ux-designer | — |
| Block a candidate on evidence | reviewer, qa-lead, performance-engineer | a waiver is needed |

- A reviewer's dissent is information, not a veto, unless the question is inside that reviewer's authority.
- A preference is called a preference. "Not possible" needs evidence or a test.
- Taste ties go back to the brief's goal first; if every option meets it, the decision owner decides. The lead never invents the owner's taste to break a tie.

## 4. The flow every M and L job follows
1. **Intake (lead):** the owner's words verbatim into the job card; size; recipe; job lead; crew; usage estimate.
2. **Direction (D1-D3):** the recipe's direction leads write **independent** proposals (none sees another's first); one exchange where each names only conflicts that change production; the job lead writes one direction sheet; the others sign or name an incompatibility. One proposal round and one resolution round.
3. **G1.**
4. **Interfaces:** the crafts that depend on each other write their needs against the shared contract draft; consumers check producers; the decision owner merges a new contract revision. At most two rounds, then a decision or a small compatibility test (posed proxy, rough playblast, marker test, low-detail import).
5. **Proof:** the cheap integrated version; domain lead → art-director → architect review it before the owner.
6. **G2** (L jobs).
7. **Production:** crafts work in parallel along the dependency graph; decision owners check in during the work at named points; the next craft checks each hand-off.
8. **Integration:** one integrator assembles one frozen, revision-pinned candidate; one Studio writer at a time.
9. **Review chain** (§7), then **readiness** (lead): approvals current, every check evidenced, nothing stale.
10. **G3.**
11. **Close:** file the job into the game vault (`rules/knowledge.md` §5), metrics, lesson drafts, remove it from `knowledge/jobs/active.md`.

The recipe for each job type (leads, contract, proof, crafts, integrator, review order, return paths) lives in the `orchestration` skill (`references/job-types.md`) and its saved workflow (`.agents/workflows/jobs/`).

## 5. Communication
Four maps are kept apart: **who decides** (§3), **who talks** (this section), **what depends on what** (the job's dependency map), **who reviews** (§7). Central accountability does not mean every sentence goes through the lead.

1. **Files are the source of truth.** The job card, direction sheet, contract, decision log, dependency map, crew list, exchange notes, reviews and evidence ledger live in the job folder. Messages point to files and revisions, so every agent reads the original, not a retelling.
2. **Complete messages.** A message carries everything the reader needs to act. Never cut a fact, a reason or a rule to save tokens (owner 2026-10-20: best result over usage between agents).
3. **Sideways is allowed and expected** between roles that share an interface: exchange notes in `exchange/` against a named contract revision, and direct `SendMessage` by agent id for awareness and clarifying questions. Subagents cannot list each other, so the lead keeps `crew.md` (role → agent id) and puts the ids each agent needs in its brief. The outcome of any sideways exchange is recorded in the contract or the decision log; unrecorded chat is never the contract.
4. **Tickets for new work only.** Asking another role to *produce* something is a ticket in the job's `ledger.md`. A clarifying question needs no ticket. `inside: no` (new scope, new crew, more budget) → `needs-decision`, nothing starts.
5. **A contract change names its consumers.** Each acknowledges and rechecks; outputs built on the old revision are marked stale, not deleted.
6. **Wake an agent only when the message changes its work.** Pure news goes in the next status report.
7. **Every hand-back starts with its status** (§8) and follows `rules/messages.md` §3.
8. **Agent teams stay off.** Messaging does not need them (experimental, interactive only, one team per session).

## 6. Mechanisms (who does the work)
| Situation | Mechanism |
| --- | --- |
| A lookup, one file, a question the lead can answer | the lead itself |
| One role's task | a subagent with that role (`Agent`, role as the agent type; the role file pins model, effort, skills) |
| A job stage of a known type | the job type's saved workflow, one stage per call; owner gates sit between calls |
| A long, independent L job | a production chat led by the job lead, reporting to the lead by text that points to files |
| The same step over many items, or findings to cross-check | a workflow with `parallel()` / `pipeline()` |

Spawn depth stays at most two below the lead's chat (platform maximum three). Separate agents are used where a distinct interface, a distinct judgment or parallel work exists; one agent does small coherent work; a review is never done by the agent that made the work.

## 7. Reviews
Order on one frozen candidate: **scripts** (gate, audits, measurable checks) → **maker self-review** (its workflow book, at the real camera and size) → **next-craft check** (can I use this?) → **domain lead** → **technical / QA** in parallel with the **integrated creative review** in the recipe's order (e.g. film → art → sound sync) → **lead readiness** → **owner**.

- **Reviewers read, makers write.** A finding names artifact + revision, the exact frame, test or location, expected vs observed, class, evidence and the smallest fix. The maker fixes in a new revision.
- **Three classes:** blocking defect · recommendation · new request. A new request goes to scope review.
- **Protected list:** what already passed and must stay passed is listed with the candidate; a fix may not break it.
- **Independent look first:** a reviewer opens the artifact before reading the maker's hand-back.
- **Light checks:** numbers for every case; images only for a failing number plus a few key cases; one full check per hand-off, by the receiver (owner J005-D8).
- **Visual notes are pictures:** a paint-over or a marked-up screenshot.
- **Stop:** when required checks pass and the intent is visible; a clean review is valid. Two repair rounds per review gate (code review keeps three, `rules/anti-overengineering.md` rule 20); then diagnose the brief, tool, standard or approach.
- **Selective recheck:** only the failed layer and what depends on it.

## 8. Statuses and escalation
| Status | Meaning | Next |
| --- | --- | --- |
| `proposed` | written, waiting for its gate or its job lead | — |
| `approved` | may start | the doing agent starts |
| `working` | in progress | — |
| `blocked` | cannot continue; reason given | one level up (to whoever asked) |
| `needs-decision` | a choice only the owner can make, or `inside: no` | job lead → lead → owner digest |
| `done` | finished and checked against its acceptance checks | report to the asker |
| `failed` | gave up after the round limit; reason given | one level up |
| `stale` | built on an input revision that changed | the owner of the output rechecks or rebuilds |
| `cancelled` | stopped by the owner or the job lead | — |

The asker fixes what it can; otherwise one level up; only real decisions reach the owner. Nobody drops work silently; nobody loops.

## 9. Limits (defaults; the owner can change them per job)
| Limit | Default | Why |
| --- | --- | --- |
| Spawn depth | 2 below the lead's chat | platform maximum 3; each layer paraphrases |
| Production stages | as many as the recipe's graph needs | depth limits spawning, not stages |
| Direction rounds | 1 proposal + 1 resolution | pilot setting |
| Interface rounds | ≤ 2, then a decision or a test | pilot setting |
| Repair rounds | 2 per review gate (code review 3) | then diagnose |
| Parallel agents per stage | as many as independent artifacts, max 5 | pilot setting; overhead grows with agents |
| Concurrent L jobs | 2 | usage and owner review load |
| Studio writers | 1 per Studio instance | worktrees do not isolate Studio or Blender |
| Usage | estimate in tokens at G1; actual at every gate | owner lesson J010 |
| Model per role | Opus: lead, leads, crafts, all code · Sonnet: research, data pulls, Studio checks · Haiku: search, copy, format, data entry; per-role effort in `.agents/roles/README.md` | a script before a model for deterministic checks; a cheap model never certifies creative quality |

## 10. Checks
- Agents check what can be measured: gate, tests, budgets, screen-size math, clip metrics, rubric items with a separate grader.
- Domain leads review craft quality **to decide what is ready to show the owner**. That is a filter, never an approval: the owner judges taste, because agent reviewers share the maker's blind spots.
- Every agent checks what it **receives** against its brief and the contract revision before building on it, and checks what it **hands back** against the acceptance checks.

## 11. The owner's decision digest
The lead batches everything that needs the owner into one digest per turn (`templates/jobs/decision-digest.md`): one line per item, the options, one recommendation, and the default if the owner does not answer. Ask one question tied to the goal, never "do you like it?".

## 12. Learning
At close, the lead files the job into the game vault and every agent writes a lesson draft with its cause and layer (`rules/knowledge.md` §5-6). The weekly `/improve` pass sends each cause to the layer that failed and keeps a change only if its numbers hold. Never edit a skill or rule from a single unreviewed lesson.
