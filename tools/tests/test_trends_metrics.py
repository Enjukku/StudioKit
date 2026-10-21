#!/usr/bin/env python3
"""Offline tests for tools/trends/trend_metrics.py (synthetic series only)."""
import os
import sys
import unittest
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trends"))
import trend_metrics as tm  # noqa: E402

T0 = datetime(2026, 10, 1, tzinfo=timezone.utc)
AS_OF = datetime(2026, 10, 22, 6, 0, tzinfo=timezone.utc)  # complete days end 2026-10-22 00:00
END = datetime(2026, 10, 22, tzinfo=timezone.utc)
TH = {"breakout_g7_min": 0.5, "breakout_added_ccu_min": 100, "breakout_consecutive_days": 3,
      "coverage_min": 0.9, "max_gap_minutes": 60, "fade_negative_weeks": 2}
GAP = timedelta(minutes=60)


def sampled(fn, start=END - timedelta(days=21), end=END, step=timedelta(minutes=10), skip=None):
    """Samples every step from start to end inclusive; fn(t) -> value; skip(t) -> True drops the sample."""
    out, t = [], start
    while t <= end:
        if not (skip and skip(t)):
            out.append((t, float(fn(t))))
        t += step
    return out


def by_week(newest, middle, oldest):
    def fn(t):
        return newest if t >= END - tm.WEEK else middle if t >= END - 2 * tm.WEEK else oldest
    return fn


class Integration(unittest.TestCase):
    def test_trapezoid_player_hours(self):
        s = [(T0, 0.0), (T0 + timedelta(minutes=30), 100.0), (T0 + timedelta(hours=1), 100.0)]
        w = tm.integrate(s, T0, T0 + timedelta(hours=1), GAP)
        self.assertAlmostEqual(w["player_hours"], 0.5 * 50 + 0.5 * 100)  # 25 + 50
        self.assertAlmostEqual(w["covered_hours"], 1.0)
        self.assertAlmostEqual(w["mean_ccu"], 75.0)

    def test_gap_not_bridged(self):
        s = [(T0, 100.0), (T0 + timedelta(hours=2), 100.0), (T0 + timedelta(hours=2, minutes=30), 100.0)]
        w = tm.integrate(s, T0, T0 + timedelta(hours=3), GAP)
        self.assertAlmostEqual(w["player_hours"], 50.0)  # only the 30-minute segment
        self.assertAlmostEqual(w["covered_hours"], 0.5)
        self.assertAlmostEqual(w["coverage"], 0.5 / 3)
        self.assertAlmostEqual(w["max_gap_minutes"], 120.0)


class Growth(unittest.TestCase):
    def test_g7_non_overlapping_and_momentum_labelled(self):
        s = sampled(lambda t: 200 if t >= END - tm.DAY else 100)
        cur, prev = tm.weeks(s, AS_OF, 2, GAP)
        self.assertEqual(cur["start"], prev["end"])
        self.assertEqual(cur["end"], END)
        g = tm.g7(cur, prev)
        self.assertAlmostEqual(g["value"], cur["mean_ccu"] / prev["mean_ccu"] - 1)
        self.assertAlmostEqual(g["value"], 1 / 7, places=2)
        m = tm.momentum(s, AS_OF, TH)
        self.assertEqual(m["label"], "momentum, not week-over-week")
        self.assertAlmostEqual(m["value"], 200 / cur["mean_ccu"], places=3)

    def test_zero_baseline_is_not_infinity(self):
        zero = {"mean_ccu": 0.0}
        g = tm.g7({"mean_ccu": 500.0}, zero)
        self.assertIsNone(g["value"])
        self.assertEqual(g["status"], "new / insufficient baseline")
        young = sampled(lambda t: 500, start=END - tm.WEEK)  # no previous-week history
        self.assertEqual(tm.breakout(young, AS_OF, TH)["status"], "new / insufficient baseline")

    def test_breakout_when_all_conditions_hold(self):
        b = tm.breakout(sampled(by_week(400, 200, 200)), AS_OF, TH)
        self.assertEqual(b["status"], "breakout")
        self.assertAlmostEqual(b["g7"]["value"], 1.0, places=2)
        self.assertGreaterEqual(b["matched_days"], 3)

    def test_coverage_below_threshold_suppresses_breakout(self):
        hole = (END - timedelta(days=3), END - timedelta(days=2))  # one missing day: coverage ~86%
        s = sampled(by_week(400, 200, 200), skip=lambda t: hole[0] < t < hole[1])
        b = tm.breakout(s, AS_OF, TH)
        self.assertEqual(b["status"], "suppressed: coverage")
        self.assertLess(b["current"]["coverage"], 0.9)

    def test_fade_needs_two_negative_weeks_and_lower_trough(self):
        s = sampled(by_week(200, 300, 400))
        self.assertEqual(tm.fade(s, s, AS_OF, TH)["status"], "fade")
        one_drop = sampled(by_week(200, 450, 400))  # only the latest week fell
        self.assertEqual(tm.fade(one_drop, one_drop, AS_OF, TH)["status"], "no fade")

    def test_momentum_held_under_coverage_gate(self):  # J004-T12 finding 8
        # steady 1,000 all week; the last 24 h hold one hour of samples at a 3,000 peak
        s = sampled(lambda t: 3000 if t >= END - tm.HOUR else 1000,
                    skip=lambda t: END - tm.DAY - 2 * tm.HOUR < t < END - tm.HOUR)
        m = tm.momentum(s, AS_OF, TH)
        self.assertEqual((m["value"], m["status"]), (None, "insufficient coverage"))
        self.assertAlmostEqual(m["coverage_24h"], 1 / 24)

    def test_trough_is_lowest_daily_mean_not_one_sample(self):  # J004-T12 finding 10
        glitch = END - tm.WEEK - timedelta(days=3)  # one 0 sample in the middle week (API glitch)
        s = sampled(lambda t: 0 if t == glitch else by_week(200, 300, 400)(t))
        f = tm.fade(s, s, AS_OF, TH)
        self.assertEqual(f["status"], "fade")
        self.assertAlmostEqual(f["troughs"][0], 200)

    def test_fade_changes_use_the_off_event_series(self):  # J004-T12 finding 10
        event = (END - 3 * tm.WEEK + timedelta(days=2), END - 3 * tm.WEEK + timedelta(days=3))  # oldest week
        s = sampled(lambda t: 3000 if event[0] <= t < event[1] else by_week(200, 310, 300)(t))
        off = [(t, v) for t, v in s if not event[0] <= t < event[1]]
        self.assertEqual(tm.fade(s, s, AS_OF, TH)["status"], "fade")  # the event week makes a false fall
        self.assertEqual(tm.fade(s, off, AS_OF, TH)["status"], "no fade")

    def test_playtime_estimate_is_labelled(self):
        ccu = sampled(lambda t: 120)
        visits = sampled(lambda t: 1000 + 10 * (t - ccu[0][0]) / timedelta(hours=1))
        p = tm.playtime_estimate(ccu, visits, END - tm.WEEK, END, TH)
        self.assertAlmostEqual(p["minutes_per_entry"], 60 * 120 / 10, places=3)  # 720 min per entry
        self.assertIn("estimate", p["label"])

    def test_approval_undefined_without_votes(self):
        self.assertIsNone(tm.approval(0, 0))
        self.assertAlmostEqual(tm.approval(3, 1), 0.75)


if __name__ == "__main__":
    unittest.main()
