---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J023-D6, J023-D7 (owner); J023 lead brief 2026-10-24; knowledge/jobs/J023-flow-speed/research/*.md
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J024 design: no roughs, one direction-and-needs step, fewer reviewers (binding for the J024 builders)

Goal: about 75 % fewer agent runs than the original flow, same results (J023-D3, D6, D7). J023's build (`knowledge/jobs/J023-flow-speed/design.md` B-G) is the start state; everything there stays unless this file changes it. Recipes (`orchestration/references/job-types.md`), the scripts (`.agents/workflows/jobs/*.js`), `.agents/workflows/jobs/README.md` and `rules/company.md` must say the same thing after the change.

## 1. The new flow (every job type, both sizes)

`direction` → **G1** → `build` → **G3** → close; `repair` after a G3 change request or a review that needs one. **No `proof` stage and no G2 in any job type.** A call with `stage: "proof"` returns `blocked` before any agent, with the reason "no proof stage (J024): direction → G1 → build → G3". G1 and G3 stay in every type (no other gate is removed).

L and M differ only in direction: L brings 2-3 options at equal finish (pictured, as today) and may set a new look; M brings one direction inside the approved style. The build stage is the same for both sizes.

## 2. No roughs (J023-D6, D7)
- Each craft builds the real, polished thing **once**, in one run. Removed everywhere: rough, temp, prototype, blockout, greybox, proxy, value-strip, board, animatic, first-spec and proof passes, every check-in run between a rough and a final, and every review of a rough.
- An agent may rough things out **inside its own run** (its own blockout, proxy pose, quick probe). It never hands a rough to another agent and nothing waits on it.
- A check that caught a real problem in our jobs moves into the maker's own run as a measured self-check, and the integrated review measures it again on the final captures (examples: the rigger's posed-proxy clearances, J005; the film-director's 4:3-centre read, J015). Cutscene: the film-director plans every shot's camera (size, angle, FOV, move), length and the marker list in the beat sheet only (J023-D7).

## 3. Direction and craft needs in one stage
1. **D1 plan (one run, the job lead):** the direction (L: 2-3 options with their image prompt rows; M: one direction) **and** the shared plan draft (the type's plan: beat sheet, character sheet, blueprint, screen contract, feature contract, effect timeline, asset kit), revision 1, written to hold for every option. Where the plan depends on the option, the row says so.
2. **N1 needs (parallel, one run each):** every craft in the type's needs row (§6) writes a **needs table** against plan revision 1; every constraint owner writes a **limits table**. Format (`rules/messages.md` §4, new template `templates/jobs/needs-table.md`): at most 12 rows; columns `id | need or limit | from (role) | value or range, with unit | why (one line) | blocks build (yes/no)`; rows beyond 12 go into one `omitted:` line. Each agent reads **only the plan file and its own brief**: never the other crafts' tables or any lead's proposal.
3. **Merge (one run, the job lead):** reads the plan and all needs tables, settles every conflict it owns, writes `direction.md` (each conflict with its owner and resolution) and plan revision 2 (the merged contract) with the G1 packet rows. Its hand-back names the conditional crafts the plan needs (§6, "if the plan lists").
4. **N2, only on a conflict the job lead cannot settle alone:** only the crafts in that conflict, each given only the conflicting rows, answer once; then a second merge. Never more than these 2 needs rounds (`rules/company.md` §4 limit); then a decision or a small test.
5. **G1** shows the direction and the agreed plan together. After G1, `build` starts at once. Each craft confirms the merged plan or names an incompatibility in its first build hand-back (J023 D3 rule stays; an incompatibility is `needs-decision`).
6. J023's joint needs meeting (C) is this step, moved before G1: the owner's "crafts come back together" (J023-D2) happens here. Build never re-asks; a later need is a contract change.

## 4. Build and fewer reviewers
1. **Production:** each craft one run, in the plan's dependency order (marker producers before consumers: animator → VFX → sound; modeler → rigger → animator; UI design → builder). Independent crafts run in parallel (≤ 5 at once, one Studio, Blender and browser user at a time).
2. **Integration:** the type's integrator, one run (folded into a maker's run where §6 says so).
3. **Capture and scripts, one `studio-operator` run (Sonnet):** imports or plays the frozen candidate; runs the gate and the type's measuring scripts (`look_check.py`, `clip_check.py`, `thumb_check.py`, scene audit, `shotlist.py` diff, budgets); captures key frames (numbers for every case, images at key frames and where a number fails); reads the Output-log cue times. Hand-back adds `visual_flags` (measured visual numbers outside their range; [] when none) and `cue_log` (event, VFX and cue start on one clock). A scripts FAIL stops the other reviews until it is fixed (existing rule).
4. **Review round 0:**

| Reviewer | When |
| --- | --- |
| scripts and gate (§4.3) | always |
| **job lead, integrated review** on the captures | always. It measures key frames itself (`look_check.py` at the game camera and phone size; J015 near-black shot), checks the gameplay read, and checks **sound sync** from `cue_log` against the marker list (the sound-designer no longer reviews) |
| `reviewer` (code review) | only when the candidate changed code (a code-owning maker's files) |
| `qa-lead` | only for player-facing logic: skip and endings, shop and purchase flows, saves, server results, multiplayer (per type in §6) |
| `performance-engineer` | only when `risks` names the new universal token `performance` |
| `art-director` | only with `newLook: true` (or `launch: true` in marketing), or when `visual_flags` is not empty (it then reviews in that round) |
| risk-gated slots (`risks` tokens, `money`), the `event` live-ops review | unchanged from J023 |

   Removed as reviewers: the sound-designer, the game-designer (except as job lead of feature), the progression-designer, the architect, the VFX designer (except as job lead of effect), the animator, the feature-builder.
5. **Selective recheck (J023 B) stays,** with the new chain: later rounds run the capture-and-scripts step, the qa-lead where the chain has one, the `reviewer` when code changed, every reviewer with a blocking finding, and the dependents of a repaired layer (the job lead's integrated review after any visual or timing repair; the art-director after a visual repair, only when it is in the chain). The rest are `carried: <reviewer> (round n, revision r)`. Limits: 2 rounds, code 3.

## 5. Two ideas from T3 Code (`J023-flow-speed/research/t3code.md` takeaways 1-2)
- **(a) Capped repair hand-offs.** A repair brief to a maker carries only: its own findings (id, expected, observed, evidence path), the list of parts changed since it last worked (file @ revision), and the protected list. A rechecking reviewer gets its own previous findings and the changed-parts list and reopens only those parts and the fresh capture. Cap: at most 10 findings and about 1,500 words per brief; every finding left out is named on one `omitted: <ids> (lower rank, sent next round if still open)` line. Never the other reviewers' full review files or the whole previous candidate. Scripts build these briefs; tests read them from `dump`.
- **(b) Compact before the pause, not after.** The lead cannot run `/compact` or `/clear` itself. Before it sends a gate packet (G1, G3) or any digest it must wait on, it writes the stage state to the job files; the packet's last line asks the owner to answer in a fresh session (or to run `/compact` first) when the chat is past the session size, so a paused chat is never resumed at full size after the prompt cache expired. One line in `rules/assistants/claude.md` (Session size or a new Gate pause row) and one in the orchestration skill (§1 step 5 and §8).

## 6. Per job type: steps and minimum runs
"min" = clean fakes, `risks: []`, every flag at its cheapest value (measured with `tools/workflows/wf_harness.mjs`). Before: original (committed HEAD) / J023.

| Type | Direction: D1 plan · N1 needs (crafts) · N1 limits (constraint owners) · merge | Build: production · integrator · capture · reviews | L min after (target) | Before L min: orig / J023 |
| --- | --- | --- | --- | --- |
| Cutscene (film-director) | D1 film-director: options (L) + beat sheet with every shot's camera, length and the marker list (no strips, boards or animatic). Needs: animator, environment-designer, vfx-designer, sound-designer; ui-ux-designer only if the plan lists on-screen UI beyond the stock player (title cards, subtitles, choices). Limits: architect (player contract, skip, endings, code owners); art-director when `newLook`. A new cast stops direction with `needs-decision` and a linked character job (as today: before build) | environment-designer set; animator clips + import; vfx-designer; sound-designer on the VFX envelope; ui-ux-designer if listed; feature-builder playback, skip and every ending; film-director scene assembly (integrator). Capture. Reviews: film-director integrated (incl. sound sync), qa-lead (always: skip and endings), reviewer (always: player code); art-director, performance by rule | 17 (16-20) | 56 / 48 |
| Character (art-director) | D1 art-director: directions (L) + character sheet (read plan, size at game camera, moves, sell list). Needs: game-designer (gameplay needs), character-rigger (rig plan: S0 sheet + S2 cuts, joints, pivots; its posed-proxy clearances measured inside its own run), animator (S1 motion needs), modeler, vfx-designer, sound-designer. Limits: architect (wiring contract) when `playable` | art-director reference set (the final model sheet from the G1 pick; pending images stop the stage as today); modeler final geometry from the approved reference (cuts, UVs, textures, icons, own audit) in one run; character-rigger rig (S4 check, S5 rig, tests); animator S6 acceptance + S7 clips + import; vfx; sound; feature-builder wiring when `playable`. Capture. Reviews: art-director integrated; reviewer and qa-lead when `playable`; performance by rule. Variant mode keeps its skips | 16, playable 20 (about 20) | 46 / 43 |
| Stage (environment-designer) | D1 environment-designer: options (L) + blueprint (spaces, landmarks, light plan, ambience zones). Needs: game-designer (route graph and route needs), modeler (new kit pieces), vfx-designer, sound-designer (ambience). Limits: performance-engineer when `performance`; art-director when `newLook` | modeler new kit pieces only if the plan lists them; environment-designer builds the final place (terrain, dressing, light, atmosphere, sky; scene audit inside its run); vfx and sound ambience; environment-designer places ambience and freezes (integrator). Capture (scene audit, budgets, route numbers). Reviews: environment-designer integrated; art-director, performance by rule | 12 (about 12) | 48 / 41 |
| UI screen (ui-ux-designer) | D1 ui-ux-designer: options (L, `newLook`) + screen contract (every screen and state, information list, flow). Needs: feature-builder, sound-designer; vfx-designer only if the plan lists UI effects. Limits: architect (code owners, interface); progression-designer when `shop`; art-director when `newLook` | ui-ux-designer final Figma + Roblox handoff; feature-builder implements and integrates (one run); sound; vfx if listed. Capture. Reviews: ui-ux-designer integrated; reviewer (always: screen code); qa-lead when `shop` or `paid-random`, `server-result`, `shop-screen`; art-director, performance by rule | 11 (about 12) | 35 / 26 |
| Feature (game-designer; technical lead architect) | D1 game-designer: options (L: approaches) + feature contract (behaviours, states, failure cases, presentation list). Limits: architect (presentation contract, placement, code owners); progression-designer when `numbers`. Needs: ui-ux-designer, vfx-designer, sound-designer, animator, each only if the presentation list names it | qa-lead protected acceptance tests first; feature-builder builds and integrates; progression tables when `numbers`; ui, vfx, sound, animator if listed. Capture. Reviews: game-designer integrated; reviewer (always); qa-lead (always: feature logic); art-director, performance by rule | 9 | 37 / 32 |
| Effect (vfx-designer) | D1 vfx-designer: options (L, `newLook`) + effect timeline (frame script, marker list, importance tier). Needs: sound-designer, feature-builder (wiring); animator when `animated`. Limits: game-designer when `danger-area` or `frequent-effect`; art-director when `newLook` | animator final clip + import when `animated`; vfx-designer final spec, once; sound cues on the VFX envelope; feature-builder (quick-builder when `small`) wiring. Capture. Reviews: vfx-designer integrated (incl. sound sync); reviewer (always: wiring); qa-lead when `server-result` or `paid-random`; art-director, performance by rule | 10 (about 10) | 35 / 29 |
| Marketing art (marketing) | D1 marketing: options (L, prompt rows) + asset kit plan (sell list, display sizes). Limits: art-director when `launch`. No needs crafts: D1 writes `direction.md` itself; a merge runs only when a limits table exists | marketing makes the final piece once (render, colour, polish, layered file, crops). Scripts (`thumb_check.py` at player sizes) on the studio-operator. Reviews: marketing integrated review and package; art-director when `launch` or `visual_flags` | 4 | 22 / 17 |

Builders may land one or two runs off a target when a rule needs it; they say which rule. Every conditional craft is switched by an explicit field in the D1 or merge hand-back (default false/[] in the fakes) or by an arg or risk token, and each switch has an on and an off test.

## 7. Args (README args table)
- `stage`: `direction`, `build`, `repair` (`proof` is refused, §1).
- New universal `risks` token `performance` (all 7 scripts): switches on the performance-engineer (limits in stage direction; review in every type).
- New required boolean `newLook` in cutscene and stage (no default; `true` needs `L`, like UI and effect). Character: the job lead is the art-director; no arg. Feature: none (`visual_flags` only). Marketing: `launch` plays this part.
- `images` and `studioId`: every stage that J023 required them in `proof` now requires them in `build` and `repair` only (character `new-enemy` direction keeps `studioId`). Images approved at G1 enter `build`.

## 8. What stays (quality checks with measured evidence: `J023-flow-speed/research/lead-and-evidence.md` §2)
Scripts first and the gate; code review where code changed (strongest evidence); the qa-lead protected suite; the job lead's own key-frame measurement (J015) and the lead's readiness look (SKILL §7.4); coverage reading; contracts with a Consumers table and one marker list; capped repair rounds with selective recheck; G1 and G3 with approval bound to a revision; images only after the owner's yes; one Studio driver.

## 9. Quality risks this leaves (for the owner summary)
- No G2: the owner first sees built work at G3; a wrong big shape costs a repair of finals, not a cheap proof. Mitigation: the plan is agreed at G1 with pictures; repairs are selective.
- No separate rough review: real catches from the J015 greybox and the J005 posed proxy now rely on the maker's own in-run check plus the integrated review.
- Fewer domain reviewers: gameplay read (game-designer), sound listening (sound-designer) and prices (progression-designer) are judged by the job lead and measured numbers; sound is checked by cue times, listening stays owner-confirmed at G3.
- The 75 % figure counts agent runs with clean fakes; tokens per run may rise (one bigger run per craft). Real-job tokens must be measured with `tools/usage_report.py`.

## 10. Who builds what (file owners)
| Builder | Owns |
| --- | --- |
| A | `.agents/workflows/jobs/job-cutscene.js`, `job-effect.js`; new `tools/tests/test_j024_cutscene_effect.py` |
| B | `job-character.js`, `job-stage.js`; new `tools/tests/test_j024_character_stage.py` |
| C | `job-feature.js`, `job-ui-screen.js`, `job-marketing-art.js`; new `tools/tests/test_j024_feature_ui_marketing.py` |
| Writer | `rules/company.md`, `rules/messages.md`, `rules/assistants/claude.md`, `.agents/skills/orchestration/**`, `templates/jobs/**` (new `needs-table.md`), `.agents/workflows/jobs/README.md`, the "place in the job flow" lines of `.agents/roles/*.md` and craft `references/handoffs.md` lines that name a removed step |
| Test updater (after A-C) | `tools/tests/test_job_workflow*.py`, `tools/tests/test_j023_*.py` |
Nobody edits another builder's files or `.claude/` copies (generated by `python tools/sync_harness.py`).

## 11. Lead decisions inside the brief
| ID | Decision | Why |
| --- | --- | --- |
| LD1 | The proof stage is removed from every type, and so is G2 | J023-D6, D7: no roughs; the proof is the rough pass; brief: "No owner gate other than G2 is removed" |
| LD2 | Capture and scripts are one studio-operator run | both always run together; saves one run per type and round |
| LD3 | The needs step sits before G1 (in `direction`) | brief cut 2: "G1 shows the direction and the agreed plan together; production starts at once" |
| LD4 | Conditional crafts (cutscene UI, UI VFX, feature presentation, stage new kit) are switched by plan fields | build what is asked (`rules/anti-overengineering.md`) |
| LD5 | `performance` risk token and `newLook` in cutscene and stage | brief cut 3 needs a flag for both; `risks` and `newLook` already exist as patterns |
| LD6 | Character keeps the reference-set run at build start | the modeler builds from an approved reference image (brief); it is the final reference, not a rough |
| LD7 | A switch the merge decides reaches `build` through the hand-back of the build step that owns that part of the plan (UI: `B1-figma` `ui_effects`; feature: the qa-lead's `B1-acceptance` `presentation`). Where no early build step owns it (cutscene on-screen UI), the direction result returns `build_args` and the lead passes it as a required arg (`ui`) | a stage call cannot read the previous stage's result (builders A and C, 2026-10-24); the plan file stays the source of truth |
