> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-craft`. Tools built in J011-T07 and extended in J011-T11 after real use (sim and chart 1.2.0 after J011-T13; 97 offline tests, standard library only). The authority for the model-file schema and every definition is the header docstring of `tools/progression/sim.py`; this page is how to use the tools and read their output. Never edit the tools; ask the lead for a change. Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (new §6: reward rates, the decision check, luck vs skill, the paid odds check; each run once on the example models before it was written here; §6a-b repaired in review round 1: repeated completions and wins from the trace, the decision check per run between resets).

# The tools: curves, simulator, charts

| Tool | Does | Never does |
| --- | --- | --- |
| `tools/progression/curves.py` | exact formulas (Fraction): curve library, per-level ↔ cumulative, time from a requirement, bulk buy and max affordable (inequality-checked), waits (zero income → `UNREACHABLE`), payback, prestige (3 published formulas + accounting rules + inverse), offline, hits-to-kill, TTK both conventions, effective health, stacking, luck (c/p, 1 − (1 − p)^n, n_q, pity) | pick a coefficient; extrapolate a table past its end |
| `tools/progression/sim.py` | plays one named policy through one JSON model; JSON report: goals in active and calendar time with pass / fail / not testable, soft and hard walls, power spikes, blocked paths with reasons, fights (TTK, TTD, duel time), ledger per currency, precision flags, assumptions list, optional event trace | fill a missing number (no default rate, session, horizon, threshold, offline cap); call a policy optimal; forecast a population |
| `tools/progression/chart.py` | one self-contained HTML page from one or more reports: curves (log axis when > 3 orders of magnitude), timeline per policy with walls and spikes, window bands with verdicts, assumptions panel, run identity, tables for every value | compute anything new |

## 1. Write the model (schema: `sim.py` docstring)
- **Every number is a value object** `{"v": 4, "src": "<label>"}`, label one of `published:<source id>`, `owner:<decision id>`, `measured:<dataset>`, `EXAMPLE ASSUMPTION`, `PROPOSAL`. A bare number is an error. Exact rationals as `"107/100"`.
- Tables: `meta` (revision, event_order, time mode, duel rules) · `currencies` (start, cap, smallest_unit) · `producers` (output, cost curve with index_offset and rounding, milestones, requires) · `items` (cost, requires, effects on stats, producers or currencies) · `levels` (per-level or cumulative XP) · `player.stats` (curves by level) · `enemies` (hp, damage, interval, overhead, rewards, drops, boss, once) · `activities` (duration, success chance, rewards; this is how obbies and tycoon tasks fit) · `unlocks` · `prestige` (basis lifetime / maximum / run, rule, formula, reset and keep lists covering every state id, bonus) · `offline` (efficiency, cap) · `sessions.patterns` · `skill_profiles` · `policies` · `goals` (= timeline rows, same ids, with windows) · `analysis` (soft-wall and spike thresholds) · `run.horizon_active_s`.
- **Goals are the feeling timeline.** Use the timeline row id (`TL-03`) as the goal id; window `{basis: active|calendar, min_s, max_s}` from the owner's decision or labelled PROPOSAL / EXAMPLE ASSUMPTION.
- **Thresholds are design decisions.** Soft wall (`min_wait_s`, `min_ratio_to_previous`) and spike (`metric`, `enemy`/`currency`, `min_change`, `min_ratio`) thresholds come from the timeline; without them the report says "not evaluated" and lists the slowest steps.
- **Spikes need reference content:** name the enemy (hits_to_kill, ttk_s) or currency (production_per_s) the spike is measured on (`progression-design` D-06).
- Continuous mode needs piecewise-constant rates (no producers that make producers; use discrete ticks with the creation-tick rule stated). Continuous exact mode with exponential prices grows fractions without bound (a 17 MB report for 18 minutes of play in J011-T08): for long incremental runs use 1-second discrete ticks and whole-unit prices, and `--lean`.
- **Resets that grow** (G-01): any predicate number may be a threshold object `{"curve": spec, "index": "prestiges", "index_offset"?}`; `prestige.min_award` stops resets for tiny awards; `prestige.offline_counts_toward_basis` decides whether offline income feeds the basis (default true). A fixed requirement shortens every later run. With a lifetime-based award, a rising requirement mostly changes how many resets happen and how big each one is, much less the total award over a month (J011-T12: 20 resets instead of 40 by day 21, each +3.6-5.2 % instead of +0.9-2.9 %, total seeds about the same). `--lean` thins steps: keep the exact early trace (waits shrinking, then growing) from a non-lean run in the design file.
- **Rewards on levels** (track rewards): `levels.rewards [{level, currencies?, items?}]`, booked as ledger source `level_reward:<L>`, once per level per player.
- **Orders with counts:** `policies.order` entries `"id"` or `{"id", "until": N}` (units owned, enemy wins or activity completions).
- **Boss attempts:** `policies.boss_attempt {min_margin, recovery_s}` makes policies try a boss at a declared preview margin and count attempts, losses and attempts-to-first-win; without it, policies fight only when the preview wins (no lost fights appear).
- **Spike metrics:** `hits_to_kill`, `ttk_s`, `production_per_s`, and defensive `hits_to_die`, `ttd_s`; `active_when` (a predicate) so content the player cannot reach yet is not measured.
- **Goals on walls and spikes:** predicates `{"soft_walls": N}` (or `{"soft_walls": [N, {"after": predicate}]}` to count only walls after a point, e.g. after a zone opens), `{"spikes": [metric id, N]}` and `{"hard_wall": id}` (goal time = the wall's start) give wall and spike timeline rows a verdict like any goal (thresholds required). Also `{"not": predicate}`.
- **Model limits to state:** no equipment slots (every owned item stacks; two swords add up); defeat times include the enemy's `overhead_s` (walk and respawn), so a first-kill goal includes it.
- Fixtures for engineering (cost at n, X_l, hits per build × enemy, prestige award at L) are computed with `curves.py` in exact mode from the same model revision and shipped in the export (`references/data-handoff.md`); the model file itself has no fixtures section.

## 2. Run it
```text
python tools/progression/sim.py MODEL.json --policy greedy-roi --mode exact --out run/greedy.json
python tools/progression/sim.py MODEL.json --policy save-for --target factory --out run/save.json
python tools/progression/sim.py MODEL.json --policy fight-best --skill struggling --out run/struggle.json
python tools/progression/sim.py MODEL.json --policy fight-best --sessions returning --out run/return.json
python tools/progression/sim.py MODEL.json --policy fight-best --seed 1 --runs 400 --out run/drops.json
python tools/progression/chart.py run/greedy.json run/save.json run/struggle.json --out run/compare.html
```
- Policies: `buy-next-in-order`, `cheapest-eligible`, `greedy-roi` (heuristic, not optimal), `save-for --target`, `fight-best`, `grind-to-level --target-level`; `--skill` applies a struggling profile; `--sessions` applies a session pattern (calendar time, offline, returning after absence).
- Minimum set per question (C-05): an efficient policy, a saver or cheapest-first, a struggling or explorer variant, a returning pattern; paid and unpaid routes as separate models or items when both exist. Incremental games have no fights: explorer = `cheapest-eligible`, impatient player = `save-for` a gated target. Hard walls are recorded for every policy (affordable or beatable but locked → unlocked, with `pursued_by_policy`).
- Horizon for calendar rows: sessions × session length (30 days × 20 min = 36,000 s active); a run stops early when every goal is reached.
- `--lean` keeps goals, resets, walls and spikes and drops the trace (a month run: 2.67 MB → 143 KB); use it for long runs and anything committed. `--lean-steps N` also keeps the first N steps in full (the early "waits shrink, then grow" picture).
- `--mode exact` for fixtures and checks; `float` only for speed on long horizons (the report says which, and float books a `float_rounding` ledger adjustment).
- Randomness (drops, success chances, accuracy < 1) needs `--seed` and `--runs`; decide runs from the precision you need before running; the report gives Wilson 95 % intervals per goal (C-06). A model with no random inputs refuses `--runs > 1`.
- Every run needs a horizon (model or `--horizon-s`).

## 3. Read the report (in this order)
1. **Identity:** model revision + SHA-256, policy, mode, seed, runs. A chart or claim without these is not evidence.
2. **Assumptions:** every EXAMPLE ASSUMPTION / PROPOSAL input. Every result is conditional on all of them (the tool does not trace which result uses which input). Say so in the hand-back.
3. **Ledger:** residual must be `0` in exact mode; named adjustments (cap_loss, reset) explained.
4. **Precision:** any currency over 2^53 or losing its smallest unit → design question, not a footnote.
5. **Blocked paths:** each with its reason; a required goal blocked for any supported policy fails checklist row 5.
6. **Goals:** pass / fail / not testable against windows, per policy. "Pass" is arithmetic only. With `--runs` above 1 the top-level `timeline` holds one run: read `runs_summary.goals` (§6c).
7. **Walls and spikes:** match each to a timeline row (planned) or raise it (unplanned). Hard walls show kind, gate type (`prerequisite`, `chained` with `via` = the locked gates behind it, `timed`, `activity`), the missing prerequisite, time blocked and whether the policy was pursuing the target. Charts mark resets, plot the wait per step against the soft-wall line and each reference metric over time; on an options page a curve shared by several models is drawn once and names them.
8. **Fights (RPG):** TTK, TTD, actual duel time per enemy, attempts and losses with `boss_attempt`; check breakpoints against the reference enemies. A boss at a TTK = TTD tie is decided by the simultaneous-hit rule: engineering must copy that rule exactly.

## 4. Charts for the owner
One page per decision: the compared policies or options side by side, the curves, the timeline with windows. Put the page path (and, for the owner, a published private page if the lead asks) in the hand-back with one line on what to look at. The page already states that each row is one strategy and that a pass is not fun.

## 5. Known limits (after T11, 2026-10-21)
No cap-upgrade items (a cap below cost is a blocked path); no currency conversion or player transfers (ledger slots exist, empty); no equipment slots; `cheapest-eligible` compares prices across currencies by amount (avoid mixed-currency choices or use `save-for`); assumption dependence is not traced per result; level rewards are not re-granted after a reset lowers the level; no reward-rate summary in the report (§6a computes it from the steps and the event trace; `--lean` drops both). Ask the lead for a tool ticket when a model needs one of these.

## 6. Measures I compute from reports
Short scripts I keep in my working folder; each reads one report or table of this model revision and prints numbers. Each was run once on the example models: what makes it give a wrong number without an error is written under it.

**a. Reward rates (for the tier table).** Read the report's `reward_rates` block (`sim.py` since J019 G3-P8): per step kind and id, fight win and successful activity completion (repeats included: obby runs, tycoon tasks), the count, rate per active hour, first time, median and longest gap, plus the longest stretch with no step and with no reward at all. It is kept under `--lean`. Per session = per active hour × the session's active hours. In a multi-run report it is run 1's (see `timeline_scope`).
Wrong without an error: a `--lean` report (it keeps only resets, goals, walls and spikes: 11 greenhouse purchases instead of 265 in the incremental example), hence the guard; a run stopped early by the horizon or "all goals reached" (rates are per active time actually played: the last line prints the stop reason); "no step" is not "no reward" where repeated kills or activity completions pay: read the `wins:` and `completions:` lines and the second stretch (an obby example: 1 step-completion and a 570-second stretch with no step, but 20 completions, 120 per hour, never more than 30 s apart); income ticks are not events, so in an idle game read the stretches against what the screen shows during them.

**b. The decision check.** Input: two full single-run reports of the same model revision from policies with different objectives (`greedy-roi` and `cheapest-eligible`, or `save-for`); never `buy-next-in-order`, which follows the scripted order. The purchase lists are split at each reset, so each run between resets is compared from its start.
```python
import json, sys
def runs(p):
    r = json.load(open(p, encoding="utf-8"))
    if r["lean"]["on"] or r["runs"] != 1: sys.exit(p + ": need a full single-run report (no --lean, --runs 1)")
    out = [[]]
    for s in r["steps"]:
        if s["kind"] == "prestige": out.append([])
        elif s["kind"] == "purchase": out[-1].append(s["id"])
    return r["policy"]["name"], out
(na, A), (nb, B) = runs(sys.argv[1]), runs(sys.argv[2])
for i, (a, b) in enumerate(zip(A, B), 1):
    n = next((j for j, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    print("run", i, ":", na, "vs", nb, "identical first", n, "of", min(len(a), len(b)), "purchases; first difference", a[n:n + 1], b[n:n + 1], "; only", na, sorted(set(a) - set(b)), "; only", nb, sorted(set(b) - set(a)))
if len(A) != len(B): print("runs (resets + 1):", na, len(A), nb, len(B), "; runs past the shorter list are not compared")
```
Reading: a long identical stretch outside a tutorial row is a "no decision" finding (incremental example: run 1 identical for 31 of 233 purchases, runs 3 and 4 for the first 17 after each reset). Two heuristics agreeing is a flag, not proof that no player would choose differently. Not found by the script: a stretch that matches again in the middle of a run (not at a run start), and decisions that are not purchases (which activity, route or enemy): read the purchase lists, or the `completions:` and `wins:` lines of §6a, there by eye. Runs are paired by reset count, not by time.

**c. Luck vs skill.** Input: the same model, the same `--seed` and `--runs`, two `--skill` profiles (or a profile and the default); `--lean` is fine here, `runs_summary` is kept. A model without random inputs refuses `--runs` above 1.
```text
python tools/progression/sim.py MODEL.json --policy fight-best --seed 1 --runs 200 --lean --out run/luck-base.json
python tools/progression/sim.py MODEL.json --policy fight-best --skill struggling --seed 1 --runs 200 --lean --out run/luck-struggling.json
python -c "import json,sys; r=json.load(open(sys.argv[1], encoding='utf-8')); [print(g['goal'], g['reached_runs'], '/', g['runs'], g['window_verdicts'], g['window_pass_wilson_95'], g.get('active_s_median')) for g in r['runs_summary']['goals']]" run/luck-base.json
```
Reading: per goal, compare verdict counts and the median time across profiles against the row's intent (a goal meant for everyone is reached by the struggling profile in some runs; a skill goal separates the profiles more than the seeds do). Wrong without an error: `active_s_median` is the median over the runs that reached the goal only (2 of 40 runs can show a median), so read it only next to `reached_runs`; the top-level `timeline` of a multi-run report is one run; a calendar goal run without `--sessions` shows a pass share of 0 while its verdicts say "not testable"; 100 runs of an 18,000-second RPG model take about 90 s, so plan the run count.

**d. Paid odds check.** Input: the odds table as JSON (`price`, `outcomes` with `id`, `odds` as a `"p/q"` string, `value`, `tier`), the same data the server rolls. `value` is the owner's value label on the price's scale, never a sell-back price: an outcome that can be sold or converted back into the price currency is the stake-and-win-back shape in `platform-policy` rules §A: stop and raise it to the owner. Run from the repository root.
```python
import json, sys
from fractions import Fraction as F
sys.path.insert(0, "tools/progression"); import curves as cv
t = json.load(open(sys.argv[1], encoding="utf-8")); price = F(t["price"]); odds = [F(o["odds"]) for o in t["outcomes"]]
print("odds sum", sum(odds), "(must be exactly 1); expected value per roll", float(sum(p * F(o["value"]) for p, o in zip(odds, t["outcomes"]))), "for", price)
for p, o in zip(odds, t["outcomes"]):
    print(o["id"], "mean cost to first", float(cv.expected_spend(price, p)), "rolls for 90 %", cv.attempts_for_quantile(F(9, 10), p), "99 %", cv.attempts_for_quantile(F(99, 100), p), "below price: reveal only" if F(o["value"]) < price else "tier " + o["tier"])
```
Wrong without an error: odds written as JSON floats (0.1 is not exactly a tenth, so the sum misses 1); a value label on a different scale than the price; the printed percentages are not the display string (rounding and disclaimer: `platform-policy`).
