"""Offline tests for tools/rig/rig_audit.py pure checks (no Blender needed)."""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "rig"))
import rig_audit as ra  # noqa: E402

CUBE = [[0, 1, 2, 3], [4, 7, 6, 5], [0, 4, 5, 1], [1, 5, 6, 2], [2, 6, 7, 3], [3, 7, 4, 0]]


class WeightTest(unittest.TestCase):
    BONES = {"Root", "Spine", "Head", "ArmL", "ArmR"}

    def test_clean_rig_passes(self):
        vw = [[("Spine", 1.0)], [("Spine", 0.5), ("Head", 0.5)], [("ArmL", 1.0), ("ctrl_select", 1.0)]]
        r = ra.audit_weights(vw, self.BONES, root="Root")
        self.assertEqual(r["verdict"], "PASS")
        self.assertEqual(r["non_deform_groups_with_weight"], ["ctrl_select"])  # ignored, but reported

    def test_five_influences_fail(self):
        vw = [[("Root", 0.0), ("Spine", 0.2), ("Head", 0.2), ("ArmL", 0.2), ("ArmR", 0.2), ("Root", 0.2)]]
        r = ra.audit_weights(vw, self.BONES, root="Root")
        self.assertEqual(r["over_influence_limit"]["count"], 1)
        self.assertEqual(r["root_weighted"]["count"], 1)
        self.assertEqual(r["verdict"], "FAIL")

    def test_root_weight_fails_even_alone(self):
        r = ra.audit_weights([[("Root", 1.0)]], self.BONES, root="Root")
        self.assertEqual(r["verdict"], "FAIL")

    def test_zero_weight_root_is_not_an_influence(self):
        r = ra.audit_weights([[("Root", 0.0), ("Spine", 1.0)]], self.BONES, root="Root")
        self.assertEqual(r["verdict"], "PASS")

    def test_unweighted_and_unnormalized_are_reported(self):
        r = ra.audit_weights([[], [("Spine", 0.4), ("Head", 0.3)]], self.BONES)
        self.assertEqual(r["unweighted"]["count"], 1)
        self.assertEqual(r["not_normalized"]["count"], 1)

    def test_nan_weight_is_invalid(self):
        r = ra.audit_weights([[("Spine", math.nan)]], self.BONES)
        self.assertEqual(r["invalid_weight"]["count"], 1)
        self.assertEqual(r["verdict"], "FAIL")


class MeshTest(unittest.TestCase):
    def test_closed_cube(self):
        r = ra.audit_mesh(CUBE, 8)
        self.assertEqual((r["triangles"], r["non_manifold_edges"], r["connected_parts"]), (12, 0, 1))
        self.assertEqual(r["verdict"], "PASS")

    def test_open_cube_fails(self):
        r = ra.audit_mesh(CUBE[:-1], 8)
        self.assertEqual(r["boundary_edges"], 4)
        self.assertEqual(r["verdict"], "FAIL")

    def test_two_islands_in_one_object(self):
        second = [[i + 8 for i in face] for face in CUBE]
        r = ra.audit_mesh(CUBE + second, 16)
        self.assertEqual(r["connected_parts"], 2)

    def test_triangle_limit(self):
        tris = [[0, 1, 2]] * 20_001
        self.assertEqual(ra.audit_mesh(tris, 3)["verdict"], "FAIL")
        self.assertEqual(ra.audit_mesh(tris, 3, max_triangles=30_000)["triangles"], 20_001)


class MotionTest(unittest.TestCase):
    REST = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]

    def test_protected_region_moves(self):
        posed = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.3), (0.0, 0.0, 1.0)]
        r = ra.max_displacement(self.REST, posed, [0, 1, 2])
        self.assertAlmostEqual(r["max"], 0.3)
        self.assertEqual(r["vertex"], 2)

    def test_rigid_rotation_has_no_drift(self):
        c, s = math.cos(0.7), math.sin(0.7)
        posed = [(x * c - y * s, x * s + y * c, z) for x, y, z in self.REST]
        self.assertLess(ra.rigid_drift(self.REST, posed, [0, 1, 2, 3])["max"], 1e-9)

    def test_bent_part_drifts(self):
        posed = list(self.REST)
        posed[3] = (0.0, 0.0, 1.5)
        self.assertAlmostEqual(ra.rigid_drift(self.REST, posed, [0, 1, 2, 3])["max"], 0.5 * 1.0 + 0.0, places=6)

    def test_no_tolerance_means_measured_not_pass(self):
        self.assertEqual(ra.judge(0.0, None), "MEASURED")
        self.assertEqual(ra.judge(0.002, 0.001), "FAIL")
        self.assertEqual(ra.judge(0.001, 0.001), "PASS")


if __name__ == "__main__":
    unittest.main()
