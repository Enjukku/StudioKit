# J015-T06 probe p05: Track To (axes, validity, roll near the pole) vs Damped Track.
# Run: blender -b --factory-startup --python p05_track_to.py
import bpy, math
from mathutils import Vector
def out(k, v): print("PROBE p05", k, "=", v)
D = math.degrees
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
tgt = bpy.data.objects.new("T", None); sc.collection.objects.link(tgt)
cd = bpy.data.cameras.new("c"); cam = bpy.data.objects.new("c", cd); sc.collection.objects.link(cam)
vl = bpy.context.view_layer
# constraint defaults
c = cam.constraints.new('TRACK_TO')
out("TrackTo defaults via constraints.new (track_axis, up_axis)", (c.track_axis, c.up_axis))
out("TrackTo track_axis items", [i.identifier for i in c.bl_rna.properties["track_axis"].enum_items])
out("TrackTo up_axis items", [i.identifier for i in c.bl_rna.properties["up_axis"].enum_items])
out("TrackTo use_target_z default", c.use_target_z)
c.target = tgt
# same axis for track and up
c.track_axis, c.up_axis = 'TRACK_Y', 'UP_Y'
vl.update()
out("TrackTo track=Y up=Y -> is_valid / active", (c.is_valid, getattr(c, "active", None)))
c.track_axis, c.up_axis = 'TRACK_NEGATIVE_Y', 'UP_Y'
vl.update(); out("TrackTo track=-Y up=Y -> is_valid", c.is_valid)
c.track_axis, c.up_axis = 'TRACK_NEGATIVE_Z', 'UP_Y'
vl.update(); out("TrackTo track=-Z up=Y (camera setup) -> is_valid", c.is_valid)
# Damped Track
d = cam.constraints.new('DAMPED_TRACK')
out("DampedTrack track_axis items", [i.identifier for i in d.bl_rna.properties["track_axis"].enum_items])
out("DampedTrack has up_axis", "up_axis" in d.bl_rna.properties.keys())
cam.constraints.remove(d)

def spin(kind, radius, height=10.0, steps=36):
    for k in list(cam.constraints): cam.constraints.remove(k)
    if kind == "TRACK_TO":
        k = cam.constraints.new('TRACK_TO'); k.track_axis, k.up_axis = 'TRACK_NEGATIVE_Z', 'UP_Y'
    else:
        k = cam.constraints.new('DAMPED_TRACK'); k.track_axis = 'TRACK_NEGATIVE_Z'
    k.target = tgt
    cam.rotation_euler = (0, 0, 0)
    quats, aims = [], []
    for i in range(steps + 1):
        th = 2 * math.pi * i / steps
        cam.location = (radius * math.cos(th), radius * math.sin(th), height)
        vl.update()
        m = cam.matrix_world.to_3x3()
        quats.append(m.to_quaternion()); aims.append(m @ Vector((0, 0, -1)))
    def qang(a, b):
        d = abs(a.dot(b)); return D(2 * math.acos(min(1.0, d)))
    orient = [qang(quats[i], quats[i + 1]) for i in range(steps)]
    aim = [D(aims[i].angle(aims[i + 1])) for i in range(steps)]
    return max(orient), max(aim)
for kind in ("TRACK_TO", "DAMPED_TRACK"):
    for radius in (0.01, 0.5, 3.0, 10.0):
        mo, ma = spin(kind, radius)
        out("orbit[%s r=%g h=10, 10deg orbit step] max camera-rotation change / max aim-direction change (deg)" % (kind, radius), "%.4f / %.4f" % (mo, ma))
# exact pole
for kind in ("TRACK_TO", "DAMPED_TRACK"):
    for k in list(cam.constraints): cam.constraints.remove(k)
    if kind == "TRACK_TO":
        k = cam.constraints.new('TRACK_TO'); k.track_axis, k.up_axis = 'TRACK_NEGATIVE_Z', 'UP_Y'
    else:
        k = cam.constraints.new('DAMPED_TRACK'); k.track_axis = 'TRACK_NEGATIVE_Z'
    k.target = tgt; cam.rotation_euler = (0, 0, 0); cam.location = (0, 0, 10); vl.update()
    m = cam.matrix_world.to_3x3()
    out("exact pole camera above target [%s] aim, local Y in world" % kind, ("aim=%s" % str(tuple(round(v, 3) for v in (m @ Vector((0, 0, -1))))), "Y=%s" % str(tuple(round(v, 3) for v in (m @ Vector((0, 1, 0)))))))
