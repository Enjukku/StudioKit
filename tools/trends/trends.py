#!/usr/bin/env python3
"""Trend scout data tools: command line.

Usage:
  python tools/trends/trends.py registry                      # list sources and their rulings
  python tools/trends/trends.py collect-roblox [--watchlist P] # one sample of every watched universe
  python tools/trends/trends.py page [--as-of ISO] [--out DIR] [--watchlist P]
  python tools/trends/trends.py prune [--now ISO]             # apply storage_limit_days (records and pages)
  python tools/trends/trends.py collect-apple|collect-steam|collect-youtube [--watchlist P]  # outside panels
  python tools/trends/trends.py import-manual CSV              # rows read by hand (tools/trends/manual/)

Data: env TREND_DATA_DIR (default <repo>/.tools/trend-data/). Watchlist: <data_dir>/watchlist.json
(copy tools/trends/watchlist.example.json). Network commands exit 2 without any request when the
registry ruling is not "allowed". Every command except registry first applies the storage limits (records and
pages), as prune does. No scheduling: run on demand.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import apple_collector  # noqa: E402
import manual_import  # noqa: E402
import outside_page  # noqa: E402
import steam_collector  # noqa: E402
import trend_registry  # noqa: E402
import trend_store  # noqa: E402
import youtube_collector  # noqa: E402
from roblox_collector import collect, load_watchlist  # noqa: E402
from trend_http import FetchFailed, PoliteClient, urllib_fetch  # noqa: E402
from trend_keys import MissingKey  # noqa: E402
from trend_page import ROBLOX_SOURCES, write_pages  # noqa: E402

EXIT_REFUSED = 2
# command -> (key under watchlist "outside", collector module)
OUTSIDE = {"collect-apple": ("apple", apple_collector), "collect-steam": ("steam", steam_collector),
           "collect-youtube": ("youtube", youtube_collector)}


def _watchlist_path(arg: str | None) -> Path:
    path = Path(arg) if arg else trend_store.data_dir() / "watchlist.json"
    if not path.is_file():
        raise SystemExit(f"no watchlist at {path}; copy tools/trends/watchlist.example.json there")
    return path


def _watchlist(arg: str | None) -> list[dict]:
    return load_watchlist(_watchlist_path(arg))


def _outside(arg: str | None) -> dict:
    return json.loads(_watchlist_path(arg).read_text(encoding="utf-8")).get("outside", {})


def _prune(rows: dict, when: datetime, verbose: bool) -> bool:
    """Apply storage_limit_days to records and pages. Prints what it removed (all lines when verbose, else
    only removals) and every failure on stderr. Returns False if any file could not be pruned."""
    removed, failed = trend_registry.prune_all(rows, when)
    pages, page_failed = outside_page.prune_pages(rows, when, trend_store.data_dir())
    lines = [f"{sid}: removed {n}" for sid, n in removed.items() if verbose or n]
    lines += [f"deleted page {path} (past its storage limit)" for path in pages]
    if verbose:
        print("\n".join(lines) or "no source has a storage limit")
    elif lines:
        print("prune: " + "; ".join(lines), file=sys.stderr)
    for what, err in list(failed.items()) + [(f, "") for f in page_failed]:
        print(f"PRUNE FAILED: {what} {err}".rstrip() + "; run prune again", file=sys.stderr)
    return not (failed or page_failed)


def main(argv: list[str] | None = None, fetch=urllib_fetch) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("registry")
    c = sub.add_parser("collect-roblox")
    c.add_argument("--watchlist")
    p = sub.add_parser("page")
    p.add_argument("--as-of", help="ISO UTC time; default now. The week is the 7 complete UTC days before it")
    p.add_argument("--out", type=Path)
    p.add_argument("--watchlist")
    pr = sub.add_parser("prune")
    pr.add_argument("--now")
    for name in OUTSIDE:
        sub.add_parser(name).add_argument("--watchlist")
    sub.add_parser("import-manual").add_argument("csv", type=Path)
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    rows = trend_registry.load()
    cfg = trend_store.load_config()
    now = datetime.now(timezone.utc)

    if args.cmd == "registry":
        for row in rows.values():
            print(f"{row['id']:<24} {row['ruling']:<12} checked {row['checked_on']}  "
                  f"limit {row['storage_limit_days']} days  {row['route']}")
        return 0

    if args.cmd == "prune":
        return 0 if _prune(rows, trend_store.parse_utc(args.now) if args.now else now, verbose=True) else 1
    _prune(rows, now, verbose=False)

    if args.cmd == "collect-roblox":
        client = PoliteClient(cfg["collector"], fetch=fetch)
        try:
            recs = collect(_watchlist(args.watchlist), rows, client, int(cfg["collector"]["batch_size"]))
        except trend_registry.PermissionRefused as err:
            print(f"REFUSED: {err}", file=sys.stderr)
            return EXIT_REFUSED
        except FetchFailed as err:
            print(f"FAILED: {err}", file=sys.stderr)
            return 1
        trend_store.append(recs)
        print(f"stored {len(recs)} observations in {trend_store.data_dir()}")
        return 0

    if args.cmd in OUTSIDE:
        key, module = OUTSIDE[args.cmd]
        try:
            recs = module.collect(_outside(args.watchlist).get(key, {}), rows, cfg["collector"], fetch=fetch)
        except trend_registry.PermissionRefused as err:
            print(f"REFUSED: {err}", file=sys.stderr)
            return EXIT_REFUSED
        except (MissingKey, ValueError) as err:
            print(f"FAILED: {err}", file=sys.stderr)
            return 1
        trend_store.append(recs)
        print(f"stored {len(recs)} observations in {trend_store.data_dir()}")
        return 0

    if args.cmd == "import-manual":
        n_rec, n_notes, skipped, rejected = manual_import.import_csv(args.csv, rows)
        print(f"stored {n_rec} records and {n_notes} notes; skipped {skipped} already imported; "
              f"rejected {len(rejected)} rows")
        for line in rejected:
            print(f"REJECTED {line}", file=sys.stderr)
        return 1 if rejected else 0

    if args.cmd == "page":
        as_of = trend_store.parse_utc(args.as_of) if args.as_of else now
        records = [rec for sid in ROBLOX_SOURCES for rec in trend_store.read(source=sid)]
        outside_ids = list(outside_page.OUTSIDE_SOURCES) + outside_page.manual_sources(rows)
        outside_recs = [rec for sid in outside_ids for rec in trend_store.read(source=sid)]
        secs, marker = outside_page.build(outside_recs, manual_import.read_notes(), _outside(args.watchlist),
                                          as_of, rows, cfg["thresholds"])
        out = args.out or trend_store.data_dir() / "pages"
        md, page = write_pages(records, _watchlist(args.watchlist), as_of, rows, cfg["thresholds"], out,
                               (outside_page.render_markdown(secs, marker), outside_page.render_html(secs, marker)),
                               list(ROBLOX_SOURCES) + outside_ids)
        print(f"wrote {md}\nwrote {page}")
        if marker and not out.resolve().is_relative_to(trend_store.data_dir().resolve()):
            print("WARNING: this page holds YouTube API data outside the data dir, where `prune` cannot "
                  "delete it. Delete it within 30 days of the oldest fetch.", file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
