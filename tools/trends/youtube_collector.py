#!/usr/bin/env python3
"""YouTube Data API panel: public statistics of a fixed video panel (registry row youtube.data, allowed).

Panel (watchlist "outside.youtube"):
  channels  channel ids -> uploads playlist (channels.list, 1 unit) -> newest uploads (playlistItems.list)
  videos    explicit video ids
  queries   optional topic searches (search.list, type=video, publishedAfter/publishedBefore), capped by
            collector.youtube_search_daily_budget in config.json over any trailing 24 hours (stricter than
            the per-day quota). Every attempted search is logged (time only) in <data_dir>/state/.
Statistics come from videos.list in batches of up to 50 ids. The key comes only from env YOUTUBE_API_KEY
and is added at fetch time by trend_keys.KeyedFetch.

Records: entity_type youtube_video, entity_id = video id, metrics views, likes, comments (a hidden count
writes no record), provenance official. Labels: channel_id, published_at, title, panel. Creators only by
channel id; no channel scores, channel rankings, genre labels or blends with outside data.
Storage: every value expires 30 days after fetch (registry storage_limit_days 30; `trends.py prune`).

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode

import trend_store
from trend_http import FetchFailed, PoliteClient, urllib_fetch
from trend_keys import KeyedFetch, key_from_env
from trend_registry import permission_version, require_allowed
from trend_store import make_record, parse_utc, utc_iso

SOURCE = "youtube.data"
KEY_ENV = "YOUTUBE_API_KEY"
COLLECTOR_VERSION = "youtube_collector/0.1.0"
API = "https://www.googleapis.com/youtube/v3/"
BATCH = 50  # documented maximum ids per channels.list / videos.list call
# statistics field -> (metric, unit)
STATS = {"viewCount": ("views", "views"), "likeCount": ("likes", "likes"), "commentCount": ("comments", "comments")}


def _search_log_path(base) -> Path:
    return (base or trend_store.data_dir()) / "state" / "youtube_search_calls.json"


def _recent_searches(base, now: datetime) -> list[str]:
    path = _search_log_path(base)
    stamps = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else []
    return [s for s in stamps if now - parse_utc(s) < timedelta(hours=24)]


def _log_search(base, stamps: list[str]) -> None:
    path = _search_log_path(base)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stamps), encoding="utf-8")


def _get(client, method: str, params: dict) -> dict:
    return json.loads(client.get(API + method + "?" + urlencode(params)))


def parse_videos(body: dict, row: dict, origins: dict[str, list[str]], observed_at: datetime) -> list[dict]:
    out = []
    for item in body.get("items", []):
        vid = str(item.get("id", ""))
        if vid not in origins:
            continue
        snip = item.get("snippet", {})
        labels = {"channel_id": snip.get("channelId"), "published_at": snip.get("publishedAt"),
                  "title": snip.get("title"), "panel": ",".join(origins[vid])}
        for raw, (metric, unit) in STATS.items():
            text = str(item.get("statistics", {}).get(raw, ""))
            if not text.isdigit():
                continue
            out.append(make_record(
                source=row["id"], entity_type="youtube_video", entity_id=vid, metric=metric, value=int(text),
                unit=unit, observed_at_utc=utc_iso(observed_at), provenance="official",
                permission_version=permission_version(row), collector_version=COLLECTOR_VERSION, labels=labels))
    return out


def collect(panel: dict, rows: dict, settings: dict, fetch=urllib_fetch, now=lambda: datetime.now(timezone.utc),
            log=print, base=None) -> list[dict]:
    row = require_allowed(rows, SOURCE)
    client = PoliteClient(settings, fetch=KeyedFetch(fetch, "key", key_from_env(KEY_ENV)))
    origins: dict[str, list[str]] = {}

    def add(vid, origin):
        if vid:
            origins.setdefault(str(vid), []).append(origin)

    def step(what, call):
        try:
            return call()
        except FetchFailed as err:
            log(f"skip: {what}: {err}")
        except (ValueError, AttributeError, TypeError) as err:
            log(f"skip: {what}: unreadable response ({type(err).__name__})")
        return None

    channels = [str(c["channel_id"]) for c in panel.get("channels", [])]
    for i in range(0, len(channels), BATCH):
        chunk = channels[i:i + BATCH]
        body = step("channels.list", lambda: _get(client, "channels", {"part": "contentDetails", "id": ",".join(chunk)}))
        for ch in (body or {}).get("items", []):
            uploads = ch.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads")
            if not uploads:
                continue
            items = step(f"playlistItems.list {ch.get('id')}", lambda: _get(client, "playlistItems", {
                "part": "contentDetails", "playlistId": uploads,
                "maxResults": int(panel.get("uploads_per_channel", 10))}))
            for it in (items or {}).get("items", []):
                add(it.get("contentDetails", {}).get("videoId"), f"channel:{ch.get('id')}")
    for vid in panel.get("videos", []):
        add(vid, "video")
    budget = int(settings["youtube_search_daily_budget"])
    for q in panel.get("queries", []):
        stamps = _recent_searches(base, now())
        if len(stamps) >= budget:
            log(f"skip: search.list {q['q']!r}: daily search budget {budget} used (trailing 24 h)")
            continue
        _log_search(base, stamps + [utc_iso(now())])  # quota is spent even if the call fails
        params = {"part": "id", "type": "video", "q": q["q"], "maxResults": int(q.get("max_results", 25)),
                  "publishedAfter": utc_iso(now() - timedelta(days=int(q.get("days", 7)))),
                  "publishedBefore": utc_iso(now())}
        params.update({k: q[k] for k in ("regionCode", "relevanceLanguage") if q.get(k)})
        body = step(f"search.list {q['q']!r}", lambda: _get(client, "search", params))
        for it in (body or {}).get("items", []):
            add(it.get("id", {}).get("videoId"), f"query:{q['q']}")
    ids = list(origins)
    records: list[dict] = []
    for i in range(0, len(ids), BATCH):
        chunk = ids[i:i + BATCH]
        body = step("videos.list", lambda: _get(client, "videos", {"part": "snippet,statistics", "id": ",".join(chunk)}))
        if body:
            records += parse_videos(body, row, origins, now())
    return records
