# Company rulebook — how the AI studio works

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit file: universal. Evidence base: Claude Code docs (agents, sub-agents, agent-teams, costs, projects, memory; read 2026-10-20 at v2.1.296), arXiv 2608.16801 (2026-08-17), DevelopersDigest HITL patterns (2026-10-17), arXiv 2608.28122 (2026-08-28). Research notes: `knowledge/reference/studio/orchestration-research-2026-10.md`.

Every agent reads this file. It exists so that agents can call each other freely **without** losing the owner's vision, burning usage, or looping. When this file and a brief disagree, this file wins; when the owner and this file disagree, the owner wins.

## 1. Roles

| Role | Who | Owns |
| --- | --- | --- |
| **Owner** | the human | Creative direction, taste, every gate answer, every locked decision |
| **Lead** | the first chat (orchestrator) | Talking to the owner, sizing jobs, routing, briefs, merging, the decision digest, final report |
| **Job owner** | the lead, or a production lead the lead appoints (e.g. cutscene director, art director) | One job from brief to final gate: its crew, ledger, budget and quality |
| **Specialist** | any agent doing craft work (modeler, animator, VFX, sound, UI, builder...) | How its part is made, inside the brief |
| **Checker** | reviewer, QA, verifier agents | Measurable checks against stated pass rules; never taste |

The owner talks to the lead. Production leads report to the lead; the lead reports to the owner. Specialists never go to the owner directly.

## 2. Job sizes and owner gates

The lead sizes every request before work starts and says the size in one line.

| Size | Typical work | Gates (owner) | Paperwork |
| --- | --- | --- | --- |
| **S** | One agent, one area, a fix or a small addition, no new look | none before; the owner sees the result | none (a log line) |
| **M** | One specialist output (an asset, an effect, a screen, a system) | **G1 brief** + **G3 final** | job card + brief |
| **L** | Several crafts or a new look (character, cutscene, stage, feature with UI + VFX + sound) | **G1 brief** + **G2 first samples** + **G3 final** | full job folder |

- **G1 brief:** the job card and intent brief (goal and feeling, references, scope in/out, crew, models, budget, what is fixed vs open, acceptance checks). No expensive work before the owner's yes.
- **G2 first samples:** each craft makes **one cheap sample that sets direction** (modeler: silhouette or blockout render; animator: key poses or one clip; VFX: frame script + one capture; sound: 2-3 candidate cues; UI: one screen; cutscene: shot list). The owner reviews all samples in **one batched review**, picks and comments. Only then the full build.
- **G3 final look:** before anything goes into the game.
- **Agent approvals never count as owner approval** (Claude Code agent-team plan approval is automatic and unreviewed). A gate is passed only by an owner message, recorded with the owner's words in the job's decision log.
- **Loosening:** when a job type has come back right three times in a row, the lead may propose dropping G2 for that type; the owner decides (ledger row).

## 3. Tickets: how agents call each other

Any agent may ask any other agent for work **inside an approved brief**. Every request is a ticket in the job's `ledger.md`:

| Field | Meaning |
| --- | --- |
| `id` | `<job-id>-T<nn>` |
| `from` → `to` | requesting agent → doing agent |
| `ask` | pointer to the brief section or a 1-3 line intent brief (what and why, never how) |
| `inside` | `yes` = same scope, crew and budget as the approved brief; `no` = new scope, new crew or more budget |
| `status` | see §5 |
| `hops` | how many agents this request chain has passed through |
| `result` | pointer to the output file(s) |

- `inside: yes` → the doing agent starts.
- `inside: no` → status `needs-decision`; it goes up to the job owner, then into the owner's decision digest. Nothing starts.
- The doing agent reports **to whoever asked**, never sideways.
- Duplicate asks are merged into one ticket.

## 4. Communication rules (usage and quality)

1. **Shared files, short messages.** Briefs, beat sheets, results and decisions live in the job folder. A message says "done, see file X", asks one question, or reports a status. Never paste large content into messages (arXiv 2608.16801: shared files cut output tokens ~42% at 8 agents).
2. **Hub and spoke by default.** A job owner runs specialists as subagents (results come back as summaries). Separate chats only for long, independent productions. Agent teams stay off (experimental, ~7× tokens, plans auto-approved).
3. **Do not wake idle chats for small things.** Every message to an idle chat re-sends its whole context. Batch updates into the next status report.
4. **Briefs are complete.** A new agent does not see the asker's conversation; the brief and the files it points to must be enough.
5. **Every hand-back ends with a status block** (§5): status, what was done, files, open questions, the default you will take if nobody answers.

## 5. Statuses and escalation

| Status | Meaning | Next |
| --- | --- | --- |
| `proposed` | written, waiting for its gate or its job owner | — |
| `approved` | may start | doing agent starts |
| `working` | in progress | — |
| `blocked` | cannot continue; reason given | goes **one level up** (to whoever asked) |
| `needs-decision` | a choice only the owner can make, or `inside: no` | job owner → lead → owner digest |
| `done` | finished, checked against its acceptance checks | report to asker |
| `failed` | gave up after the retry limit; reason given | one level up |
| `cancelled` | stopped by the owner or job owner | — |

Escalation: the asker fixes it if it can; otherwise one level up; only real decisions reach the owner. Nobody silently drops work; nobody loops.

## 6. Limits (defaults; the owner can change them per job)

| Limit | Default | Why |
| --- | --- | --- |
| Concurrent specialists per job | 3 | team sizes of 3-5 recommended; 3 focused beat 5 scattered (Claude Code agent-teams docs) |
| Concurrent L jobs | 2 | usage and owner review load |
| Request chain hops | 3 | stops ping-pong; platform nesting limit is 3 levels |
| Retries per task | 2 | then `failed` with a reason |
| Budget | estimated on the job card at G1 (sessions, agents, models) | the lead reports actual vs estimate at every gate |
| Model per role | Opus: lead and taste-critical design calls · Sonnet: specialist craft and building · Haiku: mechanical work (search, copy, format, data entry) | cost scales with model; every agent file pins its model (no silent inherit) |

## 7. Checks

- **Agents check what can be measured:** gate, tests, budgets, screen-size math, clip metrics, rubric items with a separate grader context.
- **The owner judges taste.** Agent reviewers share the maker's blind spots (arXiv 2608.28122), so a creative result is never "approved" by an agent.
- Every agent checks what it **receives** against its brief before building on it, and checks what it **hands back** against the acceptance checks.

## 8. The owner's decision digest

The lead batches everything that needs the owner into one digest per turn (template `templates/jobs/decision-digest.md`): one line per item, the options, the lead's recommendation, and the default that happens if the owner does not answer. Few, clear questions: "the more often a reviewer is asked, the less each answer means".

## 9. Learning

When a job ends or a gate is answered, each agent writes a short lesson draft to `knowledge/inbox/`: what worked, what failed, and the owner's corrections word for word. A weekly reviewed pass (`/learn`, kit phase 2) promotes lessons into skills and rules. Never edit a skill or rule from a single unreviewed lesson.
