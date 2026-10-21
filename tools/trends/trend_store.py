#!/usr/bin/env python3
"""History store for the trend scout: one observation per metric value, long format, JSONL per source.

Contract (builder B and every collector build on this; change only with a schema_version bump):
  - Layout: <data_dir>/observations/<source>.jsonl, one JSON record per line, append-only.
    data_dir = env TREND_DATA_DIR, default <repo>/.tools/trend-data/ (gitignored).
  - Record fields (make_record fills the defaults):
      source               registry row id (tools/trends/sources.json), e.g. "roblox.games"
      entity_type          e.g. "roblox_universe", "steam_app"
      entity_id            stable string key (Roblox: universe_id). Names are never keys.
      metric, value, unit  value is a finite number; a missing value is NO record (gaps stay gaps)
      observed_at_utc      collector clock, ISO 8601 with Z
      source_sample_at_utc source clock if the source states one, else null
      provenance           official | third_party_sampled | third_party_estimate | developer_statement
                           | derived | manual_entry
      observed_or_imputed  observed | imputed (imputed is never written by a collector)
      event_flag, outage_flag  booleans
      schema_version, permission_version, collector_version
      labels               dict of mutable labels (name, root_place_id, ...); never used as keys
  - read() returns records sorted by observed_at_utc; prune() enforces storage_limit_days.
  - An unreadable line (a torn write) is skipped with a warning on stderr; it never stops read, prune or
    append. append always starts on a new line; prune drops unreadable lines (they cannot be dated).
  - event_flag is the window known at collection time; readers take event windows from the watchlist.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import math
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOL_DIR = Path(__file__).resolve().parent
SCHEMA_VERSION = 1
PROVENANCE = ("official", "third_party_sampled", "third_party_estimate", "developer_statement", "derived",
              "manual_entry")
OBSERVED_OR_IMPUTED = ("observed", "imputed")
REQUIRED = ("source", "entity_type", "entity_id", "metric", "value", "unit", "observed_at_utc", "provenance",
            "permission_version", "collector_version")


def data_dir() -> Path:
    env = os.environ.get("TREND_DATA_DIR")
    return Path(env) if env else ROOT / ".tools" / "trend-data"


def load_config(path: Path | None = None) -> dict:
    """config.json -> {"thresholds": {name: value}, "collector": {name: value}} (labels and sources dropped)."""
    raw = json.loads((path or TOOL_DIR / "config.json").read_text(encoding="utf-8"))
    return {group: {k: v["value"] for k, v in raw[group].items()} for group in ("thresholds", "collector")}


def utc_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + "Z"


def parse_utc(text: str) -> datetime:
    dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt.astimezone(timezone.utc)


def make_record(*, source: str, entity_type: str, entity_id, metric: str, value, unit: str,
                observed_at_utc: str, provenance: str, permission_version: str, collector_version: str,
                source_sample_at_utc: str | None = None, observed_or_imputed: str = "observed",
                event_flag: bool = False, outage_flag: bool = False, labels: dict | None = None) -> dict:
    rec = {
        "source": source, "entity_type": entity_type, "entity_id": str(entity_id), "metric": metric,
        "value": value, "unit": unit, "observed_at_utc": observed_at_utc,
        "source_sample_at_utc": source_sample_at_utc, "provenance": provenance,
        "observed_or_imputed": observed_or_imputed, "event_flag": event_flag, "outage_flag": outage_flag,
        "schema_version": SCHEMA_VERSION, "permission_version": permission_version,
        "collector_version": collector_version, "labels": dict(labels or {}),
    }
    validate(rec)
    return rec


def validate(rec: dict) -> None:
    """Raise ValueError if the record breaks the contract."""
    missing = [k for k in REQUIRED if rec.get(k) in (None, "")]
    if missing:
        raise ValueError(f"record missing {missing}")
    v = rec["value"]
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise ValueError(f"value must be a finite number, got {v!r}")
    if rec["provenance"] not in PROVENANCE:
        raise ValueError(f"provenance {rec['provenance']!r} not in {PROVENANCE}")
    if rec.get("observed_or_imputed") not in OBSERVED_OR_IMPUTED:
        raise ValueError(f"observed_or_imputed must be one of {OBSERVED_OR_IMPUTED}")
    parse_utc(rec["observed_at_utc"])
    if rec.get("source_sample_at_utc"):
        parse_utc(rec["source_sample_at_utc"])
    if not isinstance(rec.get("labels", {}), dict):
        raise ValueError("labels must be a dict")


def _path(base: Path, source: str) -> Path:
    if not source or any(c in source for c in "/\\:") or source.startswith("."):
        raise ValueError(f"bad source id {source!r}")
    return base / "observations" / f"{source}.jsonl"


def read_jsonl(path: Path) -> list[dict]:
    """Every readable JSON object line of path; an unreadable line is skipped with a warning."""
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
    """Append one JSON line per item, starting on a new line even if the file ends in a torn line."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lead = ""
    if path.is_file() and path.stat().st_size:
        with path.open("rb") as fh:
            fh.seek(-1, os.SEEK_END)
            lead = "" if fh.read(1) == b"\n" else "\n"
    text = "".join(json.dumps(i, sort_keys=True, ensure_ascii=False) + "\n" for i in items)
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(lead + text)


def append(records: list[dict], base: Path | None = None) -> int:
    base = base or data_dir()
    by_source: dict[str, list[dict]] = {}
    for rec in records:
        validate(rec)
        by_source.setdefault(rec["source"], []).append(rec)
    for source, recs in by_source.items():
        append_jsonl(_path(base, source), recs)
    return len(records)


def read(base: Path | None = None, *, source: str | None = None, entity_id=None, metric: str | None = None,
         start: datetime | None = None, end: datetime | None = None) -> list[dict]:
    """Records matching every given filter; start inclusive, end exclusive; sorted by observed_at_utc."""
    base = base or data_dir()
    folder = base / "observations"
    paths = [_path(base, source)] if source else sorted(folder.glob("*.jsonl")) if folder.is_dir() else []
    out = []
    for path in paths:
        if not path.is_file():
            continue
        for rec in read_jsonl(path):
            if entity_id is not None and rec["entity_id"] != str(entity_id):
                continue
            if metric is not None and rec["metric"] != metric:
                continue
            t = parse_utc(rec["observed_at_utc"])
            if (start and t < start) or (end and t >= end):
                continue
            out.append(rec)
    out.sort(key=lambda r: r["observed_at_utc"])
    return out


def prune(source: str, keep_days: int, now: datetime, base: Path | None = None) -> int:
    """Delete records of one source observed before now - keep_days, and unreadable lines. Returns the number
    of records removed. Raises OSError if the file cannot be read or replaced (e.g. locked); no .tmp is left."""
    path = _path(base or data_dir(), source)
    if not path.is_file():
        return 0
    cutoff = now - timedelta(days=keep_days)
    recs = read_jsonl(path)
    keep = [r for r in recs if parse_utc(r["observed_at_utc"]) >= cutoff]
    tmp = path.with_suffix(".jsonl.tmp")
    try:
        tmp.write_text("".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in keep),
                       encoding="utf-8", newline="\n")
        os.replace(tmp, path)
    except OSError:
        tmp.unlink(missing_ok=True)
        raise
    return len(recs) - len(keep)


def series(records: list[dict], metric: str) -> list[tuple[datetime, float]]:
    """[(observed_at, value)] for one metric, observed values only, sorted by time."""
    return sorted((parse_utc(r["observed_at_utc"]), float(r["value"])) for r in records
                  if r["metric"] == metric and r.get("observed_or_imputed") == "observed")
