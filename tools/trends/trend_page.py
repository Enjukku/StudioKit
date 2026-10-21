#!/usr/bin/env python3
"""Weekly trend page: computes the measured columns for every watched Roblox universe and writes
trend-week-<YYYY-MM-DD>.md and .html (self-contained: inline CSS, inline SVG, inline script, no network).

The page holds measured data only. Columns that need a person or another source (loop, earning rank,
independent source, update notes) are listed as "not collected by tools". No revenue number is produced.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import html
import json
from datetime import datetime, timedelta
from pathlib import Path

import trend_metrics as tm
from roblox_collector import in_event
from trend_store import parse_utc, series, utc_iso

ROBLOX_SOURCES = ("roblox.games", "roblox.votes")
CHART_WEEKS = 3
NOT_COLLECTED = ("repeated-action loop", "confirmed launch", "recent event and update", "earning rank",
                 "revenue status", "independent source")


def _fmt(v, spec: str = ",.0f", none: str = "n/a") -> str:
    return none if v is None else format(v, spec)


def _g7_shown(b: dict, history_days: int, th: dict) -> dict:
    """g7 as the page may show it: young games and empty weeks get a status; g7 from a week under the
    coverage gate is marked "low coverage" (rows sort by g7 only when status is "ok")."""
    if history_days is None:
        return {"value": None, "status": "no data"}
    if history_days < th["emerging_lead_days"]:
        return {"value": None, "status": f"emerging lead ({history_days} days)"}
    if b["current"]["mean_ccu"] is None:
        return {"value": None, "status": "no recent data"}
    g = b["g7"]
    if g["value"] is not None and not (tm.passes_gate(b["current"], th) and tm.passes_gate(b["previous"], th)):
        return {**g, "status": "low coverage"}
    return g


def game_rows(records: list[dict], watchlist: list[dict], as_of: datetime, th: dict) -> list[dict]:
    """One row per watched game from records at or before as_of. Event windows come from the watchlist now,
    not from the stored event_flag. Name: the API name; the watchlist label is only a note."""
    gap = timedelta(minutes=th["max_gap_minutes"])
    end = tm.week_end(as_of)
    by_entity: dict[str, list[dict]] = {}
    for r in records:
        if parse_utc(r["observed_at_utc"]) <= as_of:
            by_entity.setdefault(r["entity_id"], []).append(r)
    rows = []
    for game in watchlist:
        uid = str(game["universe_id"])
        recs = by_entity.get(uid, [])
        ccu = series(recs, "playing")
        ccu_off = [(t, v) for t, v in ccu if not in_event(game, t)]
        labels: dict = {}
        for r in recs:
            labels.update(r.get("labels", {}))
        api_names = [r["labels"]["name"] for r in recs if r["source"] == "roblox.games" and r["labels"].get("name")]
        cur_start = end - tm.WEEK
        up, down = series(recs, "upvotes"), series(recs, "downvotes")
        up_add, down_add = tm.counter_added(up, cur_start, end), tm.counter_added(down, cur_start, end)
        history_days = None if not ccu else (end - ccu[0][0]) // tm.DAY if ccu[0][0] < end else 0
        b = tm.breakout(ccu, as_of, th)
        if history_days is not None and history_days < th["emerging_lead_days"]:
            b = {**b, "status": f"emerging lead ({history_days} days)",
                 "reason": f"under {th['emerging_lead_days']} complete days of our history; daily numbers only"}
        g = _g7_shown(b, history_days, th)
        cur_mean, prev_mean = b["current"]["mean_ccu"], b["previous"]["mean_ccu"]
        rows.append({
            "universe_id": uid, "label": api_names[-1] if api_names else "API name not collected",
            "watchlist_label": game.get("label"),
            "root_place_id": game.get("root_place_id") or labels.get("root_place_id"),
            "created": labels.get("created"),
            "first_observed": utc_iso(ccu[0][0]) if ccu else None,
            "current": ccu[-1] if ccu else None,
            "mean_24h": tm.integrate(ccu, end - tm.DAY, end, gap),
            "week": b["current"], "prev_week": b["previous"], "g7": g,
            "added_ccu": cur_mean - prev_mean if g["value"] is not None else None,
            "acceleration_pp": tm.acceleration_pp(ccu, as_of, th) if g["status"] == "ok" else None,
            "trough_offevent": tm.daily_trough(ccu, ccu_off, cur_start, end, th),
            "visits_added": tm.counter_added(series(recs, "visits"), cur_start, end),
            "votes_added": None if up_add is None or down_add is None else up_add + down_add,
            "approval": tm.approval(up_add, down_add),
            "momentum": tm.momentum(ccu, as_of, th),
            "breakout": b, "fade": tm.fade(ccu, ccu_off, as_of, th),
            "playtime": tm.playtime_estimate(ccu, series(recs, "visits"), cur_start, end, th),
            "chart": [(t, v) for t, v in ccu if end - tm.WEEK * CHART_WEEKS <= t < end],
        })
    rows.sort(key=lambda r: (r["g7"]["status"] != "ok", -(r["g7"]["value"] or 0)))
    return rows


def _header(as_of: datetime, rows: list[dict], registry: dict, sources) -> list[tuple[str, str]]:
    end = tm.week_end(as_of)
    covs = sorted(r["week"]["coverage"] for r in rows)
    cov = (f"{end - tm.WEEK:%Y-%m-%d} to {end - tm.DAY:%Y-%m-%d} UTC; current-week coverage "
           f"min {covs[0]:.0%}, max {covs[-1]:.0%} over {len(rows)} games") if rows else "no watched games"
    perms = "; ".join(f"{sid}: {registry[sid]['ruling']} (checked {registry[sid]['checked_on']})"
                      for sid in sources if sid in registry)
    return [("WEEK ENDING", f"{end - tm.DAY:%Y-%m-%d} (complete UTC days)"), ("AS OF", utc_iso(as_of)),
            ("DATA COVERAGE", cov), ("PERMISSION STATUS", perms or "no registry rows")]


def _g7_text(r: dict) -> str:
    g = r["g7"]
    if g["value"] is None:
        return g["status"]
    return f"{g['value']:+.1%} / {r['added_ccu']:+,.0f}" + ("" if g["status"] == "ok" else f" ({g['status']})")


def _current_text(cur, as_of: datetime) -> str:
    if not cur:
        return "n/a"
    end = tm.week_end(as_of)
    where = "" if end - tm.WEEK <= cur[0] < end else "; latest snapshot, outside the week window"
    return f"{cur[1]:,.0f} ({utc_iso(cur[0])}{where})"


def _table(rows: list[dict], as_of: datetime) -> tuple[list[str], list[list[str]]]:
    head = ["Game: API name (universe / root place)", "First observed", "Current CCU (UTC time)",
            "24h mean CCU (24h coverage)", "7d mean CCU: current / previous", "g7 % / added CCU", "Acceleration pp",
            "Off-event trough (lowest daily mean)", "Visits added (7d)",
            "Votes added (7d) / approval of votes added (7d)", "Coverage current / previous (longest gap)",
            "Momentum 24h/7d (24h coverage)", "Breakout", "Fade"]
    body = []
    for r in rows:
        m = r["momentum"]
        wl = r["watchlist_label"]
        body.append([
            f"{r['label']} ({r['universe_id']} / {r['root_place_id'] or 'n/a'})"
            + (f"; watchlist label: {wl}" if wl and wl != r["label"] else ""),
            (r["first_observed"] or "n/a") + (f"; created {r['created'][:10]}" if r["created"] else ""),
            _current_text(r["current"], as_of),
            f"{_fmt(r['mean_24h']['mean_ccu'])} ({r['mean_24h']['coverage']:.0%})",
            f"{_fmt(r['week']['mean_ccu'])} / {_fmt(r['prev_week']['mean_ccu'])}",
            _g7_text(r),
            _fmt(r["acceleration_pp"], "+.1f"),
            _fmt(r["trough_offevent"]),
            _fmt(r["visits_added"]),
            f"{_fmt(r['votes_added'])} / {_fmt(r['approval'], '.1%')}",
            f"{r['week']['coverage']:.0%} / {r['prev_week']['coverage']:.0%} "
            f"({r['week']['max_gap_minutes']:.0f} min)",
            (f"{m['value']:.2f}" if m["value"] is not None else m["status"])
            + f" ({m['coverage_24h']:.0%}; {tm.MOMENTUM_LABEL})",
            r["breakout"]["status"], r["fade"]["status"],
        ])
    return head, body


def _flag_lines(rows: list[dict]) -> list[str]:
    out = []
    for r in rows:
        for kind in ("breakout", "fade"):
            st = r[kind]["status"]
            if st in ("breakout", "fade") or st.startswith(("suppressed", "emerging lead")) or st == tm.NO_BASELINE:
                out.append(f"{r['label']} ({r['universe_id']}): {kind} = {st}. {r[kind].get('reason', '')}".strip())
    return out


def _playtime_lines(rows: list[dict]) -> list[str]:
    out = []
    for r in rows:
        p = r["playtime"]
        val = f"{p['minutes_per_entry']:.1f} min per entry" if p["minutes_per_entry"] is not None else p["status"]
        out.append(f"{r['label']} ({r['universe_id']}): {val} ({p['label']})")
    return out


def _threshold_lines(th: dict) -> list[str]:
    return [f"{k} = {v} (PROPOSAL, see tools/trends/config.json)" for k, v in th.items()]


def render_markdown(rows, as_of, registry, th, extra: str = "", sources=ROBLOX_SOURCES) -> str:
    lines = [f"# Trend week {tm.week_end(as_of) - tm.DAY:%Y-%m-%d}", ""]
    lines += [f"- **{k}:** {v}" for k, v in _header(as_of, rows, registry, sources)]
    lines += ["", "Roblox values are public counters (provenance: official, sampled by the studio collector) or derived "
              "from them; other sections carry their own labels. Gaps are not filled. No revenue is computed.", ""]
    if not rows or not any(r["current"] for r in rows):
        lines += ["## No data", "", "No stored observations for the watched games in this window. "
                  "Nothing can be measured this week.", ""]
    lines += ["## Flags", ""] + ([f"- {x}" for x in _flag_lines(rows)] or ["- none"]) + [""]
    head, body = _table(rows, as_of)
    lines += ["## Rising games (measured columns)", "", "| " + " | ".join(head) + " |",
              "| " + " | ".join("---" for _ in head) + " |"]
    lines += ["| " + " | ".join(c.replace("|", "/") for c in row) + " |" for row in body]
    lines += ["", "Not collected by tools (scout fills from other evidence): " + ", ".join(NOT_COLLECTED) + ".", ""]
    lines += ["## Playtime estimates", ""] + ([f"- {x}" for x in _playtime_lines(rows)] or ["- none"]) + [""]
    lines += [extra] if extra else []
    lines += ["## Thresholds used", ""] + [f"- {x}" for x in _threshold_lines(th)] + [""]
    return "\n".join(lines)


# ----------------------------------------------------------------------------- HTML

CSS = """
:root{color-scheme:light;--surface:#fcfcfb;--panel:#ffffff;--ink:#0b0b0b;--ink2:#52514e;--muted:#8a8984;
--grid:#e6e5e1;--series:#2a78d6;--mean:#52514e;--good:#008300;--warn:#c98500;--bad:#e34948;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--surface:#1a1a19;
--panel:#232322;--ink:#f0efec;--ink2:#c3c2b7;--muted:#8f8e88;--grid:#3a3936;--series:#3987e5;--mean:#c3c2b7;}}
:root[data-theme="dark"]{color-scheme:dark;--surface:#1a1a19;--panel:#232322;--ink:#f0efec;--ink2:#c3c2b7;
--muted:#8f8e88;--grid:#3a3936;--series:#3987e5;--mean:#c3c2b7;}
*{box-sizing:border-box}body{margin:0;background:var(--surface);color:var(--ink);
font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}main{max-width:1100px;margin:0 auto;padding:24px 16px}
h1{font-size:24px;margin:0 0 12px}h2{font-size:18px;margin:28px 0 8px}dl{display:grid;grid-template-columns:max-content 1fr;
gap:4px 16px;margin:0}dt{font-weight:600;color:var(--ink2)}dd{margin:0}p.note{color:var(--ink2)}
.tablewrap{overflow-x:auto}table{border-collapse:collapse;font-size:13px;min-width:900px}
th,td{border-bottom:1px solid var(--grid);padding:6px 8px;text-align:left;vertical-align:top}
th{color:var(--ink2);font-weight:600}td.num{text-align:right;font-variant-numeric:tabular-nums}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}
figure{margin:0;background:var(--panel);border:1px solid var(--grid);border-radius:8px;padding:12px;position:relative}
figcaption{font-weight:600;margin-bottom:4px}figure .sub{color:var(--ink2);font-size:12px;font-weight:400}
svg{width:100%;height:auto;display:block}svg text{fill:var(--muted);font-size:11px}
.tip{position:absolute;pointer-events:none;background:var(--panel);border:1px solid var(--grid);border-radius:6px;
padding:4px 8px;font-size:12px;display:none;white-space:nowrap}
.flag{font-weight:600}.flag.breakout{color:var(--good)}.flag.fade{color:var(--bad)}.flag.held{color:var(--warn)}
"""

SCRIPT = """
document.querySelectorAll('figure[data-points]').forEach(function(fig){
  var pts=JSON.parse(fig.dataset.points), svg=fig.querySelector('svg'), tip=fig.querySelector('.tip'),
      cross=svg.querySelector('.cross');
  if(!pts.length)return;
  svg.addEventListener('mousemove',function(e){
    var r=svg.getBoundingClientRect(), vb=svg.viewBox.baseVal, x=(e.clientX-r.left)*vb.width/r.width, best=pts[0];
    pts.forEach(function(p){if(Math.abs(p[0]-x)<Math.abs(best[0]-x))best=p;});
    cross.setAttribute('x1',best[0]);cross.setAttribute('x2',best[0]);cross.style.display='';
    tip.textContent=best[2]+'  '+best[3]+' players';tip.style.display='block';
    var px=r.left-fig.getBoundingClientRect().left+best[0]*r.width/vb.width+12;
    tip.style.left=Math.max(0,Math.min(px,fig.clientWidth-tip.offsetWidth-4))+'px';tip.style.top='36px';
  });
  svg.addEventListener('mouseleave',function(){tip.style.display='none';cross.style.display='none';});
});
"""


def _svg(points, start: datetime, end: datetime, max_gap: timedelta, week_means) -> tuple[str, list]:
    w, h, left, right, top, bottom = 640, 200, 52, 12, 10, 26
    vmax = max([v for _, v in points] + [m for _, _, m in week_means if m is not None] + [1]) * 1.1
    span = (end - start).total_seconds()

    def x(t):
        return left + (w - left - right) * (t - start).total_seconds() / span

    def y(v):
        return top + (h - top - bottom) * (1 - v / vmax)

    parts = [f'<svg viewBox="0 0 {w} {h}" role="img">']
    for frac in (0, 0.5, 1):
        gy = y(vmax / 1.1 * frac)
        parts.append(f'<line x1="{left}" x2="{w - right}" y1="{gy:.1f}" y2="{gy:.1f}" stroke="var(--grid)"/>'
                     f'<text x="{left - 6}" y="{gy + 4:.1f}" text-anchor="end">{vmax / 1.1 * frac:,.0f}</text>')
    t = start
    while t <= end:
        parts.append(f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top}" y2="{h - bottom}" stroke="var(--grid)"/>'
                     f'<text x="{x(t):.1f}" y="{h - 8}" text-anchor="middle">{t:%m-%d}</text>')
        t += tm.WEEK
    for ws, we, m in week_means:
        if m is not None:
            parts.append(f'<line x1="{x(ws):.1f}" x2="{x(we):.1f}" y1="{y(m):.1f}" y2="{y(m):.1f}" '
                         f'stroke="var(--mean)" stroke-width="1.5" stroke-dasharray="4 3"/>')
    segs, cur = [], []
    for i, (t, v) in enumerate(points):
        if cur and t - points[i - 1][0] > max_gap:
            segs.append(cur)
            cur = []
        cur.append((t, v))
    if cur:
        segs.append(cur)
    for seg in segs:
        if len(seg) == 1:
            parts.append(f'<circle cx="{x(seg[0][0]):.1f}" cy="{y(seg[0][1]):.1f}" r="2.5" fill="var(--series)"/>')
        else:
            d = " ".join(f"{'M' if j == 0 else 'L'}{x(t):.1f},{y(v):.1f}" for j, (t, v) in enumerate(seg))
            parts.append(f'<path d="{d}" fill="none" stroke="var(--series)" stroke-width="2" '
                         f'stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<line class="cross" y1="{top}" y2="{h - bottom}" stroke="var(--ink2)" style="display:none"/></svg>')
    hover = [[round(x(t), 1), 0, f"{t:%Y-%m-%d %H:%M} UTC", f"{v:,.0f}"] for t, v in points]
    return "".join(parts), hover


def render_html(rows, as_of, registry, th, extra: str = "", sources=ROBLOX_SOURCES) -> str:
    e = html.escape
    end = tm.week_end(as_of)
    gap = timedelta(minutes=th["max_gap_minutes"])
    title = f"Trend week {end - tm.DAY:%Y-%m-%d}"
    out = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>'
           f"<style>{CSS}</style></head><body><main><h1>{e(title)}</h1><dl>"]
    out += [f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in _header(as_of, rows, registry, sources)]
    out.append('</dl><p class="note">Roblox values are public counters (provenance: official, sampled by the '
               "studio collector) or derived from them; other sections carry their own labels. Gaps are not filled and show as breaks in the lines. "
               "No revenue is computed.</p>")
    if not rows or not any(r["current"] for r in rows):
        out.append("<h2>No data</h2><p>No stored observations for the watched games in this window. "
                   "Nothing can be measured this week.</p>")
    out.append("<h2>Flags</h2><ul>")
    flags = _flag_lines(rows)
    for line in flags:
        cls = "breakout" if "breakout = breakout" in line else "fade" if "fade = fade" in line else "held"
        word = {"breakout": "Breakout", "fade": "Fade", "held": "Held"}[cls]
        out.append(f'<li><span class="flag {cls}">{word}:</span> {e(line)}</li>')
    out.append("" if flags else "<li>none</li>")
    out.append("</ul>")
    charted = [r for r in rows if r["chart"]]
    if charted:
        out.append(f"<h2>Players online, last {CHART_WEEKS} complete weeks (UTC)</h2>"
                   '<p class="note">Solid line: observed samples. Dashed: time-weighted weekly mean CCU. '
                   f"Breaks: gaps over {th['max_gap_minutes']} minutes, not bridged.</p><div class=\"grid\">")
        cstart = end - tm.WEEK * CHART_WEEKS
        for r in charted:
            means = []
            for i in range(CHART_WEEKS):
                ws, we = cstart + tm.WEEK * i, cstart + tm.WEEK * (i + 1)
                means.append((ws, we, tm.integrate(r["chart"], ws, we, gap)["mean_ccu"]))
            svg, hover = _svg(r["chart"], cstart, end, gap, means)
            sub = f"g7 {_g7_text(r)}"
            out.append(f"<figure data-points='{e(json.dumps(hover))}'><figcaption>{e(r['label'])} "
                       f'<span class="sub">universe {e(r["universe_id"])} · {e(sub)} · coverage '
                       f'{r["week"]["coverage"]:.0%}</span></figcaption>{svg}<div class="tip"></div></figure>')
        out.append("</div>")
    head, body = _table(rows, as_of)
    out.append('<h2>Rising games (measured columns)</h2><div class="tablewrap"><table><thead><tr>')
    out += [f"<th>{e(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>" + "".join(f"<td>{e(c)}</td>" for c in row) + "</tr>")
    out.append(f"</tbody></table></div><p class=\"note\">Not collected by tools (scout fills from other evidence): "
               f"{e(', '.join(NOT_COLLECTED))}.</p>")
    out.append("<h2>Playtime estimates</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in _playtime_lines(rows))
               + ("" if rows else "<li>none</li>") + "</ul>")
    out.append(extra)
    out.append("<h2>Thresholds used</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in _threshold_lines(th)) + "</ul>")
    out.append(f"<script>{SCRIPT}</script></main></body></html>")
    return "".join(out)


def write_pages(records, watchlist, as_of, registry, th, out_dir: Path,
                outside: tuple[str, str] = ("", ""), sources=ROBLOX_SOURCES) -> tuple[Path, Path]:
    """outside: (markdown, html) of the outside sections (outside_page.py), placed before the thresholds.
    sources: every registry row the page draws on, listed under PERMISSION STATUS."""
    rows = game_rows(records, watchlist, as_of, th)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"trend-week-{tm.week_end(as_of) - tm.DAY:%Y-%m-%d}"
    md, page = out_dir / f"{stem}.md", out_dir / f"{stem}.html"
    md.write_text(render_markdown(rows, as_of, registry, th, outside[0], sources), encoding="utf-8", newline="\n")
    page.write_text(render_html(rows, as_of, registry, th, outside[1], sources), encoding="utf-8", newline="\n")
    return md, page

