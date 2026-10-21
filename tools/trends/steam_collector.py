#!/usr/bin/env python3
"""Steam current players: one GetNumberOfCurrentPlayers call per watched app id per run.

Route (registry row steam.current_players; ruling unclear until the owner decides, J004 digest):
  GET https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}&key=<env>
The key comes only from env STEAM_WEB_API_KEY and is added by trend_keys.KeyedFetch at fetch time, so it is
never in a URL the tool logs, a record or an error text. Cache-Control max-age is respected: the record
keeps fresh_until_utc and the next run skips the app until then. Fail soft: a refused, failed or
unreadable app writes no record and the run goes on (Valve can end access without notice).

Records: entity_type steam_app, entity_id = app id, metric current_players (unit players), provenance
official, source_sample_at_utc from the Date header.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import trend_store
from trend_http import FetchFailed, PoliteClient, urllib_fetch
from trend_keys import KeyedFetch, key_from_env
from trend_registry import permission_version, require_allowed
from trend_store import make_record, parse_utc, utc_iso

SOURCE = "steam.current_players"
KEY_ENV = "STEAM_WEB_API_KEY"
COLLECTOR_VERSION = "steam_collector/0.1.0"
URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}"
MAX_AGE = re.compile(r"max-age\s*=\s*(\d+)", re.I)


def check_apps(panel: dict) -> list[dict]:
    apps = panel.get("apps", [])
    for app in apps:
        if not str(app.get("app_id") or "").isdigit():
            raise ValueError(f"steam panel entry without a numeric app_id: {app}")
    return apps


def parse(body: bytes, headers: dict, row: dict, app: dict, observed_at: datetime) -> list[dict]:
    """{"response": {"player_count": N, "result": 1}} -> one record; result != 1 or a bad count -> none."""
    resp = json.loads(body).get("response", {})
    count = resp.get("player_count")
    if resp.get("result") != 1 or not isinstance(count, int) or isinstance(count, bool) or count < 0:
        return []
    lower = {k.lower(): v for k, v in headers.items()}
    labels = {"name": app.get("label")}
    m = MAX_AGE.search(lower.get("cache-control", ""))
    if m:
        labels["fresh_until_utc"] = utc_iso(observed_at + timedelta(seconds=int(m.group(1))))
    try:
        sample_at = utc_iso(parsedate_to_datetime(lower["date"]))
    except (KeyError, TypeError, ValueError):
        sample_at = None
    return [make_record(
        source=row["id"], entity_type="steam_app", entity_id=str(app["app_id"]), metric="current_players",
        value=count, unit="players", observed_at_utc=utc_iso(observed_at), source_sample_at_utc=sample_at,
        provenance="official", permission_version=permission_version(row), collector_version=COLLECTOR_VERSION,
        labels=labels)]


def _fresh_until(app_id: str, base) -> datetime | None:
    last = trend_store.read(base, source=SOURCE, entity_id=app_id)
    stamp = last[-1]["labels"].get("fresh_until_utc") if last else None
    return parse_utc(stamp) if stamp else None


def collect(panel: dict, rows: dict, settings: dict, fetch=urllib_fetch, now=lambda: datetime.now(timezone.utc),
            log=print, base=None) -> list[dict]:
    row = require_allowed(rows, SOURCE)
    apps = check_apps(panel)
    keyed = KeyedFetch(fetch, "key", key_from_env(KEY_ENV))
    client = PoliteClient(settings, fetch=keyed)
    records: list[dict] = []
    for app in apps:
        app_id = str(app["app_id"])
        fresh = _fresh_until(app_id, base)
        if fresh and now() < fresh:
            log(f"skip: steam app {app_id} cached by Steam until {utc_iso(fresh)} (Cache-Control)")
            continue
        try:
            body = client.get(URL.format(app_id=app_id))
            got = parse(body, keyed.last_headers, row, app, now())
        except FetchFailed as err:
            log(f"skip: steam app {app_id}: {err}")
            continue
        except (ValueError, AttributeError) as err:
            log(f"skip: steam app {app_id}: unreadable response ({type(err).__name__})")
            continue
        if not got:
            log(f"skip: steam app {app_id}: no player count in response")
        records += got
    return records
