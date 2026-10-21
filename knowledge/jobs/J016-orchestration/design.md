---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J016 step 1 (owner papers P1, P2; 14 Riot transcripts; current kit; capability check)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 step 1 — Studio orchestration design (PROPOSAL until the owner's G1)

Status: PROPOSAL. Written before reading the owner's sketch (owner's step order). Every choice cites evidence. Labels: **VERIFIED** (docs or a measured, checked result), **PROBED** (tested on the installed Claude Code 2.1.296), **EXPERIENCE** (a studio's first-hand account; Riot transcripts are this), **OPINION** (a paper's or this design's recommendation). Human-studio practice is evidence of what works for people; using it for AI agents is an inference (P1:29).

## Evidence keys
| Key | Source |
| --- | --- |
| P1:n | `Studio_Orchestration_Research_2026.txt` line n (owner paper) |
| P2:n | `AI_Roblox_Studio_Orchestration_Research.txt` line n (owner paper) |
| C01-C16, K1-K7 | `capability-check.md` in this folder (docs check, live probe, claim spot-checks) |
| R00 | Riot core fundamentals series · R01 concept art (ep1) · R02 environment art (ep2) · R03 3D character art (ep3) · R04 animation (ep4) · R05 VALORANT key art (ep5) · R06 TFT VFX (ep6) · R07 Arcane sound (ep7) · R08 TFT splash (ep8) · R09 VALORANT map (ep9) · R10 TCG card art (ep10) · R11 2XKO style (ep11) · R12 VALORANT skin concept (ep12) · R13 TFT environment (ep13). `R05:170` = transcript line 170. Extracts: `riot-extracts.md` |
| kit | file:line in this repo |

## 0. The design in ten lines
1. You talk to one lead (the orchestrator). It sizes the job, picks the job type's recipe, names a **job lead** and convenes only the leads the job needs (P1:353; P2:446; kit `rules/company.md:17`).
2. Four maps are kept apart: **who decides**, **who talks**, **what depends on what**, **who reviews** (P1:39; P2:22).
3. **Direction:** the right leads write independent proposals, exchange them once, and the job lead writes one direction sheet that the others sign (P1:194; P2:183; K1).
4. **G1:** you choose the direction from 2-3 options shown as pictures, with one recommendation (P1:355; P2:372; R05:170-176; R08:656-712).
5. **Interfaces:** the crafts that depend on each other agree a shared contract (beat list, rig sheet, route graph, state map, feature contract) in at most two exchange rounds, with a small test when words cannot settle it (P2:147-158; kit `rig-pipeline`; R03:864-900; R02:472-480).
6. **Proof:** a cheap integrated version (animatic, greybox, pose test, clickable wireframe, playable prototype) is reviewed by the leads, then **G2:** you see it (P1:256; P2:373; K5; K6; R13:663-697).
7. **Production** runs in parallel along the contract; decision owners check in during the work, not only at the end (R02:460-470; R09 loops; K4).
8. **Reviews go up in a fixed order** on one frozen candidate: scripts → maker self-review → next craft → domain lead → integrated review (technical in parallel, creative in order) → lead readiness. Reviewers do not edit; makers fix; two repair rounds, then diagnose (P1:220-234; P2:199-215; K2).
9. **G3:** you accept the real result in Roblox. Agent reviews decide what is ready to show you, never what is approved (kit `rules/company.md:93-95`).
10. One saved workflow per job type runs **one stage per call**, because a workflow cannot pause for you; your gates sit between calls (C07; C08).

## 1. Four maps, kept apart
| Map | What it holds | Shape | Evidence |
| --- | --- | --- | --- |
| Authority | who decides each question | owner → lead → job lead → decision owner per question | P1:188, P2:174-181 |
| Communication | who may talk to whom | anyone sharing an interface talks directly (files first, messages by id); the lead sees status and blockers, not every sentence | P1:39, P1:398, P2:447 rule 3 |
| Dependency | which artifact needs which | a graph per job type (§6); edges carry revisions | P1:234, P2:231 |
| Review | who checks what, in what order | §4; each review answers one distinct question | P1:220, P1:464, P2:199 |

Why separate: one tree for all four makes the lead a relay that rewrites every interface question, the hub-and-spoke failure both papers name (P1:41; P2:86). The kit today joins them: "The doing agent reports to whoever asked, never sideways" and "Hub and spoke by default" (kit `rules/company.md:51`, `:60`).

## 2. Who decides what (authority map)
One role owns each decision. Others are consulted where their interface or an approved direction is touched (P2:174-181; P1:188). The veto rows come from Riot practice (R02, R09, R13: extract C §6).

| Decision | Owner | Must consult | Escalate to the owner when |
| --- | --- | --- | --- |
| Game promise, fantasy, style direction, scope, budget, locks, every gate | **Owner** | lead, relevant leads | always for material changes |
| Job size, recipe, crew, order, integrator, routing, readiness | **Lead (orchestrator)** | job lead | a schedule/quality trade-off outside the approved brief |
| Player rules, routes, cover, sight lines, pacing of play, what a screen must let the player decide | **game-designer** (numbers: progression-designer) | architect, art-director | the player promise changes |
| Visual language: shape, value, colour roles, light mood, silhouette, cross-craft cohesion | **art-director** | game-designer, film-director | the approved style changes |
| Shot order, staging, camera, pacing, performance intent, the beat list of a cinematic | **film-director** | art-director, animator, VFX, sound | story meaning or approved direction changes |
| Technical feasibility, engine features, code interfaces, file owners, runtime budgets | **architect** (budgets measured: performance-engineer) | builders, crafts | the creative goal cannot be met inside the constraints |
| What moves, how far, event timing inside gameplay windows | animator (planned role) | rigger, game-designer | — |
| Joints, cuts, rigid vs skinned | character-rigger | animator, modeler | a look change (rig-pipeline §1) |
| How a cut or shape is built; asset budgets | modeler | rigger, art-director | — |
| The picture of an effect | vfx-designer | sound, animator | — |
| The sound of an event; whether a new surface material can have footsteps in time | sound-designer | vfx, environment | — |
| Screen states, hierarchy, layout | ui-ux-designer | game-designer, art-director | — |
| The built place, light, atmosphere, ambience map | environment-designer | game-designer (routes are theirs), art-director | — |
| Block release of a candidate on evidence | reviewer, qa-lead, performance-engineer | maker | a waiver is needed |

Rules: a reviewer's dissent is information, not a veto, unless it is inside that reviewer's authority (P1:190). A preference is called a preference; an impossibility comes with evidence or a test (P2:183). The lead resolves order and scope inside the approved brief and never invents your taste to break a tie (P1:196). Taste ties go back to the brief's goal first; when every option meets it, the craft owner decides the last details (R05:160-164, R05:834-846).

## 3. The general flow (every M and L job)

```
OWNER ──request──► LEAD: intake, size, recipe, job lead, crew
                     │
          ┌──────────┴──────────┐   D1 independent proposals (parallel)
     job lead       other leads     D2 one exchange: conflicts that change production
          └──────────┬──────────┘   D3 job lead writes the direction sheet; others sign
                     ▼
                ◆ G1 DIRECTION (owner picks from 2-3 pictured options)
                     │
     crafts that share an interface  I1 each writes needs/plan against the contract draft
     (model↔rig↔anim, anim↔VFX↔sound, I2 consumers check producers; conflicts named
      layout↔environment, UI↔code)    I3 decision owner reconciles → contract rev; ≤2 rounds; small test if words fail
                     ▼
     cheap integrated PROOF (animatic / greybox / pose test / wireframe prototype / playable prototype)
     lead reviews: domain lead → art-director → architect
                     ▼
                ◆ G2 PROOF (owner: does this execution express the direction?)
                     │
     PRODUCTION in parallel along the contract; decision owners check in during the work;
     each maker: workflow book → self-review → hand-off; the next craft checks what it receives
                     ▼
     INTEGRATION: one integrator, one Studio writer, a frozen candidate revision
                     ▼
     REVIEW CHAIN on that revision: scripts → technical/QA ∥ domain lead → art-director → lead readiness
     findings go to the maker; only the failed layer and its dependants are rechecked; ≤2 repair rounds
                     ▼
                ◆ G3 FINAL (owner accepts the real result, or names an experience-level change)
                     ▼
     CLOSE: archive, evidence ledger, usage actual vs estimate, lessons into the right workflow-book step
```

| # | Stage | Who starts and works | Output | Claude Code tools | Evidence |
| --- | --- | --- | --- | --- | --- |
| P0 | Intake | Lead, from your message | job card with your words verbatim, size, recipe, job lead, crew, usage estimate in tokens | lead chat (`orchestration` skill), job folder files | P1:361 (keep the owner's words); kit lesson J010 (estimate tokens, report the meter) |
| D1 | Independent proposals | the job's leads, in parallel, **without seeing each other** | one short proposal each: reference images, intended experience, non-negotiables, uncertain assumptions; constraint owners (rig, sound, tech) state limits before design | `Workflow` stage `direction` → `parallel(agent({agentType: <lead role>}))`; `reference-images` (ChatGPT, built-in browser) | P1:194; K1 (11.1 % of correct answers flipped by upstream messages); R01:94-99, R11:87-129 (constraint owners speak first) |
| D2 | One exchange | each lead reads the others' files | only conflicts that would change production | same workflow, second `parallel()` | P1:194, P1:196 |
| D3 | Synthesis | job lead | direction sheet + decision records (question, options, owner, evidence, affected assets, dissent, revisit trigger); others sign their part or name an incompatibility | same workflow, one `agent()`; files | P1:190, P1:194 |
| G1 | Direction gate | Lead → owner | one screen: 2-3 pictured options, recommendation, trade-off in player terms, scope, usage estimate | lead chat; `decision-digest`; workflow boundary | P1:355-359; P2:372; R05:170-176 (2-3 directions, state the preferred one); R08:554-566 (show rough so the idea is judged) |
| I1-I3 | Interface agreement | crafts that share an interface (§6 per type) | contract revision with stable ids; acknowledgements; compatibility test results | `Workflow` stage `interfaces`; files in `exchange/`; direct `SendMessage` by id for a clarifying question | P2:147-158; P1:165-169; C01-C03 |
| PR | Proof | the crafts the proof needs (only those) | the cheap integrated version | Workflow stage `proof`; Blender MCP, Studio MCP (one writer), Figma MCP | P1:256; P2:65-70 table; K5; K6 |
| PR-R | Lead review of the proof | domain lead → art-director → architect | ranked findings; fixes before you see it | same stage | P2:201 ("review animatic and blocking before finished animation") |
| G2 | Proof gate | Lead → owner | the proof itself first, then the decision | workflow boundary | P1:355; P2:373; R08:668-682 (green light: big things stop moving) |
| PD | Production | crafts in parallel where the graph allows | owned artifacts with revisions, self-review records, evidence | Workflow stage `build` (`pipeline()` per artifact chain); or a production chat for a long L job | P1:426; P2:231 |
| PD-C | Check-ins | decision owner looks at work in progress at named points | short notes; paint-over on a screenshot when visual | `SendMessage` (resume by id) or a file note | R02:460-470 (embedded designer; without check-ins the result is "mediocre"); R03:790-806, R13:205-219 (paint-overs) |
| IN | Integration | the job's integrator, holding the Studio writer lease | one revision-pinned candidate | Studio MCP with its `studio_id`; files mode for code | P1:294; P2:274; kit `rules/owner-profile.md` (one Studio, sequential) |
| RV | Review chain | §4 | findings, verdicts per revision | Workflow stage `review` (`parallel()` for independent technical checks, ordered `agent()` calls for creative) | P1:220-234; P2:199-215 |
| RD | Readiness | lead | owner package: what was checked, by what evidence, what was not | lead chat; `python tools/verify.py` for code | P2:210; C15 (a hook can enforce hand-back shape) |
| G3 | Final gate | owner | accept, or one experience-level change | — | P1:361; P2:374 |
| CL | Close | lead (+ doc-keeper, Haiku) | ledger final, lessons in `knowledge/inbox/`, usage actual vs estimate | files | kit `rules/company.md:101-103`; P1:436 |

**S jobs** (one agent, one area, no new look): no direction stage, no gates before; maker self-review + one domain check; you see the result (kit `rules/company.md:25`; P2:376 combine gates for tiny jobs). **M jobs** (one specialist output inside an approved style): G1 (brief + direction in one) and G3; the proof is shown at G3 unless the job changes the look (P1:355 "a small already-approved variation may need fewer gates"). **L jobs:** all three gates. An extra gate opens only when scope, artistic intent, rights, spend or release risk changes (P1:355).

## 4. Reviews: order, rules and stop conditions
| Order | Review | Question | Evidence it needs | On failure | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Scripts first | do the measurable rules pass? | gate, audits, `shotlist.py check`, `model_audit.py`, `look_check.py` numbers | back to maker, no reviewer time spent | P2:199; P2:346 (script before model); kit J005-D8 (numbers for every case) |
| 2 | Maker self-review | did I meet my contract and my workflow book's bar? | the book's self-check, at the real camera and size | maker fixes before asking | P2:205; R03:198-208, R08:302-310 (zoom out, real size) |
| 3 | Consumer check | can the next craft use this? | pose / import / timing / interface test | producer and consumer reconcile | P2:206; kit `rig-pipeline` K-checks |
| 4 | Domain lead | is it good inside its discipline? | in-context capture beside the references | notes to the maker | P2:207 |
| 5a | Technical / QA (parallel with 5b) | does it behave right on target devices? | test logs, Studio captures, phone evidence | blocks acceptance | P2:209; C15 |
| 5b | Integrated creative, in order | does the whole communicate and belong? | full synchronized playback, not parts | one consolidated note set to the affected crafts | P2:208; P1:432 |
| 6 | Lead readiness | are approvals current, every check evidenced, nothing stale? | revision-pinned evidence ledger | resolve missing, stale or contradictory items | P2:210 |
| 7 | Owner | is this the experience you want? | the real result | accept, or a clear experience-level change | P2:211 |

Rules that protect correct work:
- **Reviewers read, makers write.** A finding names artifact + revision, the exact frame/test/location, expected vs observed, severity, evidence and the smallest fix; the maker applies it in a new revision (P1:226; P2:213). Evidence: a review chain lost 36 correct answers and repaired 6 of 371 (K2).
- **Three classes:** blocking defect · recommendation · new request. New requests go to scope review, so taste does not pose as a defect (P1:228; P2:215).
- **Protected list** per candidate: what already passed and must not change (P1:228).
- **Independent look first:** a reviewer opens the files before reading the maker's narrative (P1:171; P2:213; K1).
- **Light checks** stay the default: numbers for every case, images only for a failing number plus a few key cases; one full check per hand-off, by the receiver (kit `rig-pipeline` §4a, owner J005-D8).
- **Stop:** when required checks pass and the intent is visible; a clean review is valid (P1:232). Two repair rounds per review gate; a third means diagnose the brief, the tool, the standard or the approach (P1:232; P2:215; kit `anti-overengineering.md` rule 20 uses 3 for code: kept for code review). "Done" signs from practice: the notes start to repeat (R08:814-820); after the polish point big changes wait for the next version (R13:681-697).
- **Selective recheck:** only the failed layer and the artifacts that depend on it; the dependency map says which (P1:234; P2:272).
- **Visual notes are pictures:** a paint-over or marked-up screenshot, not only words (R03:790-806; R13:205-219, R13:826-832).

## 5. Sideways cooperation (communication map)
**Transport, as tested:** subagents can message each other with `SendMessage`, but **only by id**: there is no sibling list inside a subagent (C01, C02). On 2.1.306 a message reaches a working agent at its next tool step; on 2.1.296 it arrived only after the agent finished (C03, probed on both). So:
1. **Files are the default channel.** Each craft writes its plan, needs and responses in the job's `exchange/` folder against a named contract revision; the decision owner merges accepted changes into the contract (P1:165; P2:145; K7; kit `rules/messages.md:110`, files stop injected instructions spreading: 0 % vs 95 %).
2. **Direct messages are for awareness and clarifying questions** between crafts on one interface: "contract rev 7 moved B04 to 4.8 s; acknowledge and recheck" reaches a working craft at once. The lead keeps the crew's ids in the job's `crew.md` and in each brief; the answer is recorded in the contract or decision log (P1:171 messages solve awareness, files solve persistence; P1:398; P2:158; P2:447).
3. **Resume the maker for repairs** (`SendMessage` to its id), so it keeps its context; the repair note still points to files (C03, C11 fixed in 2.1.304).
4. **Tickets only for new work** (asking another role to produce something). Clarifications need no ticket. `inside: no` still goes up, nothing starts (P2:447 rule 3; kit `rules/company.md:49-50` kept).
5. Exchange shape: each note says **agree / conflict / missing evidence**, names the artifact revision, and the decision or test needed. "Looks good" is not enough for a critical interface (P2:151; P1:334).
6. Rounds: direction 1 proposal + 1 resolution; interfaces ≤ 2 reconciliation rounds; then a decision by the owner of that question or a focused test (P1:196; P2:154). These are pilot settings, not measured optima (P1:208; P2:160).
7. A contract change lists every consumer; each acknowledges and rechecks; outputs built on the old revision are marked stale, not deleted (P1:298; P2:158, P2:272).

## 6. Job types
See `design-jobtypes.md` (cutscene, character or creature, stage, UI screen, gameplay feature; plus effect and marketing art, which the transcripts show have their own dependency shape; variant of an existing asset runs as a mode of the character recipe).

## 7. Claude Code tools per job element
| Element | Tool | Facts that bind it |
| --- | --- | --- |
| You ↔ lead | the lead chat (main session), `orchestration` skill | the only chat that talks to you |
| A lead or craft doing one task | `Agent` tool with the role as `subagent_type`; the role file pins model, effort, skills, memory | C05, C06; nesting ≤ 3 below the main chat (C04) |
| A job stage with fixed order | saved `Workflow` per job type in `.claude/workflows/`, source in `.agents/workflows/jobs/`, `args: {job, stage}`; `agent({agentType, model, effort, schema})`; `parallel()` for independent proposals and checks; `pipeline()` for artifact chains; shared sub-recipes via `workflow()` | C07-C09; no file access in the script (agents read and write); no pause mid-run, so one stage per call |
| Your gates | between workflow calls; the lead records your words, then starts the next stage with the decision as input | C07; P2:241 |
| Sideways exchange | job-folder files (`exchange/`, contract, decision log) | C02; K7 |
| A clarifying question or a repair | `SendMessage` to an id the brief names | C01, C03, C11 |
| A long, independent L job | a production chat (`start_session`), reporting by cross-session text that points to files | C13, C14 |
| Studio and Blender | Studio MCP with `studio_id`, one writer at a time; Blender MCP; worktrees do not isolate them | P1:294; C14 |
| Hand-back shape | `templates/jobs/handback.schema.json` as the `schema`; optional owner-applied `SubagentStop` hook that refuses a hand-back without `STATUS`/`coverage` | C15 |
| Not used | agent teams (experimental, interactive only, one per session) | C12 |

## 8. Limits that replace "3 hops" and "3 concurrent"
The kit's hop limit cites the platform nesting limit (kit `rules/company.md:86`); nesting limits spawning, not production stages (C04; P1:12; P2:92).

| Limit | New default (pilot setting) | Why |
| --- | --- | --- |
| Spawn depth | lead → workflow or job lead → helper (2 below the main chat) | platform max 3 (C04); deeper nesting adds paraphrase layers (P1:41) |
| Production stages | as many as the recipe's graph needs | P1:402 |
| Direction rounds | 1 proposal + 1 resolution | P1:196 |
| Interface rounds | ≤ 2, then decide or test | P2:154 |
| Repair rounds | 2 per review gate, then diagnose (code review keeps 3, kit rule 20) | P1:232; P2:215 |
| Parallel agents per stage | as many as independent artifacts in the graph, max 5 (pilot) | P2:82 (parallel only where outputs are independent); K3 (overhead grows with agents) |
| Usage | estimate in tokens at G1; actual at every gate | kit lesson J010 |

## 9. Models and effort
Keep the owner's roster (kit `.agents/roles/README.md`: Opus for leads, crafts and all code; Sonnet for research, data pulls and Studio checks; Haiku for search, copy, format). It matches both papers: strongest model for leads, creative judgment, integration and high-risk review; cheap models only for checkable mechanical work; a script before a model when the check is deterministic; never a cheap model certifying creative quality (P1:328-330; P2:338-346). Effort by uncertainty and consequence, not title (P1:330); Opus medium is the measured sweet spot on coding, xhigh only for measured gains (P2:315). Messages between agents stay complete: omitted constraints come back as rework (P2:352; kit `rules/messages.md:5`).

## 10. Workflow books (every role)
Each role's book (role file + design skill + craft skill + references) must have, near the top, the items both papers and the owner list (P2:282-293; P1:260-262; owner 2026-10-21):
1. Mission, authority, consumers, what great work looks like in this game. 2. Inputs and stop conditions. 3. **Reference images first** for visual work (approved image, game camera, style book), alternatives before polish. 4. Numbered steps with the **collaboration points** of this design (which contract it reads, who it checks in with, who checks it). 5. Its Roblox docs rows (`knowledge/reference/roblox/docs-map.md`) with the date checked. 6. File and export conventions. 7. Self-review with positive and failure examples. 8. Evidence capture and hand-off. 9. Tool limits and escalation. 10. Change history: lessons go into the step they fix, not a growing warning list (P1:262).
Riot practice per role: `riot-extracts.md` §4. Step 6 updates each role file's place in the chain; adding the Riot craft lessons to each craft skill's steps is a separate owner decision (digest item).

## 11. What changes from today's kit
| Today (kit) | New | Evidence |
| --- | --- | --- |
| Hub and spoke by default; report only to whoever asked, never sideways (`company.md:51`, `:60`) | Hybrid: one accountable lead; direct exchange between crafts that share an interface; status to the lead | P1:7, P1:41, P2:15, P2:84-90 |
| Every request is a ticket (`company.md:37`) | Tickets for new work only; clarifications in exchange files or by direct message; decisions recorded | P1:398; P2:447 |
| Chains max 3 hops (`company.md:86`, `messages.md:112`) | Round, repair and depth limits (§8) | C04; P1:402 |
| 3 concurrent specialists per job (`company.md:84`, from agent-teams advice) | parallel by the dependency graph, max 5 per stage (pilot) | C12 (teams not used); P2:82 |
| G2 = one sample per craft, batched (`company.md:30`) | G1 shows direction options (pictures); G2 = one **integrated** cheap proof | P1:355; P2:373; K5; K6; R08:656-712; R13:663-697 |
| Checkers check measurable rules; taste only by the owner (`company.md:93-95`) | Kept for checkers. Domain leads also review craft quality before you see it, as a filter that never approves | P2:207-208; kit `art-director` role (reviews before visual work reaches the owner) |
| "Split by context, not by role; no planner → builder → tester chain" (orchestration skill §4) | Separate agents where a distinct interface, judgment or parallel product exists; one agent for small coherent work; never review by the same agent that made it | P2:513 table; K3; P1:392 |
| Lead briefs every specialist | Lead briefs the job lead; the job lead's direction sheet and the contract brief the crafts; briefs still in the `messages.md` format with every rule | P1:384-390; kit `rules/messages.md` §1-2 kept |
| Approval recorded per gate | Approval recorded per gate **and bound to the artifact revision**; a later revision that departs from it is surfaced | P1:361; P2:455 rule 10 |

Kept unchanged because they protect quality: briefs in the `<intent>`/`<spec>` format with every rule stated and every fixed value sourced; claims checked against files; `STATUS` first and `coverage` in every hand-back; one decision digest per turn; your words recorded; no agent passes on your approval (kit `rules/messages.md` §1-5; `rules/company.md` §8).

## 12. Unknowns and the pilot
- No controlled study shows this hybrid beats the current process for Opus 5.5 on Roblox work (P1:33; P2:540). It is a hypothesis for your pilot.
- Your step 8 pilot, as both papers propose: a capability rehearsal first (one lead exchange, one parallel hand-off, one rejected review, one repair by resume, one restart), then one short cutscene under (A) today's process, (B) one strong Opus agent with the same books, (C) this design; same brief, assets and models; measure your blind rating, first-pass acceptance, defects that escaped review, repairs that broke correct work, usage and time, and your minutes spent (P2:402-422; P1:440-450).
- Claude Code is now 2.1.306 (J016-D3): C10 and C11 are fixed. Re-run the capability probes after every update (C03 changed between versions).
- Context handling (owner J016-D2): `design-context.md`.
