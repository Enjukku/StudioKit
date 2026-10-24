"""J023 shortened job flow (knowledge/jobs/J023-flow-speed/design.md B-F) in the feature, UI screen and marketing art workflows.

Kit test (universal). Author: J023 builder · claude-opus-5-5 · high · 2026-10-24; revised by J024 test updater · claude-opus-5-5 · default ·
2026-10-24 (each J023 rule retargeted to the J024 step that holds it: knowledge/jobs/J024-flow-cuts-r2/design.md). Drives
tools/workflows/wf_harness.mjs with fake agents through the helpers of test_job_workflows; skipped when Node.js is not installed.
B: a later review round runs only the failing reviewers, the regression set and the dependents; the others are listed as carried.
C (J024: the needs step moved before G1): N1 needs tables in parallel against the plan, N2 only on a conflict, the build never re-asks.
D: limits tables, no default exchange, no sign-off; each craft confirms the merged plan in its first build hand-back.
E (J024: no proof in any size): M direction plus build is never larger than L, and no proof stage exists.
F: captures and the deterministic scripts check run on the studio-operator (Sonnet); probes run inside the builder's own run.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, full, index, run, span

FEAT, UI, MKT = "job-feature.js", "job-ui-screen.js", "job-marketing-art.js"
CRAFTS = ["animator", "ui-ux-designer", "vfx-designer", "sound-designer"]


def labels_of(out: dict, pattern: str) -> list[str]:
    return [x for x in out["labels"] if re.search(pattern, x)]


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


def total(name: str, size: str, **flags) -> int:
    return sum(run(name, full(name, stage=st, size=size, **flags))["agents"] for st in ("direction", "build"))


@unittest.skipIf(NODE is None, "Node.js not installed")
class J023FlowTests(unittest.TestCase):
    def done(self, out: dict) -> dict:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])
        return out

    # ------------------------------------------------------------------ B: re-check only what failed
    def test_feature_later_round_reruns_only_the_failed_reviewer_the_regression_set_and_dependents(self):
        # J024: the architect no longer reviews and the art-director joins only on visual_flags; round 1 = capture, qa-lead, the blocked
        # job lead (also the dependent of a visual repair); the art-director reruns after a visual repair only when it is in the chain.
        out = self.done(run(FEAT, full(FEAT, stage="build", money=False, risks=["performance"]), {"blockLabelOnce": r"^game-designer: RV-candidate-r0", "maker": "ui-ux-designer"}))
        self.assertEqual(set(labels_of(out, r"RV-candidate-r1-")), {
            "studio-operator: RV-candidate-r1-capture",      # a fresh capture: the reviews judge captures
            "qa-lead: RV-candidate-r1-qa-lead",              # the protected suite, always
            "game-designer: RV-candidate-r1-game-designer",  # raised the blocking finding
        })
        carried = out["result"]["carried"]
        for role in ("reviewer", "performance-engineer"):
            with self.subTest(role=role):
                self.assertTrue(any(c.startswith(f"carried: {role} (round 0, revision ") for c in carried), carried)
        self.assertEqual(index(out["labels"], r"^(architect|art-director):"), -1, "removed or not in this chain")
        flagged = self.done(run(FEAT, full(FEAT, stage="build", money=False), {"blockLabelOnce": r"^game-designer: RV-candidate-r0", "maker": "ui-ux-designer", "set": {"visual_flags": ["x"]}}))
        self.assertGreaterEqual(index(flagged["labels"], r"^art-director: RV-candidate-r1-art-director$"), 0, "in the chain: a visual repair reopens it")

    def test_feature_reviewer_reruns_when_the_repair_changed_code(self):
        builder = self.done(run(FEAT, full(FEAT, stage="build", money=False), {"blockLabelOnce": r"^qa-lead: RV-candidate-r0", "maker": "feature-builder"}))
        self.assertGreaterEqual(index(builder["labels"], r"^reviewer: RV-candidate-r1-reviewer$"), 0)
        self.assertEqual(index(builder["labels"], r"^game-designer: RV-candidate-r1-"), -1, "a code fix does not reopen the play review")
        rewired = self.done(run(FEAT, full(FEAT, stage="build", money=False), {"blockLabelOnce": r"^game-designer: RV-candidate-r0", "maker": "game-designer",
                                                                              "set": {"files": ["src/server/Feature.luau"]}}))
        self.assertGreaterEqual(index(rewired["labels"], r"^reviewer: RV-candidate-r1-reviewer$"), 0, "the builder's re-wire changed code")

    def test_ui_later_round_reruns_only_the_failed_reviewer_the_regression_set_and_dependents(self):
        # J024: B6-capture-…-fix → every round's capture-and-scripts run; the game-designer is no longer a reviewer, so the blocked
        # reviewer is the job lead's integrated review; no code changed, so the reviewer keeps its verdict; no art-director in this chain.
        out = self.done(run(UI, full(UI, stage="build", size="M"), {"blockLabelOnce": r"^ui-ux-designer: RV-candidate-r0", "maker": "sound-designer"}))
        self.assertEqual(set(labels_of(out, r"RV-candidate-r1-")), {
            "studio-operator: RV-candidate-r1-capture",       # the recapture after the repair
            "qa-lead: RV-candidate-r1-qa-lead",
            "ui-ux-designer: RV-candidate-r1-ui-ux-designer",   # raised the finding; also the dependent of a timing repair
        }, "no code changed, so no recheck")
        self.assertTrue(any(c.startswith("carried: reviewer (round 0") for c in out["result"]["carried"]))
        self.assertEqual(index(out["labels"], r"^(game-designer|progression-designer|art-director): RV-"), -1)

    def test_marketing_later_round_reruns_only_the_failed_reviewer_and_dependents(self):
        # J024: the game-designer is no longer a reviewer; every repair here is visual, so marketing's integrated review reruns; the
        # art-director joins only with launch (then it reruns after the visual repair).
        out = self.done(run(MKT, full(MKT, stage="build", risks=["event"]), {"blockLabelOnce": r"^live-ops-designer: RV-candidate-r0", "maker": "marketing"}))
        self.assertEqual(set(labels_of(out, r"RV-candidate-r1-")), {
            "studio-operator: RV-candidate-r1-scripts",            # the scripts check, always
            "marketing: RV-candidate-r1-marketing",                # every maker of this job is visual
            "live-ops-designer: RV-candidate-r1-live-ops-designer",
        })
        self.assertEqual(index(out["labels"], r"^(game-designer|art-director):"), -1)
        launch = self.done(run(MKT, full(MKT, stage="build", risks=["event"], launch=True), {"blockLabelOnce": r"^live-ops-designer: RV-candidate-r0", "maker": "marketing"}))
        self.assertGreaterEqual(index(launch["labels"], r"^art-director: RV-candidate-r1-art-director$"), 0)

    # ------------------------------------------------------------------ C: one needs step, before G1
    def test_feature_needs_meeting_round_one_runs_in_parallel_and_nobody_is_asked_twice(self):
        # J024: the proof meeting → N1 tables in direction, in parallel against plan revision 1; each craft is asked once before G1 and
        # builds once in build (never re-asked); N2 only for the crafts in a conflict the merge reports, then one more merge.
        listed = {"set": {"presentation": CRAFTS}}
        dirn = self.done(run(FEAT, full(FEAT, stage="direction", money=False, numbers=False), dict(listed, timeline=True, uniform=True)))
        tables = [t for t in dirn["timeline"] if re.search(r": N1-", t["label"])]
        self.assertEqual(len(tables), 5)
        self.assertLess(max(t["start"] for t in tables), min(t["end"] for t in tables), "every table is written against the same revision at once")
        self.assertEqual(labels_of(dirn, r"^animator:"), ["animator: N1-needs-animator"], "the animator states its timings once")
        self.assertEqual(index(dirn["labels"], r": N2-"), -1, "no conflict: no round 2")
        build = self.done(run(FEAT, full(FEAT, stage="build", money=False, numbers=False), listed))
        self.assertEqual(labels_of(build, r"^animator:"), ["animator: B4-animation"], "build never re-asks: one run")
        self.assertEqual(index(build["labels"], r"N1-|N2-|needs"), -1)
        conflict = run(FEAT, full(FEAT, stage="direction", money=False, numbers=False),
                       dict(listed, set=dict(listed["set"], open_conflicts=[{"about": "N1-row-1", "roles": ["animator", "vfx-designer"], "why": "w"}])))
        self.assertEqual(set(labels_of(conflict, r": N2-")), {"animator: N2-animator", "vfx-designer: N2-vfx-designer"}, "round 2: only the crafts in the conflict")
        self.assertEqual(labels_of(conflict, r"^game-designer: D3-merge"), ["game-designer: D3-merge", "game-designer: D3-merge-n2"])
        self.assertEqual(index(conflict["labels"], r"-r3|N3-"), -1)

    def test_ui_needs_meeting_holds_the_cue_list_and_world_beats_with_no_second_storyboard_round(self):
        # J024: C2-needs-r1 → the sound and VFX needs tables in direction, against the D1 plan's beat list, in parallel; the build asks
        # each craft once (its own build run) and the Figma build reads the merged beat list and tables.
        effects = {"set": {"ui_effects": True}}
        out = self.done(run(UI, full(UI, stage="direction", size="M"), dict(effects, timeline=True, uniform=True, dump=r"D1-plan|vfx-designer: N1")))
        self.assertEqual(index(out["labels"], r"storyboard"), -1)
        for role in ("sound-designer", "vfx-designer"):
            with self.subTest(role=role):
                self.assertEqual(labels_of(out, rf"^{role}:"), [f"{role}: N1-needs-{role}"], "one ask before G1")
        self.assertLess(span(out, r"^sound-designer: N1-")["start"], span(out, r"^vfx-designer: N1-")["end"], "round 1 in parallel")
        self.assertIn("beat list", brief(out, r"D1-plan"))
        self.assertIn("world-to-HUD beats", brief(out, r"vfx-designer: N1"))
        build = self.done(run(UI, full(UI, stage="build", size="M"), dict(effects, dump=r"B1-figma")))
        for role in ("sound-designer", "vfx-designer"):
            with self.subTest(role=role, stage="build"):
                self.assertEqual(len(labels_of(build, rf"^{role}: ")), 1, "the build does not re-ask")
        figma_brief = brief(build, r"B1-figma")
        self.assertIn("motion/storyboard.md", figma_brief)
        self.assertIn("/needs/", figma_brief)

    # ------------------------------------------------------------------ D: lighter direction
    def test_feature_direction_has_limits_sheets_no_exchange_and_no_sign_off(self):
        # J024: D1-<lead> + D3-synthesis → D1 plan, the N1 limits tables, one merge; the confirmation moves to PLAN-CONFIRM in each
        # craft's first build hand-back, asked once.
        out = self.done(run(FEAT, full(FEAT, stage="direction"), {"dump": r"N1-limits-architect"}))
        self.assertEqual(out["labels"][0], "game-designer: D1-plan")
        self.assertEqual(set(out["labels"][1:-1]), {"architect: N1-limits-architect", "progression-designer: N1-limits-progression-designer"})
        self.assertEqual(out["labels"][-1], "game-designer: D3-merge")
        self.assertEqual(index(out["labels"], r": D2-|D3-sign-|D3-synthesis"), -1)
        self.assertIn("architect/plan.md", brief(out, r"N1-limits-architect"))
        build = self.done(run(FEAT, full(FEAT, stage="build"), {"blockLabelOnce": r"^reviewer: RV-candidate-r0", "maker": "feature-builder", "dump": r"^feature-builder: "}))
        mine = [d for d in build["dumps"] if d["label"].startswith("feature-builder: ")]
        self.assertGreaterEqual(len(mine), 2)
        self.assertIn("PLAN-CONFIRM", mine[0]["prompt"], "the first build hand-back confirms the merged plan")
        self.assertTrue(all("PLAN-CONFIRM" not in d["prompt"] for d in mine[1:]), "asked once")

    def test_feature_incompatibility_in_the_first_hand_back_is_needs_decision(self):
        # J024: P2-needs in the proof → a craft's first build hand-back; an incompatibility there stops the build before the builder.
        out = run(FEAT, full(FEAT, stage="build"), {"statusLabel": r"^progression-designer: B2-tables", "status": "needs-decision"})
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(index(out["labels"], r"B7-build|: RV-"), -1)

    def test_ui_exchange_runs_only_for_a_conflict_between_proposals(self):
        # J024: D1-art-director + D2 exchange → the art-director's N1 limits table only with newLook; no exchange without a conflict; N2
        # only for the crafts in a conflict the merge reports, then the second merge.
        clean = self.done(run(UI, full(UI, stage="direction")))
        self.assertEqual(index(clean["labels"], r": D2-|D3-sign-|: N2-|art-director"), -1)
        look = self.done(run(UI, full(UI, stage="direction", newLook=True), {"dump": r"art-director: N1"}))
        self.assertIn("needs/art-director.md", brief(look, r"art-director: N1"))
        conflict = run(UI, full(UI, stage="direction"), {"set": {"open_conflicts": [{"about": "back button", "roles": ["feature-builder", "architect"], "why": "w"}]}})
        self.assertEqual(set(labels_of(conflict, r": N2-")), {"feature-builder: N2-feature-builder", "architect: N2-architect"})
        self.assertGreater(index(conflict["labels"], r"^ui-ux-designer: D3-merge-n2$"), index(conflict["labels"], r": N2-"))

    def test_marketing_direction_has_limits_sheets_and_the_confirmation_moves_to_the_next_stage(self):
        # J024: no proof and no green light; the art-director writes a limits table only with launch, and confirms the merged plan in its
        # first build hand-back (PLAN-CONFIRM).
        out = self.done(run(MKT, full(MKT, stage="direction")))
        self.assertEqual(index(out["labels"], r": D2-|D3-sign-|D3-resolution|art-director"), -1)
        self.assertEqual(run(MKT, full(MKT, stage="proof"))["status"], "blocked")
        launch = self.done(run(MKT, full(MKT, stage="direction", launch=True)))
        self.assertGreaterEqual(index(launch["labels"], r"^art-director: N1-limits-art-director$"), 0)
        build = self.done(run(MKT, full(MKT, stage="build", launch=True), {"dump": r"^art-director: RV-candidate-r0-"}))
        self.assertIn("PLAN-CONFIRM", brief(build, r"^art-director: RV-candidate-r0-"))

    # ------------------------------------------------------------------ E: no proof; M is never larger than L
    def test_feature_m_build_runs_no_proof_calls(self):
        # J024: M build < L proof + build → no proof stage in any size; the build is the same for M and L; M direction + build ≤ L.
        medium = self.done(run(FEAT, full(FEAT, stage="build", size="M")))
        self.assertEqual(index(medium["labels"], r": (P3-|P4-|PR-)|prototype"), -1)
        proof = run(FEAT, full(FEAT, stage="proof"))
        self.assertEqual((proof["status"], proof["agents"]), ("blocked", 0))
        large = self.done(run(FEAT, full(FEAT, stage="build")))
        self.assertEqual(medium["labels"], large["labels"], "the build stage is the same for both sizes")
        self.assertLessEqual(total(FEAT, "M", money=True, numbers=True), total(FEAT, "L", money=True, numbers=True))

    def test_ui_m_direction_has_no_look_options(self):
        # J024: the ui-ux-designer always writes the D1 plan; M has one direction and no target images (no prompts step); L has them.
        out = self.done(run(UI, full(UI, stage="direction", size="M"), {"dump": r": D1-plan"}))
        self.assertEqual(out["labels"][0], "ui-ux-designer: D1-plan")
        self.assertFalse(any("write every image prompt first" in d["prompt"] for d in out["dumps"]), "no style targets in M")
        self.assertIn("no look options and no target images", brief(out, r"D1-plan"))
        large = self.done(run(UI, full(UI, stage="direction", size="L"), {"dump": r": D1-plan"}))
        self.assertIn("write every image prompt first", brief(large, r"D1-plan"))
        self.assertEqual(index(self.done(run(UI, full(UI, stage="build", size="M")))["labels"], r"prototype|PR-r"), -1)

    def test_marketing_m_build_runs_no_green_light(self):
        # J024: B1-render → B1-final renders the option the owner chose at G1; no green light in any size; M direction + build ≤ L.
        medium = self.done(run(MKT, full(MKT, stage="build", size="M"), {"dump": r"B1-final"}))
        self.assertEqual(index(medium["labels"], r"P1-value|P2-light|RV-greenlight"), -1)
        self.assertIn("the option the owner chose at G1", brief(medium, r"B1-final"))
        self.assertEqual(run(MKT, full(MKT, stage="proof"))["agents"], 0)
        self.assertLessEqual(total(MKT, "M"), total(MKT, "L"))

    # ------------------------------------------------------------------ F: right model, short agents
    def test_feature_captures_and_probes_run_on_the_studio_operator(self):
        # J024: the separate B1-probes run is gone; the builder runs the plan's Studio probes inside its own build run; the only
        # studio-operator run is the capture-and-scripts run per round, on Sonnet, and every capture is on the studio-operator.
        out = self.done(run(FEAT, full(FEAT, stage="build"), {"set": {"probes": ["RemoteEvent order holds under a burst"]}, "dump": r"^studio-operator: |B7-build"}))
        self.assertEqual(labels_of(out, r"^studio-operator: "), ["studio-operator: RV-candidate-r0-capture"])
        self.assertEqual(index(out["labels"], r"probes"), -1)
        for label in labels_of(out, r"capture|P4-play"):
            self.assertTrue(label.startswith("studio-operator: "), label)
        self.assertTrue(all("model: sonnet" in d["prompt"] for d in out["dumps"] if d["label"].startswith("studio-operator: ")))
        self.assertIn("run the plan's Studio probe inside this run", brief(out, r"B7-build"))

    def test_ui_builder_takes_no_routine_captures(self):
        # J024: B2-implement → B4-build (implement and integrate).
        out = self.done(run(UI, full(UI, stage="build"), {"dump": r"feature-builder: B4-build"}))
        text = brief(out, r"B4-build")
        self.assertIn("take no captures", text)
        self.assertNotIn("one Studio capture per state", text)

    def test_marketing_scripts_check_is_not_an_opus_run(self):
        # The workflow runtime cannot run a command, so the deterministic check stays an agent run, on Sonnet.
        # J024: marketing now has its own integrated review (RV-…-marketing) after the scripts; the scripts are never marketing's run;
        # the maker freezes in B1-final (B4-crops is folded into it).
        out = self.done(run(MKT, full(MKT, stage="build"), {"dump": r"RV-candidate-r0-scripts|B1-final"}))
        scripts = index(out["labels"], r"^studio-operator: RV-candidate-r0-scripts$")
        self.assertGreaterEqual(scripts, 0)
        self.assertEqual(index(out["labels"], r"^marketing: RV-candidate-r0-scripts"), -1)
        self.assertGreater(index(out["labels"], r"^marketing: RV-candidate-r0-marketing$"), scripts)
        self.assertIn("model: sonnet", brief(out, r"scripts"))
        self.assertIn("freeze the candidate", brief(out, r"B1-final"), "the maker freezes; the operator only measures")


if __name__ == "__main__":
    unittest.main()
