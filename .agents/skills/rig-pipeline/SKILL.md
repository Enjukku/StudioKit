---
name: rig-pipeline
description: Shared workflow and rig sheet for anything rigged and animated in Roblox - who decides what among animator, rigger and modeler, stages S0-S8, one exact fix note, Tripo routes. Use at the start of any rig or animation job, when a rig "breaks" (seams, stretching, body skews when the head moves), when a Tripo model must be rigged, or when roles disagree about a cut or joint.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Owner-approved workflow (J005-D1, 2026-10-21). Evidence: `knowledge/reference/rigging/` (rigging paper notes 01-02, fact-checks), `knowledge/reference/animation/` (animation paper notes), first-game owner experience (EXPERIENCE, cited by decision id). Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the standard motion needs at K1 and K2, the design-for-motion screen and posed plan at S2, numbers-first S4, the read controls at S6, §8; repair round 2: the `cap` group in K3; repair round 3: one `cap_<cut id>` group per cut).

# Rig pipeline: animator → rigger → modeler → rigger → animator

## 1. Who decides what
Each role decides what it knows best. The others state needs, never methods (`rules/messages.md` §1).

| Role | Decides | Never decides |
| --- | --- | --- |
| animator | what must move, how far (range of motion, ROM, with units), how (active / passive / rigid / mechanical), contacts, held tools, stress poses, clip list, event timing inside gameplay windows | joint layout, cut lines, topology |
| character-rigger | rigid / skinned / mixed per region, joints, bones, pivots, axes, the controls (including the read controls, `rigging-design/references/design-for-motion.md` §2), which parts must be separate, where cuts go and why, deformation zones, Tripo route, every rig test | how a cut is built or hidden, motion style |
| modeler | how each cut is made, capped and hidden; re-modelling; retopology; UVs and texture re-bake; counter-proposals for a better cut or build | joint plan, ROM |
| lead | opens the sheet, routes notes, settles what it can, sends design trade-offs to the owner | craft |
| owner | look, feel, any design change a technical limit forces, G2 and G3 | — |
| gameplay owner (designer, config) | gameplay windows: startup, active, recovery, cancel | animation craft |

A disagreement between roles is settled by a **posed proxy test** (render both options at the pose that matters), not by argument. A creative trade-off goes to the owner with both options rendered.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The rig sheet to copy for a new asset | `templates/rig/rig-sheet.md` |
| The fix-note format (rigger → modeler, animator → rigger) | `templates/rig/fix-note.md` |
| The brief the modeler receives at S3 | `references/modeler-handoff.md` |
| Tripo routes, Tripo tool facts and versions | `references/tripo-routes.md` |
| How to judge rigid vs skinned, joints, seams (rigger craft) | `rigging-design` skill |
| Design for motion: the screen, the read controls, push routes, the posed plan | `rigging-design/references/design-for-motion.md` |
| Platform limits and their sources | §6 below; `knowledge/reference/rigging/fact-check-roblox.md` |

## 3. Stages and the check between each
```
S0 lead intake ─► S1 animator: motion needs ─► S2 rigger: rig plan ─► K2 animator signs "plan covers needs"
 ─► S3 modeler: cuts + geometry ◄─ counter-proposal (one round) ─► rigger
 ─► S4 rigger: geometry acceptance ─ fail: ONE fix note ─► S3 (max 2 rounds, then failed → lead)
 ─► S5 rigger: rig + tests (Blender + Roblox) ─► S6 animator: rig acceptance ─ fail: ONE rig note ─► rigger
 ─► S7 animator: animate, export, Roblox, timing list ─► S8 owner G3 on the imported revision
 rig problem found in S7 ─► rig note to rigger (rigger triages: rig fix / geometry note to modeler / design → lead → owner)
```

| Stage | Owner | Does | Writes (sheet) | Check before the next stage (the receiver runs it) |
| --- | --- | --- | --- | --- |
| S0 intake | lead | Confirms the approved reference image (`reference-images` skill) and the model source; purpose, camera, device, on-screen count; copies the sheet to `content/rigs/<asset-id>/rig-sheet.md`; snapshots the source | §A | K0: reference approved (decision line); purpose and runtime driver known or UNKNOWN; source snapshot saved and never edited |
| S1 motion needs | animator | Studies the whole body from multi-view renders (front, back, both sides, ¾, gameplay camera); writes its motion profile; then the rig needs | §B animator keys | K1 (rigger): every visible part has a record, also "does not move"; every ROM has a unit, the pose or clip that needs it and a source (reference, owner, PROPOSAL); contacts and held tools declared; the standard needs answered (shoulders and hips for wind-ups, the head through a spin, hand or finger shapes, every hook-shape part: needed with its pose, or not needed); stress poses include costume near joints; no invented mass or delay numbers |
| S2 rig plan | rigger | Inspects geometry (objects, connected parts, fused bridges, open edges, triangles, materials, UVs) and the concept's material intent; screens the design for motion (§8); picks a route per region with the reason; joint plan with the read controls; cut list with why; deformation zones; push routes; budgets; test plan; marked-up renders of cuts and zones (back and game camera included); the posed plan at the game camera (`rigging-design` §3 step 10) | §C rigger keys, §E, §F | K2 (animator): every §B record has an answer: supported / supported with limit / not supported + alternative, including shoulder and hip controls, a way to hold the head's world orientation through a spin, finger or hand-shape controls where hands must read, and control of every hook-shape part. Animator signs. A "not supported" that changes the look → `needs-decision` → lead → owner |
| S3 geometry | modeler | Per cut: accept or counter (names the §B/§C rows the counter still meets; one round with the rigger). Cuts, caps, sockets, seam clean-up, retopology of bend zones, UVs, texture re-bake, on a working copy | §D modeler keys | K3 (modeler self-check, evidence attached): watertight per part; triangles per part; no fused bridge in a moving zone; rest silhouette matches the reference from 6 views; caps hidden at rest, each in the `cap_<cut id>` group of its cut (one group per cut; a socket only where the child covers it, or n/a on a closed parent face); every design-for-motion finding in the brief built or answered |
| S4 geometry acceptance | rigger | Scripted checks (`tools/rig/rig_audit.py`) + proxy sweep: a temporary one-bone-per-part rig moved to every §B extreme; numbers per pose (part overlaps, cap exposure from the review cameras, the game-camera black-fill), images only where a number fails plus the key poses (`rigging-craft/references/tests.md` §6) | §D status, §G | Fail, each failing number confirmed on its still → **one fix note** (§4). Max 2 rounds, then `failed` → lead |
| S5 rig + tests | rigger | Skeleton, weights, controls, control manifest, export skeleton, test clips, Blender checks, export, Studio import, test clips played on the intended Animator | §G test record | K5: every test and every release line (`rigging-craft/references/tests.md` §6) PASS, MEASURED (no sheet tolerance), n/a, or BLOCKED / not verified with the reason; Roblox evidence labelled MCP-verified. Only then the rig goes to the animator, with the ROM sweep and contact-hold clips |
| S6 rig acceptance | animator | Poses every §B extreme and stress pose on the real rig through the control manifest; checks reset, IK/FK and space switches it needs; confirms the read controls (shoulders and hips, head world-orient or a plan to counter-key it, hand shapes, every hook-shape part); numbers first (`clip_check.py` rom on the sweep clip, contact holds, reset) | §H | Fail → **one rig note** to the rigger. Rigger triages: rig fix / geometry note to modeler / design question to lead. Max 2 rounds |
| S7 animate | animator | Blocking (G2 sample on first use) → spline → polish; export; Roblox import; timing list (§5); phone check | timing list | animator's own review checklist |
| S8 final | owner | G3 on the imported revision in Roblox | decision line | — |

**Modeler:** the `modeler` role (J007; skills `modeling-design`, `modeling-craft`) does S3 with `references/modeler-handoff.md` as its brief. If it is not available, the lead runs a stand-in agent (Opus, high) with the same brief (J005-D2). The rigger never cuts or remodels when a modeler or stand-in exists.

## 4. Notes between roles: one exact note per round
- A failed check goes back as **one** note listing every failed item (`templates/rig/fix-note.md`, `rules/messages.md` §2 format).
- Each item: part id, check id, measured value, where (view, frame, vertex group or coordinates, evidence file), why (the §B/§C row it breaks), pass condition. The how stays open for the receiver.
- No note without evidence. A claim without evidence is a question, not a fail (`rules/messages.md` §5).
- Rounds: 2 per stage, then `failed` with the reason → lead (`rules/company.md` §9).
- The animator never works around a missing degree of freedom (bending a tool, rotating a wing through the body). It sends a rig note and proposes alternatives: change the pose, revise the rig, separate a rigid part, reduce a close-up need, or ask the owner to change the design.

## 4a. Check budget: always light (owner J005-D8)
- **Every pose is checked by script** (numbers: audit, fold, seam and contact counts). Numbers are cheap; run them all.
- **Images only when a number fails**, plus at most 8 key poses (rest, the main locomotion pose, each signature action's peak, the hardest stress pose), seen from the gameplay camera and one close view.
- **One full check per hand-off, by the receiver.** The sender's self-check is numbers only; never both sides render and inspect the full set.
- **The full image set once, at release** (S5 / G3), not every round.
- No exploratory searches (weight variants, shape trials) unless a check fails; stop at the first variant that passes.
- **Plan-stage images are making, not checks, with their own small budget:** the rigger's posed plan at S2 (at most 4 poses at the game camera, black-fill and shaded from one pass, plus one close view) and one black-fill per option when two routes are close; the animator's key-pose contact sheet (`animation-design/references/review.md` §5).
- Report in every hand-back how many renders were made and how many images were looked at.

## 5. Timing list (animator → VFX, sound, UI)
One list per action revision, owned by the animator: named events with time in seconds (exact, plus the source frame and frame rate), meaning, owner, consumers, interruption rule. Gameplay windows come from the gameplay owner; the animator never retimes gameplay to fit a clip. A marker is presentation, never damage authority. VFX frame scripts and sound cue cards use the same event ids. Format: `templates/anim/timing-list.md`; rules in `animation-design` → `references/game-timing.md` §4.

## 6. Change control and platform limits
- The sheet has a `revision`. After S5 releases a rig, any change to §B, §C or §D bumps the revision, names the retests and keeps the old rig and clips.
- Renaming bones, moving joints or changing the rest pose after animation starts needs a migration plan and a retest of every clip (rigging paper RP:119, RP:578).
- Platform limits (fixed, no tolerance): ≤ 20,000 triangles per mesh; ≤ 4 influences per vertex; no weights on Root; watertight (`knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34-35, 59-60`; fact-check RR01-RR05). Avatar bodies have their own budgets (head 4000, torso 1750, each limb 1248, total 10,742 triangles; up to 37 optional joints: RR02, RR07).
- No documented custom-rig bone cap, Motor6D cap or model byte ceiling was found as of 2026-10-21 (RR31). Bones per rig, triangles per asset and on-screen counts are game budgets (game profile, `performance` skill) or PROPOSAL until measured on the target phone.

## 7. Self-check (lead, at each hand-off)
- [ ] The sheet exists, has a revision, and each role wrote only its own keys.
- [ ] The receiver ran the stage check and recorded it in §H with evidence.
- [ ] Every fix or rig note lists every failed item with evidence and a pass condition.
- [ ] No round 3. No silent design change: look changes went to the owner.
- [ ] Rig released only with a complete §G (Blender and Roblox evidence).

## 8. Design for motion: who catches what, and when
Most rig failures are designed in: mass on a joint, a drape over the arm, a costly chain nobody counted, a mouth modelled shut. Each role catches its share at its stage, so the problem is fixed while it is a sentence, not a re-cut.
| Stage | Role | Catches | Where it is written |
| --- | --- | --- | --- |
| Direction (character recipe) | animator + rigger | costly parts (capes, long hair, coattails, new chains), each with a cheap fallback | direction sheet |
| S1 | animator | stress poses that test costume near joints; the standard needs (shoulders and hips, the head through a spin, hands, hook shapes) | §B |
| S2 | rigger | the design-for-motion screen on the reference set or blockout; the read controls; push routes; the posed plan at the game camera | §C, plan renders, the S3 brief (`rigging-design/references/design-for-motion.md`) |
| S3 | modeler | builds the fixes: mass off joints, nothing over the arms, parts the rig moves built to move, moving parts with room, contact points fixed | §D (`modeling-design/references/read-and-form.md` §6) |
| S4-S5 | rigger | proves them in numbers at every extreme (overlaps, cap exposure, black-fill) and in the key poses at the game camera | §G (`rigging-craft/references/tests.md` §6) |
| S6 | animator | the read controls work through the manifest | §H |

A finding that changes the approved look goes to the lead for the owner with both options rendered at the game camera.

Project overlay: if `knowledge/overlays/rig-pipeline.md` exists, read it after this file; it wins for this game.
