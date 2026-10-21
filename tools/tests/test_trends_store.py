#!/usr/bin/env python3
"""Offline tests for tools/trends/trend_store.py and trend_registry.py (temp dirs only)."""
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import date, datetime, timezone
from io import StringIO
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trends"))
import trend_registry as reg  # noqa: E402
import trend_store as st  # noqa: E402


def rec(when: str, value=10, source="roblox.games", **kw):
    return st.make_record(source=source, entity_type="roblox_universe", entity_id=1, metric="playing",
                          value=value, unit="players", observed_at_utc=when, provenance="official",
                          permission_version="roblox.games:allowed:2026-10-20", collector_version="test", **kw)


class Records(unittest.TestCase):
    def test_defaults_and_shape(self):
        r = rec("2026-10-20T00:00:00Z")
        self.assertEqual((r["observed_or_imputed"], r["source_sample_at_utc"], r["entity_id"]), ("observed", None, "1"))
        self.assertEqual(r["schema_version"], st.SCHEMA_VERSION)

    def test_rejects_non_finite_value_and_bad_provenance(self):
        for bad in (float("nan"), float("inf"), None, True):
            with self.assertRaises(ValueError):
                rec("2026-10-20T00:00:00Z", value=bad)
        with self.assertRaises(ValueError):
            st.make_record(source="s", entity_type="e", entity_id=1, metric="m", value=1, unit="u",
                           observed_at_utc="2026-10-20T00:00:00Z", provenance="guess",
                           permission_version="p", collector_version="c")

    def test_append_read_round_trip_sorted_and_filtered(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            st.append([rec("2026-10-20T02:00:00Z"), rec("2026-10-20T01:00:00Z")], base)
            got = st.read(base, source="roblox.games", start=st.parse_utc("2026-10-20T01:30:00Z"))
            self.assertEqual([r["observed_at_utc"] for r in got], ["2026-10-20T02:00:00Z"])
            self.assertEqual(len(st.read(base)), 2)

    def test_torn_line_is_skipped_by_read_and_dropped_by_prune(self):  # J004-T12 finding 3
        with tempfile.TemporaryDirectory() as tmp, redirect_stderr(StringIO()) as err:
            base = Path(tmp)
            st.append([rec("2026-08-01T00:00:00Z"), rec("2026-10-19T00:00:00Z")], base)
            path = base / "observations" / "roblox.games.jsonl"
            with path.open("a", encoding="utf-8") as fh:
                fh.write('{"source": "roblox.ga')  # process killed mid-write
            self.assertEqual(len(st.read(base)), 2)
            self.assertEqual(st.prune("roblox.games", 30, datetime(2026, 10, 20, tzinfo=timezone.utc), base), 1)
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 1)
        self.assertIn("unreadable line skipped", err.getvalue())

    def test_append_after_torn_line_starts_a_new_line(self):  # J004-T12 finding 3
        with tempfile.TemporaryDirectory() as tmp, redirect_stderr(StringIO()):
            base = Path(tmp)
            (base / "observations").mkdir()
            (base / "observations" / "roblox.games.jsonl").write_text('{"torn', encoding="utf-8")
            st.append([rec("2026-10-19T00:00:00Z")], base)
            self.assertEqual([r["observed_at_utc"] for r in st.read(base)], ["2026-10-19T00:00:00Z"])

    def test_prune_by_age(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            st.append([rec("2026-09-01T00:00:00Z"), rec("2026-10-19T00:00:00Z")], base)
            removed = st.prune("roblox.games", 30, datetime(2026, 10, 20, tzinfo=timezone.utc), base)
            self.assertEqual(removed, 1)
            self.assertEqual([r["observed_at_utc"] for r in st.read(base)], ["2026-10-19T00:00:00Z"])


class Registry(unittest.TestCase):
    def test_committed_registry_loads_with_roblox_rulings(self):
        rows = reg.load()
        for sid in ("roblox.games", "roblox.votes"):
            self.assertEqual(rows[sid]["ruling"], "not_allowed")  # owner J004-D10
        self.assertEqual(rows["roblox.place-universe"]["ruling"], "not_allowed")

    def test_refusal_unless_allowed(self):
        rows = {"a": {"id": "a", "ruling": "manual", "checked_on": "2026-10-20", "notes": ""}}
        with self.assertRaises(reg.PermissionRefused):
            reg.require_allowed(rows, "a")
        with self.assertRaises(reg.PermissionRefused):
            reg.require_allowed(rows, "missing")
        rows["a"]["ruling"] = "allowed"
        self.assertIs(reg.require_allowed(rows, "a"), rows["a"])

    def test_allowed_row_expires_after_valid_until(self):
        rows = {"a": {"id": "a", "ruling": "allowed", "checked_on": "2026-10-21", "notes": "",
                      "valid_until": "2026-10-31"}}
        self.assertIs(reg.require_allowed(rows, "a", today=date(2026, 10, 31)), rows["a"])
        with self.assertRaises(reg.PermissionRefused):
            reg.require_allowed(rows, "a", today=date(2026, 11, 1))

    def test_prune_all_uses_storage_limit_days(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            st.append([rec("2026-10-01T00:00:00Z", source="limited"), rec("2026-10-01T00:00:00Z", source="kept")], base)
            rows = {"limited": {"storage_limit_days": 7}, "kept": {"storage_limit_days": None}}
            removed, failed = reg.prune_all(rows, datetime(2026, 10, 20, tzinfo=timezone.utc), base)
            self.assertEqual((removed, failed), ({"limited": 1}, {}))
            self.assertEqual([r["source"] for r in st.read(base)], ["kept"])

    def test_prune_continues_past_a_locked_file(self):  # J004-T12 finding 3 (Windows lock while collecting)
        real_replace = os.replace

        def replace(src, dst):
            if str(dst).endswith("a.jsonl"):
                raise PermissionError(13, "file in use")
            return real_replace(src, dst)
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            st.append([rec("2026-10-01T00:00:00Z", source="a"), rec("2026-10-01T00:00:00Z", source="b")], base)
            rows = {"a": {"storage_limit_days": 7}, "b": {"storage_limit_days": 7}}
            with mock.patch.object(st.os, "replace", side_effect=replace):
                removed, failed = reg.prune_all(rows, datetime(2026, 10, 20, tzinfo=timezone.utc), base)
            self.assertEqual((removed, list(failed)), ({"b": 1}, ["a"]))
            self.assertEqual(sorted(p.name for p in (base / "observations").iterdir()), ["a.jsonl", "b.jsonl"])

    def test_malformed_row_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "sources.json"
            p.write_text(json.dumps({"sources": [{"id": "x", "ruling": "maybe"}]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                reg.load(p)


if __name__ == "__main__":
    unittest.main()
