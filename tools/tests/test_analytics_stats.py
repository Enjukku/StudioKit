#!/usr/bin/env python3
"""Offline tests for tools/analytics/ax_stats.py. Every expected value is published or hand-computed; the
arithmetic or the source is in the comment. Sources: knowledge/reference/analyst/02-statistics-experiments.md
§4 (F-01..F-09) and §5, re-run by the lead (J013-T04 update 2)."""
import os
import sys
import unittest
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "analytics"))
import ax_stats as s  # noqa: E402


def utc(*a):
    return datetime(*a, tzinfo=timezone.utc)


class Maturity(unittest.TestCase):
    # F-08 / RF-14: D7 of cohort 2026-06-20 is the return on 06-27; D30 on 07-20. Lag L = 1 (PROPOSAL):
    # readable once 06-28 (07-21) is a closed UTC day, i.e. from 06-29T00:00Z (07-22T00:00Z).
    def test_d7_boundary(self):
        before = s.cohort_maturity(date(2026, 6, 20), 7, utc(2026, 6, 28, 23, 59, 59))
        self.assertEqual((before["mature"], before["verdict"], before["return_day"]), (False, "not mature", "2026-06-27"))
        self.assertNotIn("value", before)
        at = s.cohort_maturity(date(2026, 6, 20), 7, utc(2026, 6, 29))
        self.assertTrue(at["mature"])
        self.assertEqual((at["readable_once_closed_day"], at["readable_from_utc"]), ("2026-06-28", "2026-06-29T00:00:00Z"))
        self.assertIn("PROPOSAL", at["lag_label"])

    def test_d30_and_lag_parameter(self):
        r = s.cohort_maturity(date(2026, 6, 20), 30, utc(2026, 7, 21, 12))
        self.assertEqual((r["return_day"], r["readable_once_closed_day"], r["mature"]), ("2026-07-20", "2026-07-21", False))
        self.assertEqual(r["wait_hours"], 12.0)  # 07-22T00 - 07-21T12
        self.assertTrue(s.cohort_maturity(date(2026, 6, 20), 30, utc(2026, 7, 21), lag_days=0)["mature"])


class Rates(unittest.TestCase):
    def test_wilson_published(self):
        # Newcombe 1998 (Stat Med 17:857) 81/263 -> 0.2553, 0.3662; 02 F-03 check 2: 10/100 -> 0.0552, 0.1744
        for (x, n), (lo, hi) in (((81, 263), (0.2553, 0.3662)), ((10, 100), (0.0552, 0.1744))):
            got = s.wilson_interval(x, n)
            self.assertAlmostEqual(got[0], lo, places=4)
            self.assertAlmostEqual(got[1], hi, places=4)

    def test_newcombe_published(self):
        # Newcombe 1998 (Stat Med 17:873) method 10, 56/70 vs 48/80: d = 0.2, (0.0524, 0.3339); 02 F-03 check 1
        # gives (0.05243, 0.33387). Here A = 48/80, B = 56/70 so B - A = +20 pp.
        r = s.rate_difference(48, 80, 56, 70)
        self.assertAlmostEqual(r["absolute_difference_pp"], 20.0, places=9)
        self.assertAlmostEqual(r["absolute_interval_pp"][0], 5.243, places=2)
        self.assertAlmostEqual(r["absolute_interval_pp"][1], 33.387, places=2)
        # relative: 0.8 / 0.6 = 1.3333 -> +33.33 %; it is a percent, not percentage points
        self.assertAlmostEqual(r["relative_difference_pct"], 33.3333, places=3)
        self.assertTrue(r["interval_excludes_zero"])

    def test_newcombe_zero_cell(self):
        # 02 F-03 check 3: 2/50 vs 0/50 -> (-0.0370, 0.1346); Wald would give (-0.0143, 0.0943)
        r = s.rate_difference(0, 50, 2, 50)
        self.assertAlmostEqual(r["absolute_interval_pp"][0], -3.700, places=2)
        self.assertAlmostEqual(r["absolute_interval_pp"][1], 13.460, places=2)
        self.assertIsNone(r["relative_difference_pct"])
        w = s.rate_difference(0, 50, 2, 50, method="wald")
        self.assertAlmostEqual(w["absolute_interval_pp"][0], -1.43, places=1)
        self.assertIn("warning", w)

    def test_wald_check(self):
        # 02 F-03: 56/70 vs 48/80 Wald SE 0.072703 -> (0.0575, 0.3425)
        w = s.rate_difference(48, 80, 56, 70, method="wald")
        self.assertAlmostEqual(w["absolute_interval_pp"][0], 5.75, places=1)
        self.assertAlmostEqual(w["absolute_interval_pp"][1], 34.25, places=1)

    def test_relative_katz_hand(self):
        # 100/1000 vs 120/1000: RR 1.2 -> +20 %; SE ln = sqrt(1/120 - 1/1000 + 1/100 - 1/1000) = sqrt(0.0163333)
        # = 0.127802; 1.2 * exp(-+1.959964*0.127802) = 0.93414 / 1.54156 -> -6.586 % / +54.156 %
        r = s.rate_difference(100, 1000, 120, 1000)
        self.assertAlmostEqual(r["absolute_difference_pp"], 2.0, places=9)  # 2 pp, while relative is 20 %
        self.assertAlmostEqual(r["relative_difference_pct"], 20.0, places=9)
        self.assertAlmostEqual(r["relative_interval_pct"][0], -6.586, places=2)
        self.assertAlmostEqual(r["relative_interval_pct"][1], 54.156, places=2)


class Welch(unittest.TestCase):
    def test_t_quantile_table(self):
        # standard table: t(0.975, 25) = 2.0595, t(0.975, 26) = 2.0555, t(0.975, 10) = 2.2281
        self.assertAlmostEqual(s.t_quantile(0.975, 25), 2.0595, places=4)
        self.assertAlmostEqual(s.t_quantile(0.975, 26), 2.0555, places=4)
        self.assertAlmostEqual(s.t_quantile(0.975, 10), 2.2281, places=4)

    def test_f04(self):
        # 02 F-04: n1 10, s1^2 4, n2 20, s2^2 9, d 2: SE 0.921954, df 25.408, t ~2.0578, (0.103, 3.897) +-0.002
        r = s.welch_difference(0.0, 2.0, 10, 2.0, 3.0, 20)
        self.assertAlmostEqual(r["se"], 0.921954, places=5)
        self.assertAlmostEqual(r["df"], 25.408, places=3)
        self.assertAlmostEqual(r["t"], 2.0578, delta=0.002)
        self.assertAlmostEqual(r["interval"][0], 0.103, delta=0.002)
        self.assertAlmostEqual(r["interval"][1], 3.897, delta=0.002)
        self.assertIn("Revenue", r["warning"])


class SampleSize(unittest.TestCase):
    def test_two_proportions_f02(self):
        # 02 F-02: 0.05 -> 0.0525, alpha .05 two-sided, power .8: 122,123.4 -> 122,124 per arm
        r = s.sample_size_proportions(0.05, 0.0525)
        self.assertEqual(r["n_per_arm"], 122124)
        self.assertAlmostEqual(r["absolute_effect_pp"], 0.25, places=9)   # +0.25 pp ...
        self.assertAlmostEqual(r["relative_effect_pct"], 5.0, places=9)   # ... is +5 %
        # lead re-run: 0.18 -> 0.20 = 6,038.53 -> 6,039
        self.assertEqual(s.sample_size_proportions(0.18, 0.20)["n_per_arm"], 6039)
        # hand: 0.10 -> 0.12: pbar .11; 1.959964*sqrt(.1958)=.867270; .841621*sqrt(.1956)=.372222;
        # (1.239492)^2 = 1.536340; / .0004 = 3840.85 -> 3841
        self.assertEqual(s.sample_size_proportions(0.10, 0.12)["n_per_arm"], 3841)
        self.assertEqual(r["inputs"], {"p_a": 0.05, "p_b": 0.0525, "alpha": 0.05, "power": 0.8, "sides": 2})

    def test_means_rule_f01(self):
        # 02 F-01 check A: sigma 30, delta 0.1875: 16*900/0.03515625 = 409,600
        self.assertEqual(s.sample_size_means(30, 0.1875)["n_per_arm"], 409600)
        # check B: sigma^2 0.0475, delta 0.0025: 121,600 (80 %), 159,600 (90 %); exact constant 119,303
        sig = 0.0475 ** 0.5
        b = s.sample_size_means(sig, 0.0025)
        self.assertEqual(b["n_per_arm"], 121600)
        self.assertIn(b["n_per_arm_normal_approx"], (119303, 119304))
        self.assertEqual(s.sample_size_means(sig, 0.0025, power=0.9)["n_per_arm"], 159600)
        self.assertIn("Skewed", b["warning"])
        with self.assertRaises(ValueError):
            s.sample_size_means(1, 1, power=0.85)


class SRM(unittest.TestCase):
    def test_f07_checks(self):
        # 02 F-07 (lead re-run): 105/100 -> 0.121951, p 0.72693; 1050/1000 -> 1.219512, p 0.26946;
        # 10500/10000 -> 12.195122, p 0.00047915 (flagged at 0.0005); 18040/17120 -> 24.0728, p 9.28e-7
        for counts, chi, p, flag in (([105, 100], 0.121951, 0.72693, False), ([1050, 1000], 1.219512, 0.26946, False),
                                     ([10500, 10000], 12.195122, 0.00047915, True),
                                     ([18040, 17120], 24.0728, 9.28e-7, True)):
            r = s.sample_ratio_check(counts)
            self.assertAlmostEqual(r["chi_square"], chi, places=4)
            self.assertAlmostEqual(r["p_value"] / p, 1.0, places=3)
            self.assertEqual(r["srm"], flag)
            self.assertEqual(r["verdict"], "invalid test: investigate" if flag else "no sample ratio mismatch detected")
            self.assertEqual(r["inputs"]["alarm_p"], 0.0005)

    def test_kohavi_example_and_three_arms(self):
        # Kohavi, Tang & Xu 2020 ch. 3: 821,588 vs 815,482 at 50/50 -> p ~1.8e-6
        self.assertAlmostEqual(s.sample_ratio_check([821588, 815482])["p_value"], 1.8e-6, delta=0.05e-6)
        # 02 F-07: 3,400/3,300/3,300 equal weights: chi2 2.0, p = exp(-1) = 0.3679
        r = s.sample_ratio_check([3400, 3300, 3300])
        self.assertAlmostEqual(r["chi_square"], 2.0, places=9)
        self.assertAlmostEqual(r["p_value"], 0.367879, places=5)
        # unequal plan 20/80, observed exactly on plan -> chi2 0, p 1
        self.assertAlmostEqual(s.sample_ratio_check([200, 800], [0.2, 0.8])["p_value"], 1.0, places=9)
        # threshold is a parameter
        self.assertFalse(s.sample_ratio_check([10500, 10000], alarm_p=0.0001)["srm"])

    def test_chi2_sf_critical_values(self):
        # critical values at p = .05: 3.841459 (1 df), 5.991465 (2), 7.814728 (3); 12.116 at p .0005 (1 df)
        for x, df in ((3.841459, 1), (5.991465, 2), (7.814728, 3)):
            self.assertAlmostEqual(s.chi2_sf(x, df), 0.05, places=6)
        self.assertAlmostEqual(s.chi2_sf(12.116, 1), 0.0005, places=6)
        # closed form for df 4: exp(-x/2)(1 + x/2); x = 0.5 -> 0.778801 * 1.25 = 0.973501
        self.assertAlmostEqual(s.chi2_sf(0.5, 4), 0.973501, places=6)


class DiD(unittest.TestCase):
    def test_card_krueger(self):
        # 02 F-09: Card & Krueger, NJ change +0.59, PA change -2.16 -> DiD 2.75 (FTE means 20.44->21.03, 23.33->21.17)
        r = s.diff_in_diff(20.44, 21.03, 23.33, 21.17)
        self.assertAlmostEqual(r["did"], 2.75, places=9)
        self.assertIn("parallel trends", r["assumption"])

    def test_rates_and_se(self):
        # 02 F-09: 0.10 -> 0.12 treated, 0.10 -> 0.11 comparison: 0.01 (1 pp); four SE 0.2 -> 0.4
        r = s.diff_in_diff(0.10, 0.12, 0.10, 0.11, se=[0.2, 0.2, 0.2, 0.2])
        self.assertAlmostEqual(r["did"], 0.01, places=12)
        self.assertAlmostEqual(r["did_se"], 0.4, places=12)
        self.assertAlmostEqual(r["did_interval"][1] - r["did"], 1.959964 * 0.4, places=5)


class Mix(unittest.TestCase):
    def test_hand_computed_split(self):
        # before: A 800 @ 0.20, B 200 @ 0.20 -> 0.20. after: A 800 @ 0.20, B 1000 @ 0.09 -> (160 + 90) / 1800
        # = 0.138889. Standardized after (before weights 0.8 / 0.2): 0.8*0.20 + 0.2*0.09 = 0.178.
        # rate part = 0.178 - 0.20 = -2.2 pp; mix part = 0.138889 - 0.178 = -3.9111 pp; total -6.1111 pp.
        r = s.mix_decomposition([
            {"name": "A", "n_before": 800, "rate_before": 0.20, "n_after": 800, "rate_after": 0.20},
            {"name": "B", "n_before": 200, "rate_before": 0.20, "n_after": 1000, "rate_after": 0.09}])
        self.assertAlmostEqual(r["overall_after"], 250 / 1800, places=9)
        self.assertAlmostEqual(r["standardized_after_before_weights"], 0.178, places=9)
        self.assertAlmostEqual(r["rate_effect_pp_before_weights"], -2.2, places=6)
        self.assertAlmostEqual(r["mix_effect_pp_before_weights"], -3.911111, places=5)
        self.assertAlmostEqual(r["rate_effect_pp_before_weights"] + r["mix_effect_pp_before_weights"],
                               r["total_change_pp"], places=9)
        self.assertAlmostEqual(r["rate_effect_pp_after_weights"] + r["mix_effect_pp_after_weights"],
                               r["total_change_pp"], places=9)
        self.assertAlmostEqual(r["returned_after"], 250, places=9)

    def test_rejects_bad_input(self):
        with self.assertRaises(ValueError):
            s.mix_decomposition([{"name": "A", "n_before": 10, "rate_before": 1.5, "n_after": 10, "rate_after": 0.1}])
        with self.assertRaises(ValueError):
            s.mix_decomposition([])


class Verdict(unittest.TestCase):
    def v(self, lo, hi, point=None, **kw):
        return s.verdict(lo, hi, (lo + hi) / 2 if point is None else point, 2.0, 1.0, **kw)

    def test_02_table_strict(self):
        # 02 §5 test vectors, b = 2.0, h = 1.0, strict rule
        table = [((2.5, 4.0), "useful improvement", ""), ((2.0, 3.0), "useful improvement", ""),
                 ((0.5, 3.0), "inconclusive", "benefit unproven"), ((1.0, 5.0), "inconclusive", "benefit unproven"),
                 ((-0.5, 1.5), "no worthwhile effect within tested bounds", ""),
                 ((-1.5, 1.0), "inconclusive", "harm not excluded"), ((-3.0, -1.0), "harmful", "upper bound <= -harm"),
                 ((-2.0, 3.0), "inconclusive", "harm not excluded")]
        for (lo, hi), verdict, reason in table:
            r = self.v(lo, hi, rule="strict")
            self.assertEqual((r["verdict"], r["reason"]), (verdict, reason), (lo, hi))

    def test_default_rule_is_lead_proposal(self):
        # [1.0, 5.0], point 3.0: strict -> inconclusive; default (L > 0 and point >= b) -> useful; label PROPOSAL
        r = self.v(1.0, 5.0)
        self.assertEqual(r["verdict"], "useful improvement")
        self.assertIn("PROPOSAL", r["rule_label"])
        # [0.5, 3.0] with point 1.75 < b -> still inconclusive under default
        self.assertEqual(self.v(0.5, 3.0)["verdict"], "inconclusive")

    def test_guardrail_srm_maturity(self):
        g = [{"name": "crash rate", "lower": -1.2, "upper": 0.3, "margin": 1.0}]
        self.assertEqual(self.v(2.5, 4.0, guardrails=g)["reason"], "guardrail not cleared")
        self.assertEqual(self.v(2.5, 4.0, integrity_ok=False)["verdict"], "invalid")
        self.assertEqual(self.v(2.5, 4.0, matured=False)["verdict"], "no verdict yet")
        self.assertEqual(self.v(2.5, 4.0, integrity_ok=False, matured=False)["verdict"], "no verdict yet")


if __name__ == "__main__":
    unittest.main()
