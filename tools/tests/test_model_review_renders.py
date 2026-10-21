"""Offline tests for tools/model/review_renders.py camera placement (no Blender needed)."""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "model"))
import review_renders as rr  # noqa: E402

BMIN, BMAX = (-1.0, -0.5, 0.0), (1.0, 0.5, 3.0)  # 2 x 1 x 3 studs, standing on z = 0


def forward(rot):
    return tuple(-rot[i][2] for i in range(3))  # camera looks down its -Z axis


class LookAtTest(unittest.TestCase):
    def test_camera_points_at_target(self):
        rot = rr.look_at((0, -10, 0), (0, 0, 0), (0, 0, 1))
        for a, b in zip(forward(rot), (0, 1, 0)):
            self.assertAlmostEqual(a, b)
        self.assertAlmostEqual(rot[2][1], 1.0)  # image up = world +Z

    def test_rotation_is_orthonormal(self):
        rot = rr.look_at((3, -4, 2), (0, 0, 1), (0, 0, 1))
        cols = [[rot[i][j] for i in range(3)] for j in range(3)]
        for j in range(3):
            self.assertAlmostEqual(sum(x * x for x in cols[j]), 1.0)
            for k in range(j + 1, 3):
                self.assertAlmostEqual(sum(a * b for a, b in zip(cols[j], cols[k])), 0.0)


class OrthoTest(unittest.TestCase):
    def test_square_image_uses_longer_side(self):
        self.assertAlmostEqual(rr.ortho_scale(2, 3, 1024, 1024, 1.0), 3.0)

    def test_wide_image_fits_height(self):
        self.assertAlmostEqual(rr.ortho_scale(2, 3, 2048, 1024, 1.0), 6.0)  # 3 tall needs 6 wide
        self.assertAlmostEqual(rr.ortho_scale(8, 3, 2048, 1024, 1.0), 8.0)

    def test_tall_image(self):
        self.assertAlmostEqual(rr.ortho_scale(3, 2, 1024, 2048, 1.0), 6.0)

    def test_views_frame_the_right_extents(self):
        v = rr.plan_views(BMIN, BMAX, (1000, 1000), margin=1.0)
        self.assertAlmostEqual(v["front"]["ortho_scale"], 3.0)  # x 2, z 3
        self.assertAlmostEqual(v["left"]["ortho_scale"], 3.0)  # y 1, z 3
        self.assertAlmostEqual(v["top"]["ortho_scale"], 2.0)  # x 2, y 1

    def test_ortho_cameras_sit_outside_and_look_in(self):
        v = rr.plan_views(BMIN, BMAX)
        expect = {"front": (0, 1, 0), "back": (0, -1, 0), "left": (1, 0, 0), "right": (-1, 0, 0), "top": (0, 0, -1)}
        for name, f in expect.items():
            for a, b in zip(forward(v[name]["rotation"]), f):
                self.assertAlmostEqual(a, b, msg=name)
            self.assertGreater(math.dist(v[name]["eye"], v[name]["target"]), math.dist(BMIN, BMAX) / 2, name)
        self.assertAlmostEqual(v["top"]["rotation"][1][1], 1.0)  # top image up = +Y


class PerspectiveTest(unittest.TestCase):
    def test_fit_distance_shows_sphere(self):
        d = rr.fit_distance(1.0, 60.0, 100, 100, 1.0)
        self.assertAlmostEqual(math.asin(1.0 / d), math.radians(30))

    def test_fit_distance_uses_narrower_axis(self):
        self.assertGreater(rr.fit_distance(1.0, 60.0, 100, 200, 1.0), rr.fit_distance(1.0, 60.0, 100, 100, 1.0))

    def test_three_quarter_from_front_right_above(self):
        v = rr.plan_views(BMIN, BMAX)["three_quarter"]
        ex, ey, ez = (e - t for e, t in zip(v["eye"], v["target"]))
        self.assertGreater(ex, 0)
        self.assertLess(ey, 0)
        self.assertAlmostEqual(ex, -ey)
        self.assertAlmostEqual(math.degrees(math.atan2(ez, math.hypot(ex, ey))), 20.0)
        self.assertEqual(v["type"], "PERSP")

    def test_game_camera(self):
        v = rr.plan_views(BMIN, BMAX, game_cam=(12.0, 6.0, 70.0))["game"]
        self.assertEqual(v["eye"], (0.0, -12.0, 6.0))
        self.assertEqual(v["target"], (0.0, 0.0, 1.5))
        self.assertEqual(v["fov_deg"], 70.0)
        self.assertGreater(v["clip_end"], math.dist(v["eye"], v["target"]))

    def test_no_game_camera_without_flag(self):
        self.assertNotIn("game", rr.plan_views(BMIN, BMAX))


class DummyTest(unittest.TestCase):
    def test_dummy_beside_model_on_its_feet(self):
        d = rr.dummy_box(BMIN, BMAX, 5.0)
        self.assertEqual(d["min"][2], 0.0)
        self.assertEqual(d["max"][2], 5.0)
        self.assertGreater(d["min"][0], BMAX[0])

    def test_scale_view_frames_model_and_dummy(self):
        v = rr.plan_views(BMIN, BMAX, (1000, 1000), margin=1.0, player_height=5.0)["scale"]
        # union: x from -1 to 1 + 1 gap + 2 block = 4 -> 5 wide; z 0..5 -> 5 tall
        self.assertAlmostEqual(v["ortho_scale"], 5.0)
        self.assertEqual(v["dummy"]["size"], (2.0, 1.0, 5.0))

    def test_all_standard_views_planned(self):
        self.assertEqual(set(rr.plan_views(BMIN, BMAX)),
                         {"front", "back", "left", "right", "top", "three_quarter", "scale"})


if __name__ == "__main__":
    unittest.main()
