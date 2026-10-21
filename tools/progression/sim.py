#!/usr/bin/env python3
"""Progression simulator: plays one named model player (a policy) through a game's data tables (one JSON
model file) and reports the timeline - time to each goal in active and calendar time, soft and hard walls,
power spikes, blocked paths, the per-currency ledger and numeric precision flags.

Kit tool (universal, Studio Kit). Python 3.11+ standard library only. Curve maths: curves.py next to this file.

What it never claims:
  - A run is ONE modelled strategy, not the player population, and not a forecast of real pacing.
  - A goal inside its window is "pass" for arithmetic only; it is never a verdict that the game is fun.
  - The tool never fills a missing number: no default earning rate, session length, wall or spike
    threshold, horizon, offline cap or efficiency. A missing required number is an error; a missing
    analysis threshold means "not evaluated".
  - A policy named greedy-roi is a heuristic; no policy is called optimal.

Definitions used in the report:
  goal         a model-declared predicate (own N of X, own item, reach level L, defeat B, complete A,
               unlock U, prestige count P, balance/lifetime/run earnings >= C, active time >= T, at least N
               soft walls so far, at least N spikes on metric M so far; combined with all/any/not) with an
               optional window {basis: active|calendar, min_s, max_s}. Verdict per goal: pass (measured time
               inside the declared window), fail (outside, or never reached because the path is blocked),
               not testable (no window; calendar window without a session model; run ended by the horizon
               or event limit before the window closed). A wall or spike goal is reached when the wall's step
               completes (its end) or the spike's change happens; it needs a declared threshold (else error).
  step         a state change the player works toward: a purchase, a level-up, a first defeat, a first
               activity completion, a prestige. Its wait = active seconds since the previous step.
  soft wall    a step whose wait >= the declared min_wait_s, or >= min_ratio_to_previous x the wait of the
               previous step with a non-zero wait. Thresholds come from the model (analysis.soft_wall) or the
               CLI; with none, walls are "not evaluated" and the slowest steps are listed ranked.
  hard wall    for every policy: per gated id (a buyable producer or item, or an enemy, with "requires"), the
               interval from the first instant it is affordable (enemy: the preview duel is a win) while its
               prerequisite is false, until the prerequisite holds; with the missing predicate, the condition,
               and whether the policy was pursuing it. An activity counts only while the policy pursues it (a
               chain of stages alone is ordinary sequencing). Open at the run end = "open_at_end". "gate"
               says which kind: "prerequisite" (a real gate), "chained" (it names a gated id that is itself
               still locked; "via" lists them), "timed" (the prerequisite tests active_s), "activity" (a
               pursued activity). "unlocked U" is read through U's own predicate for both tests.
  power spike  a change between consecutive measured states in a declared reference metric on unchanged
               reference content: hits_to_kill / ttk_s (the player against a named enemy, lower is better),
               hits_to_die / ttd_s (the enemy against the player, higher is better), production_per_s of a
               currency (higher is better); a spike when the improvement >= min_change or the improvement
               ratio >= min_ratio (declared per metric). active_when (a predicate) limits measuring to content
               the player can reach; a metric that becomes active starts a new segment (no change is measured
               across the inactive gap). Without a threshold: "not evaluated", changes listed.
  blocked path a goal not reached, with a reason: "unreachable: zero income", "prerequisite missing",
               "cap below cost", "found only" (an item with no price; the detail names its drops and level
               rewards), "cannot win duel", "no eligible purchase", "horizon reached", "event limit reached".

Time semantics (declared by the model in meta.time and recorded in the report):
  continuous   rates are piecewise constant between events; the simulator advances exactly to the next
               event (purchase affordable, activity end, predicate threshold, session end, horizon).
               Producers that produce producers are rejected in this mode (the rate would not be
               piecewise constant; use the closed form or discrete ticks).
  discrete     fixed ticks of tick_s seconds; production per tick uses the counts at the start of the tick,
               unless new_units_produce_in_creation_tick is true, in which case producers are processed in
               model order and a count raised earlier in the tick produces in the same tick. Activities end
               at the first tick boundary at or after their duration; sessions end likewise.
  event order  meta.event_order is a permutation of the six phases produce, rewards, caps, purchase, unlock
               and reset (there is no "run" phase); they run at every event instant (continuous: production
               accrues between instants, the other phases run in the declared order; a state change after
               the purchase phase re-runs the instant). "purchase" is the policy's decision phase (buys, starts a fight or an activity).
               A purchase that costs 0 is taken at most once per instant (no endless free loop).
  levels       a level-up is an event at its exact time, also when XP comes from production. levels.rewards
               grant currencies (ledger source level_reward:<L>) and items once per level per simulated player.
  combat       a discrete duel per fight: both sides' hit times (first hit at 0 or after one interval, per
               meta.duel), damage after mitigation, simultaneous-hit priority (player_first, enemy_first or
               both; "both" with two deaths is "mutual", not a win). The fight stops at the actual death
               event; a killed enemy does not land its next strike. Both sides start each fight at full HP;
               recovery, travel and respawn are the enemy's declared overhead_s, so a defeat's goal time
               includes overhead_s. Preview margin: a win -> the player's HP left / HP; a loss -> -(the
               enemy's HP left / HP). With policies.boss_attempt a boss is attempted when the margin >=
               min_margin, a lost fight adds recovery_s, and after a loss the same stats (level and items) do
               not retry unless the player's accuracy is random. report.fights.per_enemy counts fights (=
               attempts), wins, losses and attempts_to_first_win.
  prestige     the reset fires when take_when holds and the award >= min_award (when declared). Offline
               income counts toward the basis and the take_when counters unless
               prestige.offline_counts_toward_basis is false (default true, recorded in the report).
  calendar     only with a session pattern (--sessions): active_s per session and gaps between sessions
               (gaps_s cycled; absences replace the gap after a named session); offline earnings follow the
               model's offline contract (eta * rate at exit * min(gap, cap)) only when it gives one, and
               arrive in the rewards phase when the next session starts.

Policies (each a named stress scenario; ties go to model order):
  buy-next-in-order  works through policies.order (default: purchasables in model order): buys a producer
                     or item as soon as affordable, fights an enemy until first defeated (only if the
                     preview duel is a win), repeats an activity until it first succeeds. An entry
                     {"id": X, "until": N} finishes at N owned (producer), N wins or N completions; a
                     producer without "until" is never finished. A found-only item is pursued by fighting
                     an enemy that drops it.
  cheapest-eligible  buys the lowest-priced purchasable whose prerequisite holds (prices are compared by
                     amount, whatever the currency), waiting for it if needed.
  greedy-roi         buys the purchasable with the largest immediate production gain per price in
                     policies.objective_currency; falls back to cheapest-eligible when nothing adds income.
  save-for           pursues --target only (waits, fights or repeats for it), then cheapest-eligible. While
                     the target is locked, unaffordable or not beatable, it keeps fighting the enemy with
                     the most of the target's price currency (else policies.objective_currency) per second,
                     when the model has enemies; it buys nothing else.
  fight-best         buys any affordable eligible purchasable (cheapest first), fights an undefeated
                     beatable boss first, otherwise the beatable enemy with the most
                     policies.objective_currency per second (duel time + overhead_s). Enemies marked
                     "once" are not fought again after their first defeat.
  grind-to-level     fight-best, but bosses are skipped until --target-level is reached.
  "Beatable" is the policy's preview duel with every attack landing; --skill changes the player's
  attack delay, damage factor and accuracy in previews and fights alike (accuracy only in fights).

Provenance: every number in the model is {"v": number | "p/q" | [numbers], "src": label} with label one of
published:<source id>, owner:<decision id>, measured:<dataset>, EXAMPLE ASSUMPTION, PROPOSAL. A bare number
is an error. Inputs labelled EXAMPLE ASSUMPTION or PROPOSAL are listed under assumptions; every result of a
run is conditional on all of them (the tool does not trace which result uses which input).

Model file (JSON; every number a value object as above; ids unique across producers, items, enemies,
activities):
  meta        revision (required), title, event_order, time {mode, tick_s, new_units_produce_in_creation_tick},
              duel {player_first_hit immediate|after_interval, enemy_first_hit, simultaneous}
  currencies  {id: {start, cap?, smallest_unit?}}
  producers   {id: {start_owned, produces {"currency:<id>"|"producer:<id>": per unit per second},
              cost? {currency, curve (curves.evaluate spec), index_offset? (n = owned + offset),
              rounding? none|floor|ceil|half_even}, milestones? [{owned, mult}], requires?}}
  items       {id: {cost? {currency, amount, rounding?}, requires?, effects [{target stat:<name> |
              producer:<id> | currency:<id>, op add|add_pct|mul (producer/currency: mul only), value}]}}
              stat = (base + sum add) * (1 + sum add_pct) * prod mul; no cost = found only (drops)
  levels      {currency, max_level, per_level curve at n = level + index_offset (XP from l to l+1) or
              cumulative [X_1 = 0, ...], rewards? [{level, currencies? {currency: amount}, items? [ids]}]};
              level = the largest l with X_l <= that currency's balance
  player      {stats {hp, attack, attack_interval_s, mitigation?}: curve at n = level + index_offset}
  enemies     {id: {hp, damage, attack_interval_s, overhead_s, mitigation?, rewards {currency: amount},
              drops? [{item, chance}], requires?, boss?, once?}}
  activities  {id: {duration_s, success_chance?, rewards?, requires?}}
  unlocks     {id: {when}}
  prestige    {basis_currency, basis lifetime|maximum|run, rule total_entitlement|per_run, award_currency,
              formula {kind power, a, alpha, divisor: floor(a*(x/divisor)**alpha)} or {kind triangular_root,
              divisor: floor((sqrt(1 + 8x/divisor) - 1)/2)}, take_when, reset [state ids], keep [state ids]
              (every state id in exactly one list), bonus? {target currency:<id>, per_unit}: rate x
              (1 + per_unit * award balance), min_award? (no reset for a smaller award),
              offline_counts_toward_basis? (true|false, default true)}
  offline     {efficiency, cap_s (null only when the design says uncapped), currencies [ids]}
  sessions    {patterns {name: {active_s, gaps_s [...], absences? [{after_session, gap_s}]}}}
  skill_profiles {name: {extra_attack_delay_s?, damage_factor?, accuracy?}}
  policies    {order? [id | {id, until}], objective_currency?, boss_attempt? {min_margin (-1..1), recovery_s}}
  goals       [{id, label?, when, window? {basis active|calendar, min_s?, max_s?}}]
  analysis    {soft_wall? {min_wait_s?, min_ratio_to_previous?}, spikes? [{id, metric hits_to_kill|ttk_s|
              hits_to_die|ttd_s|production_per_s, enemy | currency, min_change?, min_ratio?, active_when?}]}
  run         {horizon_active_s}
  Predicates: {"owned": [producer, N]} {"item": id} {"level": L} {"defeated": id} {"completed": id}
  {"unlocked": id} {"prestiges": P} {"balance"|"lifetime"|"run": [currency, C]} {"active_s": T}
  {"soft_walls": N} {"soft_walls": [N, {"after": predicate}]} (walls whose step starts at or after the
  first time the predicate held) {"spikes": [metric id, N]} {"hard_wall": id} (a hard wall on id has started;
  read from walls.hard, so the goal time equals the wall start) {"all": [...]} {"any": [...]}
  {"not": predicate}.
  Any predicate number may instead be {"curve": spec, "index": "prestiges", "index_offset"?}: the threshold
  is evaluated at n = prestige count + offset (e.g. a rebirth requirement that grows with each rebirth).
  State ids: currency:, producer:, item:, unlock:, defeated:, completed:<id>.

Ledger per currency: end = start + sources - sinks + adjustments (cap_loss, reset, float_rounding in float
mode); residual reported, exactly 0 in exact mode. Float mode books float_rounding whenever a grant or a
sink changes the balance by a different amount than booked (e.g. a 3-coin sink absorbed at 4e17).
Precision: flags a currency whose maximum reached value (balance, lifetime or run counter) exceeds 2**53, or
where adding its declared smallest_unit does not change a float at that magnitude. Float mode compares
balances with prices and thresholds with a relative 1e-9 tolerance; exact mode compares exactly.

Report size: --lean drops the event trace, keeps steps only at resets, goals, soft walls and spikes, and
metric histories only at segment starts, spikes and the last value; --lean-steps N also keeps the first N
steps in full (the early "waits shrink, then grow" pattern); the report says so ("lean"). Continuous
exact mode with exponential prices builds fractions with many digits; long incremental runs are smaller in
discrete ticks.

Usage:
  python tools/progression/sim.py MODEL.json --policy buy-next-in-order [--mode exact|float]
      [--target ID] [--target-level L] [--skill PROFILE] [--sessions PATTERN] [--seed N --runs N]
      [--horizon-s S] [--soft-wall-s S] [--soft-wall-ratio K] [--top 10] [--max-events N]
      [--out report.json] [--trace-out trace.json] [--lean [--lean-steps N]]
  Policies: buy-next-in-order, cheapest-eligible, greedy-roi, save-for (--target), fight-best,
            grind-to-level (--target-level). --skill applies a model skill profile (e.g. a struggling
            player); --sessions picks a model session pattern (e.g. returning after an absence).
  Randomness (drop chances, activity success chances, skill accuracy below 1) requires --seed and --runs;
  a model without random inputs rejects --runs > 1. Proportions get a Wilson 95 % interval (NIST).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import statistics
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import curves as cv  # noqa: E402

VERSION = "1.2.0"
PHASES = ("produce", "rewards", "caps", "purchase", "unlock", "reset")
ASSUMED_LABELS = ("EXAMPLE ASSUMPTION", "PROPOSAL")
POLICIES = ("buy-next-in-order", "cheapest-eligible", "greedy-roi", "save-for", "fight-best", "grind-to-level")
PRED_KEYS = ("owned", "item", "level", "defeated", "completed", "unlocked", "prestiges", "balance", "lifetime",
             "run", "active_s", "soft_walls", "spikes", "hard_wall", "all", "any", "not")
METRICS = ("hits_to_kill", "ttk_s", "hits_to_die", "ttd_s", "production_per_s")
LOWER_IS_BETTER = ("hits_to_kill", "ttk_s")
OUTCOME_KEY = {"win": "won", "loss": "lost", "mutual": "mutual"}
Z95 = 1.959963984540054  # two-sided 95 % normal quantile for the Wilson score interval
TWO_53 = 2 ** 53
FLOAT_REL_TOL = 1e-9  # float mode only: comparison tolerance for balances against prices and thresholds
LABEL_RE = re.compile(r"^(published|owner|measured):\S.*$")


class ModelError(ValueError):
    """The model file is incomplete or inconsistent; the message names the path."""


# ---------------------------------------------------------------- loading and provenance

def _num(x, path: str, exact: bool):
    if isinstance(x, bool) or x is None:
        raise ModelError(f"{path}: expected a number, got {x!r}")
    if isinstance(x, str):
        try:
            x = Fraction(x.strip())
        except (ValueError, ZeroDivisionError) as e:
            raise ModelError(f"{path}: {x!r} is not a number") from e
    if isinstance(x, float):
        if not math.isfinite(x):
            raise ModelError(f"{path}: non-finite number")
        x = Fraction(x)
    if not isinstance(x, (int, Fraction)):
        raise ModelError(f"{path}: expected a number, got {x!r}")
    return Fraction(x) if exact else float(x)


def _label(src, path: str) -> str:
    if not isinstance(src, str) or not (src in ASSUMED_LABELS or LABEL_RE.match(src)):
        raise ModelError(f"{path}: provenance {src!r} must be published:<id>, owner:<decision id>, "
                         f"measured:<dataset>, EXAMPLE ASSUMPTION or PROPOSAL")
    return src


def unwrap(node, path: str, exact: bool, inputs: list):
    """Replace every {"v", "src"} value object by its number(s); record each in `inputs`; reject bare numbers."""
    if isinstance(node, dict):
        if "v" in node and "src" in node and set(node) <= {"v", "src", "note"}:
            src = _label(node["src"], path)
            v = node["v"]
            val = [_num(x, f"{path}[{i}]", exact) for i, x in enumerate(v)] if isinstance(v, list) \
                else _num(v, path, exact)
            inputs.append({"input": path, "src": src, "value": val})
            return val
        return {k: unwrap(v, f"{path}.{k}" if path else k, exact, inputs) for k, v in node.items()}
    if isinstance(node, list):
        return [unwrap(x, f"{path}[{i}]", exact, inputs) for i, x in enumerate(node)]
    if isinstance(node, (bool, str)) or node is None:
        return node
    raise ModelError(f"{path}: number {node} has no provenance label; write {{\"v\": {node}, \"src\": ...}}")


def read_model(path) -> tuple[dict, str]:
    data = Path(path).read_bytes()
    raw = json.loads(data.decode("utf-8"), parse_float=Fraction)
    return raw, hashlib.sha256(data).hexdigest()


def _req(cond, msg):
    if not cond:
        raise ModelError(msg)


# ---------------------------------------------------------------- model validation

class Model:
    """Unwrapped, validated model tables. All numbers are Fraction (exact) or float (float mode)."""

    def __init__(self, raw: dict, exact: bool):
        self.exact = exact
        self.inputs: list = []
        m = unwrap(raw, "", exact, self.inputs)
        self.m = m
        meta = m.get("meta") or {}
        _req(isinstance(meta.get("revision"), str) and meta["revision"], "meta.revision (string) is required")
        self.revision = meta["revision"]
        self.title = meta.get("title", "")
        order = meta.get("event_order")
        _req(isinstance(order, list) and sorted(order) == sorted(PHASES) and len(order) == len(PHASES),
             f"meta.event_order must be a permutation of {list(PHASES)}")
        self.event_order = order
        tm = meta.get("time") or {}
        _req(tm.get("mode") in ("continuous", "discrete"), "meta.time.mode must be continuous or discrete")
        self.time = tm
        if tm["mode"] == "discrete":
            _req("tick_s" in tm and tm["tick_s"] > 0, "meta.time.tick_s (> 0) is required in discrete mode")
            _req(isinstance(tm.get("new_units_produce_in_creation_tick"), bool),
                 "meta.time.new_units_produce_in_creation_tick (true/false) is required in discrete mode")
        self.currencies = m.get("currencies") or {}
        _req(self.currencies, "currencies: at least one currency is required")
        for c, d in self.currencies.items():
            _req("start" in d, f"currencies.{c}.start is required")
        self.producers = m.get("producers") or {}
        self.items = m.get("items") or {}
        self.enemies = m.get("enemies") or {}
        self.activities = m.get("activities") or {}
        self.unlocks = m.get("unlocks") or {}
        self.levels = m.get("levels")
        self.player = m.get("player")
        self.prestige = m.get("prestige")
        self.offline = m.get("offline")
        self.sessions = (m.get("sessions") or {}).get("patterns") or {}
        self.skills = m.get("skill_profiles") or {}
        self.policy_cfg = m.get("policies") or {}
        self.goals = m.get("goals") or []
        self.analysis = m.get("analysis") or {}
        self.run_cfg = m.get("run") or {}
        self.duel_cfg = meta.get("duel")
        self._validate()
        self.after_preds = []
        for p in self.all_preds():
            self._collect_after(p)

    def all_preds(self):
        out = [g["when"] for g in self.goals] + [u["when"] for u in self.unlocks.values()]
        out += [t[i]["requires"] for t in (self.producers, self.items, self.enemies, self.activities) for i in t
                if "requires" in t[i]]
        out += [sp["active_when"] for sp in self.analysis.get("spikes", []) if "active_when" in sp]
        return out + ([self.prestige["take_when"]] if self.prestige else [])

    def _collect_after(self, p):
        (k, a), = p.items()
        if k in ("all", "any"):
            for q in a:
                self._collect_after(q)
        elif k == "not":
            self._collect_after(a)
        elif k == "soft_walls" and isinstance(a, list) and a[1]["after"] not in self.after_preds:
            self.after_preds.append(a[1]["after"])

    # ids -------------------------------------------------------------
    def kind_of(self, i: str) -> str | None:
        for kind, table in (("producer", self.producers), ("item", self.items), ("enemy", self.enemies),
                            ("activity", self.activities)):
            if i in table:
                return kind
        return None

    def state_ids(self) -> list[str]:
        return ([f"currency:{c}" for c in self.currencies] + [f"producer:{p}" for p in self.producers]
                + [f"item:{i}" for i in self.items] + [f"unlock:{u}" for u in self.unlocks]
                + [f"defeated:{e}" for e in self.enemies] + [f"completed:{a}" for a in self.activities])

    def _cur(self, c, path):
        _req(c in self.currencies, f"{path}: unknown currency {c!r}")

    def check_threshold(self, x, path):
        """A predicate number, or {"curve": spec, "index": "prestiges", "index_offset"?} that grows with the
        prestige count (n = prestiges + index_offset)."""
        if isinstance(x, dict):
            _req(set(x) <= {"curve", "index", "index_offset"} and "curve" in x and x.get("index") == "prestiges",
                 f"{path}: a threshold object is {{\"curve\": spec, \"index\": \"prestiges\", \"index_offset\"?}}")
            _req(x["curve"].get("kind") in ("table", *cv.CURVE_KINDS), f"{path}.curve.kind unknown")
        else:
            _req(isinstance(x, (int, float, Fraction)) and not isinstance(x, bool), f"{path}: expected a number")

    def check_pred(self, p, path):
        _req(isinstance(p, dict) and len(p) == 1, f"{path}: a predicate is one-key object, one of {PRED_KEYS}")
        (k, a), = p.items()
        _req(k in PRED_KEYS, f"{path}: unknown predicate {k!r}")
        if k in ("all", "any"):
            _req(isinstance(a, list) and a, f"{path}.{k}: needs a non-empty list")
            for i, q in enumerate(a):
                self.check_pred(q, f"{path}.{k}[{i}]")
        elif k == "not":
            self.check_pred(a, f"{path}.not")
        elif k == "soft_walls" and isinstance(a, list):
            _req(len(a) == 2 and isinstance(a[1], dict) and set(a[1]) == {"after"},
                 f"{path}: soft_walls is N or [N, {{\"after\": predicate}}]")
            self.check_threshold(a[0], f"{path}.soft_walls[0]")
            self.check_pred(a[1]["after"], f"{path}.soft_walls[1].after")
        elif k in ("level", "prestiges", "active_s", "soft_walls"):
            self.check_threshold(a, f"{path}.{k}")
        elif k == "hard_wall":
            _req(self.kind_of(a) is not None, f"{path}: hard_wall needs a producer, item, enemy or activity id")
        elif k == "spikes":
            _req(isinstance(a, list) and len(a) == 2 and a[0] in {s.get("id") for s in self.analysis.get("spikes", [])},
                 f"{path}: spikes [spike metric id, N]")
            self.check_threshold(a[1], f"{path}.spikes[1]")
        elif k == "owned":
            _req(isinstance(a, list) and len(a) == 2 and a[0] in self.producers, f"{path}: owned [producer, N]")
            self.check_threshold(a[1], f"{path}.owned[1]")
        elif k == "item":
            _req(a in self.items, f"{path}: unknown item {a!r}")
        elif k == "defeated":
            _req(a in self.enemies, f"{path}: unknown enemy {a!r}")
        elif k == "completed":
            _req(a in self.activities, f"{path}: unknown activity {a!r}")
        elif k == "unlocked":
            _req(a in self.unlocks, f"{path}: unknown unlock {a!r}")
        elif k in ("balance", "lifetime", "run"):
            _req(isinstance(a, list) and len(a) == 2, f"{path}: {k} [currency, amount]")
            self._cur(a[0], path)
            self.check_threshold(a[1], f"{path}.{k}[1]")
        if k == "level":
            _req(self.levels is not None, f"{path}: level predicate needs a levels table")

    def _validate(self):
        seen = {}
        for kind, table in (("producer", self.producers), ("item", self.items), ("enemy", self.enemies),
                            ("activity", self.activities)):
            for i in table:
                _req(i not in seen, f"id {i!r} is used by both a {seen.get(i)} and a {kind}; ids must be unique")
                seen[i] = kind
        for pid, p in self.producers.items():
            path = f"producers.{pid}"
            _req("start_owned" in p, f"{path}.start_owned is required")
            cost = p.get("cost")
            if cost is not None:  # a producer without cost is never bought (e.g. a fixed starting generator)
                _req("currency" in cost and "curve" in cost, f"{path}.cost needs currency and curve")
                self._cur(cost["currency"], f"{path}.cost")
                _req(cost.get("rounding", "none") in cv.ROUNDING_RULES, f"{path}.cost.rounding unknown")
            _req(p.get("produces"), f"{path}.produces is required")
            for tgt in p["produces"]:
                kind, _, tid = tgt.partition(":")
                _req((kind == "currency" and tid in self.currencies) or (kind == "producer" and tid in self.producers),
                     f"{path}.produces: {tgt!r} must be currency:<id> or producer:<id>")
                if kind == "producer":
                    _req(self.time["mode"] == "discrete",
                         f"{path}: a producer that produces producers makes rates non-constant; continuous mode "
                         f"integrates only piecewise-constant rates. Use discrete ticks or the closed form.")
            for i, ms in enumerate(p.get("milestones", [])):
                _req("owned" in ms and "mult" in ms, f"{path}.milestones[{i}] needs owned and mult")
            if "requires" in p:
                self.check_pred(p["requires"], f"{path}.requires")
        for iid, it in self.items.items():
            path = f"items.{iid}"
            if "cost" in it:
                _req("currency" in it["cost"] and "amount" in it["cost"], f"{path}.cost needs currency and amount")
                self._cur(it["cost"]["currency"], f"{path}.cost")
                _req(it["cost"].get("rounding", "none") in cv.ROUNDING_RULES, f"{path}.cost.rounding unknown")
            for j, ef in enumerate(it.get("effects", [])):
                tgt, op = ef.get("target", ""), ef.get("op")
                kind, _, tid = tgt.partition(":")
                _req("value" in ef, f"{path}.effects[{j}].value is required")
                if kind == "stat":
                    _req(op in ("add", "add_pct", "mul"), f"{path}.effects[{j}].op must be add, add_pct or mul")
                else:
                    _req((kind == "producer" and tid in self.producers) or (kind == "currency" and tid in self.currencies),
                         f"{path}.effects[{j}].target {tgt!r} must be stat:<name>, producer:<id> or currency:<id>")
                    _req(op == "mul", f"{path}.effects[{j}]: producer and currency effects support op mul only")
            if "requires" in it:
                self.check_pred(it["requires"], f"{path}.requires")
        if self.enemies:
            _req(self.player and "stats" in self.player, "player.stats is required when enemies exist")
            for s in ("hp", "attack", "attack_interval_s"):
                _req(s in self.player["stats"], f"player.stats.{s} is required when enemies exist")
            _req(self.levels is not None, "levels are required when enemies exist (stats are per level)")
            d = self.duel_cfg or {}
            _req(d.get("player_first_hit") in ("immediate", "after_interval")
                 and d.get("enemy_first_hit") in ("immediate", "after_interval"),
                 "meta.duel.player_first_hit and enemy_first_hit must be immediate or after_interval")
            _req(d.get("simultaneous") in ("player_first", "enemy_first", "both"),
                 "meta.duel.simultaneous must be player_first, enemy_first or both")
        for eid, e in self.enemies.items():
            path = f"enemies.{eid}"
            for f in ("hp", "damage", "attack_interval_s", "overhead_s"):
                _req(f in e, f"{path}.{f} is required (overhead_s = time between fights: travel, respawn, "
                             f"recovery; it may be 0 but must be declared)")
            _req(e["hp"] > 0 and e["attack_interval_s"] > 0, f"{path}: hp and attack_interval_s must be > 0")
            _req(0 <= e.get("mitigation", 0) < 1, f"{path}.mitigation must be in [0, 1)")
            for c in e.get("rewards", {}):
                self._cur(c, f"{path}.rewards")
            for j, dr in enumerate(e.get("drops", [])):
                _req(dr.get("item") in self.items and 0 <= dr.get("chance", -1) <= 1,
                     f"{path}.drops[{j}] needs a known item and chance in [0, 1]")
            if "requires" in e:
                self.check_pred(e["requires"], f"{path}.requires")
        for aid, a in self.activities.items():
            path = f"activities.{aid}"
            _req("duration_s" in a and a["duration_s"] > 0, f"{path}.duration_s (> 0) is required")
            _req(0 <= a.get("success_chance", 1) <= 1, f"{path}.success_chance must be in [0, 1]")
            for c in a.get("rewards", {}):
                self._cur(c, f"{path}.rewards")
            if "requires" in a:
                self.check_pred(a["requires"], f"{path}.requires")
        for uid, u in self.unlocks.items():
            _req("when" in u, f"unlocks.{uid}.when is required")
            self.check_pred(u["when"], f"unlocks.{uid}.when")
        if self.levels is not None:
            lv = self.levels
            _req("currency" in lv and "max_level" in lv and ("per_level" in lv or "cumulative" in lv),
                 "levels needs currency, max_level and per_level (curve) or cumulative (list)")
            self._cur(lv["currency"], "levels")
            for j, rw in enumerate(lv.get("rewards", [])):
                _req("level" in rw and 2 <= rw["level"] <= lv["max_level"],
                     f"levels.rewards[{j}].level must be in 2..max_level")
                for c in rw.get("currencies", {}):
                    self._cur(c, f"levels.rewards[{j}].currencies")
                for it in rw.get("items", []):
                    _req(it in self.items, f"levels.rewards[{j}].items: unknown item {it!r}")
        if self.prestige is not None:
            pr = self.prestige
            for f in ("basis_currency", "basis", "formula", "rule", "award_currency", "take_when", "reset", "keep"):
                _req(f in pr, f"prestige.{f} is required")
            self._cur(pr["basis_currency"], "prestige.basis_currency")
            self._cur(pr["award_currency"], "prestige.award_currency")
            _req(pr["basis"] in ("lifetime", "maximum", "run"), "prestige.basis must be lifetime, maximum or run")
            _req(pr["rule"] in ("total_entitlement", "per_run"), "prestige.rule must be total_entitlement or per_run")
            _req(pr["formula"].get("kind") in ("power", "triangular_root"),
                 "prestige.formula.kind must be power (a, alpha, divisor) or triangular_root (divisor)")
            self.check_pred(pr["take_when"], "prestige.take_when")
            if "min_award" in pr:
                _req(pr["min_award"] >= 1, "prestige.min_award must be >= 1")
            _req(isinstance(pr.get("offline_counts_toward_basis", True), bool),
                 "prestige.offline_counts_toward_basis must be true or false")
            ids, reset, keep = set(self.state_ids()), set(pr["reset"]), set(pr["keep"])
            _req(not (reset & keep), f"prestige: ids both reset and kept: {sorted(reset & keep)}")
            _req(reset | keep == ids, f"prestige: every state id must be listed in reset or keep; missing "
                                      f"{sorted(ids - reset - keep)}, unknown {sorted((reset | keep) - ids)}")
        if self.offline is not None:
            _req("efficiency" in self.offline and "cap_s" in self.offline and "currencies" in self.offline,
                 "offline needs efficiency, cap_s (null only if the design says uncapped) and currencies")
        for name, pat in self.sessions.items():
            _req("active_s" in pat and pat["active_s"] > 0 and pat.get("gaps_s"),
                 f"sessions.patterns.{name} needs active_s > 0 and a non-empty gaps_s list")
        ids = set()
        for i, g in enumerate(self.goals):
            _req("id" in g and "when" in g, f"goals[{i}] needs id and when")
            _req(g["id"] not in ids, f"goals[{i}]: duplicate id {g['id']}")
            ids.add(g["id"])
            self.check_pred(g["when"], f"goals[{i}].when")
            w = g.get("window")
            if w is not None:
                _req(w.get("basis") in ("active", "calendar") and ("min_s" in w or "max_s" in w),
                     f"goals[{i}].window needs basis active|calendar and min_s and/or max_s")
        self.order = []
        for j, e in enumerate(self.policy_cfg.get("order", [])):
            i, until = (e, None) if isinstance(e, str) else (e.get("id"), e.get("until"))
            _req(self.kind_of(i) is not None, f"policies.order[{j}]: unknown id {i!r}")
            if until is not None:
                _req(self.kind_of(i) != "item", f"policies.order[{j}]: an item is bought once; 'until' does not apply")
                _req(until >= 1, f"policies.order[{j}].until must be >= 1")
            self.order.append((i, until))
        ba = self.policy_cfg.get("boss_attempt")
        if ba is not None:
            _req("min_margin" in ba and "recovery_s" in ba and -1 <= ba["min_margin"] <= 1 and ba["recovery_s"] >= 0,
                 "policies.boss_attempt needs min_margin in [-1, 1] and recovery_s >= 0")
        ids = set()
        for j, sp in enumerate(self.analysis.get("spikes", [])):
            _req(sp.get("metric") in METRICS and "id" in sp and sp["id"] not in ids,
                 f"analysis.spikes[{j}] needs a unique id and metric {' | '.join(METRICS)}")
            ids.add(sp["id"])
            if sp["metric"] == "production_per_s":
                self._cur(sp.get("currency"), f"analysis.spikes[{j}]")
            else:
                _req(sp.get("enemy") in self.enemies, f"analysis.spikes[{j}].enemy must be a known enemy")
            if "active_when" in sp:
                self.check_pred(sp["active_when"], f"analysis.spikes[{j}].active_when")

    # derived tables ---------------------------------------------------
    def cumulative_xp(self) -> list:
        lv = self.levels
        top = int(lv["max_level"])
        if "cumulative" in lv:
            x = list(lv["cumulative"])
            _req(len(x) >= top, "levels.cumulative is shorter than max_level")
            cv.per_level_from_cumulative(x[:top])
            return x[:top]
        off = int(lv.get("index_offset", 0))
        per = [cv.evaluate(lv["per_level"], lvl + off) for lvl in range(1, top)]
        return [Fraction(x) if self.exact else float(x) for x in cv.cumulative_from_per_level(per)]

    def stat_at(self, stat: str, level: int):
        spec = self.player["stats"][stat]
        return cv.evaluate(spec, level + int(spec.get("index_offset", 0)))

    def has_randomness(self, skill: str | None) -> bool:
        def chance(p):
            return p not in (0, 1)
        if any(chance(d["chance"]) for e in self.enemies.values() for d in e.get("drops", [])):
            return True
        if any(chance(a.get("success_chance", 1)) for a in self.activities.values()):
            return True
        return bool(skill and chance(self.skills[skill].get("accuracy", 1)))


# ---------------------------------------------------------------- combat duel

def duel(player: dict, enemy: dict, simultaneous: str, rng=None) -> dict:
    """Discrete-event duel. Each side: hp, damage (per landed hit, after mitigation), interval_s, first_s,
    optional accuracy (chance a hit lands; needs rng). Returns outcome win | loss | mutual | stalemate,
    time_s of the deciding death (None for stalemate), hits landed by each side, and the isolated
    hits/TTK/TTD formulas (N = ceil(H/d), t0 + (N-1)*tau) for comparison."""
    def can(side):
        return side["damage"] > 0 and side.get("accuracy", 1) > 0

    def lands(side):
        acc = side.get("accuracy", 1)
        if acc >= 1:
            return True
        if rng is None:
            raise ValueError("accuracy below 1 needs a seeded rng")
        return rng.random() < acc

    def isolated(att, dfn):
        if not can(att):
            return None, None
        n = cv.hits_to_kill(dfn["hp"], att["damage"])
        return n, cv.time_to_kill(n, att["interval_s"], att["first_s"])

    n_k, ttk = isolated(player, enemy)
    n_d, ttd = isolated(enemy, player)
    out = {"hits_to_kill": n_k, "ttk_isolated_s": ttk, "hits_to_die": n_d, "ttd_isolated_s": ttd}
    cp, ce = can(player), can(enemy)
    if not cp and not ce:
        return {"outcome": "stalemate", "time_s": None, "player_hits": 0, "enemy_hits": 0,
                "player_hp_left": player["hp"], "enemy_hp_left": enemy["hp"], **out}
    hp_p, hp_e = player["hp"], enemy["hp"]
    tp, te = player["first_s"], enemy["first_s"]
    hits = {"p": 0, "e": 0}
    for _ in range(10_000_000):
        t = min(x for x, ok in ((tp, cp), (te, ce)) if ok)
        p_now, e_now = cp and tp == t, ce and te == t
        if p_now and e_now and simultaneous == "both":
            if lands(player):
                hp_e -= player["damage"]
                hits["p"] += 1
            if lands(enemy):
                hp_p -= enemy["damage"]
                hits["e"] += 1
            if hp_e <= 0 or hp_p <= 0:
                res = "mutual" if hp_e <= 0 and hp_p <= 0 else ("win" if hp_e <= 0 else "loss")
                return {"outcome": res, "time_s": t, "player_hits": hits["p"], "enemy_hits": hits["e"],
                        "player_hp_left": max(hp_p, 0), "enemy_hp_left": max(hp_e, 0), **out}
        else:
            seq = (["p", "e"] if simultaneous != "enemy_first" else ["e", "p"]) if p_now and e_now \
                else (["p"] if p_now else ["e"])
            for who in seq:
                if who == "p" and lands(player):
                    hp_e -= player["damage"]
                    hits["p"] += 1
                elif who == "e" and lands(enemy):
                    hp_p -= enemy["damage"]
                    hits["e"] += 1
                if hp_e <= 0 or hp_p <= 0:
                    return {"outcome": "win" if hp_e <= 0 else "loss", "time_s": t,
                            "player_hits": hits["p"], "enemy_hits": hits["e"],
                            "player_hp_left": max(hp_p, 0), "enemy_hp_left": max(hp_e, 0), **out}
        if p_now:
            tp += player["interval_s"]
        if e_now:
            te += enemy["interval_s"]
    raise ValueError("duel did not finish within 10,000,000 attacks")


def wilson_interval(successes: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion (NIST/SEMATECH e-Handbook, W05)."""
    if n <= 0:
        raise ValueError("n must be > 0")
    p = successes / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, centre - half), min(1.0, centre + half)


# ---------------------------------------------------------------- the simulation

class Sim:
    def __init__(self, model: Model, policy: str, opts: dict, rng):
        self.M = model
        self.policy = policy
        self.opts = opts
        self.rng = rng
        self.Z = Fraction(0) if model.exact else 0.0
        M = model
        self.discrete = M.time["mode"] == "discrete"
        self.bal = {c: d["start"] for c, d in M.currencies.items()}
        self.lifetime = {c: self.Z for c in M.currencies}
        self.run_earned = {c: self.Z for c in M.currencies}
        self.best_run = {c: self.Z for c in M.currencies}
        self.maxbal = dict(self.bal)
        self.ledger = {c: {"start": d["start"], "sources": {}, "sinks": {}, "adjustments": {}}
                       for c, d in M.currencies.items()}
        self.owned = {p: d["start_owned"] for p, d in M.producers.items()}
        self.items: set = set()
        self.unlocked: set = set()
        self.defeated: set = set()
        self.completed: set = set()
        self.prestiges = 0
        self.awarded_total = 0
        self.t = self.Z
        self.pattern = M.sessions[opts["sessions"]] if opts.get("sessions") else None
        self.cal = self.Z if self.pattern else None
        self.session_index = 0
        self.session_end = self.pattern["active_s"] if self.pattern else None
        self.pending_offline: dict = {}
        self.activity = None
        self.pursuit = ("idle", "start")
        self.cumxp = M.cumulative_xp() if M.levels else None
        self.level = self._level_now() if M.levels else None
        self.skill = M.skills[opts["skill"]] if opts.get("skill") else {}
        self.trace: list = []
        self.steps: list = []
        self.goal_hits: dict = {}
        self.hard_walls: list = []
        self.prestige_log: list = []
        self.unlock_log: list = []
        self.metrics = {sp["id"]: [] for sp in M.analysis.get("spikes", [])}
        self.fights = {"won": 0, "lost": 0, "mutual": 0}
        self.fight_log: dict = {}
        self.max_owned = dict(self.owned)
        self.max_level = self.level
        self.stop = None
        self.events = 0
        self._changed = False
        self.lean = opts.get("lean", False)
        self.offline_lifetime = {c: self.Z for c in M.currencies}  # offline grants inside lifetime / run
        self.offline_run = {c: self.Z for c in M.currencies}
        self.completions: dict = {}
        self.soft_thresholds = opts.get("soft_thresholds") or {}
        self.soft_walls: list = []
        self._prev_wait = None
        self.spike_counts = {sp["id"]: 0 for sp in M.analysis.get("spikes", [])}
        self.metric_active = {sp["id"]: False for sp in M.analysis.get("spikes", [])}
        self.spike_log: list = []
        self.free_bought: set = set()
        self.level_rewards_done: set = set()
        self.lost_at: dict = {}
        self.warnings: list = []
        self._skip_noted = False
        self.marks: dict = {}

    # ---- helpers ---------------------------------------------------
    def ge(self, have, need) -> bool:
        """have >= need; exact in exact mode. Float mode allows a relative 1e-9 shortfall, so that a balance
        that reaches a price at the computed time but lands one rounding step short still counts."""
        if self.M.exact:
            return have >= need
        return have >= need - FLOAT_REL_TOL * max(1.0, abs(need))

    def _event(self, kind: str, **detail):
        if self.lean:
            return
        rec = {"t_active_s": self.t, "t_calendar_s": self.cal, "event": kind}
        rec.update(detail)
        self.trace.append(rec)

    def _warn(self, text):
        if text not in self.warnings:
            self.warnings.append(text)

    def _move(self, c, amount):
        """Change a balance. Float mode: when rounding makes the actual change differ from `amount` (a grant or a
        sink absorbed at a large magnitude), the difference is booked as the float_rounding adjustment."""
        old = self.bal[c]
        self.bal[c] = old + amount
        if not self.M.exact:
            diff = (self.bal[c] - old) - amount
            if diff != 0:
                self._adjust(c, diff, "float_rounding")

    def _credit(self, c, amount, source):
        if amount == 0:
            return
        self._move(c, amount)
        self.lifetime[c] += amount
        self.run_earned[c] += amount
        if source == "offline":
            self.offline_lifetime[c] += amount
            self.offline_run[c] += amount
        src = self.ledger[c]["sources"]
        src[source] = src.get(source, self.Z) + amount
        if self.bal[c] > self.maxbal[c]:
            self.maxbal[c] = self.bal[c]

    def _adjust(self, c, amount, name):
        adj = self.ledger[c]["adjustments"]
        adj[name] = adj.get(name, self.Z) + amount

    def _cap_loss(self, c, loss):
        if loss > 0:
            self._adjust(c, -loss, "cap_loss")
            self.lifetime[c] -= loss
            self.run_earned[c] -= loss

    def _level_now(self) -> int:
        return cv.level_for(self.cumxp, self.bal[self.M.levels["currency"]])

    def item_mult(self, key):
        out = 1
        for iid in self.M.items:
            if iid in self.items:
                for ef in self.M.items[iid].get("effects", []):
                    if ef["target"] == key:
                        out = out * ef["value"]
        return out

    def prestige_mult(self, c):
        pr = self.M.prestige
        if not pr or "bonus" not in pr or pr["bonus"]["target"] != f"currency:{c}":
            return 1
        return 1 + pr["bonus"]["per_unit"] * self.bal[pr["award_currency"]]

    def rates(self, owned=None, items=None):
        """(currency rates, producer rates, per-(currency, producer) rates), all per second."""
        owned = self.owned if owned is None else owned
        saved = self.items
        if items is not None:
            self.items = items
        cur = {c: self.Z for c in self.M.currencies}
        prod = {p: self.Z for p in self.M.producers}
        per = {}
        for pid, p in self.M.producers.items():
            n = owned[pid]
            if n == 0:
                continue
            pm = cv.milestone_product(1, [(ms["owned"], ms["mult"]) for ms in p.get("milestones", [])], int(n)) \
                * self.item_mult(f"producer:{pid}")
            for tgt, base in p["produces"].items():
                kind, _, tid = tgt.partition(":")
                out = base * n * pm
                if kind == "currency":
                    out = out * self.item_mult(f"currency:{tid}") * self.prestige_mult(tid)
                    cur[tid] += out
                    per[(tid, pid)] = out
                else:
                    prod[tid] += out
        self.items = saved
        return cur, prod, per

    def stats(self) -> dict:
        lvl = self.level
        out = {}
        for s in self.M.player["stats"]:
            base = self.M.stat_at(s, lvl)
            add, pct, mul = 0, [], 1
            for iid in self.M.items:
                if iid in self.items:
                    for ef in self.M.items[iid].get("effects", []):
                        if ef["target"] == f"stat:{s}":
                            if ef["op"] == "add":
                                add += ef["value"]
                            elif ef["op"] == "add_pct":
                                pct.append(ef["value"])
                            else:
                                mul = mul * ef["value"]
            out[s] = (base + add) * (1 + cv.stack_bonus(pct, ())) * mul
        return out

    def sides(self, eid: str, with_accuracy: bool) -> tuple[dict, dict]:
        st, e, d = self.stats(), self.M.enemies[eid], self.M.duel_cfg
        p_int = st["attack_interval_s"] + self.skill.get("extra_attack_delay_s", 0)
        p_dmg = st["attack"] * self.skill.get("damage_factor", 1) * (1 - e.get("mitigation", 0))
        e_dmg = e["damage"] * (1 - st.get("mitigation", 0))
        player = {"hp": st["hp"], "damage": p_dmg, "interval_s": p_int,
                  "first_s": cv.first_hit_offset(p_int, d["player_first_hit"])}
        if with_accuracy and "accuracy" in self.skill:
            player["accuracy"] = self.skill["accuracy"]
        enemy = {"hp": e["hp"], "damage": e_dmg, "interval_s": e["attack_interval_s"],
                 "first_s": cv.first_hit_offset(e["attack_interval_s"], d["enemy_first_hit"])}
        return player, enemy

    def preview(self, eid):
        p, e = self.sides(eid, with_accuracy=False)
        return duel(p, e, self.M.duel_cfg["simultaneous"])

    def preview_margin(self, eid):
        """(preview duel, margin): a win -> the player's HP left / HP; a loss -> -(the enemy's HP left / HP);
        mutual or stalemate -> 0. Range -1..1."""
        p, e = self.sides(eid, with_accuracy=False)
        res = duel(p, e, self.M.duel_cfg["simultaneous"])
        if res["outcome"] == "win":
            return res, cv._div(res["player_hp_left"], p["hp"])
        if res["outcome"] == "loss":
            return res, -cv._div(res["enemy_hp_left"], e["hp"])
        return res, 0

    # ---- predicates --------------------------------------------------
    def num(self, x):
        """A predicate number; a threshold object grows with the prestige count."""
        if isinstance(x, dict):
            return cv.evaluate(x["curve"], self.prestiges + int(x.get("index_offset", 0)))
        return x

    def counter(self, k, c, no_offline=False):
        """Balance, lifetime or run-earned of currency c; no_offline leaves offline grants out (prestige switch)."""
        if k == "balance":
            return self.bal[c]
        if k == "lifetime":
            return self.lifetime[c] - (self.offline_lifetime[c] if no_offline else 0)
        return self.run_earned[c] - (self.offline_run[c] if no_offline else 0)

    def pred(self, p, no_offline=False) -> bool:
        (k, a), = p.items()
        if k == "all":
            return all(self.pred(q, no_offline) for q in a)
        if k == "any":
            return any(self.pred(q, no_offline) for q in a)
        if k == "not":
            return not self.pred(a, no_offline)
        if k == "owned":
            return self.owned[a[0]] >= self.num(a[1])
        if k == "item":
            return a in self.items
        if k == "level":
            return self.level >= self.num(a)
        if k == "defeated":
            return a in self.defeated
        if k == "completed":
            return a in self.completed
        if k == "unlocked":
            return a in self.unlocked
        if k == "prestiges":
            return self.prestiges >= self.num(a)
        if k == "soft_walls":
            if isinstance(a, list):  # walls whose step starts at or after the first time "after" held
                t0 = self.marks.get(_key(a[1]["after"]))
                n = 0 if t0 is None else sum(1 for w in self.soft_walls if w["start_active_s"] >= t0)
                return n >= self.num(a[0])
            return len(self.soft_walls) >= self.num(a)
        if k == "hard_wall":
            return any(w["id"] == a for w in self.hard_walls)
        if k == "spikes":
            return self.spike_counts[a[0]] >= self.num(a[1])
        if k in ("balance", "lifetime", "run"):
            return self.ge(self.counter(k, a[0], no_offline), self.num(a[1]))
        return self.t >= self.num(a)  # active_s

    def pred_time(self, p, rates, no_offline=False):
        """Active seconds until predicate p becomes true if nothing but production changes; None if never."""
        if self.pred(p, no_offline):
            return self.Z
        (k, a), = p.items()
        if k in ("all", "any"):
            ts = [self.pred_time(q, rates, no_offline) for q in a]
            if k == "all":
                return None if any(t is None for t in ts) else max(ts)
            ok = [t for t in ts if t is not None]
            return min(ok) if ok else None
        if k == "active_s":
            return self.num(a) - self.t
        if k == "level":  # level L <=> level currency balance >= X_L
            lvl = self.num(a)
            if lvl > len(self.cumxp):
                return None
            k, a = "balance", [self.M.levels["currency"], self.cumxp[int(lvl) - 1]]
        if k in ("balance", "lifetime", "run"):
            c, target = a[0], self.num(a[1])
            r = rates[c]
            if r <= 0:
                return None
            cap = self.M.currencies[c].get("cap")
            need = target - self.counter(k, c, no_offline)
            if cap is not None and (self.bal[c] >= cap or self.bal[c] + need > cap):
                return None
            return cv.wait_time(need, 0, r)
        return None  # owned, item, defeated, completed, unlocked, prestiges, walls, spikes, not: change only at events

    # ---- purchases ---------------------------------------------------
    def buyable(self, i) -> bool:
        """A producer or item with a cost (items without a cost are found only: drops, level rewards)."""
        table = self.M.producers if i in self.M.producers else self.M.items if i in self.M.items else None
        return table is not None and "cost" in table[i]

    def found_only_detail(self, i) -> str:
        srcs = [f"drop from {e} (chance {dr['chance']})" for e, d in self.M.enemies.items()
                for dr in d.get("drops", []) if dr["item"] == i]
        srcs += [f"reward at level {rw['level']}" for rw in (self.M.levels or {}).get("rewards", []) if i in rw.get("items", [])]
        return f"{i} has no price: " + ("; ".join(srcs) if srcs else "no source in the model")

    def purchasables(self) -> list:
        producers = [p for p, d in self.M.producers.items() if "cost" in d and p not in self.free_bought]
        return producers + [i for i, it in self.M.items.items() if "cost" in it and i not in self.items]

    def price(self, i):
        if not self.buyable(i):
            raise ModelError(f"{i} cannot be bought ({self.found_only_detail(i)})")
        if i in self.M.producers:
            cost = self.M.producers[i]["cost"]
            n = int(self.owned[i]) + int(cost.get("index_offset", 0))
            return cost["currency"], cv.round_price(cv.evaluate(cost["curve"], n), cost.get("rounding", "none"))
        cost = self.M.items[i]["cost"]
        return cost["currency"], cv.round_price(cost["amount"], cost.get("rounding", "none"))

    def requires(self, i):
        kind = self.M.kind_of(i)
        table = {"producer": self.M.producers, "item": self.M.items, "enemy": self.M.enemies,
                 "activity": self.M.activities}[kind]
        return table[i].get("requires")

    def eligible(self, i) -> bool:
        r = self.requires(i)
        return r is None or self.pred(r)

    def affordable(self, i) -> bool:
        kind = self.M.kind_of(i)
        if kind not in ("producer", "item"):
            return True
        if not self.buyable(i):
            return False  # found only: no price to pay
        c, amt = self.price(i)
        return self.ge(self.bal[c], amt)

    def done(self, i, until=None) -> bool:
        """Finished for an order entry: an item when owned; a producer when `until` units are owned (never
        without `until`); an enemy after `until` wins (default 1); an activity after `until` completions."""
        kind = self.M.kind_of(i)
        if kind == "producer":
            if "cost" not in self.M.producers[i]:
                return True  # a cost-less producer is never bought
            return until is not None and self.owned[i] >= until
        if kind == "item":
            return i in self.items
        if kind == "enemy":
            return i in self.defeated if until is None else self.fight_log.get(i, {}).get("won", 0) >= until
        return i in self.completed if until is None else self.completions.get(i, 0) >= until

    def gain(self, i, c):
        """Immediate production gain in currency c per second from buying i (greedy-roi)."""
        before = self.rates()[0][c]
        if i in self.M.producers:
            owned = dict(self.owned)
            owned[i] += 1
            after = self.rates(owned=owned)[0][c]
        else:
            after = self.rates(items=self.items | {i})[0][c]
        return after - before

    def _step(self, kind, i, label):
        prev = self.steps[-1] if self.steps else None
        start = prev["t_active_s"] if prev else self.Z
        start_cal = (prev["t_calendar_s"] if prev else self.Z) if self.cal is not None else None
        step = {"kind": kind, "id": i, "label": label, "t_active_s": self.t, "t_calendar_s": self.cal,
                "wait_s": self.t - start, "start_calendar_s": start_cal}
        self.steps.append(step)
        self._soft_wall_check(step)
        self._record_metrics(label)

    def _soft_wall_check(self, s):
        """Soft walls are found as steps complete (so goals can test them); thresholds from model or CLI."""
        th, rule = self.soft_thresholds, None
        if "min_wait_s" in th and s["wait_s"] > 0 and s["wait_s"] >= th["min_wait_s"]:
            rule = f"wait >= {th['min_wait_s']} s"
        elif "min_ratio_to_previous" in th and self._prev_wait and s["wait_s"] >= th["min_ratio_to_previous"] * self._prev_wait:
            rule = f"wait >= {th['min_ratio_to_previous']} x previous wait"
        if rule:
            s["soft_wall"] = True
            self.soft_walls.append({
                "step": s["label"], "start_active_s": s["t_active_s"] - s["wait_s"], "end_active_s": s["t_active_s"],
                "start_calendar_s": s["start_calendar_s"], "end_calendar_s": s["t_calendar_s"], "wait_s": s["wait_s"],
                "previous_wait_s": self._prev_wait, "rule": rule,
                "start_active_s_approx": _approx(s["t_active_s"] - s["wait_s"]),
                "end_active_s_approx": _approx(s["t_active_s"]), "wait_s_approx": _approx(s["wait_s"])})
            self._event("soft_wall", step=s["label"], wait_s=s["wait_s"])
        if s["wait_s"] > 0:
            self._prev_wait = s["wait_s"]

    def buy(self, i):
        c, amt = self.price(i)
        self._move(c, -amt)
        if self.bal[c] < 0:  # float mode only (see ge): a rounding-step shortfall, kept as a named adjustment
            self._adjust(c, -self.bal[c], "float_rounding")
            self.bal[c] = self.Z
        if amt == 0:
            self.free_bought.add(i)
            self._warn(f"{i} costs 0: at most one is bought per event instant")
        sinks = self.ledger[c]["sinks"]
        sinks[f"purchase:{i}"] = sinks.get(f"purchase:{i}", self.Z) + amt
        if i in self.M.producers:
            self.owned[i] += 1
            self.max_owned[i] = max(self.max_owned[i], self.owned[i])
            label = f"buy {i} ({int(self.owned[i])} owned)"
        else:
            self.items.add(i)
            label = f"buy {i}"
        self._event("buy", id=i, currency=c, price=amt)
        self._step("purchase", i, label)
        self._check_goals()

    # ---- metrics (power spikes) -------------------------------------
    def metric_value(self, sp):
        """The reference metric now: hits/TTK the player needs against the enemy, hits/TTD the enemy needs
        against the player (current stats, every attack landing), or production per second. None = never."""
        if sp["metric"] == "production_per_s":
            return self.rates()[0][sp["currency"]]
        p, e = self.sides(sp["enemy"], with_accuracy=False)
        att, dfn = (p, e) if sp["metric"] in ("hits_to_kill", "ttk_s") else (e, p)
        if att["damage"] <= 0:
            return None
        n = cv.hits_to_kill(dfn["hp"], att["damage"])
        return n if sp["metric"] in ("hits_to_kill", "hits_to_die") else cv.time_to_kill(n, att["interval_s"], att["first_s"])

    def _record_metrics(self, cause):
        for sp in self.M.analysis.get("spikes", []):
            sid = sp["id"]
            if "active_when" in sp and not self.pred(sp["active_when"]):
                self.metric_active[sid] = False  # locked content is not measured
                continue
            v = self.metric_value(sp)
            hist = self.metrics[sid]
            if not self.metric_active[sid]:
                self.metric_active[sid] = True
                hist.append({"t_active_s": self.t, "t_calendar_s": self.cal, "value": v, "cause": cause,
                             "segment_start": True})
            elif hist[-1]["value"] != v:
                hist.append({"t_active_s": self.t, "t_calendar_s": self.cal, "value": v, "cause": cause})
                rule = spike_rule(sp, hist[-2]["value"], v)[2]
                if rule:
                    self.spike_counts[sid] += 1
                    hist[-1]["spike"] = rule
                    self._event("spike", metric=sid, value=v, cause=cause)

    # ---- phases ------------------------------------------------------
    def phase_produce(self):
        if not self.discrete:
            return  # continuous production accrues in advance()
        dt = self.M.time["tick_s"]
        if self.M.time["new_units_produce_in_creation_tick"]:
            for pid in self.M.producers:  # model order; counts raised earlier in the tick produce now
                one = {q: (self.owned[q] if q == pid else 0) for q in self.M.producers}
                cur, prod, per = self.rates(owned=one)
                self._apply_production(cur, prod, per, dt)
        else:
            cur, prod, per = self.rates()
            self._apply_production(cur, prod, per, dt)

    def _apply_production(self, cur, prod, per, dt):
        for (c, pid), r in per.items():
            self._credit(c, r * dt, f"production:{pid}")
        for pid, r in prod.items():
            if r:
                self.owned[pid] += r * dt
                self.max_owned[pid] = max(self.max_owned[pid], self.owned[pid])

    def phase_rewards(self):
        for c, amt in self.pending_offline.items():
            self._credit(c, amt, "offline")
            self._event("offline_reward", currency=c, amount=amt)
        self.pending_offline = {}
        self._finish_activity()
        self._check_level()

    def _finish_activity(self):
        a = self.activity
        if a is None or a["end"] > self.t:
            return
        self.activity = None
        if a["kind"] == "fight":
            eid, res = a["id"], a["result"]
            self.fights[OUTCOME_KEY[res["outcome"]]] += 1
            per = self.fight_log.setdefault(eid, {"fights": 0, "won": 0, "lost": 0, "mutual": 0,
                                                  "attempts_to_first_win": None})
            per["fights"] += 1
            per[OUTCOME_KEY[res["outcome"]]] += 1
            if res["outcome"] == "win" and per["attempts_to_first_win"] is None:
                per["attempts_to_first_win"] = per["fights"]
            if res["outcome"] != "win":
                self.lost_at[eid] = self.stat_signature()
            per["last"] = {k: res[k] for k in ("outcome", "time_s", "hits_to_kill", "ttk_isolated_s", "hits_to_die",
                                               "ttd_isolated_s", "player_hits", "enemy_hits")}
            per["last"]["at_level"] = self.level
            self._event("fight_end", id=eid, outcome=res["outcome"], duel_s=res["time_s"],
                        ttk_isolated_s=res["ttk_isolated_s"], ttd_isolated_s=res["ttd_isolated_s"],
                        player_hits=res["player_hits"], enemy_hits=res["enemy_hits"])
            if res["outcome"] != "win":
                return
            for c, amt in self.M.enemies[eid].get("rewards", {}).items():
                self._credit(c, amt, f"reward:{eid}")
            for dr in self.M.enemies[eid].get("drops", []):
                if dr["item"] in self.items:
                    continue
                if dr["chance"] == 1 or (dr["chance"] > 0 and self.rng.random() < dr["chance"]):
                    self.items.add(dr["item"])
                    self._event("drop", id=dr["item"], source=eid)
                    self._step("drop", dr["item"], f"found {dr['item']}")
            if eid not in self.defeated:
                self.defeated.add(eid)
                self._step("defeat", eid, f"defeat {eid}")
        else:
            aid, act = a["id"], self.M.activities[a["id"]]
            ch = act.get("success_chance", 1)
            ok = ch == 1 or (ch > 0 and self.rng.random() < ch)
            self._event("activity_end", id=aid, success=ok)
            if not ok:
                return
            for c, amt in act.get("rewards", {}).items():
                self._credit(c, amt, f"reward:{aid}")
            self.completions[aid] = self.completions.get(aid, 0) + 1
            if aid not in self.completed:
                self.completed.add(aid)
                self._step("complete", aid, f"complete {aid}")

    def _check_level(self):
        if self.cumxp is None:
            return
        lvl = self._level_now()
        while self.level < lvl:
            self.level += 1
            self.max_level = max(self.max_level, self.level)
            self._event("level_up", level=self.level)
            self._grant_level_rewards(self.level)
            self._step("level", f"level {self.level}", f"level {self.level}")
            lvl = self._level_now()  # a level reward in the level currency can raise the level further
        if lvl < self.level:
            self.level = lvl

    def _grant_level_rewards(self, lvl):
        """levels.rewards: granted once per level per simulated player (not again after a reset)."""
        if lvl in self.level_rewards_done:
            return
        self.level_rewards_done.add(lvl)
        for rw in self.M.levels.get("rewards", []):
            if rw["level"] == lvl:
                for c, amt in rw.get("currencies", {}).items():
                    self._credit(c, amt, f"level_reward:{lvl}")
                for it in rw.get("items", []):
                    if it not in self.items:
                        self.items.add(it)
                        self._event("level_reward_item", id=it, level=lvl)

    def stat_signature(self):
        return (self.level, tuple(sorted(self.items)))

    def phase_caps(self):
        for c, d in self.M.currencies.items():
            cap = d.get("cap")
            if cap is not None and self.bal[c] > cap:
                loss = self.bal[c] - cap
                self.bal[c] = cap
                self._cap_loss(c, loss)
                self._event("cap_clip", currency=c, lost=loss)

    def phase_purchase(self):
        if self.activity is not None:
            return
        for _ in range(100_000):
            act = decide(self)
            if act[0] == "buy":
                self.buy(act[1])
                continue
            self.pursuit = act
            if act[0] == "fight":
                eid = act[1]
                p, e = self.sides(eid, with_accuracy=True)
                res = duel(p, e, self.M.duel_cfg["simultaneous"], self.rng)
                if res["time_s"] is None:
                    raise ModelError(f"fight against {eid} can never end (neither side can deal damage)")
                dur = res["time_s"] + self.M.enemies[eid]["overhead_s"]
                ba = self.M.policy_cfg.get("boss_attempt")
                if ba is not None and res["outcome"] != "win":
                    dur += ba["recovery_s"]  # declared recovery time after a lost fight
                self.activity = {"kind": "fight", "id": eid, "result": res, "end": self.t + self._ticks(dur)}
                self._event("fight_start", id=eid)
            elif act[0] == "do":
                aid = act[1]
                self.activity = {"kind": "activity", "id": aid,
                                 "end": self.t + self._ticks(self.M.activities[aid]["duration_s"])}
                self._event("activity_start", id=aid)
            self._track_gates()
            return
        raise ModelError("more than 100,000 purchases in one instant")

    def _ticks(self, dur):
        if not self.discrete:
            return dur
        tick = self.M.time["tick_s"]
        return math.ceil(dur / tick) * tick

    def gated_ids(self):
        """Ids whose prerequisite can hold the player back: buyable producers and items, enemies, and an
        activity while the policy pursues it (activity chains alone are ordinary sequencing)."""
        out = [i for i in list(self.M.producers) + list(self.M.items) if self.buyable(i) and self.requires(i) is not None]
        out += [e for e, d in self.M.enemies.items() if "requires" in d]
        p = self.pursued()
        if p is not None and self.M.kind_of(p) == "activity" and self.requires(p) is not None:
            out.append(p)
        return out

    def pursued(self):
        """The id the policy is working toward: the save-for target, or what it waits for."""
        if self.policy == "save-for" and not self.done(self.opts["target"]):
            return self.opts["target"]
        return self.pursuit[1] if self.pursuit[0] == "wait" else None

    def _gate_condition(self, i):
        """Why the player could take i now if it were unlocked: affordable, beatable or pursued; None if not."""
        kind = self.M.kind_of(i)
        if kind in ("producer", "item"):
            return "affordable" if (i not in self.items and self.affordable(i)) else None
        if kind == "enemy":
            if self.M.enemies[i].get("once") and i in self.defeated:
                return None
            return "beatable" if self.preview(i)["outcome"] == "win" else None
        return "pursued"

    def _track_gates(self):
        """Hard walls for every policy: per gated id, from the first instant it is affordable (or beatable)
        while its prerequisite is false, until the prerequisite holds."""
        pursued = self.pursued()
        open_ids = {w["id"]: w for w in self.hard_walls if w["end_s"] is None}
        for i in self.gated_ids():
            w = open_ids.get(i)
            if self.eligible(i):
                if w:
                    w["end_s"], w["end_calendar_s"], w["duration_s"] = self.t, self.cal, self.t - w["start_s"]
                    self._event("hard_wall_end", id=i)
                continue
            if w:
                w["pursued_by_policy"] = w["pursued_by_policy"] or pursued == i
                continue
            cond = self._gate_condition(i)
            if cond:
                gate, via = self._gate_kind(i)
                self.hard_walls.append({"id": i, "kind": self.M.kind_of(i), "condition": cond, "gate": gate,
                                        "via": via, "start_s": self.t,
                                        "start_calendar_s": self.cal, "end_s": None, "end_calendar_s": None,
                                        "duration_s": None, "missing": self.requires(i),
                                        "pursued_by_policy": pursued == i})
                self._event("hard_wall_start", id=i, missing=self.requires(i))
        for i, w in open_ids.items():  # a pursued activity the policy dropped is closed when it unlocks
            if i not in self.gated_ids() and self.eligible(i) and w["end_s"] is None:
                w["end_s"], w["end_calendar_s"], w["duration_s"] = self.t, self.cal, self.t - w["start_s"]

    def _gate_kind(self, i):
        """(gate, via): "activity" for a pursued activity; "timed" when the prerequisite tests active time;
        "chained" when it names a gated id that is itself still locked (via lists them); else "prerequisite"."""
        if self.M.kind_of(i) == "activity":
            return "activity", []
        req = self.requires(i)
        if self._tests_time(req):
            return "timed", []
        via = [x for x in self._refs(req) if self.requires(x) is not None and not self.eligible(x)]
        return ("chained", via) if via else ("prerequisite", [])

    def _tests_time(self, p, seen=None):
        """True when the predicate (reading unlocked U through U's predicate) tests active_s."""
        seen = set() if seen is None else seen
        (k, a), = p.items()
        if k == "active_s":
            return True
        if k in ("all", "any"):
            return any(self._tests_time(q, seen) for q in a)
        if k == "not":
            return self._tests_time(a, seen)
        if k == "unlocked" and a not in seen:
            seen.add(a)
            return self._tests_time(self.M.unlocks[a]["when"], seen)
        return False

    def _refs(self, p, seen=None):
        """Ids a predicate names (owned, item, defeated, completed; unlocked expands to its unlock's predicate)."""
        seen = set() if seen is None else seen
        out = []
        (k, a), = p.items()
        if k in ("all", "any"):
            for q in a:
                out += self._refs(q, seen)
        elif k == "not":
            out += self._refs(a, seen)
        elif k == "owned":
            out.append(a[0])
        elif k in ("item", "defeated", "completed"):
            out.append(a)
        elif k == "unlocked" and a not in seen:
            seen.add(a)
            out += self._refs(self.M.unlocks[a]["when"], seen)
        return list(dict.fromkeys(out))

    def phase_unlock(self):
        for uid, u in self.M.unlocks.items():
            if uid not in self.unlocked and self.pred(u["when"]):
                self.unlocked.add(uid)
                self.unlock_log.append({"id": uid, "t_active_s": self.t, "t_calendar_s": self.cal})
                self._event("unlock", id=uid)
                self._changed = True
                self._record_metrics(f"unlock {uid}")  # a metric's active_when may have become true

    def _no_offline(self):
        return not self.M.prestige.get("offline_counts_toward_basis", True)

    def prestige_basis(self):
        pr = self.M.prestige
        c, no_off = pr["basis_currency"], self._no_offline()
        run = self.counter("run", c, no_off)
        return {"lifetime": self.counter("lifetime", c, no_off), "run": run,
                "maximum": max(self.best_run[c], run)}[pr["basis"]]

    def prestige_award(self, x):
        pr, f = self.M.prestige, self.M.prestige["formula"]
        y = x / f["divisor"]
        if f["kind"] == "power":
            fl = cv.floor_power(f["a"], y, f["alpha"]) if self.M.exact else math.floor(f["a"] * y ** f["alpha"])
        else:
            fl = cv.triangular_root_floor(y) if self.M.exact else math.floor((math.sqrt(1 + 8 * y) - 1) / 2)
        return cv.award_total_entitlement(fl, self.awarded_total) if pr["rule"] == "total_entitlement" \
            else cv.award_per_run(fl)

    def basis_for_award(self, award):
        """Smallest basis value x whose award is >= `award` (inverse of the formula, checked exactly)."""
        pr, f = self.M.prestige, self.M.prestige["formula"]
        target = award + (self.awarded_total if pr["rule"] == "total_entitlement" else 0)
        if f["kind"] == "triangular_root":
            return f["divisor"] * target * (target + 1) / 2
        alpha = f["alpha"]
        if self.M.exact and Fraction(alpha).numerator == 1:
            return f["divisor"] * (Fraction(target) / f["a"]) ** Fraction(alpha).denominator
        x = float(f["divisor"]) * (float(target) / float(f["a"])) ** (1 / float(alpha))
        x = Fraction(x) if self.M.exact else x
        while self.prestige_award(x) < award:  # the float estimate may land a hair short
            x = x * (1 + Fraction(1, 10 ** 12)) if self.M.exact else x * (1 + 1e-12)
        return x

    def phase_reset(self):
        pr = self.M.prestige
        if not pr or not self.pred(pr["take_when"], self._no_offline()):
            return
        x = self.prestige_basis()
        award = self.prestige_award(x)
        if "min_award" in pr and award < pr["min_award"]:
            if not self._skip_noted:
                self._skip_noted = True
                self._event("prestige_skipped", award=award, min_award=pr["min_award"])
            return
        self._skip_noted = False
        self.marks: dict = {}
        for cc in self.M.currencies:
            self.best_run[cc] = max(self.best_run[cc], self.counter("run", cc, self._no_offline()))
        removed = {}
        for sid in pr["reset"]:
            kind, _, i = sid.partition(":")
            if kind == "currency":
                start = self.M.currencies[i]["start"]
                removed[sid] = self.bal[i] - start
                self._adjust(i, start - self.bal[i], "reset")
                self.bal[i] = start
                self.run_earned[i] = self.Z
                self.offline_run[i] = self.Z
            elif kind == "producer":
                removed[sid] = self.owned[i] - self.M.producers[i]["start_owned"]
                self.owned[i] = self.M.producers[i]["start_owned"]
            else:
                bag = {"item": self.items, "unlock": self.unlocked, "defeated": self.defeated,
                       "completed": self.completed}[kind]
                removed[sid] = i in bag
                bag.discard(i)
        self._credit(pr["award_currency"], self.Z + award, "prestige_award")
        self.awarded_total += award
        self.prestiges += 1
        if self.cumxp is not None:
            self.level = self._level_now()
        self.prestige_log.append({"t_active_s": self.t, "t_calendar_s": self.cal, "basis_value": x,
                                  "award": award, "removed": removed, "kept": list(pr["keep"])})
        self._event("prestige", award=award, basis_value=x)
        self._step("prestige", f"prestige {self.prestiges}", f"prestige {self.prestiges}")
        self.activity = None
        self._changed = True

    def instant(self, produce: bool = True):
        """Run the declared phases at the current time; re-run while a state change after the purchase
        phase may change the policy's decision (bounded). produce=False at t = 0 (no tick has elapsed)."""
        self.free_bought = set()  # a 0-price purchase is taken at most once per instant
        for _ in range(1000):
            self._changed = False
            after_purchase = False
            for ph in self.M.event_order:
                if ph == "produce" and not (self.discrete and produce):
                    continue
                self._check_goals()  # a goal state may be transient inside one instant (e.g. undone by a reset)
                getattr(self, f"phase_{ph}")()
                self._check_goals()
                if ph == "purchase":
                    after_purchase = True
                    self._changed = False
            self._track_gates()
            self._check_goals()
            if not (after_purchase and self._changed) or self.discrete or self._all_goals():
                return
        raise ModelError("more than 1,000 re-runs of one instant (an unlock or reset that never settles?)")

    def _check_goals(self):
        for p in self.M.after_preds:  # the first time each "after" point holds (soft_walls [N, {after}])
            k = _key(p)
            if k not in self.marks and self.pred(p):
                self.marks[k] = self.t
        for g in self.M.goals:
            if g["id"] not in self.goal_hits and self.pred(g["when"]):
                self.goal_hits[g["id"]] = {"t_active_s": self.t, "t_calendar_s": self.cal}
                self._event("goal", id=g["id"])

    def _all_goals(self):
        return bool(self.M.goals) and len(self.goal_hits) == len(self.M.goals)

    # ---- time --------------------------------------------------------
    def advance_to(self, t_new):
        dt = t_new - self.t
        if dt < 0:
            raise AssertionError("time went backwards")
        if not self.discrete and dt > 0:
            cur, _, per = self.rates()
            for c in self.M.currencies:
                total = cur[c] * dt
                if total == 0:
                    continue
                before, max_before = self.bal[c], self.maxbal[c]
                for (cc, pid), r in per.items():
                    if cc == c:
                        self._credit(c, r * dt, f"production:{pid}")
                cap = self.M.currencies[c].get("cap")
                if cap is not None:
                    # production cannot raise a balance past its cap; the clipped part is a named adjustment
                    loss = total if before >= cap else max(self.Z, before + total - cap)
                    if loss > 0:
                        self.bal[c] -= loss
                        self._cap_loss(c, loss)
                        self.maxbal[c] = max(max_before, self.bal[c])
        self.t = t_new
        if self.cal is not None:
            self.cal += dt

    def end_session(self):
        """Close the session: gap in calendar time, offline earnings per the model's contract."""
        pat = self.pattern
        self.session_index += 1
        gap = pat["gaps_s"][(self.session_index - 1) % len(pat["gaps_s"])]
        for ab in pat.get("absences", []):
            if int(ab["after_session"]) == self.session_index:
                gap = ab["gap_s"]
        self._event("session_end", session=self.session_index, gap_s=gap)
        off = self.M.offline
        if off is not None:
            cur = self.rates()[0]
            for c in off["currencies"]:
                amt = cv.offline_earned(off["efficiency"], cur[c], gap, cap_s=off["cap_s"])
                if amt:
                    self.pending_offline[c] = self.pending_offline.get(c, self.Z) + amt
        self.cal += gap
        self.session_end = self.t + pat["active_s"]

    def next_progress_time(self):
        """Earliest absolute active time at which something can change, or None (blocked)."""
        cur = self.rates()[0]
        cands = []
        if self.activity is not None:
            cands.append(self.activity["end"])
        preds = [u["when"] for uid, u in self.M.unlocks.items() if uid not in self.unlocked]
        preds += [p for p in self.M.after_preds if _key(p) not in self.marks]
        preds += [g["when"] for g in self.M.goals if g["id"] not in self.goal_hits]
        for i in list(self.M.producers) + list(self.M.items) + list(self.M.enemies) + list(self.M.activities):
            r = self.requires(i)
            if r is not None:
                preds.append(r)
        if self.cumxp is not None and self.level < len(self.cumxp):  # level-ups are events (passive XP too)
            preds.append({"level": self.level + 1})
        pr = self.M.prestige
        if pr:
            no_off = self._no_offline()
            tw = pr["take_when"]
            if not self.pred(tw, no_off):
                w = self.pred_time(tw, cur, no_off)
                if w is not None:
                    cands.append(self.t + w)
            elif "min_award" in pr:  # held back by the minimum award: when does the award reach it?
                x = self.basis_for_award(pr["min_award"])
                k = "lifetime" if pr["basis"] == "lifetime" else "run"
                w = self.pred_time({k: [pr["basis_currency"], x]}, cur, no_off)
                if w is not None:
                    cands.append(self.t + w)
        waits = []
        if self.pursuit[0] == "wait" and self.buyable(self.pursuit[1]):
            waits.append(self.pursuit[1])
        open_ids = {w["id"] for w in self.hard_walls if w["end_s"] is None}
        waits += [i for i in self.gated_ids() if self.buyable(i) and i not in open_ids and not self.eligible(i)]
        for i in waits:  # affordability crossings: a purchase, or the exact start of a hard wall
            c, amt = self.price(i)
            cap = self.M.currencies[c].get("cap")
            if not self.ge(self.bal[c], amt) and (cap is None or amt <= cap):
                w = cv.wait_time(amt, self.bal[c], cur[c])
                if not isinstance(w, cv.Unreachable):
                    cands.append(self.t + w)
        for p in preds:
            if not self.pred(p):
                w = self.pred_time(p, cur)
                if w is not None:
                    cands.append(self.t + w)
        if self.discrete and any(r > 0 for r in self.rates()[1].values()):
            cands.append(self.t + self.M.time["tick_s"])
        return min(cands) if cands else None

    def blocked_reason(self) -> tuple[str, str]:
        act = self.pursuit
        if act[0] == "wait":
            i = act[1]
            if not self.eligible(i):
                return "prerequisite missing", f"{i} requires {json.dumps(_plain(self.requires(i)))}"
            if self.M.kind_of(i) == "item" and not self.buyable(i):
                return "found only", self.found_only_detail(i)
            if self.buyable(i):
                c, amt = self.price(i)
                cap = self.M.currencies[c].get("cap")
                if cap is not None and amt > cap:
                    return "cap below cost", f"{i} costs {amt} {c}; the {c} cap is {cap}"
                if self.rates()[0][c] == 0:
                    return "unreachable: zero income", f"{i} costs {amt} {c}; balance {self.bal[c]}; income 0 {c}/s"
        return act[1] if act[0] == "idle" else "no progress possible", act[2] if len(act) > 2 else ""

    def run(self):
        horizon = self.opts["horizon_s"]
        max_events = self.opts["max_events"]
        self._record_metrics("start")
        self.instant(produce=False)
        while True:
            if self._all_goals():
                self.stop = ("all goals reached", "")
                break
            self.events += 1
            if self.events > max_events:
                self.stop = ("event limit reached", f"{max_events} events")
                break
            nxt = self.next_progress_time()
            if nxt is None:
                self.stop = self.blocked_reason()
                break
            if self.discrete:
                nxt = self.t + self.M.time["tick_s"]
            elif self.session_end is not None:
                nxt = min(nxt, self.session_end)
            if nxt > horizon:
                if not self.discrete:
                    self.advance_to(horizon)
                    self._check_goals()
                self.stop = ("horizon reached", f"active time {horizon} s")
                break
            self.advance_to(nxt)
            self.instant()
            if self.session_end is not None and self.t >= self.session_end:
                self.end_session()
                if not self.discrete:
                    self.instant()  # the next session starts: offline earnings arrive in its rewards phase
        for w in self.hard_walls:
            w["open_at_end"] = w["end_s"] is None
            if w["end_s"] is None:
                w["duration_s"] = self.t - w["start_s"]
        self._event("stop", reason=self.stop[0], detail=self.stop[1])
        return self


def _plain(x):
    """JSON-ready copy: Fraction -> 'p/q' string, sets sorted; refuses non-finite floats."""
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, float):
        if not math.isfinite(x):
            raise ValueError("non-finite number in report")
        return x
    if isinstance(x, dict):
        return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_plain(v) for v in x]
    if isinstance(x, set):
        return sorted(_plain(v) for v in x)
    return x


def _approx(x):
    return None if x is None else float(x)


def spike_rule(sp, old, new):
    """(improvement, ratio, rule or None) for one change of a spike metric. Hits/TTK: lower is better;
    hits/TTD and production: higher is better. No threshold declared -> rule None (not evaluated)."""
    lower_better = sp["metric"] in LOWER_IS_BETTER
    if old is None or new is None:
        gained =(old is None and new is not None) if lower_better else (old is not None and new is None)
        rule = "capability gained (was not possible)" if gained and ("min_change" in sp or "min_ratio" in sp) else None
        return None, None, rule
    imp = (old - new) if lower_better else (new - old)
    ratio = (cv._div(old, new) if new else None) if lower_better else (cv._div(new, old) if old else None)
    rule = None
    if imp > 0 and "min_change" in sp and imp >= sp["min_change"]:
        rule = f"improvement >= {sp['min_change']}"
    elif imp > 0 and "min_ratio" in sp and ratio is not None and ratio >= sp["min_ratio"]:
        rule = f"ratio >= {sp['min_ratio']}"
    return imp, ratio, rule


# ---------------------------------------------------------------- policies

def _buy_or_wait(sim, i):
    if sim.eligible(i) and sim.affordable(i):
        return ("buy", i)
    return ("wait", i)


def _can_fight(sim, eid):
    """The policy's fight test: the preview duel is a win; for a boss with policies.boss_attempt, the preview
    margin is >= min_margin instead, and after a loss the same stats do not retry a fight with no random input."""
    e = sim.M.enemies[eid]
    if e.get("once") and eid in sim.defeated:
        return False
    res, margin = sim.preview_margin(eid)
    ba = sim.M.policy_cfg.get("boss_attempt")
    if ba is None or not e.get("boss"):
        return res["outcome"] == "win"
    if sim.lost_at.get(eid) == sim.stat_signature() and sim.skill.get("accuracy", 1) == 1:
        return False
    return margin >= ba["min_margin"]


def _earn(sim, currency):
    """The eligible enemy the policy can fight with the most `currency` per second (preview duel time +
    overhead_s), or None."""
    best, rate = None, None
    for eid, e in sim.M.enemies.items():
        amt = e.get("rewards", {}).get(currency, 0)
        if amt <= 0 or not sim.eligible(eid) or (e.get("once") and eid in sim.defeated):
            continue
        res = sim.preview(eid)
        if res["outcome"] != "win":
            continue
        r = amt / (res["time_s"] + e["overhead_s"])
        if rate is None or r > rate:
            best, rate = eid, r
    return best


def _step_for(sim, i):
    kind = sim.M.kind_of(i)
    if kind == "item" and not sim.buyable(i):  # found only: fight an enemy that drops it
        for eid, e in sim.M.enemies.items():
            drops_it = any(dr["item"] == i and dr["chance"] > 0 for dr in e.get("drops", []))
            if drops_it and sim.eligible(eid) and _can_fight(sim, eid):
                return ("fight", eid)
        return ("idle", "found only", sim.found_only_detail(i))
    if kind in ("producer", "item"):
        return _buy_or_wait(sim, i)
    if not sim.eligible(i):
        return ("wait", i)
    if kind == "activity":
        return ("do", i)
    if _can_fight(sim, i):
        return ("fight", i)
    return ("idle", "cannot win duel", f"{i}: the policy's preview duel is not a win with current stats")


def _cheapest(sim):
    cands = [i for i in sim.purchasables() if sim.eligible(i)]
    if not cands:
        return ("idle", "no eligible purchase", "every purchasable is owned or locked")
    best = min(cands, key=lambda i: sim.price(i)[1])  # min() keeps the first in model order on ties
    return _buy_or_wait(sim, best)


def _greedy(sim):
    obj = sim.M.policy_cfg.get("objective_currency")
    if obj is None:
        raise ModelError("greedy-roi needs policies.objective_currency")
    best, score = None, None
    for i in sim.purchasables():
        if not sim.eligible(i):
            continue
        g = sim.gain(i, obj)
        if g <= 0:
            continue
        price = sim.price(i)[1]
        s = math.inf if price == 0 else g / price
        if score is None or s > score:
            best, score = i, s
    return _buy_or_wait(sim, best) if best is not None else _cheapest(sim)


def _save_for(sim, tgt):
    if sim.done(tgt):
        return _cheapest(sim)
    step = _step_for(sim, tgt)
    if step[0] in ("buy", "fight", "do") or not sim.M.enemies:
        return step
    # the target cannot be taken now: keep earning by fighting (gold for its price, else the objective currency)
    obj = sim.M.policy_cfg.get("objective_currency")
    need = sim.price(tgt)[0] if sim.buyable(tgt) and not sim.affordable(tgt) else obj
    eid = (_earn(sim, need) if need else None) or (_earn(sim, obj) if obj and obj != need else None)
    return ("fight", eid) if eid else step


def _fight_best(sim, grind_level=None):
    for i in sorted((i for i in sim.purchasables() if sim.eligible(i) and sim.affordable(i)),
                    key=lambda i: sim.price(i)[1]):
        return ("buy", i)
    obj = sim.M.policy_cfg.get("objective_currency")
    if obj is None:
        raise ModelError("fight-best and grind-to-level need policies.objective_currency")
    allow_boss = grind_level is None or sim.level >= grind_level
    for eid, e in sim.M.enemies.items():
        if e.get("boss") and eid not in sim.defeated and allow_boss and sim.eligible(eid) and _can_fight(sim, eid):
            return ("fight", eid)
    beatable = []
    for eid, e in sim.M.enemies.items():
        if not sim.eligible(eid) or (e.get("once") and eid in sim.defeated):
            continue
        res = sim.preview(eid)
        if res["outcome"] == "win":
            beatable.append((eid, e, res))
    best, rate = None, None
    for eid, e, res in beatable:
        if e.get("boss") and not allow_boss:
            continue
        r = e.get("rewards", {}).get(obj, 0) / (res["time_s"] + e["overhead_s"])
        if rate is None or r > rate:
            best, rate = eid, r
    if best is None or rate <= 0:
        return ("idle", "cannot win duel", "no eligible enemy is beatable with current stats")
    return ("fight", best)


def decide(sim):
    pol, cfg = sim.policy, sim.opts
    if pol == "buy-next-in-order":
        order = sim.M.order or [(i, None) for i in sim.purchasables()]
        for i, until in order:
            if i not in sim.free_bought and not sim.done(i, until):
                return _step_for(sim, i)
        return ("idle", "no eligible purchase", "the order list is finished")
    if pol == "cheapest-eligible":
        return _cheapest(sim)
    if pol == "greedy-roi":
        return _greedy(sim)
    if pol == "save-for":
        return _save_for(sim, cfg["target"])
    if pol == "fight-best":
        return _fight_best(sim)
    return _fight_best(sim, grind_level=cfg["target_level"])


# ---------------------------------------------------------------- report

def _soft_walls(sim, thresholds, top):
    steps = sim.steps
    ranked = sorted(range(len(steps)), key=lambda k: (-steps[k]["wait_s"], k))[:top]
    slowest = [{"step": steps[k]["label"], "end_active_s": steps[k]["t_active_s"], "wait_s": steps[k]["wait_s"],
                "wait_s_approx": _approx(steps[k]["wait_s"])} for k in ranked]
    if not thresholds:
        return {"evaluated": False, "reason": "no soft-wall threshold declared (model analysis.soft_wall or "
                                              "--soft-wall-s / --soft-wall-ratio)", "walls": [], "slowest_steps": slowest}
    return {"evaluated": True, "thresholds": thresholds, "walls": sim.soft_walls, "slowest_steps": slowest}


def _spikes(sim, top):
    out = {"metrics": [], "spikes": [], "changes_ranked": []}
    any_threshold = False
    for sp in sim.M.analysis.get("spikes", []):
        has_t = "min_change" in sp or "min_ratio" in sp
        any_threshold = any_threshold or has_t
        hist = sim.metrics[sp["id"]]
        for a, b in zip(hist, hist[1:]):
            if b.get("segment_start"):
                continue  # the metric was inactive (active_when false) in between: no change is measured across
            imp, ratio, rule = spike_rule(sp, a["value"], b["value"])
            ch = {"metric": sp["id"], "t_active_s": b["t_active_s"], "t_calendar_s": b["t_calendar_s"],
                  "t_active_s_approx": _approx(b["t_active_s"]), "from": a["value"], "to": b["value"],
                  "cause": b["cause"], "improvement": imp, "ratio": ratio}
            out["changes_ranked"].append(ch)
            if rule:
                out["spikes"].append({**ch, "rule": rule})
        if sim.lean:  # keep segment starts, spikes and the last value
            hist = [h for k, h in enumerate(hist) if h.get("segment_start") or h.get("spike") or k == len(hist) - 1]
        out["metrics"].append({"id": sp["id"], "metric": sp["metric"], "reference": sp.get("enemy", sp.get("currency")),
                               "direction": "lower is better" if sp["metric"] in LOWER_IS_BETTER else "higher is better",
                               "active_when": sp.get("active_when"),
                               "thresholds": {k: sp[k] for k in ("min_change", "min_ratio") if k in sp} or None,
                               "evaluated": has_t, "history": hist})
    out["changes_ranked"].sort(key=lambda c: (-(float(c["ratio"]) if c["ratio"] is not None else 0.0),
                                              float(c["t_active_s"])))
    out["changes_ranked"] = out["changes_ranked"][:top]
    out["evaluated"] = any_threshold
    if not any_threshold:
        out["reason"] = "no spike metric declares min_change or min_ratio; changes listed, spikes not evaluated"
    return out


def _goal_reason(sim, g):
    """Most specific reason a goal was not reached."""
    stop, detail = sim.stop
    (k, a), = g["when"].items()
    i = a[0] if k == "owned" else (a if k in ("item", "defeated", "completed") else None)
    if k == "item" and not sim.buyable(i) and not any(
            dr["item"] == i and dr["chance"] > 0 for e in sim.M.enemies.values() for dr in e.get("drops", [])) \
            and not any(i in rw.get("items", []) for rw in (sim.M.levels or {}).get("rewards", [])):
        return "found only", sim.found_only_detail(i) + "; no source can give it"
    if stop in ("horizon reached", "event limit reached"):
        return stop, detail
    if i is not None and sim.requires(i) is not None and not sim.eligible(i):
        return "prerequisite missing", f"{i} requires {json.dumps(_plain(sim.requires(i)))}"
    if i is not None and sim.M.kind_of(i) == "item" and not sim.buyable(i):
        return "found only", sim.found_only_detail(i)
    if i is not None and sim.buyable(i):
        c, amt = sim.price(i)
        cap = sim.M.currencies[c].get("cap")
        if cap is not None and amt > cap:
            return "cap below cost", f"{i} costs {amt} {c}; the {c} cap is {cap}"
        if sim.rates()[0][c] == 0 and not sim.ge(sim.bal[c], amt):
            return "unreachable: zero income", f"{i} costs {amt} {c}; balance {sim.bal[c]}; income 0 {c}/s"
    return stop, detail


def _timeline(sim):
    out = []
    for g in sim.M.goals:
        hit = sim.goal_hits.get(g["id"])
        rec = {"goal": g["id"], "label": g.get("label", g["id"]), "when": g["when"], "reached": hit is not None,
               "active_s": hit and hit["t_active_s"], "active_s_approx": _approx(hit and hit["t_active_s"]),
               "calendar_s": hit and hit["t_calendar_s"], "calendar_s_approx": _approx(hit and hit["t_calendar_s"])}
        if hit is None:
            rec["reason"], rec["detail"] = _goal_reason(sim, g)
        w = g.get("window")
        if w is None:
            rec["window"] = None
            rec["verdict"], rec["evidence"] = "not testable", "no target window declared"
        else:
            rec["window"] = w
            rec["verdict"], rec["evidence"] = _window_verdict(sim, w, hit, rec)
        out.append(rec)
    return out


def _window_verdict(sim, w, hit, rec):
    lo, hi, basis = w.get("min_s"), w.get("max_s"), w["basis"]
    bounds = f"[{lo if lo is not None else '-'}, {hi if hi is not None else '-'}] s ({basis} time)"
    if basis == "calendar" and sim.pattern is None:
        return "not testable", "calendar window, but no session pattern was selected (--sessions)"
    if hit is None:
        now = sim.t if basis == "active" else sim.cal
        if rec["reason"] in ("horizon reached", "event limit reached") and (hi is None or now < hi):
            return "not testable", f"not reached; the run stopped ({rec['reason']}) at {now} s before the window closed"
        return "fail", f"not reached ({rec['reason']}); window {bounds}"
    t = hit["t_active_s"] if basis == "active" else hit["t_calendar_s"]
    inside = (lo is None or t >= lo) and (hi is None or t <= hi)
    shown = f"{t} s" if float(t).is_integer() else f"{t} s (= {float(t):.6g} s)"
    return ("pass" if inside else "fail"), \
        f"measured {basis} time {shown} is {'inside' if inside else 'outside'} the declared window {bounds}"


def _precision(sim):
    out = {}
    for c, d in sim.M.currencies.items():
        mx = max(sim.maxbal[c], sim.lifetime[c], sim.best_run[c], sim.run_earned[c])
        rec = {"max_reached": mx, "exceeds_2_53": mx > TWO_53, "smallest_unit": d.get("smallest_unit")}
        try:
            fm = float(mx)
            if d.get("smallest_unit") is None:
                rec["unit_lost_in_float"] = None
                rec["unit_check"] = "not checked: no smallest_unit declared"
            else:
                rec["unit_lost_in_float"] = fm + float(d["smallest_unit"]) == fm
                rec["unit_check"] = "adding the smallest unit at the maximum does not change a double" \
                    if rec["unit_lost_in_float"] else "ok at the maximum reached"
        except OverflowError:
            rec["unit_lost_in_float"] = True
            rec["unit_check"] = "maximum exceeds the double range"
        rec["flagged"] = bool(rec["exceeds_2_53"] or rec["unit_lost_in_float"])
        out[c] = rec
    return out


def _ledger(sim):
    out = {}
    for c, L in sim.ledger.items():
        total = L["start"] + sum(L["sources"].values(), sim.Z) - sum(L["sinks"].values(), sim.Z) \
            + sum(L["adjustments"].values(), sim.Z)
        out[c] = {"start": L["start"], "sources": L["sources"], "sinks": L["sinks"], "transfers_in": {},
                  "transfers_out": {}, "adjustments": L["adjustments"], "end": sim.bal[c],
                  "residual": sim.bal[c] - total}
    return out


def _curves(sim):
    """Series for the chart, from the model tables (no run data except the index range reached)."""
    M, out = sim.M, []
    for pid, p in M.producers.items():
        targets = [g["when"]["owned"][1] for g in M.goals if "owned" in g["when"] and g["when"]["owned"][0] == pid]
        hi = int(max([sim.max_owned[pid]] + targets))
        lo = int(p["start_owned"])
        hi = max(hi, lo + 1)
        save = sim.owned[pid]
        costs, cum, total, income = [], [], sim.Z, []
        for k in range(lo, hi + 1):
            sim.owned[pid] = k
            if "cost" in p:
                price = sim.price(pid)[1]
                total += price
                costs.append([k, price])
                cum.append([k + 1, total])
            mult = cv.milestone_product(1, [(ms["owned"], ms["mult"]) for ms in p.get("milestones", [])], k)
            income.append([k, sum(p["produces"].values()) * k * mult])
        sim.owned[pid] = save
        if "cost" in p:
            cur = p["cost"]["currency"]
            out.append({"id": f"cost:{pid}", "title": f"{pid}: price of the next unit", "x": f"{pid} owned",
                        "y": f"price ({cur})", "points": costs})
            out.append({"id": f"cumulative:{pid}", "title": f"{pid}: cumulative spend",
                        "x": f"{pid} owned after buying", "y": f"total spent ({cur})", "points": cum})
        out.append({"id": f"income:{pid}", "title": f"{pid}: output at k owned (milestones only)",
                    "x": f"{pid} owned", "y": "units per second", "points": income})
    if M.levels:
        cum = sim.cumxp
        per = cv.per_level_from_cumulative(cum)
        out.append({"id": "xp:per_level", "title": "XP to next level", "x": "level",
                    "y": f"{M.levels['currency']} from level l to l+1", "points": [[l + 1, e] for l, e in enumerate(per)]})
        out.append({"id": "xp:cumulative", "title": "Cumulative XP at level start", "x": "level",
                    "y": f"cumulative {M.levels['currency']}", "points": [[l + 1, x] for l, x in enumerate(cum)]})
    refs = [sp for sp in M.analysis.get("spikes", []) if sp["metric"] == "hits_to_kill"]
    if refs and M.levels:
        series = []
        save_lvl, save_items = sim.level, sim.items
        sim.items = set()
        for sp in refs:
            pts = []
            for lvl in range(1, int(M.levels["max_level"]) + 1):
                sim.level = lvl
                v = sim.metric_value(sp)
                if v is not None:
                    pts.append([lvl, v])
            series.append({"name": sp["enemy"], "points": pts})
        sim.level, sim.items = save_lvl, save_items
        out.append({"id": "hits_to_kill:per_level", "title": "Hits to kill per level (base stats, no gear)",
                    "x": "player level", "y": "hits", "series": series})
    return out


def _summary_runs(sims, model):
    timelines = [_timeline(s) for s in sims]
    goals = []
    for g in model.goals:
        times = [float(s.goal_hits[g["id"]]["t_active_s"]) for s in sims if g["id"] in s.goal_hits]
        lo, hi = wilson_interval(len(times), len(sims))
        rec = {"goal": g["id"], "reached_runs": len(times), "runs": len(sims), "proportion": len(times) / len(sims),
               "wilson_95": [lo, hi]}
        if times:
            rec["active_s_min"], rec["active_s_median"], rec["active_s_max"] = \
                min(times), statistics.median(times), max(times)
        if g.get("window") is not None:
            verdicts = [next(r["verdict"] for r in tl if r["goal"] == g["id"]) for tl in timelines]
            n_pass = verdicts.count("pass")
            lo, hi = wilson_interval(n_pass, len(sims))
            rec["window_verdicts"] = {v: verdicts.count(v) for v in ("pass", "fail", "not testable")}
            rec["window_pass_proportion"], rec["window_pass_wilson_95"] = n_pass / len(sims), [lo, hi]
        goals.append(rec)
    stops = {}
    for s in sims:
        stops[s.stop[0]] = stops.get(s.stop[0], 0) + 1
    return {"goals": goals, "stop_reasons": dict(sorted(stops.items())),
            "interval_method": "Wilson score, 95 % (NIST/SEMATECH e-Handbook W05); runs share one seeded generator",
            "note": "proportions describe this policy on this model, not a player population"}


def simulate(model_source, policy: str, *, mode: str = "exact", target=None, target_level=None, skill=None,
             sessions=None, seed=None, runs=None, horizon_s=None, soft_wall_s=None, soft_wall_ratio=None,
             top: int = 10, max_events: int = 1_000_000, model_path_label=None, trace_out=None,
             lean: bool = False, lean_steps: int | None = None) -> dict:
    """Run the simulator and return the report dict (JSON-ready). model_source: path or raw dict.
    lean=True: no event trace, steps kept only at resets, goals, soft walls and spikes, metric histories
    kept only at segment starts, spikes and the last value (for month-long runs). lean_steps=N also keeps the
    first N steps in full (the early wait pattern)."""
    if lean_steps is not None and (not lean or lean_steps < 0):
        raise ValueError("--lean-steps needs --lean and a count >= 0")
    if isinstance(model_source, dict):
        raw = json.loads(json.dumps(model_source, default=str), parse_float=Fraction)
        sha, path_label = None, model_path_label
    else:
        raw, sha = read_model(model_source)
        path_label = model_path_label or Path(model_source).as_posix()
    if mode not in ("exact", "float"):
        raise ValueError("mode must be exact or float")
    if policy not in POLICIES:
        raise ValueError(f"unknown policy {policy!r}; known: {', '.join(POLICIES)}")
    M = Model(raw, exact=mode == "exact")
    if policy == "save-for" and (target is None or M.kind_of(target) is None):
        raise ValueError("save-for needs --target with a known producer, item, enemy or activity id")
    if policy == "grind-to-level" and target_level is None:
        raise ValueError("grind-to-level needs --target-level")
    if skill is not None and skill not in M.skills:
        raise ValueError(f"unknown skill profile {skill!r}; model has {sorted(M.skills)}")
    if sessions is not None and sessions not in M.sessions:
        raise ValueError(f"unknown session pattern {sessions!r}; model has {sorted(M.sessions)}")
    random_model = M.has_randomness(skill)
    if random_model:
        if seed is None or runs is None:
            raise ValueError("the model has random inputs: --seed and --runs are required")
    else:
        if runs not in (None, 1):
            raise ValueError("the model has no random inputs: repeating the run gives the same path; use runs=1")
        runs = 1
    if runs < 1:
        raise ValueError("runs must be >= 1")
    num = (lambda x: Fraction(x)) if M.exact else float
    if horizon_s is not None:
        horizon, horizon_src = num(horizon_s), "cli"
    elif "horizon_active_s" in M.run_cfg:
        horizon, horizon_src = M.run_cfg["horizon_active_s"], "model run.horizon_active_s"
    else:
        raise ValueError("a run horizon is required: model run.horizon_active_s or --horizon-s")
    thresholds = {}
    sw = M.analysis.get("soft_wall") or {}
    for k in ("min_wait_s", "min_ratio_to_previous"):
        if k in sw:
            thresholds[k] = sw[k]
    if soft_wall_s is not None:
        thresholds["min_wait_s"] = num(soft_wall_s)
    if soft_wall_ratio is not None:
        thresholds["min_ratio_to_previous"] = num(soft_wall_ratio)
    for g in M.goals:
        keys = set(_pred_keys(g["when"]))
        if "soft_walls" in keys and not thresholds:
            raise ValueError(f"goal {g['id']} tests soft walls, but no soft-wall threshold is declared "
                             "(model analysis.soft_wall or --soft-wall-s / --soft-wall-ratio)")
        for sid in _pred_args(g["when"], "spikes"):
            sp = next(x for x in M.analysis["spikes"] if x["id"] == sid[0])
            if "min_change" not in sp and "min_ratio" not in sp:
                raise ValueError(f"goal {g['id']} tests spikes on {sid[0]}, which declares no min_change or min_ratio")
    opts = {"target": target, "target_level": target_level, "skill": skill, "sessions": sessions,
            "horizon_s": horizon, "max_events": max_events, "soft_thresholds": thresholds, "lean": lean}
    rng = random.Random(seed) if random_model else None
    sims = [Sim(M, policy, opts, rng).run() for _ in range(runs)]
    s = sims[0]
    timeline = _timeline(s)
    assumed = [i for i in M.inputs if i["src"] in ASSUMED_LABELS]
    counts = {}
    for i in M.inputs:
        k = i["src"].split(":")[0]
        counts[k] = counts.get(k, 0) + 1
    behaviour = [f"policy {policy}: one modelled strategy, not the player population"]
    if skill:
        behaviour.append(f"skill profile {skill} (model skill_profiles.{skill})")
    if sessions:
        behaviour.append(f"session pattern {sessions} (model sessions.patterns.{sessions})")
    if M.enemies:
        behaviour.append("the fight-choosing preview assumes every attack lands; actual fights roll accuracy")
        ba = M.policy_cfg.get("boss_attempt")
        if ba is not None:
            behaviour.append(f"bosses are attempted at a preview margin >= {ba['min_margin']} "
                             f"(model policies.boss_attempt); {ba['recovery_s']} s recovery after a lost fight")
        if policy == "save-for":
            behaviour.append("save-for keeps fighting for income or XP while its target is locked or unaffordable")
    ledgers = [_ledger(x) for x in sims]
    report = {
        "tool": "progression_sim",
        "version": VERSION,
        "curves_version": cv.VERSION,
        "model": {"path": path_label, "sha256": sha, "revision": M.revision, "title": M.title},
        "mode": mode,
        "policy": {"name": policy, "target": target, "target_level": target_level, "skill_profile": skill,
                   "session_pattern": sessions},
        "seed": seed if random_model else None,
        "runs": runs,
        "random_inputs": random_model,
        "semantics": {
            "event_order": M.event_order, "time": M.time, "duel": M.duel_cfg,
            "horizon_active_s": horizon, "horizon_source": horizon_src,
            "calendar": "session pattern " + sessions if sessions else "not modelled (no session pattern selected)",
            "offline": M.offline if M.offline is not None else "not modelled (the model gives no offline contract)",
            "prestige_offline_counts_toward_basis":
                M.prestige.get("offline_counts_toward_basis", True) if M.prestige else None,
            "prestige_min_award": M.prestige.get("min_award") if M.prestige else None,
            "boss_attempt": M.policy_cfg.get("boss_attempt"),
            "level_rewards": "granted once per level per simulated player" if (M.levels or {}).get("rewards") else None,
            "hard_walls": "every gated buyable or enemy: from affordable (or beatable) while locked until it unlocks; "
                          "an activity only while the policy pursues it",
        },
        "lean": {"on": True, "first_steps_kept": lean_steps or 0,
                 "omitted": ["trace", "steps after the first first_steps_kept other than resets, goals, soft walls "
                             "and spikes", "metric history between segment starts, spikes and the last value"]}
        if lean else {"on": False},
        "warnings": s.warnings,
        "never_claims": ["a population forecast (one policy is one strategy)", "that any target feeling passed",
                         "that the game is fun", "any default threshold, rate, horizon or session length"],
        "assumptions": {
            "inputs": assumed,
            "behaviour": behaviour,
            "note": "every result below is conditional on all listed inputs and the behaviour lines; "
                    "the tool does not trace which result uses which input",
        },
        "provenance_counts": dict(sorted(counts.items())),
        "stop": {"reason": s.stop[0], "detail": s.stop[1], "active_s": s.t, "active_s_approx": float(s.t),
                 "calendar_s": s.cal, "calendar_s_approx": _approx(s.cal)},
        "timeline": timeline,
        "walls": {"soft": _soft_walls(s, thresholds, top),
                  "hard": [{**w, "start_s_approx": float(w["start_s"]), "duration_s_approx": _approx(w["duration_s"])}
                           for w in s.hard_walls]},
        "spikes": _spikes(s, top),
        "blocked": [{"goal": r["goal"], "reason": r["reason"], "detail": r["detail"]}
                    for r in timeline if not r["reached"]],
        "unlocks": s.unlock_log,
        "prestige": s.prestige_log,
        "fights": {**s.fights, "per_enemy": s.fight_log,
                   "note": "time_s is the duel's actual deciding death; *_isolated_s are N = ceil(H/d) and "
                           "t0 + (N-1)*tau for each side alone (TTK, TTD)"} if M.enemies else None,
        "ledger": ledgers[0],
        "ledger_all_runs_residual_zero": all(v["residual"] == 0 for L in ledgers for v in L.values()),
        "precision": _precision(s),
        "final_state": {"balances": s.bal, "owned": s.owned, "items": s.items, "unlocked": s.unlocked,
                        "defeated": s.defeated, "completed": s.completed, "level": s.level, "prestiges": s.prestiges,
                        "lifetime": s.lifetime},
        "steps": _lean_steps(s, timeline, lean_steps or 0) if lean else s.steps,
        "curves": _curves(s),
    }
    if runs > 1:
        report["runs_summary"] = _summary_runs(sims, M)
    if lean:
        report["trace"] = None
    elif trace_out:
        Path(trace_out).parent.mkdir(parents=True, exist_ok=True)
        Path(trace_out).write_text(json.dumps(_plain(s.trace), indent=1) + "\n", encoding="utf-8")
        report["trace"] = {"path": Path(trace_out).as_posix(), "events": len(s.trace)}
    else:
        report["trace"] = s.trace
    return _plain(report)


def _key(p):
    return json.dumps(_plain(p), sort_keys=True)


def _pred_keys(p):
    (k, a), = p.items()
    yield k
    if k in ("all", "any"):
        for q in a:
            yield from _pred_keys(q)
    elif k == "not":
        yield from _pred_keys(a)


def _pred_args(p, key):
    (k, a), = p.items()
    if k == key:
        yield a
    if k in ("all", "any"):
        for q in a:
            yield from _pred_args(q, key)
    elif k == "not":
        yield from _pred_args(a, key)


def _lean_steps(sim, timeline, first=0):
    goal_t = {r["active_s"] for r in timeline if r["reached"]}
    spike_at = {(h["t_active_s"], h["cause"]) for hist in sim.metrics.values() for h in hist if h.get("spike")}
    return [s for k, s in enumerate(sim.steps) if k < first or s["kind"] == "prestige" or s.get("soft_wall")
            or s["t_active_s"] in goal_t or (s["t_active_s"], s["label"]) in spike_at]


def dumps(report: dict) -> str:
    return json.dumps(report, indent=1, ensure_ascii=True) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sim", description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model", help="game model JSON")
    ap.add_argument("--policy", required=True, choices=POLICIES)
    ap.add_argument("--mode", default="exact", choices=("exact", "float"))
    ap.add_argument("--target", help="save-for: producer/item/enemy/activity id")
    ap.add_argument("--target-level", type=int, help="grind-to-level: level to reach before bosses")
    ap.add_argument("--skill", help="skill profile name from the model")
    ap.add_argument("--sessions", help="session pattern name from the model")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--runs", type=int)
    ap.add_argument("--horizon-s", help="active-time horizon in seconds (overrides the model)")
    ap.add_argument("--soft-wall-s", help="soft wall: minimum wait in active seconds")
    ap.add_argument("--soft-wall-ratio", help="soft wall: minimum multiple of the previous step's wait")
    ap.add_argument("--top", type=int, default=10, help="rows in ranked lists (display only)")
    ap.add_argument("--max-events", type=int, default=1_000_000)
    ap.add_argument("--out", help="also write the report here")
    ap.add_argument("--trace-out", help="write the event trace here instead of inline")
    ap.add_argument("--lean", action="store_true",
                    help="small report: no trace; steps only at resets, goals, soft walls and spikes")
    ap.add_argument("--lean-steps", type=int, help="with --lean: also keep the first N steps in full")
    a = ap.parse_args(argv)
    try:
        rep = simulate(a.model, a.policy, mode=a.mode, target=a.target, target_level=a.target_level, skill=a.skill,
                       sessions=a.sessions, seed=a.seed, runs=a.runs, horizon_s=a.horizon_s,
                       soft_wall_s=a.soft_wall_s, soft_wall_ratio=a.soft_wall_ratio, top=a.top,
                       max_events=a.max_events, trace_out=a.trace_out, lean=a.lean,
                       lean_steps=a.lean_steps)
    except (ModelError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    text = dumps(rep)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
