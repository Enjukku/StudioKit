#!/usr/bin/env python3
"""Trend metrics over stored history (formulas: knowledge/reference/trends/01-roblox-data-loops.md §8).

All functions are pure. A series is [(datetime UTC, value)] sorted by time. Thresholds come from
config.json (trend_store.load_config) and are passed in; none live in a formula.

  integrate      trapezoid player-hours between adjacent samples no further apart than max_gap; longer gaps
                 are not bridged. Reports covered hours, coverage and the longest uncovered run with every window.
  g7             meanCCU(last 7 complete UTC days) / meanCCU(previous 7) - 1, non-overlapping windows;
                 zero or missing baseline -> "new / insufficient baseline", never infinity.
  momentum       24 h mean / overlapping 7 d mean, labelled "momentum, not week-over-week"; held under the gate.
  daily_trough   lowest off-event daily mean (F §2), days gated on the full series.
  breakout, fade PROPOSAL flags (RP:97, RP:99); suppressed when coverage or max gap fail the gate.
  playtime       60 x player-hours / added visits over matched boundaries; always labelled an estimate.

Python 3.11+ standard library only.
"""
from __future__ import annotations

from datetime import datetime, timedelta

HOUR = timedelta(hours=1)
DAY = timedelta(days=1)
WEEK = timedelta(days=7)
NO_BASELINE = "new / insufficient baseline"
MOMENTUM_LABEL = "momentum, not week-over-week"
PLAYTIME_LABEL = "estimate: occupancy / arrivals, not session telemetry"


def _interp(t0, v0, t1, v1, t):
    span = (t1 - t0).total_seconds()
    return v0 if span == 0 else v0 + (v1 - v0) * (t - t0).total_seconds() / span


def integrate(series, start: datetime, end: datetime, max_gap: timedelta) -> dict:
    """Player-hours and coverage for [start, end). Segments longer than max_gap count as uncovered."""
    ph = 0.0
    covered: list[tuple[datetime, datetime]] = []
    for (t0, v0), (t1, v1) in zip(series, series[1:]):
        if t1 - t0 > max_gap or t1 <= start or t0 >= end:
            continue
        a, b = max(t0, start), min(t1, end)
        if b <= a:
            continue
        va, vb = _interp(t0, v0, t1, v1, a), _interp(t0, v0, t1, v1, b)
        ph += (va + vb) / 2 * ((b - a) / HOUR)
        covered.append((a, b))
    covered_h = sum((b - a) / HOUR for a, b in covered)
    longest, cursor = timedelta(0), start
    for a, b in covered:
        longest = max(longest, a - cursor)
        cursor = max(cursor, b)
    longest = max(longest, end - cursor)
    inside = [v for t, v in series if start <= t < end]
    window_h = (end - start) / HOUR
    return {
        "start": start, "end": end, "player_hours": ph, "covered_hours": covered_h, "window_hours": window_h,
        "coverage": covered_h / window_h if window_h else 0.0, "max_gap_minutes": longest / timedelta(minutes=1),
        "mean_ccu": ph / covered_h if covered_h > 0 else None, "samples": len(inside),
        "peak": max(inside) if inside else None, "trough": min(inside) if inside else None,
    }


def week_end(as_of: datetime) -> datetime:
    """End of the last complete UTC day at or before as_of (week_boundary = complete UTC days)."""
    return as_of.replace(hour=0, minute=0, second=0, microsecond=0)


def weeks(series, as_of: datetime, count: int, max_gap: timedelta) -> list[dict]:
    """Non-overlapping 7-day windows of complete UTC days, newest first."""
    end = week_end(as_of)
    return [integrate(series, end - WEEK * (i + 1), end - WEEK * i, max_gap) for i in range(count)]


def passes_gate(window: dict, th: dict) -> bool:
    return window["coverage"] >= th["coverage_min"] and window["max_gap_minutes"] <= th["max_gap_minutes"]


def g7(current: dict, previous: dict) -> dict:
    cur, prev = current["mean_ccu"], previous["mean_ccu"]
    if cur is None or not prev:
        return {"value": None, "status": NO_BASELINE}
    return {"value": cur / prev - 1, "status": "ok"}


def momentum(series, as_of: datetime, th: dict) -> dict:
    """24 h mean / 7 d mean; value None ("insufficient coverage") unless both windows pass the coverage gate.
    coverage_24h is always returned so the page can print it next to the 24 h mean."""
    gap = timedelta(minutes=th["max_gap_minutes"])
    end = week_end(as_of)
    day, week = integrate(series, end - DAY, end, gap), integrate(series, end - WEEK, end, gap)
    out = {"value": None, "label": MOMENTUM_LABEL, "coverage_24h": day["coverage"], "coverage_7d": week["coverage"]}
    if day["mean_ccu"] is None:
        return {**out, "status": "no data in the last 24 h"}
    if not week["mean_ccu"]:
        return {**out, "status": NO_BASELINE}
    if not (passes_gate(day, th) and passes_gate(week, th)):
        return {**out, "status": "insufficient coverage"}
    return {**out, "value": day["mean_ccu"] / week["mean_ccu"], "status": "ok"}


def matched_days_above(series, as_of: datetime, th: dict) -> int:
    """Consecutive complete UTC days, counting back from the newest, whose mean CCU beats the same weekday one
    week earlier. A day failing the coverage gate on either side ends the run."""
    gap = timedelta(minutes=th["max_gap_minutes"])
    end, run = week_end(as_of), 0
    for i in range(7):
        d_end = end - DAY * i
        now_d = integrate(series, d_end - DAY, d_end, gap)
        then_d = integrate(series, d_end - DAY - WEEK, d_end - WEEK, gap)
        if not (passes_gate(now_d, th) and passes_gate(then_d, th)) or now_d["mean_ccu"] <= then_d["mean_ccu"]:
            break
        run += 1
    return run


def breakout(series, as_of: datetime, th: dict) -> dict:
    gap = timedelta(minutes=th["max_gap_minutes"])
    cur, prev = weeks(series, as_of, 2, gap)
    growth = g7(cur, prev)
    out = {"g7": growth, "current": cur, "previous": prev, "added_ccu": None, "matched_days": 0}
    if not passes_gate(cur, th):
        return {**out, "status": "suppressed: coverage", "reason": _gate_reason(cur, th, "current week")}
    if growth["status"] != "ok":
        return {**out, "status": NO_BASELINE, "reason": "previous week has no usable data (emerging lead)"}
    if not passes_gate(prev, th):
        return {**out, "status": "suppressed: coverage", "reason": _gate_reason(prev, th, "previous week")}
    added = cur["mean_ccu"] - prev["mean_ccu"]
    days = matched_days_above(series, as_of, th)
    out.update(added_ccu=added, matched_days=days)
    checks = [growth["value"] >= th["breakout_g7_min"], added >= th["breakout_added_ccu_min"],
              days >= th["breakout_consecutive_days"]]
    return {**out, "status": "breakout" if all(checks) else "no breakout",
            "reason": f"g7 {growth['value']:+.0%} (min {th['breakout_g7_min']:+.0%}), added {added:+.0f} CCU "
                      f"(min {th['breakout_added_ccu_min']}), matched days {days} (min {th['breakout_consecutive_days']})"}


def daily_trough(series, offevent_series, start: datetime, end: datetime, th: dict) -> float | None:
    """Lowest off-event daily mean CCU over the complete UTC days in [start, end). A day counts only when the
    full series passes the coverage gate that day (event hours are excluded on purpose, not missing data)."""
    gap = timedelta(minutes=th["max_gap_minutes"])
    means, d = [], start
    while d + DAY <= end:
        if passes_gate(integrate(series, d, d + DAY, gap), th):
            m = integrate(offevent_series, d, d + DAY, gap)["mean_ccu"]
            if m is not None:
                means.append(m)
        d += DAY
    return min(means, default=None)


def fade(series, offevent_series, as_of: datetime, th: dict) -> dict:
    """Two (fade_negative_weeks) negative non-overlapping weekly changes in a row plus a lower off-event trough.
    Coverage is gated on the full series; the changes and troughs use the off-event series."""
    gap = timedelta(minutes=th["max_gap_minutes"])
    n = int(th["fade_negative_weeks"])
    ws = weeks(series, as_of, n + 1, gap)
    if any(w["mean_ccu"] is None for w in ws):
        return {"status": "insufficient history", "reason": f"needs {n + 1} weeks with data"}
    bad = [w for w in ws if not passes_gate(w, th)]
    if bad:
        return {"status": "suppressed: coverage", "reason": _gate_reason(bad[0], th, "a compared week")}
    off = weeks(offevent_series, as_of, n + 1, gap)
    changes = [g7(off[i], off[i + 1]) for i in range(n)]
    troughs = [daily_trough(series, offevent_series, w["start"], w["end"], th) for w in ws[:2]]
    negative = all(c["status"] == "ok" and c["value"] < 0 for c in changes)
    lower = None not in troughs and troughs[0] < troughs[1]
    shown = ["n/a" if t is None else f"{t:,.0f}" for t in troughs]
    return {"status": "fade" if negative and lower else "no fade", "changes": changes, "troughs": troughs,
            "reason": "off-event weekly changes "
                      + ", ".join(f"{c['value']:+.0%}" for c in changes if c["value"] is not None)
                      + f"; lowest off-event daily mean {shown[0]} vs {shown[1]}"}


def acceleration_pp(series, as_of: datetime, th: dict) -> float | None:
    """g7(current) - g7(previous week), in percentage points."""
    w0, w1, w2 = weeks(series, as_of, 3, timedelta(minutes=th["max_gap_minutes"]))
    a, b = g7(w0, w1), g7(w1, w2)
    return None if a["value"] is None or b["value"] is None else (a["value"] - b["value"]) * 100


def counter_added(series, start: datetime, end: datetime) -> float | None:
    """Last minus first observed value of a cumulative counter inside [start, end); None with < 2 samples."""
    inside = [(t, v) for t, v in series if start <= t < end]
    return inside[-1][1] - inside[0][1] if len(inside) >= 2 else None


def playtime_estimate(ccu, visits, start: datetime, end: datetime, th: dict) -> dict:
    """60 x player-hours / added visits, both measured between the first and last visits sample in the window."""
    inside = [(t, v) for t, v in visits if start <= t < end]
    out = {"minutes_per_entry": None, "label": PLAYTIME_LABEL}
    if len(inside) < 2:
        return {**out, "status": "insufficient visits samples"}
    (t0, v0), (t1, v1) = inside[0], inside[-1]
    span = integrate(ccu, t0, t1, timedelta(minutes=th["max_gap_minutes"]))
    out.update(added_visits=v1 - v0, player_hours=span["player_hours"], coverage=span["coverage"])
    if v1 - v0 <= 0:
        return {**out, "status": "no added visits"}
    if not passes_gate(span, th):
        return {**out, "status": "suppressed: coverage"}
    return {**out, "minutes_per_entry": 60 * span["player_hours"] / (v1 - v0), "status": "ok"}


def approval(up: float | None, down: float | None) -> float | None:
    return None if up is None or down is None or up + down == 0 else up / (up + down)


def _gate_reason(w: dict, th: dict, name: str) -> str:
    return (f"{name} coverage {w['coverage']:.0%} (min {th['coverage_min']:.0%}), longest gap "
            f"{w['max_gap_minutes']:.0f} min (max {th['max_gap_minutes']})")
