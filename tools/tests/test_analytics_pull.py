#!/usr/bin/env python3
"""Offline tests for tools/analytics/ax_pull.py and ax_store.py: history kept append-only with statuses and
revisions (C3), request checks before any request, range split on code 3000, missing buckets stay missing,
the 21-day status warning, the funnel two-step, raw experiment saves, the data dir rule. Temp dirs only."""
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "analytics"))
import ax_client as cl  # noqa: E402
import ax_pull as pl  # noqa: E402
import ax_store as st  # noqa: E402
from test_analytics_client import TEST_KEY, FakeFetch, fixture, ok  # noqa: E402

NOW = datetime(2026, 10, 21, 12, tzinfo=timezone.utc)
SETS = pl.load_sets()
CAT = SETS["catalog"]


def clock(*stamps):
    it = iter(stamps)
    last = [stamps[-1]]

    def now_iso():
        last[0] = next(it, last[0])
        return last[0]
    return now_iso


def done_body(points, breakdowns=None):
    return json.dumps({"path": "v1/universes/1/operations/metrics/t", "done": True,
                       "response": {"values": [{"breakdowns": breakdowns or [], "dataPoints": points}]}}).encode()


class Base(unittest.TestCase):
    def setUp(self):
        p = mock.patch.dict(os.environ, {cl.KEY_ENV: TEST_KEY})
        p.start()
        self.addCleanup(p.stop)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)

    def client(self, responses):
        self.fake = FakeFetch(responses)
        return cl.Client(fetch=self.fake, sleep=lambda s: None, clock=lambda: 0.0)

    def adhoc(self, client, query, start, end, now_iso):
        return pl.pull_queries(client, "1234567890", [query], label="adhoc", now=NOW, catalog=CAT, lookback_days=0,
                               clamp=False, window=(start, end), base=self.base, now_iso=now_iso)


class History(Base):
    def test_c3_202_then_done_then_revision_keeps_both(self):
        q = {"metric": "DailyActiveUsers", "granularity": "OneDay"}
        s, e = datetime(2026, 10, 17, tzinfo=timezone.utc), datetime(2026, 10, 21, tzinfo=timezone.utc)
        c = self.client([ok("metrics_202_pending.json", 202), ok("metrics_done_statuses.json")])
        row1 = self.adhoc(c, q, s, e, clock("2026-10-21T12:00:00Z"))
        self.assertTrue(row1["ok"])
        self.assertEqual((row1["points"], row1["points_not_final"]), (4, 2))
        recs = st.read_points(self.base, "DailyActiveUsers")
        self.assertEqual([r["point_status"] for r in recs], ["Valid", None, "Projected", "NotStatisticallySignificant"])
        r0 = recs[0]
        self.assertEqual(r0["operation_path"], "v1/universes/1234567890/operations/metrics/testop1")
        self.assertEqual(r0["request"], {"metric": "DailyActiveUsers", "granularity": "OneDay",
                                         "startTime": "2026-10-17T00:00:00Z", "endTime": "2026-10-21T00:00:00Z"})
        for k in ("universe_id", "metric", "granularity", "breakdown", "series", "filter", "bucket_time_utc", "value",
                  "string_values", "point_status", "request", "operation_path", "pulled_at_utc", "tool_version"):
            self.assertIn(k, r0)
        # second pull of the same bucket, revised value
        c = self.client([ok("metrics_done_revised.json")])
        self.adhoc(c, q, s, e, clock("2026-10-23T09:00:00Z"))
        recs = st.read_points(self.base, "DailyActiveUsers")
        self.assertEqual(len(recs), 5)  # nothing overwritten
        view = pl.show(self.base, "DailyActiveUsers", "OneDay", with_revisions=True)
        b19 = [p for p in view["points"] if p["bucket_time_utc"] == "2026-10-19T00:00:00Z"][0]
        self.assertEqual((b19["value"], b19["point_status"], b19["final"], b19["revision_count"]), (1234, "Valid", True, 2))
        self.assertEqual([(r["value"], r["point_status"]) for r in b19["revisions"]], [(1200, "Projected"), (1234, "Valid")])
        b20 = [p for p in view["points"] if p["bucket_time_utc"] == "2026-10-20T00:00:00Z"][0]
        self.assertFalse(b20["final"])  # NotStatisticallySignificant is never final
        self.assertEqual(view["not_final"], 1)

    def test_breakdown_and_text_values_kept(self):
        q = {"metric": "ThumbnailWinningSegments", "granularity": "OneDay", "breakdown": ["Platform"]}
        c = self.client([ok("metrics_done_breakdown_text.json")])
        self.adhoc(c, q, datetime(2026, 10, 19, tzinfo=timezone.utc), datetime(2026, 10, 20, tzinfo=timezone.utc),
                   clock("2026-10-21T00:00:00Z"))
        recs = st.read_points(self.base, "ThumbnailWinningSegments")
        self.assertEqual(recs[0]["string_values"], ["TopEngagement", "HighCTR"])
        self.assertEqual(recs[0]["series"], [{"dimension": "Platform", "value": "Computer"}])
        self.assertEqual(recs[1]["series"][0]["displayValue"], "Phone")
        self.assertEqual(len(st.latest(recs)), 2)  # two series, not one bucket

    def test_missing_bucket_is_not_filled(self):
        body = done_body([{"time": "2026-10-17T00:00:00Z", "value": 5}, {"time": "2026-10-19T00:00:00Z", "value": 6}])
        c = self.client([(200, {}, body)])
        self.adhoc(c, {"metric": "Visits", "granularity": "OneDay"}, datetime(2026, 10, 17, tzinfo=timezone.utc),
                   datetime(2026, 10, 20, tzinfo=timezone.utc), clock("2026-10-21T00:00:00Z"))
        view = pl.show(self.base, "Visits")
        self.assertEqual([p["bucket_time_utc"] for p in view["points"]], ["2026-10-17T00:00:00Z", "2026-10-19T00:00:00Z"])

    def test_show_breakdown_filter_separates_total_and_series(self):
        day = datetime(2026, 10, 17, tzinfo=timezone.utc)
        total = done_body([{"time": "2026-10-17T00:00:00Z", "value": 100}])
        phone = done_body([{"time": "2026-10-17T00:00:00Z", "value": 60}], [{"dimension": "Platform", "value": "Phone"}])
        c = self.client([(200, {}, total), (200, {}, phone)])
        self.adhoc(c, {"metric": "Visits", "granularity": "OneDay"}, day, day + timedelta(days=1),
                   clock("2026-10-21T00:00:00Z"))
        self.adhoc(c, {"metric": "Visits", "granularity": "OneDay", "breakdown": ["Platform"]}, day,
                   day + timedelta(days=1), clock("2026-10-21T00:01:00Z"))
        self.assertEqual(len(pl.show(self.base, "Visits")["points"]), 2)
        self.assertEqual([p["value"] for p in pl.show(self.base, "Visits", breakdown="none")["points"]], [100])
        self.assertEqual([p["value"] for p in pl.show(self.base, "Visits", breakdown="Platform")["points"]], [60])
        self.assertEqual(pl.show(self.base, "Visits", breakdown="Country")["points"], [])

    def test_torn_line_skipped_and_next_append_on_new_line(self):
        path = st.metric_path(self.base, "Visits")
        path.parent.mkdir(parents=True)
        path.write_text('{"kind": "metric_po', encoding="utf-8")
        c = self.client([(200, {}, done_body([{"time": "2026-10-17T00:00:00Z", "value": 5}]))])
        with mock.patch("sys.stderr"):
            self.adhoc(c, {"metric": "Visits", "granularity": "OneDay"}, datetime(2026, 10, 17, tzinfo=timezone.utc),
                       datetime(2026, 10, 18, tzinfo=timezone.utc), clock("2026-10-21T00:00:00Z"))
            self.assertEqual(len(st.read_points(self.base, "Visits")), 1)


class RequestChecks(Base):
    def body(self, metric, gran, start, end, **kw):
        return {"metric": metric, "granularity": gran, "startTime": start, "endTime": end, **kw}

    def test_refusals_make_no_request(self):
        cases = [
            self.body("NotAMetric", "OneDay", "2026-10-01T00:00:00Z", "2026-10-02T00:00:00Z"),
            self.body("MonthlyActiveUsers", "OneWeek", "2026-10-01T00:00:00Z", "2026-10-15T00:00:00Z"),
            # performance: 28-day retention -> 2026-09-20 is too old at NOW
            self.body("ClientCrashRate15m", "OneDay", "2026-09-20T00:00:00Z", "2026-10-01T00:00:00Z"),
            # thumbnails: 30 days
            self.body("ThumbnailImpressions", "OneDay", "2026-09-15T00:00:00Z", "2026-10-01T00:00:00Z"),
            # over 2 years at OneDay
            self.body("DailyActiveUsers", "OneDay", "2024-01-01T00:00:00Z", "2026-10-01T00:00:00Z"),
            self.body("DailyActiveUsers", "OneDay", "2026-10-01T00:00:00Z", "2026-10-02T00:00:00Z", limit=5),
            self.body("DailyActiveUsers", "OneDay", "2026-10-02T00:00:00Z", "2026-10-02T00:00:00Z"),
        ]
        for body in cases:
            with self.assertRaises(pl.RequestRefused, msg=body):
                pl.check_request(CAT, body, NOW)
        # allowed: over 2 years at OneWeek; performance inside the window
        pl.check_request(CAT, self.body("DailyActiveUsers", "OneWeek", "2024-01-01T00:00:00Z", "2026-10-01T00:00:00Z"), NOW)
        pl.check_request(CAT, self.body("ClientCrashRate15m", "OneDay", "2026-09-25T00:00:00Z", "2026-10-21T00:00:00Z"), NOW)
        c = self.client([])
        row = self.adhoc(c, {"metric": "ClientCrashRate15m", "granularity": "OneDay"},
                         datetime(2026, 9, 1, tzinfo=timezone.utc), datetime(2026, 10, 1, tzinfo=timezone.utc),
                         clock("2026-10-21T00:00:00Z"))
        self.assertFalse(row["ok"])
        self.assertEqual(self.fake.calls, [])

    def test_set_start_clamped_to_retention(self):
        c = self.client([(200, {}, done_body([]))] * len(SETS["sets"]["performance"]["queries"]))
        row = pl.pull_set(c, "1234567890", "performance", now=NOW, base=self.base, now_iso=clock("2026-10-21T12:00:00Z"))
        self.assertTrue(row["ok"], row)
        first = pl.earliest_start(CAT["ClientCrashRate15m"], NOW)
        for call in self.fake.calls:
            body = json.loads(call["body"])
            self.assertGreaterEqual(st.parse_utc(body["startTime"]), first)
            self.assertEqual(body["endTime"], "2026-10-21T00:00:00Z")  # exclusive: last full UTC day is 10-20

    def test_3000_splits_range_on_day_boundaries(self):
        p1 = done_body([{"time": "2026-10-01T00:00:00Z", "value": 1}])
        p2 = done_body([{"time": "2026-10-03T00:00:00Z", "value": 2}])
        c = self.client([(429, {}, fixture("error_3000.json")), (200, {}, p1), (200, {}, p2)])
        row = self.adhoc(c, {"metric": "Visits", "granularity": "OneDay"}, datetime(2026, 10, 1, tzinfo=timezone.utc),
                         datetime(2026, 10, 5, tzinfo=timezone.utc), clock("2026-10-21T00:00:00Z"))
        self.assertTrue(row["ok"])
        spans = [(json.loads(x["body"])["startTime"], json.loads(x["body"])["endTime"]) for x in self.fake.calls]
        self.assertEqual(spans, [("2026-10-01T00:00:00Z", "2026-10-05T00:00:00Z"),
                                 ("2026-10-01T00:00:00Z", "2026-10-03T00:00:00Z"),
                                 ("2026-10-03T00:00:00Z", "2026-10-05T00:00:00Z")])
        self.assertIn("split", row["notes"][0])
        # one bucket cannot be split: reported, not retried
        c = self.client([(429, {}, fixture("error_3000.json"))])
        row = self.adhoc(c, {"metric": "Visits", "granularity": "OneDay"}, datetime(2026, 10, 1, tzinfo=timezone.utc),
                         datetime(2026, 10, 2, tzinfo=timezone.utc), clock("2026-10-21T00:00:00Z"))
        self.assertFalse(row["ok"])
        self.assertEqual(row["requests"][0]["code"], 3000)
        self.assertIn("cannot split", row["requests"][0]["error"])

    def test_auth_error_stops_the_run(self):
        c = self.client([(401, {}, b"")])
        row = pl.pull_set(c, "1234567890", "weekly", now=NOW, base=self.base, now_iso=clock("2026-10-21T12:00:00Z"))
        self.assertEqual(len(self.fake.calls), 1)
        self.assertFalse(row["ok"])
        self.assertTrue(all(r["error"].startswith("not requested") for r in row["requests"][1:]))


class Status(Base):
    def write_pull(self, label, finished, ok=True, end=None):
        st.append_pull(self.base, {"pull_id": "p", "universe_id": "1", "metric_set": label, "started_at_utc": finished,
                                   "finished_at_utc": finished, "window_start_utc": "2026-01-01T00:00:00Z",
                                   "window_end_utc": end or finished[:10] + "T00:00:00Z", "ok": ok, "requests": []})

    def test_21_day_warning_and_gap(self):
        self.write_pull("performance", "2026-10-01T10:00:00Z")   # 20.1 days before NOW: no warning
        self.write_pull("weekly", "2026-09-29T10:00:00Z")        # 22.1 days: warning, standard retention
        res = pl.status(self.base, NOW)
        by = {s["metric_set"]: s for s in res["sets"]}
        self.assertNotIn("warning", by["performance"])
        self.assertIn("> 21", by["weekly"]["warning"])
        # performance last good pull 35 days ago -> gap already
        self.write_pull("performance", "2026-09-16T10:00:00Z")
        self.write_pull("performance", "2026-10-20T10:00:00Z", ok=False)  # failed pulls do not count
        later = NOW + timedelta(days=15)
        perf = {s["metric_set"]: s for s in pl.status(self.base, later)["sets"]}["performance"]
        self.assertIn("GAP", perf["warning"])
        self.assertEqual(perf["last_success_utc"], "2026-10-01T10:00:00Z")
        self.assertFalse(perf["last_attempt_ok"])

    def test_never_pulled(self):
        res = pl.status(self.base, NOW)
        self.assertTrue(any("never pulled" in w for w in res["warnings"]))


class FunnelDimsExperiments(Base):
    def test_funnel_two_step(self):
        disc = done_body([{"time": "2026-07-23T00:00:00Z", "value": 50}], [{"dimension": "FunnelStep", "value": "2"}])
        disc2 = json.loads(disc)
        disc2["response"]["values"].append({"breakdowns": [{"dimension": "FunnelStep", "value": "1"}],
                                            "dataPoints": [{"time": "2026-07-23T00:00:00Z", "value": 80}]})
        n = len(SETS["sets"]["funnel"]["queries"])
        c = self.client([(200, {}, json.dumps(disc2).encode())] + [(200, {}, done_body([]))] * n)
        res = pl.pull_funnel(c, "1234567890", "TEST_Funnel", now=NOW, base=self.base, now_iso=clock("2026-10-21T00:00:00Z"))
        self.assertEqual(res["steps"], ["1", "2"])
        second = json.loads(self.fake.calls[1]["body"])
        self.assertEqual(second["filter"], [{"dimension": "FunnelStep", "values": ["1", "2"], "operation": "In"},
                                            {"dimension": "FunnelName", "values": ["TEST_Funnel"], "operation": "In"}])
        self.assertEqual(second["granularity"], "None")

    def test_dimension_values_saved(self):
        c = self.client([ok("dimension_values_done.json")])
        res = pl.pull_dimensions(c, "1234567890", "DailyActiveUsers", ["Country"], start=NOW - timedelta(days=30),
                                 end=NOW, now=NOW, base=self.base)
        self.assertEqual(res["values"], {"Country": ["US", "GB"]})
        self.assertEqual(len(st.read_jsonl(self.base / "observations" / "dimension-values.jsonl")), 2)

    def test_experiments_raw_saved(self):
        c = self.client([ok("experiments_list.json")])
        pl.pull_experiments(c, "1234567890", "list", base=self.base, now_iso=clock("2026-10-21T00:00:00Z"))
        c = self.client([ok("experiments_stats_pending.json"), ok("experiments_stats_done.json")])
        pl.pull_experiments(c, "1234567890", "stats", "test-exp-1", base=self.base, now_iso=clock("2026-10-21T00:00:00Z"))
        saved = st.read_jsonl(self.base / "experiments" / "stats.jsonl")[0]
        self.assertEqual(saved["final_operation"]["experimentStats"], {"isSrmDetected": False})
        self.assertEqual(saved["response"], json.loads(fixture("experiments_stats_pending.json")))
        self.assertEqual(saved["pulled_at_utc"], "2026-10-21T00:00:00Z")
        listed = st.read_jsonl(self.base / "experiments" / "list.jsonl")[0]
        self.assertEqual(listed["responses"][0]["total"], 1)


class DataDir(unittest.TestCase):
    def test_env_override_and_default(self):
        with mock.patch.dict(os.environ, {"ANALYTICS_DATA_DIR": "/tmp/x"}):
            self.assertEqual(st.data_dir("42"), Path("/tmp/x") / "42")
        with mock.patch.dict(os.environ, {"ANALYTICS_DATA_DIR": ""}):
            self.assertEqual(st.data_dir(42), st.ROOT / ".tools" / "analytics-data" / "42")
        for bad in ("../x", "12a", ""):
            with self.assertRaises(ValueError):
                st.data_dir(bad)

    def test_catalog_sets_use_catalog_metrics(self):
        for name, spec in SETS["sets"].items():
            for q in spec["queries"] + ([spec["discovery"]] if "discovery" in spec else []):
                self.assertIn(q["metric"], CAT, name)
                self.assertIn(q["granularity"], CAT[q["metric"]]["granularities"], (name, q))


if __name__ == "__main__":
    unittest.main()
