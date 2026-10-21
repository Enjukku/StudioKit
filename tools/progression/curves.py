#!/usr/bin/env python3
"""Progression curve library: exact formulas for costs, levels, waits, prestige, offline earnings,
combat breakpoints, stacking and paid-random odds.

Kit tool (universal, Studio Kit). Python 3.11+ standard library only.

What it does: evaluates closed forms and their direct sums with exact rational arithmetic
(fractions.Fraction) whenever the result is rational; pass floats to get float results. Functions whose
result is irrational for general inputs (logarithms, non-integer powers) return a float, and the
`floor_*` helpers give the exact integer floor by checking an inequality in rational arithmetic.

What it never claims: no function picks a coefficient for the caller; every coefficient is an input.
A curve is not a feeling: an exponential price says nothing about whether the wait is fun. The published
prestige formulas below are historical models of other games, not recommended values.

Conventions:
  - Index n is a non-negative integer unless a docstring says otherwise. "level l" starts at 1.
  - Units: prices and balances are in the caller's currency unit; rates in currency per second;
    times in seconds; health and damage in hit points; probabilities are fractions in [0, 1].
  - Invalid domains raise ValueError with the reason; nothing returns a silent wrong number.
  - An unaffordable target with zero income returns UNREACHABLE (never 0 and never infinity).

Sources (paraphrased, never copied): owner research paper Progression_Designer_Research_2026 (outside git)
sections 3-5 and 7-8; M01 (2016-10-04) exponential prices and bulk buy; M02/C01 (2017-01-12) prestige
formulas and accounting bases; M04 (2010-07-14) XP tables and hit breakpoints; M06 (2023-10-10) stacking;
W05 (NIST) interval methods are in sim.py.

Usage (library):
  import curves as cv
  cv.exponential(4, Fraction(107, 100), 2)          # a * r**n
  cv.wait_time(cost=4, wallet=0, rate=Fraction(167, 100))
  cv.max_affordable(b=4, r=Fraction(107, 100), k=0, wallet=100, rounding="none")
  python tools/progression/curves.py                # prints a short self-check of the paper fixtures
"""

from __future__ import annotations

import math
from fractions import Fraction
from numbers import Rational
from typing import Callable, Iterable, Sequence

VERSION = "1.0.0"
ROUNDING_RULES = ("none", "floor", "ceil", "half_even")


class Unreachable:
    """A target that cannot be reached under the stated state (for example zero income). Never a number."""

    __slots__ = ("reason",)

    def __init__(self, reason: str):
        self.reason = reason

    def __repr__(self) -> str:
        return f"Unreachable({self.reason!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Unreachable) and other.reason == self.reason

    def __hash__(self) -> int:
        return hash(self.reason)


UNREACHABLE_ZERO_INCOME = Unreachable("unreachable: zero income")


# ---------------------------------------------------------------- helpers

def _req(cond: bool, msg: str) -> None:
    if not cond:
        raise ValueError(msg)


def _is_int(x) -> bool:
    return isinstance(x, int) and not isinstance(x, bool) or (isinstance(x, Fraction) and x.denominator == 1)


def _count(n, name: str = "n") -> int:
    _req(_is_int(n) or (isinstance(n, float) and n.is_integer()), f"{name} must be an integer, got {n!r}")
    n = int(n)
    _req(n >= 0, f"{name} must be >= 0, got {n}")
    return n


def _div(a, b):
    """a/b, exact (Fraction) when both are rational, float otherwise."""
    if isinstance(a, Rational) and isinstance(b, Rational):
        return Fraction(a) / Fraction(b)
    return a / b


def _pow(x, p):
    """x**p, exact when x is rational and p an integer; float otherwise."""
    if _is_int(p):
        return x ** int(p)
    return float(x) ** float(p)


def round_price(x, rule: str):
    """Apply a declared price rounding rule: none | floor | ceil | half_even (to a whole unit)."""
    _req(rule in ROUNDING_RULES, f"rounding must be one of {ROUNDING_RULES}, got {rule!r}")
    if rule == "none":
        return x
    if rule == "floor":
        return math.floor(x)
    if rule == "ceil":
        return math.ceil(x)
    return round(x)  # Python's round() on int, Fraction and float is round-half-to-even


# ---------------------------------------------------------------- curves (paper section 3 table)

def affine(a, b, n):
    """f(n) = a + b*n; a, b >= 0; n >= 0 integer index."""
    _req(a >= 0 and b >= 0, "affine needs a >= 0 and b >= 0")
    return a + b * _count(n)


def polynomial(a, b, p, n):
    """f(n) = a + b*n**p; a, b >= 0, p > 1. Exact for integer p, float otherwise."""
    _req(a >= 0 and b >= 0, "polynomial needs a >= 0 and b >= 0")
    _req(p > 1, f"polynomial needs p > 1, got {p}")
    return a + b * _pow(_count(n), p)


def triangular_cumulative(b, n):
    """F(n) = b*n*(n+1)/2: cumulative cost of n purchases whose k-th costs b*k (k = 1..n). b >= 0."""
    _req(b >= 0, "triangular needs b >= 0")
    n = _count(n)
    return b * _div(n * (n + 1), 2)


def triangular_increment(b, n):
    """Incremental cost of the n-th purchase under the triangular schedule: b*n (n >= 1)."""
    _req(b >= 0, "triangular needs b >= 0")
    n = _count(n)
    _req(n >= 1, "the first purchase has index 1")
    return b * n


def exponential(a, r, n):
    """f(n) = a * r**n; a > 0, r > 1."""
    _req(a > 0, f"exponential needs a > 0, got {a}")
    _req(r > 1, f"exponential needs r > 1, got {r}")
    return a * r ** _count(n)


def logarithmic(a, b, r, n) -> float:
    """f(n) = a + b*log_r(1+n); b >= 0, r > 1. Irrational in general: returns float."""
    _req(b >= 0, "logarithmic needs b >= 0")
    _req(r > 1, f"logarithmic needs r > 1, got {r}")
    return float(a) + float(b) * math.log(1 + _count(n)) / math.log(float(r))


def fractional_power(a, b, alpha, n):
    """f(n) = a + b*n**alpha; 0 < alpha < 1. Float unless n**alpha happens to be exact (n = 0 or 1)."""
    _req(0 < alpha < 1, f"fractional power needs 0 < alpha < 1, got {alpha}")
    n = _count(n)
    if n in (0, 1):
        return a + b * n
    return float(a) + float(b) * float(n) ** float(alpha)


def saturating(a, b, h, n):
    """f(n) = a + b*n/(h+n); h > 0. Approaches a + b as n grows."""
    _req(h > 0, f"saturating needs h > 0, got {h}")
    n = _count(n)
    return a + b * _div(n, h + n)


def piecewise_linear(a, b1, b2, k, n):
    """Continuous piecewise: a + b1*n for n <= K; a + b1*K + b2*(n-K) for n > K. Keeps breakpoint K."""
    k = _count(k, "K")
    n = _count(n)
    return a + b1 * n if n <= k else a + b1 * k + b2 * (n - k)


def milestone_product(base, milestones: Iterable[tuple], n):
    """base * prod(m_i for each (K_i, m_i) with n >= K_i). n is the count compared with K_i (e.g. owned)."""
    n = _count(n)
    out = base
    for k, m in milestones:
        _req(m > 0, f"milestone multiplier must be > 0, got {m}")
        if n >= _count(k, "K"):
            out = out * m
    return out


CURVE_KINDS = {
    "affine": (affine, ("a", "b")),
    "polynomial": (polynomial, ("a", "b", "p")),
    "triangular_cumulative": (triangular_cumulative, ("b",)),
    "exponential": (exponential, ("a", "r")),
    "logarithmic": (logarithmic, ("a", "b", "r")),
    "fractional_power": (fractional_power, ("a", "b", "alpha")),
    "saturating": (saturating, ("a", "b", "h")),
    "piecewise_linear": (piecewise_linear, ("a", "b1", "b2", "K")),
}


def evaluate(spec: dict, n):
    """Evaluate a curve spec {"kind": <name>, <params>} or {"kind": "table", "values": [...]} at index n.

    A table is indexed from 0 (values[n]); an index past its end raises ValueError (no extrapolation).
    """
    kind = spec.get("kind")
    if kind == "table":
        vals = spec["values"]
        n = _count(n)
        _req(n < len(vals), f"table index {n} is past its last entry ({len(vals) - 1}); no extrapolation")
        return vals[n]
    _req(kind in CURVE_KINDS, f"unknown curve kind {kind!r}; known: table, {', '.join(CURVE_KINDS)}")
    fn, names = CURVE_KINDS[kind]
    missing = [p for p in names if p not in spec]
    _req(not missing, f"curve {kind} is missing {missing}")
    return fn(*(spec[p] for p in names), n)


# ---------------------------------------------------------------- level tables

def cumulative_from_per_level(per_level: Sequence) -> list:
    """Per-level requirements e_1..e_m (e_l = XP from level l to l+1) -> cumulative X_1..X_{m+1}.

    Level 1 starts at 0: X_l = sum(e_j for j < l). Index origin: result[0] is X_1.
    """
    out = [0]
    for i, e in enumerate(per_level):
        _req(e >= 0, f"requirement for level {i + 1} is negative: {e}")
        out.append(out[-1] + e)
    return out


def per_level_from_cumulative(cumulative: Sequence) -> list:
    """Cumulative X_1..X_m (X_1 must be 0, non-decreasing) -> per-level e_1..e_{m-1}."""
    _req(len(cumulative) >= 1 and cumulative[0] == 0, "cumulative table must start with X_1 = 0")
    out = []
    for i in range(1, len(cumulative)):
        e = cumulative[i] - cumulative[i - 1]
        _req(e >= 0, f"cumulative table decreases at level {i + 1}")
        out.append(e)
    return out


def level_for(cumulative: Sequence, amount) -> int:
    """Level (1-based) reached with `amount` cumulative XP: the largest l with X_l <= amount."""
    _req(amount >= 0, "XP amount must be >= 0")
    lvl = 0
    for i, x in enumerate(cumulative):
        if x <= amount:
            lvl = i + 1
        else:
            break
    return lvl


# ---------------------------------------------------------------- time from a requirement

def time_for_requirement(requirement, rate=None) -> dict:
    """Time to accumulate `requirement` units at a constant `rate` units/second.

    Returns {"time_s": t | None, "requirement": requirement, "status": ...}:
      status "time"         -> time_s = requirement / rate
      status "symbolic"     -> no rate given: time_s is None; the answer is requirement / q for an unknown q
      status "unreachable"  -> rate == 0 and requirement > 0 (reason: zero income)
    """
    _req(requirement >= 0, "requirement must be >= 0")
    if rate is None:
        return {"time_s": None, "requirement": requirement, "status": "symbolic"}
    _req(rate >= 0, "rate must be >= 0")
    if requirement == 0:
        return {"time_s": 0, "requirement": requirement, "status": "time"}
    if rate == 0:
        return {"time_s": None, "requirement": requirement, "status": "unreachable",
                "reason": UNREACHABLE_ZERO_INCOME.reason}
    return {"time_s": _div(requirement, rate), "requirement": requirement, "status": "time"}


def time_piecewise(requirement, segments: Sequence[tuple]):
    """Time to accumulate `requirement` under piecewise-constant rates.

    segments: [(duration_s, rate), ..., (None, final_rate)]; a None duration means "until the end".
    Returns the time in seconds, or UNREACHABLE if the requirement is never met.
    """
    _req(requirement >= 0, "requirement must be >= 0")
    left, t = requirement, 0
    for dur, rate in segments:
        _req(rate >= 0, "rates must be >= 0")
        if left == 0:
            return t
        if dur is None:
            return t + _div(left, rate) if rate else UNREACHABLE_ZERO_INCOME
        _req(dur >= 0, "segment durations must be >= 0")
        gain = rate * dur
        if gain >= left:
            return t + _div(left, rate)
        left -= gain
        t += dur
    return t if left == 0 else UNREACHABLE_ZERO_INCOME


# ---------------------------------------------------------------- incremental: bulk buy, waits, payback

def bulk_cost_closed(b, r, k, n):
    """Closed form B(k, n) = b*r**k*(r**n - 1)/(r - 1) for n purchases from k owned; r > 1 (r == 1: b*n).

    Valid only for unrounded, unchanged exponential prices C(j) = b*r**j.
    """
    _req(b > 0, "b must be > 0")
    _req(r >= 1, f"r must be >= 1, got {r}")
    k, n = _count(k, "k"), _count(n)
    if r == 1:
        return b * n
    return b * r ** k * (r ** n - 1) / (r - 1)


def bulk_cost_direct(price: Callable[[int], object], k, n, rounding: str = "none", scope: str = "per_item"):
    """Direct sum of n purchases starting at k owned, with the declared rounding rule.

    price(j) is the unrounded price of the purchase made while owning j. scope "per_item" sums the rounded
    per-item prices (the default for bulk buys); scope "bulk_sum" rounds the summed price once.
    """
    k, n = _count(k, "k"), _count(n)
    _req(scope in ("per_item", "bulk_sum"), f"scope must be per_item or bulk_sum, got {scope!r}")
    if scope == "per_item":
        return sum((round_price(price(j), rounding) for j in range(k, k + n)), 0)
    return round_price(sum((price(j) for j in range(k, k + n)), 0), rounding)


def max_affordable(b, r, k, wallet, rounding: str = "none", scope: str = "per_item") -> int:
    """Largest n with B(k, n) <= wallet < B(k, n+1) for prices b*r**j (j = owned before each purchase).

    The log formula floor(log_r(1 + w(r-1)/(b r**k))) is only an estimate; the inequality on the actual
    (rounded) prices decides. A purchase that costs 0 after rounding makes the count unbounded -> ValueError.
    """
    _req(b > 0, "b must be > 0")
    _req(r >= 1, f"r must be >= 1, got {r}")
    _req(wallet >= 0, "wallet must be >= 0")
    k = _count(k, "k")

    def price(j):
        return b * r ** j

    def total(n):
        return bulk_cost_direct(price, k, n, rounding, scope)

    if r == 1:
        est = int(wallet // b)
    else:
        arg = 1 + float(wallet) * (float(r) - 1) / (float(b) * float(r) ** k)
        est = max(0, int(math.floor(math.log(arg) / math.log(float(r))))) if arg > 0 and math.isfinite(arg) else 0
    n = est
    while n > 0 and total(n) > wallet:
        n -= 1
    guard = 0
    while total(n + 1) <= wallet:
        n += 1
        guard += 1
        _req(guard < 10_000_000, "max_affordable did not converge (zero-cost purchases after rounding?)")
    return n


def wait_time(cost, wallet, rate):
    """Wait max(0, C - w)/P in seconds for a constant rate P >= 0; UNREACHABLE when P == 0 and C > w."""
    _req(cost >= 0 and wallet >= 0, "cost and wallet must be >= 0")
    _req(rate >= 0, "rate must be >= 0")
    missing = cost - wallet
    if missing <= 0:
        return 0
    if rate == 0:
        return UNREACHABLE_ZERO_INCOME
    return _div(missing, rate)


def payback(cost, delta_rate):
    """Simple payback C / dP in seconds for an upgrade adding dP > 0 per second. Not a ranking proof."""
    _req(cost >= 0, "cost must be >= 0")
    _req(delta_rate > 0, f"payback needs dP > 0, got {delta_rate}")
    return _div(cost, delta_rate)


def sequential_reinvest_time(c1, r, p, k_target):
    """Cumulative time to own K producers starting from 1 owned and an empty wallet, buying each next one as
    soon as affordable, with next price c1*r**(k-1) at k owned and income p*k (no multipliers in range):

        T_K = (c1/p) * sum_{j=1}^{K-1} r**(j-1)/j        (K >= 1; T_1 = 0)
    """
    _req(c1 > 0 and p > 0, "c1 and p must be > 0")
    _req(r >= 1, "r must be >= 1")
    k_target = _count(k_target, "K")
    _req(k_target >= 1, "K starts at 1 (the first producer is owned)")
    s = sum((_div(r ** (j - 1), j) for j in range(1, k_target)), 0)
    return _div(c1, p) * s


# ---------------------------------------------------------------- prestige

def floor_power(a, x, alpha: Fraction) -> int:
    """Exact floor(a * x**alpha) for a > 0, x >= 0 and rational alpha = p/q > 0 (inequality-checked).

    n <= a*x**(p/q)  <=>  (n/a)**q <= x**p  for n >= 0.
    """
    _req(a > 0, "a must be > 0")
    _req(x >= 0, "x must be >= 0")
    alpha = Fraction(alpha)
    _req(alpha > 0, "alpha must be > 0")
    p, q = alpha.numerator, alpha.denominator
    a, x = Fraction(a), Fraction(x)

    def ok(n: int) -> bool:
        return (Fraction(n) / a) ** q <= x ** p

    est = float(a) * float(x) ** float(alpha) if x else 0.0
    n = int(est) if math.isfinite(est) else 0
    while n > 0 and not ok(n):
        n -= 1
    while ok(n + 1):
        n += 1
    return n


def power_entitlement(a, x, alpha):
    """F(x) = a * x**alpha (float unless alpha is an integer); a > 0, alpha > 0, x >= 0."""
    _req(a > 0 and alpha > 0 and x >= 0, "power entitlement needs a > 0, alpha > 0, x >= 0")
    return a * _pow(x, alpha)


def input_multiplier_for_entitlement(z, alpha):
    """For F = A*x**alpha: reaching z times the entitlement needs z**(1/alpha) times the input (before rounding)."""
    _req(z > 0 and alpha > 0, "z and alpha must be > 0")
    return _pow(z, _div(1, alpha))


def adventure_capitalist_prestige(lifetime) -> float:
    """Historical published model (C01, 2017-01-12): p = 150*sqrt(L/1e15), L = lifetime earnings. Float."""
    _req(lifetime >= 0, "lifetime earnings must be >= 0")
    return 150 * math.sqrt(float(lifetime) / 1e15)


def adventure_capitalist_prestige_floor(lifetime) -> int:
    """Exact floor of the C01 AdVenture Capitalist model."""
    return floor_power(150, Fraction(lifetime) / 10 ** 15, Fraction(1, 2))


def cookie_clicker_prestige(lifetime) -> float:
    """Historical published model (C01, 2017-01-12): p = (L/1e12)**(1/3), L = lifetime earnings. Float."""
    _req(lifetime >= 0, "lifetime earnings must be >= 0")
    return (float(lifetime) / 1e12) ** (1 / 3)


def cookie_clicker_prestige_floor(lifetime) -> int:
    """Exact floor of the C01 Cookie Clicker model."""
    return floor_power(1, Fraction(lifetime) / 10 ** 12, Fraction(1, 3))


def realm_grinder_prestige(maximum) -> float:
    """Historical published model (C01, 2017-01-12): p = (sqrt(1 + 8M/1e12) - 1)/2, M = maximum earnings."""
    _req(maximum >= 0, "maximum earnings must be >= 0")
    return (math.sqrt(1 + 8 * float(maximum) / 1e12) - 1) / 2


def triangular_root_floor(x) -> int:
    """Exact floor((sqrt(1 + 8x) - 1)/2) = the largest n with n(n+1)/2 <= x, for x >= 0."""
    _req(x >= 0, "x must be >= 0")
    m = math.floor(Fraction(x))
    n = (math.isqrt(8 * m + 1) - 1) // 2  # n(n+1)/2 <= floor(x) <=> n(n+1)/2 <= x for integer n
    return n


def realm_grinder_prestige_floor(maximum) -> int:
    """Exact floor of the C01 Realm Grinder model."""
    return triangular_root_floor(Fraction(maximum) / 10 ** 12)


def award_total_entitlement(entitlement_floor: int, already_awarded: int) -> int:
    """Total-entitlement rule: award = max(0, floor(F(L)) - already_awarded). Spent prestige is not subtracted."""
    _count(entitlement_floor, "floor(F)")
    _count(already_awarded, "already_awarded")
    return max(0, int(entitlement_floor) - int(already_awarded))


def award_per_run(run_value) -> int:
    """Per-run rule: award = floor(G(R)), G(R) >= 0."""
    _req(run_value >= 0, "G(R) must be >= 0")
    return math.floor(run_value)


# ---------------------------------------------------------------- offline earnings

def offline_earned(efficiency, rate_saved, elapsed_s, *, cap_s):
    """Frozen-rate offline reward: eta * P_saved * min(max(elapsed, 0), cap). cap_s is required (keyword);
    pass cap_s=None only when the approved design says offline accumulation is uncapped.

    0 <= eta; P_saved >= 0 per second. Not valid if production, boosts or auto-buys change during the absence.
    """
    _req(efficiency >= 0, "efficiency must be >= 0")
    _req(rate_saved >= 0, "saved rate must be >= 0")
    dt = max(elapsed_s, 0)
    if cap_s is not None:
        _req(cap_s >= 0, "cap must be >= 0")
        dt = min(dt, cap_s)
    return efficiency * rate_saved * dt


# ---------------------------------------------------------------- combat

def hits_to_kill(hp, damage) -> int:
    """N = ceil(H/d) for H > 0 hit points and d > 0 effective damage per hit."""
    _req(hp > 0, f"H must be > 0, got {hp}")
    _req(damage > 0, f"d must be > 0, got {damage}")
    return math.ceil(_div(hp, damage))


def time_to_kill(n_hits, interval_s, first_hit_s):
    """TTK = t0 + (N - 1)*tau seconds, N >= 1 hits, tau > 0, t0 >= 0 (0 = immediate, tau = one wind-up)."""
    n = _count(n_hits, "N")
    _req(n >= 1, "N must be >= 1")
    _req(interval_s > 0, "tau must be > 0")
    _req(first_hit_s >= 0, "t0 must be >= 0")
    return first_hit_s + (n - 1) * interval_s


def first_hit_offset(interval_s, convention: str):
    """t0 for a first-hit convention: 'immediate' -> 0, 'after_interval' -> tau."""
    _req(convention in ("immediate", "after_interval"), f"unknown first-hit convention {convention!r}")
    return 0 if convention == "immediate" else interval_s


def hits_for_sequence(hp, damages: Iterable):
    """Smallest n with d_1 + ... + d_n >= H for a finite damage sequence; UNREACHABLE-style None if never."""
    _req(hp > 0, "H must be > 0")
    total = 0
    for i, d in enumerate(damages, start=1):
        _req(d >= 0, "damage values must be >= 0")
        total += d
        if total >= hp:
            return i
    return None


def effective_health(hp, reduction):
    """H / (1 - rho) for damage-fraction reduction 0 <= rho < 1."""
    _req(hp >= 0, "H must be >= 0")
    _req(0 <= reduction < 1, f"rho must satisfy 0 <= rho < 1, got {reduction}")
    return _div(hp, 1 - reduction)


def stack_bonus(additive: Sequence = (), multiplicative: Sequence = ()):
    """Total bonus (1 + sum(additive)) * prod(1 + m) - 1. Additive bonuses share one bucket; each
    multiplicative bonus is its own factor. Example (M06): additive [18/100], multiplicative [1/5] -> 52/125.
    """
    total = 1 + sum(additive, 0)
    for m in multiplicative:
        total = total * (1 + m)
    _req(total >= 0, "stacked multiplier below zero")
    return total - 1


# ---------------------------------------------------------------- paid random (independent, constant p)

def _prob(p, name="p"):
    _req(0 < p < 1, f"{name} must be in (0, 1), got {p}")


def expected_spend(cost, p):
    """Expected spend to the first success, c/p, for independent tries at constant 0 < p < 1 (no pity)."""
    _req(cost >= 0, "cost must be >= 0")
    _prob(p)
    return _div(cost, p)


def p_success_within(n, p):
    """P(at least one success in n tries) = 1 - (1-p)**n, independent tries, constant 0 < p < 1."""
    _prob(p)
    return 1 - (1 - p) ** _count(n)


def attempts_for_quantile(q, p) -> int:
    """n_q = ceil(log(1-q)/log(1-p)): least tries with P(success) >= q; 0 < q < 1, 0 < p < 1.

    The log estimate is checked and corrected with the exact inequality 1 - (1-p)**n >= q.
    """
    _prob(p)
    _prob(q, "q")
    n = max(1, math.ceil(math.log(1 - float(q)) / math.log(1 - float(p))))
    while n > 1 and p_success_within(n - 1, p) >= q:
        n -= 1
    while p_success_within(n, p) < q:
        n += 1
    return n


def p_success_within_conditional(success_probs: Sequence):
    """Pity / hard-guarantee variant: P(success by try n) = 1 - prod(1 - s_i) over the actual conditional
    success probability s_i of try i given all earlier tries failed (s_i = 1 is a hard guarantee)."""
    fail = 1
    for s in success_probs:
        _req(0 <= s <= 1, f"conditional probabilities must be in [0, 1], got {s}")
        fail = fail * (1 - s)
    return 1 - fail


def expected_tries_conditional(success_probs: Sequence):
    """Expected tries to the first success when try i succeeds with conditional probability s_i; the
    sequence must end with a hard guarantee (s_last = 1) so the expectation is finite."""
    _req(len(success_probs) >= 1 and success_probs[-1] == 1, "the sequence must end with a guarantee (1)")
    e, reach = 0, 1
    for s in success_probs:
        _req(0 <= s <= 1, "conditional probabilities must be in [0, 1]")
        e = e + reach
        reach = reach * (1 - s)
    return e


def _self_check() -> int:
    r = Fraction(107, 100)
    waits = [exponential(4, r, k - 1) / (Fraction(167, 100) * k) for k in range(1, 6)]
    print("Lemonade waits:", ", ".join(str(w) for w in waits))
    print("T_6 closed form:", sequential_reinvest_time(4, r, Fraction(167, 100), 6))
    print("Stacking (1.18)(1.2)-1:", stack_bonus([Fraction(18, 100)], [Fraction(1, 5)]))
    return 0


if __name__ == "__main__":
    raise SystemExit(_self_check())
