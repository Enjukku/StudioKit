#!/usr/bin/env python3
"""Analyst data tool: command line. Pulls the owner's own game metrics (Open Cloud Analytics Query API) and
experiment reads (Experiments API, read only) into append-only history, and runs the stats helper.

Usage (every network command needs --universe ID or --game-config PATH with {"universe_id": ...}):
  python tools/analytics/analytics.py sets                                   # metric sets and catalog size
  python tools/analytics/analytics.py pull --set weekly|performance --universe ID
  python tools/analytics/analytics.py pull-funnel --funnel NAME --universe ID
  python tools/analytics/analytics.py pull-metric --metric M --granularity G --start ISO --end ISO
                                      [--breakdown D ...] [--filter JSON] [--limit N] --universe ID
  python tools/analytics/analytics.py dims --metric M --dimension D [--dimension D2] [--days 90] --universe ID
  python tools/analytics/analytics.py experiments list|get|stats [--id EXPERIMENT_ID] --universe ID
  python tools/analytics/analytics.py status --universe ID                   # last pulls, 21-day warning
  python tools/analytics/analytics.py show --metric M [--granularity G] [--breakdown D|none] [--start ISO] [--end ISO]
                                      [--revisions] --universe ID
  python tools/analytics/analytics.py stats maturity|diff|welch|samplesize|samplesize-mean|srm|did|verdict ...

Output: JSON on stdout; one short human line on stderr. Exit 0 ok, 1 a pull or request failed, 2 refused
before any request (missing key, bad input, a request the docs say fails).

Key: env ROBLOX_ANALYTICS_API_KEY (the owner sets it; this tool never prints, logs or saves it).
Data: env ANALYTICS_DATA_DIR/<universe id>/, default <repo>/.tools/analytics-data/<universe id>/.
No scheduler: run on demand.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ax_client  # noqa: E402
import ax_pull  # noqa: E402
import ax_stats  # noqa: E402
import ax_store as st  # noqa: E402

EXIT_FAIL, EXIT_REFUSED = 1, 2


def _emit(obj: dict, line: str) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))
    print(line, file=sys.stderr)


def _now(arg: str | None) -> datetime:
    return st.parse_utc(arg) if arg else datetime.now(timezone.utc)


def _universe(args) -> str:
    if getattr(args, "universe", None):
        return st.check_universe(args.universe)
    if getattr(args, "game_config", None):
        data = json.loads(Path(args.game_config).read_text(encoding="utf-8"))
        return st.check_universe(data["universe_id"])
    raise ValueError("give --universe ID or --game-config PATH (a JSON file with \"universe_id\")")


def _client() -> ax_client.Client:
    ax_client.read_key()  # stop before any request when the key is missing
    return ax_client.Client()


def _pull_line(row: dict) -> str:
    failed = [f"{r['metric']}({r.get('code') or 'refused' if 'code' in r else 'stopped'})"
              for r in row["requests"] if not r["ok"]]
    text = (f"{row['metric_set']}: {'OK' if row['ok'] else 'PARTIAL/FAILED'}, {row['points']} points "
            f"({row['points_not_final']} not final: Projected or NotStatisticallySignificant)")
    return text + (f"; failed: {', '.join(failed)}" if failed else "")


def cmd_sets(args) -> int:
    sets = ax_pull.load_sets()
    out = {name: {"about": s.get("about"), "lookback_days": s.get("lookback_days"),
                  "queries": s["queries"], "discovery": s.get("discovery")} for name, s in sets["sets"].items()}
    _emit({"sets": out, "catalog_metrics": sorted(sets["catalog"])},
          f"{len(out)} sets; {len(sets['catalog'])} metrics in the catalog")
    return 0


def cmd_pull(args) -> int:
    uid, now = _universe(args), _now(args.now)
    row = ax_pull.pull_set(_client(), uid, args.set, now=now)
    _emit(row, _pull_line(row))
    return 0 if row["ok"] else EXIT_FAIL


def cmd_pull_funnel(args) -> int:
    uid, now = _universe(args), _now(args.now)
    res = ax_pull.pull_funnel(_client(), uid, args.funnel, now=now)
    ok = res["pull"] is not None and res["pull"]["ok"]
    line = (f"funnel {args.funnel}: {len(res['steps'])} steps found; "
            + (_pull_line(res["pull"]) if res["pull"] else "no step pull (discovery failed or found no steps)"))
    _emit(res, line)
    return 0 if ok else EXIT_FAIL


def cmd_pull_metric(args) -> int:
    uid, now = _universe(args), _now(args.now)
    sets = ax_pull.load_sets()
    query = {"metric": args.metric, "granularity": args.granularity}
    if args.breakdown:
        query["breakdown"] = args.breakdown
    if args.filter:
        query["filter"] = json.loads(args.filter)
    if args.limit is not None:
        query["limit"] = args.limit
    start, end = st.parse_utc(args.start), st.parse_utc(args.end)
    ax_pull.check_request(sets["catalog"], ax_pull.make_body(query, start, end), now)  # refuse before the key
    row = ax_pull.pull_queries(_client(), uid, [query], label="adhoc", now=now, catalog=sets["catalog"],
                               lookback_days=0, clamp=False, window=(start, end))
    _emit(row, _pull_line(row))
    return 0 if row["ok"] else EXIT_FAIL


def cmd_dims(args) -> int:
    uid, now = _universe(args), _now(args.now)
    end = ax_pull.day_floor(now)
    res = ax_pull.pull_dimensions(_client(), uid, args.metric, args.dimension, start=end - timedelta(days=args.days),
                                  end=end, now=now)
    _emit(res, f"{args.metric}: " + "; ".join(f"{d}: {len(v)} values" for d, v in res["values"].items()))
    return 0


def cmd_experiments(args) -> int:
    uid = _universe(args)
    rec = ax_pull.pull_experiments(_client(), uid, args.what, args.id)
    if args.what == "list":
        n = sum(len(p.get("experiments") or []) for p in rec["responses"])
        line = f"experiments list: {n} rows saved"
    elif args.what == "stats":
        stats = rec["final_operation"].get("experimentStats")
        line = f"experiment {args.id} stats saved; experimentStats = {json.dumps(stats)}"
    else:
        line = f"experiment {args.id} saved"
    _emit(rec, line)
    return 0


def cmd_status(args) -> int:
    uid, now = _universe(args), _now(args.now)
    res = ax_pull.status(st.data_dir(uid), now)
    res["data_dir"] = str(st.data_dir(uid))
    line = ("WARNING: " + " | ".join(res["warnings"])) if res["warnings"] else "all metric sets pulled within 21 days"
    _emit(res, line)
    return 0


def cmd_show(args) -> int:
    uid = _universe(args)
    sets = ax_pull.load_sets()
    res = ax_pull.show(st.data_dir(uid), args.metric, args.granularity,
                       start=st.parse_utc(args.start) if args.start else None,
                       end=st.parse_utc(args.end) if args.end else None,
                       with_revisions=args.revisions, catalog=sets["catalog"], breakdown=args.breakdown)
    _emit(res, f"{args.metric}: {len(res['points'])} buckets, {res['not_final']} not final, "
               f"{res['revised_buckets']} revised")
    return 0


def cmd_stats(args) -> int:
    k = args.kind
    if k == "maturity":
        res = ax_stats.cohort_maturity(date.fromisoformat(args.first_play), args.n, _now(args.now), args.lag_days)
        line = (f"D{args.n} of cohort {args.first_play}: {res['verdict']}"
                + ("" if res["mature"] else f" (readable from {res['readable_from_utc']})"))
    elif k == "diff":
        res = ax_stats.rate_difference(args.xa, args.na, args.xb, args.nb, args.conf, args.method)
        lo, hi = res["absolute_interval_pp"]
        rel = res["relative_difference_pct"]
        line = (f"B - A = {res['absolute_difference_pp']:+.2f} pp ({args.conf:.0%} CI {lo:+.2f} to {hi:+.2f} pp)"
                + (f"; relative {rel:+.1f} %" if rel is not None else ""))
    elif k == "samplesize":
        res = ax_stats.sample_size_proportions(args.pa, args.pb, args.alpha, args.power)
        line = (f"{res['n_per_arm']} players per arm for {args.pa} -> {args.pb} "
                f"(alpha {args.alpha}, two-sided, power {args.power})")
    elif k == "samplesize-mean":
        res = ax_stats.sample_size_means(args.sigma, args.delta, args.power)
        line = (f"{res['n_per_arm']} players per arm for delta {args.delta}, sigma {args.sigma}, power {args.power} "
                f"(alpha 0.05 two-sided). {res['warning']}")
    elif k == "srm":
        res = ax_stats.sample_ratio_check(args.counts, args.planned, args.alarm_p)
        line = f"SRM check p = {res['p_value']:.3g} (alarm when p < {args.alarm_p}): {res['verdict']}"
    elif k == "welch":
        res = ax_stats.welch_difference(args.ma, args.sa, args.na, args.mb, args.sb, args.nb, args.conf)
        lo, hi = res["interval"]
        line = (f"B - A = {res['difference']:+.6g} ({args.conf:.0%} CI {lo:+.6g} to {hi:+.6g}, Welch df "
                f"{res['df']:.1f}). {res['warning']}")
    elif k == "verdict":
        guards = json.loads(args.guardrails) if args.guardrails else None
        res = ax_stats.verdict(args.lower, args.upper, args.point, args.benefit, args.harm, guardrails=guards,
                               integrity_ok=not args.integrity_failed, matured=not args.not_mature,
                               stopping_ok=not args.stopping_failed, rule=args.rule)
        line = f"{res['verdict']}" + (f": {res['reason']}" if res["reason"] else "") + f" [{res['rule_label']}]"
    elif k == "mix":
        res = ax_stats.mix_decomposition(json.loads(Path(args.segments).read_text(encoding="utf-8"))
                                         if args.segments.endswith(".json") else json.loads(args.segments))
        line = (f"overall {res['overall_before']:.4f} -> {res['overall_after']:.4f} "
                f"({res['total_change_pp']:+.2f} pp): rate part {res['rate_effect_pp_before_weights']:+.2f} pp, "
                f"mix part {res['mix_effect_pp_before_weights']:+.2f} pp (before weights). {res['warning']}")
    elif k == "did":
        res = ax_stats.diff_in_diff(args.tb, args.ta, args.cb, args.ca, args.se)
        line = f"difference in differences = {res['did']:+.6g} (assumes parallel trends)"
    else:
        raise ValueError(k)
    _emit(res, line)
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    def net(p):
        p.add_argument("--universe", help="universe id (digits)")
        p.add_argument("--game-config", help='game-side JSON file with "universe_id"')
        p.add_argument("--now", help="override the clock (ISO UTC), for tests and replays")
        return p

    sub.add_parser("sets").set_defaults(fn=cmd_sets)
    p = net(sub.add_parser("pull"))
    p.add_argument("--set", required=True)
    p.set_defaults(fn=cmd_pull)
    p = net(sub.add_parser("pull-funnel"))
    p.add_argument("--funnel", required=True, help="funnel name exactly as logged by the game")
    p.set_defaults(fn=cmd_pull_funnel)
    p = net(sub.add_parser("pull-metric"))
    p.add_argument("--metric", required=True)
    p.add_argument("--granularity", required=True)
    p.add_argument("--start", required=True, help="inclusive, RFC 3339")
    p.add_argument("--end", required=True, help="exclusive, RFC 3339")
    p.add_argument("--breakdown", nargs="*")
    p.add_argument("--filter", help='JSON list, e.g. [{"dimension":"Platform","values":["Phone"],"operation":"In"}]')
    p.add_argument("--limit", type=int)
    p.set_defaults(fn=cmd_pull_metric)
    p = net(sub.add_parser("dims"))
    p.add_argument("--metric", required=True)
    p.add_argument("--dimension", required=True, action="append")
    p.add_argument("--days", type=int, default=90)
    p.set_defaults(fn=cmd_dims)
    p = net(sub.add_parser("experiments"))
    p.add_argument("what", choices=["list", "get", "stats"])
    p.add_argument("--id")
    p.set_defaults(fn=cmd_experiments)
    p = net(sub.add_parser("status"))
    p.set_defaults(fn=cmd_status)
    p = net(sub.add_parser("show"))
    p.add_argument("--metric", required=True)
    p.add_argument("--granularity")
    p.add_argument("--start")
    p.add_argument("--end")
    p.add_argument("--revisions", action="store_true")
    p.add_argument("--breakdown", help='only series pulled with this one breakdown (e.g. Platform); "none" = total only')
    p.set_defaults(fn=cmd_show)

    s = sub.add_parser("stats").add_subparsers(dest="kind", required=True)
    q = s.add_parser("maturity")
    q.add_argument("--first-play", required=True, help="cohort first-play date YYYY-MM-DD (UTC)")
    q.add_argument("--n", type=int, required=True, help="N of DN retention (1, 7, 30)")
    q.add_argument("--lag-days", type=int, default=ax_stats.DEFAULT_REPORTING_LAG_DAYS)
    q.add_argument("--now")
    q = s.add_parser("diff", help="two rates: A = control/before, B = treatment/after")
    for name in ("xa", "na", "xb", "nb"):
        q.add_argument(f"--{name}", type=int, required=True)
    q.add_argument("--conf", type=float, default=0.95)
    q.add_argument("--method", choices=["newcombe", "wald"], default="newcombe")
    q = s.add_parser("welch", help="two means: A = control/before, B = treatment/after")
    for name in ("ma", "sa", "mb", "sb"):
        q.add_argument(f"--{name}", type=float, required=True)
    for name in ("na", "nb"):
        q.add_argument(f"--{name}", type=int, required=True)
    q.add_argument("--conf", type=float, default=0.95)
    q = s.add_parser("verdict", help="PROPOSAL verdict rules (fact-check 02 section 5)")
    for name in ("lower", "upper", "point", "benefit", "harm"):
        q.add_argument(f"--{name}", type=float, required=True)
    q.add_argument("--guardrails", help='JSON list of {"name","lower","upper","margin"}')
    q.add_argument("--integrity-failed", action="store_true", help="SRM alarm or logging failure")
    q.add_argument("--not-mature", action="store_true")
    q.add_argument("--stopping-failed", action="store_true")
    q.add_argument("--rule", choices=["default", "strict"], default="default")
    q = s.add_parser("samplesize")
    q.add_argument("--pa", type=float, required=True)
    q.add_argument("--pb", type=float, required=True)
    q.add_argument("--alpha", type=float, default=0.05)
    q.add_argument("--power", type=float, default=0.8)
    q = s.add_parser("samplesize-mean")
    q.add_argument("--sigma", type=float, required=True)
    q.add_argument("--delta", type=float, required=True)
    q.add_argument("--power", type=float, default=0.8)
    q = s.add_parser("srm")
    q.add_argument("--counts", type=int, nargs="+", required=True)
    q.add_argument("--planned", type=float, nargs="+")
    q.add_argument("--alarm-p", type=float, default=ax_stats.SRM_ALARM_P)
    q = s.add_parser("did", help="difference in differences")
    for name in ("tb", "ta", "cb", "ca"):
        q.add_argument(f"--{name}", type=float, required=True)
    q.add_argument("--se", type=float, nargs=4)
    q = s.add_parser("mix", help="split a rate change into segment-rate and player-mix parts")
    q.add_argument("--segments", required=True,
                   help='JSON list or a .json file: [{"name","n_before","rate_before","n_after","rate_after"}, ...]')
    for q in s.choices.values():
        q.set_defaults(fn=cmd_stats)
    return ap


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except ax_client.MissingKey as err:
        print(f"REFUSED: {err}", file=sys.stderr)
        return EXIT_REFUSED
    except (ax_pull.RequestRefused, ValueError, KeyError, FileNotFoundError) as err:
        print(f"REFUSED: {err}", file=sys.stderr)
        return EXIT_REFUSED
    except ax_client.ApiError as err:  # message already redacted
        print(f"FAILED: {err}", file=sys.stderr)
        return EXIT_FAIL


if __name__ == "__main__":
    raise SystemExit(main())
