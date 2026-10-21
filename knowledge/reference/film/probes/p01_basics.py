# J015-T06 probe p01: version, defaults, enums, operator names, menu labels.
# Run: blender -b --factory-startup --python p01_basics.py
import bpy, inspect
def out(k, v): print("PROBE p01", k, "=", v)
sc = bpy.context.scene
out("version", bpy.app.version_string)
out("fps_default", sc.render.fps)
out("fps_base_default", sc.render.fps_base)
out("fps_prop_range", (bpy.types.RenderSettings.bl_rna.properties["fps"].hard_min, bpy.types.RenderSettings.bl_rna.properties["fps"].hard_max))
out("fps_base_prop_range", (bpy.types.RenderSettings.bl_rna.properties["fps_base"].hard_min, bpy.types.RenderSettings.bl_rna.properties["fps_base"].hard_max))
cam = bpy.data.cameras.new("c")
out("sensor_fit_items", [i.identifier for i in bpy.types.Camera.bl_rna.properties["sensor_fit"].enum_items])
out("sensor_fit_default", cam.sensor_fit)
out("sensor_width_default", cam.sensor_width)
out("sensor_height_default", cam.sensor_height)
out("lens_default", cam.lens)
out("camera_type_items", [i.identifier for i in bpy.types.Camera.bl_rna.properties["type"].enum_items])
out("TimelineMarker_has_camera", "camera" in bpy.types.TimelineMarker.bl_rna.properties.keys())
out("TimelineMarker_frame_type", bpy.types.TimelineMarker.bl_rna.properties["frame"].type)
out("render.opengl_exists", hasattr(bpy.ops.render, "opengl"))
out("render.opengl_label", bpy.ops.render.opengl.get_rna_type().name)
out("render.opengl_props", [p.identifier for p in bpy.ops.render.opengl.get_rna_type().properties if p.identifier != "rna_type"])
out("FCurve_auto_smoothing_items", [i.identifier for i in bpy.types.FCurve.bl_rna.properties["auto_smoothing"].enum_items])
out("Keyframe_handle_types", [i.identifier for i in bpy.types.Keyframe.bl_rna.properties["handle_left_type"].enum_items])
p = bpy.context.preferences.edit
out("new_key_handle_type_default", p.keyframe_new_handle_type)
out("new_key_interp_default", p.keyframe_new_interpolation_type)
# menu labels: scan the View menu of the 3D viewport by drawing into a fake layout is hard in background; read source
import os
src = os.path.join(os.path.dirname(bpy.__file__), "..", "..", "..")  # fallback below
path = os.path.join(bpy.utils.system_resource('SCRIPTS'), "startup", "bl_ui", "space_view3d.py")
txt = open(path, encoding="utf8").read()
for needle in ("Render Viewport Preview", "Render Playblast", "Render Playblast on Keyframes", "Viewport Render Animation", "Viewport Render Image"):
    out("space_view3d.py_contains[%s]" % needle, needle in txt)
out("space_view3d_path", path)
