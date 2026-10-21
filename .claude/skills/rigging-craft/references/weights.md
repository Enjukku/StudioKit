> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Sources: rigging paper RP:265-292, 184-192 (notes `knowledge/reference/rigging/02-*.md` §1, `01-*.md` §6.2), fact-check RR03-RR04, RB (Blender tool names). All [O] unless marked.

# Weights and deformation

## 1. Before any weight work
Weights come last. Check, in order: rest transforms and hierarchy → joint positions and axes → fused bridges → only then weights (`rigging-design/references/diagnosis.md` §1). Bind only after joints and rest transforms are final (RP:192).

## 2. Deform allowlist
- The deform groups are exactly the export-skeleton deform bones. Control and selection groups are ignored when counting influences (RP:269).
- Per deforming vertex: finite, non-negative weights; non-zero total; names match intended bones; ≤ 4 influences [V RR03]; no Root weight [V RR04].
- Rigid region: one influence at weight 1.0 (this is the definition of a rigid binding, not a quality threshold) (RP:269).

## 3. Cleanup order (RP:271)
1. Remove accidental non-deform groups.
2. Repair unweighted regions.
3. Remove irrelevant and cross-body support (arm weights on the belly or the other arm; head weights on the chest).
4. Prune to ≤ 4 influences: `bpy.ops.object.vertex_group_limit_total(group_select_mode='BONE_DEFORM', limit=4)`.
5. Normalize the remaining weights: `vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)`. Normalizing before pruning does not give a normalized result.
6. Retest (`tools/rig/rig_audit.py`).
- Always pass `group_select_mode='BONE_DEFORM'`: the default `'ALL'` counts control and selection groups (RB rule 13). `vertex_group_clean(group_select_mode=..., limit=..., keep_single=True)` removes tiny weights without emptying a vertex.
- Set any tiny-weight cut-off from measured visual tolerance and asset scale; never blindly delete small weights (a tiny weight on a remote bone still moves the mesh when that bone moves) (RP:271-273).
- Re-check locked groups: Normalize All skips locked groups (RB rule 13).
- Blender normalizes deform weights at deform time, so a rig that looks normalized may not export weights that sum to 1: measure with `rig_audit.py` (RB rule 14).

## 4. Locality
- Use segmentation masks or face sets to keep influence local (RP:273).
- Protected vertices: the set that must not move in a head-only or hand-only test. Measure their largest move and report the worst vertices with bone names and positions (RP:273).
- Auto weights are a starting point. Inspect them numerically and with one-joint-at-a-time motion (RP:192).
- Weight transfer from a proxy: restrict by body region; nearest-surface matching mixes an arm resting on the torso or neighbouring legs (RP:190).
- Neck: blend into the upper torso only across the planned neck transition (RP:192).

## 5. Specific deformation problems (RP:277)
| Problem | Do |
| --- | --- |
| Shoulder collapse | share the move between arm and clavicle / torso; keep the armpit crease; isolate rigid pads |
| Elbow / knee pinch | check the hinge centre and compression-side geometry before widening the weight span |
| Hip collapse | pelvis and thigh support; no opposing-thigh leakage |
| Forearm or tail twist (candy-wrapper) | spread twist over a justified chain of helper / twist joints, inside the 4-influence limit |
| Weights legal but still collapsing | go back to topology or articulation; do not smooth the whole body |

## 6. Deformation the engine will actually run
- Blender's Armature modifier "Preserve Volume" (`ArmatureModifier.use_deform_preserve_volume`) is dual-quaternion skinning (RB09); set it off explicitly. Roblox's 2026 skinning method is not documented; a historical Roblox page names linear skinning. Preview with Preserve Volume **off**; the Roblox result decides (RP:279-281; RB fact-check for the Blender wording).
- Helper bones count only if exported and driven by baked animation or a specified runtime mechanism. Drivers and corrective modifiers do not run in Studio (RP:281).
- Corrective shapes: target in the problem pose minus what the base rig gives; use as authoring reference or convert to supported articulation. Arbitrary body shape-key import was not established; FACS correctives are a face-only pipeline (RP:283).

## 7. Stress test (RP:285)
Combine degrees of freedom: arm raised + forearm twist; head turned + torso bent; hip flexed + leg spread; tail curved + base rotated. Compare shaded, wireframe, silhouette, UV-checker and in-game material views. Reject unapproved spikes, collapsed volume, texture smears, seam detachment, or visible self-intersection in required shots.
