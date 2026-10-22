"""Offline tests for tools/model/model_audit.py pure checks (no Blender needed)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "model"))
import model_audit as ma  # noqa: E402

CUBE_FACES = [[0, 1, 2, 3], [4, 7, 6, 5], [0, 4, 5, 1], [1, 5, 6, 2], [2, 6, 7, 3], [3, 7, 4, 0]]


def cube(name, x0=0.0, y0=0.0, z0=0.0, s=1.0, faces=None, **extra):
    """Axis-aligned cube, outward winding (the bottom face [0,1,2,3] winds clockwise seen from outside)."""
    base = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
    verts = [(x0 + x * s, y0 + y * s, z0 + z * s) for x, y, z in base]
    return {"name": name, "verts": verts, "polygons": faces or [list(f) for f in CUBE_FACES], "uv_sets": 1,
            "uvs": [(0.5, 0.5)] * 24, "materials": 1, "images": [], **extra}


def run(*meshes, **kw):
    return ma.audit_model(list(meshes), **kw)


class CubeTest(unittest.TestCase):
    def test_cube_passes(self):
        r = run(cube("Box"))
        self.assertEqual(r["meshes"][0]["triangles"], 12)
        self.assertEqual(r["meshes"][0]["verdict"], "PASS")
        self.assertEqual(r["checks"]["orientation"]["inverted_parts"], 0)
        for k in ("mesh_limits", "floating", "hidden", "orientation", "export"):
            self.assertEqual(r["checks"][k]["verdict"], "PASS", k)
        self.assertEqual(r["verdict"], "MEASURED")  # no budget, size or expect given

    def test_cube_with_all_numbers_passes(self):
        r = run(cube("Box"), budget=12, size=[1, 1, 1], size_tol=0.01, expect=["Box"])
        self.assertEqual(r["verdict"], "PASS")

    def test_cube_positive_volume(self):
        p = ma.build_parts([cube("Box")])[0]
        self.assertTrue(p["closed"])
        self.assertAlmostEqual(p["volume"], 1.0)

    def test_hole_reports_open_edges(self):
        r = run(cube("Box", faces=[list(f) for f in CUBE_FACES[:-1]]))
        row = r["meshes"][0]
        self.assertEqual(row["boundary_edges"], 4)
        self.assertEqual(row["verdict"], "FAIL")
        self.assertEqual(r["verdict"], "FAIL")


class FloatingTest(unittest.TestCase):
    def test_touching_cubes_not_floating(self):
        r = run(cube("A"), cube("B", x0=1.0))
        self.assertEqual(r["checks"]["floating"]["count"], 0)
        self.assertEqual(r["checks"]["floating"]["verdict"], "PASS")

    def test_stacked_cube_touches_without_ground(self):
        r = run(cube("A"), cube("B", z0=1.0), ground=None)
        self.assertEqual(r["checks"]["floating"]["count"], 0)

    def test_cube_one_stud_above_everything_floats(self):
        r = run(cube("A"), cube("B", x0=1.0), cube("C", x0=0.5, z0=2.0))
        f = r["checks"]["floating"]
        self.assertEqual(f["count"], 1)
        self.assertEqual(f["listed"][0]["part"], "C#0")
        self.assertAlmostEqual(f["listed"][0]["nearest_box_gap"], 1.0)
        self.assertEqual(f["verdict"], "FAIL")

    def test_gap_inside_contact_tolerance_touches(self):
        r = run(cube("A"), cube("B", x0=1.005))
        self.assertEqual(r["checks"]["floating"]["count"], 0)
        r = run(cube("A"), cube("B", x0=1.005, z0=0.5), contact_tol=0.001)
        self.assertEqual(r["checks"]["floating"]["count"], 1)

    def test_edge_to_edge_contact(self):
        # B is rotated 90 degrees; its bottom edge crosses A's top edge with no vertex on a face
        a = ma.make_part("A", 0, [(0, 0, 0), (1, 0, 1), (0, 0, 1)], [[0, 1, 2]], [0])
        b = ma.make_part("B", 0, [(0.5, -1, 1), (0.5, 1, 1), (0.5, 0, 2)], [[0, 1, 2]], [0])
        self.assertAlmostEqual(ma.segment_distance((0, 0, 1), (1, 0, 1), (0.5, -1, 1), (0.5, 1, 1)), 0.0)
        self.assertTrue(ma.touching(a, b))
        far = ma.make_part("F", 0, [(0.5, -1, 1.5), (0.5, 1, 1.5), (0.5, 0, 2)], [[0, 1, 2]], [0])
        self.assertFalse(ma.touching(a, far))

    def test_interpenetrating_triangles_touch(self):
        a = ma.make_part("A", 0, [(-1, 0, -1), (1, 0, -1), (0, 0, 1)], [[0, 1, 2]], [0])
        b = ma.make_part("B", 0, [(0, -1, 0), (0, 1, 0), (0, 0, 5)], [[0, 1, 2]], [0])
        self.assertTrue(ma.touching(a, b))

    def test_two_islands_in_one_object_counted_as_parts(self):
        two = cube("Two")
        two["verts"] = two["verts"] + [(x + 3, y, z) for x, y, z in two["verts"]]
        two["polygons"] = two["polygons"] + [[i + 8 for i in f] for f in CUBE_FACES]
        r = run(two)
        self.assertEqual(r["meshes"][0]["connected_parts"], 2)
        self.assertEqual(r["data"]["surface_parts"], 2)
        self.assertEqual(r["checks"]["floating"]["count"], 0)  # both on the ground
        self.assertEqual(r["checks"]["floating"]["contact_groups"], 1)


class HiddenTest(unittest.TestCase):
    def test_small_cube_inside_big_cube_is_hidden(self):
        r = run(cube("Big", s=4.0), cube("Small", 1.5, 1.5, 1.5))
        h = r["checks"]["hidden"]
        self.assertEqual(h["count"], 1)
        self.assertEqual(h["listed"][0], {"part": "Small#0", "inside": "Big#0"})
        self.assertEqual(h["verdict"], "FAIL")
        self.assertEqual(r["checks"]["floating"]["count"], 0)  # hidden, not also floating

    def test_cube_poking_out_is_not_hidden(self):
        r = run(cube("Big", s=4.0), cube("Small", 3.5, 1.5, 1.5))
        self.assertEqual(r["checks"]["hidden"]["count"], 0)


class OrientationTest(unittest.TestCase):
    def test_reversed_winding_has_negative_volume(self):
        r = run(cube("Inv", faces=[list(reversed(f)) for f in CUBE_FACES]))
        o = r["checks"]["orientation"]
        self.assertEqual(o["inverted_parts"], 1)
        self.assertLess(o["inverted"][0]["volume"], 0)
        self.assertEqual(o["verdict"], "FAIL")

    def test_mirrored_object_uses_its_own_winding(self):
        flipped = [list(reversed(f)) for f in CUBE_FACES]
        r = run(cube("Mir", faces=flipped, mirrored=True))
        self.assertEqual(r["checks"]["orientation"]["inverted_parts"], 0)
        self.assertEqual(r["checks"]["orientation"]["mirrored_objects"], ["Mir"])

    def test_one_flipped_face_is_a_winding_conflict(self):
        faces = [list(f) for f in CUBE_FACES]
        faces[0] = list(reversed(faces[0]))
        o = run(cube("Box", faces=faces))["checks"]["orientation"]
        self.assertEqual(o["winding_conflict_edges"], 4)
        self.assertEqual(o["verdict"], "FAIL")


class LimitTest(unittest.TestCase):
    def test_triangles_over_per_mesh_limit_fail(self):
        m = {"name": "Big", "verts": [(0, 0, 0), (1, 0, 0), (0, 1, 0)], "polygons": [[0, 1, 2]] * 20_001,
             "uv_sets": 1, "uvs": [], "materials": 1, "images": []}
        row = ma.mesh_row(m)
        self.assertEqual(row["triangles"], 20_001)
        self.assertEqual(row["verdict"], "FAIL")
        self.assertTrue(any("20000" in f for f in row["fails"]))

    def test_total_over_budget_fails(self):
        r = run(cube("A"), cube("B", x0=1.0), budget=20)
        self.assertEqual(r["checks"]["budget"]["total_triangles"], 24)
        self.assertEqual(r["checks"]["budget"]["verdict"], "FAIL")
        self.assertEqual(r["verdict"], "FAIL")

    def test_total_without_budget_is_measured(self):
        b = run(cube("A"))["checks"]["budget"]
        self.assertEqual((b["total_triangles"], b["verdict"]), (12, "MEASURED"))

    def test_uv_at_1_2_counted_outside(self):
        self.assertEqual(ma.uv_outside([(0.5, 0.5), (1.2, 0.5), (0.0, 1.0), (1.0, -0.1)]), 2)
        row = ma.mesh_row(cube("Box", uvs=[(1.2, 0.3)] + [(0.5, 0.5)] * 23))
        self.assertEqual((row["uvs_outside_0_1"], row["verdict"]), (1, "FAIL"))

    def test_two_materials_and_two_uv_sets_fail(self):
        self.assertEqual(ma.mesh_row(cube("Box", materials=2))["verdict"], "FAIL")
        self.assertEqual(ma.mesh_row(cube("Box", uv_sets=2))["verdict"], "FAIL")

    def test_zero_area_face_is_counted(self):
        m = {"name": "Flat", "verts": [(0, 0, 0), (1, 0, 0), (2, 0, 0)], "polygons": [[0, 1, 2]]}
        self.assertEqual(ma.mesh_row(m)["zero_area_faces"], 1)


class SizeTest(unittest.TestCase):
    def test_size_within_tolerance_passes(self):
        self.assertEqual(ma.check_size([1.0, 1.0, 1.05], [1, 1, 1], 0.1)["verdict"], "PASS")

    def test_size_outside_tolerance_fails(self):
        self.assertEqual(ma.check_size([1.0, 1.0, 1.5], [1, 1, 1], 0.1)["verdict"], "FAIL")

    def test_size_without_tolerance_is_measured(self):
        self.assertEqual(ma.check_size([1.0, 1.0, 1.5], [1, 1, 1], None)["verdict"], "MEASURED")
        self.assertEqual(ma.check_size([1.0, 1.0, 1.5])["verdict"], "MEASURED")

    def test_bbox_in_studs(self):
        r = run(cube("A", s=2.0), cube("B", x0=2.0))
        self.assertEqual(r["checks"]["size"]["measured_studs_xyz"], [3.0, 2.0, 2.0])


class RecordTest(unittest.TestCase):
    def test_names_missing_and_extra(self):
        n = ma.check_names(["Body", "Hat"], ["Body", "Head"])
        self.assertEqual((n["missing"], n["extra"], n["verdict"]), (["Head"], ["Hat"], "FAIL"))
        self.assertEqual(ma.check_names(["Body"])["verdict"], "MEASURED")

    def test_export_lists_helpers_and_hidden(self):
        objs = [{"name": "Body", "type": "MESH", "hidden": []},
                {"name": "Old", "type": "MESH", "hidden": ["disabled in renders"]},
                {"name": "Camera", "type": "CAMERA", "hidden": []},
                {"name": "Grip", "type": "EMPTY", "hidden": []},
                {"name": "Junk", "type": "EMPTY", "hidden": []}]
        e = ma.check_export(objs, ["Body", "Old", "Camera", "Grip"])
        self.assertEqual([x["name"] for x in e["listed"]], ["Old", "Camera", "Junk"])
        self.assertEqual(e["verdict"], "FAIL")

    def test_worst_row(self):
        self.assertEqual(ma.worst(["PASS", "MEASURED"]), "MEASURED")
        self.assertEqual(ma.worst(["PASS", "MEASURED", "FAIL"]), "FAIL")

    def test_summary_is_markdown(self):
        md = ma.summary_md(run(cube("Box")))
        self.assertIn("| Box | 12 |", md)


class ReuseTest(unittest.TestCase):
    def test_parts_agree_with_rig_audit_count(self):
        polys = [list(f) for f in CUBE_FACES] + [[i + 8 for i in f] for f in CUBE_FACES]
        self.assertEqual(len(ma.face_parts(polys)), ma.ra.count_parts(16, [(a, b) for p in polys
                                                                           for a, b in zip(p, p[1:] + p[:1])]))

    def test_no_copy_of_rig_audit_functions(self):
        src = (Path(ma.__file__).parent).glob("*.py")
        for f in src:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("def audit_mesh", text, f.name)
            self.assertNotIn("def count_parts", text, f.name)


if __name__ == "__main__":
    unittest.main()


class TexelDensityTest(unittest.TestCase):
    """J018 G3-P8: DT9 px per stud from areas."""

    def test_formula(self):
        # a 1024 x 1024 texture whose UVs fill a quarter of the map, on 4 square studs: 256 px per stud
        self.assertAlmostEqual(ma.texel_density(1024, 1024, 0.25, 4.0), 256.0)
        self.assertIsNone(ma.texel_density(1024, 1024, 0.0, 4.0))
