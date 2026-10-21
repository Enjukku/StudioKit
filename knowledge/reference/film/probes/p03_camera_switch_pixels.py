# J015-T06 probe p03: do camera-bound markers change the camera that is actually rendered? (pixel test, 3 colored cubes)
# Also: camera before the first marker, render_pre vs render_post camera log, viewport-render operator poll in background.
# Run: blender -b --factory-startup --python p03_camera_switch_pixels.py
import bpy, os, shutil
def out(k, v): print("PROBE p03", k, "=", v)
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
cols = {"A": (1, 0, 0, 1), "B": (0, 1, 0, 1), "C": (0, 0, 1, 1)}
cams = {}
for i, (n, c) in enumerate(cols.items()):
    bpy.ops.mesh.primitive_cube_add(size=2, location=(i * 20, 0, 0))
    cube = bpy.context.active_object; cube.color = c
    cd = bpy.data.cameras.new("Cam" + n); co = bpy.data.objects.new("Cam" + n, cd); sc.collection.objects.link(co)
    co.location = (i * 20, -10, 0); co.rotation_euler = (1.5707963, 0, 0)  # looks +Y
    cams[n] = co
sc.render.engine = 'BLENDER_WORKBENCH'
sc.display.shading.light = 'FLAT'; sc.display.shading.color_type = 'OBJECT'
sc.view_settings.view_transform = 'Standard'
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 32, 18, 100
sc.render.image_settings.file_format = 'PNG'
sc.world = bpy.data.worlds.new("w"); sc.world.color = (0.5, 0.5, 0.5)
for n, f in (("A", 5), ("B", 10), ("C", 15)):
    sc.timeline_markers.new(n, frame=f).camera = cams[n]
# camera before the first marker
sc.camera = cams["C"]; sc.frame_set(1)
out("frame_set(1) with scene.camera=CamC and first marker at 5 ->", sc.camera.name)
# render and read centre pixel
here = os.path.dirname(os.path.abspath(__file__))
tmp = os.path.join(here, "_out_p03"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
sc.render.filepath = os.path.join(tmp, "f_")
sc.frame_start, sc.frame_end = 1, 16
post = []
bpy.app.handlers.render_post.append(lambda s, *a: post.append((s.frame_current, s.camera.name)))
pre = []
bpy.app.handlers.render_pre.append(lambda s, *a: pre.append((s.frame_current, s.camera.name)))
sc.camera = cams["C"]
bpy.ops.render.render(animation=True)
def name_of(px):
    r, g, b = px[0] > .5, px[1] > .5, px[2] > .5
    return {(1,0,0): "red=A", (0,1,0): "green=B", (0,0,1): "blue=C"}.get((r, g, b), "other%s" % (tuple(round(v,2) for v in px[:3]),))
res = []
for f in range(1, 17):
    img = bpy.data.images.load(os.path.join(tmp, "f_%04d.png" % f))
    w, h = img.size; i = ((h // 2) * w + w // 2) * 4
    res.append((f, name_of(img.pixels[i:i+4])))
out("rendered_centre_pixel(frame, colour)", res)
out("render_pre_camera", pre)
out("render_post_camera", post)
shutil.rmtree(tmp, ignore_errors=True)
# viewport-render operator in background
try:
    r = bpy.ops.render.opengl(animation=False)
    out("render.opengl in background", "returned %s" % r)
except Exception as e:
    out("render.opengl in background", "%s: %s" % (type(e).__name__, str(e).strip().splitlines()[0][:110]))
