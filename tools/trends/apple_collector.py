#!/usr/bin/env python3
"""Apple App Store RSS ranks: one fetch per country and feed per run from the fixed panel in the watchlist.

Route (registry row apple.rss, ruling allowed J004-T04):
  GET https://rss.marketingtools.apple.com/api/v2/{country}/apps/{feed}/{limit}/apps.json
  feed in top-free, top-paid (top-grossing is not built: unverified); limit 10, 25 or 50.

Records: entity_type apple_app, entity_id = Apple app id, metric rank (unit rank, 1 = top), provenance
official; country and feed are labels. A rank is an ordinal position, never download growth. The feed has
no category filter: items get a genres label only when the feed lists genres, and are never called "game"
otherwise. A failed fetch (e.g. HTTP 504) writes nothing; the client makes no retries (apple_max_retries,
"one retry next day, no loops"). A 429 that stops the client ends the run. Every feed logs how many items
it listed, how many were stored and how many were skipped (id not numeric).

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

from trend_http import FetchFailed, PoliteClient, urllib_fetch
from trend_registry import permission_version, require_allowed
from trend_store import make_record, utc_iso

SOURCE = "apple.rss"
COLLECTOR_VERSION = "apple_collector/0.1.0"
URL = "https://rss.marketingtools.apple.com/api/v2/{country}/apps/{feed}/{limit}/apps.json"
FEEDS = ("top-free", "top-paid")
LIMITS = (10, 25, 50)


def check_panel(panel: dict) -> tuple[list[str], list[str], int]:
    countries = [str(c).lower() for c in panel.get("countries", [])]
    feeds = list(panel.get("feeds", FEEDS))
    limit = int(panel.get("limit", 25))
    bad = [c for c in countries if len(c) != 2 or not c.isalpha()]
    if bad or any(f not in FEEDS for f in feeds) or limit not in LIMITS:
        raise ValueError(f"apple panel: countries must be 2-letter codes (bad: {bad}), feeds in {FEEDS}, "
                         f"limit in {LIMITS}; got feeds {feeds}, limit {limit}")
    return countries, feeds, limit


def _source_time(text) -> str | None:
    try:
        return utc_iso(parsedate_to_datetime(text))
    except (TypeError, ValueError):
        return None


def parse(body: bytes, row: dict, country: str, feed: str, observed_at: datetime, log=lambda line: None) -> list[dict]:
    """Feed JSON -> one rank record per listed app. Raises ValueError if the body is not this feed."""
    data = json.loads(body)["feed"]
    if str(data.get("country", "")).lower() != country:
        raise ValueError(f"feed country {data.get('country')!r} is not the requested {country!r}")
    sample_at = _source_time(data.get("updated"))
    out = []
    results = data.get("results", [])
    for rank, item in enumerate(results, start=1):
        app_id = str(item.get("id", ""))
        if not app_id.isdigit():
            continue
        labels = {"name": item.get("name"), "country": country, "feed": feed, "kind": item.get("kind")}
        genres = [g.get("name") for g in item.get("genres") or [] if isinstance(g, dict) and g.get("name")]
        if genres:
            labels["genres"] = genres
        out.append(make_record(
            source=row["id"], entity_type="apple_app", entity_id=app_id, metric="rank", value=rank, unit="rank",
            observed_at_utc=utc_iso(observed_at), source_sample_at_utc=sample_at, provenance="official",
            permission_version=permission_version(row), collector_version=COLLECTOR_VERSION, labels=labels))
    log(f"apple {country}/{feed}: feed listed {len(results)} items; stored {len(out)}; "
        f"skipped {len(results) - len(out)} (id not numeric)")
    return out


def collect(panel: dict, rows: dict, settings: dict, fetch=urllib_fetch, now=lambda: datetime.now(timezone.utc),
            log=print, base=None) -> list[dict]:
    row = require_allowed(rows, SOURCE)
    countries, feeds, limit = check_panel(panel)
    client = PoliteClient({**settings, "max_retries": settings["apple_max_retries"]}, fetch=fetch)
    records: list[dict] = []
    for country in countries:
        for feed in feeds:
            try:
                body = client.get(URL.format(country=country, feed=feed, limit=limit))
                records += parse(body, row, country, feed, now(), log)
            except FetchFailed as err:
                log(f"skip: {err}")
                if client.stopped:
                    log(f"stopped: no further Apple request this run ({client.stopped})")
                    return records
            except (ValueError, KeyError, TypeError) as err:
                log(f"skip: unreadable Apple feed {country}/{feed} ({err})")
    return records
