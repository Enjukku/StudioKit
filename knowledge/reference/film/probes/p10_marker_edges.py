# J015-T06 probe p10: marker edge cases that the shotlist tool can hit (unbound markers, duplicate frames, name reuse, read-back).
# Run: blender -b --factory-startup --python p10_marker_edges.py
import bpy
def out(k, v): print("PROBE p10", k, "=", v)
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
def mk_cam(n):
    cd = bpy.data.cameras.new(n); co = bpy.data.objects.new(n, cd); sc.collection.objects.link(co); return co
A, B, C = mk_cam("CamA"), mk_cam("CamB"), mk_cam("CamC")
# 1. unbound marker between two bound ones
sc.timeline_markers.clear()
sc.timeline_markers.new("A", frame=10).camera = A
sc.timeline_markers.new("X_unbound", frame=15)
sc.timeline_markers.new("B", frame=20).camera = B
for f in (12, 15, 17, 20): sc.frame_set(f); out("unbound marker@15: frame %d camera" % f, sc.camera.name)
# 2. two bound markers on the same frame (creation order A then C, and reversed)
for order in ((A, C), (C, A)):
    sc.timeline_markers.clear()
    sc.timeline_markers.new("first", frame=10).camera = order[0]
    sc.timeline_markers.new("second", frame=10).camera = order[1]
    sc.frame_set(10); out("two bound markers on frame 10, created %s then %s -> camera" % (order[0].name, order[1].name), sc.camera.name)
# 3. duplicate marker names
sc.timeline_markers.clear()
m1 = sc.timeline_markers.new("S010", frame=1); m2 = sc.timeline_markers.new("S010", frame=50)
out("duplicate names allowed; count", (len(sc.timeline_markers), [m.name for m in sc.timeline_markers]))
# 4. read back order of timeline_markers (creation order, not frame order)
sc.timeline_markers.clear()
for n, f in (("late", 90), ("early", 5), ("mid", 40)): sc.timeline_markers.new(n, frame=f)
out("timeline_markers iteration order (creation order, unsorted)", [(m.name, m.frame) for m in sc.timeline_markers])
out("sorted by frame", [(m.name, m.frame) for m in sorted(sc.timeline_markers, key=lambda m: m.frame)])
# 5. marker.camera read back + clearing
mm = sc.timeline_markers.new("cam", frame=3); mm.camera = A
out("marker.camera readback", mm.camera.name); mm.camera = None; out("marker.camera after None", mm.camera)
# 6. marker removal and 'remove' API
sc.timeline_markers.remove(mm); out("markers after remove", len(sc.timeline_markers))
# 7. camera object removed while bound
sc.timeline_markers.clear()
mm = sc.timeline_markers.new("dead", frame=1); mm.camera = C
bpy.data.objects.remove(C)
out("marker.camera after the camera object is deleted", mm.camera)
# 8. marker in a scene with a frame range: marker outside range is still honoured by frame_set
sc.timeline_markers.clear(); sc.frame_start, sc.frame_end = 10, 20
sc.timeline_markers.new("out", frame=5).camera = B
sc.frame_set(12); out("marker before frame_start (5), frame_set(12) camera", sc.camera.name)
