#!/usr/bin/env python3
"""Offline tests for the outside page sections and the YouTube 30-day rule (records and pages), through the
trends.py command line with a temporary data dir. Records are synthetic."""
import json
import os
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "trends"))
import trend_store as st  # noqa: E402
import trends  # noqa: E402

AS_OF = datetime(2026, 10, 22, 6, 0, tzinfo=timezone.utc)  # week = 2026-10-15 .. 2026-10-21
EXTERNAL = re.compile(r"""(src|href)\s*=\s*["']?\s*(https?:)?//""", re.I)
WATCH = {"games": [], "outside": {"steam": {"apps": [{"app_id": "730", "label": "CS2 <b>"}]}}}


def rec(source, etype, eid, metric, value, unit, when, labels=None, prov="official"):
    return st.make_record(source=source, entity_type=etype, entity_id=eid, metric=metric, value=value, unit=unit,
                          observed_at_utc=st.utc_iso(when), provenance=prov, permission_version=f"{source}:test",
                          collector_version="test", labels=labels or {})


def outside_records():
    d = datetime(2026, 10, 20, 3, 0, tzinfo=timezone.utc)
    prev = d - timedelta(days=7)
    apple = [rec("apple.rss", "apple_app", "111", "rank", 1, "rank", d, {"name": "App One", "country": "us", "feed": "top-free"}),
             rec("apple.rss", "apple_app", "222", "rank", 2, "rank", d, {"name": "App Two", "country": "us", "feed": "top-free"}),
             rec("apple.rss", "apple_app", "111", "rank", 4, "rank", prev, {"name": "App One", "country": "us", "feed": "top-free"}),
             rec("apple.rss", "apple_app", "333", "rank", 1, "rank", prev, {"name": "App Gone", "country": "us", "feed": "top-free"})]
    steam = [rec("steam.current_players", "steam_app", "730", "current_players", v, "players", d + timedelta(minutes=30 * i))
             for i, v in enumerate((400000, 410000, 420000))]
    yt_labels = {"channel_id": "UCx", "published_at": "2026-10-18T15:00:00Z", "title": "Video A", "panel": "video"}
    youtube = [rec("youtube.data", "youtube_video", "vidA", "views", 1000, "views", d - timedelta(days=2), yt_labels),
               rec("youtube.data", "youtube_video", "vidA", "views", 5800, "views", d, yt_labels)]
    manual = [rec("google.play", "play_app", "com.example", "rank", 3, "rank", d,
                  {"region": "US", "page": "Top charts", "entity_name": "Example"}, prov="manual_entry")]
    return apple + steam + youtube + manual


class OutsidePage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        os.environ["TREND_DATA_DIR"] = self.tmp.name
        (self.base / "watchlist.json").write_text(json.dumps(WATCH), encoding="utf-8")

    def tearDown(self):
        del os.environ["TREND_DATA_DIR"]
        self.tmp.cleanup()

    def cli(self, *argv, now=AS_OF, code=0):
        """Run trends.py with its clock frozen at now (every command prunes first, J004-T12 finding 2)."""
        clock = mock.Mock(wraps=datetime, now=mock.Mock(return_value=now))
        with redirect_stdout(StringIO()) as out, redirect_stderr(StringIO()), mock.patch.object(trends, "datetime", clock):
            self.assertEqual(trends.main(list(argv)), code)
        return out.getvalue()

    def page(self):
        self.cli("page", "--as-of", st.utc_iso(AS_OF))
        pages = self.base / "pages"
        return ((pages / "trend-week-2026-10-21.md").read_text(encoding="utf-8"),
                (pages / "trend-week-2026-10-21.html").read_text(encoding="utf-8"))

    def test_sections_render_without_data(self):
        md, page = self.page()
        for title in ("Apple App Store ranks", "Steam current players", "YouTube panel view velocity",
                      "Manual entries this week"):
            self.assertIn(title, md)
            self.assertIn(title, page)
        self.assertEqual(md.count("No data this week."), 4)
        self.assertIn("steam.current_players: unclear", md)
        self.assertNotIn("storage-limit", md + page)
        self.assertIsNone(EXTERNAL.search(page))

    def test_sections_render_with_data_and_labels(self):
        st.append(outside_records())
        md, page = self.page()
        self.assertIn("| US top-free", md)
        self.assertRegex(md, r"\| 1 \| App One \(111\) \| 4 \| \+3 \|")
        self.assertRegex(md, r"\| 2 \| App Two \(222\) \| n/a \| new \|")
        self.assertRegex(md, r"\| out \| App Gone \(333\) \| 1 \| left \|")
        self.assertIn("not download or revenue growth", md)
        self.assertRegex(md, r"\| CS2 <b> \(730\) \| 420,000 \(2026-10-20 04:00\) \| 3 \| 410,000 \|")
        self.assertRegex(md, r"\| \+4,800 \| 48\.0 \| 100\.0 \|")  # 4,800 views over 48 h
        self.assertIn("| google.play | 2026-10-20 | US |", md)
        self.assertIn("[MAN]", md)
        self.assertIn("storage-limit source=youtube.data oldest=2026-10-18T03:00:00Z", page)
        self.assertIn("CS2 &lt;b&gt;", page)
        self.assertNotIn("CS2 <b>", page)
        self.assertEqual(page.count("<svg"), 2)  # Steam line, YouTube bars
        self.assertIsNone(EXTERNAL.search(page))

    def test_prune_removes_youtube_records_and_pages_after_30_days(self):
        st.append(outside_records())
        self.page()
        pages = self.base / "pages"
        self.cli("prune", "--now", "2026-11-17T02:00:00Z")  # 29 days 23 h after the oldest YouTube fetch
        self.assertEqual(len(st.read(source="youtube.data")), 2)
        self.assertEqual(len(list(pages.iterdir())), 2)
        out = self.cli("prune", "--now", "2026-11-17T04:00:00Z")
        self.assertEqual(len(st.read(source="youtube.data")), 1)  # the newer fetch is under 30 days
        self.assertEqual(list(pages.iterdir()), [])
        self.assertIn("deleted page", out)
        self.assertEqual(len(st.read(source="apple.rss")), 4)  # no storage limit: kept
        leftovers = [p for p in self.base.rglob("*") if p.is_file() and "vidA" in p.read_text(encoding="utf-8")
                     and p.name != "youtube.data.jsonl"]
        self.assertEqual(leftovers, [])

    def test_every_data_command_prunes_first(self):  # J004-T12 finding 2
        csv_in = self.base / "empty.csv"
        csv_in.write_text("source,read_date,page,entity_type,entity_id,metric\n", encoding="utf-8")
        later = datetime(2026, 11, 18, 4, 0, tzinfo=timezone.utc)  # 31 days after the oldest YouTube fetch
        for argv, code in ((["page"], 0), (["import-manual", str(csv_in)], 0), (["collect-steam"], 2)):
            with self.subTest(argv[0]):
                (self.base / "observations" / "youtube.data.jsonl").unlink(missing_ok=True)
                st.append([r for r in outside_records() if r["source"] == "youtube.data"])
                self.cli(*argv, now=later, code=code)
                self.assertEqual(len(st.read(source="youtube.data")), 1)  # the 29-day-old fetch stays

    def test_pages_folder_files_expire_30_days_after_last_change(self):  # J004-T12 finding 4
        now = datetime(2026, 10, 22, tzinfo=timezone.utc)
        pages = self.base / "pages"
        pages.mkdir()
        files = {"old": pages / "trend-week-2026-09-15-scout.md", "fresh": pages / "trend-week-2026-09-22-scout.md",
                 "log": self.base / "scout-log.md"}
        for name, days in (("old", 31), ("fresh", 29), ("log", 400)):
            files[name].write_text("no storage marker", encoding="utf-8")
            stamp = (now - timedelta(days=days)).timestamp()
            os.utime(files[name], (stamp, stamp))
        self.cli("prune", "--now", st.utc_iso(now), now=now)
        self.assertEqual({k: p.exists() for k, p in files.items()}, {"old": False, "fresh": True, "log": True})

    def test_latest_snapshot_shown_when_outside_the_week(self):  # J004-T12 F18 (scan note T3)
        after_week = datetime(2026, 10, 22, 3, 0, tzinfo=timezone.utc)  # after the week end, before as-of
        st.append([rec("apple.rss", "apple_app", "111", "rank", 1, "rank", after_week,
                       {"name": "App One", "country": "us", "feed": "top-free"})])
        md, _ = self.page()
        self.assertEqual(md.count("No data this week."), 3)  # Steam, YouTube, manual
        self.assertIn("| US top-free (latest snapshot (outside the week window, 2026-10-22 03:00 UTC)) | 1 | "
                      "App One (111) | n/a | n/a |", md)

    def test_permission_status_lists_every_source_used(self):  # J004-T12 F21 (scan note T12)
        md, _ = self.page()
        status = next(ln for ln in md.splitlines() if ln.startswith("- **PERMISSION STATUS:**"))
        for part in ("roblox.games: not_allowed", "apple.rss: allowed", "youtube.data: allowed",
                     "steam.current_players: unclear", "google.play: manual", "reddit: manual"):
            self.assertIn(part, status)


if __name__ == "__main__":
    unittest.main()
