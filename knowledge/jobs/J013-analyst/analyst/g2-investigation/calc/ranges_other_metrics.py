# SYNTHETIC TEST DATA (universe 9000000001). J013-T05b. Author: analyst · claude-opus-5-5 · high · 2026-10-21
# Min/max per period for the totals that support the investigation. Reads only show-<metric>.json in this folder.
# Ranges, never averages of daily values. Not-final points are listed separately and left out of the ranges.
# Rerun: python ranges_other_metrics.py  (from this folder) -> ranges-other-metrics.json
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PERIODS = {
    "pre_video_2026-09-09..10-03": ("2026-09-09", "2026-10-03"),
    "pre_video_perf_2026-09-25..10-03": ("2026-09-25", "2026-10-03"),
    "pre_v112_2026-09-25..10-08": ("2026-09-25", "2026-10-08"),
    "video_pre_v112_2026-10-04..10-08": ("2026-10-04", "2026-10-08"),
    "post_v112_2026-10-09..10-18": ("2026-10-09", "2026-10-18"),
    "post_v112_2026-10-09..10-20": ("2026-10-09", "2026-10-20"),
    "post_video_2026-10-04..10-18": ("2026-10-04", "2026-10-18"),
}
METRICS = [("ForwardD1Retention", "total"), ("DailyActiveUsers", "IsNewUser=true"), ("DailyActiveUsers", "total"),
           ("DailyActiveUsers", "AcquisitionSource=Other"), ("DailyActiveUsers", "AcquisitionSource=HomeRecommendations"),
           ("DailyActiveUsers", "Platform=Phone"),
           ("ClientCrashCount", "total"), ("OomUnexpectedExits", "total"), ("ClientMemoryUsageP90", "total"),
           ("ClientCrashRate15m", "Platform=Phone"), ("ClientCrashRate15m", "Platform=Computer"),
           ("ClientCrashRate15m", "Platform=Tablet"), ("ClientCrashRate15m", "Platform=Console"),
           ("ClientFpsP10", "Platform=Phone"), ("ClientFpsP10", "Platform=Computer"), ("ClientFpsP10", "Platform=Tablet"),
           ("ClientFpsP10", "Platform=Console"), ("ClientFpsP50", "total"), ("PeakConcurrentPlayers", "total"),
           ("AverageSessionLengthMinutes", "total"), ("DailyRevenue", "total"), ("PayingUsers", "total"),
           ("PayingUsersCVR", "total"), ("AverageRevenuePerPayingUser", "total"), ("ForwardD7Retention", "total")]

out = {"label": "SYNTHETIC TEST DATA", "ranges": {}, "not_final_points": []}
for metric, key in METRICS:
    pts = json.load(open(os.path.join(HERE, f"show-{metric}.json"), encoding="utf-8"))["points"]
    vals = {}
    for p in pts:
        k = ";".join(f"{s['dimension']}={s['value']}" for s in p["series"]) or "total"
        if p["granularity"] != "OneDay" or k != key:
            continue
        d = p["bucket_time_utc"][:10]
        if not p["final"]:
            out["not_final_points"].append({"metric": metric, "series": key, "date": d, "value": p["value"], "status": p["point_status"]})
            continue
        vals[d] = p["value"]
    r = {}
    for name, (a, b) in PERIODS.items():
        sel = {d: v for d, v in vals.items() if a <= d <= b}
        if sel:
            r[name] = {"min": min(sel.values()), "max": max(sel.values()), "days": len(sel),
                       "first": min(sel), "last": max(sel)}
    out["ranges"][f"{metric}|{key}"] = r
with open(os.path.join(HERE, "ranges-other-metrics.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
for k, r in out["ranges"].items():
    print(k)
    for n, v in r.items():
        print("   ", n, v["min"], v["max"], v["days"])
print("not final:", [(p["metric"], p["series"], p["date"], p["status"]) for p in out["not_final_points"]][:12], len(out["not_final_points"]))
