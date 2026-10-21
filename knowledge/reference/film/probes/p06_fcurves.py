# J015-T06 probe p06: F-curve interpolation, Auto Clamped vs Auto handles (overshoot), Linear speed continuity, continuous-acceleration smoothing.
# Run: blender -b --factory-startup --python p06_fcurves.py
import bpy
from bpy_extras import anim_utils
def out(k, v): print("PROBE p06", k, "=", v)
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
def fresh():
    o = bpy.data.objects.new("o%d" % len(bpy.data.objects), None); sc.collection.objects.link(o); return o
def fcurve_of(o):
    a = o.animation_data.action
    slot = o.animation_data.action_slot
    cb = anim_utils.action_get_channelbag_for_slot(a, slot)
    return cb.fcurves[0]
def keyed(vals, frames=None):
    o = fresh(); frames = frames or [i * 10 for i in range(len(vals))]
    for f, v in zip(frames, vals):
        o.location.x = v; o.keyframe_insert("location", index=0, frame=f)
    return o, fcurve_of(o)
o, fc = keyed([0, 10, 0])
k = fc.keyframe_points[1]
out("new key defaults (interp, handle_left, handle_right)", (k.interpolation, k.handle_left_type, k.handle_right_type))
out("fcurve.auto_smoothing default", fc.auto_smoothing)
out("one F-curve = one channel (data_path, array_index, keys)", (fc.data_path, fc.array_index, len(fc.keyframe_points)))
def sample(fc, a, b, step=0.25):
    n = int((b - a) / step) + 1; return [fc.evaluate(a + i * step) for i in range(n)]
# overshoot: keys 0, 10, 10.0 plateau-ish and a sharp peak 0,10,0 and a step-like 0,0,10,10
for label, vals in (("peak 0,10,0", [0, 10, 0]), ("step 0,0,10,10", [0, 0, 10, 10])):
    for ht in ("AUTO_CLAMPED", "AUTO"):
        o, fc = keyed(vals)
        for kp in fc.keyframe_points: kp.handle_left_type = ht; kp.handle_right_type = ht
        fc.update()
        lo, hi = min(vals), max(vals)
        s = sample(fc, 0, (len(vals) - 1) * 10)
        out("overshoot[%s, %s] min/max of sampled curve (key range %g..%g)" % (label, ht, lo, hi), "%.4f / %.4f" % (min(s), max(s)))
# Linear: speed discontinuity at the middle key
o, fc = keyed([0, 10, 0])
for kp in fc.keyframe_points: kp.interpolation = 'LINEAR'
fc.update()
eps = 0.001
sp_l = (fc.evaluate(10) - fc.evaluate(10 - eps)) / eps; sp_r = (fc.evaluate(10 + eps) - fc.evaluate(10)) / eps
out("LINEAR speed just before / after middle key (units per frame)", "%.4f / %.4f" % (sp_l, sp_r))
# Auto clamped on a monotone run: speed continuous across the middle key?
o, fc = keyed([0, 10, 20, 40])
sp_l = (fc.evaluate(10) - fc.evaluate(10 - eps)) / eps; sp_r = (fc.evaluate(10 + eps) - fc.evaluate(10)) / eps
out("AUTO_CLAMPED monotone keys 0,10,20,40: speed before / after key at frame 10", "%.4f / %.4f" % (sp_l, sp_r))
# Auto-clamped at an extremum: speed at the peak
o, fc = keyed([0, 10, 0])
sp_l = (fc.evaluate(10) - fc.evaluate(10 - eps)) / eps; sp_r = (fc.evaluate(10 + eps) - fc.evaluate(10)) / eps
out("AUTO_CLAMPED peak key: speed before / after (flat handle => ~0)", "%.5f / %.5f" % (sp_l, sp_r))
# Continuous acceleration smoothing: change the LAST key, see how far the effect propagates
def curve_vals(mode, last):
    o, fc = keyed([0, 1, 3, 4, 7, 8, last], frames=[0, 10, 20, 30, 40, 50, 60])
    fc.auto_smoothing = mode; fc.update()
    return [fc.evaluate(f) for f in (5, 15, 25, 35, 45, 55)]
for mode in ("NONE", "CONT_ACCEL"):
    a = curve_vals(mode, 9); b = curve_vals(mode, 20)
    out("auto_smoothing=%s: |change| at frames 5,15,25,35,45,55 when last key 9->20 (monotone keys)" % mode, [round(abs(x - y), 4) for x, y in zip(a, b)])
