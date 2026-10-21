#!/usr/bin/env python3
"""Source-permission registry (tools/trends/sources.json). Every collector calls require_allowed() before
any network request; a ruling other than "allowed", or a date after the row's optional valid_until (inclusive,
YYYY-MM-DD, UTC), raises PermissionRefused and no request is made.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

from trend_store import TOOL_DIR, prune

FIELDS = ("id", "name", "route", "purpose", "auth", "quota", "storage_limit_days", "terms_url", "ruling",
          "checked_on", "notes")
RULINGS = ("allowed", "manual", "not_allowed", "unclear")


class PermissionRefused(Exception):
    pass


def load(path: Path | None = None) -> dict[str, dict]:
    """sources.json -> {id: row}. Raises ValueError on a malformed row."""
    raw = json.loads((path or TOOL_DIR / "sources.json").read_text(encoding="utf-8"))
    rows: dict[str, dict] = {}
    for row in raw["sources"]:
        missing = [f for f in FIELDS if f not in row]
        if missing:
            raise ValueError(f"source {row.get('id')!r} missing fields {missing}")
        if row["ruling"] not in RULINGS:
            raise ValueError(f"source {row['id']!r} ruling {row['ruling']!r} not in {RULINGS}")
        if row["id"] in rows:
            raise ValueError(f"duplicate source id {row['id']!r}")
        rows[row["id"]] = row
    return rows


def permission_version(row: dict) -> str:
    """The registry state a record was collected under, stored on every record."""
    return f"{row['id']}:{row['ruling']}:{row['checked_on']}"


def require_allowed(rows: dict[str, dict], source_id: str, today: date | None = None) -> dict:
    """Return the row if automated access is allowed today, else raise PermissionRefused (with the reason)."""
    row = rows.get(source_id)
    if row is None:
        raise PermissionRefused(f"{source_id}: no registry row in sources.json; no request made")
    if row["ruling"] != "allowed":
        raise PermissionRefused(
            f"{source_id}: registry ruling is '{row['ruling']}' (checked {row['checked_on']}), not 'allowed'; "
            f"no request made. Notes: {row['notes']}")
    until = row.get("valid_until")
    today = today or datetime.now(timezone.utc).date()
    if until and today > date.fromisoformat(until):
        raise PermissionRefused(
            f"{source_id}: ruling 'allowed' expired after {until} (UTC); no request made. Notes: {row['notes']}")
    return row


def prune_all(rows: dict[str, dict], now: datetime, base: Path | None = None) -> tuple[dict[str, int], dict[str, str]]:
    """Apply storage_limit_days for every source that has one. A source whose file cannot be read or replaced
    is skipped and reported; the others are still pruned. Returns ({source: removed}, {source: error})."""
    removed, failed = {}, {}
    for sid, row in rows.items():
        if row["storage_limit_days"] is None:
            continue
        try:
            removed[sid] = prune(sid, int(row["storage_limit_days"]), now, base)
        except OSError as err:
            failed[sid] = str(err)
    return removed, failed
