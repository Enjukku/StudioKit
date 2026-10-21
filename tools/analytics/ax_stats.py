#!/usr/bin/env python3
"""Statistics helper for the analyst: the analyst calls these instead of doing arithmetic in prose.

Every function states its assumptions in its docstring and has a test with a checked value
(tools/tests/test_analytics_stats.py). Output conventions:
  - absolute differences of rates are in percentage points (`*_pp`); relative differences are in percent
    (`*_pct`). They are never mixed.
  - every result repeats its inputs, so no number travels without what produced it.

Python 3.11+ standard library only (statistics.NormalDist for the normal quantiles).
"""
from __future__ import annotations

import math
from datetime import date, datetime, time, timedelta, timezone
from statistics import NormalDist

SRM_ALARM_P = 0.0005           # Microsoft ExP practice (brief J013-T04); configurable per call
DEFAULT_REPORTING_LAG_DAYS = 1  # PROPOSAL: Roblox documents no data lag (fact-check 01 §4.1); configurable
_N = NormalDist()


def _z(p: float) -> float:
    return _N.inv_cdf(p)


# -- Cohort maturity ---------------------------------------------------------------------------------------------
def cohort_maturity(first_play: date, day_n: int, now: datetime,
                    lag_days: int = DEFAULT_REPORTING_LAG_DAYS) -> dict:
    """Can the DN retention value of the cohort that first played on `first_play` (a UTC date) be read at `now`?

    Assumptions: Roblox's DN is the return on the (N+1)th day counting the first-play day as day 1, so D7 of
    the 06/20 cohort is the return on 06/27 (docs example, fact-check 01 RF-14): return day = first_play + N. The value is readable only after that whole UTC day has passed
    (i.e. from first_play + day_n + 1 at 00:00 UTC) plus `lag_days` of reporting lag. Roblox documents no lag;
    the default 1 day is a PROPOSAL. Before that the answer is "not mature": never a number.
    """
    if day_n < 0 or lag_days < 0:
        raise ValueError("day_n and lag_days must be >= 0")
    now = now.astimezone(timezone.utc)
    return_day = first_play + timedelta(days=day_n)
    readable = datetime.combine(return_day + timedelta(days=1 + lag_days), time(0), tzinfo=timezone.utc)
    mature = now >= readable
    return {"first_play_date": first_play.isoformat(), "day_n": day_n, "lag_days": lag_days,
            "lag_label": "PROPOSAL: Roblox documents no reporting lag (fact-check 01 §4.1, 02 F-08)",
            "return_day": return_day.isoformat(),
            "readable_once_closed_day": (return_day + timedelta(days=lag_days)).isoformat(),
            "readable_from_utc": readable.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "now_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "mature": mature,
            "verdict": "mature" if mature else "not mature",
            "wait_hours": 0.0 if mature else round((readable - now).total_seconds() / 3600, 1)}


# -- Two rates ---------------------------------------------------------------------------------------------------
def wilson_interval(x: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Wilson score interval for one proportion x/n.

    Assumptions: independent binary outcomes, one per player (not per session). Chosen over the Wald
    interval because Wald covers badly for small n or rates near 0 or 1 (Newcombe 1998, Stat Med 17:857).
    """
    if n <= 0 or not 0 <= x <= n:
        raise ValueError("need 0 <= x <= n and n > 0")
    z = _z(1 - (1 - conf) / 2)
    p = x / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def rate_difference(x_a: int, n_a: int, x_b: int, n_b: int, conf: float = 0.95, method: str = "newcombe") -> dict:
    """Difference between two rates, B minus A (A = control or before, B = treatment or after).

    Absolute difference: Newcombe hybrid score interval (method 10, Newcombe 1998, Stat Med 17:873), built from
    the two Wilson intervals; good coverage for small samples and rates near 0 or 1, unlike Wald.
    Relative difference: risk ratio B/A with the Katz log interval; reported as percent change (ratio - 1).
    method="wald" gives d +/- z sqrt(pa qa/na + pb qb/nb) instead, with a warning: it fails with small counts,
    rates near 0 or 1 and zero cells (fact-check 02 F-03).
    Assumptions: two independent groups; each player counted once in one group; binary (yes/no) outcome only,
    never money amounts. Not valid for the same players measured twice, or for averages of per-session values.
    """
    if method not in ("newcombe", "wald"):
        raise ValueError("method is newcombe (default) or wald")
    if n_a <= 0 or n_b <= 0 or not 0 <= x_a <= n_a or not 0 <= x_b <= n_b:
        raise ValueError("need 0 <= x <= n and n > 0 for both groups")
    p_a, p_b = x_a / n_a, x_b / n_b
    l_a, u_a = wilson_interval(x_a, n_a, conf)
    l_b, u_b = wilson_interval(x_b, n_b, conf)
    d = p_b - p_a
    if method == "wald":
        half = _z(1 - (1 - conf) / 2) * math.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
        lo, hi = d - half, d + half
    else:
        lo = d - math.sqrt((p_b - l_b) ** 2 + (u_a - p_a) ** 2)
        hi = d + math.sqrt((u_b - p_b) ** 2 + (p_a - l_a) ** 2)
    out = {"inputs": {"x_a": x_a, "n_a": n_a, "x_b": x_b, "n_b": n_b, "confidence": conf},
           "rate_a": p_a, "rate_b": p_b,
           "absolute_difference_pp": 100 * d, "absolute_interval_pp": [100 * lo, 100 * hi],
           "absolute_method": "Newcombe hybrid score (method 10)" if method == "newcombe" else "Wald",
           "relative_difference_pct": None, "relative_interval_pct": None,
           "relative_method": "risk ratio B/A, Katz log interval"}
    if x_a > 0 and x_b > 0:
        rr = p_b / p_a
        z = _z(1 - (1 - conf) / 2)
        se = math.sqrt(1 / x_b - 1 / n_b + 1 / x_a - 1 / n_a)
        out["relative_difference_pct"] = 100 * (rr - 1)
        out["relative_interval_pct"] = [100 * (rr * math.exp(-z * se) - 1), 100 * (rr * math.exp(z * se) - 1)]
    else:
        out["relative_note"] = "relative difference undefined when a group has 0 successes"
    if method == "wald":
        out["warning"] = "Wald interval: poor coverage with small counts, rates near 0 or 1, or a zero cell; prefer newcombe"
    out["interval_excludes_zero"] = lo > 0 or hi < 0
    return out


# -- Sample size -------------------------------------------------------------------------------------------------
def sample_size_proportions(p_a: float, p_b: float, alpha: float = 0.05, power: float = 0.8) -> dict:
    """Players needed per arm to detect p_a -> p_b with a two-sided test at `alpha` and `power`.

    Normal approximation without continuity correction (Fleiss, Levin & Paik 2003, eq. 4.14):
      n = (z_{1-alpha/2} sqrt(2 pbar qbar) + z_{power} sqrt(p_a q_a + p_b q_b))^2 / (p_a - p_b)^2, rounded up.
    Assumptions: equal arms, independent players, binary outcome, a fixed horizon (no peeking).
    """
    if not (0 < p_a < 1 and 0 < p_b < 1) or p_a == p_b:
        raise ValueError("need two different rates strictly between 0 and 1")
    if not (0 < alpha < 1 and 0 < power < 1):
        raise ValueError("alpha and power must be in (0, 1)")
    za, zb = _z(1 - alpha / 2), _z(power)
    pbar = (p_a + p_b) / 2
    num = za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p_a * (1 - p_a) + p_b * (1 - p_b))
    n = math.ceil(num ** 2 / (p_a - p_b) ** 2)
    return {"inputs": {"p_a": p_a, "p_b": p_b, "alpha": alpha, "power": power, "sides": 2},
            "absolute_effect_pp": 100 * (p_b - p_a), "relative_effect_pct": 100 * (p_b / p_a - 1),
            "n_per_arm": n, "n_total": 2 * n, "method": "two-proportion normal approximation (Fleiss)"}


def sample_size_means(sigma: float, delta: float, power: float = 0.8) -> dict:
    """Players needed per arm to detect a mean difference `delta` when the per-player standard deviation is
    `sigma`, two-sided alpha 0.05: Lehr's rule n = 16 sigma^2 / delta^2 (80 % power) or 21 sigma^2 / delta^2
    (90 % power). Also returns the normal-approximation value 2 (z_0.975 + z_power)^2 sigma^2 / delta^2.

    Assumptions: equal arms, roughly normal per-player means (needs large n). Revenue per player is heavily
    skewed (most players pay 0, a few pay a lot): sigma from a small sample is unreliable and the normal
    approximation can be poor; cap or trim outliers, or use a payer-conversion test, and check with care.
    """
    if sigma <= 0 or delta == 0:
        raise ValueError("need sigma > 0 and delta != 0")
    factor = {0.8: 16, 0.9: 21}.get(round(power, 2))
    if factor is None:
        raise ValueError("Lehr's rule exists for power 0.8 (16) and 0.9 (21) only")
    ratio = sigma ** 2 / delta ** 2
    exact = 2 * (_z(0.975) + _z(power)) ** 2 * ratio
    return {"inputs": {"sigma": sigma, "delta": delta, "alpha": 0.05, "power": power, "sides": 2},
            "n_per_arm": math.ceil(factor * ratio), "n_total": 2 * math.ceil(factor * ratio),
            "n_per_arm_normal_approx": math.ceil(exact), "method": f"Lehr's rule n = {factor} sigma^2 / delta^2",
            "warning": "Skewed data (revenue per player) needs care: sigma is unstable and outliers dominate; "
                       "cap or trim values, or test payer conversion instead."}


# -- Sample ratio mismatch ---------------------------------------------------------------------------------------
def _gamma_q(a: float, x: float) -> float:
    """Regularized upper incomplete gamma Q(a, x) (series for x < a + 1, continued fraction otherwise;
    Numerical Recipes 3rd ed. §6.2)."""
    if x <= 0:
        return 1.0
    gln = math.lgamma(a)
    if x < a + 1:
        term = total = 1.0 / a
        ap = a
        for _ in range(10000):
            ap += 1
            term *= x / ap
            total += term
            if abs(term) < abs(total) * 1e-15:
                break
        return max(0.0, 1.0 - total * math.exp(-x + a * math.log(x) - gln))
    b = x + 1 - a
    c = 1 / 1e-300
    d = 1 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c
        c = 1e-300 if abs(c) < 1e-300 else c
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def chi2_sf(x: float, df: int) -> float:
    """P(X >= x) for a chi-square variable with df degrees of freedom."""
    if df < 1:
        raise ValueError("df >= 1")
    return _gamma_q(df / 2, x / 2)


def sample_ratio_check(counts: list[int], planned: list[float] | None = None, alarm_p: float = SRM_ALARM_P) -> dict:
    """Chi-square goodness-of-fit of the observed arm sizes against the planned split.

    Assumptions: counts are assignment units (players), each in one arm; `planned` are the planned shares
    (any positive weights; default equal). p < alarm_p (default 0.0005, Microsoft ExP practice) means the
    assignment or logging is broken: the experiment's results are not trustworthy. The tool never suggests
    reweighting or "adjusting".
    """
    k = len(counts)
    if k < 2 or any(c < 0 for c in counts) or sum(counts) == 0:
        raise ValueError("need at least 2 non-negative counts with a positive total")
    planned = planned or [1.0] * k
    if len(planned) != k or any(w <= 0 for w in planned):
        raise ValueError("planned needs one positive weight per arm")
    total, wsum = sum(counts), sum(planned)
    expected = [total * w / wsum for w in planned]
    stat = sum((o - e) ** 2 / e for o, e in zip(counts, expected))
    p = chi2_sf(stat, k - 1)
    bad = p < alarm_p
    return {"inputs": {"counts": counts, "planned": planned, "alarm_p": alarm_p},
            "expected": expected, "chi_square": stat, "df": k - 1, "p_value": p, "srm": bad,
            "verdict": "invalid test: investigate" if bad else "no sample ratio mismatch detected"}


# -- Difference in differences -----------------------------------------------------------------------------------
def mix_decomposition(segments: list[dict]) -> dict:
    """Split a change in an overall rate into a "rate" part (segments' own rates moved) and a "mix" part (the
    share of players in each segment moved). Each segment: {"name", "n_before", "rate_before", "n_after",
    "rate_after"}; n = players (or estimated players) in the segment, rate = a fraction 0..1.

    Assumptions and limits: an arithmetic identity, not a causal split; segments must be the same, complete and
    non-overlapping in both periods (counts reconcile to the totals); the split depends on which weights are held
    fixed, so both versions are returned (before weights = the "standardized" rate the diagnosis asks for). With
    estimated n (rate x players) every output is an estimate too. No interval: use rate_difference per segment."""
    if not segments:
        raise ValueError("no segments")
    for sg in segments:
        for k in ("n_before", "rate_before", "n_after", "rate_after"):
            if k not in sg:
                raise ValueError(f"segment {sg.get('name')!r} lacks {k}")
        if sg["n_before"] < 0 or sg["n_after"] < 0 or not (0 <= sg["rate_before"] <= 1 and 0 <= sg["rate_after"] <= 1):
            raise ValueError(f"segment {sg.get('name')!r}: n must be >= 0 and rates in 0..1")
    nb = sum(sg["n_before"] for sg in segments)
    na = sum(sg["n_after"] for sg in segments)
    if nb <= 0 or na <= 0:
        raise ValueError("each period needs players")
    before = sum(sg["n_before"] * sg["rate_before"] for sg in segments) / nb
    after = sum(sg["n_after"] * sg["rate_after"] for sg in segments) / na
    std_after = sum(sg["n_before"] / nb * sg["rate_after"] for sg in segments)   # after rates, before mix
    std_before = sum(sg["n_after"] / na * sg["rate_before"] for sg in segments)  # before rates, after mix
    pp = 100.0
    return {
        "inputs": {"segments": segments},
        "overall_before": before, "overall_after": after,
        "returned_before": sum(sg["n_before"] * sg["rate_before"] for sg in segments),
        "returned_after": sum(sg["n_after"] * sg["rate_after"] for sg in segments),
        "total_change_pp": (after - before) * pp,
        "standardized_after_before_weights": std_after,
        "rate_effect_pp_before_weights": (std_after - before) * pp,
        "mix_effect_pp_before_weights": (after - std_after) * pp,
        "rate_effect_pp_after_weights": (after - std_before) * pp,
        "mix_effect_pp_after_weights": (std_before - before) * pp,
        "shares_before": {sg.get("name", str(i)): sg["n_before"] / nb for i, sg in enumerate(segments)},
        "shares_after": {sg.get("name", str(i)): sg["n_after"] / na for i, sg in enumerate(segments)},
        "warning": "identity, not a cause; the split depends on the weights held fixed (both shown); "
                   "estimated n makes every output an estimate",
    }


def diff_in_diff(treat_before: float, treat_after: float, control_before: float, control_after: float,
                 se: list[float] | None = None, conf: float = 0.95) -> dict:
    """(treat_after - treat_before) - (control_after - control_before).

    Assumptions: parallel trends (without the change, the treated group would have moved like the control);
    no spill-over between groups; the same metric definition in both periods. Optional `se` = standard errors
    of the four inputs in the order above, assumed independent: SE = sqrt(sum se_i^2), normal interval.
    The arithmetic does not test parallel trends: check the pre-period trend separately.
    """
    t_change = treat_after - treat_before
    c_change = control_after - control_before
    did = t_change - c_change
    out = {"inputs": {"treat_before": treat_before, "treat_after": treat_after, "control_before": control_before,
                      "control_after": control_after, "se": se, "confidence": conf},
           "treat_change": t_change, "control_change": c_change, "did": did,
           "assumption": "parallel trends; not tested by this arithmetic"}
    if se is not None:
        if len(se) != 4 or any(s < 0 for s in se):
            raise ValueError("se needs 4 non-negative values")
        s = math.sqrt(sum(x * x for x in se))
        z = _z(1 - (1 - conf) / 2)
        out["did_se"] = s
        out["did_interval"] = [did - z * s, did + z * s]
    return out


# -- Welch difference of means -----------------------------------------------------------------------------------
def _betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta (Numerical Recipes 3rd ed. §6.4)."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (tiny if abs(d) < tiny else d)
    h = d
    for m in range(1, 10000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        d = 1 / (tiny if abs(d) < tiny else d)
        c = 1 + aa / c
        c = tiny if abs(c) < tiny else c
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        d = 1 / (tiny if abs(d) < tiny else d)
        c = 1 + aa / c
        c = tiny if abs(c) < tiny else c
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * _betacf(a, b, x) / a
    return 1 - front * _betacf(b, a, 1 - x) / b


def t_cdf(t: float, df: float) -> float:
    """Student t CDF for any real df > 0: 1 - I_{df/(df+t^2)}(df/2, 1/2) / 2 for t >= 0."""
    if df <= 0:
        raise ValueError("df > 0")
    tail = 0.5 * _betai(df / 2, 0.5, df / (df + t * t))
    return 1 - tail if t >= 0 else tail


def t_quantile(p: float, df: float) -> float:
    """Inverse Student t CDF by bisection on t_cdf (|error| < 1e-10)."""
    if not 0 < p < 1:
        raise ValueError("p in (0, 1)")
    lo, hi = -1e4, 1e4
    for _ in range(200):
        mid = (lo + hi) / 2
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-10:
            break
    return (lo + hi) / 2


def welch_difference(mean_a: float, sd_a: float, n_a: int, mean_b: float, sd_b: float, n_b: int,
                     conf: float = 0.95) -> dict:
    """Difference of means B - A with the Welch interval (unequal variances; Welch-Satterthwaite df).

    SE = sqrt(sd_a^2/n_a + sd_b^2/n_b); df = (a+b)^2 / (a^2/(n_a-1) + b^2/(n_b-1)), a = sd_a^2/n_a,
    b = sd_b^2/n_b; interval d +/- t_{df, 1-alpha/2} SE (fact-check 02 F-04).
    Assumptions: independent players, one value per player, per-player means near normal (large n).
    Revenue-like data (mostly zeros, a long tail): approximate only; coverage can be poor at modest n. Validate
    on pre-period A/A data and pre-declare any capping for both arms (02 F-14).
    """
    if n_a < 2 or n_b < 2 or sd_a < 0 or sd_b < 0 or (sd_a == 0 and sd_b == 0):
        raise ValueError("need n >= 2 per arm and a positive variance")
    a, b = sd_a ** 2 / n_a, sd_b ** 2 / n_b
    se = math.sqrt(a + b)
    df = (a + b) ** 2 / (a * a / (n_a - 1) + b * b / (n_b - 1))
    t = t_quantile(1 - (1 - conf) / 2, df)
    d = mean_b - mean_a
    out = {"inputs": {"mean_a": mean_a, "sd_a": sd_a, "n_a": n_a, "mean_b": mean_b, "sd_b": sd_b, "n_b": n_b,
                      "confidence": conf},
           "difference": d, "se": se, "df": df, "t": t, "interval": [d - t * se, d + t * se],
           "relative_difference_pct": 100 * d / mean_a if mean_a else None,
           "method": "Welch t interval",
           "warning": "Revenue-like (zero-heavy, long-tailed) data: approximate only; validate on A/A data."}
    return out


# -- Verdict helper (PROPOSAL rules, fact-check 02 §5 with the lead's default) -----------------------------------
VERDICT_RULE_LABEL = ("PROPOSAL (lead J013-T04 update 2, pending owner G3): default useful = L > 0 and point >= b; "
                      "strict useful = L >= b")


def verdict(lower: float, upper: float, point: float, benefit: float, harm: float, *,
            guardrails: list[dict] | None = None, integrity_ok: bool = True, matured: bool = True,
            stopping_ok: bool = True, rule: str = "default") -> dict:
    """One verdict from an interval [lower, upper] for theta = treatment - control (sign set so higher is
    better), following fact-check 02 §5, first true wins:
      0 no verdict yet (matured false) · 1 invalid (integrity_ok or stopping_ok false) · 2 harmful
      (upper <= -harm, or a guardrail upper <= -margin) · 3 useful improvement · 4 no worthwhile effect within
      tested bounds (upper < benefit and lower > -harm) · 5 inconclusive with a reason.
    Useful: rule "default" = lower > 0 and point >= benefit (and every guardrail lower > -margin);
            rule "strict"  = lower >= benefit (and the same guardrail condition).
    guardrails: [{"name", "lower", "upper", "margin"}]. benefit and harm must be > 0 and in theta's unit.
    Assumptions: the interval comes from a fixed-horizon (or valid sequential) analysis at the planned alpha.
    """
    if rule not in ("default", "strict"):
        raise ValueError("rule is default or strict")
    if benefit <= 0 or harm <= 0 or lower > upper:
        raise ValueError("need benefit > 0, harm > 0, lower <= upper")
    guards = guardrails or []
    inputs = {"lower": lower, "upper": upper, "point": point, "benefit": benefit, "harm": harm,
              "guardrails": guards, "integrity_ok": integrity_ok, "matured": matured, "stopping_ok": stopping_ok,
              "rule": rule}

    def done(v: str, reason: str = "") -> dict:
        return {"inputs": inputs, "verdict": v, "reason": reason, "rule_label": VERDICT_RULE_LABEL}

    if not matured:
        return done("no verdict yet", "outcomes not mature")
    if not integrity_ok or not stopping_ok:
        return done("invalid", "integrity check failed" if not integrity_ok else "stopping rule not met")
    bad_guard = [g["name"] for g in guards if g["upper"] <= -g["margin"]]
    if upper <= -harm or bad_guard:
        return done("harmful", f"guardrail harmed: {bad_guard}" if bad_guard else "upper bound <= -harm")
    guards_clear = all(g["lower"] > -g["margin"] for g in guards)
    useful = lower >= benefit if rule == "strict" else (lower > 0 and point >= benefit)
    if useful and guards_clear:
        return done("useful improvement")
    if upper < benefit and lower > -harm and guards_clear:
        return done("no worthwhile effect within tested bounds")
    if not guards_clear:
        reason = "guardrail not cleared"
    elif lower <= -harm:
        reason = "harm not excluded"
    else:
        reason = "benefit unproven"
    return done("inconclusive", reason)
