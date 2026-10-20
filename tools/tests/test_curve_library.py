#!/usr/bin/env python3
"""Offline tests for tools/vfx/curve_library.py using synthetic curves."""
import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "vfx"))
import curve_library as cl  # noqa: E402


class Resample(unittest.TestCase):
    def test_linear_and_endpoints(self):
        v = cl.resample([[0, 0, 0], [1, 10, 0]], 41)
        self.assertEqual(len(v), 41)
        self.assertAlmostEqual(v[0], 0)
        self.assertAlmostEqual(v[20], 5)
        self.assertAlmostEqual(v[40], 10)

    def test_step_like_pop(self):
        keys = [[0, 0, 0], [0.01, 1, 0], [1, 1, 0]]
        self.assertAlmostEqual(cl.at(keys, 0.005), 0.5)
        self.assertAlmostEqual(cl.at(keys, 0.5), 1.0)


class Clean(unittest.TestCase):
    def test_dupes_range_and_bounds(self):
        k = cl.clean_keys([[0.2, 0.5, 0], [1.0, 2.0, 0], [1.0, 3.0, 0]], 0.0, 1.0)
        self.assertEqual(k[0][0], 0.0)
        self.assertEqual(k[-1][0], 1.0)
        self.assertEqual([p[0] for p in k], sorted({p[0] for p in k}))
        self.assertTrue(all(0 <= p[1] <= 1 for p in k))

    def test_max_keys(self):
        k = cl.clean_keys([[i / 39, (i % 2) * 1.0, 0] for i in range(40)])
        self.assertLessEqual(len(k), 20)
        self.assertEqual((k[0][0], k[-1][0]), (0.0, 1.0))


class Normalise(unittest.TestCase):
    def test_peak_and_sign(self):
        k, peak = cl.normalise([[0, -4, 0], [1, 2, 1]])
        self.assertEqual(peak, 4)
        self.assertAlmostEqual(k[0][1], -1)
        self.assertAlmostEqual(k[1][1], 0.5)
        self.assertAlmostEqual(k[1][2], 0.25)


class Medoid(unittest.TestCase):
    def test_two_groups_and_real_medoid(self):
        grow = [[[0, 0, 0], [1, 1 + 0.01 * i, 0]] for i in range(6)]
        shrink = [[[0, 1, 0], [1, 0.01 * i, 0]] for i in range(6)]
        curves = [cl.normalise(c)[0] for c in grow + shrink]
        D = cl.dist_matrix(np.array([cl.features(c) for c in curves]))
        med, lab = cl.kmedoids(D, 2, restarts=5)
        self.assertEqual(len(set(lab[:6])), 1)
        self.assertEqual(len(set(lab[6:])), 1)
        self.assertNotEqual(lab[0], lab[6])
        self.assertTrue(all(m in range(12) for m in med))  # medoids are members, not averages

    def test_names(self):
        self.assertEqual(cl.name_size([[0, 0, 0], [0.01, 1, 0], [1, 0, 0]]), "impact pop then shrink")
        self.assertEqual(cl.name_size([[0, 1, 0], [1, 0, 0]]), "linear shrink")
        self.assertEqual(cl.name_transp([[0, 1, 0], [0.5, 0, 0], [1, 1, 0]]), "fade in, hold, fade out")
        self.assertEqual(cl.name_transp([[0, 0, 0], [1, 0, 0]]), "opaque hold")

    def test_colour_pattern(self):
        self.assertEqual(cl.colour_pattern([[0, [10, 20, 30]], [1, [10, 20, 30]]]), "constant colour")
        self.assertEqual(cl.colour_pattern([[0, [255, 255, 0]], [1, [170, 60, 255]]]), "hue shift")


if __name__ == "__main__":
    unittest.main()
