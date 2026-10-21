# J015-T06 probe p02: fps/fps_base effective rate, marker rules, camera-bound markers (frame_set + animation render), 31-sample count.
# Run: blender -b --factory-startup --python p02_rate_markers.py
import bpy, os, shutil, math
from fractions import Fraction
def out(k, v): print("PROBE p02", k, "=", v)
sc = bpy.context.scene
r = sc.render
# --- effective rate
def setrate(fps, base):
    r.fps = fps; r.fps_base = base
    return r.fps, r.fps_base, r.fps / r.fps_base
for label, fps, base in [("24", 24, 1.0), ("30", 30, 1.0), ("29.97 via 30/1.001", 30, 1.001), ("29.97 via 30000/1001", 30000, 1001.0), ("60", 60, 1.0), ("23.976 via 24000/1001", 24000, 1001.0)]:
    f, b, eff = setrate(fps, base)
    out("rate[%s]" % label, "fps=%r fps_base=%r effective=%.12f" % (f, b, eff))
exact = 30000/1001
out("exact_30000_over_1001", "%.12f" % exact)
r.fps = 30; r.fps_base = 1.001
out("fps_base_set_1.001_readback", repr(r.fps_base))
out("error_30_over_1.001_vs_exact", "%.3e" % (r.fps / r.fps_base - exact))
r.fps = 30000; r.fps_base = 1001.0
out("error_30000_over_1001_vs_exact", "%.3e" % (r.fps / r.fps_base - exact))
# fps is int-only:
try:
    r.fps = 29.97
    out("fps_assign_29.97", "accepted -> %r" % r.fps)
except Exception as e:
    out("fps_assign_29.97", "TypeError: %s" % str(e)[:80])
r.fps = 30; r.fps_base = 1.0
# --- markers
try:
    m = sc.timeline_markers.new("a", frame=10.5)
    out("marker_new_frame_10.5", "accepted -> frame=%r" % m.frame)
except Exception as e:
    out("marker_new_frame_10.5", "%s: %s" % (type(e).__name__, str(e)[:90]))
try:
    sc.timeline_markers.clear()
    m = sc.timeline_markers.new("b", frame=10)
    m.frame = 12.7
    out("marker_set_frame_12.7", "accepted -> frame=%r" % m.frame)
except Exception as e:
    out("marker_set_frame_12.7", "%s: %s" % (type(e).__name__, str(e)[:90]))
out("marker_frame_negative_ok", sc.timeline_markers.new("neg", frame=-5).frame)
sc.timeline_markers.clear()
# --- camera-bound markers
cams = []
for i, n in enumerate(("CamA", "CamB", "CamC")):
    cd = bpy.data.cameras.new(n); co = bpy.data.objects.new(n, cd); sc.collection.objects.link(co)
    co.location = (i * 10, -10, 0); cams.append(co)
sc.camera = cams[0]
for n, f, cam in (("A", 10, cams[0]), ("B", 20, cams[1]), ("C", 30, cams[2])):
    mk = sc.timeline_markers.new(n, frame=f); mk.camera = cam
out("marker_cameras", [(m.name, m.frame, m.camera.name) for m in sc.timeline_markers])
for f in (1, 9, 10, 11, 19, 20, 21, 29, 30, 31, 100):
    sc.frame_set(f)
    out("frame_set[%d].scene.camera" % f, sc.camera.name)
# subframe behaviour at 19.5 / 20.0 boundary
sc.frame_set(19, subframe=0.9); out("frame_set[19+0.9].scene.camera", sc.camera.name)
sc.frame_set(20, subframe=0.0); out("frame_set[20+0.0].scene.camera", sc.camera.name)
# --- during animation render: log active camera per rendered frame (frame_change_pre/post and render_pre)
log = []
def on_render_pre(scene, *a): log.append((scene.frame_current, scene.camera.name))
bpy.app.handlers.render_pre.append(on_render_pre)
here = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
tmp = os.path.join(here, "_out_p02"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
sc.render.engine = 'BLENDER_WORKBENCH'
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 32, 18, 100
sc.render.image_settings.file_format = 'PNG'
sc.render.filepath = os.path.join(tmp, "f_")
sc.frame_set(1)
sc.camera = cams[2]  # deliberately start from the wrong camera
sc.frame_start, sc.frame_end = 1, 31
bpy.ops.render.render(animation=True)
files = sorted(os.listdir(tmp))
out("render_animation_1_to_31_file_count", len(files))
out("render_animation_first_last_file", (files[0], files[-1]))
out("render_pre_camera_log(frame:cam) sample", [(f, c) for f, c in log if f in (1, 9, 10, 19, 20, 29, 30, 31)])
out("render_pre_distinct_camera_runs", [(c, min(f for f, cc in log if cc == c), max(f for f, cc in log if cc == c)) for c in dict.fromkeys(c for f, c in log)])
out("scene.camera_after_render", sc.camera.name)
# --- timing arithmetic for 31 samples
r.fps = 30; r.fps_base = 1.0
rate = Fraction(r.fps) / Fraction(r.fps_base).limit_denominator(1000000)
out("samples_frames_1_to_31", sc.frame_end - sc.frame_start + 1)
out("seconds_for_31_samples_at_30fps", "%s = %.12f" % (Fraction(31, 30), 31/30))
out("t(31)-t(1) elapsed positions", float((31-1)/rate))
shutil.rmtree(tmp, ignore_errors=True)
