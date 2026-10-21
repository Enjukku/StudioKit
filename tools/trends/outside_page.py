#!/usr/bin/env python3
"""Outside sections of the weekly page: Apple rank movement per country, Steam current players for watched
apps, YouTube panel view velocity, manual entries this week. Each platform stays in its own table; no number
is added across platforms. Labels as in templates/trends/weekly-report.md: [OFF] official, [DER] derived,
[MAN] manual entry.

Storage limits reach pages too: a page that shows values from a source with storage_limit_days (YouTube,
30 days) carries a marker "<!-- storage-limit source=<id> oldest=<UTC> -->"; prune_pages() deletes every
.md or .html under the data dir whose marker is older than the limit, and every file under <data_dir>/pages/
30 days after its last change, marker or not (lead decision J004-T12 finding 4: the scout's copies of pages
live there too). The scout's lasting record is <data_dir>/scout-log.md, outside pages/.

Each section uses records at or before as-of only. When the week holds no snapshot, the section shows the
latest snapshot before as-of, labelled "latest snapshot (outside the week window, <UTC>)", with no movement
or velocity: growth numbers use complete weeks only.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

import trend_metrics as tm
import trend_page as tp
from trend_store import parse_utc, utc_iso

OUTSIDE_SOURCES = ("apple.rss", "steam.current_players", "youtube.data")
LIMIT_MARK = re.compile(r"<!-- storage-limit source=(\S+) oldest=(\S+) -->")
RANK_LABEL = "rank movement in positions, not download or revenue growth"
YT_LABEL = ("views added / hours between the first and last sample this week, per video, this panel only; "
            "not platform supply")
YT_BARS = 15
PAGES_KEEP_DAYS = 30  # equals youtube.data's 30-day limit; applies to every file in pages/ (J004-T12)


def manual_sources(registry: dict) -> list[str]:
    return [sid for sid, row in registry.items() if row["ruling"] == "manual"]


def _perm(registry: dict, sids) -> str:
    return "; ".join(f"{s}: {registry[s]['ruling']} (checked {registry[s]['checked_on']})" for s in sids if s in registry)


def _t(text: str) -> str:
    return f"{parse_utc(text):%Y-%m-%d %H:%M}"


def _outside_week(text: str) -> str:
    return f"latest snapshot (outside the week window, {_t(text)} UTC)"


def _in_week(text: str, end: datetime) -> bool:
    return end - tm.WEEK <= parse_utc(text) < end


def apple_section(recs: list[dict], end: datetime) -> dict:
    snaps: dict[tuple[str, str], dict[str, dict[str, dict]]] = {}
    for r in recs:
        key = (r["labels"].get("country", "?"), r["labels"].get("feed", "?"))
        snaps.setdefault(key, {}).setdefault(r["observed_at_utc"], {})[r["entity_id"]] = r
    body = []
    for (country, feed), by_time in sorted(snaps.items()):
        cur_t = max((t for t in by_time if _in_week(t, end)), default=None)
        outside = cur_t is None
        if outside:  # no snapshot this week: show the latest one, no movement
            cur_t, prev = max(by_time), {}
            where = f"{country.upper()} {feed} ({_outside_week(cur_t)})"
        else:
            prev_t = max((t for t in by_time if parse_utc(t) < end - tm.WEEK), default=None)
            prev = by_time.get(prev_t, {})
            where = f"{country.upper()} {feed} ({_t(cur_t)}; previous {_t(prev_t) if prev_t else 'none'})"
        for app_id, r in sorted(by_time[cur_t].items(), key=lambda kv: kv[1]["value"]):
            before = prev.get(app_id)
            move = "n/a" if outside else "new" if before is None else f"{before['value'] - r['value']:+d}"
            body.append([where, str(r["value"]), f"{r['labels'].get('name') or '?'} ({app_id})",
                         str(before["value"]) if before else "n/a", move])
        for app_id, r in sorted(prev.items(), key=lambda kv: kv[1]["value"]):
            if app_id not in by_time[cur_t]:
                body.append([where, "out", f"{r['labels'].get('name') or '?'} ({app_id})", str(r["value"]), "left"])
    return {"title": "Apple App Store ranks per country [OFF]", "sources": ["apple.rss"],
            "note": f"Positions in Apple's RSS feed, newest sample this week vs the newest sample before it. "
                    f"Movement = {RANK_LABEL}. The feed has no game filter: items are apps, not games.",
            "head": ["Country feed (sample UTC; previous)", "Rank", "App (Apple id)", "Previous rank",
                     "Movement (positions)"], "body": body, "charts": []}


def steam_section(recs: list[dict], apps: list[dict], end: datetime, max_gap: timedelta) -> dict:
    body, charts = [], []
    for app in apps:
        aid = str(app["app_id"])
        pts = [(parse_utc(r["observed_at_utc"]), float(r["value"])) for r in recs if r["entity_id"] == aid]
        week = [v for t, v in pts if end - tm.WEEK <= t < end]
        prev = [v for t, v in pts if end - 2 * tm.WEEK <= t < end - tm.WEEK]
        if not pts:
            continue
        lt, lv = max(pts)
        when = f"{lt:%Y-%m-%d %H:%M}" if end - tm.WEEK <= lt < end else _outside_week(utc_iso(lt))
        body.append([f"{app.get('label') or '?'} ({aid})", f"{lv:,.0f} ({when})",
                     str(len(week)), f"{sum(week) / len(week):,.0f}" if week else "n/a",
                     f"{max(week):,.0f}" if week else "n/a", f"{sum(prev) / len(prev):,.0f}" if prev else "n/a"])
        start = end - tm.WEEK * tp.CHART_WEEKS
        chart = [(t, v) for t, v in pts if start <= t < end]
        if chart:
            svg, hover = tp._svg(chart, start, end, max_gap, [])
            charts.append((f"{app.get('label') or '?'}", f"Steam app {aid} · current players [OFF]", svg, hover))
    return {"title": "Steam current players, watched apps [OFF]", "sources": ["steam.current_players"],
            "note": "GetNumberOfCurrentPlayers samples. Means are plain sample means [DER], not time-weighted; "
                    "a gap is not filled. Steam players are never added to Roblox or other counts.",
            "head": ["App (Steam app id)", "Latest current players (UTC)", "Samples this week",
                     "Mean of samples this week [DER]", "Max sample this week", "Mean of samples previous week [DER]"],
            "body": body, "charts": charts}


def youtube_section(recs: list[dict], end: datetime) -> tuple[dict, str | None]:
    by_vid: dict[str, list[dict]] = {}
    used = []
    for r in recs:
        if r["metric"] == "views":
            by_vid.setdefault(r["entity_id"], []).append(r)
    rows = []
    for vid, rs in by_vid.items():
        rs.sort(key=lambda r: r["observed_at_utc"])
        week = [r for r in rs if _in_week(r["observed_at_utc"], end)]
        rs = week or rs[-1:]  # no sample this week: the latest one only, no velocity
        used += [r["observed_at_utc"] for r in rs]
        first, last = rs[0], rs[-1]
        hours = (parse_utc(last["observed_at_utc"]) - parse_utc(first["observed_at_utc"])).total_seconds() / 3600
        vel = (last["value"] - first["value"]) / hours if len(rs) > 1 and hours > 0 else None
        lab = last["labels"]
        when = _t(last["observed_at_utc"]) if week else _outside_week(last["observed_at_utc"])
        rows.append((vel, [f"{lab.get('title') or '?'} ({vid})", lab.get("channel_id") or "?",
                           (lab.get("published_at") or "?")[:10], lab.get("panel") or "?",
                           f"{last['value']:,.0f} ({when})",
                           f"{last['value'] - first['value']:+,.0f}" if len(rs) > 1 else "n/a",
                           f"{hours:.1f}" if len(rs) > 1 else "n/a",
                           f"{vel:,.1f}" if vel is not None else "needs 2 samples"], vid))
    rows.sort(key=lambda x: (x[0] is None, -(x[0] or 0)))
    bars = [(vel, vid, cells[0]) for vel, cells, vid in rows if vel is not None][:YT_BARS]
    charts = [("Views per hour this week", f"top {len(bars)} videos of this panel [DER]", _bars(bars), None)] if bars else []
    sec = {"title": "YouTube panel view velocity [OFF] [DER]", "sources": ["youtube.data"],
           "note": f"Velocity = {YT_LABEL}. YouTube API data: deleted 30 days after fetch, this page with it.",
           "head": ["Video (id)", "Channel id", "Published", "Panel", "Views at last sample (UTC)",
                    "Views added this week", "Hours between samples", "Views per hour [DER]"],
           "body": [cells for _, cells, _ in rows], "charts": charts}
    return sec, min(used) if used else None


def manual_section(recs: list[dict], notes: list[dict], end: datetime) -> dict:
    body = []
    entries = recs + notes
    shown = [r for r in entries if _in_week(r["observed_at_utc"], end)]
    if not shown and entries:  # nothing read this week: the latest read day, labelled
        day = max(r["observed_at_utc"] for r in entries)[:10]
        shown = [r for r in entries if r["observed_at_utc"][:10] == day]
    for r in sorted(shown, key=lambda r: (r["source"], r["observed_at_utc"])):
        lab = r.get("labels", {})
        value = f"{r['value']:,} {r['unit']}" if "value" in r else "(no number shown)"
        read = r["observed_at_utc"][:10] if _in_week(r["observed_at_utc"], end) else _outside_week(r["observed_at_utc"])
        body.append([r["source"], read, lab.get("region", ""),
                     f"{lab.get('entity_name') or r['entity_id']} ({r['entity_type']} {r['entity_id']})",
                     r["metric"], value, r["provenance"], lab.get("window", ""), lab.get("page", ""),
                     lab.get("note", "")])
    return {"title": "Manual entries this week [MAN]", "sources": None,
            "note": "Read by hand from public pages (fact-check-outside.md §4); figures as shown on the page. "
                    "Kind: manual_entry, or the kind of figure the reader recorded (third_party_estimate = 3P-E).",
            "head": ["Source", "Read date", "Region", "Item", "Metric", "Value", "Kind", "Window", "Page", "Note"],
            "body": body, "charts": []}


def _bars(bars: list[tuple[float, str, str]]) -> str:
    w, row_h, left, right = 640, 22, 110, 70
    h = row_h * len(bars) + 8
    vmax = max(v for v, _, _ in bars) or 1
    parts = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Views per hour by video">']
    for i, (v, vid, name) in enumerate(bars):
        y = 4 + i * row_h
        bw = max(0.0, (w - left - right) * v / vmax)
        parts.append(f'<g><title>{html.escape(name)}: {v:,.1f} views per hour</title>'
                     f'<text x="{left - 6}" y="{y + 14}" text-anchor="end">{html.escape(vid)}</text>'
                     f'<rect x="{left}" y="{y + 3}" width="{bw:.1f}" height="{row_h - 8}" rx="4" fill="var(--series)"/>'
                     f'<text x="{left + bw + 6:.1f}" y="{y + 14}">{v:,.1f}</text></g>')
    parts.append("</svg>")
    return "".join(parts)


def build(records: list[dict], notes: list[dict], outside: dict, as_of: datetime, registry: dict,
          th: dict) -> tuple[list[dict], str | None]:
    """-> (sections, YouTube marker or None). records: every stored record of OUTSIDE_SOURCES and manual rows."""
    end = tm.week_end(as_of)
    by_src: dict[str, list[dict]] = {}
    for r in records:
        if parse_utc(r["observed_at_utc"]) <= as_of:
            by_src.setdefault(r["source"], []).append(r)
    notes = [n for n in notes if parse_utc(n["observed_at_utc"]) <= as_of]
    yt, oldest = youtube_section(by_src.get("youtube.data", []), end)
    manual = manual_sources(registry)
    secs = [apple_section(by_src.get("apple.rss", []), end),
            steam_section(by_src.get("steam.current_players", []), outside.get("steam", {}).get("apps", []), end,
                          timedelta(minutes=th["max_gap_minutes"])),
            yt, manual_section([r for s in manual for r in by_src.get(s, [])], notes, end)]
    secs[3]["sources"] = manual
    for s in secs:
        s["permission"] = _perm(registry, s["sources"]) or "no registry rows"
    marker = f"<!-- storage-limit source=youtube.data oldest={oldest} -->" if oldest else None
    return secs, marker


def render_markdown(secs: list[dict], marker: str | None) -> str:
    lines = [marker, ""] if marker else []
    lines += ["## Outside trends (one table per platform; never add numbers across platforms)", ""]
    for s in secs:
        lines += [f"### {s['title']}", "", f"Permission: {s['permission']}. {s['note']}", ""]
        if not s["body"]:
            lines += ["No data this week.", ""]
            continue
        lines += ["| " + " | ".join(s["head"]) + " |", "| " + " | ".join("---" for _ in s["head"]) + " |"]
        lines += ["| " + " | ".join(str(c).replace("|", "/") for c in row) + " |" for row in s["body"]] + [""]
    return "\n".join(lines)


def render_html(secs: list[dict], marker: str | None) -> str:
    e = html.escape
    out = [marker or "", "<h2>Outside trends</h2><p class=\"note\">One table per platform; numbers are never "
           "added across platforms.</p>"]
    for s in secs:
        out.append(f"<h3>{e(s['title'])}</h3><p class=\"note\">Permission: {e(s['permission'])}. {e(s['note'])}</p>")
        if not s["body"]:
            out.append("<p>No data this week.</p>")
            continue
        if s["charts"]:
            out.append('<div class="grid">')
            for cap, sub, svg, hover in s["charts"]:
                data = f" data-points='{e(json.dumps(hover))}'" if hover is not None else ""
                out.append(f"<figure{data}><figcaption>{e(cap)} <span class=\"sub\">{e(sub)}</span></figcaption>"
                           f"{svg}<div class=\"tip\"></div></figure>")
            out.append("</div>")
        out.append('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th>{e(c)}</th>" for c in s["head"])
                   + "</tr></thead><tbody>")
        out += ["<tr>" + "".join(f"<td>{e(str(c))}</td>" for c in row) + "</tr>" for row in s["body"]]
        out.append("</tbody></table></div>")
    return "".join(out)


def _marker_expired(text: str, registry: dict, now: datetime) -> bool:
    for sid, oldest in LIMIT_MARK.findall(text):
        days = registry.get(sid, {}).get("storage_limit_days")
        if days is not None and parse_utc(oldest) < now - timedelta(days=int(days)):
            return True
    return False


def prune_pages(registry: dict, now: datetime, base: Path) -> tuple[list[Path], list[str]]:
    """Delete (1) every file under base/pages/ whose last change is older than PAGES_KEEP_DAYS, whatever it
    holds, and (2) every .md or .html under base whose storage-limit marker is older than that source's limit.
    A file that cannot be read or deleted is skipped and reported. Returns (deleted paths, failures)."""
    removed, failed = [], []
    pages, page_cutoff = base / "pages", (now - timedelta(days=PAGES_KEEP_DAYS)).timestamp()
    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        try:
            expired = ((pages in path.parents and path.stat().st_mtime < page_cutoff)
                       or (path.suffix in (".md", ".html")
                           and _marker_expired(path.read_text(encoding="utf-8", errors="replace"), registry, now)))
            if expired:
                path.unlink()
                removed.append(path)
        except OSError as err:
            failed.append(f"{path}: {err}")
    return removed, failed
