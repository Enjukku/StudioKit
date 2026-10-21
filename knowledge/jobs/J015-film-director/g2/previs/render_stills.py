# Render named stills from the previs .blend without saving it.
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# blender -b <file.blend> --python render_stills.py -- <outdir> <res_x> <res_y> <stamp 0|1> <ghosts 0|1> <cam:frame:name> ...
# cam "PLAYCAM_beat1" moves the explorer to the entry causeway (beat 1 is play, before the sequence).
import os
import sys

import bpy
from mathutils import Vector

a = sys.argv[sys.argv.index("--") + 1:]
outdir, rx, ry, stamp, ghosts = a[0], int(a[1]), int(a[2]), a[3] == "1", a[4] == "1"
items = a[5:]
os.makedirs(outdir, exist_ok=True)
scene = bpy.context.scene
scene.render.resolution_x, scene.render.resolution_y = rx, ry
scene.render.use_stamp = stamp
scene.render.image_settings.file_format = "PNG"
if ghosts:
    for o in bpy.data.collections["CHECK_GHOSTS"].objects:
        o.hide_render = False
for it in items:
    cam, frame, name = it.split(":")
    scene.frame_set(int(frame))
    root = bpy.data.objects["EXP_root"]
    saved, action = root.location.copy(), root.animation_data.action
    if cam == "PLAYCAM_beat1":
        root.animation_data.action = None  # this run only; the file is never saved
        root.location = Vector((-15.0, -0.5, 0.3))
    for m in scene.timeline_markers:  # an unbound still: point every marker at the requested camera
        m.camera = bpy.data.objects[cam]
    scene.camera = bpy.data.objects[cam]
    scene.render.filepath = os.path.join(outdir, name + ".png")
    bpy.ops.render.render(write_still=True)
    root.animation_data.action = action
    root.location = saved
    print("STILL", name, cam, frame)
