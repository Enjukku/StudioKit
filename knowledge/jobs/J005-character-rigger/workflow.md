---
type: job
scope: universal
status: superseded
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent character-rigger, then animator); rigging paper (Roblox_Character_Rigger_Research.txt, cutoff 2026-10-20); animation paper (Animator_Research_Paper.txt, 2026-10-21); DestructionSimulator D-160, D-185, D-186, F-020 (read-only)
supersedes: []
superseded_by: .agents/skills/rig-pipeline/SKILL.md
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Rig workflow: animator → rigger → modeler → rigger → animator (DRAFT for owner review, step 1)

After owner approval this becomes the shared skill `rig-pipeline` (loaded by animator, character-rigger, modeler, lead). Paper claims marked † are fact-checked in J005 step 2 before they enter a skill.

## 1. Principle

Each role decides what it knows best; the others state needs, not methods (`rules/messages.md` §1).

| Role | Decides | Never decides |
| --- | --- | --- |
| animator | what must move, how far (range of motion, ROM), how (active / passive / rigid), contacts, stress poses, clip list, event timing inside gameplay windows | joint layout, cut lines, topology |
| character-rigger | rigid / skinned / mixed per region, joints and bones, pivots, which parts must be separate, where cuts go and why, deformation zones, Tripo route, all rig tests | how a cut is built or hidden in geometry, motion style |
| modeler (planned) | how each cut is made, capped and hidden; re-modelling; retopology; UVs and texture re-bake; may counter-propose a better cut or build | joint plan, ROM |
| lead | opens the sheet, routes notes, settles disagreements it can, sends design trade-offs to the owner | craft |
| owner | look, feel, any design change a technical limit forces, G2 / G3 | — |
| gameplay owner (designer / config) | gameplay windows (startup, active, recovery, cancel) | animation craft |

Evidence beats position: a disagreement between roles is settled by a posed proxy test (rigging paper §3), not by argument. A creative trade-off goes to the owner with both options rendered.

## 2. The loop (stages, owner of each, check between stages)

```
S0 lead: intake ─► S1 animator: motion needs ─► S2 rigger: rig plan ─► K2 animator: "plan covers needs"
   ─► S3 modeler: cuts + geometry ◄──counter-proposal── (one round) ──► rigger
   ─► S4 rigger: geometry acceptance ──fail: ONE fix note──► S3 (max 2 rounds, then failed → lead)
   ─► S5 rigger: rig + tests (Blender + Roblox) ─► S6 animator: rig acceptance ──fail: ONE rig note──► rigger
   ─► S7 animator: animate, export, Roblox, timing list ─► S8 owner G3 (imported revision)
   rig problem found during S7 ──► rig note to rigger (rigger triages: rig fix / geometry note to modeler / design → lead → owner)
```

| Stage | Owner | Does | Writes (sheet section) | Check before the next stage starts (receiver runs it) |
| --- | --- | --- | --- | --- |
| S0 intake | lead | Confirms approved reference image and model source; purpose, camera, device, on-screen count; opens `content/rigs/<asset-id>/rig-sheet.md` | §A | K0: reference approved (decision line); purpose and runtime driver known or marked UNKNOWN; source files snapshotted, never edited |
| S1 motion needs | animator | Studies the whole body from multi-view renders (front, back, sides, ¾, gameplay camera); writes the motion profile (`motion-profile.md`, animator's own file), then the rig needs | §B | K1 (rigger): every visible part has a row, also "does not move"; every ROM has a unit, the pose or clip that needs it and a source (reference, owner, PROPOSAL); contacts and held tools declared; no invented mass or delay numbers |
| S2 rig plan | rigger | Inspects geometry (objects, connected parts, fused bridges, open edges, triangles, materials, UVs); per region: rigid / skinned / mixed with reason; joint plan; cut list with why; deformation zones; Tripo route; budgets; test plan | §C, §E, §F | K2 (animator): every §B row has an answer: supported / supported with limit / not supported + alternative. Animator signs "C covers B". A "not supported" that changes the look → `needs-decision` → lead → owner |
| S3 geometry | modeler | Per cut: accept or counter (better cut or better build, with the §B/§C rows it still meets). Cuts, caps, sockets, seam clean-up, retopology of deformation zones, UVs, texture re-bake, on a working copy | §D | K3 (modeler self-check, evidence attached): watertight per part; triangles per part; no fused bridges in moving zones; rest silhouette matches the approved reference from 6 views; caps hidden at rest |
| S4 geometry acceptance | rigger | Scripted checks + proxy rotation: temporary one-bone-per-part rig swept to every §B extreme, seams checked from the review views | §D status | Fail → **one fix note** (§4) with every failed item. Max 2 rounds, then `failed` → lead |
| S5 rig + tests | rigger | Skeleton, weights, controls, control manifest, export skeleton; test clips; Blender checks; export; Studio import; play test clips on the intended Animator | §G test record | K5: every test PASS, or BLOCKED with reason; Roblox evidence labelled MCP-verified. Only then the rig goes to the animator |
| S6 rig acceptance | animator | Poses every §B extreme and stress pose on the real rig through the control manifest; checks reset, IK/FK and space switches it needs | §H sign-off | Fail → **one rig note** to the rigger (same format). Rigger triages: rig fix / geometry note to modeler / design question to lead. Max 2 rounds per stage |
| S7 animate | animator | Blocking (G2 sample on first use) → spline → polish; export; Roblox import; timing list shared with VFX, sound, UI; phone check | timing list (J006) | Animator's own review checklist (J006) |
| S8 final | owner | G3 on the imported revision in Roblox | decision line | — |

Change control: the sheet has a `revision`. After S5 releases a rig, any change to §B, §C or §D bumps the revision, names the retests, and keeps the old rig and clips (rigging paper §3, animation paper "Do not do"). Renaming bones or moving the rest pose after animation starts needs a migration plan and retest.

## 3. Tripo models (one merged mesh): where the loop matters most

A Tripo model arrives with head, body, arms and legs in one piece. One object is not one connected surface: the rigger counts connected parts before anyone cuts (rigging paper rule 06).

Per region the rigger picks one route at S2 (paper §4c, applied by region, not by asset label):

| Route | When (PROPOSAL rule, owner first-game evidence below) | Who works |
| --- | --- | --- |
| R-cut: separate rigid piece, 100% on one bone, cut hidden by collar / socket / overlap / deliberate gap | the break can hide (collar, sleeve, cuff, glove, tuft, crease); stylized, toy, plush; rigid gear | rigger plans cut → modeler cuts, caps, builds socket |
| R-skin: keep continuous, rebuild topology in the bend zone, localized weights | bare skin or fur seen close where a break would show; long soft parts (tail, tentacle, membrane) | rigger names zone and protected regions → modeler retopologizes → rigger weights |
| R-mix | soft body + rigid armor, eyes, teeth, weapons | both |
| R-reject | neither repair keeps the approved design in scope | rigger → lead → owner (regenerate or remodel) |

Tripo's own tools are candidates, never acceptance (paper rules 10-12):

| Tripo tool † | Who runs it | Acceptance |
| --- | --- | --- |
| Mesh Segmentation (keeps geometry; v2 Beta adds labels; version pinned explicitly) | modeler, when the rig plan says its boundaries fit | rigger compares boundaries and pivots with the cut list; labels do not prove a good joint seam |
| Smart Segmentation (also re-models parts) | modeler | plus silhouette, proportion, UV and material check against the approved reference |
| Rig check + Auto Rigging (humanoid model v3.0-20260909 must be requested by name; API default is older) | rigger, as a candidate | same audit as a hand rig: joint positions, weights, names, roots, influences, Roblox round trip |

Owner evidence from the first game (DestructionSimulator, EXPERIENCE, game-specific decisions not copied): a skinned single Tripo mesh webbed the golem's arms to the torso (D-160); a new neck mesh creased (D-185); skinned Tripo arms "become wrinkly" (D-186); deleting faces to close Tripo shells opened holes, tuck-and-cap worked (F-020). Separate rigid pieces with buried roots were the fix. This supports R-cut as the first try for stylized merged characters; R-skin stays for regions where a break must not show.

## 4. Notes between roles (one exact note per round)

A failed check goes back as **one** note that lists every failed item, in the `rules/messages.md` §2 brief format. Template: `fix-note-template.md`. Each item names: part ID, check ID, measured value, where (view, frame, vertex group or coordinates, evidence file), why (the §B/§C row it breaks), pass condition. The how stays open for the receiver. No note without evidence; a claim without evidence is a question, not a fail (`rules/messages.md` §5).

## 5. Timing list (animator → VFX, sound, UI)

The animator owns one timing list per action revision: named events in seconds (exact, source frame basis), meaning, owner, consumers, interruption rule. Gameplay windows come from the gameplay owner; the animator never retimes gameplay to fit a clip (animation paper §6, §12). VFX frame scripts and sound cue cards name the same event IDs. Format: J006 (animator build).

## 6. Budgets (sheet §E)

| Limit | Value | Source | Kind |
| --- | --- | --- | --- |
| triangles per mesh | ≤ 20,000 | `knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34` | platform ceiling, not a phone target |
| influences per vertex | ≤ 4 | `specifications.md:59` | platform |
| weights on Root | none | `specifications.md:60` | platform |
| geometry | watertight, no exposed holes or backfaces | `specifications.md:35` | platform |
| avatar bodies, advanced R15 | own triangle budgets; up to 37 optional extra joints | `avatar/character-bodies/specifications.md:686` | only for avatar bodies |
| bones per rig, tris per asset, materials, on-screen count | game budget (game profile / `performance` skill) or PROPOSAL until measured on the target phone | rigging paper §2.3: no universal custom-rig bone cap established | project |

## 7. What the role files will say about this workflow

- character-rigger: owns S2, S4, S5 and rig-note triage; never cuts or remodels when a modeler exists; stand-in rule while the modeler is planned (digest item 2).
- animator: owns S1, S6, S7; never works around a missing degree of freedom (distorting a tool, rotating a wing through the body); raises a rig note instead (animation paper §12).
- modeler: `modeler-handoff.md` until the role is built.
