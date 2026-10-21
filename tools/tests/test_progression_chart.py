"""Offline tests for tools/progression/chart.py (reports made by sim.py from the test fixtures)."""

import contextlib
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "progression"))
import chart  # noqa: E402
import sim  # noqa: E402

FIX = ROOT / "tools" / "tests" / "fixtures" / "progression"
EXTERNAL = re.compile(r"""(?:src|href)\s*=\s*["']?\s*(?:https?:)?//""", re.I)


def report(name, policy, **kw):
    return sim.simulate(FIX / f"{name}.json", policy, model_path_label=f"{name}.json", **kw)


class Page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reps = [report("rpg_duel", "fight-best"), report("rpg_duel", "grind-to-level", target_level=4),
                    report("rpg_duel", "fight-best", skill="struggling")]
        cls.page = chart.render(cls.reps)

    def test_self_contained_no_network_urls(self):
        self.assertIsNone(EXTERNAL.search(self.page))
        sample = ROOT / "output" / "progression" / "j011-t07" / "sample.html"  # delivered sample (gitignored)
        if sample.is_file():
            text = sample.read_text(encoding="utf-8")
            self.assertIsNone(EXTERNAL.search(text))
            self.assertIn('id="assumptions"', text)
        self.assertNotIn("<script", self.page.lower())
        self.assertNotIn("<link", self.page.lower())
        self.assertIn("<svg", self.page)

    def test_assumptions_panel_and_run_identity(self):
        self.assertIn('id="assumptions"', self.page)
        self.assertIn("enemies.slime.hp", self.page)  # an EXAMPLE ASSUMPTION input is listed by name
        self.assertIn("fixture-rpg-duel-r1", self.page)
        self.assertIn(self.reps[0]["model"]["sha256"][:16], self.page)
        self.assertIn(f"sim {sim.VERSION}", self.page)

    def test_one_timeline_row_per_policy_with_marks(self):
        self.assertEqual(self.page.count('class="row-label"'), 3)
        self.assertIn("skill_profile struggling", self.page)
        self.assertIn('class="soft"', self.page)
        self.assertIn('class="spike"', self.page)
        self.assertIn("level3 window: pass", self.page)

    def test_curves_and_tables(self):
        for title in ("XP to next level", "Cumulative XP at level start", "Hits to kill per level"):
            self.assertIn(title, self.page)
        self.assertIn("<details><summary>Table</summary>", self.page)

    def test_light_and_dark_tokens(self):
        self.assertIn("prefers-color-scheme:dark", self.page)
        self.assertIn(':root[data-theme="dark"]', self.page)
        self.assertIn("width=device-width", self.page)


class Details(unittest.TestCase):
    def test_model_strings_are_escaped(self):
        m = json.loads((FIX / "zero_income.json").read_text(encoding="utf-8"))
        m["meta"]["title"] = "<script>alert(1)</script>"
        m["goals"][0]["label"] = '"><img src=x onerror=alert(1)>'
        rep = sim.simulate(m, "cheapest-eligible", model_path_label="z.json")
        page = chart.render([rep])
        self.assertNotIn("<script>alert", page)
        self.assertNotIn("<img", page)
        self.assertIn("&lt;script&gt;", page)

    def test_blocked_and_hard_wall_shown(self):
        page = chart.render([report("zero_income", "cheapest-eligible")])
        self.assertIn("unreachable: zero income", page)
        page = chart.render([report("idle_prestige", "save-for", target="factory")])
        self.assertIn('class="hard"', page)
        self.assertIn("prestige", page)

    def test_log_scale_when_values_span_more_than_three_orders(self):
        curve = {"id": "c", "title": "big", "x": "n", "y": "price", "points": [[0, 1], [1, 10], [2, 100], [3, 10000]]}
        self.assertIn("(log scale)", chart.curve_svg(curve))
        small = dict(curve, points=[[0, 1], [1, 2], [2, 3]])
        self.assertNotIn("(log scale)", chart.curve_svg(small))

    def test_calendar_timeline_when_sessions_ran(self):
        page = chart.render([report("sessions_offline", "cheapest-eligible", sessions="regular")])
        self.assertIn("Timeline (calendar time", page)

    def test_rejects_non_report(self):
        with self.assertRaises(ValueError):
            chart.render([{"tool": "other"}])

    def test_cli_writes_one_file(self):
        with tempfile.TemporaryDirectory() as d:
            r = Path(d) / "r.json"
            r.write_text(sim.dumps(report("lemonade_m01", "buy-next-in-order")), encoding="utf-8")
            out = Path(d) / "sub" / "page.html"
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(chart.main([str(r), "--out", str(out)]), 0)
            text = out.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("<!doctype html>"))
            self.assertIsNone(EXTERNAL.search(text))



class T11Chart(unittest.TestCase):
    """J011-T11 G-06: resets, wait per step, reference metrics over time, calendar walls and rows, revisions."""

    def test_G06_reset_marks_waits_and_metric_plots(self):
        page = chart.render([report("idle_prestige", "greedy-roi"), report("idle_prestige", "save-for", target="factory")])
        self.assertIn('class="reset"', page)
        self.assertIn("reset (prestige) 1 at", page)
        self.assertIn("Wait per step", page)
        self.assertIn("Reference metrics over time", page)
        self.assertIn("cash_rate: production_per_s vs cash", page)
        self.assertIn("· model fixture-idle-prestige-r1", page)
        self.assertIsNone(EXTERNAL.search(page))

    def test_G06_calendar_axis_has_walls_and_only_session_runs(self):
        m = json.loads((FIX / "idle_prestige.json").read_text(encoding="utf-8"))
        ea = "EXAMPLE ASSUMPTION"
        m["sessions"] = {"patterns": {"daily": {"active_s": {"v": 60, "src": ea}, "gaps_s": {"v": [3600], "src": ea}}}}
        with_sessions = sim.simulate(m, "greedy-roi", sessions="daily", model_path_label="idle+sessions")
        without = report("idle_prestige", "greedy-roi")
        page = chart.render([with_sessions, without])
        cal = page[page.index("Timeline (calendar time"):]
        cal = cal[:cal.index("</svg>")]
        self.assertEqual(cal.count('class="row-label"'), 1)  # the run without sessions has no calendar row
        self.assertIn('class="soft"', cal)
        self.assertIn('class="hard"', cal)

    def test_G06_t07_reports_still_render(self):
        rep = report("idle_prestige", "save-for", target="factory")
        for w in rep["walls"]["soft"]["walls"]:
            del w["start_calendar_s"]
        for w in rep["walls"]["hard"]:
            for k in ("end_calendar_s", "kind", "condition", "pursued_by_policy"):
                w.pop(k, None)
        self.assertIn("<svg", chart.render([rep]))

if __name__ == "__main__":
    unittest.main()
