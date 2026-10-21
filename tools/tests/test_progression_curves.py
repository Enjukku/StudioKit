"""Offline tests for tools/progression/curves.py: the research paper's exact fixtures (Fraction equality).

Sources of the fixture numbers (owner research paper, outside git): M01 Lemonade 2016-10-04 (section 4),
M05 generator chain 2016-10-28, M04 XP table and 5-HP combat example 2010-07-14, M06 stacking 2023-10-10,
C01 prestige formulas 2017-01-12, C02 Factorio research cost 2016-10-21.
"""

import itertools
import math
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "progression"))
import curves as cv  # noqa: E402

R = F(107, 100)  # M01 growth
P1 = F(167, 100)  # M01 output per producer per second


def lemonade_price(k):  # next price with k owned (M01 reindexed): 4 * r**(k-1)
    return cv.exponential(4, R, k - 1)


def lemonade_income(k):  # P(k) = 1.67 k with x2 at 25 and 50 owned (M01)
    return cv.milestone_product(P1 * k, [(25, 2), (50, 2)], k)


class LemonadeM01(unittest.TestCase):
    WAITS = [F(400, 167), F(214, 167), F(11449, 12525), F(1225043, 1670000), F(131079601, 208750000)]
    CUMULATIVE = [F(400, 167), F(614, 167), F(57499, 12525), F(26674729, 5010000), F(465947491, 78281250)]

    def test_waits_and_cumulative_times_exact(self):
        t, waits, cum = F(0), [], []
        for k in range(1, 6):  # 1 -> 2 ... 5 -> 6, wallet 0 after each purchase
            w = cv.wait_time(lemonade_price(k), 0, lemonade_income(k))
            t += w
            waits.append(w)
            cum.append(t)
        self.assertEqual(waits, self.WAITS)
        self.assertEqual(cum, self.CUMULATIVE)

    def test_closed_form_equals_step_sum_for_every_k_up_to_25(self):
        t = F(0)
        for k in range(1, 26):
            self.assertEqual(cv.sequential_reinvest_time(4, R, P1, k), t, k)
            if k < 25:
                t += cv.wait_time(lemonade_price(k), 0, lemonade_income(k))
        self.assertEqual(cv.sequential_reinvest_time(4, R, P1, 6), self.CUMULATIVE[-1])

    def test_income_at_milestones(self):
        self.assertEqual(lemonade_income(24), F("40.08"))
        self.assertEqual(lemonade_income(25), F("83.5"))
        self.assertEqual(lemonade_income(49), F("163.66"))
        self.assertEqual(lemonade_income(50), F(334))


class BulkBuy(unittest.TestCase):
    def test_closed_form_equals_direct_sum_on_a_grid(self):
        count = 0
        for b, r, k, n in itertools.product((F(1), F(4), F(7, 2)), (F(1), F(107, 100), F(115, 100), F(3, 2), F(2)),
                                            range(10), range(17)):
            direct = cv.bulk_cost_direct(lambda j: b * r ** j, k, n)
            self.assertEqual(cv.bulk_cost_closed(b, r, k, n), direct, (b, r, k, n))
            count += 1
        self.assertGreaterEqual(count, 2550)

    def test_max_affordable_decided_by_the_inequality(self):
        for b, r, k in ((F(4), R, 0), (F(4), R, 7), (F(10), F(3, 2), 2), (F(3), F(1), 0)):
            for wallet in [F(0), F(3), F(4), F(25), F(100), cv.bulk_cost_closed(b, r, k, 5), cv.bulk_cost_closed(b, r, k, 5) - F(1, 10**9)]:
                for rounding in ("none", "ceil", "floor", "half_even"):
                    n = cv.max_affordable(b, r, k, wallet, rounding)
                    total = lambda m: cv.bulk_cost_direct(lambda j: b * r ** j, k, m, rounding)  # noqa: E731
                    self.assertLessEqual(total(n), wallet)
                    self.assertGreater(total(n + 1), wallet)

    def test_bulk_rounding_scope(self):
        price = lambda j: F(5, 2) + j  # noqa: E731  2.5, 3.5
        self.assertEqual(cv.bulk_cost_direct(price, 0, 2, "ceil"), 7)  # 3 + 4: sum of rounded prices
        self.assertEqual(cv.bulk_cost_direct(price, 0, 2, "ceil", scope="bulk_sum"), 6)  # ceil(6)
        self.assertEqual(cv.round_price(F(5, 2), "half_even"), 2)


class Waits(unittest.TestCase):
    def test_zero_income_is_unreachable_never_zero(self):
        self.assertIsInstance(cv.wait_time(10, 3, 0), cv.Unreachable)
        self.assertEqual(cv.wait_time(10, 3, 0).reason, "unreachable: zero income")
        self.assertEqual(cv.wait_time(10, 12, 0), 0)
        self.assertEqual(cv.time_for_requirement(5, 0)["status"], "unreachable")

    def test_symbolic_rate_returns_the_requirement(self):
        r = cv.time_for_requirement(15000)
        self.assertEqual((r["status"], r["time_s"], r["requirement"]), ("symbolic", None, 15000))
        self.assertEqual(cv.time_for_requirement(15000, F(3))["time_s"], 5000)

    def test_piecewise_rates(self):
        self.assertEqual(cv.time_piecewise(30, [(10, 1), (None, 2)]), 20)
        self.assertEqual(cv.time_piecewise(30, [(10, 1), (None, 0)]), cv.UNREACHABLE_ZERO_INCOME)

    def test_payback(self):
        self.assertEqual(cv.payback(F(4), P1), F(400, 167))
        with self.assertRaises(ValueError):
            cv.payback(4, 0)


class CurveShapes(unittest.TestCase):
    def test_samples_at_0_1_2(self):
        self.assertEqual([cv.affine(3, 2, n) for n in range(3)], [3, 5, 7])
        self.assertEqual([cv.polynomial(1, 2, 3, n) for n in range(3)], [1, 3, 17])
        self.assertEqual([cv.triangular_cumulative(5, n) for n in range(3)], [0, 5, 15])
        self.assertEqual([cv.exponential(2, F(3, 2), n) for n in range(3)], [2, 3, F(9, 2)])
        self.assertEqual([cv.saturating(1, 4, 2, n) for n in range(3)], [1, F(7, 3), 3])
        self.assertAlmostEqual(cv.logarithmic(1, 2, 2, 1), 3.0)
        self.assertAlmostEqual(cv.fractional_power(0, 1, F(1, 2), 4), 2.0)
        self.assertEqual(cv.fractional_power(5, 3, F(1, 2), 1), 8)

    def test_piecewise_keeps_breakpoint(self):
        self.assertEqual([cv.piecewise_linear(0, 2, 5, 3, n) for n in (2, 3, 4)], [4, 6, 11])

    def test_factorio_research_cost_c02(self):
        self.assertEqual([cv.exponential(1000, 2, lvl - 6) for lvl in (6, 7, 8)], [1000, 2000, 4000])
        with self.assertRaises(ValueError):
            cv.exponential(1000, 2, 5 - 6)  # level below 6 is outside the published formula's domain

    def test_m05_continuous_chain_closed_form(self):
        # C(t) = t^2/2 with one tier-2 generator (M05): polynomial a=0, b=1/2, p=2
        self.assertEqual([cv.polynomial(0, F(1, 2), 2, t) for t in range(6)], [0, F(1, 2), 2, F(9, 2), 8, F(25, 2)])

    def test_evaluate_spec_and_no_table_extrapolation(self):
        self.assertEqual(cv.evaluate({"kind": "exponential", "a": 4, "r": R}, 1), F("4.28"))
        self.assertEqual(cv.evaluate({"kind": "table", "values": [1, 2]}, 1), 2)
        with self.assertRaises(ValueError):
            cv.evaluate({"kind": "table", "values": [1, 2]}, 2)
        with self.assertRaises(ValueError):
            cv.evaluate({"kind": "exponential", "a": 4}, 1)


class Levels(unittest.TestCase):
    def test_m04_cumulative_xp_and_points(self):
        per = [cv.affine(0, 1000, lvl) for lvl in range(1, 6)]  # e_l = 1000 l
        x = cv.cumulative_from_per_level(per)
        self.assertEqual(x, [0, 1000, 3000, 6000, 10000, 15000])
        for lvl in range(1, 7):
            self.assertEqual(x[lvl - 1], 500 * lvl * (lvl - 1))
            a_l = cv.triangular_cumulative(1, lvl - 1)  # A_l = l(l-1)/2
            self.assertEqual(a_l, F(lvl * (lvl - 1), 2))
            self.assertEqual(x[lvl - 1], 1000 * a_l)
        self.assertEqual(cv.per_level_from_cumulative(x), per)
        self.assertEqual(cv.level_for(x, 2999), 2)
        self.assertEqual(cv.level_for(x, 3000), 3)


class Combat(unittest.TestCase):
    def test_m04_breakpoint_and_both_first_hit_conventions(self):
        for tau in (F(1), F(3, 2), F(7, 10)):
            n4, n5 = cv.hits_to_kill(5, 4), cv.hits_to_kill(5, 5)
            self.assertEqual((n4, n5), (2, 1))
            immediate = cv.first_hit_offset(tau, "immediate")
            windup = cv.first_hit_offset(tau, "after_interval")
            self.assertEqual((cv.time_to_kill(n4, tau, immediate), cv.time_to_kill(n5, tau, immediate)), (tau, 0))
            self.assertEqual((cv.time_to_kill(n4, tau, windup), cv.time_to_kill(n5, tau, windup)), (2 * tau, tau))

    def test_variable_damage_sequence(self):
        self.assertEqual(cv.hits_for_sequence(10, [3, 3, 3, 3]), 4)
        self.assertEqual(cv.hits_for_sequence(10, [6, 4]), 2)
        self.assertIsNone(cv.hits_for_sequence(10, [3, 3]))

    def test_effective_health_and_stacking_m06(self):
        self.assertEqual(cv.effective_health(100, F(1, 4)), F(400, 3))
        self.assertEqual(cv.stack_bonus([F("0.18")], [F("0.2")]), F("0.416"))
        self.assertEqual(cv.stack_bonus([F("0.18"), F("0.2")], []), F("0.38"))
        with self.assertRaises(ValueError):
            cv.effective_health(100, 1)


class Prestige(unittest.TestCase):
    def test_published_formulas_c01_exact_floors(self):
        self.assertEqual(cv.adventure_capitalist_prestige_floor(10 ** 15), 150)
        self.assertEqual(cv.adventure_capitalist_prestige_floor(4 * 10 ** 15), 300)
        self.assertEqual(cv.adventure_capitalist_prestige_floor(4 * 10 ** 15 - 1), 299)
        self.assertEqual(cv.cookie_clicker_prestige_floor(8 * 10 ** 12), 2)
        self.assertEqual(cv.cookie_clicker_prestige_floor(8 * 10 ** 12 - 1), 1)
        self.assertEqual(cv.realm_grinder_prestige_floor(3 * 10 ** 12), 2)  # n(n+1)/2 = 3 -> n = 2
        self.assertEqual(cv.realm_grinder_prestige_floor(3 * 10 ** 12 - 1), 1)
        for x in (12345678901234567, 98765432109876543210, 10 ** 13 + 7):
            self.assertEqual(cv.adventure_capitalist_prestige_floor(x), math.floor(cv.adventure_capitalist_prestige(x)))
            self.assertEqual(cv.realm_grinder_prestige_floor(x), math.floor(cv.realm_grinder_prestige(x)))

    def test_accounting_rules(self):
        self.assertEqual(cv.award_total_entitlement(17, 10), 7)
        self.assertEqual(cv.award_total_entitlement(17, 20), 0)
        self.assertEqual(cv.award_per_run(F(17, 2)), 8)

    def test_inverse_rule(self):
        self.assertEqual(cv.input_multiplier_for_entitlement(2, F(1, 2)), 4)
        self.assertEqual(cv.input_multiplier_for_entitlement(2, F(1, 3)), 8)  # doubling a cube root: 8x input


class Offline(unittest.TestCase):
    def test_cap_is_required_and_applied(self):
        with self.assertRaises(TypeError):
            cv.offline_earned(F(1, 2), 10, 600)  # pylint: disable=missing-kwoa
        self.assertEqual(cv.offline_earned(F(1, 2), 10, 600, cap_s=300), 1500)
        self.assertEqual(cv.offline_earned(F(1, 2), 10, 200, cap_s=300), 1000)
        self.assertEqual(cv.offline_earned(F(1, 2), 10, -5, cap_s=300), 0)
        self.assertEqual(cv.offline_earned(1, 10, 600, cap_s=None), 6000)


class PaidRandom(unittest.TestCase):
    def test_constant_p(self):
        p = F(1, 20)
        self.assertEqual(cv.expected_spend(10, p), 200)
        self.assertEqual(cv.p_success_within(2, p), 1 - F(19, 20) ** 2)
        for q in (F(1, 2), F(9, 10), F(99, 100)):
            n = cv.attempts_for_quantile(q, p)
            self.assertGreaterEqual(cv.p_success_within(n, p), q)
            self.assertLess(cv.p_success_within(n - 1, p), q)
        self.assertEqual(cv.attempts_for_quantile(F(1, 2), F(1, 2)), 1)  # exact boundary

    def test_pity_variant_uses_conditional_probabilities(self):
        seq = [F(1, 10)] * 9 + [F(1)]
        self.assertEqual(cv.p_success_within_conditional(seq), 1)
        self.assertEqual(cv.p_success_within_conditional(seq[:2]), 1 - F(9, 10) ** 2)
        self.assertEqual(cv.expected_tries_conditional(seq), sum(F(9, 10) ** i for i in range(10)))

    def test_domain_errors(self):
        for bad in (0, 1, F(3, 2), -F(1, 10)):
            with self.assertRaises(ValueError):
                cv.expected_spend(10, bad)
        with self.assertRaises(ValueError):
            cv.exponential(1, 1, 2)
        with self.assertRaises(ValueError):
            cv.affine(0, 1, -1)
        with self.assertRaises(ValueError):
            cv.hits_to_kill(5, 0)


if __name__ == "__main__":
    unittest.main()
