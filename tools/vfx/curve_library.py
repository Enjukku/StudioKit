#!/usr/bin/env python3
"""Build the VFX CURVE LIBRARY from the S+A tier study emitters.

  python tools/vfx/curve_library.py    # writes content/vfx/curves.json and
                                       # knowledge/reference/vfx/training/curve-library.md

Input: output/vfx/training-dumps/emitters_study.jsonl (study set only; hidden effects already excluded).
Library = S+A rows only (ParticleEmitter dup=false, Beam, Trail). B+C appear only in the pop check.
Each curve kind is clustered with k-medoids on 41 resampled points + 7 log-time points; the library
keeps the MEDOID (a real curve, original keypoints) per cluster, never an average.
"""
from __future__ import annotations

import colorsys
import json
import math
import os
import statistics
from collections import Counter, defaultdict

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ROWS = os.path.join(ROOT, "output", "vfx", "training-dumps", "emitters_study.jsonl")
OUT_JSON = os.path.join(ROOT, "content", "vfx", "curves.json")
OUT_MD = os.path.join(ROOT, "knowledge", "reference", "vfx", "training", "curve-library.md")

N_LIN = 41
LOG_T = (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0)
LOG_W = 1.5
SPARK_T = (0.0, 0.01, 0.03, 0.06, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0)
BLOCKS = "▁▂▃▄▅▆▇█"
MAX_KEYS = 20

# ----------------------------------------------------------------------------- curve maths


def clean_keys(keys, vmin=None, vmax=None):
    """Roblox-valid NumberSequence keypoints [[t, v, env], ...]: sorted, unique t, starts 0, ends 1, <=20."""
    pts = {}
    for k in keys:
        t = min(1.0, max(0.0, float(k[0])))
        env = float(k[2]) if len(k) > 2 else 0.0
        pts[round(t, 6)] = [t, float(k[1]), abs(env)]  # same t: last wins
    out = [pts[t] for t in sorted(pts)]
    if not out:
        return []
    if out[0][0] > 0:
        out.insert(0, [0.0, out[0][1], out[0][2]])
    if out[-1][0] < 1:
        out.append([1.0, out[-1][1], out[-1][2]])
    while len(out) > MAX_KEYS:  # drop the interior point whose removal changes the curve least
        best, bi = None, None
        for i in range(1, len(out) - 1):
            a, b, c = out[i - 1], out[i], out[i + 1]
            f = (b[0] - a[0]) / (c[0] - a[0])
            err = abs(a[1] + (c[1] - a[1]) * f - b[1])
            if best is None or err < best:
                best, bi = err, i
        out.pop(bi)
    for p in out:
        if vmin is not None:
            p[1] = max(vmin, p[1])
        if vmax is not None:
            p[1] = min(vmax, p[1])
    return out


def at(keys, t):
    """Linear NumberSequence evaluation (keys sorted, [t, v, ...])."""
    if t <= keys[0][0]:
        return keys[0][1]
    if t >= keys[-1][0]:
        return keys[-1][1]
    for a, b in zip(keys, keys[1:]):
        if a[0] <= t <= b[0]:
            return b[1] if b[0] == a[0] else a[1] + (b[1] - a[1]) * (t - a[0]) / (b[0] - a[0])
    return keys[-1][1]


def resample(keys, n=N_LIN):
    return [at(keys, i / (n - 1)) for i in range(n)]


def normalise(keys):
    """Divide values by max|v|. Returns (keys', peak). Peak 0 -> unchanged."""
    peak = max((abs(k[1]) for k in keys), default=0.0)
    if peak <= 1e-12:
        return [list(k) for k in keys], 0.0
    return [[k[0], k[1] / peak, k[2] / peak] for k in keys], peak


def features(keys):
    return np.array(resample(keys) + [LOG_W * at(keys, t) for t in LOG_T])


def dist_matrix(X):
    d = X[:, None, :] - X[None, :, :]
    return np.sqrt((d * d).sum(-1))


def kmedoids(D, k, restarts=25, seed=7):
    """PAM-style alternating k-medoids with k-medoids++ init. Returns (medoid_idx list, labels)."""
    n = len(D)
    rng = np.random.default_rng(seed)
    k = max(1, min(k, n))
    best = None
    for _ in range(restarts):
        med = [int(rng.integers(n))]
        while len(med) < k:
            dmin = D[:, med].min(1) ** 2
            if dmin.sum() <= 0:
                rest = [i for i in range(n) if i not in med]
                med.append(rest[int(rng.integers(len(rest)))])
            else:
                med.append(int(rng.choice(n, p=dmin / dmin.sum())))
        for _ in range(50):
            lab = D[:, med].argmin(1)
            new = []
            for c in range(k):
                idx = np.where(lab == c)[0]
                if len(idx) == 0:
                    new.append(med[c])
                    continue
                new.append(int(idx[D[np.ix_(idx, idx)].sum(1).argmin()]))
            if new == med:
                break
            med = new
        lab = D[:, med].argmin(1)
        cost = float(D[np.arange(n), [med[l] for l in lab]].sum())
        if best is None or cost < best[0]:
            best = (cost, list(med), lab)
    return best[1], best[2]


def silhouette(D, lab):
    n = len(D)
    ks = sorted(set(lab.tolist()))
    if len(ks) < 2:
        return 0.0
    s = []
    for i in range(n):
        own = lab == lab[i]
        if own.sum() <= 1:
            s.append(0.0)
            continue
        a = D[i, own].sum() / (own.sum() - 1)
        b = min(D[i, lab == c].mean() for c in ks if c != lab[i])
        s.append((b - a) / max(a, b, 1e-12))
    return float(np.mean(s))


def pick_k(D, kmin, kmax):
    best = None
    for k in range(kmin, min(kmax, len(D) - 1) + 1):
        _, lab = kmedoids(D, k, restarts=10)
        sc = silhouette(D, lab)
        if best is None or sc > best[0]:
            best = (sc, k)
    return best[1], best[0]


def spark(keys, lo=0.0, hi=1.0):
    out = ""
    for t in SPARK_T:
        v = (at(keys, t) - lo) / (hi - lo) if hi > lo else 0.0
        out += BLOCKS[max(0, min(7, int(round(v * 7))))]
    return out


# ----------------------------------------------------------------------------- naming


def _extrema(v, eps=0.08):
    """Count direction changes larger than eps in a resampled curve."""
    n, last, d = 0, v[0], 0
    for x in v[1:]:
        if abs(x - last) > eps:
            s = 1 if x > last else -1
            if d and s != d:
                n += 1
            d = s
            last = x
    return n


def name_size(keys):
    """keys normalised (value/max). Name by shape."""
    v = resample(keys, 101)
    s0, s02, s25, s5, e = at(keys, 0), at(keys, 0.02), at(keys, 0.25), at(keys, 0.5), v[-1]
    mx = max(range(101), key=lambda i: v[i]) / 100.0
    if min(v) >= 0.8:
        return "constant size"
    if _extrema(v, 0.15) >= 3:
        return "pulse (size wobble)"
    if s0 < 0.3 and s02 >= 0.6:
        return "impact pop, hold" if e >= 0.8 else ("impact pop then shrink" if e < 0.45 else "impact pop, partial shrink")
    if s0 >= 0.6 and e >= 0.8:
        return "constant size" if e - s0 < 0.15 else "start 60%, grow to full"
    if s0 < 0.55 and e >= 0.8:
        if s0 >= 0.25:
            return f"grow from {round(s0 * 100)}%"
        if s25 >= 0.65:
            return "ease-out grow"
        if s5 < 0.3:
            return "late grow (ease-in)"
        return "S-curve grow" if (s25 < 0.55 and at(keys, 0.75) > 0.93) else "linear grow"
    if s0 >= 0.7 and e <= 0.35:
        if s5 >= 0.8:
            return "hold then shrink"
        if s25 < 0.45:
            return "fast shrink (ease-out)"
        return "linear shrink"
    if 0.03 < mx < 0.97 and max(s0, e) < 0.8:
        pos = "early" if mx < 0.3 else ("mid" if mx < 0.65 else "late")
        return f"bump ({pos} peak)"
    if s0 >= 0.7:
        return "start big, partial shrink"
    return "partial grow"


def name_signed(keys):
    v = resample(keys, 101)
    if max(abs(x) for x in v) < 0.05:
        return "zero"
    if _extrema(v, 0.2) >= 2:
        return "pulse"
    s0, e = v[0], v[-1]
    mi = max(range(101), key=lambda i: abs(v[i]))
    if abs(s0 - e) < 0.2 and min(abs(x) for x in v) > 0.7:
        return "constant"
    if abs(v[mi]) > max(abs(s0), abs(e)) + 0.25:
        return "bump"
    return "ramp up" if abs(e) > abs(s0) else "ramp down"


def name_transp(keys):
    v = resample(keys, 101)
    a, b, lo, hi = v[0], v[-1], min(v), max(v)
    if _extrema(v, 0.2) >= 3:
        return "twinkle bumps"
    if lo > 0.7:
        return "faint (barely visible)"
    if hi < 0.3 and abs(a - b) < 0.3:
        return "opaque hold"
    if a > 0.5 and b > 0.5 and lo < 0.4:
        wide = sum(1 for x in v if x < 0.5) / 101.0
        return "V glow (sharp peak)" if wide < 0.2 else ("fade in, hold, fade out" if wide < 0.8 else "V glow (fade in, fade out)")
    if a > 0.5 and b <= 0.5:
        return "fade in"
    if b > 0.5 and a <= 0.5:
        tc = next(i for i in range(101) if v[i] > 0.5) / 100.0
        if a >= 0.1:
            return "fade from translucent"
        if tc >= 0.6:
            return "late fade"
        if tc <= 0.3:
            return "early fade"
        return "linear fade"
    if hi - lo < 0.25:
        return "steady translucent"
    if abs(a - b) < 0.1:
        return "shallow V (translucent dip)"
    if b > a:
        return "translucent start, fade out" if a < 0.5 else "partial fade out"
    return "partial fade in"


def name_width(keys):
    a, b = keys[0][1], keys[-1][1]
    if abs(a - b) < 0.15 * max(a, b, 1e-9):
        return "constant width"
    return "taper to thin" if b < a else "widen"


def unique(names):
    seen, out = Counter(), []
    for n in names:
        seen[n] += 1
        out.append(n if seen[n] == 1 else f"{n} #{seen[n]}")
    return out


# ----------------------------------------------------------------------------- colour


def lum(c):
    return (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255.0


def hsv(c):
    return colorsys.rgb_to_hsv(c[0] / 255, c[1] / 255, c[2] / 255)


def colour_pattern(keys):
    cols = [k[1] for k in keys]
    f, l = cols[0], cols[-1]
    rgbd = max(math.dist(c, f) for c in cols)
    if rgbd < 15:
        return "constant colour"
    fh, fs, _ = hsv(f)
    lh, ls, _ = hsv(l)
    dh = min(abs(fh - lh), 1 - abs(fh - lh)) * 360
    lf, ll = lum(f), lum(l)
    if lf > 0.8 and fs < 0.4 and ls > fs + 0.3:
        return "white core to colour"
    if math.dist(f, l) < 40:
        return "cycle (returns to start colour)"
    if ll < 0.2 and lf - ll > 0.25:
        return "body to dark"
    if dh >= 40 and fs > 0.2 and ls > 0.2:
        return "hue shift"
    if lf - ll > 0.15:
        return "hot to body (same hue, darker)"
    if ll - lf > 0.2:
        return "tint toward white/bright"
    return "subtle drift"


def colour_vec(keys):
    out = []
    for i in range(11):
        t = i / 10
        if t <= keys[0][0]:
            c = keys[0][1]
        elif t >= keys[-1][0]:
            c = keys[-1][1]
        else:
            c = keys[-1][1]
            for a, b in zip(keys, keys[1:]):
                if a[0] <= t <= b[0]:
                    f = 0 if b[0] == a[0] else (t - a[0]) / (b[0] - a[0])
                    c = [a[1][j] + (b[1][j] - a[1][j]) * f for j in range(3)]
                    break
        out += list(c)
    return np.array(out)


def clean_colour(seq):
    pts = {}
    for t, c in seq:
        t = min(1.0, max(0.0, float(t)))
        pts[round(t, 6)] = [t, [int(round(x)) for x in c]]
    out = [pts[t] for t in sorted(pts)]
    if out[0][0] > 0:
        out.insert(0, [0.0, out[0][1]])
    if out[-1][0] < 1:
        out.append([1.0, out[-1][1]])
    while len(out) > MAX_KEYS:
        out.pop(len(out) // 2)
    return out


# ----------------------------------------------------------------------------- build


def med(vals):
    v = [x for x in vals if x is not None]
    return round(statistics.median(v), 4) if v else None


def mean_life(r):
    lt = r.get("lifetime")
    if isinstance(lt, (list, tuple)) and lt:
        return sum(lt) / len(lt)
    if isinstance(lt, (int, float)):
        return float(lt)
    lf = r.get("Lifetime")
    return float(lf) if lf is not None else None


def load_rows(path=ROWS):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def collect(rows):
    """Return {kind: [item]}; item = dict(keys, job, effect, path, life, peak, rid)."""
    kinds = defaultdict(list)
    for i, r in enumerate(rows):
        if r["tier"] not in ("S", "A"):
            continue
        base = {"job": r.get("job", "?"), "effect": r["effect"], "path": r["path"], "life": mean_life(r), "rid": i}
        if r["class"] == "ParticleEmitter" and not r.get("dup"):
            sz = clean_keys(r["size"], 0.0)
            if sz and max(k[1] for k in sz) > 0:
                kinds["size"].append(dict(base, keys=sz, peak=max(k[1] for k in sz)))
            kinds["transparency"].append(dict(base, keys=clean_keys(r["transparency"], 0.0, 1.0), peak=None))
            if r.get("squash_used"):
                sq = clean_keys(r["squash"])
                if sq and max(abs(k[1]) for k in sq) > 0:
                    kinds["squash"].append(dict(base, keys=sq, peak=max(abs(k[1]) for k in sq)))
            if r.get("color"):
                kinds["color"].append(dict(base, keys=clean_colour(r["color"]), peak=None))
        elif r["class"] == "Beam":
            kinds["beam_transparency"].append(dict(base, keys=clean_keys(r["Transparency"], 0.0, 1.0), peak=None, job="beam"))
            w0, w1 = float(r["Width0"]), float(r["Width1"])
            if max(w0, w1) > 0:
                kinds["beam_width"].append(dict(base, keys=clean_keys([[0, w0, 0], [1, w1, 0]], 0.0), peak=max(w0, w1), job="beam"))
            if r.get("Color"):
                kinds["color"].append(dict(base, keys=clean_colour(r["Color"]), peak=None, job="beam"))
        elif r["class"] == "Trail":
            kinds["trail_transparency"].append(dict(base, keys=clean_keys(r["Transparency"], 0.0, 1.0), peak=None, job="trail"))
            if r.get("WidthScale"):
                ws = clean_keys(r["WidthScale"], 0.0)
                if max(k[1] for k in ws) > 0:
                    kinds["trail_widthscale"].append(dict(base, keys=ws, peak=max(k[1] for k in ws), job="trail"))
            if r.get("Color"):
                kinds["color"].append(dict(base, keys=clean_colour(r["Color"]), peak=None, job="trail"))
    return kinds


K_RANGE = {"size": (9, 12), "transparency": (9, 12), "squash": (3, 5), "beam_transparency": (3, 4),
           "beam_width": (2, 3), "trail_transparency": (2, 4), "trail_widthscale": (2, 3)}
NAMER = {"size": name_size, "transparency": name_transp, "squash": name_signed, "beam_transparency": name_transp,
         "beam_width": name_width, "trail_transparency": name_transp, "trail_widthscale": name_size}
NORMALISED = ("size", "squash", "beam_width", "trail_widthscale")


def rnd(keys):
    return [[round(a, 4), round(b, 4), round(e, 4)] for a, b, e in keys]


def cluster_kind(kind, items):
    """Cluster, pick medoids + alternates, name. Returns (library list, per-item name list, info)."""
    norm = kind in NORMALISED
    shapes = [normalise(it["keys"])[0] if norm else it["keys"] for it in items]
    X = np.array([features(s) for s in shapes])
    D = dist_matrix(X)
    kmin, kmax = K_RANGE[kind]
    k, sil = pick_k(D, kmin, kmax)
    meds, lab = kmedoids(D, k, restarts=40)
    names = unique([NAMER[kind](shapes[m]) for m in meds])
    n = len(items)
    lib = []
    for c, m in enumerate(meds):
        idx = np.where(lab == c)[0]
        cost = {int(i): float(D[i, idx].sum()) for i in idx}
        alts, used_eff = [], {items[m]["effect"]}
        for i in sorted(cost, key=cost.get):
            if i == m or items[i]["effect"] in used_eff or D[i, m] < 0.05:
                continue
            alts.append(i)
            used_eff.add(items[i]["effect"])
            if len(alts) == 2:
                break
        it = items[m]

        def pack(j):
            x = items[j]
            d = {"keypoints": rnd(x["keys"]), "source": {"effect": x["effect"], "path": x["path"]}}
            if norm:
                d["keypoints_norm"] = rnd(shapes[j])
            return d

        entry = {"name": names[c], "share": round(len(idx) / n, 4), "n": int(len(idx)), "n_kind": n,
                 "jobs": dict(Counter(items[i]["job"] for i in idx).most_common()),
                 "lifetime_median": med([items[i]["life"] for i in idx]),
                 "peak_size_median": med([items[i]["peak"] for i in idx]),
                 "n_keypoints": len(it["keys"]),
                 "envelope": any(k_[2] > 0 for k_ in it["keys"])}
        entry.update(pack(m))
        entry["alternates"] = [pack(j) for j in alts]
        lib.append(entry)
    lib.sort(key=lambda e: -e["n"])
    return lib, [names[l] for l in lab], {"k": k, "silhouette": round(sil, 3), "n": n}


def cluster_colour(items):
    pats = [colour_pattern(it["keys"]) for it in items]
    n = len(items)
    lib = []
    for p, _ in Counter(pats).most_common():
        idx = [i for i, q in enumerate(pats) if q == p]
        X = np.array([colour_vec(items[i]["keys"]) for i in idx])
        D = dist_matrix(X)
        m = idx[int(D.sum(1).argmin())]
        it = items[m]
        lib.append({"name": p, "share": round(len(idx) / n, 4), "n": len(idx), "n_kind": n,
                    "jobs": dict(Counter(items[i]["job"] for i in idx).most_common()),
                    "lifetime_median": med([items[i]["life"] for i in idx]), "peak_size_median": None,
                    "n_keypoints": len(it["keys"]), "keypoints": it["keys"],
                    "source": {"effect": it["effect"], "path": it["path"]}})
    return lib, pats


def pop_check(rows):
    def stats(tiers, job=None):
        n = flat = pop = mid = 0
        for r in rows:
            if r["class"] != "ParticleEmitter" or r.get("dup") or r["tier"] not in tiers:
                continue
            if job and r.get("job") != job:
                continue
            sz = clean_keys(r["size"], 0.0)
            if not sz or max(k[1] for k in sz) <= 0:
                continue
            m = max(k[1] for k in sz)
            n += 1
            s0, s02 = at(sz, 0) / m, at(sz, 0.02) / m
            if s02 >= 0.6:
                flat += 1
                if s0 < 0.3:
                    pop += 1
                elif s0 < 0.6:
                    mid += 1
        return {"n": n, "reach60_by_0.02": flat, "true_pop(start<30%)": pop, "start_30_60": mid}
    out = {}
    for label, tiers in (("S+A", "SA"), ("B+C", "BC")):
        out[label] = stats(tiers)
        out[label + " impact burst"] = stats(tiers, "impact burst")
    return out


def pairings(items_size, labs_size, items_tr, labs_tr):
    sz = {it["rid"]: lab for it, lab in zip(items_size, labs_size)}
    per = defaultdict(Counter)
    for it, tl in zip(items_tr, labs_tr):
        if it["rid"] in sz:
            per[it["job"]][(sz[it["rid"]], tl)] += 1
    return per


# ----------------------------------------------------------------------------- output


def ck(keys, nd=2):
    return " ".join((f"{k[0]:.{nd}f}:{k[1]:.{nd}f}").replace("0.", ".") for k in keys)


def fmtjobs(j, top=4):
    return ", ".join(f"{a} {b}" for a, b in list(j.items())[:top])


TRANSP_KINDS = ("transparency", "beam_transparency", "trail_transparency")


def shape_md(kind, lib, info):
    lines = [f"### {kind} (n={info['n']}, k={info['k']}, silhouette {info['silhouette']})"]
    if kind in TRANSP_KINDS:
        lines.append("Spark = opacity (1-transparency); keypoints are raw transparency.")
    lines.append("| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for e in lib:
        keys = e.get("keypoints_norm") or e["keypoints"]
        if kind in TRANSP_KINDS:
            sp = spark([[k[0], 1 - k[1]] for k in e["keypoints"]])
        elif kind == "squash":
            sp = spark(keys, -1, 1)
        else:
            sp = spark(keys)
        env = " (+env)" if e.get("envelope") else ""
        lt = e["lifetime_median"] if e["lifetime_median"] is not None else "-"
        pk = e["peak_size_median"] if e["peak_size_median"] is not None else "-"
        lines.append(f"| {e['name']} | {sp} | {ck(keys)}{env} | {e['share']*100:.0f}% (n={e['n']}) | "
                     f"{fmtjobs(e['jobs'])} | {lt} | {pk} | {e['source']['effect'].split('__')[-1]} |")
    return lines


def build(rows):
    kinds = collect(rows)
    lib, labels, infos = {}, {}, {}
    for kind in K_RANGE:
        lib[kind], labels[kind], infos[kind] = cluster_kind(kind, kinds[kind])
    lib["color"], _ = cluster_colour(kinds["color"])
    per = pairings(kinds["size"], labels["size"], kinds["transparency"], labels["transparency"])
    jobn = Counter(it["job"] for it in kinds["transparency"])
    return {"lib": lib, "infos": infos, "pairs": per, "pop": pop_check(rows), "jobn": jobn,
            "n_rows": {k: len(v) for k, v in kinds.items()}}


def write_json(res, path=OUT_JSON):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc = {"_about": "Curve library from S+A pro VFX (study set). Keypoints are [t, value, envelope] (colour: [t,[r,g,b]]). "
                     "Size/squash/beam_width/trail_widthscale also give keypoints_norm (value/max); scale by peak_size_median studs.",
           "_n": res["n_rows"], "_k": res["infos"]}
    doc.update(res["lib"])
    with open(path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=1)
    return doc


def write_md(res, path=OUT_MD):
    L = ["> Author: data agent · claude-sonnet-5-5 · medium · 2026-10-20", "",
         "# Curve library: named S+A pro curve shapes (medoids, not averages)", "",
         "Source: `output/vfx/training-dumps/emitters_study.jsonl`, S+A tier only (particle emitters dup=false, Beam, Trail). "
         "Rebuild: `python tools/vfx/curve_library.py` (also writes `content/vfx/curves.json` with exact keypoints, envelope and 2 alternates per curve). "
         "Each curve is the real medoid of a k-medoids cluster on 41 linear + 7 log-time points (t=.001 to 1); k chosen by silhouette in a preset range. "
         "Size/squash are shown normalised (value/max): multiply by peak studs. Shares are of that kind's n. "
         "Spark uses a non-uniform time axis (t=0,.01,.03,.06,.1,.2,.35,.5,.65,.8,.9,1) so early pops stay visible. "
         "`(+env)` = medoid carries envelope (random range) keypoints, see json.", "", "## Curves per kind"]
    R = res["lib"]
    for kind in ("size", "transparency", "squash", "beam_transparency", "beam_width", "trail_transparency", "trail_widthscale"):
        L += shape_md(kind, R[kind], res["infos"][kind]) + [""]
    nc = res["n_rows"]["color"]
    L.append(f"### colour pattern (n={nc}; rule on first/last colour + luminance; medoid = nearest real sequence; RGB 0-255, first 6 keys)")
    L += ["| pattern | keypoints t:[r,g,b] | share | jobs (count) | src |", "|---|---|---|---|---|"]
    for e in R["color"]:
        kp = " ".join(f"{k[0]:.2f}:[{k[1][0]},{k[1][1]},{k[1][2]}]" for k in e["keypoints"][:6])
        L.append(f"| {e['name']} | {kp} | {e['share']*100:.0f}% (n={e['n']}) | {fmtjobs(e['jobs'])} | {e['source']['effect'].split('__')[-1]} |")
    L += ["", "## Pairings: (size curve + transparency curve) per job, top 3",
          "n = S+A particle emitters of that job. Jobs with n<8 are anecdotes.", "| job | n | #1 | #2 | #3 |", "|---|---|---|---|---|"]
    defaults = {}
    for job, n in res["jobn"].most_common():
        if job in ("beam", "trail"):
            continue
        top = res["pairs"][job].most_common(3)
        if top:
            defaults[job] = (top[0][0], n, top[0][1])
        cells = [f"{a} + {b} ({c}, {c*100/n:.0f}%)" for (a, b), c in top] + [""] * (3 - len(top))
        L.append(f"| {job} | {n} | " + " | ".join(cells) + " |")
    p = res["pop"]
    L += ["", "## Pop check (size reaches >=60% of its max by t<=0.02)",
          "Of the curves that reach 60% by t<=.02: true pop = start below 30% (a real jump); start 30-60% = partial jump; the rest start at >=60% already (constant size or shrink-only).",
          "| set | n size curves | reach 60% by t<=.02 | true pop (start<30%) | partial (30-60%) |", "|---|---|---|---|---|"]
    for k in ("S+A", "B+C", "S+A impact burst", "B+C impact burst"):
        v = p[k]
        n = max(1, v["n"])
        L.append(f"| {k} | {v['n']} | {v['reach60_by_0.02']} ({v['reach60_by_0.02']*100/n:.0f}%) | "
                 f"{v['true_pop(start<30%)']} ({v['true_pop(start<30%)']*100/n:.0f}%) | {v['start_30_60']} ({v['start_30_60']*100/n:.0f}%) |")
    L += ["", "## How to pick (planner rules)",
          "1. Pick the layer job, then copy its default size + transparency pair below (most common S+A pair). Copy `keypoints` verbatim from `content/vfx/curves.json`; scale size with `keypoints_norm` x your peak studs.",
          "2. Deviate only with a reason (a longer-lived smoke may want a later fade). Never average two curves: choose one.",
          "3. Keep envelope keypoints when the medoid has them: the random range is part of the look.",
          "4. Impact flash and core pop: an `impact pop` size curve with a short lifetime (life column). Glow and halo: V-glow transparency.",
          "5. Colour: one pattern per layer; start from the medoid keypoints, then re-key hue to the stage palette.",
          "", "Default pair per job (n = S+A layers of the job):", "| job | size | transparency | n(job) | pair count |", "|---|---|---|---|---|"]
    for job, (pair, n, c) in defaults.items():
        L.append(f"| {job} | {pair[0]} | {pair[1]} | {n} | {c} |")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return len(L)


def main():
    res = build(load_rows())
    write_json(res)
    n = write_md(res)
    print("curves:", {k: len(v) for k, v in res["lib"].items()}, "md lines:", n)
    print("pop:", res["pop"])


if __name__ == "__main__":
    main()
