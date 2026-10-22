"""Offline tests for tools/anim/clip_check.py pure checks (no Blender needed)."""

import contextlib
import io
import json
import math
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "anim"))
import clip_check as cc  # noqa: E402

TOL = {"loop_seam_position": 0.01, "loop_seam_velocity": 0.5, "contact_slide": 0.01,
       "contact_drift_vertical": 0.01, "event_offset_frames": 0.5, "rom_over": 0.0, "pop_ratio": 10.0,
       "window": [0.9, 1.1]}
TIMING = {"events": [
    {"event_id": "footdown_L", "marker": "footdown_L", "time_s": "3/10"},
    {"event_id": "contact_confirmed", "marker": "—", "time_s": "—"},
]}
MANIFEST = {"controls": [
    {"control_id": "P01.yaw", "pose_bone": "c_Head", "channel": "rotation_euler.y", "units": "deg",
     "min": -60, "max": 60},
    {"control_id": "P12.ik", "pose_bone": "c_FootIK_L", "units": "0 = FK, 1 = IK"},
]}


def swing(f: int) -> int:
    """Foot swing step: 0 at frames 5..15 (planted), 1..19 over frames 16..31 then 1..4 (31 duplicates 1)."""
    if 5 <= f <= 15:
        return 0
    return f - 15 if f >= 16 else f + 15


def clean_clip() -> dict:
    """Frames 1..31 at 30 fps (1 s), loop with duplicate end; a hand on a sine, a planted foot."""
    frames = range(1, 32)
    hand = [[math.sin(2 * math.pi * (f - 1) / 30), 1.0, 0.0] for f in frames]
    foot = [[0.2, 0.1 * (1 - math.cos(math.pi * swing(f) / 10)), 0.0] for f in frames]
    yaw = [50 * math.sin(2 * math.pi * (f - 1) / 30) for f in frames]
    return {"clip": "walk", "fps": [30, 1], "frame_start": 1, "frame_end": 31, "loop": True,
            "loop_end_duplicates_start": True, "units": "studs",
            "landmarks": {"hand_R": hand, "foot_L": foot}, "controls": {"P01.yaw": yaw},
            "contacts": [{"landmark": "foot_L", "start": 5, "end": 15, "kind": "planted"}],
            "markers": [{"name": "footdown_L", "frame": 10}]}


def by(report, check, item=None):
    return [r for r in report["results"] if r["check"] == check and (item is None or r["item"] == item)]


class LengthTest(unittest.TestCase):
    def test_exact_one_second(self):
        r = cc.check_length(clean_clip())
        self.assertEqual(r["where"]["exact"], "1")
        self.assertEqual(Fraction(r["where"]["exact"]), Fraction(1))
        self.assertEqual(r["result"], "MEASURED")

    def test_ntsc_rate_is_exact(self):
        s = clean_clip() | {"fps": [30000, 1001]}
        self.assertEqual(Fraction(cc.check_length(s)["where"]["exact"]), Fraction(30 * 1001, 30000))

    def test_window(self):
        self.assertEqual(cc.check_length(clean_clip(), [0.9, 1.1])["result"], "PASS")
        self.assertEqual(cc.check_length(clean_clip(), [1.2, 2.0])["result"], "FAIL")


class CleanClipTest(unittest.TestCase):
    def test_clean_passes_with_tolerances(self):
        rep = cc.run_all(clean_clip(), TIMING, MANIFEST, TOL)
        self.assertEqual(rep["summary"]["FAIL"], 0, rep["failing"])
        self.assertEqual(rep["summary"]["MEASURED"], 0)
        self.assertEqual(rep["verdict"], "PASS")
        self.assertEqual(rep["frames_to_render"], [])

    def test_no_tolerance_is_measured(self):
        rep = cc.run_all(clean_clip(), TIMING, MANIFEST)
        self.assertEqual(rep["summary"]["PASS"], 0)
        self.assertEqual(rep["summary"]["FAIL"], 0)
        self.assertEqual(rep["verdict"], "MEASURED")
        for r in rep["results"]:
            self.assertIsNone(r["tolerance"])

    def test_record_shape(self):
        rep = cc.run_all(clean_clip(), TIMING, MANIFEST, TOL)
        checks = {r["check"] for r in rep["results"]}
        self.assertEqual(checks, {"length", "loop_seam_position", "loop_seam_velocity", "contact_slide",
                                  "contact_drift_vertical", "events", "rom", "pops"})
        for r in rep["results"]:
            self.assertEqual(set(r), {"check", "item", "measured", "unit", "tolerance", "result", "where"})
            self.assertIn("frames", r["where"])


class PlantedFaultTest(unittest.TestCase):
    def test_seam_pop_fails(self):
        s = clean_clip()
        s["landmarks"]["hand_R"][-1] = [0.5, 1.0, 0.0]  # the duplicate end no longer matches the start
        rep = cc.run_all(s, tolerances=TOL)
        pos = by(rep, "loop_seam_position", "hand_R")[0]
        self.assertAlmostEqual(pos["measured"], 0.5)
        self.assertEqual(pos["result"], "FAIL")
        self.assertIn(31, rep["frames_to_render"])

    def test_seam_velocity_fails(self):
        s = clean_clip()
        s["landmarks"]["hand_R"][29][0] += 0.2  # the frame before the duplicate end: speed breaks at the join
        rep = cc.run_all(s, tolerances=TOL)
        self.assertEqual(by(rep, "loop_seam_velocity", "hand_R")[0]["result"], "FAIL")

    def test_non_duplicate_seam_uses_last_sample(self):
        s = clean_clip() | {"loop_end_duplicates_start": False}
        s["landmarks"] = {k: v[:-1] for k, v in s["landmarks"].items()}
        s["controls"] = {k: v[:-1] for k, v in s["controls"].items()}
        s["frame_end"] = 30
        rec = by(cc.run_all(s, tolerances=TOL), "loop_seam_velocity", "hand_R")[0]
        self.assertEqual(rec["result"], "PASS")

    def test_sliding_planted_foot_fails(self):
        s = clean_clip()
        for f in range(5, 16):
            s["landmarks"]["foot_L"][f - 1] = [0.2 + 0.01 * (f - 5), 0.0, 0.0]
        rep = cc.run_all(s, tolerances=TOL)
        slide = by(rep, "contact_slide")[0]
        self.assertAlmostEqual(slide["measured"], 0.1)
        self.assertEqual(slide["result"], "FAIL")
        self.assertEqual(slide["where"]["frames"], [5, 15])
        self.assertEqual(by(rep, "contact_drift_vertical")[0]["result"], "PASS")

    def test_up_axis_parameter(self):
        s = clean_clip()
        for f in range(5, 16):
            s["landmarks"]["foot_L"][f - 1] = [0.2, 0.0, 0.01 * (f - 5)]  # z drift
        r_y = {r["check"]: r for r in cc.check_contact_slide(s, up="y")}
        r_z = {r["check"]: r for r in cc.check_contact_slide(s, up="z")}
        self.assertAlmostEqual(r_y["contact_slide"]["measured"], 0.1)
        self.assertAlmostEqual(r_z["contact_drift_vertical"]["measured"], 0.1)
        self.assertAlmostEqual(r_z["contact_slide"]["measured"], 0.0)

    def test_moved_marker_fails(self):
        s = clean_clip()
        s["markers"] = [{"name": "footdown_L", "frame": 13}]
        rec = by(cc.run_all(s, TIMING, tolerances=TOL), "events", "footdown_L")[0]
        self.assertEqual(rec["measured"], 3.0)
        self.assertAlmostEqual(rec["where"]["offset_s"], 0.1)
        self.assertEqual(rec["where"]["frames"], [10, 13])
        self.assertEqual(rec["result"], "FAIL")

    def test_missing_and_extra_markers(self):
        s = clean_clip()
        s["markers"] = [{"name": "spare", "frame": 4}]
        recs = by(cc.run_all(s, TIMING, tolerances=TOL), "events")
        missing = [r for r in recs if r["where"].get("problem") == "missing"]
        extra = [r for r in recs if str(r["where"].get("problem", "")).startswith("extra")]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0]["result"], "FAIL")
        self.assertEqual(len(extra), 1)
        self.assertEqual(extra[0]["result"], "MEASURED")

    def test_timing_by_frame(self):
        timing = [{"id": "footdown_L", "marker_name": "footdown_L", "frame": 10}]
        rec = cc.check_events(clean_clip(), timing, 0.5)[0]
        self.assertEqual(rec["measured"], 0.0)
        self.assertEqual(rec["result"], "PASS")

    def test_over_range_control_fails(self):
        s = clean_clip()
        s["controls"]["P01.yaw"][7] = 70.0
        rec = by(cc.run_all(s, manifest=MANIFEST, tolerances=TOL), "rom")[0]
        self.assertEqual(rec["item"], "P01.yaw")
        self.assertAlmostEqual(rec["measured"], 10.0)
        self.assertEqual(rec["unit"], "deg")
        self.assertEqual(rec["where"]["frames"], [8])
        self.assertEqual(rec["result"], "FAIL")

    def test_control_without_range_skipped(self):
        s = clean_clip()
        s["controls"]["P12.ik"] = [1.0] * 31
        self.assertEqual([r["item"] for r in cc.check_rom(s, MANIFEST)], ["P01.yaw"])

    def test_pop_ratio(self):
        s = clean_clip()
        s["landmarks"]["hand_R"][12][1] += 0.3
        rep = cc.run_all(s, tolerances=TOL)
        rec = by(rep, "pops", "hand_R")[0]
        self.assertEqual(rec["result"], "FAIL")
        self.assertIn(13, rec["where"]["frames"])
        self.assertEqual(by(cc.run_all(s), "pops", "hand_R")[0]["result"], "MEASURED")


class JudgeAndInputTest(unittest.TestCase):
    def test_judge(self):
        self.assertEqual(cc.judge(0.1, None), "MEASURED")
        self.assertEqual(cc.judge(None, 1.0), "MEASURED")
        self.assertEqual(cc.judge(0.1, 0.1), "PASS")
        self.assertEqual(cc.judge(0.2, 0.1), "FAIL")

    def test_bad_input(self):
        s = clean_clip()
        s["landmarks"]["hand_R"] = s["landmarks"]["hand_R"][:-1]
        with self.assertRaises(ValueError):
            cc.run_all(s)
        with self.assertRaises(ValueError):
            cc.run_all(clean_clip(), tolerances={"foot_slide": 0.1})

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
            good, bad, tol = Path(d, "s.json"), Path(d, "bad.json"), Path(d, "tol.json")
            good.write_text(json.dumps(clean_clip()), encoding="utf-8")
            tol.write_text(json.dumps(TOL), encoding="utf-8")
            bad.write_text("{not json", encoding="utf-8")
            self.assertEqual(cc.main([str(good), "--tol", str(tol), "--out", str(Path(d, "r.json"))]), 0)
            self.assertTrue(Path(d, "r.json").exists())
            fault = clean_clip()
            fault["landmarks"]["hand_R"][-1] = [0.5, 1.0, 0.0]
            good.write_text(json.dumps(fault), encoding="utf-8")
            self.assertEqual(cc.main([str(good), "--tol", str(tol)]), 1)
            self.assertEqual(cc.main([str(bad)]), 2)


if __name__ == "__main__":
    unittest.main()


class ChannelValueTest(unittest.TestCase):
    """J018: quaternion components follow Blender's (w, x, y, z) order; degrees on a quaternion are refused."""

    class _PB:
        rotation_quaternion = (0.9, 0.1, 0.2, 0.3)
        rotation_euler = (0.5, 0.25, 0.0)

    def test_quaternion_order(self):
        self.assertEqual(cc._channel_value(self._PB, "rotation_quaternion.w", "blender_units"), 0.9)
        self.assertEqual(cc._channel_value(self._PB, "rotation_quaternion.z", "blender_units"), 0.3)

    def test_euler_unchanged(self):
        self.assertAlmostEqual(cc._channel_value(self._PB, "rotation_euler.y", "deg"), math.degrees(0.25))

    def test_degrees_on_quaternion_refused(self):
        with self.assertRaises(ValueError):
            cc._channel_value(self._PB, "rotation_quaternion.x", "deg")


class CurvesTest(unittest.TestCase):
    """J018 G3-P8: the curve lines the animator computed by hand."""

    def jump(self, gravity=True):
        n = 21
        hs = [(1 - ((i - 10) / 10) ** 2) * 2 for i in range(n)] if gravity else [2 - abs(i - 10) / 5 for i in range(n)]
        root = [[i * 0.1, h, 0.0] for i, h in enumerate(hs)]
        return {"clip": "jump", "fps": [30, 1], "frame_start": 1, "frame_end": n, "units": "studs",
                "landmarks": {"root": root},
                "controls": {"arm_L": [0.0] * 5 + [0.5, 1.2, 0.9, 1.05, 1.0] + [1.0] * 11,
                             "arm_R": [0.0] * 5 + [-0.5, -1.2, -0.9, -1.05, -1.0] + [-1.0] * 11}}

    def by(self, recs, check):
        return [r for r in recs if r["check"] == check]

    def test_gravity_spacing_and_hang_time(self):
        g = self.by(cc.check_curves(self.jump(True), "root"), "gravity_spacing")[0]["measured"]
        lin = self.by(cc.check_curves(self.jump(False), "root"), "gravity_spacing")[0]["measured"]
        self.assertLess(g, 0.6)          # slow at the top, fast near the ground
        self.assertGreater(lin, 0.9)     # even spacing
        h = self.by(cc.check_curves(self.jump(True), "root"), "hang_time")[0]["measured"]
        self.assertEqual(h["launch_to_apex_frames"], h["apex_to_landing_frames"])

    def test_arc_and_overshoot_and_twins(self):
        recs = cc.check_curves(self.jump(False), "root", twins=[("arm_L", "arm_R")])
        self.assertGreaterEqual(self.by(recs, "arc_straight_run")[0]["measured"], 8)   # a linear jump has straight runs
        ov = {r["item"]: r["measured"] for r in self.by(recs, "overshoot")}
        self.assertGreater(ov["arm_L"]["crossings"], 0)
        tw = self.by(recs, "twinning")[0]
        self.assertEqual(tw["measured"], 1.0)
        self.assertAlmostEqual(tw["where"]["mean_mirrored_difference"], 0.0)

    def test_root_must_exist(self):
        with self.assertRaises(ValueError):
            cc.check_curves(self.jump(), "hips")
