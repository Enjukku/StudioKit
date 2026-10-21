#!/usr/bin/env python3
"""Offline tests for the manual-entry import (tools/trends/manual_import.py)."""
import csv
import os
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "trends"))
import manual_import as mi  # noqa: E402
import trend_registry as reg  # noqa: E402
import trend_store as st  # noqa: E402

NOW = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)
GOOD = {"source": "steam.charts", "read_date": "2026-10-20", "page": "https://store.steampowered.com/charts",
        "region": "global", "window": "now", "entity_type": "steam_app", "entity_id": "730",
        "entity_name": "Counter-Strike 2", "metric": "rank", "value": "1", "unit": "rank", "note": "free-to-play"}


class Import(unittest.TestCase):
    def run_import(self, rows):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            path = base / "in.csv"
            with path.open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=mi.COLUMNS)
                w.writeheader()
                w.writerows(rows)
            result = mi.import_csv(path, reg.load(), now=NOW, base=base)
            return result, st.read(base), mi.read_notes(base)

    def test_good_row_writes_one_manual_record(self):
        (n_rec, n_notes, _, rejected), recs, _ = self.run_import([GOOD])
        self.assertEqual((n_rec, n_notes, rejected), (1, 0, []))
        r = recs[0]
        self.assertEqual((r["source"], r["entity_id"], r["value"], r["provenance"]),
                         ("steam.charts", "730", 1, "manual_entry"))
        self.assertEqual(r["observed_at_utc"], "2026-10-20T00:00:00Z")
        self.assertEqual(r["labels"]["region"], "global")
        self.assertTrue(r["permission_version"].startswith("steam.charts:manual:"))

    def test_blank_value_is_a_note_not_a_zero(self):
        row = {**GOOD, "source": "release.calendars", "region": "", "entity_type": "title", "entity_id": "Show S2",
               "metric": "release_date_announced", "value": "", "unit": "", "note": "announced for 2026-12-01"}
        (n_rec, n_notes, _, rejected), recs, notes = self.run_import([row])
        self.assertEqual((n_rec, n_notes, rejected, recs), (0, 1, [], []))
        self.assertEqual(notes[0]["provenance"], "manual_entry")
        self.assertNotIn("value", notes[0])

    def test_each_bad_row_kind_is_rejected_with_reason(self):
        bad = {
            "not in the registry": {**GOOD, "source": "sensortower"},
            "not 'manual'": {**GOOD, "source": "apple.rss"},
            "not an ISO date": {**GOOD, "read_date": "20/10/2026"},
            "in the future": {**GOOD, "read_date": "2026-11-30"},
            "missing page": {**GOOD, "page": ""},
            "region is required": {**GOOD, "region": ""},
            "is not a number": {**GOOD, "value": "about 5"},
            "is not finite": {**GOOD, "value": "inf"},
            "unit is required": {**GOOD, "unit": ""},
            "looks like a username": {**GOOD, "source": "reddit", "entity_id": "u/someone", "note": ""},
            "no notes for discord": {**GOOD, "source": "discord", "note": "copied message"},
        }
        for reason, row in bad.items():
            with self.subTest(reason=reason):
                (n_rec, n_notes, _, rejected), recs, notes = self.run_import([row])
                self.assertEqual((n_rec, n_notes, recs, notes), (0, 0, [], []))
                self.assertEqual(len(rejected), 1)
                self.assertIn(reason, rejected[0])
                self.assertTrue(rejected[0].startswith("line 2:"))

    def test_bad_row_does_not_block_good_rows_and_comments_are_skipped(self):
        rows = [{**GOOD, "source": "# example"}, GOOD, {**GOOD, "value": "nan"}]
        (n_rec, _, _, rejected), recs, _ = self.run_import(rows)
        self.assertEqual((n_rec, len(recs), len(rejected)), (1, 1, 1))
        self.assertIn("line 4:", rejected[0])

    def test_reddit_discord_user_paths_rejected_in_any_field(self):  # J004-T12 finding 6
        topic = {**GOOD, "region": "", "entity_type": "topic", "entity_id": "obby tycoon", "entity_name": "",
                 "value": "", "unit": "", "note": ""}
        bad = {"page /user/": {"page": "https://www.reddit.com/user/SomeRealPerson/comments/abc"},
               "page /u/": {"source": "discord", "page": "https://www.reddit.com/u/SomeRealPerson"},
               "window u/": {"window": "thread by u/someone"},
               "entity_name @": {"source": "discord", "entity_name": "@someone"}}
        for name, change in bad.items():
            with self.subTest(name):
                (n_rec, n_notes, _, rejected), _, _ = self.run_import([{**topic, "source": "reddit", **change}])
                self.assertEqual((n_rec, n_notes, len(rejected)), (0, 0, 1))
                self.assertIn("looks like a username", rejected[0])

    def test_money_metric_needs_estimate_kind(self):  # J004-T12 finding 12
        row = {**GOOD, "source": "roblox.trackers", "region": "global", "entity_type": "roblox_universe",
               "entity_id": "123", "metric": "revenue_robux_per_day", "value": "50000", "unit": "robux", "note": ""}
        (n_rec, _, _, rejected), _, _ = self.run_import([row])
        self.assertEqual(n_rec, 0)
        self.assertIn("money metric needs kind", rejected[0])
        (n_rec, _, _, rejected), recs, _ = self.run_import([{**row, "kind": "third_party_estimate"}])
        self.assertEqual((n_rec, rejected, recs[0]["provenance"]), (1, [], "third_party_estimate"))
        (_, _, _, rejected), _, _ = self.run_import([{**GOOD, "kind": "guess"}])
        self.assertIn("kind 'guess'", rejected[0])

    def test_row_with_wrong_field_count_rejected_with_line(self):  # J004-T12 finding 14
        header = ",".join(mi.COLUMNS)
        good = "steam.charts,2026-10-20,charts,global,now,steam_app,730,CS2,rank,1,rank,,free-to-play"
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            path = base / "in.csv"
            path.write_text("\n".join([header, good + ", but top seller only in EU", good, "steam.charts,2026-10-20"]),
                            encoding="utf-8")
            n_rec, _, _, rejected = mi.import_csv(path, reg.load(), now=NOW, base=base)
        self.assertEqual(n_rec, 1)
        self.assertEqual([r.split(":")[0] for r in rejected], ["line 2", "line 4"])
        self.assertIn("14 fields, the header has 13", rejected[0])

    def test_reimport_skips_identical_rows(self):  # J004-T12 finding 15
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            path = base / "in.csv"
            with path.open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=mi.COLUMNS)
                w.writeheader()
                w.writerows([GOOD, {**GOOD, "entity_id": "570", "value": "2"}])
            first = mi.import_csv(path, reg.load(), now=NOW, base=base)
            again = mi.import_csv(path, reg.load(), now=NOW, base=base)
            self.assertEqual((first, again), ((2, 0, 0, []), (0, 0, 2, [])))
            self.assertEqual(len(st.read(base)), 2)

    def test_template_header_matches_columns(self):
        template = Path(HERE).parent / "trends" / "manual" / "manual-entries.template.csv"
        with template.open(encoding="utf-8") as fh:
            self.assertEqual(tuple(next(csv.reader(fh))), mi.COLUMNS)


if __name__ == "__main__":
    unittest.main()
