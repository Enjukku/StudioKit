#!/usr/bin/env python3
"""Offline tests for the outside collectors (Apple RSS, Steam current players, YouTube Data API).

Fixtures in tools/tests/fixtures/trends/outside/: *.http are recorded responses (status line, headers,
body, CRLF); synthetic_youtube_*.json are built from documented field names (marked inside the file).
"""
import copy
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "trends"))
import apple_collector as ac  # noqa: E402
import steam_collector as sc  # noqa: E402
import trend_registry as reg  # noqa: E402
import trend_store as st  # noqa: E402
import trends  # noqa: E402
import youtube_collector as yc  # noqa: E402
from trend_keys import MissingKey  # noqa: E402

FIX = Path(HERE) / "fixtures" / "trends" / "outside"
WHEN = datetime(2026, 10, 21, 4, 0, tzinfo=timezone.utc)
SETTINGS = {"min_interval_s": 0, "batch_size": 10, "max_retries": 2, "backoff_base_s": 0.0,
            "max_retry_after_s": 60, "timeout_s": 5, "apple_max_retries": 0, "youtube_search_daily_budget": 2}
DUMMY = "DUMMY-steam-value-0123456789abcdef"


def http_fixture(name):
    """Recorded .http file -> (status, headers, body)."""
    head, _, body = (FIX / name).read_bytes().partition(b"\r\n\r\n")
    lines = head.decode("latin-1").split("\r\n")
    headers = dict(ln.split(": ", 1) for ln in lines[1:])
    return int(lines[0].split()[1]), headers, body


def rows_with(source, ruling):
    rows = copy.deepcopy(reg.load())
    rows[source]["ruling"] = ruling
    return rows


class Spy:
    """Injected fetch: route(url) -> (status, headers, body) or raises; records every URL."""

    def __init__(self, route):
        self.calls, self.route = [], route

    def __call__(self, url, headers, timeout):
        self.calls.append(url)
        return self.route(url)


def quiet(log=lambda line: None):
    return {"now": lambda: WHEN, "log": log}


class Refusal(unittest.TestCase):
    def test_each_collector_refuses_without_request_when_not_allowed(self):
        for module, source in ((ac, "apple.rss"), (sc, "steam.current_players"), (yc, "youtube.data")):
            spy = Spy(lambda url: (200, {}, b"{}"))
            with self.subTest(source=source), self.assertRaises(reg.PermissionRefused):
                module.collect({}, rows_with(source, "unclear"), SETTINGS, fetch=spy, **quiet())
            self.assertEqual(spy.calls, [])

    def test_steam_unclear_cli_exits_refused_with_key_set(self):
        spy = Spy(lambda url: http_fixture("steam_GetNumberOfCurrentPlayers_appid730.http"))
        with tempfile.TemporaryDirectory() as tmp:
            wl = Path(tmp) / "watchlist.json"
            wl.write_text(json.dumps({"games": [], "outside": {"steam": {"apps": [{"app_id": "730"}]}}}), "utf-8")
            os.environ.update(TREND_DATA_DIR=tmp, STEAM_WEB_API_KEY=DUMMY)
            try:
                with redirect_stderr(StringIO()) as err:
                    code = trends.main(["collect-steam", "--watchlist", str(wl)], fetch=spy)
            finally:
                del os.environ["TREND_DATA_DIR"], os.environ["STEAM_WEB_API_KEY"]
        self.assertEqual(reg.load()["steam.current_players"]["ruling"], "unclear")
        self.assertEqual(code, trends.EXIT_REFUSED)
        self.assertEqual(spy.calls, [])
        self.assertIn("REFUSED", err.getvalue())
        self.assertNotIn(DUMMY, err.getvalue())


class Apple(unittest.TestCase):
    def test_parse_recorded_feeds(self):
        row = rows_with("apple.rss", "allowed")["apple.rss"]
        for feed in ("top-free", "top-paid"):
            _, _, body = http_fixture(f"apple_rss_us_apps_{feed}_10.http")
            recs = ac.parse(body, row, "us", feed, WHEN)
            self.assertEqual([r["value"] for r in recs], list(range(1, 11)))
            r = recs[0]
            self.assertEqual((r["entity_type"], r["metric"], r["provenance"]), ("apple_app", "rank", "official"))
            self.assertTrue(r["entity_id"].isdigit())
            self.assertEqual((r["labels"]["country"], r["labels"]["feed"]), ("us", feed))
            self.assertNotIn("genres", r["labels"])  # feed lists no genres: never labelled a game
            self.assertEqual(r["permission_version"], "apple.rss:allowed:2026-10-20")
        self.assertEqual(recs[0]["source_sample_at_utc"], "2026-10-21T03:53:55Z")

    def test_504_writes_nothing_and_does_not_retry(self):
        spy = Spy(lambda url: http_fixture("apple_rss_us_apps_top-grossing_10.http"))
        logs = []
        recs = ac.collect({"countries": ["us"], "feeds": ["top-free"], "limit": 10},
                          rows_with("apple.rss", "allowed"), SETTINGS, fetch=spy, **quiet(log=logs.append))
        self.assertEqual(recs, [])
        self.assertEqual(spy.calls, ["https://rss.marketingtools.apple.com/api/v2/us/apps/top-free/10/apps.json"])
        self.assertIn("HTTP 504", logs[0])


    def test_skipped_items_and_feed_length_are_logged(self):  # J004-T12 F19 (scan note T8)
        items = [{"id": "111", "name": "A"}, {"id": "id-not-digits", "name": "B"}, {"id": "333", "name": "C"}]
        body = json.dumps({"feed": {"country": "gb", "results": items}}).encode()
        logs = []
        recs = ac.collect({"countries": ["gb"], "feeds": ["top-paid"], "limit": 25}, rows_with("apple.rss", "allowed"),
                          SETTINGS, fetch=Spy(lambda url: (200, {}, body)), **quiet(log=logs.append))
        self.assertEqual(len(recs), 2)
        self.assertIn("apple gb/top-paid: feed listed 3 items; stored 2; skipped 1 (id not numeric)", logs)


class Steam(unittest.TestCase):
    def setUp(self):
        os.environ["STEAM_WEB_API_KEY"] = DUMMY
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self):
        del os.environ["STEAM_WEB_API_KEY"]
        self.tmp.cleanup()

    def test_key_never_in_records_logs_or_errors(self):
        def route(url):
            if "appid=730" in url:
                return http_fixture("steam_GetNumberOfCurrentPlayers_appid730.http")
            if "appid=440" in url:
                raise OSError(f"connection reset while fetching {url}")
            return 403, {}, b"Forbidden"
        spy = Spy(route)
        logs = []
        panel = {"apps": [{"app_id": "730", "label": "CS2"}, {"app_id": "440"}, {"app_id": "570"}]}
        recs = sc.collect(panel, rows_with("steam.current_players", "allowed"), SETTINGS, fetch=spy,
                          base=self.base, **quiet(log=logs.append))
        self.assertTrue(all(f"key={DUMMY}" in url for url in spy.calls))  # the request itself carries it
        self.assertEqual([(r["entity_id"], r["value"]) for r in recs], [("730", 408548)])  # fail soft
        self.assertEqual(recs[0]["source_sample_at_utc"], "2026-10-21T03:52:11Z")
        self.assertEqual(recs[0]["labels"]["fresh_until_utc"], "2026-10-21T04:07:01Z")  # max-age 421 s
        self.assertEqual(len(logs), 2)
        st.append(recs, self.base)
        stored = "".join(p.read_text(encoding="utf-8") for p in self.base.rglob("*") if p.is_file())
        for text in [json.dumps(recs), "\n".join(logs), stored]:
            self.assertNotIn(DUMMY, text)
        self.assertIn("<redacted>", "\n".join(logs))

    def test_cache_control_skips_until_fresh(self):
        spy = Spy(lambda url: http_fixture("steam_GetNumberOfCurrentPlayers_appid730.http"))
        panel = {"apps": [{"app_id": "730"}]}
        rows = rows_with("steam.current_players", "allowed")
        st.append(sc.collect(panel, rows, SETTINGS, fetch=spy, base=self.base, **quiet()), self.base)
        again = sc.collect(panel, rows, SETTINGS, fetch=spy, base=self.base, now=lambda: WHEN + timedelta(minutes=5),
                           log=lambda line: None)
        later = sc.collect(panel, rows, SETTINGS, fetch=spy, base=self.base, now=lambda: WHEN + timedelta(minutes=8),
                           log=lambda line: None)
        self.assertEqual((len(again), len(later), len(spy.calls)), (0, 1, 2))

    def test_missing_key_makes_no_request(self):
        del os.environ["STEAM_WEB_API_KEY"]
        spy = Spy(lambda url: (200, {}, b"{}"))
        with self.assertRaises(MissingKey):
            sc.collect({"apps": [{"app_id": "730"}]}, rows_with("steam.current_players", "allowed"), SETTINGS,
                       fetch=spy, base=self.base, **quiet())
        os.environ["STEAM_WEB_API_KEY"] = DUMMY
        self.assertEqual(spy.calls, [])


class YouTube(unittest.TestCase):
    PANEL = {"channels": [{"channel_id": "UCsynthetic000000000001"}], "videos": ["vidB0000002"],
             "queries": [{"q": "obby", "days": 7}, {"q": "tycoon"}, {"q": "horror"}], "uploads_per_channel": 5}

    def setUp(self):
        os.environ["YOUTUBE_API_KEY"] = "DUMMY-youtube-value-abcdef"
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self):
        del os.environ["YOUTUBE_API_KEY"]
        self.tmp.cleanup()

    @staticmethod
    def route(url):
        method = url.split("/youtube/v3/")[1].split("?")[0]
        return 200, {}, (FIX / f"synthetic_youtube_{method}.json").read_bytes()

    def collect(self, spy, now=WHEN, logs=None):
        return yc.collect(self.PANEL, rows_with("youtube.data", "allowed"), SETTINGS, fetch=spy, base=self.base,
                          now=lambda: now, log=(logs if logs is not None else []).append)

    def test_panel_records_per_video(self):
        spy = Spy(self.route)
        recs = self.collect(spy)
        got = {(r["entity_id"], r["metric"]): r["value"] for r in recs}
        self.assertEqual(got[("vidA0000001", "views")], 120000)
        self.assertNotIn(("vidB0000002", "likes"), got)  # hidden count: no record, no zero
        self.assertEqual(len({r["entity_id"] for r in recs}), 3)  # vidA deduplicated
        a = next(r for r in recs if r["entity_id"] == "vidA0000001")
        self.assertEqual(a["labels"]["panel"], "channel:UCsynthetic000000000001,query:obby,query:tycoon")
        self.assertNotIn("channelTitle", json.dumps(recs))  # creators only by channel id
        self.assertEqual(sum("/videos?" in u for u in spy.calls), 1)  # one statistics batch
        self.assertNotIn("DUMMY-youtube", json.dumps(recs))

    def test_search_budget_holds_across_runs(self):
        spy, logs = Spy(self.route), []
        self.collect(spy, logs=logs)
        self.collect(spy, now=WHEN + timedelta(hours=2), logs=logs)
        self.assertEqual(sum("/search?" in u for u in spy.calls), SETTINGS["youtube_search_daily_budget"])
        self.assertEqual(sum("daily search budget" in ln for ln in logs), 4)
        self.collect(spy, now=WHEN + timedelta(hours=25))  # trailing 24 h window has passed
        self.assertEqual(sum("/search?" in u for u in spy.calls), 2 * SETTINGS["youtube_search_daily_budget"])


if __name__ == "__main__":
    unittest.main()
