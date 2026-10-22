> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Facts: `knowledge/reference/rigging/fact-check-blender.md` (RB rows; Blender 5.2.2 source and 5.2 manual, bundled MCP docs = 5.1). Method: rigging paper RP:340-374, 495-556 [O]; animation paper AP:542-701 [O]. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§6 measuring recipes, run on Blender 5.1.2 headless on a synthetic proxy rig; §3 slot and bake rows; repair round 1: recipe 1 on the evaluated mesh with orthographic rays, recipe 5 swing, the crop count; repair round 2: recipe 1 samples any face through its triangles, the `cap` group's source, recipe 5 pass in degrees; repair round 3: one `cap_<cut id>` group per cut, read from the evaluated mesh at weight 1, part files as .blend; repair round 4: a socket only where the child's cap covers it, every recipe labelled a screening aid with its known false readings).

# Blender through Python and the Blender MCP

## 1. Version first (every session)
1. Run once and save to the build manifest (`content/rigs/<id>/build-manifest.json`): `bpy.app.version_string`, `bpy.app.version`, `bpy.app.build_hash`, the FBX add-on `bl_info["version"]`, and `roblox_fbx.check_exporter()` (must return `[]`) (RB rule 1; RP:593).
2. API floor: Blender ≥ 5.0 for the slotted-Action calls below (`fcurves.ensure`, `group_name`); the Blender MCP add-on needs ≥ 5.1. The studio PC has 5.1 installed (2026-10-21); facts below hold for 5.1 and 5.2.2 unless marked. Do not mix versions inside one asset.
3. Check API names against the installed Blender before relying on them: `mcp__blender__search_api_docs` (bundled docs are 5.1) or `dir()` / `get_rna_type()` in the live session.

## 2. MCP working rules
- Blender must be running with the MCP add-on server started (`localhost:9876`). If the call fails, the stage is BLOCKED; ask the lead, never fake a result.
- `execute_blender_code` returns data through a variable named `result` (JSON-serialisable). Return compact dicts, not print output or whole scenes.
- **Inspect before you change.** `get_objects_summary` first; never assume names, modes or selection.
- **Idempotent stages** (RP:367, 548): each stage reads the scene, saves a checkpoint (`bpy.ops.wm.save_as_mainfile(filepath=..., copy=True)`), changes one thing, evaluates, records evidence. A rerun replaces its own named output (`<asset>_proxy_rig`, `<asset>_rig`); it never adds a second armature, modifier or joint. After a disconnect, re-read the scene before retrying.
- Never edit the source snapshot. Work in `content/rigs/<id>/work/<asset>_work.blend`.
- Prefer direct data access (`bpy.data`) for repeatable edits; for operators set mode, active object and selection explicitly and use `bpy.context.temp_override(...)`. No Python threads (RB rule 26).

## 3. API facts you will use (RB rules)
| Need | Call / fact | RB |
| --- | --- | --- |
| Split a mesh | `bpy.ops.mesh.separate(type='SELECTED' / 'MATERIAL' / 'LOOSE')`; LOOSE splits only disconnected pieces | 15 |
| Plane cut | `bpy.ops.mesh.bisect(plane_co, plane_no, use_fill, clear_inner, clear_outer)` takes the plane in **world space** and cuts selected geometry of every Edit Mode object; `bmesh.ops.bisect_plane` works in mesh coordinates | 16 |
| Pose matrices | `PoseBone.matrix` = final, armature-object space; world = `arm.matrix_world @ pb.matrix`; `matrix_basis` = relative to parent and rest; `Bone.head_local` armature-relative; `edit_bones` exist only in Edit Mode | 17 |
| Evaluated geometry | re-fetch `bpy.context.evaluated_depsgraph_get()` after every change; `ob.evaluated_get(dg).to_mesh()` (pass `preserve_all_data_layers=True, depsgraph=dg` to keep vertex groups); always `to_mesh_clear()` | 18 |
| Frames | `scene.frame_set(frame)`, then restore; effective rate = `scene.render.fps / scene.render.fps_base` | 19, 25 |
| Weights | `vertex_group_limit_total`, `vertex_group_normalize_all`, `vertex_group_clean` with `group_select_mode='BONE_DEFORM'` | 13 |
| Preserve Volume | `ArmatureModifier.use_deform_preserve_volume` (dual quaternion); set False for Roblox preview | 12 |
| New test clip | `bpy.data.actions.new(name)`; `action.slots.new(id_type='OBJECT', name=arm.name)`; `ad.action = action`; `ad.action_slot = slot`; `bag = anim_utils.action_ensure_channelbag_for_slot(action, slot)`; `bag.fcurves.ensure(path, index=i, group_name=bone)`; `keyframe_points.add(n)`; `foreach_set('co', flat)`; `fcurve.update()`. Legacy `action.fcurves` is gone since 5.0 | 2, 3 |
| Bake constraints | `bpy.ops.nla.bake(..., visual_keying=True, only_selected=...)` (defaults are `visual_keying=False`, `only_selected=True`); `clean_curves` only with a set tolerance. A default bake drops a world-orient switch's result with no error (tested 2026-10-22) | 20 |
| Play an Action on another object (a copy, the export skeleton) | set `ad.action` **and** `ad.action_slot` (for example `action.slots[0]`); with the Action but no slot the object plays nothing, and a bake of it records a frozen pose with no error (tested 2026-10-22) | — |
| Import a check file | native `bpy.ops.wm.fbx_import` | 24 |
| Export | `tools/rig/roblox_fbx.py` (never defaults) | 4 |

## 4. Stage scripts (what each stage produces)
| Stage | Script does | Output |
| --- | --- | --- |
| S2 inspect | object list, per-mesh `audit_mesh` (triangles, open edges, connected parts), materials, UV maps, bounding sizes in studs | `tests/s2_inventory.json` + 6 orthographic renders with wireframe over shaded |
| S2 plan renders | coloured cut lines and bend zones over the model, 6 views | `renders/plan_*.png` for the modeler |
| S4 proxy sweep | temporary one-bone-per-part armature at the §C pivots; pose each §B extreme; renders + `audit_mesh` per part | `tests/s4_r<n>_*.png`, `tests/s4_r<n>.json`; proxy deleted after |
| S5 rig | export skeleton by allowlist + parent map; authoring controls on top; weights; control manifest | `<asset>_rig.blend`, `control-manifest.json` |
| S5 tests | test clips as named Actions (one per test); `rig_audit.audit_scene` with protected groups and sweeps | `tests/audit_s5.json`, clip renders |
| S2 posed plan | the S4 proxy at the plan's pivots on the blockout or source, posed at the hardest stress poses and the signature pose; §6 numbers; game-camera black-fill and shaded (`animation-craft/references/blender-keying.md` §7) | `tests/s2_posed.json`, `renders/posed_*.png` |
| S5 export | `roblox_fbx.export` rest model + one file per clip; re-import into a fresh scene (`wm.fbx_import`) and compare hierarchy, weights, sizes; compare clips by clip frame (the re-import moved the range start by one frame in the 2026-10-22 test) | `export/*.fbx`, `tests/roundtrip.json` |

Renders for review: Workbench (fast, deterministic), fixed saved cameras so before/after views match (AP:680). Name every evidence file in the rig sheet §G.

## 5. Proposed automation surface (studio wrappers, not Blender or MCP names)
The papers propose wrappers such as `inspect_rig`, `set_pose`, `evaluate_frame`, `sample_deformed_mesh`, `bake_export_skeleton`, `validate_export` (RP:361; AP:634). They do not exist yet. Write them only when a second asset needs the same code (`rules/anti-overengineering.md`); until then, keep stage scripts in `content/rigs/<id>/scripts/` and reuse `tools/rig/`. When you repeat the same manual sequence on a third asset, file a tool ticket for `tools/rig/` in the hand-back's proposals (the recipes in §6 are such candidates).

## 6. Measuring recipes (numbers before images; each run once on a synthetic proxy rig, Blender 5.1.2 headless, 2026-10-22)
Run inside Blender after `dg = bpy.context.evaluated_depsgraph_get()` and `sc = bpy.context.scene`. Return dicts; write them to `tests/<stage>.json`. **Every recipe here is a screening aid, not a verdict:** it finds the poses and cameras worth looking at. Each one ends with its known false readings, found in the test and review rounds. A failing or borderline reading (a few points, a value near the tolerance) is checked by eye on the still of that pose and camera before any fix note goes out, and a pass in a case on the recipe's known-false list is checked the same way. No fix note goes out on a number alone. A tested kit tool for these measures is proposed; until it exists, copy the code as written.

**Recipe 1: cap exposure.** One vertex group per cap or socket, named `cap_<cut id>`; the cut id is the part id of the rig sheet record whose §C `cut` it is, the child side of the joint (the shoulder cap on upper arm P05 and the shoulder socket on the torso are both `cap_P05`; the elbow cap of that upper arm is `cap_P06`, its forearm's id); a cap face is a face whose vertices are all in that one group at weight 1. A socket is only the parent's faces that the child's cap covers at rest. On a blocky or primitive parent (a blockout built from primitives, a blocky part) the cut plane lies on one of the parent's own closed faces, the torso top under the head or a side face under a flush arm, and that face reaches past the child's cap: the part outside is ordinary surface and shows at rest (in the test the whole torso top as the neck socket read 6 of 14 from the game camera at rest, and the whole side face under a flush arm 9 of 14 from the side, where the area each child covers read 0). So mark the child's cap first, then the socket with `child=`: `mark_plane_caps(parent, cut, co, no, child=child)` keeps only faces whose corners all lie inside the child's cap outline. On a closed face it finds 0; then either cut the child's cap outline into that face (Knife Project with a flat copy of the child's cap as the cutter, viewed along the cut normal: a closed part cannot cut; in a script, bisect that face along each outline edge) and mark again, or record the socket n/a in the child record's §C `cut` (`socket n/a: closed parent face`) and count that cut on the child's cap only. Record n/a when the face is the same surface inside and outside the outline (nothing there to hide); cut it when the covered area must stay hidden (a hole, a fill face in another material). Never put two cuts of a part in one group: a part between two cuts with no edge loop between them (a box limb, a low-poly part) then has side faces whose corners all lie on the two rims, and they are sampled as cap (in the test, at rest, an 8-vertex box upper arm between a shoulder and an elbow cut read 14 of 84 from the front, back and right, and a triangulated six-sided forearm 42 of 140, where a dense count over the true caps read 0; with one group per cut the recipe was 0 exactly where the dense count was 0 in all 294 cut, camera and pose cells, on box, low-poly, weighted and skinned parts). Sample points over every cap face, never only the face centre: a cap that turns about its own centre keeps the centre hidden while its rim shows (in the test, centre sampling read 0 at a 70° head tilt while 10 of 25 grid points showed from the back). Sample each face through its triangles, so the whole face is covered whatever its shape: a Bisect-with-Fill cap is one n-gon, a Tripo or triangulated cap is a fan of triangles, and a cap can be concave (in the test a grid built from a face's first four corners covered one patch of a 16-gon cap and read 0 at a 60° tilt while 1,371 of 3,542 points of a dense count showed; on a triangle fan it stopped with an IndexError; this recipe read 37 of 98, and on the fan, the quad and a concave L-shaped cap it was 0 exactly where the dense count was 0). Take the points from the **evaluated** mesh: `ob.data` holds the rest positions, so a part moved by an Armature modifier (weighted or skinned) reads 0 at every pose with no error (in the test, the same head weighted 100 % to its bone: `ob.data` read 0 from every camera at a 70° tilt, the evaluated mesh read the same counts as the bone-parented head). An orthographic camera casts parallel rays along its view axis, not from its position (in the test, a close orthographic camera below the cap: 10 points by parallel rays, 5 by rays from its position).
```python
from mathutils import Vector
W = [(.6, .2, .2), (.2, .6, .2), (.2, .2, .6), (1 / 3, 1 / 3, 1 / 3), (.45, .45, .1), (.1, .45, .45), (.45, .1, .45)]
def tri_points(me, t):                                         # 7 points inside one triangle, 3 of them near its edges
    a, b, c = (me.vertices[i].co for i in t.vertices)
    return [a * u + b * v + c * w for u, v, w in W]
def ray_origin(cam, w):                                        # orthographic: start on the camera plane
    if cam.data.type == 'ORTHO':
        ax = (cam.matrix_world.to_3x3() @ Vector((0, 0, -1))).normalized()
        return w - ax * ax.dot(w - cam.matrix_world.translation)
    return cam.matrix_world.translation
def visible(ob, face, point, cam):                             # first hit is this cap face at this point
    w = ob.matrix_world @ point; o = ray_origin(cam, w); d = w - o
    hit, loc, _, idx, hob, _ = sc.ray_cast(dg, o, d.normalized(), distance=d.length + 1e-3)
    return hit and hob.original == ob and idx == face and (loc - w).length < 1e-3 * d.length
def cap_count(ob, cam, cut):                                   # one cut's cap or socket, posed: evaluated mesh, never ob.data
    g = ob.vertex_groups.get(f"cap_{cut}")
    if g is None: raise KeyError(f"{ob.name}: no 'cap_{cut}' vertex group")
    if not ob.visible_get(): raise RuntimeError(f"{ob.name} is hidden: its caps would read 0")
    ev = ob.evaluated_get(dg); me = ev.to_mesh(); me.calc_loop_triangles()
    caps = {v.index for v in me.vertices if any(x.group == g.index and x.weight > 0.99 for x in v.groups)}
    pts = [(t.polygon_index, p) for t in me.loop_triangles
           if set(me.polygons[t.polygon_index].vertices) <= caps for p in tri_points(me, t)]
    n = sum(visible(ob, f, p, cam) for f, p in pts)
    ev.to_mesh_clear(); return n, len(pts)                     # (visible, sampled)
def in_tris(tris, w, eps):                                     # w on or inside one of the triangles (w on their plane)
    for p, q, r in tris:
        n = (q - p).cross(r - p)
        if n.length > 1e-9 and all(n.normalized().dot((b - a).cross(w - a)) >= -eps * (b - a).length
                                   for a, b in ((p, q), (q, r), (r, p))): return True
    return False
def mark_plane_caps(ob, cut, co, no, child=None, eps=0.005):   # flat cap on §C cut plane `cut` (world space, rest pose)
    mw, no, tris = ob.matrix_world, no.normalized(), None      # child: ob is the parent, mark its socket
    if child:                                                  # only inside the child's cap outline (mark the child first)
        cg, cm = child.vertex_groups[f"cap_{cut}"], child.data; cm.calc_loop_triangles()
        cv = {v.index for v in cm.vertices if any(x.group == cg.index and x.weight > 0.99 for x in v.groups)}
        tris = [[child.matrix_world @ cm.vertices[i].co for i in t.vertices] for t in cm.loop_triangles
                if set(cm.polygons[t.polygon_index].vertices) <= cv]
    def keep(i):
        w = mw @ ob.data.vertices[i].co
        return abs(no.dot(w - co)) < eps and (tris is None or in_tris(tris, w, eps))
    vs = {i for p in ob.data.polygons if all(keep(i) for i in p.vertices) for i in p.vertices}
    g = ob.vertex_groups.get(f"cap_{cut}") or ob.vertex_groups.new(name=f"cap_{cut}"); g.add(sorted(vs), 1.0, 'REPLACE')
    return sum(set(p.vertices) <= vs for p in ob.data.polygons)   # cap or socket faces found
# per part and camera: {c: cap_count(ob, cam, c) for c in cuts}   cuts: the part's own id (if cut from its parent)
#   + each R-cut child's id whose socket is not recorded n/a (closed parent face)
```
Re-fetch `dg` after every pose change and every group change. Run it for every §C cut that bounds the part, except a socket recorded n/a. The pass, per cut and per camera, at rest and at every extreme: `visible` 0 with `sampled` above 0. A cut with no group (other than an n/a socket) stops with a KeyError; `sampled` 0 means the group holds no whole face at weight 1: never a pass. A part hidden in the viewport reads 0 with no error (in the test: 0 of 98 hidden, 37 of 98 shown), so the recipe stops on it; show every part, occluders too (a hidden occluder makes the count too high). The group is read from the evaluated mesh at weight 1, so a modifier that changes the topology anywhere in the stack (a Subdivision or a Mirror, before or after the Armature) is counted on the faces it makes (in the test, a Subdivision after the Armature: the old reading from `ob.data` sampled 0 points; this one samples the 16 cap quads the modifier makes and leaves out the side strips, which carry weight 0.5; it read 80 of 224 from the side at rest because the subdivided cap rises 0.11 to 0.20 above the cut plane, a real gap. A half head with a Mirror before the Armature: 98 points, as for the whole head, where `ob.data` gave 49). `sampled` 0 on a part with a modifier is the sign that the modifier dropped the group: count on a copy with it turned off.

**Where the `cap_<cut id>` groups come from:** the modeler puts each cap's and socket's faces in the group of its cut, at weight 1, and hands back the part files as a .blend working copy, because FBX drops a vertex group that is not bound to a bone (`rig-pipeline/references/modeler-handoff.md` `deliver` and C5). For a flat cap with no group (your own S2 proxy cuts, or a part handed back without it), `mark_plane_caps` selects the faces on that §C cut plane at rest into `cap_<cut id>`; run it once per cut of the part and check that each run found cap faces (one face per Bisect-with-Fill cut; in the test it found 1, and 16 for the same cap poked into a fan). On the parent side pass `child=` (above); a socket recorded n/a needs no group. Delete an existing `cap_<cut id>` group before you mark it again: `REPLACE` keeps the vertices already in it. A socket dome or a tucked cap with no group is an item in the fix note, never a guess. Keep the `cap_*` groups through the S5 weight cleanup: R-03 counts them on the real rig.

**Recipe 1 and `mark_plane_caps` are screening aids. Known false readings:** (a) a false 0 on a large low-poly cap: 7 fixed points per triangle miss a thin strip along the rim (in the test a box shoulder cap read 0 of 14 from the ¾-high camera where 10 to 12 of 210 dense points showed): any 0 on a cap of a few large faces, from a camera that sees the cap at a low angle, is checked on the still; (b) a false few on a socket cut along the child's outline: a ray that grazes the child's bottom rim passes the edge (3 of 112 from the game camera at rest; all three hidden when moved 0.0001 in the socket's plane); the same leak adds a few points to a real exposure (2 of 48, 9 of 55); (c) a socket marked without `child=` on a closed parent face (13 of 56 socket cells false in the test); (d) a group marked again without deleting it first keeps its old faces, while the found count looks right (the neck socket still read 6 of 14 at rest); (e) a stale `dg` reads the old pose or the old group (an emptied group still sampled 98 points); (f) a hidden occluder makes the count too high (a hidden part stops the recipe); (g) `mark_plane_caps` finds 0 on a posed part, a socket dome or a tucked cap (not on the plane); (h) not tested: a concave child outline with a parent face whose corners lie inside it and whose edge crosses outside it is kept. Not false: a subdivided cap that rises above its plane reads a real gap; `sampled` 0 after a modifier means the modifier dropped the group. Any FAIL, any borderline count and any 0 in case (a) is checked by eye on the still before a fix note.

**Recipe 2: part overlap.** World-space trees from the evaluated meshes; count overlapping face pairs for every pair of parts that are not parent and child; compare with the rest pose (in the test: 0 at rest, 8 head/forearm pairs with the hand pulled into the face).
```python
from mathutils.bvhtree import BVHTree
def tree(ob):
    ev = ob.evaluated_get(dg); m = ev.to_mesh()
    t = BVHTree.FromPolygons([ob.matrix_world @ v.co for v in m.vertices], [list(p.vertices) for p in m.polygons])
    ev.to_mesh_clear(); return t
pairs = len(tree(a).overlap(tree(b)))                          # a, b: parts that are not parent and child
```
For one skinned mesh, split the evaluated mesh by the planned regions (vertex groups) into temporary objects first, or the count includes neighbouring faces.

**Screening aid. Known false readings:** one skinned mesh not split by region counts neighbouring faces; parts that touch at rest count as pairs (so compare with the rest count); a parent and child pair is never counted (a hand through its own forearm reads 0); a near miss reads 0 (no distance). A new pair is checked on the still of that pose before it goes in a fix note.

**Recipe 3: head drift through a spin.** The rotation difference of the head from the clip's first frame, per frame; compare authoring rig, baked export skeleton and FBX re-import by clip frame. Do not read a bone matrix's Euler `z` as yaw: a bone's rest frame is rotated, so the Euler parts mix axes.
```python
import math
def drift(ob, bone, frames):
    q1, out = None, []
    for f in frames:
        sc.frame_set(f); q = (ob.matrix_world @ ob.pose.bones[bone].matrix).to_quaternion()
        q1 = q1 or q; out.append(round(math.degrees(q.rotation_difference(q1).angle), 2))
    return out
```
In the test, switch on: 0.0° every frame while the chest turned 180°; a default bake: the head followed the chest; a visual-key bake and the FBX re-import: 0.0°. The switch's target must be the head's rest world frame (`arm.matrix_world @ arm.data.bones["Head"].matrix_local`); a target at identity turned the head 90° at rest.

**Screening aid. Known false readings:** a bone matrix's Euler `z` read as yaw (the parts mix axes); absolute frames after the FBX re-import (one frame off: compare by clip frame); a copy that has the Action but no slot plays nothing, so it reads 0° on a frozen pose (check that the chest turns in the same frames). A drift above the tolerance is checked on the stills of the worst frame before a fix note.

**Recipe 4: scale keys in an export clip.** A visual-key bake writes a scale channel for every bone, all at 1.0 (45 channels in the test): harmless, since a Roblox pose stores only a CFrame. What fails is a scale **value** other than 1: count the scale F-curves that do.
```python
def scaled_channels(action, eps=1e-4):                         # Blender 5.x layered Actions
    return [fc.data_path for lay in action.layers for st in lay.strips for cb in st.channelbags
            for fc in cb.fcurves if fc.data_path.endswith("scale")
            and any(abs(k.co[1] - 1.0) > eps for k in fc.keyframe_points)]
```
An empty list is the pass; each listed channel is a push that Roblox will not play: give it a route (`rigging-design/references/design-for-motion.md` §3).

**Screening aid. Known false readings:** a count of every scale channel flags a bake's constant-1 channels (45 in the test; this recipe lists only values other than 1); none seen since. Run it on the export clip's Action, after the bake.

**Recipe 5: swing of a quaternion control in degrees.** The angle between the bone's own axis at rest and in the pose, from its own channels (parents ignored, twist about the bone's axis ignored). Use it for a range on a bone that turns about two axes in the same clip (hips that tilt during a spin), where `clip_check.py` rom on one quaternion component passes falsely (`references/controls-export-import.md` §3).
```python
def swing(ob, bone, frames):
    out = []
    for f in frames:
        sc.frame_set(f); y = ob.pose.bones[bone].matrix_basis.to_3x3() @ Vector((0, 1, 0))
        out.append(round(math.degrees(Vector((0, 1, 0)).angle(y)), 2))
    return out
```
The pass: the largest swing ≤ θ, the §B tilt range in degrees, never the manifest's ±sin(θ/2) component values (the control's validation query names θ: `references/controls-export-import.md` §3) (in the test, hips tilted 30° during a 180° spin: the component check read 0 and passed; the swing read 30.0°).

**Screening aid. Known false readings:** the largest swing compared with the manifest's ±sin(θ/2) component fails every tilt; a twist about the bone's own axis and a parent's turn read 0 by design (they have their own controls). A swing over θ is checked on the still of that frame before a fix note.

**Black-fill and game-camera renders:** one recipe for the studio, `animation-craft/references/blender-keying.md` §7 (magenta world, Workbench FLAT, single colour black); then `python tools/art/look_check.py silhouette <png> --out <full.json>`: in the test a head lifted off its socket read 2 components instead of 1. A front camera too close gave a box touching the frame edge (x0 = 0, x1 = width): reframe before trusting any number. `look_check.py` lists only components of 0.5 % of the image or more, so on a full phone frame a small figure's detached head, hand or the player-sized block is not listed and the count stays equal to rest (in the test: a 127 px figure on 1170x540 with its head lifted read 1, the same as rest). Count on a crop of the figure's box with a 10 % margin, then run `silhouette` on the crop:
```python
import json; from PIL import Image                             # args: full.json, frame.png, crop.png
b = json.load(open(full_json))["measurements"]["bbox_px"]; im = Image.open(frame_png); m = max(b["w"], b["h"]) // 10 + 4
im.crop((max(0, b["x0"] - m), max(0, b["y0"] - m), min(im.width, b["x1"] + m), min(im.height, b["y1"] + m))).save(crop_png)
```
In the test the crop read 2 at rest (figure and block) and 3 with the head lifted. The count is trusted only when the listed components' `area_px` add up to the mask's `area_px`; when they do not, a piece is still under the limit: render the count frame closer at the same angle.

**Screening aid. Known false readings of `look_check.py silhouette`:** a piece under 0.5 % of the image is not listed (full frame: 1 component with the head lifted, the same as rest); a box touching the frame edge means a cropped figure and every number is wrong; listed areas that do not add up to the mask area. A count above rest is looked at on the still before a fix note.

**Sampling clips for `clip_check.py`:** `clip_check.sample_clip(arm, {"hand_L": ("LowerArm_L", "tail"), ...}, manifest["controls"], start, end, contacts=[...], units="studs")`, then the CLI with `--up z`. The rom check reads the bone's own channels as the manifest names them; the channel and unit rules (quaternion channels by index, in `quat` units, never degrees) are in `references/controls-export-import.md` §3 (in the test `rotation_quaternion.w` read the z component and reported a false over-range on every frame; an Euler channel on a quaternion bone read 0 and passed; a degree range on a quaternion channel passed a 30° tilt against ±15°). Measure controls moved by constraints or IK on the baked export skeleton. Pops needs a landmark off the spin axis (in the test a wrap from 170° to -170° read 8.3 times the median on the hand, nothing on the head on the axis). **Screening aid. Known false readings of `clip_check.py`:** `rotation_quaternion.w` reads the z component (a false over-range on every frame); an Euler channel on a quaternion bone reads 0 and passes; a degree range on a quaternion channel always passes; a tilt during a spin passes the `quat` range (use recipe 5); pops on a landmark on the spin axis reads nothing; a control moved by a constraint or IK reads its basis channels only. A FAIL is checked on the stills of the frames it names before a fix note.

