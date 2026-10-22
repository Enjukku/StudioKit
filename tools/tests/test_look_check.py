"""Offline tests for tools/art/look_check.py (synthetic images built in the test, no fixtures)."""

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy and Pillow")

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "art"))
import look_check as lc  # noqa: E402

MAGENTA = (255, 0, 255)

# Sharma, Wu & Dalal (2005), Table 1: all 34 pairs (L1, a1, b1, L2, a2, b2, dE00).
SHARMA = [
    (50.0000, 2.6772, -79.7751, 50.0000, 0.0000, -82.7485, 2.0425),
    (50.0000, 3.1571, -77.2803, 50.0000, 0.0000, -82.7485, 2.8615),
    (50.0000, 2.8361, -74.0200, 50.0000, 0.0000, -82.7485, 3.4412),
    (50.0000, -1.3802, -84.2814, 50.0000, 0.0000, -82.7485, 1.0000),
    (50.0000, -1.1848, -84.8006, 50.0000, 0.0000, -82.7485, 1.0000),
    (50.0000, -0.9009, -85.5211, 50.0000, 0.0000, -82.7485, 1.0000),
    (50.0000, 0.0000, 0.0000, 50.0000, -1.0000, 2.0000, 2.3669),
    (50.0000, -1.0000, 2.0000, 50.0000, 0.0000, 0.0000, 2.3669),
    (50.0000, 2.4900, -0.0010, 50.0000, -2.4900, 0.0009, 7.1792),
    (50.0000, 2.4900, -0.0010, 50.0000, -2.4900, 0.0010, 7.1792),
    (50.0000, 2.4900, -0.0010, 50.0000, -2.4900, 0.0011, 7.2195),
    (50.0000, 2.4900, -0.0010, 50.0000, -2.4900, 0.0012, 7.2195),
    (50.0000, -0.0010, 2.4900, 50.0000, 0.0009, -2.4900, 4.8045),
    (50.0000, -0.0010, 2.4900, 50.0000, 0.0010, -2.4900, 4.8045),
    (50.0000, -0.0010, 2.4900, 50.0000, 0.0011, -2.4900, 4.7461),
    (50.0000, 2.5000, 0.0000, 50.0000, 0.0000, -2.5000, 4.3065),
    (50.0000, 2.5000, 0.0000, 73.0000, 25.0000, -18.0000, 27.1492),
    (50.0000, 2.5000, 0.0000, 61.0000, -5.0000, 29.0000, 22.8977),
    (50.0000, 2.5000, 0.0000, 56.0000, -27.0000, -3.0000, 31.9030),
    (50.0000, 2.5000, 0.0000, 58.0000, 24.0000, 15.0000, 19.4535),
    (50.0000, 2.5000, 0.0000, 50.0000, 3.1736, 0.5854, 1.0000),
    (50.0000, 2.5000, 0.0000, 50.0000, 3.2972, 0.0000, 1.0000),
    (50.0000, 2.5000, 0.0000, 50.0000, 1.8634, 0.5757, 1.0000),
    (50.0000, 2.5000, 0.0000, 50.0000, 3.2592, 0.3350, 1.0000),
    (60.2574, -34.0099, 36.2677, 60.4626, -34.1751, 39.4387, 1.2644),
    (63.0109, -31.0961, -5.8663, 62.8187, -29.7946, -4.0864, 1.2630),
    (61.2901, 3.7196, -5.3901, 61.4292, 2.2480, -4.9620, 1.8731),
    (35.0831, -44.1164, 3.7933, 35.0232, -40.0716, 1.5901, 1.8645),
    (22.7233, 20.0904, -46.6940, 23.0331, 14.9730, -42.5619, 2.0373),
    (36.4612, 47.8580, 18.3852, 36.2715, 50.5065, 21.2231, 1.4146),
    (90.8027, -2.0831, 1.4410, 91.1528, -1.6435, 0.0447, 1.4441),
    (90.9257, -0.5406, -0.9208, 88.6381, -0.8985, -0.7239, 1.5381),
    (6.7747, -0.2908, -2.4247, 5.8714, -0.0985, -2.2286, 0.6377),
    (2.0776, 0.0795, -1.1350, 0.9033, -0.0636, -0.5514, 0.9082),
]


def circle_on_magenta(w=200, h=160, cx=100, cy=80, r=50, colour=(40, 120, 200)) -> np.ndarray:
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:] = MAGENTA
    yy, xx = np.mgrid[0:h, 0:w]
    img[(xx - cx + 0.5) ** 2 + (yy - cy + 0.5) ** 2 <= r * r] = colour
    return img


def disc(h, w, cx, cy, r) -> np.ndarray:
    yy, xx = np.mgrid[0:h, 0:w]
    return (xx - cx + 0.5) ** 2 + (yy - cy + 0.5) ** 2 <= r * r


def run_cli(args) -> dict:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        lc.main([str(a) for a in args])
    return json.loads(buf.getvalue())


class LuminanceTest(unittest.TestCase):  # C1
    def test_reference_values(self):
        self.assertEqual(float(lc.relative_luminance(np.array([255, 255, 255]))), 1.0)
        self.assertEqual(float(lc.relative_luminance(np.array([0, 0, 0]))), 0.0)
        self.assertAlmostEqual(float(lc.relative_luminance(np.array([128, 128, 128]))), 0.2158605, delta=1e-6)

    def test_ratios_not_rounded(self):
        self.assertAlmostEqual(lc.contrast_ratio(1.0, 0.0), 21.0, places=12)
        r = lc.contrast_ratio(1.0, float(lc.relative_luminance(np.array(lc.hex_to_rgb("#777777")))))
        self.assertTrue(4.47 < r < 4.5, r)
        rec = run_cli(["contrast", "--pair", "777777,ffffff", "--rule", "wcag-text"])
        self.assertEqual(rec["verdict"], "fail")
        self.assertEqual(rec["rule"]["name"], "wcag-text")
        self.assertLess(rec["measurements"]["pairs"][0]["ratio"], 4.5)
        self.assertIn("UI text", rec["scope"])
        self.assertEqual(run_cli(["contrast", "--pair", "000000,ffffff", "--rule", "xbox-hc"])["verdict"], "pass")


class Ciede2000Test(unittest.TestCase):  # C2
    def test_sharma_pairs(self):
        d = np.array(SHARMA)
        got = lc.ciede2000(d[:, 0:3], d[:, 3:6])
        for i, (g, want) in enumerate(zip(got, d[:, 6])):
            self.assertAlmostEqual(float(g), want, delta=1e-4, msg=f"pair {i + 1}")
        swapped = lc.ciede2000(d[:, 3:6], d[:, 0:3])
        np.testing.assert_allclose(swapped, got, atol=1e-9)


class LabTest(unittest.TestCase):  # C3
    def test_white_and_red(self):
        white = lc.srgb_to_lab(np.array([255, 255, 255]))
        np.testing.assert_allclose(white, [100, 0, 0], atol=0.05)
        red = lc.srgb_to_lab(np.array([255, 0, 0]))
        np.testing.assert_allclose(red, [53.24, 80.09, 67.20], atol=0.05)
        np.testing.assert_allclose(lc.lab_to_srgb(red), [255, 0, 0], atol=0.01)


class SilhouetteTest(unittest.TestCase):  # C4
    def test_circle_bbox_and_area(self):
        img = Image.fromarray(circle_on_magenta())
        mask, src, info = lc.subject_mask(img)
        self.assertEqual((src, info["estimated_key"]), ("key-auto", "#FF00FF"))
        s = lc.silhouette_stats(mask)
        b = s["bbox_px"]
        for got, want in ((b["x0"], 50), (b["y0"], 30), (b["x1"], 150), (b["y1"], 130)):
            self.assertLessEqual(abs(got - want), 1)
        self.assertAlmostEqual(s["area_px"] / (np.pi * 50 * 50), 1.0, delta=0.01)

    def test_alpha_mask(self):
        rgba = np.zeros((40, 60, 4), dtype=np.uint8)
        rgba[10:30, 5:25] = (200, 10, 10, 255)
        mask, src, _ = lc.subject_mask(Image.fromarray(rgba, "RGBA"))
        self.assertEqual(src, "alpha")
        self.assertEqual(lc.bbox(mask), (5, 10, 25, 30))

    def test_iou(self):
        a = disc(160, 200, 100, 80, 40)
        self.assertEqual(lc.aligned_iou(a, a)[0], 1.0)
        big = disc(300, 400, 150, 160, 80)
        iou, align = lc.aligned_iou(a, big)
        self.assertGreaterEqual(iou, 0.98)
        self.assertAlmostEqual(align["scale_a"], 2.0, places=6)
        square = np.zeros((160, 200), dtype=bool)
        square[40:120, 60:140] = True
        self.assertAlmostEqual(lc.aligned_iou(a, square)[0], np.pi / 4, delta=0.02)

    def test_cli_compare_and_tolerance(self):
        with tempfile.TemporaryDirectory() as d:
            p, q = Path(d) / "a.png", Path(d) / "b.png"
            Image.fromarray(circle_on_magenta()).save(p)
            Image.fromarray(circle_on_magenta(400, 320, 200, 160, 100)).save(q)
            rec = run_cli(["silhouette", p, "--compare", q])
            self.assertGreaterEqual(rec["measurements"]["compare"]["iou"], 0.98)
            self.assertEqual(rec["verdict"], "measured")
            self.assertTrue(Path(rec["images"]["silhouette"]).exists())
            rec2 = run_cli(["silhouette", p, "--compare-mask", rec["images"]["silhouette"], "--min-iou", "0.9", "--tolerance-source", "test"])
            self.assertEqual(rec2["verdict"], "pass")
            self.assertEqual(rec2["rule"]["source"], "test")
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                lc.main(["silhouette", str(p), "--compare", str(q), "--min-iou", "0.9"])


class PaletteTest(unittest.TestCase):  # C5
    COLOURS = [(200, 30, 30), (30, 160, 60), (40, 60, 210)]

    def image(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        img[:50] = self.COLOURS[0]
        img[50:80] = self.COLOURS[1]
        img[80:] = self.COLOURS[2]
        return img

    def test_three_flat_colours(self):
        img = self.image()
        roles = {"danger": "#C81E1E", "ally": "#1EA03C"}
        out = lc.palette_stats(img, None, 3, 7, roles)
        self.assertEqual(len(out["clusters"]), 3)
        for c, share, want in zip(out["clusters"], (0.5, 0.3, 0.2), self.COLOURS):
            de = float(lc.ciede2000(np.array(c["lab"]), lc.srgb_to_lab(np.array(want, dtype=float))))
            self.assertLess(de, 1.0)
            self.assertAlmostEqual(c["share"], share, delta=0.01)
        self.assertLess(out["roles"]["danger"]["delta_e2000"], 1.0)
        self.assertEqual(lc.palette_stats(img, None, 3, 7), lc.palette_stats(img, None, 3, 7))

    def test_kmeans_with_noise_is_seeded(self):
        rng = np.random.default_rng(1)
        img = np.clip(self.image().astype(int) + rng.integers(-6, 7, (100, 100, 3)), 0, 255).astype(np.uint8)
        a, b = lc.palette_stats(img, None, 3, 42), lc.palette_stats(img, None, 3, 42)
        self.assertEqual(a, b)
        shares = sorted(c["share"] for c in a["clusters"])
        np.testing.assert_allclose(shares, [0.2, 0.3, 0.5], atol=0.01)


class AutoKeyTest(unittest.TestCase):  # push 1: flat light-grey background and invalid masks
    def grey_subject(self):
        rng = np.random.default_rng(3)
        img = np.clip(211 + rng.integers(-4, 5, (160, 200, 3)), 0, 255).astype(np.uint8)  # #D3D3D3 + mild noise
        img[disc(160, 200, 100, 80, 50)] = (90, 60, 40)
        return img

    def test_light_grey_keys_with_auto(self):
        mask, src, info = lc.subject_mask(Image.fromarray(self.grey_subject()))
        self.assertEqual(src, "key-auto")
        self.assertTrue(info["flat"])
        self.assertGreater(info["border_share_within_tol"], 0.99)
        de = float(lc.ciede2000(lc.srgb_to_lab(np.array(lc.hex_to_rgb(info["estimated_key"]))), lc.srgb_to_lab(np.array([211, 211, 211]))))
        self.assertLess(de, 1.0)
        self.assertAlmostEqual(mask.sum() / (np.pi * 50 * 50), 1.0, delta=0.01)
        self.assertIsNone(lc.mask_problem(mask, src))

    def test_cli_light_grey_and_no_flat_border(self):
        with tempfile.TemporaryDirectory() as d:
            g, n = Path(d) / "grey.png", Path(d) / "noise.png"
            Image.fromarray(self.grey_subject()).save(g)
            rng = np.random.default_rng(5)
            Image.fromarray(rng.integers(0, 256, (120, 160, 3)).astype(np.uint8)).save(n)
            rec = run_cli(["silhouette", g])
            self.assertEqual((rec["verdict"], rec["params"]["mask_source"]), ("measured", "key-auto"))
            self.assertAlmostEqual(rec["measurements"]["area_frac"], np.pi * 2500 / 32000, delta=0.003)
            for check in ("silhouette", "value"):
                r = run_cli([check, n, "--min-ratio" if check == "value" else "--min-iou", "1", "--tolerance-source", "t"])
                self.assertEqual(r["verdict"], "invalid-mask", check)
                self.assertIn("no subject mask", r["invalid_reason"])
                self.assertNotIn("rule", r)
            self.assertIsNone(run_cli(["value", n])["measurements"]["subject"])
            self.assertEqual(run_cli(["thumb", n, "--size", "40x40"])["verdict"], "invalid-mask")
            self.assertEqual(run_cli(["palette", n])["verdict"], "measured")  # no mask: whole-image palette

    def test_full_and_empty_masks_invalid(self):
        full = np.ones((100, 100), dtype=bool)
        self.assertIn(">= 0.98", lc.mask_problem(full, "mask-image"))
        tiny = np.zeros((100, 100), dtype=bool)
        tiny[0, 0] = True
        self.assertIn("< 0.001", lc.mask_problem(tiny, "key-auto"))
        with tempfile.TemporaryDirectory() as d:
            p, m = Path(d) / "a.png", Path(d) / "m.png"
            Image.fromarray(self.grey_subject()).save(p)
            Image.fromarray(np.zeros((160, 200), dtype=np.uint8)).save(m)  # all-black mask = whole image
            for check in ("silhouette", "palette", "value"):
                self.assertEqual(run_cli([check, p, "--mask", m])["verdict"], "invalid-mask", check)


class NearKeyTest(unittest.TestCase):  # J018: a lit head on a flat grey render backdrop is cut by --key-tol 40
    def render(self):
        img = np.full((160, 200, 3), 128, dtype=np.uint8)  # flat render backdrop, one exact grey
        img[100:150, 80:120] = (40, 40, 60)                 # dark body
        img[60:100, 85:115] = (150, 145, 140)               # lit head, 22 levels from the backdrop
        return img

    def test_warns_and_suggests_a_tight_tolerance(self):
        mask, src, info = lc.subject_mask(Image.fromarray(self.render()))
        self.assertEqual(src, "key-auto")
        self.assertFalse(mask[80, 100])                     # the head is cut at the default tolerance
        self.assertIn("near_key_warning", info)
        self.assertLessEqual(info["suggested_key_tol"], 6)
        tight, _, info2 = lc.subject_mask(Image.fromarray(self.render()), key_tol=info["suggested_key_tol"])
        self.assertTrue(tight[80, 100])                     # the suggested tolerance keeps it
        self.assertNotIn("near_key_warning", info2)

    def test_no_warning_on_a_clear_subject(self):
        img = np.full((160, 200, 3), 128, dtype=np.uint8)
        img[60:150, 80:120] = (40, 40, 60)
        _, _, info = lc.subject_mask(Image.fromarray(img))
        self.assertNotIn("near_key_warning", info)


class InvertedMaskTest(unittest.TestCase):  # J018: a white-subject-on-black mask image
    def test_inverted_mask_warns(self):
        img = Image.fromarray(np.full((120, 160, 3), 200, dtype=np.uint8))
        good = np.full((120, 160), 255, dtype=np.uint8)
        good[40:80, 60:100] = 0                              # dark = subject (the expected format)
        _, src, info = lc.subject_mask(img, mask_img=Image.fromarray(good))
        self.assertEqual(src, "mask-image")
        self.assertNotIn("mask_warning", info)
        _, _, info2 = lc.subject_mask(img, mask_img=Image.fromarray(255 - good))
        self.assertIn("mask_warning", info2)


class BrighterSideTest(unittest.TestCase):  # J018: the symmetric ratio now names the brighter side
    def test_brighter_side(self):
        m = np.zeros((60, 60), dtype=bool)
        m[20:40, 20:40] = True
        dark_on_light = np.full((60, 60, 3), 230, dtype=np.uint8)
        dark_on_light[m] = 30
        light_on_dark = 255 - dark_on_light
        a = lc.value_stats(dark_on_light, m, 6)
        b = lc.value_stats(light_on_dark, m, 6)
        self.assertEqual(a["brighter_side"], "ring")
        self.assertEqual(b["brighter_side"], "subject")


class ShadowOnKeyTest(unittest.TestCase):  # J018: a cast shadow on the key is counted as subject
    def test_shadow_warns(self):
        img = np.full((160, 200, 3), (200, 190, 170), dtype=np.uint8)   # warm flat backdrop
        img[40:110, 80:120] = (40, 90, 160)                            # blue subject
        img[110:140, 70:150] = (100, 95, 85)                           # its shadow: the backdrop, half as bright
        _, src, info = lc.subject_mask(Image.fromarray(img))
        self.assertEqual(src, "key-auto")
        self.assertIn("shadow_warning", info)

    def test_no_shadow_no_warning(self):
        img = np.full((160, 200, 3), (200, 190, 170), dtype=np.uint8)
        img[40:140, 80:120] = (40, 90, 160)
        _, _, info = lc.subject_mask(Image.fromarray(img))
        self.assertNotIn("shadow_warning", info)


class ReservedAndHueSpreadTest(unittest.TestCase):  # J018 G3-P8: the two colour checks as look_check modes
    def run_mode(self, args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            lc.main([str(x) for x in args])
        return json.loads(buf.getvalue())

    def test_reserved_finds_a_small_accent_a_palette_merges(self):
        with tempfile.TemporaryDirectory() as d:
            img = np.full((100, 200, 3), (120, 90, 60), dtype=np.uint8)
            img[10:13, 10:15] = (220, 30, 30)                    # a 15 px reserved red accent (0.075 %)
            p = Path(d) / "env.png"
            Image.fromarray(img).save(p)
            r = self.run_mode(["reserved", p, "--swatch", "#DC1E1E", "--max-de", "10", "--out-dir", d])
            self.assertEqual(r["measurements"]["px"], 15)
            ex = np.full((100, 200), 255, dtype=np.uint8)
            ex[10:13, 10:15] = 0                                 # the accent is a gameplay object: excluded
            Image.fromarray(ex).save(Path(d) / "ex.png")
            r2 = self.run_mode(["reserved", p, "--swatch", "#DC1E1E", "--max-de", "10", "--exclude", Path(d) / "ex.png",
                                "--out-dir", d])
            self.assertEqual(r2["measurements"]["px"], 0)

    def test_hue_spread_one_hue_low_hue_patches_high(self):
        with tempfile.TemporaryDirectory() as d:
            rng = np.random.default_rng(1)
            base = np.array([180, 90, 50], dtype=np.float64)
            one = np.clip(base * rng.uniform(0.6, 1.0, (80, 80, 1)), 0, 255).astype(np.uint8)  # value texture, one hue
            patch = one.copy()
            patch[::8, :] = (80, 140, 60)
            patch[4::8, :] = (60, 90, 170)                                                    # hue changes
            for name, arr in (("one.png", one), ("patch.png", patch)):
                Image.fromarray(arr).save(Path(d) / name)
            a = self.run_mode(["hue-spread", Path(d) / "one.png", "--box", "0,0,80,80"])["measurements"]
            b = self.run_mode(["hue-spread", Path(d) / "patch.png", "--box", "0,0,80,80"])["measurements"]
            self.assertTrue(a["valid"])
            self.assertLess(a["hue_sd_deg"], 3)
            self.assertGreater(b["hue_sd_deg"], 10)

    def test_extremes_see_a_small_patch_p5_misses(self):
        with tempfile.TemporaryDirectory() as d:
            img = np.full((200, 300, 3), 70, dtype=np.uint8)
            img[50:80, 50:80] = 0                                  # a 30x30 pure-black patch
            img[150:160, 200:220] = 255                            # a white accent, excluded below
            p = Path(d) / "env.png"
            Image.fromarray(img).save(p)
            ex = np.full((200, 300), 255, dtype=np.uint8)
            ex[150:160, 200:220] = 0
            Image.fromarray(ex).save(Path(d) / "ex.png")
            m = self.run_mode(["extremes", p, "--box", "0,0,300,200", "--exclude", Path(d) / "ex.png", "--out-dir", d])["measurements"]
            self.assertEqual(m["near_black_px"], 900)
            self.assertEqual(m["clipped_px"], 0)

    def model(self, d):
        img = np.full((720, 1600, 3), 200, dtype=np.uint8)
        img[300:500, 760:840] = (40, 40, 40)                       # dark lower body
        img[220:300, 770:830] = (200, 60, 60)                      # red torso (the focal colour)
        img[200:220, 790:810] = (240, 230, 220)                    # bright head
        img[300:320, 765:835] = (20, 10, 5)                         # near-black tinted boots line
        mask = np.full((720, 1600), 255, dtype=np.uint8)
        mask[200:500, 760:840] = 0
        Image.fromarray(img).save(Path(d) / "m.png")
        Image.fromarray(mask).save(Path(d) / "k.png")
        return Path(d) / "m.png", Path(d) / "k.png"

    def test_peaks_chroma_marks_the_torso_not_the_dark_boots(self):
        with tempfile.TemporaryDirectory() as d:
            img, k = self.model(d)
            m = self.run_mode(["peaks", img, "--mask", k, "--channel", "chroma", "--out-dir", d])["measurements"]
            bb = m["marked_bbox_px"]
            self.assertGreaterEqual(bb["y0"], 220)
            self.assertLessEqual(bb["y1"], 300)

    def test_detail_is_measured_at_phone_size(self):
        with tempfile.TemporaryDirectory() as d:
            img, k = self.model(d)
            r = self.run_mode(["detail", img, "--mask", k, "--phone-height", "360", "--out-dir", d])
            self.assertEqual(r["measurements"]["model_px_at_phone"], [40, 150])
            self.assertTrue(Path(r["images"]["cells"]).exists())

    def test_mask_box_cuts_the_mask_to_a_region(self):
        with tempfile.TemporaryDirectory() as d:
            img, k = self.model(d)
            r = self.run_mode(["value", img, "--mask", k, "--mask-box", "700,300,900,500", "--out-dir", d])
            self.assertEqual(r["params"]["key_estimate"]["mask_box"], [700, 300, 900, 500])

    def test_hue_spread_grey_is_not_measured(self):
        with tempfile.TemporaryDirectory() as d:
            Image.fromarray(np.full((40, 40, 3), 128, dtype=np.uint8)).save(Path(d) / "g.png")
            r = self.run_mode(["hue-spread", Path(d) / "g.png", "--box", "0,0,40,40"])
            self.assertEqual(r["verdict"], "not-measured")


class HolesAndComponentsTest(unittest.TestCase):  # push 2: hole fill, components, --component
    GREY = (211, 211, 211)

    def ring_image(self):
        img = np.zeros((120, 120, 3), dtype=np.uint8)
        img[:] = self.GREY
        img[20:100, 20:100] = (60, 40, 30)  # 80x80 dark square
        img[40:80, 40:80] = self.GREY  # 40x40 key-coloured interior, not touching the border
        return img

    def test_ring_hole_filled_or_kept(self):
        img = Image.fromarray(self.ring_image())
        mask, src, info = lc.subject_mask(img)
        self.assertEqual((src, int(mask.sum())), ("key-auto", 80 * 80))
        self.assertEqual((info["hole_fill"], info["filled_holes"], info["filled_area_px"]), (True, 1, 40 * 40))
        mask, _, info = lc.subject_mask(img, fill_holes=False)
        self.assertEqual(int(mask.sum()), 80 * 80 - 40 * 40)
        self.assertEqual((info["hole_fill"], info["filled_holes"]), (False, 0))

    def test_cli_keep_holes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ring.png"
            Image.fromarray(self.ring_image()).save(p)
            a = run_cli(["silhouette", p])
            b = run_cli(["silhouette", p, "--keep-holes"])
            self.assertEqual(a["measurements"]["area_px"], 6400)
            self.assertEqual(b["measurements"]["area_px"], 4800)
            self.assertEqual((a["params"]["hole_fill"], b["params"]["hole_fill"]), (True, False))
            self.assertEqual(a["params"]["key_estimate"]["filled_area_px"], 1600)

    def sheet(self):
        img = np.zeros((200, 300, 3), dtype=np.uint8)
        img[:] = self.GREY
        img[20:60, 200:260] = (200, 30, 30)  # top right: 60x40
        img[30:90, 30:70] = (30, 160, 60)  # top left: 40x60
        img[130:180, 100:180] = (40, 60, 210)  # bottom row: 80x50
        return img

    def test_three_components(self):
        mask, src, _ = lc.subject_mask(Image.fromarray(self.sheet()))
        comps = lc.components(mask)
        self.assertEqual(len(comps), 3)
        got = [(c["n"], c["bbox_px"]["x0"], c["bbox_px"]["y0"], c["bbox_px"]["x1"], c["bbox_px"]["y1"], c["area_px"]) for c in comps]
        self.assertEqual(got, [(1, 30, 30, 70, 90, 2400), (2, 200, 20, 260, 60, 2400), (3, 100, 130, 180, 180, 4000)])

    def test_label_matches_four_and_eight_connectivity(self):
        m = np.zeros((5, 5), dtype=bool)
        m[1, 1] = m[2, 2] = m[3, 3] = True
        self.assertEqual(lc.label(m, eight=False)[1], 3)
        self.assertEqual(lc.label(m, eight=True)[1], 1)

    def test_cli_component(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "sheet.png"
            Image.fromarray(self.sheet()).save(p)
            full = run_cli(["silhouette", p])
            self.assertEqual(full["measurements"]["component_count"], 3)
            r = run_cli(["silhouette", p, "--component", "2"])
            self.assertEqual(r["verdict"], "measured")
            self.assertEqual(r["measurements"]["area_px"], 2400)
            self.assertEqual((r["measurements"]["bbox_px"]["w"], r["measurements"]["bbox_px"]["h"]), (60, 40))
            self.assertEqual(r["params"]["key_estimate"]["component"]["n"], 2)
            self.assertEqual(r["input"]["size_px"], [300, 200])
            self.assertIn("c2.", Path(r["images"]["silhouette"]).name)
            pal = run_cli(["palette", p, "--component", "2", "--k", "2"])
            self.assertEqual(pal["measurements"]["clusters"][0]["hex"], "#C81E1E")
            self.assertAlmostEqual(pal["measurements"]["clusters"][0]["share"], 1.0)
            val = run_cli(["value", p, "--component", "3"])
            self.assertEqual(val["measurements"]["subject"]["n_px"], 4000)
            th = run_cli(["thumb", p, "--component", "1", "--size", "28x38"])
            self.assertEqual(th["verdict"], "measured")
            self.assertIsNotNone(th["measurements"]["silhouette"])
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                lc.main(["silhouette", str(p), "--component", "4"])


class ThumbTest(unittest.TestCase):  # C6
    def test_size_filter_and_subresults(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "hero.png"
            Image.fromarray(circle_on_magenta(400, 200, 200, 100, 80)).save(p)
            out = Path(d) / "diag"
            rec = run_cli(["thumb", p, "--size", "150x150", "--out-dir", out])
            with Image.open(rec["images"]["thumb"]) as th:
                self.assertEqual(th.size, (150, 150))
            m = rec["measurements"]
            self.assertEqual((m["content_box_px"]["w"], m["content_box_px"]["h"]), (150, 75))
            self.assertEqual(rec["params"]["filter"], "lanczos")
            self.assertIsNotNone(m["value"]["subject"])
            self.assertIsNotNone(m["silhouette"]["bbox_px"])
            self.assertAlmostEqual(m["silhouette"]["bbox_px"]["w"], 60, delta=2)
            self.assertTrue(Path(rec["images"]["sheet"]).exists())
            self.assertEqual(Path(rec["images"]["thumb"]).parent, out)


class RecordTest(unittest.TestCase):  # C7
    def test_value_record(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "shot.png"
            img = circle_on_magenta(colour=(255, 255, 255))
            Image.fromarray(img).save(p)
            before = p.read_bytes()
            mask_p = Path(d) / "m.png"
            Image.fromarray(np.where(disc(160, 200, 100, 80, 50), 0, 255).astype(np.uint8)).save(mask_p)
            js = Path(d) / "r.json"
            rec = run_cli(["value", p, "--mask", mask_p, "--ring", "4", "--out", js])
            self.assertEqual(rec["input"]["sha256"], lc.sha256(p))
            self.assertEqual(rec["params"]["ring_px"], 4)
            self.assertEqual(rec["params"]["mask_source"], "mask-image")
            self.assertEqual(rec["verdict"], "measured")
            self.assertEqual(json.loads(js.read_text(encoding="utf-8")), rec)
            meas = rec["measurements"]
            self.assertAlmostEqual(meas["subject"]["p50"], 1.0)
            l_mag = float(lc.relative_luminance(np.array(MAGENTA)))
            self.assertAlmostEqual(meas["ring"]["p50"], l_mag, places=9)
            self.assertAlmostEqual(meas["subject_ring_ratio"], 1.05 / (l_mag + 0.05), places=9)
            self.assertEqual(p.read_bytes(), before)
            with Image.open(rec["images"]["luminance"]) as lum:
                self.assertEqual((lum.mode, lum.size), ("L", (200, 160)))
            for check in ("silhouette", "palette"):
                r = run_cli([check, p])
                self.assertEqual(r["verdict"], "measured")
                self.assertEqual(r["input"]["sha256"], lc.sha256(p))
                self.assertIn("key_tol", r["params"])
            self.assertEqual(run_cli(["palette", p])["params"]["seed"], 0)


PANEL, BUY, CHANCES = (50, 60, 100), (60, 200, 80), (220, 220, 230)
BUY_BOX, CHANCES_BOX = (40, 120, 140, 170), (160, 120, 260, 170)


def lum(rgb) -> float:
    return float(lc.relative_luminance(np.array(rgb)))


def ui_panel() -> np.ndarray:
    """Flat panel 300x200 with two 100x50 buttons: green Buy (left) and light Chances (right), 20 px apart."""
    img = np.zeros((200, 300, 3), dtype=np.uint8)
    img[:] = PANEL
    img[120:170, 40:140] = BUY
    img[120:170, 160:260] = CHANCES
    return img


def box_arg(b) -> str:
    return ",".join(str(v) for v in b)


class UiBoxTest(unittest.TestCase):  # T12 C1: --box masks, --box-key
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = Path(self.tmp.name) / "ui.png"
        Image.fromarray(ui_panel()).save(self.p)

    def tearDown(self):
        self.tmp.cleanup()

    def test_box_masks_exact_area(self):
        rec = run_cli(["silhouette", self.p, "--box", box_arg(BUY_BOX)])
        self.assertEqual((rec["verdict"], rec["params"]["mask_source"]), ("measured", "box"))
        self.assertEqual(rec["measurements"]["area_px"], 5000)
        b = rec["measurements"]["bbox_px"]
        self.assertEqual((b["x0"], b["y0"], b["x1"], b["y1"]), BUY_BOX)
        self.assertEqual(rec["params"]["boxes"], [{"box_px": list(BUY_BOX), "name": None}])
        both = run_cli(["silhouette", self.p, "--box", box_arg(BUY_BOX), "--box", box_arg(CHANCES_BOX)])
        self.assertEqual((both["measurements"]["area_px"], both["measurements"]["component_count"]), (10000, 2))
        overlap = run_cli(["silhouette", self.p, "--box", "40,120,140,170", "--box", "90,120,150,170"])
        self.assertEqual(overlap["measurements"]["area_px"], 110 * 50)  # union, not a sum

    def test_box_key_drops_panel_colour(self):
        loose = (30, 110, 150, 180)  # 120x70 box, 10 px of panel around the Buy button
        plain = run_cli(["silhouette", self.p, "--box", box_arg(loose)])
        self.assertEqual(plain["measurements"]["area_px"], 120 * 70)
        keyed = run_cli(["silhouette", self.p, "--box", box_arg(loose), "--box-key"])
        self.assertEqual(keyed["measurements"]["area_px"], 5000)
        self.assertTrue(keyed["params"]["box_key"])
        info = keyed["params"]["key_estimate"]["boxes"][0]
        self.assertEqual((info["box_key"]["estimated_key"], info["area_px"]), (lc.rgb_to_hex(PANEL), 5000))
        val = run_cli(["value", self.p, "--box", box_arg(loose), "--box-key", "--ring", "4"])
        self.assertAlmostEqual(val["measurements"]["subject"]["p50"], lum(BUY), places=12)
        self.assertAlmostEqual(val["measurements"]["ring"]["p50"], lum(PANEL), places=12)
        pal = run_cli(["palette", self.p, "--box", box_arg(loose), "--box-key", "--k", "2"])
        self.assertEqual([c["hex"] for c in pal["measurements"]["clusters"]], [lc.rgb_to_hex(BUY)])
        th = run_cli(["thumb", self.p, "--box", box_arg(BUY_BOX), "--size", "150x100"])
        self.assertEqual(th["verdict"], "measured")
        self.assertEqual(th["measurements"]["silhouette"]["area_px"], 50 * 25)

    def test_box_key_needs_flat_border_and_valid_boxes(self):
        straddle = (100, 110, 200, 180)  # border crosses both buttons and the panel: not flat
        rec = run_cli(["value", self.p, "--box", box_arg(straddle), "--box-key", "--min-ratio", "1", "--tolerance-source", "t"])
        self.assertEqual(rec["verdict"], "invalid-mask")
        self.assertIn("--box-key", rec["invalid_reason"])
        self.assertNotIn("rule", rec)
        for bad in (["silhouette", self.p, "--box", "0,0,400,10"], ["silhouette", self.p, "--box", "0,0,10,10", "--mask", self.p],
                    ["silhouette", self.p, "--box-key"]):
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                lc.main([str(x) for x in bad])
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            lc.main(["silhouette", str(self.p), "--name", "x"])


class UiExcludeTest(unittest.TestCase):  # T12 C2: --exclude-box / --exclude keep a neighbour out of the ring
    def test_exclude_box_removes_neighbour_from_ring(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ui.png"
            Image.fromarray(ui_panel()).save(p)
            base = ["value", p, "--box", box_arg(BUY_BOX), "--ring", "30"]
            a = run_cli(base)
            ring = a["measurements"]["ring"]
            self.assertEqual(ring["n_px"], 160 * 110 - 5000)  # dilated box minus subject
            # 500 Chances px (10 cols x 50 rows) fall in the ring
            self.assertAlmostEqual(ring["mean"], (12100 * lum(PANEL) + 500 * lum(CHANCES)) / 12600, places=12)
            self.assertIsNone(a["params"]["exclude"])
            b = run_cli(base + ["--exclude-box", box_arg(CHANCES_BOX)])
            ring_b = b["measurements"]["ring"]
            self.assertEqual(b["measurements"]["ring_excluded_px"], 500)
            self.assertEqual(ring_b["n_px"], ring["n_px"] - 500)
            self.assertAlmostEqual(ring_b["mean"], lum(PANEL), places=12)
            self.assertAlmostEqual(ring_b["p95"], lum(PANEL), places=12)
            self.assertAlmostEqual(ring_b["p5"], lum(PANEL), places=12)
            self.assertEqual(b["params"]["exclude"]["boxes"], [list(CHANCES_BOX)])
            self.assertEqual(b["measurements"]["subject"], a["measurements"]["subject"])  # subject untouched
            m = Path(d) / "excl.png"
            em = np.full((200, 300), 255, dtype=np.uint8)
            em[120:170, 160:260] = 0
            Image.fromarray(em).save(m)
            c = run_cli(base + ["--exclude", m])
            self.assertEqual((c["measurements"]["ring"], c["params"]["exclude"]["masks"]), (ring_b, [str(m)]))

    def test_exclude_box_in_palette(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ui.png"
            Image.fromarray(ui_panel()).save(p)
            a = run_cli(["palette", p, "--k", "3"])  # auto-key: both buttons are the subject
            self.assertEqual(sorted(c["hex"] for c in a["measurements"]["clusters"]), sorted(lc.rgb_to_hex(c) for c in (BUY, CHANCES)))
            b = run_cli(["palette", p, "--k", "3", "--exclude-box", box_arg(CHANCES_BOX)])
            self.assertEqual([c["hex"] for c in b["measurements"]["clusters"]], [lc.rgb_to_hex(BUY)])
            self.assertEqual((b["measurements"]["n_px"], b["measurements"]["excluded_px"]), (5000, 5000))


class UiSampleContrastTest(unittest.TestCase):  # T12 C3: contrast --sample
    def test_flat_boxes_match_hex_pair(self):
        img = np.zeros((40, 80, 3), dtype=np.uint8)
        img[:, :40] = (0x77, 0x77, 0x77)
        img[:, 40:] = (255, 255, 255)
        img[10:30, 50:70] = (0x77, 0x77, 0x77)  # grey "text" inside the white half
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "s.png"
            Image.fromarray(img).save(p)
            before = p.read_bytes()
            hexr = run_cli(["contrast", "--pair", "777777,ffffff"])["measurements"]["pairs"][0]["ratio"]
            rec = run_cli(["contrast", "--sample", p, "--fg-box", "5,5,35,35", "--bg-box", "42,0,80,8", "--rule", "wcag-text"])
            q = rec["measurements"]["pairs"][0]
            self.assertAlmostEqual(q["ratio"], hexr, delta=1e-6)
            self.assertEqual((q["fg"], q["bg"], q["source"]), ("#777777", "#FFFFFF", "sample"))
            self.assertEqual((q["fg_sample"]["box_px"], q["fg_sample"]["stat"]), ([5, 5, 35, 35], "median"))
            self.assertEqual(rec["verdict"], "fail")
            self.assertEqual(rec["input"]["sha256"], lc.sha256(p))
            self.assertEqual(rec["params"]["bg_boxes"], [[42, 0, 80, 8]])
            # one box holding text and background: p10 picks the darkest 10 %, p90 the lightest
            mix = run_cli(["contrast", "--sample", p, "--fg-box", "40,0,80,40", "--fg-stat", "p10",
                           "--bg-box", "40,0,80,40", "--bg-stat", "p90"])["measurements"]["pairs"][0]
            self.assertEqual((mix["fg"], mix["bg"]), ("#777777", "#FFFFFF"))
            self.assertAlmostEqual(mix["ratio"], hexr, delta=1e-6)
            both = run_cli(["contrast", "--pair", "000000,ffffff", "--sample", p, "--fg-box", "5,5,35,35", "--bg-box", "42,0,80,8"])
            self.assertEqual(len(both["measurements"]["pairs"]), 2)
            self.assertEqual(p.read_bytes(), before)
            for bad in (["contrast"], ["contrast", "--sample", str(p), "--fg-box", "0,0,5,5"],
                        ["contrast", "--pair", "000000,ffffff", "--fg-box", "0,0,5,5", "--bg-box", "0,0,5,5"]):
                with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                    lc.main(bad)


class UiCompareSubjectsTest(unittest.TestCase):  # T12 C4: value --compare-subjects
    def test_ranks_buttons_and_records_names(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ui.png"
            Image.fromarray(ui_panel()).save(p)
            rec = run_cli(["value", p, "--box", box_arg(BUY_BOX), "--name", "buy", "--box", box_arg(CHANCES_BOX),
                           "--name", "chances", "--compare-subjects", "--ring", "6"])
            self.assertEqual(rec["verdict"], "measured")
            cs = rec["measurements"]["compare_subjects"]
            self.assertEqual(cs["rank_by_median"], ["chances", "buy"])
            self.assertEqual([b["name"] for b in rec["params"]["boxes"]], ["buy", "chances"])
            self.assertAlmostEqual(cs["ring"]["p50"], lum(PANEL), places=12)
            for name, colour, box in (("buy", BUY, BUY_BOX), ("chances", CHANCES, CHANCES_BOX)):
                s = cs["subjects"][name]
                self.assertEqual((s["area_px"], s["boxes_px"]), (5000, [list(box)]))
                self.assertAlmostEqual(s["ratio_to_ring"], lc.contrast_ratio(lum(colour), lum(PANEL)), places=9)
                self.assertTrue(s["brighter_than_ring"])
            # a darker "buy" flips the ranking; a name used twice is one subject (union)
            img = ui_panel()
            img[120:170, 40:140] = (20, 40, 30)
            Image.fromarray(img).save(p)
            rec2 = run_cli(["value", p, "--box", "40,120,90,170", "--name", "buy", "--box", "90,120,140,170", "--name", "buy",
                            "--box", box_arg(CHANCES_BOX), "--name", "chances", "--compare-subjects"])
            cs2 = rec2["measurements"]["compare_subjects"]
            self.assertEqual(cs2["rank_by_median"], ["chances", "buy"])
            self.assertEqual(cs2["subjects"]["buy"]["area_px"], 5000)
            self.assertFalse(cs2["subjects"]["buy"]["brighter_than_ring"])
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                lc.main(["value", str(p), "--box", box_arg(BUY_BOX), "--compare-subjects"])


if __name__ == "__main__":
    unittest.main()
