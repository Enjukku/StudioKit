"""Offline tests for tools/film/shotlist.py (fixtures in tools/tests/fixtures/film; Blender only if BLENDER_EXE is set)."""

import ast
import contextlib
import copy
import io
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import types
import unittest
from unittest import mock
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "film"))
import shotlist as sl  # noqa: E402

FIX = ROOT / "tools" / "tests" / "fixtures" / "film"
EXAMPLE = FIX / "boss-reveal.shots.json"  # the paper example with TEST VALUE timings
TEMPLATE = ROOT / "templates" / "film" / "shotlist.example.json"


def load(name):
    return json.loads((FIX / name).read_text(encoding="utf-8"))


DRILL = load("drill.shots.json")


def shot(sid, frames, **kw):
    s = {"id": sid, "frames": frames, "size": "wide", "angle": "eye", "lens": "UNKNOWN", "movement": "static",
         "action": "a", "sound": "none", "emotion": "e", "transition": "cut"}
    s.update(kw)
    return s


def plan(frames_list, fps=(30, 1), stage="previs", cues=(), start=1):
    return {"format": sl.FORMAT, "sequence": "t", "title": "t", "revision": 1, "stage": stage, "fps": list(fps),
            "start_frame": start, "aspect": [16, 9], "board_policy": "constraint",
            "shots": [shot(f"S{i + 1}", f) for i, f in enumerate(frames_list)], "cues": list(cues)}


def cue(cid="sfx.a.b", shot_id="S1", at=0, **kw):
    c = {"id": cid, "shot": shot_id, "at": at, "kind": "sfx", "sync": "locked"}
    c.update(kw)
    return c


def errors(data):
    rep, _ = sl.validate(data)
    return [e["where"] + ": " + e["msg"] for e in rep.errors]


def run_main(args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = sl.main([str(a) for a in args])
    return code, out.getvalue(), err.getvalue()


def push_payload(script: str) -> dict:
    line = next(ln for ln in script.splitlines() if ln.startswith("DATA = json.loads("))
    return json.loads(ast.literal_eval(line[len("DATA = json.loads("):-1]))


class TimingTest(unittest.TestCase):
    """C1, C2: half-open intervals and exact fractions."""

    def test_c1_31_frames_last_31_over_30_s(self):
        _, tl = sl.validate(plan([31]))
        self.assertEqual(sl.frame_time(tl["shots"][0]["frames"], tl["rate"]), Fraction(31, 30))
        self.assertEqual(tl["total_frames"], 31)

    def test_c1_cut_list_30_30_puts_shot_2_at_exactly_1_s(self):
        _, tl = sl.validate(plan([30, 30]))
        s2 = tl["shots"][1]
        self.assertEqual(s2["start_frame"], 31)
        self.assertEqual(sl.frame_time(s2["offset"], tl["rate"]), Fraction(1))
        self.assertEqual(sl.frame_time(tl["total_frames"], tl["rate"]), Fraction(2))

    def test_c1_start_frame_shifts_frames_not_times(self):
        _, tl = sl.validate(plan([30, 30], start=101))
        self.assertEqual([s["start_frame"] for s in tl["shots"]], [101, 131])
        self.assertEqual(sl.frame_time(tl["shots"][1]["offset"], tl["rate"]), 1)

    def test_c2_ntsc_rate_stays_exact(self):
        _, tl = sl.validate(plan([1001, 30], fps=(30000, 1001)))
        self.assertEqual(sl.frame_time(1001, tl["rate"]), Fraction(1001 * 1001, 30000))
        self.assertIsInstance(sl.frame_time(1001, tl["rate"]), Fraction)
        res = sl.check_result("x", None, *sl.validate(plan([1001, 30], fps=(30000, 1001))))
        self.assertEqual(res["shots"][0]["duration_s"], "1002001/30000")
        self.assertEqual(res["shots"][1]["start_s"], "1002001/30000")

    def test_c2_blender_script_sets_exact_ntsc_rate(self):
        data = plan([1001], fps=(30000, 1001))
        _, tl = sl.validate(data)
        p = push_payload(sl.blender_push_script(data, tl, "x.shots.json", "push.py"))
        self.assertEqual(p["fps"], 30000)  # fps 30 + base 1.001 is inexact in Blender's float32 (fact-check FC-08)
        self.assertEqual(p["fps_base"], 1001.0)
        self.assertEqual(Fraction(p["fps"]) / Fraction(p["fps_base"]), Fraction(30000, 1001))
        self.assertEqual((p["frame_start"], p["frame_end"]), (1, 1001))

    def test_blender_rate_integer_and_odd(self):
        self.assertEqual(sl.blender_rate(24, 1), (24, Fraction(1)))
        self.assertEqual(sl.blender_rate(24000, 1001), (24000, Fraction(1001)))
        self.assertEqual(sl.blender_rate(25, 2), (25, Fraction(2)))
        fps, base = sl.blender_rate(48000, 1001)  # above Blender's int fps range: rounded fallback
        self.assertEqual((fps, Fraction(fps) / base), (48, Fraction(48000, 1001)))
        with self.assertRaises(sl.ShotlistError):
            sl.blender_rate(40000, 3000000)

    def test_unknown_length_makes_later_starts_unknown(self):
        _, tl = sl.validate(plan([30, "UNKNOWN", 30], stage="plan"))
        self.assertEqual([s["start_frame"] for s in tl["shots"]], [1, 31, None])
        self.assertIsNone(tl["total_frames"])


class CheckTest(unittest.TestCase):
    """C3 and the schema rules."""

    def test_fixtures_and_example_are_valid(self):
        self.assertEqual(errors(DRILL), [])
        example = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(errors(example), [])
        self.assertEqual([s["id"] for s in example["shots"]], ["A", "B", "C", "D", "E"])
        for s in example["shots"]:
            self.assertIn("TEST VALUE", s["notes"])

    def test_template_has_no_invented_timings(self):
        tpl = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        self.assertEqual(errors(tpl), [])
        self.assertEqual(tpl["stage"], "plan")
        self.assertTrue(all(s["frames"] == "UNKNOWN" for s in tpl["shots"]))
        self.assertTrue(all(c["at"] == "UNKNOWN" for c in tpl["cues"]))
        self.assertNotIn("TEST VALUE", TEMPLATE.read_text(encoding="utf-8"))

    def test_c3_duplicate_ids(self):
        d = plan([30, 30])
        d["shots"][1]["id"] = "S1"
        self.assertTrue(any("duplicate shot id" in e for e in errors(d)))

    def test_c3_zero_and_negative_frames(self):
        for bad in (0, -5, 2.5, True, "30"):
            self.assertTrue(any("zero-length" in e for e in errors(plan([30, bad]))), bad)

    def test_c3_unknown_cue_shot(self):
        self.assertTrue(any("not a shot id" in e for e in errors(plan([30], cues=[cue(shot_id="S9")]))))

    def test_c3_cue_at_outside_shot(self):
        self.assertTrue(any("outside shot S1" in e for e in errors(plan([30], cues=[cue(at=30)]))))
        self.assertEqual(errors(plan([30], cues=[cue(at=29)])), [])
        self.assertTrue(any("greater than at" in e for e in errors(plan([30], cues=[cue(at=10, end=10)]))))

    def test_c3_unknown_at_previs_is_error(self):
        d = plan([30, "UNKNOWN"], cues=[cue(at="UNKNOWN")])
        d["shots"][0]["fov_deg"] = "UNKNOWN"
        errs = errors(d)
        self.assertTrue(any("frames UNKNOWN" in e for e in errs))
        self.assertTrue(any("fov_deg UNKNOWN" in e for e in errs))
        self.assertTrue(any("at UNKNOWN" in e for e in errs))
        for stage in ("locked", "runtime"):
            d["stage"] = stage
            self.assertEqual(len(errors(d)), 3)

    def test_c3_unknown_at_plan_is_open_item(self):
        d = plan([30, "UNKNOWN"], stage="plan", cues=[cue(at="UNKNOWN")])
        d["shots"][0]["fov_deg"] = "UNKNOWN"
        rep, _ = sl.validate(d)
        self.assertEqual(rep.errors, [])
        msgs = [o["msg"] for o in rep.open]
        for want in ("frames UNKNOWN", "fov_deg UNKNOWN", "at UNKNOWN", "total length UNKNOWN"):
            self.assertTrue(any(want in m for m in msgs), want)

    def test_schema_errors(self):
        d = plan([30])
        d.update(format="x", sequence="Bad_Name", revision=0, stage="final", fps=[30, 0], aspect=[16],
                 board_policy="any", fov_mode="Horizontal")
        errs = " ".join(errors(d))
        for key in ("format", "kebab-case", "revision", "stage", "fps", "aspect", "board_policy", "fov_mode"):
            self.assertIn(key, errs)
        d = plan([30])
        del d["shots"][0]["emotion"]
        d["shots"][0]["size"] = " "
        self.assertTrue(any("missing field 'emotion'" in e for e in errors(d)))
        self.assertTrue(any("size is empty" in e for e in errors(d)))

    def test_cue_rules(self):
        self.assertTrue(any("dotted" in e for e in errors(plan([30], cues=[cue(cid="nodots")]))))
        self.assertTrue(any("duplicate cue" in e for e in errors(plan([30], cues=[cue(), cue()]))))
        d = plan([30])
        d["shots"][0]["id"] = "a.b"
        d["cues"] = [cue(cid="a.b", shot_id="a.b")]
        self.assertTrue(any("equals a shot id" in e for e in errors(d)))
        self.assertTrue(any("kind" in e for e in errors(plan([30], cues=[cue(kind="noise")]))))

    def test_fov_range_with_named_bound(self):
        for bad, ok in ((0, False), (120, True), (120.5, False), (0.5, True)):
            d = plan([30])
            d["shots"][0]["fov_deg"] = bad
            self.assertEqual(errors(d) == [], ok, bad)
        self.assertEqual(sl.FOV_MAX_DEG, 120)

    def test_fov_bound_source_line_states_it(self):
        path, lines = sl.FOV_SRC.rsplit(":", 1)
        a, b = (int(x) for x in lines.split("-"))
        text = " ".join((ROOT / path).read_text(encoding="utf-8").splitlines()[a - 1:b])
        self.assertRegex(text, r"`1`\s+and\s+`120`\s+degrees")

    def test_warnings_do_not_change_exit_code(self):
        d = copy.deepcopy(DRILL)
        d["extra_key"] = 1
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "w.shots.json"
            p.write_text(json.dumps(d), encoding="utf-8")
            code, out, _ = run_main(["check", p, "--json"])
            res = json.loads(out)
            self.assertEqual(code, 0)
            self.assertEqual(len(res["warnings"]), 1)
            d["shots"][0]["frames"] = 0
            p.write_text(json.dumps(d), encoding="utf-8")
            self.assertEqual(run_main(["check", p])[0], 1)

    def test_check_json_totals(self):
        code, out, _ = run_main(["check", FIX / "drill.shots.json", "--json"])
        res = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual(res["total"], {"frames": 105, "seconds": "7/2", "seconds_decimal": "3.500000"})
        self.assertEqual([s["start_frame"] for s in res["shots"]], [1, 31, 61])
        self.assertEqual(res["shots"][2]["end_frame_exclusive"], 106)

    def test_nan_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "n.shots.json"
            p.write_text(json.dumps(DRILL).replace('"fov_deg": 23', '"fov_deg": NaN'), encoding="utf-8")
            code, _, err = run_main(["check", p])
            self.assertEqual(code, 1)
            self.assertIn("NaN", err)


class FovTest(unittest.TestCase):
    """C4: vertical FOV from focal length, sensor size, sensor fit and aspect."""

    def test_c4_horizontal_sensor_16_9(self):
        want = math.degrees(2 * math.atan((36 / (16 / 9)) / (2 * 50)))
        got = sl.vertical_fov_deg({"focal_mm": 50, "sensor_mm": 36, "sensor_fit": "HORIZONTAL"}, (16, 9))
        self.assertAlmostEqual(got, want, places=12)

    def test_vertical_and_auto(self):
        v = sl.vertical_fov_deg({"focal_mm": 35, "sensor_mm": 24, "sensor_fit": "VERTICAL"}, (16, 9))
        self.assertAlmostEqual(v, math.degrees(2 * math.atan(24 / 70)), places=12)
        lens = {"focal_mm": 50, "sensor_mm": 36, "sensor_fit": "AUTO"}
        self.assertAlmostEqual(sl.vertical_fov_deg(lens, (16, 9)),
                               sl.vertical_fov_deg(dict(lens, sensor_fit="HORIZONTAL"), (16, 9)), places=12)
        self.assertAlmostEqual(sl.vertical_fov_deg(lens, (9, 16)),
                               sl.vertical_fov_deg(dict(lens, sensor_fit="VERTICAL"), (9, 16)), places=12)

    def test_difference_reported_and_judged_only_with_tolerance(self):
        rep, tl = sl.validate(DRILL)
        s = tl["shots"][0]
        want = 23 - math.degrees(2 * math.atan((36 / (16 / 9)) / 100))
        self.assertAlmostEqual(s["fov_diff_deg"], want, places=12)
        self.assertEqual(rep.errors, [])
        rep, _ = sl.validate(DRILL, fov_tol=0.05)
        self.assertTrue(any("caller tolerance" in e["msg"] for e in rep.errors))
        self.assertEqual(sl.validate(DRILL, fov_tol=0.2)[0].errors, [])
        code, _, err = run_main(["check", FIX / "drill.shots.json", "--fov-tol-deg", "0.1"])
        self.assertEqual(code, 1)
        self.assertIn("--tol-source", err)

    def test_non_vertical_mode_not_compared(self):
        d = copy.deepcopy(DRILL)
        d["fov_mode"] = "Diagonal"
        rep, tl = sl.validate(d)
        self.assertIsNone(tl["shots"][0]["fov_diff_deg"])
        self.assertTrue(any("not compared" in w["msg"] for w in rep.warnings))


class OutputTest(unittest.TestCase):
    def test_table_shows_unknown_and_header(self):
        d = plan([30, "UNKNOWN", 45], stage="plan", fps=(30000, 1001))
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "t.shots.json"
            p.write_text(json.dumps(d), encoding="utf-8")
            code, out, _ = run_main(["table", p])
        self.assertEqual(code, 0)
        self.assertIn("fps 30000/1001 (29.970030)", out)
        self.assertIn("total UNKNOWN", out)
        rows = [ln for ln in out.splitlines() if ln.startswith("| S")]
        self.assertEqual(rows[0].split(" | ")[1:3], ["0.000-1.001", "30 / 1.001"])
        self.assertEqual(rows[1].split(" | ")[1:3], ["1.001-UNKNOWN", "UNKNOWN"])
        self.assertEqual(rows[2].split(" | ")[1:3], ["UNKNOWN", "45 / 1.502"])

    def test_cues_sorted_by_time_unknown_last(self):
        code, out, _ = run_main(["cues", EXAMPLE])
        self.assertEqual(code, 0)
        ids = [ln.split(" | ")[0][2:] for ln in out.splitlines() if ln.startswith("| ") and "." in ln.split(" | ")[0]]
        self.assertEqual(ids, ["amb.water.observatory", "sfx.beacon.pulse", "sfx.water.disturbance",
                               "sfx.guardian.stone", "vo.guardian.vocal", "music.encounter.entry",
                               "ui.interact.available"])
        self.assertIn("| sfx.beacon.pulse | A | 1.000 | 31 |", out)

    def test_markdown_cells_escaped(self):
        self.assertEqual(sl.md("a|b\nc"), "a\\|b c")

    def test_luau_module(self):
        _, tl = sl.validate(DRILL)
        text = sl.luau_module(DRILL, tl, "tools/tests/fixtures/film/drill.shots.json")
        self.assertTrue(text.startswith("--!strict\n-- generated by tools/film/shotlist.py from "
                                        "tools/tests/fixtures/film/drill.shots.json rev 3; edit the .shots.json, "
                                        "not this file\n"))
        self.assertIn('{ id = "S020", startFrame = 31, frames = 30, start = 1.000000, duration = 1.000000, '
                      'fovDeg = nil, transition = "cut" }', text)
        self.assertIn('time = 0.166667, kind = "ambience", sync = "flexible", endTime = 2.333333', text)
        self.assertIn("fps = { num = 30, den = 1 }", text)
        self.assertTrue(text.rstrip().endswith("return sequence"))

    def test_luau_ntsc_six_decimals_from_fraction(self):
        d = plan([1001, 30], fps=(30000, 1001))
        _, tl = sl.validate(d)
        text = sl.luau_module(d, tl, "x")
        self.assertIn("start = 33.400033", text)  # 1002001/30000 = 33.4000333...

    def test_luau_and_blender_refuse_unknown(self):
        ex = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        _, tl = sl.validate(ex)
        with self.assertRaisesRegex(sl.ShotlistError, "music.encounter.entry"):
            sl.luau_module(ex, tl, "x")
        d = plan([30, "UNKNOWN"], stage="plan")
        _, tl = sl.validate(d)
        with self.assertRaisesRegex(sl.ShotlistError, "S2"):
            sl.blender_push_script(d, tl, "x", "p.py")
        with self.assertRaisesRegex(sl.ShotlistError, "S2"):
            sl.luau_module(d, tl, "x")
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "u.shots.json"
            p.write_text(json.dumps(d), encoding="utf-8")
            self.assertEqual(run_main(["blender", p, "--out", Path(tmp) / "p.py"])[0], 1)
            self.assertFalse((Path(tmp) / "p.py").exists())

    def test_lua_string_escapes(self):
        self.assertEqual(sl.lua_str('a"b\\c\n\x01'), '"a\\"b\\\\c\\n\\001"')

    def test_emitted_blender_scripts_compile(self):
        _, tl = sl.validate(DRILL)
        push = sl.blender_push_script(DRILL, tl, "drill.shots.json", "push.py")
        compile(push, "push.py", "exec")
        compile(sl.blender_export_script("export.py"), "export.py", "exec")
        p = push_payload(push)
        self.assertEqual([(s["id"], s["frame"]) for s in p["shots"]], [("S010", 1), ("S020", 31), ("S030", 61)])
        self.assertEqual((p["frame_start"], p["frame_end"], p["sequence"], p["revision"]), (1, 105, "drill", 3))
        self.assertIn('startswith((DATA["prefix"], DATA["cue_prefix"]))', push)
        self.assertEqual((p["prefix"], p["cue_prefix"]), ("shot:", "cue:"))


class DiffTest(unittest.TestCase):
    """C5: Blender export vs shot list."""

    def setUp(self):
        _, self.tl = sl.validate(DRILL)

    def test_exact_fixture_has_no_drift(self):
        res = sl.diff(DRILL, self.tl, load("drill-cues.blender.json"))
        self.assertTrue(res["match"], res["issues"])
        self.assertEqual([r["start_drift_frames"] for r in res["shots"]], [0, 0, 0])
        self.assertEqual([r["drift_frames"] for r in res["cues"]], [0, 0, 0])

    def test_export_without_cue_markers_reports_them_missing(self):
        res = sl.diff(DRILL, self.tl, load("drill.blender.json"))  # an export made before cue markers existed
        self.assertFalse(res["match"])
        self.assertEqual(res["cue_missing"], ["sfx.test.one", "music.test.sting", "amb.test.bed"])
        self.assertEqual(res["write_blockers"], [])  # --write keeps their at

    def test_c5_moved_marker(self):
        res = sl.diff(DRILL, self.tl, load("drill.blender-retimed.json"))
        self.assertFalse(res["match"])
        s020 = res["shots"][1]
        self.assertEqual((s020["start_drift_frames"], s020["length_drift_frames"]), (6, -6))
        self.assertEqual(s020["start_drift_ms"], "200")
        self.assertEqual(res["shots"][0]["length_drift_frames"], 6)
        self.assertEqual(res["write_blockers"], [])

    def test_c5_missing_extra_and_order(self):
        bj = load("drill.blender.json")
        bj["markers"] = [m for m in bj["markers"] if m["name"] != "shot:S020"]
        res = sl.diff(DRILL, self.tl, bj)
        self.assertEqual(res["missing"], ["S020"])
        self.assertIn("missing marker", res["write_blockers"])
        bj = load("drill.blender.json")
        bj["markers"].append({"name": "shot:S999", "frame": 90, "camera": None})
        self.assertEqual(sl.diff(DRILL, self.tl, bj)["extra"], ["S999"])
        bj = load("drill.blender.json")
        bj["markers"][0]["frame"], bj["markers"][1]["frame"] = 31, 1
        res = sl.diff(DRILL, self.tl, bj)
        self.assertFalse(res["order_ok"])
        self.assertIn("marker order", res["write_blockers"])

    def test_c5_fps_mismatch(self):
        bj = load("drill.blender.json")
        bj["fps"] = 24
        res = sl.diff(DRILL, self.tl, bj)
        self.assertFalse(res["rate"]["match"])
        self.assertTrue(any(i.startswith("fps mismatch") for i in res["issues"]))
        bj["fps"], bj["fps_base"] = 60, 2.0  # same rate, other representation
        self.assertTrue(sl.diff(DRILL, self.tl, bj)["rate"]["match"])

    def test_ntsc_float32_fps_base_from_real_blender_export(self):
        d = copy.deepcopy(DRILL)
        d["fps"], d["sequence"] = [30000, 1001], "drill-ntsc"
        d["shots"][0]["frames"] = 1001
        d["cues"] = []  # this real export predates cue markers; the test is about the rate
        _, tl = sl.validate(d)
        bj = load("drill-ntsc.blender.json")
        self.assertNotEqual(bj["fps_base"], 1.001)  # Blender stores fps_base as a 32-bit float
        res = sl.diff(d, tl, bj)
        self.assertTrue(res["rate"]["match"])
        self.assertTrue(res["match"], res["issues"])
        bj["fps_base"] = 1.0
        self.assertFalse(sl.diff(d, tl, bj)["rate"]["match"])

    def test_c5_write_updates_frames_and_revision_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "drill.shots.json"
            p.write_text((FIX / "drill.shots.json").read_text(encoding="utf-8"), encoding="utf-8")
            code, out, err = run_main(["diff", p, FIX / "drill.blender-retimed.json", "--write"])
            self.assertEqual(code, 0, err)
            new = json.loads(p.read_text(encoding="utf-8"))
        want = copy.deepcopy(DRILL)
        want["revision"] = 4
        for s, f in zip(want["shots"], (36, 24, 51)):
            s["frames"] = f
        self.assertEqual(new, want)
        self.assertEqual(list(new), list(DRILL))  # key order kept

    def test_write_refused_on_missing_marker_and_file_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "drill.shots.json"
            original = (FIX / "drill.shots.json").read_text(encoding="utf-8")
            p.write_text(original, encoding="utf-8")
            bj = load("drill.blender-retimed.json")
            bj["markers"].pop()
            b = Path(tmp) / "b.json"
            b.write_text(json.dumps(bj), encoding="utf-8")
            code, _, err = run_main(["diff", p, b, "--write"])
            self.assertEqual(code, 1)
            self.assertIn("missing marker", err)
            self.assertEqual(p.read_text(encoding="utf-8"), original)

    def test_write_refused_when_a_cue_falls_outside_its_new_length(self):
        bj = load("drill.blender.json")
        bj["markers"][1]["frame"] = 5  # S010 becomes 4 frames; cue amb.test.bed at 5 is outside
        res = sl.diff(DRILL, self.tl, bj)
        with self.assertRaisesRegex(sl.ShotlistError, "amb.test.bed"):
            sl.apply_write(DRILL, res)

    def test_write_fills_unknown_lengths_at_plan_stage(self):
        d = plan([30, "UNKNOWN", "UNKNOWN"], stage="plan")
        _, tl = sl.validate(d)
        bj = {"fps": 30, "fps_base": 1.0, "frame_start": 1, "frame_end": 100, "sequence": "t", "revision": 1,
              "markers": [{"name": "shot:S1", "frame": 1}, {"name": "shot:S2", "frame": 31},
                          {"name": "shot:S3", "frame": 61}]}
        new, changed = sl.apply_write(d, sl.diff(d, tl, bj))
        self.assertEqual([s["frames"] for s in new["shots"]], [30, 30, 40])
        self.assertEqual(new["revision"], 2)
        self.assertEqual(len(changed), 2)


class LogDiffTest(unittest.TestCase):
    def setUp(self):
        _, self.tl = sl.validate(DRILL)
        self.log = json.loads((FIX / "drill.log.json").read_text(encoding="utf-8"), parse_float=Fraction,
                              parse_int=Fraction)

    def test_rows_and_lists_without_tolerance(self):
        res = sl.log_diff(DRILL, self.tl, self.log)
        rows = {r["id"]: r for r in res["rows"]}
        self.assertEqual(rows["S020"]["diff_ms"], "50.000")
        self.assertEqual(rows["S020"]["diff_frames"], "1.500")
        self.assertEqual(rows["sfx.test.one"]["diff_ms"], "12.000")
        self.assertEqual(res["not_logged"], ["music.test.sting", "amb.test.bed"])
        self.assertEqual(res["not_planned"], ["debug.extra"])
        self.assertEqual(res["verdict"], "measured")
        self.assertNotIn("verdict", rows["S020"])

    def test_tolerance_needs_source_and_judges(self):
        code, _, err = run_main(["log-diff", FIX / "drill.shots.json", FIX / "drill.log.json", "--tol-ms", "20"])
        self.assertEqual(code, 1)
        self.assertIn("--tol-source", err)
        res = sl.log_diff(DRILL, self.tl, self.log, Fraction(60))
        self.assertEqual({r["id"]: r["verdict"] for r in res["rows"]}["S020"], "pass")
        self.assertEqual(res["verdict"], "fail")  # two planned cues were not logged
        code, out, _ = run_main(["log-diff", FIX / "drill.shots.json", FIX / "drill.log.json", "--tol-ms", "20",
                                 "--tol-source", "test value", "--json"])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(out)["tolerance"], {"ms": "20", "source": "test value"})

    def test_bad_log_entry(self):
        with self.assertRaises(sl.ShotlistError):
            sl.log_diff(DRILL, self.tl, [{"id": "S010", "t": "soon"}])


class FakeMarker:
    def __init__(self, name, frame):
        self.name, self.frame, self.camera = name, frame, None


class FakeMarkers(list):
    def new(self, name, frame):
        m = FakeMarker(name, frame)
        self.append(m)
        return m

    def remove(self, m):
        del self[next(i for i, x in enumerate(self) if x is m)]


class FakeScene(dict):
    """The part of a Blender scene the emitted scripts touch (no Blender needed)."""

    def __init__(self, markers=(), frame_end=250):
        super().__init__()
        self.name = "Scene"
        self.render = types.SimpleNamespace(fps=24, fps_base=1.0)
        self.frame_start, self.frame_end = 1, frame_end
        self.timeline_markers = FakeMarkers()
        for name, frame in markers:
            self.timeline_markers.new(name, frame)


def run_in_fake_blender(script: str, scene: FakeScene, argv=("blender",), objects=None):
    bpy = types.ModuleType("bpy")
    bpy.context = types.SimpleNamespace(scene=scene)
    bpy.data = types.SimpleNamespace(objects=objects or {})
    bpy.app = types.SimpleNamespace(version_string="fake")
    with mock.patch.dict(sys.modules, {"bpy": bpy}), mock.patch.object(sys, "argv", list(argv)), \
            contextlib.redirect_stdout(io.StringIO()):
        exec(compile(script, "emitted.py", "exec"), {"__name__": "__main__"})


def code_lines(script: str) -> str:
    return "\n".join(ln for ln in script.splitlines() if not ln.lstrip().startswith("#"))


FIRST = load("first-cut.shots.json")


class PropsOnlyTest(unittest.TestCase):
    """J015-T10 g1 / C1: --props-only sets rate and the two scene properties, nothing else; UNKNOWN lengths allowed."""

    def test_c1_props_only_script_with_all_lengths_unknown(self):
        _, tl = sl.validate(FIRST)
        self.assertTrue(all(t["frames"] is None for t in tl["shots"]))
        script = sl.blender_props_script(FIRST, "first-cut.shots.json", "props.py")
        compile(script, "props.py", "exec")
        self.assertEqual(set(push_payload(script)), {"sequence", "revision", "fps", "fps_base", "prop_sequence",
                                                     "prop_revision"})
        code = code_lines(script)
        for banned in ("timeline_markers", "frame_start", "frame_end", "camera", "frame_set"):
            self.assertNotIn(banned, code)
        scene = FakeScene(markers=[("shot:keep", 7), ("mine", 3)], frame_end=250)
        run_in_fake_blender(script, scene)
        self.assertEqual((scene.render.fps, scene.render.fps_base), (24, 1.0))
        self.assertEqual((scene["film_sequence"], scene["film_revision"]), ("first-cut", 1))
        self.assertEqual(scene.frame_end, 250)
        self.assertEqual([(m.name, m.frame) for m in scene.timeline_markers], [("shot:keep", 7), ("mine", 3)])

    def test_props_only_keeps_ntsc_rate_exact(self):
        d = plan(["UNKNOWN"], fps=(30000, 1001), stage="plan")
        p = push_payload(sl.blender_props_script(d, "x", "p.py"))
        self.assertEqual(Fraction(p["fps"]) / Fraction(p["fps_base"]), Fraction(30000, 1001))

    def test_cli_props_only_allowed_full_push_still_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "props.py"
            code, text, err = run_main(["blender", FIX / "first-cut.shots.json", "--out", out, "--props-only"])
            self.assertEqual(code, 0, err)
            self.assertIn("--props-only", out.read_text(encoding="utf-8"))
            code, _, err = run_main(["blender", FIX / "first-cut.shots.json", "--out", Path(tmp) / "push.py"])
            self.assertEqual(code, 1)
            self.assertIn("frames UNKNOWN", err)
            self.assertFalse((Path(tmp) / "push.py").exists())


class UnknownPlanDiffTest(unittest.TestCase):
    """J015-T10 g3 / C2: an UNKNOWN plan is never "no drift"; --write shows the range and guards frame_end."""

    def test_c2_all_unknown_never_no_drift(self):
        code, out, _ = run_main(["diff", FIX / "first-cut.shots.json", FIX / "first-cut.blender.json"])
        self.assertEqual(code, 1)
        self.assertNotIn("no drift", out)
        for sid in ("A", "B", "C"):
            self.assertRegex(out, rf"(?m)^  {sid}: .*not compared \(plan UNKNOWN\)$")
        self.assertIn("compared 0 of 3 shots", out.splitlines()[-1])
        res = sl.diff(FIRST, sl.validate(FIRST)[1], load("first-cut.blender.json"))
        self.assertFalse(res["match"])
        self.assertFalse(res["complete"])
        self.assertEqual(res["issues"], [])

    def test_c2_partly_unknown_counts_compared_shots(self):
        d = plan([30, "UNKNOWN", "UNKNOWN"], stage="plan")
        bj = {"fps": 30, "fps_base": 1.0, "frame_start": 1, "frame_end": 100, "sequence": "t", "revision": 1,
              "markers": [{"name": "shot:S1", "frame": 1}, {"name": "shot:S2", "frame": 31},
                          {"name": "shot:S3", "frame": 61}]}
        res = sl.diff(d, sl.validate(d)[1], bj)
        self.assertEqual(res["compared"]["shots"], 1)
        self.assertEqual(res["not_compared"], ["shot S2", "shot S3"])
        self.assertNotIn("no drift", sl.summary_line(res))
        self.assertIn("compared 1 of 3 shots", sl.summary_line(res))
        full = sl.diff(DRILL, sl.validate(DRILL)[1], load("drill-cues.blender.json"))
        self.assertEqual(sl.summary_line(full), "no drift (compared 3 of 3 shots and 3 of 3 cues)")

    def test_c2_write_prints_range_and_last_length_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "first-cut.shots.json"
            p.write_text((FIX / "first-cut.shots.json").read_text(encoding="utf-8"), encoding="utf-8")
            code, out, err = run_main(["diff", p, FIX / "first-cut.blender.json", "--write"])
            self.assertEqual(code, 0, err)
            preview = "--write: Blender frame range 1..96; the last shot C will get 36 frame(s)"
            self.assertIn(preview, out)
            self.assertLess(out.index(preview), out.index("wrote "))
            self.assertEqual([s["frames"] for s in json.loads(p.read_text(encoding="utf-8"))["shots"]], [24, 36, 36])

    def test_c2_write_refused_when_frame_end_before_last_marker(self):
        bj = load("first-cut.blender.json")
        bj["frame_end"] = 50  # before shot:C at 61
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "first-cut.shots.json"
            original = (FIX / "first-cut.shots.json").read_text(encoding="utf-8")
            p.write_text(original, encoding="utf-8")
            b = Path(tmp) / "b.json"
            b.write_text(json.dumps(bj), encoding="utf-8")
            code, out, err = run_main(["diff", p, b, "--write"])
            self.assertEqual(code, 1)
            self.assertIn("frame_end 50 is before the last shot marker (61)", err)
            self.assertIn("--write: Blender frame range 1..50", out)
            self.assertEqual(p.read_text(encoding="utf-8"), original)

    def test_write_refused_when_two_shot_markers_share_a_frame(self):
        bj = load("first-cut.blender.json")
        bj["markers"][2]["frame"] = 1  # shot:B on shot:A's frame
        res = sl.diff(FIRST, sl.validate(FIRST)[1], bj)
        with self.assertRaisesRegex(sl.ShotlistError, "two shot markers on one frame"):
            sl.apply_write(FIRST, res)


class CueMarkerTest(unittest.TestCase):
    """J015-T10 g4 / C3: cue:<id> markers pushed, exported, diffed and written back into `at`."""

    def setUp(self):
        _, self.tl = sl.validate(DRILL)

    def test_c3_push_puts_cue_markers_at_shot_start_plus_at(self):
        p = push_payload(sl.blender_push_script(DRILL, self.tl, "drill.shots.json", "push.py"))
        self.assertEqual([(c["id"], c["frame"]) for c in p["cues"]],
                         [("sfx.test.one", 1), ("music.test.sting", 76), ("amb.test.bed", 6)])  # 1+0, 61+15, 1+5
        d = plan([30, 30], start=101, cues=[cue(shot_id="S2", at=7), cue(cid="ui.x.y", at="UNKNOWN")], stage="plan")
        p = push_payload(sl.blender_push_script(d, sl.validate(d)[1], "x", "p.py"))
        self.assertEqual(p["cues"], [{"id": "sfx.a.b", "frame": 138}])  # 101 + 30 + 7
        self.assertEqual(p["cues_unknown"], ["ui.x.y"])

    def test_c3_push_replaces_only_shot_and_cue_markers(self):
        script = sl.blender_push_script(DRILL, self.tl, "drill.shots.json", "push.py")
        scene = FakeScene(markers=[("cue:old", 9), ("shot:old", 2), ("director note", 40)])
        cam = types.SimpleNamespace(name="CAM_S010", type="CAMERA")
        run_in_fake_blender(script, scene, objects={"CAM_S010": cam})
        got = sorted((m.name, m.frame, m.camera.name if m.camera else None) for m in scene.timeline_markers)
        self.assertEqual(got, sorted([("director note", 40, None), ("shot:S010", 1, "CAM_S010"),
                                      ("shot:S020", 31, None), ("shot:S030", 61, None),
                                      ("cue:sfx.test.one", 1, None), ("cue:music.test.sting", 76, None),
                                      ("cue:amb.test.bed", 6, None)]))
        self.assertEqual((scene.frame_start, scene.frame_end), (1, 105))

    def test_c3_export_includes_cue_markers_and_round_trips(self):
        script = sl.blender_push_script(DRILL, self.tl, "drill.shots.json", "push.py")
        scene = FakeScene(markers=[("director note", 40)])
        run_in_fake_blender(script, scene)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "out.json"
            run_in_fake_blender(sl.blender_export_script("export.py"), scene, argv=("blender", "--", str(out)))
            bj = json.loads(out.read_text(encoding="utf-8"))
        names = [m["name"] for m in bj["markers"]]
        self.assertIn("cue:music.test.sting", names)
        self.assertNotIn("director note", names)
        self.assertEqual([m["frame"] for m in bj["markers"]], sorted(m["frame"] for m in bj["markers"]))
        res = sl.diff(DRILL, self.tl, bj)
        self.assertTrue(res["match"], res["issues"])

    def test_c3_diff_shows_cue_drift_missing_and_extra(self):
        bj = load("drill-cues.blender.json")
        next(m for m in bj["markers"] if m["name"] == "cue:music.test.sting")["frame"] = 78
        bj["markers"] = [m for m in bj["markers"] if m["name"] != "cue:amb.test.bed"]
        bj["markers"].append({"name": "cue:sfx.not.planned", "frame": 40, "camera": None})
        res = sl.diff(DRILL, self.tl, bj)
        rows = {r["id"]: r for r in res["cues"]}
        self.assertEqual((rows["music.test.sting"]["plan_frame"], rows["music.test.sting"]["blender_frame"]), (76, 78))
        self.assertEqual((rows["music.test.sting"]["drift_frames"], rows["music.test.sting"]["drift_ms"]), (2, "200/3"))
        self.assertIn("cue music.test.sting: +2 frames (66.667 ms)", res["issues"])
        self.assertEqual(res["cue_missing"], ["amb.test.bed"])
        self.assertEqual(res["cue_extra"], ["sfx.not.planned"])
        self.assertIn("extra cue marker", res["write_blockers"])
        self.assertFalse(res["match"])

    def test_c3_write_sets_at_keeps_unmarked_cues_and_bumps_revision(self):
        bj = load("drill-cues.blender.json")
        next(m for m in bj["markers"] if m["name"] == "cue:music.test.sting")["frame"] = 78  # S030 starts at 61
        bj["markers"] = [m for m in bj["markers"] if m["name"] != "cue:amb.test.bed"]
        new, changed = sl.apply_write(DRILL, sl.diff(DRILL, self.tl, bj))
        want = copy.deepcopy(DRILL)
        want["revision"] = 4
        want["cues"][1]["at"] = 17
        self.assertEqual(new, want)  # amb.test.bed (no marker) keeps at 5; end of music.test.sting unchanged
        self.assertEqual(changed, ["cue music.test.sting at: 15 -> 17"])

    def test_c3_write_fills_cue_at_on_first_animatic(self):
        new, changed = sl.apply_write(FIRST, sl.diff(FIRST, sl.validate(FIRST)[1], load("first-cut.blender.json")))
        cues = {c["id"]: c for c in new["cues"]}
        self.assertEqual(cues["sfx.first.hit"]["at"], 12)  # marker 37 - shot:B 25
        self.assertEqual(cues["ui.first.prompt"]["at"], "UNKNOWN")  # no marker: unchanged
        self.assertEqual((cues["amb.first.bed"]["at"], cues["amb.first.bed"]["end"]), (0, 40))
        self.assertEqual(new["revision"], 2)
        self.assertEqual({k: v for k, v in new.items() if k not in ("shots", "cues", "revision")},
                         {k: v for k, v in FIRST.items() if k not in ("shots", "cues", "revision")})

    def test_c3_write_refused_on_cue_marker_outside_its_shot(self):
        for frame in (31, 0):  # sfx.test.one belongs to S010 = frames 1..30: one past its end, one before its start
            bj = load("drill-cues.blender.json")
            next(m for m in bj["markers"] if m["name"] == "cue:sfx.test.one")["frame"] = frame
            res = sl.diff(DRILL, self.tl, bj)
            with self.assertRaisesRegex(sl.ShotlistError, r"cue:sfx\.test\.one outside its shot S010"):
                sl.apply_write(DRILL, res)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "drill.shots.json"
            original = (FIX / "drill.shots.json").read_text(encoding="utf-8")
            p.write_text(original, encoding="utf-8")
            b = Path(tmp) / "b.json"
            b.write_text(json.dumps(bj), encoding="utf-8")
            code, _, err = run_main(["diff", p, b, "--write"])
            self.assertEqual(code, 1)
            self.assertIn("outside its shot", err)
            self.assertEqual(p.read_text(encoding="utf-8"), original)

    def test_cue_marker_bound_to_a_camera_is_reported(self):
        bj = load("drill-cues.blender.json")
        bj["markers"][0]["camera"] = "CAM_S020"
        self.assertTrue(any("bound to camera" in i for i in sl.diff(DRILL, self.tl, bj)["issues"]))

    def test_cli_diff_prints_cue_rows(self):
        code, out, _ = run_main(["diff", FIX / "drill.shots.json", FIX / "drill-cues.blender.json"])
        self.assertEqual(code, 0)
        self.assertIn("  cue music.test.sting: plan 76, Blender 76 (at 15) +0 f (0.000 ms)", out)
        self.assertEqual(out.splitlines()[-1], "no drift (compared 3 of 3 shots and 3 of 3 cues)")


@unittest.skipUnless(os.environ.get("BLENDER_EXE"), "set BLENDER_EXE to run the emitted scripts in Blender")
class BlenderRoundTripTest(unittest.TestCase):
    """C7: push, export and diff with no drift (needs Blender; new empty scene, writes only to a temp folder)."""

    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            _, tl = sl.validate(DRILL)
            (t / "push.py").write_text(sl.blender_push_script(DRILL, tl, "drill.shots.json", "push.py"), encoding="utf-8")
            (t / "export.py").write_text(sl.blender_export_script("export.py"), encoding="utf-8")
            proc = subprocess.run([os.environ["BLENDER_EXE"], "-b", "--factory-startup", "--python", str(t / "push.py"),
                                   "--python", str(t / "export.py"), "--", str(t / "out.json")],
                                  capture_output=True, text=True, timeout=300)
            self.assertEqual(proc.returncode, 0, proc.stderr[-2000:])
            bj = json.loads((t / "out.json").read_text(encoding="utf-8"))
        res = sl.diff(DRILL, tl, bj)
        self.assertTrue(res["match"], res["issues"])
        self.assertEqual(len([m for m in bj["markers"] if m["name"].startswith("cue:")]), 3)

    def blender(self, t: Path, *scripts, out: Path):
        args = [os.environ["BLENDER_EXE"], "-b", "--factory-startup"]
        for s in scripts:
            args += ["--python", str(s)]
        proc = subprocess.run(args + ["--", str(out)], capture_output=True, text=True, timeout=300)
        self.assertEqual(proc.returncode, 0, proc.stderr[-2000:])
        return json.loads(out.read_text(encoding="utf-8"))

    def test_first_animatic_props_only_write_then_full_push(self):
        """J015-T10 C5: props-only push, markers authored in the same run, export, diff --write; then full push."""
        author = ("import bpy\n"
                  "s = bpy.context.scene\n"
                  "s.frame_start, s.frame_end = 1, 96\n"
                  "for n, f in (('shot:A', 1), ('shot:B', 25), ('shot:C', 61), ('cue:amb.first.bed', 1),\n"
                  "             ('cue:sfx.first.hit', 37), ('cue:ui.first.prompt', 70)):\n"
                  "    s.timeline_markers.new(n, frame=f)\n")
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            f = t / "first-cut.shots.json"
            f.write_text((FIX / "first-cut.shots.json").read_text(encoding="utf-8"), encoding="utf-8")
            (t / "author.py").write_text(author, encoding="utf-8")
            (t / "export.py").write_text(sl.blender_export_script("export.py"), encoding="utf-8")
            self.assertEqual(run_main(["blender", f, "--out", t / "props.py", "--props-only"])[0], 0)
            self.blender(t, t / "props.py", t / "author.py", t / "export.py", out=t / "out1.json")
            self.assertEqual(run_main(["diff", f, t / "out1.json"])[0], 1)  # UNKNOWN plan: never "no drift"
            code, out, err = run_main(["diff", f, t / "out1.json", "--write"])
            self.assertEqual(code, 0, err)
            new = json.loads(f.read_text(encoding="utf-8"))
            self.assertEqual([s["frames"] for s in new["shots"]], [24, 36, 36])
            self.assertEqual([c["at"] for c in new["cues"]], [0, 12, 9])
            self.assertEqual(run_main(["blender", f, "--out", t / "push.py"])[0], 0)
            bj = self.blender(t, t / "push.py", t / "export.py", out=t / "out2.json")
            code, out, _ = run_main(["diff", f, t / "out2.json"])
            self.assertEqual(code, 0, out)
            self.assertEqual(out.splitlines()[-1], "no drift (compared 3 of 3 shots and 3 of 3 cues)")


if __name__ == "__main__":
    unittest.main()
