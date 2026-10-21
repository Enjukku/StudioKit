# J015-T06 probe p04: sensor fit, FOV formula, camera.angle_x/angle_y, projection matrix and real rendered pixels.
# 50 mm lens, 36 x 24 mm sensor, 1920x1080 and 1080x1920, fit HORIZONTAL / VERTICAL / AUTO.
# Run: blender -b --factory-startup --python p04_sensor_fit.py
import bpy, os, shutil, math
def out(k, v): print("PROBE p04", k, "=", v)
D = math.degrees
def fov(S, f): return 2 * math.atan(S / (2 * f))
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
cd = bpy.data.cameras.new("c"); cam = bpy.data.objects.new("c", cd); sc.collection.objects.link(cam)
cam.location = (0, -10, 0); cam.rotation_euler = (math.pi / 2, 0, 0)   # looks +Y, plane at distance 10
cd.lens = 50.0; cd.sensor_width = 36.0; cd.sensor_height = 24.0
sc.camera = cam
bpy.ops.mesh.primitive_plane_add(size=2.0, location=(0, 0, 0), rotation=(math.pi / 2, 0, 0))   # 2x2 m plane facing the camera
plane = bpy.context.active_object; plane.color = (1, 1, 1, 1)
sc.render.engine = 'BLENDER_WORKBENCH'
sc.display.shading.light = 'FLAT'; sc.display.shading.color_type = 'OBJECT'
sc.view_settings.view_transform = 'Standard'
sc.world = bpy.data.worlds.new("w"); sc.world.color = (0, 0, 0)
sc.render.image_settings.file_format = 'PNG'
here = os.path.dirname(os.path.abspath(__file__))
tmp = os.path.join(here, "_out_p04"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
dg = bpy.context.evaluated_depsgraph_get()
d = 10.0
def run_len(vals):
    idx = [i for i, v in enumerate(vals) if v > 0.5]
    return (idx[-1] - idx[0] + 1) if idx else 0
for (W, H) in ((1920, 1080), (1080, 1920)):
    for fit in ("HORIZONTAL", "VERTICAL", "AUTO"):
        cd.sensor_fit = fit
        sc.render.resolution_x, sc.render.resolution_y = W, H
        sc.render.resolution_percentage = 100
        dg = bpy.context.evaluated_depsgraph_get(); dg.update()
        a = W / H
        # formula: which sensor value governs? Blender: HORIZONTAL -> sensor_width governs width; VERTICAL -> sensor_height governs height;
        # AUTO -> sensor_width governs the larger side.  (hypothesis, tested below by projection matrix and pixels)
        if fit == "HORIZONTAL": Hf = fov(36, 50); Vf = 2 * math.atan(math.tan(Hf / 2) / a)
        elif fit == "VERTICAL": Vf = fov(24, 50); Hf = 2 * math.atan(math.tan(Vf / 2) * a)
        else:
            if W >= H: Hf = fov(36, 50); Vf = 2 * math.atan(math.tan(Hf / 2) / a)
            else: Vf = fov(36, 50); Hf = 2 * math.atan(math.tan(Vf / 2) * a)
        # projection matrix angles (what the renderer uses)
        P = cam.calc_matrix_camera(dg, x=W, y=H)
        Hp = 2 * math.atan(1 / P[0][0]); Vp = 2 * math.atan(1 / P[1][1])
        # real render, small size, same aspect
        w, h = (960, 540) if W > H else (540, 960)
        sc.render.resolution_x, sc.render.resolution_y = w, h
        sc.render.filepath = os.path.join(tmp, "r_%s_%dx%d.png" % (fit, W, H))
        bpy.ops.render.render(write_still=True)
        img = bpy.data.images.load(sc.render.filepath)
        px = img.pixels[:]
        row = [px[((h // 2) * w + x) * 4] for x in range(w)]
        col = [px[(y * w + w // 2) * 4] for y in range(h)]
        rx, ry = run_len(row), run_len(col)
        # plane is 2 m x 2 m at d=10: measured angle = 2*atan((run/size) * tan(FOV/2)) ... invert: visible half-width = 1.0 / (rx / w)
        Hr = 2 * math.atan((1.0 / (rx / w)) / d) if rx else float("nan")
        Vr = 2 * math.atan((1.0 / (ry / h)) / d) if ry else float("nan")
        out("case[%s %dx%d]" % (fit, W, H),
            "angle_x=%.4f angle_y=%.4f cam.angle=%.4f | formula H=%.4f V=%.4f | projmatrix H=%.4f V=%.4f | pixel-measured H=%.2f V=%.2f (run %dx%d of %dx%d px)" %
            (D(cd.angle_x), D(cd.angle_y), D(cd.angle), D(Hf), D(Vf), D(Hp), D(Vp), D(Hr), D(Vr), rx, ry, w, h))
        sc.render.resolution_x, sc.render.resolution_y = W, H
# Does sensor_height matter under HORIZONTAL/AUTO? Change it and re-read the projection matrix.
for fit in ("HORIZONTAL", "AUTO", "VERTICAL"):
    cd.sensor_fit = fit; res = []
    for sh in (24.0, 12.0):
        cd.sensor_height = sh
        sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
        dg = bpy.context.evaluated_depsgraph_get()
        P = cam.calc_matrix_camera(dg, x=1920, y=1080)
        res.append((sh, round(D(2 * math.atan(1 / P[1][1])), 4)))
    out("sensor_height_effect[%s] (sensor_height -> projmatrix V deg @1920x1080)" % fit, res)
cd.sensor_height = 24.0
# camera.angle setter/getter by fit
for fit in ("HORIZONTAL", "VERTICAL", "AUTO"):
    cd.sensor_fit = fit
    out("cam.angle[%s] deg (resolution-independent)" % fit, round(D(cd.angle), 4))
# Resolution-dependence of angle_x/angle_y
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080; cd.sensor_fit = 'AUTO'
a1 = (cd.angle_x, cd.angle_y)
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920
a2 = (cd.angle_x, cd.angle_y)
out("angle_x/angle_y identical at 1920x1080 and 1080x1920 (i.e. resolution-independent)?", a1 == a2)
# Pixel aspect effect (non-square pixels change a)
sc.render.pixel_aspect_x, sc.render.pixel_aspect_y = 2.0, 1.0
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080; cd.sensor_fit = 'HORIZONTAL'
dg = bpy.context.evaluated_depsgraph_get()
P = cam.calc_matrix_camera(dg, x=1920, y=1080, scale_x=2.0, scale_y=1.0)
out("pixel_aspect_2:1 HORIZONTAL projmatrix H,V deg (calc_matrix_camera with scale_x=2)", (round(D(2*math.atan(1/P[0][0])),4), round(D(2*math.atan(1/P[1][1])),4)))
shutil.rmtree(tmp, ignore_errors=True)
