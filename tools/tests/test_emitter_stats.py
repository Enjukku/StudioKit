#!/usr/bin/env python3
"""Offline tests for tools/vfx/emitter_stats.py (synthetic input only)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "vfx"))
import emitter_stats as es  # noqa: E402


def feat(**kw):
    base = {
        "name": "x", "ctx": "", "orient": 0, "squash": False, "lum": 0.8, "light_emission": 0.0, "brightness": 1.0,
        "drag": 0.0, "speed": 0.0, "peak": 2.0, "lifetime": 0.5, "growth": 1.0, "fb": False, "tex_shape": None,
        "tex_group": None,
    }
    base.update(kw)
    return base


class SequenceShape(unittest.TestCase):
    def test_interpolation(self):
        pts = es.seq_points([[0, 0, 0], [1, 10, 0]])
        self.assertAlmostEqual(es.seq_at(pts, 0.25), 2.5)
        self.assertEqual(es.seq_at(pts, -1), 0)
        self.assertEqual(es.seq_at(pts, 2), 10)

    def test_size_shape_fraction_of_max(self):
        sh = es.size_shape([[0, 0, 0], [0.5, 4, 0], [1, 2, 0]], (0.0, 0.25, 0.5, 1.0))
        self.assertEqual([round(v, 3) for v in sh], [0.0, 0.5, 1.0, 0.5])

    def test_negative_clamps_to_zero_and_zero_curve_is_none(self):
        self.assertEqual(es.size_shape([[0, -5, 0], [1, 5, 0]], (0.0, 1.0)), [0.0, 1.0])
        self.assertIsNone(es.size_shape([[0, 0, 0], [1, 0, 0]]))
        self.assertIsNone(es.size_shape([]))

    def test_classes(self):
        self.assertEqual(es.size_class([[0, 1, 0], [1, 0, 0]]), "shrink")
        self.assertEqual(es.size_class([[0, 0.2, 0], [1, 1, 0]]), "grow")
        self.assertEqual(es.size_class([[0, 1, 0], [1, 1, 0]]), "flat")
        self.assertEqual(es.size_class([[0, 0, 0], [0.3, 1, 0], [1, 0, 0]]), "bump")
        self.assertEqual(es.transp_class([[0, 0, 0], [1, 1, 0]]), "fade-out")
        self.assertEqual(es.transp_class([[0, 1, 0], [0.5, 0, 0], [1, 1, 0]]), "fade-in-out")
        self.assertEqual(es.transp_class([[0, 0, 0], [1, 0.1, 0]]), "opaque")

    def test_colour_change(self):
        self.assertFalse(es.colour_changes([[0, [255, 0, 0]], [1, [255, 10, 0]]]))
        self.assertTrue(es.colour_changes([[0, [255, 0, 0]], [1, [0, 0, 255]]]))


class Stats(unittest.TestCase):
    def test_percentiles(self):
        v = [1, 2, 3, 4, 5]
        self.assertEqual(es.pctl(v, 50), 3)
        self.assertAlmostEqual(es.pctl(v, 10), 1.4)
        self.assertIsNone(es.pctl([], 50))

    def test_summarize_skips_none(self):
        s = es.summarize([None, 1, 3])
        self.assertEqual((s["n"], s["med"]), (2, 2))

    def test_median_curve_and_share(self):
        self.assertEqual(es.median_curve([[0, 1], [1, 3], [2, 5]]), [1, 3])
        self.assertEqual(es.share([1, 2, 3, 4], lambda x: x > 2), 0.5)

    def test_live_particle_estimate(self):
        rows = [
            {"class": "ParticleEmitter", "lifetime": [1, 1], "emit_count": 10, "emit_delay": 0.0, "enabled": False, "rate": 20},
            {"class": "ParticleEmitter", "lifetime": [1, 1], "emit_count": 5, "emit_delay": 2.0, "enabled": False, "rate": 0},
            {"class": "ParticleEmitter", "lifetime": [0.5, 0.5], "emit_count": None, "emit_delay": None, "enabled": True, "rate": 10},
        ]
        self.assertEqual(es.effect_peak_live(rows), 15.0)  # 10 burst + 10*0.5 continuous at t=0

    def test_unit_recipe_relative_times(self):
        rows = [
            {"class": "ParticleEmitter", "job": "core", "emit_count": 1, "emit_delay": 0.05, "enabled": False, "rate": 0, "lifetime": [0.2, 0.2], "z_offset": 1.0},
            {"class": "ParticleEmitter", "job": "smoke", "emit_count": 4, "emit_delay": 0.15, "enabled": False, "rate": 0, "lifetime": [1, 1], "z_offset": 0.0},
        ]
        rec = es.unit_recipe(rows)
        self.assertAlmostEqual(rec["core"][0], 0.0)
        self.assertAlmostEqual(rec["smoke"][0], 0.10)
        self.assertEqual(rec["smoke"][1], 4)


class Classify(unittest.TestCase):
    def test_name_rules(self):
        self.assertEqual(es.classify(feat(name="Fancy Smoke33"))[0], "smoke")
        self.assertEqual(es.classify(feat(name="Flare213New"))[0], "flare/star")
        self.assertEqual(es.classify(feat(name="Ground15", orient=3))[0], "ground decal")
        self.assertEqual(es.classify(feat(name="Ele1ctric 2"))[0], "lightning/electric")

    def test_props_rules(self):
        self.assertEqual(es.classify(feat(name="1", orient=2, squash=True, speed=40))[0], "streak/speedline")
        self.assertEqual(es.classify(feat(name="1", drag=5, speed=30, peak=0.4))[0], "spark")
        self.assertEqual(es.classify(feat(name="1", orient=3, speed=0, growth=5))[0], "ring/shockwave")
        self.assertEqual(es.classify(feat(name="D33ark", lum=0.05))[0], "dark underlay/twin")

    def test_big_static_spec_is_glow(self):
        self.assertEqual(es.classify(feat(name="Spec19", peak=25, speed=0))[0], "glow/halo")

    def test_hidden_set_never_listed(self):
        self.assertEqual(len(es.HIDDEN), 8)
        if os.path.isdir(os.path.join(es.DUMPS, "json")):
            self.assertEqual(len(es.study_files()), 30)
            self.assertFalse(set(es.study_files()) & set(es.HIDDEN))

    def test_attribute_line_parse_shape(self):
        import tempfile
        d = tempfile.mkdtemp()
        old = es.DUMPS
        try:
            os.makedirs(os.path.join(d, "attributes"))
            with open(os.path.join(d, "attributes", "fx.txt"), "w", encoding="utf-8") as fh:
                fh.write("/A/B/Fire [ParticleEmitter] EmitCount=7.0 EmitDelay=0.05\n/A/B/Fire [ParticleEmitter] EmitCount=3.0 EmitDelay=0.0\n")
            es.DUMPS = d
            a = es.parse_attrs("fx")
            self.assertEqual(len(a[("/A/B/Fire", "ParticleEmitter")]), 2)
            self.assertEqual(es.num(a[("/A/B/Fire", "ParticleEmitter")][0]["EmitCount"]), 7.0)
        finally:
            es.DUMPS = old


if __name__ == "__main__":
    unittest.main()
