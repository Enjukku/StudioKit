#!/usr/bin/env python3
"""Planted-key test (J013-T04 C2): a fake key is set in the environment, every command path runs against fake
responses that echo the key back (network error text, error bodies, failed polls, poll timeout, auth errors),
and the key must appear in no stdout, stderr, exception text, URL, request body or file under the data dir.
Add a print of the key anywhere in tools/analytics and this test fails."""
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "analytics"))
import analytics  # noqa: E402
import ax_client as cl  # noqa: E402
from test_analytics_client import FakeFetch, fixture, ok  # noqa: E402

PLANTED = "TEST-PLANTED-k3y/+=9zQ-do-not-leak"
FORMS = (PLANTED, quote(PLANTED, safe=""), json.dumps(PLANTED)[1:-1])


def echo_error(status, code):
    body = {"done": True, "error": {"code": code, "message": f"bad key {PLANTED} sent as {quote(PLANTED, safe='')}"}}
    return (status, {}, json.dumps(body).encode())


class PlantedKey(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        p = mock.patch.dict(os.environ, {cl.KEY_ENV: PLANTED, "ANALYTICS_DATA_DIR": str(self.dir)})
        p.start()
        self.addCleanup(p.stop)
        self.fakes = []
        self.texts = []

    def run_cli(self, argv, responses, **settings):
        fake = FakeFetch(responses)
        self.fakes.append(fake)

        def make():
            cl.read_key()
            return cl.Client(settings or None, fetch=fake, sleep=lambda s: None, clock=lambda: 0.0)
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(analytics, "_client", make), redirect_stdout(out), redirect_stderr(err):
            try:
                code = analytics.main(argv)
            except BaseException as exc:  # noqa: BLE001 - the text of any escaping exception is checked too
                self.texts.append(repr(exc))
                code = None
        self.texts += [out.getvalue(), err.getvalue()]
        return code

    def assert_no_key_anywhere(self):
        for text in self.texts:
            for form in FORMS:
                self.assertNotIn(form, text)
        files = [p for p in self.dir.rglob("*") if p.is_file()]
        self.assertTrue(files, "the scenarios should have written history")
        for path in files:
            data = path.read_bytes()
            for form in FORMS:
                self.assertNotIn(form.encode(), data, path)
        for fake in self.fakes:
            for call in fake.calls:
                self.assertEqual(call["headers"].get("x-api-key"), PLANTED)  # the header is the only place
                for form in FORMS:
                    self.assertNotIn(form, call["url"])
                    self.assertNotIn(form.encode(), call["body"] or b"")

    def test_key_never_leaks(self):
        u = ["--universe", "1234567890", "--now", "2026-10-21T12:00:00Z"]
        network = OSError(f"connect failed for x-api-key: {PLANTED} ({quote(PLANTED, safe='')})")
        # weekly: network error (echoes key), 500/2000 x4 (echo), 503/2002 then ok, then 401 (echo) stops the run
        self.run_cli(["pull", "--set", "weekly", *u],
                     [network] + [echo_error(500, 2000)] * 4 + [echo_error(503, 2002), ok("metrics_done_statuses.json"),
                                                                echo_error(401, None)])
        # failed poll: 202 then done:true with an error that echoes the key
        self.run_cli(["pull-metric", "--metric", "Visits", "--granularity", "OneDay", "--start", "2026-10-01T00:00:00Z",
                      "--end", "2026-10-05T00:00:00Z", *u],
                     [ok("metrics_202_pending.json", 202), echo_error(200, 2001)])
        # poll timeout
        self.run_cli(["pull-metric", "--metric", "Visits", "--granularity", "OneDay", "--start", "2026-10-01T00:00:00Z",
                      "--end", "2026-10-05T00:00:00Z", *u],
                     [ok("metrics_202_pending.json", 202)] + [ok("metrics_202_pending.json")] * 10, poll_timeout_s=3.0)
        # 3000 on a single bucket, echoing the key
        self.run_cli(["pull-metric", "--metric", "Visits", "--granularity", "OneDay", "--start", "2026-10-01T00:00:00Z",
                      "--end", "2026-10-02T00:00:00Z", *u], [echo_error(429, 3000)])
        # dimension values, then an auth failure on it
        self.run_cli(["dims", "--metric", "DailyActiveUsers", "--dimension", "Country", *u], [ok("dimension_values_done.json")])
        self.run_cli(["dims", "--metric", "DailyActiveUsers", "--dimension", "Country", *u], [echo_error(403, None)])
        # experiments: list ok, stats pending -> network error during poll, get 403 echo
        self.run_cli(["experiments", "list", *u], [ok("experiments_list.json")])
        self.run_cli(["experiments", "stats", "--id", "test-exp-1", *u],
                     [ok("experiments_stats_pending.json")] + [network] * 4)
        self.run_cli(["experiments", "get", "--id", "test-exp-1", *u], [echo_error(403, None)])
        self.run_cli(["status", *u], [])
        self.run_cli(["show", "--metric", "DailyActiveUsers", "--revisions", *u], [])
        # direct client calls: exception texts
        for responses in ([network], [echo_error(401, None)], [echo_error(400, 2001)], [echo_error(429, 3000)]):
            fake = FakeFetch(responses)
            self.fakes.append(fake)
            try:
                cl.Client(fetch=fake, sleep=lambda s: None, clock=lambda: 0.0).query(
                    "1", "metrics", {"metric": "Visits", "granularity": "OneDay"})
            except cl.ApiError as exc:
                self.texts += [str(exc), repr(exc), repr(exc.args)]
        joined = "\n".join(self.texts)
        self.assertIn("FAILED", joined)          # the scenarios really failed ...
        self.assertIn("<redacted>", joined)       # ... and the echoed key was redacted, not dropped by luck
        self.assertIn("key lacks universe:read for experiments", joined)
        self.assert_no_key_anywhere()

    def test_missing_key_refuses_before_any_request(self):
        fake = FakeFetch([])
        self.fakes.append(fake)
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.dict(os.environ, {cl.KEY_ENV: ""}), redirect_stdout(out), redirect_stderr(err):
            code = analytics.main(["pull", "--set", "weekly", "--universe", "1"])
        self.assertEqual(code, 2)
        self.assertIn(cl.KEY_ENV, err.getvalue())
        self.assertEqual(fake.calls, [])


if __name__ == "__main__":
    unittest.main()
