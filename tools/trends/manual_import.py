#!/usr/bin/env python3
"""Manual-entry import: rows a person read by hand (fact-check-outside.md §4) into the trend store.

CSV layout (template: tools/trends/manual/manual-entries.template.csv; one file, a source column):
  source       registry id whose ruling is "manual" (any other ruling is rejected)
  read_date    ISO date or UTC time the page was read (not in the future)
  page         page URL or page name
  region       country or region as shown ("global" allowed); required for REGION_SOURCES
  window       time window shown on the page (e.g. "7 days"), optional
  entity_type  e.g. steam_app, play_app, hashtag, sound, category, title
  entity_id    app id, video id, hashtag or name exactly as shown
  entity_name  display name, optional
  metric       e.g. rank, peak_players, viewers, interest_0_100, release_date_announced
  value        finite number, or blank when the page shows no number
  unit         required when value is given
  kind         kind of figure: official, third_party_sampled, third_party_estimate, developer_statement;
               blank = manual_entry. Stored as the record's provenance. Money metrics (metric or unit naming
               revenue, earnings or robux) need third_party_estimate or developer_statement (formulas.md §5)
  note         short note, optional (not allowed for reddit and discord: no message copies)
Lines whose source starts with "#" are comments. Every row is checked on its own: a good row with a value
writes one record; a good row without a value writes one note to <data_dir>/manual/notes.jsonl; a bad row
(including one with more or fewer fields than the header) writes nothing and is listed with the reason. A
row identical to one already stored (source, entity_id, metric, read_date, value, page) is skipped and counted.
reddit and discord rows are rejected if any field holds a user path or handle (/user/, /u/, u/name, @name).

Python 3.11+ standard library only.
"""
from __future__ import annotations

import csv
import math
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import trend_store
from trend_registry import permission_version
from trend_store import make_record, parse_utc, utc_iso

COLLECTOR_VERSION = "manual_import/0.1.0"
COLUMNS = ("source", "read_date", "page", "region", "window", "entity_type", "entity_id", "entity_name",
           "metric", "value", "unit", "kind", "note")
KINDS = ("official", "third_party_sampled", "third_party_estimate", "developer_statement")
MONEY = re.compile(r"revenue|earning|robux", re.I)
MONEY_KINDS = ("third_party_estimate", "developer_statement")
REQUIRED = ("source", "read_date", "page", "entity_type", "entity_id", "metric")
# fact-check-outside.md §4: these pages differ by country or geography, so the row must say which
REGION_SOURCES = frozenset({"steam.charts", "google.play", "tiktok.creative-center", "tiktok.top-ads",
                            "google.trends"})
# no usernames or message copies from these (fact-check §4); /user/x, /u/x, u/x and @x are rejected in any field
NO_PEOPLE_SOURCES = frozenset({"reddit", "discord"})
PERSON_HANDLE = re.compile(r"(^|[^\w])(u|user)/\w|@\w", re.I)


def notes_path(base=None) -> Path:
    return (base or trend_store.data_dir()) / "manual" / "notes.jsonl"


def read_notes(base=None) -> list[dict]:
    path = notes_path(base)
    return trend_store.read_jsonl(path) if path.is_file() else []


def _key(item: dict) -> tuple:
    """Identity of an imported row: source, entity_id, metric, read time, value, page."""
    return (item["source"], item["entity_id"], item["metric"], item["observed_at_utc"], item.get("value"),
            item.get("labels", {}).get("page"))


def check_row(row: dict, registry: dict, now: datetime) -> tuple[dict | None, str | None]:
    """-> (record or note, None) for a good row, (None, reason) for a bad one."""
    missing = [c for c in REQUIRED if not row.get(c)]
    if missing:
        return None, f"missing {', '.join(missing)}"
    sid = row["source"]
    reg = registry.get(sid)
    if reg is None:
        return None, f"source {sid!r} is not in the registry"
    if reg["ruling"] != "manual":
        return None, f"source {sid!r} has ruling {reg['ruling']!r}, not 'manual'"
    try:
        read_at = parse_utc(row["read_date"])
    except ValueError:
        return None, f"read_date {row['read_date']!r} is not an ISO date or time"
    if read_at > now + timedelta(days=1):
        return None, f"read_date {row['read_date']!r} is in the future"
    if sid in REGION_SOURCES and not row.get("region"):
        return None, f"region is required for {sid}"
    if sid in NO_PEOPLE_SOURCES:
        if row.get("note"):
            return None, f"no notes for {sid} (no message copies)"
        if any(PERSON_HANDLE.search(v or "") for v in row.values()):
            return None, f"looks like a username; {sid} rows record topics only"
    kind = row.get("kind") or "manual_entry"
    if kind not in KINDS + ("manual_entry",):
        return None, f"kind {kind!r} is not one of {KINDS} (or blank for manual_entry)"
    if MONEY.search(row["metric"] + " " + (row.get("unit") or "")) and kind not in MONEY_KINDS:
        return None, f"money metric needs kind {' or '.join(MONEY_KINDS)} (other games' revenue is an estimate)"
    labels = {k: row[k] for k in ("page", "region", "window", "entity_name", "note") if row.get(k)}
    common = dict(source=sid, entity_type=row["entity_type"], entity_id=row["entity_id"], metric=row["metric"],
                  observed_at_utc=utc_iso(read_at), provenance=kind,
                  permission_version=permission_version(reg), collector_version=COLLECTOR_VERSION)
    if not row.get("value"):
        return {**common, "labels": labels, "imported_at_utc": utc_iso(now)}, None
    try:
        value = float(row["value"].replace(",", ""))
    except ValueError:
        return None, f"value {row['value']!r} is not a number"
    if not math.isfinite(value):
        return None, f"value {row['value']!r} is not finite"
    if not row.get("unit"):
        return None, "unit is required when value is given"
    value = int(value) if value.is_integer() else value
    return make_record(**common, value=value, unit=row["unit"], labels=labels), None


def import_csv(path: Path, registry: dict, now=None, base=None) -> tuple[int, int, int, list[str]]:
    """-> (records written, notes written, rows skipped as already imported, rejected lines "line N: reason")."""
    now = now or datetime.now(timezone.utc)
    records, notes, rejected, skipped = [], [], [], 0
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        unknown = set(reader.fieldnames or []) - set(COLUMNS)
        if unknown or "source" not in (reader.fieldnames or []):
            raise ValueError(f"{path}: header must use the columns {COLUMNS}; unknown {sorted(unknown)}")
        width = len(reader.fieldnames)
        for raw in reader:
            if (raw.get("source") or "").strip().startswith("#"):
                continue
            if None in raw or None in raw.values():  # DictReader: extra fields under None, missing ones None
                got = width + len(raw.get(None, [])) - sum(v is None for v in raw.values())
                rejected.append(f"line {reader.line_num}: {got} fields, the header has {width} "
                                "(a comma inside a field? wrap that field in double quotes)")
                continue
            row = {k: v.strip() for k, v in raw.items()}
            if not any(row.values()):
                continue
            item, reason = check_row(row, registry, now)
            if reason:
                rejected.append(f"line {reader.line_num}: {reason}")
            elif "value" in item:
                records.append(item)
            else:
                notes.append(item)
    sources = {i["source"] for i in records}
    seen = {_key(r) for s in sources for r in trend_store.read(base, source=s)} | {_key(n) for n in read_notes(base)}
    new_records, new_notes = [], []
    for item, out in [(r, new_records) for r in records] + [(n, new_notes) for n in notes]:
        if _key(item) in seen:
            skipped += 1
            continue
        seen.add(_key(item))
        out.append(item)
    trend_store.append(new_records, base)
    if new_notes:
        trend_store.append_jsonl(notes_path(base), new_notes)
    return len(new_records), len(new_notes), skipped, rejected
