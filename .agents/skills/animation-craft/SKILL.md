---
name: animation-craft
description: The how for animation in Blender and Roblox - rig acceptance, keying by Python + MCP, loops, bake and FBX export, Roblox import, Animator playback (priorities, blending, markers, replication), motion specs for code-driven props, ambient loops at scale, light checks with clip_check.py. Use at rig-pipeline S6-S7, for "the loop hitches", "markers don't fire". Read animation-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J006. Evidence: Roblox runtime fact-check `knowledge/reference/animation/fact-check-roblox-runtime.md` (RA ids), technique fact-check `fact-check-techniques.md` (RT<q>-<n>, TC ids, SD = silent in the docs), Blender keying fact-check `fact-check-blender-keying.md` (KB ids) and `knowledge/reference/rigging/fact-check-blender.md` (RB ids), rigging fact-check `fact-check-roblox.md` (RR ids), animation paper notes `01-*.md`, `02-*.md` (AP:<line>). Tools: `tools/anim/clip_check.py`, `tools/rig/roblox_fbx.py`. Tags: [V] verified, [E] experience, [O] studio opinion.

# Animation craft: build, export and play it

## 1. When this skill starts
After `animation-design` produced the read, the technique per part, the set and the timing list draft. For a rigged asset the rigger has released the rig (`rig-pipeline` S5: rig sheet, control manifest, test record); you start at S6. For code-driven or physics motion you write a motion spec (§5) and stop there: a builder writes the code. Needs: Blender 5.x with the MCP add-on (or headless Blender), Roblox Studio for import and playback (`studio-mcp` skill), the game profile (camera, devices).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Blender: versions, Actions and slots, keying by Python, interpolation, loops, sampling, bake, previews | `references/blender-keying.md` |
| Roblox: import routes, publish, Animator, tracks, priorities, blending, markers, replication, lifecycle, throttling, graphs | `references/roblox-playback.md` |
| Code-driven or physics motion: TweenService, CFrame / PivotTo, Motor6D.Transform, constraints, textures, flipbooks; the spec | `references/motion-specs.md` |
| Many copies: flags, windmills, plants, crowds; cost per copy, streaming, LOD, wind | `references/ambient-at-scale.md` |
| Export profile and Studio import of the rig (rigger's side) | `rigging-craft` → `references/controls-export-import.md` |
| Review rows, failure diagnosis, light-check budget | `animation-design` → `references/review.md` |
| Phone measurement method and floor devices | `performance` skill |

## 3. Steps (rigged asset: S6 → S7)
1. **Versions and inputs.** Record the Blender build, the FBX add-on check (`roblox_fbx.check_exporter() == []`), the rig sheet and control manifest revisions, the timing-list revision. Work on a copy of the released rig file; never edit the rigger's file. *Check: build manifest in `content/anim/<asset-id>/`.*
2. **S6 rig acceptance.** Pose every §B extreme and stress pose through the control manifest only (key controls, never export bones: follow the manifest's keying policy). Numbers first: `clip_check.py` `rom` on a sweep clip, contact holds, reset to rest. Images only for a failing number plus the hardest stress pose from the game camera. A fail → **one rig note** (`templates/rig/fix-note.md`) with every failed item; max 2 rounds. *Check: §H S6 row signed with evidence.*
3. **Clip setup** (`references/blender-keying.md` §2). One named Action per clip with its slot assigned explicitly; frame range and effective fps (`render.fps / render.fps_base`) recorded; loop clips get the range policy of §4 C-09. Keep clip ids, event times, contacts and loop policy in data (the animation set and timing list), not in display names. *Check: Action list matches the animation set.*
4. **Block** (design §3 step 5). Key poses and holds that show the real timing: stepped (CONSTANT) keys or copied-pair holds, as you prefer (method is open; the result is judged, `animation-design` principles P-08). Root and contacts first, whole body on shared frames so timing stays movable. Render a cheap preview at the game camera. *Check: the action reads from the blocking preview; get the brief's check-in (film-director for cutscenes, the proof reviewer for a character proof) before polish.*
5. **Breakdowns, spline, polish.** Breakdowns and arcs; interpolation per channel and segment (`references/blender-keying.md` §3); offsets move a key with both handles; secondary and face last. Run `clip_check.py` after each pass (`python tools/anim/clip_check.py samples.json --timing timing.json --manifest control-manifest.json --tol tol.json --up z`; tolerances come from the rig sheet, game profile or owner, else results are MEASURED). *Check: no FAIL in the clip_check report, or a reason per item.*
6. **Bake and export** (`references/blender-keying.md` §5). Bake the export skeleton with visual keying on a copy, then `roblox_fbx.export(path, kind="clip")` per clip (or one multi-clip file when the import route is the Clip Editor). In-place locomotion by default: native root motion is not released (RA41, RR39-RR41). *Check: the export log lists the intended clips, range and fps only.*
7. **Round trip.** Re-import the FBX into a fresh scene, sample it and compare with the source samples (clip_check on both; poses, length and contacts match). *Check: `tests/roundtrip-<clip>.json`.*
8. **Roblox import and publish** (`references/roblox-playback.md` §1). Import route named (Animation Editor import / Clip Editor / Import 3D); the owner clicks Import or Publish when the brief says so (J005-D6: test place only). Set priority and loop on the asset; add markers from the timing list if they did not survive import (probe once per route, §4 C-17). *Check: the asset id and the route are in the animation set.*
9. **Play on the intended Animator** (`references/roblox-playback.md` §2-4). Server-created Animator and server playback when other players must see it; client Animator for cosmetic motion. Load once, cache the track. Read the Output log for marker times against the timing list. Capture stills at the event frames from the game camera (MCP captures are stills, not video). *Check: MCP-verified rows in the check record.*
10. **Phone and scale** (`performance` skill; §6). The agreed scene with the peak on-screen count on the floor phone; without a phone the row is BLOCKED, never PASS. *Check: measured numbers or BLOCKED with reason.*
11. **Final timing list.** Times in seconds plus source frame and fps; mark which were confirmed in the Output log. Bump the revision and tell every consumer if a time moved. *Check: VFX and sound acknowledge the revision.*

Code-driven or physics motion: steps 1, then write the motion spec (§5), then review the builder's result in Studio against it (step 9 checks, Output-log event times).

## 4. Craft core: what separates working clips from broken ones
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | Load with `Animator:LoadAnimation` (the Humanoid and AnimationController versions are deprecated); the Animator must be in Workspace first; each call makes a new track, so load once and cache, or fetch with `GetTrackByAnimationId` | [V] RA03-RA05 |
| C-02 | Replication: NPC and prop clips must be loaded and started on the server to replicate; a client-created Animator never replicates; a player's own client may start tracks on its Character's Animator. Cosmetic crowds and decoration use a client Animator on purpose | [V] RA02, RA42; TC10 |
| C-03 | Priority settles per joint, high to low: Action4, Action3, Action2, Action, Movement, Idle, Core; compare by name, never by enum number; default and catalog clips play at Core, so any custom clip at Idle or above overrides them joint by joint. A layered clip keys only the joints it drives | [V] RA09-RA10; [O] AP:751 |
| C-04 | Priority first, weight second; same-priority tracks blend by weight. Defaults: fadeTime 0.1 s for Play, AdjustWeight and Stop; weight 1; speed 1. Fade lengths are a design or measured value, written in the set | [V] RA12-RA14 |
| C-05 | After `Stop()`, call `Play()` before adjusting that track. Use `Ended`, not `Stopped`, to know its influence is gone. Avoid `Stop(0)` on Motor6Ds with MaxVelocity 0 | [V] RA14-RA15 |
| C-06 | Speed: negative plays backward, 0 pauses; real duration = Length / Speed; Length is 0 until loaded; TimePosition is settable only while playing | [V] RA16-RA17 |
| C-07 | Markers: read with `GetMarkerReachedSignal(name)`, connected before `Play()`; payload in the Parameter string. `KeyframeReached` is deprecated; `GetKeyframeMarkerReached` (named in one doc page) does not exist. Marker behaviour under throttling or low frame rate is undocumented: markers drive cosmetics only | [V] RA19-RA22 |
| C-08 | Gameplay never waits on a marker or a client's visual state: the server owns hits, damage, open, occupied | [O] AP:473, AP:833; [V] TC30 |
| C-09 | Loops: a Roblox loop does not blend from the last key to the first, so the last key repeats the first pose and the clip length equals the period. Check pose and velocity at the seam after import | [V] RA18; [O] AP:458 |
| C-10 | Blender keying through the current API: Actions with slots and channelbags (`action.fcurves` was removed in 5.0); `fcurves.ensure(..., group_name=)` needs 5.0+; batch keys with `keyframe_points.add` + `foreach_set('co', ...)` then `update()` | [V] RB30, RB39-RB40; KB rows |
| C-11 | Interpolation describes the span from a key to the next; set it and the handles on purpose (automatic handles can overshoot); one rotation mode per animated bone, the rig's | [V] AP:638, RB42; [O] AP:646-650 |
| C-12 | FBX carries baked samples, never constraints, IK or drivers: bake the export skeleton with visual keying on a copy (the bake defaults are traps: `visual_keying=False`, `only_selected=True`, `clean_curves=False`) | [V] RB12, RB44 |
| C-13 | Never export with Blender's FBX defaults; use `tools/rig/roblox_fbx.py` (`kind="clip"`); start with simplification 0.0 so any later reduction has a baseline | [V] RB23; [O] AP:688 |
| C-14 | In-place locomotion; the controller owns travel. Avatar animations play in place: mute root translation before export | [V] RA41; [O] AP:813 |
| C-15 | Procedural layers on top of a clip write `Transform` in PreSimulation and skip when `Animator.EvaluationThrottled` is true; R15 avatar joints are AnimationConstraints when the avatar joint upgrade is on; Motor6D stays right for mechanical rigs | [V] RA24, RA28-RA30 |
| C-16 | IKControl needs Type, EndEffector, Target, ChainRoot; turn it off with `Enabled=false`, not weight 0 | [V] RA33 |
| C-17 | Whether Blender markers survive FBX import into Roblox markers is not documented: probe once per import route; the fallback is to add markers on the Animation Events bar from the timing list | [O] SD (not in the mirror, J006) |
| C-18 | A cap on playing tracks per character exists and warns; 64 is forum-reported, undocumented: never a budget. Leaked or duplicate tracks are the usual cause | [E] RA27 |
| C-19 | Cosmetic code motion runs on the client: a server-side tween replicates the property every frame | [V] RT1-05, TC01 |
| C-20 | Animation memory unloads only when scripts drop their references and connections; strip saved animation metadata from shipped rigs | [V] RA42-RA43 |
| C-21 | KeyframeSequence is what the editor saves; CurveAnimation is required for emotes and animation packs; converting quaternion curves cannot be undone | [V] RA31-RA32 |

## 5. Code-driven and physics motion: the spec (detail `references/motion-specs.md`; template `templates/anim/motion-spec.md`)
- You write what moves, the pivot or rail, travel, phases with lengths and curves (EasingStyle + direction, or a named custom curve), events, interruption rules, client or server, and the checks. A builder writes the code; values go into data.
- TweenInfo gives 11 easing styles, 3 directions, repeat, reverse and delay; a one-axis door or lever needs nothing more [V] TC03. A second tween on the same property cancels the first and Cancel leaves it mid-way: every spec states the end pose and the interrupt rule [V] TC02.
- Rigid props moved by code: anchor one root, weld the rest, move with `PivotTo` or CFrame [V] TC05; `BulkMoveTo` only for a measured bottleneck [V] TC06. For rigid hierarchies moved every frame, writing `Motor6D.Transform` in PreSimulation is the documented efficient path [V] TC07.
- Constraints: hinge servo (doors, gates), prismatic servo (lifts, sliding doors), motor (wheels, windmills) take few properties and sleep when idle; set a servo target once per state change, never per frame [V] TC12, TC14. Physics is simulated by the owner, so a free mechanism can look different per client: server-owned servo targets where everyone must see the same pose [V] TC13.
- A keyed multi-part mechanism (drawbridge with chains, windmill with gears) = Motor6D rig + AnimationController + Animator through `rig-pipeline`; a one-axis rigid door, lever or lift needs no rigger step [V] TC09.

## 6. Ambient loops at scale (detail `references/ambient-at-scale.md`)
- No documented per-copy cost exists for tween, Animator track, Motor6D, Bone or flipbook (SD01): measure the technique at the peak count on the floor phone before choosing it for hundreds of copies.
- One loop per system, never one Heartbeat or PreRender loop per object [V] TC08; a shared curve sampled with `TweenService:GetValue` avoids one Tween object per copy [V] TC04.
- Global wind moves terrain grass, clouds and particles only; flags, trees and signs need their own motion [V] TC19. Animated models get no SLIM or far LOD: plan the pop-in at the streaming radius [V] TC20. Client-set motion on server-made models is lost on stream-out: restart it on stream-in at a believable phase [V] TC23.
- Texture offset scrolling is the cheapest surface motion (water, belts, lava) [V] TC16; flipbooks are at most 8×8 frames at 30 fps and may be switched off on low-memory phones, so the object must still read without them [V] TC17. There is no general animated mesh texture [V] TC18.
- Vary phase or speed per copy; offer a still or slow variant for players who reduce motion [V] TC29 (the setting exists; the variant is a design choice).

## 7. Rules (final check)
- Never edit the rigger's file, the source snapshot or game code; motion specs go to a builder.
- Never export with Blender defaults (C-13); never rely on a Blender-only deformer, constraint or driver in Roblox (C-12).
- Never let a marker or a client's visual state decide gameplay (C-08).
- Never upload, publish or import into a live place without the brief saying so; tests run in the test place (J005-D6).
- Never write scripts through Studio MCP in `files` source mode (`AGENTS.md` §3); Studio MCP is for import checks, play-tests and captures.
- Never claim a Blender or Studio result without an evidence file from this task; label each check gate-verified / MCP-verified / owner-confirmed / not verified.
- Checks are light (owner J005-D8): numbers for every clip, images only on a failing number plus at most 8 key frames per action.

## 8. Self-check before hand-back
- [ ] Build manifest: Blender build, exporter check `[]`, rig sheet, manifest and timing-list revisions.
- [ ] S6 signed with evidence, or one rig note sent.
- [ ] Every clip in the set exists as a named Action and an export file; clip_check report with no unexplained FAIL.
- [ ] Round trip done; Roblox import route and asset ids recorded; priority and loop set as the set says.
- [ ] Played on the intended Animator (server or client, as designed); marker times from the Output log against the timing list.
- [ ] Phone row measured or BLOCKED with reason; render and image counts reported.
- [ ] Timing list final, revision bumped, consumers told.

Project overlay: if `knowledge/overlays/animation-craft.md` exists, read it after this file; it wins for this game.
