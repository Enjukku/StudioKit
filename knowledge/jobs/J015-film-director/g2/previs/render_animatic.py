# Render the timed greybox animatic as a PNG sequence (burn-in: frame, shot marker, camera, lens).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# blender -b <file.blend> --python render_animatic.py -- <outdir> [first last] [camera_for_D]
# Headless = a Workbench/EEVEE render, not a viewport playblast (film-craft blender-previs §5). Never saves.
import os
import sys

import bpy

a = sys.argv[sys.argv.index("--") + 1:]
outdir = a[0]
scene = bpy.context.scene
if len(a) >= 3:
    scene.frame_start, scene.frame_end = int(a[1]), int(a[2])
if len(a) >= 4:  # alternative camera for shot D (this run only)
    for m in scene.timeline_markers:
        if m.name == "shot:D":
            m.camera = bpy.data.objects[a[3]]
    scene.render.stamp_note_text = scene.render.stamp_note_text + " - ALTERNATIVE D: " + a[3]
os.makedirs(outdir, exist_ok=True)
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = os.path.join(outdir, "f_")
scene.render.use_stamp = True
bpy.ops.render.render(animation=True)
print("ANIMATIC", outdir, scene.frame_start, scene.frame_end, bpy.app.version_string)
