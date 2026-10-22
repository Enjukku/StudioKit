"""Blender-layer tests for tools/rig/rig_audit.py caps, overlap and orient (J018 G3-P1).

Runs Blender headless on a scene built in the script; skipped when no Blender executable is found
(set BLENDER to its path, or install it in the default Windows folder).
"""

import json
import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

RIG = Path(__file__).resolve().parents[2] / "tools" / "rig"


def blender_exe():
    for c in (os.environ.get("BLENDER"), shutil.which("blender"),
              r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"):
        if c and Path(c).is_file():
            return c
    return None


SCENE = textwrap.dedent(r"""
    import bpy, bmesh, json, math, sys
    sys.path.insert(0, RIG)
    import rig_audit as ra
    from mathutils import Vector
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene

    def box(name, loc, size):
        me = bpy.data.meshes.new(name); bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(name, me); sc.collection.objects.link(ob)
        ob.location, ob.scale = loc, size
        bpy.context.view_layer.update()
        bpy.ops.object.select_all(action='DESELECT'); ob.select_set(True); bpy.context.view_layer.objects.active = ob
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        return ob

    def cam(name, loc, look):
        c = bpy.data.objects.new(name, bpy.data.cameras.new(name)); sc.collection.objects.link(c)
        c.location = loc
        c.rotation_euler = (Vector(look) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
        return c

    out = {}
    # an upper arm box between a shoulder cut (top, z = 2.8) and an elbow cut (bottom, z = 1.6): one group per cut
    arm = box("UpperArm", (0, 0, 2.2), (0.3, 0.3, 1.2))
    bpy.context.view_layer.update()
    out["mark_shoulder"] = ra.mark_plane_caps(arm, "P05", Vector((0, 0, 2.8)), Vector((0, 0, 1)))
    out["mark_elbow"] = ra.mark_plane_caps(arm, "P06", Vector((0, 0, 1.6)), Vector((0, 0, 1)))
    front = cam("Front", (0, -6, 2.2), (0, 0, 2.2))
    top = cam("Top", (0, 0, 8), (0, 0, 2.2))
    bpy.context.view_layer.update()
    out["front_shoulder"] = ra.cap_count(arm, front, "P05")
    out["top_shoulder"] = ra.cap_count(arm, top, "P05")
    try:
        ra.cap_count(arm, front, "P99"); out["missing"] = "no error"
    except KeyError:
        out["missing"] = "KeyError"
    # a torso under a smaller head: the socket is only the area the head covers
    torso = box("Torso", (2, 0, 1), (1.0, 0.6, 2.0))
    head = box("Head", (2, 0, 2.25), (0.4, 0.4, 0.5))
    bpy.context.view_layer.update()
    ra.mark_plane_caps(head, "P02", Vector((2, 0, 2.0)), Vector((0, 0, 1)))
    out["socket_whole_face"] = ra.mark_plane_caps(torso, "P02x", Vector((2, 0, 2.0)), Vector((0, 0, 1)))
    out["socket_child"] = ra.mark_plane_caps(torso, "P02", Vector((2, 0, 2.0)), Vector((0, 0, 1)), child=head)
    # overlap: a hand box pulled into the head reads pairs; apart reads 0
    hand = box("Hand", (5, 0, 0), (0.2, 0.2, 0.2))
    bpy.context.view_layer.update()
    out["overlap_apart"] = ra.overlap_pairs(hand, head)
    hand.location = (2, 0, 2.5); bpy.context.view_layer.update()  # crosses the head's top face
    out["overlap_in"] = ra.overlap_pairs(hand, head)
    hand.location = (2, 0, 2.25); bpy.context.view_layer.update()  # wholly inside: no surface crosses
    out["overlap_inside"] = ra.overlap_pairs(hand, head)
    print("RESULT" + json.dumps(out))
""")


@unittest.skipUnless(blender_exe(), "no Blender executable (set BLENDER)")
class RigAuditBlenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as d:
            script = Path(d) / "scene.py"
            script.write_text(f"RIG = {str(RIG)!r}\n" + SCENE, encoding="utf-8")
            p = subprocess.run([blender_exe(), "-b", "--factory-startup", "--python", str(script)],
                               capture_output=True, text=True, timeout=300)
        line = next((ln for ln in p.stdout.splitlines() if ln.startswith("RESULT")), None)
        if line is None:
            raise AssertionError(f"Blender run failed:\n{p.stdout[-2000:]}\n{p.stderr[-2000:]}")
        cls.r = json.loads(line[len("RESULT"):])

    def test_one_group_per_cut(self):
        self.assertEqual((self.r["mark_shoulder"], self.r["mark_elbow"]), (1, 1))

    def test_cap_hidden_from_the_side_seen_from_above(self):
        self.assertEqual(self.r["front_shoulder"][0], 0)   # side faces are not sampled as cap
        self.assertGreater(self.r["front_shoulder"][1], 0)
        self.assertGreater(self.r["top_shoulder"][0], 0)   # the open shoulder cap shows from above

    def test_missing_group_stops(self):
        self.assertEqual(self.r["missing"], "KeyError")

    def test_socket_is_only_the_covered_area(self):
        self.assertEqual(self.r["socket_whole_face"], 1)   # without child=: the whole torso top
        self.assertEqual(self.r["socket_child"], 0)        # with child=: a closed face has no covered-only face

    def test_overlap(self):
        self.assertEqual(self.r["overlap_apart"], 0)
        self.assertGreater(self.r["overlap_in"], 0)
        self.assertEqual(self.r["overlap_inside"], 0)      # known false reading: a part wholly inside reads 0



FRAMES = textwrap.dedent(r"""
    import bpy, json, sys
    sys.path.insert(0, MODEL)
    import review_renders as rr
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0))
    cam = bpy.data.objects.new("GameCam", bpy.data.cameras.new("GameCam")); sc.collection.objects.link(cam)
    cam.location = (0, -6, 0); cam.rotation_euler = (1.5708, 0, 0)
    before = (sc.display.shading.light, sc.render.engine, sc.camera)
    rep = rr.render_frames("GameCam", [1, 3], OUT, (200, 120))
    after = (sc.display.shading.light, sc.render.engine, sc.camera)
    print("RESULT" + json.dumps({"files": [f["file"] for f in rep["files"]], "restored": before == after}))
""")


@unittest.skipUnless(blender_exe(), "no Blender executable (set BLENDER)")
class RenderFramesBlenderTest(unittest.TestCase):
    def test_shaded_and_blackfill_and_settings_restored(self):
        import sys
        sys.path.insert(0, str(RIG.parents[0] / "art"))
        import look_check as lc
        from PIL import Image
        with tempfile.TemporaryDirectory() as d:
            script = Path(d) / "frames.py"
            script.write_text(f"MODEL = {str(RIG.parent / 'model')!r}\nOUT = {d!r}\n" + FRAMES, encoding="utf-8")
            p = subprocess.run([blender_exe(), "-b", "--factory-startup", "--python", str(script)],
                               capture_output=True, text=True, timeout=300)
            line = next((ln for ln in p.stdout.splitlines() if ln.startswith("RESULT")), None)
            self.assertIsNotNone(line, p.stdout[-1500:] + p.stderr[-1500:])
            r = json.loads(line[len("RESULT"):])
            self.assertEqual(len(r["files"]), 4)
            self.assertTrue(r["restored"])
            mask, src, _ = lc.subject_mask(Image.open(Path(d) / "frame_0001.blackfill.png").convert("RGB"))
            self.assertEqual(src, "key-auto")          # the magenta backdrop keys automatically
            self.assertTrue(mask.any())




AUDIT = textwrap.dedent(r"""
    import bpy, json, sys
    sys.path.insert(0, MODEL)
    sys.path.insert(0, RIGDIR)
    import model_audit as ma
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y = 1600, 720
    bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 0))   # 2 studs tall, 24 square studs of surface
    cube = bpy.context.active_object
    cam = bpy.data.objects.new("GameCam", bpy.data.cameras.new("GameCam")); sc.collection.objects.link(cam)
    cam.location = (0, -10, 0); cam.rotation_euler = (1.5708, 0, 0)
    cam.data.sensor_fit = "VERTICAL"
    bpy.context.view_layer.update()
    ps = ma.projected_size(["Cube"], "GameCam", 360, (1600, 720))
    td = ma.mesh_texel_density(cube, 1024, 1024)
    print("RESULT" + json.dumps({"projected": ps, "texel": td}))
""")


@unittest.skipUnless(blender_exe(), "no Blender executable (set BLENDER)")
class ModelAuditBlenderTest(unittest.TestCase):
    def test_projected_size_and_texel_density(self):
        with tempfile.TemporaryDirectory() as d:
            script = Path(d) / "audit.py"
            script.write_text(f"MODEL = {str(RIG.parent / 'model')!r}\nRIGDIR = {str(RIG)!r}\n" + AUDIT, encoding="utf-8")
            p = subprocess.run([blender_exe(), "-b", "--factory-startup", "--python", str(script)],
                               capture_output=True, text=True, timeout=300)
            line = next((ln for ln in p.stdout.splitlines() if ln.startswith("RESULT")), None)
            self.assertIsNotNone(line, p.stdout[-1500:] + p.stderr[-1500:])
            r = json.loads(line[len("RESULT"):])
            row = r["projected"][0]
            self.assertTrue(row["in_front"])
            self.assertGreater(row["height_px_on_phone"], 20)
            self.assertLess(row["box_px"]["y0"], row["box_px"]["y1"])
            self.assertAlmostEqual(r["texel"]["world_area"], 24.0, places=3)
            self.assertIsNotNone(r["texel"]["px_per_stud"])


if __name__ == "__main__":
    unittest.main()
