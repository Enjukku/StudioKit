---
type: job
scope: universal
status: draft
updated: 2026-10-24
source: J023 research
supersedes: []
---
> Author: researcher (general-purpose) · claude-sonnet-5-5 · default · 2026-10-24

# J023 flow map: character (and creature) job and stage job

Scope: every step, who does it, what passes between agents, why the step exists and what it protects. No cuts are recommended here. "What breaks if removed or merged" gives evidence or says "no evidence found".

## 0. Method, short names and limits

**How the counts were made.** The saved scripts were run under the kit's fake-agent harness (`tools/workflows/wf_harness.mjs`, read-only use). Agent runs, labels and the longest serial chain ("depth") come from those runs, not from estimates. For the maximum cases a copy of the harness was patched in the scratchpad (not in the repo) so a review could name several makers in one round, force note rounds and force open interface conflicts. Every maximum below was checked against the label list the harness printed. The fake agents never fail on their own, so each "maximum" is a ceiling (every repair round used, every maker named), not a forecast.

**No real run exists.** J016's evidence ledger says a real run of any job workflow was "not run" (J016 `evidence.md:25`). The only rig run is the J005 teddy test (`J5L`). All "why" and "breaks" evidence is therefore design-time evidence (owner papers, Riot transcripts, the first game, the J005 test), not run data. Where a step has none, the cell says so.

| Short | File |
| --- | --- |
| JC / JS | `.agents/workflows/jobs/job-character.js` / `job-stage.js` |
| RM | `.agents/workflows/jobs/README.md` |
| JT | `.agents/skills/orchestration/references/job-types.md` |
| OS / BH / GF | `.agents/skills/orchestration/SKILL.md` / `references/briefs-and-handoffs.md` / `references/gates-and-feedback.md` |
| RP / MH / TR | `.agents/skills/rig-pipeline/SKILL.md` / `references/modeler-handoff.md` / `references/tripo-routes.md` |
| CO | `rules/company.md` |
| CL | `rules/assistants/claude.md` |
| DJ / DD / RX | `knowledge/jobs/J016-orchestration/design-jobtypes.md` / `design.md` / `riot-extracts.md` |
| CAP | `knowledge/reference/studio/claude-code-capabilities.md` (rows K1-K7) |
| J5D / J5W / J5L / J5G | `knowledge/jobs/J005-character-rigger/` `decisions.md` / `workflow.md` / `ledger.md` / `g2-gaps.md` |
| G3P | `knowledge/jobs/J018-riot-craft/g3-proposals.md` |
| ED / J8B | `.agents/skills/environment-design/SKILL.md` / `knowledge/jobs/J008-environment-designer/brief.md` |

Path shorthand in tables: `D/` = `knowledge/jobs/<job>/`; `RIG/` = `content/rigs/<asset>/`; `MOD/` = `content/models/<asset>/`; `ANIM/` = `content/anim/<asset>/`; `SND/` = `output/sound/<asset>/`; `VFX/` = `content/vfx/<asset>/`; `SH` = `RIG/rig-sheet.md`; `S/` = `content/stages/<stage>/`. "Opus H/M" = Opus high/medium effort. "Par X" = agents that run at the same time in group X.

**Fixed cost of every agent run (not repeated in the tables).** Each run is a fresh agent. Before its own work it reads the job card and `decisions.md`, runs the context packet and reads its docs-map rows (BASE_RULES, `JC:173-187`, `JS:150-164`). Its role file and preloaded skills are already in its context: role file plus `SKILL.md` files are about 14 KB (studio-operator), 48 KB (sound-designer), 62-71 KB (environment, rigger, animator, qa, builders), 78-96 KB (game-designer, modeler, art-director, vfx-designer) (measured with `wc -c` on `.agents/roles/*.md` and the `skills:` they list). CL:45 says cost is calls times context.

## 1. Totals

| Item | Character, L | Character, M | Stage, L | Stage, M |
| --- | --- | --- | --- | --- |
| Owner gates | G1, G2, G3 (3) | G1, G3 (2) | G1, G2, G3 (3) | G1, G3 (2) |
| Saved-workflow calls (stage calls) | direction, proof, build (3), plus repair on a G3 change | direction, build (2), plus repair | same 3 | same 2 |
| Agent runs, minimum (no repairs, no risks) | 46 = 12 + 15 + 19 | 46 = 12 + 34 | 48 = 12 + 12 + 24 | 48 = 12 + 36 |
| Same, if wired into gameplay (`playable`) | 49 = 12 + 16 + 21 | 49 | not a stage arg | - |
| Agent runs, maximum (every repair round used) | 116 = 13 + 46 + 57 | 116 | 170 = 13 + 39 + 118 | 170 |
| Same, playable | 136 = 13 + 51 + 72 | 136 | - | - |
| Same, stage with every play-change and new-material hand-back refused | - | - | 258 = 13 + 47 + 198 | 258 |
| Longest serial chain at minimum (depth; agents that must wait for one before it) | 32 = 4 + 12 + 16 | 32 | 35 = 4 + 9 + 22 | 35 |
| Models at minimum | 45 Opus, 1 Sonnet (studio-operator) | same | 42 Opus, 6 Sonnet (studio-operator) | same |
| Exchange rounds | D2 x1 (+ D3 resolution x1); K1, K2, S3 counter, S4, S6 note rounds (see section 2.7); review repair rounds 2 (code 3) | same | D2 x1 (+ resolution x1); interface rounds up to 2; 5 check-ins x up to 2 repair rounds; proof review repairs 2; final review repairs 2 | same |
| Owner "yes" for image batches | up to 3: G1 options, reference set, reference-check views (`results.images_pending`, `JC:524`, `:593`) | same | up to 3 groups: G1 looks, paint-over (`JS:423`), one model sheet batch per kit piece (`JS:739`) | same |
| Agent runs outside the workflow | doc-keeper at close (1, Haiku); optional analyst belief check (Sonnet M) (OS:14, OS:83) | same | same | same |

Facts behind the table:
- **M costs the same agent runs as L.** M `build` runs the proof first and then production in one call: `proof()` then `production()` (`JC:1245-1252`, `JS:999-1004`). The only M saving is one owner gate and one stage call; the M harness runs gave 34 (character, 46 total) and 36 (stage, 48 total) in `build`.
- Variant mode and the risk tokens change the counts (section 2.8). Stage counts also depend on the kit-piece count K: add K modeler runs and 1 place-kit run if K > 0 (measured: K=2 gave 27, K=3 gave 28 in `build`).
- The J023 job card says one real cutscene run used 24 agent runs and about 200 M tokens before the animatic (J023 `job-card.md:25`). Compare: character L is 46 runs and stage L is 48 before any repair.

## 2. Character (and creature) job

A creature is the same recipe. The only creature-specific hook is the `new-enemy` risk (behaviour test). Skins and recolours use variant mode (section 2.8). Recipe: JT:36-51. Script: JC. Stages and checks: RP S0-S8.

### 2.1 Lead and owner steps (no `agent()` call)

| Id | Step | Who | Reads / writes | Why (evidence) | Breaks if removed or merged |
| --- | --- | --- | --- | --- | --- |
| L1 | Intake: size, recipe, job card, four lines, Risks row, `active.md` | lead (orchestrator) | reads owner message, `active.md`, `git status`, game profile; writes `D/job-card.md` | the script refuses to start without `size`, `variant`, `playable`, `risks` (JC:70-86); OS:12-14, OS:40-45 | missing arg returns `blocked` before any agent (JC:84-86); no other evidence found |
| L2 | Belief check (only if the owner's words claim what current players do and data exists) | analyst, Sonnet M | reads player data; writes belief result in card | OS:14 | skipped by rule when no data; no evidence found |
| G1 | Owner picks a direction | owner | lead shows 2-3 options at equal finish, grey and black-fill, anchors, failed options as numbers, recommendation (GF:17, OS:75-80) | CO:30, DD:107 | no evidence found |
| L3 | Image batch(es) between stages | lead + owner yes per batch | pending prompts to approved paths into `decisions.md` and `args.images` (OS:19, RM:11) | RM:11 (a workflow cannot pause for the owner); LD2 | pending batch stops proof as `blocked` (JC:193-195, :524) |
| G2 (L only) | Owner approves the proof | owner | signature pose options, stress-pose numbers, roster lineup, blockout views, rig plan (JC:1239) | CO:31, DD:111 | no evidence found; G2 freezes layout, proportions, timing beats (OS:58) |
| L4 | Between stages: read hand-back `coverage` against files, record owner words and closed doors, inbox lesson drafts | lead | OS:19, OS:116 | OS:19 | no evidence found |
| L5 | Readiness, then G3 packet | lead | evidence at the candidate revision, approvals current (OS:73) | CO:65 | no evidence found |
| G3 | Owner accepts the result in Roblox | owner | the imported revision (RP:55) | CO:32; DD:132 (the owner's question: is this the experience you want) | no evidence found |
| L6 | Close: file into the vault | doc-keeper (Haiku) + lead runs `kb_index.py` | OS:82-91 | CO:67 | not mapped further |

### 2.2 Direction stage (workflow call 1) -> G1

| Id | Stage / step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | D1 proposal: role in play | game-designer Opus H; Par A (4 runs C-01..04) | `D/job-card.md`, art bible if any, `templates/rig/rig-sheet.md`; not the other proposals (JC:377-394) | `D/direction/proposal-game-designer.md` | C-05 (D2), C-09 | game-designer owns what the character does and the reaction windows (JT:40; CO:43) | no evidence found for this call alone |
| C-02 | D1 proposal: 2-3 looks with images | art-director Opus M; Par A | same; plus art bible | `proposal-art-director.md`, `D/direction/image-prompts.md`, `content/art/refs/` via `art_refs.py` | C-05, C-09 | options each from its own hook, warm-up labelled, radical one, grey pass first (JT:138, GF:46-53) | no evidence found |
| C-03 | D1 proposal: rig cost | character-rigger Opus M; Par A | same | `proposal-character-rigger.md`, `D/direction/stills-character-rigger/` | C-05, C-09 | constraint owners state limits before design: capes, parts over joints, each with a cheap fallback (DJ:53; RX:37-39; RP:95) | none found for a run-time failure; RX:39 (capes and cloth cost animators months) is the design-time reason |
| C-04 | D1 proposal: motion profile and cost | animator Opus H; Par A | same | `proposal-animator.md` | C-05, C-09 | same reason as C-03, plus R15 limits (JC:355) | the recipe lists rigger and animator as one row (JT:40) but the script runs them as two proposals, two exchange notes and two signatures (JC:367-375, :424); no evidence found either way |
| C-05..08 | D2 exchange (one round) | same 4 roles; Par B | the other 3 proposals | `D/exchange/r1-<role>.md` | C-09 | only conflicts that change production (DD:105, CO:58, CO:130) | not tested: the 1 + 1 round limits are "pilot settings, not measured optima" (DD:151) |
| C-09 | D3 synthesis: direction sheet rev 1 | art-director Opus M | 4 proposals + 4 exchange notes + `templates/jobs/direction-sheet.md` | `D/direction.md` (options, anchors, signature action, costly parts, closed doors, could-not-check) | C-10..12, G1 packet | one sheet the owner picks from; job lead is the art-director (CO:12, JT:39) | no sheet, no G1 packet; no run evidence |
| C-10..12 | D3 signatures | game-designer H, rigger M, animator H; Par C | `direction.md@rev` | `D/direction/sign-<role>.md` | C-09 (merge) | each lead signs its part or names an incompatibility (CO:58) | an unsigned conflict reaches G1; no evidence found. The art-director does not sign (it wrote the sheet) |
| C-13 | D3 resolution (only if a signer refuses) | art-director Opus M | direction + sign files | `direction.md` next revision | G1 | the one resolution round (CO:130) | +1 run, only on refusal |
| C-14 | D4 behaviour capture (risk `new-enemy`) | studio-operator Sonnet M (Studio) | direction, game-designer proposal, game profile | `D/direction/behaviour-test/` stills, Output log, manifest | C-15 | plain Parts play the planned pattern before any model is briefed (JT:41) | G3P:85 (without it the game-designer must block the job or skip its own rule, game-designer rev3 R9) |
| C-15 | D4 behaviour verdict (risk `new-enemy`) | game-designer Opus H | captures + direction | `behaviour-test/verdict.md` | G1 packet | the game-designer judges planned vs measured | same as C-14 |

Direction totals: 12 runs, depth 4 (A, B, synthesis, C); +1 resolution; +2 behaviour test.

### 2.3 Proof stage (workflow call 2, L only; inside `build` for M) -> G2

Stop condition: if the reference set returns pending images, the stage returns `blocked` after the first two runs (JC:524). Contract steps first, then the proof.

| Id | Stage / step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-16 | P1 reference set (extra views, anchor close-ups, material intent) | art-director Opus M (images); Par D | approved direction, `decisions.md` | `D/art/reference-set.md`, `content/art/refs/` | modeler, rigger, animator | one set of views so three crafts build one character (JT:43) | RX:40 (a mouth modelled shut broke animation: the modeler must know the rig); no run evidence |
| C-17 | P1 gameplay sheet (actions, windows startup/active/recovery/cancel, camera, device) | game-designer Opus H; Par D | direction, decisions, game profile | `D/design/gameplay-sheet.md` | animator, rigger, feature-builder, perf | animation timing is set inside gameplay windows the designer owns (RP:20, RP:54) | the recipe never names this file (grep found it only in JC and J016 review notes); windows would be PROPOSAL in the rig sheet; no run evidence |
| C-18 | S0 open the rig sheet | character-rigger Opus M; Par E (3-4 runs C-18..21) | direction, reference set, gameplay sheet (+ base rig for a variant) | `SH` rev 1, section A | animator, modeler | K0: approved reference, source snapshot, purpose known (RP:47) | J5G:19 (GP05: K0 assumes an approved image for a pre-made test asset); RP names the lead as S0 owner, the script has the rigger do it (JC:530) |
| C-19 | P1 wiring contract (only if `playable`) | architect Opus H; Par E | gameplay sheet, direction, game profile | `D/contract-wiring.md` with Code file owners | feature-builder, reviewer, animator | code needs a file-owner table before the builder starts (RM:19) | the builder returns `blocked` if its row is empty (JC:992) |
| C-20 | P1 modeler reference check | modeler Opus H; Par E | reference set, direction | asset record in `MOD/`; `D/exchange/reference-check-modeler.md` only if it must ask | art-director (C-22), rigger, animator | catch missing views and unclear materials before the blockout (JT:43; G3P:80) | gaps would surface at S3; no run evidence |
| C-21 | P1 character sound plan (not for a variant) | sound-designer Opus M; Par E | direction (character card), gameplay sheet | `SND/sound-plan.md` | listed: animator, vfx-designer; actual readers: C-41 and C-47 only (grep `sound-plan` in JC) | sound joins before clips so the signature sound is known (JT:44; G3P:80) | no evidence found; see section 4 |
| C-22 | P1 reference answer (only if C-20 asked) | art-director Opus M (images) | modeler note, reference set | reference set next revision | modeler | the producer answers the consumer's note (RM:12) | +1 run; pending views stop the stage again (JC:593) |
| C-23 | S1 motion needs | animator Opus H | reference set, reference check, gameplay sheet, `SH`, direction | `SH` section B, `ANIM/motion-profile.md` | rigger | the animator states what moves and how far, with units and sources (RP:48) | J5G:15-17 (GP01-GP03: template gaps found in the teddy test); skipped in variant mode unless S0 finds new moving parts (JC:595-596) |
| C-24 | K1 check of the needs (<= 2 note rounds) | character-rigger Opus M; fix by animator Opus H | `SH`, reference set, gameplay sheet | `RIG/notes/k1-rN.md`, section H row | animator (fix), S2 | the receiver checks what it receives: every part has a record, no invented numbers (RP:48) | no evidence found of a K1 failure in the J005 test |
| C-25 | S2 rig plan, joints, cut list, renders | character-rigger Opus M | `SH`, reference set, reference check, direction, gameplay sheet | `SH` sections C, E, F; `RIG/renders/plan_*.png` | animator (K2), modeler | route per region, cuts with a reason, budgets with sources (RP:49) | first game: skinned merged limbs webbed and wrinkled, bridge necks creased, deleted faces opened holes (J5W:77, TR:11) |
| C-26 | K2 sign "plan covers needs" (<= 2 note rounds) | animator Opus H; fix by rigger Opus M | `SH`, `RIG/renders/` | `ANIM/notes/k2-rN.md`, section H row | rigger (fix), modeler | the producer's plan is checked by its consumer (RP:49) | J5L:29 (in the teddy test the K2b re-sign changed cap floors and swing numbers); a "not supported" that changes the look becomes `needs-decision` (JC:347) |
| C-27 | P2 blockout at player scale, split into the rig's cuts | modeler Opus H | reference set, reference check, `SH`, gameplay sheet | `MOD/export/`, `MOD/renders/` | rigger | cheap body for the proof (JT:45, DJ:56) | no evidence found |
| C-28 | P3 proxy rig and signature pose (2-3 pose options, 2-3 hardest stress poses with overlap and cap numbers, 6 rest views) | character-rigger Opus M (Studio, Blender) | blockout export, `SH`, gameplay sheet, direction | `RIG/proof/` captures + manifest | art-director, animator, game-designer | G2 shows a pose at the game camera on the real background (JT:45; DJ:56 -> R00:1183-1199) | G3P:79 (the cheap pass is the point of the proof) |
| C-29 | P3 roster lineup capture | studio-operator Sonnet M (Studio) | `RIG/proof/`, gameplay sheet, game profile | `D/captures/roster-lineup/` | game-designer, art-director | judge the role among existing characters at the same scale (JT:158; G3P:101) | no evidence found |
| C-30 | Proof review 1 | art-director Opus M | captures, lineup, blockout renders (looks at captures before hand-backs) | `D/reviews/proof-r0-art-director.md` | C-31 | silhouette, anchors, picks the signature pose (JT:45) | CAP:50 (K2): a review workflow lost 36 correct answers and repaired 6 of 371; reviews are read-only |
| C-31 | Proof review 2 | animator Opus H | same | `proof-r0-animator.md` | C-32 | is the rig usable for every action (JT:45) | no evidence found |
| C-32 | Proof review 3 | game-designer Opus H | same | `proof-r0-game-designer.md` | G2 | does the role read against the roster (JT:45) | no evidence found |

C-30..32 run one after the other (JC:1081). Repair loop in the proof: blocking findings go to makers in pipeline order (art-director, game-designer, modeler, rigger, animator, vfx, sound), then the rigger re-poses if the modeler or animator changed, then the lineup is retaken (JC:1128-1171). Limit 2 rounds. Proof totals: 15 runs (16 if playable), depth 12 = almost fully serial; the only runs that overlap are Par D (2) and Par E (3-4).

### 2.4 Build stage (workflow call 3) -> G3

| Id | Stage / step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-33 | S3 geometry: cuts, caps, sockets, UVs, rough textures; capture at game camera | modeler Opus H (Studio, Blender) | `SH`, reference set, `RIG/renders/`, `RIG/proof/`, decisions, modeler hand-off (MH) | `RIG/geometry/` parts, asset record, section D, `MOD/renders/` | rigger, art-director | the modeler decides how each cut is built and hidden (RP:17, RP:50) | first-game failures when the rigger cut or merged meshes (J5W:77) |
| C-34 / C-35 | S3 counter answer by rigger, then rebuild by modeler (only if the modeler counters a cut; one round) | rigger Opus M, modeler Opus H | `SH`, `MOD/` | `RIG/notes/s3-counter.md`, `SH` section C | modeler | the modeler may push back once with a better cut (RP:50, MH:51) | +2 runs on a counter; a posed proxy test settles it (RP:22) |
| C-36 | S3 art check-in at game camera before texture polish | art-director Opus M | `MOD/renders/`, reference set, direction | `D/reviews/model-rough-art-director.md` + marked captures | modeler | paint-over before polish; no grand reveals (OS:62; JT:47) | DJ:59 (R03:790-806); no evidence found of a run failure |
| C-37 | S3 texture polish; rerun K3 numbers | modeler Opus H | check-in notes, reference set, `SH`, `MOD/` | final parts, K3 numbers | rigger | polish after the look is checked | no evidence found |
| C-38 | S4 geometry acceptance: `rig_audit.py` + proxy sweep (<= 2 note rounds; fix by modeler) | character-rigger Opus M; fix by modeler Opus H | `RIG/geometry/`, `SH`, `MOD/` | `RIG/tests/`, `RIG/notes/s4-rN.md`, section G/H | modeler (fix), S5 | the receiver checks the cuts at every extreme (RP:51) | J5G:24 (GP10) shows the cost problem the S4 check had: 64-79 poses x 6 views per round; fixed by "numbers for every case, images only on failure" (J5D:22) |
| C-39 | S5 rig + tests: skeleton, weights, controls, manifest, export, Studio import | character-rigger Opus M (Studio, Blender) | `RIG/geometry/`, `SH` | `RIG/export/`, `control-manifest.json`, section G | animator | K5: release the rig only with a complete test record (RP:52) | J5L:32 (Roblox rows stayed BLOCKED in the J005 test until the owner imported) |
| C-40 | S6 rig acceptance: pose every extreme through the manifest (<= 2 note rounds; rigger triage: rig fix, or geometry note -> modeler fix -> rigger rebind) | animator Opus H; fix by rigger Opus M (+ modeler, + rigger rebind on a geometry note) | `RIG/export/`, manifest, `SH` | `ANIM/notes/s6-rN.md`, `ANIM/tests/`, section H | rigger | the animator never works around a missing degree of freedom (RP:53, RP:64) | no evidence found of a S6 failure; RP:93-100 lists which role catches which design-for-motion fault |
| C-41 | S7 blocking of every clip | animator Opus H | `RIG/export/`, manifest, gameplay sheet, `SH`, direction, `SND/sound-plan.md` | `ANIM/` blocking playblasts | C-42/43 | G2 sample on first use (RP:54); gameplay windows are not retimed (RP:76) | CAP:52 (K4): effects must wait for the beat list |
| C-42 / C-43 | S7 blocking check-ins | art-director Opus M; game-designer Opus H; Par F (2) | `ANIM/`, reference set, gameplay sheet | `D/reviews/blocking-art-director.md`, `blocking-game-designer.md` | animator | script-only step: the comment says the recipe names only the model check-in and this one follows `job-cutscene.js` (JC:901) | no evidence found |
| C-44 | S7 polish, export, timing list | animator Opus H | check-in files, gameplay sheet, `SH` | `ANIM/` clips, `ANIM/timing-list.md` | VFX, sound, feature-builder, icons | one marker list per job (BH:30-34; RP:75-76) | CAP:52 (K4): one timing change cascades into animation, effects and sound |
| C-45 | S7 icon renders | modeler Opus H (Blender); Par G (lane 1) | `MOD/`, `RIG/export/`, timing list, reference set | `MOD/renders/icons/` | ui-ux-designer, marketing | icons of the shipped model at their smallest size (JT:46) | the recipe names no owner for this step (JT:46); no evidence found |
| C-46 | S7 VFX against the timing list (not for a variant) | vfx-designer Opus H; Par G (lane 2, first) | timing list, `SH`, direction, gameplay sheet | `VFX/` frame scripts + spec | sound, feature-builder | VFX writes each envelope first, sound answers on it (RM:12) | CAP:52 (K4) |
| C-47 | S7 sound against timing list and VFX scripts (not for a variant) | sound-designer Opus M; Par G (lane 2, second) | `SND/sound-plan.md`, timing list, `VFX/`, direction, gameplay sheet | `SND/` cue cards | feature-builder | same | same |
| C-48 | S7 import into Studio; every clip plays | animator Opus H (Studio) | `ANIM/`, `RIG/export/`, `MOD/` | `ANIM/import-record.md` | C-50 | integrator for the imported revision (RP:54; JT:48) | no evidence found |
| C-49 | S7 wiring (only if `playable`) | feature-builder Opus H (Studio) | wiring contract, gameplay sheet, timing list, import record | code, tests, change manifest | reviewer | the server decides fairness (JC:987) | review with the `reviewer` is mandatory for code (CO:100) |
| C-50 | S7 candidate: freeze, evidence rows, captures | animator Opus H (Studio) | import record, `SH`, gameplay sheet, icons | `ANIM/captures/`, `D/evidence.md` | all reviewers | one frozen, revision-pinned candidate (CO:64) | no evidence found |
| C-51 | Review scripts: `model_audit.py`, `rig_audit.py`, section H rows present | qa-lead Opus M | `D/evidence.md`, `SH` | `D/reviews/candidate-r0-qa-lead.md` | other reviewers wait if it fails | scripts first, a FAIL stops the others (RM:13; JT:14) | the recipe also lists `clip_check.py` (JT:49); the script's step does not (grep `clip_check` in JC: none) |
| C-52 | Review: phone cost | performance-engineer Opus H (Studio); runs beside C-55/56 | candidate, game profile budgets | `candidate-r0-performance-engineer.md` | repair | on-screen count and phone cost (JT:49) | without a phone the phone line is BLOCKED (JC:1028) |
| C-53 | Review: variant parity PF-13 (risk `sold-variant`) | qa-lead Opus M (Studio) | evidence, base rig, `SH`, `D/design/` | `candidate-r0-pf13.md` | repair | a sold variant changes no stat, hit box or socket (JT:51) | G3P:104 |
| C-54 | Review: code (only if `playable`) | reviewer Opus H | evidence, wiring contract, code files | `candidate-r0-reviewer.md` | feature-builder | every candidate with code has the reviewer (CO:100) | CAP:50 (K2) argues reviews can lose correct work, so it is read-only |
| C-55 | Review: identity, silhouette, value at game camera | art-director Opus M; first of two sequential creative reviews | captures, icons, reference set | `candidate-r0-art-director.md` | C-56 | JT:49 | no evidence found |
| C-56 | Review: role reads in play | game-designer Opus H | same | `candidate-r0-game-designer.md` | readiness, G3 | JT:49 | no evidence found |
| C-57 / C-58 | Event capture + live-ops review (risk `event`) | studio-operator Sonnet M; live-ops-designer Opus M | candidate, job card | capture set; `candidate-r0-live-ops-designer.md` | readiness | JT:123 | +2 runs per review round |

Build totals: 19 runs non-playable, 21 playable, depth 16 (17 playable). Parallel runs in the whole build: Par F (2), Par G (modeler icons next to the VFX-then-sound lane), and in the review chain perf (and code reviewer) beside the art-then-design lane (JC:1078-1083).

### 2.5 How the review chain and its repairs run (JC:1049-1207)

1. Round r: qa-lead scripts (C-51). If it has a blocking finding, nothing else runs this round.
2. Else: perf (C-52) in Studio, the reviewer (C-54, playable), and art then design (C-55, C-56) in sequence, all at the same time.
3. Blocking findings split into code (maker feature-builder, 3 rounds) and other (2 rounds). After the limit the stage returns `needs-decision` to the lead.
4. Repair round: each named maker runs once, in pipeline order (art-director, game-designer, modeler, rigger, animator, vfx, sound, then architect, feature-builder). Then the receivers recheck: modeler changed -> rigger rechecks (S4 and K5 again); modeler or rigger changed -> animator rechecks (S6 again). Then the animator refreezes the candidate and recaptures (REFREEZE). Then the next review round starts at step 1.
5. Cost: a one-maker (modeler) repair round is +8 runs (27 vs 19 measured: fix, rigger recheck, animator recheck, refreeze, then 4 reviewers). A round that names all 7 makers is 7 fixes + 1 refreeze + 4 reviews = 12 (the recheck runs are skipped because the rigger and animator already fixed).

### 2.6 Repair stage (workflow call 4, after G3 change request)

| Id | Step | Who | Runs |
| --- | --- | --- | --- |
| C-R1 | scope: map the owner's change to affected makers, say if the sheet or timing list moves, flag new scope | art-director Opus M (JC:1212) | 1 |
| C-R2 | repair round 0: only affected makers, receivers recheck, refreeze | named makers; same as 2.5 step 4 | 1 maker + rechecks |
| C-R3 | full review chain on the new candidate (scripts, perf, art, design, +reviewer, +pf13, +event) | as C-51..56 | 4 minimum |

Measured: 6 (art-director only), 9 (modeler), 37 (all 7 makers, all review rounds). Why: OS:20, GF:72-73 (a G3 note reopens only the affected layers). No evidence found of what a full re-review adds over a partial one.

### 2.7 Exchange and note rounds in detail (character)

| Round | Between | Limit | Extra runs per round | Source |
| --- | --- | --- | --- | --- |
| D2 | 4 direction leads | 1 (+ D3 resolution 1) | 4 (+1) | CO:130 |
| Reference answer | modeler -> art-director | 1 | +1 | JC:579-594 |
| K1 | rigger checks, animator answers | 2 | +2 (animator fix, rigger recheck); max +4 | JC:612-632 |
| K2 | animator checks, rigger answers | 2 | +2; max +4 | JC:648-668 |
| S3 counter | modeler counters, rigger answers, modeler rebuilds | 1 | +2 | JC:750-764 |
| S4 | rigger checks, modeler fixes | 2 | +2; max +4 | JC:796-820 |
| S6 | animator checks, rigger triages (rig fix, or modeler fix + rigger rebind) | 2 | +2 (rig fix) or +4 (geometry route); max +8 | JC:838-881 |
| Review repairs | makers named by findings | 2 (code 3) | see 2.5 | CO:132 |
| Proof review repairs | makers named by findings | 2 | fixes + rigger re-pose + lineup | JC:1154-1171 |

If a note round ends unaccepted, the stage returns `failed` (JC:346-348). A rigger "design question" route, or a K2 "not supported" that changes the look, returns `needs-decision` for the owner (JC:340, :347).

### 2.8 Modes and risk tokens (counts measured with the harness)

| Case | Direction | Proof | Build | Notes |
| --- | --- | --- | --- | --- |
| Base (not variant, not playable) | 12 | 15 | 19 | section 1 |
| Playable | 12 | 16 | 21 | +wiring contract, +wiring, +reviewer per review round |
| Risk `new-enemy` | 14 | 15 | 19 | +2 in direction (C-14, C-15); needs `studioId` in direction (JC:83) |
| Risk `event` | 12 | 15 | 21 | +2 per review round (JC:1085-1103) |
| Variant, palette only, no new moving parts | 12 | 10 | 10 | skips C-21 sound plan, C-23..26 (S1-K2), S4-S6, S7 clips, VFX and sound (JC:595-596, :792-795, :887, :946); wiring still runs if `playable` |
| Variant, new moving parts at S0 | 12 | 14 | - | S1-K2 run for the new parts only |
| Variant, geometry changed, no new parts | 12 | 10 | 13 | adds S4, S5, S6 |
| Variant, geometry changed + new parts | 12 | 14 | 17 | adds S7 blocking, check-ins, polish |
| Variant, risk `sold-variant` | - | - | +1 per review round | PF-13 (JC:1029-1034) |
| Variant, maximum | 13 | 41 | 54 | measured with all 5 variant makers, geometry + new parts + sold-variant |

Variants never run the VFX and sound passes, even when new moving parts exist (JC:946); the recipe row does not say this (JT:51).

### 2.9 Maximum composition (character L, non-playable, non-variant): 116 runs

- Direction 13 = 12 + 1 resolution.
- Proof 46 = 15 + 1 reference answer + 4 (K1: 5 runs instead of 1) + 4 (K2: 5 instead of 1) + 6 (two extra review rounds of 3 reviewers) + 16 (2 repair rounds x (7 fixes + 1 lineup retake)).
- Build 57 = 19 + 2 (S3 counter round) + 4 (S4 note rounds) + 8 (S6 note rounds with the geometry route) + 8 (two extra review rounds of 4) + 16 (2 repair rounds x (7 fixes + 1 refreeze)).
- With `playable`: the proof max is 51 and the build max is 72, because code findings get 3 repair rounds (4 review rounds in total) and the architect and feature-builder join every repair round.

### 2.10 M versus L (character)

| Item | L | M |
| --- | --- | --- |
| Stage calls | direction, proof, build | direction, build (`proof` refuses size M: JC:78) |
| Steps run | C-01..15 / C-16..32 / C-33..56 | the same, in the same order; `build` runs C-16..32 and then C-33..56 in one call (JC:1245-1252) |
| Owner sees the proof | at G2, before the build | at G3 only (CO:27: "the proof runs inside the build and is shown at G3") |
| After the proof | big shapes (layout, proportions, timing beats) frozen by G2 (OS:58) | no freeze point; a fault in the proof is found after the build ran |
| Image batch for the reference set | between `proof` and `build` | between `direction` and `build`: the first two runs of `build` return `blocked` if it is pending (harness: 2 agents) |
| When to use | a new look, or several crafts with separate outputs (CO:28) | one output inside an approved style (CO:27); a look change is sized L (RM:22); several forms count once per form (OS:15) |
| Agent runs at minimum | 46 | 46 |

### 2.11 Walk-through of one L character job, request to G3 (for a non-technical reader)

1. You tell the lead what character you want, in your own words. 2. The lead writes your words on a job card, calls the job "large" because it is a new look, and names the art director as the job lead. 3. Four specialists each write a short idea alone: the game designer says what the character does in play, the art director draws two or three looks, the rigger says what will be hard to move, and the animator says what must move. 4. They read each other's notes once, list only the conflicts that would change the work, and the art director merges everything into one direction sheet that three of them sign (12 agent runs). 5. The lead shows you two or three looks in grey and black-fill at phone size, with one recommendation, and you pick one: that is Gate 1. 6. Before anything is built, the team writes down what each craft needs from the others: extra views of the picture, a table of game timing, a skeleton sheet where the animator says what must move and the rigger says how to build it, a sound plan, and the modeler's check of the picture for gaps. 7. They then make a cheap proof: a rough blocky body at player size, a stick skeleton, and the signature pose in Studio at the game camera beside other characters; the art director, animator and game designer look at it first, then you say yes or no: that is Gate 2, and after it size, pose and plan stop moving. 8. The build runs in a fixed order: the modeler makes the final parts, the art director checks them on the real background before textures are finished, the rigger tests the seams and builds and tests the real skeleton in Blender and Roblox, the animator checks it can reach every pose and makes the clips and a timing list, and the effects and sound artists build to that list. 9. The animator then imports everything into Studio, freezes one version and takes the pictures. 10. Scripts check the numbers first, then the performance engineer, art director and game designer review, and any problem goes back to the maker who owns it, for at most two rounds. 11. The lead checks that every claim has evidence and shows you the character working in Roblox: that is Gate 3, and a change request reopens only the crafts it touches. 12. In the best case this is 46 agent runs, and the longest chain of runs that each wait for the one before it is 32 runs long.

## 3. Stage job (level, hub, lobby, arena, world area)

Recipe: JT:53-66. Script: JS. Decision rights: routes, cover, sight lines and blocking surfaces belong to the game-designer; look to the art-director; budgets to the performance-engineer; the built place to the environment-designer (JT:57; CO:43; DJ:69 -> R02:454-460, R09:606-622).

### 3.1 Lead and owner steps

Same as 2.1, with two differences. (1) The G1 packet must show the blueprint draft, and the approval line for the blueprint revision must be in `decisions.md` before the greybox: `proof` and the greybox return `blocked` without it (JS:526, :629). (2) `risks` accepts only `event` (JS:43). Why the blueprint gate: first-game practice, "owner approves the blueprint before building" (J8B:20; ED:70; JS:133).

### 3.2 Direction stage -> G1

| Id | Step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-01 | D1: route graph draft, 2-3 layouts with route times, route table, hazard sheets | game-designer Opus H; Par A (4 runs T-01..04) | job card, game profile, art bible, direction-sheet template | `D/direction/proposal-game-designer.md` | T-05, T-09 | the game-designer decides routes first; layouts come before art (JT:57-58; DJ:69; RX:43) | no evidence found for this call alone |
| T-02 | D1: 2-3 key-place reference images, value bands | art-director Opus M (images); Par A | same | `proposal-art-director.md`, `D/direction/image-prompts.md`, `content/art/refs/` | T-05, T-09 | JT:58 | no evidence found |
| T-03 | D1: set list, landmarks, built-where, ambience idea, own blueprint sketch (Blender stills) | environment-designer Opus H; Par A | same | `proposal-environment-designer.md`, `D/direction/env-stills/` | T-05, T-09 | JT:58 | no evidence found |
| T-04 | D1: budgets and capture recipe | performance-engineer Opus H; Par A | same | `proposal-performance-engineer.md` | T-05, T-09 | constraint owners state limits before design (JT:58, JT:129) | no evidence found |
| T-05..08 | D2 exchange | same 4; Par B | the other 3 proposals | `D/exchange/r1-<role>.md` | T-09 | CO:58 | not tested (DD:151) |
| T-09 | D3 synthesis + blueprint draft (DRAFT FOR G1) | environment-designer Opus H (Blender) | 4 proposals, 4 exchange notes, direction + blueprint templates, game profile | `D/direction.md` rev 1, `S/blueprint.md` rev 1 | T-10..12, G1 | the owner approves the blueprint before building (JT:59; J8B:20) | without it, nothing gives the greybox an approved layout (JS:526) |
| T-10..12 | D3 signatures: game-designer (every route edge kept), art-director (looks, elevations), performance-engineer (estimate vs budget) | Opus H / M / H; Par C | direction + blueprint | `D/direction/sign-<role>.md` | T-13 | CO:58 | no evidence found |
| T-13 | D3 resolution (only on refusal) | environment-designer Opus H | direction, blueprint, signs | next revisions | G1 | CO:130 | +1 run |

Direction totals: 12 runs, depth 4; +1 resolution. No `studioId` is needed in direction.

### 3.3 Proof stage (L only; inside `build` for M) -> G2

| Id | Step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-14 | P1 full route graph (10 node fields, 5 walk-throughs, 4 failure traces, route table, hazard sheets, read rank, sight lines and cover with ids) | game-designer Opus H | direction, approved blueprint, own proposal, `level-design/references/review-artifact.md` | `D/route-graph.md` rev 1 | T-15, studio-operator, qa-lead | the contract the greybox is built on (JT:60) | no evidence found |
| T-15 | P2 blueprint refinement, read plan, ambience map rev 1, kit-piece list + floor-material list | environment-designer Opus H | direction, approved blueprint, route graph | `S/blueprint.md`, `read-plan.md`, `ambience-map.md`, `kit-pieces.md` | T-16..20 | contract + a player-size scale reference in every space (JT:60); stops with `needs-decision` if an approved item changed (JS:614-616) | blocked without the G1 approval line (JS:551) |
| T-16 | Needs round: blueprint vs route graph; read plan vs route table | game-designer Opus H; Par H (T-16, T-17, T-18 and the T-19 -> T-20 chain run at the same time) | pins of route graph, blueprint, read plan, ambience map, kit list | `D/exchange/p1-game-designer.md` | merges T-21/22 | consumers state needs before the producer builds (JT:137) | see section 4 |
| T-17 | Needs round: buildability of each kit piece | modeler Opus H | same | `p1-modeler.md` | same | same | same |
| T-18 | Needs round: estimate per zone vs budget, stress scene | performance-engineer Opus H | same | `p1-performance-engineer.md` | same | same | same |
| T-19 | Needs round: ambience map, shared wind state | vfx-designer Opus H; first of the chain | same | `p1-vfx-designer.md` | T-20 | VFX writes first, sound answers (JS:575-583) | same |
| T-20 | Needs round: floor-material list and ambience map; answers on the VFX note | sound-designer Opus M; second of the chain | same + VFX note | `p1-sound-designer.md` | merges | sound can refuse a material for time (JT:66; RX:38) | same |
| T-21 / T-22 | Merge round (only if any note holds a conflict or a missing item): route items by game-designer, then the rest by environment-designer; round 2 repeats | game-designer Opus H; environment-designer Opus H | notes | route graph next rev; blueprint, read plan, ambience map, kit list next revs | greybox | game-designer decides routes (CO:43); what stays open after round 2 becomes a G2 question (JS:594, :604) | +2 runs per open round; a round-2 round adds 5 more needs runs |
| T-23 | P4 playable greybox + grey value pass (light direction chosen in grey), scene audit, ambience numbers | environment-designer Opus H (Studio, Blender) | blueprint, G1 approval line, route graph, ambience map | `S/greybox/`, `S/review/`, ambience map next rev | studio-operator, reviewers | cheap playable proof (JT:61; CAP:53 K5) | G3P:79 |
| T-24 | P5 playtest: walk times, first view, landmark read, multi-client | studio-operator Sonnet M (Studio) | greybox, route graph | `D/playtests/greybox-r0/` | reviewers | measured route times, not eyeballed (JS:263) | no evidence found |
| T-25 | Proof review: play | game-designer Opus H | playtest captures, camera set, audit | `D/reviews/greybox-rev0-game-designer.md` | T-26 | JT:61 | no evidence found |
| T-26 | Proof review: composition and value | art-director Opus M | same | `greybox-rev0-art-director.md` | T-27 | JT:61 | no evidence found |
| T-27 | Proof review: cost; writes the budget file | performance-engineer Opus H | same | `greybox-rev0-performance-engineer.md`, `D/perf/budgets.json` | G2 | JT:61 | no evidence found |

Proof totals: 12 runs, depth 9 (route graph, blueprint, the VFX-then-sound needs chain, greybox, playtest, 3 reviews in sequence). Repairs go to makers by role (file makers first, environment-designer last as Studio driver) with a new playtest each round after round 0 (JS:643-665). Maximum measured: 39 (two open interface rounds, 5 makers named in two repair rounds), 47 if every play-change and material hand-back is refused.

### 3.4 Build stage -> G3

| Id | Step | Who (model, effort; group) | Reads | Writes | Hands to | Why it exists | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-28 | B1 art blockout snapped to the greybox; reports play-affecting changes | environment-designer Opus H (Studio, Blender) | greybox at the approved revision, blueprint, route graph, kit list, images | place in Studio, `S/review/`, kit list | T-29 | art stays inside the approved greybox (JT:62; RX:43) | no evidence found |
| T-29 | Playtest (blockout) | studio-operator Sonnet M | place, route graph | `D/playtests/blockout-r0/` | T-30 | playtests continue during art (JT:62; CAP:53 K5) | no evidence found |
| T-30 | Check-in: game-designer on placement, routes, landmarks | game-designer Opus H | playtest, place captures, route graph | `D/reviews/checkin-blockout-r0-game-designer.md` | repair loop | the game-designer is "embedded" (JT:63; RX:44 -> R02:460-470: without check-ins the result is mediocre) | no evidence found |
| T-31 | Check-in: art-director paint-over on first rough art (paint-over image batch can be pending) | art-director Opus M (images) | `S/review/`, read plan, direction | `D/reviews/checkin-paintover-r0-art-director.md`, `D/art/paintover/` | environment-designer | JT:63; RX:51 (paint-over is the review style) | a pending batch stops the stage (JS:423) |
| T-32 | B2 kit pieces, one run per piece, one after the other (only if K > 0) | modeler Opus H (Blender); lane 1 of Par I | kit list, blueprint, direction, art bible | `content/models/<id>/` | environment-designer | kit pieces from the modeler (JT:62) | +K runs; a pending model sheet stops the stage (JS:739) |
| T-33 | B2 art production inside the greybox (terrain, assembly, dressing) | environment-designer Opus H (Studio); lane 2 of Par I | greybox, blueprint, read plan, floor-material list, paint-over | place revision, `S/review/` | T-34, T-35 | JT:62 | no evidence found |
| T-34 | B2 place kit pieces (one round trip first) (only if K > 0) | environment-designer Opus H (Studio, Blender) | `content/models/<id>/`, kit list | place revision | check-in | stand-ins replaced | +1 run |
| T-35 | Playtest (art) | studio-operator Sonnet M | place | `D/playtests/art-r0/` | T-36 | JT:62 | no evidence found |
| T-36 | Check-in: game-designer on materials, dressing, space plays well enough for light | game-designer Opus H | playtest, captures | `checkin-art-r0-game-designer.md` | repair loop | lighting only after the space plays well (JT:62) | no evidence found |
| T-37 | B3 2-3 grey lighting variants with `look_check.py` numbers | environment-designer Opus H (Studio) | grey value pass, read plan, direction | `S/review/light-variants/` | T-38 | art-director sees the light before the pass (JT:63; G3P:86: the art-director first saw stage light at the final review) | G3P:86 |
| T-38 | Check-in: art-director picks a variant | art-director Opus M | variants | `checkin-light-variants-r0-art-director.md` | T-39 | JT:63 | G3P:86 |
| T-39 | B3 light, atmosphere, sky; low and high quality camera set | environment-designer Opus H (Studio) | direction, pick, review captures | place revision | T-40 | JT:62 | no evidence found |
| T-40 | B4 ambient VFX specs from the ambience map | vfx-designer Opus H | ambience map, review captures | `content/vfx/<stage>-ambient/` | T-41, T-42 | JT:62; one wind state (JS:800) | no evidence found |
| T-41 | B4 ambience sound against the map and the VFX specs | sound-designer Opus M | ambience map, VFX specs | `output/sound/<stage>-ambience/` | T-42 | same | no evidence found |
| T-42 | B4 place sources and effects; map vs place check | environment-designer Opus H (Studio) | sound and VFX specs, map | place revision, `audit.json` | T-43 | JS:825-834 | no evidence found |
| T-43 | Playtest (ambience) | studio-operator Sonnet M | place | `D/playtests/ambience-r0/` | T-44 | JT:62 | no evidence found |
| T-44 | Check-in: game-designer on VFX placement and cue readability | game-designer Opus H | playtest | `checkin-ambience-r0-game-designer.md` | repair loop | JT:63 | no evidence found |
| T-45 | Freeze: environment-designer reviews own work, writes review packet, evidence rows, protected list | environment-designer Opus H (Studio, Blender) | reviews, ambience map, budgets | `S/review-packet.md`, `D/evidence.md` | T-46 | one frozen revision-pinned candidate (CO:64) | no evidence found |
| T-46 | Recorded playtest with the art-director's named captures (layer cuts, environment-only, lowest graphics, landmark mask) | studio-operator Sonnet M | evidence, packet | `D/playtests/candidate-record/` | reviewers | JT:65 | no evidence found |
| T-47 | Review scripts: scene audit, budgets, floating parts (run by studio-operator) | studio-operator Sonnet M (Studio) | evidence, map, `budgets.json` | `D/reviews/candidate-r0-scripts/` | T-48..54 wait on a FAIL | scripts first (RM:13) | no evidence found |
| T-48 | Review: collision, falls, stuck spots, ledges vs jump height, diff vs greybox probe, graphics levels, spawns | qa-lead Opus M (Studio); Par J lane 1 (with T-49) | candidate, record | `candidate-r0-qa-lead.md` | repair | JT:65 | no evidence found |
| T-49 | Review: frame time and memory in the stress scene | performance-engineer Opus H (Studio); Par J lane 1 (after T-48) | same | `candidate-r0-performance-engineer.md` | repair | recipe's Review order row names no performance-engineer; the general rule does (JT:14, JT:65) | no evidence found |
| T-50 | Review: play | game-designer Opus H; Par J lane 2 | same | `candidate-r0-game-designer.md` | T-51 | play wins over art readability (JT:65) | no evidence found |
| T-51 | Review: camera set + layer cuts + mask | art-director Opus M | same | `candidate-r0-art-director.md` | T-52 | JT:65 | no evidence found |
| T-52 | Review: ambience, map vs place | sound-designer Opus M | same | `candidate-r0-sound-designer.md` | T-53 | JT:65 | no evidence found |
| T-53 | Review: ambient effects | vfx-designer Opus H | same | `candidate-r0-vfx-designer.md` | readiness | the recipe has one "sound and VFX ambience check" (JT:65); the script runs two reviewers | no evidence found |
| T-54 | Review: event E-01..E-19 (risk `event`) | live-ops-designer Opus M | event capture set | `candidate-r0-live-ops-designer.md` | readiness | JT:123 | +1 per review round |

Build totals: 24 runs, depth 22 (25 with K=3 pieces). Cost split: the five check-ins use 8 of the 24 minimum runs (3 Sonnet playtests T-29, T-35, T-43; 3 game-designer reviews T-30, T-36, T-44; 2 art-director reviews T-31, T-38); the final chain T-47..53 uses 7. After a repair the stage refreezes with T-45 and T-46 again (JS:941-942).

Check-in loop (JS:381-430): a check-in is a playtest (Sonnet) + a review (Opus). On a blocking finding the makers named repair, then the playtest and the review run again; at most 2 repair rounds, then `needs-decision`. A game-designer check-in therefore costs 2 runs clean and up to 16 at maximum (3 x 2 + 2 x 5 makers); an art-director check-in has no playtest and costs 1 clean and up to 13.

`returnPaths` (JS:274-331): after each environment build step, any change to a route edge, opening, cover, sight line, blocking surface or collision goes to the game-designer (accept or refuse; a refusal makes the environment-designer restore), and any surface material not on the floor-material list goes to the sound-designer (accept or refuse; a refusal makes the environment-designer swap). Each hand-back that lists items costs +2 runs, +4 if refused. These are empty in the minimum case.

### 3.5 Repair stage

Scope (environment-designer Opus H), then the named makers (game-designer first, file makers, environment-designer last), freeze + recorded playtest, and the full review chain. Measured: 11 (environment only), 12 (game-designer and environment), 43 maximum.

### 3.6 Exchange and repair rounds (stage)

| Round | Between | Limit | Runs | Source |
| --- | --- | --- | --- | --- |
| D2 | 4 direction leads | 1 (+ resolution 1) | 4 (+1) | CO:130 |
| Interface rounds | 5 consumers -> producers | 2, then a G2 question | 5 minimum (T-16..20), +2 merge runs per open round; two open rounds = 14 | JS:564-612; CO:131 |
| Check-ins | 3 game-designer and 2 art-director check-ins vs environment | 2 repair rounds each | game-designer 2 clean, 16 at maximum; art-director 1 clean, 13 at maximum | JS:381-430 |
| Proof review | design -> art -> perf | 2 repair rounds | 3 + fixes + 1 playtest per round > 0 | JS:642-667 |
| Final review chain | scripts, then qa and perf (Studio, one after the other) beside design -> art -> sound -> vfx | 2 repair rounds | 7 per round (8 with event) + fixes + freeze 2 | JS:891-944 |

Maximum composition (stage L, no play-change or material hand-backs): direction 13 = 12 + 1 resolution. Proof 39 = 12 + 9 (two open interface rounds: 14 runs instead of 5) + 2 playtests (rounds 1 and 2) + 6 (rounds 1 and 2 reviewers) + 10 (2 repair rounds x 5 makers). Build 118 = 24 + 42 (three game-designer check-ins at +14 each) + 24 (two art-director check-ins at +12 each) + 14 (two extra review rounds of 7) + 14 (two repairs of 5 fixes + 2 freeze runs). Add K kit pieces + 1 for placing. With every play-change and new-material hand-back refused, proof is 47 and build 198 (ceiling 258 for the three calls).

### 3.7 M versus L (stage)

| Item | L | M |
| --- | --- | --- |
| Stage calls | direction, proof, build | direction, build (`proof` refuses size M: JS:58) |
| Steps run | T-01..13 / T-14..27 / T-28..54 | the same; `build` runs T-14..27 and then T-28..54 in one call (JS:999-1004) |
| Owner sees the greybox | at G2 | at G3 only |
| Blueprint approval | at G1, line in `decisions.md` before the greybox | same: `proof` and the greybox return `blocked` without it, in M too (JS:526, :629) |
| Where a pending image batch stops it | `build`, at the paint-over or a kit model sheet | same, plus the key-place images are required for `build` in both (JS:56) |
| Agent runs at minimum | 48 | 48 |

## 4. The needs and interface steps in detail

The owner's words (J023-D2): "it might be important for the four crafts to come back together to kind of say what they need." Below is what the two scripts and the recipes do today.

### 4.1 Character: modeler <-> rigger <-> animator, and sound, VFX

Order of the interface steps, with files:

1. C-16 art-director -> modeler, rigger, animator: the reference set (views, anchors, material intent). C-17 game-designer -> animator, rigger: the gameplay sheet.
2. C-18 rigger opens `SH` section A.
3. C-20 modeler -> art-director: reference check (iconic qualities, gaps with the choice made, material intent per region, missing views). The art-director answers in C-22 (1 round). The modeler makes no statement about the rig here.
4. C-21 sound-designer reads the character card, writes `SND/sound-plan.md`. Declared consumers are animator and vfx-designer (`JC:569`), but the animator's S1 inputs (`JC:603`) and the vfx-designer's S7 inputs (`JC:952`) do not list it. Only the animator's blocking step (`JC:894`) and the sound-designer's own S7 step (`JC:960`) read it.
5. C-23 animator -> rigger: section B (what moves, ROM with unit and source, contacts, held tools, stress poses, sockets needed) and `motion-profile.md`.
6. C-24 rigger checks the needs (K1). The animator answers in up to 2 rounds.
7. C-25 rigger -> animator, modeler: section C (route per region, joints, cuts, hide method), budgets, test plan, marked-up renders. C-26 animator signs (K2). The rigger revises in up to 2 rounds.
8. C-27 modeler builds the blockout split along the rig's cuts (first time the modeler uses the rig plan). C-28 rigger poses the proxy rig on it.
9. After G2: C-33 modeler accepts or counters each cut (1 round, rigger answers), builds, then the rigger accepts the geometry (C-38, up to 2 fix rounds), builds the rig (C-39), and the animator accepts the rig (C-40, up to 2 note rounds).
10. After the clips: C-44 timing list -> C-46 VFX writes envelopes -> C-47 sound keys to the VFX scripts. VFX and sound are first told the timing list here.

Findings:
- The recipe's cross-type rule says a craft that keys from another's output "is consulted at direction or at the needs round, not after the build" (JT:137). In the character job VFX is consulted after the clips exist (C-46) and is not a direction lead (JC:356-375; JT:40). G3P:80 lists the "character needs round" for sound only.
- No step has the modeler, rigger, animator, sound-designer and vfx-designer read one draft contract together. The exchanges are pairs: animator <-> rigger (C-24, C-26), modeler -> art-director (C-20), rigger <-> modeler (C-33/34, C-38), animator <-> rigger (C-40). Searched `job-character.js` phases and every `parallel(` call: not found.
- The modeler states its needs in writing only for the picture (C-20) and for each cut at S3 (after G2). The rig plan is given to the modeler at C-25 (before G2) but the modeler's counter is allowed at C-33 (after G2). The rig sheet's section B has "sockets needed" (JC:602), which is the only place effects attachment is asked from the rigger before S7.
- Pending-image rule: if C-20 asks for views and they are pending, the stage stops (`JC:593`).
- Tripo: no step, arg or word in either script handles it (grep `tripo` in JC and JS: none). Rules sit in `TR:1-44` and `modeling-craft/SKILL.md:17,29`: the modeler picks hand or Tripo at its step, writes an input pack, and the owner runs Tripo (J007-D4). A workflow cannot pause for the owner (RM:10), so a Tripo-source character cannot fit inside one `build` call without a manual hand-run step. S3's brief says "Build the final model" and "Work on a copy; the source snapshot stays untouched" (JC:737, :747).

### 4.2 Stage: environment <-> game-designer routes; sound and VFX needs

Order of the interface steps:

1. T-03/T-01: environment-designer and game-designer each propose alone; T-09 lays the environment sketch on the game-designer's route graph. Where they disagree, the route graph wins and the difference becomes a decision record the game-designer owns (JS:478).
2. T-14 game-designer -> environment-designer: route graph with node fields, route table, hazard sheets, read rank, ids for every sight line and cover that must hold.
3. T-15 environment-designer refines the approved blueprint; a layout change is "a proposal to the game-designer, never a silent edit". Changes to approved items go in `approved_items_changed`; a non-empty list stops the proof before the greybox (JS:614-616).
4. T-16..T-20 needs round, in parallel except the VFX -> sound chain:
   - game-designer: blueprint vs route graph; read plan vs route table, hazard sheets, read rank (JS:558).
   - sound-designer: the floor-material list before any material is built (footstep and impact set per walkable material, or refuse one that costs more time than the job has) and the ambience map (JS:559).
   - vfx-designer: the ambience map, what moves and its visible cause, the shared wind state, the quiet space that must stay readable (JS:560). It writes first; sound answers on its note (JS:575-583).
   - modeler: each kit piece buildable at its size, pivot, collision and budget (JS:561).
   - performance-engineer: estimate per zone vs budget and the stress scene (JS:562).
5. Merge: route items first by the game-designer (route graph next revision), then everything else by the environment-designer (blueprint, read plan, ambience map, kit list with a refused material replaced). At most 2 rounds; what stays open becomes a G2 question (JS:592-612).
6. During the build the interface continues through hand-backs: every environment build step reports play-affecting changes (to the game-designer) and new surface materials (to the sound-designer), each of which can force a restore or a swap (JS:274-331). The game-designer also checks after each build phase with playtest evidence (JS:381-403). The QA step diffs collision and cover against the approved blockout (JS:878).
7. B4 repeats the VFX -> sound order for ambience (JS:800-822); the environment-designer places both (JS:825-834).

Findings:
- The stage script holds the one real "come back together" round: five consumers state needs against the same pinned contract revisions, with a merge, up to twice. The recipe has no "Interfaces" row for a stage (JT:53-66 has rows for contract and proof only); the round comes from the cross-type rule (JT:137) and the script.
- The animator and the character-rigger have no place in the stage job; character needs rounds are in the character job.
- The needs round happens in `proof`, before the greybox. The kit-piece builders (modeler) get a buildability check but not the art look; model sheets are made later per piece (JS:717).

## 5. Where the hand-run recipe and the saved script differ

### 5.1 Character

| Topic | Recipe / rig-pipeline says | Saved script does | Source |
| --- | --- | --- | --- |
| Gameplay sheet | not named; windows come from the "gameplay owner" | a game-designer step writes `design/gameplay-sheet.md` in the proof | RP:20; JC:508-518 |
| S0 owner | the lead | the rigger runs S0 "on the lead's behalf" | RP:47; JC:530 |
| rigger and animator in direction | one row "character-rigger + animator" | two proposals, two exchange notes, two signatures | JT:40; JC:367-375, :424 |
| S7 blocking check-ins | recipe names only the art check-in before texture polish | adds an art-director and a game-designer check-in on blocking, copied from the cutscene script | JT:47; JC:901-922 |
| Review scripts | `model_audit.py`, `rig_audit.py`, `clip_check.py` | a qa-lead agent runs the first two and checks section H rows; `clip_check.py` is not in its brief | JT:49; JC:1020-1022 |
| Consumer K-checks | step in the review order | inside the build steps; the review checks that their rows exist | JT:49; JC:1021 |
| Icon renders | "UI icon renders", owner unnamed | the modeler | JT:46; JC:937-944 |
| Variant | "skip S1 unless new moving parts"; palette-only skips S4-S6 | also skips K1, S2, K2, the sound plan, S7 clips and VFX/sound unless new parts; VFX/sound never run for a variant | JT:51; JC:595-596, :887, :946 |
| Tripo route | rig-pipeline carries the rules | not in the script | TR; section 4.1 |
| Sideways messages | agents can message by id and be resumed (`SendMessage`) | no ids; every note round is a fresh call that rereads context; sideways work only through files | CO:77-79; JC:181 |
| Repairs | "resume a hand-spawned maker by id" | fresh call with finding files and protected list | OS:66; RM:14 |
| Recapture after repair | refreeze before the next review | REFREEZE (animator, Studio) after any non-art maker changed | JC:1194-1204 |
| Image pending | lead runs the batch | stage returns `blocked` after the reference set and again after the reference check | RM:11; JC:524, :593 |
| Animator effort | role default medium | high for all 11 animator calls, including import, candidate, recheck and refreeze | `.agents/roles/README.md:14,40`; JC:102 |

### 5.2 Stage

| Topic | Recipe says | Saved script does | Source |
| --- | --- | --- | --- |
| Interfaces | no row for a stage | a needs round with 5 consumers, 2 rounds, 2 merge runs per open round | JT:53-66; JS:557-612 |
| Review order | scripts -> game -> art -> "sound and VFX ambience check" -> qa-lead | scripts by studio-operator; then qa + perf in Studio beside design -> art -> sound -> vfx; the recipe's row names no performance-engineer | JT:65, :14; JS:875-945 |
| Check-ins | game-designer "as the build grows"; art-director before light | 3 game-designer check-ins and 2 art-director check-ins, each preceded by a Sonnet playtest (the 2 art-director ones have no playtest) | JT:63; JS:690-841 |
| Freeze | integrator assembles one frozen candidate | a self-review step with a review packet, then a Sonnet recorded playtest; repeated after each repair | JT:64; JS:850-873, :941-942 |
| Kit pieces | modeler builds kit pieces | one modeler run per piece in series; each piece needs a model sheet batch | JT:62; JS:703-722 |
| Blueprint gate | blueprint draft shown at G1 | `proof` and the greybox return `blocked` without the approval line in `decisions.md` | JT:59; JS:526, :629 |
| Studio drivers | one Studio user at a time | enforced in the harness; the modeler in Blender can run beside the environment-designer in Studio | CO:135; JS:701 |

### 5.3 Both

- Hand-run: the lead's chat spawns every craft and a subagent job lead may draft briefs (CO:95). Saved script: the script builds each brief from one template (`brief()`), and the job lead is just an agent in the step that names it.
- Hand-run `M`: the recipe skips `proof`; script `M build` runs `proof()` then `production()` in one call with no pause for the owner between them (OS:18; RM:22; JC:1245-1252).
- The lead's belief check (OS:14), the job card, `crew.md` upkeep and close-out are not in either script.
- Owner gate packets, image budgets and the "doors closed" rows (GF:14-21, GF:55-64) are lead work, not workflow work.

## 6. Not found / could not map

- Real token or time costs per step: no run of either workflow exists in the repo, so only agent-run counts and depth are measured. The J023 job card figure for a cutscene run (24 runs, about 200 M tokens) is the only usage number found (`job-card.md:25`).
- Which docs pages and skill references each agent reads inside its step: the briefs name them (BASE_RULES) but their size was not summed.
- The exact `templates/` contents (direction sheet, rig sheet, fix note, review) and each role file's own steps: not read; only what the scripts and recipes cite.
- Whether any role's `SendMessage` allowlist change affects these two flows: not checked.
- Evidence of what breaks if a step is removed: only design-time sources exist (Riot transcripts, owner papers, first game, J005 teddy test). Steps marked "no evidence found" have none.
