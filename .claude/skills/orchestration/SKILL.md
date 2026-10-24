---
name: orchestration
description: The lead's playbook for running the AI studio. Use at the start of every owner request, and whenever an agent must size a job, pick a job recipe, run leads' direction, gates, sideways exchange, reviews, a job workflow stage, briefs, statuses, the owner digest or job close-out.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; rewritten in J016 (owner approval J016-D4, 2026-10-21). Kit skill: universal. Binding rules: `rules/company.md` (flow, roles, gates, limits), `rules/messages.md` (formats), `rules/knowledge.md` (context). Evidence: `knowledge/jobs/J016-orchestration/`. Revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3 audit). Rebuilt by J018 maker orchestration · claude-opus-5-5 · high · 2026-10-22 (repair rounds 1 and 2 the same day): built also from the owner's Riot transcripts (J018). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021-D3, D5, D6): target-experience sentence, belief check, outside method, stop floor and bar. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-24 (J022): fresh session per stage.

# Orchestration: running the studio

After a compaction, re-load this skill and re-read §8, §14 and §15 before you continue; the end of §14 and all of §15 sit past the part a compaction keeps.

## 1. The lead's loop for every owner message
1. **Read** the message twice: what the owner wants to see and feel, not only what to build. Check `knowledge/jobs/active.md`, other chats and `git status` for overlap. Write **four lines**: the problem in the owner's terms; the constraints (camera, device and input, player count, budget, platform rules, locks); the target experience (one or two named kinds of fun, never "fun", then one sentence of what the work must make the player feel, do or believe, with no number: "mastery: a stranger does the core action without reading"; the sentence shows which outside fields can help, and is never written into a mechanic `Verb` field); the success test the owner will see (its numbers live here). A line you cannot fill is a digest question or a PROPOSAL assumption.
   **Belief check** (before any D1 brief): when the problem line or the owner's words claim what this game's current players do or feel (quit, skip, miss, get stuck, do not return, do not buy), a different answer would change the direction, no analyst reading of that claim is cited from the last 21 days, and the game has player data (`game-profile.md` Live data row filled, key set), spawn the analyst for a belief check (`analysis-craft` §3.7; Sonnet medium; one run per card revision). Record the result in the card's Belief check row; the G1 packet shows it as evidence, never as a decision: the owner's words stand by default. No data: write "not run: no player data", tag the belief PROPOSAL and name its cheapest test; no spawn.
2. **Size it** (`rules/company.md` §2): S, M or L, with one line of why; a character with several forms counts once per form. **Pick the recipe** (§2 below).
3. **S:** do it yourself or give it to one role; self-review + one domain check; show the result where players meet it (game-camera capture at phone size, or a play-test); report. Stop here.
4. **M / L: open the job** (§3), then run the stages in order. Each stage is one call of the job type's saved workflow (`/job-<type>`) or the same steps by hand with subagents. Args (`.agents/workflows/jobs/README.md`): `gate` (the owner's words verbatim) after every gate, `studioId` for every Studio stage; `size` and every flag that switches a rule or gate (money, saves, remotes, newLook, variant) have no default: a missing one returns `blocked`.
   `direction` → **G1** → `proof` → **G2** (L only) → `build` → **G3** → close. M jobs: `direction` → G1 → `build` (the proof runs inside `build`) → G3.
5. **Between stages:** read every hand-back's `coverage` against the files, record the owner's words and the doors the gate closed (§8), update `active.md` (and `crew.md` for hand-spawned agents), write inbox drafts from the hand-backs' `lesson` fields, run the stage result's `images_pending` batches (`reference-images` §4: the owner's yes per batch, one digest question per stage; approved paths into `decisions.md` and the next stage's `images` arg), then start the next stage with the gate decision as input and the closed doors in its briefs' `avoid`. A workflow cannot pause for the owner: never start the next stage before the gate answer. Run each stage from a fresh session when this chat is past the size in `rules/assistants/claude.md` (Session size): the job folder carries the state; never carry a stage's file reads, images or tool output into the next.
6. **G3 change request:** restate the note as the problem behind it and name the door it reopens and what goes stale (`references/gates-and-feedback.md` §5); stage `repair` reopens only the affected crafts and rechecks only what depends on them.
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
| Mixed request | one job per type, linked in `knowledge/jobs/active.md` ("a gold skin to sell in the shop" = a character variant job + a shop-listing feature job with money); never a "closest type" that drops part of the request; one owner job per shared interface, its contract first (`references/briefs-and-handoffs.md` §8) | — | — |
| Unclear (no type fits) | the closest type that covers the whole request, with the reason in the job card; none covers it → one question in the owner digest | — | — |

A role that is still planned runs as a stand-in: a general subagent on Opus high with that role's brief and the skills it would load (same pattern as J005-D2).

## 3. Opening a job (M and L)
1. **Prerequisites first:** check the recipe's prerequisites for this game (`knowledge/design/game-profile.md` filled; for a job that creates assets, a naming and folder rule: a link in the game profile, or one line in the job card until the profile has a field for it; `art-bible.md` and approved anchors for visual work; released rigs, with joint lists, for existing cast; a test place and its `studio_id`). Run a missing one as its own job or gate before this job opens.
2. Re-list `knowledge/jobs/` right before creating the folder (parallel chats take numbers). Copy `templates/jobs/`.
3. **Job card:** the owner's words verbatim first, then the four lines (§1), size, type, job lead, direction leads, crew, mechanism, stop criteria per stage as floor (the success test) and bar (observable signs a top professional needs; `rules/messages.md` §2), a budget per stage (passes, image cap, usage estimate **in tokens** from the last job of this type in its `evidence.md`; no history: say so), acceptance checks, gates.
4. Add the job to `knowledge/jobs/active.md`. For hand-run stages start `crew.md` (role → agent id, filled as agents start).
5. Brief the direction leads (§4). Every brief carries the packet line `--role <role> --job <job-id>`.

## 4. Direction stage (the right leads agree before crafts start)
1. **D1 independent proposals, in parallel:** each direction lead gets the same job card, references and constraints, and **not** the others' proposals. Each returns what its recipe row names, plus the intended player experience, non-negotiables, uncertain assumptions, limits it knows (rig cost, sound time, tech risk, budget), one recommendation and what it needs from the other crafts first. A lead that owns a look or an approach (the recipe's pictured options) adds the options package: research (its outside source chosen from the target-experience sentence, naming the method taken from that field: `references/gates-and-feedback.md` §3), hooks, a warm-up set aside, one radical, 2-3 options at equal low finish with play value and cost (`references/gates-and-feedback.md` §3). A constraint owner (architect, performance-engineer) returns limits and needs, never an option menu for a technical choice; the progression-designer returns its targets the way its books shape them (options that bracket the key number, one recommendation).
2. **D2 one exchange:** each lead reads the others' files and lists **only conflicts that would change production** (exchange notes, `rules/messages.md` §4).
3. **D3 synthesis:** the job lead writes `direction.md` (`templates/jobs/direction-sheet.md`) with a decision record per consequential question (the template's fields), the target-experience line every craft brief quotes, the dropped options with reasons (closed at G1), one importance rank when several effects, sounds or celebrations compete (game-designer; reward tiers: progression-designer), and the marker-list owner when animation, VFX and sound meet. Each other lead signs its part or names an incompatibility.
4. Unresolved taste or a material trade-off → the owner digest with pictures. A tie is not by itself a reason to ask the owner; the decision owner decides inside the brief.
5. **G1 packet** (§8).

## 5. Interfaces and proof
1. The job lead drafts the **contract** (its form per recipe) with stable ids, a revision and a Consumers table (the dependency map; `templates/jobs/contract-header.md`). With code, the architect fills its code file owners table (`owns` per builder). Where animation, VFX and sound meet, the timing contract is **one marker list** (`references/briefs-and-handoffs.md` §3).
2. Interfaces where the recipe places them (a needs round before the proof, craft planning after G2): each consumer writes its needs against the contract draft **before** its producer builds; consumers check producers; the decision owner merges the next revision. ≤ 2 rounds; then a decision or a small test.
3. The proof is cheap (greybox, proxy, placeholders, temp sound; nothing polished) and uses only the crafts it needs. The recipe's proof reviewers review it in its order before the owner (`rules/company.md` §4 step 5).
4. **G2 packet** (§8). After G2 the big shapes stop moving: layout, proportions, timing beats and key light change only by a new owner decision.

## 6. Production, sideways work and contract changes
- Crafts work in parallel along the dependency map. In a hand-run stage you spawn every craft (a subagent job lead drafts the briefs); give each brief the `peers` ids it needs from `crew.md`, but only for roles that can send (`rules/company.md` §5-6). Saved-workflow stages have no ids: sideways work goes through files in a fixed order.
- Decision owners check in at the recipe's named points (e.g. film reviews blocking before polish; the game-designer checks the stage build as it grows). Visual notes are paint-overs. **No grand reveals:** a craft's first hand-back to its consumers is a rough state, checked before polish; the owner sees roughs at G1 and the cheap proof at G2; each status report carries the newest rough picture, labelled rough (who sees which rough: `references/gates-and-feedback.md` §6).
- A contract change: new revision, change table row, a notice to each consumer (`rules/messages.md` §5; relay it when the producer cannot send), stale outputs marked. A retime is a contract change (`references/briefs-and-handoffs.md` §3). When a message reaches a working or finished agent: `rules/assistants/claude.md`, Peer message row.
- **Additions are tickets:** a "cooler" idea after G1 or a costly part beyond the brief (a cape, a new joint chain, an extra form) gets a ledger row with its cost and the reason it earns its place; approve it inside the budget or digest it.
- One owner per file or Studio container: check `git status` and the contract's `owns` before routing an edit; a crossing edit goes through an exchange note.
- Repairs go back to the maker with the finding file and the protected list: resume a hand-spawned maker by id; in a workflow, a fresh call.
- One Studio driver (read or write) at a time; name the `studio_id` in every Studio brief.

## 7. Integration, review chain, readiness
1. The recipe's integrator assembles one frozen, revision-pinned candidate.
2. Scripts first; then the recipe's review order (`references/job-types.md`), technical checks beside the creative order. A candidate with code always has the `reviewer` (`rules/company.md` §7). Reviewers open the artifact before the maker's hand-back; findings follow `rules/messages.md` §6.
3. Two repair rounds per review gate; then the stage returns `needs-decision` to you. Diagnose (brief, tool, standard or approach) and fix what is yours; an approach that failed both rounds restarts at its cheapest stage, not a third patch; only scope, taste or budget goes to the owner digest.
4. **Readiness (lead):** every acceptance check has evidence at the candidate's revision; approvals are current; no stale input; open limits, placeholders and stand-ins listed. Look at key frames or captures yourself, at the game camera and phone size, in the order gameplay read, feel, look; not only the reviews (J015 lesson).

## 8. Talking to the owner and gate packets
- Follow `rules/owner-profile.md` and `ste-writing`. **One decision digest per turn** (`templates/jobs/decision-digest.md`).
- **The goal question:** it carries the job card's goal word and asks for one decision ("which pet reads as the most loyal friend at phone size?"), never "do you like it?"; labelled options, one recommendation with reasons tied to that goal, the default.
- **Gate packet, one screen, in this order:** (1) the artifact as players meet it (game-camera capture at phone size, playable preview, icon at 150x150), never a polished picture shown as the in-game result; (2) the goal question; (3) the options at the recipe's count and equal finish, each with its play value and cost; failed options listed with the reason, never shown as equals; (4) the recommendation, its weakest part said plainly, one real alternative, the trade-off in player terms, a rejection reason per option, and at G1 the belief check result when the card has one; (5) what changed since the last approval; (6) the checks block (`references/gates-and-feedback.md` §2, "Every packet carries"), with each craft's `BAR` line; (7) the doors this answer closes; (8) usage, estimate vs actual. Per gate and image budget: `references/gates-and-feedback.md` §2.
- **Gates close doors.** Record the answer with the owner's words **and the revision it approves** in the job's `decisions.md`, and each option not picked as a closed door with "may return only if" (reference §4); none is re-proposed without new owner words. G1 freezes the direction, G2 the big shapes and timing beats; a structural note at polish is a follow-up or a `repair` with its cost stated.
- **Owner notes** become repair briefs only through `references/gates-and-feedback.md` §5, every step (an agent never overrules an owner note: §5 step 8).

## 9. Close: file the job into the vault
Give a doc-keeper (Haiku or Sonnet) the list; check its result; then run `python tools/kb_index.py` yourself (the doc-keeper has no `Bash`).
1. Owner decisions → `knowledge/design/decisions.md` with a revisit trigger.
2. Accepted artifacts → `knowledge/design/precedents.md` (what, why accepted, owner's words, path@revision).
3. New names (states, events, cues, assets) → `knowledge/design/vocabulary.md`.
4. Finished systems → `knowledge/systems/<system>.md` with a contract card + index row.
5. Rejected options and closed doors with a lasting lesson → `tried-and-failed.md` with a retry condition. Owner corrections → `taste-log.md`, word for word.
6. New reusable assets → their catalog.
7. Job metrics: every row of `evidence.md` §4 (first-pass acceptance, repair rounds by cause, owner-found defects, usage vs estimate, ...).
8. Inbox drafts from the hand-backs' `lesson` fields and your own, with `cause` and `layer`; remove the job from `active.md`; final ledger statuses; an honest retrospective line (what worked, what was too tame or too big, what more iteration would fix); a manual step repeated 3 or more times (PROPOSAL count) becomes a tool proposal.

## 10. Intent briefs: what and why, never how
Example (cutscene beat → animator): intent "the player must feel the dragon is too big to fight; beat 3 of 6, shot 4"; spec `fixed` length and camera from the shot list, `open` the poses and timing inside it.
A brief gives the receiver everything it needs to make **its own best craft choices**, in the `rules/messages.md` §2 format: `<intent>` prose (goal, feeling, context, why), then `<spec>` with every key, each `fixed` value with its source, every `rule`. Send it whole, in one message; direction briefs never carry another lead's proposal.
- **Open with what `references/briefs-and-handoffs.md` §1 lists** (the four lines for the receiver's part, budget, stop criteria, consumers' needs), plus that file's per-type items (§4); exact vs open per craft: `preproduction/references/handoffs.md` §2.
- **Exact where another system, craft or the owner depends on the value; open where the role is the expert.** A feeling is a target plus an observable sign, never a method. Never prescribe craft ("use 3 flaps per second") unless it is a locked owner decision; downstream crafts get intent, not settings. If the brief cannot say *why*, it is not ready.
- **Every brief names the Roblox docs** the work touches: the packet's "Roblox docs" section and the receiver's rows in `knowledge/reference/roblox/docs-map.md` (why: `references/briefs-and-handoffs.md` §9).
- **Code briefs** add the files owned, the interface, invariants, dependencies, non-goals and failure-case checks; effort and where `fixed` goes: `references/briefs-and-handoffs.md` §9. One runnable check per rule, never "double-check everything".

## 11. Models and usage
Per-role defaults: `.agents/roles/README.md` (owner-approved); helpers without a role file: `references/briefs-and-handoffs.md` §10.

- A script before a model for any deterministic check. A cheap model never certifies creative quality or safety.
- Every brief and every workflow `agent()` call names the role (`agentType`), model and effort.

## 12. Statuses
- `blocked` / `failed`: fix it if you can (missing file, unclear brief); otherwise send it one level up with the reason.
- `needs-decision`: the lead first decides what is its own (`rules/company.md` §3, §8); only scope, taste or budget goes into the owner digest, with a recommendation and a default. `inside: no` requests: never start them; digest them.
- `stale`: the output's owner rechecks or rebuilds against the new revision.
- `done` follows the real outcome: only when every acceptance check has evidence; a pending capture or test is reported as pending, never as done.
- Two pushes on open coverage items, then `failed`; repair rounds: §7.3.

## 13. Verification before reporting
- Gate PASS for code; measurable checks for content (budgets, screen-size math, clip metrics, `look_check.py`, `thumb_check.py`); reviews in the recipe's order.
- **Read each hand-back's `coverage` against the files, not the summary.** A missing item or a `pass` without evidence goes back with one line naming it. The hand-back hook checks shape only (`references/briefs-and-handoffs.md` §6).
- Say exactly what was checked and what was not, with its label (gate-verified, MCP-verified, owner-confirmed, not verified) and what its input can prove (`references/gates-and-feedback.md` §2); end with the could-not-check list. A job whose result the server confirms carries a rejected-request capture (no success layer plays). Never claim the owner's approval from an agent's message.

## 14. Self-check before every report to the owner
Input in brackets.
- [ ] Size and recipe stated; gates followed; no stage started before its gate answer; the four lines, stop floor and bar and budget in the card before the first brief; the belief check run or marked "not run" before D1 [job card, `active.md`].
- [ ] Packet in the §8 order: opens on the artifact as players meet it (each image names camera, size, place); one goal question with the card's goal word; options at equal finish with play value and cost, failed ones listed with the reason; one recommendation with its weakest part, a rejection reason per option [packet vs job card; greps: `references/gates-and-feedback.md` §1-2].
- [ ] Checks read, feel, look, each with its input label; stand-ins named; could-not-check list; feel and listening only owner-confirmed; the images the owner is asked to look at (the `Shown:` line) inside the budget, counted by eye, never from the whole-file grep [packet, hand-backs' `checks`; `references/gates-and-feedback.md` §2].
- [ ] Rough states reached partner crafts and the owner before polish; no first look at polish [ledger, status reports].
- [ ] A closed door per option not picked; none re-proposed this turn without new owner words [`decisions.md` vs briefs; grep: reference §4].
- [ ] Owner answers recorded with words and approved revision; notes restated as problems with a layer; one problem per repair brief; conflicting notes settled by `references/gates-and-feedback.md` §5 step 8, never averaged [`decisions.md`, repair briefs].
- [ ] Every brief: the four lines, the target-experience line, budget and `stop` floor and bar, every rule, skills, the Roblox docs rows, sourced `fixed` values, inputs with revisions, consumers' needs [briefs, `rules/messages.md` §9].
- [ ] The card and briefs carry the job type's items (`references/briefs-and-handoffs.md` §1, §4) before the briefs that depend on them: sell list and display sizes (visual work); the roster gap (character); the grey-box verdict cited in any production art brief and a balance re-check list for a mode change (feature); the ranked list, the floor-material list and a light brief dated after the last route change (stage); every screen and state before style (UI); a cue list per state change (sound); the importance tier, play rate and worst-case count, and marker names (effect); the asset kit with the launched thing as hero (marketing); a theme library before character work (new theme); data, audience and differentiator (live update) [job card, briefs, ledger dates].
- [ ] Hand-backs read against their files; no consumer left with an open question about its input [hand-backs, files].
- [ ] One marker list where animation, VFX and sound meet; each retime has a change row and a notice to both [contract, `exchange/`].
- [ ] "Done" only with evidence at the candidate revision; pending said as pending; a rejected-request capture where the server confirms the result [evidence ledger].
- [ ] Additions after G1 are tickets with a cost; `active.md`, `crew.md`, ledger current; nothing `working` without a reason; usage estimate vs actual; one digest with defaults [ledger].
- [ ] At each gate and at close: inbox drafts from lessons; at close the vault filing (§9).

## 15. Core principles for this craft
The studio's shared principles (master numbers), stated for the lead's work: sizing, routing, briefs, gates, reports. 5 (shape), 9 (push past real) and 12 (controlled variation) are craft execution: route them to their owners; check only that the job lead's review ran them.

| # | For my work | Example | Check [input] |
| --- | --- | --- | --- |
| 1 | **Gameplay read first:** packets and readiness put the read before beauty | A lava obby's G3 packet opens on the busiest phone capture where the safe platforms read, not the key art | Read checks come before feel and look [packet] |
| 2 | **Judge where players meet it:** no decision on a beauty shot, editor view or turnaround | A fountain approved from a Blender render hid the shop door at spawn | Each image names camera, size, place [packet] |
| 3 | **Decide what is read first:** the owner reads the decision first; one importance rank per job | Eight new tower-defense effects get one tier table; only the boss wave fills the screen | Goal question right after the artifact; tier table when events compete [packet, `direction.md`] |
| 4 | **Big before small:** direction, proof, build, in order | No texture brief for the pet before G1 picks its silhouette | No polish ticket dated before its gate [ledger] |
| 6 | **Less is more:** fewest decisions before the owner; features earn their place; briefs stay complete | A five-item digest becomes two decisions and three defaults | Packet fits one screen; additions are tickets [packet, ledger] |
| 7 | **One code for meaning:** one vocabulary, one marker list, one decision log | `slam_contact` is one name in the timing list, VFX script and cue card | Brief names match `vocabulary.md` and the contract [briefs] |
| 8 | **Timing tells cause and effect:** I keep the timing contract whole | The wind-up shortens 0.5 → 0.4 s; VFX and sound get the notice that turn | Change row and notice per consumer [contract] |
| 10 | **The owner's intent drives every choice** | "Scary but beatable" rides in the animator, VFX and sound briefs | `owner_words` copied from the card [briefs] |
| 11 | **One world, one style:** visual briefs name the bible revision and anchors; a new look is L | A winter re-skin is M; a second world's new style is L with G2 | Bible revision in `refs`; size per `rules/company.md` §2 [briefs, job card] |
| 13 | **Problem, constraints, target first** | "Make the shop better" → "players miss the shop", phone first, comfort, "names the shop in 1 s at spawn" | Four lines in the card before the first brief [job card, ledger dates] |
| 14 | **Research, distinct options, a reasoned pick** | D1 brings research, hooks, a warm-up set aside, one radical; G1 shows equal finish | Options differ in the big read; one pick; rejection reasons [packet] |
| 15 | **Cheap stages first; gates freeze; not precious** | The neon option closed at G1 stays closed; a look failing two rounds restarts at roughs | Closed-door rows; none re-proposed [`decisions.md`] |
| 16 | **Critique against the goal, one problem at a time; say our own weak spots** | "Make it pop" → "the shop sign does not read first at spawn (value)"; the G1 packet says the recommended pet's weakest part | Each repair brief: one problem, its layer, the goal word; the packet names the recommendation's weakest part [repair briefs, packet] |
| 17 | **Build for the next craft and the engine:** needs first, reuse first, one owner per file | The rigger's joint list reaches the modeler before modelling | No consumer question left open [hand-backs] |
| 18 | **Know when it is done:** stop criteria and budgets; rounds end when notes repeat | A third "slightly better" option round becomes a follow-up | Budget and stop lines in each brief [briefs] |
| 19 | **Feedback follows the real outcome:** done on evidence, pending as pending | "Purchase works" waits for the capture where the server rejects a buy and no coins fly | No "done" without an evidence path [report, ledger] |
| 20 | **Every player can read it:** safety and comfort faults block a gate | A boss flash over 3 per second stops G3 until its reduced path exists | Grayscale, sound-off, reduced-motion checks listed or "not verified" [packet] |

## Read this file when
| You need | Open |
| --- | --- |
| The recipe for a job type (leads, contract, proof, crafts, integrator, review order, return paths) | `references/job-types.md` |
| Goal questions, gate packets per gate, image budget, what each input proves, closing doors, owner notes, showing early, when it is done, worked examples | `references/gates-and-feedback.md` |
| What every lead brief opens with, asking the next craft first, the timing contract, per-type card and brief items, reuse and cost, reading hand-backs, an example direction brief, linked jobs of a mixed request, code briefs and effort, helper models | `references/briefs-and-handoffs.md` |
| The binding rules (roles, gates, decisions, limits, reviews, statuses) | `rules/company.md` |
| Brief, exchange, review and hand-back formats | `rules/messages.md` |
| How context is layered, routed, passed and learned | `rules/knowledge.md` |
| Job folder templates | `templates/jobs/` |
| The roster and per-role effort | `.agents/roles/README.md` |
| How the owner wants to be talked to | `rules/owner-profile.md` |
| Claude Code and Codex specifics | `rules/assistants/claude.md`, `rules/assistants/codex.md` |
| The evidence behind this design | `knowledge/jobs/J016-orchestration/design.md` |

Project overlay: if `knowledge/overlays/orchestration.md` exists, read it after this file; it wins for this game.
