# J015-T06 probe p07: reading evaluated camera matrices (parent + Track To + animated lens) through the depsgraph.
# Run: blender -b --factory-startup --python p07_depsgraph.py
import bpy, math
from mathutils import Vector
def out(k, v): print("PROBE p07", k, "=", v)
def r(v): return tuple(round(x, 4) for x in v)
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
rig = bpy.data.objects.new("Rig", None); sc.collection.objects.link(rig)
tgt = bpy.data.objects.new("Tgt", None); sc.collection.objects.link(tgt); tgt.location = (0, 20, 0)
cd = bpy.data.cameras.new("c"); cam = bpy.data.objects.new("c", cd); sc.collection.objects.link(cam)
cam.parent = rig; cam.location = (0, 0, 2)
con = cam.constraints.new('TRACK_TO'); con.target = tgt; con.track_axis = 'TRACK_NEGATIVE_Z'; con.up_axis = 'UP_Y'
sc.camera = cam
rig.location.x = 0; rig.keyframe_insert("location", index=0, frame=1)
rig.location.x = 10; rig.keyframe_insert("location", index=0, frame=11)
cd.lens = 35; cd.keyframe_insert("lens", frame=1)
cd.lens = 85; cd.keyframe_insert("lens", frame=11)
sc.frame_set(1)
for f in (1, 6, 11):
    sc.frame_set(f)
    dg = bpy.context.evaluated_depsgraph_get()
    ce = cam.evaluated_get(dg)
    m = ce.matrix_world
    out("frame %d" % f, "raw cam.location=%s (local, unchanged) | evaluated world pos=%s | evaluated aim(-Z)=%s | raw rotation_euler=%s | eval lens=%.3f | orig lens=%.3f | orig matrix_world pos=%s" %
        (r(cam.location), r(m.translation), r(m.to_3x3() @ Vector((0, 0, -1))), r(cam.rotation_euler), ce.data.lens, cd.lens, r(cam.matrix_world.translation)))
# stale original matrix_world after a property change without update
cam.location = (0, 0, 50)
out("after cam.location=(0,0,50), no update: original matrix_world z / evaluated z", (round(cam.matrix_world.translation.z, 3), round(cam.evaluated_get(bpy.context.evaluated_depsgraph_get()).matrix_world.translation.z, 3)))
bpy.context.view_layer.update()
out("after view_layer.update(): original matrix_world z / evaluated z", (round(cam.matrix_world.translation.z, 3), round(cam.evaluated_get(bpy.context.evaluated_depsgraph_get()).matrix_world.translation.z, 3)))
# projection matrix from evaluated
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
P = cam.calc_matrix_camera(bpy.context.evaluated_depsgraph_get(), x=1920, y=1080)
out("calc_matrix_camera H deg (lens 85 at frame 11, 36mm AUTO)", round(math.degrees(2 * math.atan(1 / P[0][0])), 4))
out("formula 2*atan(36/(2*85)) deg", round(math.degrees(2 * math.atan(36 / 170)), 4))
