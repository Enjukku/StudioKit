#!/usr/bin/env python3
"""Roblox public-counter collector: playing, visits, favorites, upvotes, downvotes per watched universe.

Routes (documented, unauthenticated; knowledge/reference/trends/01-roblox-data-loops.md §3):
  roblox.games          R1 GET games.roblox.com/v1/games?universeIds=...        playing, visits, favoritedCount
  roblox.votes          R2 GET games.roblox.com/v1/games/votes?universeIds=...  upVotes, downVotes
Favorites come from R1 (favoritedCount), so R3 (favorites/count per universe) is not called. At most
MAX_IDS ids per call whatever config.json says (the ruling's condition). Place -> universe lookup (R4) is
ruled not_allowed and not built: resolve by hand.

Before any request every route's registry row must say "allowed" (trend_registry.require_allowed). A 429
that stops the client ends the run; batches already fetched are kept. A failed batch is a gap.
Identity: universe_id is the key; root_place_id is a label. Names: label "name" is the API name (R1 only);
label "watchlist_label" is the studio's own label from the watchlist. A universe missing from a response or
a value that is not a finite non-negative number writes no record (gaps stay gaps).

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from trend_http import FetchFailed
from trend_registry import permission_version, require_allowed
from trend_store import make_record, parse_utc, utc_iso

COLLECTOR_VERSION = "roblox_collector/0.1.0"
ENTITY_TYPE = "roblox_universe"
GAMES_URL = "https://games.roblox.com/v1/games?universeIds={ids}"
VOTES_URL = "https://games.roblox.com/v1/games/votes?universeIds={ids}"
MAX_IDS = 50  # documented maximum ids per call (sources.json roblox.games conditions)
# raw field -> (metric, unit)
GAMES_FIELDS = {"playing": ("playing", "players"), "visits": ("visits", "visits"),
                "favoritedCount": ("favorites", "favorites")}
VOTES_FIELDS = {"upVotes": ("upvotes", "votes"), "downVotes": ("downvotes", "votes")}


def load_watchlist(path: Path) -> list[dict]:
    games = json.loads(path.read_text(encoding="utf-8"))["games"]
    for g in games:
        if not str(g.get("universe_id") or "").isdigit():
            raise ValueError(f"watchlist entry without a numeric universe_id: {g}")
    return games


def in_event(game: dict, when: datetime) -> bool:
    return any(parse_utc(w["start_utc"]) <= when < parse_utc(w["end_utc"]) for w in game.get("event_windows", []))


def _count(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and v >= 0


def _parse(body: bytes, fields: dict, row: dict, observed_at: datetime, games: dict[str, dict],
           label_keys: dict[str, str]) -> list[dict]:
    out = []
    for item in json.loads(body).get("data", []):
        uid = str(item.get("id", ""))
        game = games.get(uid)
        if game is None:  # not requested: ignore
            continue
        labels = {"watchlist_label": game.get("label")}
        if game.get("root_place_id"):
            labels["root_place_id"] = str(game["root_place_id"])
        for raw, key in label_keys.items():
            if item.get(raw) is not None:
                labels[key] = str(item[raw])
        for raw, (metric, unit) in fields.items():
            if not _count(item.get(raw)):
                continue
            out.append(make_record(
                source=row["id"], entity_type=ENTITY_TYPE, entity_id=uid, metric=metric, value=item[raw],
                unit=unit, observed_at_utc=utc_iso(observed_at), source_sample_at_utc=None,
                provenance="official", permission_version=permission_version(row),
                collector_version=COLLECTOR_VERSION, event_flag=in_event(game, observed_at), labels=labels))
    return out


def parse_games(body: bytes, row: dict, observed_at: datetime, games: dict[str, dict]) -> list[dict]:
    return _parse(body, GAMES_FIELDS, row, observed_at, games,
                  {"name": "name", "rootPlaceId": "root_place_id", "created": "created", "updated": "updated"})


def parse_votes(body: bytes, row: dict, observed_at: datetime, games: dict[str, dict]) -> list[dict]:
    return _parse(body, VOTES_FIELDS, row, observed_at, games, {})


def collect(watchlist: list[dict], rows: dict, client, batch_size: int, now=lambda: datetime.now(timezone.utc),
            log=print) -> list[dict]:
    """One sample of every watched universe. Raises PermissionRefused before any request if a row is not
    allowed. A failed batch is logged and skipped (its gap stays a gap); a 429 that stops the client ends the
    run and returns the batches already fetched."""
    games_row = require_allowed(rows, "roblox.games")
    votes_row = require_allowed(rows, "roblox.votes")
    games = {str(g["universe_id"]): g for g in watchlist}
    ids = list(games)
    records: list[dict] = []
    batch_size = min(batch_size, MAX_IDS)
    for i in range(0, len(ids), batch_size):
        chunk = ",".join(ids[i:i + batch_size])
        for url, parse, row in ((GAMES_URL, parse_games, games_row), (VOTES_URL, parse_votes, votes_row)):
            try:
                body = client.get(url.format(ids=chunk))
            except FetchFailed as err:
                log(f"skip: {err}")
                if client.stopped:
                    log(f"stopped: no further Roblox request this run ({client.stopped})")
                    return records
                continue
            try:
                records += parse(body, row, now(), games)
            except ValueError as err:
                log(f"skip: unreadable response from {row['id']} ({err})")
    return records
