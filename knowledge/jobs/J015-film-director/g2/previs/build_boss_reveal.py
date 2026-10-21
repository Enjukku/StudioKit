# J015 G2 boss-reveal greybox previs: builds a NEW .blend (never opens an existing one).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# Run headless:
#   blender -b --factory-startup --python build_boss_reveal.py -- <out.blend> <events.json>
# Units: 1 Blender unit = 1 stud (kit-test assumption, no game scale chain). Z up. The guardian faces -X,
# the explorer faces +X; every authored camera except CAM_E sits on the south (-Y) side of the action axis.
# Event frames below are authored acting choices (PROPOSAL); shot cuts are placed on the event that ends each
# shot, and tools/film/shotlist.py measures the shot lengths from the resulting `shot:<id>` markers.
import json
import math
import sys

import bmesh
import bpy
from mathutils import Euler, Quaternion, Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT_BLEND = argv[0] if argv else "boss-reveal_previs.blend"
OUT_EVENTS = argv[1] if len(argv) > 1 else "events.json"

START = 1
# Shot-relative event frames (offset from the shot's first frame). "end" = the cut event (the next shot's
# first frame offset). Reasons are in g2/beat-sheet.md and g2/animatic-manifest.md.
EV = {
    "B": {"pulse_peak": 5, "pulse_rise": 18, "collapse": 20, "ember": 26, "hand_stop": 26, "ripple1": 28,
          "ripple2": 37, "end": None},  # end measured below: the first ripple reaches the pedestal foot
    "C": {"crack": 3, "look_start": 7, "look_end": 17, "hand_down_start": 16, "hand_down_end": 26,
          "step_start": 20, "step_land": 34, "end": 36},
    "D": {"rise_start": 0, "head_start": 6, "rise_end": 30, "head_up": 30, "eyes": 32, "eyes_full": 38,
          "gaze_start": 40, "gaze_end": 50, "vocal": 50, "arm_back_start": 52, "arm_back_end": 62,
          "end": 64},
    "E": {"strike": 7, "settle_end": 30, "ember_pulse": 20, "control": 37, "end": 38},
}
ORDER = ["B", "C", "D", "E"]
SHOT_START = {}
LAST_FRAME = START


def compute_starts():
    global LAST_FRAME
    f = START
    for sid in ORDER:
        SHOT_START[sid] = f
        f += EV[sid]["end"]
    LAST_FRAME = f - 1


EV["B"]["end"] = 46  # provisional until the ripple is measured
compute_starts()


def g(sid, key):
    """Global frame of a shot-relative event."""
    return SHOT_START[sid] + EV[sid][key]


# ------------------------------------------------------------------ scene
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.name = "boss-reveal"
scene.render.fps = 30
scene.render.fps_base = 1.0
scene.frame_start = START
scene.frame_end = LAST_FRAME
scene.render.resolution_x = 960
scene.render.resolution_y = 540
scene.render.pixel_aspect_x = 1.0
scene.render.pixel_aspect_y = 1.0
scene.render.engine = "BLENDER_EEVEE"
scene.eevee.taa_render_samples = 16
try:
    scene.view_settings.view_transform = "Standard"
except TypeError:
    pass
scene.unit_settings.system = "NONE"

world = bpy.data.worlds.new("night")
scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value = (0.010, 0.013, 0.022, 1.0)
bg.inputs["Strength"].default_value = 1.0


def mat(name, color, emit=None, strength=0.0, rough=0.7, alpha=1.0, spec=0.3):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    p = m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = (*color, 1.0)
    p.inputs["Roughness"].default_value = rough
    if "Specular IOR Level" in p.inputs:
        p.inputs["Specular IOR Level"].default_value = spec
    if emit is not None:
        p.inputs["Emission Color"].default_value = (*emit, 1.0)
        p.inputs["Emission Strength"].default_value = strength
    if alpha < 1.0:
        p.inputs["Alpha"].default_value = alpha
        m.surface_render_method = "BLENDED"
    return m


M = {
    "wall": mat("stone_wall", (0.16, 0.16, 0.17)),
    "floor": mat("stone_floor", (0.20, 0.19, 0.18)),
    "water": mat("water", (0.015, 0.03, 0.045), rough=0.06, spec=0.8),
    "statue": mat("statue_stone", (0.30, 0.29, 0.27)),
    "pedestal": mat("pedestal", (0.26, 0.25, 0.24)),
    "beacon": mat("beacon", (1.0, 0.55, 0.12), emit=(1.0, 0.55, 0.12), strength=12.0),
    "eyes": mat("guardian_eyes", (1.0, 0.55, 0.12), emit=(1.0, 0.55, 0.12), strength=0.0),
    "explorer": mat("explorer", (0.92, 0.86, 0.72)),
    "pack": mat("explorer_pack", (0.45, 0.33, 0.20)),
    "visor": mat("explorer_visor", (0.03, 0.03, 0.03)),
    "ghost": mat("ghost_avatar", (0.2, 0.8, 0.9), alpha=0.35),
    "daylight": mat("exit_daylight", (0.0, 0.0, 0.0), emit=(0.85, 0.9, 1.0), strength=0.32),  # pure glow, unlit; below the moon shaft in value (v14)
    "shaft": mat("moon_shaft", (0.6, 0.7, 1.0), emit=(0.6, 0.7, 1.0), strength=0.6, alpha=0.07),
    "ripple": mat("ripple", (0.6, 0.7, 0.8), emit=(0.6, 0.7, 0.8), strength=0.8),
}

COLL = {}


def coll(name):
    if name not in COLL:
        c = bpy.data.collections.new(name)
        scene.collection.children.link(c)
        COLL[name] = c
    return COLL[name]


def link(obj, cname):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    coll(cname).objects.link(obj)
    return obj


def box(name, size, loc, material, cname, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0))
    o = bpy.context.active_object
    o.name = name
    o.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.location = loc
    o.data.materials.append(material)
    if parent is not None:
        o.parent = parent
    return link(o, cname)


def cyl(name, r, depth, loc, material, cname, verts=32, parent=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth, location=loc)
    o = bpy.context.active_object
    o.name = name
    o.data.materials.append(material)
    if parent is not None:
        o.parent = parent
    return link(o, cname)


def sphere(name, r, loc, material, cname, parent=None):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=r, location=loc)
    o = bpy.context.active_object
    o.name = name
    o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    if parent is not None:
        o.parent = parent
    return link(o, cname)


def empty(name, loc, cname, parent=None):
    o = bpy.data.objects.new(name, None)
    o.empty_display_size = 0.5
    o.location = loc
    coll(cname).objects.link(o)
    if parent is not None:
        o.parent = parent
    return o


# ------------------------------------------------------------------ set
ROOM_R = 30.0
# walls: open cylinder
bm = bmesh.new()
bmesh.ops.create_circle(bm, cap_ends=False, radius=ROOM_R, segments=64)
geom = bmesh.ops.extrude_edge_only(bm, edges=bm.edges[:])
for v in [e for e in geom["geom"] if isinstance(e, bmesh.types.BMVert)]:
    v.co.z += 30.0
me = bpy.data.meshes.new("wall")
bm.to_mesh(me)
bm.free()
wall = bpy.data.objects.new("SET_wall", me)
wall.data.materials.append(M["wall"])
coll("SET").objects.link(wall)
wall.location.z = -1.5

# ceiling with an oculus above the guardian's risen head
OCULUS = Vector((7.5, 0.0))
bm = bmesh.new()
outer = bmesh.ops.create_circle(bm, cap_ends=False, radius=ROOM_R, segments=64)["verts"]
inner = bmesh.ops.create_circle(bm, cap_ends=False, radius=2.6, segments=64)["verts"]
for v in inner:
    v.co.x += OCULUS.x
bmesh.ops.bridge_loops(bm, edges=[e for e in bm.edges])
me = bpy.data.meshes.new("ceiling")
bm.to_mesh(me)
bm.free()
ceil = bpy.data.objects.new("SET_ceiling", me)
ceil.data.materials.append(M["wall"])
ceil.location.z = 28.5
coll("SET").objects.link(ceil)

bpy.ops.mesh.primitive_circle_add(vertices=64, radius=ROOM_R, fill_type="NGON", location=(0, 0, 0))
water = link(bpy.context.active_object, "SET")
water.name = "SET_water"
water.data.materials.append(M["water"])

cyl("SET_dais", 6.0, 1.3, (0, 0, -0.9), M["floor"], "SET", verts=48)  # top at z = -0.25: under the flood water


def causeway(name, a, b, width=3.0):
    a, b = Vector(a), Vector(b)
    mid = (a + b) / 2
    d = b - a
    o = box(name, (d.length, width, 1.3), (mid.x, mid.y, -0.9), M["floor"], "SET")
    o.rotation_euler.z = math.atan2(d.y, d.x)
    return o


causeway("SET_causeway_entry", (-28.0, 0.0), (-5.0, 0.0))
EXIT = Vector((-5.2, 29.5))  # v13: north-north-west wall: a retreat away from the guardian, left of the explorer in E
causeway("SET_causeway_exit", (0.5, 5.5), (EXIT.x * 0.95, EXIT.y * 0.95))
box("SET_entry_landing", (5.0, 9.0, 3.3), (-28.0, 0.0, 0.15), M["floor"], "SET")

# exit arch on the north-east wall, facing the room centre
ang = math.atan2(EXIT.y, EXIT.x)
arch = empty("SET_exit_arch", (EXIT.x, EXIT.y, 0.3), "SET")
arch.rotation_euler.z = ang
for side in (-1, 1):
    box(f"SET_exit_pillar_{'L' if side < 0 else 'R'}", (1.8, 1.6, 12.0), (-0.9, side * 3.6, 6.0), M["wall"], "SET",
        parent=arch)
box("SET_exit_lintel", (1.8, 8.8, 1.6), (-0.9, 0.0, 12.8), M["wall"], "SET", parent=arch)
box("SET_exit_daylight", (0.1, 5.6, 12.0), (-0.35, 0.0, 6.0), M["daylight"], "SET", parent=arch)
# entry arch on the west wall (dark: the way the player came)
entry = empty("SET_entry_arch", (-ROOM_R + 0.3, 0.0, 1.8), "SET")
for side in (-1, 1):
    box(f"SET_entry_pillar_{side}", (1.4, 1.4, 8.0), (0.0, side * 2.6, 4.0), M["wall"], "SET", parent=entry)
box("SET_entry_lintel", (1.4, 6.6, 1.2), (0.0, 0.0, 8.6), M["wall"], "SET", parent=entry)

# columns around the wall (depth cues); keep the arches clear
for i in range(16):
    a = 2 * math.pi * i / 16
    p = Vector((math.cos(a), math.sin(a))) * 27.6
    if (p - EXIT).length < 7 or (p - Vector((-30, 0))).length < 7:
        continue
    cyl(f"SET_column_{i:02d}", 1.0, 30.0, (p.x, p.y, 13.5), M["wall"], "SET", verts=16)

# pedestal and beacon
cyl("PROP_pedestal", 0.8, 3.75, (0, 0, 1.625), M["pedestal"], "PROPS")
BEACON_POS = Vector((0.0, 0.0, 3.95))
beacon = sphere("PROP_beacon", 0.45, BEACON_POS, M["beacon"], "PROPS")
bl = bpy.data.lights.new("LIGHT_beacon", "POINT")
bl.color = (1.0, 0.55, 0.12)
bl.shadow_soft_size = 0.4
blo = bpy.data.objects.new("LIGHT_beacon", bl)
blo.location = BEACON_POS + Vector((0, 0, 0.0))
coll("LIGHTS").objects.link(blo)

# moonlight: a narrow spot through the oculus + a faint visible shaft
moon = bpy.data.lights.new("LIGHT_moon", "SPOT")
moon.color = (0.62, 0.72, 1.0)
moon.energy = 60000.0
moon.spot_size = math.radians(9.0)
moon.spot_blend = 0.15
moon.shadow_soft_size = 0.3
mo = bpy.data.objects.new("LIGHT_moon", moon)
mo.location = (OCULUS.x, OCULUS.y, 44.0)
coll("LIGHTS").objects.link(mo)
bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=3.2, radius2=0.25, depth=26.5,
                                location=(OCULUS.x, OCULUS.y, 15.25))
shaft = link(bpy.context.active_object, "LIGHTS")
shaft.name = "FX_moon_shaft"
shaft.data.materials.append(M["shaft"])

fill = bpy.data.lights.new("LIGHT_fill", "SUN")
fill.color = (0.45, 0.55, 0.8)
fill.energy = 2.5
fo = bpy.data.objects.new("LIGHT_fill", fill)
fo.rotation_euler = Vector((1.0, 0.8, -0.8)).to_track_quat("-Z", "Y").to_euler()  # from the south-west, behind CAM_E
coll("LIGHTS").objects.link(fo)

# the exit reads by its own glow (no extra light: an area light here washed out shots C and D)

KNEE_BASE = Vector((5.3, -1.5, 0.03))  # front edge of the statue plinth, in the water


def ripple(name, f0, frames=18, grow=4.2):
    bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.05, location=KNEE_BASE)
    o = link(bpy.context.active_object, "FX")
    o.name = name
    o.data.materials.append(M["ripple"])
    for f, s, hide in ((f0 - 1, 0.01, True), (f0, 0.9, False), (f0 + frames, grow, False),
                       (f0 + frames + 6, grow * 1.2, True)):
        o.scale = (s, s, 1.0)
        o.keyframe_insert("scale", frame=f)
        o.hide_render = hide
        o.hide_viewport = hide
        o.keyframe_insert("hide_render", frame=f)
        o.keyframe_insert("hide_viewport", frame=f)
    return o


ripple("FX_ripple_1", g("B", "ripple1"), grow=6.0)
ripple("FX_ripple_2", g("B", "ripple2"), grow=6.0)


# measure the cut event: frame at which ripple 1's radius reaches the pedestal's foot
PED_R = 0.8
dist = (KNEE_BASE.to_2d() - Vector((0.0, 0.0))).length - PED_R
r1 = bpy.data.objects["FX_ripple_1"]
arrival = None
for f in range(g("B", "ripple1"), g("B", "ripple1") + 30):
    scene.frame_set(f)
    if r1.scale.x >= dist:
        arrival = f
        break
EV["B"]["end"] = arrival - SHOT_START["B"]
compute_starts()
MEASURED = {"ripple1_reaches_pedestal_frame": arrival, "ripple_distance_studs": round(dist, 3)}

ww = bpy.data.lights.new("LIGHT_wallwash", "AREA")
ww.color = (0.5, 0.6, 0.85)
ww.energy = 3500.0
ww.size = 10.0
wo = bpy.data.objects.new("LIGHT_wallwash", ww)
wo.location = (10.0, 12.0, 3.0)
wo.rotation_euler = (Vector((9.0, 29.0, 13.0)) - Vector((8.0, 12.0, 3.0))).to_track_quat("-Z", "Y").to_euler()
coll("LIGHTS").objects.link(wo)

# ------------------------------------------------------------------ guardian (faces -X)
G_hips = empty("GUARD_hips", (8.0, 0.0, 3.8), "GUARDIAN")
box("GUARD_plinth", (6.0, 6.4, 1.0), (8.6, 0.0, -0.2), M["floor"], "GUARDIAN")
box("GUARD_legs", (3.6, 4.8, 3.6), (8.7, 0.0, 2.1), M["statue"], "GUARDIAN")
box("GUARD_knee_fwd", (1.8, 1.8, 2.7), (6.3, -1.5, 1.65), M["statue"], "GUARDIAN")
G_torso = empty("GUARD_torso_pivot", (0, 0, 0), "GUARDIAN", parent=G_hips)
box("GUARD_torso", (3.0, 5.4, 6.6), (0.0, 0.0, 3.3), M["statue"], "GUARDIAN", parent=G_torso)
G_neck = empty("GUARD_neck", (-0.3, 0.0, 6.6), "GUARDIAN", parent=G_torso)
G_head = box("GUARD_head", (2.6, 2.4, 2.6), (-0.2, 0.0, 1.4), M["statue"], "GUARDIAN", parent=G_neck)
for side in (-1, 1):
    sphere(f"GUARD_eye_{'L' if side < 0 else 'R'}", 0.34, (-1.52, side * 0.62, 1.7), M["eyes"], "GUARDIAN",
           parent=G_neck)
G_sh = {}
G_hand = {}
for side, tag in ((-1, "L"), (1, "R")):  # L = the guardian's left = -Y = camera side
    sh = empty(f"GUARD_shoulder_{tag}", (0.0, side * 3.3, 5.8), "GUARDIAN", parent=G_torso)
    box(f"GUARD_arm_{tag}", (1.5, 1.5, 7.2), (0.0, 0.0, -3.6), M["statue"], "GUARDIAN", parent=sh)
    G_hand[tag] = box(f"GUARD_hand_{tag}", (2.2, 2.0, 1.3), (0.0, 0.0, -7.6), M["statue"], "GUARDIAN", parent=sh)
    G_sh[tag] = sh

# ------------------------------------------------------------------ explorer (faces +X), plus avatar-range ghosts
AVATAR_H = 5.75  # Roblox "Normal" body scale is roughly 5.75-6.5 studs, Classic roughly 4.75
# (knowledge/external/roblox-creator-docs/art/accessories/body-scale.md:24-36)
X_START = Vector((-2.5, 0.0, -0.25))  # ankle-deep in the flood
X_BACK = Vector((-4.9, 0.0, -0.25))


def make_explorer(prefix, scale, material, cname):
    root = empty(prefix + "root", X_START, cname)
    root.scale = (scale, scale, scale)
    parts = {"root": root}
    for side in (-1, 1):
        box(f"{prefix}leg_{side}", (0.9, 0.9, 2.2), (0.0, side * 0.5, 1.1), material, cname, parent=root)
    hips = empty(prefix + "hips", (0, 0, 2.2), cname, parent=root)
    box(prefix + "torso", (1.0, 2.0, 2.25), (0.0, 0.0, 1.125), material, cname, parent=hips)
    box(prefix + "pack", (0.7, 1.6, 1.4), (-0.85, 0.0, 1.2), M["pack"] if material is M["explorer"] else material,
        cname, parent=hips)
    neck = empty(prefix + "neck", (0, 0, 2.25), cname, parent=hips)
    box(prefix + "head", (1.3, 1.3, 1.3), (0.0, 0.0, 0.65), material, cname, parent=neck)
    box(prefix + "visor", (0.12, 0.95, 0.35), (0.66, 0.0, 0.75), M["visor"] if material is M["explorer"] else material,
        cname, parent=neck)
    for side, tag in ((-1, "R"), (1, "L")):  # explorer's right = -Y = camera side
        sh = empty(f"{prefix}shoulder_{tag}", (0.0, side * 1.45, 2.0), cname, parent=hips)
        sh.rotation_mode = "QUATERNION"
        box(f"{prefix}arm_{tag}", (0.85, 0.85, 2.2), (0.0, 0.0, -1.1), material, cname, parent=sh)
        parts["sh_" + tag] = sh
    parts.update({"hips": hips, "neck": neck})
    return parts


EXP = make_explorer("EXP_", 1.0, M["explorer"], "EXPLORER")
GHOSTS = [make_explorer("GHOST_small_", 4.75 / AVATAR_H, M["ghost"], "CHECK_GHOSTS"),
          make_explorer("GHOST_tall_", 6.5 / AVATAR_H, M["ghost"], "CHECK_GHOSTS")]
for o in coll("CHECK_GHOSTS").objects:
    o.hide_render = True


def key(o, path, f, value):
    setattr(o, path, value)
    o.keyframe_insert(path, frame=f)


def reach_quat(parts, frac):
    """Shoulder rotation (in the hips' space) that points the right arm at the beacon; frac 0..1 slerps."""
    bpy.context.view_layer.update()
    sh = parts["sh_R"]
    sh_world = sh.matrix_world.translation
    d_world = (BEACON_POS - sh_world).normalized()
    parent_rot = parts["hips"].matrix_world.to_quaternion()
    d_local = parent_rot.inverted() @ d_world
    q = Vector((0, 0, -1)).rotation_difference(d_local)
    return Quaternion().slerp(q, frac)


def animate_explorer(parts):
    root, hips, neck, shR = parts["root"], parts["hips"], parts["neck"], parts["sh_R"]
    b0, bstop = SHOT_START["B"], g("B", "hand_stop")
    key(root, "location", b0, X_START.copy())
    key(hips, "rotation_euler", b0, Euler((0, math.radians(4), 0)))
    key(neck, "rotation_euler", b0, Euler((0, math.radians(14), 0)))  # looking down at the beacon
    key(shR, "rotation_quaternion", b0, reach_quat(parts, 0.35))
    key(hips, "rotation_euler", bstop, Euler((0, math.radians(9), 0)))
    key(shR, "rotation_quaternion", bstop, reach_quat(parts, 0.86))
    key(shR, "rotation_quaternion", bstop + 5, reach_quat(parts, 0.80))  # flinch
    # C: look up past the beacon, hand down, one step back
    key(neck, "rotation_euler", g("C", "look_start"), Euler((0, math.radians(14), 0)))
    key(neck, "rotation_euler", g("C", "look_end"), Euler((0, math.radians(-24), 0)))
    key(shR, "rotation_quaternion", g("C", "hand_down_start"), reach_quat(parts, 0.80))
    key(shR, "rotation_quaternion", g("C", "hand_down_end"), Quaternion((1, 0, 0, 0)))
    key(root, "location", g("C", "step_start"), X_START.copy())
    key(root, "location", g("C", "step_land"), X_BACK.copy())
    key(hips, "rotation_euler", g("C", "step_start"), Euler((0, math.radians(9), 0)))
    key(hips, "rotation_euler", g("C", "step_land"), Euler((0, math.radians(-7), 0)))
    # D/E: the gaze follows the guardian's head, weight stays back
    key(neck, "rotation_euler", g("D", "head_up"), Euler((0, math.radians(-28), 0)))
    key(neck, "rotation_euler", g("E", "strike"), Euler((0, math.radians(-20), 0)))
    key(hips, "rotation_euler", g("E", "strike"), Euler((0, math.radians(-12), 0)))
    key(hips, "rotation_euler", g("E", "settle_end"), Euler((0, math.radians(-5), 0)))


for p in [EXP] + GHOSTS:
    animate_explorer(p)

# ------------------------------------------------------------------ guardian animation
def gkey(o, f, deg_y, deg_z=0.0):
    key(o, "rotation_euler", f, Euler((0, math.radians(deg_y), math.radians(deg_z))))


TORSO_BOW, TORSO_UP, TORSO_SETTLE = -32.0, 2.0, -48.0
HEAD_BOW, HEAD_UP, HEAD_GAZE = -40.0, 14.0, -14.0
ARM_REST = 4.0  # hands rest on the floor beside the knees, outside shot B's frame (no hand next to the explorer's hand)
gkey(G_torso, SHOT_START["B"], TORSO_BOW)
gkey(G_neck, SHOT_START["B"], HEAD_BOW)
for tag in ("L", "R"):
    gkey(G_sh[tag], SHOT_START["B"], ARM_REST)
gkey(G_torso, g("C", "crack"), TORSO_BOW)
gkey(G_torso, g("C", "crack") + 4, TORSO_BOW + 1.5)  # the crack: a shiver, off screen
gkey(G_torso, g("D", "rise_start"), TORSO_BOW + 1.5)
gkey(G_torso, g("D", "rise_end"), TORSO_UP)
gkey(G_neck, g("D", "head_start"), HEAD_BOW)
gkey(G_neck, g("D", "head_up"), HEAD_UP)
gkey(G_neck, g("D", "gaze_start"), HEAD_UP)
gkey(G_neck, g("D", "gaze_end"), HEAD_GAZE)
gkey(G_sh["L"], g("D", "arm_back_start"), ARM_REST)
gkey(G_sh["L"], g("D", "arm_back_end"), 150.0)

# solve the strike: torso settles forward, left hand lands between the explorer and the beacon
STRIKE_TARGET = Vector((-1.6, -1.1, 0.4))  # hand centre; the hand's underside is then on the flooded dais
HIPS_REST, HIPS_SETTLE = Vector((8.0, 0.0, 3.8)), Vector((5.0, 0.0, 3.5))  # the strike is a lunge forward
G_hips.location = HIPS_SETTLE
G_torso.rotation_euler = Euler((0, math.radians(TORSO_SETTLE), 0))
best = None
for deg in range(30, 151):
    for xdeg in range(0, 41, 2):
        G_sh["L"].rotation_euler = Euler((math.radians(xdeg), math.radians(deg), 0))
        bpy.context.view_layer.update()
        err = (G_hand["L"].matrix_world.translation - STRIKE_TARGET).length
        if best is None or err < best[1]:
            best = (deg, err, xdeg)
STRIKE_ARM, STRIKE_ARM_X = float(best[0]), float(best[2])
G_hips.location = HIPS_REST
key(G_hips, "location", SHOT_START["B"], HIPS_REST.copy())
key(G_hips, "location", g("D", "rise_end"), HIPS_REST.copy())
key(G_hips, "location", g("E", "strike"), HIPS_SETTLE.copy())
strike_f = g("E", "strike")
gkey(G_torso, strike_f, TORSO_SETTLE)
key(G_sh["L"], "rotation_euler", strike_f, Euler((math.radians(STRIKE_ARM_X), math.radians(STRIKE_ARM), 0)))
gkey(G_torso, g("E", "settle_end"), TORSO_SETTLE + 4.0)
key(G_sh["L"], "rotation_euler", g("E", "settle_end"),
    Euler((math.radians(STRIKE_ARM_X), math.radians(STRIKE_ARM - 4.0), 0)))
gkey(G_neck, strike_f, HEAD_GAZE + 6.0)
gkey(G_neck, g("E", "settle_end"), HEAD_GAZE + 10.0)
gkey(G_sh["R"], g("D", "rise_end"), ARM_REST)
gkey(G_sh["R"], g("E", "settle_end"), 40.0)  # the far arm curls around the pedestal side


# ------------------------------------------------------------------ light and effect animation
def light_key(f, energy):
    bl.energy = energy
    bl.keyframe_insert("energy", frame=f)


def emis_key(material, f, strength):
    node = material.node_tree.nodes.get("Principled BSDF").inputs["Emission Strength"]
    node.default_value = strength
    node.keyframe_insert("default_value", frame=f)


PULSE_HI, PULSE_LO, EMBER = 700.0, 220.0, 20.0
b = SHOT_START["B"]
for f, e in ((b, 600.0), (g("B", "pulse_peak"), PULSE_HI), (b + 15, PULSE_LO), (g("B", "pulse_rise"), 420.0),
             (g("B", "collapse"), 470.0), (g("B", "ember"), EMBER), (g("E", "ember_pulse"), EMBER),
             (g("E", "ember_pulse") + 15, 110.0), (LAST_FRAME, 60.0)):
    light_key(f, e)
for f, s in ((b, 1.6), (g("B", "pulse_peak"), 2.4), (b + 15, 1.0), (g("B", "pulse_rise"), 1.4),
             (g("B", "collapse"), 1.5), (g("B", "ember"), 0.25), (g("E", "ember_pulse"), 0.25),
             (g("E", "ember_pulse") + 15, 0.9), (LAST_FRAME, 0.6)):
    emis_key(M["beacon"], f, s)
for f, s in ((b, 0.0), (g("D", "eyes"), 0.0), (g("D", "eyes_full"), 7.0), (LAST_FRAME, 5.0)):
    emis_key(M["eyes"], f, s)

# splash proxy at the strike (VFX owns the real effect; this only marks where and when)
bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=1.6, radius2=0.2, depth=1.0,
                                location=(STRIKE_TARGET.x, STRIKE_TARGET.y, 0.4))
splash = link(bpy.context.active_object, "FX")
splash.name = "FX_splash_marker"
splash.data.materials.append(M["ripple"])
contact_f = strike_f - 1  # the hand reaches the floor one frame before its pose key (measured in v5-v9)
for f, s, hide in ((contact_f - 1, 0.01, True), (contact_f, 0.6, False), (contact_f + 8, 1.6, False),
                   (contact_f + 12, 1.7, True)):
    splash.scale = (s, s, s)
    splash.keyframe_insert("scale", frame=f)
    splash.hide_render = hide
    splash.keyframe_insert("hide_render", frame=f)


# ------------------------------------------------------------------ cameras (static; lens objects recorded)
def camera(name, loc, target, focal, sensor=36.0, fit="HORIZONTAL", cname="CAMERAS"):
    cd = bpy.data.cameras.new(name)
    cd.lens = focal
    cd.sensor_fit = fit
    cd.sensor_width = sensor
    cd.clip_start = 0.1
    cd.clip_end = 400.0
    co = bpy.data.objects.new(name, cd)
    co.location = loc
    direction = Vector(target) - Vector(loc)
    co.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    coll(cname).objects.link(co)
    co["look_at"] = list(target)
    return co


def focal_for_vfov(vdeg, sensor=36.0, aspect=16 / 9):
    return (sensor / aspect) / (2 * math.tan(math.radians(vdeg) / 2))


CAMS = {
    "B": camera("CAM_B", (-3.2, -6.5, 7.4), (1.2, 0.0, 1.4), 30.0),
    "C": camera("CAM_C", (-1.8, -9.5, 4.0), (-3.5, 0.0, 4.0), 28.0),  # v11: beacon back inside the 4:3 centre
    "D": camera("CAM_D", (0.5, -21.0, 1.2), (3.6, 0.0, 6.6), 24.0),
    "E": camera("CAM_E", (-12.5, -13.0, 9.0), (-4.9, 0.0, 3.2), focal_for_vfov(70.0)),  # v13: over the right shoulder: avatar between exit (left) and guardian (right), no overlap
}
# alternatives and helpers (not shots; never bound to a marker)
ALT_D = camera("ALT_D_tilt", (1.5, -11.0, 1.2), (4.4, 0.0, 6.0), 30.0, cname="CAMERAS_ALT")
alt_target = empty("ALT_D_tilt_target", (4.4, 0.0, 6.0), "CAMERAS_ALT")
c = ALT_D.constraints.new("DAMPED_TRACK")
c.target = alt_target
c.track_axis = "TRACK_NEGATIVE_Z"
alt_target.location = (4.4, 0.0, 6.0)
alt_target.keyframe_insert("location", frame=g("D", "rise_start"))
alt_target.location = (7.4, 0.0, 12.2)
alt_target.keyframe_insert("location", frame=g("D", "head_up"))
alt_target.location = (6.6, 0.0, 10.6)
alt_target.keyframe_insert("location", frame=g("D", "gaze_end"))
camera("PLAYCAM_beat1", (-26.0, -3.5, 9.0), (2.0, 2.5, 4.5), focal_for_vfov(70.0), cname="CAMERAS_ALT")
cd = bpy.data.cameras.new("MAPCAM_top")
cd.type = "ORTHO"
cd.ortho_scale = 66.0
mapcam = bpy.data.objects.new("MAPCAM_top", cd)
mapcam.location = (0, 0, 80)
coll("CAMERAS_ALT").objects.link(mapcam)

for o in bpy.data.objects:
    if o.name.startswith(("PROP_beacon", "GUARD_eye", "FX_", "SET_exit_daylight")):
        o.visible_shadow = False

# ------------------------------------------------------------------ markers + sequence props
scene.frame_start, scene.frame_end = START, LAST_FRAME  # after the ripple measurement moved the cuts (bug fix v9)
for sid in ORDER:
    m = scene.timeline_markers.new("shot:" + sid, frame=SHOT_START[sid])
    m.camera = CAMS[sid]
scene.camera = CAMS["B"]
scene["film_sequence"] = "boss-reveal"
scene["film_revision"] = 1

# burn-in for review movies (frame, marker, camera, lens); the board-input stills switch it off
r = scene.render
r.use_stamp = True
for attr, val in (("use_stamp_date", False), ("use_stamp_time", False), ("use_stamp_render_time", False),
                  ("use_stamp_frame", True), ("use_stamp_marker", True), ("use_stamp_camera", True),
                  ("use_stamp_lens", True), ("use_stamp_scene", False), ("use_stamp_filename", False),
                  ("use_stamp_memory", False), ("use_stamp_hostname", False), ("use_stamp_note", True)):
    if hasattr(r, attr):
        setattr(r, attr, val)
r.stamp_note_text = "boss-reveal greybox previs (J015 G2) - proxies, temp light"
r.stamp_font_size = 14

# measured, not authored: when the head enters the moon shaft, and when the strike hand reaches the floor
def shaft_radius(z):
    return 3.2 - (z - 2.0) * (2.95 / 26.5)


head_in = hand_down = None
for f in range(SHOT_START["D"], LAST_FRAME + 1):
    scene.frame_set(f)
    hp = G_head.matrix_world.translation
    if head_in is None and (hp.to_2d() - OCULUS).length < shaft_radius(hp.z):
        head_in = f
    if hand_down is None and f >= SHOT_START["E"] and G_hand["L"].matrix_world.translation.z <= STRIKE_TARGET.z + 0.25:
        hand_down = f
MEASURED.update({"head_enters_moon_shaft_frame": head_in, "eyes_frame": g("D", "eyes"),
                 "strike_hand_on_floor_frame": hand_down, "strike_key_frame": g("E", "strike")})

events = {"start_frame": START, "last_frame": LAST_FRAME, "shot_start": SHOT_START,
          "measured": MEASURED, "events_rel": EV, "strike_arm_deg": [STRIKE_ARM_X, STRIKE_ARM], "strike_err": best[1],
          "cameras": {k: {"name": v.name, "focal_mm": v.data.lens, "sensor_mm": v.data.sensor_width,
                          "sensor_fit": v.data.sensor_fit, "location": list(v.location),
                          "look_at": list(v["look_at"])} for k, v in CAMS.items()},
          "blender_version": bpy.app.version_string}
with open(OUT_EVENTS, "w", encoding="utf-8") as fh:
    json.dump(events, fh, indent=2)
scene.frame_set(START)
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND)
print("BUILD OK", json.dumps({"blend": OUT_BLEND, "last_frame": LAST_FRAME, "shot_start": SHOT_START,
                              "strike_arm": STRIKE_ARM, "strike_err": round(best[1], 3)}))
