"""Offline tests for tools/art/thumb_check.py (synthetic images built in the test, no fixtures)."""

import contextlib
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy and Pillow")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "art"))
import look_check as lc  # noqa: E402
import thumb_check as tc  # noqa: E402

MAGENTA = (255, 0, 255)


def discs_on(w, h, centres, r, colour=(20, 20, 20), bg=MAGENTA) -> np.ndarray:
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:] = bg
    yy, xx = np.mgrid[0:h, 0:w]
    radii = r if isinstance(r, list) else [r] * len(centres)
    for (cx, cy), r in zip(centres, radii):
        img[(xx - cx + 0.5) ** 2 + (yy - cy + 0.5) ** 2 <= r * r] = colour
    return img


def gradient(w, h) -> np.ndarray:
    """No flat border: no subject can be keyed."""
    xx, yy = np.meshgrid(np.linspace(0, 255, w), np.linspace(0, 255, h))
    return np.stack([xx, yy, 255 - xx], axis=-1).astype(np.uint8)


class Cli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def save(self, arr, name="in.png") -> Path:
        p = self.dir / name
        Image.fromarray(arr).save(p)
        return p

    def run_cli(self, args) -> dict:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            tc.main([str(a) for a in args] + ["--out-dir", str(self.dir / "diag")])
        return json.loads(buf.getvalue())


class MasterChecksTest(unittest.TestCase):
    def test_icon_square_and_size(self):
        ok = tc.master_checks("icon", 512, 512, 1000)
        self.assertTrue(ok["checks"]["square"]["meets"] and ok["checks"]["min_512"]["meets"] and ok["all_met"])
        bad = tc.master_checks("icon", 600, 400, 1000)
        self.assertFalse(bad["checks"]["square"]["meets"])
        self.assertFalse(bad["checks"]["min_512"]["meets"])
        self.assertFalse(tc.master_checks("icon", 511, 511, 1)["checks"]["min_512"]["meets"])
        self.assertIn("experience-icons.md:55", ok["checks"]["square"]["source"])

    def test_thumbnail_aspect_stretch_size(self):
        ok = tc.master_checks("thumbnail", 1920, 1080, 100)["checks"]
        self.assertTrue(ok["aspect_16_9"]["meets"] and ok["ideal_1920x1080"]["meets"] and ok["upload_within_1920x1080"]["meets"])
        self.assertAlmostEqual(ok["display_stretch"]["horizontal_scale_vs_vertical"], 1.0)
        four3 = tc.master_checks("thumbnail", 1600, 1200, 100)["checks"]
        self.assertFalse(four3["aspect_16_9"]["meets"])
        self.assertAlmostEqual(four3["display_stretch"]["horizontal_scale_vs_vertical"], 4 / 3)
        self.assertIn("thumbnails.md:220", four3["display_stretch"]["source"])
        big = tc.master_checks("thumbnail", 2560, 1440, 100)["checks"]
        self.assertTrue(big["aspect_16_9"]["meets"])
        self.assertFalse(big["ideal_1920x1080"]["meets"] or big["upload_within_1920x1080"]["meets"])

    def test_3mb(self):
        under = tc.master_checks("thumbnail", 1920, 1080, 2_999_999)["checks"]["upload_under_3mb"]
        self.assertTrue(under["meets_decimal"] and under["meets_binary"])
        mid = tc.master_checks("thumbnail", 1920, 1080, 3_100_000)
        self.assertFalse(mid["checks"]["upload_under_3mb"]["meets_decimal"])
        self.assertTrue(mid["checks"]["upload_under_3mb"]["meets_binary"])
        self.assertFalse(mid["all_met"])
        self.assertFalse(tc.master_checks("thumbnail", 1920, 1080, 3 * 1024 * 1024)["checks"]["upload_under_3mb"]["meets_binary"])


class SmallSizeTest(Cli):
    def test_icon_default_150_with_docs_source(self):
        p = self.save(discs_on(512, 512, [(256, 256)], 150))
        before = lc.sha256(p)
        rec = self.run_cli(["icon", p, "--title", "Test Game"])
        s = rec["measurements"]["small_size"]
        self.assertEqual(s["size_px"], [150, 150])
        self.assertTrue(s["source"].endswith("experience-icons.md:34"))
        self.assertEqual(rec["measurements"]["one_clear_moment"]["small"]["frame_px"], [150, 150])
        with Image.open(rec["images"]["sheet"]) as sheet:
            self.assertGreaterEqual(sheet.width, 3 * 150 + 450)  # master panel at 3x small height + three small panels
        self.assertEqual(lc.sha256(p), before)  # input never overwritten
        self.assertEqual(rec["verdict"], "measured")

    def test_thumbnail_needs_size_and_source(self):
        p = self.save(discs_on(320, 180, [(160, 90)], 40))
        with self.assertRaises(SystemExit):
            self.run_cli(["thumbnail", p])
        with self.assertRaises(SystemExit):
            self.run_cli(["thumbnail", p, "--size", "160x90"])
        rec = self.run_cli(["thumbnail", p, "--size", "160x90", "--size-source", "test tile"])
        self.assertEqual(rec["measurements"]["small_size"]["size_px"], [160, 90])
        self.assertEqual(rec["measurements"]["small_size"]["source"], "test tile")

    def test_thumbnail_is_stretched_to_tile(self):
        p = self.save(discs_on(400, 300, [(200, 150)], 60))  # 4:3 master, round disc
        rec = self.run_cli(["thumbnail", p, "--size", "160x90", "--size-source", "test tile"])
        b = rec["measurements"]["contrast"]["small"]  # whole-image covers every tile pixel: no padding
        self.assertEqual(b["whole"]["n_px"], 160 * 90)
        comp = rec["measurements"]["one_clear_moment"]["small"]["components"][0]["bbox_px"]
        self.assertGreater(comp["w"] / comp["h"], 1.25)  # disc widened by the 16:9 stretch (4/3)


class SheetNameTest(Cli):  # J018: another run never overwrites a sheet
    def test_runs_with_other_parameters_keep_their_sheets(self):
        p = self.save(discs_on(512, 512, [(256, 256)], 150))
        a = self.run_cli(["icon", p, "--title", "One"])["images"]["sheet"]
        b = self.run_cli(["icon", p, "--title", "Two"])["images"]["sheet"]
        again = self.run_cli(["icon", p, "--title", "One"])["images"]["sheet"]
        self.assertNotEqual(a, b)
        self.assertEqual(a, again)
        self.assertTrue(Path(a).exists() and Path(b).exists())


class MomentTest(Cli):
    def test_one_vs_three_subjects(self):
        one = self.run_cli(["icon", self.save(discs_on(512, 512, [(256, 256)], 150), "one.png")])
        three = self.run_cli(["icon", self.save(discs_on(512, 512, [(110, 256), (256, 256), (402, 256)], 60), "three.png")])
        for rec, n in ((one, 1), (three, 3)):
            for at in ("master", "small"):
                m = rec["measurements"]["one_clear_moment"][at]
                self.assertEqual(m["component_count"], n, (at, m))
        self.assertAlmostEqual(one["measurements"]["one_clear_moment"]["small"]["largest_share_of_subject"], 1.0, delta=0.01)
        self.assertAlmostEqual(three["measurements"]["one_clear_moment"]["small"]["largest_share_of_subject"], 1 / 3, delta=0.05)
        self.assertIsNone(one["measurements"]["one_clear_moment"]["small"]["second_to_largest_area_ratio"])
        self.assertAlmostEqual(three["measurements"]["one_clear_moment"]["master"]["second_to_largest_area_ratio"], 1.0, delta=0.02)

    def test_dominant_subject_share(self):
        rec = self.run_cli(["icon", self.save(discs_on(512, 512, [(200, 256), (440, 256)], [150, 40]), "two.png")])
        m = rec["measurements"]["one_clear_moment"]["master"]
        self.assertEqual(m["component_count"], 2)
        want = 150**2 / (150**2 + 40**2)
        self.assertAlmostEqual(m["largest_share_of_subject"], want, delta=0.01)
        self.assertAlmostEqual(m["second_to_largest_area_ratio"], (40 / 150) ** 2, delta=0.01)

    def test_no_subject_not_measured(self):
        rec = self.run_cli(["icon", self.save(gradient(512, 512))])
        for at in ("master", "small"):
            m = rec["measurements"]["one_clear_moment"][at]
            self.assertEqual(m["status"], "not measured")
            self.assertIn("no subject mask", m["reason"])
            c = rec["measurements"]["contrast"][at]
            self.assertIsNone(c["subject_ring_ratio"])
            self.assertEqual(c["subject_status"]["status"], "not measured")
            self.assertGreater(c["whole_p95_p5_ratio"], 1.0)  # whole-image spread still reported
        self.assertEqual(rec["verdict"], "measured")

    def test_bottom_band_needs_caller_percent(self):
        arr = discs_on(320, 180, [(160, 160)], 15)  # subject sits at the bottom
        p = self.save(arr)
        rec = self.run_cli(["thumbnail", p, "--size", "160x90", "--size-source", "t"])
        self.assertNotIn("bottom_band", rec["measurements"])  # no default band
        rec = self.run_cli(["thumbnail", p, "--size", "160x90", "--size-source", "t", "--bottom-band", "20"])
        bb = rec["measurements"]["bottom_band"]
        self.assertEqual(bb["band_rows_px"], 36)
        self.assertGreater(bb["subject_share_in_band"], 0.75)
        self.assertTrue(bb["source"].endswith("thumbnails.md:215"))


class VerdictTest(Cli):
    def test_tolerance_without_source_refused(self):
        p = self.save(discs_on(512, 512, [(256, 256)], 150))
        for flags in (["--min-ratio", "3"], ["--max-components", "1"]):
            with self.assertRaises(SystemExit):
                self.run_cli(["icon", p, *flags])
        with self.assertRaises(SystemExit):
            self.run_cli(["thumbnail", p, "--size", "160x90", "--size-source", "t", "--max-bottom-share", "0.1",
                          "--tolerance-source", "x"])  # no --bottom-band

    def test_pass_and_fail_with_source(self):
        p = self.save(discs_on(512, 512, [(256, 256)], 150, colour=(10, 10, 10), bg=(240, 240, 240)))
        ok = self.run_cli(["icon", p, "--min-ratio", "3", "--max-components", "1", "--tolerance-source", "J012 test"])
        self.assertEqual(ok["verdict"], "pass")
        self.assertEqual(ok["rule"]["source"], "J012 test")
        bad = self.run_cli(["icon", p, "--min-ratio", "100", "--tolerance-source", "J012 test"])
        self.assertEqual(bad["verdict"], "fail")
        three = self.save(discs_on(512, 512, [(110, 256), (256, 256), (402, 256)], 60), "three.png")
        self.assertEqual(self.run_cli(["icon", three, "--max-components", "1", "--tolerance-source", "s"])["verdict"], "fail")

    def test_tolerance_without_subject_is_not_measured(self):
        rec = self.run_cli(["icon", self.save(gradient(512, 512)), "--min-ratio", "3", "--tolerance-source", "s"])
        self.assertEqual(rec["verdict"], "not-measured")
        self.assertIn("no subject mask", rec["not_measured_reason"])


class SourcesTest(unittest.TestCase):
    """C4 guard: every cited docs line still states the number the code uses."""

    EXPECT = {
        "icon_square_min_512": ["square", "512×512"],
        "icon_small_150": ["150×150"],
        "thumb_16_9_ideal_1920x1080": ["16:9", "1920×1080"],
        "thumb_upload_3mb_1920x1080": ["3 MB", "1920×1080"],
        "thumb_bottom_metadata": ["bottom", "metadata"],
        "thumb_stretched_16_9": ["stretched to 16:9"],
    }

    def test_cited_lines(self):
        self.assertEqual(set(self.EXPECT), set(tc.SRC))
        for key, words in self.EXPECT.items():
            path, line = tc.SRC[key].rsplit(":", 1)
            f = ROOT / path
            if not f.exists():
                self.skipTest(f"docs mirror missing: {f}")
            text = f.read_text(encoding="utf-8").splitlines()[int(line) - 1]
            for w in words:
                self.assertIn(w, text, (key, tc.SRC[key]))

    def test_no_reimplemented_maths(self):
        src = (ROOT / "tools" / "art" / "thumb_check.py").read_text(encoding="utf-8")
        for pat in (r"0\.04045", r"0\.2126", r"def kmeans", r"def relative_luminance", r"12\.92"):
            self.assertIsNone(re.search(pat, src), pat)


if __name__ == "__main__":
    unittest.main()
