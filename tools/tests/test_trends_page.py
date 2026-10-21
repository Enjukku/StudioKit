#!/usr/bin/env python3
"""Offline tests for tools/trends/trend_page.py (synthetic store records)."""
import os
import re
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trends"))
import trend_metrics as tm  # noqa: E402
import trend_page as tp  # noqa: E402
import trend_registry as reg  # noqa: E402
import trend_store as st  # noqa: E402

AS_OF = datetime(2026, 10, 22, 6, 0, tzinfo=timezone.utc)
END = datetime(2026, 10, 22, tzinfo=timezone.utc)
WATCH = [{"universe_id": "1", "root_place_id": "11", "label": "Rising <Game>", "event_windows": []}]
EXTERNAL = re.compile(r"""(src|href)\s*=\s*["']?\s*(https?:)?//""", re.I)


def records():
    out, t = [], END - timedelta(days=21)
    while t < END:
        ccu = 400 if t >= END - timedelta(days=7) else 200
        for metric, value, unit in (("playing", ccu, "players"), ("visits", (t - END).total_seconds() + 1e7, "visits")):
            out.append(st.make_record(source="roblox.games", entity_type="roblox_universe", entity_id="1",
                                      metric=metric, value=value, unit=unit, observed_at_utc=st.utc_iso(t),
                                      provenance="official", permission_version="p", collector_version="test"))
        t += timedelta(minutes=30)
    return out


def samples(uid, fn, start, end=END, step=timedelta(minutes=10), metric="playing", source="roblox.games", labels=None):
    """Records of one metric every step in [start, end]; fn(t) -> value, or None for no sample."""
    out, t = [], start
    while t <= end:
        if fn(t) is not None:
            out.append(st.make_record(source=source, entity_type="roblox_universe", entity_id=uid, metric=metric,
                                      value=fn(t), unit="players", observed_at_utc=st.utc_iso(t), provenance="official",
                                      permission_version="p", collector_version="test", labels=labels))
        t += step
    return out


TH = st.load_config()["thresholds"]


class Rows(unittest.TestCase):
    def test_young_game_is_an_emerging_lead_not_ranked_by_g7(self):  # J004-T12 finding 7
        watch = [{"universe_id": u, "label": None} for u in ("old", "young", "quiet")]
        recs = (samples("old", lambda t: 220 if t >= END - tm.WEEK else 200, END - timedelta(days=21))
                + samples("young", lambda t: 1000 if t >= END - tm.WEEK else 200, END - timedelta(days=8))
                + samples("quiet", lambda t: 300, END - timedelta(days=21), END - timedelta(days=8)))
        rows = {r["universe_id"]: r for r in tp.game_rows(recs, watch, AS_OF, TH)}
        self.assertEqual(rows["young"]["g7"], {"value": None, "status": "emerging lead (8 days)"})
        self.assertIsNone(rows["young"]["acceleration_pp"])
        self.assertEqual(rows["quiet"]["g7"]["status"], "no recent data")
        self.assertEqual([r["universe_id"] for r in tp.game_rows(recs, watch, AS_OF, TH)][0], "old")

    def test_24h_coverage_printed_and_momentum_held(self):  # J004-T12 finding 8
        recs = samples("1", lambda t: 3000 if t >= END - tm.HOUR else 1000, END - timedelta(days=21))
        recs = [r for r in recs if not END - tm.DAY - 2 * tm.HOUR < st.parse_utc(r["observed_at_utc"]) < END - tm.HOUR]
        md = tp.render_markdown(tp.game_rows(recs, WATCH, AS_OF, TH), AS_OF, reg.load(), TH)
        self.assertIn("| 3,000 (4%) |", md)  # 24 h mean with its coverage
        self.assertIn("| insufficient coverage (4%; momentum, not week-over-week) |", md)

    def test_approval_uses_votes_added_in_the_week(self):  # J004-T12 finding 9
        start = END - tm.WEEK + tm.HOUR
        recs = (samples("1", lambda t: 900 if t < END - tm.DAY else 910, start, END - tm.HOUR, timedelta(days=1),
                        "upvotes", "roblox.votes")
                + samples("1", lambda t: 100 if t < END - tm.DAY else 190, start, END - tm.HOUR, timedelta(days=1),
                          "downvotes", "roblox.votes"))
        row = tp.game_rows(recs, WATCH, AS_OF, TH)[0]
        self.assertAlmostEqual(row["approval"], 10 / 100)  # +10 up, +90 down this week; lifetime would be 82.7 %
        self.assertIn("approval of votes added (7d)", tp.render_markdown([row], AS_OF, reg.load(), TH))

    def test_event_windows_added_later_reach_old_records(self):  # J004-T12 finding 11
        event = (END - 3 * tm.WEEK + timedelta(days=2), END - 3 * tm.WEEK + timedelta(days=3))
        recs = samples("1", lambda t: 3000 if event[0] <= t < event[1] else 200 if t >= END - tm.WEEK else 310 if t >= END - 2 * tm.WEEK else 300,
                       END - timedelta(days=21))  # stored with event_flag false: the window was not known yet
        watch = [{**WATCH[0], "event_windows": [{"start_utc": st.utc_iso(event[0]), "end_utc": st.utc_iso(event[1])}]}]
        self.assertEqual(tp.game_rows(recs, watch, AS_OF, TH)[0]["fade"]["status"], "no fade")

    def test_samples_after_as_of_are_not_used(self):  # J004-T12 finding 13
        recs = records() + samples("1", lambda t: 5000, datetime(2026, 10, 25, 6, 0, tzinfo=timezone.utc),
                                   datetime(2026, 10, 25, 6, 0, tzinfo=timezone.utc))
        row = tp.game_rows(recs, WATCH, AS_OF, TH)[0]
        self.assertLessEqual(row["current"][0], AS_OF)
        self.assertNotIn("5,000", tp.render_markdown([row], AS_OF, reg.load(), TH))

    def test_api_name_shown_watchlist_label_only_a_note(self):  # J004-T12 F20 (scan note T10)
        watch = [{"universe_id": "1", "root_place_id": "11", "label": "check: event prefix?"}]
        recs = samples("1", lambda t: 100, END - timedelta(days=2), labels={"name": "Grow a Garden"})
        md = tp.render_markdown(tp.game_rows(recs, watch, AS_OF, TH), AS_OF, reg.load(), TH)
        self.assertIn("| Grow a Garden (1 / 11); watchlist label: check: event prefix? |", md)


class Page(unittest.TestCase):
    def render(self, recs):
        th = st.load_config()["thresholds"]
        with tempfile.TemporaryDirectory() as tmp:
            md, page = tp.write_pages(recs, WATCH, AS_OF, reg.load(), th, Path(tmp))
            self.assertEqual(md.name, "trend-week-2026-10-21.md")
            return md.read_text(encoding="utf-8"), page.read_text(encoding="utf-8")

    def test_renders_with_no_data(self):
        md, page = self.render([])
        self.assertIn("No data", md)
        self.assertIn("PERMISSION STATUS", md)
        self.assertIn("roblox.games: not_allowed", page)  # owner J004-D10
        self.assertIsNone(EXTERNAL.search(page))

    def test_renders_with_data(self):
        md, page = self.render(records())
        self.assertIn("breakout = breakout", md)
        self.assertRegex(md, r"\| \+99\.\d% / \+200 \|")  # step change; boundary segment is integrated
        self.assertIn("momentum, not week-over-week", md)
        self.assertIn("estimate", md)
        self.assertIn("<svg", page)
        self.assertIn("Rising &lt;Game&gt;", page)  # labels are escaped
        self.assertNotIn("<Game>", page)
        self.assertIsNone(EXTERNAL.search(page))
        self.assertNotIn("revenue:", page.lower())


if __name__ == "__main__":
    unittest.main()
