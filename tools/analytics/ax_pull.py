#!/usr/bin/env python3
"""Pull planning and execution for the analyst tool: metric sets, request checks, date-range splitting,
history writes, the pull log, `status` and `show`.

Request checks run before any request (docs mirror cloud/guides/analytics/index.md; fact-check 01 §4.1-4.2):
  - the metric must be in the catalog (metric_sets.json, names from metrics.md) and support the granularity;
  - startTime never earlier than the metric's own retention (standard 1468 d, performance 28 d, thumbnails
    30 d, matchmaking 90 d, RotraceTotalCalls 365 d) minus a one-day safety margin: an older start is clamped
    for sets and refused for a single `pull-metric`;
  - a range over 2 years only with OneWeek, OneMonth or None;
  - `limit` only with granularity None and a breakdown.
429 code 3000 (data point budget) and 504 code 1000: the range is halved on bucket boundaries and each half
is retried, down to one bucket; then the failure is reported. A missing bucket is never filled.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

import ax_client
import ax_store as st

TOOL_DIR = Path(__file__).resolve().parent
STALE_WARNING_DAYS = 21          # J013-D6
TWO_YEARS = timedelta(days=730)  # docs: "Date ranges longer than two years only support OneWeek, OneMonth, None"
LONG_RANGE_OK = ("OneWeek", "OneMonth", "None")
BUCKET = {"OneMinute": timedelta(minutes=1), "HalfHour": timedelta(minutes=30), "OneHour": timedelta(hours=1),
          "OneDay": timedelta(days=1), "OneWeek": timedelta(days=7)}
MAX_SPLIT_DEPTH = 8
RETENTION_MARGIN = timedelta(days=1)


class RequestRefused(ValueError):
    """A request this tool will not send because the docs say it would fail."""


def load_sets(path: Path | None = None) -> dict:
    return json.loads((path or TOOL_DIR / "metric_sets.json").read_text(encoding="utf-8"))


def day_floor(dt: datetime) -> datetime:
    return dt.astimezone(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)


def earliest_start(catalog_row: dict, now: datetime) -> datetime:
    """First UTC midnight we may use as startTime: retention_days back, plus a one-day margin."""
    return day_floor(now - timedelta(days=int(catalog_row["retention_days"])) + RETENTION_MARGIN) + timedelta(days=1)


def check_request(catalog: dict, body: dict, now: datetime) -> None:
    """Raise RequestRefused if the docs say this request fails."""
    metric, gran = body["metric"], body["granularity"]
    row = catalog.get(metric)
    if row is None:
        raise RequestRefused(f"{metric}: not in the catalog (metric_sets.json); add its row from metrics.md first")
    if gran not in row["granularities"]:
        raise RequestRefused(f"{metric}: granularity {gran} not supported (supported: {row['granularities']})")
    start, end = st.parse_utc(body["startTime"]), st.parse_utc(body["endTime"])
    if start >= end:
        raise RequestRefused(f"{metric}: startTime must be before endTime (end is exclusive)")
    if end - start > TWO_YEARS and gran not in LONG_RANGE_OK:
        raise RequestRefused(f"{metric}: ranges over 2 years need OneWeek, OneMonth or None, not {gran}")
    first = earliest_start(row, now)
    if start < first:
        raise RequestRefused(f"{metric}: startTime {body['startTime']} is older than its {row['retention_days']}-day "
                             f"retention allows; earliest safe start is {st.utc_iso(first)}")
    if body.get("limit") is not None and (gran != "None" or not body.get("breakdown")):
        raise RequestRefused(f"{metric}: limit is only valid with granularity None and a breakdown")


def make_body(query: dict, start: datetime, end: datetime, extra_filter: list | None = None) -> dict:
    body = {"metric": query["metric"], "granularity": query["granularity"],
            "startTime": st.utc_iso(start), "endTime": st.utc_iso(end)}
    if query.get("breakdown"):
        body["breakdown"] = list(query["breakdown"])
    filters = list(query.get("filter") or []) + list(extra_filter or [])
    if filters:
        body["filter"] = filters
    if query.get("limit") is not None:
        body["limit"] = query["limit"]
    return body


def split_point(start: datetime, end: datetime, granularity: str) -> datetime | None:
    """Midpoint on a bucket boundary counted from start, or None when the range cannot be split."""
    step = BUCKET.get(granularity)
    if step is None:
        return None
    n = int((end - start) / step)
    if n < 2:
        return None
    return start + step * (n // 2)


def run_query(client: ax_client.Client, base: Path, universe_id: str, body: dict, *, pull_id: str,
              metric_set: str | None, now_iso, depth: int = 0) -> tuple[int, list[str]]:
    """Send one metrics query (splitting on 3000/1000), append its points. Returns (points, notes)."""
    try:
        resp, path = client.query(universe_id, "metrics", body)
    except ax_client.SplitNeeded as err:
        mid = split_point(st.parse_utc(body["startTime"]), st.parse_utc(body["endTime"]), body["granularity"])
        if mid is None or depth >= MAX_SPLIT_DEPTH:
            raise ax_client.ApiError(f"{err}; cannot split further: use a shorter range, coarser granularity "
                                     f"or fewer breakdown series", err.status, err.code) from None
        notes = [f"{body['metric']}: code {err.code}, range split at {st.utc_iso(mid)}"]
        total = 0
        for a, b in ((body["startTime"], st.utc_iso(mid)), (st.utc_iso(mid), body["endTime"])):
            n, sub = run_query(client, base, universe_id, {**body, "startTime": a, "endTime": b}, pull_id=pull_id,
                               metric_set=metric_set, now_iso=now_iso, depth=depth + 1)
            total += n
            notes += sub
        return total, notes
    recs = st.points_from_response(resp, universe_id=universe_id, request=body, operation_path=path,
                                   pulled_at_utc=now_iso(), pull_id=pull_id, metric_set=metric_set)
    st.append_points(base, recs)
    return len(recs), []


def _utc_now_iso() -> str:
    return st.utc_iso(datetime.now(timezone.utc))


def _not_final(base: Path, pull_id: str, metrics: set[str]) -> int:
    n = 0
    for m in metrics:
        n += sum(1 for r in st.read_points(base, m) if r.get("pull_id") == pull_id
                 and r.get("point_status") not in (None, "Valid"))
    return n


def pull_queries(client, universe_id: str, queries: list[dict], *, label: str, now: datetime, catalog: dict,
                 lookback_days: int, clamp: bool = True, extra_filter: list | None = None, base: Path | None = None,
                 now_iso=_utc_now_iso, window: tuple[datetime, datetime] | None = None) -> dict:
    """Run queries for one pull; write points and one pulls.jsonl row. Auth and missing-key errors stop the run."""
    universe_id = st.check_universe(universe_id)
    base = base or st.data_dir(universe_id)
    pull_id = uuid.uuid4().hex[:12]
    started = now_iso()
    results, notes = [], []
    stopped = None
    end_default = day_floor(now)
    for q in queries:
        row = catalog.get(q["metric"], {})
        start, end = window or (end_default - timedelta(days=lookback_days), end_default)
        if clamp and row and start < earliest_start(row, now):
            start = earliest_start(row, now)
            notes.append(f"{q['metric']}: start clamped to {st.utc_iso(start)} ({row['retention_days']}-day retention)")
        body = make_body(q, start, end, extra_filter)
        item = {"metric": q["metric"], "granularity": q["granularity"], "breakdown": body.get("breakdown", []),
                "start": body["startTime"], "end": body["endTime"]}
        if stopped:
            results.append({**item, "ok": False, "error": f"not requested: {stopped}"})
            continue
        try:
            check_request(catalog, body, now)
            n, sub = run_query(client, base, universe_id, body, pull_id=pull_id, metric_set=label, now_iso=now_iso)
            notes += sub
            results.append({**item, "ok": True, "points": n})
        except (ax_client.AuthError, ax_client.MissingKey) as err:
            stopped = str(err)
            results.append({**item, "ok": False, "error": str(err)})
        except (ax_client.ApiError, RequestRefused) as err:
            results.append({**item, "ok": False, "error": str(err),
                            "code": getattr(err, "code", None), "status": getattr(err, "status", None)})
    ok = all(r["ok"] for r in results) and bool(results)
    starts = [r["start"] for r in results] or [st.utc_iso(end_default)]
    ends = [r["end"] for r in results] or [st.utc_iso(end_default)]
    row = {"pull_id": pull_id, "universe_id": universe_id, "metric_set": label, "started_at_utc": started,
           "finished_at_utc": now_iso(), "window_start_utc": min(starts), "window_end_utc": max(ends), "ok": ok,
           "requests": results, "notes": notes,
           "points": sum(r.get("points", 0) for r in results),
           "points_not_final": _not_final(base, pull_id, {r["metric"] for r in results if r["ok"]})}
    st.append_pull(base, row)
    return row


def pull_set(client, universe_id: str, set_name: str, *, now: datetime, sets: dict | None = None,
             base: Path | None = None, now_iso=_utc_now_iso) -> dict:
    sets = sets or load_sets()
    spec = sets["sets"].get(set_name)
    if spec is None or "discovery" in spec:
        raise SystemExit(f"unknown plain metric set {set_name!r}; plain sets: "
                         f"{[k for k, v in sets['sets'].items() if 'discovery' not in v]}")
    return pull_queries(client, universe_id, spec["queries"], label=set_name, now=now, catalog=sets["catalog"],
                        lookback_days=spec["lookback_days"], base=base, now_iso=now_iso)


def pull_funnel(client, universe_id: str, funnel: str, *, now: datetime, sets: dict | None = None,
                base: Path | None = None, now_iso=_utc_now_iso) -> dict:
    """Docs two-step pattern: discover step ids (FunnelStep values), then per-step metrics filtered to them."""
    sets = sets or load_sets()
    spec = sets["sets"]["funnel"]
    name_filter = [{"dimension": "FunnelName", "values": [funnel], "operation": "In"}]
    disc = spec["discovery"]
    found = pull_queries(client, universe_id, [disc], label=f"funnel:{funnel}:discovery", now=now,
                         catalog=sets["catalog"], lookback_days=disc["lookback_days"], extra_filter=name_filter,
                         base=base, now_iso=now_iso)
    if not found["ok"]:
        return {"discovery": found, "steps": [], "pull": None}
    b = base or st.data_dir(universe_id)
    steps = sorted({s["value"] for r in st.read_points(b, disc["metric"], "None") if r["pull_id"] == found["pull_id"]
                    for s in r.get("series", []) if s.get("dimension") == "FunnelStep"},
                   key=lambda v: (len(str(v)), str(v)))
    if not steps:
        return {"discovery": found, "steps": [], "pull": None}
    step_filter = [{"dimension": "FunnelStep", "values": steps, "operation": "In"}] + name_filter
    row = pull_queries(client, universe_id, spec["queries"], label=f"funnel:{funnel}", now=now,
                       catalog=sets["catalog"], lookback_days=spec["lookback_days"], extra_filter=step_filter,
                       base=base, now_iso=now_iso)
    return {"discovery": found, "steps": steps, "pull": row}


def pull_dimensions(client, universe_id: str, metric: str, dimensions: list[str], *, start: datetime,
                    end: datetime, now: datetime, sets: dict | None = None, base: Path | None = None,
                    now_iso=_utc_now_iso) -> dict:
    sets = sets or load_sets()
    universe_id = st.check_universe(universe_id)
    base = base or st.data_dir(universe_id)
    row = sets["catalog"].get(metric)
    if row is None:
        raise RequestRefused(f"{metric}: not in the catalog (metric_sets.json)")
    if start < earliest_start(row, now):
        raise RequestRefused(f"{metric}: start older than its {row['retention_days']}-day retention")
    body = {"metric": metric, "dimensions": list(dimensions), "startTime": st.utc_iso(start), "endTime": st.utc_iso(end)}
    resp, path = client.query(universe_id, "dimension-values", body)
    pull_id = uuid.uuid4().hex[:12]
    recs = st.dimension_values_from_response(resp, universe_id=universe_id, request=body, operation_path=path,
                                             pulled_at_utc=now_iso(), pull_id=pull_id)
    st.append_jsonl(base / "observations" / "dimension-values.jsonl", recs)
    return {"pull_id": pull_id, "metric": metric,
            "values": {d: [r["value"] for r in recs if r["dimension"] == d] for d in dimensions}}


# -- Experiments (read only) -------------------------------------------------------------------------------------
def pull_experiments(client, universe_id: str, what: str, experiment_id: str | None = None, *,
                     base: Path | None = None, now_iso=_utc_now_iso, page_size: int = 20) -> dict:
    """Save the raw response of list / get / stats with pulled-at time. No field is invented or renamed."""
    universe_id = st.check_universe(universe_id)
    base = base or st.data_dir(universe_id)
    if what == "list":
        pages, skip = [], 0
        while True:
            params = {"maxPageSize": page_size, "skip": skip, "sortKey": "LIST_EXPERIMENT_SORT_KEY_RELEVANCE",
                      "sortOrder": "SORT_ORDER_DESCENDING"}
            page = client.experiments_get(universe_id, "experiments", params)
            pages.append(page)
            rows = page.get("experiments") if isinstance(page.get("experiments"), list) else []
            skip += len(rows)
            total = page.get("total")
            if not rows or not isinstance(total, int) or skip >= total or len(pages) >= 50:
                break
        rec = {"universe_id": universe_id, "experiment_id": None, "pulled_at_utc": now_iso(),
               "request_path": "experiments", "responses": pages}
        st.append_experiment(base, "list", rec)
        return rec
    if not experiment_id or not experiment_id.replace("-", "").replace("_", "").isalnum():
        raise ValueError("an experiment id (letters, digits, - or _) is needed")
    rel = f"experiments/{experiment_id}" + ("/stats" if what == "stats" else "")
    first = client.experiments_get(universe_id, rel)
    if what == "stats":
        final = client.experiments_operation(universe_id, first)
        rec = {"universe_id": universe_id, "experiment_id": experiment_id, "pulled_at_utc": now_iso(),
               "request_path": rel, "response": first, "final_operation": final}
    elif what == "get":
        rec = {"universe_id": universe_id, "experiment_id": experiment_id, "pulled_at_utc": now_iso(),
               "request_path": rel, "response": first}
    else:
        raise ValueError(f"unknown experiments read {what!r}")
    st.append_experiment(base, what, rec)
    return rec


# -- Reading ---------------------------------------------------------------------------------------------------
def set_retention_days(sets: dict, label: str) -> int | None:
    name = "funnel" if label.startswith("funnel:") else label
    spec = sets["sets"].get(name)
    if not spec:
        return None
    return min(int(sets["catalog"][q["metric"]]["retention_days"]) for q in spec["queries"])


def status(base: Path, now: datetime, sets: dict | None = None) -> dict:
    """Last successful pull per metric set, its age, and the 21-day warning (with a gap note when data older than
    the set's shortest retention has already expired since the last pull)."""
    sets = sets or load_sets()
    pulls = st.read_pulls(base)
    labels = sorted({p["metric_set"] for p in pulls if not p["metric_set"].endswith(":discovery")}
                    | {k for k, v in sets["sets"].items() if "discovery" not in v})
    out, warnings = [], []
    for label in labels:
        rows = [p for p in pulls if p["metric_set"] == label]
        good = [p for p in rows if p.get("ok")]
        last = max(good, key=lambda p: p["finished_at_utc"]) if good else None
        last_any = max(rows, key=lambda p: p["finished_at_utc"]) if rows else None
        ret = set_retention_days(sets, label)
        item = {"metric_set": label, "retention_days": ret, "last_success_utc": last and last["finished_at_utc"],
                "last_attempt_utc": last_any and last_any["finished_at_utc"],
                "last_attempt_ok": last_any and last_any.get("ok")}
        if last is None:
            item["age_days"] = None
            item["warning"] = "never pulled successfully"
        else:
            age = (now - st.parse_utc(last["finished_at_utc"])).total_seconds() / 86400
            item["age_days"] = round(age, 1)
            if age > STALE_WARNING_DAYS:
                msg = f"last successful pull is {age:.1f} days old (> {STALE_WARNING_DAYS})"
                if ret is not None:
                    lost_before = now - timedelta(days=ret)
                    covered = st.parse_utc(last["window_end_utc"])
                    if lost_before > covered:
                        msg += (f"; GAP: Roblox keeps these {ret} days only, so data from {st.utc_iso(covered)} to "
                                f"{st.utc_iso(day_floor(lost_before))} is gone from our history")
                    else:
                        msg += (f"; pull within {(covered - lost_before).total_seconds() / 86400:.1f} days or "
                                f"history gets a gap ({ret}-day retention)")
                item["warning"] = msg
        if item.get("warning"):
            warnings.append(f"{label}: {item['warning']}")
        out.append(item)
    return {"now_utc": st.utc_iso(now), "stale_warning_days": STALE_WARNING_DAYS, "sets": out, "warnings": warnings}


def show(base: Path, metric: str, granularity: str | None = None, *, start: datetime | None = None,
         end: datetime | None = None, with_revisions: bool = False, catalog: dict | None = None,
         breakdown: str | None = None) -> dict:
    """Latest value per bucket (start inclusive, end exclusive), with not-final points flagged. Missing buckets
    stay missing; nothing is summed. breakdown: None = every series; "none" = only the total (no breakdown);
    a dimension name (e.g. "Platform") = only series pulled with that one breakdown."""
    recs = st.read_points(base, metric, granularity)
    if breakdown is not None:
        want = [] if breakdown.lower() == "none" else [breakdown]
        recs = [r for r in recs if list(r.get("breakdown") or []) == want]
    if start or end:
        recs = [r for r in recs if (not start or st.parse_utc(r["bucket_time_utc"]) >= start)
                and (not end or st.parse_utc(r["bucket_time_utc"]) < end)]
    rows = st.latest(recs)
    keep = ("bucket_time_utc", "granularity", "series", "filter", "value", "string_values", "point_status", "final",
            "revision_count", "pulled_at_utc")
    points = [{k: r.get(k) for k in keep} for r in rows]
    if with_revisions:
        revs = st.revisions(recs)
        for p, r in zip(points, rows):
            p["revisions"] = [{"pulled_at_utc": x["pulled_at_utc"], "value": x.get("value"),
                               "point_status": x.get("point_status")} for x in revs[st.bucket_key(r)]]
    note = (catalog or {}).get(metric, {}).get("note")
    return {"metric": metric, "granularity": granularity, "breakdown": breakdown, "points": points,
            "not_final": sum(1 for p in points if not p["final"]),
            "revised_buckets": sum(1 for p in points if p["revision_count"] > 1), "note": note}
