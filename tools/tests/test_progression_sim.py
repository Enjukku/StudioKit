"""Offline tests for tools/progression/sim.py on the small fixtures in tools/tests/fixtures/progression/.

Paper fixtures (owner research paper, outside git): M01 Lemonade 2016-10-04, M05 chain 2016-10-28,
M04 XP table 2010-07-14. Every other fixture number is labelled EXAMPLE ASSUMPTION or PROPOSAL.
"""

import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "progression"))
import sim  # noqa: E402

FIX = ROOT / "tools" / "tests" / "fixtures" / "progression"


def path(name):
    return FIX / f"{name}.json"


def raw(name):
    return json.loads(path(name).read_text(encoding="utf-8"))


def run(name, policy="cheapest-eligible", **kw):
    src = kw.pop("model", None) or path(name)
    return sim.simulate(src, policy, model_path_label=f"{name}.json", **kw)


def goal(rep, gid):
    return next(g for g in rep["timeline"] if g["goal"] == gid)


class LemonadeM01(unittest.TestCase):
    def test_buy_next_policy_reproduces_paper_waits_exactly(self):
        rep = run("lemonade_m01", "buy-next-in-order")
        self.assertEqual(rep["mode"], "exact")
        waits = [F(s["wait_s"]) for s in rep["steps"]]
        self.assertEqual(waits, [F(400, 167), F(214, 167), F(11449, 12525), F(1225043, 1670000), F(131079601, 208750000)])
        times = [F(goal(rep, f"own{k}")["active_s"]) for k in range(2, 7)]
        self.assertEqual(times, [F(400, 167), F(614, 167), F(57499, 12525), F(26674729, 5010000), F(465947491, 78281250)])
        self.assertEqual(rep["semantics"]["time"], {"mode": "continuous"})

    def test_window_verdict_and_ledger(self):
        rep = run("lemonade_m01", "buy-next-in-order")
        g = goal(rep, "own6")
        self.assertEqual(g["verdict"], "pass")
        self.assertIn("inside the declared window", g["evidence"])
        self.assertEqual(goal(rep, "own2")["verdict"], "not testable")
        self.assertEqual(rep["ledger"]["cash"]["residual"], "0")
        names = [a["input"] for a in rep["assumptions"]["inputs"]]
        self.assertEqual(names, ["goals[4].window.max_s", "analysis.spikes[0].min_ratio", "run.horizon_active_s"])


class DiscreteTicks(unittest.TestCase):
    def coins_at(self, t, produce_in_creation_tick):
        m = raw("m05_chain_discrete")
        m["meta"]["time"]["new_units_produce_in_creation_tick"] = produce_in_creation_tick
        rep = run("m05", model=m, horizon_s=t)
        self.assertEqual(rep["semantics"]["time"]["new_units_produce_in_creation_tick"], produce_in_creation_tick)
        return F(rep["final_state"]["balances"]["coins"])

    def test_tick_model_differs_from_continuous_closed_form_by_a_stated_half_tick(self):
        for t in range(1, 6):
            continuous = F(t * t, 2)  # M05 closed form C(t) = t^2/2
            # new tier-1 generators wait one tick: coins = t(t-1)/2 = t^2/2 - t/2
            self.assertEqual(self.coins_at(t, False), continuous - F(t, 2))
            # new generators produce in their creation tick: coins = t(t+1)/2 = t^2/2 + t/2
            self.assertEqual(self.coins_at(t, True), continuous + F(t, 2))

    def test_continuous_mode_rejects_producer_chains(self):
        m = raw("m05_chain_discrete")
        m["meta"]["time"] = {"mode": "continuous"}
        with self.assertRaisesRegex(sim.ModelError, "piecewise-constant"):
            run("m05", model=m)


class Determinism(unittest.TestCase):
    def test_same_model_policy_seed_gives_byte_identical_json(self):
        cases = [("lemonade_m01", "buy-next-in-order", {}),
                 ("rpg_duel", "fight-best", {"skill": "clumsy", "seed": 11, "runs": 5}),
                 ("obby_random", "buy-next-in-order", {"seed": 7, "runs": 20})]
        for name, pol, kw in cases:
            a = sim.dumps(run(name, pol, **kw))
            b = sim.dumps(run(name, pol, **kw))
            self.assertEqual(a.encode(), b.encode(), name)
        self.assertNotEqual(sim.dumps(run("obby_random", "buy-next-in-order", seed=7, runs=20)),
                            sim.dumps(run("obby_random", "buy-next-in-order", seed=8, runs=20)))


class BlockedPaths(unittest.TestCase):
    def test_zero_income_is_unreachable(self):
        rep = run("zero_income")
        self.assertEqual(rep["blocked"], [{"goal": "first_stand", "reason": "unreachable: zero income",
                                           "detail": "stand costs 10 cash; balance 3; income 0 cash/s"}])
        g = goal(rep, "first_stand")
        self.assertFalse(g["reached"])
        self.assertIsNone(g["active_s"])
        self.assertEqual(g["verdict"], "fail")

    def test_cap_below_cost(self):
        rep = run("cap_block")
        self.assertEqual(rep["blocked"][0]["reason"], "cap below cost")
        self.assertIn("cap is 100", rep["blocked"][0]["detail"])

    def test_policy_without_income_source_is_blocked_not_zero(self):
        rep = run("rpg_duel", "buy-next-in-order")  # the order starts with the sword; gold only comes from fights
        self.assertEqual(rep["stop"]["reason"], "unreachable: zero income")

    def test_horizon_gives_not_testable_before_window_closes(self):
        rep = run("lemonade_m01", "buy-next-in-order", horizon_s="5")
        g = goal(rep, "own6")
        self.assertEqual((g["reason"], g["verdict"]), ("horizon reached", "not testable"))


class IdlePrestige(unittest.TestCase):
    def setUp(self):
        self.rep = run("idle_prestige", "save-for", target="factory")

    def test_hard_wall_and_cap_loss(self):
        hw = self.rep["walls"]["hard"]
        self.assertEqual([(w["id"], w["start_s"], w["end_s"], w["duration_s"]) for w in hw], [("factory", "50", "150", "100")])
        self.assertEqual(hw[0]["missing"], {"unlocked": "permit"})
        self.assertEqual(self.rep["ledger"]["cash"]["adjustments"]["cap_loss"], "-50")

    def test_reset_records_removed_and_kept(self):
        p = self.rep["prestige"]
        self.assertEqual(len(p), 1)
        self.assertEqual(p[0]["award"], 17)  # floor(sqrt(300)) with lifetime 300 at the reset
        self.assertEqual(p[0]["removed"], {"currency:cash": "41", "producer:stand": "6", "item:factory": True})
        self.assertEqual(p[0]["kept"], ["currency:angels", "unlock:permit"])
        self.assertEqual(self.rep["ledger"]["cash"]["adjustments"]["reset"], "-41")
        self.assertEqual(self.rep["final_state"]["balances"]["angels"], "17")

    def test_soft_wall_threshold_and_spikes(self):
        sw = self.rep["walls"]["soft"]
        self.assertTrue(sw["evaluated"])
        self.assertEqual([w["step"] for w in sw["walls"]], ["buy factory"])
        self.assertTrue(self.rep["spikes"]["evaluated"])
        self.assertEqual(self.rep["spikes"]["spikes"][0]["cause"], "buy factory")

    def test_walls_not_evaluated_without_threshold(self):
        m = raw("idle_prestige")
        del m["analysis"]["soft_wall"]
        rep = run("idle", "save-for", target="factory", model=m)
        sw = rep["walls"]["soft"]
        self.assertFalse(sw["evaluated"])
        self.assertEqual(sw["walls"], [])
        self.assertEqual(sw["slowest_steps"][0]["step"], "buy factory")
        rep2 = run("idle", "save-for", target="factory", model=m, soft_wall_ratio="3")
        self.assertEqual(rep2["walls"]["soft"]["thresholds"], {"min_ratio_to_previous": "3"})

    def test_reset_list_must_cover_every_state_id(self):
        m = raw("idle_prestige")
        m["prestige"]["keep"].remove("unlock:permit")
        with self.assertRaisesRegex(sim.ModelError, "unlock:permit"):
            run("idle", model=m)

    def test_greedy_roi_and_cheapest_run(self):
        for pol in ("greedy-roi", "cheapest-eligible"):
            rep = run("idle_prestige", pol)
            self.assertEqual(rep["stop"]["reason"], "all goals reached")
            self.assertEqual(rep["policy"]["name"], pol)


class LedgerAllFixtures(unittest.TestCase):
    def test_residual_exactly_zero(self):
        cases = [("lemonade_m01", "buy-next-in-order", {}), ("m05_chain_discrete", "cheapest-eligible", {}),
                 ("zero_income", "cheapest-eligible", {}), ("cap_block", "cheapest-eligible", {}),
                 ("idle_prestige", "save-for", {"target": "factory"}), ("idle_prestige", "greedy-roi", {}),
                 ("sessions_offline", "cheapest-eligible", {"sessions": "returning"}),
                 ("big_numbers", "cheapest-eligible", {}), ("rpg_duel", "fight-best", {}),
                 ("rpg_duel", "grind-to-level", {"target_level": 4}),
                 ("rpg_duel", "fight-best", {"skill": "clumsy", "seed": 1, "runs": 10}),
                 ("obby_random", "buy-next-in-order", {"seed": 2, "runs": 10})]
        for name, pol, kw in cases:
            rep = run(name, pol, **kw)
            self.assertTrue(rep["ledger_all_runs_residual_zero"], name)
            for c, v in rep["ledger"].items():
                self.assertEqual(v["residual"], "0", (name, c))


class Precision(unittest.TestCase):
    def test_balance_past_2_53_is_flagged(self):
        rep = run("big_numbers")
        p = rep["precision"]
        self.assertTrue(p["cash"]["exceeds_2_53"])
        self.assertTrue(p["cash"]["unit_lost_in_float"])
        self.assertTrue(p["cash"]["flagged"])
        self.assertFalse(p["gems"]["flagged"])


class SessionsOffline(unittest.TestCase):
    def test_calendar_time_and_offline_contract(self):
        rep = run("sessions_offline", sessions="regular")
        g = goal(rep, "save1000")
        # 4 sessions of 120 s: 480 produced + 4 offline grants of 1/2 * 1/s * min(600, 300) = 600
        self.assertEqual((g["active_s"], g["calendar_s"]), ("480", "2880"))
        self.assertEqual(rep["ledger"]["cash"]["sources"], {"production:stand": "480", "offline": "600"})
        self.assertEqual(g["verdict"], "pass")

    def test_returning_after_absence(self):
        g = goal(run("sessions_offline", sessions="returning"), "save1000")
        self.assertEqual((g["active_s"], g["calendar_s"]), ("480", str(480 + 600 + 604800 + 600 + 600)))
        self.assertEqual(g["verdict"], "fail")

    def test_no_offline_contract_means_no_offline_earnings(self):
        m = raw("sessions_offline")
        del m["offline"]
        rep = run("so", model=m, sessions="regular")
        g = goal(rep, "save1000")
        self.assertEqual((g["active_s"], g["calendar_s"]), ("1000", str(1000 + 8 * 600)))
        self.assertIn("not modelled", rep["semantics"]["offline"])

    def test_calendar_window_without_sessions_is_not_testable(self):
        g = goal(run("sessions_offline"), "save1000")
        self.assertEqual(g["verdict"], "not testable")
        self.assertIsNone(g["calendar_s"])


class Combat(unittest.TestCase):
    def side(self, hp, dmg, tau, first):
        return {"hp": F(hp), "damage": F(dmg), "interval_s": F(tau), "first_s": F(first)}

    def test_killed_enemy_does_not_land_its_next_strike(self):
        # player kills at t = 2 (hits at 1, 2); the enemy would strike at 2 and 4
        r = sim.duel(self.side(20, 4, 1, 1), self.side(5, 1, 2, 2), "player_first")
        self.assertEqual((r["outcome"], r["time_s"], r["player_hits"], r["enemy_hits"]), ("win", 1 + 1, 2, 0))
        r = sim.duel(self.side(20, 4, 1, 1), self.side(5, 1, 2, 2), "enemy_first")
        self.assertEqual((r["outcome"], r["enemy_hits"]), ("win", 1))
        r = sim.duel(self.side(1, 4, 1, 1), self.side(5, 1, 2, 2), "both")
        self.assertEqual(r["outcome"], "mutual")

    def test_ttk_and_ttd_reported(self):
        r = sim.duel(self.side(20, 4, F(3, 2), 0), self.side(5, 3, 1, 1), "player_first")
        self.assertEqual((r["hits_to_kill"], r["ttk_isolated_s"]), (2, F(3, 2)))  # immediate first hit: tau
        self.assertEqual((r["hits_to_die"], r["ttd_isolated_s"]), (7, 7))
        r = sim.duel(self.side(5, 3, 1, 1), self.side(20, 4, 1, 1), "player_first")
        self.assertEqual((r["outcome"], r["time_s"]), ("loss", 2))

    def test_rpg_policies(self):
        best = run("rpg_duel", "fight-best")
        grind = run("rpg_duel", "grind-to-level", target_level=4)
        slow = run("rpg_duel", "fight-best", skill="struggling")
        self.assertEqual(goal(best, "boss")["active_s"], "96")
        self.assertGreater(F(goal(grind, "boss")["active_s"]), F(goal(best, "boss")["active_s"]))
        self.assertGreater(F(goal(slow, "boss")["active_s"]), F(goal(best, "boss")["active_s"]))
        self.assertEqual(goal(best, "ogre")["reached"], True)  # the boss gate opens zone 2
        spike = best["spikes"]["spikes"][0]
        self.assertEqual((spike["metric"], spike["from"], spike["to"], spike["cause"]), ("slime_hits", 2, 1, "level 2"))
        self.assertEqual(best["fights"]["lost"], 0)
        boss = best["fights"]["per_enemy"]["boss"]["last"]  # level 3 + sword: attack 7 vs 60 HP; boss 6 dmg vs 28 HP
        self.assertEqual((boss["outcome"], boss["time_s"], boss["ttk_isolated_s"], boss["ttd_isolated_s"],
                          boss["enemy_hits"]), ("win", "9", "9", "10", 4))
        self.assertIsNone(best["seed"])

    def test_m04_xp_curve_in_report(self):
        cum = next(c for c in run("rpg_duel", "fight-best")["curves"] if c["id"] == "xp:cumulative")
        self.assertEqual([p[1] for p in cum["points"]], ["0", "1000", "3000", "6000", "10000", "15000"])


class Randomness(unittest.TestCase):
    def test_random_model_needs_seed_and_runs_and_reports_wilson(self):
        with self.assertRaisesRegex(ValueError, "--seed and --runs"):
            run("obby_random", "buy-next-in-order")
        rep = run("obby_random", "buy-next-in-order", seed=7, runs=50)
        self.assertEqual((rep["seed"], rep["runs"], rep["random_inputs"]), (7, 50, True))
        g = next(x for x in rep["runs_summary"]["goals"] if x["goal"] == "stage3")
        lo, hi = g["window_pass_wilson_95"]
        self.assertLessEqual(lo, g["window_pass_proportion"])
        self.assertGreaterEqual(hi, g["window_pass_proportion"])
        self.assertEqual(sum(g["window_verdicts"].values()), 50)

    def test_deterministic_model_rejects_repetition(self):
        with self.assertRaisesRegex(ValueError, "no random inputs"):
            run("lemonade_m01", "buy-next-in-order", runs=5)

    def test_wilson_interval(self):
        lo, hi = sim.wilson_interval(0, 10)
        self.assertEqual(lo, 0.0)
        self.assertAlmostEqual(hi, 0.2775327998628899, places=12)
        lo, hi = sim.wilson_interval(5, 10)
        self.assertAlmostEqual(lo + hi, 1.0, places=12)


class Provenance(unittest.TestCase):
    def test_bare_number_rejected(self):
        m = raw("zero_income")
        m["currencies"]["cash"]["start"] = 3
        with self.assertRaisesRegex(sim.ModelError, "no provenance"):
            run("z", model=m)

    def test_bad_label_rejected(self):
        m = raw("zero_income")
        m["currencies"]["cash"]["start"] = {"v": 3, "src": "guess"}
        with self.assertRaisesRegex(sim.ModelError, "provenance"):
            run("z", model=m)

    def test_strong_labels_are_not_assumptions(self):
        rep = run("m05_chain_discrete")
        self.assertEqual([a["input"] for a in rep["assumptions"]["inputs"]], ["meta.time.tick_s"])
        self.assertEqual(rep["provenance_counts"], {"EXAMPLE ASSUMPTION": 1, "published": 6})

    def test_missing_horizon_is_an_error_not_a_default(self):
        m = raw("zero_income")
        del m["run"]
        with self.assertRaisesRegex(ValueError, "horizon"):
            run("z", model=m)


class ModesAndCli(unittest.TestCase):
    def test_float_mode_is_reported(self):
        rep = run("lemonade_m01", "buy-next-in-order", mode="float")
        self.assertEqual(rep["mode"], "float")
        self.assertAlmostEqual(goal(rep, "own6")["active_s"], 465947491 / 78281250, places=12)
        self.assertLess(abs(rep["ledger"]["cash"]["residual"]), 1e-9)

    def test_cli_out_and_stdout_match_and_record_the_model_hash(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "r.json"
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.main([str(path("lemonade_m01")), "--policy", "buy-next-in-order", "--out", str(out)])
            self.assertEqual(code, 0)
            self.assertEqual(out.read_text(encoding="utf-8"), buf.getvalue())
            rep = json.loads(buf.getvalue())
            self.assertEqual(len(rep["model"]["sha256"]), 64)
            self.assertEqual(rep["model"]["revision"], "fixture-lemonade-m01-r1")

    def test_trace_can_go_to_a_file(self):
        with tempfile.TemporaryDirectory() as d:
            rep = run("lemonade_m01", "buy-next-in-order", trace_out=str(Path(d) / "t.json"))
            self.assertEqual(rep["trace"]["events"], len(json.loads((Path(d) / "t.json").read_text())))



# ---------------------------------------------------------------- J011-T11 fixes and additions

EA = "EXAMPLE ASSUMPTION"


def v(x):
    return {"v": x, "src": EA}


def mini(**extra):
    """A small continuous model: one producer of cash at 1/s, no goals unless given."""
    m = {"meta": {"revision": "t11", "event_order": ["produce", "rewards", "caps", "purchase", "unlock", "reset"],
                  "time": {"mode": "continuous"}},
         "currencies": {"cash": {"start": v(0)}},
         "producers": {"stand": {"start_owned": v(1), "produces": {"currency:cash": v(1)}}},
         "goals": [], "run": {"horizon_active_s": v(1000)}}
    m.update(extra)
    return m


class T11Fixes(unittest.TestCase):
    def test_G02_found_only_item_goal_and_save_for_do_not_crash(self):
        m = raw("rpg_duel")
        m["items"]["relic"] = {"effects": []}
        m["enemies"]["ogre"]["drops"] = [{"item": "relic", "chance": v(0)}]
        m["goals"].append({"id": "relic", "when": {"item": "relic"}})
        rep = run("r", "fight-best", model=m)
        g = goal(rep, "relic")
        self.assertEqual(g["reason"], "found only")
        self.assertIn("drop from ogre", g["detail"])
        blocked = run("r", "buy-next-in-order", model=m)  # stops blocked at 0 s: the path that used to crash
        self.assertEqual(goal(blocked, "relic")["reason"], "found only")
        m["enemies"]["wolf"]["drops"] = [{"item": "relic", "chance": v(1)}]
        rep = run("r", "save-for", model=m, target="relic")  # pursues the item by fighting what drops it
        self.assertTrue(goal(rep, "relic")["reached"])

    def test_T09G1_float_sink_absorbed_by_rounding_is_booked(self):
        m = mini(currencies={"coins": {"start": v(400000000000000000), "smallest_unit": v(1)}},
                 producers={}, items={"cheap": {"cost": {"currency": "coins", "amount": v(3)}, "effects": []}},
                 goals=[{"id": "buy", "when": {"item": "cheap"}}])
        rep = run("h3", "buy-next-in-order", model=m, mode="float")
        led = rep["ledger"]["coins"]
        self.assertEqual(led["end"], 4e17)  # the 3-coin sink did not change the float balance ...
        self.assertEqual(led["adjustments"]["float_rounding"], 3.0)  # ... and the ledger shows it
        self.assertTrue(rep["precision"]["coins"]["flagged"])
        exact = run("h3", "buy-next-in-order", model=m)
        self.assertEqual(exact["ledger"]["coins"]["end"], "399999999999999997")
        self.assertNotIn("float_rounding", exact["ledger"]["coins"]["adjustments"])

    def test_G10_docstring_lists_six_phases(self):
        self.assertIn('there is no "run" phase', sim.__doc__)
        m = raw("zero_income")
        m["meta"]["event_order"] = ["produce", "rewards", "caps", "purchase", "unlock", "reset", "run"]
        with self.assertRaises(sim.ModelError):
            run("z", model=m)


class T11Prestige(unittest.TestCase):
    def test_G01_requirement_grows_with_prestige_count_and_not_predicate(self):
        rep = run("rebirth_growing")
        self.assertEqual([(p["t_active_s"], p["basis_value"], p["award"]) for p in rep["prestige"]],
                         [("100", "100", 10), ("300", "200", 14), ("700", "400", 20)])
        self.assertEqual(goal(rep, "third")["active_s"], "700")
        self.assertFalse(goal(rep, "fourth")["reached"])  # {"not": {"prestiges": 3}} stops a fourth reset

    def test_G01_min_award_guard(self):
        m = raw("rebirth_growing")
        m["prestige"]["min_award"] = v(15)
        rep = run("rb", model=m)
        # floor(sqrt(run)) >= 15 needs run >= 225 (exact inverse), so the first two resets wait for it
        self.assertEqual([(p["t_active_s"], p["basis_value"], p["award"]) for p in rep["prestige"]],
                         [("225", "225", 15), ("450", "225", 15), ("850", "400", 20)])
        self.assertEqual(rep["semantics"]["prestige_min_award"], "15")

    def test_G09_offline_income_toward_the_basis_is_a_switch(self):
        on = run("rebirth_growing", sessions="short")
        # 50 s session + 1/2 * 1/s * min(1000, 100) offline = 100 at the next session start
        self.assertEqual([(p["t_active_s"], p["basis_value"]) for p in on["prestige"]][0], ("50", "100"))
        self.assertTrue(on["semantics"]["prestige_offline_counts_toward_basis"])
        m = raw("rebirth_growing")
        m["prestige"]["offline_counts_toward_basis"] = False
        off = run("rb", model=m, sessions="short")
        self.assertEqual([(p["t_active_s"], p["basis_value"]) for p in off["prestige"]][0], ("100", "100"))
        self.assertFalse(off["semantics"]["prestige_offline_counts_toward_basis"])


class T11Walls(unittest.TestCase):
    def test_G03_hard_walls_recorded_for_every_policy(self):
        greedy = run("idle_prestige", "greedy-roi")
        w = greedy["walls"]["hard"][0]
        self.assertEqual((w["id"], w["condition"], w["start_s"], w["end_s"], w["pursued_by_policy"]),
                         ("factory", "affordable", "131/3", "150", False))  # 50 cash reached exactly at 131/3 s
        best = run("rpg_duel", "fight-best")
        w = best["walls"]["hard"][0]
        self.assertEqual((w["id"], w["condition"], w["start_s"], w["end_s"], w["missing"]),
                         ("ogre", "beatable", "0", "96", {"unlocked": "zone2"}))

    def test_G03_rpg_save_for_keeps_earning_while_it_waits(self):
        rep = run("rpg_duel", "save-for", target="ogre")
        self.assertEqual(goal(rep, "ogre")["active_s"], "204")
        self.assertTrue(rep["walls"]["hard"][0]["pursued_by_policy"])
        self.assertGreater(rep["fights"]["won"], 1)

    def test_G08_goals_for_first_soft_wall_and_first_spike(self):
        m = raw("rpg_duel")
        m["goals"] += [{"id": "wall1", "when": {"soft_walls": v(1)},
                        "window": {"basis": "active", "min_s": v(20), "max_s": v(60)}},
                       {"id": "spike1", "when": {"spikes": ["slime_hits", v(1)]}}]
        rep = run("r", "fight-best", model=m)
        self.assertEqual(rep["walls"]["soft"]["walls"][0]["end_active_s"], "28")
        self.assertEqual((goal(rep, "wall1")["active_s"], goal(rep, "wall1")["verdict"]), ("28", "pass"))
        self.assertEqual(goal(rep, "spike1")["active_s"], "28")
        del m["analysis"]["soft_wall"]
        with self.assertRaisesRegex(ValueError, "soft-wall threshold"):
            run("r", "fight-best", model=m)


class T11Combat(unittest.TestCase):
    def test_G05_boss_attempts_with_margin_and_recovery(self):
        m = raw("rpg_duel")
        m["policies"]["boss_attempt"] = {"min_margin": v("-1/2"), "recovery_s": v(30)}
        rep = run("r", "fight-best", model=m)
        boss = rep["fights"]["per_enemy"]["boss"]
        self.assertEqual((boss["fights"], boss["lost"], boss["won"], boss["attempts_to_first_win"]), (4, 3, 1, 4))
        self.assertEqual(rep["semantics"]["boss_attempt"], {"min_margin": "-1/2", "recovery_s": "30"})
        default = run("rpg_duel", "fight-best")["fights"]["per_enemy"]["boss"]
        self.assertEqual((default["lost"], default["attempts_to_first_win"]), (0, 1))

    def test_G07_hits_to_die_ttd_and_active_when(self):
        m = raw("rpg_duel")
        m["analysis"]["spikes"] += [
            {"id": "boss_htd", "metric": "hits_to_die", "enemy": "boss", "min_change": v(1)},
            {"id": "ogre_ttd", "metric": "ttd_s", "enemy": "ogre", "active_when": {"unlocked": "zone2"}}]
        rep = run("r", "fight-best", model=m)
        hist = {x["id"]: x["history"] for x in rep["spikes"]["metrics"]}
        self.assertEqual([h["value"] for h in hist["boss_htd"]], [4, 5])  # HP 20 and 24 -> 28 at level 3, 6 dmg
        self.assertEqual(rep["spikes"]["spikes"][-1]["metric"], "boss_htd")
        self.assertEqual((hist["ogre_ttd"][0]["t_active_s"], hist["ogre_ttd"][0]["cause"]), ("96", "unlock zone2"))
        self.assertTrue(hist["ogre_ttd"][0]["segment_start"])


class T11Orders(unittest.TestCase):
    def test_G11_order_entries_with_a_count(self):
        m = mini(producers={
            "pot": {"start_owned": v(1), "produces": {"currency:cash": v(1)},
                    "cost": {"currency": "cash", "curve": {"kind": "affine", "a": v(5), "b": v(0)}}},
            "house": {"start_owned": v(0), "produces": {"currency:cash": v(10)},
                      "cost": {"currency": "cash", "curve": {"kind": "affine", "a": v(50), "b": v(0)}}}},
            policies={"order": [{"id": "pot", "until": v(3)}, "house"]},
            goals=[{"id": "house", "when": {"owned": ["house", v(1)]}}])
        rep = run("o", "buy-next-in-order", model=m)
        self.assertEqual([s["label"] for s in rep["steps"]], ["buy pot (2 owned)", "buy pot (3 owned)", "buy house (1 owned)"])

    def test_G11_zero_price_producer_does_not_stop_the_run(self):
        m = mini(producers={
            "stand": {"start_owned": v(1), "produces": {"currency:cash": v(1)}},
            "freebie": {"start_owned": v(0), "produces": {"currency:cash": v(1)},
                        "cost": {"currency": "cash", "curve": {"kind": "affine", "a": v(0), "b": v(0)}}}},
            goals=[{"id": "cash", "when": {"balance": ["cash", v(10)]}}])
        rep = run("z", "cheapest-eligible", model=m)
        self.assertEqual(rep["stop"]["reason"], "all goals reached")
        self.assertIn("freebie costs 0: at most one is bought per event instant", rep["warnings"])

    def test_T09G2_level_ups_are_events_at_their_exact_time(self):
        m = mini(currencies={"xp": {"start": v(0)}},
                 producers={"study": {"start_owned": v(1), "produces": {"currency:xp": v(10)}}},
                 levels={"currency": "xp", "max_level": v(5), "per_level": {"kind": "affine", "a": v(0), "b": v(1000)}},
                 goals=[{"id": "l4", "when": {"level": v(4)}}])
        rep = run("l", model=m)
        self.assertEqual([(s["label"], s["t_active_s"]) for s in rep["steps"]],
                         [("level 2", "100"), ("level 3", "300"), ("level 4", "600")])

    def test_T09G4_level_rewards_are_a_ledger_source(self):
        m = raw("rpg_duel")
        m["items"]["charm"] = {"effects": []}
        m["levels"]["rewards"] = [{"level": v(2), "currencies": {"gold": v(50)}, "items": ["charm"]}]
        rep = run("r", "fight-best", model=m)
        self.assertEqual(rep["ledger"]["gold"]["sources"]["level_reward:2"], "50")
        self.assertEqual(rep["ledger"]["gold"]["residual"], "0")
        self.assertIn("charm", rep["final_state"]["items"])
        self.assertLess(F(goal(rep, "sword")["active_s"]), F(goal(run("rpg_duel", "fight-best"), "sword")["active_s"]))


class T11Lean(unittest.TestCase):
    def test_G04_lean_report_is_small_and_keeps_the_timeline(self):
        full = run("rpg_duel", "fight-best", skill="struggling")
        lean = run("rpg_duel", "fight-best", skill="struggling", lean=True)
        self.assertEqual(lean["lean"]["on"], True)
        self.assertIsNone(lean["trace"])
        self.assertEqual(lean["timeline"], full["timeline"])
        self.assertEqual(lean["walls"], full["walls"])
        self.assertLess(len(lean["steps"]), len(full["steps"]))
        self.assertEqual({s["t_active_s"] for s in lean["steps"]},
                         {g["active_s"] for g in full["timeline"]} | {w["end_active_s"] for w in full["walls"]["soft"]["walls"]}
                         | {x["t_active_s"] for x in full["spikes"]["spikes"]})
        self.assertLess(len(sim.dumps(lean)), len(sim.dumps(full)) / 2)
        reset = run("idle_prestige", "greedy-roi", lean=True)
        self.assertIn("prestige", [s["kind"] for s in reset["steps"]])


# ---------------------------------------------------------------- J011-T13 additions


class T13(unittest.TestCase):
    def test_G16_lean_steps_keeps_the_first_steps_in_full(self):
        full = run("rpg_duel", "fight-best", skill="struggling")
        lean = run("rpg_duel", "fight-best", skill="struggling", lean=True, lean_steps=5)
        self.assertEqual(lean["steps"][:5], full["steps"][:5])
        self.assertEqual(lean["lean"]["first_steps_kept"], 5)
        plain = run("rpg_duel", "fight-best", skill="struggling", lean=True)
        self.assertEqual(plain["lean"]["first_steps_kept"], 0)
        self.assertLess(len(plain["steps"]), len(lean["steps"]))
        with self.assertRaisesRegex(ValueError, "--lean-steps needs --lean"):
            run("rpg_duel", "fight-best", lean_steps=5)

    def test_G17_hard_wall_goal_agrees_with_walls_hard(self):
        m = raw("idle_prestige")
        m["goals"].insert(0, {"id": "hw", "when": {"hard_wall": "factory"}})
        for pol in ("greedy-roi", "cheapest-eligible", "save-for"):
            rep = run("i", pol, model=m, target="factory" if pol == "save-for" else None)
            w = next(x for x in rep["walls"]["hard"] if x["id"] == "factory")
            self.assertEqual(goal(rep, "hw")["active_s"], w["start_s"], pol)

    def test_G18_gate_kind_on_each_hard_wall(self):
        w = run("idle_prestige", "greedy-roi")["walls"]["hard"][0]
        self.assertEqual((w["id"], w["gate"], w["via"]), ("factory", "timed", []))  # permit opens at active_s 150
        m = raw("rpg_duel")
        m["items"]["crown"] = {"cost": {"currency": "gold", "amount": v(1)}, "requires": {"defeated": "ogre"},
                               "effects": []}
        walls = {x["id"]: x for x in run("r", "fight-best", model=m)["walls"]["hard"]}
        self.assertEqual((walls["ogre"]["gate"], walls["ogre"]["via"]), ("prerequisite", []))
        self.assertEqual((walls["crown"]["gate"], walls["crown"]["via"]), ("chained", ["ogre"]))

    def test_G19_soft_walls_counted_after_a_declared_point(self):
        m = raw("rpg_duel")
        m["goals"] += [{"id": "any_wall", "when": {"soft_walls": v(1)}},
                       {"id": "wall_after_sword", "when": {"soft_walls": [v(1), {"after": {"item": "sword"}}]}}]
        rep = run("r", "fight-best", model=m)
        self.assertEqual(goal(rep, "any_wall")["active_s"], "28")  # level 2 (wait 21 s after a 7 s step)
        self.assertEqual(goal(rep, "wall_after_sword")["active_s"], "77")  # level 3: its step starts at 35 s

if __name__ == "__main__":
    unittest.main()
