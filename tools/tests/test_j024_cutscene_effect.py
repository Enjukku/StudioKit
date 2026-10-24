"""J024 flow-cut tests for the cutscene and effect workflows, with fake agents (no tokens).

Kit test (universal). Author: J024 builder A · claude-opus-5-5 · default · 2026-10-24. Binding design: knowledge/jobs/J024-flow-cuts-r2/design.md.
Runs .agents/workflows/jobs/job-cutscene.js and job-effect.js under tools/workflows/wf_harness.mjs; skipped when Node is not installed.
Covers: §1 no proof stage and no G2; §2 one run per craft, no rough labels; §3 direction = D1 plan, N1 needs and limits tables from the
plan only (12-row cap, omitted line), one merge, N2 only for the crafts in a conflict the merge reports, a new cast stops direction;
§4 capture and scripts in one studio-operator run (a FAIL stops the other reviews), the reviewer table with each conditional reviewer on
and off, sound sync in the job lead's integrated review from cue_log, selective recheck with the new chain; §5a capped repair briefs;
§6 run-count ceilings; §7 the newLook, ui and performance args. Every test fails on the J023 scripts.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import JOBS, NODE, full, index, run, span

CUT = JOBS / "job-cutscene.js"
FX = JOBS / "job-effect.js"
ROUGH = re.compile(r"rough|temp|proto|blocking|greybox|proxy|strip|board|animatic|first-spec|check-?in|polish|lock|value-r", re.I)


def cut(scenario: dict | None = None, **changes) -> dict:
    a = dict(newLook=False, ui=False)
    a.update(changes)
    out = run(CUT, full("job-cutscene.js", **a), scenario)
    if out["violation"]:
        raise AssertionError(f"harness violation: {out['violation']}")
    return out


def fx(scenario: dict | None = None, **changes) -> dict:
    a = dict(animated=False)
    a.update(changes)
    out = run(FX, full("job-effect.js", **a), scenario)
    if out["violation"]:
        raise AssertionError(f"harness violation: {out['violation']}")
    return out


def matching(labels: list[str], pattern: str) -> list[str]:
    return [x for x in labels if re.search(pattern, x)]


def reviewers(labels: list[str], tag: str) -> set[str]:
    """The reviewer ids that ran in one review round, from labels like 'role: RV-candidate-r1-<id>'."""
    return {m.group(1) for x in labels for m in [re.search(rf": RV-{tag}-(.+)$", x)] if m}


def dump(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dump matches {pattern}: {out['labels']}")
    return hits[0]


def block(prompt: str, key: str) -> list[str]:
    """The '  - ' items of one list field of a brief (inputs:, findings:, changed_parts:)."""
    lines = prompt.splitlines()
    start = next((i for i, x in enumerate(lines) if x.startswith(key)), None)
    if start is None:
        return []
    out = []
    for x in lines[start + 1:]:
        if not x.startswith("  - "):
            break
        out.append(x[4:])
    return out


def findings(n: int, maker: str) -> list[dict]:
    return [{"id": f"F{i}", "class": "blocking", "maker_role": maker, "where": "w", "expected": f"e{i}", "observed": f"o{i}",
             "evidence": f"ev{i}.png", "smallest_fix": "f"} for i in range(1, n + 1)]


@unittest.skipIf(NODE is None, "Node.js not installed")
class NoProofTests(unittest.TestCase):
    """§1: direction → G1 → build → G3; the proof stage is refused before any agent."""

    def test_proof_stage_is_refused_before_any_agent(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            for size in ("L", "M"):
                with self.subTest(name, size=size):
                    out = go(stage="proof", size=size)
                    self.assertEqual((out["status"], out["agents"]), ("blocked", 0), out["outcome"])
                    self.assertIn("no proof stage (J024): direction → G1 → build → G3", out["outcome"])

    def test_direction_leads_to_build_and_no_phase_or_owner_line_names_g2_or_a_proof(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            out = go({"dump": "."}, stage="direction")
            with self.subTest(name):
                self.assertIn("calls stage build", out["result"]["outcome"])
                self.assertNotIn("stage proof", out["result"]["outcome"])
                self.assertFalse([p for p in out["meta"]["phases"] if re.search(r"proof|G2", p["title"] + p["detail"], re.I)])
                self.assertFalse([x for x in out["result"]["owner_confirmed"] if "(G2" in x or "at G2" in x], out["result"]["owner_confirmed"])


@unittest.skipIf(NODE is None, "Node.js not installed")
class DirectionTests(unittest.TestCase):
    """§3: D1 plan → N1 needs and limits (in parallel, plan only) → merge; N2 only on a conflict the merge reports."""

    def test_cutscene_direction_is_plan_needs_merge(self):
        out = cut({"timeline": True}, stage="direction")
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertEqual(labels[0], "film-director: D1-plan")
        self.assertEqual(labels[-1], "film-director: M1-merge")
        n1 = {x.split(": N1-")[1] for x in matching(labels, ": N1-")}
        self.assertEqual(n1, {"animator", "environment-designer", "vfx-designer", "sound-designer", "architect"})
        d1, merge = span(out, "D1-plan"), span(out, "M1-merge")
        for x in matching(labels, ": N1-"):
            s = span(out, re.escape(x))
            self.assertGreater(s["start"], d1["end"], x)
            self.assertLess(s["end"], merge["start"], x)
        self.assertEqual(out["result"]["build_args"], {"ui": False})

    def test_effect_direction_is_plan_needs_merge(self):
        out = fx(stage="direction")
        self.assertEqual(out["labels"], ["vfx-designer: D1-plan", "sound-designer: N1-sound-designer", "feature-builder: N1-feature-builder", "vfx-designer: M1-merge"])

    def test_m_and_l_differ_only_in_direction(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                big, mid = go({"dump": "D1-plan"}, stage="direction", size="L"), go({"dump": "D1-plan"}, stage="direction", size="M")
                self.assertIn("2-3 options", dump(big, "D1-plan"))
                self.assertIn("one direction inside the approved style", dump(mid, "D1-plan"))
                self.assertEqual(big["labels"], mid["labels"])
                self.assertEqual(go(stage="build", size="L")["labels"], go(stage="build", size="M")["labels"])

    def test_needs_briefs_read_only_the_plan_and_keep_the_table_cap(self):
        for name, go, plan in (("cutscene", cut, "beat-sheet.md@rev"), ("effect", fx, "contract-timeline.md@rev")):
            out = go({"dump": ": N1-"}, stage="direction", newLook=True)
            self.assertTrue(out["dumps"], name)
            for d in out["dumps"]:
                with self.subTest(name, label=d["label"]):
                    p = d["prompt"]
                    ins = [x for x in block(p, "inputs:") if "job-card.md" not in x]
                    self.assertEqual(len(ins), 1, ins)
                    self.assertIn(plan, ins[0])
                    self.assertNotRegex("\n".join(block(p, "inputs:")), r"needs/n\d-|proposal|options\.md")
                    for must in ("at most 12 rows", "omitted:", "templates/jobs/needs-table.md", "Read only the plan file"):
                        self.assertIn(must, p)

    def test_second_needs_round_runs_only_on_a_reported_conflict_and_only_for_its_crafts(self):
        cases = (("cutscene", cut, ["vfx-designer", "sound-designer"]), ("effect", fx, ["sound-designer", "feature-builder"]))
        for name, go, pair in cases:
            with self.subTest(name, conflict=False):
                out = go(stage="direction")
                self.assertFalse(matching(out["labels"], r": N2-|M2-merge"), out["labels"])
            with self.subTest(name, conflict=True):
                c = {"about": "cue E3 onset", "why": "w", "between": pair, "rows": ["V3", "S2"]}
                out = go({"set": {"open_conflicts": [c]}, "dump": ": N2-"}, stage="direction")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(sorted(x.split(": N2-")[1] for x in matching(out["labels"], ": N2-")), sorted(pair))
                self.assertEqual(out["labels"][-1].split(": ")[1], "M2-merge")
                self.assertFalse(matching(out["labels"], r"N3-|M3-"))   # never more than 2 needs rounds
                p = dump(out, ": N2-")
                self.assertIn('"rows":["V3","S2"]', p)
                self.assertEqual(len([x for x in block(p, "inputs:") if "job-card.md" not in x]), 1)

    def test_a_new_cast_stops_direction_with_a_linked_character_job(self):
        out = cut({"newCast": True}, stage="direction")
        self.assertEqual(out["status"], "needs-decision")
        self.assertIn("character job", out["result"]["outcome"])
        self.assertEqual(out["labels"], ["film-director: D1-plan"])

    def test_cutscene_ui_craft_is_switched_by_the_plan(self):
        off, on = cut(stage="direction"), cut({"set": {"ui_needed": True}}, stage="direction")
        self.assertEqual(index(off["labels"], r"N1-ui-ux-designer"), -1)
        self.assertGreaterEqual(index(on["labels"], r"N1-ui-ux-designer"), 0)
        self.assertEqual(on["result"]["build_args"], {"ui": True})
        self.assertGreaterEqual(index(cut(stage="build", ui=True)["labels"], r"ui-ux-designer: B5-ui"), 0)
        self.assertEqual(index(cut(stage="build", ui=False)["labels"], r"ui-ux-designer"), -1)
        missing = cut(stage="build", ui=None)
        self.assertEqual((missing["status"], missing["agents"]), ("blocked", 0))
        self.assertTrue(any(r.startswith("ui:") for r in missing["result"]["required"]))

    def test_effect_needs_and_limits_crafts_are_switched_by_args_and_risks(self):
        def n1(**kw):
            return {x.split(": N1-")[1] for x in matching(fx(stage="direction", **kw)["labels"], ": N1-")}
        self.assertEqual(n1(), {"sound-designer", "feature-builder"})
        self.assertIn("animator", n1(animated=True))
        self.assertIn("game-designer", n1(risks=["danger-area"]))
        self.assertIn("game-designer", n1(risks=["frequent-effect"]))
        self.assertNotIn("game-designer", n1(risks=["server-result", "paid-random", "event", "performance"]))
        self.assertIn("art-director", n1(newLook=True))
        self.assertIn("quick-builder", n1(small=True))


@unittest.skipIf(NODE is None, "Node.js not installed")
class BuildTests(unittest.TestCase):
    """§2 and §4.1-4.3: one run per craft in dependency order; capture and scripts in one studio-operator run."""

    def test_cutscene_build_runs_each_craft_once_in_dependency_order(self):
        out = cut({"timeline": True}, stage="build", ui=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        pre = out["labels"][:index(out["labels"], r": RV-")]
        roles = [x.split(":")[0] for x in pre]
        self.assertEqual(sorted(roles), sorted(["animator", "environment-designer", "vfx-designer", "sound-designer", "ui-ux-designer", "feature-builder", "film-director"]))
        self.assertLess(span(out, "animator: B1")["end"], span(out, "vfx-designer: B3")["start"])
        self.assertLess(span(out, "vfx-designer: B3")["end"], span(out, "sound-designer: B4")["start"])
        self.assertLess(span(out, "feature-builder: PLY")["end"], span(out, "film-director: SCN")["start"])

    def test_effect_build_runs_each_craft_once_in_dependency_order(self):
        out = fx(stage="build", animated=True)
        self.assertEqual(out["labels"][:4], ["animator: B1-animator", "vfx-designer: B2-vfx", "sound-designer: B3-sound", "feature-builder: W-candidate"])
        self.assertEqual(out["labels"][4], "studio-operator: RV-candidate-r0-scripts")

    def test_no_rough_pass_in_any_stage(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            for stage in ("direction", "build", "repair"):
                for size in ("L", "M"):
                    with self.subTest(name, stage=stage, size=size):
                        extra = {"animated": True} if go is fx else {}
                        out = go(stage=stage, size=size, **extra)
                        self.assertEqual(out["status"], "done", out["outcome"])
                        self.assertFalse([x for x in out["labels"] if ROUGH.search(x)], out["labels"])

    def test_capture_and_scripts_is_one_studio_operator_run_and_a_fail_stops_the_other_reviews(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                out = go({"blockLabelOnce": r"studio-operator: RV-candidate-r0-scripts", "maker": "vfx-designer"}, stage="build")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(reviewers(out["labels"], "candidate-r0"), {"scripts"})
                self.assertFalse(matching(out["labels"], r"CAP-|RECAP|event-captures"), out["labels"])
                for tag in ("candidate-r0", "candidate-r1"):
                    self.assertEqual(len(matching(out["labels"], rf"^studio-operator: RV-{tag}-scripts$")), 1)

    def test_table_writers_confirm_the_merged_plan_in_their_first_build_hand_back(self):
        out = cut({"dump": r"B3-vfx|B1-animator"}, stage="build")
        self.assertIn('"plan confirmed: vfx-designer rev N"', dump(out, "B3-vfx"))
        out = fx({"dump": r"B3-sound"}, stage="build")
        self.assertIn('"plan confirmed: sound-designer rev N"', dump(out, "B3-sound"))


@unittest.skipIf(NODE is None, "Node.js not installed")
class ReviewerTableTests(unittest.TestCase):
    """§4.4: who reviews, with each conditional reviewer on and off."""

    def test_cutscene_round_0_reviewers(self):
        base = {"scripts", "qa-lead", "reviewer", "film-director"}
        self.assertEqual(reviewers(cut(stage="build")["labels"], "candidate-r0"), base)
        self.assertEqual(reviewers(cut(stage="build", newLook=True)["labels"], "candidate-r0"), base | {"art-director"})
        self.assertEqual(reviewers(cut(stage="build", risks=["performance"])["labels"], "candidate-r0"), base | {"performance-engineer"})
        ev = cut({"dump": r"RV-candidate-r0-scripts"}, stage="build", risks=["event"])
        self.assertEqual(reviewers(ev["labels"], "candidate-r0"), base | {"live-ops-designer"})
        self.assertGreater(index(ev["labels"], "live-ops-designer"), index(ev["labels"], "film-director: RV"))
        self.assertIn("event capture set", dump(ev, "RV-candidate-r0-scripts"))
        self.assertEqual(cut(stage="build")["result"]["skipped_slots"],
                         ["live-ops event review: risks does not name event", "performance-engineer review: risks does not name performance"])

    def test_effect_round_0_reviewers(self):
        base = {"scripts", "vfx-designer", "reviewer"}
        self.assertEqual(reviewers(fx(stage="build")["labels"], "candidate-r0"), base)
        for risk in ("server-result", "paid-random"):
            self.assertEqual(reviewers(fx(stage="build", risks=[risk])["labels"], "candidate-r0"), base | {"qa-lead"}, risk)
        for risk in ("danger-area", "frequent-effect"):
            out = fx({"dump": r"RV-candidate-r0-scripts"}, stage="build", risks=[risk])
            self.assertEqual(reviewers(out["labels"], "candidate-r0"), base, risk)
            self.assertIn({"danger-area": "PF-04", "frequent-effect": "PF-10"}[risk], dump(out, "RV-candidate-r0-scripts"))
        self.assertEqual(reviewers(fx(stage="build", risks=["performance"])["labels"], "candidate-r0"), base | {"performance-engineer"})
        self.assertEqual(reviewers(fx(stage="build", risks=["event"])["labels"], "candidate-r0"), base | {"live-ops-designer"})
        self.assertEqual(reviewers(fx(stage="build", newLook=True)["labels"], "candidate-r0"), base | {"art-director"})

    def test_removed_reviewers_never_review(self):
        gone = r"^(sound-designer|game-designer|architect|animator|feature-builder|progression-designer): RV-"
        self.assertFalse(matching(cut(stage="build", newLook=True, risks=["event", "performance"])["labels"], gone))
        self.assertFalse(matching(fx(stage="build", animated=True, newLook=True, risks=["server-result", "danger-area", "event"])["labels"], gone + r"|^vfx-designer: RV-.*(?<!vfx-designer)$"))

    def test_visual_flags_bring_the_art_director_into_that_round(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                out = go({"set": {"visual_flags": ["shot 3 peak value 0.98 > 0.92"]}, "dump": r"art-director: RV"}, stage="build")
                self.assertIn("art-director", reviewers(out["labels"], "candidate-r0"))
                self.assertIn("shot 3 peak value 0.98 > 0.92", dump(out, r"art-director: RV"))

    def test_performance_is_a_universal_risk_token(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                self.assertEqual(go(stage="direction", risks=["performance"])["status"], "done")
                self.assertEqual(index(go(stage="direction", risks=["performance"])["labels"], "performance-engineer"), -1)
                self.assertGreaterEqual(index(go(stage="repair", risks=["performance"])["labels"], "performance-engineer: RV-repair-r0"), 0)
                self.assertEqual(go(stage="build", risks=["speed"])["status"], "blocked")

    def test_cutscene_new_look_is_a_required_boolean_that_needs_l(self):
        for stage in ("direction", "build", "repair"):
            out = cut(stage=stage, newLook=None)
            self.assertEqual((out["status"], out["agents"]), ("blocked", 0), stage)
            self.assertTrue(any(r.startswith("newLook:") for r in out["result"]["required"]))
        out = cut(stage="direction", size="M", newLook=True)
        self.assertEqual((out["status"], out["agents"]), ("blocked", 0))
        self.assertGreaterEqual(index(cut(stage="direction", newLook=True)["labels"], "art-director: N1-art-director"), 0)

    def test_sound_sync_is_in_the_job_leads_integrated_review(self):
        line = "E3 t=1.200 vfx=1.201 sound=1.215"
        for name, go, lead in (("cutscene", cut, "film-director"), ("effect", fx, "vfx-designer")):
            with self.subTest(name):
                out = go({"set": {"cue_log": [line]}, "dump": rf"{lead}: RV-candidate-r0"}, stage="build")
                p = dump(out, rf"{lead}: RV-candidate-r0")
                self.assertIn(line, p)
                self.assertIn("sound sync from cue_log", p)
                self.assertIn("look_check.py", p)
                self.assertEqual(index(out["labels"], r"sound-designer: RV-"), -1)


@unittest.skipIf(NODE is None, "Node.js not installed")
class RepairTests(unittest.TestCase):
    """§4.5 selective recheck with the new chain; §5a capped repair briefs."""

    def test_cutscene_recheck_runs_the_blocker_the_regression_set_and_the_dependents(self):
        out = cut({"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "vfx-designer"}, stage="build")
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "qa-lead", "film-director"})
        self.assertEqual([c.split(" (")[0] for c in out["result"]["carried"]], ["carried: reviewer"])
        look = cut({"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "vfx-designer"}, stage="build", newLook=True)
        self.assertEqual(reviewers(look["labels"], "candidate-r1"), {"scripts", "qa-lead", "film-director", "art-director"})
        code = cut({"blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "feature-builder"}, stage="build", newLook=True)
        self.assertEqual(reviewers(code["labels"], "candidate-r1"), {"scripts", "qa-lead", "reviewer", "film-director"})
        self.assertEqual([c.split(" (")[0] for c in code["result"]["carried"]], ["carried: art-director"])

    def test_effect_recheck_runs_the_blocker_the_regression_set_and_the_dependents(self):
        out = fx({"blockLabelOnce": r"vfx-designer: RV-candidate-r0", "maker": "sound-designer"}, stage="build", risks=["server-result"])
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "vfx-designer", "qa-lead"})
        self.assertEqual([c.split(" (")[0] for c in out["result"]["carried"]], ["carried: reviewer"])

    def test_repair_briefs_are_capped(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                out = go({"set": {"findings": findings(12, "vfx-designer"), "files": ["content/vfx/a/spec.json@rev3"]},
                          "dump": r"FIX-candidate-r0-vfx-designer"}, stage="build")
                self.assertEqual(out["status"], "needs-decision", out["outcome"])
                p = dump(out, r"FIX-candidate-r0-vfx-designer")
                shown = block(p, "findings:")
                self.assertEqual(len(shown), 10)
                self.assertEqual(shown[0], '{"id":"F1","expected":"e1","observed":"o1","evidence":"ev1.png"}')
                self.assertIn("omitted: F11, F12 (lower rank, sent next round if still open)", p)
                self.assertTrue(any("@rev3" in x for x in block(p, "changed_parts:")), block(p, "changed_parts:"))
                self.assertIn("protected:", p)
                self.assertNotIn("/reviews/", "\n".join(block(p, "inputs:")))
                self.assertLessEqual(len(p.split()), 1500)

    def test_rechecking_reviewer_gets_its_own_findings_and_the_changed_parts(self):
        for name, go, lead in (("cutscene", cut, "film-director"), ("effect", fx, "vfx-designer")):
            with self.subTest(name):
                out = go({"blockLabelOnce": rf"{lead}: RV-candidate-r0", "maker": "vfx-designer", "dump": rf"{lead}: RV-candidate-r1"}, stage="build")
                p = dump(out, rf"{lead}: RV-candidate-r1")
                self.assertEqual(len(block(p, "previous_findings:")), 1)
                self.assertTrue(block(p, "changed_parts:"))
                self.assertNotIn("direction.md", "\n".join(block(p, "inputs:")))

    def test_a_dead_agent_in_the_new_steps_is_never_a_pass(self):
        for name, go, label in (("cutscene", cut, "N1-vfx-designer"), ("cutscene", cut, "M1-merge"), ("effect", fx, "N1-sound-designer"), ("effect", fx, "M1-merge")):
            with self.subTest(name, label=label):
                out = go({"nullLabel": label}, stage="direction")
                self.assertEqual(out["status"], "failed", out["outcome"])
                self.assertNotIn("g1", out["result"])

    def test_images_and_studio_are_required_in_build_and_repair_only(self):
        for name, go in (("cutscene", cut), ("effect", fx)):
            with self.subTest(name):
                self.assertEqual(go(stage="direction", images=None, studioId=None)["status"], "done")
                for stage in ("build", "repair"):
                    req = go(stage=stage, images=None, studioId=None)["result"]["required"]
                    self.assertEqual(sorted(r.split(":")[0] for r in req), ["images", "studioId"], req)
                # J023 asked for them in proof; J024 has no proof stage, so the call is refused, not asked for args.
                out = go(stage="proof", images=None, studioId=None)
                self.assertNotIn("required", out["result"])
                self.assertIn("no proof stage (J024)", out["result"]["outcome"])


@unittest.skipIf(NODE is None, "Node.js not installed")
class RunCountTests(unittest.TestCase):
    """§6: minimum agent runs (clean fakes, risks [], cheapest flags), direction + build; M never above L."""

    def total(self, go, size, **kw) -> int:
        return sum(go(stage=s, size=size, **kw)["agents"] for s in ("direction", "build"))

    def test_cutscene_run_count(self):
        big, mid = self.total(cut, "L"), self.total(cut, "M")
        self.assertEqual(big, 17)
        self.assertLessEqual(big, 20)
        self.assertLessEqual(mid, big)

    def test_effect_run_count(self):
        self.assertEqual(self.total(fx, "L"), 10)
        self.assertEqual(self.total(fx, "L", animated=True), 12)
        self.assertLessEqual(self.total(fx, "M", animated=True), self.total(fx, "L", animated=True))


if __name__ == "__main__":
    unittest.main()
