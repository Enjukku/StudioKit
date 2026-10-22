#!/usr/bin/env python3
"""Progression chart: turns one or more sim.py reports into ONE self-contained HTML page (inline SVG and CSS,
no script from the network, no external file) that opens offline in a browser.

Kit tool (universal, Studio Kit). Python 3.11+ standard library only.

What the page shows:
  (a) curves the model declares (price per unit, cumulative spend, producer output, XP per level and
      cumulative XP, hits to kill per level against reference enemies); log scale when the plotted values
      span more than 3 orders of magnitude, and the axis then says "log scale";
  (b) the timeline: goals on an active-time axis (and a calendar axis for the reports run with a session
      pattern; reports without one get no calendar row), soft walls, hard walls, power spikes, resets
      (prestige, diamond) and blocked paths marked and labelled, one row per report titled with its policy
      and model revision; walls are drawn on the calendar axis too (reports from sim 1.1+);
  (b2) wait per step (one dot per step with a non-zero wait, per report) and each reference metric over
      active time (a step line per report, gaps where the metric was not measured);
  (a2) on a page with several models, a curve identical in several models is drawn once and its title names
      every model revision that shares it; a curve that differs is drawn once per variant;
  (c) target windows as bands with the verdict as text (pass / fail / not testable);
  (d) the assumptions panel (every EXAMPLE ASSUMPTION and PROPOSAL input, the behaviour lines), the model
      revision and SHA-256, policy, seed, runs, mode and tool versions; tables for every plotted value.

What it never claims: the page repeats the reports' limits - each row is one modelled strategy, not the
player population; a pass is arithmetic against a declared window, not a verdict on fun. It computes nothing
new: every number comes from the reports. All report text is escaped (model strings are data).

Hover: each mark carries an SVG <title> (native tooltip) on a hit area larger than the mark; every value is
also in a table, so nothing depends on hovering. Colours follow the dataviz reference palette; status colours
(walls, verdicts) always come with a text label or icon.

Usage:
  python tools/progression/chart.py REPORT.json [REPORT2.json ...] --out output/progression/run.html [--title T]
"""

from __future__ import annotations

import argparse
import html
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

VERSION = "1.2.0"
LOG_SPAN = 1000  # "more than 3 orders of magnitude" (owner brief J011-T07)
SERIES = 8  # categorical slots in the CSS below
TABLE_MAX = 100  # rows per chart table (display only; every value stays in the report JSON)


def esc(x) -> str:
    return html.escape("" if x is None else str(x), quote=True)


def num(x):
    """Report number (float, int or 'p/q' string) -> float; None stays None."""
    if x is None or isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x)
    return float(Fraction(x))


def fmt_t(s) -> str:
    """Seconds -> short human text."""
    if s is None:
        return "-"
    s = float(s)
    if s < 120:
        return f"{s:.3g} s"
    if s < 7200:
        return f"{s / 60:.3g} min"
    if s < 172800:
        return f"{s / 3600:.3g} h"
    return f"{s / 86400:.3g} d"


def fmt_v(v) -> str:
    if v is None:
        return "-"
    v = float(v)
    a = abs(v)
    if a == 0:
        return "0"
    if a >= 1e15 or a < 1e-3:
        return f"{v:.3g}"
    for div, suf in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= div:
            return f"{v / div:.3g}{suf}"
    return f"{v:.4g}"


def exact_text(x) -> str:
    """Exact value as written in the report, plus a decimal when it is a fraction."""
    if x is None:
        return "-"
    if isinstance(x, str) and "/" in x:
        return f"{x} (= {float(Fraction(x)):.6g})"
    return str(x)


# ---------------------------------------------------------------- scales and ticks

class Scale:
    def __init__(self, lo, hi, a, b, log=False):
        self.log = log
        if log:
            self.lo, self.hi = math.log10(lo), math.log10(hi)
        else:
            self.lo, self.hi = lo, hi
        if self.hi == self.lo:
            self.hi = self.lo + 1
        self.a, self.b = a, b

    def __call__(self, v):
        if self.log:
            v = math.log10(v) if v > 0 else self.lo
        return self.a + (v - self.lo) / (self.hi - self.lo) * (self.b - self.a)


def nice_ticks(lo, hi, n=5):
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    out = [round(math.floor(lo / step) * step, 12)]
    while out[-1] < hi - step * 1e-9:  # the last tick covers hi, so no point falls outside the axis
        out.append(round(out[-1] + step, 12))
    return out


def log_ticks(lo, hi):
    return [10.0 ** e for e in range(math.floor(math.log10(lo)), math.ceil(math.log10(hi)) + 1)]


def use_log(values) -> bool:
    pos = [v for v in values if v is not None and v > 0]
    return bool(pos) and all(v is None or v > 0 for v in values) and max(pos) / min(pos) > LOG_SPAN


# ---------------------------------------------------------------- timeline

def _row_marks(rep, basis):
    """Collect what one report row draws on the given time basis (active or calendar)."""
    key = "active_s" if basis == "active" else "calendar_s"
    goals = [(g, num(g[key])) for g in rep["timeline"] if g["reached"] and num(g[key]) is not None]
    if basis == "active":
        soft = [(w, num(w["start_active_s"]), num(w["end_active_s"])) for w in rep["walls"]["soft"]["walls"]]
        hard = [(w, num(w["start_s"]), num(w["start_s"]) + num(w["duration_s"] or 0)) for w in rep["walls"]["hard"]]
    else:  # reports from sim 1.1+ carry calendar times for both ends of a wall
        soft = [(w, num(w["start_calendar_s"]), num(w["end_calendar_s"])) for w in rep["walls"]["soft"]["walls"]
                if w.get("start_calendar_s") is not None and w.get("end_calendar_s") is not None]
        end_cal = num(rep["stop"]["calendar_s"])
        hard = [(w, num(w["start_calendar_s"]), num(w["end_calendar_s"]) if w.get("end_calendar_s") is not None else end_cal)
                for w in rep["walls"]["hard"] if w.get("start_calendar_s") is not None]
    t_key = "t_active_s" if basis == "active" else "t_calendar_s"
    spikes = [(s, num(s[t_key])) for s in rep["spikes"]["spikes"] if num(s[t_key]) is not None]
    resets = [(p, num(p[t_key])) for p in rep.get("prestige", []) if num(p[t_key]) is not None]
    windows = [g for g in rep["timeline"] if g.get("window") and g["window"]["basis"] == basis]
    end = num(rep["stop"][key])
    return goals, soft, hard, spikes, windows, end, resets


def timeline_svg(reports, basis) -> str:
    if basis == "calendar":  # runs without a session pattern have no calendar time: no empty rows
        reports = [r for r in reports if r["stop"]["calendar_s"] is not None]
    rows = [_row_marks(r, basis) for r in reports]
    if not any(r[5] is not None for r in rows):
        return ""
    vals = []
    for goals, soft, hard, spikes, windows, end, resets in rows:
        vals += [t for _, t in goals] + [t for _, a, b in soft + hard for t in (a, b)] + [t for _, t in spikes]
        vals += [t for _, t in resets]
        vals += [end] if end is not None else []
        for g in windows:
            vals += [num(g["window"].get(k)) for k in ("min_s", "max_s") if g["window"].get(k) is not None]
    pos = [v for v in vals if v and v > 0]
    hi = max(pos) if pos else 1.0
    lo_pos = min(pos) if pos else 1.0
    log = hi / lo_pos > LOG_SPAN
    W, left, right, zero_gap = 640, 16, 16, 28 if log else 0
    if log:
        lo = 10 ** math.floor(math.log10(lo_pos))
        hi_t = 10 ** math.ceil(math.log10(hi))
        sx = Scale(lo, hi_t, left + zero_gap, W - right, log=True)
        ticks = log_ticks(lo, hi_t)
    else:
        unit = next(u for lim, u in ((120, 1), (7200, 60), (172800, 3600), (math.inf, 86400)) if hi < lim)
        ticks = [t * unit for t in nice_ticks(0, hi / unit)]  # round numbers in the unit the labels use
        sx = Scale(0, ticks[-1], left, W - right)

    def X(t):
        return left + zero_gap / 2 if (log and (t is None or t <= 0)) else sx(t)

    parts, y = [], 0
    for rep, (goals, soft, hard, spikes, windows, end, resets) in zip(reports, rows):
        pol = rep["policy"]
        name = pol["name"] + "".join(f" · {k} {pol[k]}" for k in ("target", "target_level", "skill_profile",
                                                                  "session_pattern") if pol.get(k) is not None)
        name += f" · model {rep['model']['revision']}"
        lanes = len(windows)
        top = y + 22
        track = top + 14 * lanes + 22
        h = track - y + 60
        parts.append(f'<text class="row-label" x="{left}" y="{y + 15}">{esc(name)}</text>')
        for i, g in enumerate(windows):
            w = g["window"]
            ly = top + 14 * i + 6
            a = X(num(w.get("min_s")) if w.get("min_s") is not None else 0)
            b = X(num(w["max_s"])) if w.get("max_s") is not None else W - right
            icon = {"pass": "✓", "fail": "✗"}.get(g["verdict"], "–")
            parts.append(f'<g><title>{esc(g["label"])}: window {esc(w.get("min_s", "-"))} to {esc(w.get("max_s", "-"))} s; '
                         f'{esc(g["verdict"])}. {esc(g["evidence"])}</title>'
                         f'<rect class="window w-{esc(g["verdict"].replace(" ", "-"))}" x="{a:.1f}" y="{ly - 4}" '
                         f'width="{max(b - a, 2):.1f}" height="8" rx="2"/>'
                         f'<text class="small" x="{min(b + 4, W - 120):.1f}" y="{ly + 3}">{icon} {esc(g["goal"])} '
                         f'window: {esc(g["verdict"])}</text></g>')
        if end is not None:
            parts.append(f'<line class="track" x1="{X(0):.1f}" x2="{X(end):.1f}" y1="{track}" y2="{track}"/>')
        for w, a, b in soft:
            parts.append(f'<g><title>soft wall: {esc(w["step"])} waited {esc(fmt_t(num(w["wait_s"])))} ({esc(w["rule"])})</title>'
                         f'<rect class="soft" x="{X(a):.1f}" y="{track - 9}" width="{max(X(b) - X(a), 3):.1f}" height="18"/></g>')
        for w, a, b in hard:
            parts.append(f'<g><title>hard wall: {esc(w["id"])} affordable but locked for {esc(fmt_t(b - a))}; '
                         f'missing {esc(json.dumps(w["missing"]))}</title>'
                         f'<rect class="hard" x="{X(a):.1f}" y="{track - 9}" width="{max(X(b) - X(a), 3):.1f}" height="18"/></g>')
        for s, t in spikes:
            x = X(t)
            parts.append(f'<g><title>power spike {esc(s["metric"])}: {esc(s["from"])} → {esc(s["to"])} at {esc(fmt_t(t))} '
                         f'({esc(s["cause"])}; {esc(s["rule"])})</title><circle class="hit" cx="{x:.1f}" cy="{track - 17}" r="10"/>'
                         f'<path class="spike" d="M{x - 5:.1f},{track - 22} L{x + 5:.1f},{track - 22} L{x:.1f},{track - 13} Z"/></g>')
        for n, (p, t) in enumerate(resets, 1):
            x = X(t)
            parts.append(f'<g><title>reset (prestige) {n} at {esc(fmt_t(t))}: award {esc(p["award"])}; removed '
                         f'{esc(json.dumps(p["removed"]))}; kept {esc(", ".join(p["kept"]))}</title>'
                         f'<circle class="hit" cx="{x:.1f}" cy="{track}" r="10"/>'
                         f'<path class="reset" d="M{x:.1f},{track - 7} L{x + 6:.1f},{track} L{x:.1f},{track + 7} '
                         f'L{x - 6:.1f},{track} Z"/></g>')
        if resets:
            parts.append(f'<text class="small" x="{W - right}" y="{track - 12}" text-anchor="end">'
                         f'◆ {len(resets)} reset(s)</text>')
        for k, (g, t) in enumerate(goals):
            x = X(t)
            ly = track + 22 + 11 * (k % 3)
            parts.append(f'<g><title>{esc(g["label"])}: {esc(fmt_t(t))} ({esc(exact_text(g["active_s" if basis == "active" else "calendar_s"]))} s)</title>'
                         f'<circle class="hit" cx="{x:.1f}" cy="{track}" r="12"/><circle class="goal" cx="{x:.1f}" cy="{track}" r="5"/>'
                         f'<text class="small" x="{x:.1f}" y="{ly}" text-anchor="middle">{esc(g["goal"])}</text></g>')
        blocked = [g for g in rep["timeline"] if not g["reached"]]
        if end is not None:
            x = X(end)
            label = f'end: {rep["stop"]["reason"]}'
            anchor = "end" if x > W / 2 else "start"
            parts.append(f'<g><title>{esc(label)}. {esc(rep["stop"]["detail"])}'
                         + (f'; not reached: {esc(", ".join(g["goal"] for g in blocked))}' if blocked else "")
                         + f'</title><line class="endtick" x1="{x:.1f}" x2="{x:.1f}" y1="{track - 12}" y2="{track + 12}"/>'
                         + (f'<text class="blocked" x="{x:.1f}" y="{track + 5}" text-anchor="middle">✕</text>' if blocked else "")
                         + f'<text class="small" x="{x + (-6 if anchor == "end" else 6):.1f}" y="{y + 15}" text-anchor="{anchor}">'
                         f'{esc(label)}</text></g>')
        y += h
    axis_y = y + 6
    tick_parts = [f'<line class="axis" x1="{left}" x2="{W - right}" y1="{axis_y}" y2="{axis_y}"/>']
    for t in ticks:
        x = sx(t)
        tick_parts.append(f'<line class="grid" x1="{x:.1f}" x2="{x:.1f}" y1="4" y2="{axis_y}"/>'
                          f'<text class="tick" x="{x:.1f}" y="{axis_y + 16}" text-anchor="middle">{esc(fmt_t(t))}</text>')
    if log:
        tick_parts.append(f'<text class="tick" x="{left + zero_gap / 2:.1f}" y="{axis_y + 16}" text-anchor="middle">0</text>')
    label = f'{"active" if basis == "active" else "calendar"} time{" (log scale)" if log else ""}'
    tick_parts.append(f'<text class="axis-label" x="{W / 2}" y="{axis_y + 34}" text-anchor="middle">{esc(label)}</text>')
    H = axis_y + 42
    defs = ('<defs><pattern id="hatch" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">'
            '<rect class="hatch-bg" width="6" height="6"/><line class="hatch" x1="0" y1="0" x2="0" y2="6"/></pattern></defs>')
    return (f'<div class="scroll"><svg class="timeline" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(label)} timeline, one row per policy">{defs}{"".join(tick_parts)}{"".join(parts)}</svg></div>')


# ---------------------------------------------------------------- curves

def curve_svg(curve) -> str:
    series = curve.get("series") or [{"name": curve["title"], "points": curve["points"]}]
    pts = [[(num(x), num(y)) for x, y in s["points"]] for s in series]
    xs = [x for p in pts for x, _ in p]
    ys = [y for p in pts for _, y in p]
    if not xs:
        return ""
    ref = curve.get("hline")  # (value, label): a declared threshold drawn as a reference line
    if ref is not None:
        ys = ys + [num(ref[0])]
    W, H, l, r, t, b = 360, 220, 52, 12, 12, 44
    logy = use_log(ys)
    if logy:
        lo, hi = 10 ** math.floor(math.log10(min(ys))), 10 ** math.ceil(math.log10(max(ys)))
        sy, yt = Scale(lo, hi, H - b, t, log=True), log_ticks(lo, hi)
        if len(yt) > 7:
            yt = yt[::math.ceil(len(yt) / 6)]
    else:
        yt = nice_ticks(min(0.0, min(ys)), max(ys) * 1.05 if max(ys) > 0 else 1)
        sy = Scale(yt[0], yt[-1], H - b, t)
    xt = nice_ticks(min(xs), max(xs), 5) if max(xs) > min(xs) else [min(xs)]
    sx = Scale(min(xs), max(xs) if max(xs) > min(xs) else min(xs) + 1, l, W - r)
    out = []
    for v in yt:
        y = sy(v)
        out.append(f'<line class="grid" x1="{l}" x2="{W - r}" y1="{y:.1f}" y2="{y:.1f}"/>'
                   f'<text class="tick" x="{l - 6}" y="{y + 4:.1f}" text-anchor="end">{esc(fmt_v(v))}</text>')
    for v in xt:
        x = sx(v)
        out.append(f'<text class="tick" x="{x:.1f}" y="{H - b + 16}" text-anchor="middle">{esc(fmt_v(v))}</text>')
    out.append(f'<line class="axis" x1="{l}" x2="{W - r}" y1="{H - b}" y2="{H - b}"/>')
    if ref is not None:
        yr = sy(num(ref[0]))
        out.append(f'<line class="refline" x1="{l}" x2="{W - r}" y1="{yr:.1f}" y2="{yr:.1f}"/>'
                   f'<text class="small" x="{W - r}" y="{yr - 4:.1f}" text-anchor="end">{esc(ref[1])}</text>')
    out.append(f'<text class="axis-label" x="{(l + W - r) / 2}" y="{H - 8}" text-anchor="middle">{esc(curve["x"])}</text>')
    out.append(f'<text class="axis-label" x="12" y="{(t + H - b) / 2}" text-anchor="middle" '
               f'transform="rotate(-90 12 {(t + H - b) / 2})">{esc(curve["y"])}{" (log scale)" if logy else ""}</text>')
    for k, (s, p) in enumerate(zip(series, pts)):
        cls = f"s{k % SERIES + 1}"
        if curve.get("marks") != "dots" and p:
            if curve.get("step"):  # the value holds until the next change
                d = f"M{sx(p[0][0]):.1f},{sy(p[0][1]):.1f} " + " ".join(
                    f"H{sx(x):.1f} V{sy(y):.1f}" for x, y in p[1:])
            else:
                d = " ".join(f"{'M' if i == 0 else 'L'}{sx(x):.1f},{sy(y):.1f}" for i, (x, y) in enumerate(p))
            out.append(f'<path class="line {cls}" d="{d}"/>')
        if len(p) <= 40:
            for x, y in p:
                out.append(f'<g><title>{esc(s["name"])}: {esc(curve["x"])} {esc(fmt_v(x))} → {esc(fmt_v(y))}</title>'
                           f'<circle class="hit" cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="9"/>'
                           f'<circle class="dot {cls}" cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="3.5"/></g>')
        elif curve.get("marks") == "dots":  # many points: one path of round dots keeps the page small
            d = "".join(f"M{sx(x):.1f},{sy(y):.1f}h0" for x, y in p)
            out.append(f'<path class="dots {cls}" d="{d}"/>')
    legend = ""
    if len(series) > 1:
        legend = '<div class="legend">' + "".join(
            f'<span><i class="key s{k % SERIES + 1}"></i>{esc(s["name"])}</span>' for k, s in enumerate(series)) + "</div>"
    all_rows = [(s["name"], x, y) for s in series for x, y in s["points"]]
    rows = "".join(f"<tr><td>{esc(n)}</td><td>{esc(exact_text(x))}</td><td>{esc(exact_text(y))}</td></tr>"
                   for n, x, y in all_rows[:TABLE_MAX])
    if len(all_rows) > TABLE_MAX:
        rows += f"<tr><td colspan='3'>first {TABLE_MAX} of {len(all_rows)} rows; every value is in the report JSON</td></tr>"
    return (f'<figure class="card"><figcaption>{esc(curve["title"])}</figcaption>{legend}'
            f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(curve["title"])}">{"".join(out)}</svg>'
            f'<details><summary>Table</summary><div class="scroll"><table><thead><tr><th>series</th><th>{esc(curve["x"])}</th>'
            f'<th>{esc(curve["y"])}</th></tr></thead><tbody>{rows}</tbody></table></div></details></figure>')


# ---------------------------------------------------------------- tables and panels

def _policy_name(rep) -> str:
    p = rep["policy"]
    extra = [f"{k}={p[k]}" for k in ("target", "target_level", "skill_profile", "session_pattern") if p.get(k) is not None]
    return p["name"] + (f" ({', '.join(extra)})" if extra else "")


def meta_table(reports) -> str:
    rows = []
    for i, r in enumerate(reports, 1):
        m = r["model"]
        rows.append(f"<tr><td>{i}</td><td>{esc(_policy_name(r))}</td><td>{esc(m['revision'])}</td>"
                    f"<td><code>{esc((m['sha256'] or 'in-memory model')[:16])}</code></td><td>{esc(r['mode'])}</td>"
                    f"<td>{esc(r['seed'] if r['seed'] is not None else 'none (no random inputs)')}</td><td>{esc(r['runs'])}</td>"
                    f"<td>sim {esc(r['version'])}, curves {esc(r['curves_version'])}</td></tr>")
    return ('<div class="scroll"><table><thead><tr><th>#</th><th>policy</th><th>model revision</th><th>model SHA-256</th>'
            '<th>mode</th><th>seed</th><th>runs</th><th>tool versions</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


def assumptions_panel(reports) -> str:
    seen, blocks = set(), []
    for r in reports:
        key = (r["model"]["sha256"], r["model"]["revision"])
        items = r["assumptions"]["inputs"]
        if key not in seen:
            seen.add(key)
            rows = "".join(f"<tr><td><code>{esc(a['input'])}</code></td><td>{esc(a['src'])}</td>"
                           f"<td>{esc(exact_text(a['value']) if not isinstance(a['value'], list) else ', '.join(map(str, a['value'])))}</td></tr>"
                           for a in items)
            counts = ", ".join(f"{esc(k)}: {esc(v)}" for k, v in r["provenance_counts"].items())
            blocks.append(f"<h3>Model {esc(r['model']['revision'])}</h3><p class='muted'>Inputs by label: {counts}</p>"
                          + (f'<div class="scroll"><table><thead><tr><th>input</th><th>label</th><th>value</th></tr></thead>'
                             f"<tbody>{rows}</tbody></table></div>" if items else
                             "<p>No input is labelled EXAMPLE ASSUMPTION or PROPOSAL.</p>"))
    beh = sorted({b for r in reports for b in r["assumptions"]["behaviour"]})
    sem = []
    for r in reports:
        s = r["semantics"]
        sem.append(f"<li>{esc(_policy_name(r))}: time {esc(json.dumps(s['time']))}; event order "
                   f"{esc(' → '.join(s['event_order']))}; horizon {esc(exact_text(s['horizon_active_s']))} s "
                   f"({esc(s['horizon_source'])}); calendar: {esc(s['calendar'])}; offline: "
                   f"{esc(s['offline'] if isinstance(s['offline'], str) else json.dumps(s['offline']))}</li>")
    return ('<section class="panel assumptions" id="assumptions"><h2>Assumptions</h2>'
            "<p>Every result on this page is conditional on these inputs and behaviour lines. "
            "The tool does not trace which result uses which input.</p>"
            + "".join(blocks)
            + "<h3>Behaviour modelled</h3><ul>" + "".join(f"<li>{esc(b)}</li>" for b in beh) + "</ul>"
            + "<h3>Semantics per run</h3><ul>" + "".join(sem) + "</ul>"
            + "<h3>Never claimed</h3><ul>" + "".join(f"<li>{esc(c)}</li>" for c in reports[0]["never_claims"])
            + "</ul></section>")


def goals_table(reports) -> str:
    ids, labels = [], {}
    for r in reports:
        for g in r["timeline"]:
            if g["goal"] not in labels:
                ids.append(g["goal"])
                labels[g["goal"]] = g["label"]
    head = "".join(f"<th>{i}. active</th><th>{i}. calendar</th><th>{i}. verdict</th>" for i in range(1, len(reports) + 1))
    rows = []
    for gid in ids:
        cells = []
        for r in reports:
            g = next((x for x in r["timeline"] if x["goal"] == gid), None)
            if g is None:
                cells.append("<td>-</td><td>-</td><td>-</td>")
                continue
            if g["reached"]:
                act = f'{esc(fmt_t(num(g["active_s"])))}<br><span class="muted">{esc(exact_text(g["active_s"]))} s</span>'
            else:
                act = f'not reached<br><span class="muted">{esc(g["reason"])}: {esc(g["detail"])}</span>'
            icon = {"pass": "✓ ", "fail": "✗ "}.get(g["verdict"], "– ")
            cells.append(f"<td>{act}</td><td>{esc(fmt_t(num(g['calendar_s'])))}</td>"
                         f'<td><span class="v-{esc(g["verdict"].replace(" ", "-"))}">{icon}{esc(g["verdict"])}</span>'
                         f'<br><span class="muted">{esc(g["evidence"])}</span></td>')
        rows.append(f"<tr><td>{esc(labels[gid])}<br><code>{esc(gid)}</code></td>{''.join(cells)}</tr>")
    return (f'<div class="scroll"><table><thead><tr><th>goal</th>{head}</tr></thead><tbody>{"".join(rows)}</tbody>'
            "</table></div>")


def findings_tables(reports) -> str:
    out = []
    for i, r in enumerate(reports, 1):
        sw, hw, sp = r["walls"]["soft"], r["walls"]["hard"], r["spikes"]
        rows = []
        if sw["evaluated"]:
            rows += [f"<tr><td>soft wall</td><td>{esc(w['step'])}</td><td>{esc(fmt_t(num(w['end_active_s'])))}</td>"
                     f"<td>waited {esc(fmt_t(num(w['wait_s'])))} ({esc(w['rule'])})</td></tr>" for w in sw["walls"]]
        else:
            rows.append(f"<tr><td>soft walls</td><td colspan='3'>not evaluated: {esc(sw['reason'])}. Slowest steps: "
                        + esc("; ".join(f"{s['step']} {fmt_t(num(s['wait_s']))}" for s in sw["slowest_steps"])) + "</td></tr>")
        rows += [f"<tr><td>hard wall</td><td>{esc(w['id'])}</td><td>{esc(fmt_t(num(w['start_s'])))}</td>"
                 f"<td>affordable but locked for {esc(fmt_t(num(w['duration_s'])))}; missing "
                 f"<code>{esc(json.dumps(w['missing']))}</code>{' (still open at the end)' if w.get('open_at_end') else ''}</td></tr>"
                 for w in hw]
        if sp["evaluated"]:
            rows += [f"<tr><td>power spike</td><td>{esc(s['metric'])}</td><td>{esc(fmt_t(num(s['t_active_s'])))}</td>"
                     f"<td>{esc(s['from'])} → {esc(s['to'])} after {esc(s['cause'])} ({esc(s['rule'])})</td></tr>"
                     for s in sp["spikes"]]
        else:
            rows.append(f"<tr><td>power spikes</td><td colspan='3'>not evaluated: {esc(sp.get('reason', 'no spike metric declared'))}</td></tr>")
        rows += [f"<tr><td>blocked</td><td>{esc(b['goal'])}</td><td>-</td><td>{esc(b['reason'])}: {esc(b['detail'])}</td></tr>"
                 for b in r["blocked"]]
        for p in r["prestige"]:
            rows.append(f"<tr><td>prestige</td><td>award {esc(p['award'])}</td><td>{esc(fmt_t(num(p['t_active_s'])))}</td>"
                        f"<td>removed {esc(json.dumps(p['removed']))}; kept {esc(', '.join(p['kept']))}</td></tr>")
        led = "; ".join(f"{c}: residual {v['residual']}" for c, v in r["ledger"].items())
        prec = [c for c, v in r["precision"].items() if v["flagged"]]
        rows.append(f"<tr><td>ledger</td><td colspan='3'>{esc(led)}"
                    f"{'' if r['ledger_all_runs_residual_zero'] else ' (not zero in every run)'}</td></tr>")
        rows.append(f"<tr><td>precision</td><td colspan='3'>"
                    + (esc("flagged: " + ", ".join(f"{c} (max {fmt_v(num(r['precision'][c]['max_reached']))}; "
                                                    f"{r['precision'][c]['unit_check']}; above 2^53: {r['precision'][c]['exceeds_2_53']})"
                                                    for c in prec)) if prec else "no currency flagged") + "</td></tr>")
        if "runs_summary" in r:
            rs = r["runs_summary"]
            for g in rs["goals"]:
                txt = (f"reached in {g['reached_runs']}/{g['runs']} runs, Wilson 95 % "
                       f"[{g['wilson_95'][0]:.3f}, {g['wilson_95'][1]:.3f}]")
                if g.get("window_pass_wilson_95") is not None:
                    tested = g.get("window_tested_runs", g["runs"])
                    txt += (f"; window pass {g['window_verdicts']['pass']}/{tested} tested runs, Wilson 95 % "
                            f"[{g['window_pass_wilson_95'][0]:.3f}, {g['window_pass_wilson_95'][1]:.3f}]")
                elif "window_verdicts" in g:
                    txt += "; window not testable in any run"
                if "active_s_median" in g:
                    txt += f"; active time min {fmt_t(g['active_s_min'])}, median {fmt_t(g['active_s_median'])}, max {fmt_t(g['active_s_max'])}"
                rows.append(f"<tr><td>runs</td><td>{esc(g['goal'])}</td><td>-</td><td>{esc(txt)}</td></tr>")
            rows.append(f"<tr><td>runs</td><td colspan='3'>{esc(rs['interval_method'])}. {esc(rs['note'])}.</td></tr>")
        out.append(f"<h3>{i}. {esc(_policy_name(r))}</h3><div class='scroll'><table><thead><tr><th>kind</th><th>what</th>"
                   f"<th>active time</th><th>evidence</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>")
    return "".join(out)


CSS = """
:root{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;
--grid:#e1e0d9;--axis:#c3c2b7;--border:rgba(11,11,11,.10);--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;
--s5:#e87ba4;--s6:#008300;--s7:#6250d6;--s8:#e34948;--good:#0ca30c;--warning:#fab219;--critical:#d03b3b;--good-text:#006300}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;
--ink:#f0efec;--ink2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--s1:#3987e5;
--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;--good-text:#0ca30c}}
:root[data-theme="dark"]{color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--muted:#898781;
--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;
--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;--good-text:#0ca30c}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1080px;margin:0 auto;padding:16px}
h1{font-size:1.4rem;margin:.2em 0}h2{font-size:1.15rem;margin:1.4em 0 .4em}h3{font-size:1rem;margin:1em 0 .3em}
.muted{color:var(--ink2);font-size:.85em}code{font-size:.85em;overflow-wrap:anywhere}
.panel,.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px;margin:10px 0}
.assumptions{border-left:4px solid var(--warning)}
.grid-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
figure{margin:0}figcaption{font-weight:600;margin-bottom:4px}
.scroll{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;font-size:.85em;width:100%}
th,td{border-bottom:1px solid var(--grid);padding:4px 6px;text-align:left;vertical-align:top}
th{color:var(--ink2);font-weight:600}td{font-variant-numeric:tabular-nums}
svg{display:block;width:100%;height:auto}
svg.timeline{min-width:600px}
svg text{fill:var(--ink2);font-size:11px;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
svg .tick{fill:var(--muted);font-size:11px}svg .axis-label{fill:var(--ink2);font-size:12px}
svg .row-label{fill:var(--ink);font-size:12px;font-weight:600}svg .small{font-size:10px}
.grid{stroke:var(--grid);stroke-width:1}.axis{stroke:var(--axis);stroke-width:1}
.track{stroke:var(--axis);stroke-width:2}.refline{stroke:var(--ink2);stroke-width:1}.endtick{stroke:var(--ink2);stroke-width:2}
.line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.goal{fill:var(--s1);stroke:var(--surface);stroke-width:2}.reset{fill:var(--ink2);stroke:var(--surface);stroke-width:1.5}.spike{fill:var(--s7);stroke:var(--surface);stroke-width:1.5}
.dot{stroke:var(--surface);stroke-width:2}path.dots{fill:none;stroke-width:5;stroke-linecap:round}.hit{fill:transparent}
.soft{fill:var(--warning);fill-opacity:.45}.hard{fill:url(#hatch)}
.hatch-bg{fill:var(--critical);fill-opacity:.15}.hatch{stroke:var(--critical);stroke-width:2}
.blocked{fill:var(--critical);font-size:14px;font-weight:700}
.window{fill:var(--muted);fill-opacity:.35}.w-pass{fill:var(--good);fill-opacity:.45}.w-fail{fill:var(--critical);fill-opacity:.45}
.s1{stroke:var(--s1);fill:var(--s1)}.s2{stroke:var(--s2);fill:var(--s2)}.s3{stroke:var(--s3);fill:var(--s3)}
.s4{stroke:var(--s4);fill:var(--s4)}.s5{stroke:var(--s5);fill:var(--s5)}.s6{stroke:var(--s6);fill:var(--s6)}
.s7{stroke:var(--s7);fill:var(--s7)}.s8{stroke:var(--s8);fill:var(--s8)}path.line{fill:none}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.85em;color:var(--ink2);margin:4px 0 8px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.key{display:inline-block;width:16px;height:3px;border-radius:2px;background:currentColor}
.key.s1{background:var(--s1)}.key.s2{background:var(--s2)}.key.s3{background:var(--s3)}.key.s4{background:var(--s4)}
.key.s5{background:var(--s5)}.key.s6{background:var(--s6)}.key.s7{background:var(--s7)}.key.s8{background:var(--s8)}
.sw{display:inline-block;width:14px;height:12px;border-radius:2px}
.sw-goal{width:10px;height:10px;border-radius:50%;background:var(--s1)}.sw-soft{background:var(--warning);opacity:.6}
.sw-hard{background:repeating-linear-gradient(45deg,var(--critical) 0 2px,transparent 2px 5px)}
.sw-spike{width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:9px solid var(--s7);border-radius:0}
.sw-reset{width:10px;height:10px;transform:rotate(45deg);background:var(--ink2);border-radius:1px}.sw-pass{background:var(--good);opacity:.6;height:6px}.sw-fail{background:var(--critical);opacity:.6;height:6px}
.v-pass{color:var(--good-text);font-weight:600}.v-fail{color:var(--critical);font-weight:600}.v-not-testable{color:var(--ink2)}
details summary{cursor:pointer;color:var(--ink2);font-size:.85em}
"""

LEGEND = ('<div class="legend"><span><i class="sw sw-goal"></i>goal reached</span><span><i class="sw sw-soft"></i>soft wall</span>'
          '<span><i class="sw sw-hard"></i>hard wall (affordable, locked)</span><span><i class="sw sw-spike"></i>power spike</span>'
          '<span><i class="sw sw-reset"></i>reset (prestige)</span><span><i class="sw sw-pass"></i>✓ window pass</span><span><i class="sw sw-fail"></i>✗ window fail</span>'
          '<span>✕ goal(s) not reached at run end</span></div>')


def shared_curves(reports) -> list:
    """Model curves drawn once per distinct content: models of the same game that share a curve (same title,
    axes and points) get one chart whose title names every model revision that has it."""
    models, seen = [], set()
    for r in reports:
        key = (r["model"]["sha256"], r["model"]["revision"])
        if key not in seen:
            seen.add(key)
            models.append((r["model"]["revision"], r["curves"]))
    groups = {}  # curve id -> [[curve, [revisions]], ...], in first-seen order

    def same(a, b):
        """Same curve: same title, axes and series, and the points agree on the shorter range (the range a
        report shows depends on how far its run went)."""
        if any(a.get(k) != b.get(k) for k in ("title", "x", "y", "series")):
            return False
        pa, pb = a.get("points") or [], b.get("points") or []
        n = min(len(pa), len(pb))
        return pa[:n] == pb[:n]

    for rev, cs in models:
        for cu in cs:
            variants = groups.setdefault(cu["id"], [])
            for v in variants:
                if same(v[0], cu):
                    if len(cu.get("points") or []) > len(v[0].get("points") or []):
                        v[0] = cu  # keep the longest range
                    v[1].append(rev)
                    break
            else:
                variants.append([cu, [rev]])
    out = []
    for variants in groups.values():
        for cu, revs in variants:
            if len(models) > 1:
                cu = dict(cu, title=f"{cu['title']} · model{'s' if len(revs) > 1 else ''} {', '.join(revs)}")
            out.append(cu)
    return out


def wait_curves(reports) -> list:
    out = []
    for i, r in enumerate(reports, 1):
        pts = [[s["t_active_s"], s["wait_s"]] for s in r.get("steps", []) if num(s["wait_s"]) > 0]
        if pts:
            ln = r.get("lean", {})
            lean = (f" (lean report: first {ln.get('first_steps_kept', 0)} steps in full, then only resets, goals, "
                    "walls and spikes)") if ln.get("on") else ""
            th = (r["walls"]["soft"].get("thresholds") or {}).get("min_wait_s")
            out.append({"id": f"wait:{i}", "title": f"{i}. {_policy_name(r)} · {r['model']['revision']}{lean}",
                        "x": "active time at step end (s)", "y": "wait (s)", "points": pts, "marks": "dots",
                        "hline": (th, f"soft-wall threshold {fmt_t(num(th))}") if th is not None else None})
    return out


def metric_curves(reports) -> list:
    ids = []
    for r in reports:
        for m in r["spikes"]["metrics"]:
            if m["id"] not in ids:
                ids.append(m["id"])
    out = []
    for mid in ids:
        series, label = [], mid
        for i, r in enumerate(reports, 1):
            m = next((x for x in r["spikes"]["metrics"] if x["id"] == mid), None)
            if m is None:
                continue
            label = f"{mid}: {m['metric']} vs {m['reference']} ({m['direction']})"
            pts = [[h["t_active_s"], h["value"]] for h in m["history"] if h["value"] is not None]
            if pts:
                pts.append([r["stop"]["active_s"], pts[-1][1]])  # the last value holds to the end of the run
                series.append({"name": f"{i}. {_policy_name(r)}", "points": pts})
        if series:
            out.append({"id": f"metric:{mid}", "title": label, "x": "active time (s)", "y": mid, "series": series,
                        "step": True})
    return out


def render(reports: list, title: str | None = None) -> str:
    if not reports:
        raise ValueError("at least one report is needed")
    for r in reports:
        if r.get("tool") != "progression_sim":
            raise ValueError("input is not a progression_sim report")
    title = title or reports[0]["model"]["title"] or reports[0]["model"]["revision"]
    curves = shared_curves(reports)
    n_assumed = len({(r["model"]["sha256"], r["model"]["revision"], a["input"])
                     for r in reports for a in r["assumptions"]["inputs"]})
    active = timeline_svg(reports, "active")
    calendar = timeline_svg(reports, "calendar") if any(r["stop"]["calendar_s"] is not None for r in reports) else ""
    body = [
        f"<h1>{esc(title)}</h1>",
        "<p class='muted'>Each row is one modelled strategy (policy), not the player population. A window pass means "
        "the measured time is inside the declared window; it is not a verdict that the game is fun.</p>",
        meta_table(reports),
        f"<p class='panel assumptions'>{n_assumed} model input(s) are EXAMPLE ASSUMPTION or PROPOSAL; every result "
        "below depends on them and on the modelled behaviour. <a href='#assumptions'>See the assumptions panel</a>.</p>",
        "<h2>Timeline (active play time)</h2>", LEGEND,
        active or "<p>No timeline data.</p>",
    ]
    if calendar:
        body += ["<h2>Timeline (calendar time, from the session pattern)</h2>", calendar]
    body += ["<h2>Goals by policy</h2>", goals_table(reports), assumptions_panel(reports),
             "<h2>Walls, spikes, blocked paths, ledger and precision</h2>", findings_tables(reports)]
    waits = wait_curves(reports)
    if waits:
        body += ["<h2>Wait per step (active seconds since the previous step)</h2>",
                 "<p class='muted'>One dot per purchase, level-up, first defeat, first completion or reset with a "
                 "non-zero wait; a soft wall is a dot above the declared threshold. Steps at the same instant "
                 "(wait 0) are left out.</p><div class='grid-cards'>", "".join(curve_svg(c) for c in waits), "</div>"]
    metrics = metric_curves(reports)
    if metrics:
        body += ["<h2>Reference metrics over time (one line per policy)</h2>",
                 "<p class='muted'>Each value holds until the next change; a gap means the metric was not measured "
                 "(its active_when was false, or the value was 'never').</p><div class='grid-cards'>",
                 "".join(curve_svg(c) for c in metrics), "</div>"]
    if curves:
        body += ["<h2>Curves the model declares</h2><div class='grid-cards'>", "".join(curve_svg(c) for c in curves), "</div>"]
    body.append(f"<p class='muted'>chart.py {VERSION}. Generated from {len(reports)} report(s); no network resources.</p>")
    return ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>{esc(title)}</title><style>{CSS}</style></head><body><main>{''.join(body)}</main></body></html>\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="chart", description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reports", nargs="+", help="sim.py report JSON files")
    ap.add_argument("--out", required=True, help="HTML file to write")
    ap.add_argument("--title")
    a = ap.parse_args(argv)
    reps = [json.loads(Path(p).read_text(encoding="utf-8")) for p in a.reports]
    try:
        page = render(reps, a.title)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8", newline="\n")
    print(out.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
