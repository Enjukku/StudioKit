# Top-down blocking map: orthographic Workbench render of the proxies (ceiling and light shaft hidden).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# blender -b <file.blend> --python render_map.py -- <out_dir> <frame> [<frame> ...]
import os
import sys

import bpy

a = sys.argv[sys.argv.index("--") + 1:]
outdir, frames = a[0], [int(x) for x in a[1:]]
os.makedirs(outdir, exist_ok=True)
scene = bpy.context.scene
for name in ("SET_ceiling", "FX_moon_shaft"):
    bpy.data.objects[name].hide_render = True
scene.render.engine = "BLENDER_WORKBENCH"
scene.display.shading.light = "FLAT"
scene.display.shading.color_type = "OBJECT"
COLS = (("SET_water", (0.05, 0.09, 0.14, 1)), ("SET_wall", (0.35, 0.35, 0.37, 1)), ("SET_column", (0.3, 0.3, 0.32, 1)),
        ("SET_exit", (0.85, 0.9, 1.0, 1)), ("SET_entry", (0.45, 0.45, 0.45, 1)), ("SET_", (0.2, 0.2, 0.22, 1)),
        ("PROP_beacon", (1.0, 0.6, 0.15, 1)), ("PROP_", (0.45, 0.42, 0.4, 1)), ("GUARD_eye", (1.0, 0.6, 0.15, 1)),
        ("GUARD_plinth", (0.25, 0.24, 0.23, 1)), ("GUARD_", (0.55, 0.53, 0.5, 1)), ("EXP_", (0.95, 0.9, 0.75, 1)))
for o in bpy.data.objects:
    for pre, col in COLS:
        if o.name.startswith(pre):
            o.color = col
            break
scene.render.resolution_x = scene.render.resolution_y = 1080
scene.render.use_stamp = False
cam = bpy.data.objects["MAPCAM_top"]
cam.data.ortho_scale = 66.0
for m in scene.timeline_markers:
    m.camera = cam
scene.camera = cam
for f in frames:
    scene.frame_set(f)
    scene.render.filepath = os.path.join(outdir, "map_f%03d.png" % f)
    bpy.ops.render.render(write_still=True)
    print("MAP", f)
