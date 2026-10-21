#!/usr/bin/env python3
"""Offline tests for the Roblox collector and polite HTTP (recorded and synthetic fixtures; no network).

Fixtures in tools/tests/fixtures/trends/roblox/: games_v1_games.json is a recorded response;
synthetic_*.json are built from documented field names (marked inside the file).
"""
import copy
import http.client
import json
import os
import random
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import datetime, timezone
from io import StringIO
from unittest import mock
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "trends"))
import roblox_collector as rc  # noqa: E402
import trend_registry as reg  # noqa: E402
import trends  # noqa: E402
from trend_http import FetchFailed, PoliteClient  # noqa: E402

FIX = Path(HERE) / "fixtures" / "trends" / "roblox"
UID = "7436755782"
WHEN = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
SETTINGS = {"min_interval_s": 0, "batch_size": 10, "max_retries": 3, "backoff_base_s": 1.0,
            "max_retry_after_s": 60, "timeout_s": 5}
GAME = {"universe_id": UID, "root_place_id": None, "label": "Grow a Garden",
        "event_windows": [{"start_utc": "2026-10-20T11:00:00Z", "end_utc": "2026-10-20T13:00:00Z"}]}


def allowed_rows():
    rows = copy.deepcopy(reg.load())
    for row in rows.values():
        row["ruling"] = "allowed"
        row.pop("valid_until", None)  # expiry has its own test (test_trends_store); keep these date-independent
    return rows


class Spy:
    """Injected fetch: returns queued (status, headers, body) or routes by URL; records every call."""

    def __init__(self, responses=None):
        self.calls, self.responses = [], list(responses or [])

    def __call__(self, url, headers, timeout):
        self.calls.append((url, headers))
        if self.responses:
            return self.responses.pop(0)
        name = "synthetic_games_votes.json" if "/votes" in url else "games_v1_games.json"
        return 200, {}, (FIX / name).read_bytes()


class Parsing(unittest.TestCase):
    def test_recorded_games_response(self):
        recs = rc.parse_games((FIX / "games_v1_games.json").read_bytes(), allowed_rows()["roblox.games"], WHEN,
                              {UID: GAME})
        got = {r["metric"]: r["value"] for r in recs}
        self.assertEqual(set(got), {"playing", "visits", "favorites"})
        r = recs[0]
        self.assertEqual((r["entity_id"], r["provenance"], r["source_sample_at_utc"]), (UID, "official", None))
        self.assertEqual(r["labels"]["root_place_id"], "126884695634066")
        self.assertTrue(r["event_flag"])
        self.assertEqual(r["permission_version"], reg.permission_version(allowed_rows()["roblox.games"]))

    def test_bad_or_missing_values_write_no_record(self):
        body = json.dumps({"data": [{"id": int(UID), "playing": None, "visits": -1, "favoritedCount": 5},
                                    {"id": 999, "playing": 3}]}).encode()
        recs = rc.parse_games(body, allowed_rows()["roblox.games"], WHEN, {UID: GAME})
        self.assertEqual([(r["metric"], r["entity_id"]) for r in recs], [("favorites", UID)])


class Permission(unittest.TestCase):
    def test_unclear_ruling_refuses_without_any_request(self):
        spy = Spy()
        unclear = copy.deepcopy(reg.load())
        for sid in ("roblox.games", "roblox.votes"):
            unclear[sid]["ruling"] = "unclear"
        with tempfile.TemporaryDirectory() as tmp:
            wl = Path(tmp) / "watchlist.json"
            wl.write_text(json.dumps({"games": [GAME]}), encoding="utf-8")
            os.environ["TREND_DATA_DIR"] = tmp
            try:
                with redirect_stderr(StringIO()) as err, mock.patch.object(trends.trend_registry, "load",
                                                                           return_value=unclear):
                    code = trends.main(["collect-roblox", "--watchlist", str(wl)], fetch=spy)
            finally:
                del os.environ["TREND_DATA_DIR"]
            self.assertFalse((Path(tmp) / "observations").exists())
        self.assertEqual(code, trends.EXIT_REFUSED)
        self.assertEqual(spy.calls, [])
        self.assertIn("REFUSED", err.getvalue())

    def test_allowed_collect_batches_and_names_tool(self):
        spy = Spy()
        recs = rc.collect([GAME], allowed_rows(), PoliteClient(SETTINGS, fetch=spy, sleep=lambda s: None), 10,
                          now=lambda: WHEN)
        self.assertEqual(len(spy.calls), 2)  # one games call, one votes call for the batch
        self.assertIn("universeIds=" + UID, spy.calls[0][0])
        self.assertIn("StudioKit-TrendScout", spy.calls[0][1]["User-Agent"])
        self.assertNotIn("Cookie", spy.calls[0][1])
        self.assertEqual(sorted(r["metric"] for r in recs),
                         ["downvotes", "favorites", "playing", "upvotes", "visits"])


class Politeness(unittest.TestCase):
    def test_429_honours_retry_after(self):
        sleeps = []
        spy = Spy([(429, {"Retry-After": "7"}, b""), (200, {}, b"ok")])
        client = PoliteClient(SETTINGS, fetch=spy, sleep=sleeps.append, clock=lambda: 0.0)
        self.assertEqual(client.get("https://example.invalid/x"), b"ok")
        self.assertEqual(sleeps, [7.0])

    def test_backoff_is_bounded(self):
        sleeps = []
        spy = Spy([(503, {}, b"")] * 10)
        client = PoliteClient(SETTINGS, fetch=spy, sleep=sleeps.append, clock=lambda: 0.0, rng=random.Random(1))
        with self.assertRaises(FetchFailed):
            client.get("https://example.invalid/x")
        self.assertEqual(len(spy.calls), SETTINGS["max_retries"] + 1)
        self.assertEqual(len(sleeps), SETTINGS["max_retries"])
        for i, s in enumerate(sleeps):  # base * 2^i plus jitter in [0, base]
            self.assertTrue(2 ** i <= s <= 2 ** i + 1)

    def test_long_retry_after_stops(self):
        spy = Spy([(429, {"Retry-After": "3600"}, b"")])
        with self.assertRaises(FetchFailed):
            PoliteClient(SETTINGS, fetch=spy, sleep=lambda s: None).get("https://example.invalid/x")
        self.assertEqual(len(spy.calls), 1)

    def test_429_stop_ends_the_run_for_the_source(self):  # J004-T12 finding 1
        games = [{"universe_id": str(1000 + i), "label": None} for i in range(30)]
        cases = {"Retry-After over the max": ([(429, {"Retry-After": "900"}, b"")] * 50, 1),
                 "429 after every retry": ([(429, {}, b"")] * 50, SETTINGS["max_retries"] + 1)}
        for name, (responses, requests) in cases.items():
            with self.subTest(name):
                spy, logs = Spy(responses), []
                client = PoliteClient(SETTINGS, fetch=spy, sleep=lambda s: None, rng=random.Random(1))
                recs = rc.collect(games, allowed_rows(), client, 10, now=lambda: WHEN, log=logs.append)
                self.assertEqual((len(spy.calls), recs), (requests, []))
                self.assertTrue(any(line.startswith("stopped:") for line in logs))

    def test_batch_never_exceeds_50_ids(self):  # J004-T12 finding 5
        games = [{"universe_id": str(1000 + i), "label": None} for i in range(120)]
        spy = Spy([(200, {}, b'{"data": []}')] * 6)
        rc.collect(games, allowed_rows(), PoliteClient(SETTINGS, fetch=spy, sleep=lambda s: None), 100,
                   now=lambda: WHEN, log=lambda line: None)
        self.assertEqual([len(url.split("universeIds=")[1].split(",")) for url, _ in spy.calls], [50, 50, 50, 50, 20, 20])

    def test_dropped_connection_fails_only_that_request(self):  # J004-T12 finding 16
        def fetch(url, headers, timeout):
            calls.append(url)
            if "universeIds=999" in url and "/votes" not in url:
                raise http.client.IncompleteRead(b'{"da')
            name = "synthetic_games_votes.json" if "/votes" in url else "games_v1_games.json"
            return 200, {}, (FIX / name).read_bytes()
        calls, logs = [], []
        games = [GAME, {"universe_id": "999", "label": "Other"}]
        recs = rc.collect(games, allowed_rows(), PoliteClient(SETTINGS, fetch=fetch, sleep=lambda s: None), 1,
                          now=lambda: WHEN, log=logs.append)
        self.assertTrue({"playing", "visits", "favorites"} <= {r["metric"] for r in recs if r["entity_id"] == UID})
        self.assertIn("https://games.roblox.com/v1/games/votes?universeIds=999", calls)  # the run went on
        self.assertTrue(any("IncompleteRead" in line for line in logs))


class Removed(unittest.TestCase):
    def test_resolve_place_command_removed(self):  # J004-T12 finding 17: route ruled not_allowed
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit):
            trends.main(["resolve-place", "126884695634066"], fetch=Spy())
        self.assertFalse(hasattr(rc, "resolve_place") or hasattr(rc, "parse_place_universe"))
        self.assertEqual(reg.load()["roblox.place-universe"]["ruling"], "not_allowed")  # the row stays


if __name__ == "__main__":
    unittest.main()
