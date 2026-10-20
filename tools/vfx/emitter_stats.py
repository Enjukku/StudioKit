#!/usr/bin/env python3
"""Flatten the STUDY set of pro VFX dumps into emitter rows, classify each emitter's job, compute stats.

Usage:
  python tools/vfx/emitter_stats.py rows            # write output/vfx/training-dumps/emitters_study.jsonl
  python tools/vfx/emitter_stats.py report OUT.md   # write generated markdown tables (used to build building-blocks.md)

The hidden test set (HIDDEN) is filtered by file name BEFORE any file is opened.
Rows are the single source for every number in knowledge/reference/vfx/training/building-blocks.md.
"""
from __future__ import annotations

import json
import math
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DUMPS = os.path.join(ROOT, "output", "vfx", "training-dumps")
CATALOG = os.path.join(ROOT, "content", "vfx", "library", "catalog.json")
ROWS_PATH = os.path.join(DUMPS, "emitters_study.jsonl")

# Hidden test set: never opened. Matched on the file stem.
HIDDEN = (
    "sTier__Missile_Sequence",
    "sTier__Purple_arcane_showcase",
    "aTier__Slashes",
    "aTier__Constellations",
    "bTier__explosion",
    "bTier__Healing_VFX",
    "cTier__fiya_beam",
    "Unknown__Portal_VFX",
)
TIER_OF = {"sTier": "S", "aTier": "A", "bTier": "B", "cTier": "C", "Unknown": "U"}
SHAPE_T = (0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0)
VFX_CLASSES = ("ParticleEmitter", "Beam", "Trail", "PointLight", "SpotLight", "SurfaceLight")

# ----------------------------------------------------------------------------- sequence helpers


def seq_points(seq):
    """[[t, v, env], ...] -> sorted [(t, v)] (colour keypoints are skipped, use colour_points)."""
    pts = []
    for k in seq or []:
        pts.append((float(k[0]), float(k[1])))
    pts.sort(key=lambda p: p[0])
    return pts


def seq_at(pts, t):
    """Linear interpolation of a NumberSequence at t (Roblox semantics)."""
    if not pts:
        return 0.0
    if t <= pts[0][0]:
        return pts[0][1]
    if t >= pts[-1][0]:
        return pts[-1][1]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        if t0 <= t <= t1:
            if t1 == t0:
                return v1
            return v0 + (v1 - v0) * (t - t0) / (t1 - t0)
    return pts[-1][1]


def size_shape(seq, ts=SHAPE_T):
    """Size curve as fractions of its own max (negative keypoints clamp to 0). None if max <= 0."""
    pts = [(t, max(0.0, v)) for t, v in seq_points(seq)]
    if not pts:
        return None
    m = max(v for _, v in pts)
    if m <= 1e-9:
        return None
    return [seq_at(pts, t) / m for t in ts]


def value_shape(seq, ts=SHAPE_T):
    """Raw curve values at ts (used for Transparency, already 0..1)."""
    pts = seq_points(seq)
    if not pts:
        return None
    return [seq_at(pts, t) for t in ts]


def peak_size(seq):
    pts = seq_points(seq)
    return max([v for _, v in pts], default=0.0)


def size_class(seq):
    """grow / shrink / bump / flat / other, from the size curve as fraction of its max (dense sampling)."""
    sh = size_shape(seq, tuple(i / 20.0 for i in range(21)))
    if not sh:
        return None
    s0, s1, mx_i = sh[0], sh[-1], max(range(len(sh)), key=lambda i: sh[i])
    if min(sh) >= 0.8:
        return "flat"
    if s0 <= 0.6 and s1 >= 0.8:
        return "grow"
    if s0 >= 0.7 and s1 <= 0.3:
        return "shrink"
    if 1 <= mx_i <= 19 and s0 < 0.8 and s1 < 0.8 and sh[mx_i] - max(s0, s1) > 0.2:
        return "bump"
    return "other"


def transp_class(seq):
    """fade-out / fade-in-out / fade-in / opaque / faint / partial, from the transparency curve (dense sampling)."""
    pts = seq_points(seq)
    if not pts:
        return None
    v = [seq_at(pts, i / 20.0) for i in range(21)]
    a, b, mn = v[0], v[-1], min(v)
    if mn > 0.7:
        return "faint"
    if max(v) < 0.3:
        return "opaque"
    if a > 0.5 and b > 0.5:
        return "fade-in-out"
    if b > 0.5 and a <= 0.5:
        return "fade-out"
    if a > 0.5 and b <= 0.5:
        return "fade-in"
    return "partial"


def pctl(vals, q):
    """Linear-interpolated percentile, q in 0..100. None for empty."""
    v = sorted(x for x in vals if x is not None and not (isinstance(x, float) and math.isnan(x)))
    if not v:
        return None
    if len(v) == 1:
        return v[0]
    pos = (len(v) - 1) * q / 100.0
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    return v[lo] + (v[hi] - v[lo]) * (pos - lo)


def summarize(vals):
    """{n, med, p10, p90} over non-None values."""
    v = [x for x in vals if x is not None]
    return {"n": len(v), "med": pctl(v, 50), "p10": pctl(v, 10), "p90": pctl(v, 90)}


def median_curve(curves):
    """Per-index median over equal-length curves (None skipped)."""
    cs = [c for c in curves if c]
    if not cs:
        return None
    return [statistics.median(c[i] for c in cs) for i in range(len(cs[0]))]


def share(rows, pred):
    n = len(rows)
    return (sum(1 for r in rows if pred(r)) / n) if n else None


def mean_range(r):
    if not r:
        return None
    return (float(r[0]) + float(r[-1])) / 2.0


def colour_points(seq):
    return [(float(k[0]), tuple(float(c) for c in k[1])) for k in seq or []]


def colour_changes(seq, thresh=30.0):
    """True if the colour sequence moves more than thresh (0..255) in any channel."""
    cp = colour_points(seq)
    if len(cp) < 2:
        return False
    for ch in range(3):
        vals = [c[ch] for _, c in cp]
        if max(vals) - min(vals) > thresh:
            return True
    return False


def luminance(rgb):
    if rgb is None:
        return None
    r, g, b = (c / 255.0 for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# ----------------------------------------------------------------------------- IO


def study_files():
    out = []
    for f in sorted(os.listdir(os.path.join(DUMPS, "json"))):
        if not f.endswith(".json"):
            continue
        stem = f[:-5]
        if stem in HIDDEN:
            continue
        out.append(stem)
    return out


def load_catalog():
    with open(CATALOG, encoding="utf-8") as fh:
        return {r["id"]: r for r in json.load(fh)["rows"]}


def tex_id(tex):
    m = re.search(r"(\d+)\s*$", tex or "")
    return int(m.group(1)) if m else None


def parse_attrs(stem):
    """{(path, class): [ {k: v}, ... ]} in file order (duplicate paths keep order)."""
    p = os.path.join(DUMPS, "attributes", stem + ".txt")
    out = defaultdict(list)
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            m = re.match(r"^(/.*?) \[(\w+)\] (.*)$", line.rstrip("\n"))
            if not m:
                continue
            kv = dict(re.findall(r"(\w+)=(\S*)", m.group(3)))
            out[(m.group(1), m.group(2))].append(kv)
    return out


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------------- classification

JOBS = (
    "core", "glow/halo", "flare/star", "ring/shockwave", "spark", "ember/spec", "flame body", "smoke",
    "dark underlay/twin", "wisp/swirl", "streak/speedline", "slash/crescent", "debris/chunks",
    "flipbook burst", "ground decal", "impact burst", "liquid/splash", "lightning/electric", "other",
)

# (job, regex on the emitter NAME). First match wins, order matters.
NAME_RULES = [
    ("smoke", r"smoke|fog|dust|cloud|steam|vapou?r|mist|puff|haze"),
    ("slash/crescent", r"slash|crescent|swipe|blade|swing"),
    ("lightning/electric", r"lightning|electric|zap|thunder|bolt"),
    ("liquid/splash", r"water|splash|drip|droplet|bubble|rain|liquid|ripple"),
    ("ground decal", r"ground|crack|rune|decal|floor|glyph"),
    ("ring/shockwave", r"ring|shock|circular|circle|donut|pulse|wave(?!y)"),
    ("impact burst", r"impact|smack|hit\b|basic hit|punch|burst"),
    ("flare/star", r"flare|star|twinkl|shine|glint|lens|sparkle|snowflake|constellation(?! spec)"),
    ("ember/spec", r"spec|ember|firefl|fleck|glitter|ash|pixel|dots?\b|sprinkle|speck"),
    ("spark", r"spark"),
    ("flame body", r"fire|flame|blaze|inferno|lava|magma|burn|^fb?$"),
    ("debris/chunks", r"debris|chunk|rock|shard|stone|rubble|fragment|splinter|gem|crystal|leaf|petal|emerald"),
    ("streak/speedline", r"wind|speed|streak|trail|line\b|thin"),
    ("wisp/swirl", r"swirl|wisp|spiral|vortex|tornado|twist|wavey|wiggly|bezier|rainbow|chrome|energy|aura|electr"),
    ("glow/halo", r"glow|halo|bloom|blur|overlay|aura|soft"),
    ("core", r"core|orb|ball|blob|main|center|sphere|head|bastard"),
]
# Catalog texture shape -> job
SHAPE_JOB = {
    "ring": "ring/shockwave", "ring-broken": "ring/shockwave", "ring-double": "ring/shockwave",
    "swirl": "wisp/swirl", "spiral": "wisp/swirl", "vortex": "wisp/swirl", "energy-wisp": "wisp/swirl",
    "smoke-wisp": "smoke", "smoke-puff": "smoke", "smoke-flipbook": "smoke",
    "aura-flame": "flame body", "flame-tongue": "flame body", "fire-flipbook": "flame body",
    "spark-dots": "ember/spec", "spark-lines": "spark",
    "star-4": "flare/star", "star-6": "flare/star", "star-many": "flare/star", "burst-rays": "flare/star",
    "impact-burst": "impact burst", "glow-round": "glow/halo", "gradient": "glow/halo", "orb": "core",
    "streak": "streak/speedline", "slash-arc": "slash/crescent", "crescent": "slash/crescent",
    "lightning-bolt": "lightning/electric", "lightning-branch": "lightning/electric",
    "debris": "debris/chunks", "shard": "debris/chunks", "leaf-petal": "debris/chunks",
    "crack": "ground decal", "splash": "liquid/splash",
}
GROUP_JOB = {
    "Smoke": "smoke", "Fire": "flame body", "Spec": "ember/spec", "Flare": "flare/star", "Star": "flare/star",
    "Impact": "impact burst", "Slashes": "slash/crescent", "Lightning": "lightning/electric",
    "Swirl": "wisp/swirl", "Energy": "wisp/swirl", "Ground": "ground decal", "Water": "liquid/splash",
    "Circle": "ring/shockwave",
}
ORIENT_NAMES = {0: "FacingCamera", 1: "FacingCameraWorldUp", 2: "VelocityParallel", 3: "VelocityPerpendicular"}


def classify(f):
    """f: feature dict (see row_features). Returns (job, rule). Rules documented in building-blocks.md."""
    # digits are stripped: library names carry ids ("Spec19", "Ele1ctric", "D33ark")
    name = re.sub(r"\d+", "", f["name"].lower()).strip()
    ctx = re.sub(r"\d+", "", f["ctx"].lower())  # last three ancestor names
    # 1. smoke by name (dark smoke stays smoke)
    for job, rx in NAME_RULES[:1]:
        if re.search(rx, name):
            return job, "name:" + rx
    # 2. velocity-parallel + squash = streak (unless the name already says slash/lightning)
    if f["orient"] == 2 and f["squash"] and not re.search(r"slash|crescent|lightning|electric|water|flare|star", name):
        return "streak/speedline", "orient=velocity+squash"
    # 3. dark underlay: dark colour, or very low brightness without additive light
    if (f["lum"] is not None and f["lum"] < 0.12 and f["light_emission"] < 0.5) or re.search(r"dark|shadow|black|underlay|twin|outline", name):
        if not re.search(r"slash|crescent|smoke", name):
            return "dark underlay/twin", "dark colour/name"
    if f["brightness"] < 0.6 and f["light_emission"] < 0.3 and f["lum"] is not None and f["lum"] < 0.35:
        return "dark underlay/twin", "brightness<0.6+dim"
    # 4. name keywords
    if re.search(r"^note|arrow|^other$", name):
        return "other", "name:note/arrow/other"
    for job, rx in NAME_RULES[1:]:
        if re.search(rx, name):
            if job == "ember/spec" and f["peak"] >= 8 and f["speed"] < 3:
                return "glow/halo", "name:spec+huge+static"
            if job == "ember/spec" and (f["drag"] > 3 or (f["speed"] > 25 and f["peak"] < 1.0 and f["lifetime"] < 1.0)):
                return "spark", "name:spec+drag/speed"
            if job == "ring/shockwave" and f["tex_shape"] in ("symbol", "rune", "grid-tile"):
                return "ground decal", "name:ring+rune tex"
            return job, "name:" + rx
    # 5. texture tags
    if f["tex_shape"] in SHAPE_JOB:
        job = SHAPE_JOB[f["tex_shape"]]
        if job == "ring/shockwave" and f["orient"] == 3 and f["speed"] < 1 and f["lifetime"] > 1.5:
            job = "ground decal"
        return job, "tex_shape:" + f["tex_shape"]
    if f["tex_shape"] in ("rune", "symbol") and f["orient"] in (1, 3):
        return "ground decal", "tex_shape:" + f["tex_shape"] + "+flat orient"
    if f["tex_group"] in GROUP_JOB:
        return GROUP_JOB[f["tex_group"]], "tex_group:" + f["tex_group"]
    # 6. ancestor context keywords
    for job, rx in NAME_RULES:
        if job in ("core", "glow/halo", "streak/speedline"):
            continue
        if re.search(rx, ctx):
            return job, "ctx:" + rx
    # 7. props only
    if f["drag"] > 3 and f["speed"] > 20 and f["peak"] < 1.0:
        return "spark", "props:drag>3+fast+small"
    if f["orient"] == 3 and f["speed"] < 1 and f["growth"] > 2:
        return "ring/shockwave", "props:flat+static+growing"
    if f["orient"] == 3:
        return "ground decal", "props:flat"
    if f["speed"] < 1 and f["growth"] > 2:
        return "glow/halo", "props:static+growing"
    if f["peak"] < 0.6 and f["lifetime"] < 1.5:
        return "ember/spec", "props:tiny"
    if f["fb"]:
        return "flipbook burst", "props:flipbook"
    if f["lifetime"] < 0.7 and f["speed"] < 3 and f["light_emission"] > 0.5:
        return "core", "props:short+static+additive"
    if f["speed"] < 3 and f["light_emission"] > 0.5:
        return "glow/halo", "props:static+additive"
    # low-confidence fallbacks (rule text starts with "props:fallback")
    if f["speed"] >= 3 and f["peak"] < 1.5:
        return "ember/spec", "props:fallback small+moving"
    if f["lifetime"] < 0.3 and f["speed"] < 3:
        return "glow/halo", "props:fallback flash"
    if f["speed"] < 3:
        return "core", "props:fallback static"
    return "other", "none"


# ----------------------------------------------------------------------------- flattening


def row_features(cls, name, props, ctx, cat):
    """Derive classification features from raw props."""
    f = {"name": name, "ctx": ctx}
    if cls != "ParticleEmitter":
        return f
    p = props
    tid = tex_id(p.get("Texture"))
    t = cat.get(tid) if tid is not None else None
    sz = seq_points(p.get("Size"))
    mx = max([v for _, v in sz], default=0.0)
    first = max(0.0, sz[0][1]) if sz else 0.0
    last = max(0.0, sz[-1][1]) if sz else 0.0
    cols = colour_points(p.get("Color"))
    lum = luminance(cols[0][1]) if cols else None
    if cols:
        lum = max(luminance(c) for _, c in cols)
    f.update({
        "orient": p.get("Orientation", 0),
        "squash": any(abs(k[1]) > 1e-6 for k in p.get("Squash", [])),
        "lum": lum,
        "light_emission": p.get("LightEmission", 0.0),
        "brightness": p.get("Brightness", 1.0),
        "drag": p.get("Drag", 0.0),
        "speed": max(abs(x) for x in p.get("Speed", [0, 0])),
        "peak": mx,
        "lifetime": mean_range(p.get("Lifetime")) or 0.0,
        "growth": (last / first) if first > 1e-6 else (10.0 if last > 0 else 1.0),
        "fb": p.get("FlipbookLayout", 0) > 0,
        "tex_shape": t["shape"] if t else None,
        "tex_group": t["group"] if t else None,
    })
    return f


def walk(node, path, out):
    path = path + [node["Name"]]
    out.append((node, path))
    for c in node.get("children", []):
        walk(c, path, out)


def flatten_effect(stem, cat):
    tier = TIER_OF[stem.split("__")[0]]
    with open(os.path.join(DUMPS, "json", stem + ".json"), encoding="utf-8") as fh:
        data = json.load(fh)
    attrs = parse_attrs(stem)
    used = Counter()
    nodes = []
    for r in data["roots"]:
        walk(r, [], nodes)
    rows = []
    for node, path in nodes:
        cls = node["ClassName"]
        if cls not in VFX_CLASSES:
            continue
        p = node.get("props", {})
        ppath = "/" + "/".join(path)
        key = (ppath, cls)
        a = {}
        if cls == "ParticleEmitter" and attrs.get(key):
            i = used[key]
            lst = attrs[key]
            a = lst[min(i, len(lst) - 1)] if i < len(lst) else lst[-1]
            used[key] += 1
        ctx = " ".join(path[-4:-1])
        feat = row_features(cls, node["Name"], p, ctx, cat)
        row = {"effect": stem, "tier": tier, "path": ppath, "class": cls, "name": node["Name"], "depth": len(path)}
        if cls == "ParticleEmitter":
            tid = tex_id(p.get("Texture"))
            t = cat.get(tid) if tid is not None else None
            job, rule = classify(feat)
            row.update({
                "job": job, "job_rule": rule,
                "enabled": p.get("Enabled"), "rate": p.get("Rate"),
                "lifetime": p.get("Lifetime"), "speed": p.get("Speed"), "drag": p.get("Drag"),
                "accel": p.get("Acceleration"), "brightness": p.get("Brightness"),
                "light_emission": p.get("LightEmission"), "light_influence": p.get("LightInfluence"),
                "z_offset": p.get("ZOffset"), "spread": p.get("SpreadAngle"),
                "rot": p.get("Rotation"), "rot_speed": p.get("RotSpeed"),
                "orientation": p.get("Orientation"), "locked_to_part": p.get("LockedToPart"),
                "time_scale": p.get("TimeScale"), "velocity_inheritance": p.get("VelocityInheritance"),
                "flipbook_layout": p.get("FlipbookLayout"), "flipbook_mode": p.get("FlipbookMode"),
                "flipbook_fps": p.get("FlipbookFramerate"),
                "size": p.get("Size"), "transparency": p.get("Transparency"), "squash": p.get("Squash"),
                "color": p.get("Color"), "texture": p.get("Texture"),
                "tex_id": tid,
                "tex_tags": ({k: t[k] for k in ("group", "style", "shape", "quality")} if t else None),
                "emit_count": num(a.get("EmitCount")), "emit_delay": num(a.get("EmitDelay")),
                "emit_duration": num(a.get("EmitDuration")),
                "attrs": a,
                "peak_size": peak_size(p.get("Size")),
                "size_negative": any(k[1] < 0 for k in p.get("Size", [])),
                "squash_used": feat["squash"],
                "colour_changes": colour_changes(p.get("Color")),
            })
            row["sig"] = json.dumps([row["name"].lower(), row["texture"], row["lifetime"], row["speed"], row["drag"],
                                     row["accel"], row["size"], row["transparency"], row["brightness"],
                                     row["light_emission"], row["orientation"], row["rate"], row["emit_count"],
                                     row["emit_delay"]], sort_keys=True)
        elif cls == "Beam":
            row.update({k: p.get(k) for k in (
                "Enabled", "Brightness", "LightEmission", "LightInfluence", "Width0", "Width1", "CurveSize0",
                "CurveSize1", "Segments", "TextureLength", "TextureMode", "TextureSpeed", "FaceCamera",
                "ZOffset", "Texture", "Transparency", "Color")})
            row["job"] = "beam"
        elif cls == "Trail":
            row.update({k: p.get(k) for k in (
                "Enabled", "Brightness", "LightEmission", "LightInfluence", "Lifetime", "MinLength", "MaxLength",
                "FaceCamera", "TextureLength", "TextureMode", "Texture", "Transparency", "WidthScale", "Color")})
            row["job"] = "trail"
        else:
            row.update({k: p.get(k) for k in ("Enabled", "Brightness", "Color", "Range", "Angle", "Shadows", "Face")})
            row["job"] = "light"
        rows.append(row)
    seen = set()
    for row in rows:  # dup = same recipe (colour and path ignored) already present in this effect
        if "sig" in row:
            row["dup"] = row["sig"] in seen
            seen.add(row["sig"])
            del row["sig"]
    return rows


def all_rows():
    cat = load_catalog()
    rows = []
    for stem in study_files():
        rows.extend(flatten_effect(stem, cat))
    return rows


def write_rows(rows, path=ROWS_PATH):
    with open(path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_rows(path=ROWS_PATH):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


# ----------------------------------------------------------------------------- per-job stats


def accel_y(r):
    a = r.get("accel")
    return a[1] if a else None


def job_stats(rows):
    """rows: emitter rows of ONE job -> dict of statistics."""
    em = rows
    s = {"n": len(em), "n_eff": len({r["effect"] for r in em})}
    s["lifetime"] = summarize([mean_range(r["lifetime"]) for r in em])
    s["speed"] = summarize([mean_range(r["speed"]) for r in em])
    s["drag"] = summarize([r["drag"] for r in em])
    s["accel_y"] = summarize([accel_y(r) for r in em])
    s["brightness"] = summarize([r["brightness"] for r in em])
    s["light_emission"] = summarize([r["light_emission"] for r in em])
    s["light_influence"] = summarize([r["light_influence"] for r in em])
    s["z_offset"] = summarize([r["z_offset"] for r in em])
    s["emit_count"] = summarize([r["emit_count"] for r in em if r["emit_count"] is None or r["emit_count"] < 500])
    s["rate"] = summarize([r["rate"] for r in em if r["enabled"] and r["rate"] and r["rate"] > 0])
    s["sh_continuous"] = share(em, lambda r: r["enabled"] and r["rate"] and r["rate"] > 0)
    s["sh_has_count"] = share(em, lambda r: r["emit_count"])
    s["sh_delay"] = share([r for r in em if r["emit_count"]], lambda r: (r["emit_delay"] or 0) > 0)
    s["size_classes"] = Counter(c for c in (size_class(r["size"]) for r in em) if c)
    s["transp_classes"] = Counter(c for c in (transp_class(r["transparency"]) for r in em) if c)
    s["spread"] = summarize([max(r["spread"]) if r["spread"] else None for r in em])
    s["rot_speed"] = summarize([max(abs(x) for x in r["rot_speed"]) if r["rot_speed"] else None for r in em])
    s["peak_size"] = summarize([r["peak_size"] for r in em])
    s["sh_squash"] = share(em, lambda r: r["squash_used"])
    s["sh_flat"] = share(em, lambda r: r["orientation"] == 3)
    s["sh_locked"] = share(em, lambda r: r["locked_to_part"])
    s["sh_flipbook"] = share(em, lambda r: (r["flipbook_layout"] or 0) > 0)
    s["sh_colour"] = share(em, lambda r: r["colour_changes"])
    s["sh_enabled"] = share(em, lambda r: r["enabled"])
    s["size_curve"] = median_curve([size_shape(r["size"]) for r in em])
    s["transp_curve"] = median_curve([value_shape(r["transparency"]) for r in em])
    return s


# ----------------------------------------------------------------------------- per-effect stats


def effect_peak_live(rows):
    """Estimate peak live particles: bursts at EmitDelay live ~mean lifetime; Enabled+Rate emitters add Rate*life."""
    events = []
    for r in rows:
        if r["class"] != "ParticleEmitter":
            continue
        life = mean_range(r["lifetime"]) or 0.0
        if r["emit_count"] and r["emit_count"] > 0:
            d = r["emit_delay"] or 0.0
            events.append((d, d + life, r["emit_count"]))
        if r["enabled"] and r["rate"] and r["rate"] > 0:
            events.append((0.0, life, r["rate"] * life))
    if not events:
        return 0.0
    ts = sorted({e[0] for e in events} | {e[1] for e in events})
    best = 0.0
    for t in ts:
        live = sum(n for a, b, n in events if a <= t < b or (a == t))
        best = max(best, live)
    return best


def effect_timeline(rows):
    """{job: first fire (s)} using EmitDelay for burst emitters; enabled continuous emitters fire at 0."""
    tl = {}
    for r in rows:
        if r["class"] != "ParticleEmitter":
            continue
        if r["emit_count"] and r["emit_count"] > 0:
            d = r["emit_delay"] or 0.0
        elif r["enabled"] and r["rate"] and r["rate"] > 0:
            d = 0.0
        else:
            continue
        j = r["job"]
        tl[j] = min(tl.get(j, 9e9), d)
    return tl


def effect_stats(rows):
    em = [r for r in rows if r["class"] == "ParticleEmitter"]
    texs = {r["tex_id"] for r in em if r["tex_id"]}
    return {
        "emitters": len(em),
        "unique_tex": len(texs),
        "emit_per_tex": (len(em) / len(texs)) if texs else None,
        "peak_live": effect_peak_live(rows),
        "beams": sum(1 for r in rows if r["class"] == "Beam"),
        "trails": sum(1 for r in rows if r["class"] == "Trail"),
        "lights": sum(1 for r in rows if r["class"] in ("PointLight", "SpotLight", "SurfaceLight")),
        "timeline": effect_timeline(rows),
    }


# ----------------------------------------------------------------------------- effect type / units

TYPE_RULES = [
    ("slash", r"slash|swing|sword|swipe|crescent|blade"),
    ("beam", r"beam|laser"),
    ("projectile", r"projectile|bullet|missile|arrow|fireball|\bball\b|shot|orb|barrage|meteor|travel|comet|bolt"),
    ("impact/explosion", r"impact|hit|explo|blast|smack|punch|land|crash|boom|collision|slam|shatter"),
    ("aura/loop", r"aura|idle|loop|charge|buff|shield|ambient|constant|fireflies|orbit"),
    ("burst/one-shot", r"burst|cast|spawn|death|goal|pop|reveal|activate|summon|ult|special"),
]


def unit_type(path_names, rows_in_unit):
    """Return effect-type for a unit. Keyword on the unit's path first, else structure."""
    txt = " ".join(path_names).lower()
    for t, rx in TYPE_RULES:
        if re.search(rx, txt):
            return t, "kw:" + t
    em = [r for r in rows_in_unit if r["class"] == "ParticleEmitter"]
    burst = sum(1 for r in em if r["emit_count"])
    cont = sum(1 for r in em if r["enabled"] and r["rate"] and r["rate"] > 0 and not r["emit_count"])
    if em and cont > burst:
        return "aura/loop", "structure:continuous"
    return "burst/one-shot", "structure:burst"


def unit_key(path):
    """Group key: the first ancestor beneath the root whose name carries a type keyword, else the parent."""
    parts = path.strip("/").split("/")
    for i in range(len(parts) - 1):
        if any(re.search(rx, parts[i].lower()) for _, rx in TYPE_RULES):
            return "/" + "/".join(parts[: i + 1]), parts[: i + 1]
    return "/" + "/".join(parts[:-1]), parts[:-1]


def units(rows):
    """Group emitter rows into units; returns {(effect, key): (names, rows)}."""
    g = {}
    for r in rows:
        if r["class"] != "ParticleEmitter":
            continue
        k, names = unit_key(r["path"])
        g.setdefault((r["effect"], k), (names, []))[1].append(r)
    return g


def unit_recipe(urows):
    """Job -> (first fire s rel. to unit start, total EmitCount, emitters, median lifetime s, median ZOffset)."""
    first = {}
    cnt = Counter()
    ne = Counter()
    life = defaultdict(list)
    zs = defaultdict(list)
    for r in urows:
        if r["emit_count"] and r["emit_count"] > 0:
            d = r["emit_delay"] or 0.0
        elif r["enabled"] and r["rate"] and r["rate"] > 0:
            d = 0.0
        else:
            continue
        j = r["job"]
        first[j] = min(first.get(j, 9e9), d)
        cnt[j] += (r["emit_count"] or 0) if (r["emit_count"] or 0) < 500 else 0
        ne[j] += 1
        life[j].append(mean_range(r["lifetime"]) or 0.0)
        zs[j].append(r["z_offset"] or 0.0)
    if not first:
        return {}
    t0 = min(first.values())
    return {j: (first[j] - t0, cnt[j], ne[j], statistics.median(life[j]), statistics.median(zs[j])) for j in first}


# ----------------------------------------------------------------------------- markdown


def f2(x, nd=2):
    if x is None:
        return "-"
    if abs(x) >= 100:
        return "%d" % round(x)
    if abs(x) >= 10:
        return ("%." + str(max(nd - 1, 0)) + "f") % x
    return ("%." + str(nd) + "f") % x


def stat_cell(s, nd=2):
    if s["n"] == 0:
        return "-"
    return "%s (%s-%s)" % (f2(s["med"], nd), f2(s["p10"], nd), f2(s["p90"], nd))


def pc(x):
    return "-" if x is None else "%d%%" % round(100 * x)


def curve_cell(c):
    return "-" if not c else "/".join("%.2f" % v for v in c)[:80].replace("0.", ".").replace("1.00", "1")


def report(rows):
    em_all = [r for r in rows if r["class"] == "ParticleEmitter"]
    em = [r for r in em_all if not r.get("dup")]  # distinct recipes: all statistics use these
    n_all_job = Counter(r["job"] for r in em_all)
    by_job = defaultdict(list)
    for r in em:
        by_job[r["job"]].append(r)
    order = sorted(by_job, key=lambda j: -len(by_job[j]))
    L = []
    L.append("## GEN1 job counts")
    L.append("| job | n distinct | n rows | n_eff | S | A | B | C | U |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for j in order:
        t = Counter(r["tier"] for r in by_job[j])
        L.append("| %s | %d | %d | %d | %d | %d | %d | %d | %d |" % (j, len(by_job[j]), n_all_job[j], len({r['effect'] for r in by_job[j]}), t["S"], t["A"], t["B"], t["C"], t["U"]))
    L.append("")
    L.append("## GEN2 job value table: median (p10-p90)")
    L.append("| job | n | Lifetime s | Speed | Drag | Accel.Y | Brightness | LightEm | LightInfl | ZOffset | EmitCount | Rate | Spread | RotSpeed | peak size |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    stats = {j: job_stats(by_job[j]) for j in order}
    for j in order:
        s = stats[j]
        L.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            j, s["n"], stat_cell(s["lifetime"]), stat_cell(s["speed"], 1), stat_cell(s["drag"], 1),
            stat_cell(s["accel_y"], 1), stat_cell(s["brightness"], 1), stat_cell(s["light_emission"]),
            stat_cell(s["light_influence"]), stat_cell(s["z_offset"], 1), stat_cell(s["emit_count"], 0),
            stat_cell(s["rate"], 0), stat_cell(s["spread"], 0), stat_cell(s["rot_speed"], 0), stat_cell(s["peak_size"], 1)))
    L.append("")
    L.append("## GEN3 shares and curves")
    L.append("| job | n | squash | vel-parallel(2) | flat(3) | locked | flipbook | colour change | enabled | size@0/.05/.1/.25/.5/.75/1 (frac of max) | transp@same t |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for j in order:
        s = stats[j]
        vel = share(by_job[j], lambda r: r["orientation"] == 2)
        L.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            j, s["n"], pc(s["sh_squash"]), pc(vel), pc(s["sh_flat"]), pc(s["sh_locked"]), pc(s["sh_flipbook"]),
            pc(s["sh_colour"]), pc(s["sh_enabled"]), curve_cell(s["size_curve"]), curve_cell(s["transp_curve"])))
    L.append("")
    # S+A vs B+C splits
    L.append("## GEN3b curve classes (share of distinct emitters) and continuous/burst")
    L.append("| job | n | size grow | shrink | bump | flat | other | transp fade-out | fade-in-out | opaque | faint | partial | continuous(enabled+Rate) | has EmitCount | burst delayed>0 |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for j in order:
        s_ = stats[j]
        sc, tc = s_["size_classes"], s_["transp_classes"]
        ns, nt = sum(sc.values()) or 1, sum(tc.values()) or 1
        L.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            j, s_["n"], pc(sc["grow"] / ns), pc(sc["shrink"] / ns), pc(sc["bump"] / ns), pc(sc["flat"] / ns),
            pc(sc["other"] / ns), pc(tc["fade-out"] / nt), pc(tc["fade-in-out"] / nt), pc(tc["opaque"] / nt),
            pc(tc["faint"] / nt), pc((tc["partial"] + tc["fade-in"]) / nt), pc(s_["sh_continuous"]),
            pc(s_["sh_has_count"]), pc(s_["sh_delay"])))
    L.append("")
    L.append("## GEN3c colour (start colour = first keypoint)")
    L.append("| job | n | white-ish start (min ch>=200) | saturated start (max-min>=100) | dark start (lum<0.15) | end darker than start (lum x0.7) | median start lum |")
    L.append("|---|---|---|---|---|---|---|")
    for j in order:
        cs = [colour_points(r["color"]) for r in by_job[j] if r["color"]]
        cs = [c for c in cs if c]
        if not cs:
            continue
        st0 = [c[0][1] for c in cs]
        en0 = [c[-1][1] for c in cs]
        L.append("| %s | %d | %s | %s | %s | %s | %s |" % (
            j, len(cs), pc(sum(1 for c in st0 if min(c) >= 200) / len(cs)),
            pc(sum(1 for c in st0 if max(c) - min(c) >= 100) / len(cs)),
            pc(sum(1 for c in st0 if luminance(c) < 0.15) / len(cs)),
            pc(sum(1 for a_, b_ in zip(st0, en0) if luminance(b_) < 0.7 * luminance(a_)) / len(cs)),
            f2(pctl([luminance(c) for c in st0], 50))))
    L.append("")
    L.append("## GEN4 tier split (S+A vs B+C): median Lifetime / Speed / Brightness / LightEm / EmitCount / peak size")
    L.append("| job | n SA | n BC | Lifetime SA/BC | Speed SA/BC | Bright SA/BC | LightEm SA/BC | EmitCount SA/BC | peak SA/BC |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for j in order:
        sa = [r for r in by_job[j] if r["tier"] in "SA"]
        bc = [r for r in by_job[j] if r["tier"] in "BC"]
        if len(sa) < 5 or len(bc) < 5:
            continue
        a, b = job_stats(sa), job_stats(bc)

        def pair(k, nd=2):
            return "%s / %s" % (f2(a[k]["med"], nd), f2(b[k]["med"], nd))
        L.append("| %s | %d | %d | %s | %s | %s | %s | %s | %s |" % (
            j, len(sa), len(bc), pair("lifetime"), pair("speed", 1), pair("brightness", 1), pair("light_emission"),
            pair("emit_count", 0), pair("peak_size", 1)))
    L.append("")
    # per effect
    L.append("## GEN5 per effect")
    L.append("| effect | tier | emit | uniq tex | emit/tex | peak live | beam | trail | light | first-fire timeline |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for stem in study_files():
        er = [r for r in rows if r["effect"] == stem]
        e = effect_stats(er)
        tl = sorted(e["timeline"].items(), key=lambda kv: kv[1])
        zero = [j.split("/")[0] for j, t in tl if t <= 0.0005]
        short = ["0ms:" + ",".join(zero)] if zero else []
        for j, t in tl:
            if t > 0.0005:
                short.append("%s@%dms" % (j.split("/")[0], round(t * 1000)))
        L.append("| %s | %s | %d | %d | %s | %d | %d | %d | %d | %s |" % (
            stem.split("__")[1], TIER_OF[stem.split("__")[0]], e["emitters"], e["unique_tex"], f2(e["emit_per_tex"], 1),
            e["peak_live"], e["beams"], e["trails"], e["lights"], " ".join(short)))
    L.append("")
    # per type recipes
    g = units([r for r in rows if not r.get("dup")])
    typed = defaultdict(list)
    for (eff, key), (names, urows) in g.items():
        if len(urows) < 2:
            continue
        t, why = unit_type(names, urows)
        typed[t].append((eff, key, urows))
    L.append("## GEN6 per effect type (units with >=2 distinct emitters; time = ms after the unit first fire)")
    for t in sorted(typed, key=lambda t: -len(typed[t])):
        us = typed[t]
        recs = [unit_recipe(u[2]) for u in us]
        recs = [r for r in recs if r]
        L.append("")
        L.append("### %s: %d units, %d effects, median %d emitters/unit" % (
            t, len(us), len({u[0] for u in us}), statistics.median(len(u[2]) for u in us)))
        L.append("| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        jobs = Counter(j for r in recs for j in r)
        for j, nj in sorted(jobs.items(), key=lambda kv: (statistics.median(r[kv[0]][0] for r in recs if kv[0] in r), -kv[1])):
            ts = [r[j][0] * 1000 for r in recs if j in r]
            cs = [r[j][1] for r in recs if j in r]
            ns = [r[j][2] for r in recs if j in r]
            lf = [r[j][3] * 1000 for r in recs if j in r]
            zz = [r[j][4] for r in recs if j in r]
            if nj < max(2, 0.15 * len(recs)):
                continue
            L.append("| %s | %d | %s | %s (%s-%s) | %s | %s | %s | %s | %s |" % (
                j, nj, pc(nj / len(recs)), f2(pctl(ts, 50), 0), f2(pctl(ts, 10), 0), f2(pctl(ts, 90), 0),
                pc(sum(1 for t_ in ts if t_ > 0.5) / len(ts)), f2(pctl(lf, 50), 0), f2(pctl(zz, 50), 1),
                f2(pctl(cs, 50), 0), f2(pctl(ns, 50), 0)))
    L.append("")
    L.append("## GEN7 beams / trails / lights (raw rows, not deduped)")
    for cls, keys in (("Beam", ("Width0", "Width1", "Brightness", "LightEmission", "LightInfluence", "Segments", "CurveSize0", "CurveSize1", "TextureLength", "TextureSpeed", "ZOffset")),
                      ("Trail", ("Lifetime", "Brightness", "LightEmission", "LightInfluence", "MinLength")),
                      ("PointLight", ("Brightness", "Range")), ("SpotLight", ("Brightness", "Range", "Angle"))):
        rr = [r for r in rows if r["class"] == cls]
        if not rr:
            continue
        L.append("")
        L.append("### %s n=%d in %d effects (S+A %d, B+C %d)" % (cls, len(rr), len({r['effect'] for r in rr}),
                 sum(1 for r in rr if r['tier'] in 'SA'), sum(1 for r in rr if r['tier'] in 'BC')))
        L.append("| prop | n | median (p10-p90) |")
        L.append("|---|---|---|")
        for k in keys:
            sm = summarize([r.get(k) for r in rr if isinstance(r.get(k), (int, float))])
            L.append("| %s | %d | %s |" % (k, sm["n"], stat_cell(sm)))
        if cls in ("Beam", "Trail"):
            L.append("| FaceCamera true | %d | %s |" % (len(rr), pc(share(rr, lambda r: r.get("FaceCamera")))))
        L.append("| Enabled | %d | %s |" % (len(rr), pc(share(rr, lambda r: r.get("Enabled")))))
    return "\n".join(L)


def main(argv):
    if len(argv) < 2 or argv[1] not in ("rows", "report"):
        print(__doc__)
        return 1
    if argv[1] == "rows":
        rows = all_rows()
        write_rows(rows)
        em = [r for r in rows if r["class"] == "ParticleEmitter"]
        c = Counter(r["job"] for r in em)
        print("rows", len(rows), "emitters", len(em), "other", c["other"], "%.1f%%" % (100.0 * c["other"] / len(em)))
        return 0
    rows = read_rows()
    out = report(rows)
    with open(argv[2], "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote", argv[2])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
