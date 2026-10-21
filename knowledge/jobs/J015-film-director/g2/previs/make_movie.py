# Assemble the review movie: rendered frames + TEMP cue sounds at the shot-list frames, in a NEW .blend.
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# blender -b --factory-startup --python make_movie.py -- <frames_dir> <audio_dir> <out.mp4> <hold_frames> <out.blend> [silent]
import json
import os
import sys

import bpy

a = sys.argv[sys.argv.index("--") + 1:]
frames_dir, audio_dir, out_mp4, hold, out_blend = a[0], a[1], a[2], int(a[3]), a[4]
silent = len(a) > 5 and a[5] == "silent"
cues = json.load(open(os.path.join(audio_dir, "cues_temp.json")))
files = sorted(f for f in os.listdir(frames_dir) if f.endswith(".png"))
scene = bpy.context.scene
scene.render.fps, scene.render.fps_base = cues["fps"][0], float(cues["fps"][1])
scene.render.resolution_x, scene.render.resolution_y = 960, 540
scene.frame_start, scene.frame_end = 1, len(files) + hold
se = scene.sequence_editor_create()
img = se.strips.new_image("animatic", os.path.join(frames_dir, files[0]), 1, 1)
for f in files[1:]:
    img.elements.append(f)
if hold:
    last = se.strips.new_image("hold_last_frame", os.path.join(frames_dir, files[-1]), 2, len(files) + 1)
    last.frame_final_duration = hold
if not silent:
    ch = 3
    for cid, info in cues["files"].items():
        snd = se.strips.new_sound(cid, os.path.join(audio_dir, info["file"]), ch, info["frame"])
        ch += 1
r = scene.render
r.image_settings.media_type = "VIDEO"  # 5.1.2: before file_format (film-craft blender-previs §5)
r.image_settings.file_format = "FFMPEG"
r.ffmpeg.format = "MPEG4"
r.ffmpeg.codec = "H264"
r.ffmpeg.audio_codec = "NONE" if silent else "AAC"
r.ffmpeg.audio_channels = "MONO"
r.ffmpeg.audio_mixrate = 48000
r.use_sequencer = True
r.filepath = out_mp4
bpy.ops.wm.save_as_mainfile(filepath=out_blend)
bpy.ops.render.render(animation=True)
print("MOVIE", out_mp4, scene.frame_start, scene.frame_end, "silent" if silent else "with TEMP sound",
      bpy.app.version_string)
