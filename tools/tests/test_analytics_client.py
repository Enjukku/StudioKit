#!/usr/bin/env python3
"""Offline tests for tools/analytics/ax_client.py: header-only key, missing key, 202 polling, retry rules from
the docs' errors table, rate-limit retry-after, read-only Experiments. No network: a fake fetch plays fixtures."""
import json
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "analytics"))
import ax_client as cl  # noqa: E402

FIX = HERE / "fixtures" / "analytics"
TEST_KEY = "TEST-not-a-real-key/+=Zq9"


def fixture(name: str) -> bytes:
    return (FIX / name).read_bytes()


class FakeFetch:
    """Plays a list of responses: (status, headers, body bytes) or an Exception instance to raise."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "headers": dict(headers), "body": body})
        if not self.responses:
            raise AssertionError(f"unexpected extra request {method} {url}")
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


def ok(name, status=200):
    return (status, {}, fixture(name))


def client(responses, **settings):
    fake = FakeFetch(responses)
    sleeps = []
    c = cl.Client(settings or None, fetch=fake, sleep=sleeps.append, clock=lambda: 0.0)
    return c, fake, sleeps


BODY = {"metric": "DailyActiveUsers", "granularity": "OneDay", "startTime": "2026-10-17T00:00:00Z",
        "endTime": "2026-10-21T00:00:00Z"}


class WithKey(unittest.TestCase):
    def setUp(self):
        p = mock.patch.dict(os.environ, {cl.KEY_ENV: TEST_KEY})
        p.start()
        self.addCleanup(p.stop)


class Analytics(WithKey):
    def test_202_then_done_polls_the_path_with_the_header(self):
        c, fake, sleeps = client([ok("metrics_202_pending.json", 202), ok("metrics_done_statuses.json")])
        data, path = c.query("1234567890", "metrics", BODY)
        self.assertTrue(data["done"])
        self.assertEqual(path, "v1/universes/1234567890/operations/metrics/testop1")
        self.assertEqual(fake.calls[0]["method"], "POST")
        self.assertEqual(fake.calls[0]["url"], "https://apis.roblox.com/analytics-query-api/v1/universes/1234567890/metrics")
        self.assertEqual(json.loads(fake.calls[0]["body"]), BODY)
        self.assertEqual(fake.calls[1]["method"], "GET")
        self.assertEqual(fake.calls[1]["url"],
                         "https://apis.roblox.com/analytics-query-api/v1/universes/1234567890/operations/metrics/testop1")
        for call in fake.calls:
            self.assertEqual(call["headers"]["x-api-key"], TEST_KEY)
            self.assertNotIn(TEST_KEY, call["url"])
        self.assertEqual(sleeps, [1.0])  # first poll wait

    def test_missing_key_makes_no_request(self):
        c, fake, _ = client([ok("metrics_done_statuses.json")])
        with mock.patch.dict(os.environ, {cl.KEY_ENV: ""}):
            with self.assertRaises(cl.MissingKey) as ctx:
                c.query("1234567890", "metrics", BODY)
        self.assertIn(cl.KEY_ENV, str(ctx.exception))
        self.assertEqual(fake.calls, [])

    def test_2002_and_2000_retried_bounded(self):
        c, fake, sleeps = client([(503, {}, fixture("error_2002.json")), (500, {}, fixture("error_2000.json")),
                                  ok("metrics_done_statuses.json")])
        data, _ = c.query("1", "metrics", BODY)
        self.assertTrue(data["done"])
        self.assertEqual(len(fake.calls), 3)
        self.assertIn(1.0, sleeps)
        self.assertIn(2.0, sleeps)
        c, fake, _ = client([(503, {}, fixture("error_2002.json"))] * 4)
        with self.assertRaises(cl.ApiError) as ctx:
            c.query("1", "metrics", BODY)
        self.assertEqual(len(fake.calls), 4)  # 1 + max_retries 3
        self.assertEqual(ctx.exception.code, 2002)

    def test_2001_401_403_404_never_retried(self):
        for status, body, kind in ((400, fixture("error_2001.json"), cl.ApiError), (401, b"", cl.AuthError),
                                   (403, b"", cl.AuthError), (404, b"", cl.ApiError)):
            c, fake, _ = client([(status, {}, body)])
            with self.assertRaises(kind) as ctx:
                c.query("1", "metrics", BODY)
            self.assertEqual(len(fake.calls), 1, status)
            self.assertNotIsInstance(ctx.exception, cl.SplitNeeded)
            if status in (401, 403):
                self.assertIn("universe.analytics:read", str(ctx.exception))

    def test_3000_raises_split_needed_without_retry(self):
        c, fake, _ = client([(429, {}, fixture("error_3000.json"))])
        with self.assertRaises(cl.SplitNeeded) as ctx:
            c.query("1", "metrics", BODY)
        self.assertEqual((ctx.exception.status, ctx.exception.code, len(fake.calls)), (429, 3000, 1))

    def test_plain_429_reads_retry_after_first(self):
        c, fake, sleeps = client([(429, {"Retry-After": "7"}, b""), (429, {}, b""), ok("metrics_done_statuses.json")])
        c.query("1", "metrics", BODY)
        self.assertEqual(sleeps[:2], [7.0, 2.0])  # header first, then backoff 1 s * 2^1
        c, fake, _ = client([(429, {"retry-after": "600"}, b"")])
        with self.assertRaises(cl.ApiError):
            c.query("1", "metrics", BODY)
        self.assertEqual(len(fake.calls), 1)

    def test_failed_operation_after_poll_and_poll_timeout(self):
        c, fake, _ = client([ok("metrics_202_pending.json", 202), ok("error_2001.json")])
        with self.assertRaises(cl.ApiError) as ctx:
            c.query("1", "metrics", BODY)
        self.assertEqual(ctx.exception.code, 2001)
        c, fake, sleeps = client([ok("metrics_202_pending.json", 202)] + [ok("metrics_202_pending.json")] * 50,
                                 poll_timeout_s=10.0)
        with self.assertRaises(cl.ApiError) as ctx:
            c.query("1", "metrics", BODY)
        self.assertIn("poll timeout", str(ctx.exception))
        self.assertLessEqual(sum(sleeps), 10.0 + 10.0)

    def test_post_pacing_two_seconds(self):
        clock = [0.0]
        fake = FakeFetch([ok("metrics_done_statuses.json")] * 2)
        sleeps = []
        c = cl.Client(fetch=fake, sleep=sleeps.append, clock=lambda: clock[0])
        c.query("1", "metrics", BODY)
        clock[0] = 0.5
        c.query("1", "metrics", BODY)
        self.assertEqual(sleeps, [1.5])


class Experiments(WithKey):
    def test_list_get_are_get_only(self):
        c, fake, _ = client([ok("experiments_list.json")])
        c.experiments_get("1234567890", "experiments", {"maxPageSize": 20, "skip": 0})
        self.assertEqual(fake.calls[0]["method"], "GET")
        self.assertTrue(fake.calls[0]["url"].startswith(
            "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/1234567890/experiments?"))
        with self.assertRaises(ValueError):
            c.experiments_get("1", "experiments/x:complete")

    def test_auth_message_names_scope(self):
        for status in (401, 403):
            c, fake, _ = client([(status, {}, b"")])
            with self.assertRaises(cl.AuthError) as ctx:
                c.experiments_get("1", "experiments")
            self.assertIn("key lacks universe:read for experiments", str(ctx.exception))

    def test_stats_operation_polled(self):
        c, fake, sleeps = client([ok("experiments_stats_done.json")])
        op = c.experiments_operation("1", json.loads(fixture("experiments_stats_pending.json")))
        self.assertEqual(op["experimentStats"], {"isSrmDetected": False})
        self.assertTrue(fake.calls[0]["url"].endswith("/universes/1/operations/testop5"))
        self.assertEqual(sleeps[0], 2.0)

    def test_no_write_method_exists(self):
        names = [n for n in dir(cl.Client) if not n.startswith("__")]
        self.assertFalse([n for n in names if any(w in n.lower() for w in
                                                  ("create", "start", "complete", "discard", "schedule", "update"))])


if __name__ == "__main__":
    unittest.main()
