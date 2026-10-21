# J015-T06 probe p09: movie-strip frame-rate options, image sequence + movie output, encoded rate readback.
# Run: blender -b --factory-startup --python p09_movie.py
import bpy, os, shutil
def out(k, v): print("PROBE p09", k, "=", v)
sc = bpy.context.scene
op = bpy.ops.sequencer.movie_strip_add.get_rna_type()
for p in op.properties:
    if "frame" in p.identifier.lower() or "rate" in p.identifier.lower() or "fps" in p.identifier.lower():
        out("movie_strip_add prop", "%s | name=%r | desc=%r | default=%r" % (p.identifier, p.name, p.description, getattr(p, "default", None)))
out("movie_strip_add label", op.name)
ims = sc.render.image_settings
out("image_settings.media_type items", [i.identifier for i in ims.bl_rna.properties["media_type"].enum_items] if "media_type" in ims.bl_rna.properties.keys() else "no media_type property")
out("file_format items (media_type=%s)" % getattr(ims, "media_type", "-"), [i.identifier for i in ims.bl_rna.properties["file_format"].enum_items])
try:
    ims.file_format = 'FFMPEG'; out("set file_format='FFMPEG' directly", "accepted")
except Exception as e:
    out("set file_format='FFMPEG' directly", "TypeError: " + str(e)[:70])
if "media_type" in ims.bl_rna.properties.keys():
    ims.media_type = 'VIDEO'
    out("file_format items (media_type=VIDEO)", [i.identifier for i in ims.bl_rna.properties["file_format"].enum_items])
# render a short movie at 30000/1001 and read the encoded rate back through a movie clip
here = os.path.dirname(os.path.abspath(__file__))
tmp = os.path.join(here, "_out_p09"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
sc.render.engine = 'BLENDER_WORKBENCH'
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 64, 36, 100
sc.render.fps, sc.render.fps_base = 30000, 1001.0
sc.frame_start, sc.frame_end = 1, 31
ims.media_type = 'VIDEO'; ims.file_format = 'FFMPEG'
sc.render.ffmpeg.format = 'MPEG4'; sc.render.ffmpeg.codec = 'H264'
sc.render.filepath = os.path.join(tmp, "m_")
cd = bpy.data.cameras.new("c"); co = bpy.data.objects.new("c", cd); sc.collection.objects.link(co); co.location = (0, -5, 0); co.rotation_euler = (1.5707963, 0, 0); sc.camera = co
try:
    bpy.ops.render.render(animation=True)
    files = os.listdir(tmp); out("movie_files", files)
    clip = bpy.data.movieclips.load(os.path.join(tmp, files[0]))
    out("movieclip fps / frame_duration / size", (clip.fps, clip.frame_duration, tuple(clip.size)))
    # sequencer strip
    sc.sequence_editor_create()
    st = sc.sequence_editor.strips.new_movie("s", os.path.join(tmp, files[0]), channel=1, frame_start=1)
    out("strip.fps / frame_final_duration", (st.fps, st.frame_final_duration))
except Exception as e:
    out("movie render", "%s: %s" % (type(e).__name__, str(e)[:160]))
for c in list(bpy.data.movieclips): bpy.data.movieclips.remove(c)
if sc.sequence_editor: sc.sequence_editor_clear()
shutil.rmtree(tmp, ignore_errors=True)
