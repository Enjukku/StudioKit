#!/usr/bin/env python3
"""History store for the analyst tool. Append-only JSONL; nothing is ever overwritten or deleted.

Layout: <data_dir>/
  observations/metrics/<metric>.jsonl     one record per returned data point (kind "metric_point")
  observations/dimension-values.jsonl     one record per returned dimension value (kind "dimension_value")
  experiments/<list|get|stats>.jsonl      one record per raw Experiments API response (kind "experiment_*")
  pulls.jsonl                             one record per pull run (kind "pull"), read by `status`

data_dir = env ANALYTICS_DATA_DIR/<universe id>/ if the variable is set, else
           <repo>/.tools/analytics-data/<universe id>/ (.tools/ is git-ignored).

metric_point fields (schema_version 1):
  schema_version, tool_version, kind, universe_id, metric, granularity,
  breakdown        request breakdown names (list)
  series           the series' breakdowns as returned: [{dimension, value, displayValue?}] ([] = no breakdown)
  filter           request filter (list)
  bucket_time_utc  data point `time` (UTC bucket start)
  value            number or null; string_values list or null (text metrics; value then not meaningful)
  point_status     "Valid" | "Projected" | "NotStatisticallySignificant" | null (omitted by the API)
  request          the exact request body sent (never the key)
  endpoint, operation_path, pulled_at_utc, pull_id, metric_set

A re-pull of a bucket is a new record. latest() picks the newest pull per bucket; revisions() lists all.
A bucket the API did not return is no record (never a 0).

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SCHEMA_VERSION = 1
TOOL_VERSION = "0.1.0"
DATA_ENV = "ANALYTICS_DATA_DIR"
STATUSES = ("Valid", "Projected", "NotStatisticallySignificant")
NOT_FINAL = ("Projected", "NotStatisticallySignificant")
_UNIVERSE_RE = re.compile(r"^[0-9]{1,20}$")
_NAME_RE = re.compile(r"^[A-Za-z0-9_]{1,120}$")


def check_universe(universe_id) -> str:
    text = str(universe_id).strip()
    if not _UNIVERSE_RE.match(text):
        raise ValueError(f"universe id must be digits only, got {text!r}")
    return text


def data_dir(universe_id) -> Path:
    uid = check_universe(universe_id)
    env = os.environ.get(DATA_ENV, "").strip()
    return (Path(env) if env else ROOT / ".tools" / "analytics-data") / uid


def utc_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_utc(text: str) -> datetime:
    dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt.astimezone(timezone.utc)


def read_jsonl(path: Path) -> list[dict]:
    """Every readable JSON object line; an unreadable line (torn write) is skipped with a warning."""
    if not path.is_file():
        return []
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except ValueError:
            item = None
        if not isinstance(item, dict):
            print(f"WARNING: {path} line {n}: unreadable line skipped (torn write?)", file=sys.stderr)
            continue
        out.append(item)
    return out


def append_jsonl(path: Path, items: list[dict]) -> None:
    """Append only. Starts on a new line even if the file ends in a torn line."""
    if not items:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    lead = ""
    if path.is_file() and path.stat().st_size:
        with path.open("rb") as fh:
            fh.seek(-1, os.SEEK_END)
            lead = "" if fh.read(1) == b"\n" else "\n"
    text = "".join(json.dumps(i, sort_keys=True, ensure_ascii=False) + "\n" for i in items)
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(lead + text)


def metric_path(base: Path, metric: str) -> Path:
    if not _NAME_RE.match(metric):
        raise ValueError(f"bad metric name {metric!r}")
    return base / "observations" / "metrics" / f"{metric}.jsonl"


def points_from_response(response: dict, *, universe_id: str, request: dict, operation_path: str,
                         pulled_at_utc: str, pull_id: str, metric_set: str | None) -> list[dict]:
    """metric_point records for every data point in a metrics operation response. Values are kept as returned;
    an unknown status is kept as returned too (never dropped, never upgraded to final)."""
    out = []
    for series in (response.get("response") or {}).get("values") or []:
        for point in series.get("dataPoints") or []:
            value = point.get("value")
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                value = None
            sv = point.get("stringValues")
            out.append({
                "schema_version": SCHEMA_VERSION, "tool_version": TOOL_VERSION, "kind": "metric_point",
                "universe_id": universe_id, "metric": request["metric"], "granularity": request["granularity"],
                "breakdown": list(request.get("breakdown") or []), "series": list(series.get("breakdowns") or []),
                "filter": list(request.get("filter") or []), "bucket_time_utc": str(point.get("time")),
                "value": value, "string_values": list(sv) if isinstance(sv, list) else None,
                "point_status": point.get("status"), "request": request, "endpoint": "metrics",
                "operation_path": operation_path, "pulled_at_utc": pulled_at_utc, "pull_id": pull_id,
                "metric_set": metric_set,
            })
    return out


def dimension_values_from_response(response: dict, *, universe_id: str, request: dict, operation_path: str,
                                   pulled_at_utc: str, pull_id: str) -> list[dict]:
    out = []
    for dim in (response.get("response") or {}).get("values") or []:
        for item in dim.get("values") or []:
            out.append({
                "schema_version": SCHEMA_VERSION, "tool_version": TOOL_VERSION, "kind": "dimension_value",
                "universe_id": universe_id, "metric": request["metric"], "dimension": dim.get("dimension"),
                "value": item.get("value"), "display_value": item.get("displayValue"),
                "filter": list(request.get("filter") or []), "request": request, "endpoint": "dimension-values",
                "operation_path": operation_path, "pulled_at_utc": pulled_at_utc, "pull_id": pull_id,
            })
    return out


def append_points(base: Path, records: list[dict]) -> int:
    by_metric: dict[str, list[dict]] = {}
    for rec in records:
        by_metric.setdefault(rec["metric"], []).append(rec)
    for metric, recs in by_metric.items():
        append_jsonl(metric_path(base, metric), recs)
    return len(records)


def read_points(base: Path, metric: str, granularity: str | None = None) -> list[dict]:
    recs = [r for r in read_jsonl(metric_path(base, metric)) if r.get("kind") == "metric_point"]
    if granularity:
        recs = [r for r in recs if r.get("granularity") == granularity]
    return recs


def bucket_key(rec: dict) -> tuple:
    """Identity of one bucket: same metric, granularity, breakdown, series, filter and bucket time."""
    def canon(x):
        return json.dumps(x, sort_keys=True)
    return (rec["metric"], rec["granularity"], canon(rec.get("breakdown") or []), canon(rec.get("series") or []),
            canon(rec.get("filter") or []), rec["bucket_time_utc"])


def revisions(records: list[dict]) -> dict[tuple, list[dict]]:
    """bucket key -> every observation of it, oldest pull first."""
    out: dict[tuple, list[dict]] = {}
    for rec in records:
        out.setdefault(bucket_key(rec), []).append(rec)
    for recs in out.values():
        recs.sort(key=lambda r: r["pulled_at_utc"])
    return out


def latest(records: list[dict]) -> list[dict]:
    """The newest observation per bucket, sorted by series then bucket time. Each carries `revision_count`
    and `final` (False for Projected, NotStatisticallySignificant, or a status this tool does not know)."""
    out = []
    for recs in revisions(records).values():
        rec = dict(recs[-1])
        rec["revision_count"] = len(recs)
        status = rec.get("point_status")
        rec["final"] = status is None or status == "Valid"
        out.append(rec)
    out.sort(key=lambda r: (json.dumps(r.get("series") or [], sort_keys=True), json.dumps(r.get("filter") or [],
                                                                                         sort_keys=True),
                            r["bucket_time_utc"]))
    return out


def append_pull(base: Path, row: dict) -> None:
    append_jsonl(base / "pulls.jsonl", [{"schema_version": SCHEMA_VERSION, "tool_version": TOOL_VERSION,
                                         "kind": "pull", **row}])


def read_pulls(base: Path) -> list[dict]:
    return [r for r in read_jsonl(base / "pulls.jsonl") if r.get("kind") == "pull"]


def append_experiment(base: Path, kind: str, row: dict) -> None:
    if kind not in ("list", "get", "stats"):
        raise ValueError(kind)
    append_jsonl(base / "experiments" / f"{kind}.jsonl",
                 [{"schema_version": SCHEMA_VERSION, "tool_version": TOOL_VERSION, "kind": f"experiment_{kind}",
                   **row}])
