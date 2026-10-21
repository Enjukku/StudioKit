> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Sources: rigging paper RP:340-427 (notes `knowledge/reference/rigging/02-*.md` §4-5), animation paper AP:686-881 (notes `knowledge/reference/animation/02-*.md`), fact-checks RR (Roblox) and RB (Blender, `fact-check-blender.md`).

# Controls, control manifest, export and Roblox import

## 1. Two skeletons
- **Authoring rig:** control bones, IK targets, poles, widgets, drivers, constraints, selection helpers. Never exported.
- **Export skeleton:** the deform hierarchy plus approved non-deforming roots and sockets, chosen by an **explicit allowlist and parent map**. "Deform only" can drop a needed root; "everything" bloats the schema (RP:342 [O]).
- FBX carries evaluated motion, not the constraint graph: bake the export skeleton (RP:352; RB fact-check).

## 2. Controls (RP:346-350 [O])
- FK for direct rotation and clean arcs; IK to hold hand / foot contact. One pole convention; no exactly straight chain in the working pose.
- Add foot roll, grip, jaw, gaze or tail controls only when the clip list needs them.
- IK/FK switch = pose match: evaluate, match the destination in the documented space, keep the pole, change the mode, key it. A Boolean that snaps is not a switch.
- Space switch: capture the world matrix, change the parent or constraint, compute the keeping offset, key switch and offset. State who drives each object in each phase so nothing moves twice. Test hand world → weapon and weapon hand → holster.

## 3. Control manifest (the animator's interface; RP:354-359)
One file per rig, `content/rigs/<id>/control-manifest.json`, one record per control:

`control_id · blender object path · pose-bone or property id · role · side · coordinate_space · allowed_channels · rotation_mode · units · min/max (from §B ROM) · neutral value · dependencies · ik_fk mode property · snap routine · space-switch routine · export mapping · keying policy · named pose library · contact markers · validation query`

The animator reads this, never guesses controls from viewport shapes (RP:354).

## 4. Export profile (Blender → FBX): `tools/rig/roblox_fbx.py`
**Blender's FBX defaults are the opposite of Roblox's guidance** (leaf bones on, bake animation on, NLA strips and All Actions on, simplify 1.0, scale option NONE). Never export with defaults: call `roblox_fbx.export(path, kind="rest" | "clip" | "avatar_body")`, which sets every option by name and first runs `check_exporter()` against the installed Blender (RB rule 4).

| Setting (UI label → Python) | Value | Source |
| --- | --- | --- |
| Path Mode → `path_mode`; Embed Textures → `embed_textures` | `COPY`; on | [V] `art/modeling/export-requirements.md:29` |
| Apply Scalings "FBX Units Scale" → `apply_scale_options` | `FBX_SCALE_UNITS` (exporter default is `FBX_SCALE_NONE`) | [V] RR18; RB rule 4 |
| Add Leaf Bones → `add_leaf_bones` | off | [V] RR18 |
| Bake Animation → `bake_anim` | off for the rest model; on for clip files | [V] RR18 |
| Clip files | `bake_anim_use_all_actions` off (on exports every resolvable Action as an extra clip), `bake_anim_use_nla_strips` off, `bake_anim_force_startend_keying` off, `bake_anim_simplify_factor` 0.0, `bake_anim_step` 1.0 (frames); assign the Action + slot and set the scene frame range first | [V] RR19; RB52 |
| Avatar bodies only | `use_custom_props` on (FACS data) | [V] RR19 |
| Only Deform Bones → `use_armature_deform_only` | off: on keeps deform bones and their ancestors but drops non-deforming sockets; choose the export bones by allowlist instead | RB26 |
| Axes → `axis_forward`, `axis_up` | Roblox gives none; keep the exporter pair `-Z` / `Y`, record it, prove it with a labelled-reference round trip | [O] RP:386 |
| `global_scale` | 1.0 (the manual's "10" is stale) | RB31 |
| `bake_space_transform` | off (experimental for armatures) | AP:686; RB |
| Apply Modifiers → `use_mesh_modifiers` | on: it skips Armature modifiers and evaluates at rest; never hand-apply the Armature modifier | RB24 |
| Shape keys | exported as BlendShapes unless a non-Armature modifier is applied; whether Roblox imports body BlendShapes is not verified | RB32 |
| Units | calibrate with a dimensioned reference; compare exported vs imported size in studs; never stack scale factors | [O] RP:388 |
| Transforms | frozen: scale 1, rotation 0, Root at origin | [V] RR30 |
| Files | one rest-model file + one named file per test clip (traceable); the Animation Clip Editor also accepts multi-clip files since 2026-03-31 | [O] RP:382; [V] RR37 |
| Constraints, IK, drivers | never in FBX; only baked, sampled results | RB rule 6 |

## 5. Roblox import (S5)
1. File > Import (FBX or glTF; FBX preferred, glTF supported; glTF nests each mesh in its own Model with one MeshPart per primitive) [V RR21, RR23].
2. Rig Type: R15 (avatar bodies only), Custom, or No Rig [V RR21].
3. **Keep Zero Influence Bones on** when sockets or a weightless Root must survive (default off) [V RR22]. Never add Root weights to keep it (RP:417).
4. Read the whole hierarchy and every warning before accepting. Separate rigid objects stay separate (RP:394).
5. Check MeshParts, Bones / joints, attachments, the controller (Humanoid or AnimationController) and the Animator [V RR13].
6. Import each test clip against the right rig; play it on the intended Animator (`Animator:LoadAnimation`, the controller's own method is deprecated) [V RR13, RR45].
7. Avatar bodies: Avatar Setup / validation, attachments, HumanoidRigDescription and DigitsRigDescription for advanced joints [V RR08]. Custom assets: attach the agreed controller and collision proxies instead.
8. Evidence: Studio MCP (`studio-mcp` skill) hierarchy dump + screenshot / clip; label MCP-verified.

## 6. Runtime facts the rig must respect
- Bone motion moves the picture, not collision: physics gets proxy parts [V RR12].
- Motor6D joins two parts animatably; the Animator overwrites `Motor6D.Transform` each frame; custom offsets go after the Animator, before physics [V RR51].
- R15 characters with Avatar Joint Upgrade use AnimationConstraints, not Motor6Ds [V RR52].
- Root motion is not released (forum reply 2026-01-21; roadmap Early 2027): clips are in place, the controller moves the root [V RR39-RR41].
- Animation priority, high → low: Action4, Action3, Action2, Action, Movement, Idle, Core; per joint until weight 1 [V RR44]. Key only the joints an overlay needs.
- IKControl: off is `Enabled = false`, not weight 0 [V RR57].
- Phone frame budget: 33.33 ms at 30 FPS, 16.67 ms at 60 FPS for the whole frame, not animation alone; profile on a phone [V RR59].
- No documented custom-rig bone or Motor6D cap found (2026-10-21) [RR31]; "64 playing tracks" is forum-reported only [RR61].
