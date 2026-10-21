# SYNTHETIC TEST DATA (universe 9000000001). J013-T05b. Author: analyst · claude-opus-5-5 · high · 2026-10-21
# Reads only the saved `analytics.py show` outputs in this folder (show-<metric>.json) and writes derived-counts.json.
# No network, no key. Rerun: python derive_counts.py  (from this folder)
# Assumption A1: the ForwardD1Retention / ForwardD7Retention cohort of a date = new players that date
#   = DailyActiveUsers with IsNewUser=true on that date. Estimated returners = round(rate x new players).
#   Roblox does not document the denominator in the API; this is an estimate, labelled as such.
# Assumption A2: Forward* values sit on the first-play date (analysis-craft data-tools.md §4: unknown to settle).
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))


def load(metric):
    with open(os.path.join(HERE, f"show-{metric}.json"), encoding="utf-8") as f:
        return json.load(f)["points"]


def series_key(p):
    return ";".join(f"{s['dimension']}={s['value']}" for s in p["series"]) or "total"


def table(metric, gran="OneDay"):
    t = {}
    for p in load(metric):
        if p["granularity"] != gran:
            continue
        t.setdefault(series_key(p), {})[p["bucket_time_utc"][:10]] = p["value"]
    return t


def days(a, b):
    d0, d1 = datetime.date.fromisoformat(a), datetime.date.fromisoformat(b)
    return [(d0 + datetime.timedelta(i)).isoformat() for i in range((d1 - d0).days + 1)]


dau = table("DailyActiveUsers")
d1 = table("ForwardD1Retention")
d7 = table("ForwardD7Retention")
mat = json.load(open(os.path.join(HERE, "maturity-all-cohorts.json"), encoding="utf-8"))["results"]
mature = {(r["metric"], r["first_play"]) for r in mat if r["mature"]}
new = dau["IsNewUser=true"]

daily = []
for d in sorted(d1["total"]):
    row = {"date": d, "new_players": new.get(d), "d1_rate": d1["total"][d],
           "d1_mature": ("ForwardD1Retention", d) in mature}
    row["d1_returners_est"] = round(row["d1_rate"] * row["new_players"]) if row["new_players"] else None
    if d in d7["total"]:
        row["d7_rate"] = d7["total"][d]
        row["d7_mature"] = ("ForwardD7Retention", d) in mature
        row["d7_returners_est"] = round(d7["total"][d] * new[d])
    daily.append(row)
by_date = {r["date"]: r for r in daily}


def period(name, a, b, key="d1"):
    rows = [by_date[d] for d in days(a, b)]
    ok = all(r[f"{key}_mature"] for r in rows)
    n = sum(r["new_players"] for r in rows)
    x = sum(r[f"{key}_returners_est"] for r in rows)
    return {"name": name, "first_play_from": a, "first_play_to": b, "outcome": key.upper(),
            "all_cohorts_mature": ok, "new_players": n, "returners_est": x,
            "rate_from_counts": round(x / n, 4)}


periods = [
    period("W-2 baseline", "2026-09-13", "2026-09-19"),
    period("W-1 baseline", "2026-09-20", "2026-09-26"),
    period("W0 last week before video", "2026-09-27", "2026-10-03"),
    period("W1 video week (v112 from Fri 10-09)", "2026-10-04", "2026-10-10"),
    period("W2 latest mature whole week (v112)", "2026-10-11", "2026-10-17"),
    period("B0 matched weekdays before video", "2026-09-27", "2026-10-01"),
    period("B1 video days before v112", "2026-10-04", "2026-10-08"),
    period("C1 first 5 days of v112", "2026-10-09", "2026-10-13"),
    period("D7 W0", "2026-09-27", "2026-10-03", "d7"),
    period("D7 W1", "2026-10-04", "2026-10-10", "d7"),
]
P = {p["name"]: p for p in periods}

# Excess-player split for the video days (B1) against the same weekdays one week earlier (B0).
b0, b1 = P["B0 matched weekdays before video"], P["B1 video days before v112"]
extra_n = b1["new_players"] - b0["new_players"]
extra_x = b1["returners_est"] - b0["returners_est"]
excess = {
    "method": "if the usual players kept B0's count and rate, the extra players are B1 minus B0 (both counts estimated, A1)",
    "extra_new_players": extra_n, "extra_returners_est": extra_x,
    "extra_players_d1_rate": round(extra_x / extra_n, 4),
    "usual_players_rate_B0": b0["rate_from_counts"], "observed_rate_B1": b1["rate_from_counts"],
}

# Rough split of the latest mature whole week (W2) against W0. ESTIMATE, assumptions:
#   A3: W2 holds W0's number of usual new players; every new player above that is "extra".
#   A4: extra players return at the rate measured for the extra video players in B1 (excess split above).
# expected = usual at W0's rate + extra at A4's rate; the gap to observed is what the player mix does not explain.
w0, w2 = P["W0 last week before video"], P["W2 latest mature whole week (v112)"]
w2_extra = w2["new_players"] - w0["new_players"]
expected = w0["returners_est"] + round(w2_extra * excess["extra_players_d1_rate"])
w2_split = {
    "label": "ESTIMATE (A1, A3, A4)",
    "w0_rate": w0["rate_from_counts"], "w2_rate_observed": w2["rate_from_counts"],
    "w2_extra_new_players": w2_extra, "w2_returners_expected_from_mix_only": expected,
    "w2_rate_expected_from_mix_only": round(expected / w2["new_players"], 4),
    "w2_returners_observed": w2["returners_est"],
    "returners_not_explained_by_mix": expected - w2["returners_est"],
    "points_explained_by_mix": round((w0["rate_from_counts"] - expected / w2["new_players"]) * 100, 2),
    "points_not_explained_by_mix": round((expected - w2["returners_est"]) / w2["new_players"] * 100, 2),
}

# Ranges (no averages of daily rates: daily denominators by segment are not pulled).
def rng(tab, keys, a, b):
    out = {}
    for k in keys:
        vals = [tab[k][d] for d in days(a, b) if d in tab.get(k, {})]
        out[k] = {"min": min(vals), "max": max(vals), "days": len(vals)} if vals else None
    return out

src = ["AcquisitionSource=Friends", "AcquisitionSource=HomeRecommendations", "AcquisitionSource=Search", "AcquisitionSource=Other"]
plat = ["Platform=Computer", "Platform=Console", "Platform=Phone", "Platform=Tablet"]
crash = table("ClientCrashRate15m"); fps = table("ClientFpsP10")
ranges = {}
for name, a, b in (("B0", "2026-09-27", "2026-10-01"), ("pre-video 9-25..10-03", "2026-09-25", "2026-10-03"),
                   ("B1", "2026-10-04", "2026-10-08"), ("C1", "2026-10-09", "2026-10-13"),
                   ("W2", "2026-10-11", "2026-10-17"), ("post-v112 10-09..10-18", "2026-10-09", "2026-10-18")):
    ranges[name] = {"d1_by_source": rng(d1, src, a, b), "d1_by_platform": rng(d1, plat, a, b),
                    "dau_by_source": rng(dau, src, a, b), "new_players": rng(dau, ["IsNewUser=true"], a, b),
                    "crash_rate_by_platform": rng(crash, plat, a, b), "fps_p10_by_platform": rng(fps, plat, a, b)}

# Reconciliation checks.
recon = {"dau_platform_sum_ne_total": [], "dau_newuser_sum_ne_total": [], "dau_source_sum_minus_total": {},
         "d1_total_outside_platform_range": [], "d1_total_outside_source_range": [],
         "d1_tablet_equals_console_days": [], "crash_total_ne_only_returned_version": []}
for d, tot in dau["total"].items():
    if sum(dau[k].get(d, 0) for k in plat) != tot: recon["dau_platform_sum_ne_total"].append(d)
    if dau["IsNewUser=true"].get(d, 0) + dau["IsNewUser=false"].get(d, 0) != tot: recon["dau_newuser_sum_ne_total"].append(d)
    if all(d in dau[k] for k in src): recon["dau_source_sum_minus_total"][d] = sum(dau[k][d] for k in src) - tot
for d, v in d1["total"].items():
    pv = [d1[k][d] for k in plat if d in d1.get(k, {})]
    sv = [d1[k][d] for k in src if d in d1.get(k, {})]
    if pv and not (min(pv) <= v <= max(pv)): recon["d1_total_outside_platform_range"].append({"date": d, "total": v, "platform_min": min(pv), "platform_max": max(pv)})
    if sv and not (min(sv) <= v <= max(sv)): recon["d1_total_outside_source_range"].append(d)
    if d in d1.get("Platform=Tablet", {}) and d1["Platform=Tablet"][d] == d1["Platform=Console"][d]: recon["d1_tablet_equals_console_days"].append(d)
for d, v in crash["total"].items():
    vers = [k for k in crash if k.startswith("PlaceVersion=") and d in crash[k]]
    if len(vers) == 1 and crash[vers[0]][d] != v: recon["crash_total_ne_only_returned_version"].append({"date": d, "total": v, vers[0]: crash[vers[0]][d]})
ident = {}
for m in ("ServerFrameRateP10", "ServerFrameRateP50", "MemoryUsageP90", "SessionDurationSecondsP50"):
    ident[m] = {p["bucket_time_utc"][:10]: p["value"] for p in load(m)}
recon["identical_series_ServerFrameRateP10_P50_MemoryUsageP90_SessionDurationSecondsP50"] = (
    ident["ServerFrameRateP10"] == ident["ServerFrameRateP50"] == ident["MemoryUsageP90"] == ident["SessionDurationSecondsP50"])

out = {"label": "SYNTHETIC TEST DATA", "assumptions": ["A1", "A2"], "periods": periods, "excess_split_video_days": excess,
       "latest_week_rough_split": w2_split, "segment_ranges": ranges, "reconciliation": recon, "daily": daily}
with open(os.path.join(HERE, "derived-counts.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print(json.dumps({"periods": periods, "excess": excess, "latest_week_rough_split": w2_split}, indent=1))
